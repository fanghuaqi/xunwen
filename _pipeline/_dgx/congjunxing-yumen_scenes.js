/* ================= 从军行·其四 · 两境场景（大漠金戈：长云暗雪、百战金甲） =================
   美术立意：大漠金戈赛道——底色 #120d08、雾 #1a120a 系、accent=#c4824a（取自 queue，
   用于烽燧/城垣/人物边缘光/旗杆），禁艳金。四层色板递进：长云暗雪山（灰暗压抑）→ 孤城（沉赭剪影）
   → 黄沙（境②转亮的暖赭）→ 金甲（accent 亮的誓言）。前二句压抑暗色、后二句亮色誓言，
   读懂这条明暗递进线，就读懂了这首七绝的气骨。风沙横流（makeFlow 赭色）是贯穿两境的动态元素。
   标志性瞬间（境②）：金甲之光在黄沙中明灭 + 大漠孤城——黄沙百战、誓师不还；
   末境点击金甲（queue interact）：甲光千磨百战波次明灭 + 楼兰方向烽火次第点亮。
   情感曲线：苍茫压抑 → 慷慨誓师。 */

/* —— 长云：横压雪山的万里层云（自写着色器：横向漂移回绕 + 云隙明暗；uFade 显式交给 setFade）—— */
const CJX_CLOUD_VERT=`
uniform float uTime; uniform float uLen; uniform float uDrift;
varying vec2 vUv;
void main(){
  vUv=uv;
  vec3 p=position;
  p.x=mod(p.x+uTime*uDrift+uLen*0.5,uLen)-uLen*0.5;
  p.y+=sin(uv.x*12.0+uTime*0.22)*0.8;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const CJX_CLOUD_FRAG=`
uniform float uTime; uniform float uFade; uniform float uMaxA; uniform vec3 uColor;
varying vec2 vUv;
void main(){
  float across=smoothstep(0.0,0.42,vUv.y)*smoothstep(1.0,0.55,vUv.y);
  float streak=0.62+0.38*sin(vUv.x*46.0+uTime*0.35)*sin(vUv.x*17.0-uTime*0.21+1.7);
  float pulse=0.86+0.14*sin(uTime*0.3+vUv.x*7.0);
  gl_FragColor=vec4(uColor,uFade*uMaxA*across*streak*pulse);
}`;
function makeChangyun(o){
  o=o||{};
  const bands=o.bands===undefined?4:o.bands;
  const g=new THREE.Group(), parts=[];
  for(let i=0;i<bands;i++){
    const len=(o.len===undefined?360:o.len)*(1-0.05*i);
    const w=(o.w===undefined?16:o.w)*(1-0.10*i);
    const geo=new THREE.PlaneGeometry(len,w,64,1);
    const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
      uniforms:{uTime:{value:i*2.3},uLen:{value:len},uDrift:{value:(o.drift===undefined?1.6:o.drift)*(0.6+0.5*i)},
        uFade:{value:0},uMaxA:{value:(o.maxA===undefined?0.55:o.maxA)*(1-0.10*i)},
        uColor:{value:C(o.color===undefined?0x2e2924:o.color)}},
      vertexShader:CJX_CLOUD_VERT,fragmentShader:CJX_CLOUD_FRAG});
    const mesh=new THREE.Mesh(geo,m); mesh.frustumCulled=false; mesh.renderOrder=2;
    mesh.position.set((i-1)*6.0,(o.y===undefined?16:o.y)+i*6.5,(o.z===undefined?-70:o.z)+i*11);
    mesh.rotation.x=(o.rx===undefined?-0.06:o.rx); mesh.rotation.z=(i%2?0.015:-0.02);
    g.add(mesh); parts.push(m);
  }
  return {g,update(t){ for(let i=0;i<parts.length;i++)parts[i].uniforms.uTime.value=t+i*2.3; }};
}

/* —— 甲光：金甲上的百战之光（additive 点阵，uExt 控制明灭推进，uFade 显式交给 setFade）——
   千磨百战：点击后光痕按 aT 相位波次扫过甲面，如一磨一闪 */
const CJX_AREN_VERT=`
attribute float aSeed; attribute float aSize; attribute float aT;
uniform float uTime; uniform float uExt;
varying float vA;
void main(){
  vec3 p=position;
  p.y+=sin(uTime*0.9+aSeed*41.0)*0.10;
  p.x+=cos(uTime*0.7+aSeed*27.0)*0.08;
  float wave=pow(max(0.0,sin(uTime*1.5-aT*6.283+aSeed*0.7)),3.0);
  vA=uExt*(0.30+0.70*wave)*(0.65+0.35*sin(uTime*(3.0+5.0*aSeed)+aSeed*47.0));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.8+0.5*wave)*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const CJX_AREN_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.08,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeJiaguang(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?20501:o.seed);
  const n=o.n===undefined?70:o.n;
  const box=o.box===undefined?[3.0,3.8,2.0]:o.box, pos=o.pos===undefined?[0,1.6,0]:o.pos;
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n),T=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(R()-0.5)*box[0];
    P[i*3+1]=pos[1]+(R()-0.5)*box[1];
    P[i*3+2]=pos[2]+(R()-0.5)*box[2];
    S[i]=R(); T[i]=R(); Z[i]=2.6+R()*3.0;
  }
  const g=new THREE.BufferGeometry();
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  g.setAttribute('aT',new THREE.BufferAttribute(T,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uExt:{value:o.ext===undefined?0.001:o.ext},uColor:{value:C(o.color===undefined?0xe8b878:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.55:o.maxA}},
    vertexShader:CJX_AREN_VERT,fragmentShader:CJX_AREN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;},
    setExt(v){m.uniforms.uExt.value=Math.max(0.001,Math.min(1,v));}};
}

