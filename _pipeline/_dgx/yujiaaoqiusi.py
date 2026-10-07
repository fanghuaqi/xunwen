# -*- coding: utf-8 -*-
"""yujiaaoqiusi.py —— 《渔家傲·秋思》（宋·范仲淹，no.147，大漠金戈·边塞变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='yujiaao-qiusi', title='渔家傲·秋思', dyn='宋 · 范仲淹', brand_author='范 仲 淹',
    gold_rgb='192,138,74',
    root=""":root{
  --gold:#c08a4a; --ink:#f0e2cc; --dim:#a08a6e; --paper:rgba(16,11,7,.60);
  --line:rgba(192,138,74,.30);
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
    tip='轻点城头 / 按空格 —— 羌管声起，霜满边城',
    hint='← → 键或空格逐境游览 · 末境可点击城头，羌管声起',
    cover_read='渔家傲秋思。宋，范仲淹。塞下秋来风景异，衡阳雁去无留意。四面边声连角起，千嶂里，长烟落日孤城闭。',
    cover_p1='三重意境，随词句次第展开：塞下秋来、长烟落日孤城闭的苍凉；浊酒一杯、燕然未勒的沉郁；夜深人不寐、将军白发征夫泪的壮阔与悲凉。',
    cover_p2='边读词，边走进范文正公笔下那个沉郁苍凉的宋代边塞世界。',
    end_h2='千嶂秋思', cn_word='三',
    words_js="['再读一次，长烟落日','初识文正，尚需共读','渐入边声，略有所感','苍凉渐生，燕然未勒','深得豪放词之先声','将军白发，孤城秋思']",
    sky_atmo='0x442c18',
)

POEM_JS = io.open(os.path.join(_here, 'yujiaaoqiusi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yujiaaoqiusi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yujiaaoqiusi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yujiaaoqiusi_stages.js'), encoding='utf-8').read()
