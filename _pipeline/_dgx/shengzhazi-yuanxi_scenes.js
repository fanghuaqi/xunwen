/* ================= 生查子·元夕 · 两境场景（夜宴金彩·欧阳修元夕灯市变体：灯如昼、月依旧） =================
   美术口径：元夕灯市——去年/今年同机位对照。同一条灯市长街、同一轮柳梢月：
   壹（去年）暖金满灯、人约黄昏后；贰（今年）灯依旧而人不在（人海依旧、独少一人，色温微降）。
   标志性瞬间：灯如昼的人约黄昏——柳梢月上 + 一街灯海。
   末境点击：灯海渐暗只余月光——去年人事不再。bg 硬性 #05070d，金彩属灯焰。 */

/* 宫灯：六角宫灯变体——骨架/灯穗 1 mesh + 六面灯纱 1 mesh + 外辉 1 sprite（+可选内焰 2）
   返回 {g,update,setDim}；dim 供末境「灯海渐暗」统一压暗 */
function makePalaceLantern(o){
  o=o||{};
  const sc=o.scale===undefined?0.8:o.scale;
  const B=new GeoBag();
  const top=new THREE.CylinderGeometry(0.30,0.46,0.13,6); top.translate(0,0.415,0); B.put(top,0x3a2a18);
  const bot=new THREE.CylinderGeometry(0.46,0.30,0.13,6); bot.translate(0,-0.415,0); B.put(bot,0x3a2a18);
  const cap=new THREE.CylinderGeometry(0.09,0.19,0.10,6); cap.translate(0,0.52,0); B.put(cap,0xc9a24a);
  const cord=new THREE.CylinderGeometry(0.014,0.014,0.46,4); cord.translate(0,0.79,0); B.put(cord,0x2a1c12);
  for(let i=0;i<6;i++){
    const a=i*Math.PI/3, rib=new THREE.CylinderGeometry(0.020,0.020,0.80,5);
    rib.translate(Math.cos(a)*0.45,0,Math.sin(a)*0.45); B.put(rib,0x4a3620);
  }
  for(let i=0;i<3;i++){
    const ts=new THREE.ConeGeometry(0.045,0.34,5); ts.rotateX(Math.PI);
    ts.translate((i-1)*0.09,-0.60,0); B.put(ts,i===1?0xc9a24a:0x8a5a2a);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:22,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xd9a85a,i:0.34,p:2.6})));
  /* 六面灯纱：合批 1 mesh，透光暖纱 */
  const P=new GeoBag();
  for(let i=0;i<6;i++){
    const a=i*Math.PI/3, pa=new THREE.PlaneGeometry(0.50,0.62);
    pa.rotateY(a+Math.PI/2); pa.translate(Math.cos(a)*0.40,0,Math.sin(a)*0.40); P.put(pa,0xffffff);
  }
  const panelMat=new THREE.MeshPhongMaterial({color:0xffc470,emissive:0xd97a28,emissiveIntensity:1.0,
    transparent:true,opacity:0.58,side:THREE.DoubleSide,shininess:8,specular:0x6a4a28});
  const panels=new THREE.Mesh(mergeGeos(P.list),panelMat); panels.renderOrder=2; g.add(panels);
  /* 外辉 */
  const glowBase=o.glow===undefined?0.50:o.glow;
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffa24e,
    transparent:true,opacity:glowBase,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(2.6,2.6,1); glow.renderOrder=3; g.add(glow);
  let flame=null;
  if(o.flame){
    flame=makeFlame({h:0.42,w:0.15,planes:2,embers:7,esize:3,spark:false,wide:0.30,
      core:0xffe2a0,outer:0xff7a22,seed:Math.random()*8});
    flame.g.renderOrder=3; g.add(flame.g);
  }
  g.scale.setScalar(sc);
  const ph=Math.random()*6.283;
  let dim=1;
  const api={g,update(t,k){
      const kk=(k===undefined?1:k)*dim;
      glow.material.opacity=kk*glowBase*(0.82+0.18*Math.sin(t*5.1+ph));
      panelMat.emissiveIntensity=kk*(0.88+0.12*Math.sin(t*6.3+ph*1.3));
      if(flame){ flame.update(t,kk); flame.mat.uniforms.uFade.value=kk; }
    },setDim(v){ dim=v; }};
  return api;
}

