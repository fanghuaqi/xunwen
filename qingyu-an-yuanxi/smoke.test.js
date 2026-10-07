/* smoke.test.js —— 青玉案·元夕（辛弃疾）深度冒烟测试
 * 真结构 THREE 桩跑完整链路：boot() → 封面 → 逐境 goto → 五个 builder 深跑（含 InstancedMesh
 * 灯笼海、灯轮、鱼龙、星雨）→ 第四境标志性瞬间「点击 → 满城灯海次第暗下」（熄灭波前/波前守卫/
 * 空格触发）→ 终章 → 回封面。另含：数据对齐 queue.json、逐字注音与多音字、色板、自动游览默认开、
 * 返回诗集目录两处、每境 draw call/三角面预算、NaN 扫描、fadeK 归零断言。
 * 任何异常即失败。 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const FILE = path.join(__dirname, 'index.html');
const html = fs.readFileSync(FILE, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
let failures = 0;
const ok = (cond, msg) => { if (!cond) { failures++; console.error('  ✗ ' + msg); } else console.log('  ✓ ' + msg); };

/* ---------------- THREE 桩（带真数组的几何，mergeGeos/InstancedMesh 可跑） ---------------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  lerpVectors(a, b, k) { this.x = a.x + (b.x - a.x) * k; this.y = a.y + (b.y - a.y) * k; this.z = a.z + (b.z - a.z) * k; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) { this.x = a.y * b.z - a.z * b.y; this.y = a.z * b.x - a.x * b.z; this.z = a.x * b.y - a.y * b.x; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; this.x /= l; this.y /= l; this.z /= l; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  length() { return Math.hypot(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class Color {
  constructor(h = 0xffffff) { this.h = h; this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(0); }
  lerpColors(a, b, k) { this.r = a.r + (b.r - a.r) * k; this.g = a.g + (b.g - a.g) * k; this.b = a.b + (b.b - a.b) * k; return this; }
  lerp(c, k) { return this.lerpColors(this, c, k); }
  setRGB(r, g, b) { this.r = r; this.g = g; this.b = b; return this; }
  setScalar(s) { this.r = this.g = this.b = s; return this; }
  toArray(a, o) { a[o] = this.r; a[o + 1] = this.g; a[o + 2] = this.b; return a; }
}
class BufferAttribute {
  constructor(array, itemSize) { this.array = array; this.itemSize = itemSize; this.count = array.length / itemSize; this.needsUpdate = false; }
  getX(i) { return this.array[i * this.itemSize]; }
  getY(i) { return this.array[i * this.itemSize + 1]; }
  setX(i, v) { this.array[i * this.itemSize] = v; }
  setY(i, v) { this.array[i * this.itemSize + 1] = v; }
  setZ(i, v) { if (this.itemSize > 2) this.array[i * this.itemSize + 2] = v; }
}
const NVERT = 6;
class BufferGeometry {
  constructor() {
    this.type = 'BufferGeometry'; this.index = null;
    this.attributes = {};
    this.attributes.position = new BufferAttribute(new Float32Array(NVERT * 3), 3);
    this.attributes.normal = new BufferAttribute(new Float32Array(NVERT * 3), 3);
    this.attributes.uv = new BufferAttribute(new Float32Array(NVERT * 2), 2);
  }
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  setIndex(i) { this.index = i; return this; }
  toNonIndexed() { return this; }
  computeVertexNormals() { return this; }
  setFromPoints() { return this; }
  translate() { return this; } rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  scale() { return this; } applyMatrix4() { return this; } center() { return this; } dispose() { }
}
const geo = n => class extends BufferGeometry { constructor(...a) { super(); this.type = n; this.args = a; } };
class Object3D {
  constructor() {
    this.children = []; this.userData = {}; this.position = new V3(); this.parent = null;
    this.rotation = { x: 0, y: 0, z: 0, set(x, y, z) { this.x = x; this.y = y; this.z = z; }, order: 'XYZ' };
    this.quaternion = { setFromAxisAngle() { return this; }, copy() { return this; } };
    this.matrix = { elements: new Float32Array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) }; this.matrixWorld = {};
    this.scale = { x: 1, y: 1, z: 1, set(x, y, z) { this.x = x; this.y = y; this.z = z; }, setScalar(s) { this.x = this.y = this.z = s; } };
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true;
  }
  add(...os) { os.forEach(o => { if (!o) return; this.children.push(o); o.parent = this; }); return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); }
  traverse(fn) { fn(this); this.children.forEach(c => c.traverse && c.traverse(fn)); }
  lookAt() { } updateMatrixWorld() { } rotateZ() { } rotateOnAxis() { }
  updateMatrix() {
    const e = this.matrix.elements;
    e[0] = this.scale.x; e[5] = this.scale.y; e[10] = this.scale.z;
    e[12] = this.position.x; e[13] = this.position.y; e[14] = this.position.z;
  }
}
class Group extends Object3D { }
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isPoints = true; } }
class Line extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isLine = true; } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; this.isSprite = true; } }
class InstancedMesh extends Object3D {
  constructor(g, m, n) {
    super(); this.geometry = g; this.material = m; this.count = n; this.isMesh = true;
    this.instanceMatrix = { count: n, needsUpdate: false, array: new Float32Array(n * 16) };
    this.instanceColor = null;
  }
  setMatrixAt(i, m) { this.instanceMatrix.array.set(m.elements, i * 16); }
  setColorAt(i, c) { if (!this.instanceColor) this.instanceColor = { array: new Float32Array(this.count * 3), needsUpdate: false }; c.toArray(this.instanceColor.array, i * 3); }
}
class Scene extends Object3D { }
const mat = () => class {
  constructor(o = {}) {
    Object.assign(this, { opacity: o.opacity === undefined ? 1 : o.opacity, transparent: !!o.transparent, depthWrite: o.depthWrite !== false }, o);
    this.userData = o.userData || {};
    ['color', 'specular', 'emissive', 'fog'].forEach(k => { if (typeof this[k] === 'number') this[k] = new Color(this[k]); });
    if (!this.color) this.color = new Color(0xffffff);
    this.map = this.map || null; this.isShaderMaterial = false; this.dispose = () => { };
  }
};
class ShaderMaterial {
  constructor(o = {}) { Object.assign(this, o); this.uniforms = o.uniforms || {}; this.isShaderMaterial = true; this.transparent = true; this.userData = {}; this.dispose = () => { }; }
}
class Quaternion { setFromUnitVectors() { return this; } copy() { return this; } }
class Matrix4 { makeRotationFromQuaternion() { return this; } setPosition() { return this; } }
class Curve {
  constructor(pts) { this.points = pts; }
  pAt(u) {
    const p = this.points, f = Math.max(0, Math.min(0.9999, u)) * (p.length - 1);
    const i = Math.floor(f), k = f - i, a = p[i], b = p[Math.min(p.length - 1, i + 1)];
    return new V3(a.x + (b.x - a.x) * k, a.y + (b.y - a.y) * k, a.z + (b.z - a.z) * k);
  }
  getPointAt(u) { return this.pAt(u); }
  getPoint(u) { return this.pAt(u); }
  getTangentAt(u) { const a = this.pAt(Math.max(0, u - 0.01)), b = this.pAt(Math.min(1, u + 0.01)); return b.subVectors(b, a).normalize(); }
  getLength() { return 1; }
}
const THREE = {
  Vector3: V3, Vector2: V2, Color, BufferAttribute, BufferGeometry, Quaternion, Matrix4,
  Scene, Group, Mesh, Points, Line, Sprite, Object3D, InstancedMesh,
  ShaderMaterial, CatmullRomCurve3: Curve,
  CanvasTexture: class { constructor() { this.dispose = () => { }; this.wrapS = 0; this.wrapT = 0; this.repeat = { set() { } }; this.needsUpdate = false; } clone() { return new this.constructor(); } },
  SphereGeometry: geo('Sphere'), CylinderGeometry: geo('Cyl'), BoxGeometry: geo('Box'), ConeGeometry: geo('Cone'),
  PlaneGeometry: geo('Plane'), RingGeometry: geo('Ring'), LatheGeometry: geo('Lathe'), CircleGeometry: geo('Circle'),
  TorusGeometry: geo('Torus'), TubeGeometry: geo('Tube'), IcosahedronGeometry: geo('Ico'),
  OctahedronGeometry: geo('Octa'), TetrahedronGeometry: geo('Tetra'), DodecahedronGeometry: geo('Dode'),
  MeshBasicMaterial: mat(), MeshPhongMaterial: mat(), PointsMaterial: mat(), SpriteMaterial: mat(), LineBasicMaterial: mat(),
  BackSide: 1, DoubleSide: 2, AdditiveBlending: 3, NormalBlending: 4, DynamicDrawUsage: {},
  WebGLRenderer: class { constructor() { this.domElement = makeEl('canvas'); this.info = { render: { calls: 0, triangles: 0 } }; } setPixelRatio() { } setSize() { } render() { } setClearColor() { } },
  PerspectiveCamera: class { constructor() { this.position = new V3(); this.aspect = 1; this.quaternion = { copy() { } }; } lookAt() { } rotateZ() { } updateProjectionMatrix() { } },
  FogExp2: class { constructor(h, d) { this.color = new Color(h); this.density = d; } },
  DirectionalLight: class { constructor(c, i) { this.isLight = true; this.color = new Color(c); this.intensity = i; this.position = new V3(); this.userData = {}; } },
  AmbientLight: class { constructor(c, i) { this.isLight = true; this.color = new Color(c); this.intensity = i; this.position = new V3(); this.userData = {}; } },
  PointLight: class { constructor(c, i, d) { this.isLight = true; this.color = new Color(c); this.intensity = i; this.distance = d; this.position = new V3(); this.userData = {}; } },
};

/* ---------------- DOM / 环境桩 ---------------- */
const EL = {};
function makeEl(sel) {
  return EL[sel] || (EL[sel] = {
    sel, _ls: {}, style: {}, textContent: '', innerHTML: '', title: '', open: true, offsetWidth: 100, disabled: false,
    classList: {
      _s: {}, add(c) { this._s[c] = true; }, remove(c) { delete this._s[c]; },
      toggle(c, v) { if (v === undefined) v = !this._s[c]; v ? this._s[c] = true : delete this._s[c]; return v; },
      contains(c) { return !!this._s[c]; }
    },
    addEventListener(t, f) { this._ls[t] = f; }, appendChild() { }, querySelectorAll() { return []; },
  });
}
let now = 0;
function makeCanvas() {
  return {
    width: 0, height: 0,
    getContext() {
      return {
        font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
        createRadialGradient: () => ({ addColorStop() { } }), createLinearGradient: () => ({ addColorStop() { } }),
        fillRect() { }, clearRect() { }, fillText() { }, beginPath() { }, arc() { }, fill() { },
      };
    },
  };
}
const sandbox = {
  THREE, console, Math, JSON, Float32Array, isFinite,
  performance: { now: () => (now += 16.7) },
  requestAnimationFrame() { }, setTimeout() { return 0; }, clearTimeout() { },
  window: { innerWidth: 1600, innerHeight: 900, devicePixelRatio: 1, addEventListener(t, f) { this['_on' + t] = f; } },
  document: {
    querySelector: s => makeEl(s), createElement: t => t === 'canvas' ? makeCanvas() : makeEl('el' + Math.random()),
    getElementById: s => makeEl('#' + s), querySelectorAll: () => [],
    addEventListener() { }, documentElement: makeEl('#html'), body: makeEl('#body'),
    activeElement: null, fullscreenElement: null, head: makeEl('#head'),
  },
  location: { reload() { } },
};
sandbox.window.AudioContext = function () {
  const node = () => ({ connect(x) { return x; }, gain: { value: 1, setValueAtTime() { }, exponentialRampToValueAtTime() { }, cancelScheduledValues() { }, linearRampToValueAtTime() { } } });
  return {
    destination: node(), sampleRate: 44100, currentTime: 0, state: 'running', resume() { },
    createGain: node,
    createOscillator: () => ({ connect(x) { return x; }, frequency: { value: 0 }, type: '', start() { }, stop() { } }),
    createBuffer: () => ({ getChannelData: () => new Float32Array(88200) }),
    createBufferSource: () => ({ connect(x) { return x; }, buffer: null, loop: false, start() { }, stop() { } }),
    createBiquadFilter: () => ({ connect(x) { return x; }, type: '', frequency: { value: 0 } }),
  };
};
sandbox.window.addEventListener = function (t, f) { this['_on' + t] = f; };
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: FILE });
console.log('== 主脚本顶层执行通过（THREE 桩） ==');
const get = e => vm.runInContext(e, sandbox);

