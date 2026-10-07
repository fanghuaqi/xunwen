#!/usr/bin/env node
/* smoke-test.js —— 《赤壁》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、4 境 build()/update()×300帧、goto() 集成路径、
 * mixSky、setFade/disposeGroup、showEnding()、小测，
 * 以及交互境（东风二乔）点击序列：沙退戟现 / 铭文显现 / 东风骤起 / 冷却守卫。
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
const elCache = {};
const doc = {
  querySelector: s => (elCache[s] || (elCache[s] = elStub('q:' + s))),
  querySelectorAll: () => [],
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

console.log('[3] 场景冒烟：buildSky + 4 境 build/update + goto/showEnding + quiz …');
const harness = `
;(function(){
  const out=[];
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='折戟沉沙铁未销，自将磨洗认前朝。东风不与周郎便，铜雀春深锁二乔。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==4)throw new Error('STAGES 应为 4（封面+3境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 多音字/拼音逐项核对 ——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  if(!POEM[0].segs[0].p[1].startsWith('jǐ'))throw new Error('戟 应读 jǐ');
  if(!POEM[0].segs[0].p[6].startsWith('xiāo'))throw new Error('销 应读 xiāo');
  if(!POEM[1].segs[0].p[1].startsWith('jiāng'))throw new Error('将（拿取义）应读 jiāng');
  if(!POEM[2].segs[0].p[5].startsWith('láng'))throw new Error('郎 应读 láng');
  if(!POEM[2].segs[1].p[6].startsWith('qiáo'))throw new Error('乔 应读 qiáo');
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x1a120a,0.0055);
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
    if(obj.click){ obj.click(); for(let f=0;f<40;f++){stageT+=dt; if(obj.update)obj.update(stageT,dt);} }
    // 天空插值（前后境混合）
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1);
    SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group);
    scene.remove(obj.group);
    out.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  // —— 交互境专项：沙退戟现 + 铭文显现 + 东风骤起 + 冷却守卫 ——
  const s3=STAGES[3].build(); scene.add(s3.group); setFade(s3.group,1); s3.group.userData.fadeK=1;
  if(!s3.click)throw new Error('交互境缺 click()');
  if(!s3.sandMat||!s3.inscMat||!s3.ctl)throw new Error('交互境缺可测句柄 sandMat/inscMat/ctl');
  let fire1=null,redLight=null;
  s3.group.traverse(o=>{
    if(o.isPoints&&o.material.uniforms&&o.material.uniforms.uMaxA&&fire1===null)fire1=o.material;
    if(o.isLight&&o.isPointLight&&o.color.getHex()===0xff5a22)redLight=o;
  });
  if(!fire1||!redLight)throw new Error('火场粒子/暖红点光未找到');
  // 初始：覆沙在、戟低、铭文隐、东风未起
  for(let f=0;f<30;f++){stageT+=dt; s3.update(stageT,dt);}
  if(s3.sandMat.opacity<0.9)throw new Error('初始覆沙应完整: '+s3.sandMat.opacity);
  if(s3.ctl.fired)throw new Error('未点击不应触发');
  if(redLight.intensity>1.7)throw new Error('东风未起红光不应爆亮: '+redLight.intensity);
  const sand0=s3.sandMat.opacity;
  // 点击一次 → 沙退戟现 + 铭文闪耀 + 东风骤起
  s3.click();
  if(!s3.ctl.fired)throw new Error('click 未置 fired');
  for(let f=0;f<10;f++){stageT+=dt; s3.update(stageT,dt);}   // 0.5s
  // 冷却守卫：冷却期内连点只算一次（ctl.t 不被重置）
  const tMid=s3.ctl.t;
  s3.click(); s3.click();
  if(s3.ctl.t!==tMid)throw new Error('冷却守卫失效: '+s3.ctl.t+'≠'+tMid);
  for(let f=0;f<40;f++){stageT+=dt; s3.update(stageT,dt);}   // ~2.5s
  if(s3.inscMat.opacity<0.6)throw new Error('铭文未闪耀: '+s3.inscMat.opacity);
  if(redLight.intensity<2.4)throw new Error('东风骤起红光不足: '+redLight.intensity);
  if(fire1.uniforms.uMaxA.value<1.0)throw new Error('火场未随东风增强: '+fire1.uniforms.uMaxA.value);
  if(document.querySelector('#flash').textContent!=='铜雀春深锁二乔')throw new Error('题字未弹出');
  for(let f=0;f<70;f++){stageT+=dt; s3.update(stageT,dt);}   // ~6s：沙退完成
  if(s3.sandMat.opacity>0.05)throw new Error('沙未退尽: '+s3.sandMat.opacity+'（初始 '+sand0+'）');
  // 冷却期满可再次点击
  s3.click();
  if(s3.ctl.t>0.01)throw new Error('冷却期满再点应重置计时');
  for(let f=0;f<60;f++){stageT+=dt; s3.update(stageT,dt);}
  if(redLight.intensity<2.0)throw new Error('二度东风未起: '+redLight.intensity);
  // 漫长演化至风息（>8.5s 后东风完全止息）
  for(let f=0;f<140;f++){stageT+=dt; s3.update(stageT,dt);}
  if(fire1.uniforms.uMaxA.value>0.85)throw new Error('东风应渐息: '+fire1.uniforms.uMaxA.value);
  if(s3.inscMat.opacity<0.4)throw new Error('铭文应常显: '+s3.inscMat.opacity);
  out.push('交互境 click → 沙退(sand '+sand0.toFixed(2)+'→'+s3.sandMat.opacity.toFixed(2)+
    ') 铭文'+s3.inscMat.opacity.toFixed(2)+' 东风红光'+redLight.intensity.toFixed(2)+' 守卫 [OK]');
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
  console.log('  ✓ goto×3 + showEnding + quiz + words[6] [OK]');
}
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
