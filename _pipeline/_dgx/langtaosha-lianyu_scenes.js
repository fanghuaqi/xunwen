/* ================= 浪淘沙令·帘外雨潺潺 · 三境场景（烟雨江南·李煜绝笔：梦里暖、醒后寒） =================
   美术立意：境①冷雨囚夜、境③冷江凭栏皆黛蓝湿雾；唯境②梦境用全页唯一的低饱和烛橙微暖。
   标志性瞬间「天上人间」：一水之隔的天上/人间两界（末境点击凭栏点亮）。 */

/* —— 细雨/落花：自写「下落」小着色器（makeGlow 的粒子只悬浮或上浮，落向不对）——
   uFade 仍交给 setFade 统一淡入淡出；slant 给一点斜风。 */
const LTR_RAIN_VERT=`attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform float uSlant; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float h=mod(uTime*uSpeed*(0.65+aSeed*0.7)+aSeed*97.31, uBox.y);
  p.y-=h; p.x+=h*uSlant;
  float f=h/uBox.y;
  vA=smoothstep(0.0,0.10,f)*smoothstep(1.0,0.70,f);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeRain(o){
  o=o||{};
  const n=o.n===undefined?300:o.n, box=o.box||[160,30,90], pos=o.pos||[0,16,-20];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?3.6:o.size)*(0.7+Math.random()*0.7);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?10:o.speed},
      uSlant:{value:o.slant===undefined?0:o.slant},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x9fb2c8:o.color)},uFade:{value:0},
      uMaxA:{value:o.maxA===undefined?0.4:o.maxA}},
    vertexShader:LTR_RAIN_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* —— 末境专属着色器：天上界宫阙 / 水上光路 / 凭栏延伸（uExt 由点击驱动，uFade 走 setFade）—— */
const LTR_REALM_VERT=`varying vec3 vN; varying vec2 vUv;
void main(){ vN=normal; vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const LTR_REALM_FRAG=`uniform vec3 uC; uniform float uFade; uniform float uExt;
varying vec3 vN; varying vec2 vUv;
void main(){
  float d=0.62+0.38*max(0.0,vN.y);
  gl_FragColor=vec4(uC*d, uFade*(0.12+0.55*uExt));
}`;
const LTR_GLEAM_FRAG=`uniform vec3 uC; uniform float uFade; uniform float uExt;
varying vec2 vUv;
void main(){
  float a=uFade*uExt*0.50*(0.25+0.75*vUv.y)*smoothstep(0.0,0.30,vUv.x)*smoothstep(1.0,0.70,vUv.x);
  gl_FragColor=vec4(uC,a);
}`;
const LTR_EXT_FRAG=`uniform vec3 uC; uniform float uFade; uniform float uExt;
varying vec3 vN;
void main(){
  float d=0.55+0.45*max(0.0,vN.y);
  gl_FragColor=vec4(uC*d, uFade*(0.18+0.72*uExt));
}`;

/* —— 烛台：梦境的低饱和烛橙点光（全页唯一暖源，非金）—— */
function makeCandle(o){
  o=o||{};
  const h=o.h===undefined?1.15:o.h;
  const B=new GeoBag();
  const stem=new THREE.CylinderGeometry(0.05,0.075,0.95,6); stem.translate(0,0.45,0); B.put(stem,0x35322c);
  const hold=new THREE.CylinderGeometry(0.21,0.27,0.09,8); hold.translate(0,0.05,0); B.put(hold,0x35322c);
  const bd=new THREE.CylinderGeometry(0.085,0.10,h,8); bd.translate(0,0.95+h/2,0); B.put(bd,0xd8c8ac);
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:18,
    specular:0x6a5c48,emissive:0x0a0806})));
  const fl=makeFlame({h:0.68,w:0.22,planes:2,embers:12,spark:false,
    light:o.light===undefined?1.5:o.light,lightD:o.lightD===undefined?36:o.lightD,
    lightC:0xd88a50,wide:0.3,core:0xffe2a8,outer:0xd07f42});
  fl.g.position.y=0.95+h+0.28; g.add(fl.g);
  return {g,update:function(t,k){ fl.update(t,k===undefined?1:k); }};
}

