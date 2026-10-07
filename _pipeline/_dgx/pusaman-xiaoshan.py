# -*- coding: utf-8 -*-
"""pusaman-xiaoshan.py —— 《菩萨蛮·小山重叠金明灭》（唐·温庭筠，no.156，夜宴金彩·闺阁晨妆变体）生成配置
二境（queue.json 分境口径）：金屏晓妆（小山屏风金明灭+鬓云香腮+懒起画蛾弄妆梳洗）、
花面交映（标志性瞬间·末境可点击：前后镜相照花面交映+新帖罗襦双双金鹧鸪）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

def io_open(name):
    return io.open(os.path.join(_here, name), encoding='utf-8').read()

META = dict(
    N=2, slug='pusaman-xiaoshan', title='菩萨蛮·小山重叠金明灭', dyn='唐 · 温庭筠', brand_author='温庭筠',
    gold_rgb='212,176,80',
    root=""":root{
  --gold:#d4b050; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(212,176,80,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,4', 1),
        ('rgba(4,6,11', 'rgba(7,5,3', 2),
        ('rgba(6,9,16', 'rgba(9,6,4', 1),
        ('rgba(3,5,9', 'rgba(6,4,3', 1),
        ('#0b101c', '#141008', 1),
        ('#6f664f', '#6b5c46', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点画面 / 按空格 —— 前后镜相照，花面交相映',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看前后镜里花面重影交映',
    cover_read='菩萨蛮。唐，温庭筠。小山重叠金明灭，鬓云欲度香腮雪。懒起画蛾眉，弄妆梳洗迟。照花前后镜，花面交相映。新帖绣罗襦，双双金鹧鸪。',
    cover_p1='二重意境，随词句次第展开：小山重叠金明灭、鬓云欲度香腮雪，懒起画蛾眉、弄妆梳洗迟的晓妆慵懒；照花前后镜、花面交相映，新帖绣罗襦、双双金鹧鸪的妆成寂寞。',
    cover_p2='边读词，边走进温庭筠笔下那间金明灭的闺阁，体会花间词的浓丽与幽微。',
    end_h2='花面 · 交映', cn_word='二',
    words_js="['再读一次，金明灭处见晓妆','初识飞卿，尚需共读','渐入佳境，再诵几遍','晓妆渐明，已得词境','深解「懒」「迟」之幽怨','花面交映，双鸪成双人独立']",
    sky_atmo='0x3a2c20',
)

POEM_JS = io_open('pusaman-xiaoshan_poem.js')
QUIZ_JS = io_open('pusaman-xiaoshan_quiz.js')
SCENES_JS = io_open('pusaman-xiaoshan_scenes.js')
STAGES_JS = io_open('pusaman-xiaoshan_stages.js')
