/* ================= 诉衷情·当年万里觅封侯 · 三境场景（大漠金戈：梦戍梁州、尘暗貂裘、天山沧洲） =================
   美术立意：大漠金戈赛道——底色 #120d08、雾 #1a120a 系、accent=#b0906a（取自 queue，用于人物边缘光/旗纹/
   烽火光池），禁艳金。全页情绪轴：梦里大漠金戈的暖亮 vs 现实沧洲渔屋的冷灰。
   境①梦戍梁州（全页最暖最亮：年少戎装、军马、战旗、烽燧、关城剪影——一问「梦断何处」收）；
   境②尘暗貂裘（转冷：檐下衣架蒙尘的旧貂裘、霜鬓老人、冷月入窗、尘光浮游）；
   境③天山沧洲（全词结穴·标志性瞬间）：天山雪岭的幻象与沧洲茅屋的现实同框对切，
   末境点击貂裘（queue interact）：尘光自裘上浮起 + 天山侧年少戎装的「对影」显形，与沧洲老人隔水相望。
   情感曲线：梦暖金戈 → 尘暗泪空 → 心身两地撕裂。 */

/* —— 军马：匹马侧影（身/颈/首/耳/四足/尾/鞍鞯 合批 1 mesh，剪影靠轮廓与边缘光读出）—— */
function makeJunma(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.05,12,9); body.scale(1.65,0.78,0.66);
  body.translate(0,2.05,0); B.put(body,shadeColor(0x171009,1.0));
  const neck=new THREE.CylinderGeometry(0.30,0.52,1.55,8);
  neck.rotateZ(-0.62); neck.translate(1.42,2.95,0); B.put(neck,0x140e08);
  const head=new THREE.BoxGeometry(0.42,0.46,0.5); head.rotateZ(0.34);
  head.translate(2.22,3.42,0); B.put(head,0x120c07);
  const muzzle=new THREE.BoxGeometry(0.3,0.26,0.4); muzzle.rotateZ(0.5);
  muzzle.translate(2.52,3.18,0); B.put(muzzle,0x100a06);
  [-0.16,0.16].forEach(function(s){
    const ear=new THREE.ConeGeometry(0.09,0.3,5); ear.translate(1.98,3.78,s); B.put(ear,0x120c07);
  });
  [[0.95,0.42],[0.95,-0.42],[-0.95,0.42],[-0.95,-0.42]].forEach(function(p){
    const leg=new THREE.CylinderGeometry(0.11,0.09,2.0,6);
    leg.translate(p[0],1.0,p[1]); B.put(leg,0x120c07);
  });
  const tail=new THREE.ConeGeometry(0.13,1.15,6); tail.rotateZ(2.6);
  tail.translate(-1.72,2.2,0); B.put(tail,0x0e0906);
  const saddle=new THREE.BoxGeometry(1.0,0.16,1.0); saddle.translate(-0.1,2.78,0);
  B.put(saddle,0x5a3a1c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x241a10,emissive:0x040302}),{c:0xb0906a,i:o.rim===undefined?0.26:o.rim,p:2.6})));
  return g;
}

/* —— 貂裘：衣架（立杆+横杆+叉脚底座）+ 蒙尘貂裘（垂坠袍形+毛领），合批 1 mesh ——
   「尘暗旧貂裘」的本体：境②的静物主角，境③的点击对象。 */
