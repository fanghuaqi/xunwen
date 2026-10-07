#!/usr/bin/env node
/* update-gallery.js —— 依据 queue.json + manifest.json 重新生成总画廊 index.html */
'use strict';
const fs = require('fs');
const path = require('path');
const BASE = path.resolve(__dirname, '..');
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, 'queue.json'), 'utf8'));
const manifest = JSON.parse(fs.readFileSync(path.join(__dirname, 'manifest.json'), 'utf8'));

const LEGACY = [
  { slug: 'jingyesi', title: '静夜思', author: '李白', dynasty: '唐', track: '水墨夜思', accent: '#c9d3e0', hook: '月光如练穿窗而入，霜华满地；举头是月，低头是千里故乡的灯火。' },
  { slug: 'jiangxue', title: '江雪', author: '柳宗元', dynasty: '唐', track: '宣纸留白', accent: '#2c2f33', hook: '天地皆白的宣纸上，千山鸟绝、万径踪灭，唯有一舟一翁，一点墨。' },
  { slug: 'chunxiao', title: '春晓', author: '孟浩然', dynasty: '唐', track: '青绿春晓·晨光', accent: '#9fce8f', hook: '夜来风雨声里酣眠，醒来满树花团、落瓣成毯——花落知多少。' },
  { slug: 'youziyin', title: '游子吟', author: '孟郊', dynasty: '唐', track: '宣纸暖烛', accent: '#c9a06a', hook: '油灯下一针一线密密缝，那根线走出柴门，在原野上化作三春晖。' },
  { slug: 'shuidiao-getou', title: '水调歌头', author: '苏轼', dynasty: '宋', track: '夜宴金彩·天界', accent: '#d9c98a', hook: '把酒问青天，乘风归去——云上琼楼玉宇，高处不胜寒；千里共婵娟。' },
  { slug: 'guancanghai', title: '观沧海', author: '曹操', dynasty: '汉魏', track: '大漠金戈·沧海', accent: '#d98e3a', hook: '碣石临海，洪波涌起；日月沉浮于海中，银河倒卷入其里。' },
  { slug: 'guanju', title: '关雎', author: '诗经·周南', dynasty: '先秦', track: '青绿·水泽', accent: '#8fb89a', hook: '河洲之上雎鸠和鸣，荇菜左右流之；辗转反侧，终以钟鼓乐之。' },
  { slug: 'shengshengman', title: '声声慢', author: '李清照', dynasty: '宋', track: '烟雨江南', accent: '#8fb3c9', hook: '寻寻觅觅，冷冷清清；梧桐细雨点点滴滴到黄昏，怎一个愁字了得。' },
  { slug: 'jiangjinjiu', title: '将进酒', author: '李白', dynasty: '唐', track: '夜宴金彩', accent: '#d4af37', hook: '黄河之水天上来；三百金杯列如星河，与尔同销万古愁。' },
];
const legacyCard = p => `  <a class="card" style="--ac:${p.accent}" href="${p.slug}/index.html">
    <div class="name">${p.title}</div><div class="author">${p.dynasty} · ${p.author}</div>
    <div class="track">${p.track}</div>
    <div class="jing">${p.hook}</div>
    <div class="meta">点击画面有互动</div>
  </a>`;

/* 回填约定：旧引擎页回填后会以同 slug 进 queue.json（供 accept.js 验收），
   但画廊仍以 LEGACY 卡（手写 hook）为准——queue 里与 LEGACY 同名的不再出第二张卡 */
const legacySlugs = new Set(LEGACY.map(p => p.slug));
const qPoems = queue.poems.filter(p => !legacySlugs.has(p.slug));
const done = qPoems.filter(p => manifest[p.slug] && manifest[p.slug].status === 'done');
const building = qPoems.filter(p => manifest[p.slug] && manifest[p.slug].status === 'building');
const queuedN = qPoems.length - done.length - building.length;

const card = p => `  <a class="card" style="--ac:${p.accent}" href="${p.slug}/index.html">
    <div class="name">${p.title}</div><div class="author">${p.dynasty} · ${p.author}</div>
    <div class="track">${queue.tracks[p.track].name}</div>
    <div class="jing">${p.stages[0]}</div>
    <div class="meta">${p.stages.length}境 · 点击画面有互动</div>
  </a>`;

