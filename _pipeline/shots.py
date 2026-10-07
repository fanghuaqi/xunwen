#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
shots.py —— 用 Chrome DevTools Protocol 驱动无头 Chrome，实拍「循文入境」页面的每一境。

为什么需要它：validate.js / smoke.test.js 都只跑 THREE 桩，证不了"画面对不对"。
建模粗糙、构图出框、景物被雾吃掉这类问题只有真渲染 + 真截图才看得见。

用法:
  python shots.py <index.html 路径> [--out 输出目录] [--stages 0,1,2,3] [--w 1600] [--h 900]
  python shots.py <目录> --all-stages          # 拍封面 + 全部境 + 终章

输出: <输出目录>/stageN.png
"""
import argparse
import base64
import http.client
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def find_chrome():
    for p in CHROME_CANDIDATES:
        if os.path.isfile(p):
            return p
    raise SystemExit("未找到 Chrome/Edge")


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


class CDP:
    """极简 CDP 客户端：只用到 Page / Runtime / Emulation 三个域。"""

    def __init__(self, ws_url):
        import websocket  # websocket-client
        self.ws = websocket.create_connection(ws_url, timeout=60)
        self.id = 0

    def call(self, method, **params):
        self.id += 1
        mid = self.id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError("%s -> %s" % (method, msg["error"]))
                return msg.get("result", {})
            # 其它事件（Page.loadEventFired 等）直接丢弃

    def js(self, expr, timeout=30):
        r = self.call("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True)
        res = r.get("result", {})
        if r.get("exceptionDetails"):
            raise RuntimeError("JS 异常: %s" % json.dumps(r["exceptionDetails"])[:300])
        return res.get("value")

    def wait_for(self, expr, timeout=30, interval=0.25, what=""):
        t0 = time.time()
        while time.time() - t0 < timeout:
            try:
                if self.js(expr):
                    return True
            except Exception:
                pass
            time.sleep(interval)
        raise RuntimeError("等待超时(%ss): %s" % (timeout, what or expr))

    def shot(self, path):
        r = self.call("Page.captureScreenshot", format="png", captureBeyondViewport=False)
        with open(path, "wb") as f:
            f.write(base64.b64decode(r["data"]))
        return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="index.html 路径或诗目录")
    ap.add_argument("--out", default=None)
    ap.add_argument("--stages", default=None, help="逗号分隔的境号；0=封面, -1=终章")
    ap.add_argument("--all-stages", action="store_true")
    ap.add_argument("--w", type=int, default=1600)
    ap.add_argument("--h", type=int, default=900)
    ap.add_argument("--hold", type=float, default=1.6, help="每境过渡结束后的额外等待秒数（等动画起势）")
    args = ap.parse_args()

    if os.path.isdir(args.target):
        page = os.path.join(args.target, "index.html")
    else:
        page = args.target
    if not os.path.isfile(page):
        raise SystemExit("找不到页面: %s" % page)
    page = os.path.abspath(page)
    out = args.out or os.path.join(os.path.dirname(page), "_shots")
    os.makedirs(out, exist_ok=True)
    # 每首单独一个子目录：多首连拍到同一 --out 时，stageN.png 会互相覆盖
    slug = os.path.basename(os.path.dirname(page))
    out = os.path.join(out, slug)
    os.makedirs(out, exist_ok=True)

    chrome = find_chrome()
    port = free_port()
    profile = tempfile.mkdtemp(prefix="cdp-prof-")
    proc = subprocess.Popen([
        chrome, "--headless=new", "--remote-debugging-port=%d" % port,
        "--remote-allow-origins=*",
        "--user-data-dir=%s" % profile, "--no-first-run", "--no-default-browser-check",
        "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",
        "--hide-scrollbars", "--mute-audio", "--window-size=%d,%d" % (args.w, args.h),
        "--allow-file-access-from-files", "about:blank",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    cdp = None
    try:
        # 等调试端口起来
        t0 = time.time()
        ws_url = None
        while time.time() - t0 < 30:
            try:
                c = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
                c.request("GET", "/json/list")
                data = json.loads(c.getresponse().read().decode("utf-8", "replace"))
                for t in data:
                    if t.get("type") == "page":
                        ws_url = t["webSocketDebuggerUrl"]
                        break
                if ws_url:
                    break
            except Exception:
                pass
            time.sleep(0.4)
        if not ws_url:
            raise SystemExit("Chrome 调试端口未就绪")

        cdp = CDP(ws_url)
        cdp.call("Page.enable")
        cdp.call("Runtime.enable")
        cdp.call("Emulation.setDeviceMetricsOverride", width=args.w, height=args.h,
                 deviceScaleFactor=1, mobile=False)

        url = "file:///" + page.replace("\\", "/")
        cdp.call("Page.navigate", url=url)
        # 等页面 boot 完成（initApp 里置 window.__inited；boot 后 canvas 存在）
        cdp.wait_for("!!document.querySelector('canvas')", timeout=45, what="canvas 出现（可能 CDN 加载慢）")
        cdp.wait_for("window.__inited===true", timeout=20, what="initApp 完成")
        time.sleep(1.2)

        # 决策要拍哪些境
        if args.all_stages:
            n = cdp.js("(typeof STAGES!=='undefined')?STAGES.length:0") or 0
            stages = ["cover"] + list(range(1, n)) + ["ending"]
        elif args.stages:
            stages = []
            for s in args.stages.split(","):
                s = s.strip()
                stages.append("cover" if s == "0" else ("ending" if s == "-1" else int(s)))
        else:
            stages = ["cover"]

        errs = cdp.js("JSON.stringify((window.__errs||[]).slice(0,5))")
        made = []
        for st in stages:
            if st == "cover":
                time.sleep(0.6)
                p = cdp.shot(os.path.join(out, "cover.png"))
            elif st == "ending":
                cdp.js("(function(){try{ if(typeof showEnding==='function'){showEnding();return 'ok';} }catch(e){return 'err:'+e.message}})()")
                time.sleep(2.2)
                p = cdp.shot(os.path.join(out, "ending.png"))
            else:
                # 必须先把封面关掉：封面是 z-index 40 的遮罩，不点「入境」它会一直盖住画面。
                # 走真实按钮点击（顺带初始化 WebAudio），再等遮罩淡出。
                cdp.js("(function(){var b=document.getElementById('enterBtn'); if(b)b.click();"
                       "var c=document.getElementById('cover'); if(c)c.classList.add('off'); return 1})()")
                time.sleep(0.8)
                # 关掉自动游览：否则等过渡的几秒里页面会自动切到下一境，拍到的就不是要拍的那一境。
                cdp.js("(function(){ if(typeof autoMode!=='undefined') autoMode=false; return 1})()")
                # 关键：绝对不能强行写 state='stage'。
                # 点「入境」会触发封面→第一境 的过渡；若此时硬写 state='stage'，过渡会被永久打断，
                # 封面停在淡入态、第一境停在 uFade≈0 的淡出态，curStageObj 也永不更新——
                # 结果就是"拍第一境却拍到封面残留、第一境内容全不可见"，会让人误判成页面 bug。
                # 正确做法：先把上一段过渡等完，再 goto 目标境并等它自己走完。
                t0 = time.time()
                while time.time() - t0 < 25:
                    if cdp.js("(typeof state!=='undefined' && state==='stage')"):
                        break
                    time.sleep(0.3)
                cdp.js("(function(){try{ if(typeof goto==='function')goto(%d); }catch(e){} return 1})()" % st)
                t0 = time.time()
                while time.time() - t0 < 25:
                    if cdp.js("(typeof state!=='undefined' && state==='stage' && curIdx===%d)" % st):
                        break
                    time.sleep(0.3)
                time.sleep(args.hold)   # 过渡结束后再等动画起势
                p = cdp.shot(os.path.join(out, "stage%d.png" % st))
            made.append(p)
            print("  ✓ %s" % p)

        print("实拍完成 %d 张 → %s" % (len(made), out))
        if errs and errs != "[]":
            print("页面运行期错误: %s" % errs)
    finally:
        if cdp:
            try:
                cdp.ws.close()
            except Exception:
                pass
        proc.terminate()
        try:
            proc.wait(timeout=8)
        except Exception:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)


if __name__ == "__main__":
    main()
