#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ci_browser_check.py —— CI 真浏览器健康检查（Playwright + Chromium）

用法:
  python _pipeline/ci_browser_check.py <slug> [<slug>...] [--port 8123]

对每个诗页做端到端验证（本地静态服务 + 无头 Chromium）：
  1. 页面加载无未捕获异常（pageerror 记失败；console.error 仅记录不判死）
  2. 卷首出现「入境」按钮
  3. 按空格能入境（卷首隐去）——对应全站空格键进入功能
  4. 方向键可推进一境
  5. 点击「释 义」标题面板可折叠/展开——对应释义折叠功能
  6. 每页存卷首/两境截图到 _ci-shots/ 供人工复核

本地也可用（需 pip install playwright && playwright install chromium）。
"""
import argparse
import functools
import http.server
import os
import socketserver
import sys
import threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_ci-shots")

handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)


def serve(port):
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", port), handler)
    httpd.serve_forever()


def check_one(pw_browser, base, slug):
    """返回 (失败列表, console错误列表)；失败列表非空即该页不合格"""
    fails, console_err = [], []
    ctx = pw_browser.new_context(viewport={"width": 1600, "height": 900})
    page = ctx.new_page()
    page.on("pageerror", lambda e: fails.append("pageerror: %s" % e))
    page.on("console", lambda m: console_err.append(m.text) if m.type == "error" else None)
    try:
        page.goto("%s/%s/index.html" % (base, slug), wait_until="load", timeout=30000)
        page.wait_for_selector("#enterBtn", timeout=15000)
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(OUT, slug + "-cover.png"))

        # 空格入境（卷首隐去）。SwiftShader 软渲染编译首批着色器会阻塞主线程数秒，
        # 必须 polling 用定时器而非默认 RAF，否则等待函数与页面一起被饿死
        page.keyboard.press("Space")
        page.wait_for_function(
            "() => document.querySelector('#cover').classList.contains('off')",
            timeout=30000, polling=200)
        page.wait_for_timeout(4000)

        # 释义面板折叠/展开
        page.click("#notePanel h3")
        folded = page.evaluate("document.querySelector('#notePanel').classList.contains('fold')")
        page.click("#notePanel h3")
        unfolded = page.evaluate("document.querySelector('#notePanel').classList.contains('fold')")
        if not folded:
            fails.append("释义面板点击后未折叠")
        if unfolded:
            fails.append("释义面板再次点击后未展开")

        # 方向键推进一境
        page.keyboard.press("ArrowRight")
        page.wait_for_timeout(3000)
        page.screenshot(path=os.path.join(OUT, slug + "-stage2.png"))
    except Exception as e:  # noqa: BLE001 —— 任何等待超时都记为该页失败
        fails.append("异常: %s" % e)
    finally:
        ctx.close()
    return fails, console_err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="+")
    ap.add_argument("--port", type=int, default=8123)
    ap.add_argument("--channel", default=None,
                    help="用系统浏览器渠道（chrome/msedge）替代 Playwright 自带 Chromium")
    a = ap.parse_args()

    os.makedirs(OUT, exist_ok=True)
    t = threading.Thread(target=serve, args=(a.port,), daemon=True)
    t.start()
    base = "http://127.0.0.1:%d" % a.port

    from playwright.sync_api import sync_playwright

    SW = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader"]

    def launch(p):
        """默认自带 Chromium；失败则依次回退系统 Chrome / Edge"""
        attempts = [({}, a.channel)] if a.channel else [({}, None), ({"channel": "chrome"}, None),
                                                        ({"channel": "msedge"}, None)]
        last = None
        for kw, ch in attempts:
            try:
                if ch:
                    return p.chromium.launch(channel=ch, args=SW)
                return p.chromium.launch(args=SW)
            except Exception as e:  # noqa: BLE001
                last = e
        raise SystemExit("无法启动浏览器（已尝试自带 Chromium/Chrome/Edge）：%s" % last)

    bad = 0
    with sync_playwright() as p:
        browser = launch(p)
        for i, slug in enumerate(a.slugs, 1):
            fails, console_err = check_one(browser, base, slug)
            mark = "✗" if fails else "✓"
            print("[%d/%d] %s %s" % (i, len(a.slugs), mark, slug), flush=True)
            for f in fails:
                print("    " + f, flush=True)
            for c in console_err[:5]:
                print("    [console.error] %s" % c[:160], flush=True)
            if fails:
                bad += 1
        browser.close()
    print("浏览器健康检查：%d/%d 通过" % (len(a.slugs) - bad, len(a.slugs)))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
