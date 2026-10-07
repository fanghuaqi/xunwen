# -*- coding: utf-8 -*-
"""yueyeyishe.py —— 《月夜忆舍弟》（唐·杜甫，no.143，水墨夜思·忆弟变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yueye-yishe', title='月夜忆舍弟', dyn='唐 · 杜甫', brand_author='杜 甫',
    gold_rgb='157,179,201',
    root=""":root{
  --gold:#9db3c9; --ink:#dfe6f0; --dim:#7e8ea0; --paper:rgba(9,13,22,.58);
  --line:rgba(157,179,201,.28);
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
    tip='轻点画面 / 按空格 —— 家书化作雁影，故乡月转明',
    hint='← → 键或空格逐境游览 · 末境可点击画面，故乡月转明',
    cover_read='月夜忆舍弟。唐，杜甫。戍鼓断人行，边秋一雁声。露从今夜白，月是故乡明。',
    cover_p1='四重意境，随诗句次第展开：戍鼓雁声的秋夜；露从今夜白、月是故乡明的移情；有弟皆分散、无家问死生的离散；寄书长不达、况乃未休兵的家国之痛。',
    cover_p2='边读诗，边走进杜甫那月白露冷、兄弟万里的思念之夜。',
    end_h2='月是故乡明', cn_word='四',
    words_js="['再读一次，白露月明','初识杜工部，尚需共读','渐入秋夜，略有所感','思念渐深，如露如霜','深得移情之妙','月是故乡明']",
    sky_atmo='0x26303f',
)

POEM_JS = io.open(os.path.join(_here, 'yueyeyishe_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yueyeyishe_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yueyeyishe_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yueyeyishe_stages.js'), encoding='utf-8').read()
