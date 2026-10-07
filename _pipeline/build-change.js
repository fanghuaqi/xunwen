#!/usr/bin/env node
/* build-change.js —— 《嫦娥》水墨夜思·烛影与碧海青天对切 */
'use strict';
const fs = require('fs');
const SRC = path.resolve(__dirname, '_dgx', 'reference-jiangjinjiu.html');
const OUT = path.resolve(__dirname, '..', 'chang-e/index.html');
let h = fs.readFileSync(SRC, 'utf8');
let fail = 0;
const rep = (o, n, exp) => {
  const c = h.split(o).length - 1;
  if (c !== exp) { console.error(`✗ 匹配 ${c}≠${exp}: ${o.slice(0, 60)}`); fail++; return; }
  h = h.split(o).join(n);
};
const A = a => `rgba(214,222,233,${a})`;

rep('<title>循文入境 · 将进酒 | Three.js 沉浸式诗词课堂</title>', '<title>循文入境 · 嫦娥 | Three.js 沉浸式诗词课堂</title>', 1);
rep('<h1>将进酒</h1>\n      <div class="dyn">唐 · 李白</div>', '<h1>嫦娥</h1>\n      <div class="dyn">唐 · 李商隐</div>', 1);
rep('<div id="brand">将进酒<small>循 文 入 境 · 李 白</small></div>', '<div id="brand">嫦娥<small>循 文 入 境 · 李商隐</small></div>', 1);
rep('<p>十三重意境，随诗句次第展开：看黄河之水天上来，奔流到海不复回，揽高堂明镜悲白发，与岑夫子、丹丘生举杯共饮，最终与尔同销万古愁。</p>\n      <p>边读诗，边走进李白笔下那个奔涌、狂放而又深藏愁绪的世界。</p>', '<p>三重意境，随诗句次第展开：云母屏风前烛影深深，窗外银河渐落、晓星将沉——遥想月宫里的嫦娥，碧海青天，夜夜孤心。</p>\n      <p>边读诗，边走进李商隐笔下那间烛影摇曳的小室与那片清冷的月宫天空。</p>', 1);
rep('<h2>酒尽 · 愁销</h2>', '<h2>烛影 · 青天</h2>', 1);
rep('<div class="sub">十 三 境 已 尽 · 全 诗 在 此</div>', '<div class="sub">三 境 已 尽 · 全 诗 在 此</div>', 1);
rep('← → 键或空格逐境游览 · 第七境可点击画面与君同酌', '← → 键或空格逐境游览 · 末境点击烛影摇曳晓星沉 · 建议开启声音', 1);
rep('/* 循文入境 · 将进酒 —— Three.js 沉浸式诗词课件', '/* 循文入境 · 嫦娥 —— Three.js 沉浸式诗词课件', 1);

rep('--gold:#d4af37', '--gold:#d6dce9', 1);
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

rep("scene.fog=new THREE.FogExp2(0x0a1526,0.0045)", "scene.fog=new THREE.FogExp2(0x131822,0.0046)", 1);
rep("bot:C(0x0c1016)", "bot:C(0x090d14)", 1);
rep("uBot:{value:C(0x0c1016)}", "uBot:{value:C(0x090d14)}", 1);
rep("fog:C(0x0a1526)", "fog:C(0x131822)", 1);
rep("top:C(0x081020),hor:C(0x1d3350)", "top:C(0x0e1420),hor:C(0x1c2436)", 1);

