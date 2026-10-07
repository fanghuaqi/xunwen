# -*- coding: utf-8 -*-
"""suzhongqing-wanli.py —— 《诉衷情·当年万里觅封侯》（宋·陆游，queue no.196，大漠金戈）生成配置
美术立意：大漠金戈赛道（底色 #120d08、雾 #1a120a 系、accent=#b0906a 取自 queue），放翁暮年壮志、苍茫悲壮。
全页情绪轴：梦里大漠金戈的暖亮（境①全页最暖最亮：年少戎装、匹马军阵、战旗烽燧）
对比 现实沧洲渔屋的冷灰（境②转冷、境③冷灰水乡）——读懂两重画面的温差，就读懂了这首词。
标志性瞬间（全词结穴）：境③「心在天山，身老沧洲」——天山雪岭幻象与沧洲茅屋现实同框对切，
理想与现实的地理撕裂一帧看尽。
末境点击（queue interact）：点击貂裘——尘光自裘上浮起 + 天山侧年少戎装的「对影」显形，与沧洲老人隔水相望。
情感曲线：梦暖金戈 → 尘暗泪空 → 心身两地撕裂。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='suzhongqing-wanli', title='诉衷情·当年万里觅封侯', dyn='宋 · 陆游', brand_author='陆 游',
    gold_rgb='176,144,106',
    root=""":root{
  --gold:#b0906a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(176,144,106,.3);
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
    tip='轻点貂裘 / 按空格 —— 尘光浮起，天山沧洲两地对影',
    hint='← → 键或空格逐境游览 · 末境可点击貂裘：尘光浮起，天山沧洲两地对影',
    cover_read='诉衷情。宋，陆游。当年万里觅封侯，匹马戍梁州。关河梦断何处？尘暗旧貂裘。胡未灭，鬓先秋，泪空流。此生谁料？心在天山，身老沧洲。',
    cover_p1='三重意境，随词句次第展开：当年万里觅封侯、匹马戍梁州的梦中壮游；胡未灭、鬓先秋，尘暗旧貂裘的霜鬓泪眼；此生谁料——心在天山、身老沧洲，理想与现实的地理撕裂。',
    cover_p2='边读词，边走进放翁的暮年一梦：梦里大漠金戈越暖亮，醒后沧洲渔屋越冷清——读懂这两重画面的温差，就读懂了这首词。',
    end_h2='心在天山 · 身老沧洲', cn_word='三',
    words_js="['再游一次，重梦梁州','初识放翁，尚需共读','渐入词境，略有所感','壮志暮年，感同身受','深得放翁词心','天山沧洲，一梦成诵']",
    sky_atmo='0x3a2a18',
)

POEM_JS = io.open(os.path.join(_here, 'suzhongqing-wanli_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'suzhongqing-wanli_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'suzhongqing-wanli_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'suzhongqing-wanli_stages.js'), encoding='utf-8').read()
