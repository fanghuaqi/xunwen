# -*- coding: utf-8 -*-
"""wangjiangnan.py —— 《望江南·梳洗罢》（唐·温庭筠，no.139，烟雨江南·望楼变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='wangjiangnan', title='望江南·梳洗罢', dyn='唐 · 温庭筠', brand_author='温 庭 筠',
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
    tip='轻点江面 / 按空格 —— 最后一帆远去，斜晖更沉',
    hint='← → 键或空格逐境游览 · 末境可点击江面，最后一帆远去',
    cover_read='望江南。唐，温庭筠。梳洗罢，独倚望江楼。过尽千帆皆不是，斜晖脉脉水悠悠。',
    cover_p1='三重意境，随词句次第展开：晨起梳洗、独倚江楼的期待；过尽千帆皆不是、斜晖脉脉水悠悠的漫长失望；末了一句肠断白蘋洲——当年分别之地。',
    cover_p2='边读词，边走进思妇那从期待到断肠的一天。',
    end_h2='斜晖悠悠', cn_word='三',
    words_js="['再读一次，且看千帆','初识飞卿，尚需共读','渐入江楼，略有所感','愁绪渐生，如水悠悠','深得望江之盼','肠断蘋洲，千帆过尽']",
    sky_atmo='0x3a4454',
)

POEM_JS = io.open(os.path.join(_here, 'wangjiangnan_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'wangjiangnan_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'wangjiangnan_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'wangjiangnan_stages.js'), encoding='utf-8').read()