const mPoem = h.match(/const POEM = \[[\s\S]*?\n\];/);
if (!mPoem) { console.error('✗ POEM 锚点'); fail++; } else h = h.replace(mPoem[0], `const POEM = [
{ name:'云母烛影', jing:'云母屏风上映着幽深暗淡的烛影。',
  segs:[{c:'云母屏风烛影深，', p:py('yún mǔ píng fēng zhú yǐng shēn')}],
  read:'云母屏风烛影深，',
  yisi:'云母屏风上映出幽深暗淡的烛影，室内越来越昏暗。',
  zhu:[['云母屏风','以云母石制作的屏风','云母是一种矿物，晶莹闪光'],['烛影','烛光的暗影'],['深','暗淡，幽深']] },
{ name:'晓星渐沉', jing:'银河渐渐斜落，晨星一点点沉没——天快亮了。',
  segs:[{c:'长河渐落晓星沉。', p:py('cháng hé jiàn luò xiǎo xīng chén')}],
  read:'长河渐落晓星沉。',
  yisi:'银河渐渐向西南方向斜落，晨星也渐渐下沉，天快要亮了。',
  zhu:[['长河','指银河'],['渐落','渐渐西斜落下'],['晓星','黎明的星辰'],['沉','沉下去']] },
{ name:'碧海青天', jing:'嫦娥想必悔偷灵药，夜夜面对碧海青天，孤独清冷。',
  segs:[{c:'嫦娥应悔偷灵药，碧海青天夜夜心。', p:py('cháng é yīng huǐ tōu líng yào bì hǎi qīng tiān yè yè xīn')}],
  read:'嫦娥应悔偷灵药，碧海青天夜夜心。',
  yisi:'嫦娥想必悔恨当初偷吃了灵药，如今独处月宫，夜夜面对碧海般的青天，孤寂清冷。',
  zhu:[['嫦娥','神话中后羿之妻，偷吃灵药飞升月宫'],['应悔','恐怕会后悔'],['夜夜心','夜夜面对青天，心情孤寂']] },
];`);
rep("const CN = ['壹','贰','叁','肆','伍','陆','柒','捌','玖','拾','拾壹','拾贰','拾叁'];", "const CN = ['壹','贰','叁'];", 1);
const mQuiz = h.match(/const QUIZ = \[[\s\S]*?\n\];/);
if (!mQuiz) { console.error('✗ QUIZ 锚点'); fail++; } else h = h.replace(mQuiz[0], `const QUIZ = [
 {q:'「云母屏风烛影深」的下一句是？', o:['长河渐落晓星沉','碧海青天夜夜心','嫦娥应悔偷灵药'], a:0},
 {q:'《嫦娥》的作者是？', o:['李商隐','杜牧','李贺'], a:0},
 {q:'诗中推测嫦娥"悔恨"的事情是？', o:['偷吃了不死灵药','离开了月宫','没有带上玉兔'], a:0},
 {q:'「碧海青天夜夜心」写出嫦娥怎样的心境？', o:['夜夜独对青天的孤独寂寥','翱翔天际的自由快乐','对后羿的思念怨恨'], a:0},
 {q:'「长河渐落晓星沉」暗示了时间怎样的变化？', o:['夜晚将尽、天将破晓','正午时分','傍晚黄昏'], a:0},
];`);

