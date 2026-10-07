# -*- coding: utf-8 -*-
"""yeshouxiangwen.py —— 《夜上受降城闻笛》（唐·李益，no.141，大漠金戈·霜月变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='yeshouxiangwen', title='夜上受降城闻笛', dyn='唐 · 李益', brand_author='李 益',
    gold_rgb='184,135,74',
    root=""":root{
  --gold:#b8874a; --ink:#e8e4da; --dim:#8a8a94; --paper:rgba(14,16,20,.60);
  --line:rgba(184,135,74,.28);
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
    tip='轻点城头 / 按空格 —— 芦管声起，征人尽望乡',
    hint='← → 键或空格逐境游览 · 末境可点击城头，芦管声起',
    cover_read='夜上受降城闻笛。唐，李益。回乐烽前沙似雪，受降城外月如霜。不知何处吹芦管，一夜征人尽望乡。',
    cover_p1='两重意境，随诗句次第展开：回乐烽前沙似雪、受降城外月如霜的清寒月夜；不知何处一声芦管，一夜征人尽望乡。',
    cover_p2='边读诗，边走进李益笔下那被一支芦管勾起的万里乡愁。',
    end_h2='霜月望乡', cn_word='二',
    words_js="['再读一次，霜月沙雪','初识君虞，尚需共读','渐入边声，略有所感','乡愁渐起，如闻芦管','深得含蓄之妙','一夜芦管，尽是乡心']",
    sky_atmo='0x4a5058',
)

POEM_JS = io.open(os.path.join(_here, 'yeshouxiangwen_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yeshouxiangwen_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yeshouxiangwen_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yeshouxiangwen_stages.js'), encoding='utf-8').read()