/* 内联 SVG favicon（金月黛山·诗境）：data-URI 零文件，file:// 直开可用 */
const FAVICON = 'data:image/svg+xml,' + encodeURIComponent(`<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='#0a0d13'/><circle cx='41' cy='21' r='10' fill='#d4af37'/><path d='M4 53 L19 31 L31 45 L40 36 L60 53 Z' fill='#253044'/><path d='M14 58 q5 -4 10 0 t10 0 t10 0 t10 0' stroke='#56687f' stroke-width='3' fill='none' stroke-linecap='round'/></svg>`);

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="${FAVICON}">
<title>循文入境 · 古诗词沉浸式诗集</title>
<style>
:root{--bg:#0a0d13;--card:#11161f;--line:rgba(255,255,255,.09);--txt:#e8e4d8;--dim:#8d8672}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--txt);font-family:'Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;min-height:100vh;padding:6vh 6vw}
header{text-align:center;margin-bottom:5vh}
header h1{font-size:clamp(30px,5vw,46px);letter-spacing:.35em;font-weight:normal}
header .sub{color:var(--dim);letter-spacing:.5em;font-size:13px;margin-top:12px}
header .tip{color:var(--dim);font-size:12.5px;margin-top:18px;line-height:2;font-family:'Noto Serif SC','SimSun',serif}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;max-width:1200px;margin:0 auto}
a.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:22px 24px;text-decoration:none;color:var(--txt);transition:all .3s;position:relative;overflow:hidden}
a.card::before{content:'';position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--ac)}
a.card:hover{transform:translateY(-4px);border-color:var(--ac);box-shadow:0 10px 34px rgba(0,0,0,.45)}
.card .name{font-size:24px;letter-spacing:.2em;margin-bottom:4px}
.card .author{color:var(--dim);font-size:12.5px;letter-spacing:.25em;margin-bottom:12px}
.card .track{display:inline-block;font-size:11.5px;letter-spacing:.15em;color:var(--ac);border:1px solid var(--ac);border-radius:20px;padding:3px 12px;margin-bottom:12px;opacity:.9}
.card .jing{font-size:13.5px;color:#b5ad98;line-height:1.9;font-family:'Noto Serif SC','SimSun',serif}
.card .meta{margin-top:12px;color:var(--dim);font-size:11px;letter-spacing:.2em}
a.ext{opacity:.92}
.sister{margin-top:5vh;text-align:center;color:var(--dim);font-size:12.5px;letter-spacing:.2em;line-height:2.2}
.sister a{color:#d4af37;text-decoration:none;border-bottom:1px dashed rgba(212,175,55,.5)}
.progress{margin:0 auto 4vh;max-width:1200px;color:var(--dim);font-size:12px;letter-spacing:.2em;text-align:center;font-family:'Noto Serif SC',serif}
</style>
</head>
<body>
<header>
  <h1>循文入境 · 诗集</h1>
  <div class="sub">诗 句 到 哪 一 句 · 实 景 走 到 哪 一 境</div>
  <div class="tip">每首一个独立网页：逐句入画 · 逐字注音 · 释义注释 · AI 朗读 · 自动游览 · 结课小测<br>
  双击各页 index.html 打开 · 用 Microsoft Edge 体验最佳真人感朗诵 · 首次打开需联网加载三维引擎</div>
</header>
<div class="progress">已完成 ${LEGACY.length + done.length} 首 —— 六大画风：夜宴金彩 / 水墨夜思 / 宣纸留白 / 青绿春晓 / 大漠金戈 / 烟雨江南</div>
<div class="grid">
${LEGACY.map(legacyCard).concat(done.map(card)).join('\n')}
</div>
<div class="sister">
  由循文入境技能批量生成 · 每页独立可分发 · 制作进度见 <a href="_pipeline/manifest.json">manifest</a>
</div>
</body>
</html>
`;
fs.writeFileSync(path.join(BASE, 'index.html'), html);
console.log(`gallery: done=${LEGACY.length + done.length} building=${building.length} queued=${queuedN}`);
