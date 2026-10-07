/* ================= 茅屋为秋风所破歌 · 四境场景（水墨夜思·破庐变体：秋风卷茅、群童抱茅、屋漏夜雨、广厦万间） ================= */

/* 破茅屋：歪斜土墙 + 破顶（缺口的茅草顶，合批 1 mesh） */
function makeHutBroken(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(5.6,2.3,4.4); body.translate(0,1.15,0); B.put(body,0x2a2620);
  const roof=new THREE.ConeGeometry(4.8,1.7,4); roof.rotateY(Math.PI/4);
  roof.translate(0,3.0,0); B.put(roof,0x241e16);
  const hole=new THREE.ConeGeometry(1.3,0.5,4); hole.rotateY(Math.PI/4);
  hole.translate(1.3,3.15,0.7); B.put(hole,0x0e0c09);      // 顶上破洞
  const door=new THREE.BoxGeometry(0.95,1.6,0.08); door.translate(0.7,0.8,2.24); B.put(door,0x0d0a07);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2c2c30,emissive:0x070709}),{c:o.rimC===undefined?0x8a9ab0:o.rimC,i:0.18,p:2.2}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return g;
}

/* 茅草片：被风卷起的草叶（合批 1 mesh，顶点动画随机化不做——整体绕 x 翻转即可） */
function makeStraws(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?761:o.seed);
  const B=new GeoBag();
  for(let i=0;i<(o.n===undefined?16:o.n);i++){
    const st=new THREE.CylinderGeometry(0.03,0.05,1.1,4);
    st.rotateZ((R()-0.5)*2.4); st.rotateX((R()-0.5)*2.4);
    st.translate((R()-0.5)*30,(R()-0.5)*16,-(R()*20));
    B.put(st,0x5a4a34);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x3c3a30,emissive:0x090806}),{c:0x8a9ab0,i:0.2,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return g;
}

/* 广厦幻影：连片高屋的半透剪影（点击后亮窗） */
function makeMansion(o){
  o=o||{};
  const g=new THREE.Group();
  const B=new GeoBag();
  for(let i=0;i<6;i++){
    const w=7+(i%3)*3, h=10+((i*7)%14);
    const b=new THREE.BoxGeometry(w,h,w*0.6);
    b.translate(-26+i*10.5,h/2,0); B.put(b,0x1a2230);
    const r=new THREE.ConeGeometry(w*0.72,w*0.3,4); r.rotateY(Math.PI/4);
    r.translate(-26+i*10.5,h+w*0.15,0); B.put(r,0x232e40);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36486a,emissive:0x0a0f18}),{c:0x8a9ab0,i:0.24,p:2.4}));
  mesh.frustumCulled=false; mesh.position.z=-30;
  const g2=new THREE.Group(); g2.add(mesh);
  /* 暖窗（点击后亮） */
  const wins=[];
  for(let i=0;i<8;i++){
    const w=new THREE.Mesh(new THREE.PlaneGeometry(0.8,1.1),
      new THREE.MeshBasicMaterial({color:0xffc878,transparent:true,opacity:0.75}));
    w.position.set(-22+(i%4)*10.5,4+(i>>2)*5,-26.6);
    g2.add(w); wins.push(w);
  }
  g2.userData.wins=wins;
  return g2;
}

