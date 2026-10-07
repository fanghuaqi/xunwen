/* ================= 浣溪沙·一曲新词酒一杯 · 三境场景（夜宴金彩·晏殊闲雅暮宴变体：新曲旧亭、花落燕归） =================
   美术口径：暮色亭池——落日熔金、灯烛初上、金樽淡酒；境②转入小园香径，落花与归燕同框。
   与豪饮金赛道的区别：本篇的金长在「残照、灯烛、香径落花」上，通篇禁艳红。 */

/* 烛台：烛身 + 焰（合批 1 mesh + 焰体） */
function makeCandle(o){
  o=o||{};
  const stem=o.stem===undefined?0.8:o.stem, wax=o.wax===undefined?0.9:o.wax;
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(0.30,0.38,0.10,12); base.translate(0,0.05,0); B.put(base,0x7a5c30);
  const st=new THREE.CylinderGeometry(0.06,0.10,stem,8); st.translate(0,0.10+stem/2,0); B.put(st,0x6a4c26);
  const cup=new THREE.CylinderGeometry(0.16,0.10,0.08,10); cup.translate(0,0.10+stem+0.04,0); B.put(cup,0x8a6a38);
  const wd=new THREE.CylinderGeometry(0.11,0.13,wax,10); wd.translate(0,0.10+stem+0.08+wax/2,0); B.put(wd,0xe6d8bc);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xffd890,i:0.34,p:2.6}));
  const g=new THREE.Group(); g.add(mesh);
  const fl=makeFlame({h:o.fh===undefined?0.50:o.fh,w:o.fw===undefined?0.20:o.fw,planes:2,
    embers:o.embers===undefined?8:o.embers,esize:3.5,spark:false,light:o.light||0,lightD:o.lightD||30,
    core:0xffdca0,outer:0xff7a22,wide:0.30,seed:Math.random()*8});
  fl.g.position.y=0.10+stem+0.08+wax; g.add(fl.g);
  return {g,update(t,k){ fl.update(t,k); }};
}

/* 落日：暖白日轮（自绘日面贴图，不带月斑）+ 双层暖辉（fog:false，renderOrder -8，缓缓沉入山脊之后）
   ——境①的时间性元素 */
function makeSun(o){
  o=o||{};
  const r=o.r===undefined?9:o.r;
  const S=256, cv=document.createElement('canvas'); cv.width=cv.height=S;
  const cx=cv.getContext('2d');
  const gr=cx.createRadialGradient(S/2,S/2,0,S/2,S/2,S/2);
  gr.addColorStop(0.00,'rgba(255,246,224,1)');
  gr.addColorStop(0.55,'rgba(255,216,150,1)');
  gr.addColorStop(0.85,'rgba(255,178,98,0.96)');
  gr.addColorStop(1.00,'rgba(255,160,80,0)');
  cx.fillStyle=gr; cx.fillRect(0,0,S,S);
  const tex=new THREE.CanvasTexture(cv);
  const disc=new THREE.Mesh(new THREE.CircleGeometry(r,40),
    new THREE.MeshBasicMaterial({map:tex,color:0xffffff,transparent:true,fog:false,depthWrite:true}));
  disc.renderOrder=-8;
  const g=new THREE.Group(); g.add(disc);
  const halo=[];
  [[r*6.0,0.34,0xd87a30],[r*2.8,0.50,0xffa050]].forEach(function(cfg){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:cfg[2],
      transparent:true,opacity:cfg[1],depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    s.scale.set(cfg[0],cfg[0],1); s.renderOrder=-8; g.add(s);
    halo.push({s:s,op:cfg[1]});
  });
  return {g,disc,halo,update(t,k){
    for(let i=0;i<halo.length;i++)
      halo[i].s.material.opacity=k*halo[i].op*(0.88+0.12*Math.sin(t*0.9+i*1.7));
  }};
}

