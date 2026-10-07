/* ================= 望江南·梳洗罢 · 三境场景（烟雨江南·望楼变体：梳洗独倚、千帆不是、肠断蘋洲） ================= */

/* 望江楼：江畔小楼（两层木构，栏杆可倚，合批 1 mesh） */
function makeWatchTower(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const c1=o.c1===undefined?0x2a2018:o.c1;
  const base=new THREE.BoxGeometry(7,4.4,5.4); base.translate(0,2.2,0); B.put(base,c1);
  const upper=new THREE.BoxGeometry(6,3.2,4.6); upper.translate(0,6.0,0); B.put(upper,shadeColor(c1,1.15));
  const roof1=new THREE.ConeGeometry(5.4,1.6,4); roof1.rotateY(Math.PI/4); roof1.translate(0,5.4,0); B.put(roof1,0x1a1410);
  const roof2=new THREE.ConeGeometry(4.6,1.5,4); roof2.rotateY(Math.PI/4); roof2.translate(0,8.35,0); B.put(roof2,0x1a1410);
  /* 上层回廊栏杆 */
  const railF=new THREE.BoxGeometry(5.8,0.55,0.14); railF.translate(0,4.7,2.4); B.put(railF,shadeColor(c1,1.3));
  const railL=new THREE.BoxGeometry(0.14,0.55,4.4); railL.translate(-2.9,4.7,0); B.put(railL,shadeColor(c1,1.3));
  const railR=railL.clone(); railR.translate(5.8,0,0); B.put(railR,shadeColor(c1,1.3));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a4050,emissive:0x0a0c10}),{c:o.rimC===undefined?0x8fb3c9:o.rimC,i:0.26,p:2.4})));
  g.scale.setScalar(s);
  return g;
}

/* 帆船群：远近帆点（近帆 2 只完整，远帆用 InstancedMesh 帆片） */
function makeSailField(o){
  o=o||{};
  const g=new THREE.Group();
  /* 远帆：帆片 + 暗船点（一批） */
  const R=seedRnd(o.seed===undefined?471:o.seed);
  const n=o.n===undefined?14:o.n;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*(o.w===undefined?170:o.w), z=(o.z0===undefined?-30:o.z0)-R()*40;
    const sc=0.5+R()*0.9;
    const hull=new THREE.BoxGeometry(2.6*sc,0.35*sc,0.8*sc);
    hull.translate(x,0.3*sc,z); B.put(hull,0x141a20);
    const sail=new THREE.CylinderGeometry(0.5*sc,0.35*sc,2.2*sc,7,1,true,0,Math.PI);
    sail.translate(x,1.4*sc,z); B.put(sail,0xc8c4b4);
  }
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4650,emissive:0x0a0d12,side:THREE.DoubleSide}),{c:0x8fb3c9,i:0.22,p:2.5})));
  return g;
}

