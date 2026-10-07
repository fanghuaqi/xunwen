# -*- coding: utf-8 -*-
"""guizhixiang-jinling.py —— 《桂枝香·金陵怀古》（宋·王安石，queue no.172，大漠金戈·怀古变体）生成配置
美术立意：同《潼关怀古》大漠怀古先例——底色 #120d08、雾 #1a120a、主色灰沉、禁艳金；
本诗自开两色：澄江白练（低饱和暖白，全页唯一亮色，取「澄江似练」）与残阳锈赭（低饱和金照）。
标志性瞬间「千里澄江似练」（境①）：登临俯瞰，长江如一匹白绢在暮秋天地里铺展，翠峰攒聚如簇。
末境点击澄江似练：江面展白绢 + 六朝残迹（城砖/断柱/残碑）浮沉；「至今商女时时犹唱」以
拨弦余音作全篇听觉收束。
情感曲线：肃爽登临 → 残阳如画 → 悲恨相续 → 余音不绝。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='guizhixiang-jinling', title='桂枝香·金陵怀古', dyn='宋 · 王安石', brand_author='王 安 石',
    gold_rgb='184,144,90',
    root=""":root{
  --gold:#b8905a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(184,144,90,.3);
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
    tip='轻点画面 / 按空格 —— 江面展白绢，六朝残迹浮沉',
    hint='← → 键或空格逐境游览 · 末境可点击澄江似练：江面展白绢，六朝残迹浮沉',
    cover_read='桂枝香。宋，王安石。登临送目，正故国晚秋，天气初肃。千里澄江似练，翠峰如簇。',
    cover_p1='四重意境，随词句次第展开：登临送目，正故国晚秋，千里澄江如一匹白绢铺展天际，翠峰攒聚如箭；归帆点点没入残阳，酒旗斜矗，白鹭破空而起，画图难足；转入六朝旧梦——门外隋兵已至，楼头歌舞未歇，悲恨相续；最后六朝旧事随流水而去，寒烟衰草之外，商女的《后庭遗曲》犹自隐隐传来。',
    cover_p2='边读词，边走进王安石登高望远的冷眼：江山胜迹仍在，兴亡之叹未远——唯有看清历史的人，才照得见当下。',
    end_h2='兴亡 · 余音', cn_word='四',
    words_js="['再游一次，登高送目','初识半山，尚需共读','渐入词境，略有所感','怀古之情渐深','已解兴亡之叹','半山冷眼，千古兴亡']",
    sky_atmo='0x332414',
)

POEM_JS = io.open(os.path.join(_here, 'guizhixiang-jinling_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'guizhixiang-jinling_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'guizhixiang-jinling_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'guizhixiang-jinling_stages.js'), encoding='utf-8').read()
