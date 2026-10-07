/* ================= 卜算子·我住长江头 · 三境场景（青绿春晓·大江春晓变体：大江头尾、此水此恨、千里同心）
   本诗专属系统「一江贯两头」：长江自西（江头）向东（江尾），两岸青山夹一水，渡船在江心；
   相思瓣日日东漂（循环回流 = 「日日」的循环感），水面长周期呼吸同律；
   末境点击——镜头沿江千里贯通，江头江尾两点渐亮，一江灯自头至尾次第点亮连成一线
   （只愿君心似我心，定不负相思意） ================= */

/* —— 相思瓣：沿江东漂的花瓣（InstancedMesh，1 draw call；东流循环回流，永不休止） —— */
function makePetalsBJ(o){
  o=o||{};
  const n=o.n===undefined?24:o.n, R=seedRnd(o.seed===undefined?37:o.seed);
  const len=o.len===undefined?130:o.len, wide=o.wide===undefined?22:o.wide;
  const geo=new THREE.PlaneGeometry(0.30,0.18);
  const mat=new THREE.MeshPhongMaterial({color:o.color===undefined?0xe6d3bd:o.color,
    shininess:10,specular:0x8a7a5a,emissive:0x140c06,side:THREE.DoubleSide,transparent:true,opacity:0.92});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({x:(R()-0.5)*len, y:(o.y===undefined?0.5:o.y)+(R()-0.5)*2.0, z:(R()-0.5)*wide,
      s:0.5+R()*0.7, ph:R()*6.283, sp:0.55+R()*0.9});
  }
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,update:function(t,dt,spd){
    const v=(spd===undefined?1.6:spd);
    for(let i=0;i<n;i++){
      const it=items[i];
      it.x+=v*it.sp*dt;                       // 日日东流：漂到尽头便从头再来
      if(it.x>len*0.5)it.x-=len;
      dm.position.set(it.x,it.y+0.10*Math.sin(t*1.7+it.ph),it.z+Math.sin(t*0.9+it.ph)*0.6);
      dm.scale.setScalar(it.s);
      dm.rotation.set(Math.sin(t*1.1+it.ph)*0.7,t*0.6+it.ph,Math.sin(t*0.8+it.ph*2.0)*0.5);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* —— 白浪浮沫：急流上的白沫（InstancedMesh，1 draw call，流速可控 → 「日夜不休」的可见证据） —— */
function makeFoamBJ(o){
  o=o||{};
  const n=o.n===undefined?30:o.n, R=seedRnd(o.seed===undefined?53:o.seed);
  const len=o.len===undefined?90:o.len, wide=o.wide===undefined?26:o.wide;
  const geo=new THREE.SphereGeometry(0.26,7,5); geo.scale(1.2,0.28,1.0);
  const mat=new THREE.MeshPhongMaterial({color:o.color===undefined?0xc6dcc9:o.color,
    shininess:30,specular:0xc8e0cc,emissive:0x0e1a12,transparent:true,opacity:0.8});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({x:(R()-0.5)*len, z:(R()-0.5)*wide, s:0.35+R()*0.7, ph:R()*6.283, sp:0.6+R()*0.8});
  }
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.y=o.y===undefined?0.30:o.y;
  return {g,update:function(t,dt,spd){
    const v=(spd===undefined?4.0:spd);
    for(let i=0;i<n;i++){
      const it=items[i];
      it.x+=v*it.sp*dt;
      if(it.x>len*0.5)it.x-=len;
      dm.position.set(it.x,0.09*Math.sin(t*2.2+it.ph),it.z+Math.sin(t*1.2+it.ph)*0.5);
      dm.scale.setScalar(it.s);
      dm.rotation.y=it.ph+t*0.4;
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* —— 渡船：南北渡口的平底小船（船身+舷板+船头船尾+拱篷+橹+桅灯，合批 1 mesh + 灯辉 1 sprite） —— */
function makeSampanBJ(o){
  o=o||{};
  const wood=o.wood===undefined?0x1c1410:o.wood, canopyC=o.canopy===undefined?0x2a2118:o.canopy;
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(4.6,0.42,1.30); hull.translate(0,0.21,0); B.put(hull,wood);
  const bl=new THREE.BoxGeometry(4.7,0.16,0.10); bl.translate(0,0.52,0.62); B.put(bl,shadeColor(wood,1.25));
  const br=new THREE.BoxGeometry(4.7,0.16,0.10); br.translate(0,0.52,-0.62); B.put(br,shadeColor(wood,1.25));
  const bow=new THREE.CylinderGeometry(0.16,0.62,1.2,4); bow.rotateZ(-Math.PI/2); bow.translate(2.8,0.21,0);
  B.put(bow,shadeColor(wood,1.1));
  const stern=new THREE.CylinderGeometry(0.16,0.62,0.9,4); stern.rotateZ(-Math.PI/2); stern.translate(-2.7,0.21,0);
  B.put(stern,shadeColor(wood,1.1));
  const canopy=new THREE.CylinderGeometry(0.68,0.68,2.0,10,1,true,0,Math.PI);
  canopy.rotateY(-Math.PI/2); canopy.rotateX(-Math.PI/2); canopy.translate(0.3,0.66,0);
  B.put(canopy,canopyC);
  const scull=limbGeo([-1.5,0.5,0.35],[-2.7,0.85,1.25],0.045,0.02,5); B.put(scull,0x241a10);
  const post=new THREE.CylinderGeometry(0.035,0.035,0.95,5); post.translate(1.75,0.86,0); B.put(post,0x241a10);
  const lampBox=new THREE.BoxGeometry(0.17,0.21,0.17); lampBox.translate(1.75,1.42,0); B.put(lampBox,0xc8a05a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3226,emissive:0x080604}),{c:0xb8c8a0,i:0.20,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffca70,
    transparent:true,opacity:0.5,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(2.8,2.8,1); glow.position.set(1.75,1.5,0); glow.renderOrder=3; g.add(glow);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=o.seed===undefined?2.0:(o.seed%7)*0.9;
  let baseY=null;
  return {g,update(t,k){
    if(baseY===null)baseY=g.position.y;
    g.position.y=baseY+0.07*Math.sin(t*0.85+ph);
    g.rotation.z=0.03*Math.sin(t*0.7+ph*1.3);
    g.rotation.x=0.02*Math.sin(t*0.55+ph*0.7);
    glow.material.opacity=k*(0.40+0.10*(0.5+0.5*Math.sin(t*3.1+ph)));
  }};
}

/* —— 江头/江尾的信标：石灯柱 + 暖辉（fog:false Sprite；点击千里贯通后随旅程渐亮） —— */
function makeBeaconBJ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(0.9,0.5,0.9); base.translate(0,0.25,0); B.put(base,0x2e2c26);
  const post=new THREE.CylinderGeometry(0.11,0.14,1.5,7); post.translate(0,1.25,0); B.put(post,0x3a362e);
  const cap=new THREE.ConeGeometry(0.34,0.30,6); cap.translate(0,2.28,0); B.put(cap,0x443e32);
  const lampBox=new THREE.BoxGeometry(0.30,0.34,0.30); lampBox.translate(0,1.95,0); B.put(lampBox,0xc8a05a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    emissive:0x0a0806}),{c:0xd8c890,i:0.26,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0xffd9a0:o.color,
    transparent:true,opacity:0.62,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(5.4,5.4,1); glow.position.set(0,2.0,0); glow.renderOrder=3; g.add(glow);
  g.scale.setScalar(s);
  return {g,update(t,k,lit,pulse){
    glow.material.opacity=k*(0.10+0.42*lit+0.08*(pulse||0)+0.015*Math.sin(t*2.2));
  }};
}

/* 末境镜头旅程的起讫（起=入境高点，讫=沿江东行抵达江尾）；STAGES[3].cam 由它派生 */
const BJ_CAM3={f:[-44,24,50],t:[-28,21,42],lf:[10,0,-6],lt:[16,0,-8]};

function bCover(){ // 卷首 · 大江春晓 —— 千里大江晨光初开，两岸青山夹一水，渡船在江心
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0c1710,c2:0x16281a,y:-1.8}); g.add(grd.mesh);
  const north=makeRange({r:250,h:38,layers:3,peaks:6,seed:57,color:0x11241a,atmo:0x2c4434,fogK:0.62,glowK:0.08,glow:0xbcd8a0,y:-10});
  north.g.position.set(0,0,-88); g.add(north.g);
  /* 江头（西）与江尾（东）两头的远山：河流在两端没入山影 —— 相思的地理 */
  const west=makeRange({r:92,h:20,layers:2,peaks:4,seed:59,color:0x102018,atmo:0x2c4434,fogK:0.60,glowK:0.06,glow:0xa8cc90,y:-8});
  west.g.position.set(-122,-2,-34); g.add(west.g);
  const east=makeRange({r:92,h:18,layers:2,peaks:4,seed:61,color:0x102018,atmo:0x2c4434,fogK:0.60,glowK:0.06,glow:0xa8cc90,y:-8});
  east.g.position.set(122,-2,-42); g.add(east.g);
  /* 大江：东西横贯（西＝江头，东＝江尾），水面东流 */
  const water=makeWater({size:16,seg:36,amp:0.12,freq:0.15,speed:0.55,flow:[0.8,0.06],spec:0.95,
    deep:0x0a1a14,shallow:0x226048,skyc:0x2f6450,moonDir:[-25,80,-140],y:-1.55});
  water.mesh.scale.set(15,1,2.0); g.add(water.mesh);
  /* 两岸岸线（北深南浅两层） */
  const bankB=new GeoBag();
  const bn=new THREE.BoxGeometry(210,1.5,7); bn.translate(0,-1.05,-19.5); bankB.put(bn,shadeColor(0x18271c,1.0));
  const bs=new THREE.BoxGeometry(210,1.5,7); bs.translate(0,-1.05,19.5); bankB.put(bs,shadeColor(0x1a2a1e,1.0));
  g.add(bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x8fc4a8,i:0.13,p:2.4})));
  /* 渡船在江心 */
  const boat=makeSampanBJ({scale:1.25,seed:7});
  boat.g.position.set(2,-1.55,-2); boat.g.rotation.y=0.5; g.add(boat.g);
  /* 江头、江尾两处人影（两岸相望的种子，末境里长成两头灯火） */
  const man1=makeFigure({pose:'独立',robe:0x24312a,belt:0x8f6a33,hat:'发髻',scale:0.62,rim:0.4,rimC:0xb8d0a8,noProp:true});
  man1.position.set(-46,-0.3,17.8); man1.rotation.y=1.42; g.add(man1);
  const man2=makeFigure({pose:'独立',robe:0x2a3038,belt:0x7a5a30,hat:'发髻',scale:0.62,rim:0.4,rimC:0xb8d0a8,noProp:true});
  man2.position.set(41,-0.3,-18.4); man2.rotation.y=-1.38; g.add(man2);
  /* 晨曦：东天（江尾所向）一抹暖意 */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.22,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(170,60,1); dawn.position.set(115,28,-130); dawn.renderOrder=-7; g.add(dawn);
  const petals=makePetalsBJ({n:22,len:150,wide:20,seed:37});
  petals.g.position.set(0,-1.2,-2); g.add(petals.g);
  const motes=makeGlow({n:40,box:[200,26,100],pos:[0,6,-24],color:0xcfe0a8,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,26,130],pos:[0,7,-46],scale:78,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:26,n:12,d:5,color:0x071009,seed:19,sway:1.0,tip:0x2c4028});
  reed.g.position.set(8,-1.8,24); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.8,w:10,d:6,color:0x060c08,seed:21,rim:0.12,rimC:0x8fc4a8});
  rk.g.position.set(-20,-2.0,26); g.add(rk.g);
  addLights(g,{c:0xe8d8a8,i:0.46,p:[-50,80,30]},{c:0x22301f,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    north.update(t,0); west.update(t,0); east.update(t,0); water.update(t);
    mist.update(t,k); motes.update(t); reed.update(t,k); rk.update(t,k);
    man1.update(t,k); man2.update(t,k); boat.update(t,k);
    petals.update(t,dt,1.5);
    dawn.material.opacity=k*(0.16+0.05*Math.sin(t*0.4));
  }};
}
function bGongyin(){ // 一 · 共饮长江 —— 我住长江头，君住长江尾；两岸相望，共饮一江水
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0a130d,c2:0x152417,y:-0.6}); g.add(grd.mesh);
  const north=makeRange({r:230,h:34,layers:3,peaks:5,seed:71,color:0x09150e,atmo:0x29412e,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-6});
  north.g.position.set(0,0,-85); g.add(north.g);
  const west=makeRange({r:70,h:13,layers:2,peaks:3,seed:73,color:0x091409,atmo:0x29412e,fogK:0.60,glowK:0.04,glow:0x9ab888,y:-5});
  west.g.position.set(-98,-3,-26); g.add(west.g);
  const east=makeRange({r:70,h:12,layers:2,peaks:3,seed:75,color:0x091409,atmo:0x29412e,fogK:0.60,glowK:0.04,glow:0x9ab888,y:-5});
  east.g.position.set(98,-3,-34); g.add(east.g);
  /* 一江春水：东西向横贯（西＝江头，东＝江尾） */
  const water=makeWater({size:16,seg:32,amp:0.11,freq:0.17,speed:0.55,flow:[0.85,0.06],spec:0.95,
    deep:0x0a1a14,shallow:0x226048,skyc:0x2f6450,moonDir:[-30,80,-140],y:0.02});
  water.mesh.scale.set(13,1,1.7); g.add(water.mesh);
  const bankB=new GeoBag();
  const bn=new THREE.BoxGeometry(190,1.4,6.8); bn.translate(0,0.2,-17.0); bankB.put(bn,shadeColor(0x16241a,1.0));
  const bs=new THREE.BoxGeometry(190,1.4,6.8); bs.translate(0,0.2,17.0); bankB.put(bs,shadeColor(0x18271c,1.0));
  const bankM=bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x8fc4a8,i:0.13,p:2.4}));
  g.add(bankM);
  /* 江头人：南岸临流而立，望下游；江尾人：北岸远影，望上游（两岸相望） */
  const man1=makeFigure({pose:'独立',robe:0x24312a,belt:0x8f6a33,hat:'发髻',scale:1.22,rim:0.5,rimC:0xb8d0a8,noProp:true});
  man1.position.set(-11,0.9,13.6); man1.rotation.y=1.42; g.add(man1);
  const man2=makeFigure({pose:'独立',robe:0x2a3038,belt:0x7a5a30,hat:'发髻',scale:0.9,rim:0.44,rimC:0xb8d0a8,noProp:true});
  man2.position.set(17,0.9,-14.6); man2.rotation.y=-1.38; g.add(man2);
  /* 渡船：江心一叶（两岸唯凭此一水相通） */
  const boat=makeSampanBJ({scale:1.0,seed:9});
  boat.g.position.set(2,0.02,-2); boat.g.rotation.y=0.85; g.add(boat.g);
  const petals=makePetalsBJ({n:22,len:130,wide:20,y:0.45,seed:41});
  g.add(petals.g);
  const crowd=makeCrowd({n:3,rect:[8,-26,18,6],seed:77,color:0x121c13,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:30,box:[150,20,80],pos:[0,6,-16],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[210,20,110],pos:[0,6,-40],scale:66,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:45,sway:1.1,tip:0x2c4028});
  reed.g.position.set(14,-0.8,12); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:6,color:0x060b07,seed:47,rim:0.12,rimC:0x8fc4a8});
  rk.g.position.set(-18,-1.2,14); g.add(rk.g);
  addLights(g,{c:0xc2bd90,i:0.42,p:[-40,75,25]},{c:0x1c2a1e,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      north.update(t,0); west.update(t,0); east.update(t,0); water.update(t);
      mist.update(t,k); motes.update(t); reed.update(t,k); rk.update(t,k);
      man1.update(t,k); man2.update(t,k); boat.update(t,k); crowd.update(t);
      petals.update(t,dt,1.8);
      water.mesh.material.uniforms.uAmp.value=0.11*(1+0.14*Math.sin(t*0.21));  // 「日日」的水面呼吸
    }};
}
function bCishui(){ // 二 · 此水此恨 —— 江水日夜不休，此恨何时能已；中流石矶分水，渡船被水流裹挟东去
  const g=new THREE.Group();
  const grd=makeGround({r:200,c1:0x0a120c,c2:0x132216,y:-0.6}); g.add(grd.mesh);
  const north=makeRange({r:215,h:26,layers:2,peaks:5,seed:86,color:0x0f2014,atmo:0x28402c,fogK:0.60,glowK:0.08,glow:0x9ab888,y:-6});
  north.g.position.set(0,0,-78); g.add(north.g);
  const west=makeRange({r:64,h:15,layers:2,peaks:3,seed:85,color:0x0e1d13,atmo:0x28402c,fogK:0.58,glowK:0.05,glow:0x9ab888,y:-5});
  west.g.position.set(-72,-2,-16); g.add(west.g);
  const east=makeRange({r:64,h:13,layers:2,peaks:3,seed:87,color:0x0e1d13,atmo:0x28402c,fogK:0.58,glowK:0.05,glow:0x9ab888,y:-5});
  east.g.position.set(76,-2,-24); g.add(east.g);
  /* 急流：日夜不休地东去（uAmp 长周期呼吸 = 「日日」的循环感） */
  const water=makeWater({size:16,seg:40,amp:0.16,freq:0.22,speed:0.9,flow:[1.6,0.10],spec:0.9,
    deep:0x0a1a14,shallow:0x25604a,skyc:0x2f6450,moonDir:[-10,42,-120],y:0.02});
  water.mesh.scale.set(12,1,2.2); g.add(water.mesh);
  const bankB=new GeoBag();
  const bn=new THREE.BoxGeometry(170,1.4,6); bn.translate(0,0.2,-20.9); bankB.put(bn,shadeColor(0x16241a,1.0));
  const bs=new THREE.BoxGeometry(170,1.4,6); bs.translate(0,0.2,20.9); bankB.put(bs,shadeColor(0x18271c,1.0));
  g.add(bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x8fc4a8,i:0.13,p:2.4})));
  /* 中流石矶 + 南岸矶头（江头人立矶望下游；矶石收小，不挡江面） */
  const rockB=new GeoBag();
  const r1=rockGeo(1.9,1,seedRnd(101)); r1.translate(-4.5,0.25,2.0); rockB.put(r1,shadeColor(0x232e22,1.0));
  const r2=rockGeo(1.4,1,seedRnd(103)); r2.translate(-1.0,0.1,5.2); rockB.put(r2,shadeColor(0x1e281d,1.0));
  const r3=rockGeo(2.1,1,seedRnd(107)); r3.translate(-6.5,0.25,12.5); rockB.put(r3,shadeColor(0x232e22,1.0));
  const rockM=rockB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    emissive:0x060a06}),{c:0x9cc0a0,i:0.22,p:2.4}));
  rockM.frustumCulled=false; g.add(rockM);
  /* 白浪浮沫：日夜东去的白沫（流速 4.2，一刻不停） */
  const foam=makeFoamBJ({n:30,len:90,wide:28,seed:53});
  foam.g.position.set(4,0.30,0); g.add(foam.g);
  /* 江头人：中流矶头独立望下游；江尾人：北岸远影 */
  const man1=makeFigure({pose:'独立',robe:0x24312a,belt:0x8f6a33,hat:'发髻',scale:1.25,rim:0.5,rimC:0xb8d0a8,noProp:true});
  man1.position.set(-4.5,1.55,2.0); man1.rotation.y=1.35; g.add(man1);
  const man2=makeFigure({pose:'独立',robe:0x2a3038,belt:0x7a5a30,hat:'发髻',scale:0.8,rim:0.42,rimC:0xb8d0a8,noProp:true});
  man2.position.set(23,0.9,-17.4); man2.rotation.y=-1.42; g.add(man2);
  /* 渡船：被水流裹挟东去（慢漂 + 循环回绕 = 「几时休」的移情） */
  const boat=makeSampanBJ({scale:0.9,seed:11});
  boat.g.position.set(10,0.02,-6); boat.g.rotation.y=-0.3; g.add(boat.g);
  const petals=makePetalsBJ({n:14,len:90,wide:24,y:0.4,seed:43});
  g.add(petals.g);
  const motes=makeGlow({n:26,box:[150,16,70],pos:[0,5,-14],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[190,12,90],pos:[0,2.5,-26],scale:60,color:0x1e3424,op:0.13});
  g.add(mist.g);
  const cliff=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x060b07,seed:91,rim:0.14,rimC:0x8fc4a8});
  cliff.g.position.set(-18,-1.5,12); g.add(cliff.g);
  const reed=makeForeground({kind:'芦苇',w:16,n:9,d:5,color:0x071009,seed:95,sway:1.3,tip:0x2c4028});
  reed.g.position.set(12,-1.2,12.5); g.add(reed.g);
  addLights(g,{c:0xbccdb4,i:0.38,p:[30,60,30]},{c:0x1a261c,i:0.60});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      north.update(t,0); west.update(t,0); east.update(t,0); water.update(t);
      mist.update(t,k); motes.update(t); cliff.update(t,k); reed.update(t,k);
      man1.update(t,k); man2.update(t,k);
      water.mesh.material.uniforms.uAmp.value=0.16*(1+0.15*Math.sin(t*0.21));  // 「日日」的水面呼吸
      foam.update(t,dt,4.2);
      petals.update(t,dt,3.0);
      boat.update(t,k);
      boat.g.position.x+=dt*1.1; if(boat.g.position.x>32)boat.g.position.x=-26;
    },onEnter(){   // 两问三音：低问渐沉
      pluck(2,0.15,0.12); pluck(1,0.7,0.10); pluck(0,1.3,0.09);
    }};
}
function bXiangsi(){ // 三（末境·可点击）· 不负相思 —— 点击：镜头沿江千里贯通，江头江尾两点渐亮，一江灯连成一线
  const g=new THREE.Group();
  const ctl={t:0,j:0,clicked:false,pulse:0,flashed:false,JDUR:9.5};
  /* 旅程讫点：自入境高点沿江东行，抵近江尾；每次入境先把本境镜头复位到 BJ_CAM3 */
  const J1={f:[44,8.5,21],t:[52,8,19],lf:[58,3,-10],lt:[58,2.6,-12]};
  (function(){ const D=STAGES[3].cam;
    D.f=BJ_CAM3.f.slice(); D.t=BJ_CAM3.t.slice(); D.lf=BJ_CAM3.lf.slice(); D.lt=BJ_CAM3.lt.slice(); })();
  function sstep(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); }
  const grd=makeGround({r:270,c1:0x081009,c2:0x152417,y:-1.2}); g.add(grd.mesh);
  const north=makeRange({r:265,h:40,layers:3,peaks:6,seed:91,color:0x102218,atmo:0x2c4434,fogK:0.62,glowK:0.08,glow:0xaad0a0,y:-10});
  north.g.position.set(0,0,-100); g.add(north.g);
  const west=makeRange({r:100,h:22,layers:2,peaks:4,seed:93,color:0x0f1e14,atmo:0x2c4434,fogK:0.60,glowK:0.06,glow:0xa8cc90,y:-9});
  west.g.position.set(-130,-3,-40); g.add(west.g);
  const east=makeRange({r:100,h:20,layers:2,peaks:4,seed:95,color:0x0f1e14,atmo:0x2c4434,fogK:0.60,glowK:0.06,glow:0xa8cc90,y:-9});
  east.g.position.set(130,-3,-46); g.add(east.g);
  /* 千里大江：东西贯通全境（西＝江头，东＝江尾） */
  const water=makeWater({size:16,seg:40,amp:0.13,freq:0.15,speed:0.6,flow:[0.9,0.05],spec:0.9,
    deep:0x0a1a14,shallow:0x26604a,skyc:0x2f6450,moonDir:[-10,45,-130],y:-0.55});
  water.mesh.scale.set(17,1,2.3); g.add(water.mesh);
  const bankB=new GeoBag();
  const bn=new THREE.BoxGeometry(290,1.4,6.5); bn.translate(0,-0.45,-21.6); bankB.put(bn,shadeColor(0x18271c,1.0));
  const bs=new THREE.BoxGeometry(290,1.4,6.5); bs.translate(0,-0.45,21.6); bankB.put(bs,shadeColor(0x1a2a1e,1.0));
  g.add(bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x8fc4a8,i:0.13,p:2.4})));
  /* 江头人（西）与江尾人（东）：两岸相望，一眼千里 */
  const man1=makeFigure({pose:'独立',robe:0x24312a,belt:0x8f6a33,hat:'发髻',scale:1.05,rim:0.5,rimC:0xc8dcb0,noProp:true});
  man1.position.set(-47,0.25,19.0); man1.rotation.y=1.5; g.add(man1);
  const man2=makeFigure({pose:'独立',robe:0x2a3038,belt:0x7a5a30,hat:'发髻',scale:1.05,rim:0.5,rimC:0xc8dcb0,noProp:true});
  man2.position.set(60,0.25,-19.5); man2.rotation.y=-1.5; g.add(man2);
  /* 江头、江尾两盏信标（点击后随千里贯通先后点亮） */
  const headBcn=makeBeaconBJ({scale:1.1});
  headBcn.g.position.set(-44.5,0.25,17.2); g.add(headBcn.g);
  const tailBcn=makeBeaconBJ({scale:1.1});
  tailBcn.g.position.set(57.5,0.25,-17.6); g.add(tailBcn.g);
  /* 一江灯：沿江九盏（点击后自江头至江尾次第点亮，连成一线） */
  const lamps=[];
  for(let i=0;i<9;i++){
    const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd9a0,
      transparent:true,opacity:0.44,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    sp.scale.set(4.6,4.6,1); sp.position.set(-54+i*13.5,0.7,0.5); sp.renderOrder=3;
    g.add(sp); lamps.push(sp);
  }
  /* 一江暖流：顺流东去的光点（点击后随旅程渐亮） */
  const flow=makeFlow({n:160,box:[10,3.5,150],pos:[0,1.0,0],color:0xd8b880,size:9,speed:6,maxA:0.30});
  flow.points.rotation.y=Math.PI/2;   // 局部 +z → 世界 +x：顺流东去
  flow.mat.uniforms.uMaxA.value=0;
  g.add(flow.points);
  /* 渡船仍在江心 */
  const boat=makeSampanBJ({scale:0.95,seed:13});
  boat.g.position.set(8,-0.55,-4); boat.g.rotation.y=0.3; g.add(boat.g);
  const petals=makePetalsBJ({n:20,len:170,wide:22,y:0.1,seed:49});
  g.add(petals.g);
  const crowd=makeCrowd({n:3,rect:[34,-27,18,6],seed:81,color:0x121c13,rimC:0x8fae78,rim:0.18});
  g.add(crowd.mesh);
  const motes=makeGlow({n:30,box:[180,22,90],pos:[0,6,-24],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[250,20,130],pos:[0,5,-50],scale:80,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.8,w:10,d:6,color:0x060b07,seed:97,rim:0.12,rimC:0x8fc4a8});
  rk.g.position.set(-26,-2.4,28); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:10,d:5,color:0x071009,seed:99,sway:1.1,tip:0x2c4028});
  reed.g.position.set(20,-2.2,30); g.add(reed.g);
  addLights(g,{c:0xd8c8a0,i:0.46,p:[-60,80,40]},{c:0x1e2c20,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.j=Math.min(1,ctl.j+dt/ctl.JDUR);
      const je=sstep(ctl.j);                       // 千里贯通的缓起缓收
      if(ctl.clicked){
        const D=STAGES[3].cam;                     // 旅程镜头：沿江东行，直抵江尾
        for(let i=0;i<3;i++){
          D.f[i]=BJ_CAM3.f[i]+(J1.f[i]-BJ_CAM3.f[i])*je;
          D.t[i]=BJ_CAM3.t[i]+(J1.t[i]-BJ_CAM3.t[i])*je;
          D.lf[i]=BJ_CAM3.lf[i]+(J1.lf[i]-BJ_CAM3.lf[i])*je;
          D.lt[i]=BJ_CAM3.lt[i]+(J1.lt[i]-BJ_CAM3.lt[i])*je;
        }
      }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const jh=Math.min(1,ctl.j*2.4), jt=Math.max(0,(ctl.j-0.5)/0.5);   // 江头先亮，江尾后亮
      headBcn.update(t,k,jh,ctl.pulse); tailBcn.update(t,k,jt,ctl.pulse);
      for(let i=0;i<9;i++){
        const th=Math.max(0,Math.min(1,(ctl.j-(0.06+0.78*i/8))/0.16));
        lamps[i].material.opacity=k*(0.07+th*(0.26+0.08*ctl.pulse)+0.02*Math.sin(t*2.4+i*1.7));
      }
      flow.mat.uniforms.uMaxA.value=0.26*je+0.08*ctl.pulse*je;
      if(ctl.clicked&&!ctl.flashed&&ctl.j>0.3){
        ctl.flashed=true;
        const fl=$('#flash'); fl.textContent='只愿君心似我心'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
        pluck(4,0,0.15); pluck(5,0.5,0.12); pluck(2,1.1,0.10);
      }
      north.update(t,0); west.update(t,0); east.update(t,0); water.update(t);
      mist.update(t,k); motes.update(t); rk.update(t,k); reed.update(t,k);
      man1.update(t,k); man2.update(t,k); boat.update(t,k); crowd.update(t);
      petals.update(t,dt,2.2);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.14); pluck(2,0.35,0.12); pluck(4,0.85,0.11);
      }
      ctl.pulse=1;                            // 可反复点：一江灯火再涨一拍
    },clicked:false};
  return api;
}
