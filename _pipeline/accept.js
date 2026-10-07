#!/usr/bin/env node
/*
 * accept.js —— 「循文入境」批量生产的确定性验收
 * 用法: node accept.js <slug>
 * 退出码 0 = ACCEPT；1 = REJECT（打印全部问题）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { execFileSync } = require('child_process');

const BASE = path.resolve(__dirname, '..');
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === process.argv[2]);
if (!entry) { console.error('queue.json 中无 ' + process.argv[2]); process.exit(1); }

const file = path.join(BASE, entry.slug, 'index.html');
const issues = [];
const N = entry.stages.length;
const track = queue.tracks[entry.track];

/* 0. validate.js */
try {
  execFileSync('node', [path.join(__dirname, 'tools', 'validate.js'), file], { stdio: 'pipe' });
} catch (e) {
  issues.push('validate.js 未通过: ' + String(e.stderr || e.message).slice(0, 300));
}

/* 1. vm 提取数据 */
const mk = n => class C { constructor(...a) { this.args = a; } };
const THREE = new Proxy({}, { get: (t, p) => (p === 'then' ? undefined : mk(String(p))) });
const el = () => ({ addEventListener() {}, classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } }, style: {}, textContent: '', innerHTML: '', appendChild() {}, querySelectorAll() { return []; } });
const sandbox = { THREE, window: {}, document: { querySelector: () => el(), createElement: () => el(), addEventListener() {}, documentElement: el(), body: el(), head: el(), activeElement: null, fullscreenElement: null }, performance: { now: () => 0 }, requestAnimationFrame() {}, console, setTimeout() { return 0; }, clearTimeout() {} };
sandbox.window.addEventListener = () => {};
let code = '', ok = false;
try {
  const html = fs.readFileSync(file, 'utf8');
  code = html;
  const m = html.match(/<script id="main">([\s\S]*?)<\/script>/);
  vm.createContext(sandbox);
  vm.runInContext(m[1], sandbox, { filename: file });
  ok = true;
} catch (e) { issues.push('主脚本执行失败: ' + e.message); }

if (ok) {
  const get = e => vm.runInContext(e, sandbox);
  const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ');

  /* 2. 诗文逐字 */
  const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
  if (joined !== entry.text) {
    issues.push(`诗文不一致!\n  期望: ${entry.text}\n  实际: ${joined}`);
  }
  if (POEM.length !== N) issues.push(`POEM ${POEM.length} 句 ≠ 清单 ${N} 句`);

  /* 3. 边界 */
  if (!code.includes(`clamp(i,0,${N})`)) issues.push(`goto 缺 clamp(i,0,${N})`);
  if (!new RegExp(`curIdx[>=]=*${N}\\)`).test(code) && !code.includes(`curIdx===${N})showEnding`) && !new RegExp(`curIdx>=${N}\\)?showEnding`).test(code)) {
    if (!new RegExp(`curIdx(?:>=|===)${N}\\)?\\s*\\)?\\s*showEnding`).test(code)) issues.push(`末境 showEnding 判断缺 ${N}`);
  }
  const fullNum = String(N + 1).padStart(2, '0');
  if (!code.includes(`'${fullNum}.mp3'`)) issues.push(`全诗音频 '${fullNum}.mp3' 未引用`);
  if (entry.interact) {
    const c = (code.match(new RegExp(`curIdx===${N}&&state==='stage'`, 'g')) || []).length;
    if (c < 2) issues.push(`交互境 curIdx===${N} 接线仅 ${c} 处（应 pointerdown+空格 ≥2）`);
  }

  /* 4. 残留（jiangjinjiu 本尊除外——这两条查的是其他页照搬《将进酒》模板的残留） */
  if (entry.slug !== 'jiangjinjiu' && (code.includes('将进酒') || code.includes('万古愁'))) issues.push('残留《将进酒》字样');
  if (entry.slug !== 'jiangjinjiu' && /如见太白|深得太白/.test(code)) issues.push('小测评语残留太白');

  /* 5. 色板（赛道不符=照搬默认） */
  const root = (code.match(/:root\s*\{[^}]*\}/) || [''])[0];
  const gm = (root.match(/--gold:\s*([^;\s]+)/) || [])[1];
  if (entry.track !== 'yanye') {
    if (!gm || gm.toLowerCase() === '#d4af37') issues.push('--gold 仍为默认金，未按赛道换肤');
  }
  if (entry.track !== 'yanye' && /background:#05070d/.test(code)) issues.push('body 背景仍为夜宴默认');
  if (entry.track !== 'yanye' && (code.match(/0x05070d/g) || []).length > 1) issues.push('0x05070d 出现 >1 次（makeWater 默认允许 1 次）');
  if (gm && gm.toLowerCase() !== entry.accent.toLowerCase()) issues.push(`--gold=${gm} ≠ 分配强调色 ${entry.accent}`);

  /* 6. 小测 */
  if (!Array.isArray(QUIZ) || QUIZ.length < 5) issues.push('小测不足 5 题');
  else QUIZ.forEach((q, i) => {
    if (!Array.isArray(q.o) || q.o.length !== 3) issues.push(`小测${i + 1}选项数≠3`);
    if (typeof q.a !== 'number' || q.a < 0 || q.a >= (q.o ? q.o.length : 0)) issues.push(`小测${i + 1}答案越界`);
  });

  /* 7. 音频 */
  const audioDir = path.join(path.dirname(file), 'audio');
  if (!fs.existsSync(audioDir)) issues.push('audio/ 不存在');
  else {
    const have = fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length;
    if (have !== N + 2) issues.push(`audio ${have} 个 ≠ ${N + 2}`);
  }
}

if (issues.length) {
  console.log(`REJECT ${entry.slug}`);
  issues.forEach((s, i) => console.log(`  ${i + 1}. ${s}`));
  process.exit(1);
}
console.log(`ACCEPT ${entry.slug}（${N}境 · ${track.name}）`);
