# -*- coding: utf-8 -*-
"""batch7_verify.py —— 批次7（诗40首）语料核对：按（作者, 首句指纹）取原文。"""
import glob, io, json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
import zhconv

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'chinese-poetry'))
N = lambda s: zhconv.convert(s, 'zh-hans')

CANDS = [
    ('望月怀远', '张九龄', '海上生明月天涯共此时'),
    ('过故人庄', '孟浩然', '故人具鸡黍邀我至田家'),
    ('望洞庭湖赠张丞相', '孟浩然', '八月湖水平涵虚混太清'),
    ('终南望余雪', '祖咏', '终南阴岭秀积雪浮云端'),
    ('题破山寺后禅院', '常建', '清晨入古寺初日照高林'),
    ('塞下曲其二', '卢纶', '林暗草惊风将军夜引弓'),
    ('行军九日思长安故园', '岑参', '强欲登高去无人送酒来'),
    ('塞上听吹笛', '高适', '雪净胡天牧马还月明羌笛戍楼间'),
    ('题金陵渡', '张祜', '金陵津渡小山楼一宿行人自可愁'),
    ('陇西行', '陈陶', '誓扫匈奴不顾身五千貂锦丧胡尘'),
    ('剑客', '贾岛', '十年磨一剑霜刃未曾试'),
    ('马诗其五', '李贺', '大漠沙如雪燕山月似钩'),
    ('南园其五', '李贺', '男儿何不带吴钩收取关山五十州'),
    ('咸阳城东楼', '许浑', '一上高城万里愁蒹葭杨柳似汀洲'),
    ('江楼感旧', '赵嘏', '独上江楼思渺然月光如水水如天'),
    ('登乐游原', '李商隐', '向晚意不适驱车登古原'),
    ('贾生', '李商隐', '宣室求贤访逐臣贾生才调更无伦'),
    ('锦瑟', '李商隐', '锦瑟无端五十弦一弦一柱思华年'),
    ('遣怀', '杜牧', '落魄江湖载酒行楚腰纤细掌中轻'),
    ('题乌江亭', '杜牧', '胜败兵家事不期包羞忍耻是男儿'),
    ('过华清宫', '杜牧', '长安回望绣成堆山顶千门次第开'),
    ('台城', '韦庄', '江雨霏霏江草齐六朝如梦鸟空啼'),
    ('渡汉江', '宋之问', '岭外音书断经冬复历春'),
    ('行宫', '元稹', '寥落古行宫宫花寂寞红'),
    ('菊花', '元稹', '秋丛绕舍似陶家遍绕篱边日渐斜'),
    ('溪居即事', '崔道融', '篱外谁家不系船春风吹入钓鱼湾'),
    ('桃花溪', '张旭', '隐隐飞桥隔野烟石矶西畔问渔船'),
    ('辛夷坞', '王维', '木末芙蓉花山中发红萼'),
]

files = []
for sub in ('全唐诗', '御定全唐詩', '水墨唐诗', '宋词', '宋诗', '金元明清诗', '五代诗词'):
    files += glob.glob(os.path.join(ROOT, sub, '**', '*.json'), recursive=True)
files = [f for f in files if 'author' not in os.path.basename(f) and os.path.getsize(f) < 60 * 1024 * 1024]
print('files: %d' % len(files), file=sys.stderr)
ents = []
for f in files:
    try:
        d = json.load(io.open(f, encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(d, list):
        continue
    for e in d:
        if not isinstance(e, dict):
            continue
        p = e.get('paragraphs') or e.get('para') or []
        if (e.get('title') or e.get('rhythmic')) and p:
            ents.append((e.get('title') or e.get('rhythmic'), e.get('author') or '', p))
print('entries: %d' % len(ents), file=sys.stderr)

out = []
for label, author, fp in CANDS:
    hits = []
    for t, a, p in ents:
        if N(author) not in N(a):
            continue
        txt = N(''.join(p)).replace('，', '').replace('。', '').replace('、', '').replace('？', '').replace('！', '').replace('　', '').replace(' ', '').replace('：', '').replace('；', '')
        if fp in txt:
            hits.append(N(''.join(p)))
    out.append('### %s [%s] %d hits' % (label, author, len(hits)))
    seen = set()
    for h in hits[:3]:
        k = h[:40]
        if k in seen:
            continue
        seen.add(k)
        out.append('  ' + h[:170])
    if not hits:
        out.append('  !! NOT FOUND')
io.open(os.path.join(os.path.dirname(__file__), 'batch7_corpus.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
print('done %d candidates' % len(CANDS))
