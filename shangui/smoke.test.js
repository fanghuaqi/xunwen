#!/usr/bin/env node
/* smoke.test.js —— 《山鬼》深度冒烟测试
 *
 * 在 Node vm 中装载 THREE（本地 three.min.js 真 r128），配「真实 classList / 事件登记 / 画布 2D」DOM 桩，
 * 执行主脚本顶层后真实跑：
 *   1) 顶层安全（THREE 未加载时不炸）
 *   2) boot() 全流程（WebGLRenderer 打桩）→ 逐境 build()/update()×400 帧/onEnter/click×2
 *   3) goto() 跨场运镜 + mixSky + setFade/disposeGroup 全生命周期
 *   4) 封面 → 自动游览（autoMode 默认开）→ 终章 → 小测，一路真实驱动 animate()
 *   5) 交互接线：pointerdown 第三境（山巅现豹）/第七境（雷雨）、空格先交互再进终章
 *   6) NaN 扫描 + fadeK 覆盖（每帧写 opacity/intensity 处须乘 fadeK）
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
const warn = m => { console.log('  ! ' + m); warns++; };

/* ---------------- 引擎：真 THREE r128 ---------------- */
let engineSrc = '';
const localThree = path.join(DIR, 'three.min.js');
const threePath = fs.existsSync(localThree) ? localThree : path.join(DIR, '..', '_pipeline', 'vendor', 'three.min.js');
if (fs.existsSync(threePath)) engineSrc = fs.readFileSync(threePath, 'utf8');
console.log('[1] 引擎：' + (engineSrc ? '真 THREE r128（本地 three.min.js）' : 'THREE 桩'));

