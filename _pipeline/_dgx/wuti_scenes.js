/* ================= 无题·相见时难别亦难 · 四境场景（烟雨江南·相思变体：东风花残、蚕丝烛泪、晓镜夜吟、青鸟探看） ================= */

/* 大红蜡烛：粗柱 + 烛泪凝结 + 烛芯焰体（蜡炬成灰泪始干） */
function makeCandleBig(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.55,0.65,5.2,10);
  body.translate(0,2.6,0); B.put(body,0xb02428);
  /* 烛泪堆积凝痕 */
  for(let i=0;i<4;i++){
    const drop=new THREE.CylinderGeometry(0.12,0.06,1.4+i*0.3,5);
    const a=i*1.57;
    drop.translate(Math.cos(a)*0.6,4.0-i*0.6,Math.sin(a)*0.6); B.put(drop,0xc8383c);
  }
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,
    specular:0xe08080,emissive:0x1a0505}),{c:0xe07080,i:0.35,p:2.5})));
  /* 烛台底座 */
  const stand=new THREE.Mesh(new THREE.CylinderGeometry(1.6,2.0,0.5,14),
    new THREE.MeshPhongMaterial({color:0x3a2818,shininess:16}));
  stand.position.y=0.25; g.add(stand);
  /* 焰心火焰 */
  const fl=makeFlame({h:2.2,w:1.0,planes:2,embers:20,spark:false,light:1.4,lightD:32,wide:0.34,
    core:0xffe4a0,outer:0xff4020});
  fl.g.position.y=5.2; g.add(fl.g);
  g.userData.flame=fl;
  g.scale.setScalar(s);
  return g;
}

/* 铜镜：圆镜+镜台（晓镜但愁云鬓改） */
function makeMirrorStand(o){
  o=o||{};
  const g=new THREE.Group();
  const base=new THREE.Mesh(new THREE.BoxGeometry(3.6,0.6,2.4),
    new THREE.MeshPhongMaterial({color:0x2a1c14,shininess:8}));
  base.position.y=0.3; g.add(base);
  const post=new THREE.Mesh(new THREE.CylinderGeometry(0.1,0.1,2.0,6),
    new THREE.MeshPhongMaterial({color:0x2a1c14}));
  post.position.set(0,1.6,0); g.add(post);
  const ring=new THREE.Mesh(new THREE.TorusGeometry(1.5,0.12,6,24),
    new THREE.MeshPhongMaterial({color:0x8a6a34,shininess:40,specular:0xd8b060}));
  ring.position.set(0,3.6,0); g.add(ring);
  const glass=new THREE.Mesh(new THREE.CircleGeometry(1.4,24),
    new THREE.MeshPhongMaterial({color:0x242830,shininess:90,specular:0xaac0d8}));
  glass.position.set(0,3.6,0.02); g.add(glass);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 青鸟：衔书飞鸟（自写小鸟原语，青羽银光） */
function makeBlueBird(o){
  o=o||{};
  const g=new THREE.Group();
  const B=new GeoBag();
  const c=o.color===undefined?0x2a6a8a:o.color;
  const body=new THREE.SphereGeometry(0.35,7,5); body.scale(1.8,0.85,0.85); B.put(body,c);
  const head=new THREE.SphereGeometry(0.2,6,5); head.translate(0.68,0.22,0); B.put(head,shadeColor(c,1.2));
  const tail=new THREE.BoxGeometry(0.7,0.06,0.28); tail.translate(-0.68,0.05,0); B.put(tail,shadeColor(c,0.8));
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x70b8d8,emissive:0x06141a}),{c:0x7fd8e8,i:0.4,p:2.5})));
  const wgeo=new THREE.PlaneGeometry(1.6,0.55); wgeo.rotateY(Math.PI/2);
  const wmat=new THREE.MeshPhongMaterial({color:0x3a88aa,side:THREE.DoubleSide,shininess:20,specular:0x8ae8ff});
  const w1=new THREE.Mesh(wgeo,wmat); w1.position.x=-0.1;
  const w2=new THREE.Mesh(wgeo,wmat); w2.position.x=-0.1;
  g.add(w1,w2);
  g.userData.w1=w1; g.userData.w2=w2;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