/* 走马灯：外纱六棱筒 + 内转剪影带（热气驱动自转）+ 上下盖/立柱底座——元夕灯市的一盏「活」灯
   返回 {g,update,setDim} */
function makeHorseLantern(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale, poleH=o.pole===undefined?0:o.pole;
  const B=new GeoBag();
  const top=new THREE.CylinderGeometry(0.40,0.30,0.10,6); top.translate(0,0.30,0); B.put(top,0x3a2a18);
  const bot=new THREE.CylinderGeometry(0.30,0.40,0.10,6); bot.translate(0,-0.30,0); B.put(bot,0x3a2a18);
  const fin=new THREE.SphereGeometry(0.06,7,5); fin.translate(0,0.40,0); B.put(fin,0xc9a24a);
  if(poleH>0){
    const pole=new THREE.CylinderGeometry(0.045,0.065,poleH,7); pole.translate(0,-0.30-poleH/2,0); B.put(pole,0x3a2c1c);
    const ft=new THREE.CylinderGeometry(0.26,0.34,0.09,9); ft.translate(0,-0.30-poleH-0.045,0); B.put(ft,0x241a12);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xd9a85a,i:0.32,p:2.6})));
  const paper=new THREE.Mesh(new THREE.CylinderGeometry(0.34,0.34,0.52,6,1,true),
    new THREE.MeshPhongMaterial({color:0xffb868,emissive:0xb85c18,emissiveIntensity:1.0,
      transparent:true,opacity:0.40,side:THREE.DoubleSide,depthWrite:false}));
  paper.renderOrder=2; g.add(paper);
  /* 内转带：白纱 + 四匹奔马剪影（深色小块），热气自转 */
  const N=new GeoBag();
  const band=new THREE.CylinderGeometry(0.215,0.215,0.36,8,1,true); N.put(band,0xf2e2c2);
  for(let i=0;i<4;i++){
    const a=i*Math.PI/2, hb=new THREE.SphereGeometry(0.085,7,5);
    hb.scale(1.55,0.72,0.5); hb.rotateY(a);
    hb.translate(Math.cos(a)*0.24,-0.015,Math.sin(a)*0.24);
    const hl=new THREE.SphereGeometry(0.045,6,4); hl.scale(1.1,0.9,0.5);
    hl.translate(Math.cos(a)*0.24+Math.cos(a)*0.10,0.055,Math.sin(a)*0.24+Math.sin(a)*0.10);
    N.put(hb,0x2c2018); N.put(hl,0x2c2018);
  }
  const bandMesh=new THREE.Mesh(mergeGeos(N.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      transparent:true,opacity:0.92,emissive:0x7a4a18,emissiveIntensity:1.0,side:THREE.DoubleSide,depthWrite:false}));
  bandMesh.renderOrder=2; g.add(bandMesh);
  const glowBase=o.glow===undefined?0.42:o.glow;
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9440,
    transparent:true,opacity:glowBase,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(2.3,2.3,1); glow.renderOrder=3; g.add(glow);
  g.scale.setScalar(sc);
  const ph=Math.random()*6.283;
  let dim=1;
  const api={g,update(t,k){
      const kk=(k===undefined?1:k)*dim;
      bandMesh.rotation.y=t*1.15+ph;               // 走马灯依旧自转——灯「活」着，人不在
      glow.material.opacity=kk*glowBase*(0.82+0.18*Math.sin(t*4.7+ph));
      paper.material.emissiveIntensity=kk*(0.86+0.14*Math.sin(t*5.9+ph*1.7));
      bandMesh.material.emissiveIntensity=kk*(0.80+0.20*Math.sin(t*3.3+ph));
    },setDim(v){ dim=v; }};
  return api;
}

/* 柳树：躯干主枝 1 mesh + 垂柳丝（FG 摆动着色器，梢头受月光染金）1 mesh
   ——「月上柳梢头」的柳，去年今年同株同位 */