/* ---------------- DOM 桩（元素按选择器缓存，事件可回放） ---------------- */
function ctx2d() {
  return { createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {},
    beginPath() {}, arc() {}, ellipse() {}, fill() {}, stroke() {}, translate() {}, rotate() {},
    quadraticCurveTo() {}, moveTo() {}, lineTo() {},
    fillStyle: '', strokeStyle: '', lineWidth: 1, lineCap: '', font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0 };
}
function makeEl(tag) {
  const cls = new Set();
  const el = {
    tag, id: '', className: '', children: [], _h: {},
    style: { setProperty(k, v) { this[k] = v; }, removeProperty() {} },
    textContent: '', innerHTML: '', open: false, offsetWidth: 0, disabled: false, title: '',
    classList: {
      add: c => cls.add(c), remove: c => cls.delete(c),
      contains: c => cls.has(c),
      toggle: (c, f) => { const on = f === undefined ? !cls.has(c) : !!f; on ? cls.add(c) : cls.delete(c); return on; },
      _set: cls,
    },
    addEventListener(t, f) { el._h[t] = f; }, removeEventListener() {},
    appendChild(c) { el.children.push(c); return c; },
    querySelectorAll() { return el.children.filter(c => c.className && String(c.className).indexOf('opt') === 0); },
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

/* [2] 顶层安全 */
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
  A(STAGES.length===8,'境数应为 8（封面 + 7 境），实为 '+STAGES.length);
  for(let i=1;i<STAGES.length;i++) A(STAGES[i].name===POEM[i-1].name,'境名错位 @'+i+' '+STAGES[i].name+' vs '+POEM[i-1].name);
  A(CN.length>=POEM.length,'CN 中文数字数组太短');
  A(autoMode===true,'自动游览应默认开启');
  A(QUIZ.length>=5,'小测应≥5题');
  // —— WebGLRenderer 打桩（Node 无 GL），boot() 全流程真实执行 ——
  THREE.WebGLRenderer=function(){ return {
    setPixelRatio(){}, setSize(){}, setClearColor(){}, render(){},
    domElement:{ _h:{}, addEventListener(t,f){ this._h[t]=f; } },
  }; };
  boot();
  A(state==='stage','boot 后应处于 stage');
  A(curIdx===0,'boot 后应在封面境');
  // —— 逐境深测（真 THREE 建几何/材质/着色器）——
  const stats=[];
  for(let i=0;i<STAGES.length;i++){
    const def=STAGES[i];
    const obj=def.build();
    scene.add(obj.group); setFade(obj.group,1); obj.group.userData.fadeK=1;
    let meshes=0,points=0,lights=0,sprites=0,tris=0;
    obj.group.traverse(o=>{
      if(o.isMesh)meshes++; if(o.isPoints)points++; if(o.isLight)lights++; if(o.isSprite)sprites++;
      if(o.geometry&&o.geometry.attributes&&o.geometry.attributes.position){
        const g=o.geometry, n=g.index?g.index.count:g.attributes.position.count;
        tris+=Math.floor(n/3)*(o.count||1);
      }
    });
    A(meshes>0,'境 '+def.name+' 应至少有一个 Mesh');
    // NaN 扫描：几何顶点
    let nanGeo=0;
    obj.group.traverse(o=>{
      if(o.geometry&&o.geometry.attributes&&o.geometry.attributes.position){
        const a=o.geometry.attributes.position.array;
        for(let k=0;k<a.length;k+=Math.max(1,Math.floor(a.length/240))){ if(!isFinite(a[k]))nanGeo++; }
      }
    });
    A(nanGeo===0,'境 '+def.name+' 几何出现 NaN 顶点 '+nanGeo+' 个');
    for(let f=0;f<400;f++){ stageT+=0.05; if(obj.update)obj.update(stageT,0.05); }
    if(obj.onEnter)obj.onEnter();
    if(obj.click){ obj.click(); for(let f=0;f<60;f++){ stageT+=0.05; obj.update(stageT,0.05); } obj.click(); }
    A(isFinite(obj.group.position.x),'境 '+def.name+' group 位置 NaN');
    // fadeK 覆盖：group 内每个材质的 opacity / uniform 必须已淡出到 0
    setFade(obj.group,0);
    let leak=0, checked=0;
    obj.group.traverse(o=>{
      if(o.isLight){ checked++; if(Math.abs(o.intensity)>1e-6)leak++; return; }
      const m=o.material; if(!m)return;
      if(m.isShaderMaterial){ if(m.uniforms&&m.uniforms.uFade){ checked++; if(m.uniforms.uFade.value>1e-6)leak++; } return; }
      checked++; if(m.opacity>1e-6)leak++;
    });
    A(leak===0,'境 '+def.name+' fadeK=0 时仍有 '+leak+'/'+checked+' 个材质没淡出（未乘 fadeK）');
    setFade(obj.group,1);
    skyFrom=cloneSky(SKYcur); skyTo=def.sky(); mixSky(0.5); mixSky(1); SKYcur=skyTo; applySky();
    setFade(obj.group,0.3); setFade(obj.group,1);
    disposeGroup(obj.group); scene.remove(obj.group);
    stats.push('境'+i+' '+def.name+' mesh='+meshes+' points='+points+' sprite='+sprites+' light='+lights+' tris≈'+tris+(obj.click?' [可点击]':''));
  }
  out.push(...stats);
  // 三角面 / 场景规模预算
  const total=stats.map(s=>({n:s.split(' ')[1],t:Number((s.match(/tris≈(\\d+)/)||[])[1]||0)}));
  const heavy=total.filter(x=>x.t>120000);
  A(heavy.length===0,'超三角面预算(12万)的境: '+JSON.stringify(heavy));
  out.push('三角面预算：全部境 ≤12 万（最大 '+Math.max(...total.map(x=>x.t))+'）[OK]');
  // —— 交互接线：pointerdown（第三境 山巅现豹 / 第七境 雷雨）——
  const pd=renderer.domElement._h.pointerdown;
  A(typeof pd==='function','未接线 pointerdown');
  const st3=STAGES[3].build(); scene.add(st3.group); setFade(st3.group,1);
  curStageObj=st3; state='stage'; curIdx=3; s3Clicks=0; s3Armed=false; pd();
  A(s3Clicks===1,'第三境 pointerdown 应触发山巅交互');
  const st7=STAGES[7].build(); scene.add(st7.group); setFade(st7.group,1);
  curStageObj=st7; state='stage'; curIdx=7; s7Clicks=0; s7Armed=false;
  const kd=window._h.keydown;
  A(typeof kd==='function','未接线 keydown');
  kd({code:'Space',preventDefault(){}});
  A(s7Clicks===1,'第七境空格应先触发交互（雷雨）');
  A(state==='stage','第七境空格触发交互后不应立即跳境');
  kd({code:'Space',preventDefault(){}});
  A(state==='ending','第七境再按空格应进终章');
  out.push('交互接线 pointerdown/空格（第三境山巅·第七境雷雨），空格先交互再进终章 [OK]');
  // —— 封面 → 自动游览 → 终章（真实 animate 驱动，autoMode 默认开）——
  goto(0); state='stage';
  $('#enterBtn')._h.click();
  let frames=0;
  while(frames<25000 && state!=='ending'){ __clock.t+=16.7; animate(); frames++; }
  A(state==='ending','自动游览应自行走到终章（跑了 '+frames+' 帧）');
  A($('#ending').classList.contains('show'),'终章遮罩应显示');
  out.push('封面→自动游览→终章 无人值守全程走完（'+frames+' 帧 ≈ '+(frames*0.0167).toFixed(1)+'s）[OK]');
  // —— showEnding 守卫 ——
  const st0=state; showEnding(); A(state===st0,'showEnding 守卫失效（非 stage 时不应重入）');
  // —— 键盘 ——
  state='stage';
  kd({code:'ArrowLeft',preventDefault(){}});
  A(curIdx===7||state==='transition','ArrowLeft 应回退一境');
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
  out.push('小测流程 startQuiz/renderQuiz/showResult（'+QUIZ.length+' 题）[OK]');
  // —— 相机 NaN ——
  A(isFinite(camera.position.x)&&isFinite(camera.position.y)&&isFinite(camera.position.z),'相机位置出现 NaN');
  // —— 诗句/注音一致性 ——
  for(let i=0;i<POEM.length;i++){
    POEM[i].segs.forEach(seg=>{
      const han=[...seg.c].filter(c=>!/[，。、！？；：…—·]/.test(c)).length;
      A(han===seg.p.length,'第'+(i+1)+'句「'+seg.c+'」汉字'+han+'≠拼音'+seg.p.length);
    });
  }
  out.push('逐句汉字数 = 拼音数（7 境 '+POEM.reduce((a,l)=>a+l.segs.length,0)+' 段）[OK]');
  // —— 诗文与 queue 权威文本逐字比对 ——
  const expect='若有人兮山之阿，被薜荔兮带女萝。既含睇兮又宜笑，子慕予兮善窈窕。乘赤豹兮从文狸，辛夷车兮结桂旗。被石兰兮带杜衡，折芬馨兮遗所思。余处幽篁兮终不见天，路险难兮独后来。表独立兮山之上，云容容兮而在下。杳冥冥兮羌昼晦，东风飘兮神灵雨。留灵修兮憺忘归，岁既晏兮孰华予。采三秀兮于山间，石磊磊兮葛蔓蔓。怨公子兮怅忘归，君思我兮不得闲。山中人兮芳杜若，饮石泉兮荫松柏。君思我兮然疑作。雷填填兮雨冥冥，猿啾啾兮狖夜鸣。风飒飒兮木萧萧，思公子兮徒离忧。';
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  A(joined===expect,'诗文与权威文本不一致');
  out.push('诗文逐字 = queue.json 权威文本 [OK]');
  window.__SMOKE=out.join('\\n');
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__SMOKE).split('\n').map(l => '  ✓ ' + l).join('\n'));
} else fails++;

