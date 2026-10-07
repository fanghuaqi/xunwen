# -*- coding: utf-8 -*-
"""yulinling.py —— 《雨霖铃·寒蝉凄切》（宋·柳永，no.169，烟雨江南）生成配置
美术立意：柳永压卷、宋词离别第一篇。全页禁金，黛蓝湿雾 #8fb3c9 主调、藕荷 #d8a7b1 点缀；
月隐为常，唯设想之景（境③/末境点击后）悬一弯残月。
标志性瞬间「长亭执手」：雨后长亭前的执手二人剪影；末境点击兰舟——舟发烟波，残月悬上杨柳岸。
情感曲线：雨歇催发 → 执手凝噎 → 设想孤旅 → 风情谁说；雾随境渐阔渐沉。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yulinling', title='雨霖铃', dyn='宋 · 柳永', brand_author='柳 永',
    gold_rgb='143,179,201',
    root=""":root{
  --gold:#8fb3c9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(143,179,201,.28);
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
    tip='轻点画面 / 按空格 —— 兰舟发入烟波，残月悬上杨柳岸',
    hint='← → 键或空格逐境游览 · 末境可点击兰舟：舟发烟波，残月悬上杨柳岸',
    cover_read='雨霖铃。宋，柳永。寒蝉凄切，对长亭晚，骤雨初歇。都门帐饮无绪，留恋处，兰舟催发。执手相看泪眼，竟无语凝噎。',
    cover_p1='四重意境，随词句次第展开：寒蝉凄切、骤雨初歇后的长亭执手与无声凝噎；念去去千里烟波、暮霭沉沉楚天阔的浩渺离愁；今宵酒醒何处、杨柳岸晓风残月的凄清设想；此去经年，纵有千种风情、更与何人说的无尽余恨。',
    cover_p2='边读词，边走进柳永笔下这场千古离别——「多情自古伤离别」，宋词离别的压卷之作。',
    end_h2='更与何人说', cn_word='四',
    words_js="['再读一次，执手长亭','初识柳永，尚需共读','渐入词境，略有所感','离愁渐深，烟波在望','深得屯田词心','千种风情，与君共说']",
    sky_atmo='0x36445a',
)

POEM_JS = io.open(os.path.join(_here, 'yulinling_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'yulinling_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'yulinling_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'yulinling_stages.js'), encoding='utf-8').read()
