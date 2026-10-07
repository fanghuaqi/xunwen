# -*- coding: utf-8 -*-
"""wuti.py —— 《无题·相见时难别亦难》（唐·李商隐，no.152，烟雨江南·相思变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='wuti', title='无题·相见时难别亦难', dyn='唐 · 李商隐', brand_author='李 商 隐',
    gold_rgb='192,138,168',
    root=""":root{
  --gold:#c08aa8; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(192,138,168,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#131a24', 1),
        ('#6f664f', '#5f6a7a', 1),
        ('#5a5340', '#525c6c', 1),
    ],
    tip='轻点画面 / 按空格 —— 青鸟衔书，飞向蓬山',
    hint='← → 键或空格逐境游览 · 末境可点击画面，青鸟衔书探看',
    cover_read='无题相见时难别亦难。唐，李商隐。相见时难别亦难，东风无力百花残。',
    cover_p1='四重意境，随诗句次第展开：相见时难、百花凋残的凄恻；春蚕到死、蜡炬成灰的至情；晓镜愁鬓、夜吟月寒的设身相思；蓬山无多路、青鸟为探看的缥缈希冀。',
    cover_p2='边读诗，边走进李商隐那幽约怨怼、至死不渝的相思绝唱。',
    end_h2='青鸟探看', cn_word='四',
    words_js="['再读一次，春蚕蜡炬','初识义山，尚需共读','渐入深情，略有所感','相思渐浓，丝尽泪干','深得幽微缠绵之妙','蓬山无多路，青鸟为探看']",
    sky_atmo='0x3c3444',
)

POEM_JS = io.open(os.path.join(_here, 'wuti_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'wuti_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'wuti_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'wuti_stages.js'), encoding='utf-8').read()
