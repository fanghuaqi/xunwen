#!/usr/bin/env node
/* smoke-test.js —— 《山坡羊·潼关怀古》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、5 境（封面+4境）build()/update()×300帧、goto() 集成路径、
 * mixSky、setFade/disposeGroup、showEnding()、小测，
 * 以及交互境（兴亡之叹）点击序列：虚影常立 / 题字兴亡叠现 / 点击崩塌+迸尘+题字 /
 * 冷却守卫 / 尘埃落定 / 虚影复起（兴亡轮回）/ 二次点击。
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

console.log('[3] 场景冒烟：buildSky + 5 境 build/update + goto/showEnding + quiz …');
const harness = `
;(function(){
  const out=[];
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='峰峦如聚，波涛如怒，山河表里潼关路。望西都，意踌躇。伤心秦汉经行处，宫阙万间都做了土。兴，百姓苦；亡，百姓苦。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==5)throw new Error('STAGES 应为 5（封面+4境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 多音字/拼音逐项核对 ——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  const s1=POEM[0].segs[0].p, s2=POEM[1].segs[0].p, s3a=POEM[2].segs[0].p, s3b=POEM[2].segs[1].p, s4=POEM[3].segs[0].p;
  if(s1[3]!=='jù')throw new Error('聚 应读 jù: '+s1[3]);
  if(s1[7]!=='nù')throw new Error('怒 应读 nù: '+s1[7]);
  if(s2[4]!=='chóu'||s2[5]!=='chú')throw new Error('踌躇 应读 chóu chú: '+s2[4]+s2[5]);
  if(s3a[5]!=='xíng')throw new Error('经行之行 应读 xíng: '+s3a[5]);
  if(s3a[6]!=='chù')throw new Error('经行处之处 应读 chù: '+s3a[6]);
  if(s3b[1]!=='què')throw new Error('阙 应读 què: '+s3b[1]);
  if(s3b[4]!=='dōu')throw new Error('都做土之都 应读 dōu: '+s3b[4]);
  if(s3b[6]!=='le')throw new Error('做了土之了 应读 le: '+s3b[6]);
  if(s4[0]!=='xīng')throw new Error('兴亡之兴 应读 xīng: '+s4[0]);
  if(s4[4]!=='wáng')throw new Error('亡 应读 wáng: '+s4[4]);
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x1a120a,0.0075);
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
  // —— 交互境专项：宫阙化土 ——
  const s4obj=STAGES[4].build(); scene.add(s4obj.group);
  setFade(s4obj.group,1); s4obj.group.userData.fadeK=1;
  if(!s4obj.click)throw new Error('交互境缺 click()');
  if(!s4obj.ctl||!s4obj.ghost||!s4obj.edgeMat)throw new Error('交互境缺可测句柄 ctl/ghost/edgeMat');
  let burstMat=null,dustMat=null;
  s4obj.group.traverse(o=>{
    if(o.isPoints&&o.material.uniforms){
      if(o.material.uniforms.uT0&&burstMat===null)burstMat=o.material;
      if(o.material.uniforms.uMaxA&&!o.material.uniforms.uT0&&dustMat===null)dustMat=o.material;
    }
  });
  if(!burstMat||!dustMat)throw new Error('迸尘/尘柱粒子未找到');
  // 初始：虚影常立、题字隐、未触发
  let t4=0;
  for(let f=0;f<20;f++){ t4+=dt; s4obj.update(t4,dt); }
  if(s4obj.ghost.scale.y<0.95)throw new Error('初始宫阙虚影应常立: '+s4obj.ghost.scale.y);
  if(s4obj.ctl.fall!==0)throw new Error('未点击不应触发崩塌');
  if(dustMat.uniforms.uMaxA.value>0.05)throw new Error('未点击尘柱不应起: '+dustMat.uniforms.uMaxA.value);
  // 题字叠现：兴（前半轮）与 亡（后半轮）
  s4obj.update(8.6,dt);
  if(s4obj.xing.material.opacity<0.3)throw new Error('「兴」题字未叠现: '+s4obj.xing.material.opacity);
  s4obj.update(12.5,dt);
  if(s4obj.wang.material.opacity<0.3)throw new Error('「亡」题字未叠现: '+s4obj.wang.material.opacity);
  if(s4obj.xing.material.opacity>0.01)throw new Error('「兴」不应与「亡」同显: '+s4obj.xing.material.opacity);
  // 点击 → 崩塌 + 迸尘 + 题字
  t4+=dt; s4obj.update(t4,dt);
  s4obj.click();
  if(s4obj.ctl.fall!==1||s4obj.ctl.t>0.05)throw new Error('click 未启动崩塌');
  if(doc_els().flash!=='兴，百姓苦；亡，百姓苦')throw new Error('题字未弹出: '+doc_els().flash);
  if(burstMat.uniforms.uT0.value<0)throw new Error('迸尘未触发');
  // 冷却守卫：1.6s 内连点只算一次
  for(let f=0;f<10;f++){ t4+=dt; s4obj.update(t4,dt); }  // ~0.5s
  const tMid=s4obj.ctl.t;
  s4obj.click(); s4obj.click();
  if(s4obj.ctl.t!==tMid)throw new Error('冷却守卫失效: '+s4obj.ctl.t+'≠'+tMid);
  // 崩塌中段：尘柱起、虚影倾颓
  for(let f=0;f<30;f++){ t4+=dt; s4obj.update(t4,dt); }  // ~1.5s → 2.0s
  if(dustMat.uniforms.uMaxA.value<0.2)throw new Error('崩塌尘柱未起: '+dustMat.uniforms.uMaxA.value);
  if(s4obj.ghost.scale.y>0.55)throw new Error('虚影未开始倾颓: '+s4obj.ghost.scale.y);
  for(let f=0;f<40;f++){ t4+=dt; s4obj.update(t4,dt); }  // ~2.0 → 4.0s：崩塌完成
  if(s4obj.ghost.scale.y>0.12)throw new Error('宫阙未塌尽: '+s4obj.ghost.scale.y);
  // 兴亡轮回：10~14s 后虚影复起
  for(let f=0;f<220;f++){ t4+=dt; s4obj.update(t4,dt); } // → ~15s
  if(s4obj.ghost.scale.y<0.5)throw new Error('虚影未复起（兴亡轮回）: '+s4obj.ghost.scale.y);
  if(dustMat.uniforms.uMaxA.value>0.1)throw new Error('尘柱应已平息: '+dustMat.uniforms.uMaxA.value);
  // 冷却期满可再点
  s4obj.click();
  if(s4obj.ctl.t>0.05)throw new Error('冷却期满再点应重置计时');
  out.push('交互境 click → 宫阙化土(ghost '+s4obj.ghost.scale.y.toFixed(2)+
    ' 复起中) 尘柱'+dustMat.uniforms.uMaxA.value.toFixed(2)+' 迸尘+题字+守卫+轮回 [OK]');
  disposeGroup(s4obj.group); scene.remove(s4obj.group);
  // —— 境三标志瞬间专项：金碧虚影自动崩塌 ——
  const s3=STAGES[3].build(); scene.add(s3.group); setFade(s3.group,1); s3.group.userData.fadeK=1;
  let ghostMat=null;
  s3.group.traverse(o=>{ if(o.isLineSegments&&o.material.transparent&&ghostMat===null)ghostMat=o.material; });
  if(!ghostMat)throw new Error('金碧轮廓线未找到');
  let t3=0;
  s3.update(5.5,dt);
  if(ghostMat.opacity<0.3)throw new Error('虚影应亮起: '+ghostMat.opacity);
  s3.update(13.0,dt);
  if(ghostMat.opacity>0.4)throw new Error('13s 时应已近乎塌尽: '+ghostMat.opacity);
  s3.update(17.0,dt);
  let ruinOp=0; s3.group.traverse(o=>{ if(o.isMesh&&o.material.transparent&&o.material.opacity>ruinOp&&o.material.color.getHex()===0x2a2016)ruinOp=o.material.opacity; });
  if(ruinOp<0.8)throw new Error('残垣未显现: '+ruinOp);
  out.push('境三 虚影亮起→崩塌(edge '+ghostMat.opacity.toFixed(2)+') 残垣'+ruinOp.toFixed(2)+' [OK]');
  disposeGroup(s3.group); scene.remove(s3.group);
  // —— goto() 集成路径 ——
  for(let i=1;i<STAGES.length;i++){ goto(i); state='stage'; }
  // —— 终章 ——
  showEnding(); state='stage';
  // —— 小测逻辑 ——
  startQuiz(); qIdx=QUIZ.length-1; renderQuiz(); showResult();
  if(QUIZ.length!==5)throw new Error('小测应为 5 题');
  out.push('goto×4 + showEnding + quiz [OK]');
  window.__SMOKE=out.join('\\n');

  function doc_els(){ return {flash:document.querySelector('#flash').textContent}; }
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__SMOKE).split('\n').map(l => '  ✓ ' + l).join('\n'));
  console.log('  ✓ goto×4 + showEnding + quiz [OK]');
}
/* —— words 评语数组静态核对（题数+1=6，且为本诗定制）—— */
const wq = code.match(/words\s*=\s*\[([^\]]*)\]/);
const wn = wq ? wq[1].split(',').length : 0;
if (wn !== 6) { console.error('  ✗ words 评语数组应为 6 项，实际 ' + wn); fails++; }
else console.log('  ✓ words 评语数组 6 项（题数+1），按本诗定制 [OK]');
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
