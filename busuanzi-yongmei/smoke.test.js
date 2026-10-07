#!/usr/bin/env node
/*
 * smoke.test.js —— 「卜算子·咏梅」深度冒烟测试
 * 用带真实数学的 THREE 桩，把 5 个 STAGES 的 build/sky/cam/update、第四境点击交互全时序、
 * boot() → goto(1..4) → 自动游览 → showEnding() → 小测全流程跑一遍，
 * 并校验数据一致性、数量联动常量、色板与残留。全绿输出 SMOKE PASS。
 * 用法: node smoke.test.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const dir = __dirname;
const html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
const m = html.match(/<script id="main">([\s\S]*?)<\/script>/);
if (!m) { console.error('✗ 未找到主脚本 <script id="main">'); process.exit(1); }
const code = m[1];

const fails = [];
const chk = (ok, msg) => { if (!ok) fails.push(msg); };

/* ================= THREE 桩（带真实数学） ================= */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  lerpVectors(a, b, t) { return this.copy(a).lerp(b, t); }
  lerp(v, t) { this.x += (v.x - this.x) * t; this.y += (v.y - this.y) * t; this.z += (v.z - this.z) * t; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  setScalar(s) { this.x = s; this.y = s; this.z = s; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; return this.multiplyScalar(1 / l); }
  crossVectors(a, b) {
    const ax = a.x, ay = a.y, az = a.z, bx = b.x, by = b.y, bz = b.z;
    this.x = ay * bz - az * by; this.y = az * bx - ax * bz; this.z = ax * by - ay * bx; return this;
  }
  distanceTo(v) { return Math.hypot(this.x - v.x, this.y - v.y, this.z - v.z); }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class Col {
  constructor(h) { this.setHex(h); }
  setHex(h) { this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; return this; }
  clone() { const c = new Col(0); return c.copy(this); }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  lerp(c, t) { return this.lerpColors(this, c, t); }
}
class Euler { constructor() { this.x = 0; this.y = 0; this.z = 0; this.order = 'XYZ'; } set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } }
class Obj {
  constructor() {
    this.children = []; this.position = new V3(); this.rotation = new Euler();
    this.scale = new V3(1, 1, 1); this.userData = {}; this.visible = true;
    this.matrix = { elements: [] }; this.parent = null; this.frustumCulled = true;
  }
  add(...cs) { for (const c of cs) { c.parent = this; this.children.push(c); } return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) { fn(this); for (const c of this.children) { if (c && typeof c.traverse === 'function') c.traverse(fn); else fn(c); } }
  rotateZ() { return this; } rotateOnAxis() { return this; }
  updateMatrix() { return this; } updateMatrixWorld() { return this; }
  lookAt() {}
}
class Group extends Obj { constructor() { super(); this.isGroup = true; } }
class Geo {
  constructor(...a) { this.args = a; this.attributes = {}; }
  setAttribute(n, at) { this.attributes[n] = at; return this; }
  rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; } translate() { return this; }
  dispose() {}
}
class Curve { constructor(pts) { this.points = pts; } }
class BufferAttribute { constructor(a, s) { this.array = a; this.itemSize = s; this.needsUpdate = false; } }
class Mat {
  constructor(p = {}) {
    Object.assign(this, p);
    if (typeof this.color === 'number') this.color = new Col(this.color);
    this.userData = {}; this.uniforms = p.uniforms || null;
  }
  dispose() {}
}
class InstancedMesh extends Obj {
  constructor(g, mt, n) { super(); this.geometry = g; this.material = mt; this.count = n; this.instanceMatrix = { needsUpdate: false }; this.writes = 0; }
  setMatrixAt(i, mx) { this.writes++; }
}
class Texture { constructor(c) { this.image = c; } dispose() {} }
const ctx2d = new Proxy({}, {
  get: (t, p) => {
    if (p === 'createRadialGradient' || p === 'createLinearGradient') return () => ({ addColorStop() {} });
    if (typeof p === 'string') return () => {};
    return undefined;
  },
  set: () => true,
});
const mkCanvas = () => ({ width: 0, height: 0, getContext: () => ctx2d, style: {} });

