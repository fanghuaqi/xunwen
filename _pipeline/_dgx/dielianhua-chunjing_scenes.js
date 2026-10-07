/* ================= 蝶恋花·春景 · 三境场景（青绿春晓·晚春墙垣变体：卷首晨园、芳草天涯、墙里墙外）
   本诗专属系统「一墙两世界」：灰白矮墙横贯画面，墙内秋千佳人、墙外土道行人；
   末境点击秋千：笑声渐远渐悄（暖杏光点收隐）+ 柳绵飘少（絮量衰减） ================= */

/* —— 柳绵：白絮随风缓飘、可越墙过道（Points 自定义着色器；青绿底上的浮白） —— */
const DLH_CK_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB;
uniform float uSway; uniform float uWind; uniform float uDrift;
varying float vA; varying float vMix;
void main(){
  vec3 p=position;
  float sp=uFall*(0.75+aSeed*0.5);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.1+aSeed*40.0)*uSway+(uH-y)*uWind;
  p.z+=(uH-y)*uDrift+cos(uTime*0.8+aSeed*27.0)*uSway*0.6;
  vA=smoothstep(0.0,2.4,y)*(0.72+0.28*sin(uTime*1.5+aSeed*31.0));
  vMix=fract(aSeed*7.31);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const DLH_CK_FRAG=`
uniform vec3 uC1; uniform vec3 uC2; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vMix;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  q.x*=1.3;
  float a=smoothstep(0.5,0.16,length(q))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(mix(uC1,uC2,vMix),a);
}`;
function makeCatkins(o){
  const d=Object.assign({n:110,box:[120,26,70],pos:[0,14,-12],fall:0.016,sway:2.4,wind:0.05,drift:0.0,
    size:4.6,maxA:0.4,c1:0xdce8cc,c2:0xf6fbef},o);
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
      uSway:{value:d.sway},uWind:{value:d.wind},uDrift:{value:d.drift},
      uC1:{value:C(d.c1)},uC2:{value:C(d.c2)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:DLH_CK_VERT,fragmentShader:DLH_CK_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 燕阵：一抹合并几何的燕影，绕中心盘旋（1 draw call 一群） —— */
function makeSwallows(o){
  o=o||{};
  const n=o.n===undefined?6:o.n, r=o.r===undefined?10:o.r;
  const c=o.color===undefined?0x0a130d:o.color, R=seedRnd(o.seed===undefined?23:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const a=(i/n)*Math.PI*2+R()*0.8, x=Math.cos(a)*r*(0.8+R()*0.4), z=Math.sin(a)*r*(0.8+R()*0.4);
    const y=(R()-0.5)*2.4, s=0.8+R()*0.5;
    const wl=new THREE.PlaneGeometry(1.5,0.34); wl.rotateX(-Math.PI/2+0.25); wl.rotateZ(0.42);
    wl.scale(s,s,s); wl.translate(x-0.32*s,y,z);
    const wr=new THREE.PlaneGeometry(1.5,0.34); wr.rotateX(-Math.PI/2-0.25); wr.rotateZ(-0.42);
    wr.scale(s,s,s); wr.translate(x+0.32*s,y,z);
    const bd=new THREE.PlaneGeometry(0.85,0.3); bd.rotateX(-Math.PI/2); bd.scale(s,s,s); bd.translate(x,y+0.06,z);
    B.put(wl,c); B.put(wr,c); B.put(bd,c);
  }
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,side:THREE.DoubleSide}));
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.cx===undefined?0:o.cx,o.h===undefined?15:o.h,o.cz===undefined?-20:o.cz);
  const sp=o.speed===undefined?0.14:o.speed, sd=(o.seed===undefined?23:o.seed)%10;
  mesh.rotation.y=R()*6.28;
  return {g,update(t){ mesh.rotation.y+=sp*0.016; g.position.y=g.position.y*0.96+( (o.h===undefined?15:o.h)+Math.sin(t*0.8+sd)*1.1 )*0.04; }};
}

