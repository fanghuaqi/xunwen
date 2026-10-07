# -*- coding: utf-8 -*-
"""guohuaqinggong.py —— 《过华清宫》（唐·杜牧，no.234，夜宴金彩·骊山华清变体）生成配置
词眼「一骑红尘妃子笑」：骊山绝顶千重宫门次第洞开（门扇可动），驿道上一骑扬尘直上；
末境点击红尘 → 驿马加速、千门大开、妃子一笑。
与同为夜宴赛道的《将进酒》（酒器星河）不同：本页是骊山晚照的宫阙、锦绣山色与驿道红尘。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='guohuaqinggong', title='过华清宫', dyn='唐 · 杜牧', brand_author='杜 牧',
    gold_rgb='224,176,96',
    root=""":root{
  --gold:#e0b060; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(224,176,96,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,4', 1),
        ('rgba(4,6,11', 'rgba(7,5,3', 2),
        ('rgba(6,9,16', 'rgba(9,6,4', 1),
        ('rgba(3,5,9', 'rgba(6,4,3', 1),
        ('#0b101c', '#141008', 1),
        ('#6f664f', '#6b5c46', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点红尘 / 按空格 —— 一骑扬尘直上，千门次第洞开',
    hint='← → 键或空格逐境游览 · 末境可点击红尘：驿马疾驰扬尘，千门洞开、妃子一笑',
    cover_read='过华清宫。唐，杜牧。长安回望绣成堆，山顶千门次第开。一骑红尘妃子笑，无人知是荔枝来。',
    cover_p1='两重意境，随诗句次第展开：从长安回望骊山，宫殿花木如一堆堆锦绣，骊山绝顶的千重宫门正一重接一重地次第打开；驿道上一人一马扬尘飞驰而来，山顶贵妃展颜一笑——却无人知道，那千里飞骑送来的只是几筐荔枝。',
    cover_p2='边读诗，边走进晚唐诗人回望中的骊山：一座宫阙、一道红尘，写尽一个王朝的荒唐与疲敝。',
    end_h2='红尘 · 一笑', cn_word='两',
    words_js="['再望一次，骊山晚照','初识樊川，尚需共读','渐入佳境，再诵几遍','宫门渐开，红尘渐近','已识讽喻之意','一骑红尘，无人知是荔枝来']",
    sky_atmo='0x3a2c20',
)

POEM_JS = io.open(os.path.join(_here, 'guohuaqinggong_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'guohuaqinggong_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'guohuaqinggong_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'guohuaqinggong_stages.js'), encoding='utf-8').read()
