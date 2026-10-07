#!/usr/bin/env node
/* build-gulang.js —— 《古朗月行（节选）》水墨夜思 · 月作白玉盘/瑶台镜 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'gu-lang-yue-xing/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
/* 函数式色值：水墨夜思强调色 #d6dee9 */
const A = a => `rgba(214,222,233,${a})`;
const BG = '#0d1117', FOG = '0x10161f';

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 古朗月行 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>古朗月行</h1>\n      <div class="dyn">唐 · 李白</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">古朗月行<small>循 文 入 境 · 李 白</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：小时候不识月，呼作白玉盘；又疑瑶台镜，飞在青云端——回到童年第一次抬头看月的好奇。</p>\n      <p>边读诗，边走进李白笔下那轮又大又亮、天真烂漫的月亮。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>月上 · 云端</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击切换白玉盘与瑶台镜 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 古朗月行 —— Three.js 沉浸式诗词课件', 1);

/* CSS 换肤 */
rep('--gold:#d4af37', '--gold:#d6dee9', 1);
rep('--ink:#e8dcc0', '--ink:#dfe6f0', 1);
rep('--dim:#9b8d6e', '--dim:#7e8a9c', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(10,15,24,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(214,222,233,.28)', 1);
rep('background:#05070d', 'background:#0d1117', 2);
rep('rgba(4,6,11,.82)', 'rgba(7,11,18,.82)', 1);
rep('rgba(4,6,11,.9)', 'rgba(7,11,18,.9)', 1);
rep('rgba(212,175,55,.35)', A('.35'), 1);
rep('rgba(212,175,55,.4)', A('.4'), 2);
rep('rgba(212,175,55,.5)', A('.5'), 1);
rep('rgba(212,175,55,.6)', A('.6'), 1);
rep('rgba(212,175,55,.8)', A('.8'), 2);
rep('rgba(212,175,55,.25)', A('.25'), 1);
rep('rgba(212,175,55,.14)', A('.14'), 1);
rep('rgba(212,175,55,.3)', A('.3'), 1);
rep('rgba(232,220,192,.25)', A('.22'), 1);
rep('rgba(232,220,192,.30)', A('.26'), 1);
rep('color:#5a5340', 'color:#5c6a80', 1);
rep('color:#6f664f', 'color:#67748a', 1);
rep('background:#0b101c', 'background:#0e1520', 1);

/* 天空/雾常量（水墨夜思） */
rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x10161f,0.0042)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x080d12)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x080d12)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x10161f)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x0d1520),hor:C(0x1b2534)", 1);

