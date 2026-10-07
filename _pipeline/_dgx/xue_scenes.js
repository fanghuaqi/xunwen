/* ================= 江雪 · 四境场景（宣纸留白：浓墨剪影 + 雪原小径 + 孤舟蓑翁 + 天地皆白一点墨） ================= */

/* 枯树：主干收分 + 发散枝条（合批 1 mesh；冬日无叶的浓墨剪影） */
function makeTree(o){
  o=o||{};
  const h=o.h===undefined?11:o.h, R=seedRnd(o.seed===undefined?5:o.seed);
  const trunkC=o.trunk===undefined?0x23262b:o.trunk;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*1.4-0.7,h*0.98,0],h*0.050,h*0.014,8),trunkC);
  const nb=o.branches===undefined?8:o.branches;
  for(let i=0;i<nb;i++){
    const a=(i/nb)*Math.PI*2+R()*0.9, el=0.45+R()*0.85, len=h*(0.28+R()*0.40);
    const dx=Math.cos(a)*Math.cos(el), dy=Math.sin(el), dz=Math.sin(a)*Math.cos(el);
    const y0=h*(0.50+R()*0.42);
    const p1=[dx*len*0.22,y0+dy*len*0.28,dz*len*0.22];
    const p2=[dx*len,y0+dy*len,dz*len];
    B.put(limbGeo(p1,p2,h*0.020,h*0.007,6),trunkC);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x3a3d44,emissive:0x060608}),
    {c:o.rimC===undefined?0xe8e2d0:o.rimC,i:o.rim===undefined?0.14:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 寒鸦：双翅扑动的远鸟（2 draw call/只，掠过群山后隐入天际） */
function makeBird(o){
  o=o||{};
  const c=o.color===undefined?0x2c2f33:o.color;
  const g=new THREE.Group();
  const mat=new THREE.MeshBasicMaterial({color:c,side:THREE.DoubleSide,transparent:true,opacity:0.95});
  const wgeo=new THREE.PlaneGeometry(o.w===undefined?2.8:o.w,0.8);
  const w1=new THREE.Mesh(wgeo,mat); w1.position.x=-1.35;
  const w2=new THREE.Mesh(wgeo,mat); w2.position.x=1.35;
  g.add(w1,w2);
  g.userData={mat,w1,w2,op:0.95};
  return g;
}

/* 孤舟：Lathe 半壳拉长成舢板 + 坐板（合批 1 mesh） */
function makeBoat(o){
  o=o||{};
  const wood=o.wood===undefined?0x4a3c2a:o.wood;
  const B=new GeoBag();
  const pts=[[0,0],[0.52,0.05],[0.95,0.32],[1.14,0.66],[1.2,0.74]].map(p=>new THREE.Vector2(p[0],p[1]));
  const hull=new THREE.LatheGeometry(pts,20); hull.scale(1.15,0.62,2.9); B.put(hull,wood);
  const bench=new THREE.BoxGeometry(1.6,0.09,0.55); bench.translate(0,0.47,0.5); B.put(bench,shadeColor(wood,1.3));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:14,specular:0x554433,emissive:0x0a0806}),
    {c:o.rimC===undefined?0xe8e0cc:o.rimC,i:o.rim===undefined?0.18:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 远舟剪影：舟 + 蓑笠翁 + 斗笠全合批 1 mesh（"天地皆白独此一点墨"的远观点） */
function makeBoatSil(o){
  o=o||{};
  const ink=o.ink===undefined?0x2c2f33:o.ink;
  const B=new GeoBag();
  const pts=[[0,0.02],[0.55,0.08],[0.98,0.36],[1.16,0.70],[1.2,0.78]].map(p=>new THREE.Vector2(p[0],p[1]));
  const hull=new THREE.LatheGeometry(pts,16); hull.scale(1.1,0.6,2.7); B.put(hull,ink);
  const body=new THREE.CylinderGeometry(0.34,0.9,1.5,9); body.translate(0,0.72,-0.3); B.put(body,ink);
  const head=new THREE.SphereGeometry(0.27,8,6); head.translate(0,1.66,-0.3); B.put(head,ink);
  const hat=new THREE.ConeGeometry(0.72,0.32,12); hat.translate(0,1.90,-0.3); B.put(hat,ink);
  const mesh=B.mesh(new THREE.MeshBasicMaterial({color:0xffffff,vertexColors:true}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 钓竿 + 钓线：细竹竿 + 始终连着竿尖的钓线（竿动线随） */
function makeRod(len){
  len=len===undefined?4.6:len;
  const g=new THREE.Group();
  const geo=new THREE.CylinderGeometry(0.025,0.05,len,6); geo.translate(0,len/2,0);
  const rod=new THREE.Mesh(geo,new THREE.MeshPhongMaterial({color:0x33291c,shininess:20,specular:0x554433}));
  g.add(rod);
  const lp=new Float32Array(6);
  const lineGeo=new THREE.BufferGeometry();
  lineGeo.setAttribute('position',new THREE.BufferAttribute(lp,3));
  const line=new THREE.Line(lineGeo,new THREE.LineBasicMaterial({color:0x2c2f33,transparent:true,opacity:0.65}));
  line.renderOrder=2; g.add(line);
  const tipV=new THREE.Vector3();
  return {g,update(){
    g.updateWorldMatrix(true,false);
    tipV.set(0,len,0).applyMatrix4(rod.matrixWorld);
    lp[0]=tipV.x; lp[1]=tipV.y; lp[2]=tipV.z;
    lp[3]=tipV.x; lp[4]=0.07; lp[5]=tipV.z+0.22;
    lineGeo.attributes.position.needsUpdate=true;
  }};
}

function bCover(){ // 卷首 · 宣纸雪意，远舟一点
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0xe9e3d3,c2:0xdcd4bd,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:30,layers:3,peaks:5,seed:41,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.05,glow:0xf4eeda,y:-12});
  ridge.g.position.set(0,0,-70); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const hint=makeBoatSil({scale:1.5}); hint.position.set(-9,0.05,-80); g.add(hint);
  const snow=makeGlow({n:150,box:[240,54,160],pos:[0,24,-24],color:0xb3bfcb,size:3.2,speed:0.034,
    rise:1,add:false,maxA:0.42});
  g.add(snow.points);
  const mist=makeMist({n:10,spread:[280,36,160],pos:[0,12,-60],scale:88,color:0xe6dfcc,op:0.10});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',w:64,n:20,d:8,color:0x2c2f33,seed:5,sway:1.0,tip:0x4a4f56});
  reeds.g.position.set(0,-1.5,32); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[60,120,40]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); snow.update(t); mist.update(t,k); reeds.update(t,k);
  }};
}function bMountains(){ // 一 · 千山鸟绝 —— 浓墨层叠山影，群鸟掠过后隐入天际
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d3,c2:0xded7c4,y:-1.5}); g.add(grd.mesh);
  /* 背景：远山淡墨（连绵成脊，愈远愈淡） */
  const ridge=makeRange({r:260,h:84,layers:3,peaks:6,seed:151,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.58,glowK:0.05,glow:0xf4eeda,y:-6});
  ridge.g.position.set(0,0,-90); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 中景：近山浓墨（一层压一层；接缝转向背面） */
  const ridge2=makeRange({r:160,h:44,layers:2,peaks:6,seed:161,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.66,glowK:0.04,glow:0xf4eeda,y:-4,order:-5});
  ridge2.g.position.set(0,0,-30); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  /* 鸟飞绝：寒鸦掠过群山，次第隐入天际 */
  const birds=[];
  for(let i=0;i<7;i++){
    const b=makeBird({w:3.4+i*0.2});
    g.add(b);
    birds.push({b,sp:0.010+0.010*Math.abs(Math.sin(i*7.7)),y:36+i*5.2,ph:i/7,z:-96-i*8,dir:i%2?1:-1});
  }
  const snow=makeGlow({n:150,box:[230,64,150],pos:[0,26,-20],color:0xb3bfcb,size:3.0,speed:0.036,
    rise:1,add:false,maxA:0.45});
  g.add(snow.points);
  const mist=makeMist({n:8,spread:[300,34,150],pos:[0,14,-100],scale:92,color:0xe0d8c2,op:0.11});
  g.add(mist.g);
  /* 前景：近岸坡石 + 枯苇（框住画面下缘） */
  const rk=makeForeground({kind:'坡石',n:3,r:7,w:26,d:6,color:0x23262b,seed:63,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(20,-2.4,48); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:40,n:14,d:6,color:0x2c2f33,seed:71,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(-24,-2,44); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.55,p:[60,120,40]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); snow.update(t); mist.update(t,k);
    rk.update(t,k); reeds.update(t,k);
    for(const o of birds){
      const s=(t*o.sp+o.ph)%1;
      o.b.position.set(o.dir*(-150+300*s),o.y+Math.sin(t*0.9+o.ph*9)*2.5,o.z);
      const f=Math.sin(t*8+o.ph*9)*0.55;
      o.b.userData.w1.rotation.z=f; o.b.userData.w2.rotation.z=-f;
      o.b.userData.mat.opacity=k*o.b.userData.op*(sstep(0,0.12,s)*(1-sstep(0.80,0.98,s)));
    }
  }};
}
function bPaths(){ // 二 · 万径踪灭 —— 雪原小径扇开没入雾中，一行远踪渐被落雪掩没
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0xeae4d4,c2:0xdfd8c5,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:220,h:40,layers:3,peaks:4,seed:171,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.64,glowK:0.04,glow:0xf4eeda,y:-12});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 万径：数条小径扇开（踏雪的暖灰，须比雪面深一档，别亮成光带） */
  [[0,0,2.4],[-0.26,10,2.0],[0.26,10,2.0],[-0.52,24,1.5],[0.52,24,1.5],[-0.84,44,1.2],[0.84,44,1.2]].forEach(function(d){
    const p=new THREE.Mesh(new THREE.BoxGeometry(d[2],0.08,250),
      new THREE.MeshPhongMaterial({color:0x7e7663,shininess:4,specular:0x55503f}));
    p.rotation.y=d[0]; p.position.set(d[1],0.05,-70); g.add(p);
  });
  /* 人踪灭：一串脚印循环"显现——被落雪掩没" */
  const steps=[];
  for(let i=0;i<24;i++){
    const mat=new THREE.MeshBasicMaterial({color:0x6b6152,transparent:true});
    const s=new THREE.Mesh(new THREE.CircleGeometry(0.24,8),mat);
    s.rotation.x=-Math.PI/2;
    s.position.set((i%2?0.5:-0.5),0.12,-4-i*1.6);
    g.add(s); steps.push({mat,ph:i/24});
  }
  /* 枯树数株（浓墨剪影） */
  [[-9,-22],[10,-38],[-17,-58],[7,-70]].forEach(function(p,i){
    const tr=makeTree({h:5.2+i*0.5,seed:31+i,branches:6,trunk:0x23262b,rim:0.14});
    tr.g.position.set(p[0],0,p[1]); g.add(tr.g);
  });
  /* 远处一行旅人，渐行渐没入风雪（人踪 → 灭） */
  const crowd=makeCrowd({n:7,rect:[-42,-46,84,16],seed:33,color:0x3a3d44,rimC:0xe8e2d0,rim:0.16,
    sMin:0.62,sMax:0.92});
  g.add(crowd.mesh);
  const snow=makeGlow({n:180,box:[220,62,150],pos:[0,24,-16],color:0xb3bfcb,size:3.2,speed:0.040,
    rise:1,add:false,maxA:0.50});
  g.add(snow.points);
  const mist=makeMist({n:8,spread:[280,30,150],pos:[0,10,-80],scale:86,color:0xe0d8c2,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:6,color:0x23262b,seed:73,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(16,-1.6,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:44,n:16,d:6,color:0x2c2f33,seed:75,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(-18,-1.8,10); g.add(reeds.g);
  addLights(g,{c:0xd5d1c4,i:0.45,p:[50,110,40]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); snow.update(t); mist.update(t,k); rk.update(t,k); reeds.update(t,k);
    crowd.update(t);
    const c=(t/26)%1;                          // 26s 一轮：远踪显而复灭
    crowd.mesh.material.opacity=k*(1-sstep(0.30,0.72,c));
  }};
}
function bBoat(){ // 三 · 孤舟蓑翁 —— 寒江近景：一舟一翁，蓑衣斗笠，钓竿垂波
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:96,amp:0.36,freq:0.09,speed:0.5,flow:[0.2,0.25],spec:0.8,
    deep:0x8f918a,shallow:0xbdbaa9,skyc:0xd9d2bd,moonDir:[0.3,1,0.2]});
  g.add(water.mesh);
  /* 远岸淡墨一线 */
  const ridge=makeRange({r:200,h:20,layers:2,peaks:4,seed:181,color:0x2c2f33,atmo:0xdcd5c0,
    fogK:0.70,glowK:0.04,glow:0xf4eeda,y:-6});
  ridge.g.position.set(0,0,-70); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 孤舟 + 蓑笠翁（深袍 + 蓑衣披肩 + 斗笠；人比舟略矮，才是舟中人） */
  const craft=new THREE.Group(); craft.position.set(0,0.14,-5.5); craft.rotation.y=0.42; g.add(craft);
  craft.add(makeBoat({scale:1.35}));
  const angler=makeFigure({pose:'独立',robe:0x4a4538,belt:0x3a362c,hat:'无',beard:true,
    scale:0.78,rim:0.14,rimC:0xe8e2d0});
  angler.position.set(0,0.40,-1.35); angler.rotation.y=-0.5; craft.add(angler);
  const cape=new THREE.Mesh(new THREE.ConeGeometry(0.95,1.35,12,1,true),
    new THREE.MeshPhongMaterial({color:0x57503c,shininess:6,specular:0x6a6250,side:THREE.DoubleSide}));
  cape.position.set(0,2.10,0); angler.add(cape);
  const hat=new THREE.Mesh(new THREE.ConeGeometry(0.70,0.30,14),
    new THREE.MeshPhongMaterial({color:0x6e5c3e,shininess:8,specular:0x8a7a56}));
  hat.position.set(0,3.90,0.02); angler.add(hat);
  const rod=makeRod(3.8); rod.g.position.set(0.52,1.44,-1.20);
  rod.g.rotation.set(-1.85,-0.6,0); craft.add(rod.g);
  /* 浮冰几点（远小近大，几点缀在寒江上） */
  const ice=[];
  for(let i=0;i<7;i++){
    const f=new THREE.Mesh(new THREE.CircleGeometry(1.2+1.8*Math.abs(Math.sin(i*3.1)),10),
      new THREE.MeshBasicMaterial({color:0xf2eee0,transparent:true}));
    f.rotation.x=-Math.PI/2;
    const x0=-33+i*11; f.position.set(x0,0.06,-38+i*7.3);
    g.add(f); ice.push({f,x0,ph:i*1.7});
  }
  const snow=makeGlow({n:200,box:[150,44,90],pos:[0,18,-4],color:0xb3bfcb,size:3.4,speed:0.040,
    rise:1,add:false,maxA:0.50});
  g.add(snow.points);
  const mist=makeMist({n:8,spread:[240,24,130],pos:[0,8,-40],scale:74,color:0xe2dac4,op:0.10});
  g.add(mist.g);
  const rkR=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:4,color:0x23262b,seed:77,rim:0.12,rimC:0xf0ead8});
  rkR.g.position.set(6.5,-1.5,8); g.add(rkR.g);
  const rkL=makeForeground({kind:'坡石',n:2,r:1.9,w:8,d:4,color:0x23262b,seed:87,rim:0.12,rimC:0xf0ead8});
  rkL.g.position.set(-2.6,-1.5,8.5); g.add(rkL.g);
  addLights(g,{c:0xd0d0c8,i:0.45,p:[50,100,40]},{c:0xd2ccb8,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); snow.update(t); mist.update(t,k);
    rkR.update(t,k); rkL.update(t,k); rod.update(); angler.update(t,k);
    for(const o of ice){
      o.f.position.x=o.x0+Math.sin(t*0.10+o.ph)*2.2;
      o.f.position.y=0.06+Math.sin(t*0.5+o.ph)*0.05;
    }
    craft.position.y=0.14+Math.sin(t*0.5)*0.07;
    craft.rotation.z=Math.sin(t*0.4+1)*0.015;
  }};
}
function bSnowSolo(){ // 四（末境·可点击）· 独钓寒江 —— 标志性瞬间：天地皆白独此一点墨
  const g=new THREE.Group();
  const ctl={t:0,boost:0,clicked:false};
  const water=makeWater({size:900,seg:100,amp:0.28,freq:0.08,speed:0.42,flow:[0.1,0.2],spec:0.55,
    deep:0x999b94,shallow:0xc4c1b0,skyc:0xded7c2,moonDir:[0.2,1,0.1]});
  g.add(water.mesh);
  /* 远岸：几乎化进天光的一线淡墨 */
  const ridge=makeRange({r:260,h:26,layers:2,peaks:4,seed:191,color:0x4a4e55,atmo:0xe4dcc7,
    fogK:0.78,glowK:0.03,glow:0xf6f0de,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 一点墨：茫茫江面上的孤舟蓑笠翁（剪影 + 可轻摇的钓竿） */
  const craft=new THREE.Group(); craft.position.set(0,0.05,-40); g.add(craft);
  craft.add(makeBoatSil({scale:2.0}));
  const rodGeo=new THREE.CylinderGeometry(0.03,0.055,4.2,5); rodGeo.translate(0,2.1,0);
  const rodSil=new THREE.Mesh(rodGeo,new THREE.MeshBasicMaterial({color:0x2c2f33,transparent:true}));
  rodSil.position.set(0.6,1.35,-0.9); rodSil.rotation.x=-1.9; rodSil.rotation.z=-0.25; craft.add(rodSil);
  /* 两层落雪：远小近大，细密缓落 */
  const snowFar=makeGlow({n:240,box:[320,76,170],pos:[0,30,-40],color:0xb3bfcb,size:2.4,speed:0.030,
    rise:1,add:false,maxA:0.40});
  const snowNear=makeGlow({n:170,box:[150,46,90],pos:[0,20,6],color:0xaeb9c6,size:3.4,speed:0.040,
    rise:1,add:false,maxA:0.50});
  g.add(snowFar.points,snowNear.points);
  const mist=makeMist({n:10,spread:[320,36,170],pos:[0,12,-64],scale:96,color:0xe4dcc6,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:20,d:6,color:0x23262b,seed:81,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(16,-2.2,14); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:44,n:16,d:6,color:0x2c2f33,seed:83,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(-19,-1.8,12); g.add(reeds.g);
  addLights(g,{c:0xd8d6cc,i:0.4,p:[40,100,30]},{c:0xdcd6c2,i:0.68});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ctl.boost=Math.max(0,ctl.boost-dt/3.4);
      const b=ctl.boost;
      water.update(t); mist.update(t,k); rk.update(t,k); reeds.update(t,k);
      snowFar.update(t); snowNear.update(t);
      /* 雪落更急：速度/密度在满亮基座上按点击系数抬升 */
      snowNear.mat.uniforms.uSpeed.value=0.040*(1+2.4*b);
      snowFar.mat.uniforms.uSpeed.value=0.030*(1+2.0*b);
      snowNear.mat.uniforms.uMaxA.value=k*0.50*(1+0.42*b);
      snowFar.mat.uniforms.uMaxA.value=k*0.40*(1+0.35*b);
      rodSil.rotation.x=1.15+Math.sin(t*3.4)*0.12*b;   // 钓竿轻摇
      craft.position.y=0.05+Math.sin(t*0.5)*0.05;
      craft.rotation.z=Math.sin(t*0.4)*0.012;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0,0.16); pluck(5,0.3,0.10);
        const fl=$('#flash'); fl.textContent='独钓寒江'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.boost=1;                                     // 雪落更急（可反复点）
    },clicked:false};
  return api;
}
