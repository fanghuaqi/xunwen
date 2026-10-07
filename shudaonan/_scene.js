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
  vec2 uv=vUv; float t=uTime*2.4;
  /* 纵向拉长的水丝 + 低频大水团：飞湍不是雾 */
  float s1=fbm(vec2(uv.x*24.0,uv.y*2.4+t*3.6));
  float s2=fbm(vec2(uv.x*6.0+3.0,uv.y*1.3+t*1.8));
  float w=clamp(s1*0.52+s2*0.58,0.0,1.0);
  w=pow(w,1.02);
  vec3 col=mix(uTint*0.42,vec3(0.97,0.99,1.0),w);
  float edge=smoothstep(0.0,0.16,uv.x)*smoothstep(1.0,0.84,uv.x);
  float top=smoothstep(0.0,0.14,1.0-uv.y);
  float bot=smoothstep(0.0,0.09,uv.y);
  float a=uFade*edge*top*bot*(0.34+0.66*w);
  gl_FragColor=vec4(col,a);
}`;
function makeFalls(o){
  o=o||{};
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uFade:{value:0},uTint:{value:C(o.tint===undefined?0xbfe0ff:o.tint)}},
    vertexShader:FALL2_VERT,fragmentShader:FALL2_FRAG});
  const B=new GeoBag();
  (o.items||[]).forEach(function(it){
    const p=new THREE.PlaneGeometry(it.w,it.h,1,1);
    p.translate(0,it.h/2,0);
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
  const w=o.w===undefined?2.8:w, col=o.color===undefined?0x241a12:o.color;
  const B=new GeoBag();
  for(let i=0;i<pts.length-1;i++){
    const A=pts[i], Bp=pts[i+1];
    const d=new THREE.Vector3().subVectors(Bp,A), len=Math.max(d.length(),0.001);
    const q=new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0,0,1),d.clone().normalize());
    const deck=new THREE.BoxGeometry(w,0.24,len);
    deck.applyQuaternion(q); deck.translate((A.x+Bp.x)/2,(A.y+Bp.y)/2,(A.z+Bp.z)/2);
    B.put(deck,shadeColor(col,1.15));
    const nseg=Math.max(2,Math.round(len/1.7));
    for(let k=1;k<nseg;k++){
      const t=k/nseg;
      const bar=new THREE.BoxGeometry(w*1.06,0.09,0.17);
      bar.applyQuaternion(q);
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
  const h=o.h===undefined?18:o.h, r=o.r===undefined?0.9:o.r;
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
  const w=o.w===undefined?28:w, h=o.h===undefined?24:h, d=o.d===undefined?11:d;
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

/* ---------------- 卷首 + 七境 ---------------- */
function bCover(){ // 卷首 · 苍茫层峦，一线鸟道
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0a0806,c2:0x2c1e12});
  grd.mesh.position.y=-8; g.add(grd.mesh);
  const far=makeRange({r:345,h:92,layers:3,peaks:6,seed:20260929,color:0x150f09,atmo:0x7a4a24,
    fogK:0.60,glowK:0.10,y:-20});
  g.add(far.g);
  const cL=makeCliffWall({n:3,h:62,w:52,seed:311,color:0x33210f,rimC:0xd9a05a,rim:0.30,y:-12,zjit:16});
  cL.g.position.set(-108,-4,-96); cL.g.rotation.y=0.30; g.add(cL.g);
  const cR=makeCliffWall({n:3,h:54,w:48,seed:317,color:0x2c1c0e,rimC:0xd9a05a,rim:0.30,y:-12,zjit:16});
  cR.g.position.set(112,-4,-88); cR.g.rotation.y=-0.28; g.add(cR.g);
  const road=makePlankRoad({w:3.0,color:0x241a12,
    pts:[[-58,44,-64],[-30,50,-62],[-2,45,-60],[26,52,-62],[54,47,-64]]});
  g.add(road.g);
  const birds=new THREE.Group(); g.add(birds);
  const bs=[];
  for(let i=0;i<3;i++){ const b=makeBird({scale:2.2,color:0x120d09,ph:i*1.7,flap:2.0}); birds.add(b); bs.push(b); }
  const sun=makeDisc({r:23,color:0xffe0b0,glowC:0xd97a2a,glow:240});
  sun.g.position.set(-92,52,-330); g.add(sun.g);
  const mist=makeMist({n:12,spread:[340,34,180],pos:[0,18,-124],scale:96,color:0x9a7048,op:0.13});
  g.add(mist.g);
  const flow=makeFlow({n:700,box:[260,30,190],pos:[0,22,-92],color:0xb08a5a,size:22,speed:3.0,maxA:0.24});
  g.add(flow.points);
  const motes=makeGlow({n:80,box:[260,50,140],pos:[0,26,-72],color:0xd9a05a,size:8,speed:0.05,rise:0,maxA:0.38});
  g.add(motes.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:6.4,w:30,d:12,color:0x060403,seed:41,rim:0.16,rimC:0xb07a44});
  fgL.g.position.set(-42,-7,24); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:4.8,w:26,d:10,color:0x060403,seed:47,rim:0.16,rimC:0xb07a44});
  fgR.g.position.set(44,-7,18); g.add(fgR.g);
  addLights(g,{c:0xe0b070,i:0.58,p:[-150,90,-140]},{c:0x3c2c1c,i:0.62});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.6); mist.update(t,k); flow.update(t); motes.update(t);
    fgL.update(t,k); fgR.update(t,k); road.g.update(t,k);
    for(let i=0;i<bs.length;i++){
      const b=bs[i], a=t*0.07+i*2.1;
      b.update(t);
      b.position.set(-30+Math.sin(a)*78,62+Math.sin(t*0.4+i*1.3)*4,-168+Math.cos(a)*46);
      b.rotation.y=-a+Math.PI/2;
    }
  }};
}
function bWeihu(){ // 一 · 危乎高哉 —— 层峦直逼天穹，云海茫然
  const g=new THREE.Group();
  const grd=makeGround({r:230,c1:0x0b0805,c2:0x2e2013});
  grd.mesh.position.y=-10; g.add(grd.mesh);
  const far=makeRange({r:335,h:112,layers:3,peaks:7,seed:1201,color:0x1a120b,atmo:0x8a5426,fogK:0.56,glowK:0.13,y:-24});
  g.add(far.g);
  const mid=makeCliffWall({n:5,h:104,w:48,seed:1207,color:0x3a240f,rimC:0xe8b070,rim:0.36,y:-16,zjit:20});
  mid.g.position.set(0,-6,-124); g.add(mid.g);
  const sun=makeDisc({r:27,color:0xffe8c0,glowC:0xe08a30,glow:290});
  sun.g.position.set(104,88,-300); g.add(sun.g);
  const mist=makeMist({n:13,spread:[330,42,170],pos:[0,34,-124],scale:106,color:0xa87c50,op:0.155});
  g.add(mist.g);
  const low=makeMist({n:8,spread:[300,20,150],pos:[0,14,-98],scale:82,color:0x8a6440,op:0.13});
  g.add(low.g);
  const flow=makeFlow({n:900,box:[280,34,200],pos:[0,26,-92],color:0xbb8f58,size:24,speed:3.6,maxA:0.26});
  g.add(flow.points);
  const motes=makeGlow({n:90,box:[260,60,150],pos:[0,32,-82],color:0xe0a860,size:9,speed:0.05,rise:0,maxA:0.40});
  g.add(motes.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:6.8,w:32,d:12,color:0x060403,seed:1209,rim:0.18,rimC:0xb88048});
  fgL.g.position.set(-46,-8,26); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:3,r:5.4,w:28,d:10,color:0x060403,seed:1213,rim:0.18,rimC:0xb88048});
  fgR.g.position.set(48,-8,20); g.add(fgR.g);
  addLights(g,{c:0xe8b478,i:0.64,p:[130,90,-140]},{c:0x42301e,i:0.64});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.5); mist.update(t,k); low.update(t,k);
    flow.update(t); motes.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bNiandao(){ // 二 · 鸟道天梯 —— 天梯石栈相钩连，崖底是地崩山摧的乱石
  const g=new THREE.Group();
  const grd=makeGround({r:190,c1:0x090705,c2:0x261a10});
  grd.mesh.position.y=-30; g.add(grd.mesh);
  const far=makeRange({r:300,h:92,layers:2,peaks:6,seed:2201,color:0x150f0a,atmo:0x5a4028,fogK:0.64,glowK:0.08,y:-36});
  g.add(far.g);
  const cliff=makeCliffWall({n:3,h:132,w:60,seed:2203,color:0x3e2511,rimC:0xe8b478,rim:0.40,y:-34,zjit:12});
  cliff.g.position.set(8,-2,-58); g.add(cliff.g);
  const road=makePlankRoad({w:3.4,color:0x2a1c10,rimC:0xe8b478,rim:0.46,
    pts:[[-34,-28,-30],[-18,-20,-32],[6,-22,-34],[22,-14,-36],[2,-8,-38],[-16,-2,-40],
         [-4,6,-42],[16,10,-44],[4,20,-46],[-8,28,-48]]});
  g.add(road.g);
  const ledge=makePlankRoad({w:1.6,color:0x1a120b,rimC:0xc9a06a,rim:0.34,
    pts:[[-44,44,-50],[-10,48,-52],[28,44,-54],[60,48,-56]]});
  g.add(ledge.g);
  const bird=makeBird({scale:3.4,color:0x110c08,ph:0.6,flap:2.6});
  g.add(bird);
  const rocks=[];
  [[-52,-26,-10,7.5],[16,-27,4,6.2],[48,-25,-14,8.4],[-18,-28,10,5.0],[36,-27,18,4.2]].forEach(function(p,i){
    const r=makeForeground({kind:'坡石',n:1,r:p[3],w:0,d:0,color:0x0b0705,seed:2210+i,rim:0.24,rimC:0xc08a4a});
    r.g.position.set(p[0],p[1],p[2]); g.add(r.g); rocks.push(r);
  });
  const mist=makeMist({n:10,spread:[240,26,120],pos:[0,-12,-48],scale:78,color:0x8a6a48,op:0.15});
  g.add(mist.g);
  const dust=makeFlow({n:600,box:[220,26,160],pos:[0,-2,-52],color:0xa8825a,size:22,speed:2.6,maxA:0.22});
  g.add(dust.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:7.4,w:34,d:14,color:0x050303,seed:2217,rim:0.15,rimC:0xa87848});
  fgL.g.position.set(-54,-9,24); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:5.8,w:30,d:12,color:0x050303,seed:2221,rim:0.15,rimC:0xa87848});
  fgR.g.position.set(56,-9,18); g.add(fgR.g);
  addLights(g,{c:0xd9a05a,i:0.52,p:[-100,80,-100]},{c:0x37271a,i:0.60});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.5); mist.update(t,k); dust.update(t);
    fgL.update(t,k); fgR.update(t,k); road.g.update(t,k); ledge.g.update(t,k);
    bird.update(t);
    bird.position.set(-24+Math.sin(t*0.16)*44,56+Math.sin(t*0.5)*3,-62);
    bird.rotation.y=-t*0.16+Math.PI/2;
    for(const r of rocks) r.update(t,k);
  }};
}
function bGaobiao(){ // 三 · 高标回川 —— 六龙回日之高标，冲波逆折之回川
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:76,amp:2.5,freq:0.055,speed:1.5,flow:[0,-2.8],spec:1.8,
    deep:0x0c1216,shallow:0x28383a,skyc:0x74451f,moonDir:[-0.45,0.5,-1],moonColor:0xffd9a0,y:-3});
  g.add(water.mesh);
  const biao=makeBiao({h:172,r:25,color:0x30200f,seed:3301,rim:0.44,rimC:0xf0c880});
  biao.g.position.set(-8,-8,-104); g.add(biao.g);
  const sun=makeDisc({r:21,color:0xfff4d2,glowC:0xff9a3a,glow:270});
  sun.g.position.set(34,70,-268); g.add(sun.g);
  const cL=makeCliffWall({n:3,h:98,w:52,seed:3305,color:0x2c1b0e,rimC:0xd9a05a,rim:0.34,y:-26,zjit:14});
  cL.g.position.set(-104,-6,-80); cL.g.rotation.y=0.26; g.add(cL.g);
  const cR=makeCliffWall({n:3,h:88,w:48,seed:3309,color:0x281808,rimC:0xd9a05a,rim:0.34,y:-26,zjit:14});
  cR.g.position.set(106,-6,-74); cR.g.rotation.y=-0.24; g.add(cR.g);
  const foam=makeGlow({n:460,box:[150,10,60],pos:[0,2,-62],color:0xe4f2ff,size:13,speed:0.9,rise:1,maxA:0.56});
  foam.points.renderOrder=4; g.add(foam.points);
  const spray=makeGlow({n:240,box:[140,20,52],pos:[0,7,-64],color:0xeff8ff,size:9,speed:1.2,rise:1,maxA:0.42});
  spray.points.renderOrder=4; g.add(spray.points);
  const crane=makeBird({scale:6.4,color:0x15141a,flap:2.0,ph:0.4});
  g.add(crane);
  const apeL=makeApe({scale:2.6,ph:0.2,color:0x181310}), apeR=makeApe({scale:2.1,ph:1.5,color:0x1c150f});
  apeL.position.set(-70,-4,-62); apeL.rotation.y=0.5; g.add(apeL);
  apeR.position.set(-38,6,-60); apeR.rotation.y=0.25; g.add(apeR);
  const mist=makeMist({n:10,spread:[270,32,130],pos:[0,24,-84],scale:82,color:0xa07850,op:0.12});
  g.add(mist.g);
  const fog=makeMist({n:7,spread:[200,14,90],pos:[0,4,-58],scale:60,color:0xbfd0dc,op:0.13});
  g.add(fog.g);
  const fgL=makeForeground({kind:'岩壁',n:3,r:7.0,w:32,d:13,color:0x050303,seed:3313,rim:0.16,rimC:0xb88048});
  fgL.g.position.set(-50,-8,20); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:2,r:5.6,w:28,d:11,color:0x050303,seed:3317,rim:0.16,rimC:0xb88048});
  fgR.g.position.set(52,-8,14); g.add(fgR.g);
  addLights(g,{c:0xe8bc82,i:0.74,p:[110,90,-140]},{c:0x40301e,i:0.62});
  const pl=new THREE.PointLight(0xcfe4ff,0.55,180); pl.position.set(0,10,-60); g.add(pl);
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); mist.update(t,k); fog.update(t,k); foam.update(t); spray.update(t);
    fgL.update(t,k); fgR.update(t,k);
    apeL.update(t); apeR.update(t);
    const a=t*0.14;
    crane.update(t);
    crane.position.set(-4+Math.sin(a)*56,64+Math.sin(t*0.45)*5,-120+Math.cos(a)*30);
    crane.rotation.y=-a+Math.PI/2;
    pl.intensity=k*(0.42+0.13*Math.sin(t*1.9));
    foam.mat.uniforms.uMaxA.value=k*(0.34+0.22*Math.sin(t*0.8));
  }};
}
function bShenjing(){ // 四 · 扪参历井 —— 百步九折，仰可扪星，抚膺长叹
  const g=new THREE.Group();
  const grd=makeGround({r:170,c1:0x080706,c2:0x1e1710}); grd.mesh.position.y=-26; g.add(grd.mesh);
  const far=makeRange({r:285,h:100,layers:2,peaks:6,seed:4401,color:0x0f0e12,atmo:0x3c3c50,fogK:0.70,glowK:0.05,y:-30});
  g.add(far.g);
  const can=makeAsterism({size:9,op:0.96,
    nodes:[[-124,206,-334],[-96,244,-338],[-66,216,-342],[-72,188,-344],[-100,176,-346],[-30,224,-348],[-16,196,-350]],
    links:[[0,1],[1,2],[2,3],[3,4],[4,0],[1,5],[5,6],[6,2]]});
  g.add(can.g);
  const jing=makeAsterism({size:8,op:0.92,color:0xd6e4ff,lineColor:0x9fb6e0,lineOp:0.30,
    nodes:[[52,176,-340],[82,176,-342],[52,206,-344],[82,206,-346],[67,191,-348]],
    links:[[0,1],[0,2],[1,3],[2,3]]});
  g.add(jing.g);
  const cliff=makeCliffWall({n:3,h:116,w:48,seed:4407,color:0x261b13,rimC:0xb8b0c8,rim:0.32,y:-28,zjit:12});
  cliff.g.position.set(6,-6,-74); g.add(cliff.g);
  const road=makePlankRoad({w:3.2,color:0x241a12,rimC:0xc9c0d8,rim:0.40,
    pts:[[-42,-24,-44],[-22,-16,-46],[4,-18,-48],[24,-10,-50],[2,-4,-52],[-20,2,-54],
         [-2,8,-56],[20,12,-58],[0,18,-60],[-16,24,-62]]});
  g.add(road.g);
  const f=makeFigure({pose:'坐饮',robe:0x1e2028,belt:0x6a5638,hat:'幞头',beard:true,scale:2.1,face:0.35,
    rim:0.66,rimC:0xc9b090,noProp:true});
  f.position.set(8,-11.4,-48); g.add(f);
  const mist=makeMist({n:9,spread:[240,26,120],pos:[0,2,-60],scale:76,color:0x7a7286,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:120,box:[200,120,140],pos:[0,60,-80],color:0xcfd8ff,size:6,speed:0.03,rise:0,maxA:0.5});
  g.add(motes.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:6.6,w:30,d:12,color:0x040405,seed:4411,rim:0.18,rimC:0x9a92b0});
  fgL.g.position.set(-46,-9,18); g.add(fgL.g);
  const fgR=makeForeground({kind:'树枝',n:20,w:34,d:5,color:0x040405,seed:4417,sway:0.5});
  fgR.g.position.set(30,-6,16); g.add(fgR.g);
  addLights(g,{c:0x9fb0d8,i:0.34,p:[-80,110,-160]},{c:0x2a2c3c,i:0.58});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.4); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k); road.g.update(t,k); f.update(t,k);
  }};
}
function bZigui(){ // 五 · 悲鸟子规 —— 悲鸟绕古木，子规啼夜月，朱颜凋落
  const g=new THREE.Group();
  const grd=makeGround({r:180,c1:0x08070a,c2:0x1e1812}); grd.mesh.position.y=-12; g.add(grd.mesh);
  const far=makeRange({r:305,h:96,layers:3,peaks:6,seed:5501,color:0x100e11,atmo:0x4e3c34,fogK:0.62,glowK:0.06,y:-18});
  g.add(far.g);
  const trees=[];
  const t1=makeTree({h:32,bend:3.8,branches:9,blen:0.50,leaf:0x2a3a2a,color:0x2a2018,seed:5503,sway:0.5});
  t1.g.position.set(-26,-12,-46); g.add(t1.g); trees.push(t1);
  const t2=makeTree({h:25,bend:3.0,branches:8,blen:0.56,leaf:0x243424,color:0x241c14,seed:5507,sway:0.6});
  t2.g.position.set(24,-12,-52); g.add(t2.g); trees.push(t2);
  const t3=makeTree({h:21,bend:4.4,branches:7,blen:0.62,dead:true,color:0x201811,seed:5511,sway:0.5});
  t3.g.position.set(-2,-12,-40); g.add(t3.g); trees.push(t3);
  const birds=[];
  for(let i=0;i<2;i++){ const b=makeBird({scale:3.0+i*0.5,color:0x161418,flap:3.6,ph:i*2.4}); g.add(b); birds.push(b); }
  const zigui=makeBird({scale:1.7,color:0x1c1a20,flap:0.5,ph:1.1});
  g.add(zigui);
  const leaves=makeGlow({n:100,box:[74,44,44],pos:[0,26,-36],color:0xb8402a,size:7,speed:0.075,rise:1,maxA:0.66});
  leaves.points.renderOrder=4; g.add(leaves.points);
  const mist=makeMist({n:11,spread:[265,26,140],pos:[0,4,-56],scale:86,color:0x7c6c6c,op:0.13});
  g.add(mist.g);
  const br=makeForeground({kind:'树枝',n:24,w:38,d:5,color:0x050405,seed:5517,sway:0.55});
  br.g.position.set(8,-4,18); g.add(br.g);
  const fg=makeForeground({kind:'岩壁',n:2,r:5.2,w:26,d:10,color:0x050405,seed:5519,rim:0.16,rimC:0x9a8a8a});
  fg.g.position.set(-34,-9,14); g.add(fg.g);
  addLights(g,{c:0xc4d2e8,i:0.36,p:[-80,100,-160]},{c:0x2c2e3c,i:0.60});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    far.update(t,mouse.x*0.4); mist.update(t,k); leaves.update(t);
    fg.update(t,k); br.update(t,k);
    for(const tr of trees) tr.update(t,k);
    for(let i=0;i<birds.length;i++){
      const a=t*(0.30+i*0.07)+i*2.6;
      birds[i].update(t);
      birds[i].position.set(-12+Math.sin(a)*26,26+Math.cos(a*1.4)*7+ (i?2:0),-46+Math.cos(a)*16);
      birds[i].rotation.y=-a+Math.PI/2;
    }
    zigui.update(t);
    zigui.position.set(-4.5,18.4,-40.5);
    zigui.rotation.y=2.3;
  }};
}
function bLianfeng(){ // 六 · 连峰飞湍（标志性瞬间）—— 绝壁如墙逼近天穹，枯松倒挂，飞瀑坠雷
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0b0806,c2:0x2c2014}); grd.mesh.position.y=-6; g.add(grd.mesh);
  const far=makeRange({r:305,h:152,layers:3,peaks:7,seed:6601,color:0x1c140c,atmo:0x9a6a34,fogK:0.50,glowK:0.15,y:-32});
  g.add(far.g);
  const wall=makeCliffWall({n:7,h:116,w:50,seed:6607,color:0x442a13,rimC:0xf4c884,rim:0.42,y:-16,zjit:18});
  wall.g.position.set(0,-2,-76); g.add(wall.g);
  const biao=makeBiao({h:180,r:27,color:0x2c1c10,seed:6611,rim:0.46,rimC:0xffd48a,transparent:true});
  biao.g.position.set(-38,-12,-196); g.add(biao.g);
  const pines=[];
  [[-64,42,-60,1.10,7],[-34,54,-62,1.28,9],[6,46,-58,0.98,11],[36,58,-62,1.32,13],[64,48,-60,1.08,17]]
  .forEach(function(p){
    const tr=makeTree({h:26*p[3],bend:3.2,branches:8,blen:0.52,dead:true,hang:true,color:0x241a12,
      seed:p[4],sway:0.7});
    tr.g.position.set(p[0],p[1],p[2]); g.add(tr.g); pines.push(tr);
  });
  const falls=makeFalls({tint:0xbfe0ff,items:[
    {x:-58,y:26,z:-64,w:13,h:54},{x:-34,y:36,z:-66,w:8,h:44},{x:-8,y:30,z:-62,w:17,h:64},
    {x:22,y:40,z:-66,w:9,h:46},{x:48,y:28,z:-64,w:14,h:56},{x:74,y:34,z:-66,w:7,h:40}]});
  g.add(falls.g);
  const foam=makeGlow({n:540,box:[168,12,46],pos:[0,4,-62],color:0xe2f0fa,size:13,speed:1.0,rise:1,maxA:0.64});
  foam.points.renderOrder=4; g.add(foam.points);
  const spray=makeGlow({n:280,box:[176,24,42],pos:[0,11,-64],color:0xf0f8ff,size:8,speed:1.35,rise:1,maxA:0.48});
  spray.points.renderOrder=4; g.add(spray.points);
  const flood=makeFlow({n:760,box:[230,20,150],pos:[0,10,-52],color:0xba9668,size:24,speed:5.5,maxA:0.24});
  g.add(flood.points);
  const road=makePlankRoad({w:3.0,color:0x241a12,rimC:0xe8bc82,rim:0.44,
    pts:[[-20,-2,-42],[6,-1,-40],[32,0,-38]]});
  g.add(road.g);
  const man=makeFigure({pose:'独立',robe:0x1a1c24,hat:'幞头',scale:1.4,face:2.7,rim:0.62,rimC:0xe8c070});
  man.position.set(6,0,-42); g.add(man);
  const rocks=[];
  [[-42,1,-34,4.6],[-6,1.4,-30,6.2],[34,1.2,-34,5.0],[66,1.6,-32,3.8]].forEach(function(p,i){
    const r=makeForeground({kind:'坡石',n:1,r:p[3],w:0,d:0,color:0x0d0a07,seed:6613+i,rim:0.26,rimC:0xd9a05a});
    r.g.position.set(p[0],p[1],p[2]); g.add(r.g); rocks.push(r);
  });
  const fgL=makeForeground({kind:'岩壁',n:3,r:8.2,w:36,d:15,color:0x050403,seed:6621,rim:0.16,rimC:0xb88048});
  fgL.g.position.set(-54,-5,22); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:3,r:6.6,w:32,d:13,color:0x050403,seed:6627,rim:0.16,rimC:0xb88048});
  fgR.g.position.set(56,-5,16); g.add(fgR.g);
  const fgPine=makeTree({h:34,bend:3.0,branches:7,blen:0.50,dead:true,hang:true,color:0x1a130d,seed:6631,sway:0.6});
  fgPine.g.position.set(-22,48,10); g.add(fgPine);
  const sun=makeDisc({r:25,color:0xfff2d4,glowC:0xe8822a,glow:310});
  sun.g.position.set(-74,124,-300); g.add(sun.g);
  const mist=makeMist({n:12,spread:[300,44,160],pos:[0,38,-100],scale:92,color:0xa8805a,op:0.12});
  g.add(mist.g);
  addLights(g,{c:0xecc088,i:0.88,p:[-150,95,-165]},{c:0x48341e,i:0.74});
  const pl=new THREE.PointLight(0xdfefff,0.62,220); pl.position.set(0,18,-58); g.add(pl);
  const burst=makeBurst({n:180,color:0xeaf4ff,pos:[0,12,-62]}); g.add(burst.points);
  let power=0, reveal=0;
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    power=Math.max(0,power-dt*0.42);
    reveal=Math.max(0,reveal-dt*0.30);
    const rv=sstep(0,1.2,reveal+power);
    falls.update(t); foam.update(t); spray.update(t); flood.update(t); mist.update(t,k);
    for(const p of pines) p.update(t,k);
    man.update(t,k);
    for(const r of rocks) r.update(t,k);
    fgL.update(t,k); fgR.update(t,k); fgPine.update(t,k);
    road.g.update(t,k); burst.update(t);
    foam.mat.uniforms.uMaxA.value=k*(0.34+0.20*Math.sin(t*0.7)+0.24*power);
    spray.mat.uniforms.uMaxA.value=k*(0.28+0.14*Math.sin(t*1.1+1)+0.28*power);
    pl.intensity=k*(0.46+0.14*Math.sin(t*2.3)+0.55*power);
    /* 高标显形：从雾里长出来（本体提亮 + 山头抬高） */
    biao.mat.opacity=k*(0.30+0.70*rv);
    biao.g.scale.setScalar(0.90+0.10*rv);
    biao.g.position.y=-12+6*rv;
  },click(){
    if(power>0.6)return;
    power=1; reveal=1.2; burst.fire(); roar();
    const fl=$('#flash'); fl.textContent='万壑雷！'; fl.classList.remove('go');
    void fl.offsetWidth; fl.classList.add('go');
  }};
}
function bJiange(){ // 七 · 剑阁崔嵬 —— 一夫当关，万夫莫开；侧身西望长咨嗟
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0a0806,c2:0x281c12}); grd.mesh.position.y=-8; g.add(grd.mesh);
  const far=makeRange({r:300,h:120,layers:3,peaks:6,seed:7701,color:0x140f0a,atmo:0x6a4a2c,fogK:0.58,glowK:0.10,y:-24});
  g.add(far.g);
  const cL=makeCliffWall({n:3,h:126,w:54,seed:7703,color:0x3c2611,rimC:0xe8b878,rim:0.40,y:-18,zjit:12});
  cL.g.position.set(-58,-4,-72); cL.g.rotation.y=0.16; g.add(cL.g);
  const cR=makeCliffWall({n:3,h:120,w:52,seed:7707,color:0x3a2410,rimC:0xe8b878,rim:0.40,y:-18,zjit:12});
  cR.g.position.set(60,-4,-70); cR.g.rotation.y=-0.14; g.add(cR.g);
  const gate=makeGate({w:30,h:26,d:12,color:0x2e1e10});
  gate.g.position.set(2,-6,-64); g.add(gate.g);
  const biao=makeBiao({h:168,r:24,color:0x2a1c12,seed:7711,rim:0.42,rimC:0xf0c880,transparent:true});
  biao.g.position.set(96,-10,-210); g.add(biao.g);
  /* 万夫莫开：谷底列阵的人影与旗影（InstancedMesh 1 call + 旗各 1 call） */
  const crowd=makeCrowd({n:16,rect:[-46,-46,92,10],seed:7717,color:0x14161e,rimC:0xd98e3a,rim:0.30,sMin:0.9,sMax:1.15,y:-8});
  g.add(crowd.mesh);
  const banners=[];
  [[-34,-40,15],[6,-44,17],[40,-40,14]].forEach(function(p,i){
    const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.30,0.44,p[2],6),
      new THREE.MeshPhongMaterial({color:0x1c1409,shininess:6}));
    pole.position.set(p[0],-8+p[2]/2,p[1]); g.add(pole);
    const bn=makeBanner({w:6.2,h:3.4,color:0x7a2c16,ph:i*2.1});
    bn.mesh.position.set(p[0]+3.4,-8+p[2]-2.4,p[1]); g.add(bn.mesh);
    banners.push({b:bn});
  });
  /* 朝避猛虎，夕避长蛇：关前暗处的兽影 + 蛇身（磨牙吮血） */
  const beasts=[];
  const b1=makeBeast({scale:2.6,face:-0.5,ph:0.4}); b1.position.set(-30,-8,-34); b1.rotation.y=-0.6;
  g.add(b1); beasts.push(b1);
  const b2=makeBeast({scale:2.2,face:0.6,ph:2.1,color:0x120e0b}); b2.position.set(34,-8,-30); b2.rotation.y=2.5;
  g.add(b2); beasts.push(b2);
  const snake=makeSnake({len:40,r:0.55,ph:0.8});
  snake.g.position.set(6,-7.2,-26); snake.g.rotation.y=0.12; g.add(snake.g);
  /* 关楼火把 + 灯笼：森然里的暖点 */
  const flames=[];
  [[-13.4,12,-58.4],[15.4,12,-58.4]].forEach(function(p,i){
    const fl=makeFlame({h:3.4,w:1.5,planes:3,embers:26,spark:i===0,light:0.9,lightD:60,wide:0.36,seed:7719+i});
    fl.g.position.set(p[0],p[1],p[2]); g.add(fl.g); flames.push(fl);
  });
  const lans=[];
  [[-16.2,18.4,-58],[17.4,18.6,-58]].forEach(function(p,i){
    const l=makeLantern(0.62,{flame:i===0}); l.position.set(p[0],p[1],p[2]); g.add(l); lans.push(l);
  });
  /* 行人：侧身西望长咨嗟（关前崖台，背身而立） */
  const man=makeFigure({pose:'独立',robe:0x1c1e26,belt:0x7a5a34,hat:'幞头',beard:true,scale:1.9,face:2.4,
    rim:0.62,rimC:0xe8c070});
  man.position.set(-20,-6,-40); g.add(man);
  /* 锦城虽云乐：西望处远远的暖色灯火 */
  const city=makeGlow({n:150,box:[70,16,26],pos:[-96,16,-250],color:0xffc070,size:9,speed:0.05,rise:0,maxA:0.55});
  g.add(city.points);
  const cityGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
    transparent:true,opacity:0.42,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  cityGlow.scale.set(120,52,1); cityGlow.position.set(-96,20,-256); cityGlow.renderOrder=3; g.add(cityGlow);
  const mist=makeMist({n:11,spread:[280,34,150],pos:[0,16,-92],scale:84,color:0x8a6a4c,op:0.12});
  g.add(mist.g);
  const dust=makeFlow({n:600,box:[240,24,170],pos:[0,4,-50],color:0xa8825a,size:22,speed:2.4,maxA:0.22});
  g.add(dust.points);
  const fgL=makeForeground({kind:'岩壁',n:3,r:8.0,w:34,d:14,color:0x050403,seed:7723,rim:0.16,rimC:0xb88048});
  fgL.g.position.set(-50,-6,20); g.add(fgL.g);
  const fgR=makeForeground({kind:'岩壁',n:3,r:6.4,w:30,d:12,color:0x050403,seed:7727,rim:0.16,rimC:0xb88048});
  fgR.g.position.set(52,-6,16); g.add(fgR.g);
  addLights(g,{c:0xe0b070,i:0.52,p:[-120,80,-150]},{c:0x3a2a1c,i:0.60});
  const pl=new THREE.PointLight(0xffb066,0.75,80); pl.position.set(0,12,-56); g.add(pl);
  const burst=makeBurst({n:170,color:0xffd9a0,pos:[2,16,-62]}); g.add(burst.points);
  let power=0, reveal=0;
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    power=Math.max(0,power-dt*0.40);
    reveal=Math.max(0,reveal-dt*0.28);
    const rv=sstep(0,1.2,reveal+power);
    far.update(t,mouse.x*0.4); mist.update(t,k); dust.update(t); city.update(t);
    crowd.update(t); man.update(t,k); snake.update(t);
    for(const f2 of flames) f2.update(t,k);
    for(const l of lans) l.update(t,k);
    for(const b of banners) b.b.update(t);
    for(const b of beasts) b.update(t,k);
    fgL.update(t,k); fgR.update(t,k); burst.update(t);
    pl.intensity=k*(0.60+0.15*Math.sin(t*3.3)+0.60*power);
    cityGlow.material.opacity=k*0.42*(0.80+0.20*Math.sin(t*1.3));
    biao.mat.opacity=k*(0.26+0.74*rv);
    biao.g.scale.setScalar(0.90+0.10*rv);
  },click(){
    if(power>0.6)return;
    power=1; reveal=1.2; burst.fire(); roar();
    const fl=$('#flash'); fl.textContent='万夫莫开！'; fl.classList.remove('go');
    void fl.offsetWidth; fl.classList.add('go');
  }};
}
