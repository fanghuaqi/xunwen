#!/usr/bin/env node
/* build-xuemei.js —— 《雪梅》宣纸留白·梅雪争春（浅色主题） */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'xuemei/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(74,80,96,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 雪梅 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>雪梅</h1>\n      <div class="dyn">宋 · 卢梅坡</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">雪梅<small>循 文 入 境 · 卢梅坡</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：梅花开时雪未停，梅与雪各占春色互不相让——比白、比香，难坏了评诗的人。</p>\n      <p>边读诗，边走进卢梅坡笔下那场梅与雪的"比武"——比白、比香，各不相让。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>梅雪 · 争春</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击香雾自梅而出 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 雪梅 —— Three.js 沉浸式诗词课件', 1);

/* 浅色主题全链路换肤 */
rep('--gold:#d4af37', '--gold:#4a5060', 1);
rep('--ink:#e8dcc0', '--ink:#23272e', 1);
rep('--dim:#9b8d6e', '--dim:#6a707c', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(255,252,240,.72)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(74,80,96,.3)', 1);
rep('background:#05070d', 'background:#e9e2d0', 2);
rep('rgba(4,6,11,.82)', 'rgba(216,208,188,.78)', 1);
rep('rgba(4,6,11,.9)', 'rgba(210,200,178,.88)', 1);
rep('rgba(212,175,55,.35)', A('.35'), 1);
rep('rgba(212,175,55,.4)', A('.4'), 2);
rep('rgba(212,175,55,.5)', A('.5'), 1);
rep('rgba(212,175,55,.6)', A('.6'), 1);
rep('rgba(212,175,55,.8)', A('.8'), 2);
rep('rgba(212,175,55,.25)', A('.25'), 1);
rep('rgba(212,175,55,.14)', A('.14'), 1);
rep('rgba(212,175,55,.3)', A('.3'), 1);
rep('rgba(232,220,192,.25)', A('.18'), 1);
rep('rgba(232,220,192,.30)', A('.22'), 1);
rep('color:#5a5340', 'color:#8a8272', 1);
rep('color:#6f664f', 'color:#7a7464', 1);
rep('background:#0b101c', 'background:#f4eeda', 1);

/* 天空/雾常量（宣纸浅色） */
rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0xe6dfcc,0.0035)", 1);
rep("bot:C(0x0c1016)", "bot:C(0xcfc5ab)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0xcfc5ab)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0xe6dfcc)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0xe9e2d0),hor:C(0xded5bd)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'梅雪争春', jing:'梅花开时雪还在下，梅和雪都觉得自己占了春色，谁也不肯认输。',
  segs:[{c:'梅雪争春未肯降，', p:py('méi xuě zhēng chūn wèi kěn xiáng')}],
  read:'梅雪争春未肯降。',
  yisi:'梅花和雪花都认为自己占尽了春色，谁也不肯服输。',
  zhu:[['降','服输'],['未肯降','不肯服输']] },
{ name:'搁笔评章', jing:'难坏了诗人，放下笔来费心思量、难以评判高下。',
  segs:[{c:'骚人搁笔费评章。', p:py('sāo rén gē bǐ fèi píng zhāng')}],
  read:'骚人搁笔费评章。',
  yisi:'这可难坏了诗人，只好放下笔来，费尽心思地评判梅与雪的高下。',
  zhu:[['骚人','诗人'],['搁笔','放下笔'],['评章','评议，评判高下']] },
{ name:'逊白输香', jing:'梅比雪少了三分白，雪却输了梅的一段清香——各有所长。',
  segs:[{c:'梅须逊雪三分白，雪却输梅一段香。', p:py('méi xū xùn xuě sān fēn bái xuě què shū méi yī duàn xiāng')}],
  read:'梅须逊雪三分白，雪却输梅一段香。',
  yisi:'梅花比起雪来少了三分洁白，雪却输给梅花一段清香。',
  zhu:[['逊','不及，比不上'],['输','败给，比不过'],['一段香','一片清香']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「梅雪争春未肯降」的下一句是？', o:['骚人搁笔费评章','雪却输梅一段香','梅须逊雪三分白'], a:0},
 {q:'「未肯降」的「降」在这里的正确读音是？', o:['jiàng','xiáng','jiáng'], a:1},
 {q:'「骚人」在诗中的意思是？', o:['诗人','骚乱的人','年轻人'], a:0},
 {q:'梅和雪各输在哪里？', o:['梅逊雪三分白，雪输梅一段香','梅不如雪香，雪不如梅红','都输了，不分高下'], a:0},
 {q:'这首诗蕴含的道理是？', o:['人和事物各有所长、各有所短','冬天比春天美','要多下雪'], a:0},
];`);

const BUILDERS = `function makeSnowLight(n,sizeMax){
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=rnd(-55,55);P[i*3+1]=rnd(0.5,24);P[i*3+2]=rnd(-45,25);
    S[i]=rnd(14,26);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  const m=new THREE.Points(g,new THREE.PointsMaterial({color:0x9aa4b8,size:sizeMax*0.06,map:circleTex(),
    transparent:true,opacity:0.75,depthWrite:false}));
  m.userData.spd=S;
  const api={points:m,update(t,dt){
    const pos=m.geometry.attributes.position.array;
    for(let i=0;i<n;i++){
      pos[i*6]=pos[i*6]; // noop keep layout
    }
    for(let i=0;i<n;i++){
      let y=pos[i*3+1]-S[i]*dt*0.35;
      if(y<0.4)y=24;
      pos[i*3+1]=y;
      pos[i*3]=pos[i*3]+Math.sin(t*0.9+i)*dt*0.5;
    }
    m.geometry.attributes.position.needsUpdate=true;
  }};
  return api;
}
function makePlumBranch(){
  const g=new THREE.Group();
  const bm=new THREE.MeshPhongMaterial({color:0x3a3630,shininess:6});
  const main=new THREE.Mesh(new THREE.CylinderGeometry(0.28,0.5,10,7),bm);
  main.position.set(0,5,0); main.rotation.z=0.12; g.add(main);
  const arms=[[4.2,7.6,-0.9],[6.8,9.2,-0.3],[8.6,11.2,0.5]];
  for(const a of arms){
    const b=new THREE.Mesh(new THREE.CylinderGeometry(0.14,0.22,4.6,6),bm);
    b.position.set(a[0]*0.62,a[1],0); b.rotation.z=a[2]; g.add(b);
  }
  const petals=[];
  const pm=new THREE.MeshBasicMaterial({color:0xd8ccc4});
  for(let i=0;i<26;i++){
    const p=new THREE.Mesh(new THREE.SphereGeometry(0.24,7,6),pm);
    p.position.set(rnd(1,10.5),rnd(5,13),rnd(-0.6,0.6));
    p.scale.setScalar(rnd(0.7,1.3)); g.add(p); petals.push(p);
  }
  return {g,petals,update(t){
    petals.forEach((p,i)=>{p.scale.setScalar((0.7+((i*7)%10)/14)*(1+0.05*Math.sin(t*1.2+i)));});
  }};
}
function bCoverMeixue(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0xd8d0ba}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const snow=makeSnowLight(160,1); g.add(snow.points);
  const plum=makePlumBranch(); plum.g.position.set(-16,0,-18); g.add(plum.g);
  const mist=makeMist({n:7,spread:[150,20,100],pos:[0,8,-40],scale:65,color:0xffffff,op:0.16});
  g.add(mist.g);
  addLights(g,{c:0xfff6e0,i:0.5,p:[30,60,30]},{c:0xdad2be,i:0.9});
  return {group:g,update(t,dt){snow.update(t,dt);mist.update(t);plum.update(t);}};
}
function bZhengchun(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0xd8d0ba}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const snow=makeSnowLight(200,1.1); g.add(snow.points);
  const plum=makePlumBranch(); plum.g.position.set(-15,0,-16); plum.g.rotation.y=-0.5; g.add(plum.g);
  const snowM=new THREE.Mesh(new THREE.SphereGeometry(9,16,12),
    new THREE.MeshPhongMaterial({color:0xf4f7fc,emissive:0x8a94a8,transparent:true,opacity:0.85}));
  snowM.position.set(14,12,-30); g.add(snowM);
  addLights(g,{c:0xfff6e0,i:0.5,p:[30,60,30]},{c:0xdad2be,i:0.95});
  return {group:g,update(t,dt){snow.update(t,dt);plum.update(t);
    snowM.scale.setScalar(1+0.05*Math.sin(t*0.8));
  }};
}
function bGebi(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(70,40),new THREE.MeshPhongMaterial({color:0xd8d0ba}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const desk=new THREE.Mesh(new THREE.BoxGeometry(9,2.6,4.6),new THREE.MeshPhongMaterial({color:0x3a3226}));
  desk.position.set(0,1.3,-4); g.add(desk);
  const paper=new THREE.Mesh(new THREE.PlaneGeometry(4.6,2.8),new THREE.MeshBasicMaterial({color:0xf6f0dc}));
  paper.rotation.x=-Math.PI/2; paper.position.set(-1,2.65,-4); g.add(paper);
  const brush=new THREE.Group();
  const shaft=new THREE.Mesh(new THREE.CylinderGeometry(0.08,0.08,3.4,6),new THREE.MeshPhongMaterial({color:0x5a4a32}));
  const tip=new THREE.Mesh(new THREE.ConeGeometry(0.14,0.7,6),new THREE.MeshPhongMaterial({color:0x2a241c}));
  tip.position.y=-2.0; brush.add(shaft,tip);
  brush.rotation.z=Math.PI/2-0.15; brush.position.set(0.6,2.9,-3.6); g.add(brush);
  const ink=new THREE.Mesh(new THREE.CylinderGeometry(0.5,0.5,0.4,12),new THREE.MeshPhongMaterial({color:0x1c1c22}));
  ink.position.set(-3,2.85,-4.4); g.add(ink);
  const poet=makeFigure(0.95); poet.position.set(5.5,0,1.5); poet.rotation.y=-2.3; g.add(poet);
  addLights(g,{c:0xfff6e0,i:0.5,p:[20,50,30]},{c:0xdad2be,i:0.95});
  return {group:g,update(t){
    poet.rotation.y=-2.3+Math.sin(t*0.4)*0.06;
    poet.rotation.x=Math.sin(t*0.3)*0.04;
  }};
}
function bXunbaiXiang(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0xd8d0ba}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const snow=makeSnowLight(220,1.2); g.add(snow.points);
  const snowBall=new THREE.Mesh(new THREE.SphereGeometry(8,16,12),
    new THREE.MeshPhongMaterial({color:0xf4f7fc,emissive:0x8a94a8,transparent:true,opacity:0.85}));
  snowBall.position.set(-15,12,-30); g.add(snowBall);
  const plum=makePlumBranch(); plum.g.position.set(12,0,-18); plum.g.rotation.y=0.6; g.add(plum.g);
  const mist=makeMist({n:10,spread:[16,20,10],pos:[12,9,-16],scale:26,color:0xc9b98a,op:0.22});
  g.add(mist.g);
  const ctl={t:99};
  addLights(g,{c:0xfff6e0,i:0.5,p:[30,60,30]},{c:0xdad2be,i:0.95});
  return {group:g,update(t,dt){
    snow.update(t,dt); mist.update(t); plum.update(t);
    ctl.t+=dt;
    snowBall.scale.setScalar(1+0.05*Math.sin(t*0.8));
    mist.g.children.forEach(s=>{s.position.y+=dt*(0.5+Math.sin(t*0.7)*0.2);});
  },click(){
    if(ctl.t<2.6)return;
    ctl.t=0; bell();
    mist.g.children.forEach(s=>{s.scale.multiplyScalar(1.25);});
    const fl=$('#flash'); fl.textContent='雪却输梅一段香'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.012,build:bCoverMeixue,
  cam:{f:[0,8,52],t:[0,8,48],lf:[0,8,-30],lt:[0,8,-30]},
  sky:()=>SK({star:0.04,ms:0.85,moon:new THREE.Vector3(50,80,-150),fd:0.0034,ambC:C(0xdad2be),ambI:0.95,dirC:C(0xfff2d8),dirI:0.45}) },
{ name:'梅雪争春',dwell:14,river:0.012,build:bZhengchun,
  cam:{f:[0,8,42],t:[0,8,38],lf:[0,9,-22],lt:[14,11,-30]},
  sky:()=>SK({star:0.04,ms:0.8,moon:new THREE.Vector3(50,80,-150),fd:0.0038,ambC:C(0xdad2be),ambI:0.95,dirC:C(0xfff2d8),dirI:0.45}) },
{ name:'搁笔评章',dwell:13,river:0.012,build:bGebi,
  cam:{f:[0,6.5,26],t:[0,6,24],lf:[0,3.5,-4],lt:[0,3.2,-4]},
  sky:()=>SK({star:0.03,ms:0.75,moon:new THREE.Vector3(50,80,-150),fd:0.0042,ambC:C(0xdad2be),ambI:0.95,dirC:C(0xfff2d8),dirI:0.45}) },
{ name:'逊白输香',dwell:16,river:0.012,build:bXunbaiXiang,
  cam:{f:[0,7,34],t:[0,7,30],lf:[-13,9,-30],lt:[13,9,-18]},
  sky:()=>SK({star:0.05,ms:0.8,moon:new THREE.Vector3(-50,80,-150),fd:0.0036,ambC:C(0xdad2be),ambI:0.95,dirC:C(0xfff2d8),dirI:0.45}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 香雾自梅而出'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','雪梅。宋，卢梅坡。梅雪争春未肯降，骚人搁笔费评章。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重评梅雪','初识梅坡，尚需共读','渐入佳境，再诵几遍','评章有味，搁笔一笑','深得梅坡哲思','梅雪知己，各有所长'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