function bCover(){ // 封面 · 秋高风夜
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0a0a0e,c2:0x141419});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:28,layers:2,peaks:4,seed:41,color:0x0b0c11,atmo:0x323448,fogK:0.74,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x08080b,seed:5,rim:0.12});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x7c8094,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:50,box:[220,36,130],pos:[0,9,-40],color:0x9aa0b4,size:7,speed:0.05,rise:0,maxA:0.3,add:false});
  g.add(motes.points);
  addLights(g,{c:0x8a90a4,i:0.34,p:[30,70,40]},{c:0x22242e,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bJuenao(){ // 一 · 秋风卷茅 —— 风怒号、茅飞天际（风声粒子横扫）
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a0a0e,c2:0x121319});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:34,layers:2,peaks:4,seed:751,color:0x0b0c11,atmo:0x323448,fogK:0.60,glowK:0.05});
  ridge.g.position.set(0,0,-50); g.add(ridge.g);
  /* 破茅屋 */
  const hut=makeHutBroken({scale:1.3}); hut.position.set(0,0,-6); hut.rotation.y=-0.25; g.add(hut);
  /* 江对岸（茅飞渡江） */
  const water=makeWater({size:400,seg:70,amp:0.5,freq:0.12,speed:1.0,flow:[-0.9,0.2],spec:1.3,
    deep:0x0b1118,shallow:0x182c38,skyc:0x243448,moonDir:[-60,90,-160]});
  water.mesh.position.set(0,-0.4,-30); g.add(water.mesh);
  /* 飞茅（空中翻卷的草叶） */
  const straws=makeStraws({n:18,seed:761}); straws.position.set(0,6,-6); g.add(straws);
  /* 狂风流（横扫的暗色风流） */
  const wind=makeFlow({n:520,box:[160,24,100],pos:[0,12,-18],color:0x5a6274,size:18,speed:8.5,maxA:0.3});
  g.add(wind.points);
  const mist=makeMist({n:7,spread:[190,18,100],pos:[0,8,-36],scale:64,color:0x7c8094,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x08080b,seed:137,rim:0.12});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0x8a90a4,i:0.3,p:[30,60,30]},{c:0x22242e,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); wind.update(t); mist.update(t,k);
    straws.rotation.z=Math.sin(t*0.9)*0.06;
    straws.position.y=6+Math.sin(t*0.7)*1.2;
    rk.update(t,k);
  }};
}
function bQuntong(){ // 二 · 群童抱茅 —— 竹林边群童抱茅跑，老人倚杖叹息
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x09090d,c2:0x111218});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:30,layers:2,peaks:4,seed:761,color:0x0a0b10,atmo:0x2e303c,fogK:0.58,glowK:0.04});
  g.add(ridge.g);
  /* 竹林（右后） */
  for(let i=0;i<9;i++){
    const st=new THREE.Mesh(new THREE.CylinderGeometry(0.09,0.11,9,6),
      new THREE.MeshPhongMaterial({color:0x1c2418,shininess:10}));
    st.position.set(12+Math.sin(i*2.1)*2.5,4.5,-12-i*1.6); g.add(st);
  }
  /* 老人倚杖 */
  const poet=makeFigure({pose:'独立',robe:0x22202a,belt:0x4a4436,hat:'发髻',beard:true,face:-0.4,scale:1.28,rim:0.4,rimC:0x8a9ab0});
  poet.position.set(-2,0,-3); g.add(poet);
  const staff=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.06,3.6,5),
    new THREE.MeshPhongMaterial({color:0x3a3428}));
  staff.rotation.z=0.12; staff.position.set(-3.1,1.8,-2.4); g.add(staff);
  /* 群童：三四个抱茅跑向竹林（剪影小身影） */
  const kids=makeCrowd({n:4,rect:[2,-4,10,6],seed:763,color:0x181a22,rimC:0x8a9ab0,rim:0.3,sMin:0.6,sMax:0.7});
  g.add(kids.mesh);
  const straws=makeStraws({n:10,seed:765}); straws.position.set(4,1.5,-4); g.add(straws);
  const mist=makeMist({n:6,spread:[170,16,90],pos:[0,7,-32],scale:60,color:0x7c8094,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:16,d:6,color:0x08080b,seed:139,rim:0.11});
  rk.g.position.set(-11,-1.3,9); g.add(rk.g);
  addLights(g,{c:0x8a90a4,i:0.28,p:[30,60,30]},{c:0x22242e,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    poet.update(t,k); kids.update(t); straws.rotation.y=t*0.5; rk.update(t,k);
  }};
}
function bWulou(){ // 三 · 屋漏夜雨 —— 风定云墨、雨脚如麻的长夜（冷雨滴线）
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x08080c,c2:0x0f0f14});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:26,layers:2,peaks:3,seed:771,color:0x090a0f,atmo:0x242634,fogK:0.56,glowK:0.03});
  g.add(ridge.g);
  /* 屋（更近更破）+ 床（室内暗位示意） */
  const hut=makeHutBroken({scale:1.5}); hut.position.set(0,0,-7); hut.rotation.y=0.2; g.add(hut);
  /* 雨脚如麻：密雨滴线（长条雨，NormalBlending 淡灰） */
  const rain=makeGlow({n:320,box:[120,34,80],pos:[0,18,-12],color:0x9aa4b4,size:4.5,speed:0.55,rise:1,maxA:0.5,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  /* 墨云压顶 */
  const dark=makeMist({n:8,spread:[240,20,120],pos:[0,34,-56],scale:92,color:0x14161e,op:0.4});
  g.add(dark.g);
  /* 屋内一点暖（娇儿+破被的位置感） */
  const warm=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc88840,
    transparent:true,opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  warm.scale.set(4,4,1); warm.position.set(0.9,1.4,-5.4); warm.renderOrder=2; g.add(warm);
  const mist=makeMist({n:6,spread:[170,16,90],pos:[0,7,-30],scale:58,color:0x7c8094,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:16,d:6,color:0x08080b,seed:141,rim:0.11});
  rk.g.position.set(-11,-1.3,9); g.add(rk.g);
  addLights(g,{c:0x8a90a4,i:0.26,p:[30,60,30]},{c:0x20222c,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rain.update(t); dark.update(t,k); mist.update(t,k); rk.update(t,k);
    warm.material.opacity=k*(0.34*(0.85+0.15*Math.sin(t*2.6)));
  }};
}
function bGuangsha(){ // 四（末境·可点击）· 广厦万间 —— 点击暗夜，千万广厦亮窗庇寒士
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,rise:0};
  const grd=makeGround({r:120,c1:0x08080c,c2:0x0f0f14});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:26,layers:2,peaks:3,seed:781,color:0x090a0f,atmo:0x262a38,fogK:0.56,glowK:0.03});
  ridge.g.position.set(0,0,-70); g.add(ridge.g);
  /* 破屋（近，仍破） */
  const hut=makeHutBroken({scale:1.2}); hut.position.set(-6,0,-4); hut.rotation.y=0.3; g.add(hut);
  const poet=makeFigure({pose:'独立',robe:0x22202a,belt:0x4a4436,hat:'发髻',beard:true,face:0.5,scale:1.22,rim:0.42,rimC:0x8a9ab0});
  poet.position.set(-3.4,0,-1.5); g.add(poet);
  /* 广厦幻影（点击后升起亮窗） */
  const mansion=makeMansion({}); mansion.position.set(0,0,0); mansion.visible=true; g.add(mansion);
  const burst=makeBurst({n:90,color:0xffc878,pos:[0,14,-26]}); g.add(burst.points);
  const rain=makeGlow({n:200,box:[130,30,90],pos:[0,17,-16],color:0x9aa4b4,size:4,speed:0.5,rise:1,maxA:0.36,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  const mist=makeMist({n:7,spread:[200,18,110],pos:[0,8,-40],scale:66,color:0x7c8094,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x08080b,seed:143,rim:0.12});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0x8a90a4,i:0.28,p:[30,60,30]},{c:0x20222c,i:0.68});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.rise=Math.min(1,ctl.rise+dt/2.6);
      ridge.update(t,0); rain.update(t); mist.update(t,k);
      burst.update(t); rk.update(t,k);
      poet.update(t,k);
      /* 广厦升起+亮窗次第亮起 */
      mansion.position.y=(1-ctl.rise)*(-8);
      mansion.userData.wins.forEach(function(w,i){
        w.material.opacity=k*0.75*ctl.rise*(0.62+0.3*Math.sin(t*3+i*1.3))*sstep(i/8,(i+2)/8,ctl.rise);
      });
      rain.mat.uniforms.uMaxA.value=k*(0.36-0.2*ctl.rise);      // 雨渐歇
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.13); pluck(4,0.6,0.11); pluck(5,1.1,0.11);
        const fl=$('#flash'); fl.textContent='大庇天下寒士俱欢颜'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
