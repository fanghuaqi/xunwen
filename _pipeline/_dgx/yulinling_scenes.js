/* ================= 雨霖铃 · 四境场景（烟雨江南·柳永离别之祖：黛蓝湿雾、雨歇长亭、烟波楚天、晓风残月） =================
   美术立意：全页禁金，黛蓝 #8fb3c9 主调、藕荷 #d8a7b1 仅作点缀；月隐为常，唯设想之景（境③/末境点击后）悬一弯残月。
   标志性瞬间「长亭执手」：雨后长亭前的执手二人剪影；末境点击兰舟——舟发烟波，残月悬上杨柳岸。 */

/* —— 细雨：自写「下落」小着色器（uFade 交给 setFade，slant 给一点斜风）—— */
const YLL_RAIN_VERT=`attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform float uSlant; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float h=mod(uTime*uSpeed*(0.65+aSeed*0.7)+aSeed*97.31, uBox.y);
  p.y-=h; p.x+=h*uSlant;
  float f=h/uBox.y;
  vA=smoothstep(0.0,0.10,f)*smoothstep(1.0,0.70,f);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeRain(o){
  o=o||{};
  const n=o.n===undefined?300:o.n, box=o.box||[160,30,90], pos=o.pos||[0,16,-20];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?3.4:o.size)*(0.7+Math.random()*0.7);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?9:o.speed},
      uSlant:{value:o.slant===undefined?0:o.slant},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x9fb2c8:o.color)},uFade:{value:0},
      uMaxA:{value:o.maxA===undefined?0.34:o.maxA}},
    vertexShader:YLL_RAIN_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* —— 兰舟：Lathe 半壳拉长船身 + 拱篷 + 船凳 + 橹（合批 1 mesh + 接触阴影 1）—— */
function makeLanzhou(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const wood=o.wood===undefined?0x3a332a:o.wood;
  const B=new GeoBag();
  const pts=[[0,0.02],[0.5,0.06],[0.9,0.32],[1.08,0.64],[1.14,0.74]].map(p=>new THREE.Vector2(p[0],p[1]));
  const hull=new THREE.LatheGeometry(pts,18); hull.scale(1.05,0.62,2.8); B.put(hull,wood);
  const bench=new THREE.BoxGeometry(1.5,0.08,0.5); bench.translate(0,0.46,1.0); B.put(bench,shadeColor(wood,1.4));
  const can=new THREE.CylinderGeometry(0.95,0.95,2.5,12,1,true,Math.PI/2,Math.PI);
  can.rotateX(Math.PI/2); can.scale(1,0.62,1); can.translate(0,0.60,-0.6); B.put(can,0x27322c);
  const oar=new THREE.CylinderGeometry(0.035,0.05,2.6,5); oar.rotateX(0.55); oar.translate(0,0.5,2.15);
  B.put(oar,shadeColor(wood,0.8));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x36424a,emissive:0x0a0d12,side:THREE.DoubleSide}),{c:0x8fb3c9,i:0.4,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const sh=new THREE.Mesh(new THREE.CircleGeometry(1.9,16),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0x000000,transparent:true,opacity:0.5,depthWrite:false}));
  sh.rotation.x=-Math.PI/2; sh.position.y=0.03; sh.renderOrder=0; g.add(sh);
  g.scale.setScalar(sc);
  return g;
}

/* —— 垂柳：曲干 + 冠团（Phong 合批 1 mesh）+ 垂丝（摆动着色器 1 mesh，越向梢端摆幅越大）—— */
const YLL_WILLOW_VERT=`
uniform float uTime; uniform float uSway; uniform float uRefY;
void main(){
  vec3 p=position;
  float k=clamp((uRefY-p.y)*0.22,0.0,1.0);
  float ph=p.x*2.3+p.z*1.7;
  p.x+=sin(uTime*0.7+ph)*uSway*k;
  p.z+=cos(uTime*0.55+ph*1.4)*uSway*0.5*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const YLL_WILLOW_FRAG=`uniform vec3 uC; uniform float uFade;
void main(){ gl_FragColor=vec4(uC,uFade); }`;
function makeWillow(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1700:o.seed);
  const h=o.h===undefined?8.5:o.h, n=o.n===undefined?14:o.n, sway=o.sway===undefined?0.55:o.sway;
  const lean=o.lean===undefined?0.16:o.lean;
  const B=new GeoBag();
  let tx=0;
  for(let i=0;i<3;i++){
    const r0=0.24*(1-i*0.24), r1=0.24*(1-(i+1)*0.24);
    const seg=new THREE.CylinderGeometry(Math.max(r1,0.06),Math.max(r0,0.09),h/3,7);
    seg.rotateZ(lean*(i*0.7)); seg.translate(tx,h*(i+0.5)/3,0);
    B.put(seg,0x1d1812);
    tx+=Math.tan(lean*(i*0.7+0.35))*h/3*0.55;
  }
  for(let i=0;i<3;i++){
    const cp=new THREE.SphereGeometry(1.5+R()*1.0,8,6);
    cp.scale(1.3,0.48,1.1); cp.translate(tx+(R()-0.5)*2.6,h+(R()-0.2)*1.4,(R()-0.5)*2.2);
    B.put(cp,0x121b17);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3a38,emissive:0x040806}),{c:0x7fa0b4,i:0.22,p:2.6})));
  /* 垂丝：4 节细管链，自冠顶垂落 */
  const SB=new GeoBag();
  for(let i=0;i<n;i++){
    const sx=tx+(R()-0.5)*5.0, sz=(R()-0.5)*3.6;
    const top=h+(R()-0.5)*1.6, len=2.8+R()*3.6, drift=(R()-0.5)*0.5;
    for(let k=0;k<4;k++){
      const y0=top-len*k/4, y1=top-len*(k+1)/4;
      const st=new THREE.CylinderGeometry(0.014,0.02,Math.abs(y1-y0)*1.06,4,1,true);
      st.translate(sx+drift*k/3,(y0+y1)/2,sz+drift*0.4*k/3);
      SB.put(st,0x212e27);
    }
  }
  const sm=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:sway},uRefY:{value:h-0.8},
      uC:{value:C(0x212e27)},uFade:{value:1}},
    vertexShader:YLL_WILLOW_VERT,fragmentShader:YLL_WILLOW_FRAG});
  const strands=new THREE.Mesh(mergeGeos(SB.list),sm);
  strands.frustumCulled=false; g.add(strands);
  const api={g,update(t,k){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    sm.uniforms.uTime.value=t; }};
  g.userData.update=api.update;
  return api;
}

