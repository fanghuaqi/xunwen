/*
 * smoke.test.js —— 《蝉》(chan-yushinan) 深冒烟测试
 * 用 THREE 桩 + DOM 桩在 Node 里真实执行主脚本，跑通：
 *   引导加载 → boot → 全部 builder/update → 点击交互 → 自动游览全生命周期
 *   → 终章 → 小测全流程 → 各按钮/键盘/窗口事件
 * 运行: node smoke.test.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const FILE = path.join(__dirname, 'index.html');
const html = fs.readFileSync(FILE, 'utf8');
const mm = html.match(/<script id="main">([\s\S]*?)<\/script>/);
if (!mm) { console.error('✗ 未找到主脚本'); process.exit(1); }
const code = mm[1];
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'chan-yushinan');

let fails = 0, checks = 0;
const ok = (cond, msg) => { checks++; if (!cond) { fails++; console.error('✗ ' + msg); } };
const eq = (a, b, msg) => ok(a === b, msg + ` (期望 ${b}，实得 ${a})`);

/* ============================ THREE 桩 ============================ */
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } set(x, y) { this.x = x; this.y = y; return this; } copy(v) { this.x = v.x; this.y = v.y; return this; } clone() { return new V2(this.x, this.y); } }
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  setScalar(s) { this.x = this.y = this.z = s; return this; }
  setComponent(i, v) { if (i === 0) this.x = v; else if (i === 1) this.y = v; else this.z = v; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  length() { return Math.hypot(this.x, this.y, this.z); }
  normalize() { const l = this.length() || 1; return this.multiplyScalar(1 / l); }
  lerpVectors(a, b, t) { this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t; return this; }
  crossVectors(a, b) { const ax = a.x, ay = a.y, az = a.z, bx = b.x, by = b.y, bz = b.z; this.x = ay * bz - az * by; this.y = az * bx - ax * bz; this.z = ax * by - ay * bx; return this; }
  dot(v) { return this.x * v.x + this.y * v.y + this.z * v.z; }
  distanceTo(v) { return Math.hypot(this.x - v.x, this.y - v.y, this.z - v.z); }
  applyQuaternion() { return this; }
  applyMatrix4() { return this; }
  negate() { this.x = -this.x; this.y = -this.y; this.z = -this.z; return this; }
  divideScalar(s) { return this.multiplyScalar(1 / (s || 1)); }
  setFromMatrixPosition() { return this; }
}
const hex2rgb = h => [((h >> 16) & 255) / 255, ((h >> 8) & 255) / 255, (h & 255) / 255];
class Color {
  constructor(h = 0xffffff) { const c = (typeof h === 'number') ? hex2rgb(h) : [h.r || 0, h.g || 0, h.b || 0]; this.r = c[0]; this.g = c[1]; this.b = c[2]; }
  setHex(h) { const c = hex2rgb(h); this.r = c[0]; this.g = c[1]; this.b = c[2]; return this; }
  set(h) { return this.setHex(h); }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { const c = new Color(0); c.r = this.r; c.g = this.g; c.b = this.b; return c; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  lerp(a, t) { return this.lerpColors(this, a, t); }
  getHex() { return (Math.round(this.r * 255) << 16) | (Math.round(this.g * 255) << 8) | Math.round(this.b * 255); }
}
class Euler { constructor() { this.x = 0; this.y = 0; this.z = 0; } set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } copy(e) { this.x = e.x; this.y = e.y; this.z = e.z; return this; } }
class Quat { setFromUnitVectors() { return this; } setFromAxisAngle() { return this; } copy() { return this; } }
class Obj3D {
  constructor() {
    this.position = new V3(); this.rotation = new Euler(); this.scale = new V3(1, 1, 1);
    this.quaternion = new Quat(); this.userData = {}; this.children = []; this.visible = true;
    this.renderOrder = 0; this.frustumCulled = true; this.material = null; this.geometry = null;
    this.isObject3D = true; this.parent = null;
  }
  add(...os) { for (const o of os) { if (!o) continue; this.children.push(o); o.parent = this; } return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(cb) { cb(this); for (const c of this.children) c.traverse(cb); }
  rotateZ(a) { this.rotation.z += a; return this; }
  rotateOnAxis() { return this; }
  rotateY(a) { this.rotation.y += a; return this; }
  lookAt() { return this; }
  updateMatrix() { return this; }
  getObjectById() { return this; }
}
const matBase = () => ({
  color: new Color(), opacity: 1, transparent: false, depthWrite: true, side: 0,
  blending: 1, needsUpdate: false, fog: true, uniform: null, uniforms: null,
  userData: {}, map: null, emissive: null, specular: null, shininess: 0,
  clone() { const m = Object.assign({}, this); m.userData = Object.assign({}, this.userData); if (this.color) m.color = this.color.clone(); return m; },
  dispose() { this.disposed = true; },
});
class Mat { constructor(o) { Object.assign(this, matBase(), o || {}); if (!(this.color instanceof Color)) this.color = new Color(this.color || 0xffffff); } }
class ShaderMat extends Mat { constructor(o) { super(o); this.isShaderMaterial = true; this.uniforms = (o && o.uniforms) || {}; this.vertexShader = o && o.vertexShader; this.fragmentShader = o && o.fragmentShader; } }
class BufAttr { constructor(array, itemSize) { this.array = array; this.itemSize = itemSize; this.count = array ? array.length / itemSize : 0; this.needsUpdate = false; } }
class Geo {
  constructor() { this.attributes = {}; this.parameters = {}; this.disposed = false; }
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  getAttribute(n) { return this.attributes[n]; }
  setIndex() { return this; }
  setFromPoints(p) { this.pts = p; return this; }
  rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  translate() { return this; } scale() { return this; } center() { return this; }
  computeVertexNormals() { return this; }
  dispose() { this.disposed = true; }
}
class Camera extends Obj3D { constructor() { super(); this.aspect = 1; } updateProjectionMatrix() { return this; } }
class Renderer {
  constructor() {
    this.domElement = { style: {}, _l: {}, addEventListener(t, f) { (this._l[t] = this._l[t] || []).push(f); }, removeEventListener() {}, getContext: () => null };
    this.calls = 0;
  }
  setPixelRatio() {} setSize() {} setClearColor(c) { this.clearColor = c; }
  render() { this.calls++; } dispose() {} getContext() { return null; }
}
let DYN = 0;
function lightClass() {
  return class extends Obj3D {
    constructor(c, i) { super(); this.isLight = true; this.color = new Color(c); this.intensity = i === undefined ? 1 : i; this.baseI = undefined; }
  };
}
const REAL = {
  Vector2: V2, Vector3: V3, Color, Euler: Euler, Quaternion: Quat, Object3D: Obj3D, Group: Obj3D, Scene: class extends Obj3D { constructor() { super(); this.fog = null; } },
  Mesh: class extends Obj3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } },
  Points: class extends Obj3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isPoints = true; } },
  Line: class extends Obj3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } },
  Sprite: class extends Obj3D { constructor(m) { super(); this.material = m; this.isSprite = true; } },
  PerspectiveCamera: Camera,
  WebGLRenderer: Renderer,
  DirectionalLight: lightClass(), AmbientLight: lightClass(), PointLight: lightClass(), SpotLight: lightClass(),
  FogExp2: class { constructor(c, d) { this.color = new Color(c); this.density = d; } },
  BufferGeometry: Geo, PlaneGeometry: Geo, SphereGeometry: Geo, ConeGeometry: Geo, CylinderGeometry: Geo,
  CircleGeometry: Geo, RingGeometry: Geo, TorusGeometry: Geo, TubeGeometry: Geo, ShapeGeometry: Geo,
  BoxGeometry: Geo, LatheGeometry: Geo, EdgesGeometry: Geo, IcosahedronGeometry: Geo, TorusKnotGeometry: Geo,
  BufferAttribute: BufAttr, Float32BufferAttribute: BufAttr,
  InstancedMesh: class extends Obj3D { constructor(g, m, n) { super(); this.geometry = g; this.material = m; this.count = n; this.instanceMatrix = { needsUpdate: false, setUsage() {} }; } setMatrixAt() {} },
  ShaderMaterial: ShaderMat, MeshBasicMaterial: Mat, MeshPhongMaterial: Mat, MeshLambertMaterial: Mat,
  MeshStandardMaterial: Mat, PointsMaterial: Mat, SpriteMaterial: Mat, LineBasicMaterial: Mat, LineDashedMaterial: Mat,
  CanvasTexture: class { constructor(c) { this.image = c; } dispose() {} },
  VideoTexture: class { dispose() {} },
  Shape: class { moveTo() { return this; } lineTo() { return this; } bezierCurveTo() { return this; } quadraticCurveTo() { return this; } absarc() { return this; } arc() { return this; } closePath() { return this; } },
  CatmullRomCurve3: class { constructor(p) { this.points = p; } getPoint() { return new V3(); } },
  Clock: class { getDelta() { return 0.016; } },
  BackSide: 1, FrontSide: 0, DoubleSide: 2, AdditiveBlending: 2, NormalBlending: 1, DynamicDrawUsage: 35048,
  LinearFilter: 1006, ReinhardToneMapping: 4, NoToneMapping: 0, RepeatWrapping: 1000, MathUtils: { clamp: (a, b, c) => Math.max(b, Math.min(c, a)) },
};
const THREE = new Proxy(REAL, {
  get(t, p) {
    if (p === 'then') return undefined;
    if (p in t) return t[p];
    // 未知 API 一律给一个可 new / 可调用的惰性桩，保证测试不因桩缺口中断
    const G = class extends Obj3D { constructor() { super(); const a = arguments; for (let i = 0; i < a.length; i++) { if (a[i] && a[i].isObject3D) this.geometry = a[i]; else if (a[i] && a[i].isMaterial) this.material = a[i]; } } };
    t[p] = G; return G;
  },
});