/* —— 暮春杂树：主干+散枝+叶簇/残红花簇/青杏果簇（合批 1 mesh） —— */
function makeSpringTree(o){
  o=o||{};
  const h=o.h===undefined?10:o.h, R=seedRnd(o.seed===undefined?11:o.seed);
  const trunkC=o.trunk===undefined?0x241c14:o.trunk;
  const leaf=o.leaf===undefined?0x2c4426:o.leaf;
  const bloom=o.bloom===undefined?null:o.bloom;      // 残红：暗粉、稀疏
  const fruit=o.fruit===undefined?null:o.fruit;      // 青杏：黄绿小果簇
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*1.2-0.6,h*0.96,0],h*0.05,h*0.014,8),trunkC);
  const nb=o.branches===undefined?8:o.branches, tips=[];
  for(let i=0;i<nb;i++){
    const a=(i/nb)*Math.PI*2+R()*0.9, el=0.45+R()*0.7, len=h*(0.24+R()*0.34);
    const dx=Math.cos(a)*Math.cos(el),dy=Math.sin(el),dz=Math.sin(a)*Math.cos(el);
    const y0=h*(0.46+R()*0.42);
    const p1=[dx*len*0.22,y0+dy*len*0.26,dz*len*0.22], p2=[dx*len,y0+dy*len,dz*len];
    B.put(limbGeo(p1,p2,h*0.019,h*0.007,6),trunkC);
    tips.push([p2[0],p2[1]+len*0.14,p2[2]]);
  }
  const nc=o.clusters===undefined?(nb+2):o.clusters;
  for(let i=0;i<nc;i++){
    const t=tips[i%tips.length]||[0,h*0.9,0];
    const r=h*(0.11+R()*0.09);
    const s=new THREE.SphereGeometry(r,7,5);
    s.scale(1.15,0.85,1.15);
    s.translate(t[0]+(R()-0.5)*h*0.18,t[1]+(R()-0.5)*h*0.1,t[2]+(R()-0.5)*h*0.18);
    const pick=R();
    let col;
    if(bloom&&pick<0.24)col=shadeColor(bloom,0.85+R()*0.5);
    else if(fruit&&pick<0.44)col=shadeColor(fruit,0.9+R()*0.35);
    else col=shadeColor(leaf,0.8+R()*0.55);
    B.put(s,col);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:5,specular:0x33402c,emissive:o.em===undefined?0x0a120a:o.em}),
    {c:o.rimC===undefined?0x9fce8f:o.rimC,i:o.rim===undefined?0.2:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 人家：粉墙黛瓦小屋（墙体+四棱攒尖顶+门+一扇暖杏窗，合批 1+1 mesh） —— */
function makeCottage(o){
  o=o||{};
  const w=o.w===undefined?5:o.w, h=o.h===undefined?2.6:o.h, d=o.d===undefined?4:o.d;
  const wallC=o.wall===undefined?0x5c584c:o.wall, roofC=o.roof===undefined?0x161b14:o.roof;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h/2,0); B.put(body,wallC);
  const roof=new THREE.ConeGeometry(Math.hypot(w,d)*0.62,h*0.62,4); roof.rotateY(Math.PI/4);
  roof.translate(0,h+h*0.31,0); B.put(roof,roofC);
  const door=new THREE.BoxGeometry(w*0.2,h*0.62,0.08); door.translate(0,h*0.31,d/2+0.02); B.put(door,0x0c0f0a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6}),
    {c:0xa8cf8f,i:0.16,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  if(o.window!==false){
    const win=new THREE.Mesh(new THREE.PlaneGeometry(w*0.18,h*0.3),
      new THREE.MeshBasicMaterial({color:0xf2c94c}));
    win.position.set(-w*0.24,h*0.55,d/2+0.03); g.add(win);
  }
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 秋千：木架（A 字双柱+横梁）+ 双绳座板，可摆动（末境标志性瞬间主角） —— */
function makeSwing(o){
  o=o||{};
  const H=o.h===undefined?5.6:o.h, L=o.l===undefined?2.7:o.l;   // 梁高 / 绳长
  const wood=o.wood===undefined?0x4a3a28:o.wood, ropeC=o.rope===undefined?0xb8ae98:o.rope;
  const F=new GeoBag();
  [1,-1].forEach(function(s){
    F.put(limbGeo([s*2.1,0,0.25],[s*0.28,H,0.25],0.16,0.12,7),shadeColor(wood,1.05));
    const bar=limbGeo([s*2.1,0,-0.35],[s*2.1,0,0.85],0.08,0.06,6); F.put(bar,shadeColor(wood,0.85));
  });
  const beam=new THREE.CylinderGeometry(0.13,0.15,5.2,8); beam.rotateZ(Math.PI/2);
  beam.translate(0,H,0.25); F.put(beam,shadeColor(wood,1.15));
  const frame=F.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5}),
    {c:0xa8cf8f,i:0.22,p:2.4}));
  const g=new THREE.Group(); g.add(frame);
  const S=new GeoBag();
  const r1=new THREE.CylinderGeometry(0.035,0.035,L,5); r1.translate(-0.55,-L/2,0.25); S.put(r1,ropeC);
  const r2=new THREE.CylinderGeometry(0.035,0.035,L,5); r2.translate(0.55,-L/2,0.25); S.put(r2,ropeC);
  const seat=new THREE.BoxGeometry(1.5,0.09,0.5); seat.translate(0,-L,0.25); S.put(seat,shadeColor(wood,1.35));
  const seatM=S.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8}));
  const pivot=new THREE.Group(); pivot.position.set(0,H,0); pivot.add(seatM); g.add(pivot);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,pivot};
}

