/* ================= 画眉鸟 · 三境场景（青绿春晓 · 山花鸟鸣变体：卷首山林、百啭千声、金笼林间）
   本诗专属系统「金笼·林间」：林间画眉自由啼鸣（随意移），金笼里的画眉也在啼。
   末境点击自在啼 → 笼门开启、笼中画眉飞出盘旋、与林间画眉对啼会合，题字「自在啼」。
   与同赛道《三衢道中》（黄鹂绿阴）不同：本页主角是**画眉**（白眉纹的褐鸟）与一只金笼。 ================= */

/* —— 画眉：白眉纹的褐羽鸟（区别于黄鹂的黄色），合批 1 mesh，啼鸣时挺颈振羽 —— */
function makeWarblerHM(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0x9a7448:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.27,8,6); body.scale(1.5,0.95,0.9); body.translate(0,0.27,0); B.put(body,c);
  const rump=new THREE.SphereGeometry(0.18,7,6); rump.scale(1.2,0.9,0.9); rump.translate(-0.30,0.24,0);
  B.put(rump,shadeColor(c,0.88));
  const head=new THREE.SphereGeometry(0.165,8,6); head.translate(0.31,0.45,0); B.put(head,shadeColor(c,1.12));
  /* 画眉特征：眼周白圈 + 白眉纹 */
  const brow1=new THREE.BoxGeometry(0.20,0.05,0.06); brow1.rotateZ(0.18); brow1.translate(0.34,0.53,0.075);
  B.put(brow1,0xf0ece0);
  const brow2=new THREE.BoxGeometry(0.20,0.05,0.06); brow2.rotateZ(0.18); brow2.translate(0.34,0.53,-0.075);
  B.put(brow2,0xf0ece0);
  const eye1=new THREE.SphereGeometry(0.045,6,5); eye1.translate(0.40,0.47,0.10); B.put(eye1,0x201c18);
  const eye2=new THREE.SphereGeometry(0.045,6,5); eye2.translate(0.40,0.47,-0.10); B.put(eye2,0x201c18);
  const beak=new THREE.ConeGeometry(0.045,0.19,5); beak.rotateZ(-Math.PI/2); beak.translate(0.50,0.44,0); B.put(beak,0xb08a4a);
  const wing=new THREE.SphereGeometry(0.16,7,6); wing.scale(1.35,0.42,0.85); wing.translate(-0.06,0.40,0.15);
  B.put(wing,shadeColor(0x6a5030,1.1));
  const tail=new THREE.ConeGeometry(0.085,0.5,5); tail.rotateZ(1.28); tail.translate(-0.50,0.32,0); B.put(tail,shadeColor(c,0.92));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x8a7a58,emissive:0x141008,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe0d8b0:o.rimC,i:0.40,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?401:o.seed)()*6.283;
  g.update=function(t,k,sing){
    const kk=k===undefined?1:k, sg=sing===undefined?0:sing;
    g.rotation.z=0.06*Math.sin(t*1.2+ph)*kk;
    g.rotation.y=(o.ry===undefined?0:o.ry)+0.22*sg*Math.sin(t*5.6+ph);
    const pulse=1+0.10*sg*Math.max(0,Math.sin(t*4.6+ph));
    g.scale.setScalar(s*pulse);
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 金笼：华美的鸟笼（笼身竖条 + 上下箍 + 拱顶 + 挂钩 + 食罐 + 笼门） —— */
function makeCageHM(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, r=o.r===undefined?1.1:o.r, h=o.h===undefined?2.4:o.h;
  const gold=o.gold===undefined?0xc8a04a:o.gold;
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(r*1.08,r*1.18,0.22,16); base.translate(0,0.11,0); B.put(base,shadeColor(gold,0.85));
  const top=new THREE.CylinderGeometry(r*1.02,r*1.10,0.16,16); top.translate(0,h,0); B.put(top,shadeColor(gold,1.05));
  for(let i=0;i<14;i++){
    const a=i/14*6.283;
    const bar=new THREE.CylinderGeometry(0.035,0.035,h,4);
    bar.translate(Math.sin(a)*r,h/2+0.16,Math.cos(a)*r); B.put(bar,shadeColor(gold,0.9+(i%2)*0.15));
  }
  [0.35,0.62,0.88].forEach(function(f){
    const ring=new THREE.TorusGeometry(r*1.0,0.045,5,18); ring.rotateX(Math.PI/2);
    ring.translate(0,0.16+h*f,0); B.put(ring,shadeColor(gold,1.2));
  });
  const dome=new THREE.SphereGeometry(r*0.95,14,8,0,Math.PI*2,0,Math.PI*0.5); dome.translate(0,h+0.16,0);
  B.put(dome,shadeColor(gold,1.1));
  const hook=new THREE.TorusGeometry(0.22,0.045,5,14); hook.rotateY(Math.PI/2);
  hook.translate(0,h+0.16+r*0.95+0.2,0); B.put(hook,shadeColor(gold,1.25));
  const dish=new THREE.CylinderGeometry(0.22,0.18,0.18,10); dish.translate(r*0.5,0.36,0); B.put(dish,0x8a6a34);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:44,
    specular:0xf0d898,emissive:0x1c1408}),{c:o.rimC===undefined?0xf0d898:o.rimC,i:0.46,p:2.6}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 笼门（可开：绕竖轴旋转；末境点击后打开） */
  const doorGeo=new THREE.BoxGeometry(r*0.9,h*0.62,0.06);
  doorGeo.translate(r*0.45,h*0.52,0);
  const door=new THREE.Mesh(doorGeo,rimHook(new THREE.MeshPhongMaterial({color:0xd8b45a,shininess:50,
    specular:0xf8e8b0,emissive:0x241a08}),{c:0xf8e8b0,i:0.5,p:2.6}));
  door.frustumCulled=false;
  const hinge=new THREE.Group(); hinge.position.set(-r*0.45,0,0); hinge.add(door); g.add(hinge);
  g.scale.setScalar(s);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  const ph=seedRnd(o.seed===undefined?409:o.seed)()*6.283;
  g.update=function(t,k,open){
    const kk=k===undefined?1:k, op=open===undefined?0:open;
    hinge.rotation.y=op*1.9;
    g.rotation.z=0.012*Math.sin(t*0.9+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,hinge};
}

