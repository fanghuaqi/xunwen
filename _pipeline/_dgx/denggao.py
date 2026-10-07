# -*- coding: utf-8 -*-
"""denggao.py —— 《登高》（唐·杜甫，no.206，水墨夜思·七律之冠）生成配置
四境（七律四联各一境）：
  壹 风急猿哀（首联·登高所见之景，动：急风/哀猿/飞鸟/清渚沙白）
  贰 落木长江（颔联·七律之冠联·标志性瞬间：落木如雨 + 长江层浪的对仗动景）
  叁 万里悲秋（颈联·八重悲，静：常作客/百年多病/独登台）
  肆 霜鬓停杯（尾联·末境点击落木长江：落叶如雨 + 江浪层叠 + 镜头拔高）"""

META = dict(
    N=4, slug='denggao', title='登高', dyn='唐 · 杜甫', brand_author='杜 甫',
    gold_rgb='152,168,184',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#98a8b8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(152,168,184,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(7,10,16', 1),
        ('rgba(4,6,11', 'rgba(6,8,14', 2),
        ('rgba(6,9,16', 'rgba(7,9,15', 1),
        ('rgba(3,5,9', 'rgba(5,7,12', 1),
        ('#0b101c', '#101624', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
    ],
    tip='轻点画面 / 按空格 —— 落叶如雨、江浪层叠，镜头拔高',
    hint='← → 键或空格逐境游览 · 末境可点击落木长江，看落叶如雨、江浪层叠、镜头拔高',
    cover_read='登高。唐，杜甫。风急天高猿啸哀，渚清沙白鸟飞回。无边落木萧萧下，不尽长江滚滚来。',
    cover_p1='四重意境，随诗句次第展开：急风高天里哀猿长啸，清渚白沙上众鸟回旋；无边落木萧萧而下，不尽长江滚滚而来；万里悲秋、百年多病，旅人独登高台；末了艰难苦恨、两鬓成霜，浊酒新停，连愁都无处可浇。',
    cover_p2='边读诗，边走进杜甫「七律之冠」沉郁顿挫的秋江高台。',
    end_h2='杯停 · 悲深', cn_word='四',
    words_js="['再登一次高台','初识少陵，尚需共读','渐入佳境，再诵几遍','诗境渐深，秋声入怀','已解八重悲慨','沉郁顿挫，诗史悲怀']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'风急猿哀', jing:'急风、高天、哀猿、清渚、白沙、回鸟 —— 十四字六景，皆登高所见。（风 · 猿 · 鸟）',
  segs:[
   {c:'风急天高猿啸哀，', p:py('fēng jí tiān gāo yuán xiào āi')},
   {c:'渚清沙白鸟飞回。', p:py('zhǔ qīng shā bái niǎo fēi huí')}],
  read:'风急天高猿啸哀，渚清沙白鸟飞回。',
  yisi:'秋风迅急，天宇高远，猿声凄哀；水中小洲清冷，白沙耀眼，鸟儿在急风中低回盘旋。——首联一句三景、两句六景，俯仰之间皆是登高所见。',
  zhu:[['风急天高','夔州峡口多风，秋高而风势逼人——起笔便是高台之上的体感，也暗写此台之高'],['猿啸哀','三峡多猿，鸣声凄厉。啸（xiào），拉长声音叫；哀，凄切悲哀——为全诗定下悲凉基调'],['渚','水中的小块陆地、小洲。渚（zhǔ）；清，既指水清，也见冷清'],['鸟飞回','江鸟在急风中盘旋低徊。回，回旋——风急，故鸟飞而难进']] },
{ name:'落木长江', jing:'无边落木萧萧而下，不尽长江滚滚而来 —— 一气磅礴，七律之冠联。（落木 · 长江）',
  segs:[
   {c:'无边落木萧萧下，', p:py('wú biān luò mù xiāo xiāo xià')},
   {c:'不尽长江滚滚来。', p:py('bù jìn cháng jiāng gǔn gǔn lái')}],
  read:'无边落木萧萧下，不尽长江滚滚来。',
  yisi:'望不到边际的落叶，萧萧地飘坠而下；奔流不尽的长江，滚滚地汹涌而来。——仰看无边落木，俯望不尽长江：空间之无垠，对时间之无穷，被誉为「古今七言律第一」中的绝唱。',
  zhu:[['落木','深秋飘落的树木，即落叶。用「木」不用「叶」，更见疏朗萧瑟'],['萧萧','风吹落叶飘坠之声，拟声词——未见落木，先闻秋声'],['不尽','无穷无尽'],['滚滚','波涛连绵不绝之貌。此联对仗精工、气象雄浑，明胡应麟《诗薮》推全诗为「古今七言律第一」']] },
{ name:'万里悲秋', jing:'万里悲秋，常作客；百年多病，独登台 —— 八重悲意，层层递进。（客 · 病 · 台）',
  segs:[
   {c:'万里悲秋常作客，', p:py('wàn lǐ bēi qiū cháng zuò kè')},
   {c:'百年多病独登台。', p:py('bǎi nián duō bìng dú dēng tái')}],
  read:'万里悲秋常作客，百年多病独登台。',
  yisi:'悲对秋色，感慨万里漂泊、长年客居他乡；一生多病，今日又独自登上高台。——由写景转入抒情，前人评此联「十四字之间含八意」，即八重悲。',
  zhu:[['八重悲','宋罗大经《鹤林玉露》析此联十四字含八意：万里，地之远也；秋，时之凄惨也；作客，羁旅也；常作客，久旅也；百年，暮齿也；多病，衰疾也；台，高迥处也；独登台，无亲朋也——十四字八重悲，层层加码'],['作客','客居他乡。杜甫自战乱以来辗转秦州、成都、夔州等地，漂泊日久'],['百年','一生，此处指暮年——作诗时杜甫五十六岁，肺病缠身'],['独登台','独自登上高台。此诗作于唐代宗大历二年（767）秋，杜甫流寓夔州（今重庆奉节），重阳独登——登高本应亲朋结伴，一个「独」字写尽孤绝']] },
{ name:'霜鬓停杯', jing:'艰难苦恨繁霜鬓，潦倒新停浊酒杯。（点击落木长江 —— 落叶如雨、江浪层叠、镜头拔高）',
  segs:[
   {c:'艰难苦恨繁霜鬓，', p:py('jiān nán kǔ hèn fán shuāng bìn')},
   {c:'潦倒新停浊酒杯。', p:py('liáo dǎo xīn tíng zhuó jiǔ bēi')}],
  read:'艰难苦恨繁霜鬓，潦倒新停浊酒杯。',
  yisi:'一生艰难、时世艰辛，两鬓的白发日渐繁多；穷愁潦倒，偏又新近因病戒了酒——愁到极处，连借酒浇愁也不能够了。',
  zhu:[['艰难苦恨','「艰难」兼指国运与身世：时逢乱世，又一生坎坷；「苦恨」即极恨——苦，极甚；恨，遗憾。一语双关，沉痛至深'],['繁霜鬓','白发日渐增多。繁，多；霜鬓，白如秋霜的鬓发'],['潦倒','衰颓困顿。潦（liáo）倒'],['新停','最近刚刚停止。杜甫晚年因肺疾戒酒——忧愁无处排遣，悲慨更进一层']] },
];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「风急天高猿啸哀」的下一句是？', o:['渚清沙白鸟飞回','无边落木萧萧下','不尽长江滚滚来'], a:0},
 {q:'「无边落木萧萧下」的下一句是？', o:['万里悲秋常作客','不尽长江滚滚来','百年多病独登台'], a:1},
 {q:'「渚清沙白鸟飞回」的「渚」与「潦倒新停浊酒杯」的「潦」，注音全都正确的是？', o:['渚 zhě、潦 liáo','渚 zhǔ、潦 liǎo','渚 zhǔ、潦 liáo'], a:2},
 {q:'这首被推为「古今七言律第一」的诗，写于杜甫晚年流寓夔州（今重庆奉节）时，在哪一个节日独自登高所作？', o:['重阳节','中秋节','寒食节'], a:0},
 {q:'宋人罗大经评颈联十四字含「八重悲」：万里（地远）、悲秋（时惨）、作客（羁旅）、常作客（久旅）、百年（暮年）、多病（衰疾）、登台（高迥）、独（无亲朋）。这八重悲共同托出的是？', o:['秋景壮美、豪情满怀','暮年漂泊、老病孤愁的沉郁悲慨','思乡怀人、急切盼归'], a:1},
];
"""

SCENES_JS = """/* ================= 登高 · 四境场景（水墨夜思：风急猿哀、落木长江、万里悲秋、霜鬓停杯） ================= */

