# -*- coding: utf-8 -*-
"""duhanjiang.py —— 《渡汉江》（唐·宋之问，no.248，水墨夜思·汉江近乡变体）生成配置
诗眼「近乡情更怯，不敢问来人」：岭外四层叠嶂、音书断绝（孤雁远飞）、渡江渐近乡关。
末境点击问来人 → 来人迎面走近并"欲问又止"（顿步侧身）、乡关村落整体前移 7 单位、诗人侧身，题字「近乡情怯」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='duhanjiang', title='渡汉江', dyn='唐 · 宋之问', brand_author='宋之问',
    gold_rgb='159,176,201',
    root=""":root{
  --gold:#9fb0c9; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(159,176,201,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(7,10,16', 1),
        ('rgba(4,6,11', 'rgba(6,8,14', 2),
        ('rgba(6,9,16', 'rgba(7,9,15', 1),
        ('rgba(3,5,9', 'rgba(5,7,12', 1),
        ('#0b101c', '#101624', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
    ],
    tip='轻点问来人 / 按空格 —— 来人欲问又止，乡关渐近',
    hint='← → 键或空格逐境游览 · 末境可点击问来人：来人走近，乡关渐近',
    cover_read='渡汉江。唐，宋之问。岭外音书断，经冬复历春。近乡情更怯，不敢问来人。',
    cover_p1='两重意境，随诗句次第展开：被贬在五岭之外，家中音信断绝，熬过一个冬天又经历一个春天；越走近家乡心里越发怯，连迎面来的人也不敢开口问一声。',
    cover_p2='边读诗，边走进汉江上那叶渡舟：一「怯」一「不敢」，写尽归乡人患得患失之心。',
    end_h2='近乡 · 情怯', cn_word='两',
    words_js="['再渡一次，汉江近乡','初识延清，尚需共读','渐入佳境，再诵几遍','乡关渐近，脚步渐怯','已识近乡情怯意','近乡情更怯，不敢问来人']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = io.open(os.path.join(_here, 'duhanjiang_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'duhanjiang_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'duhanjiang_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'duhanjiang_stages.js'), encoding='utf-8').read()
