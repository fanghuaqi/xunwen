#!/usr/bin/env node
/* smoke.test.js —— 《白雪歌送武判官归京》冒烟测试
 * 真实 THREE r128（本地 three.min.js）+ DOM 桩，在 Node vm 中执行主脚本，
 * 真实走 boot → 逐境（含过渡完成）→ 交互境点击 → 终章 → 回封面 全流程；
 * 每境扫描 NaN（uniform 数值 / opacity）与 fadeK 越界；核对多音字注音与小测结构。
 * 用法: node smoke.test.js   （退出码 0 = 全部通过）
 */
'use strict';
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const DIR = __dirname;
const html = fs.readFileSync(path.join(DIR, 'index.html'), 'utf8');
const code = html.match(/<script id="main">([\s\S]*?)<\/script>/)[1];
const localThree = path.join(DIR, 'three.min.js');
const threePath = fs.existsSync(localThree) ? localThree : path.join(DIR, '..', '_pipeline', 'vendor', 'three.min.js');
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

/* ---------- DOM 桩（带事件捕获，可 fire） ---------- */
function ctx2d() {
  return { createRadialGradient: () => ({ addColorStop() {} }), fillRect() {}, fillText() {},
    fillStyle: '', font: '', textAlign: '', textBaseline: '', shadowColor: '', shadowBlur: 0 };
}
function elStub(tag) {
  const el = {
    tag, children: [], style: {}, textContent: '', innerHTML: '', className: '', id: '', open: false,
    _h: {},
    addEventListener(t, f) { (el._h[t] || (el._h[t] = [])).push(f); },
    removeEventListener() {},
    fire(t) { (el._h[t] || []).forEach(f => f({ preventDefault() {}, clientX: 0, clientY: 0, code: '', currentTarget: el })); },
    appendChild(c) { el.children.push(c); return c; },
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
let simNow = 1000;
const sandbox = {
  document: doc, console,
  performance: { now: () => (simNow += 33) },
  requestAnimationFrame() { return 0; },
  setTimeout() { return 0; }, clearTimeout() {},
  location: { reload() {} }, navigator: { userAgent: 'node' },
};
sandbox.window = sandbox;
sandbox.self = sandbox;
sandbox.globalThis = sandbox;
sandbox.addEventListener = () => {};
vm.createContext(sandbox);

let fails = 0;
const run = (src, name) => {
  try { vm.runInContext(src, sandbox, { filename: name }); return true; }
  catch (e) { console.error('  ✗ ' + name + ': ' + (e && e.stack ? e.stack.split('\n').slice(0, 3).join(' | ') : e)); fails++; return false; }
};

console.log('[1] 加载 THREE r128 …');
if (!run(threeSrc, 'three.min.js')) process.exit(1);
run('THREE.WebGLRenderer=function(){this.domElement=document.createElement("canvas");this.setPixelRatio=function(){};this.setSize=function(){};this.setClearColor=function(){};this.render=function(){};this.info={render:{calls:0,triangles:0}};}', 'stub renderer');

console.log('[2] 执行主脚本顶层 …');
if (!run(code, 'main')) process.exit(1);

console.log('[3] boot → 逐境（过渡走完）→ 交互 → 终章 → 回封面 …');
const harness = `
;(function(){
  const out=[];
  const N=6;
  // —— 诗文与清单一致性 ——
  const joined=POEM.map(l=>l.segs.map(s=>s.c).join('')).join('');
  const EXPECT='北风卷地白草折，胡天八月即飞雪。忽如一夜春风来，千树万树梨花开。散入珠帘湿罗幕，狐裘不暖锦衾薄。将军角弓不得控，都护铁衣冷难着。瀚海阑干百丈冰，愁云惨淡万里凝。中军置酒饮归客，胡琴琵琶与羌笛。纷纷暮雪下辕门，风掣红旗冻不翻。轮台东门送君去，去时雪满天山路。山回路转不见君，雪上空留马行处。';
  if(joined!==EXPECT)throw new Error('诗文不一致: '+joined);
  if(STAGES.length!==N+1)throw new Error('STAGES 应为 '+(N+1)+'（封面+'+N+'境）');
  for(let i=1;i<STAGES.length;i++)if(STAGES[i].name!==POEM[i-1].name)throw new Error('境名错位 @'+i);
  if(CN.length<POEM.length)throw new Error('CN 数字数组不足');
  if(autoMode!==true)throw new Error('autoMode 应默认开');
  if(!Array.isArray(QUIZ)||QUIZ.length!==5)throw new Error('小测应为 5 题');
  // —— 多音字注音核对 ——
  function py(i,si,ci){ return POEM[i].segs[si].p[ci]; }
  if(py(0,0,6).indexOf('zhé')!==0)throw new Error('折 应读 zhé');
  if(py(0,1,4).indexOf('jí')!==0)throw new Error('即 应读 jí');
  if(py(2,0,0).indexOf('sàn')!==0)throw new Error('散（散入）应读 sàn');
  if(py(2,1,6).indexOf('bó')!==0)throw new Error('薄 应读 bó');
  if(py(2,2,6).indexOf('kòng')!==0)throw new Error('控 应读 kòng');
  if(py(2,3,0).indexOf('dū')!==0)throw new Error('都（都护）应读 dū');
  if(py(2,3,6).indexOf('zhuó')!==0)throw new Error('着（难着）应读 zhuó');
  if(py(3,0,2).indexOf('lán')!==0)throw new Error('阑 应读 lán');
  if(py(3,1,2).indexOf('cǎn')!==0)throw new Error('惨 应读 cǎn');
  if(py(4,1,1).indexOf('chè')!==0)throw new Error('掣 应读 chè');
  if(py(4,0,5).indexOf('yuán')!==0)throw new Error('辕 应读 yuán');
  if(py(4,2,0).indexOf('lún')!==0)throw new Error('轮（轮台）应读 lún');
  // —— boot ——
  boot();
  if(state!=='stage'||curIdx!==0)throw new Error('boot 后应处于封面境');
  const frames=n=>{ for(let f=0;f<n;f++)animate(); };
  // —— NaN / fadeK 扫描 ——
  function scan(group){
    const bad=[];
    group.traverse(o=>{
      const m=o.material; if(!m)return;
      const ms=Array.isArray(m)?m:[m];
      ms.forEach(mm=>{
        if(mm.uniforms)for(const k in mm.uniforms){
          const v=mm.uniforms[k].value;
          if(typeof v==='number'&&Number.isNaN(v))bad.push('uniform '+k);
          if(v&&v.x!==undefined&&typeof v.x==='number'&&Number.isNaN(v.x+v.y+(v.z||0)))bad.push('uniform '+k+' vec');
        }
        if(typeof mm.opacity==='number'&&Number.isNaN(mm.opacity))bad.push('opacity');
        if(mm.color&&typeof mm.color.r==='number'&&Number.isNaN(mm.color.r+mm.color.g+mm.color.b))bad.push('material color');
      });
      if(o.isInstancedMesh&&o.instanceColor){
        const a=o.instanceColor.array; let nan=0;
        for(let i=0;i<a.length;i++)if(Number.isNaN(a[i]))nan++;
        if(nan)bad.push('instanceColor NaN×'+nan);
      }
    });
    return bad;
  }
  function waitStage(i){
    if(curIdx!==i)goto(i);             // 触发真实 goto（过渡中重复调用会自动跳过）
    frames(120);                       // 2.6s 过渡 ≈ 79 帧
    if(state!=='stage')throw new Error('过渡未完成 state='+state+' @'+i);
    if(curIdx!==i)throw new Error('curIdx='+curIdx+' 应为 '+i);
    const fk=curStageObj.group.userData.fadeK;
    if(typeof fk!=='number'||fk<0.99||fk>1.01)throw new Error('fadeK='+fk+' 应为 1 @'+i);
    const bad=scan(curStageObj.group);
    if(bad.length)throw new Error('发现 NaN: '+bad.slice(0,4).join(',')+' @'+i);
    let meshes=0,points=0,lights=0;
    curStageObj.group.traverse(o=>{ if(o.isMesh)meshes++; if(o.isPoints)points++; if(o.isLight)lights++; });
    out.push('境'+i+' '+STAGES[i].name+' mesh='+meshes+' points='+points+' light='+lights+' [OK]');
  }
  // 封面先扫一遍
  {
    const bad=scan(curStageObj.group);
    if(bad.length)throw new Error('封面 NaN: '+bad.slice(0,4).join(','));
  }
  // —— 入境（真实按钮）——
  document.querySelector('#enterBtn').fire('click');
  waitStage(1);
  waitStage(2);
  // —— 交互境 · 梨花千树：点击绽开 ——
  {
    const st=curStageObj;
    if(!st.click)throw new Error('第2境缺 click()');
    if(!st.ctl)throw new Error('第2境缺 ctl');
    frames(30);
    st.click();
    if(!st.ctl.clicked||st.ctl.t0<0)throw new Error('梨花 click 未触发');
    frames(60);
    let im=null,pl=null;
    st.group.traverse(o=>{ if(o.isInstancedMesh&&o.count>10)im=o;
      if(o.isPointLight&&o.userData.baseI===0)pl=o; });
    if(!im)throw new Error('花簇 InstancedMesh 未找到');
    if(!im.instanceColor)throw new Error('花簇 instanceColor 未启用');
    if(!pl||pl.intensity<=0.01)throw new Error('雪光未随绽开转亮: '+(pl&&pl.intensity));
    const c=new THREE.Color(); im.getColorAt(0,c);
    if(Math.abs(c.b-c.r)<0.02)throw new Error('花簇颜色未转暖: r='+c.r.toFixed(3)+' b='+c.b.toFixed(3));
    out.push('交互·梨花绽开 instanceColor 转暖 + 春光点亮 [OK]');
  }
  waitStage(3);
  waitStage(4);
  waitStage(5);
  waitStage(6);
  // —— 交互境 · 空留马迹：点击续蹄印；空格先交互、再按进终章 ——
  {
    const st=curStageObj;
    if(!st.click||!st.ctl)throw new Error('第6境缺 click()/ctl');
    st.click();
    if(!st.ctl.clicked)throw new Error('马迹 click 未触发');
    frames(30);
    const t0=st.ctl.t0;
    st.click();                        // 冷却期内连点不重置
    if(st.ctl.t0!==t0)throw new Error('马迹冷却守卫失效');
    // 模拟空格路径：clicked 后第二次空格应进终章
    if(state!=='stage')throw new Error('进入终章前应为 stage');
    showEnding();
    if(state!=='ending')throw new Error('showEnding 未生效');
    out.push('交互·马蹄印延伸 + 冷却守卫 + 二次空格进终章 [OK]');
  }
  // —— 终章 → 回封面 ——
  hideEnding('cover');
  frames(120);
  if(state!=='stage'||curIdx!==0)throw new Error('回封面失败 state='+state+' curIdx='+curIdx);
  out.push('终章 → 回封面 [OK]');
  // —— 小测结构 ——
  startQuiz(); renderQuiz(); showResult();
  out.push('小测 5 题 + words[6] [OK]');
  window.__SMOKE=out.join('\\n');
})();
`;
if (run(harness, 'harness')) {
  console.log(String(sandbox.window.__SMOKE).split('\n').map(l => '  ✓ ' + l).join('\n'));
}
// words 评语数组长度 = 题数+1（node 侧正则，评语按本诗定制）
{
  const wm = code.match(/words\s*=\s*\[([^\]]*)\]/);
  const wn = wm ? wm[1].split(',').length : -1;
  if (wn !== 6) { console.error('  ✗ words 评语数组应为 6 项（题数+1），实际 ' + wn); fails++; }
  else console.log('  ✓ words 评语 6 项 [OK]');
}
if (fails === 0) console.log('\nSMOKE PASS —— boot/逐境/交互/终章/回封面 全部真实执行无异常，无 NaN，fadeK 正常');
else { console.log('\nSMOKE FAIL —— ' + fails + ' 处异常'); process.exit(1); }
