/* ================= 游子吟 · 三境场景（宣纸暖烛：浅宣纸底 + 赭墨剪影 + 暖烛光点题） ================= */

/* 油灯：灯座+灯柱+灯碗（合批 1 mesh）+ 灯芯 + 引擎 makeFlame 小参数暖焰 + 暖晕（自写原语） */
function makeOilLamp(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const wood=o.wood===undefined?0x6b4a26:o.wood;
  const haloA=o.halo===undefined?0.30:o.halo;
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(0.42,0.58,0.22,14); base.translate(0,0.11,0); B.put(base,wood);
  const stem=new THREE.CylinderGeometry(0.075,0.11,0.62,10); stem.translate(0,0.52,0); B.put(stem,shadeColor(wood,0.85));
  const bowl=new THREE.CylinderGeometry(0.30,0.20,0.24,12); bowl.translate(0,0.94,0); B.put(bowl,wood);
  const lip=new THREE.TorusGeometry(0.29,0.035,6,14); lip.rotateX(Math.PI/2); lip.translate(0,1.06,0); B.put(lip,shadeColor(wood,1.3));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x6a4a28,emissive:0x0c0703}),{c:0xffc27a,i:o.rim===undefined?0.30:o.rim,p:2.6}));
  const g=new THREE.Group(); g.add(mesh);
  const wick=new THREE.Mesh(new THREE.CylinderGeometry(0.028,0.035,0.20,6),
    new THREE.MeshPhongMaterial({color:0x2a1c10}));
  wick.position.set(0.05,1.14,0); g.add(wick);
  const fl=makeFlame({h:o.fh===undefined?0.62:o.fh,w:0.22,planes:2,embers:10,spark:false,wide:0.34,
    core:0xffe8b0,outer:0xff8a2a,seed:o.seed===undefined?3.3:o.seed,
    light:o.light===undefined?1.5:o.light,lightD:o.lightD===undefined?34:o.lightD,lightC:0xffb46a});
  fl.g.position.set(0.05,1.22,0); g.add(fl.g);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc27a,
    transparent:true,opacity:haloA,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(3.4,4.2,1); halo.position.set(0.05,1.52,0); halo.renderOrder=3; g.add(halo);
  g.scale.setScalar(s);
  return {g,update(t,k){ const kk=k===undefined?1:k;
    fl.update(t,kk);
    halo.material.opacity=haloA*(0.88+0.12*Math.sin(t*6.1))*kk;   // ≤ 初值×fadeK
  }};
}

/* 远行者剪影：包袱行囊（合批 1 mesh，"临行远行"的点睛小人物） */
function makeWalkerSil(o){
  o=o||{};
  const c=o.color===undefined?0x4a3826:o.color;
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.5,1.7,8); body.translate(0,0.85,0); B.put(body,c);
  const head=new THREE.SphereGeometry(0.19,8,6); head.translate(0,1.86,0); B.put(head,c);
  const pack=new THREE.BoxGeometry(0.36,0.52,0.22); pack.translate(0,1.32,-0.32); B.put(pack,shadeColor(c,0.8));
  const hat=new THREE.ConeGeometry(0.30,0.16,10); hat.translate(0,2.02,0); B.put(hat,shadeColor(c,1.25));
  const mesh=B.mesh(new THREE.MeshBasicMaterial({color:0xffffff,vertexColors:true,transparent:true,opacity:1}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mat:mesh.material};
}

