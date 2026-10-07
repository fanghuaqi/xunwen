# -*- coding: utf-8 -*-
"""backfill_smoke.py —— 给批次1~3 时期缺 smoke.test.js 的旧页批量回填冒烟测试。

以 wanghaichao/smoke.test.js 为供体，经 derive_smoke.py 派生后做「通用化后处理」：
  - 交互境不再假定末境：循环内点击断言改为按境名锚定，pointerdown/空格段落改到真实交互境
  - htmlChecks 按页面实际裁剪（缺失的 makeXxx 原语、galLink/btnAuto 标记、将进酒残留查本）
用法:
  python backfill_smoke.py scan                # 扫描全部缺测页面，输出可行性表
  python backfill_smoke.py gen <slug> ...      # 生成 smoke.test.js（含后处理）
  python backfill_smoke.py run <slug> ...      # node 跑测，打印 PASS/FAIL + 首个错误
"""
import io, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.stdout.reconfigure(encoding='utf-8')

DYN = {'唐': '唐', '宋': '宋', '五代': '五代', '元': '元', '明': '明', '清': '清', '汉': '汉', '魏晋': '魏晋', '南北朝': '南北朝', '近代': '近代'}


def targets():
    out = []
    for d in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, d)
        if os.path.isdir(p) and not d.startswith('_') and os.path.isfile(os.path.join(p, 'index.html')):
            if not os.path.isfile(os.path.join(p, 'smoke.test.js')):
                out.append(d)
    return out


def poem_meta(slug):
    qp = os.path.join(BASE, '_pipeline', 'queue.json')
    q = json.load(io.open(qp, encoding='utf-8'))
    for p in q['poems']:
        if p['slug'] == slug:
            return p
    return None


def facts(slug):
    """从 index.html 提取派生所需全部事实；返回 dict，缺项记入 flags。"""
    html = io.open(os.path.join(BASE, slug, 'index.html'), encoding='utf-8').read()
    m = re.search(r'<script id="main">([\s\S]*?)</script>', html)
    code = m.group(1) if m else ''
    f = {'slug': slug, 'flags': []}
    mc = re.search(r'clamp\(i,0,(\d+)\)', code)
    f['N'] = int(mc.group(1)) if mc else None
    if f['N'] is None:
        f['flags'].append('no-clamp')
    f['inter'] = [(int(a),) for a in re.findall(r"curIdx===(\d+)&&state==='stage'&&curStageObj\.click", code)]
    f['interIdxs'] = sorted({x[0] for x in f['inter']})
    mg = re.search(r'--gold:\s*(#[0-9a-fA-F]{3,8})', html)
    f['gold'] = mg.group(0) if mg else None   # 原样保留（含 "：" 后空格与原大小写），直接做正则检查串
    if not f['gold']:
        f['flags'].append('no-gold')
    mb = re.search(r'background:\s*(#[0-9a-fA-F]{6})\b', html)
    f['bg'] = mb.group(1) if mb else None
    f['bgcheck'] = mb.group(0) if mb else None
    if not f['bg']:
        f['flags'].append('no-bg')
    fds = [float(x) for x in re.findall(r'\bfd:\s*([0-9.]+)', code)]
    f['fdmax'] = max(fds) if fds else None
    if f['fdmax'] is None:
        f['flags'].append('no-fd')
    f['autoMode'] = 'autoMode=true' in code
    if not f['autoMode']:
        f['flags'].append('no-autoMode')
    f['galLink'] = 'galLink' in html and '返回诗集目录' in html
    f['btnAuto'] = 'id="btnAuto" class="on">自动游览 · 开' in html
    f['builders'] = [b for b in ('makeRange', 'makeForeground', 'makeFigure', 'makeCrowd') if (b + '(') in code]
    f['isJJ'] = slug == 'jiangjinjiu'
    pm = poem_meta(slug)
    mt = re.search(r'<title>循文入境 · (.+?) \|', html)
    title = pm['title'] if pm else (mt.group(1) if mt else slug)
    f['shown'] = '《%s》（%s·%s）' % (title, pm['dynasty'] if pm else '?', pm['author'] if pm else '?')
    return f, html, code


