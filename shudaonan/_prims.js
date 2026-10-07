/* ================= 场景构件（大漠金戈 · 剑阁苍崖变体） =================
   本诗专用：峰柱（高标）、绝壁如墙、天梯石栈、飞湍群瀑、枯松/古木、鸟、猿、兽、关门。
   一律合并几何（GeoBag）+ 每帧写 opacity/intensity 必乘 fadeK；材质每次 build 新建。 */

/* ---- 飞湍瀑流：多条瀑布共用一份材质合并成 1 个 draw call（纵向条纹 = 一眼看出是水） ---- */
const FALL2_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const FALL2_FRAG=`
uniform float uTime; uniform float uFade; uniform vec3 uTint; varying vec2 vUv;
float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453123);}
float noise(vec2 p){vec2 i=floor(p);vec2 f=fract(p);f=f*f*(3.0-2.0*f);
 return mix(mix(hash(i),hash(i+vec2(1.0,0.0)),f.x),mix(hash(i+vec2(0.0,1.0)),hash(i+vec2(1.0,1.0)),f.x),f.y);}
float fbm(vec2 p){float v=0.0;float a=0.5;for(int i=0;i<4;i++){v+=a*noise(p);p*=2.03;a*=0.5;}return v;}
void main(){
  vec2 uv=vUv; float t=uTime*2.2;
  /* 细水丝（纵向拉长的 fbm）叠低频大水团：一眼是"水"不是"雾" */
  float s1=fbm(vec2(uv.x*30.0,uv.y*2.0+t*3.4));
  float s2=fbm(vec2(uv.x*7.0+3.0,uv.y*1.1+t*1.6));
  float w=clamp(s1*0.50+s2*0.62,0.0,1.0);
  w=pow(w,1.08);
  vec3 col=mix(uTint*0.30,vec3(0.95,0.98,1.0),w);
  /* 边缘柔化：水帘两侧渐隐、上口从岩缝里渗出、下缘化进白雾 */
  float edge=smoothstep(0.0,0.30,uv.x)*smoothstep(1.0,0.70,uv.x);
  float top=smoothstep(0.0,0.34,1.0-uv.y);
  float bot=smoothstep(0.0,0.22,uv.y);
  float a=uFade*edge*top*bot*(0.20+0.58*w);
  gl_FragColor=vec4(col,a);
}`;
/* 上窄下宽的水面片：瀑布/飞湍的形体感（比矩形面片像水得多） */
function taperPlane(wTop,wBot,h,segY){
  const n=segY||4, pos=[], uv=[], idx=[];
  for(let i=0;i<=n;i++){
    const t=i/n, y=h*t, w=wTop+(wBot-wTop)*t;
    pos.push(-w*0.5,y,0, w*0.5,y,0);
    uv.push(0,t, 1,t);
  }
  for(let i=0;i<n;i++){ const a2=i*2; idx.push(a2,a2+1,a2+2, a2+1,a2+3,a2+2); }
  const g=new THREE.BufferGeometry();
  g.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  g.setAttribute('uv',new THREE.BufferAttribute(new Float32Array(uv),2));
  g.setIndex(idx); g.computeVertexNormals();
  return g;
}
function makeFalls(o){
  o=o||{};
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uFade:{value:0},uTint:{value:C(o.tint===undefined?0xbfe0ff:o.tint)}},
    vertexShader:FALL2_VERT,fragmentShader:FALL2_FRAG});
  const B=new GeoBag();
  (o.items||[]).forEach(function(it){
    const p=taperPlane(it.w*(it.taper===undefined?0.52:it.taper),it.w,it.h,5);
    if(it.ry)p.rotateY(it.ry);
    if(it.rx)p.rotateX(it.rx);
    if(it.rz)p.rotateZ(it.rz);
    p.translate(it.x||0,it.y||0,it.z||0);
    B.put(p,0xffffff);
  });
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat);
  mesh.frustumCulled=false; mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t){ mat.uniforms.uTime.value=t; };
  g.userData.update=g.update;
  return {g,mesh,mat,update:g.update};
}

