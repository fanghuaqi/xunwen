#!/usr/bin/env node
/*
 * smoke.test.js —— 「循文入境·黄鹤楼（崔颢）」深度冒烟测试
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
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  lerp(c, a) { this.r += (c.r - this.r) * a; this.g += (c.g - this.g) * a; this.b += (c.b - this.b) * a; return this; }
}
Color.prototype.isColor = true;

class Object3D {
  constructor() {
    this.position = new V3(); this.rotation = new Euler(); this.scale = new V3(1, 1, 1);
    this.quaternion = new Quaternion(); this.children = []; this.userData = {};
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true; this.name = '';
    this.matrix = {}; this.matrixWorld = {}; this.parent = null;
  }
  add(...cs) { for (const c of cs) { if (Array.isArray(c)) this.add(...c); else if (c && c.isObject3D) { this.children.push(c); c.parent = this; } } return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) { fn(this); for (const c of this.children) c.traverse(fn); }
  getObjectByName(n) { let f = null; this.traverse(o => { if (o.name === n && !f) f = o; }); return f; }
  translateX(v) { this.position.x += v; return this; }
  translateY(v) { this.position.y += v; return this; }
  translateZ(v) { this.position.z += v; return this; }
  rotateOnAxis() { return this; }
  rotateZ() { return this; }
  lookAt() { return this; }
  updateMatrix() { return this; }
  updateWorldMatrix() { return this; }
  getWorldPosition(t) { return t ? t.set(0, 0, 0) : new V3(); }
  clear() { this.children.length = 0; return this; }
}
Object3D.prototype.isObject3D = true;
class Group extends Object3D { constructor() { super(); this.isGroup = true; this.type = 'Group'; } }
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isPoints = true; } }
class Line extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class LineSegments extends Line { constructor(g, m) { super(g, m); } }
class LineLoop extends Line { constructor(g, m) { super(g, m); } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; this.isSprite = true; } }
class Light extends Object3D { constructor(c, i) { super(); this.color = new Color(c === undefined ? 0xffffff : c); this.intensity = i === undefined ? 1 : i; this.isLight = true; } }
class DirectionalLight extends Light { constructor(c, i) { super(c, i); } }
class AmbientLight extends Light { constructor(c, i) { super(c, i); } }
class PointLight extends Light { constructor(c, i, d) { super(c, i); this.distance = d; } }
class BufferAttribute {
  constructor(arr, s) { this.array = arr; this.itemSize = s; this.needsUpdate = false; this.count = arr ? arr.length / s : 0; }
  getX(i) { return this.array[i * this.itemSize]; }
  setX(i, v) { this.array[i * this.itemSize] = v; return this; }
  setY(i, v) { this.array[i * this.itemSize + 1] = v; return this; }
  setZ(i, v) { this.array[i * this.itemSize + 2] = v; return this; }
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
  translate() { return this; } computeBoundingSphere() {} dispose() {}
}
class InstancedMesh extends Object3D {
  constructor(g, m, n) { super(); this.geometry = g; this.material = m; this.count = n;
    this.instanceMatrix = { setUsage() {}, needsUpdate: false }; }
  setMatrixAt(i, m) { this._last = [i, m]; }
  getMatrixAt() { return new THREE.Matrix4(); }
  dispose() {}
}
class Matrix4 { constructor() { this.elements = new Float32Array(16); } identity() { return this; } compose() { return this; } }
class Material { constructor(o) { this.userData = {}; this.transparent = false; this.opacity = 1; this.side = 0; this.fog = true; Object.assign(this, o || {}); } dispose() {} }
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
class ShapeGeometry extends GeoC('ShapeGeometry') { constructor(shape, seg) { super(shape, seg); } }
const geos = ['SphereGeometry', 'PlaneGeometry', 'CircleGeometry', 'CylinderGeometry', 'ConeGeometry',
  'BoxGeometry', 'TorusGeometry', 'LatheGeometry', 'RingGeometry', 'IcosahedronGeometry', 'TubeGeometry', 'ExtrudeGeometry'];
const THREE = {
  Vector3: V3, Vector2: V2, Quaternion, Euler, Color, Matrix4,
  Object3D, Group, Mesh, Points, Line, LineSegments, LineLoop, Sprite,
  Light, DirectionalLight, AmbientLight, PointLight,
  BufferAttribute, InstancedBufferAttribute, BufferGeometry, InstancedMesh,
  Material, ShaderMaterial, MeshBasicMaterial, MeshPhongMaterial, PointsMaterial,
  LineBasicMaterial, SpriteMaterial, MeshStandardMaterial,
  Shape, ShapeGeometry, CatmullRomCurve3, CanvasTexture, Texture,
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
  performance: { now: () => 0 },
  requestAnimationFrame() { return 0; },
  setTimeout: () => 0, clearTimeout() {},
  console, Math, String, Number, Array, Object, Float32Array, parseInt, isNaN,
  location: { reload() {} },
  speechSynthesis: undefined,
};
sandbox.globalThis = sandbox;
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: 'index.html (smoke)' });

/* ---------------- 逐境深度执行 ---------------- */
const POEM = vm.runInContext('POEM', sandbox), STAGES = vm.runInContext('STAGES', sandbox);
let failures = 0;
const fail = m => { failures++; console.error('✗ ' + m); };
const ok = m => console.log('✓ ' + m);