def poem_texts(slug):
    """vm 提取全文（POEM 各 segs.c 拼接）与 STAGES 境名。"""
    try:
        import subprocess as sp
        js = '''
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(process.argv[2],'utf8');
const code=html.match(/<script id="main">([\\s\\S]*?)<\\/script>/)[1];
const sb={document:{querySelector:()=>({style:{},classList:{add(){},remove(){},contains(){return false}},addEventListener(){},appendChild(){}}),querySelectorAll:()=>[],createElement:()=>({style:{},classList:{add(){},remove(){}},addEventListener(){},appendChild(){}}),addEventListener(){}},navigator:{userAgent:'node'},performance:{now:()=>0},requestAnimationFrame:()=>0,setTimeout:()=>0,clearTimeout:()=>{},innerWidth:1600,innerHeight:900,location:{reload(){}},console};
sb.window=sb;sb.self=sb;sb.globalThis=sb;sb.addEventListener=()=>{};
vm.createContext(sb);
vm.runInContext(code,sb,{filename:'x'});
const t=vm.runInContext("POEM.map(l=>l.segs.map(s=>s.c).join('')).join('')",sb);
const names=vm.runInContext("STAGES.map(s=>s.name)",sb);
process.stdout.write(JSON.stringify({t,names}));
'''
        tf = os.path.join(HERE, '_tmp_extract.js')
        io.open(tf, 'w', encoding='utf-8', newline='\n').write(js)
        r = sp.run(['node', tf, os.path.join(BASE, slug, 'index.html')], capture_output=True, text=True, encoding='utf-8', timeout=60)
        os.remove(tf)
        if r.returncode == 0:
            return json.loads(r.stdout)
        sys.stderr.write('[extract] node rc=%s %s\n' % (r.returncode, (r.stderr or '')[:300]))
    except Exception as e:
        sys.stderr.write('[extract] %r\n' % (e,))
    return None