/* 池畔亭台：台基 + 双阶 + 四柱 + 枋 + 攒尖顶 + 宝顶（合批 1 mesh）——席面在台上 y=0.9 */
function makeTingTai(o){
  o=o||{};
  const B=new GeoBag();
  const stone=0x1e1a16, stone2=0x171310, wood=0x2a1a0e, wood2=0x1e1309;
  const base=new THREE.BoxGeometry(10.4,0.9,8.4); base.translate(0,0.45,0); B.put(base,stone);
  const base2=new THREE.BoxGeometry(11.2,0.20,9.2); base2.translate(0,0.10,0); B.put(base2,stone2);
  const st1=new THREE.BoxGeometry(2.0,0.45,1.2); st1.translate(0,0.225,5.1); B.put(st1,stone2);
  const st2=new THREE.BoxGeometry(2.0,0.45,0.9); st2.translate(0,0.675,4.7); B.put(st2,stone2);
  [[-3.9,-3.1],[3.9,-3.1],[-3.9,3.0],[3.9,3.0]].forEach(function(p){
    const col=new THREE.CylinderGeometry(0.20,0.24,4.4,9); col.translate(p[0],0.9+2.2,p[1]); B.put(col,wood);
    const cap=new THREE.BoxGeometry(0.62,0.14,0.62); cap.translate(p[0],5.32,p[1]); B.put(cap,wood2);
  });
  const bf=new THREE.BoxGeometry(8.6,0.34,0.42); bf.translate(0,5.05,3.0); B.put(bf,wood2);
  const bb=new THREE.BoxGeometry(8.6,0.34,0.42); bb.translate(0,5.05,-3.1); B.put(bb,wood2);
  const bl=new THREE.BoxGeometry(0.42,0.34,6.9); bl.translate(-3.9,5.05,-0.05); B.put(bl,wood2);
  const br=new THREE.BoxGeometry(0.42,0.34,6.9); br.translate(3.9,5.05,-0.05); B.put(br,wood2);
  const roof=new THREE.ConeGeometry(7.4,2.5,4); roof.rotateY(Math.PI/4); roof.translate(0,6.65,0); B.put(roof,0x241609);
  const eave=new THREE.ConeGeometry(8.6,0.9,4); eave.rotateY(Math.PI/4); eave.translate(0,5.45,0); B.put(eave,wood2);
  const fin=new THREE.SphereGeometry(0.20,8,6); fin.translate(0,7.95,0); B.put(fin,0xc9a24a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x8a6a3a,emissive:0x0a0704}),{c:0xe0b060,i:0.30,p:2.6})));
  return g;
}

/* 立灯檠：灯杆 + 承盘 + 焰（夜宴灯列的一盏，合批 1 mesh + 焰体） */
function makeStandingLamp(o){
  o=o||{};
  const h=o.h===undefined?2.7:o.h;
  const B=new GeoBag();
  const ft=new THREE.CylinderGeometry(0.26,0.34,0.12,10); ft.translate(0,0.06,0); B.put(ft,0x3a2c1a);
  const pole=new THREE.CylinderGeometry(0.05,0.08,h,7); pole.translate(0,h/2+0.10,0); B.put(pole,0x4a3820);
  const dish=new THREE.CylinderGeometry(0.26,0.14,0.10,10); dish.translate(0,h+0.16,0); B.put(dish,0x8a6a38);
  const ring=new THREE.TorusGeometry(0.25,0.03,6,16); ring.rotateX(Math.PI/2); ring.translate(0,h+0.22,0); B.put(ring,0xc9a24a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xffd890,i:0.36,p:2.7})));
  const fl=makeFlame({h:o.fh===undefined?0.62:o.fh,w:o.fw===undefined?0.24:o.fw,planes:2,
    embers:o.embers===undefined?10:o.embers,esize:3.5,spark:false,light:o.light||0,lightD:o.lightD||26,
    core:0xffdca0,outer:0xff7a22,wide:0.30,seed:Math.random()*8});
  fl.g.position.y=h+0.24; g.add(fl.g);
  return {g,update(t,k){ fl.update(t,k); }};
}

