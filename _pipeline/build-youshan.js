#!/usr/bin/env node
/* build-youshan.js —— 《游山西村》夜宴金彩·山村暖黄 · 柳暗花明转场 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'you-shanxicun/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(217,201,138,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 游山西村 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>游山西村</h1>\n      <div class="dyn">宋 · 陆游</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">游山西村<small>循 文 入 境 · 陆 游</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：农家腊酒虽浑、鸡豚留客，山重水复疑无路——转过柳暗，花明处豁然又一村。</p>\n      <p>边读诗，边走进陆游笔下那个淳朴好客、峰回路转的山村。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>村现 · 路明</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击柳暗花明转场 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 游山西村 —— Three.js 沉浸式诗词课件', 1);

rep('--gold:#d4af37', '--gold:#d9c98a', 1);
rep('--ink:#e8dcc0', '--ink:#ece4cf', 1);
rep('--dim:#9b8d6e', '--dim:#9a8a6a', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(14,10,6,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(217,201,138,.28)', 1);
rep('background:#05070d', 'background:#120d08', 2);
rep('rgba(4,6,11,.82)', 'rgba(10,7,4,.82)', 1);
rep('rgba(4,6,11,.9)', 'rgba(10,7,4,.9)', 1);
rep('rgba(212,175,55,.35)', A('.35'), 1);
rep('rgba(212,175,55,.4)', A('.4'), 2);
rep('rgba(212,175,55,.5)', A('.5'), 1);
rep('rgba(212,175,55,.6)', A('.6'), 1);
rep('rgba(212,175,55,.8)', A('.8'), 2);
rep('rgba(212,175,55,.25)', A('.25'), 1);
rep('rgba(212,175,55,.14)', A('.14'), 1);
rep('rgba(212,175,55,.3)', A('.3'), 1);
rep('rgba(232,220,192,.25)', 'rgba(236,228,207,.22)', 1);
rep('rgba(232,220,192,.30)', 'rgba(236,228,207,.26)', 1);
rep('color:#5a5340', 'color:#7a6a50', 1);
rep('color:#6f664f', 'color:#8a7a5f', 1);
rep('background:#0b101c', 'background:#1a130a', 1);

rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x1a120a,0.0048)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x0a0705)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x0a0705)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x1a120a)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x141008),hor:C(0x2a2012)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'农家腊酒', jing:'不要笑话农家腊月酿的酒浑浊，丰年待客的菜肴足够丰盛。',
  segs:[{c:'莫笑农家腊酒浑，丰年留客足鸡豚。', p:py('mò xiào nóng jiā là jiǔ hún fēng nián liú kè zú jī tún')}],
  read:'莫笑农家腊酒浑，丰年留客足鸡豚。',
  yisi:'不要笑话农家腊月酿的酒浑浊不清，丰收年景他们待客的菜肴足够丰盛，有鸡有肉。',
  zhu:[['腊酒','腊月里酿造的酒'],['浑','浑浊，酒以清浊贵'],['豚','小猪，诗中代指猪肉'],['足','足够，丰盛']] },
{ name:'山重水复', jing:'山峦重叠、水道迂回，正怀疑前方无路可走了。',
  segs:[{c:'山重水复疑无路，', p:py('shān chóng shuǐ fù yí wú lù')}],
  read:'山重水复疑无路，',
  yisi:'山峦重重叠叠，溪水迂回曲折，正怀疑前面没有路了。',
  zhu:[['重','重叠'],['复','迂回曲折'],['疑','怀疑，以为']] },
{ name:'柳暗花明', jing:'柳色深绿、花光明艳，眼前豁然开朗，又是一个村庄。',
  segs:[{c:'柳暗花明又一村。', p:py('liǔ àn huā míng yòu yī cūn')}],
  read:'柳暗花明又一村。',
  yisi:'走过柳树浓绿、花光明艳之处，眼前豁然开朗，又出现一个村庄。',
  zhu:[['柳暗花明','柳色浓绿，花光明艳；后成成语，比喻困境中出现转机'],['又一村','又一个村庄']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「山重水复疑无路」的下一句是？', o:['柳暗花明又一村','丰年留客足鸡豚','莫笑农家腊酒浑'], a:0},
 {q:'「丰年留客足鸡豚」中「豚」指的是？', o:['小猪，代指肉菜','河豚','小溪'], a:0},
 {q:'《游山西村》的作者是？', o:['范成大','杨万里','陆游'], a:2},
 {q:'成语「柳暗花明」现在比喻什么？', o:['春天的田园景色','困境中出现转机和希望','柳树成荫的村庄'], a:1},
 {q:'「莫笑农家腊酒浑」中「浑」的意思是？', o:['浑浊不清','浑厚有力','浑身'], a:0},
];`);

const BUILDERS = `function bCoverShan(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x171008}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  for(let i=0;i<3;i++){
    const r=new THREE.Mesh(new THREE.ConeGeometry(60-i*8,26-i*4,5),new THREE.MeshBasicMaterial({color:0x0e0a06}));
    r.position.set(rnd(-70,70),10+i*4,-90-i*40); g.add(r);
  }
  const win=new THREE.Mesh(new THREE.PlaneGeometry(3,3.6),new THREE.MeshBasicMaterial({color:0xd9a05a}));
  win.position.set(-26,4,-52); g.add(win);
  const motes=makeGlow({n:60,box:[130,26,90],pos:[0,9,-40],color:0xd9c98a,size:7,speed:0.04,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xd9c98a,i:0.5,p:[40,70,30]},{c:0x2a2012,i:0.85});
  return {group:g,update(t){motes.update(t);}};
}
function bNongJia(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(70,40),new THREE.MeshPhongMaterial({color:0x1a130a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const wall=new THREE.Mesh(new THREE.BoxGeometry(16,7,1.2),new THREE.MeshPhongMaterial({color:0x2a2016}));
  wall.position.set(0,3.5,-14); g.add(wall);
  const roof=new THREE.Mesh(new THREE.ConeGeometry(12.5,3.6,4),new THREE.MeshPhongMaterial({color:0x1c130a}));
  roof.rotation.y=Math.PI/4; roof.position.set(0,8.8,-14); g.add(roof);
  const door=new THREE.Mesh(new THREE.BoxGeometry(3.4,4.6,0.3),new THREE.MeshPhongMaterial({color:0x120d08}));
  door.position.set(-3,2.3,-13.2); g.add(door);
  const win=new THREE.Mesh(new THREE.PlaneGeometry(3.4,2.8),new THREE.MeshBasicMaterial({color:0xe8b45a}));
  win.position.set(3.2,3.6,-13.2); g.add(win);
  const wl=new THREE.PointLight(0xe8b45a,1.1,26); wl.position.set(3.2,3.6,-11); g.add(wl);
  const jar=makeJar(1.3); jar.position.set(5.5,0,-9); g.add(jar);
  const jar2=makeJar(1.0); jar2.position.set(7.2,0,-10.2); g.add(jar2);
  const table=new THREE.Mesh(new THREE.BoxGeometry(4.6,1.4,2.4),new THREE.MeshPhongMaterial({color:0x241a10}));
  table.position.set(-1,0.7,-6); g.add(table);
  const bowl=new THREE.Mesh(new THREE.CylinderGeometry(0.5,0.3,0.4,10),new THREE.MeshPhongMaterial({color:0xc9c2b0}));
  bowl.position.set(-1.6,1.6,-6); g.add(bowl);
  const bowl2=bowl.clone(); bowl2.position.x=-0.2; g.add(bowl2);
  addLights(g,{c:0xd9c98a,i:0.55,p:[30,60,30]},{c:0x2a2012,i:0.85});
  return {group:g,update(t){wl.intensity=1.1+Math.sin(t*6.1)*0.12;}};
}
function bShanchong(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x140f08}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  for(let i=0;i<4;i++){
    const r=new THREE.Mesh(new THREE.ConeGeometry(46-i*6,20+i*7,5),new THREE.MeshBasicMaterial({color:0x0f0b06}));
    r.position.set(i*4-4,9+i*2.5,-46-i*26); g.add(r);
  }
  const water=new THREE.Mesh(new THREE.PlaneGeometry(40,90),new THREE.MeshPhongMaterial({color:0x0e1a20,shininess:60}));
  water.rotation.x=-Math.PI/2; water.position.set(-12,0.04,-30); g.add(water);
  const rock=new THREE.Mesh(new THREE.DodecahedronGeometry(7,0),new THREE.MeshPhongMaterial({color:0x241c10}));
  rock.position.set(6,3.4,-42); g.add(rock);
  const mist=makeMist({n:12,spread:[150,18,120],pos:[0,4,-46],scale:70,color:0x4a4030,op:0.14});
  g.add(mist.g);
  addLights(g,{c:0xcabf9a,i:0.4,p:[-30,60,30]},{c:0x2a2012,i:0.8});
  return {group:g,update(t,dt){mist.update(t);}};
}
function bLiuAnHuaming(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(90,40),new THREE.MeshPhongMaterial({color:0x15100a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const willow=new THREE.Group();
  const wm=new THREE.MeshPhongMaterial({color:0x1a2414,transparent:true,opacity:0.95});
  for(let i=0;i<6;i++){
    const s=new THREE.Mesh(new THREE.SphereGeometry(rnd(4,6.5),10,8),wm);
    s.position.set(rnd(-26,-14),rnd(4,12),rnd(-16,-8)); willow.add(s);
  }
  for(let i=0;i<10;i++){
    const w=new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.02,7,4),wm);
    w.position.set(rnd(-24,-16),rnd(3,8),rnd(-13,-9)); willow.add(w);
  }
  g.add(willow);
  const village=new THREE.Group(); g.add(village);
  for(let i=0;i<5;i++){
    const vx=-6+i*9, vz=-30-(i%2)*12;
    const bld=new THREE.Mesh(new THREE.BoxGeometry(7,4.6,5),new THREE.MeshPhongMaterial({color:0x241c12}));
    bld.position.set(vx,2.3,vz); village.add(bld);
    const rf=new THREE.Mesh(new THREE.ConeGeometry(5.6,2.4,4),new THREE.MeshPhongMaterial({color:0x181008}));
    rf.rotation.y=Math.PI/4; rf.position.set(vx,5.8,vz); village.add(rf);
    const win=new THREE.Mesh(new THREE.PlaneGeometry(1.8,1.6),new THREE.MeshBasicMaterial({color:0xe8b45a}));
    win.position.set(vx+1.6,2.4,vz+2.55); village.add(win);
    const bl=new THREE.Group();
    const bm=new THREE.MeshBasicMaterial({color:0xe8a0b8});
    for(let k=0;k<4;k++){
      const fl=new THREE.Mesh(new THREE.SphereGeometry(0.28,6,5),bm);
      fl.position.set(vx-2.6+rnd(0,1.6),3.4+rnd(0,1.6),vz+2.6+rnd(0,0.6)); bl.add(fl);
    }
    village.add(bl);
  }
  const sun=new THREE.Mesh(new THREE.SphereGeometry(4,16,12),new THREE.MeshBasicMaterial({color:0xf2d8a0}));
  sun.position.set(24,14,-70); g.add(sun);
  willow.traverse(o=>{if(o.material){o.userData.baseOp=o.material.opacity!==undefined?o.material.opacity:1;}});
  const ctl={t:0};
  addLights(g,{c:0xd9c98a,i:0.5,p:[40,60,30]},{c:0x2a2012,i:0.8});
  return {group:g,update(t,dt){
    ctl.t+=dt;
    const p=sstep(2,9,ctl.t%16);
    willow.traverse(o=>{if(o.material&&o.userData.baseOp!==undefined)o.material.opacity=o.userData.baseOp*(1-p*0.75);});
    willow.position.x=-p*9;
    village.traverse(o=>{if(o.material&&o.material.color)o.material.color.copy(o.userData.c0||(o.userData.c0=o.material.color.clone())).multiplyScalar(0.55+0.45*p);});
  },click(){
    if(ctl.t<14)return;
    ctl.t=0; bell();
    const fl=$('#flash'); fl.textContent='柳暗花明又一村'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCoverShan,
  cam:{f:[0,10,60],t:[0,10,56],lf:[0,10,-50],lt:[0,10,-50]},
  sky:()=>SK({star:0.5,ms:1.1,moon:new THREE.Vector3(50,90,-160),fd:0.005}) },
{ name:'农家腊酒',dwell:14,river:0.015,build:bNongJia,
  cam:{f:[0,7,30],t:[0,6.5,26],lf:[0,4,-12],lt:[0,4,-14]},
  sky:()=>SK({star:0.45,ms:1.0,moon:new THREE.Vector3(40,80,-150),fd:0.0055}) },
{ name:'山重水复',dwell:14,river:0.015,build:bShanchong,
  cam:{f:[0,9,40],t:[0,8,34],lf:[0,8,-40],lt:[0,8,-46]},
  sky:()=>SK({star:0.35,ms:0.9,moon:new THREE.Vector3(-60,85,-160),fd:0.008}) },
{ name:'柳暗花明',dwell:16,river:0.015,build:bLiuAnHuaming,
  cam:{f:[0,8,36],t:[0,7.5,30],lf:[-8,5,-14],lt:[4,5,-30]},
  sky:()=>SK({star:0.4,ms:0.9,moon:new THREE.Vector3(-50,80,-150),fd:0.0065}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 柳暗花明'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','游山西村。宋，陆游。莫笑农家腊酒浑，丰年留客足鸡豚。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重访山村','初识放翁，尚需共读','渐入佳境，再诵几遍','峰回路转，会心一笑','深得放翁旷达','放翁知己，花明村现'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
