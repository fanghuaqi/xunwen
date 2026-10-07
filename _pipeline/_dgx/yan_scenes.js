/* ================= 雁门太守行 · 四境场景（大漠金戈·玄金变体：黑云压城、角声夜紫、红旗易水、黄金台玉龙） ================= */

/* 军旗：横杆下悬挂的旗面（底边摆幅最大） */
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
  const pole=new THREE.CylinderGeometry(0.055,0.085,ph,6); pole.translate(0,ph/2,0); B.put(pole,0x150f0a);
  const bar=new THREE.CylinderGeometry(0.035,0.035,w*0.7,5); bar.rotateZ(Math.PI/2); bar.translate(w*0.32,ph,0); B.put(bar,0x150f0a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x060403}),{c:0xc08048,i:0.26,p:2.4})));
  const geo=new THREE.PlaneGeometry(w,h,10,3); geo.translate(0,-h/2,0);
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,depthWrite:false,
    uniforms:{uTime:{value:0},uC:{value:C(o.color===undefined?0x6e1e14:o.color)},
      uTipC:{value:C(o.tip===undefined?0xc05a38:o.tip)},uFade:{value:1}},
    vertexShader:BANNER_VERT,fragmentShader:BANNER_FRAG});
  const mesh=new THREE.Mesh(geo,mt); mesh.position.set(w*0.32,ph,0); mesh.renderOrder=1;
  g.add(mesh);
  g.userData.mt=mt;
  g.update=function(t,fk){ mt.uniforms.uTime.value=t; };
  return {g,mt,update:g.update};
}

/* 云隙天光：交叉两片、上亮下消的金白天光柱（甲光向日） */
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

/* 城垣：一段带雉堞的城墙 + 门楼（合批 1 mesh） */
function makeWall(o){
  o=o||{};
  const w=o.w===undefined?40:o.w, h=o.h===undefined?7:o.h;
  const c=o.color===undefined?0x191210:o.color;
  const R=seedRnd(o.seed===undefined?7:o.seed);
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,4.2); body.translate(0,h/2,0); B.put(body,c);
  for(let i=0;i<Math.floor(w/2.6);i++){
    const x=-w/2+1.3+i*2.6;
    if(R()<0.85){
      const mer=new THREE.BoxGeometry(1.5,1.1,4.0); mer.translate(x,h+0.55,0); B.put(mer,shadeColor(c,1.12));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a2018,emissive:0x040302}),{c:o.rimC===undefined?0xb08050:o.rimC,i:o.rim===undefined?0.2:o.rim,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 门楼：城门上的两层谯楼（合批 1 mesh，带亮窗） */
function makeGateTower(o){
  o=o||{};
  const w=o.w===undefined?10:o.w, h=o.h===undefined?9:o.h;
  const c=o.color===undefined?0x1a1310:o.color;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w,h,w*0.6); base.translate(0,h/2,0); B.put(base,c);
  const hall=new THREE.BoxGeometry(w*0.8,3.2,w*0.5); hall.translate(0,h+1.6,0); B.put(hall,shadeColor(c,1.15));
  const roof=new THREE.ConeGeometry(w*0.62,2.0,4); roof.rotateY(Math.PI/4); roof.translate(0,h+4.2,0); B.put(roof,0x241a12);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2e241a,emissive:0x050403}),{c:o.rimC===undefined?0xc08848:o.rimC,i:o.rim===undefined?0.24:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  for(let i=0;i<2;i++){
    const win=new THREE.Mesh(new THREE.PlaneGeometry(1.0,1.4),
      new THREE.MeshBasicMaterial({color:0xffb050,transparent:true,opacity:0.75}));
    win.position.set((i?1:-1)*w*0.16,h*0.55,w*0.31); g.add(win);
  }
  return {g};
}

