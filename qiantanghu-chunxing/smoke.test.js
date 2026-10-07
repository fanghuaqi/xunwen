/* qiantanghu-chunxing/smoke.test.js —— 深冒烟测试
 * 用 THREE 桩在 Node 里真实执行 index.html 主脚本，跑通：
 *   顶层解析 → boot() → 封面 → 四境（build/update/click/onEnter/淡出）→ 终章 → 小测 → 回封面
 * 并逐一单测 5 个 builder 与 disposeGroup。
 * 运行: node smoke.test.js      退出码 0 = 全部通过
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

let pass = 0; const fails = [];
const ok = (c, m) => { if (c) { pass++; } else { fails.push(m); } };

/* ============================ THREE 桩 ============================ */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  setScalar(s) { this.x = this.y = this.z = s; return this; }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) { return this.set(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x); }
  lerpVectors(a, b, t) { this.x = a.x + (b.x - a.x) * t; this.y = a.y + (b.y - a.y) * t; this.z = a.z + (b.z - a.z) * t; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; return this.multiplyScalar(1 / l); }
  distanceTo(v) { return Math.hypot(this.x - v.x, this.y - v.y, this.z - v.z); }
  applyQuaternion() { return this; }
  cross(v) { return this.crossVectors(this, v); }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } set(x, y) { this.x = x; this.y = y; return this; } }