function makeDiaoyu(o){
  o=o||{};
  const h=o.h===undefined?3.3:o.h;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.06,0.09,h,7); pole.translate(0,h/2,0); B.put(pole,0x191209);
  const bar=new THREE.CylinderGeometry(0.055,0.055,1.7,7); bar.rotateZ(Math.PI/2);
  bar.translate(0,h,0); B.put(bar,0x191209);
  const knob=new THREE.SphereGeometry(0.09,8,6); knob.translate(0,h+0.07,0); B.put(knob,0x3a2c18);
  [[0.55,0],[-0.55,0],[0,-0.55],[0,0.55]].forEach(function(p){
    const foot=new THREE.CylinderGeometry(0.045,0.06,0.9,6); foot.rotateZ(p[0]?Math.PI/2*(p[0]>0?-1:1):0);
    foot.rotateX(p[1]?Math.PI/2*(p[1]>0?1:-1):0);
    foot.translate(p[0]*0.5,0.42,p[1]*0.5); B.put(foot,0x171009);
  });
  /* 裘身：肩线挂在横杆下，垂坠到下摆张开（上收肩、中束腰、下摆宽） */
  const coat=new THREE.LatheGeometry([[0.05,0.0],[0.58,0.06],[0.68,0.5],[0.55,1.1],[0.50,1.6],[0.58,2.1],[0.70,2.45],[0.34,2.62]]
    .map(p=>new THREE.Vector2(p[0],p[1])),14);
  coat.scale(1.3,1,0.6); coat.translate(0,h-2.62,0); B.put(coat,0x4d3826);
  const hem=new THREE.TorusGeometry(0.70,0.05,5,14); hem.rotateX(Math.PI/2); hem.scale(1.3,1,0.6);
  hem.translate(0,h-2.56,0); B.put(hem,0x3a2a1a);
  const collar=new THREE.TorusGeometry(0.34,0.09,6,12); collar.rotateX(Math.PI/2);
  collar.scale(1.3,1,0.72); collar.translate(0,h-0.24,0); B.put(collar,0x5f462a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2014,emissive:0x060402}),{c:0xb0906a,i:o.rim===undefined?0.22:o.rim,p:2.6})));
  return g;
}

/* —— 茅屋：沧洲渔隐的草顶老屋（夯土墙+草檐+门+冷窗，合批 1 mesh）—— */
function makeCaowu(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, d=o.d===undefined?5:o.d, hh=o.h===undefined?2.6:o.h;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,hh,d); wall.translate(0,hh/2,0); B.put(wall,0x1a130c);
  const roof=new THREE.ConeGeometry(w*0.86,1.9,4); roof.rotateY(Math.PI/4);
  roof.scale(1.08,1,0.92); roof.translate(0,hh+0.92,0); B.put(roof,0x241a10);
  const eave=new THREE.BoxGeometry(w*1.25,0.14,d*1.2); eave.translate(0,hh+0.05,0); B.put(eave,0x1e150d);
  const door=new THREE.BoxGeometry(0.95,1.6,0.1); door.translate(w*0.18,0.8,d/2+0.03); B.put(door,0x0d0906);
  const win=new THREE.BoxGeometry(0.8,0.7,0.1); win.translate(-w*0.2,hh*0.62,d/2+0.03); B.put(win,0x30281c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x1d160e,emissive:0x050302}),{c:0xb0906a,i:o.rim===undefined?0.16:o.rim,p:2.8})));
  return g;
}

/* —— 渔舟：沧洲水上的小船（船身+船篷+短桨 合批 1 mesh，随波轻晃）—— */
function makeYuzhou(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const hull=new THREE.LatheGeometry([[0,0.04],[0.55,0.04],[0.8,0.2],[0.88,0.46]]
    .map(p=>new THREE.Vector2(p[0],p[1])),10);
  hull.scale(0.8,0.5,2.3); B.put(hull,0x0e0a07);
  const canopy=new THREE.CylinderGeometry(0.55,0.55,1.6,8); canopy.rotateX(Math.PI/2);
  canopy.scale(1,0.62,1); canopy.translate(-0.15,0.62,0.1);
  B.put(canopy,0x1c140c);
  const oar=new THREE.CylinderGeometry(0.04,0.05,2.0,5); oar.rotateZ(1.15); oar.rotateY(0.25);
  oar.translate(0.75,0.35,0.9); B.put(oar,0x141009);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x241a10,emissive:0x040302}),{c:0xb0906a,i:0.2,p:2.6}));
  mesh.renderOrder=1;
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(sc);
  return {g,ph,update(t){
    g.position.y=this.y0+0.1*Math.sin(t*0.75+ph);
    g.rotation.z=0.022*Math.sin(t*0.62+ph);
  }};
}

