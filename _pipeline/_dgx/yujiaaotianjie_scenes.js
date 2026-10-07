/* ================= 渔家傲·天接云涛连晓雾 · 四境场景（水墨夜思·星海神游变体：云涛星河、梦魂帝所、路长嗟暮、风鹏三山） ================= */

/* 小行舟：弯壳船体 + 篷（无帆，随波轻荡） */
function makeRowBoat(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.75,0.4,4.6,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.5,1.4); B.put(hull,0x241a10);
  const bow=new THREE.ConeGeometry(0.55,1.4,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.7,1.35); bow.translate(2.9,0.05,0); B.put(bow,0x241a10);
  const canopy=new THREE.CylinderGeometry(0.62,0.62,1.9,10,1,true,Math.PI,Math.PI);
  canopy.scale(1,0.8,1.25); canopy.rotateZ(Math.PI/2); canopy.translate(-0.4,0.75,0); B.put(canopy,0x3a2c1c);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a4658,emissive:0x080b12,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x9db8d8:o.rimC,i:0.3,p:2.5})));
  g.scale.setScalar(s);
  return g;
}


/* 大鹏：巨鸟展翅（巨大双翼，合批 1 mesh） */
function makeRoc(o){
  o=o||{};
  const g=new THREE.Group();
  const B=new GeoBag();
  const c=o.color===undefined?0x242e3e:o.color;
  const body=new THREE.SphereGeometry(1.2,8,6); body.scale(2.2,0.9,0.9); B.put(body,c);
  const head=new THREE.ConeGeometry(0.5,1.4,6); head.rotateZ(-Math.PI/2);
  head.translate(2.6,0.3,0); B.put(head,shadeColor(c,1.2));
  const tail=new THREE.BoxGeometry(2.0,0.1,1.0); tail.translate(-2.4,0.1,0); B.put(tail,c);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x7090b8,emissive:0x08101a}),{c:o.rimC===undefined?0x9aa8c9:o.rimC,i:0.35,p:2.5})));
  /* 巨翅两扇（长展） */
  const wgeo=new THREE.PlaneGeometry(6.5,2.0); wgeo.rotateY(Math.PI/2);
  const wmat=new THREE.MeshPhongMaterial({color:0x344458,side:THREE.DoubleSide,shininess:18,specular:0x8ab4dc});
  const w1=new THREE.Mesh(wgeo,wmat); w1.position.x=-0.2;
  const w2=new THREE.Mesh(wgeo,wmat); w2.position.x=-0.2;
  g.add(w1,w2);
  g.userData.w1=w1; g.userData.w2=w2;
  g.scale.setScalar(o.scale===undefined?1.6:o.scale);
  return g;
}

/* 帆船群：星海舞帆（InstancedMesh 帆片） */
function makeStarSails(o){
  o=o||{};
  const g=new THREE.Group();
  const R=seedRnd(o.seed===undefined?1061:o.seed);
  const n=o.n===undefined?16:o.n;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*(o.w===undefined?180:o.w), z=(o.z0===undefined?-30:o.z0)-R()*46;
    const sc=0.6+R()*1.1;
    const hull=new THREE.BoxGeometry(2.8*sc,0.4*sc,0.9*sc);
    hull.translate(x,0.35*sc,z); B.put(hull,0x141822);
    const sail=new THREE.CylinderGeometry(0.55*sc,0.4*sc,2.4*sc,7,1,true,0,Math.PI);
    sail.translate(x,1.55*sc,z); B.put(sail,0x8fa4c0);
  }
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a6080,emissive:0x0a1018,side:THREE.DoubleSide}),{c:0x9aa8c9,i:0.25,p:2.5})));
  return g;
}