/* ============================ DOM / 环境桩 ============================ */
function ctx2d() {
  return {
    createRadialGradient: () => ({ addColorStop() {} }),
    createLinearGradient: () => ({ addColorStop() {} }),
    fillRect() {}, fillText() {}, drawImage() {}, beginPath() {}, arc() {}, fill() {}, stroke() {},
    set fillStyle(v) {}, set font(v) {}, set textAlign(v) {}, set textBaseline(v) {},
    set shadowColor(v) {}, set shadowBlur(v) {}, set globalAlpha(v) {},
  };
}
const listeners = {};
function mkEl(tag) {
  const el = {
    tagName: tag || 'DIV', style: {}, textContent: '', className: '', title: '', disabled: false, open: false,
    offsetWidth: 100, children: [], _l: {}, _html: '',
    classList: {
      _s: new Set(),
      add(...c) { c.forEach(x => this._s.add(x)); },
      remove(...c) { c.forEach(x => this._s.delete(x)); },
      toggle(c, f) { const has = this._s.has(c); const want = f === undefined ? !has : !!f; if (want) this._s.add(c); else this._s.delete(c); return want; },
      contains(c) { return this._s.has(c); },
    },
    addEventListener(t, f) { (el._l[t] = el._l[t] || []).push(f); },
    removeEventListener() {},
    appendChild(c) { el.children.push(c); return c; },
    querySelector(s) { return mkEl('div'); },
    querySelectorAll(s) {
      if (s === '.opt') return el.children.filter(c => (c.className || '').split(' ').indexOf('opt') >= 0);
      return el.children.slice();
    },
    getContext() { return ctx2d(); },
    focus() {}, blur() {}, click() {}, requestFullscreen() {},
    fire(t, ev) { (el._l[t] || []).forEach(f => f(ev || { currentTarget: el, preventDefault() {}, code: '', clientX: 0, clientY: 0, target: el })); },
  };
  Object.defineProperty(el, 'innerHTML', { get: () => el._html, set: v => { el._html = v; el.children.length = 0; } });
  return el;
}
const bySel = {};
const document = {
  _l: {},
  querySelector(s) { return bySel[s] || (bySel[s] = mkEl('div')); },
  querySelectorAll(s) { return bySel[s] ? bySel[s].children.slice() : []; },
  createElement(t) { return mkEl(t === 'canvas' ? 'CANVAS' : t); },
  addEventListener(t, f) { (document._l[t] = document._l[t] || []).push(f); },
  activeElement: null, fullscreenElement: null,
  body: mkEl('BODY'), head: mkEl('HEAD'), documentElement: mkEl('HTML'),
  exitFullscreen() {},
};
let NOW = 0;
const rafQueue = [];
class AudioCtx {
  constructor() { this.currentTime = 0; this.sampleRate = 44100; this.state = 'running'; this.destination = {}; }
  resume() {}
  createGain() { return { gain: { value: 1, setValueAtTime() {}, exponentialRampToValueAtTime() {}, linearRampToValueAtTime() {}, cancelScheduledValues() {} }, connect() { return this; } }; }
  createBufferSource() { return { buffer: null, loop: false, connect() { return this; }, start() {}, stop() {} }; }
  createBiquadFilter() { return { type: '', frequency: { value: 0 }, Q: { value: 0 }, connect() { return this; } }; }
  createOscillator() { return { type: '', frequency: { value: 0, setValueAtTime() {}, exponentialRampToValueAtTime() {} }, connect() { return this; }, start() {}, stop() {} }; }
  createBuffer(ch, len) { return { getChannelData: () => new Float32Array(len), length: len }; }
}
class AudioEl {
  constructor(src) { this.src = src; this._l = {}; this.paused = false; }
  addEventListener(t, f) { (this._l[t] = this._l[t] || []).push(f); }
  play() { this.played = true; return Promise.resolve(); }
  pause() {}
}
const speechSynth = { getVoices: () => [], speak() {}, cancel() {}, onvoiceschanged: null };
const windowObj = {
  addEventListener(t, f) { (windowObj._l = windowObj._l || {})[t] = (windowObj._l[t] || []).concat(f); },
  _l: {}, innerWidth: 1600, innerHeight: 900, devicePixelRatio: 1,
  AudioContext: AudioCtx, webkitAudioContext: AudioCtx, Audio: AudioEl,
  speechSynthesis: speechSynth, SpeechSynthesisUtterance: class { constructor(t) { this.text = t; } },
  location: { reload() {} }, __inited: false, THREE,
};
const sandbox = {
  THREE, window: windowObj, document, console,
  performance: { now: () => NOW },
  requestAnimationFrame(f) { rafQueue.push(f); return rafQueue.length; },
  cancelAnimationFrame() {},
  setTimeout(f) { return 0; }, clearTimeout() {}, setInterval() { return 0; }, clearInterval() {},
  Audio: AudioEl, speechSynthesis: speechSynth, SpeechSynthesisUtterance: windowObj.SpeechSynthesisUtterance,
  location: windowObj.location, navigator: { userAgent: 'node' }, Math, Date, JSON, String, Number, Array, Object, Promise, isNaN, parseFloat, parseInt,
};
sandbox.window.document = document; sandbox.window.performance = sandbox.performance;
sandbox.window.requestAnimationFrame = sandbox.requestAnimationFrame;
vm.createContext(sandbox);

