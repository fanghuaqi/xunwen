#!/usr/bin/env node
/* smoke-test.js —— 《惠崇春江晚景》深度冒烟测试
 * 真实 THREE r128（本地 three.min.js，缺失时从 shu-huyin 同款源下载）+ 最小 DOM 桩，Node vm 执行主脚本；
 * 仅 WebGLRenderer 用桩（Node 无 WebGL 上下文），其余 Scene/Mesh/Camera/材质全为真实 THREE。
 * 真实运行：boot 全路径（含 pointerdown/空格/控件接线注册）、4 境 build/update、
 * 境③ click×3（2.2s 防连点守卫）、goto/showEnding/小测、逐境独立 build+sky+淡出销毁。
 * 用法: node smoke-test.js   （退出码 0 = 全部通过）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = __dirname;
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
const TEXT = '竹外桃花三两枝，春江水暖鸭先知。蒌蒿满地芦芽短，正是河豚欲上时。';

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
  const listeners = {};
  const el = {
    tag, children: [], style: {}, textContent: '', innerHTML: '', className: '', id: '', open: false,
    listeners,
    addEventListener(t, f) { (listeners[t] = listeners[t] || []).push(f); },
    removeEventListener() {},
    dispatch(t, ev2) { (listeners[t] || []).forEach(f => f(ev2)); },
    appendChild(c) { el.children.push(c); return c; },
    querySelectorAll() { return []; }, querySelector() { return elStub('x'); },
    classList: { add() {}, remove() {}, toggle() { return false; }, contains() { return false; } },
    offsetWidth: 0, disabled: false, title: '',
  };
  return el;
}
const elCache = {};
const doc = {
  querySelector: s => elCache[s] || (elCache[s] = elStub(s)), querySelectorAll: () => [],
  createElement: tag => tag === 'canvas'
    ? Object.assign(elStub('canvas'), { width: 64, height: 64, getContext: () => ctx2d() })
    : elStub(tag),
  addEventListener() {}, documentElement: elStub('html'), body: elStub('body'),
  head: elStub('head'), activeElement: null, fullscreenElement: null,
};
const winListeners = {};
let NOW = 0; const rafQ = [];
const sandbox = {
  document: doc, console,
  performance: { now: () => NOW },
  requestAnimationFrame(f) { rafQ.push(f); return rafQ.length; },
  setTimeout() { return 0; }, clearTimeout() {},
  location: { reload() {} }, navigator: { userAgent: 'node' },
  innerWidth: 1280, innerHeight: 720, devicePixelRatio: 1,
};
sandbox.window = sandbox;
sandbox.self = sandbox;
sandbox.globalThis = sandbox;
sandbox.addEventListener = (t, f) => { (winListeners[t] = winListeners[t] || []).push(f); };

const frames = (n, step = 33) => {
  for (let i = 0; i < n; i++) { NOW += step; const f = rafQ.shift(); if (f) f(); }
};

let fails = 0;
const run = (src, name) => {
  try { vm.runInContext(src, sandbox, { filename: name }); return true; }
  catch (e) { console.error('  ✗ ' + name + ': ' + (e && e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e)); fails++; return false; }
};
const ev = expr => vm.runInContext(expr, sandbox, { filename: 'eval' });
const safeEv = expr => { try { return ev(expr); } catch (e) { console.error('  ✗ eval: ' + e.message); fails++; return undefined; } };
const assert = (name, ok, extra) => {
  console.log((ok ? '  ✓ ' : '  ✗ ') + name + (extra ? ' :: ' + extra : ''));
  if (!ok) fails++;
};

vm.createContext(sandbox);

console.log('[1] 加载 THREE r128 …');
if (!run(threeSrc, 'three.min.js')) process.exit(1);
if (!run('if(!window.THREE)throw new Error("THREE 未挂载")', 'check THREE')) process.exit(1);
/* Node 无 WebGL 上下文：仅换掉 WebGLRenderer（自包含桩，不引用宿主函数），
   让 boot() 全路径真实执行 —— 场景图/相机/天空/材质全是真实 THREE */
run('THREE.WebGLRenderer=class{constructor(){const L={};'
  + 'this.domElement={_ls:L,addEventListener(t,f){(L[t]=L[t]||[]).push(f);}};}'
  + 'setPixelRatio(){} setSize(){} setClearColor(){} render(){} dispose(){} }', 'renderer shim');

console.log('[2] 执行主脚本顶层 …');
if (!run(code, 'main')) process.exit(1);

