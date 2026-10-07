/* ================= 点绛唇·蹴罢秋千 · 两境场景（青绿春晓·易安春园变体：卷首春园、露浓花瘦、却把青梅嗅）
   本诗专属系统「回首嗅梅三段动作」：末境点击——少女和羞跑向门边（跑）→ 倚门回身（回首）→
   把青梅举到鼻尖（嗅梅），秋千余荡重启，梅香微光浮起；少女剪影+来访客是全页构图核心 ================= */

/* —— 新姿态：慵整纤纤手（双手举至发鬟边） / 和羞走（一手掩面颊） / 嗅梅（一手把青梅举到鼻尖） —— */
FIG_POSE['慵整']={r:[[0.52,3.20,0.10],[0.16,3.86,0.14]], l:[[-0.30,3.30,0.08],[-0.10,3.98,0.12]]};
FIG_POSE['羞走']={r:[[0.72,2.72,0.22],[0.42,3.34,0.36]], l:[[-0.62,2.10,0.02],[-0.70,1.26,0.10]]};
FIG_POSE['嗅梅']={r:[[0.60,2.20,0.02],[0.66,1.30,0.10]], l:[[-0.30,3.12,0.16],[0.08,3.58,0.32]]};

/* —— 秋千：A 形木架 + 顶梁 + 双绳吊坐板（摆体绕梁轴摆动，push() 可再荡起；合批 2 mesh） —— */
function makeSwingDJC(o){
  o=o||{};
  const h=o.h===undefined?6.6:o.h, w=o.w===undefined?4.4:o.w;
  const wood=o.wood===undefined?0x2a1c10:o.wood, woodL=shadeColor(wood,1.55);
  const ropeC=o.ropeC===undefined?0x74603c:o.ropeC;
  const FB=new GeoBag();
  [1,-1].forEach(function(s){
    const x=s*w/2;
    FB.put(limbGeo([x,0,1.15],[x*0.94,h,0],0.16,0.11,7),shadeColor(wood,0.90));
    FB.put(limbGeo([x,0,-1.15],[x*0.94,h,0],0.16,0.11,7),shadeColor(wood,1.05));
    const st=new THREE.BoxGeometry(0.9,0.42,2.8); st.translate(x,0.21,0); FB.put(st,shadeColor(0x3c4038,0.9));
  });
  const beam=new THREE.CylinderGeometry(0.13,0.13,w+1.9,8); beam.rotateZ(Math.PI/2); beam.translate(0,h,0);
  FB.put(beam,shadeColor(wood,1.25));
  const cross=new THREE.BoxGeometry(w*0.92,0.14,0.14); cross.translate(0,h*0.45,0); FB.put(cross,shadeColor(wood,0.8));
  const frame=FB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3a28,emissive:0x0a0805}),{c:o.rimC===undefined?0xb0cf9f:o.rimC,i:0.22,p:2.5}));
  const g=new THREE.Group(); g.add(frame);
  /* 摆体：双绳 + 坐板，挂点在梁心，绕 x 轴（梁向）摆动 → 坐板朝镜头方向荡 */
  const L=h-1.2, rx=w*0.30;
  const SB=new GeoBag();
  SB.put(limbGeo([-rx,0.05,0],[-rx*0.94,-L,0],0.05,0.042,6),ropeC);
  SB.put(limbGeo([rx,0.05,0],[rx*0.94,-L,0],0.05,0.042,6),ropeC);
  const seat=new THREE.BoxGeometry(1.9,0.13,0.62); seat.translate(0,-L-0.06,0); SB.put(seat,woodL);
  const swing=SB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a4630,emissive:0x0a0805}),{c:o.rimC===undefined?0xb0cf9f:o.rimC,i:0.26,p:2.5}));
  const pivot=new THREE.Group(); pivot.position.y=h; pivot.add(swing); g.add(pivot);
  const st={since:99,kick:0};
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,push:function(k){ st.since=0; st.kick=k===undefined?0.16:k; },
    update:function(t,dt){ if(dt)st.since+=dt;
      const idle=0.045*Math.sin(t*1.45+1.2);
      const kickA=st.kick*Math.exp(-0.33*st.since)*Math.sin(1.65*st.since);
      pivot.rotation.x=idle+kickA;
      pivot.rotation.z=0.02*Math.sin(t*0.7);
    }};
}