/* —— 烽燧：大漠烽火台（收分方台+顶台+垛口，合批 1 mesh）——「烽火明灭」的台，天际线的城垣 —— */
function makeFengsui(o){
  o=o||{};
  const h=o.h===undefined?9:o.h, w=o.w===undefined?3.2:o.w;
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(w*0.62,w,h,4); body.rotateY(Math.PI/4);
  body.translate(0,h/2,0); B.put(body,shadeColor(0x15100a,1.0));
  const cap=new THREE.BoxGeometry(w*1.15,0.5,w*1.15); cap.translate(0,h+0.2,0); B.put(cap,0x17110b);
  for(let i=-1;i<=1;i++){
    const mer=new THREE.BoxGeometry(0.5,0.7,0.5); mer.translate(i*w*0.34,h+0.75,0); B.put(mer,0x120d08);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc4824a,i:o.rim===undefined?0.14:o.rim,p:2.8})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 孤城：大漠孤城（四方城垣+角台+门楼，合批 1 mesh）——「孤城遥望」的城 —— */
function makeGucheng(o){
  o=o||{};
  const w=o.w===undefined?13:o.w, d=o.d===undefined?9:o.d, hh=o.h===undefined?3.4:o.h;
  const B=new GeoBag();
  const wallN=new THREE.BoxGeometry(w,hh,1.5); wallN.translate(0,hh/2,-d/2); B.put(wallN,0x16100a);
  const wallS=new THREE.BoxGeometry(w,hh,1.5); wallS.translate(0,hh/2,d/2); B.put(wallS,shadeColor(0x16100a,1.12));
  const wallW=new THREE.BoxGeometry(1.5,hh,d); wallW.translate(-w/2,hh/2,0); B.put(wallW,0x140e09);
  const wallE=new THREE.BoxGeometry(1.5,hh,d); wallE.translate(w/2,hh/2,0); B.put(wallE,0x140e09);
  [[-w/2,-d/2],[w/2,-d/2],[-w/2,d/2],[w/2,d/2]].forEach(function(p){
    const t=new THREE.BoxGeometry(2.4,hh+1.4,2.4); t.translate(p[0],(hh+1.4)/2,p[1]); B.put(t,0x17110b);
  });
  const gate=new THREE.BoxGeometry(3.6,2.6,3.4); gate.translate(0,1.3,d/2+0.6); B.put(gate,0x181209);
  const roof=new THREE.ConeGeometry(3.1,1.6,4); roof.rotateY(Math.PI/4); roof.translate(0,3.4,d/2+0.6); B.put(roof,0x1b140c);
  const doorway=new THREE.BoxGeometry(1.2,1.7,0.3); doorway.translate(0,0.85,d/2+2.25); B.put(doorway,0x060403);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc4824a,i:o.rim===undefined?0.14:o.rim,p:2.8})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 玉门关：关城剪影（城墙+双敌台+垛口+门洞，合批 1 mesh）——「遥望玉门关」的关 —— */
