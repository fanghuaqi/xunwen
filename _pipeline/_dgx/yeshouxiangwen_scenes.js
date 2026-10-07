/* ================= 夜上受降城闻笛 · 二境场景（大漠金戈·霜月变体：沙似雪、芦管望乡） ================= */

/* 烽燧：夯土墩台 + 顶瞭望棚（合批 1 mesh） */
function makeBeacon(o){
  o=o||{};
  const h=o.h===undefined?10:o.h;
  const B=new GeoBag();
  const t1=new THREE.CylinderGeometry(h*0.16,h*0.24,h,8);
  t1.translate(0,h/2,0); B.put(t1,0x241a10);
  const hut=new THREE.BoxGeometry(h*0.34,h*0.16,h*0.28);
  hut.translate(0,h+h*0.08,0); B.put(hut,shadeColor(0x241a10,1.2));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a3020,emissive:0x060503}),{c:o.rimC===undefined?0xb08050:o.rimC,i:0.22,p:2.3}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 城垣：带雉堞的城墙（合批 1 mesh） */
function makeWallY(o){
  o=o||{};
  const w=o.w===undefined?46:o.w, h=o.h===undefined?6.5:o.h;
  const c=o.color===undefined?0x191210:o.color;
  const R=seedRnd(o.seed===undefined?7:o.seed);
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,4.0); body.translate(0,h/2,0); B.put(body,c);
  for(let i=0;i<Math.floor(w/2.4);i++){
    if(R()<0.85){
      const mer=new THREE.BoxGeometry(1.4,1.0,3.8);
      mer.translate(-w/2+1.2+i*2.4,h+0.5,0); B.put(mer,shadeColor(c,1.12));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a2018,emissive:0x050403}),{c:o.rimC===undefined?0xb08050:o.rimC,i:0.2,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

function bCover(){ // 封面 · 霜月大漠
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0b0c0e,c2:0x181a1e});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:41,color:0x101216,atmo:0x4a5058,fogK:0.74,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x0a0b0e,seed:5,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x9aa4b4,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xc0c8d4,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xaab6c8,i:0.4,p:[30,70,40]},{c:0x242830,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bShasixue(){ // 一（标志性瞬间）· 沙似雪 —— 月下白沙如雪，城外月如霜
  const g=new THREE.Group();
  /* 沙原（月下泛白）+ 远山 */
  const grd=makeGround({r:150,c1:0x16181c,c2:0x242830});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:20,layers:2,peaks:3,seed:535,color:0x101216,atmo:0x3c4450,fogK:0.60,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 受降城：横贯画面 */
  const wall=makeWallY({w:100,h:7,seed:91}); wall.g.position.set(0,0,-28); g.add(wall.g);
  const beacon=makeBeacon({h:11}); beacon.g.position.set(-22,0,-27); g.add(beacon.g);
  const beacon2=makeBeacon({h:9}); beacon2.g.position.set(26,0,-30); g.add(beacon2.g);
  /* 城头两甲士（剪影） */
  const f1=makeFigure({pose:'按剑',robe:0x1c1a16,belt:0x4a3c24,hat:'幞头',face:0,scale:1.15,rim:0.45,rimC:0xc8c4b4});
  f1.position.set(-8,7.05,-26.6); g.add(f1);
  const f2=makeFigure({pose:'独立',robe:0x1c1a16,hat:'发髻',face:-0.1,scale:1.05,rim:0.4,rimC:0xc8c4b4});
  f2.position.set(7,7.05,-26.8); g.add(f2);
  /* 大月高悬（如霜：冷银） */
  const motes=makeGlow({n:80,box:[200,24,110],pos:[0,11,-30],color:0xcdd4e0,size:7,speed:0.04,rise:0,maxA:0.4});
  g.add(motes.points);
  /* 沙原反月光斑 */
  const frost=makeGlow({n:90,box:[150,3,80],pos:[0,0.8,-16],color:0xdde4ee,size:6,speed:0.03,rise:0,maxA:0.3,add:false});
  g.add(frost.points);
  const mist=makeMist({n:7,spread:[230,20,120],pos:[0,8,-52],scale:74,color:0x9aa4b4,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x0b0c0f,seed:93,rim:0.14});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  addLights(g,{c:0xb8c4d8,i:0.55,p:[-60,110,-40]},{c:0x262c38,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0);
    motes.update(t); frost.update(t); mist.update(t,k);
    f1.update(t,k); f2.update(t,k);
    rk.update(t,k);
  }};
}
function bLuguan(){ // 二（末境·可点击）· 芦管望乡 —— 点击城头，芦管声起、征人尽望乡
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,look:0};
  const grd=makeGround({r:140,c1:0x14161a,c2:0x20242c});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:22,layers:2,peaks:3,seed:531,color:0x101216,atmo:0x404854,fogK:0.58,glowK:0.06});
  g.add(ridge.g);
  /* 城墙 + 城头六甲士（点击后次第回首望月） */
  const wall=makeWallY({w:92,h:6.5,seed:95}); wall.g.position.set(0,0,-26); g.add(wall.g);
  const beacon=makeBeacon({h:10}); beacon.g.position.set(-20,0,-25); g.add(beacon.g);
  const figs=[];
  for(let i=0;i<6;i++){
    const f=makeFigure({pose:i%2?'独立':'按剑',robe:0x1c1a16,belt:0x4a3c24,hat:i%2?'发髻':'幞头',
      face:0,scale:1.12,rim:0.42,rimC:0xc8c4b4});
    f.position.set(-15+i*6,6.55,-25.4); f.rotation.y=Math.PI;   // 背对镜头面向城外
    g.add(f); figs.push(f);
  }
  /* 芦管声弧（点击后自暗处一圈圈扩散） */
  const arcs=[];
  for(let i=0;i<4;i++){
    const pts=[];
    for(let k2=0;k2<=22;k2++){
      const a=-1.2+k2/22*2.4, r=2.5+i*3.5;
      pts.push(new THREE.Vector3(18+Math.sin(a)*r,7.5+Math.cos(a)*r*0.55,-20+Math.cos(a)*r));
    }
    const ln=new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),
      new THREE.LineBasicMaterial({color:0xc8b488,transparent:true,opacity:0.5,fog:false}));
    ln.renderOrder=2; g.add(ln); arcs.push(ln);
  }
  const motes=makeGlow({n:70,box:[180,22,100],pos:[0,10,-28],color:0xcdd4e0,size:6,speed:0.04,rise:0,maxA:0.35});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,20,120],pos:[0,8,-48],scale:72,color:0x9aa4b4,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x0b0c0f,seed:97,rim:0.14});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  addLights(g,{c:0xb8c4d8,i:0.5,p:[-60,100,-40]},{c:0x262c38,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.look=Math.min(1,ctl.look+dt/2.6);
      motes.update(t); mist.update(t,k); rk.update(t,k);
      /* 征人次第回首（望月=转向镜头方向仰头） */
      figs.forEach(function(f,i){
        const thr=i/6;
        const on=sstep(thr,thr+0.3,ctl.look);
        f.rotation.y=Math.PI-on*2.4;
        f.rotation.z=on*0.06;
        f.update(t,k);
      });
      for(let i=0;i<arcs.length;i++){
        const ln=arcs[i];
        const ph=((t*0.3)+i/arcs.length)%1;
        ln.material.opacity=k*(0.42*Math.sin(ph*Math.PI)*(1-ph*0.5))*Math.min(1,ctl.look*2);
        ln.scale.setScalar(0.55+ph*0.8);
      }
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.1,0.12); pluck(2,0.8,0.1); pluck(3,1.5,0.1);
        const fl=$('#flash'); fl.textContent='一夜征人尽望乡'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
