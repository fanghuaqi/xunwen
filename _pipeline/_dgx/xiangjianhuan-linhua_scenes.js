/* ================= 相见欢·林花谢了春红 · 两境场景（青绿春晓·暮春风雨变体：花谢匆匆、长恨东流）
   本诗专属系统「风雨摧花」：朝雨/晚风轮替打落春红 + 点击后红瓣辞枝、东流水涨 ================= */

/* 春红花瓣：粉白小片缓落 + 摆动翻飞（Points 自定义着色器；青绿底上唯一暖彩） */
const XW_PETAL_VERT=`
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
const XW_PETAL_FRAG=`
uniform vec3 uC1; uniform vec3 uC2; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vRot; varying float vMix;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float cs=cos(vRot),sn=sin(vRot);
  q=mat2(cs,-sn,sn,cs)*q;
  q.x*=1.85;
  float a=smoothstep(0.5,0.30,length(q))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(mix(uC1,uC2,vMix),a);
}`;
function makePetals(o){
  const d=Object.assign({n:120,box:[90,32,60],pos:[0,16,-16],fall:0.024,sway:2.0,wind:0.06,
    size:4.4,maxA:0.5,c1:0xc98f9f,c2:0xeed6dc},o);
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
    vertexShader:XW_PETAL_VERT,fragmentShader:XW_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* 寒雨：斜雨丝（Points 自定义着色器，拉长成雨丝，随风摆） */
const XW_RAIN_VERT=`
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
const XW_RAIN_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; uniform float uTilt; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float cs=cos(uTilt),sn=sin(uTilt);
  q=mat2(cs,-sn,sn,cs)*q;
  q.y*=0.40;
  float a=smoothstep(0.5,0.18,length(q))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeRain(o){
  const d=Object.assign({n:800,box:[140,42,96],pos:[0,21,2],color:0xa4c2b6,size:3.6,
    fall:26,slant:0.34,wind:1.4,maxA:0.5,tilt:0.32},o);
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
    vertexShader:XW_RAIN_VERT,fragmentShader:XW_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* 花树：主干收分 + 发散枝条 + 春红花团（合批 1 mesh；残树用暗簇表现"谢了"） */
function makeBlossomTree(o){
  o=o||{};
  const h=o.h===undefined?11:o.h, R=seedRnd(o.seed===undefined?11:o.seed);
  const trunkC=o.trunk===undefined?0x241c14:o.trunk;
  const pink=o.pink===undefined?0xc98f9f:o.pink;
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
    B.put(s,shadeColor(pink,0.9+R()*0.55));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:5,specular:0x3a4432,emissive:o.em===undefined?0x160b10:o.em}),
    {c:o.rimC===undefined?0xd8aab8:o.rimC,i:o.rim===undefined?0.22:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* 「风雨摧花」节律：一个周期内前半场雨（朝来寒雨）、后半场风（晚来风），各自渐起渐收 */
function gustCycle(t,P){
  const ph=((t%P)+P)%P/P;
  const win=function(x){ return sstep(0.10,0.30,x)*(1-sstep(0.52,0.75,x)); };
  return {rain:win(ph),wind:win((ph+0.5)%1)};
}

function bCover(){ // 卷首 · 暮春破晓：青绿林苑，春红零星飘落
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d1810,c2:0x152718,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:32,layers:3,peaks:5,seed:41,color:0x0d1b12,atmo:0x2c4434,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-12});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  /* 远处花树两株（春红）+ 暗绿杂树 + 林间小径 */
  const t1=makeBlossomTree({h:15,seed:13,pink:0xb88494,scale:1.5}); t1.g.position.set(-18,-1.5,-38); g.add(t1.g);
  const t2=makeBlossomTree({h:13,seed:27,pink:0xb88494,scale:1.2}); t2.g.position.set(20,-1.5,-50); g.add(t2.g);
  const t3=makeBlossomTree({h:14,seed:29,pink:0x22301e,clusters:5,branches:7,scale:1.3,em:0x050a05,rimC:0x8fae78}); t3.g.position.set(-34,-1.5,-55); g.add(t3.g);
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.6,0.06,42),
    new THREE.MeshPhongMaterial({color:0x243428,shininess:6}));
  path.rotation.y=0.4; path.position.set(6,-1.4,-30); g.add(path);
  /* 远眺的词人身影 */
  const poet=makeFigure({pose:'独立',robe:0x1f2a20,belt:0x6a5230,hat:'幞头',scale:1.0,rim:0.4,rimC:0x9fce8f});
  poet.position.set(3,-1.5,-24); poet.rotation.y=-0.5; g.add(poet);
  const petals=makePetals({n:70,box:[150,34,90],pos:[0,14,-18],fall:0.020,maxA:0.30});
  g.add(petals.points);
  const motes=makeGlow({n:50,box:[200,36,120],pos:[0,10,-30],color:0xcfe0a8,size:7,speed:0.03,rise:0,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:10,spread:[260,40,150],pos:[0,12,-52],scale:84,color:0x1e3826,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:52,n:9,d:7,color:0x081009,seed:9,sway:0.7,rim:0.12,rimC:0x9fce8f});
  brL.g.position.set(-27,-1.5,44); brL.g.scale.setScalar(2.1); g.add(brL.g);
  const brR=makeForeground({kind:'树枝',w:42,n:8,d:6,color:0x081009,seed:17,sway:0.6,rim:0.12,rimC:0x9fce8f});
  brR.g.position.set(25,-1.5,38); brR.g.scale.setScalar(1.8); g.add(brR.g);
  addLights(g,{c:0xf0e8d0,i:0.5,p:[40,90,30]},{c:0x26351f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); petals.update(t); motes.update(t); mist.update(t,k);
    brL.update(t,k); brR.update(t,k); poet.update(t,k);
    t1.g.rotation.z=Math.sin(t*0.30)*0.006; t2.g.rotation.z=Math.sin(t*0.26+2)*0.007;
  }};
}
function bHuaxie(){ // 一 · 花谢匆匆 —— 满林春红正当谢，朝雨晚风轮替摧花（标志性瞬间）
  const g=new THREE.Group();
  const grd=makeGround({r:200,c1:0x0b130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:38,layers:3,peaks:5,seed:51,color:0x0a150e,atmo:0x2a4230,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  const water=makeWater({size:600,seg:90,amp:0.26,freq:0.1,speed:0.7,flow:[0.55,0.16],spec:1.1,
    deep:0x0a1a14,shallow:0x1e4a38,skyc:0x2a5a44,moonDir:[-60,90,-160],y:-0.4});
  g.add(water.mesh);
  /* 中景：春红花林（一树为主角）+ 暗绿杂树 */
  const tree=makeBlossomTree({h:13,seed:13,clusters:9,scale:1.35});
  tree.g.position.set(-7,0,-16); g.add(tree.g);
  const tree2=makeBlossomTree({h:10,seed:27,clusters:7,scale:1.05}); tree2.g.position.set(9,0,-26); g.add(tree2.g);
  const tree3=makeBlossomTree({h:9,seed:29,clusters:6,scale:0.95}); tree3.g.position.set(-21,0,-30); g.add(tree3.g);
  const tree4=makeBlossomTree({h:8,seed:31,pink:0x8f6a76,clusters:5,scale:0.9}); tree4.g.position.set(23,0,-44); g.add(tree4.g);
  const grove=makeBlossomTree({h:14,seed:33,pink:0x22301e,clusters:5,branches:7,scale:1.4,em:0x050a05,rimC:0x8fae78}); grove.g.position.set(-32,0,-48); g.add(grove.g);
  /* 落红：远层铺天 + 近层贴相机 */
  const petalsFar=makePetals({n:140,box:[180,40,100],pos:[0,18,-14],fall:0.026,maxA:0.34});
  const petalsNear=makePetals({n:90,box:[44,24,28],pos:[2,11,6],fall:0.034,maxA:0.48,size:5.0});
  g.add(petalsFar.points,petalsNear.points);
  /* 朝来寒雨 */
  const rain=makeRain({n:700}); g.add(rain.points);
  /* 一层风头打落的红瓣（阵风起时自树冠迸开） */
  const strip=makeBurst({n:64,color:0xd9a5b2,pos:[-7,10.5,-16]});
  g.add(strip.points);
  /* 词人独立树下 */
  const poet=makeFigure({pose:'独立',robe:0x24301f,belt:0x8f6a33,hat:'幞头',beard:true,scale:1.18,rim:0.5,rimC:0x9fce8f});
  poet.position.set(2.5,0,-8); poet.rotation.y=-0.6; g.add(poet);
  /* 远景赏花人影（零落将散） */
  const crowd=makeCrowd({n:7,rect:[-36,-54,72,12],seed:81,color:0x131e14,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:40,box:[140,24,80],pos:[0,8,-24],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.18});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,32,140],pos:[0,9,-48],scale:76,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rock=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:6,color:0x070d08,seed:61,rim:0.12,rimC:0x9fce8f});
  rock.g.position.set(-13,-1.4,14); g.add(rock.g);
  const reed=makeForeground({kind:'芦苇',w:22,n:10,d:5,color:0x081009,seed:63,sway:1.2,tip:0x2c4028});
  reed.g.position.set(13,-1.2,15); g.add(reed.g);
  addLights(g,{c:0xf0e8d8,i:0.5,p:[-40,80,20]},{c:0x1e2c1e,i:0.62});
  let prevWind=0;
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    const cyc=gustCycle(t,10);   // 朝雨/晚风轮替：前半场雨、后半场风
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    rock.update(t,k); reed.update(t,k); poet.update(t,k); crowd.update(t);
    petalsFar.update(t); petalsNear.update(t); rain.update(t); strip.update(t);
    /* 雨：只在雨场现身；风场收进 */
    rain.mat.uniforms.uMaxA.value=k*0.5*cyc.rain;
    /* 风：花树摇摆、落红更急 */
    const w=cyc.wind;
    tree.g.rotation.z=Math.sin(t*1.5)*0.045*(0.2+w);
    tree2.g.rotation.z=Math.sin(t*1.3+2)*0.05*(0.2+w);
    tree3.g.rotation.z=Math.sin(t*1.1+4)*0.045*(0.2+w);
    reed.g.rotation.z=Math.sin(t*2.0)*0.05*(0.2+w);
    petalsNear.mat.uniforms.uFall.value=0.034*(1+1.8*w+0.5*cyc.rain);
    petalsFar.mat.uniforms.uFall.value=0.026*(1+1.6*w+0.5*cyc.rain);
    petalsNear.mat.uniforms.uMaxA.value=k*0.48*(0.8+0.3*w);
    petalsFar.mat.uniforms.uMaxA.value=k*0.34*(0.8+0.3*w);
    /* 阵风起处：红瓣辞枝一阵 */
    if(w>0.55&&prevWind<=0.55)strip.fire();
    prevWind=w;
  }};
}
function bDongliu(){ // 二（末境·可点击）· 长恨东流 —— 胭脂泪、残红临水；点击：风雨摧花，红瓣辞枝、东流水涨
  const g=new THREE.Group();
  const ctl={t:0,storm:0,flood:0,pulse:0,clicked:false};
  /* 大江东流 */
  const water=makeWater({size:820,seg:96,amp:0.5,freq:0.09,speed:1.0,flow:[0.85,0.22],spec:1.3,
    deep:0x08150f,shallow:0x1a4432,skyc:0x22483a,moonDir:[-60,80,-160],y:0});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:42,layers:3,peaks:5,seed:151,color:0x091209,atmo:0x22361f,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 水畔台地（点击后水涨齐岸） */
  const bank=new THREE.Mesh(new THREE.CylinderGeometry(16,17.5,1.0,36),
    new THREE.MeshPhongMaterial({color:0x14251a,shininess:30,specular:0x2a4230}));
  bank.position.set(2,0.0,-14); g.add(bank);
  /* 残红一树（半谢：明簇与暗簇相间，枝头犹带胭脂泪）+ 暗树 */
  const tree=makeBlossomTree({h:12,seed:155,clusters:8,scale:1.25,pink:0xc98f9f});
  tree.g.position.set(-8,0.4,-18); g.add(tree.g);
  const tree2=makeBlossomTree({h:10,seed:157,clusters:4,scale:1.0,pink:0x5c4450});
  tree2.g.position.set(12,0.4,-26); g.add(tree2.g);
  /* 胭脂泪：残红上水珠滴落（贴树冠小片粉雨） */
  const tears=makePetals({n:40,box:[11,10,11],pos:[-8,10.5,-18],fall:0.05,size:2.6,maxA:0.5,
    c1:0xd9a5b2,c2:0xeed6dc,sway:0.6,wind:0.01});
  g.add(tears.points);
  /* 词人独立水畔，面朝东流 */
  const poet=makeFigure({pose:'独立',robe:0x1e2822,belt:0x7a5f34,hat:'幞头',beard:true,scale:1.2,rim:0.5,rimC:0x9fce8f});
  poet.position.set(4,0.5,-9); poet.rotation.y=1.15; g.add(poet);
  /* 落红两层 */
  const petalsFar=makePetals({n:120,box:[190,42,110],pos:[0,19,-10],fall:0.024,maxA:0.30});
  const petalsNear=makePetals({n:70,box:[48,26,30],pos:[0,12,7],fall:0.030,maxA:0.42,size:4.8});
  g.add(petalsFar.points,petalsNear.points);
  /* 风雨：常态微雨，点击后摧花骤雨 */
  const rain=makeRain({n:800,box:[150,44,100],pos:[0,21,0]}); g.add(rain.points);
  /* 红瓣辞枝（点击迸开）+ 愁绪东流雾（涨水后随流 surge） */
  const strip=makeBurst({n:80,color:0xd9a5b2,pos:[-8,11,-18]});
  g.add(strip.points);
  const flow=makeFlow({n:420,box:[140,10,60],pos:[0,6,-24],color:0x9fb8a8,size:12,speed:5.5,maxA:0.15});
  flow.points.rotation.y=Math.PI/2;   // 雾流转向东（+x，与水同向）
  g.add(flow.points);
  const mist=makeMist({n:10,spread:[250,36,150],pos:[0,9,-50],scale:80,color:0x0e1a12,op:0.14});
  g.add(mist.g);
  const rock=makeForeground({kind:'坡石',n:2,r:2.8,w:10,d:5,color:0x060b07,seed:161,rim:0.10,rimC:0x9fce8f});
  rock.g.position.set(12,-1.4,15); g.add(rock.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x070f09,seed:163,sway:1.4,tip:0x2c4028});
  reed.g.position.set(-14,-1.3,16); g.add(reed.g);
  addLights(g,{c:0x8fa890,i:0.3,p:[-50,70,10]},{c:0x18241c,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ctl.storm+=(1-ctl.storm)*Math.min(1,dt*0.4);
      ctl.flood+=(1-ctl.flood)*Math.min(1,dt*0.22);   // 东流水涨：约 10s 涨满
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.5);
      const st=ctl.storm,fd=ctl.flood,pu=ctl.pulse;
      ridge.update(t,0); water.update(t); mist.update(t,k);
      rock.update(t,k); reed.update(t,k); poet.update(t,k);
      petalsFar.update(t); petalsNear.update(t); tears.update(t);
      rain.update(t); strip.update(t); flow.update(t);
      /* 风雨摧花：骤雨 + 树摇 + 落红更急 + 东流雾涌 */
      rain.mat.uniforms.uMaxA.value=k*(0.10+0.40*st+0.16*pu);
      rain.mat.uniforms.uWind.value=1.4+3.2*st;
      tree.g.rotation.z=Math.sin(t*(1.2+1.3*st))*0.02+Math.sin(t*2.2)*0.05*st*(0.6+pu);
      tree2.g.rotation.z=Math.sin(t*1.4+2)*0.03*(0.3+st);
      reed.g.rotation.z=Math.sin(t*2.1)*0.04*(0.3+st+0.6*pu);
      petalsNear.mat.uniforms.uFall.value=0.030*(1+2.0*st+1.2*pu);
      petalsFar.mat.uniforms.uFall.value=0.024*(1+1.8*st+1.0*pu);
      petalsNear.mat.uniforms.uMaxA.value=k*0.42*(0.8+0.4*st);
      petalsFar.mat.uniforms.uMaxA.value=k*0.30*(0.8+0.4*st);
      tears.mat.uniforms.uMaxA.value=k*0.5*(0.8+0.5*st);
      flow.mat.uniforms.uMaxA.value=k*(0.16+0.22*st+0.12*pu);
      /* 东流水涨：水位齐岸、浪头加大 */
      water.mesh.position.y=0.5*fd;
      water.mesh.material.uniforms.uAmp.value=0.5+0.45*fd;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.16); pluck(2,0.3,0.12); pluck(4,0.7,0.12); pluck(5,1.2,0.10);
        const fl=$('#flash'); fl.textContent='水长东'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      strip.fire(); ctl.pulse=1;              // 红瓣辞枝一阵（可反复点）
    },clicked:false};
  return api;
}
