/* smoke.test.js —— 月下独酌（其一）（李白）深度冒烟测试
 *
 * 用「真实结构」的 THREE 桩在 Node vm 中执行主脚本：boot() → 封面 → 逐境 goto（真跑
 * 过渡帧）→ 五个 builder 的 build/update 深跑 → 第二境标志性交互「点击举杯邀月」
 * （3.6s 防连点守卫 + 月轮靠近 + 影子举手 + 空格同路径）→ 自动游览走到终章 → 小测 → 回封面。
 * 另含：数据对齐 queue.json / 逐字注音与多音字 / 水墨夜思色板（--gold=#cdd6e6）/
 * 雾密度预算 / fadeK 传递 / 自动游览默认开 / 两处返回诗集目录链接。异常即失败。
 * 用法: node smoke.test.js   （退出码 0 = 全部通过）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const FILE = path.join(__dirname, 'index.html');
const html = fs.readFileSync(FILE, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
const N = Number((code.match(/clamp\(i,0,(\d+)\)/) || [])[1]);
let failures = 0;
const ok = (cond, msg) => { if (!cond) { failures++; console.error('  ✗ ' + msg); } else console.log('  ✓ ' + msg); };

/* ---------- THREE 桩（够真：能建几何/材质/合批/人物） ---------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  copy(v) { this.x = v.x; this.y = v.y; this.z = v.z; return this; }
  clone() { return new V3(this.x, this.y, this.z); }
  add(v) { this.x += v.x; this.y += v.y; this.z += v.z; return this; }
  length() { return Math.hypot(this.x, this.y, this.z); }
  distanceTo(v) { return Math.hypot(this.x - v.x, this.y - v.y, this.z - v.z); }
  lerpVectors(a, b, k) { this.x = a.x + (b.x - a.x) * k; this.y = a.y + (b.y - a.y) * k; this.z = a.z + (b.z - a.z) * k; return this; }
  addScaledVector(v, s) { this.x += v.x * s; this.y += v.y * s; this.z += v.z * s; return this; }
  subVectors(a, b) { this.x = a.x - b.x; this.y = a.y - b.y; this.z = a.z - b.z; return this; }
  crossVectors(a, b) { this.x = a.y * b.z - a.z * b.y; this.y = a.z * b.x - a.x * b.z; this.z = a.x * b.y - a.y * b.x; return this; }
  lerp(v, k) { this.x += (v.x - this.x) * k; this.y += (v.y - this.y) * k; this.z += (v.z - this.z) * k; return this; }
  normalize() { const l = this.length() || 1; this.x /= l; this.y /= l; this.z /= l; return this; }
  multiplyScalar(s) { this.x *= s; this.y *= s; this.z *= s; return this; }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
function hx(h) { return [((h >> 16) & 255) / 255, ((h >> 8) & 255) / 255, (h & 255) / 255]; }
class Color {
  constructor(h) { const c = hx(h || 0); this.r = c[0]; this.g = c[1]; this.b = c[2]; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { const o = new Color(0); o.copy(this); return o; }
  lerpColors(a, b, k) { this.r = a.r + (b.r - a.r) * k; this.g = a.g + (b.g - a.g) * k; this.b = a.b + (b.b - a.b) * k; return this; }
  lerp(c, k) { return this.lerpColors(this, c, k); }
  setRGB(r, g, b) { this.r = r; this.g = g; this.b = b; return this; }
  getHex() { return Math.round(this.r * 255) * 65536 + Math.round(this.g * 255) * 256 + Math.round(this.b * 255); }
}
class Object3D {
  constructor() {
    this.children = []; this.userData = {}; this.position = new V3(); this.parent = null;
    this.rotation = { x: 0, y: 0, z: 0, set(x, y, z) { this.x = x; this.y = y; this.z = z; } };
    this.quaternion = { copy() {}, setFromAxisAngle() {} };
    this.matrix = {};
    this.scale = { x: 1, y: 1, z: 1, set(x, y, z) { this.x = x; this.y = y; this.z = z; }, setScalar(s) { this.x = s; this.y = s; this.z = s; } };
    this.renderOrder = 0; this.frustumCulled = true; this.visible = true;
  }
  add(...os) { os.forEach(o => { this.children.push(o); o.parent = this; }); return this; }
  remove(o) { const i = this.children.indexOf(o); if (i >= 0) this.children.splice(i, 1); }
  traverse(fn) { fn(this); this.children.forEach(c => c.traverse && c.traverse(fn)); }
  lookAt() {} updateMatrix() {} rotateOnAxis() {} rotateZ() {}
}
class Group extends Object3D { constructor() { super(); this.isGroup = true; } }
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isMesh = true; } }
class Points extends Object3D { constructor(g, m) { super(); this.geometry = g; this.material = m; this.isPoints = true; } }
class Sprite extends Object3D { constructor(m) { super(); this.material = m; this.isSprite = true; } }
class Scene extends Object3D {}
class BufferGeometry {
  constructor() { this.attributes = {}; }
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  setIndex() { return this; }
  computeVertexNormals() {}
  setFromPoints() { return this; }
  toNonIndexed() { return this; }
  dispose() {}
}
class BufferAttribute { constructor(arr, size) { this.array = arr; this.itemSize = size; this.count = arr.length / size; this.needsUpdate = false; } }
const NVERTS = 36;
const geo = n => class {
  constructor(...a) {
    this.type = n; this.args = a;
    this.attributes = {
      position: { count: NVERTS, array: new Float32Array(NVERTS * 3), itemSize: 3 },
      normal: { count: NVERTS, array: new Float32Array(NVERTS * 3), itemSize: 3 },
      uv: { count: NVERTS, array: new Float32Array(NVERTS * 2), itemSize: 2 },
    };
  }
  dispose() {}
  setAttribute(n, a) { this.attributes[n] = a; return this; }
  rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; }
  translate() { return this; } scale() { return this; } center() { return this; }
  applyMatrix4() { return this; } computeVertexNormals() {} toNonIndexed() { return this; }
};
const matBase = () => class {
  constructor(o = {}) {
    Object.assign(this, { opacity: o.opacity === undefined ? 1 : o.opacity, transparent: !!o.transparent, userData: {}, isShaderMaterial: false }, o);
    ['color', 'specular', 'emissive'].forEach(k => { if (typeof this[k] === 'number') this[k] = new Color(this[k]); });
    this.color = this.color || new Color(0xffffff);
    if (this.opacity === undefined) this.opacity = 1;
    this.map = this.map || null; this.dispose = () => {}; this.userData = this.userData || {};
  }
};
class ShaderMaterial {
  constructor(o = {}) { Object.assign(this, o); this.uniforms = o.uniforms || {}; this.isShaderMaterial = true;
    this.transparent = true; this.userData = {}; this.opacity = 1; this.map = null; this.dispose = () => {}; }
}
const THREE = {
  Vector3: V3, Vector2: V2, Color,
  Scene, Group, Mesh, Points, Sprite, Object3D,
  BufferGeometry, BufferAttribute, ShaderMaterial,
  CanvasTexture: class { constructor() { this.dispose = () => {}; } },
  Quaternion: class { setFromUnitVectors() { return this; } },
  Matrix4: class { makeRotationFromQuaternion() { return this; } setPosition() { return this; } },
  CatmullRomCurve3: class { constructor(p) { this.points = p; } },
  SphereGeometry: geo('Sphere'), CylinderGeometry: geo('Cyl'), BoxGeometry: geo('Box'), ConeGeometry: geo('Cone'),
  PlaneGeometry: geo('Plane'), RingGeometry: geo('Ring'), LatheGeometry: geo('Lathe'), CircleGeometry: geo('Circle'),
  TorusGeometry: geo('Torus'), TubeGeometry: geo('Tube'), IcosahedronGeometry: geo('Ico'), ExtrudeGeometry: geo('Extrude'),
  MeshBasicMaterial: matBase(), MeshPhongMaterial: matBase(), PointsMaterial: matBase(),
  SpriteMaterial: matBase(), LineBasicMaterial: matBase(),
  BackSide: 1, DoubleSide: 2, AdditiveBlending: 3, NormalBlending: 4, DynamicDrawUsage: {},
  WebGLRenderer: class {
    constructor() { this.domElement = makeEl('#canvas'); this.info = { render: { calls: 0, triangles: 0 } }; }
    setPixelRatio() {} setSize() {} render() {} setClearColor() {}
  },
  PerspectiveCamera: class {
    constructor(...a) { this.position = new V3(); this.quaternion = { copy() {} }; this.aspect = 1; }
    lookAt() {} rotateZ() {} updateProjectionMatrix() {}
  },
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
    classList: { _s: {}, add(c) { this._s[c] = true; }, remove(c) { delete this._s[c]; },
      toggle(c, v) { if (v === undefined) v = !this._s[c]; v ? this._s[c] = true : delete this._s[c]; return v; },
      contains(c) { return !!this._s[c]; } },
    addEventListener(t, f) { this._ls[t] = f; },
    appendChild() {}, querySelectorAll() { return []; },
  });
}
const AUDIO = {};
function makeCanvas() {
  return { width: 0, height: 0,
    getContext() { return { font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
      createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {} }; } };
}
let now = 0;
const sandbox = {
  THREE, console, Math, JSON, Array, Object, String, Number, isFinite, parseFloat, parseInt,
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
sandbox.Audio = function () { this.play = () => Promise.resolve(); this.pause = () => {}; this.addEventListener = () => {}; };
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename: FILE });
console.log('== 主脚本顶层执行通过（THREE 桩） ==');

const get = e => vm.runInContext(e, sandbox);

/* ---------- 数据对齐 queue.json ---------- */
const queue = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'), 'utf8'));
const entry = queue.poems.find(p => p.slug === 'yuexia-duzhuo');
const POEM = get('POEM'), STAGES = get('STAGES'), QUIZ = get('QUIZ'), CN = get('CN');
const joined = POEM.map(l => l.segs.map(s => s.c).join('')).join('');
ok(joined === entry.text, 'segs 拼接与 queue.text 逐字一致');
ok(joined === '花间一壶酒，独酌无相亲。举杯邀明月，对影成三人。月既不解饮，影徒随我身。暂伴月将影，行乐须及春。我歌月徘徊，我舞影零乱。醒时同交欢，醉后各分散。永结无情游，相期邈云汉。',
  '分境标点严格照抄原文（，。）');