/* —— 花树（露浓花瘦）：细干疏枝 + 枝头粉白瘦花 + 少量嫩叶（合批 1 mesh） —— */
function makeFlowerDJC(o){
  o=o||{};
  const h=o.h===undefined?5.6:o.h, R=seedRnd(o.seed===undefined?9:o.seed);
  const trunkC=o.trunk===undefined?0x241a12:o.trunk;
  const bl=o.blossom===undefined?0xe6c6ce:o.blossom, leaf=o.leaf===undefined?0x2f5230:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.5-0.25,h*0.58,0],h*0.05,h*0.024,7),trunkC);
  const tips=[], nb=o.branches===undefined?4:o.branches;
  for(let i=0;i<nb;i++){
    const a=R()*6.283;
    const ex=Math.cos(a)*h*(0.30+R()*0.16), ez=Math.sin(a)*h*(0.30+R()*0.16), ey=h*(0.68+R()*0.30);
    B.put(limbGeo([0,h*0.52,0],[ex,ey,ez],h*0.022,h*0.010,6),shadeColor(trunkC,1.15));
    tips.push([ex,ey,ez]);
  }
  const nB=o.blossoms===undefined?40:o.blossoms;
  for(let i=0;i<nB;i++){
    const tp=tips[i%tips.length];
    const px=tp[0]+(R()-0.5)*1.05, py=tp[1]+(R()-0.5)*0.8, pz=tp[2]+(R()-0.5)*1.05;
    const pl=new THREE.PlaneGeometry(0.20+R()*0.14,0.20+R()*0.14);
    pl.translate(px,py,pz); pl.rotateY(R()*3.14); pl.rotateX(R()*3.14);
    B.put(pl,shadeColor(bl,0.82+R()*0.30));
    if(R()<0.30){
      const lf=new THREE.PlaneGeometry(0.36,0.16);
      lf.translate(px+0.2,py-0.25,pz); lf.rotateY(R()*3.14); lf.rotateZ((R()-0.5)*0.8);
      B.put(lf,shadeColor(leaf,0.9+R()*0.3));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x40483c,emissive:0x0a0d08,side:THREE.DoubleSide}),
    {c:o.rimC===undefined?0xe8d0d6:o.rimC,i:o.rim===undefined?0.14:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 青梅枝：院门边斜出的一枝青梅（青果+嫩叶，合批 1 mesh） —— */
function makePlumDJC(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?31:o.seed);
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[0.5+R()*0.4,-0.55+R()*0.3,0.9],0.09,0.05,6),0x2c2014);
  B.put(limbGeo([0.5,-0.4,0.9],[1.6,-0.9+R()*0.3,1.7],0.05,0.03,6),0x33251a);
  const nf=o.fruits===undefined?6:o.fruits;
  for(let i=0;i<nf;i++){
    const f=new THREE.SphereGeometry(0.13+R()*0.05,8,6);
    f.translate(0.25+R()*1.4,-0.45-R()*0.55,0.45+R()*1.3);
    B.put(f,shadeColor(0x7fae56,0.85+R()*0.35));
  }
  for(let i=0;i<8;i++){
    const lf=new THREE.PlaneGeometry(0.5,0.2);
    lf.translate(0.3+R()*1.3,-0.35-R()*0.7,0.4+R()*1.4);
    lf.rotateY(R()*3.14); lf.rotateZ((R()-0.5)*0.9);
    B.put(lf,shadeColor(0x3f6b3a,0.85+R()*0.35));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:18,
    specular:0x445030,emissive:0x0a1008,side:THREE.DoubleSide}),{c:0xa8cc90,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 少女手中的青梅（并到少女 Group 里，坐标按少女躯干局部系） —— */
function makePlumFruitDJC(){
  const B=new GeoBag();
  const f1=new THREE.SphereGeometry(0.10,8,6); f1.translate(0.09,3.52,0.36); B.put(f1,0x86b258);
  const f2=new THREE.SphereGeometry(0.085,8,6); f2.translate(0.17,3.44,0.33); B.put(f2,0x76a04a);
  const twig=new THREE.CylinderGeometry(0.018,0.014,0.30,5); twig.rotateZ(0.7); twig.translate(0.16,3.58,0.30);
  B.put(twig,0x2c2014);
  const lf=new THREE.PlaneGeometry(0.26,0.11); lf.rotateY(0.6); lf.translate(0.05,3.66,0.30); B.put(lf,0x3f6b3a);
  return B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:22,
    specular:0x4a5a34,emissive:0x0a1006,side:THREE.DoubleSide}));
}

