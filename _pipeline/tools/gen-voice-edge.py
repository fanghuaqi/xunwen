#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gen-voice-edge.py —— 「循文入境」诗词网页的神经语音配音生成（免密钥，诗朗诵级）

引擎：Edge 神经语音（edge-tts）。这里用的是 zh-CN-YunjianNeural / YunxiNeural /
XiaoxiaoNeural —— 与 Azure 付费"诗朗诵"音色同一套神经语音，但无需任何密钥。
（旧脚本 gen-voice.js 走百度翻译 TTS，音色一般；本脚本是它的升级替代。）

用法:
  python gen-voice-edge.py [index.html 路径或诗目录] [--force] [--only 03]

配置（可选，放在诗目录下）:
  tts.json  {"voice":"zh-CN-YunjianNeural","rate":"-15%","pitch":"+0Hz",
             "sub":[["将进酒","枪进酒"], ...]}
  - voice/rate 不给则按该诗在 queue.json 里的风格赛道自动选
  - sub 是多音字同音替换表：只影响音频读音，不改页面文字

输出: <诗目录>/audio/00.mp3（题名）· 01..N.mp3（各境）· N+1.mp3（全篇）
"""
import argparse
import asyncio
import json
import os
import re
import sys

try:
    import edge_tts
except ImportError:
    sys.exit("未安装 edge-tts：请先 pip install -U edge-tts")

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- 音色选择
# 按风格赛道配声：豪放/怀古用沉厚男声，清冷/禅意用清朗男声，婉约/明媚用温暖女声
VOICE_BY_TRACK = {
    "yanye":   ("zh-CN-YunjianNeural", "-12%"),   # 夜宴金彩：豪放宴饮
    "damo":    ("zh-CN-YunjianNeural", "-14%"),   # 大漠金戈：边塞怀古
    "shuimo":  ("zh-CN-YunxiNeural",   "-16%"),   # 水墨夜思：静夜怀乡
    "xuanzhi": ("zh-CN-YunxiNeural",   "-18%"),   # 宣纸留白：孤寂极简
    "yanyu":   ("zh-CN-XiaoxiaoNeural", "-16%"),  # 烟雨江南：婉约
    "qinglv":  ("zh-CN-XiaoxiaoNeural", "-14%"),  # 青绿春晓：明媚
}
DEFAULT_VOICE = ("zh-CN-YunjianNeural", "-15%")

# 首批 8 首 + 将进酒 不在 queue.json 里，单独给赛道
LEGACY_TRACK = {
    "jingyesi": "shuimo", "jiangxue": "xuanzhi", "chunxiao": "qinglv",
    "youziyin": "xuanzhi", "shuidiao-getou": "yanye", "guancanghai": "damo",
    "guanju": "qinglv", "shengshengman": "yanyu", "jiangjinjiu": "yanye",
}

# ------------------------------------------------- 多音字兜底表（高置信度）
# 只收录"必须读罕见音、且神经语音通常会读错"的经典考点；宁缺勿滥——
# 替换错了比不替换更糟。各诗已有的 tts.json / gen-voice.local.js 里的表优先。
SUB_COMMON = [
    ("将进酒", "枪进酒"),      # 将 qiāng
    ("羽扇纶巾", "羽扇官巾"),  # 纶 guān，不读 lún
    ("樯橹", "墙鲁"),          # 樯 qiáng、橹 lǔ
    ("小乔初嫁了", "小乔初嫁瞭"),  # 了 liǎo
    ("一尊还酹", "一尊环酹"),  # 还 huán
    ("早生华发", "早生华髮"),  # 发 fà
    ("多情应笑我", "多情英笑我"),  # 应 yīng
    ("卷起千堆雪", "捲起千堆雪"),  # 卷 juǎn
    ("非是藉秋风", "非是借秋风"),  # 藉 jiè
    ("更著风和雨", "更浊风和雨"),  # 著 zhuó
    ("卜算子", "补算子"),      # 卜 bǔ
    ("浅草才能没马蹄", "浅草才能末马蹄"),  # 没 mò
    ("属国过居延", "蜀国过居延"),  # 属 shǔ
    ("萧关逢候骑", "萧关逢候寄"),  # 骑 jì
    ("都护在燕然", "都护在烟然"),  # 燕 yān
    ("醉里挑灯看剑", "醉里挑灯看剑"),  # 挑 tiǎo（挑 tiǎo 与 tiāo 不同，此处保留）
    ("风吹草低见牛羊", "风吹草低现牛羊"),  # 见 xiàn
    ("乡音无改鬓毛衰", "乡音无改鬓毛催"),  # 衰 cuī
    ("最喜小儿亡赖", "最喜小儿无赖"),  # 亡 wú
    ("塞下曲", "赛下曲"),      # 塞 sài
    ("几度夕阳红", "几度夕阳红"),
]

SUPPRESS_NOOP = True  # 左右相同的占位项不参与替换


def resolve_target(arg):
    p = os.path.abspath(arg or "index.html")
    if os.path.isdir(p):
        p = os.path.join(p, "index.html")
    if not os.path.isfile(p):
        sys.exit("找不到页面: %s" % p)
    return p


def extract_reads(html):
    """按出现顺序取全部 read:'…'（只认主脚本里的，避免抓到注释里的示例）"""
    m = re.search(r'<script id="main">([\s\S]*?)</script>', html)
    body = m.group(1) if m else html
    return re.findall(r"read:'([^']+)'", body)


def poem_title(html):
    t = re.search(r"<title>([^<]*)</title>", html)
    t = t.group(1) if t else ""
    segs = [s.strip() for s in re.split(r"[·|｜]", t)]
    segs = [s for s in segs if s and not re.search(r"three\.js|沉浸|诗词课|网页|interactive|循文入境", s, re.I)]
    # 诗题内含「·」（如 行路难·其一）会被拆开，重组还原完整题名
    return "·".join(segs) if segs else "古诗"


def load_track(slug):
    # queue.json 相对本脚本（tools/ 在 _pipeline/ 内），亦可用环境变量 XUNWEN_QUEUE 覆盖
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # _pipeline/
    q = os.path.join(root, "queue.json")
    cand_env = os.environ.get("XUNWEN_QUEUE")
    for cand in ([cand_env] if cand_env else []) + [q]:
        try:
            data = json.load(open(cand, encoding="utf-8"))
        except Exception:
            continue
        for p in data.get("poems", []):
            if p.get("slug") == slug:
                return p.get("track")
    return None


def load_cfg(poem_dir, slug):
    """配置优先级：tts.json > gen-voice.local.js 里的 SUB > 赛道默认 + 兜底表"""
    sub, voice, rate, src = [], None, None, "兜底表"
    tj = os.path.join(poem_dir, "tts.json")
    if os.path.isfile(tj):
        cfg = json.load(open(tj, encoding="utf-8"))
        sub = [tuple(x) for x in cfg.get("sub", [])]
        voice = cfg.get("voice")
        rate = cfg.get("rate")
        src = "tts.json"
    else:
        # 迁移旧的 gen-voice.local.js：SUB 表是子代理逐句核过的，必须继承
        js = os.path.join(poem_dir, "gen-voice.local.js")
        if os.path.isfile(js):
            txt = open(js, encoding="utf-8").read()
            body = re.search(r"const SUB\s*=\s*\[([\s\S]*?)\];", txt)
            if body:
                for a, b in re.findall(r"\[\s*'([^']*)'\s*,\s*'([^']*)'\s*\]", body.group(1)):
                    sub.append((a, b))
                if sub:
                    src = "gen-voice.local.js"
    if not sub:
        sub = list(SUB_COMMON)
        src = "兜底表"
    sub = [(a, b) for a, b in sub if a and b and a != b]
    if not voice or not rate:
        v, r = VOICE_BY_TRACK.get(load_track(slug) or LEGACY_TRACK.get(slug), DEFAULT_VOICE)
        voice = voice or v
        rate = rate or r
    return voice, rate, sub, src


def validate_mp3(path):
    if not os.path.isfile(path):
        return False
    d = open(path, "rb").read(4)
    return len(d) >= 4 and (d[0] == 0xFF or d[:3] == b"ID3")


async def synth_one(text, voice, rate, pitch, out, tries=4):
    last = None
    tmp = out + ".part"
    for a in range(1, tries + 1):
        try:
            c = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
            await c.save(tmp)
            if validate_mp3(tmp) and os.path.getsize(tmp) > 800:
                os.replace(tmp, out)          # 原子替换：失败不会弄坏已有音频
                return os.path.getsize(out)
            last = RuntimeError("返回内容不是有效 MP3")
        except Exception as e:
            last = e
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass
        await asyncio.sleep(1.2 * a)
    raise last or RuntimeError("合成失败")


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default="index.html")
    ap.add_argument("--force", action="store_true", help="重生成已存在的文件")
    ap.add_argument("--only", default=None, help="只生成某一个文件（如 03）")
    ap.add_argument("--dry", action="store_true", help="只打印计划，不合成")
    args = ap.parse_args()

    page = resolve_target(args.target)
    poem_dir = os.path.dirname(page)
    slug = os.path.basename(poem_dir)
    html = open(page, encoding="utf-8").read()
    reads = extract_reads(html)
    if not reads:
        sys.exit("未解析到任何 read:'…' 句")

    outdir = os.path.join(poem_dir, "audio")
    os.makedirs(outdir, exist_ok=True)
    voice, rate, sub, src = load_cfg(poem_dir, slug)
    title = poem_title(html)

    def apply_sub(t):
        s = t
        for a, b in sub:
            s = s.replace(a, b)
        return s

    jobs = [("00", "%s。" % title)]
    jobs += [(str(i + 1).zfill(2), t) for i, t in enumerate(reads)]
    jobs += [(str(len(reads) + 1).zfill(2), "".join(reads))]

    print("页面: %s" % page)
    print("题名: %s" % title)
    print("音色: %s  语速: %s" % (voice, rate))
    print("多音字表来源: %s（%d 条）" % (src, len(sub)))
    hits = [a for a, b in sub if a in "".join(reads)]
    if hits:
        print("本诗命中的替换: %s" % "、".join(hits))
    print("句数: %d ｜ 计划输出 %d 个文件 → %s" % (len(reads), len(jobs), outdir))

    ok = skip = fail = 0
    for name, text in jobs:
        if args.only and name != args.only.zfill(2):
            continue
        out = os.path.join(outdir, "%s.mp3" % name)
        if not args.force and validate_mp3(out):
            print("  · %s.mp3 已存在且有效，跳过（--force 可重生成）" % name)
            skip += 1
            continue
        say = apply_sub(text)
        if args.dry:
            print("  → %s.mp3  %s" % (name, say[:34] + ("…" if len(say) > 34 else "")))
            continue
        try:
            size = await synth_one(say, voice, rate, "+0Hz", out)
            print("  ✓ %s.mp3  %5.1f KB  ← %s" % (name, size / 1024.0, say[:22] + ("…" if len(say) > 22 else "")))
            ok += 1
            await asyncio.sleep(0.35)
        except Exception as e:
            fail += 1
            print("  ✗ %s.mp3 失败: %s" % (name, str(e)[:110]))

    if not args.dry:
        print("完成：新生成 %d ｜ 跳过 %d ｜ 失败 %d" % (ok, skip, fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
