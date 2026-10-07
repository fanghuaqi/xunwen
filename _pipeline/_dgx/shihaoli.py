# -*- coding: utf-8 -*-
"""shihaoli.py —— 《石壕吏》（唐·杜甫，no.145，水墨夜思·乱世变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=5, slug='shihaoli', title='石壕吏', dyn='唐 · 杜甫', brand_author='杜 甫',
    gold_rgb='122,138,153',
    root=""":root{
  --gold:#7a8a99; --ink:#dfe3ea; --dim:#7c8290; --paper:rgba(10,11,16,.60);
  --line:rgba(122,138,153,.28);
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
    tip='轻点画面 / 按空格 —— 夜去天明，独别老翁',
    hint='← → 键或空格逐境游览 · 末境可点击画面，天明独别',
    cover_read='石壕吏。唐，杜甫。暮投石壕村，有吏夜捉人。老翁逾墙走，老妇出门看。',
    cover_p1='五重意境，随诗句次第展开：暮投石壕、有吏夜捉的乱世；吏呼一何怒、妇啼一何苦的对撞；三男邺城戍、二男新战死的泣诉；老妪自请夜归的无奈；夜久语声绝、独与老翁别的余痛。',
    cover_p2='边读诗，边走进杜甫「三吏三别」中这个不眠的石壕之夜。',
    end_h2='幽咽独别', cn_word='五',
    words_js="['再读一次，乱世之夜','初识杜工部，尚需共读','渐入村舍，略有所感','苦难渐识，怒苦对闻','深得诗史之笔','独与老翁别']",
    sky_atmo='0x3a3440',
)

POEM_JS = io.open(os.path.join(_here, 'shihaoli_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'shihaoli_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'shihaoli_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'shihaoli_stages.js'), encoding='utf-8').read()