function bCover(){ // 封面 · 烟雨残红
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x10141a,c2:0x1e1c26});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:28,layers:2,peaks:4,seed:41,color:0x10121a,atmo:0x3c3444,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,44); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x0c0a12,seed:5,rim:0.15});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0xa88ea0,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xd0a8bc,size:8,speed:0.05,rise:0,maxA:0.42});
  g.add(motes.points);
  addLights(g,{c:0xb890a8,i:0.42,p:[30,70,40]},{c:0x28202c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bDongfeng(){ // 一 · 东风花残 —— 东风无力，百花飘残
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x12141c,c2:0x1c1e28});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:32,layers:2,peaks:4,seed:1021,color:0x0e1018,atmo:0x343040,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 庭院栏杆 + 闺阁回廊 */
  const rail=makeForeground({kind:'栏杆',w:26,h:2.6,color:0x1c1822,rim:0.2,seed:181});
  rail.g.position.set(-2,-0.2,-8); g.add(rail.g);
  /* 飘落残红（落瓣粉紫，缓落飘散） */
  const petals=makeGlow({n:180,box:[110,26,70],pos:[0,12,-16],color:0xd08aa8,size:5.5,speed:0.08,rise:1,maxA:0.45});
  petals.points.renderOrder=3; g.add(petals.points);
  /* 庭院独立女子（红妆微黯，黯然独立） */
  const lady=makeFigure({pose:'独立',robe:0x5a3448,belt:0x8a5468,hat:'发髻',face:0.2,scale:1.25,rim:0.55,rimC:0xd08aa8});
  lady.position.set(-1.5,0,-4); g.add(lady);
  /* 枯残花树一株 */
  const tr=new THREE.Mesh(new THREE.CylinderGeometry(0.12,0.18,5.4,6),
    new THREE.MeshPhongMaterial({color:0x2a1c16}));
  tr.position.set(9,2.7,-10); g.add(tr);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-40],scale:70,color:0x8a7a90,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x0c0a12,seed:183,rim:0.14});
  rk.g.position.set(-13,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xa88aa0,i:0.44,p:[-40,70,-40]},{c:0x221c28,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); petals.update(t); mist.update(t,k);
    lady.update(t,k); rk.update(t,k);
  }};
}
function bCanju(){ // 二（标志性瞬间）· 蚕丝烛泪 —— 春蚕到死丝方尽，蜡炬成灰泪始干
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x100e16,c2:0x1a1622});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:26,layers:2,peaks:3,seed:1031,color:0x0c0a12,atmo:0x2e2636,fogK:0.62,glowK:0.05});
  g.add(ridge.g);
  /* 主体：巨大的红烛（巨炬烛泪） */
  const candle=makeCandleBig({scale:1.45});
  candle.position.set(0,0,-4.5); g.add(candle);
  /* 蚕丝万缕：盘旋在红烛周围的银白光丝环 */
  const silkRing=makeGlow({n:220,box:[44,18,44],pos:[0,6,-4.5],color:0xe8e4f4,size:4.0,speed:0.04,rise:0,maxA:0.55});
  silkRing.points.renderOrder=4; g.add(silkRing.points);
  /* 烛泪低滴的光尘 */
  const tears=makeGlow({n:60,box:[8,12,8],pos:[0,4,-4.5],color:0xff6040,size:5,speed:0.14,rise:1,maxA:0.42});
  tears.points.renderOrder=4; g.add(tears.points);
  const mist=makeMist({n:6,spread:[190,18,100],pos:[0,8,-36],scale:66,color:0x7a5a70,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x0a0810,seed:185,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc07080,i:0.42,p:[20,50,-20]},{c:0x241822,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); silkRing.update(t); tears.update(t); mist.update(t,k);
    candle.userData.flame.update(t,k); rk.update(t,k);
  }};
}
function bXiaojing(){ // 三 · 晓镜夜吟 —— 晓镜但愁云鬓改，夜吟应觉月光寒
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0e1018,c2:0x161a24});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:30,layers:2,peaks:4,seed:1041,color:0x0a0d16,atmo:0x283244,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 妆台与铜镜 */
  const mirror=makeMirrorStand({scale:1.25}); mirror.position.set(-4.5,0,-3.5); mirror.rotation.y=0.4; g.add(mirror);
  /* 对镜人（云鬓变色意象） */
  const lady=makeFigure({pose:'独立',robe:0x3a3048,belt:0x705a6a,hat:'发髻',hair:0xb8b0c4,
    face:0.4,scale:1.15,rim:0.5,rimC:0xc08aa8});
  lady.position.set(-4.5,0,-1.6); g.add(lady);
  /* 寒月光柱洒在窗棂前 */
  const moonBeam=new THREE.Mesh(new THREE.PlaneGeometry(8,40),
    new THREE.MeshBasicMaterial({color:0xb0c8e0,transparent:true,opacity:0.25,depthWrite:false,side:THREE.DoubleSide}));
  moonBeam.position.set(4,10,-10); moonBeam.rotation.x=0.35; g.add(moonBeam);
  /* 夜吟人影（帘外相思的游子远影） */
  const poet=makeFigure({pose:'指月',robe:0x222634,belt:0x505466,hat:'幞头',beard:true,face:-0.3,scale:1.1,rim:0.4,rimC:0xa0b4cc,noProp:true});
  poet.position.set(5.5,0,-12); g.add(poet);
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-40],scale:68,color:0x7a88a0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x080910,seed:187,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x90a8c4,i:0.44,p:[-40,80,-30]},{c:0x1c2230,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); lady.update(t,k); poet.update(t,k); rk.update(t,k);
    moonBeam.material.opacity=k*(0.22+0.05*Math.sin(t*0.7));
  }};
}
function bQingniao(){ // 四（末境·可点击）· 青鸟探看 —— 蓬山无多路，青鸟殷勤为探看（点击：青鸟衔书振翅飞向蓬山）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,fly:0};
  const water=makeWater({size:720,seg:90,amp:0.3,freq:0.1,speed:0.55,flow:[-0.5,0.2],spec:1.3,
    deep:0x0a1420,shallow:0x163448,skyc:0x264258,moonDir:[0,90,-170]});
  g.add(water.mesh);
  /* 蓬山仙境：缥缈仙山（远山高拔、云烟环绕） */
  const ridge=makeRange({r:240,h:56,layers:3,peaks:5,seed:1051,color:0x0d121c,atmo:0x344660,fogK:0.60,glowK:0.07});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  /* 仙山宫殿微光 */
  for(let i=0;i<3;i++){
    const win=new THREE.Mesh(new THREE.PlaneGeometry(1.6,2.2),
      new THREE.MeshBasicMaterial({color:0x8fd0f0,transparent:true,opacity:0.6}));
    win.position.set(-16+i*16,14+i*3,-78); g.add(win);
  }
  /* 青鸟（点击后振翅破空飞向蓬山） */
  const bird=makeBlueBird({scale:1.45}); bird.position.set(0,3.6,-8); g.add(bird);
  /* 衔信光带 */
  const letter=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88ab0,
    transparent:true,opacity:0.85,depthWrite:false,blending:THREE.AdditiveBlending}));
  letter.scale.set(2.8,2.8,1); g.add(letter);
  const burst=makeBurst({n:90,color:0x7fd8e8,pos:[0,6,-8]}); g.add(burst.points);
  const mist=makeMist({n:8,spread:[240,24,130],pos:[0,10,-50],scale:76,color:0x7a8ca0,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x080910,seed:189,rim:0.15});
  rk.g.position.set(-14,-1.5,13); g.add(rk.g);
  addLights(g,{c:0x8fa8c0,i:0.46,p:[-40,80,-40]},{c:0x1a2230,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.fly=Math.min(1,ctl.fly+dt/2.8);
      ridge.update(t,0); water.update(t); mist.update(t,k); rk.update(t,k);
      burst.update(t);
      /* 青鸟飞行轨迹：向蓬山高空飞去 */
      bird.position.set(ctl.fly*12, 3.6+ctl.fly*18+Math.sin(t*2.4)*0.5, -8-ctl.fly*56);
      const f=ctl.fly>0?Math.sin(t*8)*0.5:Math.sin(t*2)*0.12;
      bird.userData.w1.rotation.x=f; bird.userData.w2.rotation.x=-f;
      letter.position.copy(bird.position).add(new THREE.Vector3(0.8,0.2,0));
      letter.material.opacity=k*0.85*(0.45+0.45*Math.min(1,ctl.fly*3))*(0.85+0.15*Math.sin(t*3));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.5,0.12); pluck(5,0.9,0.12);
        const fl=$('#flash'); fl.textContent='青鸟为探看'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
