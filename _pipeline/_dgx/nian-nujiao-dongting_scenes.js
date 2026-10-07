/* ================= 念奴娇·过洞庭 · 四境场景（水墨夜思：琼田一叶、表里澄澈、孤光冰雪、扣舷独啸） =================
   美术立意：全页禁金；冷银水墨 #b8c8dc 主调。「更无一点风色」的静、「素月分辉，明河共影」的澄澈
   是全页基调——湖面如镜映月是本页最重要的水面表现（amp 压到 0.1 以下、spec 拉高、月路入水）。
   标志性瞬间「琼田一叶」（境①）：三万顷玉鉴琼田与我一叶扁舟的大小对照。
   末境点击尽挹西江：北斗为杯舀江斟月（七星亮起、江水入斗），万象为宾（远岸林木人影显形）。 */

/* —— 扁舟：船体（Lathe 剖面）+ 船篷 + 桨，合批 1 mesh；自带随波轻晃 —— */
function makePianzhou(o){
  o=o||{};
  const B=new GeoBag();
  const pts=[[0,0.02],[0.30,0.04],[0.46,0.16],[0.52,0.34],[0.50,0.46]].map(p=>new THREE.Vector2(p[0],p[1]));
  const hull=new THREE.LatheGeometry(pts,16); hull.scale(0.62,1,2.6); B.put(hull,0x1a222e);
  const gun=new THREE.TorusGeometry(0.50,0.035,5,20); gun.rotateX(Math.PI/2);
  gun.scale(0.62,2.6,1); gun.translate(0,0.45,0); B.put(gun,shadeColor(0x1a222e,1.85));
  if(o.canopy!==false){
    const can=new THREE.CylinderGeometry(0.40,0.44,1.45,10,1,true,0,Math.PI);
    can.rotateZ(Math.PI/2); can.scale(1,1,0.78); can.translate(0,0.42,0.80); B.put(can,0x141b26);
  }
  const oar=new THREE.BoxGeometry(0.05,0.04,2.2); oar.rotateX(0.16);
  oar.translate(0.34,0.34,-0.35); B.put(oar,0x10161f);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a465c,emissive:0x05070c}),{c:o.rimC===undefined?0x8fa4c4:o.rimC,i:o.rim===undefined?0.26:o.rim,p:2.5})));
  g.userData.ph=o.ph===undefined?0:o.ph;
  let baseY=null;
  g.update=function(t,k){
    if(baseY===null)baseY=g.position.y;
    const ph=g.userData.ph;
    g.position.y=baseY+0.075*Math.sin(t*0.62+ph);
    g.rotation.z=0.026*Math.sin(t*0.5+ph+1.2);
    g.rotation.x=0.013*Math.sin(t*0.44+ph);
  };
  g.userData.update=g.update;
  return g;
}

