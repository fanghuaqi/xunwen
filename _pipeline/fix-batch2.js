#!/usr/bin/env node
/* fix-batch2.js —— 第二批 14 页补"自动游览默认开+返回诗集链接"；3 页色板偏差修正 */
'use strict';
const fs = require('fs');
const path = require('path');
const BASE = path.resolve(__dirname, '..');

const CSS = `.galLink{display:inline-block;font-family:var(--song);font-size:12.5px;letter-spacing:.25em;color:var(--dim);text-decoration:none;border:1px solid var(--line);border-radius:20px;padding:7px 18px;transition:all .3s}
.galLink:hover{color:var(--gold);border-color:var(--gold)}
#endBtns .galLink{align-self:center}
`;
const SECOND = ['chishang', 'chunwang', 'dengyouzhoutai', 'guyuancao', 'huanghelou', 'qiuci',
  'songdushaofu', 'suojiandejiang', 'wangdongting', 'wangyue', 'wenliushijiu', 'wuyixiang',
  'xiangsi', 'zashi-junzigu'];

let ok = 0;
for (const slug of SECOND) {
  const f = path.join(BASE, slug, 'index.html');
  let h = fs.readFileSync(f, 'utf8');
  const problems = [];
  const rep = (o, n, exp) => {
    const c = h.split(o).length - 1;
    if (c !== exp) { problems.push(`匹配 ${c}≠${exp}: ${o.slice(0, 40)}`); return; }
    h = h.split(o).join(n);
  };
  if (!/autoMode=true/.test(h)) rep('autoMode=false', 'autoMode=true', 1);
  if (h.includes('<button id="btnAuto">自动游览 · 关</button>')) rep('<button id="btnAuto">自动游览 · 关</button>', '<button id="btnAuto" class="on">自动游览 · 开</button>', 1);

  rep('<button id="enterBtn">入 境</button>',
    '<button id="enterBtn">入 境</button>\n      <div style="margin-top:20px"><a class="galLink" href="../index.html">← 返回诗集目录</a></div>', 1);
  rep('<button id="btnCover">回到封面</button>',
    '<button id="btnCover">回到封面</button>\n      <a class="galLink" href="../index.html" style="align-self:center">诗集目录</a>', 1);
  if (!h.includes('.galLink')) {
    const si = h.indexOf('</style>');
    if (si === -1) problems.push('无 </style>'); else h = h.slice(0, si) + CSS + h.slice(si);
  }
  if (problems.length) { console.log(`✗ ${slug}: ${problems.join(' | ')}`); continue; }
  fs.writeFileSync(f, h);
  ok++;
}
console.log(`功能补丁 ${ok}/${SECOND.length}`);

/* 色板偏差修正 */
const fixes = [
  ['chunxiao', 'uBot:{value:C(0x05070d)}', 'uBot:{value:C(0x081009)}', 1],
  ['furonglou-song', 'background:#0a0f16', 'background:#10141a', 2],
  ['tianjingsha-qiusi', 'background:#100d16', 'background:#10141a', 2],
];
for (const [slug, o, n, exp] of fixes) {
  const f = path.join(BASE, slug, 'index.html');
  let h = fs.readFileSync(f, 'utf8');
  const c = h.split(o).length - 1;
  if (c !== exp) { console.log(`✗ ${slug} 色板锚点 ${c}≠${exp}`); continue; }
  h = h.split(o).join(n);
  fs.writeFileSync(f, h);
  console.log(`色板修正 ${slug}`);
}
