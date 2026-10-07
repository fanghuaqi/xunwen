#!/usr/bin/env node
/* build-suxinshi.js —— 主会话直接生产《宿新市徐公店》：从参考实现确定性拼装 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'su-xinshi/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};

/* ---------- 1. 标题与封面文案 ---------- */
rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 宿新市徐公店 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>宿新市徐公店</h1>\n      <div class="dyn">宋 · 杨万里</div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>',
  '<p>三重意境，随诗句次第展开：篱落疏疏的小径、树头未成阴的新绿，追一只黄蝶跑进深金黄的菜花田——蝶与花同色，无处可寻。</p>\n      <p>边读诗，边走进杨万里笔下那个活泼明快的暮春村店。</p>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">宿新市徐公店<small>循 文 入 境 · 杨万里</small></div>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>店小 · 春深</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);

/* ---------- 2. CSS 换肤（青绿春晓·菜花黄蝶） ---------- */
rep('--gold:#d4af37', '--gold:#c9c95f', 1);
rep('--ink:#e8dcc0', '--ink:#eef4e6', 1);
rep('--dim:#9b8d6e', '--dim:#7f9a78', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(8,16,12,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(201,201,95,.28)', 1);
rep('html,body{width:100%;height:100%;overflow:hidden;background:#05070d}', 'html,body{width:100%;height:100%;overflow:hidden;background:#0a1410}', 1);
rep('#err{position:fixed;inset:0;z-index:99;display:none;align-items:center;justify-content:center;background:#05070d', '#err{position:fixed;inset:0;z-index:99;display:none;align-items:center;justify-content:center;background:#0a1410', 1);
rep('background:radial-gradient(ellipse at 50% 60%,rgba(5,8,15,.25),rgba(4,6,11,.82))', 'background:radial-gradient(ellipse at 50% 60%,rgba(6,14,10,.25),rgba(4,10,7,.82))', 1);
rep('background:radial-gradient(ellipse at 50% 45%,rgba(6,9,16,.42),rgba(4,6,11,.9))', 'background:radial-gradient(ellipse at 50% 45%,rgba(6,14,10,.42),rgba(4,10,7,.9))', 1);
rep('rgba(212,175,55,.35)', 'rgba(201,201,95,.35)', 1);
rep('rgba(212,175,55,.4)', 'rgba(201,201,95,.4)', 2);
rep('rgba(212,175,55,.5)', 'rgba(201,201,95,.5)', 1);
rep('rgba(212,175,55,.8)', 'rgba(201,201,95,.8)', 2);
rep('rgba(212,175,55,.25)', 'rgba(201,201,95,.25)', 1);
rep('rgba(212,175,55,.14)', 'rgba(201,201,95,.14)', 1);
rep('rgba(232,220,192,.25)', 'rgba(238,244,230,.25)', 1);
rep('rgba(232,220,192,.30)', 'rgba(238,244,230,.30)', 1);
rep('color:#5a5340', 'color:#5a7a5f', 1);
rep('color:#6f664f', 'color:#6f8a6f', 1);
rep('background:#0b101c', 'background:#0b1410', 1);

/* ---------- 3. JS 常量换肤 ---------- */
rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x0e1d16,0.0045)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x081009)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x081009)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x0e1d16)", 1);

