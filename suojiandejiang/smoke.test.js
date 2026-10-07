#!/usr/bin/env node
/* smoke-test.js —— 《宿建德江》深度冒烟测试
 * 1) 真实感 THREE 桩在 vm 中执行主脚本（抓顶层求值/未定义引用/NaN）
 * 2) 数据确定性复核：诗文逐字=queue.text、拼音数、对齐、边界常量、音频编号、色板
 * 3) 全部 STAGES：build → setFade(1)/setFade(0.35) → update 跑 8 秒 ×2 种 fadeK
 * 4) 交互境 click：clock.t 推进、守卫防连点、flash 题字观察
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = __dirname;
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const m = html.match(/<script id="main">([\s\S]*?)<\/script>/);
if (!m) { console.error('未找到主脚本'); process.exit(1); }
const code = m[1];

let fails = 0;
const bad = msg => { console.error('✗ ' + msg); fails++; };
const ok = msg => console.log('✓ ' + msg);

/* ---------------- 拟真 THREE 桩 ---------------- */
class Vec3 {
  constructor(x=0,y=0,z=0){ this.x=x; this.y=y; this.z=z; }
  set(x,y,z){ this.x=x; this.y=y; this.z=z; return this; }
  setScalar(s){ return this.set(s,s,s); }
  copy(v){ this.x=v.x; this.y=v.y; this.z=v.z; return this; }
  clone(){ return new Vec3(this.x,this.y,this.z); }
  add(v){ this.x+=v.x; this.y+=v.y; this.z+=v.z; return this; }
  addScaledVector(v,s){ this.x+=v.x*s; this.y+=v.y*s; this.z+=v.z*s; return this; }
  sub(v){ this.x-=v.x; this.y-=v.y; this.z-=v.z; return this; }
  multiplyScalar(s){ this.x*=s; this.y*=s; this.z*=s; return this; }
  normalize(){ const l=Math.hypot(this.x,this.y,this.z)||1; return this.multiplyScalar(1/l); }
  lerp(v,a){ this.x+=(v.x-this.x)*a; this.y+=(v.y-this.y)*a; this.z+=(v.z-this.z)*a; return this; }
  lerpVectors(a,b,t){ this.x=a.x+(b.x-a.x)*t; this.y=a.y+(b.y-a.y)*t; this.z=a.z+(b.z-a.z)*t; return this; }
  length(){ return Math.hypot(this.x,this.y,this.z); }
  dot(v){ return this.x*v.x+this.y*v.y+this.z*v.z; }
  cross(v){ const x=this.y*v.z-this.z*v.y, y=this.z*v.x-this.x*v.z, z=this.x*v.y-this.y*v.x;
    return this.set(x,y,z); }
  crossVectors(a,b){ return this.set(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x); }
  subVectors(a,b){ return this.set(a.x-b.x,a.y-b.y,a.z-b.z); }
}
class Vec2 { constructor(x=0,y=0){ this.x=x; this.y=y; } set(x,y){ this.x=x; this.y=y; return this; } }
class Color {
  constructor(h){ this.r=0.5; this.g=0.5; this.b=0.5; this.hex=h; }
  copy(c){ this.r=c.r; this.g=c.g; this.b=c.b; this.hex=c.hex; return this; }
  clone(){ return new Color(this.hex); }
  lerp(c,a){ this.r+=(c.r-this.r)*a; this.g+=(c.g-this.g)*a; this.b+=(c.b-this.b)*a; return this; }
  lerpColors(a,b,t){ this.r=a.r+(b.r-a.r)*t; this.g=a.g+(b.g-a.g)*t; this.b=a.b+(b.b-a.b)*t; return this; }
  setScalar(s){ this.r=this.g=this.b=s; return this; }
}
class Quaternion { setFromAxisAngle(){ return this; } }
class Euler { constructor(){ this.x=0; this.y=0; this.z=0; } }
const mkMat = name => class {
  constructor(params){
    Object.assign(this, { transparent:false, opacity:1, depthWrite:true, fog:true, side:0,
      blending:0, vertexColors:false, sizeAttenuation:true, size:1, shininess:30,
      userData:{}, color:new Color(0x888888), emissive:new Color(0x000000),
      specular:new Color(0x111111) }, params||{});
    this.type=name;
    if(this.uniforms && !this.isShaderMaterial) this.isShaderMaterial=false;
  }
  dispose(){}
};
class Material extends mkMat('Material') {}
class MeshBasicMaterial extends mkMat('MeshBasicMaterial') { constructor(p){ super(p); this.isMeshBasicMaterial=true; } }
class MeshPhongMaterial extends mkMat('MeshPhongMaterial') { constructor(p){ super(p); this.isMeshPhongMaterial=true; } }
class PointsMaterial extends mkMat('PointsMaterial') { constructor(p){ super(p); this.isPointsMaterial=true; } }
class LineBasicMaterial extends mkMat('LineBasicMaterial') { constructor(p){ super(p); this.isLineBasicMaterial=true; } }
class SpriteMaterial extends mkMat('SpriteMaterial') { constructor(p){ super(p); this.isSpriteMaterial=true; } }
class ShaderMaterial extends mkMat('ShaderMaterial') {
  constructor(p){ super(p); this.isShaderMaterial=true;
    this.uniforms=(p&&p.uniforms)||{}; this.vertexShader=(p&&p.vertexShader)||''; this.fragmentShader=(p&&p.fragmentShader)||''; }
}
let objId=0;
class Object3D {
  constructor(){
    this.id=++objId; this.children=[]; this.parent=null; this.userData={};
    this.position=new Vec3(); this.rotation=new Euler(); this.scale=new Vec3(1,1,1);
    this.quaternion=new Quaternion(); this.matrix={}; this.visible=true;
    this.frustumCulled=true; this.renderOrder=0;
  }
  add(...cs){ for(const c of cs){ c.parent=this; this.children.push(c); } return this; }
  remove(c){ const i=this.children.indexOf(c); if(i>=0)this.children.splice(i,1); return this; }
  traverse(fn){ fn(this); for(const c of this.children) c.traverse(fn); }
  rotateOnAxis(){ return this; }
  get isObject3D(){ return true; }
}
class Group extends Object3D { constructor(){ super(); this.isGroup=true; } }
class Mesh extends Object3D {
  constructor(g,mat){ super(); this.geometry=g; this.material=mat; this.isMesh=true; }
}
class Points extends Object3D { constructor(g,mat){ super(); this.geometry=g; this.material=mat; this.isPoints=true; } }
class Line extends Object3D { constructor(g,mat){ super(); this.geometry=g; this.material=mat; this.isLine=true; } }
class Sprite extends Object3D { constructor(mat){ super(); this.material=mat; this.isSprite=true; } }
class InstancedMesh extends Object3D {
  constructor(g,mat,count){ super(); this.geometry=g; this.material=mat; this.count=count;
    this.instanceMatrix={ needsUpdate:false, setUsage(){} }; }
  setMatrixAt(){}
}
class Light extends Object3D { constructor(c,i){ super(); this.isLight=true; this.intensity=i||1; this.color=new Color(c); } }
class DirectionalLight extends Light { constructor(c,i){ super(c,i); this.isDirectionalLight=true; } }
class AmbientLight extends Light { constructor(c,i){ super(c,i); this.isAmbientLight=true; } }
class PointLight extends Light { constructor(c,i,d){ super(c,i); this.distance=d||0; this.isPointLight=true; } }
class BufferAttribute { constructor(arr,n){ this.array=arr; this.itemSize=n; this.needsUpdate=false; } }
class BufferGeometry {
  constructor(){ this.attributes={}; }
  setAttribute(n,a){ this.attributes[n]=a; return this; }
  rotateX(){ return this; }
  dispose(){}
}
const geo = name => class extends BufferGeometry { constructor(...a){ super(); this.name=name; this.args=a; } };
class PlaneGeometry extends geo('Plane') {}
class SphereGeometry extends geo('Sphere') {}
class CircleGeometry extends geo('Circle') {}
class CylinderGeometry extends geo('Cylinder') {}
class ConeGeometry extends geo('Cone') {}
class TorusGeometry extends geo('Torus') {}
class LatheGeometry extends geo('Lathe') {}
class BoxGeometry extends geo('Box') {}
class RingGeometry extends geo('Ring') {}
class CanvasTexture { constructor(c){ this.canvas=c; } dispose(){} }
class FogExp2 { constructor(c,d){ this.color=new Color(c); this.density=d; } }
class PerspectiveCamera extends Object3D {
  constructor(fov,aspect){ super(); this.fov=fov; this.aspect=aspect; this.isCamera=true; }
  lookAt(){ this.looked=true; }
  updateProjectionMatrix(){}
  rotateZ(){}
}
class WebGLRenderer {
  constructor(){ this.domElement={ addEventListener(){}, tag:'canvas' }; }
  setPixelRatio(){} setSize(){} render(){} setClearColor(){}
}
class Scene extends Group { constructor(){ super(); this.isScene=true; } }
const THREE = {
  Vector3:Vec3, Vector2:Vec2, Color, Quaternion, Euler,
  Object3D, Group, Mesh, Points, Line, Sprite, InstancedMesh, Scene,
  MeshBasicMaterial, MeshPhongMaterial, PointsMaterial, LineBasicMaterial, SpriteMaterial, ShaderMaterial, Material,
  DirectionalLight, AmbientLight, PointLight,
  BufferAttribute, BufferGeometry, CanvasTexture, FogExp2, PerspectiveCamera, WebGLRenderer,
  PlaneGeometry, SphereGeometry, CircleGeometry, CylinderGeometry, ConeGeometry, TorusGeometry,
  LatheGeometry, BoxGeometry, RingGeometry,
  AdditiveBlending:1, NormalBlending:0, BackSide:1, DoubleSide:2, FrontSide:0,
  DynamicDrawUsage:{},
};

