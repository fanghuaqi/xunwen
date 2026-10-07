# -*- coding: utf-8 -*-
"""jiangchengzi.py —— 《江城子·密州出猎》（宋·苏轼，no.150，夜宴金彩·出猎变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='jiangchengzi', title='江城子·密州出猎', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='217,160,80',
    root=""":root{
  --gold:#d9a050; --ink:#e8dcc0; --dim:#9a8d72; --paper:rgba(12,10,7,.60);
  --line:rgba(217,160,80,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,4', 1),
        ('rgba(4,6,11', 'rgba(6,5,3', 2),
        ('rgba(6,9,16', 'rgba(7,6,4', 1),
        ('rgba(3,5,9', 'rgba(5,4,3', 1),
        ('#0b101c', '#141009', 1),
        ('#6f664f', '#6b6250', 1),
        ('#5a5340', '#5f5745', 1),
    ],
    tip='轻点画面 / 按空格 —— 会挽雕弓如满月，射天狼',
    hint='← → 键或空格逐境游览 · 末境可点击画面，挽弓射天狼',
    cover_read='江城子密州出猎。宋，苏轼。老夫聊发少年狂，左牵黄，右擎苍，锦帽貂裘，千骑卷平冈。',
    cover_p1='三重意境，随词句次第展开：老夫聊发少年狂、千骑卷平冈的猎场豪气；酒酣胸胆尚开张、鬓微霜又何妨的自负豪迈；末了会挽雕弓如满月，西北望，射天狼的卫国壮志。',
    cover_p2='边读词，边走进苏轼笔下那豪放词的开山之作。',
    end_h2='挽弓射狼', cn_word='三',
    words_js="['再读一次，千骑卷冈','初识东坡，尚需共读','渐入猎场，略有所感','豪气渐炽，酒酣胸胆','深得坡仙狂豪之概','会挽雕弓，西北射天狼']",
    sky_atmo='0x344258',
)

POEM_JS = io.open(os.path.join(_here, 'jiangchengzi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'jiangchengzi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'jiangchengzi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'jiangchengzi_stages.js'), encoding='utf-8').read()
