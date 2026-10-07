# -*- coding: utf-8 -*-
"""langtaosha-lianyu.py —— 《浪淘沙令·帘外雨潺潺》（五代·李煜，no.159，烟雨江南）生成配置
美术立意：梦里暖、醒后寒——梦境境用全页唯一的低饱和烛橙微暖，醒来各境转冷蓝黛雾；
末境「天上人间」为标志性瞬间（一水之隔的天上/人间两界，点击凭栏点亮）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='langtaosha-lianyu', title='浪淘沙令·帘外雨潺潺', dyn='五代 · 李煜', brand_author='李 煜',
    gold_rgb='144,168,192',
    root=""":root{
  --gold:#90a8c0; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(144,168,192,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#131a24', 1),
        ('#6f664f', '#5f6a7a', 1),
        ('#5a5340', '#525c6c', 1),
    ],
    tip='轻点凭栏 / 按空格 —— 栏杆伸向无限江山',
    hint='← → 键或空格逐境游览 · 末境可点击凭栏，栏杆伸向无限江山雾影',
    cover_read='浪淘沙令·帘外雨潺潺。五代，李煜。帘外雨潺潺，春意阑珊。罗衾不耐五更寒。',
    cover_p1='三重意境，随词句次第展开：帘外雨潺潺、罗衾难耐五更寒的孤冷长夜；梦里不知身是客、一晌贪欢的微暖幻境；独自莫凭栏，流水落花春去也——一水之隔的天上人间。',
    cover_p2='边读词，边走进李煜绝笔中那场梦与醒的诀别——梦里越暖，醒后越寒。',
    end_h2='天上人间', cn_word='三',
    words_js="['再读一次，梦回金陵','初识后主，尚需共读','渐入词境，略有所感','哀婉渐深，梦醒自知','深得后主词心','天上人间，一晌成诵']",
    sky_atmo='0x36445a',
)

POEM_JS = io.open(os.path.join(_here, 'langtaosha-lianyu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'langtaosha-lianyu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'langtaosha-lianyu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'langtaosha-lianyu_stages.js'), encoding='utf-8').read()
