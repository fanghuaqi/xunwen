# -*- coding: utf-8 -*-
"""yujiaaotianjie.py —— 《渔家傲·天接云涛连晓雾》（宋·李清照，no.153，水墨夜思·星海神游变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yujiaao-tianjie', title='渔家傲·天接云涛连晓雾', dyn='宋 · 李清照', brand_author='李 清 照',
    gold_rgb='154,168,201',
    root=""":root{
  --gold:#9aa8c9; --ink:#dfe6f0; --dim:#7e8ea0; --paper:rgba(9,13,22,.58);
  --line:rgba(154,168,201,.28);
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
    tip='轻点画面 / 按空格 —— 九万里风鹏正举，蓬舟吹取三山',
    hint='← → 键或空格逐境游览 · 末境可点击画面，风鹏高举',
    cover_read='渔家傲天接云涛连晓雾。宋，李清照。天接云涛连晓雾，星河欲转千帆舞。',
    cover_p1='四重意境，随词句次第展开：天接云涛、星河欲转千帆舞的壮阔梦境；梦魂归帝所、亲闻天语的奇遇；路长嗟日暮、学诗谩有惊人句的深沉悲慨；九万里风鹏正举，风休住，蓬舟吹取三山去的浪漫高飞。',
    cover_p2='边读词，边走进易安居士笔下那雄奇浪漫、神游八极的豪放绝唱。',
    end_h2='风鹏三山', cn_word='四',
    words_js="['再读一次，星河千帆','初识易安，尚需共读','渐入云涛，神游八极','豪兴渐起，风鹏正举','深得易安雄奇浪漫之概','九万里风鹏正举，蓬舟吹取三山去']",
    sky_atmo='0x223650',
)

POEM_JS = io.open(os.path.join(_here, 'yujiaaotianjie_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yujiaaotianjie_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yujiaaotianjie_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yujiaaotianjie_stages.js'), encoding='utf-8').read()
