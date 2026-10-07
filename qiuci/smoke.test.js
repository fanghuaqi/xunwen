/* qiuci 深度冒烟测试：真实 THREE 桩 + 完整 DOM 桩，跑 boot/goto/animate/setFade/click/quiz
 * 用法: node smoke.test.js   （全绿输出 SMOKE OK；任何断言失败退出码 1）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];

/* ---------- 数学桩 ---------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { if (typeof x === 'object') { this.x = x.x; this.y = x.y; this.z = x.z; return this; } this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  lerpVectors(a, b, t) { this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) { this.x = a.y * b.z - a.z * b.y; this.y = a.z * b.x - a.x * b.z; this.z = a.x * b.y - a.y * b.x; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; this.x /= l; this.y /= l; this.z /= l; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  lerp(v, t) { this.x += (v.x - this.x) * t; this.y += (v.y - this.y) * t; this.z += (v.z - this.z) * t; return this; }
  setScalar(s) { this.x = s; this.y = s; this.z = s; return this; }
  length() { return Math.hypot(this.x, this.y, this.z); }
  distanceTo(v) { return Math.hypot(this.x - v.x, this.y - v.y, this.z - v.z); }
}
class Color {
  constructor(h = 0xffffff, g, b) {
    if (g !== undefined) { this.r = h; this.g = g; this.b = b; }
    else if (typeof h === 'number') { this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; }
    else { this.r = 1; this.g = 0; this.b = 1; }
  }
  set(h) { if (typeof h === 'number') { this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; } return this; }
  setRGB(r, g, b) { this.r = r; this.g = g; this.b = b; return this; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(this.r, this.g, this.b); }
  lerp(c, a) { this.r += (c.r - this.r) * a; this.g += (c.g - this.g) * a; this.b += (c.b - this.b) * a; return this; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  offsetHSL() { return this; }
  getHex() { return (Math.round(this.r * 255) << 16) | (Math.round(this.g * 255) << 8) | Math.round(this.b * 255); }
}
/* ---------- 场景图桩 ---------- */
class Object3D {
  constructor() {
    this.children = []; this.parent = null;
    this.position = new V3(); this.scale = new V3(1, 1, 1);
    this.rotation = { x: 0, y: 0, z: 0, set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } };
    this.userData = {}; this.visible = true; this.renderOrder = 0; this.frustumCulled = true;
  }
  add(...os) { for (const o of os) { if (!o) continue; o.parent = this; this.children.push(o); } return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(cb) { cb(this); for (const c of this.children.slice()) { if (c && c.traverse) c.traverse(cb); else cb(c); } }
  rotateOnAxis() { return this; }
  rotateZ() { return this; }
  lookAt() { return this; }
  updateMatrix() { }
  clear() { this.children.length = 0; return this; }
}
class Group extends Object3D { constructor() { super(); this.isGroup = true; } }
class Mesh extends Object3D {
  constructor(geo, mat) { super(); this.geometry = geo; this.material = mat; this.isMesh = true; }
}
class Points extends Object3D { constructor(geo, mat) { super(); this.geometry = geo; this.material = mat; this.isPoints = true; } }
class Line extends Object3D { constructor(geo, mat) { super(); this.geometry = geo; this.material = mat; } }
class Sprite extends Object3D { constructor(mat) { super(); this.material = mat; this.isSprite = true; } }
class Light extends Object3D {
  constructor(c, i) { super(); this.color = new Color(c === undefined ? 0xffffff : c); this.intensity = i === undefined ? 1 : i; this.isLight = true; }
}
class DirectionalLight extends Light { }
class AmbientLight extends Light { }
class PointLight extends Light { constructor(c, i, dist) { super(c, i); this.distance = dist || 0; } }
/* ---------- 几何桩 ---------- */
class Geometry { constructor(...a) { this.args = a; this.attributes = {}; this.parameters = {}; } rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; } dispose() { } }
class BufferGeometry extends Geometry {
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  setFromPoints(pts) { const arr = new Float32Array(pts.length * 3); pts.forEach((p, i) => { arr[i * 3] = p.x; arr[i * 3 + 1] = p.y; arr[i * 3 + 2] = p.z; }); this.attributes.position = { array: arr, itemSize: 3, count: pts.length }; return this; }
}
class BufferAttribute { constructor(arr, size) { this.array = arr; this.itemSize = size; this.needsUpdate = false; this.count = arr.length / size; } }
/* ---------- 材质桩 ---------- */
function normColor(m, keys) { for (const k of keys) if (typeof m[k] === 'number') m[k] = new Color(m[k]); }
class Material {
  constructor(p = {}) {
    Object.assign(this, { color: 0xffffff, opacity: 1, transparent: false, depthWrite: true, side: 0 }, p);
    normColor(this, ['color', 'emissive', 'specular']);
    this.userData = {};
  }
  dispose() { }
}
class MeshBasicMaterial extends Material { constructor(p) { super(p); this.isMaterial = true; } }
class MeshPhongMaterial extends Material { constructor(p) { super(p); this.isMaterial = true; if (!this.emissive) this.emissive = new Color(0); } }
class PointsMaterial extends Material { constructor(p) { super(p); this.isMaterial = true; } }
class LineBasicMaterial extends Material { constructor(p) { super(p); this.isMaterial = true; } }
class SpriteMaterial extends Material { constructor(p) { super(p); this.isMaterial = true; this.rotation = 0; } }
class ShaderMaterial extends Material {
  constructor(p = {}) { super(p); this.isShaderMaterial = true; this.uniforms = p.uniforms || {}; this.vertexShader = p.vertexShader; this.fragmentShader = p.fragmentShader; }
}
class CanvasTexture { constructor(c) { this.image = c; } dispose() { } }
/* ---------- 相机/渲染器 ---------- */
class PerspectiveCamera extends Object3D {
  constructor(fov, aspect) { super(); this.fov = fov; this.aspect = aspect; this.projectionMatrix = {}; }
  updateProjectionMatrix() { }
}
class WebGLRenderer {
  constructor() {
    const handlers = {};
    this.domElement = {
      addEventListener(h, f) { (handlers[h] = handlers[h] || []).push(f); },
      _handlers: handlers, style: {},
    };
  }
  setPixelRatio() { } setSize() { } render() { } setClearColor() { }
}
class FogExp2 { constructor(c, d) { this.color = new Color(c); this.density = d; } }
class Scene extends Object3D { constructor() { super(); this.fog = null; this.background = null; } }
class Vector2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class Object3D_Dummy extends Object3D { }

