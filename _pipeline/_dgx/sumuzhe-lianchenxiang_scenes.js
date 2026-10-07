/* ================= 苏幕遮·燎沉香 · 四境场景（青绿春晓·荷塘晓色变体：燎香雀语、风荷并举、久客长安、梦入芙蓉浦）
   本诗专属系统「风荷举」：宿雨在叶心，初阳晒干宿雨、荷叶一一挺出水面（词眼「水面清圆，一一风荷举」，
   王国维「真能得荷之神理」）；末境点击——宿雨滚落、风荷次第挺举，轻舟梦入芙蓉浦 ================= */

/* —— 博山炉：三足香炉（合批 1 mesh，沉香所燎之器） —— */
function makeCenserSMZ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, bodyC=o.color===undefined?0x4c5a50:o.color;
  const B=new GeoBag();
  const prof=[[0.17,0.0],[0.36,0.05],[0.42,0.20],[0.37,0.44],[0.30,0.58]].map(function(p){return new THREE.Vector2(p[0],p[1]);});
  const bowl=new THREE.LatheGeometry(prof,14); B.put(bowl,bodyC);
  const lid=new THREE.SphereGeometry(0.30,12,8,0,Math.PI*2,0,Math.PI/2); lid.scale(1,0.72,1); lid.translate(0,0.60,0);
  B.put(lid,shadeColor(bodyC,1.15));
  const knob=new THREE.SphereGeometry(0.075,8,6); knob.translate(0,0.86,0); B.put(knob,shadeColor(bodyC,1.3));
  for(let i=0;i<3;i++){
    const a=i/3*Math.PI*2+0.5;
    const leg=new THREE.CylinderGeometry(0.045,0.06,0.22,6);
    leg.rotateZ(0.28); leg.translate(Math.sin(a)*0.22,0.09,Math.cos(a)*0.22); B.put(leg,shadeColor(bodyC,0.8));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:36,
    specular:0x8fb8a8,emissive:0x0c1410}),{c:o.rimC===undefined?0x95c9c0:o.rimC,i:0.38,p:2.6}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return {g};
}
/* —— 雀：檐间小鸟（合批 1 mesh，呼晴时挺颈振翅） —— */
function makeSparrowSMZ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0x2e2820:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.20,8,6); body.scale(1.45,0.85,0.8); body.translate(0,0.20,0); B.put(body,c);
  const head=new THREE.SphereGeometry(0.115,8,6); head.translate(0.32,0.38,0); B.put(head,shadeColor(c,1.2));
  const beak=new THREE.ConeGeometry(0.035,0.15,5); beak.rotateZ(-Math.PI/2); beak.translate(0.48,0.36,0); B.put(beak,0x6a5638);
  const tail=new THREE.ConeGeometry(0.07,0.38,5); tail.rotateZ(Math.PI/2.35); tail.translate(-0.34,0.26,0); B.put(tail,shadeColor(c,0.85));
  [1,-1].forEach(function(sd){
    const wg=new THREE.SphereGeometry(0.13,6,5); wg.scale(0.6,0.16,1.25); wg.translate(-0.02,0.24,0.16*sd);
    B.put(wg,shadeColor(c,1.08));
  });
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,emissive:0x060805}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  g.update=function(t,fk){
    const k=fk===undefined?1:fk, ph=g.userData.ph||0;
    g.rotation.z=0.05*Math.sin(t*1.3+ph);
    g.scale.set(s,s*(1+0.10*Math.max(0,Math.sin(t*1.3+ph))*k),s);   // 呼晴挺颈（乘 fadeK）
  };
  return {g,update:g.update};
}
/* —— 屋檐一角：双柱+檐枋+坡瓦檐+瓦当（合批 2 mesh，燎香消暑的居室一角） —— */
function makeEavesSMZ(o){
  o=o||{};
  const w=o.w===undefined?7.6:o.w, h=o.h===undefined?4.8:o.h;
  const wood=o.wood===undefined?0x241a12:o.wood, roofC=o.roof===undefined?0x1e2a22:o.roof;
  const W=new GeoBag();
  [1,-1].forEach(function(sd){
    const col=new THREE.CylinderGeometry(0.22,0.26,h,8); col.translate(sd*w/2,h/2,0); W.put(col,shadeColor(wood,1.0));
    const bs=new THREE.BoxGeometry(0.85,0.42,0.85); bs.translate(sd*w/2,0.21,0); W.put(bs,shadeColor(0x3c4038,1.0));
  });
  const beam=new THREE.BoxGeometry(w+1.2,0.46,0.72); beam.translate(0,h-0.25,0.30); W.put(beam,shadeColor(wood,1.22));
  const lintel=new THREE.BoxGeometry(w+0.6,0.30,0.4); lintel.translate(0,h-0.95,0.18); W.put(lintel,shadeColor(wood,0.8));
  const woodM=W.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3a30,emissive:0x0a0806}),{c:o.rimC===undefined?0xc8b490:o.rimC,i:0.28,p:2.4}));
  const R=new GeoBag();
  const slab=new THREE.BoxGeometry(w+2.6,0.34,3.6); slab.rotateX(-0.10); slab.translate(0,h+0.55,0.55); R.put(slab,shadeColor(roofC,1.0));
  const ridge=new THREE.BoxGeometry(w+3.0,0.26,0.9); ridge.translate(0,h+1.0,-0.5); R.put(ridge,shadeColor(roofC,1.25));
  [1,-1].forEach(function(sd){
    const tip=new THREE.BoxGeometry(1.7,0.24,1.0); tip.rotateZ(sd*0.32); tip.translate(sd*(w/2+0.9),h+0.85,0.85);
    R.put(tip,shadeColor(roofC,1.1));
  });
  for(let i=0;i<=10;i++){
    const t=new THREE.CylinderGeometry(0.13,0.10,0.16,7); t.rotateX(Math.PI/2);
    t.translate(-w/2-0.6+(w+1.2)*(i/10),h+0.36,2.1); R.put(t,shadeColor(roofC,1.5));
  }
  const roofM=R.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a5a50,emissive:0x080c0a}),{c:o.rimC===undefined?0x95c9c0:o.rimC,i:0.22,p:2.6}));
  const g=new THREE.Group(); g.add(woodM,roofM);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}
