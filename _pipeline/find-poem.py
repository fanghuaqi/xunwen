#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
find-poem.py —— 从本地 chinese-poetry 语料库按「标题 + 作者」取出权威原文（自动转简体）。

语料覆盖：全唐诗 / 唐诗三百首（繁体）、宋词（简体）、水墨唐诗（简体）、
楚辞、曹操诗集、蒙学（部分）、五代诗词、元曲、纳兰性德 等。

用法:
  python find-poem.py 春江花月夜 张若虚
  python find-poem.py 短歌行 曹操 --all      # 列出所有匹配（含不同版本）
"""
import argparse
import glob
import io
import json
import os
import sys

import zhconv

# 语料库根目录（可选依赖）：设环境变量 XUNWEN_CORPUS 指向 chinese-poetry 克隆，
# 或把克隆放到本仓库同级目录 ./chinese-poetry
ROOTS = [p for p in (os.environ.get("XUNWEN_CORPUS"),
                     os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "chinese-poetry")) if p]


def files():
    out = []
    for R in ROOTS:
        for p in glob.glob(os.path.join(R, "**", "*.json"), recursive=True):
            low = p.lower()
            if "images" in low or "loader" in low or "authors." in low or "rank" in low:
                continue          # 榜单/作者索引里只有标题没有正文
            try:
                if os.path.getsize(p) > 40 * 1024 * 1024:
                    continue      # 超大文件单独处理，避免一次性读爆内存
            except OSError:
                continue
            out.append(p)
    return out


def entries(path):
    """把各种结构的语料统一成 {title, author, paras} 迭代器（原样，不转换——转换很慢，
    只在命中之后做，见 main）。strains/*.json 只有平仄没有正文，自然被跳过。"""
    try:
        d = json.load(io.open(path, encoding="utf-8"))
    except Exception:
        return
    items = d if isinstance(d, list) else (list(d.values()) if isinstance(d, dict) else [])
    for it in items:
        if not isinstance(it, dict):
            continue
        title = it.get("title") or it.get("rhythmic") or it.get("chapter") or ""
        author = it.get("author") or it.get("poet") or ""
        paras = it.get("paragraphs") or it.get("content") or it.get("para") or []
        if isinstance(paras, str):
            paras = [paras]
        if not paras:
            continue
        yield str(title), str(author), [str(x) for x in paras]


def flat(paras):
    return "".join(p.strip() for p in paras)


def variants(s):
    """繁简两种写法——语料里标题多为繁体、作者字段繁简混杂，两边都得能匹配"""
    return {s, zhconv.convert(s, "zh-cn"), zhconv.convert(s, "zh-tw")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title")
    ap.add_argument("author", nargs="?", default="")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    tv = variants(args.title)
    av = variants(args.author) if args.author else set()

    hits = []
    for p in files():
        for t, a, paras in entries(p):
            if not any(x in t for x in tv):
                continue
            if av and a and not any(x in a for x in av):
                continue          # 语料个别集子（如曹操诗集）没有 author 字段，此时不因作者失配而丢弃
            if not av and t not in tv:
                continue
            hits.append((t, a, paras, p))

    if not hits:
        print("未找到：%s %s" % (args.title, args.author))
        return 1

    # 去重 + 按正文长度排序（完整版通常更长）
    seen, uniq = set(), []
    for t, a, paras, p in hits:
        key = (zhconv.convert(t, "zh-cn"), zhconv.convert(a, "zh-cn"), flat(paras))
        if key in seen:
            continue
        seen.add(key)
        uniq.append((t, a, paras, p))
    uniq.sort(key=lambda x: -len(flat(x[2])))

    if not args.all and len(uniq) > 1:
        uniq = uniq[:1]

    for t, a, paras, p in uniq:
        paras = [zhconv.convert(x, "zh-cn") for x in paras]
        t, a = zhconv.convert(t, "zh-cn"), zhconv.convert(a, "zh-cn")
        body = flat(paras)
        print("═" * 70)
        print("《%s》 %s" % (t, a))
        print("来源: %s" % os.path.relpath(p, ROOTS[0]))
        print("字数: %d（含标点 %d）" % (len([c for c in body if "\u4e00" <= c <= "\u9fff"]), len(body)))
        print("-" * 70)
        for i, x in enumerate(paras, 1):
            print("  %2d. %s" % (i, x))
        print("正文: %s" % body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
