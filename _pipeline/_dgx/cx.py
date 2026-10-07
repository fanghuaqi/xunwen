# -*- coding: utf-8 -*-
"""cx.py —— 《春晓》（唐·孟浩然，旧引擎页回填重建，青绿春晓）生成配置"""

META = dict(
    N=4, slug='chunxiao', title='春晓', dyn='唐 · 孟浩然', brand_author='孟 浩 然',
    gold_rgb='159,206,143',
    root=""":root{
  --gold:#9fce8f; --ink:#eef4e6; --dim:#8ba986; --paper:rgba(10,20,14,.60);
  --line:rgba(159,206,143,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    # 青绿春晓必改清单（逐项对应旧页 chunxiao/index.html 的等价物）
    repl_colors=[
        ('background:#05070d', 'background:#0a1410', 2),      # body + #err → 青绿底
        ('rgba(5,8,15', 'rgba(6,12,9', 1),                    # #cover 渐变内圈 → 旧页墨绿
        ('rgba(4,6,11,.9)', 'rgba(4,10,7,.9)', 1),            # #ending 渐变外圈 → 旧页
        ('rgba(4,6,11', 'rgba(4,10,7', 1),                    # #cover 渐变外圈 → 旧页
        ('rgba(6,9,16,.42)', 'rgba(6,12,9,.42)', 1),          # #ending 渐变内圈 → 旧页
        ('rgba(3,5,9,.72)', 'rgba(4,8,6,.74)', 1),            # #quiz 遮罩 → 旧页
        ('#0b101c', '#0c1612', 1),                            # #quizCard 深底 → 旧页
        ('#6f664f', '#6d8668', 1),                            # #coverHint 文字色 → 旧页
        ('#5a5340', '#5c7360', 1),                            # .credit 文字色 → 旧页
    ],
    tip='轻点画面 / 按空格 —— 花落更急，满地落英',
    hint='← → 键或空格逐境游览 · 末境可点击画面再赏落英',
    cover_read='春晓。唐，孟浩然。春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。',
    cover_p1='四重意境，随诗句次第展开：从一夜酣眠到处处啼鸟，忽忆夜来风雨，再看落花满地 —— 在渐亮的天光与飘落的花瓣里，读懂一个「晓」字。',
    cover_p2='边读诗，边走进孟浩然笔下那个清新恬淡而又略带怅然的春晨。',
    end_h2='雨霁 · 惜春', cn_word='四',
    words_js="['再游一次，细听啼鸟','初识浩然，尚需共读','诗意渐浓，春光正好','渐入佳境，花枝相招','深得惜春之心','诗境知己，满地花香']",
    sky_atmo='0x2e4633',
)

import io, os
_here = os.path.dirname(os.path.abspath(__file__))
POEM_JS = io.open(os.path.join(_here, 'cx_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'cx_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'cx_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'cx_stages.js'), encoding='utf-8').read()
