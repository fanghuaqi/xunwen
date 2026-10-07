/* ================= 石壕吏 · 五境场景（水墨夜思·乱世变体：暮投夜捉、吏怒妇苦、三男戍边、老妪应役、幽咽独别） ================= */

/* 差吏：持杖怒立（深褐短打+幞头，手持火把可选） */
function makeOfficer(o){
  o=o||{};
  const f=makeFigure({pose:'按剑',robe:o.robe===undefined?0x2a2018:o.robe,belt:0x4a3820,
    hat:'幞头',beard:o.beard===undefined?true:o.beard,face:o.face===undefined?0:o.face,
    scale:o.scale===undefined?1.2:o.scale,rim:o.rim===undefined?0.4:o.rim,
    rimC:o.rimC===undefined?0xc07848:o.rimC,noProp:true});
  const club=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.07,2.6,5),
    new THREE.MeshPhongMaterial({color:0x241a10,shininess:6}));
  club.rotation.z=-0.4; club.position.set(1.0*f.userData.sc||1.2,2.4,0.3);
  const g=new THREE.Group(); g.add(f); g.add(club);
  g.userData.f=f;
  return g;
}

/* 残屋：低矮草顶土屋（合批 1 mesh） */
function makeHutRuined(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(5.2,2.2,4.2); body.translate(0,1.1,0); B.put(body,0x2a241c);
  const roof=new THREE.ConeGeometry(4.4,1.5,4); roof.rotateY(Math.PI/4);
  roof.translate(0,2.9,0); B.put(roof,0x1c1610);
  const door=new THREE.BoxGeometry(0.9,1.5,0.08); door.translate(0.6,0.75,2.14); B.put(door,0x0d0a07);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2c2c30,emissive:0x070709}),{c:o.rimC===undefined?0x7a8a99:o.rimC,i:0.18,p:2.2}));
  const g=new THREE.Group(); g.add(mesh); g.scale.setScalar(s);
  return g;
}

/* 火把：竖杆+火头（照明） */
function makeTorch(o){
  o=o||{};
  const g=new THREE.Group();
  const pole=new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.08,3.6,5),
    new THREE.MeshPhongMaterial({color:0x241a10}));
  pole.position.y=1.8; g.add(pole);
  const fl=makeFlame({h:1.6,w:0.7,planes:2,embers:16,spark:false,light:o.light===undefined?1.1:o.light,
    lightD:o.lightD===undefined?24:o.lightD,wide:0.36,core:0xffd890,outer:0xe07028});
  fl.g.position.y=3.4; g.add(fl.g);
  g.userData.update=fl.update;
  return g;
}

