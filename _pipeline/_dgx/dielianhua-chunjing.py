# -*- coding: utf-8 -*-
"""dielianhua-chunjing.py —— 《蝶恋花·春景》（宋·苏轼，no.176，青绿春晓·晚春墙垣变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='dielianhua-chunjing', title='蝶恋花·春景', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='168,207,143',
    root=""":root{
  --gold:#a8cf8f; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(168,207,143,.30);
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
    tip='轻点画面 / 按空格 —— 笑声渐远渐悄，柳绵飘少',
    hint='← → 键或空格逐境游览 · 末境可点击画面，笑声渐悄、柳绵吹少',
    cover_read='蝶恋花·春景。宋，苏轼。花褪残红青杏小，燕子飞时，绿水人家绕。枝上柳绵吹又少，天涯何处无芳草。',
    cover_p1='两重意境，随词句次第展开：先入暮春郊野，看残红褪尽、青杏初小，燕子飞时绿水绕人家，柳绵吹少而芳草偏遍天涯；再隔一堵矮墙，听墙里秋千与佳人笑语，体会墙外行人「多情却被无情恼」的怅惘。',
    cover_p2='边读词，边走进东坡笔下那个春将归去、一墙之隔两样心事的世界。',
    end_h2='春恼悄然', cn_word='两',
    words_js="['再游一次，且惜春光','初识东坡，尚需共读','渐入佳境，再诵几遍','词心渐明，春意入怀','深得东坡旷达','一墙春恼，芳草天涯']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'dielianhua-chunjing_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'dielianhua-chunjing_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'dielianhua-chunjing_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'dielianhua-chunjing_stages.js'), encoding='utf-8').read()