/* —— 山花：红紫成片的花丛（低矮花簇，合批 1 mesh） —— */
function makeFlowerBushHM(o){
  o=o||{};
  const n=o.n===undefined?26:o.n, R=seedRnd(o.seed===undefined?419:o.seed);
  const w=o.w===undefined?30:o.w, d=o.d===undefined?14:o.d;
  const B=new GeoBag();
  const cols=[0xc84a60,0xa8489a,0xd06a7a,0x8a4aa0];
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, hh=0.7+R()*0.9;
    const stem=new THREE.CylinderGeometry(0.04,0.05,hh,5); stem.translate(x,hh*0.5,z);
    B.put(stem,shadeColor(0x3a5a30,0.9+R()*0.3));
    for(let k=0;k<4;k++){
      const rr=0.16+R()*0.12;
      const fl=new THREE.SphereGeometry(rr,6,5); fl.scale(1.1,0.7,1.1);
      fl.translate(x+(R()-0.5)*0.5,hh*(0.75+R()*0.4),z+(R()-0.5)*0.5);
      B.put(fl,shadeColor(cols[(i*3+k)%cols.length],0.82+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x6a5a50,emissive:0x180c10,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe0a0b0:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.01+0.03*wd)*Math.sin(t*0.8+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 高低树：山间高低错落的树（树干 + 冠），合批 1 mesh —— */
function makeTreeHM(o){
  o=o||{};
  const h=o.h===undefined?5:o.h, R=seedRnd(o.seed===undefined?421:o.seed);
  const wood=o.wood===undefined?0x3a2a18:o.wood, leaf=o.leaf===undefined?0x356030:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.5,0],h*0.06,h*0.026,6),wood);
  for(let i=0;i<3;i++){
    const a=R()*6.283, len=h*(0.25+R()*0.2);
    const p1=[Math.sin(a)*len,h*0.5+len*0.5,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.48,0],p1,h*0.022,h*0.009,5),shadeColor(wood,1.25));
  }
  const nc=o.crown===undefined?5:o.crown;
  for(let i=0;i<nc;i++){
    const rr=h*(0.16+R()*0.13);
    const s=new THREE.SphereGeometry(rr,7,6); s.scale(1.22,0.82,1.0);
    s.translate((R()-0.5)*h*0.42,h*(0.62+R()*0.3),(R()-0.5)*h*0.42);
    B.put(s,shadeColor(leaf,0.8+R()*0.45));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x3a5a34,emissive:0x0c1408,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa8d8a0:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.012+0.026*wd)*Math.sin(t*0.6+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 山林春色 —— 高低树丛、山花红紫、林间数鸟
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e1c14,c2:0x18301e,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:40,layers:3,peaks:5,seed:1711,color:0x0f2015,atmo:0x35543a,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-11});
  ridge.g.position.set(0,0,-94); g.add(ridge.g);
  const trees=[];
  [[-16,0,-20],[-8,0,-14],[2,0,-24],[11,0,-16],[19,0,-22]].forEach(function(p,i){
    const t=makeTreeHM({h:4.0+((i*3)%4)*0.9,seed:431+i*11,scale:1.05}); t.g.position.set(p[0],-1.3,p[2]); g.add(t.g); trees.push(t);
  });
  const bush1=makeFlowerBushHM({n:24,w:30,d:12,x:-9,y:-1.3,z:-9,seed:441,scale:1.0}); g.add(bush1.g);
  const bush2=makeFlowerBushHM({n:18,w:20,d:10,x:12,y:-1.3,z:-11,seed:443,scale:0.9}); g.add(bush2.g);
  const bird1=makeWarblerHM({scale:1.5,seed:451,ry:1.2}); bird1.g.position.set(-6.2,3.4,-6.4); g.add(bird1.g);
  const bird2=makeWarblerHM({scale:1.35,seed:453,ry:-1.0}); bird2.g.position.set(5.4,4.0,-8.2); g.add(bird2.g);
  const motes=makeGlow({n:42,box:[170,26,86],pos:[0,9,-22],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,100],pos:[0,8,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x060c08,seed:81,rim:0.14,rimC:0xa3c98f});
  fg.g.position.set(-15,-1.5,32); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:28,n:8,d:6,color:0x071009,seed:83,sway:0.7,rim:0.12,rimC:0xa3c98f});
  fg2.g.position.set(16,-1.4,22); fg2.g.rotation.z=-0.2; g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-40,80,26]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    const wind=0.3+0.2*Math.sin(t*0.4);
    for(let i=0;i<trees.length;i++)trees[i].update(t,k,wind);
    bush1.update(t,k,wind); bush2.update(t,k,wind);
    bird1.update(t,k,0.1); bird2.update(t,k,0.1);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bBaizhuan(){ // 一 · 百啭千声 —— 百啭千声随意移，山花红紫树高低
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e1c14,c2:0x18301e,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:42,layers:3,peaks:5,seed:1721,color:0x0f2015,atmo:0x365438,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-11});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 高低树：错落成林 */
  const trees=[];
  [[-18,0,-22],[-11,0,-13],[-3,0,-26],[4,0,-16],[12,0,-24],[19,0,-14]].forEach(function(p,i){
    const t=makeTreeHM({h:3.6+((i*5)%5)*1.0,seed:461+i*13,scale:1.1}); t.g.position.set(p[0],-1.2,p[2]); g.add(t.g); trees.push(t);
  });
  /* 山花红紫：三片花丛 */
  const bushes=[];
  [[-12,0,-8,26,1.0,471],[-1,0,-11,20,0.92,473],[10,0,-9,22,0.98,477]].forEach(function(b){
    const bs=makeFlowerBushHM({n:b[3],w:22,d:11,x:b[0],y:-1.2,z:b[2],scale:b[4],seed:b[5]});
    g.add(bs.g); bushes.push(bs);
  });
  /* 随意移：林间四只画眉（高低错落、各据一枝） */
  const birds=[];
  [[-8.5,3.2,-5.0,1.3,481],[-2.2,4.2,-7.0,-1.1,483],[6.0,3.6,-4.6,1.0,487],[12.5,4.6,-6.8,1.2,491]].forEach(function(b){
    const bd=makeWarblerHM({scale:1.6,seed:b[4],ry:b[3]}); bd.g.position.set(b[0],b[1],b[2]); g.add(bd.g); birds.push(bd);
  });
  const motes=makeGlow({n:40,box:[160,24,84],pos:[0,9,-20],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,96],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060c08,seed:85,rim:0.14,rimC:0xa3c98f});
  fg.g.position.set(-14,-1.4,19); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:24,n:7,d:6,color:0x071009,seed:87,sway:0.7,rim:0.12,rimC:0xa3c98f});
  fg2.g.position.set(15,-1.3,17); fg2.g.rotation.z=-0.18; g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-38,78,24]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      const wind=0.35+0.25*Math.sin(t*0.45);
      for(let i=0;i<trees.length;i++)trees[i].update(t,k,wind);
      for(let i=0;i<bushes.length;i++)bushes[i].update(t,k,wind);
      for(let i=0;i<birds.length;i++)birds[i].update(t,k,0.15);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(5,0.3,0.08); pluck(4,0.75,0.07); }};
}
function bZizai(){ // 二（末境·可点击）· 金笼林间 —— 始知锁向金笼听，不及林间自在啼
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,open:0,fly:0};
  const grd=makeGround({r:250,c1:0x0d1a12,c2:0x172c1c,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:38,layers:2,peaks:5,seed:1731,color:0x0e1e14,atmo:0x33503a,
    fogK:0.60,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const trees=[];
  [[-17,0,-20],[-9,0,-13],[8,0,-22],[16,0,-15],[24,0,-19]].forEach(function(p,i){
    const t=makeTreeHM({h:4.2+((i*3)%4)*0.9,seed:501+i*13,scale:1.1}); t.g.position.set(p[0],-1.2,p[2]); g.add(t.g); trees.push(t);
  });
  const bushes=[];
  [[-12,0,-7,20,0.95,511],[-2,0,-9,16,0.9,513]].forEach(function(b){
    const bs=makeFlowerBushHM({n:b[3],w:18,d:10,x:b[0],y:-1.2,z:b[2],scale:b[4],seed:b[5]});
    g.add(bs.g); bushes.push(bs);
  });
  /* 金笼挂在左侧横枝上（笼中一只画眉） */
  const cage=makeCageHM({r:1.15,h:2.5,scale:1.0,x:-6.6,y:2.4,z:-3.4,seed:417});
  g.add(cage.g);
  const caged=makeWarblerHM({scale:1.5,seed:521,ry:1.1}); caged.g.position.set(-6.6,2.9,-3.4); g.add(caged.g);
  /* 林间三只画眉（自在啼） */
  const free=[];
  [[2.6,3.6,-5.2,-1.1,523],[9.5,4.4,-7.0,1.2,527],[15.5,3.4,-4.8,-1.0,529]].forEach(function(b){
    const bd=makeWarblerHM({scale:1.6,seed:b[4],ry:b[3]}); bd.g.position.set(b[0],b[1],b[2]); g.add(bd.g); free.push(bd);
  });
  const motes=makeGlow({n:40,box:[160,24,84],pos:[0,9,-18],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,96],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x060c08,seed:91,rim:0.14,rimC:0xa3c98f});
  fg.g.position.set(-14,-1.4,14); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x071009,seed:93,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(13,-1.3,12); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-36,76,22]},{c:0x22301f,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.open=Math.min(1,ctl.open+dt/0.9); ctl.fly=Math.min(1,ctl.fly+dt/2.6); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const sg=0.3+0.7*Math.min(1,ctl.fly+0.6*ctl.pulse);
      const wind=0.35+0.5*sg;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      for(let i=0;i<trees.length;i++)trees[i].update(t,k,wind);
      for(let i=0;i<bushes.length;i++)bushes[i].update(t,k,wind);
      cage.update(t,k,ctl.open);
      /* 笼中画眉：笼门开后飞出，盘旋着落向林间（只动位置/朝向） */
      const u=ctl.fly;
      const arc=Math.sin(Math.min(1,u)*Math.PI);
      caged.g.position.set(-6.6+u*11.0,2.9+arc*2.6+u*0.9,-3.4-u*2.4);
      caged.g.rotation.y=1.1+u*3.4;
      caged.update(t,k,sg);
      for(let i=0;i<free.length;i++)free[i].update(t,k,sg);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(4,0.18,0.11); pluck(5,0.36,0.10); pluck(3,0.56,0.09); pluck(4,0.78,0.08);
        const fl=$('#flash'); fl.textContent='自在啼'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：对啼再起一阵 */
    },clicked:false};
  return api;
}