class Col {
  constructor(h) { this.r = this.g = this.b = 1; this.set(h === undefined ? 0xffffff : h); }
  set(h) { if (typeof h === 'number') { this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; } return this; }
  setRGB(r, g, b) { this.r = r; this.g = g; this.b = b; return this; }
  setHSL() { return this; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Col().copy(this); }
  lerp(c, t) { this.r += (c.r - this.r) * t; this.g += (c.g - this.g) * t; this.b += (c.b - this.b) * t; return this; }
  lerpColors(a, b, t) { return this.copy(a).lerp(b, t); }
}
class Euler { constructor() { this.x = this.y = this.z = 0; } set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } }
class Quat { setFromAxisAngle() { return this; } }
class Obj {
  constructor() {
    this.children = []; this.parent = null; this.position = new V3(); this.rotation = new Euler();
    this.scale = new V3(1, 1, 1); this.quaternion = new Quat(); this.userData = {};
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true; this.isObject3D = true;
  }
  add(...os) { for (const o of os) if (o) { o.parent = this; this.children.push(o); } return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) { fn(this); for (const c of this.children) c.traverse(fn); }
  updateMatrix() { } rotateOnAxis() { return this; } rotateZ() { return this; } rotateX() { return this; } lookAt() { return this; }
}
class Group extends Obj { }
class Scene extends Obj { constructor() { super(); this.fog = null; } }
class Cam extends Obj { constructor() { super(); this.aspect = 1; } updateProjectionMatrix() { } }
class Mat {
  constructor(o = {}) {
    Object.assign(this, { opacity: 1, transparent: false, side: 0, blending: 0, depthWrite: true, userData: {} }, o);
    this.color = new Col(o.color === undefined ? 0xffffff : o.color);
    this.emissive = new Col(o.emissive === undefined ? 0 : o.emissive);
    this.isShaderMaterial = !!(o.uniforms || o.vertexShader);
    this.uniforms = o.uniforms;
  }
  dispose() { }
}
class Geo {
  constructor() { this.attributes = { position: { array: new Float32Array(9), needsUpdate: false } }; }
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  setFromPoints() { return this; }
  rotateX(th) {
    const a = this.attributes.position.array;
    for (let i = 0; i < a.length; i += 3) {
      const y = a[i + 1], z = a[i + 2];
      a[i + 1] = y * Math.cos(th) - z * Math.sin(th); a[i + 2] = y * Math.sin(th) + z * Math.cos(th);
    }
    return this;
  }
  computeVertexNormals() { }
  dispose() { }
}
class PlaneGeo extends Geo {
  constructor(w = 1, h = 1, sx = 1, sy = 1) {
    super();
    const n = (sx + 1) * (sy + 1), a = new Float32Array(n * 3);
    let k = 0;
    for (let i = 0; i <= sy; i++) for (let j = 0; j <= sx; j++) { a[k++] = -w / 2 + w * j / sx; a[k++] = h / 2 - h * i / sy; a[k++] = 0; }
    this.attributes.position = { array: a, needsUpdate: false };
  }
}
class SimpleGeo extends Geo { constructor() { super(); this.attributes.position = { array: new Float32Array(300), needsUpdate: false }; } }
class BufferGeo extends Geo { constructor() { super(); this.attributes = { position: { array: new Float32Array(0), needsUpdate: false } }; } }
class Mesh extends Obj { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } }
class Points extends Mesh { constructor(g, m) { super(g, m); this.isPoints = true; } }
class Sprite extends Mesh { constructor(m) { super(new SimpleGeo(), m); this.isSprite = true; } }
class Inst extends Mesh {
  constructor(g, m, n) {
    super(g, m); this.count = n;
    this.instanceMatrix = { array: new Float32Array(n * 16), needsUpdate: false, setUsage() { } };
    this.instanceColor = { array: new Float32Array(n * 3), needsUpdate: false, setUsage() { } };
    this.setCalls = 0;
  }
  setMatrixAt(i) { this.setCalls++; if (i < 0 || i >= this.count) throw new Error('setMatrixAt 越界 ' + i); }
  setColorAt(i) { if (i < 0 || i >= this.count) throw new Error('setColorAt 越界 ' + i); }
}
class Light extends Obj { constructor(c, i) { super(); this.color = new Col(c); this.intensity = i; this.isLight = true; } }
class Renderer {
  constructor() {
    const h = {};
    this.domElement = { style: {}, addEventListener: (t, fn) => { (h[t] = h[t] || []).push(fn); }, fire: t => { (h[t] || []).forEach(fn => fn({})); } };
    this._renders = 0;
  }
  setPixelRatio() { } setSize() { } setClearColor() { } render() { this._renders++; }
}
const THREE = {
  Vector3: V3, Vector2: V2, Color: Col, Euler, Quaternion: Quat, Object3D: Obj, Group, Scene,
  PerspectiveCamera: Cam, WebGLRenderer: Renderer,
  SphereGeometry: SimpleGeo, ConeGeometry: SimpleGeo, CylinderGeometry: SimpleGeo, BoxGeometry: SimpleGeo,
  LatheGeometry: SimpleGeo, TubeGeometry: SimpleGeo, TorusGeometry: SimpleGeo, CircleGeometry: SimpleGeo,
  PlaneGeometry: PlaneGeo, BufferGeometry: BufferGeo,
  BufferAttribute: class { constructor(a, s) { this.array = a; this.itemSize = s; this.needsUpdate = false; } },
  Mesh, Points, Sprite, Line: Mesh, InstancedMesh: Inst,
  MeshPhongMaterial: Mat, MeshBasicMaterial: Mat, PointsMaterial: Mat, SpriteMaterial: Mat,
  LineBasicMaterial: Mat, ShaderMaterial: Mat, CanvasTexture: class { constructor(c) { this.image = c; } dispose() { } },
  DirectionalLight: Light, AmbientLight: Light, PointLight: Light,
  FogExp2: class { constructor(c, d) { this.color = new Col(c); this.density = d; } },
  CatmullRomCurve3: class { constructor(p) { this.points = p; } },
  DynamicDrawUsage: 35048, BackSide: 1, DoubleSide: 2, AdditiveBlending: 2, NormalBlending: 1,
};

