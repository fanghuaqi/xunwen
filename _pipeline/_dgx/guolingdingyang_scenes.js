/* ================= 过零丁洋 · 四境场景（大漠金戈·正气变体：干戈四周、山河风雨、滩头洋里、丹心汗青） ================= */

/* 旌旗：横杆下悬挂的旗面（底边摆幅最大），军阵气象 */
const BANNER_VERT=`
uniform float uTime; varying vec2 vUv;
void main(){ vUv=uv; vec3 p=position;
  float k=pow(1.0-uv.y,1.35);
  p.z+=sin(uTime*2.2+uv.x*4.8)*0.36*k;
  p.x+=sin(uTime*1.5+uv.x*3.1)*0.09*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0); }`;
const BANNER_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade; varying vec2 vUv;
void main(){
  vec3 c=mix(uC,uTipC,pow(clamp(vUv.x,0.0,1.0),1.2));
  gl_FragColor=vec4(c,uFade*(0.95-0.22*vUv.x)); }`;
function makeBanner(o){
  o=o||{};
  const w=o.w===undefined?2.8:o.w, h=o.h===undefined?3.6:o.h, ph=o.poleH===undefined?9:o.poleH;
  const g=new THREE.Group();
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.055,0.085,ph,6); pole.translate(0,ph/2,0); B.put(pole,0x160f0a);
  const bar=new THREE.CylinderGeometry(0.035,0.035,w*0.7,5); bar.rotateZ(Math.PI/2); bar.translate(w*0.32,ph,0); B.put(bar,0x160f0a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x060403}),{c:0xc0784a,i:0.26,p:2.4})));
  const geo=new THREE.PlaneGeometry(w,h,10,3); geo.translate(0,-h/2,0);
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,depthWrite:false,
    uniforms:{uTime:{value:0},uC:{value:C(o.color===undefined?0x701e12:o.color)},
      uTipC:{value:C(o.tip===undefined?0xc85a38:o.tip)},uFade:{value:1}},
    vertexShader:BANNER_VERT,fragmentShader:BANNER_FRAG});
  const mesh=new THREE.Mesh(geo,mt); mesh.position.set(w*0.32,ph,0); mesh.renderOrder=1;
  g.add(mesh);
  g.userData.mt=mt;
  g.update=function(t,fk){ mt.uniforms.uTime.value=t; };
  return {g,mt,update:g.update};
}

/* 兵器架与残盾：兵荒马乱之意（合批 1 mesh） */
function makeWeapons(o){
  o=o||{};
  const B=new GeoBag();
  [-1.2,1.2].forEach(function(x){
    const spear=new THREE.CylinderGeometry(0.04,0.05,4.6,5);
    spear.translate(x,2.3,0); B.put(spear,0x2c2016);
    const tip=new THREE.ConeGeometry(0.1,0.5,4);
    tip.translate(x,4.8,0); B.put(tip,0x7a6a58);
  });
  const bar=new THREE.BoxGeometry(3.2,0.12,0.16); bar.translate(0,2.6,0); B.put(bar,0x3a2c1e);
  const shield=new THREE.BoxGeometry(1.6,2.2,0.14);
  shield.rotateZ(0.2); shield.translate(0,1.1,0.3); B.put(shield,0x4a3424);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x4a3c2e,emissive:0x080604}),{c:o.rimC===undefined?0xb0703a:o.rimC,i:0.25,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

/* 囚舟：海中一叶孤舟（载文天祥过零丁洋） */
function makePrisonBoat(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.85,0.48,5.4,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.5,1.5); B.put(hull,0x1e1610);
  const bow=new THREE.ConeGeometry(0.65,1.6,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.7,1.4); bow.translate(3.4,0.05,0); B.put(bow,0x1e1610);
  const cage=new THREE.BoxGeometry(2.4,1.8,1.6);
  cage.translate(-0.4,1.1,0); B.put(cage,0x2c221a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a2c20,emissive:0x070503}),{c:o.rimC===undefined?0xb0703a:o.rimC,i:0.26,p:2.4})));
  g.scale.setScalar(s);
  return g;
}

function bCover(){ // 封面 · 沧海沉浮
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0c0806,c2:0x1a1208});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x0d0906,atmo:0x442c16,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x080504,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xa87848,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xc89050,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xc07840,i:0.45,p:[30,70,40]},{c:0x281810,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bGange(){ // 一 · 干戈四周 —— 起一经，入仕四年苦战抗敌
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0b0805,c2:0x181008});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:42,layers:3,peaks:5,seed:981,color:0x0c0806,atmo:0x402412,fogK:0.62,glowK:0.07});
  g.add(ridge.g);
  /* 战阵残破：断旗与兵器架 */
  const wp1=makeWeapons({}); wp1.position.set(-6,0,-8); g.add(wp1);
  const wp2=makeWeapons({scale:0.9}); wp2.position.set(8,0,-12); wp2.rotation.y=0.4; g.add(wp2);
  /* 破残军旗 */
  const ban=makeBanner({w:2.4,h:3.2,poleH:9.5,color:0x641810,tip:0x9a3020});
  ban.g.position.set(-11,0,-14); ban.g.rotation.y=0.4; g.add(ban.g);
  /* 营盘篝火（四年风雨战乱） */
  const braz=makeBrazier({r:1.1,fh:2.4,fw:1.2,light:1.4,lightD:42,embers:24,spark:true});
  braz.g.position.set(5,0,-4); g.add(braz.g);
  /* 主帅文天祥（宋代官袍/士大夫装，按剑伫立） */
  const boss=makeFigure({pose:'按剑',robe:0x321e16,belt:0x7a4a20,collar:0xd8c8a8,hat:'幞头',
    beard:true,face:0.1,scale:1.35,rim:0.6,rimC:0xd08040});
  boss.position.set(-0.5,0,-5); g.add(boss);
  const army=makeCrowd({n:10,rect:[-20,-24,40,8],seed:983,color:0x16100a,rimC:0xb06830,rim:0.26,sMin:0.8,sMax:1.05});
  g.add(army.mesh);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-40],scale:70,color:0x8a5030,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080504,seed:173,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xb06830,i:0.44,p:[-40,70,-30]},{c:0x22140c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ban.update(t,k); braz.update(t,k);
    army.update(t); boss.update(t,k); mist.update(t,k); rk.update(t,k);
  }};
}
function bShanhe(){ // 二（标志性瞬间）· 山河风雨 —— 山河破碎风飘絮，身世浮沉雨打萍
  const g=new THREE.Group();
  /* 狂风暴雨的暗江/海面（风飘絮+雨打萍的双意象） */
  const water=makeWater({size:780,seg:100,amp:1.6,freq:0.08,speed:1.2,flow:[-1.2,0.6],spec:1.4,
    deep:0x0a141e,shallow:0x142e3e,skyc:0x203c4c,moonDir:[-60,80,-160]});
  g.add(water.mesh);
  const ridge=makeRange({r:230,h:32,layers:2,peaks:4,seed:991,color:0x0c1016,atmo:0x2e3846,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 风飘絮：狂风翻卷的暗白柳絮粒子（上下乱卷） */
  const xu=makeGlow({n:180,box:[160,34,100],pos:[0,16,-20],color:0xd4d8dc,size:4.5,speed:0.35,rise:1,maxA:0.45,add:false});
  xu.points.renderOrder=4; g.add(xu.points);
  /* 雨打萍：暴雨如麻（斜落雨丝）+ 水面青绿浮萍（颠簸沉浮） */
  const rain=makeGlow({n:300,box:[150,38,90],pos:[0,18,-14],color:0x94a4b4,size:4.0,speed:0.7,rise:1,maxA:0.55,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  /* 水面浮萍小圆片群（颠簸） */
  const pingGroup=new THREE.Group();
  const pmat=new THREE.MeshPhongMaterial({color:0x2a5034,shininess:16,specular:0x4a7a58});
  for(let i=0;i<18;i++){
    const disc=new THREE.Mesh(new THREE.CircleGeometry(0.5+((i*7)%5)*0.15,10),pmat);
    disc.rotation.x=-Math.PI/2;
    disc.position.set(-14+(i%6)*5,0.2,-8-(i>>1)*3);
    pingGroup.add(disc);
  }
  g.add(pingGroup);
  /* 远处破残的断壁与零落山河 */
  const ru=new THREE.Mesh(new THREE.BoxGeometry(16,7,3),
    new THREE.MeshPhongMaterial({color:0x141820,shininess:4}));
  ru.position.set(22,3.5,-30); ru.rotation.y=-0.4; g.add(ru);
  const mist=makeMist({n:8,spread:[240,24,130],pos:[0,10,-48],scale:76,color:0x6a7888,op:0.12});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080c10,seed:175,rim:0.14});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x7a90a8,i:0.4,p:[-40,80,-40]},{c:0x1a222e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); xu.update(t); rain.update(t); mist.update(t,k);
    rk.update(t,k);
    pingGroup.children.forEach(function(p,i){
      p.position.y=0.2+Math.sin(t*2.4+i*1.1)*0.12;
      p.rotation.z=Math.sin(t*1.8+i)*0.08;
    });
  }};
}
function bHuangtian(){ // 三 · 滩头洋里 —— 惶恐滩头说惶恐，零丁洋里叹零丁
  const g=new THREE.Group();
  /* 零丁洋沧海：汹涌惊涛 */
  const water=makeWater({size:800,seg:100,amp:1.8,freq:0.07,speed:1.1,flow:[-0.8,0.4],spec:1.5,
    deep:0x0a1420,shallow:0x163448,skyc:0x224258,moonDir:[-70,90,-160]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:36,layers:2,peaks:4,seed:1001,color:0x0a1016,atmo:0x283848,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 险滩礁石（惶恐滩意象） */
  [[-18,-18,5],[16,-24,6],[0,-34,7]].forEach(function(p,i){
    const reef=new THREE.Mesh(new THREE.ConeGeometry(p[2]*0.8,p[2]*1.2,6),
      new THREE.MeshPhongMaterial({color:0x101620,shininess:8}));
    reef.position.set(p[0],p[2]*0.4,p[1]); g.add(reef);
  });
  /* 零丁洋囚舟（一叶小舟，载文天祥独立） */
  const boat=makePrisonBoat({scale:1.4}); boat.position.set(0,0.4,-8); boat.rotation.y=0.2; g.add(boat);
  const boss=makeFigure({pose:'独立',robe:0x321e16,collar:0xd8c8a8,hat:'幞头',beard:true,face:0.1,scale:1.2,rim:0.55,rimC:0xb0703a});
  boss.position.set(0,1.5,-8); g.add(boss);
  /* 零丁洋海雾漫漫 */
  const mist=makeMist({n:8,spread:[240,24,130],pos:[0,10,-46],scale:80,color:0x7a8c9e,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080c10,seed:177,rim:0.14});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x8fa4b8,i:0.44,p:[-40,80,-40]},{c:0x1a222c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); rk.update(t,k);
    boat.position.y=0.4+Math.sin(t*1.2)*0.16;
    boat.rotation.z=Math.sin(t*0.9)*0.035;
    boss.position.y=1.5+Math.sin(t*1.2)*0.16;
    boss.update(t,k);
  }};
}
function bDanxin(){ // 四（末境·可点击）· 丹心汗青 —— 人生自古谁无死？留取丹心照汗青（点击：一片丹心化作明灯长明，汗青史册展开）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,flame:0};
  const water=makeWater({size:800,seg:100,amp:1.5,freq:0.075,speed:0.9,flow:[-0.6,0.3],spec:1.6,
    deep:0x0a1420,shallow:0x163448,skyc:0x24445c,moonDir:[0,100,-170]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:32,layers:2,peaks:4,seed:1011,color:0x0a1016,atmo:0x28384a,fogK:0.60,glowK:0.06});
  ridge.g.position.set(0,0,-80); g.add(ridge.g);
  /* 舟头文天祥（视死如归，独立舟头） */
  const boat=makePrisonBoat({scale:1.45}); boat.position.set(0,0.4,-6); boat.rotation.y=0.15; g.add(boat);
  const boss=makeFigure({pose:'独立',robe:0x341e16,collar:0xd8c8a8,hat:'幞头',beard:true,face:0,scale:1.3,rim:0.65,rimC:0xff9040});
  boss.position.set(0,1.55,-6); g.add(boss);
  /* 一片丹心（红心长明之火，点击后升起大亮） */
  const heart=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff3020,
    transparent:true,opacity:0.95,depthWrite:false,blending:THREE.AdditiveBlending}));
  heart.scale.set(6,6,1); heart.position.set(0,3.6,-5.5); heart.renderOrder=4; g.add(heart);
  /* 汗青卷轴（竹简史册展开的光带） */
  const scroll=new THREE.Mesh(new THREE.PlaneGeometry(18,5),
    new THREE.MeshPhongMaterial({color:0xd8c890,side:THREE.DoubleSide,transparent:true,opacity:0.75,
      shininess:30,specular:0xfff0b0,emissive:0x3a2810}));
  scroll.position.set(0,10,-18); g.add(scroll);
  const burst=makeBurst({n:100,color:0xff6030,pos:[0,8,-10]}); g.add(burst.points);
  const pl=new THREE.PointLight(0xff5020,2.2,46); pl.position.set(0,6,-5.5); g.add(pl);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-44],scale:74,color:0x7a8c9e,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080c10,seed:179,rim:0.14});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x90a8c0,i:0.42,p:[-40,80,-40]},{c:0x1a222c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.flame=Math.min(1,ctl.flame+dt/2.2);
      ridge.update(t,0); water.update(t); mist.update(t,k); rk.update(t,k);
      boss.update(t,k); burst.update(t);
      boat.position.y=0.4+Math.sin(t*1.1)*0.14;
      boss.position.y=1.55+Math.sin(t*1.1)*0.14;
      /* 丹心升起照亮汗青 */
      heart.position.y=3.6+ctl.flame*6;
      heart.scale.set(6+ctl.flame*10, 6+ctl.flame*10, 1);
      heart.material.opacity=k*0.95*(0.32+0.68*ctl.flame)*(0.85+0.15*Math.sin(t*6));
      scroll.material.opacity=k*0.75*ctl.flame;
      scroll.position.y=10+Math.sin(t*1.2)*0.3;
      pl.intensity=k*2.2*(0.25+0.75*ctl.flame*(0.85+0.15*Math.sin(t*5)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(0,0.1,0.15); pluck(2,0.5,0.13); pluck(4,0.9,0.12); bell();
        const fl=$('#flash'); fl.textContent='留取丹心照汗青'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
