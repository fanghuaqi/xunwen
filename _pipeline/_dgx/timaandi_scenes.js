/* ================= 题临安邸 · 三境场景（水墨夜思 · 西湖灯影变体：卷首西湖夜色、青山画舫、杭州汴州）
   本诗专属系统「杭州·汴州」：湖山楼台层层叠叠、画舫灯影正盛（杭州），
   末境点击西湖歌舞 → 暖风横流、灯影虚化，汴州故都的残影自湖上渐渐浮现，题字「杭州作汴州」。
   与同赛道《山园小梅》（孤山梅影）、《忆秦娥》（秦楼月）不同：本页是西湖灯火、画舫与故都残影。 ================= */

/* —— 楼台：两层楼阁（台基 + 楼身 + 两层檐 + 窗 + 栏杆），合批 1 mesh —— */
function makePavilionLS(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, h1=o.h1===undefined?3.0:o.h1, h2=o.h2===undefined?2.6:o.h2;
  const col=o.color===undefined?0x2a2e38:o.color, roof=o.roof===undefined?0x1e222a:o.roof;
  const warm=o.warm===undefined?0xe0b878:o.warm;
  const B=new GeoBag();
  const bs=new THREE.BoxGeometry(w*1.15,0.6,o.d===undefined?5:o.d*1.15); bs.translate(0,0.3,0); B.put(bs,shadeColor(0x3a3f48,0.9));
  const b1=new THREE.BoxGeometry(w,h1,o.d===undefined?5:o.d); b1.translate(0,0.6+h1/2,0); B.put(b1,col);
  const e1=new THREE.ConeGeometry(w*0.84,1.0,4); e1.rotateY(Math.PI/4); e1.translate(0,0.6+h1+0.5,0); B.put(e1,roof);
  const b2=new THREE.BoxGeometry(w*0.9,h2,(o.d===undefined?5:o.d)*0.85); b2.translate(0,0.6+h1+1.05+h2/2,0);
  B.put(b2,shadeColor(col,1.08));
  const e2=new THREE.ConeGeometry(w*0.78,0.95,4); e2.rotateY(Math.PI/4); e2.translate(0,0.6+h1+1.05+h2+0.48,0);
  B.put(e2,shadeColor(roof,1.12));
  for(let i=0;i<3;i++){
    const x=-w*0.28+w*0.28*i;
    const wn=new THREE.BoxGeometry(w*0.16,h1*0.42,0.16); wn.translate(x,0.6+h1*0.56,o.d/2+0.04); B.put(wn,warm);
    const wn2=new THREE.BoxGeometry(w*0.16,h2*0.42,0.16); wn2.translate(x,0.6+h1+1.05+h2*0.52,o.d*0.425+0.04); B.put(wn2,warm);
  }
  /* 二层栏杆 */
  const rt=new THREE.BoxGeometry(w*0.86,0.14,0.2); rt.translate(0,0.6+h1+1.25,o.d*0.44); B.put(rt,shadeColor(col,1.3));
  for(let i=0;i<=7;i++){
    const q=new THREE.BoxGeometry(0.12,1.0,0.12); q.translate(-w*0.42+w*0.84*i/7,0.6+h1+0.75,o.d*0.44); B.put(q,col);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a4454,emissive:0x0e1218}),{c:o.rimC===undefined?0x9fb3cc:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mesh};
}

/* —— 湖灯：岸上与船上的灯（灯体合批 1 mesh + 暖光 sprite，只调 scale） —— */
function makeLampLS(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, B=new GeoBag();
  const pts=[[0.02,-0.26],[0.22,-0.26],[0.30,-0.12],[0.32,0.04],[0.26,0.24],[0.16,0.30],[0.02,0.32]];
  B.put(new THREE.LatheGeometry(pts.map(function(p){return new THREE.Vector2(p[0],p[1]);}),14),
    o.paper===undefined?0xe8c274:o.paper);
  const cap=new THREE.CylinderGeometry(0.10,0.13,0.08,8); cap.translate(0,0.35,0); B.put(cap,0x3a3028);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x6a5a30,emissive:0x3a2608,side:THREE.DoubleSide}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc478,transparent:true,
    opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  gl.scale.set(3.4,3.4,1); gl.renderOrder=3; g.add(gl);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?241:o.seed)()*6.283;
  g.update=function(t,k,grow){
    const gg=grow===undefined?1:grow;
    gl.scale.set(3.4*gg*(0.95+0.05*Math.sin(t*2.2+ph)),3.4*gg,1);
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,glow:gl};
}

