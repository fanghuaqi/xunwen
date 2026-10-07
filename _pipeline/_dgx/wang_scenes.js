/* ================= 望海潮 · 五境场景（青绿春晓·钱塘变体：烟柳画桥、怒涛天堑、桂子荷花、千骑高牙） ================= */

/* 孤树/云树：主干收分 + 发散枝条 + 叶团（合批 1 mesh） */
function makeTree(o){
  o=o||{};
  const h=o.h===undefined?11:o.h, R=seedRnd(o.seed===undefined?5:o.seed);
  const trunkC=o.trunk===undefined?0x151009:o.trunk;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*1.4-0.7,h*0.98,0],h*0.050,h*0.014,8),trunkC);
  const nb=o.branches===undefined?8:o.branches;
  for(let i=0;i<nb;i++){
    const a=(i/nb)*Math.PI*2+R()*0.9, el=0.45+R()*0.85, len=h*(0.28+R()*0.40);
    const dx=Math.cos(a)*Math.cos(el), dy=Math.sin(el), dz=Math.sin(a)*Math.cos(el);
    const y0=h*(0.50+R()*0.42);
    const p1=[dx*len*0.22,y0+dy*len*0.28,dz*len*0.22];
    const p2=[dx*len,y0+dy*len,dz*len];
    B.put(limbGeo(p1,p2,h*0.020,h*0.007,6),trunkC);
    if(o.leaf&&R()<0.72){
      const lf=new THREE.SphereGeometry(len*0.30,7,5); lf.scale(1.3,0.75,1.3);
      lf.translate(p2[0],p2[1]+0.3,p2[2]); B.put(lf,o.leaf);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x241d14,emissive:0x030204}),
    {c:o.rimC===undefined?0x9fc8a8:o.rimC,i:o.rim===undefined?0.3:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 仪仗旗：横杆下悬挂的旗面（底边摆幅最大） */
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
  const pole=new THREE.CylinderGeometry(0.055,0.085,ph,6); pole.translate(0,ph/2,0); B.put(pole,0x14110c);
  const bar=new THREE.CylinderGeometry(0.035,0.035,w*0.7,5); bar.rotateZ(Math.PI/2); bar.translate(w*0.32,ph,0); B.put(bar,0x14110c);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x060403}),{c:0xa8b898,i:0.26,p:2.4})));
  const geo=new THREE.PlaneGeometry(w,h,10,3); geo.translate(0,-h/2,0);
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,depthWrite:false,
    uniforms:{uTime:{value:0},uC:{value:C(o.color===undefined?0x1e3a28:o.color)},
      uTipC:{value:C(o.tip===undefined?0x5a9a68:o.tip)},uFade:{value:1}},
    vertexShader:BANNER_VERT,fragmentShader:BANNER_FRAG});
  const mesh=new THREE.Mesh(geo,mt); mesh.position.set(w*0.32,ph,0); mesh.renderOrder=1;
  g.add(mesh);
  g.userData.mt=mt;
  g.update=function(t,fk){ mt.uniforms.uTime.value=t; };
  return {g,mt,update:g.update};
}

/* 垂柳：主干 + 下垂柳丝（细管下挂，随风微摆） */
const WILLOW_VERT=`
uniform float uTime; uniform float uSway;
varying float vY;
void main(){ vY=uv.y; vec3 p=position;
  float k=pow(clamp(1.0-uv.y,0.0,1.0),1.2);
  p.x+=sin(uTime*0.8+position.y*0.7)*uSway*k;
  p.z+=cos(uTime*0.6+position.y*0.9)*uSway*0.6*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0); }`;
