# -*- coding: utf-8 -*-
"""fengrujingshi.py —— 《逢入京使》（唐·岑参，no.140，大漠金戈·驿路变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='fengrujingshi', title='逢入京使', dyn='唐 · 岑参', brand_author='岑 参',
    gold_rgb='217,142,58',
    root=""":root{
  --gold:#d98e3a; --ink:#f0e2cc; --dim:#a08a6e; --paper:rgba(16,11,7,.60);
  --line:rgba(217,142,58,.30);
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
    tip='轻点画面 / 按空格 —— 口信化作飞鸿北去',
    hint='← → 键或空格逐境游览 · 末境可点击画面，口信化作飞鸿',
    cover_read='逢入京使。唐，岑参。故园东望路漫漫，双袖龙钟泪不干。马上相逢无纸笔，凭君传语报平安。',
    cover_p1='两重意境，随诗句次第展开：东望故园、双袖龙钟的漫漫驿路；马上相逢、凭君传语的匆匆一瞬——一句口信，抵万金家书。',
    cover_p2='边读诗，边走进岑参那西赴边塞、回望长安的驿路瞬间。',
    end_h2='传语平安', cn_word='二',
    words_js="['再读一次，漫漫驿路','初识嘉州，尚需共读','渐入西行，略有所感','乡思渐浓，泪湿双袖','深得报平安之豁达','马上相逢，传语平安']",
    sky_atmo='0x4a3820',
)

POEM_JS = io.open(os.path.join(_here, 'fengrujingshi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'fengrujingshi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'fengrujingshi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'fengrujingshi_stages.js'), encoding='utf-8').read()
