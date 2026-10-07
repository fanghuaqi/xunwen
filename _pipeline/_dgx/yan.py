# -*- coding: utf-8 -*-
"""yan.py —— 《雁门太守行》（唐·李贺，no.128，大漠金戈·玄金变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yanmen-taishou-xing', title='雁门太守行', dyn='唐 · 李贺', brand_author='李 贺',
    gold_rgb='184,118,58',
    root=""":root{
  --gold:#b8763a; --ink:#f0e2cc; --dim:#a08a6e; --paper:rgba(16,11,7,.60);
  --line:rgba(184,118,58,.30);
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
    tip='轻点画面 / 按空格 —— 金甲次第亮起',
    hint='← → 键或空格逐境游览 · 末境可点击城头，金甲次第亮起',
    cover_read='雁门太守行。唐，李贺。黑云压城城欲摧，甲光向日金鳞开。',
    cover_p1='四重意境，随诗句次第展开：黑云压城与金甲向日的强光对撞；角声满天的秋色里，塞上胭脂凝成夜紫；半卷红旗潜行至易水，霜重鼓寒；终登黄金台，提携玉龙，誓死报君。',
    cover_p2='边读诗，边走进李贺笔下那场奇光异色的边塞之战。',
    end_h2='黑云金鳞', cn_word='四',
    words_js="['再诵一次，黑云金甲','初识诗鬼，尚需共读','渐入佳境，再诵几遍','奇色渐入眼中','深得长吉奇崛之思','黑云金鳞，气象万千']",
    sky_atmo='0x4a3820',
)

POEM_JS = io.open(os.path.join(_here, 'yan_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yan_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yan_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yan_stages.js'), encoding='utf-8').read()
