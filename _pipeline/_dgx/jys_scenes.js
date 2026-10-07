/* ================= 静夜思 · 四境场景（水墨夜思：冷银月色 + 月光穿窗成柱 + 霜满地 + 故乡灯火） ================= */

/* 标志性瞬间 · 月光穿窗成柱：交叉两片的冷银光柱（自定雾约定 uFade 交给 setFade） */
const JYS_SHAFT_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; uniform vec3 uC; varying vec2 vUv;
void main(){
  float x=abs(vUv.x-0.5)*2.0;
  float core=1.0-smoothstep(0.0,0.62,x);
  float a=uFade*uK*(0.85+0.15*sin(uTime*1.3))
    *pow(clamp(1.0-vUv.y,0.0,1.0),1.25)          // 落点最亮，向上渐消
    *smoothstep(0.0,0.30,vUv.x)*(1.0-smoothstep(0.70,1.0,vUv.x));
  gl_FragColor=vec4(uC,a);
}`;
function makeLightShaft(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, h=o.h===undefined?70:o.h;
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.k===undefined?0.5:o.k},
      uC:{value:C(o.color===undefined?0xdce8fb:o.color)}},
    vertexShader:'varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }',
    fragmentShader:JYS_SHAFT_FRAG});
  const B=new GeoBag();
  for(let i=0;i<2;i++){
    const p=new THREE.PlaneGeometry(w,h,1,1); p.translate(0,h*0.28,0); p.rotateY(i*Math.PI/2);
    B.put(p,0xffffff);
  }
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat);
  mesh.renderOrder=4; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.userData.mat=mat;
  g.update=function(t,fk){ const k=fk===undefined?1:fk; mat.uniforms.uTime.value=t; mat.uniforms.uFade.value=k; };
  return {g,mat,update:g.update};
}

/* 硬山墙 + 窗洞 + 窗棂：后墙 4 段合批 1 mesh，窗棂 1 mesh（月光从窗洞进来） */
function makeWallWin(o){
  o=o||{};
  const wallC=o.wall===undefined?0x10141d:o.wall, latC=o.lattice===undefined?0x090c14:o.lattice;
  const g=new THREE.Group();
  const BW=new GeoBag();
  [[-14.5,15,11,30],[14.5,15,11,30],[0,4,40,8],[0,26,40,8]].forEach(function(w){
    const b=new THREE.BoxGeometry(w[2],w[3],1.2); b.translate(w[0],w[1],0); BW.put(b,shadeColor(wallC,0.9+0.2*Math.abs(Math.sin(w[0]))));
  });
  const wall=BW.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:5,specular:0x1d2434,emissive:0x04050a}),{c:o.rimC===undefined?0x8fa8cc:o.rimC,i:0.14,p:2.4}));
  wall.position.z=-16; wall.frustumCulled=false; g.add(wall);
  const LW=new GeoBag();
  [-6,-3,0,3,6].forEach(function(x){
    const b=new THREE.BoxGeometry(0.35,14,0.5); b.translate(x,15,0); LW.put(b,latC);
  });
  const hb=new THREE.BoxGeometry(18,0.35,0.5); hb.translate(0,15,0); LW.put(hb,latC);
  const sill=new THREE.BoxGeometry(20,0.9,2.4); sill.translate(0,7.6,0.8); LW.put(sill,shadeColor(latC,1.5));
  const lat=LW.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:8,specular:0x2a3648,emissive:0x03040a}),{c:o.rimC===undefined?0x8fa8cc:o.rimC,i:0.18,p:2.4}));
  lat.position.z=-15.6; lat.frustumCulled=false; g.add(lat);
  return {g};
}

/* 床榻：榻身 + 褥 + 枕 + 双柱（合批 1 mesh，水墨暗木） */
function makeBed(o){
  o=o||{};
  const wood=o.wood===undefined?0x1b202c:o.wood;
  const B=new GeoBag();
  const frame=new THREE.BoxGeometry(11,1.4,7.5); frame.translate(0,0.7,0); B.put(frame,wood);
  const mat2=new THREE.BoxGeometry(10.4,0.8,6.9); mat2.translate(0,1.8,0); B.put(mat2,0x252b3a);
  const pil=new THREE.BoxGeometry(2.6,0.8,4.4); pil.translate(4.1,2.5,0); B.put(pil,0x39435a);
  [[-4.1,-2.8],[4.1,2.8]].forEach(function(p){
    const post=new THREE.CylinderGeometry(0.28,0.32,9,8); post.translate(p[0],4.5,p[1]); B.put(post,shadeColor(wood,0.8));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:12,specular:0x2a3648,emissive:0x05070c}),{c:o.rimC===undefined?0x9db8dd:o.rimC,i:0.20,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 青灯：灯杆 + 冷银灯焰 Sprite + 一点微光（返回 {g,update}，闪烁系数 ≤1） */
function makeLampCold(o){
  o=o||{};
  const g=new THREE.Group();
  const stick=new THREE.Mesh(new THREE.CylinderGeometry(0.18,0.26,2.6,8),
    new THREE.MeshPhongMaterial({color:0x272e3d,shininess:24,specular:0x3a4c66}));
  stick.position.y=1.3; g.add(stick);
  const fm=new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0xaac6ea:o.color,
    transparent:true,opacity:0.70,depthWrite:false,blending:THREE.AdditiveBlending});
  const flame=new THREE.Sprite(fm); flame.scale.set(2.2,3.2,1); flame.position.y=3.2; flame.renderOrder=2;
  g.add(flame);
  const lt=new THREE.PointLight(o.light===undefined?0x9db9df:o.light,0.8,o.dist===undefined?44:o.dist);
  lt.position.y=3.4; g.add(lt);
  return {g,update(t,fk){ const k=fk===undefined?1:fk;
    fm.opacity=k*0.70*(0.86+0.14*Math.sin(t*11));
    flame.scale.y=3.2+Math.sin(t*11)*0.3;
    lt.intensity=k*0.8*(0.88+0.08*Math.sin(t*9.1)+0.04*Math.sin(t*23.7));
  }};
}

function bCover(){ // 卷首 · 静夜庭院：冷银夜空一弯月，微尘浮雾，树枝框景
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0a0e16,c2:0x121926,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:30,layers:3,peaks:5,seed:41,color:0x0b111d,atmo:0x1d2836,
    fogK:0.62,glowK:0.05,glow:0xc9d8ee,y:-12});
  ridge.g.position.set(0,0,-70); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const mist=makeMist({n:10,spread:[280,36,160],pos:[0,12,-60],scale:88,color:0x8fa4c8,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:120,box:[220,44,140],pos:[0,16,-40],color:0xbfd4f2,size:4.6,speed:0.028,
    rise:0,add:true,maxA:0.30});
  g.add(motes.points);
  const brL=makeForeground({kind:'树枝',w:56,n:10,d:7,color:0x05080e,seed:9,sway:0.7,rim:0.12,rimC:0x9db8dd});
  brL.g.position.set(-30,-1.5,46); brL.g.scale.setScalar(2.2); g.add(brL.g);
  const brR=makeForeground({kind:'树枝',w:44,n:8,d:6,color:0x05080e,seed:17,sway:0.6,rim:0.12,rimC:0x9db8dd});
  brR.g.position.set(27,-1.5,40); brR.g.scale.setScalar(1.8); g.add(brR.g);
  addLights(g,{c:0xbccbe4,i:0.5,p:[40,120,-60]},{c:0x2a3550,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); brL.update(t,k); brR.update(t,k);
  }};
}
function bBedroom(){ // 一 · 床前月光 —— 标志性瞬间：月光穿窗成柱，如练斜落床前
  const g=new THREE.Group();
  const grd=makeGround({r:90,c1:0x0c101a,c2:0x141a28,y:0}); g.add(grd.mesh);
  /* 背景：窗外月下远山（从窗洞望出去的层次） */
  const ridge=makeRange({r:200,h:46,layers:2,peaks:5,seed:51,color:0x0b111d,atmo:0x1d2836,
    fogK:0.66,glowK:0.04,glow:0xc9d8ee,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 后墙 + 窗洞 + 窗棂（窗洞 x -9..9，y 8..22） */
  const ww=makeWallWin({}); g.add(ww.g);
  /* 床榻（画面右侧，水墨暗木） */
  const bed=makeBed({}); bed.position.set(9.5,0,5); g.add(bed);
  /* 月光光柱：冷银如练，自窗口斜落床前（底端落在光池，顶端探入窗洞） */
  const shaft=makeLightShaft({w:13,h:18,k:0.5,color:0xdce8fb});
  shaft.g.position.set(1,5.2,-8); shaft.g.rotation.x=-1.02; g.add(shaft.g);
  /* 床前光池 + 辉光（构造值=运行期最大值，update 只乘系数） */
  const poolMat=new THREE.MeshBasicMaterial({color:0xbfd4ee,transparent:true,opacity:0.42,
    blending:THREE.AdditiveBlending,depthWrite:false});
  const pool=new THREE.Mesh(new THREE.CircleGeometry(5.4,36),poolMat);
  pool.rotation.x=-Math.PI/2; pool.position.set(1.5,0.07,-1.5); pool.renderOrder=1; g.add(pool);
  const hm=new THREE.SpriteMaterial({map:glowTex(),color:0xa8c2e8,transparent:true,opacity:0.30,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const halo=new THREE.Sprite(hm); halo.scale.set(15,7,1); halo.position.set(1.5,1.2,-1.5); halo.renderOrder=2;
  g.add(halo);
  /* 光柱浮尘（微尘母题，冷银） */
  const motes=makeGlow({n:70,box:[8,13,7],pos:[1,5.5,-8],color:0xdce8ff,size:5.5,speed:0.03,
    rise:0,add:true,maxA:0.5});
  g.add(motes.points);
  /* 屋角一盏青灯（冷银微光，不夺月色） */
  const lamp=makeLampCold({}); lamp.g.position.set(-15.5,0,4); g.add(lamp.g);
  /* 前景：床前低栏（框住画面左下缘） */
  const rail=makeForeground({kind:'栏杆',w:18,h:3.0,color:0x0a0d15,seed:5,rim:0.14,rimC:0x9db8dd});
  rail.g.position.set(-11,0,16); g.add(rail.g);
  addLights(g,{c:0xc0d2ec,i:0.5,p:[10,90,-70]},{c:0x2a3550,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); shaft.update(t,k); motes.update(t); lamp.update(t,k); rail.update(t,k);
    poolMat.opacity=k*(0.36+0.06*Math.sin(t*0.8));
    hm.opacity=k*0.30*(0.86+0.14*Math.sin(t*0.9));
    shaft.mat.uniforms.uK.value=0.5*(0.85+0.15*Math.sin(t*0.6));
  }};
}
function bFrost(){ // 二 · 疑是清霜 —— 俯身看地，月光的池子化作满地霜斑霜晶
  const g=new THREE.Group();
  const grd=makeGround({r:100,c1:0x0d121d,c2:0x161d2b,y:0}); g.add(grd.mesh);
  /* 背景：院墙外月下远山一线 */
  const ridge=makeRange({r:220,h:40,layers:3,peaks:5,seed:61,color:0x0b111d,atmo:0x1d2836,
    fogK:0.64,glowK:0.04,glow:0xc9d8ee,y:-6});
  ridge.g.position.set(0,0,-90); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 床沿一角（右前景剪影） */
  const bed=makeBed({scale:0.9}); bed.position.set(12.5,0,7); bed.rotation.y=-0.3; g.add(bed);
  /* 霜斑（如薄雪覆地，微微呼吸；构造值=最大值） */
  const patches=[];
  [[0,-3,9.5],[1,-2,6.2],[-8,3,4.4],[8,-6,5.0],[3,8,3.4],[-4,-10,3.0],[11,3,2.6],[-13,-4,2.4]].forEach(function(p,i){
    const m=new THREE.Mesh(new THREE.CircleGeometry(p[2],22),
      new THREE.MeshBasicMaterial({color:0xdfe9f8,transparent:true,opacity:0.22,
        blending:THREE.AdditiveBlending,depthWrite:false}));
    m.rotation.x=-Math.PI/2; m.position.set(p[0],0.05+i*0.012,p[1]); m.renderOrder=1;
    g.add(m); patches.push({m,ph:i*1.7});
  });
  /* 霜晶闪烁（贴地细密冷银微粒 + 一层柔光，宁少勿糊） */
  const crys=makeGlow({n:220,box:[36,2.0,30],pos:[0,0.6,-5],color:0xe8f2ff,size:2.0,speed:0.05,
    rise:0,add:true,maxA:0.32});
  const soft=makeGlow({n:70,box:[46,2,34],pos:[0,0.5,-6],color:0xaac8ee,size:4.5,speed:0.02,
    rise:0,add:true,maxA:0.16});
  g.add(crys.points,soft.points);
  /* 贴地薄雾 */
  const mist=makeMist({n:10,spread:[76,5,54],pos:[0,1.8,-6],scale:26,color:0xaac4e8,op:0.14});
  g.add(mist.g);
  /* 一点霜夜微光 */
  const pl=new THREE.PointLight(0x9fc0ee,0.7,60); pl.position.set(0,5,-4); g.add(pl);
  /* 前景：庭院太湖石坡石（框住画面左缘） */
  const rk=makeForeground({kind:'坡石',n:3,r:2.6,w:12,d:5,color:0x0a0d15,seed:63,rim:0.14,rimC:0x9db8dd});
  rk.g.position.set(-8,-0.4,10); g.add(rk.g);
  addLights(g,{c:0x9db8e8,i:0.45,p:[15,100,-70]},{c:0x2a3450,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); crys.update(t); soft.update(t); mist.update(t,k); rk.update(t,k);
    pl.intensity=k*0.7*(0.9+0.1*Math.sin(t*0.9));
    patches.forEach(function(p){ p.m.material.opacity=k*(0.16+0.06*Math.sin(t*0.7+p.ph)); });
  }};
}
function bLookUp(){ // 三 · 举头望月 —— 镜头自地面仰起，人影指月，直指天心一轮冷银
  const g=new THREE.Group();
  const grd=makeGround({r:100,c1:0x0c101a,c2:0x131a28,y:0}); g.add(grd.mesh);
  /* 背景：地平线上淡淡山脊（镜头抬起后压在画面下缘） */
  const ridge=makeRange({r:240,h:34,layers:2,peaks:5,seed:71,color:0x0b111d,atmo:0x1d2836,
    fogK:0.68,glowK:0.04,glow:0xc9d8ee,y:-12});
  ridge.g.position.set(0,0,-120); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 廊柱一角（右侧剪影，从画缘立起，不遮月） */
  const B=new GeoBag();
  const col=new THREE.CylinderGeometry(0.8,1.0,24,10); col.translate(15,12,0); B.put(col,0x11141d);
  const plinth=new THREE.BoxGeometry(3.4,1.1,3.4); plinth.translate(15,0.55,0); B.put(plinth,0x0d1119);
  const eaveM=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x2a3648,emissive:0x04050a}),{c:0x8fa8cc,i:0.16,p:2.4}));
  eaveM.position.z=-14; eaveM.frustumCulled=false; g.add(eaveM);
  /* 举头望月的人影（左侧，指月姿，面朝天心明月） */
  const fig=makeFigure({pose:'指月',robe:0x252c3c,belt:0x7d8aa5,collar:0xcdd6e4,hat:'发髻',beard:true,
    scale:1.25,rim:0.5,rimC:0xc9d8ee});
  fig.position.set(-5.5,0,-2); fig.rotation.y=1.35; g.add(fig);
  /* 流云（水墨留白，月前缓移） */
  const clouds=makeMist({n:9,spread:[190,30,50],pos:[0,100,-190],scale:55,color:0x8094bc,op:0.13});
  g.add(clouds.g);
  /* 云缕剪影（一两缕暗云掠过月前） */
  const wisps=[];
  [[-38,96,-158,88,10,0],[26,116,-168,66,8,2.3]].forEach(function(w){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x0b111c,
      transparent:true,opacity:0.42,depthWrite:false}));
    s.scale.set(w[3],w[4],1); s.position.set(w[0],w[1],w[2]); s.renderOrder=4;
    g.add(s); wisps.push({s,baseX:w[0],ph:w[5]});
  });
  /* 月华微尘（冷银，缓缓浮游） */
  const dust=makeGlow({n:120,box:[130,80,50],pos:[0,90,-165],color:0xbfd8ff,size:8,speed:0.03,
    rise:0,add:true,maxA:0.4});
  g.add(dust.points);
  /* 前景：檐下树枝（框住画面右缘） */
  const br=makeForeground({kind:'树枝',w:40,n:10,d:5,color:0x05080e,seed:91,sway:0.8,rim:0.16,rimC:0x9db8dd});
  br.g.position.set(16,0,8); br.g.scale.setScalar(1.6); g.add(br.g);
  addLights(g,{c:0xbcd2f2,i:0.75,p:[0,120,-80]},{c:0x2c3a58,i:0.5});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); clouds.update(t,k); dust.update(t); br.update(t,k); fig.update(t,k);
    clouds.g.position.x=Math.sin(t*0.05)*16;
    wisps.forEach(function(w){ w.s.position.x=w.baseX+Math.sin(t*0.04+w.ph)*20; });
  }};
}
function bHomesick(){ // 四（末境·可点击）· 低头思乡 —— 标志性瞬间：点击逐盏点亮故乡灯火
  const g=new THREE.Group();
  const ctl={t:0,cool:99,firedAt:-1,clicked:false};
  const grd=makeGround({r:150,c1:0x0a0e16,c2:0x111726,y:0}); g.add(grd.mesh);
  /* 背景：天际月下远山（故乡在山外山） */
  const ridge=makeRange({r:260,h:44,layers:3,peaks:6,seed:81,color:0x0b111d,atmo:0x1d2836,
    fogK:0.66,glowK:0.04,glow:0xc9d8ee,y:-10});
  ridge.g.position.set(0,0,-210); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 故乡土坡（远山前一方缓坡，村舍落在坡上） */
  const hill=new THREE.Mesh(new THREE.ConeGeometry(90,26,24),
    new THREE.MeshPhongMaterial({color:0x060a12,shininess:4,specular:0x1d2434}));
  hill.position.set(0,13,-165); hill.scale.z=0.45; g.add(hill);
  /* 村舍剪影：7 座合批 1 mesh（点灯前是暗剪影） */
  const R=seedRnd(15);
  const HB=new GeoBag();
  [[-46,4.2,-140],[-28,12.9,-152],[-10,12.1,-146],[8,17.6,-155],[26,11.4,-148],[44,4.5,-140],[-2,23.2,-166]]
  .forEach(function(s){
    const body=new THREE.BoxGeometry(6,4.6,5); body.rotateY(R()*0.8-0.4); body.translate(s[0],s[1]+2.3,s[2]);
    HB.put(body,shadeColor(0x0a0f18,0.8+R()*0.4));
    const roof=new THREE.ConeGeometry(4.9,3,4); roof.rotateY(Math.PI/4+R()*0.8-0.4);
    roof.translate(s[0],s[1]+6.1,s[2]); HB.put(roof,shadeColor(0x0a0f18,0.6+R()*0.3));
  });
  const houses=HB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:5,specular:0x1d2434,emissive:0x03050a}));
  houses.frustumCulled=false; g.add(houses);
  /* 故乡灯火：每舍一盏暖橙 Sprite（唯一暖色点，「思」的温度；构造 opacity=运行期最大值） */
  const lamps=[];
  [[-46,4.2,-140],[-28,12.9,-152],[-10,12.1,-146],[8,17.6,-155],[26,11.4,-148],[44,4.5,-140],[-2,23.2,-166]]
  .forEach(function(s,i){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:0xffc27a,transparent:true,opacity:0.9,
      depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
    const sp=new THREE.Sprite(m);
    sp.scale.set(12,12,1); sp.position.set(s[0],s[1]+2.4,s[2]+2.8); sp.renderOrder=2;
    g.add(sp); lamps.push({m,delay:i*0.26,k:0});
  });
  /* 暖光：随灯火点亮而亮起（构造 intensity=最大值，update 只乘系数） */
  const pl=new THREE.PointLight(0xffa95c,1.6,120); pl.position.set(0,10,-150); g.add(pl);
  /* 忆中人影：村口远近几枚（远景人影，1 draw call） */
  const crowd=makeCrowd({n:6,rect:[-38,-150,76,10],seed:21,color:0x0d1420,rimC:0x8fa8cc,rim:0.12,
    sMin:0.5,sMax:0.8});
  g.add(crowd.mesh);
  /* 月光微尘与薄雾（冷银；暖色只留给故乡灯火） */
  const flies=makeGlow({n:60,box:[100,16,70],pos:[0,5,-45],color:0xaebfd9,size:6.5,speed:0.04,
    rise:0,add:true,maxA:0.4});
  g.add(flies.points);
  const mist=makeMist({n:10,spread:[220,26,90],pos:[0,8,-70],scale:60,color:0x8fa4c4,op:0.10});
  g.add(mist.g);
  /* 低头人影（中景，独立姿微俯） */
  const fig=makeFigure({pose:'独立',robe:0x20283a,belt:0x7d8aa5,collar:0xcdd6e4,hat:'发髻',beard:true,
    scale:1.5,rim:0.5,rimC:0xc9d8ee});
  fig.position.set(0,0,13); fig.rotation.y=Math.PI; fig.rotation.x=0.06; g.add(fig);
  /* 前景：坡石（框住画面右下缘） */
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x05080e,seed:83,rim:0.12,rimC:0x9db8dd});
  rk.g.position.set(14,-1.5,26); g.add(rk.g);
  addLights(g,{c:0xbcc9de,i:0.4,p:[0,80,-40]},{c:0x2b3246,i:0.55});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt; ctl.cool+=dt;
      ridge.update(t,0); flies.update(t); mist.update(t,k); rk.update(t,k); fig.update(t,k);
      crowd.update(t);
      let acc=0;
      if(ctl.firedAt>=0){
        const e=ctl.t-ctl.firedAt;
        lamps.forEach(function(L){
          L.k=sstep(0.12+L.delay,0.95+L.delay,e); acc+=L.k;
        });
      }
      lamps.forEach(function(L){ L.m.opacity=k*0.9*L.k; });   // 满亮基座 × 点亮系数（未点亮时为 0）
      pl.intensity=k*1.6*(acc/lamps.length);           // 满亮基座 × 平均点亮系数
    },click(){
      if(ctl.cool<1.2)return;
      ctl.cool=0;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        ctl.firedAt=ctl.t;                             // 启动逐盏点亮序列
        pluck(2,0,0.16); pluck(5,0.35,0.11); pluck(0,0.95,0.09);
        const fl=$('#flash'); fl.textContent='低头思故乡'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }else pluck(4,0,0.10);                           // 再点：一声轻拨
    },clicked:false};
  return api;
}