/* —— 画舫：船身 + 篷 + 灯 + 舫上人影（合批 1 mesh + 若干灯） —— */
function makeBoatLS(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, B=new GeoBag();
  const hull=new THREE.BoxGeometry(7.2,0.7,2.4); hull.translate(0,0.35,0); B.put(hull,0x2c3038);
  const bow=new THREE.ConeGeometry(1.1,1.8,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(3.6,0.4,0);
  B.put(bow,0x2c3038);
  const cabin=new THREE.BoxGeometry(3.2,1.2,1.9); cabin.translate(-0.4,1.3,0); B.put(cabin,0x3a3f48);
  const roof=new THREE.BoxGeometry(3.6,0.16,2.2); roof.translate(-0.4,1.98,0); B.put(roof,0x4a5058);
  for(let i=0;i<4;i++){
    const p=new THREE.CylinderGeometry(0.05,0.05,1.9,5); p.translate(-1.9+i*1.0,2.9,0); B.put(p,0x3a3028);
  }
  const canopy=new THREE.BoxGeometry(4.0,0.12,2.4); canopy.translate(-0.7,3.86,0); B.put(canopy,0x2e343c);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a5464,emissive:0x0a0e14}),{c:o.rimC===undefined?0x9fb3cc:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const lamps=[];
  [[-1.9,1.0],[-0.4,1.0],[1.1,1.0]].forEach(function(p,i){
    const L=makeLampLS({scale:0.62,seed:251+i*7}); L.g.position.set(p[0],1.9,p[1]); g.add(L.g); lamps.push(L);
  });
  const guest=makeFigure({pose:'坐饮',robe:0x323a46,belt:0x8fa4c0,collar:0xdfe6f0,hat:'幞头',
    hair:0x14161f,scale:0.72,rim:0.4,rimC:0x9fb3cc});
  guest.position.set(-0.2,1.55,0.2); guest.rotation.y=-1.5; g.add(guest);
  g.scale.setScalar(s);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  const ph=seedRnd(o.seed===undefined?257:o.seed)()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.position.y=(o.y===undefined?0:o.y)+0.05*Math.sin(t*1.1+ph)*kk;
    g.rotation.z=0.02*Math.sin(t*0.8+ph)*kk;
    for(let i=0;i<lamps.length;i++)lamps[i].update(t,kk,1);
    guest.update(t,kk);
  };
  g.userData.update=g.update;
  return {g,update:g.update,lamps,guest};
}

