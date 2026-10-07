# -*- coding: utf-8 -*-
"""tts_audit.py —— 老诗注音 + TTS 多音字机械预扫。

产出 _pipeline/_dgx/tts_audit_report.json，每首一份：
  title/reads            —— TTS 实际朗读的文本（00 题名 + 各 read）
  segs                   —— 页面逐字注音（c + pinyin）
  pinyinFlags            —— 页面注音与 pypinyin 的差异，分三桶：
                              HETERO（异读字，需裁决用哪个读音）
                              TONE （声调不同，单读音字——可能是错或轻声惯例）
                              BASE （声/韵不同且非异读解释——大概率页面错）
  subCandidates          —— 题名+朗读文本中的异读字（edge-tts 可能读错 → tts.json sub 候选）
用法: python tts_audit.py scan [slug ...]   # 无 slug = 全部无 tts.json 的非 legacy 页
"""
import io, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.stdout.reconfigure(encoding='utf-8')

LEGACY = {'jiangjinjiu', 'shuidiao-getou', 'guancanghai', 'guanju', 'shengshengman'}

EXTRACT_JS = '''
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(process.argv[2],'utf8');
const code=html.match(/<script id="main">([\\s\\S]*?)<\\/script>/)[1];
const sb={document:{querySelector:()=>({style:{},classList:{add(){},remove(){},contains(){return false},textContent:''},addEventListener(){},appendChild(){}}),querySelectorAll:()=>[],createElement:()=>({style:{},classList:{add(){},remove(){}},addEventListener(){},appendChild(){}}),addEventListener(){}},navigator:{userAgent:'node'},performance:{now:()=>0},requestAnimationFrame:()=>0,setTimeout:()=>0,clearTimeout:()=>{},innerWidth:1600,innerHeight:900,location:{reload(){}},console};
sb.window=sb;sb.self=sb;sb.globalThis=sb;sb.addEventListener=()=>{};
vm.createContext(sb);
vm.runInContext(code,sb,{filename:'x'});
const segs=vm.runInContext("POEM.map(l=>({name:l.name,segs:l.segs.map(s=>({c:s.c,p:s.p}))}))",sb);
const reads=vm.runInContext("POEM.map(l=>l.read)",sb);
process.stdout.write(JSON.stringify({segs,reads}));
'''

TONE_MARKS = str.maketrans('āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ', 'aaaaeeeeiiiioooouuuuüvvv')


def base(syl):
    return syl.translate(TONE_MARKS).lower().replace('ü', 'v').replace('ū', 'u')


def targets():
    out = []
    for d in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, d)
        if d in LEGACY:
            continue
        if os.path.isdir(p) and not d.startswith('_') and os.path.isfile(os.path.join(p, 'index.html')) \
                and not os.path.isfile(os.path.join(p, 'tts.json')):
            out.append(d)
    return out


def extract(slug):
    js = io.open(os.path.join(HERE, '_tmp_ttsx.js'), 'w', encoding='utf-8', newline='\n')
    js.write(EXTRACT_JS)
    js.close()
    r = subprocess.run(['node', os.path.join(HERE, '_tmp_ttsx.js'), os.path.join(BASE, slug, 'index.html')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=60)
    os.remove(os.path.join(HERE, '_tmp_ttsx.js'))
    if r.returncode != 0:
        return None
    return json.loads(r.stdout)


def audit(slug):
    from pypinyin import pinyin as py, Style
    from pypinyin.core import PINYIN_DICT as CHAR_DICT

    def readings(ch):
        v = CHAR_DICT.get(ord(ch))
        return v.split(',') if v else []
    data = extract(slug)
    if not data:
        return {'slug': slug, 'error': 'vm 提取失败'}
    html = io.open(os.path.join(BASE, slug, 'index.html'), encoding='utf-8').read()
    mt = re.search(r'<title>循文入境 · (.+?) \|', html)
    title = mt.group(1) if mt else slug
    title_read = title + '。'
    reads = [r for r in data['reads'] if r]

    speak_text = title_read + ''.join(reads)
    # —— 异读字候选（TTS 可能读错）——
    sub_cands = []
    for ch in sorted({c for c in speak_text if '\u4e00' <= c <= '\u9fff'}):
        rd = readings(ch)
        if len(rd) > 1:   # 有多种读音
            ctxs = [speak_text[max(0, i - 2):i + 3] for i, c in enumerate(speak_text) if c == ch][:3]
            sub_cands.append({'ch': ch, 'readings': rd, 'ctx': ctxs})

    # —— 页面注音核对 ——
    flags = {'HETERO': [], 'TONE': [], 'BASE': []}
    for li, line in enumerate(data['segs']):
        for si, seg in enumerate(line['segs']):
            c, pys = seg['c'], seg['p']
            han = [(i, ch) for i, ch in enumerate(c) if '\u4e00' <= ch <= '\u9fff']
            if len(han) != len(pys):
                flags['BASE'].append({'line': li, 'seg': si, 'why': '拼音数 %d ≠ 汉字数 %d' % (len(pys), len(han)),
                                      'c': c, 'pys': pys})
                continue
            for (i, ch), pg in zip(han, pys):
                pg = pg.strip()
                rd = readings(ch)
                rd_b = {base(r) for r in rd}
                if ch in '一不':
                    if base(pg) not in ('yi', 'bu'):
                        flags['BASE'].append({'line': li, 'seg': si, 'ch': ch, 'page': pg, 'pypy': rd, 'ctx': c})
                    continue
                if base(pg) in rd_b:
                    if pg not in rd and len({r.translate(TONE_MARKS) for r in rd}) > 1:
                        flags['HETERO'].append({'line': li, 'seg': si, 'ch': ch, 'page': pg, 'pypy': rd, 'ctx': c})
                    continue
                if base(pg) == base(rd[0]):
                    flags['TONE'].append({'line': li, 'seg': si, 'ch': ch, 'page': pg, 'pypy': rd, 'ctx': c})
                else:
                    flags['BASE'].append({'line': li, 'seg': si, 'ch': ch, 'page': pg, 'pypy': rd, 'ctx': c})
    n = sum(len(v) for v in flags.values())
    return {'slug': slug, 'title': title, 'reads': reads, 'segs': data['segs'],
            'subCandidates': sub_cands, 'pinyinFlags': flags, 'flagCount': n}


def main():
    slugs = sys.argv[2:] or targets()
    rep = {}
    for s in slugs:
        rep[s] = audit(s)
        f = rep[s]
        print('%-22s flags=%-3d subCand=%-2d %s' % (s, f.get('flagCount', -1), len(f.get('subCandidates', [])),
                                                    ('ERR:' + f['error']) if 'error' in f else ''))
    out = os.path.join(HERE, 'tts_audit_report.json')
    io.open(out, 'w', encoding='utf-8', newline='\n').write(json.dumps(rep, ensure_ascii=False, indent=1))
    print('report ->', out)


if __name__ == '__main__':
    main()
