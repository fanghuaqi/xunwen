#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""_patch.py —— 把 index.html 里某个顶层函数整体替换为新实现（仅本诗生产期临时工具，交付前删除）

用法:
  python _patch.py <函数名> <新实现文件>
新实现文件内容从 "function <名>(" 开始，到"下一个顶层 function/const/结尾"为止的整段。
文件里若以 '##' 开头表示只替换 JS 片段（不校验函数头）。
"""
import io, re, sys

name = sys.argv[1]
src = io.open(sys.argv[2], encoding='utf-8').read()
p = io.open('index.html', encoding='utf-8')
html = p.read()
p.close()

# 找函数的起点（行首 function name( ）
pat = re.compile(r'^function ' + re.escape(name) + r'\(', re.M)
m = pat.search(html)
if not m:
    sys.exit('未找到顶层函数 ' + name)
start = m.start()
# 找函数终点：从 start 起做括号配平（跳过字符串/模板/注释/正则的粗略处理）
i = html.index('{', start)
depth = 0
j = i
in_s = None      # 当前字符串类型
while j < len(html):
    c = html[j]
    if in_s:
        if c == '\\':
            j += 2
            continue
        if c == in_s:
            in_s = None
        j += 1
        continue
    if c in '"\'`':
        in_s = c
        j += 1
        continue
    if c == '/' and j + 1 < len(html) and html[j + 1] == '/':
        j = html.index('\n', j)
        continue
    if c == '/' and j + 1 < len(html) and html[j + 1] == '*':
        j = html.index('*/', j) + 2
        continue
    if c == '{':
        depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            j += 1
            break
    j += 1
end = j
old = html[start:end]
new = src.rstrip('\n')
io.open('index.html', 'w', encoding='utf-8', newline='').write(html[:start] + new + html[end:])
print('已替换 %s：%d 字符 → %d 字符' % (name, len(old), len(new)))
