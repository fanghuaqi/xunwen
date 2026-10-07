/* ================= 如梦令·常记溪亭日暮 · 三境场景（青绿春晓·荷塘日暮变体：溪亭日暮卷首、藕花深处、鸥鹭惊起）
   本诗专属系统「一滩鸥鹭」：荷荡夹一水道，一叶小舟（舟中少女、船尾点灯）误入最密处；
   末境点击「争渡」——急桨连声、桨花迸溅，鸥鹭自沙洲冲天而起、盘旋满空（全页动效最高点） ================= */

/* —— 荷荡 makeLotus：带缺刻圆盘荷叶（两档绿）+ 茎/花苞/外翻花瓣合批的荷花，各 1 个 InstancedMesh —— */
function makeLotus(o){
  o=o||{};
  const nL=o.leaves===undefined?36:o.leaves, nF=o.flowers===undefined?10:o.flowers;
  const w=o.w===undefined?56:o.w, d=o.d===undefined?34:o.d, cx=o.cx||0, cz=o.cz||0;
  const R=seedRnd(o.seed===undefined?11:o.seed);
  const y=o.y===undefined?0.16:o.y;
  const mkLeaf=function(col){
    const lg=new THREE.CircleGeometry(1,12,0,Math.PI*1.74); lg.rotateX(-Math.PI/2);
    const im=new THREE.InstancedMesh(lg,new THREE.MeshPhongMaterial({color:col,shininess:16,
      specular:0x36503a,side:THREE.DoubleSide}),Math.ceil(nL/2));
    return im;
  };
  const leafA=mkLeaf(o.leafA===undefined?0x1a3a22:o.leafA), leafB=mkLeaf(o.leafB===undefined?0x245030:o.leafB);
  const FB=new GeoBag();
  FB.put(limbGeo([0,-0.85,0],[0,0.05,0],0.035,0.05,5),0x24421e);
  const bud=new THREE.SphereGeometry(0.15,8,6); bud.scale(1,1.6,1); bud.translate(0,0.28,0); FB.put(bud,0xa85864);
  for(let i=0;i<6;i++){
    const a=i/6*Math.PI*2;
    const pt=new THREE.PlaneGeometry(0.20,0.42);
    pt.rotateX(-0.85); pt.rotateY(a); pt.translate(Math.cos(a)*0.13,0.30,Math.sin(a)*0.13);
    FB.put(pt,i%2?0xe8bcc0:0xf2d8d2);
  }
  const flowers=new THREE.InstancedMesh(mergeGeos(FB.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:20,
      specular:0x5a3a3a,side:THREE.DoubleSide,emissive:0x140a0a}),nF);
  const items=[];
  for(let i=0;i<nL;i++){
    items.push({mesh:i%2?leafB:leafA, idx:Math.floor(i/2),
      x:cx+(R()-0.5)*w, z:cz+(R()-0.5)*d, s:0.8+R()*1.1, ph:R()*6.283, tilt:(R()-0.5)*0.16});
  }
  const fitems=[];
  for(let i=0;i<nF;i++){
    fitems.push({x:cx+(R()-0.5)*w, z:cz+(R()-0.5)*d, s:0.7+R()*0.55, ph:R()*6.283, ry:R()*6.283});
  }
  leafA.frustumCulled=leafB.frustumCulled=flowers.frustumCulled=false;
  const g=new THREE.Group(); g.add(leafA); g.add(leafB); g.add(flowers);
  const dm=new THREE.Object3D();
  const upd=function(t){
    for(let i=0;i<items.length;i++){
      const it=items[i];
      dm.position.set(it.x,y+0.05*Math.sin(t*0.8+it.ph),it.z);
      dm.rotation.set(it.tilt*Math.sin(t*0.5+it.ph),it.ph,it.tilt*Math.cos(t*0.4+it.ph));
      dm.scale.setScalar(it.s); dm.updateMatrix();
      it.mesh.setMatrixAt(it.idx,dm.matrix);
    }
    for(let i=0;i<fitems.length;i++){
      const it=fitems[i];
      dm.position.set(it.x,y+0.55*it.s+0.05*Math.sin(t*0.9+it.ph),it.z);
      dm.rotation.set(0.06*Math.sin(t*0.7+it.ph),it.ry+0.05*Math.sin(t*0.5+it.ph),0.05*Math.cos(t*0.6+it.ph));
      dm.scale.setScalar(it.s); dm.updateMatrix();
      flowers.setMatrixAt(i,dm.matrix);
    }
    leafA.instanceMatrix.needsUpdate=true; leafB.instanceMatrix.needsUpdate=true; flowers.instanceMatrix.needsUpdate=true;
  };
  upd(0);
  return {g,update:function(t){upd(t);}};
}

