# -*- coding: utf-8 -*-
"""juesi-gumu.py —— 《绝句·古木阴中》（宋·志南，no.247，青绿春晓·古木溪桥变体）生成配置
诗眼「沾衣欲湿杏花雨，吹面不寒杨柳风」：皆以触觉写春——雨"欲湿"而未湿、风"不寒"而微暖。
末境点击杨柳风 → 雨丝加密、柳丝拂动加剧、杏花瓣落在老僧肩头（y 落到肩高即驻留），题字「杏花雨」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='juesi-gumu', title='绝句·古木阴中', dyn='宋 · 志南', brand_author='志 南',
    gold_rgb='143,201,184',
    root=""":root{
  --gold:#8fc9b8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(143,201,184,.30);
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
    tip='轻点杨柳风 / 按空格 —— 杏花雨细，柳风拂面，落花沾衣',
    hint='← → 键或空格逐境游览 · 末境可点击杨柳风：雨细柳摇，杏花落肩',
    cover_read='绝句。宋，志南。古木阴中系短篷，杖藜扶我过桥东。沾衣欲湿杏花雨，吹面不寒杨柳风。',
    cover_p1='两重意境，随诗句次第展开：在古树浓荫里系好小船，拄着藜杖慢慢走过桥东；杏花时节的细雨像要沾湿衣裳却未湿，杨柳间的春风吹在脸上一点也不冷。',
    cover_p2='边读诗，边走进志南和尚笔下的早春：这两句不写「看」，只写「沾」与「吹」，春天就成了可以摸到的东西。',
    end_h2='杏花 · 柳风', cn_word='两',
    words_js="['再走一程，古木溪桥','初识志南，尚需共读','渐入佳境，再诵几遍','雨细如丝，柳风拂面','已识以触觉写春','沾衣欲湿，吹面不寒']",
    sky_atmo='0x2f4a34',
)

POEM_JS = io.open(os.path.join(_here, 'juesi-gumu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'juesi-gumu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'juesi-gumu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'juesi-gumu_stages.js'), encoding='utf-8').read()