/* ---- 高标：插入天穹的巨型峰柱（六龙回日之高标）；mat 供"显形"用 ---- */
function makeBiao(o){
  o=o||{};
  const h=o.h===undefined?150:o.h, r=o.r===undefined?22:o.r;
  const col=o.color===undefined?0x2e1d10:o.color;
  const R=seedRnd(o.seed===undefined?91:o.seed), B=new GeoBag();
  const tiers=[[r*1.20,r*0.94,h*0.44],[r*0.90,r*0.62,h*0.30],[r*0.56,r*0.30,h*0.20]];
  let y=0;
  tiers.forEach(function(t,i){
    const gg=new THREE.CylinderGeometry(t[1],t[0],t[2],5+(i%2),1);
    gg.rotateY(R()*6.283);
    gg.translate((R()-0.5)*r*0.30,y+t[2]/2,(R()-0.5)*r*0.20);
    B.put(gg,shadeColor(col,0.84+0.30*R())); y+=t[2]*0.985;
  });
  const tip=new THREE.ConeGeometry(r*0.30,h*0.17,5);
  tip.rotateY(R()*6.283); tip.rotateZ(0.10); tip.translate(0,y+h*0.085,0);
  B.put(tip,shadeColor(col,1.18));
  /* 山脊微光条：把"标"的轮廓从天空里挑出来 */
  const ridge=new THREE.BoxGeometry(r*0.10,h*0.84,r*0.09);
  ridge.rotateZ(-0.05); ridge.translate(-r*0.60,h*0.44,r*0.16);
  B.put(ridge,shadeColor(col,2.1));
  const g=new THREE.Group();
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,flatShading:true,
    shininess:9,specular:0x3e2c18,emissive:0x05040a,transparent:true,opacity:1}),
    {c:o.rimC===undefined?0xe8c070:o.rimC,i:o.rim===undefined?0.38:o.rim,p:2.0});
  const mesh=B.mesh(mat); mesh.frustumCulled=false; g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mesh,mat};
}

/* ---- 绝壁如墙：一排棱面崖体合并成 1 个 mesh（连峰/剑阁的山体） ---- */
function makeCliffWall(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?5:o.seed);
  const n=o.n===undefined?6:o.n, w=o.w===undefined?46:o.w, hh=o.h===undefined?90:o.h;
  const col=o.color===undefined?0x3a2412:o.color, B=new GeoBag();
  const yb=o.y||0;
  for(let i=0;i<n;i++){
    const bw=w*R()*(0.94-0.30*R()), bh=hh*(0.66+1.02*R());
    const bd=(o.d===undefined?26:o.d)*(0.7+0.7*R());
    const x=(i-(n-1)/2)*(o.step===undefined?w*0.76:o.step)+(R()-0.5)*w*0.18;
    const z=(R()-0.5)*(o.zjit===undefined?14:o.zjit);
    const body=new THREE.CylinderGeometry(bw*0.40,bw*0.74,bh,5+(i%3),1);
    body.rotateY(R()*6.283); body.translate(x,yb+bh*0.5,z);
    B.put(body,shadeColor(col,0.80+0.42*R()));
    const sh=new THREE.CylinderGeometry(bw*0.28,bw*0.42,bh*0.20,5);
    sh.rotateY(R()*6.283); sh.translate(x,yb+bh*1.05,z);
    B.put(sh,shadeColor(col,0.88+0.44*R()));
    const base=new THREE.BoxGeometry(bw*1.5,bh*0.09,bd);
    base.rotateY(R()*0.4); base.translate(x,yb+bh*0.045,z);
    B.put(base,shadeColor(col,0.62+0.3*R()));
  }
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,flatShading:true,
    shininess:5,specular:0x2e2014,emissive:0x04030a}),{c:o.rimC===undefined?0xd9a05a:o.rimC,
    i:o.rim===undefined?0.32:o.rim,p:1.98}));
  mesh.frustumCulled=false; g.add(mesh);
  return {g,mesh,mat:mesh.material};
}