function makeYumen(o){
  o=o||{};
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(26,5.0,2.6); wall.translate(0,2.5,0); B.put(wall,0x120d08);
  [-10,10].forEach(function(x){
    const tw=new THREE.BoxGeometry(4.4,8.0,3.6); tw.translate(x,4.0,0); B.put(tw,0x131009);
  });
  for(let i=-5;i<=5;i++){
    const mer=new THREE.BoxGeometry(0.9,0.9,0.8); mer.translate(i*2.3,5.45,0); B.put(mer,0x100b07);
  }
  const doorway=new THREE.BoxGeometry(2.2,2.8,0.5); doorway.translate(0,1.4,1.4); B.put(doorway,0x050302);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x1d160e,emissive:0x030201}),{c:0xc4824a,i:o.rim===undefined?0.10:o.rim,p:2.8})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 战旗：旗杆+杆顶+暗赭战旗（旗面摆动，2 draw call）——誓师军旗猎猎 —— */
function makeZhanqi(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.08,0.11,h,6); pole.translate(0,h/2,0); B.put(pole,0x0b0806);
  const fin=new THREE.SphereGeometry(0.16,8,6); fin.translate(0,h+0.1,0); B.put(fin,0x6a5030);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc4824a,i:0.2,p:2.6})));
  const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.7,1.7,5,2),
    new THREE.MeshPhongMaterial({color:o.flagC===undefined?0x6a2818:o.flagC,side:THREE.DoubleSide,
      shininess:6,specular:0x3a2418,emissive:0x0d0803}));
  fl.position.set(1.35,h-1.15,0); g.add(fl);
  return {g,fl,ph,update(t){ fl.rotation.y=0.42*Math.sin(t*1.5+ph)+0.16*Math.sin(t*2.6+ph*1.7); }};
}

