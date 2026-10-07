#!/usr/bin/env node
/* smoke-test.js —— 《出塞》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、4 境 build()/update()×300帧/click×3、goto() 集成路径、
 * mixSky、setFade/disposeGroup、showEnding()、交互境烽火点亮序列/冷却守卫专项校验。
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

console.log('[3] 场景冒烟：buildSky + 4 境 build/update/click + goto/showEnding …');
const harness = `
;(function(){
  const out=[];
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='秦时明月汉时关，万里长征人未还。但使龙城飞将在，不教胡马度阴山。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==4)throw new Error('STAGES 应为 4（封面+3境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 注音数量逐句核对 ——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  if(!POEM[1].segs[0].p[6].startsWith('huán'))throw new Error('还 应读 huán');
  if(!POEM[2].segs[0].p[5].startsWith('jiàng'))throw new Error('将 应读 jiàng');
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x150e08,0.0055);
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
      stageT+=dt;
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
      obj.click(); for(let f=0;f<40;f++){stageT+=dt; if(obj.update)obj.update(stageT,dt);}
      obj.click(); for(let f=0;f<40;f++){stageT+=dt; if(obj.update)obj.update(stageT,dt);}
    }
    // 天空插值（前后境混合）
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1);
    SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group);
    scene.remove(obj.group);
    out.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  // —— 交互境专项：烽火依次点亮 + 冷却守卫 ——
  const s3=STAGES[3].build(); scene.add(s3.group); setFade(s3.group,1); s3.group.userData.fadeK=1;
  const halos=[],fires=[];
  s3.group.traverse(o=>{
    if(o.isSprite&&o.material.map===glowTex()&&o.material.opacity===0)halos.push(o);
    if(o.isPoints&&o.material.uniforms&&o.material.uniforms.uRise&&o.material.uniforms.uMaxA)fires.push(o.material);
  });
  if(halos.length!==13)throw new Error('应有 13 处烽火（2 火盆+11 烽燧），实际 '+halos.length);
  if(fires.length!==13)throw new Error('应有 13 层火焰粒子，实际 '+fires.length);
  const litCount=()=>halos.filter(h=>h.material.opacity>0.1).length;
  for(let f=0;f<200;f++){stageT+=dt; if(s3.update)s3.update(stageT,dt);}
  s3.onEnter(); // 关头火盆自动先燃一处（延时 2.2s）
  for(let f=0;f<120;f++){stageT+=dt; if(s3.update)s3.update(stageT,dt);}
  if(litCount()<1)throw new Error('onEnter 后火盆未自动燃起');
  const c0=litCount();
  s3.click(); s3.click(); s3.click(); // 三连点：仅第一发生效，后两发被冷却守卫拦截
  for(let f=0;f<60;f++){stageT+=dt; if(s3.update)s3.update(stageT,dt);}
  if(litCount()!==c0+1)throw new Error('点击/冷却守卫异常: lit='+litCount()+' 期望 '+(c0+1));
  let guard=0;
  while(litCount()<13&&guard++<40){ s3.click(); for(let f=0;f<60;f++){stageT+=dt; if(s3.update)s3.update(stageT,dt);} }
  if(litCount()!==13)throw new Error('烽火未传遍天边: '+litCount()+'/13');
  const minHalo=Math.min(...halos.map(h=>h.material.opacity));
  const minFire=Math.min(...fires.map(m=>m.uniforms.uMaxA.value));
  if(minHalo<0.1)throw new Error('有烽火辉光未亮: opacity='+minHalo);
  if(minFire<0.4)throw new Error('有火焰粒子未燃: uMaxA='+minFire);
  s3.click(); for(let f=0;f<30;f++){stageT+=dt; if(s3.update)s3.update(stageT,dt);} // 全亮后再点 → 题字路径
  const plFound=[];
  s3.group.traverse(o=>{ if(o.isLight&&o.isPointLight)plFound.push(o); });
  if(plFound.length!==1||plFound[0].intensity<=0)throw new Error('烽火点光未生效');
  out.push('交互境 click ×N → 烽火 13/13 亮 halo≥'+minHalo.toFixed(2)+' fire≥'+minFire.toFixed(2)+' 点光='+plFound[0].intensity.toFixed(2)+' [OK]');
  disposeGroup(s3.group); scene.remove(s3.group);
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