console.log('[3] 数据断言 …');
assert('POEM 拼接 === 清单 text', safeEv('POEM.map(l=>l.segs.map(s=>s.c).join("")).join("")') === TEXT);
assert('POEM 3 句 / STAGES 4 项', safeEv('POEM.length') === 3 && safeEv('STAGES.length') === 4);
assert('境名对齐', safeEv('STAGES.slice(1).every((s,i)=>s.name===POEM[i].name)'));
assert('read 字段 3 处', (code.match(/read:'/g) || []).length === 3);
assert('多音字注音抽查（蒌蒿 lóu hāo / 芦 lú / 豚 tún）', (() => {
  const all = safeEv('JSON.stringify(POEM.map(l=>l.segs.map(s=>s.p.join(" ")).join(" | ")))') || '';
  return all.includes('lóu hāo') && all.includes('lú yá') && all.includes('tún');
})());
assert('QUIZ 5 题 / 3 选项 / 答案合法', (() => {
  const q = safeEv('JSON.parse(JSON.stringify(QUIZ.map(x=>({o:x.o,a:x.a}))))');
  return Array.isArray(q) && q.length === 5 && q.every(x => x.o.length === 3 && Number.isInteger(x.a) && x.a >= 0 && x.a < 3);
})());
assert('words 6 项（题数+1）', (() => {
  const m = code.match(/const words=\[([^\]]*)\]/);
  return !!m && m[1].split(',').length === 6;
})());
assert('交互接线 curIdx===3 恰 2 处（pointerdown+空格）',
  (code.match(/curIdx===3&&state==='stage'/g) || []).length === 2);

console.log('[4] boot + 全链路运行 …');
run('initApp()', 'initApp');
assert('boot 后封面在跑', safeEv('state') === 'stage' && safeEv('curIdx') === 0);
frames(30);

const enterBtn = doc.querySelector('#enterBtn');
enterBtn.dispatch('click', { preventDefault() {}, currentTarget: enterBtn });
frames(160);
assert('入境 → 第1境完成过渡', safeEv('state') === 'stage' && safeEv('curIdx') === 1);
frames(400);
for (const i of [2, 3]) {
  run('goto(' + i + ')', 'goto ' + i);
  frames(200);
  assert('goto(' + i + ') → stage', safeEv('state') === 'stage' && String(safeEv('curIdx')) === String(i));
}
frames(400); // 让境②标志性瞬间（群鸭跃水时间线）走一段
console.log('  （境②群鸭跃水时间线已推进 ' + (400 * 33 / 1000).toFixed(1) + 's）');

console.log('[5] 交互境专项：click×3（2.2s 守卫）+ pointerdown + 空格双接线 …');
const fire = () => { run('curStageObj&&curStageObj.click&&curStageObj.click()', 'click'); };
fire();
frames(40);
const flashEl = doc.querySelector('#flash');
assert('click → 题字「春江水暖鸭先知」', flashEl.textContent === '春江水暖鸭先知', JSON.stringify(flashEl.textContent));
fire(); // 2.2s 守卫内：不应重复触发（无异常即通过）
frames(40);
frames(500); // >2.2s，守卫解除
fire();      // 第二次触发
frames(240);
run("(renderer.domElement._ls['pointerdown']||[]).forEach(f=>f({}))", 'pointerdown wiring'); // 接线①
frames(500);
(winListeners['keydown'] || []).forEach(f => f({ code: 'Space', preventDefault() {} }));     // 接线②：空格
frames(500);
(winListeners['keydown'] || []).forEach(f => f({ code: 'ArrowRight', preventDefault() {} })); // 末境右键 → 终章
frames(30);
assert('ArrowRight 于末境进入终章', safeEv('state') === 'ending');
(winListeners['keydown'] || []).forEach(f => f({ code: 'Escape', preventDefault() {} }));

console.log('[6] 每境独立 build/update + sky 工厂 + 淡出销毁 …');
for (let i = 0; i < 4; i++) {
  const ok = safeEv('(function(){const d=STAGES[' + i + '];const o=d.build();'
    + 'if(!o.group)throw new Error("无 group");'
    + 'scene.add(o.group);setFade(o.group,1);o.group.userData.fadeK=1;'
    + 'for(let f=0;f<240;f++){stageT+=0.033;if(o.update)o.update(stageT,0.033);applySky();}'
    + 'const k=d.sky();if(!k.top||!k.hor||!k.fog||typeof k.fd!=="number"||!k.moon)throw new Error("sky 字段不全");'
    + 'if(o.click)o.click();'
    + 'setFade(o.group,0.3);setFade(o.group,1);disposeGroup(o.group);scene.remove(o.group);'
    + 'return true;})()');
  assert('STAGES[' + i + '] ' + safeEv('STAGES[' + i + '].name') + ' build/update/sky/click/dispose', ok === true);
}

console.log('[7] 终章 + 小测 …');
run('goto(3)', 'goto 3'); frames(200);
run('showEnding()', 'showEnding');
run('startQuiz()', 'startQuiz');
run('for(let i=0;i<QUIZ.length;i++){qIdx=i;renderQuiz();}showResult()', 'quiz loop');
frames(60);
run('goto(0)', 'goto 0'); frames(140);
assert('回到封面正常', safeEv('state') === 'stage' && safeEv('curIdx') === 0);

if (fails === 0) console.log('\nSMOKE PASS —— boot/接线/build/update/click/goto 全路径真实执行无异常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处失败'); process.exit(1); }
