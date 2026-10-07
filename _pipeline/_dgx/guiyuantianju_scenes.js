/* ================= 归园田居·其三 · 四境场景（青绿春晓·月归变体：种豆南山、带月荷锄、夕露沾衣、愿无违） ================= */

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


/* 锄头：木柄 + 锄板（可挂人物手侧） */
function makeHoe(){
  const B=new GeoBag();
  const shaft=new THREE.CylinderGeometry(0.045,0.055,4.6,6);
  shaft.rotateZ(0.42); B.put(shaft,0x4a3a22);
  const blade=new THREE.BoxGeometry(0.75,0.5,0.09);
  blade.rotateZ(0.42); blade.translate(-1.9,-1.75,0); B.put(blade,0x5a5a60);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a4438,emissive:0x070706}),{c:0x9fc8a8,i:0.26,p:2.4}));
  return mesh;
}

/* 豆苗畦：一垄垄豆苗（小双叶，InstancedMesh） */
function makeBeanRows(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?431:o.seed);
  const rows=o.rows===undefined?6:o.rows, per=o.per===undefined?9:o.per;
  const geo=new THREE.SphereGeometry(0.16,6,4); geo.scale(1,0.8,1);
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,shininess:14,specular:0x3a5a44,
    emissive:0x08140c}),{c:0xa8d8b0,i:0.3,p:2.5});
  const inst=new THREE.InstancedMesh(geo,mat,rows*per);
  const dm=new THREE.Object3D(); let n=0;
  for(let r=0;r<rows;r++){
    for(let c=0;c<per;c++){
      const x=-9+r*3.4+(R()-0.5)*0.7, z=-7+c*1.9+(R()-0.5)*0.7;
      dm.position.set(x,0.12,z); dm.scale.setScalar(0.7+R()*0.7);
      dm.updateMatrix(); inst.setMatrixAt(n++,dm.matrix);
    }
  }
  inst.instanceMatrix.needsUpdate=true; inst.frustumCulled=false;
  const g=new THREE.Group(); g.add(inst);
  return g;
}