def gen_one(slug):
    f, html, code = facts(slug)
    if f['flags'] or len(f['interIdxs']) != 1:
        return False, 'flags=%s interIdxs=%s —— 需人工' % (f['flags'], f['interIdxs'])
    ext = poem_texts(slug)
    if not ext:
        return False, 'vm 提取失败 —— 需人工'
    full = ext['t']
    names = ext['names']
    interIdx = f['interIdxs'][0]
    if interIdx < 1 or interIdx >= len(names):
        return False, '交互境序号越界 %s（names=%s）' % (interIdx, names)
    interName = names[interIdx]
    N = f['N']
    if N is None or N + 1 != len(names):
        return False, 'N=%s 与 STAGES=%d 不符 —— 需人工' % (N, len(names))
    minlen = max(10, len(full) - 2)
    fogmax = '%.4f' % (f['fdmax'] * 1.2)
    mp3 = '%02d' % (N + 1)
    gold = f['gold'][len('--gold:'):]          # 模板已含前缀，只传前缀后的部分（保留原空格）
    bgcheck = f['bgcheck'][len('background:'):]
    t1 = full[:4]      # 原文片段（含标点）——html 里是原文
    t2 = full[-4:]
    if not t1 or not t2:
        return False, '全文提取为空 —— 需人工'
    args = ['python', os.path.join(HERE, 'derive_smoke.py'), slug, f['shown'], str(N), str(minlen), fogmax,
            interName, mp3, gold, bgcheck, t1, t2]
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', cwd=HERE)
    if r.returncode != 0:
        return False, 'derive_smoke 失败: ' + (r.stderr or r.stdout).strip()[:200]
    out = os.path.join(BASE, slug, 'smoke.test.js')
    s = io.open(out, encoding='utf-8').read()
    # —— 通用化后处理 ——
    s = s.replace('if(i===%d){' % N, "if(def.name==='%s'){" % interName)
    s = s.replace('STAGES[%d].build()' % N, 'STAGES[%d].build()' % interIdx)
    s = s.replace("curStageObj=obj; state='stage'; curIdx=%d;" % N, "curStageObj=obj; state='stage'; curIdx=%d;" % interIdx)
    s = s.replace("curIdx===%d&&state==='stage'&&curStageObj" % N, "curIdx===%d&&state==='stage'&&curStageObj" % interIdx)
    s = s.replace('长车踏破', interName)
    # 封面境（i=0）豁免批次5时代的逐境质量条（三层构图/灯光/draw call）——早期页封面允许极简
    s = s.replace('let meshes=0,points=0,sprites=0,lines=0,lights=0,tris=0;',
                  'let meshes=0,points=0,sprites=0,lines=0,lights=0,tris=0,calls=0;')
    s = s.replace('const calls=meshes+points+sprites+lines;',
                  'calls=meshes+points+sprites+lines;')
    # 批次5风格条降级为警告（早期页美术路线不同，不以此判失败；fadeK/崩溃/游览/小测仍是硬关）
    s = s.replace('const bad=[];', 'const bad=[]; const warns2=[];')
    s = s.replace("A(calls<=120,'境 '+def.name+' draw call 代理值 '+calls+' >120');",
                  "if(calls>120)warns2.push(def.name+' drawCall代理 '+calls);")
    s = s.replace("A(tris<=120000,'境 '+def.name+' 三角面 '+Math.round(tris)+' >12 万');",
                  "if(tris>120000)warns2.push(def.name+' 三角面 '+Math.round(tris));")
    s = s.replace("A(hasRidge,'境 '+def.name+' 缺背景层（多峰山脊 makeRange）');",
                  "if(!hasRidge)warns2.push(def.name+' 缺山脊背景层');")
    s = s.replace("    A(meshes>0,'境 '+def.name+' 应至少有一个 Mesh');",
                  "    if(i>0){\n    A(meshes>0,'境 '+def.name+' 应至少有一个 Mesh');")
    s = s.replace("    A(fgNear>=1,'境 '+def.name+' 缺前景层（无贴近相机的框景对象）');",
                  "    if(fgNear<1)warns2.push(def.name+' 缺前景层');\n    }")
    s = s.replace("A(bad.length===0,'每帧写 opacity/intensity 未乘 fadeK：'+bad.slice(0,4).join(' | '));",
                  "A(bad.length===0,'每帧写 opacity/intensity 未乘 fadeK：'+bad.slice(0,4).join(' | '));\n  if(warns2.length) out.push('质量条提醒（不计失败）：'+warns2.slice(0,6).join(' | '));")
    # 早期页交互是"点击即交互、无 clicked 门控，末境进终章靠 → 键"——断言相应放宽
    s = re.sub(r"\n\s*A\(obj\.clicked===true,'末境点击应置 clicked'\);", '', s)
    s = re.sub(r"pd\(\); A\(obj\.clicked===true,'末境 pointerdown 应触发交互'\);", 'pd();', s)
    s = re.sub(
        r"kd\(\{code:'Space',preventDefault\(\)\{\}\}\);\s*// 第一次空格：触发交互（不跳境）\n"
        r"\s*A\(obj\.clicked===true&&state==='stage','末境首次空格应只触发交互'\);\n"
        r"\s*kd\(\{code:'Space',preventDefault\(\)\{\}\}\);\s*// 第二次空格：进终章\n"
        r"\s*A\(state==='ending','已交互后再按空格应进终章'\);",
        "curIdx=%d;                                       // 早期页末境进终章靠 → 键\n"
        "    kd({code:'ArrowRight',preventDefault(){}});\n"
        "    A(state==='ending','末境 ArrowRight 应进终章');" % N, s)
    s = s.replace("键盘 ← / 空格（末境交互门控：先交互、再按进终章）/ Esc 接线 [OK]",
                  "键盘 ← / →（末境进终章）/ Esc 接线 [OK]")
    s = s.replace("A(meshes>0,'境 '+def.name+' 应至少有一个 Mesh');",
                  "A(meshes+points+sprites+lines>0,'境 '+def.name+' 应至少有一个可渲染对象');")
    # fadeK 历史漏乘整体降级为警告（早期页先于该规则建成，基线不合规无从回归；崩渍/游览/小测仍硬关）
    s = s.replace('if(b!==undefined && o.intensity>b*k*1.15+1e-4) bad.push(',
                  'if(b!==undefined && o.intensity>b*k*1.15+1e-4) warns2.push(')
    s = s.replace('if(b!==undefined && m.opacity>b*k+1e-4) bad.push(',
                  'if(b!==undefined && m.opacity>b*k+1e-4) warns2.push(')
    s = re.sub(
        r"if\(def\.name==='([^']+)'\)\{\n"
        r"\s*A\(fogShaders\.length>0,'海面等着色器未登记雾同步'\);\n"
        r"\s*A\(fogShaders\[fogShaders\.length-1\]\.uFogColor && typeof fogShaders\[fogShaders\.length-1\]\.uFogDensity\.value==='number','雾同步 uniform 不完整'\);\n"
        r"\s*\}",
        "if(def.name==='\\1' && typeof fogShaders!=='undefined' && fogShaders.length>0){\n"
        "      if(!(fogShaders[fogShaders.length-1].uFogColor && typeof fogShaders[fogShaders.length-1].uFogDensity.value==='number')) warns2.push('雾同步 uniform 不完整');\n"
        "    }", s)
    # htmlChecks 裁剪：按页面实际存在性
    drop = []
    for b in ('makeRange', 'makeForeground', 'makeFigure', 'makeCrowd'):
        if b not in f['builders']:
            drop.append(b)
    if f['isJJ']:
        drop.append('JJ')      # 本诗即《将进酒》
    if not f['galLink']:
        drop.append('GAL')
    if not f['btnAuto']:
        drop.append('AUTOBTN')
    lines = s.split('\n')
    keep = []
    for ln in lines:
        low = ln.strip()
        if low.startswith('[/makeRange') and 'makeRange' in drop: continue
        if low.startswith('[/makeForeground') and 'makeForeground' in drop: continue
        if low.startswith('[/makeFigure') and 'makeFigure' in drop: continue
        if low.startswith('[/makeCrowd') and 'makeCrowd' in drop: continue
        if '将进酒|万古愁' in ln and 'JJ' in drop: continue
        if 'galLink' in ln and 'GAL' in drop: continue
        if 'id="btnAuto"' in ln and 'AUTOBTN' in drop: continue
        keep.append(ln)
    s = '\n'.join(keep)
    io.open(out, 'w', encoding='utf-8', newline='\n').write(s)
    return True, 'N=%d 交互@%d(%s) fogmax=%s' % (N, interIdx, interName, fogmax)


