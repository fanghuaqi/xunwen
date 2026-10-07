#!/usr/bin/env node
/* smoke-test.js —— 《西江月·夜行黄沙道中》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、5 境（含封面）build()/update()×300帧、行走相机、mixSky、
 * setFade/disposeGroup、goto() 集成路径、showEnding()、惊鹊起飞、茅店忽现、
 * 互动蛙声涟漪与冷却守卫专项校验。
 * 用法: node smoke-test.js   （退出码 0 = 全部通过）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = __dirname;
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
const threePath = path.join(DIR, 'three.min.js');
if (!fs.existsSync(threePath)) {
  console.log('three.min.js 不存在，从 jsdelivr 下载 …');
  fs.writeFileSync(threePath, Buffer.from(
    require('child_process').execSync(
      'curl -sL --max-time 90 https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js')));
}
const threeSrc = fs.readFileSync(threePath, 'utf8');
if (!/THREE/.test(threeSrc) || threeSrc.length < 100000) {
  console.error('three.min.js 下载不完整'); process.exit(1);
}

/* ---------- DOM 桩 ---------- */
function ctx2d() {
  return { createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {},
    fillStyle: '', font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0 };
}
function elStub(tag) {
  const el = {
    tag, children: [], style: {}, textContent: '', innerHTML: '', className: '', id: '', open: false,
    addEventListener() {}, removeEventListener() {}, appendChild(c) { el.children.push(c); return c; },
    querySelectorAll() { return []; }, querySelector() { return elStub('x'); },
    classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
    offsetWidth: 0, disabled: false, title: '',
  };
  return el;
}
const doc = {
  querySelector: () => elStub('q'), querySelectorAll: () => [],
  createElement: tag => tag === 'canvas'
    ? Object.assign(elStub('canvas'), { width: 64, height: 64, getContext: () => ctx2d() })
    : elStub(tag),
  addEventListener() {}, documentElement: elStub('html'), body: elStub('body'),
  head: elStub('head'), activeElement: null, fullscreenElement: null,
};
const sandbox = {
  document: doc, console,
  performance: { now: () => Date.now() },
  requestAnimationFrame() { return 0; },
  setTimeout() { return 0; }, clearTimeout() {},
  location: { reload() {} }, navigator: { userAgent: 'node' },
};
sandbox.window = sandbox;
sandbox.self = sandbox;
sandbox.globalThis = sandbox;
vm.createContext(sandbox);

let fails = 0;
const run = (src, name) => {
  try { vm.runInContext(src, sandbox, { filename: name }); return true; }
  catch (e) { console.error('  ✗ ' + name + ': ' + (e && e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e)); fails++; return false; }
};

console.log('[1] 加载 THREE r128 …');
if (!run(threeSrc, 'three.min.js')) process.exit(1);
if (!run('if(!window.THREE)throw new Error("THREE 未挂载"); window.__T="r128"', 'check THREE')) process.exit(1);

console.log('[2] 执行主脚本顶层 …');
if (!run(code, 'main')) process.exit(1);

