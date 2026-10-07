/* ================= 淮中晚泊犊头 · 三境场景（水墨夜思 · 淮上春阴变体：卷首春阴垂野、春阴幽花、孤舟潮生）
   本诗专属系统「风雨潮生」：春阴低垂、青草连天、一树幽花独明；晚泊孤舟于古祠之下。
   末境点击看潮生 → 雨密风急、满川潮头自远而近推进、孤舟随浪起伏，题字「满川风雨看潮生」。
   与同赛道《台城》（江雨柳堤）、《题临安邸》（西湖灯影）不同：本页是春阴旷野、古祠孤舟与潮头。 ================= */

/* —— 春阴垂野：低低压在原野上的阴云（暗色 Sprite 层，只调 scale/位置） —— */
function makeLowCloudSZ(o){
  o=o||{};
  const n=o.n===undefined?18:o.n, sp=o.spread===undefined?[220,7,80]:o.spread;
  const pos=o.pos===undefined?[0,9,-34]:o.pos, sc=o.scale===undefined?40:o.scale;
  const col=o.color===undefined?0x2a3440:o.color, op=o.op===undefined?0.26:o.op;
  const R=seedRnd(o.seed===undefined?601:o.seed);
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:col,transparent:true,
      opacity:op*(0.6+R()*0.7),depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set(pos[0]+(R()-0.5)*sp[0],pos[1]+(R()-0.5)*sp[1],pos[2]+(R()-0.5)*sp[2]);
    const k=sc*(0.7+R()*0.8);
    s.scale.set(k,k*0.34,1); s.renderOrder=5;
    g.add(s); items.push({s:s,base:[k,k*0.34],x0:s.position.x,ph:R()*6.283});
  }
  return {g,items,update:function(t,vig){
    const vg=vig===undefined?0:vig;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const w=1+0.05*Math.sin(t*0.18+it.ph)+0.10*vg;
      it.s.scale.set(it.base[0]*w,it.base[1]*w,1);
      it.s.position.x=it.x0+(-20+40*((t*0.06*vg)%1))*0;
    }
  }};
}

