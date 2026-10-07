/* ================= 菊花 · 三境场景（青绿春晓 · 秋菊绕舍变体：卷首绕舍秋菊、绕舍秋丛、偏爱菊花）
   本诗专属系统「此花开尽更无花」：秋丛绕舍、篱边遍看、日渐斜（低斜暖阳与长影）。
   末境点击偏爱菊 → 斜阳更斜、菊丛花光次第点亮并摇曳、远处百花凋尽作对照，题字「此花开尽更无花」。
   与同赛道《赠刘景文》（初冬橙橘）、《画菊》（篱菊北风）不同：本页是秋日茅舍、绕舍菊丛与斜阳。 ================= */

/* —— 茅舍：草顶 + 土墙 + 门窗（"似陶家"的屋子），合批 1 mesh —— */
function makeThatchedHouseJH(o){
  o=o||{};
  const w=o.w===undefined?8:o.w, d=o.d===undefined?6.4:o.d, h=o.h===undefined?3.4:o.h;
  const wall=o.wall===undefined?0x6a5a3e:o.wall, thatch=o.thatch===undefined?0x7a6a38:o.thatch;
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?1001:o.seed);
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h*0.5,0); B.put(body,shadeColor(wall,0.9+R()*0.25));
  /* 草顶：两坡 + 层叠草束 */
  const r1=new THREE.BoxGeometry(w*1.2,0.3,d*0.62); r1.rotateX(0.42); r1.translate(0,h+0.5,d*0.26);
  B.put(r1,shadeColor(thatch,0.92+R()*0.16));
  const r2=new THREE.BoxGeometry(w*1.2,0.3,d*0.62); r2.rotateX(-0.42); r2.translate(0,h+0.5,-d*0.26);
  B.put(r2,shadeColor(thatch,1.0+R()*0.16));
  const ridge=new THREE.BoxGeometry(w*1.22,0.26,0.4); ridge.translate(0,h+0.86,0); B.put(ridge,shadeColor(thatch,1.15));
  for(let i=0;i<8;i++){
    const t=new THREE.BoxGeometry(w*1.16,0.10,0.5); t.rotateZ((R()-0.5)*0.05);
    t.translate(0,h+0.32+i*0.07,i%2?d*0.3:-d*0.3); B.put(t,shadeColor(thatch,0.85+R()*0.3));
  }
  const door=new THREE.BoxGeometry(w*0.2,h*0.56,0.22); door.translate(-w*0.14,h*0.28,d*0.5+0.02); B.put(door,0x241c12);
  const win=new THREE.BoxGeometry(w*0.26,h*0.3,0.2); win.translate(w*0.22,h*0.62,d*0.5+0.02); B.put(win,0x2a2014);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x5a4a2a,emissive:0x0e0a06}),{c:o.rimC===undefined?0xd8c880:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 菊丛：一丛秋菊（茎 + 叶 + 多头花：黄/白/紫），合批 1 mesh —— */
function makeChrysClumpJH(o){
  o=o||{};
  const n=o.n===undefined?6:o.n, R=seedRnd(o.seed===undefined?1007:o.seed);
  const h=o.h===undefined?1.9:o.h, stem=o.stem===undefined?0x4a5a34:o.stem;
  const B=new GeoBag(), heads=[];
  const cols=[0xe0b83a,0xf0e6c8,0xb87ac8,0xd8a038];
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*(o.w===undefined?2.4:o.w), z=(R()-0.5)*2.2, hh=h*(0.7+R()*0.6), lean=(R()-0.5)*0.4;
    const top=[x+lean*hh,hh,z];
    B.put(limbGeo([x,0,z],top,0.036,0.020,5),shadeColor(stem,0.85+R()*0.3));
    for(let k=0;k<3;k++){
      const t=0.34+0.24*k;
      const lf=new THREE.PlaneGeometry(0.54,0.22);
      lf.rotateZ((R()-0.5)*0.9); lf.rotateY(R()*6.283);
      lf.translate(x+lean*hh*t+(R()-0.5)*0.32,hh*t,z+(R()-0.5)*0.32);
      B.put(lf,shadeColor(0x5f7040,0.85+R()*0.4));
    }
    const pr=0.26+R()*0.13;
    const disc=new THREE.CylinderGeometry(pr*0.4,pr*0.4,0.05,10); disc.translate(top[0],top[1]+0.06,top[2]);
    B.put(disc,0xc8a63a);
    const np=Math.round(9+R()*5);
    for(let k=0;k<np;k++){
      const a=k/np*6.283;
      const pf=new THREE.PlaneGeometry(pr*1.16,pr*0.56);
      pf.rotateZ(a); pf.rotateX(-0.5+R()*0.9); pf.rotateY(R()*0.5);
      pf.translate(top[0]+Math.cos(a)*pr*0.72, top[1]+0.02-R()*0.12, top[2]+Math.sin(a)*pr*0.72);
      B.put(pf,shadeColor(cols[(i+k)%cols.length],0.8+R()*0.5));   /* 花色在花瓣循环内取，k 才在作用域内 */
    }
    heads.push([top[0]+(o.x===undefined?0:o.x)*0,top[1],top[2]]);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x8a8a60,emissive:0x1a1608,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe0d090:o.rimC,i:0.24,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.02+0.06*wd)*Math.sin(t*(1.0+1.4*wd)+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,heads};
}