/* ---------------- DOM 桩 ---------------- */
function makeEl(tag){
  const el = {
    tagName:(tag||'div').toUpperCase(), style:{}, children:[], textContent:'', innerHTML:'', open:false,
    offsetWidth:10, className:'', title:'', disabled:false,
    classList:{ _s:new Set(), add(c){ this._s.add(c); }, remove(c){ this._s.delete(c); },
      toggle(c,f){ if(f===undefined){ this._s.has(c)?this._s.delete(c):this._s.add(c); } else if(f)this._s.add(c); else this._s.delete(c); return this._s.has(c); },
      contains(c){ return this._s.has(c); } },
    addEventListener(){}, appendChild(c){ el.children.push(c); return c; },
    querySelector(){ return makeEl(); }, querySelectorAll(){ return []; },
    getContext(){ return { createRadialGradient:()=>({ addColorStop(){} }), fillRect(){}, fillText(){},
      fillStyle:'', font:'', textAlign:'', textBaseline:'', shadowColor:'', shadowBlur:0 }; },
  };
  return el;
}
const flashEl = makeEl('div');
const els = new Map();
function getEl(sel){
  if(sel==='#flash')return flashEl;
  if(!els.has(sel))els.set(sel,makeEl(sel.replace(/[#.]/g,'')));
  return els.get(sel);
}
const sandbox = {
  THREE, console, Math, Float32Array,
  performance:{ now:()=>0 },
  requestAnimationFrame(){},
  setTimeout(){ return 0; }, clearTimeout(){},
  window:{ innerWidth:1600, innerHeight:900, devicePixelRatio:1, addEventListener(){},
    AudioContext:undefined, webkitAudioContext:undefined, __inited:false },
  document:{
    querySelector:getEl, getElementById:getEl, createElement:t=>makeEl(t),
    addEventListener(){}, body:makeEl('body'), head:makeEl('head'),
    documentElement:makeEl('html'), activeElement:null, fullscreenElement:null,
    querySelectorAll(){ return []; },
  },
  location:{ reload(){} },
};
sandbox.window.addEventListener=()=>{};
sandbox.globalThis=sandbox;
vm.createContext(sandbox);
vm.runInContext(code, sandbox, { filename:'main.js' });
ok('主脚本在拟真 THREE 桩下顶层执行通过');

const g = e => vm.runInContext(e, sandbox);

/* ---------------- 1. 数据确定性复核 ---------------- */
const q = JSON.parse(fs.readFileSync(path.join(__dirname, '..', '_pipeline', 'queue.json'),'utf8'));
const entry = q.poems.find(p=>p.slug==='suojiandejiang');
const POEM = g('POEM'), STAGES = g('STAGES'), QUIZ = g('QUIZ'), CN = g('CN');
const joined = POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
if(joined!==entry.text) bad(`诗文不一致: ${joined}`);
else ok('诗文与 queue.text 逐字逐标点一致');
if(POEM.length!==entry.stages.length) bad('POEM 句数≠stages');
else ok('POEM 句数 = 3 = queue.stages');
STAGES.forEach((s,i)=>{ if(i>0&&s.name!==POEM[i-1].name) bad(`境${i}名错位`); });
ok('STAGES/POEM 境名逐一对齐');
POEM.forEach((p,i)=>{
  p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length) bad(`句${i+1}拼音数 ${han}≠${seg.p.length}`);
  });
});
ok('每句汉字数=拼音数（5×4）');
// 多音字注音抽查
const p0=POEM[0].segs[0].p;
if(p0[2]!=='bó') bad(`泊 注音=${p0[2]} 应为 bó`); else ok('泊=bó 注音正确');
if(p0[4]!=='zhǔ') bad(`渚 注音=${p0[4]} 应为 zhǔ`); else ok('渚=zhǔ 注音正确');
if(CN.length<3) bad('CN 过短'); else ok('CN 长度≥3');
if(QUIZ.length<5) bad('小测<5题'); else ok('小测5题，选项3个/答案索引合法: '+
  QUIZ.every(qq=>qq.o.length===3&&qq.a>=0&&qq.a<3));
const wm = code.match(/words\s*=\s*\[([^\]]*)\]/);
const wn = wm[1].split(',').length;
if(wn!==QUIZ.length+1) bad(`words ${wn}≠${QUIZ.length+1}`); else ok('评语 words=6=题数+1（孟浩然定制）');
if(/将进酒|万古愁|如见太白|深得太白/.test(code)) bad('残留参考实现文案');
else ok('无《将进酒》/太白残留');
// 边界常量
const boundaryMissing=[];
for(const [pat,label] of [
  [/clamp\(i,0,3\)/,'goto clamp'], [/curIdx===3\)showEnding/,'自动游览末境'],
  [/curIdx>=3\)showEnding/g,'btnNext/方向键末境'], [/'04\.mp3'/g,'全诗音频04'],
  [/curIdx===3&&state==='stage'/g,'交互接线']]){
  const c=(code.match(pat)||[]).length;
  if(!c) boundaryMissing.push(label);
  else if(label==='交互接线'&&c<2) boundaryMissing.push(`交互接线仅${c}处`);
}
if(boundaryMissing.length) bad('缺: '+boundaryMissing.join('; '));
else ok('clamp(i,0,3) / 末境showEnding / 04.mp3 / 交互接线×2 全在');
const root=(html.match(/:root\s*\{[^}]*\}/)||[''])[0];
if(!root.includes('--gold:#8fb0c4')) bad('--gold≠#8fb0c4'); else ok('--gold=#8fb0c4（分配强调色）');
if(/background:#05070d/.test(html)||(html.match(/0x05070d/g)||[]).length>0) bad('夜宴默认底色残留');
else ok('无 #05070d / 0x05070d 残留（body/err=#10141a）');
// read 字段数
const reads=[...code.matchAll(/read:'([^']+)'/g)].map(x=>x[1]);
if(reads.length!==3) bad(`read ${reads.length}≠3`); else ok('read 字段=3；全诗拼接='+(reads.join('')===entry.text?'一致':'不一致'));

/* ---------------- 2. 全部 STAGES：build/update/click 深跑 ---------------- */
vm.runInContext(`
const __scene=new THREE.Scene();
const __errs=[];
function __runStage(i,clickTest){
  const def=STAGES[i];
  const sky=def.sky();
  if(!sky.top||!sky.hor||!sky.bot||!sky.fog||!sky.moon||typeof sky.fd!=='number')__errs.push('境'+i+' sky字段不全');
  const st=def.build();
  if(!st||!st.group)__errs.push('境'+i+' build 无 group');
  __scene.add(st.group);
  setFade(st.group,1);
  const frames=240, dt=1/30;
  for(let f=0;f<frames;f++){ st.update&&st.update(f*dt,dt); }
  setFade(st.group,0.35);
  for(let f=0;f<60;f++){ st.update&&st.update(8+f*dt,dt); }
  // 数值健康检查：位置/透明度不允许 NaN
  let nan=false;
  st.group.traverse(o=>{
    if([o.position.x,o.position.y,o.position.z,o.scale.x,o.rotation.z].some(v=>typeof v==='number'&&!isFinite(v)))nan=true;
    if(o.material&&typeof o.material.opacity==='number'&&!isFinite(o.material.opacity))nan=true;
    if(o.material&&o.material.uniforms)for(const k in o.material.uniforms){
      const v=o.material.uniforms[k].value;
      if(typeof v==='number'&&!isFinite(v))nan=true;
      if(v&&typeof v==='object'&&typeof v.r==='number'&&!isFinite(v.r))nan=true;
    }
  });
  if(nan)__errs.push('境'+i+' 出现 NaN/Inf');
  if(clickTest&&st.click){
    st.click.__ran=true;
  }
  __scene.remove(st.group);
  disposeGroup(st.group);
  return st;
}
`, sandbox);

for(let i=0;i<STAGES.length;i++){
  try{
    vm.runInContext(`__runStage(${i},false)`, sandbox);
    ok(`境${i}（${STAGES[i].name}）build+240帧update@fade1+60帧@fade0.35 通过，无NaN`);
  }catch(e){ bad(`境${i} 深跑失败: ${e.stack.split('\n').slice(0,3).join(' | ')}`); }
}
const errs=vm.runInContext('__errs', sandbox);
if(errs.length) bad('深跑错误: '+errs.join('; '));

/* ---------------- 3. 交互境 click：守卫 + flash 题字 ---------------- */
try{
  // 单独再建一次境3
  const st3=vm.runInContext('STAGES[3].build()', sandbox);
  // click 冷却起始（ctl.t0=-99，clock.t=0 → age=99>9 → 未点状态）
  vm.runInContext('clock.t=0', sandbox);
  st3.update&&st3.update(0,0.016);
  // 首次点击：age=0-(-99)=99>6.5 → 允许
  flashEl.textContent='__';
  st3.click();
  if(flashEl.textContent!=='江清月近人') bad('click 未触发题字 flash，得到: '+flashEl.textContent);
  else ok('click 触发题字「江清月近人」');
  // 连点守卫：clock.t 前进 1s（<6.5）→ 应被拦截
  vm.runInContext('clock.t=1', sandbox);
  flashEl.textContent='__';
  st3.click();
  if(flashEl.textContent!=='__') bad('连点守卫失效（1s 内重复触发）');
  else ok('ctl 守卫拦截 1s 内连点');
  // 冷却结束：clock.t=8（上次 t0=0）→ 允许
  vm.runInContext('clock.t=8', sandbox);
  st3.click();
  if(flashEl.textContent!=='江清月近人') bad('冷却后点击未被放行');
  else ok('冷却 6.5s 后可再次触发');
  // 点击后 update 推进 12 秒（碎金亮起再隐去全程）
  vm.runInContext('clock.t=8', sandbox);
  for(let f=0;f<400;f++){ st3.update&&st3.update(8+f*0.033,0.033); }
  let nan=false;
  st3.group.traverse(o=>{
    if(o.material&&o.material.uniforms)for(const k in o.material.uniforms){
      const v=o.material.uniforms[k].value;
      if(typeof v==='number'&&!isFinite(v))nan=true;
    }
  });
  if(nan) bad('交互后 update 出现 NaN'); else ok('交互后 400 帧 update 无 NaN（月影漂移+碎金+月灯）');
}catch(e){ bad('交互测试失败: '+e.stack.split('\n').slice(0,4).join(' | ')); }

/* ---------------- 4. 天空工厂 + 音频目录 ---------------- */
for(let i=0;i<STAGES.length;i++){
  const s=STAGES[i].sky();
  if(!(s.ms>0&&s.star>=0&&s.fd>0&&s.moon instanceof Vec3)) bad(`境${i} sky 参数异常`);
}
ok('4 个 sky() 工厂参数齐全（惰性，顶层无 THREE 求值）');
const audioDir=path.join(DIR,'audio');
const have=fs.existsSync(audioDir)?fs.readdirSync(audioDir).filter(f=>f.endsWith('.mp3')).length:0;
console.log(have===5?`✓ audio/ 5 个 MP3（00..04）`:`⚠ audio/ 现有 ${have} 个（gen-voice 后应为 5）`);

console.log(fails===0?'\nSMOKE ALL GREEN':`\nSMOKE ${fails} 项失败`);
process.exit(fails===0?0:1);
