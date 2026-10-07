# -*- coding: utf-8 -*-
"""pozhenzi.py —— 《破阵子·为陈同甫赋壮词以寄之》（宋·辛弃疾，no.148，大漠金戈·壮词变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='pozhenzi', title='破阵子·为陈同甫赋壮词以寄之', dyn='宋 · 辛弃疾', brand_author='辛 弃 疾',
    gold_rgb='192,80,58',
    root=""":root{
  --gold:#c0503a; --ink:#f0e2cc; --dim:#a08a6e; --paper:rgba(16,11,7,.60);
  --line:rgba(192,80,58,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(9,6,4', 1),
        ('rgba(4,6,11', 'rgba(8,5,3', 2),
        ('rgba(6,9,16', 'rgba(9,6,4', 1),
        ('rgba(3,5,9', 'rgba(7,4,3', 1),
        ('#0b101c', '#1a120c', 1),
        ('#6f664f', '#6e5d48', 1),
        ('#5a5340', '#61523e', 1),
    ],
    tip='轻点画面 / 按空格 —— 沙场幻境掠过，白发对孤灯',
    hint='← → 键或空格逐境游览 · 末境可点击画面，沙场幻境掠过',
    cover_read='破阵子为陈同甫赋壮词以寄之。宋，辛弃疾。醉里挑灯看剑，梦回吹角连营。',
    cover_p1='四重意境，随词句次第展开：醉里挑灯看剑、梦回吹角连营的军营入梦；八百里分麾下炙、沙场秋点兵的壮阔阵势；马作的卢飞快、弓如霹雳弦惊的飞驰；了却君王天下事、赢得生前身后名——可怜白发生！',
    cover_p2='边读词，边走进稼轩那金戈铁马的梦境与白发对孤灯的长叹。',
    end_h2='壮词白发', cn_word='四',
    words_js="['再读一次，连营吹角','初识稼轩，尚需共读','渐入沙场，略有所感','豪情渐炽，秋点兵声','深得雄阔沉痛之力','沙场秋点兵，可怜白发生']",
    sky_atmo='0x46321e',
)

POEM_JS = io.open(os.path.join(_here, 'pozhenzi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'pozhenzi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'pozhenzi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'pozhenzi_stages.js'), encoding='utf-8').read()
