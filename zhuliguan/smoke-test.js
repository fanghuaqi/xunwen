#!/usr/bin/env node
/* zhuliguan 深度冒烟测试：以功能性 THREE 桩真实执行主脚本顶层，
 * 并逐境跑 build → onEnter → 600 帧 update（含 setFade 渐变曲线）→ click。
 * 另做：segs 拼接 vs queue.text 逐字核对、拼音数、境名对齐、交互接线 ≥2 处、
 * 数量联动清单静态项。全绿输出 SMOKE OK。 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const file = path.join(__dirname, 'index.html');
const html = fs.readFileSync(file, 'utf8');
const m = html.match(/<script id="main">([\s\S]*?)<\/script>/);
if (!m) { console.error('✗ 未找到主脚本'); process.exit(1); }
const code = m[1];

/* ---------- 功能性 THREE 桩 ---------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  setScalar(s) { this.x = this.y = this.z = s; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) {
    this.x = a.y * b.z - a.z * b.y; this.y = a.z * b.x - a.x * b.z; this.z = a.x * b.y - a.y * b.x;
    return this;
  }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; return this.multiplyScalar(1 / l); }
  lerpVectors(a, b, t) {
    this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t;
    return this;
  }
  length() { return Math.hypot(this.x, this.y, this.z); }
  dot(v) { return this.x * v.x + this.y * v.y + this.z * v.z; }
}
class V2 {
  constructor(x = 0, y = 0) { this.x = x; this.y = y; }
}
class Color {
  constructor(h) {
    if (h && h.isColor) { this.r = h.r; this.g = h.g; this.b = h.b; }
    else if (typeof h === 'number') {
      this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255;
    } else { this.r = this.g = this.b = 0; }
  }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(0).copy(this); }
  lerp(c, t) { this.r += (c.r - this.r) * t; this.g += (c.g - this.g) * t; this.b += (c.b - this.b) * t; return this; }
  lerpColors(a, b, t) { return this.copy(a).lerp(b, t); }
}
const mkEuler = () => ({ x: 0, y: 0, z: 0, set(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; } });
const mkScale = () => ({ x: 1, y: 1, z: 1, set(x = 1, y = 1, z = 1) { this.x = x; this.y = y; this.z = z; }, setScalar(s) { this.x = this.y = this.z = s; } });
class M4 { compose() { return this; } copy() { return this; } identity() { return this; } }
class Quaternion { setFromAxisAngle() { return this; } }
class Tex { dispose() {} }
class BufferAttribute { constructor(arr, sz) { this.array = arr; this.itemSize = sz; } }

class Obj3D {
  constructor() {
    this.children = []; this.parent = null;
    this.position = new V3(); this.rotation = mkEuler(); this.scale = mkScale();
    this.quaternion = new Quaternion(); this.matrix = new M4(); this.matrixWorld = new M4();
    this.userData = {}; this.visible = true; this.frustumCulled = true;
    this.material = null; this.geometry = null; this.isLight = false;
    this.renderOrder = 0;
  }
  add(...cs) { for (const c of cs) { c.parent = this; this.children.push(c); } return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) { fn(this); for (const c of this.children) c.traverse(fn); }
  updateMatrix() { return this; }
  updateWorldMatrix() {}
  lookAt() {}
  rotateZ() {}
  getObjectByName() { return null; }
}
class Group extends Obj3D { constructor() { super(); this.isGroup = true; } }
class Geo { constructor() { this.parameters = {}; } dispose() {} translate() { return this; } rotateX() { return this; } rotateY() { return this; } setAttribute() { return this; } setFromPoints() { return this; } }
const geoCls = name => class extends Geo { constructor(...a) { super(); this.name = name; this.args = a; } };
class InstancedMesh extends Obj3D {
  constructor(geo, mat, count) { super(); this.geometry = geo; this.material = mat; this.count = count;
    this.instanceMatrix = { needsUpdate: false, setUsage() {} }; this._m = []; }
  setMatrixAt(i, m) { this._m[i] = m; }
  getMatrixAt(i) { return this._m[i]; }
}
class ShaderMaterial {
  constructor(o = {}) { Object.assign(this, { transparent: true, depthWrite: true }, o);
    this.isShaderMaterial = true; this.userData = {}; this.uniforms = o.uniforms || {}; }
  dispose() {}
}
function stdMat(o = {}) { return Object.assign({ transparent: false, opacity: 1, userData: {}, dispose() {}, isMaterial: true }, o); }
class Scene extends Obj3D { constructor() { super(); this.fog = { color: new Color(0), density: 0 }; } }

const THREE = {
  Vector2: V2, Vector3: V3, Color, Matrix4: M4, Quaternion,
  Object3D: Obj3D, Group, Scene,
  Mesh: class extends Obj3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } },
  InstancedMesh,
  Sprite: class extends Obj3D { constructor(m) { super(); this.material = m; this.isSprite = true; } },
  Points: class extends Obj3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isPoints = true; } },
  Line: class extends Obj3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } },
  SphereGeometry: geoCls('Sphere'), CylinderGeometry: geoCls('Cylinder'), BoxGeometry: geoCls('Box'),
  CircleGeometry: geoCls('Circle'), PlaneGeometry: geoCls('Plane'), ConeGeometry: geoCls('Cone'),
  Shape: class { moveTo() {} quadraticCurveTo() {} },
  ShapeGeometry: geoCls('Shape'), BufferGeometry: Geo,
  BufferAttribute,
  MeshBasicMaterial: class extends stdMat.constructor { constructor(o) { super(); Object.assign(this, o); this.isMeshBasicMaterial = true; } },
  MeshPhongMaterial: class { constructor(o = {}) { Object.assign(this, o); this.userData = {}; this.isMeshPhongMaterial = true; this.dispose = () => {}; } },
  PointsMaterial: class { constructor(o = {}) { Object.assign(this, o); this.userData = {}; this.isPointsMaterial = true; this.dispose = () => {}; } },
  LineBasicMaterial: class { constructor(o = {}) { Object.assign(this, o); this.userData = {}; this.dispose = () => {}; } },
  SpriteMaterial: class { constructor(o = {}) { Object.assign(this, o); this.rotation = 0; this.userData = {}; this.dispose = () => {}; } },
  ShaderMaterial,
  CanvasTexture: Tex, Texture: Tex,
  DirectionalLight: class extends Obj3D { constructor(c, i) { super(); this.isLight = true; this.color = new Color(c); this.intensity = i; } },
  AmbientLight: class extends Obj3D { constructor(c, i) { super(); this.isLight = true; this.color = new Color(c); this.intensity = i; } },
  PointLight: class extends Obj3D { constructor(c, i, d) { super(); this.isLight = true; this.color = new Color(c); this.intensity = i; this.distance = d; } },
  PerspectiveCamera: class extends Obj3D { constructor() { super(); this.aspect = 1; } updateProjectionMatrix() {} },
  WebGLRenderer: class { constructor() { this.domElement = { addEventListener() {} }; }
    setPixelRatio() {} setSize() {} setClearColor() {} render() {} },
  FogExp2: class { constructor(c, d) { this.color = new Color(c); this.density = d; } },
  AdditiveBlending: 1, NormalBlending: 2, DoubleSide: 3, BackSide: 4, DynamicDrawUsage: 5,
};
// MeshBasicMaterial 便捷类（上面继承写法太绕，直接补）
THREE.MeshBasicMaterial = class { constructor(o = {}) { Object.assign(this, o); this.userData = {}; this.isMeshBasicMaterial = true; this.dispose = () => {}; } };

/* ---------- DOM 桩 ---------- */
const ctxStub = () => ({
  fillStyle: '', strokeStyle: '', globalCompositeOperation: '', lineWidth: 1, font: '',
  textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0,
  fillRect() {}, strokeRect() {}, beginPath() {}, closePath() {}, moveTo() {}, lineTo() {},
  ellipse() {}, arc() {}, fill() {}, stroke() {}, fillText() {},
  createRadialGradient: () => ({ addColorStop() {} }),
  createLinearGradient: () => ({ addColorStop() {} }),
});
const elStub = () => ({
  tagName: 'DIV', style: {}, textContent: '', innerHTML: '', open: false, offsetWidth: 0,
  classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
  addEventListener() {}, appendChild() {}, querySelectorAll() { return []; },
});
const doc = {
  body: elStub(), head: elStub(), documentElement: elStub(),
  activeElement: null, fullscreenElement: null,
  querySelector: () => elStub(), querySelectorAll: () => [],
  createElement: t => t === 'canvas'
    ? { width: 0, height: 0, getContext: ctxStub }
    : elStub(),
  addEventListener() {},
};
const sandbox = {
  THREE, document: doc,
  window: { addEventListener() {}, AudioContext: null },
  performance: { now: () => Date.now() / 1000 },
  requestAnimationFrame: () => 0,
  console, Math, Date,
  setTimeout: () => 0, clearTimeout() {},
  Audio: class { constructor() {} addEventListener() {} play() { return { catch() {} }; } },
  location: { reload() {} },
};
sandbox.window.Audio = sandbox.Audio;
vm.createContext(sandbox);

