/* ================= 金缕衣 · 三境场景（夜宴金彩·中唐劝时曲变体：金缕少年、花开堪折） =================
   美术口径：夜宴庭园金彩——金缕华服（题面主色，金线光华）、夜宴灯列、帷帐厅堂；
   花开是对比的生命色（低饱和暖粉，非艳红）。末境点击：金缕光华渐淡 vs 花枝盛放催折。 */

/* 宴厅剪影：台基 + 堂身 + 前廊四柱 + 双层檐 + 攒尖顶 + 一门两窗金光（合批 1 mesh） */
function makeYanTing(){
  const B=new GeoBag(), c1=0x120d08, c2=0x1a120a, c3=0x241810;
  const base=new THREE.BoxGeometry(11,0.7,7.5); base.translate(0,0.35,0); B.put(base,c1);
  const body=new THREE.BoxGeometry(8.6,3.2,5.4); body.translate(0,2.3,0); B.put(body,c2);
  [-3.4,-1.15,1.15,3.4].forEach(function(x){
    const p=new THREE.CylinderGeometry(0.17,0.20,3.4,7); p.translate(x,2.2,2.9); B.put(p,c3);
  });
  const e1=new THREE.BoxGeometry(10.4,0.42,6.6); e1.translate(0,4.15,0); B.put(e1,c3);
  const e2=new THREE.BoxGeometry(9.0,0.50,5.2); e2.translate(0,4.85,0); B.put(e2,c2);
  const roof=new THREE.ConeGeometry(5.6,1.9,4); roof.rotateY(Math.PI/4); roof.translate(0,6.0,0); B.put(roof,c3);
  const door=new THREE.BoxGeometry(1.5,2.3,0.16); door.translate(0,1.6,2.72); B.put(door,0xb8862a);
  [-2.6,2.6].forEach(function(x){
    const w=new THREE.BoxGeometry(1.0,1.2,0.14); w.translate(x,2.4,2.72); B.put(w,0x9a7028);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x0a0603}),{c:0xd8a860,i:0.26,p:2.6})));
  return g;
}

/* 灯树：座 + 杆 + 横挑 + 挂灯（架 1 mesh + 灯笼 3-4 call；glow 初值提到包络最大值） */
function makeDengShu(o){
  o=o||{};
  const B=new GeoBag();
  const bs=new THREE.CylinderGeometry(0.16,0.22,0.14,8); bs.translate(0,0.07,0); B.put(bs,0x241810);
  const pole=new THREE.CylinderGeometry(0.05,0.07,3.2,7); pole.translate(0,1.6,0); B.put(pole,0x33220f);
  const arm=new THREE.CylinderGeometry(0.035,0.035,0.9,6); arm.rotateZ(Math.PI/2); arm.translate(0.32,3.15,0); B.put(arm,0x33220f);
  const hook=new THREE.CylinderGeometry(0.02,0.02,0.30,5); hook.translate(0.72,2.97,0); B.put(hook,0x2a1c12);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x5a4426,emissive:0x080503}),{c:0xd8a05a,i:0.24,p:2.5})));
  const lt=makeLantern(o.ls===undefined?0.42:o.ls,{flick:o.flick===undefined?0.9:o.flick,glow:o.glow});
  lt.position.set(0.72,2.64,0); g.add(lt);
  /* makeLantern 内辉包络最高 1.08×base——初值提到包络最大值，fadeK 合规 */
  const gmax=(o.glow===undefined?0.72:o.glow)*1.08;
  lt.traverse(function(n){ if(n.isSprite)n.material.opacity=gmax; });
  return {g,update(t,k){ lt.userData.update(t,k); }};
}

