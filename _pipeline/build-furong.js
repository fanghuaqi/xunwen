#!/usr/bin/env node
/* build-furong.js —— 《芙蓉楼送辛渐》烟雨江南·冰心玉壶 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'furonglou-song/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(154,184,216,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 芙蓉楼送辛渐 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>芙蓉楼送辛渐</h1>\n      <div class="dyn">唐 · 王昌龄</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">芙蓉楼送辛渐<small>循 文 入 境 · 王昌龄</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：寒雨连江的夜、平明送别的孤山，最后凝成那只玉壶——一片冰心，澄澈可见。</p>\n      <p>边读诗，边走进王昌龄笔下那场清冷的送别与坦荡的告白。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>玉壶 · 冰心</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击玉壶冰心特写 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 芙蓉楼送辛渐 —— Three.js 沉浸式诗词课件', 1);

rep('--gold:#d4af37', '--gold:#9ab8d8', 1);
rep('--ink:#e8dcc0', '--ink:#e2eaf4', 1);
rep('--dim:#9b8d6e', '--dim:#7c8ba0', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(8,12,20,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(154,184,216,.28)', 1);
rep('background:#05070d', 'background:#0a0f16', 2);
rep('rgba(4,6,11,.82)', 'rgba(6,9,14,.82)', 1);
rep('rgba(4,6,11,.9)', 'rgba(6,9,14,.9)', 1);
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
rep('color:#6f664f', 'color:#64748a', 1);
rep('background:#0b101c', 'background:#0e141d', 1);

rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x131a24,0.005)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x0a0f14)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x0a0f14)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x131a24)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x101722),hor:C(0x202c3c)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'寒雨连江', jing:'深秋的冷雨洒满江面，夜里融入吴地。',
  segs:[{c:'寒雨连江夜入吴，', p:py('hán yǔ lián jiāng yè rù wú')}],
  read:'寒雨连江夜入吴，',
  yisi:'深秋的冷雨连夜洒遍江面，我伴着雨声来到吴地。',
  zhu:[['寒雨','深秋的冷雨'],['连江','雨水与江面连成一片'],['吴','三国时的吴地，今江苏一带']] },
{ name:'楚山孤', jing:'天亮时送别友人，只留下孤零零的楚山相伴。',
  segs:[{c:'平明送客楚山孤。', p:py('píng míng sòng kè chǔ shān gū')}],
  read:'平明送客楚山孤。',
  yisi:'天刚亮时在芙蓉楼送别友人，友人离去后，只有孤独的楚山陪伴着我。',
  zhu:[['平明','天刚亮的时候'],['客','指辛渐'],['楚山','楚地的山，这里指送别之地'],['孤','孤独，孤单']] },
{ name:'冰心玉壶', jing:'若洛阳的亲友问起我，就说我的心依然像玉壶里的冰一样澄澈。',
  segs:[{c:'洛阳亲友如相问，一片冰心在玉壶。', p:py('luò yáng qīn yǒu rú xiāng wèn yī piàn bīng xīn zài yù hú')}],
  read:'洛阳亲友如相问，一片冰心在玉壶。',
  yisi:'如果洛阳的亲友问起我的近况，请告诉他们：我的心依然像玉壶中的冰一样晶莹纯洁。',
  zhu:[['冰心','像冰一样晶莹纯洁的心'],['玉壶','白玉做成的壶，比喻高洁清白'],['相问','问起我']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「寒雨连江夜入吴」的下一句是？', o:['平明送客楚山孤','一片冰心在玉壶','洛阳亲友如相问'], a:0},
 {q:'「一片冰心在玉壶」表达了诗人怎样的品格？', o:['心地纯洁、品格高洁','思念家乡','渴望做官'], a:0},
 {q:'《芙蓉楼送辛渐》的作者是？', o:['李白','王昌龄','王维'], a:1},
 {q:'「平明」在诗中的意思是？', o:['天刚亮的时候','平安','平时'], a:0},
 {q:'这首诗属于哪种题材？', o:['田园诗','送别诗','边塞诗'], a:1},
];`);

const BUILDERS = `function bCoverRain(){
  const g=new THREE.Group();
  const water=new THREE.Mesh(new THREE.PlaneGeometry(220,160),new THREE.MeshPhongMaterial({color:0x0d141d,shininess:70}));
  water.rotation.x=-Math.PI/2; water.position.set(0,0,-30); g.add(water);
  const rain=makeRain(600,0x8fa8c8,110); g.add(rain.points);
  const mist=makeMist({n:10,spread:[180,24,120],pos:[0,10,-40],scale:70,color:0x7c8ba0,op:0.12});
  g.add(mist.g);
  addLights(g,{c:0x8fa8c8,i:0.45,p:[30,60,30]},{c:0x1a2230,i:0.85});
  return {group:g,update(t,dt){rain.update(t,dt);mist.update(t);}};
}
function makeRain(n,color,height){
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*6),S=new Float32Array(n);
  for(let i=0;i<n;i++){
    const x=rnd(-60,60),z=rnd(-50,30),y=rnd(2,height),len=rnd(1.4,2.6);
    P[i*6]=x;P[i*6+1]=y;P[i*6+2]=z;P[i*6+3]=x+0.3;P[i*6+4]=y-len;P[i*6+5]=z;
    S[i]=rnd(16,30);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  const m=new THREE.LineSegments(g,new THREE.LineBasicMaterial({color,transparent:true,opacity:0.4}));
  m.userData.spd=S; m.userData.h=height;
  const api={points:m,update(t,dt){
    const pos=m.geometry.attributes.position.array;
    for(let i=0;i<n;i++){
      const fall=(S[i]*dt*3)%height;
      let y=pos[i*6+1]-dt*S[i];
      if(y<1){y+=height;}
      pos[i*6+1]=y;pos[i*6+4]=y-(pos[i*6+3]-pos[i*6])*0.9;
    }
    m.geometry.attributes.position.needsUpdate=true;
  }};
  return api;
}
function bRainNight(){
  const g=new THREE.Group();
  const water=new THREE.Mesh(new THREE.PlaneGeometry(220,160),new THREE.MeshPhongMaterial({color:0x0c1219,shininess:80}));
  water.rotation.x=-Math.PI/2; water.position.set(0,0,-30); g.add(water);
  const rain=makeRain(700,0x8fa8c8,120); g.add(rain.points);
  const mist=makeMist({n:12,spread:[200,26,130],pos:[0,9,-40],scale:80,color:0x7c8ba0,op:0.15});
  g.add(mist.g);
  const boat=makeBoatShape(4); boat.position.set(6,0.8,-8); boat.rotation.y=0.3; g.add(boat);
  addLights(g,{c:0x8fa8c8,i:0.4,p:[30,60,30]},{c:0x161e2a,i:0.85});
  return {group:g,update(t,dt){rain.update(t,dt);mist.update(t);
    boat.rotation.z=Math.sin(t*0.7)*0.03;
  }};
}
function makeBoatShape(s){
  const g=new THREE.Group();
  const hull=new THREE.Mesh(new THREE.CylinderGeometry(0.5,1.1,7,10,1,true),new THREE.MeshPhongMaterial({color:0x241c12}));
  hull.rotation.z=Math.PI/2; hull.scale.y=1; g.add(hull);
  const deck=new THREE.Mesh(new THREE.BoxGeometry(4.5,0.2,1.6),new THREE.MeshPhongMaterial({color:0x2a2016}));
  deck.position.y=0.5; g.add(deck);
  const canopy=new THREE.Mesh(new THREE.CylinderGeometry(0.9,1.1,2.6,8),new THREE.MeshPhongMaterial({color:0x1c150c}));
  canopy.rotation.z=Math.PI/2; canopy.position.set(-0.6,1.4,0); g.add(canopy);
  g.scale.setScalar(s); return g;
}
function bPingming(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x12161e}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const water=new THREE.Mesh(new THREE.PlaneGeometry(200,120),new THREE.MeshPhongMaterial({color:0x141d29,shininess:70}));
  water.rotation.x=-Math.PI/2; water.position.set(0,0,-34); g.add(water);
  const mountain=new THREE.Mesh(new THREE.ConeGeometry(30,44,6),new THREE.MeshBasicMaterial({color:0x0d131c}));
  mountain.position.set(-34,20,-90); g.add(mountain);
  const mount2=new THREE.Mesh(new THREE.ConeGeometry(18,26,5),new THREE.MeshBasicMaterial({color:0x0c1119}));
  mount2.position.set(-62,11,-78); g.add(mount2);
  const f1=makeFigure(1.0); f1.position.set(2,0,2); f1.rotation.y=2.6; g.add(f1);
  const f2=makeFigure(0.95); f2.position.set(0.2,0,0.6); f2.rotation.y=3.4; g.add(f2);
  const boat=makeBoatShape(3.4); boat.position.set(4,0.7,-16); boat.rotation.y=1.9; g.add(boat);
  const mist=makeMist({n:8,spread:[150,20,100],pos:[0,8,-40],scale:65,color:0x7c8ba0,op:0.1});
  g.add(mist.g);
  addLights(g,{c:0x9ab8d8,i:0.55,p:[-20,50,40]},{c:0x1e2836,i:0.85});
  return {group:g,update(t,dt){mist.update(t);
    boat.position.z-=0.012; boat.position.x+=0.006;
    f2.rotation.y=3.4+Math.sin(t*0.5)*0.06;
  }};
}
function bYuhu(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(60,40),new THREE.MeshPhongMaterial({color:0x0e141d}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const table=new THREE.Mesh(new THREE.CylinderGeometry(7,7.6,1.6,24),new THREE.MeshPhongMaterial({color:0x1a140c}));
  table.position.y=-0.8; g.add(table);
  const jade=new THREE.MeshPhongMaterial({color:0xbfe0d8,emissive:0x1e3a34,shininess:140,transparent:true,opacity:0.55});
  const body=new THREE.Mesh(new THREE.LatheGeometry(
    [[0,0],[1.1,0.05],[1.5,0.4],[1.65,1.1],[1.45,2.0],[0.95,2.6],[0.85,2.9]].map(p=>new THREE.Vector2(p[0],p[1])),28),jade);
  body.position.y=1.2; g.add(body);
  const neck=new THREE.Mesh(new THREE.CylinderGeometry(0.5,0.55,0.7,16),jade);
  neck.position.y=4.1; g.add(neck);
  const lip=new THREE.Mesh(new THREE.TorusGeometry(0.5,0.12,8,20),jade);
  lip.rotation.x=Math.PI/2; lip.position.y=4.45; g.add(lip);
  const heart=new THREE.Mesh(new THREE.SphereGeometry(0.62,16,12),
    new THREE.MeshBasicMaterial({color:0xdff2ff}));
  heart.position.y=2.4; g.add(heart);
  const hglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xbfe8ff,
    transparent:true,opacity:0.6,depthWrite:false,blending:THREE.AdditiveBlending}));
  hglow.scale.set(6,6,1); hglow.position.y=2.4; g.add(hglow);
  const jadeLight=new THREE.PointLight(0xbfe8ff,0.7,30); jadeLight.position.set(0,3,2); g.add(jadeLight);
  const mist=makeMist({n:6,spread:[80,14,60],pos:[0,6,-24],scale:45,color:0x7c8ba0,op:0.07});
  g.add(mist.g);
  const ctl={t:99};
  addLights(g,{c:0x9ab8d8,i:0.5,p:[20,40,30]},{c:0x1a2430,i:0.85});
  return {group:g,update(t,dt){
    mist.update(t); ctl.t+=dt;
    heart.position.y=2.4+Math.sin(t*1.4)*0.08;
    hglow.material.opacity=0.5+0.18*Math.sin(t*1.4);
    jadeLight.intensity=0.7+0.2*Math.sin(t*1.1);
  },click(){
    if(ctl.t<2.2)return;
    ctl.t=0; bell();
    hglow.scale.set(9,9,1); jadeLight.intensity=1.6;
    const fl=$('#flash'); fl.textContent='一片冰心在玉壶'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverRain,
  cam:{f:[0,9,54],t:[0,9,50],lf:[0,8,-40],lt:[0,8,-40]},
  sky:()=>SK({star:0.3,ms:0.7,moon:new THREE.Vector3(-60,80,-160),fd:0.007}) },
{ name:'寒雨连江',dwell:14,river:0.02,build:bRainNight,
  cam:{f:[0,8,40],t:[0,7.5,36],lf:[0,6,-24],lt:[0,6,-28]},
  sky:()=>SK({star:0.12,ms:0.6,moon:new THREE.Vector3(-60,70,-150),fd:0.010}) },
{ name:'楚山孤',dwell:14,river:0.02,build:bPingming,
  cam:{f:[0,7,34],t:[0,6.5,30],lf:[0,6,-30],lt:[-20,8,-70]},
  sky:()=>SK({star:0.15,ms:0.55,moon:new THREE.Vector3(-70,60,-150),fd:0.008}) },
{ name:'冰心玉壶',dwell:16,river:0.015,build:bYuhu,
  cam:{f:[0,6,26],t:[0,5.5,24],lf:[0,3,-2],lt:[0,3.4,-2]},
  sky:()=>SK({star:0.25,ms:0.6,moon:new THREE.Vector3(-60,70,-150),fd:0.008}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 冰心玉壶'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','芙蓉楼送辛渐。唐，王昌龄。寒雨连江夜入吴，平明送客楚山孤。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重送辛渐','初识少伯，尚需共读','渐入佳境，再诵几遍','冰心可鉴，澄澈见底','深得少伯高洁','少伯知己，玉壶同光'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