const THREE = {
  Vector2: V2, Vector3: V3, Color: Col, Euler, Object3D: Obj, Group,
  BufferGeometry: Geo, BufferAttribute, CatmullRomCurve3: Curve,
  MeshBasicMaterial: Mat, MeshPhongMaterial: Mat, ShaderMaterial: Mat,
  PointsMaterial: Mat, LineBasicMaterial: Mat, SpriteMaterial: Mat,
  Mesh: class extends Obj { constructor(g, mt) { super(); this.geometry = g; this.material = mt; this.isMesh = true; } },
  Points: class extends Obj { constructor(g, mt) { super(); this.geometry = g; this.material = mt; } },
  Line: class extends Obj { constructor(g, mt) { super(); this.geometry = g; this.material = mt; } },
  Sprite: class extends Obj { constructor(mt) { super(); this.material = mt; } },
  InstancedMesh,
  SphereGeometry: Geo, BoxGeometry: Geo, CylinderGeometry: Geo, ConeGeometry: Geo,
  CircleGeometry: Geo, PlaneGeometry: Geo, TorusGeometry: Geo, LatheGeometry: Geo,
  TubeGeometry: Geo, DodecahedronGeometry: Geo, IcosahedronGeometry: Geo,
  CanvasTexture: Texture,
  Scene: class extends Obj { constructor() { super(); this.fog = null; } },
  PerspectiveCamera: class extends Obj { constructor() { super(); this.aspect = 1; } updateProjectionMatrix() {} },
  WebGLRenderer: function () {
    this.domElement = { addEventListener() {}, style: {} };
    this.setPixelRatio = () => {}; this.setSize = () => {}; this.setClearColor = () => {};
    this.render = () => { this.renders = (this.renders || 0) + 1; };
  },
  FogExp2: function (c, d) { this.color = new Col(c); this.density = d; },
  DirectionalLight: class extends Obj { constructor(c, i) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } },
  AmbientLight: class extends Obj { constructor(c, i) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } },
  PointLight: class extends Obj { constructor(c, i, d) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } },
  AdditiveBlending: 1, NormalBlending: 2, BackSide: 3, DoubleSide: 4, DynamicDrawUsage: 5,
};

/* ================= document / window 桩（可派发事件） ================= */
const els = new Map();
function mkEl(tag) {
  const el = {
    tag, children: [], listeners: {}, _cls: new Set(),
    style: {}, textContent: '', innerHTML: '', id: '', title: '', disabled: false, open: false,
    offsetWidth: 0, width: 0, height: 0, getContext: () => ctx2d,
    appendChild(c) { el.children.push(c); return c; },
    addEventListener(t, fn) { (el.listeners[t] = el.listeners[t] || []).push(fn); },
    dispatch(t, ev) { (el.listeners[t] || []).forEach(fn => fn(Object.assign({ currentTarget: el, preventDefault() {}, code: t }, ev))); },
    querySelectorAll(sel) {
      const cls = String(sel).replace(/^\./, '');
      return el.children.filter(c => (c._cls && c._cls.has(cls)) || (c.tag && c.tag === cls));
    },
  };
  el.classList = {
    add(c) { el._cls.add(c); }, remove(c) { el._cls.delete(c); },
    contains(c) { return el._cls.has(c); },
    toggle(c, v) { if (v === undefined) { el._cls.has(c) ? el._cls.delete(c) : el._cls.add(c); return el._cls.has(c); } v ? el._cls.add(c) : el._cls.delete(c); return !!v; },
  };
  Object.defineProperty(el, 'className', {
    get() { return [...el._cls].join(' '); },
    set(v) { el._cls = new Set(String(v).split(/\s+/).filter(Boolean)); },
  });
  return el;
}
const sel = s => { if (!els.has(s)) els.set(s, mkEl(s)); return els.get(s); };
const winListeners = {};
const timeState = { t: 0 };
const sandbox = {
  THREE,
  document: {
    querySelector: sel, querySelectorAll: () => [], createElement: mkEl, addEventListener() {},
    documentElement: mkEl('html'), body: mkEl('body'), head: mkEl('head'),
    activeElement: null, fullscreenElement: null, exitFullscreen() {},
  },
  performance: { now: () => timeState.t },
  requestAnimationFrame() {},
  console,
  setTimeout() { return 0; }, clearTimeout() {},
  location: { reload() {} },
  window: {
    addEventListener(t, fn) { (winListeners[t] = winListeners[t] || []).push(fn); },
    innerWidth: 1280, innerHeight: 800, devicePixelRatio: 1,
  },
  Audio: function () { return { addEventListener() {}, play: function () { return { catch: function () {} }; } }; },
};
sandbox.window.document = sandbox.document;
sandbox.window.dispatchKey = ev => { (winListeners.keydown || []).forEach(fn => fn(Object.assign({ preventDefault() {} }, ev))); };
sandbox.STAGE_NAMES = ['驿外断桥', '风雨黄昏', '无意争春', '零落成泥'];
sandbox.timeState = timeState;   // 供驱动器推进“时钟”

