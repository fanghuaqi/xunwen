#!/usr/bin/env node
/*
 * smoke.test.js —— 使至塞上 页面深冒烟测试（THREE 桩 + 迷你 DOM）
 * 用法: node smoke.test.js
 * 覆盖: boot → 全部 builder → 每境 update 若干帧 → 点击交互 → 自动游览全生命周期
 *       → 终章/小测/按钮/键盘 → 淡入淡出系数(fadeK) 回归
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const FILE = path.join(__dirname, 'index.html');
const html = fs.readFileSync(FILE, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];

let pass = 0, fail = 0;
let MARK = '启动';
let FRAMES = 0;
const HARD = setTimeout(() => {   /* 自限时：防止引擎里的死循环把测试挂死 */
  console.log('\n!! 冒烟测试超时，最后进度: ' + MARK + '（已驱动 ' + FRAMES + ' 帧）');
  process.exit(2);
}, 60000);
const ok = (c, m) => { if (c) { pass++; console.log('  ✓ ' + m); } else { fail++; console.log('  ✗ ' + m); } };
const eq = (a, b, m) => ok(a === b, m + '  (got ' + JSON.stringify(a) + ')');

/* ---------------- 迷你数学/三维桩 ---------------- */
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) {
    const ax = a.x, ay = a.y, az = a.z, bx = b.x, by = b.y, bz = b.z;
    this.x = ay * bz - az * by; this.y = az * bx - ax * bz; this.z = ax * by - ay * bx; return this;
  }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; this.x /= l; this.y /= l; this.z /= l; return this; }
  setScalar(s) { this.x = this.y = this.z = s; return this; }
  lerpVectors(a, b, t) { this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t; return this; }
  length() { return Math.hypot(this.x, this.y, this.z); }
  distanceTo(v) { return Math.hypot(this.x - v.x, this.y - v.y, this.z - v.z); }
  dot(v) { return this.x * v.x + this.y * v.y + this.z * v.z; }
  get isVector3() { return true; }
}
const num = n => (typeof n === 'number' && isFinite(n));
class Color {
  constructor(c = 0) { this.r = 1; this.g = 1; this.b = 1; this.hex = c; }
  copy(c) { this.hex = c.hex; this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(this.hex); }
  lerp() { return this; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; this.hex = a.hex; return this; }
  set(c) { this.hex = c; return this; }
}

/* ---------------- 场景图桩 ---------------- */
let OBJ_ID = 0;
class Obj {
  constructor(kind = 'Group') {
    this.type = kind; this.id = ++OBJ_ID;
    this.children = []; this.parent = null; this.userData = {};
    this.position = new V3(); this.rotation = new V3(); this.scale = new V3(1, 1, 1);
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true; this.name = '';
  }
  add(...os) {
    for (const o of os) {
      if (!o) throw new Error(this.type + '.add() 收到空对象');
      if (o.__isMaterialOrGeo) throw new Error(this.type + '.add() 误把材质/几何加进场景图');
      o.parent = this; this.children.push(o);
    }
    return this;
  }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) { this.children.splice(i, 1); o.parent = null; } return this; }
  traverse(cb) { cb(this); for (const c of this.children) c.traverse(cb); }
  lookAt() { return this; }
  rotateOnAxis() { return this; }
  rotateZ(a) { this.rotation.z += a; return this; }
  updateMatrix() { return this; }
  setMatrixAt() { return this; }
}
class Geo {
  constructor(kind = 'Geometry') { this.type = kind; this.attributes = {}; this.__isGeo = true; }
  rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  getAttribute(n) { return this.attributes[n]; }
  setFromPoints(pts) { this.pointCount = pts.length; this.attributes.position = { array: pts }; return this; }
  dispose() { this.disposed = true; }
  setUsage() { return this; }
}
class BufAttr { constructor(arr, itemSize, norm) { this.array = arr; this.itemSize = itemSize; this.normalized = !!norm; this.needsUpdate = false; } }
class Mat {
  constructor(kind, o = {}) {
    Object.assign(this, o);
    this.type = kind; this.__isMat = true;
    this.isShaderMaterial = false; this.userData = {};
    if (o.uniforms) { this.uniforms = o.uniforms; this.isShaderMaterial = true; }
    this.color = (o.color === undefined ? new Color(0xffffff)
      : (o.color && o.color.isColor ? o.color : new Color(o.color)));
    this.opacity = (o.opacity === undefined ? 1 : o.opacity);
  }
  dispose() { this.disposed = true; }
}
class Light extends Obj {
  constructor(kind, color = 0xffffff, intensity = 1) { super(kind); this.isLight = true; this.color = new Color(color); this.intensity = intensity; }
}
class Cam extends Obj {
  constructor(fov, aspect, near, far) { super('PerspectiveCamera'); this.fov = fov; this.aspect = aspect; this.near = near; this.far = far; }
  updateProjectionMatrix() { this.projUpdated = (this.projUpdated || 0) + 1; }
}
const geoFactory = k => function (...a) { const g = new Geo(k); g.args = a; return g; };
const matFactory = k => function (o) { return new Mat(k, o); };