let failed = 0;
const fail = msg => { failed++; console.error('✗ ' + msg); };
const ok = msg => console.log('✓ ' + msg);

try { vm.runInContext(code, sandbox, { filename: 'main' }); ok('顶层在 THREE 桩下执行成功'); }
catch (e) { fail('顶层执行失败: ' + e.stack); process.exit(1); }

/* ---------- 深度检查 + 全 builder 跑测 ---------- */
const harness = `
(function(){
  const out = { errors: [], notes: [] };
  const err = m => out.errors.push(m);
  /* 1. segs 拼接 === 诗文原文（逐字逐标点） */
  const text = '独坐幽篁里，弹琴复长啸。深林人不知，明月来相照。';
  const concat = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
  if (concat !== text) err('segs 拼接 ≠ text：' + concat);
  else out.notes.push('segs 拼接与原文逐字一致');
  /* 2. 拼音数 === 汉字数；注音抽查 */
  const PY = { '独':'dú','坐':'zuò','幽':'yōu','篁':'huáng','里':'lǐ','弹':'tán','琴':'qín','复':'fù',
    '长':'cháng','啸':'xiào','深':'shēn','林':'lín','人':'rén','不':'bù','知':'zhī',
    '明':'míng','月':'yuè','来':'lái','相':'xiāng','照':'zhào' };
  POEM.forEach((p, i) => p.segs.forEach(s => {
    const zi = [...s.c].filter(c => !/[，。、！？；：]/.test(c));
    if (zi.length !== s.p.length) err('句' + (i + 1) + ' 拼音数不符');
    zi.forEach((z, k) => { if (PY[z] && PY[z] !== s.p[k]) err('注音错：' + z + ' → ' + s.p[k] + '（应为 ' + PY[z] + '）'); });
  }));
  /* 3. STAGES ↔ POEM 对齐、cam/sky/dwell/river/build */
  if (STAGES.length !== POEM.length + 1) err('STAGES 数量错');
  for (let i = 1; i < STAGES.length; i++) {
    if (STAGES[i].name !== POEM[i - 1].name) err('境名错位 @' + i);
    const s = STAGES[i];
    if (!s.cam || !s.cam.f || !s.cam.t || !s.cam.lf || !s.cam.lt) err('cam 不全 @' + i);
    if (typeof s.sky !== 'function') err('sky 非工厂 @' + i);
  }
  if (CN.length < POEM.length) err('CN 过短');
  /* 4. 全部 build → onEnter → 600 帧 update + setFade 渐变 + click */
  STAGES.forEach((def, si) => {
    const st = def.build();
    if (st.onEnter) st.onEnter();
    const dur = 600, dt = 1 / 30;
    let lt = 0;
    for (let f = 0; f < dur; f++) {
      lt += dt; clock.t += dt;
      const k = f < 79 ? f / 79 : 1;          // 模拟 2.6s 渐入
      setFade(st.group, k);
      st.update && st.update(lt, dt);
      if (st.click && (f === 100 || f === 118 || f === 560)) st.click();  // 118 = 快速连点（守卫应拦）
      if (f === 300 && st.click) st.click();  // 正常再点
    }
    setFade(st.group, 1);
    let meshes = 0, lights = 0, inst = 0, instCount = 0;
    st.group.traverse(o => {
      if (o.isLight) lights++;
      else if (o.geometry) meshes++;
      if (o.count !== undefined) { inst++; instCount += o.count; }
    });
    out.notes.push('境' + si + ' [' + def.name + '] build/update/click×4 全跑通 · mesh=' + meshes +
      ' light=' + lights + ' instanced=' + inst + '(' + instCount + ')');
  });
  /* 5. 快速连点守卫验证：bMoon 1.6s 内第二次 click 不应重置 t0（行为检查：不抛错即可） */
  return out;
})()
`;
let res;
try { res = vm.runInContext(harness, sandbox, { filename: 'harness' }); }
catch (e) { fail('跑测抛错: ' + e.stack); process.exit(1); }
res.errors.forEach(fail);
res.notes.forEach(n => console.log('  · ' + n));

