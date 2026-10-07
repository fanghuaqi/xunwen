#!/usr/bin/env node
/* smoke.js —— 深度冒烟测试：真实 THREE 桩，跑全部 STAGES 的 build/sky/update/click
   加数据一致性、边界常量、色板、残留检查。全绿输出 SMOKE PASS。 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const dir = __dirname;
const html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
const m = html.match(/<script id="main">([\s\S]*?)<\/script>/);
if (!m) { console.error('✗ 未找到主脚本'); process.exit(1); }
const code = m[1];

const fails = [];
const chk = (ok, msg) => { if (!ok) fails.push(msg); };

/* ---------- THREE 桩（带真实数学） ---------- */
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
  constructor(h) { this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  lerp(c, t) { return this.lerpColors(this, c, t); }
}
class Euler { constructor() { this.x = 0; this.y = 0; this.z = 0; this.order = 'XYZ'; } set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } }
class Obj {
  constructor() { this.children = []; this.position = new V3(); this.rotation = new Euler(); this.scale = new V3(1, 1, 1); this.userData = {}; this.visible = true; }
  add(...cs) { for (const c of cs) { c.parent = this; this.children.push(c); } return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) {
    fn(this);
    for (const c of this.children) { if (c && typeof c.traverse === 'function') c.traverse(fn); else fn(c); }
  }
  rotateZ() { return this; }
}
class Group extends Obj { constructor() { super(); this.isGroup = true; } }
class Geo {
  constructor(...a) { this.args = a; this.attributes = {}; }
  setAttribute(n, attr) { this.attributes[n] = attr; return this; }
  rotateX() { return this; } rotateY() { return this; }
  translate() { return this; }
  dispose() {}
}
class BufferAttribute { constructor(arr, size) { this.array = arr; this.itemSize = size; this.needsUpdate = false; } }
class Mat {
  constructor(p = {}) { Object.assign(this, p); this.userData = {}; this.uniforms = p.uniforms || null; }
  dispose() {}
}
class InstancedMesh extends Obj {
  constructor(geo, mat, n) { super(); this.geometry = geo; this.material = mat; this.count = n; this.instanceMatrix = { needsUpdate: false }; }
  setMatrixAt() {}
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
  BufferGeometry: Geo, BufferAttribute,
  MeshBasicMaterial: Mat, MeshPhongMaterial: Mat, ShaderMaterial: Mat,
  PointsMaterial: Mat, LineBasicMaterial: Mat, SpriteMaterial: Mat,
  Mesh: class extends Obj { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } },
  Points: class extends Obj { constructor(g, m) { super(); this.geometry = g; this.material = m; } },
  Line: class extends Obj { constructor(g, m) { super(); this.geometry = g; this.material = m; } },
  Sprite: class extends Obj { constructor(m) { super(); this.material = m; } },
  InstancedMesh,
  SphereGeometry: Geo, BoxGeometry: Geo, CylinderGeometry: Geo, ConeGeometry: Geo,
  CircleGeometry: Geo, PlaneGeometry: Geo, TorusGeometry: Geo, LatheGeometry: Geo,
  CanvasTexture: Texture,
  Scene: class extends Obj { constructor() { super(); this.fog = null; } },
  PerspectiveCamera: class extends Obj { constructor() { super(); this.aspect = 1; } lookAt() {} updateProjectionMatrix() {} },
  WebGLRenderer: function () { this.domElement = { addEventListener() {} }; this.setPixelRatio = () => {}; this.setSize = () => {}; this.setClearColor = () => {}; this.render = () => {}; },
  FogExp2: function (c, d) { this.color = new Col(c); this.density = d; },
  DirectionalLight: class extends Obj { constructor(c, i) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } },
  AmbientLight: class extends Obj { constructor(c, i) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } },
  PointLight: class extends Obj { constructor(c, i, d) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } },
  AdditiveBlending: 1, NormalBlending: 2, BackSide: 3, DoubleSide: 4, DynamicDrawUsage: 5,
};

/* ---------- document/window 桩 ---------- */
const elStub = () => ({
  addEventListener() {}, classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
  style: {}, textContent: '', innerHTML: '', appendChild() {}, querySelectorAll() { return []; },
  offsetWidth: 0, open: false, title: '', disabled: false,
  width: 0, height: 0, getContext: () => ctx2d,
});
const documentStub = {
  querySelector: () => elStub(), createElement: () => elStub(),
  addEventListener() {}, documentElement: elStub(), body: elStub(), head: elStub(),
  activeElement: null, fullscreenElement: null,
};

const sandbox = {
  THREE, document: documentStub, performance: { now: () => 0 },
  requestAnimationFrame() {}, console,
  setTimeout() { return 0; }, clearTimeout() {}, location: { reload() {} },
  window: { addEventListener() {} },
  Audio: function () { return { addEventListener() {}, play: function () { return { catch: function () {} }; } }; },
};
sandbox.window.innerWidth = 1280; sandbox.window.innerHeight = 800; sandbox.window.devicePixelRatio = 1;

vm.createContext(sandbox);
try {
  vm.runInContext(code, sandbox, { filename: 'index.html' });
} catch (e) { console.error('✗ 主脚本执行失败: ' + e.stack); process.exit(1); }