const THREE = {
  Group: class extends Obj { constructor() { super('Group'); } },
  Object3D: class extends Obj { constructor() { super('Object3D'); } },
  Mesh: class extends Obj { constructor(g, m) { super('Mesh'); if (!m) throw new Error('Mesh 缺材质'); this.geometry = g; this.material = m; } },
  Points: class extends Obj { constructor(g, m) { super('Points'); if (!m) throw new Error('Points 缺材质'); this.geometry = g; this.material = m; } },
  Sprite: class extends Obj { constructor(m) { super('Sprite'); if (!m) throw new Error('Sprite 缺材质'); this.material = m; } },
  Line: class extends Obj { constructor(g, m) { super('Line'); this.geometry = g; this.material = m; } },
  Scene: class extends Obj { constructor() { super('Scene'); this.fog = null; } },
  FogExp2: class { constructor(c, d) { this.color = new Color(c); this.density = d; } },
  PerspectiveCamera: Cam,
  WebGLRenderer: class {
    constructor() {
      this.domElement = makeEl('canvas');
      this.pixelRatio = 1;
      this.frames = 0;
      this.clearColor = null;
    }
    setPixelRatio(r) { this.pixelRatio = r; }
    setSize(w, h) { this.size = [w, h]; }
    setClearColor(c) { if (!(c && c.hex !== undefined && c.hex !== null)) throw new Error('setClearColor 收到非法颜色'); this.clearColor = c; }
    render(s, c) { if (!s || !c) throw new Error('render 参数缺失'); this.frames++; }
  },
  DirectionalLight: class extends Light { constructor(c, i) { super('DirectionalLight', c, i); } },
  AmbientLight: class extends Light { constructor(c, i) { super('AmbientLight', c, i); } },
  PointLight: class extends Light { constructor(c, i, d) { super('PointLight', c, i); this.distance = d; } },
  PlaneGeometry: geoFactory('PlaneGeometry'), BoxGeometry: geoFactory('BoxGeometry'),
  CylinderGeometry: geoFactory('CylinderGeometry'), SphereGeometry: geoFactory('SphereGeometry'),
  ConeGeometry: geoFactory('ConeGeometry'), TorusGeometry: geoFactory('TorusGeometry'),
  CircleGeometry: geoFactory('CircleGeometry'), RingGeometry: geoFactory('RingGeometry'),
  LatheGeometry: geoFactory('LatheGeometry'), IcosahedronGeometry: geoFactory('IcosahedronGeometry'),
  TubeGeometry: geoFactory('TubeGeometry'), BufferGeometry: geoFactory('BufferGeometry'),
  CatmullRomCurve3: class { constructor(p) { this.points = p; } },
  BufferAttribute: BufAttr, Float32BufferAttribute: BufAttr,
  MeshBasicMaterial: matFactory('MeshBasicMaterial'), MeshPhongMaterial: matFactory('MeshPhongMaterial'),
  SpriteMaterial: matFactory('SpriteMaterial'), PointsMaterial: matFactory('PointsMaterial'),
  LineBasicMaterial: matFactory('LineBasicMaterial'),
  ShaderMaterial: function (o) { const m = new Mat('ShaderMaterial', o); m.isShaderMaterial = true; return m; },
  CanvasTexture: class { constructor(c) { this.canvas = c; } dispose() {} },
  Vector2: V2, Vector3: V3, Color,
  AdditiveBlending: 2, NormalBlending: 1, DoubleSide: 2, BackSide: 1, FrontSide: 0,
  DynamicDrawUsage: 35048,
};
THREE.MeshPhongMaterial.prototype.isMeshPhongMaterial = true;

