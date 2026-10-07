/* ================= 春晓 · 四境场景（青绿春晓：晨光渐亮 + 花瓣粉白缓落 + 枝头啼鸟 + 雨霁落英）
   「造型工坊」原语：makePetals（花瓣）/ makeBlossomTree（花树）/ makeCottage（夜窗茅屋）
   / makeBirdSil（枝头鸟）/ makeFlock（远鸟群）/ makeRain（夜雨） ================= */

/* 花瓣：粉白小片缓落 + 摆动翻飞（Points 自定义着色器；浅绿底上粉白可读） */
const CX_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB;
uniform float uSway; uniform float uWind;
varying float vA; varying float vRot; varying float vMix;
void main(){
  vec3 p=position;
  float sp=uFall*(0.75+aSeed*0.5);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.2+aSeed*40.0)*uSway+(uH-y)*uWind;
  p.z+=cos(uTime*0.9+aSeed*27.0)*uSway*0.7;
  vA=smoothstep(0.0,2.2,y)*(0.78+0.22*sin(uTime*1.7+aSeed*31.0));
  vRot=uTime*(0.6+aSeed)+aSeed*17.0;
  vMix=fract(aSeed*7.31);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const CX_PETAL_FRAG=`
uniform vec3 uC1; uniform vec3 uC2; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vRot; varying float vMix;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float cs=cos(vRot),sn=sin(vRot);
  q=mat2(cs,-sn,sn,cs)*q;
  q.x*=1.85;                                   // 拉长成瓣形
  float a=smoothstep(0.5,0.30,length(q))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(mix(uC1,uC2,vMix),a);
}`;
function makePetals(o){
  const d=Object.assign({n:120,box:[90,32,60],pos:[0,16,-16],fall:0.024,sway:2.0,wind:0.06,
    size:4.4,maxA:0.5,c1:0xe8a4c6,c2:0xfbf5eb},o);
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(d.n*3),S=new Float32Array(d.n),Z=new Float32Array(d.n);
  for(let i=0;i<d.n;i++){
    P[i*3]=d.pos[0]+(Math.random()-0.5)*d.box[0];
    P[i*3+1]=d.pos[1]+Math.random()*d.box[1];
    P[i*3+2]=d.pos[2]+(Math.random()-0.5)*d.box[2];
    S[i]=Math.random(); Z[i]=d.size*(0.6+Math.random()*0.8);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uFall:{value:d.fall},uH:{value:d.box[1]},uB:{value:d.pos[1]},
      uSway:{value:d.sway},uWind:{value:d.wind},
      uC1:{value:C(d.c1)},uC2:{value:C(d.c2)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:CX_PETAL_VERT,fragmentShader:CX_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* 花树：主干收分 + 发散枝条 + 粉白花团（合批 1 mesh；枝枝有花，免生秃枝） */
function makeBlossomTree(o){
  o=o||{};
  const h=o.h===undefined?11:o.h, R=seedRnd(o.seed===undefined?11:o.seed);
  const trunkC=o.trunk===undefined?0x241c14:o.trunk;
  const pink=o.pink===undefined?0xdba8c6:o.pink;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*1.2-0.6,h*0.96,0],h*0.052,h*0.015,8),trunkC);
  const nb=o.branches===undefined?9:o.branches, tips=[];
  for(let i=0;i<nb;i++){
    const a=(i/nb)*Math.PI*2+R()*0.9, el=0.45+R()*0.7, len=h*(0.24+R()*0.34);
    const dx=Math.cos(a)*Math.cos(el),dy=Math.sin(el),dz=Math.sin(a)*Math.cos(el);
    const y0=h*(0.46+R()*0.42);
    const p1=[dx*len*0.22,y0+dy*len*0.26,dz*len*0.22], p2=[dx*len,y0+dy*len,dz*len];
    B.put(limbGeo(p1,p2,h*0.020,h*0.008,6),trunkC);
    tips.push([p2[0],p2[1]+len*0.14,p2[2]]);
  }
  const nc=o.clusters===undefined?(nb+2):o.clusters;
  for(let i=0;i<nc;i++){
    const t=tips[i%tips.length]||[0,h*0.9,0];
    const r=h*(0.15+R()*0.13);
    const s=new THREE.SphereGeometry(r,8,6);
    s.scale(1.15,0.85,1.15);
    s.translate(t[0]+(R()-0.5)*h*0.16,t[1]+(R()-0.5)*h*0.08,t[2]+(R()-0.5)*h*0.16);
    B.put(s,shadeColor(pink,0.82+R()*0.42));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:5,specular:0x3a4432,emissive:0x0a0d08}),
    {c:o.rimC===undefined?0xc8e0b0:o.rimC,i:o.rim===undefined?0.16:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* 茅屋：屋身 + 屋顶 + 门（合批 1 mesh）+ 夜窗烛光（窗面/辉光/点光，构造值=运行期最大值） */
function makeCottage(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(7,3.6,5.4); body.translate(0,1.8,0); B.put(body,0x2a2418);
  const cap=new THREE.ConeGeometry(5.9,2.9,4); cap.rotateY(Math.PI/4); cap.translate(0,5.05,0); B.put(cap,0x1c2c1a);
  const door=new THREE.BoxGeometry(1.3,2.6,0.12); door.translate(1.8,1.3,2.72); B.put(door,0x141008);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x2c2a1c,emissive:0x050704}),{c:0xbcd2a0,i:0.12,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const win=new THREE.Mesh(new THREE.PlaneGeometry(1.7,1.5),
    new THREE.MeshBasicMaterial({color:0xffca7a,transparent:true,opacity:0.92}));
  win.position.set(-1.5,2.1,2.76); g.add(win);
  const hm=new THREE.SpriteMaterial({map:glowTex(),color:0xffb668,transparent:true,opacity:0.42,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const halo=new THREE.Sprite(hm); halo.scale.set(9,9,1); halo.position.set(-1.5,2.3,3.7); halo.renderOrder=2;
  g.add(halo);
  const pl=new THREE.PointLight(0xffb668,1.3,32); pl.position.set(-1.5,2.4,4.8); g.add(pl);
  return {g,win,hm,pl};
}

/* 枝头鸟：身/头/喙/尾合批 1 mesh + 双翅（扑动）；夜色里的墨绿剪影 */
function makeBirdSil(o){
  o=o||{};
  const c=o.color===undefined?0x101c12:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,8,6); body.scale(1.25,1,1.5); body.translate(0,0.34,0); B.put(body,c);
  const head=new THREE.SphereGeometry(0.17,8,6); head.translate(0,0.66,0.30); B.put(head,c);
  const beak=new THREE.ConeGeometry(0.05,0.20,5); beak.rotateX(Math.PI/2); beak.translate(0,0.66,0.52); B.put(beak,shadeColor(c,1.7));
  const tail=new THREE.ConeGeometry(0.10,0.55,5); tail.rotateX(-Math.PI/2.6); tail.translate(0,0.36,-0.42); B.put(tail,c);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:8,specular:0x2c3a26,emissive:0x040604}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const wm=new THREE.MeshBasicMaterial({color:c,side:THREE.DoubleSide,transparent:true,opacity:0.95});
  const wg=new THREE.PlaneGeometry(0.55,0.30);
  const wl=new THREE.Mesh(wg,wm); wl.position.set(-0.26,0.40,0);
  const wr=new THREE.Mesh(wg,wm); wr.position.set(0.26,0.40,0);
  g.add(wl,wr);
  g.userData={wm,wl,wr};
  return g;
}

