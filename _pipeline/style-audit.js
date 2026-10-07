#!/usr/bin/env node
/* style-audit.js —— 全集风格审查：赛道色板/默认色残留/返回链接/自动游览 */
'use strict';
const fs = require('fs');
const path = require('path');
const BASE = path.resolve(__dirname, '..');
const queue = JSON.parse(fs.readFileSync(path.join(BASE, '_pipeline/queue.json'), 'utf8'));
const tracks = queue.tracks;

/* 8 首首批 + 将进酒 的既定赛道/强调色 */
const LEGACY = {
  jingyesi: { name: '水墨夜思', track: 'shuimo', gold: '#c9d3e0', bg: '#0d1117' },
  jiangxue: { name: '宣纸留白', track: 'xuanzhi', gold: '#2c2f33', bg: '#e9e2d0' },
  chunxiao: { name: '青绿春晓', track: 'qinglv', gold: '#9fce8f', bg: '#0a1410' },
  youziyin: { name: '宣纸暖烛', track: 'xuanzhi', gold: '#c9a06a', bg: '#efe4c8' },
  'shuidiao-getou': { name: '夜宴金彩·天界', track: 'yanye', gold: '#d9c98a', bg: '#05070d' },
  guancanghai: { name: '大漠金戈·沧海', track: 'damo', gold: '#d98e3a', bg: '#120d08' },
  guanju: { name: '青绿·水泽', track: 'qinglv', gold: '#8fb89a', bg: '#0c1714' },
  shengshengman: { name: '烟雨江南', track: 'yanyu', gold: '#8fb3c9', bg: '#10141a' },
  jiangjinjiu: { name: '夜宴金彩', track: 'yanye', gold: '#d4af37', bg: '#05070d' },
  youziyin: { name: '宣纸暖烛', track: 'xuanzhi', gold: '#8a5a2a', bg: '#efe6d0' },
  'shuidiao-getou': { name: '夜宴金彩·天界', track: 'yanye', gold: '#d9c98a', bg: '#070b13' },
  'min-nong': { name: '宣纸烈日', track: 'xuanzhi', gold: '#8a5a2a', bg: '#efe4c8' },
  'mujiang-yin': { name: '夜宴金彩·残阳', track: 'yanye', gold: '#d9b06a', bg: '#120d08' },
  wangdongting: { name: '夜宴金彩·白银盘', track: 'yanye', gold: '#d9c98a', bg: '#120d06' },
  wenliushijiu: { name: '夜宴金彩·红泥炉', track: 'yanye', gold: '#e0b060', bg: '#120d06' },
  'you-shanxicun': { name: '夜宴金彩·村宴', track: 'yanye', gold: '#d9c98a', bg: '#120d08' },
  yuanri: { name: '夜宴金彩·新春', track: 'yanye', gold: '#d4b050', bg: '#120d06' },
  hanshi: { name: '夜宴金彩·寒食', track: 'yanye', gold: '#d4b050', bg: '#120d06' },
  zenghuaqing: { name: '夜宴金彩·花卿', track: 'yanye', gold: '#e0c060', bg: '#120d06' },
  'qingyu-an-yuanxi': { name: '夜宴金彩·元夕', track: 'yanye', gold: '#e0a860', bg: '#070a10' },
  'mengyou-tianmu': { name: '夜宴金彩·梦游', track: 'yanye', gold: '#d9a8c0', bg: '#080614' },
};

const pages = fs.readdirSync(BASE).filter(d => {
  const p = path.join(BASE, d, 'index.html');
  return d !== '_pipeline' && fs.existsSync(p);
});

const issues = [];
let audited = 0;
for (const slug of pages) {
  const f = path.join(BASE, slug, 'index.html');
  const h = fs.readFileSync(f, 'utf8');
  const root = (h.match(/:root\s*\{[^}]*\}/) || [''])[0];
  let gold = (root.match(/--gold:\s*([^;\s]+)/) || [])[1] || '';
  const silver = (root.match(/--silver:\s*([^;\s]+)/) || [])[1] || '';
  if (!gold && silver) gold = silver;
  const bgm = h.match(/background:(#[0-9a-fA-F]{6})/) || [];
  const bg = bgm[1] || '';
  const probs = [];
  const isJJ = slug === 'jiangjinjiu';
  const meta = isJJ ? LEGACY.jiangjinjiu
    : LEGACY[slug] ? LEGACY[slug]
    : (() => { const q = queue.poems.find(p => p.slug === slug); return q ? { name: tracks[q.track].name, track: q.track, gold: q.accent, bg: tracks[q.track].bg } : null; })();

  if (!meta) { probs.push('不在队列且非首批（来源不明）'); }
  else if (meta.track !== 'yanye') {
    if (gold.toLowerCase() !== meta.gold.toLowerCase()) probs.push(`--gold=${gold} ≠ 应为 ${meta.gold}`);
    if (bg && meta.bg && bg.toLowerCase() !== meta.bg.toLowerCase()) probs.push(`bg=${bg} ≠ 应为 ${meta.bg}`);
    const nightLeft = (h.match(/0x05070d/g) || []).length;
    if (nightLeft > 1) probs.push(`0x05070d 出现 ${nightLeft} 次（makeWater 默认 1 次为限）`);
    if (h.includes('#d4af37')) probs.push('默认金 #d4af37 残留');
  } else if (meta.bg && bg && bg.toLowerCase() !== meta.bg.toLowerCase()) {
    probs.push(`bg=${bg} ≠ 夜宴基线 ${meta.bg}`);
  }
  /* 通用项：自动游览默认开 + 两处返回链接 */
  if (!/autoMode=true/.test(h)) probs.push('自动游览非默认开启');
  const gal = (h.match(/诗集目录/g) || []).length;
  if (gal < 2) probs.push(`返回诗集链接仅 ${gal} 处（应 ≥2）`);
  /* 残留他诗字样 */
  if (!isJJ && (h.includes('将进酒') || h.includes('万古愁'))) probs.push('残留《将进酒》字样');

  if (probs.length) issues.push(`${slug}（${meta ? meta.name : '?'}）: ${probs.join('；')}`);
  audited++;
}

console.log(`已审查 ${audited} 页`);
if (issues.length) {
  console.log(`\n✗ ${issues.length} 页存在问题：`);
  issues.forEach(s => console.log('  ' + s));
  process.exit(1);
}
console.log('✓ 全部页面风格与功能配置一致');
