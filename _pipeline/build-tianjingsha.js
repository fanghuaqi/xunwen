#!/usr/bin/env node
/* build-tianjingsha.js —— 《天净沙·秋思》烟雨江南·九意象长卷 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'tianjingsha-qiusi/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(154,144,184,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 天净沙·秋思 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>天净沙·秋思</h1>\n      <div class="dyn">元 · 马致远</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">天净沙·秋思<small>循 文 入 境 · 马致远</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>四重意境，随诗句次第展开：枯藤、老树、昏鸦，小桥、流水、人家，古道、西风、瘦马——夕阳西下，断肠人在天涯。</p>\n      <p>边读诗，边沿着马致远笔下的秋日古道，走完那条天涯路。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>夕阳 · 天涯</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">四 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击夕阳西沉瘦马长嘶 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 天净沙·秋思 —— Three.js 沉浸式诗词课件', 1);

rep('--gold:#d4af37', '--gold:#9a90b8', 1);
rep('--ink:#e8dcc0', '--ink:#e8e2ee', 1);
rep('--dim:#9b8d6e', '--dim:#837a9c', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(14,11,22,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(154,144,184,.28)', 1);
rep('background:#05070d', 'background:#100d16', 2);
rep('rgba(4,6,11,.82)', 'rgba(8,6,12,.82)', 1);
rep('rgba(4,6,11,.9)', 'rgba(8,6,12,.9)', 1);
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
rep('color:#5a5340', 'color:#6a6280', 1);
rep('color:#6f664f', 'color:#6f6890', 1);
rep('background:#0b101c', 'background:#141020', 1);

rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x171320,0.005)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x0c0912)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x0c0912)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x171320)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x151020),hor:C(0x2a2136)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'枯藤老树', jing:'枯藤缠绕的老树上栖息着黄昏归巢的乌鸦，小桥下流水潺潺，桥边是袅袅炊烟的人家。',
  segs:[{c:'枯藤老树昏鸦，小桥流水人家，', p:py('kū téng lǎo shù hūn yā xiǎo qiáo liú shuǐ rén jiā')}],
  read:'枯藤老树昏鸦，小桥流水人家。',
  yisi:'枯藤缠绕着老树，黄昏的乌鸦栖息枝头；小桥下流水潺潺，桥边升起炊烟的人家。',
  zhu:[['昏鸦','黄昏时归巢的乌鸦'],['人家','农家，这里指炊烟中的住户']] },
{ name:'古道瘦马', jing:'荒凉的古道上，西风劲吹，一匹瘦马驮着游子前行。',
  segs:[{c:'古道西风瘦马。', p:py('gǔ dào xī fēng shòu mǎ')}],
  read:'古道西风瘦马。',
  yisi:'荒凉的古道上，萧瑟的西风吹着，一匹瘦马驮着游子缓缓前行。',
  zhu:[['古道','古老的驿道'],['西风','秋风'],['瘦马','瘦弱的马']] },
{ name:'夕阳西下', jing:'傍晚的太阳渐渐向西边落下。',
  segs:[{c:'夕阳西下，', p:py('xī yáng xī xià')}],
  read:'夕阳西下。',
  yisi:'傍晚的太阳渐渐向西边沉落。',
  zhu:[['夕阳西下','点明游子思乡的时间，渲染苍凉氛围']] },
{ name:'断肠天涯', jing:'极度忧伤的旅人，还漂泊在天涯。',
  segs:[{c:'断肠人在天涯。', p:py('duàn cháng rén zài tiān yá')}],
  read:'断肠人在天涯。',
  yisi:'极度忧伤的旅人，还漂泊在天涯他乡。',
  zhu:[['断肠人','极度悲伤的旅人，指漂泊天涯的游子'],['天涯','天边，极远的地方']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁','肆'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「小桥流水人家」的前一句是？', o:['枯藤老树昏鸦','古道西风瘦马','夕阳西下'], a:0},
 {q:'「断肠人在天涯」中「断肠人」指的是？', o:['极度忧伤的漂泊游子','断了心肠的人','卖药的人'], a:0},
 {q:'《天净沙·秋思》的作者是？', o:['马致远','关汉卿','张养浩'], a:0},
 {q:'「天净沙」是这首作品的？', o:['曲牌名','题目','作者别名'], a:0},
 {q:'这首小令借哪些意象表达了羁旅之愁？', o:['枯藤、老树、昏鸦、西风、瘦马等','青山、绿水、白鹭','明月、美酒、轻舟'], a:0},
];`);

const BUILDERS = `function makeGnarledTree(){
  const g=new THREE.Group();
  const tm=new THREE.MeshPhongMaterial({color:0x1c1610,shininess:4});
  const trunk=new THREE.Mesh(new THREE.CylinderGeometry(0.5,1.1,12,7),tm);
  trunk.position.y=6; trunk.rotation.z=0.1; g.add(trunk);
  for(let i=0;i<5;i++){
    const b=new THREE.Mesh(new THREE.CylinderGeometry(0.12,0.3,6,5),tm);
    b.position.set(rnd(-2.4,2.4),rnd(7,11.5),rnd(-1.4,1.4));
    b.rotation.z=rnd(-1.1,1.1); b.rotation.x=rnd(-0.5,0.5); g.add(b);
  }
  for(let i=0;i<7;i++){
    const v=new THREE.Mesh(new THREE.TorusGeometry(rnd(0.8,1.5),0.07,5,14,rnd(2,4)),
      new THREE.MeshPhongMaterial({color:0x241c14}));
    v.position.set(rnd(-3.2,3.2),rnd(5,12),rnd(-1.6,1.6));
    v.rotation.set(rnd(0,3),rnd(0,3),rnd(0,3)); g.add(v);
  }
  const crow=new THREE.Group();
  const cb=new THREE.Mesh(new THREE.SphereGeometry(0.55,8,7),new THREE.MeshBasicMaterial({color:0x0a0808}));
  const ch=new THREE.Mesh(new THREE.SphereGeometry(0.3,7,6),cb.material); ch.position.set(0.5,0.35,0);
  const beak=new THREE.Mesh(new THREE.ConeGeometry(0.1,0.4,5),new THREE.MeshBasicMaterial({color:0x3a3020}));
  beak.position.set(0.85,0.32,0); beak.rotation.z=-Math.PI/2;
  crow.add(cb,ch,beak); crow.position.set(1.9,12.6,-0.4); g.add(crow);
  return {g,crow};
}
function makeBridgeHouse(){
  const g=new THREE.Group();
  const bridge=new THREE.Mesh(new THREE.BoxGeometry(9,0.6,3),new THREE.MeshPhongMaterial({color:0x2a2118}));
  bridge.position.set(-2,2.2,-8); bridge.rotation.z=0.08; g.add(bridge);
  const arch=new THREE.Mesh(new THREE.TorusGeometry(3,0.9,8,18,Math.PI),
    new THREE.MeshPhongMaterial({color:0x241c12}));
  arch.position.set(-2,0.4,-8); g.add(arch);
  const stream=new THREE.Mesh(new THREE.PlaneGeometry(16,10),new THREE.MeshPhongMaterial({color:0x1a2430,shininess:80}));
  stream.rotation.x=-Math.PI/2; stream.position.set(-2,0.05,-8); g.add(stream);
  const house=new THREE.Mesh(new THREE.BoxGeometry(5,3.6,4),new THREE.MeshPhongMaterial({color:0x241c12}));
  house.position.set(-10,1.8,-13); g.add(house);
  const roof=new THREE.Mesh(new THREE.ConeGeometry(4.2,2,4),new THREE.MeshPhongMaterial({color:0x16100a}));
  roof.rotation.y=Math.PI/4; roof.position.set(-10,4.6,-13); g.add(roof);
  const smoke=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8a8296,
    transparent:true,opacity:0.3,depthWrite:false}));
  smoke.scale.set(3,7,1); smoke.position.set(-10,6.5,-13); g.add(smoke);
  return {g,smoke,update(t){
    smoke.position.y=6.5+Math.sin(t*0.6)*0.5;
    smoke.material.opacity=0.22+0.1*Math.sin(t*0.8);
  }};
}
function bCoverQiuxiang(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x14101a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const tree=makeGnarledTree(); tree.g.position.set(14,0,-26); g.add(tree.g);
  const bh=makeBridgeHouse(); g.add(bh.g);
  const mist=makeMist({n:9,spread:[160,20,110],pos:[0,7,-40],scale:70,color:0x837a9c,op:0.11});
  g.add(mist.g);
  addLights(g,{c:0xc9a06a,i:0.45,p:[-40,40,30]},{c:0x241f30,i:0.85});
  return {group:g,update(t,dt){mist.update(t);bh.update(t);
    tree.crow.rotation.y=Math.sin(t*0.5)*0.3;
  }};
}
function bKuteng(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x14101a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const tree=makeGnarledTree(); tree.g.position.set(10,0,-30); tree.g.scale.setScalar(1.5); g.add(tree.g);
  const crow=tree.crow;
  const path=new THREE.Mesh(new THREE.PlaneGeometry(5,80),new THREE.MeshPhongMaterial({color:0x1c160e}));
  path.rotation.x=-Math.PI/2; path.position.set(0,0.02,-16); g.add(path);
  const mist=makeMist({n:10,spread:[170,20,120],pos:[0,7,-46],scale:75,color:0x837a9c,op:0.12});
  g.add(mist.g);
  addLights(g,{c:0xc9a06a,i:0.42,p:[-40,40,30]},{c:0x241f30,i:0.85});
  return {group:g,update(t,dt){mist.update(t);
    crow.rotation.y=Math.sin(t*0.5)*0.3;
    crow.position.y=18.9+Math.sin(t*1.2)*0.1;
  }};
}
function bGudao(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x151009}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const path=new THREE.Mesh(new THREE.PlaneGeometry(6,90),new THREE.MeshPhongMaterial({color:0x241c10}));
  path.rotation.x=-Math.PI/2; path.position.set(0,0.02,-20); g.add(path);
  const wind=makeFlow({n:200,box:[120,22,70],pos:[0,9,-20],color:0x9a90b8,size:20,speed:10,maxA:0.28});
  g.add(wind.points);
  const horse=new THREE.Group();
  const hb=new THREE.Mesh(new THREE.BoxGeometry(2.6,1.2,0.9),new THREE.MeshPhongMaterial({color:0x1a1410}));
  const hh=new THREE.Mesh(new THREE.BoxGeometry(0.8,0.9,0.7),hb.material); hh.position.set(1.5,0.9,0);
  const legs=[];
  for(let i=0;i<4;i++){
    const l=new THREE.Mesh(new THREE.CylinderGeometry(0.09,0.07,1.3,5),hb.material);
    l.position.set(i<2?0.9:-0.9,-1.2,i%2?0.3:-0.3); horse.add(l); legs.push(l);
  }
  horse.add(hb,hh); horse.position.set(0,2.4,0); horse.rotation.y=Math.PI/2;
  const rider=makeFigure(0.7); rider.position.set(0,2.9,0); rider.scale.setScalar(0.7); horse.add(rider);
  g.add(horse);
  addLights(g,{c:0xc9a06a,i:0.4,p:[-30,40,30]},{c:0x241f30,i:0.85});
  return {group:g,update(t,dt){wind.update(t);
    const w=Math.sin(t*2.2);
    horse.position.y=2.4+Math.abs(Math.sin(t*1.5))*0.15;
    legs.forEach((l,i)=>{l.rotation.x=Math.sin(t*2.2+i*1.57)*0.5;});
    rider.rotation.x=Math.sin(t*1.5)*0.08;
  }};
}
function bXiyang(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x14101a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const sun=new THREE.Mesh(new THREE.SphereGeometry(6,18,14),new THREE.MeshBasicMaterial({color:0xd88a4a}));
  sun.position.set(0,26,-110); g.add(sun);
  const sglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88a4a,
    transparent:true,opacity:0.6,depthWrite:false,blending:THREE.AdditiveBlending}));
  sglow.scale.set(70,70,1); sglow.position.copy(sun.position); g.add(sglow);
  const horizon=new THREE.Mesh(new THREE.PlaneGeometry(220,4),new THREE.MeshBasicMaterial({color:0x0c0912}));
  horizon.position.set(0,2,-118); g.add(horizon);
  addLights(g,{c:0xc9804a,i:0.5,p:[0,30,-60]},{c:0x241f30,i:0.85});
  return {group:g,update(t,dt){
    sun.position.y=Math.max(4,26-t*0.35);
    sglow.position.y=sun.position.y;
    sglow.material.opacity=0.3+sun.position.y/60;
  }};
}
function bDuoan(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x14101a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const horse=makeFigure(0.85); horse.position.set(2,0,-6); g.add(horse);
  const man=makeFigure(0.95); man.position.set(0,0,0); man.rotation.y=0.6; g.add(man);
  const scarf=new THREE.Mesh(new THREE.PlaneGeometry(0.5,2.2),new THREE.MeshPhongMaterial({color:0x4a4460,side:THREE.DoubleSide}));
  scarf.position.set(0.2,6.2,-0.2); man.add(scarf);
  const sun=new THREE.Mesh(new THREE.SphereGeometry(5,16,12),new THREE.MeshBasicMaterial({color:0xc9784a}));
  sun.position.set(-40,10,-105); g.add(sun);
  addLights(g,{c:0xc9804a,i:0.4,p:[-30,24,-50]},{c:0x241f30,i:0.85});
  return {group:g,update(t,dt){
    scarf.rotation.x=Math.sin(t*2.6)*0.5;
    man.rotation.y=0.6+Math.sin(t*0.3)*0.05;
  },click(){
    const fl=$('#flash'); fl.textContent='断肠人在天涯'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    drum2();
  }};
}
function drum2(){
  if(!groupAudio.ctx)return;
  const ctx=groupAudio.ctx, now=ctx.currentTime;
  const o=ctx.createOscillator(), gn=ctx.createGain();
  o.type='sawtooth'; o.frequency.setValueAtTime(320,now); o.frequency.linearRampToValueAtTime(180,now+0.7);
  gn.gain.setValueAtTime(0.001,now); gn.gain.linearRampToValueAtTime(0.14,now+0.15); gn.gain.exponentialRampToValueAtTime(0.001,now+0.9);
  o.connect(gn).connect(groupAudio.master); o.start(now); o.stop(now+1);
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCoverQiuxiang,
  cam:{f:[0,9,56],t:[0,9,52],lf:[0,8,-28],lt:[0,8,-28]},
  sky:()=>SK({star:0.3,ms:0.85,moon:new THREE.Vector3(-60,70,-150),fd:0.0055}) },
{ name:'枯藤老树',dwell:15,river:0.015,build:bKuteng,
  cam:{f:[0,9,44],t:[0,9,40],lf:[10,11,-28],lt:[10,11,-28]},
  sky:()=>SK({star:0.25,ms:0.7,moon:new THREE.Vector3(-60,65,-150),fd:0.006}) },
{ name:'古道瘦马',dwell:14,river:0.015,build:bGudao,
  cam:{f:[0,7,36],t:[0,7,32],lf:[0,4,-16],lt:[0,4,-24]},
  sky:()=>SK({star:0.2,ms:0.6,moon:new THREE.Vector3(-60,60,-150),fd:0.0065}) },
{ name:'夕阳西下',dwell:12,river:0.015,build:bXiyang,
  cam:{f:[0,9,48],t:[0,9,44],lf:[0,22,-110],lt:[0,12,-110]},
  sky:()=>SK({star:0.15,ms:0.5,moon:new THREE.Vector3(-60,50,-150),fd:0.007}) },
{ name:'断肠天涯',dwell:16,river:0.015,build:bDuoan,
  cam:{f:[0,7,30],t:[0,6.5,27],lf:[0,6,-40],lt:[-30,8,-100]},
  sky:()=>SK({star:0.12,ms:0.4,moon:new THREE.Vector3(-60,40,-150),fd:0.008}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,4);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=4;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=4)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===4)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===4&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===4&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===4)setTimeout(()=>tip('轻点画面 —— 夕阳西沉瘦马长嘶'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('05.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','天净沙秋思。元，马致远。枯藤老树昏鸦，小桥流水人家。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重走古道','初识东篱，尚需共读','渐入佳境，再诵几遍','秋思入骨，夕阳无限','深得东篱秋思','东篱知己，天涯同心'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
