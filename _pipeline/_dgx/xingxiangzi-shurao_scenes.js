/* ================= 行香子·树绕村庄 · 五境场景（青绿春晓：卷首村外、树绕村庄、收尽春光、青旗流水、莺燕蝶忙）
   本诗专属系统「三色春光」：桃花红/李花白/菜花黄三色花田是全词彩点——
   境二入园，三色花田次第点亮（标志性瞬间）；
   末境步上东冈回望村庄，莺啼/燕舞/蝶忙三组动态齐来，
   点击画面——红白黄三色花田再次次第点亮，满眼春光（queue 交互） ================= */

/* —— 缓落花瓣：粉白小片打着旋儿落（青绿春晓粒子母题；Points 自定义双 shader） —— */
const XXS_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uFall; uniform float uH; uniform float uB; uniform float uSway;
varying float vA; varying float vR;
void main(){
  vec3 p=position;
  float sp=uFall*(0.75+aSeed*0.5);
  float y=mod(p.y-uB-uTime*sp,uH);
  p.y=uB+y;
  p.x+=sin(uTime*1.4+aSeed*47.0)*uSway*(0.4+0.7*(1.0-y/uH));
  p.z+=cos(uTime*1.1+aSeed*29.0)*uSway*0.6;
  vA=smoothstep(0.0,uH*0.05,y)*(1.0-smoothstep(uH*0.92,uH,y));
  vR=aSeed*6.283+uTime*(0.7+aSeed*0.9);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(150.0/max(1.0,-mv.z)),18.0);
  gl_Position=projectionMatrix*mv;
}`;
const XXS_PETAL_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vR;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float c=cos(vR),s=sin(vR);
  vec2 r=mat2(c,-s,s,c)*q;
  float e=length(vec2(r.x*3.1,r.y*4.4));
  float a=(1.0-smoothstep(0.86,1.12,e))*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makePetalXXS(o){
  const d=Object.assign({n:44,box:[90,16,60],pos:[0,9,-8],fall:0.55,sway:1.2,
    size:7,maxA:0.34,c:0xe8c8d2},o||{});
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
      uSway:{value:d.sway},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:XXS_PETAL_VERT,fragmentShader:XXS_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 三色花田：一片花田=底色床+花簇 InstancedMesh（2 draw call），可被「点亮」（setLight/初值=最大值） —— */
function makeFlowerFieldXXS(o){
  o=o||{};
  const n=o.n===undefined?90:o.n, w=o.w===undefined?5:o.w, dd=o.d===undefined?4:o.d;
  const R=seedRnd(o.seed===undefined?11:o.seed);
  const col=o.color===undefined?0xd86a5a:o.color;
  const g=new THREE.Group();
  const bedM=new THREE.MeshPhongMaterial({color:shadeColor(col,0.60),emissive:col,emissiveIntensity:0.08,
    transparent:true,opacity:0.77,shininess:4});
  const bed=new THREE.Mesh(new THREE.PlaneGeometry(w,dd),bedM);
  bed.rotation.x=-Math.PI/2; bed.position.y=0.05; g.add(bed);
  const geo=new THREE.SphereGeometry(0.21,6,4); geo.scale(1,0.72,1);
  const mat=new THREE.MeshPhongMaterial({color:col,emissive:col,emissiveIntensity:0.15,
    transparent:true,opacity:1.0,shininess:10});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++) items.push({x:(R()-0.5)*w*0.96,z:(R()-0.5)*dd*0.96,s:0.65+R()*1.15,ph:R()*6.283});
  mesh.frustumCulled=false;
  g.add(mesh);
  return {g,update:function(t,lit,k){
    const kk=(k===undefined?1:k), li=(lit===undefined?0.3:lit);
    mat.opacity=kk*(0.35+0.65*li);
    mat.emissiveIntensity=kk*(0.15+1.45*li);
    bedM.opacity=kk*(0.22+0.55*li);
    bedM.emissiveIntensity=kk*(0.08+0.75*li);
    for(let i=0;i<n;i++){
      const it=items[i];
      dm.position.set(it.x,0.15*it.s+0.035*Math.sin(t*1.6+it.ph),it.z);
      dm.scale.setScalar(it.s*(0.72+0.38*li));
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}
/* —— 绿树/花树：主干+团状树冠（GeoBag 合批 1 mesh；leaf 传花色即花树，可带一根横枝站台小禽） —— */
function makeTreeXXS(o){
  o=o||{};
  const h=o.h===undefined?6:o.h, R=seedRnd(o.seed===undefined?7:o.seed);
  const trunkC=o.trunk===undefined?0x241a10:o.trunk, leaf=o.leaf===undefined?0x2e5c30:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.5-0.25,h*0.6,0],h*0.05,h*0.022,7),trunkC);
  const nb=o.blobs===undefined?3:o.blobs;
  for(let i=0;i<nb;i++){
    const r=h*(0.19+0.15*R()), a=R()*6.283, rr=h*0.09+R()*h*0.15;
    const sp=new THREE.SphereGeometry(r,8,6);
    sp.scale(1,0.85,1); sp.translate(Math.cos(a)*rr,h*(0.66+0.22*R()),Math.sin(a)*rr*0.7);
    B.put(sp,shadeColor(leaf,0.82+R()*0.42));
  }
  if(o.branch){
    const br=limbGeo([0,h*0.55,0],[o.branch[0],o.branch[1],o.branch[2]],h*0.02,h*0.008,6);
    B.put(br,trunkC);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3c2a,emissive:0x0a140c,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xa0c9b8:o.rimC,i:o.rim===undefined?0.20:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.rotation.y=(o.rot===undefined?R()*6.283:o.rot);
  return {g};
}

/* —— 垂柳：主干+下垂柳丝（合批 1 mesh；水满陂塘岸边春风摆） —— */
function makeWillowXXS(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, R=seedRnd(o.seed===undefined?9:o.seed);
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.4-0.2,h*0.55,0],h*0.045,h*0.02,7),0x2a2014);
  const nl=o.fronds===undefined?7:o.fronds;
  for(let i=0;i<nl;i++){
    const a=i/nl*6.283+R()*0.55, rr=h*(0.10+0.15*R());
    const x0=Math.cos(a)*rr, z0=Math.sin(a)*rr, y0=h*(0.58+0.28*R());
    const x1=x0+Math.cos(a)*h*0.11, y1=y0-h*0.26, z1=z0+Math.sin(a)*h*0.11;
    const x2=x1+Math.cos(a)*h*0.06+(R()-0.5)*0.3, y2=y1-h*0.30, z2=z1+Math.sin(a)*h*0.06;
    B.put(limbGeo([x0,y0,z0],[x1,y1,z1],0.05,0.032,5),0x3a6234);
    B.put(limbGeo([x1,y1,z1],[x2,y2,z2],0.032,0.016,5),0x47743a);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2c4430,emissive:0x0a140a}),{c:o.rimC===undefined?0xa0c9b8:o.rimC,i:o.rim===undefined?0.22:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.rotation.y=R()*6.283;
  return {g};
}

/* —— 茅屋：土墙+四棱茅檐+门（合批 1 mesh；隐隐茅堂） —— */
function makeHutXXS(o){
  o=o||{};
  const w=o.w===undefined?4.5:o.w, h=o.h===undefined?2.6:o.h, R=seedRnd(o.seed===undefined?13:o.seed);
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,w*0.8); body.translate(0,h/2,0); B.put(body,shadeColor(0x4a4034,0.9+R()*0.2));
  const roof=new THREE.ConeGeometry(w*0.84,h*0.62,4); roof.rotateY(Math.PI/4); roof.translate(0,h+h*0.28,0);
  B.put(roof,shadeColor(0x6a5a3a,0.85+R()*0.3));
  const door=new THREE.BoxGeometry(w*0.2,h*0.55,0.12); door.translate(0,h*0.28,w*0.4); B.put(door,0x241c12);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2c2c24,emissive:0x0a0806}),{c:o.rimC===undefined?0xc8b478:o.rimC,i:o.rim===undefined?0.24:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.rotation.y=(o.rot===undefined?0:o.rot);
  return {g};
}

/* —— 村墙：一段段矮墙（合批 1 mesh；远远围墙） —— */
function makeWallXXS(o){
  o=o||{};
  const len=o.len===undefined?26:o.len, h=o.h===undefined?1.6:o.h, R=seedRnd(o.seed===undefined?17:o.seed);
  const n=o.n===undefined?10:o.n, B=new GeoBag();
  for(let i=0;i<n;i++){
    const seg=len/n, x=-len/2+seg*(i+0.5), hh=h*(0.85+0.3*R());
    const b=new THREE.BoxGeometry(seg*0.96,hh,0.55); b.translate(x,hh/2,(R()-0.5)*0.3);
    B.put(b,shadeColor(0x5a5348,0.78+0.35*R()));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2a22,emissive:0x080806}),{c:o.rimC===undefined?0xa0c9b8:o.rimC,i:o.rim===undefined?0.15:o.rim,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.rotation.y=(o.rot===undefined?0:o.rot);
  return {g};
}

/* —— 青旗：旗杆+翻飞的青布酒招（飏青旗——村庄的烟火气所在） —— */
function makeBannerXXS(o){
  o=o||{};
  const h=o.h===undefined?6.5:o.h, w=o.w===undefined?2.6:o.w;
  const col=o.color===undefined?0x3f7f62:o.color;
  const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.10,h,7),
    new THREE.MeshPhongMaterial({color:0x3a3026,shininess:6,emissive:0x0a0805}));
  pole.position.y=h/2;
  const fg2=new THREE.PlaneGeometry(w,w*0.42,6,2); fg2.translate(w/2+0.06,0,0);
  const flag=new THREE.Mesh(fg2,new THREE.MeshPhongMaterial({color:col,emissive:0x1c4030,
    emissiveIntensity:0.35,side:THREE.DoubleSide,shininess:12}));
  flag.position.set(0,h-w*0.28,0);
  const g=new THREE.Group(); g.add(pole,flag);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,update:function(t){
    flag.rotation.y=0.30*Math.sin(t*2.6);
    flag.rotation.z=0.06*Math.sin(t*1.9+1.0);
    flag.scale.x=1+0.10*Math.sin(t*3.4);
    flag.scale.y=1+0.05*Math.sin(t*3.4+0.7);
  }};
}

/* —— 小桥：石拱+桥面+矮栏（合批 1 mesh；流水桥旁） —— */
function makeBridgeXXS(o){
  o=o||{};
  const span=o.span===undefined?8:o.span;
  const B=new GeoBag();
  const arch=new THREE.TorusGeometry(span*0.5,0.34,7,18,Math.PI);
  arch.rotateY(Math.PI/2); arch.scale(1,0.42,1); arch.translate(0,0.06,0);
  B.put(arch,shadeColor(0x63625a,0.95));
  const deck=new THREE.BoxGeometry(2.6,0.30,span*1.04); deck.translate(0,span*0.21+0.22,0);
  B.put(deck,shadeColor(0x6e6d62,1.0));
  [1,-1].forEach(function(s){
    const rail=new THREE.BoxGeometry(0.14,0.16,span*0.9); rail.translate(s*1.15,span*0.21+0.64,0);
    B.put(rail,shadeColor(0x5c5b50,0.9));
    [-0.40,0.40].forEach(function(zz){
      const post=new THREE.BoxGeometry(0.14,0.55,0.14); post.translate(s*1.15,span*0.21+0.45,zz*span);
      B.put(post,shadeColor(0x585748,0.9));
    });
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2c2c24,emissive:0x080806}),{c:o.rimC===undefined?0xa0c9b8:o.rimC,i:0.16,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 黄莺：枝头鸣禽（正莺儿啼——末境三忙之一，间歇昂首鸣叫） —— */
function makeOrioleXXS(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0xd8b83a:o.color;
  const g=new THREE.Group();
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.26,8,6); body.scale(1.45,0.95,0.9); body.translate(0,0.28,0); B.put(body,c);
  const head=new THREE.SphereGeometry(0.15,8,6); head.translate(0.44,0.52,0); B.put(head,shadeColor(c,1.12));
  const beak=new THREE.ConeGeometry(0.045,0.20,5); beak.rotateZ(-Math.PI/2); beak.translate(0.63,0.50,0); B.put(beak,0x5a4630);
  const tail=new THREE.ConeGeometry(0.09,0.50,5); tail.rotateZ(Math.PI/2.5); tail.translate(-0.45,0.32,0); B.put(tail,shadeColor(c,0.8));
  const wing=new THREE.PlaneGeometry(0.42,0.24); wing.rotateY(-0.35); wing.translate(-0.02,0.34,0.16); B.put(wing,shadeColor(c,0.88));
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    emissive:0x12100a,side:THREE.DoubleSide}));
  g.add(mesh); g.scale.setScalar(s);
  g.update=function(t,fk2){
    const k=fk2===undefined?1:fk2;
    g.rotation.z=0.04*Math.sin(t*0.8);
    const sing=Math.max(0,Math.sin(t*1.7));
    g.scale.set(s,s*(1+0.10*sing*k),s);
  };
  return {g,update:g.update};
}

/* —— 飞燕：剪影小燕（燕儿舞——单只 1 mesh，路径/倾角由调用方驱动） —— */
function makeSwallowXXS(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.20,7,5); body.scale(1.9,0.7,0.8); B.put(body,0x232c33);
  const head=new THREE.SphereGeometry(0.13,7,5); head.translate(0.34,0.05,0); B.put(head,0x2b3540);
  const wl=new THREE.PlaneGeometry(1.05,0.30); wl.rotateX(-Math.PI/2); wl.rotateZ(0.12); wl.translate(-0.10,0.02,0.55); B.put(wl,0x2b3540);
  const wr=new THREE.PlaneGeometry(1.05,0.30); wr.rotateX(-Math.PI/2); wr.rotateZ(-0.12); wr.translate(-0.10,0.02,-0.55); B.put(wr,0x2b3540);
  const t1=new THREE.ConeGeometry(0.05,0.42,4); t1.rotateZ(Math.PI/2+0.22); t1.translate(-0.52,0.02,0.05); B.put(t1,0x232c33);
  const t2=new THREE.ConeGeometry(0.05,0.42,4); t2.rotateZ(Math.PI/2-0.22); t2.translate(-0.52,0.02,-0.05); B.put(t2,0x232c33);
  const belly=new THREE.SphereGeometry(0.13,6,5); belly.scale(1.5,0.6,0.7); belly.translate(0.06,-0.10,0); B.put(belly,0xe8e8dc);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x3a4450,emissive:0x0a0e14,side:THREE.DoubleSide}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(s);
  return {g};
}

/* —— 粉蝶：双翅开合（蝶儿忙——1 只 2 mesh，翅根在体轴上扇动；路径由调用方驱动） —— */
function makeButterflyXXS(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, c=o.color===undefined?0xe8e0c8:o.color;
  const mat=new THREE.MeshPhongMaterial({color:c,emissive:shadeColor(c,0.4),emissiveIntensity:0.3,
    side:THREE.DoubleSide,shininess:10});
  const wg=new THREE.PlaneGeometry(0.55,0.36); wg.rotateX(-Math.PI/2); wg.translate(0.10,0,0.30);
  const wl=new THREE.Mesh(wg,mat);
  const wr=new THREE.Mesh(wg.clone(),mat); wr.scale.z=-1;
  const g=new THREE.Group(); g.add(wl,wr);
  g.scale.setScalar(s);
  return {g,update:function(t,ph){
    const flap=0.15+0.85*Math.abs(Math.sin(t*10.0+ph));
    wl.rotation.x=-flap*0.9; wr.rotation.x=flap*0.9;
  }};
}

function bCover(){ // 卷首 · 春晓村外 —— 绿树环抱的村庄卧在晨光里，一带陂塘闪着水光
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0c1710,c2:0x17291b,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:3,peaks:5,seed:57,color:0x0c1911,atmo:0x2c4434,fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-85); g.add(ridge.g);
  /* 远村陂塘水光 */
  const water=makeWater({size:12,seg:20,amp:0.08,freq:0.16,speed:0.45,flow:[0.1,0.4],spec:1.1,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-60,90,-160],y:-1.5});
  water.mesh.scale.set(1.3,1,1.5); water.mesh.rotation.y=0.3;
  water.mesh.position.set(-16,-1.5,-32); g.add(water.mesh);
  /* 远村轮廓：茅屋+树环+酒旗一痕 */
  const hut=makeHutXXS({scale:1.0,rot:0.4}); hut.g.position.set(-6,-1.6,-40); g.add(hut.g);
  const tr1=makeTreeXXS({h:7,seed:21,scale:1.3}); tr1.g.position.set(-11,-1.6,-37); g.add(tr1.g);
  const tr2=makeTreeXXS({h:8,seed:23,scale:1.4}); tr2.g.position.set(-1,-1.6,-43); g.add(tr2.g);
  const tr3=makeWillowXXS({h:7,seed:25,scale:1.1}); tr3.g.position.set(7,-1.6,-38); g.add(tr3.g);
  const ban=makeBannerXXS({scale:0.8}); ban.g.position.set(-2.5,-1.6,-44); g.add(ban.g);
  /* 村口一乘兴游人 */
  const walker=makeFigure({pose:'独立',robe:0x2a3830,belt:0x8f6a33,hat:'发髻',scale:1.0,rim:0.4,rimC:0xa0c9b8,noProp:true});
  walker.position.set(1,-1.6,-35); walker.rotation.y=2.7; g.add(walker);
  const crowd=makeCrowd({n:4,rect:[3,-34,16,7],seed:67,color:0x131e14,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  /* 晨曦：东天一抹暖意（青绿底上唯一的暖，随呼吸微明；初值=最大值） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.20,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,60,1); dawn.position.set(70,24,-120); dawn.renderOrder=-7; g.add(dawn);
  const petals=makePetalXXS({n:36,box:[150,22,90],pos:[0,9,-24],fall:0.5,maxA:0.22,c:0xe4ccd6});
  g.add(petals.points);
  const motes=makeGlow({n:34,box:[180,26,100],pos:[0,9,-24],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,30,130],pos:[0,11,-50],scale:78,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:48,n:9,d:7,color:0x081009,seed:19,sway:0.8,rim:0.12,rimC:0xa0c9b8});
  brL.g.position.set(-26,-1.6,42); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:21,rim:0.14,rimC:0xa0c9b8});
  rk.g.position.set(17,-1.4,16); g.add(rk.g);
  addLights(g,{c:0xe8d8a8,i:0.48,p:[50,80,30]},{c:0x22301f,i:0.62});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
    brL.update(t,k); rk.update(t,k); crowd.update(t); walker.update(t,k); ban.update(t);
    tr1.g.rotation.z=Math.sin(t*0.4)*0.008; tr3.g.rotation.z=Math.sin(t*0.5+1.4)*0.010;
    dawn.material.opacity=k*(0.14+0.06*Math.sin(t*0.4));
  }};
}
function bRaodang(){ // 一 · 树绕村庄 —— 绿树绕村，水满陂塘，倚东风豪兴徜徉
  const g=new THREE.Group();
  const ctl={zx:4};
  const grd=makeGround({r:220,c1:0x0a130d,c2:0x162718,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:38,layers:3,peaks:5,seed:71,color:0x09150e,atmo:0x29412e,
    fogK:0.62,glowK:0.04,glow:0xaac890,y:-6});
  ridge.g.position.set(0,0,-92); g.add(ridge.g);
  /* 陂塘：春水涨满的一口大塘（水面+两岸同组） */
  const pond=new THREE.Group();
  const water=makeWater({size:14,seg:24,amp:0.09,freq:0.18,speed:0.5,flow:[0.1,0.5],spec:1.1,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-60,90,-160],y:0.10});
  water.mesh.scale.set(1.3,1,1.5); pond.add(water.mesh);
  const bankB=new GeoBag();
  const b1=new THREE.BoxGeometry(5.6,1.0,30); b1.translate(-11.5,0.28,-1); bankB.put(b1,shadeColor(0x18271c,1.0));
  const b2=new THREE.BoxGeometry(5.0,1.0,26); b2.translate(2.2,0.28,-4); bankB.put(b2,shadeColor(0x1a2a1e,1.0));
  const bankM=bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0xa0c9b8,i:0.14,p:2.4}));
  pond.add(bankM);
  pond.rotation.y=0.22; pond.position.set(-12,0,-5); g.add(pond);
  /* 绕村绿树：垂柳依水，杂树成环 */
  const wl1=makeWillowXXS({h:8,seed:31,scale:1.15}); wl1.g.position.set(-7.5,0,1.5); g.add(wl1.g);
  const wl2=makeWillowXXS({h:7,seed:33,scale:1.0}); wl2.g.position.set(-20,0,-11); g.add(wl2.g);
  const tr1=makeTreeXXS({h:8,seed:35,scale:1.25}); tr1.g.position.set(-3,0,-16); g.add(tr1.g);
  const tr2=makeTreeXXS({h:7,seed:37,scale:1.1}); tr2.g.position.set(6,0,-15); g.add(tr2.g);
  const tr3=makeTreeXXS({h:9,seed:39,scale:1.35}); tr3.g.position.set(-23,0,-2); g.add(tr3.g);
  const tr4=makeTreeXXS({h:7.5,seed:41,scale:1.15}); tr4.g.position.set(13,0,-9); g.add(tr4.g);
  const tr5=makeTreeXXS({h:8.5,seed:43,scale:1.3}); tr5.g.position.set(11,0,-21); g.add(tr5.g);
  /* 村舍两三，半隐树间 */
  const hut1=makeHutXXS({scale:1.1,rot:0.35}); hut1.g.position.set(0,0,-24); g.add(hut1.g);
  const hut2=makeHutXXS({scale:0.85,rot:-0.5}); hut2.g.position.set(9,0,-20); g.add(hut2.g);
  /* 村径：沿塘而行的沙路 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.08,42),
    new THREE.MeshPhongMaterial({color:0x83816a,shininess:4,emissive:0x12120c}));
  path.rotation.y=-0.28; path.position.set(3.4,0.05,1); g.add(path);
  /* 乘兴漫步人：倚东风沿村径徜徉（缓步往返） */
  const walker=makeFigure({pose:'独立',robe:0x2a3830,belt:0x8f6a33,hat:'发髻',scale:1.12,rim:0.45,rimC:0xa0c9b8,noProp:true});
  walker.position.set(2.6,0,ctl.zx); walker.rotation.y=Math.PI+0.15; g.add(walker);
  const crowd=makeCrowd({n:3,rect:[2,-28,14,7],seed:77,color:0x121c13,rimC:0x8fae78,rim:0.2});
  g.add(crowd.mesh);
  const petals=makePetalXXS({n:46,box:[100,16,60],pos:[0,8,-4],fall:0.55,maxA:0.28});
  g.add(petals.points);
  const motes=makeGlow({n:28,box:[130,20,70],pos:[0,8,-14],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[210,26,110],pos:[0,9,-44],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:10,d:5,color:0x071009,seed:45,sway:1.2,tip:0x2c4028});
  reed.g.position.set(-12,-0.8,14); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:15,d:6,color:0x060c08,seed:47,rim:0.12,rimC:0xa0c9b8});
  rk.g.position.set(14,-1.2,13); g.add(rk.g);
  addLights(g,{c:0xd8c890,i:0.5,p:[45,75,25]},{c:0x1c2a1e,i:0.64});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
    reed.update(t,k); rk.update(t,k); crowd.update(t); walker.update(t,k);
    walker.position.z=ctl.zx+6.5*Math.sin(t*0.075);
    walker.position.y=Math.abs(Math.sin(t*2.1))*0.07;
    wl1.g.rotation.z=Math.sin(t*0.5)*0.012; wl2.g.rotation.z=Math.sin(t*0.44+2.0)*0.010;
    tr1.g.rotation.z=Math.sin(t*0.36+1.0)*0.007;
  }};
}
function bChunguang(){ // 二 · 收尽春光 —— 小园几许，桃花红李花白菜花黄，入园三色次第点亮（标志性瞬间）
  const g=new THREE.Group();
  const ctl={T:0};
  const grd=makeGround({r:210,c1:0x0a130d,c2:0x172919,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:225,h:36,layers:3,peaks:5,seed:73,color:0x09150e,atmo:0x2b4430,
    fogK:0.62,glowK:0.04,glow:0xb0cc92,y:-6});
  ridge.g.position.set(0,0,-88); g.add(ridge.g);
  /* 小园篱墙：背墙+侧墙，前口留门 */
  const wall1=makeWallXXS({len:20,h:1.25,seed:51}); wall1.g.position.set(-8,0,-20.5); g.add(wall1.g);
  const wall2=makeWallXXS({len:12,h:1.2,seed:53}); wall2.g.rotation.y=Math.PI/2; wall2.g.position.set(-17.8,0,-14); g.add(wall2.g);
  /* 三色花田：红(桃)→白(李)→黄(菜花)，入园次第点亮（红左、白中、黄右前，互不遮挡） */
  const fRed=makeFlowerFieldXXS({n:120,w:6.2,d:4.6,color:0xd05242,seed:61});
  fRed.g.position.set(-14.2,0,-13.2); g.add(fRed.g);
  const fWhite=makeFlowerFieldXXS({n:105,w:5.6,d:4.6,color:0xe8ecf2,seed:63});
  fWhite.g.position.set(-9.0,0,-15.2); g.add(fWhite.g);
  const fYellow=makeFlowerFieldXXS({n:170,w:6.2,d:4.6,color:0xe6c445,seed:65});
  fYellow.g.position.set(-3.2,0,-13.0); g.add(fYellow.g);
  /* 桃李成树，菜花铺地：花树立于花田后侧，不挡花田 */
  const peach1=makeTreeXXS({h:5.6,seed:81,leaf:0xea8fa4,blobs:4,scale:1.1}); peach1.g.position.set(-16.4,0,-16.2); g.add(peach1.g);
  const peach2=makeTreeXXS({h:4.8,seed:83,leaf:0xe8808e,blobs:3,scale:0.95}); peach2.g.position.set(-12.6,0,-17.4); g.add(peach2.g);
  const plum1=makeTreeXXS({h:5.4,seed:85,leaf:0xeef2f6,blobs:4,scale:1.05}); plum1.g.position.set(-7.6,0,-18.8); g.add(plum1.g);
  const wl1=makeWillowXXS({h:7,seed:87,scale:1.0}); wl1.g.position.set(-16.2,0,-10.8); g.add(wl1.g);
  const tr1=makeTreeXXS({h:7,seed:89,scale:1.1}); tr1.g.position.set(2.6,0,-17); g.add(tr1.g);
  /* 园径与乘兴漫步人：正跨进院门 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.0,0.08,26),
    new THREE.MeshPhongMaterial({color:0x83816a,shininess:4,emissive:0x12120c}));
  path.rotation.y=-0.55; path.position.set(2.2,0.05,-8); g.add(path);
  const walker=makeFigure({pose:'独立',robe:0x2a3830,belt:0x8f6a33,hat:'发髻',scale:1.1,rim:0.45,rimC:0xa0c9b8,noProp:true});
  walker.position.set(1.2,0,-8.6); walker.rotation.y=Math.PI-0.5; g.add(walker);
  const crowd=makeCrowd({n:2,rect:[-6,-24,10,5],seed:79,color:0x121c13,rimC:0x8fae78,rim:0.18});
  g.add(crowd.mesh);
  const petals=makePetalXXS({n:64,box:[90,16,52],pos:[-4,8,-12],fall:0.6,sway:1.5,maxA:0.34});
  g.add(petals.points);
  const motes=makeGlow({n:30,box:[110,18,60],pos:[-4,7,-14],color:0xd8e8b8,size:6,speed:0.045,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[190,24,100],pos:[0,9,-42],scale:68,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x060c08,seed:91,rim:0.12,rimC:0xa0c9b8});
  rk.g.position.set(12,-1.2,13); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:14,n:8,d:5,color:0x071009,seed:93,sway:1.1,tip:0x2c4028});
  reed.g.position.set(-14,-0.8,14); g.add(reed.g);
  addLights(g,{c:0xe0d090,i:0.52,p:[40,75,25]},{c:0x1e2c1e,i:0.66});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ctl.T+=dt;
    ridge.update(t,0); mist.update(t,k); motes.update(t); petals.update(t);
    rk.update(t,k); reed.update(t,k); crowd.update(t); walker.update(t,k);
    /* 三色次第点亮：红→白→黄，每色 1.5s 缓起（uFade/opacity 均乘 fadeK） */
    const seq=[0.6,2.2,3.8];
    const fs=[fRed,fWhite,fYellow];
    for(let i=0;i<3;i++){
      let u=(ctl.T-seq[i])/1.5; u=u<0?0:(u>1?1:u); u=u*u*(3-2*u);
      fs[i].update(t,u,k);
    }
    peach1.g.rotation.z=Math.sin(t*0.42)*0.010; plum1.g.rotation.z=Math.sin(t*0.38+1.6)*0.009;
    walker.position.z=-8.6+1.6*Math.sin(t*0.06+1);
    walker.position.y=Math.abs(Math.sin(t*2.0+0.6))*0.06;
  }};
}
function bQingqi(){ // 三 · 青旗流水 —— 远远围墙隐隐茅堂，飏青旗流水桥旁
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0x0a130d,c2:0x162718,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:36,layers:2,peaks:4,seed:75,color:0x091409,atmo:0x27402c,
    fogK:0.60,glowK:0.05,glow:0x9ab888,y:-8});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 流水：斜过画面的村溪（水面+两岸同组） */
  const stream=new THREE.Group();
  const water=makeWater({size:13,seg:24,amp:0.09,freq:0.18,speed:0.55,flow:[0.1,0.6],spec:1.15,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-60,90,-160],y:0.10});
  water.mesh.scale.set(1,1,10); stream.add(water.mesh);
  const bankB=new GeoBag();
  const bl=new THREE.BoxGeometry(4.6,1.0,150); bl.translate(-6.8,0.30,0); bankB.put(bl,shadeColor(0x18271c,1.0));
  const br=new THREE.BoxGeometry(4.6,1.0,150); br.translate(6.8,0.30,0); bankB.put(br,shadeColor(0x1a2a1e,1.0));
  const bankM=bankB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0xa0c9b8,i:0.14,p:2.4}));
  stream.add(bankM);
  stream.rotation.y=0.5; stream.position.set(-2,0,-5); g.add(stream);
  /* 小桥跨溪 */
  const bridge=makeBridgeXXS({span:8,scale:1.0});
  bridge.g.position.set(-4.2,0,-8.6); bridge.g.rotation.y=0.5+Math.PI/2; g.add(bridge.g);
  /* 围墙+茅堂+青旗：对岸村家 */
  const wall=makeWallXXS({len:24,h:1.8,seed:55,rot:-0.12}); wall.g.position.set(-8,0,-19); g.add(wall.g);
  const hut1=makeHutXXS({scale:1.2,rot:0.3}); hut1.g.position.set(-11,0,-23.5); g.add(hut1.g);
  const hut2=makeHutXXS({scale:0.8,rot:-0.4}); hut2.g.position.set(-1.5,0,-24); g.add(hut2.g);
  const ban=makeBannerXXS({h:7,scale:1.0}); ban.g.position.set(-5.5,0,-21.5); g.add(ban.g);
  /* 岸树夹溪 */
  const wl1=makeWillowXXS({h:7.5,seed:57,scale:1.1}); wl1.g.position.set(-15,0,-13); g.add(wl1.g);
  const wl2=makeWillowXXS({h:6.5,seed:59,scale:0.95}); wl2.g.position.set(9,0,-2); g.add(wl2.g);
  const tr1=makeTreeXXS({h:7.5,seed:95,scale:1.15}); tr1.g.position.set(3,0,-18); g.add(tr1.g);
  const tr2=makeTreeXXS({h:8,seed:97,scale:1.2}); tr2.g.position.set(-19,0,-23); g.add(tr2.g);
  /* 乘兴漫步人：正走向小桥 */
  const walker=makeFigure({pose:'独立',robe:0x2a3830,belt:0x8f6a33,hat:'发髻',scale:1.1,rim:0.45,rimC:0xa0c9b8,noProp:true});
  walker.position.set(2.4,0,0.5); walker.rotation.y=2.6; g.add(walker);
  const crowd=makeCrowd({n:2,rect:[-10,-22,8,5],seed:81,color:0x121c13,rimC:0x8fae78,rim:0.18});
  g.add(crowd.mesh);
  const petals=makePetalXXS({n:40,box:[100,15,58],pos:[0,8,-8],fall:0.55,maxA:0.26});
  g.add(petals.points);
  const motes=makeGlow({n:26,box:[130,18,70],pos:[0,8,-16],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[210,24,110],pos:[0,9,-46],scale:70,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:16,n:9,d:5,color:0x071009,seed:99,sway:1.3,tip:0x2c4028});
  reed.g.position.set(12,-0.8,13); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x060c08,seed:101,rim:0.12,rimC:0xa0c9b8});
  rk.g.position.set(-14,-1.2,12); g.add(rk.g);
  addLights(g,{c:0xd8c88a,i:0.5,p:[40,75,25]},{c:0x1c2a1e,i:0.64});
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
    reed.update(t,k); rk.update(t,k); crowd.update(t); walker.update(t,k); ban.update(t);
    walker.position.z=0.5-2.6*(0.5+0.5*Math.sin(t*0.06));
    walker.position.y=Math.abs(Math.sin(t*2.05+0.3))*0.06;
    wl1.g.rotation.z=Math.sin(t*0.48)*0.012; wl2.g.rotation.z=Math.sin(t*0.52+1.2)*0.011;
  }};
}
function bDonggang(){ // 四（末境·可点击）· 莺燕蝶忙 —— 步过东冈回望村庄；点击：三色花田次第点亮，满眼春光
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,seq:99,pulse:0};
  const grd=makeGround({r:230,c1:0x0a130d,c2:0x172919,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:36,layers:3,peaks:5,seed:83,color:0x09150e,atmo:0x2b4430,
    fogK:0.62,glowK:0.05,glow:0xb0cc92,y:-8});
  ridge.g.position.set(0,0,-98); g.add(ridge.g);
  /* 东冈：土冈一座，人立冈上回望村庄 */
  const moundB=new GeoBag();
  const mound=new THREE.CylinderGeometry(3.2,7.5,2.8,10); mound.translate(0,1.4,0);
  moundB.put(mound,shadeColor(0x22301c,1.0));
  for(let i=0;i<5;i++){
    const a=i*1.26+0.4, rr2=6.0+i*0.2;
    const rock=new THREE.SphereGeometry(0.8+((i*37)%10)*0.08,7,5);
    rock.scale(1,0.6,1); rock.translate(Math.cos(a)*rr2,0.25,Math.sin(a)*rr2);
    moundB.put(rock,shadeColor(0x2a3822,0.85+i*0.05));
  }
  const moundM=moundB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0xa0c9b8,i:0.14,p:2.4}));
  moundM.position.set(6.8,0,11.5); g.add(moundM);
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.2,0.08,20),
    new THREE.MeshPhongMaterial({color:0x83816a,shininess:4,emissive:0x12120c}));
  path.rotation.y=0.55; path.position.set(5,0.05,16.5); g.add(path);
  /* 乘兴漫步人：冈顶驻足回望（乘兴步过东冈） */
  const walker=makeFigure({pose:'独立',robe:0x2a3830,belt:0x8f6a33,hat:'发髻',scale:1.06,rim:0.5,rimC:0xa0c9b8,noProp:true});
  walker.position.set(6.8,2.8,11.1); walker.rotation.y=-2.0; g.add(walker);
  /* 回望里的村庄：陂塘+三色花田+围墙茅堂青旗 */
  const water=makeWater({size:11,seg:20,amp:0.08,freq:0.16,speed:0.5,flow:[0.1,0.5],spec:1.1,
    deep:0x0a1a14,shallow:0x1d4836,skyc:0x2c5844,moonDir:[-60,90,-160],y:0.08});
  water.mesh.scale.set(1.2,1,1.3); water.mesh.rotation.y=0.3;
  water.mesh.position.set(-18,0.08,-4); g.add(water.mesh);
  const fRed=makeFlowerFieldXXS({n:110,w:7.0,d:5.0,color:0xd05242,seed:63});
  fRed.g.position.set(-19,0,-12); g.add(fRed.g);
  const fWhite=makeFlowerFieldXXS({n:95,w:6.0,d:4.8,color:0xe8ecf2,seed:65});
  fWhite.g.position.set(-11.5,0,-15); g.add(fWhite.g);
  const fYellow=makeFlowerFieldXXS({n:160,w:7.5,d:4.8,color:0xe6c445,seed:67});
  fYellow.g.position.set(-3.5,0,-11.5); g.add(fYellow.g);
  const peach1=makeTreeXXS({h:5.6,seed:103,leaf:0xea8fa4,blobs:4,scale:1.1}); peach1.g.position.set(-21.5,0,-9.5); g.add(peach1.g);
  const peach2=makeTreeXXS({h:4.8,seed:105,leaf:0xe8808e,blobs:3,scale:0.9}); peach2.g.position.set(-16.5,0,-14.5); g.add(peach2.g);
  const plum1=makeTreeXXS({h:5.2,seed:107,leaf:0xeef2f6,blobs:4,scale:1.0}); plum1.g.position.set(-9,0,-17.5); g.add(plum1.g);
  const wl1=makeWillowXXS({h:7,seed:109,scale:1.05}); wl1.g.position.set(-23,0,-4); g.add(wl1.g);
  const tr1=makeTreeXXS({h:7,seed:111,scale:1.1}); tr1.g.position.set(2,0,-17); g.add(tr1.g);
  const tr2=makeTreeXXS({h:7.5,seed:113,scale:1.1}); tr2.g.position.set(-15,0,-6.5); g.add(tr2.g);
  const wall=makeWallXXS({len:18,h:1.7,seed:114,rot:0.12}); wall.g.position.set(-6,0,-20.5); g.add(wall.g);
  const hut1=makeHutXXS({scale:1.15,rot:0.3}); hut1.g.position.set(-7.5,0,-24); g.add(hut1.g);
  const ban=makeBannerXXS({h:6.5,scale:1.0}); ban.g.position.set(-2.5,0,-21.5); g.add(ban.g);
  const crowd=makeCrowd({n:2,rect:[-8,-20,10,5],seed:84,color:0x121c13,rimC:0x8fae78,rim:0.18});
  g.add(crowd.mesh);
  /* 冈边一树横枝：黄莺昂首（莺儿啼） */
  const tree=makeTreeXXS({h:7.5,seed:115,branch:[-2.2,2.4,1.0],scale:1.15}); tree.g.position.set(14.5,0,4); g.add(tree.g);
  const oriole=makeOrioleXXS({scale:1.15});
  oriole.g.position.set(12.6,6.0,5.1); oriole.g.rotation.y=-0.8; g.add(oriole.g);
  /* 双燕掠空（燕儿舞）：椭圆回旋，倾身转向 */
  const swallows=[];
  [[13,0.50,0.0],[10.5,0.38,2.4]].forEach(function(cfg,i){
    const sw=makeSwallowXXS({scale:1.0-i*0.15});
    g.add(sw.g); swallows.push({sw,rx:cfg[0],sp:cfg[1],ph:cfg[2]});
  });
  /* 三蝶穿花（蝶儿忙）：花田间 8 字游丝 */
  const butterflies=[];
  [[-17,2.4,-11,0xe8e2cc,0.0],[-10.5,2.7,-14,0xd8e4f0,2.1],[-2.5,2.3,-10.5,0xf0d890,4.2]].forEach(function(cfg){
    const bf=makeButterflyXXS({color:cfg[3],scale:0.9});
    g.add(bf.g); butterflies.push({bf,cx:cfg[0],cy:cfg[1],cz:cfg[2],ph:cfg[4]});
  });
  /* 春光辉光：点击点亮时暖一拍（初值=最大值） */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8d8a0,
    transparent:true,opacity:0.26,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(130,50,1); glow.position.set(-30,18,-70); glow.renderOrder=-7; g.add(glow);
  const petals=makePetalXXS({n:44,box:[130,18,80],pos:[-6,8,-10],fall:0.55,maxA:0.28});
  g.add(petals.points);
  const motes=makeGlow({n:28,box:[150,20,80],pos:[0,8,-14],color:0xd8e8b8,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[220,26,115],pos:[0,9,-50],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x060b07,seed:121,rim:0.12,rimC:0xa0c9b8});
  rk.g.position.set(14,-1.2,15); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:12,n:7,d:5,color:0x071009,seed:123,sway:1.2,tip:0x2c4028});
  reed.g.position.set(-14,-1.0,17); g.add(reed.g);
  addLights(g,{c:0xdcc98a,i:0.5,p:[35,80,30]},{c:0x1e2c1e,i:0.66});
  const fields=[fRed,fWhite,fYellow];
  const api={group:g,clicked:false,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked&&ctl.seq<6)ctl.seq+=dt;
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.0);
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
      rk.update(t,k); reed.update(t,k); crowd.update(t); walker.update(t,k); ban.update(t);
      oriole.update(t,k);
      walker.position.y=2.8+0.03*Math.sin(t*1.1);
      /* 三色花田：未点前敛艳（0.3），点击后红→白→黄次第满开 */
      for(let i=0;i<3;i++){
        let u=0;
        if(ctl.clicked){ u=(ctl.seq-i*0.9)/1.3; u=u<0?0:(u>1?1:u); u=u*u*(3-2*u); }
        fields[i].update(t,0.30+0.70*u,k);
      }
      /* 双燕：回旋+倾身（朝向沿切线） */
      for(let i=0;i<swallows.length;i++){
        const s=swallows[i], a=t*s.sp+s.ph;
        s.sw.g.position.set(-5+s.rx*Math.cos(a),9.0+1.4*Math.sin(t*0.9+s.ph),-7+6.5*Math.sin(a));
        s.sw.g.rotation.y=Math.atan2(-6.5*Math.cos(a),-s.rx*Math.sin(a));
        s.sw.g.rotation.z=0.38*Math.cos(a);
        s.sw.g.rotation.x=0.10*Math.sin(t*2.0+i);
      }
      /* 三蝶：8 字游丝+扇翅 */
      for(let i=0;i<butterflies.length;i++){
        const b=butterflies[i], u=t*0.7+b.ph;
        b.bf.g.position.set(b.cx+1.7*Math.sin(u),b.cy+0.5*Math.sin(t*1.3+b.ph),b.cz+1.1*Math.sin(2*u)*0.6);
        b.bf.g.rotation.y=u*0.6;
        b.bf.update(t,b.ph);
      }
      glow.material.opacity=k*(0.14+0.12*ctl.pulse);
      tree.g.rotation.z=Math.sin(t*0.4)*0.008; peach1.g.rotation.z=Math.sin(t*0.4+1.2)*0.009;
    },click(){
      if(ctl.t<1.4)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.14); pluck(2,0.35,0.12); pluck(4,0.8,0.11); pluck(5,1.35,0.10);
      }else{
        pluck(4,0,0.12); pluck(5,0.4,0.10); pluck(3,0.85,0.09);
      }
      ctl.seq=0; ctl.pulse=1;                 // 可反复点：三色再满开一轮
      const fl=$('#flash'); fl.textContent='桃花红 · 李花白 · 菜花黄'; fl.classList.remove('go');
      void fl.offsetWidth; fl.classList.add('go');
    },onEnter(){
      pluck(5,0.15,0.07); pluck(4,0.55,0.06); pluck(5,1.0,0.05);   // 冈上莺声
    }};
  return api;
}
