#!/usr/bin/env node
/* smoke.test.js —— 题西林壁 深度冒烟测试
 * 用「可运算的真实 THREE 桩」在 Node 里跑 index.html 主脚本：
 *   boot() → 逐境 goto(+settle 动画) → 每境 build/update/click/onEnter/sky()
 *   → 境一巡游镜头位移断言 → 境三五机位点击链路（含节流守卫/雾密度联动）
 *   → 山体几何断言（主峰/谷底/崖壁包围）→ 末境 showEnding → 小测渲染
 *   → 自动游览全程 → 越界钳制。用法: node smoke.test.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const file = path.join(__dirname, 'index.html');
const html = fs.readFileSync(file, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];

let pass = 0, fail = 0;
const ok = (cond, msg) => { if (cond) { pass++; console.log('  ✓ ' + msg); } else { fail++; console.error('  ✗ ' + msg); } };

/* ---------------- 可运算 THREE 桩 ---------------- */
class V3 {
  constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; }
  set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; }
  setScalar(s) { return this.set(s, s, s); }
  copy(v) { return this.set(v.x, v.y, v.z); }
  clone() { return new V3(this.x, this.y, this.z); }
  add(v) { return this.set(this.x + v.x, this.y + v.y, this.z + v.z); }
  addScaledVector(v, s) { return this.set(this.x + v.x * s, this.y + v.y * s, this.z + v.z * s); }
  subVectors(a, b) { return this.set(a.x - b.x, a.y - b.y, a.z - b.z); }
  crossVectors(a, b) { return this.set(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x); }
  multiplyScalar(s) { return this.set(this.x * s, this.y * s, this.z * s); }
  normalize() { const l = Math.hypot(this.x, this.y, this.z) || 1; return this.multiplyScalar(1 / l); }
  lerpVectors(a, b, t) { return this.set(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t, a.z + (b.z - a.z) * t); }
  lerp(v, a) { return this.lerpVectors(this, v, a); }
  length() { return Math.hypot(this.x, this.y, this.z); }
  dot(v) { return this.x * v.x + this.y * v.y + this.z * v.z; }
}
class V2 { constructor(x = 0, y = 0) { this.x = x; this.y = y; } }
class Color {
  constructor(h) { this.r = 0; this.g = 0; this.b = 0; if (h !== undefined) this.setHex(h); }
  setHex(h) { this.r = ((h >> 16) & 255) / 255; this.g = ((h >> 8) & 255) / 255; this.b = (h & 255) / 255; return this; }
  copy(c) { this.r = c.r; this.g = c.g; this.b = c.b; return this; }
  clone() { return new Color(0).copy(this); }
  lerp(c, a) { this.r += (c.r - this.r) * a; this.g += (c.g - this.g) * a; this.b += (c.b - this.b) * a; return this; }
  lerpColors(a, b, t) { this.r = a.r + (b.r - a.r) * t; this.g = a.g + (b.g - a.g) * t; this.b = a.b + (b.b - a.b) * t; return this; }
  multiplyScalar(s) { this.r *= s; this.g *= s; this.b *= s; return this; }
}
class Euler { constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; } }
class Quaternion { constructor() { this.x = 0; this.y = 0; this.z = 0; this.w = 1; } setFromAxisAngle() { return this; } }
class Matrix4 { constructor() { this.elements = new Float32Array(16); } }
class Object3D {
  constructor() {
    this.position = new V3(); this.rotation = new Euler(); this.scale = new V3(1, 1, 1);
    this.quaternion = new Quaternion(); this.userData = {}; this.children = [];
    this.visible = true; this.renderOrder = 0; this.frustumCulled = true;
    this.matrix = new Matrix4(); this.parent = null;
  }
  add(...cs) { for (const c of cs) { c.parent = this; this.children.push(c); } return this; }
  remove(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); return this; }
  traverse(fn) { fn(this); for (const c of this.children) c.traverse(fn); }
  updateMatrix() { return this; }
  rotateOnAxis() { return this; }
  rotateZ() { return this; }
  lookAt() { return this; }
}
class Group extends Object3D { constructor() { super(); this.type = 'Group'; } }
class Mesh extends Object3D { constructor(g, m) { super(); this.geometry = g || {}; this.material = m || {}; } }
class Points extends Mesh { }
class Line extends Mesh { }
class Sprite extends Object3D { constructor(m) { super(); this.material = m || {}; } }
class InstancedMesh extends Object3D {
  constructor(g, m, n) { super(); this.geometry = g; this.material = m; this.count = n;
    this.instanceMatrix = { setUsage() {}, needsUpdate: false }; }
  setMatrixAt() { return this; }
}
class Light extends Object3D {
  constructor(c, i) { super(); this.isLight = true; this.color = new Color(c === undefined ? 0xffffff : c);
    this.intensity = i === undefined ? 1 : i; }
}
class DirectionalLight extends Light { }
class AmbientLight extends Light { }
class PointLight extends Light { constructor(c, i, d) { super(c, i); this.distance = d || 0; } }
class MatBase {
  constructor(p) {
    Object.assign(this, { opacity: 1, transparent: false, fog: true, side: 0 }, p || {});
    if (this.color !== undefined && !(this.color instanceof Color)) this.color = new Color(this.color);
    this.userData = {};
  }
  dispose() {}
}
class MeshBasicMaterial extends MatBase { }
class MeshPhongMaterial extends MatBase { }
class LineBasicMaterial extends MatBase { }
class PointsMaterial extends MatBase { }
class SpriteMaterial extends MatBase { }
class ShaderMaterial extends MatBase { constructor(p) { super(p); this.isShaderMaterial = true; this.uniforms = (p && p.uniforms) || {}; } }
class GeoBase { dispose() {} rotateX() { return this; } rotateY() { return this; } rotateZ() { return this; } }
class PlaneGeometry extends GeoBase { constructor(...a) { super(); this.args = a; } }
class SphereGeometry extends GeoBase { }
class ConeGeometry extends GeoBase { }
class CylinderGeometry extends GeoBase { }
class BoxGeometry extends GeoBase { }
class CircleGeometry extends GeoBase { }
class LatheGeometry extends GeoBase { constructor(pts) { super(); this.points = pts; } }
class TorusGeometry extends GeoBase { }
class RingGeometry extends GeoBase { }
class ShapeGeometry extends GeoBase { }
class Shape { moveTo() { return this; } quadraticCurveTo() { return this; } }
class BufferGeometry extends GeoBase {
  constructor() { super(); this.attributes = {}; }
  setAttribute(name, attr) { this.attributes[name] = attr; return this; }
  setIndex(i) { this.index = i; return this; }
  setFromPoints(pts) { this.points = pts; return this; }
  computeVertexNormals() { this._normalsDone = true; return this; }
}
class BufferAttribute { constructor(arr, n) { this.array = arr; this.itemSize = n; this.needsUpdate = false; } }
class CanvasTexture { constructor(c) { this.image = c; } dispose() {} }
class FogExp2 { constructor(c, d) { this.color = new Color(c); this.density = d; } }
class Scene extends Object3D { constructor() { super(); this.fog = null; } }
class PerspectiveCamera extends Object3D { constructor(fov, aspect) { super(); this.fov = fov; this.aspect = aspect; } updateProjectionMatrix() {} }
class WebGLRenderer {
  constructor() { this.domElement = elStub(); }
  setPixelRatio() {} setSize() {} render() {} setClearColor() {}
}
const THREE = {
  Vector3: V3, Vector2: V2, Color, Euler, Quaternion, Matrix4,
  Object3D, Group, Mesh, Points, Line, Sprite, InstancedMesh,
  DirectionalLight, AmbientLight, PointLight,
  MeshBasicMaterial, MeshPhongMaterial, LineBasicMaterial, PointsMaterial, SpriteMaterial, ShaderMaterial,
  PlaneGeometry, SphereGeometry, ConeGeometry, CylinderGeometry, BoxGeometry, CircleGeometry,
  LatheGeometry, TorusGeometry, RingGeometry, ShapeGeometry, Shape, BufferGeometry, BufferAttribute,
  CanvasTexture, FogExp2, Scene, PerspectiveCamera, WebGLRenderer,
  AdditiveBlending: 1, NormalBlending: 2, BackSide: 1, DoubleSide: 2, DynamicDrawUsage: 1,
};

