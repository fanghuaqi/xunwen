# -*- coding: utf-8 -*-
"""jinyuyi.py —— 《金缕衣》（唐·杜秋娘，no.209，夜宴金彩·中唐劝时曲变体）生成配置
二境（queue.json 分境口径）：金缕少年（夜宴灯彩+金缕华服光华+持花劝时人+惜取少年时）、
花开堪折（标志性瞬间·末境可点击：金缕光华渐淡 vs 花枝盛放催折的时序对切）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

def io_open(name):
    return io.open(os.path.join(_here, name), encoding='utf-8').read()

META = dict(
    N=2, slug='jinyuyi', title='金缕衣', dyn='唐 · 杜秋娘', brand_author='杜秋娘',
    gold_rgb='212,168,79',
    root=""":root{
  --gold:#d4a84f; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(212,168,79,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(9,7,4', 1),
        ('rgba(4,6,11', 'rgba(8,6,3', 2),
        ('rgba(6,9,16', 'rgba(10,7,4', 1),
        ('rgba(3,5,9', 'rgba(7,5,3', 1),
        ('#0b101c', '#161006', 1),
        ('#6f664f', '#6e5e44', 1),
        ('#5a5340', '#60523e', 1),
    ],
    tip='轻点画面 / 按空格 —— 点击花开：金缕光华渐淡，花枝盛放催折',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看金缕光华渐淡、花枝盛放催折',
    cover_read='金缕衣。唐，杜秋娘。劝君莫惜金缕衣，劝君惜取少年时。花开堪折直须折，莫待无花空折枝。',
    cover_p1='两重意境，随诗句次第展开：劝君莫惜金缕衣、劝君惜取少年时的富贵与光阴之择；花开堪折直须折、莫待无花空折枝的殷殷催促。',
    cover_p2='边读诗，边走进杜秋娘那场金彩夜宴，听一曲中唐最著名的劝时之歌，体会「花开堪折直须折」的紧迫与恳切。',
    end_h2='惜取 · 少年', cn_word='二',
    words_js="['再读一次，惜取少年时','初识劝时曲，尚需共读','渐入佳境，再诵几遍','金缕与花枝，取舍渐明','深解「莫待空折枝」之切','花开堪折，莫负少年时']",
    sky_atmo='0x3a2c1e',
)

POEM_JS = io_open('jinyuyi_poem.js')
QUIZ_JS = io_open('jinyuyi_quiz.js')
SCENES_JS = io_open('jinyuyi_scenes.js')
STAGES_JS = io_open('jinyuyi_stages.js')
