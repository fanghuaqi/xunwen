/* ================= 赠刘景文 · 三境场景（青绿春晓 · 初冬园圃变体：卷首初冬园圃、荷尽菊残、橙黄橘绿）
   本诗专属系统「残与荣」：前半是凋尽的荷与残破的菊，后半是满树点亮起来的橙黄橘绿。
   末境点击橙黄橘绿 → 荷枯菊残褪去（半透渐隐）、橙橘果实与果园暖光次第点亮。
   与同赛道《浣溪沙》（溪山兰芽）、《画菊》（篱菊北风）不同：本页是初冬园圃的残荷、残菊与橙橘。 ================= */

/* —— 残荷：枯茎 + 破叶 + 莲蓬（合批 1 mesh；末境点击后随 fadeK 渐隐 = 褪去） —— */
function makeLotusWitherZLJ(o){
  o=o||{};
  const n=o.n===undefined?13:o.n, R=seedRnd(o.seed===undefined?27:o.seed);
  const w=o.w===undefined?26:o.w, d=o.d===undefined?16:o.d;
  const stemC=o.stem===undefined?0x4a4234:o.stem, leafC=o.leaf===undefined?0x3a4230:o.leaf;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, h=0.7+R()*1.5;
    const lean=(R()-0.5)*0.5;
    B.put(limbGeo([x,0,z],[x+lean*h,h,z+(R()-0.5)*0.4],0.045,0.03,5),shadeColor(stemC,0.8+R()*0.5));
    if(R()<0.55){       /* 破叶：残缺的圆盘 */
      const r=0.5+R()*0.5;
      const lf=new THREE.CircleGeometry(r,7,0,R()*2.2+1.2);
      lf.rotateX(-Math.PI/2+R()*0.5); lf.rotateY(R()*6.283);
      lf.translate(x+lean*h*0.9,h+0.05,z+(R()-0.5)*0.4);
      B.put(lf,shadeColor(leafC,0.7+R()*0.6));
    }
    if(R()<0.4){        /* 莲蓬 */
      const pod=new THREE.ConeGeometry(0.16,0.26,7); pod.rotateX(Math.PI);
      pod.translate(x+lean*h,h+0.14,z); B.put(pod,0x5a5040);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a3a2a,emissive:0x0a0c08,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x8fc9a8:o.rimC,i:0.20,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh,mat:mesh.material};
}

/* —— 残菊：枯菊枝 + 少许残瓣（合批 1 mesh） —— */
function makeChrysWitherZLJ(o){
  o=o||{};
  const n=o.n===undefined?7:o.n, R=seedRnd(o.seed===undefined?31:o.seed);
  const B=new GeoBag(), stemC=o.stem===undefined?0x4a5234:o.stem;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*6.0, z=(R()-0.5)*4.4, h=0.9+R()*0.8;
    const lean=(R()-0.5)*0.5;
    B.put(limbGeo([x,0,z],[x+lean*h,h,z],0.035,0.02,5),shadeColor(stemC,0.8+R()*0.5));
    for(let k=0;k<3;k++){
      const lf=new THREE.PlaneGeometry(0.46,0.18);
      lf.rotateZ((R()-0.5)*1.0); lf.rotateY(R()*6.283);
      lf.translate(x+lean*h*(0.4+0.25*k)+(R()-0.5)*0.3,h*(0.4+0.25*k),z+(R()-0.5)*0.3);
      B.put(lf,shadeColor(0x6a6a40,0.7+R()*0.5));
    }
    if(R()<0.6){        /* 残瓣 */
      const pr=0.14+R()*0.1, np=Math.round(4+R()*4);
      for(let k=0;k<np;k++){
        const a=k/np*6.283;
        const pf=new THREE.PlaneGeometry(pr*1.4,pr*0.8);
        pf.rotateZ(a); pf.rotateX(-0.4+R()*0.8);
        pf.translate(x+lean*h+Math.cos(a)*pr*0.6, h+0.03, z+Math.sin(a)*pr*0.6);
        B.put(pf,shadeColor(o.petal===undefined?0xc8a860:o.petal,0.7+R()*0.5));
      }
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a4a30,emissive:0x0c0c06,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x8fc9a8:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh,mat:mesh.material};
}

