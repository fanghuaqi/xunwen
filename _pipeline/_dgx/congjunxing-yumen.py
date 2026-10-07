# -*- coding: utf-8 -*-
"""congjunxing-yumen.py —— 《从军行·其四》（唐·王昌龄，queue no.205，大漠金戈）生成配置
美术立意：大漠金戈赛道（底色 #120d08、雾 #1a120a 系、accent=#c4824a 取自 queue），边塞七绝压卷、苍茫悲壮。
四层色板递进：长云暗雪山（灰暗压抑）→ 孤城（沉赭剪影）→ 黄沙（境②转亮的暖赭）→ 金甲（accent 亮的誓言）；
前二句压抑暗色、后二句亮色誓言，风沙横流（makeFlow 赭色）贯穿两境。
标志性瞬间（境②·全诗气骨）：金甲之光在黄沙中明灭 + 大漠孤城——黄沙百战穿金甲、不破楼兰终不还。
末境点击（queue interact）：点击金甲——甲光千磨百战波次明灭 + 楼兰方向烽燧一线三台烽火次第明灭。
情感曲线：苍茫压抑 → 慷慨誓师。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='congjunxing-yumen', title='从军行·其四', dyn='唐 · 王昌龄', brand_author='王 昌 龄',
    gold_rgb='196,130,74',
    root=""":root{
  --gold:#c4824a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(196,130,74,.3);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(24,16,9', 1),
        ('rgba(4,6,11', 'rgba(12,8,5', 2),
        ('rgba(6,9,16', 'rgba(24,16,9', 1),
        ('rgba(3,5,9', 'rgba(8,5,3', 1),
        ('#0b101c', '#181009', 1),
        ('#6f664f', '#7a6a50', 1),
        ('#5a5340', '#6a5a44', 1),
    ],
    tip='轻点金甲 / 按空格 —— 甲光千磨百战，楼兰烽火明灭',
    hint='← → 键或空格逐境游览 · 末境可点击金甲：甲光千磨百战，楼兰烽火明灭',
    cover_read='从军行·其四。唐，王昌龄。青海长云暗雪山，孤城遥望玉门关。黄沙百战穿金甲，不破楼兰终不还。',
    cover_p1='两重意境，随诗句次第展开：青海长云横空、压暗万里雪山的苍茫，孤城遥望玉门关的孤悬压抑；黄沙百战磨穿金甲的艰苦卓绝，不破楼兰终不还的慷慨誓言。',
    cover_p2='边读诗，边走进王昌龄笔下的西域战场：前两句愈是压抑暗色，后两句金甲与誓言愈亮——读懂这条明暗递进线，就读懂了这首七绝压卷之作的气骨。',
    end_h2='楼兰未破 · 壮心不还', cn_word='两',
    words_js="['再游一次，重望玉门','初识龙标，尚需共读','渐入诗境，略有所感','边声渐壮，甲光渐亮','已解黄沙百战意','楼兰未破，壮心不还']",
    sky_atmo='0x332414',
)

POEM_JS = io.open(os.path.join(_here, 'congjunxing-yumen_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'congjunxing-yumen_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'congjunxing-yumen_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'congjunxing-yumen_stages.js'), encoding='utf-8').read()
