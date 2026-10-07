/* ================= 谒金门·风乍起 · 三境场景（青绿春晓 · 春池杏影变体：卷首春池、吹皱春水、倚阑望君）
   本诗专属系统「一池春皱」：风乍起 → 池面涟漪层层皱开（着色器细纹 + 四道可见水环）；
   末境点击池水 → 涟漪再起 + 喜鹊振翅报喜（「举头闻鹊喜」）。
   与同赛道的《浣溪沙·游蕲水清泉寺》（溪山/兰芽/细雨）不同：本页是春日园池——鸳鸯、红杏、
   斗鸭阑干、碧玉搔头、喜鹊，粒子母题是飘落杏花瓣而非雨丝。 ================= */

/* —— 飘落杏花瓣（InstancedMesh，1 draw call；扁圆椭球读作花瓣，缓落 + 自转 + 随风横飘） —— */
function makePetalsYJ(o){
  o=o||{};
  const n=o.n===undefined?84:o.n, R=seedRnd(o.seed===undefined?217:o.seed);
  const geo=new THREE.SphereGeometry(0.085,7,5); geo.scale(1.8,0.30,1.0);
  const mat=new THREE.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:0.62,
    depthWrite:false,side:THREE.DoubleSide});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  const cA=C(0xf7dbe2), cB=C(0xf2c94c), cC=C(0xe4efd4);
  for(let i=0;i<n;i++){
    items.push({x:(R()-0.5)*(o.w===undefined?56:o.w), y:R()*(o.h===undefined?18:o.h),
      z:(R()-0.5)*(o.d===undefined?36:o.d), s:0.7+R()*0.9, ph:R()*6.283,
      sp:0.55+R()*0.8, sw:0.4+R()*1.0, spin:0.35+R()*0.8});
    const c=R()<0.60?cA:(R()<0.55?cB:cC);
    mesh.setColorAt(i,c);
  }
  if(mesh.instanceColor)mesh.instanceColor.needsUpdate=true;
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x, 0, o.z===undefined?-8:o.z);
  const H=o.h===undefined?18:o.h, fall=o.fall===undefined?1.3:o.fall;
  g.update=function(t,gust){
    const gu=gust===undefined?0:gust;
    for(let i=0;i<n;i++){
      const it=items[i];
      const y=((it.y-t*fall*it.sp*(1+1.4*gu))%H+H)%H;
      dm.position.set(it.x+Math.sin(t*0.5+it.ph)*it.sw*(1+2.6*gu)+gu*2.2*Math.sin(it.ph*3.1),
        0.25+y, it.z+Math.cos(t*0.42+it.ph)*it.sw*0.6);
      dm.rotation.set(t*it.spin*0.7+it.ph, it.ph+t*0.6+gu*3.0, Math.sin(t*0.8+it.ph)*0.9);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  };
  return {g,update:g.update,mesh,mat};
}

/* —— 涟漪：水面「层层皱开」的皱纹（着色器细纹 + 四道水环） ——
   风乍起时 uK 涨；末境点击时 uK 再涨一拍。水环是可见几何，截图里读得出来。 */
