/* ================= 满江红 · 四境场景（大漠金戈·赤焰变体：雨歇孤楼、长路尘月、破垣烽烟、长车山缺） ================= */

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

/* 云隙天光：交叉两片、上亮下消的金白天光柱（仰天长啸 / 天光裂云） */
const SHAFT_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float x=abs(vUv.x-0.5)*2.0;
  float core=1.0-smoothstep(0.0,0.55,x);
  float edge=smoothstep(0.2,1.0,vUv.y)*smoothstep(1.0,0.55,vUv.y);
  float a=core*edge*uFade*uK*(0.55+0.14*sin(uTime*1.3));
  gl_FragColor=vec4(vec3(1.0,0.92,0.72),a);
}`;
function makeLightShaft(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, h=o.h===undefined?70:o.h;
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.k===undefined?0.5:o.k}},
    vertexShader:'varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }',
    fragmentShader:SHAFT_FRAG});
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

/* 战车：双轮（辋+辐+毂）+ 车厢 + 长辕，合批 1 mesh */
function makeChariot(o){
  o=o||{};
  const c=o.color===undefined?0x2a1a10:o.color, metal=o.metal===undefined?0x3a2e1c:o.metal;
  const B=new GeoBag();
  [-1.05,1.05].forEach(function(wx){
    const rim=new THREE.TorusGeometry(1.05,0.10,6,20); rim.translate(wx,1.05,0); B.put(rim,shadeColor(metal,0.9));
    for(let i=0;i<6;i++){
      const a=i/6*Math.PI*2;
      const sp=new THREE.CylinderGeometry(0.035,0.035,1.9,4);
      const m4=new THREE.Matrix4().makeTranslation(wx,1.05,0)
        .multiply(new THREE.Matrix4().makeRotationZ(a));
      sp.applyMatrix4(m4);
      B.put(sp,metal);
    }
    const hub=new THREE.CylinderGeometry(0.16,0.16,0.3,8); hub.rotateX(Math.PI/2); hub.translate(wx,1.05,0); B.put(hub,shadeColor(metal,1.25));
  });
  const ax=new THREE.CylinderGeometry(0.07,0.07,2.3,6); ax.rotateZ(Math.PI/2); ax.translate(0,1.05,0); B.put(ax,metal);
  const box=new THREE.BoxGeometry(2.5,0.85,1.7); box.translate(0,1.55,-0.15); B.put(box,c);
  const railF=new THREE.BoxGeometry(2.5,0.5,0.09); railF.translate(0,2.2,0.72); B.put(railF,shadeColor(c,1.2));
  const railB=new THREE.BoxGeometry(2.5,0.62,0.09); railB.translate(0,2.26,-1.0); B.put(railB,shadeColor(c,1.2));
  const yuan=new THREE.CylinderGeometry(0.055,0.075,3.6,6); yuan.rotateX(Math.PI/2-0.14); yuan.translate(0,0.9,1.9); B.put(yuan,shadeColor(c,0.85));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:22,
    specular:0x4a3a26,emissive:0x080503}),{c:o.rimC===undefined?0xc98a4a:o.rimC,i:o.rim===undefined?0.3:o.rim,p:2.5}));
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

/* 破城垣：残破城楼/城墙（错位箱体 + 倾颓板），剪影 */
function makeRuin(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, h=o.h===undefined?10:o.h;
  const c=o.color===undefined?0x17110d:o.color;
  const R=seedRnd(o.seed===undefined?3:o.seed);
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,w*0.55); body.translate(0,h/2,0); B.put(body,c);
  const jag=new THREE.BoxGeometry(w*0.7,h*0.24,w*0.5); jag.rotateZ((R()-0.5)*0.2);
  jag.translate((R()-0.5)*w*0.2,h*1.06,0); B.put(jag,shadeColor(c,1.15));
  const tilt=new THREE.BoxGeometry(w*0.34,h*0.5,w*0.3); tilt.rotateZ(0.5+R()*0.3);
  tilt.translate(-w*0.62,h*0.32,0); B.put(tilt,shadeColor(c,0.85));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x241d14,emissive:0x040302}),{c:o.rimC===undefined?0xb08050:o.rimC,i:o.rim===undefined?0.22:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

function bCover(){ // 封面 · 大漠昏黄
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0b0805,c2:0x1c130a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0d0906,atmo:0x4a3820,fogK:0.74,glowK:0.10,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'芦苇',w:80,n:24,d:9,color:0x070503,seed:5,sway:1.0});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xb08858,op:0.10});
  g.add(mist.g);
  const dust=makeGlow({n:70,box:[220,36,130],pos:[0,8,-40],color:0xc8a060,size:8,speed:0.05,rise:0,maxA:0.45});
  g.add(dust.points);
  addLights(g,{c:0xd8a860,i:0.45,p:[30,70,40]},{c:0x2c211a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); dust.update(t); }};
}
function bXiaoxiao(){ // 一 · 怒发冲冠 —— 潇潇雨歇，孤楼凭栏，一啸上冲云霄
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0806,c2:0x1a1410}); g.add(grd.mesh);
  const ridge=makeRange({r:200,h:44,layers:3,peaks:5,seed:311,color:0x0e0a07,atmo:0x46341e,fogK:0.62,glowK:0.09});
  g.add(ridge.g);
  /* 雨丝（渐歇：update 里让 uMaxA 随 stageT 衰减） */
  const rain=makeGlow({n:520,box:[170,52,100],pos:[0,26,-12],color:0xaac0d8,size:4.5,speed:0.34,rise:1,maxA:0.4});
  rain.points.renderOrder=3; g.add(rain.points);
  /* 孤楼高台 + 凭栏 + 亭柱 + 一杆旗 */
  const plat=new THREE.Mesh(new THREE.CylinderGeometry(6.2,7.2,3.0,18),
    new THREE.MeshPhongMaterial({color:0x1a1410,shininess:16,specular:0x443626}));
  plat.position.set(0,1.5,-6); g.add(plat);
  const rail=makeForeground({kind:'栏杆',w:16,h:2.6,color:0x0d0a08,rim:0.24,seed:41});
  rail.g.position.set(0,3.0,-2.6); g.add(rail.g);
  [-5.4,5.4].forEach(function(x){
    const p=makePillar({h:9.5,r:0.36,color:0x241708,top:false});
    p.g.position.set(x,3.0,-8.2); g.add(p.g);
  });
  const ban=makeBanner({w:2.4,h:3.2,poleH:10.5}); ban.g.position.set(11,0,-9); g.add(ban.g);
  /* 主体：仰天长啸者（举臂向天） */
  const boss=makeFigure({pose:'指月',robe:0x241c14,belt:0x8a5a2a,hat:'幞头',beard:true,face:0,scale:1.5,rim:0.68,rimC:0xd8b070});
  boss.position.set(0,3.0,-6); g.add(boss);
  /* 天光裂云：细金光柱自云隙落到孤楼（update 渐亮 = 长啸冲霄） */
  const shaft=makeLightShaft({w:15,h:74,k:0.5}); shaft.g.position.set(0,26,-11); g.add(shaft.g);
  /* 高天云层 */
  const clouds=makeMist({n:9,spread:[300,26,160],pos:[0,58,-60],scale:95,color:0x241812,op:0.30});
  g.add(clouds.g);
  const mist=makeMist({n:6,spread:[180,24,110],pos:[0,9,-34],scale:60,color:0x8a7050,op:0.08});
  g.add(mist.g);
  /* 前景：湿岩 + 枯苇 */
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x070504,seed:47,rim:0.16});
  rk.g.position.set(-16,-1.5,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:34,n:14,d:6,color:0x060404,seed:49,sway:0.8});
  reeds.g.position.set(16,-1.4,11); g.add(reeds.g);
  addLights(g,{c:0xc09868,i:0.45,p:[-40,80,-40]},{c:0x2a211a,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ban.update(t,k); boss.update(t,k);
    shaft.update(t,k);
    /* 雨歇：30s 内雨势收干；啸声起，光柱渐明 */
    rain.mat.uniforms.uMaxA.value=k*0.4*(1-sstep(4,22,stageT)*0.85);
    shaft.mat.uniforms.uK.value=k*(0.28+0.45*sstep(3,14,stageT));
    rain.update(t); clouds.update(t,k); mist.update(t,k);
    rk.update(t,k); reeds.update(t,k);
  }};
}
function bQianli(){ // 二 · 八千里路 —— 长路尘土，云和月低垂，披星戴月
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0c0906,c2:0x1e140a}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:30,layers:2,peaks:4,seed:321,color:0x0e0a07,atmo:0x4a3820,fogK:0.60,glowK:0.08});
  g.add(ridge.g);
  /* 长路：一条土路伸向天际（微斜交向月） */
  const road=new THREE.Mesh(new THREE.BoxGeometry(3.4,0.08,150),
    new THREE.MeshPhongMaterial({color:0x2a2016,shininess:8,specular:0x4a3a24}));
  road.rotation.y=0.12; road.position.set(3,0.03,-40); g.add(road);
  /* 行人：主人在路上，远处一小队随行 */
  const boss=makeFigure({pose:'独立',robe:0x241c16,belt:0x8a5a2a,hat:'幞头',beard:true,face:0.2,scale:1.15,rim:0.5,rimC:0xd8a860});
  boss.position.set(3.4,0,-20); g.add(boss);
  const troop=makeCrowd({n:10,rect:[-2,-64,14,26],seed:351,color:0x171009,rimC:0xc08850,rim:0.3,sMin:0.7,sMax:1.0});
  g.add(troop.mesh);
  /* 尘与土：低空沙尘横流 + 贴地尘雾 */
  const dust=makeFlow({n:600,box:[180,22,120],pos:[0,9,-26],color:0xb08850,size:22,speed:6.5,maxA:0.34});
  g.add(dust.points);
  const motes=makeGlow({n:90,box:[120,6,70],pos:[0,2.5,-20],color:0xc8a060,size:6,speed:0.08,rise:0,maxA:0.4});
  g.add(motes.points);
  /* 云和月：昏黄低月被云层半掩 */
  const clouds=makeMist({n:10,spread:[280,22,150],pos:[0,46,-90],scale:90,color:0x2c1e12,op:0.34});
  g.add(clouds.g);
  const mist=makeMist({n:6,spread:[200,22,120],pos:[0,8,-50],scale:66,color:0x9a7a4e,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x080504,seed:53,rim:0.16});
  rk.g.position.set(-15,-1.5,13); g.add(rk.g);
  const grass=makeForeground({kind:'芦苇',w:30,n:12,d:6,color:0x070503,seed:55,sway:0.7});
  grass.g.position.set(14,-1.3,12); g.add(grass.g);
  addLights(g,{c:0xd8a860,i:0.5,p:[-60,60,-60]},{c:0x2c211a,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); troop.update(t); dust.update(t); motes.update(t);
    clouds.update(t,k); mist.update(t,k);
    boss.update(t,k); rk.update(t,k); grass.update(t,k);
  }};
}
function bJingkang(){ // 三 · 靖康未雪 —— 破垣烽烟，半卷旗垂，最沉一境
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0b0808,c2:0x181010}); g.add(grd.mesh);
  const ridge=makeRange({r:210,h:38,layers:2,peaks:5,seed:331,color:0x0d0908,atmo:0x3a2418,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 破城垣：三座残楼错落 */
  [[-14,-22,9,7],[2,-30,13,9],[16,-20,8,6]].forEach(function(p,i){
    const ru=makeRuin({w:p[3],h:p[2],seed:61+i*7});
    ru.g.position.set(p[0],0,p[1]); g.add(ru.g);
  });
  const wall=new THREE.Mesh(new THREE.BoxGeometry(44,3.2,1.6),
    new THREE.MeshPhongMaterial({color:0x140f0b,shininess:5}));
  wall.position.set(0,1.4,-16); g.add(wall);
  const gap=new THREE.Mesh(new THREE.BoxGeometry(9,2.0,1.6),
    new THREE.MeshPhongMaterial({color:0x140f0b,shininess:5}));
  gap.position.set(-4,0.8,-16); g.add(gap);
  /* 烽烟：暗烟上腾（NormalBlending 深色粒子）+ 零星火星 */
  const smoke=makeGlow({n:120,box:[60,50,40],pos:[-6,16,-26],color:0x1c130d,size:60,speed:0.05,rise:1,maxA:0.5,add:false});
  smoke.points.renderOrder=5; g.add(smoke.points);
  const smoke2=makeGlow({n:90,box:[40,44,30],pos:[14,14,-22],color:0x180f0b,size:46,speed:0.06,rise:1,maxA:0.42,add:false});
  smoke2.points.renderOrder=5; g.add(smoke2.points);
  const ember=makeGlow({n:60,box:[80,26,60],pos:[0,4,-20],color:0xe07830,size:4,speed:0.12,rise:1,maxA:0.55});
  g.add(ember.points);
  /* 半卷旗：两杆窄旗 */
  const bans=[];
  [[-9,-8,0.6],[10,-9,-0.7]].forEach(function(p,i){
    const b=makeBanner({w:1.7,h:2.6,poleH:8.5,color:0x501810,tip:0x904028});
    b.g.position.set(p[0],0,p[1]); b.g.rotation.y=p[2]; g.add(b.g); bans.push(b);
  });
  /* 守墙人影 */
  const figs=[];
  const f1=makeFigure({pose:'按剑',robe:0x1c1512,belt:0x6a4a28,hat:'幞头',face:0.1,scale:1.2,rim:0.5,rimC:0xc07848});
  f1.position.set(-3,0,-13.6); g.add(f1); figs.push(f1);
  const f2=makeFigure({pose:'独立',robe:0x201812,hat:'发髻',face:-0.2,scale:1.05,rim:0.42,rimC:0xc07848});
  f2.position.set(5.5,0,-13.8); g.add(f2); figs.push(f2);
  const mist=makeMist({n:8,spread:[200,26,120],pos:[0,10,-40],scale:72,color:0x4a2c1c,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x070504,seed:67,rim:0.14});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xa06848,i:0.3,p:[30,60,30]},{c:0x241a16,i:0.6});
  const pl=new THREE.PointLight(0xff7030,0.9,44); pl.position.set(-6,6,-22); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0);
    bans.forEach(function(b){b.update(t,k);});
    smoke.update(t); smoke2.update(t); ember.update(t); mist.update(t,k);
    figs.forEach(function(f){f.update(t,k);});
    rk.update(t,k);
    pl.intensity=k*(0.9+Math.sin(t*5.3)*0.16);
  }};
}
function bChangche(){ // 四（末境·可点击）· 长车踏破 —— 车辚辚陈列，点击天光裂云、山缺旌旗出
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,appear:0};
  const grd=makeGround({r:150,c1:0x0c0906,c2:0x1d130a}); g.add(grd.mesh);
  /* 贺兰山：层叠大山 */
  const ridge=makeRange({r:250,h:98,layers:3,peaks:6,seed:341,color:0x0d0a08,atmo:0x443220,fogK:0.58,glowK:0.09});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  /* 山缺：两座岩塔夹出关隘 */
  [[-15,-44,13,1],[15.5,-46,15,2]].forEach(function(p,i){
    const ru=makeRuin({w:9,h:p[2],seed:71+i*3,color:0x161009,rimC:0xc08048,rim:0.3});
    ru.g.position.set(p[0],0,p[1]); ru.g.rotation.y=i?0.5:-0.5; g.add(ru.g);
  });
  /* 天光（点击后裂云大涨） */
  const shaft=makeLightShaft({w:20,h:88,k:0.34}); shaft.g.position.set(0,30,-46); g.add(shaft.g);
  /* 山缺旌旗阵列（点击后浮现） */
  const army=[];
  for(let i=0;i<5;i++){
    const b=makeBanner({w:2.2,h:3.0,poleH:9,color:0x701e12,tip:0xd06838});
    b.g.position.set(-8+i*4,0,-52-(i%2)*4); g.add(b.g); army.push(b);
  }
  /* 长车三乘 + 主帅按剑 */
  const cars=[];
  [[-3.5,-13,0.16,1.5],[5.5,-18,-0.2,1.4],[-1,-27,0.05,1.3]].forEach(function(p,i){
    const c=makeChariot({});
    c.position.set(p[0],0,p[1]); c.rotation.y=p[2]; c.scale.setScalar(p[3]); g.add(c); cars.push(c);
  });
  const boss=makeFigure({pose:'按剑',robe:0x241a12,belt:0x8a5a2a,hat:'幞头',beard:true,face:0,scale:1.45,rim:0.66,rimC:0xd8a860});
  boss.position.set(0.8,0,-10); g.add(boss);
  const crowd=makeCrowd({n:13,rect:[-18,-30,36,8],seed:361,color:0x181009,rimC:0xc08048,rim:0.28,sMin:0.8,sMax:1.05});
  g.add(crowd.mesh);
  /* 火把：火盆两座 + 灯串 */
  const braz=[];
  [[-9,3.6],[9,3.8]].forEach(function(p,i){
    const br=makeBrazier({r:1.0,fh:2.4,fw:1.15,light:1.3,lightD:46,embers:i?16:26,spark:i===0});
    br.g.position.set(p[0],0,p[1]); g.add(br.g); braz.push(br);
  });
  /* 旗影：前景两杆大旗 */
  const bans=[];
  [[-17,2,0.8],[17,1,-0.8]].forEach(function(p,i){
    const b=makeBanner({w:3.0,h:4.0,poleH:11.5}); b.g.position.set(p[0],0,p[1]); b.g.rotation.y=p[2]; g.add(b.g); bans.push(b);
  });
  const burst=makeBurst({n:110,color:0xffd890,pos:[0,12,-44]}); g.add(burst.points);
  const gold=makeGlow({n:150,box:[110,34,80],pos:[0,6,-30],color:0xffd070,size:11,speed:0.05,rise:1,maxA:0});
  g.add(gold.points);
  const mist=makeMist({n:8,spread:[220,26,130],pos:[0,10,-48],scale:76,color:0x8a6a44,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080504,seed:77,rim:0.15});
  rk.g.position.set(-15,-1.6,14); g.add(rk.g);
  addLights(g,{c:0xc09058,i:0.42,p:[-40,80,-40]},{c:0x2c2118,i:0.6});
  const pl=new THREE.PointLight(0xffb060,2.7,52); pl.position.set(0,6,-16); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.appear=Math.min(1,ctl.appear+dt/2.2);
      ridge.update(t,0);
      bans.forEach(function(b){b.update(t,k);});
      army.forEach(function(b){
        b.update(t,k);
        b.mt.uniforms.uFade.value=k*ctl.appear;            // 点击后浮现
      });
      shaft.update(t,k);
      shaft.mat.uniforms.uK.value=k*(0.30+0.5*ctl.appear);
      braz.forEach(function(br){br.update(t,k);});
      crowd.update(t); mist.update(t,k); rk.update(t,k);
      burst.update(t);
      gold.mat.uniforms.uMaxA.value=k*0.6*ctl.appear;
      gold.update(t);
      boss.update(t,k);
      pl.intensity=k*(1.2*(0.85+0.15*Math.sin(t*6.1))+1.3*ctl.appear);   // 基座=满亮度 2.7，未点亮时仅为零头
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.16); pluck(4,0.5,0.12); bell();
        const fl=$('#flash'); fl.textContent='朝天阙'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