/* 金缕衣：衣架 + 绛纱衣身 + 三道金缕领缘（金线光华=题面主色；dim 入参供末境「光华渐淡」） */
function makeJinLu(o){
  o=o||{};
  const hi=o.hi===undefined?1.55:o.hi;
  const stand=new GeoBag();
  [-0.92,0.92].forEach(function(x){
    const pole=new THREE.CylinderGeometry(0.05,0.07,2.9,8); pole.translate(x,1.45,0); stand.put(pole,0x3a2414);
    const bs=new THREE.BoxGeometry(0.52,0.10,0.52); bs.translate(x,0.05,0); stand.put(bs,0x2c1c10);
  });
  const bar=new THREE.CylinderGeometry(0.045,0.045,2.0,8); bar.rotateZ(Math.PI/2); bar.translate(0,2.86,0); stand.put(bar,0x4a3018);
  const g=new THREE.Group();
  g.add(stand.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4426,emissive:0x0a0704}),{c:0xd8a860,i:0.26,p:2.5})));
  const pts=[[0.78,0.58],[0.80,0.98],[0.74,1.42],[0.62,1.88],[0.48,2.18],[0.32,2.36],[0.10,2.44]];
  const robe=new THREE.LatheGeometry(pts.map(p=>new THREE.Vector2(p[0],p[1])),20);
  robe.scale(1,1,0.40);
  const robeMesh=new THREE.Mesh(robe,rimHook(new THREE.MeshPhongMaterial({color:0x6e2636,shininess:30,
    specular:0xd8a878,emissive:0x2a0e14,side:THREE.DoubleSide}),{c:0xffc890,i:0.48,p:2.6}));
  robeMesh.position.y=0.02; g.add(robeMesh);
  const gold=new GeoBag();
  [[0.80,0.88],[0.70,1.52],[0.52,2.10]].forEach(function(rr){
    const t=new THREE.TorusGeometry(rr[0]+0.015,0.035,6,26); t.rotateX(Math.PI/2); t.scale(1,1,0.42);
    t.translate(0,rr[1],0); gold.put(t,0xd4a84f);
  });
  const collar=new THREE.TorusGeometry(0.14,0.045,6,18); collar.rotateX(Math.PI/2); collar.scale(1,1,0.5);
  collar.translate(0,2.42,0); gold.put(collar,0xe0b860);
  const goldMat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:88,
    specular:0xffe8b8,emissive:0x9a6a1c,emissiveIntensity:hi}),{c:0xffe2a0,i:0.55,p:3.0});
  g.add(gold.mesh(goldMat));
  return {g,goldMat,update(t,k,dim){
    const d=dim===undefined?0:dim;   // 光华渐淡：dim 0→1 时金线光华收敛
    goldMat.emissiveIntensity=k*hi*(1-0.87*d)*(0.84+0.16*Math.sin(t*1.8));
  }};
}

/* 手中花枝（劝时人持花）：茎叶 + 五瓣金蕊一小朵（合批 1 mesh） */
function makeHuaXiao(){
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[0.05,0.34,0.02],0.016,0.010,5),0x33200f);
  const leaf=new THREE.SphereGeometry(0.05,6,5); leaf.scale(1,0.35,0.5); leaf.rotateZ(0.7);
  leaf.translate(0.07,0.16,0.02); B.put(leaf,0x3e5a2e);
  const leaf2=new THREE.SphereGeometry(0.045,6,5); leaf2.scale(1,0.32,0.5); leaf2.rotateZ(-0.6);
  leaf2.translate(-0.03,0.23,-0.01); B.put(leaf2,0x3e5a2e);
  for(let i=0;i<5;i++){
    const a=i/5*6.283;
    const p=new THREE.SphereGeometry(0.055,7,5); p.scale(1,0.5,1);
    p.translate(0.05+Math.cos(a)*0.062,0.40+Math.sin(a)*0.062,0.02+Math.sin(a)*0.02);
    B.put(p,0xd89098);
  }
  const core=new THREE.SphereGeometry(0.028,7,5); core.translate(0.05,0.40,0.02); B.put(core,0xd4a84f);
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0xffd0d0,emissive:0x1a0a0e})));
  return g;
}

/* 花枝：老干斜出 + 满枝花簇（初为含苞，glow→1 盛放）+ 一枝「催折」垂枝 —— 标志性瞬间主体
   返回 {g,update(t,k,glow)}；花瓣低饱和暖粉 0xd89098，金蕊 0xd4a84f 与金缕同源 */