function makeWillow(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1671:o.seed);
  const h=o.h===undefined?4.6:o.h, spread=o.spread===undefined?2.6:o.spread, n=o.n===undefined?26:o.n;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.15,0.30,h*0.62,8); trunk.translate(0,h*0.31,0); B.put(trunk,0x191210);
  for(let i=0;i<4;i++){
    const a=R()*6.283, br=new THREE.CylinderGeometry(0.045,0.10,h*0.52,6);
    br.rotateZ((R()-0.5)*1.5); br.rotateX((R()-0.5)*1.3);
    br.translate(Math.cos(a)*spread*0.28,h*(0.58+R()*0.24),Math.sin(a)*spread*0.28);
    B.put(br,0x191210);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a3a28,emissive:0x060505}),{c:0xd9a85a,i:0.22,p:2.4})));
  /* 垂丝：每缕 3 段窄片（随机朝向），翻转 uv 让梢头摆幅最大、且梢头染月色金 */
  const S=new GeoBag();
  for(let i=0;i<n;i++){
    const a=R()*6.283, rr=spread*(0.22+0.78*R());
    const topX=Math.cos(a)*rr, topZ=Math.sin(a)*rr, topY=h*(0.78+0.34*R());
    const len=Math.min(1.7+R()*2.3, topY-0.5);
    const ry=R()*6.283;
    for(let k=0;k<3;k++){
      const seg=new THREE.PlaneGeometry(0.13*(1-k*0.20),len/3+0.14);
      seg.rotateZ(Math.PI);                                  // 翻转：uv.y 大的一端朝下（梢头）
      seg.rotateY(ry+(R()-0.5)*0.5);
      seg.rotateX((R()-0.5)*0.34);
      seg.translate(topX+(R()-0.5)*0.14,topY-len*(k/3)-len/6,topZ+(R()-0.5)*0.14);
      S.put(seg,0xffffff);
    }
  }
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,depthWrite:false,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.26:o.sway},uC:{value:C(0x191309)},
      uTipC:{value:C(0x7c6428)},uFade:{value:1}},
    vertexShader:FG_VERT,fragmentShader:FG_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(S.list),mt); mesh.frustumCulled=false; mesh.renderOrder=2;
  g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1.2:o.scale);
  const api={g,update(t,k){ mt.uniforms.uTime.value=t; }};
  return api;
}

/* 灯市长街（两境共用的「同机位」基底）：石板路 + 两侧楼影檐廊 + 窗光 + 跨街灯串 +
   灯海两层（远处）+ 映天灯晕 + 人海三片 + 柳一株 + 暖尘 + 雾
   ——全部 seedRnd 定位：去年/今年逐物同位，只换人与色温 */