/* —— 烽燧：边关烽火台（收分方台+垛口，合批 1 mesh）——大漠天际线的城垣剪影 —— */
function makeFengsui(o){
  o=o||{};
  const h=o.h===undefined?9:o.h, w=o.w===undefined?3.2:o.w;
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(w*0.62,w,h,4); body.rotateY(Math.PI/4);
  body.translate(0,h/2,0); B.put(body,shadeColor(0x15100a,1.0));
  const cap=new THREE.BoxGeometry(w*1.15,0.5,w*1.15); cap.translate(0,h+0.2,0); B.put(cap,0x17110b);
  for(let i=-1;i<=1;i++){
    const mer=new THREE.BoxGeometry(0.5,0.7,0.5); mer.translate(i*w*0.34,h+0.75,0); B.put(mer,0x120d08);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xb0906a,i:o.rim===undefined?0.14:o.rim,p:2.8})));
  return g;
}

/* —— 台地：大漠戈壁的桌状山剪影（收分四棱台×n，合批 1 mesh，替代圆山顶）—— */
function makeTaidi(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19701:o.seed);
  const n=o.n===undefined?5:o.n, w=o.w===undefined?170:o.w;
  const y0=o.y===undefined?0:o.y;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const ww=(4+R()*9)*(o.sMax===undefined?1:o.sMax);
    const hh=(2.2+R()*4.5)*(o.hMax===undefined?1:o.hMax);
    const mesa=new THREE.CylinderGeometry(ww*0.78,ww,hh,4);
    mesa.rotateY(R()*Math.PI); mesa.translate((R()-0.5)*w,y0+hh/2,(R()-0.5)*22);
    B.put(mesa,shadeColor(0x100b07,0.75+0.5*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x1d160e,emissive:0x030201}),{c:0xb0906a,i:o.rim===undefined?0.10:o.rim,p:2.8})));
  return g;
}

/* —— 战旗：旗杆+杆顶+暗赭战旗（旗面摆动，2 draw call）——「匹马戍梁州」的军阵旗影 —— */
function makeDaqi(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.08,0.11,h,6); pole.translate(0,h/2,0); B.put(pole,0x0b0806);
  const fin=new THREE.SphereGeometry(0.16,8,6); fin.translate(0,h+0.1,0); B.put(fin,0x6a5030);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xb0906a,i:0.2,p:2.6})));
  const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.7,1.7,5,2),
    new THREE.MeshPhongMaterial({color:o.flagC===undefined?0x6a2818:o.flagC,side:THREE.DoubleSide,
      shininess:6,specular:0x3a2418}));
  fl.position.set(1.35,h-1.15,0); g.add(fl);
  return {g,fl,ph,update(t){ fl.rotation.y=0.42*Math.sin(t*1.5+ph)+0.16*Math.sin(t*2.6+ph*1.7); }};
}

/* —— 关城：关塞城垣剪影（城墙+双敌台+垛口，合批 1 mesh）——「关河梦断」的关 —— */
function makeGuancheng(o){
  o=o||{};
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(24,4.6,2.4); wall.translate(0,2.3,0); B.put(wall,0x0d0906);
  [-9,9].forEach(function(x){
    const tw=new THREE.BoxGeometry(4,7.4,3.2); tw.translate(x,3.7,0); B.put(tw,0x0c0805);
  });
  for(let i=-5;i<=5;i++){
    const mer=new THREE.BoxGeometry(0.8,0.8,0.7); mer.translate(i*2.1,5.0,0); B.put(mer,0x0b0704);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x1d160e,emissive:0x030201}),{c:0xb0906a,i:o.rim===undefined?0.10:o.rim,p:2.8})));
  return g;
}

/* 幽影材质收集：把 group 内去重的材质表列出（对影透明度动画用） */
function ghostMats(g){
  const out=[];
  g.traverse(function(o){ if(o.material&&out.indexOf(o.material)<0)out.push(o.material); });
  return out;
}

