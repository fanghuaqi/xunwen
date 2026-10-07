# -*- coding: utf-8 -*-
"""_mk.py —— 由 _head/_prims/_builders/_stages/_tail 拼装 shudaonan/index.html
   引擎部分（着色器/天空/通用构件/造型工坊/淡入淡出/声音/朗读）从 nian-nujiao-chibi 骨架原样继承，
   数据、场景构件与各境 builder、境定义、UI/主循环/启动 全部换成本诗自己的。"""
import io, os, re

BASE = '../nian-nujiao-chibi/index.html'
base = io.open(BASE, encoding='utf-8').read()
rd = lambda p: io.open(p, encoding='utf-8').read()


def cut(s, a, b):
    i = s.index(a)
    j = s.index(b, i)
    return s[i:j]


MARK = {
    'tools': '/* ---------------- 工具 ---------------- */',
    'data': '/* ---------------- 诗词数据 ---------------- */',
    'engine': '/* ---------------- 着色器 ---------------- */',
    'scene': '/* ---------------- 场景构件（大漠金戈 · 江山怀古变体） ---------------- */',
    'fade': '/* ---------------- 淡入淡出 ---------------- */',
    'ui': '/* ---------------- UI ---------------- */',
}

tools = cut(base, MARK['tools'], MARK['data'])
engine = cut(base, MARK['engine'], MARK['scene'])
# 造型工坊里的 makeVessel 依赖 VES_PTS/VES_MAT（同段内）；makeFigure 依赖 limbGeo、GeoBag 等同段 ✓
fade = cut(base, MARK['fade'], MARK['ui'])
# 本境要用、但在我自己 _prims 里没有的两个构件：从骨架的「场景构件」段取出
scene_seg = cut(base, MARK['scene'], '/* ---------------- 卷首 + 四境 ---------------- */')
disc = cut(scene_seg, 'function makeDisc(o){', 'function makeCliff(o){')
banner = cut(scene_seg, 'function makeBanner(o){', '\n}\n') + '\n}\n'

# —— 继承段的 fadeK 合规补丁：每帧写 opacity/intensity 的抖动因子必须 ≤ 1.0×base×fadeK ——
PATCH = [
    ("if(light)light.intensity=base*(0.80+0.20*Math.sin(t*11.3+s1)+0.12*Math.sin(t*27.7+s2))*k;",
     "if(light)light.intensity=base*(0.76+0.16*Math.sin(t*11.3+s1)+0.06*Math.sin(t*27.7+s2))*k;"),
    ("gl.material.opacity=k*baseOp*(0.80+0.20*Math.sin(t*5.3+ph)+0.08*Math.sin(t*13.1+ph));",
     "gl.material.opacity=k*baseOp*(0.78+0.16*Math.sin(t*5.3+ph)+0.02*Math.sin(t*13.1+ph));"),
    ("it.s.material.opacity=it.op0*k*(0.7+0.3*Math.sin(t*0.23+it.seed));",
     "it.s.material.opacity=it.op0*k*(0.66+0.30*Math.sin(t*0.23+it.seed));"),
    ("gd.material.opacity=k*baseOp*(0.85+0.15*Math.sin(t*3.7+r));",
     "gd.material.opacity=k*baseOp*(0.82+0.15*Math.sin(t*3.7+r));"),
]
for a, b in PATCH:
    assert a in engine, '补丁目标未找到: ' + a[:60]
    engine = engine.replace(a, b)

head = rd('_head.txt')
poem = rd('_poem.js')
quiz = rd('_quiz.txt')
prims = rd('_prims.js') + '\n' + disc + banner
builders = rd('_builders.js')
stages = rd('_stages.js')
tail = rd('_tail.js')

data = (MARK['data'] + '\n'
        + "const py = s => s.split(' ');\nconst POEM = [\n" + poem + "\n];\n" + quiz + '\n')

out = (head + '\n' + tools + data + engine + prims + builders + stages + fade + tail)
io.open('index.html', 'w', encoding='utf-8', newline='\n').write(out)

n = out.count('\n')
print('index.html lines =', n)
for k, v in [('clamp(i,0,7)', "clamp(i,0,7)"), ("'08.mp3'", "'08.mp3'"),
             ("curIdx===7&&state==='stage'", "curIdx===7&&state==='stage'"),
             ('--gold:#c98f5a', '--gold:#c98f5a'), ('galLink', 'galLink'),
             ('autoMode=true', 'autoMode=true'), ('将进酒', '将进酒'), ('万古愁', '万古愁'),
             ('0x05070d', '0x05070d'), ('d4af37', 'd4af37')]:
    print('%-34s x%d' % (k, out.count(v)))