console.log('[3] 场景冒烟：buildSky + 5 境 build/update/行走相机 + click/goto/showEnding …');
const harness = `
;(function(){
  const out=[];
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='明月别枝惊鹊，清风半夜鸣蝉。稻花香里说丰年，听取蛙声一片。七八个星天外，两三点雨山前。旧时茅店社林边，路转溪桥忽见。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==5)throw new Error('STAGES 应为 5（封面+4境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 注音数量逐句核对 + 多音字 ——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  if(POEM[0].segs[1].p[5]!=='chán')throw new Error('蝉 应读 chán');
  if(POEM[3].segs[1].p[5]!=='xiàn')throw new Error('见(忽见) 应读 xiàn');
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x0d1f17,0.006);
  camera=new THREE.PerspectiveCamera(55,16/9,0.1,1500);
  curLook=new THREE.Vector3();
  buildSky();
  SKYcur=cloneSky(STAGES[0].sky());
  applySky();
  const dt=0.05;
  // —— 逐境深测（含行走相机） ——
  for(let i=0;i<STAGES.length;i++){
    const def=STAGES[i];
    const obj=def.build();
    scene.add(obj.group);
    setFade(obj.group,1);
    obj.group.userData.fadeK=1;
    let meshes=0,lights=0,points=0;
    obj.group.traverse(o=>{ if(o.isMesh)meshes++; if(o.isPoints)points++; if(o.isLight)lights++; });
    for(let f=0;f<300;f++){
      stageT+=dt; clock.t+=dt;
      if(obj.update)obj.update(stageT,dt,obj.group.userData.fadeK);
      const p=Math.min(1,stageT/30);
      camera.position.set(
        def.cam.f[0]+(def.cam.t[0]-def.cam.f[0])*p,
        def.cam.f[1]+(def.cam.t[1]-def.cam.f[1])*p,
        def.cam.f[2]+(def.cam.t[2]-def.cam.f[2])*p);
      curLook.set(def.cam.lf[0],def.cam.lf[1],def.cam.lf[2]);
      camera.lookAt(curLook);
      applySky();
    }
    if(obj.onEnter)obj.onEnter();
    if(obj.click){
      obj.click(); for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(obj.update)obj.update(stageT,dt,1);}
      obj.click(); for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(obj.update)obj.update(stageT,dt,1);}
    }
    // 天空插值（前后境混合）
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1);
    SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group);
    scene.remove(obj.group);
    out.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  // —— 境1 专项：惊鹊栖枝→月下惊起 ——
  stageT=0;
  const s1=STAGES[1].build(); scene.add(s1.group); setFade(s1.group,1); s1.group.userData.fadeK=1;
  let magpie=null;
  s1.group.traverse(o=>{ if(o.name==='magpie')magpie=o; });
  if(!magpie)throw new Error('未找到惊鹊');
  for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(s1.update)s1.update(stageT,dt,1);}   // 2s：仍栖枝头
  const yPerch=magpie.position.y;
  for(let f=0;f<140;f++){stageT+=dt;clock.t+=dt; if(s1.update)s1.update(stageT,dt,1);}   // 至 9s：已惊起
  if(!(magpie.position.y>yPerch+8))throw new Error('惊鹊未起飞: y='+magpie.position.y.toFixed(1)+' (栖 '+yPerch.toFixed(1)+')');
  out.push('境1 惊鹊 y '+yPerch.toFixed(1)+'→'+magpie.position.y.toFixed(1)+' 月下掠去 [OK]');
  disposeGroup(s1.group); scene.remove(s1.group);
  // —— 境4 专项：茅店忽现 + 蛙声涟漪互动 + 冷却守卫 ——
  stageT=0;
  const s4=STAGES[4].build(); scene.add(s4.group); setFade(s4.group,1); s4.group.userData.fadeK=1;
  let innG=null;
  s4.group.traverse(o=>{ if(o.name==='innGroup')innG=o; });
  if(!innG)throw new Error('未找到茅店组');
  if(innG.visible)throw new Error('茅店不应一开始就可见');
  let rings=[];
  const collectRings=()=>{ rings=[]; s4.group.traverse(o=>{ if(o.isMesh&&o.geometry&&o.geometry.type==='RingGeometry')rings.push(o); }); };
  collectRings();
  if(rings.length!==10)throw new Error('涟漪池应 10 环，实际 '+rings.length);
  // 前 11s：桥上行走，茅店未现，偶发涟漪
  for(let f=0;f<220;f++){stageT+=dt;clock.t+=dt; if(s4.update)s4.update(stageT,dt,1);}
  if(innG.visible)throw new Error('茅店出现过早（应约 11.2s 转过桥才忽见）');
  // 忽现
  for(let f=0;f<50;f++){stageT+=dt;clock.t+=dt; if(s4.update)s4.update(stageT,dt,1);}   // 至 13.5s
  if(!innG.visible)throw new Error('茅店未忽现');
  if(!(innG.scale.x>0.99))throw new Error('茅店呈现动画未完成: scale='+innG.scale.x.toFixed(2));
  out.push('境4 茅店 11.2s 忽现 scale='+innG.scale.x.toFixed(2)+' [OK]');
  // 点击 → 声波齐荡（7 环以上被激活）
  collectRings();
  const visibleRings=()=>rings.filter(r=>r.visible&&r.material.opacity>0.05).length;
  const a0=frogCtl.accepts;
  s4.click();
  if(frogCtl.accepts!==a0+1)throw new Error('click 未生效');
  s4.click();  // 立即连点 → 冷却守卫拦截
  if(frogCtl.accepts!==a0+1)throw new Error('冷却守卫失效: 连点被接受');
  for(let f=0;f<24;f++){stageT+=dt;clock.t+=dt; if(s4.update)s4.update(stageT,dt,1);}   // 1.2s：7 环均在荡
  const vAfterClick=visibleRings();
  if(vAfterClick<5)throw new Error('点击后声波涟漪未齐荡: visible='+vAfterClick);
  // 冷却过后再点
  for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(s4.update)s4.update(stageT,dt,1);}
  s4.click();
  if(frogCtl.accepts!==a0+2)throw Error('冷却后点击应生效');
  for(let f=0;f<24;f++){stageT+=dt;clock.t+=dt; if(s4.update)s4.update(stageT,dt,1);}
  if(visibleRings()<5)throw new Error('二次点击涟漪未荡开: visible='+visibleRings());
  out.push('境4 click×3（1 拦截）→ 涟漪 visible='+vAfterClick+' 环齐荡 [OK]');
  disposeGroup(s4.group); scene.remove(s4.group);
  // —— goto() 集成路径 ——
  for(let i=1;i<STAGES.length;i++){ goto(i); state='stage'; }
  // —— 终章 ——
  showEnding(); state='stage';
  // —— 小测逻辑 ——
  startQuiz(); qIdx=QUIZ.length-1; renderQuiz(); showResult();
  window.__SMOKE=out.join('\\n');
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__SMOKE).split('\n').map(l => '  ✓ ' + l).join('\n'));
  console.log('  ✓ goto×4 + showEnding + quiz [OK]');
}
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