/* 白发老人（独登台者）：全诗贯穿的同一人造型（每次 build 新建材质） */
function denggaoFigure(scale){
  return makeFigure({pose:'独立',robe:0x1c2430,belt:0x4a5666,skin:0xcbb9a2,collar:0xb9c4d4,
    hair:0xd8dee8,hat:'发髻',rimC:0x98a8b8,rim:0.5,noProp:true,scale:scale});
}

/* 高台：石台 + 两级台基 + 台缘（合批 1 mesh，水墨剪影） */
function makeTerrace(o){
  o=o||{};
  const B=new GeoBag(), c1=0x0a0e15, c2=0x101622, c3=0x161d2b;
  const w=o.w===undefined?15:o.w, d=o.d===undefined?9:o.d, h=o.h===undefined?2.6:o.h;
  const base=new THREE.BoxGeometry(w+6.5,1.1,d+5); base.translate(0,0.55,0); B.put(base,c1);
  const mid=new THREE.BoxGeometry(w+3,1.0,d+2.4); mid.translate(0,1.1+0.5,0); B.put(mid,c2);
  const top=new THREE.BoxGeometry(w,0.45,d); top.translate(0,h-0.22,0); B.put(top,c3);
  const edge=new THREE.BoxGeometry(w+0.3,0.12,d+0.3); edge.translate(0,h+0.02,0); B.put(edge,0x1e2735);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x39465c,emissive:0x05070c}),{c:0x98a8b8,i:0.3,p:2.5})));
  return g;
}