/* 远鸟群：双翅扑动的剪影（掠过天际，参考骨架 bSea 的飞鸟） */
function makeFlock(o){
  o=o||{};
  const c=o.color===undefined?0x14231a:o.color;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<(o.n===undefined?5:o.n);i++){
    const bm=new THREE.MeshBasicMaterial({color:c,side:THREE.DoubleSide,transparent:true,opacity:0.9});
    const b=new THREE.Group();
    const wg=new THREE.PlaneGeometry(o.w===undefined?3.0:o.w,0.85);
    const w1=new THREE.Mesh(wg,bm); w1.position.x=-wg.parameters.width*0.45;
    const w2=new THREE.Mesh(wg,bm); w2.position.x=wg.parameters.width*0.45;
    b.add(w1,w2); g.add(b);
    items.push({b,w1,w2,sp:0.045+Math.random()*0.05,r:70+Math.random()*80,
      y:(o.y0===undefined?28:o.y0)+Math.random()*16,ph:Math.random()*10,a0:Math.random()*6});
  }
  return {g,items};
}

/* 夜雨：快速下落 + 风斜 + 阵风摆动（Points 自定义着色器） */
const CX_RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB;
uniform float uSlant; uniform float uWind;
varying float vA;
void main(){
  vec3 p=position;
  float y=mod(p.y-uB-uTime*uFall*(0.8+aSeed*0.4),uH);
  p.y=uB+y;
  p.x+=(uH-y)*uSlant+sin(uTime*1.4+aSeed*40.0)*uWind;
  p.z+=cos(uTime*1.1+aSeed*25.0)*uWind*0.5;
  vA=0.35+0.65*smoothstep(0.0,3.0,y);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const CX_RAIN_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; uniform float uTilt; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float cs=cos(uTilt),sn=sin(uTilt);
  q=mat2(cs,-sn,sn,cs)*q;
  q.y*=0.40;                                   // 拉长成雨丝
  float a=smoothstep(0.5,0.18,length(q))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeRain(o){
  const d=Object.assign({n:1000,box:[150,44,100],pos:[0,22,4],color:0xa8c4b0,size:3.6,
    fall:26,slant:0.38,wind:1.5,maxA:0.55,tilt:0.35},o);
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(d.n*3),S=new Float32Array(d.n),Z=new Float32Array(d.n);
  for(let i=0;i<d.n;i++){
    P[i*3]=d.pos[0]+(Math.random()-0.5)*d.box[0];
    P[i*3+1]=d.pos[1]+Math.random()*d.box[1];
    P[i*3+2]=d.pos[2]+(Math.random()-0.5)*d.box[2];
    S[i]=Math.random(); Z[i]=d.size*(0.6+Math.random()*0.8);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uFall:{value:d.fall},uH:{value:d.box[1]},uB:{value:d.pos[1]},
      uSlant:{value:d.slant},uWind:{value:d.wind},uColor:{value:C(d.color)},
      uTilt:{value:d.tilt},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:CX_RAIN_VERT,fragmentShader:CX_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

function bCover(){ // 卷首 · 青雾晨林，零星花瓣飘落，天将破晓
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d1810,c2:0x142619,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:30,layers:3,peaks:5,seed:41,color:0x0d1b12,atmo:0x2e4633,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-12});
  ridge.g.position.set(0,0,-70); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const t1=makeBlossomTree({h:15,seed:13,scale:1.5}); t1.g.position.set(-16,-1.5,-34); g.add(t1.g);
  const t2=makeBlossomTree({h:13,seed:27,scale:1.25}); t2.g.position.set(18,-1.5,-46); g.add(t2.g);
  const petals=makePetals({n:70,box:[150,34,90],pos:[0,14,-18],maxA:0.34,fall:0.020});
  g.add(petals.points);
  const motes=makeGlow({n:50,box:[200,36,120],pos:[0,10,-30],color:0xcfe09a,size:7,speed:0.03,
    rise:0,add:true,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:10,spread:[260,40,150],pos:[0,12,-52],scale:84,color:0x1e3826,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:52,n:9,d:7,color:0x081009,seed:9,sway:0.7,rim:0.12,rimC:0x9fce8f});
  brL.g.position.set(-27,-1.5,44); brL.g.scale.setScalar(2.1); g.add(brL.g);
  const brR=makeForeground({kind:'树枝',w:42,n:8,d:6,color:0x081009,seed:17,sway:0.6,rim:0.12,rimC:0x9fce8f});
  brR.g.position.set(25,-1.5,38); brR.g.scale.setScalar(1.8); g.add(brR.g);
  addLights(g,{c:0xd8c88a,i:0.5,p:[40,90,30]},{c:0x22301f,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); petals.update(t); motes.update(t); mist.update(t,k);
    brL.update(t,k); brR.update(t,k);
    t1.g.rotation.z=Math.sin(t*0.30)*0.006; t2.g.rotation.z=Math.sin(t*0.26+2)*0.007;
  }};
}
function bSleep(){ // 一 · 春眠不觉晓 —— 夜闱烛光渐黯，天光欲晓，萤火渐隐
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0b130d,c2:0x101d12,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:220,h:40,layers:3,peaks:5,seed:51,color:0x0a150e,atmo:0x1c2e1c,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-90); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 中景：茅屋夜窗一点烛光（夜将尽，烛光渐黯） */
  const cot=makeCottage({}); cot.g.position.set(10,0,-5); cot.g.rotation.y=0.12; g.add(cot.g);
  /* 花树两株（暗剪影，花团只微微可辨） */
  const t1=makeBlossomTree({h:12,seed:31,pink:0x8a6a7c}); t1.g.position.set(-12,0,-18); g.add(t1.g);
  const t2=makeBlossomTree({h:15,seed:45,pink:0x7c6070}); t2.g.position.set(-32,0,-44); g.add(t2.g);
  /* 黄绿萤火（随天光渐亮而隐去） */
  const flies=makeGlow({n:46,box:[70,9,46],pos:[-2,4,-8],color:0xd8e89a,size:8,speed:0.035,
    rise:0,add:true,maxA:0.55});
  g.add(flies.points);
  const mist=makeMist({n:10,spread:[220,40,140],pos:[0,9,-42],scale:78,color:0x1b3022,op:0.13});
  g.add(mist.g);
  /* 前景：坡石两丛（框住画面下缘两角） */
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:14,d:6,color:0x080f09,seed:63,rim:0.12,rimC:0x9fce8f});
  rk.g.position.set(16,-1.4,12); g.add(rk.g);
  const rkL=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x080f09,seed:71,rim:0.12,rimC:0x8fbc7c});
  rkL.g.position.set(-15,-1.4,12); g.add(rkL.g);
  addLights(g,{c:0x93a06e,i:0.32,p:[-40,50,10]},{c:0x1a2618,i:0.7});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    const dim=1-sstep(6,16,stageT);                 // 夜将尽，烛光渐黯（下限见各系数）
    const fl=0.75+0.25*Math.sin(t*5.3)+0.12*Math.sin(t*13.1);
    ridge.update(t,0); flies.update(t); mist.update(t,k); rk.update(t,k); rkL.update(t,k);
    t1.g.rotation.z=Math.sin(t*0.3)*0.005; t2.g.rotation.z=Math.sin(t*0.26+1)*0.006;
    cot.win.material.opacity=0.92*(0.5+0.35*fl)*Math.max(dim,0.30)*k;
    cot.hm.opacity=0.42*(0.75+0.25*Math.sin(t*2.7))*Math.max(dim,0.34)*k;
    cot.pl.intensity=1.3*(0.72+0.28*Math.min(fl,1))*Math.max(dim,0.30)*k;
    flies.mat.uniforms.uMaxA.value=0.55*Math.max(1-sstep(9,19,stageT),0.15);
  }};
}
function bBirds(){ // 二 · 处处闻啼鸟 —— 晨光渐亮，枝头群鸟此起彼伏，远处村落人影晨起
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x142418,c2:0x1b3220,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:36,layers:3,peaks:5,seed:61,color:0x142619,atmo:0x55703f,
    fogK:0.60,glowK:0.05,glow:0xd8e8b0,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 中景：大花树立枝头鸟（啼鸣的主角），诗人独立树下听鸟 */
  const tree=makeBlossomTree({h:12,seed:77,clusters:8,scale:1.25});
  tree.g.position.set(-6,0,-8); g.add(tree.g);
  const perched=[];
  [[-7.4,9.0,-6.2],[-4.6,9.8,-7.4],[-6.2,10.6,-9.0],[-7.8,8.2,-9.6]].forEach(function(p,i){
    const b=makeBirdSil({}); b.position.set(p[0],p[1],p[2]); b.rotation.y=i*1.6+0.6;
    g.add(b); perched.push({b,py:p[1],ph:i*1.7});
  });
  const fig=makeFigure({pose:'独立',robe:0x39442e,belt:0x6b7a4e,collar:0xd8e4c8,hat:'发髻',
    scale:1.15,rim:0.4,rimC:0xd8ecc0});
  fig.position.set(4.5,0,3.5); fig.rotation.y=-2.4; g.add(fig);
  /* 远处村落晨起人影（「处处」之意，1 draw call） */
  const crowd=makeCrowd({n:8,rect:[-72,-74,144,10],seed:23,color:0x14231a,rimC:0x9fce8f,rim:0.10,
    sMin:0.5,sMax:0.8});
  g.add(crowd.mesh);
  /* 远鸟群掠过天际 + 光羽微尘 */
  const flock=makeFlock({n:5,y0:26}); g.add(flock.g);
  const motes=makeGlow({n:60,box:[160,30,90],pos:[0,12,-20],color:0xf2e2a0,size:6,speed:0.028,
    rise:0,add:true,maxA:0.26});
  g.add(motes.points);
  const petals=makePetals({n:50,box:[130,30,70],pos:[0,13,-12],maxA:0.28,fall:0.018});
  g.add(petals.points);
  const mist=makeMist({n:8,spread:[240,30,130],pos:[0,8,-60],scale:70,color:0x2a4430,op:0.09});
  g.add(mist.g);
  /* 前景：芦苇（框住画面右下缘） */
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x0c1810,seed:81,sway:1.0,tip:0x4a5c38});
  reed.g.position.set(14,-1.4,13); g.add(reed.g);
  addLights(g,{c:0xf2c94c,i:0.9,p:[-110,45,-140]},{c:0x33452c,i:0.72});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); reed.update(t,k); fig.update(t,k); crowd.update(t);
    motes.update(t); petals.update(t);
    tree.g.rotation.z=Math.sin(t*0.32)*0.006;
    for(const o of perched){
      const env=0.5+0.5*Math.sin(t*1.6+o.ph);         // 轮流啼鸣，此起彼伏
      o.b.position.y=o.py+env*0.10+Math.abs(Math.sin(t*7+o.ph))*0.05;
      const w=-0.25-env*0.35+Math.sin(t*11+o.ph)*0.12;
      o.b.userData.wl.rotation.z=w; o.b.userData.wr.rotation.z=-w;
    }
    for(const o of flock.items){
      const a=o.a0+t*o.sp;
      o.b.position.set(Math.sin(a)*o.r,o.y+Math.sin(t*0.7+o.ph)*3,-30+Math.cos(a)*o.r*0.5);
      o.b.rotation.y=-a+Math.PI/2;
      const f=Math.sin(t*9+o.ph)*0.55; o.w1.rotation.z=f; o.w2.rotation.z=-f;
    }
  }};
}
function bStorm(){ // 三 · 夜来风雨声 —— 忆中之夜：风摇花树，雨打春山
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:90,amp:0.5,freq:0.14,speed:1.2,flow:[0.1,0.3],spec:0.9,
    deep:0x081209,shallow:0x142a18,skyc:0x1c2f1e,moonDir:[0,1,0],y:-0.3});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:44,layers:3,peaks:6,seed:91,color:0x070f0a,atmo:0x16241a,
    fogK:0.66,glowK:0.03,glow:0x8aa886,y:-6});
  ridge.g.position.set(0,0,-100); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 风摇花树（花瓣被雨打落）+ 暗树两株 */
  const t1=makeBlossomTree({h:11,seed:93,pink:0x6a5468}); t1.g.position.set(-13,0,-22); g.add(t1.g);
  const t2=makeBlossomTree({h:9,seed:95,pink:0x5c4a5c}); t2.g.position.set(15,0,-34); g.add(t2.g);
  const t3=makeBlossomTree({h:13,seed:97,trunk:0x171208,pink:0x2c2420,clusters:3});
  t3.g.position.set(-30,0,-52); g.add(t3.g);
  const rain=makeRain({n:800}); g.add(rain.points);
  const mist=makeMist({n:10,spread:[260,36,150],pos:[0,10,-56],scale:80,color:0x0e1a12,op:0.14});
  g.add(mist.g);
  /* 前景：岩壁 + 湿苇（风里横摇） */
  const rock=makeForeground({kind:'岩壁',n:3,r:4.0,w:18,d:6,color:0x050a06,seed:99,rim:0.10,rimC:0x6a8a5c});
  rock.g.position.set(14,-2,16); g.add(rock.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x081009,seed:101,sway:1.6,tip:0x3a4a30});
  reed.g.position.set(-15,-1.6,16); g.add(reed.g);
  addLights(g,{c:0x5f6f63,i:0.3,p:[30,80,20]},{c:0x17211a,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    const gust=1+0.5*Math.sin(t*0.9)+0.25*Math.sin(t*2.3);   // 阵风
    water.update(t); ridge.update(t,0); rain.update(t); mist.update(t,k);
    rock.update(t,k); reed.update(t,k);
    t1.g.rotation.z=Math.sin(t*1.7)*0.05*gust;
    t2.g.rotation.z=Math.sin(t*1.5+2)*0.06*gust;
    t3.g.rotation.z=Math.sin(t*1.3+4)*0.04*gust;
    reed.g.rotation.z=Math.sin(t*2.1)*0.05*gust;
  }};
}
function bPetals(){ // 四（末境·可点击）· 花落知多少 —— 标志性瞬间：雨霁初晴，漫天落英，点击花落更急
  const g=new THREE.Group();
  const ctl={t:0,boost:0,clicked:false};
  const water=makeWater({size:820,seg:90,amp:0.16,freq:0.12,speed:0.55,flow:[0.04,0.06],spec:0.8,
    deep:0x0a1a12,shallow:0x245232,skyc:0x7a9a5a,moonDir:[-0.5,1,0.2],y:-0.3});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:34,layers:3,peaks:5,seed:111,color:0x1a2e1e,atmo:0x8fae66,
    fogK:0.58,glowK:0.06,glow:0xeaf2c8,y:-8});
  ridge.g.position.set(0,0,-100); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 池岸（落花毯的落点） */
  const bank=new THREE.Mesh(new THREE.CircleGeometry(21,36),
    new THREE.MeshPhongMaterial({color:0x1a2f1e,shininess:40,specular:0x3a5230}));
  bank.rotation.x=-Math.PI/2; bank.position.set(0,0.06,2); g.add(bank);
  /* 落花毯：岸边两片粉白浅渍（构造值=运行期最大值） */
  const carpet=[];
  [[-6,0,9,0.16],[5,-6,6.5,0.12]].forEach(function(p,i){
    const m=new THREE.MeshBasicMaterial({color:0xe8c4d4,transparent:true,opacity:p[3]});
    const c=new THREE.Mesh(new THREE.CircleGeometry(p[2],26),m);
    c.rotation.x=-Math.PI/2; c.position.set(p[0],0.10+i*0.012,p[1]); c.renderOrder=1;
    g.add(c); carpet.push({m,base:p[3],ph:i*1.9});
  });
  /* 中景：大花树（雨后犹有繁花）+ 小花树 + 远树 */
  const tree=makeBlossomTree({h:13,seed:121,clusters:8,scale:1.3});
  tree.g.position.set(-8,0,-20); g.add(tree.g);
  const tree2=makeBlossomTree({h:9,seed:123,scale:0.95}); tree2.g.position.set(16,0,-34); g.add(tree2.g);
  const tree3=makeBlossomTree({h:12,seed:125,trunk:0x1c150e,pink:0x33262c,clusters:3});
  tree3.g.position.set(-30,0,-52); g.add(tree3.g);
  /* 漫天落英：远层铺天 + 近层贴相机（点击后更急更密） */
  const petalsFar=makePetals({n:150,box:[190,44,110],pos:[0,20,-12],fall:0.022,maxA:0.40});
  const petalsNear=makePetals({n:110,box:[46,26,30],pos:[0,12,4],fall:0.030,maxA:0.58,size:5.4});
  g.add(petalsFar.points,petalsNear.points);
  const mist=makeMist({n:9,spread:[240,32,140],pos:[0,8,-46],scale:72,color:0x2a4430,op:0.09});
  g.add(mist.g);
  /* 前景：芦苇 + 坡石（框住画面下缘） */
  const rkL=makeForeground({kind:'坡石',n:3,r:3.0,w:13,d:6,color:0x0a120b,seed:131,rim:0.12,rimC:0xbcd8a0});
  rkL.g.position.set(-13,-1.5,13); g.add(rkL.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.8,w:10,d:5,color:0x0a120b,seed:133,rim:0.12,rimC:0xbcd8a0});
  rk.g.position.set(12,-1.4,14); g.add(rk.g);
  addLights(g,{c:0xf6d878,i:1.0,p:[-80,90,-50]},{c:0x3c5033,i:0.72});
  const pl=new THREE.PointLight(0xffe8b0,0.55,60); pl.position.set(0,6,8); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ctl.boost=Math.max(0,ctl.boost-dt/3.4);
      const b=ctl.boost;
      water.update(t); ridge.update(t,0); mist.update(t,k); rkL.update(t,k); rk.update(t,k);
      petalsFar.update(t); petalsNear.update(t);
      /* 花落更急：速度/密度在满亮基座上按点击系数抬升 */
      petalsNear.mat.uniforms.uFall.value=0.030*(1+2.2*b);
      petalsFar.mat.uniforms.uFall.value=0.022*(1+1.8*b);
      petalsNear.mat.uniforms.uMaxA.value=0.58*(1+0.40*b);
      petalsFar.mat.uniforms.uMaxA.value=0.40*(1+0.30*b);
      tree.g.rotation.z=Math.sin(t*0.35)*0.008; tree2.g.rotation.z=Math.sin(t*0.30+2)*0.010;
      carpet.forEach(function(p){ p.m.opacity=k*p.base*(0.9+0.1*Math.sin(t*0.5+p.ph)); });
      pl.intensity=k*0.55*(0.86+0.14*Math.sin(t*0.9));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0,0.16); pluck(5,0.3,0.10);
        const fl=$('#flash'); fl.textContent='花落知多少'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.boost=1;                                     // 花落更急（可反复点）
    },clicked:false};
  return api;
}
