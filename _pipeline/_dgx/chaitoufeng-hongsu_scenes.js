/* ================= 钗头凤·红酥手 · 四境场景（烟雨江南·沈园本事词：黛蓝湿雾、宫墙垂柳、桃花独暖） =================
   美术立意：全页禁金，黛蓝湿雾 #8fb3c9 系主调、accent=#a8a0c0（淡藤紫）用于题字辉光/人物边缘光；
   桃花红是全页唯一暖点。上下片对称回环：红酥手/春如旧、宫墙柳/人空瘦——境①与境③同景异时。
   标志性瞬间「宫墙柳」：满城春色而人隔宫墙——近在咫尺的咫尺天涯。
   末境点击（queue interact）：点击宫墙柳——柳絮拂壁，「错、错、错」「莫、莫、莫」题字次第浮现（双调回环）。 */

/* —— 落英：桃瓣缓落自写小着色器（uFade 交给 setFade，带东风斜飘）—— */
const CTF_FALL_VERT=`attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float h=mod(uTime*uSpeed*(0.5+aSeed*0.9)+aSeed*97.31, uBox.y);
  p.y-=h;
  p.x+=sin(uTime*0.8+aSeed*40.0)*1.1+h*0.18;
  p.z+=cos(uTime*0.6+aSeed*27.0)*0.9;
  float f=1.0-h/uBox.y;
  vA=smoothstep(0.0,0.12,f)*smoothstep(1.0,0.78,f);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
/* —— 柳絮：向宫墙拂去的小着色器（末境点击后大盛）—— */
const CTF_XU_VERT=`attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float h=mod(uTime*uSpeed*(0.5+aSeed*0.9)+aSeed*57.31, uBox.z);
  p.z-=h;
  p.y+=sin(uTime*0.5+aSeed*41.0)*0.9+h*0.06;
  p.x+=sin(uTime*0.8+aSeed*23.0)*1.3;
  float f=h/uBox.z;
  vA=smoothstep(0.0,0.10,f)*smoothstep(1.0,0.70,f);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeLuoying(o){ // 落英（NormalBlending 桃瓣）
  o=o||{};
  const n=o.n===undefined?110:o.n, box=o.box||[46,13,26], pos=o.pos||[0,9,-2];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?3.5:o.size)*(0.7+Math.random()*0.7);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.85:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0xc98a96:o.color)},uFade:{value:0},
      uMaxA:{value:o.maxA===undefined?0.28:o.maxA}},
    vertexShader:CTF_FALL_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}
function makeXusu(o){ // 柳絮（拂向宫墙）
  o=o||{};
  const n=o.n===undefined?120:o.n, box=o.box||[54,9,12], pos=o.pos||[2,5,-1.5];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?3.4:o.size)*(0.7+Math.random()*0.7);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.8:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0xdde2ec:o.color)},uFade:{value:0},
      uMaxA:{value:o.maxA===undefined?0.14:o.maxA}},
    vertexShader:CTF_XU_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 宫墙：灰砖墙身 + 墙帽两道 + 墙根收边（合批 1 mesh）——满城春色隔在墙外 */
function makeGongqiang(o){
  o=o||{};
  const w=o.w===undefined?70:o.w, h=o.h===undefined?5.0:o.h;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,0.9); body.translate(0,h/2,0); B.put(body,0x2b3442);
  const cap1=new THREE.BoxGeometry(w+0.4,0.4,1.3); cap1.translate(0,h+0.2,0); B.put(cap1,0x3a4452);
  const cap2=new THREE.BoxGeometry(w+0.8,0.16,1.7); cap2.translate(0,h+0.48,0); B.put(cap2,0x465060);
  const foot=new THREE.BoxGeometry(w+0.2,0.55,1.2); foot.translate(0,0.27,0); B.put(foot,0x1f2630);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3442,emissive:0x0a0d14}),{c:0xa8a0c0,i:o.rim===undefined?0.3:o.rim,p:2.8})));
  return g;
}

/* —— 垂柳：曲干 + 冠团（Phong 合批 1 mesh）+ 垂丝（摆动着色器 1 mesh，越向梢端摆幅越大）—— */
const CTF_WL_VERT=`
uniform float uTime; uniform float uSway; uniform float uRefY;
void main(){
  vec3 p=position;
  float k=clamp((uRefY-p.y)*0.22,0.0,1.0);
  float ph=p.x*2.3+p.z*1.7;
  p.x+=sin(uTime*0.7+ph)*uSway*k;
  p.z+=cos(uTime*0.55+ph*1.4)*uSway*0.5*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const CTF_WL_FRAG=`uniform vec3 uC; uniform float uFade;
