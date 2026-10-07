/* smoke.test.js —— 秋夜将晓出篱门迎凉有感 深度冒烟测试
 * 以真实结构的 THREE 桩执行主脚本：boot() → 逐境 goto → 全部 build/update →
 * 交互境 click（含防连点守卫）→ 终章 → 回封面。任何异常即失败。 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const FILE = path.join(__dirname, 'index.html');
const html = fs.readFileSync(FILE, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
let failures = 0;
const ok = (cond, msg) => { if (!cond) { failures++; console.error('  ✗ ' + msg); } else console.log('  ✓ ' + msg); };

/* ---------- THREE 桩 ---------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  lerpVectors(a, b, k) { this.x = a.x + (b.x - a.x) * k; this.y = a.y + (b.y - a.y) * k; this.z = a.z + (b.z - a.z) * k; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) { this.x = a.y * b.z - a.z * b.x; this.y = a.z * b.x - a.x * b.z; this.z = a.x * b.y - a.y * b.x; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; this.x /= l; this.y /= l; this.z /= l; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class Color {
  constructor(h) { this.h = h; this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(0); }
  lerpColors(a, b, k) { this.r = a.r + (b.r - a.r) * k; this.g = a.g + (b.g - a.g) * k; this.b = a.b + (b.b - a.b) * k; return this; }
  lerp(c, k) { return this.lerpColors(this, c, k); }
}
class Object3D {
  constructor() {
    this.children = []; this.userData = {}; this.position = new V3();
    this.rotation = { x: 0, y: 0, z: 0 }; this.scale = { x: 1, y: 1, z: 1, set(x, y, z) { this.x = x; this.y = y; this.z = z; }, setScalar(s) { this.x = s; this.y = s; this.z = s; } };
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true;
  }
  add(...os) { os.forEach(o => { this.children.push(o); o.parent = this; }); return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); }
  traverse(fn) { fn(this); this.children.forEach(c => c.traverse && c.traverse(fn)); }
  lookAt() {}
}
class Group extends Object3D {}
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Line extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; } }
class Scene extends Object3D {}
class BufferGeometry {
  constructor() { this.attributes = {}; this._pos = null; }
  setAttribute(n, a) { this.attributes[n] = a; if (n === 'position') this._pos = a; }
  dispose() {}
}
class BufferAttribute { constructor(arr, size) { this.array = arr; this.itemSize = size; this.needsUpdate = false; } }
const geo = n => class { constructor(...a) { this.type = n; this.args = a; }
  dispose() {} rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  translate() { return this; } center() { return this; } };
const mat = () => class {
  constructor(o = {}) {
    Object.assign(this, { opacity: o.opacity === undefined ? 1 : o.opacity, transparent: !!o.transparent, userData: {}, depthWrite: o.depthWrite !== false }, o);
    ['color', 'specular', 'emissive', 'fog'].forEach(k => { if (typeof this[k] === 'number') this[k] = new Color(this[k]); });
    if (!this.color) this.color = new Color(0xffffff);
    this.map = this.map || null; this.isShaderMaterial = false; this.dispose = () => {};
  }
};
class ShaderMaterial {
  constructor(o = {}) { Object.assign(this, o); this.uniforms = o.uniforms || {}; this.isShaderMaterial = true; this.transparent = true; this.userData = {}; }
  dispose() {}
}
const THREE = {
  Vector3: V3, Vector2: V2, Color,
  Scene, Group, Mesh, Points, Line, Sprite, Object3D,
  BufferGeometry, BufferAttribute, ShaderMaterial, CanvasTexture: class { constructor() { this.dispose = () => {}; } },
  SphereGeometry: geo('Sphere'), CylinderGeometry: geo('Cyl'), BoxGeometry: geo('Box'), ConeGeometry: geo('Cone'),
  PlaneGeometry: geo('Plane'), RingGeometry: geo('Ring'), LatheGeometry: geo('Lathe'), CircleGeometry: geo('Circle'), TorusGeometry: geo('Torus'),
  MeshBasicMaterial: mat(), MeshPhongMaterial: mat(), PointsMaterial: mat(), SpriteMaterial: mat(), LineBasicMaterial: mat(),
  BackSide: 1, DoubleSide: 2, AdditiveBlending: 3, NormalBlending: 4,
  WebGLRenderer: class { constructor() { this.domElement = makeEl('canvas'); } setPixelRatio() {} setSize() {} render() {} setClearColor() {} },
  PerspectiveCamera: class { constructor(...a) { this.position = new V3(); this.aspect = 1; } lookAt() {} rotateZ() {} updateProjectionMatrix() {} },
  FogExp2: class { constructor(h, d) { this.color = new Color(h); this.density = d; } },
  DirectionalLight: class { constructor(c, i) { this.isLight = true; this.color = new Color(c); this.intensity = i; this.position = new V3(); this.userData = {}; } },
  AmbientLight: class { constructor(c, i) { this.isLight = true; this.color = new Color(c); this.intensity = i; this.position = new V3(); this.userData = {}; } },
  PointLight: class { constructor(c, i, d) { this.isLight = true; this.color = new Color(c); this.intensity = i; this.distance = d; this.position = new V3(); this.userData = {}; } },
};

/* ---------- DOM / 环境桩 ---------- */
const EL = {};
function makeEl(sel) {
  return EL[sel] || (EL[sel] = {
    sel, _ls: {}, style: {}, textContent: '', innerHTML: '', title: '', open: true, offsetWidth: 100, disabled: false,
    classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
    addEventListener(t, f) { this._ls[t] = f; },
    appendChild() {}, querySelectorAll() { return []; },
  });
}
let now = 0;
function makeCanvas() {
  return {
    width: 0, height: 0,
    getContext() {
      return {
        font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
        createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {},
      };
    },
  };
}
const sandbox = {
  THREE, console, Math, JSON,
  performance: { now: () => (now += 16.7) },
  requestAnimationFrame() {},
  setTimeout() { return 0; }, clearTimeout() {},
  window: { innerWidth: 1600, innerHeight: 900, devicePixelRatio: 1, addEventListener(t, f) { this['_on' + t] = f; } },
  document: {
    querySelector: s => makeEl(s), createElement: t => t === 'canvas' ? makeCanvas() : makeEl('el' + Math.random()),
    getElementById: s => makeEl('#' + s), querySelectorAll: () => [],
    addEventListener() {}, documentElement: makeEl('#html'), body: makeEl('#body'),
    activeElement: null, fullscreenElement: null, head: makeEl('#head'),
  },
  location: { reload() {} },
};
sandbox.window.AudioContext = function () {
  const node = () => ({ connect(x) { return x; }, gain: { value: 1, setValueAtTime() {}, exponentialRampToValueAtTime() {}, cancelScheduledValues() {}, linearRampToValueAtTime() {} } });
  return {
    destination: node(), sampleRate: 44100, currentTime: 0, state: 'running', resume() {},
    createGain: node, createOscillator: () => ({ connect(x) { return x; }, frequency: { value: 0 }, type: '', start() {}, stop() {} }),
    createBuffer: () => ({ getChannelData: () => new Float32Array(88200) }),
    createBufferSource: () => ({ connect(x) { return x; }, buffer: null, loop: false, start() {}, stop() {} }),
    createBiquadFilter: () => ({ connect(x) { return x; }, type: '', frequency: { value: 0 } }),
  };
};
sandbox.window.addEventListener = function (t, f) { this['_on' + t] = f; };
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: FILE });
console.log('== 主脚本顶层执行通过（THREE 桩） ==');

