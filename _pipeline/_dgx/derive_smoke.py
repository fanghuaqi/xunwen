# -*- coding: utf-8 -*-
"""derive_smoke.py —— 从 wanghaichao/smoke.test.js 派生新诗的冒烟测试
用法: python derive_smoke.py <slug> <title显示> <N> <minlen> <fogmax> <交互境名> <全诗音频号如05> <gold> <bg> <作者朝代如"唐·李白"> <必在文本1> [必在文本2 ...]
"""
import io, re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'wanghaichao', 'smoke.test.js')

def main():
    slug, shown, N, minlen, fogmax, inter_name, mp3, gold, bg = sys.argv[1:10]
    checks = sys.argv[10:]
    N, minlen = int(N), int(minlen)
    s = io.open(SRC, encoding='utf-8').read()
    s = s.replace('《望海潮》（宋·柳永）', shown)
    s = s.replace('本诗应为 5 境 + 卷首', '本诗应为 %d 境 + 卷首' % N)
    s = s.replace(".join('').length>90", ".join('').length>%d" % minlen)
    s = s.replace('<=0.0080', '<=%s' % fogmax)
    s = s.replace('if(i===5){', 'if(i===%d){' % N)
    s = s.replace('STAGES[5].build()', 'STAGES[%d].build()' % N)
    s = s.replace("curStageObj=obj; state='stage'; curIdx=5;", "curStageObj=obj; state='stage'; curIdx=%d;" % N)
    s = s.replace("if(curIdx===5&&state==='stage'&&curStageObj.click){", "if(curIdx===%d&&state==='stage'&&curStageObj.click){" % N)
    s = re.sub(r"if\(def\.name==='千骑高牙'\)", "if(def.name==='%s')" % inter_name, s)
    txt_lines = ',\n'.join("  [/%s/, '%s 在位']" % (t, t) for t in checks)
    block = """const htmlChecks = [
  [/autoMode=true/, 'autoMode 默认 true'],
  [/id="btnAuto" class="on">自动游览 · 开/, '自动游览按钮默认 .on + 文案「自动游览 · 开」'],
  [/galLink[\\s\\S]*返回诗集目录/, '封面返回诗集目录链接'],
  [/id="btnCover"[\\s\\S]*galLink[\\s\\S]*诗集目录/, '终章返回诗集目录链接'],
  [/\\.galLink\\{display:inline-block/, '.galLink 样式已注入 </style> 前'],
  [new RegExp('clamp[(]i,0,' + N + '[)]'), 'goto clamp(i,0,' + N + ')'],
  [/'%s\\.mp3'/, '全诗音频 %s.mp3'],
  [/--gold:%s/, '--gold = 分配强调色 %s'],
  [/curIdx===%d&&state==='stage'&&curStageObj/, '交互境 curIdx===%d 接线'],
  [/background:%s/, '赛道底色 %s'],
%s,
  [/将进酒|万古愁/, '无《将进酒》残留（应为 false）'],
  [/makeRange\\(/, '使用多峰山脊 makeRange'],
  [/makeForeground\\(/, '使用前景框景 makeForeground'],
  [/makeFigure\\(/, '使用唐装人物 makeFigure'],
  [/makeCrowd\\(/, '使用远景人影 makeCrowd'],
];""" % (mp3, mp3, gold, gold, N, N, bg, bg, txt_lines)
    i = s.index('const htmlChecks = [')
    j = s.index('];', i) + 2
    s = s[:i] + block + s[j:]
    out = os.path.join(HERE, '..', '..', slug, 'smoke.test.js')
    io.open(out, 'w', encoding='utf-8', newline='\n').write(s)
    print('written', out)

if __name__ == '__main__':
    main()
