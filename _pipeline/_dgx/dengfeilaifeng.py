# -*- coding: utf-8 -*-
"""dengfeilaifeng.py —— 《登飞来峰》（宋·王安石，no.238，大漠金戈·孤峰塔影变体）生成配置
诗眼「不畏浮云遮望眼，自缘身在最高层」：孤峰顶一座七层宝塔、山腰浮云翻涌、东方旭日将升。
末境点击最高层 → 近前塔檐沉下（身已上升）、浮云向两侧散开、日轮跃出云海、金光铺满画面。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='dengfeilaifeng', title='登飞来峰', dyn='宋 · 王安石', brand_author='王安石',
    gold_rgb='184,144,90',
    root=""":root{
  --gold:#b8905a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(184,144,90,.3);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(24,16,9', 1),
        ('rgba(4,6,11', 'rgba(12,8,5', 2),
        ('rgba(6,9,16', 'rgba(24,16,9', 1),
        ('rgba(3,5,9', 'rgba(8,5,3', 1),
        ('#0b101c', '#181009', 1),
        ('#6f664f', '#7a6a50', 1),
        ('#5a5340', '#6a5a44', 1),
    ],
    tip='轻点最高层 / 按空格 —— 浮云散尽，旭日跃出云海',
    hint='← → 键或空格逐境游览 · 末境可点击最高层：身升塔顶，浮云四散、旭日东升',
    cover_read='登飞来峰。宋，王安石。飞来山上千寻塔，闻说鸡鸣见日升。不畏浮云遮望眼，自缘身在最高层。',
    cover_p1='两重意境，随诗句次第展开：飞来峰上矗立着千寻高塔，听说鸡鸣时分便能看见日出；不怕浮云遮住远望的视线，只因为已站在最高的一层。',
    cover_p2='边读诗，边登上孤峰塔顶：看清晨雾与浮云如何散开，也就读懂了这份高瞻远瞩的胸襟。',
    end_h2='浮云 · 望眼', cn_word='两',
    words_js="['再登一次，塔顶看日','初识半山，尚需共读','渐入佳境，再诵几遍','塔影渐高，云海渐开','已识登高望远意','不畏浮云，身在高层']",
    sky_atmo='0x332414',
)

POEM_JS = io.open(os.path.join(_here, 'dengfeilaifeng_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'dengfeilaifeng_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'dengfeilaifeng_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'dengfeilaifeng_stages.js'), encoding='utf-8').read()
