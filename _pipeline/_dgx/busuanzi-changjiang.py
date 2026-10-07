# -*- coding: utf-8 -*-
"""busuanzi-changjiang.py —— 《卜算子·我住长江头》（宋·李之仪，no.180，青绿春晓·大江春晓变体）生成配置
词眼「共饮长江水」：长江头尾两端、共饮一江水——地理的两端被一条江连成一线。
末境点击，镜头沿江千里贯通，江头江尾两点渐亮、一江灯连成一线（定不负相思意）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='busuanzi-changjiang', title='卜算子·我住长江头', dyn='宋 · 李之仪', brand_author='李之仪',
    gold_rgb='149,201,176',
    root=""":root{
  --gold:#95c9b0; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(149,201,176,.30);
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
    tip='轻点画面 / 按空格 —— 镜头沿江千里，贯通江头江尾',
    hint='← → 键或空格逐境游览 · 末境可点击画面，镜头沿长江千里贯通江头江尾',
    cover_read='卜算子·我住长江头。宋，李之仪。我住长江头，君住长江尾，日日思君不见君，共饮长江水。',
    cover_p1='三重意境，随词句次第展开：先立长江之头，望长江之尾那人不得见，日日思君，共饮一江春水；再听「此水几时休？此恨何时已」的绵绵一问；末境轻点江水，看镜头沿江千里贯通，江头江尾两点渐亮——只愿君心似我心，定不负相思意。',
    cover_p2='边读词，边走进李之仪笔下这条把相思连成一线的大江。',
    end_h2='千里同心', cn_word='三',
    words_js="['再游一次，江畔听水','初识端叔，尚需共读','渐入佳境，再诵几遍','相思渐明，共饮一江','深得词心坚贞','江头江尾，千里同心']",
    sky_atmo='0x2c4434',
)

POEM_JS = io.open(os.path.join(_here, 'busuanzi-changjiang_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'busuanzi-changjiang_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'busuanzi-changjiang_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'busuanzi-changjiang_stages.js'), encoding='utf-8').read()
