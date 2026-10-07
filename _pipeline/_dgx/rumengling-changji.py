# -*- coding: utf-8 -*-
"""rumengling-changji.py —— 《如梦令·常记溪亭日暮》（宋·李清照，no.187，青绿春晓·荷塘日暮变体）生成配置
词眼「争渡，争渡，惊起一滩鸥鹭」：少女醉游误入藕花深处 → 末境点击，急桨争渡、鸥鹭冲天而起。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='rumengling-changji', title='如梦令·常记溪亭日暮', dyn='宋 · 李清照', brand_author='李清照',
    gold_rgb='143,201,184',
    root=""":root{
  --gold:#8fc9b8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,20,16,.60);
  --line:rgba(143,201,184,.30);
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
    tip='轻点画面 / 按空格 —— 争渡！急桨惊起一滩鸥鹭',
    hint='← → 键或空格逐境游览 · 末境可点击画面，争渡惊起一滩鸥鹭',
    cover_read='如梦令·常记溪亭日暮。宋，李清照。常记溪亭日暮，沉醉不知归路。',
    cover_p1='两重意境，随词句次第展开：先随夕照回溪亭，看少女沉醉忘归、兴尽回舟，一叶小舟误入藕花深处；再听「争渡，争渡」，急桨声里一滩鸥鹭扑棱棱冲天而起——那是易安记忆里最烂漫的一个夏日黄昏。',
    cover_p2='边读词，边走进李清照少女时代那个荷香、酒意与鸟声都酿在一起的黄昏。',
    end_h2='舟出荷荡', cn_word='两',
    words_js="['再泛一次舟，藕花深处','初识易安，尚需共读','渐入佳境，再诵几遍','词心已明，鸥鹭惊飞','深得易安少女烂漫','溪亭日暮，一滩鸥鹭入梦来']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'rumengling-changji_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'rumengling-changji_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'rumengling-changji_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'rumengling-changji_stages.js'), encoding='utf-8').read()
