# -*- coding: utf-8 -*-
"""taicheng.py —— 《台城》（唐·韦庄，no.235，烟雨江南·台城柳堤变体）生成配置
诗眼「依旧烟笼十里堤」：十里长堤柳色如旧，六朝宫阙残影在烟雨中若隐若现；
末境点击烟笼堤 → 柳烟漫堤、六朝残影如梦散去（「六朝如梦」），唯柳色依旧。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='taicheng', title='台城', dyn='唐 · 韦庄', brand_author='韦 庄',
    gold_rgb='143,154,184',
    root=""":root{
  --gold:#8f9ab8; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(143,154,184,.28);
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
    tip='轻点烟堤 / 按空格 —— 柳烟漫过十里长堤，六朝残影散尽',
    hint='← → 键或空格逐境游览 · 末境可点击烟堤：柳烟渐浓漫堤，六朝残影如梦散去',
    cover_read='台城。唐，韦庄。江雨霏霏江草齐，六朝如梦鸟空啼。无情最是台城柳，依旧烟笼十里堤。',
    cover_p1='两重意境，随诗句次第展开：江上细雨霏霏、江草齐齐，六朝繁华如梦，只余鸟声空啼；最无情的是台城外的杨柳，六朝早已散尽，它却依旧笼烟十里、绿满长堤。',
    cover_p2='边读诗，边走进烟雨中的六朝故都：一场江雨、一行柳色，写尽三百年兴亡。',
    end_h2='烟笼 · 十里', cn_word='两',
    words_js="['再望一次，烟雨台城','初识浣花，尚需共读','渐入佳境，再诵几遍','江雨渐密，柳色渐青','已解六朝如梦意','柳色依旧，六朝如梦']",
    sky_atmo='0x344052',
)

POEM_JS = io.open(os.path.join(_here, 'taicheng_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'taicheng_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'taicheng_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'taicheng_stages.js'), encoding='utf-8').read()
