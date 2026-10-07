/* ================= 次北固山下 · 四境场景（青绿春晓·江行变体：客路行舟、潮平帆悬、海日残夜、归雁乡书） ================= */

/* 江行帆船：船体 + 高桅 + 方头布帆（"风正一帆悬"） */
function makeJunkBoat(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const hullC=o.hull===undefined?0x241708:o.hull, sailC=o.sail===undefined?0xd8ccb0:o.sail;
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.8,0.45,5.0,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.5,1.5); B.put(hull,hullC);
  const bow=new THREE.ConeGeometry(0.6,1.5,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.7,1.4); bow.translate(3.1,0.05,0); B.put(bow,hullC);
  const deck=new THREE.BoxGeometry(3.8,0.12,1.3); deck.translate(0,0.55,0); B.put(deck,shadeColor(hullC,1.4));
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a3a22,emissive:0x0a0703}),{c:o.rimC===undefined?0xa8c890:o.rimC,i:0.3,p:2.5})));
  const mast=new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.09,7.0,6),
    new THREE.MeshPhongMaterial({color:0x2e2012}));
  mast.position.set(0,3.6,0); g.add(mast);
  const yard=new THREE.Mesh(new THREE.CylinderGeometry(0.04,0.04,3.2,5),
    new THREE.MeshPhongMaterial({color:0x2e2012}));
  yard.rotation.z=Math.PI/2; yard.position.set(0,6.8,0); g.add(yard);
  const sailGeo=new THREE.PlaneGeometry(2.8,5.6,1,4);
  (function(){
    const p=sailGeo.attributes.position;
    for(let i=0;i<p.count;i++){ const y=p.getY(i); if(y>1.2)p.setX(i,p.getX(i)*0.6); }
    sailGeo.computeVertexNormals();
  })();
  const sail=new THREE.Mesh(sailGeo,new THREE.MeshPhongMaterial({color:sailC,side:THREE.DoubleSide,
    shininess:6,specular:0x8a9a76,emissive:0x1c2018}));
  sail.position.set(0,3.8,0.02); g.add(sail);
  g.userData.sail=sail;
  g.scale.setScalar(s);
  return g;
}

/* 雁阵：人字排开的雁（身+双翅扑动） */
function makeGeese(o){
  o=o||{};
  const n=o.n===undefined?7:o.n;
  const g=new THREE.Group(), items=[];
  const bmat=new THREE.MeshPhongMaterial({color:o.color===undefined?0x2a2f28:o.color,
    side:THREE.DoubleSide,shininess:10,specular:0x36443a,emissive:0x050806});
  for(let i=0;i<n;i++){
    const b=new THREE.Group();
    const body=new THREE.SphereGeometry(0.42,7,5); body.scale(1.9,0.8,0.9); b.add(body);
    const neck=new THREE.CylinderGeometry(0.09,0.13,0.7,5); neck.rotateZ(1.1); neck.translate(0.85,0.28,0); b.add(neck);
    const head=new THREE.SphereGeometry(0.2,6,5); head.translate(1.2,0.55,0); b.add(head);
    const wgeo=new THREE.PlaneGeometry(1.9,0.55); wgeo.rotateY(Math.PI/2);
    const w1=new THREE.Mesh(wgeo,bmat); w1.position.x=-0.1;
    const w2=new THREE.Mesh(wgeo,bmat); w2.position.x=-0.1;
    b.add(w1,w2);
    /* 人字队形：i=0 头雁，其后左右两列 */
    const k=(i+1)>>1, side=i===0?0:(i%2?1:-1);
    const off=new THREE.Vector3(-k*3.4, k*0.5, side*k*2.6);
    g.add(b);
    items.push({b,w1,w2,off,ph:i*0.7});
  }
  g.userData.items=items;
  return g;
}