function makeStreetBase(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2167:o.seed);
  const warm=o.warmth===undefined?1:o.warmth;      // 色温：今年 0.86
  const g=new THREE.Group();
  /* 石板路（压暗：路是夜的底，灯才是主角） */
  const RB=new GeoBag();
  for(let i=0;i<12;i++){
    const z=8-i*6.2, s=new THREE.BoxGeometry(6.8+R()*0.5,0.12,6.1);
    s.translate((R()-0.5)*0.3,0.06,z); RB.put(s,shadeColor(0x141113,0.80+0.30*R()));
  }
  g.add(RB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2c20,emissive:0x060405}),{c:0xd9a85a,i:0.12,p:2.4})));
  /* 两侧楼影 + 檐廊 + 街尾牌坊（合批 1 mesh；剪影处理，让窗光与灯串发言） */
  const BB=new GeoBag();
  for(let sd=-1;sd<=1;sd+=2){
    for(let i=0;i<8;i++){
      const z=3-i*7.6, h=4.1+R()*2.8, dep=5.6+R()*1.6;
      const bx=new THREE.BoxGeometry(5.6,h,dep); bx.translate(sd*8.3,h/2-0.12,z); BB.put(bx,shadeColor(0x121013,0.70+0.30*R()));
      const ev=new THREE.BoxGeometry(2.6,0.20,dep*0.92); ev.rotateZ(sd*0.05);
      ev.translate(sd*4.9,3.3+R()*0.7,z); BB.put(ev,0x181009);
    }
  }
  const pf=[[3.6,1],[ -3.6,1]];
  pf.forEach(function(p){
    const post=new THREE.BoxGeometry(0.55,6.2,0.55); post.translate(p[0],3.1,-45); BB.put(post,0x1c1210);
  });
  const bm1=new THREE.BoxGeometry(8.8,0.55,0.62); bm1.translate(0,5.35,-45); BB.put(bm1,0x201511);
  const bm2=new THREE.BoxGeometry(7.2,0.42,0.52); bm2.translate(0,6.15,-45); BB.put(bm2,0x201511);
  const rf=new THREE.BoxGeometry(9.8,0.30,1.7); rf.translate(0,6.72,-45); BB.put(rf,0x191009);
  g.add(BB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a28,emissive:0x060505}),{c:0xd9a85a,i:0.10,p:2.4})));
  /* 窗光：临街一层暖窗（合并 1 mesh；末境随灯海渐暗） */
  const WB=new GeoBag();
  for(let i=0;i<16;i++){
    const sd=i%2?1:-1, z=-1-i*3.4-R()*1.4, y=1.5+R()*1.8;
    const w=new THREE.PlaneGeometry(0.66+R()*0.3,0.86+R()*0.3);
    w.rotateY(sd>0?-Math.PI/2:Math.PI/2); w.translate(sd*5.46,y,z); WB.put(w,0xffffff);
  }
  const winMat=new THREE.MeshPhongMaterial({color:0x000000,emissive:0xff9d48,emissiveIntensity:1.0*warm,
    transparent:true,opacity:0.85,side:THREE.DoubleSide,depthWrite:false});
  const windows=new THREE.Mesh(mergeGeos(WB.list),winMat); windows.renderOrder=1; g.add(windows);
  /* 跨街灯串：四道，每道七盏（合批 1 mesh；「花市灯如昼」的骨架，灯体加大加亮） */
  const LB=new GeoBag();
  const lampC=[0xd9a85a,0xe0b060,0xc88a48,0xcf7f3c,0xd9a85a,0xe0b060,0xc07838];
  [-3.5,-11,-19,-28].forEach(function(z0,si){
    for(let i=0;i<7;i++){
      const u=i/6, x=-4.4+u*8.8, y=3.62-0.55*Math.sin(Math.PI*u)-R()*0.10;
      const b=new THREE.SphereGeometry(0.20,8,6); b.scale(1,0.76,1); b.translate(x,y,z0);
      LB.put(b,lampC[(i+si)%7]);
      const cpt=new THREE.CylinderGeometry(0.065,0.065,0.08,6); cpt.translate(x,y+0.17,z0); LB.put(cpt,0x3a2a18);
    }
  });
  const strMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0xffc890,emissive:0xc46a1a,emissiveIntensity:1.25*warm,transparent:true,opacity:0.98});
  const strings=new THREE.Mesh(mergeGeos(LB.list),strMat); g.add(strings);
  /* 灯海两层（远处人家的灯，一路亮到街尾——灯市纵深的主角；收在街面高度、退开近处防大光斑） */
  const seaA=makeGlow({n:150,box:[26,7,70],pos:[0,2.4,-42],color:0xe8a850,size:6.5,speed:0.02,rise:0,maxA:0.60});
  const seaB=makeGlow({n:80,box:[46,10,88],pos:[0,3.5,-66],color:0xd89848,size:8,speed:0.015,rise:0,maxA:0.34});
  g.add(seaA.points); g.add(seaB.points);
  const seaAb=seaA.mat.uniforms.uMaxA.value, seaBb=seaB.mat.uniforms.uMaxA.value;
  /* 映天灯晕：整条街把天际烘暖（fog:false，压低贴住天际线） */
  const skyGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb87a3a,
    transparent:true,opacity:0.24*warm,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  skyGlow.scale.set(130,24,1); skyGlow.position.set(0,7,-88); skyGlow.renderOrder=-7; g.add(skyGlow);
  const skyGb=0.24*warm;
  /* 人海三片（左/右沿街 + 街心远处），seed 固定：人海依旧 */
  const crowdL=makeCrowd({n:12,rect:[-13,-44,8,38],seed:2168,color:0x14100e,rimC:0xd9a85a,rim:0.26,sMin:0.78,sMax:1.05});
  const crowdR=makeCrowd({n:12,rect:[5,-44,8,38],seed:2169,color:0x14100e,rimC:0xd9a85a,rim:0.26,sMin:0.78,sMax:1.05});
  const crowdC=makeCrowd({n:10,rect:[-3.2,-52,6.4,14],seed:2170,color:0x161210,rimC:0xd9a85a,rim:0.24,sMin:0.72,sMax:0.95});
  g.add(crowdL.mesh); g.add(crowdR.mesh); g.add(crowdC.mesh);
  /* 柳（同株同位）+ 暖尘 + 街雾 */
  const willow=makeWillow({seed:1671,scale:1.2}); willow.g.position.set(-5.2,0,-7.5); g.add(willow.g);
  const dust=makeGlow({n:46,box:[40,9,36],pos:[0,1.6,-8],color:0xe0b060,size:4.0,speed:0.05,rise:0.18,maxA:0.20});
  g.add(dust.points);
  const dustB=dust.mat.uniforms.uMaxA.value;
  const mist=makeMist({n:5,spread:[120,13,60],pos:[0,3.5,-28],scale:56,color:0x5a4030,op:0.07});
  g.add(mist.g);
  const api={g,windows:winMat,strings:strMat,seaA:seaA,seaB:seaB,skyGlow:skyGlow,dust:dust,willow:willow,
    crowdL:crowdL,crowdR:crowdR,crowdC:crowdC,mist:mist,
    bases:{seaAb:seaAb,seaBb:seaBb,dustB:dustB,skyGb:skyGb,winI:1.0*warm,strI:1.25*warm},
    update(t,k){
      seaA.update(t); seaB.update(t); dust.update(t); mist.update(t,k); willow.update(t,k);
      crowdL.update(t); crowdR.update(t); crowdC.update(t);
    }};
  return api;
}