/* —— 花光：菊丛上的暖黄花光点（Sprite；点击偏爱菊后次第点亮） —— */
function makeBloomGlowJH(o){
  o=o||{};
  const pos=o.pos||[], g=new THREE.Group(), items=[];
  for(let i=0;i<pos.length;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0xffd070:o.color,
      transparent:true,opacity:0.32,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set(pos[i][0],pos[i][1]+0.15,pos[i][2]);
    s.scale.set(1.0,1.0,1); s.renderOrder=3; g.add(s);
    items.push({s:s,ph:i*0.57});
  }
  return {g,items,update:function(t,k,lit){
    const li=lit===undefined?0:lit;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const sc=(0.45+0.95*li)*(0.88+0.12*Math.sin(t*2.2+it.ph));
      it.s.scale.set(sc*1.3,sc*1.3,1);
    }
  }};
}

/* —— 百花凋尽：残枝败叶（几株枯枝 + 满地落叶），合批 1 mesh —— */
function makeWitherJH(o){
  o=o||{};
  const n=o.n===undefined?7:o.n, R=seedRnd(o.seed===undefined?1013:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*(o.w===undefined?24:o.w), z=(R()-0.5)*10, h=1.2+R()*1.4;
    B.put(limbGeo([x,0,z],[x+(R()-0.5)*0.6,h,z+(R()-0.5)*0.5],0.04,0.018,5),shadeColor(0x5a4c3a,0.8+R()*0.4));
    for(let k=0;k<2;k++){
      const a=R()*6.283, ln=0.5+R()*0.5;
      B.put(limbGeo([x,h*0.7,z],[x+Math.sin(a)*ln,h*0.9,z+Math.cos(a)*ln],0.02,0.008,4),
        shadeColor(0x5a4c3a,0.9+R()*0.3));
    }
  }
  for(let i=0;i<26;i++){
    const lf=new THREE.PlaneGeometry(0.36,0.16);
    lf.rotateZ(R()*3.0); lf.rotateX(-Math.PI/2+0.2);
    lf.translate((R()-0.5)*(o.w===undefined?26:o.w),0.05,(R()-0.5)*11);
    B.put(lf,shadeColor(0x8a6a3a,0.7+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x4a3a24,emissive:0x0c0a06,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xc0a878:o.rimC,i:0.20,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.006+0.014*wd)*Math.sin(t*0.6+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 疏篱：木篱（桩 + 两道横杆），合批 1 mesh —— */
function makeFenceJH(o){
  o=o||{};
  const w=o.w===undefined?18:o.w, h=o.h===undefined?1.5:o.h, R=seedRnd(o.seed===undefined?1019:o.seed);
  const wood=o.color===undefined?0x6a5a3e:o.color, B=new GeoBag();
  const np=o.posts===undefined?9:o.posts;
  for(let i=0;i<np;i++){
    const x=-w/2+w*i/(np-1), lean=(R()-0.5)*0.14;
    const p=new THREE.CylinderGeometry(0.07,0.09,h,6); p.rotateZ(lean); p.translate(x,h*0.5,0);
    B.put(p,shadeColor(wood,0.8+R()*0.5));
  }
  [0.45,0.85].forEach(function(f){
    const r=new THREE.BoxGeometry(w*1.02,0.08,0.1); r.rotateZ((R()-0.5)*0.03);
    r.translate(0,h*f,0.02); B.put(r,shadeColor(wood,1.15));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a6a48,emissive:0x14120c}),{c:o.rimC===undefined?0xd0d090:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 斜阳：低垂的秋日（日轮 sprite + 地面一道长影光带；只调 scale/rotation） —— */
function makeSlantSunJH(o){
  o=o||{};
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc46a,transparent:true,
    opacity:0.42,depthWrite:false,blending:THREE.AdditiveBlending}));
  disc.scale.set(o.r===undefined?34:o.r*2, o.r===undefined?34:o.r*2,1); disc.renderOrder=-8; g.add(disc);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf0a04a,transparent:true,
    opacity:0.16,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(o.r===undefined?34:o.r*5, o.r===undefined?34:o.r*4.4,1); halo.renderOrder=-8; g.add(halo);
  g.position.set(o.x===undefined?-70:o.x, o.y===undefined?20:o.y, o.z===undefined?-180:o.z);
  /* 地面长影光带 */
  const band=new THREE.Mesh(new THREE.PlaneGeometry(o.bw===undefined?90:o.bw,(o.bw===undefined?90:o.bw)*0.22),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0xffc888,transparent:true,opacity:0.18,
      depthWrite:false,blending:THREE.AdditiveBlending}));
  band.rotation.x=-Math.PI/2; band.renderOrder=3;
  band.position.set(o.bx===undefined?-4:o.bx,o.by===undefined?0.05:o.by,o.bz===undefined?-4:o.bz);
  g.add(band);
  return {g,disc,halo,band,update:function(t,k,slant){
    const kk=k===undefined?1:k, sl=slant===undefined?0:slant;
    disc.scale.set(34*(1+0.12*sl),34*(1+0.12*sl),1);
    band.rotation.z=-0.5-sl*0.5;
    const s=1+0.05*Math.sin(t*0.3);
    band.scale.set(s,s,1);
  }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 绕舍秋菊 —— 秋日茅舍、绕舍菊丛、低斜暖阳
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0f1c12,c2:0x1e3018,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:40,layers:3,peaks:5,seed:2211,color:0x101f12,atmo:0x3a5030,
    fogK:0.62,glowK:0.06,glow:0xd8c080,y:-11});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const sun=makeSlantSunJH({x:-72,y:18,z:-186,r:11,bx:-6,bz:-6,bw:80}); g.add(sun.g);
  const house=makeThatchedHouseJH({w:8.4,d:6.6,h:3.4,x:-2,y:-1.4,z:-16,seed:1003}); g.add(house.g);
  const clumps=[];
  for(let i=0;i<12;i++){
    const a=i/12*6.283;
    const c=makeChrysClumpJH({n:6,h:1.9,seed:1021+i*7,scale:1.0});
    c.g.position.set(-2+Math.sin(a)*9.5,-1.4,-16+Math.cos(a)*7.6); g.add(c.g); clumps.push(c);
  }
  const fence=makeFenceJH({w:22,h:1.5,x:-2,y:-1.4,z:-8.4,seed:1023}); g.add(fence.g);
  const wither=makeWitherJH({n:6,w:22,x:14,y:-1.4,z:-18,seed:1027}); g.add(wither.g);
  const motes=makeGlow({n:42,box:[180,24,86],pos:[0,9,-22],color:0xe8d8a0,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,24,100],pos:[0,8,-48],scale:74,color:0x24381c,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x070d08,seed:163,rim:0.14,rimC:0xa3c9a8});
  fg.g.position.set(-16,-1.5,32); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:165,sway:0.9,tip:0x3a4a20});
  fg2.g.position.set(16,-1.4,24); g.add(fg2.g);
  addLights(g,{c:0xe8d090,i:0.54,p:[-50,70,26]},{c:0x26341c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    const wind=0.25+0.15*Math.sin(t*0.4);
    for(let i=0;i<clumps.length;i++)clumps[i].update(t,k,wind);
    wither.update(t,k,wind); sun.update(t,k,0.2);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bRaoshe(){ // 一 · 绕舍秋丛 —— 秋丛绕舍似陶家，遍绕篱边日渐斜
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x0e1b11,c2:0x1c2e17,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:38,layers:3,peaks:5,seed:2221,color:0x0f1e11,atmo:0x384e2e,
    fogK:0.62,glowK:0.06,glow:0xd8c080,y:-11});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 日渐斜：低斜暖阳 + 地面长影 */
  const sun=makeSlantSunJH({x:-66,y:12,z:-176,r:12,bx:-3,bz:-4,bw:86}); g.add(sun.g);
  const house=makeThatchedHouseJH({w:9,d:7,h:3.6,x:-1,y:-1.3,z:-14,seed:1029}); g.add(house.g);
  /* 秋丛绕舍：一圈菊丛（似陶家） */
  const clumps=[];
  for(let i=0;i<14;i++){
    const a=i/14*6.283;
    const c=makeChrysClumpJH({n:7,h:2.0,seed:1031+i*7,scale:1.05});
    c.g.position.set(-1+Math.sin(a)*10.5,-1.3,-14+Math.cos(a)*7.8); g.add(c.g); clumps.push(c);
  }
  const fence=makeFenceJH({w:26,h:1.6,x:-1,y:-1.3,z:-6.4,seed:1033}); g.add(fence.g);
  const fence2=makeFenceJH({w:18,h:1.5,x:14,y:-1.3,z:-18,ry:-0.5,seed:1037}); g.add(fence2.g);
  const wither=makeWitherJH({n:8,w:28,x:-18,y:-1.3,z:-20,seed:1039}); g.add(wither.g);
  const motes=makeGlow({n:40,box:[170,22,84],pos:[0,9,-20],color:0xe8d8a0,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,22,96],pos:[0,8,-46],scale:72,color:0x24381c,op:0.11});
  g.add(mist.g);
  const crowd=makeCrowd({n:2,rect:[-30,-30,16,6],seed:1041,color:0x16220f,rimC:0xa3c9a8,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x070d08,seed:167,rim:0.14,rimC:0xa3c9a8});
  fg.g.position.set(-15,-1.4,20); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:169,sway:0.9,tip:0x3a4a20});
  fg2.g.position.set(15,-1.3,18); g.add(fg2.g);
  addLights(g,{c:0xe8d090,i:0.54,p:[-48,68,24]},{c:0x26341c,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
      const wind=0.3+0.2*Math.sin(t*0.42);
      for(let i=0;i<clumps.length;i++)clumps[i].update(t,k,wind);
      wither.update(t,k,wind); sun.update(t,k,0.35);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.35,0.09); pluck(2,0.9,0.08); }};
}
function bPianai(){ // 二（末境·可点击）· 偏爱菊花 —— 不是花中偏爱菊，此花开尽更无花
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,lit:0,slant:0};
  const grd=makeGround({r:260,c1:0x0f1c12,c2:0x1e3018,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:36,layers:2,peaks:5,seed:2231,color:0x0f1e11,atmo:0x364c2c,
    fogK:0.60,glowK:0.06,glow:0xd8c080,y:-11});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const sun=makeSlantSunJH({x:-60,y:13,z:-170,r:12,bx:-2,bz:-2,bw:80}); g.add(sun.g);
  /* 近景篱边菊丛（画面主体） */
  const clumps=[];
  [[-8,0,-3.4,1043,1.15],[-3.5,0,-2.6,1047,1.1],[1.5,0,-3.6,1049,1.15],[7,0,-2.8,1051,1.1],[11.5,0,-3.8,1053,1.0]].forEach(function(p){
    const c=makeChrysClumpJH({n:8,h:2.1,seed:p[3],scale:p[4]});
    c.g.position.set(p[0],-1.3,p[2]); g.add(c.g); clumps.push(c);
  });
  const fence=makeFenceJH({w:24,h:1.6,x:1,y:-1.3,z:0.6,seed:1057}); g.add(fence.g);
  /* 百花凋尽：远处一片残枝败叶 */
  const wither=makeWitherJH({n:9,w:30,x:2,y:-1.3,z:-16,seed:1059}); g.add(wither.g);
  /* 花光：菊丛上待点亮 */
  const pos=[];
  for(let i=0;i<clumps.length;i++){
    const c=clumps[i];
    for(let k=0;k<c.heads.length;k+=2){
      pos.push([c.g.position.x+c.heads[k][0],c.g.position.y+c.heads[k][1],c.g.position.z+c.heads[k][2]]);
    }
  }
  const glow=makeBloomGlowJH({pos:pos}); g.add(glow.g);
  const motes=makeGlow({n:38,box:[160,22,84],pos:[0,9,-18],color:0xe8d8a0,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,96],pos:[0,8,-44],scale:72,color:0x24381c,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.0,w:15,d:6,color:0x070d08,seed:171,rim:0.14,rimC:0xa3c9a8});
  fg.g.position.set(-14,-1.4,14); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x071009,seed:173,sway:0.9,tip:0x3a4a20});
  fg2.g.position.set(14,-1.3,12); g.add(fg2.g);
  addLights(g,{c:0xe8d090,i:0.54,p:[-46,66,22]},{c:0x26341c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.lit=Math.min(1,ctl.lit+dt/2.2); ctl.slant=Math.min(1,ctl.slant+dt/3.0); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const lit=ctl.lit+0.55*ctl.pulse, sl=ctl.slant+0.35*ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      sun.update(t,k,0.35+0.5*sl);
      const wind=0.3+0.8*lit;
      for(let i=0;i<clumps.length;i++)clumps[i].update(t,k,wind);
      glow.update(t,k,lit);
      wither.update(t,k,0.3);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(4,0.22,0.10); pluck(2,0.5,0.09);
        const fl=$('#flash'); fl.textContent='此花开尽更无花'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：夕阳再斜一分，花光再亮一层 */
    },clicked:false};
  return api;
}