/* ============================ 执行主脚本 ============================ */
try { vm.runInContext(code, sandbox, { filename: FILE }); }
catch (e) { console.error('✗ 主脚本顶层执行失败: ' + e.stack); process.exit(1); }
ok(true, '主脚本顶层执行');

const get = e => vm.runInContext(e, sandbox);
const run = (e) => vm.runInContext(e, sandbox);
const POEM = get('POEM'), STAGES = get('STAGES'), CN = get('CN'), QUIZ = get('QUIZ');

/* ============================ 1. 数据 ============================ */
eq(POEM.length, entry.stages.length, 'POEM 句数');
eq(STAGES.length, POEM.length + 1, 'STAGES = POEM + 1');
ok(STAGES[0].name === '卷首' || STAGES[0].key === 'cover', 'STAGES[0] 为封面');
POEM.forEach((p, i) => {
  eq(STAGES[i + 1].name, p.name, `境${i + 1} 名对齐`);
  const joined = p.segs.map(s => s.c).join('');
  ok(typeof p.read === 'string' && p.read.length > 0, `第${i + 1}句 read`);
  ok(typeof p.yisi === 'string' && p.yisi.length > 10, `第${i + 1}句 yisi`);
  ok(Array.isArray(p.zhu) && p.zhu.length >= 2, `第${i + 1}句 zhu ≥2 条`);
  ok(typeof p.jing === 'string' && p.jing.length > 4, `第${i + 1}句 jing`);
  p.segs.forEach(seg => {
    const han = [...seg.c].filter(c => !/[，。、！？；：…—·]/.test(c)).length;
    eq(seg.p.length, han, `第${i + 1}句「${seg.c}」拼音数`);
  });
});
eq(POEM.map(l => l.segs.map(s => s.c).join('')).join(''), entry.text, '诗文逐字一致');
eq(CN.length >= POEM.length, true, 'CN 长度足够');
ok(QUIZ.length >= 5, '小测 ≥5 题');
QUIZ.forEach((q, i) => {
  eq(q.o.length, 3, `小测${i + 1} 选项数`);
  ok(Number.isInteger(q.a) && q.a >= 0 && q.a < 3, `小测${i + 1} 答案下标`);
});
// 多音字读音核对
const pinyinOf = (lineIdx, segIdx) => POEM[lineIdx].segs[segIdx].p;
ok(pinyinOf(0, 0)[1] === 'ruí', '「緌」读 ruí');
ok(pinyinOf(0, 0)[2] === 'yǐn', '「饮」读 yǐn');
ok(pinyinOf(0, 0)[4] === 'lù', '「露」读 lù');
ok(pinyinOf(1, 1)[2] === 'jiè', '「藉」读 jiè');

