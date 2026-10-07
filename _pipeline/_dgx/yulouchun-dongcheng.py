# -*- coding: utf-8 -*-
"""yulouchun-dongcheng.py —— 《玉楼春·东城渐觉风光好》（宋·宋祁，no.168，青绿春晓·春日行乐变体）生成配置
accent=#c96a6a（红杏红，全页唯一暖彩点，禁金）；标志性瞬间「红杏枝头春意闹」；
末境点击红杏：枝头群蜂喧动 + 春意具象化。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='yulouchun-dongcheng', title='玉楼春·东城渐觉风光好', dyn='宋 · 宋祁', brand_author='宋 祁',
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
    tip='轻点画面 / 按空格 —— 点击红杏，枝头群蜂喧动、春意具象',
    hint='← → 键或空格逐境游览 · 末境可点击画面，红杏枝头群蜂喧动、春意具象',
    cover_read='玉楼春·东城渐觉风光好。宋，宋祁。东城渐觉风光好，縠皱波纹迎客棹。',
    cover_p1='两重意境，随词句次第展开：先入东城春晓，看縠皱波纹迎送客船、绿杨烟外晓寒渐轻、红杏枝头春意正闹；再赴花间晚照，陪持酒词人向斜阳相劝，且把一晌欢娱留在花影里。',
    cover_p2='边读词，边走进宋祁笔下那个风光正好、春意喧闹的东城春日。',
    end_h2='花间晚照', cn_word='两',
    words_js="['再游一次，且惜春光','初识宋祁，尚需共读','渐入佳境，再诵几遍','词心渐明，春意渐闹','深得「红杏尚书」词心','花间留照，春意成诵']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'yulouchun-dongcheng_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yulouchun-dongcheng_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yulouchun-dongcheng_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yulouchun-dongcheng_stages.js'), encoding='utf-8').read()
