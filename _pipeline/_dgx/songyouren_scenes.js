/* ================= 送友人 · 四境场景（水墨夜思·送别变体：青山白水、孤蓬远征、浮云落日、萧萧班马） ================= */

/* 马：身颈首尾蹄全合批（同逢入京使，深色版） */
function makeHorseS(o){
  o=o||{};
  const c=o.color===undefined?0x2c241c:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.0,10,8); body.scale(1.9,1.0,0.72); body.translate(0,1.7,0); B.put(body,c);
  const neck=new THREE.CylinderGeometry(0.28,0.42,1.5,7);
  neck.rotateZ(-0.6); neck.translate(1.55,2.5,0); B.put(neck,shadeColor(c,0.9));
  const head=new THREE.SphereGeometry(0.34,8,6); head.scale(1.5,0.9,0.7);
  head.translate(2.25,3.2,0); B.put(head,shadeColor(c,1.1));
  const tail=new THREE.ConeGeometry(0.14,1.1,6); tail.rotateZ(0.5);
  tail.translate(-1.85,1.9,0); B.put(tail,shadeColor(c,0.7));
  [[0.85,-0.32],[0.85,0.32],[-0.95,-0.32],[-0.95,0.32]].forEach(function(p){
    B.put(limbGeo([p[0],1.3,p[1]],[p[0]*1.05,0.06,p[1]],0.13,0.07,6),shadeColor(c,0.85));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3c3a34,emissive:0x060504}),{c:o.rimC===undefined?0x9db4c8:o.rimC,i:0.28,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

/* 飞蓬：一团枯蓬（线球状，随风翻滚） */
function makePeng(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?551:o.seed);
  const B=new GeoBag();
  for(let i=0;i<16;i++){
    const a=R()*6.283, e=(R()-0.3)*3.0, r=0.4+R()*0.7;
    B.put(limbGeo([0,0,0],[Math.cos(a)*Math.cos(e)*r,Math.sin(e)*r+0.3,Math.sin(a)*Math.cos(e)*r],0.03,0.012,4),0x6a5a3a);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a4030,emissive:0x0a0906}),{c:0xb0a080,i:0.2,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 水墨送别地
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07080c,c2:0x111420});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:30,layers:2,peaks:4,seed:41,color:0x080b12,atmo:0x22344c,fogK:0.74,glowK:0.09,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x04060a,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.42});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.4,p:[30,70,40]},{c:0x1c2436,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bQingshan(){ // 一 · 青山白水 —— 城郭山水间的送别之地
  const g=new THREE.Group();
  /* 青山横北郭：横陈的青山 */
  const ridge=makeRange({r:200,h:44,layers:3,peaks:4,seed:561,color:0x0a1018,atmo:0x2c4458,fogK:0.62,glowK:0.08});
  ridge.g.position.set(0,0,-52); g.add(ridge.g);
  /* 白水绕东城：绕城的河湾 */
  const water=makeWater({size:560,seg:90,amp:0.3,freq:0.1,speed:0.6,flow:[0.9,0.2],spec:1.4,
    deep:0x081420,shallow:0x143c54,skyc:0x244668,moonDir:[-60,110,-160]});
  water.mesh.rotation.y=0.3; g.add(water.mesh);
  /* 城郭一角（东城） */
  const wall=new THREE.Mesh(new THREE.BoxGeometry(26,5.5,3.4),
    new THREE.MeshPhongMaterial({color:0x14161c,shininess:5}));
  wall.position.set(-22,2.7,-8); wall.rotation.y=0.6; g.add(wall);
  const tower=new THREE.Mesh(new THREE.BoxGeometry(6,8.5,5),
    new THREE.MeshPhongMaterial({color:0x14161c,shininess:5}));
  tower.position.set(-30,4.2,-2); tower.rotation.y=0.6; g.add(tower);
  /* 河湾渡口小舟 */
  const boat=new THREE.Mesh(new THREE.CylinderGeometry(1.4,1.0,0.5,10),
    new THREE.MeshPhongMaterial({color:0x1e160e,shininess:8}));
  boat.scale.set(2.2,1,0.8); boat.position.set(4,0,-4); g.add(boat);
  const mist=makeMist({n:8,spread:[220,22,120],pos:[0,9,-42],scale:72,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x04060a,seed:99,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:101,sway:0.9});
  reeds.g.position.set(13,-1.3,11); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.48,p:[-40,90,-40]},{c:0x1c2436,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    rk.update(t,k); reeds.update(t,k);
  }};
}
function bGupeng(){ // 二 · 孤蓬远征 —— 一别之后，孤蓬随风万里
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x07080c,c2:0x10141c});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:34,layers:3,peaks:5,seed:571,color:0x090c12,atmo:0x26384c,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 长路伸向天际 */
  const road=new THREE.Mesh(new THREE.BoxGeometry(2.6,0.06,120),
    new THREE.MeshPhongMaterial({color:0x161c26,shininess:8,specular:0x2c3646}));
  road.rotation.y=0.14; road.position.set(4,0.03,-34); g.add(road);
  /* 孤蓬：几团飞蓬沿路翻滚远去（风中之物） */
  const pengs=[];
  for(let i=0;i<4;i++){
    const p=makePeng({seed:551+i});
    p.position.set(4+i*4,0.8,-14-i*10); g.add(p);
    pengs.push({p,ph:i*1.4});
  }
  /* 背影：目送之人 */
  const poet=makeFigure({pose:'独立',robe:0x1c2230,belt:0x8a6a33,hat:'幞头',face:0.1,scale:1.2,rim:0.5,rimC:0x9db4c8});
  poet.position.set(-2,0,-6); g.add(poet);
  const mist=makeMist({n:8,spread:[220,22,120],pos:[0,9,-48],scale:74,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x04060a,seed:103,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.46,p:[-50,90,-50]},{c:0x1a2434,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    poet.update(t,k); rk.update(t,k);
    for(const o of pengs){
      o.p.position.x=4+((t*2.2+o.ph*8)%30);
      o.p.position.y=0.8+Math.abs(Math.sin(t*2.5+o.ph))*0.9;
      o.p.rotation.y=t*1.6+o.ph;
    }
  }};
}
function bFuyun(){ // 三（标志性瞬间）· 浮云落日 —— 浮云游子意，落日故人情
  const g=new THREE.Group();
  const ridge=makeRange({r:230,h:24,layers:2,peaks:4,seed:581,color:0x080b10,atmo:0x2c3450,fogK:0.60,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  /* 落日：西天一轮将沉不沉（故人情） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(10,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xe8a860,transparent:true,opacity:0.92,fog:false}));
  sun.position.set(-46,22,-130); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88840,
    transparent:true,opacity:0.4,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(70,70,1); sunGlow.position.set(-46,22,-130); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 浮云：几缕缓移的云带（游子意，自写云片） */
  const clouds=new THREE.Group();
  for(let i=0;i<5;i++){
    const c=new THREE.Mesh(new THREE.CylinderGeometry(2.2+i*0.6,2.2+i*0.6,0.7,10),
      new THREE.MeshPhongMaterial({color:0x2a3242,transparent:true,opacity:0.75,shininess:4}));
    c.position.set(-20+i*11,26+Math.sin(i*2.3)*4,-96-i*4);
    clouds.add(c);
  }
  g.add(clouds);
  /* 水面染落日余光 */
  const water=makeWater({size:620,seg:90,amp:0.3,freq:0.1,speed:0.5,flow:[0.4,0.2],spec:1.5,
    deep:0x081420,shallow:0x16384e,skyc:0x2a4258,moonDir:[-60,40,-160]});
  g.add(water.mesh);
  const gold=makeGlow({n:90,box:[80,2.5,46],pos:[-26,1,-46],color:0xd89858,size:7,speed:0.06,rise:0,maxA:0.35});
  g.add(gold.points);
  /* 送别二人（一挥手一抱拳位） */
  const f1=makeFigure({pose:'独立',robe:0x1c2230,hat:'幞头',face:0.4,scale:1.2,rim:0.5,rimC:0x9db4c8});
  f1.position.set(-2,0,-5); g.add(f1);
  const f2=makeFigure({pose:'独立',robe:0x2c2420,hat:'发髻',face:-0.4,scale:1.18,rim:0.48,rimC:0xd8b090});
  f2.position.set(2.4,0,-5.5); g.add(f2);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-48],scale:70,color:0x8fa4c4,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x04060a,seed:105,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc09060,i:0.42,p:[-60,40,-40]},{c:0x1c2434,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); gold.update(t); mist.update(t,k);
    clouds.children.forEach(function(c,i){ c.position.x+=0.006*(i+1); if(c.position.x>40)c.position.x=-40; });
    sunGlow.material.opacity=k*(0.34+0.05*Math.sin(t*0.5));
    f1.update(t,k); f2.update(t,k); rk.update(t,k);
  }};
}
function bBanma(){ // 四（末境·可点击）· 萧萧班马 —— 挥手自兹去，点击双马萧萧长鸣
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,neigh:0};
  const grd=makeGround({r:120,c1:0x07080c,c2:0x10141c});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:36,layers:2,peaks:4,seed:591,color:0x090c12,atmo:0x26384c,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 岔路：一往东南一往西北 */
  [[-0.35,-10],[0.35,-10]].forEach(function(p,i){
    const road=new THREE.Mesh(new THREE.BoxGeometry(2.2,0.06,50),
      new THREE.MeshPhongMaterial({color:0x161c26,shininess:8,specular:0x2c3646}));
    road.rotation.y=p[0]; road.position.set(i?7:-7,0.02,-20); g.add(road);
  });
  /* 两匹班马（分立岔路口） */
  const mA=makeHorseS({}); mA.position.set(-4,0,-6); mA.rotation.y=0.7; g.add(mA);
  const mB=makeHorseS({color:0x363028}); mB.position.set(4.5,0,-7); mB.rotation.y=-0.7; g.add(mB);
  /* 两声嘶鸣的声纹（点击后荡开） */
  const arcs=[];
  for(let i=0;i<3;i++){
    const pts=[];
    for(let k2=0;k2<=20;k2++){
      const a=-1.0+k2/20*2.0, r=1.5+i*2.6;
      pts.push(new THREE.Vector3(-4+Math.sin(a)*r,3.2+Math.cos(a)*r*0.7,-6+Math.cos(a)*r));
    }
    const ln=new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),
      new THREE.LineBasicMaterial({color:0x9db4c8,transparent:true,opacity:0.5,fog:false}));
    g.add(ln); arcs.push(ln);
  }
  /* 挥手的二人（渐行渐远的小背影） */
  const f1=makeFigure({pose:'指月',robe:0x1c2230,hat:'幞头',face:-0.3,scale:1.1,rim:0.48,rimC:0x9db4c8,noProp:true});
  f1.position.set(-9,0,-14); g.add(f1);
  const f2=makeFigure({pose:'独立',robe:0x2c2420,hat:'发髻',face:0.3,scale:1.08,rim:0.46,rimC:0xd8b090});
  f2.position.set(9,0,-16); g.add(f2);
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-42],scale:68,color:0x8fa4c4,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x04060a,seed:107,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.44,p:[-40,80,-40]},{c:0x1a2434,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.neigh=Math.min(1,ctl.neigh+dt/2.4);
      ridge.update(t,0); mist.update(t,k); rk.update(t,k);
      f1.update(t,k); f2.update(t,k);
      for(let i=0;i<arcs.length;i++){
        const ln=arcs[i];
        const ph=((t*0.5)+i/arcs.length)%1;
        ln.material.opacity=k*0.45*Math.sin(ph*Math.PI)*(1-ph*0.5)*Math.min(1,ctl.neigh*2);
        ln.scale.setScalar(0.6+ph*0.85);
      }
      mA.rotation.y=0.7+ctl.neigh*1.5+Math.sin(t*1.2)*0.03*Math.min(1,ctl.neigh*2);
      mB.rotation.y=-0.7-ctl.neigh*1.5-Math.sin(t*1.4)*0.03*Math.min(1,ctl.neigh*2);
      mA.position.y=Math.min(1,ctl.neigh*2)*Math.abs(Math.sin(t*5))*0.12;
      mB.position.y=Math.min(1,ctl.neigh*2)*Math.abs(Math.sin(t*5+1))*0.12;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.1,0.13); pluck(2,0.5,0.11);
        const fl=$('#flash'); fl.textContent='萧萧班马鸣'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