/* 花树：枝干一 mesh + 花簇一 mesh（暮色里花簇微光），返回 Group */
function makeFlowerTree(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?71:o.seed);
  const h=o.h===undefined?3.8:o.h, spread=o.spread===undefined?2.6:o.spread;
  const B=new GeoBag(), P=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.10,0.20,h,7); trunk.translate(0,h/2,0); B.put(trunk,0x1a1210);
  for(let i=0;i<3;i++){
    const br=new THREE.CylinderGeometry(0.045,0.085,h*0.55,6);
    br.rotateZ((R()-0.5)*1.5); br.rotateX((R()-0.5)*1.2);
    br.translate((R()-0.5)*0.7,h*(0.55+R()*0.3),(R()-0.5)*0.7);
    B.put(br,0x1a1210);
    const crown=new THREE.SphereGeometry(spread*(0.42+R()*0.30),8,6);
    crown.translate((R()-0.5)*spread*1.1,h*(0.72+R()*0.30),(R()-0.5)*spread*0.9);
    B.put(crown,0x231a1c);
  }
  const bloomC=[0xb88a92,0xd0a8b0,0xc898a2,0xd8b4ba];
  for(let i=0;i<16;i++){
    const a=R()*6.283, rr=spread*(0.25+R()*0.75);
    const bl=new THREE.SphereGeometry(0.16+R()*0.13,7,5);
    bl.translate(Math.cos(a)*rr,h*(0.62+R()*0.42),Math.sin(a)*rr*0.8);
    P.put(bl,bloomC[i%4]);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2c2a,emissive:0x080606}),{c:0xd8a070,i:0.24,p:2.4})));
  g.add(P.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,
    specular:0xc898a2,emissive:0x1c0e12,emissiveIntensity:0.8}),{c:0xe0b0a8,i:0.34,p:2.6})));
  return g;
}

/* 归燕：身尾一 mesh + 双翅一 mesh（振翅绕飞；+x 为前进方向），返回 {g,wings,update} */
function makeSwallow(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.16,8,6); body.scale(1.7,0.62,0.5); B.put(body,0x181420);
  const head=new THREE.SphereGeometry(0.09,7,6); head.translate(0.25,0.03,0); B.put(head,0x181420);
  const beak=new THREE.ConeGeometry(0.03,0.10,5); beak.rotateZ(-Math.PI/2); beak.translate(0.37,0.02,0); B.put(beak,0x2c2430);
  const t1=new THREE.ConeGeometry(0.035,0.32,5); t1.rotateZ(Math.PI/2); t1.translate(-0.40,0.0,0.05); B.put(t1,0x181420);
  const t2=new THREE.ConeGeometry(0.035,0.32,5); t2.rotateZ(Math.PI/2); t2.translate(-0.40,0.0,-0.05); B.put(t2,0x181420);
  const belly=new THREE.SphereGeometry(0.10,7,5); belly.scale(1.5,0.7,0.6); belly.translate(0.02,-0.05,0); B.put(belly,0xd8d4cc);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:34,
    specular:0x8a90b0,emissive:0x08080e}),{c:0xd8a070,i:0.42,p:2.8}));
  const W=new GeoBag();
  const wl=new THREE.BoxGeometry(0.66,0.035,0.22); wl.translate(-0.36,0,0); W.put(wl,0x1c1826);
  const wr=new THREE.BoxGeometry(0.66,0.035,0.22); wr.translate(0.36,0,0); W.put(wr,0x1c1826);
  const wings=new THREE.Mesh(mergeGeos(W.list),rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:30,specular:0x8a90b0,emissive:0x08080e,side:THREE.DoubleSide}),{c:0xd8a070,i:0.42,p:2.8}));
  const g=new THREE.Group(); g.add(mesh); g.add(wings);
  g.scale.setScalar(sc);
  const ph=Math.random()*6.283;
  return {g,wings,update(t,k){
    wings.rotation.z=Math.sin(t*9.0+ph)*0.55;
    wings.rotation.x=Math.sin(t*9.0+ph)*0.10;
  }};
}

