# -*- coding: utf-8 -*-
"""songyouren.py —— 《送友人》（唐·李白，no.142，水墨夜思·送别变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='songyouren', title='送友人', dyn='唐 · 李白', brand_author='李 白',
    gold_rgb='147,168,189',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#93a8bd; --ink:#dfe6f0; --dim:#7e8ea0; --paper:rgba(9,13,22,.58);
  --line:rgba(147,168,189,.28);
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
    tip='轻点画面 / 按空格 —— 班马萧萧长鸣',
    hint='← → 键或空格逐境游览 · 末境可点击画面，班马长鸣',
    cover_read='送友人。唐，李白。青山横北郭，白水绕东城。此地一为别，孤蓬万里征。',
    cover_p1='四重意境，随诗句次第展开：青山横郭、白水绕城的送别之地；此地一别、孤蓬万里的漂泊；浮云游子、落日故人的情景互喻；挥手自兹、萧萧班马的余音。',
    cover_p2='边读诗，边走进李白那情随景生、余音袅袅的送别时刻。',
    end_h2='班马萧萧', cn_word='四',
    words_js="['再读一次，青山白水','初识太白，尚需共读','渐入别情，略有所感','离绪渐生，如水如云','深得情景互喻之妙','班马萧萧，余音袅袅']",
    sky_atmo='0x22344c',
)

POEM_JS = io.open(os.path.join(_here, 'songyouren_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'songyouren_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'songyouren_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'songyouren_stages.js'), encoding='utf-8').read()