/* —— 长亭：四柱 + 亭础 + 双层攒尖顶（合批 1 mesh）—— */
function makePavilion(o){
  o=o||{};
  const w=o.w===undefined?7.5:o.w, h=o.h===undefined?4.6:o.h;
  const col=o.color===undefined?0x1a222e:o.color;
  const B=new GeoBag();
  for(const sx of [-1,1]) for(const sz of [-1,1]){
    const pl=new THREE.CylinderGeometry(0.16,0.19,h,8); pl.translate(sx*w/2,h/2,sz*w/2); B.put(pl,col);
    const bs=new THREE.BoxGeometry(0.7,0.22,0.7); bs.translate(sx*w/2,0.11,sz*w/2); B.put(bs,shadeColor(col,0.7));
  }
  const beam=new THREE.BoxGeometry(w*1.15,0.28,w*1.15); beam.translate(0,h,0); B.put(beam,shadeColor(col,0.9));
  const roof1=new THREE.ConeGeometry(w*0.95,1.5,4); roof1.rotateY(Math.PI/4); roof1.translate(0,h+0.95,0); B.put(roof1,shadeColor(col,1.15));
  const roof2=new THREE.ConeGeometry(w*0.55,1.0,4); roof2.rotateY(Math.PI/4); roof2.translate(0,h+2.1,0); B.put(roof2,shadeColor(col,1.3));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x36424e,emissive:0x05080c}),{c:0x8fb3c9,i:0.26,p:2.5})));
  return g;
}

