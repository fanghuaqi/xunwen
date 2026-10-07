# -*- coding: utf-8 -*-
"""timaandi.py —— 《题临安邸》（宋·林升，no.243，水墨夜思·西湖灯影变体）生成配置
诗眼「直把杭州作汴州」：湖山楼台层层叠叠、画舫灯影正盛（杭州），
末境点击西湖歌舞 → 暖风横流、灯影虚化（灯的光团放大变柔），汴州故都残影自湖上渐渐浮现。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='timaandi', title='题临安邸', dyn='宋 · 林升', brand_author='林 升',
    gold_rgb='143,164,192',
    root=""":root{
  --gold:#8fa4c0; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(143,164,192,.26);
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
    tip='轻点西湖歌舞 / 按空格 —— 暖风熏人，汴州残影浮现',
    hint='← → 键或空格逐境游览 · 末境可点击西湖歌舞：灯影虚化，故都残影浮现',
    cover_read='题临安邸。宋，林升。山外青山楼外楼，西湖歌舞几时休？暖风熏得游人醉，直把杭州作汴州。',
    cover_p1='两重意境，随诗句次第展开：山外青山、楼外楼，西湖歌舞几时罢休？暖风把游人熏得像醉了一样——他们竟把临时的杭州，当成了沦陷的故都汴州。',
    cover_p2='边读诗，边走进夜色里的西湖：灯影越盛，那句「直把杭州作汴州」就越冷。',
    end_h2='杭州 · 汴州', cn_word='两',
    words_js="['再游一夜，西湖灯影','初识林升，尚需共读','渐入佳境，再诵几遍','灯影渐虚，故都渐显','已识讽喻之意','直把杭州，作了汴州']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = io.open(os.path.join(_here, 'timaandi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'timaandi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'timaandi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'timaandi_stages.js'), encoding='utf-8').read()
