/* ================= 逢入京使 · 二境场景（大漠金戈·驿路变体：东望泪湿、马上传语） ================= */

/* 使者骑马：马（合批）+ 骑手（makeFigure 缩放坐姿简化为立姿收腿） */
function makeHorse(o){
  o=o||{};
  const c=o.color===undefined?0x3a2c20:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.0,10,8); body.scale(1.9,1.0,0.72); body.translate(0,1.7,0); B.put(body,c);
  const neck=new THREE.CylinderGeometry(0.28,0.42,1.5,7);
  neck.rotateZ(-0.6); neck.translate(1.55,2.5,0); B.put(neck,shadeColor(c,0.9));
  const head=new THREE.SphereGeometry(0.34,8,6); head.scale(1.5,0.9,0.7);
  head.translate(2.25,3.2,0); B.put(head,shadeColor(c,1.1));
  const ear1=new THREE.ConeGeometry(0.09,0.28,5); ear1.translate(2.32,3.6,0.12); B.put(ear1,shadeColor(c,0.8));
  const ear2=ear1.clone(); ear2.translate(0,0,-0.24); B.put(ear2,shadeColor(c,0.8));
  const tail=new THREE.ConeGeometry(0.14,1.1,6); tail.rotateZ(0.5);
  tail.translate(-1.85,1.9,0); B.put(tail,shadeColor(c,0.7));
  [[0.85,-0.32],[0.85,0.32],[-0.95,-0.32],[-0.95,0.32]].forEach(function(p){
    B.put(limbGeo([p[0],1.3,p[1]],[p[0]*1.05,0.06,p[1]],0.13,0.07,6),shadeColor(c,0.85));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a3c2c,emissive:0x060503}),{c:o.rimC===undefined?0xd8a860:o.rimC,i:0.3,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 大漠驿路
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0b0805,c2:0x1c130a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0d0906,atmo:0x4a3820,fogK:0.74,glowK:0.09,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x070503,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xb08858,op:0.10});
  g.add(mist.g);
  const dust=makeGlow({n:60,box:[220,36,130],pos:[0,8,-40],color:0xc8a060,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(dust.points);
  addLights(g,{c:0xd8a860,i:0.45,p:[30,70,40]},{c:0x2c211a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); dust.update(t); }};
}
function bDongwang(){ // 一 · 东望泪湿 —— 驿路东望，长路漫漫
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0c0906,c2:0x1e140a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:28,layers:2,peaks:4,seed:511,color:0x0e0a07,atmo:0x4a3820,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 驿路：一条土路伸向东方地平（画面纵深） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(3.6,0.08,150),
    new THREE.MeshPhongMaterial({color:0x2a2016,shininess:8,specular:0x4a3a24}));
  road.rotation.y=0.1; road.position.set(2,0.03,-44); g.add(road);
  /* 路旁：烽燧墩台两座 + 疏柳 */
  [[-14,-18],[24,-36]].forEach(function(p,i){
    const t=new THREE.Mesh(new THREE.CylinderGeometry(2.2-i*0.5,3.0-i*0.5,9-i*2,8),
      new THREE.MeshPhongMaterial({color:0x241a10,shininess:5}));
    t.position.set(p[0],(9-i*2)/2,p[1]); g.add(t);
  });
  const willow=makeForeground({kind:'坡石',n:1,r:2.6,w:6,d:4,color:0x1c140a,seed:77,rim:0.14});
  willow.g.position.set(-7,-0.8,-9); g.add(willow.g);
  /* 主体：诗人勒马东望（背影） */
  const horse=makeHorse({}); horse.position.set(-1,0,-6); g.add(horse);
  const rider=makeFigure({pose:'独立',robe:0x241c14,belt:0x8a5a2a,hat:'幞头',beard:true,face:0.06,scale:1.05,rim:0.5,rimC:0xd8a860});
  rider.position.set(-1,1.55,-6); g.add(rider);
  /* 长路尘沙 */
  const dust=makeFlow({n:480,box:[170,18,110],pos:[0,9,-30],color:0xb08850,size:20,speed:5.0,maxA:0.3});
  g.add(dust.points);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-48],scale:70,color:0x9a7a4e,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x080504,seed:81,rim:0.15});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  addLights(g,{c:0xd8a860,i:0.48,p:[-50,60,-50]},{c:0x2c211a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); dust.update(t); mist.update(t,k);
    rider.update(t,k);
    horse.rotation.y=Math.sin(t*0.4)*0.03;
    rk.update(t,k);
  }};
}
function bChuanyu(){ // 二（末境·可点击）· 马上传语 —— 两骑相逢，传语报平安（点击：口信化作飞鸿北去）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,fly:0};
  const grd=makeGround({r:130,c1:0x0c0906,c2:0x1d130a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:26,layers:2,peaks:4,seed:521,color:0x0e0a07,atmo:0x4a3820,fogK:0.58,glowK:0.07});
  g.add(ridge.g);
  /* 驿路十字（东西向主路） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(140,0.08,4),
    new THREE.MeshPhongMaterial({color:0x2a2016,shininess:8,specular:0x4a3a24}));
  road.position.set(0,0.03,-14); g.add(road);
  /* 主体：两骑相逢（诗人西向、使者东向，首相对） */
  const horseA=makeHorse({}); horseA.position.set(-4.5,0,-14); horseA.rotation.y=Math.PI/2; g.add(horseA);
  const poet=makeFigure({pose:'独立',robe:0x241c14,belt:0x8a5a2a,hat:'幞头',beard:true,face:Math.PI/2,scale:1.05,rim:0.52,rimC:0xd8a860});
  poet.position.set(-4.5,1.55,-14); g.add(poet);
  const horseB=makeHorse({color:0x4a3a2c}); horseB.position.set(4.5,0,-14); horseB.rotation.y=-Math.PI/2; g.add(horseB);
  const rider=makeFigure({pose:'独立',robe:0x30261a,hat:'幞头',face:-Math.PI/2,scale:1.05,rim:0.5,rimC:0xd8a860});
  rider.position.set(4.5,1.55,-14); g.add(rider);
  /* 口信化作的一线飞鸿（点击后北飞） */
  const goose=new THREE.Group();
  const gw=new THREE.Mesh(new THREE.PlaneGeometry(1.8,0.5),
    new THREE.MeshBasicMaterial({color:0x2a2018,side:THREE.DoubleSide}));
  goose.add(gw); goose.position.set(0,6,-14); g.add(goose);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd890,
    transparent:true,opacity:0.25,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(3,3,1); g.add(glow);
  const burst=makeBurst({n:80,color:0xffd890,pos:[0,6,-14]}); g.add(burst.points);
  const dust=makeFlow({n:420,box:[150,16,100],pos:[0,8,-26],color:0xb08850,size:19,speed:4.5,maxA:0.28});
  g.add(dust.points);
  const mist=makeMist({n:6,spread:[190,18,100],pos:[0,8,-44],scale:66,color:0x9a7a4e,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x080504,seed:83,rim:0.14});
  rk.g.position.set(-12,-1.4,12); g.add(rk.g);
  addLights(g,{c:0xd8a860,i:0.46,p:[-50,56,-50]},{c:0x2c211a,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.fly=Math.min(1,ctl.fly+dt/2.8);
      ridge.update(t,0); dust.update(t); mist.update(t,k);
      poet.update(t,k); rider.update(t,k); burst.update(t); rk.update(t,k);
      /* 飞鸿北去（驮着口信） */
      goose.position.set(ctl.fly*0,6+ctl.fly*13,-14-ctl.fly*42);
      goose.rotation.y=0;
      const f=ctl.fly>0?Math.sin(t*8)*0.5:0;
      gw.rotation.z=f;
      glow.position.copy(goose.position);
      glow.material.opacity=k*(0.25*Math.min(1,ctl.fly*3))*(0.8+0.2*Math.sin(t*3.0));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.14); pluck(4,0.6,0.11);
        const fl=$('#flash'); fl.textContent='凭君传语报平安'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
