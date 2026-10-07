/* ================= 过华清宫 · 三境场景（夜宴金彩 · 骊山华清变体：卷首骊山晚照、长安回望、一骑红尘）
   本诗专属系统「千门次第开 + 一骑红尘」：骊山绝顶千重宫门依次洞开（门扇可动），
   驿道上一骑扬尘直上（红尘随马走）；末境点击红尘 → 驿马加速、千门大开、妃子一笑。
   赛道同组但面貌不同：本页以骊山晚照的宫阙、锦绣山色与驿道红尘为主角。 ================= */

/* —— 骊山锦绣：山坡上层层叠叠的宫树楼台（帐形铺在山腰，屋顶暖赭、松柏深绿），合批 1 mesh —— */
function makeBrocadeGHQ(o){
  o=o||{};
  const n=o.n===undefined?330:o.n, R=seedRnd(o.seed===undefined?91:o.seed);
  const halfW=o.halfW===undefined?100:o.halfW, top=o.top===undefined?24:o.top;
  const depth=o.depth===undefined?30:o.depth, B=new GeoBag();
  const roofs=[0xa8702e,0xc08a3a,0x8a5426,0xb07c34];
  const greens=[0x2f4a26,0x38562c,0x27401f];
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*2*halfW;
    const t=Math.max(0,1-Math.abs(x)/halfW);
    const cap=top*Math.pow(t,1.08);
    const y=R()*cap;
    const z=(R()-0.5)*depth*(0.5+0.6*t);
    if(R()<0.30){                        /* 松柏：深绿锥（山上的宫树） */
      const hh=1.5+R()*2.2, rr=0.55+R()*0.5;
      const cn=new THREE.ConeGeometry(rr,hh,6); cn.translate(x,y+hh*0.5,z);
      B.put(cn,shadeColor(greens[(i*3)%greens.length],0.8+R()*0.4));
    }else{                               /* 楼台：屋身 + 四坡屋顶（锦绣之"堆"） */
      const rw=1.0+R()*1.6, rh=0.9+R()*1.1;
      const bd=new THREE.BoxGeometry(rw*1.5,rh,rw*1.3); bd.translate(x,y+rh*0.5,z);
      B.put(bd,shadeColor(0x3a2818,0.8+R()*0.5));
      const rf=new THREE.ConeGeometry(rw*1.25,rh*0.9,4); rf.rotateY(Math.PI/4);
      rf.translate(x,y+rh+rh*0.45,z);
      B.put(rf,shadeColor(roofs[(i*5)%roofs.length],0.72+R()*0.5));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a22,emissive:0x120a06,side:THREE.DoubleSide}),{c:0xd8a060,i:0.26,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh};
}

