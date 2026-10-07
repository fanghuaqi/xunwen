# -*- coding: utf-8 -*-
"""maowu.py —— 《茅屋为秋风所破歌》（唐·杜甫，no.146，水墨夜思·破庐变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='maowu', title='茅屋为秋风所破歌', dyn='唐 · 杜甫', brand_author='杜 甫',
    gold_rgb='138,154,176',
    root=""":root{
  --gold:#8a9ab0; --ink:#dfe3ea; --dim:#7c8290; --paper:rgba(10,11,16,.60);
  --line:rgba(138,154,176,.28);
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
    tip='轻点暗夜 / 按空格 —— 广厦升起，亮窗庇寒士',
    hint='← → 键或空格逐境游览 · 末境可点击暗夜，广厦升起',
    cover_read='茅屋为秋风所破歌。唐，杜甫。八月秋高风怒号，卷我屋上三重茅。',
    cover_p1='四重意境，随诗句次第展开：秋风怒号卷走三重茅；群童抱茅、倚杖叹息；风定云墨、雨脚如麻的长夜；最后于破屋之中发出「安得广厦千万间，大庇天下寒士俱欢颜」的千古呼喊。',
    cover_p2='边读诗，边走进杜甫那由一己之寒推及天下寒士的博大胸怀。',
    end_h2='广厦寒士', cn_word='四',
    words_js="['再读一次，秋风茅屋','初识杜工部，尚需共读','渐入长夜，略有所感','寒意渐识，推己及人','深得忧民之怀','广厦万间，欢颜俱现']",
    sky_atmo='0x323448',
)

POEM_JS = io.open(os.path.join(_here, 'maowu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'maowu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'maowu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'maowu_stages.js'), encoding='utf-8').read()