function bCover(){ // 卷首 · 元夕灯市远眺 —— 一街灯海直到天边，柳影人潮
  const g=new THREE.Group();
  if(bgRange)bgRange.g.scale.y=0.26, bgRange.g.position.y=-3;   // 压低常驻远山为低丘，让柳梢月出得来
  const grd=makeGround({r:150,c1:0x0a0809,c2:0x171013,y:-0.06});
  g.add(grd.mesh);
  const ridge=makeRange({r:220,h:22,layers:2,peaks:5,seed:1671,color:0x0b0a0c,atmo:0x4a2c18,fogK:0.66,glowK:0.06,y:-10});
  g.add(ridge.g);
  const base=makeStreetBase({warmth:0.95});
  g.add(base.g);
  const lamp1=makePalaceLantern({scale:0.9,flame:true}); lamp1.g.position.set(-4.9,3.62,-5.5); g.add(lamp1.g);
  const lamp2=makePalaceLantern({scale:0.82}); lamp2.g.position.set(5.0,3.55,-9.5); g.add(lamp2.g);
  const horse=makeHorseLantern({scale:1.0,pole:2.2}); horse.g.position.set(4.1,2.62,-1.8); g.add(horse.g);
  const fg1=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x060404,seed:9,sway:0.8,rim:0.12});
  fg1.g.position.set(-10,5.2,37); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:26,h:2.6,color:0x070505,seed:11,rim:0.10});
  fg2.g.position.set(0,-1.4,38); g.add(fg2.g);
  addLights(g,{c:0xffb070,i:0.22,p:[-30,36,-20]},{c:0x2c261e,i:0.60});
  const pl=new THREE.PointLight(0xffb060,0.9,40); pl.position.set(0,6.4,-10); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.update(t,k); ridge.update(t,0); fg1.update(t,k); fg2.update(t,k);
    lamp1.update(t,k); lamp2.update(t,k); horse.update(t,k);
    pl.intensity=k*0.9*(0.82+0.18*Math.sin(t*8.3));
  }};
}

