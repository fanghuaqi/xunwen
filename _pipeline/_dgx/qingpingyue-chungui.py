# -*- coding: utf-8 -*-
"""qingpingyue-chungui.py —— 《清平乐·春归何处》（宋·黄庭坚，no.181，青绿春晓·山谷寻春变体）生成配置
词眼「问取黄鹂」：像问路一样问鸟——末境点击，黄鹂百啭、因风飞过蔷薇架。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='qingpingyue-chungui', title='清平乐·春归何处', dyn='宋 · 黄庭坚', brand_author='黄庭坚',
    gold_rgb='163,201,168',
    root=""":root{
  --gold:#a3c9a8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(163,201,168,.30);
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
    tip='轻点画面 / 按空格 —— 黄鹂百啭，因风飞过蔷薇',
    hint='← → 键或空格逐境游览 · 末境可点击画面，问取黄鹂、春过蔷薇',
    cover_read='清平乐·春归何处。宋，黄庭坚。春归何处？寂寞无行路。若有人知春去处，唤取归来同住。',
    cover_p1='两重意境，随词句次第展开：先入春归无路的山野，四顾寂寞、小径无痕，一声「若有人知春去处，唤取归来同住」痴问唤春；再到溪畔蔷薇架下，像问路一样问取枝头黄鹂——百啭无人能解，因风飞过蔷薇。',
    cover_p2='边读词，边走进山谷笔下这场寻找春天的天真奇想。',
    end_h2='春过蔷薇', cn_word='两',
    words_js="['再游一次，山中寻春','初识山谷，尚需共读','渐入佳境，再诵几遍','词趣已明，问取黄鹂','深得山谷奇想','一问春归处，莺声过蔷薇']",
    sky_atmo='0x2c4a36',
)

POEM_JS = io.open(os.path.join(_here, 'qingpingyue-chungui_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'qingpingyue-chungui_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'qingpingyue-chungui_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'qingpingyue-chungui_stages.js'), encoding='utf-8').read()
