# -*- coding: utf-8 -*-
"""shengzhazi-yuanxi.py —— 《生查子·元夕》（宋·欧阳修，no.167，夜宴金彩·元夕灯市变体）生成配置
二境（queue.json 分境口径，去年/今年同机位对照）：
灯如昼（去年元夜：花市灯如昼+月上柳梢头+人约黄昏后——标志性瞬间·柳梢月上灯海人约）、
月依旧（今年元夜·末境可点击：月与灯依旧+不见去年人+泪湿春衫袖，点击灯海渐暗只余月光——去年人事不再）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

def io_open(name):
    return io.open(os.path.join(_here, name), encoding='utf-8').read()

META = dict(
    N=2, slug='shengzhazi-yuanxi', title='生查子·元夕', dyn='宋 · 欧阳修', brand_author='欧阳修',
    gold_rgb='217,168,90',
    root=""":root{
  --gold:#d9a85a; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(217,168,90,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,5', 1),
        ('rgba(4,6,11', 'rgba(6,5,6', 2),
        ('rgba(6,9,16', 'rgba(8,6,6', 1),
        ('rgba(3,5,9', 'rgba(6,5,6', 1),
        ('#0b101c', '#140f0a', 1),
        ('#6f664f', '#6b5c48', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点画面 / 按空格 —— 灯海渐暗，只余月光如旧',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看灯海渐暗、只余月光',
    cover_read='生查子·元夕。宋，欧阳修。去年元夜时，花市灯如昼。月上柳梢头，人约黄昏后。今年元夜时，月与灯依旧。不见去年人，泪湿春衫袖。',
    cover_p1='二重意境，随词句次第展开：去年元夜，花市灯如昼，月上柳梢头、人约黄昏后的甜蜜期约；今年元夜，月与灯依旧、不见去年人、泪湿春衫袖的物是人非。',
    cover_p2='边读词，边走进欧阳修笔下那条灯如白昼的元夜长街——同一条街、同一轮月，读懂「依旧」与「不见」之间的深情与怅惘。',
    end_h2='月灯 · 依旧', cn_word='二',
    words_js="['再读一次，灯市柳月','初识永叔，尚需共读','渐入佳境，再诵几遍','今昔对照渐明，已得词境','深解「依旧」与「不见」','月灯依旧，泪湿春衫思无尽']",
    sky_atmo='0x4a2c18',
)

POEM_JS = io_open('shengzhazi-yuanxi_poem.js')
QUIZ_JS = io_open('shengzhazi-yuanxi_quiz.js')
SCENES_JS = io_open('shengzhazi-yuanxi_scenes.js')
STAGES_JS = io_open('shengzhazi-yuanxi_stages.js')