/* —— 明河（银河）：天上一带 + 水中一影（水墨夜思 · 明河共影；uFade 交给 setFade）—— */
const NNDY_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const NNDY_HE_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float along=smoothstep(0.0,0.22,vUv.x)*(1.0-smoothstep(0.78,1.0,vUv.x));
  float across=pow(smoothstep(0.0,0.5,vUv.y)*(1.0-smoothstep(0.5,1.0,vUv.y)),1.25);
  float drift=0.85+0.15*sin(uTime*0.22+vUv.x*5.0+uK*7.0);
  float grain=0.80+0.20*sin(vUv.x*130.0)*sin(vUv.y*27.0+uK*3.0);
  vec3 col=mix(vec3(0.60,0.71,0.88),vec3(0.28,0.38,0.56),vUv.y);
  gl_FragColor=vec4(col,uFade*uK*along*across*drift*grain);
}`;
function makeMilkyway(){
  const g=new THREE.Group();
  const skyMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.50}},
    vertexShader:NNDY_VERT,fragmentShader:NNDY_HE_FRAG});
  const sky=new THREE.Mesh(new THREE.PlaneGeometry(340,58),skyMat);
  sky.position.set(14,62,-150); sky.rotation.z=0.42; sky.rotation.x=-0.22; sky.renderOrder=-7; g.add(sky);
  const wMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.30}},
    vertexShader:NNDY_VERT,fragmentShader:NNDY_HE_FRAG});
  const wgeo=new THREE.PlaneGeometry(150,95); wgeo.rotateX(-Math.PI/2);
  const refl=new THREE.Mesh(wgeo,wMat);
  refl.position.set(13,-1.82,-66); refl.renderOrder=2; g.add(refl);
  return {g,update(t){ skyMat.uniforms.uTime.value=t; wMat.uniforms.uTime.value=t; }};
}

/* —— 月路：贴水面的一道素月光带（素月分辉；自定义窄带着色器，远亮近淡，uFade 交给 setFade）—— */
const NNDY_MOON_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float across=pow(smoothstep(0.0,0.5,vUv.x)*(1.0-smoothstep(0.5,1.0,vUv.x)),1.4);
  float along=smoothstep(0.04,0.62,vUv.y);
  float shimmer=0.80+0.20*sin(uTime*0.5+vUv.y*22.0);
  vec3 col=vec3(0.78,0.86,0.98);
  gl_FragColor=vec4(col,uFade*uK*along*across*shimmer);
}`;
function makeMoonPath(o){
  o=o||{};
  const geo=new THREE.PlaneGeometry(o.w===undefined?26:o.w,o.len===undefined?85:o.len);
  geo.rotateX(-Math.PI/2);
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.maxA===undefined?0.16:o.maxA}},
    vertexShader:NNDY_VERT,fragmentShader:NNDY_MOON_FRAG});
  const mesh=new THREE.Mesh(geo,mat);
  mesh.position.set(o.x===undefined?8:o.x,-1.86,o.z===undefined?-56:o.z);
  mesh.renderOrder=2;
  return {mesh,update(t){ mat.uniforms.uTime.value=t; }};
}

/* —— 北斗七星：勺形七星 + 连线（末境点击「细斟北斗」时亮起）—— */
const BEIDOU=[[-5.2,0,0],[-3.6,-1.7,0.7],[-0.7,-2.1,1.2],[-0.2,-0.2,1.0],[1.9,0.7,0.5],[4.2,1.6,0.1],[6.3,3.0,-0.7]];
const BEIDOU_SEG=[[0,1],[1,2],[2,3],[3,0],[3,4],[4,5],[5,6]];
function makeDipper(){
  const g=new THREE.Group();
  const stars=[];
  BEIDOU.forEach(function(p,i){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
      transparent:true,opacity:0.94,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    const sz=3.4+0.6*(i%3);
    s.scale.set(sz,sz,1);
    s.position.set(p[0],p[1],p[2]); s.renderOrder=-7; g.add(s); stars.push(s);
  });
  const lgeo=new THREE.BufferGeometry();
  const lp=[];
  BEIDOU_SEG.forEach(function(sg){ lp.push.apply(lp,BEIDOU[sg[0]]); lp.push.apply(lp,BEIDOU[sg[1]]); });
  lgeo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(lp),3));
  const line=new THREE.LineSegments(lgeo,new THREE.LineBasicMaterial({color:0xa8c0e0,
    transparent:true,opacity:0.42,depthWrite:false,fog:false}));
  line.renderOrder=-7; g.add(line);
  g.position.set(-13,24,-52); g.scale.setScalar(2.3); g.rotation.set(-0.25,0,0.12);
  return {g,stars,line,update(t,k,ext){
    for(let i=0;i<stars.length;i++){
      stars[i].material.opacity=k*(0.30+0.62*ext)*(0.92+0.08*Math.sin(t*1.1+i*1.7));
    }
    line.material.opacity=k*0.42*ext;
  }};
}

function bCover(){ // 封面 · 镜湖无声（近中秋的洞庭：风色全无，月悬琼田，远处一叶伏笔）
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:88,amp:0.18,freq:0.09,speed:0.18,flow:[0.03,0.02],
    deep:0x0a1420,shallow:0x16283c,skyc:0x20304a,spec:1.2,moonDir:[16,21,-170],y:-1.9});
  g.add(water.mesh);
  const ridge=makeRange({r:300,h:9,layers:2,peaks:6,seed:20001,color:0x080c13,atmo:0x1f2b3d,fogK:0.66,glowK:0.05,y:-10});
  ridge.g.position.set(0,0,30); g.add(ridge.g);
  const boat=makePianzhou({ph:2.0}); boat.scale.setScalar(1.1); boat.position.set(-7,-1.86,-36); g.add(boat);
  const mp=makeMoonPath({x:8.5,z:-58,w:18,len:66,maxA:0.14}); g.add(mp.mesh);
  const motes=makeGlow({n:52,box:[200,34,120],pos:[0,10,-40],color:0xa8bcd8,size:7,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,26,130],pos:[0,8,-54],scale:80,color:0x8fa4c4,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:13,d:6,color:0x04060a,seed:20002,sway:0.45,tip:0x26323e});
  fg.g.position.set(9,-1.8,26); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:7,color:0x04060a,seed:20003,rim:0.13});
  rk.g.position.set(-17,-1.6,20); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.44,p:[26,90,-40]},{c:0x19222f,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k);
    boat.update(t,k); mp.update(t); fg.update(t,k); rk.update(t,k);
  }};
}