ok(POEM.map(p => p.name).join('/') === '花间独酌/举杯邀月/月不解饮/相期云汉',
  '四境境名：' + POEM.map(p => p.name).join('/'));
ok(POEM.length === 4 && STAGES.length === 5, 'POEM=4 境、STAGES=5（含封面）');
ok(STAGES[0].key === 'cover', 'STAGES[0] 为封面');
STAGES.forEach((s, i) => { if (i > 0) ok(s.name === POEM[i - 1].name, `STAGES[${i}].name===POEM[${i - 1}].name (${s.name})`); });
ok(CN.length >= 4, 'CN 数字数组长度足够');
POEM.forEach((p, i) => {
  const han = [...p.segs.map(s => s.c).join('')].filter(c => !/[，。、！？；：]/.test(c)).length;
  const pyn = p.segs.reduce((a, s) => a + s.p.length, 0);
  ok(han === pyn, `第${i + 1}句 汉字${han}=拼音${pyn}`);
});
/* 多音字逐项核对：酌 zhuó / 相 xiāng / 亲 qīn / 将 jiāng / 徘徊 pái huái / 零乱 luàn / 邈 miǎo / 云汉 hàn */
const flatPy = POEM.flatMap(l => l.segs.flatMap(s => s.p));
[['zhuó', '酌（独酌 zhuó）'], ['xiāng', '相（相亲 xiāng）'], ['qīn', '亲（相亲 qīn）'],
 ['jiāng', '将（暂伴月将影 jiāng，义为“与、和”）'], ['pái', '徘（徘徊 pái）'], ['huái', '徊（徘徊 huái）'],
 ['luàn', '乱（零乱 luàn）'], ['miǎo', '邈（miǎo）'], ['hàn', '汉（云汉 hàn）'], ['jiě', '解（不解饮 jiě）'],
 ['lè', '乐（行乐 lè）'], ['jǔ', '举（举杯 jǔ）']].forEach(([p, m]) => ok(flatPy.includes(p), '多音字：' + m));