function bCover(){ // 封面 · 乱世暮色
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0a0a0d,c2:0x14151a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0c0d12,atmo:0x3a3440,fogK:0.74,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x08080b,seed:5,rim:0.12});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x7a7e90,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:50,box:[220,36,130],pos:[0,9,-40],color:0x9aa0b0,size:7,speed:0.05,rise:0,maxA:0.32,add:false});
  g.add(motes.points);
  addLights(g,{c:0x8a8ca0,i:0.35,p:[30,70,40]},{c:0x22242c,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bMutou(){ // 一 · 暮投夜捉 —— 暮色投宿，差吏夜来抓人
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a0a0e,c2:0x131419});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:32,layers:2,peaks:4,seed:701,color:0x0b0c11,atmo:0x322e38,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 村舍两间 */
  const hut=makeHutRuined({}); hut.position.set(3,0,-8); hut.rotation.y=-0.2; g.add(hut);
  const hut2=makeHutRuined({scale:0.8}); hut2.position.set(-9,0,-12); g.add(hut2);
  /* 差吏（村口举火把）+ 诗人（投宿背影） */
  const officer=makeOfficer({face:-0.5,scale:1.22}); officer.position.set(-5,0,-3); g.add(officer);
  const torch=makeTorch({}); torch.position.set(-5.8,0,-2.2); g.add(torch);
  const poet=makeFigure({pose:'独立',robe:0x1c2230,hat:'幞头',beard:true,face:0.2,scale:1.2,rim:0.4,rimC:0x8a9ab4});
  poet.position.set(1.5,0,2); g.add(poet);
  const mist=makeMist({n:7,spread:[190,18,100],pos:[0,7,-34],scale:64,color:0x7a7e90,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x08080b,seed:127,rim:0.12});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0x8a8ca0,i:0.32,p:[30,60,30]},{c:0x22242c,i:0.66});
  const pl=new THREE.PointLight(0xff9040,1.2,30); pl.position.set(-5.8,3.4,-2.2); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    officer.userData.f.update(t,k); torch.userData.update(t,k);
    poet.update(t,k); rk.update(t,k);
    pl.intensity=k*(1.2*(0.85+0.15*Math.sin(t*7.0)));
  }};
}
function bLinu(){ // 二（标志性瞬间）· 吏怒妇苦 —— 怒吼与啼哭在夜里对撞
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x090a0d,c2:0x121318});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:28,layers:2,peaks:3,seed:711,color:0x0b0c11,atmo:0x302c36,fogK:0.58,glowK:0.04});
  g.add(ridge.g);
  /* 主体对峙：差吏（举火怒立）vs 门内老妇（啼哭） */
  const officer=makeOfficer({face:-0.9,scale:1.35,rim:0.5}); officer.position.set(-3.2,0,-4); officer.rotation.y=0.5; g.add(officer);
  const torch=makeTorch({light:1.4,lightD:30}); torch.position.set(-2.2,0,-2.6); g.add(torch);
  const hut=makeHutRuined({}); hut.position.set(4,0,-7); hut.rotation.y=0.35; g.add(hut);
  const fume=makeFigure({pose:'独立',robe:0x3a3038,hat:'发髻',face:-0.8,scale:1.1,rim:0.42,rimC:0xb08a90});
  fume.position.set(3.2,0,-4.6); g.add(fume);
  /* 怒声/哭声的两组声弧（红褐对冷灰） */
  const arcsA=[],arcsB=[];
  for(let i=0;i<3;i++){
    const ptsA=[],ptsB=[];
    for(let k2=0;k2<=18;k2++){
      const a=-1.0+k2/18*2.0, r=1.2+i*2.2;
      ptsA.push(new THREE.Vector3(-3.2+Math.sin(a)*r,4.6+Math.cos(a)*r*0.6,-4+Math.cos(a)*r));
      ptsB.push(new THREE.Vector3(3.2+Math.sin(a)*r,3.4+Math.cos(a)*r*0.6,-4.6+Math.cos(a)*r));
    }
    const la=new THREE.Line(new THREE.BufferGeometry().setFromPoints(ptsA),
      new THREE.LineBasicMaterial({color:0xc06038,transparent:true,opacity:0.5,fog:false}));
    const lb=new THREE.Line(new THREE.BufferGeometry().setFromPoints(ptsB),
      new THREE.LineBasicMaterial({color:0x7a8a99,transparent:true,opacity:0.5,fog:false}));
    g.add(la,lb); arcsA.push(la); arcsB.push(lb);
  }
  const mist=makeMist({n:6,spread:[170,16,90],pos:[0,7,-30],scale:60,color:0x7a7e90,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:16,d:6,color:0x08080b,seed:129,rim:0.11});
  rk.g.position.set(-11,-1.3,9); g.add(rk.g);
  addLights(g,{c:0x8a8ca0,i:0.28,p:[30,60,30]},{c:0x22242c,i:0.66});
  const pl=new THREE.PointLight(0xff9040,1.4,28); pl.position.set(-2.2,3.4,-2.6); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    officer.userData.f.update(t,k); torch.userData.update(t,k); fume.update(t,k);
    rk.update(t,k);
    pl.intensity=k*(1.4*(0.85+0.15*Math.sin(t*8.2)));
    for(let i=0;i<3;i++){
      const phA=((t*0.55)+i/3)%1, phB=((t*0.4)+i/3+0.5)%1;
      arcsA[i].material.opacity=k*0.5*Math.sin(phA*Math.PI)*(1-phA*0.5);
      arcsB[i].material.opacity=k*0.5*Math.sin(phB*Math.PI)*(1-phB*0.5);
      arcsA[i].scale.setScalar(0.6+phA*0.8); arcsB[i].scale.setScalar(0.6+phB*0.8);
    }
  }};
}
function bSannan(){ // 三 · 三男戍边 —— 老妇致词：三男戍，二男死
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x08090c,c2:0x101118});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:26,layers:2,peaks:3,seed:721,color:0x0a0b10,atmo:0x2c2a34,fogK:0.58,glowK:0.04});
  g.add(ridge.g);
  /* 屋内一点昏灯（老妇泣诉处） */
  const hut=makeHutRuined({}); hut.position.set(0,0,-6); g.add(hut);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc88840,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(5,5,1); lamp.position.set(0.8,1.5,-4.2); lamp.renderOrder=2; g.add(lamp);
  const pl=new THREE.PointLight(0xc88840,1.1,26); pl.position.set(0.8,1.6,-4); g.add(pl);
  /* 远处战火微光（邺城方向，天边一抹暗红） */
  const war=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8a3020,
    transparent:true,opacity:0.4,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  war.scale.set(90,34,1); war.position.set(30,16,-110); war.renderOrder=-7; g.add(war);
  /* 三顶征盔（一还二留——两个战死者） */
  for(let i=0;i<3;i++){
    const helm=new THREE.Mesh(new THREE.SphereGeometry(0.45,8,6),
      new THREE.MeshPhongMaterial({color:i===0?0x2c3038:0x101216,shininess:16,specular:0x3a4048}));
    helm.scale.set(1.15,0.8,1.15); helm.position.set(-6+i*1.4,0.35,2+i*0.4); g.add(helm);
  }
  const mist=makeMist({n:7,spread:[190,18,100],pos:[0,7,-34],scale:64,color:0x7a7e90,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x08080b,seed:131,rim:0.12});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0x8a8ca0,i:0.3,p:[30,60,30]},{c:0x22242c,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    rk.update(t,k);
    lamp.material.opacity=k*(0.5*(0.82+0.18*Math.sin(t*3.4)));
    pl.intensity=k*(1.1*(0.85+0.15*Math.sin(t*3.4)));
    war.material.opacity=k*(0.36+0.08*Math.sin(t*1.1));
  }};
}
function bLaoyu(){ // 四 · 老妪应役 —— 老妇自请夜归，随吏远去
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x090a0d,c2:0x111218});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:30,layers:2,peaks:4,seed:731,color:0x0a0b10,atmo:0x2e2c36,fogK:0.58,glowK:0.04});
  g.add(ridge.g);
  /* 村舍（窗内婴儿襁褓微光） */
  const hut=makeHutRuined({}); hut.position.set(-4,0,-7); g.add(hut);
  const crib=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8b870,
    transparent:true,opacity:0.4,depthWrite:false,blending:THREE.AdditiveBlending}));
  crib.scale.set(2.4,2.4,1); crib.position.set(-3.4,1.2,-5.0); g.add(crib);
  /* 主体：差吏前导、老妪随行远去（背影渐远） */
  const officer=makeOfficer({face:0.1,scale:1.25}); officer.position.set(0,0,-6); officer.rotation.y=-0.15; g.add(officer);
  const torch=makeTorch({light:1.2}); torch.position.set(0.9,0,-4.8); g.add(torch);
  const fume=makeFigure({pose:'独立',robe:0x3a3038,hat:'发髻',face:0.0,scale:1.02,rim:0.36,rimC:0xb08a90});
  fume.position.set(1.6,0,-7.4); g.add(fume);
  const mist=makeMist({n:7,spread:[190,18,100],pos:[0,7,-36],scale:64,color:0x7a7e90,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x08080b,seed:133,rim:0.12});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0x8a8ca0,i:0.3,p:[30,60,30]},{c:0x22242c,i:0.66});
  const pl=new THREE.PointLight(0xff9040,1.3,30); pl.position.set(0.9,3.4,-4.8); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k);
    officer.userData.f.update(t,k); torch.userData.update(t,k); fume.update(t,k);
    rk.update(t,k);
    crib.material.opacity=k*(0.4*(0.8+0.2*Math.sin(t*2.8)));
    pl.intensity=k*(1.3*(0.85+0.15*Math.sin(t*7.4)));
  }};
}
function bYouye(){ // 五（末境·可点击）· 幽咽独别 —— 天明登前途，独与老翁别（点击：天光渐亮）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,dawn:0};
  const grd=makeGround({r:120,c1:0x0a0a0e,c2:0x14151a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:30,layers:3,peaks:4,seed:741,color:0x0b0c11,atmo:0x343440,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  const hut=makeHutRuined({}); hut.position.set(-3,0,-8); g.add(hut);
  /* 独行的诗人（前路）与留下来的老翁 */
  const poet=makeFigure({pose:'独立',robe:0x1c2230,hat:'幞头',beard:true,face:-0.3,scale:1.25,rim:0.42,rimC:0x8a9ab4});
  poet.position.set(2,0,1); g.add(poet);
  const oldman=makeFigure({pose:'独立',robe:0x3a3428,hat:'发髻',beard:true,face:0.3,scale:1.05,rim:0.32,rimC:0x8a9ab4});
  oldman.position.set(-2.5,0,-4); g.add(oldman);
  /* 天光（点击后渐亮：夜去天明） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8c8a8,
    transparent:true,opacity:0.6,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(160,70,1); dawn.position.set(-40,26,-110); dawn.renderOrder=-7; g.add(dawn);
  const mist=makeMist({n:7,spread:[190,18,100],pos:[0,7,-34],scale:64,color:0x7a7e90,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x08080b,seed:135,rim:0.12});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  addLights(g,{c:0x8a8ca0,i:0.3,p:[30,60,30]},{c:0x22242c,i:0.66});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.dawn=Math.min(1,ctl.dawn+dt/3.0);
      ridge.update(t,0); mist.update(t,k);
      poet.update(t,k); oldman.update(t,k); rk.update(t,k);
      dawn.material.opacity=k*0.6*(0.33+0.57*ctl.dawn);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0.1,0.12); pluck(2,0.8,0.1);
        const fl=$('#flash'); fl.textContent='独与老翁别'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