const get = e => vm.runInContext(e, sandbox);

/* ---------- 数据断言 ---------- */
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'qiuye-jiangxiao');
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
ok(joined === entry.text, 'segs 拼接与 queue.text 逐字一致（标点以 text 为准）');
ok(POEM.length === 3 && STAGES.length === 4, 'POEM=3 境、STAGES=4（含封面）');
ok(STAGES[0].key === 'cover', 'STAGES[0] 为封面');
STAGES.forEach((s, i) => { if (i > 0) ok(s.name === POEM[i - 1].name, `STAGES[${i}].name===POEM[${i - 1}].name (${s.name})`); });
ok(CN.length >= 3, 'CN 数组长度足够');
POEM.forEach((p, i) => {
  const han = [...p.segs.map(s => s.c).join('')].filter(c => !/[，。、！？；：]/.test(c)).length;
  const pyn = p.segs.reduce((a, s) => a + s.p.length, 0);
  ok(han === pyn, `第${i + 1}句 汉字${han}=拼音${pyn}`);
});
// 多音字抽查
const allPy = POEM.flatMap(l => l.segs.flatMap(s => s.p));
ok(allPy.includes('rèn'), '仞 注 rèn');
ok(allPy.includes('mó'), '摩 注 mó（摩天）');
ok(allPy.includes('lèi'), '泪 注 lèi');
ok(allPy.includes('yì'), '一年 注 yì（变调，与已收页面一致）');
ok(QUIZ.length === 5 && QUIZ.every(q => q.o.length === 3 && q.a >= 0 && q.a < 3), '小测 5 题、各 3 选项、答案越界检查');
const wm = code.match(/const words=\[([^\]]*)\]/);
ok(wm && wm[1].split(',').length === QUIZ.length + 1, '评语 words 长度=题数+1（6 项）');
ok(!/将进酒|万古愁|太白/.test(code), '无参考实现残留字样');
ok((code.match(/curIdx===3&&state==='stage'/g) || []).length >= 2, '交互境 curIdx===3 接线 ≥2 处（pointerdown+空格）');
ok(code.includes("'04.mp3'"), '全诗音频 04.mp3 已引用');
STAGES.forEach((s, i) => {
  ok(typeof s.build === 'function' && typeof s.sky === 'function' && s.cam && s.cam.f && s.cam.t && s.cam.lf && s.cam.lt && typeof s.dwell === 'number' && typeof s.river === 'number', `STAGES[${i}] 结构齐全`);
  const k = s.sky();
  ok(k && k.top && k.hor && k.fog && typeof k.fd === 'number' && k.moon, `STAGES[${i}].sky() 返回齐全`);
});

