# -*- coding: utf-8 -*-
"""xiju-jishi.py —— 《溪居即事》（唐·崔道融，no.251，青绿春晓·溪居童趣变体）生成配置
诗眼「小童疑是有村客，急向柴门去却关」：不系船随风漂入钓鱼湾（无人之动），
小童误认客至、急向柴门去却关（童趣之动）。末境点击去却关 → 小童奔到柴门、门闩抬起、
两扇柴扉转开、小船继续漂入湾深处，题字「去却关」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='xiju-jishi', title='溪居即事', dyn='唐 · 崔道融', brand_author='崔道融',
    gold_rgb='160,201,184',
    root=""":root{
  --gold:#a0c9b8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
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
    tip='轻点去却关 / 按空格 —— 小童飞奔柴门，门闩抬起',
    hint='← → 键或空格逐境游览 · 末境可点击去却关：小童急奔，柴扉开处船正漂来',
    cover_read='溪居即事。唐，崔道融。篱外谁家不系船，春风吹入钓鱼湾。小童疑是有村客，急向柴门去却关。',
    cover_p1='两重意境，随诗句次第展开：篱笆外不知谁家的船没有拴住，被春风吹进了钓鱼湾；小童以为是村里来了客人，急忙跑向柴门去把门闩打开。',
    cover_p2='边读诗，边走进这处溪边村居：船是「不系」的，门是「却关」的，小童是「急向」的——三个动作就是一幅风俗画。',
    end_h2='不系 · 却关', cn_word='两',
    words_js="['再看一回，溪湾柴门','初识道融，尚需共读','渐入佳境，再诵几遍','船已入湾，童已到门','已识溪居闲趣','篱外谁家不系船']",
    sky_atmo='0x2f4a34',
)

POEM_JS = io.open(os.path.join(_here, 'xiju-jishi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xiju-jishi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xiju-jishi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xiju-jishi_stages.js'), encoding='utf-8').read()
