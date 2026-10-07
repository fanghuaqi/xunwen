# -*- coding: utf-8 -*-
"""taohuaxi.py —— 《桃花溪》（唐·张旭，no.252，水墨夜思·桃源问津变体）生成配置
诗眼「洞在清溪何处边」：野烟迷离中飞桥隐约、桃花尽日随流水。
末境点击清溪 → 野烟散处（烟片缩到 28%）飞桥现出、桃花随流水溯溪而上（流向 +1→−1 平滑反转）、
云烟深处洞口微现，题字「洞在清溪何处边」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='taohuaxi', title='桃花溪', dyn='唐 · 张旭', brand_author='张 旭',
    gold_rgb='164,182,204',
    root=""":root{
  --gold:#a4b6cc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(164,182,204,.26);
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
    tip='轻点清溪 / 按空格 —— 野烟散处飞桥现，桃花溯溪问洞天',
    hint='← → 键或空格逐境游览 · 末境可点击清溪：烟散桥现，桃花溯溪而上',
    cover_read='桃花溪。唐，张旭。隐隐飞桥隔野烟，石矶西畔问渔船。桃花尽日随流水，洞在清溪何处边。',
    cover_p1='两重意境，随诗句次第展开：隐隐一座飞桥隔着野外雾霭，在石矶西边向渔船打听；桃花整日随着流水漂去，那桃源洞口究竟在清溪哪一边？',
    cover_p2='边读诗，边走进这场寻访：烟不散，桥不清；问而不答，才是全诗余味。',
    end_h2='桃花 · 问洞', cn_word='两',
    words_js="['再溯一程，野烟清溪','初识张颠，尚需共读','渐入佳境，再诵几遍','烟散桥现，花随水转','已识桃源之问','洞在清溪何处边']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = io.open(os.path.join(_here, 'taohuaxi_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'taohuaxi_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'taohuaxi_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'taohuaxi_stages.js'), encoding='utf-8').read()