/* ---------------- DOM 桩 ---------------- */
const ctx2d = () => ({
  font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0, fillStyle: '',
  createRadialGradient: () => ({ addColorStop() {} }),
  fillRect() {}, fillText() {},
});
function elStub() {
  return {
    tagName: 'DIV', className: '', title: '', textContent: '', innerHTML: '', open: false,
    style: {}, offsetWidth: 0,
    classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
    addEventListener() {}, appendChild() {}, querySelectorAll() { return []; }, blur() {},
  };
}
const canvasStub = () => ({ width: 0, height: 0, getContext: () => ctx2d() });

let simMs = 0;
const sandbox = {
  THREE,
  console,
  Math, String, Number, Array, Object, Float32Array, Promise,
  performance: { now: () => (simMs += 16.7) },
  requestAnimationFrame() {},
  setTimeout: () => 0, clearTimeout() {},
  location: { reload() {} },
  document: {
    querySelector: () => elStub(),
    createElement: t => (t === 'canvas' ? canvasStub() : elStub()),
    addEventListener() {},
    querySelectorAll: () => [],
    documentElement: elStub(), body: elStub(), head: elStub(),
    activeElement: null, fullscreenElement: null,
    getElementById: () => elStub(),
  },
};
sandbox.window = { addEventListener() {}, innerWidth: 1280, innerHeight: 720, devicePixelRatio: 1, __inited: false };
vm.createContext(sandbox);

