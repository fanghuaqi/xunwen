/* ================= 破阵子·为陈同甫赋壮词以寄之 · 四境场景（大漠金戈·壮词变体：挑灯看剑、沙场点兵、的卢霹雳、白发生叹） ================= */

/* 旌旗：横杆下悬挂的旗面（底边摆幅最大），军阵气象 */
const BANNER_VERT=`
uniform float uTime; varying vec2 vUv;
void main(){ vUv=uv; vec3 p=position;
  float k=pow(1.0-uv.y,1.35);
  p.z+=sin(uTime*2.2+uv.x*4.8)*0.36*k;
  p.x+=sin(uTime*1.5+uv.x*3.1)*0.09*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0); }`;
const BANNER_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade; varying vec2 vUv;
void main(){
  vec3 c=mix(uC,uTipC,pow(clamp(vUv.x,0.0,1.0),1.2));
  gl_FragColor=vec4(c,uFade*(0.95-0.22*vUv.x)); }`;
function makeBanner(o){
  o=o||{};
  const w=o.w===undefined?2.8:o.w, h=o.h===undefined?3.6:o.h, ph=o.poleH===undefined?9:o.poleH;
  const g=new THREE.Group();
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.055,0.085,ph,6); pole.translate(0,ph/2,0); B.put(pole,0x160f0a);
  const bar=new THREE.CylinderGeometry(0.035,0.035,w*0.7,5); bar.rotateZ(Math.PI/2); bar.translate(w*0.32,ph,0); B.put(bar,0x160f0a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x060403}),{c:0xc0784a,i:0.26,p:2.4})));
  const geo=new THREE.PlaneGeometry(w,h,10,3); geo.translate(0,-h/2,0);
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,depthWrite:false,
    uniforms:{uTime:{value:0},uC:{value:C(o.color===undefined?0x701e12:o.color)},
      uTipC:{value:C(o.tip===undefined?0xc85a38:o.tip)},uFade:{value:1}},
    vertexShader:BANNER_VERT,fragmentShader:BANNER_FRAG});
  const mesh=new THREE.Mesh(geo,mt); mesh.position.set(w*0.32,ph,0); mesh.renderOrder=1;
  g.add(mesh);
  g.userData.mt=mt;
  g.update=function(t,fk){ mt.uniforms.uTime.value=t; };
  return {g,mt,update:g.update};
}

/* 使者骑马：马（合批）+ 骑手（makeFigure 缩放坐姿简化为立姿收腿） */
function makeHorse(o){
  o=o||{};
  const c=o.color===undefined?0x3a2c20:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.0,10,8); body.scale(1.9,1.0,0.72); body.translate(0,1.7,0); B.put(body,c);
  const neck=new THREE.CylinderGeometry(0.28,0.42,1.5,7);
  neck.rotateZ(-0.6); neck.translate(1.55,2.5,0); B.put(neck,shadeColor(c,0.9));
  const head=new THREE.SphereGeometry(0.34,8,6); head.scale(1.5,0.9,0.7);
  head.translate(2.25,3.2,0); B.put(head,shadeColor(c,1.1));
  const ear1=new THREE.ConeGeometry(0.09,0.28,5); ear1.translate(2.32,3.6,0.12); B.put(ear1,shadeColor(c,0.8));
  const ear2=ear1.clone(); ear2.translate(0,0,-0.24); B.put(ear2,shadeColor(c,0.8));
  const tail=new THREE.ConeGeometry(0.14,1.1,6); tail.rotateZ(0.5);
  tail.translate(-1.85,1.9,0); B.put(tail,shadeColor(c,0.7));
  [[0.85,-0.32],[0.85,0.32],[-0.95,-0.32],[-0.95,0.32]].forEach(function(p){
    B.put(limbGeo([p[0],1.3,p[1]],[p[0]*1.05,0.06,p[1]],0.13,0.07,6),shadeColor(c,0.85));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a3c2c,emissive:0x060503}),{c:o.rimC===undefined?0xd8a860:o.rimC,i:0.3,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

/* 箭矢：一支破空飞箭（箭杆+箭头+箭羽，合批 1 mesh） */
function makeArrow(o){
  o=o||{};
  const B=new GeoBag();
  const shaft=new THREE.CylinderGeometry(0.025,0.025,2.4,5);
  shaft.rotateZ(Math.PI/2); B.put(shaft,0x3a2c1c);
  const head=new THREE.ConeGeometry(0.09,0.35,5);
  head.rotateZ(-Math.PI/2); head.translate(1.35,0,0); B.put(head,0x8a7050);
  const f1=new THREE.PlaneGeometry(0.35,0.14); f1.translate(-1.0,0.08,0); B.put(f1,0xd8c8a0);
  const f2=f1.clone(); f2.rotateX(Math.PI/2); B.put(f2,0xd8c8a0);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x8a7a50,emissive:0x080604,side:THREE.DoubleSide}),{c:0xc0503a,i:0.3,p:2.5}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1.2:o.scale);
  return g;
}

function bCover(){ // 封面 · 战阵雄风
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0d0906,c2:0x1c130a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x0e0a07,atmo:0x46321e,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x080504,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xa87848,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xc89050,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xd8a058,i:0.45,p:[30,70,40]},{c:0x2c2018,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bTiaodeng(){ // 一 · 挑灯看剑 —— 孤灯一盏，醉里挑灯按剑，背景连营角声
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0806,c2:0x181008});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 远景军帐与连营角声（暗色远山） */
  const ridge=makeRange({r:210,h:34,layers:2,peaks:4,seed:851,color:0x0c0806,atmo:0x3c2414,fogK:0.62,glowK:0.06});
  g.add(ridge.g);
  /* 帐内长案 + 油灯 */
  const tb=makeTable({w:7.5,d:3.0,h:1.45,wood:0x2e1a10}); tb.g.position.set(0,0,-3.5); g.add(tb.g);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb040,
    transparent:true,opacity:0.8,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(4.5,4.5,1); lamp.position.set(-1.2,2.4,-3.2); lamp.renderOrder=3; g.add(lamp);
  const pl=new THREE.PointLight(0xff9030,1.8,36); pl.position.set(-1.2,2.6,-2.8); g.add(pl);
  /* 诗人（醉里挑灯看剑姿态） */
  const boss=makeFigure({pose:'按剑',robe:0x342018,belt:0x8a5020,hat:'幞头',beard:true,face:0.2,scale:1.35,rim:0.65,rimC:0xffa040});
  boss.position.set(0,0,-5.6); g.add(boss);
  /* 帐外连营帐篷剪影 */
  for(let i=0;i<4;i++){
    const tent=new THREE.Mesh(new THREE.ConeGeometry(3.2,3.8,4),
      new THREE.MeshPhongMaterial({color:0x1a120a,shininess:4}));
    tent.rotation.y=Math.PI/4;
    tent.position.set(-18+i*12,1.9,-22-Math.sin(i*1.7)*6); g.add(tent);
  }
  /* 角声声纹（连营号角自远方荡来） */
  const arcs=[];
  for(let i=0;i<3;i++){
    const pts=[];
    for(let k2=0;k2<=20;k2++){
      const a=-1.0+k2/20*2.0, r=2.2+i*3.0;
      pts.push(new THREE.Vector3(-14+Math.sin(a)*r,8+Math.cos(a)*r*0.6,-22+Math.cos(a)*r));
    }
    const ln=new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),
      new THREE.LineBasicMaterial({color:0xd87030,transparent:true,opacity:0.5,fog:false}));
    g.add(ln); arcs.push(ln);
  }
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-36],scale:68,color:0x8a5030,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x080504,seed:151,rim:0.14});
  rk.g.position.set(-13,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc07038,i:0.4,p:[30,60,-20]},{c:0x281810,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); boss.update(t,k); rk.update(t,k);
    lamp.material.opacity=k*(0.8*(0.85+0.15*Math.sin(t*7.5)));
    pl.intensity=k*(1.8*(0.85+0.15*Math.sin(t*7.5)));
    for(let i=0;i<arcs.length;i++){
      const ln=arcs[i];
      const ph=((t*0.35)+i/arcs.length)%1;
      ln.material.opacity=k*0.48*Math.sin(ph*Math.PI)*(1-ph*0.5);
      ln.scale.setScalar(0.6+ph*0.8);
    }
  }};
}
function bQiudianbing(){ // 二（标志性瞬间）· 沙场点兵 —— 八百里分麾下炙，五十弦翻塞外声
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0c0806,c2:0x1e1208});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:46,layers:3,peaks:5,seed:861,color:0x0e0906,atmo:0x442c16,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 麾下炙：两座大铜火盆烤肉，烈焰熊熊 */
  const braz1=makeBrazier({r:1.3,fh:3.0,fw:1.5,light:1.6,lightD:50,embers:28,spark:true});
  braz1.g.position.set(-7,0,-6); g.add(braz1.g);
  const braz2=makeBrazier({r:1.3,fh:3.0,fw:1.5,light:1.6,lightD:50,embers:28,spark:true});
  braz2.g.position.set(7,0,-6); g.add(braz2.g);
  /* 五十弦（乐器架） */
  const qin=new THREE.Group();
  const qb=new THREE.Mesh(new THREE.BoxGeometry(7.0,0.55,2.4),
    new THREE.MeshPhongMaterial({color:0x2c1a10,shininess:30,specular:0x4a3424}));
  qin.add(qb);
  for(let i=0;i<7;i++){
    const s=new THREE.Mesh(new THREE.CylinderGeometry(0.022,0.022,6.6,5),
      new THREE.MeshPhongMaterial({color:0xe8d0a0,shininess:50,emissive:0x221808}));
    s.rotation.z=Math.PI/2; s.position.set(0,0.32,-0.75+i*0.25); qin.add(s);
  }
  qin.position.set(0,1.2,-2); qin.rotation.y=0.15; g.add(qin);
  /* 军旗阵列（左右大纛） */
  const banL=makeBanner({w:3.0,h:4.2,poleH:11,color:0x701c12,tip:0xd05030});
  banL.g.position.set(-14,0,-12); banL.g.rotation.y=0.5; g.add(banL.g);
  const banR=makeBanner({w:3.0,h:4.2,poleH:11,color:0x701c12,tip:0xd05030});
  banR.g.position.set(14,0,-12); banR.g.rotation.y=-0.5; g.add(banR.g);
  /* 沙场秋点兵：密集的军阵人影 */
  const army=makeCrowd({n:18,rect:[-26,-32,52,14],seed:871,color:0x1a110a,rimC:0xd07838,rim:0.32,sMin:0.8,sMax:1.1});
  g.add(army.mesh);
  /* 主帅点兵阅阵 */
  const boss=makeFigure({pose:'指月',robe:0x342018,belt:0x8a5020,hat:'幞头',beard:true,face:0,scale:1.45,rim:0.68,rimC:0xffa040,noProp:true});
  boss.position.set(0,0,-9); g.add(boss);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-42],scale:72,color:0x8a5030,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080504,seed:153,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xd08040,i:0.46,p:[40,80,-30]},{c:0x2c1a12,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); braz1.update(t,k); braz2.update(t,k);
    banL.update(t,k); banR.update(t,k); army.update(t); boss.update(t,k);
    mist.update(t,k); rk.update(t,k);
  }};
}
function bDilu(){ // 三 · 的卢霹雳 —— 马作的卢飞快，弓如霹雳弦惊
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0c0806,c2:0x1c120a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:38,layers:2,peaks:4,seed:881,color:0x0e0906,atmo:0x442c16,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 的卢战马（飞驰前跃） */
  const horse=makeHorse({color:0x3a2416}); horse.position.set(-2,0.4,-6); horse.rotation.y=0.4; g.add(horse);
  const rider=makeFigure({pose:'指月',robe:0x342018,belt:0x8a5020,hat:'幞头',beard:true,face:0.4,scale:1.1,rim:0.6,rimC:0xffa040,noProp:true});
  rider.position.set(-2,1.95,-6); g.add(rider);
  /* 破空飞箭（霹雳之势） */
  const arrow=makeArrow({scale:1.4}); arrow.position.set(4,3.2,-10); arrow.rotation.y=0.4; g.add(arrow);
  const arrow2=makeArrow({scale:1.1}); arrow2.position.set(8,4.0,-14); arrow2.rotation.y=0.42; g.add(arrow2);
  /* 霹雳闪电微光（弦惊如雷） */
  const thunder=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffe8a0,
    transparent:true,opacity:0.4,depthWrite:false,blending:THREE.AdditiveBlending}));
  thunder.scale.set(60,60,1); thunder.position.set(16,26,-50); g.add(thunder);
  /* 飞驰扬沙（高速沙流） */
  const dust=makeFlow({n:550,box:[180,20,110],pos:[0,8,-24],color:0xb07038,size:20,speed:9.0,maxA:0.35});
  g.add(dust.points);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-44],scale:70,color:0x8a5030,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x080504,seed:155,rim:0.14});
  rk.g.position.set(-13,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xd08040,i:0.48,p:[-40,70,-40]},{c:0x2a1a12,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); dust.update(t); mist.update(t,k); rk.update(t,k);
    horse.position.y=0.4+Math.abs(Math.sin(t*8))*0.25;
    rider.position.y=1.95+Math.abs(Math.sin(t*8))*0.25;
    arrow.position.x=4+((t*14)%40);
    arrow2.position.x=8+((t*16)%42);
    thunder.material.opacity=k*(0.25+0.2*Math.sin(t*12));
  }};
}
function bBaifa(){ // 四（末境·可点击）· 白发生叹 —— 梦境破碎，唯白发将军对孤灯，点击沙场幻象重现
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,dream:0};
  const grd=makeGround({r:120,c1:0x090705,c2:0x160e06});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:32,layers:2,peaks:4,seed:891,color:0x0a0705,atmo:0x342010,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 案几 + 孤灯（现实的清冷） */
  const tb=makeTable({w:7.5,d:3.0,h:1.45,wood:0x28160c}); tb.g.position.set(0,0,-3.5); g.add(tb.g);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9030,
    transparent:true,opacity:0.7,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(4.0,4.0,1); lamp.position.set(-1.0,2.4,-3.2); lamp.renderOrder=3; g.add(lamp);
  const pl=new THREE.PointLight(0xff8028,1.6,32); pl.position.set(-1.0,2.5,-2.8); g.add(pl);
  /* 白发老将（挑灯按剑长叹） */
  const boss=makeFigure({pose:'按剑',robe:0x281a14,belt:0x6a3e18,hat:'发髻',hair:0xd4d8e0,beard:true,
    face:0.15,scale:1.32,rim:0.5,rimC:0xc88040});
  boss.position.set(0,0,-5.4); g.add(boss);
  /* 沙场幻境（点击后战阵大军再次浮现掠过） */
  const army=makeCrowd({n:16,rect:[-26,-36,52,12],seed:893,color:0x1a110a,rimC:0xd07838,rim:0.32,sMin:0.8,sMax:1.1});
  g.add(army.mesh);
  const burst=makeBurst({n:90,color:0xffb040,pos:[0,8,-18]}); g.add(burst.points);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-40],scale:68,color:0x7a4428,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x080504,seed:157,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xb06830,i:0.38,p:[30,60,-20]},{c:0x20140c,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.dream=Math.min(1,ctl.dream+dt/2.4);
      ridge.update(t,0); mist.update(t,k); boss.update(t,k); rk.update(t,k);
      lamp.material.opacity=k*(0.7*(0.85+0.15*Math.sin(t*7.0)));
      pl.intensity=k*(1.6*(0.85+0.15*Math.sin(t*7.0)));
      burst.update(t);
      /* 幻象大军随点击浮现 */
      army.mesh.position.y=ctl.dream>0?0:-100;
      army.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.5,0.12); pluck(5,0.9,0.12);
        const fl=$('#flash'); fl.textContent='可怜白发生'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
