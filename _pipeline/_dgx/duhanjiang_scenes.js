/* ================= 渡汉江 · 三境场景（水墨夜思 · 汉江近乡变体：卷首汉江渡口、岭外音书、近乡情怯）
   本诗专属系统「近乡情怯」：岭外叠嶂、音书断绝（孤雁远飞），渡江渐近乡关。
   末境点击问来人 → 来人迎面走近、诗人侧身欲问又止、乡关与岸村落整体前移（近乡的推进），题字「近乡情怯」。
   与同赛道《淮中晚泊犊头》（春阴孤舟潮生）、《题临安邸》（西湖灯影）不同：本页是岭外叠嶂与近乡之怯。 ================= */

/* —— 渡舟：一叶小舟（船身 + 篷 + 船夫撑篙 + 舟中人） —— */
function makeFerryRaftDH(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(4.4,0.55,1.6); hull.translate(0,0.28,0); B.put(hull,0x3e352a);
  const bow=new THREE.ConeGeometry(0.76,1.25,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(2.2,0.32,0);
  B.put(bow,0x3e352a);
  const stern=new THREE.ConeGeometry(0.74,1.15,4); stern.rotateY(Math.PI/4); stern.rotateZ(Math.PI/2); stern.translate(-2.2,0.32,0);
  B.put(stern,shadeColor(0x3e352a,0.9));
  const canopy=new THREE.CylinderGeometry(0.8,0.8,1.6,10,1,true,0,Math.PI); canopy.rotateZ(Math.PI/2); canopy.rotateY(Math.PI/2);
  canopy.translate(-0.9,0.68,0); B.put(canopy,0x5a4c32);
  const seat=new THREE.BoxGeometry(1.1,0.1,1.25); seat.translate(0.6,0.58,0); B.put(seat,0x4a3e2c);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x4a4434,emissive:0x0a0806,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xb0c0d4:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 船夫撑篙 */
  const boatman=makeFigure({pose:'独立',robe:0x4a4436,belt:0x8a7a52,collar:0xd8d4c4,hat:'斗笠',
    hair:0x2a2620,scale:1.0,rim:0.34,rimC:0xa8bccc,noProp:true});
  boatman.position.set(1.5,0.5,0); boatman.rotation.y=1.2; g.add(boatman);
  const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.045,0.05,3.2,6),
    new THREE.MeshPhongMaterial({color:0x6a5a34,shininess:8,specular:0x4a4020,emissive:0x0c0a04}));
  pole.position.set(2.5,1.4,0.3); pole.rotation.z=-0.35; g.add(pole);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const ph=seedRnd(o.seed===undefined?801:o.seed)()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.position.y=(o.y===undefined?0:o.y)+0.06*Math.sin(t*1.1+ph)*kk;
    g.rotation.z=0.03*Math.sin(t*0.85+ph)*kk;
    boatman.update(t,kk); };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 乡关村落：远处村舍一片（屋顶 + 墙 + 树 + 灯），成组便于"渐近"推进 —— */
