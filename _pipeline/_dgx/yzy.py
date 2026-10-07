# -*- coding: utf-8 -*-
"""yzy.py —— 《游子吟》（唐·孟郊，旧引擎页回填重建第 4 首，宣纸暖烛·浅色暖变体）生成配置"""

META = dict(
    N=3, slug='youziyin', title='游子吟', dyn='唐 · 孟郊', brand_author='孟 郊',
    gold_rgb='138,90,42',
    root=""":root{
  --gold:#8a5a2a; --ink:#2e2418; --dim:#7a6a50; --paper:rgba(255,250,238,.75);
  --line:rgba(138,90,42,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    # 浅色暖烛必改清单（逐项对应旧页 youziyin/index.html 的宣纸暖色等价物）
    repl_colors=[
        ('background:#05070d', 'background:#efe6d0', 2),      # body + #err → 浅宣纸底
        ('rgba(5,8,15,.25)', 'rgba(255,250,238,.12)', 1),     # #cover 渐变内圈 → 纸白
        ('rgba(4,6,11,.9)', 'rgba(214,196,158,.88)', 1),      # #ending 渐变外圈 → 旧页暖灰
        ('rgba(4,6,11', 'rgba(220,202,164,.80)', 1),          # #cover 渐变外圈 → 旧页暖灰
        ('rgba(6,9,16,.42)', 'rgba(255,250,238,.30)', 1),     # #ending 渐变内圈 → 纸白
        ('rgba(3,5,9,.72)', 'rgba(88,68,40,.38)', 1),         # #quiz 遮罩 → 旧页暖赭
        ('#0b101c', '#fbf5e4', 1),                            # #quizCard 深底 → 米白卡
        ('#6f664f', '#94835f', 1),                            # #coverHint 文字色 → 旧页
        ('#5a5340', '#a8956e', 1),                            # .credit 文字色 → 旧页
    ],
    # 交互按引擎约定挂在末境（三春晖）：旧页 TIP 在第二境（加一针），新页改为春晖大盛
    tip='轻点画面 / 按空格 —— 春晖大盛，暖满原野',
    hint='← → 键或空格逐境游览 · 第三境可轻点画面沐满春晖',
    cover_read='游子吟。唐，孟郊。慈母手中线，游子身上衣。临行密密缝，意恐迟迟归。谁言寸草心，报得三春晖。',
    cover_p1='三重意境，随诗句次第展开：烛下慈母手中线，油灯前一针一线密密缝，直到推门而出天光大亮 —— 寸草春晖，一线相牵。',
    cover_p2='边读诗，边走进孟郊笔下那盏灯、那件衣、那片春晖。',
    end_h2='寸草 · 春晖', cn_word='三',
    words_js="['再游一次，重拈针线','初闻游子吟，尚需细读','孝心渐明，如沐春晖','一线一针，渐入诗心','深得诗中三昧','寸草之心，已报春晖']",
    sky_atmo='0xdbc9a6',
)

import io, os
_here = os.path.dirname(os.path.abspath(__file__))
POEM_JS = io.open(os.path.join(_here, 'yzy_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yzy_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yzy_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yzy_stages.js'), encoding='utf-8').read()
