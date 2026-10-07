# -*- coding: utf-8 -*-
"""cibeigushan.py —— 《次北固山下》（唐·王湾，no.135，青绿春晓·江行变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='cibeigushan', title='次北固山下', dyn='唐 · 王湾', brand_author='王 湾',
    gold_rgb='111,174,126',
    root=""":root{
  --gold:#6fae7e; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(111,174,126,.30);
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
    tip='轻点画面 / 按空格 —— 雁阵驮乡书北飞',
    hint='← → 键或空格逐境游览 · 末境可点击画面，雁阵驮乡书北飞',
    cover_read='次北固山下。唐，王湾。客路青山外，行舟绿水前。潮平两岸阔，风正一帆悬。',
    cover_p1='四重意境，随诗句次第展开：客路青山、行舟绿水的旅程；潮平岸阔、风正帆悬的开阔；海日生残夜、江春入旧年的时序交替；末了托北归雁阵，捎一封乡书到洛阳。',
    cover_p2='边读诗，边走进王湾笔下那既开阔又思乡的江行世界。',
    end_h2='海日江春', cn_word='四',
    words_js="['再游一次，且看江春','初识王湾，尚需共读','渐入佳境，再诵几遍','诗意渐阔，心随帆悬','深得时序交替之妙','海日江春，雁带乡愁']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'cibeigushan_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'cibeigushan_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'cibeigushan_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'cibeigushan_stages.js'), encoding='utf-8').read()