/* —— 小舟 makeSkiff：合批船体（船壳+船沿+坐板+尾板+船头）+ 可划单桨 + 舟中少女 + 船尾灯
   update(t,k,row)：row=0 缓桨漂浮，row=1 急桨（争渡），船身随桨摇摆 —— */
function makeSkiff(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.SphereGeometry(1,12,8); hull.scale(0.98,0.46,3.5); hull.translate(0,0.24,0); B.put(hull,0x241a10);
  const rim=new THREE.TorusGeometry(1,0.05,6,26); rim.rotateX(Math.PI/2); rim.scale(0.96,1,3.46); rim.translate(0,0.70,0); B.put(rim,0x3a2c1a);
  const bench=new THREE.BoxGeometry(1.6,0.09,0.5); bench.translate(0,0.62,0.35); B.put(bench,shadeColor(0x3a2c1a,1.25));
  const deck=new THREE.BoxGeometry(1.3,0.10,1.1); deck.translate(0,0.58,2.55); B.put(deck,shadeColor(0x2c2012,1.1));
  const bowtip=new THREE.ConeGeometry(0.16,0.8,6); bowtip.rotateX(-Math.PI/2); bowtip.translate(0,0.45,-3.7); B.put(bowtip,0x241a10);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2c2418,emissive:0x0a0704}),{c:0x8fc9b8,i:0.20,p:2.4})));
  /* 单桨：绕桨栓拨水（急桨时大幅快摆） */
  const oar=new THREE.Group(); oar.position.set(0.78,0.72,1.05);
  const OB=new GeoBag();
  OB.put(limbGeo([0,0,0],[0.55,-1.30,0.85],0.05,0.032,6),0x4a3820);
  const blade=new THREE.BoxGeometry(0.06,0.46,0.30); blade.rotateX(0.5); blade.translate(0.62,-1.55,0.98); OB.put(blade,shadeColor(0x4a3820,0.85));
  oar.add(OB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,emissive:0x0a0704})));
  g.add(oar);
  /* 舟中少女（坐姿，青绿腰带一点本诗accent） */
  const girl=makeFigure({pose:'坐饮',noProp:true,robe:0xb8826a,belt:0x8fc9b8,hair:0x181310,
    collar:0xe6ddc4,scale:0.5,rim:0.5,rimC:0xc9b8a0});
  girl.position.set(-0.12,0.22,0.35); girl.rotation.y=Math.PI-0.3;
  g.add(girl);
  /* 船尾灯杆+小灯（日暮点起的一点暖） */
  const pole=new THREE.Mesh(limbGeo([0,0.6,2.55],[0,2.0,2.55],0.035,0.045,5),
    new THREE.MeshPhongMaterial({color:0x3a2c1a,shininess:6,emissive:0x0a0704}));
  g.add(pole);
  const lant=makeLantern(0.26,{glow:0.42,flick:0.9});
  lant.position.set(0,1.85,2.55); g.add(lant);
  g.scale.setScalar(s);
  return {g,oar,girl,update:function(t,k,row){
    girl.update(t,k); lant.update(t,k);
    oar.rotation.y=(row>0?0.55:0.14)*Math.sin(t*(row>0?11:1.1));
    oar.rotation.z=0.16+0.10*Math.sin(t*(row>0?11:1.1)+1.2);
    g.rotation.z=(row>0?0.05:0.028)*Math.sin(t*(row>0?5.5:0.8));
    g.rotation.x=(row>0?0.035:0.02)*Math.sin(t*0.66+1.2);
  }};
}

/* —— 鸥鹭群 makeEgretFlock：沙洲栖鹭（身+左右翼 3 个 InstancedMesh），
   launch(t) 后群鸟错峰冲天、盘旋满空：爬升期急频扑翼，入空后缓频盘旋 —— */