/* —— 荷叶：叶柄挺立 + 清圆叶面（中心微凹、边缘上卷，承光承露）+ 叶心宿雨珠 ——
   返回 {g,blade,stemM,drop}：blade 可俯仰（垂→举），stem 以根部为轴伸缩（挺举） —— */
function makeLotusSMZ(o){
  o=o||{};
  const h=o.h===undefined?2.0:o.h, r=o.r===undefined?1.5:o.r;
  const stemC=o.stem===undefined?0x2c5a34:o.stem, leafC=o.leaf===undefined?0x3f7a44:o.leaf;
  const g=new THREE.Group();
  const stemG=new THREE.CylinderGeometry(0.05,0.075,h,7); stemG.translate(0,h/2,0);
  const stemM=new THREE.Mesh(stemG,new THREE.MeshPhongMaterial({color:stemC,shininess:12,
    specular:0x3a5a44,emissive:0x08140a}));
  g.add(stemM);
  const prof=[[0.02,0.16],[0.22,0.08],[0.50,0.03],[0.80,0.09],[1.0,0.28]].map(function(p){
    return new THREE.Vector2(p[0]*r,p[1]*r);});
  const bladeG=new THREE.Group(); bladeG.position.y=h;
  const blade=new THREE.Mesh(new THREE.LatheGeometry(prof,o.seg===undefined?22:o.seg),
    rimHook(new THREE.MeshPhongMaterial({color:leafC,shininess:30,specular:0xa8d8c0,
      emissive:0x0a1c10,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xbfe8cc:o.rimC,i:0.36,p:2.6}));
  bladeG.add(blade); g.add(bladeG);
  let drop=null;
  if(o.drop!==false){
    drop=new THREE.Mesh(new THREE.SphereGeometry(0.095,10,8),
      new THREE.MeshPhongMaterial({color:0xc8e8e0,shininess:140,specular:0xffffff,
        emissive:0x0e2220,transparent:true,opacity:0.8}));
    drop.position.set(0,0.20,0); bladeG.add(drop);
  }
  return {g,blade:bladeG,stemM:stemM,drop:drop,h:h,r:r};
}
/* —— 远景荷荡：荷叶 InstancedMesh（1 draw call 一片荷）+ 远荷花苞 InstancedMesh —— */
function makeLotusFieldSMZ(o){
  o=o||{};
  const n=o.n===undefined?42:o.n, R=seedRnd(o.seed===undefined?17:o.seed);
  const rect=o.rect||[-75,8,150,70], y=o.y===undefined?0.22:o.y;
  const prof=[[0.02,0.14],[0.3,0.06],[0.65,0.02],[1.0,0.20]].map(function(p){return new THREE.Vector2(p[0],p[1]);});
  const leafG=new THREE.LatheGeometry(prof,10);   // 远景叶平摊水面
  const leafM=new THREE.InstancedMesh(leafG,new THREE.MeshPhongMaterial({color:o.color===undefined?0x33653c:o.color,
    shininess:18,specular:0x6aa888,emissive:0x08160c,side:THREE.DoubleSide}),n);
  const dm=new THREE.Object3D();
  for(let i=0;i<n;i++){
    dm.position.set(rect[0]+R()*rect[2],y+R()*0.12,rect[1]-R()*rect[3]);
    dm.rotation.set(0,R()*6.283,(R()-0.5)*0.2);
    dm.scale.setScalar(0.5+R()*1.1); dm.updateMatrix(); leafM.setMatrixAt(i,dm.matrix);
  }
  leafM.frustumCulled=false;
  const g=new THREE.Group(); g.add(leafM);
  const nf=o.flowers===undefined?12:o.flowers;
  if(nf>0){
    const petG=new THREE.ConeGeometry(0.34,0.85,7); petG.translate(0,0.42,0);
    const floM=new THREE.InstancedMesh(petG,new THREE.MeshPhongMaterial({color:0xe0bcc8,shininess:20,
      specular:0xe8d8dc,emissive:0x302028}),nf);
    for(let i=0;i<nf;i++){
      dm.position.set(rect[0]+R()*rect[2],y+0.35+R()*0.5,rect[1]-R()*rect[3]);
      dm.rotation.set((R()-0.5)*0.3,R()*6.283,(R()-0.5)*0.3);
      dm.scale.setScalar(0.55+R()*0.7); dm.updateMatrix(); floM.setMatrixAt(i,dm.matrix);
    }
    floM.frustumCulled=false; g.add(floM);
  }
  return {g};
}
/* —— 荷花：九瓣有体积的锥瓣 + 内芯（合批 1 mesh，芙蓉浦的主角，任何角度不呈三角片） —— */
function makeFlowerSMZ(o){
  o=o||{};
  const h=o.h===undefined?2.2:o.h, s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const stemG=new THREE.CylinderGeometry(0.045,0.07,h,7); stemG.translate(0,h/2,0);
  const stem=new THREE.Mesh(stemG,new THREE.MeshPhongMaterial({color:0x2c5a34,shininess:12,emissive:0x08140a}));
  g.add(stem);
  const B=new GeoBag();
  for(let i=0;i<9;i++){
    const a=i/9*Math.PI*2;
    const pet=new THREE.ConeGeometry(0.20,0.92,6);
    pet.translate(0,0.46,0); pet.rotateX(0.68); pet.rotateY(a);
    pet.translate(Math.sin(a)*0.22,h,Math.cos(a)*0.22);
    B.put(pet,0xe4c2ce);
  }
  for(let i=0;i<6;i++){
    const a=i/6*Math.PI*2+0.5;
    const pet=new THREE.ConeGeometry(0.15,0.62,6);
    pet.translate(0,0.31,0); pet.rotateX(0.30); pet.rotateY(a);
    pet.translate(Math.sin(a)*0.08,h+0.10,Math.cos(a)*0.08);
    B.put(pet,0xeed4dc);
  }
  const core=new THREE.SphereGeometry(0.14,8,6); core.translate(0,h+0.24,0); B.put(core,0xd8e8b0);
  const flo=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,
    specular:0xe8d8dc,emissive:0x241418}));
  g.add(flo); g.scale.setScalar(s);
  g.update=function(t){ g.rotation.z=0.04*Math.sin(t*0.7+h); };
  return {g,update:g.update};
}
/* —— 轻舟：舟身+翘首+坐板+短楫（合批 1 mesh，梦入芙蓉浦的梦之舟） —— */
function makeBoatSMZ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, wood=o.wood===undefined?0x3a2c1c:o.wood;
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(1.7,0.5,6.4); hull.translate(0,0.30,0); B.put(hull,shadeColor(wood,1.0));
  [1,-1].forEach(function(sd){
    const bow=new THREE.BoxGeometry(1.5,0.34,1.7); bow.rotateX(-0.30); bow.translate(0,0.52,-3.6);
    B.put(bow,shadeColor(wood,1.15));
    const strake=new THREE.BoxGeometry(0.16,0.22,6.2); strake.translate(sd*0.86,0.62,0);
    B.put(strake,shadeColor(wood,1.3));
  });
  const seat=new THREE.BoxGeometry(1.5,0.10,0.7); seat.translate(0,0.62,0.4); B.put(seat,shadeColor(wood,0.9));
  const oar=new THREE.CylinderGeometry(0.045,0.045,3.0,6); oar.rotateZ(0.9); oar.rotateY(0.35);
  oar.translate(0.95,0.45,-2.0); B.put(oar,shadeColor(0x6a5638,1.0));   // 楫随渔郎在船头
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a4438,emissive:0x0a0806}),{c:o.rimC===undefined?0xb8d0b0:o.rimC,i:0.3,p:2.5}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return {g};
}
/* —— 市井屋脊群：北宋汴京的屋顶海（合批 1 mesh，久客长安的中景） —— */
function makeRoofsSMZ(o){
  o=o||{};
  const n=o.n===undefined?8:o.n, R=seedRnd(o.seed===undefined?31:o.seed);
  const B=new GeoBag(), bodyC=o.body===undefined?0x1a2620:o.body, roofC=o.roof===undefined?0x222e26:o.roof;
  for(let i=0;i<n;i++){
    const w=4+R()*5, d=3.5+R()*3, h=1.6+R()*1.8;
    const x=(R()-0.5)*(o.spread===undefined?70:o.spread), z=-(14+R()*30);
    const bd=new THREE.BoxGeometry(w,h,d); bd.translate(x,h/2,z); B.put(bd,shadeColor(bodyC,0.85+R()*0.3));
    const rf=new THREE.ConeGeometry(Math.max(w,d)*0.78,1.4+R()*0.8,4); rf.rotateY(Math.PI/4);
    rf.scale(1,1,d/Math.max(w,d)); rf.translate(x,h+0.7,z); B.put(rf,shadeColor(roofC,0.9+R()*0.3));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3a32,emissive:0x060a08}),{c:o.rimC===undefined?0x95c9c0:o.rimC,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}
