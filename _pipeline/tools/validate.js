#!/usr/bin/env node
/*
 * validate.js —— 「循文入境」网页结构校验器
 * 用法: node validate.js [index.html 路径]    （默认 ./index.html）
 *
 * 检查项:
 *  1. 主脚本可编译（语法）
 *  2. 顶层可在 THREE 未加载时安全执行（THREE 桩执行）——抓"顶层引用 THREE"/TDZ 崩溃
 *  3. STAGES 数 = POEM 数 + 1（封面），且 STAGES[i].name === POEM[i-1].name
 *  4. 每境 cam(f/t/lf/lt)/sky 工厂/dwell/river/build 齐全
 *  5. 每句 read/yisi/zhu/jing/segs 齐全；汉字数 === 拼音数
 *  6. read 字段数 === 诗句数；CN 数字数组够长
 *  7. audio/ 文件数（存在则检查，不足仅警告）
 *
 * 退出码: 0 全绿；1 有错误。任何结构性修改后必须重跑本脚本。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const file = process.argv[2] || 'index.html';
if (!fs.existsSync(file)) { console.error('✗ 找不到文件: ' + file); process.exit(1); }
const html = fs.readFileSync(file, 'utf8');
const errors = [], warns = [];
const err = m => errors.push(m);
const warn = m => warns.push(m);

/* 1. 提取主脚本 */
const m = html.match(/<script id="main">([\s\S]*?)<\/script>/);
if (!m) { console.error('✗ 未找到 <script id="main">（主脚本必须带此 id）'); process.exit(1); }
const code = m[1];

/* 2. 语法编译 */
try { new vm.Script(code, { filename: file }); }
catch (e) { err('语法错误: ' + e.message); }

/* 3. 两遍执行：
 *   Pass A —— sandbox 不含 THREE（模拟引擎未加载）：顶层若引用 THREE/未守卫的引擎对象 → 报错
 *   Pass B —— sandbox 含 THREE 桩：放行顶层，供后续数据检查
 */
const mk = n => class C { constructor(...a) { this._n = n; this.args = a; } };
const THREE = new Proxy({}, { get: (t, p) => (p === 'then' ? undefined : mk(String(p))) });
const elStub = () => ({
  addEventListener() {}, classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
  style: {}, textContent: '', innerHTML: '', appendChild() {}, querySelectorAll() { return []; }, open: false,
});
const baseStubs = {
  window: {},
  document: { querySelector: () => elStub(), createElement: () => elStub(), addEventListener() {}, documentElement: elStub(), body: elStub(), head: elStub(), activeElement: null, fullscreenElement: null },
  performance: { now: () => 0 }, requestAnimationFrame() {}, console,
  setTimeout() { return 0; }, clearTimeout() {}, location: { reload() {} },
};
baseStubs.window.addEventListener = () => {};

// Pass A: 无 THREE
try {
  const sA = Object.assign({}, baseStubs);
  vm.createContext(sA);
  vm.runInContext(code, sA, { filename: file + ' (passA: no THREE)' });
} catch (e) {
  err('顶层在引擎未加载时执行了引擎代码（THREE 未定义等）: ' + e.message + ' —— 顶层禁止出现 THREE 求值，请改为惰性工厂/boot() 内创建');
}

// Pass B: 含 THREE 桩
let ran = false, sandbox = null;
try {
  sandbox = Object.assign({ THREE }, baseStubs);
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox, { filename: file });
  ran = true;
} catch (e) {
  err('顶层执行失败（TDZ 等）: ' + e.message);
}

