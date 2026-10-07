#!/usr/bin/env node
/*
 * smoke.test.js —— 「循文入境·清明」深度冒烟测试
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
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true;
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
class Sprite extends Object3D { constructor(m) { super(); this.material = m; this.isSprite = true; } }
class Light extends Object3D { constructor(c, i) { super(); this.color = new Color(c === undefined ? 0xffffff : c); this.intensity = i === undefined ? 1 : i; this.isLight = true; } }
class DirectionalLight extends Light { constructor(c, i) { super(c, i); } }
class AmbientLight extends Light { constructor(c, i) { super(c, i); } }
class PointLight extends Light { constructor(c, i, d) { super(c, i); this.distance = d; } }
class BufferAttribute {
  constructor(arr, s) { this.array = arr; this.itemSize = s; this.needsUpdate = false; }
  setX() { return this; } setY() { return this; } setZ() { return this; }
}
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
const GeoC = name => class { constructor(...a) { this.type = name; this.parameters = {}; this.args = a; this.attributes = {}; } setAttribute(n, a) { this.attributes[n] = a; return this; } rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; } dispose() {} };
class CatmullRomCurve3 { constructor(pts) { this.points = pts; } getPoints(n) { return this.points.slice(0, Math.max(2, n)); } getPoint() { return this.points[0] || new V3(); } }
class CanvasTexture { constructor(cv) { this.image = cv; this.needsUpdate = true; } dispose() {} }
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
const geos = ['SphereGeometry', 'PlaneGeometry', 'CircleGeometry', 'CylinderGeometry', 'ConeGeometry',
  'BoxGeometry', 'TorusGeometry', 'LatheGeometry', 'RingGeometry', 'TubeGeometry'];
const THREE = {
  Vector3: V3, Vector2: V2, Quaternion, Euler, Color, Matrix4,
  Object3D, Group, Mesh, Points, Line, LineSegments, Sprite,
  Light, DirectionalLight, AmbientLight, PointLight,
  BufferAttribute, BufferGeometry,
  Material, ShaderMaterial, MeshBasicMaterial, MeshPhongMaterial, PointsMaterial,
  LineBasicMaterial, SpriteMaterial,
  CatmullRomCurve3, CanvasTexture,
  FogExp2, Scene, PerspectiveCamera, WebGLRenderer,
  DynamicDrawUsage: {}, BackSide: 1, FrontSide: 0, DoubleSide: 2,
  AdditiveBlending: 2, NormalBlending: 1,
  sRGBEncoding: 3001,
};
geos.forEach(n => { THREE[n] = GeoC(n); });

/* ---------------- DOM 桩 ---------------- */
const ctx2d = {
  fillStyle: '', globalAlpha: 1, font: '', textAlign: '', textBaseline: '',
  shadowColor: '', shadowBlur: 0, strokeStyle: '', lineWidth: 1,
  fillRect() {}, fillText() {}, strokeText() {}, clearRect() {}, strokeRect() {}, save() {}, restore() {},
  createRadialGradient: () => ({ addColorStop() {} }),
  createLinearGradient: () => ({ addColorStop() {} }),
  beginPath() {}, arc() {}, fill() {}, stroke() {}, measureText: () => ({ width: 10 }),
};
function makeEl(tag) {
  if (tag === 'canvas') return { width: 0, height: 0, getContext: () => ctx2d, style: {} };
  return {
    tagName: (tag || 'div').toUpperCase(), style: {}, textContent: '', innerHTML: '',
    classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
    addEventListener() {}, appendChild() {}, querySelectorAll: () => [], offsetWidth: 100, open: false, disabled: false,
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
};
sandbox.globalThis = sandbox;
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: 'index.html (smoke)' });

/* ---------------- 逐境深度执行 ---------------- */
const POEM = vm.runInContext('POEM', sandbox), STAGES = vm.runInContext('STAGES', sandbox);
let failures = 0;
const fail = m => { failures++; console.error('✗ ' + m); };
const ok = m => console.log('✓ ' + m);

if (!Array.isArray(POEM) || POEM.length !== 3) fail(`POEM.length=${POEM && POEM.length} 应为 3`);
else ok('POEM = 3 句');
if (!Array.isArray(STAGES) || STAGES.length !== 4) fail(`STAGES.length=${STAGES && STAGES.length} 应为 4（封面+3）`);
else ok('STAGES = 封面 + 3 境');
for (let i = 1; i < STAGES.length; i++) {
  if (STAGES[i].name !== POEM[i - 1].name) fail(`STAGES[${i}].name "${STAGES[i].name}" ≠ POEM[${i - 1}].name "${POEM[i - 1].name}"`);
}

