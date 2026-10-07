# -*- coding: utf-8 -*-
"""youyuan-buzhi.py —— 《游园不值》（宋·叶绍翁，no.210，青绿春晓）生成配置
千古名句「春色满园关不住，一枝红杏出墙来」：前二句柴扉不开的冷寂（抑），
末境墙头一枝红杏破壁而出（扬）；点击——柴扉虚掩、红杏招展，门缝漏出满园春色。
红杏红 #c96a6a（queue accent）作全页唯一暖彩点；语料未收，按统编教材通行本登记。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='youyuan-buzhi', title='游园不值', dyn='宋 · 叶绍翁', brand_author='叶绍翁',
    gold_rgb='201,106,106',
    root=""":root{
  --gold:#c96a6a; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(201,106,106,.30);
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
    tip='轻点画面 / 按空格 —— 柴扉虚掩，红杏出墙招展',
    hint='← → 键或空格逐境游览 · 末境可点击画面，柴扉虚掩、红杏出墙招展',
    cover_read='游园不值。宋，叶绍翁。应怜屐齿印苍苔，小扣柴扉久不开。春色满园关不住，一枝红杏出墙来。',
    cover_p1='两重意境，随诗句次第展开：先到园门外，看屐齿印苍苔、小扣柴扉久不开的冷寂；再抬头，撞见春色满园关不住、一枝红杏出墙来的惊喜。',
    cover_p2='边读诗，边体会那一次「不值」的游园——门虽敲不开，春色却关不住。',
    end_h2='红杏出墙', cn_word='两',
    words_js="['再游一次，轻叩柴扉','初识叶翁，尚需共读','渐入佳境，再诵几遍','抑扬之间，春意渐明','深得诗心，细品名句','满园春色，一枝出墙']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'youyuan-buzhi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'youyuan-buzhi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'youyuan-buzhi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'youyuan-buzhi_stages.js'), encoding='utf-8').read()
