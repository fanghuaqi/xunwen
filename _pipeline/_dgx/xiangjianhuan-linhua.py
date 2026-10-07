# -*- coding: utf-8 -*-
"""xiangjianhuan-linhua.py —— 《相见欢·林花谢了春红》（五代·李煜，no.158，青绿春晓·暮春风雨变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='xiangjianhuan-linhua', title='相见欢·林花谢了春红', dyn='五代 · 李煜', brand_author='李 煜',
    gold_rgb='201,143,159',
    root=""":root{
  --gold:#c98f9f; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(201,143,159,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0a1410', 2),
        ('rgba(5,8,15', 'rgba(6,12,9', 1),
        ('rgba(4,6,11', 'rgba(5,10,7', 2),
        ('rgba(6,9,16', 'rgba(6,11,8', 1),
        ('rgba(3,5,9', 'rgba(4,8,6', 1),
        ('#0b101c', '#0e1a14', 1),
        ('#6f664f', '#5f7264', 1),
        ('#5a5340', '#52604f', 1),
    ],
    tip='轻点画面 / 按空格 —— 风雨摧花，红瓣辞枝、东流水涨',
    hint='← → 键或空格逐境游览 · 末境可点击画面，风雨摧花、东流水涨',
    cover_read='相见欢·林花谢了春红。五代，李煜。林花谢了春红，太匆匆。无奈朝来寒雨晚来风。',
    cover_p1='两重意境，随词句次第展开：先入林花谢红的匆匆春暮，看朝雨晚风如何轮替摧花；再立东流水畔，听一声「人生长恨水长东」的千古浩叹。',
    cover_p2='边读词，边走进李煜笔下那个春红匆匆、长恨悠悠的暮春世界。',
    end_h2='流水落花', cn_word='两',
    words_js="['再游一次，且惜春红','初识后主，尚需共读','渐入佳境，再诵几遍','词心渐明，心随花落','深得后主词心','流水落花，长恨成诵']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'xiangjianhuan-linhua_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xiangjianhuan-linhua_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xiangjianhuan-linhua_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xiangjianhuan-linhua_stages.js'), encoding='utf-8').read()
