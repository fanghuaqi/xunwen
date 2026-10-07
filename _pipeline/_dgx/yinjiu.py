# -*- coding: utf-8 -*-
"""yinjiu.py —— 《饮酒·其五》（魏晋·陶渊明，no.137，宣纸留白·菊隐变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yinjiu', title='饮酒·其五', dyn='魏晋 · 陶渊明', brand_author='陶渊明',
    gold_rgb='122,138,90',
    root=""":root{
  --gold:#7a8a5a; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(122,138,90,.32);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(240,236,224', 1),
        ('rgba(4,6,11', 'rgba(238,233,220', 2),
        ('rgba(6,9,16', 'rgba(239,234,222', 1),
        ('rgba(3,5,9', 'rgba(236,231,218', 1),
        ('#0b101c', '#f2eee0', 1),
        ('#6f664f', '#6e695a', 1),
        ('#5a5340', '#655f4e', 1),
    ],
    tip='轻点画面 / 按空格 —— 庐中灯起，真意忘言',
    hint='← → 键或空格逐境游览 · 末境可点击画面，庐中灯起',
    cover_read='饮酒其五。魏晋，陶渊明。结庐在人境，而无车马喧。问君何能尔？心远地自偏。',
    cover_p1='四重意境，随诗句次第展开：人境结庐、心远地偏的静；采菊东篱、悠然见南山的遇；山气日夕佳、飞鸟相与还的归；此中有真意、欲辨已忘言的悟。',
    cover_p2='边读诗，边走进陶渊明那冲淡自然、物我两忘的世界。',
    end_h2='悠然南山', cn_word='四',
    words_js="['再入诗境，细品菊香','初识五柳，尚需共读','渐入南山，略有会意','淡然渐生，心远地偏','深得渊明冲淡之趣','此中真意，欲辨忘言']",
    sky_atmo='0xb8b2a0',
)

POEM_JS = io.open(os.path.join(_here, 'yinjiu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yinjiu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yinjiu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yinjiu_stages.js'), encoding='utf-8').read()