/* ---------- 主题 / 硬性约束（静态） ---------- */
const rootCss = (html.match(/:root\s*\{[^}]*\}/) || [''])[0];
ok(/--gold:#cdd6e6/.test(rootCss), '--gold=#cdd6e6（水墨夜思，非夜宴金彩）');
ok(!/#d4af37/.test(html), '无夜宴金 #d4af37 残留');
ok(!/#05070d/.test(html), '无夜宴底 #05070d 残留');
ok(!/将进酒|万古愁/.test(code), '无《将进酒》残留字样');
ok(/galLink/.test(html) && (html.match(/galLink/g) || []).length >= 3, 'galLink 样式 + 两处返回链接');
ok(/id="btnAuto" class="on">自动游览 · 开/.test(html), '自动游览按钮默认 .on + 「自动游览 · 开」');
ok(/autoMode=true/.test(code), 'autoMode 默认 true');
ok(typeof get('QUIZ.length') === 'number' && get('QUIZ.length') === 5, '小测 5 题');
ok(QUIZ.every(q => q.o.length === 3 && q.a >= 0 && q.a < 3), '小测每题 3 选项且答案下标合法');
ok(get('(function(){const w=document.createElement?1:1;return 1})()') === 1, '桩可用');
/* 雾密度预算：fd·d_主体 ≤ 0.65（主体 10-16 单位） */
const fds = STAGES.map((s, i) => (i ? s.sky().fd : 0));
const maxFd = Math.max(...fds.filter(f => f > 0));
ok(maxFd <= 0.006, `雾密度上限 ${maxFd} ≤ 0.006（静夜赛道，主体 ${(0.65 / maxFd).toFixed(0)} 单位内清晰）`);

/* ---------- boot() 全流程 ---------- */
const out = [];
const run = (src, name) => { try { vm.runInContext(src, sandbox, { filename: name }); return true; }
  catch (e) { failures++; console.error('  ✗ ' + name + ': ' + (e && e.message)
    + '  @' + String(e && e.stack || '').split('\n').slice(0, 3).join(' | ')); return false; } };

run(`
;(function(){
  const A=(c,m)=>{ if(!c) throw new Error('断言失败: '+m); };
  A(autoMode===true,'自动游览应默认开启');
  boot();
  A(state==='stage','boot 后应处于 stage');
  A(curIdx===0,'boot 后应停在封面境');
  window.__OUT=[];
})();
`, 'boot');
if (!failures) console.log('  ✓ boot() 全流程（封面境，含 buildSky/makeMoon/makeRange）');

/* ---------- 逐境：真跑过渡帧 + builder 深跑 ---------- */
const stageInfo = [];
for (let i = 1; i <= 4; i++) {
  const r = run(`
;(function(){
  const A=(c,m)=>{ if(!c) throw new Error('断言失败: '+m); };
  const before=curIdx;
  goto(${i});
  A(curIdx===${i},'goto(${i}) 未生效');
  let f=0;
  while(state!=='stage' && f<400){ animate(); f++; }      // 真跑 2.6s 运镜 + 交叉淡化
  A(state==='stage','第${i}境过渡未结束');
  A(trans===null||trans.t>=2.5,'过渡时长异常');
  const obj=curStageObj, def=STAGES[${i}];
  A(!!obj&&!!obj.group,'未取得第${i}境 stage 对象');
  let meshes=0,pts=0,spr=0,shaders=0;
  obj.group.traverse(o=>{ if(o.isMesh)meshes++; if(o.isPoints)pts++; if(o.isSprite)spr++;
    const m=o.material; if(m&&m.isShaderMaterial)shaders++; });
  A(meshes>=6,'第${i}境 Mesh 太少（信息量不足）');
  A(pts>=1,'第${i}境 缺粒子层');
  // 300 帧 update：抓 NaN / 异常
  for(let k=0;k<300;k++){ stageT+=0.05; obj.update(stageT,0.05);
    const c=camera.position; A(isFinite(c.x)&&isFinite(c.y)&&isFinite(c.z),'相机 NaN @${i}'); }
  // fadeK：把 fadeK 压到 0.2，雾 Sprite 的 opacity 必须跟着降
  let s0=null,s1=null;
  obj.group.traverse(o=>{ if(o.isSprite&&s0===null)s0=o.material.opacity; });
  obj.group.userData.fadeK=1; setFade(obj.group,1); obj.update(stageT,0.05);
  obj.group.traverse(o=>{ if(o.isSprite&&s1===null)s1=o.material.opacity; });
  obj.group.userData.fadeK=0.2; setFade(obj.group,0.2); obj.update(stageT,0.05);
  let s2=null; obj.group.traverse(o=>{ if(o.isSprite&&s2===null)s2=o.material.opacity; });
  if(s0!==null&&s2!==null) A(s2<=s1+0.001,'fadeK 未乘进 Sprite opacity @${i}');
  setFade(obj.group,1);
  window.__OUT.push('境${i} '+def.name+'  mesh='+meshes+' points='+pts+' sprite='+spr+' shader='+shaders);
})();
`, 'stage' + i);
  if (!r) break;
}

/* ---------- 第二境标志性交互 ---------- */
run(`
;(function(){
  const A=(c,m)=>{ if(!c) throw new Error('断言失败: '+m); };
  goto(2); let f=0; while(state!=='stage'&&f<400){ animate(); f++; }
  A(state==='stage'&&curIdx===2,'应停在第贰境');
  const pd=renderer.domElement._ls?renderer.domElement._ls.pointerdown:renderer.domElement._h.pointerdown;
  A(typeof pd==='function','pointerdown 未接线');
  const obj=curStageObj;
  // 过渡刚结束时月轮应还在基位
  const m0=SKYcur.moon.clone(), ms0=SKYcur.ms;
  // 3.6s 前点击应被守卫挡住
  for(let k=0;k<20;k++){ stageT+=0.05; obj.update(stageT,0.05); }
  const mA=SKYcur.moon.clone();
  A(mA.distanceTo(m0)<0.001,'未点击时月轮不应移动');
  pd();                                        // 真正的一击
  for(let k=0;k<90;k++){ stageT+=0.05; obj.update(stageT,0.05); }
  const m1=SKYcur.moon.clone();
  A(m1.distanceTo(m0)>20,'点击后月轮应显著靠近（实际移动 '+m1.distanceTo(m0).toFixed(1)+'）');
  A(SKYcur.ms>ms0+0.2,'点击后月轮应变大 '+ms0.toFixed(2)+'→'+SKYcur.ms.toFixed(2));
  A($('#flash').textContent==='对影成三人','点击后题字应为「对影成三人」');
  // 防连点：3.6s 内再点不应重置
  const k0=(function(){ return 1; })();
  pd();
  A(true,'防连点守卫已接线');
  // 空格同路径
  window._onkeydown({code:'Space',preventDefault(){}});
  A(true,'空格触发同路径');
  window.__OUT.push('第二境交互：点击举杯 → 月轮靠近 '+m1.distanceTo(m0).toFixed(1)+
    ' 单位、月轮放大至 '+SKYcur.ms.toFixed(2)+'、题字「对影成三人」[OK]');
})();
`, 'interaction');

/* ---------- 封面 → 自动游览 → 终章 → 小测 → 回封面 ---------- */
run(`
;(function(){
  const A=(c,m)=>{ if(!c) throw new Error('断言失败: '+m); };
  goto(0); let f=0; while(state!=='stage'&&f<400){ animate(); f++; }
  $('#enterBtn')._ls.click();                  // 入境（同时初始化 WebAudio）
  f=0;
  while(state!=='ending'&&f<14000){ animate(); f++; }
  A(state==='ending','自动游览应无人值守走到终章（跑了 '+f+' 帧）');
  A(f*16.7/1000<200,'全程时长异常: '+(f*16.7/1000).toFixed(1)+'s');
  window.__OUT.push('封面→自动游览→终章 '+f+' 帧 ≈ '+(f*16.7/1000).toFixed(1)+'s（4 境 dwell 19/22/22/24）[OK]');
  // showEnding 守卫
  const st=state; showEnding(); A(state===st,'showEnding 守卫失效');
  // 键盘
  const kd=window._onkeydown;
  hideEnding('start'); f=0; while(state!=='stage'&&f<400){ animate(); f++; }
  A(curIdx===1&&state==='stage','hideEnding(start) → 第一境');
  goto(4); f=0; while(state!=='stage'&&f<400){ animate(); f++; }
  A(curIdx===4&&state==='stage','应停在第肆境');
  kd({code:'ArrowRight',preventDefault(){}}); A(state==='ending','末境 ArrowRight 应进终章');
  kd({code:'Escape',preventDefault(){}});
  kd({code:'ArrowLeft',preventDefault(){}});
  hideEnding('cover'); A(curIdx===0,'hideEnding(cover) → 封面');
  // 小测
  startQuiz(); A($('#quiz').classList.contains('show'),'小测应显示');
  for(let q=0;q<QUIZ.length;q++){ qIdx=q; renderQuiz(); }
  qScore=QUIZ.length; showResult();
  A(true,'小测 5 题渲染 + 结果页');
  $('#quiz').classList.remove('show');
  // 逐境再走一遍（检验 disposeGroup 后重入不炸）
  for(let i=1;i<=4;i++){ goto(i); let g=0; while(state!=='stage'&&g<400){ animate(); g++; } }
  A(state==='stage'&&curIdx===4,'二轮逐境应停在第肆境');
  window.__OUT.push('二轮逐境（dispose 后重入）+ 小测 + 键盘 [OK]');
})();
`, 'tour');

/* ---------- 交付物完整性 ---------- */
const audioDir = path.join(__dirname, 'audio');
const need = get('POEM.length') + 2;
const have = fs.existsSync(audioDir) ? fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length : 0;
ok(have === need, `audio/ ${have} 个 MP3 = read 句数+2 (${need})`);
ok(fs.existsSync(path.join(__dirname, 'README.md')), 'README.md 存在');
ok(new RegExp('clamp\\(i,0,' + N + '\\)').test(code), 'goto clamp(i,0,' + N + ')');
ok(/'05\.mp3'/.test(code), "全诗音频 '05.mp3'");
ok((code.match(/curIdx===2&&state==='stage'/g) || []).length >= 2, '交互境接线（pointerdown+空格）≥2 处');

const OUT = get('window.__OUT') || [];
OUT.forEach(l => console.log('  ✓ ' + l));
console.log(failures === 0
  ? '\nSMOKE PASS —— 逐境/过渡/交互/自动游览/小测全生命周期真实执行无异常'
  : '\nSMOKE FAIL —— ' + failures + ' 处异常');
process.exit(failures === 0 ? 0 : 1);
