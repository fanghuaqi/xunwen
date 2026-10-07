/* smoke.test.js —— 卜算子·送鲍浩然之浙东（王观）深度冒烟测试
 * 用真实结构的 THREE 桩执行主脚本：boot() → 封面 → 逐境 goto → 五个 builder 的
 * build/update 深跑 → 第四境标志性交互「点击让春色随人同行」（1.2s 防连点守卫 +
 * 空格触发 + 春色流 maxA / 光带推移断言）→ 终章 → 回封面。
 * 另含：数据对齐 queue.json / 逐字注音与多音字 / 色板与赛道 / 水面雾参数同步 /
 * renderOrder 分层 / makeMist 的 fadeK / 标志性瞬间「山水叠化为眉眼」/ 自动游览默认开 /
 * 两处返回诗集目录链接。任何异常即失败。 */
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
  crossVectors(a, b) { this.x = a.y * b.z - a.z * b.y; this.y = a.z * b.x - a.x * b.z; this.z = a.x * b.y - a.y * b.x; return this; }
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
  setRGB(r, g, b) { this.r = r; this.g = g; this.b = b; return this; }
}
class Object3D {
  constructor() {
    this.children = []; this.userData = {}; this.position = new V3(); this.parent = null;
    this.rotation = { x: 0, y: 0, z: 0, set(x, y, z) { this.x = x; this.y = y; this.z = z; } };
    this.quaternion = { setFromAxisAngle() {} };
    this.matrix = {};
    this.scale = { x: 1, y: 1, z: 1, set(x, y, z) { this.x = x; this.y = y; this.z = z; }, setScalar(s) { this.x = s; this.y = s; this.z = s; } };
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true;
  }
  add(...os) { os.forEach(o => { this.children.push(o); o.parent = this; }); return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); }
  traverse(fn) { fn(this); this.children.forEach(c => c.traverse && c.traverse(fn)); }
  lookAt() {}
  updateMatrix() {}
  rotateOnAxis() {}
}
class Group extends Object3D {}
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Line extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; } }
class InstancedMesh extends Object3D {
  constructor(g, m, n) { super(); this.geometry = g; this.material = m; this.count = n;
    this.instanceMatrix = { needsUpdate: false, setUsage() {} }; }
  setMatrixAt() {}
}
class Scene extends Object3D {}
class Curve3 {
  constructor(p) { this.points = p; }
  getPoint(u) {
    const p = this.points, n = p.length - 1, x = Math.max(0, Math.min(0.9999, u)) * n;
    const i = Math.floor(x), t = x - i, a = p[i], b = p[Math.min(n, i + 1)];
    return new V3(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t, a.z + (b.z - a.z) * t);
  }
}
class Shape { moveTo() {} lineTo() {} quadraticCurveTo() {} bezierCurveTo() {} closePath() {} }
class BufferGeometry {
  constructor() { this.attributes = {}; }
  setAttribute(n, a) { this.attributes[n] = a; }
  setFromPoints() { return this; }
  dispose() {}
}
class BufferAttribute { constructor(arr, size) { this.array = arr; this.itemSize = size; this.needsUpdate = false; } }
const geo = n => class { constructor(...a) { this.type = n; this.args = a; }
  dispose() {} rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  translate() { return this; } center() { return this; } };
