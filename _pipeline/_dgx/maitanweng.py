# -*- coding: utf-8 -*-
"""maitanweng.py —— 《卖炭翁》（唐·白居易，no.144，宣纸留白·苦寒变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=5, slug='maitanweng', title='卖炭翁', dyn='唐 · 白居易', brand_author='白 居 易',
    gold_rgb='90,74,58',
    root=""":root{
  --gold:#5a4a3a; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(90,74,58,.32);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(240,236,224', 1),
        ('rgba(4,6,11', 'rgba(238,233,220', 2),
        ('rgba(6,9,16', 'rgba(239,234,222', 1),
        ('rgba(3,5,9', 'rgba(236,231,218', 1),
        ('#0b101c', '#f2eee0', 1),
        ('#6f664f', '#6e695a', 1),
        ('#5a5340', '#655f4e', 1),
    ],
    tip='轻点画面 / 按空格 —— 半匹红纱系向牛头',
    hint='← → 键或空格逐境游览 · 末境可点击画面，红纱系向牛头',
    cover_read='卖炭翁。唐，白居易。卖炭翁，伐薪烧炭南山中。满面尘灰烟火色，两鬓苍苍十指黑。',
    cover_p1='五重意境，随诗句次第展开：南山伐薪烧炭的满面尘灰；衣正单却愿天寒的辛酸矛盾；晓驾炭车辗冰辙的一尺雪；宫使手把文书口称敕的强夺；半匹红纱系向牛头——全篇唯一的重色。',
    cover_p2='边读诗，边看清白居易笔下那个「宫市」掠夺下的卖炭老人。',
    end_h2='炭贱宫使', cn_word='五',
    words_js="['再读一次，雪辙炭车','初识乐天，尚需共读','渐入苦寒，略有所感','辛酸渐识，衣单愿寒','深得讽喻诗之力','半匹红纱，千斤炭直']",
    sky_atmo='0xb8b2a0',
)

POEM_JS = io.open(os.path.join(_here, 'maitanweng_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'maitanweng_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'maitanweng_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'maitanweng_stages.js'), encoding='utf-8').read()