/* POEM/CN/QUIZ */
const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'不识月', jing:'小时候不懂什么是月亮，只觉得夜空里挂着一团神秘的光。',
  segs:[{c:'小时不识月，', p:py('xiǎo shí bù shí yuè')}],
  read:'小时不识月。',
  yisi:'小时候不认识月亮，不知道它是什么东西。',
  zhu:[['识','认识，知道'],['不识月','不认识月亮']] },
{ name:'白玉盘', jing:'把它叫作白玉做的盘子——又圆又亮。',
  segs:[{c:'呼作白玉盘。', p:py('hū zuò bái yù pán')}],
  read:'呼作白玉盘。',
  yisi:'于是把它叫作白玉盘——又圆又亮，像白玉琢成的盘子。',
  zhu:[['呼作','称为，叫作'],['白玉盘','白玉做成的盘子，形容圆月的洁白晶莹']] },
{ name:'瑶台镜', jing:'又怀疑它是仙女瑶台的镜子，飞挂在青云之上。',
  segs:[{c:'又疑瑶台镜，飞在青云端。', p:py('yòu yí yáo tái jìng fēi zài qīng yún duān')}],
  read:'又疑瑶台镜，飞在青云端。',
  yisi:'又怀疑它是瑶台上仙人的宝镜，飞挂在青云的顶端。',
  zhu:[['疑','怀疑'],['瑶台','传说中神仙居住的地方'],['青云端','青色的云端']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「小时不识月，呼作」的下一句是？', o:['白玉盘','瑶台镜','青云端'], a:0},
 {q:'「又疑瑶台镜」中「疑」的意思是？', o:['犹豫','怀疑、以为','询问'], a:1},
 {q:'《古朗月行（节选）》的作者是？', o:['杜甫','李白','孟浩然'], a:1},
 {q:'诗人把月亮先后比作了什么？', o:['白玉盘和瑶台镜','铜镜和玉环','银盘和明珠'], a:0},
 {q:'这四句诗写出了怎样的心情？', o:['思念故乡的愁苦','童年看月的天真好奇','对月亮的恐惧'], a:1},
];`);

/* builders：封面+三境（月亮拟物双形态） */
const BUILDERS = `function bCoverMoonKid(){
  const g=new THREE.Group();
  const hill=new THREE.Mesh(new THREE.SphereGeometry(120,24,16),new THREE.MeshPhongMaterial({color:0x0d1420}));
  hill.position.set(0,-116,-40); g.add(hill);
  const motes=makeGlow({n:70,box:[140,40,90],pos:[0,14,-40],color:0xd6dee9,size:7,speed:0.04,rise:0,maxA:0.45});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[170,26,110],pos:[0,8,-40],scale:60,color:0x9fb0c8,op:0.08});
  g.add(mist.g);
  addLights(g,{c:0xaebfd6,i:0.55,p:[-40,90,30]},{c:0x222c3a,i:0.8});
  return {group:g,update(t){motes.update(t);mist.update(t);}};
}
function bShiyue(){
  const g=new THREE.Group();
  const hill=new THREE.Mesh(new THREE.SphereGeometry(120,24,16),new THREE.MeshPhongMaterial({color:0x0c131d}));
  hill.position.set(0,-116,-40); g.add(hill);
  const kid=makeFigure(0.55); kid.position.set(1.5,0,6); kid.rotation.y=3.0; kid.rotation.x=-0.12; g.add(kid);
  const fire=makeGlow({n:40,box:[70,14,50],pos:[0,7,-10],color:0xd6dee9,size:6,speed:0.03,rise:0,maxA:0.35});
  g.add(fire.points);
  addLights(g,{c:0x8ea0ba,i:0.35,p:[-30,80,20]},{c:0x1c2430,i:0.9});
  return {group:g,update(t){fire.update(t);
    kid.rotation.z=Math.sin(t*0.8)*0.03;
  }};
}
function bMoonProp(startJing){
  const g=new THREE.Group();
  const hill=new THREE.Mesh(new THREE.SphereGeometry(120,24,16),new THREE.MeshPhongMaterial({color:0x0c131d}));
  hill.position.set(0,-116,-40); g.add(hill);
  const M=new THREE.Vector3(0,62,-120);
  const plate=new THREE.Group();
  const plateBody=new THREE.Mesh(new THREE.CylinderGeometry(17,17,2.6,48),
    new THREE.MeshPhongMaterial({color:0xeef3ee,emissive:0x93a89b,shininess:90,transparent:true,opacity:0.96}));
  const rim=new THREE.Mesh(new THREE.TorusGeometry(17,0.9,10,60),
    new THREE.MeshPhongMaterial({color:0xf4f8f4,emissive:0x7a9080,shininess:110}));
  rim.rotation.x=Math.PI/2;
  plate.add(plateBody,rim); plate.position.copy(M); plate.rotation.x=0.35; plate.visible=!startJing; g.add(plate);
  const mirror=new THREE.Group();
  const mGlass=new THREE.Mesh(new THREE.CircleGeometry(16,48),
    new THREE.MeshPhongMaterial({color:0xe9f2f8,emissive:0x8ba4c0,shininess:130,side:THREE.DoubleSide}));
  const mRing=new THREE.Mesh(new THREE.TorusGeometry(16,1.1,10,60),
    new THREE.MeshPhongMaterial({color:0xd8e4ee,emissive:0x6a80a0,shininess:120}));
  const mHandle=new THREE.Mesh(new THREE.BoxGeometry(2.4,6,1.6),
    new THREE.MeshPhongMaterial({color:0xc9d6e2,emissive:0x54687e}));
  mHandle.position.y=-18.5;
  mirror.add(mGlass,mRing,mHandle); mirror.position.copy(M); mirror.visible=!!startJing; g.add(mirror);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xdfe9f5,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(120,120,1); glow.position.copy(M); g.add(glow);
  const cloud=new THREE.Group(); g.add(cloud);
  for(let i=0;i<4;i++){
    const c=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x33415c,
      transparent:true,opacity:0.32,depthWrite:false}));
    c.scale.set(rnd(50,80),rnd(16,26),1); c.position.set(rnd(-70,70),M.y+rnd(-14,18),M.z+rnd(4,14));
    cloud.add(c);
  }
  const ctl={mode:startJing?1:0,t:99};
  addLights(g,{c:0xaebfd6,i:0.5,p:[-30,90,20]},{c:0x1e2836,i:0.85});
  return {group:g,update(t,dt){
    glow.material.opacity=0.42+0.1*Math.sin(t*0.9);
    plate.rotation.z=t*0.05; mirror.rotation.z=-t*0.04;
    cloud.children.forEach((c,i)=>{c.position.x+=Math.sin(t*0.1+i)*0.02;});
    ctl.t+=dt;
  },click(){
    if(ctl.t<2.4)return;
    ctl.t=0;
    ctl.mode=1-ctl.mode;
    plate.visible=ctl.mode===0; mirror.visible=ctl.mode===1;
    bell();
    const fl=$('#flash'); fl.textContent=ctl.mode===0?'呼作白玉盘':'疑是瑶台镜';
    fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCoverMoonKid,
  cam:{f:[0,10,66],t:[0,11,60],lf:[0,34,-70],lt:[0,36,-70]},
  sky:()=>SK({star:0.6,ms:1.5,moon:new THREE.Vector3(-40,88,-150),fd:0.0038}) },
{ name:'不识月',dwell:14,river:0.015,build:bShiyue,
  cam:{f:[0,7,58],t:[2,8,54],lf:[0,40,-90],lt:[0,44,-95]},
  sky:()=>SK({star:0.5,ms:1.05,moon:new THREE.Vector3(0,70,-130),fd:0.0046,moonC:C(0xc9d2dd)}) },
{ name:'白玉盘',dwell:14,river:0.015,build:()=>bMoonProp(false),
  cam:{f:[0,12,74],t:[0,14,68],lf:[0,52,-118],lt:[0,55,-120]},
  sky:()=>SK({star:0.55,ms:0.001,moon:new THREE.Vector3(0,-400,0),fd:0.004}) },
{ name:'瑶台镜',dwell:16,river:0.015,build:()=>bMoonProp(true),
  cam:{f:[0,14,78],t:[0,15,72],lf:[0,56,-120],lt:[0,58,-120]},
  sky:()=>SK({star:0.6,ms:0.001,moon:new THREE.Vector3(0,-400,0),fd:0.0038}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 玉盘与瑶台镜'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','古朗月行。唐，李白。小时不识月，呼作白玉盘。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重看明月','初识诗仙，尚需共读','渐入佳境，再诵几遍','童趣会心，仰头一笑','月色可亲，童趣天成','谪仙知己，月照云端'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