/* —— 橙橘树：枝干 + 叶 + 满树橙黄橘绿的果实（合批 1 mesh；果实的"点亮"由 sprite 层负责） —— */
function makeCitrusTreeZLJ(o){
  o=o||{};
  const h=o.h===undefined?4.6:o.h, R=seedRnd(o.seed===undefined?37:o.seed);
  const wood=o.wood===undefined?0x3a2a18:o.wood;
  const B=new GeoBag(), fruits=[];
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.5,0],h*0.07,h*0.032,7),wood);
  const nb=o.branches===undefined?6:o.branches;
  const tips=[];
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.32+R()*0.26);
    const p1=[Math.sin(a)*len, h*0.5+len*0.46, Math.cos(a)*len];
    B.put(limbGeo([0,h*0.46,0],p1,h*0.028,h*0.011,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.8){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5, p1[1]+len*0.3, p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.014,h*0.006,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<4;k++){
      const lf=new THREE.PlaneGeometry(0.62,0.26);
      lf.rotateZ((R()-0.5)*0.8); lf.rotateY(R()*6.283);
      lf.translate(tp[0]+(R()-0.5)*0.9, tp[1]+(R()-0.3)*0.6, tp[2]+(R()-0.5)*0.9);
      B.put(lf,shadeColor(0x2f5a2c,0.8+R()*0.5));
    }
    for(let k=0;k<3;k++){
      const rr=0.20+R()*0.09;
      const fx=tp[0]+(R()-0.5)*1.0, fy=tp[1]-(0.25+R()*0.5), fz=tp[2]+(R()-0.5)*1.0;
      const fr=new THREE.SphereGeometry(rr,8,6);
      fr.translate(fx,fy,fz);
      const warm=R()<0.55;
      B.put(fr, warm?shadeColor(0xe08a2a,0.85+R()*0.4):shadeColor(0xd8b83a,0.85+R()*0.4));
      fruits.push([fx,fy,fz]);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a6a3a,emissive:0x161208,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa8cf8f:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mesh,fruits:mesh.material?fruits:fruits};
}

/* —— 果园暖光：果实上的暖金光点（Sprite；点击后放大 = 「橙黄橘绿」次第亮起） —— */
function makeFruitGlowZLJ(o){
  o=o||{};
  const pos=o.pos||[], n=Math.max(1,pos.length);
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc45a,transparent:true,
      opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set(pos[i][0],pos[i][1],pos[i][2]);
    s.scale.set(1.1,1.1,1); s.renderOrder=3; g.add(s);
    items.push({s:s,ph:i*0.7});
  }
  const light=new THREE.PointLight(0xffb84a,o.lightMax===undefined?1.15:o.lightMax,54,2);
  light.position.set(o.lx===undefined?0:o.lx,o.ly===undefined?2.4:o.ly,o.lz===undefined?-6:o.lz);
  g.add(light);
  return {g,items,light,update:function(t,k,lit){
    const kk=k===undefined?1:k, li=lit===undefined?0:lit;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const s=(0.55+0.85*li)*(0.92+0.08*Math.sin(t*2.2+it.ph));
      it.s.scale.set(s*1.5,s*1.5,1);
    }
    light.intensity=kk*(o.lightMax===undefined?1.15:o.lightMax)*(0.10+0.90*li);
  }};
}

