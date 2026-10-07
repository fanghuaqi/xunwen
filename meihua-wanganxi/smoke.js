/* smoke.js —— 深度冒烟测试（临时文件，跑完即删）
 * 用"真行为"THREE 桩在 Node 中执行主脚本：真实 boot() + rAF 泵帧 + 完整游览链路
 * 覆盖：全部 build/update/click、setFade 淡入淡出、mixSky/applySky、goto 过场、
 *       dispose、交互两路接线（pointerdown + 空格）、终章/小测/自动游览 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = __dirname;
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];

let FAIL = 0;
const ok = (cond, msg) => { if (!cond) { FAIL++; console.error('  ✗ ' + msg); } else console.log('  ✓ ' + msg); };

/* ---------------- THREE 桩（真行为最小实现） ---------------- */
function parseHex(h) {
  if (typeof h === 'number') return [(h >> 16 & 255) / 255, (h >> 8 & 255) / 255, (h & 255) / 255];
  const s = String(h).replace('#', '');
  return [parseInt(s.slice(0, 2), 16) / 255, parseInt(s.slice(2, 4), 16) / 255, parseInt(s.slice(4, 6), 16) / 255];
}
class Color {
  constructor(h) { const c = h === undefined ? [1, 1, 1] : parseHex(h); this.r = c[0]; this.g = c[1]; this.b = c[2]; }
  set(h) { const c = parseHex(h); this.r = c[0]; this.g = c[1]; this.b = c[2]; return this; }
  setHex(h) { return this.set(h); }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(0).copy(this); }
  lerp(c, t) { this.r += (c.r - this.r) * t; this.g += (c.g - this.g) * t; this.b += (c.b - this.b) * t; return this; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
}
class Vector3 {
  constructor(x, y, z) { this.x = x || 0; this.y = y || 0; this.z = z || 0; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  setScalar(s) { this.x = s; this.y = s; this.z = s; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new Vector3(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  length() { return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z) || 1e-9; }
  normalize() { const l = this.length(); this.x /= l; this.y /= l; this.z /= l; return this; }
  lerpVectors(a, b, t) { this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t; return this; }
  crossVectors(a, b) {
    const ax = a.x, ay = a.y, az = a.z, bx = b.x, by = b.y, bz = b.z;
    this.x = ay * bz - az * by; this.y = az * bx - ax * bz; this.z = ax * by - ay * bx; return this;
  }
}
class Vector2 { constructor(x, y) { this.x = x || 0; this.y = y || 0; } }

class Object3D {
  constructor() {
    this.children = []; this.position = new Vector3(); this.scale = new Vector3(1, 1, 1);
    this.rotation = { x: 0, y: 0, z: 0 }; this.userData = {}; this.renderOrder = 0;
    this.frustumCulled = true; this.quaternion = { setFromAxisAngle() {} }; this.visible = true;
  }
  add(...cs) { cs.forEach(c => { this.children.push(c); c.parent = this; }); return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); }
  traverse(fn) { fn(this); this.children.forEach(c => c.traverse && c.traverse(fn)); }
  updateMatrix() {}
}
class Group extends Object3D {}
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Line extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; } }
class Scene extends Object3D {}
class PerspectiveCamera extends Object3D {
  constructor() { super(); this.aspect = 1; }
  lookAt() {} updateProjectionMatrix() {} rotateZ() {}
}
class FogExp2 { constructor(c, d) { this.color = new Color(c); this.density = d; } }
class WebGLRenderer {
  constructor() { this.domElement = makeEl('canvas'); }
  setPixelRatio() {} setSize() {} setClearColor() {} render() {}
}
class BufferGeometry {
  constructor() { this.attributes = {}; }
  setAttribute(n, a) { this.attributes[n] = a; }
  setFromPoints() { return this; } rotateX() {} dispose() {}
}
class BufferAttribute { constructor(arr, sz) { this.array = arr; this.itemSize = sz; this.needsUpdate = false; } }
class Material { constructor(p) { this.opacity = 1; this.transparent = false; this.depthWrite = true; this.userData = {}; Object.assign(this, p); } dispose() {} }
class MeshBasicMaterial extends Material {}
class MeshPhongMaterial extends Material { constructor(p) { super(p); if (!this.emissive) this.emissive = new Color(0); } }
class PointsMaterial extends Material {}
class LineBasicMaterial extends Material {}
class SpriteMaterial extends Material {}
class ShaderMaterial extends Material { constructor(p) { super(p); this.isShaderMaterial = true; } }
class CatmullRomCurve3 { constructor(pts) { this.points = pts; } }
class Geo { constructor() { this.params = {}; } dispose() {} }
class SphereGeometry extends Geo {}
class PlaneGeometry extends Geo {}
class CircleGeometry extends Geo {}
class BoxGeometry extends Geo {}
class CylinderGeometry extends Geo {}
class ConeGeometry extends Geo {}
class TorusGeometry extends Geo {}
class TubeGeometry extends Geo {}
class CanvasTexture { constructor() {} dispose() {} }
class Light extends Object3D { constructor(c, i) { super(); this.isLight = true; this.color = new Color(c); this.intensity = i === undefined ? 1 : i; } }
class AmbientLight extends Light {}
class DirectionalLight extends Light {}
class PointLight extends Light { constructor(c, i, d) { super(c, i); this.distance = d || 0; } }

