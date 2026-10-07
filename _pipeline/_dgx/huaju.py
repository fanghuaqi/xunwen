# -*- coding: utf-8 -*-
"""huaju.py —— 《画菊》（宋·郑思肖，no.236，宣纸留白）生成配置
诗眼「宁可枝头抱香死」：北风可见（墨色风线横扫），菊丛随风剧烈摇动却始终扎根枝头不落；
末境点击北风 → 风势暴涨、花瓣绕花盘旋而不离枝、题字「抱香枝头」。
宣纸留白：纸底、淡墨远山、篱菊一点暖黄；全页不设水、不用金色辉光（浅色赛道必改清单已逐项过）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='huaju', title='画菊', dyn='宋 · 郑思肖', brand_author='郑思肖',
    gold_rgb='58,68,68',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#3a4444; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(58,68,68,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(233,226,208', 1),
        ('rgba(4,6,11', 'rgba(212,202,176', 2),
        ('rgba(6,9,16', 'rgba(233,226,208', 1),
        ('rgba(3,5,9', 'rgba(236,230,214', 1),
        ('#0b101c', '#f6f1e1', 1),
        ('#6f664f', '#8a8268', 1),
        ('#5a5340', '#8d8571', 1),
        ('0x0a1526', '0xe6dfcc', 4),
    ],
    tip='轻点北风 / 按空格 —— 北风横扫，菊花抱香枝头不落',
    hint='← → 键或空格逐境游览 · 末境可点击北风：风势暴涨，花瓣绕枝不落',
    cover_read='画菊。宋，郑思肖。花开不并百花丛，独立疏篱趣未穷。宁可枝头抱香死，何曾吹落北风中。',
    cover_p1='两重意境，随诗句次第展开：菊花开时不挤进百花丛，只独立在稀疏的篱边，意趣无穷；它宁可在枝头抱着幽香枯死，几曾见它被北风吹落——这是画中的菊，也是画者自己的心。',
    cover_p2='边读诗，边走进南宋遗民郑思肖的篱边秋色：一丛菊、一阵北风，写尽不肯低头的骨气。',
    end_h2='抱香 · 枝头', cn_word='两',
    words_js="['再看一次，篱菊抱香','初识所南，尚需共读','渐入佳境，再诵几遍','风已起处，花犹在枝','已解咏物言志之法','宁可抱香死，不落北风中']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = io.open(os.path.join(_here, 'huaju_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'huaju_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'huaju_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'huaju_stages.js'), encoding='utf-8').read()