const matBase = () => class {
  constructor(o = {}) {
    Object.assign(this, { opacity: o.opacity === undefined ? 1 : o.opacity, transparent: !!o.transparent, userData: {} }, o);
    ['color', 'specular', 'emissive', 'fog'].forEach(k => { if (typeof this[k] === 'number') this[k] = new Color(this[k]); });
    if (!this.color) this.color = new Color(0xffffff);
    if (this.emissiveIntensity === undefined) this.emissiveIntensity = 1;
    this.map = this.map || null; this.isShaderMaterial = false; this.dispose = () => {};
    this.side = this.side || 0; this.blending = this.blending || 0;
  }
};
class ShaderMaterial {
  constructor(o = {}) { Object.assign(this, o); this.uniforms = o.uniforms || {}; this.isShaderMaterial = true;
    this.transparent = true; this.userData = {}; this.opacity = 1; this.map = null; this.dispose = () => {}; }
}
const THREE = {
  Vector3: V3, Vector2: V2, Color, Shape,
  Scene, Group, Mesh, Points, Line, Sprite, Object3D, InstancedMesh,
  BufferGeometry, BufferAttribute, ShaderMaterial, CanvasTexture: class { constructor() { this.dispose = () => {}; } },
  CatmullRomCurve3: Curve3,
  SphereGeometry: geo('Sphere'), CylinderGeometry: geo('Cyl'), BoxGeometry: geo('Box'), ConeGeometry: geo('Cone'),
  PlaneGeometry: geo('Plane'), RingGeometry: geo('Ring'), LatheGeometry: geo('Lathe'), CircleGeometry: geo('Circle'),
  TorusGeometry: geo('Torus'), TubeGeometry: geo('Tube'), ShapeGeometry: geo('Shape'), ExtrudeGeometry: geo('Extrude'),
  MeshBasicMaterial: matBase(), MeshPhongMaterial: matBase(), PointsMaterial: matBase(),
  SpriteMaterial: matBase(), LineBasicMaterial: matBase(),
  BackSide: 1, DoubleSide: 2, AdditiveBlending: 3, NormalBlending: 4, DynamicDrawUsage: {},
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
    classList: { _s: {}, add(c) { this._s[c] = true; }, remove(c) { delete this._s[c]; }, toggle(c, v) { if (v === undefined) v = !this._s[c]; v ? this._s[c] = true : delete this._s[c]; return v; }, contains(c) { return !!this._s[c]; } },
    addEventListener(t, f) { this._ls[t] = f; },
    appendChild() {}, querySelectorAll() { return []; },
  });
}
let now = 0;
function makeCanvas() {
  return { width: 0, height: 0,
    getContext() { return { font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
      createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {} }; } };
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
const setStageT = v => { vm.runInContext('stageT=' + v, sandbox); };

/* ---------- 数据断言（对齐 queue.json） ---------- */
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'busuanzi-song');
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
ok(joined === entry.text, 'segs 拼接与 queue.text 逐字一致：' + joined);
ok(joined === '水是眼波横，山是眉峰聚。欲问行人去那边？眉眼盈盈处。才始送春归，又送君归去。若到江南赶上春，千万和春住。',
  '分境标点严格照抄原文（，。？）');
ok(POEM.map(p => p.name).join('/') === '眼波眉峰/眉眼盈盈/送春送君/和春同住', '四境境名：' + POEM.map(p => p.name).join('/'));
ok(POEM.length === 4 && STAGES.length === 5, 'POEM=4 境、STAGES=5（含封面）');
ok(STAGES[0].key === 'cover', 'STAGES[0] 为封面');
STAGES.forEach((s, i) => { if (i > 0) ok(s.name === POEM[i - 1].name, `STAGES[${i}].name===POEM[${i - 1}].name (${s.name})`); });
ok(CN.length >= 4, 'CN 数字数组长度足够');
POEM.forEach((p, i) => {
  const han = [...p.segs.map(s => s.c).join('')].filter(c => !/[，。、！？；：]/.test(c)).length;
  const pyn = p.segs.reduce((a, s) => a + s.p.length, 0);
  ok(han === pyn, `第${i + 1}句 汉字${han}=拼音${pyn}`);
});
/* 多音字逐项核对：卜算子 bǔ / 鲍 bào / 浙 zhè / 那边 nǎ / 盈盈 yíng / 才始 cái shǐ / 和 hé / 横 héng / 处 chù */
const allPy = POEM.flatMap(l => l.segs.flatMap(s => s.p));
const need = ['shuǐ', 'shì', 'yǎn', 'bō', 'héng', 'shān', 'méi', 'fēng', 'jù',
  'yù', 'wèn', 'xíng', 'rén', 'qù', 'nǎ', 'biān', 'yíng', 'chù',
  'cái', 'shǐ', 'sòng', 'chūn', 'guī', 'yòu', 'jūn',
  'ruò', 'dào', 'jiāng', 'nán', 'gǎn', 'shàng', 'qiān', 'wàn', 'hé', 'zhù'];
