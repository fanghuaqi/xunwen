# -*- coding: utf-8 -*-
"""sanchu-daozhong.py —— 《三衢道中》（宋·曾几，no.244，青绿春晓·三衢山行变体）生成配置
诗眼「绿阴不减来时路，添得黄鹂四五声」：初夏梅黄、溪舟已尽、石径上山，归途绿荫夹道。
末境点击黄鹂 → 四五声啼鸣（五声音阶）、黄鹂挺颈振羽、绿阴与叶隙光斑一起摇动，题字「绿阴黄鹂」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='sanchu-daozhong', title='三衢道中', dyn='宋 · 曾几', brand_author='曾 几',
    gold_rgb='149,201,168',
    root=""":root{
  --gold:#95c9a8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(149,201,168,.30);
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
    tip='轻点黄鹂 / 按空格 —— 四五声啼鸣，绿阴光影摇动',
    hint='← → 键或空格逐境游览 · 末境可点击黄鹂：啼声四五，绿阴光影摇曳',
    cover_read='三衢道中。宋，曾几。梅子黄时日日晴，小溪泛尽却山行。绿阴不减来时路，添得黄鹂四五声。',
    cover_p1='两重意境，随诗句次第展开：梅子黄熟的时节天天放晴，乘船游到小溪尽头，就改走山路；归途的绿荫不比来时少，还多了黄鹂四五声清脆的啼鸣。',
    cover_p2='边读诗，边走进三衢道中的初夏：一次寻常的返程，因这几声鸟鸣而活了起来。',
    end_h2='绿阴 · 黄鹂', cn_word='两',
    words_js="['再游一次，三衢山道','初识茶山，尚需共读','渐入佳境，再诵几遍','绿阴正浓，鹂声初起','已识归途添趣','绿阴不减，黄鹂四五声']",
    sky_atmo='0x2f4a34',
)

POEM_JS = io.open(os.path.join(_here, 'sanchu-daozhong_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'sanchu-daozhong_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'sanchu-daozhong_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'sanchu-daozhong_stages.js'), encoding='utf-8').read()