function bQiongtian(){ // 一（标志性瞬间·词眼）· 琼田一叶 —— 三万顷玉鉴琼田，着我扁舟一叶：大小对照
  const g=new THREE.Group();
  const water=makeWater({size:940,seg:96,amp:0.20,freq:0.085,speed:0.16,flow:[0.03,0.015],
    deep:0x0a1420,shallow:0x17293e,skyc:0x22334c,spec:1.3,moonDir:[16,21,-170],y:-1.9});
  g.add(water.mesh);
  /* 万顷之阔：极低极远的环湖岸线（洞庭平远，无高山） */
  const ridge=makeRange({r:430,h:9,layers:2,peaks:6,seed:20005,color:0x080c13,atmo:0x223046,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-60); g.add(ridge.g);
  /* 一叶之微：扁舟客坐饮船头 */
  const boat=makePianzhou({ph:0.6,rim:0.4,rimC:0xb8c8dc}); boat.scale.setScalar(1.6); boat.position.set(0,-1.86,-17); g.add(boat);
  const guest=makeFigure({pose:'坐饮',robe:0x242c3c,belt:0x51617a,skin:0xcbb9a2,collar:0xaebdd2,
    hat:'发髻',rimC:0xb8c8dc,rim:0.5,noProp:true,scale:0.62});
  guest.position.set(0,0.40,-0.55); guest.rotation.y=2.6; boat.add(guest);
  /* 玉鉴：镜面月路（素月分辉的先声） */
  const mp=makeMoonPath({x:10,z:-52,w:24,len:80,maxA:0.16}); g.add(mp.mesh);
  const motes=makeGlow({n:44,box:[220,30,140],pos:[0,9,-46],color:0xa8bcd8,size:6,speed:0.04,rise:0,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[280,20,120],pos:[0,7,-64],scale:84,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:40,n:12,d:6,color:0x04060a,seed:20006,sway:0.4,tip:0x26323e});
  fg.g.position.set(12,-1.7,22); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:13,d:6,color:0x04060a,seed:20007,rim:0.12});
  rk.g.position.set(-18,-1.5,17); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[26,95,-40]},{c:0x1a2232,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k);
    boat.update(t,k); guest.update(t,k); mp.update(t); fg.update(t,k); rk.update(t,k);
  }};
}

function bChengche(){ // 二 · 表里澄澈 —— 素月分辉，明河共影：天上一带河汉，水中一带倒影，表里俱澈
  const g=new THREE.Group();
  const water=makeWater({size:800,seg:92,amp:0.08,freq:0.05,speed:0.15,flow:[0.02,0.015],
    deep:0x0a1522,shallow:0x182c44,skyc:0x243852,spec:2.0,moonDir:[16,21,-170],y:-1.9});
  g.add(water.mesh);
  const ridge=makeRange({r:380,h:8,layers:2,peaks:5,seed:20008,color:0x080c13,atmo:0x243044,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-50); g.add(ridge.g);
  /* 明河共影：天上银河 + 水中河影（本境专属着色器对） */
  const he=makeMilkyway(); g.add(he.g);
  /* 素月分辉：镜面月路直抵船前 */
  const mp=makeMoonPath({x:6,z:-40,w:18,len:66,maxA:0.20}); g.add(mp.mesh);
  /* 舟中人悠然心会：指月 */
  const boat=makePianzhou({ph:3.4,rim:0.4,rimC:0xb8c8dc}); boat.scale.setScalar(1.65); boat.position.set(1.2,-1.86,-11); g.add(boat);
  const poet=makeFigure({pose:'指月',robe:0x252d3e,belt:0x51617a,skin:0xcbb9a2,collar:0xaebdd2,
    hat:'幞头',beard:true,rimC:0xb8c8dc,rim:0.55,noProp:true,scale:0.62});
  poet.position.set(0,0.40,-0.55); poet.rotation.y=2.9; boat.add(poet);
  const motes=makeGlow({n:40,box:[180,26,110],pos:[0,9,-38],color:0xbcc9dc,size:6,speed:0.04,rise:0,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,18,100],pos:[0,6,-56],scale:80,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:38,n:11,d:6,color:0x04060a,seed:20009,sway:0.35,tip:0x26323e});
  fg.g.position.set(-12,-1.7,17); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x04060a,seed:20010,rim:0.12});
  rk.g.position.set(15,-1.5,14); g.add(rk.g);
  addLights(g,{c:0x93a8c8,i:0.52,p:[26,100,-40]},{c:0x1b2434,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); he.update(t); motes.update(t); mist.update(t,k);
    boat.update(t,k); poet.update(t,k); mp.update(t); fg.update(t,k); rk.update(t,k);
  }};
}