/* ---------- boot + 全程驾驶 ---------- */
console.log('== boot() 与全程驾驶 ==');
sandbox.boot();
const fire = (sel, ev) => { const el = EL[sel]; if (!el) return; const e = ev || { currentTarget: el, target: el, preventDefault() {}, code: '' }; Object.values(el._ls).forEach(f => f(e)); };
const key = c => sandbox.window._onkeydown({ code: c, preventDefault() {} });
const frames = n => { for (let i = 0; i < n; i++) sandbox.animate(); };
frames(30);
fire('#enterBtn');
frames(220);
ok(EL['#stageNo'].textContent === '第壹境', '入境后到达第壹境（河岳摩天）');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第贰境', '下一境到达第贰境（泪尽胡尘）');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第叁境', '下一境到达第叁境（南望王师）');
frames(40);
const canvas = EL['canvas'];
canvas._ls.pointerdown();
ok(EL['#flash'].textContent === '南望王师又一年', '点击画面 → 启明星升起 + 题字“南望王师又一年”');
frames(10);
canvas._ls.pointerdown();
key('Space');
frames(10);
ok(true, '连点守卫 + 空格触发均无异常');
frames(300);
ok(true, '启明星升起/篱门推开/旧年星沉动画全程无异常');
key('ArrowRight'); frames(5);
ok(true, '末境 → 终章 showEnding 无异常');
key('Escape'); frames(5);
fire('#btnSpeak');
fire('#btnAuto');
fire('#btnPoemAudio');
frames(5);
ok(true, '朗读/自动游览/聆听全诗控件无异常');
key('Escape');
fire('#btnCover'); frames(220);
ok(true, '回到封面 goto(0) 无异常');
key('ArrowRight'); frames(220);
ok(EL['#stageNo'].textContent === '第壹境', '封面 → 右键重新入境');

/* ---------- 各境 builder 直接深跑（build/update/click × 多帧） ---------- */
console.log('== 逐境 build/update/click 深跑 ==');
STAGES.forEach((s, i) => {
  const st = s.build();
  ok(st && st.group && typeof st.update === 'function', `STAGES[${i}] build() 返回 group+update`);
  for (let k = 0; k < 240; k++) st.update(k * 0.016, 0.016);
  let clickN = 0;
  if (st.click) { st.click(); clickN++; sandbox.animate(); sandbox.animate(); st.click(); clickN++; }
  ok(true, `STAGES[${i}] 240 帧 update + ${clickN} 次 click 无异常`);
});

console.log(failures ? `\n冒烟测试失败 ${failures} 项` : '\n冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
