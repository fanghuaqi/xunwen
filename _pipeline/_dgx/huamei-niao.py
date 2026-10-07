# -*- coding: utf-8 -*-
"""huamei-niao.py —— 《画眉鸟》（宋·欧阳修，no.245，青绿春晓·山花鸟鸣变体）生成配置
诗眼「不及林间自在啼」：林间画眉自由啼鸣（随意移），金笼里的画眉也在啼。
末境点击自在啼 → 笼门开启、笼中画眉飞出盘旋、与林间画眉一同振羽对啼，题字「自在啼」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='huamei-niao', title='画眉鸟', dyn='宋 · 欧阳修', brand_author='欧阳修',
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
    tip='轻点自在啼 / 按空格 —— 笼门开启，画眉飞向林间',
    hint='← → 键或空格逐境游览 · 末境可点击自在啼：笼门开、画眉飞出、与林间对啼',
    cover_read='画眉鸟。宋，欧阳修。百啭千声随意移，山花红紫树高低。始知锁向金笼听，不及林间自在啼。',
    cover_p1='两重意境，随诗句次第展开：画眉鸟千百声婉转、随意在林间飞来飞去，山花或红或紫、树木高高低低；这才知道，把它锁在金笼里听，远不如它在林间自在啼唱。',
    cover_p2='边读诗，边走进欧阳修笔下的春山：笼中的啼声再美，也美不过林间那一份自在。',
    end_h2='自在 · 啼', cn_word='两',
    words_js="['再听一次，林间鸟鸣','初识醉翁，尚需共读','渐入佳境，再诵几遍','笼门已开，啼声渐远','已识以鸟喻人','不及林间自在啼']",
    sky_atmo='0x2f4a34',
)

POEM_JS = io.open(os.path.join(_here, 'huamei-niao_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'huamei-niao_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'huamei-niao_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'huamei-niao_stages.js'), encoding='utf-8').read()