const THREE = {
  Vector2, Vector3: V3, Color, Object3D, Group, Mesh, Points, Line, Sprite,
  DirectionalLight, AmbientLight, PointLight,
  SphereGeometry: Geometry, PlaneGeometry: Geometry, CylinderGeometry: Geometry,
  ConeGeometry: Geometry, CircleGeometry: Geometry, RingGeometry: Geometry,
  LatheGeometry: Geometry, TorusGeometry: Geometry, BoxGeometry: Geometry,
  BufferGeometry, BufferAttribute,
  MeshBasicMaterial, MeshPhongMaterial, PointsMaterial, LineBasicMaterial, SpriteMaterial, ShaderMaterial,
  CanvasTexture, FogExp2, Scene, PerspectiveCamera, WebGLRenderer,
  AdditiveBlending: 1, NormalBlending: 2, BackSide: 3, DoubleSide: 4, DynamicDrawUsage: 5,
};

/* ---------- DOM 桩 ---------- */
function makeCtx2d() {
  return {
    createRadialGradient: () => ({ addColorStop() { } }),
    createLinearGradient: () => ({ addColorStop() { } }),
    fillRect() { }, fillText() { }, clearRect() { },
    font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
  };
}
function makeEl(tag) {
  const handlers = {};
  const el = {
    tagName: (tag || 'div').toUpperCase(), handlers, style: {}, open: false, title: '',
    textContent: '', className: '', id: '', offsetWidth: 0, disabled: false,
    classList: { add() { }, remove() { }, toggle() { return false; }, contains() { return false; } },
    addEventListener(h, f) { (handlers[h] = handlers[h] || []).push(f); },
    appendChild(c) { (el.children = el.children || []).push(c); return c; },
    querySelectorAll() { return []; },
    blur() { },
  };
  return el;
}
const els = {};
let NOW = 0;
let rafCb = null;
const winHandlers = {};

