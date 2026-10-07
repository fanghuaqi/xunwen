/* ================= 临安春雨初霁 · 五境场景（烟雨江南 · 临安客舍变体：卷首雨巷、京华客骑、小楼听雨、矮纸分茶、素衣清明）
   本诗专属系统「夜雨·明朝卖杏花」：小楼听雨一夜，深巷杏花待晓；
   末境点击卖杏花 → 夜雨渐停（雨丝 uStop 收）、深巷花担出巷、叫卖音阶响起、题字「深巷卖杏花」。 ================= */

/* —— 霏霏春雨：雨丝（Points；uStop=1 时雨住，故"夜雨渐停"是可见的） —— */
const LY_RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB; uniform float uSway;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uFall*(0.8+aSeed*0.5);
  float y=mod(p.y-uB-uTime*sp*uH,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.8+aSeed*43.0)*uSway;
  vA=smoothstep(0.0,uH*0.06,y)*(1.0-smoothstep(uH*0.92,uH,y));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(165.0/max(1.0,-mv.z)),22.0);
  gl_Position=projectionMatrix*mv;
}`;
const LY_RAIN_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA; uniform float uStop;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.13,0.03,abs(q.x))*smoothstep(0.5,0.05,abs(q.y))*vA*uFade*uMaxA*(1.0-uStop);
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeRainLY(o){
  o=o||{};
  const d=Object.assign({n:340,box:[170,26,90],pos:[0,1,-24],fall:0.09,sway:0.35,
    size:4.4,maxA:0.20,c:0x9fb3c9},o);
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
      uSway:{value:d.sway},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA},uStop:{value:0}},
    vertexShader:LY_RAIN_VERT,fragmentShader:LY_RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update:function(t,stop){ m.uniforms.uTime.value=t; m.uniforms.uStop.value=stop===undefined?0:stop; }};
}

/* —— 小楼：两层小楼（楼身 + 两层窗 + 檐 + 栏杆），合批 1 mesh；窗内可暖灯 —— */
function makeTowerLY(o){
  o=o||{};
  const w=o.w===undefined?9:o.w, h1=o.h1===undefined?3.4:o.h1, h2=o.h2===undefined?3.0:o.h2;
  const wall=o.wall===undefined?0x2a2e36:o.wall, wood=o.wood===undefined?0x3a2a1e:o.wood;
  const B=new GeoBag();
  const g1=new THREE.BoxGeometry(w,h1,o.d===undefined?6:o.d); g1.translate(0,h1/2,0); B.put(g1,wall);
  const e1=new THREE.ConeGeometry(w*0.78,1.1,4); e1.rotateY(Math.PI/4); e1.translate(0,h1+0.5,0); B.put(e1,wood);
  const g2=new THREE.BoxGeometry(w*0.92,h2,(o.d===undefined?6:o.d)*0.9); g2.translate(0,h1+1.05+h2/2,0);
  B.put(g2,shadeColor(wall,1.06));
  const e2=new THREE.ConeGeometry(w*0.74,1.05,4); e2.rotateY(Math.PI/4);
  e2.translate(0,h1+1.05+h2+0.5,0); B.put(e2,shadeColor(wood,1.12));
  for(let i=0;i<4;i++){
    const x=-w*0.30+w*0.20*i;
    B.put((function(){ const wn=new THREE.BoxGeometry(w*0.13,h2*0.44,0.16); wn.translate(x,h1+1.05+h2*0.55,3.0); return wn; })(),0xf0c070);
    const wn2=new THREE.BoxGeometry(w*0.13,h1*0.4,0.16); wn2.translate(x,h1*0.55,3.0); B.put(wn2,o.warm===undefined?0xd8a860:o.warm);
  }
  /* 二层栏杆 */
  const rt=new THREE.BoxGeometry(w*0.9,0.14,0.20); rt.translate(0,h1+1.2,3.1); B.put(rt,shadeColor(wood,1.3));
  for(let i=0;i<=8;i++){
    const q=new THREE.BoxGeometry(0.12,1.0,0.12); q.translate(-w*0.45+w*0.9*i/8,h1+0.7,3.1); B.put(q,wood);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4250,emissive:0x0c0e14}),{c:o.rimC===undefined?0x9fb3c9:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh};
}

/* —— 深巷：两侧白墙黑瓦夹出一条巷子（左右墙 + 瓦檐 + 巷底门楼），合批 2 mesh —— */
function makeAlleyLY(o){
  o=o||{};
  const len=o.len===undefined?44:o.len, gap=o.gap===undefined?7:o.gap, h=o.h===undefined?4.6:o.h;
  const wall=o.wall===undefined?0x3a3e48:o.wall, tile=o.tile===undefined?0x22262e:o.tile;
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const wl=new THREE.BoxGeometry(1.2,h,len); wl.translate(s*gap/2,h/2,0); B.put(wl,shadeColor(wall,0.9+s*0.06));
    for(let i=0;i<10;i++){
      const t=new THREE.BoxGeometry(1.6,0.18,len*0.09); t.translate(s*(gap/2-0.1),h+0.1,-len/2+len*(i+0.5)/10);
      B.put(t,shadeColor(tile,0.85+(i%2)*0.25));
    }
  });
  const gate=new THREE.BoxGeometry(gap+2.4,0.7,1.4); gate.translate(0,h+0.2,-len*0.42); B.put(gate,tile);
  const gate2=new THREE.BoxGeometry(gap+1.6,0.5,1.0); gate2.translate(0,h+0.7,-len*0.42); B.put(gate2,shadeColor(tile,1.2));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2e3846,emissive:0x080a10}),{c:o.rimC===undefined?0x9fb3c9:o.rimC,i:0.22,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  /* 巷子地面石板 */
  const S=new GeoBag();
  for(let i=0;i<14;i++){
    const st=new THREE.BoxGeometry(1.4,0.12,2.6); st.translate((i%2?0.7:-0.7)+0.0,0.06,-len/2+len*(i+0.5)/14);
    S.put(st,shadeColor(0x5a6068,0.7+(i%3)*0.16));
  }
  const sm=S.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x6a7480,emissive:0x0a0c10}));
  sm.frustumCulled=false; g.add(sm);
  return {g,mesh};
}

/* —— 杏花：临巷一枝（枝干 + 粉白花簇 + 花蕾），合批 1 mesh —— */
function makeApricotLY(o){
  o=o||{};
  const h=o.h===undefined?3.6:o.h, R=seedRnd(o.seed===undefined?97:o.seed);
  const wood=o.wood===undefined?0x2a2018:o.wood, petal=o.petal===undefined?0xf2dfe6:o.petal;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.4,h*0.55,0],h*0.06,h*0.026,6),wood);
  const tips=[];
  const nb=o.branches===undefined?5:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.6, len=h*(0.36+R()*0.3);
    const p1=[Math.sin(a)*len,h*0.55+len*0.4,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.52,0],p1,h*0.024,h*0.01,5),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.7){
      const p2=[p1[0]*1.3,p1[1]+len*0.36,p1[2]*1.3];
      B.put(limbGeo(p1,p2,h*0.012,h*0.005,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<5;k++){
      const cx=tp[0]+(R()-0.5)*0.9, cy=tp[1]+(R()-0.4)*0.6, cz=tp[2]+(R()-0.5)*0.9;
      const pr=0.16+R()*0.08;
      for(let q=0;q<5;q++){
        const aq=q/5*6.283+R()*0.4;
        const pf=new THREE.PlaneGeometry(pr*1.5,pr*0.95);
        pf.rotateZ(aq); pf.rotateX(-0.4+R()*0.8); pf.rotateY(R()*0.6);
        pf.translate(cx+Math.cos(aq)*pr*0.6,cy,cz+Math.sin(aq)*pr*0.6);
        B.put(pf,shadeColor(petal,0.85+R()*0.3));
      }
      if(R()<0.5){ const bd=new THREE.SphereGeometry(pr*0.5,6,5); bd.translate(cx,cy+0.08,cz); B.put(bd,0xd88ea0); }
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a7480,emissive:0x14121a,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xd8c8d0:o.rimC,i:0.28,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.02*Math.sin(t*0.7+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 花担：扁担 + 两只花筐（满装杏花）+ 挑担人，整体成组（末境点击后"出巷"） —— */
function makeFlowerCarryLY(o){
  o=o||{};
  const B=new GeoBag(), S=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.06,0.06,4.4,6); pole.rotateZ(Math.PI/2); pole.translate(0,1.85,0); B.put(pole,0x6a5230);
  [1,-1].forEach(function(s){
    const bk=new THREE.CylinderGeometry(0.62,0.46,0.62,10); bk.translate(s*1.75,1.28,0); B.put(bk,0x8a6a3a);
    const rim=new THREE.TorusGeometry(0.62,0.06,5,12); rim.rotateX(Math.PI/2); rim.translate(s*1.75,1.58,0); B.put(rim,0x6a5230);
  });
  const carry=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a4a3a,emissive:0x0c0a08}),{c:0xd8c8b0,i:0.28,p:2.4}));
  carry.frustumCulled=false;
  const g=new THREE.Group(); g.add(carry);
  /* 筐中杏花：粉白花团（合批到 S） */
  const R=seedRnd(o.seed===undefined?101:o.seed);
  [1,-1].forEach(function(s){
    for(let i=0;i<16;i++){
      const cx=s*1.75+(R()-0.5)*0.9, cy=1.6+R()*0.35, cz=(R()-0.5)*0.9;
      const pr=0.12+R()*0.07;
      const pf=new THREE.PlaneGeometry(pr*1.5,pr*0.95);
      pf.rotateZ(R()*6.283); pf.rotateX(-0.5+R()); pf.rotateY(R()*6.283);
      pf.translate(cx,cy,cz); S.put(pf,shadeColor(0xf2dfe6,0.85+R()*0.3));
    }
  });
  const fl=S.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x6a7480,emissive:0x161418,side:THREE.DoubleSide}),{c:0xe8d8e0,i:0.3,p:2.4}));
  fl.frustumCulled=false; g.add(fl);
  const bearer=makeFigure({pose:'独立',robe:0x4a4a3a,belt:0x8a7a5a,collar:0xd8d8d0,hat:'幞头',
    hair:0x14161c,scale:1.02,rim:0.42,rimC:0xa8c0d8,noProp:true});
  bearer.position.set(0,0,0.9); bearer.rotation.y=Math.PI; g.add(bearer);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.update=function(t,k){ bearer.update(t,k); };
  g.userData.update=g.update;
  return {g,update:g.update};
}

/* —— 书案与分茶：矮案 + 短纸（斜行墨痕）+ 笔 + 茶盏（细乳） —— */
function makeDeskLY(o){
  o=o||{};
  const B=new GeoBag();
  const top=new THREE.BoxGeometry(3.4,0.16,1.7); top.translate(0,0.98,0); B.put(top,0x4a3420);
  const edge=new THREE.BoxGeometry(3.44,0.05,1.74); edge.translate(0,0.90,0); B.put(edge,0x6a4a2a);
  [1,-1].forEach(function(s){
    const lg=new THREE.BoxGeometry(0.16,0.9,1.2); lg.translate(s*1.45,0.45,0); B.put(lg,0x3a2a18);
  });
  /* 矮纸（短纸）+ 斜行墨痕 */
  const paper=new THREE.BoxGeometry(1.5,0.02,1.05); paper.translate(-0.55,1.07,0); B.put(paper,0xe8e2d0);
  for(let i=0;i<4;i++){
    const ln=new THREE.BoxGeometry(0.02,0.008,0.72); ln.rotateY(0.22);
    ln.translate(-1.05+i*0.30,1.085,-0.34+0.05*i); B.put(ln,0x1a1a22);
  }
  /* 笔 */
  const brush=new THREE.CylinderGeometry(0.035,0.045,0.9,6); brush.rotateZ(1.1); brush.translate(0.5,1.14,0.28);
  B.put(brush,0x6a5230);
  const tip=new THREE.ConeGeometry(0.045,0.22,6); tip.rotateZ(1.1); tip.translate(0.92,1.02,0.28); B.put(tip,0x201a14);
  /* 茶盏与细乳 */
  const cup=new THREE.CylinderGeometry(0.30,0.20,0.26,12); cup.translate(1.05,1.19,0.1); B.put(cup,0x8a94a0);
  const milk=new THREE.CylinderGeometry(0.29,0.29,0.06,12); milk.translate(1.05,1.32,0.1); B.put(milk,0xf0f4f8);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x6a6a60,emissive:0x0a0a0c}),{c:0xbfd0e0,i:0.30,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh};
}

/* —— 晴窗：格子窗框 + 一束窗光（只调 scale，不写 opacity） —— */
function makeWindowLY(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, h=o.h===undefined?4.6:o.h, B=new GeoBag();
  const fr=new THREE.BoxGeometry(w,0.24,0.3); fr.translate(0,h,0); B.put(fr,0x4a3a28);
  const fb=new THREE.BoxGeometry(w,0.24,0.3); fb.translate(0,0,0); B.put(fb,0x4a3a28);
  [1,-1].forEach(function(s){ const fv=new THREE.BoxGeometry(0.24,h,0.3); fv.translate(s*w/2,h/2,0); B.put(fv,0x4a3a28); });
  for(let i=1;i<4;i++){ const v=new THREE.BoxGeometry(0.12,h,0.21); v.translate(-w/2+w*i/4,h/2,0); B.put(v,0x3a2e20); }
  for(let i=1;i<3;i++){ const hh=new THREE.BoxGeometry(w,0.12,0.21); hh.translate(0,h*i/3,0); B.put(hh,0x3a2e20); }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a4a44,emissive:0x0a0a0c}),{c:0xbfd0e0,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const beam=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf0f2e8,transparent:true,
    opacity:0.22,depthWrite:false,blending:THREE.AdditiveBlending}));
  beam.scale.set(w*1.5,h*1.6,1); beam.position.set(0,h*0.5,-0.6); beam.renderOrder=3; g.add(beam);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh,beam};
}

/* —— 骑马客：简马（合并）+ 骑者 —— */
function makeHorseRiderLY(o){
  o=o||{};
  const B=new GeoBag();
  const coat=o.coat===undefined?0x3a2c1e:o.coat;
  const body=new THREE.SphereGeometry(0.6,9,7); body.scale(1.7,0.95,0.95); body.translate(0,1.25,0); B.put(body,coat);
  const neck=new THREE.CylinderGeometry(0.17,0.28,0.8,7); neck.rotateZ(-0.6); neck.translate(1.05,1.72,0); B.put(neck,coat);
  const head=new THREE.SphereGeometry(0.19,7,6); head.scale(1.5,0.9,0.8); head.translate(1.48,1.98,0); B.put(head,shadeColor(coat,1.15));
  const tail=new THREE.ConeGeometry(0.14,0.7,6); tail.rotateZ(-1.05); tail.translate(-1.22,1.3,0); B.put(tail,0x1a120c);
  [[0.6,0.24],[-0.6,-0.24]].forEach(function(lg){
    [1,-1].forEach(function(sd){
      const up=new THREE.CylinderGeometry(0.1,0.08,0.7,6); up.translate(lg[0],0.82,0.16*sd); B.put(up,shadeColor(coat,0.96));
      const lo=new THREE.CylinderGeometry(0.07,0.06,0.62,6); lo.translate(lg[0]+lg[1],0.32,0.16*sd); B.put(lo,shadeColor(coat,0.76));
    });
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4a34,emissive:0x0a0806}),{c:0xd8b890,i:0.36,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const rider=makeFigure({pose:'独立',robe:0x2e3a4a,belt:0x8fa8c0,collar:0xe6ecef,hat:'幞头',
    hair:0x14161c,scale:0.98,rim:0.44,rimC:0xa8c0d8,noProp:true});
  rider.position.set(-0.05,1.65,0); g.add(rider);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=seedRnd(o.seed===undefined?113:o.seed)()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k; rider.update(t,kk);
    g.position.y=(o.y===undefined?0:o.y)+0.03*Math.sin(t*1.2+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* ================= 五境 ================= */
function bCover(){ // 卷首 · 临安雨巷 —— 烟雨里的深巷、小楼与巷口一枝杏花
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0c1014,c2:0x18202a,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:34,layers:3,peaks:5,seed:1311,color:0x0d1218,atmo:0x2c3a48,
    fogK:0.62,glowK:0.05,glow:0x9fb3c9,y:-10});
  ridge.g.position.set(0,0,-94); g.add(ridge.g);
  const alley=makeAlleyLY({len:44,gap:7.4,h:4.6,x:-4,y:-1.3,z:-16}); g.add(alley.g);
  const tower=makeTowerLY({w:9,h1:3.4,h2:3.0,x:11,y:-1.3,z:-20}); g.add(tower.g);
  const ap=makeApricotLY({h:3.8,seed:103,scale:1.05}); ap.g.position.set(4.5,-1.3,-8); g.add(ap.g);
  const rainFar=makeRainLY({n:330,box:[190,26,96],pos:[0,1,-28],size:4.2,maxA:0.17});
  const rainNear=makeRainLY({n:130,box:[54,15,24],pos:[2,1,6],size:5.0,maxA:0.20,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const mist=makeMist({n:8,spread:[220,26,110],pos:[0,8,-46],scale:74,color:0x22304a,op:0.12}); g.add(mist.g);
  const motes=makeGlow({n:40,box:[170,24,86],pos:[0,8,-22],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0x080c10,seed:37,rim:0.14,rimC:0x9fb3c9});
  fg.g.position.set(-15,-1.5,30); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x0a1014,seed:39,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(15,-1.4,22); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-40,70,28]},{c:0x1a2430,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    rainFar.update(t,0); rainNear.update(t,0);
    ap.update(t,k);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bJinghua(){ // 一 · 京华客骑 —— 世味年来薄似纱，谁令骑马客京华
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0c1014,c2:0x18202a,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:30,layers:3,peaks:5,seed:1321,color:0x0d1218,atmo:0x2a3846,
    fogK:0.62,glowK:0.05,glow:0x9fb3c9,y:-10});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 京华市楼与街市 */
  const t1=makeTowerLY({w:8,h1:3.2,h2:2.8,x:-13,y:-1.3,z:-24}); g.add(t1.g);
  const t2=makeTowerLY({w:9.5,h1:3.6,h2:3.2,x:13,y:-1.3,z:-28,warm:0xe0b070}); g.add(t2.g);
  const t3=makeTowerLY({w:7,h1:2.8,h2:2.4,x:1,y:-1.3,z:-38}); g.add(t3.g);
  /* 骑马客：牵马入城 */
  const horse=makeHorseRiderLY({scale:1.05,y:-1.3,seed:107}); horse.g.position.set(-1.5,-1.3,-8); horse.g.rotation.y=0.5;
  g.add(horse.g);
  const crowd=makeCrowd({n:3,rect:[-18,-30,16,8],seed:111,color:0x121a20,rimC:0x9fb3c9,rim:0.2});
  g.add(crowd.mesh);
  /* 世味薄似纱：一层低垂的薄雾 */
  const mist=makeMist({n:10,spread:[220,16,96],pos:[0,3.6,-18],scale:58,color:0x2a3a4e,op:0.14});
  g.add(mist.g);
  const rainFar=makeRainLY({n:320,box:[190,24,92],pos:[0,1,-26],size:4.2,maxA:0.16});
  const rainNear=makeRainLY({n:120,box:[50,14,22],pos:[2,1,5],size:4.8,maxA:0.19,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const motes=makeGlow({n:36,box:[160,22,80],pos:[0,7,-20],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x080c10,seed:41,rim:0.14,rimC:0x9fb3c9});
  fg.g.position.set(-14,-1.5,18); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x0a1014,seed:43,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(14,-1.4,16); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-38,68,26]},{c:0x1a2430,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
      rainFar.update(t,0); rainNear.update(t,0);
      horse.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(2,0.35,0.08); }};
}
function bXiaolou(){ // 二 · 小楼听雨 —— 小楼一夜听春雨，深巷明朝卖杏花（诗眼）
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0b0f13,c2:0x161e28,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:30,layers:2,peaks:5,seed:1331,color:0x0c1116,atmo:0x283644,
    fogK:0.60,glowK:0.05,glow:0x9ab0c6,y:-10});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 小楼（窗内暖灯：夜已深，人未眠） */
  const tower=makeTowerLY({w:10,h1:3.6,h2:3.2,x:-5,y:-1.3,z:-16,warm:0xffc070}); g.add(tower.g);
  const alley=makeAlleyLY({len:46,gap:7.2,h:4.4,x:8,y:-1.3,z:-14}); g.add(alley.g);
  const ap=makeApricotLY({h:3.6,seed:115,scale:1.0}); ap.g.position.set(3.0,-1.3,-6); g.add(ap.g);
  const ap2=makeApricotLY({h:3.0,seed:119,scale:0.9}); ap2.g.position.set(11.5,-1.3,-9); g.add(ap2.g);
  /* 夜雨 */
  const rainFar=makeRainLY({n:360,box:[190,26,96],pos:[0,1,-26],size:4.4,maxA:0.19});
  const rainNear=makeRainLY({n:150,box:[52,15,24],pos:[1,1,6],size:5.0,maxA:0.22,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const mist=makeMist({n:8,spread:[210,24,100],pos:[0,7,-44],scale:72,color:0x22304a,op:0.12}); g.add(mist.g);
  const motes=makeGlow({n:38,box:[160,22,84],pos:[0,8,-20],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x080c10,seed:45,rim:0.14,rimC:0x9fb3c9});
  fg.g.position.set(-13,-1.5,16); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:24,n:7,d:6,color:0x060a0e,seed:47,sway:0.6,rim:0.12,rimC:0x9fb3c9});
  fg2.g.position.set(12,-1.3,14); fg2.g.rotation.z=-0.2; g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.42,p:[-36,66,24]},{c:0x1a2430,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      rainFar.update(t,0); rainNear.update(t,0);
      ap.update(t,k); ap2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.3,0.09); pluck(3,1.1,0.08); }};
}
function bFencha(){ // 三 · 矮纸分茶 —— 矮纸斜行闲作草，晴窗细乳戏分茶
  const g=new THREE.Group();
  const grd=makeGround({r:200,c1:0x10141a,c2:0x1c242e,y:-1.1}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:26,layers:2,peaks:4,seed:1341,color:0x0e141c,atmo:0x2a3846,
    fogK:0.60,glowK:0.05,glow:0x9ab0c6,y:-9});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  /* 晴窗（雨后放晴，窗光成束） */
  const win=makeWindowLY({w:7.6,h:4.8,x:-3.4,y:0,z:-6.5}); g.add(win.g);
  const win2=makeWindowLY({w:6.4,h:4.2,x:4.6,y:0,z:-7.6}); g.add(win2.g);
  /* 廊下书案与分茶 */
  const desk=makeDeskLY({x:0.2,y:0,z:-1.2}); g.add(desk.g);
  const poet=makeFigure({pose:'独立',robe:0x2e3a4a,belt:0x8fa8c0,collar:0xe6ecef,hat:'幞头',
    hair:0x14161c,scale:1.1,rim:0.46,rimC:0xa8c0d8,noProp:true});
  poet.position.set(-2.6,0,-1.0); poet.rotation.y=-1.5; g.add(poet);
  const motes=makeGlow({n:36,box:[120,18,66],pos:[0,5,-14],color:0xb8c8d8,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[170,20,80],pos:[0,5,-34],scale:62,color:0x22304a,op:0.11}); g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:2.8,w:12,d:6,color:0x080c10,seed:49,rim:0.14,rimC:0x9fb3c9});
  fg.g.position.set(-11,-1.2,7); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:12,n:6,d:4,color:0x0a1014,seed:51,sway:0.8,tip:0x3a4a34});
  fg2.g.position.set(10,-1.1,6); g.add(fg2.g);
  addLights(g,{c:0xc8d4e0,i:0.50,p:[-30,60,20]},{c:0x202a36,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      win.beam.scale.set(7.6*1.5*(0.95+0.05*Math.sin(t*0.4)),4.8*1.6,1);
      win2.beam.scale.set(6.4*1.5*(0.95+0.05*Math.sin(t*0.36+1)),4.2*1.6,1);
      poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    }};
}
function bSuyi(){ // 四（末境·可点击）· 素衣清明 —— 素衣莫起风尘叹，犹及清明可到家
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,stop:0,carry:0};
  const grd=makeGround({r:250,c1:0x0c1014,c2:0x18202a,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:28,layers:3,peaks:5,seed:1351,color:0x0c1116,atmo:0x2a3846,
    fogK:0.62,glowK:0.05,glow:0x9fb3c9,y:-10});
  ridge.g.position.set(0,0,-98); g.add(ridge.g);
  const alley=makeAlleyLY({len:48,gap:7.6,h:4.6,x:-2,y:-1.3,z:-14}); g.add(alley.g);
  const tower=makeTowerLY({w:8.2,h1:3.2,h2:2.8,x:12,y:-1.3,z:-22,warm:0xe0b070}); g.add(tower.g);
  /* 素衣诗人（牵马将归） */
  const poet=makeFigure({pose:'独立',robe:0xd8dce0,belt:0x8fa8c0,collar:0xf0f4f8,hat:'幞头',
    hair:0x14161c,scale:1.16,rim:0.44,rimC:0xbfd0e0,noProp:true});
  poet.position.set(-4.6,-1.0,-1.6); poet.rotation.y=-1.2; g.add(poet);
  const horse=makeHorseRiderLY({scale:0.95,y:-1.3,seed:123}); horse.g.position.set(-8.0,-1.3,-3.4);
  horse.g.rotation.y=1.2; g.add(horse.g);
  /* 花担（在巷中；点击后出巷） */
  const carry=makeFlowerCarryLY({x:2.2,y:-1.3,z:-12}); g.add(carry.g);
  const ap=makeApricotLY({h:3.4,seed:127,scale:1.0}); ap.g.position.set(6.2,-1.3,-6.4); g.add(ap.g);
  const ap2=makeApricotLY({h:2.8,seed:131,scale:0.9}); ap2.g.position.set(-9.5,-1.3,-8); g.add(ap2.g);
  const rainFar=makeRainLY({n:330,box:[190,24,94],pos:[0,1,-26],size:4.2,maxA:0.18});
  const rainNear=makeRainLY({n:130,box:[50,14,22],pos:[2,1,5],size:4.8,maxA:0.21,c:0xb0c4d4});
  g.add(rainFar.points,rainNear.points);
  const mist=makeMist({n:8,spread:[210,24,100],pos:[0,7,-44],scale:72,color:0x22304a,op:0.12}); g.add(mist.g);
  const motes=makeGlow({n:38,box:[160,22,84],pos:[0,8,-20],color:0xa8c0d4,size:6,speed:0.03,rise:0,maxA:0.12});
  g.add(motes.points);
  const crowd=makeCrowd({n:2,rect:[-24,-34,12,6],seed:137,color:0x121a20,rimC:0x9fb3c9,rim:0.2});
  g.add(crowd.mesh);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x080c10,seed:53,rim:0.14,rimC:0x9fb3c9});
  fg.g.position.set(-14,-1.5,11); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:14,n:7,d:5,color:0x0a1014,seed:55,sway:0.9,tip:0x3a4a34});
  fg2.g.position.set(13,-1.4,10); g.add(fg2.g);
  addLights(g,{c:0xa8bccc,i:0.44,p:[-38,68,26]},{c:0x1a2430,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.stop=Math.min(1,ctl.stop+dt/2.6); ctl.carry=Math.min(1,ctl.carry+dt/3.2); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const st=Math.min(1,ctl.stop+0.3*ctl.pulse);
      ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
      rainFar.update(t,st); rainNear.update(t,st);
      /* 花担出巷：由巷中推到巷口（只动位置，不动 opacity） */
      carry.g.position.set(2.2+ctl.carry*5.4,-1.3,-12+ctl.carry*7.2);
      carry.update(t,k);
      poet.update(t,k); horse.update(t,k); ap.update(t,k); ap2.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.12); pluck(4,0.22,0.11); pluck(3,0.46,0.10); pluck(5,0.72,0.09);
        const fl=$('#flash'); fl.textContent='深巷卖杏花'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：雨再收一分，花担再出一程 */
    },clicked:false};
  return api;
}
