# -*- coding: utf-8 -*-
"""guolingdingyang.py —— 《过零丁洋》（宋·文天祥，no.151，大漠金戈·正气变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='guolingdingyang', title='过零丁洋', dyn='宋 · 文天祥', brand_author='文 天 祥',
    gold_rgb='176,112,58',
    root=""":root{
  --gold:#b0703a; --ink:#f0e2cc; --dim:#a08a6e; --paper:rgba(16,11,7,.60);
  --line:rgba(176,112,58,.30);
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
    tip='轻点画面 / 按空格 —— 丹心化灯长明，照亮汗青',
    hint='← → 键或空格逐境游览 · 末境可点击画面，丹心长明',
    cover_read='过零丁洋。宋，文天祥。辛苦遭逢起一经，干戈寥落四周星。',
    cover_p1='四重意境，随诗句次第展开：起一经、入仕四年的兵戈苦战；山河破碎风飘絮、身世浮沉雨打萍的悲壮互喻；惶恐滩头说惶恐、零丁洋里叹零丁的孤苦处境；人生自古谁无死，留取丹心照汗青的千古绝唱。',
    cover_p2='边读诗，边走进文天祥那视死如归、浩气长存的民族气节。',
    end_h2='丹心汗青', cn_word='四',
    words_js="['再读一次，干戈寥落','初识文丞相，尚需共读','渐入惊涛，略有所感','正气渐升，风雨飘萍','深得浩然正气之概','人生自古谁无死，留取丹心照汗青']",
    sky_atmo='0x442c16',
)

POEM_JS = io.open(os.path.join(_here, 'guolingdingyang_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'guolingdingyang_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'guolingdingyang_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'guolingdingyang_stages.js'), encoding='utf-8').read()