/* 小园香径：S 形石径 + 径上落花（各合批 1 mesh），返回 Group。路径：z=11→-13，x=sin(u·π·1.15)·1.9 */
function makeGardenPath(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?91:o.seed);
  const B=new GeoBag(), P=new GeoBag();
  for(let i=0;i<14;i++){
    const u=i/13, z=11-u*24, x=Math.sin(u*Math.PI*1.15)*1.9;
    const seg=new THREE.BoxGeometry(1.5+R()*0.5,0.10,1.9+R()*0.6);
    seg.rotateY(Math.sin(u*Math.PI*1.15)*0.5);
    seg.translate(x,0.03,z); B.put(seg,0x3e3024);
  }
  const petalC=[0xc898a2,0xd8b4ba,0xb88892];
  for(let i=0;i<26;i++){
    const u=R(), z=11.5-u*24.5, x=Math.sin(u*Math.PI*1.15)*1.9+(R()-0.5)*2.2;
    const pt=new THREE.CylinderGeometry(0.07,0.09,0.02,6);
    pt.translate(x,0.10,z); P.put(pt,petalC[i%3]);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a3a2a,emissive:0x070605}),{c:0xc9a06a,i:0.26,p:2.4})));
  g.add(P.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:20,
    specular:0xc898a2,emissive:0x180c10,emissiveIntensity:0.9}),{c:0xe0b0a8,i:0.34,p:2.6})));
  return g;
}

/* 园墙：矮墙 + 瓦檐带（合批 1 mesh），圈出「小园」 */
function makeGardenWall(o){
  o=o||{};
  const B=new GeoBag();
  const w=o.w===undefined?26:o.w;
  const wall=new THREE.BoxGeometry(w,2.4,0.5); wall.translate(0,1.2,0); B.put(wall,0x241b16);
  const cap=new THREE.BoxGeometry(w+0.5,0.22,0.9); cap.translate(0,2.5,0); B.put(cap,0x161013);
  for(let i=0;i<=4;i++){
    const p=new THREE.BoxGeometry(0.6,2.62,0.7); p.translate(-w/2+w*i/4,1.31,0); B.put(p,0x1d1512);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a30,emissive:0x070605}),{c:0xd8a070,i:0.22,p:2.4})));
  return g;
}

function bCover(){ // 卷首 · 暮色园苑 —— 落日熔金，亭台剪影，归燕点点
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0a0709,c2:0x181009});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0b0809,atmo:0x40281a,fogK:0.72,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd87a30,
    transparent:true,opacity:0.40,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(64,26,1); glow.position.set(-30,4,-96); glow.renderOrder=-7; g.add(glow);
  const ting1=makeTingTai(); ting1.position.set(-24,0,-64); ting1.scale.setScalar(0.85); g.add(ting1);
  const ting2=makeTingTai(); ting2.position.set(28,0,-76); ting2.scale.setScalar(0.6); g.add(ting2);
  const wall=makeGardenWall({w:22}); wall.position.set(6,0,-46); wall.rotation.y=0.2; g.add(wall);
  const sw1=makeSwallow({scale:1.4}); g.add(sw1.g);
  const sw2=makeSwallow({scale:1.1}); g.add(sw2.g);
  const servants=makeCrowd({n:3,rect:[10,-38,26,10],seed:161,color:0x14100c,rimC:0xe0b060,rim:0.22,sMin:0.8,sMax:1.0});
  g.add(servants.mesh);
  const mist=makeMist({n:9,spread:[240,30,140],pos:[0,8,-50],scale:78,color:0x8a5a40,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:56,box:[180,30,100],pos:[0,8,-30],color:0xe0b060,size:6,speed:0.05,rise:0,maxA:0.28});
  g.add(motes.points);
  const fg=makeForeground({kind:'树枝',n:2,w:16,d:6,color:0x060404,seed:9,sway:0.9,rim:0.14});
  fg.g.position.set(-18,-1,18); g.add(fg.g);
  const rail=makeForeground({kind:'栏杆',w:26,h:3.0,color:0x080505,seed:11,rim:0.12});
  rail.g.position.set(0,-2,20); g.add(rail.g);
  addLights(g,{c:0xd8a060,i:0.30,p:[-40,40,30]},{c:0x2e2418,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); servants.update(t);
    fg.update(t,k); rail.update(t,k); sw1.update(t,k); sw2.update(t,k);
    const a1=t*0.30, a2=t*0.24+2.6;
    sw1.g.position.set(2+Math.cos(a1)*9,7.6+Math.sin(t*0.7)*0.6,-24+Math.sin(a1)*6);
    sw1.g.rotation.y=Math.atan2(-Math.cos(a1)*6,-Math.sin(a1)*9);
    sw2.g.position.set(-8+Math.cos(a2)*7,6.4+Math.sin(t*0.9+1)*0.5,-34+Math.sin(a2)*5);
    sw2.g.rotation.y=Math.atan2(-Math.cos(a2)*5,-Math.sin(a2)*7);
    glow.material.opacity=k*(0.34+0.06*(0.5+0.5*Math.sin(t*0.5)));
  }};
}

