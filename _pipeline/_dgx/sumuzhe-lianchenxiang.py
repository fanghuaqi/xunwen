# -*- coding: utf-8 -*-
"""sumuzhe-lianchenxiang.py —— 《苏幕遮·燎沉香》（宋·周邦彦，no.185，青绿春晓·荷塘晓色变体）生成配置
词眼「水面清圆，一一风荷举」（王国维「真能得荷之神理」）：宿雨滚落、荷叶一一挺举 → 末境点击，
宿雨滚落+风荷次第挺举，轻舟梦入芙蓉浦。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='sumuzhe-lianchenxiang', title='苏幕遮·燎沉香', dyn='宋 · 周邦彦', brand_author='周邦彦',
    gold_rgb='149,201,192',
    root=""":root{
  --gold:#95c9c0; --ink:#eef4e6; --dim:#7fa39a; --paper:rgba(10,18,14,.60);
  --line:rgba(149,201,192,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0a1410', 2),
        ('rgba(5,8,15', 'rgba(6,11,9', 1),
        ('rgba(4,6,11', 'rgba(5,10,8', 2),
        ('rgba(6,9,16', 'rgba(6,12,10', 1),
        ('rgba(3,5,9', 'rgba(4,9,7', 1),
        ('#0b101c', '#0e1a16', 1),
        ('#6f664f', '#5f7268', 1),
        ('#5a5340', '#526057', 1),
    ],
    tip='轻点画面 / 按空格 —— 宿雨滚落，风荷次第挺举',
    hint='← → 键或空格逐境游览 · 末境可点击画面，宿雨滚落、风荷次第挺举，轻舟梦入芙蓉浦',
    cover_read='苏幕遮·燎沉香。宋，周邦彦。燎沉香，消溽暑。鸟雀呼晴，侵晓窥檐语。',
    cover_p1='四重意境，随词句次第展开：先入雨后初晴的清晨居室，焚一炉沉香消溽暑，听鸟雀檐下呼晴窥语；再到荷塘，看初阳干宿雨、水面清圆，风荷一一挺举——这正是「真能得荷之神理」的词眼；继而遥想故乡吴门，久客长安，问一声五月渔郎是否相忆；最后随一叶小楫轻舟，梦入芙蓉浦。',
    cover_p2='边读词，边走进周邦彦笔下那片雨后荷塘：清圆的叶、挺举的风荷，与藏在荷香深处的乡愁。',
    end_h2='轻舟入梦', cn_word='四',
    words_js="['再游一次，荷塘听雨','初识美成，尚需共读','渐入佳境，再诵几遍','词眼已明，风荷正举','深得清真词心','梦入芙蓉浦，乡愁化荷香']",
    sky_atmo='0x2a443c',
)

POEM_JS = io.open(os.path.join(_here, 'sumuzhe-lianchenxiang_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'sumuzhe-lianchenxiang_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'sumuzhe-lianchenxiang_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'sumuzhe-lianchenxiang_stages.js'), encoding='utf-8').read()