/* —— 长安城郭：城墙 + 女墙 + 坊市屋顶 + 点点窗火（合批 1 mesh + 1 sprite 层） —— */
function makeCityGHQ(o){
  o=o||{};
  const w=o.w===undefined?150:o.w, h=o.h===undefined?8:o.h;
  const R=seedRnd(o.seed===undefined?53:o.seed), B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,h,3.2); wall.translate(0,h/2,0); B.put(wall,0x2a1e14);
  const cap=new THREE.BoxGeometry(w*1.01,0.36,3.6); cap.translate(0,h+0.18,0); B.put(cap,shadeColor(0x3a2a1c,1.15));
  const nm=Math.floor(w/3.0);
  for(let i=0;i<nm;i++){
    const m=new THREE.BoxGeometry(1.5,1.1,3.5); m.translate(-w/2+1.5+i*3.0,h+0.9,0); B.put(m,0x2a1e14);
  }
  /* 城内坊市屋顶（层层递退） */
  for(let r=0;r<3;r++){
    for(let i=0;i<14;i++){
      const bx=(R()-0.5)*w*0.9, bz=-4-r*7-R()*3;
      const bw=5+R()*6, bh=2.6-r*0.5;
      const body=new THREE.BoxGeometry(bw,bh,bw*0.8); body.translate(bx,bh/2,bz); B.put(body,shadeColor(0x2c2016,0.8+R()*0.5));
      const roof=new THREE.ConeGeometry(bw*0.82,1.5,4); roof.rotateY(Math.PI/4); roof.translate(bx,bh+0.6,bz); B.put(roof,shadeColor(0x3a2618,0.9+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3020,emissive:0x0a0704}),{c:0xc8a060,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 万家灯火：一片暖点（Sprite 层，只调 scale 不碰 opacity） */
  const lights=new THREE.Group();
  for(let i=0;i<10;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffbe6a,transparent:true,
      opacity:0.26,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set((R()-0.5)*w*0.86, 1.6+R()*6, -3-R()*18);
    s.scale.set(9,5,1); s.renderOrder=3; lights.add(s);
  }
  g.add(lights);
  g.position.y=o.y===undefined?0:o.y;
  return {g,mesh};
}

/* —— 千门次第开：一排宫门（门楼合批 1 mesh + 12 扇可动门扇） —— */
function makeGateRowGHQ(o){
  o=o||{};
  const n=o.n===undefined?6:o.n, w=o.w===undefined?3.4:o.w, h=o.h===undefined?3.6:o.h;
  const gap=o.gap===undefined?5.6:o.gap;
  const wood=o.wood===undefined?0x2e1e12:o.wood, tile=o.tile===undefined?0x4a3018:o.tile;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(i-(n-1)/2)*gap;
    [1,-1].forEach(function(s){
      const p=new THREE.CylinderGeometry(0.18,0.22,h,8); p.translate(x+s*w/2,h/2,0); B.put(p,shadeColor(wood,1.05));
    });
    const beam=new THREE.BoxGeometry(w+0.8,0.4,0.66); beam.translate(x,h,0); B.put(beam,shadeColor(wood,1.3));
    const roof=new THREE.ConeGeometry(w*0.92,1.25,4); roof.rotateY(Math.PI/4); roof.translate(x,h+0.95,0); B.put(roof,tile);
    const ridge=new THREE.BoxGeometry(w*1.05,0.14,0.5); ridge.translate(x,h+1.58,0); B.put(ridge,shadeColor(tile,1.4));
    const plq=new THREE.BoxGeometry(0.95,0.52,0.12); plq.translate(x,h-0.66,0.36); B.put(plq,shadeColor(0x5a4426,1.2));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x6a5a3a,emissive:0x0c0804}),{c:0xe0b070,i:0.40,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 门扇：每门两扇，绕门轴开合 */
  const panels=[];
  for(let i=0;i<n;i++){
    const x=(i-(n-1)/2)*gap;
    [1,-1].forEach(function(s,si){
      const pg=new THREE.BoxGeometry(w*0.47,h*0.84,0.14);
      pg.translate(s*w*0.235,h*0.43,0);
      const pm=new THREE.MeshPhongMaterial({color:0x6e2114,shininess:26,specular:0x9a5a3a,emissive:0x1c0704});
      const pmesh=new THREE.Mesh(pg,pm); pmesh.frustumCulled=false;
      const pivot=new THREE.Group(); pivot.position.set(x,0,0); pivot.add(pmesh);
      g.add(pivot);
      panels.push({pivot:pivot,dir:si?1:-1,i:i});
    });
  }
  g.update=function(t,open){
    const oo=open===undefined?0:open;
    for(let i=0;i<panels.length;i++){
      const p=panels[i];
      const k=clamp(oo*1.55-p.i*0.13,0,1);
      p.pivot.rotation.y=p.dir*k*1.32;
    }
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,panels};
}

/* —— 宫灯：一盏暖黄宫灯（灯体合批 1 mesh + 一团暖光，只调 scale 不动 opacity） —— */
function makePalaceLampGHQ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, B=new GeoBag();
  const pts=[[0.02,-0.34],[0.30,-0.34],[0.40,-0.16],[0.42,0.06],[0.36,0.30],[0.22,0.40],[0.02,0.42]];
  B.put(new THREE.LatheGeometry(pts.map(function(p){return new THREE.Vector2(p[0],p[1]);}),16),
    o.paper===undefined?0xe8b866:o.paper);
  const capT=new THREE.CylinderGeometry(0.13,0.17,0.10,10); capT.translate(0,0.47,0); B.put(capT,0x4a3520);
  const capB=new THREE.CylinderGeometry(0.17,0.13,0.10,10); capB.translate(0,-0.39,0); B.put(capB,0x4a3520);
  const rim=new THREE.TorusGeometry(0.41,0.03,6,18); rim.rotateX(Math.PI/2); rim.translate(0,0.06,0); B.put(rim,0x6a4a26);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:18,
    specular:0x7a5a2a,emissive:0x3a2408,side:THREE.DoubleSide}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc478,transparent:true,
    opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  gl.scale.set(4.2,4.2,1); gl.renderOrder=3; g.add(gl);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?7:o.seed)()*6.283;
  g.update=function(t,k){
    gl.scale.setScalar(4.2*(0.94+0.06*Math.sin(t*2.4+ph)));
    mesh.rotation.y=0.05*Math.sin(t*0.7+ph);
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,glow:gl};
}

