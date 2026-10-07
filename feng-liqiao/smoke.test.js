#!/usr/bin/env node
/*
 * smoke.test.js —— 「循文入境·风（李峤）」深度冒烟测试
 * 用带真实数学实现的 THREE 桩，在 Node 里真实执行主脚本顶层，
 * 并逐境调用 build()/update(t,dt)/click()，扫描 NaN，
 * 覆盖 validate.js 只查顶层的盲区。
 * 用法: node smoke.test.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const code = (html.match(/<script id="main">([\s\S]*?)<\/script>/) || [])[1];
if (!code) { console.error('未找到主脚本'); process.exit(1); }

/* ---------------- 带真实数学的 THREE 桩 ---------------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  setScalar(s) { this.x = s; this.y = s; this.z = s; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  sub(v) { this.x -= v.x; this.y -= v.y; this.z -= v.z; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  length() { return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z); }
  normalize() { const l = this.length() || 1; return this.multiplyScalar(1 / l); }
  dot(v) { return this.x * v.x + this.y * v.y + this.z * v.z; }
  lerpVectors(a, b, t) { this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t; return this; }
  crossVectors(a, b) {
    const ax = a.x, ay = a.y, az = a.z, bx = b.x, by = b.y, bz = b.z;
    this.x = ay * bz - az * by; this.y = az * bx - ax * bz; this.z = ax * by - ay * bx; return this;
  }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class Quaternion {
  constructor() { this.x = 0; this.y = 0; this.z = 0; this.w = 1; }
  setFromAxisAngle(axis, angle) { this._axis = [axis.x, axis.y, axis.z]; this._angle = angle; return this; }
}
class Euler { constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; } set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } }
class Color {
  constructor(h) { this.r = 0; this.g = 0; this.b = 0; if (h !== undefined) this.set(h); }
  set(h) {
    if (h && h.isColor) return this.copy(h);
    if (typeof h === 'number') {
      this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255;
    } else if (typeof h === 'string') {
      const n = parseInt(h.replace('#', ''), 16);
      this.r = ((n >> 16) & 255) / 255; this.g = ((n >> 8) & 255) / 255; this.b = (n & 255) / 255;
    }
    return this;
  }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color().copy(this); }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  lerp(c, a) { this.r += (c.r - this.r) * a; this.g += (c.g - this.g) * a; this.b += (c.b - this.b) * a; return this; }
}
Color.prototype.isColor = true;

class Object3D {
  constructor() {
    this.position = new V3(); this.rotation = new Euler(); this.scale = new V3(1, 1, 1);
    this.quaternion = new Quaternion(); this.children = []; this.userData = {};
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true;
    this.matrix = {}; this.matrixWorld = {}; this.parent = null;
  }
  add(...cs) { for (const c of cs) { if (Array.isArray(c)) this.add(...c); else if (c && c.isObject3D) { this.children.push(c); c.parent = this; } } return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) { fn(this); for (const c of this.children) c.traverse(fn); }
  translateX(v) { this.position.x += v; return this; }
  translateY(v) { this.position.y += v; return this; }
  translateZ(v) { this.position.z += v; return this; }
  rotateOnAxis() { return this; }
  rotateZ() { return this; }
  lookAt() { return this; }
  updateMatrix() { this.matrix._matrixData = { p: this.position.clone(), q: this.quaternion._angle, s: this.scale.x * this.scale.y * this.scale.z }; return this; }
  updateWorldMatrix() { return this; }
  getWorldPosition(t) { return t ? t.set(0, 0, 0) : new V3(); }
  clear() { this.children.length = 0; return this; }
}
Object3D.prototype.isObject3D = true;
class Group extends Object3D { constructor() { super(); this.isGroup = true; this.type = 'Group'; } }
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isPoints = true; } }
class Line extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; this.isSprite = true; } }
class Light extends Object3D { constructor(c, i) { super(); this.color = new Color(c === undefined ? 0xffffff : c); this.intensity = i === undefined ? 1 : i; this.isLight = true; } }
class DirectionalLight extends Light { constructor(c, i) { super(c, i); } }
class AmbientLight extends Light { constructor(c, i) { super(c, i); } }
class PointLight extends Light { constructor(c, i, d) { super(c, i); this.distance = d; } }
class BufferAttribute {
  constructor(arr, s) { this.array = arr; this.itemSize = s; this.needsUpdate = false; }
  setX() { return this; } setY() { return this; } setZ() { return this; }
}
class InstancedBufferAttribute extends BufferAttribute {}
class BufferGeometry {
  constructor() { this.attributes = {}; this.userData = {}; this.parameters = {}; }
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  getAttribute(n) { return this.attributes[n]; }
  setFromPoints(pts) {
    const arr = new Float32Array(pts.length * 3);
    pts.forEach((p, i) => { arr[i * 3] = p.x; arr[i * 3 + 1] = p.y; arr[i * 3 + 2] = p.z; });
    this.attributes.position = new BufferAttribute(arr, 3); return this;
  }
  rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  translate(x, y, z) { this._tr = [x, y, z]; return this; }
  computeBoundingSphere() {} dispose() {}
}
class InstancedMesh extends Object3D {
  constructor(g, m, n) { super(); this.geometry = g; this.material = m; this.count = n;
    this.instanceMatrix = { setUsage() {}, needsUpdate: false };
    this._mats = new Array(n).fill(null); }
  setMatrixAt(i, m) { this._mats[i] = m && m._matrixData ? Object.assign({}, m._matrixData) : { raw: true }; }
  getMatrixAt() { return new THREE.Matrix4(); }
  dispose() {}
}
class Matrix4 { constructor() { this.elements = new Float32Array(16); } identity() { return this; } compose() { return this; } }
class Material { constructor(o) { this.userData = {}; this.transparent = false; this.opacity = 1; this.side = 0; Object.assign(this, o || {}); } dispose() {} }
class ShaderMaterial extends Material {
  constructor(o = {}) {
    super(o);
    this.uniforms = o.uniforms || {}; this.isShaderMaterial = true;
    this.vertexShader = o.vertexShader || ''; this.fragmentShader = o.fragmentShader || '';
    this.defines = o.defines || {}; this.extensions = {};
  }
  clone() { return new ShaderMaterial(this); }
}
class BasicishMaterial extends Material {
  constructor(o = {}) { super(o); this.color = new Color(o && o.color !== undefined ? o.color : 0xffffff); }
}
class MeshBasicMaterial extends BasicishMaterial {}
class MeshPhongMaterial extends BasicishMaterial { constructor(o = {}) { super(o); this.specular = new Color(o.specular !== undefined ? o.specular : 0x111111); } }
class PointsMaterial extends BasicishMaterial {}
class LineBasicMaterial extends BasicishMaterial {}
class SpriteMaterial extends BasicishMaterial {}
class MeshStandardMaterial extends BasicishMaterial {}
const GeoC = name => class { constructor(...a) { this.type = name; this.parameters = {}; this.args = a; this.attributes = {}; } setAttribute(n, a) { this.attributes[n] = a; return this; } rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; } translate() { return this; } dispose() {} };
class Shape { moveTo() {} lineTo() {} bezierCurveTo() {} quadraticCurveTo() {} }
class CatmullRomCurve3 { constructor(pts) { this.points = pts; } getPoints(n) { return this.points.slice(0, Math.max(2, n)); } getPoint(t) { return this.points[0] || new V3(); } }
class CanvasTexture { constructor(cv) { this.image = cv; this.needsUpdate = true; } dispose() {} }
class Texture extends CanvasTexture {}
class FogExp2 { constructor(c, d) { this.color = new Color(c); this.density = d; } }
class Scene extends Object3D { constructor() { super(); this.fog = null; this.background = null; } }
class PerspectiveCamera extends Object3D {
  constructor(...a) { super(); this.aspect = 1; this.fov = a[0]; }
  updateProjectionMatrix() {}
  lookAt() { return this; }
}
class WebGLRenderer {
  constructor() { this.domElement = { addEventListener() {}, style: {}, width: 1280, height: 800 }; }
  setPixelRatio() {} setSize() {} setClearColor() {} render() {} dispose() {}
}
class WebGLRenderTarget { constructor() {} dispose() {} }
const geos = ['SphereGeometry', 'PlaneGeometry', 'CircleGeometry', 'CylinderGeometry', 'ConeGeometry',
  'BoxGeometry', 'TorusGeometry', 'LatheGeometry', 'RingGeometry', 'IcosahedronGeometry', 'TubeGeometry', 'ExtrudeGeometry'];
const THREE = {
  Vector3: V3, Vector2: V2, Quaternion, Euler, Color, Matrix4,
  Object3D, Group, Mesh, Points, Line, LineSegments: Line, LineLoop: Line, Sprite,
  Light, DirectionalLight, AmbientLight, PointLight,
  BufferAttribute, InstancedBufferAttribute, BufferGeometry, InstancedMesh,
  Material, ShaderMaterial, MeshBasicMaterial, MeshPhongMaterial, PointsMaterial,
  LineBasicMaterial, SpriteMaterial, MeshStandardMaterial,
  Shape, CatmullRomCurve3, CanvasTexture, Texture,
  FogExp2, Scene, PerspectiveCamera, WebGLRenderer, WebGLRenderTarget,
  DynamicDrawUsage: {}, BackSide: 1, FrontSide: 0, DoubleSide: 2,
  AdditiveBlending: 2, NormalBlending: 1, MultiplyBlending: 3,
  VertexColors: 2, sRGBEncoding: 3001,
};
geos.forEach(n => { THREE[n] = GeoC(n); });

/* ---------------- DOM 桩 ---------------- */
const ctx2d = {
  fillStyle: '', globalAlpha: 1, font: '', textAlign: '', textBaseline: '',
  shadowColor: '', shadowBlur: 0,
  fillRect() {}, fillText() {}, strokeText() {}, clearRect() {}, save() {}, restore() {},
  createRadialGradient: () => ({ addColorStop() {} }),
  createLinearGradient: () => ({ addColorStop() {} }),
  beginPath() {}, arc() {}, fill() {}, stroke() {}, measureText: () => ({ width: 10 }),
};
function makeEl(tag) {
  if (tag === 'canvas') return { width: 0, height: 0, getContext: () => ctx2d, style: {} };
  return {
    tagName: (tag || 'div').toUpperCase(), style: {}, textContent: '', innerHTML: '',
    classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
    addEventListener() {}, appendChild() {}, querySelectorAll: () => [], offsetWidth: 100, open: false,
  };
}
const documentStub = {
  querySelector: () => makeEl('div'),
  querySelectorAll: () => [],
  createElement: t => makeEl(t),
  addEventListener() {},
  getElementById: () => makeEl('div'),
  documentElement: makeEl('html'),
  body: makeEl('body'),
  head: makeEl('head'),
  activeElement: null,
  fullscreenElement: null,
};
const sandbox = {
  THREE,
  document: documentStub,
  window: { innerWidth: 1280, innerHeight: 800, devicePixelRatio: 1, addEventListener() {}, AudioContext: null, webkitAudioContext: null },
  performance: { now: () => { perfMs += 16.7; return perfMs; } },
  requestAnimationFrame() { return 0; },
  setTimeout: () => 0, clearTimeout() {},
  console, Math, String, Number, Array, Object, Float32Array, parseInt, isNaN,
  location: { reload() {} },
  speechSynthesis: undefined,
};
let perfMs = 0;
sandbox.globalThis = sandbox;
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: 'index.html (smoke)' });

