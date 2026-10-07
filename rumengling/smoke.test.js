/* smoke.test.js —— 如梦令（李清照）深度冒烟测试
 * 用真实结构的 THREE 桩执行主脚本：boot() → 封面 → 逐境 goto → 四个 builder 的
 * build/update 深跑 → 第三境标志性瞬间「点击卷帘看海棠」click（1.2s 防连点守卫 +
 * 空格触发 + 卷帘 scale 断言）→ 终章 → 回封面；另含数据对齐/逐字注音/多音字/
 * 色板/自动游览默认开/返回诗集目录链接的断言。任何异常即失败。 */
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
    this.children = []; this.userData = {}; this.position = new V3();
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
class BufferGeometry {
  constructor() { this.attributes = {}; this._pos = null; }
  setAttribute(n, a) { this.attributes[n] = a; if (n === 'position') this._pos = a; }
  setFromPoints() { return this; }
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
  constructor(o = {}) { Object.assign(this, o); this.uniforms = o.uniforms || {}; this.isShaderMaterial = true; this.transparent = true; this.userData = {}; this.dispose = () => {}; }
}
const THREE = {
  Vector3: V3, Vector2: V2, Color,
  Scene, Group, Mesh, Points, Line, Sprite, Object3D, InstancedMesh,
  BufferGeometry, BufferAttribute, ShaderMaterial,
  CanvasTexture: class { constructor() { this.dispose = () => {}; this.wrapS = 0; this.wrapT = 0; this.repeat = { set() {} }; } clone() { return new this.constructor(); } },
  CatmullRomCurve3: class { constructor(p) { this.points = p; } },
  SphereGeometry: geo('Sphere'), CylinderGeometry: geo('Cyl'), BoxGeometry: geo('Box'), ConeGeometry: geo('Cone'),
  PlaneGeometry: geo('Plane'), RingGeometry: geo('Ring'), LatheGeometry: geo('Lathe'), CircleGeometry: geo('Circle'),
  TorusGeometry: geo('Torus'), TubeGeometry: geo('Tube'),
  MeshBasicMaterial: mat(), MeshPhongMaterial: mat(), PointsMaterial: mat(), SpriteMaterial: mat(), LineBasicMaterial: mat(),
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
  return {
    width: 0, height: 0,
    getContext() {
      return {
        font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
        createRadialGradient: () => ({ addColorStop() {} }), createLinearGradient: () => ({ addColorStop() {} }),
        fillRect() {}, clearRect() {}, fillText() {},
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

/* ---------- 数据断言（对齐 queue.json） ---------- */
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'rumengling');
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
ok(joined === entry.text, 'segs 拼接与 queue.text 逐字一致：' + joined);
ok(joined === '昨夜雨疏风骤，浓睡不消残酒。试问卷帘人，却道海棠依旧。知否，知否？应是绿肥红瘦。', '标点严格照抄原文（，。？！）');
ok(POEM.length === 3 && STAGES.length === 4, 'POEM=3 境、STAGES=4（含封面）');
ok(STAGES[0].key === 'cover', 'STAGES[0] 为封面');
STAGES.forEach((s, i) => { if (i > 0) ok(s.name === POEM[i - 1].name, `STAGES[${i}].name===POEM[${i - 1}].name (${s.name})`); });
ok(CN.length >= 3, 'CN 数字数组长度足够');
POEM.forEach((p, i) => {
  const han = [...p.segs.map(s => s.c).join('')].filter(c => !/[，。、！？；：]/.test(c)).length;
  const pyn = p.segs.reduce((a, s) => a + s.p.length, 0);
  ok(han === pyn, `第${i + 1}句 汉字${han}=拼音${pyn}`);
});
/* 多音字逐项核对：骤 zhòu / 疏 shū / 浓 nóng / 睡 shuì / 卷 juǎn / 不 bù / 绿 lǜ / 应 yīng / 否 fǒu / 瘦 shòu */
const allPy = POEM.flatMap(l => l.segs.flatMap(s => s.p));
const need = ['zuó', 'yè', 'yǔ', 'shū', 'fēng', 'zhòu', 'nóng', 'shuì', 'bù', 'xiāo', 'cán', 'jiǔ',
  'shì', 'wèn', 'juǎn', 'lián', 'rén', 'què', 'dào', 'hǎi', 'táng', 'yī', 'jiù',
  'zhī', 'fǒu', 'yīng', 'lǜ', 'féi', 'hóng', 'shòu'];
ok(need.every(p => allPy.includes(p)), '全部 30 个音节注音就位（含 shū/zhòu/juǎn/lǜ/yīng/fǒu）');
ok(!allPy.includes('juàn') && !allPy.includes('juàn,'), '「卷帘」的「卷」未误注 juàn');
ok(!allPy.includes('lù'), '「绿肥红瘦」的「绿」未误注 lù');
ok(!allPy.includes('yìng'), '「应是」的「应」未误注 yìng');
ok(allPy.length === 33, '拼音总数 33（= 三句汉字总数 12+11+10）');
ok(QUIZ.length === 5 && QUIZ.every(q => q.o.length === 3 && q.a >= 0 && q.a < 3), '小测 5 题、各 3 选项、答案不越界');
ok(/昨夜雨疏风骤/.test(QUIZ[0].q) && /试问卷帘人/.test(QUIZ[1].q), '接龙题 ×2 覆盖上下句');
ok(/卷/.test(QUIZ[2].q) && /juǎn/.test(QUIZ[2].o[1]), '多音字题考「卷」的读音与词义');
ok(/婉约派/.test(QUIZ[3].o[0]) && /小令/.test(QUIZ[3].q), '作者题考婉约派＋易安居士＋小令');
ok(/绿肥红瘦/.test(QUIZ[4].q) && /借代/.test(QUIZ[4].o[0]), '名句理解题考「绿肥红瘦」的借代与炼字');
const wm = code.match(/const words=\[([^\]]*)\]/);
ok(wm && wm[1].split(',').length === QUIZ.length + 1, '评语 words 长度=题数+1');
ok(!/将进酒|万古愁|如见太白|深得太白/.test(code), '无参考实现残留字样');
ok((code.match(/curIdx===3&&state==='stage'/g) || []).length >= 2, '交互境 curIdx===3 接线 ≥2 处（pointerdown+空格）');
ok(code.includes('clamp(i,0,3)'), 'goto 上界 clamp(i,0,3)');
ok(code.includes("'04.mp3'"), '全词音频 04.mp3 已引用');
ok(/if\(state!=='stage'\)return;/.test(code), 'showEnding 入口守卫存在');
ok(/--gold:\s*#c9a0b0/i.test(html), '--gold 为分配强调色 #c9a0b0');
ok(/background:#10141a/.test(html) && !(code.match(/0x05070d/g) || []).length, 'body 为烟雨底色 #10141a，主脚本无夜宴默认底色');
ok(!/#d4af37/.test(html), '全页无《将进酒》鎏金');
/* 赛道：烟雨江南（雨丝/雾/藏月） */
ok(/RAIN_VERT|RAIN_FRAG/.test(code) && /PETAL_FRAG/.test(code), '自绘雨丝/花瓣着色器在位（烟雨母题）');
ok((code.match(/ms:0\.001/g) || []).length >= 4, '四境月隐（ms 0.001，烟雨无月）');
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
ok(EL['#stageNo'].textContent === '第壹境', '入境后到达第壹境');
ok(get('autoMode') === true, '默认自动游览已开启');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第贰境', '下一境到达第贰境（卷帘问答）');
fire('#btnNext'); frames(220);
ok(EL['#stageNo'].textContent === '第叁境', '下一境到达第叁境（绿肥红瘦）');
console.log('== 第三境标志性瞬间：点击卷帘看海棠 ==');
frames(40);
const canvas = EL['canvas'];
const ctl = get('rollCtl');
ok(!!ctl && ctl.open === false && ctl.cur && ctl.cur.roll, '卷帘控制器与帘对象就位（帘初垂）');
const rollClose = ctl.cur.roll.scale.y;
ok(Math.abs(rollClose - 1) < 1e-6, '入第三境时帘幕垂合（roll.scale.y=' + rollClose + '）');
canvas._ls.pointerdown();
frames(30);
ok(EL['#flash'].textContent === '绿肥红瘦', '点击画面 → 题字「绿肥红瘦」');
ok(ctl.open === true && ctl.k > 0.6, '帘卷起（open=' + ctl.open + '，k=' + ctl.k.toFixed(2) + '）');
ok(ctl.cur.roll.scale.y < 0.5, '帘幕卷起动画生效（roll.scale.y=' + ctl.cur.roll.scale.y.toFixed(3) + '）');
canvas._ls.pointerdown();   // 1.2s 守卫内连点，应被吞掉
ok(ctl.open === true, '守卫内连点未改状态（不会误垂帘）');
frames(120);
ok(ctl.cur.roll.scale.y < 0.06, '帘已卷至顶（roll.scale.y=' + ctl.cur.roll.scale.y.toFixed(3) + '）');
canvas._ls.pointerdown();
ok(ctl.open === false && EL['#flash'].textContent === '海棠依旧', '守卫外再点 → 垂帘，题「海棠依旧」（可反复卷帘）');
frames(90);
key('Space');
ok(ctl.open === true, '空格触发同一交互（点击接线第二处）');
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
ok(EL['#quizBody'].innerHTML.indexOf('昨夜雨疏风骤') >= 0, '首题即接龙题');
key('ArrowRight');
ok(get('curIdx') === 3, '小测打开时方向键被忽略（模态保护）');
EL['#quiz'].classList.remove('show');   // 等价于点「回到终章」
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
    for (let k = 0; k < 120; k++) st.update(k * 0.016, 0.016);   // 越过 1.2s 守卫
    st.click(); clicks++;
    st.click(); clicks++;                                        // 守卫内连点应被吞
    for (let k = 0; k < 200; k++) st.update(k * 0.016, 0.016);
    st.click(); clicks++;
    for (let k = 0; k < 200; k++) st.update(k * 0.016, 0.016);
  }
  ok(true, `STAGES[${i}] 320+ 帧 update + ${clicks} 次 click（含防连点）无异常`);
});
/* 标志性瞬间行为断言：帘卷 → 绿叶繁茂 / 红花凋残 */
const st3 = STAGES[3].build();
const g3 = st3.group;
ok(get('rollCtl') && typeof get('rollCtl').cur.roll.scale.y === 'number', '第三境帘对象可查（roll.scale.y）');
st3.update(0.5, 0.016);
const roll0 = get('rollCtl').cur.roll.scale.y;
for (let k = 0; k < 100; k++) st3.update(0.5 + k * 0.016, 0.016);
st3.click();                                     // 卷帘
for (let k = 0; k < 200; k++) st3.update(2.1 + k * 0.016, 0.016);
const roll1 = get('rollCtl').cur.roll.scale.y;
ok(roll0 > 0.9 && roll1 < 0.06, `帘卷动画：${roll0.toFixed(2)} → ${roll1.toFixed(3)}（垂帘 → 卷至顶，露出海棠）`);
const inst = [];
g3.traverse(c => { if (c.geometry && /InstancedMesh|Sphere|Plane/.test(c.geometry.type) && c.count) inst.push(c); });
const leaves = inst.find(c => c.count >= 250);
const flowers = inst.find(c => c.count === 22);
ok(!!leaves && leaves.count >= 300, '海棠叶茂：「绿肥」——' + (leaves ? leaves.count : 0) + ' 片绿叶（InstancedMesh）');
ok(!!flowers && flowers.count === 22, '海棠花疏：「红瘦」——' + (flowers ? flowers.count : 0) + ' 朵残红');
ok(!!leaves && leaves.material.emissiveIntensity > 0.8, '卷帘后叶上水光转亮（emissiveIntensity=' + leaves.material.emissiveIntensity.toFixed(2) + ' > 垂帘时 0.55）');
const petalPts = [];
g3.traverse(c => { if (c.geometry && c.geometry.attributes && c.geometry.attributes.aSize && c.material && c.material.uniforms && c.material.uniforms.uTop) petalPts.push(c); });
ok(petalPts.length === 1, '飘零红瓣粒子系统在位（' + petalPts.length + ' 组）');
const greenGlow = [];
g3.traverse(c => { if (c.material && c.material.uniforms && c.material.uniforms.uColor && c.material.uniforms.uRise) greenGlow.push(c); });
ok(greenGlow.length >= 1, '帘卷后叶间水光粒子在位');
/* 淡入淡出系数：每帧写 opacity 的地方必须乘 fadeK */
const st1 = STAGES[1].build();
const ripples = st1.group.children.filter(c => c.geometry && c.geometry.type === 'Ring');
ok(ripples.length >= 7, '第壹境湿地面涟漪 ' + ripples.length + ' 圈');
st1.group.userData.fadeK = 0.5;
st1.update(1.2, 0.016);
ok(ripples[0].material.opacity <= 0.26, '涟漪 opacity 乘了 fadeK（' + ripples[0].material.opacity.toFixed(3) + ' ≤ 0.25）');
st1.group.userData.fadeK = 1;
st1.update(1.2, 0.016);
/* 雨丝：风偏与层数 */
const rains = [];
st1.group.traverse(c => { if (c.material && c.material.uniforms && c.material.uniforms.uFall) rains.push(c); });
ok(rains.length >= 2, '第壹境雨丝两层（远/近）共 ' + rains.length + ' 组');
const uw = rains[0].material.uniforms.uWind.value, us = rains[0].material.uniforms.uSlant.value;
ok(uw > 1.5 && us > 0.2, '「风骤」：雨丝带风斜（uWind=' + uw.toFixed(2) + '，uSlant=' + us.toFixed(3) + '）');

console.log(failures ? `\n冒烟测试失败 ${failures} 项` : '\n冒烟测试全部通过 ✓');
process.exit(failures ? 1 : 0);