ok(need.every(p => allPy.includes(p)), '全部 35 个音节注音就位（含 héng/nǎ/yíng/chù/hé）');
ok(!allPy.includes('nà'), '「那边」的「那」未误注 nà（应读 nǎ）');
ok(!allPy.includes('hèng'), '「眼波横」的「横」未误注 hèng（应读 héng）');
ok(!allPy.includes('hè') && !allPy.includes('huó'), '「千万和春住」的「和」未误注 hè/huó（应读 hé）');
ok(allPy.length === 44, '拼音总数 44（= 四句汉字总数 10+12+10+12）');
ok(POEM.every(p => p.zhu.length >= 2 && p.zhu.length <= 4), '每境注释 2-4 条');
ok(POEM.every(p => /考点/.test(p.zhu.map(z => z[0]).join(''))), '每境注释均含「考点」条目');
ok(POEM.every(p => p.jing && p.read && p.yisi), '每境意境题句/朗读文本/释义齐全');
ok((code.match(/read:'/g) || []).length === 4, 'read 字段 4 条（与诗句数一致）');
ok(QUIZ.length === 5 && QUIZ.every(q => q.o.length === 3 && q.a >= 0 && q.a < 3), '小测 5 题、各 3 选项、答案不越界');
ok(/水是眼波横/.test(QUIZ[0].q) && /山是眉峰聚/.test(QUIZ[0].o[0]), '接龙题①：水是眼波横 → 山是眉峰聚');
ok(/才始送春归/.test(QUIZ[1].q) && /又送君归去/.test(QUIZ[1].o[0]), '接龙题②：才始送春归 → 又送君归去');
ok(/卜算子/.test(QUIZ[2].q) && /bǔ/.test(QUIZ[2].o[1]), '读音题考词牌「卜算子」的「卜」读 bǔ');
ok(/王观/.test(QUIZ[3].o[1]) && /鲍浩然/.test(QUIZ[3].o[1]), '作者题：宋代词人王观送友人鲍浩然之浙东');
ok(/理解/.test(QUIZ[4].q) && /眉眼盈盈处/.test(QUIZ[4].o[0]) && /浙东/.test(QUIZ[4].o[0]) && /不写离愁/.test(QUIZ[4].o[0]),
  '主旨题：眉眼盈盈处＝浙东山水胜处，不写愁而写祝福');
const wm = code.match(/const words=\[([^\]]*)\]/);
ok(wm && wm[1].split(',').length === QUIZ.length + 1, '评语 words 长度=题数+1');
ok(!/将进酒|万古愁|如见太白|深得太白/.test(code), '无参考实现残留字样');
ok((code.match(/curIdx===4&&state==='stage'/g) || []).length >= 2, '交互境 curIdx===4 接线 ≥2 处（pointerdown+空格）');
ok(code.includes('clamp(i,0,4)'), 'goto 上界 clamp(i,0,4)');
ok(code.includes("'05.mp3'"), '全词音频 05.mp3 已引用');
ok(/if\(state!=='stage'\)return;/.test(code), 'showEnding 入口守卫存在');
ok(/--gold:\s*#9fc2b0/i.test(html), '--gold 为分配强调色 #9fc2b0');
ok(/background:#10141a/.test(html) && !(code.match(/0x05070d/g) || []).length, 'body 为烟雨底色 #10141a，主脚本无夜宴默认底色');
ok(!/#d4af37/.test(html), '全页无《将进酒》鎏金');
/* 赛道：烟雨江南的明媚变体 —— 春江/柳絮/眉峰，不写愁雨 */
ok(/FLOSS_VERT/.test(code) && /柳絮/.test(code), '自绘柳絮/飞花着色器在位（春色随人的母题）');
ok(/function makeEyeGaze/.test(code) && /function makeRidge/.test(code), '标志性瞬间「山水眉眼」骨架在位（眉峰 + 眼波水镜）');
ok((code.match(/ms:0\.001/g) || []).length >= 5, '五境月隐（ms 0.001，烟雨无月）');
ok(/update\(t,fk\)\{ const k=fk===undefined\?1:fk;/.test(code), 'makeMist.update 显式接收 fadeK（参考实现遗留隐患已修）');
/* 默认自动游览 + 返回诗集目录 */
ok(/let trans=null,stageT=0,autoT=0,autoMode=true;/.test(code), 'autoMode 变量默认 true');
ok(/<button id="btnAuto" class="on">自动游览 · 开<\/button>/.test(html), '自动游览按钮初始带 class="on" 且文案为「自动游览 · 开」');
const galLinks = (html.match(/class="galLink"/g) || []).length;
ok(galLinks === 2, '封面与终章各有 1 个 galLink（共 ' + galLinks + '）');
ok(/<a class="galLink" href="\.\.\/index\.html">← 返回诗集目录<\/a>/.test(html), '封面 enterBtn 下方返回诗集目录链接');
ok(/<a class="galLink" href="\.\.\/index\.html" style="align-self:center">诗集目录<\/a>/.test(html), '终章 btnCover 之后诗集目录链接');
ok(/\.galLink\{display:inline-block;font-family:var\(--song\);font-size:12\.5px/.test(html) && /#endBtns \.galLink\{align-self:center\}/.test(html), '.galLink 样式已注入 </style> 前');
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
ok(get('curIdx') === 0 && get('state') === 'stage', '封面境就绪');
fire('#enterBtn');
frames(220);
ok(EL['#stageNo'].textContent === '第壹境', '入境后到达第壹境（眼波眉峰）');
ok(get('autoMode') === true, '默认自动游览已开启');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第贰境', '下一境到达第贰境（眉眼盈盈）');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第叁境', '下一境到达第叁境（送春送君）');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第肆境', '下一境到达第肆境（和春同住）');
console.log('== 第四境标志性交互：点击让春色随人同行 ==');
frames(120);
const canvas = EL['canvas'];
const ctl = get('springCtl');
ok(!!ctl && ctl.on === false && typeof ctl.k === 'number', '春色控制器就位（初始未同行）');
canvas._ls.pointerdown();
frames(30);
ok(EL['#flash'].textContent === '千万和春住', '点击画面 → 题字「千万和春住」');
ok(ctl.on === true && ctl.k > 0.3, '春色随人同行已点亮（on=' + ctl.on + '，k=' + ctl.k.toFixed(2) + '）');
canvas._ls.pointerdown();   // 1.2s 守卫内连点，应被吞掉
ok(ctl.on === true, '守卫内连点未改状态');
frames(150);
ok(ctl.k > 0.85, '春色流渐亮至 k=' + ctl.k.toFixed(2));
const st4 = get('curStageObj');
let followSys = null, laneSys = null;
st4.group.traverse(c => {
  if (c.material && c.material.uniforms && c.material.uniforms.uMaxA && c.material.uniforms.uRise
      && c.geometry && c.geometry.attributes && c.geometry.attributes.position) {
    const n = c.geometry.attributes.position.array.length / 3;
    if (n === 260) followSys = c;
    if (n === 420) laneSys = c;
  }
});
ok(!!followSys && followSys.material.uniforms.uMaxA.value > 0.5,
  '跟舟春色流已点亮（uMaxA=' + (followSys ? followSys.material.uniforms.uMaxA.value.toFixed(2) : 'n/a') + '）');
ok(!!laneSys && laneSys.material.uniforms.uMaxA.value > 0.2, '春色光带已随人向江南推移（uMaxA=' + (laneSys ? laneSys.material.uniforms.uMaxA.value.toFixed(2) : 'n/a') + '）');
canvas._ls.pointerdown();
ok(ctl.on === false && EL['#flash'].textContent === '春且留住', '守卫外再点 → 收春，题「春且留住」（可反复）');
frames(90);
key('Space');
ok(ctl.on === true, '空格触发同一交互（点击接线第二处）');
frames(200);
key('ArrowRight'); frames(5);
ok(get('state') === 'ending', '末境 → 终章 showEnding 无异常');
key('Escape'); frames(5);
ok(get('state') === 'stage', 'Escape 返回舞台态');
fire('#btnSpeak');
fire('#btnPoemAudio');
fire('#btnAuto');
frames(5);
ok(get('autoMode') === false, '自动游览可一键关');
fire('#btnAuto');
fire('#btnAutoSpeak'); fire('#btnAutoSpeak');
fire('#btnPy'); fire('#btnPy');
fire('#btnSnd'); fire('#btnSnd');
fire('#btnQuiz'); frames(5);
ok(EL['#quizCnt'].textContent.indexOf('第 1 题') === 0, '小测开启并渲染首题');
ok(EL['#quizBody'].innerHTML.indexOf('水是眼波横') >= 0, '首题即接龙题');
key('ArrowRight');
ok(get('curIdx') === 4, '小测打开时方向键被忽略（模态保护）');
EL['#quiz'].classList.remove('show');
fire('#btnCover'); frames(220);
ok(get('curIdx') === 0, '回到封面 goto(0) 无异常');
key('ArrowRight'); frames(220);
ok(EL['#stageNo'].textContent === '第壹境', '封面 → 右键重新入境');

/* ---------- 各境 builder 直接深跑 ---------- */
console.log('== 逐境 build/update/click 深跑 ==');
STAGES.forEach((s, i) => {
  const st = s.build();
  ok(st && st.group && typeof st.update === 'function', `STAGES[${i}] build() 返回 group+update`);
  for (let k = 0; k < 320; k++) st.update(k * 0.016, 0.016);
  let clicks = 0;
  if (st.click) {
    for (let k = 0; k < 120; k++) st.update(k * 0.016, 0.016);
    st.click(); clicks++;
    st.click(); clicks++;
    for (let k = 0; k < 200; k++) st.update(k * 0.016, 0.016);
    st.click(); clicks++;
    for (let k = 0; k < 200; k++) st.update(k * 0.016, 0.016);
  }
  ok(true, `STAGES[${i}] 320+ 帧 update + ${clicks} 次 click（含防连点）无异常`);
});

/* ---------- 标志性瞬间：山水叠化为眉眼 ---------- */
console.log('== 标志性瞬间：山水化作眉眼的盈盈春色 ==');
const stEye = STAGES[1].build();
const shapeMeshes = [];
const ridgeGlows = [];
stEye.group.traverse(c => {
  if (c.geometry && c.geometry.type === 'Shape') shapeMeshes.push(c);
  if (c.geometry && c.geometry.type === 'Tube' && c.material && c.material.blending === 3) ridgeGlows.push(c);
});
ok(shapeMeshes.length >= 3, '眼波水镜 / 内辉 / 眼睑暗幕 三片杏眼面在位（' + shapeMeshes.length + ' 片）');
ok(ridgeGlows.length >= 2, '左右眉脊微光各一条（山 → 眉，' + ridgeGlows.length + ' 条）');
setStageT(2.0); stEye.update(2.0, 0.016);
const lensOp0 = shapeMeshes[0].material.opacity, glowOp0 = ridgeGlows[0].material.opacity;
setStageT(19.6); stEye.update(19.6, 0.016);
const lensOp1 = shapeMeshes[0].material.opacity, glowOp1 = ridgeGlows[0].material.opacity;
ok(lensOp0 < 0.05 && lensOp1 > 0.28,
  `山水叠化：眼波水镜由 ${lensOp0.toFixed(3)} 亮起至 ${lensOp1.toFixed(3)}（停留越久越像眉眼）`);
ok(glowOp0 < 0.05 && glowOp1 > 0.45,
  `眉脊微光由 ${glowOp0.toFixed(3)} 亮起至 ${glowOp1.toFixed(3)}（峰峦连成一道眉）`);
let blinkMax = 0;
for (let k = 0; k < 1400; k++) { stEye.update(k * 0.016, 0.016); const o = shapeMeshes[2].material.opacity; if (o > blinkMax) blinkMax = o; }
ok(blinkMax > 0.3, '眉眼会缓缓眨一下（眼睑暗幕峰值 opacity=' + blinkMax.toFixed(2) + '）');
const stGaze = STAGES[2].build();
const extrudes = [];
stGaze.group.traverse(c => { if (c.geometry && c.geometry.type === 'Extrude') extrudes.push(c); });
ok(extrudes.length === 1 && !!extrudes[0].parent, '兰舟船身（Shape+Extrude）在位');
const boatX0 = extrudes[0].parent.position.x;
setStageT(1.0); stGaze.update(1.0, 0.016);
setStageT(21.0); stGaze.update(21.0, 0.016);
const boatX1 = extrudes[0].parent.position.x;
ok(boatX0 > 40 && boatX1 < 20, `行人渐近「眉眼盈盈处」：兰舟 x ${boatX0.toFixed(1)} → ${boatX1.toFixed(1)}`);
const boatTwinkle = [];
stGaze.group.traverse(c => { if (c.material && c.material.uniforms && c.material.uniforms.uSpeed && c.material.uniforms.uRise
  && c.geometry.attributes.position.array.length / 3 === 200) boatTwinkle.push(c); });
ok(boatTwinkle.length === 1, '「盈盈」水光粒子 200 点（眼波内一泓盈盈春水）');

/* ---------- fadeK 与水面雾参数同步 ---------- */
console.log('== fadeK / 雾参数同步 / 透明物分层 ==');
const stMist = STAGES[3].build();
const sprites = [];
stMist.group.traverse(c => { if (c.material && c.material.isShaderMaterial === false && c.material.map && c.scale && c.scale.x > 10 && c.renderOrder === 5) sprites.push(c); });
ok(sprites.length >= 8, '第叁境大团雾 Sprite ' + sprites.length + ' 片（renderOrder=5）');
stMist.group.userData.fadeK = 1; stMist.update(3.0, 0.016);
const opFull = sprites[0].material.opacity;
stMist.group.userData.fadeK = 0.5; stMist.update(3.0, 0.016);
const opHalf = sprites[0].material.opacity;
ok(opFull > 0 && Math.abs(opHalf - opFull / 2) < 1e-9,
  `雾的 opacity 乘了父链 fadeK（${opFull.toFixed(4)} → ${opHalf.toFixed(4)}，防止交叉淡化时雾滞留）`);
stMist.group.userData.fadeK = 1; stMist.update(3.0, 0.016);
/* 另外两处每帧写 opacity 的地方（眉眼 / 花光）同样必须乘 fadeK */
const stEyeF = STAGES[1].build();
const shapeF = [];
stEyeF.group.traverse(c => { if (c.geometry && c.geometry.type === 'Shape') shapeF.push(c); });
setStageT(20); stEyeF.group.userData.fadeK = 1; stEyeF.update(20, 0.016);
const eyeFull = shapeF[0].material.opacity;
stEyeF.group.userData.fadeK = 0.5; stEyeF.update(20, 0.016);
ok(eyeFull > 0.29 && Math.abs(shapeF[0].material.opacity - eyeFull / 2) < 1e-9,
  `眼波水镜 opacity 乘了 fadeK（${eyeFull.toFixed(3)} → ${shapeF[0].material.opacity.toFixed(3)}）`);
const stBloom = STAGES[3].build();
const halos = [];
stBloom.group.traverse(c => { if (c.renderOrder === 4 && c.material && c.material.isShaderMaterial === false
  && c.material.map && c.scale && c.scale.x > 10) halos.push(c); });
setStageT(5); stBloom.group.userData.fadeK = 1; stBloom.update(5, 0.016);
const haloFull = halos.length ? halos[0].material.opacity : 0;
stBloom.group.userData.fadeK = 0.5; stBloom.update(5, 0.016);
ok(halos.length >= 3 && haloFull > 0 && Math.abs(halos[0].material.opacity - haloFull / 2) < 1e-9,
  `春树花光 halo opacity 乘了 fadeK（${haloFull.toFixed(3)} → ${(halos.length ? halos[0].material.opacity : 0).toFixed(3)}）`);
const waters = [];
stMist.group.traverse(c => { if (c.material && c.material.isShaderMaterial && c.material.uniforms && c.material.uniforms.uFogDensity) waters.push(c); });
ok(waters.length === 1, '水面自定义着色器在位（1 面）');
get('applySky')();
const fg = waters[0].material.uniforms.uFogColor.value, sg = get('scene').fog.color;
ok(Math.abs(waters[0].material.uniforms.uFogDensity.value - get('scene').fog.density) < 1e-12
  && Math.abs(fg.r - sg.r) < 1e-9 && Math.abs(fg.g - sg.g) < 1e-9 && Math.abs(fg.b - sg.b) < 1e-9,
  '水面着色器雾参数与场景同步（uFogDensity=' + waters[0].material.uniforms.uFogDensity.value.toFixed(4)
  + ' / 雾色 rgb=' + fg.r.toFixed(3) + ',' + fg.g.toFixed(3) + ',' + fg.b.toFixed(3) + '）');
ok(get('skyDome').renderOrder === -10 && get('starA').renderOrder === -9 && get('moonGroup').renderOrder === -8
  && waters[0].renderOrder === 1 && sprites[0].renderOrder === 5,
  'renderOrder 分层：穹顶 -10 < 星 -9 < 月 -8 < 水 1 < 雾 5');
ok(get('moonMesh').material.fog === false && get('starA').material.fog === false, '星/月材质 fog:false（不被雾吞）');
ok(STAGES.map(s => s.sky()).every(k => k.ms <= 0.001), '五境皆月隐（ms ≤ 0.001，烟雨赛道无月）');
/* 春色母题：柳絮粒子 / 春树 / 兰舟 / 柳 */
const flossSys = [];
STAGES[4].build().group.traverse(c => { if (c.material && c.material.uniforms && c.material.uniforms.uWind) flossSys.push(c); });
ok(flossSys.length === 1, '柳絮粒子（FLOSS 着色器 uWind）在位');
const trees = [];
STAGES[4].build().group.traverse(c => { if (c.count && c.count === 44) trees.push(c); });
ok(trees.length >= 4, '江南两岸桃杏 ' + trees.length + ' 株（花开随点击而重明）');
const houses = [];
STAGES[4].build().group.traverse(c => { if (c.material && c.material.color && Math.abs(c.material.color.r - 0.866) < 0.01) houses.push(c); });
ok(houses.length >= 6, '白墙黛瓦民居 ' + houses.length + ' 面墙（江南人家）');

console.log(failures ? `\n冒烟测试失败 ${failures} 项` : '\n冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