function bCoverSzq(){ // 封面 · 暮色大漠：烽燧剪影、台地天际线、天山雪影初现（一位霜鬓老人独立风中）
  const g=new THREE.Group();
  const ground=makeGround({r:120,c1:0x110b06,c2:0x1d1209});
  ground.mesh.position.set(0,-0.4,0); g.add(ground.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:19701,color:0x0b0806,atmo:0x3a2a18,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-16); g.add(ridge.g);
  /* 天山雪影：右后方天际一抹冷白（幻象的伏笔） */
  const snow=makeRange({r:250,h:24,layers:1,peaks:4,seed:19703,color:0x2e343c,atmo:0x6a7280,
    glow:0xdfe8f2,glowK:0.10,fogK:0.55,arc:Math.PI*0.5,a0:Math.PI*0.48,y:-12});
  g.add(snow.g);
  const mesas=makeTaidi({n:6,w:150,seed:19705,y:-2}); g.add(mesas);
  const feng=makeFengsui({h:9,w:3.2,rim:0.16}); feng.position.set(-20,0,-32); g.add(feng);
  const flame=makeFlame({h:1.5,w:0.7,core:0xffd9a0,outer:0xd9802a,planes:2,embers:16,light:1.1,lightD:34});
  flame.g.position.set(-20,10.1,-32); g.add(flame.g);
  /* 霜鬓老人：立于大漠风中（全诗的「身」） */
  const poet=makeFigure({pose:'独立',robe:0x2a251e,belt:0x5a5044,hat:'发髻',beard:true,
    hair:0xcfc9bd,scale:1.1,rim:0.5,rimC:0xb0906a});
  poet.position.set(-6,0,-12); poet.rotation.y=Math.PI-0.35; g.add(poet);
  const dust=makeFlow({n:170,box:[220,12,80],pos:[0,6,-26],color:0x9a7c50,size:16,speed:4.5,maxA:0.14});
  g.add(dust.points);
  const motes=makeGlow({n:40,box:[200,26,100],pos:[0,10,-40],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.14});
  g.add(motes.points);
  const fg=makeForeground({kind:'芦苇',w:44,n:12,d:6,color:0x0a0704,seed:19707,sway:1.0,tip:0x3a2c16});
  fg.g.position.set(0,-1.6,22); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x0b0805,seed:19709,rim:0.12,rimC:0xb0906a});
  rk.g.position.set(-15,-2.0,14); g.add(rk.g);
  addLights(g,{c:0xc09058,i:0.36,p:[-40,55,20]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ground.update(); ridge.update(t,0); snow.update(t,0);
    flame.update(t,k); dust.update(t); motes.update(t);
    fg.update(t,k); rk.update(t,k); poet.update(t,k);
  }};
}
function bMengshu(){ // 一 · 梦戍梁州 —— 梦里大漠金戈（全页最暖最亮）：年少戎装、军马、战旗、烽燧、关城
  const g=new THREE.Group();
  const ground=makeGround({r:130,c1:0x140d07,c2:0x261809});
  ground.mesh.position.set(0,-0.4,0); g.add(ground.mesh);
  const ridge=makeRange({r:340,h:22,layers:2,peaks:5,seed:19711,color:0x0c0806,atmo:0x40301c,fogK:0.58,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  const mesas=makeTaidi({n:5,w:150,seed:19713,y:-2}); g.add(mesas);
  /* 关城剪影 + 烽燧火光（「关河」在望，「觅封侯」的战场） */
  const guan=makeGuancheng({}); guan.position.set(-27,0,-44); guan.rotation.y=0.3; g.add(guan);
  const feng=makeFengsui({h:9.5,w:3.4,rim:0.2}); feng.position.set(25,0,-36); g.add(feng);
  const flame=makeFlame({h:1.8,w:0.85,core:0xffd9a0,outer:0xd9802a,planes:2,embers:22,spark:true,light:1.3,lightD:40});
  flame.g.position.set(25,10.6,-36); g.add(flame.g);
  /* 年少戎装（无须）+ 匹马：梦里正是少年 */
  const rider=makeFigure({pose:'按剑',robe:0x33261a,belt:0x8a5a2a,hat:'幞头',beard:false,
    scale:1.4,rim:0.72,rimC:0xb0906a});
  rider.position.set(3.6,0,-7.5); rider.rotation.y=Math.PI-0.5; g.add(rider);
  const horse=makeJunma({rim:0.3}); horse.position.set(8.2,0,-10); horse.rotation.y=-0.9; g.add(horse);
  /* 万兜鍪的军阵 + 战旗猎猎 */
  const army1=makeCrowd({n:38,rect:[-19,-22,36,12],color:0x1c140c,rimC:0xb0906a,rim:0.24,sMin:0.86,sMax:1.1,y:0,seed:19715});
  g.add(army1.mesh);
  const army2=makeCrowd({n:16,rect:[-14,-12,28,6],color:0x18110b,rimC:0xb0906a,rim:0.22,sMin:0.84,sMax:1.06,y:0,seed:19717});
  g.add(army2.mesh);
  const flags=[];
  [[-11,-20,7.2,0],[-4,-26,6.6,1.9],[9,-24,7.4,3.1],[16,-18,6.4,4.4]].forEach(function(fp){
    const f=makeDaqi({h:fp[2],ph:fp[3]});
    f.g.position.set(fp[0],0,fp[1]); g.add(f.g); flags.push(f);
  });
  const dust=makeFlow({n:230,box:[240,14,90],pos:[0,7,-46],color:0xa8824e,size:18,speed:5.5,maxA:0.16});
  g.add(dust.points);
  const motes=makeGlow({n:44,box:[210,24,110],pos:[0,9,-40],color:0xd8a868,size:6,speed:0.05,rise:0,maxA:0.18});
  g.add(motes.points);
  const fg=makeForeground({kind:'岩壁',n:2,r:3.6,w:14,d:6,color:0x0a0704,seed:19719,rim:0.12,rimC:0xb0906a});
  fg.g.position.set(18,-5.5,16); g.add(fg.g);
  const grass=makeForeground({kind:'芦苇',w:24,n:8,d:5,color:0x0b0805,seed:19721,sway:0.9,tip:0x42321a});
  grass.g.position.set(-13,-1.8,16); g.add(grass.g);
  addLights(g,{c:0xe0a860,i:0.52,p:[-55,55,-25]},{c:0x3a2c1c,i:0.64});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ground.update(); ridge.update(t,0);
    flame.update(t,k);
    for(let i=0;i<flags.length;i++)flags[i].update(t);
    dust.update(t); motes.update(t);
    fg.update(t,k); grass.update(t,k); rider.update(t,k);
  }};
}
function bChenan(){ // 二 · 尘暗貂裘 —— 檐下一隅（全页转冷）：衣架上的旧貂裘蒙尘，霜鬓老人独立，冷月入窗
  const g=new THREE.Group();
  const ground=makeGround({r:60,c1:0x0e0b08,c2:0x16110b});
  ground.mesh.position.set(0,-0.4,0); g.add(ground.mesh);
  const ridge=makeRange({r:280,h:14,layers:2,peaks:5,seed:19723,color:0x0a0806,atmo:0x2a2620,fogK:0.62,glowK:0.04,y:-14});
  ridge.g.position.set(0,0,-40); g.add(ridge.g);
  /* 檐廊：院墙 + 屋檐 + 柱一对（老屋一角） */
  const wall=new THREE.Mesh(new THREE.BoxGeometry(26,6.4,0.6),
    new THREE.MeshPhongMaterial({color:0x1c150d,shininess:3,specular:0x1d160e}));
  wall.position.set(0,2.8,-9); g.add(wall);
  const eave=new THREE.Mesh(new THREE.BoxGeometry(28.5,0.55,2.6),
    new THREE.MeshPhongMaterial({color:0x241a10,shininess:4,specular:0x2a1e12}));
  eave.position.set(0,6.3,-8.6); g.add(eave);
  const pilL=makePillar({h:6.4,top:false}); pilL.g.position.set(-9.5,0,-7.4); g.add(pilL.g);
  const pilR=makePillar({h:6.4,top:false}); pilR.g.position.set(9.5,0,-7.4); g.add(pilR.g);
  /* 冷月入窗：墙上一格冷光（全境唯一的亮，偏冷） */
  const win=new THREE.Mesh(new THREE.BoxGeometry(3.2,2.5,0.14),
    new THREE.MeshPhongMaterial({color:0x44403a,shininess:8,specular:0x54504a}));
  win.position.set(-5.5,3.5,-8.6); g.add(win);
  const moonin=makeGlow({n:26,box:[4.2,3,1.2],pos:[-5.5,3.5,-7.6],color:0x9aa0ac,size:5,
    speed:0.04,rise:0,add:true,maxA:0.40});
  g.add(moonin.points);
  /* 旧貂裘：衣架主体（尘暗的静物主角） */
  const diao=makeDiaoyu({h:3.6,rim:0.34}); diao.position.set(1.2,0,-3.4); diao.rotation.y=0.1;
  diao.scale.setScalar(1.15); g.add(diao);
  /* 霜鬓老人：鬓白如秋，独立裘侧（与境①的少年戎装同一人） */
  const poet=makeFigure({pose:'独立',robe:0x2a2620,belt:0x5a5044,hat:'发髻',beard:true,
    hair:0xd8d2c4,scale:1.4,rim:0.4,rimC:0x9a9484});
  poet.position.set(-3.6,0,-4.8); poet.rotation.y=1.25; g.add(poet);
  /* 尘光浮游：一束天光落在裘上，尘埃低低缓游 */
  const chen=makeGlow({n:46,box:[12,4.5,8],pos:[0.6,1.4,-4.0],color:0xa89468,size:4,speed:0.05,rise:0.12,add:true,maxA:0.26});
  g.add(chen.points);
  const dust=makeFlow({n:120,box:[190,10,70],pos:[0,6,-24],color:0x6a5c48,size:15,speed:3.5,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'树枝',w:26,n:7,d:5,color:0x0b0805,seed:19725,sway:0.55,tip:0x2c2418});
  fg.g.position.set(-15,2.5,6); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.8,w:10,d:5,color:0x0a0704,seed:19727,rim:0.10,rimC:0x8a8878});
  rk.g.position.set(13,-1.8,10); g.add(rk.g);
  addLights(g,{c:0x8a7a5e,i:0.26,p:[-40,50,15]},{c:0x2e2820,i:0.74});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ground.update(); ridge.update(t,0);
    moonin.update(t); chen.update(t); dust.update(t);
    fg.update(t,k); rk.update(t,k); poet.update(t,k);
  }};
}
function bTianshan(){ // 三（末境·可点击）· 天山沧洲 —— 标志性瞬间：天山雪岭幻象与沧洲茅屋现实同框对切
  const ctl={t:0,clicked:false,ext:0,lastSong:0};
  const g=new THREE.Group();
  const water=makeWater({size:800,seg:96,amp:0.42,freq:0.085,speed:0.55,flow:[0.15,0.5],
    deep:0x0e0c0a,shallow:0x2a2216,skyc:0x352a1c,spec:0.32,moonDir:[-0.5,0.18,-0.82],moonColor:0xc8a870,y:-1.5});
  g.add(water.mesh);
  /* 沧洲岸：右侧的现实（渔屋、滩地）；前左与远处让给水面 */
  const bank=makeGround({r:24,c1:0x0e0b08,c2:0x18120c});
  bank.mesh.position.set(10,-0.25,-6); g.add(bank.mesh);
  /* 天山雪岭（左后方，冷白辉光的幻象）与 沧洲岸线（右后方，暖灰低平）同框对切 */
  const snow=makeRange({r:150,h:46,layers:2,peaks:6,seed:19729,color:0x39404a,atmo:0x99a4b2,
    glow:0xf0f6fb,glowK:0.22,fogK:0.50,arc:Math.PI*0.52,a0:Math.PI*0.98,y:-12});
  g.add(snow.g);
  const shore=makeRange({r:230,h:12,layers:2,peaks:5,seed:19731,color:0x0c0906,atmo:0x332617,
    fogK:0.62,glowK:0.06,arc:Math.PI*0.5,a0:Math.PI*0.5,y:-12});
  g.add(shore.g);
  /* 沧洲茅屋 + 渔舟（现实的冷） */
  const cao=makeCaowu({w:7,d:5,h:2.6,rim:0.18}); cao.position.set(14,-0.2,-14); cao.rotation.y=-0.5; g.add(cao);
  const boat=makeYuzhou({scale:1.2,ph:1.3}); boat.g.position.set(23,-1.45,-30);
  boat.g.rotation.y=0.5; boat.y0=-1.45; g.add(boat.g);
  /* 旧貂裘：挂在屋前衣架（queue interact：点击貂裘） */
  const diao=makeDiaoyu({h:3.4,rim:0.34}); diao.position.set(6.5,-0.2,-3.5); diao.rotation.y=0.24;
  diao.scale.setScalar(1.2); g.add(diao);
  /* 点击后：尘光自裘上浮起（uMaxA 由 0 涌起，乘 fadeK） */
  const chen=makeGlow({n:70,box:[4.5,6,3.5],pos:[6.5,2.6,-3.5],color:0xc0a878,size:5,speed:0.06,rise:1.1,add:true,maxA:0.001});
  g.add(chen.points);
  /* 霜鬓老人：立于水滩，面朝天山（「身」在沧洲，「心」在山那侧） */
  const poet=makeFigure({pose:'独立',robe:0x2a2620,belt:0x5a5044,hat:'发髻',beard:true,
    hair:0xd8d2c4,scale:1.35,rim:0.46,rimC:0xb0906a});
  poet.position.set(-1.5,-0.2,-8); poet.rotation.y=-2.55; g.add(poet);
  /* 点击后显形：天山侧年少戎装的「对影」（幻象，隔水相望）——初值即最大透明度，乘 fadeK×vis */
  const ghost=new THREE.Group();
  const gr=makeFigure({pose:'按剑',robe:0x33261a,belt:0x8a5a2a,hat:'幞头',beard:false,
    scale:1.2,rim:0.6,rimC:0xc8d4e0});
  gr.position.set(-24,0.4,-40); gr.rotation.y=0.6; ghost.add(gr);
  const gh=makeJunma({rim:0.22}); gh.scale.setScalar(0.85); gh.position.set(-21,0.4,-42.5);
  gh.rotation.y=0.5; ghost.add(gh);
  const gmats=ghostMats(ghost);
  gmats.forEach(function(m){ m.transparent=true; m.opacity=0.85; });
  g.add(ghost);
  const mist=makeMist({n:8,spread:[230,16,110],pos:[-6,5,-44],scale:80,color:0x6a7280,op:0.10});
  g.add(mist.g);
  const flow=makeFlow({n:140,box:[220,10,90],pos:[-4,3,-32],color:0x6a5c48,size:15,speed:3.5,maxA:0.10});
  g.add(flow.points);
  const fgL=makeForeground({kind:'芦苇',w:38,n:11,d:6,color:0x0c0905,seed:19735,sway:1.0,tip:0x362a16});
  fgL.g.position.set(-10,-1.2,16); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:28,n:8,d:5,color:0x0f0a05,seed:19737,sway:0.85,tip:0x3a2c16});
  fgR.g.position.set(13,-1.4,18); g.add(fgR.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.4,w:9,d:5,color:0x0b0805,seed:19739,rim:0.10,rimC:0xb0906a});
  rk.g.position.set(-15,-1.2,8); g.add(rk.g);
  addLights(g,{c:0xb08858,i:0.32,p:[-45,55,-15]},{c:0x342a1e,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.ext=Math.min(1,ctl.ext+dt/3.2);
        if(t-ctl.lastSong>6.5){ ctl.lastSong=t; pluck(2,0,0.06); pluck(5,0.55,0.05); } // 山水余韵
      }
      const e=ctl.ext*(2-ctl.ext); // easeOut
      chen.mat.uniforms.uMaxA.value=0.5*k*Math.max(0.001,e);          // 尘光浮起（乘 fadeK）
      gmats.forEach(function(m){ m.opacity=m.userData.baseOpacity*k*(0.001+0.999*e); }); // 对影显形
      water.update(t); snow.update(t,0); shore.update(t,0);
      boat.update(t); mist.update(t,k); flow.update(t);
      fgL.update(t,k); fgR.update(t,k); rk.update(t,k); poet.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.0,0.10); pluck(3,0.4,0.09); pluck(4,0.8,0.09); pluck(5,1.2,0.08); // 心身两地的和声
        const fl=$('#flash'); fl.textContent='心在天山，身老沧洲'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
