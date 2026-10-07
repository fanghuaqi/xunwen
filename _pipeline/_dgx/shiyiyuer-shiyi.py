# -*- coding: utf-8 -*-
"""shiyiyuer-shiyi.py —— 《十一月四日风雨大作·其二》（宋·陆游，no.242，大漠金戈·孤村风雨变体）生成配置
诗眼「铁马冰河入梦来」：现实是孤村茅屋与风雨（雨丝 + 赭色风尘），梦中是冰河与铁骑纵队。
末境点击入梦 → 风雨渐急（雨丝 uK 涨）、冰河冷光亮起、六骑自远而近漫过孤村、火把明灭，题字「铁马冰河入梦来」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='shiyiyuer-shiyi', title='十一月四日风雨大作·其二', dyn='宋 · 陆游', brand_author='陆 游',
    gold_rgb='176,144,106',
    root=""":root{
  --gold:#b0906a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(176,144,106,.3);
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
    tip='轻点入梦 / 按空格 —— 风雨更急，铁马冰河入梦来',
    hint='← → 键或空格逐境游览 · 末境可点击入梦：风雨渐化马蹄，铁骑漫过孤村',
    cover_read='十一月四日风雨大作其二。宋，陆游。僵卧孤村不自哀，尚思为国戍轮台。夜阑卧听风吹雨，铁马冰河入梦来。',
    cover_p1='两重意境，随诗句次第展开：老病僵卧孤村，却不为自己的处境悲哀，还想替国家戍守轮台；夜深听风吹雨，披甲战马与冰封大河一齐闯入梦中。',
    cover_p2='边读诗，边走进那个风雨之夜：现实的孤村越逼仄，梦里的铁骑就越壮阔。',
    end_h2='铁马 · 冰河', cn_word='两',
    words_js="['再听一夜，风雨孤村','初识放翁，尚需共读','渐入佳境，再诵几遍','风雨渐急，铁骑渐近','已识以梦写志之法','铁马冰河，入梦而来']",
    sky_atmo='0x332414',
)

POEM_JS = io.open(os.path.join(_here, 'shiyiyuer-shiyi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'shiyiyuer-shiyi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'shiyiyuer-shiyi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'shiyiyuer-shiyi_stages.js'), encoding='utf-8').read()