function bXinTing(){ // 壹 · 新曲旧亭 —— 一曲新词酒一杯，去年天气旧亭台；夕阳西下几时回（落日渐沉=时间性元素）
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0b0807,c2:0x181009});
  grd.mesh.position.y=-2.4; g.add(grd.mesh);
  const water=makeWater({size:600,seg:96,amp:0.8,freq:0.10,speed:1,flow:[0.10,1],
    deep:0x0e1216,shallow:0x241a12,skyc:0x3a2414,moonDir:[-0.36,0.14,-0.92],spec:1.6,y:-1.7});
  water.mesh.material.uniforms.uMoonColor.value=C(0xffb070);
  g.add(water.mesh);
  const ridge=makeRange({r:210,h:22,layers:2,peaks:4,seed:1571,color:0x0c0807,atmo:0x4a2c18,fogK:0.62,glowK:0.05});
  g.add(ridge.g);
  const sun=makeSun({r:9}); sun.g.position.set(-42,14,-95); g.add(sun.g);
  /* 亭台（席面 y=0.9）+ 后帷 */
  const ting=makeTingTai(); ting.position.set(0,0,-6.4); g.add(ting);
  const curtain=makeCurtain({w:8.2,h:4.2,color:0x4a3018,dark:0x1c1008,folds:6,deep:0.6});
  curtain.g.position.set(0.4,0.9,-9.1); g.add(curtain.g);
  /* 案 + 盘飧 + 酒器（金樽一、陶壶一、金杯四）+ 香炉 */
  const tb=makeTable({w:4.8,d:1.9,h:1.5,wood:0x33200f}); tb.g.position.set(-1.6,0.9,-6.2); g.add(tb.g);
  const dish1=makeDish({r:0.8,n:5}); dish1.g.position.set(-2.7,2.4,-6.5); dish1.g.rotation.y=0.3; g.add(dish1.g);
  const dish2=makeDish({r:0.7,n:4,foods:[0xc08a3a,0x6a7a3a,0xd8b45a,0x8a5a2a]});
  dish2.g.position.set(-0.5,2.4,-6.9); g.add(dish2.g);
  const zun=makeVessel({type:'樽',mat:'金',scale:1.05,liquid:true}); zun.g.position.set(-1.1,2.4,-5.7); g.add(zun.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.9}); hu.g.position.set(-3.6,2.4,-5.9); g.add(hu.g);
  [[0.1,-5.6],[0.7,-6.5],[-2.2,-5.6],[0.4,-6.9]].forEach(function(p,i){
    const cp=makeVessel({type:'杯',mat:'金',scale:0.8,liquid:i<2,shadow:false});
    cp.g.position.set(p[0],2.4,p[1]); g.add(cp.g);
  });
  const censer=makeVessel({type:'碗',mat:'陶',scale:0.7,shadow:false}); censer.g.position.set(-3.7,2.4,-6.8); g.add(censer.g);
  const smoke=makeGlow({n:30,box:[0.6,5.5,0.6],pos:[-3.7,2.9,-6.8],color:0xc0a890,size:3.4,speed:0.16,rise:1,maxA:0.16});
  g.add(smoke.points);
  /* 人物：歌女独立而歌，主人与客坐饮，侍女立后 */
  const singer=makeFigure({pose:'独立',robe:0x5a3050,belt:0xc9a24a,skin:0xe0c0a8,hair:0x1a1210,collar:0xe8d0b0,
    hat:'发髻',face:0.2,scale:0.94,rim:0.55,rimC:0xffd890,noProp:true});
  singer.position.set(3.0,0.9,-4.6); singer.rotation.y=-2.4; g.add(singer);
  const host=makeFigure({pose:'坐饮',robe:0x707c8e,belt:0x8a6a3a,skin:0xd9b189,hat:'幞头',
    face:-0.3,scale:1.02,rim:0.5,rimC:0xffd890});
  host.position.set(-2.6,0.9,-4.9); host.rotation.y=0.5; g.add(host);
  const guest=makeFigure({pose:'坐饮',robe:0x8a6a4a,belt:0x6a5030,skin:0xd9b189,hat:'幞头',
    face:0.4,scale:1.0,rim:0.5,rimC:0xffd890});
  guest.position.set(-0.4,0.9,-7.6); guest.rotation.y=-2.7; g.add(guest);
  const maid=makeFigure({pose:'独立',robe:0x2c2420,belt:0x6a5030,skin:0xd9b189,hat:'发髻',
    face:0.5,scale:0.8,rim:0.4,rimC:0xffd890,noProp:true});
  maid.position.set(4.3,0.9,-8.2); maid.rotation.y=-1.2; g.add(maid);
  /* 灯列：立灯檠二（亭角）+ 案上双烛（烛焰与落日争一点暖金） */
  const lamp1=makeStandingLamp({light:0.9,lightD:22}); lamp1.g.position.set(4.6,0.9,-4.0); g.add(lamp1.g);
  const lamp2=makeStandingLamp({h:2.4}); lamp2.g.position.set(-4.6,0.9,-8.4); g.add(lamp2.g);
  const cd1=makeCandle({light:1.0,lightD:20}); cd1.g.position.set(-0.2,2.4,-5.4); g.add(cd1.g);
  const cd2=makeCandle({stem:0.6,wax:0.7}); cd2.g.position.set(-3.9,2.4,-5.5); g.add(cd2.g);
  /* 金尘 + 雾 + 前景画栏 */
  const motes=makeGlow({n:56,box:[38,12,28],pos:[-1,4.5,-5],color:0xe0b060,size:4.6,speed:0.05,rise:0.25,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[130,16,70],pos:[0,4,-26],scale:58,color:0x8a5a40,op:0.07});
  g.add(mist.g);
  const rail=makeForeground({kind:'栏杆',w:24,h:2.8,color:0x080505,seed:13,rim:0.12});
  rail.g.position.set(2,-1.6,8.6); g.add(rail.g);
  addLights(g,{c:0xffb070,i:0.34,p:[-60,34,-40]},{c:0x362416,i:0.72});
  const pl=new THREE.PointLight(0xffb060,1.7,28); pl.position.set(-1.6,4.0,-5.4); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    smoke.update(t); rail.update(t,k);
    sun.g.position.y=Math.max(4,sun.g.position.y-dt*0.22);
    sun.disc.material.opacity=k*clamp((sun.g.position.y-4)/9,0.22,1);  // 沉入山脊时日轮渐隐
    sun.update(t,k); singer.update(t,k); host.update(t,k); guest.update(t,k); maid.update(t,k);
    lamp1.update(t,k); lamp2.update(t,k); cd1.update(t,k); cd2.update(t,k);
    pl.intensity=k*1.7*(0.72+0.18*Math.sin(t*9.1)+0.10*Math.sin(t*17.3));
  }};
}

