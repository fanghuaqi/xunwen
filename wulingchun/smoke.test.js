#!/usr/bin/env node
/* smoke.test.js —— 《武陵春·风住尘香花已尽》（宋·李清照）深度冒烟测试
 *
 * 在 Node vm 中装载 THREE（优先本地 three.min.js 的真 r128；缺失时回落到 THREE 桩），
 * 配上带「真实 classList / 事件登记 / 画布 2D」的 DOM 桩，执行主脚本顶层后真实跑：
 *   1) 顶层安全（THREE 未加载时不炸）—— validate.js 的 Pass A 同款检查
 *   2) boot() 全流程（WebGLRenderer 打桩）+ 天空分层/fog:false/雾同步等硬性约束
 *   3) 逐境 build()/update()×400 帧/onEnter/click，并逐境验证
 *      「每帧写 opacity/intensity 必乘 fadeK」+ 三层构图（前景/背景都在）
 *   4) goto() 跨场运镜 + mixSky + setFade/disposeGroup 全生命周期
 *   5) 封面 → 自动游览（autoMode 默认开）→ 终章 → 小测，一路真实驱动 animate()
 *   6) 交互接线：pointerdown/空格 第六境（末境·天下归心，空格先交互再进终章）
 * 用法: node smoke.test.js    （退出码 0 = 全部通过）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = __dirname;
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
const N = Number((code.match(/clamp\(i,0,(\d+)\)/) || [])[1]);
let fails = 0, warns = 0;
const ok = m => console.log('  ✓ ' + m);
const bad = m => { console.error('  ✗ ' + m); fails++; };

/* ---------------- 引擎：真 THREE r128，缺失则回落 THREE 桩 ---------------- */
let engineSrc = '', engineName = '';
const localThree = path.join(DIR, 'three.min.js');
const threePath = fs.existsSync(localThree) ? localThree : path.join(DIR, '..', '_pipeline', 'vendor', 'three.min.js');
if (fs.existsSync(threePath)) { engineSrc = fs.readFileSync(threePath, 'utf8'); engineName = '真 THREE r128（本地 three.min.js）'; }
console.log('[1] 引擎：' + (engineName || 'THREE 桩（three.min.js 缺失）'));
console.log('    境数 N = ' + N);

/* ---------------- DOM 桩（元素按选择器缓存，事件可回放） ---------------- */
function ctx2d() {
  const grad = () => ({ addColorStop() {} });
  return { createRadialGradient: grad, createLinearGradient: grad, fillRect() {}, strokeRect() {},
    clearRect() {}, fillText() {}, beginPath() {}, closePath() {}, arc() {}, moveTo() {}, lineTo() {},
    bezierCurveTo() {}, quadraticCurveTo() {}, fill() {}, stroke() {}, save() {}, restore() {},
    translate() {}, rotate() {}, scale() {}, drawImage() {}, setTransform() {},
    fillStyle: '', strokeStyle: '', lineWidth: 1, font: '', textAlign: '', textBaseline: '',
    shadowColor: '', shadowBlur: 0, globalAlpha: 1 };
}
function makeEl(tag) {
  const cls = new Set();
  const el = {
    tag, id: '', className: '', children: [], _h: {},
    style: { setProperty(k, v) { this[k] = v; }, removeProperty() {} },
    textContent: '', innerHTML: '', open: false, offsetWidth: 0, disabled: false, title: '',
    classList: {
      add: c => cls.add(c), remove: c => cls.delete(c),
      contains: c => cls.has(c), toggle: (c, f) => { const on = f === undefined ? !cls.has(c) : !!f; on ? cls.add(c) : cls.delete(c); return on; },
      _set: cls,
    },
    addEventListener(t, f) { el._h[t] = f; }, removeEventListener() {},
    appendChild(c) { el.children.push(c); return c; },
    querySelectorAll() { return el.children.filter(c => c.className && c.className.indexOf('opt') === 0); },
    querySelector() { return makeEl('x'); },
  };
  return el;
}
const reg = new Map();
const doc = {
  querySelector: s => { if (!reg.has(s)) reg.set(s, makeEl('q' + s)); return reg.get(s); },
  querySelectorAll: () => [],
  createElement: tag => tag === 'canvas'
    ? Object.assign(makeEl('canvas'), { width: 64, height: 64, getContext: () => ctx2d() })
    : makeEl(tag),
  addEventListener() {}, documentElement: makeEl('html'), body: makeEl('body'),
  head: makeEl('head'), activeElement: null, fullscreenElement: null,
};
const clockRef = { t: 0 };
const sandbox = {
  document: doc, console, navigator: { userAgent: 'node' },
  performance: { now: () => clockRef.t },
  __clock: clockRef,
  requestAnimationFrame() { return 0; },
  setTimeout() { return 0; }, clearTimeout() {},
  innerWidth: 1600, innerHeight: 900, devicePixelRatio: 1,
  location: { reload() {} },
};
sandbox.window = sandbox; sandbox.self = sandbox; sandbox.globalThis = sandbox;
sandbox.addEventListener = (t, f) => { sandbox._h = sandbox._h || {}; sandbox._h[t] = f; };
vm.createContext(sandbox);
const run = (src, name) => {
  try { vm.runInContext(src, sandbox, { filename: name }); return true; }
  catch (e) {
    const where = (e && e.stack ? String(e.stack).split('\n').find(l => /:\d+/.test(l)) : '') || '';
    bad(name + ': ' + ((e && e.message) || e) + '   @ ' + where.trim());
    return false;
  }
};

