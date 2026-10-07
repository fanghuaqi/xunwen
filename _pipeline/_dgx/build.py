# -*- coding: utf-8 -*-
"""build.py <name> —— 从 reference-jiangjinjiu.html 骨架生成 <slug>/index.html
name 取 _dgx/<name>.py，须提供 META / POEM_JS / QUIZ_JS / SCENES_JS / STAGES_JS。
用法: python build.py duan
"""
import importlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKEL = os.environ.get('XUNWEN_TEMPLATE') or os.path.join(HERE, 'reference-jiangjinjiu.html')
BASE = os.path.dirname(os.path.dirname(HERE))  # chinese-poetry-xunwen/

GALINK_CSS = """/* ---------- 返回诗集目录 ---------- */
.galLink{display:inline-block;font-family:var(--song);font-size:12.5px;letter-spacing:.25em;color:var(--dim);text-decoration:none;border:1px solid var(--line);border-radius:20px;padding:7px 18px;transition:all .3s}
.galLink:hover{color:var(--gold);border-color:var(--gold)}
#endBtns .galLink{align-self:center}
"""


def must(s, old, new, cnt=None):
    n = s.count(old)
    if n == 0:
        raise SystemExit('build: 找不到待替换串: %r' % old[:60])
    if cnt is not None and n != cnt:
        raise SystemExit('build: 替换串出现 %d 次(期望 %d): %r' % (n, cnt, old[:60]))
    return s.replace(old, new)


