# -*- coding: utf-8 -*-
"""xinggong.py —— 《行宫》（唐·元稹，no.249，宣纸留白·荒宫白头变体）生成配置
诗眼「白头宫女在，闲坐说玄宗」：宫花寂寞红（唯一致命浓色）对白头宫女（时间感）。
末境点击说玄宗 → 昔日行宫的繁华虚影自残宫之上浮现、驻留又淡去（闪回），题字「说玄宗」。
宣纸留白：纸底、淡墨远山、浓墨残宫；不设水、不用金色辉光（浅色赛道必改清单已逐项过）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='xinggong', title='行宫', dyn='唐 · 元稹', brand_author='元 稹',
    gold_rgb='80,72,74',
    root=""":root{
  --gold:#50484a; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(80,72,74,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(233,226,208', 1),
        ('rgba(4,6,11', 'rgba(212,202,176', 2),
        ('rgba(6,9,16', 'rgba(233,226,208', 1),
        ('rgba(3,5,9', 'rgba(236,230,214', 1),
        ('#0b101c', '#f6f1e1', 1),
        ('#6f664f', '#8a8268', 1),
        ('#5a5340', '#8d8571', 1),
        ('0x0a1526', '0xe6dfcc', 4),
    ],
    tip='轻点说玄宗 / 按空格 —— 残宫之上，昔日繁华一闪而过',
    hint='← → 键或空格逐境游览 · 末境可点击说玄宗：繁华虚影闪回',
    cover_read='行宫。唐，元稹。寥落古行宫，宫花寂寞红。白头宫女在，闲坐说玄宗。',
    cover_p1='两重意境，随诗句次第展开：冷落荒凉的古行宫，宫花寂寞地红着；只有白头的老宫女还在，闲坐着说起当年的玄宗。',
    cover_p2='边读诗，边走进那座荒宫：花开得越红，越见其寂寞；白头人一开口，一朝盛衰便尽在二十字中。',
    end_h2='白头 · 说玄宗', cn_word='两',
    words_js="['再游一次，荒宫残阶','初识微之，尚需共读','渐入佳境，再诵几遍','宫花仍红，白头犹在','已识以小儿大之法','寥落行宫，闲说玄宗']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = io.open(os.path.join(_here, 'xinggong_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xinggong_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xinggong_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xinggong_stages.js'), encoding='utf-8').read()
