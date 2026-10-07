#!/usr/bin/env node
/* smoke.test.js —— 大林寺桃花 深度冒烟测试
 * 用「可运算的真实 THREE 桩」在 Node 里跑 index.html 主脚本：
 *   boot() → 逐境 goto(+settle 动画) → 每境 build/update/click/onEnter
 *   → 交互境（第三境）登山点击链路 → 末境 showEnding → 小测渲染 → 回封面
 * validate.js 只查顶层结构，抓不到 builder 内部错误（未定义函数、undefined 属性链等），
 * 本脚本补上这一层。用法: node smoke.test.js
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const file = path.join(__dirname, 'index.html');
const html = fs.readFileSync(file, 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
const N = 3; // 诗句数

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
}
class Euler { constructor(x = 0, y = 0, z = 0) { this.x = x; this.y = y; this.z = z; } set(x, y, z) { this.x = x; this.y = y; this.z = z; return this; } }
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
class GeoBase { dispose() {} rotateX() { return this; } rotateY() { return this; } }
class PlaneGeometry extends GeoBase { constructor(...a) { super(); this.args = a; } }
class SphereGeometry extends GeoBase { }
class ConeGeometry extends GeoBase { }
class CylinderGeometry extends GeoBase { }
class BoxGeometry extends GeoBase { }
class CircleGeometry extends GeoBase { }
class LatheGeometry extends GeoBase { constructor(pts) { super(); this.points = pts; } }
class TorusGeometry extends GeoBase { }
class RingGeometry extends GeoBase { }
class BufferGeometry extends GeoBase {
  constructor() { super(); this.attributes = {}; }
  setAttribute(name, attr) { this.attributes[name] = attr; return this; }
  setFromPoints(pts) { this.points = pts; return this; }
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
  LatheGeometry, TorusGeometry, RingGeometry, BufferGeometry, BufferAttribute,
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
sandbox.AudioContext = function () { throw new Error('no audio in stub'); };
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
ok(poemLen === N, `POEM 有 ${N} 句 (实际 ${poemLen})`);
ok(stagesLen === N + 1, `STAGES = 封面+${N} = ${N + 1} (实际 ${stagesLen})`);
const align = vm.runInContext(`POEM.every((p,i)=>STAGES[i+1].name===p.name)`, sandbox);
ok(align, 'STAGES[i].name === POEM[i-1].name 逐一对齐');
const joined = vm.runInContext(`POEM.map(l=>l.segs.map(s=>s.c).join('')).join('')`, sandbox);
const TEXT = '人间四月芳菲尽，山寺桃花始盛开。长恨春归无觅处，不知转入此中来。';
ok(joined === TEXT, '各境 segs 拼接 === 队列 text 原文（含标点）');
const pyOK = vm.runInContext(`POEM.every(l=>l.segs.every(s=>[...s.c].filter(c=>!/[,，。、！？；：…—·]/.test(c)).length===s.p.length))`, sandbox);
ok(pyOK, '每句汉字数 = 拼音数');
const wordsN = (code.match(/words\s*=\s*\[([^\]]*)\]/) || ['', ''])[1].split(',').length;
ok(wordsN === N + 3, `小测评语 words 为 ${N + 3} 项 (实际 ${wordsN})`);
ok(!/太白/.test(code), '小测评语无太白残留');

console.log('== 3. boot() ==');
try { vm.runInContext('boot()', sandbox); ok(true, 'boot() 完成（渲染器/天空/封面境）'); }
catch (e) { ok(false, 'boot() 抛错: ' + e.stack); }

const settle = n => vm.runInContext(`for(let _i=0;_i<${n};_i++)animate();`, sandbox);

console.log('== 4. 逐境 goto + 动画走完 ==');
for (let i = 1; i <= N; i++) {
  try {
    vm.runInContext(`goto(${i})`, sandbox);
    settle(220); // 220×16.7ms ≈ 3.7s > 2.6s 过渡
    const cur = vm.runInContext('curIdx', sandbox);
    const state = vm.runInContext('state', sandbox);
    ok(cur === i && state === 'stage', `第${i}境 goto 完成 (curIdx=${cur}, state=${state})`);
  } catch (e) { ok(false, `第${i}境 goto 抛错: ` + e.stack); }
}

console.log('== 5. 每境 builder 深跑：build/update 多帧/click/onEnter/sky ==');
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
    if(st.click){ st.click(); st.click(); } // 冷却守卫 + 防连点
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
  ok(true, `全部 ${N + 1} 境 build/update(t×8 帧)/click/onEnter/sky() 通过 (${r})`);
} catch (e) { ok(false, 'builder 深跑抛错: ' + e.message + '\n' + (e.stack || '').split('\n').slice(0, 4).join('\n')); }

console.log('== 6. 交互境（第三境）登山点击链路 ==');
try {
  vm.runInContext(`goto(3)`, sandbox); settle(220);
  const before = vm.runInContext('curStageObj.group.position.y', sandbox);
  vm.runInContext(`curStageObj.click()`, sandbox);           // 触发登山
  const guard = vm.runInContext(`(curStageObj.click(), true)`, sandbox); // 防连点：再点应被忽略
  settle(650); // ≈10.9s：登顶动画 10s 走完
  const after = vm.runInContext('curStageObj.group.position.y', sandbox);
  const done = vm.runInContext('JSON.stringify({k:curStageObj.ctl?curStageObj.ctl.k:1,rot:curStageObj.group.rotation.y})', sandbox);
  ok(guard && Math.abs(after - before) > 30, `点击登山：group 下移 ${before.toFixed(1)}→${after.toFixed(1)}（镜头上山）`);
  ok(Math.abs(vm.runInContext('curStageObj.group.rotation.y', sandbox) - Math.PI * 2) < 0.01, '盘旋一整圈后山门朝向镜头 (rotation.y≈2π)');
  settle(120);
} catch (e) { ok(false, '交互境 click 抛错: ' + e.message + '\n' + (e.stack || '').split('\n').slice(0, 4).join('\n')); }

console.log('== 7. 末境 / 终章 / 小测 ==');
try {
  vm.runInContext(`goto(3); for(let _i=0;_i<3;_i++)animate(); showEnding();`, sandbox);
  ok(vm.runInContext('state', sandbox) === 'ending', 'showEnding() 进入终章态');
  vm.runInContext(`startQuiz(); renderQuiz(); showResult();`, sandbox);
  ok(true, '小测渲染 + 结果页通过');
  vm.runInContext(`$('#quiz').classList.remove('show'); hideEnding('cover');`, sandbox);
  settle(10);
  ok(vm.runInContext('curIdx', sandbox) === 0, '回到封面');
} catch (e) { ok(false, '终章/小测抛错: ' + e.message); }

console.log('== 8. 越界钳制 ==');
try {
  vm.runInContext(`goto(0)`, sandbox); settle(220);
  ok(vm.runInContext('curIdx', sandbox) === 0 && vm.runInContext('state', sandbox) === 'stage', '回到封面并稳定');
  vm.runInContext(`goto(99)`, sandbox); settle(220);
  ok(vm.runInContext('curIdx', sandbox) === N, `goto(99) 钳制到 ${N}`);
} catch (e) { ok(false, '越界钳制抛错: ' + e.message); }

console.log(`\n结果: ${pass} 通过, ${fail} 失败`);
process.exit(fail ? 1 : 0);