function bYanGui(){ // 贰（末境·可点击）· 花落燕归 —— 无可奈何花落去，似曾相识燕归来；小园香径独徘徊
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,glow:0,pulse:0};
  const grd=makeGround({r:110,c1:0x0b090a,c2:0x171014});
  g.add(grd.mesh);
  const ridge=makeRange({r:220,h:24,layers:2,peaks:5,seed:1581,color:0x0b090c,atmo:0x33222a,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 天边残照一道（归燕剪影的背光） */
  const after=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb86a38,
    transparent:true,opacity:0.42,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  after.scale.set(80,22,1); after.position.set(-42,6,-95); after.renderOrder=-7; g.add(after);
  /* 小园：短墙圈园，香径入深，花树二株夹径 */
  const wall=makeGardenWall({w:26}); wall.position.set(3,0,-16.5); g.add(wall);
  g.add(makeGardenPath({seed:91}));
  const tree1=makeFlowerTree({seed:71,h:4.0,spread:2.8}); tree1.position.set(-3.2,0,-8.0); g.add(tree1);
  const tree2=makeFlowerTree({seed:77,h:3.4,spread:2.4}); tree2.position.set(3.4,0,-9.5); g.add(tree2);
  /* 落花：两树各一席缓落（rise=1 即自冠及地） */
  const petalBase=0.52;
  const petal1=makeGlow({n:90,box:[6.5,7.5,4.5],pos:[-3.2,0.2,-8.0],color:0xd8a8b0,size:5.2,speed:0.055,rise:1,add:false,maxA:petalBase});
  const petal2=makeGlow({n:70,box:[5.5,6.5,4.0],pos:[3.4,0.2,-9.5],color:0xc898a2,size:4.6,speed:0.05,rise:1,add:false,maxA:petalBase*0.85});
  g.add(petal1.points); g.add(petal2.points);
  /* 归燕三只绕园而飞 + 交互燕（点击后自檐下掠过香径） */
  const swallows=[];
  [[2,6.0,-10,6.0,0.34,0],[-3,5.4,-13,5.0,0.42,2.1],[4,6.6,-13,6.8,0.27,4.2]].forEach(function(p){
    const sw=makeSwallow({scale:1.2}); g.add(sw.g);
    swallows.push({sw:sw,cx:p[0],cy:p[1],cz:p[2],r:p[3],w:p[4],ph:p[5]});
  });
  const dart=makeSwallow({scale:1.25}); dart.g.visible=false; g.add(dart.g);
  /* 诗人独立香径（背影微侧，向花深处） */
  const poet=makeFigure({pose:'独立',robe:0x707c8e,belt:0x8a6a3a,skin:0xd9b189,hat:'幞头',
    face:-0.2,scale:1.04,rim:0.55,rimC:0xffd890,noProp:true});
  poet.position.set(1.5,0,-3.4); poet.rotation.y=2.55; g.add(poet);
  /* 暮色初灯一盏（金彩点题）+ 金尘 + 花屑迸光 */
  const lpole=new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.09,3.4,7),
    rimHook(new THREE.MeshPhongMaterial({color:0x4a3820,shininess:20,specular:0x8a6a3a,emissive:0x0a0704}),
      {c:0xd8a860,i:0.3,p:2.6}));
  lpole.position.set(5.9,1.7,-13.8); g.add(lpole);
  const lantern=makeLantern(0.5,{flick:0.9});
  lantern.position.set(5.9,3.2,-13.8); g.add(lantern);
  lantern.traverse(function(o){ if(o.isSprite)o.material.opacity=0.78; });
  const motes=makeGlow({n:44,box:[34,10,26],pos:[0,4,-7],color:0xe0b060,size:4.2,speed:0.05,rise:0.2,maxA:0.22});
  g.add(motes.points);
  const burst=makeBurst({n:70,color:0xe8c0c8,pos:[-2.2,3.4,-8.0]}); g.add(burst.points);
  const mist=makeMist({n:5,spread:[130,16,70],pos:[0,4,-24],scale:58,color:0x6a5060,op:0.08});
  g.add(mist.g);
  const rail=makeForeground({kind:'栏杆',w:22,h:2.8,color:0x080505,seed:15,rim:0.12});
  rail.g.position.set(-2,-1.4,7.8); g.add(rail.g);
  const fg2=makeForeground({kind:'树枝',n:2,w:14,d:5,color:0x060404,seed:19,sway:1.0,rim:0.12});
  fg2.g.position.set(-10,-0.5,9); g.add(fg2.g);
  addLights(g,{c:0xd89a78,i:0.26,p:[-40,30,20]},{c:0x2e2620,i:0.70});
  const pl=new THREE.PointLight(0xffc890,1.35,22); pl.position.set(1.0,3.4,-7.0); g.add(pl);
  const DART_T=3.2;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.glow=Math.min(1,ctl.glow+dt/1.8);
        ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      }
      const gl=ctl.glow, pu=ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motes.update(t); rail.update(t,k); fg2.update(t,k);
      petal1.update(t); petal2.update(t); burst.update(t);
      petal1.mat.uniforms.uMaxA.value=petalBase*(1.0+1.4*gl*pu);
      petal2.mat.uniforms.uMaxA.value=petalBase*0.85*(1.0+1.4*gl*pu);
      poet.update(t,k);
      lantern.userData.update(t,k);
      for(let i=0;i<swallows.length;i++){
        const s=swallows[i], a=t*s.w+s.ph;
        s.sw.g.position.set(s.cx+Math.cos(a)*s.r, s.cy+Math.sin(t*0.7+s.ph)*0.7, s.cz+Math.sin(a)*s.r*0.7);
        s.sw.g.rotation.y=Math.atan2(-Math.cos(a)*s.r*0.7*s.w,-Math.sin(a)*s.r*s.w);
        s.sw.g.rotation.z=0.30;
        s.sw.update(t,k);
      }
      if(ctl.clicked){                       // 归燕低掠：自右侧檐下入画，贴香径掠过，向左侧林梢出画
        const du=(ctl.t-0.4)/DART_T;
        if(du>=0&&du<=1){
          dart.g.visible=true;
          const q=du, a=1-q;
          const p0=[9.5,6.0,-1.0], p1=[0.2,1.6,-7.2], p2=[-9.0,7.0,-13.0];
          dart.g.position.set(a*a*p0[0]+2*a*q*p1[0]+q*q*p2[0],
                              a*a*p0[1]+2*a*q*p1[1]+q*q*p2[1],
                              a*a*p0[2]+2*a*q*p1[2]+q*q*p2[2]);
          const dx=2*a*(p1[0]-p0[0])+2*q*(p2[0]-p1[0]), dz=2*a*(p1[2]-p0[2])+2*q*(p2[2]-p1[2]);
          dart.g.rotation.y=Math.atan2(-dz,dx);
          dart.g.rotation.z=-0.5*(1-Math.abs(q-0.5)*2);
          dart.update(t,k);
        } else dart.g.visible=false;
      }
      pl.intensity=k*1.35*(0.62+0.30*gl*(0.85+0.15*Math.sin(t*2.6))+0.08*Math.sin(t*7.3));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.pulse=1;
        burst.fire();
        pluck(2,0.05,0.14); pluck(4,0.4,0.13); pluck(5,0.8,0.12); pluck(1,1.15,0.10); bell();
        const fl=$('#flash'); fl.textContent='似曾相识燕归来'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