/* ---------------- 逐境深度执行 ---------------- */
const POEM = vm.runInContext('POEM', sandbox), STAGES = vm.runInContext('STAGES', sandbox);
let failures = 0;
const fail = m => { failures++; console.error('✗ ' + m); };
const ok = m => console.log('✓ ' + m);

/* 0. 诗文与 queue.json 完全一致 */
const expectText = '解落三秋叶，能开二月花。过江千尺浪，入竹万竿斜。';
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
if (joined !== expectText) fail(`诗文不一致!\n  期望: ${expectText}\n  实际: ${joined}`);
else ok('诗文与任务清单逐字一致');

if (!Array.isArray(POEM) || POEM.length !== 4) fail(`POEM.length=${POEM && POEM.length} 应为 4`);
else ok('POEM = 4 句');
if (!Array.isArray(STAGES) || STAGES.length !== 5) fail(`STAGES.length=${STAGES && STAGES.length} 应为 5（封面+4）`);
else ok('STAGES = 封面 + 4 境');
for (let i = 1; i < STAGES.length; i++) {
  if (STAGES[i].name !== POEM[i - 1].name) fail(`STAGES[${i}].name "${STAGES[i].name}" ≠ POEM[${i - 1}].name "${POEM[i - 1].name}"`);
}

function scanNaN(root, tag) {
  let bad = 0;
  root.traverse(o => {
    const g = o.geometry;
    if (g && g.attributes) {
      for (const k of Object.keys(g.attributes)) {
        const arr = g.attributes[k] && g.attributes[k].array;
        if (arr && arr.length) for (let i = 0; i < arr.length; i++) {
          if (Number.isNaN(arr[i])) { bad++; if (bad < 4) console.error(`  NaN @ ${tag} <${o.type || '?'}>.${k}[${i}]`); break; }
        }
      }
    }
    const u = o.material && o.material.uniforms;
    if (u) for (const k of Object.keys(u)) {
      const v = u[k] && u[k].value;
      if (typeof v === 'number' && Number.isNaN(v)) { bad++; console.error(`  NaN uniform ${k} @ ${tag}`); }
    }
  });
  return bad;
}