/* —— 灰白矮墙：横贯画面的残墙（墙身+压顶石+苔痕斑驳，合批 1 mesh；一墙隔两世界） —— */
function makeWallDLH(o){
  o=o||{};
  const w=o.w===undefined?150:o.w, h=o.h===undefined?2.7:o.h, d=o.d===undefined?1.15:o.d;
  const R=seedRnd(o.seed===undefined?77:o.seed);
  const B=new GeoBag();
  const nSeg=o.seg===undefined?10:o.seg;
  for(let i=0;i<nSeg;i++){
    const sw=w/nSeg*(1.0+(R()-0.5)*0.06), hh=h*(0.92+R()*0.16);
    const x=-w/2+sw/2+i*(w/nSeg);
    const body=new THREE.BoxGeometry(sw,hh,d);
    body.translate(x+(R()-0.5)*0.12,hh/2-0.06,(R()-0.5)*0.1);
    B.put(body,shadeColor(0x8e897c,0.92+R()*0.16));
    const cap=new THREE.BoxGeometry(sw*1.02,0.26,d+0.28);
    cap.translate(x,hh+0.1,0);
    B.put(cap,shadeColor(0x6b665c,0.9+R()*0.2));
  }
  for(let i=0;i<6;i++){   // 墙脚苔痕
    const moss=new THREE.BoxGeometry(5+R()*6,0.5+R()*0.5,d+0.16);
    moss.translate(-w/2+R()*w,0.22,0);
    B.put(moss,shadeColor(0x2c3a28,0.85+R()*0.4));
  }
  for(let i=0;i<7;i++){   // 墙面斑驳
    const pat=new THREE.BoxGeometry(1.6+R()*2.2,0.8+R()*0.9,0.07);
    pat.translate(-w/2+R()*w,0.5+R()*(h-1.2),d/2+((R()<0.5)?0.03:-0.03));
    B.put(pat,shadeColor(0x767061,0.9+R()*0.2));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,specular:0x3a3f34}),
    {c:0xcfe0b0,i:0.24,p:2.2}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

