/* ================= 十一月四日风雨大作·其二 · 三境场景（大漠金戈 · 孤村风雨变体：卷首孤村、僵卧孤村、铁马冰河）
   本诗专属系统「风雨入梦」：现实是孤村风雨（雨丝 + 赭色风尘），梦中是铁马冰河。
   末境点击入梦 → 风雨渐急、冰河亮起、铁骑纵队自远而近漫过孤村、火把次第明灭，题字「铁马冰河入梦来」。
   与同赛道《从军行》（玉门孤城、金甲烽火）、《登飞来峰》（孤峰云海）不同：本页是孤村、冰河与梦中的铁骑。 ================= */

/* —— 孤村茅屋：草顶 + 土墙 + 门窗 + 篱落，合批 1 mesh —— */
function makeCottageFV(o){
  o=o||{};
  const w=o.w===undefined?6.4:o.w, d=o.d===undefined?5:o.d, h=o.h===undefined?2.8:o.h;
  const wall=o.wall===undefined?0x4a3a28:o.wall, thatch=o.thatch===undefined?0x5a4a2c:o.thatch;
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?151:o.seed);
  const bw=new THREE.BoxGeometry(w,h,d); bw.translate(0,h/2,0); B.put(bw,shadeColor(wall,0.9+R()*0.25));
  /* 草顶：两坡 */
  const r1=new THREE.BoxGeometry(w*1.14,0.24,d*0.62); r1.rotateX(0.42); r1.translate(0,h+0.42,d*0.26);
  B.put(r1,shadeColor(thatch,0.9+R()*0.2));
  const r2=new THREE.BoxGeometry(w*1.14,0.24,d*0.62); r2.rotateX(-0.42); r2.translate(0,h+0.42,-d*0.26);
  B.put(r2,shadeColor(thatch,1.0+R()*0.2));
  /* 门窗（暗） */
  const dr=new THREE.BoxGeometry(1.1,1.9,0.2); dr.translate(-w*0.18,h*0.5,d/2+0.02); B.put(dr,0x120e08);
  const wn=new THREE.BoxGeometry(1.5,1.1,0.2); wn.translate(w*0.22,h*0.62,d/2+0.02); B.put(wn,0x1a1410);
  const wn2=new THREE.BoxGeometry(0.2,1.1,1.5); wn2.translate(w/2+0.02,h*0.62,0); B.put(wn2,0x1a1410);
  /* 篱落 */
  for(let i=0;i<7;i++){
    const x=-w*0.9+w*0.3*i;
    const p=new THREE.CylinderGeometry(0.07,0.09,1.2,5); p.rotateZ((R()-0.5)*0.2);
    p.translate(x,0.6,d*0.5+1.3); B.put(p,shadeColor(0x3a3020,0.8+R()*0.4));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a3020,emissive:0x0a0806}),{c:o.rimC===undefined?0xc09060:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mesh};
}