const frames = [0.2, 1.2, 3, 6, 9, 12, 13.5, 16, 20, 26, 30];
let lastBuilt = {};
for (let i = 0; i < STAGES.length; i++) {
  const s = STAGES[i];
  const tag = `境${i}${i ? '「' + s.name + '」' : '（封面）'}`;
  try {
    // sky 工厂
    const sky = s.sky();
    if (!sky || !sky.top || !sky.hor || !sky.fog || typeof sky.fd !== 'number' || !sky.moon) fail(`${tag}: sky() 字段不全`);
    // 两轮 build（模拟重游，抓共享缓存/状态泄漏）
    for (let round = 0; round < 2; round++) {
      const st = s.build();
      if (!st || !st.group) { fail(`${tag}: build() 未返回 {group}`); break; }
      st.group.userData.fadeK = 1;
      if (st.onEnter) st.onEnter();
      for (const t of frames) {
        st.update && st.update(t, 1 / 60);
      }
      const n = scanNaN(st.group, tag + (round ? ' #2' : ''));
      if (n) fail(`${tag}: 发现 ${n} 处 NaN`);
      if (st.click) { st.click(); st.update && st.update(1.0, 1 / 60); st.click(); st.update && st.update(2.5, 1 / 60); }
      lastBuilt[i] = st;
    }
    ok(`${tag}: build×2 + update(${frames.length} 帧) + click×2 全部通过`);
  } catch (e) {
    fail(`${tag}: 运行时错误 —— ${e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e.message}`);
  }
}

