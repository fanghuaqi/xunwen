/* ================= 饮酒·其五 · 四境场景（宣纸留白·菊隐变体：心远地偏、采菊东篱、日夕鸟还、真意忘言） ================= */

/* 草庐：夯土墙 + 茅草顶 + 亮窗（合批 1 mesh） */
function makeHut(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(4.6,2.6,3.6); body.translate(0,1.3,0); B.put(body,0xcfc4a8);
  const roof=new THREE.ConeGeometry(4.1,1.9,4); roof.rotateY(Math.PI/4);
  roof.translate(0,3.5,0); B.put(roof,0x8a7a58);
  const win=new THREE.BoxGeometry(0.9,0.9,0.08); win.translate(-1.2,1.5,1.82); B.put(win,0x6a5a3a);
  const door=new THREE.BoxGeometry(0.85,1.7,0.08); door.translate(0.9,0.85,1.82); B.put(door,0x5a4a34);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a3830,emissive:0x0c0b08}),{c:o.rimC===undefined?0x8a8474:o.rimC,i:0.2,p:2.2}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return g;
}

/* 菊丛：篱边一丛黄菊（茎+花团，合批 1 mesh） */
function makeChrys(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?53:o.seed);
  const B=new GeoBag();
  const n=o.n===undefined?7:o.n;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*1.6, z=(R()-0.5)*0.9;
    const st=new THREE.CylinderGeometry(0.03,0.045,0.7+R()*0.5,5);
    st.translate(x,0.35+R()*0.2,z); B.put(st,0x4a5a34);
    const fl=new THREE.SphereGeometry(0.16+R()*0.1,7,5);
    fl.translate(x,0.75+R()*0.4,z); B.put(fl,0xd8b83a);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a4a30,emissive:0x0d0c06}),{c:0xb8a060,i:0.24,p:2.4}));
  const g=new THREE.Group(); mesh.frustumCulled=false; g.add(mesh);
  g.userData.ph=R()*6.283;
  return g;
}

