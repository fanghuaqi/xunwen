# -*- coding: utf-8 -*-
"""wang.py —— 《望海潮》（宋·柳永，no.125，青绿春晓·钱塘变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=5, slug='wanghaichao', title='望海潮', dyn='宋 · 柳永', brand_author='柳 永',
    gold_rgb='143,196,168',
    root=""":root{
  --gold:#8fc4a8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(143,196,168,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0a1410', 2),
        ('rgba(5,8,15', 'rgba(6,12,9', 1),
        ('rgba(4,6,11', 'rgba(5,10,7', 2),
        ('rgba(6,9,16', 'rgba(6,11,8', 1),
        ('rgba(3,5,9', 'rgba(4,8,6', 1),
        ('#0b101c', '#0e1a14', 1),
        ('#6f664f', '#5f7264', 1),
        ('#5a5340', '#52604f', 1),
    ],
    tip='轻点画面 / 按空格 —— 荷开桂落',
    hint='← → 键或空格逐境游览 · 末境可点击湖面，荷开桂落',
    cover_read='望海潮。宋，柳永。东南形胜，三吴都会，钱塘自古繁华。',
    cover_p1='五重意境，随词句次第展开：钱塘形胜的城郭气象；烟柳画桥间的十万人家；怒涛卷雪的天堑与市列珠玑的街市；三秋桂子、十里荷花、钓叟莲娃；千骑高牙、箫鼓烟霞。',
    cover_p2='边读词，边走进柳永笔下那个东南最繁华的钱塘城。',
    end_h2='三秋桂子', cn_word='五',
    words_js="['再游一次，且看繁华','初识柳永，尚需共读','渐入佳境，再诵几遍','湖山渐入画中来','深得钱塘风物之美','东南形胜，尽收眼底']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'wang_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'wang_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'wang_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'wang_stages.js'), encoding='utf-8').read()
