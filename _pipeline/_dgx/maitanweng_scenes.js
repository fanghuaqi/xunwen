/* ================= 卖炭翁 · 五境场景（宣纸留白·苦寒变体：伐薪烧炭、衣单愿寒、辗冰进城、宫使夺炭、半纱充直） ================= */

/* 炭窑：土丘窑口冒烟（合批 1 mesh） */
function makeKiln(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const mound=new THREE.SphereGeometry(2.6,10,7); mound.scale(1.4,0.8,1.1);
  mound.translate(0,0.9,0); B.put(mound,0x5a4a3a);
  const mouth=new THREE.CylinderGeometry(0.5,0.6,0.9,8);
  mouth.rotateZ(Math.PI/2); mouth.translate(-2.2,0.55,0); B.put(mouth,0x14100c);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x3a3428,emissive:0x0b0906}),{c:o.rimC===undefined?0x8a8474:o.rimC,i:0.18,p:2.2}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return g;
}

/* 炭车：木车 + 满车乌炭 + 两轮（合批 1 mesh；ox=true 加犍牛） */
function makeCartW(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const bed=new THREE.BoxGeometry(3.6,0.25,2.0); bed.translate(0,1.15,0); B.put(bed,0x4a3a26);
  const pile=new THREE.SphereGeometry(1.35,9,7); pile.scale(1.5,0.85,1.0);
  pile.translate(0,2.1,0); B.put(pile,0x14100c);
  [-1.1,1.1].forEach(function(z){
    const wh=new THREE.TorusGeometry(0.85,0.12,6,16);
    wh.rotateY(Math.PI/2); wh.translate(1.2,0.9,z); B.put(wh,0x3a2c1c);
    for(let i=0;i<4;i++){
      const sp=new THREE.CylinderGeometry(0.04,0.04,1.6,4);
      const m4=new THREE.Matrix4().makeTranslation(1.2,0.9,z).multiply(new THREE.Matrix4().makeRotationY(i*0.78));
      sp.applyMatrix4(new THREE.Matrix4().makeTranslation(-1.2,-0.9,-z)).applyMatrix4(m4);
      B.put(sp,0x3a2c1c);
    }
  });
  const shaft=new THREE.CylinderGeometry(0.06,0.07,3.4,5);
  shaft.rotateZ(Math.PI/2-0.1); shaft.translate(-2.9,1.05,0); B.put(shaft,0x3a2c1c);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3428,emissive:0x080706,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x8a8474:o.rimC,i:0.2,p:2.4})));
  if(o.ox){
    const ox=new THREE.Group();
    const OB=new GeoBag();
    const body=new THREE.SphereGeometry(0.95,9,7); body.scale(1.8,1.0,0.85); body.translate(0,1.35,0); OB.put(body,0x4a4034);
    const head=new THREE.SphereGeometry(0.4,8,6); head.scale(1.4,1.0,0.8); head.translate(1.85,1.75,0); OB.put(head,shadeColor(0x4a4034,1.1));
    for(let i=0;i<2;i++){
      const horn=new THREE.ConeGeometry(0.07,0.5,5); horn.rotateZ(-0.9-i*0.2);
      horn.translate(2.0,2.2,0.16-0.32*i); OB.put(horn,0x8a8070);
    }
    [[0.7,-0.35],[0.7,0.35],[-0.8,-0.35],[-0.8,0.35]].forEach(function(p){
      OB.put(limbGeo([p[0],1.0,p[1]],[p[0]*1.04,0.05,p[1]],0.13,0.07,6),shadeColor(0x4a4034,0.85));
    });
    ox.add(OB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x3c3a30,emissive:0x070605}),{c:o.rimC===undefined?0x8a8474:o.rimC,i:0.2,p:2.4})));
    ox.position.set(-5.4,0,0); g.add(ox);
  }
  g.scale.setScalar(s);
  return g;
}