if (!Array.isArray(POEM) || POEM.length !== 4) fail(`POEM.length=${POEM && POEM.length} 应为 4`);
else ok('POEM = 4 句');
if (!Array.isArray(STAGES) || STAGES.length !== 5) fail(`STAGES.length=${STAGES && STAGES.length} 应为 5（封面+4）`);
else ok('STAGES = 封面 + 4 境');
for (let i = 1; i < STAGES.length; i++) {
  if (STAGES[i].name !== POEM[i - 1].name) fail(`STAGES[${i}].name "${STAGES[i].name}" ≠ POEM[${i - 1}].name "${POEM[i - 1].name}"`);
}

/* 诗文逐字核对（与 queue.json text 一致） */
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
const EXPECT = '昔人已乘黄鹤去，此地空余黄鹤楼。黄鹤一去不复返，白云千载空悠悠。晴川历历汉阳树，芳草萋萋鹦鹉洲。日暮乡关何处是？烟波江上使人愁。';
if (joined !== EXPECT) fail(`诗文不一致!\n  期望: ${EXPECT}\n  实际: ${joined}`);
else ok('诗文与清单逐字逐标点一致');

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

const frames = [0.2, 1, 2, 4, 8, 12, 16, 20, 23, 26, 30];
for (let i = 0; i < STAGES.length; i++) {
  const s = STAGES[i];
  const tag = `境${i}${i ? '「' + s.name + '」' : '（封面）'}`;
  try {
    const sky = s.sky();
    if (!sky || !sky.top || !sky.hor || !sky.fog || typeof sky.fd !== 'number' || !sky.moon) fail(`${tag}: sky() 字段不全`);
    // 两轮 build（模拟重游，抓共享缓存/状态泄漏）
    for (let round = 0; round < 2; round++) {
      const st = s.build();
      if (!st || !st.group) { fail(`${tag}: build() 未返回 {group}`); break; }
      st.group.userData.fadeK = 1;
      if (st.onEnter) st.onEnter();
      for (const t of frames) st.update && st.update(t, 1);
      const n = scanNaN(st.group, tag + (round ? ' #2' : ''));
      if (n) fail(`${tag}: 发现 ${n} 处 NaN`);
      if (st.click) { st.click(); st.update && st.update(1, 1); st.click(); st.update && st.update(2.5, 1); }
    }
    ok(`${tag}: build×2 + update(${frames.length} 帧) + click×2 全部通过`);
  } catch (e) {
    fail(`${tag}: 运行时错误 —— ${e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e.message}`);
  }
}

/* 标志瞬间专项：境②黄鹤从楼顶振翅远去（不复返）+ 千载流云快速流过 */
try {
  const st = STAGES[2].build();
  st.group.userData.fadeK = 1;
  st.update && st.update(0, 1);
  const clouds = st.group.getObjectByName('cloudsFast');
  const crane = st.group.getObjectByName('craneFly');
  if (!clouds) fail('标志瞬间: 未找到 cloudsFast');
  else if (!clouds.children.length || !(clouds.children[0].material)) fail('标志瞬间: cloudsFast 无精灵');
  else {
    const x0 = clouds.children[0].position.x;
    st.update && st.update(1, 1);
    const dx = clouds.children[0].position.x - x0;
    if (!(dx > 12)) fail(`标志瞬间: 千载流云流速不足 (1 秒仅移动 ${dx.toFixed(1)})`);
    else ok(`标志瞬间②: 千载流云时间流逝感（1 秒移动 ${dx.toFixed(1)} 单位，数十倍速）`);
  }
  if (!crane) fail('标志瞬间: 未找到 craneFly');
  else {
    for (let t = 2; t <= 11; t++) st.update && st.update(t, 1);
    const opMid = crane.children.find(o => o.material && o.material.transparent);
    if (!opMid || !(opMid.material.opacity > 0.2)) fail('标志瞬间: 黄鹤未振翅远去（中段不可见）');
    for (let t = 12; t <= 21; t++) st.update && st.update(t, 1);
    const opEnd = crane.children.find(o => o.material && o.material.transparent);
    const far = crane.position.length();
    st.update && st.update(22, 1);
    const opCycle = opEnd.material.opacity;
    if (!(opCycle < 0.01)) fail(`标志瞬间: 黄鹤去而不返失败（周期末端 t=22 opacity=${opCycle.toFixed(3)}）`);
    else if (!(far > 120)) fail(`标志瞬间: 黄鹤未远去 (距离 ${far.toFixed(0)})`);
    else ok(`标志瞬间②: 黄鹤自楼顶振翅远去 (距离 ${far.toFixed(0)})，周期末端 opacity=${opCycle.toFixed(3)}（不复返）`);
    for (let t = 22; t <= 46; t++) st.update && st.update(t, 1);
    const n = scanNaN(st.group, '标志瞬间长跑');
    if (n) fail(`标志瞬间: 长时间运行出现 ${n} 处 NaN`);
    else ok('标志瞬间②: 46 秒长跑（跨两个周期）无 NaN');
  }
} catch (e) { fail('标志瞬间专项: ' + e.message); }