function bCover(){ // 封面 · 青绿江天
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x081009,c2:0x14231a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:34,layers:2,peaks:4,seed:41,color:0x0a120c,atmo:0x2c4434,fogK:0.74,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x050a06,seed:5,rim:0.16});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fb89a,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:70,box:[220,40,130],pos:[0,10,-40],color:0xbfe0c0,size:8,speed:0.05,rise:0,maxA:0.45});
  g.add(motes.points);
  addLights(g,{c:0xa8ccb0,i:0.42,p:[30,70,40]},{c:0x1e2c22,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bKelv(){ // 一 · 客路行舟 —— 青山绿水间一叶行舟
  const g=new THREE.Group();
  const ridge=makeRange({r:200,h:46,layers:3,peaks:5,seed:311,color:0x0b130d,atmo:0x2e4836,fogK:0.62,glowK:0.09});
  ridge.g.position.set(0,0,-46); g.add(ridge.g);
  const water=makeWater({size:520,seg:90,amp:0.4,freq:0.1,speed:0.7,flow:[0.9,0.15],spec:1.2,
    deep:0x0a1c22,shallow:0x16404a,skyc:0x245048,moonDir:[60,100,-150]});
  g.add(water.mesh);
  /* 主体：行舟（客路尽头的船） */
  const boat=makeJunkBoat({scale:1.1});
  boat.position.set(0,0.2,-2); boat.rotation.y=0.2; g.add(boat);
  /* 近岸青山夹江（左右两片近山） */
  const cliffL=makeRange({r:150,h:30,layers:1,peaks:3,seed:313,arc:Math.PI*0.24,a0:Math.PI*0.60,
    color:0x0c140e,atmo:0x2e4836,fogK:0.66,glowK:0.09,y:-16});
  cliffL.g.position.set(-30,0,6); g.add(cliffL.g);
  const cliffR=makeRange({r:150,h:26,layers:1,peaks:3,seed:317,arc:Math.PI*0.22,a0:-Math.PI*0.40,
    color:0x0c140e,atmo:0x2e4836,fogK:0.66,glowK:0.09,y:-16});
  cliffR.g.position.set(30,0,6); g.add(cliffR.g);
  /* 岸边客路（远处一条淡路绕山） */
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.4,0.06,44),
    new THREE.MeshPhongMaterial({color:0x243428,shininess:6}));
  path.rotation.y=0.5; path.position.set(-20,0.03,-28); g.add(path);
  const mist=makeMist({n:8,spread:[230,24,120],pos:[0,9,-40],scale:72,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x060a07,seed:57,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x050a06,seed:59,sway:0.9});
  reeds.g.position.set(13,-1.3,11); g.add(reeds.g);
  addLights(g,{c:0xa8ccb0,i:0.46,p:[40,80,-30]},{c:0x1e2c22,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); cliffL.update(t,0); cliffR.update(t,0); water.update(t); mist.update(t,k);
    boat.rotation.z=Math.sin(t*0.7)*0.02;
    boat.position.y=0.2+Math.sin(t*0.8)*0.08;
    rk.update(t,k); reeds.update(t,k);
  }};
}
function bChaoping(){ // 二 · 潮平帆悬 —— 江面开阔，一帆高悬
  const g=new THREE.Group();
  const ridge=makeRange({r:240,h:24,layers:2,peaks:3,seed:321,color:0x0a120c,atmo:0x28402e,fogK:0.62,glowK:0.07,y:-18});
  g.add(ridge.g);
  const water=makeWater({size:700,seg:100,amp:0.3,freq:0.09,speed:0.55,flow:[0.7,0.2],spec:1.4,
    deep:0x0a1c22,shallow:0x18464e,skyc:0x275448,moonDir:[-60,110,-160]});
  g.add(water.mesh);
  /* 主体：高悬之帆（占画面竖线，以小景衬大景） */
  const boat=makeJunkBoat({scale:1.5,sail:0xe4dcc4});
  boat.position.set(0,0.3,-8); g.add(boat);
  /* 平潮：两岸远退，水天一色 */
  const dikeL=new THREE.Mesh(new THREE.BoxGeometry(3,0.8,90),
    new THREE.MeshPhongMaterial({color:0x142018,shininess:6}));
  dikeL.rotation.y=Math.PI/2; dikeL.position.set(-46,0.2,-26); g.add(dikeL);
  const dikeR=dikeL.clone(); dikeR.position.x=46; g.add(dikeR);
  const motes=makeGlow({n:80,box:[140,16,90],pos:[0,7,-20],color:0xbfe0c0,size:7,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,20,130],pos:[0,8,-52],scale:76,color:0x7fa890,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x060a07,seed:61,rim:0.15});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  addLights(g,{c:0xa8ccb0,i:0.5,p:[-40,90,-40]},{c:0x1e2c22,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    const sail=boat.userData.sail;
    sail.rotation.y=Math.sin(t*1.3)*0.03;              // 风正：帆稳
    boat.rotation.z=Math.sin(t*0.6)*0.015;
    boat.position.y=0.3+Math.sin(t*0.7)*0.06;
    rk.update(t,k);
  }};
}
function bHairi(){ // 三（标志性瞬间）· 海日残夜 —— 残夜未尽海日已生，旧年里江春已入
  const g=new THREE.Group();
  /* 远山（背景层）+ 大江开阔 + 远处海平线 */
  const ridge=makeRange({r:230,h:26,layers:2,peaks:3,seed:327,color:0x0a120e,atmo:0x30423a,fogK:0.62,glowK:0.06,y:-18});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const water=makeWater({size:800,seg:100,amp:0.5,freq:0.08,speed:0.7,flow:[0.6,0.4],spec:1.5,
    deep:0x0a1a20,shallow:0x184046,skyc:0x2a4c50,moonDir:[70,90,-170]});
  g.add(water.mesh);
  /* 东方海平线：一轮海日自残夜里升起 */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(9,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xffb860,transparent:true,opacity:0.95,fog:false}));
  sun.position.set(34,17,-118); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
    transparent:true,opacity:0.5,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(80,80,1); sunGlow.position.set(34,17,-118); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 西天残夜：残月与疏星仍挂（东西同框=时序交替） */
  const mistDawn=makeMist({n:9,spread:[280,20,140],pos:[0,40,-90],scale:100,color:0x2c3a3e,op:0.30});
  g.add(mistDawn.g);
  /* 早春信息：岸边一树新柳（嫩绿） */
  const willow=new THREE.Group();
  const trunk=new THREE.Mesh(new THREE.CylinderGeometry(0.14,0.22,3.6,7),
    new THREE.MeshPhongMaterial({color:0x1a1410}));
  trunk.position.set(14,1.8,-16); willow.add(trunk);
  const crown=new THREE.Mesh(new THREE.SphereGeometry(2.2,9,7),
    new THREE.MeshPhongMaterial({color:0x3a6a38,shininess:12,emissive:0x0c1c0a}));
  crown.scale.set(1.2,0.85,1.2); crown.position.set(14,4.2,-16); willow.add(crown);
  g.add(willow);
  /* 日光染金江面（贴水金光带） */
  const gold=makeGlow({n:120,box:[90,3,60],pos:[16,1.5,-58],color:0xffc870,size:8,speed:0.06,rise:0,maxA:0.4});
  g.add(gold.points);
  const motes=makeGlow({n:60,box:[120,14,70],pos:[0,7,-24],color:0xcfe0c8,size:6,speed:0.05,rise:0,maxA:0.35});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,20,120],pos:[0,8,-50],scale:74,color:0x7f98a8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.8,w:20,d:7,color:0x060a08,seed:63,rim:0.15});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  addLights(g,{c:0xd8a870,i:0.55,p:[50,60,-60]},{c:0x233030,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mistDawn.update(t,k); gold.update(t); motes.update(t); mist.update(t,k);
    sunGlow.material.opacity=k*(0.40+0.08*Math.sin(t*0.8));
    rk.update(t,k);
  }};
}
function bGuiyan(){ // 四（末境·可点击）· 归雁乡书 —— 点击雁阵起飞，人字驮乡书飞向洛阳
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,fly:0};
  const ridge=makeRange({r:220,h:36,layers:2,peaks:4,seed:331,color:0x0a120c,atmo:0x2c4434,fogK:0.60,glowK:0.08});
  g.add(ridge.g);
  const water=makeWater({size:560,seg:90,amp:0.35,freq:0.1,speed:0.6,flow:[-0.5,0.3],spec:1.3,
    deep:0x0a1a18,shallow:0x143a38,skyc:0x22483c,moonDir:[-60,100,-160]});
  g.add(water.mesh);
  /* 暮色江洲 + 白蘋水草 */
  const isle=makeForeground({kind:'坡石',n:4,r:3.2,w:30,d:12,color:0x0b120d,seed:71,rim:0.16});
  isle.g.position.set(2,-1.2,-20); g.add(isle.g);
  /* 雁阵（点击前歇在洲头，点击后人字起飞向远山） */
  const geese=makeGeese({n:7,color:0x2a2f28});
  geese.position.set(0,2.5,-30); g.add(geese);
  /* 乡书：雁足一点暖光（点击后随雁阵远去） */
  const letter=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd890,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  letter.scale.set(2.6,2.6,1); g.add(letter);
  const mist=makeMist({n:8,spread:[230,22,120],pos:[0,9,-46],scale:76,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x060a07,seed:73,rim:0.15});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x050a06,seed:75,sway:0.9});
  reeds.g.position.set(13,-1.3,12); g.add(reeds.g);
  addLights(g,{c:0xa8ccb0,i:0.5,p:[-40,90,-40]},{c:0x1e2c22,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.fly=Math.min(1,ctl.fly+dt/3.0);
      ridge.update(t,0); water.update(t); mist.update(t,k);
      isle.update(t,k); rk.update(t,k); reeds.update(t,k);
      /* 雁阵：未点击=洲头歇息微动；点击后=人字升起远去 */
      const items=geese.userData.items;
      for(const it of items){
        if(!ctl.clicked){
          it.b.position.set(it.off.x,it.off.y+Math.sin(t*1.2+it.ph)*0.08,it.off.z);
          const f=Math.sin(t*2.4+it.ph)*0.12;
          it.w1.rotation.x=f; it.w2.rotation.x=-f;
        }else{
          const q=ctl.fly, e=q*q;
          it.b.position.set(it.off.x-e*6,it.off.y+q*14+Math.sin(t*2.6+it.ph)*0.5*q,it.off.z-q*36*e);
          const f=Math.sin(t*7+it.ph)*0.5;
          it.w1.rotation.x=f; it.w2.rotation.x=-f;
        }
      }
      letter.position.copy(items[0].b.position).add(new THREE.Vector3(1.2,0.5,0));
      letter.material.opacity=k*(0.35+0.25*Math.sin(t*2.0));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.1,0.14); pluck(4,0.5,0.12); pluck(5,0.9,0.12);
        const fl=$('#flash'); fl.textContent='归雁洛阳边'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
