# -*- coding: utf-8 -*-
"""duan.py —— 《短歌行》（汉·曹操，no.122，夜宴金彩·建安变体）生成配置"""

META = dict(
    N=6, slug='duange-xing', title='短歌行', dyn='汉 · 曹操', brand_author='曹 操',
    gold_rgb='201,164,74',
    root=""":root{
  --gold:#c9a44a; --ink:#e8dcc0; --dim:#9a8d72; --paper:rgba(12,10,7,.60);
  --line:rgba(201,164,74,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    # 夜宴金彩基线底色 #05070d 必须保留（style-audit 校验）
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,4', 1),
        ('rgba(4,6,11', 'rgba(6,5,3', 2),
        ('rgba(6,9,16', 'rgba(7,6,4', 1),
        ('rgba(3,5,9', 'rgba(5,4,3', 1),
        ('#0b101c', '#141009', 1),
        ('#6f664f', '#6b6250', 1),
        ('#5a5340', '#5f5745', 1),
    ],
    tip='轻点画面 / 按空格 —— 召乌鹊归山',
    hint='← → 键或空格逐境游览 · 末境可点击画面，召乌鹊归山',
    cover_read='短歌行。汉，曹操。对酒当歌，人生几何！譬如朝露，去日苦多。',
    cover_p1='六重意境，随诗句次第展开：军帐之中对酒当歌、慨叹朝露；月下按剑沉吟，思慕青衿；原野鹿鸣，鼓瑟吹笙；揽明明如月而不可掇；看月明星稀、乌鹊绕树三匝；终见山高海深，天下归心。',
    cover_p2='边读诗，边走进曹操那求贤若渴、慷慨沉雄的建安世界。',
    end_h2='歌以咏志', cn_word='六',
    words_js="['再游一次，且听慷慨之音','初识魏武，尚需共读','渐入佳境，再诵几遍','慷慨渐生，再进一觞','深得魏武求贤之切','横槊赋诗，天下归心']",
    sky_atmo='0x3d3220',
)

import io, os
_here = os.path.dirname(os.path.abspath(__file__))
POEM_JS = io.open(os.path.join(_here, 'duan_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'duan_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'duan_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'duan_stages.js'), encoding='utf-8').read()