function makeVillageDH(o){
  o=o||{};
  const n=o.n===undefined?9:o.n, R=seedRnd(o.seed===undefined?809:o.seed);
  const w=o.w===undefined?40:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*14, wh=1.6+R()*1.4, ww=2.0+R()*1.6;
    const body=new THREE.BoxGeometry(ww,wh,ww*0.8); body.translate(x,wh*0.5,z); B.put(body,0x3a3430);
    const r1=new THREE.BoxGeometry(ww*1.14,0.16,ww*0.5); r1.rotateX(0.42); r1.translate(x,wh+0.2,z+ww*0.2); B.put(r1,0x2a2622);
    const r2=new THREE.BoxGeometry(ww*1.14,0.16,ww*0.5); r2.rotateX(-0.42); r2.translate(x,wh+0.2,z-ww*0.2); B.put(r2,0x232019);
  }
  /* 村树 */
  for(let i=0;i<5;i++){
    const x=(R()-0.5)*w*0.9, z=(R()-0.5)*18;
    const tr=new THREE.CylinderGeometry(0.16,0.22,2.2,6); tr.translate(x,1.1,z); B.put(tr,0x2c2418);
    for(let k=0;k<3;k++){
      const rr=1.0+R()*0.7;
      const s=new THREE.SphereGeometry(rr,7,6); s.scale(1.2,0.8,1.0);
      s.translate(x+(R()-0.5)*1.2,2.5+R()*0.9,z+(R()-0.5)*1.2);
      B.put(s,shadeColor(0x2a4428,0.8+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2e3844,emissive:0x0a0c10}),{c:o.rimC===undefined?0xa8bccc:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 村灯（几点暖光，只调 scale） */
  const lamps=[];
  for(let i=0;i<5;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc070,transparent:true,
      opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set((R()-0.5)*w*0.9,0.9+R()*0.8,(R()-0.5)*12);
    s.scale.set(2.6,2.6,1); s.renderOrder=3; g.add(s); lamps.push({s:s,ph:R()*6.283});
  }
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  const z0=g.position.z, x0=g.position.x;
  return {g,update:function(t,near){
    const nr=near===undefined?0:near;
    g.position.z=z0+nr*7.0;            /* 乡关渐近：整组向相机推进 */
    for(let i=0;i<lamps.length;i++){
      const L=lamps[i];
      const k2=1+0.06*Math.sin(t*2.0+L.ph);
      L.s.scale.set(2.6*k2,2.6*k2,1);
    }
  }};
}

/* —— 来人：从乡关方向迎面走来的人（可"欲问又止"地顿住） —— */
function makeTravelerDH(o){
  o=o||{};
  const g=new THREE.Group();
  const f=makeFigure({pose:'独立',robe:o.robe===undefined?0x4a4a44:o.robe,belt:0x8a7a52,
    collar:0xd8d8cc,hat:'幞头',hair:0x1c1a18,scale:o.scale===undefined?1.05:o.scale,
    rim:0.36,rimC:0xa8bccc,noProp:true});
  g.add(f);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const x0=g.position.x, z0=g.position.z;
  const ph=seedRnd(o.seed===undefined?811:o.seed)()*6.283;
  g.update=function(t,k,adv,halt){
    const kk=k===undefined?1:k, a=adv===undefined?0:adv, ht=halt===undefined?0:halt;
    /* 走近：a 从 0→1；临近时"欲问又止"：在 ht 处顿住并前后微晃 */
    g.position.z=z0+a*7.5;
    g.position.x=x0-a*1.2;
    g.rotation.y=(o.ry===undefined?0:o.ry)+(0.10*ht)*Math.sin(t*1.6+ph);
    f.update(t,kk);
  };
  return {g,update:g.update,figure:f};
}

/* —— 孤雁：高空一只失群雁（"音书断"的注脚），合批 1 mesh —— */
function makeGooseDH(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, B=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,8,6); body.scale(2.0,0.75,0.7); B.put(body,0x3a3f46);
  const head=new THREE.SphereGeometry(0.13,7,6); head.translate(0.62,0.10,0); B.put(head,0x2e333a);
  const beak=new THREE.ConeGeometry(0.05,0.26,5); beak.rotateZ(-Math.PI/2); beak.translate(0.85,0.08,0); B.put(beak,0x8a7a3a);
  [1,-1].forEach(function(sd){
    const w=new THREE.PlaneGeometry(1.5,0.34); w.rotateZ(sd*0.22); w.translate(-0.15,0.14,sd*0.42);
    B.put(w,0x454b54);
  });
  const tail=new THREE.ConeGeometry(0.10,0.5,5); tail.rotateZ(1.35); tail.translate(-0.62,0.06,0); B.put(tail,0x333840);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    emissive:0x080a0e,side:THREE.DoubleSide}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?817:o.seed)()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.10*Math.sin(t*1.1+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 汉江渡口 —— 江水横陈、远山叠嶂、一叶渡舟
  const g=new THREE.Group();
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c24,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:54,layers:3,peaks:6,seed:2011,color:0x0a0f16,atmo:0x1e2836,
    fogK:0.64,glowK:0.04,glow:0x9fb3cc,y:-12});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  const water=makeWater({size:170,seg:46,amp:0.09,freq:0.10,speed:0.45,flow:[0.2,0.55],spec:1.3,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2c3e54,moonDir:[-40,90,-160],y:-0.9});
  water.mesh.position.set(0,-0.9,-32); g.add(water.mesh);
  const raft=makeFerryRaftDH({x:-2,y:-0.55,z:-6,ry:0.35,seed:803}); g.add(raft.g);
  const village=makeVillageDH({n:8,w:34,x:6,y:-1.3,z:-58,seed:807}); g.add(village.g);
  const goose=makeGooseDH({scale:1.15}); goose.g.position.set(-16,10,-30); g.add(goose.g);
  const motes=makeGlow({n:46,box:[200,26,92],pos:[0,9,-26],color:0xa8bccc,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[250,28,120],pos:[0,9,-56],scale:80,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:19,d:7,color:0x070a0d,seed:131,rim:0.16,rimC:0x9fb0c9});
  fg.g.position.set(-18,-1.5,40); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x090d10,seed:133,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(17,-1.4,26); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-44,70,28]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    raft.update(t,k); village.update(t,0.05); goose.update(t,k);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bLingwai(){ // 一 · 岭外音书 —— 岭外音书断，经冬复历春
  const g=new THREE.Group();
  const grd=makeGround({r:290,c1:0x0b0f13,c2:0x141c24,y:-1.2}); g.add(grd.mesh);
  /* 岭外叠嶂：四层山脊，一层比一层远（"岭外"之远） */
  const r1=makeRange({r:330,h:78,layers:3,peaks:7,seed:2021,color:0x090e15,atmo:0x1b2532,fogK:0.68,glowK:0.03,glow:0x8fa8c4,y:-14});
  r1.g.position.set(0,0,-132); g.add(r1.g);
  const r2=makeRange({r:250,h:56,layers:3,peaks:6,seed:2022,color:0x0a1018,atmo:0x1e2836,fogK:0.66,glowK:0.04,glow:0x93acc8,y:-11});
  r2.g.position.set(0,0,-92); g.add(r2.g);
  const r3=makeRange({r:180,h:36,layers:2,peaks:5,seed:2023,color:0x0c121a,atmo:0x222e3c,fogK:0.62,glowK:0.05,glow:0x9ab0cc,y:-7});
  r3.g.position.set(0,0,-58); g.add(r3.g);
  const water=makeWater({size:150,seg:44,amp:0.09,freq:0.10,speed:0.45,flow:[0.2,0.55],spec:1.3,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2c3e54,moonDir:[-40,90,-160],y:-0.9});
  water.mesh.position.set(0,-0.9,-30); g.add(water.mesh);
  const raft=makeFerryRaftDH({x:1,y:-0.55,z:-8,ry:-0.3,seed:813}); g.add(raft.g);
  /* 音书断：孤雁远飞（雁足不传书） */
  const goose=makeGooseDH({scale:1.3}); goose.g.position.set(-20,11,-24); g.add(goose.g);
  const goose2=makeGooseDH({scale:1.0}); goose2.g.position.set(-13,9.4,-16); g.add(goose2.g);
  /* 经冬复历春：岸上初绿与几点桃花（冬去春来） */
  const bank=makeGrassFieldDHLocal(g);
  const motes=makeGlow({n:44,box:[190,26,90],pos:[0,9,-24],color:0xa8bccc,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,26,110],pos:[0,9,-54],scale:78,color:0x22303c,op:0.12});
  g.add(mist.g);
  const crowd=makeCrowd({n:2,rect:[-26,6,14,6],seed:821,color:0x121a22,rimC:0x9fb0c9,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x070a0d,seed:137,rim:0.16,rimC:0x9fb0c9});
  fg.g.position.set(-16,-1.4,24); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x090d10,seed:139,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(16,-1.3,20); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-42,68,26]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      r1.update(t,0); r2.update(t,0); r3.update(t,0);
      water.update(t); mist.update(t,k); motes.update(t); crowd.update(t);
      raft.update(t,k); goose.update(t,k); goose2.update(t,k);
      bank.update(t,k,0.3);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(2,0.4,0.08); pluck(4,1.0,0.07); }};
}
/* 岸上初绿：局部小函数（本页专用，避免与其它 builder 名冲突） */
function makeGrassFieldDHLocal(g){
  const R=seedRnd(823), B=new GeoBag();
  for(let i=0;i<700;i++){
    const hh=0.4+R()*0.7, x=(R()-0.5)*120, z=2+R()*16;
    const bl=new THREE.ConeGeometry(0.045,hh,4);
    bl.rotateZ((R()-0.5)*0.3); bl.rotateY(R()*6.283);
    bl.translate(x,hh*0.5,z);
    B.put(bl,shadeColor(0x46613a,0.7+R()*0.6));
  }
  for(let i=0;i<9;i++){
    const x=(R()-0.5)*100, z=4+R()*12;
    const tr=new THREE.CylinderGeometry(0.08,0.11,1.0,5); tr.translate(x,0.5,z); B.put(tr,0x4a3a26);
    for(let k=0;k<4;k++){
      const rr=0.14+R()*0.08;
      const fl=new THREE.SphereGeometry(rr,6,5); fl.scale(1.15,0.75,1.15);
      fl.translate(x+(R()-0.5)*0.6,1.0+R()*0.5,z+(R()-0.5)*0.6);
      B.put(fl,shadeColor(0xe0a0b0,0.85+R()*0.3));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3a24,emissive:0x0a0c08,side:THREE.DoubleSide}),{c:0xa8d8a0,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  g.add(mesh);
  const ph=R()*6.283;
  return {update:function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    mesh.rotation.z=(0.004+0.012*wd)*Math.sin(t*0.5+ph)*kk; }};
}
function bJinxiang(){ // 二（末境·可点击）· 近乡情怯 —— 近乡情更怯，不敢问来人
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,adv:0,near:0};
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c24,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:44,layers:3,peaks:6,seed:2031,color:0x090e15,atmo:0x1c2634,
    fogK:0.64,glowK:0.04,glow:0x93acc8,y:-12});
  ridge.g.position.set(0,0,-112); g.add(ridge.g);
  const water=makeWater({size:150,seg:44,amp:0.09,freq:0.10,speed:0.45,flow:[0.2,0.55],spec:1.3,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2c3e54,moonDir:[-40,90,-160],y:-0.9});
  water.mesh.position.set(0,-0.9,-30); g.add(water.mesh);
  /* 舟中诗人（背影，向着乡关） */
  const raft=makeFerryRaftDH({x:-1.5,y:-0.55,z:-5,ry:0.2,seed:829}); g.add(raft.g);
  const poet=makeFigure({pose:'独立',robe:0x2e3648,belt:0x9fb0c9,collar:0xdfe6f0,hat:'幞头',
    hair:0x14161f,scale:1.12,rim:0.46,rimC:0x9fb0c9,noProp:true});
  poet.position.set(-1.8,-0.05,-4.2); poet.rotation.y=Math.PI; g.add(poet);
  /* 乡关村落（可前移）与北岸 */
  const village=makeVillageDH({n:10,w:38,x:4,y:-1.2,z:-52,seed:831}); g.add(village.g);
  const bank=makeGrassFieldDHLocal(g);
  /* 来人：从乡关方向迎面而来 */
  const traveler=makeTravelerDH({x:2.2,y:-1.2,z:-20,ry:0.05,scale:1.08,seed:839}); g.add(traveler.g);
  const traveler2=makeTravelerDH({x:-6.5,y:-1.2,z:-26,ry:0.2,scale:0.95,robe:0x40403a,seed:841}); g.add(traveler2.g);
  const motes=makeGlow({n:42,box:[190,24,88],pos:[0,9,-22],color:0xa8bccc,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,26,110],pos:[0,9,-52],scale:78,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.2,w:17,d:7,color:0x070a0d,seed:143,rim:0.16,rimC:0x9fb0c9});
  fg.g.position.set(-15,-1.4,18); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x090d10,seed:145,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(15,-1.3,16); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-40,66,24]},{c:0x1a222c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.adv=Math.min(1,ctl.adv+dt/3.0); ctl.near=Math.min(1,ctl.near+dt/3.4); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const ad=ctl.adv+0.35*ctl.pulse;
      const nr=ctl.near+0.3*ctl.pulse;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      raft.update(t,k);
      /* 诗人：欲问又止——侧身、微顿（只转朝向） */
      poet.update(t,k);
      poet.rotation.y=Math.PI-0.55*Math.min(1,ad);
      village.update(t,nr);
      bank.update(t,k,0.3);
      traveler.update(t,k,ad,Math.min(1,ad*1.6));
      traveler2.update(t,k,ad*0.7,Math.min(1,ad));
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(3,0.00,0.12); pluck(1,0.35,0.10); pluck(4,0.75,0.08);
        const fl=$('#flash'); fl.textContent='近乡情怯'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：来人再近一步，乡关再近一程 */
    },clicked:false};
  return api;
}