/* 城门：唐长安坊门剪影（两墩一门洞，合批 1 mesh） */
function makeGate(o){
  o=o||{};
  const w=o.w===undefined?26:o.w, h=o.h===undefined?9:o.h;
  const B=new GeoBag();
  const left=new THREE.BoxGeometry(w*0.42,h,w*0.16); left.translate(-w*0.29,h/2,0); B.put(left,0x2e2822);
  const right=new THREE.BoxGeometry(w*0.42,h,w*0.16); right.translate(w*0.29,h/2,0); B.put(right,0x2e2822);
  const top=new THREE.BoxGeometry(w,h*0.18,w*0.18); top.translate(0,h+h*0.09,0); B.put(top,shadeColor(0x2e2822,1.15));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x3a3428,emissive:0x080706}),{c:o.rimC===undefined?0x8a8474:o.rimC,i:0.16,p:2.2}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 雪前宣纸
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0xe4ddc9,c2:0xd6ceB8});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:170,h:40,layers:3,peaks:4,seed:41,color:0x2c2f33,atmo:0xb8b2a0,fogK:0.72,glowK:0.04,y:-8});
  ridge.g.position.set(0,0,60); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x23262a,seed:5,rim:0.12,rimC:0xd8d2c2});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xe0d8c2,op:0.13});
  g.add(mist.g);
  const motes=makeGlow({n:50,box:[220,36,130],pos:[0,8,-40],color:0xb8ae94,size:7,speed:0.05,rise:0,maxA:0.28,add:false});
  g.add(motes.points);
  addLights(g,{c:0xfff4e0,i:0.55,p:[30,70,40]},{c:0xcfc8b4,i:0.7});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bFaxin(){ // 一 · 伐薪烧炭 —— 南山炭窑烟火，满面尘灰的老翁
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0xdcd5c1,c2:0xcac2ac});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:52,layers:3,peaks:5,seed:651,color:0x2c2f33,atmo:0xbcb6a2,fogK:0.64,glowK:0.04});
  ridge.g.position.set(0,0,-56); g.add(ridge.g);
  /* 炭窑两座 + 窑烟 */
  const kiln=makeKiln({}); kiln.position.set(-4,0,-8); g.add(kiln);
  const kiln2=makeKiln({scale:0.8}); kiln2.position.set(-8,0,-13); g.add(kiln2);
  const smoke=makeGlow({n:70,box:[14,26,12],pos:[-4,16,-8],color:0x4a4438,size:34,speed:0.05,rise:1,maxA:0.34,add:false});
  smoke.points.renderOrder=5; g.add(smoke.points);
  /* 薪柴堆 */
  for(let i=0;i<6;i++){
    const log=new THREE.Mesh(new THREE.CylinderGeometry(0.14,0.17,3.0,6),
      new THREE.MeshPhongMaterial({color:0x3a2e20,shininess:4}));
    log.rotation.z=Math.PI/2; log.rotation.y=i*0.5;
    log.position.set(3.4,0.16+i*0.05,-6); g.add(log);
  }
  /* 主体：老翁（佝偻伐薪，衣褐） */
  const old=makeFigure({pose:'独立',robe:0x4a4034,belt:0x6a5a3a,hat:'发髻',beard:true,face:0.35,scale:1.15,rim:0.22,rimC:0xd8d2c2});
  old.position.set(0.5,0,-4.5); g.add(old);
  const axe=new THREE.Mesh(new THREE.CylinderGeometry(0.04,0.05,2.2,5),
    new THREE.MeshPhongMaterial({color:0x3a2e20}));
  axe.rotation.z=0.7; axe.position.set(1.9,1.6,-4.3); g.add(axe);
  const mist=makeMist({n:6,spread:[180,18,100],pos:[0,7,-38],scale:62,color:0xd8d0ba,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:117,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xfff4e0,i:0.55,p:[30,70,30]},{c:0xcfc8b4,i:0.7});
  const pl=new THREE.PointLight(0xffb050,1.0,26); pl.position.set(-4,1.4,-8); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); smoke.update(t,k); mist.update(t,k);
    old.update(t,k); rk.update(t,k);
    pl.intensity=k*(1.0*(0.85+0.15*Math.sin(t*6.2)));
  }};
}
function bYidan(){ // 二（标志性瞬间）· 衣单愿寒 —— 衣正单，心忧炭贱愿天寒
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0xd8d1bd,c2:0xc6beA8});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 天色转阴（雪意：宣纸天压暗一分） */
  const ridge=makeRange({r:210,h:44,layers:3,peaks:5,seed:661,color:0x2c2f33,atmo:0xa8a292,fogK:0.62,glowK:0.03});
  ridge.g.position.set(0,0,-56); g.add(ridge.g);
  /* 老翁立于崖前（单薄衣衫） */
  const old=makeFigure({pose:'独立',robe:0x4a4034,belt:0x6a5a3a,hat:'发髻',beard:true,face:0.1,scale:1.3,rim:0.26,rimC:0xd8d2c2});
  old.position.set(0,0,-4); g.add(old);
  /* 身后：小炭堆与柴担 */
  for(let i=0;i<8;i++){
    const c=new THREE.Mesh(new THREE.SphereGeometry(0.22,6,5),
      new THREE.MeshPhongMaterial({color:0x181410,shininess:6}));
    const a=i/8*6.283;
    c.position.set(Math.cos(a)*1.3,0.2,Math.sin(a)*0.9-5.6); g.add(c);
  }
  /* 寒意：细雪先至（零星几点，NormalBlending） */
  const snow=makeGlow({n:60,box:[110,26,70],pos:[0,15,-20],color:0xe8ecf0,size:3.6,speed:0.1,rise:1,maxA:0.3,add:false});
  snow.points.renderOrder=3; g.add(snow.points);
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-40],scale:68,color:0xd0c8b2,op:0.12});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:119,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xf0e8d8,i:0.42,p:[30,60,30]},{c:0xbab4a0,i:0.72});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); snow.update(t); mist.update(t,k);
    old.update(t,k); rk.update(t,k);
  }};
}
function bZhanbing(){ // 三 · 辗冰进城 —— 一尺雪、炭车辗冰辙、市南门外泥中歇
  const g=new THREE.Group();
  /* 雪原（宣纸覆雪） */
  const grd=makeGround({r:140,c1:0xe8ecf0,c2:0xd4dae0});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:30,layers:2,peaks:4,seed:671,color:0x33363a,atmo:0xc4c2be,fogK:0.60,glowK:0.03});
  ridge.g.position.set(0,0,-64); g.add(ridge.g);
  /* 雪辙长路（两道深辙） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(4.4,0.05,90),
    new THREE.MeshPhongMaterial({color:0xc0c6ce,shininess:10,specular:0xe8ecf2}));
  road.position.set(0,0.02,-24); g.add(road);
  [-0.8,0.8].forEach(function(x){
    const rut=new THREE.Mesh(new THREE.BoxGeometry(0.3,0.03,90),
      new THREE.MeshPhongMaterial({color:0x9aa2ae,shininess:6}));
    rut.position.set(x,0.05,-24); g.add(rut);
  });
  /* 主体：牛拉炭车（缓缓前行） */
  const cart=makeCartW({ox:true,scale:1.15}); cart.position.set(-2,0,-2); cart.rotation.y=0.1; g.add(cart);
  /* 老翁在旁牵牛 */
  const old=makeFigure({pose:'独立',robe:0x4a4034,hat:'发髻',beard:true,face:0.5,scale:1.05,rim:0.22,rimC:0xd8d2c2});
  old.position.set(-4.6,0,0.4); g.add(old);
  /* 落雪（一尺雪：密而缓） */
  const snow=makeGlow({n:170,box:[140,30,80],pos:[0,18,-24],color:0xf2f5f8,size:4.2,speed:0.12,rise:1,maxA:0.42,add:false});
  snow.points.renderOrder=3; g.add(snow.points);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,9,-46],scale:70,color:0xd8dce2,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x33363c,seed:121,rim:0.1,rimC:0xe0e4ea});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xf0f0f4,i:0.5,p:[20,70,30]},{c:0xc8ccd4,i:0.7});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); snow.update(t); mist.update(t,k);
    old.update(t,k); rk.update(t,k);
    cart.position.x=-2+Math.sin(t*0.4)*0.4;
    cart.rotation.z=Math.sin(t*0.5)*0.012;
  }};
}
function bGongshi(){ // 四 · 宫使夺炭 —— 翩翩两骑，手把文书口称敕，回车叱牛
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0xdad3bf,c2:0xc8c0aa});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:30,layers:2,peaks:3,seed:681,color:0x2c2f33,atmo:0xa8a292,fogK:0.60,glowK:0.03});
  ridge.g.position.set(0,0,-58); g.add(ridge.g);
  /* 城门 + 门洞（市南门） */
  const gate=makeGate({}); gate.position.set(0,0,-24); g.add(gate);
  /* 宫使两骑（黄衣+白衫，居高临下） */
  const mk=new THREE.Group();
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.0,10,8); body.scale(1.9,1.0,0.72); body.translate(0,1.7,0); B.put(body,0x2c241c);
  const neck=new THREE.CylinderGeometry(0.28,0.42,1.5,7); neck.rotateZ(-0.6); neck.translate(1.55,2.5,0); B.put(neck,shadeColor(0x2c241c,0.9));
  const head=new THREE.SphereGeometry(0.34,8,6); head.scale(1.5,0.9,0.7); head.translate(2.25,3.2,0); B.put(head,shadeColor(0x2c241c,1.1));
  [[0.85,-0.32],[0.85,0.32],[-0.95,-0.32],[-0.95,0.32]].forEach(function(p){
    B.put(limbGeo([p[0],1.3,p[1]],[p[0]*1.05,0.06,p[1]],0.13,0.07,6),shadeColor(0x2c241c,0.85));
  });
  mk.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3c3a34,emissive:0x060504}),{c:0xd8d2c2,i:0.2,p:2.4})));
  mk.position.set(-3,0,-8); mk.rotation.y=Math.PI/2-0.3; g.add(mk);
  const e1=makeFigure({pose:'独立',robe:0xc8a030,belt:0x8a6a24,hat:'幞头',face:0.4,scale:1.05,rim:0.3,rimC:0xe0d8c4});
  e1.position.set(-3.2,1.6,-8); g.add(e1);
  const mk2=mk.clone(); mk2.position.set(7,0,-11); mk2.rotation.y=Math.PI/2-0.5; g.add(mk2);
  const e2=makeFigure({pose:'独立',robe:0xd8d4c8,belt:0x8a6a24,hat:'发髻',face:0.3,scale:1.0,rim:0.28,rimC:0xe0d8c4});
  e2.position.set(7.2,1.6,-11); g.add(e2);
  /* 被夺的炭车（车头已被调向北） */
  const cart=makeCartW({ox:true,scale:1.0}); cart.position.set(-9,0,-3); cart.rotation.y=Math.PI+0.4; g.add(cart);
  const old=makeFigure({pose:'独立',robe:0x4a4034,hat:'发髻',beard:true,face:-0.6,scale:1.0,rim:0.2,rimC:0xd8d2c2});
  old.position.set(-11.5,0,-0.5); g.add(old);
  /* 文书（一点"官"色：黄卷） */
  const doc=new THREE.Mesh(new THREE.PlaneGeometry(0.8,1.1),
    new THREE.MeshBasicMaterial({color:0xe8d890,side:THREE.DoubleSide}));
  doc.position.set(-1.8,3.4,-8); doc.rotation.y=1.2; g.add(doc);
  const mist=makeMist({n:6,spread:[190,18,100],pos:[0,8,-40],scale:64,color:0xd0c8b2,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:123,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xf0e8d8,i:0.48,p:[20,60,30]},{c:0xbab4a0,i:0.72});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    e1.update(t,k); e2.update(t,k); old.update(t,k);
    doc.rotation.y=1.2+Math.sin(t*2.2)*0.2;
    rk.update(t,k);
  }};
}
function bBansha(){ // 五（末境·可点击）· 半纱充直 —— 点击牛头，半匹红纱系上——全篇唯一重色
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,tie:0};
  const grd=makeGround({r:130,c1:0xdcd5c1,c2:0xcac2ac});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:28,layers:2,peaks:3,seed:691,color:0x2c2f33,atmo:0xa8a292,fogK:0.60,glowK:0.03});
  ridge.g.position.set(0,0,-56); g.add(ridge.g);
  /* 空车北去的方向（宫城剪影） */
  const palace=new THREE.Mesh(new THREE.BoxGeometry(30,10,6),
    new THREE.MeshPhongMaterial({color:0x35302a,shininess:4}));
  palace.position.set(0,4.2,-40); g.add(palace);
  const roofP=new THREE.Mesh(new THREE.BoxGeometry(34,1.4,8),
    new THREE.MeshPhongMaterial({color:0x2a2620,shininess:4}));
  roofP.position.set(0,10,-40); g.add(roofP);
  /* 老牛与空车（炭已去） */
  const cart=makeCartW({ox:true,scale:1.1}); cart.position.set(-2,0,-4); cart.rotation.y=0.25; g.add(cart);
  /* 半匹红纱（挂在车辕上，点击后"系向牛头"） */
  const silk=new THREE.Mesh(new THREE.PlaneGeometry(1.5,2.4),
    new THREE.MeshPhongMaterial({color:0xc04028,side:THREE.DoubleSide,shininess:24,
      specular:0xe08060,emissive:0x1c0602}));
  silk.position.set(-6.2,2.0,-3.4); silk.rotation.y=0.5; g.add(silk);
  /* 老翁枯立（远处背影） */
  const old=makeFigure({pose:'独立',robe:0x4a4034,hat:'发髻',beard:true,face:-0.2,scale:1.05,rim:0.18,rimC:0xd8d2c2});
  old.position.set(-12,0,2); g.add(old);
  const burst=makeBurst({n:60,color:0xd86850,pos:[-6.6,2.6,-3.2]}); g.add(burst.points);
  const mist=makeMist({n:6,spread:[190,18,100],pos:[0,8,-38],scale:64,color:0xd0c8b2,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x23262a,seed:125,rim:0.12,rimC:0xd8d2c2});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0xf0e8d8,i:0.46,p:[20,60,30]},{c:0xbab4a0,i:0.72});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.tie=Math.min(1,ctl.tie+dt/1.8);
      ridge.update(t,0); mist.update(t,k);
      old.update(t,k); rk.update(t,k); burst.update(t);
      /* 红纱从车辕飘系到牛头 */
      silk.position.x=-6.2+ctl.tie*5.2;
      silk.position.y=2.0+ctl.tie*0.3+Math.sin(t*2.0)*0.06;
      silk.rotation.y=0.5-ctl.tie*0.5;
      silk.rotation.z=Math.sin(t*1.6)*0.05*(1-ctl.tie*0.7);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(0,0.1,0.12); pluck(2,0.8,0.1);
        const fl=$('#flash'); fl.textContent='系向牛头充炭直'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