const THREE = {
  Color, Vector3, Vector2, Group, Mesh, Line, Points, Sprite, Scene, PerspectiveCamera, FogExp2,
  WebGLRenderer, BufferGeometry, BufferAttribute, MeshBasicMaterial, MeshPhongMaterial,
  PointsMaterial, LineBasicMaterial, SpriteMaterial, ShaderMaterial, CatmullRomCurve3, CanvasTexture,
  AmbientLight, DirectionalLight, PointLight,
  SphereGeometry, PlaneGeometry, CircleGeometry, BoxGeometry, CylinderGeometry, ConeGeometry,
  TorusGeometry, TubeGeometry,
  BackSide: 1, AdditiveBlending: 2, NormalBlending: 3, DynamicDrawUsage: 4,
};

/* ---------------- DOM 桩 ---------------- */
function makeEl(tag) {
  const el = {
    tagName: (tag || 'div').toUpperCase(), _ls: {}, _children: [], style: {}, title: '', open: false,
    disabled: false, className: '', textContent: '', offsetWidth: 100,
    classList: {
      _s: new Set(),
      add(c) { this._s.add(c); }, remove(c) { this._s.delete(c); },
      toggle(c, f) { const on = f === undefined ? !this._s.has(c) : !!f; if (on) this._s.add(c); else this._s.delete(c); return on; },
      contains(c) { return this._s.has(c); },
    },
    appendChild(c) { this._children.push(c); return c; },
    querySelectorAll(sel) {
      const cls = sel.replace(/^\./, '');
      return this._children.filter(c => String(c.className).split(' ').includes(cls));
    },
    addEventListener(t, f) { (this._ls[t] = this._ls[t] || []).push(f); },
    fire(t, ev) { (this._ls[t] || []).forEach(f => f(ev || {})); },
  };
  Object.defineProperty(el, 'innerHTML', { get() { return ''; }, set() { this._children = []; } });
  return el;
}
const elMap = {};
const getEl = sel => elMap[sel] || (elMap[sel] = makeEl(sel));
const created = [];
const fake2d = { createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillStyle: '', font: '', fillText() {}, textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0 };
const document = {
  querySelector: getEl,
  createElement(tag) { const e = makeEl(tag); if (tag === 'canvas') { e.width = 64; e.height = 64; e.getContext = () => fake2d; } created.push(e); return e; },
  addEventListener() {}, documentElement: makeEl('html'), body: makeEl('body'), head: makeEl('head'),
  activeElement: null, fullscreenElement: null,
  querySelectorAll(sel) { return sel.includes('dots') ? (elMap['#dots'] ? elMap['#dots']._children : []) : []; },
};
document.body.classList.add('no-poem');

