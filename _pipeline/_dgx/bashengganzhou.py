# -*- coding: utf-8 -*-
"""bashengganzhou.py —— 《八声甘州·对潇潇暮雨洒江天》（宋·柳永，no.170，水墨夜思）生成配置
美术立意：柳永羁旅长调压卷。全页禁金，冷银水墨 #98aec8 主调、暮雨/霜风/寒江俱冷；
残照是全页唯一锈赭低饱和暖色（同《忆秦娥》先例）。
标志性瞬间「残照当楼」：一束残照打在江楼之上，而天地俱冷——苏轼所谓「不减唐人高处」。
末境点击倚阑干：倚栏人影凝愁显形，天际归舟虚影往复；妆楼颙望（她眼中）与游子倚栏（我眼中）两面对写。
情感曲线：雨洗清秋 → 江水无语 → 归思难收 → 两地凝愁。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='bashengganzhou', title='八声甘州', dyn='宋 · 柳永', brand_author='柳 永',
    gold_rgb='152,174,200',
    root=""":root{
  --gold:#98aec8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(152,174,200,.26);
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
    tip='轻点画面 / 按空格 —— 倚栏人影凝愁，天际归舟虚影往复',
    hint='← → 键或空格逐境游览 · 末境可点击倚阑干：人影凝愁显形，归舟虚影往复',
    cover_read='八声甘州。宋，柳永。对潇潇暮雨洒江天，一番洗清秋。渐霜风凄紧，关河冷落，残照当楼。',
    cover_p1='四重意境，随词句次第展开：潇潇暮雨洒遍江天，霜风凄紧里，一束残照正照楼头；红衰翠减、物华渐休，惟有长江水无语东流；不忍登高临远，故乡渺邈，归思难收；妆楼颙望的她与倚阑干的我，隔着一江秋水，同一种凝愁。',
    cover_p2='边读词，边走进柳永笔下这秋江暮色的羁旅乡愁——苏轼盛赞其「不减唐人高处」。',
    end_h2='凝愁 · 归思', cn_word='四',
    words_js="['再游一次，暮雨江天','初识柳永，尚需共读','渐入词境，略有所感','秋思渐深，归意难收','已解倚栏凝愁之味','不减唐人高处']",
    sky_atmo='0x212c3c',
)

POEM_JS = io.open(os.path.join(_here, 'bashengganzhou_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'bashengganzhou_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'bashengganzhou_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'bashengganzhou_stages.js'), encoding='utf-8').read()
