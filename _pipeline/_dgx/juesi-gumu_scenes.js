/* ================= 绝句·古木阴中 · 三境场景（青绿春晓 · 古木溪桥变体：卷首古木溪桥、古木短篷、杏花柳风）
   本诗专属系统「杏花雨·杨柳风」：皆以触觉写春 —— 雨"欲湿"而未湿、风"不寒"而微暖。
   末境点击杨柳风 → 雨丝加密（杏花雨）、柳丝拂动加剧、杏花瓣落在老僧肩头，题字「杏花雨」。
   与同赛道《三衢道中》（黄鹂绿阴）、《画眉鸟》（金笼林间）不同：本页是古木、溪桥、短篷与柳岸杏花。 ================= */

/* —— 古木：粗壮的老树（宽大浓荫，是"古木阴中"的本体），合批 1 mesh —— */
function makeOldTreeZN(o){
  o=o||{};
  const h=o.h===undefined?6.4:o.h, R=seedRnd(o.seed===undefined?701:o.seed);
  const wood=o.wood===undefined?0x2e2418:o.wood, leaf=o.leaf===undefined?0x2f5230:o.leaf;
  const B=new GeoBag();
  /* 主干（两段，下粗上细）+ 板根 */
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.4,0],h*0.12,h*0.075,9),wood);
  B.put(limbGeo([(R()-0.5)*0.5,h*0.4,0],[(R()-0.5)*1.2,h*0.62,0],h*0.075,h*0.05,8),shadeColor(wood,1.1));
  for(let i=0;i<4;i++){
    const a=i/4*6.283+R()*0.5;
    const rt=new THREE.ConeGeometry(0.5+R()*0.3,1.2+R()*0.8,5);
    rt.rotateZ(Math.sin(a)*0.5); rt.rotateX(Math.cos(a)*0.5);
    rt.translate(Math.sin(a)*h*0.12,0.5,Math.cos(a)*h*0.12); B.put(rt,shadeColor(wood,0.85));
  }
  const tips=[];
  const nb=o.branches===undefined?7:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.34+R()*0.3);
    const p1=[Math.sin(a)*len,h*0.62+len*0.42,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.6,0],p1,h*0.045,h*0.018,6),shadeColor(wood,1.2));
    tips.push(p1);
    if(R()<0.8){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5,p1[1]+len*0.32,p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.022,h*0.009,5),shadeColor(wood,1.35));
      tips.push(p2);
    }
  }
  /* 浓荫：大团叶簇 */
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<3;k++){
      const rr=h*(0.14+R()*0.12);
      const s=new THREE.SphereGeometry(rr,7,6); s.scale(1.25,0.8,1.05);
      s.translate(tp[0]+(R()-0.5)*h*0.4,tp[1]+(R()-0.3)*h*0.24,tp[2]+(R()-0.5)*h*0.4);
      B.put(s,shadeColor(leaf,0.78+R()*0.5));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a5a34,emissive:0x0c1408,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa8d8a0:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.01+0.02*wd)*Math.sin(t*0.45+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 短篷：带篷的小船（"古木阴中系短篷"） —— */
function makeShortBoatZN(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(4.2,0.55,1.5); hull.translate(0,0.28,0); B.put(hull,0x4a3a26);
  const bow=new THREE.ConeGeometry(0.72,1.2,4); bow.rotateY(Math.PI/4); bow.rotateZ(-Math.PI/2); bow.translate(2.1,0.32,0);
  B.put(bow,0x4a3a26);
  const stern=new THREE.ConeGeometry(0.7,1.1,4); stern.rotateY(Math.PI/4); stern.rotateZ(Math.PI/2); stern.translate(-2.1,0.32,0);
  B.put(stern,shadeColor(0x4a3a26,0.9));
  /* 短篷：半圆篷 */
  const canopy=new THREE.CylinderGeometry(0.85,0.85,1.9,10,1,true,0,Math.PI); canopy.rotateZ(Math.PI/2); canopy.rotateY(Math.PI/2);
  canopy.translate(-0.7,0.7,0); B.put(canopy,0x6a5a36);
  const seat=new THREE.BoxGeometry(1.0,0.1,1.2); seat.translate(1.1,0.58,0); B.put(seat,0x5a4a30);
  const rope=new THREE.TorusGeometry(0.22,0.045,5,10); rope.rotateY(Math.PI/2); rope.translate(2.3,0.46,0.45);
  B.put(rope,0x6a6250);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x4a4028,emissive:0x0a0806,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xc8b880:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  const ph=seedRnd(o.seed===undefined?709:o.seed)()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.position.y=(o.y===undefined?0:o.y)+0.05*Math.sin(t*1.1+ph)*kk;
    g.rotation.z=0.025*Math.sin(t*0.8+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 石桥：小石拱桥（拱 + 桥面 + 栏板 + 桥心），合批 1 mesh —— */
function makeBridgeZN(o){
  o=o||{};
  const span=o.span===undefined?16:o.span, w=o.w===undefined?4.4:o.w, rh=o.rh===undefined?2.6:o.rh;
  const stone=o.stone===undefined?0x6a6e64:o.stone;
  const B=new GeoBag();
  /* 桥面：微拱（用三段折线拼） */
  for(let i=0;i<3;i++){
    const seg=new THREE.BoxGeometry(span/3+0.3,0.5,w);
    const x=-span/2+span*(i+0.5)/3;
    const y=rh*(1-Math.pow((x/(span/2)),2)*0.5)+0.25;
    seg.rotateZ(-Math.atan2(2*rh*x/(span*span/4)*1.6,1)*0.5);
    seg.translate(x,y,0);
    B.put(seg,shadeColor(stone,0.9+i*0.06));
  }
  /* 栏板与栏柱 */
  for(let i=0;i<=8;i++){
    const x=-span/2+span*i/8, y=rh*(1-Math.pow((x/(span/2)),2)*0.5)+0.9;
    const p=new THREE.BoxGeometry(0.22,0.9,0.22); p.translate(x,y,w*0.42); B.put(p,shadeColor(stone,1.05));
    const p2=new THREE.BoxGeometry(0.22,0.9,0.22); p2.translate(x,y,-w*0.42); B.put(p2,shadeColor(stone,1.05));
  }
  [1,-1].forEach(function(s){
    for(let i=0;i<8;i++){
      const x=-span/2+span*(i+0.5)/8, y=rh*(1-Math.pow((x/(span/2)),2)*0.5)+1.2;
      const r=new THREE.BoxGeometry(span/8+0.06,0.16,0.14); r.translate(x,y,s*w*0.42); B.put(r,shadeColor(stone,1.15));
    }
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a7a6a,emissive:0x0c100c}),{c:o.rimC===undefined?0xbcd8b0:o.rimC,i:0.24,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* —— 杨柳：垂柳（细长柳丝随风格外易动） —— */
function makeWillowZN(o){
  o=o||{};
  const h=o.h===undefined?5.6:o.h, R=seedRnd(o.seed===undefined?713:o.seed);
  const wood=o.wood===undefined?0x3a3220:o.wood, leaf=o.leaf===undefined?0x6f9a52:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.52,0],h*0.07,h*0.03,7),wood);
  const tips=[];
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.36+R()*0.24);
    const p1=[Math.sin(a)*len,h*0.52+len*0.42,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.5,0],p1,h*0.028,h*0.011,6),shadeColor(wood,1.25));
    tips.push(p1);
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<4;k++){
      const sx=tp[0]+(R()-0.5)*0.8, sz=tp[2]+(R()-0.5)*0.8, len=h*(0.34+R()*0.3);
      B.put(limbGeo([sx,tp[1],sz],[sx+(R()-0.5)*0.4,tp[1]-len*0.6,sz+(R()-0.5)*0.4],0.026,0.018,5),
        shadeColor(leaf,0.85+R()*0.3));
      B.put(limbGeo([sx,tp[1]-len*0.55,sz],[sx+(R()-0.5)*0.7,tp[1]-len,sz+(R()-0.5)*0.7],0.018,0.010,5),
        shadeColor(leaf,0.8+R()*0.4));
      const lf=new THREE.PlaneGeometry(0.6,0.13); lf.rotateZ((R()-0.5)*0.8);
      lf.translate(sx+(R()-0.5)*0.4,tp[1]-len*(0.6+R()*0.35),sz+(R()-0.5)*0.4);
      B.put(lf,shadeColor(0x8fb268,0.8+R()*0.5));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a6a3a,emissive:0x0c1408,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xbcd8a0:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.03+0.09*wd)*Math.sin(t*(0.9+1.6*wd)+ph)*kk;
    g.rotation.x=0.02*Math.sin(t*(1.1+1.4*wd)+ph*1.7)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 杏花：临水一枝杏（粉白花团 + 花蕾） —— */
