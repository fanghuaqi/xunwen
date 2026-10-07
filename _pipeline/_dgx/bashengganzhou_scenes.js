/* ================= 八声甘州 · 四境场景（水墨夜思·柳永秋江羁旅：暮雨清秋、江水东流、登高望乡、倚栏凝愁） =================
   美术立意：全页禁金；冷银水墨 #98aec8 主调，暮雨/霜风/寒江皆冷；残照是全页唯一锈赭低饱和暖色（同《忆秦娥》先例）。
   标志性瞬间「残照当楼」（境①）：一束残照打在江楼之上，而天地俱冷——苏轼所谓「不减唐人高处」。
   末境点击倚阑干：倚栏人影凝愁显形，天际归舟虚影往复愈明；妆楼颙望（她眼中）与游子倚栏（我眼中）两面对写，
   境③（我望故乡·远镜）与境④（她望天际·反打）成镜头对切。 */

/* —— 暮雨/残红：自写「下落」小着色器（uFade 交给 setFade；slant 斜风，sway 横摆）—— */
const BSG_FALL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform float uSlant; uniform float uSway; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float h=mod(uTime*uSpeed*(0.65+aSeed*0.7)+aSeed*97.31, uBox.y);
  p.y-=h; p.x+=h*uSlant+sin(uTime*0.8+aSeed*31.0)*uSway;
  float f=h/uBox.y;
  vA=smoothstep(0.0,0.10,f)*smoothstep(1.0,0.70,f);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeRain(o){
  o=o||{};
  const n=o.n===undefined?240:o.n, box=o.box||[190,30,110], pos=o.pos||[0,16,-16];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?3.0:o.size)*(0.7+Math.random()*0.7);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?9.5:o.speed},
      uSlant:{value:o.slant===undefined?0.1:o.slant},uSway:{value:o.sway===undefined?0:o.sway},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x9fb2c8:o.color)},uFade:{value:0},
      uMaxA:{value:o.maxA===undefined?0.2:o.maxA}},
    vertexShader:BSG_FALL_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}
function makePetals(o){ // 红衰翠减：褪色花叶碎屑，缓落横摆
  o=o||{};
  const n=o.n===undefined?60:o.n, box=o.box||[80,16,46], pos=o.pos||[0,7,-12];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.4:o.size)*(0.7+Math.random()*0.7);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?1.1:o.speed},
      uSlant:{value:o.slant===undefined?0.05:o.slant},uSway:{value:o.sway===undefined?1.4:o.sway},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x6e3a3a:o.color)},uFade:{value:0},
      uMaxA:{value:o.maxA===undefined?0.28:o.maxA}},
    vertexShader:BSG_FALL_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}
/* turnFlow：makeFlow 把 pos 烘进顶点，整体 rotation.y 后平移补偿，使云心仍落在想要的世界坐标 */
function turnFlow(f,rotY,B,Cw){
  const s=Math.sin(rotY),co=Math.cos(rotY);
  f.points.rotation.y=rotY;
  f.points.position.set(Cw[0]-(B[0]*co+B[2]*s), Cw[1]-B[1], Cw[2]-(-B[0]*s+B[2]*co));
  return f;
}

