/* ================= 浣溪沙·游蕲水清泉寺 · 三境场景（青绿春晓·蕲水溪山变体：卷首溪山、兰芽浸溪、流水能西）
   本诗专属系统「一溪向西」：寺门前一溪与众水同向东流，白发意象随水东漂；
   末境点击——溪水反向西去（词眼「门前流水尚能西」），白发随西水消散，西天渐亮 ================= */

/* —— 潇潇暮雨：细雨丝（Points 自定义着色器，点内画细长雨丝，快速下落） —— */
const HXS_RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB; uniform float uSway;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uFall*(0.8+aSeed*0.45);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*2.2+aSeed*51.0)*uSway;
  vA=smoothstep(0.0,uH*0.06,y)*(1.0-smoothstep(uH*0.93,uH,y));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(160.0/max(1.0,-mv.z)),24.0);
  gl_Position=projectionMatrix*mv;
}`;
const HXS_RAIN_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.14,0.04,abs(q.x))*smoothstep(0.5,0.06,abs(q.y))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeRainHXS(o){
  const d=Object.assign({n:300,box:[150,28,80],pos:[0,1,-20],fall:0.085,sway:0.4,
    size:5,maxA:0.24,c:0x9cb8a6},o);
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
    vertexShader:HXS_RAIN_VERT,fragmentShader:HXS_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 溪沫浮瓣：随流向漂移的白色泡沫与兰芽碎瓣（InstancedMesh，1 draw call，方向可控 → 「反向西去」的主角） —— */
function makeWestFoam(o){
  o=o||{};
  const n=o.n===undefined?26:o.n, R=seedRnd(o.seed===undefined?51:o.seed);
  const geo=new THREE.SphereGeometry(0.26,7,5); geo.scale(1.5,0.4,1.0);
  const mat=new THREE.MeshPhongMaterial({color:o.color===undefined?0xcfe4d4:o.color,
    shininess:30,specular:0xbfe0cc,emissive:0x0e1a12,transparent:true,opacity:0.85});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({x:(R()-0.5)*92,z:(R()-0.5)*(o.w===undefined?5.6:o.w),
      s:0.5+R()*0.9,ph:R()*6.283,sp:0.7+R()*0.7});
  }
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.y=o.y===undefined?0.34:o.y;
  return {g,update:function(t,dir,spd){
    for(let i=0;i<n;i++){
      const it=items[i];
      it.x+=(dir===undefined?1:dir)*(spd===undefined?2.2:spd)*it.sp;
      if(it.x>47)it.x-=94; if(it.x<-47)it.x+=94;
      dm.position.set(it.x,0.10*Math.sin(t*2.1+it.ph),it.z+Math.sin(t*1.3+it.ph)*0.4);
      dm.scale.setScalar(it.s);
      dm.rotation.y=it.ph+t*0.4;
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* —— 松：主干+层层塔冠（可带一根横枝站子规），合批 1 mesh —— */
function makePineHXS(o){
  o=o||{};
  const h=o.h===undefined?10:o.h, R=seedRnd(o.seed===undefined?5:o.seed);
  const trunkC=o.trunk===undefined?0x1a1410:o.trunk, leaf=o.leaf===undefined?0x14301c:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.6-0.3,h*0.55,0],h*0.045,h*0.02,7),trunkC);
  const nl=o.tiers===undefined?4:o.tiers;
  for(let i=0;i<nl;i++){
    const f=i/nl, r=h*(0.30-0.20*f)*(0.9+R()*0.25), y=h*(0.42+0.52*f);
    const cone=new THREE.ConeGeometry(r,h*(0.32-0.05*f),8);
    cone.translate((R()-0.5)*0.3,y,0); B.put(cone,shadeColor(leaf,0.8+0.35*f+R()*0.2));
  }
  if(o.branch){
    const br=limbGeo([0,h*0.55,0],[o.branch[0],o.branch[1],o.branch[2]],h*0.018,h*0.008,6);
    B.put(br,trunkC);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x24352a,emissive:0x060c08}),{c:o.rimC===undefined?0x8fc4a8:o.rimC,i:o.rim===undefined?0.18:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 子规（杜鹃）：枝头啼鸟，鸣时挺颈（合批 1 mesh） —— */
function makeCuckooHXS(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0x232c26:o.color;
  const g=new THREE.Group();
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,8,6); body.scale(1.5,0.9,0.85); body.translate(0,0.30,0); B.put(body,c);
  const head=new THREE.SphereGeometry(0.17,8,6); head.translate(0.42,0.55,0); B.put(head,shadeColor(c,1.15));
  const beak=new THREE.ConeGeometry(0.05,0.22,5); beak.rotateZ(-Math.PI/2); beak.translate(0.62,0.53,0); B.put(beak,0x6a5638);
  const tail=new THREE.ConeGeometry(0.10,0.55,5); tail.rotateZ(Math.PI/2.4); tail.translate(-0.48,0.36,0); B.put(tail,c);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,emissive:0x050806}));
  g.add(mesh);
  g.scale.setScalar(s);
  g.update=function(t,fk){
    g.rotation.z=0.05*Math.sin(t*0.9);
    const k=fk===undefined?1:fk;
    g.scale.set(s,s*(1+0.06*Math.max(0,Math.sin(t*0.9))*k),s);   // 啼鸣时挺颈（乘 fadeK）
  };
  return {g,update:g.update};
}

/* —— 兰芽短浸溪：溪畔水边一排嫩绿新芽（细芽尖+初生小叶，嫩绿是全页最亮的生机色） —— */
function makeLanyaHXS(o){
  o=o||{};
  const n=o.n===undefined?14:o.n, w=o.w===undefined?24:o.w, R=seedRnd(o.seed===undefined?23:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*2.0, h=0.5+R()*0.9;
    const shoot=new THREE.ConeGeometry(0.075,h,5);
    shoot.rotateZ((R()-0.5)*0.24); shoot.translate(x,h*0.5,z);
    B.put(shoot,shadeColor(0x9fce8f,0.85+R()*0.5));
    if(R()<0.7){
      const lf=new THREE.PlaneGeometry(0.55,0.16);
      lf.rotateZ(0.5+R()*0.5); lf.rotateY(R()*0.8); lf.translate(x+0.16,h*0.62,z);
      B.put(lf,shadeColor(0xbcd89a,0.8+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x3a5a3a,emissive:0x0a160c,side:THREE.DoubleSide}),{c:0xc0e0a8,i:0.34,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 清泉寺门：双柱+门楣+四棱顶+匾额（门前流水之「门前」，合批 1+1 mesh） —— */
function makeGateHXS(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, h=o.h===undefined?5.2:o.h;
  const wood=o.wood===undefined?0x241a12:o.wood, roofC=o.roof===undefined?0x1c1c18:o.roof;
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const pl=new THREE.CylinderGeometry(0.22,0.26,h,8); pl.translate(s*w/2,h/2,0); B.put(pl,shadeColor(wood,1.0));
    const bs=new THREE.BoxGeometry(0.9,0.5,0.9); bs.translate(s*w/2,0.25,0); B.put(bs,shadeColor(0x4c4c46,0.9));
  });
  const beam=new THREE.BoxGeometry(w+1.2,0.42,0.7); beam.translate(0,h,0); B.put(beam,shadeColor(wood,1.2));
  const roof=new THREE.ConeGeometry(w*0.78,1.5,4); roof.rotateY(Math.PI/4); roof.translate(0,h+1.05,0); B.put(roof,roofC);
  const plaque=new THREE.BoxGeometry(1.7,0.6,0.10); plaque.translate(0,h-0.9,0.42); B.put(plaque,shadeColor(0x3a3428,1.0));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3a30,emissive:0x0a0806}),{c:o.rimC===undefined?0xc8b478:o.rimC,i:0.30,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  if(o.steps!==false){
    const SB=new GeoBag();
    const st1=new THREE.BoxGeometry(w*1.35,0.34,2.2); st1.translate(0,0.17,1.5); SB.put(st1,shadeColor(0x55554c,0.95));
    const st2=new THREE.BoxGeometry(w*1.15,0.30,1.6); st2.translate(0,0.48,0.9); SB.put(st2,shadeColor(0x606055,0.95));
    const sm=SB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
      {c:0x8fc4a8,i:0.16,p:2.4}));
    g.add(sm);
  }
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 白发意象：一缕浮在溪面的白发（细管波浪线，随流漂移；末境点击后消散） —— */
function makeHairStrandHXS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?41:o.seed), len=o.len===undefined?5:o.len;
  const pts=[];
  for(let i=0;i<=7;i++){
    const u=i/7;
    pts.push(new THREE.Vector3((u-0.5)*len, Math.sin(u*6.3+R()*6.3)*0.35, Math.cos(u*4.2+R()*3.0)*0.5));
  }
  const curve=new THREE.CatmullRomCurve3(pts);
  const geo=new THREE.TubeGeometry(curve,20,0.055,5,false);
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0xdde6dc:o.color,transparent:true,opacity:0.55});
  const mesh=new THREE.Mesh(geo,mat);
  const g=new THREE.Group(); g.add(mesh);
  return {g,mat};
}

function bCover(){ // 卷首 · 蕲水溪山 —— 清泉寺半隐松林，晨光初透，一溪绕山
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0c1710,c2:0x16281a,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:36,layers:3,peaks:5,seed:57,color:0x0c1911,atmo:0x2c4434,fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-80); g.add(ridge.g);
  /* 远景溪涧：一带水光绕山脚 */
  const water=makeWater({size:13,seg:20,amp:0.10,freq:0.16,speed:0.4,flow:[0.15,0.5],spec:1.0,
    deep:0x0a1a14,shallow:0x1c4634,skyc:0x2a5440,moonDir:[-60,90,-160],y:-1.5});
  water.mesh.scale.set(1,1,13); water.mesh.rotation.y=Math.PI/2;
  water.mesh.position.set(8,-1.5,-32); g.add(water.mesh);
  /* 寺门半隐松林 */
  const gate=makeGateHXS({scale:0.9}); gate.g.position.set(-14,-1.6,-46); gate.g.rotation.y=0.5; g.add(gate.g);
  const p1=makePineHXS({h:12,seed:11,scale:1.5}); p1.g.position.set(-24,-1.6,-42); g.add(p1.g);
  const p2=makePineHXS({h:10,seed:13,scale:1.3}); p2.g.position.set(-7,-1.6,-54); g.add(p2.g);
  const p3=makePineHXS({h:13,seed:15,scale:1.6}); p3.g.position.set(22,-1.6,-50); g.add(p3.g);
  /* 寺道上游人一痕 */
  const crowd=makeCrowd({n:4,rect:[0,-38,20,8],seed:67,color:0x131e14,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  /* 晨光熹微：西天一抹暖意（青绿底上唯一的暖，随呼吸微明） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.15,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,60,1); dawn.position.set(-60,26,-120); dawn.renderOrder=-7; g.add(dawn);
  const motes=makeGlow({n:44,box:[190,30,110],pos:[0,9,-26],color:0xcfe0a8,size:7,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[250,34,140],pos:[0,11,-54],scale:80,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:50,n:9,d:7,color:0x081009,seed:19,sway:0.7,rim:0.12,rimC:0x8fc4a8});
  brL.g.position.set(-26,-1.6,42); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const brR=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:21,rim:0.14,rimC:0x8fc4a8});
  brR.g.position.set(16,-1.4,16); g.add(brR.g);
  addLights(g,{c:0xe8d8a8,i:0.46,p:[-50,80,30]},{c:0x22301f,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    brL.update(t,k); brR.update(t,k); crowd.update(t);
    dawn.material.opacity=k*(0.11+0.028*Math.sin(t*0.4));
  }};
}
function bLanya(){ // 一 · 兰芽浸溪 —— 山下兰芽短浸，松间沙路净无泥，潇潇暮雨子规啼
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0a130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:40,layers:3,peaks:5,seed:71,color:0x09150e,atmo:0x29412e,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-6});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  /* 山下溪：斜过画面的溪涧（水面+两岸同组） */
  const stream=new THREE.Group();
  const water=makeWater({size:15,seg:26,amp:0.09,freq:0.18,speed:0.5,flow:[0.1,0.55],spec:1.0,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2a5440,moonDir:[-60,90,-160],y:0.10});
  water.mesh.scale.set(1,1,11); stream.add(water.mesh);
  const bankB=new GeoBag();
  const bl=new THREE.BoxGeometry(6.4,1.0,168); bl.translate(-9.0,0.30,0); bankB.put(bl,shadeColor(0x18271c,1.0));
  const br=new THREE.BoxGeometry(6.4,1.0,168); br.translate(9.0,0.30,0); bankB.put(br,shadeColor(0x1a2a1e,1.0));
  const bankM=bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x8fc4a8,i:0.14,p:2.4}));
  stream.add(bankM);
  stream.rotation.y=0.52; stream.position.set(1,0,-6); g.add(stream);
  /* 兰芽短浸溪：近岸水边嫩芽成排（全页最亮的生机色点） */
  const lanya=makeLanyaHXS({n:16,w:24,seed:23});
  lanya.g.position.set(-4.5,0.62,3.8); lanya.g.rotation.y=0.52; g.add(lanya.g);
  const lanya2=makeLanyaHXS({n:10,w:14,seed:29});
  lanya2.g.position.set(9.5,0.62,-0.5); lanya2.g.rotation.y=0.52; g.add(lanya2.g);
  /* 松间沙路：雨洗白沙，画面里最亮的地物（净无泥） */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.6,0.08,60),
    new THREE.MeshPhongMaterial({color:0x8a8870,shininess:4,emissive:0x14140e}));
  path.rotation.y=0.45; path.position.set(7,0.06,-16); g.add(path);
  /* 松林夹路（左一横枝站子规） */
  const pine1=makePineHXS({h:12,seed:31,branch:[-2.8,6.6,1.2],scale:1.15}); pine1.g.position.set(-10,0,-16); g.add(pine1.g);
  const pine2=makePineHXS({h:10,seed:33,scale:1.0}); pine2.g.position.set(-20,0,-26); g.add(pine2.g);
  const pine3=makePineHXS({h:11,seed:35,scale:1.2}); pine3.g.position.set(17,0,-24); g.add(pine3.g);
  const pine4=makePineHXS({h:8,seed:37,scale:0.85}); pine4.g.position.set(26,0,-13); g.add(pine4.g);
  /* 子规：枝头啼鸣（入境时两声啼） */
  const bird=makeCuckooHXS({scale:1.1});
  bird.g.position.set(-12.6,7.0,-14.9); bird.g.rotation.y=0.7; g.add(bird.g);
  /* 潇潇暮雨：远层密、近层疏 */
  const rainFar=makeRainHXS({n:300,box:[170,28,90],pos:[0,1,-26],fall:0.085,size:4.0,maxA:0.16,c:0x9cb8a6});
  const rainNear=makeRainHXS({n:130,box:[52,18,26],pos:[3,1,4],fall:0.115,size:5.0,maxA:0.22,c:0xb0cabc});
  g.add(rainFar.points,rainNear.points);
  /* 沙路上远游人 */
  const crowd=makeCrowd({n:3,rect:[4,-30,16,8],seed:77,color:0x121c13,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:34,box:[140,22,80],pos:[0,8,-18],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[220,28,120],pos:[0,9,-46],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x070d08,seed:41,rim:0.12,rimC:0x8fc4a8});
  rk.g.position.set(-13,-1.2,13); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:43,sway:1.1,tip:0x2c4028});
  reed.g.position.set(14,-1.0,15); g.add(reed.g);
  addLights(g,{c:0xbccdb4,i:0.42,p:[-40,80,20]},{c:0x1c2a1e,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      rk.update(t,k); reed.update(t,k); crowd.update(t);
      rainFar.update(t); rainNear.update(t);
      bird.update(t,k);
      pine3.g.rotation.z=Math.sin(t*0.4)*0.008;
    },onEnter(){   // 子规啼：枝头两声啼（WebAudio 可用时）
      pluck(4,0.15,0.10); pluck(3,0.55,0.09); pluck(2,1.05,0.08);
    }};
}
function bLiuxi(){ // 二（末境·可点击）· 流水能西 —— 门前流水尚能西；点击：溪水反向西去，白发意象消散
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,west:0,pulse:0};
  const grd=makeGround({r:220,c1:0x0b130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:38,layers:2,peaks:4,seed:81,color:0x091409,atmo:0x27402c,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 门前一溪：东西向横贯（西＝画面左；水面向西去是词眼所系） */
  const stream=new THREE.Group();
  const water=makeWater({size:16,seg:30,amp:0.08,freq:0.16,speed:0.5,flow:[0.12,0.85],spec:1.15,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-70,90,-150],y:0.10});
  water.mesh.scale.set(1,1,10); stream.add(water.mesh);
  const bankB=new GeoBag();
  const bl=new THREE.BoxGeometry(6.0,1.0,180); bl.translate(-8.6,0.30,0); bankB.put(bl,shadeColor(0x18271c,1.0));
  const br=new THREE.BoxGeometry(6.0,1.0,180); br.translate(8.6,0.30,0); bankB.put(br,shadeColor(0x1a2a1e,1.0));
  const bankM=bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0x8fc4a8,i:0.14,p:2.4}));
  stream.add(bankM);
  stream.rotation.y=Math.PI/2; stream.position.set(0,0,-6); g.add(stream);
  /* 溪沫浮瓣：随流向漂移（点击后反向西去、加快——词眼的可见证据） */
  const foam=makeWestFoam({n:26,seed:51});
  foam.g.position.set(0,0.34,-6); g.add(foam.g);
  /* 白发意象：三缕白发浮在溪面随东流漂去（点击后随西水消散） */
  const hairs=[];
  [[-6,0.42,-4.4,4.6,61],[-1,0.40,-7.6,5.4,63],[7,0.44,-5.6,4.2,67]].forEach(function(hd){
    const st=makeHairStrandHXS({len:hd[3],seed:hd[4]});
    st.g.position.set(hd[0],hd[1],hd[2]); st.g.rotation.y=(hd[4]%37)*0.02; g.add(st.g); hairs.push(st);
  });
  /* 清泉寺门：北岸临溪（「门前」），石阶下水 */
  const gate=makeGateHXS({scale:1.0});
  gate.g.position.set(10.5,0.8,-17); gate.g.rotation.y=0.15; g.add(gate.g);
  /* 白发词人：门侧溪畔临流而立（休将白发唱黄鸡） */
  const poet=makeFigure({pose:'独立',robe:0x222e22,belt:0x8f6a33,hat:'发髻',beard:true,hair:0xcfd4c8,
    scale:1.18,rim:0.5,rimC:0xb8d0a8,noProp:true});
  poet.position.set(4.2,0.8,-12.2); poet.rotation.y=2.4; g.add(poet);
  /* 西天微光：溪水所向的一点暖意（west 渐亮＝逆境中见希望） */
  const westGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8c890,
    transparent:true,opacity:0.36,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  westGlow.scale.set(120,46,1); westGlow.position.set(-105,20,-40); westGlow.renderOrder=-7; g.add(westGlow);
  /* 对岸松影 */
  const p1=makePineHXS({h:10,seed:53,scale:1.1}); p1.g.position.set(-20,0.8,-16); g.add(p1.g);
  const p2=makePineHXS({h:12,seed:55,scale:1.3}); p2.g.position.set(-30,0.8,-22); g.add(p2.g);
  const p3=makePineHXS({h:9,seed:59,scale:0.9}); p3.g.position.set(22,0.8,-18); g.add(p3.g);
  const motes=makeGlow({n:34,box:[150,22,80],pos:[0,8,-16],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,26,120],pos:[0,9,-52],scale:76,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x060b07,seed:91,rim:0.12,rimC:0x8fc4a8});
  rk.g.position.set(13,-1.2,12); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:93,sway:1.2,tip:0x2c4028});
  reed.g.position.set(-12,-1.0,13); g.add(reed.g);
  addLights(g,{c:0xd8c8a0,i:0.44,p:[-50,70,30]},{c:0x1e2c20,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.west=Math.min(1,ctl.west+dt/2.8);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const w=ctl.west*ctl.west*(3-2*ctl.west);      // smoothstep：反向的缓起缓收
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      rk.update(t,k); reed.update(t,k); poet.update(t,k);
      /* 水面流向：东 → 反向西去（uFlow 反向并加快） */
      water.mesh.material.uniforms.uFlow.value.set(0.12,0.85-2.1*w);
      /* 溪沫：东漂 → 西去加快（dir 1 → -1.35，spd 2.2 → 3.8） */
      foam.update(t,1-2.35*w,2.2+1.6*w);
      /* 白发：随东流缓漂；点击后随西水消散（乘 fadeK） */
      for(let i=0;i<hairs.length;i++){
        const st=hairs[i];
        st.g.position.x+=((1-w)*0.55-w*1.2)*dt;
        if(st.g.position.x>26)st.g.position.x-=52;
        if(st.g.position.x<-26)st.g.position.x+=52;
        st.mat.opacity=k*0.55*(1-w);
        st.g.rotation.z=Math.sin(t*0.8+i*2.1)*0.05;
      }
      /* 西天微光：随西流渐亮 + 点击脉冲（公式峰值 0.34 ≤ 初值 0.36，每帧乘 fadeK） */
      westGlow.material.opacity=k*(0.06+0.16*w+0.12*ctl.pulse);
      p1.g.rotation.z=Math.sin(t*0.42)*0.008; p2.g.rotation.z=Math.sin(t*0.36+2)*0.007;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.15); pluck(2,0.4,0.12); pluck(4,0.9,0.11); pluck(5,1.5,0.09);
        const fl=$('#flash'); fl.textContent='门前流水尚能西'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                            // 可反复点：西流之势再涨一拍
    },clicked:false};
  return api;
}