/* ---- 栈道 / 盘道：崖壁上一线折行的木栈（天梯石栈、百步九折） ---- */
function makePlankRoad(o){
  o=o||{};
  const pts=(o.pts||[]).map(function(p){ return new THREE.Vector3(p[0],p[1],p[2]); });
  const w=o.w===undefined?2.8:o.w, col=o.color===undefined?0x241a12:o.color;
  const B=new GeoBag();
  for(let i=0;i<pts.length-1;i++){
    const A=pts[i], Bp=pts[i+1];
    const d=new THREE.Vector3().subVectors(Bp,A), len=Math.max(d.length(),0.001);
    const q=new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0,0,1),d.clone().normalize());
    /* r128 的 BufferGeometry 没有 applyQuaternion：走矩阵 */
    const m4=new THREE.Matrix4().makeRotationFromQuaternion(q);
    const deck=new THREE.BoxGeometry(w,0.24,len);
    deck.applyMatrix4(m4); deck.translate((A.x+Bp.x)/2,(A.y+Bp.y)/2,(A.z+Bp.z)/2);
    B.put(deck,shadeColor(col,1.15));
    const nseg=Math.max(2,Math.round(len/1.7));
    for(let k=1;k<nseg;k++){
      const t=k/nseg;
      const bar=new THREE.BoxGeometry(w*1.06,0.09,0.17);
      bar.applyMatrix4(m4);
      bar.translate(A.x+d.x*t,A.y+d.y*t+0.15,A.z+d.z*t);
      B.put(bar,shadeColor(col,1.85));
    }
    for(let k=0;k<=nseg;k+=Math.max(1,Math.round(nseg/3))){
      const t=k/nseg;
      const P=new THREE.Vector3(A.x+d.x*t,A.y+d.y*t,A.z+d.z*t);
      B.put(limbGeo([P.x,P.y-0.12,P.z],[P.x+0.2,P.y-0.7,P.z-1.7],0.13,0.09,5),shadeColor(col,0.80));
      B.put(limbGeo([P.x,P.y-0.12,P.z+w*0.12],[P.x,P.y-2.6,P.z+w*0.12],0.11,0.09,5),shadeColor(col,0.72));
    }
  }
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2a1a,emissive:0x05040a}),{c:o.rimC===undefined?0xe0b070:o.rimC,
    i:o.rim===undefined?0.42:o.rim,p:2.1}));
  mesh.frustumCulled=false; g.add(mesh);
  return {g,mesh};
}

