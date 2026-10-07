/* ================= 行宫 · 三境场景（宣纸留白 · 荒宫白头变体：卷首荒宫、寥落宫花、白头宫女）
   本诗专属系统「红与白」：宫花寂寞红（全页唯一浓色）对白头宫女（时间感）。
   末境点击说玄宗 → 昔日行宫的繁华虚影自残宫之上浮现又淡去（闪回），宫女闲坐剪影不动，题字「说玄宗」。
   宣纸留白：纸底、淡墨远山、浓墨残宫；不用金色辉光、不设水。 ================= */

/* —— 残破行宫：半塌的殿身 + 断柱 + 残檐 + 台基（合批 1 mesh） —— */
function makeRuinedPalaceXG(o){
  o=o||{};
  const w=o.w===undefined?14:o.w, d=o.d===undefined?9:o.d, h=o.h===undefined?6:o.h;
  const wall=o.wall===undefined?0x2c2f33:o.wall, tile=o.tile===undefined?0x23262a:o.tile;
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?901:o.seed);
  const base=new THREE.BoxGeometry(w*1.25,1.0,d*1.2); base.translate(0,0.5,0); B.put(base,shadeColor(0x6a6458,0.9));
  const step=new THREE.BoxGeometry(w*1.05,0.4,d*1.0); step.translate(0,1.15,0); B.put(step,shadeColor(0x7a7468,1.0));
  /* 主殿：右侧尚存、左侧半塌（用高低两块表现） */
  const b1=new THREE.BoxGeometry(w*0.58,h,d*0.92); b1.translate(w*0.20,1.35+h/2,-d*0.04); B.put(b1,wall);
  const b2=new THREE.BoxGeometry(w*0.34,h*0.42,d*0.88); b2.translate(-w*0.32,1.35+h*0.21,-d*0.05); B.put(b2,shadeColor(wall,0.9));
  /* 残檐：右侧完整坡顶、左侧塌落一角 */
  const r1=new THREE.BoxGeometry(w*0.62,0.28,d*0.55); r1.rotateX(0.34); r1.translate(w*0.20,1.35+h+0.55,d*0.24); B.put(r1,tile);
  const r2=new THREE.BoxGeometry(w*0.62,0.28,d*0.55); r2.rotateX(-0.34); r2.translate(w*0.20,1.35+h+0.55,-d*0.24); B.put(r2,shadeColor(tile,0.92));
  const r3=new THREE.BoxGeometry(w*0.30,0.24,d*0.4); r3.rotateZ(-0.5); r3.translate(-w*0.36,1.35+h*0.46,d*0.22); B.put(r3,shadeColor(tile,1.1));
  /* 断柱：三根（高矮不一，一根倾倒） */
  [[-w*0.44,h*1.55,-d*0.5],[-w*0.30,h*0.9,-d*0.52],[w*0.46,h*1.3,d*0.5]].forEach(function(p){
    const c=new THREE.CylinderGeometry(0.32,0.38,p[1],10); c.translate(p[0],1.35+p[1]/2,p[2]); B.put(c,shadeColor(wall,1.08));
    const cap=new THREE.BoxGeometry(1.0,0.2,1.0); cap.translate(p[0],1.35+p[1]+0.1,p[2]); B.put(cap,shadeColor(tile,1.15));
  });
  const fall=new THREE.CylinderGeometry(0.30,0.34,3.4,9); fall.rotateZ(1.35); fall.rotateY(0.4);
  fall.translate(-w*0.2,1.6,d*0.62); B.put(fall,shadeColor(wall,0.95));
  /* 门洞与窗（暗） */
  const door=new THREE.BoxGeometry(w*0.2,h*0.5,0.24); door.translate(w*0.20,1.35+h*0.25,d*0.47); B.put(door,0x121316);
  const win=new THREE.BoxGeometry(w*0.14,h*0.3,0.22); win.translate(w*0.40,1.35+h*0.62,d*0.46); B.put(win,0x16181b);
  /* 残墙一段 */
  const wallSeg=new THREE.BoxGeometry(w*0.5,h*0.6,0.7); wallSeg.rotateY(0.2);
  wallSeg.translate(-w*0.62,1.35+h*0.3,-d*0.2); B.put(wallSeg,shadeColor(wall,0.92));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a6a60,emissive:0x0a0a0c}),{c:o.rimC===undefined?0x8a8a78:o.rimC,i:0.20,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 繁华虚影：昔日行宫的完整宫殿剪影（半透；点击后浮现又淡去） —— */
function makePalaceGhostXG(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, d=o.d===undefined?10:o.d, h=o.h===undefined?7.4:o.h;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w*1.3,1.2,d*1.25); base.translate(0,0.6,0); B.put(base,0xb8b2a4);
  /* 三层殿身（层层收进）+ 双层檐 */
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,1.2+h/2,0); B.put(body,0xcfc9bc);
  [1,-1].forEach(function(s){
    const r=new THREE.BoxGeometry(w*1.2,0.4,d*0.6); r.rotateX(s*0.36);
    r.translate(0,1.2+h+0.6,s*d*0.27); B.put(r,0xa8a29a);
  });
  const ridge=new THREE.BoxGeometry(w*1.24,0.34,0.5); ridge.translate(0,1.2+h+1.24,0); B.put(ridge,0x8e8a80);
  const up=new THREE.BoxGeometry(w*0.66,h*0.5,d*0.7); up.translate(0,1.2+h+1.5+h*0.25,0); B.put(up,0xc6c0b4);
  const up2=new THREE.ConeGeometry(w*0.5,h*0.4,4); up2.rotateY(Math.PI/4); up2.translate(0,1.2+h+1.5+h*0.5+h*0.2,0); B.put(up2,0x9a958c);
  /* 柱列 */
  for(let i=0;i<6;i++){
    const x=-w*0.42+w*0.84*i/5;
    const c=new THREE.CylinderGeometry(0.28,0.32,h,10); c.translate(x,1.2+h/2,d*0.52); B.put(c,0xd8d2c6);
    const c2=new THREE.CylinderGeometry(0.28,0.32,h,10); c2.translate(x,1.2+h/2,-d*0.52); B.put(c2,0xcfc9bc);
  }
  /* 宫灯成列（暖色小光点由 sprite 另加） */
  const mat=new THREE.MeshBasicMaterial({color:0xffffff,vertexColors:true,transparent:true,
    opacity:0.42,depthWrite:false});
  const mesh=B.mesh(mat); mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  /* 虚影上的宫灯暖光（只调 scale） */
  const lamps=[];
  for(let i=0;i<6;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb060,transparent:true,
      opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set(-w*0.42+w*0.84*i/5,1.2+h*0.62,d*0.58);
    s.scale.set(2.4,2.4,1); s.renderOrder=3; g.add(s); lamps.push(s);
  }
  return {g,mesh,mat,lamps,update:function(t,k,flash){
    const kk=k===undefined?1:k, fl=flash===undefined?0:flash;
    mat.opacity=kk*0.42*fl;                 /* 基座 0.42 = 运行期最大值；闪回时 0→1→0 */
    for(let i=0;i<lamps.length;i++){
      const f=0.6+0.5*fl;
      lamps[i].scale.set(2.4*f,2.4*f,1);
      lamps[i].material.opacity=0.30*fl;    /* 由上面同一 fl 驱动，恒 ≤ 基座 0.30 */
    }
  }};
}