/* 哀猿：崖头弓身剪影（合批 1 mesh） */
function makeApe(o){
  o=o||{};
  const B=new GeoBag(), c=0x080b12;
  const body=new THREE.SphereGeometry(0.34,8,6); body.scale(1.3,0.95,0.9); body.rotateZ(0.45);
  body.translate(0,0.40,0); B.put(body,c);
  const head=new THREE.SphereGeometry(0.145,7,5); head.translate(0.34,0.68,0); B.put(head,c);
  const jaw=new THREE.ConeGeometry(0.05,0.16,5); jaw.rotateZ(1.35); jaw.translate(0.46,0.63,0); B.put(jaw,0x0a0d15);
  const arm=new THREE.CylinderGeometry(0.045,0.05,0.78,5); arm.rotateZ(1.2); arm.translate(0.36,0.30,0); B.put(arm,c);
  const leg=new THREE.CylinderGeometry(0.05,0.055,0.42,5); leg.rotateZ(-0.35); leg.translate(-0.16,0.16,0); B.put(leg,c);
  const tail=new THREE.CylinderGeometry(0.03,0.014,0.72,4); tail.rotateZ(-2.35); tail.translate(-0.5,0.42,0); B.put(tail,c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.2,p:2.4})));
  if(o.scale)g.scale.setScalar(o.scale);
  return g;
}

/* 栖猿崖柱：石柱自江面拔起，顶端栖一只哀猿（石柱+猿分两 mesh） */
function makeApeCliff(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?71:o.seed), h=o.h===undefined?13:o.h;
  const col=rockGeo(3.0,1,R); col.scale(1,h/5.2,1); col.translate(0,h*0.45,0); B.put(col,0x080b11);
  const cap=rockGeo(2.3,1,R); cap.scale(1.5,0.42,1.25); cap.translate(0,h*0.88,0); B.put(cap,0x0b0f16);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.17,p:2.4})));
  const ape=makeApe({scale:o.ape===undefined?1.5:o.ape});
  ape.position.set(0.4,h*0.88+1.15,0); ape.rotation.y=o.face===undefined?0.8:o.face;
  g.add(ape);
  return g;
}

/* 清渚沙白：浅色石盘一片（合批 1 mesh，靠月光与银边读出「沙白」） */
function makeSandbar(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?206:o.seed);
  const n=o.n===undefined?4:o.n, w=o.w===undefined?16:o.w;
  for(let i=0;i<n;i++){
    const rg=rockGeo(2.2+R()*2.6,1,R);
    rg.scale(1+R()*0.6,0.10+R()*0.05,0.8+R()*0.5);
    rg.translate((R()-0.5)*w,-0.15,(R()-0.5)*7);
    B.put(rg,R()<0.5?0x4a5568:0x525e72);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x5a6a84,emissive:0x0a0e16}),{c:0x98a8b8,i:0.42,p:2.2})));
  return g;
}