function bCover(){ // 卷首 · 宣纸暖烛，一线横陈
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0xece1c8,c2:0xded0ae,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:30,layers:3,peaks:5,seed:41,color:0x4a3a28,atmo:0xd8c6a2,
    fogK:0.62,glowK:0.05,glow:0xf4ead2,y:-12});
  ridge.g.position.set(0,0,-70); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const mist=makeMist({n:8,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xe4d4b0,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:80,box:[220,40,130],pos:[0,10,-40],color:0xb28f52,size:7,speed:0.04,
    rise:0,add:false,maxA:0.40});
  g.add(motes.points);
  /* 一根悬空的线（全诗母题预告） */
  const pts=[];
  for(let i=0;i<=24;i++){ const u=i/24;
    pts.push(new THREE.Vector3(-70+140*u,16+Math.sin(u*Math.PI)*6+Math.sin(u*9+1.2)*1.6,-26+Math.sin(u*3.1)*8)); }
  const thread=new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),
    new THREE.LineBasicMaterial({color:0x8a5a2a,transparent:true,opacity:0.55}));
  g.add(thread);
  /* 前景：暖枝框景 */
  const brR=makeForeground({kind:'坡石',n:3,r:4.6,w:26,d:9,color:0x2e2314,seed:9,rim:0.18,rimC:0xe8cba0});
  brR.g.position.set(17,-1.6,60); g.add(brR.g);
  const brL=makeForeground({kind:'坡石',n:2,r:4.0,w:22,d:8,color:0x2e2314,seed:17,rim:0.15,rimC:0xe8cba0});
  brL.g.position.set(-20,-1.5,61); g.add(brL.g);
  addLights(g,{c:0xffe2b0,i:0.5,p:[40,60,40]},{c:0xc7b189,i:0.65});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    mist.update(t,k); motes.update(t); brR.update(t,k); brL.update(t,k);
    thread.rotation.z=Math.sin(t*0.24)*0.02; thread.position.y=Math.sin(t*0.18)*0.8;
  }};
}
function bThread(){ // 一 · 手中线 —— 慈母油灯下缝衣：烛下案头，慈母引线，衣在架上
  const g=new THREE.Group();
  const grd=makeGround({r:200,c1:0x6a5436,c2:0x54402a,y:0}); g.add(grd.mesh);
  /* 背景：夜色里淡赭远山一线（门户外天际） */
  const ridge=makeRange({r:220,h:26,layers:2,peaks:4,seed:51,color:0x453623,atmo:0xcbb489,
    fogK:0.70,glowK:0.04,glow:0xf2e6c8,y:-4});
  ridge.g.position.set(0,0,-92); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const mist=makeMist({n:6,spread:[220,26,140],pos:[0,8,-70],scale:74,color:0xdcc9a2,op:0.09});
  g.add(mist.g);
  /* 中景：案 + 衣料 + 针线筐 */
  const table=makeTable({w:11,d:5,h:1.6,wood:0x5a4026});
  table.g.position.set(0,0,0); g.add(table.g);
  const clothGeo=new THREE.PlaneGeometry(8.6,4.2,10,6);
  { const pa=clothGeo.attributes.position;
    for(let i=0;i<pa.count;i++){ pa.setZ(i,Math.sin(pa.getX(i)*0.9)*0.10+Math.cos(pa.getY(i)*1.2)*0.08); }
    clothGeo.computeVertexNormals(); }
  const cloth=new THREE.Mesh(clothGeo,new THREE.MeshPhongMaterial({color:0xdccbaa,side:THREE.DoubleSide,shininess:6}));
  cloth.rotation.x=-Math.PI/2; cloth.position.set(-1.2,1.68,0.2); g.add(cloth);
  const bb=new GeoBag();
  const basket=new THREE.CylinderGeometry(0.85,0.62,0.7,12); basket.translate(0,0.35,0); bb.put(basket,0x8a6a3a);
  for(let i=0;i<3;i++){ const sp=new THREE.CylinderGeometry(0.13,0.13,0.46,8);
    sp.translate(-0.4+i*0.4,0.86,(i%2?0.18:-0.12)); bb.put(sp,0xb89d6e); }
  const baskM=bb.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,specular:0x554433}));
  baskM.position.set(-3.8,1.6,1.7); g.add(baskM);
  /* 衣架与游子身上衣（木架合批 1 mesh + 交叉两片衣身） */
  const rw=new GeoBag();
  [-1.6,1.6].forEach(function(x){ const pole=new THREE.CylinderGeometry(0.13,0.18,7.4,8);
    pole.translate(x,3.7,0); rw.put(pole,0x3f2f1c); });
  const bar=new THREE.CylinderGeometry(0.09,0.09,3.6,8); bar.rotateZ(Math.PI/2); bar.translate(0,7.1,0); rw.put(bar,0x3f2f1c);
  const feet=new THREE.BoxGeometry(4.4,0.24,1.6); feet.translate(0,0.12,0); rw.put(feet,0x3f2f1c);
  const rack=new THREE.Group();
  rack.add(rw.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x060402}),{c:0xd8b485,i:0.22,p:2.4})));
  const robeM=new THREE.MeshPhongMaterial({color:0xcbb894,side:THREE.DoubleSide,shininess:8});
  const robe=new THREE.Mesh(new THREE.PlaneGeometry(3.3,5.4),robeM); robe.position.y=4.25; rack.add(robe);
  const robe2=new THREE.Mesh(new THREE.PlaneGeometry(3.3,5.4),robeM); robe2.rotation.y=Math.PI/2; robe2.position.y=4.25; rack.add(robe2);
  rack.position.set(8.4,0,-4.6); g.add(rack);
  /* 慈母（坐姿，油灯旁引线） */
  const mother=makeFigure({pose:'坐饮',noProp:true,robe:0x6b4a30,belt:0x8a6a3a,collar:0xd9c8a0,
    hat:'发髻',scale:1.15,rim:0.30,rimC:0xffc27a});
  mother.position.set(-5.0,0,-1.6); mother.rotation.y=0.85; g.add(mother);
  /* 油灯（画面右侧暖光源：灯座+灯芯+引擎小暖焰） */
  const lamp=makeOilLamp({scale:1.15,light:1.6,lightD:40,seed:3.3});
  lamp.g.position.set(3.9,1.6,1.8); g.add(lamp.g);
  /* 手中线：慈母手 → 案上布 → 架上衣领（细线随烛焰轻晃，Line 逐帧重采样不重建几何） */
  const handP=new THREE.Vector3(-4.15,2.85,-1.05), clothP=new THREE.Vector3(-1.2,1.76,0.3),
        collarP=new THREE.Vector3(8.4,5.9,-4.6);
  const cps=[handP.clone(),new THREE.Vector3(),clothP.clone(),new THREE.Vector3(),collarP.clone()];
  const crv=new THREE.CatmullRomCurve3(cps);
  const thN=14, thPos=new Float32Array(thN*3), thTmp=new THREE.Vector3();
  const thGeo=new THREE.BufferGeometry();
  thGeo.setAttribute('position',new THREE.BufferAttribute(thPos,3));
  const thread=new THREE.Line(thGeo,new THREE.LineBasicMaterial({color:0xd9c398,transparent:true,opacity:0.85}));
  thread.renderOrder=2; thread.frustumCulled=false; g.add(thread);
  const motes=makeGlow({n:40,box:[24,9,14],pos:[1.5,4.2,1],color:0xb28f52,size:6,speed:0.05,rise:0,add:false,maxA:0.34});
  g.add(motes.points);
  /* 前景：檐下暗枝 */
  const br=makeForeground({kind:'坡石',n:2,r:3.6,w:20,d:7,color:0x2e2314,seed:91,rim:0.15,rimC:0xe8cba0});
  br.g.position.set(-14,-1.2,13); g.add(br.g);
  addLights(g,{c:0xffd9a8,i:0.28,p:[10,30,20]},{c:0x8a7050,i:0.78});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    mist.update(t,k); motes.update(t); br.update(t,k);
    lamp.update(t,k); mother.update(t,k);
    const s1=Math.sin(t*0.9)*0.35, s2=Math.cos(t*0.7)*0.30;
    cps[1].lerpVectors(handP,clothP,0.5); cps[1].y-=0.55+s1*0.4; cps[1].z+=0.5;
    cps[3].lerpVectors(clothP,collarP,0.5); cps[3].y-=0.6+s2; cps[3].x+=0.4;
    for(let i=0;i<thN;i++){ crv.getPoint(i/(thN-1),thTmp);
      thPos[i*3]=thTmp.x; thPos[i*3+1]=thTmp.y; thPos[i*3+2]=thTmp.z; }
    thGeo.attributes.position.needsUpdate=true;
  }};
}
function bSew(){ // 二 · 密密缝（标志性瞬间）—— 油灯下一双把手一针一线，门外游子正远行
  const g=new THREE.Group();
  const grd=makeGround({r:200,c1:0x5c4930,c2:0x4a3a26,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:220,h:24,layers:2,peaks:4,seed:61,color:0x453623,atmo:0xc4ad82,
    fogK:0.72,glowK:0.04,glow:0xf0e2c2,y:-4});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const mist=makeMist({n:6,spread:[200,22,130],pos:[0,7,-75],scale:70,color:0xd6c298,op:0.09});
  g.add(mist.g);
  /* 中景：矮案 + 衣料（镜头贴近，针脚清晰） */
  const table=makeTable({w:16,d:10,h:2.6,wood:0x54402a});
  table.g.position.set(0,0,-0.4); g.add(table.g);
  const clothGeo=new THREE.PlaneGeometry(13,8.5,12,8);
  { const pa=clothGeo.attributes.position;
    for(let i=0;i<pa.count;i++){ pa.setZ(i,Math.sin(pa.getX(i)*0.7)*0.07+Math.cos(pa.getY(i)*0.9)*0.06); }
    clothGeo.computeVertexNormals(); }
  const cloth=new THREE.Mesh(clothGeo,new THREE.MeshPhongMaterial({color:0xdccbaa,side:THREE.DoubleSide,shininess:6}));
  cloth.rotation.x=-Math.PI/2; cloth.position.set(0,2.66,-0.4); g.add(cloth);
  /* 油灯（画面左侧暖光源） */
  const lamp=makeOilLamp({scale:1.2,light:1.7,lightD:42,seed:7.7});
  lamp.g.position.set(-6.6,2.6,-2.6); g.add(lamp.g);
  /* 一双把手（各合批 1 mesh，暖墨剪影） */
  const handMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,specular:0x554033});
  function handMesh(){
    const B=new GeoBag();
    const palm=new THREE.BoxGeometry(1.5,0.55,1.9); B.put(palm,0x4a3524);
    for(let i=0;i<4;i++){ const f=new THREE.CylinderGeometry(0.19,0.22,1.3,7);
      f.rotateX(1.25); f.translate(-0.55+i*0.37,0.1,-1.2); B.put(f,0x4a3524); }
    const th=new THREE.CylinderGeometry(0.2,0.24,0.95,7); th.rotateZ(0.7); th.translate(0.75,0.02,0.2);
    B.put(th,shadeColor(0x4a3524,1.15));
    return B.mesh(handMat);
  }
  const handL=handMesh();
  handL.position.set(0.6,2.92,1.05); handL.rotation.y=0.12; g.add(handL);
  /* 针 + 针眼 + 右手（随针引线） */
  const needleG=new THREE.Group(); g.add(needleG);
  const nB=new GeoBag();
  const ndl=new THREE.CylinderGeometry(0.05,0.018,2.6,7); ndl.rotateZ(-Math.PI/2); ndl.translate(-1.3,0,0);
  nB.put(ndl,0xb9b9c2);
  const eye=new THREE.TorusGeometry(0.09,0.022,6,10); eye.translate(-2.42,0,0); nB.put(eye,0xd8d8e0);
  const needleM=nB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    specular:0xffffff,shininess:110}));
  needleG.add(needleM);
  const handR=handMesh();
  handR.position.set(-1.35,-0.28,0.1); handR.rotation.y=-0.35; needleG.add(handR);
  /* 线与针脚：线尾锚在上一针，池化 9 枚针脚循环取用（不逐帧建几何） */
  const lp=new Float32Array(12);
  const threadGeo=new THREE.BufferGeometry();
  threadGeo.setAttribute('position',new THREE.BufferAttribute(lp,3));
  const thread=new THREE.Line(threadGeo,new THREE.LineBasicMaterial({color:0xc4a878,transparent:true,opacity:0.9}));
  thread.renderOrder=2; thread.frustumCulled=false; g.add(thread);
  const stitchMat=new THREE.MeshPhongMaterial({color:0xb89d6e,shininess:30});
  const stitches=new THREE.Group(); g.add(stitches);
  const POOL=9, X0=-3.4, STEP=0.52, CLOTH_Y=2.72;
  for(let i=0;i<POOL;i++){
    const s=new THREE.Mesh(new THREE.TorusGeometry(0.15,0.032,5,9,Math.PI*1.25),stitchMat);
    s.rotation.x=-Math.PI/2+0.14; s.rotation.z=(i%3-1)*0.09;
    s.position.set(X0+STEP*(i+1),CLOTH_Y+0.03,-0.4);
    s.visible=i<2; stitches.add(s);
  }
  let sHead=2, kX=2;                                  // 下一针序号 / 当前针位
  const anchor=new THREE.Vector3(X0+STEP*2,CLOTH_Y,-0.4);
  const PERIOD=2.4; let phase=0;
  /* 背景：柴门 + 土墙 + 小径，门外游子剪影渐行渐远（"意恐迟迟归"） */
  const dB=new GeoBag();
  [-4.8,4.8].forEach(function(x){ const post=new THREE.BoxGeometry(0.9,9,0.9);
    post.translate(x,4.5,0); dB.put(post,0x3f2f1c); });
  const lintel=new THREE.BoxGeometry(10.8,0.9,1.0); lintel.translate(0,8.6,0); dB.put(lintel,0x3f2f1c);
  const sill=new THREE.BoxGeometry(10.6,0.3,1.7); sill.translate(0,0.15,0.3); dB.put(sill,0x55432c);
  const door=dB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:8,specular:0x3a2e1e,emissive:0x050302}),{c:0xc9a878,i:0.18,p:2.4}));
  door.position.set(-7,0,-16); door.rotation.y=0.35; g.add(door);
  const wallM=new THREE.MeshPhongMaterial({color:0x7d6748});
  const wallL=new THREE.Mesh(new THREE.BoxGeometry(0.7,8.6,6.5),wallM); wallL.position.set(-12.3,4.3,-13.6); wallL.rotation.y=0.35; g.add(wallL);
  const wallR=new THREE.Mesh(new THREE.BoxGeometry(0.7,8.6,6.5),wallM); wallR.position.set(-1.7,4.3,-18.4); wallR.rotation.y=0.35; g.add(wallR);
  const path=new THREE.Mesh(new THREE.BoxGeometry(3.0,0.06,64),
    new THREE.MeshPhongMaterial({color:0x74624a,shininess:3}));
  path.rotation.y=0.22; path.position.set(-9.5,0.04,-44); g.add(path);
  const walker=makeWalkerSil({scale:1.25});
  g.add(walker.g);
  const motes=makeGlow({n:36,box:[22,8,12],pos:[-3,4.6,-1],color:0xb28f52,size:6,speed:0.05,rise:0,add:false,maxA:0.32});
  g.add(motes.points);
  /* 前景：檐角暗枝压住画面上缘 */
  const br=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:6,color:0x2e2314,seed:93,rim:0.13,rimC:0xe0c49a});
  br.g.position.set(-13,-1.1,8); g.add(br.g);
  addLights(g,{c:0xffd9a8,i:0.22,p:[6,26,16]},{c:0x6a5638,i:0.85});
  const eyeW=new THREE.Vector3();
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    mist.update(t,k); motes.update(t); br.update(t,k); lamp.update(t,k);
    /* 引针周期：抬针 → 引线前行 → 刺下成针脚 → 收 */
    phase+=dt/PERIOD; if(phase>=1)phase-=1;
    const p=phase, cx=X0+STEP*kX, nx=cx+STEP;
    let tipX,tipY,pitch;
    if(p<0.30){ const u=p/0.30; tipX=cx; tipY=CLOTH_Y+1.5*(u*u*(3-2*u)); pitch=0.55; }
    else if(p<0.60){ const u=(p-0.30)/0.30; tipX=cx+(nx-cx)*u;
      tipY=CLOTH_Y+1.5*(1-u)+Math.sin(u*Math.PI)*0.55; pitch=0.55-0.45*u; }
    else if(p<0.70){ const u=(p-0.60)/0.10; tipX=nx; tipY=CLOTH_Y+0.5-1.5*u; pitch=-0.5;
      if(u>0.4&&kX<POOL*40){ kX++; const sm=stitches.children[(kX-1)%POOL];
        sm.position.x=nx; sm.visible=true; sHead=kX%POOL; anchor.set(nx,CLOTH_Y,-0.4); pluck(7,0,0.045); } }
    else { const u=(p-0.70)/0.30; tipX=nx; tipY=CLOTH_Y-1.0+1.0*u; pitch=-0.5+0.65*u; }
    needleG.position.set(tipX,tipY,-0.4); needleG.rotation.z=pitch;
    handL.position.y=2.92+Math.sin(t*1.7)*0.045;
    /* 线：针眼 → 垂弧 → 上一针脚 */
    needleG.updateWorldMatrix(true,false);
    eyeW.set(-2.42,0,0).applyMatrix4(needleM.matrixWorld);
    lp[0]=eyeW.x; lp[1]=eyeW.y; lp[2]=eyeW.z;
    lp[3]=eyeW.x*0.55+anchor.x*0.45; lp[4]=Math.min(eyeW.y,anchor.y)-0.32-Math.max(0,tipY-CLOTH_Y)*0.2; lp[5]=eyeW.z*0.55+anchor.z*0.45;
    lp[6]=eyeW.x*0.2+anchor.x*0.8; lp[7]=Math.min(eyeW.y,anchor.y)-0.18; lp[8]=eyeW.z*0.2+anchor.z*0.8;
    lp[9]=anchor.x; lp[10]=anchor.y+0.05; lp[11]=anchor.z;
    threadGeo.attributes.position.needsUpdate=true;
    /* 门外游子渐行渐远（走到天际即隐没，再自柴门出发） */
    const s=(t*0.011+0.18)%1;
    walker.g.position.set(-6.5-30*s+4*(1-s),0,-16-44*s);
    walker.g.position.y=Math.abs(Math.sin(t*2.6))*0.12;
    walker.mat.opacity=1*k*(1-sstep(0.72,0.95,s))*(sstep(0,0.05,s));
  }};
}
function bSpring(){ // 三（末境·可点击）· 三春晖 —— 柴门外线化原野青草，暖金晨光渐暖渐亮
  const g=new THREE.Group();
  const ctl={t:0,boost:0,clicked:false};
  const grd=makeGround({r:260,c1:0x8a9a52,c2:0x6f8048,y:-0.3}); g.add(grd.mesh);
  /* 背景：晨光里的淡赭远山（愈远愈暖愈淡） */
  const ridge=makeRange({r:250,h:30,layers:3,peaks:5,seed:71,color:0x6a5638,atmo:0xdbc9a6,
    fogK:0.60,glowK:0.05,glow:0xf6ecd2,y:-6});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const mist=makeMist({n:6,spread:[260,26,150],pos:[0,8,-80],scale:80,color:0xe8d8b2,op:0.08});
  g.add(mist.g);
  /* 柴门与一角土墙 */
  const dB=new GeoBag();
  [-4.8,4.8].forEach(function(x){ const post=new THREE.BoxGeometry(0.9,9,0.9);
    post.translate(x,4.5,4); dB.put(post,0x3f2f1c); });
  const lintel=new THREE.BoxGeometry(10.8,0.9,1.0); lintel.translate(0,8.6,4); dB.put(lintel,0x3f2f1c);
  const sill=new THREE.BoxGeometry(10.6,0.3,1.7); sill.translate(0,0.15,4.3); dB.put(sill,0x55432c);
  const door=dB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:8,specular:0x3a2e1e,emissive:0x040302}),{c:0xd8b485,i:0.22,p:2.4}));
  g.add(door);
  const wallM=new THREE.MeshPhongMaterial({color:0x8a7350});
  const wallL=new THREE.Mesh(new THREE.BoxGeometry(0.7,8.6,6.5),wallM); wallL.position.set(-5.3,4.3,7.3); g.add(wallL);
  const wallR=new THREE.Mesh(new THREE.BoxGeometry(0.7,8.6,6.5),wallM); wallR.position.set(5.3,4.3,7.3); g.add(wallR);
  /* 线：自门槛延伸进原野（"线"母题接续） */
  const tPts=[[0,4.2],[1.6,-2],[-1.2,-12],[2.2,-28],[-0.6,-46],[1.5,-64]].map(function(pz){
    return new THREE.Vector3(pz[0],0.14,pz[1]); });
  const threadCurve=new THREE.CatmullRomCurve3(tPts);
  const thread=new THREE.Mesh(new THREE.TubeGeometry(threadCurve,48,0.055,5,false),
    new THREE.MeshPhongMaterial({color:0xd9c398,shininess:50,specular:0xfff2cc}));
  g.add(thread);
  /* 草：沿线的两侧渐次萌发 —— 线到远处化作参差青草 */
  const GN=620;
  const grass=new THREE.InstancedMesh(new THREE.ConeGeometry(0.10,1.3,4),
    new THREE.MeshPhongMaterial({color:0x5f7038}),GN);
  const dm=new THREE.Object3D();
  for(let i=0;i<GN;i++){
    let x,z;
    if(i<GN*0.62){
      const pt=threadCurve.getPoint(Math.random());
      x=pt.x+(Math.random()+Math.random()+Math.random()-1.5)*3.4;
      z=Math.min(pt.z+(Math.random()+Math.random()-1)*5,3.2);
    }else{ x=(Math.random()-0.5)*140; z=3.2-Math.random()*74; }
    const hgt=0.5+Math.random()*1.9;
    dm.position.set(x,-0.3+hgt*0.42,z);
    dm.scale.set(0.7+Math.random()*0.6,hgt/1.3,0.7+Math.random()*0.6);
    dm.rotation.set((Math.random()-0.5)*0.3,Math.random()*6.28,(Math.random()-0.5)*0.3);
    dm.updateMatrix(); grass.setMatrixAt(i,dm.matrix);
  }
  grass.instanceMatrix.needsUpdate=true; grass.frustumCulled=false;
  g.add(grass);
  /* 门边守望的慈母 */
  const mother=makeFigure({pose:'独立',robe:0x5a4630,belt:0x7a5a34,collar:0xd9c8a0,hat:'发髻',
    scale:1.05,rim:0.24,rimC:0xffd9a0});
  mother.position.set(3.3,0,2.6); mother.rotation.y=Math.PI; g.add(mother);
  /* 归鸟（掠过晨光原野） */
  const birds=[];
  const bmat=new THREE.MeshBasicMaterial({color:0x4a3826,side:THREE.DoubleSide,transparent:true,opacity:0.95});
  for(let i=0;i<3;i++){
    const b=new THREE.Group();
    const wg=new THREE.PlaneGeometry(3.0,0.85);
    const w1=new THREE.Mesh(wg,bmat); w1.position.x=-1.45;
    const w2=new THREE.Mesh(wg,bmat); w2.position.x=1.45;
    b.add(w1,w2); g.add(b);
    birds.push({b,w1,w2,sp:0.035+Math.random()*0.03,r:60+Math.random()*50,y:30+Math.random()*16,
      ph:Math.random()*6.28,a0:Math.random()*6.28});
  }
  /* 春晖浮尘 + 暖光原野（点击后光晕倍增的"满亮基座"） */
  const pollen=makeGlow({n:110,box:[150,34,130],pos:[0,12,-30],color:0xffe2a0,size:8,speed:0.040,
    rise:0,add:false,maxA:0.40});
  g.add(pollen.points);
  const HAZE=0.5;
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd88a,
    transparent:true,opacity:HAZE,depthWrite:false,blending:THREE.AdditiveBlending}));
  haze.scale.set(150,56,1); haze.position.set(0,10,-70); haze.renderOrder=3; g.add(haze);
  const LMAX=0.9;
  const boostL=new THREE.PointLight(0xffd88a,LMAX,180);
  boostL.position.set(0,26,-30); g.add(boostL);
  /* 前景：两岸草苇摇曳 */
  const reeds=makeForeground({kind:'坡石',n:3,r:4.4,w:24,d:8,color:0x2e2418,seed:83,rim:0.16,rimC:0xffd9a0});
  reeds.g.position.set(16,-1.6,9); g.add(reeds.g);
  const reeds2=makeForeground({kind:'坡石',n:2,r:3.8,w:20,d:7,color:0x2e2418,seed:85,rim:0.14,rimC:0xffd9a0});
  reeds2.g.position.set(-17,-1.5,8); g.add(reeds2.g);
  addLights(g,{c:0xffe2a8,i:0.95,p:[40,110,40],},{c:0xb9a67c,i:0.72});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt; ctl.boost=Math.max(0,ctl.boost-dt/3.2);
      const b=ctl.boost;
      mist.update(t,k); reeds.update(t,k); reeds2.update(t,k);
      pollen.update(t); mother.update(t,k);
      /* 春晖大盛：浮尘/光晕/暖光在满亮基座上按点击系数抬升 */
      pollen.mat.uniforms.uSpeed.value=0.040*(1+2.0*b);
      pollen.mat.uniforms.uMaxA.value=k*0.40*(1+0.45*b);
      haze.material.opacity=HAZE*k*(0.24+0.76*b);
      boostL.intensity=LMAX*k*(0.84+0.16*b);
      for(const o of birds){
        const a=o.a0+t*o.sp;
        o.b.position.set(Math.sin(a)*o.r,o.y+Math.sin(t*0.7+o.ph)*2.5,-30+Math.cos(a)*o.r*0.5);
        o.b.rotation.y=-a+Math.PI/2;
        const f=Math.sin(t*8+o.ph)*0.55;
        o.w1.rotation.z=f; o.w2.rotation.z=-f;
        bmat.opacity=0.95*k;
      }
      mother.rotation.y=Math.PI+Math.sin(t*0.3)*0.05;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0,0.16); pluck(5,0.3,0.10);
        const fl=$('#flash'); fl.textContent='三春晖'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.boost=1;                                     // 春晖大盛（可反复点）
    },clicked:false};
  return api;
}
