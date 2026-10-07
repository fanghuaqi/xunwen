/* ================= 桂枝香·金陵怀古 · 四境场景（大漠金戈·怀古变体：澄江如练、残阳帆影、门外楼头、后庭遗曲） =================
   美术立意：同《潼关怀古》大漠怀古先例——底色 #120d08、雾 #1a120a、主色灰沉、禁艳金；
   本诗自开两色：澄江白练（低饱和暖白，全页唯一亮色，取「澄江似练」）与残阳锈赭（低饱和金照）。
   标志性瞬间「千里澄江似练」（境①）：登临俯瞰，长江如一匹白绢在暮秋天地里铺展，翠峰攒聚如簇。
   末境点击澄江似练：江面展白绢 + 六朝残迹（城砖/断柱/残碑）浮沉；「至今商女时时犹唱」以拨弦
   余音作全篇听觉收束。
   情感曲线：肃爽登临 → 残阳如画 → 悲恨相续 → 余音不绝。 */

/* turnFlow：makeFlow 把 pos 烘进顶点，整体 rotation.y 后平移补偿，使流心仍落在想要的世界坐标 */
function turnFlow(f,rotY,B,Cw){
  const s=Math.sin(rotY),co=Math.cos(rotY);
  f.points.rotation.y=rotY;
  f.points.position.set(Cw[0]-(B[0]*co+B[2]*s), Cw[1]-B[1], Cw[2]-(-B[0]*s+B[2]*co));
  return f;
}