def build(name):
    cfg = importlib.import_module(name)
    M = cfg.META
    N = M['N']
    src = open(SKEL, encoding='utf-8').read()

    # 1. 标题 / 主脚本注释
    src = must(src, '<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>',
               '<title>循文入境 · %s | Three.js 沉浸式诗词课堂</title>' % M['title'], 1)
    src = must(src, """/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件
   十二境随诗句推进，含注音/释义/注释/朗读/小测 */""",
               '/* 循文入境 · %s（%s）—— Three.js 沉浸式诗词课件\n   %d 境随诗句推进，含注音/释义/注释/朗读/小测 */'
               % (M['title'], M['dyn'], N), 1)

    # 2. :root（--gold 必须精确等于本诗 accent）
    m = re.search(r':root\{[^}]*\}', src)
    src = src[:m.start()] + M['root'] + src[m.end():]

    # 3. 全局色字面量（金色辉光 / 底色 / 渐变）
    src = must(src, '212,175,55', M['gold_rgb'])
    for old, new, cnt in M['repl_colors']:
        src = must(src, old, new, cnt)

    # 4. 顶栏 brand
    src = must(src, '<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>',
               '<div id="brand">%s<small>循 文 入 境 · %s</small></div>' % (M['title'], M['brand_author']), 1)

    # 5. POEM+CN 与 QUIZ 整段替换
    i = src.index('const POEM = [')
    j = src.index('const QUIZ = [')
    k = src.index('\n];', j)
    src = src[:i] + cfg.POEM_JS.strip() + '\n\n' + cfg.QUIZ_JS.strip() + '\n' + src[k + len('\n];'):]

    # 6. 场景 builder 整段替换
    a = src.index('/* ---------------- 十三境场景 ---------------- */')
    b = src.index('/* ---------------- 境定义 ---------------- */')
    src = src[:a] + cfg.SCENES_JS.strip() + '\n\n' + src[b:]

    # 7. SK + STAGES 整段替换
    c = src.index('const SK=')
    d = src.index('/* ---------------- 淡入淡出')
    src = src[:c] + cfg.STAGES_JS.strip() + '\n\n' + src[d:]

    # 8. 边界常量（数量联动清单）—— 先换空格块（内含 >=13），再换通用串
    src = must(src, 'i=clamp(i,0,13);', 'i=clamp(i,0,%d);' % N, 1)
    src = must(src, 'for(let i=1;i<=13;i++){', 'for(let i=1;i<=%d;i++){' % N, 1)
    src = must(src, 'if(curIdx===13)showEnding()', 'if(curIdx===%d)showEnding()' % N, 1)
    src = must(src, """      if(curIdx===7&&state==='stage'&&curStageObj.click)curStageObj.click();
      else if(curIdx>=13)showEnding();
      else goto(curIdx+1);""",
               """      if(curIdx===%d&&state==='stage'&&curStageObj.click){
        // 末境：空格先触发交互，交互过后再按才进终章
        if(!curStageObj.clicked)curStageObj.click();
        else showEnding();
      }
      else if(curIdx>=%d)showEnding();
      else goto(curIdx+1);""" % (N, N), 1)
    src = must(src, 'if(curIdx>=13)showEnding()', 'if(curIdx>=%d)showEnding()' % N, 2)
    src = must(src, "'14.mp3'", "'%02d.mp3'" % (N + 1), 2)
    src = must(src, "else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');",
               "else aiSpeak('00.mp3','%s');" % M['cover_read'], 1)
    src = must(src, "if(curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click)curStageObj.click();",
               "if(curIdx===%d&&state==='stage'&&curStageObj&&curStageObj.click)curStageObj.click();" % N, 1)
    src = must(src, "if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);",
               "if(i===%d)setTimeout(()=>tip('%s'),2600);" % (N, M['tip']), 1)

    # 9. galLink 样式 + 两处返回链接
    src = must(src, '\n</style>', '\n' + GALINK_CSS + '</style>', 1)
    src = must(src, '<div id="coverHint">← → 键或空格逐境游览 · 第七境可点击画面与君同酌<br>建议开启声音并佩戴耳机 · 需联网加载三维引擎</div>',
               '<div id="coverHint">%s<br>建议开启声音并佩戴耳机 · 需联网加载三维引擎</div>\n      <div style="margin-top:20px"><a class="galLink" href="../index.html">← 返回诗集目录</a></div>' % M['hint'], 1)
    src = must(src, '<button id="btnCover">回到封面</button>',
               '<button id="btnCover">回到封面</button>\n      <a class="galLink" href="../index.html" style="align-self:center">诗集目录</a>', 1)

    # 10. 自动游览默认开
    src = must(src, 'let trans=null,stageT=0,autoT=0,autoMode=false;',
               'let trans=null,stageT=0,autoT=0,autoMode=true;', 1)
    src = must(src, '<button id="btnAuto">自动游览 · 关</button>',
               '<button id="btnAuto" class="on">自动游览 · 开</button>', 1)

    # 11. 封面 / 终章文案 / 小测评语
    src = must(src, '<h1>将进酒</h1>', '<h1>%s</h1>' % M['title'], 1)
    src = must(src, '<div class="dyn">唐 · 李白</div>', '<div class="dyn">%s</div>' % M['dyn'], 1)
    src = must(src, '<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>',
               '<p>%s</p>' % M['cover_p1'], 1)
    src = must(src, '<p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>',
               '<p>%s</p>' % M['cover_p2'], 1)
    src = must(src, '<h2>酒尽 · 愁销</h2>', '<h2>%s</h2>' % M['end_h2'], 1)
    src = must(src, '<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>',
               '<div class="sub">%s 境 已 尽 · 全 诗 在 此</div>' % M['cn_word'], 1)
    src = must(src, "const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];",
               'const words=%s;' % M['words_js'], 1)

    # 12. 常驻远山的大气色（随赛道换）
    if 'sky_atmo' in M:
        src = must(src, 'seed:20260929,atmo:0x2a3d58', 'seed:20260929,atmo:%s' % M['sky_atmo'], 1)

    # 13. 残留自检（accept.js 同口径；禁词表可按诗覆盖——如 quiz 干扰项合法提到「李白」）
    for bad in M.get('residual', ('将进酒', '万古愁', '太白', '李白')):
        if bad in src:
            raise SystemExit('build: 残留 %r' % bad)

    out_dir = os.path.join(BASE, M['slug'])
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'index.html')
    open(out, 'w', encoding='utf-8', newline='\n').write(src)
    print('written:', out, len(src), 'chars')


if __name__ == '__main__':
    build(sys.argv[1])
