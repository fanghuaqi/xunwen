# -*- coding: utf-8 -*-
"""zengliujingwen.py —— 《赠刘景文》（宋·苏轼，no.239，青绿春晓·初冬园圃变体）生成配置
诗眼「最是橙黄橘绿时」：前半是凋尽的荷与残破的菊（一「尽」一「残」），
后半是满树点亮起来的橙黄橘绿；末境点击 → 荷枯菊残褪去（渐隐），橙橘果实与果园暖光次第亮起。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='zengliujingwen', title='赠刘景文', dyn='宋 · 苏轼', brand_author='苏 轼',
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
    tip='轻点橙黄橘绿 / 按空格 —— 荷枯菊残褪去，满树橙橘次第点亮',
    hint='← → 键或空格逐境游览 · 末境可点击橙橘：残荷残菊褪去，果实与果园暖光次第亮起',
    cover_read='赠刘景文。宋，苏轼。荷尽已无擎雨盖，菊残犹有傲霜枝。一年好景君须记，最是橙黄橘绿时。',
    cover_p1='两重意境，随诗句次第展开：荷花凋尽，再没有擎雨的荷叶；菊花残了，花枝仍在霜里傲然挺立；一年中最好的景致你须记住——正是这橙子黄熟、橘子青绿的初冬时节。',
    cover_p2='边读诗，边走进东坡笔下的初冬园圃：前一半是凋零，后一半是丰收，而这正是他要说给朋友听的话。',
    end_h2='橙黄 · 橘绿', cn_word='两',
    words_js="['再游一次，初冬园圃','初识东坡，尚需共读','渐入佳境，再诵几遍','残荷渐隐，橙橘渐亮','已解勉励之意','橙黄橘绿，一年好景']",
    sky_atmo='0x2f4a34',
)

POEM_JS = io.open(os.path.join(_here, 'zengliujingwen_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'zengliujingwen_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'zengliujingwen_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'zengliujingwen_stages.js'), encoding='utf-8').read()