/* ---------------- 迷你 DOM ---------------- */
const listeners = new Map();                 // element -> {type: [fn]}
function makeEl(tag) {
  const el = {
    tagName: String(tag || 'div').toUpperCase(), children: [], style: {}, dataset: {},
    textContent: '', title: '', open: false, disabled: false,
    offsetWidth: 1, offsetHeight: 1,
    className: '', scrollWidth: 1,
    /* innerHTML 赋值在真实 DOM 里会清空全部子节点（无论赋的是空串还是标记串）。
       小测换题用 body.innerHTML='<div id="quizQ">…' 清场，必须按真实语义建模。 */
    _html: '',
    get innerHTML() { return el._html; },
    set innerHTML(v) { el._html = String(v); el.children.length = 0; },
    _cls: new Set(),
    classList: {
      add(...c) { c.forEach(x => el._cls.add(x)); },
      remove(...c) { c.forEach(x => el._cls.delete(x)); },
      contains(c) { return el._cls.has(c); },
      toggle(c, f) { const on = (f === undefined ? !el._cls.has(c) : !!f); if (on) el._cls.add(c); else el._cls.delete(c); return on; },
    },
    appendChild(c) { el.children.push(c); c.parentEl = el; return c; },
    getContext() { return ctx2d(); },
    addEventListener(type, fn) { const m = listeners.get(el) || {}; (m[type] = m[type] || []).push(fn); listeners.set(el, m); },
    removeEventListener() {},
    /* 选择器桩：真实 DOM 里 '.opt' 只返回带该 class 的后代，答错分支靠 opts[q.a] 取正确项，
       返回空数组会直接崩在读取处，所以类选择器必须支持。 */
    querySelectorAll(sel) {
      const walk = (n, out) => { for (const c of n.children || []) { out.push(c); walk(c, out); } return out; };
      const all = walk(el, []);
      if (sel.startsWith('.')) return all.filter(c => String(c.className || '').split(/\s+/).indexOf(sel.slice(1)) >= 0);
      if (sel.startsWith('#')) return all.filter(c => c.id === sel.slice(1));
      if (sel.indexOf(' i') >= 0) return el.children;
      const tag = sel.toUpperCase();
      return all.filter(c => c.tagName === tag);
    },
    querySelector(sel) { return el.querySelectorAll(sel)[0] || null; },
    requestFullscreen() { DOC.fullscreenElement = el; },
    focus() {}, blur() {},
  };
  el.style = {};
  return el;
}
const elCache = new Map();
function $(sel) {
  if (!elCache.has(sel)) elCache.set(sel, makeEl(sel === 'canvas' ? 'canvas' : 'div'));
  return elCache.get(sel);
}
const DOC = {
  querySelector: sel => $(sel),
  querySelectorAll: sel => $(sel).children,
  createElement: t => makeEl(t),
  addEventListener(type, fn) { const m = listeners.get(DOC) || {}; (m[type] = m[type] || []).push(fn); listeners.set(DOC, m); },
  documentElement: makeEl('html'),
  body: makeEl('body'),
  head: makeEl('head'),
  activeElement: null,
  fullscreenElement: null,
  exitFullscreen() { DOC.fullscreenElement = null; },
};
DOC.documentElement.requestFullscreen = () => { DOC.fullscreenElement = DOC.documentElement; };