/* ---------------- 执行 ---------------- */
console.log('== 1. 顶层解析执行 ==');
try {
  vm.runInContext(code, sandbox, { filename: 'index.html' });
  ok(true, '顶层在 THREE 桩下执行成功');
} catch (e) { ok(false, '顶层执行失败: ' + e.message); }

console.log('== 2. 数据一致性 ==');
const poemLen = vm.runInContext('POEM.length', sandbox);
const stagesLen = vm.runInContext('STAGES.length', sandbox);
ok(poemLen === 3, 'POEM 有 3 句 (实际 ' + poemLen + ')');
ok(stagesLen === 4, 'STAGES = 封面+3 = 4 (实际 ' + stagesLen + ')');
const align = vm.runInContext(`POEM.every((p,i)=>STAGES[i+1].name===p.name)`, sandbox);
ok(align, 'STAGES[i].name === POEM[i-1].name 逐一对齐');
const joined = vm.runInContext(`POEM.map(l=>l.segs.map(s=>s.c).join('')).join('')`, sandbox);
const TEXT = '横看成岭侧成峰，远近高低各不同。不识庐山真面目，只缘身在此山中。';
ok(joined === TEXT, '各境 segs 拼接 === 队列 text 原文');
const pyOK = vm.runInContext(`POEM.every(l=>l.segs.every(s=>[...s.c].filter(c=>!/[,，。、！？；：…—·]/.test(c)).length===s.p.length))`, sandbox);
ok(pyOK, '每句汉字数 = 拼音数');
const wordsN = (code.match(/words\s*=\s*\[([^\]]*)\]/) || ['', ''])[1].split(',').length;
ok(wordsN === 6, '小测评语 words 为 6 项 (实际 ' + wordsN + ')');

console.log('== 3. 山体几何断言（同一座庐山） ==');
try {
  const geo = vm.runInContext(`(function(){
    const H=lushanH;
    const peak=H(58,2), pit=H(38,-4), camY=${'PIT_Y'};
    const ring=[]; const R=11;
    for(let k=0;k<8;k++){ const a=k/8*Math.PI*2;
      ring.push(H(38+Math.sin(a)*R, -4+Math.cos(a)*R)); }
    return {peak,pit,camY,ring,
      ridge:H(-95,0), east:H(92,-10)};
  })()`, sandbox);
  ok(geo.peak > 60, '主峰 (58,2) 高耸: ' + geo.peak.toFixed(1));
  ok(geo.peak > geo.ridge * 2, '主峰远高于西段岭脉（侧看成峰的形体基础）: ' + geo.peak.toFixed(1) + ' vs ' + geo.ridge.toFixed(1));
  ok(geo.camY > geo.pit, '境三机位悬在谷底之上 (camY=' + geo.camY.toFixed(1) + ' > pit=' + geo.pit.toFixed(1) + ')');
  const walls = geo.ring.filter(h => h > geo.camY + 6).length;
  ok(walls >= 5, '谷底四周 ' + walls + '/8 方向有崖壁（南向谷口开放，供镜头落入）');
  const camY = vm.runInContext('PIT_Y', sandbox);
  ok(camY > 5 && camY < 60, '谷底机位高度合理: ' + camY.toFixed(1));
} catch (e) { ok(false, '山体断言抛错: ' + e.message); }