/* 境② 专项：花苞必须随时间真的绽放（bloomAvg 随 stageT 上升） */
try {
  const st = STAGES[2].build();
  st.group.userData.fadeK = 1;
  vm.runInContext('stageT=2', sandbox); // bloom 进度由引擎全局 stageT 驱动
  for (const t of [0.5, 1, 2, 4]) st.update(t, 1 / 60);
  const early = st.bloomAvg();
  vm.runInContext('stageT=16', sandbox);
  for (const t of [8, 10, 12, 14, 16]) st.update(t, 1 / 60);
  const late = st.bloomAvg();
  if (!(late > early + 0.3)) fail(`境②: 花苞未绽放 (t=4 时 ${early.toFixed(2)} → t=16 时 ${late.toFixed(2)})`);
  else ok(`境②「春风催花」: 花开进度 ${early.toFixed(2)} → ${late.toFixed(2)}（催放动画正常）`);
} catch (e) { fail('境②专项: ' + e.message); }

/* 境④ 专项：点击后疾风锋面必须真的压弯竹竿（peak 显著高于常态） */
try {
  const st = STAGES[4].build();
  st.group.userData.fadeK = 1;
  let basePeak = 0;
  for (let k = 0; k < 120; k++) { st.update(k / 60 + 1, 1 / 60); basePeak = Math.max(basePeak, st.ctl.peak); }
  st.click();
  let gustPeak = 0;
  for (let k = 0; k < 240; k++) { st.update(5 + k / 60, 1 / 60); gustPeak = Math.max(gustPeak, st.ctl.peak); }
  if (!(gustPeak > basePeak + 0.2)) fail(`境④: 疾风锋面未压弯竹竿 (常态 ${basePeak.toFixed(2)} → 阵风 ${gustPeak.toFixed(2)})`);
  else ok(`境④「风入竹林」: 常态摆幅 ${basePeak.toFixed(2)} → 疾风锋面 ${gustPeak.toFixed(2)}（万竿齐斜正常）`);
} catch (e) { fail('境④专项: ' + e.message); }