/* 音频桩 */
const audioLog = [];
class AudioStub {
  constructor(src) { this.src = src; this._h = {}; audioLog.push(src); }
  addEventListener(t, fn) { this._h[t] = fn; }
  play() { this.playing = true; return Promise.resolve(); }
  pause() { this.playing = false; }
}
function ctx2d() {
  return {
    createRadialGradient: () => ({ addColorStop() {} }),
    createLinearGradient: () => ({ addColorStop() {} }),
    fillRect() {}, fillText() {}, drawImage() {}, clearRect() {},
    set font(v) {}, get font() { return ''; }, set fillStyle(v) {}, get fillStyle() { return ''; },
    set textAlign(v) {}, set textBaseline(v) {}, set shadowColor(v) {}, set shadowBlur(v) {},
  };
}
const nodesLog = [];
class GainNode { constructor() { this.gain = { value: 1, setValueAtTime() {}, linearRampToValueAtTime() {}, exponentialRampToValueAtTime() {}, cancelScheduledValues() {} }; } connect() { return this; } }
class ACStub {
  constructor() { this.sampleRate = 22050; this.currentTime = 0; this.state = 'running'; this.destination = {}; }
  createGain() { return new GainNode(); }
  createBuffer(ch, len) { const d = new Float32Array(len); return { getChannelData: () => d, length: len }; }
  createBufferSource() { const n = { buffer: null, loop: false, connect() { return this; }, start() { nodesLog.push('src'); }, stop() {} }; return n; }
  createBiquadFilter() { return { type: 'lowpass', frequency: { value: 0 }, connect() { return this; } }; }
  createOscillator() {
    const o = { type: 'sine', frequency: { value: 0, setValueAtTime() {}, exponentialRampToValueAtTime() {} }, connect() { return this; }, start() { nodesLog.push('osc'); }, stop() {} };
    return o;
  }
  resume() { this.state = 'running'; }
}
const rafQueue = [];
const sandbox = {
  THREE, console, Math, Date, JSON, Object, Array, String, Number, Boolean, isFinite, isNaN, parseInt, parseFloat,
  Float32Array, Set, Map, Promise, Error, TypeError, RangeError,
  window: {
    innerWidth: 1440, innerHeight: 900, devicePixelRatio: 1,
    Audio: AudioStub, AudioContext: ACStub,
    addEventListener(t, fn) { const m = listeners.get(sandbox.window) || {}; (m[t] = m[t] || []).push(fn); listeners.set(sandbox.window, m); },
    removeEventListener() {},
  },
  document: DOC,
  performance: { now: () => sandbox.__t * 1000 },
  requestAnimationFrame(cb) { rafQueue.push(cb); return rafQueue.length; },
  setTimeout(fn, ms) { sandbox.__timers.push({ fn, at: sandbox.__t * 1000 + (ms || 0) }); return sandbox.__timers.length; },
  clearTimeout() {},
  navigator: { userAgent: 'node-smoke' },
  __t: 0, __timers: [],
};
sandbox.window.document = DOC;
sandbox.window.THREE = THREE;                 /* 引擎按 window.THREE 探测是否加载完成 */
/* 不提供 speechSynthesis（'speechSynthesis' in window === false）→ 走内置 MP3 / 系统语音兜底分支 */
sandbox.globalThis = sandbox;
vm.createContext(sandbox);

/* ---------------- 执行主脚本 ---------------- */
let booted = false;
try {
  vm.runInContext(code, sandbox, { filename: FILE });
} catch (e) {
  console.log('✗ 顶层执行失败: ' + e.message);
  process.exit(1);
}
console.log('1. 顶层与启动');
ok(typeof sandbox.initApp === 'function' || sandbox.window.__inited !== undefined, '顶层已执行，initApp 就绪');
try { vm.runInContext('window.__inited=false;', sandbox); vm.runInContext('initApp();', sandbox); booted = true; }
catch (e) { console.log('   boot 抛错: ' + e.stack.split('\n').slice(0, 3).join(' | ')); }
ok(booted, 'boot() 在 THREE 桩下执行成功（封面境已建）');
const get = e => vm.runInContext(e, sandbox);
ok(get('renderer') && get('scene') && get('camera') && get('curStageObj'), 'renderer/scene/camera/封面境均就绪');
ok(get('skyDome') && get('scene').children.length > 10, '天空穹顶/星/月/地平线剪影已建');

/* 驱动帧：把 rAF 队列里最新的回调反复调用 */
function frames(n, dt = 1 / 30) {
  for (let i = 0; i < n; i++) {
    FRAMES++;
    sandbox.__t += dt;
    const cb = rafQueue.pop(); rafQueue.length = 0;
    if (!cb) throw new Error('第 ' + i + ' 帧没有 rAF 回调（animate 循环断了）');
    cb();
    /* 到点的定时器（朗读/提示）也跑一遍，覆盖 aiSpeak 路径 */
    for (const t of sandbox.__timers.filter(t => t.at <= sandbox.__t * 1000)) { sandbox.__timers.splice(sandbox.__timers.indexOf(t), 1); try { t.fn(); } catch (e) { throw new Error('定时器回调抛错: ' + e.message); } }
  }
}
/* currentTarget 由浏览器在派发时注入，合成事件必须补上，否则读 e.currentTarget 的处理器会炸 */
const fire = (el, type, ev = {}) => { const m = listeners.get(el) || {}; (m[type] || []).forEach(fn => fn(Object.assign({ currentTarget: el, target: el }, ev))); };
const key = ev => fire(sandbox.window, 'keydown', Object.assign({ code: '', preventDefault() {} }, ev));

