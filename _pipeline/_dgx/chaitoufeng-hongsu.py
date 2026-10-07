# -*- coding: utf-8 -*-
"""chaitoufeng-hongsu.py —— 《钗头凤·红酥手》（宋·陆游，queue no.195，烟雨江南）生成配置
美术立意：沈园本事词。全页禁金，黛蓝湿雾 #8fb3c9 系主调、accent=#a8a0c0（淡藤紫，取自 queue）
用于题字辉光/人物边缘光/进度点；桃花红是全页唯一暖点。
上下片对称回环：红酥手/春如旧、宫墙柳/人空瘦——境①与境③同景异时（园宴对饮→池畔空瘦一人）。
标志性瞬间「宫墙柳」：满城春色而人隔宫墙——近在咫尺的咫尺天涯。
末境点击（queue interact）：点击宫墙柳——柳絮拂壁，「错、错、错」「莫、莫、莫」题字次第浮现（双调回环）。
情感曲线：园宴重逢 → 题壁三错 → 人空瘦 → 锦书难托三莫（题壁回环收束）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='chaitoufeng-hongsu', title='钗头凤', dyn='宋 · 陆游', brand_author='陆 游',
    gold_rgb='168,160,192',
    root=""":root{
  --gold:#a8a0c0; --ink:#e6ecef; --dim:#7e8aa0; --paper:rgba(13,16,24,.60);
  --line:rgba(168,160,192,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#141824', 1),
        ('#6f664f', '#686a80', 1),
        ('#5a5340', '#5e5c72', 1),
    ],
    tip='轻点画面 / 按空格 —— 柳絮拂壁，「错」「莫」题字次第浮现',
    hint='← → 键或空格逐境游览 · 末境可点击宫墙柳：柳絮拂壁，「错」「莫」题字次第浮现',
    cover_read='钗头凤。宋，陆游。红酥手，黄縢酒，满城春色宫墙柳。东风恶，欢情薄。',
    cover_p1='四重意境，随词句次第展开：沈园春宴，红酥手斟满黄縢酒，满城春色里人隔宫墙；东风恶，欢情薄，一怀愁绪几年离索，「错、错、错」题上园壁；再游沈园，春如旧而人空瘦，泪湿鲛绡，桃花吹落闲池阁；山盟虽在，锦书难托，「莫、莫、莫」一声长叹。',
    cover_p2='边读词，边走进陆游笔下这场沈园重逢——题壁而别，半个世纪的伤悼自此而起；「错错错」与「莫莫莫」上下片回环相扣。',
    end_h2='沈园 · 题壁', cn_word='四',
    words_js="['再入沈园','初识放翁，尚需共读','渐入词境，略有所感','愁绪渐深，离索在望','已解错莫之痛','一咏三叹，钗凤有声']",
    sky_atmo='0x36445a',
)

POEM_JS = io.open(os.path.join(_here, 'chaitoufeng-hongsu_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'chaitoufeng-hongsu_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'chaitoufeng-hongsu_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'chaitoufeng-hongsu_stages.js'), encoding='utf-8').read()
