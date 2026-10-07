/* ================= 渔家傲·秋思 · 三境场景（大漠金戈·边塞变体：千嶂孤城、燕然未勒、羌管白发） ================= */

/* 孤城门阙：城墙 + 紧闭城门（合批 1 mesh） */
function makeCityGate(o){
  o=o||{};
  const w=o.w===undefined?42:o.w, h=o.h===undefined?7.5:o.h;
  const c=o.color===undefined?0x201610:o.color;
  const B=new GeoBag();
  const left=new THREE.BoxGeometry(w*0.44,h,4.4); left.translate(-w*0.28,h/2,0); B.put(left,c);
  const right=new THREE.BoxGeometry(w*0.44,h,4.4); right.translate(w*0.28,h/2,0); B.put(right,c);
  const arch=new THREE.BoxGeometry(w*0.2,h*0.28,4.4); arch.translate(0,h-h*0.14,0); B.put(arch,shadeColor(c,1.1));
  const door=new THREE.BoxGeometry(w*0.18,h*0.72,0.18); door.translate(0,h*0.36,0); B.put(door,0x0d0805); // 紧闭之门
  const top=new THREE.BoxGeometry(w,1.2,4.6); top.translate(0,h+0.6,0); B.put(top,shadeColor(c,1.15));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3424,emissive:0x080503}),{c:o.rimC===undefined?0xc08a4a:o.rimC,i:0.25,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 烽燧与长烟：墩台 + 柱状长烟（暗红直上） */
function makeSmokeBeacon(o){
  o=o||{};
  const g=new THREE.Group();
  const h=o.h===undefined?10:o.h;
  const B=new GeoBag();
  const t=new THREE.CylinderGeometry(h*0.18,h*0.26,h,8); t.translate(0,h/2,0); B.put(t,0x241a10);
  const top=new THREE.BoxGeometry(h*0.35,h*0.14,h*0.35); top.translate(0,h+h*0.07,0); B.put(top,0x302216);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x403020,emissive:0x080502}),{c:0xb07038,i:0.22,p:2.3})));
  /* 长烟（直上浓烟） */
  const smoke=makeGlow({n:80,box:[6,44,6],pos:[0,h+22,0],color:0x3a2216,size:42,speed:0.06,rise:1,maxA:0.42,add:false});
  smoke.points.renderOrder=4; g.add(smoke.points);
  g.userData.smoke=smoke;
  return g;
}