/* —— 汴州残影：故都楼台的虚幻剪影（共用一个半透材质；构造 opacity = 运行期最大值 0.58） —— */
function makeBianzhouLS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?263:o.seed), B=new GeoBag();
  for(let i=0;i<7;i++){
    const x=(R()-0.5)*70, z=(R()-0.5)*22;
    const hh=8+R()*13, ww=5+R()*5;
    const body=new THREE.BoxGeometry(ww,hh,ww*0.8); body.translate(x,hh/2,z); B.put(body,0xc8d4e4);
    const eave=new THREE.ConeGeometry(ww*0.9,3.0,4); eave.rotateY(Math.PI/4); eave.translate(x,hh+1.4,z);
    B.put(eave,0xd8e2f0);
    if(R()<0.7){
      const t2=new THREE.ConeGeometry(ww*0.62,2.4,4); t2.rotateY(Math.PI/4);
      t2.translate(x,hh+3.4,z); B.put(t2,0xe0e8f4);
    }
  }
  const mat=new THREE.MeshBasicMaterial({color:0xffffff,vertexColors:true,transparent:true,
    opacity:0.58,depthWrite:false});
  const mesh=B.mesh(mat); mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?-58:o.z);
  return {g,mesh,mat};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 西湖夜色 —— 远山层叠、湖上灯影一线
  const g=new THREE.Group();
  const grd=makeGround({r:270,c1:0x0a0e14,c2:0x141c26,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:52,layers:3,peaks:6,seed:1511,color:0x0a0f16,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x9fb3cc,y:-13});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const water=makeWater({size:170,seg:46,amp:0.09,freq:0.09,speed:0.4,flow:[0.15,0.5],spec:1.3,
    deep:0x0a121c,shallow:0x1c2c3e,skyc:0x2a3a50,moonDir:[-40,90,-160],y:-1.0});
  water.mesh.position.set(0,-1.0,-36); g.add(water.mesh);
  const boats=[];
  [[-16,0,-22,0.4],[4,0,-28,0.35],[20,0,-20,0.3]].forEach(function(p,i){
    const b=makeBoatLS({scale:0.9,seed:271+i*11,x:p[0],y:-0.9,z:p[2]}); b.g.rotation.y=p[3]; g.add(b.g); boats.push(b);
  });
  const pavs=[];
  [[-30,0,-46],[26,0,-44],[-8,0,-52],[38,0,-40]].forEach(function(p,i){
    const pv=makePavilionLS({w:7,h1:3.0,h2:2.6,scale:0.95,seed:281+i*7}); pv.g.position.set(p[0],-1.3,p[2]); g.add(pv.g); pavs.push(pv);
  });
  const lamps=[];
  for(let i=0;i<5;i++){
    const L=makeLampLS({scale:1.0,seed:291+i*13}); L.g.position.set(-26+i*13,-1.1,-40); g.add(L.g); lamps.push(L);
  }
  const motes=makeGlow({n:46,box:[200,26,96],pos:[0,9,-28],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,28,120],pos:[0,9,-56],scale:80,color:0x22304a,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:19,d:7,color:0x080c10,seed:47,rim:0.16,rimC:0x9fb3cc});
  fg.g.position.set(-18,-1.5,44); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x0a1014,seed:49,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(17,-1.4,30); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-44,72,28]},{c:0x1a2430,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    for(let i=0;i<boats.length;i++)boats[i].update(t,k);
    for(let i=0;i<lamps.length;i++)lamps[i].update(t,k,1);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bQingshan(){ // 一 · 青山画舫 —— 山外青山楼外楼，西湖歌舞几时休？
  const g=new THREE.Group();
  const grd=makeGround({r:270,c1:0x0a0e14,c2:0x141c26,y:-1.2}); g.add(grd.mesh);
  /* 山外青山：三层山脊递退 */
  const r1=makeRange({r:300,h:64,layers:3,peaks:6,seed:1521,color:0x090e15,atmo:0x1c2735,fogK:0.66,glowK:0.04,glow:0x8fa8c4,y:-14});
  r1.g.position.set(0,0,-120); g.add(r1.g);
  const r2=makeRange({r:220,h:40,layers:2,peaks:5,seed:1522,color:0x0b1119,atmo:0x202c3a,fogK:0.64,glowK:0.05,glow:0x96aec8,y:-10});
  r2.g.position.set(0,0,-74); g.add(r2.g);
  const water=makeWater({size:160,seg:44,amp:0.10,freq:0.10,speed:0.45,flow:[0.15,0.55],spec:1.35,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2e4056,moonDir:[-40,90,-160],y:-1.0});
  water.mesh.position.set(0,-1.0,-30); g.add(water.mesh);
  /* 楼外楼：岸上楼台成排（两层，一层比一层远） */
  const pavs=[];
  [[-34,0,-40],[-22,0,-34],[-10,0,-44],[6,0,-36],[20,0,-42],[34,0,-32]].forEach(function(p,i){
    const pv=makePavilionLS({w:7.4,h1:3.2,h2:2.8,scale:1.0,seed:301+i*7}); pv.g.position.set(p[0],-1.2,p[2]); g.add(pv.g); pavs.push(pv);
  });
  /* 西湖歌舞：三只画舫（灯影与舫上人影） */
  const boats=[];
  [[-18,0,-16,0.35],[0,0,-22,0.2],[18,0,-15,0.4],[30,0,-26,0.5]].forEach(function(p,i){
    const b=makeBoatLS({scale:1.0,seed:311+i*9,x:p[0],y:-0.9,z:p[2]}); b.g.rotation.y=p[3]; g.add(b.g); boats.push(b);
  });
  /* 岸灯成列 */
  const lamps=[];
  for(let i=0;i<6;i++){
    const L=makeLampLS({scale:1.05,seed:321+i*11}); L.g.position.set(-32+i*13,-1.1,-30); g.add(L.g); lamps.push(L);
  }
  const crowd=makeCrowd({n:4,rect:[-30,-44,44,10],seed:331,color:0x141c26,rimC:0x9fb3cc,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:44,box:[190,24,90],pos:[0,9,-24],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,26,110],pos:[0,9,-56],scale:78,color:0x22304a,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x080c10,seed:51,rim:0.16,rimC:0x9fb3cc});
  fg.g.position.set(-16,-1.4,28); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x0a1014,seed:53,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(16,-1.3,22); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-42,70,26]},{c:0x1a2430,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      r1.update(t,0); r2.update(t,0); water.update(t); mist.update(t,k); motes.update(t); crowd.update(t);
      for(let i=0;i<boats.length;i++)boats[i].update(t,k);
      for(let i=0;i<lamps.length;i++)lamps[i].update(t,k,1);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(5,0.3,0.09); pluck(3,0.95,0.08); }};
}
function bHangzhou(){ // 二（末境·可点击）· 杭州汴州 —— 暖风熏得游人醉，直把杭州作汴州
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,reveal:0};
  const grd=makeGround({r:260,c1:0x0a0e14,c2:0x141c26,y:-1.2}); g.add(grd.mesh);
  const r1=makeRange({r:280,h:52,layers:3,peaks:6,seed:1531,color:0x090e15,atmo:0x1c2735,fogK:0.64,glowK:0.04,glow:0x8fa8c4,y:-13});
  r1.g.position.set(0,0,-116); g.add(r1.g);
  /* 湖面与近岸楼台：灯影正盛 */
  const water=makeWater({size:150,seg:42,amp:0.09,freq:0.10,speed:0.42,flow:[0.15,0.5],spec:1.35,
    deep:0x0a121c,shallow:0x1e2e42,skyc:0x2e4056,moonDir:[-40,90,-160],y:-1.0});
  water.mesh.position.set(0,-1.0,-28); g.add(water.mesh);
  const pv1=makePavilionLS({w:9,h1:3.4,h2:3.0,scale:1.15,seed:341}); pv1.g.position.set(-9,-1.2,-14); g.add(pv1.g);
  const pv2=makePavilionLS({w:8,h1:3.2,h2:2.8,scale:1.05,seed:343}); pv2.g.position.set(3,-1.2,-18); g.add(pv2.g);
  const pv3=makePavilionLS({w:8.6,h1:3.2,h2:2.8,scale:1.0,seed:347}); pv3.g.position.set(15,-1.2,-13); g.add(pv3.g);
  const lamps=[];
  [[-14,1.0,-10.5],[-4.5,1.0,-10.5],[7,1.0,-14],[18,1.0,-9.5],[-19,1.0,-15]].forEach(function(p,i){
    const L=makeLampLS({scale:1.15,seed:351+i*7}); L.g.position.set(p[0],p[1],p[2]); g.add(L.g); lamps.push(L);
  });
  /* 游人醉：楼上凭栏的两人（一杯在手） */
  const drunk1=makeFigure({pose:'坐饮',robe:0x333c4a,belt:0x8fa4c0,collar:0xdfe6f0,hat:'幞头',
    hair:0x14161f,scale:1.15,rim:0.44,rimC:0x9fb3cc});
  drunk1.position.set(-8.2,-0.2,-11.6); drunk1.rotation.y=-1.6; g.add(drunk1);
  const drunk2=makeFigure({pose:'举杯',robe:0x3a4450,belt:0x9fb3cc,collar:0xdfe6f0,hat:'幞头',
    hair:0x14161f,scale:1.1,rim:0.42,rimC:0x9fb3cc});
  drunk2.position.set(4.0,-0.2,-15.4); drunk2.rotation.y=-1.9; g.add(drunk2);
  /* 画舫两只（湖上歌舞） */
  const boats=[];
  [[-12,0,-24,0.3],[8,0,-30,0.25]].forEach(function(p,i){
    const b=makeBoatLS({scale:1.0,seed:361+i*9,x:p[0],y:-0.9,z:p[2]}); b.g.rotation.y=p[3]; g.add(b.g); boats.push(b);
  });
  /* 暖风：横流的暖色风尘（"暖风熏得游人醉"） */
  const warm=makeFlow({n:320,box:[180,18,90],pos:[0,4.5,-22],color:0xd8a878,size:16,speed:3.0,maxA:0.18});
  g.add(warm.points);
  /* 汴州残影：故都楼台，藏在湖上远处（点击后浮现） */
  const bian=makeBianzhouLS({x:0,y:-1.0,z:-62,seed:367}); g.add(bian.g);
  const crowd=makeCrowd({n:4,rect:[-26,-32,40,10],seed:371,color:0x141c26,rimC:0x9fb3cc,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:42,box:[180,24,88],pos:[0,9,-22],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[220,26,110],pos:[0,9,-54],scale:76,color:0x22304a,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.2,w:17,d:7,color:0x080c10,seed:57,rim:0.16,rimC:0x9fb3cc});
  fg.g.position.set(-15,-1.4,16); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x0a1014,seed:59,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(15,-1.3,14); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-42,70,26]},{c:0x1a2430,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/2.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const rv=ctl.reveal+0.4*ctl.pulse;
      r1.update(t,0); water.update(t); mist.update(t,k); motes.update(t); crowd.update(t);
      warm.update(t);
      /* 汴州残影浮现：基座 0.58 = 运行期最大值，每帧乘 fadeK 与进度 */
      bian.mat.opacity=k*0.58*Math.min(1,rv);
      /* 杭州灯影「虚化」：灯的光团随 reveal 放大变柔（只调 scale） */
      const grow=1+0.55*Math.min(1,rv);
      for(let i=0;i<lamps.length;i++)lamps[i].update(t,k,grow);
      for(let i=0;i<boats.length;i++)boats[i].update(t,k);
      drunk1.update(t,k); drunk2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.00,0.13); pluck(4,0.28,0.11); pluck(1,0.60,0.09);
        const fl=$('#flash'); fl.textContent='杭州作汴州'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：灯影再虚一层，故都再清一分 */
    },clicked:false};
  return api;
}
