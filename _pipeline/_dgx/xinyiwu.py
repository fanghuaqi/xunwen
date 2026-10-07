# -*- coding: utf-8 -*-
"""xinyiwu.py —— 《辛夷坞》（唐·王维，no.253，宣纸留白·空山辛夷变体）生成配置
诗眼「纷纷开且落」：木末红萼（先花后叶的木兰开在树梢）、涧户寂无人（无人之境）。
末境点击开且落 → 辛夷纷纷绽放（花光次第点亮、枝摇加剧）、花瓣纷纷飘落（落速 ×3.2）、涧水微响，
题字「纷纷开且落」。宣纸留白：纸底、淡墨远山、浓墨岩壁；辛夷的紫红是全页唯一浓色。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='xinyiwu', title='辛夷坞', dyn='唐 · 王维', brand_author='王 维',
    gold_rgb='67,72,74',
    root=""":root{
  --gold:#43484a; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(67,72,74,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(233,226,208', 1),
        ('rgba(4,6,11', 'rgba(212,202,176', 2),
        ('rgba(6,9,16', 'rgba(233,226,208', 1),
        ('rgba(3,5,9', 'rgba(236,230,214', 1),
        ('#0b101c', '#f6f1e1', 1),
        ('#6f664f', '#8a8268', 1),
        ('#5a5340', '#8d8571', 1),
        ('0x0a1526', '0xe6dfcc', 4),
    ],
    tip='轻点开且落 / 按空格 —— 辛夷纷纷绽放，又纷纷落下',
    hint='← → 键或空格逐境游览 · 末境可点击开且落：花开花落，空山寂寂',
    cover_read='辛夷坞。唐，王维。木末芙蓉花，山中发红萼。涧户寂无人，纷纷开且落。',
    cover_p1='两重意境，随诗句次第展开：树梢上开着辛夷花，在这山中绽出红色花萼；山涧边的门户寂静无人，花纷纷地开着，又纷纷地落下。',
    cover_p2='边读诗，边走进辋川的空山：花不为谁开，也不为谁落——这正是王维的寂静之美。',
    end_h2='开 · 落', cn_word='两',
    words_js="['再入一次，空山辛夷','初识摩诘，尚需共读','渐入佳境，再诵几遍','花正纷纷，开而又落','已识空山自得','纷纷开且落']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = io.open(os.path.join(_here, 'xinyiwu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xinyiwu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xinyiwu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xinyiwu_stages.js'), encoding='utf-8').read()
