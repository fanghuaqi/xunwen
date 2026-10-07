# -*- coding: utf-8 -*-
"""xinglunan.py —— 《行路难·其一》（唐·李白，no.134，夜宴金彩·行路变体）生成配置"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='xinglu-nan', title='行路难·其一', dyn='唐 · 李白', brand_author='李 白',
    gold_rgb='217,176,80',
    residual=('将进酒', '万古愁'),   # 本诗作者即李白（quiz/评语中"太白"合法），仅拦《将进酒》残留
    root=""":root{
  --gold:#d9b050; --ink:#e8dcc0; --dim:#9a8d72; --paper:rgba(12,10,7,.60);
  --line:rgba(217,176,80,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(8,6,4', 1),
        ('rgba(4,6,11', 'rgba(6,5,3', 2),
        ('rgba(6,9,16', 'rgba(7,6,4', 1),
        ('rgba(3,5,9', 'rgba(5,4,3', 1),
        ('#0b101c', '#141009', 1),
        ('#6f664f', '#6b6250', 1),
        ('#5a5340', '#5f5745', 1),
    ],
    tip='轻点画面 / 按空格 —— 云帆满张，长风破浪',
    hint='← → 键或空格逐境游览 · 末境可点击画面，云帆满张破浪',
    cover_read='行路难。唐，李白。金樽清酒斗十千，玉盘珍羞直万钱。停杯投箸不能食，拔剑四顾心茫然。',
    cover_p1='四重意境，随诗句次第展开：盛宴在前却停杯投箸、拔剑四顾的茫然；欲渡黄河冰塞川、将登太行雪满山的阻隔；溪钓梦日的两个典故与期待；终见长风破浪、直挂云帆济沧海的豪兴反转。',
    cover_p2='边读诗，边走进李白那从茫然到自信、最终喊出"长风破浪会有时"的世界。',
    end_h2='云帆沧海', cn_word='四',
    words_js="['再游一次，且听长风','初识太白，尚需共读','渐入佳境，再诵几遍','豪兴渐生，再进一杯','深得青莲乐观之志','长风破浪，云帆沧海']",
    sky_atmo='0x3d3220',
)

POEM_JS = io.open(os.path.join(_here, 'xinglunan_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'xinglunan_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'xinglunan_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'xinglunan_stages.js'), encoding='utf-8').read()
