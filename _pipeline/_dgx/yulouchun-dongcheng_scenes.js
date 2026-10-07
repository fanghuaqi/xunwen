/* ================= 玉楼春·东城渐觉风光好 · 两境场景（青绿春晓·春日行乐变体：东城春晓、花间晚照）
   本诗专属系统「红杏枝头春意闹」：枝头繁杏 + 群蜂振翅 + 嗡鸣声浪环（一字千金的「闹」）
   末境可点击红杏：群蜂喧动、春意具象化。红杏红 #c96a6a 是全页唯一暖彩点，禁金。 ================= */

/* 縠皱波光：贴着水面的细密碎光（点着色器，随波明灭 + 顺流缓移；uFade 显式双 shader） */
const YLC_GLM_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFlow; uniform float uCX; uniform float uW;
varying float vA;
void main(){
  vec3 p=position;
  p.x+=sin(uTime*0.5+aSeed*40.0)*2.2+uTime*uFlow;
  p.x=uCX+mod(p.x-uCX+uW*0.5,uW)-uW*0.5;
  p.z+=cos(uTime*0.4+aSeed*27.0)*1.1;
  vA=0.30+0.70*pow(0.5+0.5*sin(uTime*(1.4+aSeed*2.2)+aSeed*90.0),3.0);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const YLC_GLM_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  float a=smoothstep(0.5,0.10,length(gl_PointCoord-vec2(0.5)))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeGlimmer(o){
  const d=Object.assign({n:160,box:[150,1.5,80],pos:[0,1.0,-18],color:0xcfe8c8,size:5.0,maxA:0.34,flow:0.5},o);
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
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFlow:{value:d.flow},uCX:{value:d.pos[0]},uW:{value:d.box[0]},
      uC:{value:C(d.color)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:YLC_GLM_VERT,fragmentShader:YLC_GLM_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* 群蜂：绕红杏枝头盘旋的蜂群（点着色器：轨道 + 快速振翅抖动；uSpread/uBuzz 点击后放大喧动） */
const YLC_BEE_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpread; uniform float uBuzz; uniform vec3 uCenter;
varying float vA;
void main(){
  float ang=uTime*(0.5+aSeed*0.9)+aSeed*40.0;
  float r=(1.1+aSeed*3.6)*uSpread;
  vec3 p=vec3(uCenter.x+cos(ang)*r,
    uCenter.y+(aSeed-0.5)*2.4*uSpread+sin(ang*2.1+aSeed*20.0)*0.9,
    uCenter.z+sin(ang)*r*0.8);
  p+=vec3(sin(uTime*21.0+aSeed*91.0),sin(uTime*26.0+aSeed*57.0),cos(uTime*24.0+aSeed*73.0))
    *(0.05+0.26*uBuzz);
  vA=(0.55+0.45*sin(uTime*30.0+aSeed*130.0))*(0.72+0.28*uBuzz);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const YLC_BEE_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  float a=smoothstep(0.5,0.22,length(gl_PointCoord-vec2(0.5)))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeBees(o){
  const d=Object.assign({n:90,center:[0,10,-16],color:0x6a4a34,size:3.2,maxA:0.55},o);
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(d.n*3),S=new Float32Array(d.n),Z=new Float32Array(d.n);
  for(let i=0;i<d.n;i++){ S[i]=Math.random(); Z[i]=d.size*(0.6+Math.random()*0.8); }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpread:{value:1.0},uBuzz:{value:0.15},
      uCenter:{value:new THREE.Vector3(d.center[0],d.center[1],d.center[2])},
      uC:{value:C(d.color)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:YLC_BEE_VERT,fragmentShader:YLC_BEE_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* 红杏：主干收分 + 发散枝条 + 繁杏花团（红杏红为主，杂暗绿新叶；合批 1 mesh） */
function makeApricotTree(o){
  o=o||{};
  const h=o.h===undefined?11:o.h, R=seedRnd(o.seed===undefined?11:o.seed);
  const trunkC=o.trunk===undefined?0x201810:o.trunk;
  const bloom=o.bloom===undefined?0xc96a6a:o.bloom;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*1.2-0.6,h*0.94,0],h*0.055,h*0.016,8),trunkC);
  const nb=o.branches===undefined?9:o.branches, tips=[];
  for(let i=0;i<nb;i++){
    const a=(i/nb)*Math.PI*2+R()*0.9, el=0.42+R()*0.72, len=h*(0.24+R()*0.36);
    const dx=Math.cos(a)*Math.cos(el),dy=Math.sin(el),dz=Math.sin(a)*Math.cos(el);
    const y0=h*(0.44+R()*0.44);
    const p1=[dx*len*0.22,y0+dy*len*0.26,dz*len*0.22], p2=[dx*len,y0+dy*len,dz*len];
    B.put(limbGeo(p1,p2,h*0.021,h*0.008,6),trunkC);
    tips.push([p2[0],p2[1]+len*0.14,p2[2]]);
  }
  const nc=o.clusters===undefined?(nb+3):o.clusters;
  for(let i=0;i<nc;i++){
    const t=tips[i%tips.length]||[0,h*0.9,0];
    const r=h*(0.14+R()*0.13);
    const s=new THREE.SphereGeometry(r,8,6);
    s.scale(1.15,0.85,1.15);
    s.translate(t[0]+(R()-0.5)*h*0.18,t[1]+(R()-0.5)*h*0.08,t[2]+(R()-0.5)*h*0.18);
    /* 繁杏为主，间以暗绿新叶（红杏红是全页唯一暖彩点） */
    if(R()<0.72) B.put(s,shadeColor(bloom,0.80+R()*0.55));
    else B.put(s,shadeColor(0x22331c,0.8+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x3a4432,emissive:o.em===undefined?0x1c0a0c:o.em}),
    {c:o.rimC===undefined?0x9fce8f:o.rimC,i:o.rim===undefined?0.20:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* 绿杨：主干 + 暗绿冠团 + 垂丝（「绿杨烟外」；合批 1 mesh，整树轻摇） */
function makeWillow(o){
  o=o||{};
  const h=o.h===undefined?10:o.h, R=seedRnd(o.seed===undefined?5:o.seed);
  const tipC=o.tip===undefined?0x54783e:o.tip;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.8-0.4,h*0.92,0],h*0.042,h*0.014,7),0x1a140e);
  for(let i=0;i<4;i++){
    const s=new THREE.SphereGeometry(h*(0.16+R()*0.10),7,5);
    s.scale(1.3,0.9,1.3);
    s.translate((R()-0.5)*h*0.5,h*(0.72+R()*0.18),(R()-0.5)*h*0.4);
    B.put(s,shadeColor(0x22331c,0.8+R()*0.5));
  }
  const nS=o.strands===undefined?14:o.strands;
  for(let i=0;i<nS;i++){
    const a=R()*6.283, rr=h*(0.30+R()*0.30);
    const x0=Math.cos(a)*rr, z0=Math.sin(a)*rr*0.8;
    let px=x0,py=h*(0.62+R()*0.26),pz=z0;
    const len=h*(0.30+R()*0.34);
    for(let k=0;k<3;k++){
      const nx=x0+(R()-0.5)*0.5+Math.cos(a)*len*0.10*(k+1);
      const ny=py-len/3, nz=z0+(R()-0.5)*0.5;
      B.put(limbGeo([px,py,pz],[nx,ny,nz],0.05,0.02,4),k<2?shadeColor(0x1c2c16,0.9+R()*0.4):tipC);
      px=nx;py=ny;pz=nz;
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3a24,emissive:0x060c05}),{c:0x9fce8f,i:0.18,p:2.6}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* 客棹：小船（船体 + 船头 + 甲板 + 斜插水中的棹；合批 1 mesh） */
function makeBoat(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const hullC=o.hull===undefined?0x241a10:o.hull;
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.7,0.4,4.6,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.55,1.45); B.put(hull,hullC);
  const bow=new THREE.ConeGeometry(0.55,1.3,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.7,1.35); bow.translate(2.9,0.05,0); B.put(bow,hullC);
  const deck=new THREE.BoxGeometry(3.4,0.10,1.2); deck.translate(0,0.48,0); B.put(deck,shadeColor(hullC,1.5));
  const stern=new THREE.BoxGeometry(0.5,0.7,1.0); stern.translate(-1.9,0.45,0); B.put(stern,shadeColor(hullC,0.8));
  const oar=new THREE.CylinderGeometry(0.045,0.07,3.4,5);
  oar.rotateZ(2.25); oar.translate(1.2,0.35,0.75); B.put(oar,0x3a2a18);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a2c1a,emissive:0x080503}),{c:0xa8c890,i:0.26,p:2.5}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  return g;
}

/* 红瓣缓落：枝头零星飘落（点着色器，小片翻转；绕树冠小范围） */
const YLC_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH;
varying float vA; varying float vRot;
void main(){
  vec3 p=position;
  float y=mod(p.y-uTime*uFall*(0.7+aSeed*0.6),uH);
  p.y=y;
  p.x+=sin(uTime*1.1+aSeed*40.0)*1.5+(uH-y)*0.05;
  p.z+=cos(uTime*0.8+aSeed*23.0)*1.1;
  vA=smoothstep(0.0,1.5,y)*(0.7+0.3*sin(uTime*1.9+aSeed*31.0));
  vRot=uTime*(0.5+aSeed)+aSeed*17.0;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const YLC_PETAL_FRAG=`
uniform vec3 uC1; uniform vec3 uC2; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vRot;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float cs=cos(vRot),sn=sin(vRot);
  q=mat2(cs,-sn,sn,cs)*q;
  q.x*=1.7;
  float a=smoothstep(0.5,0.28,length(q))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(mix(uC1,uC2,0.5),a);
}`;
function makePetalFall(o){
  const d=Object.assign({n:40,box:[20,11,16],pos:[10,0,-20],fall:0.05,size:4.2,maxA:0.42,
    c1:0xd88a8a,c2:0xeed4cc},o);
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
    uniforms:{uTime:{value:0},uFall:{value:d.fall},uH:{value:d.box[1]},
      uC1:{value:C(d.c1)},uC2:{value:C(d.c2)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:YLC_PETAL_VERT,fragmentShader:YLC_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* 嗡鸣声浪环：自红杏枝头一圈圈荡开的「闹」之波纹（5 片公告环，随龄扩张淡出） */
function makeBuzzRings(o){
  const d=Object.assign({n:5,center:[0,10.5,-16],color:0xcfe4d4,maxA:0.24},o);
  const g=new THREE.Group(), items=[];
  for(let i=0;i<d.n;i++){
    const m=new THREE.Mesh(new THREE.RingGeometry(0.90,1.0,42),
      new THREE.MeshBasicMaterial({color:d.color,transparent:true,opacity:d.maxA,
        side:THREE.DoubleSide,depthWrite:false}));
    m.position.set(d.center[0],d.center[1],d.center[2]);
    m.renderOrder=3; g.add(m);
    items.push({m,ph:i/d.n});
  }
  return {g,update(t,k,buzz){
    for(const it of items){
      const raw=t*(0.16+0.30*buzz)+it.ph, age=raw-Math.floor(raw);
      const s=1.2+age*8.0;
      it.m.scale.setScalar(s);
      it.m.lookAt(camera.position);
      it.m.material.opacity=k*d.maxA*(1-age)*(0.55+0.45*buzz);
    }
  }};
}

function bCover(){ // 卷首 · 东城破晓：青绿园林，绿杨含烟、繁杏初绽
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0x0c1810,c2:0x16281a,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:34,layers:3,peaks:5,seed:71,color:0x0c1a11,atmo:0x2c4434,
    fogK:0.62,glowK:0.06,glow:0xbcd8a0,y:-12});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  /* 绿杨两株 + 远处一株繁杏（暗）+ 林间小径 */
  const w1=makeWillow({h:11,seed:23,scale:1.5}); w1.g.position.set(-19,-1.6,-36); g.add(w1.g);
  const w2=makeWillow({h:9,seed:29,scale:1.2}); w2.g.position.set(17,-1.6,-46); g.add(w2.g);
  const a1=makeApricotTree({h:10,seed:35,scale:1.15,em:0x120708}); a1.g.position.set(29,-1.6,-56); g.add(a1.g);
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.6,0.06,40),
    new THREE.MeshPhongMaterial({color:0x243428,shininess:6}));
  path.rotation.y=0.4; path.position.set(5,-1.5,-28); g.add(path);
  /* 远眺的词人身影 */
  const poet=makeFigure({pose:'独立',robe:0x1f2a20,belt:0x6a5230,hat:'幞头',scale:1.0,rim:0.4,rimC:0x9fce8f});
  poet.position.set(2,-1.6,-24); poet.rotation.y=-0.5; g.add(poet);
  const motes=makeGlow({n:50,box:[200,36,120],pos:[0,10,-30],color:0xcfe0a8,size:7,speed:0.03,rise:0,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:10,spread:[260,40,150],pos:[0,12,-52],scale:84,color:0x1e3826,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:52,n:9,d:7,color:0x081009,seed:9,sway:0.7,rim:0.12,rimC:0x9fce8f});
  brL.g.position.set(-27,-1.6,44); brL.g.scale.setScalar(2.1); g.add(brL.g);
  const brR=makeForeground({kind:'树枝',w:42,n:8,d:6,color:0x081009,seed:17,sway:0.6,rim:0.12,rimC:0x9fce8f});
  brR.g.position.set(25,-1.6,38); brR.g.scale.setScalar(1.8); g.add(brR.g);
  addLights(g,{c:0xf0e8d0,i:0.5,p:[40,90,30]},{c:0x26351f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); motes.update(t); mist.update(t,k);
    brL.update(t,k); brR.update(t,k); poet.update(t,k);
    w1.g.rotation.z=Math.sin(t*0.30)*0.008; w2.g.rotation.z=Math.sin(t*0.26+2)*0.009;
    a1.g.rotation.z=Math.sin(t*0.22+4)*0.006;
  }};
}
function bDongcheng(){ // 一 · 东城春晓 —— 縠皱波纹迎客棹，绿杨烟外红杏闹（标志性瞬间）
  const g=new THREE.Group();
  /* 春水：縠皱细波（高频率低波幅）+ 细密波光 */
  const water=makeWater({size:640,seg:96,amp:0.20,freq:0.17,speed:0.9,flow:[0.45,0.12],spec:1.35,
    deep:0x081711,shallow:0x21503c,skyc:0x356455,moonDir:[60,90,-160],y:0});
  g.add(water.mesh);
  const glim=makeGlimmer({n:190,box:[150,1.5,80],pos:[0,1.0,-18],maxA:0.40});
  g.add(glim.points);
  /* 远山与东岸（岸上绿杨成烟、红杏满枝） */
  const ridge=makeRange({r:240,h:30,layers:3,peaks:5,seed:73,color:0x0b1710,atmo:0x2e4a36,
    fogK:0.62,glowK:0.06,glow:0xaac890,y:-10});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  const bank=makeGround({r:60,c1:0x0d1911,c2:0x1a2c1c,y:0.35});
  bank.mesh.position.set(0,0.35,-75); g.add(bank.mesh);
  /* 主体：客棹 + 船头客（诗人东行） */
  const boat=makeBoat({scale:1.0}); boat.position.set(-4,0.06,-13); boat.rotation.y=0.35;
  boat.scale.set(1.5,1.2,1.35); g.add(boat);
  const poet=makeFigure({pose:'独立',robe:0x24301f,belt:0x8f6a33,hat:'幞头',beard:true,scale:0.95,rim:0.5,rimC:0x9fce8f});
  poet.position.set(-0.5,0.53,0.1); poet.rotation.y=2.55; boat.add(poet);
  /* 绿杨烟外：岸上柳三株 + 柳烟一带 */
  const w1=makeWillow({h:12,seed:23,scale:1.35}); w1.g.position.set(-16,0.2,-38); g.add(w1.g);
  const w2=makeWillow({h:10,seed:29,scale:1.1}); w2.g.position.set(-2,0.2,-46); g.add(w2.g);
  const w3=makeWillow({h:11,seed:31,scale:1.2}); w3.g.position.set(14,0.2,-50); g.add(w3.g);
  const smoke=makeMist({n:8,spread:[110,10,34],pos:[0,6.5,-44],scale:46,color:0x7fa890,op:0.13});
  g.add(smoke.g);
  /* 红杏枝头春意闹：一树繁杏为主角 + 群蜂 + 声浪环 */
  const tree=makeApricotTree({h:11,seed:13,clusters:11,scale:1.4});
  tree.g.position.set(10,0.3,-20); g.add(tree.g);
  const tree2=makeApricotTree({h:9,seed:37,clusters:7,scale:1.0});
  tree2.g.position.set(20,0.3,-34); g.add(tree2.g);
  const bees=makeBees({n:90,center:[10,11.5,-20]}); g.add(bees.points);
  const rings=makeBuzzRings({n:5,center:[10,11.5,-20]}); g.add(rings.g);
  const petals=makePetalFall({n:36,box:[18,10,14],pos:[10,0,-20],maxA:0.40}); g.add(petals.points);
  /* 东城游影：岸上远处的踏青人影 */
  const crowd=makeCrowd({n:6,rect:[-42,-48,54,10],seed:81,color:0x142016,rimC:0x8fae78,rim:0.2,y:0.3});
  g.add(crowd.mesh);
  const motes=makeGlow({n:40,box:[140,24,80],pos:[0,8,-24],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.18});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[220,22,80],pos:[0,9,-58],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  /* 前景框景：坡石 + 芦苇 */
  const rock=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:6,color:0x070d08,seed:61,rim:0.12,rimC:0x9fce8f});
  rock.g.position.set(-13,-1.2,14); g.add(rock.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:7,d:5,color:0x081009,seed:63,sway:1.2,tip:0x2c4028});
  reed.g.position.set(18,-1.0,15); reed.g.scale.setScalar(0.8); g.add(reed.g);
  addLights(g,{c:0xf0ecd8,i:0.55,p:[50,90,20]},{c:0x2a3a24,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); glim.update(t); smoke.update(t,k);
    motes.update(t); mist.update(t,k);
    rock.update(t,k); reed.update(t,k); poet.update(t,k); crowd.update(t);
    bees.update(t); rings.update(t,k,0.15); petals.update(t);
    /* 客棹随波轻荡，绿杨烟中轻摇 */
    boat.rotation.z=Math.sin(t*0.7)*0.022;
    boat.position.y=0.06+Math.sin(t*0.8)*0.07;
    w1.g.rotation.z=Math.sin(t*0.32)*0.010; w2.g.rotation.z=Math.sin(t*0.28+2)*0.011;
    w3.g.rotation.z=Math.sin(t*0.30+4)*0.010;
    tree.g.rotation.z=Math.sin(t*0.5)*0.006;
  }};
}
function bWanzhao(){ // 二（末境·可点击）· 花间晚照 —— 持酒劝斜阳；点击红杏：群蜂喧动、春意具象化
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,buzz:0.15,bloom:0,bee:0};
  /* 花间园地 */
  const grd=makeGround({r:150,c1:0x0c170f,c2:0x182418,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:30,layers:3,peaks:5,seed:77,color:0x0a140d,atmo:0x2c4434,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 斜阳：一轮红日半沉远山 + 红晕（红杏红同族——晚照即杏色） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(8.5,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xd8826e,transparent:true,opacity:0.95,fog:false}));
  sun.position.set(-52,20,-130); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc96a6a,
    transparent:true,opacity:0.52,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(74,74,1); sunGlow.position.set(-52,20,-130); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 晚照光带：杏色微光横过花间 */
  const band=makeGlow({n:80,box:[120,5,60],pos:[-16,2.5,-34],color:0xd88a7a,size:10,speed:0.05,rise:0,maxA:0.26});
  g.add(band.points);
  /* 花间：繁杏三株（一株为主角） */
  const tree=makeApricotTree({h:12,seed:133,clusters:12,scale:1.35});
  tree.g.position.set(-6,0,-19); g.add(tree.g);
  const tree2=makeApricotTree({h:9,seed:137,clusters:7,scale:1.0});
  tree2.g.position.set(12,0,-30); g.add(tree2.g);
  const tree3=makeApricotTree({h:8,seed:139,clusters:6,scale:0.9});
  tree3.g.position.set(-24,0,-36); g.add(tree3.g);
  /* 持酒劝斜阳的词人：举杯（玉杯在手），面朝西斜阳 */
  const poet=makeFigure({pose:'举杯',robe:0x24301f,belt:0x8f6a33,hat:'幞头',beard:true,scale:1.18,
    rim:0.5,rimC:0x9fce8f,noProp:true});
  poet.position.set(1.5,0,-7.5); poet.rotation.y=-2.62; g.add(poet);
  const cup=makeVessel({type:'杯',mat:'玉',scale:0.62,liquid:true,shadow:false});
  cup.g.position.set(0.34,3.14,0.47); poet.add(cup.g);
  /* 花间小案：一壶一杯 */
  const table=makeTable({w:6.5,d:3.2,h:1.1,wood:0x241a10}); table.g.position.set(7.5,0,-11);
  table.g.rotation.y=-0.3; g.add(table.g);
  const jar=makeVessel({type:'壶',mat:'陶',scale:1.15,liquid:true});
  jar.g.position.set(7.0,1.08,-11.4); g.add(jar.g);
  const cup2=makeVessel({type:'杯',mat:'玉',scale:1.0});
  cup2.g.position.set(8.4,1.08,-10.9); g.add(cup2.g);
  /* 群蜂 + 声浪环 + 春意迸发（点击后喧动） */
  const bees=makeBees({n:96,center:[-6,12,-19]}); g.add(bees.points);
  const rings=makeBuzzRings({n:5,center:[-6,12,-19]}); g.add(rings.g);
  const burst=makeBurst({n:90,color:0xd88a8a,pos:[-6,11,-19]}); g.add(burst.points);
  const canopyGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88a7a,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  canopyGlow.scale.set(26,26,1); canopyGlow.position.set(-6,11.5,-19); canopyGlow.renderOrder=3; g.add(canopyGlow);
  const petals=makePetalFall({n:46,box:[24,12,18],pos:[-6,0,-19],maxA:0.40}); g.add(petals.points);
  /* 远游者三人影 + 晚归飞鸟点 */
  const crowd=makeCrowd({n:4,rect:[22,-44,16,8],seed:91,color:0x131e14,rimC:0x8fae78,rim:0.18});
  g.add(crowd.mesh);
  const motes=makeGlow({n:36,box:[130,20,70],pos:[0,7,-26],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,28,130],pos:[0,9,-54],scale:76,color:0x1e3024,op:0.12});
  g.add(mist.g);
  /* 前景框景：树枝 + 坡石 */
  const brL=makeForeground({kind:'树枝',w:44,n:8,d:6,color:0x081009,seed:25,sway:0.8,rim:0.12,rimC:0x9fce8f});
  brL.g.position.set(-24,-1.4,17); brL.g.scale.setScalar(1.9); g.add(brL.g);
  const rock=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:5,color:0x060b07,seed:65,rim:0.10,rimC:0x9fce8f});
  rock.g.position.set(13,-1.2,15); g.add(rock.g);
  addLights(g,{c:0xc99a80,i:0.42,p:[-60,50,10]},{c:0x203020,i:0.60});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ctl.bloom=Math.max(0,ctl.bloom-dt/2.5);
      const bz=ctl.buzz+ctl.bee;
      ridge.update(t,0); band.update(t); motes.update(t); mist.update(t,k);
      brL.update(t,k); rock.update(t,k); poet.update(t,k); crowd.update(t);
      bees.update(t); rings.update(t,k,Math.min(1,bz)); petals.update(t); burst.update(t);
      /* 群蜂喧动：点击后蜂群扩旋、振翅更急 */
      bees.mat.uniforms.uBuzz.value=0.15+ctl.bee+ctl.bloom*0.4;
      bees.mat.uniforms.uSpread.value=1.0+ctl.bee*0.8+ctl.bloom*0.5;
      /* 树冠春光：点击后一瞬透亮 */
      canopyGlow.material.opacity=k*0.5*(0.45+0.35*ctl.bloom+0.10*(0.5+0.5*Math.sin(t*2.3)));
      /* 斜阳下沉的呼吸感 + 晚照光带明灭（峰值 ≤ 初值 0.52） */
      sunGlow.material.opacity=k*(0.40+0.10*Math.sin(t*0.8));
      band.mat.uniforms.uMaxA.value=k*(0.24+0.06*Math.sin(t*0.6));
      /* 花枝摇曳：蜂闹处摇得更欢 */
      const sw=0.008+0.020*(ctl.bee+ctl.bloom);
      tree.g.rotation.z=Math.sin(t*(0.5+0.8*ctl.bee))*sw;
      tree2.g.rotation.z=Math.sin(t*0.42+2)*sw*0.8;
      tree3.g.rotation.z=Math.sin(t*0.38+4)*sw*0.7;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.16); pluck(2,0.35,0.13); pluck(4,0.75,0.12); pluck(5,1.2,0.10);
        const fl=$('#flash'); fl.textContent='春意闹'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      /* 点击红杏：群蜂喧动 + 春意具象化（红瓣迸发，可反复点） */
      ctl.bee=Math.min(1,ctl.bee+0.45); ctl.bloom=1; burst.fire();
    },clicked:false};
  return api;
}