/* —— 罗衾：台榻上摊开的冷蓝丝被（衾 qīn）—— */
function makeBedQuilt(){
  const B=new GeoBag();
  const bed=new THREE.BoxGeometry(5.2,0.5,3.2); bed.translate(0,0.25,0); B.put(bed,0x241e18);
  const quilt=new THREE.SphereGeometry(2.5,14,10); quilt.scale(1.0,0.34,0.62); quilt.translate(-0.5,0.55,0);
  B.put(quilt,0x3a4656);
  const fold=new THREE.TorusGeometry(2.2,0.16,6,18,Math.PI); fold.rotateX(Math.PI/2); fold.scale(1,0.5,0.66);
  fold.translate(-0.5,0.58,0); B.put(fold,0x425062);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4a5c,emissive:0x060a10}),{c:0x8fb3c9,i:0.30,p:2.4})));
  return g;
}

/* —— 标志性瞬间「天上人间」：雾上天光里的一角宫阙剪影（点击点亮）—— */
function makeSkyRealm(){
  const B=new GeoBag();
  const pl1=new THREE.CylinderGeometry(0.5,0.6,7,6); pl1.translate(-4.5,3.9,0); B.put(pl1,0x9ab4d0);
  const pl2=new THREE.CylinderGeometry(0.5,0.6,7,6); pl2.translate(4.5,3.9,0); B.put(pl2,0x9ab4d0);
  const base=new THREE.BoxGeometry(11,0.8,3); base.translate(0,0.8,0); B.put(base,0x8fa6c2);
  const eave=new THREE.BoxGeometry(12.5,0.5,3.6); eave.translate(0,7.8,0); B.put(eave,0xa8c0da);
  const roof=new THREE.ConeGeometry(8.2,2.6,4); roof.rotateY(Math.PI/4); roof.translate(0,9.3,0); B.put(roof,0xb2c8e0);
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    uniforms:{uC:{value:C(0x9ab4d0)},uFade:{value:1},uExt:{value:0}},
    vertexShader:LTR_REALM_VERT,fragmentShader:LTR_REALM_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat); mesh.frustumCulled=false; mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mat};
}
/* —— 水上光路：天上界在江面的一带微光（一水之隔）—— */
function makeGleam(){
  const geo=new THREE.PlaneGeometry(26,84); geo.rotateX(-Math.PI/2);
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uC:{value:C(0x8fb4d8)},uFade:{value:1},uExt:{value:0}},
    vertexShader:LTR_REALM_VERT,fragmentShader:LTR_GLEAM_FRAG});
  const mesh=new THREE.Mesh(geo,mat); mesh.frustumCulled=false; mesh.renderOrder=2;
  mesh.position.set(0,-0.85,-46);
  const g=new THREE.Group(); g.add(mesh);
  return {g,mat};
}
/* —— 点击后的凭栏延伸：双栏栈桥自台沿伸向无限江山雾影（透视收敛，尽头即天上界）—— */
function makeRailingExt(){
  const B=new GeoBag(), L=64;
  [1,-1].forEach(function(s){
    const top=new THREE.BoxGeometry(0.16,0.14,L); top.translate(s*2.2,2.95,-L/2); B.put(top,0x324258);
    const mid=new THREE.BoxGeometry(0.12,0.10,L); mid.translate(s*2.2,1.7,-L/2); B.put(mid,0x2c3c50);
    for(let i=0;i<=10;i++){
      const p=new THREE.BoxGeometry(0.12,3.0,0.12); p.translate(s*2.2,1.45,-i*L/10); B.put(p,0x28384a);
    }
  });
  for(let i=0;i<=8;i++){
    const sl=new THREE.BoxGeometry(4.4,0.07,0.6); sl.translate(0,0.02,-i*L/8); B.put(sl,0x1f2c3c);
  }
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uC:{value:C(0x62809e)},uFade:{value:1},uExt:{value:0}},
    vertexShader:LTR_REALM_VERT,fragmentShader:LTR_EXT_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat); mesh.frustumCulled=false; mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(0,0,-2.8); g.scale.z=0.02;
  return {g,mat};
}

