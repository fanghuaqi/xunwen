/* ================= 山园小梅 · 五境场景（水墨夜思 · 孤山梅影变体：卷首小园、众芳独妍、疏影暗香、霜禽粉蝶、微吟相狎）
   本诗专属系统「疏影暗香」：月下梅枝横斜、清浅水面上一道疏影；暗香是可见的银白香雾，缓缓浮动。
   末境点击暗香 → 水中疏影横斜摇动 + 暗香成雾漫开（诗眼「疏影横斜水清浅，暗香浮动月黄昏」）。
   与同赛道《忆秦娥》（秦楼月、西风陵阙）不同：本页是月下小园、浅水梅影与暗香。 ================= */

/* —— 梅树：横斜的枝干 + 白粉梅花（花团与五瓣花），合批 1 mesh —— */
function makePlumXM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19:o.seed), h=o.h===undefined?5.2:o.h;
  const wood=o.wood===undefined?0x241d22:o.wood;
  const petal=o.petal===undefined?0xf0e6ea:o.petal;
  const B=new GeoBag();
  const lean=o.lean===undefined?0.55:o.lean;
  const top=[lean*h*0.5,h,0];
  B.put(limbGeo([0,0,0],top,h*0.055,h*0.022,7),wood);
  const tips=[top];
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, t=0.34+0.5*(i/nb);
    const base=[lean*h*0.5*t, h*t, 0];
    const len=h*(0.30+R()*0.26);
    const p1=[base[0]+Math.sin(a)*len*0.9+(o.asym===undefined?0.35:o.asym), base[1]+len*0.42, base[2]+Math.cos(a)*len*0.6];
    B.put(limbGeo(base,p1,h*0.022,h*0.009,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.8){
      const p2=[p1[0]+Math.sin(a+0.7)*len*0.55, p1[1]+len*0.3, p1[2]+Math.cos(a+0.7)*len*0.5];
      B.put(limbGeo(p1,p2,h*0.012,h*0.005,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  /* 花：五瓣花片（向阳面）+ 花团小球 */
  const nf=o.flowers===undefined?3:o.flowers;
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<nf;k++){
      const cx=tp[0]+(R()-0.5)*h*0.16, cy=tp[1]+(R()-0.4)*h*0.12, cz=tp[2]+(R()-0.5)*h*0.16;
      const pr=h*0.030*(0.8+R()*0.6);
      for(let q=0;q<5;q++){
        const a=q/5*6.283+R()*0.3;
        const pf=new THREE.PlaneGeometry(pr*1.5,pr*0.95);
        pf.rotateZ(a); pf.rotateX(-0.4+R()*0.8); pf.rotateY(R()*0.6);
        pf.translate(cx+Math.cos(a)*pr*0.62, cy, cz+Math.sin(a)*pr*0.62);
        B.put(pf,shadeColor(petal,0.86+R()*0.28));
      }
      const st=new THREE.SphereGeometry(pr*0.24,6,5); st.translate(cx,cy+pr*0.1,cz);
      B.put(st,0xd8c060);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x8a94a8,emissive:0x141018,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xc9d3e0:o.rimC,i:0.30,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.014*Math.sin(t*0.45+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 众芳摇落：无花无叶的枯枝（众芳已凋） —— */
function makeBareTreeXM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?23:o.seed), h=o.h===undefined?3.6:o.h;
  const wood=o.wood===undefined?0x1a171c:o.wood, B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.6,0],h*0.035,h*0.014,6),wood);
  const nb=o.branches===undefined?5:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.6, len=h*(0.3+R()*0.28);
    const p1=[Math.sin(a)*len,(h*0.55)+len*0.5,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.55,0],p1,h*0.016,h*0.006,5),shadeColor(wood,1.2));
    if(R()<0.7){
      const p2=[p1[0]*1.35,p1[1]+len*0.34,p1[2]*1.35];
      B.put(limbGeo(p1,p2,h*0.008,h*0.003,4),shadeColor(wood,1.35));
    }
  }
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a5060,emissive:0x08080c}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mesh};
}