function bCoverCjx(){ // 封面 · 暮色大漠：长云压雪岭、孤城烽燧剪影、金甲将影独立风中
  const g=new THREE.Group();
  const ground=makeGround({r:130,c1:0x140d07,c2:0x241708});
  ground.mesh.position.set(0,-0.4,0); g.add(ground.mesh);
  /* 天际线：暗岭在前，雪岭远影（被长云压暗）在后 */
  const ridge=makeRange({r:300,h:16,layers:2,peaks:5,seed:20505,color:0x0b0805,atmo:0x332414,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-16); g.add(ridge.g);
  const snow=makeRange({r:240,h:30,layers:1,peaks:5,seed:20503,color:0x2e343c,atmo:0x6a7280,
    glow:0xdfe8f2,glowK:0.08,fogK:0.55,arc:Math.PI*0.7,a0:Math.PI*0.65,y:-14});
  g.add(snow.g);
  /* 长云横空（三带，暮色更沉） */
  const cloud=makeChangyun({bands:3,len:340,w:15,maxA:0.45,y:18,z:-60,color:0x2c2723});
  g.add(cloud.g);
  /* 孤城剪影 + 烽燧火光 */
  const city=makeGucheng({scale:1.1,rim:0.14}); city.position.set(-15,-0.4,-34); city.rotation.y=0.3; g.add(city);
  const beacon=makeFengsui({h:8,rim:0.16}); beacon.position.set(17,-0.4,-38); g.add(beacon);
  const flame=makeFlame({h:1.4,w:0.65,core:0xffd9a0,outer:0xd9802a,planes:2,embers:14,light:1.0,lightD:32});
  flame.g.position.set(17,8.9,-38); g.add(flame.g);
  /* 金甲将影独立 + 远处甲士一片 + 战旗 */
  const general=makeFigure({pose:'按剑',robe:0x6a4722,belt:0xc4824a,collar:0x8a6a3a,beard:true,
    scale:1.15,rim:0.62,rimC:0xc4824a});
  general.position.set(-3.5,-0.4,-12); general.rotation.y=Math.PI-0.32; g.add(general);
  const sentry=makeCrowd({n:10,rect:[-26,-32,32,12],color:0x181209,rimC:0xc4824a,rim:0.16,sMin:0.60,sMax:0.85,y:-0.4,seed:20507});
  g.add(sentry.mesh);
  const q1=makeZhanqi({h:6.6,ph:0.6}); q1.g.position.set(6,-0.4,-20); g.add(q1.g);
  const q2=makeZhanqi({h:5.8,ph:2.8}); q2.g.position.set(-10,-0.4,-24); g.add(q2.g);
  /* 风沙横流 + 低雾 + 微尘 */
  const flow=makeFlow({n:160,box:[230,13,90],pos:[0,6,-28],color:0x9a7c50,size:16,speed:5,maxA:0.13});
  g.add(flow.points);
  const mist=makeMist({n:9,spread:[260,22,120],pos:[0,9,-64],scale:82,color:0x6a5c48,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:34,box:[210,24,100],pos:[0,10,-40],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.13});
  g.add(motes.points);
  /* 前景框景：坡石 + 岩壁 */
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:12,d:6,color:0x0b0805,seed:20509,rim:0.10,rimC:0xc4824a});
  rk.g.position.set(14,-3.2,20); g.add(rk.g);
  const cliff=makeForeground({kind:'岩壁',n:2,r:3.4,w:13,d:6,color:0x0a0704,seed:20511,rim:0.10,rimC:0xc4824a});
  cliff.g.position.set(-15,-4.8,19); g.add(cliff.g);
  addLights(g,{c:0xc09058,i:0.34,p:[-50,55,-15]},{c:0x33281a,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ground.update(); ridge.update(t,0); snow.update(t,0); cloud.update(t);
    flame.update(t,k); flow.update(t); motes.update(t);
    mist.update(t,k); rk.update(t,k); cliff.update(t,k); general.update(t,k); sentry.update(t);
    q1.update(t); q2.update(t);
  }};
}
function bChangyunY(){ // 一 · 长云暗雪 —— 青海长云暗雪山，孤城遥望玉门关（苍茫压抑）
  const g=new THREE.Group();
  const ground=makeGround({r:300,c1:0x110b06,c2:0x1e1309,y:-1.4}); g.add(ground.mesh);
  /* 雪山（被云压暗的白脊：只留一线雪光，不许亮过云）+ 地平暗岭 */
  const snow=makeRange({r:260,h:30,layers:2,peaks:8,seed:20513,color:0x272d36,atmo:0x59616c,
    glow:0xdfe8f2,glowK:0.05,fogK:0.56,arc:Math.PI*0.7,a0:Math.PI*0.65,y:-12});
  g.add(snow.g);
  const ridge=makeRange({r:340,h:14,layers:2,peaks:5,seed:20515,color:0x0a0704,atmo:0x2a2013,fogK:0.60,glowK:0.04,y:-14});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  /* 青海长云：五带宽层云横压雪山（标志性系统：云底擦过雪脊，雪山因之发暗） */
  const cloud=makeChangyun({bands:5,len:360,w:22,maxA:0.70,y:11,z:-58,color:0x37322b,drift:2.0});
  g.add(cloud.g);
  /* 孤城（中景左）+ 城头守军人影 + 城下双旗 */
  const city=makeGucheng({scale:1.25,rim:0.16}); city.position.set(-13,-1.4,-42); city.rotation.y=0.28; g.add(city);
  const keeper=makeCrowd({n:12,rect:[-22,-50,20,8],color:0x181209,rimC:0xc4824a,rim:0.16,sMin:0.72,sMax:0.95,y:-1.4,seed:20517});
  g.add(keeper.mesh);
  const q1=makeZhanqi({h:6.2,ph:1.1,flagC:0x5a2014}); q1.g.position.set(-17,-1.4,-37); g.add(q1.g);
  const q2=makeZhanqi({h:5.4,ph:3.3,flagC:0x5a2014}); q2.g.position.set(-9,-1.4,-39); g.add(q2.g);
  /* 玉门关（远景右，遥望的方向）+ 关旁烽燧低燃 */
  const yumen=makeYumen({scale:1.5,rim:0.10}); yumen.position.set(14,-1.4,-96); yumen.rotation.y=-0.2; g.add(yumen);
  const beacon=makeFengsui({h:8.5,rim:0.14}); beacon.position.set(21,-1.4,-86); g.add(beacon);
  const bflame=makeFlame({h:1.2,w:0.55,core:0xffd9a0,outer:0xd9802a,planes:2,embers:12,spark:false,light:0.85,lightD:30});
  bflame.g.position.set(21,9.6,-86); g.add(bflame.g);
  /* 戍卒：城下遥望玉门关的背影（画面主角，压抑的「望」） */
  const soldier=makeFigure({pose:'独立',robe:0x231a10,belt:0x5a4226,hat:'幞头',scale:1.35,rim:0.58,rimC:0xc4824a});
  soldier.position.set(2.5,-1.4,-8); soldier.rotation.y=Math.PI-0.4; g.add(soldier);
  /* 风沙横流 + 低雾 + 微尘 */
  const flow=makeFlow({n:210,box:[260,16,100],pos:[0,7,-46],color:0x8a6f4c,size:18,speed:5.5,maxA:0.16});
  g.add(flow.points);
  const mist=makeMist({n:9,spread:[280,22,130],pos:[0,9,-72],scale:84,color:0x6a5c48,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:34,box:[220,26,110],pos:[0,10,-46],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.14});
  g.add(motes.points);
  /* 前景框景：坡石 + 岩壁 */
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:12,d:6,color:0x0b0805,seed:20519,rim:0.10,rimC:0xc4824a});
  rk.g.position.set(14,-3.4,15); g.add(rk.g);
  const cliff=makeForeground({kind:'岩壁',n:2,r:3.6,w:14,d:6,color:0x0a0704,seed:20521,rim:0.12,rimC:0xc4824a});
  cliff.g.position.set(-15,-5.2,17); g.add(cliff.g);
  addLights(g,{c:0xa88658,i:0.30,p:[-50,55,-20]},{c:0x30251a,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ground.update(); snow.update(t,0); ridge.update(t,0); cloud.update(t);
    bflame.update(t,k); flow.update(t); motes.update(t);
    mist.update(t,k); rk.update(t,k); cliff.update(t,k); soldier.update(t,k); keeper.update(t);
    q1.update(t); q2.update(t);
  }};
}
function bJinjia(){ // 二（末境·可点击）· 百战金甲 —— 黄沙百战穿金甲，不破楼兰终不还（慷慨誓师）
  const ctl={t:0,clicked:false,ext:0,last:-9};
  const g=new THREE.Group();
  const ground=makeGround({r:300,c1:0x1a1109,c2:0x2e1d0d,y:-1.4}); g.add(ground.mesh); // 黄沙转亮：誓言的底色
  const ridge=makeRange({r:340,h:18,layers:2,peaks:5,seed:20523,color:0x0c0806,atmo:0x3e2c16,fogK:0.58,glowK:0.06,glow:0xd8b088,y:-14});
  ridge.g.position.set(0,0,-40); g.add(ridge.g);
  /* 大漠孤城远影（与境①呼应：城还是那座城） */
  const city=makeGucheng({scale:1.1,rim:0.12}); city.position.set(-8,-1.4,-86); city.rotation.y=-0.15; g.add(city);
  /* 楼兰方向（右前方）烽燧一线三台：点击后烽火次第明灭传递 */
  const beacons=[];
  [[26,-50,1.0,0.10],[44,-74,0.8,0.42],[60,-96,0.65,0.74]].forEach(function(bp,i){
    const fs=makeFengsui({h:8.5*(0.72+0.28*bp[2]),rim:0.14,scale:bp[2]});
    fs.position.set(bp[0],-1.4,bp[1]); g.add(fs);
    const fl=makeFlame({h:(1.5-0.3*i),w:0.6-0.12*i,core:0xffd9a0,outer:0xd9802a,planes:2,
      embers:12,spark:false});
    fl.g.position.set(bp[0],9.7*bp[2]+0.9*(1-bp[2]),bp[1]); g.add(fl.g);
    const op0=0.60;
    const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
      transparent:true,opacity:op0,depthWrite:false,blending:THREE.AdditiveBlending}));
    glow.scale.set(16,12,1); glow.position.set(bp[0],10.2*bp[2]+1.5*(1-bp[2]),bp[1]); glow.renderOrder=4; g.add(glow);
    const bc={glow:glow,flame:fl,op0:op0,th0:bp[3],th1:bp[3]+0.24,ph:i*1.7,light:null,baseI:0};
    if(i===0){
      const lt=new THREE.PointLight(0xff8c42,3.0,44); lt.position.set(bp[0],10.4,bp[1]); g.add(lt);
      bc.light=lt; bc.baseI=3.0;
    }
    beacons.push(bc);
  });
  /* 金甲将军（誓师主将）+ 甲光点阵（点击对象） */
  const general=makeFigure({pose:'按剑',robe:0x7a5224,belt:0xc4824a,collar:0x8a6a3a,beard:true,
    hat:'幞头',scale:1.5,rim:0.85,rimC:0xc4824a});
  general.position.set(0.8,-1.4,-6.5); general.rotation.y=Math.PI-0.42; g.add(general);
  const jiaguang=makeJiaguang({n:70,pos:[0.8,1.6,-6.5],box:[3.0,3.8,2.0],ext:0.001,seed:20525});
  g.add(jiaguang.points);
  /* 百战军阵：甲士两列 + 战旗四面 */
  const army1=makeCrowd({n:36,rect:[-20,-16,40,11],color:0x1c140c,rimC:0xc4824a,rim:0.24,sMin:0.86,sMax:1.1,y:-1.4,seed:20527});
  g.add(army1.mesh);
  const army2=makeCrowd({n:14,rect:[-15,-5,30,6],color:0x18110b,rimC:0xc4824a,rim:0.22,sMin:0.84,sMax:1.06,y:-1.4,seed:20529});
  g.add(army2.mesh);
  const flags=[];
  [[-12,-14,7.2,0],[-5,-20,6.6,1.9],[9,-18,7.4,3.1],[16,-12,6.4,4.4]].forEach(function(fp){
    const f=makeZhanqi({h:fp[2],ph:fp[3]});
    f.g.position.set(fp[0],-1.4,fp[1]); g.add(f.g); flags.push(f);
  });
  /* 誓师火盆（夜誓的暖光池） */
  const bz=makeBrazier({r:0.85,fh:1.9,fw:0.95,light:1.0,lightD:34,embers:20});
  bz.g.position.set(-4.2,-1.4,-3.0); g.add(bz.g);
  /* 黄沙横流 + 暖尘 + 低雾 */
  const flow=makeFlow({n:230,box:[260,16,100],pos:[0,7,-42],color:0xa8824e,size:19,speed:6,maxA:0.18});
  g.add(flow.points);
  const motes=makeGlow({n:44,box:[220,24,110],pos:[0,9,-40],color:0xd8a868,size:6,speed:0.05,rise:0,maxA:0.18});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[270,20,120],pos:[0,8,-72],scale:80,color:0x7a674c,op:0.10});
  g.add(mist.g);
  /* 前景框景：坡石 + 岩壁 */
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:12,d:6,color:0x0b0805,seed:20531,rim:0.10,rimC:0xc4824a});
  rk.g.position.set(13,-2.8,14); g.add(rk.g);
  const cliff=makeForeground({kind:'岩壁',n:2,r:3.4,w:13,d:6,color:0x0a0704,seed:20533,rim:0.12,rimC:0xc4824a});
  cliff.g.position.set(-15,-5.0,16); g.add(cliff.g);
  addLights(g,{c:0xd0a060,i:0.50,p:[-55,50,-25]},{c:0x3a2c1c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.ext=Math.min(1,ctl.ext+dt/3.4);          // 甲光与烽火渐次推进
        if(t-ctl.last>6.5){ ctl.last=t; pluck(2,0,0.06); pluck(5,0.55,0.05); } // 誓师余韵
      }
      const e=ctl.ext*(2-ctl.ext);                    // easeOut
      jiaguang.setExt(e);                             // 甲光千磨百战，波次明灭
      for(let i=0;i<beacons.length;i++){              // 楼兰方向烽火次第明灭
        const bc=beacons[i];
        const f=Math.max(0,Math.min(1,(e-bc.th0)/(bc.th1-bc.th0)));
        bc.glow.material.opacity=k*bc.op0*(0.10+0.62*f)*(0.78+0.22*Math.sin(t*(5.5+i)+bc.ph*3.0));
        if(bc.light)bc.light.intensity=k*bc.baseI*(0.10+0.74*f)*(0.82+0.18*Math.sin(t*9.3+bc.ph));
      }
      ground.update(); ridge.update(t,0);
      jiaguang.update(t);
      for(let i=0;i<beacons.length;i++)beacons[i].flame.update(t,k);
      for(let i=0;i<flags.length;i++)flags[i].update(t);
      bz.update(t,k);
      flow.update(t); motes.update(t); mist.update(t,k);
      rk.update(t,k); cliff.update(t,k); general.update(t,k); army1.update(t); army2.update(t);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.2)return;        // 冷却门控
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      setAmbience(0.4);                               // 大漠风沙声起
      pluck(0,0.0,0.10); pluck(2,0.4,0.09); pluck(4,0.8,0.08); pluck(5,1.2,0.08); // 誓师和声
      const fl=$('#flash'); fl.textContent='不破楼兰终不还'; fl.classList.remove('go');
      void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