/* 交互境专项：境④点击白云千载 → 流云加速 + 黄鹤虚影掠空 + 防连点 */
try {
  const st = STAGES[4].build();
  st.group.userData.fadeK = 1;
  st.update && st.update(0, 1);
  const clouds = st.group.getObjectByName('cloudsSlow');
  const ghost = st.group.getObjectByName('ghostCrane');
  if (!clouds) fail('交互境: 未找到 cloudsSlow');
  else if (!ghost) fail('交互境: 未找到 ghostCrane');
  else {
    const gmat = ghost.children.find(o => o.material && o.material.transparent);
    if (!gmat || gmat.material.opacity !== 0) fail('交互境: 初始黄鹤虚影应不可见');
    const x0 = clouds.children[0].position.x;
    st.update && st.update(1, 1);
    const dxBefore = clouds.children[0].position.x - x0;
    if (!(dxBefore < 8)) fail(`交互境: 点击前流云应缓慢 (1 秒移动 ${dxBefore.toFixed(1)})`);
    st.click && st.click();
    const gx0 = ghost.position.x;
    st.update && st.update(2, 1);
    st.update && st.update(3, 1);
    const opNow = gmat.material.opacity;
    if (!(opNow > 0.1)) fail(`交互境: 点击后黄鹤虚影未掠过 (opacity=${opNow.toFixed(2)})`);
    const x1 = clouds.children[0].position.x;
    st.update && st.update(4, 1);
    const raw = clouds.children[0].position.x - x1;
    const dAfter = Math.min(Math.abs(raw), 440 - Math.abs(raw));   // 环绕盒宽 440，折算真实位移
    if (!(dAfter > dxBefore * 4)) fail(`交互境: 点击后流云未加速 (点击前 ${dxBefore.toFixed(1)} → 点击后 ${dAfter.toFixed(1)})`);
    st.click && st.click();              // 掠空途中再点 → 应被守卫忽略
    const gx1 = ghost.position.x;
    st.update && st.update(5, 1);
    const gx2 = ghost.position.x;
    if (!(gx2 > gx1)) fail('交互境: 重复点击不应重置虚影航程');
    else if (!(gx0 < gx1 && gx1 < gx2)) fail('交互境: 虚影未持续掠过');
    else ok(`交互境④: 点击后流云加速 (${dxBefore.toFixed(1)}→${dAfter.toFixed(1)})、黄鹤虚影掠空 (x ${gx0.toFixed(0)}→${gx2.toFixed(0)})，航行中重复点击被忽略`);
  }
} catch (e) { fail('交互境专项: ' + e.message); }

/* 拼音抽查（多音字 + 考点字） */
const expect = { '乘': 'chéng', '空': 'kōng', '载': 'zǎi', '萋': 'qī', '鹦': 'yīng', '鹉': 'wǔ', '历': 'lì', '悠': 'yōu', '复': 'fù', '暮': 'mù', '乡': 'xiāng', '洲': 'zhōu', '鹤': 'hè' };
POEM.forEach(p => p.segs.forEach(seg => {
  const chars = [...seg.c].filter(c => !/[，。、！？；：…—·]/.test(c));
  chars.forEach((c, i) => {
    if (expect[c] && seg.p[i] && !seg.p[i].startsWith(expect[c]))
      fail(`注音: 「${c}」应读 ${expect[c]}，现为 ${seg.p[i]}（上下文：${seg.c}）`);
  });
}));
ok('指定多音字抽查完成（乘/空/载/萋/鹦/鹉/历/悠/复/暮/乡/洲/鹤）');

/* 小测与评语数组 */
try {
  const QUIZ = vm.runInContext('QUIZ', sandbox);
  if (!Array.isArray(QUIZ) || QUIZ.length !== 5) fail(`QUIZ.length=${QUIZ && QUIZ.length} 应为 5`);
  else {
    QUIZ.forEach((q, i) => {
      if (!Array.isArray(q.o) || q.o.length !== 3) fail(`小测${i + 1}选项数≠3`);
      if (typeof q.a !== 'number' || q.a < 0 || q.a >= q.o.length) fail(`小测${i + 1}答案越界`);
    });
    ok('QUIZ = 5 题 × 3 选项，答案均在界内');
  }
  const wq = code.match(/words\s*=\s*\[([^\]]*)\]/);
  const wn = wq ? wq[1].split(',').length : 0;
  if (wn !== 6) fail(`words 评语数组 ${wn} 项，应为 6（题数+1）`);
  else ok('words 评语数组 = 6 项（按本诗定制）');
} catch (e) { fail('小测/评语检查: ' + e.message); }

console.log(failures ? `\n共 ${failures} 处失败` : '\n深度冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