/* 诗文逐字对齐 queue.json */
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
const EXPECT_TEXT = '清明时节雨纷纷，路上行人欲断魂。借问酒家何处有，牧童遥指杏花村。';
if (joined !== EXPECT_TEXT) fail(`诗文不一致!\n  期望: ${EXPECT_TEXT}\n  实际: ${joined}`);
else ok('诗文与 queue.json 逐字逐标点一致');

/* 边界常量联动 */
if (!code.includes('clamp(i,0,3)')) fail('goto 缺 clamp(i,0,3)');
if ((code.match(/curIdx===3&&state==='stage'/g) || []).length < 2) fail('交互境 curIdx===3 接线不足 2 处');
else ok('交互接线 curIdx===3 ≥ 2 处（pointerdown + 空格）');
if (!code.includes("'04.mp3'")) fail("缺全诗音频 '04.mp3' 引用");
else ok("全诗音频 '04.mp3' 已引用（01–03 各境 + 00 标题）");

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
for (let i = 0; i < STAGES.length; i++) {
  const s = STAGES[i];
  const tag = `境${i}${i ? '「' + s.name + '」' : '（封面）'}`;
  try {
    const sky = s.sky();
    if (!sky || !sky.top || !sky.hor || !sky.fog || typeof sky.fd !== 'number' || !sky.moon) fail(`${tag}: sky() 字段不全`);
    for (let round = 0; round < 2; round++) {
      vm.runInContext('stageT=0', sandbox);
      const st = s.build();
      if (!st || !st.group) { fail(`${tag}: build() 未返回 {group}`); break; }
      st.group.userData.fadeK = 1;
      if (st.onEnter) st.onEnter();
      for (const t of frames) st.update && st.update(t, 1 / 60);
      const n = scanNaN(st.group, tag + (round ? ' #2' : ''));
      if (n) fail(`${tag}: 发现 ${n} 处 NaN`);
      if (st.click) { st.click(); st.update && st.update(1.0, 1 / 60); st.click(); st.update && st.update(2.5, 1 / 60); }
    }
    ok(`${tag}: build×2 + update(${frames.length} 帧) + click×2 全部通过`);
  } catch (e) {
    fail(`${tag}: 运行时错误 —— ${e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e.message}`);
  }
}

/* 境①专项：双层雨丝 LineSegments，纷纷疏密呼吸 + 杏花伏笔 */
try {
  const s1 = STAGES[1];
  vm.runInContext('stageT=0', sandbox);
  const b1 = s1.build(); b1.group.userData.fadeK = 1;
  let rains = 0, verts = 0;
  b1.group.traverse(o => {
    if (o.geometry && o.geometry.attributes && o.geometry.attributes.aTip) { rains++; verts += o.geometry.attributes.position.array.length / 6; }
  });
  if (rains < 2) fail(`境①: 雨丝层不足 (${rains} 层，应 ≥2）`);
  else ok(`境①: 雨丝 ${rains} 层 / ${verts} 条（LineSegments 斜雨）`);
  b1.update(0.3, 1 / 60);
  let a0 = null;
  b1.group.traverse(o => {
    if (o.geometry && o.geometry.attributes && o.geometry.attributes.aTip && a0 === null) a0 = o.material.uniforms.uMaxA.value;
  });
  b1.update(4.5, 1 / 60);
  let a1 = null;
  b1.group.traverse(o => {
    if (o.geometry && o.geometry.attributes && o.geometry.attributes.aTip && a1 === null) a1 = o.material.uniforms.uMaxA.value;
  });
  if (a0 === null || a1 === null) fail('境①: 未找到雨丝 uMaxA');
  else if (Math.abs(a1 - a0) < 1e-4) fail('境①: 雨丝疏密无呼吸（纷纷感缺失）');
  else ok(`境①: 纷纷疏密呼吸 uMaxA ${a0.toFixed(3)} → ${a1.toFixed(3)}`);
  let apricot = 0;
  b1.group.traverse(o => { if (o.geometry && o.geometry.type === 'SphereGeometry' && o.scale.y < 0.8) apricot++; });
  if (apricot < 3) fail('境①: 缺少远处杏花伏笔树冠');
  else ok(`境①: 远处杏花伏笔（压扁树冠 ×${apricot}）`);
} catch (e) { fail('境① 专项: ' + e.message); }