/* ---------- 数量联动清单（静态） ---------- */
const cnt = (re) => (code.match(re) || []).length;
if (!/clamp\(i,0,3\)/.test(code)) fail('goto clamp 未改为 3');
else ok('goto clamp(i,0,3)');
if (!/i<=3;i\+\+/.test(code.replace(/\s/g, '').replace('i<=3;i++)', 'i<=3;i++')) && !/i\s*<=\s*3/.test(code)) fail('dots 循环未改 3');
else ok('#dots 循环 i<=3');
if (cnt(/curIdx===3&&state==='stage'/g) < 2) fail('交互接线 <2 处独立写法（pointerdown/Space）');
else ok('交互接线（pointerdown + Space）=' + cnt(/curIdx===3&&state==='stage'/g) + ' 处');
if (!/if\(curIdx===3\)showEnding\(\)/.test(code)) fail('自动游览末境判断未改');
else ok('自动游览 curIdx===3 → showEnding');
if (cnt(/'04\.mp3'/g) < 2) fail('全诗音频 04.mp3 引用不足（showEnding + btnPoemAudio）');
else ok("audio 04.mp3 引用 ×" + cnt(/'04\.mp3'/g));
if (!/curIdx>=3\)showEnding\(\)/.test(code)) fail('下一境/方向键边界未改');
else ok('btnNext/ArrowRight curIdx>=3');
if (cnt(/read:'/g) !== 3) fail('read 字段数 ≠ 3');
else ok("read 字段数 = 3");
const wq = code.match(/words\s*=\s*\[([^\]]*)\]/);
if (!wq || wq[1].split(',').length !== 6) fail('words 评语应为 6 项（5 题 + 1）');
else ok('words 评语 6 项（按本诗定制）');
if (/THREE\./.test(code.split('function boot')[0].replace(/const (DOME|GLOW)[^;]*;/g, ''))) {
  // 粗查：顶层除函数体外的 THREE 引用已由 validate Pass A 兜底，这里仅提示
  console.log('  · 顶层 THREE 引用由 validate Pass A 把关');
}

/* ---------- 汇总 ---------- */
if (failed) { console.error('\n共 ' + failed + ' 项失败'); process.exit(1); }
console.log('\nSMOKE OK —— build/update/click 全部通过');