/* ============================ DOM / 浏览器桩 ============================ */
const ctx2d = {
  createRadialGradient: () => ({ addColorStop() { } }), fillRect() { }, fillText() { },
  fillStyle: '', font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0,
};
function elStub(tag) {
  const e = {
    tagName: (tag || 'div').toUpperCase(), children: [], style: {}, _cls: new Set(), _h: {},
    textContent: '', innerHTML: '', width: 0, height: 0, offsetWidth: 1, open: false, title: '', disabled: false,
    classList: {
      add: c => e._cls.add(c), remove: c => e._cls.delete(c),
      toggle: (c, f) => { const on = f === undefined ? !e._cls.has(c) : !!f; on ? e._cls.add(c) : e._cls.delete(c); return on; },
      contains: c => e._cls.has(c),
    },
    addEventListener: (t, fn) => { (e._h[t] = e._h[t] || []).push(fn); },
    removeEventListener() { },
    appendChild: c => { e.children.push(c); c.parentNode = e; return c; },
    querySelectorAll: s => s === '.opt' ? e.children.filter(c => c._cls.has('opt')) : [],
    querySelector: s => e.children.find(c => c._cls.has(s.replace('.', ''))) || null,
    getContext: () => ctx2d, requestFullscreen() { },
    fire(t, ev) { (e._h[t] || []).forEach(fn => fn(Object.assign({ currentTarget: e, preventDefault() { }, code: '', clientX: 0, clientY: 0 }, ev || {}))); },
  };
  Object.defineProperty(e, 'className', {
    get: () => [...e._cls].join(' '),
    set: v => { e._cls = new Set(String(v).split(/\s+/).filter(Boolean)); },
  });
  return e;
}
const bySel = {};
const winH = {};
const win = {
  innerWidth: 1440, innerHeight: 900, devicePixelRatio: 1,
  addEventListener: (t, fn) => { (winH[t] = winH[t] || []).push(fn); },
  fire(t, ev) { (winH[t] || []).forEach(fn => fn(Object.assign({ preventDefault() { }, code: '', clientX: 0, clientY: 0 }, ev || {}))); },
};
const documentStub = {
  body: elStub('body'), documentElement: elStub('html'), head: elStub('head'), activeElement: null, fullscreenElement: null,
  querySelector: s => (bySel[s] = bySel[s] || elStub()),
  querySelectorAll: s => (s === '#dots i' && bySel['#dots'] ? bySel['#dots'].children : []),
  getElementById: id => (bySel['#' + id] = bySel['#' + id] || elStub()),
  createElement: t => elStub(t), addEventListener() { },
};
let _now = 0;
win.THREE = THREE;                 // 真实浏览器里 UMD 会把 THREE 挂到 window 上
const sandbox = {
  THREE, window: win, document: documentStub, console,
  performance: { now: () => _now },
  requestAnimationFrame: fn => { sandbox.__raf = fn; return 1; },
  setTimeout: (fn, ms) => { (sandbox.__timers = sandbox.__timers || []).push({ fn, at: _now + (ms || 0), done: false }); return 1; },
  clearTimeout: () => { },
  location: { reload() { } },
};

/* ============================ 载入主脚本 ============================ */
const file = path.join(__dirname, 'index.html');
const html = fs.readFileSync(file, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];

// A. 顶层（引擎未加载）必须安全执行
try { const a = Object.assign({}, sandbox); vm.createContext(a); vm.runInContext(code, a); pass++; }
catch (e) { fails.push('顶层在无 THREE 时执行失败: ' + e.message); }

// B. 含 THREE 桩执行
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: file });
pass++;
const G = e => vm.runInContext(e, sandbox);
const run = (fn, ...args) => vm.runInContext(fn, sandbox)(...args);
const Q = s => (bySel[s] = bySel[s] || elStub());

const POEM = G('POEM'), STAGES = G('STAGES'), CN = G('CN'), QUIZ = G('QUIZ');
const N = POEM.length;

/* ============================ 静态结构 ============================ */
ok(N === 4, 'POEM 应为 4 句，实为 ' + N);
ok(STAGES.length === N + 1, `STAGES 应为 ${N + 1}，实为 ${STAGES.length}`);
STAGES.forEach((s, i) => { if (i > 0) ok(s.name === POEM[i - 1].name, `境${i} 境名错位 ${s.name} ≠ ${POEM[i - 1].name}`); });
ok(CN.length >= N, 'CN 数组长度不足');
POEM.forEach((p, i) => {
  const han = p.segs.reduce((a, s) => a + [...s.c].filter(c => !/[，。、！？；：…—·]/.test(c)).length, 0);
  const py = p.segs.reduce((a, s) => a + s.p.length, 0);
  ok(han === py, `第${i + 1}句 汉字${han} ≠ 拼音${py}`);
  ok(!!p.read && !!p.yisi && !!p.jing && p.zhu.length >= 2, `第${i + 1}句六要素不全`);
});
ok(QUIZ.length === 5, '小测应为 5 题');
QUIZ.forEach((q, i) => ok(q.o.length === 3 && q.a >= 0 && q.a < 3, `小测${i + 1} 选项/答案异常`));
ok((code.match(/curIdx===4&&state==='stage'/g) || []).length >= 2, '第四境交互接线不足 2 处');
ok((code.match(/curIdx===2&&state==='stage'/g) || []).length >= 2, '第二境交互接线不足 2 处');
ok(/autoMode=true/.test(code), '自动游览未默认开启');
ok((html.match(/诗集目录/g) || []).length >= 2, '返回诗集目录链接不足 2 处');
ok(/clamp\(i,0,4\)/.test(code), '缺少 clamp(i,0,4)');
ok(code.includes("'05.mp3'"), '全诗音频 05.mp3 未引用');