console.log('== 4. boot() ==');
try { vm.runInContext('boot()', sandbox); ok(true, 'boot() 完成（渲染器/天空/封面境）'); }
catch (e) { ok(false, 'boot() 抛错: ' + e.stack); }

const settle = n => vm.runInContext(`for(let _i=0;_i<${n};_i++)animate();`, sandbox);

console.log('== 5. 逐境 goto + 动画走完 ==');
for (let i = 1; i <= 3; i++) {
  try {
    vm.runInContext(`goto(${i})`, sandbox);
    settle(220); // 220×16.7ms ≈ 3.7s > 2.6s 过渡
    const cur = vm.runInContext('curIdx', sandbox);
    const state = vm.runInContext('state', sandbox);
    ok(cur === i && state === 'stage', `第${i}境 goto 完成 (curIdx=${cur}, state=${state})`);
  } catch (e) { ok(false, `第${i}境 goto 抛错: ` + e.stack); }
}

console.log('== 6. 境一巡游：镜头自动走过 横→侧→远→近 ==');
try {
  vm.runInContext(`goto(1)`, sandbox); settle(160); // 过渡刚结束
  const p1 = vm.runInContext('camera.position.z', sandbox);
  settle(420); // +7s → 应到达“侧看”附近
  const p2 = vm.runInContext('camera.position.x', sandbox);
  const moved = Math.abs(p2 - 178) < 40 && p1 > 100;
  ok(p1 > 100, '巡游起点=横看机位 (camZ=' + p1.toFixed(1) + ')');
  ok(moved, '巡游推进到侧看机位附近 (camX=' + p2.toFixed(1) + ')');
  settle(3600); // 走完整个巡游+驻留
} catch (e) { ok(false, '境一巡游断言抛错: ' + e.message); }

console.log('== 7. 每境 builder 深跑：build/update 多帧/click/onEnter/sky() ==');
const buildProbe = `
(function(){
  const out=[];
  for(let i=0;i<STAGES.length;i++){
    const d=STAGES[i];
    const st=d.build();
    if(!st.group)throw new Error('境'+i+' 无 group');
    if(st.update){
      for(const t of [0,0.5,1.7,3.3,5.9,9.2,13.1,17.8]) st.update(t,0.016);
    }
    if(st.onEnter)st.onEnter();
    if(st.click){ st.click(); st.click(); } // 冷却守卫 + 再次触发
    const sk=d.sky();
    if(!sk.top||!sk.hor||!sk.fog||typeof sk.fd!=='number'||!sk.moon)throw new Error('境'+i+' sky() 不全');
    out.push(i);
    scene.remove(st.group);
  }
  return out.join(',');
})()
`;
try {
  const r = vm.runInContext(buildProbe, sandbox);
  ok(true, '全部 4 境 build/update(t×8 帧)/click/onEnter/sky() 通过 (' + r + ')');
} catch (e) { ok(false, 'builder 深跑抛错: ' + e.message + '\n' + (e.stack || '').split('\n').slice(0, 4).join('\n')); }

