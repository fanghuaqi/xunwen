# -*- coding: utf-8 -*-
"""man.py —— 《满江红》（宋·岳飞，no.124，大漠金戈·赤焰变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='manjianghong', title='满江红', dyn='宋 · 岳飞', brand_author='岳 飞',
    gold_rgb='192,80,58',
    root=""":root{
  --gold:#c0503a; --ink:#f0e2cc; --dim:#a08a6e; --paper:rgba(16,11,7,.60);
  --line:rgba(192,80,58,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(9,6,4', 1),
        ('rgba(4,6,11', 'rgba(8,5,3', 2),
        ('rgba(6,9,16', 'rgba(9,6,4', 1),
        ('rgba(3,5,9', 'rgba(7,4,3', 1),
        ('#0b101c', '#1a120c', 1),
        ('#6f664f', '#6e5d48', 1),
        ('#5a5340', '#61523e', 1),
    ],
    tip='轻点画面 / 按空格 —— 天光裂云，山缺旌旗',
    hint='← → 键或空格逐境游览 · 末境可点击画面，天光裂云、山缺旌旗',
    cover_read='满江红。宋，岳飞。怒发冲冠，凭栏处、潇潇雨歇。',
    cover_p1='四重意境，随词句次第展开：雨歇凭栏、仰天长啸；八千里路、尘土云月；靖康未雪、破垣烽烟；长车踏破贺兰山缺，收拾旧山河，朝天阙。',
    cover_p2='边读词，边走进岳飞那壮怀激烈、忠愤填膺的将帅世界。',
    end_h2='壮怀激烈', cn_word='四',
    words_js="['再诵一次，雨歇凭栏','初识武穆，尚需共读','渐入佳境，再诵几遍','壮怀渐生，长啸一声','深得武穆之志','收拾山河，朝天阙']",
    sky_atmo='0x4a3820',
)

POEM_JS = io.open(os.path.join(_here, 'man_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'man_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'man_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'man_stages.js'), encoding='utf-8').read()
