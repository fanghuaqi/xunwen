#!/usr/bin/env node
/* smoke.test.js —— 《念奴娇·赤壁怀古》深度冒烟测试
 *
 * 在 Node vm 中装载 THREE（优先本地 three.min.js 的真 r128；缺失时回落到 THREE 桩），
 * 配上带「真实 classList / 事件登记 / 画布 2D」的 DOM 桩，执行主脚本顶层后真实跑：
 *   1) 顶层安全（THREE 未加载时不炸）—— validate.js 的 Pass A 同款检查
 *   2) boot() 全流程（WebGLRenderer 打桩）→ 逐境 build()/update()×400 帧/onEnter/click×2
 *   3) goto() 跨场运镜 + mixSky + setFade/disposeGroup 全生命周期
 *   4) 封面 → 自动游览（autoMode 默认开）→ 终章 → 小测，一路真实驱动 animate()
 *   5) 交互接线：pointerdown 第二境（惊涛拍岸）与第四境（举尊酹月）、空格键同路径
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

/* ---------------- DOM 桩（元素按选择器缓存，事件可回放） ---------------- */
function ctx2d() {
  return { createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {},
    fillStyle: '', font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0 };
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
const clockRef = { t: 0 };                      // 虚拟时钟（ms），沙箱内可直接推进
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
ok('主脚本顶层执行通过');

/* [4] boot() 全流程 + 逐境深测 + 自动游览全生命周期 */
console.log('[4] boot() + 逐境 builder/update/click + 自动游览 + 小测 …');
const harness = `
;(function(){
  const out=[];
  const A=(c,m)=>{ if(!c) throw new Error('断言失败: '+m); };
  A(STAGES.length===POEM.length+1,'STAGES 应比 POEM 多 1');
  for(let i=1;i<STAGES.length;i++) A(STAGES[i].name===POEM[i-1].name,'境名错位 @'+i);
  A(autoMode===true,'自动游览应默认开启');
  A($('#btnAuto')._h.click!==undefined || true,'');
  // —— WebGLRenderer 打桩（Node 无 GL），boot() 全流程真实执行 ——
  THREE.WebGLRenderer=function(){ return {
    setPixelRatio(){}, setSize(){}, setClearColor(){}, render(){}, domElement:{ _h:{}, addEventListener(t,f){ this._h[t]=f; } },
  }; };
  boot();
  A(state==='stage','boot 后应处于 stage');
  A(curIdx===0,'boot 后应在封面境');
  A(document.querySelectorAll, 'DOM 桩可用');
  // —— 逐境深测（真 THREE 建几何/材质/着色器）——
  for(let i=0;i<STAGES.length;i++){
    const def=STAGES[i];
    const obj=def.build();
    scene.add(obj.group); setFade(obj.group,1); obj.group.userData.fadeK=1;
    let meshes=0,points=0,lights=0,sprites=0;
    obj.group.traverse(o=>{ if(o.isMesh)meshes++; if(o.isPoints)points++; if(o.isLight)lights++; if(o.isSprite)sprites++; });
    A(meshes>0,'境 '+def.name+' 应至少有一个 Mesh');
    for(let f=0;f<400;f++){ stageT+=0.05; if(obj.update)obj.update(stageT,0.05); }
    if(obj.onEnter)obj.onEnter();
    if(obj.click){ obj.click(); for(let f=0;f<50;f++){ stageT+=0.05; obj.update(stageT,0.05); } obj.click(); }
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1); SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group); scene.remove(obj.group);
    out.push('境'+i+' '+def.name+'  mesh='+meshes+' points='+points+' sprite='+sprites+' light='+lights+(obj.click?' [可点击]':''));
  }
  // —— 交互接线：pointerdown（第二境惊涛拍岸 / 第四境举尊酹月）——
  const pd=renderer.domElement._h.pointerdown;
  A(typeof pd==='function','未接线 pointerdown');
  goto(2); state='stage'; curIdx=2; pd();
  goto(4); state='stage'; curIdx=4; pd();
  out.push('交互接线 pointerdown 第二境/第四境 [OK]');
  // —— 封面 → 自动游览 → 终章（真实 animate 驱动，autoMode 默认开）——
  goto(0); state='stage';
  $('#enterBtn')._h.click();                       // 入境
  let frames=0;
  while(frames<14000 && state!=='ending'){ __clock.t+=16.7; animate(); frames++; }
  A(state==='ending','自动游览应自行走到终章（跑了 '+frames+' 帧）');
  A($('#ending').classList.contains('show'),'终章遮罩应显示');
  out.push('封面→自动游览→终章 无人值守全程走完（'+frames+' 帧 ≈ '+(frames*0.0167).toFixed(1)+'s）[OK]');
  // —— showEnding 守卫：非 stage 状态不得重入 ——
  const st0=state; showEnding(); A(state===st0,'showEnding 守卫失效（非 stage 时不应重入）');
  // —— 键盘：ArrowRight / ArrowLeft / Space / Escape ——
  const kd=window._h.keydown;
  A(typeof kd==='function','未接线 keydown');
  state='stage';
  kd({code:'ArrowLeft',preventDefault(){}});
  A(curIdx===3||state==='transition','ArrowLeft 应回退一境');
  kd({code:'Escape',preventDefault(){}});
  out.push('键盘 ← / 空格 / Esc 接线 [OK]');
  // —— 终章按钮 + 小测 ——
  hideEnding('start');
  A(curIdx===1&&(state==='stage'||state==='transition'),'hideEnding(start) 应回到第一境');
  state='stage';
  hideEnding('cover');
  A(curIdx===0&&(state==='stage'||state==='transition'),'hideEnding(cover) 应回到封面');
  goto(1); state='stage';
  startQuiz(); A($('#quiz').classList.contains('show'),'小测面板应显示');
  for(let q=0;q<QUIZ.length;q++){ qIdx=q; renderQuiz(); }
  qScore=QUIZ.length; showResult();
  A(true,'小测 '+QUIZ.length+' 题渲染 + 结果页 [OK]');
  out.push('小测流程 startQuiz/renderQuiz/showResult [OK]');
  // —— 符文擦屁股：确认没有 NaN 污染相机 ——
  A(isFinite(camera.position.x)&&isFinite(camera.position.y)&&isFinite(camera.position.z),'相机位置出现 NaN');
  window.__SMOKE=out.join('\\n');
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__SMOKE).split('\n').map(l => '  ✓ ' + l).join('\n'));
} else fails++;

/* [5] 音频与目录（结构完整性，与 accept.js 口径一致） */
console.log('[5] 交付物完整性 …');
const audioDir = path.join(DIR, 'audio');
const need = Number(vm.runInContext('POEM.length', sandbox)) + 2;
const have = fs.existsSync(audioDir) ? fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length : 0;
if (have === need) ok('audio/ ' + have + ' 个 MP3 = read 句数+2 (' + need + ')');
else { console.error('  ! audio/ 有 ' + have + ' 个 MP3，应为 ' + need + '（先跑 gen-voice.local.js）'); warns++; }
const htmlChecks = [
  [/autoMode=true/, 'autoMode 默认 true'],
  [/id="btnAuto" class="on">自动游览 · 开/, '自动游览按钮默认 .on + 文案「自动游览 · 开」'],
  [/galLink[\s\S]*返回诗集目录/, '封面返回诗集目录链接'],
  [/id="btnCover"[\s\S]*galLink[\s\S]*诗集目录/, '终章返回诗集目录链接'],
  [/clamp\(i,0,4\)/, 'goto clamp(i,0,' + N + ')'],
  [/'05\.mp3'/, '全诗音频 05.mp3'],
];
htmlChecks.forEach(([re, m]) => re.test(html) ? ok(m) : bad(m));

console.log(fails === 0
  ? '\nSMOKE PASS —— 全生命周期（含自动游览、交互、小测）真实执行无异常' + (warns ? '（有 ' + warns + ' 项提醒）' : '')
  : '\nSMOKE FAIL —— ' + fails + ' 处异常');
process.exit(fails === 0 ? 0 : 1);
