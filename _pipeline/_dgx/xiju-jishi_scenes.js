/* ================= 溪居即事 · 三境场景（青绿春晓 · 溪居童趣变体：卷首溪湾村居、篱外春船、小童去关）
   本诗专属系统「不系·却关」：不系船随风漂入钓鱼湾（无人之动），小童误认客至、急向柴门去却关（童趣之动）。
   末境点击去却关 → 小童奔到柴门、门闩抬起、两扇柴扉转开、小船继续漂入湾深处，题字「去却关」。
   与同赛道《三衢道中》《画眉鸟》《菊花》《绝句·古木阴中》并排：本页是溪湾、柴门与奔跑的小童。 ================= */

/* —— 不系船：没有缆绳的小舟（可随风漂移/打转） —— */
function makeMoorlessBoatXJ(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(3.8,0.5,1.4); hull.translate(0,0.26,0); B.put(hull,0x5a452c);
  const bow=new THREE.ConeGeometry(0.7,1.15,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(1.9,0.3,0);
  B.put(bow,0x5a452c);
  const stern=new THREE.ConeGeometry(0.68,1.05,4); stern.rotateY(Math.PI/4); stern.rotateZ(Math.PI/2); stern.translate(-1.9,0.3,0);
  B.put(stern,shadeColor(0x5a452c,0.9));
  const seat=new THREE.BoxGeometry(1.0,0.1,1.15); seat.translate(0.2,0.55,0); B.put(seat,0x6a5236);
  const plank=new THREE.BoxGeometry(0.9,0.08,1.3); plank.translate(-1.0,0.5,0); B.put(plank,0x6a5236);
  /* 桨（横搁在船上，无缆绳——"不系"） */
  const oar=new THREE.CylinderGeometry(0.05,0.05,2.6,6); oar.rotateZ(1.45); oar.translate(-0.2,0.72,0.5); B.put(oar,0x7a6440);
  const blade=new THREE.BoxGeometry(0.5,0.06,0.24); blade.translate(-1.5,0.66,0.5); B.put(blade,0x8a7450);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x5a5030,emissive:0x0c0a06,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xc8d8a8:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const ph=seedRnd(o.seed===undefined?1101:o.seed)()*6.283;
  const x0=g.position.x, y0=g.position.y, z0=g.position.z, ry0=g.rotation.y;
  g.update=function(t,k,drift){
    const kk=k===undefined?1:k, dr=drift===undefined?0:drift;
    /* drift 0→1：船随风由湾口漂入湾中（位移 + 缓慢打转） */
    g.position.x=x0+dr*3.2+0.10*Math.sin(t*0.9+ph)*kk;
    g.position.z=z0+dr*7.6+0.14*Math.sin(t*0.7+ph*1.3)*kk;
    g.position.y=y0+0.07*Math.sin(t*1.2+ph)*kk;
    g.rotation.y=ry0+dr*1.5+0.05*Math.sin(t*0.6+ph)*kk;
    g.rotation.z=0.04*Math.sin(t*0.85+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 柴门：柴扉两扇 + 门柱 + 门闩（可抬起、可转开）+ 土墙，合批 1 mesh + 可动件 —— */
function makeWickerGateXJ(o){
  o=o||{};
  const w=o.w===undefined?3.2:o.w, h=o.h===undefined?2.5:o.h;
  const wood=o.wood===undefined?0x6a5436:o.wood, wall=o.wall===undefined?0x7a6a4a:o.wall;
  const R=seedRnd(o.seed===undefined?1107:o.seed);
  const B=new GeoBag();
  /* 两侧土墙（矮） */
  [1,-1].forEach(function(s){
    const seg=new THREE.BoxGeometry(w*1.25,1.5,w*0.5);
    seg.translate(s*(w*0.5+w*0.62),0.75,0); B.put(seg,shadeColor(wall,0.9+R()*0.2));
    const cap=new THREE.BoxGeometry(w*1.3,0.2,w*0.56); cap.translate(s*(w*0.5+w*0.62),1.6,0);
    B.put(cap,shadeColor(0x5a4a2c,1.05));
  });
  /* 门柱两根 */
  [1,-1].forEach(function(s){
    const p=new THREE.CylinderGeometry(0.16,0.19,h,8); p.translate(s*w*0.5,h*0.5,0); B.put(p,shadeColor(wood,1.1));
  });
  /* 门楣（横木） */
  const lintel=new THREE.BoxGeometry(w*1.3,0.22,0.28); lintel.translate(0,h+0.1,0); B.put(lintel,shadeColor(wood,1.15));
  /* 柴门顶的小披檐 */
  const eave=new THREE.BoxGeometry(w*1.5,0.14,w*0.8); eave.rotateX(0.3); eave.translate(0,h+0.5,w*0.2); B.put(eave,shadeColor(0x5a4a2c,1.2));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a6a48,emissive:0x100e08,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xc0d8a0:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 柴扉两扇：各自绕门柱转开 */
  function makeLeaf(dir){
    const LB=new GeoBag(), lw=w*0.5;
    for(let i=0;i<5;i++){
      const bar=new THREE.BoxGeometry(0.09,h*0.92,0.09);
      bar.rotateZ((R()-0.5)*0.06); bar.translate(lw*0.12+lw*0.18*i,h*0.48,0);
      LB.put(bar,shadeColor(wood,0.85+R()*0.35));
    }
    for(let i=0;i<3;i++){
      const r=new THREE.BoxGeometry(lw,h*0.08,0.08); r.translate(lw*0.52,h*(0.2+0.3*i),0);
      LB.put(r,shadeColor(wood,1.12));
    }
    const lm=LB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      specular:0x6a6a48,emissive:0x100e08,side:THREE.DoubleSide}));
    lm.frustumCulled=false;
    const hinge=new THREE.Group(); hinge.position.set(dir*w*0.5,0,0);
    const leaf=new THREE.Group(); leaf.add(lm); hinge.add(leaf);
    return {hinge:hinge,leaf:leaf};
  }
  const L=makeLeaf(1), Rl=makeLeaf(-1);
  g.add(L.hinge,Rl.hinge);
  /* 门闩（横木，可抬起） */
  const barGeo=new THREE.BoxGeometry(w*0.95,0.16,0.16); barGeo.translate(-w*0.02,0,0);
  const bar=new THREE.Mesh(barGeo,rimHook(new THREE.MeshPhongMaterial({color:0x8a7040,shininess:8,
    specular:0x6a5a30,emissive:0x100c06}),{c:0xd0c080,i:0.3,p:2.4}));
  bar.frustumCulled=false; bar.position.set(0,h*0.5,0.12); g.add(bar);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  g.update=function(t,k,open){
    const kk=k===undefined?1:k, op=open===undefined?0:open;
    L.hinge.rotation.y=op*1.5; Rl.hinge.rotation.y=-op*1.5;
    bar.position.y=h*0.5+0.28*op; bar.rotation.z=0.22*op;
    bar.position.z=0.12+0.1*op;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,bar};
}

/* —— 小童：矮小的孩童（可与成人区分），奔跑时倾身摆臂 —— */
function makeChildXJ(o){
  o=o||{};
  const g=new THREE.Group();
  const f=makeFigure({pose:'独立',robe:o.robe===undefined?0x6a7a5a:o.robe,belt:0xa8503a,
    collar:0xf0ead8,hat:'幞头',hair:0x1c1a18,scale:o.scale===undefined?0.64:o.scale,
    rim:0.30,rimC:0xc0d8a0,noProp:true});
  g.add(f);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const x0=g.position.x, z0=g.position.z;
  const ph=seedRnd(o.seed===undefined?1111:o.seed)()*6.283;
  g.update=function(t,k,run){
    const kk=k===undefined?1:k, rn=run===undefined?0:run;
    /* run 0→1：从院子里奔到柴门 */
    g.position.x=x0-rn*2.2;
    g.position.z=z0+rn*4.6;
    g.position.y=(o.y===undefined?0:o.y)+Math.abs(Math.sin(t*3.4*rn+ph))*0.16*rn;
    g.rotation.z=0.14*rn*Math.sin(t*3.4+ph);
    g.rotation.y=(o.ry===undefined?0:o.ry)+0.2*rn;
    f.update(t,kk);
  };
  return {g,update:g.update,figure:f};
}

/* —— 垂柳：溪边柳（柳丝随风） —— */
function makeWillowXJ(o){
  o=o||{};
  const h=o.h===undefined?5.2:o.h, R=seedRnd(o.seed===undefined?1117:o.seed);
  const wood=o.wood===undefined?0x40381f:o.wood, leaf=o.leaf===undefined?0x6f9a52:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.5,0],h*0.065,h*0.03,7),wood);
  const tips=[];
  for(let i=0;i<6;i++){
    const a=i/6*6.283+R()*0.5, len=h*(0.34+R()*0.22);
    const p1=[Math.sin(a)*len,h*0.5+len*0.4,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.48,0],p1,h*0.026,h*0.011,6),shadeColor(wood,1.25));
    tips.push(p1);
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<4;k++){
      const sx=tp[0]+(R()-0.5)*0.8, sz=tp[2]+(R()-0.5)*0.8, len=h*(0.32+R()*0.3);
      B.put(limbGeo([sx,tp[1],sz],[sx+(R()-0.5)*0.4,tp[1]-len*0.6,sz+(R()-0.5)*0.4],0.024,0.016,5),
        shadeColor(leaf,0.85+R()*0.3));
      const lf=new THREE.PlaneGeometry(0.58,0.13); lf.rotateZ((R()-0.5)*0.8);
      lf.translate(sx+(R()-0.5)*0.4,tp[1]-len*(0.6+R()*0.3),sz+(R()-0.5)*0.4);
      B.put(lf,shadeColor(0x8fb268,0.8+R()*0.5));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a6a3a,emissive:0x0c1408,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xbcd8a0:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.03+0.09*wd)*Math.sin(t*(0.9+1.5*wd)+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 溪湾村居 —— 溪湾、柴门土墙、垂柳、一只不系船
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0e1c14,c2:0x18301e,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:32,layers:3,peaks:5,seed:2311,color:0x0f2015,atmo:0x35543a,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-10});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  const water=makeWater({size:70,seg:32,amp:0.07,freq:0.16,speed:0.5,flow:[0.3,0.6],spec:1.2,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.35});
  water.mesh.scale.set(1,1,0.62); water.mesh.position.set(3,-0.35,-12); g.add(water.mesh);
  const gate=makeWickerGateXJ({w:3.4,h:2.6,x:-7,y:-1.3,z:-14,seed:1103}); g.add(gate.g);
  const boat=makeMoorlessBoatXJ({x:4,y:-0.25,z:-4,ry:0.4,seed:1105}); g.add(boat.g);
  const willows=[];
  [[-14,0,-8,1119],[9,0,-16,1123]].forEach(function(p,i){
    const w=makeWillowXJ({h:5.0,seed:p[3],scale:1.0}); w.g.position.set(p[0],-1.3,p[2]); g.add(w.g); willows.push(w);
  });
  const wind=makeFlow({n:200,box:[170,20,90],pos:[0,6,-22],color:0xbcd8a0,size:13,speed:2.6,maxA:0.14});
  g.add(wind.points);
  const motes=makeGlow({n:42,box:[180,24,86],pos:[0,9,-22],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,100],pos:[0,8,-46],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x060c08,seed:181,rim:0.14,rimC:0xa0c9b8});
  fg.g.position.set(-16,-1.5,30); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:183,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(16,-1.4,22); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-40,80,26]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); wind.update(t);
    boat.update(t,k,0.35); gate.update(t,k,0);
    const wd=0.3+0.2*Math.sin(t*0.4);
    for(let i=0;i<willows.length;i++)willows[i].update(t,k,wd);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bBuxi(){ // 一 · 篱外春船 —— 篱外谁家不系船，春风吹入钓鱼湾
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0e1c14,c2:0x18301e,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:34,layers:3,peaks:5,seed:2321,color:0x0f2015,atmo:0x365438,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-10});
  ridge.g.position.set(0,0,-94); g.add(ridge.g);
  /* 钓鱼湾：一处水湾（水面 + 湾口） */
  const water=makeWater({size:84,seg:36,amp:0.08,freq:0.15,speed:0.55,flow:[0.32,0.62],spec:1.25,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.35});
  water.mesh.scale.set(1,1,0.6); water.mesh.position.set(2,-0.35,-13); g.add(water.mesh);
  /* 篱与柴门（"篱外"的界） */
  const gate=makeWickerGateXJ({w:3.4,h:2.6,x:-8,y:-1.2,z:-12,seed:1129}); g.add(gate.g);
  /* 不系船：随风漂入湾中（drift 缓动） */
  const boat=makeMoorlessBoatXJ({x:0.5,y:-0.25,z:-1.5,ry:0.5,seed:1131}); g.add(boat.g);
  const willows=[];
  [[-15,0,-6,1133],[7,0,-8,1137],[-2,0,-18,1139]].forEach(function(p,i){
    const w=makeWillowXJ({h:5.4,seed:p[3],scale:1.05}); w.g.position.set(p[0],-1.2,p[2]); g.add(w.g); willows.push(w);
  });
  const wind=makeFlow({n:240,box:[180,22,94],pos:[0,6,-22],color:0xbcd8a0,size:14,speed:2.8,maxA:0.15});
  g.add(wind.points);
  const motes=makeGlow({n:40,box:[170,22,84],pos:[0,9,-20],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,22,96],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060c08,seed:185,rim:0.14,rimC:0xa0c9b8});
  fg.g.position.set(-15,-1.4,19); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:187,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(15,-1.3,17); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-38,78,24]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); wind.update(t);
      const wd=0.4+0.3*Math.sin(t*0.42);
      boat.update(t,k,0.4+0.25*Math.sin(t*0.5));
      gate.update(t,k,0);
      for(let i=0;i<willows.length;i++)willows[i].update(t,k,wd);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(5,0.3,0.09); pluck(4,0.85,0.08); }};
}
function bQuguan(){ // 二（末境·可点击）· 小童去关 —— 小童疑是有村客，急向柴门去却关
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,run:0,open:0,drift:0};
  const grd=makeGround({r:260,c1:0x0d1a12,c2:0x172c1c,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:30,layers:2,peaks:5,seed:2331,color:0x0e1e14,atmo:0x33503a,
    fogK:0.60,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-98); g.add(ridge.g);
  /* 柴门在左前，小童从院内奔来 */
  const gate=makeWickerGateXJ({w:3.6,h:2.7,x:-5.5,y:-1.2,z:-9,ry:0.25,seed:1141}); g.add(gate.g);
  /* 篱墙一段接柴门（"篱外"） */
  const fencePosts=new GeoBag();
  for(let i=0;i<7;i++){
    const x=2.2+i*1.5;
    const p=new THREE.CylinderGeometry(0.08,0.1,1.5,6); p.translate(x,0.75,-6.2); fencePosts.put(p,shadeColor(0x6a5436,0.85+((i%2)*0.25)));
  }
  const fenceMesh=fencePosts.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a6a48,emissive:0x14120c}),{c:0xc0d8a0,i:0.22,p:2.4}));
  fenceMesh.frustumCulled=false; g.add(fenceMesh);
  /* 不系船在湾中（继续漂入） */
  const water=makeWater({size:80,seg:34,amp:0.08,freq:0.15,speed:0.55,flow:[0.32,0.62],spec:1.25,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.35});
  water.mesh.scale.set(1,1,0.6); water.mesh.position.set(6,-0.35,-12); g.add(water.mesh);
  const boat=makeMoorlessBoatXJ({x:4,y:-0.25,z:-2,ry:0.5,seed:1143}); g.add(boat.g);
  /* 小童：从院内奔到柴门 */
  const child=makeChildXJ({x:-1.5,y:-1.2,z:-3,ry:0.6,scale:0.66,seed:1147}); g.add(child.g);
  const willows=[];
  [[-13,0,-4,1151],[10,0,-8,1153]].forEach(function(p,i){
    const w=makeWillowXJ({h:5.4,seed:p[3],scale:1.05}); w.g.position.set(p[0],-1.2,p[2]); g.add(w.g); willows.push(w);
  });
  const wind=makeFlow({n:240,box:[170,22,92],pos:[0,6,-20],color:0xbcd8a0,size:14,speed:2.8,maxA:0.15});
  g.add(wind.points);
  const motes=makeGlow({n:40,box:[160,22,84],pos:[0,9,-18],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,96],pos:[0,8,-44],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.0,w:15,d:6,color:0x060c08,seed:189,rim:0.14,rimC:0xa0c9b8});
  fg.g.position.set(-14,-1.4,14); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x071009,seed:191,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(14,-1.3,12); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-36,76,22]},{c:0x22301f,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.run=Math.min(1,ctl.run+dt/1.8);
        ctl.open=Math.min(1,ctl.open+dt/1.2);
        ctl.drift=Math.min(1,ctl.drift+dt/3.6);
      }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const rn=Math.min(1,ctl.run+0.4*ctl.pulse);
      const op=Math.min(1,ctl.open+0.4*ctl.pulse);
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); wind.update(t);
      const wd=0.4+0.6*rn;
      child.update(t,k,rn);
      gate.update(t,k,op);
      boat.update(t,k,0.3+0.5*ctl.drift);
      for(let i=0;i<willows.length;i++)willows[i].update(t,k,wd);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(3,0.18,0.10); pluck(2,0.40,0.09);
        const fl=$('#flash'); fl.textContent='去却关'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：小童再急一程，柴门再开一分 */
    },clicked:false};
  return api;
}
