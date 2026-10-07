#!/usr/bin/env node
/* build-yeshu.js —— 《夜书所见》水墨夜思·寒声灯明 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'yeshu-suojian/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(184,196,221,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 夜书所见 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>夜书所见</h1>\n      <div class="dyn">宋 · 叶绍翁</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">夜书所见<small>循 文 入 境 · 叶绍翁</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：梧叶萧萧送来寒声，江上秋风牵动客愁——而深夜篱落间，还亮着一盏孩童捉蟋蟀的灯。</p>\n      <p>边读诗，边走进叶绍翁笔下那个秋夜江畔的旅人记忆。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>秋深 · 灯明</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击点亮篱灯 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 夜书所见 —— Three.js 沉浸式诗词课件', 1);

rep('--gold:#d4af37', '--gold:#b8c4dd', 1);
rep('--ink:#e8dcc0', '--ink:#e2e8f2', 1);
rep('--dim:#9b8d6e', '--dim:#7e88a0', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(10,13,20,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(184,196,221,.28)', 1);
rep('background:#05070d', 'background:#0d1117', 2);
rep('rgba(4,6,11,.82)', 'rgba(7,10,16,.82)', 1);
rep('rgba(4,6,11,.9)', 'rgba(7,10,16,.9)', 1);
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
rep('background:#0b101c', 'background:#0e141f', 1);

rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x121a24,0.0048)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x090d13)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x090d13)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x121a24)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x0d141b),hor:C(0x19222d)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'梧叶寒声', jing:'萧萧秋风吹动梧桐叶，送来阵阵寒意。',
  segs:[{c:'萧萧梧叶送寒声，', p:py('xiāo xiāo wú yè sòng hán shēng')}],
  read:'萧萧梧叶送寒声，',
  yisi:'萧萧秋风吹动梧桐树的叶子，送来一阵阵寒意。',
  zhu:[['萧萧','风声，形容风吹梧桐叶的声音'],['梧','梧桐树'],['寒声','寒意阵阵的声音']] },
{ name:'秋风客情', jing:'江上的秋风吹动着客游之人的思乡之情。',
  segs:[{c:'江上秋风动客情。', p:py('jiāng shàng qiū fēng dòng kè qíng')}],
  read:'江上秋风动客情。',
  yisi:'江上的秋风吹动着漂泊在外之人的思乡情怀。',
  zhu:[['客情','旅客思乡的心情'],['动','触动，牵动']] },
{ name:'篱落灯明', jing:'知道有孩子在捉蟋蟀——深夜篱笆下，还亮着一盏灯。',
  segs:[{c:'知有儿童挑促织，', p:py('zhī yǒu ér tóng tiǎo cù zhī')},{c:'夜深篱落一灯明。', p:py('yè shēn lí luò yī dēng míng')}],
  read:'知有儿童挑促织，夜深篱落一灯明。',
  yisi:'料想是孩子们在捉蟋蟀——因为夜已深了，篱笆边还亮着一盏灯。',
  zhu:[['挑','用细长的东西拨动'],['促织','蟋蟀，也叫蛐蛐'],['篱落','篱笆']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「萧萧梧叶送寒声」的下一句是？', o:['江上秋风动客情','夜深篱落一灯明','知有儿童挑促织'], a:0},
 {q:'诗中「促织」指的是哪种小昆虫？', o:['蜻蜓','蟋蟀','蜜蜂'], a:1},
 {q:'《夜书所见》的作者是？', o:['叶绍翁','杨万里','杜甫'], a:0},
 {q:'「夜深篱落一灯明」描绘了怎样的画面？', o:['深夜篱笆下亮着一盏灯，孩童正在捉蟋蟀','江边渔火彻夜通明','庙宇里的长明灯'], a:0},
 {q:'全诗借秋夜所见抒发了诗人怎样的情感？', o:['客居在外思念家乡','丰收的喜悦','对儿童的责备'], a:0},
];`);

const BUILDERS = `function makeLeafRain(n){
  const g=new THREE.Group();
  const geo=new THREE.PlaneGeometry(0.8,0.5);
  const mat=new THREE.MeshBasicMaterial({color:0x6a5a3a,side:THREE.DoubleSide,transparent:true,opacity:0.85});
  const arr=[];
  for(let i=0;i<n;i++){
    const m=new THREE.Mesh(geo,mat);
    m.position.set(rnd(-50,50),rnd(1,26),rnd(-40,20));
    m.rotation.set(rnd(0,3),rnd(0,3),rnd(0,3));
    g.add(m); arr.push({m,sp:rnd(1.2,2.6),ph:rnd(0,6.28)});
  }
  return {g,arr,update(t,dt){
    for(const o of arr){
      o.m.position.y-=o.sp*dt;
      o.m.position.x+=Math.sin(t*1.3+o.ph)*dt*1.6;
      o.m.rotation.x+=dt*1.4; o.m.rotation.z+=dt*0.9;
      if(o.m.position.y<0.4)o.m.position.y=26;
    }
  }};
}
function bCoverWu(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x0e1219}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const trunk=new THREE.Mesh(new THREE.CylinderGeometry(0.9,1.5,14,8),new THREE.MeshPhongMaterial({color:0x18141c}));
  trunk.position.set(-12,7,-24); g.add(trunk);
  const crown=new THREE.Group(); g.add(crown);
  for(let i=0;i<6;i++){
    const s=new THREE.Mesh(new THREE.SphereGeometry(rnd(3.4,5.4),9,7),new THREE.MeshPhongMaterial({color:0x141824}));
    s.position.set(-12+rnd(-4,4),13+rnd(0,4),-24+rnd(-3,3)); crown.add(s);
  }
  const leaves=makeLeafRain(24); g.add(leaves.g);
  const mist=makeMist({n:8,spread:[150,22,110],pos:[0,8,-34],scale:65,color:0x7e88a0,op:0.1});
  g.add(mist.g);
  addLights(g,{c:0xb8c4dd,i:0.45,p:[30,60,30]},{c:0x1c2430,i:0.85});
  return {group:g,update(t,dt){leaves.update(t,dt);mist.update(t);
    crown.rotation.z=Math.sin(t*0.6)*0.02;
  }};
}
function bWuye(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x0e1219}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const trunk=new THREE.Mesh(new THREE.CylinderGeometry(1.1,1.8,15,8),new THREE.MeshPhongMaterial({color:0x18141c}));
  trunk.position.set(-4,7.5,-26); g.add(trunk);
  const crown=new THREE.Group(); g.add(crown);
  for(let i=0;i<8;i++){
    const s=new THREE.Mesh(new THREE.SphereGeometry(rnd(4,6.4),9,7),new THREE.MeshPhongMaterial({color:0x141824}));
    s.position.set(-4+rnd(-5,5),14.5+rnd(0,5),-26+rnd(-4,4)); crown.add(s);
  }
  const leaves=makeLeafRain(40); g.add(leaves.g);
  const wind=makeFlow({n:120,box:[110,20,60],pos:[0,9,-16],color:0x8fa2c2,size:18,speed:8,maxA:0.22});
  g.add(wind.points);
  addLights(g,{c:0xb8c4dd,i:0.42,p:[30,60,30]},{c:0x1c2430,i:0.85});
  return {group:g,update(t,dt){
    leaves.update(t,dt); wind.update(t);
    crown.rotation.z=Math.sin(t*0.55)*0.03;
  }};
}
function bQiujiang(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x0d1119}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const water=new THREE.Mesh(new THREE.PlaneGeometry(200,120),new THREE.MeshPhongMaterial({color:0x101823,shininess:75}));
  water.rotation.x=-Math.PI/2; water.position.set(0,0,-30); g.add(water);
  const wind=makeFlow({n:220,box:[130,22,70],pos:[0,10,-24],color:0x8fa2c2,size:22,speed:9,maxA:0.3});
  g.add(wind.points);
  const ke=makeFigure(1.0); ke.position.set(4,0,4); ke.rotation.y=2.4; g.add(ke);
  const reed=new THREE.Group(); g.add(reed);
  const rm=new THREE.MeshPhongMaterial({color:0x1a1f2a});
  for(let i=0;i<12;i++){
    const r=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.12,4.5,4),rm);
    r.position.set(rnd(-30,30),2.2,rnd(-16,-6)); r.rotation.z=rnd(-0.24,0.24); reed.add(r);
  }
  addLights(g,{c:0xb8c4dd,i:0.4,p:[-20,50,30]},{c:0x1c2430,i:0.85});
  return {group:g,update(t,dt){wind.update(t);
    reed.rotation.z=Math.sin(t*1.1)*0.05;
    ke.rotation.y=2.4+Math.sin(t*0.4)*0.05;
  }};
}
function bDengLong(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(70,40),new THREE.MeshPhongMaterial({color:0x0c0f16}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const fenceMat=new THREE.MeshPhongMaterial({color:0x241f18});
  for(let i=0;i<11;i++){
    const p=new THREE.Mesh(new THREE.BoxGeometry(0.3,3.6,0.3),fenceMat);
    p.position.set(-16+i*3.2,1.8,4); p.rotation.y=rnd(-0.1,0.1); g.add(p);
  }
  [[1.0,2.9]].forEach(h=>{const r=new THREE.Mesh(new THREE.BoxGeometry(34,0.24,0.24),fenceMat);
    r.position.set(0,h,4); g.add(r);});
  const lampG=new THREE.Group(); g.add(lampG);
  const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.1,0.14,6.5,6),fenceMat);
  pole.position.set(-7,3.25,0); lampG.add(pole);
  const arm=new THREE.Mesh(new THREE.BoxGeometry(1.6,0.12,0.12),fenceMat);
  arm.position.set(0.7,6.2,0); lampG.add(arm);
  const lamp=new THREE.Mesh(new THREE.SphereGeometry(0.8,12,10),new THREE.MeshBasicMaterial({color:0xe8a44a}));
  lamp.position.set(1.3,5.6,0); lampG.add(lamp);
  const lampGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8a44a,
    transparent:true,opacity:0.55,depthWrite:false,blending:THREE.AdditiveBlending}));
  lampGlow.scale.set(7,7,1); lampGlow.position.copy(lamp.position); lampG.add(lampGlow);
  const lampLight=new THREE.PointLight(0xe8a44a,1.0,30); lampLight.position.set(1.3,5.6,0.5); lampG.add(lampLight);
  const c1=makeFigure(0.6); c1.position.set(4.5,0,-1.5); c1.rotation.y=-1.1; c1.scale.setScalar(0.6); g.add(c1);
  const c2=makeFigure(0.52); c2.position.set(6.2,0,0.4); c2.rotation.y=-2.2; c2.scale.setScalar(0.52); g.add(c2);
  const ctl={t:99,lit:1};
  addLights(g,{c:0xb8c4dd,i:0.4,p:[-20,50,30]},{c:0x1a2230,i:0.85});
  return {group:g,update(t,dt){
    ctl.t+=dt;
    const fl=Math.sin(t*5.7)*0.06+Math.sin(t*13.3)*0.03;
    const boost=ctl.lit>1?0.45:0;
    lamp.material.color.setHex(0xe8a44a);
    lampGlow.material.opacity=Math.min(0.95,0.5+fl*3+boost);
    lampLight.intensity=1.0+fl*2+boost*2.2;
    lampGlow.scale.setScalar(7+boost*8+fl*0.6);
    c1.rotation.z=Math.sin(t*1.8)*0.08; c2.rotation.z=Math.sin(t*1.8+1.4)*0.08;
  },click(){
    if(ctl.t<2.6)return;
    ctl.t=0; ctl.lit+=1; bell();
    const fl=$('#flash'); fl.textContent='夜深篱落一灯明'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCoverWu,
  cam:{f:[0,9,48],t:[0,9,44],lf:[0,9,-24],lt:[0,9,-24]},
  sky:()=>SK({star:0.45,ms:1.05,moon:new THREE.Vector3(40,85,-150),fd:0.005}) },
{ name:'梧叶寒声',dwell:14,river:0.015,build:bWuye,
  cam:{f:[0,7,36],t:[0,6.5,32],lf:[-4,9,-26],lt:[-4,10,-26]},
  sky:()=>SK({star:0.35,ms:0.8,moon:new THREE.Vector3(45,78,-150),fd:0.0055}) },
{ name:'秋风客情',dwell:14,river:0.015,build:bQiujiang,
  cam:{f:[0,7,40],t:[0,6.5,36],lf:[0,6,-24],lt:[0,6,-28]},
  sky:()=>SK({star:0.3,ms:0.75,moon:new THREE.Vector3(50,75,-150),fd:0.006}) },
{ name:'篱落灯明',dwell:16,river:0.015,build:bDengLong,
  cam:{f:[0,6.5,30],t:[0,6,27],lf:[0,5,-2],lt:[0,4.5,-4]},
  sky:()=>SK({star:0.2,ms:0.7,moon:new THREE.Vector3(60,70,-150),fd:0.007}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 点亮篱灯'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','夜书所见。宋，叶绍翁。萧萧梧叶送寒声，江上秋风动客情。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，夜泊重来','初识绍翁，尚需共读','渐入佳境，再诵几遍','一灯如豆，秋意顿生','深得绍翁笔意','灯下知己，秋夜同游'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