function makeApricotZN(o){
  o=o||{};
  const h=o.h===undefined?4.2:o.h, R=seedRnd(o.seed===undefined?719:o.seed);
  const wood=o.wood===undefined?0x33281c:o.wood, petal=o.petal===undefined?0xf2dee6:o.petal;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.5,0],h*0.055,h*0.024,7),wood);
  const tips=[];
  const nb=o.branches===undefined?6:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.6, len=h*(0.34+R()*0.26);
    const p1=[Math.sin(a)*len,h*0.5+len*0.46,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.48,0],p1,h*0.024,h*0.01,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.75){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5,p1[1]+len*0.34,p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.012,h*0.005,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<5;k++){
      const cx=tp[0]+(R()-0.5)*1.0, cy=tp[1]+(R()-0.35)*0.7, cz=tp[2]+(R()-0.5)*1.0;
      const pr=0.17+R()*0.09;
      for(let q=0;q<5;q++){
        const aq=q/5*6.283+R()*0.4;
        const pf=new THREE.PlaneGeometry(pr*1.5,pr*0.95);
        pf.rotateZ(aq); pf.rotateX(-0.4+R()*0.8); pf.rotateY(R()*0.6);
        pf.translate(cx+Math.cos(aq)*pr*0.6,cy,cz+Math.sin(aq)*pr*0.6);
        B.put(pf,shadeColor(petal,0.85+R()*0.3));
      }
      if(R()<0.45){ const bd=new THREE.SphereGeometry(pr*0.5,6,5); bd.translate(cx,cy+0.08,cz); B.put(bd,0xd88ea0); }
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x8a94a4,emissive:0x161418,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe0d0d8:o.rimC,i:0.30,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.015+0.03*wd)*Math.sin(t*0.7+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 细雨：杏花时节的细雨（uK 可加密；"沾衣欲湿"的细，靠小而密） —— */
const ZN_RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB; uniform float uSway;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uFall*(0.85+aSeed*0.4);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.3+aSeed*29.0)*uSway;
  vA=smoothstep(0.0,uH*0.06,y)*(1.0-smoothstep(uH*0.9,uH,y));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(160.0/max(1.0,-mv.z)),16.0);
  gl_Position=projectionMatrix*mv;
}`;
const ZN_RAIN_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA; uniform float uK;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.12,0.02,abs(q.x))*smoothstep(0.5,0.05,abs(q.y))*vA*uFade*uMaxA*uK;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeRainZN(o){
  o=o||{};
  const d=Object.assign({n:260,box:[130,22,80],pos:[0,1,-18],fall:0.075,sway:0.3,
    size:3.4,maxA:0.18,c:0xc0d0d8},o);
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
    vertexShader:ZN_RAIN_VERT,fragmentShader:ZN_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update:function(t,k){ m.uniforms.uTime.value=t; m.uniforms.uK.value=k===undefined?1:k; }};
}

/* —— 杏花瓣：落花（可停在老僧肩头：y 落到肩高即驻留） —— */
function makePetalsZN(o){
  o=o||{};
  const n=o.n===undefined?90:o.n, R=seedRnd(o.seed===undefined?727:o.seed);
  const w=o.w===undefined?26:o.w, hh=o.h===undefined?7:o.h, d=o.d===undefined?16:o.d;
  /* 96 枚花瓣改用 InstancedMesh：1 个 draw call（初版逐枚建 Mesh，smoke 抓到 123>120） */
  const geo=new THREE.SphereGeometry(0.07,5,4); geo.scale(1.7,0.3,1.0);
  const mat=new THREE.MeshBasicMaterial({color:0xf2dee6,transparent:true,opacity:0.72,depthWrite:false,side:THREE.DoubleSide});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({x:(R()-0.5)*w,z:(R()-0.5)*d,y0:R()*hh,sp:0.5+R()*0.7,ph:R()*6.283,
      sway:0.4+R()*0.8,land:R()<0.35,s:0.7+R()*0.6});
  }
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh,mat,update:function(t,k,wind,shoulder){
    const kk=k===undefined?1:k, wd=wind===undefined?0:wind, sh=shoulder||null;
    for(let i=0;i<n;i++){
      const it=items[i];
      let y=(it.y0-t*it.sp*(0.6+1.4*wd))%hh; y=(y+hh)%hh;
      const x=it.x+Math.sin(t*(0.4+1.2*wd)+it.ph)*it.sway*(0.4+wd);
      const z=it.z+Math.cos(t*(0.35+wd)+it.ph)*it.sway*0.6;
      if(sh&&it.land){
        const dx=x-sh[0], dz=z-sh[2];
        if(dx*dx+dz*dz<0.9) y=Math.max(y,sh[1]);   /* 落在肩上：不再下落 */
      }
      dm.position.set(x,y,z);
      dm.rotation.set(t*it.sp*0.8+it.ph, it.ph+t*0.5+wd*2.0, Math.sin(t*0.7+it.ph)*0.9);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 古木溪桥 —— 古木浓荫、溪上小桥、短篷泊在树下
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e1c14,c2:0x18301e,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:36,layers:3,peaks:5,seed:1911,color:0x0f2015,atmo:0x35543a,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-10});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const water=makeWater({size:80,seg:36,amp:0.07,freq:0.14,speed:0.4,flow:[0.3,0.6],spec:1.2,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.3});
  water.mesh.scale.set(1,1,0.6); water.mesh.position.set(0,-0.3,-14); g.add(water.mesh);
  const bridge=makeBridgeZN({span:18,w:4.6,rh:2.8,x:2,y:-0.3,z:-12,ry:0}); g.add(bridge.g);
  const tree=makeOldTreeZN({h:7.0,seed:703,scale:1.15}); tree.g.position.set(-11,-1.3,-6); g.add(tree.g);
  const tree2=makeOldTreeZN({h:5.6,seed:707,scale:0.95}); tree2.g.position.set(14,-1.3,-18); g.add(tree2.g);
  const boat=makeShortBoatZN({x:-8.5,y:-0.25,z:-4.5,ry:0.5,seed:711}); g.add(boat.g);
  const willows=[];
  [[9,0,-6,717],[18,0,-10,721]].forEach(function(p,i){
    const w=makeWillowZN({h:5.0,seed:p[3],scale:0.95}); w.g.position.set(p[0],-1.3,p[2]); g.add(w.g); willows.push(w);
  });
  const motes=makeGlow({n:44,box:[180,26,86],pos:[0,9,-22],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,24,100],pos:[0,8,-46],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x060c08,seed:111,rim:0.14,rimC:0x8fc9b8});
  fg.g.position.set(-16,-1.5,30); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:113,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(16,-1.4,22); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-40,80,26]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    const wind=0.3+0.2*Math.sin(t*0.4);
    tree.update(t,k,wind); tree2.update(t,k,wind);
    boat.update(t,k);
    for(let i=0;i<willows.length;i++)willows[i].update(t,k,wind);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bGumu(){ // 一 · 古木短篷 —— 古木阴中系短篷，杖藜扶我过桥东
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e1c14,c2:0x18301e,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:38,layers:3,peaks:5,seed:1921,color:0x0f2015,atmo:0x365438,
    fogK:0.62,glowK:0.05,glow:0xc0e0a8,y:-10});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  const water=makeWater({size:90,seg:38,amp:0.07,freq:0.13,speed:0.42,flow:[0.3,0.6],spec:1.2,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.3});
  water.mesh.scale.set(1,1,0.6); water.mesh.position.set(-2,-0.3,-16); g.add(water.mesh);
  /* 古木当岸、短篷系其阴中 */
  const tree=makeOldTreeZN({h:7.4,seed:723,scale:1.2}); tree.g.position.set(-8,-1.2,-1.5); g.add(tree.g);
  const boat=makeShortBoatZN({x:-6.6,y:-0.25,z:2.6,ry:0.6,seed:729}); g.add(boat.g);
  /* 石桥在东，老僧拄杖过桥 */
  const bridge=makeBridgeZN({span:18,w:4.6,rh:2.8,x:9,y:-0.3,z:-10,ry:0.1}); g.add(bridge.g);
  const monk=makeFigure({pose:'独立',robe:0x6a6452,belt:0x8a7a52,collar:0xf0ead8,hat:'无',
    hair:0xb8b4a8,scale:1.14,rim:0.46,rimC:0xcae8a8,noProp:true});
  monk.position.set(7.0,0.9,-8.6); monk.rotation.y=-1.5; g.add(monk);
  /* 藜杖（独立一根细杖，斜插在僧人右前） */
  const cane=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.06,2.2,6),
    new THREE.MeshPhongMaterial({color:0x6a5a32,shininess:8,specular:0x4a4020,emissive:0x0c0a04}));
  cane.position.set(6.2,1.5,-8.2); cane.rotation.z=0.16; g.add(cane);
  const willows=[];
  [[16,0,-6,731],[3,0,-4,733]].forEach(function(p,i){
    const w=makeWillowZN({h:5.2,seed:p[3],scale:1.0}); w.g.position.set(p[0],-1.2,p[2]); g.add(w.g); willows.push(w);
  });
  const motes=makeGlow({n:42,box:[170,24,84],pos:[0,9,-20],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,100],pos:[0,8,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060c08,seed:115,rim:0.14,rimC:0x8fc9b8});
  fg.g.position.set(-14,-1.4,19); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:117,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(15,-1.3,17); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-38,78,24]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      const wind=0.35+0.25*Math.sin(t*0.45);
      tree.update(t,k,wind); boat.update(t,k); monk.update(t,k);
      for(let i=0;i<willows.length;i++)willows[i].update(t,k,wind);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(3,0.35,0.08); }};
}
function bXinghua(){ // 二（末境·可点击）· 杏花柳风 —— 沾衣欲湿杏花雨，吹面不寒杨柳风
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,rain:0,wind:0};
  const grd=makeGround({r:250,c1:0x0d1a12,c2:0x172c1c,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:2,peaks:5,seed:1931,color:0x0e1e14,atmo:0x33503a,
    fogK:0.60,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const water=makeWater({size:80,seg:34,amp:0.06,freq:0.14,speed:0.4,flow:[0.3,0.6],spec:1.25,
    deep:0x0b2018,shallow:0x2a6448,skyc:0x34705a,moonDir:[60,90,-160],y:-0.3});
  water.mesh.scale.set(1,1,0.55); water.mesh.position.set(-6,-0.3,-14); g.add(water.mesh);
  /* 桥东柳岸：柳成行、杏花临水 */
  const willows=[];
  [[-9,0,-6,737],[-2,0,-9,739],[5,0,-5,743],[12,0,-11,747]].forEach(function(p,i){
    const w=makeWillowZN({h:5.6,seed:p[3],scale:1.05}); w.g.position.set(p[0],-1.2,p[2]); g.add(w.g); willows.push(w);
  });
  const apricots=[];
  [[-13,0,-4,751,1.0],[9,0,-3,753,1.05],[-4,0,-12,757,0.85]].forEach(function(p){
    const a=makeApricotZN({h:4.4,seed:p[3],scale:p[4]}); a.g.position.set(p[0],-1.2,p[2]); g.add(a.g); apricots.push(a);
  });
  /* 老僧拄杖立于柳岸（杏花落肩处） */
  const monk=makeFigure({pose:'独立',robe:0x6a6452,belt:0x8a7a52,collar:0xf0ead8,hat:'无',
    hair:0xb8b4a8,scale:1.16,rim:0.46,rimC:0xcae8a8,noProp:true});
  monk.position.set(1.2,-1.2,-2.2); monk.rotation.y=-1.6; g.add(monk);
  const cane=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.06,2.3,6),
    new THREE.MeshPhongMaterial({color:0x6a5a32,shininess:8,specular:0x4a4020,emissive:0x0c0a04}));
  cane.position.set(0.3,-0.1,-1.9); cane.rotation.z=0.14; g.add(cane);
  /* 细雨（杏花雨）与落花（可落肩） */
  const rainFar=makeRainZN({n:280,box:[150,22,90],pos:[0,1,-22],size:3.4,maxA:0.16});
  const rainNear=makeRainZN({n:120,box:[44,14,20],pos:[1,1,4],size:4.0,maxA:0.19,c:0xd0dce0});
  g.add(rainFar.points,rainNear.points);
  const petals=makePetalsZN({n:96,w:30,h:7,d:18,x:0,y:0,z:-4,seed:761});
  g.add(petals.g);
  const motes=makeGlow({n:40,box:[160,22,84],pos:[0,9,-18],color:0xd8e8a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,96],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x060c08,seed:119,rim:0.14,rimC:0x8fc9b8});
  fg.g.position.set(-13,-1.4,13); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x071009,seed:121,sway:0.9,tip:0x2c4028});
  fg2.g.position.set(13,-1.3,12); g.add(fg2.g);
  addLights(g,{c:0xe0e0a0,i:0.50,p:[-36,76,22]},{c:0x22301f,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.rain=Math.min(1,ctl.rain+dt/2.4); ctl.wind=Math.min(1,ctl.wind+dt/2.0); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const rk=1+0.5*(ctl.rain+0.5*ctl.pulse);
      const wind=(0.3+0.7*ctl.wind)+0.5*ctl.pulse;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      rainFar.update(t,rk); rainNear.update(t,rk*1.05);
      for(let i=0;i<willows.length;i++)willows[i].update(t,k,wind);
      for(let i=0;i<apricots.length;i++)apricots[i].update(t,k,wind);
      petals.update(t,k,wind,[1.2,2.2,-2.2]);   /* 肩高 2.2：落花可停在老僧肩上 */
      monk.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(4,0.20,0.10); pluck(5,0.42,0.09);
        const fl=$('#flash'); fl.textContent='杏花雨'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：雨再细密一分，柳风再柔一阵 */
    },clicked:false};
  return api;
}