/* —— 澄江白练：一匹沿江道铺展的白绢（本诗标志性意象，uFade 显式交给 setFade）—— */
const GZX_SILK_VERT=`
uniform float uTime; uniform float uAmp; uniform float uFreq;
varying vec2 vUv; varying float vWob;
void main(){
  vUv=uv;
  vec3 p=position;
  float x=p.x;
  p.z+=sin(x*uFreq)*uAmp+sin(x*uFreq*0.37+1.7)*uAmp*0.55;
  p.y+=sin(x*0.12+uTime*1.3)*0.16;
  vWob=sin(x*0.05-uTime*0.9);
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const GZX_SILK_FRAG=`
uniform float uTime; uniform float uFade; uniform float uMaxA; uniform float uExt; uniform vec3 uColor;
varying vec2 vUv; varying float vWob;
void main(){
  float along=vUv.x;
  float across=smoothstep(0.0,0.30,vUv.y)*smoothstep(1.0,0.70,vUv.y);
  float fx=(along-0.5)*2.0;
  float win=1.0-smoothstep(uExt-0.18,uExt,abs(fx));
  float sheen=0.80+0.20*sin(vUv.x*46.0-uTime*1.1+vWob);
  float pulse=0.90+0.10*sin(uTime*0.5+along*9.0);
  vec3 col=uColor*(0.92+0.10*sin(along*23.0-uTime*0.7));
  gl_FragColor=vec4(col,uFade*uMaxA*across*win*sheen*pulse);
}`;
function makeSilk(o){
  o=o||{};
  const len=o.len===undefined?430:o.len, w=o.w===undefined?13:o.w;
  const geo=new THREE.PlaneGeometry(len,w,150,1); geo.rotateX(-Math.PI/2);
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.5:o.maxA},
      uExt:{value:o.ext===undefined?1:o.ext},uAmp:{value:o.amp===undefined?30:o.amp},
      uFreq:{value:o.freq===undefined?0.0115:o.freq},
      uColor:{value:C(o.color===undefined?0xd6cab0:o.color)}},
    vertexShader:GZX_SILK_VERT,fragmentShader:GZX_SILK_FRAG});
  const mesh=new THREE.Mesh(geo,m); mesh.frustumCulled=false; mesh.renderOrder=2; // 水面(1)之后画，避免被近水面冲掉
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh,mat:m,update(t){m.uniforms.uTime.value=t;},
    setExt(v){m.uniforms.uExt.value=Math.max(0.001,Math.min(1,v));}};
}

/* —— 翠峰如簇：攒聚如箭簇的黛色群峰（合批 1 mesh）—— */
function makeCuifeng(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17201:o.seed);
  const B=new GeoBag(), n=o.n===undefined?9:o.n;
  for(let i=0;i<n;i++){
    const h=(o.h===undefined?30:o.h)*(0.45+0.85*R());
    const r=h*(0.42+0.22*R());
    const c=new THREE.ConeGeometry(r,h,5+((i*7)%3));
    c.rotateZ((R()-0.5)*0.16);
    c.translate((R()-0.5)*(o.w===undefined?110:o.w),(R()-0.5)*10,(R()-0.5)*(o.d===undefined?70:o.d));
    B.put(c,shadeColor(o.color===undefined?0x0c110b:o.color,0.75+0.5*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x241d12,emissive:0x050703}),{c:0xb8905a,i:o.rim===undefined?0.15:o.rim,p:2.8})));
  return g;
}

/* —— 城垛：垛口城头一段（登临处/凭高处，合批 1 mesh）—— */
function makeChengduo(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, h=o.h===undefined?1.5:o.h;
  const c=o.color===undefined?0x0d0906:o.color;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,h,1.6); wall.translate(0,h/2,0); B.put(wall,c);
  const n=Math.max(3,Math.round(w/2.2));
  for(let i=0;i<n;i++){
    const m=new THREE.BoxGeometry(1.1,0.75,1.6);
    m.translate(-w/2+0.55+i*(w-1.1)/(n-1),h+0.37,0); B.put(m,shadeColor(c,1.35));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xb8905a,i:o.rim===undefined?0.14:o.rim,p:2.8})));
  return g;
}

/* —— 归帆：船身+桅+帆（帆单独 1 mesh 便于摆动）——「归帆去棹残阳里」 */
function makeGuiFan(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale, ph=o.phase===undefined?0:o.phase;
  const B=new GeoBag();
  const hull=new THREE.LatheGeometry([[0,0.05],[0.55,0.05],[0.85,0.22],[0.95,0.5],[0.9,0.62]]
    .map(p=>new THREE.Vector2(p[0],p[1])),12);
  hull.scale(0.9,0.55,2.6); B.put(hull,0x0c0806);
  const mast=new THREE.CylinderGeometry(0.06,0.09,3.4,6); mast.translate(0,2.2,0.3); B.put(mast,0x0a0705);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x241a10,emissive:0x040302}),{c:0xb8905a,i:0.20,p:2.6})));
  const sail=new THREE.Mesh(new THREE.PlaneGeometry(1.9,2.6,4,4),
    new THREE.MeshPhongMaterial({color:o.sailC===undefined?0x2a1c10:o.sailC,side:THREE.DoubleSide,
      shininess:4,specular:0x241a10}));
  sail.position.set(0,2.5,0.32); g.add(sail);
  g.scale.setScalar(sc);
  return {g,sail,ph,update(t){ sail.rotation.y=0.10*Math.sin(t*0.8+ph); }};
}

/* —— 酒旗斜矗：岸边酒垆 + 斜杆上的一幅酒旗（旗摆动）—— */
function makeJiuqi(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17203:o.seed);
  const B=new GeoBag();
  const rock=rockGeo(2.6,1,R); rock.translate(0,0.6,0); B.put(rock,0x0b0805);
  const pole=new THREE.CylinderGeometry(0.07,0.10,7.5,6); pole.rotateZ(0.10); pole.translate(0.55,3.7,0); B.put(pole,0x0a0705);
  const hut=new THREE.BoxGeometry(3.4,1.9,2.6); hut.translate(-2.6,0.95,0.4); B.put(hut,0x0d0906);
  const roof=new THREE.ConeGeometry(2.5,1.1,4); roof.rotateY(Math.PI/4); roof.translate(-2.6,2.45,0.4); B.put(roof,0x0b0705);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xb8905a,i:0.18,p:2.6})));
  const flagGeo=new THREE.PlaneGeometry(2.5,1.5,6,2);
  flagGeo.translate(1.25,0,0);
  const flag=new THREE.Mesh(flagGeo,new THREE.MeshPhongMaterial({color:0x6a3424,side:THREE.DoubleSide,
    shininess:6,specular:0x3a2418}));
  flag.position.set(1.1,5.9,0); flag.rotation.z=-0.10; g.add(flag);
  return {g,flag,update(t){ flag.rotation.y=0.35*Math.sin(t*1.4)+0.15*Math.sin(t*2.3); }};
}

/* —— 白鹭：星河鹭起（合批单 mesh，振翅以纵向伸缩示意）—— */
function makeEgret(o){
  o=o||{};
  const ph=o.phase===undefined?0:o.phase, c=o.color===undefined?0xcfc6b0:o.color;
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.09,0.7,5); body.rotateX(Math.PI/2); B.put(body,c);
  const wL=new THREE.PlaneGeometry(0.85,0.26); wL.translate(-0.45,0,0); wL.rotateZ(0.22); B.put(wL,c);
  const wR=new THREE.PlaneGeometry(0.85,0.26); wR.translate(0.45,0,0); wR.rotateZ(-0.22); B.put(wR,c);
  const mat=new THREE.MeshBasicMaterial({color:0xffffff,vertexColors:true,transparent:true,
    opacity:0.8,side:THREE.DoubleSide,depthWrite:false});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat); mesh.renderOrder=3; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mat,ph,update(t,k){
    const f=0.5+0.5*Math.sin(t*7+ph);
    mesh.scale.y=0.55+0.5*f;
    mat.opacity=k*(0.42+0.38*f);
  }};
}

/* —— 六朝宫阙虚影：黯铜色的楼台群像，在尘霾里明灭（合批 1 mesh，禁艳金）—— */
function makeGongqueGhost(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17205:o.seed);
  const ph=o.ph===undefined?0:o.ph, op0=o.op===undefined?0.26:o.op;
  const B=new GeoBag();
  const specs=o.specs||[[-52,15,-8],[-18,22,-14],[16,26,-18],[52,17,-9],[-78,10,-4],[82,12,-5]];
  for(let i=0;i<specs.length;i++){
    const sp=specs[i], x=sp[0], h=sp[1], z=sp[2], w=4+R()*3;
    const body=new THREE.BoxGeometry(w,h,w*0.7); body.translate(x,h/2,z);
    B.put(body,shadeColor(o.color===undefined?0x6a5636:o.color,0.8+0.4*R()));
    const roof=new THREE.ConeGeometry(w*0.85,w*0.42,4); roof.rotateY(Math.PI/4); roof.translate(x,h+w*0.21,z);
    B.put(roof,shadeColor(o.color===undefined?0x6a5636:o.color,1.15+0.3*R()));
  }
  const m=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,specular:0x2a2214,
    transparent:true,opacity:op0,emissive:0x120d06,depthWrite:false});
  const mesh=new THREE.Mesh(mergeGeos(B.list),m); mesh.renderOrder=1; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,m,update(t,k){ m.opacity=k*op0*(0.82+0.18*Math.sin(t*0.5+ph)); }};
}

/* —— 六朝残迹：城砖/断柱/残碑的沉江旧物（点击后自江心浮沉显形，合批 1 mesh）—— */
function makeCanji(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17207:o.seed);
  const B=new GeoBag();
  for(let i=0;i<5;i++){
    const w=1.6+R()*2.2,h=0.8+R()*1.4;
    const b=new THREE.BoxGeometry(w,h,w*(0.5+R()*0.6));
    b.rotateY(R()*6.28); b.rotateZ((R()-0.5)*0.3);
    b.translate(-26+i*12+(R()-0.5)*5,0.35,(R()-0.5)*14);
    B.put(b,shadeColor(0x2a2016,0.8+0.5*R()));
  }
  for(let i=0;i<4;i++){
    const h=1.6+R()*2.4;
    const c=new THREE.CylinderGeometry(0.35+R()*0.2,0.5+R()*0.2,h,8);
    c.rotateZ((R()-0.5)*0.7);
    c.translate(-20+i*13+(R()-0.5)*4,h*0.4,6+(R()-0.5)*16);
    B.put(c,shadeColor(0x32281a,0.8+0.5*R()));
  }
  const bb=new THREE.BoxGeometry(1.4,2.6,0.35);
  bb.rotateZ(0.35); bb.rotateY(0.5); bb.translate(14,1.0,4);
  B.put(bb,0x38301e);
  const mat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,specular:0x241d12,
    transparent:true,opacity:0.38,emissive:0x0a0805,depthWrite:false});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat); mesh.renderOrder=2; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mat,update(t,k,ext){
    mat.opacity=k*ext*(0.26+0.12*Math.sin(t*0.8));
    g.position.y=Math.sin(t*0.45)*0.55*ext;
    mesh.rotation.y=0.04*Math.sin(t*0.2);
  }};
}

/* —— 商女歌馆：江岸尽头的小楼，一点暖窗（全篇收束的唯一暖点，合批 1 mesh）—— */
function makeGeguan(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(4.2,2.4,3.0); body.translate(0,1.2,0); B.put(body,0x0e0a06);
  const roof=new THREE.ConeGeometry(3.1,1.3,4); roof.rotateY(Math.PI/4); roof.translate(0,3.05,0); B.put(roof,0x0b0805);
  const rai=new THREE.BoxGeometry(3.4,0.08,0.08); rai.translate(0.6,2.2,1.6); B.put(rai,0x120c07);
  for(let i=0;i<3;i++){
    const p=new THREE.BoxGeometry(0.07,0.7,0.07); p.translate(-0.6+i*1.2,1.85,1.6); B.put(p,0x120c07);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x1d160e,emissive:0x040302}),{c:0xb8905a,i:0.16,p:2.6})));
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa87038,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(3.2,3.2,1); win.position.set(0.4,1.6,1.7); win.renderOrder=4; g.add(win);
  return {g,win,update(t,k){ win.material.opacity=k*(0.14+0.08*Math.sin(t*1.1)+0.03*Math.sin(t*3.7)); }};
}

function bCoverGzx(){ // 封面 · 暮霭里的金陵江天（残照未熄，尘霾低回）
  const g=new THREE.Group();
  const water=makeWater({size:680,seg:88,amp:0.5,freq:0.08,speed:0.5,flow:[0,0.5],
    deep:0x120d08,shallow:0x241a10,skyc:0x3a2a18,spec:0.25,moonDir:[-0.55,0.14,-0.8],moonColor:0xb08858,y:-2.0});
  g.add(water.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:17209,color:0x0b0806,atmo:0x332414,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-16); g.add(ridge.g);
  const motes=makeGlow({n:60,box:[220,34,130],pos:[0,10,-40],color:0xc09a68,size:7,speed:0.05,rise:0,maxA:0.30});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[250,26,140],pos:[0,10,-54],scale:80,color:0x8a6f4e,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:48,n:13,d:6,color:0x0a0704,seed:17213,sway:0.9,tip:0x3a2c16});
  fg.g.position.set(0,-1.8,26); g.add(fg.g);
  /* 晚渡旅人：岸畔一行剪影（远景人迹） */
  const walker=makeFigure({pose:'独立',robe:0x1c150e,belt:0x4a3a24,hat:'幞头',scale:0.8,rim:0.5,rimC:0xb8905a});
  walker.position.set(-11,-1.8,19); walker.rotation.y=0.4; g.add(walker);
  addLights(g,{c:0xc09058,i:0.36,p:[-40,60,30]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k); fg.update(t,k);
    walker.update(t,k);
  }};
}
function bDenglin(){ // 一（标志性瞬间）· 澄江如练 —— 登临送目：俯瞰澄江，白绢铺展，翠峰如簇
  const g=new THREE.Group();
  const water=makeWater({size:980,seg:96,amp:0.32,freq:0.06,speed:0.38,flow:[0,0.3],
    deep:0x14100a,shallow:0x282015,skyc:0x42321e,spec:0.30,moonDir:[-0.4,0.16,-0.9],moonColor:0xb08858,y:-1.6});
  g.add(water.mesh);
  const silk=makeSilk({len:410,w:15,amp:26,freq:0.011,maxA:0.60,ext:1,color:0xdecfb2});
  silk.g.position.set(0,-0.4,-34); silk.g.rotation.y=-0.18; g.add(silk.g);
  const ridge=makeRange({r:340,h:26,layers:3,peaks:6,seed:17215,color:0x0a0705,atmo:0x3a2a18,fogK:0.58,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  const fengL=makeCuifeng({seed:17217,n:6,h:40,w:90,d:70,color:0x0c110b,rim:0.15});
  fengL.position.set(-105,-3,-100); g.add(fengL);
  const fengR=makeCuifeng({seed:17219,n:6,h:46,w:100,d:70,color:0x0d120c,rim:0.15});
  fengR.position.set(112,-3,-116); g.add(fengR);
  /* 登临处：脚下望楼台 + 凭堞送目的词人背影（画面下缘）+ 崖沿框景 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(7,2.4,6),
    new THREE.MeshPhongMaterial({color:0x100b07,shininess:4,specular:0x1d160e}));
  tai.position.set(3,8.2,36); g.add(tai);
  const poet=makeFigure({pose:'独立',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.4,rim:0.65,rimC:0xb8905a});
  poet.position.set(3,9.4,36.5); poet.rotation.y=Math.PI-0.3; g.add(poet);
  const duo=makeChengduo({w:10,h:1.5});
  duo.position.set(9.5,8.6,39); duo.rotation.y=0.5; g.add(duo);
  const cliff=makeForeground({kind:'岩壁',n:3,r:4.2,w:16,d:7,color:0x0a0704,seed:17221,rim:0.12,rimC:0xb8905a});
  cliff.g.position.set(16,-2.5,74); g.add(cliff.g);
  const dust=makeFlow({n:150,box:[220,12,80],pos:[0,7,-30],color:0x9a7c50,size:15,speed:4.5,maxA:0.10});
  g.add(dust.points);
  const mist=makeMist({n:8,spread:[280,22,110],pos:[0,8,-70],scale:84,color:0x8a6f4e,op:0.09});
  g.add(mist.g);
  addLights(g,{c:0xc09058,i:0.40,p:[-60,70,20]},{c:0x33281a,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); silk.update(t); ridge.update(t,0); dust.update(t); mist.update(t,k);
    cliff.update(t,k); poet.update(t,k);
  }};
}
function bGuifan(){ // 二 · 残阳帆影 —— 归帆去棹残阳里，背西风酒旗斜矗；彩舟云淡，星河鹭起
  const g=new THREE.Group();
  const water=makeWater({size:760,seg:96,amp:0.55,freq:0.08,speed:0.6,flow:[0,0.6],
    deep:0x150e08,shallow:0x32220e,skyc:0x54371c,spec:0.28,moonDir:[-0.55,0.14,-0.82],moonColor:0xb08858,y:-1.7});
  g.add(water.mesh);
  const ridge=makeRange({r:320,h:16,layers:2,peaks:4,seed:17223,color:0x0b0705,atmo:0x4a3018,fogK:0.60,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,-20); g.add(ridge.g);
  /* 残阳：低垂一轮锈赭落日 + 贴水霞光（低饱和，禁艳金） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(7.5,30),
    new THREE.MeshBasicMaterial({color:0x9a5228,transparent:true,opacity:0.55,depthWrite:false,
      fog:false,blending:THREE.AdditiveBlending}));
  sun.position.set(-86,7,-190); sun.renderOrder=-5; g.add(sun);
  const sunglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8a4c26,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunglow.scale.set(90,50,1); sunglow.position.set(-84,9,-188); sunglow.renderOrder=-4; g.add(sunglow);
  /* 归帆去棹：两叶归帆，缓帆漂移 */
  const boats=[[-20,-46,1.1],[-42,-64,1.45]].map(function(b){
    const bf=makeGuiFan({scale:b[2],phase:b[0],sailC:0x3a2817});
    bf.g.position.set(b[0],-1.5,b[1]); bf.g.rotation.y=0.14; g.add(bf.g);
    bf.x0=b[0]; bf.z0=b[1]; return bf;
  });
  /* 彩舟云淡：远处两叶彩舟（黯朱、黯青），化在云淡里 */
  const czB=new GeoBag();
  [[-92,-118,0x5a3030],[70,-126,0x2e3a30]].forEach(function(s){
    const hull=new THREE.LatheGeometry([[0,0.03],[0.5,0.04],[0.75,0.2],[0.8,0.42]]
      .map(p=>new THREE.Vector2(p[0],p[1])),10);
    hull.scale(0.8,0.5,2.2); hull.translate(s[0],-1.3,s[1]); czB.put(hull,s[2]);
  });
  const cz=czB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x241a10,transparent:true,opacity:0.6,emissive:0x0a0705,depthWrite:false}));
  cz.renderOrder=1; g.add(cz);
  /* 酒旗斜矗：西风里的岸边酒垆 + 垆前驻足的旅人 */
  const jq=makeJiuqi({seed:17225});
  jq.g.position.set(20,-1.2,-26); jq.g.rotation.y=-0.5; g.add(jq.g);
  const ke=makeFigure({pose:'独立',robe:0x201810,belt:0x54422a,hat:'幞头',scale:1.0,rim:0.55,rimC:0xb8905a});
  ke.position.set(16.5,-1.1,-21.5); ke.rotation.y=-2.6; g.add(ke);
  /* 星河鹭起：初现的星河下，白鹭联翩而起 */
  const egrets=[0,1,2,3,4].map(function(i){
    const e=makeEgret({phase:i*1.37}); g.add(e.g); return e;
  });
  const motes=makeGlow({n:50,box:[200,26,100],pos:[0,9,-40],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  const wind=turnFlow(makeFlow({n:240,box:[200,14,70],pos:[0,9,-36],color:0x8a6f4c,size:22,speed:6,maxA:0.16}),
    1.05,[0,9,-36],[0,9,-36]);
  g.add(wind.points);
  const mist=makeMist({n:8,spread:[240,18,100],pos:[0,7,-58],scale:76,color:0x9a7c58,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:36,n:9,d:6,color:0x0a0704,seed:17227,sway:1.0,tip:0x3a2c16});
  fg.g.position.set(-12,-1.6,12); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x0a0704,seed:17229,rim:0.12,rimC:0xb8905a});
  rk.g.position.set(19,-2.1,7); g.add(rk.g);
  addLights(g,{c:0xd09a58,i:0.5,p:[-70,40,-40]},{c:0x3a2c1c,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0);
    sun.material.opacity=k*(0.44+0.11*Math.sin(t*0.4));
    sunglow.material.opacity=k*(0.24+0.06*Math.sin(t*0.4+1.0));
    for(let i=0;i<boats.length;i++){
      const b=boats[i];
      b.g.position.x=b.x0+2.2*Math.sin(t*0.10+b.ph);
      b.g.position.z=b.z0+3.0*Math.sin(t*0.06+b.ph*1.7);
      b.g.position.y=-1.5+0.14*Math.sin(t*0.85+b.ph);
      b.g.rotation.z=0.02*Math.sin(t*0.7+b.ph);
      b.update(t);
    }
    for(let i=0;i<egrets.length;i++){
      const e=egrets[i], cyc=((t*0.16)+i*0.23)%1;
      e.g.position.set(-34+i*15+cyc*8, 2.5+cyc*24, -30-cyc*38-i*2.5);
      e.g.rotation.y=0.55+0.25*Math.sin(t*0.4+i);
      e.update(t,k);
    }
    jq.update(t); motes.update(t); wind.update(t); mist.update(t,k);
    fg.update(t,k); rk.update(t,k); ke.update(t,k);
  }};
}
function bPinggao(){ // 三 · 门外楼头 —— 凭高吊古：城头独立，六朝宫阙虚影明灭，门外旗影相续
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.4,freq:0.075,speed:0.5,flow:[0,0.7],
    deep:0x0f0c08,shallow:0x201810,skyc:0x2e2013,spec:0.3,moonDir:[-0.5,0.2,-0.8],moonColor:0xc8a070,y:-2.0});
  g.add(water.mesh);
  const ridge=makeRange({r:360,h:20,layers:2,peaks:5,seed:17230,color:0x0a0705,atmo:0x2e2013,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  /* 石头城头：城墙步道 + 垛口 + 凭高的词人背影 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(28,2.4,12),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  tai.position.set(0,-0.2,-6); g.add(tai);
  const top=makeGround({r:12,c1:0x0e0a07,c2:0x16100a});
  top.mesh.position.set(0,1.05,-6); g.add(top.mesh);
  const duo3=makeChengduo({w:20,h:1.5});
  duo3.position.set(0,1.0,-12.4); g.add(duo3);
  const poet=makeFigure({pose:'独立',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.35,rim:0.6,rimC:0xb8905a});
  poet.position.set(2.2,1.05,-10.6); poet.rotation.y=Math.PI-0.2; g.add(poet);
  /* 六朝宫阙虚影：明灭的黯铜色楼台（谩嗟荣辱）——近移以免没入雾里 */
  const ghost=makeGongqueGhost({seed:17231,op:0.30,ph:0.8,color:0x6a5636});
  ghost.g.position.set(0,0,-85); ghost.g.scale.setScalar(1.25); g.add(ghost.g);
  /* 门外旗影：一列暗旗自远而近（悲恨相续） */
  const flags=[];
  [[-26,12,-70],[-14,9,-88],[-36,8,-100]].forEach(function(fp,i){
    const B=new GeoBag();
    const pole=new THREE.CylinderGeometry(0.09,0.12,fp[1],5); pole.translate(0,fp[1]/2,0); B.put(pole,0x0b0806);
    const m=new THREE.Mesh(mergeGeos(B.list),
      new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,specular:0x1d160e,emissive:0x040302}));
    m.position.set(fp[0],0,fp[2]); g.add(m);
    const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.6,1.5,5,2),
      new THREE.MeshPhongMaterial({color:0x2e2620,side:THREE.DoubleSide,shininess:4,specular:0x241d14}));
    fl.position.set(1.3,fp[1]-0.9,0); m.add(fl); flags.push({fl:fl,ph:i*1.9});
  });
  /* 悲恨余烬：宫阙深处一点将熄的暗红 + 灰烬浮尘 */
  const ember=new THREE.PointLight(0x6a3020,0.30,60); ember.position.set(0,10,-85); g.add(ember);
  const ash=makeGlow({n:44,box:[150,18,70],pos:[0,9,-70],color:0x6a5a44,size:6,speed:0.04,rise:0.2,maxA:0.20});
  g.add(ash.points);
  const dust=turnFlow(makeFlow({n:260,box:[180,16,70],pos:[-20,8,-64],color:0x3a332a,size:24,speed:5,maxA:0.20}),
    0.9,[-20,8,-64],[-20,8,-64]);
  g.add(dust.points);
  const mist=makeMist({n:9,spread:[240,22,110],pos:[0,10,-66],scale:80,color:0x6a5c48,op:0.11});
  g.add(mist.g);
  /* 前景：脚下一截垛口 + 枯枝 */
  const duoF=makeChengduo({w:14,h:1.4});
  duoF.position.set(-1,-1.2,18); duoF.rotation.y=-0.08; g.add(duoF);
  const tree=makeForeground({kind:'树枝',n:2,w:13,d:5,color:0x0a0704,seed:17232,sway:1.1,rim:0.14,rimC:0xb8905a});
  tree.g.position.set(13,0.8,16); g.add(tree.g);
  addLights(g,{c:0x9a7c50,i:0.30,p:[-50,60,-30]},{c:0x2e2418,i:0.60});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0);
    poet.update(t,k);
    ghost.update(t,k);
    ember.intensity=k*(0.22+0.10*Math.sin(t*0.7)+0.04*Math.sin(t*3.1));
    for(let i=0;i<flags.length;i++){ flags[i].fl.rotation.y=0.3*Math.sin(t*1.2+flags[i].ph); }
    ash.update(t); dust.update(t); mist.update(t,k);
    tree.update(t,k);
  }};
}
function bYiqu(){ // 四（末境·可点击）· 后庭遗曲 —— 六朝旧事随流水：点击澄江似练，白绢展江、六朝残迹浮沉
  const ctl={t:0,clicked:false,ext:0,lastSong:0};
  const g=new THREE.Group();
  const water=makeWater({size:800,seg:96,amp:0.5,freq:0.075,speed:0.55,flow:[0,1.2],
    deep:0x0e0b07,shallow:0x1c160e,skyc:0x241a10,spec:0.15,moonDir:[-0.8,0.18,-0.55],moonColor:0x8a7048,y:-1.8});
  g.add(water.mesh);
  const ridge=makeRange({r:340,h:18,layers:2,peaks:5,seed:17233,color:0x0a0705,atmo:0x2e2013,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-24); g.add(ridge.g);
  /* 左岸：寒烟衰草凝绿（两块压扁的绿褐土石，无硬边圆盘） */
  const dcB=new GeoBag();
  const m1=rockGeo(7,1,seedRnd(17234)); m1.scale(1.5,0.22,1.0); m1.translate(-19,-1.2,-21); dcB.put(m1,0x11140c);
  const m2=rockGeo(4.5,1,seedRnd(17236)); m2.scale(1.4,0.24,1.0); m2.translate(-11,-1.45,-15); dcB.put(m2,0x0e120a);
  g.add(dcB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x1a160e,emissive:0x050703})));
  /* 白绢（点击后展江）+ 六朝残迹（点击后浮沉显形） */
  const silk=makeSilk({len:330,w:9,amp:24,freq:0.013,maxA:0.40,ext:0.001});
  silk.g.position.set(0,0.05,-30); silk.g.rotation.y=0.1; g.add(silk.g);
  const canji=makeCanji({seed:17235});
  canji.g.position.set(0,-1.4,-52); g.add(canji.g);
  /* 商女歌馆：江岸尽头的小楼，一点暖窗 + 凭栏的商女（全篇收束的唯一暖点） */
  const gg=makeGeguan({});
  gg.g.position.set(24,-1.2,-52); gg.g.rotation.y=-0.4; g.add(gg.g);
  const shangnv=makeFigure({pose:'独立',robe:0x3a2c2c,belt:0x5a4438,skin:0xd3b89f,collar:0x8a7a64,
    hat:'发髻',scale:0.52,rim:0.55,rimC:0xc8a878});
  shangnv.position.set(23.5,-1.5,-50.3); shangnv.rotation.y=-2.2; g.add(shangnv);
  const han=makeMist({n:10,spread:[260,18,110],pos:[0,5,-48],scale:78,color:0x5a5c4c,op:0.12});
  g.add(han.g);
  const flowc=makeFlow({n:260,box:[240,6,80],pos:[0,-0.5,-40],color:0x4a4a3c,size:20,speed:4.5,maxA:0.26});
  g.add(flowc.points);
  const fgL=makeForeground({kind:'芦苇',w:46,n:14,d:6,color:0x120c05,seed:17237,sway:1.1,tip:0x3a2e18});
  fgL.g.position.set(-8,-1.7,11); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:30,n:9,d:5,color:0x0f0a04,seed:17239,sway:0.9,tip:0x362a16});
  fgR.g.position.set(14,-2.0,16); g.add(fgR.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:11,d:6,color:0x0b0805,seed:17241,rim:0.10,rimC:0xb8905a});
  rk.g.position.set(-15,-2.2,13); g.add(rk.g);
  addLights(g,{c:0x8a7048,i:0.26,p:[-40,50,-30]},{c:0x2e2418,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.ext=Math.min(1,ctl.ext+dt/3.2);
        if(t-ctl.lastSong>6.5){ ctl.lastSong=t; pluck(2,0,0.06); pluck(5,0.55,0.05); } // 遗曲余音，隐隐相闻
      }
      const e=ctl.ext*(2-ctl.ext); // easeOut
      silk.setExt(0.001+0.999*e);
      water.update(t); ridge.update(t,0); silk.update(t); han.update(t,k); flowc.update(t);
      fgL.update(t,k); fgR.update(t,k); rk.update(t,k); gg.update(t,k);
      shangnv.update(t,k);
      canji.update(t,k,ctl.clicked?e:0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.0,0.10); pluck(3,0.4,0.09); pluck(5,0.9,0.09); pluck(7,1.5,0.08); // 后庭遗曲，拨弦余音
        const fl=$('#flash'); fl.textContent='六朝旧事随流水'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