function bCover(){ // 封面 · 斜晖江天
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x10141a,c2:0x1a2028});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0d1118,atmo:0x3a4454,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,44); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x0a0d13,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xa8bcd4,size:8,speed:0.05,rise:0,maxA:0.42});
  g.add(motes.points);
  addLights(g,{c:0x9aaec8,i:0.42,p:[30,70,40]},{c:0x222c38,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bShuxi(){ // 一 · 梳洗独倚 —— 楼头独倚的背影，江面空阔
  const g=new THREE.Group();
  const ridge=makeRange({r:210,h:22,layers:2,peaks:3,seed:481,color:0x0d1118,atmo:0x324054,fogK:0.62,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-72); g.add(ridge.g);
  const water=makeWater({size:640,seg:90,amp:0.3,freq:0.11,speed:0.55,flow:[-0.5,0.2],spec:1.3,
    deep:0x0c1420,shallow:0x1a3444,skyc:0x28404c,moonDir:[-70,80,-160]});
  g.add(water.mesh);
  /* 主体：望江楼 + 楼头独倚人（背影） */
  const tower=makeWatchTower({scale:1.35}); tower.position.set(-7,0,-16); tower.rotation.y=0.4; g.add(tower);
  const lady=makeFigure({pose:'独立',robe:0x5a3a44,belt:0x8a6a4a,hat:'发髻',face:-0.7,scale:0.95,rim:0.5,rimC:0xd8b0b8});
  lady.position.set(-4.1,9.0,-11.5); g.add(lady);
  /* 江洲白蘋（近岸一小片） */
  const isle=makeForeground({kind:'坡石',n:3,r:2.6,w:16,d:9,color:0x0d1218,seed:67,rim:0.16});
  isle.g.position.set(10,-1.2,-24); g.add(isle.g);
  const mist=makeMist({n:8,spread:[220,22,120],pos:[0,9,-46],scale:74,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x0a0d13,seed:69,rim:0.15});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  addLights(g,{c:0x9aaec8,i:0.48,p:[-40,80,-40]},{c:0x222c38,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    lady.update(t,k);
    rk.update(t,k);
  }};
}
function bQianfan(){ // 二（标志性瞬间）· 千帆不是 —— 过尽千帆，斜晖脉脉
  const g=new THREE.Group();
  const ridge=makeRange({r:230,h:20,layers:2,peaks:3,seed:491,color:0x0d1118,atmo:0x3a4054,fogK:0.60,glowK:0.06,y:-18});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  const water=makeWater({size:820,seg:100,amp:0.35,freq:0.1,speed:0.6,flow:[-0.8,0.25],spec:1.5,
    deep:0x0c1420,shallow:0x1c3a4c,skyc:0x2c4450,moonDir:[-60,70,-160]});
  g.add(water.mesh);
  /* 千帆：远近帆阵（缓缓东行） */
  const far=makeSailField({n:13,w:180,z0:-34,seed:471}); g.add(far);
  /* 近处一帆（恰在"皆不是"的错过位） */
  const near=makeJunkHull(); near.position.set(8,0.2,-14); near.rotation.y=0.15; g.add(near);
  /* 斜晖：西天暖光带染江 */
  const sunset=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88a50,
    transparent:true,opacity:0.34,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunset.scale.set(150,60,1); sunset.position.set(-70,22,-130); sunset.renderOrder=-7; g.add(sunset);
  const gold=makeGlow({n:110,box:[120,3,70],pos:[-24,1.2,-52],color:0xd8a060,size:8,speed:0.06,rise:0,maxA:0.35});
  g.add(gold.points);
  const mist=makeMist({n:8,spread:[240,22,130],pos:[0,9,-58],scale:78,color:0x8fa4c0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:20,d:8,color:0x0a0d13,seed:71,rim:0.15});
  rk.g.position.set(-13,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xc09068,i:0.42,p:[-60,50,-50]},{c:0x242c34,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); gold.update(t); mist.update(t,k);
    far.position.x=-((t*0.6)%40)+10;                  // 帆阵缓行（循环）
    near.position.z=-14+Math.sin(t*0.5)*2;
    sunset.material.opacity=k*(0.30+0.06*Math.sin(t*0.4));
    rk.update(t,k);
  }};
}
function bChangduan(){ // 三（末境·可点击）· 肠断蘋洲 —— 点击江面，最后一帆远去、斜晖更沉
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,done:0};
  const ridge=makeRange({r:230,h:20,layers:2,peaks:3,seed:501,color:0x0d1118,atmo:0x344054,fogK:0.60,glowK:0.05,y:-18});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  const water=makeWater({size:760,seg:100,amp:0.3,freq:0.11,speed:0.55,flow:[-0.6,0.2],spec:1.4,
    deep:0x0c1420,shallow:0x1a3444,skyc:0x28404c,moonDir:[-60,60,-160]});
  g.add(water.mesh);
  /* 望江楼（远景剪影）+ 楼头人影 */
  const tower=makeWatchTower({scale:1.1}); tower.position.set(-9,0,-22); tower.rotation.y=0.5; g.add(tower);
  const lady=makeFigure({pose:'独立',robe:0x5a3a44,hat:'发髻',face:-0.7,scale:0.8,rim:0.45,rimC:0xd8b0b8});
  lady.position.set(-6.6,7.3,-18.2); g.add(lady);
  /* 最后一帆（点击后远去） */
  const boat=makeJunkHull(); boat.position.set(10,0.2,-20); g.add(boat);
  /* 白蘋洲：近景小洲（肠断处） */
  const isle=makeForeground({kind:'坡石',n:4,r:3.0,w:20,d:10,color:0x0d1218,seed:73,rim:0.16});
  isle.g.position.set(4,-1.2,-10); g.add(isle.g);
  const ping=makeGlow({n:50,box:[16,1.2,9],pos:[4,0.8,-10],color:0xa8c8b0,size:4,speed:0.04,rise:0,maxA:0.35,add:false});
  g.add(ping.points);
  /* 斜晖更沉 */
  const sunset=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88a50,
    transparent:true,opacity:0.3,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunset.scale.set(150,54,1); sunset.position.set(-70,18,-130); sunset.renderOrder=-7; g.add(sunset);
  const mist=makeMist({n:7,spread:[220,20,120],pos:[0,8,-50],scale:74,color:0x8fa4c0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:16,d:7,color:0x0a0d13,seed:75,rim:0.14});
  rk.g.position.set(-12,-1.3,12); g.add(rk.g);
  addLights(g,{c:0xb08a60,i:0.36,p:[-60,44,-50]},{c:0x242c34,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.done=Math.min(1,ctl.done+dt/3.2);
      ridge.update(t,0); water.update(t); ping.update(t); mist.update(t,k);
      lady.update(t,k); rk.update(t,k);
      boat.position.z=-20-ctl.done*30;
      boat.position.x=10+ctl.done*6;
      sunset.material.opacity=k*(0.30-0.14*ctl.done);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.1,0.13); pluck(2,0.7,0.1);
        const fl=$('#flash'); fl.textContent='肠断白蘋洲'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
/* 近帆（单只）：船体+帆（供 2/3 境用） */
function makeJunkHull(){
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.8,0.45,5.2,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.5,1.5); B.put(hull,0x1a1510);
  const bow=new THREE.ConeGeometry(0.6,1.5,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.7,1.4); bow.translate(3.2,0.05,0); B.put(bow,0x1a1510);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a4650,emissive:0x0a0d12}),{c:0x8fb3c9,i:0.26,p:2.5})));
  const mast=new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.09,6.0,6),
    new THREE.MeshPhongMaterial({color:0x241c12}));
  mast.position.set(0,3.1,0); g.add(mast);
  const sail=new THREE.Mesh(new THREE.PlaneGeometry(2.6,4.6),
    new THREE.MeshPhongMaterial({color:0xc8c4b4,side:THREE.DoubleSide,shininess:6,emissive:0x14140f}));
  sail.position.set(0,3.3,0.02); g.add(sail);
  return g;
}