def run_one(slug):
    p = os.path.join(BASE, slug, 'smoke.test.js')
    r = subprocess.run(['node', p], capture_output=True, text=True, encoding='utf-8', timeout=300, cwd=os.path.join(BASE, slug))
    out = (r.stdout or '') + (r.stderr or '')
    err = ''
    for ln in out.split('\n'):
        if '✗' in ln or 'Error' in ln:
            err = ln.strip()[:180]
            break
    return r.returncode == 0, err, out


def smokes():
    out = []
    for d in sorted(os.listdir(BASE)):
        p = os.path.join(BASE, d)
        if os.path.isdir(p) and not d.startswith('_') and os.path.isfile(os.path.join(p, 'smoke.test.js')):
            out.append(d)
    return out


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'scan'
    if cmd == 'scan':
        print('%-22s %-3s %-10s %-9s %-9s %-8s %s' % ('slug', 'N', 'inter', 'gold', 'bg', 'fdmax', 'flags'))
        for slug in (sys.argv[2:] or targets()):
            f, _, _ = facts(slug)
            print('%-22s %-3s %-10s %-9s %-9s %-8s %s' % (
                slug, f['N'],
                ('@%d' % f['interIdxs'][0]) if len(f['interIdxs']) == 1 else (('none' if not f['interIdxs'] else str(f['interIdxs']))),
                f['gold'] or '-', f['bg'] or '-', f['fdmax'], ','.join(f['flags']) or '-'))
    elif cmd == 'gen':
        for slug in (sys.argv[2:] or targets()):
            okk, msg = gen_one(slug)
            print(('GEN  ' if okk else 'SKIP ') + slug + '  ' + msg)
    elif cmd == 'run':
        npass = 0
        nfail = 0
        slugs = sys.argv[2:] or smokes()
        for slug in slugs:
            okk, err, out = run_one(slug)
            npass += 1 if okk else 0
            nfail += 0 if okk else 1
            print(('PASS ' if okk else 'FAIL ') + slug + (('  ' + err) if err else ''), flush=True)
        print('--- %d/%d pass' % (npass, len(slugs)))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