/* —— 水中疏影：清浅水面上一道横斜的梅影（贴水暗片，随风轻摇；末境点击后摇得更活） —— */
function makePlumShadowXM(o){
  o=o||{};
  const n=o.n===undefined?7:o.n, R=seedRnd(o.seed===undefined?31:o.seed);
  const g=new THREE.Group(), items=[];
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0x0a0e16:o.color,transparent:true,
    opacity:0.42,depthWrite:false,side:THREE.DoubleSide});
  for(let i=0;i<n;i++){
    const w=1.0+R()*2.6, h=0.14+R()*0.16;
    const pl=new THREE.Mesh(new THREE.PlaneGeometry(w,h),mat);
    pl.rotation.x=-Math.PI/2;
    pl.rotation.z=o.tilt===undefined?0.42:o.tilt;
    pl.position.set((R()-0.5)*9, 0.02+i*0.002, (R()-0.5)*5.5);
    pl.renderOrder=2; g.add(pl);
    items.push({pl:pl,ph:R()*6.283,base:pl.position.x});
  }
  g.position.y=o.y===undefined?0.03:o.y;
  return {g,items,mat,update:function(t,k,sway){
    const kk=k===undefined?1:k, sw=sway===undefined?0:sway;
    mat.opacity=kk*0.42;                     /* 基座 0.42 = 运行期最大值 */
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.pl.position.x=it.base+Math.sin(t*(0.5+1.6*sw)+it.ph)*(0.16+0.5*sw);
      it.pl.rotation.z=(o.tilt===undefined?0.42:o.tilt)+0.06*Math.sin(t*0.6+it.ph)*(1+2*sw);
    }
  }};
}

/* —— 霜禽：白羽水鸟（欲下未下、偷眼相看），合批 1 mesh —— */
function makeFrostBirdXM(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0xe8eef4:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,9,7); body.scale(1.7,0.95,0.9); body.translate(0,0.34,0); B.put(body,c);
  const neck=new THREE.CylinderGeometry(0.085,0.13,0.72,7); neck.rotateZ(-0.5); neck.translate(0.46,0.86,0);
  B.put(neck,shadeColor(c,1.05));
  const head=new THREE.SphereGeometry(0.15,8,6); head.translate(0.66,1.18,0); B.put(head,shadeColor(c,1.1));
  const beak=new THREE.ConeGeometry(0.05,0.30,6); beak.rotateZ(-Math.PI/2); beak.translate(0.90,1.15,0);
  B.put(beak,0xd8a038);
  const w1=new THREE.SphereGeometry(0.24,8,6); w1.scale(1.2,0.36,0.9); w1.translate(-0.10,0.46,0.16);
  B.put(w1,shadeColor(c,0.88));
  const w2=new THREE.SphereGeometry(0.24,8,6); w2.scale(1.2,0.36,0.9); w2.translate(-0.10,0.46,-0.16);
  B.put(w2,shadeColor(c,0.88));
  const tail=new THREE.ConeGeometry(0.12,0.5,6); tail.rotateZ(1.4); tail.translate(-0.6,0.4,0); B.put(tail,shadeColor(c,0.8));
  const leg1=new THREE.CylinderGeometry(0.035,0.03,0.5,5); leg1.translate(0.14,0.1,0.09); B.put(leg1,0x8a6a3a);
  const leg2=new THREE.CylinderGeometry(0.035,0.03,0.5,5); leg2.translate(0.14,0.1,-0.09); B.put(leg2,0x8a6a3a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:22,
    specular:0xa8b4c8,emissive:0x101620}),{c:o.rimC===undefined?0xd8e4f2:o.rimC,i:0.42,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?53:o.seed)()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.05*Math.sin(t*0.8+ph)*kk;
    g.rotation.y=(o.ry===undefined?0:o.ry)+0.05*Math.sin(t*0.4+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 粉蝶：半透的粉色蝶影（「如知合断魂」是设想之词，故只作虚影） —— */
function makeButterflyXM(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0xe8c0cc:o.color;
  const mat=new THREE.MeshPhongMaterial({color:c,transparent:true,opacity:0.50,shininess:6,
    emissive:0x2a1418,side:THREE.DoubleSide,depthWrite:false});
  const g=new THREE.Group();
  const w1=new THREE.Mesh(new THREE.PlaneGeometry(0.52,0.38),mat);
  w1.position.set(-0.24,0,0.12); g.add(w1);
  const w2=new THREE.Mesh(new THREE.PlaneGeometry(0.52,0.38),mat);
  w2.position.set(0.24,0,0.12); g.add(w2);
  const body=new THREE.Mesh(new THREE.CylinderGeometry(0.035,0.05,0.42,6),
    new THREE.MeshPhongMaterial({color:0x3a3038,shininess:10}));
  body.rotation.x=Math.PI/2; body.position.z=0.12; g.add(body);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?61:o.seed)()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.5*Math.sin(t*(3.4+ph)*1)*0.5*kk+0.5*Math.sin(t*4.2+ph)*kk*0.5;
    g.position.y=(o.y===undefined?0:o.y)+0.28*Math.sin(t*0.9+ph);
    g.rotation.y=(o.ry===undefined?0:o.ry)+0.5*Math.sin(t*0.5+ph);
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh:null,mat};
}

