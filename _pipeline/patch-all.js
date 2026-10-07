#!/usr/bin/env node
/* patch-all.js —— 全部诗词页统一：默认自动游览 + 封面/终章返回诗集目录 */
'use strict';
const fs = require('fs');
const path = require('path');

const BASE = path.resolve(__dirname, '..');
const files = [];
for (const d of fs.readdirSync(BASE)) {
  const f = path.join(BASE, d, 'index.html');
  if (fs.existsSync(f)) files.push({ f, gal: '../index.html' });
}

const CSS = `.galLink{display:inline-block;font-family:var(--song);font-size:12.5px;letter-spacing:.25em;color:var(--dim);text-decoration:none;border:1px solid var(--line);border-radius:20px;padding:7px 18px;transition:all .3s}
.galLink:hover{color:var(--gold);border-color:var(--gold)}
#endBtns .galLink{align-self:center}
`;

let okCount = 0;
for (const { f, gal } of files) {
  let h = fs.readFileSync(f, 'utf8');
  const problems = [];
  const rep = (o, n, exp) => {
    const c = h.split(o).length - 1;
    if (c !== exp) { problems.push(`匹配 ${c}≠${exp}: ${o.slice(0, 50)}`); return; }
    h = h.split(o).join(n);
  };
  // 1. 默认自动游览
  rep('autoMode=false', 'autoMode=true', 1);
  rep('<button id="btnAuto">自动游览 · 关</button>', '<button id="btnAuto" class="on">自动游览 · 开</button>', 1);
  // 2. 封面返回诗集
  rep('<button id="enterBtn">入 境</button>',
    `<button id="enterBtn">入 境</button>\n      <div style="margin-top:20px"><a class="galLink" href="${gal}">← 返回诗集目录</a></div>`, 1);
  // 3. 终章返回诗集
  rep('<button id="btnCover">回到封面</button>',
    `<button id="btnCover">回到封面</button>\n      <a class="galLink" href="${gal}" style="align-self:center">诗集目录</a>`, 1);
  // 4. CSS
  const si = h.indexOf('</style>');
  if (si === -1) problems.push('未找到 </style>');
  else h = h.slice(0, si) + CSS + h.slice(si);

  if (problems.length) {
    console.log(`✗ ${path.basename(path.dirname(f))}: ${problems.join(' | ')}`);
    continue;
  }
  fs.writeFileSync(f, h);
  okCount++;
}
console.log(`patched ${okCount}/${files.length}`);
if (okCount !== files.length) process.exit(1);
