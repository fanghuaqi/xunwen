/* ================= 三衢道中 · 三境场景（青绿春晓 · 三衢山行变体：卷首梅黄山道、梅黄溪尽、绿阴黄鹂）
   本诗专属系统「不减·添得」：绿荫夹道的归途与枝头黄鹂；末境点击黄鹂 → 四五声啼鸣（音阶）+
   绿阴深处光影摇动（叶影摆动、光斑明灭），题字「绿阴黄鹂」。
   与同赛道《赠刘景文》（初冬园圃）、《画菊》（篱菊北风）不同：本页是初夏梅黄、溪舟与绿荫山道。 ================= */

/* —— 梅树：枝干 + 叶 + 黄熟梅子（合批 1 mesh；梅子黄时是本页的时令标志） —— */
function makePlumTreeSQ(o){
  o=o||{};
  const h=o.h===undefined?4.8:o.h, R=seedRnd(o.seed===undefined?281:o.seed);
  const wood=o.wood===undefined?0x3a2e1c:o.wood, leaf=o.leaf===undefined?0x2f5a2c:o.leaf;
  const fruit=o.fruit===undefined?0xe0b23a:o.fruit;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.46,0],h*0.07,h*0.03,7),wood);
  const tips=[];
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.34+R()*0.26);
    const p1=[Math.sin(a)*len,h*0.44+len*0.5,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.44,0],p1,h*0.028,h*0.011,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.8){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5,p1[1]+len*0.33,p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.013,h*0.005,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<5;k++){      /* 浓叶 */
      const lf=new THREE.PlaneGeometry(0.72,0.30);
      lf.rotateZ((R()-0.5)*0.9); lf.rotateY(R()*6.283);
      lf.translate(tp[0]+(R()-0.5)*1.2,tp[1]+(R()-0.35)*0.8,tp[2]+(R()-0.5)*1.2);
      B.put(lf,shadeColor(leaf,0.78+R()*0.5));
    }
    for(let k=0;k<3;k++){      /* 黄熟梅子 */
      const rr=0.16+R()*0.07;
      const fr=new THREE.SphereGeometry(rr,8,6);
      fr.translate(tp[0]+(R()-0.5)*1.1,tp[1]-(0.3+R()*0.6),tp[2]+(R()-0.5)*1.1);
      B.put(fr,shadeColor(fruit,0.85+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a5a3a,emissive:0x101408,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa8d8a0:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.015+0.03*wd)*Math.sin(t*0.7+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 绿阴：浓密树冠（大团叶簇，压暗；归途绿荫的主要体积），合批 1 mesh —— */
function makeCanopySQ(o){
  o=o||{};
  const n=o.n===undefined?26:o.n, R=seedRnd(o.seed===undefined?283:o.seed);
  const w=o.w===undefined?40:o.w, h=o.h===undefined?7:o.h, d=o.d===undefined?16:o.d;
  const B=new GeoBag();
  const cols=[0x2b5228,0x33602f,0x24461f,0x3a6a33];
  for(let i=0;i<n;i++){
    const rr=2.0+R()*2.6;
    const s=new THREE.SphereGeometry(rr,7,6); s.scale(1.25,0.78,1.0);
    s.translate((R()-0.5)*w,o.y===undefined?0:o.y+h*R(),(R()-0.5)*d);
    B.put(s,shadeColor(cols[(i*3)%cols.length],0.8+R()*0.45));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a5a34,emissive:0x0c1408,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa8d8a0:o.rimC,i:0.24,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.008+0.022*wd)*Math.sin(t*0.55+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 溪与小舟：溪水（浅）+ 岸边系着的一叶小舟（"小溪泛尽"） —— */
function makeBoatSQ(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(4.4,0.55,1.5); hull.translate(0,0.28,0); B.put(hull,0x4a3a24);
  const bow=new THREE.ConeGeometry(0.75,1.2,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(2.2,0.32,0);
  B.put(bow,0x4a3a24);
  const stern=new THREE.ConeGeometry(0.72,1.1,4); stern.rotateY(Math.PI/4); stern.rotateZ(Math.PI/2); stern.translate(-2.2,0.32,0);
  B.put(stern,shadeColor(0x4a3a24,0.9));
  const seat=new THREE.BoxGeometry(1.2,0.12,1.2); seat.translate(-0.6,0.6,0); B.put(seat,0x5a4a30);
  const pole=new THREE.CylinderGeometry(0.05,0.06,3.4,6); pole.rotateZ(1.0); pole.translate(1.1,0.9,0.5); B.put(pole,0x6a5230);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a24,emissive:0x0a0806}),{c:o.rimC===undefined?0xc8b078:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const ph=seedRnd(o.seed===undefined?293:o.seed)()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.position.y=(o.y===undefined?0:o.y)+0.06*Math.sin(t*1.2+ph)*kk;
    g.rotation.z=0.03*Math.sin(t*0.9+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 山径：石磴小径（自近及远折上），合批 1 mesh —— */
function makePathSQ(o){
  o=o||{};
  const n=o.n===undefined?24:o.n, R=seedRnd(o.seed===undefined?307:o.seed);
  const w=o.w===undefined?3.6:o.w, B=new GeoBag();
  for(let i=0;i<n;i++){
    const st=new THREE.BoxGeometry(w*(1-i/n*0.35),0.34,w*0.85);
    st.translate((R()-0.5)*0.4,0.17+i*0.46,-i*1.25);
    B.put(st,shadeColor(0x8a8468,0.75+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x6a6a50,emissive:0x0e0e08}),{c:o.rimC===undefined?0xc8d8a8:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 黄鹂：黄羽黑枕的鸟（啼鸣时挺颈，合批 1 mesh） —— */
function makeWarblerSQ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0xe8c02a:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.26,8,6); body.scale(1.5,0.92,0.9); body.translate(0,0.26,0); B.put(body,c);
  const rump=new THREE.SphereGeometry(0.17,7,6); rump.scale(1.2,0.9,0.9); rump.translate(-0.30,0.22,0);
  B.put(rump,shadeColor(c,0.85));
  const head=new THREE.SphereGeometry(0.16,8,6); head.translate(0.30,0.44,0); B.put(head,shadeColor(c,1.08));
  const mask=new THREE.BoxGeometry(0.30,0.09,0.20); mask.translate(0.34,0.44,0); B.put(mask,0x2a2418);
  const beak=new THREE.ConeGeometry(0.045,0.18,5); beak.rotateZ(-Math.PI/2); beak.translate(0.50,0.42,0); B.put(beak,0x6a5638);
  const wing=new THREE.SphereGeometry(0.16,7,6); wing.scale(1.3,0.4,0.85); wing.translate(-0.06,0.38,0.14);
  B.put(wing,shadeColor(0x9a9a58,1.1));
  const tail=new THREE.ConeGeometry(0.09,0.5,5); tail.rotateZ(1.3); tail.translate(-0.5,0.3,0); B.put(tail,shadeColor(c,0.9));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x8a8a58,emissive:0x181404,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe8e0a0:o.rimC,i:0.42,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?311:o.seed)()*6.283;
  g.update=function(t,k,sing){
    const kk=k===undefined?1:k, sg=sing===undefined?0:sing;
    g.rotation.z=0.06*Math.sin(t*1.1+ph)*kk;
    g.rotation.y=(o.ry===undefined?0:o.ry)+0.25*sg*Math.sin(t*6.0+ph);
    g.scale.setScalar(s*(1+0.12*sg*Math.max(0,Math.sin(t*5.0+ph))));
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 叶隙光斑：地面上的斑驳光点（点击后随叶影摇动、明灭；只调 scale） —— */
function makeDappleSQ(o){
  o=o||{};
  const n=o.n===undefined?22:o.n, R=seedRnd(o.seed===undefined?313:o.seed);
  const w=o.w===undefined?30:o.w, d=o.d===undefined?16:o.d;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf0f4c0,transparent:true,
      opacity:0.22,depthWrite:false,blending:THREE.AdditiveBlending}));
    const sc=0.7+R()*1.6;
    s.position.set((R()-0.5)*w,(o.y===undefined?0.12:o.y),(R()-0.5)*d);
    s.scale.set(sc,sc*0.6,1); s.renderOrder=3; g.add(s);
    items.push({s:s,base:sc,ph:R()*6.283});
  }
  g.position.set(o.x===undefined?0:o.x,0,o.z===undefined?0:o.z);
  return {g,items,update:function(t,vig){
    const vg=vig===undefined?0:vig;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const k2=(0.7+0.5*vg)*(0.75+0.25*Math.sin(t*(0.9+2.4*vg)+it.ph));
      const dx=0.6*vg*Math.sin(t*(1.1+1.8*vg)+it.ph);
      it.s.scale.set(it.base*k2,it.base*k2*0.6,1);
      it.s.position.x+=dx*0.004;
    }
  }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 梅黄山道 —— 初夏晴日、梅树成行、石径折上
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e1c14,c2:0x18301e,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:38,layers:3,peaks:5,seed:1611,color:0x0f2015,atmo:0x35543a,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-11});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const trees=[];
  [[-10,0,-16],[-1,0,-22],[8,0,-14],[16,0,-24]].forEach(function(p,i){
    const t=makePlumTreeSQ({h:5.0,seed:321+i*11,scale:1.05}); t.g.position.set(p[0],-1.3,p[2]); g.add(t.g); trees.push(t);
  });
  const path=makePathSQ({n:22,w:4.0,x:-2,y:-1.3,z:4,ry:0.1}); g.add(path.g);
  const canopy=makeCanopySQ({n:20,w:44,h:7,d:18,seed:325,scale:1.0}); canopy.g.position.set(-4,5.0,-20); g.add(canopy.g);
  const dap=makeDappleSQ({n:18,w:26,d:14,x:-2,z:0,y:0.02}); g.add(dap.g);
  const motes=makeGlow({n:42,box:[170,26,86],pos:[0,9,-22],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,100],pos:[0,8,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x060c08,seed:61,rim:0.14,rimC:0xa8d8a0});
  fg.g.position.set(-15,-1.5,32); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:63,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(16,-1.4,22); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-40,80,26]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    const wind=0.3+0.2*Math.sin(t*0.4);
    for(let i=0;i<trees.length;i++)trees[i].update(t,k,wind);
    canopy.update(t,k,wind); dap.update(t,0.1);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bMeihuang(){ // 一 · 梅黄溪尽 —— 梅子黄时日日晴，小溪泛尽却山行
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e1c14,c2:0x18301e,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:40,layers:3,peaks:5,seed:1621,color:0x0f2015,atmo:0x365438,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-11});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 小溪（画面右侧）与小舟 */
  const water=makeWater({size:44,seg:30,amp:0.08,freq:0.18,speed:0.5,flow:[0.2,0.6],spec:1.2,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.2});
  water.mesh.scale.set(0.8,1,0.55); water.mesh.position.set(9,-0.2,-10); g.add(water.mesh);
  const boat=makeBoatSQ({x:8.5,y:-0.15,z:-6.5,ry:0.4,seed:297}); g.add(boat.g);
  /* 山径自溪边折上（却山行） */
  const path=makePathSQ({n:22,w:3.8,x:-4,y:-1.2,z:6,ry:-0.28}); g.add(path.g);
  /* 梅子黄时：梅树成行 */
  const trees=[];
  [[-13,0,-10],[-6,0,-16],[1,0,-9],[7,0,-20],[14,0,-16]].forEach(function(p,i){
    const t=makePlumTreeSQ({h:5.2,seed:331+i*13,scale:1.05}); t.g.position.set(p[0],-1.2,p[2]); g.add(t.g); trees.push(t);
  });
  const canopy=makeCanopySQ({n:18,w:40,h:6,d:16,seed:337,scale:0.95}); canopy.g.position.set(-10,4.6,-16); g.add(canopy.g);
  const dap=makeDappleSQ({n:16,w:24,d:12,x:-3,z:2,y:0.02}); g.add(dap.g);
  const crowd=makeCrowd({n:2,rect:[-4,-30,14,6],seed:341,color:0x141c14,rimC:0xa8d8a0,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:40,box:[160,24,84],pos:[0,9,-20],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,100],pos:[0,8,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060c08,seed:65,rim:0.14,rimC:0xa8d8a0});
  fg.g.position.set(-14,-1.4,20); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:67,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(15,-1.3,17); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-38,78,24]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); crowd.update(t);
      const wind=0.35+0.25*Math.sin(t*0.45);
      for(let i=0;i<trees.length;i++)trees[i].update(t,k,wind);
      canopy.update(t,k,wind); dap.update(t,0.15); boat.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.3,0.09); pluck(5,0.9,0.08); }};
}
function bLvyin(){ // 二（末境·可点击）· 绿阴黄鹂 —— 绿阴不减来时路，添得黄鹂四五声
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,sing:0};
  const grd=makeGround({r:250,c1:0x0d1a12,c2:0x172c1c,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:2,peaks:5,seed:1631,color:0x0e1e14,atmo:0x33503a,
    fogK:0.60,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 绿阴夹道：两侧浓密树冠 + 成排树木 */
  const canopyL=makeCanopySQ({n:22,w:44,h:8,d:10,seed:347,scale:1.15}); canopyL.g.position.set(-14,4.2,-16); g.add(canopyL.g);
  const canopyR=makeCanopySQ({n:22,w:44,h:8,d:10,seed:349,scale:1.15}); canopyR.g.position.set(15,4.6,-17); g.add(canopyR.g);
  const trees=[];
  [[-15,0,-6],[-8,0,-12],[9,0,-8],[16,0,-14]].forEach(function(p,i){
    const t=makePlumTreeSQ({h:5.4,seed:351+i*11,scale:1.1}); t.g.position.set(p[0],-1.2,p[2]); g.add(t.g); trees.push(t);
  });
  const path=makePathSQ({n:24,w:4.2,x:0,y:-1.2,z:5,ry:0.0}); g.add(path.g);
  /* 黄鹂四五只：枝头啼鸣 */
  const birds=[];
  /* 黄鹂立在树冠之前、树干之上：避开树冠球体才读得出来 */
  [[-8.5,3.6,-5.0,1.6,353],[-3.4,4.0,-6.0,-1.2,357],[6.0,3.8,-4.6,1.1,359],[10.8,4.2,-6.4,1.4,361]].forEach(function(b){
    const bd=makeWarblerSQ({scale:1.6,seed:b[4],ry:b[3]});
    bd.g.position.set(b[0],b[1],b[2]); g.add(bd.g); birds.push(bd);
  });
  const dap=makeDappleSQ({n:26,w:30,d:16,x:0,z:1,y:0.03}); g.add(dap.g);
  const motes=makeGlow({n:42,box:[160,24,84],pos:[0,9,-18],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,96],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x060c08,seed:71,rim:0.14,rimC:0xa8d8a0});
  fg.g.position.set(-13,-1.4,15); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x071009,seed:73,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(13,-1.3,13); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-36,76,22]},{c:0x22301f,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.sing=Math.min(1,ctl.sing+dt/1.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const sg=ctl.sing+0.6*ctl.pulse;
      const wind=0.4+0.5*sg;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      canopyL.update(t,k,wind); canopyR.update(t,k,wind);
      for(let i=0;i<trees.length;i++)trees[i].update(t,k,wind);
      for(let i=0;i<birds.length;i++)birds[i].update(t,k,sg);
      dap.update(t,sg);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(4,0.16,0.11); pluck(5,0.34,0.10); pluck(3,0.52,0.09); pluck(5,0.74,0.08);
        const fl=$('#flash'); fl.textContent='绿阴黄鹂'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：黄鹂再啼几声，叶影再摇一阵 */
    },clicked:false};
  return api;
}
