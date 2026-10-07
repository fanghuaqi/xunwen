# -*- coding: utf-8 -*-
"""nian-nujiao-dongting.py —— 《念奴娇·过洞庭》（宋·张孝祥，no.200，水墨夜思）生成配置
四境长调（对句成境）：琼田一叶（词眼·标志性瞬间）、表里澄澈、孤光冰雪、扣舷独啸（末境可点击）。
美术立意：全页禁金；冷银水墨 #b8c8dc 主调。「更无一点风色」的静、「素月分辉，明河共影」的澄澈
是全页基调——湖面如镜映月（amp≤0.12、spec 拉高、月路入水）。
标志性瞬间「琼田一叶」：三万顷玉鉴琼田与我一叶扁舟的大小对照。
末境点击尽挹西江：北斗为杯舀江斟月（七星亮起、江水入斗），万象为宾（远岸林木人影显形）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='nian-nujiao-dongting', title='念奴娇·过洞庭', dyn='宋 · 张孝祥', brand_author='张孝祥',
    gold_rgb='184,200,220',
    root=""":root{
  --gold:#b8c8dc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(184,200,220,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(7,10,16', 1),
        ('rgba(4,6,11', 'rgba(6,8,14', 2),
        ('rgba(6,9,16', 'rgba(7,9,15', 1),
        ('rgba(3,5,9', 'rgba(5,7,12', 1),
        ('#0b101c', '#101624', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
    ],
    tip='轻点画面 / 按空格 —— 北斗为杯，舀江斟月，万象为宾',
    hint='← → 键或空格逐境游览 · 末境可点击尽挹西江：北斗为杯舀江斟月，万象为宾',
    cover_read='念奴娇·过洞庭。宋，张孝祥。洞庭青草，近中秋，更无一点风色。玉鉴琼田三万顷，着我扁舟一叶。',
    cover_p1='四重意境，随词句次第展开：近中秋的洞庭风平浪静，三万顷湖面如玉镜琼田，只浮着我一叶扁舟；素月分辉、明河共影，天上水下表里澄澈；回想岭海经年，孤光自照，肝胆犹自冰雪；于是舀尽西江、细斟北斗、邀万象为宾客，扣舷独啸，不知今夕何夕。',
    cover_p2='边读词，边走进张孝祥笔下这「天人澄澈」的中秋夜湖——湖面如镜，映月映星，也映一颗肝胆冰雪的心。',
    end_h2='澄澈 · 冰雪', cn_word='四',
    words_js="['再游一次，湖月澄明','初识于湖，尚需共读','渐入词境，心有所会','秋湖渐深，孤光自照','已解肝胆冰雪之洁','表里俱澄澈']",
    sky_atmo='0x1f2b3d',
)

POEM_JS = io.open(os.path.join(_here, 'nian-nujiao-dongting_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'nian-nujiao-dongting_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'nian-nujiao-dongting_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'nian-nujiao-dongting_stages.js'), encoding='utf-8').read()