/* —— 宫花：一树深红的宫花（纸色画面里唯一的浓色） —— */
function makeRedBlossomXG(o){
  o=o||{};
  const h=o.h===undefined?4.2:o.h, R=seedRnd(o.seed===undefined?907:o.seed);
  const wood=o.wood===undefined?0x3a322a:o.wood, petal=o.petal===undefined?0xb02a38:o.petal;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.5,0],h*0.055,h*0.024,7),wood);
  const tips=[];
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.6, len=h*(0.34+R()*0.26);
    const p1=[Math.sin(a)*len,h*0.5+len*0.46,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.48,0],p1,h*0.024,h*0.01,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.75){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5,p1[1]+len*0.34,p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.012,h*0.005,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<5;k++){
      const rr=0.19+R()*0.11;
      const fl=new THREE.SphereGeometry(rr,7,6); fl.scale(1.15,0.78,1.05);
      fl.translate(tp[0]+(R()-0.5)*1.0,tp[1]+(R()-0.35)*0.7,tp[2]+(R()-0.5)*1.0);
      B.put(fl,shadeColor(petal,0.82+R()*0.35));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x6a6a60,emissive:0x1c0a0c,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xc89088:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.012+0.02*wd)*Math.sin(t*0.6+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 荒草：行宫阶前的枯草（合批 1 mesh，纸色画面里的淡墨） —— */
function makeDryGrassXG(o){
  o=o||{};
  const n=o.n===undefined?800:o.n, R=seedRnd(o.seed===undefined?911:o.seed);
  const w=o.w===undefined?120:o.w, d=o.d===undefined?40:o.d, B=new GeoBag();
  for(let i=0;i<n;i++){
    const hh=0.4+R()*0.8, x=(R()-0.5)*w, z=(R()-0.5)*d;
    const bl=new THREE.ConeGeometry(0.045,hh,4);
    bl.rotateZ((R()-0.5)*0.5); bl.rotateY(R()*6.283);
    bl.translate(x,hh*0.5,z);
    B.put(bl,shadeColor(o.color===undefined?0x8a8468:o.color,0.7+R()*0.6));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x8a8a78,emissive:0x16150e,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x8a8a78:o.rimC,i:0.14,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.004+0.01*wd)*Math.sin(t*0.5+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 荒宫一角 —— 纸色天地里一座残宫、一树深红
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d0,c2:0xc6cbab,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:50,layers:3,peaks:6,seed:2111,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.03,glow:0x8a8a78,y:-14});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const palace=makeRuinedPalaceXG({w:13,d:8.5,h:5.6,x:-4,y:-1.4,z:-22,seed:903}); g.add(palace.g);
  const blossom=makeRedBlossomXG({h:4.4,seed:909,scale:1.1}); blossom.g.position.set(9,-1.4,-12); g.add(blossom.g);
  const grass=makeDryGrassXG({n:700,w:110,d:36,y:-1.4,z:-2,seed:913}); g.add(grass.g);
  const ink=makeMist({n:7,spread:[220,24,110],pos:[0,9,-48],scale:74,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:180,box:[190,24,100],pos:[0,8,-24],color:0x7a7a70,size:9,speed:0.7,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:7,color:0xb8b2a0,seed:151,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-17,-1.6,34); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:28,n:8,d:6,color:0x3f3f38,seed:153,sway:0.5,rim:0.08,rimC:0x5a5a4e});
  fg2.g.position.set(18,-1.4,26); fg2.g.rotation.z=-0.18; g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-50,110,30]},{c:0xd8dac8,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ink.update(t,k); dust.update(t);
    blossom.update(t,k,0.2); grass.update(t,k,0.2);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bLiaoluo(){ // 一 · 寥落宫花 —— 寥落古行宫，宫花寂寞红
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe8e2ce,c2:0xc3c9a8,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:54,layers:3,peaks:6,seed:2121,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.03,glow:0x8a8a78,y:-15});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 寥落古行宫：残殿居左、断柱倒柱、残墙一段 */
  const palace=makeRuinedPalaceXG({w:15,d:9.5,h:6.2,x:-6,y:-1.3,z:-18,seed:917,ry:0.12}); g.add(palace.g);
  const palace2=makeRuinedPalaceXG({w:9,d:6,h:3.4,x:14,y:-1.3,z:-26,seed:919,ry:-0.3}); g.add(palace2.g);
  /* 宫花寂寞红：一树深红（画面唯一浓色） */
  const blossom=makeRedBlossomXG({h:4.8,seed:923,scale:1.2}); blossom.g.position.set(6.5,-1.3,-9); g.add(blossom.g);
  const blossom2=makeRedBlossomXG({h:3.4,seed:927,scale:0.9}); blossom2.g.position.set(-15,-1.3,-12); g.add(blossom2.g);
  const grass=makeDryGrassXG({n:1000,w:130,d:42,y:-1.3,z:-2,seed:929}); g.add(grass.g);
  const ink=makeMist({n:7,spread:[210,22,100],pos:[0,9,-46],scale:72,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:170,box:[180,22,94],pos:[0,8,-22],color:0x7a7a70,size:9,speed:0.7,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0xc0bAA8,seed:155,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-15,-1.5,20); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0xb2ac9a,seed:157,sway:0.6,tip:0x5a5a4a});
  fg2.g.position.set(16,-1.4,18); g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-48,105,28]},{c:0xd8dac8,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); ink.update(t,k); dust.update(t);
      const wind=0.22+0.12*Math.sin(t*0.4);
      blossom.update(t,k,wind); blossom2.update(t,k,wind);
      grass.update(t,k,wind);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(2,0.4,0.08); }};
}
function bBaitou(){ // 二（末境·可点击）· 白头宫女 —— 白头宫女在，闲坐说玄宗
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,flash:0};
  const grd=makeGround({r:260,c1:0xe9e2cf,c2:0xc5cbaa,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:50,layers:3,peaks:6,seed:2131,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.03,glow:0x8a8a78,y:-15});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 残宫在近前景（宫女坐在其残阶上） */
  const palace=makeRuinedPalaceXG({w:16,d:10,h:6.6,x:-3,y:-1.3,z:-14,seed:931,ry:0.06}); g.add(palace.g);
  const grass=makeDryGrassXG({n:900,w:120,d:40,y:-1.3,z:-2,seed:937}); g.add(grass.g);
  /* 白头宫女两人：闲坐（坐饮姿势，白发） */
  const woman1=makeFigure({pose:'坐饮',robe:0x8a8478,belt:0x9a9488,collar:0xf0f0ec,hat:'发髻',
    hair:0xf2f0ea,scale:1.16,rim:0.22,rimC:0x8a8a78,noProp:true});
  woman1.position.set(1.6,-0.6,-6.4); woman1.rotation.y=-1.5; g.add(woman1);
  const woman2=makeFigure({pose:'坐饮',robe:0x7a7468,belt:0x8a8478,collar:0xe8e8e4,hat:'发髻',
    hair:0xeae8e2,scale:1.1,rim:0.20,rimC:0x8a8a78,noProp:true});
  woman2.position.set(-0.6,-0.6,-7.0); woman2.rotation.y=-1.9; g.add(woman2);
  /* 宫花寂寞红（在残宫另一侧，仍是唯一浓色） */
  const blossom=makeRedBlossomXG({h:4.4,seed:941,scale:1.15}); blossom.g.position.set(9.5,-1.3,-10); g.add(blossom.g);
  /* 昔日繁华虚影：完整宫殿剪影，浮在残宫之上（点击后闪回） */
  const ghost=makePalaceGhostXG({w:18,d:11,h:7.6,x:-3,y:-1.0,z:-24,ry:0.06,seed:947}); g.add(ghost.g);
  const ink=makeMist({n:7,spread:[210,22,100],pos:[0,9,-46],scale:72,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:170,box:[180,22,94],pos:[0,8,-22],color:0x7a7a70,size:9,speed:0.7,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0xc4beac,seed:159,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-14,-1.4,12); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0xb4ae9c,seed:161,sway:0.6,tip:0x5a5a4a});
  fg2.g.position.set(14,-1.3,11); g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-46,100,26]},{c:0xd8dac8,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.flash=Math.min(1,ctl.flash+dt/1.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.6);
      /* 闪回：浮现 → 驻留 → 淡去（由 ctl.flash 时间轴驱动，恒 ≤ 1） */
      const fl=ctl.clicked?Math.max(0,Math.sin(Math.min(1,ctl.flash)*Math.PI*0.9)):0;
      const fv=Math.min(1,fl+0.5*ctl.pulse);
      ridge.update(t,0); ink.update(t,k); dust.update(t); grass.update(t,k,0.25);
      blossom.update(t,k,0.25);
      ghost.update(t,k,fv);
      woman1.update(t,k); woman2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        ctl.flash=0;
        pluck(0,0.00,0.12); pluck(2,0.35,0.10); pluck(3,0.70,0.08);
        const fl=$('#flash'); fl.textContent='说玄宗'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：繁华再闪一回 */
    },clicked:false};
  return api;
}
