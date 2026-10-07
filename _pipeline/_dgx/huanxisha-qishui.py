# -*- coding: utf-8 -*-
"""huanxisha-qishui.py —— 《浣溪沙·游蕲水清泉寺》（宋·苏轼，no.177，青绿春晓·蕲水溪山变体）生成配置
词眼「门前流水尚能西」：众水东流此溪独西 → 末境点击，溪水反向西去、白发意象消散。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='huanxisha-qishui', title='浣溪沙·游蕲水清泉寺', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='143,196,168',
    root=""":root{
  --gold:#8fc4a8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(143,196,168,.30);
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
    tip='轻点画面 / 按空格 —— 溪水反向西去，白发消散',
    hint='← → 键或空格逐境游览 · 末境可点击画面，溪水反向西去、白发消散',
    cover_read='浣溪沙·游蕲水清泉寺。宋，苏轼。山下兰芽短浸溪，松间沙路净无泥，潇潇暮雨子规啼。',
    cover_p1='两重意境，随词句次第展开：先入蕲水清泉寺畔，看山下兰芽浸溪、松间沙路净无泥，潇潇暮雨里子规声声，一句「谁道人生无再少」迎面发问；再到寺门前，看门前流水偏能向西——休将白发唱黄鸡！',
    cover_p2='边读词，边走进东坡贬居黄州时那副身处逆境而旷达依旧的胸怀。',
    end_h2='溪水西流', cn_word='两',
    words_js="['再游一次，溪畔听雨','初识东坡，尚需共读','渐入佳境，再诵几遍','词眼已明，溪水向西','深得东坡旷达','黄州风雨，一溪春水向西流']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'huanxisha-qishui_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'huanxisha-qishui_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'huanxisha-qishui_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'huanxisha-qishui_stages.js'), encoding='utf-8').read()