/* ============================ 起引擎 ============================ */
run('initApp');
ok(G('window.__inited') === true, 'initApp 未标记初始化');
ok(G('state') === 'stage' && G('curIdx') === 0, '初始应停在封面境');

const errors = [];
let frames = 0;
function step(n, hook, stop) {
  for (let i = 0; i < n; i++) {
    if (stop && stop()) return;
    _now += 50;                                  // 每帧 50ms（主循环 dt 上限 0.05）
    const t = _now;
    for (const x of (sandbox.__timers || [])) {
      if (!x.done && x.at <= t) { x.done = true; try { x.fn(); } catch (e) { errors.push('timer: ' + e.message); } }
    }
    const raf = sandbox.__raf; sandbox.__raf = null;
    if (!raf) { errors.push('requestAnimationFrame 未续帧'); return; }
    try { raf(t); } catch (e) { errors.push('frame: ' + e.message); return; }
    frames++;
    if (hook) hook();
  }
}
step(40);
ok(G('renderer')._renders > 30, '封面境未持续渲染');
ok(G('curStageObj').group.children.length > 0, '封面 builder 未产出对象');

/* ============================ 五个 builder 单测 ============================ */
const builderNames = ['bCover', 'bGushan', 'bBirds', 'bGrassField', 'bCauseway'];
builderNames.forEach((nm, i) => {
  const def = STAGES[i];
  ok(def.build.name === nm, `STAGES[${i}].build 应为 ${nm}，实为 ${def.build.name}`);
  let st;
  try { st = def.build(); } catch (e) { fails.push(nm + ' build 抛错: ' + e.message); return; }
  ok(!!st.group && typeof st.update === 'function', nm + ' 缺 group/update');
  const lights = []; let shaders = 0, insts = 0;
  st.group.traverse(o => {
    if (o.isLight) lights.push(o);
    if (o.material && o.material.uniforms && o.material.uniforms.uFade) shaders++;
    if (o.setMatrixAt) insts++;
  });
  ok(lights.length >= 2, nm + ' 灯光不足（应含平行光+环境光）');
  ok(shaders >= 1, nm + ' 缺带 uFade 的着色器构件（水面/粒子）');
  try { for (let k = 0; k < 200; k++) st.update(k * 0.05, 0.05); pass++; }
  catch (e) { fails.push(nm + ' update 抛错: ' + e.message); }
  if (st.onEnter) { try { st.onEnter(); pass++; } catch (e) { fails.push(nm + ' onEnter 抛错: ' + e.message); } }
  if (st.click) {
    try { st.click(); for (let k = 0; k < 140; k++) st.update(k * 0.05, 0.05); pass++; }
    catch (e) { fails.push(nm + ' click 抛错: ' + e.message); }
  }
  try { run('setFade', st.group, 0); for (let k = 0; k < 30; k++) st.update(k * 0.05, 0.05); run('setFade', st.group, 1); pass++; }
  catch (e) { fails.push(nm + ' 淡出路径抛错: ' + e.message); }
  try { run('disposeGroup', st.group); pass++; } catch (e) { fails.push(nm + ' dispose 抛错: ' + e.message); }
  if (nm === 'bBirds' || nm === 'bGrassField') ok(insts >= (nm === 'bBirds' ? 0 : 5), nm + ' 实例化构件数量异常: ' + insts);
});
ok(!!G('birdCtl'), '交互境应有 birdCtl');
ok(!!G('causewayCtl'), '标志性瞬间 builder 应有 causewayCtl');

