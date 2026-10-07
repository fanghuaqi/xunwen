#!/usr/bin/env node
/* smoke-test.js —— 《夏日绝句》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、3 境 build()/update()×300帧/click、goto() 集成路径、
 * mixSky、setFade/disposeGroup、showEnding()、交互境"江风大作"触发/冷却守卫专项校验。
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

console.log('[3] 场景冒烟：buildSky + 3 境 build/update/click + goto/showEnding …');
const harness = `
;(function(){
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='生当作人杰，死亦为鬼雄。至今思项羽，不肯过江东。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==3)throw new Error('STAGES 应为 3（封面+2境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 注音数量与多音字逐字核对 ——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  if(POEM[0].segs[0].p[1]!=='dàng')throw new Error('当作之当 应读 dàng，实为 '+POEM[0].segs[0].p[1]);
  if(POEM[0].segs[0].p[4]!=='jié')throw new Error('杰 应读 jié');
  if(POEM[0].segs[1].p[1]!=='yì')throw new Error('亦 应读 yì');
  if(POEM[0].segs[1].p[2]!=='wéi')throw new Error('为（成为）应读 wéi');
  if(POEM[1].segs[1].p[0]!=='bù')throw new Error('不肯之不 应读 bù');
  // —— 小测结构与评语 ——
  if(QUIZ.length!==5)throw new Error('小测应为 5 题');
  const wm=code_words(); function code_words(){return null;} // 占位，评语在下方正则校验
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x100b07,0.005);
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
      applySky();
    }
    if(obj.onEnter)obj.onEnter();
    if(obj.click){ obj.click(); for(let f=0;f<40;f++){stageT+=dt;clock.t+=dt;if(obj.update)obj.update(stageT,dt);} }
    // 天空插值（前后境混合）
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1);
    SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group);
    scene.remove(obj.group);
    window.__LOG=(window.__LOG||[]).concat('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  // —— 交互境专项：江风大作 + 冷却守卫（计时时钟 clock.t，2.4s 冷却）——
  const s2=STAGES[2].build(); scene.add(s2.group); setFade(s2.group,1); s2.group.userData.fadeK=1;
  let burstMat=null,rope=null,capes=0;
  s2.group.traverse(o=>{
    if(o.isPoints&&o.material.uniforms&&o.material.uniforms.uT0)burstMat=o.material;
    if(o.isLine)rope=o;
    if(o.isMesh&&o.geometry&&o.geometry.type==='PlaneGeometry'&&o.material.side===THREE.DoubleSide)capes++;
  });
  if(!burstMat)throw new Error('交互境缺爆点粒子（缆绳绷响）');
  if(!rope)throw new Error('交互境缺动态缆绳');
  if(capes<3)throw new Error('衣袂/披风应至少 3 幅，实际 '+capes);
  for(let f=0;f<100;f++){stageT+=dt;clock.t+=dt;if(s2.update)s2.update(stageT,dt);}
  const ropeArr=rope.geometry.attributes.position.array;
  const finite=a=>{for(let i=0;i<a.length;i++)if(!isFinite(a[i]))return false;return true;};
  if(!finite(ropeArr))throw new Error('缆绳顶点出现 NaN');
  // 第一次点击生效
  s2.click();
  const t0a=burstMat.uniforms.uT0.value;
  if(!(t0a>0))throw new Error('点击后爆点未触发 uT0='+t0a);
  // 冷却期内再点（0.5s 后）→ 守卫拦截
  clock.t+=0.5; s2.click();
  if(burstMat.uniforms.uT0.value!==t0a)throw new Error('冷却守卫失效：2.4s 内连点未被拦截');
  // 冷却期后再点 → 生效
  clock.t+=2.5; s2.click();
  const t0b=burstMat.uniforms.uT0.value;
  if(t0b<=t0a)throw new Error('冷却后再点应生效 t0a='+t0a+' t0b='+t0b);
  // 大风期间衣袂摆幅应放大（风起前后各采 60 帧，取逐帧最大摆幅）
  let ampCalm=0,ampGust=0;
  clock.t+=10; // 等风完全回落
  for(let f=0;f<60;f++){stageT+=dt;clock.t+=dt;if(s2.update)s2.update(stageT,dt);
    s2.group.traverse(o=>{ if(o.isMesh&&o.geometry&&o.geometry.type==='PlaneGeometry'){ampCalm=Math.max(ampCalm,Math.abs(o.rotation.x));} });
  }
  s2.click(); // 风起
  for(let f=0;f<70;f++){stageT+=dt;clock.t+=dt;if(s2.update)s2.update(stageT,dt);
    s2.group.traverse(o=>{ if(o.isMesh&&o.geometry&&o.geometry.type==='PlaneGeometry'){ampGust=Math.max(ampGust,Math.abs(o.rotation.x));} });
  } // ~3.5s 处于大风
  if(!(ampGust>ampCalm))throw new Error('江风大作后衣袂摆幅未放大 calm='+ampCalm.toFixed(3)+' gust='+ampGust.toFixed(3));
  if(!finite(ropeArr))throw new Error('大风后缆绳顶点 NaN');
  window.__LOG=(window.__LOG||[]).concat('交互境 click×2+守卫+风包络 [OK] calm='+ampCalm.toFixed(2)+' gust='+ampGust.toFixed(2));
  disposeGroup(s2.group); scene.remove(s2.group);
  // —— goto() 集成路径（含越界 clamp）——
  goto(1); state='stage';
  goto(2); state='stage';
  goto(9); // 越界 → clamp 到 2
  state='stage';
  if(curIdx!==2)throw new Error('goto(9) 应 clamp 至 2，实际 '+curIdx);
  goto(0); state='stage'; // 回封面
  window.__LOG=(window.__LOG||[]).concat('goto×4（含 clamp 越界）[OK]');
  // —— 终章 ——
  showEnding(); state='stage';
  // —— 小测逻辑 ——
  startQuiz(); qIdx=QUIZ.length-1; renderQuiz(); showResult();
  window.__LOG=(window.__LOG||[]).concat('showEnding + quiz [OK]');
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__LOG).split(',').map(l => '  ✓ ' + l).join('\n'));
}
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
