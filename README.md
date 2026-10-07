# 循文入境 · 中国古诗词沉浸式课堂

> 「循文入境」：诗句推进到哪一句，三维实景就走到哪一重意境 —— 学生边读诗，边"走进"诗里。
> **270 首**古典诗词，每首一个单文件网页：Three.js 三维诗境 + 逐字注音 + 释义注释 + AI 朗读 + 自动游览 + 结课小测。双击即开，无需安装。

🌐 **在线体验**：**[fanghuaqi.github.io/xunwen](https://fanghuaqi.github.io/xunwen/)** | [English](#english) | 许可证：[CC BY-NC-SA 4.0](LICENSE)（免费教学 · 非商业 · 署名-相同方式共享）

---

## ✨ 特性

- **循文入境**：一句一境，镜头随诗句推进（如《将进酒》十三境从"黄河之水天上来"走到"与尔同销万古愁"）
- **三维实景**：Three.js r128（UMD，CDN 三路回退），自研"造型工坊"原语库 —— 唐装人物、器型剖面、有形状的火焰、多峰山脊、临边昏暗的月亮……
- **教学四件套**：逐字注音（拼音数=汉字数）、白话释义、考点注释（多音字/典故）、结课小测（5 题）
- **AI 朗读**：Edge 神经语音现场朗诵（免费无密钥，按风格赛道自动选声），内置 MP3 兜底
- **课堂友好**：自动游览 + 自动朗读默认开启，可作大屏无人值守展示；每首诗带深度冒烟测试
- **六大风格赛道**：夜宴金彩 / 水墨夜思 / 宣纸留白 / 青绿春晓 / 大漠金戈 / 烟雨江南 —— 每首诗专属配色、粒子母题与一个"标志性瞬间"，拒绝千诗一面

## 🚀 快速开始

无需构建、无需依赖：

```bash
# 方式一：直接双击
#   打开 index.html（诗集目录）→ 点任意一首 → 点「入境」

# 方式二：本地静态服务（推荐，音频加载更稳）
python -m http.server 8080
# 浏览器打开 http://localhost:8080
```

- 页面单文件自包含；Three.js 从 CDN 加载（首次打开需联网），音频在本地 `audio/`
- `← →` / 空格键逐境游览；部分诗境可点击画面触发交互（碰杯、点亮灯火、召乌鹊归山……）

## 📂 目录结构

```
chinese-poetry-xunwen/
├── index.html              # 诗集目录（270 张卡片）
├── <slug>/                 # 每首诗一个目录，如 duange-xing/（短歌行）
│   ├── index.html          # 单文件沉浸式课件
│   ├── audio/              # AI 朗读 MP3（00 题名、01..N 各境、N+1 全篇）
│   ├── tts.json            # 本诗多音字朗读配置（只影响读音）
│   ├── README.md           # 境表 / 操作 / 教学建议
│   └── smoke.test.js       # 结构冒烟测试（node smoke.test.js）
├── _pipeline/              # 批量生产与验收管线（贡献者工具）
│   ├── tools/              # validate.js 结构校验、gen-voice-edge.py 神经语音配音
│   ├── vendor/             # three.min.js r128（供本地冒烟测试）
│   ├── accept.js           # 确定性验收（诗文逐字比对 + 边界常量 + 色板 + 音频数）
│   ├── mark-done.js        # 验收并登记 manifest
│   ├── update-gallery.js   # 重建诗集目录
│   ├── style-audit.js      # 全集风格一致性审查
│   ├── shots.py            # 无头 Chrome 逐境实拍截图（视觉验收）
│   └── _dgx/               # 「骨架变换」建页管线（build.py + 每诗配置）
├── docs/                   # 引擎架构 / 美术方向 / 场景库（贡献者必读）
└── LICENSE                 # CC BY-NC-SA 4.0
```

## 🛠 技术要点

- **零构建**：每首诗是一个 HTML 文件，内联全部场景代码；改完刷新即见
- **Three.js r128 UMD**：cdnjs → jsdelivr → unpkg 三路回退，保证 file:// 直开可用
- **引擎硬约束**（详见 [docs/architecture.md](docs/architecture.md)）：主脚本顶层禁止引用 THREE、STAGES 与 POEM 严格对齐、每帧写 opacity/intensity 必乘 fadeK、透明物 renderOrder 分层、雾密度预算……每条都是真实踩过的坑
- **确定性验收**：`accept.js` 以 queue.json 为唯一口径逐字比对诗文、校验边界常量与色板，杜绝"改诗改错格"

## ➕ 新增一首诗

见 [CONTRIBUTING.md](CONTRIBUTING.md)。简言之：在 `_pipeline/queue.json` 登记条目 → 用 `_pipeline/_dgx/build.py` 骨架变换建页 → 过 `validate.js` → 冒烟 → `gen-voice-edge.py` 配音 → `accept.js` 验收。管线会把"数量联动/色板/残留"这类易错点全部拦下。

## 🤝 贡献

欢迎一切贡献：**纠错**（注音/释义/错字）、**体验改进**、**新增诗作**、**新风格赛道**。请先读 [CONTRIBUTING.md](CONTRIBUTING.md)；提交 PR 前请跑通该诗的 `smoke.test.js` 与 `_pipeline/accept.js`。

## 📜 许可证与第三方组件

本项目采用 [**CC BY-NC-SA 4.0**（署名-非商业性使用-相同方式共享 4.0 国际）](LICENSE)：

- ✅ 免费用于**教学**与个人学习；欢迎分享、改编、二次创作（需署名并以相同协议共享）
- ✅ 欢迎贡献代码与内容（贡献即同意以相同协议释出）
- ❌ **未经作者事先许可，不得用于商业用途**（商业授权请联系作者，可通过 GitHub Issue 留言）

第三方组件致谢：

| 组件 | 用途 | 许可 |
|---|---|---|
| [Three.js r128](https://github.com/mrdoob/three.js) | 三维渲染（CDN 运行时加载） | MIT |
| [Microsoft Edge 神经语音](https://www.microsoft.com/) | AI 朗读（`audio/` 由 edge-tts 生成） | 仅供学习交流，版权归原作者 |
| [Google Fonts：马善政 / 思源宋体](https://fonts.google.com/) | 页面字体（CDN 运行时加载） | SIL OFL |
| [chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry) | 诗文校对参考语料（古本，页面一律从现行教材本字） | 其自身许可 |
| [edge-tts](https://github.com/rany2/edge-tts) | 配音生成工具（Python 依赖） | GPL-3.0（仅生成工具，产物不受影响） |

> 诗词原文以现行中小学教材用字为准；注释与释义参考通行教材与权威注本。

## English

**Xunwen Rujing** ("Following the Text into the Scene") is a collection of **270 immersive, single-file web lessons** for classical Chinese poetry. Each poem unfolds scene by scene in 3D (Three.js r128) as the verses advance, with per-character pinyin annotation, plain-language explanations, exam-oriented notes, AI voice recitation (Edge Neural TTS), auto-tour mode, and a 5-question quiz. Try it live at **[fanghuaqi.github.io/xunwen](https://fanghuaqi.github.io/xunwen/)**, or open `index.html` directly — no build step, no dependencies.

Licensed under [CC BY-NC-SA 4.0](LICENSE): free for **educational and personal use** with attribution and share-alike; **commercial use requires prior permission** from the author. Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
