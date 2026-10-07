/* ================= 江城子·密州出猎 · 三境场景（夜宴金彩·出猎变体：出猎卷冈、酒酣胸胆、会挽雕弓） ================= */

/* 雕弓：弯曲拱弧 + 弓弦（合批 1 mesh） */
function makeBow(o){
  o=o||{};
  const B=new GeoBag();
  const pts=[];
  for(let i=0;i<=16;i++){
    const a=-1.2+i/16*2.4;
    pts.push(new THREE.Vector3(Math.cos(a)*2.0-0.8,Math.sin(a)*2.8,0));
  }
  const crv=new THREE.CatmullRomCurve3(pts);
  const body=new THREE.TubeGeometry(crv,16,0.06,5,false); B.put(body,0x8a5a22);
  const string=limbGeo(pts[0].toArray(),pts[pts.length-1].toArray(),0.015,0.015,4);
  B.put(string,0xe8d0a0);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x8a7040,emissive:0x100a04}),{c:o.rimC===undefined?0xd9a050:o.rimC,i:0.3,p:2.5}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

function bCover(){ // 封面 · 密州暮原
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x06080e,c2:0x141a26});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:32,layers:2,peaks:4,seed:41,color:0x070b13,atmo:0x2b3f5e,fogK:0.74,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x04060b,seed:5,rim:0.16});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x9db8dc,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:70,box:[220,40,130],pos:[0,10,-40],color:0xd9c890,size:8,speed:0.05,rise:0,maxA:0.5});
  g.add(motes.points);
  addLights(g,{c:0xb8a888,i:0.4,p:[30,70,40]},{c:0x2a241a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bChulie(){ // 一（标志性瞬间）· 出猎卷冈 —— 左牵黄、右擎苍，千骑卷平冈
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x0a0c12,c2:0x181c24});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  /* 平冈：平缓起伏的山脊（卷平冈） */
  const ridge=makeRange({r:220,h:38,layers:3,peaks:5,seed:951,color:0x0c1018,atmo:0x344258,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 千骑卷冈：奔腾的骑队剪影 */
  const army=makeCrowd({n:18,rect:[-30,-32,60,14],seed:953,color:0x161a22,rimC:0xd9a050,rim:0.32,sMin:0.8,sMax:1.1});
  g.add(army.mesh);
  /* 主体：密州太守（锦帽貂裘，英武立姿） */
  const boss=makeFigure({pose:'指月',robe:0x3a2216,belt:0x8a6020,hat:'幞头',beard:true,face:0.1,scale:1.42,rim:0.68,rimC:0xffc050,noProp:true});
  boss.position.set(0,0,-4); g.add(boss);
  /* 右臂苍鹰（小飞鸟合批） */
  const eagle=new THREE.Mesh(new THREE.ConeGeometry(0.25,0.7,5),
    new THREE.MeshPhongMaterial({color:0x201610,shininess:12}));
  eagle.position.set(1.4,4.2,-3.6); eagle.rotation.z=-0.3; g.add(eagle);
  /* 左手黄犬（小猎犬剪影） */
  const dog=new THREE.Mesh(new THREE.BoxGeometry(1.6,0.7,0.6),
    new THREE.MeshPhongMaterial({color:0x8a6030,shininess:8}));
  dog.position.set(-1.6,0.4,-3.2); dog.rotation.y=0.2; g.add(dog);
  /* 出猎飞卷扬尘 */
  const dust=makeFlow({n:500,box:[180,20,110],pos:[0,8,-24],color:0xb89050,size:20,speed:8.0,maxA:0.32});
  g.add(dust.points);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-42],scale:72,color:0x8a98b0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x05070c,seed:167,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xc09858,i:0.46,p:[-40,80,-40]},{c:0x222634,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); army.update(t); dust.update(t); mist.update(t,k);
    boss.update(t,k); rk.update(t,k);
    eagle.position.y=4.2+Math.sin(t*1.6)*0.04;
  }};
}
function bJiuhan(){ // 二 · 酒酣胸胆 —— 酒酣胸胆尚开张，鬓微霜，又何妨
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x080a10,c2:0x161c28});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:200,h:32,layers:2,peaks:4,seed:961,color:0x0a0d14,atmo:0x2c384c,fogK:0.60,glowK:0.06});
  g.add(ridge.g);
  /* 庆功大帐 + 篝火烈焰 */
  const braz=makeBrazier({r:1.2,fh:2.8,fw:1.4,light:1.6,lightD:46,embers:26,spark:true});
  braz.g.position.set(-6,0,-4); g.add(braz.g);
  /* 长案 + 金樽 */
  const tb=makeTable({w:8,d:3.0,h:1.45,wood:0x2a1c12}); tb.g.position.set(0,0,-4); g.add(tb.g);
  const zun=makeVessel({type:'樽',mat:'金',scale:1.0,liquid:true}); zun.g.position.set(1.4,1.45,-4.2); g.add(zun.g);
  /* 太守豪饮（两鬓微白，豪气开张） */
  const boss=makeFigure({pose:'举杯',robe:0x3a2216,belt:0x8a6020,hat:'幞头',hair:0xb0b8c4,beard:true,
    face:0.1,scale:1.35,rim:0.6,rimC:0xffd060,noProp:true});
  boss.position.set(0,0,-6); g.add(boss);
  const army=makeCrowd({n:10,rect:[-18,-24,36,8],seed:963,color:0x141822,rimC:0xd9a050,rim:0.28,sMin:0.8,sMax:1.05});
  g.add(army.mesh);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-40],scale:70,color:0x8a98b0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x05070c,seed:169,rim:0.14});
  rk.g.position.set(-13,-1.4,11); g.add(rk.g);
  addLights(g,{c:0xc89050,i:0.44,p:[30,60,-20]},{c:0x202432,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); braz.update(t,k); army.update(t); mist.update(t,k);
    boss.update(t,k); zun.update(t,k); rk.update(t,k);
  }};
}
function bShetianlang(){ // 三（末境·可点击）· 会挽雕弓 —— 雕弓如满月，西北望射天狼（点击：弓挽箭发，天狼爆星）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,shot:0};
  const grd=makeGround({r:130,c1:0x080a12,c2:0x141a26});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:230,h:42,layers:3,peaks:5,seed:971,color:0x090c14,atmo:0x28344c,fogK:0.58,glowK:0.07});
  ridge.g.position.set(0,0,-76); g.add(ridge.g);
  /* 西北天狼星（高天冷白亮星，点击后爆散） */
  const star=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb0d8ff,
    transparent:true,opacity:0.85,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  star.scale.set(12,12,1); star.position.set(-42,48,-120); star.renderOrder=-6; g.add(star);
  /* 太守挽弓（手持雕弓，瞄向西北高空） */
  const boss=makeFigure({pose:'指月',robe:0x3a2216,belt:0x8a6020,hat:'幞头',beard:true,face:-0.4,scale:1.4,rim:0.68,rimC:0xffd060,noProp:true});
  boss.position.set(0,0,-4); g.add(boss);
  const bow=makeBow({scale:1.15}); bow.position.set(-1.2,2.8,-3.4); bow.rotation.y=-0.35; bow.rotation.z=-0.4; g.add(bow);
  /* 破空飞矢（点击后飞向天狼） */
  const arrow=new THREE.Mesh(new THREE.CylinderGeometry(0.04,0.04,3.2,5),
    new THREE.MeshPhongMaterial({color:0xffd060,emissive:0x8a5010}));
  arrow.rotation.z=0.75; arrow.rotation.y=-0.35; arrow.position.set(-1.2,2.8,-3.4); arrow.visible=false; g.add(arrow);
  const burst=makeBurst({n:110,color:0xffd060,pos:[-42,48,-120]}); g.add(burst.points);
  const mist=makeMist({n:7,spread:[220,20,110],pos:[0,8,-44],scale:72,color:0x8a98b0,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x05070c,seed:171,rim:0.15});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xa8bcc8,i:0.48,p:[-50,90,-40]},{c:0x1e2432,i:0.62});
  const pl=new THREE.PointLight(0xffb040,2.0,40); pl.position.set(0,6,-4); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.shot=Math.min(1,ctl.shot+dt/1.6);
      ridge.update(t,0); mist.update(t,k); boss.update(t,k); rk.update(t,k);
      burst.update(t);
      star.material.opacity=k*(0.85*(1-ctl.shot*0.9))*(0.8+0.2*Math.sin(t*8));
      if(ctl.shot>0){
        arrow.visible=true;
        arrow.position.set(-1.2-ctl.shot*40, 2.8+ctl.shot*45, -3.4-ctl.shot*116);
      }
      pl.intensity=k*2.0*(0.55+ctl.shot*0.35*(0.85+0.15*Math.sin(t*3.0)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.15); pluck(4,0.4,0.13); pluck(5,0.8,0.13); bell();
        const fl=$('#flash'); fl.textContent='西北望 · 射天狼'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