function makeHuaZhi(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?209:o.seed);
  const B=new GeoBag();                       // 枝干（合批 1 mesh）
  const joints=[[0,0,0],[0.35,1.5,-0.15],[1.0,3.1,0.15],[1.7,4.4,0.05],[2.3,5.5,0.45]];
  for(let i=0;i<joints.length-1;i++)
    B.put(limbGeo(joints[i],joints[i+1],0.20-0.035*i,0.16-0.035*i,7),0x2e1c12);
  const clus=[[-0.9,3.3,0.45],[2.7,4.1,-0.6],[3.3,6.1,0.15],[0.5,4.6,0.8]];
  clus.forEach(function(c,i){
    B.put(limbGeo(joints[i+1],c,0.07,0.04,6),0x33200f);
  });
  [0,1,2].forEach(function(i){
    const bud=new THREE.SphereGeometry(0.09,6,5); bud.scale(1,1.3,1);
    const t=joints[1+i];
    bud.translate(t[0]+(R()-0.5)*0.5,t[1]+0.3+R()*0.7,t[2]+(R()-0.5)*0.4);
    B.put(bud,0x6a2830);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a26,emissive:0x080503}),{c:0xd8a860,i:0.22,p:2.4})));
  /* 花瓣合批（盛放=整组放大 + 金蕊辉起），初值=含苞 */
  const petalMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0xffd0d0,emissive:0x6a1826,emissiveIntensity:0.35});
  const petC=[0xd89098,0xe0a0a8,0xc88088,0xd898a0];
  function blossom(cx,cy,cz,rr,n,bag){
    for(let i=0;i<5;i++){
      const a=i/5*6.283+rr;
      const p=new THREE.SphereGeometry(0.155,7,5); p.scale(1,0.45,1);
      p.translate(cx+Math.cos(a)*0.17,cy+Math.sin(a)*0.06,cz+Math.sin(a)*0.17);
      bag.put(p,petC[(i+n)%4]);
    }
    const core=new THREE.SphereGeometry(0.075,7,5); core.translate(cx,cy+0.02,cz); bag.put(core,0xd4a84f);
  }
  const PB=new GeoBag();
  clus.forEach(function(c,i){
    blossom(c[0],c[1],c[2],R()*3,i, PB);
    blossom(c[0]+0.30+R()*0.2,c[1]+0.24,c[2]+(R()-0.5)*0.3,R()*3,i+2, PB);
    blossom(c[0]-0.26,c[1]+0.34+R()*0.15,c[2]+(R()-0.5)*0.4,R()*3,i+1, PB);
  });
  const petals=PB.mesh(petalMat); petals.scale.setScalar(0.58);
  petals.renderOrder=1; g.add(petals);
  /* 「催折」垂枝：独立小枝组（枝 1 + 花瓣 1），盛放时整枝下坠 */
  const twig=new THREE.Group(); twig.position.set(2.3,5.5,0.45);
  const TB=new GeoBag();
  TB.put(limbGeo([0,0,0],[1.15,0.55,0.5],0.065,0.04,6),0x33200f);
  twig.add(TB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a26,emissive:0x080503})));
  const TP=new GeoBag();
  blossom(0.75,0.42,0.32,R()*3,0,TP);
  blossom(1.15,0.55,0.5,R()*3,2,TP);
  const tPetal=TP.mesh(petalMat); tPetal.scale.setScalar(0.58);
  twig.add(tPetal);
  twig.rotation.z=0.14; g.add(twig);
  return {g,twig,update(t,k,glow){
    const gl=glow===undefined?0:glow;
    const bs=0.58+0.42*gl;
    petals.scale.setScalar(bs); tPetal.scale.setScalar(bs);
    twig.rotation.z=0.14+0.60*gl; twig.rotation.x=0.06*gl;
    petalMat.emissiveIntensity=k*(0.35+1.05*gl)*(0.85+0.15*Math.sin(t*2.1));
    g.rotation.z=0.012*Math.sin(t*0.5);
  }};
}