/* —— 青草：连片春草（合批 1 mesh，风过整片微倾） —— */
function makeGrassFieldSZ(o){
  o=o||{};
  const n=o.n===undefined?1500:o.n, R=seedRnd(o.seed===undefined?607:o.seed);
  const w=o.w===undefined?280:o.w, d=o.d===undefined?40:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const hh=0.5+R()*0.9, x=(R()-0.5)*w, z=(R()-0.5)*d;
    const bl=new THREE.ConeGeometry(0.05,hh,4);
    bl.rotateZ((R()-0.5)*0.28); bl.rotateY(R()*6.283);
    bl.translate(x,hh*0.5,z);
    B.put(bl,shadeColor(o.color===undefined?0x4a6a3c:o.color,0.7+R()*0.6));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3a24,emissive:0x070c06,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x9fb0c0:o.rimC,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.006+0.02*wd)*Math.sin(t*0.5+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 幽花一树：暗野里格外明亮的一树花（白粉花团带自发光，是画面的亮点） —— */
function makeBrightTreeSZ(o){
  o=o||{};
  const h=o.h===undefined?4.4:o.h, R=seedRnd(o.seed===undefined?613:o.seed);
  const wood=o.wood===undefined?0x2a2620:o.wood, petal=o.petal===undefined?0xf0e4e8:o.petal;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.46,0],h*0.055,h*0.024,7),wood);
  const tips=[];
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.32+R()*0.26);
    const p1=[Math.sin(a)*len,h*0.44+len*0.5,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.44,0],p1,h*0.024,h*0.01,6),shadeColor(wood,1.3));
    tips.push(p1);
    if(R()<0.75){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5,p1[1]+len*0.32,p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.012,h*0.005,5),shadeColor(wood,1.45));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<5;k++){
      const rr=0.20+R()*0.12;
      const fl=new THREE.SphereGeometry(rr,7,6); fl.scale(1.15,0.78,1.05);
      fl.translate(tp[0]+(R()-0.5)*1.0,tp[1]+(R()-0.3)*0.7,tp[2]+(R()-0.5)*1.0);
      B.put(fl,shadeColor(petal,0.86+R()*0.28));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x8a94a4,emissive:0x2a2428,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe0d8dc:o.rimC,i:0.34,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.012+0.03*wd)*Math.sin(t*0.6+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 古祠：荒祠一座（台基 + 门柱 + 坡顶 + 檐 + 残碑），合批 1 mesh —— */
function makeShrineSZ(o){
  o=o||{};
  const w=o.w===undefined?9:o.w, d=o.d===undefined?6:o.d, h=o.h===undefined?5:o.h;
  const wall=o.wall===undefined?0x2a2c30:o.wall, roof=o.roof===undefined?0x1c1f24:o.roof;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w*1.2,0.7,d*1.2); base.translate(0,0.35,0); B.put(base,shadeColor(0x3a3c40,0.9));
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,0.7+h/2,0); B.put(body,wall);
  const r1=new THREE.BoxGeometry(w*1.16,0.3,d*0.66); r1.rotateX(0.36); r1.translate(0,0.7+h+0.5,d*0.28);
  B.put(r1,shadeColor(roof,0.95));
  const r2=new THREE.BoxGeometry(w*1.16,0.3,d*0.66); r2.rotateX(-0.36); r2.translate(0,0.7+h+0.5,-d*0.28);
  B.put(r2,roof);
  const ridge=new THREE.BoxGeometry(w*1.2,0.24,0.4); ridge.translate(0,0.7+h+1.05,0); B.put(ridge,shadeColor(roof,1.2));
  /* 门洞与残破的柱 */
  const door=new THREE.BoxGeometry(w*0.34,h*0.62,0.24); door.translate(0,0.7+h*0.31,d/2+0.02); B.put(door,0x0c0d10);
  [1,-1].forEach(function(s){
    const p=new THREE.CylinderGeometry(0.26,0.30,h,10); p.translate(s*w*0.34,0.7+h/2,d/2+0.5); B.put(p,shadeColor(wall,1.1));
    const cap=new THREE.BoxGeometry(0.9,0.2,0.9); cap.translate(s*w*0.34,0.7+h+0.1,d/2+0.5); B.put(cap,shadeColor(roof,1.15));
  });
  /* 残碑 */
  const st=new THREE.BoxGeometry(0.9,1.6,0.3); st.rotateZ(0.06); st.translate(w*0.6,0.8,d/2+1.6); B.put(st,0x4a4c50);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2e3640,emissive:0x080a0c}),{c:o.rimC===undefined?0xa8b8c8:o.rimC,i:0.24,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 孤舟：一叶小舟（船身 + 篷 + 缆），可随浪起伏 —— */
function makeSoloBoatSZ(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(4.6,0.6,1.6); hull.translate(0,0.3,0); B.put(hull,0x3a3228);
  const bow=new THREE.ConeGeometry(0.8,1.3,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(2.3,0.34,0);
  B.put(bow,0x3a3228);
  const canopy=new THREE.CylinderGeometry(0.9,0.9,1.8,10,1,true,0,Math.PI); canopy.rotateZ(Math.PI/2);
  canopy.rotateY(Math.PI/2); canopy.translate(-0.5,0.72,0); B.put(canopy,0x4a4034);
  const seat=new THREE.BoxGeometry(1.0,0.1,1.2); seat.translate(1.2,0.62,0); B.put(seat,0x4a3e2e);
  const rope=new THREE.TorusGeometry(0.25,0.045,5,10); rope.rotateY(Math.PI/2); rope.translate(2.5,0.5,0.5);
  B.put(rope,0x6a6250);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a3a30,emissive:0x080806,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa8b8c8:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const ph=seedRnd(o.seed===undefined?619:o.seed)()*6.283;
  g.update=function(t,k,wave){
    const kk=k===undefined?1:k, wv=wave===undefined?0:wave;
    g.position.y=(o.y===undefined?0:o.y)+(0.06+0.35*wv)*Math.sin(t*(1.0+1.4*wv)+ph)*kk;
    g.rotation.z=(0.03+0.10*wv)*Math.sin(t*(0.9+1.2*wv)+ph)*kk;
    g.rotation.x=0.02*Math.sin(t*1.3+ph*1.7)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 潮头：自远而近推进的一道白浪线（数条浪脊 + 浪花粒子，只调位置/scale） —— */
function makeTideSZ(o){
  o=o||{};
  const bw=o.w===undefined?150:o.w, R=seedRnd(o.seed===undefined?631:o.seed);
  const g=new THREE.Group(), crests=[];
  for(let i=0;i<5;i++){
    const seg=new THREE.Group();
    for(let k=0;k<5;k++){
      const s=2.2+R()*2.6, hh=0.5+R()*0.7;
      const m=new THREE.Mesh(new THREE.ConeGeometry(s*0.36,hh,5),
        new THREE.MeshPhongMaterial({color:0xe8eef4,shininess:60,specular:0xffffff,emissive:0x2a3038,flatShading:true}));
      m.position.set((k-2)*bw/5+(R()-0.5)*3,hh*0.4,(R()-0.5)*2.4);
      m.rotation.y=R()*6.283;
      m.frustumCulled=false;
      seg.add(m);
    }
    seg.position.set(0,0.1,-i*16);
    g.add(seg); crests.push(seg);
  }
  const foam=makeGlow({n:220,box:[bw,3,16],pos:[0,0.6,0],color:0xd8e4f0,size:9,speed:0.0,rise:0,maxA:0.20});
  g.add(foam.points);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0.2:o.y,o.z===undefined?-10:o.z);
  const z0=g.position.z;
  return {g,crests,foam,update:function(t,adv){
    const a=adv===undefined?0:adv;
    g.position.z=z0+a*22;               /* 潮头向相机推进 */
    for(let i=0;i<crests.length;i++){
      const c=crests[i];
      c.position.z=-i*16+Math.sin(t*0.6+i)*0.6;
      c.scale.set(1+0.04*Math.sin(t*0.9+i*1.3),0.85+0.35*a,1);
    }
    foam.update(t);
  }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 春阴垂野 —— 阴云低压、青草连天、远处一树幽花
  const g=new THREE.Group();
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c22,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:290,h:30,layers:3,peaks:6,seed:1811,color:0x0c1218,atmo:0x27313c,
    fogK:0.62,glowK:0.04,glow:0x9fb0c0,y:-8});
  ridge.g.position.set(0,0,-88); g.add(ridge.g);
  const cloud=makeLowCloudSZ({n:18,spread:[240,7,80],pos:[0,10,-40],scale:44,op:0.28,seed:603});
  g.add(cloud.g);
  const grass=makeGrassFieldSZ({n:1400,w:300,d:44,y:-1.4,z:-6,seed:609}); g.add(grass.g);
  const tree=makeBrightTreeSZ({h:4.6,seed:617,scale:1.15}); tree.g.position.set(9,-1.4,-16); g.add(tree.g);
  const tree2=makeBrightTreeSZ({h:3.6,seed:621,scale:0.95}); tree2.g.position.set(-17,-1.4,-24); g.add(tree2.g);
  const shrine=makeShrineSZ({w:8,h:4.6,x:-6,y:-1.4,z:-38,ry:0.2}); g.add(shrine.g);
  const motes=makeGlow({n:44,box:[200,26,90],pos:[0,9,-26],color:0xa8bccc,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[250,26,120],pos:[0,9,-56],scale:80,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:19,d:7,color:0x070a0d,seed:97,rim:0.16,rimC:0x98a8b8});
  fg.g.position.set(-18,-1.6,40); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x090d10,seed:99,sway:1.0,tip:0x3a4a34});
  fg2.g.position.set(17,-1.5,26); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-44,70,28]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); cloud.update(t,0.1);
    grass.update(t,k,0.2); tree.update(t,k,0.25); tree2.update(t,k,0.2);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bChunyin(){ // 一 · 春阴幽花 —— 春阴垂野草青青，时有幽花一树明
  const g=new THREE.Group();
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c22,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:290,h:28,layers:3,peaks:6,seed:1821,color:0x0c1218,atmo:0x26303a,
    fogK:0.62,glowK:0.04,glow:0x9fb0c0,y:-8});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const cloud=makeLowCloudSZ({n:20,spread:[250,8,84],pos:[0,11,-44],scale:48,op:0.30,seed:611});
  g.add(cloud.g);
  const grass=makeGrassFieldSZ({n:1600,w:320,d:48,y:-1.3,z:-8,seed:623}); g.add(grass.g);
  /* 幽花一树明：主树在右前，最亮 */
  const tree=makeBrightTreeSZ({h:5.0,seed:627,scale:1.25}); tree.g.position.set(7.5,-1.3,-10); g.add(tree.g);
  const tree2=makeBrightTreeSZ({h:3.8,seed:629,scale:1.0}); tree2.g.position.set(-14,-1.3,-20); g.add(tree2.g);
  const tree3=makeBrightTreeSZ({h:3.2,seed:631,scale:0.9}); tree3.g.position.set(20,-1.3,-26); g.add(tree3.g);
  const shrine=makeShrineSZ({w:7.5,h:4.4,x:-4,y:-1.3,z:-40,ry:0.1}); g.add(shrine.g);
  const motes=makeGlow({n:42,box:[190,24,86],pos:[0,9,-24],color:0xa8bccc,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,24,110],pos:[0,8,-54],scale:78,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x070a0d,seed:101,rim:0.16,rimC:0x98a8b8});
  fg.g.position.set(-16,-1.5,26); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x090d10,seed:103,sway:1.0,tip:0x3a4a34});
  fg2.g.position.set(16,-1.4,22); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-42,68,26]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); cloud.update(t,0.12);
      const wind=0.25+0.15*Math.sin(t*0.4);
      grass.update(t,k,wind);
      tree.update(t,k,wind*1.2); tree2.update(t,k,wind); tree3.update(t,k,wind*0.9);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.35,0.08); }};
}
function bChaosheng(){ // 二（末境·可点击）· 孤舟潮生 —— 晚泊孤舟古祠下，满川风雨看潮生
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,storm:0,tide:0};
  const grd=makeGround({r:280,c1:0x0a0e12,c2:0x131a20,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:26,layers:2,peaks:6,seed:1831,color:0x0b1016,atmo:0x242e38,
    fogK:0.60,glowK:0.04,glow:0x9aacbc,y:-8});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 淮河水面 */
  const water=makeWater({size:170,seg:48,amp:0.14,freq:0.09,speed:0.5,flow:[0.25,0.8],spec:1.5,
    deep:0x0a121a,shallow:0x1e3040,skyc:0x2c4054,moonDir:[-30,90,-150],y:-0.6});
  water.mesh.position.set(0,-0.6,-30); g.add(water.mesh);
  /* 古祠在岸（右侧） */
  const shrine=makeShrineSZ({w:9,h:5.0,x:12,y:-1.3,z:-13,ry:-0.35}); g.add(shrine.g);
  /* 孤舟泊在祠下 */
  const boat=makeSoloBoatSZ({x:6.4,y:-0.35,z:-6.5,ry:0.5,seed:633}); g.add(boat.g);
  /* 岸草与幽花（近岸，标出"岸"） */
  const grass=makeGrassFieldSZ({n:900,w:60,d:16,y:-1.3,z:6,seed:637}); g.add(grass.g);
  const tree=makeBrightTreeSZ({h:4.0,seed:641,scale:1.05}); tree.g.position.set(-9,-1.3,-8); g.add(tree.g);
  const cloud=makeLowCloudSZ({n:20,spread:[250,8,84],pos:[0,10,-46],scale:46,op:0.30,seed:643});
  g.add(cloud.g);
  /* 潮头（自远而近） */
  const tide=makeTideSZ({w:150,x:0,y:-0.35,z:-46,seed:647}); g.add(tide.g);
  /* 雨：两层（点"看潮生"后转急） */
  const motes=makeGlow({n:42,box:[200,24,90],pos:[0,9,-26],color:0xa8bccc,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,26,110],pos:[0,8,-54],scale:78,color:0x22303c,op:0.13});
  g.add(mist.g);
  const crowd=makeCrowd({n:2,rect:[-26,10,14,5],seed:651,color:0x121a22,rimC:0x98a8b8,rim:0.2});  /* 人影在近岸草间，不在水上 */
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.2,w:17,d:7,color:0x070a0d,seed:107,rim:0.16,rimC:0x98a8b8});
  fg.g.position.set(-15,-1.5,16); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x090d10,seed:109,sway:1.1,tip:0x3a4a34});
  fg2.g.position.set(15,-1.4,14); g.add(fg2.g);
  addLights(g,{c:0xa0b4c4,i:0.42,p:[-40,66,24]},{c:0x1a222c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.storm=Math.min(1,ctl.storm+dt/2.2); ctl.tide=Math.min(1,ctl.tide+dt/3.4); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const st=ctl.storm+0.5*ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motes.update(t); cloud.update(t,st); crowd.update(t);
      water.update(t);
      water.mesh.material.uniforms.uAmp.value=0.14+0.30*ctl.tide;
      tide.update(t,ctl.tide+0.35*ctl.pulse);
      boat.update(t,k,ctl.tide+0.4*ctl.pulse);
      grass.update(t,k,1.2*st);
      tree.update(t,k,1.2*st);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.00,0.14); pluck(2,0.30,0.12); pluck(4,0.65,0.10);
        const fl=$('#flash'); fl.textContent='满川风雨看潮生'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：风雨再急一分，潮头再近一程 */
    },clicked:false};
  return api;
}