/* —— 城垣角楼：高台+楼身+双层四阿顶（合批 1 mesh，客居之地的剪影） —— */
function makeWatchtowerSMZ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0x18241e:o.color;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(16,6,12); base.translate(0,3,0); B.put(base,shadeColor(c,0.9));
  const wall=new THREE.BoxGeometry(70,4.5,6); wall.translate(-34,2.25,2); B.put(wall,shadeColor(c,0.8));
  for(let i=0;i<12;i++){
    const m=new THREE.BoxGeometry(2.6,1.3,1.2); m.translate(-64+i*5.6,5.1,2); B.put(m,shadeColor(c,1.0));
  }
  const body=new THREE.BoxGeometry(9,5.5,8); body.translate(0,8.7,0); B.put(body,shadeColor(c,1.05));
  const rf1=new THREE.ConeGeometry(7.6,2.4,4); rf1.rotateY(Math.PI/4); rf1.translate(0,12.6,0); B.put(rf1,shadeColor(c,1.2));
  const rf2=new THREE.ConeGeometry(5.6,2.0,4); rf2.rotateY(Math.PI/4); rf2.translate(0,14.6,0); B.put(rf2,shadeColor(c,1.3));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3a32,emissive:0x050806}),{c:o.rimC===undefined?0x95c9c0:o.rimC,i:0.20,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return {g};
}
/* —— 南飞雀群：一行小雀掠过城头（合批 1 mesh，缓缓横渡） —— */
function makeFlockSMZ(o){
  o=o||{};
  const n=o.n===undefined?5:o.n, R=seedRnd(o.seed===undefined?7:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*16, y=(R()-0.5)*3.5, z=(R()-0.5)*5;
    [1,-1].forEach(function(sd){
      const wg=new THREE.PlaneGeometry(1.1,0.34);
      wg.rotateZ(sd*0.28); wg.rotateY(sd*0.2); wg.translate(x+sd*0.5,y+0.06*sd,z);
      B.put(wg,0x121c16);
    });
    const bd=new THREE.SphereGeometry(0.16,6,5); bd.scale(1.5,0.8,0.8); bd.translate(x,y,z); B.put(bd,0x121c16);
  }
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    emissive:0x050806,side:THREE.DoubleSide}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