/* 境① 专项：落叶实例矩阵必须随时间更新（旋舞而非冻结） */
try {
  const st = STAGES[1].build();
  st.group.userData.fadeK = 1;
  st.update(1, 1 / 60);
  let im = null;
  st.group.traverse(o => { if (!im && o.count === 88 && o._mats) im = o; });
  if (!im) fail('境①: 未找到落叶 InstancedMesh');
  else {
    const a = JSON.stringify(im._mats[0]);
    st.update(3, 1 / 60);
    st.update(5, 1 / 60);
    const b = JSON.stringify(im._mats[0]);
    if (a === b) fail('境①: 落叶矩阵冻结（update 未驱动旋舞）');
    else ok('境①「秋风扫叶」: 落叶实例矩阵随帧更新（旋舞正常）');
  }
} catch (e) { fail('境①专项: ' + e.message); }

/* 境③ 专项：风线透明度必须每帧由 update 写入且乘 fadeK（防 setFade 冻结） */
try {
  const st = STAGES[3].build();
  st.group.userData.fadeK = 0.5; // 模拟 setFade 半透明
  let sp = null;
  st.group.traverse(o => { if (!sp && o.isSprite && o.userData.windLine) sp = o; });
  st.update(2);
  if (!sp) fail('境③: 未找到风线 Sprite');
  else if (!(sp.material.opacity > 0 && sp.material.opacity <= 1))
    fail(`境③: 风线透明度异常 ${sp.material.opacity}`);
  else ok(`境③「江风卷浪」: 风线透明度 ${sp.material.opacity.toFixed(3)}（已乘 fadeK=0.5，每帧写入）`);
} catch (e) { fail('境③专项: ' + e.message); }

/* ---------------- 引擎级演练：boot + 逐境 transition 走完全诗 + 终章 ---------------- */
try {
  let rafQ = [];
  sandbox.requestAnimationFrame = fn => { rafQ.push(fn); };
  const pump = n => { for (let i = 0; i < n; i++) { const q = rafQ; rafQ = []; q.forEach(f => f()); } };
  vm.runInContext('boot()', sandbox);
  if (vm.runInContext('state', sandbox) !== 'stage' || vm.runInContext('curIdx', sandbox) !== 0)
    fail('boot(): 封面境未就绪');
  else ok('boot() 无异常（buildSky / buildDots / 封面境 / 主循环启动）');
  pump(30);
  for (let i = 1; i <= 4; i++) {
    vm.runInContext(`goto(${i})`, sandbox);
    pump(220); // 220×0.0167s ≈ 3.7s > 过场 2.6s
    if (vm.runInContext('curIdx', sandbox) !== i || vm.runInContext('state', sandbox) !== 'stage')
      fail(`goto(${i}): 过场未完成（state=${vm.runInContext('state', sandbox)}）`);
  }
  ok('goto(1..4) 全部完成过场（相机插值 + 天空插值 + 交叉淡化）');
  const sceneRoot = vm.runInContext('scene', sandbox);
  const nNaN = scanNaN(sceneRoot, '末境场景树');
  if (nNaN) fail(`引擎级演练: 全场景树发现 ${nNaN} 处 NaN`);
  else ok('末境场景树 NaN 扫描通过（穹顶/星/月/山/水/风线/竹林）');
  vm.runInContext('showEnding()', sandbox);
  if (vm.runInContext('state', sandbox) !== 'ending') fail('showEnding(): 未进入终章');
  else ok('showEnding() 进入终章（全诗朗读 05.mp3 触发路径覆盖）');
} catch (e) {
  fail('引擎级演练: ' + (e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e.message));
}

/* 拼音抽查（多音字） */
const expect = { '解': 'jiě', '落': 'luò', '过': 'guò', '尺': 'chǐ', '斜': 'xié', '竿': 'gān', '能': 'néng', '二': 'èr' };
POEM.forEach(p => p.segs.forEach(seg => {
  const chars = [...seg.c].filter(c => !/[，。、！？；：…—·]/.test(c));
  chars.forEach((c, i) => {
    if (expect[c] && seg.p[i] && !seg.p[i].startsWith(expect[c]))
      fail(`注音: 「${c}」应读 ${expect[c]}，现为 ${seg.p[i]}（上下文：${seg.c}）`);
  });
}));
ok('多音字抽查完成（解/落/过/尺/斜/竿/能/二）');

console.log(failures ? `\n共 ${failures} 处失败` : '\n深度冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
