# -*- coding: utf-8 -*-
"""juhua.py —— 《菊花》（唐·元稹，no.250，青绿春晓·秋菊绕舍变体）生成配置
诗眼「此花开尽更无花」：秋丛绕舍似陶家、遍绕篱边、日渐斜（低斜暖阳与地面长影）。
末境点击偏爱菊 → 斜阳更斜更暖、菊丛花光次第点亮、摇曳加剧，远处百花凋尽作对照，题字「此花开尽更无花」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='juhua', title='菊花', dyn='唐 · 元稹', brand_author='元 稹',
    gold_rgb='163,201,168',
    root=""":root{
  --gold:#a3c9a8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(163,201,168,.30);
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
    tip='轻点偏爱菊 / 按空格 —— 斜阳更斜，花光次第亮起',
    hint='← → 键或空格逐境游览 · 末境可点击偏爱菊：夕阳低斜，菊光点亮',
    cover_read='菊花。唐，元稹。秋丛绕舍似陶家，遍绕篱边日渐斜。不是花中偏爱菊，此花开尽更无花。',
    cover_p1='两重意境，随诗句次第展开：一丛丛秋菊绕着屋舍，简直像陶渊明的家，绕着篱笆看了一遍又一遍，太阳渐渐西斜；并非百花中偏爱菊，只因这菊花开尽后，一年里再没有花了。',
    cover_p2='边读诗，边走进那座似陶家的茅舍：愈是最后的好景，愈值得绕着篱边多看几遍。',
    end_h2='菊 · 更无花', cn_word='两',
    words_js="['再绕一圈，篱边菊丛','初识微之，尚需共读','渐入佳境，再诵几遍','斜阳更低，花光更亮','已识惜时之意','此花开尽更无花']",
    sky_atmo='0x4a5a34',
)

POEM_JS = io.open(os.path.join(_here, 'juhua_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'juhua_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'juhua_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'juhua_stages.js'), encoding='utf-8').read()
