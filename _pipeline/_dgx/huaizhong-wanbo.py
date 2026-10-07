# -*- coding: utf-8 -*-
"""huaizhong-wanbo.py —— 《淮中晚泊犊头》（宋·苏舜钦，no.246，水墨夜思·淮上春阴变体）生成配置
诗眼「满川风雨看潮生」：春阴垂野、青草连天、一树幽花独明；晚泊孤舟于古祠之下。
末境点击看潮生 → 雨密风急、满川潮头自远而近推进、孤舟随浪起伏、水波振幅加大，题字「满川风雨看潮生」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='huaizhong-wanbo', title='淮中晚泊犊头', dyn='宋 · 苏舜钦', brand_author='苏舜钦',
    gold_rgb='152,168,184',
    root=""":root{
  --gold:#98a8b8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(152,168,184,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(7,10,16', 1),
        ('rgba(4,6,11', 'rgba(6,8,14', 2),
        ('rgba(6,9,16', 'rgba(7,9,15', 1),
        ('rgba(3,5,9', 'rgba(5,7,12', 1),
        ('#0b101c', '#101624', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
    ],
    tip='轻点看潮生 / 按空格 —— 风急雨密，满川潮头暗涌',
    hint='← → 键或空格逐境游览 · 末境可点击看潮生：风雨渐起，潮头自远而近',
    cover_read='淮中晚泊犊头。宋，苏舜钦。春阴垂野草青青，时有幽花一树明。晚泊孤舟古祠下，满川风雨看潮生。',
    cover_p1='两重意境，随诗句次第展开：春天阴云低垂原野、青草青青，不时有一树幽僻之花格外明亮；傍晚把孤舟泊在古祠之下，满川风雨里坐着看潮水涨起。',
    cover_p2='边读诗，边走进淮上那个春阴的傍晚：天地晦暗，唯此一树明；风雨潮生，而人从容。',
    end_h2='潮生 · 风雨', cn_word='两',
    words_js="['再泊一夜，淮上看潮','初识沧浪，尚需共读','渐入佳境，再诵几遍','风雨渐急，潮头渐近','已识静中看动之意','满川风雨看潮生']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = io.open(os.path.join(_here, 'huaizhong-wanbo_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'huaizhong-wanbo_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'huaizhong-wanbo_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'huaizhong-wanbo_stages.js'), encoding='utf-8').read()