/* 境②专项：行人低伏（身体前倾）且缓行（z 随时间减小） */
try {
  const s2 = STAGES[2];
  vm.runInContext('stageT=0', sandbox);
  const b2 = s2.build(); b2.group.userData.fadeK = 1;
  b2.update(0.5, 1 / 60);
  let zA = null, lean = null, n = 0;
  b2.group.traverse(o => {
    if (o.userData && o.userData.isWalker) {
      n++;
      if (zA === null) zA = o.position.z;
      const body = o.children[0];
      if (body && body.rotation.x < -0.2) lean = body.rotation.x;
    }
  });
  if (n < 3) fail(`境②: 行人不足 (${n}，应 3）`);
  b2.update(4.0, 1 / 60);
  let zB = null;
  b2.group.traverse(o => { if (o.userData && o.userData.isWalker && zB === null) zB = o.position.z; });
  if (zA === null || zB === null) fail('境②: 未找到行人');
  else if (!(zB < zA - 0.5)) fail(`境②: 行人未缓行 (z ${zA.toFixed(2)} → ${zB.toFixed(2)}）`);
  else ok(`境②: 行人低伏缓行 lean=${lean === null ? '?' : lean.toFixed(2)} z ${zA.toFixed(2)} → ${zB.toFixed(2)}`);
} catch (e) { fail('境② 专项: ' + e.message); }

/* 境③专项：雨幕裂开 → 杏花村显现 → 冷却防连点 → 杏花雨迸落 → fadeK 归零 → 自动裂开 */
function collect3(g) {
  const r = { reveal: [], curtain: [], wedge: null, shaft: null, petals: null, burst: null };
  g.traverse(o => {
    const m = o.material;
    if (m && m.userData && m.userData.o0 !== undefined && !o.isSprite) r.reveal.push(m);
    if (o.isSprite && o.scale.x > 20) r.curtain.push(o);
    if (o.isSprite && o.scale.x <= 20 && !r.shaft) r.shaft = o;
    if (o.geometry && o.geometry.attributes && o.geometry.attributes.aTip && !r.wedge) r.wedge = o.material.uniforms.uMaxA;
    if (o.isPoints && m && !m.uniforms && !r.petals) r.petals = m;
    if (o.isPoints && m && m.uniforms && m.uniforms.uT0 && !r.burst) r.burst = m.uniforms.uT0;
  });
  return r;
}
try {
  const s3 = STAGES[3];
  vm.runInContext('stageT=0', sandbox);
  const b3 = s3.build(); b3.group.userData.fadeK = 1;
  const c = collect3(b3.group);
  if (!c.reveal.length) fail('境③: 未找到杏花村 reveal 材质');
  if (!c.curtain.length) fail('境③: 未找到雨雾墙 Sprite');
  if (!c.wedge) fail('境③: 未找到山坳密雨');
  if (!c.petals) fail('境③: 未找到杏花瓣 Points');
  if (!c.burst) fail('境③: 未找到杏花雨迸落 burst');
  if (!c.shaft) fail('境③: 未找到一线暖光 Sprite');
  // 未开时全村隐藏
  b3.update(0.5, 0.5);
  const hidden = c.reveal.every(m => m.opacity < 0.02) && c.petals.opacity < 0.02 && c.shaft.material.opacity < 0.02;
  if (!hidden) fail('境③: 初始时杏花村未隐于雨幕');
  // 点击 → 裂开；冷却内第二次点击应被忽略
  b3.click(); b3.click();
  if (c.burst.value > -100) fail('境③: 冷却内第二次点击仍触发了迸落（守卫失效）');
  const cx0 = c.curtain[0].position.x;
  for (let i = 0; i < 8; i++) b3.update(0.5 + (i + 1) * 0.35, 0.35);
  const wallOp = Math.min(...c.reveal.map(m => m.opacity));
  const cx1 = c.curtain[0].position.x;
  const wedgeA = c.wedge.value;
  const shaftOp = c.shaft.material.opacity;
  if (!(wallOp > 0.4)) fail(`境③: 点击后杏花村未显现（最暗材质 opacity=${wallOp.toFixed(3)}）`);
  else ok(`境③: 点击后雨幕裂开、杏花村显现（材质最低 opacity ${wallOp.toFixed(3)}）`);
  if (Math.abs(cx1 - cx0) < 5) fail(`境③: 雾墙未沿指向线滑开 (x ${cx0.toFixed(1)} → ${cx1.toFixed(1)}）`);
  else ok(`境③: 雾墙左右滑开 ${cx0.toFixed(1)} → ${cx1.toFixed(1)}`);
  if (!(wedgeA < 0.1)) fail(`境③: 山坳密雨未退（uMaxA=${wedgeA.toFixed(3)}）`);
  else ok(`境③: 山坳密雨退去（uMaxA → ${wedgeA.toFixed(3)}）`);
  if (!(shaftOp > 0.08)) fail(`境③: 一线暖光未现（opacity=${shaftOp.toFixed(3)}）`);
  else ok(`境③: 一线暖光透出（opacity ${shaftOp.toFixed(3)}）`);
  if (!(c.petals.opacity > 0.4)) fail(`境③: 杏花瓣未飘落（opacity=${c.petals.opacity.toFixed(3)}）`);
  else ok(`境③: 杏花瓣飘落（opacity ${c.petals.opacity.toFixed(3)}）`);
  // 已开且过冷却 → 再点触发杏花雨迸落
  b3.click();
  if (!(c.burst.value > -100)) fail('境③: 过冷却后点击未触发杏花雨迸落');
  else ok('境③: 再点触发杏花雨迸落（burst.fire）');
  // fadeK=0 → 自建透明度全部归零
  b3.group.userData.fadeK = 0;
  b3.update(8, 0.3);
  const all0 = c.reveal.every(m => m.opacity < 0.02) && c.petals.opacity < 0.02
    && c.curtain.every(s => s.material.opacity < 0.02) && c.shaft.material.opacity < 0.02;
  if (!all0) fail('境③: fadeK=0 时自建动画透明度未归零');
  else ok('境③: 自建动画透明度逐帧乘 fadeK（fadeK=0 → 全透明）');
  // 自动开：stageT>7.5 时无需点击也裂开
  const b3b = s3.build(); b3b.group.userData.fadeK = 1;
  const cb = collect3(b3b.group);
  vm.runInContext('stageT=8', sandbox);
  b3b.update(0.2, 0.1);
  for (let i = 0; i < 12; i++) b3b.update(0.2 + (i + 1) * 0.25, 0.25);
  const wallOp2 = Math.min(...cb.reveal.map(m => m.opacity));
  if (!(wallOp2 > 0.4)) fail(`境③: 自动游览未触发标志瞬间（opacity=${wallOp2.toFixed(3)}）`);
  else ok('境③: 自动游览 7.5s 后自动裂开（无人值守可见标志瞬间）');
  vm.runInContext('stageT=0', sandbox);
} catch (e) { fail('境③ 专项: ' + e.message); }