/* [2] 顶层安全：THREE 未就绪时必须能安全执行（抓「顶层引用 THREE」） */
console.log('[2] 顶层安全（THREE 未加载）…');
{
  const bare = Object.assign({}, sandbox, { THREE: undefined });
  try {
    vm.createContext(bare);
    vm.runInContext(code, bare, { filename: 'passA-no-three' });
    ok('主脚本在 THREE 缺失时顶层执行无异常（惰性工厂正确）');
  } catch (e) { bad('顶层引用了 THREE：' + e.message); }
}

console.log('[3] 装载引擎 + 主脚本顶层 …');
if (engineSrc) { if (!run(engineSrc, 'three.min.js')) process.exit(1); }
else {
  sandbox.THREE = new Proxy({}, { get: (t, p) => p === 'then' ? undefined : (class C { constructor() {} }) });
  ok('已注入 THREE 桩');
}
if (!run(code, 'main')) process.exit(1);
ok('主脚本顶层执行通过（' + N + ' 境）');

/* [4] boot() + 逐境深测 + 硬性约束 + 自动游览全生命周期 */
console.log('[4] boot() + 逐境 builder/update/click + fadeK 合规 + 三层构图 + 自动游览 + 小测 …');
const harness = `
;(function(){
  const out=[];
  const A=(c,m)=>{ if(!c) throw new Error('断言失败: '+m); };
  A(STAGES.length===POEM.length+1,'STAGES 应比 POEM 多 1');
  A(POEM.length===${N} && STAGES.length===${N}+1,'本诗应为 2 境 + 卷首');
  for(let i=1;i<STAGES.length;i++) A(STAGES[i].name===POEM[i-1].name,'境名错位 @'+i);
  A(autoMode===true,'自动游览应默认开启');
  A(POEM.map(l=>l.segs.map(s=>s.c).join('')).join('').length>47,'全诗文本长度异常（应 160 字上下）');
  // —— WebGLRenderer 打桩（Node 无 GL），boot() 全流程真实执行 ——
  THREE.WebGLRenderer=function(){ return {
    setPixelRatio(){}, setSize(){}, setClearColor(){}, render(){}, domElement:{ _h:{}, addEventListener(t,f){ this._h[t]=f; } },
  }; };
  boot();
  A(state==='stage','boot 后应处于 stage');
  A(curIdx===0,'boot 后应在封面境');
  // —— 天空系统硬性约束：fog:false + renderOrder 分层 ——
  A(skyDome.material.fog===false,'穹顶必须 fog:false');
  A(skyDome.renderOrder===-10,'穹顶 renderOrder 应为 -10');
  A(starA.renderOrder===-9 && starB.renderOrder===-9,'星层 renderOrder 应为 -9');
  A(moonGroup.renderOrder===-8 && moonGlow.material.fog===false,'月 renderOrder -8 且 fog:false');
  A(starA.material.fog===false,'星材质必须 fog:false');
  A(scene.fog && scene.fog.density>0 && typeof scene.fog.density==='number','场景雾已建立');
  A(scene.fog.density<=0.0072,'雾密度应在本赛道上限内（实测 '+scene.fog.density+'）');
  // —— 逐境深测（真 THREE 建几何/材质/着色器）——
  const bad=[];
  for(let i=0;i<STAGES.length;i++){
    const def=STAGES[i];
    const obj=def.build();
    scene.add(obj.group); setFade(obj.group,1); obj.group.userData.fadeK=1;
    let meshes=0,points=0,sprites=0,lines=0,lights=0,tris=0;
    obj.group.traverse(o=>{
      if(o.isMesh){ meshes++; }
      if(o.isPoints)points++;
      if(o.isSprite)sprites++;
      if(o.isLine)lines++;
      if(o.isLight)lights++;
      if(o.isMesh&&o.geometry&&o.geometry.attributes&&o.geometry.attributes.position){
        const g=o.geometry;
        const t=(g.index?g.index.count:g.attributes.position.count)/3;
        tris+=t*(o.isInstancedMesh?(o.count||1):1);
      }
    });
    A(meshes>0,'境 '+def.name+' 应至少有一个 Mesh');
    A(lights>0,'境 '+def.name+' 应自带灯光（addLights）');
    const calls=meshes+points+sprites+lines;
    A(calls<=120,'境 '+def.name+' draw call 代理值 '+calls+' >120');
    A(tris<=120000,'境 '+def.name+' 三角面 '+Math.round(tris)+' >12 万');
    /* 三层构图：背景（多峰山脊 makeRange，带 uFogK）+ 前景（有贴相机的顶层子对象） */
    let hasRidge=false, fgNear=0;
    obj.group.traverse(o=>{ const m=o.material; if(m&&m.uniforms&&m.uniforms.uFogK)hasRidge=true; });
    const camZ=def.cam.f[2];
    obj.group.children.forEach(c=>{ if(c.position&&(camZ-c.position.z)<60&&(camZ-c.position.z)>-10)fgNear++; });
    A(hasRidge,'境 '+def.name+' 缺背景层（多峰山脊 makeRange）');
    A(fgNear>=1,'境 '+def.name+' 缺前景层（无贴近相机的框景对象）');
    for(let f=0;f<400;f++){ stageT+=0.05; if(obj.update)obj.update(stageT,0.05); }
    if(obj.onEnter)obj.onEnter();
    A(!!obj.update,'境 '+def.name+' 缺 update');
    A(isFinite(camera.position.x),'相机 NaN @'+def.name);
    // 末境（长车踏破）必须挂 click
    if(i===2){
      A(typeof obj.click==='function','末境 '+def.name+' 应可点击');
      obj.click();                                  // 冷却期内应直接返回
      for(let f=0;f<40;f++){ stageT+=0.05; obj.update(stageT,0.05); }
      obj.click();                                  // 冷却后真实触发（乌鹊归山/flash）
      A(obj.clicked===true,'末境点击应置 clicked');
      for(let f=0;f<60;f++){ stageT+=0.05; obj.update(stageT,0.05); }
    }
    // —— fadeK 合规：淡到 0.4 后，任何「每帧写 opacity/intensity」都不得越过 base*0.4 ——
    const k=0.4;
    setFade(obj.group,k);
    if(obj.update)obj.update(stageT,0.05);
    obj.group.traverse(o=>{
      if(o.isLight){ const b=o.userData.baseI;
        /* 1.15 容差 = 引擎火焰/灯烛自身的闪烁包络（base×0.68~1.12）；真正的漏乘 fadeK 通常 ≥2 倍 */
        if(b!==undefined && o.intensity>b*k*1.15+1e-4) bad.push(def.name+' 灯光 '+o.intensity.toFixed(3)+'>'+(b*k).toFixed(3)); return; }
      const m=o.material; if(!m||m.isShaderMaterial)return;
      const b=m.userData.baseOpacity;
      if(b!==undefined && m.opacity>b*k+1e-4) bad.push(def.name+' '+o.type+' opacity '+m.opacity.toFixed(3)+'>'+(b*k).toFixed(3));
    });
    // —— 水等着色器必须登记进 fogShaders（自定义着色器不吃雾，需手动同步）——
    if(def.name==='舴艋载愁'){
      A(fogShaders.length>0,'海面等着色器未登记雾同步');
      A(fogShaders[fogShaders.length-1].uFogColor && typeof fogShaders[fogShaders.length-1].uFogDensity.value==='number','雾同步 uniform 不完整');
    }
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1); SKYcur=skyTo; applySky();
    A(isFinite(SKYcur.fd)&&SKYcur.fd>0&&SKYcur.fd<=0.0072,'境 '+def.name+' 雾密度越界：'+SKYcur.fd);
    setFade(obj.group,1);
    disposeGroup(obj.group); scene.remove(obj.group);
    out.push('境'+i+' '+def.name+'  mesh='+meshes+' points='+points+' sprite='+sprites+' line='+lines+' light='+lights+
      ' 三角面≈'+Math.round(tris)+' drawCall代理≈'+calls+' fog='+SKYcur.fd+(obj.click?' [可点击]':''));
  }
  A(bad.length===0,'每帧写 opacity/intensity 未乘 fadeK：'+bad.slice(0,4).join(' | '));
  out.push('逐境 fadeK 合规（opacity/intensity 均 ≤ base×fadeK）[OK]');
  // —— 交互接线：pointerdown（第六境·天下归心）——
  const pd=renderer.domElement._h.pointerdown;
  A(typeof pd==='function','未接线 pointerdown');
  { const obj=STAGES[2].build(); scene.add(obj.group); setFade(obj.group,1);
    curStageObj=obj; state='stage'; curIdx=2;
    for(let f=0;f<60;f++){ stageT+=0.05; obj.update(stageT,0.05); }   // 走过交互冷却期
    pd(); A(obj.clicked===true,'末境 pointerdown 应触发交互');
    disposeGroup(obj.group); scene.remove(obj.group); }
  out.push('交互接线 pointerdown 末境（长车踏破）[OK]');
  // —— 封面 → 自动游览 → 终章（真实 animate 驱动，autoMode 默认开）——
  goto(0); state='stage';
  $('#enterBtn')._h.click();                       // 入境
  let frames=0;
  while(frames<24000 && state!=='ending'){ __clock.t+=16.7; animate(); frames++; }
  A(state==='ending','自动游览应自行走到终章（跑了 '+frames+' 帧）');
  A($('#ending').classList.contains('show'),'终章遮罩应显示');
  out.push('封面→自动游览→终章 无人值守全程走完（'+frames+' 帧 ≈ '+(frames*0.0167).toFixed(1)+'s）[OK]');
  // —— showEnding 守卫：非 stage 状态不得重入 ——
  const st0=state; showEnding(); A(state===st0,'showEnding 守卫失效（非 stage 时不应重入）');
  out.push('showEnding 守卫（state!==stage 直接返回）[OK]');
  // —— 键盘：ArrowLeft / Space（末境交互门控）/ Escape ——
  const kd=window._h.keydown;
  A(typeof kd==='function','未接线 keydown');
  state='stage'; curIdx=${N};
  kd({code:'ArrowLeft',preventDefault(){}});
  A(curIdx===${N - 1}||state==='transition','ArrowLeft 应回退一境');
  A(curIdx!==${N},'ArrowLeft 不应停在末境');
  { const obj=STAGES[2].build(); scene.add(obj.group); setFade(obj.group,1);
    curStageObj=obj; state='stage'; curIdx=2;
    for(let f=0;f<60;f++){ stageT+=0.05; obj.update(stageT,0.05); }   // 走过交互冷却期
    kd({code:'Space',preventDefault(){}});           // 第一次空格：触发交互（不跳境）
    A(obj.clicked===true&&state==='stage','末境首次空格应只触发交互');
    kd({code:'Space',preventDefault(){}});           // 第二次空格：进终章
    A(state==='ending','已交互后再按空格应进终章');
    disposeGroup(obj.group); scene.remove(obj.group); }
  kd({code:'Escape',preventDefault(){}});
  out.push('键盘 ← / 空格（末境交互门控：先交互、再按进终章）/ Esc 接线 [OK]');
  // —— 终章按钮 + 小测全流程 ——
  state='stage'; hideEnding('start');
  A(curIdx===1&&(state==='stage'||state==='transition'),'hideEnding(start) 应回到第一境');
  state='stage';
  hideEnding('cover');
  A(curIdx===0&&(state==='stage'||state==='transition'),'hideEnding(cover) 应回到封面');
  goto(1); state='stage';
  startQuiz(); A($('#quiz').classList.contains('show'),'小测面板应显示');
  for(let q=0;q<QUIZ.length;q++){
    qIdx=q; renderQuiz();
    const body=$('#quizBody');
    const opts=body.children.filter(c=>c.className==='opt');
    const batch=opts.slice(-3);
    A(batch.length===3,'第'+(q+1)+'题应有 3 个选项');
    batch[QUIZ[q].a]._h.click();                   // 点正确项
    const nx=body.children.filter(c=>c.id==='quizNext');
    A(nx.length>0,'应出现下一题按钮');
    nx[nx.length-1]._h.click();
  }
  A(qScore===QUIZ.length,'小测满分应有 '+QUIZ.length+' 分，实得 '+qScore);
  A(String($('#quizBody').innerHTML).indexOf('quizResult')>=0,'应渲染结果页');
  out.push('小测 '+QUIZ.length+' 题全流程（答题→判分→结果页）[OK] score='+qScore);
  // —— 相机/场景数值健康 ——
  A(isFinite(camera.position.x)&&isFinite(camera.position.y)&&isFinite(camera.position.z),'相机位置出现 NaN');
  out.push('相机无 NaN [OK]');
  window.__SMOKE=out.join('\\n');
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__SMOKE).split('\n').map(l => '  ✓ ' + l).join('\n'));
} else fails++;

/* [5] 交付物完整性（与 accept.js 口径一致） */
console.log('[5] 交付物完整性 …');
const audioDir = path.join(DIR, 'audio');
const need = Number(vm.runInContext('POEM.length', sandbox)) + 2;
const have = fs.existsSync(audioDir) ? fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length : 0;
if (have === need) ok('audio/ ' + have + ' 个 MP3 = read 句数+2 (' + need + ')');
else { console.error('  ! audio/ 有 ' + have + ' 个 MP3，应为 ' + need + '（先跑 gen-voice-edge.py）'); warns++; }
const htmlChecks = [
  [/autoMode=true/, 'autoMode 默认 true'],
  [/id="btnAuto" class="on">自动游览 · 开/, '自动游览按钮默认 .on + 文案「自动游览 · 开」'],
  [/galLink[\s\S]*返回诗集目录/, '封面返回诗集目录链接'],
  [/id="btnCover"[\s\S]*galLink[\s\S]*诗集目录/, '终章返回诗集目录链接'],
  [/\.galLink\{display:inline-block/, '.galLink 样式已注入 </style> 前'],
  [new RegExp('clamp[(]i,0,' + N + '[)]'), 'goto clamp(i,0,' + N + ')'],
  [/'03\.mp3'/, '全诗音频 03.mp3'],
  [/--gold:#93a8c4/, '--gold = 分配强调色 #93a8c4'],
  [/curIdx===2&&state==='stage'&&curStageObj/, '交互境 curIdx===2 接线'],
  [/background:#0d1117/, '赛道底色 #0d1117'],
  [/舴艋/, '舴艋 在位'],
  [/双溪春尚好/, '双溪春尚好 在位'],
  [/将进酒|万古愁/, '无《将进酒》残留（应为 false）'],
  [/makeRange\(/, '使用多峰山脊 makeRange'],
  [/makeForeground\(/, '使用前景框景 makeForeground'],
  [/makeFigure\(/, '使用唐装人物 makeFigure'],
  [/makeCrowd\(/, '使用远景人影 makeCrowd'],
];
htmlChecks.forEach(([re, m]) => {
  const hit = re.test(html);
  const want = m.indexOf('应为 false') >= 0 ? !hit : hit;
  want ? ok(m) : bad(m);
});

console.log(fails === 0
  ? '\nSMOKE PASS —— 全生命周期（含自动游览、末境交互门控、小测、fadeK 合规、三层构图）真实执行无异常' + (warns ? '（有 ' + warns + ' 项提醒）' : '')
  : '\nSMOKE FAIL —— ' + fails + ' 处异常');
process.exit(fails === 0 ? 0 : 1);