function makeEgretFlock(o){
  o=o||{};
  const n=o.n===undefined?26:o.n, R=seedRnd(o.seed===undefined?37:o.seed);
  const bar=o.bar||[-11,0.1,-16], spread=o.spread||[6,2.2];
  const BB=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,9,7); body.scale(0.85,0.8,2.0); body.translate(0,0.55,0); BB.put(body,0xe8ece2);
  BB.put(limbGeo([0,0.72,0.42],[0,1.05,0.72],0.05,0.038,5),0xe8ece2);
  const head=new THREE.SphereGeometry(0.11,8,6); head.translate(0,1.10,0.78); BB.put(head,0xf2f4ea);
  const beak=new THREE.ConeGeometry(0.035,0.26,5); beak.rotateX(Math.PI/2); beak.translate(0,1.08,1.02); BB.put(beak,0xd8b45a);
  const tail=new THREE.ConeGeometry(0.10,0.55,5); tail.rotateX(-Math.PI/2.5); tail.translate(0,0.42,-0.72); BB.put(tail,0xd8dcd0);
  const bodies=new THREE.InstancedMesh(mergeGeos(BB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,
      specular:0x3a4640,emissive:0x0e1410}),{c:0xcfe0d8,i:0.42,p:2.5}),n);
  const wingGeo=function(side){
    const wg=new THREE.PlaneGeometry(1.2,0.5,4,1);
    const p=wg.attributes.position;
    for(let i=0;i<p.count;i++){
      const u=(p.getX(i)*side+0.6)/1.2;          // 0 翼根 → 1 翼尖
      p.setY(i,p.getY(i)*(1.0-0.6*u));
      p.setX(i,p.getX(i)+0.10*u*side);
    }
    wg.rotateX(-Math.PI/2);
    wg.translate(0.66,0.12,0);
    if(side<0)wg.scale(-1,1,1);
    wg.computeVertexNormals();
    return wg;
  };
  const wingMat=new THREE.MeshPhongMaterial({color:0xe4e8dc,shininess:20,specular:0x3a4640,
    emissive:0x0e1410,side:THREE.DoubleSide});
  const wingL=new THREE.InstancedMesh(wingGeo(-1),wingMat,n);
  const wingR=new THREE.InstancedMesh(wingGeo(1),wingMat,n);
  const items=[];
  for(let i=0;i<n;i++){
    items.push({x:bar[0]+(R()-0.5)*spread[0]*2, z:bar[2]+(R()-0.5)*spread[1]*2, y:bar[1]+0.35+R()*0.5,
      s:0.75+R()*0.5, ph:R()*6.283, ry:R()*6.283,
      a0:R()*6.283, r0:3+R()*9, turn:(2.0+R()*1.1)*6.283, h:13+R()*15, delay:R()*1.5, T:2.8+R()*2.2});
  }
  bodies.frustumCulled=wingL.frustumCulled=wingR.frustumCulled=false;
  const g=new THREE.Group(); g.add(bodies); g.add(wingL); g.add(wingR);
  const dm=new THREE.Object3D(), wm=new THREE.Object3D();
  const M=new THREE.Matrix4(), MW=new THREE.Matrix4();
  let launched=false, t0=0;
  const upd=function(t){
    for(let i=0;i<n;i++){
      const it=items[i];
      let flap,px,py,pz,yaw,pitch;
      if(!launched){
        px=it.x; py=it.y+0.04*Math.sin(t*1.3+it.ph); pz=it.z;
        yaw=it.ry+0.12*Math.sin(t*0.4+it.ph); pitch=0;
        flap=0.10*Math.max(0,Math.sin(t*1.8+it.ph));
      }else{
        const raw=Math.min(1,Math.max(0,(t-t0-it.delay)/it.T));
        const e=1-Math.pow(1-raw,2.2);
        const post=Math.max(0,t-t0-it.delay-it.T);
        const a=it.a0+it.turn*e+post*0.42;
        const r=it.r0*(0.35+1.5*e);
        px=bar[0]+Math.cos(a)*r; pz=bar[2]+Math.sin(a)*r;
        py=it.y+it.h*e+Math.sin(t*0.7+it.ph)*0.6;
        yaw=a+Math.PI/2;
        pitch=-0.5*Math.sin(Math.min(e,1)*Math.PI);
        flap=0.8*Math.sin(t*(12-5*Math.min(e,1))+it.ph);
      }
      dm.position.set(px,py,pz);
      dm.rotation.set(pitch,yaw,0.14*Math.sin(t*0.9+it.ph));
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); M.copy(dm.matrix);
      bodies.setMatrixAt(i,M);
      wm.position.set(0.05,0.62,0.1); wm.rotation.set(0,0,flap); wm.updateMatrix();
      MW.multiplyMatrices(M,wm.matrix); wingR.setMatrixAt(i,MW);
      wm.rotation.set(0,0,-flap); wm.updateMatrix();
      MW.multiplyMatrices(M,wm.matrix); wingL.setMatrixAt(i,MW);
    }
    bodies.instanceMatrix.needsUpdate=true; wingL.instanceMatrix.needsUpdate=true; wingR.instanceMatrix.needsUpdate=true;
  };
  upd(0);
  return {g,update:function(t){upd(t);},launch:function(tNow){ if(!launched){launched=true; t0=tNow;} }};
}