function bCover(){ // 卷首 · 金夜庭园 —— 夜宴未散，庭中灯树夹径，远处宴厅一门烛暖
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0a0708,c2:0x1a120a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:71,color:0x0b0808,atmo:0x3a2c1e,fogK:0.72,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const ting=makeYanTing(); ting.position.set(-24,0,-62); ting.scale.setScalar(1.35); g.add(ting);
  const doorGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb060,
    transparent:true,opacity:0.46,depthWrite:false,blending:THREE.AdditiveBlending}));
  doorGlow.scale.set(11,7,1); doorGlow.position.set(-24,3.6,-58.8); doorGlow.renderOrder=2; g.add(doorGlow);
  const ds1=makeDengShu({glow:0.75}); ds1.g.position.set(9.5,0,-26); g.add(ds1.g);
  const ds2=makeDengShu({glow:0.68,ls:0.38}); ds2.g.position.set(-5.5,0,-32); g.add(ds2.g);
  const guests=makeCrowd({n:4,rect:[10,-44,28,10],seed:209,color:0x14100a,rimC:0xd4a84f,rim:0.22,sMin:0.8,sMax:1.0});
  g.add(guests.mesh);
  const maid=makeFigure({pose:'独立',robe:0x5a2430,belt:0xa8843a,skin:0xd9b189,hat:'发髻',
    face:0.5,scale:0.9,rim:0.42,rimC:0xffd890,noProp:true});
  maid.position.set(8.4,0,-23.4); g.add(maid);
  const motes=makeGlow({n:56,box:[180,30,100],pos:[0,8,-30],color:0xd4a84f,size:6,speed:0.05,rise:0,maxA:0.30});
  g.add(motes.points);
  const mist=makeMist({n:4,spread:[240,30,140],pos:[0,8,-50],scale:78,color:0x8a6a4a,op:0.09});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',n:2,w:16,d:6,color:0x060404,seed:19,sway:0.9,rim:0.14});
  fg.g.position.set(-18,-1,18); g.add(fg.g);
  const rail=makeForeground({kind:'栏杆',w:26,h:3.0,color:0x080505,seed:21,rim:0.12});
  rail.g.position.set(0,-2,20); g.add(rail.g);
  addLights(g,{c:0xd8a860,i:0.34,p:[-40,60,30]},{c:0x2c2014,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); guests.update(t); maid.update(t,k);
    fg.update(t,k); rail.update(t,k); ds1.update(t,k); ds2.update(t,k);
    doorGlow.material.opacity=k*(0.40+0.06*Math.sin(t*0.7));
  }};
}