function bCover(){ // 封面 · 星海浩渺
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090f,c2:0x121724});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x080c14,atmo:0x26344c,fogK:0.74,glowK:0.09,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x05070c,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:70,box:[220,40,130],pos:[0,10,-40],color:0xa8bce0,size:8,speed:0.05,rise:0,maxA:0.45});
  g.add(motes.points);
  addLights(g,{c:0x8fa8d0,i:0.42,p:[30,70,40]},{c:0x1c2438,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bYuntao(){ // 一（标志性瞬间）· 云涛星河 —— 天接云涛连晓雾，星河欲转千帆舞
  const g=new THREE.Group();
  /* 浩瀚水天（星河倒映的大水） */
  const water=makeWater({size:900,seg:110,amp:0.9,freq:0.08,speed:0.9,flow:[0.6,0.6],spec:1.9,
    deep:0x06101c,shallow:0x143454,skyc:0x2a5078,moonDir:[0,110,-170]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:24,layers:2,peaks:4,seed:1071,color:0x080c14,atmo:0x223650,fogK:0.60,glowK:0.07,y:-18});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 云涛翻涌：上下层层浮云 */
  const clouds=makeMist({n:10,spread:[280,26,140],pos:[0,24,-64],scale:92,color:0x24364c,op:0.35});
  g.add(clouds.g);
  /* 千帆舞：星海中乘风起舞的帆船阵列 */
  const sails=makeStarSails({n:18,w:190,z0:-36,seed:1073}); g.add(sails);
  /* 银河光屑粒子（星河欲转） */
  const galaxy=makeGlow({n:240,box:[160,28,110],pos:[0,14,-32],color:0xc8e0ff,size:5.5,speed:0.06,rise:0,maxA:0.5});
  g.add(galaxy.points);
  const mist=makeMist({n:8,spread:[240,22,120],pos:[0,8,-48],scale:76,color:0x7e9cb8,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x05080e,seed:191,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x9cb8e0,i:0.55,p:[0,110,-50]},{c:0x1a263c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); clouds.update(t,k); galaxy.update(t); mist.update(t,k);
    rk.update(t,k);
    sails.position.x=-((t*0.9)%46)+12;
    sails.position.y=Math.sin(t*0.8)*0.25;
  }};
}
function bDisuo(){ // 二 · 梦魂帝所 —— 仿佛梦魂归帝所，闻天语
  const g=new THREE.Group();
  /* 云海托底（非水面，是纯粹云海） */
  const seaCloud=makeGround({r:140,c1:0x101a28,c2:0x203046});
  seaCloud.mesh.position.y=-1.5; g.add(seaCloud.mesh);
  const ridge=makeRange({r:230,h:32,layers:2,peaks:4,seed:1081,color:0x0a1018,atmo:0x283852,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 天帝宫阙虚影（云上重楼，GeoBag 合批 1 mesh） */
  const TB=new GeoBag();
  for(let i=0;i<3;i++){
    const w=14-i*3, h=18+i*6, d=10-i*2, x=(i-1)*18, z=-50-i*6;
    const b=new THREE.BoxGeometry(w,h,d); b.translate(x,h/2,z); TB.put(b,0x162438);
    const r=new THREE.ConeGeometry(w*0.8,4.5,4); r.rotateY(Math.PI/4);
    r.translate(x,h+2.25,z); TB.put(r,0x243450);
  }
  g.add(TB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x7090b8,emissive:0x0a1420}),{c:0x9aa8c9,i:0.25,p:2.4})));
  /* 天语之光（神圣光束自九天垂落） */
  const beam=new THREE.Mesh(new THREE.PlaneGeometry(16,70),
    new THREE.MeshBasicMaterial({color:0xd8ecff,transparent:true,opacity:0.45,depthWrite:false,side:THREE.DoubleSide}));
  beam.position.set(0,26,-46); g.add(beam);
  /* 梦魂独立（李清照梦中身影，仰首闻天语） */
  const soul=makeFigure({pose:'指月',robe:0x344660,belt:0x6a86aa,hat:'发髻',face:0,scale:1.3,rim:0.65,rimC:0x9ad0ff,noProp:true});
  soul.position.set(0,0,-6); g.add(soul);
  const stars=makeGlow({n:90,box:[110,28,70],pos:[0,16,-30],color:0xc8e4ff,size:6,speed:0.045,rise:1,maxA:0.42});
  g.add(stars.points);
  const mist=makeMist({n:8,spread:[220,24,120],pos:[0,10,-42],scale:74,color:0x7a94b4,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.8,w:20,d:7,color:0x060a12,seed:193,rim:0.14});
  rk.g.position.set(-13,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xa0c4ee,i:0.55,p:[0,100,-40]},{c:0x1a263c,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); stars.update(t); mist.update(t,k); soul.update(t,k); rk.update(t,k);
    beam.material.opacity=k*0.45*(0.75+0.2*Math.sin(t*1.4));
  }};
}
function bLuchang(){ // 三 · 路长嗟暮 —— 我报路长嗟日暮，学诗谩有惊人句
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x080c14,c2:0x121a24});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:32,layers:2,peaks:4,seed:1091,color:0x090d16,atmo:0x2a3648,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 漫漫长路（向暮色延伸） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.06,120),
    new THREE.MeshPhongMaterial({color:0x161c28,shininess:8,specular:0x2c384a}));
  road.rotation.y=0.15; road.position.set(2,0.03,-34); g.add(road);
  /* 西沉残日（嗟日暮） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(9,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xd88050,transparent:true,opacity:0.88,fog:false}));
  sun.position.set(-42,18,-120); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc86038,
    transparent:true,opacity:0.4,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(70,70,1); sunGlow.position.set(-42,18,-120); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 诗人独立（嗟叹前路） */
  const poet=makeFigure({pose:'独立',robe:0x344660,belt:0x6a86aa,hat:'发髻',face:-0.3,scale:1.25,rim:0.5,rimC:0x9ad0ff});
  poet.position.set(-1,0,-5); g.add(poet);
  /* 散落书卷词简（学诗谩有惊人句） */
  for(let i=0;i<4;i++){
    const scroll=new THREE.Mesh(new THREE.BoxGeometry(0.7,0.12,1.1),
      new THREE.MeshPhongMaterial({color:0xc4b494,shininess:10}));
    scroll.position.set(1.5+i*0.8,0.12,-4.5+Math.sin(i*2)*0.6); scroll.rotation.y=i*0.4;
    g.add(scroll);
  }
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-44],scale:70,color:0x7a8ca0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x060810,seed:195,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc08860,i:0.44,p:[-50,50,-40]},{c:0x1c2434,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); poet.update(t,k); rk.update(t,k);
    sunGlow.material.opacity=k*(0.35+0.05*Math.sin(t*0.5));
  }};
}
function bPengju(){ // 四（末境·可点击）· 风鹏三山 —— 九万里风鹏正举，风休住，蓬舟吹取三山去（点击：狂飙起，大鹏振翅冲霄，蓬舟飞驶三山）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,storm:0};
  /* 沧海大浪 + 背景远峰 */
  const water=makeWater({size:850,seg:100,amp:1.6,freq:0.075,speed:1.2,flow:[0,2.2],spec:1.7,
    deep:0x061220,shallow:0x143c5e,skyc:0x285078,moonDir:[0,110,-170]});
  g.add(water.mesh);
  const ridge=makeRange({r:260,h:32,layers:2,peaks:4,seed:1095,color:0x08101a,atmo:0x20344c,fogK:0.60,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 海上三神山（蓬莱、方丈、瀛洲，远景三座耸拔神山，顶缀仙光） */
  const santai=new THREE.Group();
  [[-26,44,-96,1.0],[0,56,-110,1.2],[28,40,-90,0.9]].forEach(function(p,i){
    const mt=new THREE.Mesh(new THREE.ConeGeometry(14*p[3],p[1],5),
      new THREE.MeshPhongMaterial({color:0x0c1624,shininess:16,specular:0x5078a0}));
    mt.position.set(p[0],p[1]/2-8,p[2]); santai.add(mt);
    const aura=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x7fd4ff,
      transparent:true,opacity:0.4,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    aura.scale.set(40,40,1); aura.position.set(p[0],p[1]-6,p[2]); santai.add(aura);
  });
  g.add(santai);
  /* 巨鹏（高空振翅） */
  const roc=makeRoc({scale:2.0,rimC:0xb0d8ff});
  roc.position.set(-6,18,-30); g.add(roc);
  /* 蓬舟（一叶乘风破浪的轻舟） */
  const boat=makeRowBoat({scale:1.4,rimC:0xa8d0f8});
  boat.position.set(2,0.6,-6); boat.rotation.y=0.25; g.add(boat);
  /* 九万里大风（定向狂风流） */
  const wind=makeFlow({n:550,box:[180,30,120],pos:[0,16,-26],color:0x8eb4dc,size:22,speed:8.5,maxA:0.35});
  g.add(wind.points);
  const burst=makeBurst({n:100,color:0xa0d4ff,pos:[0,12,-20]}); g.add(burst.points);
  const mist=makeMist({n:8,spread:[240,24,130],pos:[0,10,-48],scale:76,color:0x7a9cb8,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x05080e,seed:197,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x98b8e0,i:0.52,p:[0,110,-40]},{c:0x1a263c,i:0.62});
  const pl=new THREE.PointLight(0x8ac0f0,2.6,50); pl.position.set(0,8,-10); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.storm=Math.min(1,ctl.storm+dt/2.4);
      ridge.update(t,0);
      water.update(t); wind.update(t); mist.update(t,k); rk.update(t,k);
      burst.update(t);
      /* 大鹏振翅：点击后猛振翅冲霄 */
      const flapRate=ctl.storm>0?8:4;
      const f=Math.sin(t*flapRate)*0.5;
      roc.userData.w1.rotation.x=f; roc.userData.w2.rotation.x=-f;
      roc.position.y=18+ctl.storm*16+Math.sin(t*1.5)*0.8;
      roc.position.z=-30-ctl.storm*34;
      /* 蓬舟乘风飞驶向三山 */
      boat.position.z=-6-ctl.storm*30;
      boat.position.x=2+ctl.storm*4;
      boat.position.y=0.6+Math.sin(t*1.2)*0.16;
      boat.rotation.x=-0.04-ctl.storm*0.06;
      pl.intensity=k*2.6*(0.52+ctl.storm*0.44*(0.85+0.15*Math.sin(t*3)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.15); pluck(3,0.4,0.13); pluck(5,0.8,0.13); bell();
        const fl=$('#flash'); fl.textContent='蓬舟吹取三山去'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