const YJ_RIPPLE_VERT=`
varying vec2 vW;
void main(){
  vec4 wp=modelMatrix*vec4(position,1.0);
  vW=wp.xz;
  gl_Position=projectionMatrix*viewMatrix*wp;
}`;
const YJ_RIPPLE_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; uniform float uMaxR;
uniform vec3 uC; uniform vec3 uC2; uniform vec2 uOrigin;
varying vec2 vW;
void main(){
  float d=length(vW-uOrigin);
  float a=0.0;
  a+=0.130*(0.5+0.5*sin(d*7.2-uTime*2.1))*exp(-d*0.06);
  for(int i=0;i<4;i++){
    float ph=fract(uTime*0.15+float(i)*0.25);
    float r=ph*uMaxR;
    float w=1.0+ph*3.0;
    a+=smoothstep(w,0.0,abs(d-r))*(1.0-ph)*(1.0-ph)*1.15;
  }
  a*=uK*uFade;
  if(a<0.004) discard;
  gl_FragColor=vec4(mix(uC,uC2,clamp(a*0.8,0.0,1.0)),clamp(a,0.0,0.85));
}`;
function makeRippleYJ(o){
  o=o||{};
  const size=o.size===undefined?46:o.size;
  const geo=new THREE.PlaneGeometry(size,size,1,1); geo.rotateX(-Math.PI/2);
  const ox=o.ox===undefined?0:o.ox, oz=o.oz===undefined?-12:o.oz;
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,fog:false,
    blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:0},uK:{value:o.k===undefined?0.55:o.k},
      uMaxR:{value:o.maxR===undefined?14:o.maxR},uC:{value:C(0xa6d69c)},
      uC2:{value:C(0xeaf6e2)},uOrigin:{value:new THREE.Vector2(ox,oz)}},
    vertexShader:YJ_RIPPLE_VERT,fragmentShader:YJ_RIPPLE_FRAG});
  const mesh=new THREE.Mesh(geo,mat); mesh.renderOrder=2;
  mesh.position.set(0,o.y===undefined?0.07:o.y,0);
  const g=new THREE.Group(); g.add(mesh);
  const rings=[], base=0.88;   /* 基座 = 运行期最大值：风起时水环最亮 0.88 */
  for(let i=0;i<4;i++){
    const rg=new THREE.RingGeometry(0.90,1.0,72); rg.rotateX(-Math.PI/2);
    const rm=new THREE.MeshBasicMaterial({color:0xeeffd8,transparent:true,opacity:base,
      depthWrite:false,blending:THREE.AdditiveBlending,side:THREE.DoubleSide,fog:false});
    const rmesh=new THREE.Mesh(rg,rm); rmesh.renderOrder=2;
    rmesh.position.set(ox,0.075+i*0.012,oz);
    g.add(rmesh); rings.push({mesh:rmesh,mat:rm,ph:i/4});
  }
  return {g,mat,update:function(t,k,strength){
    const s=strength===undefined?1:strength;
    mat.uniforms.uTime.value=t;
    mat.uniforms.uK.value=(o.k===undefined?0.55:o.k)*s;
    for(let i=0;i<rings.length;i++){
      const r=rings[i], ph=(t*0.15+r.ph)%1, rad=1.15+ph*(o.maxR===undefined?14:o.maxR);
      r.mesh.scale.set(rad,1,rad);
      r.mat.opacity=k*base*(1-ph)*(1-ph)*Math.min(1,s);  /* 每帧写 opacity 必乘 fadeK；系数≤1，故 ≤ base×fadeK */
    }
  }};
}

/* —— 鸳鸯：一对（闲引鸳鸯）—— 橙褐身、绿紫帆羽、朱喙、白眉纹，合批 1+1 mesh —— */
function makeYuanyangYJ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, R=seedRnd(o.seed===undefined?13:o.seed);
  const bodyC=o.body===undefined?0xb06a2e:o.body, wingC=o.wing===undefined?0x2f5f46:o.wing;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.34,10,8); body.scale(1.7,0.95,1.0); body.translate(0,0.30,0);
  B.put(body,bodyC);
  const tail=new THREE.ConeGeometry(0.20,0.52,7); tail.rotateZ(Math.PI/2.1); tail.translate(-0.62,0.42,0);
  B.put(tail,shadeColor(bodyC,0.85));
  const wing=new THREE.SphereGeometry(0.27,9,7); wing.scale(1.25,0.52,0.92); wing.translate(-0.06,0.46,0.12);
  B.put(wing,wingC);
  const sail=new THREE.PlaneGeometry(0.30,0.34); sail.translate(-0.10,0.74,0.20);
  B.put(sail,shadeColor(0xe0903a,0.9+R()*0.3));
  const cheek=new THREE.SphereGeometry(0.155,8,7); cheek.scale(1.0,0.92,0.92); cheek.translate(0.44,0.52,0.10);
  B.put(cheek,0xf2ece0);
  const head=new THREE.SphereGeometry(0.205,9,7); head.translate(0.52,0.56,0.0); B.put(head,shadeColor(wingC,1.15));
  const crest=new THREE.SphereGeometry(0.115,7,6); crest.scale(1.0,0.72,1.0); crest.translate(0.42,0.72,0.0);
  B.put(crest,0x9a5f2c);
  const beak=new THREE.ConeGeometry(0.075,0.26,6); beak.rotateZ(-Math.PI/2); beak.translate(0.76,0.53,0.0);
  B.put(beak,0xc0452e);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x5a6a4a,emissive:0x120a06,side:THREE.DoubleSide}),
    {c:o.rimC===undefined?0xf0d0a0:o.rimC,i:o.rim===undefined?0.42:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const ph=R()*6.283;
  g.update=function(t,k){
    g.position.y=(o.y===undefined?0.02:o.y)+0.055*Math.sin(t*1.5+ph);
    g.rotation.z=0.045*Math.sin(t*1.2+ph*1.4);
    g.rotation.y=(o.ry===undefined?0:o.ry)+0.12*Math.sin(t*0.32+ph);
  };
  return {g,update:g.update,mesh};
}

/* —— 红杏：临水杏树，枝条 + 粉白花团（全页唯一的暖色/粉色点，读作「红杏枝头」） —— */
function makeApricotYJ(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, R=seedRnd(o.seed===undefined?29:o.seed);
  const wood=o.wood===undefined?0x2b2118:o.wood, B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.5-0.25,h*0.50,0],h*0.05,h*0.024,7),wood);
  const tips=[];
  const nb=o.branches===undefined?5:o.branches;
  for(let i=0;i<nb;i++){
    const a=(i/nb)*6.283+R()*0.7, len=h*(0.34+0.22*R());
    const p1=[Math.sin(a)*len*0.60, h*0.50+len*0.44, Math.cos(a)*len*0.60];
    B.put(limbGeo([0,h*0.48,0],p1,h*0.019,h*0.009,6),shadeColor(wood,1.2));
    tips.push(p1);
    if(R()<0.85){
      const p2=[p1[0]+Math.sin(a+0.55)*len*0.42, p1[1]+len*0.34, p1[2]+Math.cos(a+0.55)*len*0.42];
      B.put(limbGeo(p1,p2,h*0.011,h*0.005,5),shadeColor(wood,1.35));
      tips.push(p2);
      if(R()<0.5){
        const p3=[p2[0]+Math.sin(a-0.5)*len*0.30, p2[1]+len*0.24, p2[2]+Math.cos(a-0.5)*len*0.30];
        B.put(limbGeo(p2,p3,h*0.007,h*0.003,5),shadeColor(wood,1.45));
        tips.push(p3);
      }
    }
  }
  const nm=o.clusters===undefined?8:o.clusters;
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<nm;k++){
      const rad=h*0.036*(0.7+R()*0.9);
      const b=new THREE.SphereGeometry(rad,6,5);
      b.translate(tp[0]+(R()-0.5)*h*0.17, tp[1]+(R()-0.35)*h*0.13, tp[2]+(R()-0.5)*h*0.17);
      B.put(b, R()<0.70?shadeColor(0xf7dbe2,0.84+R()*0.34):(R()<0.5?0xf2c94c:0xfaeaf0));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:9,
    specular:0x4a4a3a,emissive:0x1c0e12,side:THREE.DoubleSide}),
    {c:o.rimC===undefined?0xf0c8b0:o.rimC,i:o.rim===undefined?0.30:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.012*Math.sin(t*0.42+o.seed)*kk+0.012*Math.sin(t*0.42+o.seed);
  };
  return {g,update:g.update,mesh};
}

/* —— 斗鸭阑干：雕有斗鸭纹样的栏杆（柱头一只只小鸭），合批 1 mesh —— */
function makeDuckRailingYJ(o){
  o=o||{};
  const w=o.w===undefined?26:o.w, h=o.h===undefined?3.2:o.h;
  const col=o.color===undefined?0x2a2622:o.color, B=new GeoBag();
  const r0=new THREE.BoxGeometry(w,0.20,0.26); r0.translate(0,h,0); B.put(r0,shadeColor(col,1.6));
  const r1=new THREE.BoxGeometry(w,0.13,0.18); r1.translate(0,h*0.60,0); B.put(r1,shadeColor(col,1.25));
  const r2=new THREE.BoxGeometry(w,0.11,0.16); r2.translate(0,h*0.22,0); B.put(r2,shadeColor(col,1.05));
  const np=o.posts===undefined?7:o.posts;
  for(let i=0;i<=np;i++){
    const x=-w/2+w*i/np;
    const p=new THREE.BoxGeometry(0.22,h,0.22); p.translate(x,h/2,0); B.put(p,col);
    const d=new THREE.SphereGeometry(0.17,7,6); d.scale(1.55,0.88,0.92); d.translate(x+0.03,h+0.20,0);
    B.put(d,shadeColor(col,1.75));
    const hd=new THREE.SphereGeometry(0.095,6,5); hd.translate(x+0.26,h+0.34,0);
    B.put(hd,shadeColor(col,1.95));
    const bk=new THREE.ConeGeometry(0.045,0.13,5); bk.rotateZ(-Math.PI/2); bk.translate(x+0.36,h+0.33,0);
    B.put(bk,0xb98a4a);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4a34,emissive:0x070604}),
    {c:o.rimC===undefined?0xbfd8a0:o.rimC,i:o.rim===undefined?0.30:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh};
}

/* —— 碧玉搔头：一支斜坠的碧玉簪（簪身 + 玉首 + 一点玉光） —— */
function makeJadePinYJ(o){
  o=o||{};
  const jade=o.color===undefined?0x7fd6b0:o.color, B=new GeoBag();
  const shaft=new THREE.CylinderGeometry(0.045,0.058,1.5,8); B.put(shaft,jade);
  const head=new THREE.SphereGeometry(0.155,10,8); head.scale(1.0,0.84,1.0); head.translate(0,0.82,0);
  B.put(head,shadeColor(jade,1.3));
  const bead=new THREE.SphereGeometry(0.068,7,6); bead.translate(0,1.02,0); B.put(bead,0xd0f4de);
  const tail=new THREE.SphereGeometry(0.05,7,6); tail.translate(0,-0.78,0); B.put(tail,shadeColor(jade,0.8));
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:70,
    specular:0xc8f2dd,emissive:0x0d2a20}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8f0cc,transparent:true,
    opacity:0.42,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  gl.scale.set(1.6,1.6,1); gl.position.y=0.82; gl.renderOrder=3; g.add(gl);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    gl.material.opacity=kk*0.42*(0.55+0.45*Math.sin(t*2.1));  /* 基座 0.42 = 运行期最大值 */
  };
  return {g,update:g.update,mesh,glow:gl};
}

/* —— 喜鹊：黑白长尾的鹊（举头闻鹊喜）—— 点击后振翅上飞 —— */
function makeMagpieYJ(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,9,7); body.scale(1.55,0.98,0.92); body.translate(0,0.34,0);
  B.put(body,0x1c1e26);
  const belly=new THREE.SphereGeometry(0.225,8,6); belly.scale(1.25,0.82,0.82); belly.translate(0.06,0.26,0.07);
  B.put(belly,0xeef0f2);
  const wing=new THREE.SphereGeometry(0.21,8,6); wing.scale(1.35,0.40,0.85); wing.translate(-0.05,0.50,0.14);
  B.put(wing,0x2b3040);
  const head=new THREE.SphereGeometry(0.185,8,7); head.translate(0.47,0.58,0); B.put(head,0x1c1e26);
  const cheek=new THREE.SphereGeometry(0.095,7,6); cheek.translate(0.56,0.55,0.10); B.put(cheek,0xeef0f2);
  const beak=new THREE.ConeGeometry(0.055,0.24,6); beak.rotateZ(-Math.PI/2); beak.translate(0.68,0.56,0);
  B.put(beak,0x2a2a2e);
  const tail=new THREE.BoxGeometry(0.66,0.10,0.17); tail.rotateZ(0.40); tail.translate(-0.56,0.38,0);
  B.put(tail,0x23262e);
  const t2=new THREE.BoxGeometry(0.54,0.07,0.13); t2.rotateZ(0.62); t2.translate(-0.50,0.30,0.02);
  B.put(t2,0x2f3440);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:18,
    specular:0x6a7488,emissive:0x080a10}),
    {c:o.rimC===undefined?0xcfe4ff:o.rimC,i:o.rim===undefined?0.45:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  const y0=o.y===undefined?0:o.y;
  g.update=function(t,k,fly){
    const f=fly===undefined?0:fly;
    g.position.y=y0+f*2.4;
    g.rotation.z=0.06*Math.sin(t*1.1)+0.42*f*Math.sin(t*13.0);
    g.rotation.y=(o.ry===undefined?0:o.ry)+f*0.35*Math.sin(t*4.0);
  };
  return {g,update:g.update,mesh};
}

/* —— 春池：一池春水的池体 + 一圈池岸石（水池与岸同组，避免「水浮在空中」） —— */
function makePondYJ(o){
  o=o||{};
  const rx=o.rx===undefined?20:o.rx, rz=o.rz===undefined?15:o.rz, y=o.y===undefined?0:o.y;
  const R=seedRnd(o.seed===undefined?77:o.seed), B=new GeoBag();
  const n=o.n===undefined?22:o.n;
  for(let i=0;i<n;i++){
    const a=i/n*6.283+(R()-0.5)*0.14;
    const rg=rockGeo(1.25+R()*1.7,1,R);
    rg.translate(Math.sin(a)*rx*(1+(R()-0.5)*0.07), y+(R()-0.45)*0.5, Math.cos(a)*rz*(1+(R()-0.5)*0.07));
    B.put(rg,shadeColor(o.color===undefined?0x17251b:o.color,0.55+R()*0.75));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x233428,emissive:0x040a06}),
    {c:o.rimC===undefined?0x9fc48f:o.rimC,i:o.rim===undefined?0.16:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x, 0, o.z===undefined?0:o.z);
  return {g};
}

/* —— 香径：落花飘香的池边小路（路 + 散落花瓣，合批 1 mesh） —— */
function makeFragrantPathYJ(o){
  o=o||{};
  const len=o.len===undefined?30:o.len, R=seedRnd(o.seed===undefined?53:o.seed), B=new GeoBag();
  const road=new THREE.BoxGeometry(len,0.09,o.w===undefined?3.4:o.w);
  road.rotateZ(o.tilt===undefined?0.02:o.tilt); B.put(road,o.color===undefined?0x6e6a52:o.color);
  for(let i=0;i<46;i++){
    const p=new THREE.SphereGeometry(0.075,6,5); p.scale(1.6,0.32,1.0);
    p.translate((R()-0.5)*len*1.1, 0.10+R()*0.03, (R()-0.5)*(o.w===undefined?3.4:o.w)*1.5);
    p.rotateX(R()*0.6);
    B.put(p, R()<0.6?shadeColor(0xf2c8d4,0.8+R()*0.4):0xe8dcc0);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a3a30,emissive:0x0c0c08,side:THREE.DoubleSide}),
    {c:0xcfe0b0,i:0.18,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x, o.y===undefined?0.02:o.y, o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 春池杏影 —— 晨光里一池春水，杏花临岸，亭柱两三
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0c1710,c2:0x16281a,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:3,peaks:5,seed:137,color:0x0c1911,atmo:0x2f4a34,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-88); g.add(ridge.g);
  const water=makeWater({size:44,seg:32,amp:0.11,freq:0.15,speed:0.5,flow:[0.18,0.45],spec:1.2,
    deep:0x0b2018,shallow:0x2c6446,skyc:0x377053,moonDir:[70,90,-170],y:-1.1});
  water.mesh.scale.set(0.58,1,0.50);          /* 水面收在池岸圈之内：岸是岸、水是水，人不站在水里 */
  water.mesh.position.set(0,-1.1,-18); g.add(water.mesh);
  const pond=makePondYJ({rx:21,rz:15,y:-1.0,z:-18,seed:139}); g.add(pond.g);
  const a1=makeApricotYJ({h:8,seed:31,scale:1.15}); a1.g.position.set(-13,-1.4,-6); g.add(a1.g);
  const a2=makeApricotYJ({h:6.4,seed:37,scale:1.0}); a2.g.position.set(11,-1.4,-2); g.add(a2.g);
  const a3=makeApricotYJ({h:7,seed:41,scale:1.05}); a3.g.position.set(20,-1.4,-24); g.add(a3.g);
  const p1=makePillar({h:9,r:0.36,color:0x2a241c,top:false}); p1.g.position.set(-6,-1.5,-34); g.add(p1.g);
  const p2=makePillar({h:9,r:0.36,color:0x2a241c,top:false}); p2.g.position.set(5,-1.5,-34); g.add(p2.g);
  const crowd=makeCrowd({n:4,rect:[-4,-40,22,8],seed:67,color:0x131e14,rimC:0x9fc48f,rim:0.2});
  g.add(crowd.mesh);
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.15,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,60,1); dawn.position.set(-62,26,-120); dawn.renderOrder=-7; g.add(dawn);
  const petals=makePetalsYJ({n:70,w:120,h:24,d:90,z:-30,fall:1.1,seed:221}); g.add(petals.g);
  const motes=makeGlow({n:44,box:[190,30,110],pos:[0,9,-26],color:0xcfe0a8,size:7,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[250,34,140],pos:[0,11,-56],scale:80,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:50,n:9,d:7,color:0x081009,seed:19,sway:0.7,rim:0.14,rimC:0x9fc48f});
  brL.g.position.set(-26,-1.4,46); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const brR=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:21,rim:0.14,rimC:0x9fc48f});
  brR.g.position.set(17,-1.3,18); g.add(brR.g);
  addLights(g,{c:0xe8d8a8,i:0.46,p:[-50,80,30]},{c:0x22301f,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    petals.update(t,0); brL.update(t,k); brR.update(t,k); crowd.update(t);
    dawn.material.opacity=k*(0.11+0.028*Math.sin(t*0.4));
  }};
}
function bChunshui(){ // 一 · 吹皱春水 —— 风乍起，吹皱一池春水。闲引鸳鸯香径里，手挼红杏蕊
  const g=new THREE.Group();
  const ctl={t:0,gust:1,next:9};
  const grd=makeGround({r:230,c1:0x0b130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:38,layers:3,peaks:5,seed:151,color:0x09150e,atmo:0x29412e,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-7});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 一池春水（画面中心；涟漪即在此皱开） */
  const water=makeWater({size:46,seg:38,amp:0.135,freq:0.17,speed:0.5,flow:[0.2,0.5],spec:1.3,
    deep:0x0b2018,shallow:0x2f6a4c,skyc:0x3a7258,moonDir:[60,90,-160],y:0});
  water.mesh.scale.set(0.58,1,0.44);          /* 水面收在池岸圈之内 */
  water.mesh.position.set(0,0,-13); g.add(water.mesh);
  const pond=makePondYJ({rx:20,rz:14.5,y:0.05,z:-13,seed:157}); g.add(pond.g);
  /* 标志性瞬间：风乍起 → 涟漪层层皱开（涟漪只铺在水面范围内） */
  const ripple=makeRippleYJ({size:22,ox:0,oz:-13,maxR:9.5,k:0.80,y:0.075,seed:317}); g.add(ripple.g);
  /* 闲引鸳鸯：一对鸳鸯在水面缓游（近岸、放大，让「鸳鸯」读得出来） */
  const d1=makeYuanyangYJ({scale:1.5,seed:13,y:0.06,ry:0.5}); d1.g.position.set(-3.6,0.06,-4.8); g.add(d1.g);
  const d2=makeYuanyangYJ({scale:1.3,seed:17,y:0.06,ry:0.9}); d2.g.position.set(-1.1,0.06,-7.6); g.add(d2.g);
  /* 香径与临水杏树（手挼红杏蕊） */
  const path=makeFragrantPathYJ({len:32,w:4.2,x:1.5,z:3.2,ry:0.06,seed:53});
  g.add(path.g);
  const a1=makeApricotYJ({h:7.6,seed:61,scale:1.12}); a1.g.position.set(-9.6,0,2.6); g.add(a1.g);
  const a2=makeApricotYJ({h:6.6,seed:67,scale:1.0}); a2.g.position.set(8.6,0,2.0); g.add(a2.g);
  const a3=makeApricotYJ({h:5.8,seed:71,scale:0.9}); a3.g.position.set(15.5,0,-4.5); g.add(a3.g);
  /* 思妇：杏下香径，随手挼弄红杏之态 */
  const woman=makeFigure({pose:'独立',robe:0x46694f,belt:0xd8a7b1,collar:0xf0e4c8,hat:'发髻',
    hair:0x16181f,scale:1.14,rim:0.52,rimC:0xcae8a8,noProp:true});
  woman.position.set(-5.2,0,3.8); woman.rotation.y=2.45; g.add(woman);
  /* 花瓣（青绿春晓母题：粉白花瓣缓落，风起时横飘） */
  const petals=makePetalsYJ({n:84,w:60,h:18,d:40,z:-4,fall:1.25,seed:223}); g.add(petals.g);
  const motes=makeGlow({n:36,box:[130,22,80],pos:[0,8,-16],color:0xd6e6ae,size:6,speed:0.04,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,26,120],pos:[0,9,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const crowd=makeCrowd({n:3,rect:[6,-44,18,8],seed:77,color:0x121c13,rimC:0x9fc48f,rim:0.2});
  g.add(crowd.mesh);
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:43,sway:1.1,tip:0x2c4028});
  reed.g.position.set(15,-1.0,16); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x060c08,seed:47,rim:0.14,rimC:0x9fc48f});
  rk.g.position.set(-12,-1.1,20); g.add(rk.g);
  addLights(g,{c:0xd8d0a0,i:0.46,p:[-40,80,20]},{c:0x1c2a1e,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.t>ctl.next){ ctl.gust=1; ctl.next=ctl.t+11; }
      ctl.gust=Math.max(0,ctl.gust-dt/3.6);
      const strength=0.45+0.95*ctl.gust;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      ripple.update(t,k,strength);
      petals.update(t,ctl.gust);
      d1.update(t,k); d2.update(t,k); woman.update(t,k); crowd.update(t);
      a1.g.rotation.z=0.016*Math.sin(t*0.4)*ctl.gust;
      a2.g.rotation.z=0.014*Math.sin(t*0.37+2.0)*ctl.gust;
      reed.update(t,k); rk.update(t,k);
    },onEnter(){   // 风乍起：涟漪起势的一声
      ctl.gust=1; ctl.next=ctl.t+11;
      pluck(4,0.15,0.10); pluck(3,0.60,0.08);
    }};
}
function bYilan(){ // 二（末境·可点击）· 倚阑望君 —— 斗鸭阑干独倚，碧玉搔头斜坠。终日望君君不至，举头闻鹊喜
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,fly:0,gust:0.4,next:10};
  const grd=makeGround({r:230,c1:0x0b130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:36,layers:2,peaks:4,seed:181,color:0x091409,atmo:0x27402c,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  /* 栏外的池水 —— 点击处（涟漪层层皱开） */
  const water=makeWater({size:48,seg:36,amp:0.12,freq:0.16,speed:0.5,flow:[0.16,0.5],spec:1.3,
    deep:0x0b2018,shallow:0x2f6a4c,skyc:0x3a7258,moonDir:[55,90,-150],y:0});
  water.mesh.scale.set(0.57,1,0.44);          /* 水面收在池岸圈之内 */
  water.mesh.position.set(0,0,-13); g.add(water.mesh);
  const ripple=makeRippleYJ({size:22,ox:0,oz:-13,maxR:9.5,k:0.75,y:0.075,seed:331}); g.add(ripple.g);
  const pond=makePondYJ({rx:21,rz:15,y:0.05,z:-13,seed:191}); g.add(pond.g);
  /* 斗鸭阑干：横在近前，她独倚于此（压低栏杆，让栏外的池水看得见） */
  const rail=makeDuckRailingYJ({w:30,h:2.7,color:0x2a2622}); rail.g.position.set(0,0,6.2); g.add(rail.g);
  /* 思妇：倚栏背立，望君不至 */
  const woman=makeFigure({pose:'独立',robe:0x46694f,belt:0xd8a7b1,collar:0xf0e4c8,hat:'发髻',
    hair:0x16181f,scale:1.14,rim:0.52,rimC:0xcae8a8,noProp:true});
  woman.position.set(-1.3,0.0,7.0); woman.rotation.y=Math.PI; g.add(woman);
  /* 碧玉搔头斜坠：簪子斜斜插在发髻上、正往下滑（贴着她的头，不是横在胸前） */
  const pin=makeJadePinYJ({scale:0.80}); pin.g.position.set(-0.62,4.28,6.90);
  pin.g.rotation.set(-0.22,0.30,0.62); g.add(pin.g);
  /* 喜鹊：独立枝头、剪影在天（点击后振翅上飞，举头闻鹊喜） */
  const magpie=makeMagpieYJ({scale:1.7,y:6.9,ry:0.7,rimC:0xcfe4ff}); magpie.g.position.set(-5.4,6.9,1.0);
  g.add(magpie.g);
  const a1=makeApricotYJ({h:8,seed:199,scale:1.15}); a1.g.position.set(-10.5,0,-1.5); g.add(a1.g);
  const a2=makeApricotYJ({h:6.6,seed:211,scale:0.95}); a2.g.position.set(13,0,-5.5); g.add(a2.g);
  const p1=makePillar({h:8.6,r:0.34,color:0x2a241c,top:false}); p1.g.position.set(6.5,0,-11); g.add(p1.g);
  const petals=makePetalsYJ({n:72,w:62,h:18,d:44,z:-6,fall:1.15,seed:227}); g.add(petals.g);
  const motes=makeGlow({n:34,box:[130,22,80],pos:[0,8,-14],color:0xd6e6ae,size:6,speed:0.04,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,26,120],pos:[0,9,-52],scale:76,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const crowd=makeCrowd({n:2,rect:[-16,-40,10,6],seed:97,color:0x121c13,rimC:0x9fc48f,rim:0.2});
  g.add(crowd.mesh);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:14,d:6,color:0x060b07,seed:91,rim:0.14,rimC:0x9fc48f});
  rk.g.position.set(11,-1.1,14); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:93,sway:1.2,tip:0x2c4028});
  reed.g.position.set(-13,-1.0,15); g.add(reed.g);
  addLights(g,{c:0xd6cc9c,i:0.44,p:[-45,75,25]},{c:0x1e2c20,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.t>ctl.next){ ctl.gust=1; ctl.next=ctl.t+12; }
      ctl.gust=Math.max(0,ctl.gust-dt/4.0);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      if(ctl.clicked)ctl.fly=Math.min(1,ctl.fly+dt/0.9);
      const strength=0.40+0.7*ctl.gust+0.85*ctl.pulse;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      ripple.update(t,k,strength);
      petals.update(t,ctl.gust);
      woman.update(t,k); crowd.update(t); a1.update(t,k); a2.update(t,k);
      magpie.update(t,k,ctl.fly);
      pin.update(t,k);
      reed.update(t,k); rk.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        ctl.fly=0;
        pluck(5,0.00,0.16); pluck(4,0.16,0.13); pluck(5,0.34,0.11); pluck(3,0.56,0.09);
        const fl=$('#flash'); fl.textContent='举头闻鹊喜'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 // 可反复点：涟漪再层层皱开
    },clicked:false};
  return api;
}