const document = {
  createElement: tag => (tag === 'canvas' ? { width: 0, height: 0, getContext: makeCtx2d, style: {} } : makeEl(tag)),
  querySelector: s => (els[s] = els[s] || makeEl('div')),
  querySelectorAll: () => [],
  body: makeEl('body'), head: makeEl('head'), documentElement: makeEl('html'),
  activeElement: null, fullscreenElement: null,
  getElementById: id => (els['#' + id] = els['#' + id] || makeEl('div')),
  addEventListener() { },
};

const sandbox = {
  THREE, document,
  window: { innerWidth: 1280, innerHeight: 720, devicePixelRatio: 1, addEventListener(h, f) { (winHandlers[h] = winHandlers[h] || []).push(f); } },
  performance: { now: () => NOW },
  requestAnimationFrame: cb => { rafCb = cb; },
  setTimeout: (fn) => { pendingTimers.push(fn); return pendingTimers.length - 1; },
  clearTimeout: (id) => { if (typeof id === 'number') pendingTimers[id] = null; },
  location: { reload() { } },
  console,
};
sandbox.window.AudioContext = undefined;
const pendingTimers = [];
sandbox.Audio = undefined; // new Audio → throw → 走 speak() 兜底
vm.createContext(sandbox);
let failures = 0;
const ok = (cond, msg) => { if (cond) console.log('  ok  ' + msg); else { failures++; console.error('  FAIL ' + msg); } };

/* ---------- Pass A：无 THREE 顶层安全 ---------- */
{
  const sA = { document: { querySelector: makeEl, createElement: makeEl, addEventListener() { }, documentElement: makeEl(), body: makeEl(), head: makeEl(), activeElement: null, fullscreenElement: null }, window: {}, performance: { now: () => 0 }, requestAnimationFrame() { }, console, setTimeout() { return 0; }, clearTimeout() { } };
  sA.window.addEventListener = () => { };
  vm.createContext(sA);
  try { vm.runInContext(code, sA, { filename: 'passA' }); ok(true, '顶层在无 THREE 时安全执行'); }
  catch (e) { ok(false, '顶层在无 THREE 时崩溃: ' + e.message); }
}

/* ---------- 主执行 ---------- */
vm.runInContext(code, sandbox, { filename: 'main' });
const run = s => vm.runInContext(s, sandbox, { filename: s });

function frames(n, step = 33) {
  for (let i = 0; i < n; i++) {
    NOW += step;
    // 触发挂起的定时器（tip/自动朗读）
    for (let k = 0; k < pendingTimers.length; k++) { const f = pendingTimers[k]; if (f) { pendingTimers[k] = null; f(); } }
    const cb = rafCb; rafCb = null;
    if (cb) cb();
    if (!rafCb) throw new Error('animate 未重新调度 rAF');
  }
}
const findInScene = pred => { let hit = null; run('scene').traverse(o => { if (!hit && pred(o)) hit = o; }); return hit; };

console.log('== 1. boot 与封面 ==');
run('boot()');
ok(run('state') === 'stage', 'boot 后 state=stage');
ok(run('STAGES').length === 4 && run('POEM').length === 3, 'STAGES=4, POEM=3');
frames(80);
ok(true, '封面 80 帧跑完');

console.log('== 2. 数据断言 ==');
const joined = run("POEM.map(l=>l.segs.map(s=>s.c).join('')).join('')");
const EXPECT = '自古逢秋悲寂寥，我言秋日胜春朝。晴空一鹤排云上，便引诗情到碧霄。';
ok(joined === EXPECT, 'POEM 拼接与 queue.text 逐字一致');
let pyOK = true;
run('POEM').forEach(l => l.segs.forEach(s => {
  const han = [...s.c].filter(c => !/[，。、！？；：]/.test(c)).length;
  if (han !== s.p.length) pyOK = false;
}));
ok(pyOK, '每句汉字数=拼音数');
ok([1, 2, 3].every(i => run('STAGES')[i].name === run('POEM')[i - 1].name), 'STAGES[i].name===POEM[i-1].name');
ok(/curIdx===3&&state==='stage'/.test(html) && (html.match(/curIdx===3&&state==='stage'/g) || []).length >= 2, '交互接线 ≥2 处 (pointerdown+空格)');
ok(html.includes("'04.mp3'"), "引用全诗音频 '04.mp3'");
ok(run('QUIZ').length === 5 && run('QUIZ').every(q => q.o.length === 3), '小测 5 题 ×3 选项');