/* —— 枯树：冬日无叶的老树（合批 1 mesh） —— */
function makeBareTreeFV(o){
  o=o||{};
  const h=o.h===undefined?4.2:o.h, R=seedRnd(o.seed===undefined?157:o.seed);
  const wood=o.wood===undefined?0x241c14:o.wood, B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.5,0],h*0.06,h*0.02,6),wood);
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.6, len=h*(0.3+R()*0.3);
    const p1=[Math.sin(a)*len,h*0.5+len*0.5,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.48,0],p1,h*0.022,h*0.008,5),shadeColor(wood,1.2));
    if(R()<0.7){
      const p2=[p1[0]*1.3,p1[1]+len*0.36,p1[2]*1.3];
      B.put(limbGeo(p1,p2,h*0.01,h*0.004,4),shadeColor(wood,1.35));
    }
  }
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a3028,emissive:0x080604}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k; g.rotation.z=0.02*Math.sin(t*0.8+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 风雨：夜雨丝（Points）+ 横流风尘（复用引擎 makeFlow 赭色），可随"入梦"加剧 —— */
const FV_RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB; uniform float uSway;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uFall*(0.8+aSeed*0.6);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.5+aSeed*37.0)*uSway;
  vA=smoothstep(0.0,uH*0.06,y)*(1.0-smoothstep(uH*0.9,uH,y));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(170.0/max(1.0,-mv.z)),24.0);
  gl_Position=projectionMatrix*mv;
}`;
const FV_RAIN_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA; uniform float uK;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.14,0.03,abs(q.x))*smoothstep(0.5,0.05,abs(q.y))*vA*uFade*uMaxA*uK;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeRainFV(o){
  o=o||{};
  const d=Object.assign({n:360,box:[180,26,92],pos:[0,1,-26],fall:0.10,sway:0.4,
    size:4.5,maxA:0.22,c:0xa8b0b8},o);
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
      uSway:{value:d.sway},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA},uK:{value:1}},
    vertexShader:FV_RAIN_VERT,fragmentShader:FV_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update:function(t,k){ m.uniforms.uTime.value=t; m.uniforms.uK.value=k===undefined?1:k; }};
}

/* —— 冰河：横过画面的一条冰封大河（冰面 + 冰裂纹 + 冰凌），合批 1 mesh —— */
function makeIceRiverFV(o){
  o=o||{};
  const w=o.w===undefined?150:o.w, d=o.d===undefined?26:o.d, R=seedRnd(o.seed===undefined?163:o.seed);
  const B=new GeoBag();
  const ice=new THREE.BoxGeometry(w,0.5,d); ice.translate(0,0.25,0); B.put(ice,0x8fa6b8);
  for(let i=0;i<26;i++){       /* 冰裂纹 */
    const cr=new THREE.BoxGeometry(2.4+R()*7,0.06,0.16); cr.rotateY((R()-0.5)*0.7);
    cr.translate((R()-0.5)*w,0.52,(R()-0.5)*d*0.9); B.put(cr,0xb8ccd8);
  }
  for(let i=0;i<22;i++){       /* 冰凌/冰堆 */
    const bl=new THREE.ConeGeometry(0.5+R()*0.9,0.9+R()*1.7,5); bl.rotateY(R()*6.283);
    bl.translate((R()-0.5)*w,0.5+0.4,(R()-0.5)*d*0.8); B.put(bl,shadeColor(0xa8c0d0,0.85+R()*0.35));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:60,
    specular:0xd8e8f4,emissive:0x141e28}),{c:o.rimC===undefined?0xbfd8e8:o.rimC,i:0.34,p:2.6}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 冰河冷光（只调 scale，不写 opacity） */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9fc4e0,transparent:true,
    opacity:0.26,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(w*0.5,10,1); glow.position.set(0,1.4,0); glow.renderOrder=3; g.add(glow);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,glow,mesh,update:function(t,lit){
    const li=lit===undefined?0:lit;
    const s=(0.35+0.85*li)*(0.95+0.05*Math.sin(t*0.6));
    glow.scale.set(w*0.5*s,10*s*0.9,1);
  }};
}

/* —— 铁骑：披甲战马 + 甲士 + 火把（一只；成列由 stage 摆多只），合批 1 mesh + 火把 sprite —— */
function makeIronRiderFV(o){
  o=o||{};
  const coat=o.coat===undefined?0x2a2c34:o.coat, B=new GeoBag();
  const body=new THREE.SphereGeometry(0.58,9,7); body.scale(1.7,0.95,0.95); body.translate(0,1.22,0); B.put(body,coat);
  const neck=new THREE.CylinderGeometry(0.17,0.27,0.78,7); neck.rotateZ(-0.6); neck.translate(1.02,1.68,0); B.put(neck,coat);
  const head=new THREE.SphereGeometry(0.19,7,6); head.scale(1.5,0.9,0.8); head.translate(1.44,1.94,0); B.put(head,shadeColor(coat,1.2));
  const chanfron=new THREE.BoxGeometry(0.34,0.30,0.36); chanfron.translate(1.30,2.02,0); B.put(chanfron,0x6a6e78);
  const tail=new THREE.ConeGeometry(0.13,0.66,6); tail.rotateZ(-1.05); tail.translate(-1.18,1.26,0); B.put(tail,0x1a1a1e);
  [[0.58,0.24],[-0.58,-0.24]].forEach(function(lg){
    [1,-1].forEach(function(sd){
      const up=new THREE.CylinderGeometry(0.1,0.08,0.68,6); up.translate(lg[0],0.80,0.16*sd); B.put(up,shadeColor(coat,1.05));
      const lo=new THREE.CylinderGeometry(0.07,0.06,0.6,6); lo.translate(lg[0]+lg[1],0.32,0.16*sd); B.put(lo,shadeColor(coat,0.8));
    });
  });
  /* 甲士：头盔 + 甲身 + 长戟 */
  const torso=new THREE.CylinderGeometry(0.24,0.32,0.86,8); torso.translate(-0.05,2.02,0); B.put(torso,0x4a4e58);
  const helm=new THREE.SphereGeometry(0.19,8,6); helm.scale(1.05,0.95,1.05); helm.translate(-0.05,2.62,0); B.put(helm,0x6a6e78);
  const plume=new THREE.ConeGeometry(0.05,0.28,5); plume.translate(-0.05,2.86,0); B.put(plume,0x8a2a22);
  const spear=new THREE.CylinderGeometry(0.035,0.035,2.6,5); spear.rotateZ(0.24); spear.translate(0.42,2.0,0.06); B.put(spear,0x4a3a28);
  const tip=new THREE.ConeGeometry(0.09,0.34,5); tip.translate(0.70,3.28,0.06); B.put(tip,0xa8b0b8);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x8a94a4,emissive:0x0a0c12}),{c:o.rimC===undefined?0xc8d8e8:o.rimC,i:0.42,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const torch=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,transparent:true,
    opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  torch.position.set(0.95,2.35,0.1); torch.scale.set(2.0,2.0,1); torch.renderOrder=3; g.add(torch);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=seedRnd(o.seed===undefined?173:o.seed)()*6.283;
  g.update=function(t,k,run){
    const kk=k===undefined?1:k, rn=run===undefined?0:run;
    const f=0.92+0.16*Math.sin(t*7.4*Math.max(0.4,rn)+ph);
    torch.scale.set(2.0*f,2.0*f,1);
    g.rotation.z=0.03*Math.sin(t*1.4+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,torch};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 孤村夜雨 —— 风雨孤村、枯树篱落，远处一线冰河冷光
  const g=new THREE.Group(); const R=seedRnd(1401);
  const grd=makeGround({r:260,c1:0x100b07,c2:0x20160e,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:46,layers:3,peaks:5,seed:1411,color:0x160e07,atmo:0x40301a,
    fogK:0.62,glowK:0.07,glow:0xc09060,y:-12});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const ice=makeIceRiverFV({w:150,d:24,x:0,y:-1.2,z:-52,seed:167}); g.add(ice.g);
  const c1=makeCottageFV({w:6.4,d:5,h:2.8,scale:1.0,seed:153}); c1.g.position.set(-8,-1.4,-14); g.add(c1.g);
  const c2=makeCottageFV({w:5.4,d:4.4,h:2.5,scale:0.92,seed:159}); c2.g.position.set(1,-1.4,-18); g.add(c2.g);
  const c3=makeCottageFV({w:5.0,d:4.0,h:2.3,scale:0.86,seed:161}); c3.g.position.set(9.5,-1.4,-13); g.add(c3.g);
  const trees=[];
  [[-17,0,-22],[-13,0,-8],[13,0,-20],[17,0,-10]].forEach(function(p,i){
    const t=makeBareTreeFV({h:4.0+R()*0.8,seed:181+i*13,scale:1.0}); t.g.position.set(p[0],-1.4,p[2]); g.add(t.g); trees.push(t);
  });
  const rainFar=makeRainFV({n:360,box:[200,26,100],pos:[0,1,-30],size:4.4,maxA:0.19});
  const rainNear=makeRainFV({n:140,box:[56,15,24],pos:[2,1,6],size:5.0,maxA:0.22,c:0xbfc8d0});
  g.add(rainFar.points,rainNear.points);
  const dust=makeFlow({n:260,box:[190,20,100],pos:[0,6,-30],color:0x8a5a34,size:14,speed:3.2,maxA:0.20});
  g.add(dust.points);
  const motes=makeGlow({n:44,box:[190,26,90],pos:[0,9,-28],color:0xd0a878,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,28,120],pos:[0,8,-56],scale:78,color:0x2c1e10,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:19,d:7,color:0x090604,seed:41,rim:0.16,rimC:0xb0906a});
  fg.g.position.set(-17,-1.6,36); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:6,color:0x070503,seed:43,rim:0.14,rimC:0x9a7a58});
  fg2.g.position.set(16,-1.4,24); g.add(fg2.g);
  addLights(g,{c:0xc8a070,i:0.44,p:[-48,76,28]},{c:0x261a0e,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); dust.update(t);
    rainFar.update(t,1); rainNear.update(t,1);
    ice.update(t,0.15);
    for(let i=0;i<trees.length;i++)trees[i].update(t,k);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bJiangwo(){ // 一 · 僵卧孤村 —— 僵卧孤村不自哀，尚思为国戍轮台
  const g=new THREE.Group(); const R=seedRnd(1402);
  const grd=makeGround({r:250,c1:0x0f0a06,c2:0x1e140d,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:48,layers:3,peaks:5,seed:1421,color:0x150d07,atmo:0x3e2e18,
    fogK:0.62,glowK:0.07,glow:0xc09060,y:-12});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  /* 孤村：三间茅屋 + 篱落 */
  const c1=makeCottageFV({w:7.0,d:5.4,h:3.0,scale:1.1,seed:191}); c1.g.position.set(-3.5,-1.3,-12); g.add(c1.g);
  const c2=makeCottageFV({w:5.6,d:4.6,h:2.6,scale:0.95,seed:193}); c2.g.position.set(5.5,-1.3,-16); g.add(c2.g);
  const c3=makeCottageFV({w:5.0,d:4.0,h:2.3,scale:0.85,seed:197}); c3.g.position.set(-12,-1.3,-17); g.add(c3.g);
  const trees=[];
  [[-19,0,-12],[-9,0,-6],[12,0,-9],[19,0,-18]].forEach(function(p,i){
    const t=makeBareTreeFV({h:4.2+R()*0.9,seed:199+i*11,scale:1.0}); t.g.position.set(p[0],-1.3,p[2]); g.add(t.g); trees.push(t);
  });
  /* 屋内僵卧的诗人：借窗内一点暗影（不画细部，只给一盏昏灯与窗） */
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb060,transparent:true,
    opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.position.set(-3.2,0.9,-9.2); lamp.scale.set(3.0,2.4,1); lamp.renderOrder=3; g.add(lamp);
  /* 轮台方向：西北远山一线微光 */
  const north=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc8a878,transparent:true,
    opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  north.position.set(-70,14,-160); north.scale.set(120,30,1); north.renderOrder=-7; g.add(north);
  const rainFar=makeRainFV({n:340,box:[200,26,98],pos:[0,1,-28],size:4.3,maxA:0.18});
  const rainNear=makeRainFV({n:130,box:[54,15,24],pos:[2,1,6],size:4.9,maxA:0.21,c:0xbfc8d0});
  g.add(rainFar.points,rainNear.points);
  const dust=makeFlow({n:220,box:[180,18,92],pos:[0,6,-26],color:0x8a5a34,size:13,speed:3.0,maxA:0.18});
  g.add(dust.points);
  const motes=makeGlow({n:40,box:[180,24,86],pos:[0,9,-24],color:0xd0a878,size:7,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,26,110],pos:[0,8,-52],scale:76,color:0x2c1e10,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.4,w:18,d:7,color:0x090604,seed:45,rim:0.16,rimC:0xb0906a});
  fg.g.position.set(-15,-1.5,18); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x080604,seed:47,sway:1.0,tip:0x4a3a1e});
  fg2.g.position.set(15,-1.4,16); g.add(fg2.g);
  addLights(g,{c:0xc8a070,i:0.44,p:[-46,74,26]},{c:0x261a0e,i:0.60});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); dust.update(t);
      rainFar.update(t,1); rainNear.update(t,1);
      lamp.scale.set(3.0*(0.94+0.06*Math.sin(t*3.0)),2.4,1);
      for(let i=0;i<trees.length;i++)trees[i].update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(1,0.35,0.08); }};
}
function bTiemai(){ // 二（末境·可点击）· 铁马冰河 —— 夜阑卧听风吹雨，铁马冰河入梦来
  const g=new THREE.Group(); const R=seedRnd(1403);
  const ctl={t:0,clicked:false,pulse:0,dream:0};
  const grd=makeGround({r:250,c1:0x0f0a06,c2:0x1e140d,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:46,layers:2,peaks:5,seed:1431,color:0x140d07,atmo:0x3c2c16,
    fogK:0.60,glowK:0.07,glow:0xba8c5c,y:-12});
  ridge.g.position.set(0,0,-106); g.add(ridge.g);
  /* 冰河横过画面（梦中战场） */
  const ice=makeIceRiverFV({w:160,d:30,x:0,y:-1.2,z:-34,seed:169}); g.add(ice.g);
  /* 孤村（现实一角，仍在画面近处） */
  const c1=makeCottageFV({w:6.4,d:5.0,h:2.8,scale:1.0,seed:201}); c1.g.position.set(-10,-1.3,-10); g.add(c1.g);
  const c2=makeCottageFV({w:5.2,d:4.2,h:2.4,scale:0.9,seed:203}); c2.g.position.set(-16,-1.3,-15); g.add(c2.g);
  /* 铁骑纵队（梦中由远而近；点击后开始奔袭） */
  const riders=[];
  for(let i=0;i<6;i++){
    const r=makeIronRiderFV({scale:1.05,seed:211+i*7});
    r.g.position.set(-46+i*9.0,-1.2,-40+i*3.2);
    r.g.rotation.y=0.28; g.add(r.g); riders.push(r);
  }
  const trees=[];
  [[16,0,-8],[21,0,-16],[-22,0,-20]].forEach(function(p,i){
    const t=makeBareTreeFV({h:4.0+R()*0.8,seed:223+i*7,scale:1.0}); t.g.position.set(p[0],-1.3,p[2]); g.add(t.g); trees.push(t);
  });
  /* 梦境光晕（点击后漫开） */
  const dreamGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8fb8d8,transparent:true,
    opacity:0.18,depthWrite:false,blending:THREE.AdditiveBlending}));
  dreamGlow.position.set(0,8,-30); dreamGlow.scale.set(120,50,1); dreamGlow.renderOrder=4; g.add(dreamGlow);
  const rainFar=makeRainFV({n:380,box:[200,26,100],pos:[0,1,-30],size:4.5,maxA:0.20});
  const rainNear=makeRainFV({n:150,box:[56,15,24],pos:[2,1,6],size:5.1,maxA:0.24,c:0xbfc8d0});
  g.add(rainFar.points,rainNear.points);
  const dust=makeFlow({n:280,box:[190,20,100],pos:[0,6,-28],color:0x9a6038,size:15,speed:3.6,maxA:0.22});
  g.add(dust.points);
  const motes=makeGlow({n:42,box:[180,24,88],pos:[0,9,-26],color:0xd0a878,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,26,110],pos:[0,8,-54],scale:78,color:0x2c1e10,op:0.12});
  g.add(mist.g);
  const crowd=makeCrowd({n:3,rect:[-40,-60,16,8],seed:227,color:0x1a1208,rimC:0xc09060,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.4,w:18,d:7,color:0x090604,seed:49,rim:0.16,rimC:0xb0906a});
  fg.g.position.set(-16,-1.5,14); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x070503,seed:51,rim:0.14,rimC:0x9a7a58});
  fg2.g.position.set(15,-1.4,12); g.add(fg2.g);
  addLights(g,{c:0xc8a070,i:0.44,p:[-46,74,26]},{c:0x261a0e,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.dream=Math.min(1,ctl.dream+dt/2.2);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const dr=ctl.dream+0.5*ctl.pulse;
      const wave=1+0.35*dr;
      ridge.update(t,0); mist.update(t,k); motes.update(t); dust.update(t); crowd.update(t);
      rainFar.update(t,wave); rainNear.update(t,wave*1.05);
      ice.update(t,0.2+0.9*dr);
      dreamGlow.scale.set(120*(0.6+0.6*dr),50*(0.6+0.6*dr),1);
      /* 铁骑：按 dream 的进度自远而近漫过孤村（只动位置/朝向） */
      for(let i=0;i<riders.length;i++){
        const r=riders[i];
        const lead=i*0.08;
        const u=Math.max(0,Math.min(1,dr*1.2-lead));
        r.g.position.set(-46+u*52+i*1.2,-1.2,-40+u*26+i*2.2);
        r.g.update(t,k,u);
      }
      for(let i=0;i<trees.length;i++)trees[i].update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.00,0.15); pluck(2,0.22,0.13); pluck(4,0.48,0.11); pluck(5,0.78,0.09);
        const fl=$('#flash'); fl.textContent='铁马冰河入梦来'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：风雨再急一分，铁骑再近一程 */
    },clicked:false};
  return api;
}
