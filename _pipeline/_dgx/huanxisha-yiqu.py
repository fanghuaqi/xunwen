# -*- coding: utf-8 -*-
"""huanxisha-yiqu.py —— 《浣溪沙·一曲新词酒一杯》（宋·晏殊，no.164，夜宴金彩·闲雅暮宴变体）生成配置
二境（queue.json 分境口径）：新曲旧亭（一曲新词酒一杯+去年天气旧亭台+夕阳西下几时回·落日渐沉）、
花落燕归（标志性瞬间·末境可点击：燕归来对花落去，点击燕子掠过香径+落花飘零+香径独徘徊）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

def io_open(name):
    return io.open(os.path.join(_here, name), encoding='utf-8').read()

META = dict(
    N=2, slug='huanxisha-yiqu', title='浣溪沙·一曲新词酒一杯', dyn='宋 · 晏殊', brand_author='晏殊',
    gold_rgb='224,176,96',
    root=""":root{
  --gold:#e0b060; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(224,176,96,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(10,7,4', 1),
        ('rgba(4,6,11', 'rgba(8,6,4', 2),
        ('rgba(6,9,16', 'rgba(10,7,4', 1),
        ('rgba(3,5,9', 'rgba(8,5,4', 1),
        ('#0b101c', '#161008', 1),
        ('#6f664f', '#6b5c46', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点画面 / 按空格 —— 燕子掠过香径，落花飘零',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看归燕掠过香径、落花飘零',
    cover_read='浣溪沙。宋，晏殊。一曲新词酒一杯，去年天气旧亭台。夕阳西下几时回？无可奈何花落去，似曾相识燕归来。小园香径独徘徊。',
    cover_p1='二重意境，随词句次第展开：一曲新词、一杯淡酒，去年天气、旧时亭台，与夕阳西下几时回的闲雅怅问；无可奈何花落去、似曾相识燕归来，与小园香径独徘徊的惜时幽思。',
    cover_p2='边读词，边走进晏殊笔下那座暮色里的池畔亭台与小园香径，体会「太平宰相」淡语深处的时感之谜。',
    end_h2='香径 · 徘徊', cn_word='二',
    words_js="['再读一次，一曲新词酒一杯','初识同叔，尚需共读','渐入佳境，再诵几遍','对句渐明，已得词境','深解「去」「来」之理趣','燕归花落，香径徘徊思无尽']",
    sky_atmo='0x40281a',
)

POEM_JS = io_open('huanxisha-yiqu_poem.js')
QUIZ_JS = io_open('huanxisha-yiqu_quiz.js')
SCENES_JS = io_open('huanxisha-yiqu_scenes.js')
STAGES_JS = io_open('huanxisha-yiqu_stages.js')