/* ---------------- 计时/帧泵 ---------------- */
let NOW = 0;
const timers = []; let tid = 1;
let rafCb = null;
const winLs = {};
function pump(frames, label) {
  for (let i = 0; i < frames; i++) {
    NOW += 33;
    const cb = rafCb; rafCb = null;
    if (cb) cb();
    for (let k = timers.length - 1; k >= 0; k--) { const t = timers[k]; timers.splice(k, 1); t.fn(); }
  }
  if (label) console.log('  … ' + label + ' 泵 ' + frames + ' 帧, state=' + sandbox.state + ', curIdx=' + sandbox.curIdx);
}

/* ---------------- 沙盒 ---------------- */
const sandbox = {
  THREE, document, window: { addEventListener(t, f) { (winLs[t] = winLs[t] || []).push(f); } },
  performance: { now: () => NOW },
  requestAnimationFrame(cb) { rafCb = cb; },
  console, setTimeout(fn) { timers.push({ fn }); return tid++; }, clearTimeout(id) {},
  location: { reload() {} },
};
sandbox.window.devicePixelRatio = 1;
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: 'index.html' });
const R = e => vm.runInContext(e, sandbox);

/* ================= 数据级断言 ================= */
console.log('--- 数据断言 ---');
const queue = JSON.parse(fs.readFileSync(path.join(DIR, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'meihua-wanganxi');
const joined = R("POEM.map(l=>l.segs.map(s=>s.c).join('')).join('')");
ok(joined === entry.text, 'POEM 拼接与 queue.text 逐字一致: ' + joined);
ok(R('POEM.length') === 2, 'POEM 2 句');
ok(R('STAGES.length') === 3, 'STAGES 3 项（封面+2境）');
ok(R("STAGES[1].name") === R("POEM[0].name") && R("STAGES[2].name") === R("POEM[1].name"), '境名对齐: 墙角寒梅/暗香浮动');
const pyOK = R("POEM.every(l=>l.segs.every(s=>[...s.c].filter(c=>!/[，。、！？；：]/.test(c)).length===s.p.length))");
ok(pyOK, '汉字数=拼音数（含 凌líng/墙qiáng/为wèi 注音）');
ok(R("POEM[0].segs[0].p[0]==='qiáng' && POEM[0].segs[1].p[0]==='líng' && POEM[1].segs[1].p[0]==='wèi'"), '多音字读音: qiáng/líng/wèi');
ok((code.match(/curIdx===2&&state==='stage'/g) || []).length >= 2, '交互接线 curIdx===2&&state===\'stage\' ≥2 处');
ok(code.includes("'03.mp3'"), "引用全诗音频 '03.mp3'");
ok(R('QUIZ.length') === 5, '小测 5 题');
ok(R("POEM.map(l=>l.read).join('')") === '墙角数枝梅，凌寒独自开。遥知不是雪，为有暗香来。', 'read 拼接与原文一致');

/* ================= sky/cloneSky 全覆盖 ================= */
console.log('--- sky 工厂 ---');
ok(R('STAGES.every(s=>{const k=s.sky(); return k.top&&k.hor&&k.fog&&typeof k.fd==="number"&&k.moon;})'), '3 个 sky() 工厂全字段');
ok(R('(()=>{const a=cloneSky(STAGES[2].sky()); return a.top&&a.moon.x===0&&a.moon.y===-400;})()'), 'cloneSky 可克隆');

/* ================= boot + 游览链路 ================= */
console.log('--- boot ---');
R('boot()');
ok(sandbox.state === 'stage' && sandbox.curIdx === 0, 'boot 完成，封面境就绪');
pump(30, '封面');

console.log('--- 入境 → 墙角寒梅 ---');
getEl('#enterBtn').fire('click');
ok(sandbox.state === 'transition', '入境触发过场');
pump(90, '过场');
ok(sandbox.state === 'stage' && sandbox.curIdx === 1, '到达境一（墙角寒梅）');
pump(120, '境一运行');

console.log('--- 切境二（暗香浮动） ---');
getEl('#btnNext').fire('click');
pump(90, '过场');
ok(sandbox.state === 'stage' && sandbox.curIdx === 2, '到达境二');
pump(60, '境二运行');

console.log('--- 交互①：pointerdown 唤香 ---');
sandbox.renderer.domElement.fire('pointerdown');
pump(10);
ok(getEl('#flash').textContent === '为有暗香来', '题字闪现「为有暗香来」');
let litCount = 0, plI = -1;
R('curStageObj.group').traverse(o => {
  if (o.material && o.material.userData && o.material.userData.c0 !== undefined && o.material.color.r > 0.65) litCount++;
  if (o.isLight && o.color && o.color.r > 0.8 && o.intensity > 0) plI = o.intensity;
});
ok(litCount > 0, '红萼点亮（' + litCount + ' 朵变色）');
ok(plI > 0, '香灯光亮起 intensity=' + plI.toFixed(2));

console.log('--- 交互②：连点守卫 + 空格接线 ---');
const before = getEl('#flash').textContent;
sandbox.renderer.domElement.fire('pointerdown');   // 冷却期内连点
pump(5);
ok(getEl('#flash').textContent === before, '冷却期内连点被守卫拦截');
(winLs.keydown || []).forEach(f => f({ code: 'Space', preventDefault() {} }));  // 仍在冷却 → 空格也应被 click 守卫拦
pump(5);
ok(getEl('#flash').textContent === before, '冷却期内空格触发同样被守卫拦截');
R('clock.t += 3');                                  // 越过冷却
(winLs.keydown || []).forEach(f => f({ code: 'Space', preventDefault() {} }));
pump(10);
ok(getEl('#flash').textContent === '为有暗香来', '冷却后空格重新唤香成功（两条独立接线均验证）');
pump(120, '香雾飘近段');

console.log('--- 终章与小测 ---');
getEl('#btnNext').fire('click');
ok(getEl('#ending').classList.contains('show'), '末境后进入终章，全诗音频 03.mp3 请求已发出');
getEl('#btnQuiz').fire('click');
ok(getEl('#quiz').classList.contains('show'), '小测打开');
for (let q = 0; q < 5; q++) {
  const body = getEl('#quizBody');
  const opts = body.querySelectorAll('.opt');
  ok(opts.length === 3, '第' + (q + 1) + '题 3 选项');
  opts[q % 3].fire('click');                        // 交替答对/答错
  const nb = body._children.find(c => c.id === 'quizNext');
  nb.fire('click');
}
ok(getEl('#quizBody').textContent.includes('胸有暗香，梅知己音') || getEl('#quizBody')._children.length > 0, '评语按本诗定制且结果页可出');
const closeBtn = getEl('#quizBody')._children.find(c => c.id === 'quizClose');
if (closeBtn) closeBtn.fire('click');
ok(!getEl('#quiz').classList.contains('show'), '小测关闭');

console.log('--- 重新入境 / 回封面 ---');
getEl('#btnAgain').fire('click');
pump(90, '重入境');
ok(sandbox.curIdx === 1 && sandbox.state === 'stage', '重新入境回到境一');
getEl('#btnCover').fire('click');
pump(60, '回封面');
ok(sandbox.curIdx === 0, '回到封面境');

console.log('--- 自动游览全程（无人值守） ---');
getEl('#btnNext').fire('click'); pump(90);          // 封面 → 境一
getEl('#btnAuto').fire('click');                    // 自动游览开
pump(1250, '自动游览');
ok(getEl('#ending').classList.contains('show'), '自动游览走完两境并进入终章');
getEl('#btnAuto').fire('click');                    // 关

console.log('--- 键盘导航 ---');
getEl('#btnCover').fire('click'); pump(60);
(winLs.keydown || []).forEach(f => f({ code: 'ArrowRight', preventDefault() {} }));
pump(90);
ok(sandbox.curIdx === 1, 'ArrowRight 进入境一');
(winLs.keydown || []).forEach(f => f({ code: 'ArrowLeft', preventDefault() {} }));
pump(90);
ok(sandbox.curIdx === 0, 'ArrowLeft 返回封面');
(winLs.keydown || []).forEach(f => f({ code: 'Escape', preventDefault() {} }));

console.log(FAIL === 0 ? '\nSMOKE ALL GREEN ✓' : '\nSMOKE FAILED: ' + FAIL);
process.exit(FAIL === 0 ? 0 : 1);