/* ============================ 2. 每个 builder 独立空跑 ============================ */
STAGES.forEach((s, i) => {
  const tag = `境${i}(${s.name})`;
  let o = null;
  try { o = s.build(); } catch (e) { ok(false, tag + ' build() 抛错: ' + e.message); return; }
  ok(o && o.group && typeof o.update === 'function', tag + ' 返回 {group, update}');
  ok(o.group.children.length > 0, tag + ' 场景非空');
  ok(typeof s.sky === 'function', tag + ' sky 为惰性工厂');
  const k = s.sky();
  ok(!!k.top && !!k.hor && !!k.fog && typeof k.fd === 'number' && !!k.moon, tag + ' sky 字段齐全');
  for (let f = 0; f < 40; f++) {
    try { o.update(f * 0.25, 0.05); } catch (e) { ok(false, tag + ' update 抛错: ' + e.message); break; }
  }
  if (o.onEnter) { try { o.onEnter(); } catch (e) { ok(false, tag + ' onEnter 抛错: ' + e.message); } }
  if (o.click) { try { o.click(); } catch (e) { ok(false, tag + ' click 抛错: ' + e.message); } }
  // 透明度/强度必须带 fadeK（硬性约束 8）：把 fadeK 置 0 后，材质 opacity 应全为 0
  o.group.userData.fadeK = 0;
  try { o.update(1.0, 0.05); } catch (e) { ok(false, tag + ' fadeK=0 update 抛错: ' + e.message); }
  let leak = [];
  o.group.traverse(n => {
    if (n.material && !n.material.isShaderMaterial && n.material.transparent &&
        typeof n.material.opacity === 'number' && n.material.userData && n.material.userData.baseOpacity !== undefined &&
        n.material.opacity > 0.001) leak.push(n.material.opacity);
  });
  ok(leak.length === 0, tag + ' fadeK=0 时仍有材质 opacity>0（交叉淡化会被覆盖）: ' + leak.slice(0, 4).join(','));
  o.group.userData.fadeK = 1;
});

