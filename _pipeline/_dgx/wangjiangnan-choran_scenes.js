/* ================= 望江南·超然台作 · 三境场景（烟雨江南·登台变体：风细柳斜、烟雨千家、新火新茶） ================= */

/* 超然台：夯土高台（两层收分 + 压沿）+ 台顶木栏杆 + 北面踏道，合批 1 mesh；返回 {g, topY} */
function makeTerrace(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const stone=o.stone===undefined?0x1c222c:o.stone, stone2=shadeColor(stone,1.28);
  const wood=o.wood===undefined?0x2e2620:o.wood;
  const B=new GeoBag();
  const b1=new THREE.BoxGeometry(24,4.6,18); b1.translate(0,2.3,0); B.put(b1,stone);
  const b1t=new THREE.BoxGeometry(24.6,0.34,18.6); b1t.translate(0,4.7,0); B.put(b1t,stone2);
  const b2=new THREE.BoxGeometry(20,3.4,15); b2.translate(0,6.55,0); B.put(b2,stone);
  const top=new THREE.BoxGeometry(21,0.5,16); top.translate(0,8.55,0); B.put(top,stone2);
  /* 台顶栏杆（前缘 + 两侧） */
  const railY=9.4, postH=1.5;
  const rf=new THREE.BoxGeometry(20.4,0.13,0.16); rf.translate(0,railY,7.8); B.put(rf,shadeColor(wood,1.35));
  const rf2=new THREE.BoxGeometry(20.4,0.10,0.13); rf2.translate(0,railY-0.55,7.8); B.put(rf2,shadeColor(wood,1.1));
  [-10,10].forEach(function(sx){ const sp=new THREE.BoxGeometry(0.16,postH,0.16); sp.translate(sx,railY-0.35,7.8); B.put(sp,wood); });
  for(let i=-4;i<=4;i++){ const p=new THREE.BoxGeometry(0.11,postH*0.9,0.11); p.translate(i*2.3,railY-0.4,7.8); B.put(p,wood); }
  [-10.2,10.2].forEach(function(sx){
    const rl=new THREE.BoxGeometry(0.16,0.13,15.4); rl.translate(sx,railY,0); B.put(rl,shadeColor(wood,1.35));
    [-7.4,0,7.4].forEach(function(sz){ const p=new THREE.BoxGeometry(0.16,postH*0.9,0.16); p.translate(sx,railY-0.4,sz); B.put(p,wood); });
  });
  /* 北面门洞 + 登台踏步 */
  const door=new THREE.BoxGeometry(3.2,2.6,0.8); door.translate(0,1.3,9.05); B.put(door,shadeColor(stone,0.62));
  for(let i=0;i<5;i++){ const st=new THREE.BoxGeometry(3.4-i*0.5,0.34,1.0); st.translate(0,0.17+i*0.36,9.9+i*0.75); B.put(st,stone2); }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4654,emissive:0x080b10}),{c:o.rimC===undefined?0x9ab0c9:o.rimC,i:0.24,p:2.4})));
  g.scale.setScalar(s);
  return {g, topY:8.8*s};
}

/* 密州屋舍：盒身 + 四棱锥顶（一簇一 draw call） */
function makeCityHouses(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?77:o.seed);
  const n=o.n===undefined?90:o.n;
  const w=o.w===undefined?70:o.w, z0=o.z0===undefined?-42:o.z0, z1=o.z1===undefined?-100:o.z1;
  const sMin=o.sMin===undefined?1.8:o.sMin, sMax=o.sMax===undefined?3.4:o.sMax;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=z0+R()*(z1-z0), s=sMin+R()*(sMax-sMin), hh=s*(0.8+R()*0.6);
    const bd=new THREE.BoxGeometry(s,hh,s*0.85);
    bd.translate(x,hh/2,z); B.put(bd,shadeColor(0x232b36,0.8+R()*0.45));
    const roof=new THREE.ConeGeometry(s*0.74,hh*0.42,4);
    roof.rotateY(Math.PI/4); roof.translate(x,hh+hh*0.2,z); B.put(roof,shadeColor(0x181d26,0.85+R()*0.4));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3644,emissive:0x070a10}),{c:o.rimC===undefined?0x8fa4bc:o.rimC,i:0.18,p:2.4})));
  return g;
}

