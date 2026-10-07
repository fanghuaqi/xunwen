/* ================= 月夜忆舍弟 · 四境场景（水墨夜思·忆弟变体：戍鼓雁声、露白月明、兄弟分散、寄书不达） ================= */

/* 孤雁：单只掠空（同次北固山下的雁但单飞） */
function makeSingleGoose(o){
  o=o||{};
  const g=new THREE.Group();
  const bmat=new THREE.MeshPhongMaterial({color:o.color===undefined?0x181c24:o.color,
    side:THREE.DoubleSide,shininess:10,specular:0x2c3644,emissive:0x05070c});
  const body=new THREE.SphereGeometry(0.5,8,6); body.scale(2.0,0.85,0.95); g.add(body);
  const neck=new THREE.CylinderGeometry(0.1,0.16,0.9,6); neck.rotateZ(1.1); neck.translate(1.0,0.35,0); g.add(neck);
  const head=new THREE.SphereGeometry(0.24,7,5); head.translate(1.5,0.7,0); g.add(head);
  const wgeo=new THREE.PlaneGeometry(2.4,0.7); wgeo.rotateY(Math.PI/2);
  const w1=new THREE.Mesh(wgeo,bmat); w1.position.x=-0.15;
  const w2=new THREE.Mesh(wgeo,bmat); w2.position.x=-0.15;
  g.add(w1,w2);
  g.userData.w1=w1; g.userData.w2=w2;
  g.scale.setScalar(o.scale===undefined?1.3:o.scale);
  return g;
}