/* ============================ 3. 引擎构件覆盖 ============================ */
try {
  const flow = run('makeFlow({n:50,box:[20,10,20]})');
  flow.update(1.0);
  ok(!!flow.points, 'makeFlow 构件可构建/更新');
  const rings = run('makeRings({n:3,r0:2,r1:30})');
  rings.update(1, 0.05, 1, 1.6);
  ok(rings.items.length === 3, 'makeRings 构件可构建/按 boost 更新');
  const w = run('makeWater({size:100,amp:0.1})');
  w.update(2);
  ok(!!w.mesh, 'makeWater 构件可构建/更新');
} catch (e) { ok(false, '构件覆盖抛错: ' + e.message); }

/* ============================ 4. boot + 全生命周期 ============================ */
const frames = (n, step) => {
  for (let i = 0; i < n; i++) { NOW += (step === undefined ? 50 : step); try { run('animate()'); } catch (e) { ok(false, 'animate 抛错: ' + e.message); return; } }
};
try { run('initApp()'); ok(true, 'boot() 成功'); } catch (e) { ok(false, 'boot 抛错: ' + e.stack); }
eq(run('state'), 'stage', 'boot 后 state=stage');
eq(run('curIdx'), 0, 'boot 后停在封面境');
eq(run('autoMode'), true, 'autoMode 默认开');
frames(30);
ok(bySel['#dots'].children.length === POEM.length, `进度点为 ${POEM.length} 个（实得 ${bySel['#dots'].children.length}）`);