/* —— 院门+矮墙：门柱×2+门楣+瓦顶+微开的双扇门+两侧院墙与墙帽（合批 1 mesh） —— */
function makeGateWallDJC(o){
  o=o||{};
  const wood=o.wood===undefined?0x261b10:o.wood, wallC=o.wall===undefined?0x1e281c:o.wall;
  const wl=o.wallLen===undefined?20:o.wallLen, wh=o.wallH===undefined?2.7:o.wallH;
  const gw=o.gw===undefined?4.4:o.gw, gh=o.gh===undefined?4.6:o.gh;
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const pl=new THREE.CylinderGeometry(0.24,0.28,gh,8); pl.translate(s*gw/2,gh/2,0); B.put(pl,shadeColor(wood,1.0));
    const bs=new THREE.BoxGeometry(0.95,0.5,0.95); bs.translate(s*gw/2,0.25,0); B.put(bs,shadeColor(0x454a40,0.9));
  });
  const beam=new THREE.BoxGeometry(gw+1.3,0.44,0.75); beam.translate(0,gh,0); B.put(beam,shadeColor(wood,1.22));
  const roof=new THREE.ConeGeometry(gw*0.82,1.35,4); roof.rotateY(Math.PI/4); roof.translate(0,gh+0.95,0);
  B.put(roof,0x232a20);
  const dl=new THREE.BoxGeometry(gw*0.46,gh-0.55,0.10); dl.translate(-gw*0.24,(gh-0.55)/2,0.28);
  B.put(dl,shadeColor(0x1c1610,1.0));
  const dr=new THREE.BoxGeometry(gw*0.46,gh-0.55,0.10); dr.rotateY(0.5); dr.translate(gw*0.34,(gh-0.55)/2,0.55);
  B.put(dr,shadeColor(0x201912,1.05));
  const wl2=new THREE.BoxGeometry(wl,wh,0.75); wl2.translate(gw/2+wl/2,wh/2,-0.2); B.put(wl2,shadeColor(wallC,1.0));
  const capR=new THREE.BoxGeometry(wl+0.3,0.22,1.05); capR.translate(gw/2+wl/2,wh+0.11,-0.2);
  B.put(capR,shadeColor(wallC,1.45));
  const wr=new THREE.BoxGeometry(5.5,wh,0.75); wr.translate(-gw/2-2.75,wh/2,-0.2); B.put(wr,shadeColor(wallC,0.92));
  const capL=new THREE.BoxGeometry(5.8,0.22,1.05); capL.translate(-gw/2-2.75,wh+0.11,-0.2);
  B.put(capL,shadeColor(wallC,1.38));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2e3626,emissive:0x080a06}),{c:o.rimC===undefined?0xb0cf9f:o.rimC,i:o.rim===undefined?0.26:o.rim,p:2.5}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 滑落的金钗：跑丢在园径上的小金钗，微光闪烁（合批 1 mesh） —— */
function makeHairpinDJC(){
  const B=new GeoBag();
  const pin=new THREE.CylinderGeometry(0.028,0.02,0.85,6); pin.rotateZ(Math.PI/2-0.35); pin.rotateY(0.7);
  pin.translate(0,0.05,0); B.put(pin,0xd8b46a);
  const head=new THREE.TorusGeometry(0.09,0.022,6,12); head.rotateX(Math.PI/2); head.translate(-0.40,0.09,0.12);
  B.put(head,0xc9a24a);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:80,
    specular:0xffe8b0,emissive:0x2c220e}));
  const g=new THREE.Group(); g.add(mesh);
  return {g,update:function(t){ const p=0.16+0.14*Math.sin(t*2.2);
    mesh.material.emissive.setRGB(p,p*0.78,p*0.34); }};
}

