/* ================= 画菊 · 三境场景（宣纸留白 · 疏篱秋菊变体：卷首篱菊、独立疏篱、抱香枝头）
   本诗专属系统「抱香不落」：北风可见（墨色流线横扫），菊丛随风剧烈摇动却始终扎根枝头不落；
   末境点击北风 → 风势暴涨、花瓣绕花盘旋而不离枝、题字「抱香枝头」。
   全页宣纸留白：纸底、淡墨远山、篱菊一点暖黄，不设水、不用金色辉光。 ================= */

/* —— 疏篱：稀疏的竹篱（几根斜立的篱桩 + 两道横杆），合批 1 mesh —— */
function makeFenceHJ(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, h=o.h===undefined?2.2:o.h, R=seedRnd(o.seed===undefined?23:o.seed);
  const wood=o.color===undefined?0x6a5a3e:o.color, B=new GeoBag();
  const np=o.posts===undefined?7:o.posts;
  for(let i=0;i<np;i++){
    const x=-w/2+w*i/(np-1), lean=(R()-0.5)*0.16;
    const p=new THREE.CylinderGeometry(0.075,0.095,h,6);
    p.rotateZ(lean); p.translate(x,h/2,0);
    B.put(p,shadeColor(wood,0.8+R()*0.5));
  }
  [0.42,0.86].forEach(function(f){
    const r=new THREE.BoxGeometry(w*1.02,0.085,0.10);
    r.rotateZ((R()-0.5)*0.03); r.translate(0,h*f,0.02);
    B.put(r,shadeColor(wood,1.15));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a6a58,emissive:0x14120c}),{c:o.rimC===undefined?0x8a8a78:o.rimC,i:0.20,p:2.2}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh};
}

