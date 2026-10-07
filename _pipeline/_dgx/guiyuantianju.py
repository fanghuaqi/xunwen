# -*- coding: utf-8 -*-
"""guiyuantianju.py —— 《归园田居·其三》（魏晋·陶渊明，no.138，青绿春晓·月归变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='guiyuantianju', title='归园田居·其三', dyn='魏晋 · 陶渊明', brand_author='陶渊明',
    gold_rgb='159,206,143',
    root=""":root{
  --gold:#9fce8f; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(159,206,143,.30);
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
    tip='轻点画面 / 按空格 —— 露珠凝亮，豆影摇曳',
    hint='← → 键或空格逐境游览 · 末境可点击画面，露珠凝亮',
    cover_read='归园田居其三。魏晋，陶渊明。种豆南山下，草盛豆苗稀。晨兴理荒秽，带月荷锄归。',
    cover_p1='四重意境，随诗句次第展开：南山种豆、草盛苗稀的自嘲；晨兴理荒秽、带月荷锄归的月夜剪影；道狭草木长、夕露沾我衣的归途；末了一句衣沾不足惜，但使愿无违。',
    cover_p2='边读诗，边走进陶渊明那躬耕陇亩、甘之如饴的田园世界。',
    end_h2='带月荷锄', cn_word='四',
    words_js="['再入诗境，且随月归','初识五柳，尚需共读','渐入田园，略有会意','辛劳渐识，粒粒皆辛','深得渊明躬耕之乐','愿无违处，月色满襟']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'guiyuantianju_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'guiyuantianju_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'guiyuantianju_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'guiyuantianju_stages.js'), encoding='utf-8').read()