/* ---- 松 / 古木：可直立、可倒挂、可枯（枯松倒挂倚绝壁；悲鸟号古木） ---- */
function makeTree(o){
  o=o||{};
  const h=o.h===undefined?18:o.h, r=o.r===undefined?1.25:o.r;
  const col=o.color===undefined?0x2a2016:o.color;
  const leaf=o.leaf===undefined?0x2b3a26:o.leaf;
  const dead=!!o.dead, hang=!!o.hang, R=seedRnd(o.seed===undefined?17:o.seed);
  const B=new GeoBag(), nseg=o.segs===undefined?5:o.segs;
  const pts=[[0,0,0]];
  let px=0,pz=0;
  for(let k=1;k<=nseg;k++){
    px+=(R()-0.5)*(o.bend===undefined?1.6:o.bend); pz+=(R()-0.5)*0.8;
    pts.push([px,h*k/nseg,pz]);
  }
  for(let k=0;k<pts.length-1;k++){
    B.put(limbGeo(pts[k],pts[k+1],r*(1-k/nseg*0.60),r*(1-(k+1)/nseg*0.60),6),
      shadeColor(col,0.84+0.34*R()));
  }
  /* 根部盘结：倒挂在崖檐上时，锚点必须"咬"住岩石 */
  if(hang){
    const root=new THREE.SphereGeometry(r*1.9,9,7); root.scale(1.3,0.7,1.1);
    root.translate(0,r*0.4,0); B.put(root,shadeColor(col,1.25));
  }
  const nb=o.branches===undefined?6:o.branches;
  for(let k=0;k<nb;k++){
    const t=0.30+0.64*(k+0.4)/nb, idx=Math.min(nseg-1,Math.floor(t*nseg));
    const A=[pts[idx][0],h*t,pts[idx][2]];
    const a=R()*6.283, len=(o.blen===undefined?0.44:o.blen)*h*(0.46+0.66*R())*(1-0.32*t);
    const E=[A[0]+Math.cos(a)*len, A[1]+len*(dead?0.14:0.30)*(R()-0.15), A[2]+Math.sin(a)*len];
    B.put(limbGeo(A,E,r*0.44,r*0.13,5),shadeColor(col,0.88+0.28*R()));
    if(!dead){
      const nl=len*0.95;
      const lp=new THREE.ConeGeometry(nl*0.52,nl*0.62,5);
      lp.rotateX(Math.PI/2); lp.rotateY(-a);
      lp.translate(E[0]+Math.cos(a)*nl*0.26,E[1]+nl*0.06,E[2]+Math.sin(a)*nl*0.26);
      B.put(lp,shadeColor(leaf,0.80+0.52*R()));
    }else{
      /* 枯枝末梢：再分一小杈，倒挂时剪影更像"枯松" */
      B.put(limbGeo(E,[E[0]+Math.cos(a+0.7)*len*0.36,E[1]+len*0.22,E[2]+Math.sin(a+0.7)*len*0.36],
        r*0.13,r*0.05,4),shadeColor(col,1.1));
    }
  }
  if(!dead){
    for(let k=0;k<4;k++){
      const rr=r*(3.4-k*0.62), yy=h*(0.70+k*0.088);
      const cn=new THREE.ConeGeometry(rr,rr*0.72,7);
      cn.translate(pts[nseg][0]*0.55,yy,pts[nseg][2]*0.55);
      B.put(cn,shadeColor(leaf,0.84+0.32*k/4));
    }
  }
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x2e2a20,emissive:0x04050a}),{c:o.rimC===undefined?0xc9a06a:o.rimC,
    i:o.rim===undefined?0.34:o.rim,p:2.2}));
  mesh.frustumCulled=false; g.add(mesh);
  const rz=hang?Math.PI:0;
  g.rotation.z=rz;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.update=function(t,fk){
    if(!o.sway)return;
    g.rotation.z=rz+o.sway*0.022*Math.sin(t*0.85+(o.seed||3));
  };
  g.userData.update=g.update;
  return {g,mesh,update:g.update,mat:mesh.material};
}

/* ---- 鸟：黄鹤 / 悲鸟 / 子规（躯体合并 1 + 双翼 2，可振翅） ---- */
function makeBird(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, col=o.color===undefined?0x0e1014:o.color;
  const g=new THREE.Group();
  const mat=new THREE.MeshBasicMaterial({color:col,side:THREE.DoubleSide});
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.40,2.5,6); body.rotateX(-Math.PI/2); B.put(body,col);
  const head=new THREE.SphereGeometry(0.29,8,6); head.translate(0,0.14,-1.28); B.put(head,shadeColor(col,1.25));
  const beak=new THREE.ConeGeometry(0.11,0.42,4); beak.rotateX(-Math.PI/2); beak.translate(0,0.11,-1.68);
  B.put(beak,shadeColor(col,1.5));
  const tail=new THREE.ConeGeometry(0.30,1.5,4); tail.rotateX(Math.PI/2); tail.translate(0,0.02,1.72);
  B.put(tail,shadeColor(col,0.9));
  g.add(B.mesh(mat));
  const mk=function(sd){
    const geo=new THREE.PlaneGeometry(3.4,0.95);
    geo.translate(1.7*sd,0,0);
    const m=new THREE.Mesh(geo,mat); m.position.set(0.22*sd,0.05,0.08);
    return m;
  };
  const wl=mk(-1), wr=mk(1);
  g.add(wl,wr);
  g.scale.setScalar(s);
  const ph=o.ph===undefined?Math.random()*6.283:o.ph, fl=o.flap===undefined?3.4:o.flap;
  g.update=function(t){ const f=Math.sin(t*fl+ph); wl.rotation.z=f*0.55; wr.rotation.z=-f*0.55; };
  g.userData.update=g.update;
  return g;
}