/* —— 疏篱秋菊：一丛菊（茎 + 叶 + 花头：一圈花瓣 + 花心），合批 1 mesh，风起时整丛摇而不倒 —— */
function makeChrysanthemumHJ(o){
  o=o||{};
  const n=o.n===undefined?5:o.n, R=seedRnd(o.seed===undefined?13:o.seed);
  const h=o.h===undefined?1.75:o.h;
  const stemC=o.stem===undefined?0x4a5a34:o.stem, petalC=o.petal===undefined?0xd8b84a:o.petal;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*1.9, z=(R()-0.5)*1.7, hh=h*(0.7+R()*0.6);
    const lean=(R()-0.5)*0.35;
    const top=[x+lean*hh,hh,z];
    B.put(limbGeo([x,0,z],top,0.036,0.020,5),stemC);
    for(let k=0;k<3;k++){
      const t=0.34+0.24*k;
      const lf=new THREE.PlaneGeometry(0.54,0.22);
      lf.rotateZ((R()-0.5)*0.9); lf.rotateY(R()*6.283);
      lf.translate(x+lean*hh*t+(R()-0.5)*0.32, hh*t, z+(R()-0.5)*0.32);
      B.put(lf,shadeColor(0x5f7040,0.85+R()*0.4));
    }
    const pr=0.30+R()*0.16;
    const disc=new THREE.CylinderGeometry(pr*0.42,pr*0.42,0.05,12);
    disc.translate(top[0],top[1]+0.07,top[2]); B.put(disc,0xc8a63a);
    const np=Math.round(9+R()*5);
    for(let k=0;k<np;k++){
      const a=k/np*6.283;
      const pf=new THREE.PlaneGeometry(pr*1.18,pr*0.56);
      pf.rotateZ(a); pf.rotateX(-0.5+R()*0.9); pf.rotateY(R()*0.5);
      pf.translate(top[0]+Math.cos(a)*pr*0.74, top[1]+0.02-R()*0.12, top[2]+Math.sin(a)*pr*0.74);
      B.put(pf,shadeColor(petalC,0.8+R()*0.5));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x8a8a70,emissive:0x1a1808,side:THREE.DoubleSide}),{c:o.rimC===undefined?0x6a6a5a:o.rimC,i:0.20,p:2.2}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const ph=R()*6.283;
  g.update=function(t,k,gust){
    const kk=k===undefined?1:k, gu=gust===undefined?0:gust;
    g.rotation.z=(0.03+0.17*gu)*Math.sin(t*(1.5+2.6*gu)+ph)*kk;   /* 风越大摇得越狠，根却不动 */
    g.rotation.x=0.6*(0.02+0.09*gu)*Math.sin(t*(1.9+2.2*gu)+ph*1.6)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 北风：可见的墨色风线（Points 着色器，横向流线扫过画面；uGust 起风时加快变长） —— */
const HJ_WIND_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uW; uniform float uGust;
varying float vA;
void main(){
  vec3 p=position;
  float sp=1.7+aSeed*1.5;
  float x=mod(p.x+uW*0.5+uTime*sp*(1.0+1.5*uGust),uW)-uW*0.5;
  p.x=x;
  p.y+=sin(uTime*1.25+aSeed*31.0)*0.35;
  vA=(1.0-abs(x)/(uW*0.5))*(0.55+0.45*uGust);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(150.0/max(1.0,-mv.z)),42.0);
  gl_Position=projectionMatrix*mv;
}`;
const HJ_WIND_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.5,0.06,abs(q.x))*smoothstep(0.10,0.0,abs(q.y))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeWindHJ(o){
  o=o||{};
  const d=Object.assign({n:260,w:70,h:16,pos:[0,3,-4],size:26,maxA:0.26,c:0x3a4048},o);
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(d.n*3),S=new Float32Array(d.n),Z=new Float32Array(d.n);
  for(let i=0;i<d.n;i++){
    P[i*3]=d.pos[0]+(Math.random()-0.5)*d.w;
    P[i*3+1]=d.pos[1]+(Math.random()-0.5)*d.h;
    P[i*3+2]=d.pos[2]+(Math.random()-0.5)*22;
    S[i]=Math.random(); Z[i]=d.size*(0.55+Math.random()*0.9);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uW:{value:d.w},uGust:{value:0},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:HJ_WIND_VERT,fragmentShader:HJ_WIND_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  return {points,mat:m,update:function(t,gust){ m.uniforms.uTime.value=t; m.uniforms.uGust.value=gust===undefined?0:gust; }};
}

/* —— 绕花之瓣：风起时绕着花头盘旋却离不开枝头的菊瓣（Points，浅黄小瓣；uGust 越大转得越急） —— */
const HJ_SWIRL_VERT=`
attribute float aSeed; attribute float aR; attribute float aA; attribute float aSize;
uniform float uTime; uniform float uGust;
varying float vA;
void main(){
  vec3 p=position;
  float ang=aA+uTime*(0.7+2.4*uGust)*(0.6+aSeed*0.8);
  float r=aR*(1.0+0.22*uGust);
  p.x+=cos(ang)*r;
  p.z+=sin(ang)*r;
  p.y+=0.10*sin(uTime*1.6+aSeed*7.0)+0.22*uGust*sin(uTime*2.2+aSeed*3.0);
  vA=1.0;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(140.0/max(1.0,-mv.z)),16.0);
  gl_Position=projectionMatrix*mv;
}`;
function makeSwirlHJ(o){
  o=o||{};
  const d=Object.assign({n:120,centers:[[0,1.6,0]],r:1.1,size:3.6,maxA:0.75,c:0xe0c86a},o);
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(d.n*3),S=new Float32Array(d.n),Rr=new Float32Array(d.n),A=new Float32Array(d.n),Z=new Float32Array(d.n);
  for(let i=0;i<d.n;i++){
    const c=d.centers[i%d.centers.length];
    P[i*3]=c[0]; P[i*3+1]=c[1]; P[i*3+2]=c[2];
    S[i]=Math.random(); Rr[i]=d.r*(0.35+0.75*Math.random());
    A[i]=Math.random()*6.283; Z[i]=d.size*(0.6+Math.random()*0.8);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aR',new THREE.BufferAttribute(Rr,1));
  g.setAttribute('aA',new THREE.BufferAttribute(A,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uGust:{value:0},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:HJ_SWIRL_VERT,fragmentShader:`uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.5,0.12,length(q))*vA*uFade*uMaxA;
  if(a<0.005) discard;
  gl_FragColor=vec4(uC,a);
}`});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  return {points,mat:m,update:function(t,gust){ m.uniforms.uTime.value=t; m.uniforms.uGust.value=gust===undefined?0:gust; }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 篱菊秋光 —— 宣纸留白里疏篱一角、秋菊数丛、淡墨远山
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d0,c2:0xc6cbab,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:56,layers:3,peaks:6,seed:811,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.04,glow:0x9a9a88,y:-14});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  const ridge2=makeRange({r:190,h:26,layers:2,peaks:4,seed:812,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.66,glowK:0.03,glow:0x8a8a78,y:-6});
  ridge2.g.position.set(0,0,-58); g.add(ridge2.g);
  const fence=makeFenceHJ({w:20,h:2.3,seed:31}); fence.g.position.set(-3,-1.5,-10); g.add(fence.g);
  const clumps=[];
  [[-8,0,-8.4],[-3.5,0,-8.0],[1.5,0,-8.6],[7,0,-8.2]].forEach(function(p,i){
    const c=makeChrysanthemumHJ({n:6,seed:41+i*13,h:1.8}); c.g.position.set(p[0],-1.5,p[2]); g.add(c.g); clumps.push(c);
  });
  const poet=makeFigure({pose:'独立',robe:0x3a4048,belt:0x8a8a70,collar:0xe8e2d0,hat:'发髻',
    hair:0x2a2a2e,scale:1.16,rim:0.30,rimC:0x8a8a78,noProp:true});
  poet.position.set(10.5,-1.5,-7); poet.rotation.y=-2.3; g.add(poet);
  const ink=makeMist({n:7,spread:[220,26,120],pos:[0,10,-50],scale:76,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:180,box:[190,26,110],pos:[0,8,-26],color:0x7a7a70,size:9,speed:0.7,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:7,color:0xb8b2a0,seed:33,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-18,-1.6,36); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:30,n:8,d:6,color:0x3f3f38,seed:35,sway:0.5,rim:0.10,rimC:0x6a6a5a});
  fg2.g.position.set(20,-1.4,30); fg2.g.rotation.z=-0.16; g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-50,110,30]},{c:0xd8dac8,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); ink.update(t,k); dust.update(t);
    fence.mesh.rotation.y=0; for(let i=0;i<clumps.length;i++)clumps[i].update(t,k,0.12);
    poet.update(t,k);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bShuli(){ // 一 · 独立疏篱 —— 花开不并百花丛，独立疏篱趣未穷
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0xe8e2ce,c2:0xc3c9a8,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:62,layers:3,peaks:6,seed:821,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.04,glow:0x9a9a88,y:-15});
  ridge.g.position.set(0,0,-98); g.add(ridge.g);
  const ridge2=makeRange({r:180,h:28,layers:2,peaks:5,seed:822,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.66,glowK:0.03,glow:0x8a8a78,y:-6});
  ridge2.g.position.set(0,0,-62); g.add(ridge2.g);
  /* 疏篱横陈，菊丛独立篱边 */
  const fence=makeFenceHJ({w:26,h:2.4,seed:37}); fence.g.position.set(-2,-1.5,-4); fence.g.rotation.y=0.06; g.add(fence.g);
  const clumps=[];
  [[-9,0,-3.0],[-4.5,0,-2.4],[0.5,0,-3.2],[6,0,-2.6],[11,0,-3.0]].forEach(function(p,i){
    const c=makeChrysanthemumHJ({n:7,seed:51+i*17,h:1.85}); c.g.position.set(p[0],-1.5,p[2]); g.add(c.g); clumps.push(c);
  });
  const poet=makeFigure({pose:'独立',robe:0x3a4048,belt:0x8a8a70,collar:0xe8e2d0,hat:'发髻',
    hair:0x2a2a2e,scale:1.16,rim:0.30,rimC:0x8a8a78,noProp:true});
  poet.position.set(14.5,-1.5,-2.4); poet.rotation.y=-2.5; g.add(poet);
  const wind=makeWindHJ({n:200,w:64,h:14,pos:[0,3.4,-2],size:22,maxA:0.20});
  g.add(wind.points);
  const swirl=makeSwirlHJ({n:110,centers:[[-4.5,0.35,-2.4],[0.5,0.35,-3.2]],r:1.0,size:3.2,maxA:0.6});
  swirl.points.position.y=-1.5; g.add(swirl.points);
  const ink=makeMist({n:6,spread:[210,24,110],pos:[0,10,-46],scale:72,color:0x8a8578,op:0.09}); g.add(ink.g);
  const dust=makeFlow({n:160,box:[180,24,100],pos:[0,8,-22],color:0x7a7a70,size:9,speed:0.7,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.0,w:16,d:6,color:0xc0bAA8,seed:39,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-16,-1.5,16); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:8,d:5,color:0xb2ac9a,seed:41,sway:0.6,tip:0x5a5a4a});
  fg2.g.position.set(15,-1.4,14); g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-48,105,26]},{c:0xd8dac8,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); ridge2.update(t,0); ink.update(t,k); dust.update(t);
      const gust=0.16+0.10*Math.sin(t*0.4);
      wind.update(t,gust); swirl.update(t,gust);
      for(let i=0;i<clumps.length;i++)clumps[i].update(t,k,gust);
      poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(3,0.3,0.08); }};
}
function bBaoxiang(){ // 二（末境·可点击）· 抱香枝头 —— 宁可枝头抱香死，何曾吹落北风中
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,gust:0.18};
  const grd=makeGround({r:250,c1:0xe9e2cf,c2:0xc5cbaa,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:64,layers:3,peaks:6,seed:831,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.04,glow:0x9a9a88,y:-15});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  const ridge2=makeRange({r:175,h:28,layers:2,peaks:4,seed:832,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.66,glowK:0.03,glow:0x8a8a78,y:-6});
  ridge2.g.position.set(0,0,-66); g.add(ridge2.g);
  /* 近景：三丛菊（主角，镜头贴近「抱香枝头」） */
  const near=[];
  [[-3.4,0,-1.6],[-0.6,0,-0.9],[2.6,0,-2.2]].forEach(function(p,i){
    const c=makeChrysanthemumHJ({n:8,seed:61+i*19,h:2.0}); c.g.position.set(p[0],-1.5,p[2]); g.add(c.g); near.push(c);
  });
  const fence=makeFenceHJ({w:22,h:2.4,seed:43}); fence.g.position.set(0,-1.5,-6.2); g.add(fence.g);
  const wind=makeWindHJ({n:300,w:60,h:14,pos:[0,3.2,-1],size:26,maxA:0.26});
  g.add(wind.points);
  const swirl=makeSwirlHJ({n:170,centers:[[-3.4,0.45,-1.6],[-0.6,0.45,-0.9],[2.6,0.45,-2.2]],r:1.15,size:3.6,maxA:0.72});
  swirl.points.position.y=-1.5; g.add(swirl.points);
  const poet=makeFigure({pose:'独立',robe:0x3a4048,belt:0x8a8a70,collar:0xe8e2d0,hat:'发髻',
    hair:0x2a2a2e,scale:1.12,rim:0.28,rimC:0x8a8a78,noProp:true});
  poet.position.set(6.4,-1.5,-3.4); poet.rotation.y=-2.6; g.add(poet);
  const ink=makeMist({n:6,spread:[200,22,100],pos:[0,9,-44],scale:70,color:0x8a8578,op:0.09}); g.add(ink.g);
  const dust=makeFlow({n:150,box:[170,22,96],pos:[0,7,-20],color:0x7a7a70,size:9,speed:0.7,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:2.8,w:14,d:6,color:0xc4beac,seed:45,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(11,-1.5,9); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0xb4ae9c,seed:47,sway:0.55,tip:0x5a5a4a});
  fg2.g.position.set(-11,-1.4,8); g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-46,100,24]},{c:0xd8dac8,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.gust=Math.min(1.6,ctl.gust+dt/1.8);
      else ctl.gust=0.18+0.06*Math.sin(t*0.5);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const gu=ctl.gust+0.5*ctl.pulse;
      ridge.update(t,0); ridge2.update(t,0); ink.update(t,k); dust.update(t);
      wind.update(t,gu); swirl.update(t,gu);
      for(let i=0;i<near.length;i++)near[i].update(t,k,gu);
      poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.00,0.13); pluck(0,0.30,0.11); pluck(3,0.62,0.09);
        const fl=$('#flash'); fl.textContent='抱香枝头'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：风再紧一分，花仍不落 */
    },clicked:false};
  return api;
}