console.log('== 3. 壹境 悲寂寥 ==');
run('goto(1)');
frames(100);   // 过渡 2.6s + 入境
ok(run('curIdx') === 1 && run('state') === 'stage', '进入壹境');
frames(260);
ok(true, '壹境 260 帧跑完（落叶/悲雾/寒鸦）');

console.log('== 4. 贰境 胜春朝 ==');
run('goto(2)');
frames(100);
ok(run('curIdx') === 2 && run('state') === 'stage', '进入贰境');
frames(220);
ok(true, '贰境 220 帧跑完（朝阳/金叶/鹤影）');

console.log('== 5. 叁境 鹤排碧霄 + 交互 ==');
run('goto(3)');
frames(100);
ok(run('curIdx') === 3 && run('state') === 'stage', '进入叁境');
const pointerHandlers = run('renderer').domElement._handlers['pointerdown'] || [];
ok(pointerHandlers.length === 1, 'renderer.domElement 已接 pointerdown');
pointerHandlers[0]({ clientX: 640, clientY: 360 });       // 点击：鹤穿云+金流
frames(30);
const goldMid = findInScene(o => o.material && o.material.uniforms && o.material.uniforms.uMaxA && o.material.uniforms.uFall === undefined && o.geometry && o.geometry.attributes.aSeed && o.material.uniforms.uRise && o.material.uniforms.uRise.value === 1);
ok(!!goldMid, '找到诗情金流 Points(rise=1)');
frames(70);    // act≈3.3s：爬升中段、云已排开
const crane = findInScene(o => o.userData && o.userData.isCrane);
ok(!!crane, '找到鹤');
ok(crane.position.y > 20 && crane.position.y < 60, '鹤爬升中（缓起） y=' + crane.position.y.toFixed(1));
const cloud = findInScene(o => o.userData && o.userData.homeX !== undefined);
ok(cloud && Math.abs(cloud.position.x - cloud.userData.homeX) > 8, '云被排开 offset=' + (cloud ? (cloud.position.x - cloud.userData.homeX).toFixed(1) : 'n/a'));
ok(goldMid && goldMid.material.uniforms.uMaxA.value > 0.4, '金流已起 uMaxA=' + (goldMid ? goldMid.material.uniforms.uMaxA.value.toFixed(2) : 'n/a'));
frames(160);   // act≈8.6s：登顶
ok(crane.position.y > 110, '鹤已登顶 y=' + crane.position.y.toFixed(1));
ok(goldMid.material.uniforms.uMaxA.value < 0.95, '金流包络正常');

console.log('== 6. 防连点守卫 ==');
const yBefore = crane.position.y;
pointerHandlers[0]({ clientX: 0, clientY: 0 });           // 立刻再点 → 应被守卫拦截
frames(6);
ok(crane.position.y > yBefore - 2, '连点被拦截（y 未跳回落点 ' + crane.position.y.toFixed(1) + '）');

console.log('== 7. 空格键交互 + 末境流转 ==');
const keyHandlers = winHandlers['keydown'] || [];
ok(keyHandlers.length === 1, 'window 已接 keydown');
keyHandlers[0]({ code: 'Space', preventDefault() { } });  // 空格触发 click（此刻已 >2.4s，应生效）
frames(40);
ok(true, '空格交互无异常');
keyHandlers[0]({ code: 'ArrowRight', preventDefault() { } });
ok(run('state') === 'ending', '末境 ArrowRight → showEnding');
frames(30);
run('startQuiz()');
ok(true, '小测渲染无异常');
run("hideEnding('cover')");
frames(80);
ok(run('curIdx') === 0 && run('state') === 'stage', '回到封面重新入境');
frames(60);

console.log('== 8. 逐境直接 build（独立冒烟） ==');
for (let i = 0; i < 4; i++) {
  const st = run(`STAGES[${i}].build()`);
  ok(st && st.group && typeof st.update === 'function', `STAGES[${i}] build 返回 group+update`);
  st.update(3.3, 0.033);
  run('setFade')(st.group, 0.42); st.update(4.0, 0.033); run('setFade')(st.group, 1); st.update(4.5, 0.033);
  if (st.click) { st.click(); st.update(5.0, 0.033); }
  ok(true, `STAGES[${i}] update/click(若有) 直跑无异常`);
}

console.log(failures === 0 ? '\nSMOKE OK —— 全部断言通过' : `\nSMOKE FAILED —— ${failures} 个断言失败`);
process.exit(failures === 0 ? 0 : 1);