/* ---- 猿猱：崖壁上攀援的猿（长臂上抓、后腿蜷起、尾垂） ---- */
function makeApe(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, col=o.color===undefined?0x181310:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.60,10,8); body.scale(1.0,1.16,0.86); B.put(body,col);
  const head=new THREE.SphereGeometry(0.33,9,7); head.translate(0,0.90,0.12); B.put(head,shadeColor(col,1.22));
  B.put(limbGeo([0.42,0.40,0],[1.00,1.84,0.18],0.17,0.10,6),col);
  B.put(limbGeo([-0.42,0.40,0],[-0.98,1.84,0.14],0.17,0.10,6),col);
  B.put(limbGeo([0.28,-0.40,0],[0.60,-1.22,0.26],0.15,0.09,6),shadeColor(col,0.94));
  B.put(limbGeo([-0.28,-0.40,0],[-0.62,-1.14,0.22],0.15,0.09,6),shadeColor(col,0.94));
  B.put(limbGeo([0,-0.58,-0.22],[0.10,-1.62,-0.60],0.09,0.03,5),shadeColor(col,0.86));
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x322820,emissive:0x030202}),{c:o.rimC===undefined?0xd9a05a:o.rimC,
    i:o.rim===undefined?0.44:o.rim,p:2.2}));
  mesh.frustumCulled=false; g.add(mesh);
  g.scale.setScalar(s);
  const ph=o.ph===undefined?0:o.ph;
  g.update=function(t){ mesh.rotation.z=0.07*Math.sin(t*0.75+ph); mesh.position.y=0.18*Math.sin(t*0.5+ph); };
  g.userData.update=g.update;
  return g;
}

/* ---- 猛兽剪影（猛虎/豺狼）：磨牙吮血，暗底靠轮廓 + 两点幽光读出 ---- */
function makeBeast(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, col=o.color===undefined?0x140f0a:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.0,10,8); body.scale(1.9,0.80,0.76); body.translate(0,1.16,0); B.put(body,col);
  const neck=new THREE.CylinderGeometry(0.40,0.52,0.92,7); neck.rotateZ(-0.55); neck.translate(1.46,1.48,0);
  B.put(neck,shadeColor(col,1.12));
  const head=new THREE.SphereGeometry(0.45,9,7); head.scale(1.28,0.9,0.9); head.translate(2.06,1.84,0);
  B.put(head,shadeColor(col,1.18));
  const muz=new THREE.ConeGeometry(0.25,0.60,6); muz.rotateZ(-Math.PI/2); muz.translate(2.52,1.76,0);
  B.put(muz,shadeColor(col,0.9));
  [0.24,-0.24].forEach(function(z){
    const ear=new THREE.ConeGeometry(0.16,0.34,5); ear.translate(2.00,2.20,z); B.put(ear,shadeColor(col,1.06));
  });
  [[1.05,1],[-0.95,1],[1.05,-1],[-0.95,-1]].forEach(function(p,i){
    B.put(limbGeo([p[0],0.95,p[1]*0.42],[p[0]+(i%2?0.10:-0.14),0,p[1]*0.54],0.20,0.13,6),shadeColor(col,0.92));
  });
  B.put(limbGeo([-1.70,1.28,0],[-2.70,1.86,0.24],0.15,0.05,5),shadeColor(col,0.86));
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2e2418,emissive:0x030203}),{c:o.rimC===undefined?0xd98e3a:o.rimC,
    i:o.rim===undefined?0.30:o.rim,p:2.2}));
  mesh.frustumCulled=false; g.add(mesh);
  const eyes=makeGlow({n:18,box:[0.9,0.34,0.5],pos:[2.0,1.84,0],color:o.eyeC===undefined?0xd8b060:o.eyeC,
    size:5,speed:0.35,rise:0,maxA:0.72});
  g.add(eyes.points);
  g.scale.setScalar(s);
  g.update=function(t,fk){ const k=fk===undefined?1:fk;
    eyes.update(t);
    eyes.mat.uniforms.uMaxA.value=k*0.72*(0.55+0.45*Math.sin(t*1.7+(o.ph||0)));
  };
  g.userData.update=g.update;
  return g;
}