const WILLOW_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade; varying float vY;
void main(){ vec3 c=mix(uC,uTipC,pow(clamp(vY,0.0,1.0),1.4));
  gl_FragColor=vec4(c,uFade); }`;
function makeWillow(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, R=seedRnd(o.seed===undefined?13:o.seed);
  const trunkC=o.trunk===undefined?0x1c1410:o.trunk;
  const g=new THREE.Group();
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.8-0.4,h*0.62,0],h*0.05,h*0.02,7),trunkC);
  for(let i=0;i<4;i++){
    const a=i/4*Math.PI*2+R();
    B.put(limbGeo([0,h*0.55,0],[Math.cos(a)*h*0.22,h*0.78,Math.sin(a)*h*0.22],h*0.024,h*0.012,5),trunkC);
  }
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a2418,emissive:0x050704}),{c:o.rimC===undefined?0xa8c890:o.rimC,i:o.rim===undefined?0.3:o.rim,p:2.4})));
  /* 柳丝：自树冠下垂的细束（合并 + 顶点摆动着色器） */
  const B2=new GeoBag();
  const nf=o.fronds===undefined?14:o.fronds;
  for(let i=0;i<nf;i++){
    const a=(i/nf)*Math.PI*2+R()*0.5, rr=h*(0.16+R()*0.30);
    const top=[Math.cos(a)*rr,h*(0.66+R()*0.2),Math.sin(a)*rr];
    const len=h*(0.42+R()*0.42);
    const p0=top, p1=[top[0]*1.12,top[1]-len*0.5,top[2]*1.12], p2=[top[0]*1.2,top[1]-len,top[2]*1.2];
    B2.put(limbGeo(p0,p1,0.030,0.014,4),0x2a3a20);
    B2.put(limbGeo(p1,p2,0.014,0.007,4),0x2a3a20);
  }
  const geo=mergeGeos(B2.list);
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.16:o.sway},
      uC:{value:C(0x26361e)},uTipC:{value:C(o.tip===undefined?0x4a6a38:o.tip)},uFade:{value:1}},
    vertexShader:WILLOW_VERT,fragmentShader:WILLOW_FRAG});
  const fm=new THREE.Mesh(geo,mt); fm.frustumCulled=false; g.add(fm);
  g.userData.mt=mt;
  g.update=function(t,fk){ mt.uniforms.uTime.value=t; };
  return {g,update:g.update};
}

/* 画桥：石拱桥（桥面沿拱弧 + 桥栏），合批 1 mesh */
function makeBridge(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, h=o.h===undefined?3.2:o.h;
  const c=o.color===undefined?0x232a26:o.color;
  const B=new GeoBag();
  const seg=12;
  for(let i=0;i<seg;i++){
    const t0=i/seg, t1=(i+1)/seg;
    const x0=(t0-0.5)*w, x1=(t1-0.5)*w;
    const y0=Math.sin(t0*Math.PI)*h, y1=Math.sin(t1*Math.PI)*h;
    const sl=new THREE.BoxGeometry(w/seg+0.15,0.34,3.0);
    sl.rotateZ(Math.atan2(y1-y0,x1-x0));
    sl.translate((x0+x1)/2,(y0+y1)/2,0);
    B.put(sl,c);
  }
  for(let i=0;i<=6;i++){
    const t=i/6, x=(t-0.5)*w, y=Math.sin(t*Math.PI)*h;
    const post=new THREE.BoxGeometry(0.16,0.85,0.16); post.translate(x,y+0.6,1.3); B.put(post,shadeColor(c,1.3));
    const post2=post.clone(); post2.translate(0,0,-2.6); B.put(post2,shadeColor(c,1.3));
  }
  const rail=new THREE.BoxGeometry(w*0.94,0.12,0.14); rail.translate(0,h*0.5+1.02,1.3); B.put(rail,shadeColor(c,1.2));
  const rail2=rail.clone(); rail2.translate(0,0,-2.6); B.put(rail2,shadeColor(c,1.2));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x3a4438,emissive:0x060806}),{c:o.rimC===undefined?0x9fc8a8:o.rimC,i:o.rim===undefined?0.26:o.rim,p:2.5}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 人家：一组屋舍（合批 1 mesh：墙 + 坡顶 + 亮窗） */
function makeHouse(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17:o.seed);
  const n=o.n===undefined?6:o.n, w=o.w===undefined?26:o.w, d=o.d===undefined?10:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, s=0.7+R()*0.7, hh=2.2*s, ww=2.6*s, dd=2.2*s;
    const body=new THREE.BoxGeometry(ww,hh,dd); body.translate(x,hh/2,z); B.put(body,0x1c2018);
    const roof=new THREE.ConeGeometry(ww*0.86,hh*0.55,4); roof.rotateY(Math.PI/4);
    roof.translate(x,hh+hh*0.26,z); B.put(roof,0x12160f);
    const win=new THREE.BoxGeometry(ww*0.2,hh*0.24,0.05);
    win.translate(x+ww*0.1,hh*0.55,z+dd/2+0.02); B.put(win,0xd8b868);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3228,emissive:0x060806}),{c:o.rimC===undefined?0x9fc8a8:o.rimC,i:o.rim===undefined?0.24:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 荷：一株荷叶 + 花苞/绽花（合批 1 mesh） */
function makeLotus(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, R=seedRnd(o.seed===undefined?23:o.seed);
  const leafC=o.leaf===undefined?0x2c5a38:o.leaf, bloomC=o.bloom===undefined?0xe89ab8:o.bloom;
  const B=new GeoBag();
  const nLeaf=o.leaves===undefined?3:o.leaves;
  for(let i=0;i<nLeaf;i++){
    const a=R()*6.283, rr=R()*0.7;
    const lf=new THREE.CylinderGeometry(0.85,0.85,0.03,14);
    lf.scale(1,1,0.92); lf.translate(Math.cos(a)*rr,0.55+0.06*i,Math.sin(a)*rr);
    B.put(lf,shadeColor(leafC,0.85+0.3*R()));
    const st=limbGeo([Math.cos(a)*rr,0.2,Math.sin(a)*rr],[Math.cos(a)*rr,0.56+0.06*i,Math.sin(a)*rr],0.045,0.035,5);
    B.put(st,shadeColor(leafC,0.7));
  }
  if(o.bloom!==false){
    const bx=(R()-0.5)*0.5, bz=(R()-0.5)*0.5;
    B.put(limbGeo([bx,0.2,bz],[bx,1.35,bz],0.04,0.03,5),shadeColor(leafC,0.72));
    const bud=new THREE.ConeGeometry(0.2,0.5,7); bud.translate(bx,1.55,bz); B.put(bud,bloomC);
    const bud2=new THREE.ConeGeometry(0.13,0.36,6); bud2.translate(bx,1.5,bz); bud2.scale(1.4,0.9,0.8); B.put(bud2,shadeColor(bloomC,1.2));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a5a44,emissive:0x061008}),{c:o.rimC===undefined?0xa8d8b0:o.rimC,i:o.rim===undefined?0.3:o.rim,p:2.5}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  g.userData.ph=R()*6.283;
  return g;
}

/* 桂树：树冠缀金点（桂子），合批 1 mesh */
function makeOsmanthus(o){
  o=o||{};
  const h=o.h===undefined?4.6:o.h, R=seedRnd(o.seed===undefined?31:o.seed);
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.5-0.25,h*0.55,0],h*0.045,h*0.02,6),0x1a140c);
  const c1=new THREE.SphereGeometry(h*0.30,9,7); c1.scale(1.25,0.8,1.25); c1.translate(0,h*0.72,0); B.put(c1,0x24371e);
  const c2=new THREE.SphereGeometry(h*0.20,8,6); c2.scale(1.2,0.75,1.2); c2.translate(h*0.16,h*0.88,h*0.1); B.put(c2,0x2a4022);
  for(let i=0;i<12;i++){
    const a=R()*6.283, rr=R()*h*0.30;
    const dot=new THREE.SphereGeometry(0.05,5,4);
    dot.translate(Math.cos(a)*rr,h*(0.62+R()*0.3),Math.sin(a)*rr);
    B.put(dot,0xe8c058);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3220,emissive:0x0a0d06}),{c:o.rimC===undefined?0xc8d890:o.rimC,i:o.rim===undefined?0.3:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

function bCover(){ // 封面 · 青绿湖山
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x081009,c2:0x14231a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x0a120c,atmo:0x2c4434,fogK:0.74,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'芦苇',w:80,n:24,d:9,color:0x050a06,seed:5,sway:1.1});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8fb89a,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:70,box:[220,40,130],pos:[0,10,-40],color:0xbfe0c0,size:8,speed:0.05,rise:0,maxA:0.45});
  g.add(motes.points);
  addLights(g,{c:0xa8ccb0,i:0.42,p:[30,70,40]},{c:0x1e2c22,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bDongnan(){ // 一 · 东南形胜 —— 城郭塔影临江，钱塘气象
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a110c,c2:0x18231a}); g.add(grd.mesh);
  const ridge=makeRange({r:210,h:40,layers:3,peaks:5,seed:411,color:0x0b130d,atmo:0x2e4836,fogK:0.62,glowK:0.09});
  g.add(ridge.g);
  /* 江面：城前一条大水 */
  const water=makeWater({size:420,seg:80,amp:0.55,freq:0.09,speed:0.85,flow:[0.4,0.7],spec:1.2,
    deep:0x0a1c22,shallow:0x16404a,skyc:0x245048,moonDir:[60,100,-150]});
  water.mesh.position.set(0,-0.4,-46); g.add(water.mesh);
  /* 城郭：塔楼 + 屋舍群 + 城门楼 */
  function tower(wd,hh,x,z){
    const t=new THREE.Group();
    const B=new GeoBag(), dark=0x141a16;
    const b=new THREE.BoxGeometry(wd,hh,wd*0.8); b.translate(0,hh/2,0); B.put(b,dark);
    const r1=new THREE.ConeGeometry(wd*0.98,wd*0.55,4); r1.rotateY(Math.PI/4); r1.translate(0,hh+wd*0.27,0); B.put(r1,0x1a241c);
    const b2=new THREE.BoxGeometry(wd*0.55,wd*0.5,wd*0.44); b2.translate(0,hh+wd*0.55+wd*0.25,0); B.put(b2,dark);
    const r2=new THREE.ConeGeometry(wd*0.64,wd*0.45,4); r2.rotateY(Math.PI/4); r2.translate(0,hh+wd*0.8+wd*0.22,0); B.put(r2,0x1a241c);
    t.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x2a3a30,emissive:0x060a08}),{c:0x9fc8a8,i:0.2,p:2.4})));
    for(let i=0;i<2;i++){
      const win=new THREE.Mesh(new THREE.PlaneGeometry(1.2,1.6),
        new THREE.MeshBasicMaterial({color:0xe8c878,transparent:true,opacity:0.8}));
      win.position.set((i?1:-1)*wd*0.18,hh*0.55,wd*0.42); t.add(win);
    }
    t.position.set(x,0,z); return t;
  }
  g.add(tower(12,20,-20,-40),tower(16,28,2,-52),tower(10,17,22,-38));
  const houses=makeHouse({n:9,w:44,d:12,seed:41}); houses.g.position.set(0,0,-30); g.add(houses.g);
  /* 城头灯影 */
  const lans=[];
  [-8,0,8].forEach(function(x,i){
    const l=makeLantern(0.55,{flame:i===1}); l.position.set(x,4.6,-24); g.add(l); lans.push(l);
  });
  const mist=makeMist({n:8,spread:[240,26,130],pos:[0,9,-44],scale:74,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x060a07,seed:57,rim:0.15});
  rk.g.position.set(-15,-1.5,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:30,n:12,d:6,color:0x050a06,seed:59,sway:0.9});
  reeds.g.position.set(15,-1.3,11); g.add(reeds.g);
  addLights(g,{c:0xa8ccb0,i:0.45,p:[40,80,-30]},{c:0x1e2c22,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    lans.forEach(function(l){l.update(t,k);});
    rk.update(t,k); reeds.update(t,k);
  }};
}
function bYanliu(){ // 二 · 烟柳画桥 —— 垂柳夹岸、画桥卧波、十万人家
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0a120c,c2:0x18241a}); g.add(grd.mesh);
  const ridge=makeRange({r:220,h:34,layers:2,peaks:4,seed:421,color:0x0b130d,atmo:0x2c4434,fogK:0.62,glowK:0.08});
  g.add(ridge.g);
  /* 河道：画桥下的水 */
  const water=makeWater({size:300,seg:70,amp:0.35,freq:0.11,speed:0.7,flow:[0.8,0.2],spec:1.1,
    deep:0x0a1a18,shallow:0x143a34,skyc:0x22483c,moonDir:[-60,90,-130]});
  water.mesh.rotation.y=0.3; water.mesh.position.set(-4,-0.3,-18); g.add(water.mesh);
  /* 画桥一座 */
  const bridge=makeBridge({w:17,h:3.4}); bridge.g.position.set(-4,0,-16); bridge.g.rotation.y=0.3; g.add(bridge.g);
  /* 烟柳两岸 */
  const willows=[];
  [[-16,-8,0.9,1],[-11,-22,1.05,2],[3,-24,1.0,3],[12,-12,0.95,4],[18,-26,1.1,5],[-20,-30,1.0,6]].forEach(function(p){
    const wl=makeWillow({h:7.5*p[2],seed:p[3]});
    wl.g.position.set(p[0],0,p[1]); g.add(wl.g); willows.push(wl);
  });
  /* 十万人家：两岸屋舍群 + 风帘翠幕（青绿帷幕） */
  const h1=makeHouse({n:7,w:36,d:9,seed:43}); h1.g.position.set(-18,0,-34); g.add(h1.g);
  const h2=makeHouse({n:8,w:44,d:10,seed:45}); h2.g.position.set(12,0,-38); g.add(h2.g);
  const h3=makeHouse({n:5,w:30,d:8,seed:47}); h3.g.position.set(-2,0,-46); g.add(h3.g);
  const curtains=[];
  [[-9,-28,0.4],[6,-30,-0.3],[14,-22,0.2]].forEach(function(p,i){
    const ct=makeCurtain({w:4.2,h:3.4,color:0x1e3a2a,folds:5,deep:0.5});
    ct.g.position.set(p[0],1.7,p[1]); ct.g.rotation.y=p[2]; g.add(ct.g); curtains.push(ct);
  });
  /* 灯串沿街 */
  const lans=[];
  [[-13,-4],[0,-3],[12,-5]].forEach(function(p,i){
    const l=makeLantern(0.5,{flame:i===0}); l.position.set(p[0],5.2,p[1]); g.add(l); lans.push(l);
  });
  const mist=makeMist({n:8,spread:[240,24,130],pos:[0,10,-40],scale:74,color:0x7fa890,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x060a07,seed:61,rim:0.15});
  rk.g.position.set(-13,-1.3,12); g.add(rk.g);
  addLights(g,{c:0xa8ccb0,i:0.45,p:[-40,80,-30]},{c:0x203024,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    willows.forEach(function(wl){wl.update(t,k);});
    lans.forEach(function(l){l.update(t,k);});
    rk.update(t,k);
  }};
}
function bNutao(){ // 三 · 怒涛天堑 —— 云树长堤，怒涛卷雪；市列珠玑
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0c120d,c2:0x1a261c}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:36,layers:2,peaks:4,seed:431,color:0x0b130d,atmo:0x2c4434,fogK:0.60,glowK:0.08});
  g.add(ridge.g);
  /* 大江：怒涛（浪高流急 + 白沫） */
  const water=makeWater({size:560,seg:100,amp:1.7,freq:0.055,speed:1.5,flow:[-1.8,0.9],spec:1.5,
    deep:0x0a1c22,shallow:0x1a4a52,skyc:0x2a544c,moonDir:[-80,100,-150]});
  water.mesh.position.set(0,-0.5,-34); g.add(water.mesh);
  const foam=makeGlow({n:340,box:[190,7,26],pos:[0,2.2,-24],color:0xd8ecf0,size:11,speed:0.95,rise:1,maxA:0.5});
  foam.points.renderOrder=4; g.add(foam.points);
  const spray=makeGlow({n:130,box:[150,14,40],pos:[0,7,-26],color:0xcfe8ec,size:8,speed:0.5,rise:1,maxA:0.35});
  g.add(spray.points);
  /* 长堤 + 云树成列 */
  const dike=new THREE.Mesh(new THREE.BoxGeometry(150,1.6,7),
    new THREE.MeshPhongMaterial({color:0x1c241c,shininess:10,specular:0x36443a}));
  dike.position.set(0,0.6,-12); g.add(dike);
  const trees=[];
  for(let i=0;i<5;i++){
    const tr=makeTree({h:9+i*0.5,seed:81+i,leaf:0x1e3422,rimC:0xa8c890,rim:0.3});
    tr.g.position.set(-36+i*18,1.4,-13); g.add(tr.g); trees.push(tr);
  }
  /* 市列珠玑：堤后市街，摊案 + 珠光 + 罗绮 */
  const tb=makeTable({w:9,d:2.6,h:1.35,wood:0x2a2018}); tb.g.position.set(-7,0,-6.5); g.add(tb.g);
  const tb2=makeTable({w:7,d:2.4,h:1.3,wood:0x2a2018}); tb2.g.position.set(8,0,-7); g.add(tb2.g);
  const pearls=[];
  [[-8.6,1.35,-6.2,0xd88a3a],[-6.4,1.35,-7.0,0x7ac0d8],[-9.6,1.35,-7.2,0xd8d0b0],
   [7.0,1.3,-7.4,0xc0789a],[9.2,1.3,-6.6,0x8ad8a0]].forEach(function(p,i){
    const j=new THREE.Mesh(new THREE.SphereGeometry(0.24,10,8),
      new THREE.MeshPhongMaterial({color:p[3],emissive:shadeColor(p[3],0.4),shininess:90,specular:0xffffff}));
    j.position.set(p[0],p[1]+0.28,p[2]); g.add(j); pearls.push(j);
  });
  const silks=[];
  [[-3.4,-4.5,0x3a6a8a],[-1.8,-4.8,0x8a4a6a],[10.8,-5,0x3a8a5a]].forEach(function(p,i){
    const ct=makeCurtain({w:1.8,h:3.2,color:p[2],folds:3,deep:0.4});
    ct.g.position.set(p[0],1.6,p[1]); g.add(ct.g); silks.push(ct);
  });
  const buyers=makeCrowd({n:8,rect:[-14,-9,26,4],seed:91,color:0x182018,rimC:0xc8b878,rim:0.3,sMin:0.85,sMax:1.1});
  g.add(buyers.mesh);
  const lans=[];
  [[-11,-3],[3,-2.6],[13,-3.4]].forEach(function(p,i){
    const l=makeLantern(0.48,{flame:i===1}); l.position.set(p[0],4.6,p[1]); g.add(l); lans.push(l);
  });
  const mist=makeMist({n:7,spread:[220,24,120],pos:[0,10,-40],scale:70,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.8,w:18,d:7,color:0x060a07,seed:63,rim:0.15});
  rk.g.position.set(-14,-1.4,12); g.add(rk.g);
  addLights(g,{c:0xa8ccb0,i:0.45,p:[-50,80,-40]},{c:0x203024,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); foam.update(t); spray.update(t); mist.update(t,k);
    buyers.update(t);
    lans.forEach(function(l){l.update(t,k);});
    pearls.forEach(function(p,i){ p.material.emissiveIntensity=k*(0.8+0.3*Math.sin(t*2.1+i*1.7)); });
    rk.update(t,k);
  }};
}
function bGuizi(){ // 四（标志性瞬间）· 桂子荷花 —— 重湖叠巘，十里荷花，钓叟莲娃
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0a110c,c2:0x16241a}); g.add(grd.mesh);
  /* 叠巘：重湖后的层叠山影 */
  const ridge=makeRange({r:240,h:52,layers:3,peaks:6,seed:441,color:0x0c140e,atmo:0x32503c,fogK:0.60,glowK:0.09});
  g.add(ridge.g);
  /* 湖面：重湖（里外两片水光） */
  const water=makeWater({size:520,seg:90,amp:0.3,freq:0.12,speed:0.55,flow:[0.2,0.4],spec:1.1,
    deep:0x0a1a16,shallow:0x16443a,skyc:0x275448,moonDir:[-70,110,-150]});
  g.add(water.mesh);
  /* 十里荷花：荷田成片铺向远处 */
  const lotus=[];
  [[-6,2,1.1],[-2.4,5,0.9],[2,1.2,1.0],[6,4.5,0.95],[-10,-3,1.0],[9,-1,0.9],[14,3,1.05],[-15,4,0.9],
   [18,-4,0.95],[-20,-2,1.0],[22,2,0.9],[26,-1,1.0]].forEach(function(p,i){
    const lo=makeLotus({scale:p[2],seed:101+i,bloom:i%3!==0});
    lo.position.set(p[0],0.06,p[1]); g.add(lo); lotus.push(lo);
  });
  const leafGlow=makeGlow({n:120,box:[70,2.4,30],pos:[2,0.9,1.5],color:0x7fd8a0,size:5,speed:0.06,rise:0,maxA:0.3});
  g.add(leafGlow.points);
  /* 三秋桂子：岸上桂树两株 + 金屑香气粒子 */
  const os=[];
  [[-24,-14,1.15],[20,-16,1.0],[2,-20,0.9]].forEach(function(p,i){
    const t=makeOsmanthus({h:5.4*p[2],seed:121+i});
    t.g.position.set(p[0],0,p[1]); g.add(t.g); os.push(t);
  });
  const gold=makeGlow({n:150,box:[80,16,50],pos:[0,5,-12],color:0xe8c058,size:5,speed:0.045,rise:1,maxA:0.5});
  g.add(gold.points);
  /* 钓叟莲娃：一翁垂钓、二娃采莲 */
  const figs=[];
  const old=makeFigure({pose:'独立',robe:0x2c3428,belt:0x6a5a34,hat:'发髻',beard:true,face:0.4,scale:1.05,rim:0.5,rimC:0xc8d890});
  old.position.set(-12,0,7); g.add(old); figs.push(old);
  const boat=new THREE.Mesh(new THREE.CylinderGeometry(1.6,1.1,0.5,10),
    new THREE.MeshPhongMaterial({color:0x241c12,shininess:8}));
  boat.scale.set(2.6,1,0.8); boat.position.set(-12,-0.1,8.8); g.add(boat);
  const girl1=makeFigure({pose:'独立',robe:0x7a4a5a,hat:'发髻',face:-0.6,scale:0.88,rim:0.5,rimC:0xd8a8b8});
  girl1.position.set(4.5,0,6.5); g.add(girl1); figs.push(girl1);
  const girl2=makeFigure({pose:'指月',robe:0x4a6a4a,hat:'发髻',face:0.5,scale:0.86,rim:0.5,rimC:0xc8d8a0,noProp:true});
  girl2.position.set(7.5,0,8); g.add(girl2); figs.push(girl2);
  /* 菱歌：音符号点升起 */
  const notes=[];
  const nGroup=new THREE.Group(); g.add(nGroup);
  for(let i=0;i<12;i++){
    const m=new THREE.SpriteMaterial({map:i%2?noteTex('♫'):noteTex('♪'),transparent:true,
      opacity:0.7,depthWrite:false,blending:THREE.AdditiveBlending});
    const s=new THREE.Sprite(m); s.scale.set(1.8,1.8,1); nGroup.add(s);
    notes.push({s,seed:Math.random()*10,spd:rnd(0.08,0.14),x:rnd(-10,10),z:rnd(2,8)});
  }
  const mist=makeMist({n:8,spread:[240,26,130],pos:[0,10,-46],scale:76,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',w:40,n:16,d:6,color:0x050a06,seed:65,sway:0.9});
  reeds.g.position.set(-16,-1.3,13); g.add(reeds.g);
  addLights(g,{c:0xa8ccb0,i:0.5,p:[-40,90,-40]},{c:0x203024,i:0.58});
  const pl=new THREE.PointLight(0xd8b878,0.8,50); pl.position.set(0,5,0); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); leafGlow.update(t); gold.update(t); mist.update(t,k);
    lotus.forEach(function(lo){ lo.rotation.z=Math.sin(t*0.8+lo.userData.ph)*0.03; });
    figs.forEach(function(f){f.update(t,k);});
    for(const n of notes){
      const life=(t*n.spd+n.seed)%1;
      n.s.position.set(n.x+Math.sin(t*0.7+n.seed*7)*1.4,2.5+life*9,n.z);
      n.s.material.opacity=k*Math.sin(life*Math.PI)*0.7;
    }
    reeds.update(t,k);
    pl.intensity=k*(0.8+Math.sin(t*1.9)*0.1);
  },onEnter(){ pluck(2,0.3,0.13); pluck(4,0.9,0.11); pluck(5,1.5,0.11); }};
}
function bQianqi(){ // 五（末境·可点击）· 千骑高牙 —— 高牙大纛，箫鼓烟霞；点击湖面，荷开桂落
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,bloom:0};
  const grd=makeGround({r:150,c1:0x0a110c,c2:0x18241a}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:56,layers:3,peaks:6,seed:451,color:0x0c140e,atmo:0x32503c,fogK:0.60,glowK:0.09});
  g.add(ridge.g);
  /* 湖山全景：水 + 荷田（点击后层层推开）+ 桂树 */
  const water=makeWater({size:520,seg:90,amp:0.3,freq:0.12,speed:0.55,flow:[0.2,0.4],spec:1.1,
    deep:0x0a1a16,shallow:0x16443a,skyc:0x275448,moonDir:[-70,110,-150]});
  g.add(water.mesh);
  const lotusG=new THREE.Group(); g.add(lotusG);
  const lotus=[];
  for(let i=0;i<16;i++){
    const a=i/16*Math.PI*2, rr=4+(i%4)*3.2;
    const lo=makeLotus({scale:0.9+(i%3)*0.12,seed:131+i,bloom:i%3!==0});
    lo.position.set(Math.cos(a)*rr,0.06,6+Math.sin(a)*rr*0.7);
    lo.userData.r0=rr;
    lotusG.add(lo); lotus.push(lo);
  }
  const os=[];
  [[-26,-16,1.1],[22,-18,0.95]].forEach(function(p,i){
    const t=makeOsmanthus({h:5.6*p[2],seed:141+i});
    t.g.position.set(p[0],0,p[1]); g.add(t.g); os.push(t);
  });
  /* 高牙大纛：中央大旗 + 两侧仪仗 */
  const bigBan=makeBanner({w:4.2,h:5.2,poleH:13,color:0x1e3a28,tip:0x5a9a68});
  bigBan.g.position.set(0,0,-12); g.add(bigBan.g);
  const bans=[];
  [[-10,-9,0.5],[10,-10,-0.5]].forEach(function(p,i){
    const b=makeBanner({w:2.4,h:3.2,poleH:10,color:0x1e3a28,tip:0x5a9a68});
    b.g.position.set(p[0],0,p[1]); b.g.rotation.y=p[2]; g.add(b.g); bans.push(b);
  });
  /* 千骑：行列人影 + 主官按剑 */
  const riders=makeCrowd({n:16,rect:[-24,-22,48,8],seed:151,color:0x16201a,rimC:0xc8d890,rim:0.26,sMin:0.8,sMax:1.05});
  g.add(riders.mesh);
  const boss=makeFigure({pose:'按剑',robe:0x20302a,belt:0x8a6a34,hat:'幞头',beard:true,face:0,scale:1.25,rim:0.6,rimC:0xc8d890});
  boss.position.set(-2.5,0,-8.5); g.add(boss);
  /* 箫鼓：鼓一架 */
  const drum=new THREE.Mesh(new THREE.CylinderGeometry(1.5,1.5,1.0,16),
    new THREE.MeshPhongMaterial({color:0x5a2a1a,shininess:20,specular:0x8a5a3a}));
  drum.rotation.z=Math.PI/2; drum.position.set(7,1.2,-7); g.add(drum);
  /* 桂子金屑（点击后落如金雨） */
  const gold=makeGlow({n:220,box:[90,30,60],pos:[0,18,-2],color:0xe8c058,size:6,speed:0.09,rise:1,maxA:0});
  g.add(gold.points);
  const burst=makeBurst({n:100,color:0xffe0a0,pos:[0,6,3]}); g.add(burst.points);
  const mist=makeMist({n:8,spread:[240,26,130],pos:[0,10,-50],scale:78,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x060a07,seed:67,rim:0.15});
  rk.g.position.set(-15,-1.5,14); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:28,n:12,d:6,color:0x050a06,seed:69,sway:0.8});
  reeds.g.position.set(14,-1.3,13); g.add(reeds.g);
  addLights(g,{c:0xa8ccb0,i:0.48,p:[-40,90,-40]},{c:0x203024,i:0.58});
  const pl=new THREE.PointLight(0xe8c878,1.45,55); pl.position.set(0,7,-4); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.bloom=Math.min(1,ctl.bloom+dt/2.5);
      ridge.update(t,0); water.update(t); mist.update(t,k);
      bigBan.update(t,k); bans.forEach(function(b){b.update(t,k);});
      riders.update(t); boss.update(t,k);
      lotus.forEach(function(lo,i){
        const open=1+ctl.bloom*0.9*(0.5+0.5*Math.sin(i*1.7+t*0.8));
        lo.scale.setScalar(open);
        lo.rotation.z=Math.sin(t*0.8+i)*0.03;
      });
      gold.mat.uniforms.uMaxA.value=k*0.65*ctl.bloom;
      gold.update(t); burst.update(t);
      rk.update(t,k); reeds.update(t,k);
      pl.intensity=k*1.45*(0.62+ctl.bloom*0.36*(0.85+0.15*Math.sin(t*2.6)));   // 基座=满亮度，点亮前仅零头
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.5,0.12); pluck(5,0.9,0.12); bell();
        const fl=$('#flash'); fl.textContent='十里荷花'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