/* 回鸟：盘旋江鸟（每只 2 面片，一片拍翅） */
function makeGulls(o){
  o=o||{};
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0x223048:o.color,side:THREE.DoubleSide});
  const g=new THREE.Group(), items=[];
  const n=o.n===undefined?5:o.n;
  for(let i=0;i<n;i++){
    const b=new THREE.Group();
    const w1=new THREE.Mesh(new THREE.PlaneGeometry(2.6,0.7),mat); w1.position.x=-1.2;
    const w2=new THREE.Mesh(new THREE.PlaneGeometry(2.6,0.7),mat); w2.position.x=1.2;
    b.add(w1,w2); g.add(b);
    items.push({b,w1,w2,cx:o.cx===undefined?4:o.cx,cz:o.cz===undefined?-26:o.cz,
      r:(o.r===undefined?7:o.r)*(0.6+Math.random()*0.7),
      y:(o.y===undefined?8:o.y)+Math.random()*4,
      sp:(o.sp===undefined?0.15:o.sp)*(0.75+Math.random()*0.5),
      ph:Math.random()*6.283,sc:(o.scMin===undefined?0.65:o.scMin)+Math.random()*(o.scVar===undefined?0.6:o.scVar)});
  }
  const api={g,items,update(t){
    for(const it of items){
      const a=it.ph+t*it.sp;
      it.b.position.set(it.cx+Math.sin(a)*it.r,it.y+Math.sin(t*0.8+it.ph)*1.2,it.cz+Math.cos(a)*it.r*0.7);
      it.b.rotation.y=-a+Math.PI/2;
      it.b.scale.setScalar(it.sc);
      const f=Math.sin(t*7+it.ph)*0.5; it.w1.rotation.z=f; it.w2.rotation.z=-f;
    }
  }};
  return api;
}

/* 落木如雨：InstancedMesh 菱叶小面片，逐帧下落/翻转（1 draw call） */
function makeLeaves(o){
  o=o||{};
  const n=o.n===undefined?300:o.n;
  const geo=new THREE.PlaneGeometry(0.9,0.6); geo.rotateX(-0.5);
  const baseOp=o.op===undefined?0.85:o.op;
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0xbfcadb:o.color,
    side:THREE.DoubleSide,transparent:true,opacity:baseOp});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  mesh.frustumCulled=false; mesh.renderOrder=3;
  const R=seedRnd(o.seed===undefined?206:o.seed);
  const box=o.box||[120,44,70], pos=o.pos||[-24,24,-38];
  const data=[];
  for(let i=0;i<n;i++){
    data.push({x:pos[0]+(R()-0.5)*box[0], y:pos[1]+R()*box[1], z:pos[2]+(R()-0.5)*box[2],
      v:2.2+R()*2.6, ph:R()*6.283, sw:0.6+R()*1.4,
      rx:R()*6.283, rz:R()*6.283, wx:0.5+R()*1.5, wz:0.5+R()*1.5, sc:0.6+R()*0.9});
  }
  const dm=new THREE.Object3D();
  let boost=0;
  const api={mesh,mat,setBoost(v){ boost=v; },update(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<n;i++){
      const d=data[i];
      const cyc=d.y+4;
      const yy=d.y-((t*d.v+d.ph*13.7)%cyc);
      dm.position.set(d.x+Math.sin(t*0.7+d.ph)*d.sw, yy, d.z+Math.cos(t*0.5+d.ph)*d.sw*0.5);
      dm.rotation.set(d.rx+t*d.wx, d.ph+t*0.3, d.rz+t*d.wz);
      dm.scale.setScalar(d.sc);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mat.opacity=kk*baseOp*(0.32+0.68*boost);
  }};
  return api;
}

/* 石案：高台上的小石桌（合批 1 mesh） */
function makeStoneTable(){
  const B=new GeoBag();
  const top=new THREE.CylinderGeometry(1.15,1.25,0.22,14); top.translate(0,1.08,0); B.put(top,0x1a2230);
  const leg=new THREE.CylinderGeometry(0.30,0.42,1.0,10); leg.translate(0,0.5,0); B.put(leg,0x141a26);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x39465c,emissive:0x05070c}),{c:0x98a8b8,i:0.32,p:2.4})));
  return g;
}

