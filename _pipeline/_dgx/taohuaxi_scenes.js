/* ================= 桃花溪 · 三境场景（水墨夜思 · 桃源问津变体：卷首溪山野烟、飞桥石矶、桃花清溪）
   本诗专属系统「问津」：野烟迷离中飞桥隐现、桃花尽日随流水、洞口在清溪何处边。
   末境点击清溪 → 野烟散处飞桥隐现（烟片缩小、桥面现出）、桃花随流水溯溪而上（流向反转）、
   云烟深处洞口微现，题字「洞在清溪何处边」。
   与同赛道《淮中晚泊犊头》《渡汉江》《题临安邸》并排：本页是野烟、飞桥、石矶与桃源之问。 ================= */

/* —— 飞桥：凌空高架的桥（拱 + 桥面 + 栏板 + 桥亭），可"隐现" —— */
function makeFlyingBridgeTH(o){
  o=o||{};
  const span=o.span===undefined?26:o.span, w=o.w===undefined?5:o.w, rh=o.rh===undefined?4.4:o.rh;
  const stone=o.stone===undefined?0x2a3240:o.stone;
  const B=new GeoBag();
  /* 桥拱：两段弧用折线拼 */
  for(let i=0;i<5;i++){
    const x=-span/2+span*(i+0.5)/5;
    const y=rh*(1-Math.pow(x/(span/2),2)*0.6)+0.3;
    const seg=new THREE.BoxGeometry(span/5+0.4,0.55,w);
    seg.rotateZ(-Math.atan2(1.6*x/(span/2)*rh/(span/4),1)*0.5);
    seg.translate(x,y,0);
    B.put(seg,shadeColor(stone,0.9+i*0.05));
  }
  /* 栏板与栏柱 */
  for(let i=0;i<=10;i++){
    const x=-span/2+span*i/10, y=rh*(1-Math.pow(x/(span/2),2)*0.6)+1.2;
    [1,-1].forEach(function(s){
      const p=new THREE.BoxGeometry(0.24,1.0,0.24); p.translate(x,y,s*w*0.44); B.put(p,shadeColor(stone,1.08));
    });
  }
  [1,-1].forEach(function(s){
    for(let i=0;i<10;i++){
      const x=-span/2+span*(i+0.5)/10, y=rh*(1-Math.pow(x/(span/2),2)*0.6)+1.65;
      const r=new THREE.BoxGeometry(span/10+0.06,0.18,0.16); r.translate(x,y,s*w*0.44); B.put(r,shadeColor(stone,1.18));
    }
  });
  /* 桥亭：一顶小方亭（"飞桥"凌空之感） */
  const pav=new THREE.ConeGeometry(w*0.9,2.0,4); pav.rotateY(Math.PI/4); pav.translate(0,rh+3.2,0); B.put(pav,0x232a36);
  [1,-1].forEach(function(s){
    const c=new THREE.CylinderGeometry(0.16,0.18,1.6,8); c.translate(s*w*0.4,rh+2.6,0); B.put(c,shadeColor(stone,1.1));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4454,emissive:0x080c12}),{c:o.rimC===undefined?0xa4b6cc:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 石矶：溪中突出的巨石（可问渔船之处），合批 1 mesh —— */
function makeStoneJettyTH(o){
  o=o||{};
  const s=o.s===undefined?1:o.s, R=seedRnd(o.seed===undefined?1201:o.seed);
  const B=new GeoBag();
  const main=new THREE.BoxGeometry(5.2,2.0,3.6); main.rotateY(0.2); main.translate(0,1.0,0); B.put(main,0x3a4250);
  const top=new THREE.BoxGeometry(4.4,0.7,3.0); top.rotateY(0.35); top.translate(0.2,2.2,0.1); B.put(top,shadeColor(0x46505e,1.1));
  for(let i=0;i<5;i++){
    const r=new THREE.ConeGeometry(0.5+R()*0.5,0.8+R()*0.9,5);
    r.rotateZ((R()-0.5)*1.2); r.rotateX((R()-0.5)*1.2);
    r.translate((R()-0.5)*5,0.6+R()*1.2,(R()-0.5)*3.2); B.put(r,shadeColor(0x323a46,0.9+R()*0.3));
  }
  /* 矶上青苔与草 */
  for(let i=0;i<26;i++){
    const g2=new THREE.ConeGeometry(0.05,0.3+R()*0.4,4);
    g2.rotateZ((R()-0.5)*0.5); g2.translate((R()-0.5)*4.2,2.5,(R()-0.5)*2.8);
    B.put(g2,shadeColor(0x3a5538,0.8+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a5464,emissive:0x080c10}),{c:o.rimC===undefined?0xa4b6cc:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 渔船：小渔船 + 渔人（问讯的对象） —— */
function makeFishingBoatTH(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(3.6,0.5,1.3); hull.translate(0,0.26,0); B.put(hull,0x3a3428);
  const bow=new THREE.ConeGeometry(0.66,1.1,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(1.8,0.3,0);
  B.put(bow,0x3a3428);
  const stern=new THREE.ConeGeometry(0.64,1.0,4); stern.rotateY(Math.PI/4); stern.rotateZ(Math.PI/2); stern.translate(-1.8,0.3,0);
  B.put(stern,shadeColor(0x3a3428,0.9));
  const canopy=new THREE.CylinderGeometry(0.7,0.7,1.4,10,1,true,0,Math.PI); canopy.rotateZ(Math.PI/2); canopy.rotateY(Math.PI/2);
  canopy.translate(-0.8,0.66,0); B.put(canopy,0x4a4230);
  const oar=new THREE.CylinderGeometry(0.045,0.045,2.4,6); oar.rotateZ(1.4); oar.translate(0.4,0.7,0.4); B.put(oar,0x6a5a38);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a4030,emissive:0x080a08,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa4b6cc:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const fisher=makeFigure({pose:'独立',robe:0x3f4436,belt:0x7a6a44,collar:0xc8c8b8,hat:'斗笠',
    hair:0x2a2620,scale:0.98,rim:0.34,rimC:0xa8bccc,noProp:true});
  fisher.position.set(0.5,0.52,0); fisher.rotation.y=0.4; g.add(fisher);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const ph=seedRnd(o.seed===undefined?1207:o.seed)()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.position.y=(o.y===undefined?0:o.y)+0.05*Math.sin(t*1.1+ph)*kk;
    g.rotation.z=0.03*Math.sin(t*0.85+ph)*kk;
    fisher.update(t,kk); };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 桃树：深粉桃花（溪畔成行） —— */
function makePeachTreeTH(o){
  o=o||{};
  const h=o.h===undefined?4.4:o.h, R=seedRnd(o.seed===undefined?1211:o.seed);
  const wood=o.wood===undefined?0x2e2620:o.wood, petal=o.petal===undefined?0xd878a0:o.petal;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.48,0],h*0.06,h*0.026,7),wood);
  const tips=[];
  for(let i=0;i<6;i++){
    const a=i/6*6.283+R()*0.6, len=h*(0.34+R()*0.28);
    const p1=[Math.sin(a)*len,h*0.46+len*0.46,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.46,0],p1,h*0.026,h*0.011,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.75){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5,p1[1]+len*0.32,p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.013,h*0.005,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<5;k++){
      const rr=0.18+R()*0.1;
      const fl=new THREE.SphereGeometry(rr,7,6); fl.scale(1.15,0.8,1.05);
      fl.translate(tp[0]+(R()-0.5)*1.0,tp[1]+(R()-0.35)*0.7,tp[2]+(R()-0.5)*1.0);
      B.put(fl,shadeColor(petal,0.82+R()*0.35));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:9,
    specular:0x6a6474,emissive:0x1c0e18,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xd8a8c0:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.014+0.03*wd)*Math.sin(t*0.6+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 花瓣随流水：InstancedMesh 花瓣沿溪漂流（dir 反转即"溯溪而上"） —— */
function makePetalFlowTH(o){
  o=o||{};
  const n=o.n===undefined?120:o.n, R=seedRnd(o.seed===undefined?1217:o.seed);
  const w=o.w===undefined?12:o.w, len=o.len===undefined?40:o.len;
  const y0=o.y===undefined?-0.15:o.y, z0=o.z===undefined?-4:o.z;
  const geo=new THREE.SphereGeometry(0.09,5,4); geo.scale(1.8,0.28,1.0);
  const mat=new THREE.MeshBasicMaterial({color:0xe0a0c0,transparent:true,opacity:0.75,depthWrite:false,side:THREE.DoubleSide});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({u:R(), v:(R()-0.5)*w, ph:R()*6.283, sp:0.5+R()*0.8, sc:0.7+R()*0.7});
  }
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh,mat,update:function(t,k,speed){
    const kk=k===undefined?1:k, sp0=speed===undefined?1:speed;   /* speed<0 → 溯溪而上 */
    for(let i=0;i<n;i++){
      const it=items[i];
      let u=(it.u+t*0.06*it.sp*sp0)%1; u=(u+1)%1;
      const z=z0+u*len;                       /* 自上游（远）漂向下游（近） */
      const x=Math.sin(z*0.18+it.ph)*2.2+it.v*0.4;
      dm.position.set(x,y0+0.05*Math.sin(t*1.4+it.ph),z);
      dm.rotation.set(Math.sin(t*1.1+it.ph)*0.8,it.ph+t*0.6,Math.sin(t*0.9+it.ph)*1.1);
      dm.scale.setScalar(it.sc);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* —— 野烟：溪上的野雾（片状 sprites；点击清溪后缩小"散去"） —— */
function makeWildSmokeTH(o){
  o=o||{};
  const n=o.n===undefined?16:o.n, R=seedRnd(o.seed===undefined?1223:o.seed);
  const sp=o.spread===undefined?[190,9,70]:o.spread, pos=o.pos===undefined?[0,6,-30]:o.pos;
  const sc=o.scale===undefined?38:o.scale, col=o.color===undefined?0x2c3a4a:o.color;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:col,transparent:true,
      opacity:0.30*(0.6+R()*0.7),depthWrite:false}));
    s.position.set(pos[0]+(R()-0.5)*sp[0],pos[1]+(R()-0.5)*sp[1],pos[2]+(R()-0.5)*sp[2]);
    const k=sc*(0.7+R()*0.8);
    s.scale.set(k,k*0.4,1); s.renderOrder=5;
    g.add(s); items.push({s:s,base:[k,k*0.4],ph:R()*6.283});
  }
  return {g,items,update:function(t,cleared){
    const cl=cleared===undefined?0:cleared;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const w=(1-0.72*cl)*(1+0.05*Math.sin(t*0.2+it.ph));
      it.s.scale.set(it.base[0]*w,it.base[1]*w,1);
      it.s.position.x=it.s.position.x;      /* 只缩不放，不写 opacity */
    }
  }};
}

/* —— 洞口：云烟深处的桃源洞（暗色洞口 + 一线微光） —— */
function makeCaveMouthTH(o){
  o=o||{};
  const g=new THREE.Group();
  const rockB=new GeoBag();
  const m1=new THREE.BoxGeometry(6.4,7.2,2.6); m1.translate(0,3.6,0); rockB.put(m1,0x2a3240);
  [-1,1].forEach(function(s){
    const m=new THREE.BoxGeometry(2.6,5.2,3.0); m.rotateZ(s*0.18); m.translate(s*3.4,2.6,0.2); rockB.put(m,0x323a48);
  });
  const m2=new THREE.BoxGeometry(8.4,1.4,3.2); m2.translate(0,7.8,0); rockB.put(m2,0x3a4250);
  const rock=rockB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    emissive:0x06080c}));
  rock.frustumCulled=false; g.add(rock);
  /* 洞口（暗） */
  const hole=new THREE.Mesh(new THREE.CylinderGeometry(1.3,1.5,0.6,14,1,false,0,Math.PI),
    new THREE.MeshBasicMaterial({color:0x0a0e14}));
  hole.rotation.x=Math.PI/2; hole.rotation.z=Math.PI; hole.position.set(0,1.9,1.4); g.add(hole);
  /* 洞口微光（只调 scale） */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfd8e4,transparent:true,
    opacity:0.22,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.position.set(0,2.0,1.6); glow.scale.set(4.4,3.6,1); glow.renderOrder=3; g.add(glow);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?-52:o.z);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,glow,update:function(t,show){
    const sh=show===undefined?0:show;
    const s=0.5+0.9*sh;
    glow.scale.set(4.4*s,3.6*s,1);
    g.position.y=(o.y===undefined?0:o.y)+0.3*show;
  }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 溪山野烟 —— 野烟弥漫、飞桥隐约、两岸桃花
  const g=new THREE.Group();
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c24,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:52,layers:3,peaks:6,seed:2411,color:0x0a0f16,atmo:0x1f2a38,
    fogK:0.64,glowK:0.04,glow:0x9fb3cc,y:-13});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  const water=makeWater({size:110,seg:40,amp:0.07,freq:0.13,speed:0.45,flow:[0.25,0.6],spec:1.3,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2c3e54,moonDir:[-40,90,-160],y:-0.5});
  water.mesh.scale.set(1,1,0.62); water.mesh.position.set(0,-0.5,-22); g.add(water.mesh);
  const bridge=makeFlyingBridgeTH({span:26,w:5,rh:4.4,x:-6,y:-0.4,z:-34,ry:0.1}); g.add(bridge.g);
  const peaches=[];
  [[-14,0,-12,1229],[-7,0,-18,1231],[8,0,-14,1237],[16,0,-20,1241]].forEach(function(p){
    const t=makePeachTreeTH({h:4.6,seed:p[3],scale:1.1}); t.g.position.set(p[0],-1.4,p[2]); g.add(t.g); peaches.push(t);
  });
  const smoke=makeWildSmokeTH({n:16,pos:[0,6,-30],scale:40,seed:1219}); g.add(smoke.g);
  const cave=makeCaveMouthTH({x:2,y:-1.4,z:-56,scale:0.9}); g.add(cave.g);
  const motes=makeGlow({n:44,box:[200,26,92],pos:[0,9,-26],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[250,28,120],pos:[0,9,-56],scale:80,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:19,d:7,color:0x070a0d,seed:193,rim:0.16,rimC:0xa4b6cc});
  fg.g.position.set(-18,-1.5,40); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x090d10,seed:197,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(17,-1.4,26); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-44,70,28]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    smoke.update(t,0.1); cave.update(t,0.15);
    const wd=0.3+0.15*Math.sin(t*0.4);
    for(let i=0;i<peaches.length;i++)peaches[i].update(t,k,wd);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bFeiqiao(){ // 一 · 飞桥石矶 —— 隐隐飞桥隔野烟，石矶西畔问渔船
  const g=new THREE.Group();
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c24,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:50,layers:3,peaks:6,seed:2421,color:0x0a0f16,atmo:0x1e2836,
    fogK:0.64,glowK:0.04,glow:0x9fb3cc,y:-13});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  const water=makeWater({size:120,seg:42,amp:0.08,freq:0.12,speed:0.48,flow:[0.25,0.6],spec:1.35,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2c3e54,moonDir:[-40,90,-160],y:-0.5});
  water.mesh.scale.set(1,1,0.6); water.mesh.position.set(0,-0.5,-24); g.add(water.mesh);
  /* 飞桥在远处（野烟之中） */
  const bridge=makeFlyingBridgeTH({span:30,w:5.2,rh:4.8,x:-4,y:-0.4,z:-38,ry:0.06}); g.add(bridge.g);
  /* 石矶近景（溪中巨石，"问渔船"之处） */
  const jetty=makeStoneJettyTH({x:-6.5,y:-0.9,z:-3,s:1.25,seed:1205,ry:0.3}); g.add(jetty.g);
  /* 渔船泊在石矶西畔 */
  const boat=makeFishingBoatTH({x:-1.2,y:-0.35,z:-5.5,ry:0.5,seed:1209}); g.add(boat.g);
  const peaches=[];
  [[-15,0,-10,1247],[-8,0,-14,1249],[9,0,-12,1253],[16,0,-18,1259]].forEach(function(p){
    const t=makePeachTreeTH({h:4.8,seed:p[3],scale:1.1}); t.g.position.set(p[0],-1.3,p[2]); g.add(t.g); peaches.push(t);
  });
  const smoke=makeWildSmokeTH({n:18,pos:[0,6,-32],scale:42,seed:1251}); g.add(smoke.g);
  const cave=makeCaveMouthTH({x:4,y:-1.3,z:-58,scale:0.95}); g.add(cave.g);
  const motes=makeGlow({n:42,box:[190,24,90],pos:[0,9,-24],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,26,110],pos:[0,9,-54],scale:78,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x070a0d,seed:199,rim:0.16,rimC:0xa4b6cc});
  fg.g.position.set(-16,-1.4,24); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x090d10,seed:211,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(16,-1.3,20); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-42,68,26]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      smoke.update(t,0.2); cave.update(t,0.2); boat.update(t,k);
      const wd=0.35+0.2*Math.sin(t*0.42);
      for(let i=0;i<peaches.length;i++)peaches[i].update(t,k,wd);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(2,0.4,0.08); pluck(4,0.9,0.07); }};
}
function bTaohua(){ // 二（末境·可点击）· 桃花清溪 —— 桃花尽日随流水，洞在清溪何处边
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,clear:0,dream:0,up:0};
  const grd=makeGround({r:280,c1:0x0b0f13,c2:0x141c24,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:48,layers:3,peaks:6,seed:2431,color:0x0a0f16,atmo:0x1e2836,
    fogK:0.62,glowK:0.04,glow:0x9fb3cc,y:-13});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 清溪（桃花随流水） */
  const water=makeWater({size:130,seg:44,amp:0.08,freq:0.12,speed:0.5,flow:[0.3,0.65],spec:1.4,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2c3e54,moonDir:[-40,90,-160],y:-0.5});
  water.mesh.scale.set(1,1,0.58); water.mesh.position.set(0,-0.5,-24); g.add(water.mesh);
  /* 石矶与渔船（近景） */
  const jetty=makeStoneJettyTH({x:-7,y:-0.9,z:-4,s:1.3,seed:1261,ry:0.25}); g.add(jetty.g);
  const boat=makeFishingBoatTH({x:-2,y:-0.35,z:-6,ry:0.45,seed:1263}); g.add(boat.g);
  /* 飞桥在远处烟中 */
  const bridge=makeFlyingBridgeTH({span:30,w:5.2,rh:4.8,x:-3,y:-0.4,z:-40,ry:0.05}); g.add(bridge.g);
  /* 两岸桃花 */
  const peaches=[];
  [[-14,0,-9,1267],[-9,0,-16,1273],[9,0,-11,1277],[15,0,-17,1279]].forEach(function(p){
    const t=makePeachTreeTH({h:5.0,seed:p[3],scale:1.15}); t.g.position.set(p[0],-1.3,p[2]); g.add(t.g); peaches.push(t);
  });
  /* 花瓣随流水（speed<0 → 溯溪而上） */
  const petals=makePetalFlowTH({n:130,w:14,len:42,y:-0.42,z:-4,x:1,seed:1283});
  g.add(petals.g);
  /* 洞口在云烟深处 */
  const cave=makeCaveMouthTH({x:5,y:-1.3,z:-62,scale:1.0}); g.add(cave.g);
  const smoke=makeWildSmokeTH({n:20,pos:[0,6,-34],scale:44,seed:1289}); g.add(smoke.g);
  const motes=makeGlow({n:42,box:[190,24,90],pos:[0,9,-26],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,26,110],pos:[0,9,-56],scale:78,color:0x22303c,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.2,w:17,d:7,color:0x070a0d,seed:213,rim:0.16,rimC:0xa4b6cc});
  fg.g.position.set(-15,-1.4,16); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x090d10,seed:217,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(15,-1.3,14); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-40,66,24]},{c:0x1a222c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.clear=Math.min(1,ctl.clear+dt/2.2);     /* 野烟散去 */
        ctl.up=Math.min(1,ctl.up+dt/3.0);           /* 花瓣由顺流转为溯溪 */
        ctl.dream=Math.min(1,ctl.dream+dt/3.4);     /* 洞口微现 */
      }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const cl=Math.min(1,ctl.clear+0.4*ctl.pulse);
      const dr=ctl.dream+0.3*ctl.pulse;
      /* 流向：+1 顺流 → −1 溯溪（用 smooth 过渡，避免突变） */
      const dir=1-2*Math.min(1,ctl.up+0.35*ctl.pulse);
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      smoke.update(t,cl); cave.update(t,dr);
      petals.update(t,k,dir);
      boat.update(t,k);
      const wd=0.35+0.5*cl;
      for(let i=0;i<peaches.length;i++)peaches[i].update(t,k,wd);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(4,0.25,0.10); pluck(2,0.55,0.09); pluck(3,0.85,0.08);
        const fl=$('#flash'); fl.textContent='洞在清溪何处边'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：烟再散一分，桃花再溯一程 */
    },clicked:false};
  return api;
}
