/* ================= 南乡子·登京口北固亭有怀 · 四境场景（大漠金戈：望断神州、不尽长江、坐断东南、生子仲谋） =================
   美术立意：大漠金戈赛道落于江天——底色 #120d08、雾 #1a120a 系、accent=#c49a5a（栏柱/人物边缘光/旗纹），禁艳金。
   江涛与战旗是本页动态元素；「神州不可见」的怅惘（境①尘霭锁江天、星光压暗）与「少年英主」的昂扬
   （境③火光军阵战旗）对照。三问三答为骨架。
   标志性瞬间「不尽长江滚滚流」（境②）：亭上凭栏，千叠浪着色器滚滚东去，以大江回答千古一问；
   末境点击北固亭：江浪千叠自远涌起答千古一问，「生子当如孙仲谋」题字同现。
   情感曲线：怅惘北望 → 苍茫江声 → 少年昂扬 → 江声作答。 */

/* —— 江浪千叠（本诗标志性意象，uFade 显式双 shader 交给 setFade）——
   数条长浪带沿江道向东滚动，浪脊 pow 提亮；uExt 控制涌起程度（末境点击后自 0 涌起） */
const NXZ_WAVE_VERT=`
uniform float uTime; uniform float uAmp;
varying vec2 vUv; varying float vRoll;
void main(){
  vUv=uv;
  vec3 p=position;
  float roll=sin(p.x*0.085-uTime*1.15)+0.55*sin(p.x*0.21-uTime*1.9+2.0);
  p.y+=roll*uAmp*(0.35+0.65*vUv.x);
  vRoll=roll;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const NXZ_WAVE_FRAG=`