console.log('== 8. 交互境 click 链路（五机位循环 + 节流 + 雾密度联动） ==');
try {
  // §6 的 60s 驻留会让 autoMode 自动游览走完全程进入 ending（curIdx 停在 3）：
  // 此时 goto(3) 会因 i===curIdx 早退，click 链路全在 ending 态下失真（update 不推进 ctl.t）。
  // 先关 autoMode 并跳回封面，再入交互境取得全新 bShenzhong 实例（viewIdx=0、节流 ctl={t:99} 重置）；
  // 同时避免 §8 后半程累计 autoT 超 dwell(18s) 提前触发 showEnding（§11 会自行重新开启 autoMode）。
  vm.runInContext(`autoMode=false; goto(0)`, sandbox); settle(220);
  vm.runInContext(`goto(3)`, sandbox); settle(200);
  const r = vm.runInContext(`(function(){
    const log=[];
    const camY0=camera.position.y;
    // 第 1 击：山中→横看（节流期内连击应只生效一次）
    curStageObj.click(); const v1=viewIdx;
    curStageObj.click(); const v2=viewIdx;
    for(let i=0;i<150;i++)animate(); // 2.5s 平滑运镜
    const zAfterHeng=camera.position.z, xAfterHeng=camera.position.x, fdHeng=SKYcur.fd;
    // 走完 側→远→近→山中
    for(let k=0;k<4;k++){ for(let i=0;i<140;i++)animate(); curStageObj.click(); }
    for(let i=0;i<140;i++)animate();
    log.push('guard='+(v1===1&&v2===1?'ok':'FAIL'),
      'camZ='+(zAfterHeng>120&&xAfterHeng<30?'heng-ok':'FAIL'),
      'fd='+(fdHeng<0.008?'fog-open-ok':'FAIL'),
      'camY0='+camY0.toFixed(1),'viewIdx='+viewIdx,
      'backInPit='+(camera.position.y<PIT_Y+6?'ok':'FAIL'));
    return log.join(' | ');
  })()`, sandbox);
  ok(/guard=ok/.test(r), '节流守卫：冷却期连击只生效一次');
  ok(/camZ=heng-ok/.test(r), '点击后镜头滑向横看机位 (z>120, x<30): ' + r);
  ok(/fd=fog-open-ok/.test(r), '切出山中后雾密度联动变清 (fd<0.008)');
  ok(/backInPit=ok/.test(r), '五击循环回到山中机位: ' + r);
  // 快速五连击（每击间隔 ≥ 冷却）应恰好绕一整圈回原位
  const full = vm.runInContext(`(function(){
    for(let k=0;k<5;k++){ curStageObj.click(); for(let i=0;i<90;i++)animate(); }
    return viewIdx;
  })()`, sandbox);
  ok(full === 0, '再绕一整圈 viewIdx 归零 (实际 ' + full + ')');
} catch (e) { ok(false, '交互境 click 抛错: ' + e.message); }

console.log('== 9. 末境 / 终章 / 小测 ==');
try {
  vm.runInContext(`goto(3); for(let _i=0;_i<3;_i++)animate(); showEnding();`, sandbox);
  ok(vm.runInContext('state', sandbox) === 'ending', 'showEnding() 进入终章态');
  vm.runInContext(`startQuiz(); renderQuiz(); showResult();`, sandbox);
  ok(true, '小测渲染 + 结果页通过');
  vm.runInContext(`$('#quiz').classList.remove('show'); hideEnding('cover');`, sandbox);
  settle(10);
  ok(vm.runInContext('curIdx', sandbox) === 0, '回到封面');
} catch (e) { ok(false, '终章/小测抛错: ' + e.message); }

console.log('== 10. 越界钳制 ==');
try {
  vm.runInContext(`goto(0)`, sandbox); settle(220);
  ok(vm.runInContext('curIdx', sandbox) === 0 && vm.runInContext('state', sandbox) === 'stage', '回到封面并稳定');
  vm.runInContext(`goto(99)`, sandbox); settle(220);
  ok(vm.runInContext('curIdx', sandbox) === 3, 'goto(99) 钳制到 3');
} catch (e) { ok(false, '越界钳制抛错: ' + e.message); }

console.log('== 11. 自动游览全程无操作走完 ==');
try {
  vm.runInContext(`autoMode=true; autoT=0; goto(1);`, sandbox); settle(220);
  settle(5400); // 3境(22/17/18s)+3次过渡2.6s ≈ 65s ≈ 3900 帧
  const st = vm.runInContext('state', sandbox);
  const ci = vm.runInContext('curIdx', sandbox);
  ok(st === 'ending' && ci === 3, `自动游览到达终章 (state=${st}, curIdx=${ci})`);
  vm.runInContext('autoMode=false', sandbox);
} catch (e) { ok(false, '自动游览抛错: ' + e.message); }

console.log(`\n结果: ${pass} 通过, ${fail} 失败`);
process.exit(fail ? 1 : 0);
