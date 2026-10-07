# -*- coding: utf-8 -*-
"""xue.py —— 《江雪》（唐·柳宗元，旧引擎页回填重建试点，宣纸留白·浅色）生成配置"""

META = dict(
    N=4, slug='jiangxue', title='江雪', dyn='唐 · 柳宗元', brand_author='柳 宗 元',
    gold_rgb='44,47,51',
    root=""":root{
  --gold:#2c2f33; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(44,47,51,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    # 浅色必改清单（逐项对应旧页 jiangxue/index.html 的宣纸浅色等价物）
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),      # body + #err → 宣纸底
        ('rgba(5,8,15', 'rgba(233,226,208', 1),               # #cover 渐变内圈 → 宣纸
        ('rgba(4,6,11,.9)', 'rgba(205,195,168,.94)', 1),      # #ending 渐变外圈 → 旧页暖灰
        ('rgba(4,6,11', 'rgba(212,202,176', 1),               # #cover 渐变外圈 → 旧页暖灰
        ('rgba(6,9,16,.42)', 'rgba(233,226,208,.5)', 1),      # #ending 渐变内圈 → 宣纸
        ('rgba(3,5,9,.72)', 'rgba(236,230,214,.78)', 1),      # #quiz 遮罩 → 宣纸
        ('#0b101c', '#f6f1e1', 1),                            # #quizCard 深底 → 米白卡
        ('#6f664f', '#8a8268', 1),                            # #coverHint 文字色 → 旧页
        ('#5a5340', '#8d8571', 1),                            # .credit 文字色 → 旧页
    ],
    tip='轻点江面 / 按空格 —— 雪落更急，钓竿轻摇',
    hint='← → 键或空格逐境游览 · 第四境可点击江面唤雪摇竿',
    cover_read='江雪。唐，柳宗元。千山鸟飞绝，万径人踪灭。孤舟蓑笠翁，独钓寒江雪。',
    cover_p1='四重意境，随诗句次第展开：看千山飞鸟绝迹，看万径踪影湮灭，走近寒江上一叶孤舟里蓑衣斗笠的老翁，最终置身天地皆白的茫茫江雪。',
    cover_p2='边读诗，边走进柳宗元笔下那个空寂、孤绝而又坚韧澄澈的世界。',
    end_h2='独钓 · 千秋', cn_word='四',
    words_js="['再入诗境，细品雪意','初识柳子厚，尚需共读','渐入寒江，略有会意','深得孤舟之境','蓑笠知音，孤高自守','雪满千山，独钓千秋']",
    sky_atmo='0xd8d2c0',
)

import io, os
_here = os.path.dirname(os.path.abspath(__file__))
POEM_JS = io.open(os.path.join(_here, 'xue_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xue_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xue_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xue_stages.js'), encoding='utf-8').read()