/* 黑云团：几团大暗云 Sprite 的组合（可整体缓转、增厚） */
function makeDarkClouds(o){
  o=o||{};
  const n=o.n===undefined?9:o.n;
  const R=seedRnd(o.seed===undefined?17:o.seed);
  const spread=o.spread===undefined?[220,26,120]:o.spread, pos=o.pos===undefined?[0,52,-60]:o.pos;
  const g=new THREE.Group(); const items=[];
  for(let i=0;i<n;i++){
    const op0=0.35+R()*0.35, b0=Math.min(0.9,op0+0.45);   // 基线=加厚后的上限
    const m=new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0x0c0a10:o.color,
      transparent:true,opacity:b0,depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set(pos[0]+(R()-0.5)*spread[0],pos[1]+(R()-0.5)*spread[1],pos[2]+(R()-0.5)*spread[2]);
    const sc=(o.scale===undefined?110:o.scale)*(0.55+R()*0.8);
    s.scale.set(sc,sc*0.52,1);
    g.add(s); items.push({s,op0:op0,b0:b0,ph:R()*6.28});
  }
  g.update=function(t,fk,thick){
    const k=fk===undefined?1:fk, th=thick===undefined?0:thick;
    for(const it of items){
      it.s.material.opacity=k*Math.min(it.b0,it.op0+th*0.45)*(0.82+0.18*Math.sin(t*0.2+it.ph));
    }
    g.rotation.y=t*0.006;
  };
  return {g,update:g.update};
}

