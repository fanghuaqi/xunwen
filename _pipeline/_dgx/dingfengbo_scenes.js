/* ================= 定风波·莫听穿林打叶声 · 三境场景（烟雨江南·旷达变体：一蓑烟雨、山头斜照、无雨无晴） ================= */

/* 竹杖：细圆柱杖身 + 杖头弯柄（合批 1 mesh） */
function makeCane(o){
  o=o||{};
  const B=new GeoBag();
  const shaft=new THREE.CylinderGeometry(0.035,0.045,4.2,6);
  shaft.translate(0,2.1,0); B.put(shaft,0x3a2c1a);
  const hook=new THREE.TorusGeometry(0.24,0.04,5,10,Math.PI*1.1);
  hook.rotateZ(-Math.PI/2); hook.translate(-0.18,4.2,0); B.put(hook,0x3a2c1a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x4a4030,emissive:0x080705}),{c:0x8fb3c9,i:0.25,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

/* 竹林阵列：几株修竹 */
function makeBambooGrove(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?911:o.seed);
  const n=o.n===undefined?8:o.n, w=o.w===undefined?18:o.w, d=o.d===undefined?12:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, h=8+R()*4;
    const trunk=new THREE.CylinderGeometry(0.06,0.09,h,6);
    trunk.translate(x,h/2,z); B.put(trunk,0x243224);
    for(let k=0;k<3;k++){
      const lf=new THREE.PlaneGeometry(1.6,0.4);
      lf.rotateZ((R()-0.5)*0.8); lf.translate(x+(R()-0.5)*1.2,h*(0.5+k*0.18),z+(R()-0.5)*0.8);
      B.put(lf,0x3a5038);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3c2a,emissive:0x050a06,side:THREE.DoubleSide}),{c:0x8fb3c9,i:0.22,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 烟雨山林
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x10141a,c2:0x1a2228});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:28,layers:2,peaks:4,seed:41,color:0x0d1118,atmo:0x344052,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,44); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x0a0d13,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xa8bcd4,size:8,speed:0.05,rise:0,maxA:0.42});
  g.add(motes.points);
  addLights(g,{c:0x9aaec8,i:0.42,p:[30,70,40]},{c:0x222c38,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bYisuo(){ // 一（标志性瞬间）· 一蓑烟雨 —— 穿林打叶骤雨中，苏轼拄竹杖穿芒鞋，吟啸徐行
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0e1218,c2:0x161e26});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:32,layers:2,peaks:4,seed:921,color:0x0c1016,atmo:0x2c384a,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 斜风骤雨（密集的斜落雨丝） */
  const rain=makeGlow({n:380,box:[140,36,90],pos:[0,18,-16],color:0xa8bcd0,size:4.0,speed:0.65,rise:1,maxA:0.55,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  /* 竹林两簇（穿林打叶） */
  const groveL=makeBambooGrove({n:10,seed:923}); groveL.position.set(-14,0,-16); g.add(groveL);
  const groveR=makeBambooGrove({n:8,seed:925}); groveR.position.set(16,0,-20); g.add(groveR);
  /* 山间泥泞小路 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.06,56),
    new THREE.MeshPhongMaterial({color:0x1a1e22,shininess:12,specular:0x34404a}));
  path.rotation.y=0.18; path.position.set(2,0.02,-12); g.add(path);
  /* 主体：苏轼（蓑衣斗笠，右手拄杖，徐行从容） */
  const poet=makeFigure({pose:'独立',robe:0x3a3c36,belt:0x5a5440,hat:'发髻',face:0.2,scale:1.32,rim:0.55,rimC:0x8fb3c9});
  poet.position.set(1.5,0,-2); g.add(poet);
  const cane=makeCane({}); cane.position.set(2.8,0,-1.4); cane.rotation.z=-0.12; g.add(cane);
  /* 斗笠 */
  const hat=new THREE.Mesh(new THREE.ConeGeometry(1.0,0.35,8),
    new THREE.MeshPhongMaterial({color:0x4a3c28,shininess:6}));
  hat.position.set(1.5,5.1,-2); g.add(hat);
  /* 远处狼狈奔逃的同行者（剪影） */
  const runners=makeCrowd({n:3,rect:[-8,-32,16,10],seed:927,color:0x12161c,rimC:0x6a7a8a,rim:0.25,sMin:0.7,sMax:0.85});
  g.add(runners.mesh);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-40],scale:70,color:0x7a8ca0,op:0.12});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:20,d:8,color:0x080b10,seed:161,rim:0.15});
  rk.g.position.set(-13,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x8fa4c0,i:0.42,p:[-40,80,-40]},{c:0x1a222e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rain.update(t); mist.update(t,k);
    poet.update(t,k); runners.update(t); rk.update(t,k);
    cane.position.y=Math.sin(t*1.1)*0.04;
    hat.position.y=5.1+Math.sin(t*0.6)*0.03;
  }};
}
function bXiezhao(){ // 二 · 山头斜照 —— 料峭春风吹酒醒，山头斜照却相迎
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x10141a,c2:0x1c242c});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:36,layers:3,peaks:5,seed:931,color:0x0e1218,atmo:0x3c404c,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 山头夕阳斜照（穿透残云，金光洒山头） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(9,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xe8a050,transparent:true,opacity:0.92,fog:false}));
  sun.position.set(38,24,-110); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88840,
    transparent:true,opacity:0.45,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(70,70,1); sunGlow.position.set(38,24,-110); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 雨歇残云（渐渐稀疏的云雾） */
  const rainLeft=makeGlow({n:80,box:[100,20,60],pos:[-18,12,-20],color:0xa8bcd0,size:3.5,speed:0.3,rise:1,maxA:0.25,add:false});
  rainLeft.points.renderOrder=3; g.add(rainLeft.points);
  /* 金光洒在山道上 */
  const gold=makeGlow({n:90,box:[70,2.5,40],pos:[10,1,-24],color:0xd8a060,size:6,speed:0.05,rise:0,maxA:0.35});
  g.add(gold.points);
  /* 苏轼（酒醒微冷，抬头望山头斜照） */
  const poet=makeFigure({pose:'指月',robe:0x3a3c36,belt:0x5a5440,hat:'发髻',face:0.5,scale:1.3,rim:0.6,rimC:0xd8a060,noProp:true});
  poet.position.set(0,0,-4); g.add(poet);
  const cane=makeCane({}); cane.position.set(1.4,0,-3.4); cane.rotation.z=-0.12; g.add(cane);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-44],scale:72,color:0x8fa4c0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x0a0d13,seed:163,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc09060,i:0.48,p:[40,60,-30]},{c:0x222c38,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rainLeft.update(t); gold.update(t); mist.update(t,k);
    poet.update(t,k); rk.update(t,k);
    sunGlow.material.opacity=k*(0.40+0.05*Math.sin(t*0.6));
  }};
}
function bWufengyu(){ // 三（末境·可点击）· 无雨无晴 —— 回首萧瑟处，也无风雨也无晴（点击：风雨全消，斜阳洒满山径）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,peace:0};
  const grd=makeGround({r:130,c1:0x10141a,c2:0x1e2630});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:32,layers:3,peaks:5,seed:941,color:0x0d1118,atmo:0x364254,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 归去山径：蜿蜒伸向远山 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.06,70),
    new THREE.MeshPhongMaterial({color:0x1e242c,shininess:8,specular:0x364450}));
  path.rotation.y=-0.22; path.position.set(-3,0.02,-20); g.add(path);
  /* 苏轼（信步徐行归去的背影） */
  const poet=makeFigure({pose:'独立',robe:0x3a3c36,belt:0x5a5440,hat:'发髻',face:-0.3,scale:1.25,rim:0.55,rimC:0x8fb3c9});
  poet.position.set(-3,0,-8); g.add(poet);
  const cane=makeCane({}); cane.position.set(-1.8,0,-7.5); cane.rotation.z=-0.12; g.add(cane);
  /* 萧瑟处烟云（点击后烟消云散） */
  const rainMist=makeGlow({n:60,box:[80,18,50],pos:[16,8,-18],color:0x7a8ca0,size:6,speed:0.04,rise:0,maxA:0.3,add:false});
  g.add(rainMist.points);
  /* 斜阳暖辉（点击后大盛，洒满归途） */
  const warm=makeGlow({n:120,box:[120,20,80],pos:[0,8,-24],color:0xd8a058,size:8,speed:0.045,rise:0,maxA:0});
  g.add(warm.points);
  const burst=makeBurst({n:80,color:0xffd080,pos:[-3,6,-8]}); g.add(burst.points);
  const mist=makeMist({n:7,spread:[220,20,120],pos:[0,8,-44],scale:72,color:0x8fa4c0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:20,d:8,color:0x0a0d13,seed:165,rim:0.14});
  rk.g.position.set(-13,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x9aaec8,i:0.42,p:[-40,80,-40]},{c:0x222c38,i:0.62});
  const pl=new THREE.PointLight(0xffb060,1.4,40); pl.position.set(-3,6,-8); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.peace=Math.min(1,ctl.peace+dt/2.6);
      ridge.update(t,0); mist.update(t,k); rk.update(t,k); burst.update(t);
      poet.update(t,k);
      /* 风雨消、暖阳照 */
      rainMist.mat.uniforms.uMaxA.value=k*0.3*(1-ctl.peace*0.9);
      rainMist.update(t);
      warm.mat.uniforms.uMaxA.value=k*0.5*ctl.peace;
      warm.update(t);
      pl.intensity=k*1.4*(0.35+ctl.peace*0.65*(0.85+0.15*Math.sin(t*2.8)));
      poet.position.z=-8-ctl.peace*14;
      cane.position.z=-7.5-ctl.peace*14;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.5,0.12); pluck(5,0.9,0.12);
        const fl=$('#flash'); fl.textContent='也无风雨也无晴'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