void main(){ gl_FragColor=vec4(uC,uFade); }`;
function makeChuiliu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1950:o.seed);
  const h=o.h===undefined?7.5:o.h, n=o.n===undefined?13:o.n, sway=o.sway===undefined?0.6:o.sway;
  const lean=o.lean===undefined?0.15:o.lean;
  const B=new GeoBag();
  let tx=0;
  for(let i=0;i<3;i++){
    const r0=0.23*(1-i*0.24), r1=0.23*(1-(i+1)*0.24);
    const seg=new THREE.CylinderGeometry(Math.max(r1,0.06),Math.max(r0,0.09),h/3,7);
    seg.rotateZ(lean*(i*0.7)); seg.translate(tx,h*(i+0.5)/3,0);
    B.put(seg,0x1b1611);
    tx+=Math.tan(lean*(i*0.7+0.35))*h/3*0.55;
  }
  for(let i=0;i<3;i++){
    const cp=new THREE.SphereGeometry(1.5+R()*1.0,8,6);
    cp.scale(1.3,0.48,1.1); cp.translate(tx+(R()-0.5)*2.6,h+(R()-0.2)*1.4,(R()-0.5)*2.2);
    B.put(cp,0x121a16);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3a38,emissive:0x040806}),{c:0x8fa8bc,i:0.22,p:2.6})));
  /* 垂丝：4 节细管链，自冠顶垂落（柳拂墙头） */
  const SB=new GeoBag();
  for(let i=0;i<n;i++){
    const sx=tx+(R()-0.5)*5.0, sz=(R()-0.5)*3.4;
    const top=h+(R()-0.5)*1.6, len=2.8+R()*3.8, drift=(R()-0.5)*0.5;
    for(let k=0;k<4;k++){
      const y0=top-len*k/4, y1=top-len*(k+1)/4;
      const st=new THREE.CylinderGeometry(0.014,0.02,Math.abs(y1-y0)*1.06,4,1,true);
      st.translate(sx+drift*k/3,(y0+y1)/2,sz+drift*0.4*k/3);
      SB.put(st,0x20302a);
    }
  }
  const sm=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:sway},uRefY:{value:h-0.8},
      uC:{value:C(0x20302a)},uFade:{value:1}},
    vertexShader:CTF_WL_VERT,fragmentShader:CTF_WL_FRAG});
  const strands=new THREE.Mesh(mergeGeos(SB.list),sm);
  strands.frustumCulled=false; g.add(strands);
  const api={g,update(t,k){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    sm.uniforms.uTime.value=t; }};
  g.userData.update=api.update;
  return api;
}

/* —— 桃树：曲干 + 花冠（暗桃红几团 + 亮桃红数簇）——全页唯一暖点 */
function makeTaoshu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19501:o.seed);
  const h=o.h===undefined?4.0:o.h;
  const B=new GeoBag();
  const tr=new THREE.CylinderGeometry(0.10,0.18,h,6); tr.rotateZ((R()-0.5)*0.3); tr.translate(0,h/2,0);
  B.put(tr,0x1a1410);
  for(let i=0;i<3;i++){
    const br=new THREE.CylinderGeometry(0.035,0.07,h*0.45,5);
    br.rotateZ((R()<0.5?1:-1)*(0.7+R()*0.5)); br.rotateY(R()*6.28);
    br.translate(0,h*0.62,0); B.put(br,0x171210);
  }
  for(let i=0;i<4;i++){
    const cp=new THREE.SphereGeometry(0.75+R()*0.5,8,6);
    cp.scale(1.25,0.55,1.1);
    cp.translate((R()-0.5)*1.6,h*0.92+(R()-0.3)*0.9,(R()-0.5)*1.3);
    B.put(cp,0x6e3a44);
  }
  for(let i=0;i<3;i++){
    const cp=new THREE.SphereGeometry(0.34+R()*0.2,8,6);
    cp.scale(1.2,0.5,1.0);
    cp.translate((R()-0.5)*1.7,h*1.02+(R()+0.1)*0.8,(R()-0.5)*1.4);
    B.put(cp,0xa8556a);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2a30,emissive:0x0a0508}),{c:0xa8a0c0,i:o.rim===undefined?0.14:o.rim,p:2.6})));
  return g;
}

/* —— 池阁：石台 + 四柱 + 攒尖小顶（合批 1 mesh）——闲池阁，无人无灯 */
function makeChige(o){
  o=o||{};
  const w=o.w===undefined?5.5:o.w, h=o.h===undefined?3.4:o.h;
  const col=o.color===undefined?0x1a222c:o.color;
  const B=new GeoBag();
  const tai=new THREE.BoxGeometry(w+1.6,0.5,w+1.6); tai.translate(0,0.5,0); B.put(tai,0x141a22);
  const tai2=new THREE.BoxGeometry(w+1.9,0.18,w+1.9); tai2.translate(0,0.84,0); B.put(tai2,shadeColor(col,1.15));
  for(const sx of [-1,1]) for(const sz of [-1,1]){
    const leg=new THREE.CylinderGeometry(0.11,0.13,1.4,6); leg.translate(sx*w/2,-0.35,sz*w/2); B.put(leg,0x10151c);
    const pl=new THREE.CylinderGeometry(0.13,0.16,h,7); pl.translate(sx*w/2,h/2+0.9,sz*w/2); B.put(pl,col);
  }
  const beam=new THREE.BoxGeometry(w*1.12,0.24,w*1.12); beam.translate(0,h+0.9,0); B.put(beam,shadeColor(col,0.9));
  const roof1=new THREE.ConeGeometry(w*0.92,1.4,4); roof1.rotateY(Math.PI/4); roof1.translate(0,h+1.8,0); B.put(roof1,shadeColor(col,1.1));
  const roof2=new THREE.ConeGeometry(w*0.5,0.9,4); roof2.rotateY(Math.PI/4); roof2.translate(0,h+2.8,0); B.put(roof2,shadeColor(col,1.25));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2c3442,emissive:0x05070c}),{c:0xa8a0c0,i:o.rim===undefined?0.2:o.rim,p:2.6})));
  return g;
}

/* —— 壁上题字：右「错、错、错」左「莫、莫、莫」（canvas 题字，fog:false；次第浮现交给 lvl）—— */
function ctfBiwenTex(chars){
  const c=document.createElement('canvas'); c.width=960; c.height=320;
  const x=c.getContext('2d');
  x.font='160px "Ma Shan Zheng","Kaiti SC","STKaiti","KaiTi","Noto Serif SC",serif';
  x.textAlign='center'; x.textBaseline='middle';
  x.shadowColor='rgba(168,160,192,.85)'; x.shadowBlur=20;
  x.fillStyle='#e9e6f2';
  x.fillText(chars,480,168);
  return new THREE.CanvasTexture(c);
}
function makeBiwen(o){
  o=o||{};
  const matC=new THREE.MeshBasicMaterial({map:ctfBiwenTex('错、错、错'),transparent:true,
    opacity:0.95,depthWrite:false,fog:false});
  const matM=new THREE.MeshBasicMaterial({map:ctfBiwenTex('莫、莫、莫'),transparent:true,
    opacity:0.95,depthWrite:false,fog:false});
  const w=o.w===undefined?7.8:o.w, h=w*320/960;
  const pc=new THREE.Mesh(new THREE.PlaneGeometry(w,h),matC);
  pc.position.set(2.9,3.1,0.5); pc.renderOrder=6; pc.frustumCulled=false;
  const pm=new THREE.Mesh(new THREE.PlaneGeometry(w,h),matM);
  pm.position.set(-4.4,2.6,0.5); pm.renderOrder=6; pm.frustumCulled=false;
  const g=new THREE.Group(); g.add(pc); g.add(pm);
  return {g,update(t,k,lvC,lvM){ const kk=k===undefined?1:k;
    matC.opacity=kk*0.95*(lvC===undefined?0:lvC);
    matM.opacity=kk*0.95*(lvM===undefined?0:lvM);
    pc.position.y=3.1+0.06*Math.sin(t*0.4);
    pm.position.y=2.6+0.05*Math.sin(t*0.34+1.3);
  }};
}

const CTF_MOMENT='错、错、错 —— 莫、莫、莫';

function bCoverShen(){ // 封面 · 烟雨沈园（宫墙一角、垂柳拂墙、池塘雾气、重游人影）
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:88,amp:0.4,freq:0.09,speed:0.45,flow:[0,0.35],
    deep:0x0a121c,shallow:0x16283a,skyc:0x22303e,spec:0.6,y:-1.7});
  g.add(water.mesh);
  const ground=makeGround({r:60,c1:0x0c1016,c2:0x141a24});
  ground.mesh.position.set(0,-0.1,26); g.add(ground.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:1951,color:0x0a0e15,atmo:0x36445a,fogK:0.66,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,6); g.add(ridge.g);
  const wall=makeGongqiang({w:72,h:4.6}); wall.position.set(0,0,-24); g.add(wall);
  const wl1=makeChuiliu({h:7.6,seed:1953,n:13,sway:0.55}); wl1.g.position.set(-13,-0.1,-21); g.add(wl1.g);
  const wl2=makeChuiliu({h:6.4,seed:1955,n:11,sway:0.5}); wl2.g.position.set(14,-0.1,-22); g.add(wl2.g);
  const tao=makeTaoshu({seed:1957,h:3.6}); tao.position.set(6,-0.1,-19.5); g.add(tao);
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.05,rim:0.5,rimC:0xa8a0c0});
  poet.position.set(-4,-0.1,-14); poet.rotation.y=0.4; g.add(poet);
  const xu=makeXusu({n:90,box:[52,8,10],pos:[0,4.5,-11],color:0xd8dde8,size:3.2,speed:0.55,maxA:0.16});
  g.add(xu.points);
  const mist=makeMist({n:8,spread:[220,24,110],pos:[0,8,-38],scale:76,color:0x8b9ab4,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',w:26,n:7,d:5,color:0x0b0f14,seed:1959,sway:0.85,tip:0x24303a});
  fg.g.position.set(-16,-1.4,16); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:13,d:6,color:0x080b10,seed:1961,rim:0.12});
  rk.g.position.set(20,-1.4,12); g.add(rk.g);
  addLights(g,{c:0x93a8c2,i:0.32,p:[-40,70,40]},{c:0x24303e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); xu.update(t);
    wl1.update(t,k); wl2.update(t,k); fg.update(t,k); rk.update(t,k); poet.update(t,k);
  }};
}
function bChunyan(){ // 一（标志性瞬间）· 宫墙柳 —— 红酥手黄縢酒，满城春色宫墙柳：园中对饮，柳拂墙头，咫尺天涯
  const g=new THREE.Group();
  const water=makeWater({size:480,seg:80,amp:0.35,freq:0.09,speed:0.4,flow:[0,0.3],
    deep:0x0a121c,shallow:0x152636,skyc:0x1f2c3a,spec:0.55,y:-1.6});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(52,1.3,40),
    new THREE.MeshPhongMaterial({color:0x10151c,shininess:6,specular:0x242e3a}));
  bank.position.set(0,-0.65,-8); g.add(bank);
  const soil=makeGround({r:28,c1:0x0c1015,c2:0x141a23});
  soil.mesh.position.set(0,0.02,-8); g.add(soil.mesh);
  const ridge=makeRange({r:260,h:18,layers:2,peaks:4,seed:1963,color:0x0a0e15,atmo:0x36445a,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,0); g.add(ridge.g);
  /* 宫墙横亘（咫尺天涯）+ 墙外桃杏探出头来（满城春色）+ 墙头一线春色微光 */
  const wall=makeGongqiang({w:72,h:4.8}); wall.position.set(0,0,-9); g.add(wall);
  const tao1=makeTaoshu({seed:1965,h:6.4,rim:0.14}); tao1.position.set(18,-0.1,-11.5); g.add(tao1);
  const tao2=makeTaoshu({seed:1967,h:5.8,rim:0.1}); tao2.position.set(-21,-0.1,-11); g.add(tao2);
  const chunguang=makeGlow({n:26,box:[70,5,8],pos:[0,5.6,-12],color:0xb87e8a,size:11,speed:0.05,rise:0,maxA:0.1});
  g.add(chunguang.points);
  /* 宫墙柳：垂丝正拂在墙面上 */
  const wl1=makeChuiliu({h:8.0,seed:1969,n:15,sway:0.72}); wl1.g.position.set(7.5,-0.1,-7.4); g.add(wl1.g);
  const wl2=makeChuiliu({h:6.6,seed:1971,n:11,sway:0.58}); wl2.g.position.set(-15,-0.1,-8.2); g.add(wl2.g);
  /* 园中春宴：案 + 黄縢酒（坛/壶）+ 玉杯 + 盘飧，二人对饮 */
  const table=makeTable({w:5.6,d:2.0,h:1.35,wood:0x241a12}); table.g.position.set(-2.6,0,-3.4); g.add(table.g);
  const dish=makeDish({r:0.75,n:3}); dish.g.position.set(-4.2,1.28,-3.6); g.add(dish.g);
  const tan=makeVessel({type:'坛',mat:'陶',scale:0.46}); tan.g.position.set(-1.2,1.28,-4.0); g.add(tan.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.44}); hu.g.position.set(-2.3,1.28,-3.9); g.add(hu.g);
  const cup1=makeVessel({type:'杯',mat:'玉',scale:0.36,liquid:true}); cup1.g.position.set(-3.1,1.28,-2.9); g.add(cup1.g);
  const cup2=makeVessel({type:'杯',mat:'玉',scale:0.34,liquid:true}); cup2.g.position.set(-1.7,1.28,-2.8); g.add(cup2.g);
  const you=makeFigure({pose:'独立',robe:0x2c3442,belt:0x3e4a58,hat:'幞头',beard:true,scale:1.26,rim:0.66,rimC:0xa8a0c0,noProp:true});
  you.position.set(-5.0,0,-1.8); you.rotation.y=2.16; g.add(you);
  const wan=makeFigure({pose:'独立',robe:0x4e3c48,belt:0x60505c,hat:'发髻',scale:1.12,rim:0.62,rimC:0xd8a7b1,noProp:true});
  wan.position.set(-0.2,0,-5.2); wan.rotation.y=-0.93; g.add(wan);
  /* 东风渐恶：柳絮已有乱意（境②题壁的伏笔） */
  const xu=makeXusu({n:80,box:[46,8,9],pos:[2,4.5,-2.5],color:0xd8dde8,size:3.2,speed:0.6,maxA:0.14});
  g.add(xu.points);
  const mist=makeMist({n:7,spread:[210,20,90],pos:[0,8,-36],scale:72,color:0x8b9ab4,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',w:22,n:6,d:5,color:0x0a0e13,seed:1973,sway:0.9,tip:0x223038});
  fg.g.position.set(17,-1.2,14); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x080b10,seed:1975,rim:0.12});
  rk.g.position.set(-18,-1.2,11); g.add(rk.g);
  addLights(g,{c:0x8fa6c0,i:0.32,p:[-40,70,-20]},{c:0x222d3b,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); xu.update(t); chunguang.update(t);
    wl1.update(t,k); wl2.update(t,k); fg.update(t,k); rk.update(t,k);
    you.update(t,k); wan.update(t,k);
  }};
}
function bCuocuo(){ // 二 · 错错错 —— 一怀愁绪，几年离索：壁前独立，「错、错、错」已题上沈园壁
  const g=new THREE.Group();
  const water=makeWater({size:420,seg:72,amp:0.3,freq:0.09,speed:0.4,flow:[0,0.3],
    deep:0x0a121c,shallow:0x14242f,skyc:0x1c2937,spec:0.5,y:-1.8});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(46,1.3,34),
    new THREE.MeshPhongMaterial({color:0x0f141b,shininess:6,specular:0x222c38}));
  bank.position.set(0,-0.65,-9); g.add(bank);
  const soil=makeGround({r:24,c1:0x0b0f14,c2:0x121820});
  soil.mesh.position.set(0,0.02,-9); g.add(soil.mesh);
  const ridge=makeRange({r:240,h:16,layers:2,peaks:4,seed:1977,color:0x090d14,atmo:0x33414f,fogK:0.62,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-4); g.add(ridge.g);
  const wall=makeGongqiang({w:66,h:5.0}); wall.position.set(0,0,-10); g.add(wall);
  /* 壁上题字：右「错、错、错」已题（微光呼吸）；左「莫、莫、莫」此境不显 */
  const bi=makeBiwen({}); bi.g.position.set(0,0,-10); g.add(bi.g);
  const wl1=makeChuiliu({h:7.0,seed:1979,n:12,sway:0.68}); wl1.g.position.set(-13,-0.1,-9.0); g.add(wl1.g);
  /* 壁前独立人影（背影四分之三，面向题壁） */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.34,rim:0.6,rimC:0xa8a0c0});
  poet.position.set(-0.8,0,-5.4); poet.rotation.y=Math.PI-0.45; g.add(poet);
  /* 落英乱飞（东风恶之后） */
  const luo=makeLuoying({n:70,box:[40,12,22],pos:[0,8,-6],color:0xb87e8a,size:3.4,speed:0.85,maxA:0.22});
  g.add(luo.points);
  const mist=makeMist({n:7,spread:[200,20,90],pos:[0,8,-34],scale:70,color:0x8492aa,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:6,color:0x080b10,seed:1981,rim:0.12});
  fg.g.position.set(-16,-1.3,10); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:20,n:5,d:5,color:0x0a0e13,seed:1983,sway:0.85,tip:0x223038});
  fg2.g.position.set(16,-1.0,12); g.add(fg2.g);
  addLights(g,{c:0x8ba2bc,i:0.3,p:[-30,60,-10]},{c:0x202b39,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); luo.update(t);
    wl1.update(t,k); fg.update(t,k); fg2.update(t,k); poet.update(t,k);
    bi.update(t,k,0.62+0.14*Math.sin(t*0.5),0);
  }};
}
function bRenShou(){ // 三 · 人空瘦 —— 春如旧，人空瘦：同景异时，桃花吹落闲池阁，池畔一人空瘦
  const g=new THREE.Group();
  const water=makeWater({size:460,seg:80,amp:0.28,freq:0.11,speed:0.5,flow:[0,0.25],
    deep:0x0a121c,shallow:0x17293b,skyc:0x20303e,spec:0.75,y:-0.5});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(30,1.3,13),
    new THREE.MeshPhongMaterial({color:0x10151c,shininess:6,specular:0x242e3a}));
  bank.position.set(6,-0.65,9); g.add(bank);
  const soil=makeGround({r:14,c1:0x0c1015,c2:0x131922});
  soil.mesh.position.set(6,0.02,9); g.add(soil.mesh);
  const ridge=makeRange({r:250,h:16,layers:2,peaks:4,seed:1985,color:0x0a0e15,atmo:0x36445a,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-14); g.add(ridge.g);
  /* 闲池阁：水榭闲置在池上（无灯无人） */
  const xie=makeChige({}); xie.position.set(-7,-0.55,-3); xie.rotation.y=0.5; g.add(xie);
  /* 岸畔桃树两株（花已吹落大半）+ 垂柳一株（春如旧） */
  const tao1=makeTaoshu({seed:1987,h:4.2,rim:0.14}); tao1.position.set(12,0,4); g.add(tao1);
  const tao2=makeTaoshu({seed:1989,h:3.4,rim:0.1}); tao2.position.set(-2,0,6.5); g.add(tao2);
  const wl1=makeChuiliu({h:7.2,seed:1991,n:12,sway:0.6}); wl1.g.position.set(-14,-0.1,-8); g.add(wl1.g);
  /* 池畔空瘦一人（去年对饮者已不见） */
  const poet=makeFigure({pose:'独立',robe:0x252d3a,belt:0x39434f,hat:'幞头',beard:true,scale:1.3,rim:0.6,rimC:0xa8a0c0});
  poet.position.set(4.5,0,6.0); poet.rotation.y=Math.PI+0.6; g.add(poet);
  /* 桃花瓣落：空中缓落 + 水面浮瓣 */
  const luo=makeLuoying({n:130,box:[54,13,28],pos:[0,9,-5],color:0xc98a96,size:3.6,speed:0.85,maxA:0.3});
  g.add(luo.points);
  const fu=makeGlow({n:40,box:[40,0.5,16],pos:[0,-0.36,-6],color:0xc08090,size:3.2,speed:0.06,rise:0,maxA:0.24,add:false});
  g.add(fu.points);
  const mist=makeMist({n:7,spread:[210,16,90],pos:[0,4,-30],scale:70,color:0x8b9ab4,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:30,n:10,d:5,color:0x0a0e13,seed:1993,sway:0.8,tip:0x26323c});
  fg.g.position.set(-13,-0.5,13); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:6,color:0x080b10,seed:1995,rim:0.12});
  rk.g.position.set(19,-1.2,11); g.add(rk.g);
  addLights(g,{c:0x8fa6c0,i:0.32,p:[-40,60,-20]},{c:0x222d3b,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); luo.update(t); fu.update(t);
    wl1.update(t,k); fg.update(t,k); rk.update(t,k); poet.update(t,k);
  }};
}
function bMomo(){ // 四（末境·可点击）· 莫莫莫 —— 山盟虽在锦书难托：点击宫墙柳，柳絮拂壁，题字次第浮现
  const ctl={t:0,clicked:false,clickT:0,lastXu:0};
  const g=new THREE.Group();
  const water=makeWater({size:460,seg:76,amp:0.3,freq:0.09,speed:0.45,flow:[0,0.35],
    deep:0x0a121c,shallow:0x152636,skyc:0x1e2c3a,spec:0.55,y:-1.7});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(48,1.3,36),
    new THREE.MeshPhongMaterial({color:0x0f141b,shininess:6,specular:0x222c38}));
  bank.position.set(0,-0.65,-9); g.add(bank);
  const soil=makeGround({r:25,c1:0x0b0f14,c2:0x131922});
  soil.mesh.position.set(0,0.02,-9); g.add(soil.mesh);
  const ridge=makeRange({r:270,h:20,layers:2,peaks:5,seed:1997,color:0x0a0e15,atmo:0x36445a,fogK:0.62,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-6); g.add(ridge.g);   // 山盟虽在：远山仍横在天际
  const wall=makeGongqiang({w:70,h:5.0}); wall.position.set(0,0,-10); g.add(wall);
  const bi=makeBiwen({}); bi.g.position.set(0,0,-10); g.add(bi.g);
  /* 宫墙柳（点击主体）：柳拂墙头 */
  const wl1=makeChuiliu({h:8.2,seed:1999,n:16,sway:0.78}); wl1.g.position.set(7,-0.1,-8.2); g.add(wl1.g);
  const wl2=makeChuiliu({h:6.4,seed:2001,n:10,sway:0.6}); wl2.g.position.set(-14,-0.1,-8.8); g.add(wl2.g);
  /* 壁前背影（锦书难托） */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.32,rim:0.6,rimC:0xa8a0c0});
  poet.position.set(-2.4,0,-5.0); poet.rotation.y=Math.PI+0.3; g.add(poet);
  /* 柳絮（点击后大盛拂壁）+ 落尽前最后几瓣桃花 */
  const xu=makeXusu({n:220,box:[60,9,12],pos:[2,5,-1.5],color:0xdde2ec,size:3.6,speed:1.1,maxA:0});
  g.add(xu.points);
  const luo=makeLuoying({n:46,box:[40,12,20],pos:[0,8,-6],color:0xb87e8a,size:3.2,speed:0.7,maxA:0.16});
  g.add(luo.points);
  const mist=makeMist({n:7,spread:[210,20,100],pos:[0,8,-36],scale:74,color:0x8492aa,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',w:24,n:6,d:5,color:0x0a0e13,seed:2003,sway:0.9,tip:0x223038});
  fg.g.position.set(-17,-1.2,13); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:13,d:6,color:0x080b10,seed:2005,rim:0.12});
  rk.g.position.set(19,-1.3,10); g.add(rk.g);
  addLights(g,{c:0x8ba2bc,i:0.32,p:[-30,60,-15]},{c:0x212c3a,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt||0;
      const since=ctl.clicked?ctl.t-ctl.clickT:-1;
      /* 柳絮拂壁：点击后絮涌向壁面，尔后长拂不歇 */
      const xuLvl=since<0?0:Math.min(1,0.25+since/1.6);
      xu.mat.uniforms.uMaxA.value=k*0.34*xuLvl*(0.85+0.15*Math.sin(t*0.9));
      xu.update(t);
      /* 题字次第浮现：先「错、错、错」，再「莫、莫、莫」；未点击时只余 faint 呼吸的壁上旧题 */
      let lvC,lvM;
      if(since>=0){ lvC=sstep(0.2,1.6,since); lvM=sstep(1.8,3.4,since); }
      else{ lvC=0.15+0.05*Math.sin(t*0.5); lvM=0.1+0.04*Math.sin(t*0.4+1.3); }
      bi.update(t,k,lvC,lvM);
      if(ctl.clicked&&t-ctl.lastXu>6.0){ ctl.lastXu=t; pluck(0,0,0.045); pluck(2,0.4,0.04); }
      water.update(t); ridge.update(t,0); mist.update(t,k); luo.update(t);
      wl1.update(t,k); wl2.update(t,k); fg.update(t,k); rk.update(t,k); poet.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t; ctl.lastXu=-99;
        pluck(1,0.1,0.12); pluck(3,0.6,0.1); pluck(5,1.15,0.11); pluck(0,1.7,0.09);
        const fl=$('#flash'); fl.textContent=CTF_MOMENT; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