const BUILDERS = `function makeCandleFlame(){
  const g=new THREE.Group();
  const stick=new THREE.Mesh(new THREE.CylinderGeometry(0.09,0.13,2.4,8),new THREE.MeshPhongMaterial({color:0xcabf9a}));
  stick.position.y=1.2; g.add(stick);
  const flame=new THREE.Mesh(new THREE.SphereGeometry(0.34,10,8),new THREE.MeshBasicMaterial({color:0xffd27a}));
  flame.scale.y=1.7; flame.position.y=2.9; g.add(flame);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb85a,
    transparent:true,opacity:0.7,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(9,12,1); glow.position.y=3.0; g.add(glow);
  const light=new THREE.PointLight(0xffb85a,1.1,34); light.position.y=3.0; g.add(light);
  return {g,flame,glow,light};
}
function bCoverZhu(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(70,40),new THREE.MeshPhongMaterial({color:0x0d1119}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const candle=makeCandleFlame(); candle.g.position.set(-5,0,2); g.add(candle.g);
  const motes=makeGlow({n:50,box:[90,20,60],pos:[0,8,-20],color:0xd6dee9,size:6,speed:0.03,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0x8ea0ba,i:0.35,p:[20,50,30]},{c:0x1a2230,i:0.85});
  return {group:g,update(t,dt){motes.update(t);
    candle.flame.scale.y=1.7+Math.sin(t*9)*0.25;
    candle.light.intensity=1.1+Math.sin(t*7.3)*0.18;
  }};
}
function bZhuying(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(60,40),new THREE.MeshPhongMaterial({color:0x0c0f18}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const screen=new THREE.Group(); g.add(screen);
  const sm=new THREE.MeshPhongMaterial({color:0x22283a,shininess:60});
  for(let i=0;i<4;i++){
    const p=new THREE.Mesh(new THREE.PlaneGeometry(5.6,10),sm);
    p.position.set(-8.4+i*5.6,5,-8); p.rotation.y=0.1*i-0.15; screen.add(p);
  }
  const candle=makeCandleFlame(); candle.g.position.set(-3,0,-1); g.add(candle.g);
  const shadow=new THREE.Mesh(new THREE.PlaneGeometry(3,9),new THREE.MeshBasicMaterial({color:0x05070c,transparent:true,opacity:0.75}));
  shadow.position.set(-1.4,4.6,-7.9); screen.add(shadow);
  const mist=makeMist({n:6,spread:[70,14,50],pos:[0,5,-12],scale:45,color:0x8ea0ba,op:0.08});
  g.add(mist.g);
  addLights(g,{c:0x6a7a96,i:0.25,p:[20,40,30]},{c:0x141a26,i:0.85});
  return {group:g,update(t,dt){mist.update(t);
    candle.flame.scale.y=1.7+Math.sin(t*8.5)*0.3;
    candle.light.intensity=1.1+Math.sin(t*6.7)*0.22;
    shadow.material.opacity=0.68+Math.sin(t*6.7+1)*0.1;
  }};
}
function bXiaoxing(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(70,40),new THREE.MeshPhongMaterial({color:0x0e1420}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const river=new THREE.Mesh(new THREE.PlaneGeometry(180,50),new THREE.MeshPhongMaterial({color:0x16202e,shininess:80}));
  river.rotation.x=-Math.PI/2; river.position.set(0,0.02,-46); river.rotation.z=0.16; g.add(river);
  const star=new THREE.Mesh(new THREE.SphereGeometry(1.4,12,10),new THREE.MeshBasicMaterial({color:0xe8f0ff}));
  star.position.set(28,42,-140); g.add(star);
  const sglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8e4f8,
    transparent:true,opacity:0.7,depthWrite:false,blending:THREE.AdditiveBlending}));
  sglow.scale.set(14,14,1); sglow.position.copy(star.position); g.add(sglow);
  const band=new THREE.Points((function(){
    const bg=new THREE.BufferGeometry(); const P=new Float32Array(900*3);
    for(let i=0;i<900;i++){
      const t0=rnd(-1,1), s=rnd(-0.16,0.16);
      P[i*3]=t0*260; P[i*3+1]=34+t0*26+Math.abs(s)*40; P[i*3+2]=-150+Math.abs(t0)*30;
    }
    bg.setAttribute('position',new THREE.BufferAttribute(P,3)); return bg;
  })(),new THREE.PointsMaterial({color:0x9fb4d4,size:1.6,sizeAttenuation:false,map:circleTex(),
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending,fog:false}));
  g.add(band);
  addLights(g,{c:0x8ea0ba,i:0.4,p:[30,50,40]},{c:0x1a2230,i:0.85});
  return {group:g,update(t,dt){
    star.position.y=42-sstep(2,14,t)*14; sglow.position.y=star.position.y;
    sglow.material.opacity=0.7*(1-sstep(6,16,t)*0.75);
    star.material.color.setHex(0xe8f0ff);
    band.position.y=-sstep(2,14,t)*10;
  }};
}
function bBitian(){
  const g=new THREE.Group();
  const ground=new THREE.Mesh(new THREE.CircleGeometry(80,40),new THREE.MeshPhongMaterial({color:0x0c1420}));
  ground.rotation.x=-Math.PI/2; g.add(ground);
  const moon=new THREE.Mesh(new THREE.SphereGeometry(20,32,24),
    new THREE.MeshBasicMaterial({color:0xeef4fb,fog:false}));
  moon.position.set(0,86,-170); g.add(moon);
  const mglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f5,
    transparent:true,opacity:0.65,depthWrite:false,blending:THREE.AdditiveBlending,fog:false}));
  mglow.scale.set(130,130,1); mglow.position.copy(moon.position); g.add(mglow);
  const palace=new THREE.Group(); g.add(palace);
  const pm=new THREE.MeshPhongMaterial({color:0xbcd0e4,emissive:0x2a3c52,transparent:true,opacity:0.92});
  const hall=new THREE.Mesh(new THREE.BoxGeometry(10,5,7),pm); hall.position.set(0,24,-168); palace.add(hall);
  const roof=new THREE.Mesh(new THREE.ConeGeometry(8.4,3.4,4),pm);
  roof.rotation.y=Math.PI/4; roof.position.set(0,28.2,-168); palace.add(roof);
  const ce=makeFigure(1.05);
  ce.traverse(o=>{if(o.material)o.material=new THREE.MeshPhongMaterial({color:0xe8f0f8,emissive:0x30405a});});
  ce.position.set(7.5,23.4,-166); ce.rotation.y=2.4; palace.add(ce);
  const mist=makeMist({n:8,spread:[140,20,90],pos:[0,10,-40],scale:60,color:0x8fb0cc,op:0.1});
  g.add(mist.g);
  addLights(g,{c:0xaebfd6,i:0.5,p:[0,90,30]},{c:0x202c3e,i:0.85});
  return {group:g,update(t,dt){mist.update(t);
    ce.rotation.y=2.4+Math.sin(t*0.4)*0.2;
    ce.position.y=23.4+Math.sin(t*0.7)*0.25;
  },click(){
    const fl=$('#flash'); fl.textContent='碧海青天夜夜心'; fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
  }};
}
`;
const mBuild = h.match(/function bCover\(\)\{[\s\S]*?\/\* ---------------- 境定义/);
if (!mBuild) { console.error('✗ builders 锚点'); fail++; } else h = h.replace(mBuild[0], BUILDERS + '/* ---------------- 境定义');

const STAGES = `const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCoverZhu,
  cam:{f:[0,9,44],t:[0,9,40],lf:[0,7,-20],lt:[0,7,-20]},
  sky:()=>SK({star:0.3,ms:0.9,moon:new THREE.Vector3(40,80,-150),fd:0.005}) },
{ name:'云母烛影',dwell:14,river:0.015,build:bZhuying,
  cam:{f:[0,7,26],t:[0,6.5,23],lf:[-3,5,-8],lt:[-3,5,-8]},
  sky:()=>SK({star:0.05,ms:0.001,moon:new THREE.Vector3(0,-400,0),fd:0.012,ambC:C(0x1a2230),ambI:0.9}) },
{ name:'晓星渐沉',dwell:14,river:0.015,build:bXiaoxing,
  cam:{f:[0,8,40],t:[0,8,36],lf:[20,34,-140],lt:[24,30,-140]},
  sky:()=>SK({star:0.5,ms:0.7,moon:new THREE.Vector3(-70,50,-150),fd:0.006}) },
{ name:'碧海青天',dwell:16,river:0.015,build:bBitian,
  cam:{f:[0,16,50],t:[0,18,46],lf:[0,50,-170],lt:[0,54,-170]},
  sky:()=>SK({star:0.28,ms:0.001,moon:new THREE.Vector3(0,-400,0),fd:0.0036}) },
];`;
const mStages = h.match(/const STAGES=\[[\s\S]*?\n\];/);
if (!mStages) { console.error('✗ STAGES 锚点'); fail++; } else h = h.replace(mStages[0], STAGES);

rep('i=clamp(i,0,13);', 'i=clamp(i,0,3);', 1);
rep('for(let i=1;i<=13;i++){', 'for(let i=1;i<=3;i++){', 1);
rep('curIdx>=13)showEnding()', 'curIdx>=3)showEnding()', 3);
rep('if(curIdx===13)showEnding(); else goto(curIdx+1);', 'if(curIdx===3)showEnding(); else goto(curIdx+1);', 1);
rep("curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj&&curStageObj.click", 1);
rep("curIdx===7&&state==='stage'&&curStageObj.click", "curIdx===3&&state==='stage'&&curStageObj.click", 1);
rep("if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 与君同酌'),2600);", "if(i===3)setTimeout(()=>tip('轻点画面 —— 烛影摇曳晓星沉'),2600);", 1);
rep("aiSpeak('14.mp3'", "aiSpeak('04.mp3'", 2);
rep("else aiSpeak('00.mp3','将进酒。唐，李白。君不见，黄河之水天上来，奔流到海不复回。');", "else aiSpeak('00.mp3','嫦娥。唐，李商隐。云母屏风烛影深，长河渐落晓星沉。');", 1);
rep("const words=['再游一次，与君同酌','初识太白，尚需共读','渐入佳境，再诵几遍','豪气渐生，再进一杯','深得太白豪情','诗仙知己，万古愁销'];", "const words=['再游一次，重上高楼','初识义山，尚需共读','渐入佳境，再诵几遍','烛影青天，孤心可鉴','深得义山深情','义山知己，月夜同心'];", 1);

if (fail) { console.error(`\n${fail} 处拼装失败，未写出`); process.exit(1); }
fs.mkdirSync(require('path').dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, h);
console.log('written', OUT, h.length, 'bytes');
