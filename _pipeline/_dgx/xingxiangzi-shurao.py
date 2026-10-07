# -*- coding: utf-8 -*-
"""xingxiangzi-shurao.py —— 《行香子·树绕村庄》（宋·秦观，no.184，青绿春晓）生成配置
词眼「有桃花红，李花白，菜花黄」：红/白/黄三色花田是全词彩点——
境二入园三色次第点亮（标志性瞬间）；末境登东冈，点击画面三色花田再满开，莺啼燕舞蝶忙齐来。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='xingxiangzi-shurao', title='行香子·树绕村庄', dyn='宋 · 秦观', brand_author='秦 观',
    gold_rgb='160,201,184',
    root=""":root{
  --gold:#a0c9b8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,20,16,.60);
  --line:rgba(160,201,184,.30);
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
    tip='轻点画面 / 按空格 —— 红白黄三色花田次第点亮',
    hint='← → 键或空格逐境游览 · 境二看三色花田次第点亮 · 末境可点击画面重燃满园春色',
    cover_read='行香子·树绕村庄。宋，秦观。树绕村庄，水满陂塘。倚东风，豪兴徜徉。',
    cover_p1='四重意境，随词句次第展开：先绕绿树掩映的村庄走一遭，看春水涨满陂塘，倚着东风豪兴徜徉；再到小园门前，看桃花红、李花白、菜花黄，三色花田次第点亮满园春光；远处围墙隐约、茅堂前青旗招展，流水绕过小桥；最后步上东冈回望，莺啼燕舞蝶儿忙，满眼春色都在忙。',
    cover_p2='边读词，边走进秦观笔下这幅最明快的春游画卷，与他一同乘兴徜徉。',
    end_h2='满眼春光', cn_word='四',
    words_js="['再游一次，随莺声回村','初识少游，尚需共读','渐入佳境，春色渐浓','三色在目，春光满眼','深得淮海闲趣','人在画中游，莺燕蝶正忙']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'xingxiangzi-shurao_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xingxiangzi-shurao_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xingxiangzi-shurao_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xingxiangzi-shurao_stages.js'), encoding='utf-8').read()
