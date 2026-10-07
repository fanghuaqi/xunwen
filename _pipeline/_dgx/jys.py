# -*- coding: utf-8 -*-
"""jys.py —— 《静夜思》（唐·李白，旧引擎页回填重建，水墨夜思）生成配置"""

META = dict(
    N=4, slug='jingyesi', title='静夜思', dyn='唐 · 李白', brand_author='李 白',
    gold_rgb='201,211,224',
    root=""":root{
  --gold:#c9d3e0; --ink:#dfe6f0; --dim:#8b98ac; --paper:rgba(12,16,24,.60);
  --line:rgba(180,195,215,.25);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    # 水墨夜色必改清单（逐项对应旧页 jingyesi/index.html 的等价物；:root 值照抄旧页，变量名 --silver→--gold 供引擎引用）
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),      # body + #err → 水墨夜色
        ('rgba(5,8,15', 'rgba(13,17,23', 1),                  # #cover 渐变内圈 → 旧页深蓝
        ('rgba(4,6,11,.9)', 'rgba(8,11,17,.9)', 1),           # #ending 渐变外圈 → 旧页
        ('rgba(4,6,11', 'rgba(8,11,17', 1),                   # #cover 渐变外圈 → 旧页
        ('rgba(6,9,16,.42)', 'rgba(13,18,27,.45)', 1),        # #ending 渐变内圈 → 旧页
        ('rgba(3,5,9,.72)', 'rgba(6,9,14,.74)', 1),           # #quiz 遮罩 → 旧页
        ('#0b101c', '#10161f', 1),                            # #quizCard 深底 → 旧页
        ('#6f664f', '#6d7889', 1),                            # #coverHint 文字色 → 旧页
        ('#5a5340', '#5b6574', 1),                            # .credit 文字色 → 旧页
    ],
    # 本诗作者就是李白：覆盖禁词表，避免 build 残留自检误伤 quiz 对「李白」的合法提及
    residual=('将进酒', '万古愁', '太白'),
    tip='轻点画面 / 按空格 —— 点亮故乡灯火',
    hint='← → 键或空格逐境游览 · 末境可点击画面点亮故乡灯火',
    cover_read='静夜思。唐，李白。床前明月光，疑是地上霜。举头望明月，低头思故乡。',
    cover_p1='四重意境，随诗句次第展开：看床前月光如练穿窗，如霜满地；随诗人举头望一轮冷银明月，穿过流云；再低头遥想千里之外，那一豆温热的故乡灯火。',
    cover_p2='边读诗，边走进那个安静的秋夜，体会李白藏在月光里的一缕乡愁。',
    end_h2='月明 · 乡思', cn_word='四',
    words_js="['再游一次，月光会记得你','初识静夜，尚需共读','诗意渐明，月色可亲','颇解诗情，可对月吟','深得诗心，低头亦见月','诗仙知己，乡思相通']",
    sky_atmo='0x1d2836',
)

import io, os
_here = os.path.dirname(os.path.abspath(__file__))
POEM_JS = io.open(os.path.join(_here, 'jys_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'jys_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'jys_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'jys_stages.js'), encoding='utf-8').read()