/* —— 残照：一束锈赭余晖（水墨赛道唯一非冷色，禁金——残照取锈赭不取金）—— */
const BSG_ZHAO_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const BSG_ZHAO_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float along=smoothstep(0.0,0.18,vUv.x)*(1.0-smoothstep(0.72,1.0,vUv.x));
  float across=smoothstep(0.0,0.32,vUv.y)*smoothstep(1.0,0.68,vUv.y);
  float sway=0.88+0.12*sin(uTime*0.4+vUv.x*7.0);
  vec3 col=mix(vec3(0.50,0.31,0.22),vec3(0.24,0.18,0.21),clamp(vUv.y*1.2,0.0,1.0));
  gl_FragColor=vec4(col,uFade*uK*along*across*sway);
}`;

/* —— 江楼：双重大檐楼影 + 临水平台栏杆（合批 1 mesh）——「残照当楼」之楼 */
function makeJianglou(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const B=new GeoBag(), c1=0x0a0f16, c2=0x0e141f, c3=0x11171f;
  const base=new THREE.BoxGeometry(13,1.6,9); base.translate(0,0.8,0); B.put(base,c1);
  const lower=new THREE.BoxGeometry(7.6,6.0,6.0); lower.translate(0,1.6+3.0,0); B.put(lower,c2);
  const lowerRoof=new THREE.ConeGeometry(6.4,1.9,4); lowerRoof.rotateY(Math.PI/4);
  lowerRoof.scale(1.25,1,1.05); lowerRoof.translate(0,7.6+0.95,0); B.put(lowerRoof,c3);
  const upper=new THREE.BoxGeometry(5.2,3.8,4.4); upper.translate(0,9.5+1.9,0); B.put(upper,c2);
  const topRoof=new THREE.ConeGeometry(4.6,1.8,4); topRoof.rotateY(Math.PI/4);
  topRoof.scale(1.25,1,1.05); topRoof.translate(0,13.3+0.9,0); B.put(topRoof,c3);
  const deck=new THREE.BoxGeometry(4.6,0.35,3.2); deck.translate(3.2,2.0,0.5); B.put(deck,c1);
  [1,-1].forEach(function(s){
    for(let i=0;i<4;i++){
      const post=new THREE.BoxGeometry(0.12,0.9,0.12);
      post.translate(1.4+i*1.05,2.0+0.62,0.5+s*1.3); B.put(post,c3);
    }
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x98aec8,i:0.32,p:2.5})));
  g.scale.setScalar(sc);
  return g;
}

/* —— 妆楼：小体量楼影 + 上层露台围栏（佳人颙望处，合批 1 mesh）—— */
function makeZhuanglou(o){
  o=o||{};
  const B=new GeoBag(), c1=0x0d1219, c2=0x131a26, c3=0x1a2230;
  const base=new THREE.BoxGeometry(8,1.2,6); base.translate(0,0.6,0); B.put(base,c1);
  const body=new THREE.BoxGeometry(4.6,5.6,3.8); body.translate(0,1.2+2.8,0); B.put(body,c2);
  const waist=new THREE.BoxGeometry(5.2,0.5,4.3); waist.translate(0,6.9,0); B.put(waist,c3);
  const terrace=new THREE.BoxGeometry(4.2,0.3,3.2); terrace.translate(2.4,7.0,0.2); B.put(terrace,c1);
  [1,-1].forEach(function(s){
    for(let i=0;i<3;i++){
      const post=new THREE.BoxGeometry(0.11,0.85,0.11);
      post.translate(0.8+i*1.55,7.0+0.58,0.2+s*1.35); B.put(post,c3);
    }
  });
  for(let i=0;i<4;i++){
    const col=new THREE.CylinderGeometry(0.13,0.16,4.4,7);
    col.translate(0.9+(i%2)*3.0,7.15+2.2,0.2+(i<2?-1.2:1.4)); B.put(col,c3);
  }
  const roof=new THREE.ConeGeometry(3.4,1.5,4); roof.rotateY(Math.PI/4);
  roof.scale(1.2,1,1.0); roof.translate(2.4,11.7+0.75,0.2); B.put(roof,c2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x98aec8,i:0.30,p:2.5})));
  return g;
}

/* —— 栏干：中景一段凭栏（合批 1 mesh）——「倚阑干处」之阑干 */
function makeLangan(o){
  o=o||{};
  const B=new GeoBag(), w=o.w===undefined?9:o.w, h=o.h===undefined?1.2:o.h;
  const c=o.color===undefined?0x151b26:o.color;
  const top=new THREE.BoxGeometry(w,0.14,0.18); top.translate(0,h,0); B.put(top,shadeColor(c,1.6));
  const mid=new THREE.BoxGeometry(w,0.10,0.14); mid.translate(0,h*0.62,0); B.put(mid,shadeColor(c,1.2));
  const foot=new THREE.BoxGeometry(w,0.12,0.30); foot.translate(0,0.06,0); B.put(foot,c);
  const np=Math.max(2,Math.round(w/1.3));
  for(let i=0;i<=np;i++){
    const p=new THREE.BoxGeometry(0.12,h,0.12); p.translate(-w/2+w*i/np,h/2,0); B.put(p,c);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:o.rimC===undefined?0x98aec8:o.rimC,i:o.rim===undefined?0.3:o.rim,p:2.4})));
  return g;
}

/* —— 归舟虚影：远天水线的船影（透明材质，往复明灭）—— */
function makeYingzhou(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale, ph=o.phase===undefined?0:o.phase;
  const B=new GeoBag();
  const pts=[[0,0.02],[0.42,0.05],[0.72,0.26],[0.85,0.5],[0.9,0.58]].map(p=>new THREE.Vector2(p[0],p[1]));
  const hull=new THREE.LatheGeometry(pts,14); hull.scale(0.8,0.5,2.4); B.put(hull,0x1a222e);
  const cano=new THREE.CylinderGeometry(0.55,0.55,1.6,10,1,true,Math.PI/2,Math.PI);
  cano.rotateX(Math.PI/2); cano.scale(0.9,0.55,1); cano.translate(0,0.42,-0.3); B.put(cano,0x141b26);
  const m=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,specular:0x3a465c,
    emissive:0x060a12,transparent:true,opacity:0.30,depthWrite:false});
  const mesh=new THREE.Mesh(mergeGeos(B.list),m);
  mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(sc);
  return {g,mesh,m,phase:ph};
}

function bCoverBsg(){ // 封面 · 秋江暮雨（潇潇雨脚里，江楼一点伏笔）
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:88,amp:0.5,freq:0.09,speed:0.5,flow:[0,0.6],
    deep:0x0a121c,shallow:0x152638,skyc:0x1e2b3a,spec:0.55,y:-1.9});
  g.add(water.mesh);
  const ridge=makeRange({r:270,h:22,layers:2,peaks:4,seed:17101,color:0x0a0e15,atmo:0x212c3c,fogK:0.70,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,26); g.add(ridge.g);
  const lou=makeJianglou({scale:0.55}); lou.position.set(-32,-1.9,-72); lou.rotation.y=0.5; g.add(lou);
  const rain=makeRain({n:170,box:[210,32,120],pos:[0,16,-16],color:0x9fb2c8,size:3.0,speed:8.5,maxA:0.14,slant:0.07});
  g.add(rain.points);
  const motes=makeGlow({n:56,box:[220,36,130],pos:[0,10,-44],color:0xa8bcd8,size:7,speed:0.05,rise:0,maxA:0.3});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[250,30,150],pos:[0,10,-56],scale:80,color:0x8fa4c4,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:50,n:15,d:7,color:0x05080d,seed:17103,sway:0.9,tip:0x26323e});
  fg.g.position.set(0,-1.7,28); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:8,color:0x04060a,seed:17104,rim:0.13});
  rk.g.position.set(18,-1.4,20); g.add(rk.g);
  addLights(g,{c:0x93a8c2,i:0.38,p:[30,70,40]},{c:0x1e2835,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); rain.update(t); motes.update(t); mist.update(t,k);
    fg.update(t,k); rk.update(t,k);
  }};
}
function bMuyu(){ // 一（标志性瞬间）· 暮雨清秋 —— 潇潇暮雨、霜风凄紧、关河冷落：残照当楼而天地俱冷
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:84,amp:0.5,freq:0.09,speed:0.55,flow:[0,0.4],
    deep:0x0a121c,shallow:0x152638,skyc:0x1e2b3a,spec:0.35,y:-1.9});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(26,1.2,16),
    new THREE.MeshPhongMaterial({color:0x0d1219,shininess:5,specular:0x202a36}));
  bank.position.set(-14,-0.55,-24); g.add(bank);
  const soil=makeGround({r:11,c1:0x0c1016,c2:0x121924});
  soil.mesh.position.set(-14,0.02,-26); g.add(soil.mesh);
  const ridge=makeRange({r:290,h:20,layers:2,peaks:5,seed:17105,color:0x090d14,atmo:0x252b36,fogK:0.66,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,-10); g.add(ridge.g);
  /* 江楼（残照当楼之「楼」，立于矶岸）+ 一束锈赭残照打在楼上 + 楼头一点残照光 */
  const lou=makeJianglou({}); lou.position.set(-13,0,-26); lou.rotation.y=0.35; g.add(lou);
  const beamMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.95}},
    vertexShader:BSG_ZHAO_VERT,fragmentShader:BSG_ZHAO_FRAG});
  const beamGeo=new THREE.PlaneGeometry(90,22); beamGeo.rotateZ(-0.08);
  const beam=new THREE.Mesh(beamGeo,beamMat);
  beam.position.set(-23.5,11.5,-68); beam.rotation.y=1.32; beam.renderOrder=2; g.add(beam);
  const sunGhost=new THREE.Mesh(new THREE.CircleGeometry(5.5,28),
    new THREE.MeshBasicMaterial({color:0x66402f,transparent:true,opacity:0.45,depthWrite:false,
      fog:false,blending:THREE.AdditiveBlending}));
  sunGhost.position.set(-34,8,-110); sunGhost.renderOrder=2; g.add(sunGhost);
  const zhao=new THREE.PointLight(0x7a4638,0.5,36); zhao.position.set(-11,13,-24); g.add(zhao);
  /* 潇潇暮雨（斜急）+ 霜风横扫（侧向雾流） */
  const rain=makeRain({n:240,box:[190,30,110],pos:[0,16,-16],color:0x9fb2c8,size:3.0,speed:10,maxA:0.22,slant:0.12});
  g.add(rain.points);
  const wind=turnFlow(makeFlow({n:260,box:[220,16,80],pos:[0,10,-48],color:0x8fa0b8,size:26,speed:7.5,maxA:0.20}),
    1.1,[0,10,-48],[0,10,-48]);
  g.add(wind.points);
  const mist=makeMist({n:8,spread:[220,20,100],pos:[0,8,-52],scale:74,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:13,d:6,color:0x05080d,seed:17107,sway:1.0,tip:0x26323e});
  fg.g.position.set(-10,-0.2,12); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:13,d:6,color:0x04060a,seed:17108,rim:0.13});
  rk.g.position.set(18,-0.7,8); g.add(rk.g);
  addLights(g,{c:0x8ea6c2,i:0.30,p:[-40,70,-20]},{c:0x1c2734,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); rain.update(t); wind.update(t); mist.update(t,k);
    fg.update(t,k); rk.update(t,k);
    beamMat.uniforms.uTime.value=t;
    beamMat.uniforms.uK.value=0.78+0.17*Math.sin(t*0.5);
    sunGhost.material.opacity=k*(0.32+0.10*Math.sin(t*0.5+1.1));
    zhao.intensity=k*(0.32+0.18*(0.5+0.5*Math.sin(t*0.9)));
  }};
}
function bDongliu(){ // 二 · 江水东流 —— 红衰翠减、苒苒物华休：褪色残红缓落，长江无语东流
  const g=new THREE.Group();
  const water=makeWater({size:900,seg:96,amp:0.75,freq:0.07,speed:0.75,flow:[0,1.3],
    deep:0x0a1220,shallow:0x14283c,skyc:0x20303e,spec:0.14,moonDir:[0.7,0.3,-0.6],y:-2.0});
  g.add(water.mesh);
  const ridge=makeRange({r:430,h:12,layers:2,peaks:3,seed:17109,color:0x090d14,atmo:0x2b3542,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-36); g.add(ridge.g);
  /* 无语东流：两层侧向江雾流（整体转向东去）+ 贴水横雾 */
  const flow1=turnFlow(makeFlow({n:420,box:[380,7,90],pos:[0,-1.1,-50],color:0x849ab2,size:22,speed:6,maxA:0.32}),
    1.25,[0,-1.1,-50],[0,-1.1,-50]);
  g.add(flow1.points);
  const flow2=turnFlow(makeFlow({n:260,box:[300,5,70],pos:[0,0.8,-70],color:0x7288a2,size:24,speed:4.5,maxA:0.24}),
    1.25,[0,0.8,-70],[0,0.8,-70]);
  g.add(flow2.points);
  /* 红衰翠减：褪红与黯翠的残红碎屑，缓缓坠落 */
  const red=makePetals({n:66,box:[84,16,46],pos:[-6,7,-12],color:0x6e3a3a,size:2.5,speed:1.1,maxA:0.34});
  g.add(red.points);
  const green=makePetals({n:44,box:[70,15,40],pos:[10,8,-9],color:0x3e4c44,size:2.3,speed:0.9,maxA:0.24});
  g.add(green.points);
  const mist=makeMist({n:8,spread:[300,18,90],pos:[0,5,-60],scale:80,color:0x7f95b0,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:46,n:13,d:6,color:0x05080d,seed:17111,sway:0.85,tip:0x26323e});
  fg.g.position.set(-10,-1.8,15); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x04060a,seed:17112,rim:0.12});
  rk.g.position.set(20,-2.0,10); g.add(rk.g);
  addLights(g,{c:0x89a0ba,i:0.28,p:[-30,60,-30]},{c:0x1e2937,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); flow1.update(t); flow2.update(t);
    red.update(t); green.update(t); mist.update(t,k); fg.update(t,k); rk.update(t,k);
  }};
}
function bDenggao(){ // 三 · 登高望乡（我眼中·远镜）—— 不忍登高临远：危台凭栏、背影远望，故乡渺邈
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.4,freq:0.08,speed:0.5,flow:[0,0.5],
    deep:0x0a121c,shallow:0x152638,skyc:0x1f2c3c,spec:0.35,moonDir:[0,0.3,-1],y:-2.0});
  g.add(water.mesh);
  /* 危台（登高处）：石台 + 台面 + 临江一侧栏干 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(30,3.2,22),
    new THREE.MeshPhongMaterial({color:0x10151d,shininess:6,specular:0x242e3a}));
  tai.position.set(0,1.6,-6); g.add(tai);
  const top=makeGround({r:13,c1:0x0c0f16,c2:0x121823});
  top.mesh.position.set(0,3.24,-6); g.add(top.mesh);
  const lg=makeLangan({w:18,h:1.25}); lg.position.set(0,3.24,-16.2); g.add(lg);
  /* 词人背影（不忍而登临）：凭栏远望，望向 -Z 深处 */
  const poet=makeFigure({pose:'独立',robe:0x2a3140,belt:0x3d4859,hat:'幞头',beard:true,scale:1.3,rim:0.6,rimC:0x98aec8});
  poet.position.set(1.4,3.24,-14.6); poet.rotation.y=Math.PI-0.25; g.add(poet);
  const ridge=makeRange({r:320,h:26,layers:3,peaks:5,seed:17113,color:0x090d14,atmo:0x232e3d,fogK:0.62,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-20); g.add(ridge.g);
  /* 望故乡渺邈：对岸极远处一簇村影 + 渡头人影（几乎化进雾里） */
  const B=new GeoBag();
  for(let i=0;i<6;i++){
    const b=new THREE.BoxGeometry(0.9+(i%3)*0.5,0.8+((i*7)%3)*0.4,0.8);
    b.translate(-10+i*1.7,(0.8+((i*7)%3)*0.4)/2,(i%2)*1.1-0.5); B.put(b,0x161c28);
  }
  const cun=new THREE.Mesh(mergeGeos(B.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,specular:0x20293a,
      transparent:true,opacity:0.85}));
  cun.position.set(-10,-1.5,-108); g.add(cun);
  const crowd=makeCrowd({n:3,rect:[12,-80,10,4],seed:17114,color:0x10151d,rimC:0x8fa4c4,
    rim:0.12,sMin:0.4,sMax:0.55,y:-1.5});
  g.add(crowd.mesh);
  /* 归思难收：一缕向远处去的思雾 */
  const si=turnFlow(makeFlow({n:200,box:[120,12,60],pos:[0,8,-40],color:0x8fa0b8,size:22,speed:4,maxA:0.16}),
    Math.PI,[0,8,-40],[0,8,-40]);
  g.add(si.points);
  const mist=makeMist({n:7,spread:[240,24,80],pos:[0,12,-78],scale:84,color:0x7e8ea8,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:7,color:0x04060a,seed:17115,rim:0.12});
  rk.g.position.set(-12,2.6,9); g.add(rk.g);
  const tree=makeForeground({kind:'树枝',n:2,w:13,d:5,color:0x04060a,seed:17116,sway:1.2,rim:0.15});
  tree.g.position.set(13,3.2,8); g.add(tree.g);
  addLights(g,{c:0x9db0c8,i:0.34,p:[-30,80,-40]},{c:0x202b39,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); si.update(t); mist.update(t,k);
    poet.update(t,k); crowd.update(t); rk.update(t,k); tree.update(t,k);
  }};
}
function bNingchou(){ // 四（末境·可点击）· 倚栏凝愁 —— 妆楼颙望（她眼中）；点击倚阑干：人影凝愁显形，归舟虚影往复（我眼中）
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.6,freq:0.08,speed:0.6,flow:[0,0.8],
    deep:0x0a121c,shallow:0x152838,skyc:0x1f2d3c,spec:0.22,moonDir:[0.8,0.25,-0.55],y:-1.9});
  g.add(water.mesh);
  const ridge=makeRange({r:300,h:15,layers:2,peaks:4,seed:17117,color:0x090d14,atmo:0x2b3542,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-14); g.add(ridge.g);
  /* 妆楼（她眼中）：水中矶上小楼，楼上露台，佳人颙望天际 */
  const isle=new THREE.Mesh(new THREE.BoxGeometry(12,1.4,9),
    new THREE.MeshPhongMaterial({color:0x0d1219,shininess:5,specular:0x202a36}));
  isle.position.set(-17,-0.7,-30); g.add(isle);
  const isoil=makeGround({r:5.5,c1:0x0c1016,c2:0x121924});
  isoil.mesh.position.set(-17,0.02,-30); g.add(isoil.mesh);
  const zlou=makeZhuanglou({}); zlou.position.set(-17,0,-30); zlou.rotation.y=-0.3; g.add(zlou);
  const lady=makeFigure({pose:'指月',robe:0x463a44,belt:0x5a4c58,skin:0xd3b89f,collar:0x8a93a8,
    hat:'发髻',scale:1.05,rim:0.62,rimC:0xaebfd4,noProp:true});
  lady.position.set(-14.8,7.0,-29.1); lady.rotation.y=0.55; g.add(lady);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.26,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(3.6,3.6,1); win.position.set(-15.6,5.4,-27.8); win.renderOrder=2; g.add(win);
  /* 倚阑干处（我眼中·点击显形）：凭栏一段 + 游子人影 */
  const lg=makeLangan({w:9,h:1.2}); lg.position.set(5.5,0,-10); lg.rotation.y=-0.15; g.add(lg);
  const poet=makeFigure({pose:'独立',robe:0x252c3a,belt:0x37414f,hat:'幞头',beard:true,scale:1.24,rim:0.7,rimC:0x98aec8});
  poet.position.set(5.2,0,-9.3); poet.rotation.y=-0.12; poet.rotation.x=0.03;
  poet.traverse(function(o){ const m=o.material; if(m){ m.transparent=true; m.opacity=0.92; m.depthWrite=false; o.renderOrder=2; } });
  g.add(poet);
  /* 天际识归舟：远天水线的归舟虚影（往复明灭，点击后愈明且左右往复） */
  const boats=[[-2,-70,0.4],[16,-84,1.9],[34,-96,3.6]].map(function(b){
    const yb=makeYingzhou({scale:1.35,phase:b[2]});
    yb.g.position.set(b[0],-1.7,b[1]); yb.g.rotation.y=0.12; g.add(yb.g); return yb;
  });
  const motes=makeGlow({n:52,box:[180,24,90],pos:[0,9,-30],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,20,110],pos:[0,8,-52],scale:78,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:42,n:12,d:6,color:0x05080d,seed:17119,sway:0.8,tip:0x26323e});
  fg.g.position.set(0,-1.6,14); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:7,color:0x04060a,seed:17120,rim:0.12});
  rk.g.position.set(-14,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x8fa6c0,i:0.30,p:[-30,70,-20]},{c:0x1e2937,i:0.62});
  let poetMat=null;
  poet.traverse(function(o){ if(!poetMat&&o.isMesh)poetMat=o.material; });
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/2.6);
      water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k);
      lady.update(t,k); fg.update(t,k); rk.update(t,k);
      win.material.opacity=k*(0.20+0.06*Math.sin(t*0.7));
      /* 归舟虚影往复：明灭 + 点击后左右往复 */
      for(let i=0;i<boats.length;i++){
        const b=boats[i], pu=0.6+0.4*Math.sin(t*0.7+b.phase);
        b.m.opacity=k*(0.14+0.16*ctl.ext)*pu;
        b.g.position.x=(i===0?-2:(i===1?16:34))+(3.0*Math.sin(t*0.22+b.phase))*ctl.ext;
        b.mesh.rotation.z=0.02*Math.sin(t*0.5+b.phase);
      }
      /* 倚栏人影凝愁（点击显形） */
      if(poetMat)poetMat.opacity=k*(0.08+0.84*ctl.ext);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(1,0.1,0.12); pluck(3,0.5,0.11); pluck(5,1.0,0.12);
        const fl=$('#flash'); fl.textContent='正恁凝愁'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