uniform float uTime; uniform float uFade; uniform float uMaxA; uniform float uExt; uniform vec3 uColor;
varying vec2 vUv; varying float vRoll;
void main(){
  float crest=pow(clamp(0.5+0.5*vRoll,0.0,1.0),3.0);
  float across=smoothstep(0.0,0.32,vUv.y)*smoothstep(1.0,0.68,vUv.y);
  float band=0.78+0.22*sin(vUv.x*30.0-uTime*2.4);
  float sheen=0.86+0.14*sin(uTime*0.8+vUv.x*9.0);
  vec3 col=uColor*(0.80+0.52*crest);
  gl_FragColor=vec4(col,uFade*uMaxA*across*band*(0.22+0.78*crest)*(0.35+0.65*uExt)*sheen);
}`;
function makeLangdie(o){
  o=o||{};
  const bands=o.bands===undefined?3:o.bands, ext0=o.ext===undefined?1:o.ext;
  const g=new THREE.Group(), parts=[];
  for(let i=0;i<bands;i++){
    const len=(o.len===undefined?290:o.len)*(1-0.14*i);
    const w=(o.w===undefined?14:o.w)*(1-0.15*i);
    const geo=new THREE.PlaneGeometry(len,w,110,1); geo.rotateX(-Math.PI/2);
    const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
      uniforms:{uTime:{value:i*1.7},uAmp:{value:(o.amp===undefined?0.55:o.amp)*(1-0.12*i)},
        uFade:{value:0},uMaxA:{value:(o.maxA===undefined?0.46:o.maxA)*(1-0.12*i)},
        uExt:{value:ext0},uColor:{value:C(o.color===undefined?0xd6c6a6:o.color)}},
      vertexShader:NXZ_WAVE_VERT,fragmentShader:NXZ_WAVE_FRAG});
    const mesh=new THREE.Mesh(geo,m); mesh.frustumCulled=false; mesh.renderOrder=2;
    mesh.position.set((o.x===undefined?0:o.x)+(i-1)*2.4, (o.y===undefined?0:o.y)+i*0.28, (o.z===undefined?-40:o.z)+i*26);
    mesh.rotation.y=(o.ry===undefined?0.05:o.ry)+(i%2?-0.03:0.03);
    g.add(mesh); parts.push(m);
  }
  return {g,update(t){ for(let i=0;i<parts.length;i++)parts[i].uniforms.uTime.value=t+i*1.7; },
    setExt(v){ for(let i=0;i<parts.length;i++)parts[i].uniforms.uExt.value=Math.max(0.001,Math.min(1,v)); }};
}

/* —— 北固亭：台基+四柱+额枋+攒尖顶+顶珠+栏杆（合批 1 mesh，剪影靠轮廓与边缘光读出）—— */
function makeBeigu(o){
  o=o||{};
  const wood=o.color===undefined?0x1c130a:o.color, wood2=shadeColor(wood,1.7);
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(9,1.4,7); base.translate(0,0.7,0); B.put(base,shadeColor(wood,1.1));
  [[-3.3,-2.3],[3.3,-2.3],[-3.3,2.3],[3.3,2.3]].forEach(function(p){
    const c=new THREE.CylinderGeometry(0.20,0.25,4.6,8); c.translate(p[0],3.7,p[1]); B.put(c,wood2);
  });
  const beam=new THREE.BoxGeometry(8.8,0.5,6.4); beam.translate(0,6.25,0); B.put(beam,shadeColor(wood,1.3));
  const roof=new THREE.ConeGeometry(6.3,2.5,4); roof.rotateY(Math.PI/4); roof.translate(0,7.65,0); B.put(roof,shadeColor(wood,1.5));
  const orb=new THREE.SphereGeometry(0.42,10,8); orb.translate(0,9.15,0); B.put(orb,0x8a6a3a);
  const rl=new THREE.BoxGeometry(7.4,0.12,0.14); rl.translate(0,2.52,2.35); B.put(rl,wood2);
  for(let i=0;i<5;i++){
    const p=new THREE.BoxGeometry(0.13,1.0,0.13); p.translate(-3.4+i*1.7,2.0,2.35); B.put(p,wood);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a1c10,emissive:0x0a0704}),{c:0xc49a5a,i:o.rim===undefined?0.3:o.rim,p:2.6})));
  return g;
}

/* —— 战旗：旗杆+杆顶+暗赭战旗（旗面摆动，2 draw call）——「战未休」猎猎旗影 —— */
function makeZhanqi(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.08,0.11,h,6); pole.translate(0,h/2,0); B.put(pole,0x0b0806);
  const fin=new THREE.SphereGeometry(0.16,8,6); fin.translate(0,h+0.1,0); B.put(fin,0x6a5030);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc49a5a,i:0.2,p:2.6})));
  const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.7,1.7,5,2),
    new THREE.MeshPhongMaterial({color:o.flagC===undefined?0x6a2818:o.flagC,side:THREE.DoubleSide,
      shininess:6,specular:0x3a2418}));
  fl.position.set(1.35,h-1.15,0); g.add(fl);
  return {g,fl,ph,update(t){ fl.rotation.y=0.42*Math.sin(t*1.5+ph)+0.16*Math.sin(t*2.6+ph*1.7); }};
}

/* —— 枪林：一片斜竖的长枪（杆+铁簇，部分带缨，合批 1 mesh）——「万兜鍪」的军阵气 —— */
function makeQianglin(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19303:o.seed);
  const n=o.n===undefined?26:o.n, w=o.w===undefined?32:o.w, d=o.d===undefined?10:o.d;
  const y0=o.y===undefined?0:o.y;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const h=3.8+R()*1.7, x=(R()-0.5)*w, z=y0+d*0.5-R()*d;
    const tl=(R()-0.5)*0.22;
    const pole=new THREE.CylinderGeometry(0.035,0.05,h,5);
    pole.rotateZ(tl); pole.translate(x,h/2,z); B.put(pole,shadeColor(0x14100a,0.8+0.5*R()));
    const tip=new THREE.ConeGeometry(0.085,0.5,6);
    tip.rotateZ(tl); tip.translate(x+tl*h*0.42,h+0.24,z); B.put(tip,shadeColor(0x4a4438,0.8+0.5*R()));
    if(R()<0.5){
      const tassel=new THREE.ConeGeometry(0.14,0.42,6); tassel.rotateX(Math.PI); tassel.rotateZ(tl);
      tassel.translate(x+tl*(h-0.5)*0.42,h-0.62,z); B.put(tassel,shadeColor(0x7a2818,0.8+0.4*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a241a,emissive:0x040302}),{c:0xc49a5a,i:0.16,p:2.6})));
  return g;
}

/* —— 长枪：少年孙权手中提枪（挂到人物手位；作为人物 group 子对象随淡入淡出）—— */
function makeChangqiang(o){
  o=o||{};
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.042,0.055,7.0,7); pole.translate(0,0.2,0); B.put(pole,0x1a140c);
  const butt=new THREE.CylinderGeometry(0.075,0.075,0.22,7); butt.translate(0,-3.28,0); B.put(butt,0x3a3022);
  const tip=new THREE.ConeGeometry(0.10,0.62,7); tip.translate(0,3.96,0); B.put(tip,0x5a5448);
  const tassel=new THREE.ConeGeometry(0.17,0.52,7); tassel.rotateX(Math.PI); tassel.translate(0,3.52,0); B.put(tassel,0x7a2818);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a3022,emissive:0x050403}),{c:0xc49a5a,i:0.22,p:2.5})));
  g.rotation.z=o.rz===undefined?-0.13:o.rz; g.rotation.x=o.rx===undefined?0.05:o.rx;
  return g;
}

/* —— 遥帆：江上远影小舟（船身+桅+帆合批 1 mesh，随浪起伏漂移）——千古兴亡随帆去 —— */
function makeYaofan(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const hull=new THREE.LatheGeometry([[0,0.04],[0.5,0.04],[0.75,0.18],[0.82,0.4]]
    .map(p=>new THREE.Vector2(p[0],p[1])),10);
  hull.scale(0.75,0.5,2.1); B.put(hull,0x0c0806);
  const mast=new THREE.CylinderGeometry(0.05,0.07,2.6,6); mast.translate(0,1.5,0.2); B.put(mast,0x0a0705);
  const sail=new THREE.PlaneGeometry(1.5,2.0,3,3); sail.translate(0.72,1.85,0.22); B.put(sail,0x2a1c10);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x241a10,emissive:0x040302}),{c:0xc49a5a,i:0.2,p:2.6}));
  mesh.renderOrder=1;
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(sc);
  return {g,ph,x0:0,z0:0,y0:0,update(t){
    g.position.x=this.x0+2.4*Math.sin(t*0.07+ph);
    g.position.z=this.z0+1.6*Math.sin(t*0.05+ph*1.9);
    g.position.y=this.y0+0.13*Math.sin(t*0.8+ph);
    g.rotation.z=0.02*Math.sin(t*0.7+ph);
  }};
}

function bCoverNxz(){ // 封面 · 暮色大江上的北固亭剪影（尘霭低回，江流无声）
  const g=new THREE.Group();
  const water=makeWater({size:680,seg:88,amp:0.5,freq:0.08,speed:0.5,flow:[0,0.5],
    deep:0x120d08,shallow:0x241a10,skyc:0x3a2a18,spec:0.25,moonDir:[-0.55,0.14,-0.8],moonColor:0xb08858,y:-2.0});
  g.add(water.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:19301,color:0x0b0806,atmo:0x332414,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-16); g.add(ridge.g);
  /* 崖上北固亭剪影（暮霭里的「满眼风光」） */
  const cliff=new THREE.Group();
  const cb=new GeoBag();
  const r1=rockGeo(9,1,seedRnd(19305)); r1.scale(2.1,1.15,1.3); r1.translate(0,2.6,-26); cb.put(r1,0x0d0906);
  const r2=rockGeo(6,1,seedRnd(19307)); r2.scale(1.7,0.9,1.1); r2.translate(-9,1.9,-29); cb.put(r2,0x0b0805);
  const r3=rockGeo(6,1,seedRnd(19309)); r3.scale(1.8,1.0,1.2); r3.translate(9,2.1,-28); cb.put(r3,0x0c0906);
  cliff.add(cb.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc49a5a,i:0.12,p:2.8})));
  const pav=makeBeigu({}); pav.position.set(0,4.6,-26); pav.scale.setScalar(1.0); cliff.add(pav);
  g.add(cliff);
  const motes=makeGlow({n:50,box:[220,34,130],pos:[0,10,-40],color:0xc09a68,size:7,speed:0.05,rise:0,maxA:0.28});
  g.add(motes.points);
  const flow=makeFlow({n:130,box:[220,12,80],pos:[0,7,-30],color:0x9a7c50,size:15,speed:4.5,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:9,spread:[250,26,140],pos:[0,10,-54],scale:80,color:0x8a6f4e,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:48,n:13,d:6,color:0x0a0704,seed:19311,sway:0.9,tip:0x3a2c16});
  fg.g.position.set(0,-1.8,26); g.add(fg.g);
  /* 晚渡旅人：岸畔一行剪影（远景人迹） */
  const walker=makeFigure({pose:'独立',robe:0x1c150e,belt:0x4a3a24,hat:'幞头',scale:0.8,rim:0.5,rimC:0xc49a5a});
  walker.position.set(-11,-1.8,19); walker.rotation.y=0.4; g.add(walker);
  addLights(g,{c:0xc09058,i:0.36,p:[-40,60,30]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); motes.update(t); flow.update(t); mist.update(t,k);
    fg.update(t,k); walker.update(t,k);
  }};
}
function bWangshen(){ // 一 · 望断神州 —— 楼头凭栏北望：满眼风光，神州却望不见（怅惘）
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.5,freq:0.08,speed:0.55,flow:[0,0.8],
    deep:0x100c08,shallow:0x201810,skyc:0x2e2013,spec:0.22,moonDir:[-0.5,0.16,-0.85],moonColor:0xb08858,y:-5.0});
  g.add(water.mesh);
  const ridge=makeRange({r:340,h:16,layers:2,peaks:5,seed:19313,color:0x0a0705,atmo:0x302212,fogK:0.60,glowK:0.05,y:-18});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  /* 北固楼头：台面 + 亭柱一对 + 凭栏按剑北望的词人背影 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(30,2.6,14),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  tai.position.set(0,-0.3,-4); g.add(tai);
  const top=makeGround({r:12,c1:0x0e0a07,c2:0x16100a});
  top.mesh.position.set(0,1.05,-4); g.add(top.mesh);
  const pilL=makePillar({h:9,top:false}); pilL.g.position.set(-7,1.05,-1.5); g.add(pilL.g);
  const pilR=makePillar({h:9,top:false}); pilR.g.position.set(7.5,1.05,-2.2); g.add(pilR.g);
  const poet=makeFigure({pose:'按剑',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.35,rim:0.62,rimC:0xc49a5a});
  poet.position.set(2.0,1.05,-3.0); poet.rotation.y=Math.PI-0.22; g.add(poet);
  /* 「神州不可见」：北望方向一堵尘霭，压住远天远山 */
  const haze=makeMist({n:10,spread:[290,26,130],pos:[0,6,-95],scale:92,color:0x6a5c48,op:0.14});
  g.add(haze.g);
  const dust=makeFlow({n:200,box:[250,16,90],pos:[0,8,-72],color:0x5a5044,size:22,speed:5,maxA:0.22});
  g.add(dust.points);
  const motes=makeGlow({n:36,box:[200,26,100],pos:[0,10,-40],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.16});
  g.add(motes.points);
  const fg=makeForeground({kind:'栏杆',w:26,h:2.8,color:0x0d0906,seed:19315,rim:0.16,rimC:0xc49a5a});
  fg.g.position.set(0,1.0,3.6); g.add(fg.g);
  const rock=makeForeground({kind:'岩壁',n:3,r:4.2,w:16,d:7,color:0x0a0704,seed:19317,rim:0.12,rimC:0xc49a5a});
  rock.g.position.set(16,-5.4,20); g.add(rock.g);
  addLights(g,{c:0xa88658,i:0.32,p:[-50,60,-20]},{c:0x30251a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); haze.update(t,k); dust.update(t); motes.update(t);
    fg.update(t,k); rock.update(t,k); poet.update(t,k);
  }};
}
function bChangjiang(){ // 二（标志性瞬间）· 不尽长江 —— 亭上凭栏：千叠浪滚滚东去，答千古一问
  const g=new THREE.Group();
  const water=makeWater({size:900,seg:96,amp:0.62,freq:0.075,speed:0.9,flow:[0,1.6],
    deep:0x100c08,shallow:0x241a10,skyc:0x34281a,spec:0.30,moonDir:[-0.5,0.16,-0.85],moonColor:0xb08858,y:-1.8});
  g.add(water.mesh);
  const lang=makeLangdie({bands:4,len:300,w:15,amp:0.58,maxA:0.44,ext:1,z:-40,y:-1.0,ry:0.05,color:0xd6c6a6});
  g.add(lang.g);
  const ridge=makeRange({r:360,h:20,layers:2,peaks:5,seed:19319,color:0x0a0705,atmo:0x3a2a18,fogK:0.58,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-40); g.add(ridge.g);
  /* 亭上凭栏：词人背影独立楼头，栏与柱框住大江 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(26,2.4,12),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  tai.position.set(0,0.8,-2); g.add(tai);
  const top=makeGround({r:12,c1:0x0e0a07,c2:0x16100a});
  top.mesh.position.set(0,2.05,-2); g.add(top.mesh);
  const pilL=makePillar({h:9,top:false}); pilL.g.position.set(-8.5,2.05,1.0); g.add(pilL.g);
  const pilR=makePillar({h:9,top:false}); pilR.g.position.set(8.5,2.05,2.0); g.add(pilR.g);
  const poet=makeFigure({pose:'独立',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.35,rim:0.58,rimC:0xc49a5a});
  poet.position.set(-5.5,2.05,-0.5); poet.rotation.y=Math.PI+0.38; g.add(poet);
  /* 千帆远影：兴亡旧事随江去 */
  const boats=[[-34,-70,1.25],[26,-96,1.6]].map(function(b){
    const bf=makeYaofan({scale:b[2],ph:b[0]}); bf.x0=b[0]; bf.z0=b[1]; bf.y0=-1.6;
    bf.g.position.set(b[0],-1.6,b[1]); bf.g.rotation.y=0.12; g.add(bf.g); return bf;
  });
  const mist=makeMist({n:9,spread:[300,20,120],pos:[0,6,-92],scale:88,color:0x8a7454,op:0.12});
  g.add(mist.g);
  const flow=makeFlow({n:240,box:[280,10,150],pos:[0,2,-60],color:0x8a6f4c,size:20,speed:6,maxA:0.15});
  g.add(flow.points);
  const motes=makeGlow({n:40,box:[240,24,110],pos:[0,8,-50],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.16});
  g.add(motes.points);
  const fg=makeForeground({kind:'栏杆',w:30,h:2.9,color:0x0d0906,seed:19321,rim:0.18,rimC:0xc49a5a});
  fg.g.position.set(0,2.0,4.2); g.add(fg.g);
  addLights(g,{c:0xc09058,i:0.40,p:[-60,70,10]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); lang.update(t); ridge.update(t,0);
    for(let i=0;i<boats.length;i++)boats[i].update(t);
    mist.update(t,k); flow.update(t); motes.update(t);
    fg.update(t,k); poet.update(t,k);
  }};
}
function bZuoduan(){ // 三 · 坐断东南 —— 少年孙权提枪点兵：万兜鍪、战旗猎猎、烽火不熄（昂扬）
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.5,freq:0.08,speed:0.6,flow:[0,0.7],
    deep:0x0f0c08,shallow:0x201810,skyc:0x2e2013,spec:0.28,moonDir:[-0.6,0.18,-0.8],moonColor:0xc8a070,y:-2.2});
  g.add(water.mesh);
  const ridge=makeRange({r:340,h:18,layers:2,peaks:5,seed:19323,color:0x0a0705,atmo:0x332414,fogK:0.60,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  /* 点兵城头：台面 + 少年孙权（提枪英姿，指月位的手擎长枪） */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(34,2.6,16),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  tai.position.set(0,-0.3,-6); g.add(tai);
  const top=makeGround({r:14,c1:0x0e0a07,c2:0x181009});
  top.mesh.position.set(0,1.05,-6); g.add(top.mesh);
  const sunQuan=makeFigure({pose:'指月',robe:0x2c241c,belt:0x9a6a2e,hat:'幞头',scale:1.5,rim:0.75,rimC:0xc49a5a});
  sunQuan.position.set(0,1.05,-3.2); sunQuan.rotation.y=Math.PI-0.5;
  const qiang=makeChangqiang({}); qiang.position.set(0.98,3.66,0.26); sunQuan.add(qiang);
  g.add(sunQuan);
  /* 万兜鍪：军阵两列 + 枪林一片 */
  const army1=makeCrowd({n:44,rect:[-17,-15,34,11],color:0x1a140e,rimC:0xc49a5a,rim:0.26,sMin:0.88,sMax:1.12,y:1.05,seed:19325});
  g.add(army1.mesh);
  const army2=makeCrowd({n:18,rect:[-15,-4,30,6],color:0x16110c,rimC:0xc49a5a,rim:0.24,sMin:0.86,sMax:1.08,y:1.05,seed:19327});
  g.add(army2.mesh);
  const qlin=makeQianglin({n:26,w:32,d:10,y:1.05,seed:19329}); qlin.position.set(0,0,-9); g.add(qlin);
  /* 战旗猎猎 + 烽火不熄 */
  const flags=[];
  [[-12,-9,7.2,0],[-5,-12,6.6,1.9],[7,-11,7.4,3.1],[13,-8,6.4,4.4]].forEach(function(fp){
    const f=makeZhanqi({h:fp[2],ph:fp[3]});
    f.g.position.set(fp[0],1.05,fp[1]); g.add(f.g); flags.push(f);
  });
  const bz1=makeBrazier({r:0.9,fh:2.4,fw:1.2,light:1.4,lightD:44,embers:34});
  bz1.g.position.set(-3.5,1.05,1.5); g.add(bz1.g);
  const bz2=makeBrazier({r:0.8,fh:2.2,fw:1.1,light:1.2,lightD:40,embers:30});
  bz2.g.position.set(4.5,1.05,2.2); g.add(bz2.g);
  const dust=makeFlow({n:220,box:[240,14,90],pos:[0,8,-58],color:0x8a6f4c,size:18,speed:5,maxA:0.16});
  g.add(dust.points);
  const mist=makeMist({n:8,spread:[240,20,110],pos:[0,8,-64],scale:78,color:0x8a6f4e,op:0.10});
  g.add(mist.g);
  /* 前景：水畔坡石与芦苇框景 */
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:11,d:6,color:0x0b0805,seed:19331,rim:0.12,rimC:0xc49a5a});
  rk.g.position.set(14,-1.6,15); g.add(rk.g);
  const fg=makeForeground({kind:'芦苇',w:26,n:9,d:5,color:0x0a0704,seed:19333,sway:1.0,tip:0x3a2c16});
  fg.g.position.set(-14,-1.9,18); g.add(fg.g);
  addLights(g,{c:0xd0a060,i:0.50,p:[-60,50,-30]},{c:0x3a2c1c,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0);
    army1.update(t); army2.update(t);
    for(let i=0;i<flags.length;i++)flags[i].update(t);
    bz1.update(t,k); bz2.update(t,k);
    dust.update(t); mist.update(t,k);
    rk.update(t,k); fg.update(t,k); sunQuan.update(t,k);
  }};
}
function bZhongmou(){ // 四（末境·可点击）· 生子仲谋 —— 亭头远望：点击北固亭，江浪千叠答千古一问
  const ctl={t:0,clicked:false,ext:0,lastSong:0};
  const g=new THREE.Group();
  const water=makeWater({size:800,seg:96,amp:0.55,freq:0.08,speed:0.75,flow:[0,1.0],
    deep:0x100c08,shallow:0x221810,skyc:0x302212,spec:0.22,moonDir:[-0.55,0.16,-0.83],moonColor:0xb08858,y:-1.6});
  g.add(water.mesh);
  const lang=makeLangdie({bands:3,len:280,w:17,amp:0.6,maxA:0.5,ext:0.001,z:-2,y:-1.2,ry:-0.04,color:0xd6c6a6});
  g.add(lang.g);
  const ridge=makeRange({r:340,h:18,layers:2,peaks:5,seed:19335,color:0x0a0705,atmo:0x302212,fogK:0.60,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-34); g.add(ridge.g);
  /* 江崖上的北固亭 + 亭头凭栏北望的词人背影（楼头远望） */
  const cliff=new THREE.Group();
  const cb=new GeoBag();
  const r1=rockGeo(9,1,seedRnd(19337)); r1.scale(2.2,1.25,1.4); r1.translate(0,3.4,-28); cb.put(r1,0x0c0906);
  const r2=rockGeo(6,1,seedRnd(19339)); r2.scale(1.8,0.95,1.2); r2.translate(-9.5,2.4,-31); cb.put(r2,0x0b0805);
  const r3=rockGeo(6,1,seedRnd(19341)); r3.scale(1.9,1.05,1.3); r3.translate(10,2.6,-30); cb.put(r3,0x0c0906);
  const top=new THREE.BoxGeometry(15,1.2,9); top.translate(0.5,6.0,-28); cb.put(top,0x0e0a07);
  cliff.add(cb.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc49a5a,i:0.14,p:2.8})));
  const pav=makeBeigu({}); pav.position.set(0.5,6.6,-28); pav.scale.setScalar(1.1); cliff.add(pav);
  const poet=makeFigure({pose:'按剑',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:0.8,rim:0.55,rimC:0xc49a5a});
  poet.position.set(0.5,6.6,-26.9); poet.rotation.y=Math.PI; cliff.add(poet);
  const flags=[];
  [[-5.5,5.2,0],[6,5.0,2.2]].forEach(function(fp){
    const f=makeZhanqi({h:fp[1],ph:fp[2],flagC:0x4a2014});
    f.g.position.set(fp[0],6.6,-30.5); cliff.add(f.g); flags.push(f);
  });
  g.add(cliff);
  const mist=makeMist({n:8,spread:[240,20,110],pos:[0,7,-40],scale:80,color:0x7a674c,op:0.11});
  g.add(mist.g);
  const flow=makeFlow({n:160,box:[230,14,90],pos:[0,6,-32],color:0x8a7454,size:16,speed:4.5,maxA:0.12});
  g.add(flow.points);
  const fgL=makeForeground({kind:'芦苇',w:40,n:12,d:6,color:0x120c05,seed:19343,sway:1.1,tip:0x3a2e18});
  fgL.g.position.set(-11,-1.4,18); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:30,n:9,d:5,color:0x0f0a04,seed:19345,sway:0.9,tip:0x362a16});
  fgR.g.position.set(12,-1.7,20); g.add(fgR.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:11,d:6,color:0x0b0805,seed:19347,rim:0.10,rimC:0xc49a5a});
  rk.g.position.set(-16,-2.2,12); g.add(rk.g);
  addLights(g,{c:0xb08858,i:0.34,p:[-40,55,-15]},{c:0x32271a,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.ext=Math.min(1,ctl.ext+dt/3.2);
        if(t-ctl.lastSong>6.5){ ctl.lastSong=t; pluck(2,0,0.06); pluck(5,0.55,0.05); } // 江声余韵
      }
      const e=ctl.ext*(2-ctl.ext); // easeOut
      lang.setExt(0.001+0.999*e);
      water.update(t); lang.update(t); ridge.update(t,0);
      mist.update(t,k); flow.update(t);
      fgL.update(t,k); fgR.update(t,k); rk.update(t,k);
      poet.update(t,k);
      for(let i=0;i<flags.length;i++)flags[i].update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.0,0.10); pluck(2,0.35,0.09); pluck(4,0.7,0.09); pluck(5,1.05,0.08); // 江浪千叠，和声作答
        const fl=$('#flash'); fl.textContent='生子当如孙仲谋'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