/* ---- 长蛇（夕避长蛇）：沿岩面起伏的暗色蛇身 ---- */
function makeSnake(o){
  o=o||{};
  const len=o.len===undefined?34:o.len, r=o.r===undefined?0.52:o.r;
  const col=o.color===undefined?0x2b2c18:o.color;
  const pts=[];
  for(let i=0;i<=8;i++){
    const t=i/8;
    pts.push(new THREE.Vector3(-len*0.5+len*t, r*1.2+Math.sin(t*Math.PI*1.75)*2.4,
      Math.cos(t*Math.PI*2.1)*1.8));
  }
  const geo=new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts),40,r,7,false);
  const g=new THREE.Group();
  const mesh=new THREE.Mesh(geo,rimHook(new THREE.MeshPhongMaterial({color:col,shininess:30,
    specular:0x7a7a44,emissive:0x070806}),{c:0xcfc878,i:0.34,p:2.2}));
  mesh.frustumCulled=false; g.add(mesh);
  g.update=function(t){ mesh.position.y=0.22*Math.sin(t*0.5+(o.ph||0)); };
  g.userData.update=g.update;
  return {g,mesh,update:g.update};
}

/* ---- 关门 / 剑阁关楼：两垛墙 + 门洞过梁 + 二层关楼（合并 1 个 mesh） ---- */
function makeGate(o){
  o=o||{};
  const w=o.w===undefined?28:o.w, h=o.h===undefined?24:o.h, d=o.d===undefined?11:o.d;
  const col=o.color===undefined?0x2c1c10:o.color, B=new GeoBag();
  [1,-1].forEach(function(s){
    const bw=w*0.33;
    const wall=new THREE.BoxGeometry(bw,h,d); wall.translate(s*(w*0.5-bw*0.5),h*0.5,0);
    B.put(wall,col);
    const cap=new THREE.BoxGeometry(bw*1.07,h*0.05,d*1.08); cap.translate(s*(w*0.5-bw*0.5),h*1.025,0);
    B.put(cap,shadeColor(col,1.45));
    /* 墙面箭孔（暗点，暗场里读出"关"） */
    for(let k=0;k<3;k++){
      const slit=new THREE.BoxGeometry(bw*0.10,h*0.05,0.6);
      slit.translate(s*(w*0.5-bw*0.5),h*(0.34+k*0.16),d*0.52);
      B.put(slit,shadeColor(col,0.45));
    }
  });
  const lintel=new THREE.BoxGeometry(w*0.36,h*0.15,d*1.05); lintel.translate(0,h*0.925,0);
  B.put(lintel,shadeColor(col,1.22));
  const up=new THREE.BoxGeometry(w*0.50,h*0.34,d*0.84); up.translate(0,h*1.17,0); B.put(up,shadeColor(col,1.08));
  const roof1=new THREE.ConeGeometry(w*0.39,h*0.14,4); roof1.rotateY(Math.PI/4);
  roof1.translate(0,h*1.41,0); B.put(roof1,shadeColor(col,0.66));
  const up2=new THREE.BoxGeometry(w*0.28,h*0.20,d*0.58); up2.translate(0,h*1.56,0); B.put(up2,shadeColor(col,1.14));
  const roof2=new THREE.ConeGeometry(w*0.25,h*0.12,4); roof2.rotateY(Math.PI/4);
  roof2.translate(0,h*1.72,0); B.put(roof2,shadeColor(col,0.60));
  [1,-1].forEach(function(s){
    const leaf=new THREE.BoxGeometry(w*0.155,h*0.80,0.6);
    leaf.translate(s*w*0.082,h*0.40,d*0.26); B.put(leaf,shadeColor(col,0.55));
  });
  const bar=new THREE.BoxGeometry(w*0.32,0.42,0.42); bar.translate(0,h*0.54,d*0.30);
  B.put(bar,0xb8803a);
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,flatShading:true,
    shininess:7,specular:0x34261a,emissive:0x06040a}),{c:o.rimC===undefined?0xffca7a:o.rimC,
    i:o.rim===undefined?0.36:o.rim,p:2.2}));
  mesh.frustumCulled=false; g.add(mesh);
  return {g,mesh};
}