function bJinLv(){ // 壹 · 金缕少年 —— 夜宴灯彩，金缕华服光华流转；持花之人劝君惜取少年时
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0b0808,c2:0x1c1410});
  g.add(grd.mesh);
  const ridge=makeRange({r:210,h:24,layers:2,peaks:4,seed:2091,color:0x0c0808,atmo:0x38281c,fogK:0.62,glowK:0.05});
  g.add(ridge.g);
  /* 厅堂一瞥：帷帐 + 双柱 + 灯列成行 */
  const curt=makeCurtain({w:15,h:6.4,color:0x471419,dark:0x200a0d,folds:9,deep:0.9});
  curt.g.position.set(0.6,0,-13.6); g.add(curt.g);
  const plA=makePillar({h:5.2,r:0.24,color:0x2c1c10,top:false}); plA.g.position.set(-9.4,0,-11.6); g.add(plA.g);
  const plB=makePillar({h:5.2,r:0.24,color:0x2c1c10,top:false}); plB.g.position.set(10.0,0,-11.6); g.add(plB.g);
  const lt1=makeLantern(0.5,{flick:0.95}); lt1.position.set(-7.8,3.1,-11.2); g.add(lt1);
  const lt2=makeLantern(0.5,{flick:0.85}); lt2.position.set(7.6,3.1,-11.2); g.add(lt2);
  const lt3=makeLantern(0.44,{flame:false,glow:0.62}); lt3.position.set(-2.6,3.7,-12.2); g.add(lt3);
  const lt4=makeLantern(0.44,{flame:false,glow:0.62}); lt4.position.set(3.4,3.7,-12.2); g.add(lt4);
  [lt1,lt2,lt3,lt4].forEach(function(lt){
    lt.traverse(function(n){ if(n.isSprite)n.material.opacity=0.78; });
  });
  /* 长案 + 盘飧 + 酒器（樽壶爵杯碗混搭） */
  const tb=makeTable({w:5.2,d:2.0,h:1.52,wood:0x33200f}); tb.g.position.set(0.4,0,-4.6); g.add(tb.g);
  const ds1=makeDish({r:0.8,n:5,plate:0x7a6a52}); ds1.g.position.set(-1.2,1.52,-4.9); g.add(ds1.g);
  const ds2=makeDish({r:0.66,n:4,plate:0x6a5a46,sheen:false}); ds2.g.position.set(1.7,1.52,-4.4); g.add(ds2.g);
  const vz1=makeVessel({type:'樽',mat:'金',scale:0.62,liquid:true,shadow:false}); vz1.g.position.set(-0.4,1.52,-4.4); g.add(vz1.g);
  const vz2=makeVessel({type:'壶',mat:'陶',scale:0.7,shadow:false}); vz2.g.position.set(0.7,1.52,-5.0); g.add(vz2.g);
  const vz3=makeVessel({type:'爵',mat:'金',scale:0.55,shadow:false}); vz3.g.position.set(2.7,1.52,-4.9); g.add(vz3.g);
  const vz4=makeVessel({type:'杯',mat:'金',scale:0.5,liquid:true,shadow:false}); vz4.g.position.set(-2.1,1.52,-4.3); g.add(vz4.g);
  const vz5=makeVessel({type:'碗',mat:'陶',scale:0.6,shadow:false}); vz5.g.position.set(0.1,1.52,-4.0); g.add(vz5.g);
  const vz6=makeVessel({type:'碗',mat:'玉',scale:0.5,shadow:false}); vz6.g.position.set(2.3,1.52,-4.2); g.add(vz6.g);
  /* 金缕衣（题面主器）+ 持花劝时人 + 席上客 + 火盆 */
  const jin=makeJinLu({}); jin.g.position.set(-4.9,0,-7.0); jin.g.rotation.y=0.55; g.add(jin.g);
  const poet=makeFigure({pose:'举杯',robe:0x6a2838,belt:0xc9a24a,skin:0xd9b189,hair:0x1a1210,collar:0xe8d0b0,
    hat:'幞头',face:-0.5,scale:1.06,rim:0.55,rimC:0xffd890,noProp:true});
  poet.position.set(4.3,0,-7.6); poet.rotation.y=-0.5; g.add(poet);
  const sprig=makeHuaXiao(); sprig.position.set(0.34,3.08,0.47); sprig.rotation.z=-0.35; poet.add(sprig);
  const guest=makeFigure({pose:'坐饮',robe:0x2c2434,belt:0x8a6a38,skin:0xd9b189,hat:'幞头',
    face:2.6,scale:1.0,rim:0.4,rimC:0xffd0a0});
  guest.position.set(5.8,0,-5.4); guest.rotation.y=-0.7; g.add(guest);
  const br=makeBrazier({r:0.5,fh:1.0,fw:0.9,light:1.2,lightD:26}); br.g.position.set(7.2,0,-8.8); g.add(br.g);
  /* 香篆 + 金尘 + 雾 + 前景画栏 */
  const smoke=makeGlow({n:26,box:[0.6,5.5,0.6],pos:[-3.0,2.4,-6.6],color:0xc0a890,size:3.2,speed:0.15,rise:1,maxA:0.16});
  g.add(smoke.points);
  const motes=makeGlow({n:60,box:[34,12,26],pos:[0,4.5,-6],color:0xd4a84f,size:4.6,speed:0.05,rise:0.25,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:4,spread:[120,16,70],pos:[0,4,-24],scale:58,color:0x8a6a4a,op:0.07});
  g.add(mist.g);
  const rail=makeForeground({kind:'栏杆',w:24,h:2.8,color:0x080505,seed:23,rim:0.12});
  rail.g.position.set(0,-1.4,8.6); g.add(rail.g);
  addLights(g,{c:0xffc890,i:0.30,p:[-20,50,26]},{c:0x322414,i:0.72});
  const pl=new THREE.PointLight(0xffb060,1.76,30); pl.position.set(0.4,3.6,-4.8); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); smoke.update(t);
    poet.update(t,k); guest.update(t,k); rail.update(t,k);
    lt1.userData.update(t,k); lt2.userData.update(t,k); lt3.userData.update(t,k); lt4.userData.update(t,k);
    br.update(t,k); jin.update(t,k,0);
    pl.intensity=k*1.76*(0.72+0.18*Math.sin(t*8.3)+0.10*Math.sin(t*15.7));
  }};
}