function bGubing(){ // 三 · 孤光冰雪 —— 岭海经年，孤光自照，肝胆皆冰雪：短发萧骚襟袖冷，稳泛沧浪空阔
  const g=new THREE.Group();
  const water=makeWater({size:760,seg:90,amp:0.22,freq:0.07,speed:0.35,flow:[0.06,0.08],
    deep:0x0a1320,shallow:0x15263a,skyc:0x1e2e44,spec:1.1,moonDir:[16,21,-170],y:-1.9});
  g.add(water.mesh);
  /* 岭海：远岭连绵（回望谪居之地，全页唯一的高远山） */
  const ridge=makeRange({r:360,h:30,layers:3,peaks:6,seed:20011,color:0x090d15,atmo:0x27334a,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-40); g.add(ridge.g);
  /* 孤光：月晕收窄，薄雾遮月，只余一线清辉 */
  const mistMoon=makeMist({n:5,spread:[130,34,60],pos:[14,26,-90],scale:60,color:0x7e8ea8,op:0.12});
  g.add(mistMoon.g);
  /* 稳泛沧浪：船与人皆稳，襟袖略冷 */
  const boat=makePianzhou({ph:1.4,rim:0.5,rimC:0xdfe9f6}); boat.scale.setScalar(1.7); boat.position.set(0.5,-1.86,-10); g.add(boat);
  const poet=makeFigure({pose:'独立',robe:0x232b3b,belt:0x4d5d76,skin:0xc7b69f,collar:0xa8b7cc,
    hat:'幞头',beard:true,rimC:0xdfe9f6,rim:0.72,noProp:true,scale:0.70});
  poet.position.set(0,0.40,-0.35); poet.rotation.y=2.75; boat.add(poet);
  /* 肝胆冰雪：霜晶缓落 + 一缕袖冷之风 */
  const frost=makeGlow({n:64,box:[70,16,40],pos:[0,8,-12],color:0xdfe9f6,size:4,speed:0.10,rise:-0.45,add:false,maxA:0.30});
  g.add(frost.points);
  const wind=makeFlow({n:150,box:[130,12,60],pos:[0,7,-30],color:0x8fa0b8,size:22,speed:3.6,maxA:0.13});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[200,16,90],pos:[0,6,-50],scale:76,color:0x7e8ea8,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:15,d:7,color:0x04060a,seed:20012,rim:0.13});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  const fg=makeForeground({kind:'芦苇',w:34,n:10,d:6,color:0x04060a,seed:20013,sway:0.8,tip:0x26323e});
  fg.g.position.set(11,-1.6,15); g.add(fg.g);
  addLights(g,{c:0x9db0c8,i:0.34,p:[26,90,-40]},{c:0x1c2531,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); frost.update(t); wind.update(t);
    mist.update(t,k); mistMoon.update(t,k);
    boat.update(t,k); poet.update(t,k); rk.update(t,k); fg.update(t,k);
  }};
}

