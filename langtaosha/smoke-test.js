#!/usr/bin/env node
/* smoke-test.js —— 《浪淘沙（其一）》深度冒烟测试
 * 用真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本顶层，
 * 然后真实运行：buildSky、4 境 build()/update()×300帧/click×2、goto() 集成路径、
 * mixSky、setFade/disposeGroup、showEnding()，以及交互境「直上银河」专项：
 * 光带点亮、双星+题字渐亮、相机升空终点、clock.t 计时 + 一次一击守卫、cam 重置。
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
  const near=(a,b,eps)=>Math.abs(a-b)<=(eps===undefined?0.6:eps);
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  if(joined!=='九曲黄河万里沙，浪淘风簸自天涯。如今直上银河去，同到牵牛织女家。')throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==4)throw new Error('STAGES 应为 4（封面+3境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  // —— 注音数量与多音字逐句核对 ——
  POEM.forEach(p=>p.segs.forEach(seg=>{
    const han=[...seg.c].filter(c=>!/[，。、！？；：]/.test(c)).length;
    if(han!==seg.p.length)throw new Error('注音数不符: '+seg.c);
  }));
  if(POEM[0].segs[0].p[1]!=='qū')throw new Error('曲 应读 qū, 实际 '+POEM[0].segs[0].p[1]);
  if(POEM[1].segs[0].p[3]!=='bǒ')throw new Error('簸 应读 bǒ, 实际 '+POEM[1].segs[0].p[3]);
  if(POEM[1].segs[0].p[6]!=='yá')throw new Error('涯 应读 yá, 实际 '+POEM[1].segs[0].p[6]);
  if(POEM[2].segs[1].p[5]!=='nǚ')throw new Error('女 应读 nǚ, 实际 '+POEM[2].segs[1].p[5]);
  // —— 小测评语长度 ——
  const wq=codeWordLen(); function codeWordLen(){return 6;} // words 由 validate 校验，此处仅占位
  // —— 最小 renderer 桩 ——
  renderer={setClearColor(){},render(){},domElement:{addEventListener(){}}};
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x241811,0.0046);
  camera=new THREE.PerspectiveCamera(55,16/9,0.1,1500);
  curLook=new THREE.Vector3();
  buildSky();
  SKYcur=cloneSky(STAGES[0].sky());
  applySky();
  const dt=0.05;
  // —— 逐境深测（clock.t 与 stageT 同步推进，模拟主循环） ——
  for(let i=0;i<STAGES.length;i++){
    const def=STAGES[i];
    const obj=def.build();
    scene.add(obj.group);
    setFade(obj.group,1);
    obj.group.userData.fadeK=1;
    let meshes=0,lights=0,points=0,sprites=0;
    obj.group.traverse(o=>{ if(o.isMesh)meshes++; if(o.isPoints)points++; if(o.isLight)lights++; if(o.isSprite)sprites++; });
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
    out.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' light='+lights+' sprite='+sprites+' [OK]');
  }
  // —— 交互境专项：直上银河 ——
  stageT=0; clock.t=0;
  const s3=STAGES[3].build(); scene.add(s3.group); setFade(s3.group,1); s3.group.userData.fadeK=1;
  const cores=[],tags=[],ribbons=[],bands=[];
  s3.group.traverse(o=>{
    if(o.isSprite&&o.material.map===glowTex()&&o.material.color.getHex()===0xfff4dc)cores.push(o);
    if(o.isSprite&&o.material.map&&o.material.map.image&&o.material.map.image.width===200)tags.push(o);
    if(o.isPoints&&o.material.isPointsMaterial&&o.material.map===circleTex()&&o.material.size>=5)ribbons.push(o);
    if(o.isPoints&&o.material.isPointsMaterial&&o.material.fog===false&&o.material.size<3)bands.push(o);
  });
  if(cores.length!==2)throw new Error('应有 2 颗主星（牵牛/织女），实际 '+cores.length);
  if(tags.length!==2)throw new Error('应有 2 幅星名题字，实际 '+tags.length);
  if(ribbons.length!==2)throw new Error('应有 2 层银河光带（金核+星晕），实际 '+ribbons.length);
  if(bands.length<3)throw new Error('银河底带+双星团 应≥3 组星点，实际 '+bands.length);
  const runFrames=n=>{ for(let f=0;f<n;f++){stageT+=dt;clock.t+=dt; if(s3.update)s3.update(stageT,dt);} };
  // 未点击：光带微光星轨，双星暗淡
  runFrames(40);
  if(cores[0].material.opacity>0.4)throw new Error('未点击时双星不应亮起: '+cores[0].material.opacity);
  if(ribbons[0].material.opacity>0.25)throw new Error('未点击时光带不应点亮: '+ribbons[0].material.opacity);
  if(tags.some(tg=>tg.material.opacity>0.05))throw new Error('未点击时题字不应浮现');
  // 点击 → 光带亮起 + 相机升空
  s3.click();
  if(Math.abs(STAGES[3].cam.f[1]-15)>0.1)throw new Error('点击瞬间相机应仍在起点');
  runFrames(60); // 3s：升空中段
  const midY=STAGES[3].cam.f[1];
  if(!(midY>60&&midY<120))throw new Error('升空中段高度异常: '+midY);
  s3.click(); s3.click(); // 连点：一次一击守卫，飞航不得重置
  runFrames(90); // 共 >6.5s：升空完成
  const endY=STAGES[3].cam.f[1];
  if(!near(endY,130,0.5))throw new Error('升空终点应为 130, 实际 '+endY);
  if(!near(STAGES[3].cam.lf[1],265,0.5))throw new Error('终点注视高度应为 265, 实际 '+STAGES[3].cam.lf[1]);
  if(midY>=endY)throw new Error('升空应单调上升');
  const maxCore=Math.max(cores[0].material.opacity,cores[1].material.opacity);
  const minCore=Math.min(cores[0].material.opacity,cores[1].material.opacity);
  if(minCore<0.95)throw new Error('双星未全亮: '+minCore);
  const minTag=Math.min(tags[0].material.opacity,tags[1].material.opacity);
  if(minTag<0.85)throw new Error('题字未浮现: '+minTag);
  const minRib=Math.min(ribbons[0].material.opacity,ribbons[1].material.opacity);
  if(minRib<0.45)throw new Error('银河光带未点亮: '+minRib);
  // 光带粒子确实沿曲线铺到高空
  let maxY=0;
  ribbons.forEach(r=>{ const arr=r.geometry.attributes.position.array;
    for(let i=1;i<arr.length;i+=3)if(arr[i]>maxY)maxY=arr[i]; });
  if(maxY<200)throw new Error('光带未升至高空: maxY='+maxY.toFixed(1));
  s3.click(); runFrames(30); // 完成后再点 → 不得重新起飞
  if(!near(STAGES[3].cam.f[1],130,0.5))throw new Error('完成后连点导致重新起飞: '+STAGES[3].cam.f[1]);
  const plCnt=[]; s3.group.traverse(o=>{ if(o.isLight&&o.isPointLight)plCnt.push(o); });
  if(plCnt.length!==1||plCnt[0].intensity<2)throw new Error('升空点光未增强: '+plCnt.map(p=>p.intensity).join(','));
  out.push('交互境 click → 升空 '+midY.toFixed(1)+'→'+endY.toFixed(1)+' 星'+minCore.toFixed(2)+' 字'+minTag.toFixed(2)+' 带 maxY='+maxY.toFixed(0)+' 守卫[OK]');
  // cam 重置：再次进入本境时起飞相机恢复
  disposeGroup(s3.group); scene.remove(s3.group);
  const again=STAGES[3].build();
  if(!near(again&&STAGES[3].cam.f[1],15,0.1))throw new Error('重入本境 cam 未重置: '+STAGES[3].cam.f[1]);
  disposeGroup(again.group);
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
  console.log('  ✓ goto×3 + cam重置 + showEnding + quiz [OK]');
}
if (fails === 0) console.log('\nSMOKE PASS —— 全部 builder/update/click/goto 真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
