# -*- coding: utf-8 -*-
"""wangjiangnan-choran.py —— 《望江南·超然台作》（宋·苏轼，no.179，烟雨江南·登台变体）生成配置
N=3 取自 queue.json stages（春未老…一城花 / 烟雨暗千家…咨嗟 / 休对故人…趁年华）
"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='wangjiangnan-choran', title='望江南·超然台作', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='154,176,201',
    root=""":root{
  --gold:#9ab0c9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(154,176,201,.28);
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
    tip='轻点新火 / 按空格 —— 茶烟袅起，千家渐明',
    hint='← → 键或空格逐境游览 · 末境可点击新火试茶，千家烟雨渐明',
    cover_read='望江南超然台作。宋，苏轼。春未老，风细柳斜斜。试上超然台上看，半壕春水一城花。烟雨暗千家。',
    cover_p1='三重意境，随词句次第展开：春未老、风细柳斜斜，试上超然台看半壕春水一城花；烟雨暗千家，寒食后酒醒却咨嗟的黯然；休对故人思故国，且将新火试新茶、诗酒趁年华的超然旷达。',
    cover_p2='边读词，边登上超然台，和东坡一起望一城烟雨，把乡愁烹成一瓯新茶。',
    end_h2='诗酒年华', cn_word='三',
    words_js="['再读一遍，超然台上','初识东坡，尚需共读','渐入台上看，略有所感','烟雨入怀，愁绪暗生','新火初红，渐得超然','诗酒趁年华，旷达开怀']",
    sky_atmo='0x33414e',
)

POEM_JS = io.open(os.path.join(_here, 'wangjiangnan-choran_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'wangjiangnan-choran_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'wangjiangnan-choran_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'wangjiangnan-choran_stages.js'), encoding='utf-8').read()
