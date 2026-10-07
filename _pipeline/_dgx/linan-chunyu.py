# -*- coding: utf-8 -*-
"""linan-chunyu.py —— 《临安春雨初霁》（宋·陆游，no.241，烟雨江南·临安客舍变体）生成配置
诗眼「小楼一夜听春雨，深巷明朝卖杏花」：小楼夜雨、深巷杏花、矮纸分茶、素衣归心。
末境点击卖杏花 → 夜雨渐停（雨丝 uStop 收）、花担由巷中推到巷口、四声叫卖音阶、题字「深巷卖杏花」。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='linan-chunyu', title='临安春雨初霁', dyn='宋 · 陆游', brand_author='陆 游',
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
    tip='轻点卖杏花 / 按空格 —— 夜雨渐停，深巷花担出巷',
    hint='← → 键或空格逐境游览 · 末境可点击卖杏花：雨住、花担出巷、叫卖声起',
    cover_read='临安春雨初霁。宋，陆游。世味年来薄似纱，谁令骑马客京华。小楼一夜听春雨，深巷明朝卖杏花。',
    cover_p1='四重意境，随诗句次第展开：世态人情薄得像纱，骑马客居京华的无奈；小楼一夜听雨，深巷明朝卖花的清响；矮纸斜行闲作草、晴窗细乳戏分茶的闲；素衣莫叹风尘，清明便可到家的归心。',
    cover_p2='边读诗，边走进临安春雨里的那座小楼：一夜无眠是客愁，一声叫卖是春天。',
    end_h2='深巷 · 杏花', cn_word='四',
    words_js="['再听一夜，雨打小楼','初识放翁，尚需共读','渐入佳境，再诵几遍','雨声渐住，叫卖渐近','已识闲中落寞','小楼听雨，深巷杏花']",
    sky_atmo='0x344052',
)

POEM_JS = io.open(os.path.join(_here, 'linan-chunyu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'linan-chunyu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'linan-chunyu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'linan-chunyu_stages.js'), encoding='utf-8').read()
