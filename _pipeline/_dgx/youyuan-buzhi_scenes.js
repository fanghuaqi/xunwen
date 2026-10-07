/* ================= 游园不值 · 三境场景（青绿春晓·园墙春晓变体：卷首园外春晓、屐齿苍苔、红杏出墙）
   本诗专属系统「关不住」：一道粉墙一扇柴扉，前境冷寂紧闭（抑：门冷、苔静、扣而不开），
   末境墙头一枝红杏破壁而出（扬：色满、杏出、扑面而来）——红杏红 #c96a6a 是全页唯一浓彩；
   末境点击：柴扉虚掩、红杏探出墙头招展，门缝里漏出一线满园春色 ================= */

/* —— 粉墙黛瓦：三段微错落的园墙（合批 1 mesh），本诗「关」之形 —— */
function makeWallYYBZ(o){
  o=o||{};
  const w=o.w===undefined?27:o.w, h=o.h===undefined?3.8:o.h;
  const wallC=o.wall===undefined?0x9aa08e:o.wall, capC=o.cap===undefined?0x2a2f26:o.cap;
  const R=seedRnd(o.seed===undefined?7:o.seed);
  const B=new GeoBag();
  for(let i=0;i<3;i++){
    const sw=w/3, x0=-w/2+sw*(i+0.5);
    const sh=h*(0.94+R()*0.10);
    const seg=new THREE.BoxGeometry(sw*1.005,sh,0.55);
    seg.translate(x0,sh*0.5,(R()-0.5)*0.06);
    B.put(seg,shadeColor(wallC,0.92+R()*0.16));
    const cap=new THREE.BoxGeometry(sw*1.06,0.22,0.86);
    cap.translate(x0,sh+0.11,0);
    B.put(cap,shadeColor(capC,0.9+R()*0.2));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a4038,emissive:0x0a0d09}),{c:o.rimC===undefined?0x9fce8f:o.rimC,i:o.rim===undefined?0.16:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 柴门：门框+柴扉（door 可绕门轴转，末境点击后虚掩露出园内春色） —— */
function makeChaiFeiYYBZ(o){
  o=o||{};
  const w=o.w===undefined?3.6:o.w, h=o.h===undefined?3.3:o.h;
  const woodC=o.wood===undefined?0x3a2e1e:o.wood, stickC=o.stick===undefined?0x4a3a24:o.stick;
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const post=new THREE.CylinderGeometry(0.16,0.20,h,7);
    post.translate(s*w/2,h/2,0); B.put(post,shadeColor(woodC,1.0));
    const bs=new THREE.BoxGeometry(0.5,0.3,0.5); bs.translate(s*w/2,0.15,0); B.put(bs,shadeColor(0x55584a,0.9));
  });
  const beam=new THREE.BoxGeometry(w+0.7,0.28,0.5); beam.translate(0,h,0); B.put(beam,shadeColor(woodC,1.25));
  const frame=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2e2a20,emissive:0x080604}),{c:o.rimC===undefined?0x9fce8f:o.rimC,i:0.16,p:2.4}));
  const g=new THREE.Group(); g.add(frame);
  /* 柴扉：竖枝+两道横木+一道斜撑，铰链在左缘（door.rotation.y 负值=向内虚掩） */
  const hinge=new THREE.Group(); hinge.position.set(-w/2+0.34,0,0.12);
  const D=new GeoBag();
  const dw=w-0.68, dh=h-0.7, R=seedRnd(o.seed===undefined?17:o.seed);
  const n=Math.round(dw/0.30);
  for(let i=0;i<=n;i++){
    const x=i/n*dw;
    const st=new THREE.CylinderGeometry(0.055,0.075,dh,5);
    st.translate(x,dh/2+0.1,(R()-0.5)*0.05);
    D.put(st,shadeColor(stickC,0.85+R()*0.35));
  }
  [dh*0.22,dh*0.78].forEach(function(y){
    const rail=new THREE.BoxGeometry(dw,0.18,0.08); rail.translate(dw/2,y+0.1,0.09); D.put(rail,shadeColor(woodC,1.3));
  });
  const brace=new THREE.BoxGeometry(dw*1.15,0.14,0.07);
  brace.rotateZ(0.42); brace.translate(dw/2,dh/2+0.1,0.16); D.put(brace,shadeColor(woodC,1.18));
  const door=D.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a2418,emissive:0x060503}),{c:0x9fce8f,i:0.12,p:2.4}));
  hinge.add(door); g.add(hinge);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,door:hinge};
}