function bCover(){ // 封面 · 夔州秋夜
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:28,layers:2,peaks:4,seed:2060,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:2061,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:9,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,40,130],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.36});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bFengYuan(){ // 一 · 风急猿哀 —— 急风高天哀猿，清渚沙白鸟飞回（所见之景，动）
  const g=new THREE.Group();
  const water=makeWater({size:520,seg:84,amp:0.55,freq:0.11,speed:0.85,flow:[0.2,1.4],spec:2.0,
    deep:0x081220,shallow:0x132b42,skyc:0x20394f,moonDir:[38,116,-185]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:24,layers:2,peaks:5,seed:2062,color:0x070a10,atmo:0x1f2a3d,fogK:0.62,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 栖猿崖柱两根（哀猿长啸处） */
  const cliffA=makeApeCliff({h:11,ape:1.9,seed:207,face:0.9}); cliffA.position.set(-26,-1,-30); g.add(cliffA);
  const cliffB=makeApeCliff({h:14,ape:1.4,seed:209,face:-0.6}); cliffB.position.set(-40,-1,-46); g.add(cliffB);
  /* 清渚沙白 + 渚上渔人 + 回鸟盘旋 */
  const bar=makeSandbar({n:4,w:18,seed:2064}); bar.position.set(7,-0.4,-26); g.add(bar);
  const crowd=makeCrowd({n:3,rect:[3,-28,8,3],seed:2065,color:0x11161f,rimC:0x8fa4c4,
    rim:0.16,sMin:0.35,sMax:0.45,y:-0.3});
  g.add(crowd.mesh);
  const gulls=makeGulls({n:5,cx:7,cz:-26,y:11,r:9}); g.add(gulls.g);
  /* 高台 + 白发老人（独登台者，全诗一线贯穿） */
  const terrace=makeTerrace({w:14,d:8,h:2.4}); terrace.position.set(-11,-0.5,2); g.add(terrace);
  const poet=denggaoFigure(1.6); poet.position.set(-11,1.9,-0.5); poet.rotation.y=0.35; g.add(poet);
  /* 急风：横流风雾（「风急」的主视觉） */
  const wind=makeFlow({n:150,box:[130,14,70],pos:[0,10,-30],color:0x8fa0b8,size:15,speed:6.0,maxA:0.15});
  g.add(wind.points);
  const motes=makeGlow({n:50,box:[150,22,80],pos:[0,8,-34],color:0xa8bcd8,size:6,speed:0.06,rise:0,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[210,22,110],pos:[0,9,-52],scale:74,color:0x7e8ea8,op:0.055});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:2066,rim:0.14});
  rk.g.position.set(-16,-1.4,13); g.add(rk.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:2067,sway:1.6,rim:0.18});
  tree.g.position.set(15,-0.5,12); g.add(tree.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[-30,90,-40]},{c:0x1a2232,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t);
    gulls.update(t); wind.update(t); motes.update(t); mist.update(t,k);
    crowd.update(t); rk.update(t,k); tree.update(t,k); poet.update(t,k);
  }};
}