function bKouxian(){ // 四（末境·可点击）· 扣舷独啸 —— 点击尽挹西江：北斗为杯舀江斟月，万象为宾
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const water=makeWater({size:820,seg:92,amp:0.12,freq:0.055,speed:0.2,flow:[0.03,0.02],
    deep:0x0a1522,shallow:0x172b42,skyc:0x233650,spec:1.1,moonDir:[16,21,-170],y:-1.9});
  g.add(water.mesh);
  const ridge=makeRange({r:400,h:10,layers:2,peaks:5,seed:20014,color:0x080c13,atmo:0x243048,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-52); g.add(ridge.g);
  /* 扣舷独啸之人：举杯邀万象 */
  const boat=makePianzhou({ph:0.2,rim:0.45,rimC:0xb8c8dc}); boat.scale.setScalar(1.7); boat.position.set(0,-1.86,-14); g.add(boat);
  const poet=makeFigure({pose:'举杯',robe:0x262e40,belt:0x51617a,skin:0xcbb9a2,collar:0xaebdd2,
    hat:'幞头',beard:true,rimC:0xb8c8dc,rim:0.6,noProp:true,scale:0.70});
  poet.position.set(0,0.40,-0.4); poet.rotation.y=3.3; boat.add(poet);
  /* 北斗（点击亮起）+ 挹江入斗的水流 + 江面承接处的雾 */
  const dip=makeDipper(); g.add(dip.g);
  /* 挹江入斗：一柱江水自船畔斜升入斗（点击转旺）+ 江面承接处的雾 */
  const stream=makeGlow({n:110,box:[5,26,7],pos:[-10,10,-50],color:0xcfe0f4,size:5,speed:2.4,rise:1,add:true,maxA:0.03});
  stream.points.rotation.z=0.43;
  g.add(stream.points);
  const splash=makeMist({n:4,spread:[10,3,10],pos:[-5,-1.4,-48],scale:18,color:0xbfd2ea,op:0.06});
  g.add(splash.g);
  /* 万象为宾：远岸林木剪影（根入水线，点击显形）+ 远处人影 4 */
  const B=new GeoBag(), R=seedRnd(20015);
  for(let i=0;i<12;i++){
    const x=(i<6?-1:1)*(16+R()*54), z=-64-R()*30, h=2.2+R()*3.4;
    const tr=new THREE.ConeGeometry(0.9+R()*0.8,h,6); tr.translate(x,-1.9+h*0.5,z); B.put(tr,0x0d1420);
    const crown=new THREE.SphereGeometry(1.0+R()*0.8,6,5); crown.scale(1.5,0.75,1.5);
    crown.translate(x,-1.9+h*0.82,z); B.put(crown,0x101826);
  }
  const shore=new THREE.Mesh(mergeGeos(B.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,specular:0x243044,
      emissive:0x05070c,transparent:true,opacity:0.88}));
  shore.material.opacity=0.88; g.add(shore);
  const crowd=makeCrowd({n:4,rect:[-30,-86,26,5],seed:20016,color:0x10161f,rimC:0xb8c8dc,
    rim:0.14,sMin:0.32,sMax:0.44,y:-1.9});
  g.add(crowd.mesh);
  const motes=makeGlow({n:46,box:[200,28,110],pos:[0,9,-36],color:0xbcc9dc,size:6,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,20,110],pos:[0,7,-54],scale:80,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:40,n:12,d:6,color:0x04060a,seed:20017,sway:0.5,tip:0x26323e});
  fg.g.position.set(-11,-1.7,18); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:13,d:6,color:0x04060a,seed:20018,rim:0.12});
  rk.g.position.set(14,-1.5,14); g.add(rk.g);
  /* 点击后的月华点光（ intensity 每帧乘 fadeK），照向北斗舀江处 */
  const pl=new THREE.PointLight(0xcfe0f4,1.25,90); pl.position.set(-13,22,-48); g.add(pl);
  addLights(g,{c:0x93a8c8,i:0.5,p:[26,95,-40]},{c:0x1a2434,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/2.8);
      water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k); splash.update(t,k);
      boat.update(t,k); poet.update(t,k); fg.update(t,k); rk.update(t,k); crowd.update(t);
      dip.update(t,k,ctl.ext);
      stream.mat.uniforms.uMaxA.value=0.03+0.40*ctl.ext;
      shore.material.opacity=k*(0.38+0.50*ctl.ext);
      pl.intensity=k*1.25*(0.12+0.88*ctl.ext)*(0.88+0.12*Math.sin(t*1.6));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.05,0.13); pluck(4,0.45,0.11); pluck(5,0.95,0.12);
        const fl=$('#flash'); fl.textContent='万象为宾客'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