/* —— 苍苔屐齿：湿地上苔斑成片；prints=true 时一串双齿屐印从路口走到门前 —— */
function makeMossYYBZ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?29:o.seed);
  const B=new GeoBag();
  const n=o.n===undefined?16:o.n, w=o.w===undefined?16:o.w;
  for(let i=0;i<n;i++){
    const r=0.38+R()*0.92;
    const blob=new THREE.SphereGeometry(r,7,5); blob.scale(1.6,0.14,1.2);
    blob.translate((R()-0.5)*w,0.03,(R()-0.5)*10);
    B.put(blob,shadeColor(0x1d3a20,0.75+R()*0.55));
  }
  if(o.prints){
    for(let i=0;i<6;i++){
      const t=i/5, px=2.9-(2.9-1.35)*t, pz=-4.5-7.2*t;
      [1,-1].forEach(function(s){
        const pr=new THREE.CylinderGeometry(0.10,0.12,0.06,6);
        pr.translate(px+s*0.30,0.048,pz+(s>0?0.30:0));
        B.put(pr,shadeColor(0x0c1a0e,1.0));
      });
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:18,
    specular:0x2c4a30,emissive:0x060f08}),{c:0x9fce8f,i:0.22,p:2.3}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 红杏出墙：枝干自园内翻上墙头、朝游人探来，杏花簇拥成云——全页唯一浓彩（标志瞬间） —— */
function makeXingYYBZ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?43:o.seed);
  const pts=[new THREE.Vector3(5.5,0.5,-17.5),
    new THREE.Vector3(4.0,2.6,-15.6), new THREE.Vector3(2.6,4.15,-13.6),
    new THREE.Vector3(1.2,5.4,-11.9), new THREE.Vector3(-0.4,5.9,-10.6)];
  const curve=new THREE.CatmullRomCurve3(pts);
  const B=new GeoBag();
  B.put(new THREE.TubeGeometry(curve,22,0.10,6,false),0x2e2016);
  const c2=new THREE.CatmullRomCurve3([pts[2],new THREE.Vector3(3.4,5.0,-12.6),new THREE.Vector3(2.6,5.8,-11.4)]);
  B.put(new THREE.TubeGeometry(c2,10,0.055,5,false),0x2a1e14);
  const c3=new THREE.CatmullRomCurve3([pts[3],new THREE.Vector3(-0.6,6.3,-12.2),new THREE.Vector3(-1.6,6.7,-11.6)]);
  B.put(new THREE.TubeGeometry(c3,10,0.05,5,false),0x302216);
  /* 杏花：只在红杏一族里取色——它是全页唯一的浓彩点 */
  const bloomCs=[0xc96a6a,0xd98f84,0xb85448,0xe0a494];
  const nb=o.blobs===undefined?26:o.blobs;
  for(let i=0;i<nb;i++){
    const u=0.55+0.45*R();
    const p=curve.getPoint(u);
    const r=0.16+R()*0.30;
    const sp=new THREE.SphereGeometry(r,6,5);
    sp.translate(p.x+(R()-0.5)*0.9, p.y+(R()-0.2)*0.8, p.z+(R()-0.5)*0.9);
    B.put(sp,bloomCs[Math.floor(R()*bloomCs.length)%bloomCs.length]);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a2a24,emissive:0x140806}),{c:o.rimC===undefined?0xe89a8a:o.rimC,i:o.rim===undefined?0.5:o.rim,p:2.2}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 招展：绕墙头支点轻摆；e（0..1）放大摆幅——点击后红杏出墙招展 */
  g.update=function(t,e){
    const en=e===undefined?0:e;
    g.rotation.z=0.020*Math.sin(t*0.7)*(1+2.2*en);
    g.rotation.x=0.012*Math.sin(t*0.53+1.7)*(1+2.2*en);
  };
  return {g,update:g.update};
}

