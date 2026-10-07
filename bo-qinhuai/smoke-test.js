#!/usr/bin/env node
/* smoke-test.js —— 《泊秦淮》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、4 境 build()/update()×300帧/click×2、
 * 涟漪触发与连点守卫、goto() 集成路径、mixSky、setFade/disposeGroup、showEnding()、小测。
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
  console.error('three.min.js 不完整'); process.exit(1);
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

console.log('[3] 场景冒烟：buildSky + 4 境 build/update/click + 涟漪 + goto/showEnding …');
const harness = `
;(function(){
  const out=[];
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='烟笼寒水月笼沙，夜泊秦淮近酒家。商女不知亡国恨，隔江犹唱后庭花。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==4)throw new Error('STAGES 应为 4（封面+3境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位@'+i);
  POEM.forEach(l=>l.segs.forEach(s=>{ const han=[...s.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==s.p.length)throw new Error('拼音数不符: '+s.c); }));
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x141b24,0.0085);
  camera=new THREE.PerspectiveCamera(55,16/9,0.1,1500);
  curLook=new THREE.Vector3();
  buildSky();
  SKYcur=cloneSky(STAGES[0].sky());
  applySky();
  const dt=0.05;
  let ringMeshes=0;
  // —— 逐境深测 ——
  for(let i=0;i<STAGES.length;i++){
    const def=STAGES[i];
    const obj=def.build();
    scene.add(obj.group);
    setFade(obj.group,1);
    obj.group.userData.fadeK=1;
    let meshes=0,lights=0,points=0;
    obj.group.traverse(o=>{ if(o.isMesh)meshes++; if(o.isPoints)points++; if(o.isLight)lights++;
      if(o.geometry&&o.geometry.type==='RingGeometry')ringMeshes++; });
    for(let f=0;f<300;f++){
      clock.t+=dt; stageT+=dt;
      if(obj.update)obj.update(stageT,dt);
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
      obj.click(); for(let f=0;f<40;f++){clock.t+=dt; stageT+=dt; if(obj.update)obj.update(stageT,dt);}
      obj.click(); for(let f=0;f<40;f++){clock.t+=dt; stageT+=dt; if(obj.update)obj.update(stageT,dt);}
    }
    // 天空插值（前后境混合）
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1);
    SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group);
    scene.remove(obj.group);
    out.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  if(ringMeshes<12)throw new Error('声波涟漪 RingGeometry 少于 12: '+ringMeshes);
  out.push('涟漪环 '+ringMeshes+' 只 [OK]');
  // —— 交互境专项：click 触发涟漪 + 连点守卫 ——
  const cl=STAGES[3].build(); scene.add(cl.group); setFade(cl.group,1); cl.group.userData.fadeK=1;
  let vis0=0; cl.group.traverse(o=>{ if(o.geometry&&o.geometry.type==='RingGeometry'&&o.visible)vis0++; });
  if(vis0!==0)throw new Error('未点击时涟漪不应可见: '+vis0);
  for(let f=0;f<120;f++){clock.t+=dt; stageT+=dt; if(cl.update)cl.update(stageT,dt);}
  cl.click();
  const last1=songCtl.last;
  cl.click();                                    // 立刻连点：应被守卫拒绝
  if(songCtl.last!==last1)throw new Error('连点守卫失效');
  let vis1=0;
  for(let f=0;f<50;f++){clock.t+=dt; stageT+=dt; if(cl.update)cl.update(stageT,dt);
    if(f===10){ cl.group.traverse(o=>{ if(o.geometry&&o.geometry.type==='RingGeometry'&&o.visible)vis1++; }); } }
  if(vis1<1)throw new Error('click 后涟漪未出现');
  out.push('click → 涟漪可见 '+vis1+' 环 · 连点守卫 [OK]');
  disposeGroup(cl.group); scene.remove(cl.group);
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
  console.log('  ✓ goto×3 + showEnding + quiz [OK]');
}
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