/* 城墙：十二边形环 + 压顶走道（1 mesh） */
function makeCityWall(o){
  o=o||{};
  const r=o.r===undefined?44:o.r, h=o.h===undefined?3.6:o.h;
  const B=new GeoBag();
  const ring=new THREE.CylinderGeometry(r,r*1.06,h,12,1,true);
  ring.translate(0,h/2,0); B.put(ring,0x1a212b);
  const walk=new THREE.CylinderGeometry(r*1.02,r*1.02,0.3,12,1,false);
  walk.translate(0,h+0.15,0); B.put(walk,shadeColor(0x1a212b,1.2));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3644,emissive:0x060a0e,side:THREE.DoubleSide}),{c:0x8fa4bc,i:0.16,p:2.4})));
  return g;
}

/* 城门楼（架在墙上，1 mesh） */
function makeGateTower(){
  const B=new GeoBag();
  const b=new THREE.BoxGeometry(7,4.2,4); b.translate(0,2.1,0); B.put(b,0x1d242e);
  const roof=new THREE.ConeGeometry(5.2,1.7,4); roof.rotateY(Math.PI/4); roof.translate(0,5.0,0); B.put(roof,0x141a22);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3644,emissive:0x070a10}),{c:0x8fa4bc,i:0.2,p:2.4})));
  return g;
}

/* 柳：主干 + 垂丝（复用 FG 风动着色器，1 mesh/株；垂丝陡垂成裙，不是竖立的枝） */
function makeWillow(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?97:o.seed);
  const h=o.h===undefined?9.5:o.h;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.09,0.22,h,7);
  trunk.translate(0,h/2,0); B.put(trunk,0x241f16);
  const fr=o.n===undefined?24:o.n;
  for(let i=0;i<fr;i++){
    const a=(i/fr)*6.283+R()*0.6, rr=R()*1.1;
    let px=Math.cos(a)*rr, py=h*(0.86+R()*0.14), pz=Math.sin(a)*rr;
    const cx=Math.cos(a), cz=Math.sin(a);
    for(let k=0;k<6;k++){
      const L=(1.3+R()*0.5)*(1-k/6*0.2);
      const drop=L*(0.55+0.14*k), hor=L*0.14, len=Math.hypot(drop,hor);
      const pg=new THREE.PlaneGeometry(0.12+R()*0.07,len,1,2);
      pg.rotateX(Math.PI-Math.atan2(hor,drop));
      pg.rotateY(Math.atan2(cx,cz));
      pg.translate(px+cx*hor*0.5, py-drop*0.5, pz+cz*hor*0.5);
      B.put(pg,0x2e3c26);
      px+=cx*hor; py-=drop; pz+=cz*hor;
    }
  }
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:1.3},uC:{value:C(0x28321f)},
      uTipC:{value:C(0x4c5c31)},uFade:{value:1}},
    vertexShader:FG_VERT,fragmentShader:FG_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mt); mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t,fk){ if(fk!==undefined)mt.uniforms.uFade.value=fk; mt.uniforms.uTime.value=t; };
  g.userData.update=g.update;
  return {g,update:g.update};
}