function bCover(){ // 封面 · 边塞落日
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0d0906,c2:0x1c130a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x0e0a07,atmo:0x46321e,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x080504,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xa87848,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xc89050,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xd8a058,i:0.45,p:[30,70,40]},{c:0x2c2018,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bQianzhang(){ // 一 · 千嶂孤城 —— 重山叠嶂、长烟落日、孤城紧闭
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0c0806,c2:0x1e1208});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 千嶂：重重高山（两层险峰） */
  const ridgeFar=makeRange({r:240,h:72,layers:3,peaks:6,seed:801,color:0x0d0907,atmo:0x442c18,fogK:0.60,glowK:0.07});
  ridgeFar.g.position.set(0,0,-80); g.add(ridgeFar.g);
  const ridgeNear=makeRange({r:180,h:42,layers:2,peaks:4,seed:803,color:0x120c08,atmo:0x50341c,fogK:0.64,glowK:0.08,y:-14});
  ridgeNear.g.position.set(0,0,-48); g.add(ridgeNear.g);
  /* 落日：西天残阳（圆红沉暮） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(11,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xd86830,transparent:true,opacity:0.92,fog:false}));
  sun.position.set(-36,24,-130); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc85020,
    transparent:true,opacity:0.45,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(80,80,1); sunGlow.position.set(-36,24,-130); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 烽火长烟 */
  const beacon=makeSmokeBeacon({h:11}); beacon.position.set(22,0,-36); g.add(beacon);
  /* 孤城（紧闭城门） */
  const city=makeCityGate({w:56,h:8}); city.g.position.set(-2,0,-24); g.add(city.g);
  /* 雁阵南归（无留意） */
  const geese=[];
  const bmat=new THREE.MeshBasicMaterial({color:0x160f0a,side:THREE.DoubleSide});
  for(let i=0;i<7;i++){
    const b=new THREE.Group();
    const w=new THREE.Mesh(new THREE.PlaneGeometry(2.0,0.5),bmat); b.add(w);
    b.position.set(-24+i*7,22+i*1.1,-70-i*5); g.add(b); geese.push(b);
  }
  const mist=makeMist({n:8,spread:[230,22,120],pos:[0,9,-44],scale:76,color:0x9a6840,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080504,seed:145,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xc88048,i:0.46,p:[-50,60,-40]},{c:0x2c1c14,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridgeFar.update(t,0); ridgeNear.update(t,0); mist.update(t,k);
    beacon.userData.smoke.update(t); rk.update(t,k);
    sunGlow.material.opacity=k*(0.38+0.05*Math.sin(t*0.5));
    geese.forEach(function(b,i){
      b.position.x=-24+i*7+((t*1.8)%60);
      b.position.y=22+i*1.1+Math.sin(t*0.9+i)*0.6;
    });
  }};
}
function bZhuojiu(){ // 二 · 燕然未勒 —— 浊酒一杯家万里，燕然未勒归无计
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0b0805,c2:0x1a120a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:38,layers:2,peaks:4,seed:811,color:0x0e0a07,atmo:0x442c18,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 军帐 + 案几（将军饮酒处） */
  const tb=makeTable({w:8.5,d:3.0,h:1.45,wood:0x2e1e12}); tb.g.position.set(0,0,-4.5); g.add(tb.g);
  const zun=makeVessel({type:'樽',mat:'陶',scale:0.95,liquid:true}); zun.g.position.set(-1.8,1.45,-4.6); g.add(zun.g);
  const cup=makeVessel({type:'杯',mat:'陶',scale:0.9,liquid:true}); cup.g.position.set(1.4,1.45,-4.3); g.add(cup.g);
  /* 将军（独酌按剑） */
  const boss=makeFigure({pose:'按剑',robe:0x281a12,belt:0x7a4a20,hat:'幞头',beard:true,face:0.1,scale:1.35,rim:0.55,rimC:0xd89050});
  boss.position.set(0,0,-6.6); g.add(boss);
  /* 营盘篝火 + 哨兵剪影 */
  const braz=makeBrazier({r:1.0,fh:2.2,fw:1.1,light:1.3,lightD:40,embers:20,spark:true});
  braz.g.position.set(8,0,-2); g.add(braz.g);
  const guard=makeFigure({pose:'独立',robe:0x1a120c,hat:'幞头',face:-0.3,scale:1.05,rim:0.35,rimC:0xc07840});
  guard.position.set(11,0,-5); g.add(guard);
  /* 燕然勒石幻影（远处一座陡峰上刻字微光） */
  const cliff=new THREE.Mesh(new THREE.BoxGeometry(6,16,4),
    new THREE.MeshPhongMaterial({color:0x18120c,shininess:4}));
  cliff.position.set(-20,8,-36); cliff.rotation.y=0.3; g.add(cliff);
  const motes=makeGlow({n:60,box:[110,20,70],pos:[0,8,-20],color:0xb88048,size:6,speed:0.04,rise:0,maxA:0.3});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-44],scale:72,color:0x8a5830,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x080504,seed:147,rim:0.14});
  rk.g.position.set(-13,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc08048,i:0.42,p:[30,60,-30]},{c:0x2a1c14,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); braz.update(t,k); motes.update(t); mist.update(t,k);
    boss.update(t,k); guard.update(t,k); zun.update(t,k); cup.update(t,k);
    rk.update(t,k);
  }};
}
function bQiangguan(){ // 三（末境·可点击）· 羌管白发 —— 羌管悠悠霜满地，将军白发征夫泪
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,frost:0};
  const grd=makeGround({r:140,c1:0x12141a,c2:0x222630});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:32,layers:2,peaks:4,seed:821,color:0x0e1014,atmo:0x343a46,fogK:0.60,glowK:0.06});
  ridge.g.position.set(0,0,-76); g.add(ridge.g);
  /* 受降城残段城垣 */
  const city=makeCityGate({w:60,h:7.5}); city.g.position.set(0,0,-24); g.add(city.g);
  /* 寒霜地（白霜光斑，点击后大盛） */
  const frost=makeGlow({n:140,box:[80,3,40],pos:[0,0.8,-12],color:0xd8e4f0,size:4.0,speed:0.02,rise:0,maxA:0.35,add:false});
  g.add(frost.points);
  /* 城头将军（白发）与征夫群像 */
  const general=makeFigure({pose:'按剑',robe:0x20242c,belt:0x7a5a30,hat:'发髻',hair:0xd0d4dc,beard:true,
    face:0,scale:1.25,rim:0.55,rimC:0xb0c4d8});
  general.position.set(-2,7.55,-23.4); g.add(general);
  const soldiers=makeCrowd({n:8,rect:[-18,-25,36,4],seed:823,color:0x161820,rimC:0x9aa8b8,rim:0.28,sMin:0.8,sMax:1.05});
  g.add(soldiers.mesh);
  /* 羌管声波（点击后荡开） */
  const arcs=[];
  for(let i=0;i<3;i++){
    const pts=[];
    for(let k2=0;k2<=22;k2++){
      const a=-1.1+k2/22*2.2, r=2.5+i*3.2;
      pts.push(new THREE.Vector3(12+Math.sin(a)*r,8+Math.cos(a)*r*0.6,-22+Math.cos(a)*r));
    }
    const ln=new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),
      new THREE.LineBasicMaterial({color:0xc8a060,transparent:true,opacity:0.5,fog:false}));
    g.add(ln); arcs.push(ln);
  }
  const burst=makeBurst({n:80,color:0xffd890,pos:[0,9,-22]}); g.add(burst.points);
  const mist=makeMist({n:7,spread:[220,20,120],pos:[0,8,-48],scale:74,color:0x7a8494,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x080a0c,seed:149,rim:0.15});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  addLights(g,{c:0xa0b4cc,i:0.46,p:[-50,90,-40]},{c:0x1e2430,i:0.62});
  const pl=new THREE.PointLight(0xffca7a,1.8,40); pl.position.set(0,9,-20); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.frost=Math.min(1,ctl.frost+dt/2.4);
      ridge.update(t,0); frost.update(t); mist.update(t,k);
      general.update(t,k); soldiers.update(t); rk.update(t,k); burst.update(t);
      frost.mat.uniforms.uMaxA.value=k*0.35*(1+ctl.frost*0.8);
      pl.intensity=k*1.8*(0.35+ctl.frost*0.65*(0.85+0.15*Math.sin(t*2.8)));
      for(let i=0;i<arcs.length;i++){
        const ln=arcs[i];
        const ph=((t*0.35)+i/arcs.length)%1;
        ln.material.opacity=k*0.48*Math.sin(ph*Math.PI)*(1-ph*0.5)*Math.min(1,ctl.frost*2);
        ln.scale.setScalar(0.55+ph*0.85);
      }
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(0,0.1,0.14); pluck(2,0.6,0.12); pluck(3,1.2,0.1);
        const fl=$('#flash'); fl.textContent='将军白发征夫泪'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