function bCover(){ // 封面 · 白露边秋
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x08090d,c2:0x101319});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:28,layers:2,peaks:4,seed:41,color:0x090b11,atmo:0x26303f,fogK:0.74,glowK:0.08,y:-13});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x050609,seed:5,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:12,spread:[260,40,170],pos:[0,12,-60],scale:85,color:0x8a9ab4,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,36,130],pos:[0,9,-40],color:0xa8b6cc,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0x8c9cc0,i:0.4,p:[30,70,40]},{c:0x1e2432,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}
function bShugu(){ // 一 · 戍鼓雁声 —— 戍楼更鼓、孤雁掠空
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x07080c,c2:0x0f1218});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:36,layers:3,peaks:5,seed:601,color:0x080a10,atmo:0x243040,fogK:0.60,glowK:0.07});
  g.add(ridge.g);
  /* 戍楼与鼓 */
  const tower=new THREE.Mesh(new THREE.BoxGeometry(5.5,11,4.4),
    new THREE.MeshPhongMaterial({color:0x12151c,shininess:5}));
  tower.position.set(-11,5.5,-16); g.add(tower);
  const roof=new THREE.Mesh(new THREE.ConeGeometry(4.4,1.7,4),
    new THREE.MeshPhongMaterial({color:0x181420,shininess:5}));
  roof.rotation.y=Math.PI/4;
  roof.position.set(-11,11.8,-16); g.add(roof);
  const drum=new THREE.Mesh(new THREE.CylinderGeometry(1.3,1.3,0.9,14),
    new THREE.MeshPhongMaterial({color:0x3a2420,shininess:14}));
  drum.rotation.z=Math.PI/2; drum.position.set(-11,10.2,-13.6); g.add(drum);
  /* 空街（断人行：无人的石板路） */
  const street=new THREE.Mesh(new THREE.BoxGeometry(3.2,0.06,60),
    new THREE.MeshPhongMaterial({color:0x0e1118,shininess:10,specular:0x1e2836}));
  street.position.set(2,0.03,-10); g.add(street);
  /* 孤雁一声掠过（缓慢横飞） */
  const goose=makeSingleGoose({}); goose.position.set(0,14,-30); g.add(goose);
  /* 白露初凝（草尖冷光点点） */
  const dew=makeGlow({n:70,box:[70,2.4,50],pos:[0,0.9,-10],color:0xcdd8e8,size:3.6,speed:0.02,rise:0,maxA:0.4});
  g.add(dew.points);
  const mist=makeMist({n:7,spread:[200,20,110],pos:[0,8,-42],scale:68,color:0x8a9ab4,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x050609,seed:109,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x8c9cc0,i:0.44,p:[-40,90,-40]},{c:0x1e2432,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); dew.update(t); mist.update(t,k); rk.update(t,k);
    goose.position.x=((t*1.2)%70)-35;
    goose.position.y=14+Math.sin(t*0.7)*1.2;
    goose.rotation.y=Math.PI/2;
    const f=Math.sin(t*5)*0.42;
    goose.userData.w1.rotation.x=f; goose.userData.w2.rotation.x=-f;
  }};
}
function bLubai(){ // 二（标志性瞬间）· 露白月明 —— 两轮月：他乡之月与故乡之月
  const g=new THREE.Group();
  /* 露夜草坡 */
  const grd=makeGround({r:130,c1:0x090a0e,c2:0x12141a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:30,layers:2,peaks:4,seed:611,color:0x080a10,atmo:0x263040,fogK:0.58,glowK:0.06});
  g.add(ridge.g);
  /* 他乡之月（画面正上方，清冷常规亮） */
  /* 故乡之月（远处山那边，更暖更亮——思念的移情） */
  const halo2=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffe0b0,
    transparent:true,opacity:0.34,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  halo2.scale.set(60,60,1); halo2.position.set(34,40,-110); halo2.renderOrder=-7; g.add(halo2);
  /* 草尖露珠成片（今夜白） */
  const dew=makeGlow({n:130,box:[90,3,60],pos:[0,0.9,-14],color:0xdde6f2,size:3.8,speed:0.02,rise:0,maxA:0.5});
  g.add(dew.points);
  /* 望月人（独立背影） */
  const poet=makeFigure({pose:'独立',robe:0x1a2030,belt:0x6a5a33,hat:'幞头',beard:true,face:0.05,scale:1.3,rim:0.52,rimC:0x9db4c8});
  poet.position.set(0,0,-4); g.add(poet);
  const mist=makeMist({n:8,spread:[220,22,120],pos:[0,9,-46],scale:74,color:0x8a9ab4,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x050609,seed:111,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x9aaccc,i:0.5,p:[-40,110,-40]},{c:0x1e2432,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); dew.update(t); mist.update(t,k);
    poet.update(t,k); rk.update(t,k);
    /* 故乡之月光晕随 stageT 渐显（移情：想着想着就亮了） */
    halo2.material.opacity=k*0.34*sstep(4,14,stageT)*0.99;
  }};
}
function bFensan(){ // 三 · 兄弟分散 —— 四方离散的身影，无家可问
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x07080b,c2:0x0f1117});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:32,layers:2,peaks:5,seed:621,color:0x080a10,atmo:0x222c3a,fogK:0.58,glowK:0.05});
  g.add(ridge.g);
  /* 战乱后的荒村断墙 */
  [[-16,-22,7,6],[4,-30,10,8],[20,-20,6,5]].forEach(function(p,i){
    const ru=new THREE.Mesh(new THREE.BoxGeometry(p[3],p[2],p[3]*0.5),
      new THREE.MeshPhongMaterial({color:0x111318,shininess:4}));
    ru.rotation.z=(i%2?-0.06:0.05); ru.position.set(p[0],p[2]/2-0.4,p[1]); g.add(ru);
  });
  /* 四方离散的身影（远处各自东西的剪影） */
  const walkers=makeCrowd({n:9,rect:[-36,-34,72,16],seed:631,color:0x131820,rimC:0x8a9ab4,rim:0.3,sMin:0.75,sMax:1.05});
  g.add(walkers.mesh);
  /* 断雁再掠（呼应首句） */
  const goose=makeSingleGoose({scale:1.1}); goose.position.set(10,13,-38); g.add(goose);
  const mist=makeMist({n:8,spread:[230,20,120],pos:[0,9,-48],scale:74,color:0x8a9ab4,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x050609,seed:113,rim:0.14});
  rk.g.position.set(-14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x8292b4,i:0.4,p:[-40,80,-40]},{c:0x1a2030,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); walkers.update(t); mist.update(t,k); rk.update(t,k);
    goose.position.x=10-((t*1.0)%50);
    goose.position.y=13+Math.sin(t*0.6)*1.0;
    goose.rotation.y=-Math.PI/2;
    const f=Math.sin(t*5.4)*0.4;
    goose.userData.w1.rotation.x=f; goose.userData.w2.rotation.x=-f;
  }};
}
function bJishu(){ // 四（末境·可点击）· 寄书不达 —— 点击故乡月，月转明、家书化作雁影
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,bright:0};
  const grd=makeGround({r:130,c1:0x08090d,c2:0x10131a});
  grd.mesh.position.y=-1.5; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:30,layers:3,peaks:5,seed:641,color:0x080a10,atmo:0x263040,fogK:0.58,glowK:0.06});
  ridge.g.position.set(0,0,-64); g.add(ridge.g);
  /* 望月人 */
  const poet=makeFigure({pose:'指月',robe:0x1a2030,belt:0x6a5a33,hat:'幞头',beard:true,face:0.35,scale:1.32,rim:0.55,rimC:0x9db4c8});
  poet.position.set(-2,0,-5); g.add(poet);
  /* 家书化作雁影（点击后飞向山月） */
  const goose=makeSingleGoose({scale:1.0}); goose.position.set(2,6,-18); g.add(goose);
  const burst=makeBurst({n:70,color:0xffe0b0,pos:[2,8,-16]}); g.add(burst.points);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffe0b0,
    transparent:true,opacity:0.3,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(3,3,1); g.add(glow);
  const dew=makeGlow({n:100,box:[70,3,44],pos:[0,0.9,-10],color:0xdde6f2,size:3.6,speed:0.02,rise:0,maxA:0.3});
  g.add(dew.points);
  /* 故乡月之光晕（山那边，点击后转明） */
  const moonHalo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffe2b8,
    transparent:true,opacity:0.48,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  moonHalo.scale.set(56,56,1); moonHalo.position.set(34,38,-108); moonHalo.renderOrder=-7; g.add(moonHalo);
  const mist=makeMist({n:7,spread:[210,20,110],pos:[0,8,-44],scale:70,color:0x8a9ab4,op:0.09});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x050609,seed:115,rim:0.14});
  rk.g.position.set(-12,-1.4,11); g.add(rk.g);
  addLights(g,{c:0x9aaccc,i:0.46,p:[-40,100,-40]},{c:0x1e2432,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.bright=Math.min(1,ctl.bright+dt/2.6);
      ridge.update(t,0); dew.update(t); mist.update(t,k);
      burst.update(t); rk.update(t,k);
      poet.update(t,k);
      /* 雁影驮书：点击后向山月方向远去 */
      goose.position.set(2+ctl.bright*20,6+ctl.bright*16,-18-ctl.bright*36);
      const f=ctl.bright>0?Math.sin(t*7)*0.45:Math.sin(t*3)*0.2;
      goose.userData.w1.rotation.x=f; goose.userData.w2.rotation.x=-f;
      glow.position.copy(goose.position);
      glow.material.opacity=k*(0.3*Math.min(1,ctl.bright*3));
      /* 山月亮起（故乡月明） */
      moonHalo.material.opacity=k*0.48*(0.25+0.66*ctl.bright)*(0.92+0.08*Math.sin(t*1.1));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.13); pluck(4,0.6,0.11);
        const fl=$('#flash'); fl.textContent='月是故乡明'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