/* 4. 数据完整性 */
if (ran) {
  const get = expr => vm.runInContext(expr, sandbox, { filename: file });
  const stages = get('STAGES'), poem = get('POEM'), cn = get('CN');
  if (!Array.isArray(stages) || !Array.isArray(poem)) {
    err('未找到 STAGES/POEM 数组');
  } else {
    if (stages.length !== poem.length + 1) err(`STAGES(${stages.length}) 应比 POEM(${poem.length}) 恰好多 1（封面）`);
    const s0 = stages[0] || {};
    if (!(s0.name === '卷首' || s0.name === '封面' || s0.key === 'cover')) warn('STAGES[0] 应为封面境（name=卷首/封面 或 key=cover），当前: ' + (s0.name || '(空)'));
    for (let i = 1; i < stages.length; i++) {
      const s = stages[i], p = poem[i - 1];
      const tag = `境${i} (${(s && s.name) || '?'})`;
      if (!s.name || !p || !p.name) err(`${tag}: STAGES/POEM 缺 name 或数量错位`);
      else if (s.name !== p.name) err(`${tag}: 境名错位 STAGES="${s.name}" ≠ POEM="${p.name}"`);
      if (typeof s.build !== 'function') err(`${tag}: 缺 build`);
      if (!s.cam || !s.cam.f || !s.cam.t || !s.cam.lf || !s.cam.lt) err(`${tag}: cam 缺 f/t/lf/lt`);
      if (typeof s.dwell !== 'number' || typeof s.river !== 'number') err(`${tag}: 缺 dwell/river`);
      if (typeof s.sky !== 'function') err(`${tag}: sky 必须是惰性工厂 ()=>SK({...})（顶层禁止求值 THREE）`);
      else {
        try {
          const k = s.sky();
          if (!k.top || !k.hor || !k.fog || typeof k.fd !== 'number' || !k.moon) err(`${tag}: sky() 返回字段不全`);
        } catch (e) { err(`${tag}: sky() 抛错: ${e.message}`); }
      }
    }
    if (Array.isArray(cn) && cn.length < poem.length) err(`CN 数字数组(${cn.length}) 少于诗句数(${poem.length})`);
    poem.forEach((p, idx) => {
      const n = idx + 1, tag = `第${n}句 (${p.name || '?'})`;
      if (!p.name) err(`${tag}: 缺 name`);
      if (!p.read) err(`${tag}: 缺 read（朗读文本）`);
      if (!p.yisi) err(`${tag}: 缺 yisi（释义）`);
      if (!Array.isArray(p.zhu) || !p.zhu.length) err(`${tag}: 缺 zhu（注释）`);
      if (!p.jing) err(`${tag}: 缺 jing（意境题句）`);
      if (!Array.isArray(p.segs) || !p.segs.length) err(`${tag}: 缺 segs`);
      else p.segs.forEach(seg => {
        const han = [...seg.c].filter(c => !/[，。、！？；：…—·]/.test(c)).length;
        if (!Array.isArray(seg.p)) err(`${tag} "${seg.c.slice(0, 12)}": 缺拼音数组 p`);
        else if (han !== seg.p.length) err(`${tag} "${seg.c.slice(0, 12)}": 汉字 ${han} ≠ 拼音 ${seg.p.length}`);
      });
    });
    const reads = (code.match(/read:'/g) || []).length;
    if (reads !== poem.length) err(`read 字段数(${reads}) ≠ 诗句数(${poem.length})`);
    // 小测评语数组长度必须 = 题数+1（qScore 可取 0..题数）
    const wq = code.match(/words\s*=\s*\[([^\]]*)\]/);
    if (wq) {
      const wn = wq[1].split(',').length;
      const qn = get('QUIZ.length');
      if (wn !== qn + 1) err(`小测评语 words 数组(${wn} 项)应为 题数+1=${qn + 1} 项，且评语需按本诗定制（勿照抄参考实现）`);
    }
    const quizN = (code.match(/QUIZ\s*=/g) || []).length;
    if (!quizN) warn('未找到 QUIZ 小测数据');
  }
}

/* 4.5 防同质化提醒：色板原样照搬参考实现 */
const rootCss = (html.match(/:root\s*\{[^}]*\}/) || [''])[0];
if (rootCss.includes('--gold:#d4af37') && /background:#05070d/.test(html))
  warn('色板与参考实现完全一致（夜宴金彩）——请按 references/art-direction.md 选风格赛道换配色；若该诗确属此赛道可忽略');

/* 5. 音频目录（存在才检查） */
if (ran) {
  const audioDir = path.join(path.dirname(path.resolve(file)), 'audio');
  if (fs.existsSync(audioDir)) {
    const have = fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length;
    const need = Number(vm.runInContext('POEM.length', sandbox)) + 2;
    if (have < need) warn(`audio/ 有 ${have} 个 MP3，少于 诗句数+2=${need}（00 标题 + 全诗）——运行 gen-voice.js 补齐`);
  } else {
    warn('无 audio/ 目录——运行 gen-voice.js 生成 AI 配音（否则回退浏览器语音）');
  }
}

/* 汇总 */
warns.forEach(w => console.log('⚠ ' + w));
if (errors.length) {
  errors.forEach(e => console.error('✗ ' + e));
  console.error(`\n共 ${errors.length} 个错误，请修复后重跑`);
  process.exit(1);
}
console.log('✓ 校验全部通过');