function bCover(){ // 卷首 · 溪亭日暮 —— 夕照里的荷塘全景，溪亭半隐远岸，一水映着天光
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0c1710,c2:0x18291b,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:3,peaks:5,seed:87,color:0x0c1911,atmo:0x2c4434,fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-85); g.add(ridge.g);
  const water=makeWater({size:15,seg:24,amp:0.09,freq:0.16,speed:0.45,flow:[0.08,0.5],spec:0.45,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x39543c,moonDir:[0,160,0],y:-1.4});
  water.mesh.scale.set(1,1,13); water.mesh.position.set(0,-1.4,-30); g.add(water.mesh);
  /* 溪亭：四柱小亭+攒尖顶（远岸点景） */
  const pav=new THREE.Group();
  const PB=new GeoBag();
  const pbase=new THREE.CylinderGeometry(3.2,3.6,0.7,10); pbase.translate(0,0.35,0); PB.put(pbase,shadeColor(0x3a3a30,0.9));
  for(let i=0;i<4;i++){
    const a=i/4*Math.PI*2+Math.PI/4;
    const pl=new THREE.CylinderGeometry(0.16,0.19,3.4,7); pl.translate(Math.cos(a)*2.2,2.4,Math.sin(a)*2.2); PB.put(pl,shadeColor(0x241a10,1.1));
  }
  const rail=new THREE.TorusGeometry(2.2,0.05,5,18); rail.rotateX(Math.PI/2); rail.translate(0,1.5,0); PB.put(rail,shadeColor(0x3a2c1a,1.2));
  pav.add(PB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c2c22,emissive:0x0a0806}),{c:0x8fc9b8,i:0.22,p:2.4})));
  const roof=new THREE.Mesh(new THREE.ConeGeometry(3.6,1.6,4),
    new THREE.MeshPhongMaterial({color:0x1c2418,shininess:14,emissive:0x0a0f08}));
  roof.rotateY(Math.PI/4); roof.position.set(0,4.9,0); pav.add(roof);
  pav.position.set(-16,-1.4,-52); pav.rotation.y=0.5; pav.scale.setScalar(1.35); g.add(pav);
  /* 亭中一点暖光（夕照+亭灯：全页低饱和暖点的引子） */
  const pavGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe0b470,
    transparent:true,opacity:0.14,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  pavGlow.scale.set(10,8,1); pavGlow.position.set(-16,2.2,-52); pavGlow.renderOrder=-5; g.add(pavGlow);
  /* 远处荷带 + 亭边游人 */
  const lotus=makeLotus({leaves:26,flowers:8,w:100,d:24,cx:2,cz:-40,seed:29});
  lotus.g.position.y=-1.35; g.add(lotus.g);
  const crowd=makeCrowd({n:3,rect:[-22,-50,10,7],seed:97,color:0x131e14,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  /* 夕照：西天一带低饱和暖光（全页唯一暖源，随呼吸微明） */
  const dusk=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8b070,
    transparent:true,opacity:0.19,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dusk.scale.set(150,50,1); dusk.position.set(-45,16,-115); dusk.renderOrder=-7; g.add(dusk);
  const motes=makeGlow({n:40,box:[190,26,110],pos:[0,8,-30],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,30,130],pos:[0,10,-56],scale:78,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:52,n:9,d:7,color:0x081009,seed:101,sway:0.7,rim:0.12,rimC:0x8fc9b8});
  brL.g.position.set(-26,-1.4,44); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x060c08,seed:103,rim:0.05,rimC:0x8fc9b8});
  rk.g.position.set(15,-1.0,18); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:8,d:5,color:0x071009,seed:105,sway:1.0,tip:0x2c4028});
  reed.g.position.set(-12,-1.2,20); g.add(reed.g);
  addLights(g,{c:0xe0c890,i:0.46,p:[-50,70,30]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    lotus.update(t); crowd.update(t);
    brL.update(t,k); rk.update(t,k); reed.update(t,k);
    dusk.material.opacity=k*(0.15+0.04*Math.sin(t*0.37));
    pavGlow.material.opacity=k*(0.12+0.02*Math.sin(t*0.5+1));
  }};
}
function bWuru(){ // 壹 · 藕花深处 —— 荷荡夹一水道，小舟（舟中少女）误入最密处；萤火明灭、荷瓣缓落
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0x0a130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:38,layers:3,peaks:4,seed:111,color:0x09150e,atmo:0x29412e,fogK:0.62,glowK:0.04,glow:0xaac890,y:-6});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  const water=makeWater({size:16,seg:28,amp:0.08,freq:0.17,speed:0.5,flow:[0.1,0.55],spec:0.45,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x3a5640,moonDir:[0,160,0],y:0});
  water.mesh.scale.set(1,1,12); water.mesh.position.set(0,0,-14); g.add(water.mesh);
  /* 荷荡：两岸夹一水道，舟在最小水道处；近景一簇大叶框底 */
  const lotL=makeLotus({leaves:26,flowers:9,w:36,d:42,cx:-13,cz:-4,seed:121});
  const lotR=makeLotus({leaves:22,flowers:8,w:28,d:36,cx:12,cz:-6,seed:123});
  const lotF=makeLotus({leaves:20,flowers:7,w:74,d:22,cx:0,cz:-34,seed:125});
  const lotN=makeLotus({leaves:9,flowers:3,w:15,d:9,cx:6.5,cz:8,seed:127});
  g.add(lotL.g); g.add(lotR.g); g.add(lotF.g); g.add(lotN.g);
  /* 小舟（舟中少女，日暮点亮船尾灯） */
  const skiff=makeSkiff({scale:1.0});
  skiff.g.position.set(-1.5,0.04,-3); skiff.g.rotation.y=Math.PI+0.35;
  g.add(skiff.g);
  /* 黄绿萤火 + 粉白落瓣（青绿赛道母题；盒子远离相机，避免近距粒子糊成光球） */
  const flies=makeGlow({n:34,box:[70,6,34],pos:[0,2.2,-14],color:0xcfe08a,size:4,speed:0.05,rise:0,maxA:0.18});
  g.add(flies.points);
  const petals=makeGlow({n:22,box:[50,7,24],pos:[0,3.2,-12],color:0xe8c4c4,size:3.5,speed:0.03,rise:0,maxA:0.13});
  g.add(petals.points);
  const motes=makeGlow({n:26,box:[150,20,70],pos:[0,7,-20],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,110],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const dusk=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8b070,
    transparent:true,opacity:0.18,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dusk.scale.set(120,38,1); dusk.position.set(-52,12,-105); dusk.renderOrder=-7; g.add(dusk);
  const reed=makeForeground({kind:'芦苇',w:20,n:9,d:5,color:0x071009,seed:131,sway:1.1,tip:0x2c4028});
  reed.g.position.set(-13,-1.0,13); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:12,d:5,color:0x060b07,seed:133,rim:0.12,rimC:0x8fc9b8});
  rk.g.position.set(10,-1.0,11); g.add(rk.g);
  addLights(g,{c:0xd8c090,i:0.42,p:[-45,65,25]},{c:0x1e2c20,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      flies.update(t); petals.update(t);
      lotL.update(t); lotR.update(t); lotF.update(t); lotN.update(t);
      reed.update(t,k); rk.update(t,k);
      skiff.update(t,k,0);
      dusk.material.opacity=k*(0.14+0.04*Math.sin(t*0.4));
    },onEnter(){
      pluck(2,0.15,0.10); pluck(4,0.7,0.09);
    }};
}
function bJingdu(){ // 贰（末境·可点击）· 鸥鹭惊起 —— 争渡，争渡；点击：急桨击水，一滩鸥鹭冲天盘旋
  const g=new THREE.Group();
  const ctl={t:0,lastT:0,clicked:false,pulse:0,strokeT:0};
  const grd=makeGround({r:220,c1:0x0a130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:36,layers:2,peaks:4,seed:141,color:0x091409,atmo:0x27402c,fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  const water=makeWater({size:16,seg:28,amp:0.09,freq:0.18,speed:0.55,flow:[0.12,0.6],spec:0.5,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x3a5640,moonDir:[0,160,0],y:0});
  water.mesh.scale.set(1,1,12); water.mesh.position.set(0,0,-12); g.add(water.mesh);
  /* 一滩沙洲：鸥鹭群栖（白色在青绿暮色里最亮，是下一拍的伏笔） */
  const bar=new THREE.Mesh(new THREE.SphereGeometry(1,12,8),
    rimHook(new THREE.MeshPhongMaterial({color:0x4a4434,shininess:6,emissive:0x12100a}),{c:0x8fc9b8,i:0.16,p:2.4}));
  bar.scale.set(9.5,0.5,3.4); bar.position.set(-10,0.02,-14); g.add(bar);
  const flock=makeEgretFlock({n:26,bar:[-10,0.1,-14],spread:[6.0,2.2],seed:151});
  g.add(flock.g);
  /* 小舟（少女与急桨所在）+ 桨花（跟船，争渡时逐桨迸溅） */
  const skiff=makeSkiff({scale:1.02});
  skiff.g.position.set(-1.5,0.04,0.5); skiff.g.rotation.y=Math.PI-0.1;
  g.add(skiff.g);
  const splash=makeBurst({n:26,color:0xc8e4d4,pos:[1.4,-0.35,2.0]});
  skiff.g.add(splash.points);
  /* 荷荡两侧夹水道 + 近景一簇大叶框底 */
  const lotL=makeLotus({leaves:18,flowers:6,w:26,d:30,cx:-14,cz:-2,seed:161});
  const lotR=makeLotus({leaves:18,flowers:6,w:24,d:28,cx:12,cz:-4,seed:163});
  const lotF=makeLotus({leaves:12,flowers:4,w:60,d:18,cx:2,cz:-30,seed:165});
  const lotN=makeLotus({leaves:7,flowers:2,w:13,d:8,cx:10,cz:7,seed:167});
  g.add(lotL.g); g.add(lotR.g); g.add(lotF.g); g.add(lotN.g);
  const flies=makeGlow({n:26,box:[56,5,26],pos:[0,2,-12],color:0xcfe08a,size:4,speed:0.05,rise:0,maxA:0.16});
  g.add(flies.points);
  const motes=makeGlow({n:24,box:[150,20,70],pos:[0,7,-20],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,110],pos:[0,8,-50],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const dusk=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8b070,
    transparent:true,opacity:0.18,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dusk.scale.set(120,38,1); dusk.position.set(-50,12,-110); dusk.renderOrder=-7; g.add(dusk);
  const reed=makeForeground({kind:'芦苇',w:16,n:7,d:4,color:0x071009,seed:171,sway:1.2,tip:0x2c4028});
  reed.g.position.set(15,-1.0,12); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x060b07,seed:173,rim:0.12,rimC:0x8fc9b8});
  rk.g.position.set(-14,-1.4,9); g.add(rk.g);
  addLights(g,{c:0xd8c090,i:0.44,p:[-45,65,25]},{c:0x1e2c20,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt; ctl.lastT=t;
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const row=ctl.clicked?1:0;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      flies.update(t); flock.update(t);
      lotL.update(t); lotR.update(t); lotF.update(t); lotN.update(t);
      reed.update(t,k); rk.update(t,k);
      skiff.update(t,k,row);
      /* 急桨节奏：每半秒一桨，桨叶击水迸一蓬水花+一声轻响（全页动效最高点） */
      if(row&&t-ctl.strokeT>0.55){
        ctl.strokeT=t; splash.fire();
        pluck(2+(Math.floor(t/0.55)%3),0,0.06);
      }
      /* 夕照微光：争渡后随 pulse 再亮一拍（公式峰值 0.18 = 初值，不越 fadeK 基线） */
      dusk.material.opacity=k*(0.14+0.025*Math.sin(t*0.4)+0.015*ctl.pulse);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        flock.launch(ctl.lastT||0);
        pluck(4,0,0.14); pluck(5,0.25,0.12); pluck(3,0.55,0.10); pluck(5,0.9,0.09); pluck(4,1.3,0.08);
        const fl=$('#flash'); fl.textContent='惊起一滩鸥鹭'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                            // 可反复点：再划一桨，群鹭盘旋再高一拍
    },clicked:false};
  return api;
}