function bZheHua(){ // 贰（末境·可点击）· 花开堪折 —— 点击花开：金缕光华渐淡，花枝盛放催折
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,glow:0};
  const grd=makeGround({r:110,c1:0x0b0808,c2:0x1a1210});
  g.add(grd.mesh);
  const ridge=makeRange({r:220,h:26,layers:2,peaks:5,seed:2101,color:0x0c0808,atmo:0x3e2c1c,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  const curt=makeCurtain({w:13,h:6.0,color:0x541a24,dark:0x260c12,folds:8,deep:0.9});
  curt.g.position.set(-6.2,0,-12.8); g.add(curt.g);
  const plA=makePillar({h:5.2,r:0.24,color:0x2c1c10,top:false}); plA.g.position.set(6.4,0,-11.4); g.add(plA.g);
  const lt1=makeLantern(0.5,{flick:0.9}); lt1.position.set(5.2,3.1,-11.0); g.add(lt1);
  const lt2=makeLantern(0.44,{flame:false,glow:0.5}); lt2.position.set(-10.2,3.2,-12.0); g.add(lt2);
  [lt1,lt2].forEach(function(lt){
    lt.traverse(function(n){ if(n.isSprite)n.material.opacity=0.78; });
  });
  /* 金缕衣（光华将淡）与花枝（将盛放催折）同框对切 —— 全诗警策的画面化 */
  const jin=makeJinLu({hi:1.5}); jin.g.position.set(-4.7,0,-6.8); jin.g.rotation.y=0.5; g.add(jin.g);
  const hz=makeHuaZhi({seed:209}); hz.g.position.set(3.6,0,-6.4); hz.g.scale.setScalar(1.18); g.add(hz.g);
  /* 持花劝时人 */
  const poet=makeFigure({pose:'举杯',robe:0x6a2838,belt:0xc9a24a,skin:0xd9b189,hair:0x1a1210,collar:0xe8d0b0,
    hat:'幞头',face:0.35,scale:1.05,rim:0.55,rimC:0xffd890,noProp:true});
  poet.position.set(-0.4,0,-8.8); poet.rotation.y=0.28; g.add(poet);
  const sprig=makeHuaXiao(); sprig.position.set(0.34,3.08,0.47); sprig.rotation.z=-0.35; poet.add(sprig);
  /* 小案余席 */
  const tb=makeTable({w:3.6,d:1.7,h:1.52,wood:0x33200f}); tb.g.position.set(2.2,0,-3.6); g.add(tb.g);
  const ds1=makeDish({r:0.6,n:4,plate:0x7a6a52,sheen:false}); ds1.g.position.set(2.0,1.52,-3.6); g.add(ds1.g);
  const vz1=makeVessel({type:'樽',mat:'金',scale:0.56,liquid:true,shadow:false}); vz1.g.position.set(3.1,1.52,-3.8); g.add(vz1.g);
  const vz2=makeVessel({type:'杯',mat:'金',scale:0.5,liquid:true,shadow:false}); vz2.g.position.set(1.3,1.52,-3.4); g.add(vz2.g);
  /* 落瓣微光 + 迸瓣 + 金尘 + 雾 + 前景 */
  const petals=makeGlow({n:44,box:[11,7.5,8],pos:[4.6,5.2,-6.4],color:0xd89098,size:4.6,speed:0.08,rise:0,maxA:0.30});
  g.add(petals.points);
  const burst=makeBurst({n:90,color:0xe8b0a0,pos:[4.8,5.6,-6.2]}); g.add(burst.points);
  const motes=makeGlow({n:44,box:[34,12,26],pos:[0,4.5,-6],color:0xd4a84f,size:4.2,speed:0.05,rise:0.2,maxA:0.20});
  g.add(motes.points);
  const mist=makeMist({n:4,spread:[120,16,70],pos:[0,4,-24],scale:58,color:0x8a6a4a,op:0.07});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',n:2,w:15,d:5,color:0x060404,seed:27,sway:0.9,rim:0.14});
  fg.g.position.set(10,-0.5,13.5); g.add(fg.g);
  const rail=makeForeground({kind:'栏杆',w:22,h:2.8,color:0x080505,seed:29,rim:0.12});
  rail.g.position.set(-2,-1.4,8.4); g.add(rail.g);
  addLights(g,{c:0xffd8a0,i:0.32,p:[-20,50,26]},{c:0x362816,i:0.74});
  const pl=new THREE.PointLight(0xffc890,1.7,32); pl.position.set(3.6,5.0,-5.6); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.glow=Math.min(1,ctl.glow+dt/1.8);
      const gl=ctl.glow;
      ridge.update(t,0); mist.update(t,k); motes.update(t); petals.update(t);
      burst.update(t); poet.update(t,k); rail.update(t,k); fg.update(t,k);
      lt1.userData.update(t,k); lt2.userData.update(t,k);
      jin.update(t,k,gl); hz.update(t,k,gl);
      pl.intensity=k*1.7*(0.60+0.40*gl*(0.85+0.15*Math.sin(t*2.4)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire();
        pluck(0,0.05,0.14); pluck(2,0.35,0.13); pluck(4,0.7,0.12); pluck(5,1.05,0.10); bell();
        const fl=$('#flash'); fl.textContent='花开堪折'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
