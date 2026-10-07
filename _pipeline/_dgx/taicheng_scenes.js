/* ================= 台城 · 三境场景（烟雨江南 · 台城柳堤变体：卷首江雨台城、江雨空啼、烟笼十里）
   本诗专属系统「依旧烟笼十里堤」：十里长堤柳色如旧，六朝宫阙残影在烟雨中若隐若现；
   末境点击烟笼堤 → 柳烟漫堤、六朝残影如梦散去（「六朝如梦」），唯柳色依旧。
   与同为烟雨赛道的《定风波》（竹林夜雨）不同：本页是江雨、江草、长堤垂柳与故都残影。 ================= */

/* —— 霏霏江雨：密雨丝（Points 自定义着色器，点内画细长雨丝；远层密、近层疏） —— */
const TC_RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB; uniform float uSway;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uFall*(0.8+aSeed*0.5);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.8+aSeed*47.0)*uSway;
  vA=smoothstep(0.0,uH*0.06,y)*(1.0-smoothstep(uH*0.92,uH,y));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(170.0/max(1.0,-mv.z)),22.0);
  gl_Position=projectionMatrix*mv;
}`;
const TC_RAIN_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.13,0.03,abs(q.x))*smoothstep(0.5,0.05,abs(q.y))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeRainTC(o){
  o=o||{};
  const d=Object.assign({n:340,box:[180,26,90],pos:[0,1,-24],fall:0.09,sway:0.35,
    size:4.5,maxA:0.20,c:0x9fb3c9},o);
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
      uSway:{value:d.sway},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:TC_RAIN_VERT,fragmentShader:TC_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update:function(t){ m.uniforms.uTime.value=t; },mat:m};
}

/* —— 江草齐：江边齐整的青草（合批 1 mesh，风过时整片微倾） —— */
function makeGrassTC(o){
  o=o||{};
  const n=o.n===undefined?1100:o.n, R=seedRnd(o.seed===undefined?23:o.seed);
  const w=o.w===undefined?240:o.w, d=o.d===undefined?26:o.d, B=new GeoBag();
  for(let i=0;i<n;i++){
    const h=0.55+R()*1.15, x=(R()-0.5)*w, z=(R()-0.5)*d;
    const bl=new THREE.ConeGeometry(0.055,h,4);
    bl.rotateZ((R()-0.5)*0.3); bl.rotateY(R()*6.283);
    bl.translate(x,h*0.5,z);
    B.put(bl, shadeColor(o.color===undefined?0x54703c:o.color, 0.7+R()*0.6));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3a24,emissive:0x070c06,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x9fb3c9:o.rimC,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.y=o.y===undefined?0:o.y;
  g.update=function(t,k){ g.rotation.z=0.012*Math.sin(t*0.55)*(k===undefined?1:k); };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 台城柳：垂柳（主干 + 主枝 + 下垂柳条 + 柳叶），合批 1 mesh，微风中轻摆 —— */
function makeWillowTC(o){
  o=o||{};
  const h=o.h===undefined?6.4:o.h, R=seedRnd(o.seed===undefined?17:o.seed);
  const wood=o.wood===undefined?0x2b2418:o.wood, leafC=o.leaf===undefined?0x6f8f52:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.7,h*0.56,0],h*0.075,h*0.036,7),wood);
  const nb=o.branches===undefined?7:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5;
    const tip=[Math.sin(a)*h*0.44, h*(0.70+R()*0.14), Math.cos(a)*h*0.44];
    B.put(limbGeo([0,h*0.52,0],tip,h*0.030,h*0.012,6),shadeColor(wood,1.22));
    const ns=o.strands===undefined?4:o.strands;
    for(let k=0;k<ns;k++){
      const sx=tip[0]+(R()-0.5)*1.1, sz=tip[2]+(R()-0.5)*1.1;
      const len=h*(0.34+R()*0.34);
      const p0=[sx,tip[1],sz];
      const p1=[sx+(R()-0.5)*0.55, tip[1]-len*0.55, sz+(R()-0.5)*0.55];
      const p2=[sx+(R()-0.5)*0.95, tip[1]-len, sz+(R()-0.5)*0.95];
      B.put(limbGeo(p0,p1,0.034,0.023,5),shadeColor(leafC,0.86+R()*0.28));
      B.put(limbGeo(p1,p2,0.023,0.013,5),shadeColor(leafC,0.78+R()*0.38));
      for(let q=0;q<3;q++){
        const lf=new THREE.PlaneGeometry(0.62,0.14);
        lf.rotateZ((R()-0.5)*0.7);
        lf.translate(p2[0]+(R()-0.5)*0.42, tip[1]-len*(0.5+0.17*q), p2[2]+(R()-0.5)*0.42);
        B.put(lf,shadeColor(0x93b26a,0.78+R()*0.5));
      }
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4a30,emissive:0x0a120a,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x9fb3c9:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=(o.sway===undefined?0.05:o.sway)*Math.sin(t*0.5+ph)*kk;
    g.rotation.x=0.03*Math.sin(t*0.42+ph*1.7)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 十里长堤：一条横贯画面的江堤（堤身 + 护堤石 + 堤上小径），合批 1 mesh —— */
function makePierTC(o){
  o=o||{};
  const len=o.len===undefined?170:o.len, R=seedRnd(o.seed===undefined?31:o.seed), B=new GeoBag();
  const body=new THREE.BoxGeometry(len,2.6,o.d===undefined?9:o.d); body.translate(0,1.0,0); B.put(body,0x2f3a34);
  const top=new THREE.BoxGeometry(len*1.01,0.26,o.d===undefined?9:o.d); top.translate(0,2.42,0); B.put(top,0x46544a);
  for(let i=0;i<34;i++){
    const rg=rockGeo(0.7+R()*0.9,1,R);
    rg.translate(-len/2+len*R(),0.35+(R()-0.5)*0.5,(o.d===undefined?9:o.d)*(0.42+(R()-0.5)*0.5));
    B.put(rg,shadeColor(0x28322c,0.7+R()*0.6));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3a34,emissive:0x060a08}),{c:o.rimC===undefined?0x8fb3c9:o.rimC,i:0.18,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x, o.y===undefined?0:o.y, o.z===undefined?-4:o.z);
  return {g,mesh};
}

/* —— 六朝残影：烟雨里若隐若现的宫阙断壁残柱（共用一个半透材质，末境点击后散尽） —— */
function makeRuinTC(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?43:o.seed), B=new GeoBag();
  for(let i=0;i<7;i++){
    const x=(R()-0.5)*46, z=(R()-0.5)*14;
    const hh=3.4+R()*4.6;
    const col=new THREE.CylinderGeometry(0.5,0.62,hh,8); col.translate(x,hh/2,z); B.put(col,0xb8c4d0);
    if(R()<0.6){
      const wall=new THREE.BoxGeometry(5+R()*7,1.6+R()*2.6,0.8); wall.translate(x+(R()-0.5)*7,1.2,z+(R()-0.5)*6);
      B.put(wall,0x9aa8b6);
    }
  }
  const mat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,transparent:true,opacity:0.42,
    depthWrite:false,shininess:4,emissive:0x30383f});
  const mesh=B.mesh(mat); mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?-46:o.z);
  return {g,mesh,mat};
}

/* —— 柳烟：沿堤弥漫的雨烟（Sprite 层；只调 scale，不写 opacity） —— */
function makeSmokeTC(o){
  o=o||{};
  const n=o.n===undefined?11:o.n, sp=o.spread===undefined?[150,14,40]:o.spread;
  const pos=o.pos===undefined?[0,5,-8]:o.pos, sc=o.scale===undefined?26:o.scale;
  const col=o.color===undefined?0xa8bccc:o.color, op=o.op===undefined?0.11:o.op;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:col,transparent:true,opacity:op*(0.6+Math.random()*0.6),
      depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set(pos[0]+(Math.random()-0.5)*sp[0], pos[1]+(Math.random()-0.5)*sp[1], pos[2]+(Math.random()-0.5)*sp[2]);
    const k=sc*(0.7+Math.random()*0.85);
    s.scale.set(k,k*0.55,1); s.renderOrder=5;
    g.add(s); items.push({s:s,base:[k,k*0.55],ph:Math.random()*6.283});
  }
  return {g,items,update:function(t,k,grow){
    const kk=k===undefined?1:k, gr=grow===undefined?1:grow;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const s=1+0.06*Math.sin(t*0.25+it.ph);
      it.s.scale.set(it.base[0]*s*gr, it.base[1]*s*gr, 1);
    }
  }};
}

/* —— 空啼之鸟：一只掠江而过的鸟（合批 1 mesh） —— */
function makeBirdTC(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0x2c3038:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.22,8,6); body.scale(1.7,0.9,0.85); B.put(body,c);
  const head=new THREE.SphereGeometry(0.13,7,6); head.translate(0.36,0.10,0); B.put(head,shadeColor(c,1.2));
  const beak=new THREE.ConeGeometry(0.04,0.16,5); beak.rotateZ(-Math.PI/2); beak.translate(0.50,0.09,0); B.put(beak,0x6a5a3a);
  const w1=new THREE.PlaneGeometry(0.9,0.26); w1.rotateZ(0.25); w1.translate(-0.05,0.16,0.30); B.put(w1,shadeColor(c,1.1));
  const w2=new THREE.PlaneGeometry(0.9,0.26); w2.rotateZ(-0.25); w2.translate(-0.05,0.16,-0.30); B.put(w2,shadeColor(c,1.1));
  const tail=new THREE.ConeGeometry(0.10,0.42,5); tail.rotateZ(1.35); tail.translate(-0.42,0.06,0); B.put(tail,c);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    emissive:0x06080c,side:THREE.DoubleSide}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const ph=seedRnd(o.seed===undefined?61:o.seed)()*6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.10*Math.sin(t*3.1+ph)*kk;
    g.position.y=(o.y===undefined?0:o.y)+0.35*Math.sin(t*0.6+ph);
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 台城烟雨 —— 江雨迷蒙，远岸台城柳堤一线
  const g=new THREE.Group();
  const grd=makeGround({r:280,c1:0x0c1014,c2:0x18202a,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:34,layers:3,peaks:5,seed:311,color:0x0d1218,atmo:0x2c3a48,
    fogK:0.62,glowK:0.05,glow:0x9fb3c9,y:-9});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const water=makeWater({size:150,seg:44,amp:0.13,freq:0.11,speed:0.5,flow:[0.2,0.6],spec:1.1,
    deep:0x0a141c,shallow:0x1d3242,skyc:0x31485c,moonDir:[-40,90,-160],y:-1.1});
  water.mesh.position.set(0,-1.1,-30); g.add(water.mesh);
  const bank=makeGrassTC({n:900,w:230,d:24,color:0x4a6636,seed:29}); bank.g.position.set(0,-1.2,-8); g.add(bank.g);
  const pier=makePierTC({len:170,d:8,x:0,y:-1.2,z:-40}); g.add(pier.g);
  const ruins=makeRuinTC({x:-6,y:-1.0,z:-58,seed:47}); g.add(ruins.g);
  const willows=[];
  [[-24,0.0,-40],[-8,0.0,-41],[10,0.0,-40],[27,0.0,-41]].forEach(function(p,i){
    const w=makeWillowTC({h:6.2,seed:81+i*7,scale:0.95}); w.g.position.set(p[0],-1.2,p[2]); g.add(w.g); willows.push(w);
  });
  const rainFar=makeRainTC({n:340,box:[200,26,100],pos:[0,1,-28],size:4.2,maxA:0.16});
  const rainNear=makeRainTC({n:140,box:[60,16,26],pos:[2,1,6],size:5.0,maxA:0.20,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const smoke=makeSmokeTC({n:12,spread:[180,16,60],pos:[0,6,-26],scale:30,op:0.12}); g.add(smoke.g);
  const motes=makeGlow({n:40,box:[180,24,90],pos:[0,7,-20],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const fg=makeForeground({kind:'芦苇',w:24,n:12,d:6,color:0x0a1014,seed:19,sway:1.0,tip:0x3a4a34});
  fg.g.position.set(-16,-1.2,34); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x090d10,seed:21,rim:0.14,rimC:0x9fb3c9});
  fg2.g.position.set(15,-1.1,20); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-40,70,30]},{c:0x1a2430,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); smoke.update(t,k,1); motes.update(t);
    bank.update(t,k); ruins.mat.opacity=k*0.42; rainFar.update(t); rainNear.update(t);
    for(let i=0;i<willows.length;i++)willows[i].update(t,k);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bJiangyu(){ // 一 · 江雨空啼 —— 江雨霏霏江草齐，六朝如梦鸟空啼
  const g=new THREE.Group();
  const grd=makeGround({r:270,c1:0x0b0f13,c2:0x171f28,y:-0.5}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:36,layers:3,peaks:5,seed:321,color:0x0c1116,atmo:0x2a3846,
    fogK:0.62,glowK:0.05,glow:0x9fb3c9,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 江面在岸外：近缘退到 z=-23，近岸才是岸 */
  const water=makeWater({size:170,seg:46,amp:0.14,freq:0.10,speed:0.55,flow:[0.25,0.7],spec:1.15,
    deep:0x0a141c,shallow:0x20384a,skyc:0x354c60,moonDir:[-30,90,-150],y:-0.1});
  water.mesh.scale.set(1,1,0.5);
  water.mesh.position.set(0,-0.1,-66); g.add(water.mesh);
  /* 江草齐：近岸一大片齐整青草（本境最亮的生机色） */
  const bank=makeGrassTC({n:1300,w:250,d:26,color:0x557040,seed:37}); bank.g.position.set(0,-0.5,-6); g.add(bank.g);
  /* 六朝如梦：近岸烟雨里的宫阙残影（江草之后、长堤之前） */
  const ruins=makeRuinTC({x:-4,y:-0.45,z:-16,seed:51}); g.add(ruins.g);
  const pier=makePierTC({len:180,d:9,x:0,y:-0.2,z:-30}); g.add(pier.g);
  const willows=[];
  [[-30,0,-31],[-14,0,-32],[6,0,-31],[22,0,-32],[36,0,-31]].forEach(function(p,i){
    const w=makeWillowTC({h:6.0,seed:101+i*9,scale:0.9}); w.g.position.set(p[0],-0.2,p[2]); g.add(w.g); willows.push(w);
  });
  /* 鸟空啼：两只掠过江面的鸟 */
  const b1=makeBirdTC({scale:1.15,seed:61,y:7.5}); b1.g.position.set(-16,7.5,2); g.add(b1.g);
  const b2=makeBirdTC({scale:0.95,seed:67,y:8.4}); b2.g.position.set(6,8.4,-8); g.add(b2.g);
  const rainFar=makeRainTC({n:360,box:[210,26,100],pos:[0,1,-30],size:4.3,maxA:0.17});
  const rainNear=makeRainTC({n:150,box:[56,16,24],pos:[1,1,7],size:5.0,maxA:0.21,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const smoke=makeSmokeTC({n:11,spread:[190,16,60],pos:[0,6,-30],scale:32,op:0.12}); g.add(smoke.g);
  const motes=makeGlow({n:42,box:[180,24,90],pos:[0,7,-22],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const crowd=makeCrowd({n:2,rect:[-30,-18,16,6],seed:71,color:0x121a20,rimC:0x9fb3c9,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'芦苇',w:26,n:13,d:6,color:0x0a1014,seed:23,sway:1.1,tip:0x3f5236});
  fg.g.position.set(-14,-0.5,30); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.2,w:15,d:6,color:0x090d10,seed:25,rim:0.14,rimC:0x9fb3c9});
  fg2.g.position.set(14,-0.5,18); g.add(fg2.g);
  addLights(g,{c:0xa4b8c8,i:0.44,p:[-36,70,26]},{c:0x1a2430,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); smoke.update(t,k,1); motes.update(t);
      bank.update(t,k); ruins.mat.opacity=k*0.40; crowd.update(t);
      rainFar.update(t); rainNear.update(t);
      for(let i=0;i<willows.length;i++)willows[i].update(t,k);
      b1.update(t,k); b2.update(t,k);
      b1.g.position.x=-16+4.5*Math.sin(t*0.16); b1.g.position.z=2-2.0*Math.cos(t*0.16);
      b2.g.position.x=6+3.6*Math.sin(t*0.14+1.2); b2.g.position.z=-8-1.6*Math.cos(t*0.14+1.2);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.3,0.09); pluck(3,0.9,0.08); }};
}
function bYanlong(){ // 二（末境·可点击）· 烟笼十里 —— 无情最是台城柳，依旧烟笼十里堤
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,smoke:0};
  const grd=makeGround({r:270,c1:0x0b0f13,c2:0x171f28,y:-0.8}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:32,layers:2,peaks:5,seed:331,color:0x0b1015,atmo:0x283644,
    fogK:0.60,glowK:0.05,glow:0x9ab0c6,y:-8});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  /* 长堤横贯画面（柳堤） */
  const pier=makePierTC({len:190,d:11,x:0,y:-0.8,z:-6}); g.add(pier.g);
  /* 堤上垂柳成行 —— 「台城柳」 */
  const willows=[];
  for(let i=0;i<9;i++){
    const w=makeWillowTC({h:6.6+(i%3)*0.5,seed:141+i*13,scale:1.0,sway:0.06});
    w.g.position.set(-40+i*10.5,-0.8,-4.5+((i%2)?1.6:-1.0)); g.add(w.g); willows.push(w);
  }
  /* 六朝残影：堤外烟雨里的宫阙断壁（点击后如梦散去） */
  const ruins=makeRuinTC({x:-2,y:-0.6,z:-34,seed:57}); g.add(ruins.g);
  /* 江面在堤外 */
  const water=makeWater({size:150,seg:40,amp:0.12,freq:0.10,speed:0.5,flow:[0.2,0.6],spec:1.1,
    deep:0x0a141c,shallow:0x1e3444,skyc:0x33495d,moonDir:[-30,90,-150],y:-0.3});
  water.mesh.scale.set(1,1,0.5);
  water.mesh.position.set(0,-0.3,-89); g.add(water.mesh);
  /* 柳烟：薄烟常在，点击后漫堤 */
  const smoke=makeSmokeTC({n:12,spread:[170,14,50],pos:[0,5,-10],scale:30,op:0.13}); g.add(smoke.g);
  const rainFar=makeRainTC({n:320,box:[200,26,96],pos:[0,1,-28],size:4.2,maxA:0.16});
  const rainNear=makeRainTC({n:130,box:[54,15,24],pos:[2,1,6],size:5.0,maxA:0.20,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const motes=makeGlow({n:38,box:[170,22,86],pos:[0,7,-18],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  /* 堤上凭吊的诗人：独立于柳下 */
  const poet=makeFigure({pose:'独立',robe:0x2e3a44,belt:0x8a9ab0,collar:0xd8e2ea,hat:'幞头',
    hair:0x14181e,scale:1.1,rim:0.5,rimC:0xa8c0d8,noProp:true});
  poet.position.set(-3.4,-0.6,0.6); poet.rotation.y=2.5; g.add(poet);
  const crowd=makeCrowd({n:2,rect:[-42,-30,12,6],seed:77,color:0x121a20,rimC:0x9fb3c9,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'芦苇',w:22,n:11,d:5,color:0x0a1014,seed:27,sway:1.0,tip:0x3f5236});
  fg.g.position.set(16,-0.9,14); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x090d10,seed:29,rim:0.16,rimC:0x9fb3c9});
  fg2.g.position.set(-15,-0.9,12); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-40,68,26]},{c:0x1a2430,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.smoke=Math.min(1,ctl.smoke+dt/2.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const grow=1+0.85*ctl.smoke+0.25*ctl.pulse;
      ridge.update(t,0); water.update(t); motes.update(t); crowd.update(t);
      smoke.update(t,k,grow);
      ruins.mat.opacity=k*0.40*(1-0.92*ctl.smoke);   /* 六朝残影如梦散去（基座 0.40 = 运行期最大值） */
      rainFar.update(t); rainNear.update(t);
      for(let i=0;i<willows.length;i++)willows[i].update(t,k);
      poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(3,0.00,0.12); pluck(1,0.35,0.10); pluck(4,0.75,0.08);
        const fl=$('#flash'); fl.textContent='烟笼十里堤'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;
    },clicked:false};
  return api;
}