function bCover(){ // 封面 · 超然台远望
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x10141a,c2:0x1a222a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0d1118,atmo:0x33414e,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,44); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x0a0d13,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  /* 远处超然台 + 台上凭栏人剪影 */
  const terrace=makeTerrace({scale:0.9}); terrace.g.position.set(0,-1,-52); g.add(terrace.g);
  const poet=makeFigure({pose:'独立',robe:0x3a4250,belt:0x6a5a44,hat:'发髻',scale:0.8,rim:0.45,rimC:0x9ab0c9});
  poet.position.set(0,6.9,-53.5); poet.rotation.y=Math.PI; g.add(poet);
  /* 远城千家灯火（微暗） */
  const cityGlow=makeGlow({n:70,box:[110,5,40],pos:[0,3,-92],color:0xd89a58,size:4.5,speed:0.05,rise:0,maxA:0.14});
  g.add(cityGlow.points);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xa8bcd4,size:8,speed:0.05,rise:0,maxA:0.42});
  g.add(motes.points);
  addLights(g,{c:0x9ab0c9,i:0.42,p:[30,70,40]},{c:0x222c38,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); cityGlow.update(t); poet.update(t,k); }};
}
function bFengliu(){ // 一 · 风细柳斜 —— 春未老，风细柳斜斜；试上超然台看半壕春水一城花
  const g=new THREE.Group();
  const water=makeWater({size:520,seg:88,amp:0.26,freq:0.12,speed:0.5,flow:[-0.4,0.15],spec:1.6,
    deep:0x0b131e,shallow:0x224052,skyc:0x2e4254,moonDir:[-80,70,-170]});
  g.add(water.mesh);
  const bankN=makeGround({r:95,c1:0x10151c,c2:0x192028});
  bankN.mesh.position.set(0,-0.5,20); g.add(bankN.mesh);
  const bankF=makeGround({r:80,c1:0x10151c,c2:0x182026});
  bankF.mesh.position.set(0,-0.4,-42); g.add(bankF.mesh);
  const ridge=makeRange({r:240,h:24,layers:2,peaks:4,seed:671,color:0x0d1118,atmo:0x34424e,fogK:0.62,glowK:0.06,y:-12});
  g.add(ridge.g);
  /* 对岸城郭：半壕春水之外，一城花 */
  const wall=makeCityWall({r:26,h:3.2}); wall.position.set(0,0.2,-78); g.add(wall);
  const houses=makeCityHouses({n:64,w:64,z0:-56,z1:-96,seed:673,sMin:1.6,sMax:3.0}); g.add(houses);
  const bloom=makeGlow({n:90,box:[110,7,36],pos:[0,4.2,-78],color:0xc8899a,size:6.5,speed:0.04,rise:0,maxA:0.22});
  g.add(bloom.points);
  /* 超然台 + 台上凭栏人 */
  const terrace=makeTerrace({scale:1.15}); terrace.g.position.set(0,-0.4,-30); g.add(terrace.g);
  const poet=makeFigure({pose:'独立',robe:0x3a4250,belt:0x6a5a44,hat:'发髻',beard:true,scale:1.16,rim:0.55,rimC:0x9ab0c9});
  poet.position.set(-1.4,9.6,-21.5); poet.rotation.y=Math.PI+0.12; g.add(poet);
  /* 岸柳三株（风细柳斜斜） */
  const wl1=makeWillow({h:10,seed:681,n:18}); wl1.g.position.set(-15,-0.3,-8); g.add(wl1.g);
  const wl2=makeWillow({h:11,seed:683,n:16}); wl2.g.position.set(15.5,-0.3,-13); g.add(wl2.g);
  const wl3=makeWillow({h:8.5,seed:687,n:12}); wl3.g.position.set(-7.5,-0.3,7); g.add(wl3.g);
  /* 花瓣缓浮 */
  const petals=makeGlow({n:70,box:[80,11,55],pos:[0,7,-16],color:0xd8c8d0,size:3.2,speed:0.12,rise:1,add:false,maxA:0.3});
  g.add(petals.points);
  const mist=makeMist({n:6,spread:[240,22,120],pos:[0,9,-56],scale:76,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:8,color:0x0a0d13,seed:691,rim:0.15});
  rk.g.position.set(-15,-1.0,16); g.add(rk.g);
  addLights(g,{c:0x9ab0c9,i:0.46,p:[-40,80,-30]},{c:0x232e3a,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); petals.update(t); mist.update(t,k);
    poet.update(t,k); rk.update(t,k); bloom.update(t);
    wl1.update(t); wl2.update(t); wl3.update(t);
  }};
}
function bYanyu(){ // 二（标志性瞬间）· 烟雨千家 —— 登台俯瞰：半壕春水绕城郭，烟雨暗千家（灯火渐次黯淡）
  const g=new THREE.Group(), ctl={t:0};
  const water=makeWater({size:430,seg:86,amp:0.32,freq:0.11,speed:0.55,flow:[-0.5,0.2],spec:1.5,
    deep:0x0a121c,shallow:0x182c3a,skyc:0x223442,moonDir:[-70,60,-160]});
  g.add(water.mesh);
  const island=makeGround({r:43,c1:0x11161d,c2:0x1a212a});
  island.mesh.position.set(0,0.32,-58); g.add(island.mesh);
  const ridge=makeRange({r:300,h:30,layers:3,peaks:5,seed:701,color:0x0c1016,atmo:0x32414e,fogK:0.60,glowK:0.05,y:-16});
  g.add(ridge.g);
  /* 城郭：墙 + 门楼 + 屋舍两簇（拉近加密，千家可读） */
  const wall=makeCityWall({r:38,h:3.6}); wall.position.set(0,0.3,-58); g.add(wall);
  const gate=makeGateTower(); gate.position.set(0,3.9,-21.8); g.add(gate);
  const housesN=makeCityHouses({n:130,w:66,z0:-26,z1:-88,seed:703,sMin:2.0,sMax:4.2}); housesN.position.set(0,0.32,0); g.add(housesN);
  const housesF=makeCityHouses({n:60,w:100,z0:-88,z1:-104,seed:707,sMin:1.4,sMax:2.2}); g.add(housesF);
  /* 千家灯火（随烟雨渐次黯淡） */
  const lights=makeGlow({n:150,box:[72,3.5,58],pos:[0,2.6,-58],color:0xd89a58,size:6,speed:0.06,rise:0,maxA:0.30});
  g.add(lights.points);
  /* 烟雨渐起：斜雨 + 湿雾 */
  const rain=makeGlow({n:300,box:[200,40,140],pos:[0,20,-48],color:0x9fb4c8,size:3.6,speed:0.7,rise:1,add:false,maxA:0.14});
  rain.points.renderOrder=3; g.add(rain.points);
  const mist=makeMist({n:8,spread:[280,24,170],pos:[0,9,-56],scale:84,color:0x8fa4c0,op:0.13});
  g.add(mist.g);
  /* 超然台（脚下场）+ 台上凭栏人背影 */
  const terrace=makeTerrace({scale:1.2}); terrace.g.position.set(0,-0.2,-2); g.add(terrace.g);
  const poet=makeFigure({pose:'独立',robe:0x3a4250,belt:0x6a5a44,hat:'发髻',beard:true,scale:1.15,rim:0.55,rimC:0x9ab0c9});
  poet.position.set(3.2,10.3,-11.6); poet.rotation.y=Math.PI-0.3; g.add(poet);
  const rk=makeForeground({kind:'坡石',n:2,r:2.6,w:14,d:6,color:0x0a0d13,seed:711,rim:0.14});
  rk.g.position.set(-7.5,10.2,2.5); g.add(rk.g);
  addLights(g,{c:0x8ba0b8,i:0.34,p:[-50,90,-40]},{c:0x1e2632,i:0.6});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const dim=sstep(5,17,ctl.t);
      ridge.update(t,0); water.update(t); mist.update(t,k);
      poet.update(t,k); rk.update(t,k);
      lights.update(t); rain.update(t);
      lights.mat.uniforms.uMaxA.value=k*(0.30-0.18*dim)*(0.9+0.1*Math.sin(t*2.4));
      rain.mat.uniforms.uMaxA.value=k*(0.14+0.28*dim);
    },clicked:false};
}
function bXinhuo(){ // 三（末境·可点击）· 新火新茶 —— 且将新火试新茶（点击：茶烟袅起，千家烟雨渐明）
  const g=new THREE.Group(), ctl={t:0,clicked:false,done:0};
  const water=makeWater({size:430,seg:80,amp:0.28,freq:0.11,speed:0.5,flow:[-0.45,0.18],spec:1.4,
    deep:0x0a121c,shallow:0x182c3a,skyc:0x223442,moonDir:[-70,60,-160]});
  g.add(water.mesh);
  const island=makeGround({r:43,c1:0x11161d,c2:0x1a212a});
  island.mesh.position.set(0,0.32,-58); g.add(island.mesh);
  const ridge=makeRange({r:300,h:28,layers:2,peaks:4,seed:721,color:0x0c1016,atmo:0x30404c,fogK:0.60,glowK:0.05,y:-16});
  g.add(ridge.g);
  const wall=makeCityWall({r:38,h:3.6}); wall.position.set(0,0.3,-58); g.add(wall);
  const housesN=makeCityHouses({n:120,w:66,z0:-26,z1:-88,seed:703,sMin:2.0,sMax:4.2}); housesN.position.set(0,0.32,0); g.add(housesN);
  /* 千家灯火（点击后渐明） */
  const lights=makeGlow({n:150,box:[72,3.5,58],pos:[0,2.6,-58],color:0xd89a58,size:6,speed:0.06,rise:0,maxA:0.05});
  g.add(lights.points);
  /* 残雨（点击后收干） */
  const driz=makeGlow({n:80,box:[200,36,120],pos:[0,20,-50],color:0x9fb4c8,size:3.2,speed:0.55,rise:1,add:false,maxA:0.16});
  driz.points.renderOrder=3; g.add(driz.points);
  const mist=makeMist({n:5,spread:[280,24,170],pos:[0,10,-70],scale:84,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  /* 台上茶案 + 凭栏人（坐饮） */
  const terrace=makeTerrace({scale:1.5}); terrace.g.position.set(0,-0.2,-2); g.add(terrace.g);
  const topY=13.0;
  const table=makeTable({w:4.6,d:2.4,h:1.5,wood:0x2d2018});
  table.g.position.set(-0.8,topY,-6.2); g.add(table.g);
  const poet=makeFigure({pose:'坐饮',robe:0x40424c,belt:0x6a5a44,hat:'发髻',beard:true,scale:1.06,rim:0.55,rimC:0x9ab0c9,noProp:true});
  poet.position.set(-0.8,topY-0.5,-8.0); poet.rotation.y=0.30; g.add(poet);
  /* 新火试茶：陶壶 + 茶盏 + 茶烟 */
  const pot=makeVessel({type:'壶',mat:'陶',scale:0.55,shadow:false}); pot.g.position.set(0.2,topY+1.5,-6.0); g.add(pot.g);
  const bowl=makeVessel({type:'碗',mat:'陶',scale:0.42,shadow:false}); bowl.g.position.set(-2.2,topY+1.5,-6.6); g.add(bowl.g);
  const steam=makeGlow({n:60,box:[1.1,6,1.1],pos:[0.2,topY+2.1,-6.0],color:0xd8c6ac,size:3.2,speed:0.22,rise:1,maxA:0.18});
  steam.points.renderOrder=4; g.add(steam.points);
  /* 新火：寒食禁火后重起的小火炉（全境一点暖） */
  const brazier=makeBrazier({r:0.6,fh:1.15,fw:0.48,light:0.9,lightD:18,embers:16,spark:true});
  brazier.g.position.set(2.6,topY,-5.0); g.add(brazier.g);
  const burst=makeBurst({n:40,color:0xffc890,pos:[2.6,topY+0.9,-5.0]}); g.add(burst.points);
  /* 千家暖光（点击后亮起；构造强度=写入最大值，供引擎 setFade 记 baseI 包络） */
  const warmL=new THREE.PointLight(0xd89058,2.3,90); warmL.position.set(0,12,-58); g.add(warmL);
  const rk=makeForeground({kind:'坡石',n:2,r:2.6,w:13,d:6,color:0x0a0d13,seed:731,rim:0.14});
  rk.g.position.set(-9.5,12.85,3); g.add(rk.g);
  addLights(g,{c:0x8fa4bc,i:0.36,p:[-40,90,-30]},{c:0x212a34,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.done=Math.min(1,ctl.done+dt/3.0);
      ridge.update(t,0); water.update(t); mist.update(t,k);
      poet.update(t,k); rk.update(t,k);
      pot.update(t,k); bowl.update(t,k);
      brazier.update(t,k); burst.update(t);
      lights.update(t); driz.update(t); steam.update(t);
      lights.mat.uniforms.uMaxA.value=k*(0.05+0.42*ctl.done);
      driz.mat.uniforms.uMaxA.value=k*(0.16*(1-ctl.done*0.85));
      steam.mat.uniforms.uMaxA.value=k*(0.18+0.28*ctl.done);
      warmL.intensity=k*(0.25+2.0*ctl.done*(0.9+0.1*Math.sin(t*2.2)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(0,0.1,0.13); pluck(2,0.55,0.11); pluck(4,1.0,0.11);
        const fl=$('#flash'); fl.textContent='诗酒趁年华'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
