# -*- coding: utf-8 -*-
"""nanxiangzi-jingkou.py —— 《南乡子·登京口北固亭有怀》（宋·辛弃疾，queue no.193，大漠金戈）生成配置
美术立意：大漠金戈赛道（底色 #120d08、雾 #1a120a 系、accent=#c49a5a 取自 queue），但本诗在江上——
京口北固亭下临长江，故以「暮色大江」承载赛道：赭金 accent 用于栏柱/人物边缘光/旗影，禁艳金；
江涛与战旗是全页动态元素。三问三答是全词骨架（何处望神州？千古兴亡多少事？谁敌手？），
「神州不可见」的怅惘（境①压暗、尘霭锁江天）与「少年英主」的昂扬（境③火光、军阵、战旗）对比。
标志性瞬间「不尽长江滚滚流」（境②）：亭上凭栏，千叠浪着色器滚滚东去，以大江回答千古一问；
末境点击北固亭：亭头远望 + 江浪千叠涌起，答千古一问，"生子当如孙仲谋"题字同现。
情感曲线：怅惘北望 → 苍茫江声 → 少年昂扬 → 江声作答。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='nanxiangzi-jingkou', title='南乡子·登京口北固亭有怀', dyn='宋 · 辛弃疾', brand_author='辛 弃 疾',
    gold_rgb='196,154,90',
    root=""":root{
  --gold:#c49a5a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(196,154,90,.3);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(24,16,9', 1),
        ('rgba(4,6,11', 'rgba(12,8,5', 2),
        ('rgba(6,9,16', 'rgba(24,16,9', 1),
        ('rgba(3,5,9', 'rgba(8,5,3', 1),
        ('#0b101c', '#181009', 1),
        ('#6f664f', '#7a6a50', 1),
        ('#5a5340', '#6a5a44', 1),
    ],
    tip='轻点画面 / 按空格 —— 江浪千叠，答千古一问',
    hint='← → 键或空格逐境游览 · 末境可点击北固亭：江浪千叠，答千古一问',
    cover_read='南乡子。宋，辛弃疾。何处望神州？满眼风光北固楼。千古兴亡多少事？悠悠。不尽长江滚滚流。',
    cover_p1='四重意境，随词句次第展开：登上北固楼，满眼风光，可神州在哪里？千古兴亡多少事，都付眼前一江滚滚东流水；遥想年少孙权统率万兜鍪，坐断东南、战未休，天下英雄谁堪敌手？曹刘——连曹操也感叹：生子当如孙仲谋。',
    cover_p2='边读词，边登上京口北固亭：三问三答层层递进，「神州不可见」的怅惘与「少年英主」的昂扬，最终都交给大江去回答。',
    end_h2='千古 · 江声', cn_word='四',
    words_js="['再游一次，亭上北望','初识稼轩，尚需共读','渐入词境，略有所感','英雄之气渐生','已解亭上三问','稼轩豪情，江水长流']",
    sky_atmo='0x332414',
)

POEM_JS = io.open(os.path.join(_here, 'nanxiangzi-jingkou_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'nanxiangzi-jingkou_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'nanxiangzi-jingkou_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'nanxiangzi-jingkou_stages.js'), encoding='utf-8').read()