/* —— 一骑红尘：驿马与驿使（马身 1 mesh + 左右两对腿 2 mesh + 骑者 1 mesh） —— */
function makeHorseRiderGHQ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const coat=o.coat===undefined?0x3c2a1e:o.coat, cloth=o.cloth===undefined?0x6e2a1e:o.cloth;
  const g=new THREE.Group();
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.62,10,8); body.scale(1.75,0.95,0.95); body.translate(0,1.30,0); B.put(body,coat);
  const chest=new THREE.SphereGeometry(0.45,9,7); chest.scale(1.0,1.06,0.98); chest.translate(0.80,1.34,0); B.put(chest,shadeColor(coat,1.14));
  const rump=new THREE.SphereGeometry(0.45,9,7); rump.scale(1.0,1.02,0.98); rump.translate(-0.80,1.32,0); B.put(rump,shadeColor(coat,0.9));
  const neck=new THREE.CylinderGeometry(0.19,0.31,0.94,8); neck.rotateZ(-0.62); neck.translate(1.18,1.86,0); B.put(neck,coat);
  const head=new THREE.SphereGeometry(0.21,8,7); head.scale(1.5,0.86,0.8); head.translate(1.66,2.16,0); B.put(head,shadeColor(coat,1.18));
  const muzzle=new THREE.BoxGeometry(0.34,0.18,0.20); muzzle.translate(1.98,2.05,0); B.put(muzzle,shadeColor(coat,0.8));
  const mane=new THREE.ConeGeometry(0.13,0.78,6); mane.rotateZ(-0.52); mane.translate(1.20,2.20,0); B.put(mane,0x1a120c);
  const tail=new THREE.ConeGeometry(0.15,0.80,6); tail.rotateZ(-1.05); tail.translate(-1.34,1.34,0); B.put(tail,0x1a120c);
  const bodyMesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:18,
    specular:0x6a5a40,emissive:0x0a0704}),{c:0xe8bc7c,i:0.46,p:2.4}));
  bodyMesh.frustumCulled=false; g.add(bodyMesh);
  /* 四腿：左右各一对，合并后各 1 mesh（奔腾时前后摆） */
  const legs={r:null,l:null};
  [1,-1].forEach(function(sd){
    const L=new GeoBag();
    [[0.66,0.30],[-0.66,-0.30]].forEach(function(lg){
      const upper=new THREE.CylinderGeometry(0.105,0.085,0.74,6); upper.translate(lg[0],0.86,0.17*sd); L.put(upper,shadeColor(coat,0.96));
      const lower=new THREE.CylinderGeometry(0.075,0.06,0.64,6); lower.translate(lg[0]+lg[1]*0.5,0.34,0.17*sd); L.put(lower,shadeColor(coat,0.76));
      const hoof=new THREE.CylinderGeometry(0.085,0.095,0.13,6); hoof.translate(lg[0]+lg[1]*0.6,0.07,0.17*sd); L.put(hoof,0x2a221c);
    });
    const m=L.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
      specular:0x4a3a28,emissive:0x080604}),{c:0xd8a868,i:0.34,p:2.3}));
    m.frustumCulled=false; g.add(m); legs[sd>0?'r':'l']=m;
  });
  /* 驿使：斗篷 + 身躯 + 头 + 幞头（合批 1 mesh） */
  const R2=new GeoBag();
  const cloak=new THREE.ConeGeometry(0.46,1.10,9); cloak.translate(0,2.06,0); R2.put(cloak,cloth);
  const torso=new THREE.CylinderGeometry(0.20,0.27,0.64,8); torso.translate(0,2.38,0); R2.put(torso,0x3a2c22);
  const belt=new THREE.TorusGeometry(0.24,0.05,5,14); belt.rotateX(Math.PI/2); belt.translate(0,2.14,0); R2.put(belt,0x8a6a34);
  const hd=new THREE.SphereGeometry(0.17,8,7); hd.translate(0,2.90,0); R2.put(hd,0xd8b189);
  const hat=new THREE.SphereGeometry(0.20,8,6); hat.scale(1.05,0.85,1.05); hat.translate(0,3.02,0); R2.put(hat,0x1a1410);
  const arm=new THREE.CylinderGeometry(0.065,0.055,0.52,6); arm.rotateZ(-1.15); arm.translate(0.30,2.56,0); R2.put(arm,0x3a2c22);
  const rider=R2.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x5a4a34,emissive:0x0a0604}),{c:0xe8c088,i:0.42,p:2.4}));
  rider.frustumCulled=false; g.add(rider);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?11:o.seed)()*6.283;
  g.update=function(t,k,speed){
    const sp=speed===undefined?1:speed;
    legs.r.rotation.x=0.78*Math.sin(t*9.2*sp+ph);
    legs.l.rotation.x=0.78*Math.sin(t*9.2*sp+ph+Math.PI);
    bodyMesh.position.y=0.055*Math.sin(t*18.4*sp+ph);
    rider.position.y=0.05*Math.sin(t*18.4*sp+ph+0.6);
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh:bodyMesh,legs:legs};
}