function bDengRuZhou(){ // 壹 · 灯如昼 —— 去年元夜：花市灯如昼；月上柳梢头，人约黄昏后（标志性瞬间）
  const g=new THREE.Group();
  if(bgRange)bgRange.g.scale.y=0.26, bgRange.g.position.y=-3;   // 压低常驻远山为低丘，让柳梢月出得来
  const base=makeStreetBase({warmth:1.0});
  g.add(base.g);
  const ridge=makeRange({r:230,h:20,layers:2,peaks:5,seed:1672,color:0x0c0a0b,atmo:0x4a2c18,fogK:0.62,glowK:0.05,y:-12});
  g.add(ridge.g);
  /* 近景灯：檐下宫灯二（一盏带焰）+ 立柱走马灯——金彩属灯焰 */
  const lamp1=makePalaceLantern({scale:0.9,flame:true}); lamp1.g.position.set(-4.9,3.62,-5.5); g.add(lamp1.g);
  const lamp2=makePalaceLantern({scale:0.82}); lamp2.g.position.set(5.0,3.55,-9.5); g.add(lamp2.g);
  const horse=makeHorseLantern({scale:1.0,pole:2.2}); horse.g.position.set(4.1,2.62,-1.8); g.add(horse.g);
  /* 街边小摊：糖球花担一桌一盘（市井信息量） */
  const stall=makeTable({w:2.6,d:1.3,h:1.15,wood:0x2a1c10}); stall.g.position.set(-4.6,0,-2.6); stall.g.rotation.y=0.5; g.add(stall.g);
  const dish=makeDish({r:0.62,n:4,foods:[0xc05838,0xd8a050,0x9a3a2a,0xc88a3a]}); dish.g.position.set(-4.45,1.15,-2.5); g.add(dish.g);
  /* 人约：柳下一对——男子幞头青袍候于灯影，女子发髻裙衫恰至 */
  const he=makeFigure({pose:'独立',robe:0x4a5868,belt:0x8a6a3a,skin:0xd9b189,hair:0x1a1410,collar:0xe8dcc0,
    hat:'幞头',scale:1.0,rim:0.55,rimC:0xffd890,noProp:true});
  he.position.set(-3.8,0,-7.2); he.rotation.y=0.85; g.add(he);
  const she=makeFigure({pose:'独立',robe:0x7c5464,belt:0xc9a24a,skin:0xe0c4ac,hair:0x1a1210,collar:0xe8d4c0,
    hat:'发髻',scale:0.88,rim:0.58,rimC:0xffd890,noProp:true});
  she.position.set(-2.6,0,-6.3); she.rotation.y=-2.35; g.add(she);
  /* 前景：柳枝垂入画 + 摊沿矮栏 */
  const fg1=makeForeground({kind:'树枝',n:2,w:14,d:4,color:0x060404,seed:19,sway:0.7,rim:0.12});
  fg1.g.position.set(-8,4.8,8.2); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:22,h:2.2,color:0x070505,seed:21,rim:0.10});
  fg2.g.position.set(1,-1.2,8.6); g.add(fg2.g);
  addLights(g,{c:0xffbe78,i:0.22,p:[-28,34,-18]},{c:0x2a221a,i:0.60});
  const pl=new THREE.PointLight(0xffb060,1.05,26); pl.position.set(0,6.4,-6); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.update(t,k); ridge.update(t,0);
    lamp1.update(t,k); lamp2.update(t,k); horse.update(t,k);
    he.update(t,k); she.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
    pl.intensity=k*1.05*(0.80+0.20*Math.sin(t*8.9));
  }};
}

