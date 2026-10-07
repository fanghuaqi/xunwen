# -*- coding: utf-8 -*-
"""zhegutian-caixiu.py —— 《鹧鸪天·彩袖殷勤捧玉钟》（宋·晏几道，no.173，夜宴金彩·小山词冠篇）生成配置
二境（queue.json 分境口径）：舞低楼月（当年盛欢：彩袖捧钟+拼却一醉+舞低楼心月·歌尽扇底风，
标志性瞬间=楼心月随彻夜歌舞徐徐西沉）、银釭疑梦（末境可点击：从别后魂梦相逢→今宵银釭照，
点击挑亮银釭、灯下相认、恍然如梦——犹恐相逢是梦中）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

def io_open(name):
    return io.open(os.path.join(_here, name), encoding='utf-8').read()

META = dict(
    N=2, slug='zhegutian-caixiu', title='鹧鸪天·彩袖殷勤捧玉钟', dyn='宋 · 晏几道', brand_author='晏几道',
    gold_rgb='224,192,96',
    root=""":root{
  --gold:#e0c060; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(224,192,96,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,7', 1),
        ('rgba(4,6,11', 'rgba(6,5,7', 2),
        ('rgba(6,9,16', 'rgba(8,6,8', 1),
        ('rgba(3,5,9', 'rgba(6,5,7', 1),
        ('#0b101c', '#14100a', 1),
        ('#6f664f', '#6b5c46', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点画面 / 按空格 —— 挑亮银釭，灯下相认，恍然如梦',
    hint='← → 键或空格逐境游览 · 末境可点击画面，挑亮银釭、灯下相认',
    cover_read='鹧鸪天。宋，晏几道。彩袖殷勤捧玉钟，当年拼却醉颜红。舞低杨柳楼心月，歌尽桃花扇底风。从别后，忆相逢，几回魂梦与君同。今宵剩把银釭照，犹恐相逢是梦中。',
    cover_p1='二重意境，随词句次第展开：当年歌筵，彩袖歌女殷勤捧钟劝酒、少年拼却一醉，舞低楼心月、歌尽扇底风的彻夜盛欢；从别后魂梦里几度相逢，到今宵银釭高照、真相逢反疑在梦中的悲喜交并。',
    cover_p2='边读词，边走进晏几道笔下那座歌舞彻夜的高楼与那盏照见重逢的银灯，体会「小山词」压卷之作里盛欢与疑梦的翻覆深情。',
    end_h2='银釭 · 照梦', cn_word='二',
    words_js="['再读一次，彩袖玉钟','初识小山，尚需共读','渐入佳境，再诵几遍','梦魂相逢渐明，已得词境','深解「盛欢」与「疑梦」','银釭照处，犹恐相逢在梦中']",
    sky_atmo='0x4a3018',
)

POEM_JS = io_open('zhegutian-caixiu_poem.js')
QUIZ_JS = io_open('zhegutian-caixiu_quiz.js')
SCENES_JS = io_open('zhegutian-caixiu_scenes.js')
STAGES_JS = io_open('zhegutian-caixiu_stages.js')
