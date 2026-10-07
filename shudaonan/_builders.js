/* ---------------- 卷首 + 七境 ----------------
   构图铁律：每境三层 —— 前景（贴相机 15-30 单位、压暗、做框）→ 中景主体（60-110 单位、受光）
   → 背景 2-3 层（150-210 单位，越远越淡）。雾预算：fd·d_主体 ≤ 0.65，主体永远在 110 单位以内。
   山一律 makeRange 多峰脊线 / makeCliffWall 棱面崖体，不用三角形山。 */
function bCover(){ // 卷首 · 苍茫层峦，一线鸟道
  const g=new THREE.Group();
  const grd=makeGround({r:180,c1:0x0a0806,c2:0x2c1e12});
  grd.mesh.position.y=-6; g.add(grd.mesh);
  const far=makeRange({r:150,h:112,layers:3,peaks:6,seed:20260929,color:0x1a120c,atmo:0x8a5228,
    fogK:0.50,glowK:0.14,y:-24,arc:Math.PI*1.5,a0:-Math.PI*0.75});
  g.add(far.g);
  const cL=makeCliffWall({n:2,h:74,w:46,seed:311,color:0x3a2410,rimC:0xe0ac6a,rim:0.34,y:-26,zjit:12});
  cL.g.position.set(-74,-4,-66); cL.g.rotation.y=0.26; g.add(cL.g);
  const cR=makeCliffWall({n:2,h:64,w:42,seed:317,color:0x33210f,rimC:0xe0ac6a,rim:0.34,y:-26,zjit:12});
  cR.g.position.set(82,-4,-62); cR.g.rotation.y=-0.24; g.add(cR.g);
  /* 鸟道：中景崖壁上的一线木栈（西当太白有鸟道） */
  const road=makePlankRoad({w:2.6,color:0x241a12,rimC:0xe0ac6a,rim:0.42,
    pts:[[-46,20,-58],[-24,26,-57],[-2,21,-56],[20,27,-57],[42,22,-58]]});
  g.add(road.g);
  const sun=makeSunDisc({r:19,color:0xffe2b4,glowC:0xd97a2a,glow:230});
  sun.g.position.set(-70,48,-196); g.add(sun.g);
  const mist=makeMist({n:10,spread:[230,26,130],pos:[0,20,-84],scale:70,color:0x9a7048,op:0.11});
  g.add(mist.g);
  const flow=makeFlow({n:620,box:[190,22,150],pos:[0,20,-66],color:0xb08a5a,size:18,speed:3.0,maxA:0.18});
  g.add(flow.points);
  const motes=makeGlow({n:60,box:[190,40,110],pos:[0,24,-56],color:0xd9a05a,size:4.5,speed:0.05,rise:0,maxA:0.16});
  g.add(motes.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:4.4,w:24,d:9,color:0x060403,seed:41,rim:0.20,rimC:0xb07a44});
  fgL.g.position.set(-16,8,42); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:3.6,w:20,d:8,color:0x060403,seed:47,rim:0.20,rimC:0xb07a44});
  fgR.g.position.set(18,7,38); g.add(fgR.g);
  const bs=[];
  for(let i=0;i<3;i++){ const b=makeBird({scale:2.2,color:0x120d09,ph:i*1.7,flap:2.0}); g.add(b); bs.push(b); }
  addLights(g,{c:0xe0b070,i:0.58,p:[-150,90,-140]},{c:0x3c2c1c,i:0.62});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.6); mist.update(t,k); flow.update(t); motes.update(t);
    fgL.update(t,k); fgR.update(t,k); sun.update(t,k);
    for(let i=0;i<bs.length;i++){
      const b=bs[i], a=t*0.08+i*2.1;
      b.update(t);
      b.position.set(-24+Math.sin(a)*58,44+Math.sin(t*0.4+i*1.3)*3,-118+Math.cos(a)*34);
      b.rotation.y=-a+Math.PI/2;
    }
  }};
}
function bWeihu(){ // 一 · 危乎高哉 —— 层峦直逼天穹，云海茫然
  const g=new THREE.Group();
  const grd=makeGround({r:170,c1:0x0b0805,c2:0x2e2013});
  grd.mesh.position.y=-6; g.add(grd.mesh);
  /* 三层山：近层受光（主）、中层压暗、远层混天光（渐淡） */
  const far=makeRange({r:150,h:132,layers:3,peaks:7,seed:1201,color:0x1c140c,atmo:0x96592a,
    fogK:0.46,glowK:0.18,y:-28,arc:Math.PI*1.35,a0:-Math.PI*0.675});
  g.add(far.g);
  const mid=makeCliffWall({n:4,h:124,w:46,seed:1207,color:0x3c2510,rimC:0xf0b874,rim:0.40,y:-26,zjit:16});
  mid.g.position.set(0,-4,-102); g.add(mid.g);
  const near=makeCliffWall({n:5,h:96,w:44,seed:1211,color:0x44290f,rimC:0xf4c080,rim:0.46,y:-16,zjit:16});
  near.g.position.set(0,-2,-54); g.add(near.g);
  const sun=makeSunDisc({r:21,color:0xffeac4,glowC:0xe08a30,glow:260});
  sun.g.position.set(112,72,-206); g.add(sun.g);
  const mist=makeMist({n:11,spread:[240,32,140],pos:[0,28,-84],scale:74,color:0xa87c50,op:0.12});
  g.add(mist.g);
  const low=makeMist({n:6,spread:[210,16,110],pos:[0,12,-62],scale:58,color:0x8a6440,op:0.10});
  g.add(low.g);
  const flow=makeFlow({n:700,box:[200,24,150],pos:[0,22,-62],color:0xbb8f58,size:18,speed:3.6,maxA:0.20});
  g.add(flow.points);
  const motes=makeGlow({n:70,box:[190,40,110],pos:[0,26,-56],color:0xe0a860,size:4.5,speed:0.05,rise:0,maxA:0.16});
  g.add(motes.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:4.6,w:24,d:10,color:0x060403,seed:1209,rim:0.20,rimC:0xb88048});
  fgL.g.position.set(-18,5,36); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:3.8,w:20,d:8,color:0x060403,seed:1213,rim:0.20,rimC:0xb88048});
  fgR.g.position.set(20,4,32); g.add(fgR.g);
  addLights(g,{c:0xe8b478,i:0.64,p:[130,90,-120]},{c:0x42301e,i:0.64});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.5); mist.update(t,k); low.update(t,k); sun.update(t,k);
    flow.update(t); motes.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bNiandao(){ // 二 · 鸟道天梯 —— 天梯石栈相钩连，崖上是鸟道，崖下是崩落的乱石
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x090705,c2:0x261a10});
  grd.mesh.position.y=-30; g.add(grd.mesh);
  const far=makeRange({r:140,h:124,layers:2,peaks:6,seed:2201,color:0x181009,atmo:0x6a4a28,
    fogK:0.52,glowK:0.12,y:-32,arc:Math.PI*1.3,a0:-Math.PI*0.65});
  g.add(far.g);
  const mid=makeCliffWall({n:3,h:120,w:52,seed:2202,color:0x33200e,rimC:0xc99a60,rim:0.30,y:-30,zjit:12});
  mid.g.position.set(-6,-2,-88); g.add(mid.g);
  /* 主崖：天梯石栈挂在这一面绝壁上（主体的受光面，顶出画框） */
  const cliff=makeCliffWall({n:3,h:124,w:56,seed:2203,color:0x45290f,rimC:0xf0b874,rim:0.46,y:-30,zjit:10});
  cliff.g.position.set(8,-2,-36); g.add(cliff.g);
  /* 天梯石栈：之字形盘上崖壁（"相钩连"要一眼读出来） */
  const road=makePlankRoad({w:3.2,color:0x2a1c10,rimC:0xf0c080,rim:0.50,
    pts:[[-30,-8,-16],[-14,-1,-18],[8,-3,-20],[24,4,-22],[4,9,-24],[-14,14,-26],
         [-2,20,-28],[16,24,-30],[2,30,-32],[-8,35,-34]]});
  g.add(road.g);
  /* 鸟道：崖壁上部一线窄岩脊 */
  const ledge=makePlankRoad({w:1.5,color:0x1a120b,rimC:0xd8a868,rim:0.36,
    pts:[[-40,42,-30],[-10,46,-32],[24,42,-34],[52,46,-36]]});
  g.add(ledge.g);
  /* 崩落的山石（地崩山摧）：横在栈道下缘的乱石，压住画面底边 */
  const rocks=[];
  [[-26,-2,-14,4.2],[2,0,-12,5.0],[24,1,-14,3.6],[-8,10,-10,2.8]].forEach(function(p,i){
    const r=makeForeground({kind:'坡石',n:1,r:p[3],w:0,d:0,color:0x0e0a07,seed:2210+i,rim:0.28,rimC:0xd9a05a});
    r.g.position.set(p[0],p[1],p[2]); g.add(r.g); rocks.push(r);
  });
  const bird=makeBird({scale:2.8,color:0x110c08,ph:0.6,flap:2.6}); g.add(bird);
  const mist=makeMist({n:9,spread:[190,20,110],pos:[0,-10,-42],scale:62,color:0x8a6a48,op:0.13});
  g.add(mist.g);
  const dust=makeFlow({n:520,box:[170,20,120],pos:[0,-4,-40],color:0xa8825a,size:18,speed:2.6,maxA:0.16});
  g.add(dust.points);
  /* 前景：贴相机的暗崖两角 + 头顶压下来的暗岩 */
  const fgL=makeForeground({kind:'岩壁',n:2,r:3.8,w:22,d:9,color:0x050303,seed:2217,rim:0.18,rimC:0xa87848});
  fgL.g.position.set(-22,2,16); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:3.2,w:20,d:8,color:0x050303,seed:2221,rim:0.18,rimC:0xa87848});
  fgR.g.position.set(13,0,14); g.add(fgR.g);
  const fgTop=makeForeground({kind:'岩壁',n:2,r:3.0,w:20,d:9,color:0x050303,seed:2227,rim:0.16,rimC:0xa87848});
  fgTop.g.position.set(-4,30,10); g.add(fgTop.g);
  addLights(g,{c:0xd9a05a,i:0.58,p:[-100,80,-70]},{c:0x37271a,i:0.60});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.5); mist.update(t,k); dust.update(t);
    fgL.update(t,k); fgR.update(t,k); fgTop.update(t,k);
    bird.update(t);
    bird.position.set(-20+Math.sin(t*0.16)*38,52+Math.sin(t*0.5)*3,-46);
    bird.rotation.y=-t*0.16+Math.PI/2;
    for(const r of rocks) r.update(t,k);
  }};
}
function bGaobiao(){ // 三 · 高标回川 —— 六龙回日之高标，冲波逆折之回川
  const g=new THREE.Group();
  /* 回川：逆着流向反卷的江水（flow 取负 = 水往回卷） */
  const water=makeWater({size:280,seg:72,amp:2.4,freq:0.06,speed:1.5,flow:[0,-2.9],spec:1.9,
    deep:0x101a1e,shallow:0x36484a,skyc:0x8a5426,moonDir:[0.35,0.62,-1],moonColor:0xffdca8,y:-12});
  g.add(water.mesh);
  const far=makeRange({r:140,h:104,layers:3,peaks:5,seed:3303,color:0x1c140d,atmo:0x8a5a2c,
    fogK:0.50,glowK:0.16,y:-30,arc:Math.PI*1.4,a0:-Math.PI*0.7});
  g.add(far.g);
  /* 高标：插入天穹的巨峰，峰尖将将顶到画框上缘（上有六龙回日之高标） */
  const biao=makeBiao({h:112,r:19,color:0x35230f,seed:3301,rim:0.48,rimC:0xf8d08a});
  biao.g.position.set(-6,-10,-62); g.add(biao.g);
  /* 六龙回日：日轮贴着峰肩，龙车到此也要折返 */
  const sun=makeSunDisc({r:17,color:0xfff6da,glowC:0xff9a3a,glow:250});
  sun.g.position.set(34,58,-192); g.add(sun.g);
  const cL=makeCliffWall({n:2,h:92,w:44,seed:3305,color:0x2e1c0e,rimC:0xd9a05a,rim:0.36,y:-34,zjit:12});
  cL.g.position.set(-80,-6,-58); cL.g.rotation.y=0.24; g.add(cL.g);
  const cR=makeCliffWall({n:2,h:84,w:40,seed:3309,color:0x2a1908,rimC:0xd9a05a,rim:0.36,y:-34,zjit:12});
  cR.g.position.set(84,-6,-54); cR.g.rotation.y=-0.22; g.add(cR.g);
  /* 冲波逆折：浪头逆着水面回卷的白沫（收在水口宽度内） */
  const foam=makeGlow({n:360,box:[74,8,26],pos:[0,-4,-46],color:0xe8f4ff,size:8,speed:0.9,rise:1,maxA:0.50});
  foam.points.renderOrder=4; g.add(foam.points);
  const spray=makeGlow({n:190,box:[62,16,24],pos:[0,2,-48],color:0xf0f8ff,size:6,speed:1.2,rise:1,maxA:0.40});
  spray.points.renderOrder=4; g.add(spray.points);
  /* 黄鹤之飞尚不得过：一只大鹤贴峰腰掠过却"过不去" */
  const crane=makeBird({scale:4.6,color:0x15141a,flap:2.0,ph:0.4}); g.add(crane);
  /* 猿猱欲度愁攀援：崖壁上攀援的两只猿 */
  const apeL=makeApe({scale:2.0,ph:0.2,color:0x181310}), apeR=makeApe({scale:1.7,ph:1.5,color:0x1c150f});
  apeL.position.set(-46,2,-44); apeL.rotation.y=0.5; g.add(apeL);
  apeR.position.set(-26,11,-42); apeR.rotation.y=0.25; g.add(apeR);
  const mist=makeMist({n:9,spread:[200,24,110],pos:[0,14,-64],scale:64,color:0xa07850,op:0.11});
  g.add(mist.g);
  const fog=makeMist({n:6,spread:[150,12,70],pos:[0,-6,-44],scale:50,color:0xbfd0dc,op:0.12});
  g.add(fog.g);
  const fgL=makeForeground({kind:'岩壁',n:3,r:4.2,w:24,d:11,color:0x050303,seed:3313,rim:0.18,rimC:0xb88048});
  fgL.g.position.set(-16,2,26); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:3.4,w:20,d:9,color:0x050303,seed:3317,rim:0.18,rimC:0xb88048});
  fgR.g.position.set(17,1,22); g.add(fgR.g);
  addLights(g,{c:0xe8bc82,i:0.78,p:[110,90,-120]},{c:0x40301e,i:0.62});
  const pl=new THREE.PointLight(0xcfe4ff,0.55,150); pl.position.set(0,-2,-46); g.add(pl);
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.4); sun.update(t,k);
    water.update(t); mist.update(t,k); fog.update(t,k); foam.update(t); spray.update(t);
    fgL.update(t,k); fgR.update(t,k); apeL.update(t); apeR.update(t);
    const a=t*0.14;
    crane.update(t);
    crane.position.set(-2+Math.sin(a)*42,44+Math.sin(t*0.45)*4,-92+Math.cos(a)*22);
    crane.rotation.y=-a+Math.PI/2;
    pl.intensity=k*(0.40+0.12*Math.sin(t*1.9));
    foam.mat.uniforms.uMaxA.value=k*(0.28+0.18*Math.sin(t*0.8));
  }};
}
function bShenjing(){ // 四 · 扪参历井 —— 百步九折萦岩峦，仰可扪星，抚膺长叹
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x080706,c2:0x1e1710}); grd.mesh.position.y=-34; g.add(grd.mesh);
  const far=makeRange({r:145,h:116,layers:2,peaks:6,seed:4401,color:0x121016,atmo:0x4a4a60,
    fogK:0.60,glowK:0.07,y:-34,arc:Math.PI*1.3,a0:-Math.PI*0.65});
  g.add(far.g);
  /* 参宿（猎户）+ 井宿（井字）："扪参历井"必须在天上看得见 */
  const can=makeAsterism({size:9,op:0.96,
    nodes:[[-96,148,-252],[-74,178,-256],[-50,156,-260],[-56,134,-262],[-78,124,-264],[-22,162,-266],[-10,140,-268]],
    links:[[0,1],[1,2],[2,3],[3,4],[4,0],[1,5],[5,6],[6,2]]});
  g.add(can.g);
  const jing=makeAsterism({size:8,op:0.92,color:0xd6e4ff,lineColor:0x9fb6e0,lineOp:0.30,
    nodes:[[44,126,-256],[68,126,-258],[44,152,-260],[68,152,-262],[56,139,-264]],
    links:[[0,1],[0,2],[1,3],[2,3]]});
  g.add(jing.g);
  const cliff=makeCliffWall({n:3,h:116,w:46,seed:4407,color:0x2a1e16,rimC:0xc8c0d8,rim:0.34,y:-36,zjit:10});
  cliff.g.position.set(6,-4,-52); g.add(cliff.g);
  /* 青泥盘道：百步九折，绕岩而上（一路盘向星空） */
  const road=makePlankRoad({w:3.2,color:0x241a12,rimC:0xd0c8e0,rim:0.48,
    pts:[[-34,6,-30],[-16,14,-32],[6,10,-34],[22,18,-36],[2,24,-38],[-16,30,-40],
         [-2,36,-42],[16,40,-44],[0,46,-46],[-12,52,-48]]});
  g.add(road.g);
  /* 以手抚膺坐长叹：栈道上坐着的行人（沉入地面 = 坐姿，靠边缘光读出人形） */
  const f=makeFigure({pose:'坐饮',robe:0x24262f,belt:0x6a5638,hat:'幞头',beard:true,scale:2.0,face:0.35,
    rim:0.70,rimC:0xdcd0c0,noProp:true});
  f.position.set(8,6.4,-34); g.add(f);
  const mist=makeMist({n:8,spread:[180,20,100],pos:[0,2,-48],scale:58,color:0x7a7286,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:110,box:[150,90,110],pos:[0,56,-70],color:0xcfd8ff,size:4,speed:0.03,rise:0,maxA:0.40});
  g.add(motes.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:3.6,w:22,d:10,color:0x040405,seed:4411,rim:0.20,rimC:0x9a92b0});
  fgL.g.position.set(-9,8,20); g.add(fgL.g);
  const fgR=makeForeground({kind:'树枝',n:20,w:30,d:5,color:0x040405,seed:4417,sway:0.5});
  fgR.g.position.set(20,10,17); g.add(fgR.g);
  addLights(g,{c:0x9fb0d8,i:0.38,p:[-80,110,-140]},{c:0x2a2c3c,i:0.58});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.4); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k); f.update(t,k);
  }};
}
function bZigui(){ // 五 · 悲鸟子规 —— 悲鸟绕古木，子规啼夜月，朱颜凋落
  const g=new THREE.Group();
  const grd=makeGround({r:160,c1:0x08070a,c2:0x1e1812}); grd.mesh.position.y=-14; g.add(grd.mesh);
  const far=makeRange({r:150,h:104,layers:3,peaks:6,seed:5501,color:0x141216,atmo:0x5a463c,
    fogK:0.54,glowK:0.09,y:-20,arc:Math.PI*1.35,a0:-Math.PI*0.675});
  g.add(far.g);
  const cliff=makeCliffWall({n:3,h:96,w:44,seed:5502,color:0x241d18,rimC:0xa8a8b8,rim:0.26,y:-26,zjit:10});
  cliff.g.position.set(-4,-2,-70); g.add(cliff.g);
  /* 古木：三株虬曲老树（悲鸟号古木），树身从画面下缘伸进来 */
  const trees=[];
  const t1=makeTree({h:30,bend:3.8,branches:9,blen:0.50,leaf:0x2c3c2c,color:0x2a2018,seed:5503,sway:0.5,r:1.5});
  t1.g.position.set(-22,-8,-30); g.add(t1.g); trees.push(t1);
  const t2=makeTree({h:24,bend:3.0,branches:8,blen:0.56,leaf:0x243424,color:0x241c14,seed:5507,sway:0.6,r:1.3});
  t2.g.position.set(22,-8,-34); g.add(t2.g); trees.push(t2);
  const t3=makeTree({h:20,bend:4.4,branches:8,blen:0.62,dead:true,color:0x201811,seed:5511,sway:0.5,r:1.2});
  t3.g.position.set(-1,-8,-26); g.add(t3.g); trees.push(t3);
  /* 雄飞雌从绕林间：两只大鸟绕树盘旋 */
  const birds=[];
  for(let i=0;i<2;i++){ const b=makeBird({scale:2.6+i*0.5,color:0x161418,flap:3.6,ph:i*2.4}); g.add(b); birds.push(b); }
  /* 又闻子规啼夜月：一只小鸟栖在枯枝上，朝着月 */
  const zigui=makeBird({scale:1.5,color:0x1c1a20,flap:0.5,ph:1.1}); g.add(zigui);
  /* 凋朱颜：几片红叶缓缓坠落（把"朱颜凋"物质化） */
  const leaves=makeGlow({n:100,box:[60,36,36],pos:[0,12,-26],color:0xb8402a,size:5.5,speed:0.075,rise:1,maxA:0.62});
  leaves.points.renderOrder=4; g.add(leaves.points);
  const mist=makeMist({n:10,spread:[210,22,120],pos:[0,-2,-46],scale:64,color:0x7c6c6c,op:0.11});
  g.add(mist.g);
  /* 前景：贴相机的枯枝（最近一层，"绕林间"的框） */
  const br=makeForeground({kind:'树枝',n:22,w:32,d:5,color:0x050405,seed:5517,sway:0.55});
  br.g.position.set(8,8,15); g.add(br.g);
  const fg=makeForeground({kind:'岩壁',n:2,r:3.4,w:20,d:9,color:0x050405,seed:5519,rim:0.18,rimC:0x9a8a8a});
  fg.g.position.set(-20,4,13); g.add(fg.g);
  addLights(g,{c:0xc4d2e8,i:0.38,p:[-80,100,-140]},{c:0x2c2e3c,i:0.60});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.4); mist.update(t,k); leaves.update(t);
    fg.update(t,k); br.update(t,k);
    for(const tr of trees) tr.update(t,k);
    for(let i=0;i<birds.length;i++){
      const a=t*(0.30+i*0.07)+i*2.6;
      birds[i].update(t);
      birds[i].position.set(-8+Math.sin(a)*22,22+Math.cos(a*1.4)*5+(i?2:0),-30+Math.cos(a)*13);
      birds[i].rotation.y=-a+Math.PI/2;
    }
    zigui.update(t);
    zigui.position.set(-3.4,11.2,-27.4);
    zigui.rotation.y=2.3;
  }};
}
function bLianfeng(){ // 六 · 连峰飞湍（标志性瞬间）—— 绝壁如墙逼近天穹，枯松倒挂，飞瀑坠雷
  const g=new THREE.Group();
  const grd=makeGround({r:190,c1:0x0b0806,c2:0x2c2014}); grd.mesh.position.y=-8; g.add(grd.mesh);
  /* 三层峰：远层混天光（渐淡）→ 中层压暗 → 近层绝壁如墙（主体受光，顶出画框） */
  const far=makeRange({r:165,h:172,layers:3,peaks:7,seed:6601,color:0x1e160e,atmo:0xa87238,
    fogK:0.42,glowK:0.20,y:-34,arc:Math.PI*1.3,a0:-Math.PI*0.65});
  g.add(far.g);
  const mid=makeCliffWall({n:5,h:150,w:50,seed:6605,color:0x33210f,rimC:0xd8a05a,rim:0.28,y:-28,zjit:16});
  mid.g.position.set(-6,-2,-100); g.add(mid.g);
  const wall=makeCliffWall({n:7,h:120,w:46,seed:6607,color:0x4a2c12,rimC:0xffd894,rim:0.50,y:-16,zjit:14});
  wall.g.position.set(0,-2,-54); g.add(wall.g);
  /* 远处的"高标"：点击后从雾里长出来 */
  const biao=makeBiao({h:150,r:26,color:0x3a2612,seed:6611,rim:0.50,rimC:0xffe0a0});
  biao.g.position.set(-84,-12,-152); g.add(biao.g);
  /* 枯松倒挂倚绝壁：倒挂在崖檐上的枯松（本诗最标志性的细节） */
  const pines=[];
  [[-52,34,-44,1.05,7],[-26,46,-46,1.25,9],[6,38,-42,0.95,11],[32,50,-46,1.30,13],[56,40,-44,1.05,17]]
  .forEach(function(p){
    const tr=makeTree({h:30*p[3],bend:3.2,branches:9,blen:0.54,dead:true,hang:true,color:0x261b12,
      seed:p[4],sway:0.7,r:1.35*p[3]});
    tr.g.position.set(p[0],p[1],p[2]); g.add(tr.g); pines.push(tr);
  });
  /* 飞湍瀑流争喧豗：六道高差不同、宽窄不同的水瀑（锥形面片，合并成 1 个 draw call） */
  const falls=makeFalls({tint:0xbfe0ff,items:[
    {x:-50,y:18,z:-46,w:11,h:44},{x:-30,y:28,z:-48,w:7,h:36},{x:-6,y:22,z:-44,w:15,h:52},
    {x:20,y:30,z:-48,w:8,h:38},{x:42,y:20,z:-46,w:12,h:46},{x:64,y:26,z:-48,w:6,h:34}]});
  g.add(falls.g);
  /* 砯崖：瀑流砸在崖脚石上的撞点（给瀑布一个"落点"，不是悬空的布） */
  const hits=[];
  [[-50,8,-46,5.2],[-6,10,-44,6.4],[42,8,-46,5.6]].forEach(function(p,i){
    const r=makeForeground({kind:'坡石',n:1,r:p[3],w:0,d:0,color:0x120c07,seed:6613+i,rim:0.32,rimC:0xe8b878});
    r.g.position.set(p[0],p[1],p[2]); g.add(r.g); hits.push(r);
  });
  /* 撞崖炸开的白雾与水沫：分三团收在水口上，不铺满整条谷 */
  const foams=[];
  [[-50,9,-46,46],[-6,11,-44,60],[42,9,-46,48]].forEach(function(p,i){
    const f2=makeGlow({n:150,box:[p[3],7,20],pos:[p[0],p[1],p[2]],color:0xe6f2fa,size:7,
      speed:0.95,rise:1,maxA:0.52});
    f2.points.renderOrder=4; g.add(f2.points); foams.push(f2);
  });
  const spray=makeGlow({n:220,box:[150,18,36],pos:[0,20,-48],color:0xf0f8ff,size:5.5,speed:1.3,rise:1,maxA:0.38});
  spray.points.renderOrder=4; g.add(spray.points);
  const flood=makeFlow({n:640,box:[190,16,130],pos:[0,4,-42],color:0xba9668,size:18,speed:5.5,maxA:0.18});
  g.add(flood.points);
  /* 嗟尔远道之人：崖下栈道上一个背身而立的行人（给巨崖一个尺度参照） */
  const road=makePlankRoad({w:3.0,color:0x241a12,rimC:0xf0c488,rim:0.50,
    pts:[[-20,-1,-30],[4,0,-28],[28,1,-26]]});
  g.add(road.g);
  const man=makeFigure({pose:'独立',robe:0x1c1e26,belt:0x8a6a33,hat:'幞头',scale:1.45,face:2.7,rim:0.66,rimC:0xf0c880});
  man.position.set(4,0,-30); g.add(man);
  /* 前景：贴相机的暗崖左右夹击 + 头顶垂下的倒挂枯松 */
  const fgL=makeForeground({kind:'岩壁',n:3,r:5.4,w:28,d:12,color:0x050403,seed:6621,rim:0.18,rimC:0xb88048});
  fgL.g.position.set(-18,2,26); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:4.4,w:24,d:11,color:0x050403,seed:6627,rim:0.18,rimC:0xb88048});
  fgR.g.position.set(30,0,22); g.add(fgR.g);
  const fgPine=makeTree({h:32,bend:3.0,branches:8,blen:0.52,dead:true,hang:true,color:0x1c140d,seed:6631,sway:0.6,r:1.5});
  fgPine.g.position.set(-22,46,6); g.add(fgPine.g);
  const sun=makeSunDisc({r:19,color:0xfff2d4,glowC:0xe8822a,glow:280});
  sun.g.position.set(-70,92,-210); g.add(sun.g);
  const mist=makeMist({n:10,spread:[230,30,130],pos:[0,34,-82],scale:68,color:0xa8805a,op:0.10});
  g.add(mist.g);
  addLights(g,{c:0xecc088,i:0.90,p:[-150,95,-140]},{c:0x48341e,i:0.74});
  const pl=new THREE.PointLight(0xdfefff,0.62,180); pl.position.set(0,14,-46); g.add(pl);
  const burst=makeBurst({n:190,color:0xeaf4ff,pos:[0,18,-48]}); g.add(burst.points);
  let power=0, reveal=0;
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    power=Math.max(0,power-dt*0.42);
    reveal=Math.max(0,reveal-dt*0.30);
    const rv=sstep(0,1.2,reveal+power);
    falls.update(t); spray.update(t); flood.update(t); mist.update(t,k); sun.update(t,k);
    for(const f2 of foams) f2.update(t);
    for(const p of pines) p.update(t,k);
    for(const r of hits) r.update(t,k);
    man.update(t,k);
    fgL.update(t,k); fgR.update(t,k); fgPine.update(t,k);
    burst.update(t);
    foams.forEach(function(f2,i){
      f2.mat.uniforms.uMaxA.value=k*(0.26+0.14*Math.sin(t*0.9+i*1.7)+0.24*power);
    });
    spray.mat.uniforms.uMaxA.value=k*(0.22+0.12*Math.sin(t*1.1+1)+0.24*power);
    pl.intensity=k*(0.36+0.14*Math.sin(t*2.3)+0.44*power);
    /* 高标显形：从雾里长出来（本体提亮 + 山头抬高） */
    biao.mat.opacity=k*(0.26+0.74*rv);
    biao.g.scale.setScalar(0.92+0.08*rv);
    biao.g.position.y=-12+5*rv;
  },click(){
    if(power>0.6)return;
    power=1; reveal=1.2; burst.fire(); roar();
    const fl=$('#flash'); fl.textContent='万壑雷！'; fl.classList.remove('go');
    void fl.offsetWidth; fl.classList.add('go');
  }};
}
function bJiange(){ // 七 · 剑阁崔嵬 —— 一夫当关，万夫莫开；侧身西望长咨嗟
  const g=new THREE.Group();
  const grd=makeGround({r:190,c1:0x0a0806,c2:0x281c12}); grd.mesh.position.y=-16; g.add(grd.mesh);
  const far=makeRange({r:150,h:126,layers:3,peaks:6,seed:7701,color:0x17110b,atmo:0x74522e,
    fogK:0.50,glowK:0.13,y:-26,arc:Math.PI*1.35,a0:-Math.PI*0.675});
  g.add(far.g);
  /* 剑门：两壁夹峙，关楼就在这一线之间（峥嵘而崔嵬） */
  const cL=makeCliffWall({n:2,h:104,w:42,seed:7703,color:0x40280f,rimC:0xf0bc78,rim:0.46,y:-22,zjit:10});
  cL.g.position.set(-70,-4,-58); cL.g.rotation.y=0.20; g.add(cL.g);
  const cR=makeCliffWall({n:3,h:112,w:46,seed:7707,color:0x3c2610,rimC:0xf0bc78,rim:0.46,y:-22,zjit:10});
  cR.g.position.set(76,-4,-54); cR.g.rotation.y=-0.18; g.add(cR.g);
  const gate=makeGate({w:26,h:22,d:11,color:0x34220f});
  gate.g.position.set(26,-8,-54); gate.g.rotation.y=-0.20; g.add(gate.g);
  /* 高标：关外更远处的巨峰（点击显形） */
  const biao=makeBiao({h:126,r:22,color:0x362418,seed:7711,rim:0.46,rimC:0xf8d492});
  biao.g.position.set(74,-12,-132); g.add(biao.g);
  /* 万夫莫开：关下列阵的人影与旗影 */
  const crowd=makeCrowd({n:16,rect:[-6,-40,56,11],seed:7717,color:0x171922,rimC:0xe09a44,rim:0.34,sMin:0.9,sMax:1.15,y:-10});
  g.add(crowd.mesh);
  const banners=[];
  [[10,-34,13],[32,-36,15],[52,-32,12]].forEach(function(p,i){
    const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.26,0.38,p[2],6),
      new THREE.MeshPhongMaterial({color:0x1c1409,shininess:6}));
    pole.position.set(p[0],-10+p[2]/2,p[1]); g.add(pole);
    const bn=makeBanner({w:5.4,h:3.0,color:0x8a3218,ph:i*2.1});
    bn.mesh.position.set(p[0]+3.0,-10+p[2]-2.1,p[1]); g.add(bn.mesh);
    banners.push(bn);
  });
  /* 朝避猛虎，夕避长蛇：关前暗处的兽影（磨牙吮血）+ 拖过岩面的长蛇 */
  const beasts=[];
  const b1=makeBeast({scale:2.2,ph:0.4,color:0x171009}); b1.position.set(-24,-10,-38); b1.rotation.y=-0.7;
  g.add(b1); beasts.push(b1);
  const b2=makeBeast({scale:1.8,ph:2.1,color:0x140f0b}); b2.position.set(12,-10,-26); b2.rotation.y=2.5;
  g.add(b2); beasts.push(b2);
  const snake=makeSnake({len:34,r:0.5,ph:0.8});
  snake.g.position.set(-4,-9,-22); snake.g.rotation.y=0.12; g.add(snake.g);
  /* 关楼火把 + 两盏灯笼：森然里的暖点 */
  const flames=[];
  [[14.6,0,-49.4],[37.4,0,-49.4]].forEach(function(p,i){
    const fl=makeFlame({h:3.2,w:1.5,planes:3,embers:24,spark:i===0,light:0.9,lightD:54,wide:0.36,seed:7719+i});
    fl.g.position.set(p[0],p[1],p[2]); g.add(fl.g); flames.push(fl);
  });
  const lans=[];
  [[12.2,6.0,-49],[39.8,6.2,-49]].forEach(function(p,i){
    const l=makeLantern(0.56,{flame:i===0}); l.position.set(p[0],p[1],p[2]); g.add(l); lans.push(l);
  });
  /* 侧身西望长咨嗟：崖台上的行人，侧身朝西（朝着锦城灯火的方向） */
  const man=makeFigure({pose:'独立',robe:0x1e2028,belt:0x7a5a34,hat:'幞头',beard:true,scale:1.9,face:-1.6,
    rim:0.66,rimC:0xf0c880});
  man.position.set(-14,-10,-34); g.add(man);
  /* 锦城虽云乐：西望处极远处的暖色灯火（与关下的森然对冲） */
  const city=makeGlow({n:130,box:[52,12,18],pos:[-62,2,-152],color:0xffc070,size:6,speed:0.05,rise:0,maxA:0.50});
  g.add(city.points);
  const cityGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
    transparent:true,opacity:0.34,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  cityGlow.scale.set(96,40,1); cityGlow.position.set(-62,6,-160); cityGlow.renderOrder=3; g.add(cityGlow);
  const mist=makeMist({n:10,spread:[220,26,120],pos:[0,4,-72],scale:64,color:0x8a6a4c,op:0.10});
  g.add(mist.g);
  const dust=makeFlow({n:520,box:[190,18,130],pos:[0,-4,-40],color:0xa8825a,size:18,speed:2.4,maxA:0.16});
  g.add(dust.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:4.2,w:24,d:12,color:0x050403,seed:7723,rim:0.18,rimC:0xb88048});
  fgL.g.position.set(-12,2,20); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:3.6,w:22,d:10,color:0x050403,seed:7727,rim:0.18,rimC:0xb88048});
  fgR.g.position.set(28,0,16); g.add(fgR.g);
  addLights(g,{c:0xe0b070,i:0.54,p:[-120,80,-120]},{c:0x3a2a1c,i:0.60});
  const pl=new THREE.PointLight(0xffb066,0.78,64); pl.position.set(26,4,-48); g.add(pl);
  const burst=makeBurst({n:180,color:0xffd9a0,pos:[26,8,-52]}); g.add(burst.points);
  let power=0, reveal=0;
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    power=Math.max(0,power-dt*0.40);
    reveal=Math.max(0,reveal-dt*0.28);
    const rv=sstep(0,1.2,reveal+power);
    far.update(t,mouse.x*0.4); mist.update(t,k); dust.update(t); city.update(t);
    crowd.update(t); man.update(t,k); snake.update(t);
    for(const f2 of flames) f2.update(t,k);
    for(const l of lans) l.update(t,k);
    for(const b of banners) b.update(t);
    for(const b of beasts) b.update(t,k);
    fgL.update(t,k); fgR.update(t,k); burst.update(t);
    pl.intensity=k*(0.38+0.14*Math.sin(t*3.3)+0.44*power);
    cityGlow.material.opacity=k*0.34*(0.80+0.20*Math.sin(t*1.3));
    biao.mat.opacity=k*(0.30+0.70*rv);
    biao.g.scale.setScalar(0.92+0.08*rv);
  },click(){
    if(power>0.6)return;
    power=1; reveal=1.2; burst.fire(); roar();
    const fl=$('#flash'); fl.textContent='万夫莫开！'; fl.classList.remove('go');
    void fl.offsetWidth; fl.classList.add('go');
  }};
}