function bCoverLangtaosha(){ // 封面 · 烟雨宫苑（冷黛蓝湿雾，一场夜雨拉开全词）
  const g=new THREE.Group();
  const grd=makeGround({r:26,c1:0x0f131a,c2:0x1a222c});
  grd.mesh.position.y=-1.6; g.add(grd.mesh);
  const water=makeWater({size:320,seg:72,amp:0.3,freq:0.1,speed:0.55,flow:[0,0.4],
    deep:0x0a121c,shallow:0x16283a,skyc:0x1e2c3c,spec:0.8,y:-1.75});
  g.add(water.mesh);
  const ridge=makeRange({r:180,h:26,layers:2,peaks:4,seed:1591,color:0x0c1017,atmo:0x36445a,fogK:0.72,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,30); g.add(ridge.g);
  /* 烟雨中的一角宫苑剪影 */
  const palL=makePillar({h:9,r:0.5,color:0x1b2431,top:false}); palL.g.position.set(-16,0,-14); g.add(palL.g);
  const palR=makePillar({h:9,r:0.5,color:0x1b2431,top:false}); palR.g.position.set(-5,0,-18); g.add(palR.g);
  const cur=makeCurtain({w:14,h:7,color:0x222e3c,dark:0x0d1420,folds:5});
  cur.g.position.set(-10.5,3.5,-17); g.add(cur.g);
  /* 细雨 + 水面涨雾 + 微光 */
  const rain=makeRain({n:320,box:[200,32,120],pos:[0,17,-18],color:0x9fb2c8,size:3.6,speed:10,maxA:0.36,slant:0.08});
  g.add(rain.points);
  const mist=makeMist({n:11,spread:[240,34,150],pos:[0,10,-46],scale:80,color:0x8fa4c0,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x0a0d13,seed:1593,rim:0.14});
  fg.g.position.set(0,-1.8,30); g.add(fg.g);
  const motes=makeGlow({n:50,box:[200,30,120],pos:[0,10,-24],color:0xa8bcd4,size:7,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  addLights(g,{c:0x9aaec8,i:0.36,p:[-30,70,40]},{c:0x232e3c,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); rain.update(t); mist.update(t,k);
    fg.update(t,k); motes.update(t);
  }};
}
function bYuhan(){ // 一 · 帘外雨寒 —— 冷雨敲帘、春意阑珊、罗衾不耐五更寒（全词之冷自此始）
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0d1016,c2:0x151b23});
  grd.mesh.position.y=-1.6; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:30,layers:2,peaks:4,seed:1597,color:0x0a0e15,atmo:0x36445a,fogK:0.66,glowK:0.06});
  g.add(ridge.g);
  /* 囚居小楼：台基 + 双柱 + 半透帘幕（帘外雨潺潺） */
  const plat=new THREE.Mesh(new THREE.BoxGeometry(20,0.8,9),
    new THREE.MeshPhongMaterial({color:0x141a24,shininess:8,specular:0x2c3a4a}));
  plat.position.set(0,-0.4,-8); g.add(plat);
  const pilL=makePillar({h:8.5,r:0.42,color:0x1a2230,top:false}); pilL.g.position.set(-7,0,-8.5); g.add(pilL.g);
  const pilR=makePillar({h:8.5,r:0.42,color:0x1a2230,top:false}); pilR.g.position.set(7,0,-8.5); g.add(pilR.g);
  const cur=makeCurtain({w:13.5,h:6.6,color:0x2a3a4e,dark:0x0d1420,folds:6});
  cur.g.position.set(0,3.3,-7.6); g.add(cur.g);
  /* 罗衾（帘内冷蓝丝被 + 一点冷光） */
  const bed=makeBedQuilt(); bed.position.set(-2.6,0.4,-9.2); g.add(bed);
  const lampLight=new THREE.PointLight(0x7a94b4,0.85,26); lampLight.position.set(-2.6,3,-8.6); g.add(lampLight);
  /* 主角：李煜立于帘侧听雨（幞头旧袍，孤冷） */
  const poet=makeFigure({pose:'独立',robe:0x2c3442,belt:0x4a5060,hat:'幞头',scale:1.3,rim:0.6,rimC:0x8fb3c9});
  poet.position.set(3.6,0.4,-5.6); poet.rotation.y=-0.5; g.add(poet);
  /* 春意阑珊：无主落花（淡藕荷缓落） */
  const petals=makeRain({n:64,box:[80,20,44],pos:[4,12,-8],color:0xa88890,size:5.4,speed:2.0,maxA:0.30,slant:0.03});
  g.add(petals.points);
  /* 潺潺细雨（斜风细雨，自写下落着色器） */
  const rain=makeRain({n:460,box:[190,34,110],pos:[0,18,-16],color:0x9fb2c8,size:3.0,speed:10.5,maxA:0.40,slant:0.10});
  g.add(rain.points);
  const mist=makeMist({n:8,spread:[220,20,110],pos:[0,8,-38],scale:72,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  /* 远墙边几个模糊的人影（看守的剪影） */
  const guards=makeCrowd({n:3,rect:[-22,-25,14,6],seed:1599,color:0x0e131a,rimC:0x5a6a7a,rim:0.12,sMin:0.75,sMax:0.95});
  g.add(guards.mesh);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:20,d:8,color:0x080b10,seed:1601,rim:0.14});
  fgRock.g.position.set(13,-1.6,12); g.add(fgRock.g);
  const fgTwig=makeForeground({kind:'树枝',w:20,n:7,d:4,color:0x0a0d12,seed:1603,sway:0.7});
  fgTwig.g.position.set(-13,-1.4,10); g.add(fgTwig.g);
  addLights(g,{c:0x8ea6c2,i:0.34,p:[-40,80,-30]},{c:0x1c2734,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rain.update(t); petals.update(t);
    mist.update(t,k); poet.update(t,k); guards.update(t);
    fgRock.update(t,k); fgTwig.update(t,k);
    lampLight.intensity=0.85*k*(0.9+0.1*Math.sin(t*1.3));
  }};
}
function bTanhuan(){ // 二 · 一晌贪欢（梦境 · 全页唯一微暖）—— 梦里不知身是客：旧宫一隅，烛影酒温
  const g=new THREE.Group();
  const grd=makeGround({r:100,c1:0x14110d,c2:0x1e1812});
  grd.mesh.position.y=-1.6; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:30,layers:2,peaks:4,seed:1607,color:0x0c0f15,atmo:0x36445a,fogK:0.68,glowK:0.05});
  g.add(ridge.g);
  /* 旧宫帷帐（梦里宫苑的一角） */
  const cur=makeCurtain({w:18,h:9,color:0x3c2a28,dark:0x140c0a,folds:7});
  cur.g.position.set(0,4.5,-12); g.add(cur.g);
  /* 长案与梦里的宴席（陶器玉杯，禁金） */
  const table=makeTable({w:9,d:3,h:1.5,wood:0x3a2a18}); table.g.position.set(1.5,0,-7.5); g.add(table.g);
  const dish1=makeDish({r:0.9,n:5}); dish1.g.position.set(0.2,1.58,-7.3); g.add(dish1.g);
  const dish2=makeDish({r:0.75,n:4}); dish2.g.position.set(1.1,1.58,-8.1); g.add(dish2.g);
  const zun=makeVessel({type:'樽',mat:'陶',scale:0.52}); zun.g.position.set(3.1,1.58,-7.8); g.add(zun.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.5}); hu.g.position.set(3.9,1.58,-7.0); g.add(hu.g);
  const cup1=makeVessel({type:'杯',mat:'玉',scale:0.42,liquid:true}); cup1.g.position.set(2.0,1.58,-6.9); g.add(cup1.g);
  const cup2=makeVessel({type:'杯',mat:'玉',scale:0.42}); cup2.g.position.set(4.6,1.58,-7.6); g.add(cup2.g);
  /* 烛台：低饱和烛橙点光 —— 梦境唯一的暖源 */
  const candle=makeCandle({h:1.15,scale:1.1,light:1.6,lightD:40}); candle.g.position.set(5.0,1.58,-7.0); g.add(candle.g);
  /* 梦里的李煜：举杯向虚（不知身是客） */
  const poet=makeFigure({pose:'举杯',robe:0x4c4034,belt:0x6a5438,hat:'幞头',scale:1.28,rim:0.6,rimC:0xd8a06a,noProp:true});
  poet.position.set(-1.6,0,-4.8); poet.rotation.y=0.35; g.add(poet);
  /* 梦境光尘（烛橙微尘） */
  const dust=makeGlow({n:90,box:[60,14,40],pos:[0,7,-7],color:0xd8a06a,size:6,speed:0.04,rise:0,maxA:0.32});
  g.add(dust.points);
  /* 醒意的冷雾从四缘渗进来（梦里暖、醒后寒） */
  const coldMist=makeMist({n:7,spread:[200,16,100],pos:[0,6,-30],scale:68,color:0x8fa4c0,op:0.10});
  g.add(coldMist.g);
  const fg=makeForeground({kind:'坡石',n:2,r:3.6,w:16,d:7,color:0x0a0c10,seed:1609,rim:0.12});
  fg.g.position.set(12,-1.5,11); g.add(fg.g);
  addLights(g,{c:0xc89a64,i:0.40,p:[30,70,10]},{c:0x2c2a2c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); poet.update(t,k); coldMist.update(t,k); fg.update(t,k);
    dust.update(t); candle.update(t,k);
    zun.update(t,k); cup1.update(t,k);
  }};
}
function bTianshang(){ // 三（末境·可点击）· 天上人间 —— 凭栏处流水落花；点击凭栏，栏杆伸向无限江山，天上界浮现
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const grd=makeGround({r:26,c1:0x0e1117,c2:0x161d26});
  grd.mesh.position.y=-0.55; g.add(grd.mesh);
  /* 高台 + 凭栏 */
  const terrace=new THREE.Mesh(new THREE.BoxGeometry(26,1.0,11),
    new THREE.MeshPhongMaterial({color:0x12161e,shininess:6,specular:0x2a3444}));
  terrace.position.set(0,-0.5,2); g.add(terrace);
  const rail=makeForeground({kind:'栏杆',w:26,h:3.1,color:0x1c2634,rim:0.3});
  rail.g.position.set(0,0,1.6); g.add(rail.g);
  /* 主角：李煜凭栏背影（face 由 rotation.y 定朝向） */
  const poet=makeFigure({pose:'独立',robe:0x2c3442,belt:0x4a5060,hat:'幞头',scale:1.3,rim:0.6,rimC:0x8fb3c9});
  poet.position.set(0.5,0,-0.4); poet.rotation.y=Math.PI; g.add(poet);
  /* 流水（冷江东去）+ 落花 + 水上雾流 */
  const water=makeWater({size:680,seg:90,amp:0.85,freq:0.07,speed:0.8,flow:[0,1.2],
    deep:0x0a121d,shallow:0x142c44,skyc:0x22303e,spec:1.0,y:-1.9});
  g.add(water.mesh);
  const petals=makeRain({n:70,box:[90,18,50],pos:[0,10,-26],color:0xa88890,size:5,speed:1.8,maxA:0.26,slant:0.04});
  g.add(petals.points);
  const flow=makeFlow({n:420,box:[150,7,70],pos:[0,-0.9,-48],color:0x7a92ac,size:22,speed:6,maxA:0.38});
  g.add(flow.points);
  /* 无限江山雾影（三层渐远渐淡） */
  const ridge=makeRange({r:260,h:38,layers:3,peaks:6,seed:1613,color:0x0a0e15,atmo:0x36445a,fogK:0.62,glowK:0.06});
  ridge.g.position.set(0,0,-20); g.add(ridge.g);
  /* 标志性瞬间：一水之隔的天上/人间两界（点击点亮） */
  const realm=makeSkyRealm(); realm.g.position.set(0,15.5,-90); g.add(realm.g);
  const realmGlow=makeGlow({n:80,box:[84,26,26],pos:[0,17,-90],color:0xa8c4e0,size:14,speed:0.05,rise:0,maxA:0});
  g.add(realmGlow.points);
  const gleam=makeGleam(); g.add(gleam.g);
  /* 点击后凭栏延伸向无限江山 */
  const ext=makeRailingExt(); g.add(ext.g);
  const mist=makeMist({n:8,spread:[240,20,120],pos:[0,8,-50],scale:76,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  const fgRock=makeForeground({kind:'坡石',n:2,r:4.0,w:16,d:8,color:0x080b10,seed:1615,rim:0.14});
  fgRock.g.position.set(14,-1.2,14); g.add(fgRock.g);
  const fgTwig=makeForeground({kind:'树枝',w:18,n:6,d:4,color:0x0a0d12,seed:1617,sway:0.8});
  fgTwig.g.position.set(-14,-1.0,12); g.add(fgTwig.g);
  addLights(g,{c:0x93a8c2,i:0.38,p:[-40,80,-30]},{c:0x202c3a,i:0.62});
  const burst=makeBurst({n:70,color:0xbcd4ee,pos:[0.5,5,-1]}); g.add(burst.points);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/2.6);
      water.update(t); ridge.update(t,0); petals.update(t); flow.update(t);
      mist.update(t,k); poet.update(t,k); burst.update(t);
      fgRock.update(t,k); fgTwig.update(t,k);
      realm.mat.uniforms.uExt.value=ctl.ext;
      gleam.mat.uniforms.uExt.value=ctl.ext;
      ext.mat.uniforms.uExt.value=ctl.ext;
      ext.g.scale.z=0.02+0.98*ctl.ext;
      realmGlow.mat.uniforms.uMaxA.value=k*(0.10+0.42*ctl.ext)*(0.85+0.15*Math.sin(t*0.8));
      realmGlow.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.5,0.12); pluck(5,0.9,0.14); bell();
        const fl=$('#flash'); fl.textContent='天上人间'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