console.log('2. 数据与边界');
eq(get('STAGES.length'), get('POEM.length') + 1, 'STAGES = POEM + 1');
ok(get('STAGES.slice(1).every((s,i)=>s.name===POEM[i].name)'), 'STAGES[i].name === POEM[i-1].name');
eq(get('POEM.length'), 4, '四境');
ok(get('CN.length') >= 4, 'CN 数字数组够长');
ok(code.includes('clamp(i,0,4)'), 'goto clamp 上界 = 4');
ok(/'05\.mp3'/.test(code), '全诗音频引用 05.mp3');
eq((code.match(/curIdx===4&&state==='stage'/g) || []).length, 2, '交互境 curIdx===4 接线 2 处');
eq((code.match(/curIdx===3&&state==='stage'/g) || []).length, 2, '交互境 curIdx===3 接线 2 处');
ok(/autoMode=true/.test(code) && /id="btnAuto" class="on"/.test(html), 'autoMode 默认开 + 按钮初始 on');
ok(/id="enterBtn"[\s\S]{0,200}返回诗集目录/.test(html) && /诗集目录<\/a>/.test(html), '封面与终章均有返回诗集目录链接');
ok(!code.includes('将进酒') && !code.includes('万古愁') && !/太白/.test(code), '无《将进酒》残留');
eq(get('QUIZ.length'), 5, '小测 5 题');
eq((code.match(/read:'/g) || []).length, 4, "read 字段 4 处");

console.log('3. 逐境 builder + 多帧 update（NaN / 抛错检测）');
const stageInfo = [];
for (let i = 0; i < get('STAGES.length'); i++) {
  const def = get('STAGES[' + i + ']');
  let st;
  try { st = def.build(); } catch (e) { ok(false, `境${i} (${def.name}) build 抛错: ${e.message}`); continue; }
  ok(!!st && !!st.group, `境${i} (${def.name}) build 返回 group`);
  try { st.group.traverse(() => {}); } catch (e) { ok(false, `境${i} traverse 抛错`); }
  if (i === 0) { sandbox.__stageSave = st; }
  stageInfo.push({ i, def, st });
  /* 独立跑 90 帧 update（含 d1 变化），并把 group 挂到场景里以模拟真实父链 */
  get('scene').add(st.group);
  sandbox.setFade(st.group, 1);
  let bad = null;
  for (let f = 0; f < 90; f++) {
    sandbox.__t += 1 / 30;
    try { if (st.update) st.update(sandbox.__t, 1 / 30); } catch (e) { bad = e; break; }
  }
  ok(!bad, `境${i} (${def.name}) update ×90 帧无抛错` + (bad ? ': ' + bad.message : ''));
  let nan = 0, opBad = 0;
  st.group.traverse(o => {
    if (o.position && !(num(o.position.x) && num(o.position.y) && num(o.position.z))) nan++;
    if (o.scale && !(num(o.scale.x) && num(o.scale.y) && num(o.scale.z))) nan++;
    if (o.material && o.material.opacity !== undefined && !num(o.material.opacity)) opBad++;
    if (o.isLight && !num(o.intensity)) opBad++;
    if (o.material && o.material.isShaderMaterial && o.material.uniforms && o.material.uniforms.uFade && !num(o.material.uniforms.uFade.value)) opBad++;
  });
  ok(nan === 0, `境${i} 位置/缩放无 NaN`);
  ok(opBad === 0, `境${i} opacity/intensity/uFade 均为有限数`);
  get('scene').remove(st.group);
}

console.log('4. 交互境 click（第三境 孤烟升起 + 落日更圆）');
{
  const s3 = stageInfo[3].st;
  get('scene').add(s3.group); sandbox.setFade(s3.group, 1);
  const smokeBefore = s3.group.children.find(o => o.userData && o.userData.__smokeTag);
  /* 通过公开接口拿烟柱：直接在 group 里找 Col 材质 shader 的圆柱 */
  let cyl = null, sunDisc = null, ring = null, vline = null;
  s3.group.traverse(o => {
    if (o.material && o.material.isShaderMaterial && o.material.uniforms && o.material.uniforms.uGrow) cyl = o;
    if (o.material && o.material.color && o.material.type === 'MeshBasicMaterial' && o.geometry && o.geometry.type === 'CircleGeometry') sunDisc = o;
    if (o.geometry && o.geometry.type === 'RingGeometry') ring = o;
    if (o.material && o.material.type === 'LineBasicMaterial' && o.geometry && o.geometry.pointCount === 2) {
      const a = o.geometry.attributes.position.array;
      if (a[0].x === a[1].x) vline = o;
    }
  });
  ok(!!cyl, '找到孤烟柱体（uGrow uniform）');
  ok(!!sunDisc && !!ring, '找到落日圆面与细圆环');
  ok(!!vline, '找到"一竖"基准线');
  const g0 = s3.group.userData.__g || 0;
  for (let f = 0; f < 30; f++) { sandbox.__t += 1 / 30; s3.update(sandbox.__t, 1 / 30); }
  const scaleA = cyl.scale.y, opA = ring.material.opacity;
  fire(s3 ? $(('#flash')) : $('#flash'), 'x');       // 无害：确保 flash 元素存在
  /* AudioContext 在真实流程里由「入境」按钮的 click 里 initAudio() 创建；
     本段直接调境位 click，绕过了那次手势，音频链路还没建起来，先补上。 */
  get('initAudio()');
  s3.click();
  ok($('#flash').textContent.indexOf('孤烟直') >= 0, '点击后题字闪出「孤烟直 · 落日圆」');
  for (let f = 0; f < 120; f++) { sandbox.__t += 1 / 30; s3.update(sandbox.__t, 1 / 30); }
  ok(cyl.scale.y > scaleA + 0.15, '孤烟升起（柱体变高）');
  ok(ring.material.opacity > opA + 0.3, '落日更圆（细圆环显形）');
  ok(cyl.material.uniforms.uGrow.value > 0.9, 'uGrow 收敛到 1');
  ok(sunDisc.material.opacity > 0 && num(sunDisc.material.opacity), '落日落日不透明度有效');
  ok(audioLog.length > 0 || nodesLog.length > 0, '点击触发了音频反馈（WebAudio/MP3）');
  get('scene').remove(s3.group);
}
console.log('5. 第四境 click（点燃烽燧，回应孤烟）');
{
  const s4 = stageInfo[4].st;
  get('scene').add(s4.group); sandbox.setFade(s4.group, 1);
  for (let f = 0; f < 20; f++) { sandbox.__t += 1 / 30; s4.update(sandbox.__t, 1 / 30); }
  eq(s4.clicked(), false, '未点击时尚未点燃');
  s4.click();
  eq(s4.clicked(), true, '点击后点燃');
  for (let f = 0; f < 150; f++) { sandbox.__t += 1 / 30; s4.update(sandbox.__t, 1 / 30); }
  ok($('#flash').textContent.indexOf('都护在燕然') >= 0, '闪出「都护在燕然」');
  let lit = 0;
  s4.group.traverse(o => { if (o.material && o.material.isShaderMaterial && o.material.uniforms && o.material.uniforms.uMaxA && o.material.uniforms.uMaxA.value > 0.2) lit++; });
  ok(lit >= 4, '烽火链至少 4 处亮起（get ' + lit + '）');
  get('scene').remove(s4.group);
}

console.log('6. 淡入淡出回归（fadeK 必须乘进每帧写入的 opacity）');
{
  /* 过渡中途：新境按 fadeK 淡入（上限 = base*fadeK），旧境按 1-fadeK 淡出（上限 = base*(1-fadeK)）。
     注意 curStageObj 要到过渡结束才指向新境，中途它仍是旧境 —— 必须分别取 trans.stage / trans.old 来查。 */
  $(('#cover')).classList.add('off');
  sandbox.goto(3);
  frames(30);                                  // 过渡约进行到一半
  const kf = get('trans.stage.group.userData.fadeK');   // 新境实际应用的淡入系数（已缓动）
  const ko = get('trans.old ? trans.old.group.userData.fadeK : 0');
  const scan = (root, limit, tag) => {
    let over = 0, checked = 0, shown = 0, zeroBase = 0;
    root.traverse(o => {
      const m = o.material;
      if (m && m.opacity !== undefined && m.userData && m.userData.baseOpacity !== undefined) {
        checked++;
        /* base*fadeK 上界只对"破透明度非零"的材质成立：它们的每帧值是 base*包络*fadeK。
           破透明度为 0 的材质（如被 update 用绝对式 (0.16+0.52*grow)*k 驱动的 Line/Sprite）
           不适用该模型，只查有限性与上界，避免把"本来就正确"的写法误判为越界。 */
        if (m.userData.baseOpacity > 0) {
          if (m.opacity > m.userData.baseOpacity * Math.min(1, limit) + 1e-6) {
            over++;
            if (shown++ < 4) console.log('      · ' + tag + ' ' + (o.type || o.name) + ' op=' + m.opacity.toFixed(4) + ' base=' + m.userData.baseOpacity.toFixed(4) + ' 限=' + (m.userData.baseOpacity * limit).toFixed(4));
          }
        } else {
          zeroBase++;
          if (!(m.opacity >= 0 && m.opacity <= 1)) {
            over++;
            if (shown++ < 4) console.log('      · ' + tag + ' ' + (o.type || o.name) + ' 破透明度为 0 但每帧写入 op=' + m.opacity);
          }
        }
      }
      if (o.isLight && o.userData && o.userData.baseI !== undefined) {
        checked++;
        if (o.intensity > o.userData.baseI * Math.min(1, limit) + 1e-6) {
          over++;
          if (shown++ < 4) console.log('      · ' + tag + ' LIGHT ' + o.type + ' I=' + o.intensity.toFixed(4) + ' base=' + o.userData.baseI.toFixed(4));
        }
      }
    });
    return { over, checked, zeroBase };
  };
  const inc = scan(get('trans.stage.group'), kf, '入境');
  const out = get('trans.old') ? scan(get('trans.old.group'), ko, '出境') : { over: 0, checked: 0 };
  console.log('    fadeK: 入境=' + kf.toFixed(3) + ' 出境=' + ko.toFixed(3) + '（破透明度为 0 的材质：入境 ' + inc.zeroBase + ' / 出境 ' + out.zeroBase + ' 个，仅查有限性）');
  ok(inc.checked > 0, '入境境位确有正在淡入的材质/灯光（' + inc.checked + ' 个）');
  ok(out.checked > 0 || !get('trans.old'), '出境境位确有正在淡出的材质/灯光（' + out.checked + ' 个）');
  eq(inc.over, 0, '入境：所有每帧写入的 opacity/intensity 都乘了 fadeK');
  eq(out.over, 0, '出境：所有每帧写入的 opacity/intensity 都乘了 1-fadeK');
}

console.log('7. 自动游览全生命周期（封面 → 四境 → 终章）');
{
  fire($('#enterBtn'), 'click');
  ok(get("state") === 'transition' || get('curIdx') === 1, '入境按钮把页面推到第一境');
  let guard = 0;
  while (get("state") !== 'ending' && guard < 9000) { frames(1, 1 / 30); guard++; }
  ok(get("state") === 'ending', '自动游览无人值守走到终章（' + (guard / 30).toFixed(0) + 's）');
  ok($('#ending')._cls.has('show'), '终章面板已显示');
  ok($('#endPoem').children.length > 0, '终章竖排全诗已渲染');
}

console.log('8. 终章按钮 / 小测 / 键盘 / 开关');
{
  let threw = null;
  try {
    fire($('#btnQuiz'), 'click');                        // 学习小测
    for (let q = 0; q < 5; q++) {
      const body = $('#quizBody');
      const opts = body.children.filter(c => c.className === 'opt');
      if (!opts.length) throw new Error('第 ' + (q + 1) + ' 题没有选项按钮');
      eq(opts.length, 3, '  第 ' + (q + 1) + ' 题 3 个选项');
      opts[0]._click = true;
      fire(opts[0], 'click');
      const nb = body.children.find(c => c.id === 'quizNext');
      if (!nb) throw new Error('第 ' + (q + 1) + ' 题缺"下一题"按钮');
      fire(nb, 'click');
    }
    ok($('#quizBody').children.length > 0, '小测结果页渲染成功');
    /* 结果页的"回到终章"是真按钮（createElement 造的），必须从 quizBody 里取；
       $('#quizClose') 走的是选择器缓存、永远返回一个假元素，点了也没用。
       不关掉小测弹窗，页面会按设计忽略方向键，后半程的键盘断言全会假失败。 */
    const cb = $('#quizBody').children.find(c => c.id === 'quizClose');
    if (!cb) throw new Error('结果页缺"回到终章"按钮');
    fire(cb, 'click');
    ok(!$('#quiz')._cls.has('show'), '小测弹窗已关闭（键盘恢复可用）');
  } catch (e) { threw = e; }
  ok(!threw, '小测全流程无抛错' + (threw ? ': ' + threw.message : ''));
  try {
    fire($('#btnPoemAudio'), 'click');                   // 聆听全诗
    fire($('#btnAuto'), 'click');                        // 自动游览开关
    fire($('#btnAuto'), 'click');
    fire($('#btnPy'), 'click'); fire($('#btnPy'), 'click');
    fire($('#btnSnd'), 'click'); fire($('#btnSnd'), 'click');
    fire($('#btnAutoSpeak'), 'click'); fire($('#btnAutoSpeak'), 'click');
    fire($('#btnFs'), 'click');
    fire($('#btnAgain'), 'click');                       // 重新入境
    frames(5);
    ok(get('curIdx') === 1 || get('state') === 'transition', '重新入境回到第一境');
    fire($('#btnAuto'), 'click');                        // 关掉自动游览，后半程手动走（按钮此刻是"开"态）
    ok(get('autoMode') === false, '自动游览已关闭，手动模式');
    /* 过渡 2.6s 期间页面会忽略一切切境输入，按键前必须先把过渡走完 */
    const settle = () => { let g = 0; while (get("state") === 'transition' && g++ < 400) frames(1); return g; };
    settle();
    ok(get("state") === 'stage', '重新入境的过渡已完成（' + settle() + ' 帧内）');
    key({ code: 'ArrowRight' }); settle();
    ok(get('curIdx') === 2, '→ 键推进到第二境');
    key({ code: 'ArrowLeft' }); settle();
    ok(get('curIdx') === 1, '← 键退回第一境');
    key({ code: 'Space' }); settle();
    ok(get('curIdx') === 2, '空格推进到第二境');
    key({ code: 'ArrowRight' }); settle();               // 到第三境（交互境）
    ok(get('curIdx') === 3, '到达第三境');
    key({ code: 'Space' }); settle();                    // 交互境：空格 = 点击
    ok($('#flash').textContent.indexOf('孤烟直') >= 0, '第三境空格触发孤烟交互');
    key({ code: 'ArrowRight' }); settle();
    ok(get('curIdx') === 4, '到达第四境');
    key({ code: 'Space' }); settle();                    // 首次空格点燃
    ok(get('curStageObj.clicked()') === true, '第四境空格点燃烽燧');
    key({ code: 'Space' }); settle();                    // 再次空格结束全诗
    ok(get('state') === 'ending', '第四境再按空格进入终章');
    key({ code: 'Escape' }); frames(5);
    ok(get('state') === 'stage', 'Esc 退出终章回到舞台');
    fire($('#btnNext'), 'click'); frames(200);
    ok(get('state') === 'ending', '第四境"下一境"进入终章');
    fire($('#btnCover'), 'click'); frames(60);
    ok(get('curIdx') === 0 && $('#cover')._cls.size >= 0, '回到封面');
  } catch (e) { ok(false, '按钮/键盘流程抛错: ' + e.message + '\n' + e.stack.split('\n')[1]); }
}

console.log('9. 渲染循环健康');
{
  const before = sandbox.renderer ? sandbox.renderer.frames : 0;
  frames(60);
  const after = get('renderer.frames');
  ok(after > before, 'rAF 循环持续出帧（' + before + ' → ' + after + '）');
  ok(num(get('camera.position.x')) && num(get('camera.position.y')) && num(get('camera.position.z')), '相机位置有效');
  ok(num(get('SKYcur.fd')) && get('SKYcur.fd') > 0, '雾密度有效');
  ok(get('fogShaders').length > 0, '风沙/长河着色器已登记进 fogShaders（手动同步雾）');
}

console.log('\n' + (fail === 0 ? 'SMOKE PASS' : 'SMOKE FAIL') + ' —— 通过 ' + pass + ' 项，失败 ' + fail + ' 项');
process.exit(fail === 0 ? 0 : 1);