/* ---------------- 数据断言 ---------------- */
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'qingyu-an-yuanxi');
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
ok(joined === entry.text, 'segs 拼接与 queue.text 逐字一致');
ok(joined === '东风夜放花千树。更吹落、星如雨。宝马雕车香满路。凤箫声动，玉壶光转，一夜鱼龙舞。蛾儿雪柳黄金缕。笑语盈盈暗香去。众里寻他千百度。蓦然回首，那人却在，灯火阑珊处。', '标点严格照抄原文');
ok(POEM.length === 4 && STAGES.length === 5, 'POEM=4 境、STAGES=5（含封面）');
ok(STAGES[0].key === 'cover' && STAGES[0].name === '卷首', 'STAGES[0] 为封面');
STAGES.forEach((s, i) => { if (i > 0) ok(s.name === POEM[i - 1].name, `STAGES[${i}].name===POEM[${i - 1}].name（${s.name}）`); });
ok(/东风夜放花千树/.test(POEM[0].name + POEM[0].read) && POEM[0].name === '花树星雨', '第壹境境名「花树星雨」');
ok(POEM[3].name === '蓦然回首', '第肆境境名「蓦然回首」（标志性瞬间）');
ok(CN.length >= 4, 'CN 数字数组长度足够');
POEM.forEach((p, i) => {
  const han = [...p.segs.map(s => s.c).join('')].filter(c => !/[，。、！？；：]/.test(c)).length;
  const pyn = p.segs.reduce((a, s) => a + s.p.length, 0);
  ok(han === pyn, `第${i + 1}境 汉字${han}=拼音${pyn}`);
});
const allPy = POEM.flatMap(l => l.segs.flatMap(s => s.p));
ok(allPy.length === 67, '拼音总数 67（= 全词 67 字）');
/* 多音字逐项核对：玉壶 hú / 蛾 é / 蓦然 mò / 阑珊 lán shān / 千百度 dù / 盈盈 yíng / 凤箫 xiāo / 转 zhuǎn */
['hú', 'é', 'mò', 'rán', 'lán', 'shān', 'dù', 'yíng', 'xiāo', 'zhuǎn', 'gèng'].forEach(p => ok(allPy.includes(p), '注音含 ' + p));
ok(!allPy.includes('mù') && !allPy.includes('zhuàn'), '「蓦」未误注 mù、「光转」未误注 zhuàn');
ok(POEM[3].zhu.some(z => /阑珊/.test(z[0]) && /不是/.test(z[1]) && /辉煌/.test(z[1])), '第肆境注释写明「灯火阑珊＝零落稀疏，不是灯火辉煌」');
ok(POEM[3].zhu.some(z => /词眼/.test(z[0])), '第肆境注释含「词眼」考点');
ok(QUIZ.length === 5 && QUIZ.every(q => q.o.length === 3 && q.a >= 0 && q.a < 3), '小测 5 题、各 3 选项、答案不越界');
ok(/东风夜放花千树/.test(QUIZ[0].q) && /更吹落/.test(QUIZ[0].o[0]), '接龙题①：花千树 → 星如雨');
ok(/众里寻他千百度/.test(QUIZ[1].q) && /蓦然回首/.test(QUIZ[1].o[1]), '接龙题②：千百度 → 蓦然回首');
ok(/阑珊/.test(QUIZ[2].q) && /零落稀疏/.test(QUIZ[2].o[1]), '词义题考「灯火阑珊」的准确含义');
ok(/稼轩/.test(QUIZ[3].q) && /婉约/.test(QUIZ[3].o[0]), '作者题考稼轩＋豪放词人的婉约一路');
ok(/人间词话/.test(QUIZ[4].q) && /第三重/.test(QUIZ[4].o[2]), '名句理解题考王国维「第三重境界」');
const wm = code.match(/const words=\[([^\]]*)\]/);
ok(wm && wm[1].split(',').length === QUIZ.length + 1, '评语 words 长度=题数+1（6）');
ok(!/将进酒|万古愁|如见太白|深得太白/.test(code), '无参考实现残留字样');
ok((code.match(/curIdx===4&&state==='stage'/g) || []).length >= 2, '交互境 curIdx===4 接线 ≥2 处（pointerdown+空格）');
ok(code.includes('clamp(i,0,4)'), 'goto 上界 clamp(i,0,4)');
ok(code.includes("'05.mp3'"), '全词音频 05.mp3 已引用');
ok(!/'14\.mp3'/.test(code) && !/curIdx===13|curIdx>=13|i<=13/.test(code), '骨架遗留 13/14.mp3 已清干净');
ok(/if\(state!=='stage'\)return;/.test(code), 'showEnding 入口守卫存在');
ok(/--gold:\s*#e0a860/i.test(html), '--gold 精确等于分配强调色 #e0a860');
ok(/background:#070a10/.test(html) && !(code.match(/0x05070d/g) || []).length, 'body 为元宵夜色 #070a10，主脚本无夜宴默认底色');
ok(!/#d4af37/.test(html), '全页无《将进酒》鎏金');
ok(/let trans=null,stageT=0,autoT=0,autoMode=true;/.test(code), 'autoMode 变量默认 true（自动游览默认开）');
ok(/<button id="btnAuto" class="on">自动游览 · 开<\/button>/.test(html), '自动游览按钮初始 class="on" 且文案「自动游览 · 开」');
const galLinks = (html.match(/class="galLink"/g) || []).length;
ok(galLinks === 2, '封面与终章各有 1 个 galLink（共 ' + galLinks + '）');
ok(/<a class="galLink" href="\.\.\/index\.html">← 返回诗集目录<\/a>/.test(html), '封面 enterBtn 下返回诗集目录');
ok(/<a class="galLink" href="\.\.\/index\.html" style="align-self:center">诗集目录<\/a>/.test(html), '终章 btnCover 后诗集目录链接');
ok(/\.galLink\{display:inline-block;font-family:var\(--song\);font-size:12\.5px/.test(html) && /#endBtns \.galLink\{align-self:center\}/.test(html), '.galLink 样式已注入 </style> 前');
ok(/HALO_VERT|STARRAIN_VERT|DRAGON_VERT/.test(code), '本词自绘母题着色器在位（灯晕/星雨/鱼龙）');
ok(/function makeLanternField/.test(code) && /function makeLantern\(/.test(code), '灯笼：makeLantern 与批量灯海 makeLanternField 双原语在位');
['makeFigure', 'makeFlame', 'makeVessel', 'makeRange', 'makeMoon', 'makeForeground', 'makePillar', 'makeCrowd', 'makeMist', 'makeGround']
  .forEach(f => ok(new RegExp('function ' + f + '\\(').test(code), '新原语可用：' + f));
STAGES.forEach((s, i) => ok(typeof s.build === 'function' && typeof s.sky === 'function' && s.cam && s.cam.f && s.cam.t && s.cam.lf && s.cam.lt && typeof s.dwell === 'number' && typeof s.river === 'number', `STAGES[${i}] 结构齐全`));

/* ---------------- 预算 / NaN / fade 工具 ---------------- */
function stats(g) {
  let calls = 0, tris = 0;
  g.traverse(o => {
    if (o.isMesh || o.isPoints || o.isLine || o.isSprite) {
      calls++;
      const g2 = o.geometry, n = g2 && g2.attributes && g2.attributes.position ? g2.attributes.position.count / 3 : 0;
      tris += n * (o.isMesh && o.count ? o.count : 1);
    }
  });
  return { calls, tris: Math.round(tris) };
}
function scanNaN(g) {
  const bad = [];
  const chk = (v, p) => { if (typeof v === 'number' && !isFinite(v)) bad.push(p); };
  g.traverse(o => {
    chk(o.position && o.position.x, 'pos.x'); chk(o.position && o.position.y, 'pos.y'); chk(o.position && o.position.z, 'pos.z');
    chk(o.rotation && o.rotation.x, 'rot.x'); chk(o.rotation && o.rotation.y, 'rot.y'); chk(o.rotation && o.rotation.z, 'rot.z');
    chk(o.scale && o.scale.x, 'scale');
    const ge = o.geometry;
    if (ge && ge.attributes) for (const k in ge.attributes) {
      const a = ge.attributes[k].array;
      for (let i = 0; i < a.length; i++) if (!isFinite(a[i])) { bad.push('geo.' + k + '[' + i + ']'); break; }
    }
    const m = o.material; if (!m) return;
    chk(m.opacity, 'opacity'); chk(m.emissiveIntensity, 'emissiveIntensity'); chk(m.shininess, 'shininess');
    if (m.uniforms) for (const k in m.uniforms) {
      const v = m.uniforms[k].value;
      if (typeof v === 'number') chk(v, 'u.' + k);
      else if (v && typeof v === 'object') { chk(v.x, 'u.' + k + '.x'); chk(v.y, 'u.' + k + '.y'); chk(v.z, 'u.' + k + '.z'); chk(v.r, 'u.' + k + '.r'); }
    }
  });
  return bad;
}
function fadeZero(g, t) {
  const bad = [];
  sandbox.setFade(g, 0);
  if (g.userData.update) g.userData.update(t, 0.016);
  g.traverse(o => {
    if (o.isLight && o.intensity > 1e-9) bad.push('light.intensity=' + o.intensity);
    const m = o.material; if (!m) return;
    if (m.isSprite && m.opacity > 1e-9) bad.push('sprite.opacity=' + m.opacity);
    if (m.isShaderMaterial && m.uniforms && m.uniforms.uFade && m.uniforms.uFade.value > 1e-9) bad.push('uFade=' + m.uniforms.uFade.value);
  });
  return bad;
}

/* ---------------- boot + 全程驾驶 ---------------- */
console.log('== boot() 与全程驾驶 ==');
sandbox.boot();
const fire = (sel, ev) => { const el = EL[sel]; if (!el) return; const e = ev || { currentTarget: el, target: el, preventDefault() { }, code: '' }; Object.values(el._ls).forEach(f => f(e)); };
const key = c => sandbox.window._onkeydown({ code: c, preventDefault() { } });
const frames = n => { for (let i = 0; i < n; i++) sandbox.animate(); };
frames(30);
ok(get('curIdx') === 0 && get('state') === 'stage', '封面境就绪');
fire('#enterBtn');
frames(240);
ok(EL['#stageNo'].textContent === '第壹境', '入境后到达第壹境');
ok(get('autoMode') === true, '默认自动游览已开启');
fire('#btnNext'); frames(240);
ok(EL['#stageNo'].textContent === '第贰境', '下一境到达第贰境（灯轮鱼龙）');
fire('#btnNext'); frames(240);
ok(EL['#stageNo'].textContent === '第叁境', '下一境到达第叁境（蛾儿雪柳）');
fire('#btnNext'); frames(240);
ok(EL['#stageNo'].textContent === '第肆境', '下一境到达第肆境（蓦然回首）');

console.log('== 第四境标志性瞬间：点击 → 满城灯海次第暗下 ==');
frames(60);
const canvas = EL['canvas'];
const ctl = get('lingerCtl');
ok(!!ctl && ctl.dim < 0.05, '入第四境时灯海全亮（dim=' + (ctl ? ctl.dim.toFixed(3) : 'n/a') + '）');
const st4 = get('curStageObj');
const field4 = (() => { let f = null; st4.group.traverse(o => { if (o.isMesh && o.count > 60 && o.material && o.material.isShaderMaterial === false) f = f || o; }); return f; })();
canvas._ls.pointerdown();
frames(4);
ok(EL['#flash'].textContent === '灯火阑珊', '点击画面 → 题字「灯火阑珊」');
ok(ctl.tgt === 1, '进入熄灭态（tgt=1）');
canvas._ls.pointerdown();                        // 1.6s 守卫内连点应被吞
ok(ctl.tgt === 1 && EL['#flash'].textContent === '灯火阑珊', '守卫内连点被吞（不会闪回）');
frames(420);
ok(ctl.dim > 0.9 && ctl.front > 1.2, '灯海次第暗下完成（dim=' + ctl.dim.toFixed(2) + '，波前=' + ctl.front.toFixed(2) + '）');
const sc4 = field4 ? field4.instanceMatrix.array : null;
let shrunk = 0;
if (sc4) for (let i = 0; i < field4.count; i++) if (sc4[i * 16] < 0.2) shrunk++;
ok(field4 && shrunk >= field4.count * 0.7, `远灯实例已被逐盏缩到近零（${shrunk}/${field4 ? field4.count : 0} 盏）`);
const personPool = (() => { let p = null; st4.group.traverse(o => { if (o.isMesh && o.material && o.material.map && o.geometry && o.geometry.type === 'Circle') p = p || o; }); return p; })();
ok(!!personPool, '「那人」脚下留有一摊灯光（灯海灭后仍看得见人）');
frames(120);
key('Space');
ok(ctl.tgt === 0, '空格触发同一交互 → 灯海复明（点击接线第二处）');
frames(60);
ok(EL['#flash'].textContent === '蓦然回首', '复明题字「蓦然回首」');
frames(300);
ok(ctl.dim < 0.15, '灯海重新亮起（dim=' + ctl.dim.toFixed(2) + '）');

key('ArrowRight'); frames(6);
ok(get('state') === 'ending', '末境 → 终章 showEnding 无异常');
key('Escape'); frames(6);
ok(get('state') === 'stage', 'Escape 返回舞台态');
fire('#btnSpeak'); fire('#btnPoemAudio'); fire('#btnAuto');
frames(6);
ok(get('autoMode') === false, '自动游览可一键关');
fire('#btnAuto'); fire('#btnAutoSpeak'); fire('#btnAutoSpeak'); fire('#btnPy'); fire('#btnPy'); fire('#btnSnd'); fire('#btnSnd');
fire('#btnQuiz'); frames(6);
ok(EL['#quizCnt'].textContent.indexOf('第 1 题') === 0, '小测开启并渲染首题');
key('ArrowRight');
ok(get('curIdx') === 4, '小测打开时方向键被忽略（模态保护）');
EL['#quiz'].classList.remove('show');
fire('#btnCover'); frames(240);
ok(get('curIdx') === 0, '回到封面 goto(0) 无异常');
key('ArrowRight'); frames(240);
ok(EL['#stageNo'].textContent === '第壹境', '封面 → 右键重新入境');

/* ---------------- 逐境 builder 深跑 + 预算 + NaN + fade ---------------- */
console.log('== 逐境 build/update/click 深跑 + 预算 + NaN + fadeK ==');
STAGES.forEach((s, i) => {
  const st = s.build();
  ok(st && st.group && typeof st.update === 'function', `STAGES[${i}].build() 返回 group+update`);
  for (let k = 0; k < 400; k++) st.update(k * 0.016, 0.016);
  let clicks = 0;
  if (st.click) {
    for (let k = 0; k < 120; k++) st.update(6.4 + k * 0.016, 0.016);
    st.click(); clicks++;
    st.click(); clicks++;                       // 守卫内连点应被吞
    for (let k = 0; k < 300; k++) st.update(8.4 + k * 0.016, 0.016);
    st.click(); clicks++;
    for (let k = 0; k < 300; k++) st.update(13.4 + k * 0.016, 0.016);
  }
  const nan = scanNaN(st.group);
  ok(nan.length === 0, `STAGES[${i}] 400+ 帧 update + ${clicks} 次 click，NaN 扫描 ${nan.length} 处` + (nan.length ? '：' + nan.slice(0, 4) : ''));
  const bad = fadeZero(st.group, 9.9);
  ok(bad.length === 0, `STAGES[${i}] fadeK=0 时无残留发光/灯光（${bad.slice(0, 3).join(',')}）`);
  const sc = stats(st.group);
  ok(sc.calls <= 120, `STAGES[${i}] draw call ${sc.calls} ≤ 120`);
  ok(sc.tris <= 120000, `STAGES[${i}] 三角面 ${sc.tris} ≤ 12 万`);
  console.log(`     · STAGES[${i}] ${s.name || '卷首'}：calls=${sc.calls} tris=${sc.tris}`);
});

/* 雾密度预算（宴饮/市井 fd ≤ 0.008：主体 15-30 单位内） */
STAGES.forEach((s, i) => {
  const k = s.sky();
  ok(k.fd <= 0.008, `STAGES[${i}] fd=${k.fd} ≤ 0.008（市井赛道上限）`);
});

console.log(failures ? `\n冒烟测试失败 ${failures} 项` : '\n冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