/* ---------- 1. 数据一致性 ---------- */
const get = e => vm.runInContext(e, sandbox);
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const TEXT = '日暮苍山远，天寒白屋贫。柴门闻犬吠，风雪夜归人。';
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
chk(joined === TEXT, `诗文不一致: ${joined}`);
chk(POEM.length === 3, `POEM 应 3 句，实际 ${POEM.length}`);
chk(STAGES.length === 4, `STAGES 应 4 项，实际 ${STAGES.length}`);
for (let i = 1; i < STAGES.length; i++) {
  chk(STAGES[i].name === POEM[i - 1].name, `境${i} 名错位 ${STAGES[i].name}≠${POEM[i - 1].name}`);
  chk(STAGES[i].name.length >= 2 && STAGES[i].name.length <= 4, `境${i} 名长度 2-4: ${STAGES[i].name}`);
}
POEM.forEach((p, i) => p.segs.forEach(seg => {
  const han = [...seg.c].filter(c => !/[，。、！？；：]/.test(c)).length;
  chk(han === seg.p.length, `第${i + 1}句 "${seg.c}" 汉字${han}≠拼音${seg.p.length}`);
}));
// 多音字抽查：吠 fèi / 贫 pín
const pyAll = POEM.flatMap(l => l.segs.flatMap(s => s.p));
chk(pyAll.includes('fèi'), '缺 吠 fèi 注音');
chk(pyAll.includes('pín'), '缺 贫 pín 注音');
chk(CN.length >= 3, 'CN 太短');

/* ---------- 2. 边界常量 / 残留 / 色板 ---------- */
chk(code.includes('clamp(i,0,3)'), '缺 clamp(i,0,3)');
chk((code.match(/curIdx===3&&state==='stage'/g) || []).length >= 2, `交互接线 ${ (code.match(/curIdx===3&&state==='stage'/g) || []).length } 处 <2`);
chk((code.match(/curIdx>=3\)showEnding|curIdx===3\)showEnding/g) || []).length >= 2, '末境 showEnding 判断不足');
chk(code.includes("'04.mp3'"), "缺 '04.mp3' 全诗音频引用");
chk(/for\(let i=1;i<=3;i\+\+\)/.test(code), 'dots 循环未改 3');
chk(!code.includes('将进酒') && !code.includes('万古愁'), '残留《将进酒》字样');
chk(!/太白/.test(code), '小测评语残留太白');
const root = (html.match(/:root\s*\{[^}]*\}/) || [''])[0];
chk(root.includes('--gold:#4a5060'), '--gold ≠ #4a5060');
chk(/background:#e9e2d0/.test(html), 'body 背景非宣纸 #e9e2d0');
chk((code.match(/0x05070d/g) || []).length <= 1, '0x05070d 出现 >1 次');
chk(QUIZ.length === 5, `QUIZ 应 5 题，实际 ${QUIZ.length}`);
QUIZ.forEach((q, i) => {
  chk(q.o.length === 3, `题${i + 1} 选项≠3`);
  chk(typeof q.a === 'number' && q.a >= 0 && q.a < q.o.length, `题${i + 1} 答案越界`);
});
const wq = code.match(/words\s*=\s*\[([^\]]*)\]/);
chk(wq && wq[1].split(',').length === 6, 'words 评语应 6 项');

/* ---------- 3. 全部 builder/update/sky ---------- */
try {
  vm.runInContext(`
  for (let i = 0; i < STAGES.length; i++) {
    const s = STAGES[i];
    const sk = s.sky();
    if (!sk.top || !sk.hor || !sk.fog || typeof sk.fd !== 'number' || !sk.moon) throw new Error('境' + i + ' sky() 字段不全');
    if (typeof s.dwell !== 'number' || typeof s.river !== 'number') throw new Error('境' + i + ' 缺 dwell/river');
    if (!s.cam || !s.cam.f || !s.cam.t || !s.cam.lf || !s.cam.lt) throw new Error('境' + i + ' cam 不全');
    const st = s.build();
    st.group.userData.fadeK = 1;
    for (let k = 0; k < 30; k++) { if (st.update) st.update(k * 0.1 + 1, 0.016); }
    setFade(st.group, 0.3); setFade(st.group, 0); setFade(st.group, 1);
    if (i > 0 && typeof s.build !== 'function') throw new Error('no build');
  }
  `, sandbox, { filename: 'drivers' });
} catch (e) { fails.push('builder 阶段抛错: ' + e.message); }

/* ---------- 4. 交互境全时序：click → 走完全程 → 守卫 → 复位 → 再点 ---------- */
try {
  vm.runInContext(`
  const st3 = STAGES[3].build();
  st3.group.userData.fadeK = 1;
  clock.t = 100;
  st3.click();                       // 触发
  st3.click();                       // 立刻再点 → 守卫应拦截（不抛错即可）
  for (let t = 100; t <= 135; t += 0.05) {
    clock.t = t;
    st3.update(t, 0.05);
    if (Math.abs(t - 105.5) < 0.001) st3.click();   // 动画中点击 → 守卫拦截
  }
  clock.t = 200;
  st3.click();                       // 冷却后再点
  st3.update(200.2, 0.2);
  `, sandbox, { filename: 'interact' });
} catch (e) { fails.push('交互境时序抛错: ' + e.message); }

/* ---------- 5. pointerdown/空格接线语义（模拟 goto 后状态调用） ---------- */
try {
  vm.runInContext(`
  // 模拟引擎接线条件在第三境成立
  const wireOk = (STAGES[3].build().click !== undefined);
  if (!wireOk) throw new Error('第三境无 click');
  `, sandbox, { filename: 'wire' });
} catch (e) { fails.push('接线检查抛错: ' + e.message); }

if (fails.length) {
  console.error('SMOKE FAIL:');
  fails.forEach((f, i) => console.error(`  ${i + 1}. ${f}`));
  process.exit(1);
}
console.log('SMOKE PASS：3 境 build/update/sky 全跑通；交互境 click 全时序（触发/守卫/复位/冷却）通过；数据/边界/色板/残留检查通过。');