// 入 境
bySel['#enterBtn'].fire('click');
frames(70, 50);                                  // 2.6s 过渡 + 若干帧
eq(run('state'), 'stage', '入境过渡完成');
eq(run('curIdx'), 1, '进入第一境');
ok(bySel['#poemBox'].children.length === POEM[0].segs.length, '第一境竖排诗句已渲染');
ok(bySel['#yisi'].textContent === POEM[0].yisi, '释义已填充');
ok(bySel['#zhu'].children.length === POEM[0].zhu.length, '注释条数一致');
ok(run('document.body.classList.contains("no-poem")') === false, '诗句容器显示');
// 视差/呼吸后相机无 NaN
frames(5);
ok(!/NaN/.test(JSON.stringify(run('camera.position'))), '相机位置无 NaN');

// 自动游览：一路走到终章（封面停留 + 两境 dwell + 过渡）
let guard = 0;
while (run('state') !== 'ending' && guard++ < 2000) frames(1, 50);
eq(run('state'), 'ending', '自动游览抵达终章');
ok(run('curIdx') === 2, '终章停在末境');
ok(bySel['#endPoem'].children.length > 0, '终章全诗已渲染');

// 点击交互境（指针 + 空格两条接线）
run('goto(2)');
frames(90, 50);
eq(run('curIdx'), 2, '进入第二境（交互境）');
ok(typeof run('curStageObj.click') === 'function', '第二境有 click()（交互境）');
const cv = run('renderer.domElement');
ok(cv._l && (cv._l.pointerdown || []).length >= 1, 'canvas 已绑定 pointerdown');
(cv._l.pointerdown || []).forEach(f => { try { f({}); } catch (e) { ok(false, 'pointerdown 抛错: ' + e.message); } });
eq(bySel['#flash'].textContent, '流响自远', '点击画面触发流响（flash 文案）');
frames(60, 50);                                   // 越过 0.9s 点击冷却
const keyFns = (windowObj._l.keydown || []);
ok(keyFns.length >= 1, 'keydown 已接线');
keyFns.forEach(f => { try { f({ code: 'Space', preventDefault() {} }); } catch (e) { ok(false, '空格处理抛错: ' + e.message); } });
eq(run('curIdx'), 2, '交互境空格=点击（不直接跳境）');
eq(bySel['#flash'].textContent, '流响自远', '空格同样触发流响');
keyFns.forEach(f => { try { f({ code: 'ArrowLeft', preventDefault() {} }); } catch (e) { ok(false, 'ArrowLeft 抛错: ' + e.message); } });
frames(80, 50);
keyFns.forEach(f => { try { f({ code: 'ArrowRight', preventDefault() {} }); } catch (e) { ok(false, 'ArrowRight 抛错: ' + e.message); } });
frames(80, 50);
eq(run('curIdx'), 2, '方向键回到末境');

// 终章 → 小测全流程
run('state="stage"'); run('showEnding()');
eq(run('state'), 'ending', 'showEnding 生效');
bySel['#btnQuiz'].fire('click');
eq(bySel['#quiz'].classList.contains('show'), true, '小测面板打开');
for (let qi = 0; qi < QUIZ.length; qi++) {
  const opts = bySel['#quizBody'].children.filter(c => (c.className || '').indexOf('opt') >= 0);
  eq(opts.length, 3, `小测第 ${qi + 1} 题选项渲染`);
  opts[QUIZ[qi].a].fire('click');
  const next = bySel['#quizBody'].children.filter(c => c.id === 'quizNext');
  if (next.length) next[0].fire('click');
}
ok(bySel['#quizCnt'].textContent.indexOf('完') >= 0, '小测走完到结果页');
const closeBtn = bySel['#quizBody'].children.filter(c => c.id === 'quizClose');
ok(closeBtn.length === 1, '结果页有关闭按钮');
closeBtn[0].fire('click');