function bLuomu(){ // 二（标志性瞬间）· 落木长江 —— 冠联对仗动景：左天落木如雨，前江层浪滚滚
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:92,amp:1.15,freq:0.075,speed:1.05,flow:[0.1,2.2],spec:2.2,
    deep:0x071120,shallow:0x11293e,skyc:0x1c3348,moonDir:[10,110,-195]});
  water.mesh.position.y=-1.2; g.add(water.mesh);
  const ridge=makeRange({r:270,h:22,layers:2,peaks:4,seed:2068,color:0x070a10,atmo:0x223044,fogK:0.60,glowK:0.05,y:-18});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 峡口两岸（夔州峡口，江从两山间来） */
  const bankL=makeRange({r:150,h:40,layers:2,peaks:3,seed:2069,arc:Math.PI*0.40,a0:-Math.PI*0.92,
    color:0x070a10,atmo:0x27334a,fogK:0.64,glowK:0.08,y:-20});
  bankL.g.position.set(-16,0,-10); g.add(bankL.g);
  const bankR=makeRange({r:170,h:34,layers:2,peaks:3,seed:2070,arc:Math.PI*0.36,a0:Math.PI*0.55,
    color:0x070a10,atmo:0x27334a,fogK:0.64,glowK:0.08,y:-20});
  bankR.g.position.set(14,0,-14); g.add(bankR.g);
  /* 落木如雨（标志性瞬间·左天）：两片落叶雨 */
  const leaves=makeLeaves({n:300,box:[120,44,70],pos:[-24,24,-38],color:0xbfcadb,seed:2071,op:0.85});
  g.add(leaves.mesh);
  const leaves2=makeGlow({n:260,box:[90,36,60],pos:[-34,20,-52],color:0x8a97a8,size:5,speed:0.085,rise:1,maxA:0.34});
  g.add(leaves2.points);
  /* 长江滚滚（中前江面）：浪头白沫两层 + 江雾顺流 */
  const foam=makeGlow({n:300,box:[130,5,60],pos:[8,-0.4,-34],color:0xbfd2e4,size:9,speed:0.5,rise:1,maxA:0.34});
  g.add(foam.points);
  const foam2=makeGlow({n:200,box:[150,4,80],pos:[4,-0.6,-20],color:0x9fb4c8,size:7,speed:0.42,rise:1,maxA:0.26});
  g.add(foam2.points);
  const riverFlow=makeFlow({n:200,box:[120,8,90],pos:[2,1,-36],color:0x8fa0b8,size:16,speed:7.0,maxA:0.22});
  g.add(riverFlow.points);
  /* 高台老人（左前景，望江） */
  const terrace=makeTerrace({w:13,d:7,h:2.4}); terrace.position.set(-13.5,-0.5,6); g.add(terrace);
  const poet=denggaoFigure(1.55); poet.position.set(-13.5,1.9,3.5); poet.rotation.y=-0.15; g.add(poet);
  const motes=makeGlow({n:46,box:[160,26,80],pos:[0,9,-40],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,26,120],pos:[0,10,-56],scale:80,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:20,d:8,color:0x04060a,seed:2072,rim:0.14});
  rk.g.position.set(-15,-1.5,15); g.add(rk.g);
  const tree=makeForeground({kind:'树枝',n:2,w:14,d:5,color:0x04060a,seed:2073,sway:1.4,rim:0.18});
  tree.g.position.set(18,-0.6,13); g.add(tree.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[10,95,-50]},{c:0x1a2232,i:0.6});
  const pl=new THREE.PointLight(0x9fb8d4,1.2,80); pl.position.set(-8,14,-30); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); bankL.update(t,0); bankR.update(t,0);
    water.update(t); leaves.update(t,k); leaves2.update(t);
    foam.update(t); foam2.update(t); riverFlow.update(t);
    motes.update(t); mist.update(t,k);
    rk.update(t,k); tree.update(t,k); poet.update(t,k);
    pl.intensity=k*1.2*(0.9+0.1*Math.sin(t*1.3));
  }};
}

function bBeiqiu(){ // 三 · 万里悲秋 —— 镜头贴近高台：常作客、独登台（八重悲，静）
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x07090e,c2:0x0e131c});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:300,h:26,layers:3,peaks:4,seed:2074,color:0x070a10,atmo:0x1f2a3d,fogK:0.58,glowK:0.04,y:-20});
  ridge.g.position.set(0,0,-130); g.add(ridge.g);
  /* 高台 + 台缘短篱 + 白发老人（独登台，面朝万里秋色） */
  const terrace=makeTerrace({w:16,d:10,h:2.8}); terrace.position.set(0,-0.3,0); g.add(terrace);
  const rail=makeForeground({kind:'栏杆',w:20,h:2.6,color:0x0b0e14,rim:0.2,seed:2075});
  rail.g.position.set(0,2.5,-3.4); g.add(rail.g);
  const poet=denggaoFigure(1.7); poet.position.set(1.2,2.5,-1.2); poet.rotation.y=0.08; g.add(poet);
  /* 台下万里秋雾（万里之遥） */
  const mist=makeMist({n:9,spread:[260,30,150],pos:[0,4,-70],scale:88,color:0x7e8ea8,op:0.10});
  g.add(mist.g);
  /* 孤雁远去（客） */
  const goose=makeGulls({n:1,cx:0,cz:-60,y:16,r:26,sp:0.05,color:0x0d1420});
  g.add(goose.g);
  /* 霜晶微尘 */
  const frost=makeGlow({n:70,box:[90,16,50],pos:[0,9,-20],color:0xcdd8e6,size:4.5,speed:0.045,rise:0,maxA:0.3});
  g.add(frost.points);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:6,color:0x04060a,seed:2076,rim:0.14});
  rk.g.position.set(-12,2.0,9); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:16,n:7,d:5,color:0x04060a,seed:2077,sway:0.5});
  reeds.g.position.set(17,2.3,2); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.44,p:[-20,80,-30]},{c:0x1a2232,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); frost.update(t); goose.update(t);
    rail.update(t,k); rk.update(t,k); reeds.update(t,k); poet.update(t,k);
  }};
}

