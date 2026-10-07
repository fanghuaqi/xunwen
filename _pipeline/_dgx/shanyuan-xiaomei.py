# -*- coding: utf-8 -*-
"""shanyuan-xiaomei.py —— 《山园小梅》（宋·林逋，no.237，水墨夜思·孤山梅影变体）生成配置
诗眼「疏影横斜水清浅，暗香浮动月黄昏」：月下梅枝横斜、清浅水面一道疏影，暗香是可见的银白香雾。
末境点击暗香 → 水中疏影横斜摇动 + 暗香成雾漫开（四境，末境可点击）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='shanyuan-xiaomei', title='山园小梅', dyn='宋 · 林逋', brand_author='林 逋',
    gold_rgb='168,188,212',
    root=""":root{
  --gold:#a8bcd4; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(168,188,212,.26);
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
    tip='轻点暗香 / 按空格 —— 疏影横斜，暗香浮动成雾',
    hint='← → 键或空格逐境游览 · 末境可点击暗香：水中疏影横斜摇动，暗香成雾漫开',
    cover_read='山园小梅。宋，林逋。众芳摇落独暄妍，占尽风情向小园。疏影横斜水清浅，暗香浮动月黄昏。',
    cover_p1='四重意境，随诗句次第展开：百花摇落，唯独小园里的梅花占尽风情；月下稀疏的梅影横斜在清浅水上，幽微的暗香在黄昏月色里浮动；霜禽欲下先偷眼，粉蝶如知合断魂；幸有微吟可与它相亲，不须檀板金樽的热闹。',
    cover_p2='边读诗，边走进孤山月色下的那一片梅影暗香——千古咏梅绝唱，写的正是这份清与独。',
    end_h2='暗香 · 疏影', cn_word='四',
    words_js="['再游一次，且嗅暗香','初识君复，尚需共读','渐入佳境，再诵几遍','影已横斜，香正浮动','已识孤山清绝意','疏影暗香，千古梅魂']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = io.open(os.path.join(_here, 'shanyuan-xiaomei_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'shanyuan-xiaomei_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'shanyuan-xiaomei_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'shanyuan-xiaomei_stages.js'), encoding='utf-8').read()