/* —— 暗香：月下若有若无的香雾（银白 Sprite 群，只调 scale；点击后成雾漫开） —— */
function makeScentXM(o){
  o=o||{};
  const n=o.n===undefined?10:o.n, sp=o.spread===undefined?[16,5,12]:o.spread;
  const pos=o.pos===undefined?[0,2.2,0]:o.pos, sc=o.scale===undefined?7:o.scale;
  const col=o.color===undefined?0xc9d3e0:o.color, op=o.op===undefined?0.13:o.op;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:col,transparent:true,
      opacity:op*(0.55+Math.random()*0.7),depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set(pos[0]+(Math.random()-0.5)*sp[0], pos[1]+(Math.random()-0.5)*sp[1], pos[2]+(Math.random()-0.5)*sp[2]);
    const k=sc*(0.65+Math.random()*0.9);
    s.scale.set(k,k*0.62,1); s.renderOrder=5;
    g.add(s); items.push({s:s,base:[k,k*0.62],ph:Math.random()*6.283,rise:0.4+Math.random()*0.9});
  }
  return {g,items,update:function(t,k,grow,rise){
    const kk=k===undefined?1:k, gr=grow===undefined?1:grow, ri=rise===undefined?0:rise;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const s2=1+0.07*Math.sin(t*0.3+it.ph);
      it.s.scale.set(it.base[0]*s2*gr, it.base[1]*s2*gr, 1);
      it.s.position.y=it.base ? (it.s.position.y) : it.s.position.y;
      it.s.position.y+=Math.sin(t*0.4+it.ph)*0.0025*kk+ri*0.004*it.rise;
      if(it.s.position.y>5.4)it.s.position.y=0.6;
    }
  }};
}

/* —— 小园矮墙：一道粉墙（合批 1 mesh，衬月色梅影） —— */
function makeGardenWallXM(o){
  o=o||{};
  const len=o.len===undefined?70:o.len, h=o.h===undefined?3.2:o.h;
  const R=seedRnd(o.seed===undefined?71:o.seed), B=new GeoBag();
  const wall=new THREE.BoxGeometry(len,h,0.7); wall.translate(0,h/2,0); B.put(wall,o.color===undefined?0x1a1d24:o.color);
  const cap=new THREE.BoxGeometry(len*1.01,0.26,0.95); cap.translate(0,h+0.13,0); B.put(cap,shadeColor(0x2a3038,1.05));
  for(let i=0;i<10;i++){
    const t=(i+0.5)/10;
    const tile=new THREE.BoxGeometry(len*0.075,0.16,1.0); tile.translate(-len/2+len*t,h+0.3,0);
    B.put(tile,shadeColor(0x323a44,0.8+R()*0.4));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x39434f,emissive:0x080a10}),{c:o.rimC===undefined?0x9fb0c8:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?-40:o.z);
  return {g,mesh};
}