function bYueYiJiu(){ // 贰（末境·可点击）· 月依旧 —— 今年元夜：月与灯依旧；不见去年人，泪湿春衫袖
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,glow:0};
  if(bgRange)bgRange.g.scale.y=0.26, bgRange.g.position.y=-3;   // 压低常驻远山为低丘，让柳梢月出得来
  const base=makeStreetBase({warmth:0.86});          // 色温微降：灯依旧，暖意减一分
  g.add(base.g);
  const ridge=makeRange({r:230,h:20,layers:2,peaks:5,seed:1672,color:0x0c0a0b,atmo:0x3a2a1c,fogK:0.62,glowK:0.05,y:-12});
  g.add(ridge.g);
  const lamp1=makePalaceLantern({scale:0.9,flame:true}); lamp1.g.position.set(-4.9,3.62,-5.5); g.add(lamp1.g);
  const lamp2=makePalaceLantern({scale:0.82}); lamp2.g.position.set(5.0,3.55,-9.5); g.add(lamp2.g);
  const horse=makeHorseLantern({scale:1.0,pole:2.2}); horse.g.position.set(4.1,2.62,-1.8); g.add(horse.g);
  const stall=makeTable({w:2.6,d:1.3,h:1.15,wood:0x2a1c10}); stall.g.position.set(-4.6,0,-2.6); stall.g.rotation.y=0.5; g.add(stall.g);
  const dish=makeDish({r:0.62,n:4,foods:[0xc05838,0xd8a050,0x9a3a2a,0xc88a3a]}); dish.g.position.set(-4.45,1.15,-2.5); g.add(dish.g);
  /* 独行的人：淡青春衫，望向柳下旧约处——人海依旧，独少一人 */
  const poet=makeFigure({pose:'独立',robe:0x6a7488,belt:0x9a8a70,skin:0xd9b189,hair:0x1a1410,collar:0xd8d4c8,
    hat:'幞头',scale:1.0,rim:0.52,rimC:0xc8d4e8,noProp:true});
  poet.position.set(2.6,0,-4.2); poet.rotation.y=-2.1; g.add(poet);
  const fg1=makeForeground({kind:'树枝',n:2,w:14,d:4,color:0x060404,seed:19,sway:0.7,rim:0.12});
  fg1.g.position.set(-8,4.8,8.2); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:22,h:2.2,color:0x070505,seed:21,rim:0.10});
  fg2.g.position.set(1,-1.2,8.6); g.add(fg2.g);
  addLights(g,{c:0xd8a888,i:0.20,p:[-28,34,-18]},{c:0x2a2826,i:0.58});
  const pl=new THREE.PointLight(0xffb060,1.0,26); pl.position.set(0,6.4,-6); g.add(pl);
  /* 月光池：点击后灯海渐暗，唯此一片清辉（基线 1.0，包络 ≤1） */
  const ml=new THREE.PointLight(0xa8c4e8,1.0,44); ml.position.set(-7,13,-24); g.add(ml);
  /* 收集点光/平行光以便交互压暗 */
  let dirL=null;
  g.traverse(function(o){ if(o.isDirectionalLight&&!dirL)dirL=o; });
  const plB=1.0, mlB=1.0, dirB=0.20;
  const api={group:g,clicked:false,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.glow=Math.min(1,ctl.glow+dt/2.2);
      const gl=ctl.glow, dim=1-0.94*gl;
      base.update(t,k); ridge.update(t,0);
      /* 灯海渐暗：窗光/灯串/灯海/映天晕/暖尘/近灯一律压暗 */
      base.windows.emissiveIntensity=k*base.bases.winI*dim;
      base.strings.emissiveIntensity=k*base.bases.strI*dim;
      base.seaA.mat.uniforms.uMaxA.value=base.bases.seaAb*(1-0.93*gl);
      base.seaB.mat.uniforms.uMaxA.value=base.bases.seaBb*(1-0.93*gl);
      base.dust.mat.uniforms.uMaxA.value=base.bases.dustB*(1-0.88*gl);
      base.skyGlow.material.opacity=k*base.bases.skyGb*(1-0.72*gl);
      lamp1.setDim(dim); lamp2.setDim(dim); horse.setDim(dim);
      lamp1.update(t,k); lamp2.update(t,k); horse.update(t,k);
      poet.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
      pl.intensity=k*plB*(0.80+0.20*Math.sin(t*8.9))*dim;
      if(dirL)dirL.intensity=k*dirB*(1-0.55*gl);
      ml.intensity=k*mlB*(0.22+0.78*gl);                 // 只余月光：清辉缓缓涨满
    },click(){
      if(ctl.t<1.2)return;
      if(ctl.clicked)return;
      ctl.clicked=true; api.clicked=true;
      bell();
      pluck(2,0.06,0.14); pluck(4,0.5,0.13); pluck(1,1.0,0.12); pluck(5,1.5,0.10); pluck(0,2.2,0.09);
      const fl=$('#flash'); fl.textContent='不见去年人';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    }};
  return api;
}