/* ============================ 全生命周期 ============================ */
const visited = new Set([0]);
Q('#enterBtn').fire('click');
step(80);
ok(G('curIdx') === 1, '点击入境后应到第 1 境，实为 ' + G('curIdx'));
const clicked = { 2: 0, 4: 0 };
step(3000, () => {
  const i = G('curIdx'); visited.add(i);
  if ((i === 2 || i === 4) && G('state') === 'stage' && clicked[i] < 3) {
    clicked[i]++;
    G('renderer').domElement.fire('pointerdown');
    win.fire('keydown', { code: 'Space' });
    win.fire('keydown', { code: 'ArrowRight' });
    win.fire('keydown', { code: 'ArrowLeft' });
  }
}, () => G('state') === 'ending');
ok(errors.length === 0, '运行期无异常: ' + errors.slice(0, 3).join(' | '));
ok(G('state') === 'ending', '自动游览应走到终章，实为 ' + G('state'));
ok(visited.size === 5, '应访问全部 5 境，实访 ' + [...visited].join(','));
ok(clicked[2] >= 1 && clicked[4] >= 1, '交互境点击未触发: ' + JSON.stringify(clicked));
ok(G('curIdx') === 4, '终章时应停在第 4 境');
ok(Q('#endPoem').children.length >= N, '终章未铺全诗');

Q('#btnPoemAudio').fire('click'); step(20);
Q('#btnAgain').fire('click'); step(80);
ok(G('state') === 'stage' && G('curIdx') === 1, '重新入境应回到第 1 境');
Q('#btnNext').fire('click'); step(60); Q('#btnPrev').fire('click'); step(60);
Q('#btnAuto').fire('click'); step(30); Q('#btnAuto').fire('click'); step(30);
Q('#btnPy').fire('click'); Q('#btnSpeak').fire('click'); Q('#btnSnd').fire('click'); step(20);
ok(G('state') === 'stage', '控件操作后应仍在 stage');
ok(errors.length === 0, '控件区异常: ' + errors.slice(0, 3).join(' | '));

// 小测 5 题全流程
run('startQuiz'); step(4);
ok(Q('#quiz')._cls.has('show'), '小测未显示');
for (let q = 0; q < 5; q++) {
  const body = Q('#quizBody');
  const opts = body.children.filter(c => c._cls.has('opt') && !c.disabled);
  ok(opts.length === 3, `第${q + 1}题选项应为 3，实为 ${opts.length}`);
  if (opts.length) opts[0].fire('click');
  const nb = body.children.find(c => c.id === 'quizNext');
  ok(!!nb, `第${q + 1}题缺下一题按钮`);
  if (nb) nb.fire('click');
  step(2);
}
ok(String(Q('#quizBody').innerHTML).includes('score'), '小测未出结果页');
const closeBtn = Q('#quizBody').children.find(c => c.id === 'quizClose');
ok(!!closeBtn, '小测缺关闭按钮');
if (closeBtn) closeBtn.fire('click');
ok(!Q('#quiz')._cls.has('show'), '小测未关闭');

// 回封面 → 进度点 → 逐境 → 末境 → showEnding 守卫
run('hideEnding', 'cover'); step(60);
ok(G('curIdx') === 0, '未回到封面');
Q('#dots').children.forEach(d => d.fire('click')); step(40);
for (let i = 1; i <= 4; i++) { run('goto', i); step(70); }
ok(G('curIdx') === 4, '逐境 goto 后应停在第 4 境');
run('showEnding'); step(10);
ok(G('state') === 'ending', 'showEnding 未生效');
run('showEnding'); run('showEnding'); pass++;   // 守卫：重复调用不应出错
ok(errors.length === 0, '终章区异常: ' + errors.slice(0, 3).join(' | '));

/* ============================ 音频核对 ============================ */
const audioDir = path.join(__dirname, 'audio');
if (fs.existsSync(audioDir)) {
  const mp3 = fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).sort();
  ok(mp3.length === N + 2, `audio 文件数 ${mp3.length} ≠ 诗句数+2=${N + 2}`);
  for (let i = 0; i <= N + 1; i++) {
    const f = String(i).padStart(2, '0') + '.mp3';
    ok(mp3.includes(f), '缺 ' + f);
  }
} else console.log('（跳过音频核对：audio/ 尚未生成）');

/* ============================ 汇总 ============================ */
console.log(`\n冒烟测试：${frames} 帧 · 通过 ${pass} 项 · 失败 ${fails.length} 项`);
if (fails.length) { fails.forEach(f => console.error('  ✗ ' + f)); process.exit(1); }
console.log('✓ smoke.test.js 全部通过');
