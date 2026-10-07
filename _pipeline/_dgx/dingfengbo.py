# -*- coding: utf-8 -*-
"""dingfengbo.py —— 《定风波·莫听穿林打叶声》（宋·苏轼，no.149，烟雨江南·旷达变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='dingfengbo', title='定风波·莫听穿林打叶声', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='143,179,201',
    root=""":root{
  --gold:#8fb3c9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(143,179,201,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#131a24', 1),
        ('#6f664f', '#5f6a7a', 1),
        ('#5a5340', '#525c6c', 1),
    ],
    tip='轻点雨幕 / 按空格 —— 也无风雨也无晴',
    hint='← → 键或空格逐境游览 · 末境可点击雨幕，烟雨散去',
    cover_read='定风波莫听穿林打叶声。宋，苏轼。莫听穿林打叶声，何妨吟啸且徐行。竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。',
    cover_p1='三重意境，随词句次第展开：穿林打叶声中竹杖芒鞋、一蓑烟雨任平生的从容；料峭春风吹酒醒、山头斜照却相迎的明媚；回首向来萧瑟处，归去，也无风雨也无晴的旷达超然。',
    cover_p2='边读词，边走进东坡居士那超越顺逆荣辱、从容潇洒的一生。',
    end_h2='任平生', cn_word='三',
    words_js="['再读一次，烟雨平生','初识东坡，尚需共读','渐入风雨，略有所悟','旷达渐生，竹杖芒鞋','深得坡仙超然之境','也无风雨也无晴']",
    sky_atmo='0x344052',
)

POEM_JS = io.open(os.path.join(_here, 'dingfengbo_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'dingfengbo_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'dingfengbo_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'dingfengbo_stages.js'), encoding='utf-8').read()