/* —— 杏花落英：粉白小瓣缓落（点内画椭圆小瓣+旋转飘），春的可见性 —— */
const YYBZ_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uH; uniform float uB;
varying float vA; varying float vR;
void main(){
  vec3 p=position;
  float sp=0.55+aSeed*0.5;
  float y=mod(p.y-uB-uTime*sp,uH);
  p.y=uB+y;
  p.x+=sin(uTime*0.7+aSeed*47.0)*1.1;
  p.z+=cos(uTime*0.5+aSeed*31.0)*0.7;
  vA=smoothstep(0.0,uH*0.08,y)*(1.0-smoothstep(uH*0.9,uH,y));
  vR=uTime*(0.6+aSeed*0.7)+aSeed*40.0;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(150.0/max(1.0,-mv.z)),18.0);
  gl_Position=projectionMatrix*mv;
}`;
const YYBZ_PETAL_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vR;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float cs=cos(vR), sn=sin(vR);
  q=mat2(cs,-sn,sn,cs)*q;
  float a=smoothstep(0.30,0.16,length(q*vec2(1.0,1.6)))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makePetalsYYBZ(o){
  const d=Object.assign({n:80,box:[24,8,12],pos:[1.2,0,-11.5],size:9,maxA:0.30,c:0xd8b0a4},o||{});
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
    uniforms:{uTime:{value:0},uH:{value:d.box[1]},uB:{value:d.pos[1]},
      uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:YYBZ_PETAL_VERT,fragmentShader:YYBZ_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 燕子：剪影小燕掠墙而过（1 mesh 1 只，机身沿 +z，lookAt 飞行方向） —— */
function makeSwallowYYBZ(o){
  o=o||{};
  const c=o.color===undefined?0x0b130d:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.16,6,5); body.scale(0.7,0.65,2.1); B.put(body,c);
  const tail=new THREE.ConeGeometry(0.09,0.46,4); tail.rotateX(-Math.PI/2); tail.translate(0,0.02,-0.42); B.put(tail,c);
  const wl=new THREE.PlaneGeometry(0.38,1.0); wl.rotateX(-Math.PI/2); wl.translate(0.44,0.05,0.05); B.put(wl,c);
  const wr=new THREE.PlaneGeometry(0.38,1.0); wr.rotateX(-Math.PI/2); wr.translate(-0.44,0.05,0.05); B.put(wr,c);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    side:THREE.DoubleSide,emissive:0x050a06}));
  const g=new THREE.Group(); g.add(mesh);
  const cx=o.x===undefined?0:o.x, cy=o.y===undefined?8:o.y, cz=o.z===undefined?-13:o.z;
  const rx=o.rx===undefined?10:o.rx, rz=o.rz===undefined?5:o.rz, sp=o.sp===undefined?0.5:o.sp, ph=o.ph===undefined?0:o.ph;
  const prv=new THREE.Vector3(), nxt=new THREE.Vector3();
  g.update=function(t){
    const a=ph+t*sp, a2=a+0.06;
    prv.set(cx+Math.cos(a)*rx, cy+Math.sin(a*1.7)*1.2, cz+Math.sin(a)*rz);
    nxt.set(cx+Math.cos(a2)*rx, cy+Math.sin(a2*1.7)*1.2, cz+Math.sin(a2)*rz);
    g.position.copy(prv);
    g.lookAt(nxt);
  };
  return {g,update:g.update};
}

/* —— 园内春色：粉白偏绿的花树两株（柴扉紧闭时被挡住，虚掩后从门缝漏出——园内的春不是红，红只在墙头那枝） —— */
function makeSpringYYBZ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?61:o.seed);
  const B=new GeoBag();
  const n=o.n===undefined?2:o.n;
  for(let j=0;j<n;j++){
    const cx=(j===0?-1.4:2.2), cz=-j*1.6, h=4.6+R()*1.6;
    const trunk=new THREE.CylinderGeometry(0.12,0.20,h*0.55,6); trunk.translate(cx,h*0.27,cz); B.put(trunk,0x2a2016);
    for(let i=0;i<6;i++){
      const r=0.7+R()*0.8;
      const blob=new THREE.SphereGeometry(r,6,5);
      blob.translate(cx+(R()-0.5)*2.2, h*0.55+R()*h*0.45, cz+(R()-0.5)*1.6);
      B.put(blob,shadeColor(0xcfd8c0,0.85+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3c4438,emissive:0x0a0e08}),{c:0xd8e4c8,i:0.35,p:2.2}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 青绿杂树：干+团冠（合批 1 mesh），晨色里的中景 —— */
function makeTreeYYBZ(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, R=seedRnd(o.seed===undefined?5:o.seed);
  const leaf=o.leaf===undefined?0x16301c:o.leaf;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.10,h*0.03,h*0.55,6); trunk.translate((R()-0.5)*0.2,h*0.27,0); B.put(trunk,0x1c1712);
  for(let i=0;i<3;i++){
    const r=h*(0.24+R()*0.14);
    const blob=new THREE.SphereGeometry(r,7,5); blob.scale(1.15,0.85,1.1);
    blob.translate((R()-0.5)*h*0.4, h*(0.52+i*0.16)+(R()-0.5)*0.5, (R()-0.5)*h*0.25);
    B.put(blob,shadeColor(leaf,0.8+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3a26,emissive:0x060c08}),{c:o.rimC===undefined?0x8fce7f:o.rimC,i:0.2,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

function bCover(){ // 卷首 · 春晓园外 —— 一带粉墙先掩着，晨雾里还看不见那枝红杏
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0b1710,c2:0x18291b,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:3,peaks:5,seed:57,color:0x0c1911,atmo:0x2c4434,fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-80); g.add(ridge.g);
  /* 园墙与柴扉（远，紧闭） */
  const wl=makeWallYYBZ({w:27,seed:71}); wl.g.position.set(-16.5,-1.6,-40); wl.g.rotation.y=0.10; g.add(wl.g);
  const wr=makeWallYYBZ({w:27,seed:73}); wr.g.position.set(16.5,-1.6,-40); wr.g.rotation.y=-0.06; g.add(wr.g);
  const gate=makeChaiFeiYYBZ({}); gate.g.position.set(0,-1.6,-40); g.add(gate.g);
  /* 通向柴门的小径 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.10,42),
    new THREE.MeshPhongMaterial({color:0x6d7260,shininess:4,emissive:0x101208}));
  path.position.set(0.6,-1.55,-20); path.rotation.y=0.03; g.add(path);
  /* 两三株杂树夹径（中景） */
  const t1=makeTreeYYBZ({h:8,seed:81}); t1.g.position.set(-9,-1.6,-34); g.add(t1.g);
  const t2=makeTreeYYBZ({h:6.5,seed:83}); t2.g.position.set(10,-1.6,-30); g.add(t2.g);
  const t3=makeTreeYYBZ({h:9,seed:85}); t3.g.position.set(-20,-1.6,-26); g.add(t3.g);
  /* 远行的诗人：正沿小径走向园门（远景小，不抢戏） */
  const poet=makeFigure({pose:'独立',robe:0x24302a,belt:0x6f5a2e,hat:'幞头',scale:1.05,rim:0.4,rimC:0xa8c498,noProp:true});
  poet.position.set(2.2,-1.6,-24); poet.rotation.y=Math.atan2(0-2.2,-40-(-24)); g.add(poet);
  /* 远处村舍人影（墙尽头以左，不被园墙挡住） */
  const crowd=makeCrowd({n:4,rect:[-45,-44,12,8],seed:67,color:0x121d13,rimC:0x8fae78,rim:0.2,y:-1.6});
  g.add(crowd.mesh);
  /* 晨光熹微：东天一抹微暖的天光（全页唯一暖彩留给墙头红杏，此处只是天色） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8e0a8,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,54,1); dawn.position.set(55,20,-120); dawn.renderOrder=-7; g.add(dawn);
  const motes=makeGlow({n:40,box:[170,26,90],pos:[0,8,-24],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,30,120],pos:[0,10,-50],scale:78,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:48,n:8,d:7,color:0x081009,seed:19,sway:0.7,rim:0.12,rimC:0x9fce8f});
  brL.g.position.set(-24,-1.6,40); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const rkR=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x060c08,seed:21,rim:0.14,rimC:0x9fce8f});
  rkR.g.position.set(15,-1.4,16); g.add(rkR.g);
  addLights(g,{c:0xdde0b0,i:0.52,p:[50,70,40]},{c:0x22301f,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    brL.update(t,k); rkR.update(t,k); crowd.update(t); poet.update(t,k);
    dawn.material.opacity=k*(0.12+0.04*Math.sin(t*0.4));
  }};
}
function bCangtai(){ // 一（抑）· 屐齿苍苔 —— 柴门紧闭、苍苔屐齿，小扣久久不开
  const g=new THREE.Group();
  const grd=makeGround({r:200,c1:0x0a130d,c2:0x162517,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:36,layers:3,peaks:5,seed:91,color:0x09150e,atmo:0x29412e,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  /* 园墙两段+柴门（紧闭=「久不开」） */
  const wl=makeWallYYBZ({w:27,seed:71}); wl.g.position.set(-16.4,0,-14); wl.g.rotation.y=0.06; g.add(wl.g);
  const wr=makeWallYYBZ({w:27,seed:73}); wr.g.position.set(16.4,0,-14); wr.g.rotation.y=-0.05; g.add(wr.g);
  const gate=makeChaiFeiYYBZ({}); gate.g.position.set(0,0,-14); g.add(gate.g);
  /* 苍苔与屐齿印（沿路到门前——「屐齿印苍苔」的痕迹叙事） */
  const moss=makeMossYYBZ({n:18,w:18,seed:29,prints:true}); moss.g.position.set(0.4,0,-8.5); g.add(moss.g);
  /* 门前小径 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.08,28),
    new THREE.MeshPhongMaterial({color:0x676c58,shininess:4,emissive:0x0f110a}));
  path.position.set(1.2,0.05,1); path.rotation.y=0.05; g.add(path);
  /* 扣门诗人：面对柴扉、扬手小扣（举杯姿不持物=抬手扣门） */
  const poet=makeFigure({pose:'举杯',robe:0x24302a,belt:0x6f5a2e,hat:'幞头',scale:1.16,rim:0.46,rimC:0xa8c498,noProp:true});
  poet.position.set(2.5,0,-9.6);
  poet.rotation.y=Math.atan2(0-2.5,-14-(-9.6)); g.add(poet);
  /* 墙外杂树两株 + 远处村人 */
  const t1=makeTreeYYBZ({h:8,seed:95}); t1.g.position.set(-11,0,-11); g.add(t1.g);
  const t2=makeTreeYYBZ({h:6,seed:97}); t2.g.position.set(12,0,-10.5); g.add(t2.g);
  const crowd=makeCrowd({n:3,rect:[18,-30,12,8],seed:77,color:0x121c13,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  const motes=makeGlow({n:30,box:[90,16,50],pos:[0,6,-8],color:0xc4d8ac,size:5,speed:0.035,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[140,22,70],pos:[0,7,-34],scale:60,color:0x1c3020,op:0.12});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:14,d:6,color:0x060b07,seed:41,rim:0.12,rimC:0x9fce8f});
  rk.g.position.set(-12,-1.0,10); g.add(rk.g);
  const brR=makeForeground({kind:'树枝',w:26,n:7,d:5,color:0x070f08,seed:43,sway:0.8,rim:0.14,rimC:0x9fce8f});
  brR.g.position.set(12,-0.6,12); brR.g.scale.setScalar(1.4); g.add(brR.g);
  addLights(g,{c:0xb8c4a0,i:0.36,p:[-30,60,26]},{c:0x1a261c,i:0.66});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      rk.update(t,k); brR.update(t,k); crowd.update(t); poet.update(t,k);
      t1.g.rotation.z=Math.sin(t*0.35)*0.006;
    }};
}
function bXing(){ // 二（末境·可点击·扬）· 红杏出墙 —— 春色满园关不住，一枝红杏出墙来
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,reveal:0};
  const grd=makeGround({r:200,c1:0x0b150e,c2:0x17271a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:38,layers:2,peaks:4,seed:99,color:0x0a160e,atmo:0x2c4630,
    fogK:0.60,glowK:0.05,glow:0xa2c488,y:-8});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 同一道园墙、同一扇柴门（对切延续），末境点击后虚掩 */
  const wl=makeWallYYBZ({w:27,seed:71}); wl.g.position.set(-16.4,0,-14); wl.g.rotation.y=0.06; g.add(wl.g);
  const wr=makeWallYYBZ({w:27,seed:73}); wr.g.position.set(16.4,0,-14); wr.g.rotation.y=-0.05; g.add(wr.g);
  const gate=makeChaiFeiYYBZ({}); gate.g.position.set(0,0,-14); g.add(gate.g);
  /* 园内春色：柴扉紧闭时被挡住，虚掩后从门缝漏出 */
  const spring=makeSpringYYBZ({n:2,seed:61}); spring.g.position.set(0,0,-17.5); g.add(spring.g);
  /* 门缝漏光：一线春光（初值=公式峰值 0.5，每帧乘 fadeK） */
  const seam=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xdcead0,
    transparent:true,opacity:0.5,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  seam.scale.set(7,5,1); seam.position.set(-0.4,2.1,-15.2); seam.renderOrder=4; g.add(seam);
  /* 红杏出墙：全页唯一浓彩（标志瞬间） */
  const xing=makeXingYYBZ({seed:43}); g.add(xing.g);
  /* 落英：粉白花瓣缓落 */
  const petals=makePetalsYYBZ({n:80,box:[24,8,12],pos:[1.2,0,-11.5],size:9,maxA:0.30,c:0xd8b0a4});
  g.add(petals.points);
  /* 燕子两只：掠墙而过 */
  const sw1=makeSwallowYYBZ({x:-2,y:7.5,z:-12,rx:12,rz:4,sp:0.42,ph:1.2});
  const sw2=makeSwallowYYBZ({x:4,y:9,z:-16,rx:15,rz:5,sp:0.34,ph:3.6});
  g.add(sw1.g,sw2.g);
  /* 诗人：惊喜抬头，指向墙头红杏（指月姿） */
  const poet=makeFigure({pose:'指月',robe:0x24302a,belt:0x6f5a2e,hat:'幞头',scale:1.16,rim:0.5,rimC:0xb8d0a8,noProp:true});
  poet.position.set(-3.4,0,-8.6);
  poet.rotation.y=Math.atan2(0.6-(-3.4),-11.5-(-8.6)); g.add(poet);
  /* 苍苔仍在（上一境的延续，避开门前小径） */
  const moss=makeMossYYBZ({n:10,w:10,seed:29,prints:false}); moss.g.position.set(-4.5,0,-8); g.add(moss.g);
  /* 墙外杂树 */
  const t1=makeTreeYYBZ({h:7,seed:95}); t1.g.position.set(-13,0,-10.5); g.add(t1.g);
  const t2=makeTreeYYBZ({h:5.5,seed:97}); t2.g.position.set(13.5,0,-11); g.add(t2.g);
  const motes=makeGlow({n:30,box:[100,16,54],pos:[0,7,-8],color:0xd8e4b8,size:5,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[150,22,70],pos:[0,7,-38],scale:62,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:5,color:0x060b07,seed:51,rim:0.12,rimC:0x9fce8f});
  rk.g.position.set(11,-1.0,11); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:16,n:9,d:5,color:0x071009,seed:53,sway:1.0,tip:0x2c4028});
  reed.g.position.set(-11,-0.8,12); g.add(reed.g);
  addLights(g,{c:0xe2d8a8,i:0.46,p:[40,70,30]},{c:0x1e2c20,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/2.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const rv=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);   // smoothstep：虚掩与漏光缓起缓收
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      rk.update(t,k); reed.update(t,k); poet.update(t,k);
      xing.update(t,Math.min(1,ctl.pulse*0.8+rv*0.5));   // 红杏招展：点击后摆幅放大
      petals.update(t); sw1.update(t); sw2.update(t);
      petals.mat.uniforms.uMaxA.value=0.30+0.18*Math.min(1,ctl.pulse+rv);  // 点击后落英密一拍
      /* 柴扉虚掩：门轴缓缓转开一线，门缝漏光渐显（乘 fadeK） */
      gate.door.rotation.y=-0.92*rv;
      seam.material.opacity=k*(0.36*rv+0.12*ctl.pulse);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.15); pluck(2,0.4,0.12); pluck(4,0.9,0.11); pluck(5,1.5,0.09);
        const fl=$('#flash'); fl.textContent='春色满园关不住'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                            // 可反复点：红杏再招展一拍
    },clicked:false};
  return api;
}
