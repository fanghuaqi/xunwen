#!/usr/bin/env node
/*
 * smoke.test.js —— 「循文入境·赠汪伦」深度冒烟测试
 * 用带真实数学实现的 THREE 桩，在 Node 里真实执行主脚本顶层，
 * 并逐境调用 build()/update(t,dt)/click()/onEnter()，扫描 NaN，
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
class LineLoop extends Line { constructor(g, m) { super(g, m); } }
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
const GeoC = name => class { constructor(...a) { this.type = name; this.parameters = {}; this.args = a; this.attributes = {}; } setAttribute(n, a) { this.attributes[n] = a; return this; } rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; } dispose() {} };
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
  Object3D, Group, Mesh, Points, Line, LineSegments, LineLoop, Sprite,
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

if (!Array.isArray(POEM) || POEM.length !== 3) fail(`POEM.length=${POEM && POEM.length} 应为 3`);
else ok('POEM = 3 句');
if (!Array.isArray(STAGES) || STAGES.length !== 4) fail(`STAGES.length=${STAGES && STAGES.length} 应为 4（封面+3）`);
else ok('STAGES = 封面 + 3 境');
for (let i = 1; i < STAGES.length; i++) {
  if (STAGES[i].name !== POEM[i - 1].name) fail(`STAGES[${i}].name "${STAGES[i].name}" ≠ POEM[${i - 1}].name "${POEM[i - 1].name}"`);
}

/* 诗文逐字对齐 queue.json */
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
const EXPECT_TEXT = '李白乘舟将欲行，忽闻岸上踏歌声。桃花潭水深千尺，不及汪伦送我情。';
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
    }
    ok(`${tag}: build×2 + update(${frames.length} 帧) + click×2 全部通过`);
  } catch (e) {
    fail(`${tag}: 运行时错误 —— ${e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e.message}`);
  }
}

/* 境② 专项：人影必须随节拍起伏，涟漪必须荡开 */
try {
  const s2 = STAGES[2].build();
  s2.group.userData.fadeK = 1;
  s2.update && s2.update(0.05, 1 / 60);
  let yA = null; s2.group.traverse(o => { if (o.userData && o.userData.arms && yA === null) yA = o.position.y; });
  s2.update && s2.update(0.33, 1 / 60);
  let yB = null; s2.group.traverse(o => { if (o.userData && o.userData.arms && yB === null) yB = o.position.y; });
  if (yA === null || yB === null) fail('境②: 未找到踏歌人影（makeDancer）');
  else if (Math.abs(yA - yB) < 0.05) fail(`境②: 人影未随节拍起伏 (${yA.toFixed(3)} → ${yB.toFixed(3)})`);
  else ok(`境②: 人影随节拍起伏 ${yA.toFixed(3)} → ${yB.toFixed(3)}（顿足 dip）`);
  // 涟漪圈：扫 6 秒，圈透明度必须出现过非零
  let maxRing = 0;
  for (let t = 0.2; t < 6; t += 0.3) {
    s2.update(t, 0.3);
    s2.group.traverse(o => { if (o.geometry && o.geometry.type === 'RingGeometry' && o.material) maxRing = Math.max(maxRing, o.material.opacity); });
  }
  if (maxRing <= 0.01) fail('境②: 踏歌涟漪圈未出现（opacity 全 0）');
  else ok(`境②: 涟漪圈随节拍荡开（峰值 opacity ${maxRing.toFixed(2)}）`);
  // 浮瓣透明度必须 × fadeK：fadeK=0 时应全透明（排除水面——它也是 PlaneGeometry 但为 ShaderMaterial）
  let opAt0 = -1;
  s2.group.userData.fadeK = 0;
  s2.update(7, 0.3);
  s2.group.traverse(o => {
    if (opAt0 < 0 && o.geometry && o.geometry.type === 'PlaneGeometry' && o.material &&
        !o.material.isShaderMaterial && o.geometry.args && o.geometry.args[0] < 2) opAt0 = o.material.opacity;
  });
  if (opAt0 > 0.02) fail(`境②: 浮瓣未乘 fadeK（fadeK=0 时 opacity=${opAt0}）`);
  else ok('境②: 浮瓣透明度逐帧写入并乘 fadeK（fadeK=0 → 全透明）');
} catch (e) { fail('境② 专项: ' + e.message); }

/* 境③ 专项：点击后人群齐顿足 + 涟漪强荡开 */
try {
  const s3 = STAGES[3].build();
  s3.group.userData.fadeK = 1;
  s3.update && s3.update(0.5, 1 / 60);
  let y0 = null; s3.group.traverse(o => { if (o.userData && o.userData.arms && y0 === null) y0 = o.position.y; });
  s3.click && s3.click();
  s3.click && s3.click(); // 冷却期内重复点击应被忽略而非崩溃
  let y1 = null; // 顿足是脉冲：取 kick 窗口内人影最低点
  for (let i = 0; i < 20; i++) {
    s3.update && s3.update(0.5 + (i + 1) * 0.1, 0.1);
    s3.group.traverse(o => {
      if (o.userData && o.userData.arms) y1 = (y1 === null) ? o.position.y : Math.min(y1, o.position.y);
    });
  }
  if (y0 === null || y1 === null) fail('境③: 未找到岸上人群');
  else if (!(y1 < y0 - 0.15)) fail(`境③: 点击后人群未齐顿足 (${y0.toFixed(3)} → min ${y1.toFixed(3)})`);
  else ok(`境③: 点击后人群齐顿足 ${y0.toFixed(3)} → min ${y1.toFixed(3)}`);
  let maxRing = 0;
  for (let i = 0; i < 6; i++) {
    s3.update(2.0 + i * 0.2, 0.2);
    s3.group.traverse(o => { if (o.geometry && o.geometry.type === 'RingGeometry' && o.material) maxRing = Math.max(maxRing, o.material.opacity); });
  }
  if (maxRing <= 0.1) fail('境③: 点击后涟漪未强荡开');
  else ok(`境③: 点击后涟漪强荡开（峰值 opacity ${maxRing.toFixed(2)}）`);
  // 深水断面着色器 uFade 必须由 setFade 驱动
  let faceA = -1;
  s3.group.traverse(o => { if (o.material && o.material.isShaderMaterial && o.material.uniforms && o.material.uniforms.uTop && faceA < 0) faceA = o.material.uniforms.uFade.value; });
  if (faceA < 0) fail('境③: 未找到深水断面 ShaderMaterial');
  else ok(`境③: 深水断面 uFade=${faceA.toFixed(2)} 由 setFade 统一驱动`);
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

/* 拼音抽查（题目指定的多音字） */
const expect = { '将': 'jiāng', '踏': 'tà', '乘': 'chéng', '欲': 'yù', '尺': 'chǐ', '及': 'jí', '伦': 'lún', '潭': 'tán', '闻': 'wén' };
POEM.forEach(p => p.segs.forEach(seg => {
  const chars = [...seg.c].filter(c => !/[，。、！？；：…—·]/.test(c));
  chars.forEach((c, i) => {
    if (expect[c] && seg.p[i] && !seg.p[i].startsWith(expect[c]))
      fail(`注音: 「${c}」应读 ${expect[c]}，现为 ${seg.p[i]}（上下文：${seg.c}）`);
  });
}));
ok('指定多音字抽查完成（将/踏/乘/欲/尺/及/伦/潭/闻）');

console.log(failures ? `\n共 ${failures} 处失败` : '\n深度冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