function bCover(){ // 封面 · 黑云玄夜
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0b0806,c2:0x191009});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:28,layers:2,peaks:4,seed:41,color:0x0e0a08,atmo:0x4a3820,fogK:0.74,glowK:0.09,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const clouds=makeDarkClouds({n:9,pos:[0,54,-60]});
  g.add(clouds.g);
  const fg=makeForeground({kind:'芦苇',w:80,n:24,d:9,color:0x070503,seed:5,sway:1.0});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,8,-40],color:0xd0a060,size:7,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xc09058,i:0.4,p:[30,70,40]},{c:0x2a201a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); clouds.update(t,k,0); fg.update(t,k); motes.update(t); }};
}
function bHeiyun(){ // 一（标志性瞬间）· 黑云压城 —— 乌云压顶与金甲反光强对撞
  const g=new THREE.Group();
  const ctl={t:0};
  const grd=makeGround({r:130,c1:0x0c0806,c2:0x1a120a}); g.add(grd.mesh);
  /* 背景：黑云下的远山（城垣之后） */
  const ridge=makeRange({r:220,h:34,layers:2,peaks:4,seed:151,color:0x0e0a08,atmo:0x46341e,fogK:0.60,glowK:0.07,y:-8});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  /* 黑云：低垂压顶的大暗云（浓、低、暗） */
  const clouds=makeDarkClouds({n:13,pos:[0,34,-46],spread:[280,26,120],scale:160,color:0x08070b});
  g.add(clouds.g);
  /* 城垣 + 门楼：横贯画面 */
  const wall=makeWall({w:96,h:8,seed:71}); wall.g.position.set(0,0,-26); g.add(wall.g);
  const tower=makeGateTower({w:12,h:10}); tower.g.position.set(-2,8,-26); g.add(tower.g);
  /* 云隙天光：一道窄金光斜落城头（甲光向日） */
  const shaft=makeLightShaft({w:11,h:64,k:0.6}); shaft.g.position.set(6,24,-22); g.add(shaft.g);
  shaft.g.rotation.z=0.24;
  /* 城头甲士：金甲立在光带里（鳞光小高光片） */
  const figs=[], armors=[];
  [[2.5,-25.0],[6.2,-24.6],[9.4,-25.2],[-8.5,-24.8]].forEach(function(p,i){
    const f=makeFigure({pose:i===1?'按剑':'独立',robe:0x6a4e1e,belt:0x8a5a24,hat:'幞头',
      face:0,scale:1.25,rim:0.75,rimC:0xffd890});
    f.position.set(p[0],8.05,p[1]); g.add(f); figs.push(f);
    for(let k2=0;k2<4;k2++){
      const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffdf9a,
        transparent:true,opacity:0.75,depthWrite:false,blending:THREE.AdditiveBlending}));
      sp.scale.set(1.1,1.1,1);
      sp.position.set(p[0]+(k2%2?0.5:-0.4),8.05+1.2+k2*0.85+(k2>1?0.3:0),p[1]+0.6);
      sp.renderOrder=3; g.add(sp); armors.push({sp,ph:i*1.3+k2*0.8});
    }
  });
  /* 城下旌旗与营火 */
  const bans=[];
  [[-16,-14,0.5],[14,-15,-0.5]].forEach(function(p,i){
    const b=makeBanner({w:2.6,h:3.4,poleH:10}); b.g.position.set(p[0],0,p[1]); b.g.rotation.y=p[2]; g.add(b.g); bans.push(b);
  });
  const br=makeBrazier({r:1.0,fh:2.3,fw:1.15,light:1.3,lightD:44,embers:24,spark:true});
  br.g.position.set(-5,0,-10); g.add(br.g);
  const army=makeCrowd({n:10,rect:[-22,-20,44,6],seed:161,color:0x1a120a,rimC:0xc08048,rim:0.26});
  g.add(army.mesh);
  const mist=makeMist({n:7,spread:[200,22,110],pos:[0,8,-38],scale:70,color:0x6a4a34,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080504,seed:81,rim:0.14});
  rk.g.position.set(-15,-1.6,12); g.add(rk.g);
  addLights(g,{c:0xc09058,i:0.32,p:[-40,70,-30]},{c:0x2a201a,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ctl.t+=dt;
    ridge.update(t,0);
    clouds.update(t,k,0);
    bans.forEach(function(b){b.update(t,k);});
    army.update(t); br.update(t,k); mist.update(t,k);
    shaft.update(t,k);
    shaft.mat.uniforms.uK.value=k*(0.30+0.35*sstep(2,10,stageT));
    figs.forEach(function(f){f.update(t,k);});
    armors.forEach(function(a,i2){
      a.sp.material.opacity=k*0.75*(0.30+0.66*sstep(2.5,9,stageT))*(0.6+0.4*Math.sin(t*2.6+a.ph));
    });
    rk.update(t,k);
  }};
}
function bJiaosheng(){ // 二 · 角声满天 —— 满天号角，塞上胭脂凝夜紫
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0f0a0e,c2:0x1e1218}); g.add(grd.mesh);
  const ridge=makeRange({r:220,h:40,layers:3,peaks:5,seed:171,color:0x120c12,atmo:0x50283c,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 角声涟漪：号手身后一圈圈扩散的声弧 */
  const arcs=[];
  const arcMat=new THREE.LineBasicMaterial({color:0xc07858,transparent:true,opacity:0.5,fog:false});
  for(let i=0;i<4;i++){
    const pts=[];
    for(let k2=0;k2<=24;k2++){
      const a=-1.1+k2/24*2.2, r=3+i*4;
      pts.push(new THREE.Vector3(-9+Math.sin(a)*r,8+Math.cos(a)*r*0.62,-22+Math.cos(a)*r));
    }
    const ln=new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts),arcMat.clone());
    ln.renderOrder=2; g.add(ln); arcs.push(ln);
  }
  /* 号手立于城垣残段 */
  const ru=makeWall({w:18,h:6,seed:73}); ru.g.position.set(-9,0,-24); g.add(ru.g);
  const horn=makeFigure({pose:'指月',robe:0x241a20,belt:0x6a4a2c,hat:'幞头',face:0.3,scale:1.3,rim:0.6,rimC:0xd88868,noProp:true});
  horn.position.set(-9,6,-23.4); g.add(horn);
  /* 塞上秋色：枯草、流沙、微红尘霭 */
  const grass=makeForeground({kind:'芦苇',w:60,n:22,d:8,color:0x140c10,seed:83,sway:1.1});
  grass.g.position.set(6,-1.4,10); g.add(grass.g);
  const dust=makeFlow({n:500,box:[180,24,110],pos:[0,12,-22],color:0x8a4a54,size:22,speed:4.2,maxA:0.3});
  g.add(dust.points);
  const embers=makeGlow({n:50,box:[120,20,70],pos:[0,4,-14],color:0xd86848,size:4,speed:0.1,rise:1,maxA:0.4});
  g.add(embers.points);
  /* 夜紫天幕：低垂的紫云 */
  const clouds=makeDarkClouds({n:7,pos:[0,48,-64],color:0x241024,spread:[260,26,130],scale:120});
  g.add(clouds.g);
  const mist=makeMist({n:7,spread:[210,24,110],pos:[0,9,-40],scale:72,color:0x7a4a58,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.8,w:20,d:7,color:0x0b070a,seed:85,rim:0.16});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xc07868,i:0.4,p:[-50,70,-40]},{c:0x2c1c26,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); dust.update(t); embers.update(t); clouds.update(t,k,0); mist.update(t,k);
    horn.update(t,k); grass.update(t,k); rk.update(t,k);
    /* 声弧：周期性扩散、渐隐 */
    for(let i=0;i<arcs.length;i++){
      const ln=arcs[i];
      const ph=((t*0.35)+i/arcs.length)%1;
      ln.material.opacity=k*0.5*Math.sin(ph*Math.PI)*(1-ph*0.55);
      ln.scale.setScalar(0.55+ph*0.75);
    }
  },onEnter(){ pluck(0,0.1,0.12); pluck(2,0.7,0.1); pluck(3,1.4,0.1); }};
}
function bHongqi(){ // 三 · 红旗半卷 —— 潜行至易水，霜重鼓寒
  const g=new THREE.Group();
  const ctl={t:0};
  const grd=makeGround({r:140,c1:0x0c0a0c,c2:0x181218}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:34,layers:2,peaks:4,seed:181,color:0x0e0a0e,atmo:0x3a2838,fogK:0.58,glowK:0.06});
  g.add(ridge.g);
  /* 易水：一条冷色暗河横过 */
  const water=makeWater({size:600,seg:90,amp:0.35,freq:0.1,speed:0.7,flow:[0.9,0.2],spec:1.0,
    deep:0x081018,shallow:0x122838,skyc:0x1e3444,moonDir:[-60,100,-150]});
  water.mesh.position.set(0,-0.7,-26); g.add(water.mesh);
  /* 霜地：河岸白霜斑块 */
  [[-14,-8,7],[4,-6,9],[18,-9,6],[-4,-4,5]].forEach(function(p,i){
    const fr=new THREE.Mesh(new THREE.CircleGeometry(p[2],16),
      new THREE.MeshPhongMaterial({color:0x3a4448,shininess:26,specular:0x6a7a84,transparent:true,opacity:0.5}));
    fr.rotation.x=-Math.PI/2; fr.position.set(p[0],0.03+i*0.005,p[1]); fr.renderOrder=0; g.add(fr);
  });
  /* 半卷红旗：旗面收窄低垂 */
  const bans=[];
  [[-8,-13,0.4],[3,-14,-0.4],[11,-12,-0.2]].forEach(function(p,i){
    const b=makeBanner({w:1.15,h:2.7,poleH:9,color:0x541610,tip:0x8a3424});
    b.g.position.set(p[0],0,p[1]); b.g.rotation.y=p[2]; g.add(b.g); bans.push(b);
  });
  /* 行军队伍：潜行的人流 + 主将按剑 */
  const army=makeCrowd({n:13,rect:[-20,-18,40,7],seed:191,color:0x15100f,rimC:0x9a8068,rim:0.24,sMin:0.8,sMax:1.05});
  g.add(army.mesh);
  const boss=makeFigure({pose:'按剑',robe:0x1e1614,belt:0x6a4a28,hat:'幞头',beard:true,face:0,scale:1.3,rim:0.55,rimC:0xc08858});
  boss.position.set(-2,0,-9); g.add(boss);
  /* 鼓寒：一面战鼓覆霜，声音发闷（低频声点） */
  const drum=new THREE.Mesh(new THREE.CylinderGeometry(1.5,1.5,1.1,16),
    new THREE.MeshPhongMaterial({color:0x3a2226,shininess:12,specular:0x5a4a52}));
  drum.rotation.z=Math.PI/2; drum.position.set(8,1.15,-8); g.add(drum);
  const stand1=new THREE.Mesh(new THREE.BoxGeometry(0.4,0.7,0.4),
    new THREE.MeshPhongMaterial({color:0x1a1210}));
  stand1.position.set(7.3,0.35,-8); g.add(stand1);
  const stand2=stand1.clone(); stand2.position.x=8.7; g.add(stand2);
  const frost=new THREE.Mesh(new THREE.CircleGeometry(2.2,14),
    new THREE.MeshPhongMaterial({color:0x44505a,shininess:30,specular:0x7a8a94,transparent:true,opacity:0.4}));
  frost.rotation.x=-Math.PI/2; frost.position.set(8,0.04,-8); g.add(frost);
  /* 寒雾贴水 */
  const mist=makeMist({n:9,spread:[260,16,140],pos:[0,4,-24],scale:80,color:0x5a7080,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080608,seed:87,rim:0.14});
  rk.g.position.set(-14,-1.6,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x0a0a0c,seed:89,sway:0.9});
  reeds.g.position.set(14,-1.4,11); g.add(reeds.g);
  addLights(g,{c:0x8a92a8,i:0.3,p:[-40,70,-40]},{c:0x222430,i:0.6});
  const pl=new THREE.PointLight(0x9ab0c8,0.5,46); pl.position.set(0,6,-14); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    bans.forEach(function(b){b.update(t,k);});
    army.update(t); boss.update(t,k);
    rk.update(t,k); reeds.update(t,k);
    pl.intensity=k*(0.5+Math.sin(t*0.5)*0.06);
  }};
}
function bHuangjintai(){ // 四（末境·可点击）· 黄金台上 —— 筑台之意，玉龙之誓；点击城头，金甲次第亮起
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,lit:0};
  const grd=makeGround({r:140,c1:0x0c0907,c2:0x1a110a}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:46,layers:3,peaks:5,seed:201,color:0x0e0a08,atmo:0x463220,fogK:0.58,glowK:0.08});
  g.add(ridge.g);
  /* 黑云（点击后加厚） */
  const clouds=makeDarkClouds({n:10,pos:[0,46,-62],spread:[260,28,130],scale:125});
  g.add(clouds.g);
  /* 黄金台：三层金顶高台 */
  const plat=new THREE.Group();
  [[15,1.2,0x2a1e10],[11.5,2.4,0x332412],[8,3.6,0x3c2a14]].forEach(function(p,i){
    const tier=new THREE.Mesh(new THREE.CylinderGeometry(p[0],p[0]+1.2,p[1],18),
      new THREE.MeshPhongMaterial({color:p[2],shininess:26,specular:0x8a6a34}));
    tier.position.y=p[1]/2+i*1.2; plat.add(tier);
  });
  const goldTop=new THREE.Mesh(new THREE.CylinderGeometry(5.6,6.2,0.5,18),
    new THREE.MeshPhongMaterial({color:0x8a6420,emissive:0x2a1c06,shininess:60,specular:0xffd888}));
  goldTop.position.y=4.05; plat.add(goldTop);
  plat.position.set(0,0,-16); g.add(plat);
  /* 台上千金（金盘 + 金饼堆） */
  const plate=new THREE.Mesh(new THREE.CylinderGeometry(1.7,1.9,0.3,14),
    new THREE.MeshPhongMaterial({color:0x6a4e1a,shininess:50,specular:0xd8b060}));
  plate.position.set(0,4.45,-16); g.add(plate);
  const pile=new THREE.Mesh(new THREE.SphereGeometry(0.9,10,8),
    new THREE.MeshPhongMaterial({color:0xc89838,emissive:0x3a2a08,shininess:70,specular:0xffe0a0}));
  pile.scale.set(1.3,0.62,1.3); pile.position.set(0,4.85,-16); g.add(pile);
  /* 台上持剑者（提携玉龙） */
  const boss=makeFigure({pose:'按剑',robe:0x2a1e14,belt:0xa8842f,hat:'幞头',beard:true,face:0,scale:1.4,rim:0.7,rimC:0xffd890});
  boss.position.set(2.6,4.3,-15); g.add(boss);
  /* 城头甲士两排（立于城垣之上，点击后金甲鳞光次第亮起） */
  const wall2=makeWall({w:96,h:8,seed:77}); wall2.g.position.set(0,0,-27); g.add(wall2.g);
  const armors=[];
  for(let row=0;row<2;row++){
    for(let i=0;i<4;i++){
      const f=makeFigure({pose:i===2?'按剑':'独立',robe:0x6a4e1e,belt:0x8a5a24,hat:'幞头',
        face:0,scale:1.2,rim:0.7,rimC:0xffd890});
      f.position.set(-12+i*8+(row?2:0),8.05,-25.4-row*1.6);
      g.add(f);
      const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffdf9a,
        transparent:true,opacity:0.9,depthWrite:false,blending:THREE.AdditiveBlending}));
      sp.scale.set(1.6,1.6,1);
      sp.position.copy(f.position); sp.position.y+=2.6; sp.position.z+=0.5;
      sp.renderOrder=3; g.add(sp);
      armors.push({sp,idx:row*4+i,f});
    }
  }
  /* 大纛与仪仗 */
  const bigBan=makeBanner({w:3.6,h:4.4,poleH:12,color:0x6e1e14,tip:0xd06838});
  bigBan.g.position.set(-8,0,-11); g.add(bigBan.g);
  const army=makeCrowd({n:12,rect:[-22,-19,40,6],seed:211,color:0x1a120a,rimC:0xc08048,rim:0.26});
  g.add(army.mesh);
  const burst=makeBurst({n:110,color:0xffe0a0,pos:[0,9,-14]}); g.add(burst.points);
  const gold=makeGlow({n:150,box:[80,26,60],pos:[0,6,-10],color:0xffd070,size:10,speed:0.05,rise:1,maxA:0});
  g.add(gold.points);
  const br=makeBrazier({r:1.0,fh:2.3,fw:1.15,light:1.25,lightD:44,embers:22,spark:false});
  br.g.position.set(7,0,-8); g.add(br.g);
  const mist=makeMist({n:7,spread:[210,24,110],pos:[0,9,-42],scale:72,color:0x8a6044,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x080504,seed:91,rim:0.14});
  rk.g.position.set(-15,-1.6,12); g.add(rk.g);
  addLights(g,{c:0xc09058,i:0.38,p:[-40,80,-30]},{c:0x2a201a,i:0.6});
  const pl=new THREE.PointLight(0xffca7a,1.9,60); pl.position.set(0,10,-14); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.lit=Math.min(1,ctl.lit+dt/2.4);
      ridge.update(t,0);
      clouds.update(t,k,ctl.lit);                          // 点击后黑云加厚
      bigBan.update(t,k);
      army.update(t); br.update(t,k); mist.update(t,k);
      burst.update(t);
      gold.mat.uniforms.uMaxA.value=k*0.6*ctl.lit;
      gold.update(t);
      boss.update(t,k);
      armors.forEach(function(a){
        /* 次第亮起：按 idx 推迟点亮时间 */
        const thr=a.idx/8;
        const on=sstep(thr,thr+0.25,ctl.lit);
        a.sp.material.opacity=k*0.9*(0.31+0.69*on)*(0.6+0.4*Math.sin(t*2.8+a.idx*1.1));
        a.f.userData.update(t,k);
      });
      pl.intensity=k*1.9*(0.62+ctl.lit*0.38*(0.85+0.15*Math.sin(t*3.3)));
      rk.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.16); pluck(4,0.6,0.12); bell();
        const fl=$('#flash'); fl.textContent='提携玉龙'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