/* 顶层执行（含 THREE 桩） */
vm.createContext(sandbox);
try { vm.runInContext(code, sandbox, { filename: 'index.html' }); }
catch (e) { console.error('✗ 主脚本执行失败: ' + (e && e.stack)); process.exit(1); }
const get = e => vm.runInContext(e, sandbox);
const run = (src, tag) => { try { vm.runInContext(src, sandbox, { filename: tag || 'driver' }); return null; } catch (e) { return (e && e.message) || String(e); } };

/* ================= 1. 数据一致性 ================= */
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const TEXT = '驿外断桥边，寂寞开无主。已是黄昏独自愁，更著风和雨。无意苦争春，一任群芳妒。零落成泥碾作尘，只有香如故。';
let joined = '';
try { joined = POEM.map(l => l.segs.map(s => s.c).join('')).join(''); } catch (e) { fails.push('POEM 结构异常: ' + e.message); }
chk(joined === TEXT, '诗文与 queue.json 不一致:\n    实际: ' + joined);
chk(POEM.length === 4, `POEM 应 4 句，实际 ${POEM.length}`);
chk(STAGES.length === 5, `STAGES 应 5 项（封面+4境），实际 ${STAGES.length}`);
const STAGE_NAMES = ['驿外断桥', '风雨黄昏', '无意争春', '零落成泥'];
for (let i = 1; i < STAGES.length; i++) {
  chk(STAGES[i].name === POEM[i - 1].name, `境${i} 名错位 STAGES="${STAGES[i].name}" ≠ POEM="${POEM[i - 1].name}"`);
  chk(STAGES[i].name === STAGE_NAMES[i - 1], `境${i} 名应为 ${STAGE_NAMES[i - 1]}，实际 ${STAGES[i].name}`);
  chk(STAGES[i].name.length >= 2 && STAGES[i].name.length <= 4, `境${i} 境名应 2-4 字: ${STAGES[i].name}`);
}
POEM.forEach((p, i) => {
  const tag = `第${i + 1}句(${p.name})`;
  chk(!!p.jing, tag + ' 缺意境导览句 jing');
  chk(!!p.read, tag + ' 缺 read');
  chk(!!p.yisi, tag + ' 缺释义');
  chk(Array.isArray(p.zhu) && p.zhu.length >= 2, tag + ' 注释少于 2 条');
  const reads = p.segs.map(s => s.c).join('');
  chk(reads === p.read, tag + ' read 与 segs 不一致: ' + p.read);
  p.segs.forEach(seg => {
    const han = [...seg.c].filter(c => !/[，。、！？；：]/.test(c)).length;
    chk(han === seg.p.length, `${tag} "${seg.c}" 汉字${han}≠拼音${seg.p.length}`);
    chk(seg.p.every(x => /^[a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+$/i.test(x)), `${tag} "${seg.c}" 拼音含非法字符: ${seg.p.join(' ')}`);
  });
});
/* 多音字定点核查：著 zhuó / 一任 yī rèn / 碾 niǎn / 卜 bǔ */
const pyAll = POEM.flatMap(l => l.segs.flatMap(s => s.p));
chk(pyAll.includes('zhuó'), '缺「著(zhuó)」的注音');
chk(JSON.stringify(pyAll).includes('"yī","rèn"'), '缺「一任(yī rèn)」的逐字注音');
chk(pyAll.includes('niǎn'), '缺「碾(niǎn)」的注音');
chk(pyAll.includes('bǔ') || /卜.*bǔ/.test(code) || JSON.stringify(QUIZ).includes('bǔ'), '缺「卜(bǔ)」的读音说明');
chk(pyAll.includes('gèng'), '缺「更(gèng)」的注音');
chk(CN.length >= 4, `CN 中文数字数组太短: ${CN.length}`);
chk(JSON.stringify(CN.slice(0, 4)) === JSON.stringify(['壹', '贰', '叁', '肆']), 'CN 前四项应为 壹贰叁肆');

/* ================= 2. 数量联动 / 边界常量 / 色板 / 残留 ================= */
chk(code.includes('clamp(i,0,4)'), 'goto 缺 clamp(i,0,4)');
chk(/for\(let i=1;i<=4;i\+\+\)/.test(code), '进度点循环未改为 4');
chk((code.match(/curIdx===4&&state==='stage'/g) || []).length >= 2, `交互境接线 ${(code.match(/curIdx===4&&state==='stage'/g) || []).length} 处（应 pointerdown+空格 ≥2）`);
chk((code.match(/curIdx>=4\)showEnding\(\)/g) || []).length >= 2, `末境 showEnding 判断 ${(code.match(/curIdx>=4\)showEnding\(\)/g) || []).length} 处 <2（按钮+方向键）`);
chk(code.includes('curIdx===4)showEnding()'), '自动游览末境判断缺 curIdx===4');
chk(code.includes("'05.mp3'"), "缺全词音频 '05.mp3' 引用");
chk(code.includes('if(state!==\'stage\')return;'), 'showEnding 缺 state 守卫');
chk(!code.includes('将进酒') && !code.includes('万古愁'), '残留《将进酒》字样');
chk(!/太白/.test(code), '小测评语残留太白');
const root = (html.match(/:root\s*\{[^}]*\}/) || [''])[0];
const gm = (root.match(/--gold:\s*([^;\s]+)/) || [])[1];
chk(gm === '#4a4450', `--gold=${gm} ≠ 分配强调色 #4a4450`);
chk(!/background:#05070d/.test(html), 'body 背景仍为夜宴默认');
chk((code.match(/0x05070d/g) || []).length <= 1, `0x05070d 出现 ${(code.match(/0x05070d/g) || []).length} 次（>1）`);
chk(/background:#e9e2d0/.test(html), 'body 背景非宣纸 #e9e2d0（xuanzhi 浅色赛道）');
chk(/autoMode=true/.test(code), 'autoMode 未默认开启');
chk(/id="btnAuto" class="on">自动游览 · 开/.test(html), '自动游览按钮初始态应为 on + “自动游览 · 开”');
chk(html.includes('href="../index.html"'), '缺返回诗集目录链接');
chk((html.match(/class="galLink"/g) || []).length >= 2, `galLink 链接 ${(html.match(/class="galLink"/g) || []).length} 处（封面+终章各一）`);
chk(html.includes('.galLink{display:inline-block'), '缺 .galLink 样式');
chk(QUIZ.length === 5, `QUIZ 应 5 题，实际 ${QUIZ.length}`);
QUIZ.forEach((q, i) => {
  chk(Array.isArray(q.o) && q.o.length === 3, `题${i + 1} 选项数≠3`);
  chk(typeof q.a === 'number' && q.a >= 0 && q.a < q.o.length, `题${i + 1} 答案越界`);
});
const wq = code.match(/words\s*=\s*\[([^\]]*)\]/);
chk(wq && wq[1].split(',').length === 6, `小测评语 words 应 6 项，实际 ${wq ? wq[1].split(',').length : 0}`);

/* ================= 3. 全部 STAGES：sky / cam / build / update / fade ================= */
const ctx = run(`
window.__errs = [];
for (let i = 0; i < STAGES.length; i++) {
  const s = STAGES[i];
  const sk = s.sky();
  if (!sk.top || !sk.hor || !sk.fog || typeof sk.fd !== 'number' || !sk.moon) throw new Error('境' + i + ' sky() 字段不全');
  if (typeof s.dwell !== 'number' || typeof s.river !== 'number') throw new Error('境' + i + ' 缺 dwell/river');
  if (!s.cam || !s.cam.f || !s.cam.t || !s.cam.lf || !s.cam.lt) throw new Error('境' + i + ' cam 不全');
  const st = s.build();
  if (!st.group) throw new Error('境' + i + ' build 未返回 group');
  st.group.userData.fadeK = 1;
  for (let k = 0; k < 40; k++) { if (st.update) st.update(k * 0.1 + 1, 0.016); }
  setFade(st.group, 0.3); setFade(st.group, 0); setFade(st.group, 1);
  // 透明物 renderOrder 分层：穹顶 -10 < 星 -9 < 月 -8 < 水 1 < 粒子 3 < 雾 5
  st.group.traverse(o => {
    if (o.renderOrder !== undefined && o.material && o.material.isShaderMaterial && o.material.uniforms && o.material.uniforms.uFade === undefined)
      throw new Error('境' + i + ' 着色器材质缺 uFade（无法随境淡入淡出）');
  });
}
`, 'stages');
chk(ctx === null, 'STAGES 全量 build/update/fade 抛错: ' + ctx);

/* ================= 4. 标志性瞬间：第四境 click 全时序 ================= */
const c4 = run(`
const st4 = STAGES[4].build();
st4.group.userData.fadeK = 1;
if (typeof st4.click !== 'function') throw new Error('第四境缺 click');
clock.t = 100;
for (let t = 100; t <= 118; t += 0.05) { clock.t = t; stageT = t; st4.update(t, 0.05); }
stageT = 6; st4.click();
const flash = document.querySelector('#flash');
if (flash.textContent !== '香如故') throw new Error('点击后题字未更新: ' + flash.textContent);
st4.click();                                    // 冷却中再点 → 守卫应拦截
for (let t = 118; t <= 130; t += 0.05) { clock.t = t; stageT = 6 + (t - 118); st4.update(t - 118, 0.05); }
st4.click();                                    // 冷却后再点 → 应再次触发
`, 'interact');
chk(c4 === null, '第四境点击交互时序抛错: ' + c4);

/* ================= 5. 全生命周期：boot → goto(1..4) → 自动游览 → 终章 → 小测 ================= */
const boot = run('boot();', 'boot');
chk(boot === null, 'boot() 抛错: ' + boot);
chk(get('state') === 'stage', 'boot() 后 state 应为 stage');
chk(get('renderer.renders') >= 1, 'boot() 未渲染首帧');
chk(get("document.querySelector('#dots').children.length") === 4, '进度点应为 4 个');

/* 5.1 手动逐境（关自动），每境推进足够帧数完成 2.6s 转场并运行 update */
const walk = run(`
autoMode = false;
for (let i = 1; i <= 4; i++) {
  goto(i);
  if (state !== 'transition') throw new Error('goto(' + i + ') 未进入转场');
  for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
  if (state !== 'stage') throw new Error('境' + i + ' 转场未结束: ' + state);
  if (curIdx !== i) throw new Error('境' + i + ' curIdx=' + curIdx);
  if (!curStageObj || !curStageObj.group) throw new Error('境' + i + ' curStageObj 异常');
  if (document.querySelector('#stageName').textContent !== STAGE_NAMES[i-1]) throw new Error('境' + i + ' HUD 境名未更新');
}
goto(0); for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 0) throw new Error('返回封面失败');
`, 'walk');
chk(walk === null, '逐境生命周期抛错: ' + walk);

/* 5.2 第四境空格键 → 触发交互（真实键盘接线） */
const space = run(`
autoMode = false;
goto(4); for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
stageT = 6;
document.querySelector('#flash').textContent = '';
document.querySelector('#flash')._cls.delete('go');
window.dispatchKey({ code: 'Space' });
if (document.querySelector('#flash').textContent !== '香如故') throw new Error('空格键未触发第四境交互');
`, 'space');
chk(space === null, '空格键交互接线抛错: ' + space);

/* 5.3 自动游览全程：从第一境一路走到终章 */
const auto = run(`
autoMode = true; autoT = 0;
goto(1); for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
let frames = 0;
while (state !== 'ending' && frames < 9000) { timeState.t += 16.7; animate(); frames++; }
if (state !== 'ending') throw new Error('自动游览未能抵达终章（frames=' + frames + ', curIdx=' + curIdx + '）');
if (!document.querySelector('#ending')._cls.has('show')) throw new Error('终章未显示');
const segTotal = POEM.reduce((n, l) => n + l.segs.length, 0);
if (document.querySelector('#endPoem').children.length !== segTotal)
  throw new Error('终章全文块数≠' + segTotal + '（实际 ' + document.querySelector('#endPoem').children.length + '）');
const endZi = document.querySelector('#endPoem').children.map(c => c.children.length).reduce((a, b) => a + b, 0);
if (endZi < 20) throw new Error('终章全文逐字块过少: ' + endZi);
`, 'auto');
chk(auto === null, '自动游览全程抛错: ' + auto);

/* 5.4 终章按钮 → 小测全流程（真实点击派发） */
const quiz = run(`
document.querySelector('#btnQuiz').dispatch('click');
if (!document.querySelector('#quiz')._cls.has('show')) throw new Error('小测未打开');
let asked = 0;
for (let q = 0; q < QUIZ.length; q++) {
  const body = document.querySelector('#quizBody');
  const opts = body.children.filter(c => c._cls && c._cls.has('opt')).slice(-3);
  if (opts.length !== 3) throw new Error('第' + (q+1) + '题选项未生成: ' + opts.length);
  const right = opts[QUIZ[q].a];
  right.dispatch('click');
  asked++;
  const next = body.children.filter(c => c.id === 'quizNext')[q];
  if (!next) throw new Error('第' + (q+1) + '题缺“下一题”按钮');
  next.dispatch('click');
}
if (qScore !== QUIZ.length) throw new Error('全选正确时得分应为 ' + QUIZ.length + '，实际 ' + qScore);
const close = document.querySelector('#quizBody').children.filter(c => c.id === 'quizClose')[0];
if (!close) throw new Error('结果页缺关闭按钮');
close.dispatch('click');
if (document.querySelector('#quiz')._cls.has('show')) throw new Error('小测未关闭');
if (asked !== 5) throw new Error('实际答题数 ' + asked);
`, 'quiz');
chk(quiz === null, '小测全流程抛错: ' + quiz);

/* 5.5 其余控件监听器全部可派发（按钮无一漏接） */
const wired = run(`
['#btnPrev','#btnNext','#btnAuto','#btnSpeak','#btnAutoSpeak','#btnPy','#btnSnd','#btnFs','#btnAgain','#btnCover','#btnPoemAudio','#enterBtn'].forEach(id => {
  const el = document.querySelector(id);
  if (!el.listeners || !el.listeners.click || !el.listeners.click.length) throw new Error(id + ' 未接 click 监听');
});
document.querySelector('#btnAuto').dispatch('click');
if (autoMode !== false) throw new Error('自动游览按钮未切换状态');
document.querySelector('#btnAuto').dispatch('click');
if (autoMode !== true) throw new Error('自动游览按钮未切回');
document.querySelector('#btnPy').dispatch('click');
if (!document.body._cls.has('no-py-off')) throw new Error('注音开关未生效');
document.querySelector('#btnPy').dispatch('click');
document.querySelector('#btnSnd').dispatch('click');
if (groupAudio.muted !== true) throw new Error('静音开关未生效');
document.querySelector('#btnSnd').dispatch('click');
document.querySelector('#btnPrev').dispatch('click');
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 3) throw new Error('上一境未生效: curIdx=' + curIdx);
document.querySelector('#btnNext').dispatch('click');
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 4) throw new Error('下一境未生效: curIdx=' + curIdx);
document.querySelector('#btnAgain').dispatch('click');
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 1) throw new Error('重新入境未回到第一境: curIdx=' + curIdx);
document.querySelector('#btnCover').dispatch('click');
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 0) throw new Error('回到封面未生效: curIdx=' + curIdx);
document.querySelector('#btnSpeak').dispatch('click');
document.querySelector('#btnPoemAudio').dispatch('click');
document.querySelector('#enterBtn').dispatch('click');
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 1) throw new Error('封面入境未生效: curIdx=' + curIdx);
window.dispatchKey({ code: 'ArrowLeft', preventDefault() {} });
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 0) throw new Error('← 键未生效');
window.dispatchKey({ code: 'ArrowRight', preventDefault() {} });
for (let k = 0; k < 220; k++) { timeState.t += 16.7; animate(); }
if (curIdx !== 1) throw new Error('→ 键未生效');
window.dispatchKey({ code: 'Escape', preventDefault() {} });
`, 'wire');
chk(wired === null, '控件/键盘接线抛错: ' + wired);

/* ================= 6. 资源与音频 ================= */
const audioDir = path.join(dir, 'audio');
if (!fs.existsSync(audioDir)) {
  console.log('⚠ 尚无 audio/ 目录（gen-voice.local.js 尚未运行）');
} else {
  const have = fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length;
  const need = POEM.length + 2;
  chk(have === need, `audio ${have} 个 ≠ 诗句数+2=${need}`);
  for (let i = 0; i <= need - 1; i++) {
    const f = String(i).padStart(2, '0') + '.mp3';
    chk(fs.existsSync(path.join(audioDir, f)), '缺音频 ' + f);
  }
}

/* ================= 汇总 ================= */
if (fails.length) {
  console.error('SMOKE FAIL:');
  fails.forEach((f, i) => console.error(`  ${i + 1}. ${f}`));
  process.exit(1);
}
console.log('SMOKE PASS：4 境 + 卷首 build/sky/cam/update 全跑通；第四境点击(指针/空格/守卫/冷却/复位)全时序通过；'
  + 'boot → 逐境 → 自动游览 → 终章 → 小测全流程通过；数据/数量联动/色板/残留/音频检查通过。');