function bCover(){ // 卷首 · 荷塘晓色 —— 雨后初晴的黎明，荷荡尽处一角屋檐，晨雾未散
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0a1710,c2:0x152619,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:3,peaks:5,seed:57,color:0x0b1911,atmo:0x2a443c,fogK:0.62,glowK:0.05,glow:0xa8ccb0,y:-10});
  ridge.g.position.set(0,0,-80); g.add(ridge.g);
  /* 荷荡水光：一带水面绕山脚 */
  const water=makeWater({size:14,seg:20,amp:0.09,freq:0.15,speed:0.45,flow:[0.1,0.5],spec:1.1,
    deep:0x0a1a12,shallow:0x1d4a36,skyc:0x2c584a,moonDir:[-60,90,-160],y:-1.5});
  water.mesh.scale.set(1,1,13); water.mesh.rotation.y=Math.PI/2;
  water.mesh.position.set(4,-1.5,-30); g.add(water.mesh);
  /* 近岸荷荡（封面预告词眼） */
  const field=makeLotusFieldSMZ({n:46,flowers:14,rect:[-70,6,140,42],seed:23});
  field.g.position.set(0,-1.5,-14); g.add(field.g);
  /* 尽处一角屋檐 + 堤上游人一痕 */
  const eaves=makeEavesSMZ({scale:1.0}); eaves.g.position.set(-24,-1.6,-40); eaves.g.rotation.y=0.6; g.add(eaves.g);
  const crowd=makeCrowd({n:4,rect:[6,-30,22,8],seed:67,color:0x14201a,rimC:0x8fb8a0,rim:0.2});
  g.add(crowd.mesh);
  /* 黎明第一缕光（青绿底上唯一的暖） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,58,1); dawn.position.set(-58,24,-120); dawn.renderOrder=-7; g.add(dawn);
  const motes=makeGlow({n:44,box:[190,28,110],pos:[0,9,-26],color:0xcfe4d0,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[250,32,140],pos:[0,10,-52],scale:80,color:0x1e382a,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:52,n:9,d:7,color:0x081009,seed:19,sway:0.7,rim:0.12,rimC:0x95c9c0});
  brL.g.position.set(-27,-1.6,40); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const brR=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:21,rim:0.14,rimC:0x95c9c0});
  brR.g.position.set(17,-1.4,14); g.add(brR.g);
  /* 堤上远望的词人 */
  const poet=makeFigure({pose:'独立',robe:0x2a352c,belt:0x8f6a33,hat:'幞头',scale:0.9,rim:0.4,rimC:0xbfe0cc,noProp:true});
  poet.position.set(9,-1.6,-20); poet.rotation.y=2.3; g.add(poet);
  addLights(g,{c:0xe8d8a8,i:0.46,p:[-50,80,30]},{c:0x223426,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    brL.update(t,k); brR.update(t,k); crowd.update(t); poet.update(t,k);
    dawn.material.opacity=k*(0.12+0.03*Math.sin(t*0.4));
  }};
}
function bLiaoXiang(){ // 一 · 燎香消暑 —— 燎沉香消溽暑，鸟雀呼晴侵晓窥檐语
  const g=new THREE.Group();
  const ctl={birds:[]};
  const grd=makeGround({r:200,c1:0x0b150f,c2:0x1a2c1e,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:220,h:36,layers:3,peaks:5,seed:71,color:0x09150e,atmo:0x2a4438,
    fogK:0.62,glowK:0.04,glow:0xa8ccb0,y:-6});
  ridge.g.position.set(0,0,-85); g.add(ridge.g);
  /* 屋檐一角（画面左后，檐下焚香人、檐上双雀） */
  const eaves=makeEavesSMZ({scale:1.05}); eaves.g.position.set(-6.0,0,-8.5); eaves.g.rotation.y=0.55; g.add(eaves.g);
  /* 檐上双雀：呼晴窥语 */
  const sp1=makeSparrowSMZ({scale:1.2}); sp1.g.position.set(-5.4,4.95,-6.3); sp1.g.userData.y0=sp1.g.position.y; sp1.g.userData.ph=0; sp1.g.rotation.y=0.7;
  const sp2=makeSparrowSMZ({scale:1.0}); sp2.g.position.set(-3.7,4.95,-5.5); sp2.g.userData.y0=sp2.g.position.y; sp2.g.userData.ph=2.1; sp2.g.rotation.y=-0.4;
  g.add(sp1.g,sp2.g); ctl.birds=[sp1,sp2];
  /* 檐下词人：焚香人立 */
  const poet=makeFigure({pose:'独立',robe:0x2a352c,belt:0x8f6a33,hat:'幞头',scale:1.12,rim:0.5,rimC:0xcfe8da,noProp:true});
  poet.position.set(-4.0,0,-5.0); poet.rotation.y=0.55; g.add(poet);
  /* 石案 + 博山炉 + 沉香青烟（画面右前的暖点） */
  const tbl=makeTable({w:2.8,d:1.7,h:1.05,wood:0x4a463c}); tbl.g.position.set(3.4,0,2.6); tbl.g.rotation.y=-0.3; g.add(tbl.g);
  const censer=makeCenserSMZ({scale:1.1}); censer.g.position.set(3.4,1.05,2.6); g.add(censer.g);
  const smokeA=makeGlow({n:24,box:[1.7,7.5,1.7],pos:[3.4,2.3,2.6],color:0xcfe4da,size:7.5,speed:0.025,rise:1,add:false,maxA:0.28});
  const smokeB=makeGlow({n:13,box:[1.1,8.5,1.1],pos:[3.4,2.3,2.6],color:0xe8f4ec,size:4.5,speed:0.035,rise:1,add:false,maxA:0.20});
  g.add(smokeA.points,smokeB.points);
  /* 宿雨初收：阶前一泓积水映天光 */
  const puddle=makeWater({size:22,seg:14,amp:0.05,freq:0.2,speed:0.4,flow:[0.04,0.2],spec:1.8,
    deep:0x0c1a14,shallow:0x2c5846,skyc:0x4a705c,moonDir:[40,70,-60],y:0.05});
  puddle.mesh.position.set(3.0,0.03,7.0); g.add(puddle.mesh);
  /* 庭中宿雨初干的地气 + 晨雾 */
  const motes=makeGlow({n:30,box:[130,20,70],pos:[0,7,-14],color:0xcfe4d0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,110],pos:[0,8,-40],scale:74,color:0x1e382a,op:0.11});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:14,n:6,d:5,color:0x070f08,seed:41,sway:0.9,rim:0.12,rimC:0x95c9c0});
  brL.g.position.set(-13,-0.6,10); brL.g.scale.setScalar(1.1); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x060b07,seed:43,rim:0.12,rimC:0x95c9c0});
  rk.g.position.set(11,-1.0,8); g.add(rk.g);
  addLights(g,{c:0xd8c8a0,i:0.44,p:[30,70,40]},{c:0x1e2c22,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      brL.update(t,k); rk.update(t,k); poet.update(t,k);
      smokeA.update(t); smokeB.update(t);
      puddle.update(t);
      for(let i=0;i<ctl.birds.length;i++)ctl.birds[i].update(t,k);
    },onEnter(){   // 雀语呼晴：檐头两声啁啾
      pluck(4,0.15,0.10); pluck(5,0.55,0.09); pluck(3,1.05,0.08);
    }};
}
function bFengHe(){ // 二 · 风荷并举（词眼境）—— 叶上初阳干宿雨，水面清圆，一一风荷举
  const g=new THREE.Group();
  const ctl={leaves:[]};
  const grd=makeGround({r:210,c1:0x091309,c2:0x142316,y:-0.6}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:34,layers:3,peaks:4,seed:81,color:0x0a1710,atmo:0x2a443c,
    fogK:0.61,glowK:0.05,glow:0xa8ccb0,y:-8});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  /* 水面清圆：整面荷塘水 */
  const water=makeWater({size:150,seg:30,amp:0.10,freq:0.15,speed:0.5,flow:[0.08,0.5],spec:1.25,
    deep:0x0a1a12,shallow:0x1d4a36,skyc:0x2c584a,moonDir:[50,80,-120],y:0.02});
  g.add(water.mesh);
  /* 风荷并举：六柄主荷次第挺出（初阳干宿雨 → 一一风荷举），一一错峰 */
  const defs=[[-5.5,1.9,-1.2,1.55],[-1.5,2.5,0.8,1.75],[2.8,2.1,-0.5,1.6],[6.2,1.7,1.5,1.4],[-8.5,1.6,2.2,1.3],[0.8,1.5,3.4,1.25]];
  for(let i=0;i<defs.length;i++){
    const d=defs[i];
    const lf=makeLotusSMZ({h:d[1],r:d[3],seed:101+i*7,leaf:shadeColor(0x3f7a44,0.9+0.14*(i%3))});
    lf.g.position.set(d[0],0,d[2]);
    lf.g.rotation.y=i*1.13;
    lf.blade.rotation.x=0.55;                 // 初始垂叶承雨
    lf.stemM.scale.y=0.78;
    lf.t0=2.2+i*1.05; lf.ph=i*2.1; lf.d0=3.0+i*1.05;
    g.add(lf.g); ctl.leaves.push(lf);
  }
  /* 远景荷荡 + 近处两枝荷花 */
  const field=makeLotusFieldSMZ({n:44,flowers:12,rect:[-75,4,150,60],seed:23});
  g.add(field.g);
  const flo=makeFlowerSMZ({h:2.3,scale:1.0}); flo.g.position.set(7.6,0,3.6); g.add(flo.g);
  const flo2=makeFlowerSMZ({h:1.8,scale:0.9}); flo2.g.position.set(-3.2,0,1.2); g.add(flo2.g);
  /* 凭岸望荷的词人 */
  const poet=makeFigure({pose:'独立',robe:0x2a352c,belt:0x8f6a33,hat:'幞头',scale:1.05,rim:0.5,rimC:0xcfe8da,noProp:true});
  poet.position.set(-11.0,0,3.0); poet.rotation.y=2.1; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:1.8,w:7,d:4,color:0x0a120c,seed:61,rim:0.16,rimC:0x95c9c0});
  rock.g.position.set(-11.0,-0.6,1.8); g.add(rock.g);
  /* 初阳：东天低日，暖金是青绿底上唯一的暖 */
  const sun=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf0d898,
    transparent:true,opacity:0.42,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sun.scale.set(90,36,1); sun.position.set(78,12,-95); sun.renderOrder=-7; g.add(sun);
  const motes=makeGlow({n:36,box:[150,20,80],pos:[0,6,-12],color:0xe8dce0,size:6,speed:0.03,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,22,110],pos:[0,7,-46],scale:76,color:0x1e382a,op:0.10});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:10,n:8,d:5,color:0x071009,seed:63,sway:1.2,tip:0x2c4a2c});
  reed.g.position.set(7,-0.8,8.5); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x060b07,seed:65,rim:0.12,rimC:0x95c9c0});
  rk.g.position.set(-9.0,-0.9,4.0); g.add(rk.g);
  addLights(g,{c:0xe8d8a0,i:0.52,p:[60,50,20]},{c:0x1e2e22,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      reed.update(t,k); rk.update(t,k); poet.update(t,k); flo.update(t); flo2.update(t);
      sun.material.opacity=k*(0.30+0.08*Math.sin(t*0.35));
      /* 一一风荷举：垂叶次第挺出，宿雨随初阳晒干（公式峰值 ≤ 初值，乘 fadeK） */
      for(let i=0;i<ctl.leaves.length;i++){
        const lf=ctl.leaves[i];
        const s=Math.max(0,Math.min(1,(t-lf.t0)/2.4)), e=s*s*(3-2*s);
        lf.blade.rotation.x=0.55*(1-e)+0.03*Math.sin(t*0.8+lf.ph)*e;
        lf.blade.rotation.z=0.04*Math.sin(t*0.6+lf.ph*2)*e;
        const st=0.78+0.22*e;
        lf.stemM.scale.y=st;
        if(lf.drop&&lf.drop.visible){
          const dry=Math.max(0,Math.min(1,(t-lf.d0)/4.0));
          lf.drop.scale.setScalar(Math.max(0.001,1-dry));
          if(dry>=1)lf.drop.visible=false;
        }
      }
    },onEnter(){ pluck(2,0.2,0.08); pluck(4,0.8,0.07); }};
}
function bChangAn(){ // 三 · 久客长安 —— 家住吴门久作长安旅，五月渔郎相忆否
  const g=new THREE.Group();
  const ctl={flock:null};
  const grd=makeGround({r:220,c1:0x0c120e,c2:0x18201a,y:-2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:40,layers:2,peaks:4,seed:91,color:0x0a130e,atmo:0x2a4038,
    fogK:0.60,glowK:0.04,glow:0x9ab8a0,y:-10});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 城垣角楼 + 市井屋脊海（客居之地） */
  const tower=makeWatchtowerSMZ({scale:1.0}); tower.g.position.set(-6,0,-58); g.add(tower.g);
  const roofs=makeRoofsSMZ({n:9,spread:80,seed:31,body:0x1e2b24,roof:0x27342b}); g.add(roofs.g);
  /* 街市人影 */
  const crowd=makeCrowd({n:8,rect:[-32,-4,52,12],seed:77,color:0x131c16,rimC:0x8fb8a0,rim:0.2});
  g.add(crowd.mesh);
  /* 街市的一点暖黄灯火（客居之地唯一的暖） */
  const lamps=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8c890,
    transparent:true,opacity:0.18,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  lamps.scale.set(34,12,1); lamps.position.set(-8,2.5,-24); lamps.renderOrder=-5; g.add(lamps);
  /* 凭栏高台：词人客居的酒楼层台 */
  const deck=new THREE.Mesh(new THREE.BoxGeometry(38,0.8,22),
    new THREE.MeshPhongMaterial({color:0x1c2420,shininess:6,emissive:0x070a08}));
  deck.position.set(0,7.05,8); g.add(deck);
  const poet=makeFigure({pose:'独立',robe:0x2a352c,belt:0x8f6a33,hat:'幞头',beard:true,scale:1.02,rim:0.5,rimC:0xcfe8da,noProp:true});
  poet.position.set(-4.2,7.45,12.6); poet.rotation.y=2.75; g.add(poet);
  /* 五月晚风中的南飞雀群 */
  const flock=makeFlockSMZ({n:5,seed:9}); flock.g.position.set(-30,16,-40); g.add(flock.g); ctl.flock=flock;
  /* 远村方向的一点暮光（吴门在南方） */
  const south=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8c890,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  south.scale.set(110,40,1); south.position.set(-20,14,-110); south.renderOrder=-7; g.add(south);
  const motes=makeGlow({n:30,box:[150,22,80],pos:[0,12,-10],color:0xcfe0c8,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,26,110],pos:[0,8,-52],scale:76,color:0x1c3026,op:0.11});
  g.add(mist.g);
  const rail=makeForeground({kind:'栏杆',w:32,h:1.6,color:0x1a231d,seed:93,rim:0.20,rimC:0x95c9c0});
  rail.g.position.set(0,7.45,16.8); g.add(rail.g);
  const br=makeForeground({kind:'树枝',w:10,n:4,d:6,color:0x070f08,seed:95,sway:0.8,rim:0.12,rimC:0x95c9c0});
  br.g.position.set(16,6.0,6); g.add(br.g);
  addLights(g,{c:0xd8c8a0,i:0.40,p:[-40,60,20]},{c:0x1e2a22,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      rail.update(t,k); br.update(t,k); poet.update(t,k); crowd.update(t);
      south.material.opacity=k*(0.22+0.06*Math.sin(t*0.3));
      lamps.material.opacity=k*(0.12+0.05*Math.sin(t*0.5+1));
      if(ctl.flock){ ctl.flock.g.position.x+=dt*1.1; if(ctl.flock.g.position.x>70)ctl.flock.g.position.x=-80;
        ctl.flock.g.position.y=16+0.5*Math.sin(t*0.5); }
    },onEnter(){ pluck(1,0.3,0.09); pluck(0,1.1,0.08); }};
}
function bMengPu(){ // 四（末境·可点击）· 梦入芙蓉浦 —— 小楫轻舟梦入芙蓉浦；点击：宿雨滚落+风荷次第挺举+轻舟入荷荡
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickAt:-1,pulse:0,boatZ0:4,leaves:[],drops:[]};
  const grd=makeGround({r:220,c1:0x0a140e,c2:0x152417,y:-0.8}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:32,layers:2,peaks:4,seed:111,color:0x0a1810,atmo:0x2c4a40,
    fogK:0.60,glowK:0.06,glow:0xa8ccb0,y:-9});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 梦之水：比白昼更幽的青 */
  const water=makeWater({size:160,seg:30,amp:0.09,freq:0.14,speed:0.4,flow:[0.06,0.4],spec:1.3,
    deep:0x081710,shallow:0x1a4636,skyc:0x2a564a,moonDir:[-40,90,-120],y:0.02});
  g.add(water.mesh);
  /* 荷荡水巷：八柄主荷夹道（初态垂叶承雨，点击后次第挺举） */
  const defs=[[-4.6,2.0,-2.5,1.6],[-7.2,1.7,-6.5,1.45],[4.4,2.3,-4.0,1.7],[7.4,1.8,-9.0,1.5],
              [-5.8,2.4,-12.0,1.7],[5.6,2.0,-14.5,1.55],[-8.8,1.6,-18.0,1.4],[-3.4,1.6,3.2,1.15]];
  for(let i=0;i<defs.length;i++){
    const d=defs[i];
    const lf=makeLotusSMZ({h:d[1],r:d[3],seed:201+i*11,leaf:shadeColor(0x3a7244,0.9+0.14*(i%3))});
    lf.g.position.set(d[0],0,d[2]); lf.g.rotation.y=i*1.31;
    lf.blade.rotation.x=0.5;
    lf.stemM.scale.y=0.8;
    lf.i=i; g.add(lf.g); ctl.leaves.push(lf);
    if(lf.drop)ctl.drops.push(lf.drop);
  }
  /* 远景荷荡 + 荷花三枝夹道 */
  const field=makeLotusFieldSMZ({n:46,flowers:14,rect:[-80,2,160,66],seed:53});
  g.add(field.g);
  const fl1=makeFlowerSMZ({h:2.4,scale:1.05}); fl1.g.position.set(-6.2,0,-8.6); g.add(fl1.g);
  const fl2=makeFlowerSMZ({h:2.1,scale:0.95}); fl2.g.position.set(6.4,0,-11.5); g.add(fl2.g);
  const fl3=makeFlowerSMZ({h:2.5,scale:1.1}); fl3.g.position.set(-7.6,0,-19.0); g.add(fl3.g);
  /* 小楫轻舟 + 船头摇楫的渔郎（船头不在镜头与荷巷之间，画面留给荷） */
  const boat=makeBoatSMZ({scale:1.0});
  boat.g.position.set(0.5,0,ctl.boatZ0); g.add(boat.g);
  const fisher=makeFigure({pose:'独立',robe:0x2c3830,belt:0x6a5638,hat:'发髻',scale:0.8,rim:0.46,rimC:0xcfe8da,noProp:true});
  fisher.position.set(0.35,0.42,-2.9); fisher.rotation.y=Math.PI; boat.g.add(fisher);
  /* 梦境化转场：芙蓉色天光（点击后渐亮＝梦入深处） */
  const dream=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8c0d0,
    transparent:true,opacity:0.48,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dream.scale.set(170,60,1); dream.position.set(0,16,-90); dream.renderOrder=-7; g.add(dream);
  const motes=makeGlow({n:38,box:[160,18,90],pos:[0,5,-14],color:0xd8c8d4,size:6,speed:0.035,rise:0.2,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,24,120],pos:[0,7,-50],scale:80,color:0x24382e,op:0.14});
  g.add(mist.g);
  const rdL=makeForeground({kind:'芦苇',w:8,n:7,d:5,color:0x071009,seed:121,sway:1.4,tip:0x2c4a34});
  rdL.g.position.set(-6.5,-0.8,4.5); g.add(rdL.g);
  const rdR=makeForeground({kind:'芦苇',w:8,n:7,d:5,color:0x071009,seed:123,sway:1.4,tip:0x2c4a34});
  rdR.g.position.set(7,-0.8,4); g.add(rdR.g);
  addLights(g,{c:0xc8d8c0,i:0.40,p:[-30,60,20]},{c:0x20302a,i:0.66});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt; ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      let w=0, dtc=-1;
      if(ctl.clicked){
        w=Math.min(1,(ctl.t-ctl.clickAt)/3.0); w=w*w*(3-2*w);
        dtc=ctl.t-ctl.clickAt;
      }
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      rdL.update(t,k); rdR.update(t,k); fisher.update(t,k);
      /* 风荷次第挺举 + 宿雨滚落（点击后按序触发；乘 fadeK 的每帧写不越 base） */
      for(let i=0;i<ctl.leaves.length;i++){
        const lf=ctl.leaves[i];
        let e=0;
        if(dtc>=0){
          e=Math.max(0,Math.min(1,(dtc-0.3-lf.i*0.45)/2.0));
          e=e*e*(3-2*e);
        }
        lf.blade.rotation.x=(0.5)*(1-e)+0.03*Math.sin(t*0.8+lf.i*2.1)*e;
        lf.blade.rotation.z=0.04*Math.sin(t*0.6+lf.i*1.7)*e;
        lf.stemM.scale.y=0.8+0.2*e;
        const dr=lf.drop;
        if(dr&&dr.visible){
          if(dtc>=0){
            const roll=Math.max(0,Math.min(1,(dtc-lf.i*0.45)/0.8));
            const fall=Math.max(0,Math.min(1,(dtc-lf.i*0.45-0.8)/0.7));
            dr.position.x=roll*0.85*lf.r*0.6;
            dr.position.y=0.20+roll*0.05-fall*fall*(lf.h+0.5);
            dr.material.opacity=k*0.8*(1-fall);
            if(fall>=1)dr.visible=false;
          }else{
            dr.position.x=0.03*Math.sin(t*1.1+lf.i);
            dr.material.opacity=k*0.8;
          }
        }
      }
      /* 轻舟：入梦前轻晃，点击后摇入荷荡深处 */
      boat.g.position.y=0.08*Math.sin(t*0.9);
      boat.g.rotation.z=0.03*Math.sin(t*0.7);
      if(ctl.clicked){
        boat.g.position.z=ctl.boatZ0-8.5*w-((ctl.t-ctl.clickAt)>3? (ctl.t-ctl.clickAt-3)*1.2:0);
        boat.g.position.x=0.5+0.5*Math.sin(t*0.5)*w;
      }
      fl1.update(t); fl2.update(t); fl3.update(t);
      /* 芙蓉色天光：点击后渐亮 + 脉冲（公式峰值 0.44 ≤ 初值 0.48，乘 fadeK） */
      dream.material.opacity=k*(0.10+0.28*w+0.06*ctl.pulse);
    },click(){
      if(ctl.t<1.6)return;                     // 冷却：入境未稳不触发
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickAt=ctl.t;
        pluck(0,0,0.14); pluck(2,0.4,0.11); pluck(4,0.9,0.10); pluck(5,1.5,0.08);
        const fl=$('#flash'); fl.textContent='小楫轻舟，梦入芙蓉浦'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                             // 可反复点：梦色再涨一拍
    },clicked:false};
  return api;
}