/* —— 池岸石：一圈岸边石（遮住水面平面硬边，读成"池"而不是"一块水"），合批 1 mesh —— */
function makePondRimZLJ(o){
  o=o||{};
  const rx=o.rx===undefined?9:o.rx, rz=o.rz===undefined?6:o.rz;
  const n=o.n===undefined?20:o.n, R=seedRnd(o.seed===undefined?71:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const a=i/n*6.283+(R()-0.5)*0.16;
    const rg=rockGeo(0.7+R()*1.0,1,R);
    rg.translate(Math.sin(a)*rx*(1+(R()-0.5)*0.06), o.y===undefined?0.1:o.y, Math.cos(a)*rz*(1+(R()-0.5)*0.06));
    B.put(rg,shadeColor(o.color===undefined?0x18261c:o.color,0.6+R()*0.7));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x233428,emissive:0x040a06}),{c:o.rimC===undefined?0xa8cf8f:o.rimC,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,0,o.z===undefined?0:o.z);
  return {g,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 初冬园圃 —— 残荷池、篱边残菊、远处橙橘园一片橙黄
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0c1710,c2:0x16281a,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:34,layers:3,peaks:5,seed:1111,color:0x0c1911,atmo:0x2f4a34,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const water=makeWater({size:40,seg:30,amp:0.07,freq:0.16,speed:0.4,flow:[0.15,0.45],spec:1.1,
    deep:0x0b2018,shallow:0x24563e,skyc:0x2e5c48,moonDir:[60,90,-160],y:-0.2});
  water.mesh.scale.set(0.7,1,0.5); water.mesh.position.set(-6,-0.2,-10); g.add(water.mesh);
  const rim=makePondRimZLJ({rx:8.6,rz:5.4,n:20,x:-6,z:-10,seed:73,y:0.02}); g.add(rim.g);
  const lotus=makeLotusWitherZLJ({n:11,w:22,d:12,x:-6,y:-0.2,z:-10,seed:29}); g.add(lotus.g);
  const chrys=makeChrysWitherZLJ({n:6,x:10,y:-1.4,z:-6,seed:33}); g.add(chrys.g);
  const c1=makeCitrusTreeZLJ({h:5.0,seed:113,scale:1.05}); c1.g.position.set(-16,-1.4,-26); g.add(c1.g);
  const c2=makeCitrusTreeZLJ({h:4.6,seed:127,scale:1.0}); c2.g.position.set(4,-1.4,-30); g.add(c2.g);
  const c3=makeCitrusTreeZLJ({h:4.2,seed:131,scale:0.92}); c3.g.position.set(17,-1.4,-24); g.add(c3.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.4,w:18,d:7,color:0x070d08,seed:37,rim:0.14,rimC:0xa8cf8f});
  fg.g.position.set(-17,-1.6,36); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:39,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(16,-1.5,24); g.add(fg2.g);
  const crowd=makeCrowd({n:3,rect:[-6,-34,16,8],seed:67,color:0x131e14,rimC:0xa8cf8f,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:40,box:[180,26,90],pos:[0,9,-24],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,28,120],pos:[0,9,-52],scale:78,color:0x1e3424,op:0.11});
  g.add(mist.g);
  addLights(g,{c:0xd8d0a0,i:0.46,p:[-45,80,24]},{c:0x1c2a1e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); crowd.update(t);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bHejin(){ // 一 · 荷尽菊残 —— 荷尽已无擎雨盖，菊残犹有傲霜枝
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0b130d,c2:0x152417,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:32,layers:3,peaks:5,seed:1121,color:0x0b160f,atmo:0x2c4432,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-9});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 残荷之池（近景主体） */
  const water=makeWater({size:36,seg:28,amp:0.06,freq:0.17,speed:0.38,flow:[0.12,0.4],spec:1.05,
    deep:0x0b2018,shallow:0x214c36,skyc:0x2a5442,moonDir:[50,90,-150],y:-0.2});
  water.mesh.scale.set(0.8,1,0.6); water.mesh.position.set(-4,-0.2,-6); g.add(water.mesh);
  const rim=makePondRimZLJ({rx:10.5,rz:6.6,n:24,x:-4,z:-6,seed:75,y:0.02}); g.add(rim.g);
  const lotus=makeLotusWitherZLJ({n:15,w:24,d:14,x:-4,y:-0.2,z:-6,seed:41}); g.add(lotus.g);
  /* 篱边残菊（傲霜枝） */
  const chrys=makeChrysWitherZLJ({n:8,x:13,y:-1.2,z:-4,seed:43}); g.add(chrys.g);
  const fence=makeForeground({kind:'栏杆',w:16,h:1.8,n:3,color:0x0a120c,seed:45,rim:0.14,rimC:0x8fc9a8});
  fence.g.position.set(13,-1.0,-4); g.add(fence.g);
  const c1=makeCitrusTreeZLJ({h:4.6,seed:137,scale:0.95}); c1.g.position.set(20,-1.2,-22); g.add(c1.g);
  const motes=makeGlow({n:36,box:[160,24,84],pos:[0,8,-20],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,26,110],pos:[0,8,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060c08,seed:47,rim:0.14,rimC:0xa8cf8f});
  fg.g.position.set(-14,-1.4,16); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:49,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(15,-1.3,14); g.add(fg2.g);
  addLights(g,{c:0xc8d0a0,i:0.44,p:[-40,78,22]},{c:0x1c2a1e,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(3,0.3,0.08); }};
}
function bChengju(){ // 二（末境·可点击）· 橙黄橘绿 —— 一年好景君须记，最是橙黄橘绿时
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,lit:0};
  const grd=makeGround({r:240,c1:0x0c1710,c2:0x16281a,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:32,layers:3,peaks:5,seed:1131,color:0x0b160f,atmo:0x2f4a34,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-9});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 残荷与残菊：点击后「褪去」 */
  const water=makeWater({size:32,seg:26,amp:0.06,freq:0.17,speed:0.38,flow:[0.12,0.4],spec:1.05,
    deep:0x0b2018,shallow:0x214c36,skyc:0x2a5442,moonDir:[50,90,-150],y:-0.2});
  water.mesh.scale.set(0.7,1,0.5); water.mesh.position.set(-9,-0.2,-8); g.add(water.mesh);
  const rim=makePondRimZLJ({rx:8.4,rz:5.2,n:20,x:-9,z:-8,seed:77,y:0.02}); g.add(rim.g);
  const lotus=makeLotusWitherZLJ({n:12,w:20,d:12,x:-9,y:-0.2,z:-8,seed:53}); g.add(lotus.g);
  const chrys=makeChrysWitherZLJ({n:6,x:-13,y:-1.2,z:-2,seed:57}); g.add(chrys.g);
  /* 橙橘园：两株树 + 满树果实（近景主体） */
  const c1=makeCitrusTreeZLJ({h:5.4,seed:139,scale:1.15}); c1.g.position.set(1.5,-1.2,-6.5); g.add(c1.g);
  const c2=makeCitrusTreeZLJ({h:4.8,seed:149,scale:1.0}); c2.g.position.set(11,-1.2,-9); g.add(c2.g);
  const fruitPos=[];
  for(let i=0;i<c1.fruits.length;i+=6){ const f=c1.fruits[i]; fruitPos.push([f[0]+1.5,f[1]-1.2,f[2]-6.5]); }
  for(let i=0;i<c2.fruits.length;i+=7){ const f=c2.fruits[i]; fruitPos.push([f[0]+11,f[1]-1.2,f[2]-9]); }
  const glow=makeFruitGlowZLJ({pos:fruitPos,lx:4.5,ly:2.0,lz:-7,lightMax:1.25}); g.add(glow.g);
  /* 诗人与友人：树下指点橙橘（二人） */
  const poet=makeFigure({pose:'独立',robe:0x2f4a3a,belt:0xa8cf8f,collar:0xeef4e6,hat:'幞头',
    hair:0x14181f,scale:1.14,rim:0.50,rimC:0xcae8a8,noProp:true});
  poet.position.set(-2.6,-1.0,-3.4); poet.rotation.y=-0.8; g.add(poet);
  const friend=makeFigure({pose:'独立',robe:0x3a4a3a,belt:0x8fc9a8,collar:0xeef4e6,hat:'幞头',
    hair:0x14181f,scale:1.08,rim:0.44,rimC:0xcae8a8,noProp:true});
  friend.position.set(-4.9,-1.0,-3.0); friend.rotation.y=-0.5; g.add(friend);
  const motes=makeGlow({n:38,box:[160,24,84],pos:[0,8,-18],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,26,110],pos:[0,8,-46],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060c08,seed:59,rim:0.14,rimC:0xa8cf8f});
  fg.g.position.set(-15,-1.3,13); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x071009,seed:61,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(14,-1.2,11); g.add(fg2.g);
  addLights(g,{c:0xd0d8a0,i:0.46,p:[-42,80,22]},{c:0x1c2a1e,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.lit=Math.min(1,ctl.lit+dt/2.0);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const lit=ctl.lit+0.5*ctl.pulse;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      /* 荷枯菊残褪去：基座 = 运行期最大值（0.92 / 0.94），每帧乘 fadeK */
      lotus.mat.opacity=k*0.92*(1-0.88*ctl.lit);
      chrys.mat.opacity=k*0.94*(1-0.86*ctl.lit);
      glow.update(t,k,lit);
      poet.update(t,k); friend.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(4,0.00,0.13); pluck(5,0.26,0.11); pluck(2,0.55,0.09);
        const fl=$('#flash'); fl.textContent='橙黄橘绿'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：果园再亮一分 */
    },clicked:false};
  return api;
}
