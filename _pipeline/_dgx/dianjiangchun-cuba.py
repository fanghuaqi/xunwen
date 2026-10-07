# -*- coding: utf-8 -*-
"""dianjiangchun-cuba.py —— 《点绛唇·蹴罢秋千》（宋·李清照，no.190，青绿春晓·易安春园变体）生成配置
词眼「和羞走，倚门回首，却把青梅嗅」：宋词里最灵动的少女瞬间 → 末境点击，
三段小动作（跑→回首→嗅梅）依次展开，秋千余荡重启，梅香微光浮起。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='dianjiangchun-cuba', title='点绛唇·蹴罢秋千', dyn='宋 · 李清照', brand_author='李清照',
    gold_rgb='176,207,159',
    root=""":root{
  --gold:#b0cf9f; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(176,207,159,.30);
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
    tip='轻点画面 / 按空格 —— 和羞走 · 倚门回首 · 却把青梅嗅',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看少女回首嗅梅、秋千余荡',
    cover_read='点绛唇·蹴罢秋千。宋，李清照。蹴罢秋千，起来慵整纤纤手。露浓花瘦，薄汗轻衣透。',
    cover_p1='两重意境，随词句次第展开：先入春日后园，少女蹴罢秋千、慵整纤纤手，露浓花瘦、薄汗轻衣透；再逢客人入来——和羞走，倚门回首，却把青梅嗅，那一借梅香掩住的回望，是宋词里最灵动的少女瞬间。',
    cover_p2='边读词，边走进易安居士笔下那个天真娇憨、羞中带俏的豆蔻年华。',
    end_h2='青梅犹香', cn_word='两',
    words_js="['再游一次，园中秋千','初识易安，尚需共读','渐入佳境，再诵几遍','娇羞渐明，回首一望','深得易安笔意','春园寂寂，青梅犹香']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'dianjiangchun-cuba_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'dianjiangchun-cuba_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'dianjiangchun-cuba_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'dianjiangchun-cuba_stages.js'), encoding='utf-8').read()
