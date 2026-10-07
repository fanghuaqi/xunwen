# -*- coding: utf-8 -*-
"""haitang.py —— 《海棠》（宋·苏轼，no.240，夜宴金彩·夜庭海棠变体）生成配置
诗眼「故烧高烛照红妆」：夜庭里一树海棠，东风与香雾浮动，月转回廊（地面月光带缓缓转过）；
末境点击高烛 → 烛焰亮起、暖光池铺开、海棠"红妆"在夜色中显影（花光次第亮起）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='haitang', title='海棠', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='217,168,90',
    residual=('将进酒', '万古愁', '太白'),   # 小测干扰项合法提到「李白」（「云想衣裳花想容」以牡丹比贵妃），故按 build.py 注释覆盖禁词表
    root=""":root{
  --gold:#d9a85a; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(217,168,90,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,4', 1),
        ('rgba(4,6,11', 'rgba(7,5,3', 2),
        ('rgba(6,9,16', 'rgba(9,6,4', 1),
        ('rgba(3,5,9', 'rgba(6,4,3', 1),
        ('#0b101c', '#141008', 1),
        ('#6f664f', '#6b5c46', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点高烛 / 按空格 —— 烛光亮起，海棠红妆在夜色中显影',
    hint='← → 键或空格逐境游览 · 末境可点击高烛：烛焰亮起、暖光铺地，海棠红妆渐显',
    cover_read='海棠。宋，苏轼。东风袅袅泛崇光，香雾空蒙月转廊。只恐夜深花睡去，故烧高烛照红妆。',
    cover_p1='两重意境，随诗句次第展开：东风袅袅，花上浮起一层光泽；香雾迷蒙，月亮已转过回廊——夜已深了；只因怕海棠睡去，诗人特意点起高高的蜡烛，照着它的一树红妆。',
    cover_p2='边读诗，边走进苏轼笔下的夜庭：一支高烛、一树海棠，读的是花，也是惜花之心。',
    end_h2='烛照 · 红妆', cn_word='两',
    words_js="['再赏一夜，秉烛看花','初识东坡，尚需共读','渐入佳境，再诵几遍','香雾渐起，烛光渐明','已解惜花之意','故烧高烛，照见红妆']",
    sky_atmo='0x3a2c20',
)

POEM_JS = io.open(os.path.join(_here, 'haitang_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'haitang_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'haitang_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'haitang_stages.js'), encoding='utf-8').read()