/* 东篱：竹篱一段（细竹竿排开，合批 1 mesh） */
function makeFence(o){
  o=o||{};
  const w=o.w===undefined?9:o.w, R=seedRnd(o.seed===undefined?59:o.seed);
  const B=new GeoBag();
  for(let i=0;i<=Math.floor(w/0.55);i++){
    const x=-w/2+i*0.55, h=1.5+R()*0.35;
    const st=new THREE.CylinderGeometry(0.05,0.06,h,5);
    st.translate(x,h/2,0); B.put(st,0x6a5a3a);
  }
  const rail1=new THREE.CylinderGeometry(0.04,0.04,w,5);
  rail1.rotateZ(Math.PI/2); rail1.translate(0,1.05,0); B.put(rail1,0x6a5a3a);
  const rail2=rail1.clone(); rail2.translate(0,0.45,0); B.put(rail2,0x6a5a3a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a4030,emissive:0x0b0a07}),{c:0x8a8474,i:0.2,p:2.3}));
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 宣纸南山
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0xe6dfcc,c2:0xd8d0ba});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:170,h:44,layers:3,peaks:4,seed:41,color:0x2c2f33,atmo:0xb8b2a0,fogK:0.72,glowK:0.05,y:-8});
  ridge.g.position.set(0,0,60); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x23262a,seed:5,rim:0.12,rimC:0xd8d2c2});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xe0d8c2,op:0.14});
  g.add(mist.g);
  const motes=makeGlow({n:50,box:[220,36,130],pos:[0,8,-40],color:0xb8ae94,size:7,speed:0.05,rise:0,maxA:0.3,add:false});
  g.add(motes.points);
  addLights(g,{c:0xfff4e0,i:0.55,p:[30,70,40]},{c:0xcfc8b4,i:0.7});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bXinyuan(){ // 一 · 心远地偏 —— 人境结庐，远处车马成尘（浅色留白）
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0xe2dbc6,c2:0xd4ccb4});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 远景：淡墨远山（"偏"） */
  const ridge=makeRange({r:200,h:38,layers:3,peaks:4,seed:381,color:0x33363a,atmo:0xc2bca8,fogK:0.66,glowK:0.04});
  g.add(ridge.g);
  /* 中景：草庐一栋 */
  const hut=makeHut({scale:1.15}); hut.position.set(0,0,-6); g.add(hut);
  /* 远处车马喧：大路上走动的车与人影（以"喧"衬"静"） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(3,0.06,70),
    new THREE.MeshPhongMaterial({color:0xb8ae94,shininess:4}));
  road.rotation.y=-0.35; road.position.set(26,0.02,-24); g.add(road);
  const walkers=makeCrowd({n:8,rect:[10,-40,26,30],seed:391,color:0x3a3c40,rimC:0xd8d2c2,rim:0.16,sMin:0.75,sMax:1.0});
  g.add(walkers.mesh);
  const cart=new THREE.Group();
  const cbody=new THREE.Mesh(new THREE.BoxGeometry(2.2,0.9,1.4),
    new THREE.MeshPhongMaterial({color:0x4a4438,shininess:6}));
  cbody.position.y=1.0; cart.add(cbody);
  [-0.8,0.8].forEach(function(x){
    const wh=new THREE.Mesh(new THREE.TorusGeometry(0.55,0.1,6,14),
      new THREE.MeshPhongMaterial({color:0x3a342a}));
    wh.position.set(x,0.55,0.8); cart.add(wh);
  });
  cart.position.set(20,0,-18); cart.rotation.y=-0.4; g.add(cart);
  /* 庐前一点静：石+小树 */
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:7,color:0x23262a,seed:63,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  const tree=makeForeground({kind:'坡石',n:1,r:2.2,w:8,d:4,color:0x2c2f33,seed:65,rim:0.1,rimC:0xd8d2c2});
  tree.g.position.set(10,-1.0,8); g.add(tree.g);
  const mist=makeMist({n:7,spread:[200,22,110],pos:[0,8,-40],scale:70,color:0xd8d0ba,op:0.12});
  g.add(mist.g);
  addLights(g,{c:0xfff4e0,i:0.55,p:[30,70,30]},{c:0xcfc8b4,i:0.7});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); walkers.update(t); mist.update(t,k);
    cart.rotation.z=Math.sin(t*0.8)*0.015;
    rk.update(t,k); tree.update(t,k);
  }};
}
function bCaiju(){ // 二（标志性瞬间）· 采菊东篱 —— 东篱采菊，悠然见南山
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0xe6dfcc,c2:0xd6ceb8});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 南山：画面主体（淡墨大屏） */
  const ridge=makeRange({r:200,h:52,layers:3,peaks:5,seed:401,color:0x2c2f33,atmo:0xc2bca8,fogK:0.64,glowK:0.05});
  ridge.g.position.set(0,0,-58); g.add(ridge.g);
  /* 东篱 + 菊丛 + 采菊人（俯身） */
  const fence=makeFence({w:11,seed:59}); fence.position.set(-1,0,-3.2); g.add(fence);
  const chrys=makeChrys({seed:53}); chrys.position.set(1.2,0,-2.4); g.add(chrys);
  const chrys2=makeChrys({seed:57,n:5}); chrys2.position.set(3.4,0,-3.6); g.add(chrys2);
  const poet=makeFigure({pose:'独立',robe:0x4a4438,belt:0x6a5a3a,hat:'发髻',face:0.4,scale:1.25,rim:0.2,rimC:0xd8d2c2});
  poet.position.set(-1.4,0,-1.2); g.add(poet);
  /* 一只蝶绕菊（悠然生气） */
  const bf=new THREE.Group();
  const bw=new THREE.Mesh(new THREE.PlaneGeometry(0.5,0.3),
    new THREE.MeshBasicMaterial({color:0xd8b83a,side:THREE.DoubleSide}));
  bw.rotation.z=0.4; bf.add(bw); g.add(bf);
  const mist=makeMist({n:6,spread:[180,20,100],pos:[0,8,-40],scale:66,color:0xe0d8c2,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:67,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xfff4e0,i:0.6,p:[-30,60,30]},{c:0xcfc8b4,i:0.72});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    poet.update(t,k);
    chrys.rotation.z=Math.sin(t*1.1+chrys.userData.ph)*0.02;
    chrys2.rotation.z=Math.sin(t*0.9)*0.02;
    bf.position.set(1.2+Math.sin(t*0.7)*0.8,1.1+Math.sin(t*1.1)*0.3,-2.0+Math.cos(t*0.5)*0.5);
    rk.update(t,k);
  }};
}
function bRihuan(){ // 三 · 日夕鸟还 —— 暮霭山气佳，飞鸟相与还
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0xdcd4be,c2:0xc8c0a8});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 南山暮霭（远山+暖暮天光渐染） */
  const ridge=makeRange({r:210,h:50,layers:3,peaks:5,seed:411,color:0x33363a,atmo:0xd8c8a8,fogK:0.62,glowK:0.05});
  g.add(ridge.g);
  /* 山气：暮霭流岚（贴山雾流） */
  const haze=makeFlow({n:380,box:[170,16,100],pos:[0,14,-52],color:0xe8dcc0,size:20,speed:2.2,maxA:0.22,add:false});
  g.add(haze.points);
  /* 飞鸟相与还：成对归鸟掠向山坳 */
  const birds=[];
  const bmat=new THREE.MeshBasicMaterial({color:0x2c2f33,side:THREE.DoubleSide});
  for(let i=0;i<6;i++){
    const b=new THREE.Group();
    const w1=new THREE.Mesh(new THREE.PlaneGeometry(1.6,0.5),bmat); w1.position.x=-0.7;
    const w2=new THREE.Mesh(new THREE.PlaneGeometry(1.6,0.5),bmat); w2.position.x=0.7;
    b.add(w1,w2); g.add(b);
    birds.push({b,w1,w2,ph:i*1.1,r:rnd(40,80),y:rnd(14,24),sp:rnd(0.05,0.09)});
  }
  const mist=makeMist({n:6,spread:[190,20,100],pos:[0,8,-38],scale:66,color:0xdccdb0,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:69,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xffe8c0,i:0.55,p:[40,50,20]},{c:0xc4bca6,i:0.72});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); haze.update(t); mist.update(t,k); rk.update(t,k);
    for(const o of birds){
      const a=o.ph+t*o.sp;
      o.b.position.set(Math.cos(a)*o.r-10,o.y+Math.sin(t*0.8+o.ph)*1.2,-40+Math.sin(a)*o.r*0.6);
      o.b.rotation.y=-a;
      const f=Math.sin(t*7+o.ph*3)*0.5;
      o.w1.rotation.z=f; o.w2.rotation.z=-f;
    }
  }};
}
function bZhenyi(){ // 四（末境·可点击）· 真意忘言 —— 暮色四合，点击庐中灯起，真意不必言
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,lamp:0};
  const grd=makeGround({r:120,c1:0xd8d0ba,c2:0xc4bca4});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:48,layers:3,peaks:5,seed:421,color:0x2c2f33,atmo:0xc8b898,fogK:0.62,glowK:0.04});
  g.add(ridge.g);
  /* 草庐（窗暗待点） */
  const hut=makeHut({scale:1.2}); hut.position.set(0,0,-4); hut.rotation.y=0.25; g.add(hut);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffcf70,
    transparent:true,opacity:0.78,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(4,4,1); lamp.position.set(1.1,1.6,-2.6); g.add(lamp);
  const pl=new THREE.PointLight(0xffcf70,2.0,34); pl.position.set(1.1,2,-2); g.add(pl);
  /* 篱菊剪影 */
  const fence=makeFence({w:9,seed:73}); fence.position.set(-4,0,-2.4); fence.rotation.y=0.5; g.add(fence);
  const chrys=makeChrys({seed:71,n:6}); chrys.position.set(-2.6,0,-1.6); g.add(chrys);
  /* 归鸟三点入暮 */
  const bmat=new THREE.MeshBasicMaterial({color:0x2c2f33,side:THREE.DoubleSide,transparent:true,opacity:0.85});
  const birds=[];
  for(let i=0;i<3;i++){
    const b=new THREE.Group();
    const w1=new THREE.Mesh(new THREE.PlaneGeometry(1.4,0.44),bmat); w1.position.x=-0.6;
    const w2=new THREE.Mesh(new THREE.PlaneGeometry(1.4,0.44),bmat); w2.position.x=0.6;
    b.add(w1,w2); g.add(b); birds.push({b,w1,w2,ph:i*2.0});
  }
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-40],scale:70,color:0xd8ccb0,op:0.12});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:79,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xffe0b0,i:0.4,p:[30,50,20]},{c:0xbfb8a2,i:0.75});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.lamp=Math.min(1,ctl.lamp+dt/2.0);
      ridge.update(t,0); mist.update(t,k); rk.update(t,k);
      lamp.material.opacity=k*0.78*(0.45+ctl.lamp*0.52*(0.82+0.18*Math.sin(t*5.0)));
      pl.intensity=k*2.0*(0.10+ctl.lamp*0.88*(0.85+0.15*Math.sin(t*4.2)));
      for(const o of birds){
        const x=-30+((t*2.2+o.ph*10)%70);
        o.b.position.set(x,16+Math.sin(t*0.6+o.ph)*1.5,-46);
        const f=Math.sin(t*6+o.ph)*0.45;
        o.w1.rotation.z=f; o.w2.rotation.z=-f;
      }
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.1,0.13); pluck(4,0.6,0.11);
        const fl=$('#flash'); fl.textContent='欲辨已忘言'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