/* [5] 交付物完整性（与 accept.js 同口径） */
console.log('[5] 交付物完整性 …');
const audioDir = path.join(DIR, 'audio');
const need = Number(vm.runInContext('POEM.length', sandbox)) + 2;
const have = fs.existsSync(audioDir) ? fs.readdirSync(audioDir).filter(f => f.endsWith('.mp3')).length : 0;
if (have === need) ok('audio/ ' + have + ' 个 MP3 = read 句数+2 (' + need + ')');
else warn('audio/ 有 ' + have + ' 个 MP3，应为 ' + need + '（先跑 gen-voice-edge.py）');
const htmlChecks = [
  [/autoMode=true/, 'autoMode 默认 true'],
  [/id="btnAuto" class="on">自动游览 · 开/, '自动游览按钮默认 .on + 文案「自动游览 · 开」'],
  [/galLink[\s\S]*返回诗集目录/, '封面返回诗集目录链接'],
  [/id="btnCover"[\s\S]*galLink[\s\S]*诗集目录/, '终章返回诗集目录链接'],
  [/clamp\(i,0,7\)/, 'goto clamp(i,0,7)'],
  [/'08\.mp3'/, '全诗音频 08.mp3'],
  [/curIdx===3&&state==='stage'/, '交互境 curIdx===3（山巅现豹）'],
  [/curIdx===7&&state==='stage'/, '交互境 curIdx===7（雷雨）'],
  [/--gold:#7fa88f/, '--gold = 分配强调色 #7fa88f'],
  [/background:#0d1117/, 'body 背景为水墨赛道底色 #0d1117'],
];
htmlChecks.forEach(([re, m]) => re.test(html) ? ok(m) : bad(m));
const resi = ['将进酒', '万古愁', '如见太白', '深得太白'].filter(s => code.includes(s));
resi.length ? bad('残留字样: ' + resi.join('、')) : ok('无《将进酒》残留字样');

console.log(fails === 0
  ? '\nSMOKE PASS —— 全生命周期（含自动游览、交互、小测、fadeK、NaN）真实执行无异常' + (warns ? '（有 ' + warns + ' 项提醒）' : '')
  : '\nSMOKE FAIL —— ' + fails + ' 处异常');
process.exit(fails === 0 ? 0 : 1);