/* ================= 五境 ================= */
function bCover(){ // 卷首 · 孤山小园 —— 月色下的小园矮墙、数株老梅、银雾一片
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0a0d13,c2:0x141a24,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:46,layers:3,peaks:5,seed:911,color:0x080b11,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x9fb3cc,y:-12});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  const wall=makeGardenWallXM({len:76,h:3.2,x:0,y:-1.4,z:-46}); g.add(wall.g);
  const plums=[];
  [[-15,0,-30],[-4,0,-26],[8,0,-32],[18,0,-24]].forEach(function(p,i){
    const m=makePlumXM({h:5.2,seed:101+i*17,scale:1.0,flowers:3}); m.g.position.set(p[0],-1.4,p[2]); g.add(m.g); plums.push(m);
  });
  const bare=[];
  [[-24,0,-20],[24,0,-18],[-32,0,-34]].forEach(function(p,i){
    const b=makeBareTreeXM({h:3.4,seed:131+i*11,scale:1.0}); b.g.position.set(p[0],-1.4,p[2]); g.add(b.g); bare.push(b);
  });
  const crowd=makeCrowd({n:3,rect:[-8,-40,20,8],seed:151,color:0x101620,rimC:0xc9d3e0,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:46,box:[200,30,110],pos:[0,9,-28],color:0xc9d3e0,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const myst=makeMist({n:8,spread:[250,32,140],pos:[0,10,-56],scale:82,color:0x22304a,op:0.12});
  g.add(myst.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.4,w:20,d:7,color:0x05070a,seed:37,rim:0.16,rimC:0xc9d3e0});
  fg.g.position.set(-18,-1.5,38); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:34,n:9,d:6,color:0x05070a,seed:39,sway:0.6,rim:0.14,rimC:0xc9d3e0});
  fg2.g.position.set(20,-1.4,32); fg2.g.rotation.z=-0.18; g.add(fg2.g);
  addLights(g,{c:0xc9d3e0,i:0.46,p:[-50,90,30]},{c:0x1a2230,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); myst.update(t,k); motes.update(t); crowd.update(t);
    for(let i=0;i<plums.length;i++)plums[i].update(t,k);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bZhongfang(){ // 一 · 众芳独妍 —— 众芳摇落独暄妍，占尽风情向小园
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0a0d13,c2:0x141a24,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:44,layers:3,peaks:5,seed:921,color:0x080b11,atmo:0x1e2939,
    fogK:0.62,glowK:0.05,glow:0x9fb3cc,y:-12});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const wall=makeGardenWallXM({len:80,h:3.4,x:0,y:-1.4,z:-48}); g.add(wall.g);
  /* 众芳摇落：满园枯枝（无花） */
  const bare=[];
  for(let i=0;i<9;i++){
    const b=makeBareTreeXM({h:2.8+((i*7)%3)*0.5,seed:141+i*13,scale:1.0});
    b.g.position.set(-24+i*6,-1.4,-26-((i%3)*4)); g.add(b.g); bare.push(b);
  }
  /* 独暄妍：一树梅花开到最盛 */
  const plum=makePlumXM({h:5.6,seed:107,scale:1.15,flowers:4}); plum.g.position.set(2,-1.4,-14); g.add(plum.g);
  const plum2=makePlumXM({h:4.6,seed:109,scale:0.95,flowers:3,asym:-0.3}); plum2.g.position.set(-8,-1.4,-18); g.add(plum2.g);
  const motes=makeGlow({n:44,box:[180,28,100],pos:[0,9,-24],color:0xc9d3e0,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const scent=makeScentXM({n:8,spread:[16,5,12],pos:[2,2.4,-14],scale:6.4,op:0.12});
  g.add(scent.g);
  const myst=makeMist({n:7,spread:[230,28,120],pos:[0,9,-50],scale:78,color:0x22304a,op:0.11});
  g.add(myst.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:7,color:0x05070a,seed:41,rim:0.16,rimC:0xc9d3e0});
  fg.g.position.set(-14,-1.5,20); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x060810,seed:43,sway:0.9,tip:0x2a3a4a});
  fg2.g.position.set(15,-1.4,17); g.add(fg2.g);
  addLights(g,{c:0xc9d3e0,i:0.46,p:[-46,88,26]},{c:0x1a2230,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); myst.update(t,k); motes.update(t); scent.update(t,k,1,0.25);
      plum.update(t,k); plum2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.3,0.09); pluck(2,0.85,0.08); }};
}
function bShuying(){ // 二 · 疏影暗香 —— 疏影横斜水清浅，暗香浮动月黄昏（诗眼）
  const g=new THREE.Group();
  const ctl={t:0};
  const grd=makeGround({r:240,c1:0x0a0d13,c2:0x131922,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:40,layers:3,peaks:5,seed:931,color:0x070a10,atmo:0x1c2735,
    fogK:0.62,glowK:0.05,glow:0x9fb3cc,y:-11});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  /* 清浅之水：一泓浅水（白得发亮，衬梅影） */
  const water=makeWater({size:46,seg:34,amp:0.045,freq:0.16,speed:0.35,flow:[0.1,0.35],spec:1.5,
    deep:0x0d1622,shallow:0x2a3a4e,skyc:0x3a4a60,moonDir:[-20,90,-140],y:-0.5});
  water.mesh.position.set(0,-0.5,-6); g.add(water.mesh);
  /* 水中疏影：横斜的一道梅影 */
  const shadow=makePlumShadowXM({n:7,y:-0.44,tilt:0.42,seed:33}); shadow.g.position.set(0.5,-0.44,-6); g.add(shadow.g);
  /* 横斜梅枝：临水一枝（画面主体） */
  const plum=makePlumXM({h:5.0,seed:113,scale:1.1,flowers:4,lean:0.9,asym:0.7});
  plum.g.position.set(-5.6,-0.5,-5.2); plum.g.rotation.z=0.30; g.add(plum.g);
  const plum2=makePlumXM({h:4.2,seed:127,scale:0.9,flowers:3,lean:0.5,asym:-0.4});
  plum2.g.position.set(7.4,-0.5,-7.6); g.add(plum2.g);
  const bare=makeBareTreeXM({h:3.0,seed:149,scale:0.9}); bare.g.position.set(-2.5,-0.5,-11); g.add(bare.g);
  const scent=makeScentXM({n:12,spread:[18,5,12],pos:[-2,1.6,-4],scale:7.2,op:0.14});
  g.add(scent.g);
  const motes=makeGlow({n:40,box:[150,24,90],pos:[0,7,-18],color:0xc9d3e0,size:6,speed:0.03,rise:0,maxA:0.13});
  g.add(motes.points);
  const myst=makeMist({n:7,spread:[210,26,110],pos:[0,8,-46],scale:74,color:0x22304a,op:0.11});
  g.add(myst.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:16,d:6,color:0x05070a,seed:45,rim:0.16,rimC:0xc9d3e0});
  fg.g.position.set(-13,-1.3,13); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x060810,seed:47,sway:0.9,tip:0x2a3a4a});
  fg2.g.position.set(12,-1.2,12); g.add(fg2.g);
  addLights(g,{c:0xc9d3e0,i:0.48,p:[-42,84,24]},{c:0x1a2230,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ridge.update(t,0); water.update(t); myst.update(t,k); motes.update(t);
      scent.update(t,k,1,0.3);
      shadow.update(t,k,0.25);
      plum.update(t,k); plum2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(5,0.4,0.09); pluck(3,1.0,0.08); }};
}
function bShuangqin(){ // 三 · 霜禽粉蝶 —— 霜禽欲下先偷眼，粉蝶如知合断魂
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0a0d13,c2:0x131922,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:38,layers:2,peaks:5,seed:941,color:0x070a10,atmo:0x1b2633,
    fogK:0.60,glowK:0.05,glow:0x9ab0c6,y:-11});
  ridge.g.position.set(0,0,-106); g.add(ridge.g);
  const water=makeWater({size:40,seg:30,amp:0.04,freq:0.16,speed:0.32,flow:[0.1,0.3],spec:1.4,
    deep:0x0d1622,shallow:0x28384a,skyc:0x36465a,moonDir:[-20,90,-140],y:-0.5});
  water.mesh.position.set(0,-0.5,-8); g.add(water.mesh);
  const plum=makePlumXM({h:5.0,seed:151,scale:1.1,flowers:4,lean:0.8,asym:0.6});
  plum.g.position.set(-4.6,-0.5,-4.6); plum.g.rotation.z=0.26; g.add(plum.g);
  const bare=makeBareTreeXM({h:3.2,seed:157,scale:0.9}); bare.g.position.set(8.5,-0.5,-11); g.add(bare.g);
  /* 霜禽：欲下未下、偷眼相看（停在枝侧上方） */
  const bird=makeFrostBirdXM({scale:1.25,seed:55,ry:1.9}); bird.g.position.set(0.9,3.5,-4.0); g.add(bird.g);
  /* 粉蝶：如知合断魂（虚影一对） */
  const bf1=makeButterflyXM({scale:1.15,seed:63,y:2.4}); bf1.g.position.set(2.2,2.4,-3.2); g.add(bf1.g);
  const bf2=makeButterflyXM({scale:0.95,seed:67,y:2.9}); bf2.g.position.set(-0.6,2.9,-5.0); g.add(bf2.g);
  const scent=makeScentXM({n:9,spread:[14,5,10],pos:[-2,1.6,-4],scale:6.4,op:0.12});
  g.add(scent.g);
  const motes=makeGlow({n:38,box:[140,22,84],pos:[0,7,-16],color:0xc9d3e0,size:6,speed:0.03,rise:0,maxA:0.13});
  g.add(motes.points);
  const myst=makeMist({n:7,spread:[200,24,100],pos:[0,8,-44],scale:72,color:0x22304a,op:0.11});
  g.add(myst.g);
  const fg=makeForeground({kind:'坡石',n:3,r:2.9,w:15,d:6,color:0x05070a,seed:49,rim:0.16,rimC:0xc9d3e0});
  fg.g.position.set(11,-1.2,10); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:15,n:8,d:5,color:0x060810,seed:51,sway:0.9,tip:0x2a3a4a});
  fg2.g.position.set(-11,-1.1,9); g.add(fg2.g);
  addLights(g,{c:0xc9d3e0,i:0.48,p:[-40,82,22]},{c:0x1a2230,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); myst.update(t,k); motes.update(t);
      scent.update(t,k,1,0.28);
      plum.update(t,k); bird.update(t,k); bf1.update(t,k); bf2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(5,0.25,0.09); }};
}
function bWeiyin(){ // 四（末境·可点击）· 微吟相狎 —— 幸有微吟可相狎，不须檀板共金樽
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,sway:0};
  const grd=makeGround({r:240,c1:0x0a0d13,c2:0x131922,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:40,layers:3,peaks:5,seed:951,color:0x070a10,atmo:0x1c2735,
    fogK:0.62,glowK:0.05,glow:0x9fb3cc,y:-11});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  const water=makeWater({size:42,seg:32,amp:0.045,freq:0.15,speed:0.35,flow:[0.1,0.34],spec:1.5,
    deep:0x0d1622,shallow:0x2a3a4e,skyc:0x3a4a60,moonDir:[-20,90,-140],y:-0.5});
  water.mesh.position.set(0,-0.5,-6); g.add(water.mesh);
  const shadow=makePlumShadowXM({n:8,y:-0.44,tilt:0.40,seed:37}); shadow.g.position.set(0.4,-0.44,-6); g.add(shadow.g);
  const plum=makePlumXM({h:5.2,seed:163,scale:1.15,flowers:4,lean:0.95,asym:0.75});
  plum.g.position.set(-5.2,-0.5,-4.8); plum.g.rotation.z=0.32; g.add(plum.g);
  const plum2=makePlumXM({h:4.4,seed:167,scale:0.95,flowers:3,lean:0.6,asym:-0.4});
  plum2.g.position.set(6.8,-0.5,-7.2); g.add(plum2.g);
  /* 诗人：月下微吟（无檀板金樽） */
  const poet=makeFigure({pose:'独立',robe:0x2a3446,belt:0x9fb3cc,collar:0xdfe6f0,hat:'发髻',
    hair:0x14161f,scale:1.14,rim:0.52,rimC:0xc9d3e0,noProp:true});
  poet.position.set(3.6,-0.3,-2.6); poet.rotation.y=-2.5; g.add(poet);
  const scent=makeScentXM({n:14,spread:[20,6,14],pos:[-2,1.8,-4],scale:7.6,op:0.15});
  g.add(scent.g);
  const motes=makeGlow({n:42,box:[150,24,90],pos:[0,7,-18],color:0xc9d3e0,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const myst=makeMist({n:7,spread:[210,26,110],pos:[0,8,-46],scale:74,color:0x22304a,op:0.11});
  g.add(myst.g);
  const crowd=makeCrowd({n:2,rect:[-16,-34,10,6],seed:171,color:0x101620,rimC:0xc9d3e0,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:16,d:6,color:0x05070a,seed:53,rim:0.16,rimC:0xc9d3e0});
  fg.g.position.set(-12,-1.3,12); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x060810,seed:55,sway:0.9,tip:0x2a3a4a});
  fg2.g.position.set(11,-1.2,11); g.add(fg2.g);
  addLights(g,{c:0xc9d3e0,i:0.48,p:[-42,84,24]},{c:0x1a2230,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.sway=Math.min(1,ctl.sway+dt/2.2);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const sw=ctl.sway+0.6*ctl.pulse;
      const grow=1+1.0*ctl.sway;
      ridge.update(t,0); water.update(t); myst.update(t,k); motes.update(t); crowd.update(t);
      scent.update(t,k,grow,0.35+0.6*ctl.sway);
      shadow.update(t,k,sw);
      plum.update(t,k); plum2.update(t,k); poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(3,0.35,0.10); pluck(1,0.75,0.08);
        const fl=$('#flash'); fl.textContent='暗香浮动'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：暗香再浓一分，疏影再摇一回 */
    },clicked:false};
  return api;
}
