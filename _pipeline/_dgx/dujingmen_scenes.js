/* ================= 渡荆门送别 · 四境场景（水墨夜思·江月变体：渡远楚国、山平江阔、月镜海楼、故乡水送） ================= */

/* 小行舟：弯壳船体 + 篷（无帆，随波轻荡） */
function makeRowBoat(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.75,0.4,4.6,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.5,1.4); B.put(hull,0x241a10);
  const bow=new THREE.ConeGeometry(0.55,1.4,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.7,1.35); bow.translate(2.9,0.05,0); B.put(bow,0x241a10);
  const canopy=new THREE.CylinderGeometry(0.62,0.62,1.9,10,1,true,Math.PI,Math.PI);
  canopy.scale(1,0.8,1.25); canopy.rotateZ(Math.PI/2); canopy.translate(-0.4,0.75,0); B.put(canopy,0x3a2c1c);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a4658,emissive:0x080b12,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x9db8d8:o.rimC,i:0.3,p:2.5})));
  g.scale.setScalar(s);
  return g;
}

/* 海楼：云霞幻结的蜃楼（几层半透楼影，缓缓明灭） */
const MIRAGE_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const MIRAGE_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float band=smoothstep(0.0,0.25,vUv.y)*smoothstep(1.0,0.55,vUv.y);
  float col=0.55+0.45*sin(vUv.x*9.0+uTime*0.7);
  float a=uFade*uK*band*(0.42+0.26*col);
  gl_FragColor=vec4(vec3(0.84,0.90,1.0),a);
}`;
function makeMirage(o){
  o=o||{};
  const g=new THREE.Group();
  const mats=[];
  for(let i=0;i<3;i++){
    const w=(o.w===undefined?26:o.w)*(1-i*0.22), h=(o.h===undefined?16:o.h)*(1-i*0.18);
    const mt=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
      uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:(o.k===undefined?0.5:o.k)*(1-i*0.24)}},
      vertexShader:MIRAGE_VERT,fragmentShader:MIRAGE_FRAG});
    const m=new THREE.Mesh(new THREE.PlaneGeometry(w,h,1,1),mt);
    m.position.set((i-1)*w*0.8,h/2+12+i*5,(o.z===undefined?-60:o.z)+i*3);
    m.renderOrder=3; g.add(m); mats.push(mt);
  }
  g.userData.mats=mats;
  g.update=function(t,fk){ const k=fk===undefined?1:fk;
    for(const mt of mats){ mt.uniforms.uTime.value=t; mt.uniforms.uFade.value=k; } };
  return g;
}

function bCover(){ // 封面 · 蜀江月夜
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07080c,c2:0x11161f});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x080b12,atmo:0x24344c,fogK:0.74,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x04060a,seed:5,rim:0.16});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:70,box:[220,40,130],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.45});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.4,p:[30,70,40]},{c:0x1c2436,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bDujing(){ // 一 · 渡远楚国 —— 出峡口，江面初阔
  const g=new THREE.Group();
  const water=makeWater({size:520,seg:90,amp:0.5,freq:0.1,speed:0.8,flow:[1.1,0.2],spec:1.3,
    deep:0x081622,shallow:0x123a52,skyc:0x22405e,moonDir:[60,110,-160]});
  g.add(water.mesh);
  /* 两岸峡壁渐开（荆门口） */
  const cliffL=makeRange({r:170,h:52,layers:2,peaks:3,seed:341,arc:Math.PI*0.26,a0:Math.PI*0.60,
    color:0x070b12,atmo:0x2a3c58,fogK:0.66,glowK:0.10,y:-22});
  cliffL.g.position.set(-24,0,0); g.add(cliffL.g);
  const cliffR=makeRange({r:170,h:46,layers:2,peaks:3,seed:343,arc:Math.PI*0.24,a0:-Math.PI*0.42,
    color:0x070b12,atmo:0x2a3c58,fogK:0.66,glowK:0.10,y:-22});
  cliffR.g.position.set(24,0,0); g.add(cliffR.g);
  /* 主体：一叶行舟出峡 */
  const boat=makeRowBoat({scale:1.3,rimC:0xa8c0e0});
  boat.position.set(2,0.2,-2); g.add(boat);
  const mist=makeMist({n:8,spread:[220,24,120],pos:[0,9,-40],scale:72,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x04060a,seed:77,rim:0.16});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[-40,90,-40]},{c:0x1c2436,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    cliffL.update(t,0); cliffR.update(t,0); water.update(t); mist.update(t,k);
    boat.rotation.z=Math.sin(t*0.7)*0.03;
    boat.position.y=0.2+Math.sin(t*0.8)*0.1;
    rk.update(t,k);
  }};
}
function bDahuang(){ // 二 · 山平江阔 —— 山随平野尽，江入大荒流
  const g=new THREE.Group();
  /* 山影只剩最远处一线（"尽"） */
  const ridge=makeRange({r:260,h:16,layers:2,peaks:4,seed:351,color:0x080b10,atmo:0x1e2c40,fogK:0.60,glowK:0.06,y:-20});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 大江入荒原：极宽水面 */
  const water=makeWater({size:900,seg:100,amp:0.45,freq:0.075,speed:0.9,flow:[0,1.6],spec:1.5,
    deep:0x081826,shallow:0x14405c,skyc:0x24466a,moonDir:[70,120,-180]});
  g.add(water.mesh);
  /* 荒原两岸：低平滩地 */
  [[-70,-24],[70,-24]].forEach(function(p,i){
    const bank=new THREE.Mesh(new THREE.BoxGeometry(50,1.0,60),
      new THREE.MeshPhongMaterial({color:0x0c1018,shininess:6}));
    bank.rotation.y=i?-0.3:0.3; bank.position.set(p[0],0.2,p[1]); g.add(bank);
  });
  /* 一行雁影远去（空间感） */
  const geese=[];
  const bmat=new THREE.MeshBasicMaterial({color:0x0e141e,side:THREE.DoubleSide});
  for(let i=0;i<5;i++){
    const b=new THREE.Group();
    const w=new THREE.Mesh(new THREE.PlaneGeometry(2.4,0.6),bmat); b.add(w);
    b.position.set(-18+i*9,16+i*1.2,-70-i*6); g.add(b); geese.push(b);
  }
  const mist=makeMist({n:8,spread:[260,22,140],pos:[0,9,-56],scale:80,color:0x7e94b4,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x04060a,seed:81,rim:0.14});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:83,sway:0.8});
  reeds.g.position.set(13,-1.3,11); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[-50,100,-50]},{c:0x1a2434,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    geese.forEach(function(b,i){ b.rotation.y=Math.sin(t*0.5+i)*0.1; b.position.y=16+i*1.2+Math.sin(t*0.8+i)*0.8; });
    rk.update(t,k); reeds.update(t,k);
  }};
}
function bFeitianjing(){ // 三（标志性瞬间）· 月镜海楼 —— 月影飞天镜，云生结海楼
  const g=new THREE.Group();
  const ridge=makeRange({r:250,h:20,layers:2,peaks:3,seed:361,color:0x080b10,atmo:0x20304a,fogK:0.60,glowK:0.06,y:-20});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 静江如镜（低波高反光） */
  const water=makeWater({size:800,seg:100,amp:0.18,freq:0.13,speed:0.4,flow:[0.2,0.2],spec:2.0,
    deep:0x081420,shallow:0x14385a,skyc:0x2a5078,moonDir:[0,90,-170]});
  g.add(water.mesh);
  /* 月下飞天镜：天上月 + 江中月影（亮椭圆倒影） */
  const moonRef=new THREE.Mesh(new THREE.CircleGeometry(8,32),
    new THREE.MeshBasicMaterial({color:0xd8e4f4,transparent:true,opacity:0.5,depthWrite:false}));
  moonRef.rotation.x=-Math.PI/2; moonRef.scale.set(1,1.9,1);
  moonRef.position.set(0,0.15,-44); moonRef.renderOrder=2; g.add(moonRef);
  const moonHalo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  moonHalo.scale.set(13,8,1); moonHalo.position.set(0,1.5,-44); moonHalo.renderOrder=2; g.add(moonHalo);
  /* 云生结海楼 */
  const mirage=makeMirage({w:22,h:14,z:-64,k:0.7}); g.add(mirage);
  /* 舟行镜中 */
  const boat=makeRowBoat({scale:1.2,rimC:0xa8c0e0});
  boat.position.set(-6,0.2,-10); g.add(boat);
  const motes=makeGlow({n:70,box:[130,14,80],pos:[0,6,-24],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.35});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,20,110],pos:[0,8,-52],scale:72,color:0x7e94b4,op:0.07});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x04060a,seed:85,rim:0.14});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  addLights(g,{c:0x9db4d8,i:0.55,p:[0,100,-60]},{c:0x1a2436,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mirage.update(t,k); motes.update(t); mist.update(t,k);
    moonRef.material.opacity=k*(0.44+0.08*Math.sin(t*0.9));
    moonHalo.material.opacity=k*(0.20+0.05*Math.sin(t*0.7));
    boat.rotation.z=Math.sin(t*0.6)*0.02;
    rk.update(t,k);
  }};
}
function bGuxiangshui(){ // 四（末境·可点击）· 故乡水送 —— 点击江面，故乡水泛起粼粼波光送舟
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,gold:0};
  const ridge=makeRange({r:240,h:22,layers:2,peaks:3,seed:371,color:0x080b10,atmo:0x1e2c40,fogK:0.60,glowK:0.06,y:-20});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const water=makeWater({size:760,seg:100,amp:0.4,freq:0.1,speed:0.8,flow:[0.8,0.3],spec:1.6,
    deep:0x081624,shallow:0x143c58,skyc:0x244a6c,moonDir:[0,100,-170]});
  g.add(water.mesh);
  /* 行舟（沿波东去） */
  const boat=makeRowBoat({scale:1.25,rimC:0xa8c0e0});
  boat.position.set(0,0.25,-4); g.add(boat);
  /* 故乡水的暖色波光（点击后亮起，一路随舟） */
  const warm=makeGlow({n:150,box:[26,2.5,90],pos:[0,0.8,-26],color:0xe8c890,size:7,speed:0.06,rise:0,maxA:0});
  g.add(warm.points);
  const burst=makeBurst({n:90,color:0xffd890,pos:[0,3,-4]}); g.add(burst.points);
  const mist=makeMist({n:7,spread:[230,20,120],pos:[0,8,-48],scale:74,color:0x7e94b4,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x04060a,seed:87,rim:0.15});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:89,sway:0.9});
  reeds.g.position.set(13,-1.3,12); g.add(reeds.g);
  addLights(g,{c:0x9db4d8,i:0.55,p:[-40,100,-50]},{c:0x1a2436,i:0.6});
  const pl=new THREE.PointLight(0xe8c890,2.1,50); pl.position.set(0,5,-8); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.gold=Math.min(1,ctl.gold+dt/2.5);
      ridge.update(t,0); water.update(t); mist.update(t,k);
      rk.update(t,k); reeds.update(t,k); burst.update(t);
      warm.mat.uniforms.uMaxA.value=k*0.42*ctl.gold;
      warm.update(t);
      pl.intensity=k*2.1*(0.48+ctl.gold*0.47*(0.85+0.15*Math.sin(t*2.6)));
      boat.position.z=-4-ctl.gold*8;
      boat.position.y=0.25+Math.sin(t*0.8)*0.09;
      boat.rotation.z=Math.sin(t*0.7)*0.025;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.6,0.12);
        const fl=$('#flash'); fl.textContent='万里送行舟'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
