#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
regen-all-voice.py —— 把全部诗词页面的打包配音换成 Edge 神经语音（诗朗诵级）。

对仓库根目录下每个含 index.html 的诗目录调用
gen-voice-edge.py --force。逐目录独立失败不影响其它；最后打印汇总。
"""
import os
import subprocess
import sys
import time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "gen-voice-edge.py")

only = sys.argv[1:]  # 可选：只跑指定 slug

dirs = []
for d in sorted(os.listdir(BASE)):
    p = os.path.join(BASE, d)
    if d == "_pipeline" or not os.path.isdir(p):
        continue
    if not os.path.isfile(os.path.join(p, "index.html")):
        continue
    if only and d not in only:
        continue
    dirs.append(d)

print("待处理 %d 首" % len(dirs))
bad, t0 = [], time.time()
for i, d in enumerate(dirs, 1):
    t = time.time()
    r = subprocess.run([sys.executable, GEN, os.path.join(BASE, d), "--force"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = (r.stdout or "").strip().splitlines()
    line = tail[-1] if tail else ""
    mark = "✓" if r.returncode == 0 else "✗"
    if r.returncode != 0:
        bad.append((d, line or (r.stderr or "")[-160:]))
    print("[%3d/%d] %s %-24s %5.1fs  %s" % (i, len(dirs), mark, d, time.time() - t, line))
    sys.stdout.flush()

print("\n总计 %.1f 分钟" % ((time.time() - t0) / 60))
if bad:
    print("失败 %d 首：" % len(bad))
    for d, m in bad:
        print("  ✗ %s  %s" % (d, m))
else:
    print("全部成功 ✓")