/* 草丛簇：茂盛的深草（合批 1 mesh） */
function makeWeeds(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?433:o.seed);
  const B=new GeoBag();
  const n=o.n===undefined?40:o.n;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*(o.w===undefined?36:o.w), z=(R()-0.5)*(o.d===undefined?20:o.d);
    const h=0.8+R()*1.5;
    const bl=new THREE.ConeGeometry(0.14,h,4);
    bl.translate(x,h/2,z); B.put(bl,0x223618);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c4430,emissive:0x060d08}),{c:0x9fc8a8,i:0.24,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 月下南山
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x081009,c2:0x14231a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:160,h:40,layers:2,peaks:4,seed:41,color:0x0a120c,atmo:0x2c4434,fogK:0.74,glowK:0.10,y:-12});
  ridge.g.position.set(0,0,50); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x050a06,seed:5,rim:0.16});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fb89a,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xbfe0c0,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xa8ccb0,i:0.42,p:[30,70,40]},{c:0x1e2c22,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bZhongdou(){ // 一 · 种豆南山 —— 南山坡地豆田，草盛苗稀
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a110c,c2:0x18241a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:44,layers:3,peaks:5,seed:441,color:0x0b130d,atmo:0x2e4836,fogK:0.62,glowK:0.09});
  ridge.g.position.set(0,0,-52); g.add(ridge.g);
  /* 豆田：垄上的豆苗（稀）与草丛（盛） */
  const rows=makeBeanRows({seed:443,rows:6,per:9}); rows.position.set(0,0,-8); g.add(rows);
  const weeds=makeWeeds({seed:445,n:46,w:30,d:16}); weeds.position.set(0,0,-8); g.add(weeds);
  /* 竹篱与农舍一角 */
  const fence=makeFence({w:10,seed:447}); fence.position.set(-10,0,-2); fence.rotation.y=0.3; g.add(fence);
  const hut=makeHut({scale:1.0}); hut.position.set(-14,0,-14); hut.rotation.y=0.4; g.add(hut);
  const mist=makeMist({n:7,spread:[200,22,110],pos:[0,9,-42],scale:70,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x060a07,seed:91,rim:0.15});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  addLights(g,{c:0xa8ccb0,i:0.46,p:[40,80,-30]},{c:0x1e2c22,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); rk.update(t,k);
  }};
}
function bHeyue(){ // 二（标志性瞬间）· 带月荷锄归 —— 月下荷锄独行剪影
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x081009,c2:0x121c14});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:42,layers:3,peaks:5,seed:451,color:0x0a120c,atmo:0x2c4434,fogK:0.60,glowK:0.08});
  ridge.g.position.set(0,0,-56); g.add(ridge.g);
  /* 大月：银月高悬 */
  const motes=makeGlow({n:80,box:[160,26,100],pos:[0,12,-30],color:0xcfe0d0,size:7,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  /* 田埂小径 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.7,0.07,58),
    new THREE.MeshPhongMaterial({color:0x1a2620,shininess:8,specular:0x36443a}));
  path.rotation.y=0.18; path.position.set(2,0.03,-16); g.add(path);
  /* 主体：荷锄夜归人（背影，锄在肩） */
  const farmer=makeFigure({pose:'独立',robe:0x2c3428,belt:0x6a5a34,hat:'发髻',face:0.15,scale:1.35,rim:0.55,rimC:0xc8d8b0});
  farmer.position.set(1.2,0,6); g.add(farmer);
  const hoe=makeHoe(); hoe.position.set(2.6,2.6,5.6); hoe.rotation.y=-0.5; g.add(hoe);
  /* 两岸豆田延向月下 */
  const rows=makeBeanRows({seed:453,rows:5,per:8}); rows.position.set(-6,0,-16); g.add(rows);
  const weeds=makeWeeds({seed:455,n:36,w:26,d:20}); weeds.position.set(8,0,-18); g.add(weeds);
  const mist=makeMist({n:8,spread:[220,22,120],pos:[0,9,-44],scale:74,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x060a07,seed:93,rim:0.15});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  addLights(g,{c:0xb8cce0,i:0.5,p:[-40,100,-40]},{c:0x20302a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); motes.update(t); mist.update(t,k);
    farmer.update(t,k);
    hoe.rotation.z=Math.sin(t*0.8)*0.02;
    rk.update(t,k);
  }};
}
function bXilv(){ // 三 · 夕露沾衣 —— 道狭草木长，夕露沾衣
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x091009,c2:0x141f16});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:38,layers:2,peaks:4,seed:461,color:0x0a120c,atmo:0x2a4030,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 狭道：两侧草木夹一条小径 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.6,0.07,52),
    new THREE.MeshPhongMaterial({color:0x1a241e,shininess:8,specular:0x36443a}));
  path.position.set(0,0.03,-14); g.add(path);
  const weedsL=makeWeeds({seed:463,n:40,w:14,d:40}); weedsL.position.set(-4,0,-14); g.add(weedsL);
  const weedsR=makeWeeds({seed:465,n:40,w:14,d:40}); weedsR.position.set(4,0,-14); g.add(weedsR);
  /* 夕露：草梢凝亮的露珠（小亮点，点缀性） */
  const dew=makeGlow({n:110,box:[16,3.2,42],pos:[0,1.2,-12],color:0xd8ecf0,size:3.4,speed:0.02,rise:0,maxA:0.5});
  g.add(dew.points);
  /* 走在小径上的人（正面远来） */
  const farmer=makeFigure({pose:'独立',robe:0x2c3428,hat:'发髻',face:-0.2,scale:1.2,rim:0.5,rimC:0xc8d8b0});
  farmer.position.set(0,0,2); g.add(farmer);
  const mist=makeMist({n:6,spread:[160,18,90],pos:[0,7,-32],scale:62,color:0x7fa890,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:16,d:6,color:0x060a07,seed:95,rim:0.14});
  rk.g.position.set(-12,-1.3,11); g.add(rk.g);
  addLights(g,{c:0xa8ccb0,i:0.44,p:[-40,80,-30]},{c:0x1e2c22,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); dew.update(t); mist.update(t,k);
    farmer.update(t,k); rk.update(t,k);
  }};
}
function bYuanwuwei(){ // 四（末境·可点击）· 愿无违 —— 点击月下豆田，苗影摇曳露更亮
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,glow:0};
  const grd=makeGround({r:120,c1:0x081009,c2:0x121c14});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:44,layers:3,peaks:5,seed:471,color:0x0a120c,atmo:0x2c4434,fogK:0.60,glowK:0.08});
  ridge.g.position.set(0,0,-54); g.add(ridge.g);
  const rows=makeBeanRows({seed:473,rows:6,per:10}); rows.position.set(0,0,-6); g.add(rows);
  const weeds=makeWeeds({seed:475,n:34,w:26,d:14}); weeds.position.set(-2,0,-6); g.add(weeds);
  /* 露光与豆影（点击后凝亮） */
  const dew=makeGlow({n:130,box:[30,3,36],pos:[0,1.0,-5],color:0xd8ecf0,size:3.6,speed:0.02,rise:0,maxA:0});
  g.add(dew.points);
  const burst=makeBurst({n:80,color:0xd8ecf0,pos:[0,2.5,-4]}); g.add(burst.points);
  const farmer=makeFigure({pose:'独立',robe:0x2c3428,belt:0x6a5a34,hat:'发髻',face:0.3,scale:1.28,rim:0.5,rimC:0xc8d8b0});
  farmer.position.set(-3,0,2); g.add(farmer);
  const hoe=makeHoe(); hoe.position.set(-1.8,2.5,1.7); hoe.rotation.y=0.6; g.add(hoe);
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-40],scale:70,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x060a07,seed:97,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xa8ccb0,i:0.46,p:[-40,90,-40]},{c:0x1e2c22,i:0.62});
  const pl=new THREE.PointLight(0xcfe0d0,1.2,40); pl.position.set(0,4,-4); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.glow=Math.min(1,ctl.glow+dt/2.4);
      ridge.update(t,0); mist.update(t,k); rk.update(t,k); burst.update(t);
      dew.mat.uniforms.uMaxA.value=k*0.5*ctl.glow;
      dew.update(t);
      pl.intensity=k*1.2*(0.5+ctl.glow*0.45*(0.85+0.15*Math.sin(t*2.4)));
      farmer.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.13); pluck(4,0.6,0.11);
        const fl=$('#flash'); fl.textContent='但使愿无违'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
