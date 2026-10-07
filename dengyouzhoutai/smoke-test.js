#!/usr/bin/env node
/* smoke-test.js —— 《登幽州台歌》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、3 境 build()/update()×300帧/click、境一淡影消散、
 * 境二点击极速拉远 camHook + 连点守卫、mixSky、setFade/disposeGroup、
 * goto() 集成路径、showEnding、小测。
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

console.log('[3] 场景冒烟：buildSky + 3 境 build/update/click/camHook + goto/showEnding …');
const harness = `
;(function(){
  const out=[];
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='前不见古人，后不见来者。念天地之悠悠，独怆然而涕下。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==3)throw new Error('STAGES 应为 3（封面+2境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 注音数量逐句核对（含多音字）——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  if(!POEM[0].segs[0].p[1].startsWith('bú'))throw new Error('不见 应读 bú jiàn');
  if(!POEM[0].segs[1].p[1].startsWith('bú'))throw new Error('不见 应读 bú jiàn');
  if(!POEM[1].segs[1].p[1].startsWith('chuàng'))throw new Error('怆 应读 chuàng');
  if(!POEM[1].segs[1].p[4].startsWith('tì'))throw new Error('涕 应读 tì');
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x1a120a,0.006);
  camera=new THREE.PerspectiveCamera(55,16/9,0.1,1500);
  curLook=new THREE.Vector3();
  buildSky();
  SKYcur=cloneSky(STAGES[0].sky());
  applySky();
  const dt=0.05;
  // —— 逐境深测 ——
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
      if(obj.update)obj.update(stageT,dt);
      const p=Math.min(1,stageT/30);
      camera.position.set(
        def.cam.f[0]+(def.cam.t[0]-def.cam.f[0])*p,
        def.cam.f[1]+(def.cam.t[1]-def.cam.f[1])*p,
        def.cam.f[2]+(def.cam.t[2]-def.cam.f[2])*p);
      curLook.set(def.cam.lf[0],def.cam.lf[1],def.cam.lf[2]);
      camera.lookAt(curLook);
      if(obj.camHook)obj.camHook(clock.t);
      applySky();
    }
    if(obj.onEnter)obj.onEnter();
    if(obj.click){
      obj.click(); for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(obj.update)obj.update(stageT,dt);}
      obj.click(); for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(obj.update)obj.update(stageT,dt);}
    }
    // 天空插值（前后境混合）
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1);
    SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group);
    scene.remove(obj.group);
    out.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  // —— 境一专项：前后淡影「隐现而散尽」 ——
  const s1=STAGES[1].build(); scene.add(s1.group); setFade(s1.group,1); s1.group.userData.fadeK=1;
  const ghostMats=[];
  s1.group.traverse(o=>{ if(o.isMesh&&o.material&&o.material.userData&&o.material.userData.o0===0.35&&!ghostMats.includes(o.material))ghostMats.push(o.material); });
  if(ghostMats.length!==6)throw new Error('应有 6 处前后淡影，实际 '+ghostMats.length);
  stageT=0;
  for(let f=0;f<60;f++){stageT+=dt; if(s1.update)s1.update(stageT,dt);}
  const early=Math.max(...ghostMats.map(m=>m.opacity));
  if(early<0.05)throw new Error('淡影未隐现: maxOpacity='+early.toFixed(3));
  for(let f=0;f<280;f++){stageT+=dt; if(s1.update)s1.update(stageT,dt);}
  const late=Math.max(...ghostMats.map(m=>m.opacity));
  if(late>0.08)throw new Error('淡影未散尽（应"不见"）: maxOpacity='+late.toFixed(3));
  out.push('境一 淡影 隐现 '+early.toFixed(2)+' → 散尽 '+late.toFixed(2)+' [OK]');
  disposeGroup(s1.group); scene.remove(s1.group);
  // —— 境二专项：点击极速拉远 + 连点守卫 ——
  const s2=STAGES[2].build(); scene.add(s2.group); setFade(s2.group,1); s2.group.userData.fadeK=1;
  stageT=0; clock.t=100;
  for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt; if(s2.update)s2.update(stageT,dt);}
  const before=camera.position.clone();
  s2.click(); s2.click(); s2.click(); // 三连点：仅首发生效（守卫）
  for(let f=0;f<80;f++){stageT+=dt;clock.t+=dt; if(s2.update)s2.update(stageT,dt); if(s2.camHook)s2.camHook(clock.t);}
  const dZoom=camera.position.distanceTo(new THREE.Vector3(0,96,332));
  if(dZoom>1.5)throw new Error('点击后镜头未拉远至天地尽头: 距目标 '+dZoom.toFixed(1));
  if(camera.position.distanceTo(before)<50)throw new Error('镜头几乎未动');
  s2.click(); // 守卫后再点：不得重置/报错，镜头保持天地尽头
  for(let f=0;f<30;f++){stageT+=dt;clock.t+=dt; if(s2.update)s2.update(stageT,dt); if(s2.camHook)s2.camHook(clock.t);}
  const dAgain=camera.position.distanceTo(new THREE.Vector3(0,96,332));
  if(dAgain>1.5)throw new Error('连点后镜头异常: 距目标 '+dAgain.toFixed(1));
  const pls=[]; s2.group.traverse(o=>{ if(o.isLight&&o.isPointLight)pls.push(o); });
  if(pls.length!==1||pls[0].intensity<=0)throw new Error('境二点光未生效');
  if(pls[0].intensity>1.2)throw new Error('点光强度异常（应受 fadeK 约束）: '+pls[0].intensity);
  out.push('境二 click×3 → 拉远 ('+camera.position.x.toFixed(0)+','+camera.position.y.toFixed(0)+','+camera.position.z.toFixed(0)+') 守卫+点光 '+pls[0].intensity.toFixed(2)+' [OK]');
  disposeGroup(s2.group); scene.remove(s2.group);
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
  console.log('  ✓ goto×2 + showEnding + quiz [OK]');
}
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/camHook/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
