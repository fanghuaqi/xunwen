/* ================= 清平乐·春归何处 · 两境场景（青绿春晓·山谷寻春变体：春山无路、问取黄鹂）
   本诗专属系统「问路问鸟」：境①小径没入乱石草莽（寂寞无行路），春随流水落花而去；
   末境溪畔蔷薇架畔问取枝头黄鹂——点击：黄鹂百啭（引颈后仰+滑音啼啭），
   因风飞过蔷薇架（弧线飞越，风卷蔷薇瓣漫架而过），随后绕枝归栖、可再问 ================= */

/* —— 蔷薇落瓣：粉白花瓣（Points 自定义着色器：点内画旋转带缺刻小瓣，缓落+风向可控 → 「因风」的主角） —— */
const QP_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB;
uniform float uW; uniform float uX0; uniform float uSway; uniform float uDrift;
varying float vA; varying float vSeed;
void main(){
  vec3 p=position;
  float sp=uFall*(0.55+aSeed*0.75);
  float y=mod(p.y-uB-uTime*sp,uH);
  p.y=uB+y;
  p.x+=sin(uTime*0.7+aSeed*47.0)*uSway;
  p.x=uX0+mod(p.x-uX0+uDrift*uTime*(0.5+aSeed),uW)-uW*0.5;
  p.z+=cos(uTime*0.5+aSeed*31.0)*uSway*0.6;
  vA=smoothstep(0.0,uH*0.05,y)*(1.0-smoothstep(uH*0.9,uH,y));
  vSeed=aSeed;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(150.0/max(1.0,-mv.z)),20.0);
  gl_Position=projectionMatrix*mv;
}`;
const QP_PETAL_FRAG=`
uniform vec3 uC; uniform vec3 uC2; uniform float uFade; uniform float uMaxA; uniform float uTime;
varying float vA; varying float vSeed;
void main(){
  float ang=uTime*(1.2+vSeed*2.6)+vSeed*40.0;
  float ca=cos(ang), sa=sin(ang);
  vec2 q=mat2(ca,-sa,sa,ca)*(gl_PointCoord-vec2(0.5));
  float body=smoothstep(0.5,0.16,length(q*vec2(1.0,1.45)));
  float notch=smoothstep(0.10,0.02,abs(q.x*2.6+q.y*0.4))*step(0.0,-q.y);
  float a=clamp(body-notch*0.5,0.0,1.0)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(mix(uC,uC2,vSeed),a);
}`;
function makePetalQP(o){
  const d=Object.assign({n:80,box:[80,22,46],pos:[0,2,-10],fall:0.05,sway:0.6,drift:0.4,
    size:5,maxA:0.2,c:0xe8bcc8,c2:0xf2dce2},o||{});
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
      uW:{value:d.box[0]},uX0:{value:d.pos[0]},uSway:{value:d.sway},uDrift:{value:d.drift},
      uC:{value:C(d.c)},uC2:{value:C(d.c2)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:QP_PETAL_VERT,fragmentShader:QP_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* —— 溪面浮瓣：随水流漂去的粉瓣（InstancedMesh，1 draw call，方向可调 → 「春随流水去」） —— */
function makeDriftQP(o){
  o=o||{};
  const n=o.n===undefined?20:o.n, w=o.w===undefined?4.6:o.w, R=seedRnd(o.seed===undefined?55:o.seed);
  const geo=new THREE.PlaneGeometry(0.30,0.16); geo.rotateX(-Math.PI/2);
  const mat=new THREE.MeshPhongMaterial({color:0xe0b4c2,shininess:8,emissive:0x1a0c10,
    transparent:true,opacity:0.9,side:THREE.DoubleSide});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++) items.push({x:(R()-0.5)*92,z:(R()-0.5)*w,s:0.6+R()*0.8,ph:R()*6.283,sp:0.7+R()*0.7});
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.y=o.y===undefined?0.30:o.y;
  return {g,update:function(t,dir){
    for(let i=0;i<n;i++){
      const it=items[i];
      it.x+=(dir===undefined?-1:dir)*1.1*it.sp;
      if(it.x>46)it.x-=92; if(it.x<-46)it.x+=92;
      dm.position.set(it.x,0.03*Math.sin(t*1.8+it.ph),it.z);
      dm.rotation.set(0,it.ph+t*0.3,0);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* —— 山径：一串石板沿弯排布，愈远愈小愈疏、到乱石处而断（寂寞无行路） —— */
function makePathQP(o){
  o=o||{};
  const n=o.n===undefined?20:o.n, len=o.len===undefined?40:o.len, R=seedRnd(o.seed===undefined?7:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const u=i/(n-1);
    const x=(u-0.5)*len*0.5+(R()-0.5)*1.4*(0.4+u);
    const z=-Math.pow(u,1.2)*len-u*4;
    const w=1.5-0.72*u+R()*0.3;
    const st=new THREE.BoxGeometry(w*(0.8+R()*0.5),0.10+0.05*R(),w*(0.6+R()*0.4));
    st.rotateY((R()-0.5)*0.5);
    st.translate(x,0.03+0.03*R(),z);
    B.put(st,shadeColor(0x7c7660,0.85+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x2a2a20,emissive:0x12110a}),{c:0xa3c9a8,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 草莽：乱草小簇铺底（合批 1 mesh，「无行路」的地面质感） —— */
function makeGrassQP(o){
  o=o||{};
  const n=o.n===undefined?36:o.n, w=o.w===undefined?40:o.w, dd=o.d===undefined?18:o.d;
  const R=seedRnd(o.seed===undefined?13:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*dd, blades=3+Math.floor(R()*4);
    for(let j=0;j<blades;j++){
      const hh=0.5+R()*1.1;
      const bl=new THREE.ConeGeometry(0.045,hh,4);
      bl.rotateZ((R()-0.5)*0.5); bl.rotateX((R()-0.5)*0.5);
      bl.translate(x+(R()-0.5)*0.5,hh*0.5,z+(R()-0.5)*0.5);
      B.put(bl,shadeColor(0x1e3a22,0.7+R()*0.8));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x243c24,emissive:0x081208,side:THREE.DoubleSide}),{c:0xa3c9a8,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 蔷薇架：木架双柱+顶横杆+斜撑，蔷薇花团攀梁垂开、柱脚花丛（晚春点睛，残春之花） —— */
function makeRoseQP(o){
  o=o||{};
  const span=o.span===undefined?6.4:o.span, h=o.h===undefined?3.3:o.h, R=seedRnd(o.seed===undefined?17:o.seed);
  const g=new THREE.Group();
  const FB=new GeoBag(), woodC=0x241a12;
  [1,-1].forEach(function(s){
    const post=new THREE.CylinderGeometry(0.10,0.14,h+0.3,7);
    post.translate(s*span/2,(h+0.3)/2-0.15,0); FB.put(post,shadeColor(woodC,0.9+0.2*R()));
    const brace=new THREE.CylinderGeometry(0.05,0.06,1.5,5);
    brace.rotateZ(s*0.5); brace.translate(s*(span/2-0.55),h-0.55,0); FB.put(brace,shadeColor(woodC,0.8));
  });
  const beam=new THREE.CylinderGeometry(0.085,0.085,span+0.7,7);
  beam.rotateZ(Math.PI/2); beam.translate(0,h,0); FB.put(beam,shadeColor(woodC,1.15));
  const beam2=new THREE.CylinderGeometry(0.06,0.06,span*0.7,7);
  beam2.rotateZ(Math.PI/2); beam2.translate(0,h-0.62,0); FB.put(beam2,shadeColor(woodC,1.0));
  g.add(FB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a3228,emissive:0x0a0705}),{c:0xc9b48a,i:0.20,p:2.4})));
  /* 花团+叶：攀梁为主，两柱脚各一丛 */
  const RB=new GeoBag(), pinks=[0xd8a0b4,0xe4b8c4,0xefd2d8,0xc8889f];
  const flowerAt=function(cx,cy,cz,big){
    const cn=pinks[Math.floor(R()*pinks.length)], np=(big?3:2)+Math.floor(R()*3);
    for(let j=0;j<np;j++){
      const f=new THREE.SphereGeometry((big?0.09:0.07)+R()*0.07,6,5);
      f.translate(cx+(R()-0.5)*0.32,cy+(R()-0.5)*0.28,cz+(R()-0.5)*0.32);
      RB.put(f,shadeColor(cn,0.85+R()*0.35));
    }
  };
  for(let i=0;i<24;i++) flowerAt((R()-0.5)*span*1.06,h+(R()<0.75?(R()-0.3)*0.55:-R()*0.95),(R()-0.5)*0.5,true);
  [1,-1].forEach(function(s){
    for(let i=0;i<7;i++) flowerAt(s*span/2+(R()-0.5)*1.3,0.25+R()*1.0,(R()-0.5)*0.9,false);
  });
  for(let i=0;i<44;i++){
    const lf=new THREE.PlaneGeometry(0.34,0.16);
    lf.rotateZ((R()-0.5)*1.2); lf.rotateY(R()*3.14);
    lf.translate((R()-0.5)*span*1.05,h*0.16+R()*h*0.9,(R()-0.5)*0.5);
    RB.put(lf,shadeColor(0x2c5a30,0.7+R()*0.7));
  }
  const flowers=RB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    emissive:0x1c0d12,side:THREE.DoubleSide}));
  flowers.frustumCulled=false; g.add(flowers);
  return {g,update:function(t,k,wind){
    flowers.rotation.z=Math.sin(t*2.2)*0.006*(1+(wind===undefined?0:wind));
  }};
}

/* —— 黄鹂：明黄羽+贯眼黑纹+粉喙（全页唯一亮彩，是鸟羽黄非金）；会引颈百啭、振翅飞 —— */
function makeOrioleQP(o){
  o=o||{};
  const g=new THREE.Group();
  const yB=0xe2bd46, yW=0xc9a63c, dk=0x2a2418, bk=0xb87848;
  /* 躯干+腹+腿（合批 1 mesh） */
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.30,10,8); body.scale(1.35,0.95,0.9); body.translate(0,0.30,0); B.put(body,yB);
  const belly=new THREE.SphereGeometry(0.20,8,6); belly.scale(1.2,0.8,0.8); belly.translate(0.02,0.20,0.14); B.put(belly,shadeColor(yB,1.12));
  [1,-1].forEach(function(s){
    const lg=new THREE.CylinderGeometry(0.022,0.022,0.20,5); lg.translate(0.03*s,0.10,0); B.put(lg,dk);
  });
  const bodyMesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:22,
    specular:0x6a5a2a,emissive:0x241a06}));
  g.add(bodyMesh);
  /* 尾：羽尖深色（可摆） */
  const tailG=new THREE.Group(); tailG.position.set(-0.36,0.38,0);
  const TB=new GeoBag();
  const t1=new THREE.ConeGeometry(0.09,0.46,6); t1.rotateZ(Math.PI/2+0.18); t1.translate(-0.22,0.02,0); TB.put(t1,0x8a7430);
  const t2=new THREE.ConeGeometry(0.055,0.14,5); t2.rotateZ(Math.PI/2+0.18); t2.translate(-0.47,0.06,0); TB.put(t2,dk);
  tailG.add(TB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,emissive:0x0e0c04})));
  g.add(tailG);
  /* 双翼：肩关节起摆（栖时收拢 ↔ 飞时扑扇） */
  const wingMat=new THREE.MeshPhongMaterial({color:yW,shininess:18,emissive:0x120e04,side:THREE.DoubleSide});
  const wL=new THREE.Group(), wR=new THREE.Group();
  const wgeoL=new THREE.PlaneGeometry(0.66,0.30); wgeoL.rotateX(-Math.PI/2); wgeoL.translate(-0.30,0,0.15);
  wL.add(new THREE.Mesh(wgeoL,wingMat)); wL.position.set(-0.02,0.40,0.13); g.add(wL);
  const wgeoR=wgeoL.clone(); wgeoR.translate(0,0,-0.30);
  wR.add(new THREE.Mesh(wgeoR,wingMat)); wR.position.set(-0.02,0.40,-0.13); g.add(wR);
  /* 头颈：贯眼纹+上喙（合批），下喙单独挂关节（百啭时张口） */
  const headG=new THREE.Group(); headG.position.set(0.34,0.52,0);
  const HB=new GeoBag();
  const head=new THREE.SphereGeometry(0.155,9,7); head.translate(0.10,0.06,0); HB.put(head,yB);
  const stripe=new THREE.BoxGeometry(0.30,0.045,0.24); stripe.translate(0.06,0.05,0); HB.put(stripe,dk);
  const beakU=new THREE.ConeGeometry(0.038,0.16,5); beakU.rotateZ(-Math.PI/2); beakU.translate(0.30,0.05,0); HB.put(beakU,bk);
  headG.add(HB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,emissive:0x241a06})));
  const beakG=new THREE.Group(); beakG.position.set(0.26,0.045,0);
  const beakL=new THREE.ConeGeometry(0.028,0.12,5); beakL.rotateZ(-Math.PI/2); beakL.translate(0.06,0,0);
  beakG.add(new THREE.Mesh(beakL,new THREE.MeshPhongMaterial({color:bk,shininess:20,emissive:0x0e0804})));
  headG.add(beakG);
  g.add(headG);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  /* mode: 0 栖（收翼/引颈百啭） 1 飞（扑扇）；sing 0~1 啭的强度 */
  g.update=function(t,k,mode,sing){
    const s=sing===undefined?0:sing, fly=mode===1;
    tailG.rotation.z=fly?0.35:(-0.05*Math.sin(t*1.2));
    if(fly){
      const f=Math.sin(t*26);
      wL.rotation.set(0,0.10,-0.30+f*0.95);
      wR.rotation.set(0,-0.10,0.30-f*0.95);
      headG.rotation.z=-0.18; beakG.rotation.z=0;
    }else{
      wL.rotation.set(0,0.55,-0.12+0.02*Math.sin(t*2.2));
      wR.rotation.set(0,-0.55,0.12-0.02*Math.sin(t*2.2));
      headG.rotation.z=0.38*s+0.10*Math.sin(t*1.6);
      beakG.rotation.z=-(0.05+0.30*s*(0.6+0.4*Math.sin(t*21)));
    }
  };
  return {g,update:g.update};
}

/* —— 黄鹂百啭声：一串滑音啼啭（WebAudio 可用时；vol 0~1） —— */
function warbleQP(vol){
  if(!groupAudio.ctx)return;
  const ctx=groupAudio.ctx, now=ctx.currentTime, v=vol===undefined?1:vol;
  const seq=[[2350,0.00,0.16],[2620,0.14,0.12],[2100,0.26,0.14],[2900,0.40,0.10],[2450,0.52,0.16],
             [3150,0.68,0.09],[2300,0.80,0.12],[2700,0.94,0.10],[2050,1.08,0.14],[2550,1.22,0.10]];
  seq.forEach(function(d){
    const o=ctx.createOscillator(), gn=ctx.createGain();
    o.type='sine';
    o.frequency.setValueAtTime(d[0],now+d[1]);
    o.frequency.exponentialRampToValueAtTime(d[0]*0.72,now+d[1]+d[2]*0.8);
    o.frequency.exponentialRampToValueAtTime(d[0]*1.06,now+d[1]+d[2]);
    gn.gain.setValueAtTime(0.0001,now+d[1]);
    gn.gain.exponentialRampToValueAtTime(0.045*v,now+d[1]+0.025);
    gn.gain.exponentialRampToValueAtTime(0.0001,now+d[1]+d[2]+0.03);
    o.connect(gn).connect(groupAudio.master);
    o.start(now+d[1]); o.stop(now+d[1]+d[2]+0.06);
  });
}

function bCover(){ // 卷首 · 春山晓色 —— 青绿春山晨光初动，一径入山没入薄雾，寻春人小小的身影行在途中
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0c1710,c2:0x182a1a,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:40,layers:3,peaks:5,seed:83,color:0x0b1910,atmo:0x2c4a36,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-85); g.add(ridge.g);
  /* 一径入山（愈远愈细，消失在山脚雾里） */
  const path=makePathQP({n:24,len:56,seed:5});
  path.g.position.set(-2,-1.58,-8); path.g.rotation.y=0.14; g.add(path.g);
  /* 远溪一带横过山脚 */
  const water=makeWater({size:12,seg:18,amp:0.08,freq:0.15,speed:0.4,flow:[0.1,0.5],spec:1.0,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-60,90,-160],y:-1.5});
  water.mesh.scale.set(1,1,12); water.mesh.rotation.y=0.5; water.mesh.position.set(-16,-1.5,-34); g.add(water.mesh);
  /* 途中寻春人一痕（远景） */
  const walker=makeFigure({pose:'独立',robe:0x24352a,belt:0x6a5a30,hat:'发髻',scale:0.5,rim:0.4,rimC:0xa8c890,noProp:true});
  walker.position.set(-6.5,-1.6,-26); walker.rotation.y=0.5; g.add(walker);
  const crowd=makeCrowd({n:3,rect:[2,-46,18,8],seed:87,color:0x121d13,rimC:0x8fae78,rim:0.18});
  g.add(crowd.mesh);
  /* 晓光：东天一抹暖（晨曦，不作主角） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8d2a0,
    transparent:true,opacity:0.14,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,54,1); dawn.position.set(55,22,-130); dawn.renderOrder=-7; g.add(dawn);
  const motes=makeGlow({n:40,box:[190,28,110],pos:[0,8,-26],color:0xd0e0a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[250,32,140],pos:[0,10,-56],scale:80,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:48,n:8,d:7,color:0x081009,seed:29,sway:0.7,rim:0.12,rimC:0xa3c9a8});
  brL.g.position.set(-25,-1.6,44); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const rkR=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:31,rim:0.13,rimC:0xa3c9a8});
  rkR.g.position.set(17,-1.4,18); g.add(rkR.g);
  addLights(g,{c:0xe6d4a0,i:0.45,p:[50,80,30]},{c:0x243220,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    brL.update(t,k); rkR.update(t,k); crowd.update(t); walker.update(t,k);
    dawn.material.opacity=k*(0.10+0.025*Math.sin(t*0.4));
  }};
}
function bChungui(){ // 一 · 春归何处 —— 小径无痕没入乱石草莽，寻春人四顾；流水落花春去也
  const g=new THREE.Group();
  const grd=makeGround({r:210,c1:0x0a130d,c2:0x152417,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:42,layers:3,peaks:5,seed:91,color:0x09150e,atmo:0x2a4634,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-6});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  /* 山径：从脚下弯向山坳，到乱石处而断（无行路） */
  const path=makePathQP({n:22,len:44,seed:7});
  path.g.position.set(1,0.02,-4); path.g.rotation.y=-0.5; g.add(path.g);
  const grass=makeGrassQP({n:40,w:46,d:22,seed:13});
  grass.g.position.set(-4,0,-14); g.add(grass.g);
  /* 断路乱石：小径尽头的塌石堆（走到这里已无路） */
  const endRock=makeForeground({kind:'坡石',n:5,r:2.6,w:8,d:5,color:0x0b140c,seed:33,rim:0.16,rimC:0xa3c9a8});
  endRock.g.position.set(-8.5,-0.4,-22); g.add(endRock.g);
  /* 寻春人：立在岔口回身张望（全境唯一清晰主体） */
  const seeker=makeFigure({pose:'独立',robe:0x26382c,belt:0x6a5a30,hat:'发髻',beard:true,
    scale:1.16,rim:0.5,rimC:0xb8d0a8,noProp:true});
  seeker.position.set(4.2,0,-1.5); seeker.rotation.y=2.5; g.add(seeker);
  /* 春随流水去：溪在左，落花点点评过水面 */
  const stream=new THREE.Group();
  const water=makeWater({size:15,seg:24,amp:0.09,freq:0.17,speed:0.5,flow:[0.1,0.6],spec:1.05,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-60,90,-160],y:0.08});
  water.mesh.scale.set(1,1,11); stream.add(water.mesh);
  const bankB=new GeoBag();
  const b1=new THREE.BoxGeometry(5.6,0.9,160); b1.translate(-8.4,0.26,0); bankB.put(b1,shadeColor(0x18271c,1.0));
  const b2=new THREE.BoxGeometry(5.6,0.9,160); b2.translate(8.4,0.26,0); bankB.put(b2,shadeColor(0x1a2a1e,1.0));
  stream.add(bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0xa3c9a8,i:0.13,p:2.4})));
  stream.rotation.y=0.62; stream.position.set(-13,0,-10); g.add(stream);
  const drift=makeDriftQP({n:22,seed:55,w:4.6});
  drift.g.position.set(-13,0.30,-10); drift.g.rotation.y=0.62; g.add(drift.g);
  /* 落瓣稀疏：春已在离开的路上 */
  const petal=makePetalQP({n:70,box:[70,20,42],pos:[-2,2,-12],fall:0.05,size:5,maxA:0.20,drift:0.35});
  g.add(petal.points);
  const motes=makeGlow({n:30,box:[140,20,70],pos:[0,7,-16],color:0xd0e0a8,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[220,26,110],pos:[-4,8,-44],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:15,d:6,color:0x070d08,seed:43,rim:0.12,rimC:0xa3c9a8});
  rk.g.position.set(-12,-1.1,13); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x071009,seed:45,sway:1.1,tip:0x2c4028});
  reed.g.position.set(13,-1.0,14); g.add(reed.g);
  addLights(g,{c:0xc8ce9a,i:0.42,p:[40,75,25]},{c:0x1e2c1e,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    rk.update(t,k); reed.update(t,k); endRock.update(t,k); seeker.update(t,k);
    drift.update(t,-1.1); petal.update(t);
  },onEnter(){ pluck(1,0.12,0.09); pluck(3,0.62,0.07); }};
}
function bWenqu(){ // 二（末境·可点击）· 问取黄鹂 —— 蔷薇架畔问鸟；点击：黄鹂百啭，因风飞过蔷薇
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,phase:'perch',ph:0,wind:0.25};
  const grd=makeGround({r:220,c1:0x0b130d,c2:0x162618,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:38,layers:2,peaks:4,seed:97,color:0x091409,atmo:0x2a4634,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 小径横过，蔷薇架跨径而立 */
  const path=makePathQP({n:16,len:34,seed:11});
  path.g.position.set(-7,0.02,2); path.g.rotation.y=0.35; g.add(path.g);
  const grass=makeGrassQP({n:26,w:40,d:16,seed:15});
  grass.g.position.set(-2,0,-18); g.add(grass.g);
  const stream=new THREE.Group();
  const water=makeWater({size:16,seg:28,amp:0.08,freq:0.16,speed:0.5,flow:[0.12,0.7],spec:1.1,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-70,90,-150],y:0.08});
  water.mesh.scale.set(1,1,10); stream.add(water.mesh);
  const bankB=new GeoBag();
  const b1=new THREE.BoxGeometry(5.6,0.9,150); b1.translate(-8.6,0.26,0); bankB.put(b1,shadeColor(0x18271c,1.0));
  const b2=new THREE.BoxGeometry(5.6,0.9,150); b2.translate(8.6,0.26,0); bankB.put(b2,shadeColor(0x1a2a1e,1.0));
  stream.add(bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0xa3c9a8,i:0.13,p:2.4})));
  stream.rotation.y=Math.PI/2+0.1; stream.position.set(4,0,-20); g.add(stream);
  const drift=makeDriftQP({n:16,seed:57,w:4.4});
  drift.g.position.set(4,0.30,-20); drift.g.rotation.y=Math.PI/2+0.1; g.add(drift.g);
  /* 蔷薇架（晚春点睛）+ 黄鹂栖在架顶横杆（全页唯一明黄） */
  const rose=makeRoseQP({span:6.4,h:3.3,seed:17});
  rose.g.position.set(3.4,0,-9.8); g.add(rose.g);
  const bird=makeOrioleQP({scale:1.9});
  const perch={p:new THREE.Vector3(4.6,3.66,-9.6),yaw:-2.75};
  bird.g.position.copy(perch.p); bird.g.rotation.y=perch.yaw; g.add(bird.g);
  /* 栖点微辉：给一点黄鹂的暖晕（ sing 时增强，峰值 ≤ 初值 0.16 ） */
  const birdGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c860,
    transparent:true,opacity:0.14,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  birdGlow.scale.set(4.5,4.5,1); birdGlow.position.set(4.6,3.9,-9.5); birdGlow.renderOrder=4; g.add(birdGlow);
  /* 寻春人：指而问之（像问路一样问鸟） */
  const seeker=makeFigure({pose:'指月',robe:0x26382c,belt:0x6a5a30,hat:'发髻',beard:true,
    scale:1.16,rim:0.5,rimC:0xb8d0a8,noProp:true});
  seeker.position.set(-3.4,0,-6.6); seeker.rotation.y=1.95; g.add(seeker);
  /* 落瓣 + 起飞爆瓣 */
  const petal=makePetalQP({n:90,box:[80,22,46],pos:[3,2,-10],fall:0.055,size:5,maxA:0.22,drift:0.4});
  g.add(petal.points);
  const burst=makeBurst({n:60,color:0xf0ccd8,pos:[4.6,3.9,-9.6]});
  g.add(burst.points);
  const motes=makeGlow({n:30,box:[150,20,80],pos:[0,7,-14],color:0xd0e0a8,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[210,24,100],pos:[0,8,-46],scale:74,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:40,n:7,d:6,color:0x081009,seed:47,sway:0.8,rim:0.12,rimC:0xa3c9a8});
  brL.g.position.set(-21,-1.0,15); brL.g.scale.setScalar(1.7); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:14,d:6,color:0x070d08,seed:49,rim:0.13,rimC:0xa3c9a8});
  rk.g.position.set(13,-1.2,12); g.add(rk.g);
  addLights(g,{c:0xd8ce9a,i:0.44,p:[-45,70,25]},{c:0x203020,i:0.65});
  /* 飞行路线：栖点 → 越架顶 → 画右远去；归程绕高弧回栖（黄鹂百啭 + 飞过蔷薇架） */
  const ease=function(u){ return u*u*(3-2*u); };
  const qbez=function(a,b,c,u,out){ const s=1-u;
    out.set(s*s*a.x+2*s*u*b.x+u*u*c.x, s*s*a.y+2*s*u*b.y+u*u*c.y, s*s*a.z+2*s*u*b.z+u*u*c.z); return out; };
  const P0=perch.p, P1=new THREE.Vector3(7.4,7.8,-12.0), P2=new THREE.Vector3(16.5,5.4,-15.0),
        P3=new THREE.Vector3(9.0,9.4,-3.5);
  const tmp=new THREE.Vector3(), prev=new THREE.Vector3().copy(P0);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt; ctl.ph+=dt;
      /* 风：栖时微，啭时起，飞时盛（蔷薇瓣因风漫架） */
      const wTarget=(ctl.phase==='fly'||ctl.phase==='back')?2.3:(ctl.phase==='sing'?1.2:0.25);
      ctl.wind+=(wTarget-ctl.wind)*Math.min(1,dt*1.6);
      petal.mat.uniforms.uDrift.value=0.4+ctl.wind*1.15;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      rk.update(t,k); brL.update(t,k); seeker.update(t,k);
      rose.update(t,k,ctl.wind); drift.update(t,-(1.1+ctl.wind*0.5)); burst.update(t);
      birdGlow.material.opacity=k*(0.08+0.06*ctl.wind/2.3);
      /* 黄鹂状态机：栖 → 啭 → 飞越蔷薇架 → 绕高弧归栖（可再问） */
      if(ctl.phase==='sing'){
        bird.update(t,k,0,1);
        if(ctl.ph>=1.15){ ctl.phase='fly'; ctl.ph=0; prev.copy(P0); burst.fire(); }
      }else if(ctl.phase==='fly'){
        const u=ease(Math.min(1,ctl.ph/2.6));
        qbez(P0,P1,P2,u,tmp);
        bird.g.rotation.y=Math.atan2(-(tmp.z-prev.z),tmp.x-prev.x);
        prev.copy(tmp); bird.g.position.copy(tmp);
        bird.update(t,k,1,0);
        if(ctl.ph>=2.6){ ctl.phase='back'; ctl.ph=0; prev.copy(P2); }
      }else if(ctl.phase==='back'){
        const u=ease(Math.min(1,ctl.ph/2.5));
        qbez(P2,P3,P0,u,tmp);
        bird.g.rotation.y=Math.atan2(-(tmp.z-prev.z),tmp.x-prev.x);
        prev.copy(tmp); bird.g.position.copy(tmp);
        bird.update(t,k,1,0);
        if(ctl.ph>=2.5){ ctl.phase='perch'; ctl.ph=0;
          bird.g.position.copy(P0); bird.g.rotation.y=perch.yaw; }
      }else{
        bird.update(t,k,0,0);
      }
    },click(){
      if(ctl.t<1.2)return;
      if(ctl.phase==='perch'&&ctl.ph>0.3){
        ctl.phase='sing'; ctl.ph=0; warbleQP(1);
        if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
        const fl=$('#flash'); fl.textContent='因风飞过蔷薇'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }else if(ctl.phase==='sing'){ ctl.ph=Math.max(ctl.ph,1.0); }  /* 啭中将尽：尽快起飞 */
    },clicked:false};
  return api;
}