/* ---------- 4. POEM / CN / QUIZ ---------- */
const POEM = `const POEM = [
{ name:'篱落新绿', jing:'稀疏的篱笆，一条小径伸向深处，树头新绿还遮不成荫。',
  segs:[{c:'篱落疏疏一径深，树头新绿未成阴。', p:py('lí luò shū shū yī jìng shēn shù tóu xīn lǜ wèi chéng yīn')}],
  read:'篱落疏疏一径深，树头新绿未成阴。',
  yisi:'篱笆稀稀落落，一条小路通向深处；树上的花瓣纷纷飘落，但新叶刚刚长出还未形成树荫。',
  zhu:[['篱落','篱笆'],['疏疏','稀疏，稀稀落落的样子'],['一径深','一条小路很远很远'],['阴','同“荫”，树荫']] },
{ name:'急走追蝶', jing:'孩童奔跑起来，追一只黄色的蝴蝶。',
  segs:[{c:'儿童急走追黄蝶，', p:py('ér tóng jí zǒu zhuī huáng dié')}],
  read:'儿童急走追黄蝶，',
  yisi:'小孩子飞快地奔跑着，追赶黄色的蝴蝶。',
  zhu:[['急走','飞快地奔跑'],['追','追赶']] },
{ name:'花深蝶隐', jing:'蝴蝶飞进金黄的菜花丛中，再也找不到了。',
  segs:[{c:'飞入菜花无处寻。', p:py('fēi rù cài huā wú chù xún')}],
  read:'飞入菜花无处寻。',
  yisi:'蝴蝶飞到金黄的菜花丛中，和菜花混在一起，孩子们再也找不到它了。',
  zhu:[['菜花','油菜花'],['无处寻','没有地方再找到它']] },
];`;
const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点未找到'); fail++; } else h = h.replace(mPoem[0], POEM);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const QUIZ = `const QUIZ = [
 {q:'「儿童急走追黄蝶」的下一句是？', o:['飞入菜花无处寻','树头新绿未成阴','篱落疏疏一径深'], a:0},
 {q:'「篱落疏疏一径深」中「篱落」指的是？', o:['篱笆','飘落的叶子','小村落'], a:0},
 {q:'《宿新市徐公店》的作者是哪位诗人？', o:['范成大','杨万里','陆游'], a:1},
 {q:'「树头新绿未成阴」写的是怎样的景象？', o:['树叶枯黄飘落','新叶尚小还未成树荫','树上开满了花'], a:1},
 {q:'黄蝶飞入菜花后为什么「无处寻」？', o:['蝴蝶飞走了','天太黑看不见','蝶与菜花同为黄色，难以分辨'], a:2},
];`;
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点未找到'); fail++; } else h = h.replace(mQuiz[0], QUIZ);

/* ---------- 5. 场景 builders（bCover..境定义 注释前整体替换） ---------- */
const BUILDERS = `function bCoverInn(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),
    new THREE.MeshPhongMaterial({color:0x0d2418,shininess:8}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const path=new THREE.Mesh(new THREE.PlaneGeometry(5,80),new THREE.MeshPhongMaterial({color:0x2a2418}));
  path.rotation.x=-Math.PI/2; path.position.set(0,0.02,-10); g.add(path);
  const motes=makeGlow({n:90,box:[120,22,90],pos:[0,8,-20],color:0xcfe8a8,size:7,speed:0.04,rise:0,maxA:0.5});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[160,26,110],pos:[0,7,-30],scale:60,color:0x8fb89a,op:0.09});
  g.add(mist.g);
  addLights(g,{c:0xaecfa8,i:0.6,p:[50,80,40]},{c:0x24382c,i:0.7});
  return {group:g,update(t){motes.update(t);mist.update(t);}};
}
function bHedge(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),
    new THREE.MeshPhongMaterial({color:0x102a1a,shininess:6}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const path=new THREE.Mesh(new THREE.PlaneGeometry(4.5,90),new THREE.MeshPhongMaterial({color:0x2a2418}));
  path.rotation.x=-Math.PI/2; path.position.set(0,0.02,-20); g.add(path);
  const fenceMat=new THREE.MeshPhongMaterial({color:0x3a2e1c,shininess:4});
  for(let i=0;i<14;i++){
    const p=new THREE.Mesh(new THREE.BoxGeometry(0.35,4.2,0.35),fenceMat);
    p.position.set(-24+i*3.7,2.1,8); p.rotation.y=rnd(-0.08,0.08); g.add(p);
  }
  [[1.2,7.6],[2.4,6.4]].forEach(r=>{
    const rail=new THREE.Mesh(new THREE.BoxGeometry(52,0.28,0.28),fenceMat);
    rail.position.set(0,r,8); g.add(rail);
  });
  const trunk=new THREE.Mesh(new THREE.CylinderGeometry(0.6,0.9,9,8),
    new THREE.MeshPhongMaterial({color:0x2a2018}));
  trunk.position.set(-14,4.5,-18); g.add(trunk);
  const canopy=new THREE.Group(); g.add(canopy);
  const cm=new THREE.MeshPhongMaterial({color:0x6fae5f,emissive:0x1a3018,shininess:12});
  for(let i=0;i<7;i++){
    const s=new THREE.Mesh(new THREE.SphereGeometry(rnd(2.6,4.2),10,8),cm);
    s.position.set(-14+rnd(-3.4,3.4),9.5+rnd(0,3.4),-18+rnd(-3,3)); canopy.add(s);
  }
  const motes=makeGlow({n:60,box:[90,16,70],pos:[0,6,-8],color:0xcfe8a8,size:7,speed:0.05,rise:0,maxA:0.55});
  g.add(motes.points);
  addLights(g,{c:0xaecfa8,i:0.65,p:[40,70,30]},{c:0x24382c,i:0.75});
  return {group:g,update(t){motes.update(t);
    canopy.rotation.z=Math.sin(t*0.4)*0.02;
  }};
}
function bChase(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),
    new THREE.MeshPhongMaterial({color:0x112c1b,shininess:6}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const path=new THREE.Mesh(new THREE.PlaneGeometry(6,90),new THREE.MeshPhongMaterial({color:0x2a2418}));
  path.rotation.x=-Math.PI/2; path.position.set(0,0.02,-14); g.add(path);
  const boy=makeFigure(0.72); boy.position.set(-2.5,0,2); boy.rotation.y=0.5; g.add(boy);
  const girl=makeFigure(0.66); girl.position.set(1.8,0,0.5); girl.rotation.y=0.42; g.add(girl);
  const butterfly=new THREE.Group();
  const bmat=new THREE.MeshBasicMaterial({color:0xe8d24a,side:THREE.DoubleSide});
  const w1=new THREE.Mesh(new THREE.PlaneGeometry(0.9,0.7),bmat); w1.position.x=-0.4;
  const w2=new THREE.Mesh(new THREE.PlaneGeometry(0.9,0.7),bmat); w2.position.x=0.4;
  butterfly.add(w1,w2); butterfly.scale.setScalar(1.6); g.add(butterfly);
  const tufts=new THREE.InstancedMesh(new THREE.ConeGeometry(0.22,1.6,5),
    new THREE.MeshPhongMaterial({color:0x5a9a4e}),80);
  const dummy=new THREE.Object3D();
  for(let i=0;i<80;i++){
    dummy.position.set(rnd(-38,38),0.7,rnd(-45,5));
    dummy.rotation.set(rnd(-0.2,0.2),rnd(0,6.28),rnd(-0.2,0.2));
    dummy.updateMatrix(); tufts.setMatrixAt(i,dummy.matrix);
  }
  g.add(tufts);
  addLights(g,{c:0xaecfa8,i:0.7,p:[30,70,40]},{c:0x24382c,i:0.75});
  return {group:g,update(t,dt){
    motesU(t);
    const bob=Math.abs(Math.sin(t*5.2));
    boy.position.y=bob*0.32; girl.position.y=Math.abs(Math.sin(t*5.2+1.2))*0.3;
    const bx=Math.sin(t*1.1)*7, bz=-8+Math.sin(t*0.7)*6;
    butterfly.position.set(bx,3.6+Math.sin(t*2.3)*0.9,bz);
    butterfly.rotation.y=t*0.9;
    const f=Math.sin(t*26)*0.9; w1.rotation.y=f; w2.rotation.y=-f;
  }};
  function motesU(t){}
}
function bFlowerField(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),
    new THREE.MeshPhongMaterial({color:0x1a3018,shininess:6}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const N=320;
  const stems=new THREE.InstancedMesh(new THREE.CylinderGeometry(0.06,0.1,1.8,5),
    new THREE.MeshPhongMaterial({color:0x4a7a3e}),N);
  const heads=new THREE.InstancedMesh(new THREE.SphereGeometry(0.62,8,6),
    new THREE.MeshPhongMaterial({color:0xd8c94a,emissive:0x3a3208,shininess:20}),N);
  const base=[];
  const dummy=new THREE.Object3D();
  for(let i=0;i<N;i++){
    const pr=6+Math.sqrt(Math.random())*46, pa=rnd(0,6.283);
    const x=Math.sin(pa)*pr, z=-14+Math.cos(pa)*pr*0.8;
    base.push({x,z,ph:rnd(0,6.283),h:rnd(0.8,1.25)});
    dummy.position.set(x,0.9*base[i].h,z); dummy.scale.setScalar(base[i].h);
    dummy.updateMatrix(); stems.setMatrixAt(i,dummy.matrix);
    dummy.position.set(x,1.9*base[i].h,z); dummy.updateMatrix(); heads.setMatrixAt(i,dummy.matrix);
  }
  stems.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  heads.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
  g.add(stems,heads);
  const butterfly=new THREE.Group();
  const bmat=new THREE.MeshBasicMaterial({color:0xe8d24a,side:THREE.DoubleSide});
  const w1=new THREE.Mesh(new THREE.PlaneGeometry(0.9,0.7),bmat); w1.position.x=-0.4;
  const w2=new THREE.Mesh(new THREE.PlaneGeometry(0.9,0.7),bmat); w2.position.x=0.4;
  butterfly.add(w1,w2); butterfly.scale.setScalar(1.7); g.add(butterfly);
  const burst=makeBurst({n:80,color:0xffe9a0,pos:[0,4,-6]}); g.add(burst.points);
  const ctl={t:99};
  const mist=makeMist({n:8,spread:[130,20,90],pos:[0,6,-16],scale:55,color:0x8fb89a,op:0.08});
  g.add(mist.g);
  addLights(g,{c:0xaecfa8,i:0.7,p:[30,70,40]},{c:0x24382c,i:0.8});
  return {group:g,update(t,dt){
    mist.update(t); burst.update(t);
    ctl.t+=dt;
    const sway=Math.sin(t*1.4)*0.09;
    for(let i=0;i<N;i++){
      const b=base[i];
      dummy.position.set(b.x,0.9*b.h,b.z);
      dummy.rotation.set(sway*(0.6+b.ph*0.05),0,sway);
      dummy.scale.setScalar(b.h); dummy.updateMatrix(); stems.setMatrixAt(i,dummy.matrix);
      dummy.position.set(b.x,1.9*b.h+Math.sin(t*1.4+b.ph)*0.06,b.z);
      dummy.updateMatrix(); heads.setMatrixAt(i,dummy.matrix);
    }
    stems.instanceMatrix.needsUpdate=true; heads.instanceMatrix.needsUpdate=true;
    const cyc=(t*0.12)%1;
    const flying=cyc<0.62;
    if(flying){
      const k=cyc/0.62;
      butterfly.visible=true;
      butterfly.position.set(lerp(-16,4,k)+Math.sin(t*3)*0.8, 3+Math.sin(t*2.1)*1.1+k*1.2, lerp(4,-10,k));
    }else{
      const k=(cyc-0.62)/0.38;
      butterfly.position.set(4+k*3, 3.2-k*2.0, -10-k*4);
      butterfly.visible=k<0.92;
    }
    const f=Math.sin(t*24)*0.9; w1.rotation.y=f; w2.rotation.y=-f;
    butterfly.rotation.y=t*0.8;
  },click(){
    if(ctl.t<4)return;
    ctl.t=0; burst.fire(); bell();
    const fl=$('#flash'); fl.textContent='飞入菜花无处寻'; fl.classList.remove('go');
    void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点未找到'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

/* ---------- 6. STAGES ---------- */
const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverInn,
  cam:{f:[0,10,62],t:[0,10,58],lf:[0,8,-40],lt:[0,8,-40]},
  sky:()=>SK({star:0.55,ms:1.15,moon:new THREE.Vector3(-70,100,-180),fd:0.0048}) },
{ name:'篱落新绿',dwell:14,river:0.02,build:bHedge,
  cam:{f:[0,8,42],t:[0,8,38],lf:[0,5,-12],lt:[0,5,-16]},
  sky:()=>SK({star:0.6,ms:1.2,moon:new THREE.Vector3(-70,100,-180),fd:0.005}) },
{ name:'急走追蝶',dwell:14,river:0.02,build:bChase,
  cam:{f:[0,6.5,34],t:[-3,6.5,30],lf:[0,4,-6],lt:[2,4,-10]},
  sky:()=>SK({star:0.65,ms:1.2,moon:new THREE.Vector3(-60,95,-170),fd:0.0055}) },
{ name:'花深蝶隐',dwell:16,river:0.02,build:bFlowerField,
  cam:{f:[0,7,38],t:[0,7,32],lf:[0,4,-8],lt:[0,4,-12]},
  sky:()=>SK({star:0.7,ms:1.3,moon:new THREE.Vector3(-50,90,-160),fd:0.006}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点未找到'); fail++; } else h = h.replace(mStages[0], STAGES);

/* ---------- 7. 数量联动 ---------- */
rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 追蝶去也'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','宿新市徐公店。宋，杨万里。篱落疏疏一径深，树头新绿未成阴。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];",
  "const words=['再游一次，追蝶去也','初识诚斋，尚需共读','渐入佳境，再诵几遍','童趣会心，一笑而过','深得诚斋妙趣','村店知己，春深蝶隐'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
