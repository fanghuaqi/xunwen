# 贡献指南 · 循文入境

感谢你有兴趣为「循文入境」做贡献！无论是改一个注音、修一处释义，还是新增一首诗，都欢迎。

## 行为约定

- 保持友善与耐心，这是一份服务于课堂的项目
- 提交 PR 前请确认对应检查全绿（见下文）
- 贡献的内容（代码与文案）将随项目以 [CC BY-NC-SA 4.0](LICENSE) 释出，提交即表示你同意

## 贡献类型

### 1. 纠错（最欢迎，门槛最低）

注音错误、释义不准、错别字、注释考点缺漏 —— 直接改 `<slug>/index.html` 里对应字段即可：

| 字段 | 位置 | 注意 |
|---|---|---|
| `segs[].p` | 逐字拼音数组 | **拼音数必须等于汉字数**（标点不注音），validate.js 强制 |
| `segs[].c` | 诗句原文 | **逐字不可随意改动**——诗文以 queue.json 为唯一口径 |
| `yisi` / `zhu` | 释义 / 注释 | 白话通顺、注释含考点（多音字/典故） |
| `tts.json` | 多音字读音替换 | 只影响朗读，不改页面文字 |

改完运行：

```bash
node _pipeline/tools/validate.js <slug>/index.html   # 结构校验，必须全绿
node _pipeline/accept.js <slug>                      # 验收，必须 ACCEPT
```

### 2. 新增一首诗

推荐走「骨架变换」管线（_pipeline/_dgx/），它把易错点全部自动化拦截：

1. **登记**：在 `_pipeline/queue.json` 的 `poems` 数组追加条目（`no` 顺延；`slug` 小写 kebab-case；`text` 全文；`stages` 分境——一句一境，超长联句可拆上下句；`track` 六赛道之一；`accent` 本诗强调色）
2. **建页**：参考 `_dgx/duan.py`（深色）或 `_dgx/xue.py`（浅色）写一个配置模块（META + POEM/QUIZ/SCENES/STAGES 四段 JS），然后 `python _pipeline/_dgx/build.py <name>` 从骨架生成 `<slug>/index.html`
3. **校验**：`node _pipeline/tools/validate.js <slug>/index.html` 全绿
4. **冒烟**：复制相邻诗的 `smoke.test.js` 改写为本诗版（改 N/交互境号/htmlChecks），`node <slug>/smoke.test.js` 必须 SMOKE PASS
5. **配音**：写 `<slug>/tts.json`（逐句核对多音字），`python _pipeline/tools/gen-voice-edge.py <slug>`，文件数 = 朗读句数 + 2
6. **文档**：写 `<slug>/README.md`（境表/操作/教学建议/文件清单）
7. **验收登记**：`node _pipeline/accept.js <slug>` 必须 ACCEPT → `node _pipeline/mark-done.js <slug>` → `node _pipeline/update-gallery.js` → `node _pipeline/style-audit.js` 全绿
8. （可选但强烈推荐）`cd _pipeline && python shots.py ../<slug> --out <目录>` 实拍逐境截图自查：三层构图、主体可读性、无浮空物件

### 3. 引擎 / 体验改进

改公共引擎段前请先读 [docs/architecture.md](docs/architecture.md) —— 里面有**每一条都真实炸过**的硬性约束（顶层禁 THREE、STAGES 对齐、fadeK、renderOrder、雾预算、绝不要强写 `state='stage'`……）。改动后需要全集回归：

```bash
for f in */smoke.test.js; do node "$f" || echo "FAIL: $f"; done   # 全量冒烟
node _pipeline/style-audit.js                                     # 风格一致性
```

### 4. 美术方向

六大风格赛道见 [docs/art-direction.md](docs/art-direction.md)，意象→场景原型对照见 [docs/scene-library.md](docs/scene-library.md)。核心纪律：**拒绝千诗一面** —— 每首诗必须换全套色板/粒子母题，并自创一个场景库里没有的"标志性瞬间"。

## 本地开发提示

- 无需安装任何依赖；Node ≥ 18、Python ≥ 3.10（配音需 `pip install -U edge-tts`，版本 ≥ 7.2.8）
- `smoke.test.js` 的三维引擎：优先用诗目录内的本地副本，缺失时自动回退 `_pipeline/vendor/three.min.js`（已随仓库提供）
- `find-poem.py`（语料校对）是可选工具：需要 [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) 的本地克隆，设环境变量 `XUNWEN_CORPUS` 指向它即可
- 实拍工具 `shots.py` 需要本机 Chrome/Edge，用无头模式逐境截图（`--stages 1,2 --out 目录`）

## PR 检查清单

CI 会在 PR 和 push 时自动执行：改动诗的结构校验/冒烟/确定性验收 + 全库风格审查 + （改动 ≤ 40 首时）Playwright 真浏览器健康检查；动到 `_pipeline/` 时自动回退全量。以下清单供本地自查：

- [ ] `node _pipeline/tools/validate.js <改动页>` 全绿
- [ ] `node <改动页目录>/smoke.test.js` SMOKE PASS
- [ ] `node _pipeline/accept.js <slug>` 输出 ACCEPT
- [ ] `node _pipeline/style-audit.js` 全绿（改色板/返回链接/自动游览时必查）
- [ ] 未引入任何本机绝对路径（`C:\...`、`/Users/...`）