/* —— 红尘：驿道上扬起的红褐色尘雾（复用引擎定向流 + 尘团 sprite，随马而行） —— */
function makeDustGHQ(o){
  o=o||{};
  const flow=makeFlow({n:o.n===undefined?420:o.n, box:[o.w===undefined?30:o.w,o.h===undefined?7:o.h,o.d===undefined?12:o.d],
    pos:[0,1.7,0], color:o.color===undefined?0x9a5a34:o.color, size:o.size===undefined?15:o.size, speed:o.speed===undefined?2.8:o.speed,
    maxA:o.maxA===undefined?0.30:o.maxA});
  const puff=makeMist({n:5,spread:[9,4,6],pos:[0,1.6,0],scale:7,color:0x7a4a2e,op:0.20});
  const g=new THREE.Group(); g.add(flow.points,puff.g);
  return {g,update:function(t,k){ flow.update(t); puff.update(t,k); }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 骊山晚照 —— 晚霞里的骊山宫阙，山下长安城郭一片灯火
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0d0906,c2:0x1c1310,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:52,layers:3,peaks:4,seed:211,color:0x140d07,atmo:0x4a3218,
    fogK:0.62,glowK:0.09,glow:0xe0a860,y:-12});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  const sun=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf0b060,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sun.scale.set(170,66,1); sun.position.set(-70,30,-130); sun.renderOrder=-7; g.add(sun);
  const brocade=makeBrocadeGHQ({n:260,halfW:96,top:22,depth:28,seed:93}); brocade.g.position.set(-4,0,-74); g.add(brocade.g);
  const gates=makeGateRowGHQ({n:5,gap:5.2,h:3.4}); gates.g.position.set(-2,-1.0,-50); gates.g.scale.setScalar(1.15); g.add(gates.g);
  const city=makeCityGHQ({w:150,h:8,seed:53}); city.g.position.set(6,-1.4,-16); g.add(city.g);
  const lamps=[];
  [[-13,3.4,-48],[13,3.4,-48]].forEach(function(p){
    const L=makePalaceLampGHQ({scale:1.15,seed:p[0]+40});
    L.g.position.set(p[0],p[1],p[2]); g.add(L.g); lamps.push(L);
  });
  const crowd=makeCrowd({n:5,rect:[-6,-52,16,10],seed:67,color:0x1a120c,rimC:0xe0b070,rim:0.24});
  g.add(crowd.mesh);
  const motes=makeGlow({n:52,box:[210,34,120],pos:[0,10,-30],color:0xf0c080,size:7,speed:0.03,rise:0,maxA:0.17});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[260,32,150],pos:[0,12,-60],scale:84,color:0x30200f,op:0.13});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:4.2,w:20,d:8,color:0x070503,seed:31,rim:0.16,rimC:0xe0b070});
  fg.g.position.set(-19,-1.6,44); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:3.2,w:16,d:6,color:0x060403,seed:33,rim:0.14,rimC:0xd8a860});
  fg2.g.position.set(18,-1.4,20); g.add(fg2.g);
  addLights(g,{c:0xf0c078,i:0.52,p:[-60,80,30]},{c:0x2a1c10,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
    gates.update(t,0.55);
    for(let i=0;i<lamps.length;i++)lamps[i].update(t,k);
    fg.update(t,k); fg2.update(t,k);
    sun.material.opacity=0.30*k*(0.92+0.08*Math.sin(t*0.5));
  }};
}
function bChangan(){ // 一 · 长安回望 —— 长安回望绣成堆，山顶千门次第开
  const g=new THREE.Group();
  const ctl={t:0,open:0};
  const grd=makeGround({r:250,c1:0x0c0806,c2:0x1a1210,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:54,layers:3,peaks:4,seed:221,color:0x130c07,atmo:0x452f16,
    fogK:0.62,glowK:0.08,glow:0xdca058,y:-11});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  /* 绣成堆：骊山山腰的宫树花木（远望如锦绣堆叠） */
  const brocade=makeBrocadeGHQ({n:380,halfW:112,top:26,depth:32,seed:97}); brocade.g.position.set(-2,0,-80); g.add(brocade.g);
  /* 山顶千门次第开 */
  const gates=makeGateRowGHQ({n:6,gap:5.8,h:3.6}); gates.g.position.set(-2,16.2,-56); gates.g.scale.setScalar(1.25); g.add(gates.g);
  const platform=new THREE.Mesh(new THREE.BoxGeometry(52,1.2,11),
    new THREE.MeshPhongMaterial({color:0x2e2116,shininess:8,specular:0x4a3a24,emissive:0x0a0704}));
  platform.position.set(-2,15.6,-56); g.add(platform);
  const lamps=[];
  [[-16,17.7,-52],[-5,17.7,-52],[6,17.7,-52],[17,17.7,-52]].forEach(function(p){
    const L=makePalaceLampGHQ({scale:1.2,seed:p[0]+60});
    L.g.position.set(p[0],p[1],p[2]); g.add(L.g); lamps.push(L);
  });
  /* 宫人两个（千门开处） */
  const w1=makeFigure({pose:'独立',robe:0x4a3420,belt:0xd8a24a,hat:'幞头',hair:0x14100c,scale:1.0,
    rim:0.48,rimC:0xe8c088,noProp:true});
  w1.position.set(-4.4,16.2,-49); w1.rotation.y=2.9; g.add(w1);
  const w2=makeFigure({pose:'独立',robe:0x50381c,belt:0xc08a3a,hat:'幞头',hair:0x14100c,scale:0.96,
    rim:0.44,rimC:0xe8c088,noProp:true});
  w2.position.set(3.6,16.2,-49); w2.rotation.y=3.3; g.add(w2);
  /* 长安城郭在近前（回望之所） */
  const city=makeCityGHQ({w:170,h:8.6,seed:59}); city.g.position.set(2,0,10); g.add(city.g);
  const crowd=makeCrowd({n:4,rect:[-30,-4,26,10],seed:71,color:0x181008,rimC:0xe0b070,rim:0.22});
  g.add(crowd.mesh);
  const motes=makeGlow({n:48,box:[200,32,120],pos:[0,10,-24],color:0xf0c080,size:7,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[250,30,140],pos:[0,11,-56],scale:80,color:0x2c1e0e,op:0.13});
  g.add(mist.g);
  /* 前景：城头女墙（近相机，做画面的框） */
  const fg=makeForeground({kind:'栏杆',w:26,h:2.6,n:3,color:0x070503,seed:37,rim:0.18,rimC:0xe0b070});
  fg.g.position.set(6,1.2,24); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:3.0,w:14,d:6,color:0x060403,seed:39,rim:0.14,rimC:0xd8a860});
  fg2.g.position.set(-20,-1.0,22); g.add(fg2.g);
  addLights(g,{c:0xe8bc78,i:0.50,p:[-55,80,25]},{c:0x281a0e,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ctl.open=Math.min(1,ctl.open+dt/7.5);      /* 千门次第开：约 7.5 秒开齐 */
      ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
      gates.update(t,ctl.open);
      for(let i=0;i<lamps.length;i++)lamps[i].update(t,k);
      w1.update(t,k); w2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(2,0.2,0.10); pluck(4,0.9,0.09); }};
}
function bHongchen(){ // 二（末境·可点击）· 一骑红尘 —— 一骑红尘妃子笑，无人知是荔枝来
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,open:0.25,speed:1};
  const grd=makeGround({r:250,c1:0x0c0806,c2:0x1a1210,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:50,layers:2,peaks:4,seed:231,color:0x120b06,atmo:0x402c14,
    fogK:0.60,glowK:0.08,glow:0xd89850,y:-12});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  const brocade=makeBrocadeGHQ({n:330,halfW:116,top:26,depth:32,seed:101}); brocade.g.position.set(-2,0,-84); g.add(brocade.g);
  /* 山顶千门（洞开处）+ 妃子所在的宫台 */
  const gates=makeGateRowGHQ({n:5,gap:5.6,h:3.6}); gates.g.position.set(2,10.2,-52); gates.g.scale.setScalar(1.5); g.add(gates.g);
  const terrace=new THREE.Mesh(new THREE.BoxGeometry(44,9.0,12),
    new THREE.MeshPhongMaterial({color:0x32241a,shininess:10,specular:0x5a4228,emissive:0x0c0804}));
  terrace.position.set(2,5.2,-56); g.add(terrace);
  const lamps=[];
  [[-14,12.9,-48],[-3,12.9,-48],[8,12.9,-48],[19,12.9,-48]].forEach(function(p){
    const L=makePalaceLampGHQ({scale:1.3,seed:p[0]+80});
    L.g.position.set(p[0],p[1],p[2]); g.add(L.g); lamps.push(L);
  });
  /* 妃子：台上一袭红妆（一笑） */
  const feizi=makeFigure({pose:'独立',robe:0xa8303a,belt:0xe0b060,collar:0xf2e0c0,hat:'发髻',
    hair:0x14100c,scale:1.15,rim:0.55,rimC:0xf0c890,noProp:true});
  feizi.position.set(9.5,9.6,-48.5); feizi.rotation.y=2.6; g.add(feizi);
  /* 驿道上的红尘与驿马（沿驿道由近及远） */
  const dust=makeDustGHQ({n:560,w:34,h:7.5,d:13,color:0xa04f28,size:18,speed:2.8,maxA:0.42});
  g.add(dust.g);
  const horse=makeHorseRiderGHQ({scale:1.05,coat:0x3c2a1e,cloth:0x7a2a1c,seed:11});
  g.add(horse.g);
  /* 红尘之光：跟着驿马走的一团红褐尘光（只调 scale，不写 opacity） */
  const dustGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb06a34,transparent:true,
    opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  dustGlow.scale.set(16,9,1); dustGlow.renderOrder=3; g.add(dustGlow);
  const burst=makeBurst({n:110,color:0xe0a060,pos:[9.5,11.2,-48.5]});
  g.add(burst.points);
  const crowd=makeCrowd({n:3,rect:[-16,-56,14,8],seed:83,color:0x1a120c,rimC:0xe0b070,rim:0.22});
  g.add(crowd.mesh);
  const motes=makeGlow({n:46,box:[190,30,110],pos:[0,9,-22],color:0xf0c080,size:7,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,30,140],pos:[0,10,-60],scale:80,color:0x2c1e0e,op:0.13});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060403,seed:41,rim:0.16,rimC:0xe0b070});
  fg.g.position.set(-15,-1.0,12); g.add(fg.g);
  const fg2=makeForeground({kind:'岩壁',n:2,r:3.2,w:14,d:6,color:0x070503,seed:43,rim:0.14,rimC:0xd8a860});
  fg2.g.position.set(16,-1.0,10); g.add(fg2.g);
  addLights(g,{c:0xeab878,i:0.50,p:[-50,75,25]},{c:0x2a1c0e,i:0.60});
  /* 驿道：一道缓坡自近及远（马在其上行进） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(4.6,0.22,50),
    new THREE.MeshPhongMaterial({color:0x3c2f20,shininess:4,specular:0x241e14,emissive:0x0a0806}));
  road.position.set(3,0.9,-21); road.rotation.set(-0.072,-2.61,0); g.add(road);
  const A=[13,0.6,-4], Bp=[-7,1.8,-38];
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.open=Math.min(1,ctl.open+dt/0.9); ctl.speed=1.9; }
      else { ctl.open=Math.min(1,ctl.open+dt/9.0); ctl.speed=1; }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const u=(ctl.t/13.0)%1;
      const hx=A[0]+(Bp[0]-A[0])*u, hy=A[1]+(Bp[1]-A[1])*u, hz=A[2]+(Bp[2]-A[2])*u;
      horse.g.position.set(hx,hy,hz);
      horse.g.rotation.y=Math.PI*0.86;
      horse.update(t,k,ctl.speed);
      dust.g.position.set(hx+1.6,hy,hz+0.4);
      dust.update(t,k);
      dustGlow.position.set(hx+0.6,hy+1.5,hz);
      const dg=16*(1+0.42*ctl.pulse);
      dustGlow.scale.set(dg,dg*0.56,1);
      ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
      gates.update(t,ctl.open);
      for(let i=0;i<lamps.length;i++)lamps[i].update(t,k);
      feizi.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        ctl.open=0.3; ctl.speed=1.9;
        burst.fire();
        pluck(5,0.00,0.16); pluck(2,0.22,0.12); pluck(4,0.48,0.10);
        const fl=$('#flash'); fl.textContent='妃子笑'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;
    },clicked:false};
  return api;
}