/* ---- 日轮：limbTex（临边昏暗 + 淡斑纹 + 软边）当贴图 + 暖辉，取代"平涂白圆" ---- */
function makeSunDisc(o){
  o=o||{};
  const r=o.r===undefined?20:o.r, g=new THREE.Group();
  const disc=new THREE.Mesh(new THREE.PlaneGeometry(r*2,r*2),
    new THREE.MeshBasicMaterial({map:limbTex(),color:o.color===undefined?0xffe0b0:o.color,
      transparent:true,opacity:o.op===undefined?0.95:o.op,depthWrite:false,fog:false,
      blending:THREE.AdditiveBlending}));
  disc.renderOrder=-7;
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),
    color:o.glowC===undefined?0xff9a3a:o.glowC,transparent:true,opacity:0.62,depthWrite:false,
    fog:false,blending:THREE.AdditiveBlending}));
  const gs=o.glow===undefined?r*11:o.glow; halo.scale.set(gs,gs,1); halo.renderOrder=-7;
  g.add(disc,halo);
  const baseOp=halo.material.opacity;
  g.update=function(t,fk){ const k=fk===undefined?1:fk;
    halo.material.opacity=k*baseOp*(0.86+0.14*Math.sin(t*0.55));
    disc.quaternion.copy(camera.quaternion);
    disc.material.opacity=k*(o.op===undefined?0.95:o.op);
  };
  g.userData.update=g.update;
  return {g,disc,halo,update:g.update};
}

/* ---- 星宿：参宿 / 井宿（星点 + 连线，fog:false，星不吃场景雾） ---- */
function makeAsterism(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const nodes=(o.nodes||[]).map(function(p){ return new THREE.Vector3(p[0]*sc,p[1]*sc,p[2]*sc); });
  const g=new THREE.Group();
  if(!nodes.length)return {g};
  const pts=new THREE.Points(new THREE.BufferGeometry().setFromPoints(nodes),
    new THREE.PointsMaterial({size:o.size===undefined?7:o.size,sizeAttenuation:false,map:circleTex(),
      color:o.color===undefined?0xe4ecff:o.color,transparent:true,opacity:o.op===undefined?0.95:o.op,
      depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  pts.renderOrder=-9; g.add(pts);
  if(o.links&&o.links.length){
    const lp=[];
    o.links.forEach(function(l){ lp.push(nodes[l[0]],nodes[l[1]]); });
    const line=new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(lp),
      new THREE.LineBasicMaterial({color:o.lineColor===undefined?0x8fa8d8:o.lineColor,transparent:true,
        opacity:o.lineOp===undefined?0.34:o.lineOp,fog:false}));
    line.renderOrder=-9; g.add(line);
  }
  return {g,pts};
}

