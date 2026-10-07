#!/usr/bin/env node
/* build-yuanri.js —— 《元日》夜宴金彩·新春暖金（爆竹+桃符） */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'yuanri/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(212,176,80,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 元日 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>元日</h1>\n      <div class="dyn">宋 · 王安石</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">元日<small>循 文 入 境 · 王安石</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：爆竹声声送走旧岁，春风送暖、屠苏畅饮，千门万户的曈曈朝阳里，新桃符换下旧桃符。</p>\n      <p>边读诗，边走进王安石笔下那个爆竹声声、旭日曈曈的新年早晨。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>爆竹 · 新符</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击爆竹声起桃符换新 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 元日 —— Three.js 沉浸式诗词课件', 1);

rep('--gold:#d4af37', '--gold:#d4b050', 1);
rep('--ink:#e8dcc0', '--ink:#f0e6d0', 1);
rep('--dim:#9b8d6e', '--dim:#a08a5e', 1);
rep('--paper:rgba(9,13,22,.58)', '--paper:rgba(16,11,5,.58)', 1);
rep('--line:rgba(212,175,55,.28)', '--line:rgba(212,176,80,.28)', 1);
rep('background:#05070d', 'background:#120d06', 2);
rep('rgba(4,6,11,.82)', 'rgba(12,8,3,.82)', 1);
rep('rgba(4,6,11,.9)', 'rgba(12,8,3,.9)', 1);
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
rep('color:#5a5340', 'color:#8a7a50', 1);
rep('color:#6f664f', 'color:#8a7a5f', 1);
rep('background:#0b101c', 'background:#1a130a', 1);

rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x1a1208,0.0048)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x0e0a05)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x0e0a05)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x1a1208)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x1a1208),hor:C(0x2e2010)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'爆竹除岁', jing:'爆竹声中旧的一年过去了。',
  segs:[{c:'爆竹声中一岁除，', p:py('bào zhú shēng zhōng yī suì chú')}],
  read:'爆竹声中一岁除，',
  yisi:'在阵阵爆竹声中，旧的一年过去了。',
  zhu:[['爆竹','古人烧竹子使爆裂发声，用来驱鬼避邪，后来演变成放鞭炮'],['一岁除','一年过去了']] },
{ name:'春风屠苏', jing:'春风把暖气吹进屠苏酒中，人人畅饮迎春。',
  segs:[{c:'春风送暖入屠苏。', p:py('chūn fēng sòng nuǎn rù tú sū')}],
  read:'春风送暖入屠苏。',
  yisi:'和暖的春风吹来了新年，人们畅饮着屠苏酒。',
  zhu:[['屠苏','屠苏酒，饮屠苏酒是古代过年时的习俗']] },
{ name:'新桃换符', jing:'初升的太阳照耀千家万户，大家都用新桃符换下旧桃符。',
  segs:[{c:'千门万户曈曈日，总把新桃换旧符。', p:py('qiān mén wàn hù tóng tóng rì zǒng bǎ xīn táo huàn jiù fú')}],
  read:'千门万户曈曈日，总把新桃换旧符。',
  yisi:'初升的太阳照耀着千家万户，人们都取下旧桃符，换上新桃符。',
  zhu:[['曈曈','日出时光亮的样子'],['桃','桃符，画着门神的桃木板，春节时挂在门旁'],['新桃换旧符','换上新桃符，取下旧桃符']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「爆竹声中一岁除」的下一句是？', o:['春风送暖入屠苏','千门万户曈曈日','总把新桃换旧符'], a:0},
 {q:'「总把新桃换旧符」中的「桃符」是？', o:['画有门神的桃木板，春联的前身','一种水果','桃木做的家具'], a:0},
 {q:'《元日》描写的是哪个节日的景象？', o:['中秋节','春节（农历正月初一）','清明节'], a:1},
 {q:'《元日》的作者是？', o:['苏轼','王安石','陆游'], a:1},
 {q:'「曈曈日」写出了太阳怎样的样子？', o:['日出时光亮耀眼','夕阳西下','朦胧昏暗'], a:0},
];`);

const BUILDERS = `function makeBaozhuString(){
  const g=new THREE.Group();
  const sm=new THREE.MeshPhongMaterial({color:0xc23a2a});
  for(let i=0;i<10;i++){
    const c=new THREE.Mesh(new THREE.CylinderGeometry(0.16,0.16,0.7,8),sm);
    c.position.set(0,4.5-i*0.75,0); c.rotation.z=Math.sin(i*1.7)*0.5;
    c.translateX(0.34); g.add(c);
  }
  const fuse=new THREE.Mesh(new THREE.CylinderGeometry(0.04,0.04,1.2,5),new THREE.MeshBasicMaterial({color:0xd8c08a}));
  fuse.position.y=5.2; g.add(fuse);
  return g;
}
function bCoverXinnian(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x1a130a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const bstr=makeBaozhuString(); bstr.position.set(-8,0,-14); bstr.rotation.z=0.5; g.add(bstr);
  const motes=makeGlow({n:70,box:[130,26,90],pos:[0,10,-30],color:0xd4b050,size:7,speed:0.04,rise:0,maxA:0.45});
  g.add(motes.points);
  addLights(g,{c:0xd4b050,i:0.55,p:[30,60,30]},{c:0x2a2012,i:0.85});
  return {group:g,update(t){motes.update(t);}};
}
function bBaozhu(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x1a130a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const bstr=makeBaozhuString(); bstr.position.set(-7,0,-12); bstr.rotation.z=0.4; g.add(bstr);
  const burst=makeBurst({n:120,color:0xff8a5a,pos:[-7,5,-12]}); g.add(burst.points);
  const flash=new THREE.PointLight(0xff8a5a,0,60); flash.position.set(-7,5,-11); g.add(flash);
  const glow=makeGlow({n:80,box:[26,10,20],pos:[-7,4,-12],color:0xffa060,size:9,speed:0.5,rise:1,maxA:0});
  g.add(glow.points);
  const ctl={t:99};
  addLights(g,{c:0xd4b050,i:0.5,p:[30,60,30]},{c:0x2a2012,i:0.85});
  return {group:g,update(t,dt){
    burst.update(t); glow.update(t); ctl.t+=dt;
    flash.intensity=Math.max(0,flash.intensity-dt*3);
  },click(){
    if(ctl.t<2)return;
    ctl.t=0; burst.fire(); flash.intensity=2.4;
    glow.mat.uniforms.uMaxA.value=0.9; setTimeout(()=>{glow.mat.uniforms.uMaxA.value=0;},900);
    drum();
    const fl=$('#flash'); fl.textContent='爆竹声中一岁除'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
function drum(){
  if(!groupAudio.ctx)return;
  const ctx=groupAudio.ctx, now=ctx.currentTime;
  [0,0.28].forEach(off=>{
    const o=ctx.createOscillator(), gn=ctx.createGain();
    o.type='sine'; o.frequency.setValueAtTime(150,now+off); o.frequency.exponentialRampToValueAtTime(55,now+off+0.22);
    gn.gain.setValueAtTime(0.3,now+off); gn.gain.exponentialRampToValueAtTime(0.001,now+off+0.3);
    o.connect(gn).connect(groupAudio.master); o.start(now+off); o.stop(now+off+0.32);
  });
}
function bTusu(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(70,40),new THREE.MeshPhongMaterial({color:0x1a130a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const table=new THREE.Mesh(new THREE.BoxGeometry(9,2.4,4.6),new THREE.MeshPhongMaterial({color:0x2a1c10}));
  table.position.y=1.2; g.add(table);
  const cups=[];
  for(let i=0;i<3;i++){
    const c=new THREE.Mesh(new THREE.CylinderGeometry(0.42,0.3,0.6,12),new THREE.MeshPhongMaterial({color:0xd8e0d8,shininess:70}));
    c.position.set(-2+i*2,2.7,-0.6); g.add(c); cups.push(c);
    const wine=new THREE.Mesh(new THREE.CylinderGeometry(0.36,0.28,0.14,12),
      new THREE.MeshBasicMaterial({color:0xc8e0a0}));
    wine.position.set(-2+i*2,2.85,-0.6); g.add(wine);
  }
  const breeze=makeFlow({n:140,box:[110,20,60],pos:[0,9,-20],color:0xd4b050,size:20,speed:6,maxA:0.22});
  g.add(breeze.points);
  addLights(g,{c:0xd4b050,i:0.55,p:[-20,50,40]},{c:0x2a2012,i:0.85});
  return {group:g,update(t,dt){breeze.update(t);
    cups.forEach((c,i)=>{c.position.y=2.7+Math.sin(t*1.2+i)*0.03;});
  }};
}
function bTaofu(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x1a130a}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const sun=new THREE.Mesh(new THREE.SphereGeometry(5,16,12),new THREE.MeshBasicMaterial({color:0xffd890}));
  sun.position.set(-34,16,-80); g.add(sun);
  const sglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd890,
    transparent:true,opacity:0.75,depthWrite:false,blending:THREE.AdditiveBlending}));
  sglow.scale.set(56,56,1); sglow.position.copy(sun.position); g.add(sglow);
  const doors=[];
  for(let i=0;i<4;i++){
    const hz=-14-(i%2)*14, hx=-24+i*16;
    const house=new THREE.Mesh(new THREE.BoxGeometry(12,7.5,7),new THREE.MeshPhongMaterial({color:0x241a10}));
    house.position.set(hx,3.75,hz); g.add(house);
    const roof=new THREE.Mesh(new THREE.ConeGeometry(9.6,3.4,4),new THREE.MeshPhongMaterial({color:0x181008}));
    roof.rotation.y=Math.PI/4; roof.position.set(hx,9.2,hz); g.add(roof);
    const dOld=new THREE.Mesh(new THREE.PlaneGeometry(1.1,2.4),new THREE.MeshBasicMaterial({color:0x6a5a4a}));
    dOld.position.set(hx-1.4,3.4,hz+3.55); g.add(dOld);
    const dNew=new THREE.Mesh(new THREE.PlaneGeometry(1.1,2.4),new THREE.MeshBasicMaterial({color:0xd4444a}));
    dNew.position.set(hx+1.4,3.4,hz+3.55); dNew.material.transparent=true; dNew.material.opacity=0.25; g.add(dNew);
    doors.push({dNew,dOld});
  }
  const ctl={t:0};
  addLights(g,{c:0xd4b050,i:0.6,p:[-20,50,40]},{c:0x2a2012,i:0.85});
  return {group:g,update(t,dt){
    ctl.t+=dt;
    const p=sstep(1,8,ctl.t%14);
    doors.forEach(d=>{
      d.dNew.material.opacity=0.25+0.75*p;
      d.dOld.material.opacity=0.9*(1-p);
    });
  },click(){
    if(ctl.t<6)return;
    ctl.t=0; drum(); bell();
    const fl=$('#flash'); fl.textContent='总把新桃换旧符'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCoverXinnian,
  cam:{f:[0,9,50],t:[0,9,46],lf:[0,8,-24],lt:[0,8,-24]},
  sky:()=>SK({star:0.4,ms:0.9,moon:new THREE.Vector3(50,85,-150),fd:0.0048}) },
{ name:'爆竹除岁',dwell:14,river:0.015,build:bBaozhu,
  cam:{f:[0,7,32],t:[0,6.5,29],lf:[-7,5,-12],lt:[-7,5,-12]},
  sky:()=>SK({star:0.35,ms:0.8,moon:new THREE.Vector3(45,80,-150),fd:0.005}) },
{ name:'春风屠苏',dwell:13,river:0.015,build:bTusu,
  cam:{f:[0,6.5,26],t:[0,6,24],lf:[0,3.4,-1],lt:[0,3.2,-1]},
  sky:()=>SK({star:0.3,ms:0.8,moon:new THREE.Vector3(50,80,-150),fd:0.0055}) },
{ name:'新桃换符',dwell:16,river:0.015,build:bTaofu,
  cam:{f:[0,8,44],t:[0,8,40],lf:[-10,6,-20],lt:[10,6,-26]},
  sky:()=>SK({star:0.2,ms:0.6,moon:new THREE.Vector3(-50,60,-150),fd:0.005}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 / 按空格 —— 爆竹声起'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','元日。宋，王安石。爆竹声中一岁除，春风送暖入屠苏。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重过新年','初识介甫，尚需共读','渐入佳境，再诵几遍','爆竹声里，春意顿生','深得介甫革新之志','介甫知己，新桃同换'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