/* 小测与评语数量 */
try {
  const QUIZ = vm.runInContext('QUIZ', sandbox);
  if (!Array.isArray(QUIZ) || QUIZ.length < 5) fail(`小测 ${QUIZ && QUIZ.length} 题应为 5`);
  else {
    const w = code.match(/words\s*=\s*\[([^\]]*)\]/);
    const wn = w ? w[1].split(',').length : 0;
    if (wn !== QUIZ.length + 1) fail(`评语 words ${wn} 项应为 ${QUIZ.length + 1}`);
    else ok(`小测 ${QUIZ.length} 题 + 评语 ${wn} 项（题数+1）`);
  }
} catch (e) { fail('小测检查: ' + e.message); }

/* 拼音抽查（本诗多音字/关键读音） */
const expect = { '魂': 'hún', '酒': 'jiǔ', '处': 'chù', '行': 'xíng', '节': 'jié', '指': 'zhǐ', '杏': 'xìng', '借': 'jiè', '遥': 'yáo', '欲': 'yù', '纷': 'fēn' };
POEM.forEach(p => p.segs.forEach(seg => {
  const chars = [...seg.c].filter(c => !/[，。、！？；：…—·]/.test(c));
  chars.forEach((c, i) => {
    if (expect[c] && seg.p[i] && !seg.p[i].startsWith(expect[c]))
      fail(`注音: 「${c}」应读 ${expect[c]}，现为 ${seg.p[i]}（上下文：${seg.c}）`);
  });
}));
ok('指定多音字抽查完成（魂/酒/处/行/节/指/杏/借/遥/欲/纷）');

console.log(failures ? `\n共 ${failures} 处失败` : '\n深度冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