function bCover(){ // 卷首 · 晚春晨园：青绿郊野，柳绵初飘
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d1810,c2:0x152718,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:32,layers:3,peaks:5,seed:41,color:0x0d1b12,atmo:0x2c4434,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-12});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  const t1=makeSpringTree({h:14,seed:13,bloom:0x9c6470,clusters:8,scale:1.5}); t1.g.position.set(-18,-1.5,-38); g.add(t1.g);
  const t2=makeSpringTree({h:12,seed:27,fruit:0x93b458,scale:1.25}); t2.g.position.set(20,-1.5,-50); g.add(t2.g);
  const t3=makeSpringTree({h:13,seed:29,scale:1.35}); t3.g.position.set(-34,-1.5,-55); g.add(t3.g);
  const cot=makeCottage({scale:1.1}); cot.g.position.set(12,-1.5,-46); cot.g.rotation.y=0.5; g.add(cot.g);
  const path=new THREE.Mesh(new THREE.BoxGeometry(1.8,0.06,40),
    new THREE.MeshPhongMaterial({color:0x243428,shininess:6}));
  path.rotation.y=0.35; path.position.set(4,-1.42,-28); g.add(path);
  const poet=makeFigure({pose:'独立',robe:0x1f2a20,belt:0x6a5230,hat:'幞头',scale:1.0,rim:0.4,rimC:0x9fce8f});
  poet.position.set(6,-1.5,-22); poet.rotation.y=2.6; g.add(poet);
  const ck=makeCatkins({n:60,box:[150,32,90],pos:[0,14,-18],fall:0.016,maxA:0.26});
  g.add(ck.points);
  const motes=makeGlow({n:44,box:[200,34,120],pos:[0,10,-30],color:0xcfe0a8,size:7,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[260,38,150],pos:[0,12,-52],scale:82,color:0x1e3826,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:52,n:9,d:7,color:0x081009,seed:9,sway:0.7,rim:0.12,rimC:0x9fce8f});
  brL.g.position.set(-27,-1.5,44); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const brR=makeForeground({kind:'树枝',w:42,n:8,d:6,color:0x081009,seed:17,sway:0.6,rim:0.12,rimC:0x9fce8f});
  brR.g.position.set(25,-1.5,38); brR.g.scale.setScalar(1.7); g.add(brR.g);
  addLights(g,{c:0xf0e8d0,i:0.5,p:[40,90,30]},{c:0x26351f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ck.update(t); motes.update(t); mist.update(t,k);
    brL.update(t,k); brR.update(t,k); poet.update(t,k);
    t1.g.rotation.z=Math.sin(t*0.30)*0.006; t2.g.rotation.z=Math.sin(t*0.26+2)*0.007;
  }};
}
function bChuncan(){ // 一 · 芳草天涯 —— 残红青杏、燕飞水绕、柳绵吹少
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0b130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:38,layers:3,peaks:5,seed:51,color:0x0a150e,atmo:0x2a4230,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  /* 绿水：斜绕人家的溪流（窄水面 + 两岸土埂同组旋转） */
  const stream=new THREE.Group();
  const water=makeWater({size:14,seg:24,amp:0.10,freq:0.2,speed:0.5,flow:[0.1,0.6],spec:1.0,
    deep:0x0a1a14,shallow:0x1e4a38,skyc:0x2a5a44,moonDir:[-60,90,-160],y:0.12});
  water.mesh.scale.set(1,1,12); stream.add(water.mesh);
  const bankB=new GeoBag();
  const bl=new THREE.BoxGeometry(5.6,1.1,176); bl.translate(-8.4,0.28,0); bankB.put(bl,shadeColor(0x18271c,1.0));
  const br=new THREE.BoxGeometry(5.6,1.1,176); br.translate(8.4,0.28,0); bankB.put(br,shadeColor(0x1a2a1e,1.0));
  const bankM=bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x9fce8f,i:0.14,p:2.4}));
  stream.add(bankM);
  stream.rotation.y=0.55; stream.position.set(2,0,-4); g.add(stream);
  /* 人家：溪畔三户，一户亮着暖杏窗 */
  const cot1=makeCottage({scale:1.15}); cot1.g.position.set(-2,0,-30); cot1.g.rotation.y=-0.35; g.add(cot1.g);
  const cot2=makeCottage({scale:0.95,window:false}); cot2.g.position.set(9,0,-40); cot2.g.rotation.y=-0.15; g.add(cot2.g);
  const cot3=makeCottage({scale:0.85,window:false}); cot3.g.position.set(-13,0,-44); cot3.g.rotation.y=0.25; g.add(cot3.g);
  /* 树：残红一株（对岸）、青杏一株、杂树两株 */
  const tr1=makeSpringTree({h:11,seed:61,bloom:0x9c6470,clusters:9,scale:1.3}); tr1.g.position.set(-20,0,-28); g.add(tr1.g);
  const tr2=makeSpringTree({h:12,seed:63,fruit:0x93b458,clusters:10,scale:1.2}); tr2.g.position.set(26,0,-38); g.add(tr2.g);
  const tr3=makeSpringTree({h:13,seed:65,scale:1.35}); tr3.g.position.set(-34,0,-52); g.add(tr3.g);
  const tr4=makeSpringTree({h:9,seed:67,scale:1.0}); tr4.g.position.set(24,0,-16); g.add(tr4.g);
  /* 燕子飞时：两群燕影绕溪盘旋 */
  const sw1=makeSwallows({n:6,r:9,h:15,cx:2,cz:-20,seed:23,speed:0.16}); g.add(sw1.g);
  const sw2=makeSwallows({n:5,r:7.5,h:19,cx:-10,cz:-40,seed:37,speed:0.12}); g.add(sw2.g);
  /* 词人立近岸望人家 */
  const poet=makeFigure({pose:'独立',robe:0x24301f,belt:0x8f6a33,hat:'幞头',beard:true,scale:1.16,rim:0.5,rimC:0x9fce8f});
  poet.position.set(8,0,-2); poet.rotation.y=2.75; g.add(poet);
  /* 远处村口人影 */
  const crowd=makeCrowd({n:6,rect:[-2,-46,26,10],seed:81,color:0x131e14,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  /* 柳绵：远层铺天 + 近层贴身（吹又少：缓慢疏密起伏） */
  const ckFar=makeCatkins({n:130,box:[180,38,100],pos:[0,18,-12],fall:0.018,maxA:0.30});
  const ckNear=makeCatkins({n:70,box:[46,22,26],pos:[2,10,7],fall:0.024,size:5.0,maxA:0.42});
  g.add(ckFar.points,ckNear.points);
  /* 芳草：青草土丘沿溪点缀 */
  const moundB=new GeoBag();
  [[-22,-16,3.2],[30,-20,2.6],[-32,-40,3.8],[16,-48,3.0],[-6,-56,3.4]].forEach(function(m,i){
    const s=new THREE.SphereGeometry(m[2],9,6); s.scale(1.5,0.34,1.2);
    s.translate(m[0],0.1,m[1]); moundB.put(s,shadeColor(0x1e3620,0.85+0.03*(i%4)));
  });
  const mounds=moundB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5}),
    {c:0x9fce8f,i:0.18,p:2.4}));
  g.add(mounds);
  const motes=makeGlow({n:40,box:[150,26,90],pos:[0,9,-22],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,32,140],pos:[0,9,-48],scale:76,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rock=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:6,color:0x070d08,seed:61,rim:0.12,rimC:0x9fce8f});
  rock.g.position.set(-14,-1.2,14); g.add(rock.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:9,d:5,color:0x081009,seed:63,sway:1.2,tip:0x2c4028,scale:0.8});
  reed.g.position.set(17,-1.0,17); g.add(reed.g);
  addLights(g,{c:0xf0e8d8,i:0.5,p:[-40,80,20]},{c:0x1e2c1e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    rock.update(t,k); reed.update(t,k); poet.update(t,k); crowd.update(t);
    ckFar.update(t); ckNear.update(t);
    sw1.update(t); sw2.update(t);
    /* 柳绵吹又少：絮量缓慢起伏（风时密时疏，越吹越见少） */
    const w=0.5+0.5*Math.sin(t*0.11);
    ckNear.mat.uniforms.uMaxA.value=k*(0.30+0.14*w);
    ckFar.mat.uniforms.uMaxA.value=k*(0.22+0.10*w);
    tr1.g.rotation.z=Math.sin(t*0.5)*0.012; tr2.g.rotation.z=Math.sin(t*0.42+2)*0.014;
  }};
}
function bQiang(){ // 二（末境·可点击）· 墙里墙外 —— 一道矮墙两个世界；点击：秋千渐静、笑声渐悄、柳绵飘少
  const g=new THREE.Group();
  const ctl={t:0,quiet:0,pulse:0,clicked:false};
  const grd=makeGround({r:220,c1:0x0b130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:42,layers:3,peaks:5,seed:151,color:0x091209,atmo:0x22361f,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 灰白矮墙：横贯画面（标志性瞬间：一墙隔两世界） */
  const wall=makeWallDLH({w:150,h:2.7,seg:10,seed:77});
  wall.g.position.set(0,0,-16); wall.g.rotation.y=0.045; g.add(wall.g);
  /* 墙外：土道沿墙 */
  const roadB=new GeoBag();
  const rd=new THREE.BoxGeometry(150,0.3,6.5); rd.translate(0,0.05,-8.5); roadB.put(rd,shadeColor(0x241f19,1.0));
  const ge1=new THREE.BoxGeometry(150,0.5,1.2); ge1.translate(0,0.1,-4.9); roadB.put(ge1,shadeColor(0x1c2e1e,1.0));
  const ge2=new THREE.BoxGeometry(150,0.5,1.2); ge2.translate(0,0.1,-12.1); roadB.put(ge2,shadeColor(0x1c2e1e,1.0));
  const road=roadB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x9fce8f,i:0.14,p:2.4}));
  road.rotation.y=0.045; g.add(road);
  /* 墙外行人：驻足望墙（背身，画面右前） */
  const walker=makeFigure({pose:'独立',robe:0x1f2a20,belt:0x6a5230,hat:'幞头',beard:true,scale:1.15,rim:0.5,rimC:0x9fce8f});
  walker.position.set(7,0,-9.6); walker.rotation.y=Math.PI+0.12; g.add(walker);
  /* 墙内：秋千架 + 佳人在旁（一手轻送） */
  const swing=makeSwing({h:5.6,l:2.7,scale:1.22}); swing.g.position.set(-6,0,-27); swing.g.rotation.y=-0.35; g.add(swing.g);
  const beauty=makeFigure({pose:'指月',robe:0xb08a5e,belt:0xc9a13a,hat:'发髻',scale:1.02,rim:0.55,rimC:0xf2c94c});
  beauty.position.set(-2.6,0,-25.2); beauty.rotation.y=-2.05; g.add(beauty);
  /* 墙内花木：墙里犹有春（一株残红、一株青杏） */
  const tin1=makeSpringTree({h:11,seed:91,bloom:0xc498a2,clusters:8,scale:1.25}); tin1.g.position.set(-20,0,-34); g.add(tin1.g);
  const tin2=makeSpringTree({h:10,seed:93,fruit:0x93b458,clusters:7,scale:1.05}); tin2.g.position.set(9,0,-38); g.add(tin2.g);
  /* 笑语：佳人头顶一撮暖杏光点（全境唯一暖色，点击后渐悄） */
  const laugh=makeGlow({n:30,box:[8,6,6],pos:[-5,7.6,-26],color:0xf2c94c,size:6,speed:0.05,rise:0.4,add:true,maxA:0.34});
  g.add(laugh.points);
  /* 柳绵：从墙里越墙飘到道上（点击后飘少） */
  const ckFar=makeCatkins({n:120,box:[170,36,90],pos:[0,17,-14],fall:0.018,drift:0.035,maxA:0.30});
  const ckNear=makeCatkins({n:60,box:[44,20,24],pos:[2,10,6],fall:0.024,drift:0.05,size:5.0,maxA:0.40});
  g.add(ckFar.points,ckNear.points);
  /* 墙外远处行旅人影 */
  const crowd=makeCrowd({n:5,rect:[30,-8,60,5],seed:87,color:0x131e14,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:36,box:[150,24,90],pos:[0,9,-20],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,32,140],pos:[0,9,-52],scale:78,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const rock=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:5,color:0x060b07,seed:97,rim:0.12,rimC:0x9fce8f});
  rock.g.position.set(14,-1.2,7); g.add(rock.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x070f09,seed:99,sway:1.3,tip:0x2c4028});
  reed.g.position.set(-15,-1.1,8); g.add(reed.g);
  addLights(g,{c:0xe0cf8e,i:0.42,p:[-40,80,10]},{c:0x1c2a1c,i:0.6});
  let swT=0;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ctl.quiet+=(1-ctl.quiet)*Math.min(1,dt*0.30);       // 笑声渐远渐悄
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.5);
      const q=ctl.quiet,pu=ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      rock.update(t,k); reed.update(t,k); walker.update(t,k); beauty.update(t,k);
      crowd.update(t); ckFar.update(t); ckNear.update(t); laugh.update(t);
      /* 秋千：常态轻荡，点击后声悄荡缓 */
      swT+=dt;
      const amp=0.15*(1-0.86*q);
      swing.pivot.rotation.z=Math.sin(swT*1.9)*amp*(1+0.5*pu);
      /* 笑语光点：渐悄；点击瞬间短暂回亮 */
      laugh.mat.uniforms.uMaxA.value=k*0.34*(1-0.82*q)*(0.75+0.6*pu);
      /* 柳绵飘少 */
      ckNear.mat.uniforms.uMaxA.value=k*0.40*(1-0.55*q);
      ckFar.mat.uniforms.uMaxA.value=k*0.30*(1-0.55*q);
      tin1.g.rotation.z=Math.sin(t*0.5)*0.012; tin2.g.rotation.z=Math.sin(t*0.44+2)*0.012;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.16); pluck(2,0.35,0.12); pluck(4,0.8,0.10); pluck(5,1.3,0.08);
        const fl=$('#flash'); fl.textContent='声渐悄'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                              // 笑声又隐约泛起一阵，再渐悄（可反复点）
    },clicked:false};
  return api;
}