function bCover(){ // 卷首 · 春园晓色 —— 秋千遥挂、花树初开、院门半掩，晨光自东来
  const g=new THREE.Group();
  const grd=makeGround({r:230,c1:0x0b150e,c2:0x16271a,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:3,peaks:5,seed:57,color:0x0c1911,atmo:0x2c4434,fogK:0.62,glowK:0.05,
    glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-80); g.add(ridge.g);
  const swing=makeSwingDJC({scale:1.25}); swing.g.position.set(6,-1.6,-18); swing.g.rotation.y=-0.3;
  g.add(swing.g);
  const fl1=makeFlowerDJC({h:6.2,seed:11,scale:1.4}); fl1.g.position.set(-11,-1.6,-16); g.add(fl1.g);
  const fl2=makeFlowerDJC({h:5.4,seed:13,scale:1.15}); fl2.g.position.set(14,-1.6,-22); g.add(fl2.g);
  const gate=makeGateWallDJC({scale:1.0,wallLen:14}); gate.g.position.set(-17,-1.6,-30); gate.g.rotation.y=0.42;
  g.add(gate.g);
  const plum=makePlumDJC({seed:35,scale:1.2}); plum.g.position.set(-15.2,1.6,-28.4); g.add(plum.g);
  /* 园墙外过路人影 */
  const crowd=makeCrowd({n:4,rect:[-8,-40,30,6],seed:67,color:0x131e14,rimC:0x8fae78,rim:0.2});
  crowd.mesh.position.y=-1.6; g.add(crowd.mesh);
  /* 晨曦：东天一抹暖意（青绿底上唯一的暖） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.14,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,58,1); dawn.position.set(70,26,-120); dawn.renderOrder=-7; g.add(dawn);
  const petals=makeGlow({n:36,box:[70,10,36],pos:[0,8,-16],color:0xe9cfd4,size:4.5,speed:0.07,rise:1,maxA:0.16,add:false});
  g.add(petals.points);
  const motes=makeGlow({n:30,box:[190,28,110],pos:[0,9,-26],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[240,30,130],pos:[0,11,-50],scale:78,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:30,n:7,d:7,color:0x081009,seed:19,sway:0.7,rim:0.12,rimC:0xb0cf9f});
  brL.g.position.set(-26,-1.6,42); brL.g.scale.setScalar(1.5); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:21,rim:0.14,rimC:0xb0cf9f});
  rk.g.position.set(17,-1.4,16); g.add(rk.g);
  addLights(g,{c:0xe0d0a0,i:0.46,p:[50,80,30]},{c:0x243320,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); swing.update(t,dt); mist.update(t,k); motes.update(t); petals.update(t);
    brL.update(t,k); rk.update(t,k); crowd.update(t);
    dawn.material.opacity=k*(0.10+0.03*Math.sin(t*0.4));
  }};
}
function bNong(){ // 一 · 露浓花瘦 —— 蹴罢秋千，慵整纤纤手；露浓花瘦，薄汗轻衣透
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0a130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:38,layers:2,peaks:5,seed:71,color:0x09150e,atmo:0x29412e,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-6});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  /* 秋千（主景）：余荡未歇，坐板缓缓摆动 */
  const swing=makeSwingDJC({scale:0.92}); swing.g.position.set(4.2,0,-10); swing.g.rotation.y=0.15; g.add(swing.g);
  /* 少女：慵整纤纤手（双手举至鬟边，衣衫被薄汗浸得微亮） */
  const girl=makeFigure({pose:'慵整',robe:0xb8938a,belt:0x9a7a4a,skin:0xe4c2a8,hair:0x1c1410,
    collar:0xe8dfc6,hat:'发髻',scale:0.98,rim:0.5,rimC:0xe8d8c8,noProp:true});
  const w1=new THREE.Group(); w1.add(girl); w1.position.set(0.8,0,-4.2); w1.rotation.y=-0.4; g.add(w1);
  /* 露浓花瘦：花树×3，花冠上露光微闪 */
  const fl1=makeFlowerDJC({h:6.0,seed:23,scale:1.35}); fl1.g.position.set(-11,0,-12); g.add(fl1.g);
  const fl2=makeFlowerDJC({h:5.2,seed:25,scale:1.1}); fl2.g.position.set(13,0,-16); g.add(fl2.g);
  const fl3=makeFlowerDJC({h:4.6,seed:27,scale:0.9}); fl3.g.position.set(-5,0,-20); g.add(fl3.g);
  const dew=makeGlow({n:14,box:[6,3,6],pos:[-11,4.6,-12],color:0xdceecf,size:3,speed:0.02,rise:0,maxA:0.18});
  g.add(dew.points);
  /* 石径 + 落花瓣 + 黄绿萤火 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.2,0.06,24),
    new THREE.MeshPhongMaterial({color:0x3a3a2c,shininess:4,emissive:0x0c0b08}));
  path.rotation.y=0.12; path.position.set(2.2,0.03,-6); g.add(path);
  const petals=makeGlow({n:42,box:[48,9,30],pos:[0,7.5,-3],color:0xe9cfd4,size:4.5,speed:0.09,rise:1,maxA:0.20,add:false});
  g.add(petals.points);
  const fire=makeGlow({n:20,box:[50,6,26],pos:[0,2.2,-2],color:0xc8e08a,size:4.5,speed:0.06,rise:0.4,maxA:0.15});
  g.add(fire.points);
  const motes=makeGlow({n:28,box:[140,20,70],pos:[0,8,-18],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[200,26,110],pos:[0,8,-44],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const brL=makeForeground({kind:'坡石',n:2,r:3.0,w:14,d:5,color:0x070d08,seed:41,rim:0.12,rimC:0xb0cf9f});
  brL.g.position.set(-14,-1.3,10); brL.g.scale.setScalar(0.95); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:6,color:0x060b07,seed:43,rim:0.12,rimC:0xb0cf9f});
  rk.g.position.set(12,-1.2,11); rk.g.scale.setScalar(0.9); g.add(rk.g);
  addLights(g,{c:0xd8c88a,i:0.48,p:[-40,75,35]},{c:0x243320,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); swing.update(t,dt);
      girl.update(t,k);
      mist.update(t,k); motes.update(t); dew.update(t); petals.update(t); fire.update(t);
      brL.update(t,k); rk.update(t,k);
    },onEnter(){ pluck(4,0.3,0.08); pluck(2,0.85,0.07); }};
}
function bXiu(){ // 二（末境·可点击）· 却把青梅嗅 —— 见客入来袜刬金钗溜；点击：跑→回首→嗅梅 三段动作+秋千余荡
  const g=new THREE.Group();
  const ctl={ph:0,scT:0,cool:0};
  const A=[-1.4,0,-4.8], B=[-8.9,0,-10.6], RY0=2.75, RY1=0.75;
  const grd=makeGround({r:220,c1:0x0a130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:36,layers:2,peaks:4,seed:81,color:0x091409,atmo:0x27402c,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 院门+矮墙（院墙自门向右延伸，圈出后园） */
  const gate=makeGateWallDJC({}); gate.g.position.set(-10,0,-13.5); gate.g.rotation.y=0.3; g.add(gate.g);
  /* 门边青梅枝（点睛：却把青梅嗅的出处） */
  const plum=makePlumDJC({seed:37,scale:1.15}); plum.g.position.set(-11.6,3.1,-12.6); g.add(plum.g);
  /* 秋千：画面右侧，点击后余荡重启 */
  const swing=makeSwingDJC({}); swing.g.position.set(7.5,0,-9.5); swing.g.rotation.y=-0.25; g.add(swing.g);
  /* 来访客：刚入门、立在门前（中景次主体，袍色稍亮以从墙影里读出） */
  const guest=makeFigure({pose:'独立',robe:0x4a5438,belt:0x6a5638,hat:'幞头',beard:true,
    scale:1.08,rim:0.55,rimC:0xc8e0b0,noProp:true});
  guest.position.set(-6.6,0,-9.0); guest.rotation.y=1.0; g.add(guest);
  /* 少女×2（同一人两态）：girl1=和羞走（掩颊）→ girl2=倚门回首、嗅梅（青梅举到鼻尖） */
  const robeOpt={robe:0xb8938a,belt:0x9a7a4a,skin:0xe4c2a8,hair:0x1c1410,collar:0xe8dfc6,hat:'发髻',
    scale:0.98,rim:0.5,rimC:0xe8d8c8,noProp:true};
  const girl1=makeFigure(Object.assign({pose:'羞走'},robeOpt));
  const w1=new THREE.Group(); w1.add(girl1); w1.position.set(A[0],0,A[2]); w1.rotation.y=RY0; g.add(w1);
  const girl2=makeFigure(Object.assign({pose:'嗅梅'},robeOpt));
  girl2.add(makePlumFruitDJC());
  const w2=new THREE.Group(); w2.add(girl2); w2.position.set(B[0],0,B[2]); w2.rotation.y=RY1;
  w2.visible=false; g.add(w2);
  /* 金钗溜：跑丢在园径上的金钗，微光闪烁 */
  const pin=makeHairpinDJC(); pin.g.position.set(-4.8,0.05,-7.2); pin.g.rotation.y=0.5; g.add(pin.g);
  /* 嗅梅时的梅香微光（点击第三段才浮起） */
  const scent=makeGlow({n:24,box:[1.6,1.4,1.6],pos:[B[0]+0.3,3.6,B[2]+0.4],color:0xd8ecc2,size:3.4,
    speed:0.22,rise:1,maxA:0});
  g.add(scent.points);
  const petals=makeGlow({n:30,box:[44,9,26],pos:[0,7,-3],color:0xe9cfd4,size:4.2,speed:0.08,rise:1,maxA:0.16,add:false});
  g.add(petals.points);
  const fire=makeGlow({n:18,box:[46,6,24],pos:[0,2.2,-2],color:0xc8e08a,size:4.2,speed:0.06,rise:0.4,maxA:0.14});
  g.add(fire.points);
  const motes=makeGlow({n:28,box:[150,20,70],pos:[0,8,-16],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[210,26,110],pos:[0,8,-46],scale:74,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x060b07,seed:91,rim:0.12,rimC:0xb0cf9f});
  rk.g.position.set(14,-1.2,12); rk.g.scale.setScalar(0.9); g.add(rk.g);
  const brL=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:5,color:0x070d08,seed:93,rim:0.12,rimC:0xb0cf9f});
  brL.g.position.set(-15,-1.3,10); brL.g.scale.setScalar(0.9); g.add(brL.g);
  addLights(g,{c:0xdcc98c,i:0.50,p:[-45,75,35]},{c:0x28381f,i:0.66});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.cool=Math.max(0,ctl.cool-dt);
      ridge.update(t,0); swing.update(t,dt);
      guest.update(t,k); girl1.update(t,k); girl2.update(t,k);
      mist.update(t,k); motes.update(t); petals.update(t); fire.update(t);
      rk.update(t,k); brL.update(t,k); pin.update(t);
      /* 三段动作：ph1 跑 → ph2 回首 → ph3 嗅梅 → ph4 定格 */
      if(ctl.ph===1){
        ctl.scT+=dt; const u=Math.min(1,ctl.scT/1.15), e=u*u*(3-2*u);
        w1.position.set(A[0]+(B[0]-A[0])*e, 0.15*Math.abs(Math.sin(u*Math.PI*3)), A[2]+(B[2]-A[2])*e);
        w1.rotation.x=0.07*Math.sin(u*Math.PI);
        if(u>=1){ ctl.ph=2; ctl.scT=0; }
      } else if(ctl.ph===2){
        ctl.scT+=dt; const u=Math.min(1,ctl.scT/0.95), e=u*u*(3-2*u);
        w1.rotation.y=RY0+(RY1-RY0)*e;
        if(u>=1){
          ctl.ph=3; ctl.scT=0;
          w1.visible=false; w2.visible=true;
          swing.push(0.17);
          pluck(3,0,0.12); pluck(5,0.35,0.10); pluck(4,0.85,0.09);
          const fl=$('#flash'); fl.textContent='却把青梅嗅'; fl.classList.remove('go');
          void fl.offsetWidth; fl.classList.add('go');
        }
      } else if(ctl.ph===3){
        ctl.scT+=dt; const u=Math.min(1,ctl.scT/1.5);
        scent.mat.uniforms.uMaxA.value=k*0.30*(u*u*(3-2*u));
        if(u>=1)ctl.ph=4;
      } else if(ctl.ph===4){
        scent.mat.uniforms.uMaxA.value=k*(0.10+0.045*Math.sin(t*2.2));
      }
    },click(){
      if(ctl.cool>0)return;
      ctl.cool=0.9;
      if(ctl.ph===0){
        ctl.ph=1; ctl.scT=0; api.clicked=true; pluck(1,0,0.10);
      } else if(ctl.ph>=3){
        ctl.ph=1; ctl.scT=0; api.clicked=true;
        w1.visible=true; w2.visible=false;
        w1.position.set(A[0],0,A[2]); w1.rotation.set(0,RY0,0);
        scent.mat.uniforms.uMaxA.value=0;
        pluck(1,0,0.10);
      }
    },clicked:false,onEnter(){ pluck(2,0.2,0.07); }};
  return api;
}
