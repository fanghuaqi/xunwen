#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
extend3.py —— 把第三批（高意境名篇）并入 queue.json 与 manifest.json。

入库前自检：slug 唯一、分境拼接与全文逐字一致、赛道合法、境数≥2。
"""
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("b3", os.path.join(HERE, "batch3-data.py"))
b3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b3)

qpath = os.path.join(HERE, "queue.json")
mpath = os.path.join(HERE, "manifest.json")
q = json.load(io.open(qpath, encoding="utf-8"))
man = json.load(io.open(mpath, encoding="utf-8"))

existing = {p["slug"] for p in q["poems"]}
maxno = max(p["no"] for p in q["poems"])
added, bad = [], []

for p in b3.BATCH3:
    if p["slug"] in existing:
        bad.append((p["slug"], "slug 已存在"))
        continue
    if "".join(p["stages"]) != p["text"]:
        bad.append((p["slug"], "分境拼接与全文不一致"))
        continue
    if p["track"] not in q["tracks"]:
        bad.append((p["slug"], "赛道非法: %s" % p["track"]))
        continue
    if len(p["stages"]) < 2:
        bad.append((p["slug"], "境数不足"))
        continue
    if len(p["text"]) < 20:
        bad.append((p["slug"], "正文过短"))
        continue
    maxno += 1
    q["poems"].append({
        "no": maxno, "slug": p["slug"], "title": p["title"], "author": p["author"],
        "dynasty": p["dynasty"], "track": p["track"], "accent": p["accent"],
        "text": p["text"], "stages": p["stages"],
        "moment": p["moment"], "interact": p["interact"], "note": p.get("note", ""),
    })
    man[p["slug"]] = {"status": "queued", "attempts": 0}
    added.append((p["slug"], p["title"], len(p["stages"])))

if bad:
    print("有 %d 条未入库：" % len(bad))
    for s, m in bad:
        print("  ✗ %s  %s" % (s, m))
    sys.exit(1)

json.dump(q, io.open(qpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(man, io.open(mpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("入库 %d 首（no 续至 %d）：" % (len(added), maxno))
for s, t, n in added:
    print("  + %-22s %-12s %d境" % (s, t, n))
cnt = {}
for v in man.values():
    cnt[v["status"]] = cnt.get(v["status"], 0) + 1
print("manifest:", json.dumps(cnt, ensure_ascii=False))
print("queue 总数:", len(q["poems"]))
