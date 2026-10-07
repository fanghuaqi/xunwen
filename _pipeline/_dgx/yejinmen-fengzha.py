# -*- coding: utf-8 -*-
"""yejinmen-fengzha.py —— 《谒金门·风乍起》（五代·冯延巳，no.162，青绿春晓·春池杏影变体）生成配置
词眼「风乍起，吹皱一池春水」：一「皱」字把无形的春风写成看得见的层层水纹——
境壹自动起风（涟漪层层皱开 + 花瓣横飘），末境点击池水再皱一层并惊起喜鹊（举头闻鹊喜）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='yejinmen-fengzha', title='谒金门·风乍起', dyn='五代 · 冯延巳', brand_author='冯 延 巳',
    gold_rgb='163,201,143',
    root=""":root{
  --gold:#a3c98f; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(163,201,143,.30);
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
    tip='轻点画面 / 按空格 —— 一池春水，涟漪层层皱开',
    hint='← → 键或空格逐境游览 · 末境可点击池水，涟漪层层皱开、鹊鸣报喜',
    cover_read='谒金门·风乍起。五代，冯延巳。风乍起，吹皱一池春水。闲引鸳鸯香径里，手挼红杏蕊。',
    cover_p1='两重意境，随词句次第展开：先入春日园池，看风乍起处一池春水被吹起层层细皱，鸳鸯在香径水面成双缓游，她随手揉搓着红杏花蕊；再倚上刻有斗鸭的阑干，看碧玉搔头斜坠，终日望君君不至——举头忽闻鹊喜。',
    cover_p2='边读词，边走进五代南唐词人笔下那个春水皱、人独倚的相思黄昏。',
    end_h2='鹊声报喜', cn_word='两',
    words_js="['再游一次，一池春水','初识冯词，尚需共读','渐入佳境，再诵几遍','春水已皱，君犹未至','鹊声报喜，深得其味','风乍起处，吹皱千年春水']",
    sky_atmo='0x2f4a34',
    residual=('将进酒', '万古愁', '太白'),
)

POEM_JS = io.open(os.path.join(_here, 'yejinmen-fengzha_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yejinmen-fengzha_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yejinmen-fengzha_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yejinmen-fengzha_stages.js'), encoding='utf-8').read()
