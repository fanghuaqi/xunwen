# -*- coding: utf-8 -*-
"""yongyule-jingkou.py —— 《永遇乐·京口北固亭怀古》（宋·辛弃疾，queue no.194，大漠金戈）生成配置
美术立意：大漠金戈赛道（底色 #120d08、雾 #1a120a 系、accent=#c9a06a 取自 queue），暮色怀古、苍茫悲壮；
accent 用于人物边缘光/旗纹/祠庙轮廓光，禁艳金。全页意象链：斜阳—尘霭—战旗—烽烟—神鸦社鼓。
稼轩怀古压卷、用典最密：孙权→刘裕→刘义隆→佛狸→廉颇五典连环是教学骨架。
标志性瞬间：境②「金戈铁马气吞万里如虎」（斜阳巷陌外铁骑碾尘，全页最亮一境）
            对 境④「佛狸祠下神鸦社鼓」（沦陷区的太平假象，香火最暖、心底最寒）。
末境点击（queue interact）：点击烽火扬州路——烽烟起落 + 「廉颇老矣，尚能饭否」问句悬空。
情感曲线：怅惘无觅 → 昂扬追慕 → 沉痛警醒 → 最沉一问（收束留白）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yongyule-jingkou', title='永遇乐·京口北固亭怀古', dyn='宋 · 辛弃疾', brand_author='辛 弃 疾',
    gold_rgb='201,160,106',
    root=""":root{
  --gold:#c9a06a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(201,160,106,.3);
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
    tip='轻点画面 / 按空格 —— 烽烟起落，「凭谁问」悬空作结',
    hint='← → 键或空格逐境游览 · 末境可点击画面：烽烟起落，问句悬空',
    cover_read='永遇乐。宋，辛弃疾。千古江山，英雄无觅，孙仲谋处。舞榭歌台，风流总被，雨打风吹去。斜阳草树，寻常巷陌，人道寄奴曾住。想当年，金戈铁马，气吞万里如虎。元嘉草草，封狼居胥，赢得仓皇北顾。四十三年，望中犹记，烽火扬州路。可堪回首，佛狸祠下，一片神鸦社鼓。凭谁问，廉颇老矣，尚能饭否？',
    cover_p1='四重意境，随词句次第展开：登北固亭怀古——千古江山，英雄无觅孙仲谋处，舞榭歌台俱成陈迹；斜阳巷陌，人道寄奴曾住，遥想金戈铁马、气吞万里如虎；元嘉草草，赢得仓皇北顾，四十三年，烽火扬州路犹在望中；最后面对佛狸祠下的神鸦社鼓，发出「凭谁问：廉颇老矣，尚能饭否」的最沉一问。',
    cover_p2='边读词，边登上京口北固亭：五典连环（孙权、刘裕、刘义隆、佛狸、廉颇），一典一叹——追慕英雄、警告草率、痛心沦陷，收束处是老臣无人过问的悲愤留白。',
    end_h2='千古 · 老臣心', cn_word='四',
    words_js="['再登北固亭','初读稼轩，尚需共读','渐入词境，略有所感','五典已识其半','渐懂老臣之心','稼轩肝胆，千载犹闻']",
    sky_atmo='0x332414',
)

POEM_JS = io.open(os.path.join(_here, 'yongyule-jingkou_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yongyule-jingkou_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yongyule-jingkou_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yongyule-jingkou_stages.js'), encoding='utf-8').read()
