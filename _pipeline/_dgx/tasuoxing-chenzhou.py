# -*- coding: utf-8 -*-
"""tasuoxing-chenzhou.py —— 《踏莎行·郴州旅舍》（宋·秦观，no.183，烟雨江南）生成配置
美术立意：淮海词最凄苦之作，浓雾是本页主角。黛蓝湿雾 #151d26 主调、accent #8f9fc0（queue 分配）、
藕荷 #d8a7b1 仅作梅萼/桃色一点；月隐为常，唯「月迷津渡」境悬一团被雾裹住的低垂淡月。
标志性瞬间「楼台显而复失」：远景楼台自浓雾里浮出轮廓、又溶回雾中——开篇八字（雾失楼台、月迷津渡）
是全词意境总纲，一切景物都被雾月迷蒙失去轮廓。
末境点击郴江：三道江流绕郴山加速增亮（流向叩问），杜鹃三啼，题字「为谁流下潇湘去？」。
情感曲线：雾迷 → 孤寒 → 恨砌 → 江问，逐境加深（N=2，queue stages 唯一口径）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='tasuoxing-chenzhou', title='踏莎行·郴州旅舍', dyn='宋 · 秦观', brand_author='秦 观',
    gold_rgb='143,159,192',
    root=""":root{
  --gold:#8f9fc0; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(143,159,192,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#131a24', 1),
        ('#6f664f', '#5f6a7a', 1),
        ('#5a5340', '#525c6c', 1),
    ],
    tip='轻点画面 / 按空格 —— 江水绕山叩问潇湘，杜鹃啼远',
    hint='← → 键或空格逐境游览 · 末境可点击郴江：江流绕山而下，杜鹃声起',
    cover_read='踏莎行。宋，秦观。雾失楼台，月迷津渡，桃源望断无寻处。可堪孤馆闭春寒，杜鹃声里斜阳暮。',
    cover_p1='两重意境，随词句次第展开：雾失楼台、月迷津渡的凄迷远景与孤馆春寒、杜鹃斜阳的暮色旅愁；驿寄梅花、鱼传尺素反砌起的层层离恨，与郴江绕山、竟自流下潇湘的一声天问。',
    cover_p2='边读词，边走进秦观笔下这座被浓雾深锁的郴州旅舍——「雾失楼台，月迷津渡」，淮海词最凄苦的绝唱。',
    end_h2='为谁流下潇湘去', cn_word='二',
    words_js="['再入雾中，寻一回楼台','初识少游，尚需共读','渐入词境，略有所感','孤寒渐深，恨意如砌','深得淮海词心','郴江有问，与君同听']",
    sky_atmo='0x35455c',
)

POEM_JS = io.open(os.path.join(_here, 'tasuoxing-chenzhou_poem.js'), encoding='utf-8').read()
QUIZ_JS = io.open(os.path.join(_here, 'tasuoxing-chenzhou_quiz.js'), encoding='utf-8').read()
SCENES_JS = io.open(os.path.join(_here, 'tasuoxing-chenzhou_scenes.js'), encoding='utf-8').read()
STAGES_JS = io.open(os.path.join(_here, 'tasuoxing-chenzhou_stages.js'), encoding='utf-8').read()
