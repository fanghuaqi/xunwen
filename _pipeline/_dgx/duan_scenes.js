/* ================= 短歌行 · 六境场景（夜宴金彩·建安变体：铜器、旌旗、朝露、乌鹊） ================= */

/* 旌旗：横杆下悬挂的旗面（底边摆幅最大），军帐气象 */
const BANNER_VERT=`
uniform float uTime; varying vec2 vUv;
void main(){ vUv=uv; vec3 p=position;
  float k=pow(1.0-uv.y,1.35);
  p.z+=sin(uTime*2.1+uv.x*4.6)*0.34*k;
  p.x+=sin(uTime*1.5+uv.x*3.1)*0.09*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0); }`;
const BANNER_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade; varying vec2 vUv;
void main(){
  vec3 c=mix(uC,uTipC,pow(clamp(vUv.x,0.0,1.0),1.2));
  gl_FragColor=vec4(c,uFade*(0.95-0.22*vUv.x)); }`;
function makeBanner(o){
  o=o||{};
  const w=o.w===undefined?2.8:o.w, h=o.h===undefined?3.6:o.h, ph=o.poleH===undefined?9:o.poleH;
  const g=new THREE.Group();
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.055,0.085,ph,6); pole.translate(0,ph/2,0); B.put(pole,0x1a130e);
  const bar=new THREE.CylinderGeometry(0.035,0.035,w*0.7,5); bar.rotateZ(Math.PI/2); bar.translate(w*0.32,ph,0); B.put(bar,0x1a130e);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x060403}),{c:0xb9905a,i:0.24,p:2.4})));
  const geo=new THREE.PlaneGeometry(w,h,10,3); geo.translate(0,-h/2,0);
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,depthWrite:false,
    uniforms:{uTime:{value:0},uC:{value:C(o.color===undefined?0x6e1e14:o.color)},
      uTipC:{value:C(o.tip===undefined?0xc05a38:o.tip)},uFade:{value:1}},
    vertexShader:BANNER_VERT,fragmentShader:BANNER_FRAG});
  const mesh=new THREE.Mesh(geo,mt); mesh.position.set(w*0.32,ph,0); mesh.renderOrder=1;
  g.add(mesh);
  g.userData.mt=mt;
  g.update=function(t,fk){ mt.uniforms.uTime.value=t; };
  return {g,update:g.update};
}

/* 孤树：主干收分 + 发散枝条（合批 1 mesh），可带稀疏叶团 */
function makeTree(o){
  o=o||{};
  const h=o.h===undefined?11:o.h, R=seedRnd(o.seed===undefined?5:o.seed);
  const trunkC=o.trunk===undefined?0x151009:o.trunk;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*1.4-0.7,h*0.98,0],h*0.050,h*0.014,8),trunkC);
  const nb=o.branches===undefined?8:o.branches;
  for(let i=0;i<nb;i++){
    const a=(i/nb)*Math.PI*2+R()*0.9, el=0.45+R()*0.85, len=h*(0.28+R()*0.40);
    const dx=Math.cos(a)*Math.cos(el), dy=Math.sin(el), dz=Math.sin(a)*Math.cos(el);
    const y0=h*(0.50+R()*0.42);
    const p1=[dx*len*0.22,y0+dy*len*0.28,dz*len*0.22];
    const p2=[dx*len,y0+dy*len,dz*len];
    B.put(limbGeo(p1,p2,h*0.020,h*0.007,6),trunkC);
    if(o.leaf&&R()<0.72){
      const lf=new THREE.SphereGeometry(len*0.30,7,5); lf.scale(1.3,0.75,1.3);
      lf.translate(p2[0],p2[1]+0.3,p2[2]); B.put(lf,o.leaf);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x241d14,emissive:0x030204}),
    {c:o.rimC===undefined?0xc9b088:o.rimC,i:o.rim===undefined?0.34:o.rim,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* 乌鹊：身首尾合批 1 mesh + 左右独立扑动的翅（3 draw call/只） */
function makeCrowBird(o){
  o=o||{};
  const c=o.color===undefined?0x0b0c12:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.5,8,6); body.scale(1.55,0.78,0.85); B.put(body,c);
  const head=new THREE.SphereGeometry(0.26,8,6); head.translate(0.82,0.26,0); B.put(head,c);
  const bk=new THREE.ConeGeometry(0.07,0.26,5); bk.rotateZ(-Math.PI/2); bk.translate(1.10,0.24,0); B.put(bk,shadeColor(c,2.0));
  const tail=new THREE.BoxGeometry(0.85,0.07,0.34); tail.translate(-0.82,0.06,0); B.put(tail,c);
  const b=new THREE.Group();
  b.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:c,vertexColors:true,shininess:12,
    specular:0x303a52,emissive:0x020305}),{c:0x8fa4c4,i:0.30,p:2.6})));
  const wgeo=new THREE.PlaneGeometry(1.9,0.72); wgeo.rotateY(Math.PI/2);   // 展向 z
  const wmat=new THREE.MeshPhongMaterial({color:shadeColor(c,1.6),side:THREE.DoubleSide,
    shininess:16,specular:0x3a4666,emissive:0x04050a});
  const w1=new THREE.Mesh(wgeo,wmat); w1.position.x=-0.15;
  const w2=new THREE.Mesh(wgeo,wmat); w2.position.x=-0.15;
  b.add(w1,w2);
  b.userData.w1=w1; b.userData.w2=w2;
  return b;
}

/* 鹿：颈首角足全合批，1 draw call 一只（深色剪影，靠火光边缘光塑形，避免被火光染成金球） */
function makeDeer(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale, R=seedRnd(o.seed===undefined?9:o.seed);
  const bodyC=o.body===undefined?0x4a3a28:o.body, dark=shadeColor(bodyC,0.62);
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(1.0,10,8); body.scale(1.45,0.80,0.66); body.translate(0,1.62,0); B.put(body,bodyC);
  const rump=new THREE.SphereGeometry(0.5,8,6); rump.scale(1,0.85,0.75); rump.translate(-1.2,1.8,0); B.put(rump,bodyC);
  B.put(limbGeo([0.8,1.9,0],[1.6,3.3,0],0.24,0.17,7),bodyC);
  const head=new THREE.SphereGeometry(0.42,8,6); head.scale(1.5,0.82,0.72); head.translate(1.95,3.55,0); B.put(head,shadeColor(bodyC,1.12));
  [-1,1].forEach(function(sd){
    B.put(limbGeo([1.7,3.8,sd*0.15],[2.05,4.05,sd*0.36],0.055,0.03,5),dark);
    B.put(limbGeo([2.0,3.85,sd*0.11],[2.5,4.7,sd*0.15],0.05,0.024,5),dark);
    B.put(limbGeo([2.3,4.4,sd*0.13],[2.56,4.82,sd*0.3],0.034,0.02,5),dark);
  });
  [[0.6,-0.4],[0.6,0.4],[-0.68,-0.4],[-0.68,0.4]].forEach(function(p){
    B.put(limbGeo([p[0],1.25,p[1]],[p[0]*1.05,0.05,p[1]],0.115,0.055,6),dark);
  });
  const tail=new THREE.SphereGeometry(0.14,6,5); tail.translate(-1.68,1.9,0); B.put(tail,shadeColor(bodyC,1.3));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x40342a,emissive:0x050402}),{c:o.rimC===undefined?0xd8b070:o.rimC,i:o.rim===undefined?0.32:o.rim,p:2.5}));
  const g=new THREE.Group(); mesh.frustumCulled=false; g.add(mesh);
  g.scale.setScalar(s);
  g.userData.ph=R()*6.283;
  return g;
}

/* 铜鼎：三足双耳圆鼎（周公吐哺之器），合批 1 mesh */
function makeDing(o){
  o=o||{};
  const r=o.r===undefined?1.1:o.r, c=o.color===undefined?0x453521:o.color;
  const B=new GeoBag();
  const pts=[[0,r*0.40],[r*0.70,r*0.40],[r*0.86,r*0.52],[r*0.90,r*0.80],[r*0.86,r*1.00],[r*0.70,r*1.05],[r*0.30,r*1.06],[0,r*1.06]];
  B.put(new THREE.LatheGeometry(pts.map(p=>new THREE.Vector2(p[0],p[1])),20),c);
  for(let i=0;i<3;i++){
    const a=i/3*Math.PI*2+0.4;
    B.put(limbGeo([Math.sin(a)*r*0.55,r*0.34,Math.cos(a)*r*0.55],[Math.sin(a)*r*0.66,0.02,Math.cos(a)*r*0.66],r*0.085,r*0.06,6),shadeColor(c,0.8));
  }
  [-1,1].forEach(function(sd){
    const ear=new THREE.TorusGeometry(r*0.20,r*0.048,6,12); ear.translate(sd*r*0.52,r*1.22,0); B.put(ear,shadeColor(c,1.18));
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:46,
    specular:0x8a7040,emissive:0x0c0804,side:THREE.DoubleSide}),{c:0xd8a860,i:0.38,p:2.8}));
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

function bCover(){ // 封面 · 苍茫夜色
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x070504,c2:0x171106});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:30,layers:2,peaks:4,seed:41,color:0x0a0806,atmo:0x3d3220,fogK:0.74,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'芦苇',w:80,n:24,d:9,color:0x050403,seed:5,sway:1.2});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xb8a888,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:70,box:[220,40,130],pos:[0,10,-40],color:0xd8c49a,size:8,speed:0.05,rise:0,maxA:0.5});
  g.add(motes.points);
  addLights(g,{c:0xb8a888,i:0.4,p:[30,70,40]},{c:0x2a241a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bJiuge(){ // 一 · 对酒当歌 —— 军帐夜宴：铜鼎列樽、旌旗火盆，高天朝露缓落
  const g=new THREE.Group();
  const grd=makeGround({r:95,c1:0x080605,c2:0x1e150c}); g.add(grd.mesh);
  /* 背景：帐外远山 + 帷帐 + 亭柱 */
  const ridge=makeRange({r:170,h:42,layers:2,peaks:4,seed:131,color:0x0a0807,atmo:0x3a3020,fogK:0.66,glowK:0.09,y:-14});
  ridge.g.position.set(0,0,-46); g.add(ridge.g);
  const curt=makeCurtain({w:44,h:12,color:0x2a1210,folds:12,deep:0.7});
  curt.g.position.set(0,0,-22); g.add(curt.g);
  [-15,15].forEach(function(x){
    const p=makePillar({h:11.5,r:0.4,color:0x241408,top:false});
    p.g.position.set(x,0,-8); g.add(p.g);
  });
  /* 旌旗两杆（旗面顶点波动） */
  const bans=[];
  [[-19,-4,0.7],[19,-5,-0.5]].forEach(function(p,i){
    const b=makeBanner({w:2.6,h:3.4,poleH:10,seed:i+1});
    b.g.position.set(p[0],0,p[1]); b.g.rotation.y=p[2]; g.add(b.g); bans.push(b);
  });
  /* 中景：长案 + 铜鼎 + 酒器 + 盘飧（器物皆落在案面上） */
  const tb=makeTable({w:11,d:3.4,h:1.5,wood:0x30201a}); tb.g.position.set(0,0,-0.5); g.add(tb.g);
  const ding=makeDing({r:1.05}); ding.position.set(-3.6,1.5,-0.8); g.add(ding);
  const zun=makeVessel({type:'樽',mat:'金',scale:0.95}); zun.g.position.set(-1.2,1.5,-1.1); g.add(zun.g);
  const jue=makeVessel({type:'爵',mat:'金',scale:1.0}); jue.g.position.set(0.6,1.5,-1.3); g.add(jue.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.95}); hu.g.position.set(2.4,1.5,-0.9); g.add(hu.g);
  const d1=makeDish({r:0.7,n:5}); d1.g.position.set(1.5,1.5,0.4); g.add(d1.g);
  const d2=makeDish({r:0.6,n:4,plate:0x5a4a3a}); d2.g.position.set(-0.4,1.5,0.7); g.add(d2.g);
  /* 人物：曹操倾酒居中，两位谋士坐饮 */
  const figs=[];
  const boss=makeFigure({pose:'倾酒',robe:0x30222a,belt:0xa8842f,hat:'幞头',beard:true,face:0,scale:1.22,rim:0.6,rimC:0xe8c070});
  boss.position.set(-0.6,0,-4.6); g.add(boss); figs.push(boss);
  const g1=makeFigure({pose:'坐饮',robe:0x243038,hat:'发髻',face:0.4,scale:1.12,rim:0.5,rimC:0xd8a05a});
  g1.position.set(-4.4,-0.9,-3.8); g.add(g1); figs.push(g1);
  const g2=makeFigure({pose:'坐饮',robe:0x2c303a,hat:'幞头',face:-0.4,scale:1.12,rim:0.5,rimC:0xd8a05a});
  g2.position.set(3.6,-0.9,-3.9); g.add(g2); figs.push(g2);
  const crowd=makeCrowd({n:8,rect:[-17,-14,34,5],seed:21,color:0x181a20,rimC:0xc98a4a,rim:0.26});
  g.add(crowd.mesh);
  /* 火盆两座 + 灯串三盏 */
  const braz=[];
  [[-9,3.2],[9,3.4]].forEach(function(p,i){
    const br=makeBrazier({r:1.0,fh:2.3,fw:1.15,light:1.3,lightD:44,embers:i?18:26,spark:i===0});
    br.g.position.set(p[0],0,p[1]); g.add(br.g); braz.push(br);
  });
  const lans=[];
  [0,1,2].forEach(function(i){
    const l=makeLantern(0.5,{flame:i===0});
    l.position.set(-6+i*6,7.6,-6); g.add(l); lans.push(l);
  });
  /* 朝露：高天缓落的露滴（凉白），应"譬如朝露" */
  const dew=makeGlow({n:110,box:[90,44,70],pos:[0,20,-16],color:0xbcd2e8,size:6,speed:0.045,rise:1,maxA:0.5});
  g.add(dew.points);
  /* 前景：坡石 + 栏杆 */
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:22,d:7,color:0x060504,seed:63,rim:0.15});
  rk.g.position.set(-16,-1.3,8); g.add(rk.g);
  const rail=makeForeground({kind:'栏杆',w:34,h:2.9,color:0x0c0a09,rim:0.2,seed:65});
  rail.g.position.set(1,-0.25,9.5); g.add(rail.g);
  const mist=makeMist({n:6,spread:[120,20,80],pos:[0,8,-14],scale:52,color:0xa8886a,op:0.07});
  g.add(mist.g);
  addLights(g,{c:0x9a8568,i:0.32,p:[30,60,40]},{c:0x2c2218,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); bans.forEach(function(b){b.update(t,k);});
    crowd.update(t); braz.forEach(function(br){br.update(t,k);});
    lans.forEach(function(l){l.update(t,k);});
    figs.forEach(function(f){f.update(t,k);});
    zun.update(t,k); jue.update(t,k); hu.update(t,k);
    dew.update(t); mist.update(t,k); rk.update(t,k); rail.update(t,k);
  }};
}
function bQingjin(){ // 二 · 青衿沉吟 —— 月下按剑独立，青衿身影自远方循路而来
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x07070a,c2:0x131722}); g.add(grd.mesh);
  const ridge=makeRange({r:200,h:48,layers:3,peaks:5,seed:151,color:0x0a0c12,atmo:0x2e3a50,fogK:0.60,glowK:0.09});
  g.add(ridge.g);
  /* 主体：按剑沉吟者（月色银蓝边缘光） */
  const boss=makeFigure({pose:'按剑',robe:0x1c2230,belt:0x8a6a33,hat:'幞头',beard:true,face:0.08,scale:1.5,rim:0.7,rimC:0xc9d8f0});
  boss.position.set(0,0,-2); g.add(boss);
  /* 远方：一列青衿身影（青色边缘光），沿小径疏落而来 */
  const scholars=makeCrowd({n:9,rect:[-26,-26,52,10],seed:33,color:0x14202a,rimC:0x7fc0a8,rim:0.4,sMin:0.8,sMax:1.0});
  g.add(scholars.mesh);
  /* 小径：两条微亮长石板，把"来路"引向主体 */
  [-2.6,2.6].forEach(function(x){
    const path=new THREE.Mesh(new THREE.BoxGeometry(1.6,0.06,44),
      new THREE.MeshPhongMaterial({color:0x1a2030,shininess:8,specular:0x36435c}));
    path.position.set(x,0.02,-8); g.add(path);
  });
  /* 忧思如流：银蓝雾流向远处淌去 */
  const flow=makeFlow({n:500,box:[130,20,90],pos:[0,11,-24],color:0x93a4bd,size:22,speed:3.6,maxA:0.3});
  g.add(flow.points);
  const mist=makeMist({n:10,spread:[240,34,150],pos:[0,10,-52],scale:75,color:0x9db2cc,op:0.10});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',w:56,n:20,d:7,color:0x04050a,seed:71,sway:0.9});
  reeds.g.position.set(-22,-1.6,18); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:6,color:0x05060a,seed:73,rim:0.15});
  rk.g.position.set(20,-1.2,15); g.add(rk.g);
  addLights(g,{c:0xaec2e0,i:0.5,p:[-40,90,-50]},{c:0x273248,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); scholars.update(t); flow.update(t); mist.update(t,k);
    boss.update(t,k); reeds.update(t,k); rk.update(t,k);
  }};
}
function bLuming(){ // 三 · 鹿鸣嘉宾 —— 呦呦鹿鸣于野，席上鼓瑟吹笙
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0d07,c2:0x1c2412}); g.add(grd.mesh);
  const ridge=makeRange({r:190,h:40,layers:2,peaks:4,seed:171,color:0x0b0e09,atmo:0x3a4028,fogK:0.62,glowK:0.08});
  g.add(ridge.g);
  /* 鹿群：一公四母，低头食苹（苹 = 草地上淡绿光点；鹿为深色剪影，不受火光直射） */
  const deer=[];
  [[-3.5,-9,1.2,0.4],[-8,-6,1.0,2.4],[-6.5,-4.5,0.95,1.2],[-0.5,-7,0.95,-0.9],[-2.5,-5,0.9,0.2]].forEach(function(p,i){
    const d=makeDeer({scale:p[2],seed:180+i,body:i?0x40342a:0x4a3a28});
    d.position.set(p[0],0,p[1]); d.rotation.y=p[3]; g.add(d); deer.push(d);
  });
  const ping=makeGlow({n:60,box:[40,1.4,26],pos:[-3,0.7,-6.5],color:0x9fce8f,size:4.5,speed:0.06,rise:0,maxA:0.28});
  g.add(ping.points);
  /* 席面：瑟 + 酒器 + 盘飧 + 嘉宾 */
  const tb=makeTable({w:8.5,d:3.0,h:1.45,wood:0x2e2014}); tb.g.position.set(12,0,-3.5); g.add(tb.g);
  const qin=new THREE.Group();
  const qb=new THREE.Mesh(new THREE.BoxGeometry(6.4,0.5,2.1),
    new THREE.MeshPhongMaterial({color:0x241812,shininess:46,specular:0x442a18}));
  qin.add(qb);
  for(let i=0;i<7;i++){
    const s=new THREE.Mesh(new THREE.CylinderGeometry(0.02,0.02,6.0,5),
      new THREE.MeshPhongMaterial({color:0xe8e2c8,shininess:60,emissive:0x222014}));
    s.rotation.z=Math.PI/2; s.position.set(0,0.30,-0.66+i*0.22); qin.add(s);
  }
  qin.position.set(12.4,2.05,-3.7); qin.rotation.y=-0.4; g.add(qin);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.8}); hu.g.position.set(9.6,1.45,-3.1); g.add(hu.g);
  const d1=makeDish({r:0.66,n:5}); d1.g.position.set(10.8,1.45,-4.4); g.add(d1.g);
  const d2=makeDish({r:0.6,n:4,plate:0x5a4a3a}); d2.g.position.set(13.8,1.45,-2.9); g.add(d2.g);
  const figs=[];
  const m1=makeFigure({pose:'坐饮',robe:0x26304a,hat:'幞头',face:-0.5,scale:1.1,rim:0.55,rimC:0xd8a05a});
  m1.position.set(9.2,-0.9,-5.6); g.add(m1); figs.push(m1);
  const m2=makeFigure({pose:'坐饮',robe:0x3a2c2a,hat:'发髻',face:0.3,scale:1.1,rim:0.55,rimC:0xd8a05a});
  m2.position.set(14.4,-0.9,-5.8); g.add(m2); figs.push(m2);
  /* 原野夜宴：篝火一座 */
  for(let i=0;i<4;i++){
    const log=new THREE.Mesh(new THREE.CylinderGeometry(0.26,0.36,3.8,7),
      new THREE.MeshPhongMaterial({color:0x241811,shininess:6}));
    log.rotation.z=Math.PI/2; log.rotation.y=i*Math.PI/4;
    log.position.set(5.5,0.32,-1); g.add(log);
  }
  const fire=makeFlame({h:4.6,w:2.4,planes:3,embers:60,spark:true,light:1.8,lightD:60,wide:0.33});
  fire.g.position.set(5.5,0.4,-1); g.add(fire.g);
  const mist=makeMist({n:6,spread:[120,22,80],pos:[0,8,-20],scale:52,color:0x8aa078,op:0.07});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:48,n:18,d:6,color:0x050704,seed:91,sway:1.0});
  fg.g.position.set(-16,-1.4,12); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:16,d:6,color:0x050704,seed:93,rim:0.14});
  rk.g.position.set(16,-1.2,10); g.add(rk.g);
  addLights(g,{c:0xc9b088,i:0.4,p:[40,70,30]},{c:0x26241a,i:0.62});
  const pl=new THREE.PointLight(0xff9a4a,1.2,48); pl.position.set(5.5,4,-1); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fire.update(t,k); mist.update(t,k);
    deer.forEach(function(d){ d.position.y=0.05+0.05*Math.sin(t*0.7+d.userData.ph); });
    hu.update(t,k);
    figs.forEach(function(f){f.update(t,k);});
    d1.glow.material.opacity=k*0.16*(0.8+0.2*Math.sin(t*2.2));
    d2.glow.material.opacity=k*0.16*(0.8+0.2*Math.sin(t*2.5+1));
    fg.update(t,k); rk.update(t,k);
    pl.intensity=k*(1.2+Math.sin(t*7.7)*0.14);
  },onEnter(){ pluck(1,0.2,0.14); pluck(3,0.8,0.12); pluck(4,1.4,0.12); pluck(2,2.0,0.12); }};
}
function bMingyue(){ // 四 · 明月可掇 —— 高台指月，明月高不可掇；故人越陌度阡而来
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x070809,c2:0x16181c}); g.add(grd.mesh);
  const ridge=makeRange({r:210,h:44,layers:2,peaks:4,seed:191,color:0x0a0b10,atmo:0x33405c,fogK:0.60,glowK:0.10});
  g.add(ridge.g);
  /* 主体：高台指月者 */
  const plat=new THREE.Mesh(new THREE.CylinderGeometry(4.6,5.2,1.5,18),
    new THREE.MeshPhongMaterial({color:0x1a1a20,shininess:14,specular:0x3a4050}));
  plat.position.set(0,0.75,-6); g.add(plat);
  const boss=makeFigure({pose:'指月',robe:0x202838,belt:0x9a7a38,hat:'幞头',beard:true,face:0,scale:1.55,rim:0.72,rimC:0xd8e4fa});
  boss.position.set(0,1.5,-6); g.add(boss);
  /* 越陌度阡：田陌纵横，远处行人成列 */
  const pa=new THREE.Mesh(new THREE.BoxGeometry(2.0,0.06,70),
    new THREE.MeshPhongMaterial({color:0x181c26,shininess:8,specular:0x303a4c}));
  pa.rotation.y=0.35; pa.position.set(-4,0.02,-14); g.add(pa);
  const pb=new THREE.Mesh(new THREE.BoxGeometry(2.0,0.06,70),
    new THREE.MeshPhongMaterial({color:0x181c26,shininess:8,specular:0x303a4c}));
  pb.rotation.y=-0.5; pb.position.set(6,0.02,-10); g.add(pb);
  const walkers=makeCrowd({n:10,rect:[-30,-34,60,14],seed:201,color:0x151a26,rimC:0xd8b878,rim:0.34,sMin:0.75,sMax:1.0});
  g.add(walkers.mesh);
  /* 忧从中来：灰蓝雾流自月下漫过 */
  const flow=makeFlow({n:600,box:[150,26,110],pos:[0,14,-18],color:0x8fa2c0,size:24,speed:4.2,maxA:0.34});
  g.add(flow.points);
  const mist=makeMist({n:8,spread:[220,30,130],pos:[0,12,-56],scale:78,color:0x9fb2d0,op:0.09});
  g.add(mist.g);
  const fgL=makeForeground({kind:'岩壁',n:3,r:4.6,w:22,d:8,color:0x04050a,seed:97,rim:0.16});
  fgL.g.position.set(-24,-2,16); g.add(fgL.g);
  const reeds=makeForeground({kind:'芦苇',w:36,n:14,d:6,color:0x04050a,seed:99,sway:0.9});
  reeds.g.position.set(22,-1.6,14); g.add(reeds.g);
  addLights(g,{c:0xb8cce8,i:0.55,p:[-50,110,-60]},{c:0x2a344c,i:0.55});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); walkers.update(t); flow.update(t); mist.update(t,k);
    boss.update(t,k); fgL.update(t,k); reeds.update(t,k);
  }};
}
function bWuque(){ // 五 · 月明星稀（标志性瞬间）—— 孤树立于四野，乌鹊绕树三匝
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x050609,c2:0x101318}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:36,layers:3,peaks:5,seed:211,color:0x080a10,atmo:0x2c3850,fogK:0.58,glowK:0.07});
  g.add(ridge.g);
  /* 孤树：主干虬枝（月色勾边） */
  const tree=makeTree({h:13,seed:7,branches:9,rimC:0xb9c4d8,rim:0.4});
  tree.g.position.set(0,0,-6); g.add(tree.g);
  /* 乌鹊群：绕树盘旋（三匝之势），翅独立扑动 */
  const crows=[];
  for(let i=0;i<7;i++){
    const b=makeCrowBird({});
    g.add(b);
    crows.push({b,r:7.5+i*1.1,y:9.5+i*1.15,sp:0.42+(i%3)*0.09,ph:i*0.9});
  }
  const mist=makeMist({n:10,spread:[280,30,160],pos:[0,9,-58],scale:82,color:0x8ea4c4,op:0.10});
  g.add(mist.g);
  /* 前景：枯枝入画 + 坡石 */
  const fgBr=makeForeground({kind:'树枝',w:30,n:12,d:6,color:0x05060a,seed:101,sway:0.7});
  fgBr.g.position.set(6,-0.5,16); g.add(fgBr.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:20,d:7,color:0x04050a,seed:103,rim:0.16});
  rk.g.position.set(-13,-1.4,14); g.add(rk.g);
  addLights(g,{c:0xb8cce8,i:0.55,p:[-50,100,-40]},{c:0x232c40,i:0.5});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); fgBr.update(t,k); rk.update(t,k);
    for(const c of crows){
      const a=c.ph+t*c.sp;
      c.b.position.set(Math.cos(a)*c.r,c.y+Math.sin(t*0.9+c.ph)*0.8,-6+Math.sin(a)*c.r*0.8);
      c.b.rotation.y=-a-Math.PI/2;
      const f=Math.sin(t*7+c.ph*3)*0.5;
      c.b.userData.w1.rotation.x=f; c.b.userData.w2.rotation.x=-f;
    }
  }};
}
function bGuixin(){ // 六（末境·可点击）· 天下归心 —— 山不厌高海不厌深，点召乌鹊绕山而栖
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,moon:0};
  const grd=makeGround({r:150,c1:0x070708,c2:0x15141a}); g.add(grd.mesh);
  /* 背景高山（不厌其高） */
  const ridge=makeRange({r:220,h:92,layers:3,peaks:5,seed:231,color:0x0a0b12,atmo:0x364460,fogK:0.58,glowK:0.10});
  ridge.g.position.set(0,0,-60); g.add(ridge.g);
  /* 海（不厌其深）：右侧暗海，月光碎浪 */
  const sea=makeWater({size:540,seg:80,amp:0.8,freq:0.09,speed:0.9,flow:[-0.6,0.4],spec:1.5,
    deep:0x081626,shallow:0x123452,skyc:0x24425e,moonDir:[-90,110,-160]});
  sea.mesh.position.set(135,-0.6,-60); g.add(sea.mesh);
  /* 高台铜鼎：周公吐哺之诚 */
  const plat=new THREE.Mesh(new THREE.CylinderGeometry(7.5,8.6,2.2,18),
    new THREE.MeshPhongMaterial({color:0x191a1e,shininess:12,specular:0x363c48}));
  plat.position.set(-6,1.1,-16); g.add(plat);
  const ding=makeDing({r:1.6}); ding.position.set(-6,2.2,-16); g.add(ding);
  const fire=makeFlame({h:2.6,w:1.3,planes:2,embers:26,spark:false,light:1.1,lightD:40,wide:0.32,core:0xffe3a0,outer:0xff7a22});
  fire.g.position.set(-6,3.6,-16); g.add(fire.g);
  /* 台上孤树（可栖之枝） */
  const tree=makeTree({h:10,seed:9,branches:8,rimC:0xc9b088,rim:0.36});
  tree.g.position.set(-10,2.2,-13); g.add(tree.g);
  /* 四野先有三两远鸦（点击后群鸦南来绕山而栖） */
  const perches=[[-10,12.4,-13],[-9.2,11.4,-12.2],[-10.6,11.0,-13.6],[-9.6,12.8,-13.8],[-10.2,10.4,-12.4],
                 [-4.2,3.6,-12.2],[-8.0,3.6,-11.4],[-11.8,3.6,-14.6],[-6.2,3.6,-18.2]];
  const crows=[];
  for(let i=0;i<9;i++){
    const b=makeCrowBird({});
    g.add(b);
    crows.push({b,ph:i*0.75,r:rnd(46,70),y:rnd(16,26),sp:rnd(0.16,0.24),perch:i%perches.length});
  }
  /* 归心金光（点击后升起） */
  const gold=makeGlow({n:160,box:[90,30,70],pos:[-6,4,-14],color:0xffd98a,size:11,speed:0.05,rise:1,maxA:0});
  g.add(gold.points);
  const burst=makeBurst({n:90,color:0xffe0a0,pos:[-6,8,-14]}); g.add(burst.points);
  const mist=makeMist({n:10,spread:[260,34,150],pos:[0,10,-52],scale:80,color:0x94a8c8,op:0.09});
  g.add(mist.g);
  const fgL=makeForeground({kind:'岩壁',n:3,r:4.8,w:24,d:8,color:0x04050a,seed:107,rim:0.16});
  fgL.g.position.set(-22,-2.4,18); g.add(fgL.g);
  const fgBr=makeForeground({kind:'树枝',w:26,n:10,d:6,color:0x05060a,seed:109,sway:0.6});
  fgBr.g.position.set(14,-0.6,15); g.add(fgBr.g);
  addLights(g,{c:0xaec4ea,i:0.6,p:[-60,110,-50]},{c:0x28304a,i:0.55});
  const pl=new THREE.PointLight(0xffca7a,1.7,60); pl.position.set(-6,6,-14); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      ridge.update(t,0); sea.update(t); fire.update(t,k); mist.update(t,k);
      fgL.update(t,k); fgBr.update(t,k); burst.update(t);
      gold.mat.uniforms.uMaxA.value=k*0.7*ctl.moon;
      gold.update(t);
      pl.intensity=k*1.7*(0.30+ctl.moon*0.70*(0.85+0.15*Math.sin(t*3.1)));
      for(const c of crows){
        const a=c.ph+t*c.sp;
        if(ctl.t<1.5){                              // 未点击：远处漫飞
          c.b.position.set(Math.cos(a)*c.r,c.y+Math.sin(t*0.7+c.ph)*1.5,-30+Math.sin(a)*c.r*0.6);
          c.b.rotation.y=-a-Math.PI/2;
          const f=Math.sin(t*6+c.ph*3)*0.45;
          c.b.userData.w1.rotation.x=f; c.b.userData.w2.rotation.x=-f;
        }else{                                      // 点击后：绕山渐收 → 落枝
          const q=clamp((ctl.t-1.5)/6,0,1);
          const rr=lerp(c.r,7,Math.pow(q,0.75)), yy=lerp(c.y,perches[c.perch][1]+0.4,Math.pow(q,0.8));
          const ang=a+q*6.0;
          const px=lerp(Math.cos(ang)*rr,perches[c.perch][0],sstep(0.8,1,q));
          const pz=lerp(-16+Math.sin(ang)*rr*0.8,perches[c.perch][2],sstep(0.8,1,q));
          c.b.position.set(px,yy,pz);
          c.b.rotation.y=-ang-Math.PI/2;
          const f=q<0.85?Math.sin(t*8+c.ph*3)*0.5:0.18;
          c.b.userData.w1.rotation.x=f; c.b.userData.w2.rotation.x=-f;
        }
      }
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.t=1.5;   // 直接进入"南来归山"段
        burst.fire(); pluck(3,0.1,0.16); pluck(5,0.5,0.12); bell();
        const fl=$('#flash'); fl.textContent='天下归心'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.moon=Math.min(1,ctl.moon+0.5);            // 月更明
    },clicked:false};
  return api;
}