function bTingbei(){ // 四（末境可点击）· 霜鬓停杯 —— 点击落木长江：落叶如雨+江浪层叠+镜头拔高
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  /* —— 远世界（点击后整体下沉 → 镜头拔高感）：江、岸、落木、浪 —— */
  const world=new THREE.Group(); g.add(world);
  const water=makeWater({size:640,seg:92,amp:0.9,freq:0.08,speed:0.95,flow:[0.1,2.0],spec:2.0,
    deep:0x071120,shallow:0x112a40,skyc:0x1d3348,moonDir:[16,108,-190]});
  water.mesh.position.y=-10; world.add(water.mesh);
  const ridge=makeRange({r:280,h:24,layers:2,peaks:4,seed:2078,color:0x070a10,atmo:0x223044,fogK:0.60,glowK:0.05,y:-24});
  ridge.g.position.set(0,0,-130); world.add(ridge.g);
  const bankL=makeRange({r:160,h:42,layers:2,peaks:3,seed:2079,arc:Math.PI*0.38,a0:-Math.PI*0.92,
    color:0x070a10,atmo:0x27334a,fogK:0.62,glowK:0.08,y:-26});
  bankL.g.position.set(-18,-4,-16); world.add(bankL.g);
  const leaves=makeLeaves({n:300,box:[130,46,80],pos:[-6,26,-44],color:0xbfcadb,seed:2080,op:0.85});
  world.add(leaves.mesh);
  const leaves2=makeGlow({n:220,box:[90,38,64],pos:[-16,22,-56],color:0x8a97a8,size:5,speed:0.08,rise:1,maxA:0.12});
  world.add(leaves2.points);
  const foam=makeGlow({n:240,box:[170,5,60],pos:[-22,-9,-28],color:0xbfd2e4,size:8,speed:0.5,rise:1,maxA:0.2});
  world.add(foam.points);
  const riverFlow=makeFlow({n:180,box:[130,10,90],pos:[-12,-6,-30],color:0x8fa0b8,size:16,speed:6.5,maxA:0.14});
  world.add(riverFlow.points);
  const mistW=makeMist({n:6,spread:[230,24,110],pos:[0,-2,-60],scale:78,color:0x7e8ea8,op:0.07});
  world.add(mistW.g);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaec2d8,
    transparent:true,opacity:0.4,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(46,20,1); halo.position.set(-4,2,-46); halo.renderOrder=1; world.add(halo);
  const pl=new THREE.PointLight(0x9fb8d4,1.5,70); pl.position.set(-4,4,-36); world.add(pl);
  /* —— 近世界（不沉）：高台、石案、新停的浊酒、老人、前景 —— */
  const terrace=makeTerrace({w:15,d:9,h:2.6}); g.add(terrace);
  const tb=makeStoneTable(); tb.position.set(2.4,2.6,-1.6); g.add(tb);
  const cup=makeVessel({type:'杯',mat:'陶',scale:1.0,liquid:true}); cup.g.position.set(2.2,3.79,-1.4); g.add(cup.g);
  const pot=makeVessel({type:'壶',mat:'陶',scale:0.9}); pot.g.position.set(3.1,3.79,-2.0); g.add(pot.g);
  const poet=denggaoFigure(1.65); poet.position.set(-0.6,2.6,-1.8); poet.rotation.y=-0.5; g.add(poet);
  const frost=makeGlow({n:60,box:[80,14,44],pos:[0,9,-16],color:0xcdd8e6,size:4.5,speed:0.045,rise:0,maxA:0.26});
  g.add(frost.points);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:20,d:7,color:0x04060a,seed:2081,rim:0.14});
  rk.g.position.set(-13,-0.6,10); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:15,n:8,d:5,color:0x04060a,seed:2082,sway:0.6});
  reeds.g.position.set(16,-0.6,3); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.46,p:[-24,84,-36]},{c:0x1a2232,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/4.5);
      const rv=ctl.reveal, sink=rv*rv*(3-2*rv);
      world.position.y=-7.0*sink;
      leaves.setBoost(rv);
      ridge.update(t,0); bankL.update(t,0); water.update(t);
      water.mesh.material.uniforms.uAmp.value=0.9+1.1*rv;
      water.mesh.material.uniforms.uSpeed.value=0.95+0.9*rv;
      leaves.update(t,k); leaves2.update(t); foam.update(t); riverFlow.update(t);
      leaves2.mat.uniforms.uMaxA.value=k*(0.12+0.26*rv);
      foam.mat.uniforms.uMaxA.value=k*(0.20+0.26*rv);
      riverFlow.mat.uniforms.uMaxA.value=k*(0.14+0.20*rv);
      mistW.update(t,k); frost.update(t);
      rk.update(t,k); reeds.update(t,k); poet.update(t,k); cup.update(t,k); pot.update(t,k);
      halo.material.opacity=k*(0.10+0.30*rv);
      pl.intensity=k*1.5*(0.25+0.75*rv*(0.85+0.15*Math.sin(t*2.1)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(3,0.05,0.13); pluck(1,0.5,0.11); pluck(4,1.0,0.10);
        const fl=$('#flash'); fl.textContent='落木长江'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(34,118,-190),ms:1.8,mph:0,mhaze:0.05,dirC:C(0x8fa4c8),dirI:0.5,
  dirP:new THREE.Vector3(30,90,-40),ambC:C(0x1a2232),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,16,-40],lt:[0,16,-40]},
  sky:()=>SK({top:C(0x060910),hor:C(0x141c2a),bot:C(0x080b11),fog:C(0x0f1520),fd:0.0050,star:0.42,
    ms:1.6,moon:new THREE.Vector3(20,100,-180),
    dirC:C(0x8fa4c8),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'风急猿哀',dwell:16,river:0.05,build:bFengYuan,
  cam:{f:[0,9.5,30],t:[1.6,9,26],lf:[-4,10,-30],lt:[-1,9.5,-34]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0060,star:0.5,
    ms:1.9,mph:0,mhaze:0.05,moon:new THREE.Vector3(38,116,-185),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
{ name:'落木长江',dwell:17,river:0.07,build:bLuomu,
  cam:{f:[0,17,62],t:[0,15,54],lf:[-4,12,-56],lt:[0,14,-68]},
  sky:()=>SK({top:C(0x080c13),hor:C(0x1a2331),bot:C(0x090d13),fog:C(0x121a26),fd:0.0058,star:0.46,
    ms:1.85,mph:0,mhaze:0.05,moon:new THREE.Vector3(10,110,-195),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1b2330),ambI:0.6}) },
{ name:'万里悲秋',dwell:17,river:0.015,build:bBeiqiu,
  cam:{f:[0,7.5,22],t:[-1.6,7,19],lf:[0,7.5,-8],lt:[0.5,7,-12]},
  sky:()=>SK({top:C(0x060a10),hor:C(0x141b28),bot:C(0x080b10),fog:C(0x101622),fd:0.0065,star:0.32,
    ms:1.5,mph:0.08,mhaze:0.06,moon:new THREE.Vector3(-30,120,-190),
    dirC:C(0x8496ac),dirI:0.42,ambC:C(0x19202e),ambI:0.66}) },
{ name:'霜鬓停杯',dwell:18,river:0.03,build:bTingbei,
  cam:{f:[1.5,6.8,19],t:[-1.8,6.2,16.5],lf:[-1,6.5,-16],lt:[-2,8,-22]},
  sky:()=>SK({top:C(0x070b12),hor:C(0x182030),bot:C(0x090d13),fog:C(0x111826),fd:0.0062,star:0.42,
    ms:1.7,mph:0.04,mhaze:0.05,moon:new THREE.Vector3(16,108,-190),
    dirC:C(0x8fa4c8),dirI:0.46,ambC:C(0x1a2232),ambI:0.64}) },
];
"""