// 终章各按钮
bySel['#btnPoemAudio'].fire('click');
bySel['#btnAgain'].fire('click'); frames(70, 50);
eq(run('curIdx'), 1, '「重新入境」回到第一境');
bySel['#btnNext'].fire('click'); frames(70, 50);
eq(run('curIdx'), 2, '「下一境」到第二境');
bySel['#btnNext'].fire('click');
eq(run('state'), 'ending', '末境「下一境」进终章');
bySel['#btnCover'].fire('click'); frames(40, 50);
eq(run('curIdx'), 0, '「回到封面」回卷首');
ok(bySel['#cover'].classList.contains('off') === false, '封面重新显示');

// 控件开关
bySel['#btnAuto'].fire('click'); eq(run('autoMode'), false, '自动游览可关'); bySel['#btnAuto'].fire('click'); eq(run('autoMode'), true, '自动游览可开');
bySel['#btnAutoSpeak'].fire('click'); eq(run('autoSpeak'), false, '自动朗读可关'); bySel['#btnAutoSpeak'].fire('click');
bySel['#btnPy'].fire('click'); bySel['#btnPy'].fire('click');
bySel['#btnSnd'].fire('click'); bySel['#btnSnd'].fire('click');
bySel['#btnFs'].fire('click');
bySel['#btnSpeak'].fire('click');
bySel['#btnPrev'].fire('click'); frames(60, 50);
ok(run('curIdx') >= 0, '上一境不越界');
(windowObj._l.resize || []).forEach(f => { try { f({}); } catch (e) { ok(false, 'resize 抛错: ' + e.message); } });
(windowObj._l.pointermove || []).forEach(f => { try { f({ clientX: 800, clientY: 300 }); } catch (e) { ok(false, 'pointermove 抛错: ' + e.message); } });
keyFns.forEach(f => { try { f({ code: 'Escape', preventDefault() {} }); } catch (e) { ok(false, 'Escape 抛错: ' + e.message); } });
frames(60, 50);
ok(!/NaN/.test(JSON.stringify(run('camera.position'))) && !/NaN/.test(JSON.stringify(run('curLook'))), '全程结束后相机/注视点无 NaN');
ok(run('renderer').calls > 100, '渲染循环持续运行');

/* ============================ 5. 交付物 ============================ */
const audioDir = path.join(__dirname, 'audio');
const mp3 = fs.existsSync(audioDir) ? fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).sort() : [];
eq(mp3.length, POEM.length + 2, 'audio 文件数 = 句数+2');
['00.mp3', '01.mp3', '02.mp3', '03.mp3'].forEach(f => ok(mp3.indexOf(f) >= 0, 'audio 含 ' + f));
ok(mp3.every(f => fs.statSync(path.join(audioDir, f)).size > 800), 'audio 均为有效 MP3（>800B）');
ok(html.indexOf('class="galLink" href="../index.html"') > 0, '封面含返回诗集目录链接');
ok(html.indexOf('id="btnCover"') > 0 && html.split('galLink').length >= 3, '终章含诗集目录链接');
ok(html.indexOf('id="btnAuto" class="on">自动游览 · 开') > 0, '自动游览按钮默认开');
ok(/--gold:#3a4048/.test(html), '强调色为 #3a4048');
ok(!/0x05070d|#05070d/.test(html), '无夜宴深色残留');
ok(!/将进酒|万古愁|太白/.test(html), '无参考实现字样残留');
ok(/<title>[^<]*蝉/.test(html), '标题为《蝉》');

console.log(`\n${fails ? '✗' : '✓'} smoke.test.js: ${checks - fails}/${checks} 项通过` + (fails ? `，${fails} 项失败` : ''));
process.exit(fails ? 1 : 0);
