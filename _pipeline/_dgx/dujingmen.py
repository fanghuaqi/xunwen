# -*- coding: utf-8 -*-
"""dujingmen.py —— 《渡荆门送别》（唐·李白，no.136，水墨夜思·江月变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='dujingmen', title='渡荆门送别', dyn='唐 · 李白', brand_author='李 白',
    gold_rgb='143,179,201',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#8fb3c9; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(143,179,201,.28);
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
    tip='轻点江面 / 按空格 —— 故乡水泛起粼粼波光',
    hint='← → 键或空格逐境游览 · 末境可点击江面，故乡水送行舟',
    cover_read='渡荆门送别。唐，李白。渡远荆门外，来从楚国游。山随平野尽，江入大荒流。',
    cover_p1='四重意境，随诗句次第展开：渡远荆门、来游楚地的初出之怀；山随平野尽、江入大荒流的开阔；月下飞天镜、云生结海楼的奇景；末了仍怜故乡水，万里送行舟。',
    cover_p2='边读诗，边走进青年李白初出蜀地、既兴奋又恋乡的世界。',
    end_h2='月镜舟行', cn_word='四',
    words_js="['再游一次，且看江月','初识太白，尚需共读','渐入佳境，再诵几遍','诗境渐阔，心随江行','深得青莲恋乡之巧','月镜海楼，故乡水送']",
    sky_atmo='0x24344c',
)

POEM_JS = io.open(os.path.join(_here, 'dujingmen_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'dujingmen_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'dujingmen_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'dujingmen_stages.js'), encoding='utf-8').read()