function bCoverYulinling(){ // 封面 · 烟雨江岸（寒蝉声里，一场秋雨将歇）
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:88,amp:0.55,freq:0.09,speed:0.5,flow:[0,0.5],
    deep:0x0a121c,shallow:0x15263a,skyc:0x1e2c3c,spec:0.7,y:-1.9});
  g.add(water.mesh);
  const bank=makeGround({r:44,c1:0x0d1117,c2:0x151c26});
  bank.mesh.position.set(0,-1.1,40); g.add(bank.mesh);
  const ridge=makeRange({r:250,h:22,layers:2,peaks:4,seed:1691,color:0x0b0f16,atmo:0x36445a,fogK:0.70,glowK:0.06,y:-14});
  ridge.g.position.set(0,0,26); g.add(ridge.g);
  const wl1=makeWillow({h:8,seed:1693,n:12,sway:0.5}); wl1.g.position.set(-14,-1.7,8); g.add(wl1.g);
  const wl2=makeWillow({h:6.8,seed:1695,n:10,sway:0.45}); wl2.g.position.set(15,-1.7,4); g.add(wl2.g);
  const pav=makePavilion({w:6,h:4.2}); pav.position.set(6,-1.1,26); pav.rotation.y=-0.4; g.add(pav);
  const rain=makeRain({n:220,box:[200,30,110],pos:[0,16,-16],color:0x9fb2c8,size:3.2,speed:9,maxA:0.2,slant:0.06});
  g.add(rain.points);
  const mist=makeMist({n:10,spread:[240,30,140],pos:[0,9,-42],scale:78,color:0x8fa4c0,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:52,n:16,d:7,color:0x0d1218,seed:1697,sway:0.9,tip:0x2c3a44});
  fg.g.position.set(0,-1.6,28); g.add(fg.g);
  addLights(g,{c:0x93a8c2,i:0.34,p:[-30,70,40]},{c:0x232e3c,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); rain.update(t); mist.update(t,k);
    wl1.update(t,k); wl2.update(t,k); fg.update(t,k);
  }};
}
function bChangting(){ // 一（标志性瞬间）· 长亭执手 —— 骤雨初歇、帐饮无绪、兰舟催发：雨后长亭前，执手二人剪影
  const g=new THREE.Group();
  const water=makeWater({size:520,seg:80,amp:0.4,freq:0.1,speed:0.45,flow:[0,0.3],
    deep:0x0a121c,shallow:0x142434,skyc:0x1d2a3a,spec:0.6,y:-1.9});
  g.add(water.mesh);
  /* 岸台（送别的河岸） */
  const bank=new THREE.Mesh(new THREE.BoxGeometry(30,1.1,24),
    new THREE.MeshPhongMaterial({color:0x10151c,shininess:6,specular:0x242e3a}));
  bank.position.set(0,-0.55,-1); g.add(bank);
  const soil=makeGround({r:20,c1:0x0d1016,c2:0x141a22});
  soil.mesh.position.set(0,0.02,-2); g.add(soil.mesh);
  const ridge=makeRange({r:230,h:20,layers:2,peaks:4,seed:1701,color:0x0a0e15,atmo:0x33404e,fogK:0.68,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,6); g.add(ridge.g);
  /* 对长亭晚（半侧远景）+ 帐饮：席帐 + 长案 + 壶杯盘（陶玉，禁金） */
  const pav=makePavilion({w:7.5,h:4.6}); pav.position.set(-8.5,0,-10.5); pav.rotation.y=0.5; g.add(pav);
  const cur=makeCurtain({w:10,h:5.2,color:0x242e3c,dark:0x0c1119,folds:5});
  cur.g.position.set(-2.8,0.05,-12.5); g.add(cur.g);
  const table=makeTable({w:6.5,d:2.2,h:1.4,wood:0x241a12}); table.g.position.set(-3.2,0,-9.6); g.add(table.g);
  const dish=makeDish({r:0.8,n:4}); dish.g.position.set(-4.6,1.48,-9.4); g.add(dish.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.5}); hu.g.position.set(-2.2,1.48,-10.1); g.add(hu.g);
  const cup1=makeVessel({type:'杯',mat:'玉',scale:0.4,liquid:true}); cup1.g.position.set(-1.3,1.48,-9.3); g.add(cup1.g);
  const cup2=makeVessel({type:'杯',mat:'陶',scale:0.38}); cup2.g.position.set(-0.4,1.48,-9.9); g.add(cup2.g);
  /* 同行的送别人影（帐前） */
  const crowd=makeCrowd({n:3,rect:[-7,-13,6,2.6],seed:1703,color:0x11161e,rimC:0x5a6a7a,rim:0.16,sMin:0.8,sMax:1.0});
  g.add(crowd.mesh);
  /* 标志性瞬间：执手相看泪眼——二人剪影相对，手臂相向近乎相接（避开诗句竖排区，居左前） */
  const poet=makeFigure({pose:'独立',robe:0x2c3442,belt:0x3e4a5a,hat:'幞头',beard:true,scale:1.32,rim:0.72,rimC:0x8fb3c9});
  poet.position.set(-4.6,0,-5.0); poet.rotation.y=0.9; g.add(poet);
  const lady=makeFigure({pose:'独立',robe:0x54414c,belt:0x66525c,hat:'发髻',scale:1.18,rim:0.66,rimC:0xd8a7b1});
  lady.position.set(-3.2,0,-4.8); lady.rotation.y=-0.9; g.add(lady);
  /* 留恋处，兰舟催发：兰舟系岸 + 舟子催发 */
  const boat=makeLanzhou({}); boat.position.set(9,-1.78,-6.5); boat.rotation.y=-0.9; g.add(boat);
  const boatman=makeFigure({pose:'独立',robe:0x1c2129,belt:0x2a323c,hat:'无',scale:0.98,rim:0.4,rimC:0x7a92a8});
  boatman.position.set(9.2,-1.52,-4.6); boatman.rotation.y=-2.2; g.add(boatman);
  /* 骤雨初歇：余雨稀疏 + 亭檐残滴 */
  const rain=makeRain({n:200,box:[170,28,100],pos:[0,15,-14],color:0x9fb2c8,size:3.0,speed:8.5,maxA:0.2,slant:0.05});
  g.add(rain.points);
  const drip=makeRain({n:36,box:[5.5,3.6,4.5],pos:[-8.5,3.6,-10],color:0xa8bccf,size:2.6,speed:6.5,maxA:0.24,slant:0});
  g.add(drip.points);
  const mist=makeMist({n:8,spread:[210,20,70],pos:[0,8,-44],scale:66,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:40,n:12,d:6,color:0x0b0f15,seed:1705,sway:0.8,tip:0x26323c});
  fg.g.position.set(-10,-0.2,10); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x080b10,seed:1706,rim:0.13});
  rk.g.position.set(19,-0.8,7); g.add(rk.g);
  addLights(g,{c:0x8ea6c2,i:0.34,p:[-40,70,-20]},{c:0x1c2734,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); rain.update(t); drip.update(t); mist.update(t,k);
    poet.update(t,k); lady.update(t,k); boatman.update(t,k); crowd.update(t);
    fg.update(t,k); rk.update(t,k);
    boat.position.y=-1.78+0.06*Math.sin(t*0.8);
    boat.rotation.z=0.02*Math.sin(t*0.6);
  }};
}
function bYanbo(){ // 二 · 烟波楚天 —— 千里烟波、暮霭沉沉：贴水横雾两层压住水平线，做出压迫性的开阔
  const g=new THREE.Group();
  const water=makeWater({size:900,seg:96,amp:0.9,freq:0.06,speed:0.7,flow:[0,1.1],
    deep:0x0a1220,shallow:0x142a40,skyc:0x233140,spec:0.9,moonDir:[0,0.3,-1],y:-2.0});
  g.add(water.mesh);
  /* 楚天低阔：远山压得极低极远 */
  const ridge=makeRange({r:430,h:13,layers:2,peaks:3,seed:1707,color:0x090d14,atmo:0x33414f,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  /* 去去孤舟（主体：设想中的行旅，人舟俱孤） */
  const boat=makeLanzhou({}); boat.position.set(-3,-1.8,-24); boat.rotation.y=0.16; g.add(boat);
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',scale:1.12,rim:0.56,rimC:0x8fb3c9});
  poet.position.set(-3.35,-1.62,-24.6); poet.rotation.y=0.3; g.add(poet);
  /* 暮霭沉沉：两层贴水横雾 + 大团横雾（全部退离相机 ≥28 单位，防近景糊团） */
  const fogLow=makeFlow({n:520,box:[420,9,100],pos:[0,-1.2,-58],color:0x7c92aa,size:20,speed:5,maxA:0.36});
  g.add(fogLow.points);
  const fogLow2=makeFlow({n:300,box:[380,6,90],pos:[0,1.8,-82],color:0x6c82a0,size:24,speed:4,maxA:0.3});
  g.add(fogLow2.points);
  const mist=makeMist({n:9,spread:[300,22,80],pos:[0,7,-64],scale:84,color:0x7f95b0,op:0.13});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:46,n:13,d:6,color:0x0b0f15,seed:1709,sway:0.85,tip:0x26323c});
  fg.g.position.set(-10,-1.8,15); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x080b10,seed:1711,rim:0.12});
  rk.g.position.set(20,-2.0,10); g.add(rk.g);
  addLights(g,{c:0x89a0ba,i:0.3,p:[-40,60,-30]},{c:0x1e2937,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); fogLow.update(t); fogLow2.update(t);
    mist.update(t,k); poet.update(t,k); fg.update(t,k); rk.update(t,k);
    boat.position.y=-1.8+0.08*Math.sin(t*0.7); boat.rotation.z=0.02*Math.sin(t*0.5);
  }};
}
function bXiaoyue(){ // 三 · 晓风残月（设想来日之景）—— 今宵酒醒何处？杨柳岸，晓风残月：柳丝拂水、残月低悬
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:88,amp:0.5,freq:0.09,speed:0.5,flow:[0,0.4],
    deep:0x0a121e,shallow:0x16283c,skyc:0x1f2e40,spec:1.15,moonDir:[-0.45,0.16,-0.88],y:-1.9});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(20,1.1,18),
    new THREE.MeshPhongMaterial({color:0x0f141b,shininess:6,specular:0x222c38}));
  bank.position.set(10,-0.55,4); g.add(bank);
  const soil=makeGround({r:13,c1:0x0c1016,c2:0x131a24});
  soil.mesh.position.set(10,0.02,2); g.add(soil.mesh);
  const ridge=makeRange({r:260,h:14,layers:2,peaks:4,seed:1717,color:0x090d14,atmo:0x36445a,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-4); g.add(ridge.g);
  /* 杨柳岸：两株垂柳（晓风拂动；残月由 STAGES 天空提供，低垂于江面上空） */
  const wl1=makeWillow({h:9,seed:1719,n:16,sway:0.62}); wl1.g.position.set(9.5,-0.3,-2); g.add(wl1.g);
  const wl2=makeWillow({h:7.6,seed:1721,n:12,sway:0.55}); wl2.g.position.set(15,-0.3,-7); g.add(wl2.g);
  /* 今宵酒醒：兰舟泊岸（居左前可见区），词中人独坐舟中，酒壶翻倒在舟内 */
  const boat=makeLanzhou({}); boat.position.set(-4.2,-1.78,-3.5); boat.rotation.y=0.45; g.add(boat);
  const poet=makeFigure({pose:'坐饮',robe:0x232b38,belt:0x37414f,hat:'幞头',scale:1.02,rim:0.56,rimC:0xaebfd4,noProp:true});
  poet.position.set(-3.9,-1.55,-3.1); poet.rotation.y=2.6; g.add(poet);
  const jar=makeVessel({type:'壶',mat:'陶',scale:0.4,shadow:false}); jar.g.position.set(-3.2,-1.36,-2.7); jar.g.rotation.z=1.35; g.add(jar.g);
  /* 残月下的水雾微光 */
  const motes=makeGlow({n:60,box:[160,24,90],pos:[0,9,-20],color:0xaebfd4,size:6,speed:0.05,rise:0,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[220,18,110],pos:[0,8,-40],scale:74,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:40,n:12,d:6,color:0x0b0f15,seed:1725,sway:0.8,tip:0x26323c});
  fg.g.position.set(-8,-1.2,14); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x080b10,seed:1726,rim:0.12});
  rk.g.position.set(19,-0.8,10); g.add(rk.g);
  addLights(g,{c:0xaebfd4,i:0.36,p:[-60,50,-70]},{c:0x212d3b,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k);
    poet.update(t,k); fg.update(t,k); rk.update(t,k);
    wl1.update(t,k); wl2.update(t,k);
    boat.position.y=-1.78+0.06*Math.sin(t*0.75);
    boat.rotation.z=0.02*Math.sin(t*0.55);
  }};
}
function bFengqing(){ // 四（末境·可点击）· 风情谁说 —— 此去经年；点击兰舟：舟发烟波，残月悬上杨柳岸
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const water=makeWater({size:760,seg:92,amp:0.7,freq:0.07,speed:0.6,flow:[0,0.9],
    deep:0x0a121e,shallow:0x152840,skyc:0x20303e,spec:0.9,moonDir:[-0.3,0.2,-0.93],y:-1.9});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(26,1.1,20),
    new THREE.MeshPhongMaterial({color:0x0f141b,shininess:6,specular:0x222c38}));
  bank.position.set(0,-0.55,8); g.add(bank);
  const soil=makeGround({r:16,c1:0x0c0f15,c2:0x131922});
  soil.mesh.position.set(0,0.02,4); g.add(soil.mesh);
  const ridge=makeRange({r:280,h:16,layers:2,peaks:3,seed:1731,color:0x090d14,atmo:0x33414f,fogK:0.62,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,-8); g.add(ridge.g);
  /* 杨柳岸：两株垂柳夹岸 */
  const wl1=makeWillow({h:8.8,seed:1733,n:15,sway:0.6}); wl1.g.position.set(-9,-0.3,-2.5); g.add(wl1.g);
  const wl2=makeWillow({h:7.4,seed:1735,n:12,sway:0.55}); wl2.g.position.set(11.5,-0.3,-6); g.add(wl2.g);
  /* 独行客立于岸边（背影四分之三） */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',scale:1.26,rim:0.58,rimC:0x8fb3c9});
  poet.position.set(0.6,0,-0.8); poet.rotation.y=Math.PI+0.35; g.add(poet);
  /* 兰舟（点击主体）：系在岸旁 */
  const boat=makeLanzhou({scale:1.15}); boat.position.set(3.4,-1.76,-3.0); boat.rotation.y=-0.2; g.add(boat);
  const wake=makeGlow({n:110,box:[5,1.4,22],pos:[0,0,0],color:0x9fb6cc,size:6,speed:0.16,rise:0,maxA:0,add:false});
  g.add(wake.points);
  /* 烟波渐阔（点击后大盛） */
  const smoke=makeFlow({n:380,box:[300,8,130],pos:[0,-1.2,-36],color:0x7c92aa,size:24,speed:5.5,maxA:0});
  g.add(smoke.points);
  /* 残月（点击后亮起，悬于杨柳岸上） */
  const moon=makeMoon({r:10,phase:0.64,base:0xdfe8f4,dark:0x2a3550,haze:0.45,hazeColor:0x7f95b0});
  moon.halo[0].op*=0.62; moon.halo[0].s.material.opacity*=0.62;
  moon.group.position.set(-30,30,-120); g.add(moon.group);
  const burst=makeBurst({n:70,color:0xbcd4ee,pos:[3.4,1.4,-3.0]}); g.add(burst.points);
  const mist=makeMist({n:8,spread:[240,20,120],pos:[0,8,-48],scale:78,color:0x8fa4c0,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:12,d:6,color:0x0b0f15,seed:1737,sway:0.75,tip:0x26323c});
  fg.g.position.set(0,-1.6,15); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.8,w:16,d:7,color:0x080b10,seed:1739,rim:0.13});
  rk.g.position.set(-13,-1.7,12); g.add(rk.g);
  addLights(g,{c:0x8fa6c0,i:0.34,p:[-30,70,-20]},{c:0x1f2a38,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/2.8);
      water.update(t); ridge.update(t,0); mist.update(t,k);
      poet.update(t,k); fg.update(t,k); rk.update(t,k);
      wl1.update(t,k); wl2.update(t,k);
      burst.update(t); moon.update(t);
      /* 舟发烟波 */
      boat.position.z=-3.0-34*ctl.ext; boat.position.x=3.4+6*ctl.ext;
      boat.position.y=-1.76+0.08*Math.sin(t*0.8)-0.02*ctl.ext;
      boat.rotation.z=0.025*Math.sin(t*0.55);
      wake.points.position.set(boat.position.x-1.5*ctl.ext,-1.55,boat.position.z+13);
      wake.mat.uniforms.uMaxA.value=k*(0.05+0.42*ctl.ext)*(0.85+0.15*Math.sin(t*1.1));
      wake.update(t);
      smoke.mat.uniforms.uMaxA.value=k*(0.12+0.34*ctl.ext);
      smoke.update(t);
      /* 残月悬杨柳岸 */
      const mA=k*(0.28+0.72*ctl.ext);
      moon.mat.uniforms.uAlpha.value=mA;
      for(let i=0;i<moon.halo.length;i++)moon.halo[i].s.material.opacity=moon.halo[i].op*mA;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.55,0.12); pluck(5,1.0,0.13);
        const fl=$('#flash'); fl.textContent='更与何人说？'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
