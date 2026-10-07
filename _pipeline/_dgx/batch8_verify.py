# -*- coding: utf-8 -*-
"""batch8_verify.py —— 批次8（长境名篇40首）语料核对：按（作者, 首句指纹）取原文。

仿 batch7_verify.py；扩展：加载 诗经/蒙学/楚辞 等集（条目用 content 键、dict 形 json），
author 为空（诗经/乐府/古诗十九首）时跳过作者过滤。首条命中打印全文，其余截断。
"""
import glob, io, json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
import zhconv

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'chinese-poetry'))
N = lambda s: zhconv.convert(s, 'zh-hans')

CANDS = [
    ('蒹葭', '', '蒹葭苍苍白露为霜'),
    ('采薇(节选)', '', '昔我往矣杨柳依依'),
    ('桃夭', '', '桃之夭夭灼灼其华'),
    ('无衣', '', '岂曰无衣与子同袍'),
    ('十五从军征', '', '十五从军征八十始得归'),
    ('迢迢牵牛星', '', '迢迢牵牛星皎皎河汉女'),
    ('涉江采芙蓉', '', '涉江采芙蓉兰泽多芳草'),
    ('木兰辞', '', '唧唧复唧唧木兰当户织'),
    ('兵车行', '杜甫', '车辚辚马萧萧'),
    ('燕歌行', '高适', '汉家烟尘在东北'),
    ('走马川行奉送封大夫出师西征', '岑参', '走马川行雪海边'),
    ('古从军行', '李颀', '白日登山望烽火'),
    ('老将行', '王维', '少年十五二十时'),
    ('宣州谢朓楼饯别校书叔云', '李白', '弃我去者昨日之日不可留'),
    ('山石', '韩愈', '山石荦确行径微'),
    ('蜀相', '杜甫', '丞相祠堂何处寻'),
    ('登岳阳楼', '杜甫', '昔闻洞庭水今上岳阳楼'),
    ('旅夜书怀', '杜甫', '细草微风岸危樯独夜舟'),
    ('咏怀古迹其三', '杜甫', '群山万壑赴荆门'),
    ('左迁至蓝关示侄孙湘', '韩愈', '一封朝奏九重天'),
    ('长沙过贾谊宅', '刘长卿', '三年谪宦此栖迟'),
    ('登柳州城楼寄漳汀封连四州', '柳宗元', '城上高楼接大荒'),
    ('九日齐山登高', '杜牧', '江涵秋影雁初飞'),
    ('马嵬其二', '李商隐', '海外徒闻更九州'),
    ('无题昨夜星辰', '李商隐', '昨夜星辰昨夜风'),
    ('观猎', '王维', '风劲角弓鸣'),
    ('渔翁', '柳宗元', '渔翁夜傍西岩宿'),
    ('滕王阁诗', '王勃', '滕王高阁临江渚'),
    ('书愤', '陆游', '早岁那知世事艰'),
    ('金陵驿其一', '文天祥', '草合离宫转夕晖'),
    ('戏答元珍', '欧阳修', '春风疑不到天涯'),
    ('病起书怀', '陆游', '病骨支离纱帽宽'),
    ('水龙吟登建康赏心亭', '辛弃疾', '楚天千里清秋'),
    ('摸鱼儿更能消', '辛弃疾', '更能消几番风雨'),
    ('满庭芳山抹微云', '秦观', '山抹微云'),
    ('永遇乐落日熔金', '李清照', '落日熔金暮云合璧'),
    ('青玉案凌波不过', '贺铸', '凌波不过横塘路'),
    ('摸鱼儿雁丘词', '元好问', '直教生死相许'),
    ('鹧鸪天重过阊门', '贺铸', '重过阊门万事非'),
    ('洞仙歌冰肌玉骨', '苏轼', '冰肌玉骨'),
]

SUBS = ('全唐诗', '御定全唐詩', '水墨唐诗', '宋词', '五代诗词', '元曲', '纳兰性德',
        '诗经', '楚辞', '蒙学', '四书五经', '论语', '幽梦影', '曹操诗集')

files = []
for sub in SUBS:
    files += glob.glob(os.path.join(ROOT, sub, '**', '*.json'), recursive=True)
files = [f for f in files if 'author' not in os.path.basename(f)
         and 'images' not in f.lower() and 'loader' not in f.lower()
         and os.path.getsize(f) < 60 * 1024 * 1024]
print('files: %d' % len(files), file=sys.stderr)

ents = []
for f in files:
    try:
        d = json.load(io.open(f, encoding='utf-8'))
    except Exception:
        continue
    items = d if isinstance(d, list) else (list(d.values()) if isinstance(d, dict) else [])
    for e in items:
        if not isinstance(e, dict):
            continue
        p = e.get('paragraphs') or e.get('content') or e.get('para') or []
        if isinstance(p, str):
            p = [p]
        if (e.get('title') or e.get('rhythmic') or e.get('chapter')) and p:
            ents.append((e.get('title') or e.get('rhythmic') or e.get('chapter') or '',
                         e.get('author') or e.get('poet') or '', p))
print('entries: %d' % len(ents), file=sys.stderr)

out = []
for label, author, fp in CANDS:
    hits = []
    for t, a, p in ents:
        if author and N(author) not in N(a):
            continue
        txt = N(''.join(p))
        for ch in '，。、？！　 ：；?!,.':
            txt = txt.replace(ch, '')
        if fp in txt:
            hits.append(N(''.join(p)))
    out.append('### %s [%s] %d hits' % (label, author or '佚', len(hits)))
    seen = set()
    for i, h in enumerate(hits[:3]):
        k = h[:40]
        if k in seen:
            continue
        seen.add(k)
        out.append('  ' + (h if i == 0 else h[:60]))
    if not hits:
        out.append('  !! NOT FOUND')
io.open(os.path.join(os.path.dirname(__file__), 'batch8_corpus.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('done %d candidates' % len(CANDS))
