/* ================= 行路难 · 四境场景（夜宴金彩·行路变体：盛宴停杯、冰塞雪满、溪钓梦日、云帆济海） ================= */

/* 帆船：船体（弯盒壳）+ 桅杆 + 大帆（可满张） */
function makeSailBoat(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const hullC=o.hull===undefined?0x241708:o.hull, sailC=o.sail===undefined?0xe8dcc0:o.sail;
  const g=new THREE.Group();
  const B=new GeoBag();
  const hull=new THREE.CylinderGeometry(1.0,0.55,6.2,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.55,1.6); B.put(hull,hullC);
  const bow=new THREE.ConeGeometry(0.75,1.8,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.75,1.5); bow.translate(3.9,0.1,0); B.put(bow,hullC);
  const deck=new THREE.BoxGeometry(4.6,0.14,1.5); deck.translate(0,0.62,0); B.put(deck,shadeColor(hullC,1.4));
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a3a22,emissive:0x0a0703}),{c:o.rimC===undefined?0xd8a860:o.rimC,i:0.3,p:2.5})));
  const mast=new THREE.Mesh(new THREE.CylinderGeometry(0.07,0.10,6.4,6),
    new THREE.MeshPhongMaterial({color:0x2e2012,shininess:8}));
  mast.position.set(-0.4,3.4,0); g.add(mast);
  /* 大帆：梯形布帆（顶边收窄）+ 帆骨横条 + 包边，斜对镜头读得出"帆" */
  const yard=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.05,3.4,5),
    new THREE.MeshPhongMaterial({color:0x2e2012}));
  yard.rotation.z=Math.PI/2; yard.position.set(-0.3,5.9,0); g.add(yard);
  const sailGeo=new THREE.PlaneGeometry(4.6,5.4,1,4);
  (function(){                       // 顶两排顶点内收 → 梯形
    const p=sailGeo.attributes.position;
    for(let i=0;i<p.count;i++){
      const y=p.getY(i);
      if(y>1.3)p.setX(i,p.getX(i)*0.55);
      else if(y>0)p.setX(i,p.getX(i)*0.78);
    }
    sailGeo.computeVertexNormals();
  })();
  const sail=new THREE.Mesh(sailGeo,new THREE.MeshPhongMaterial({color:sailC,side:THREE.DoubleSide,
    shininess:6,specular:0x9a8a66,emissive:0x201c14}));
  sail.position.set(-0.3,3.05,0); g.add(sail);
  const B2=new GeoBag();
  for(let i=0;i<4;i++){              // 帆骨
    const b=new THREE.CylinderGeometry(0.035,0.035,4.6*(1-i*0.11),5);
    b.rotateZ(Math.PI/2); b.translate(-0.3,0.9+i*1.35,0.05); B2.put(b,0x3a2818);
  }
  const boom=new THREE.CylinderGeometry(0.045,0.045,3.0,5);
  boom.rotateZ(Math.PI/2); boom.translate(-0.3,0.42,0.05); B2.put(boom,0x3a2818);
  g.add(B2.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a22,emissive:0x0a0703}),{c:o.rimC===undefined?0xd8a860:o.rimC,i:0.3,p:2.5})));
  g.userData.sail=sail; g.userData.mast=mast;
  g.scale.setScalar(s);
  return g;
}

/* 箸：一双细筷搁在箸架（合批 1 mesh） */
function makeChopsticks(){
  const B=new GeoBag();
  [-0.09,0.09].forEach(function(z){
    const ch=new THREE.CylinderGeometry(0.028,0.02,1.5,5);
    ch.rotateZ(Math.PI/2); ch.translate(0,0.05,z); B.put(ch,0x4a3018);
  });
  const rest=new THREE.BoxGeometry(0.5,0.1,0.28); rest.translate(0,0.02,0); B.put(rest,0x6a4522);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:20,
    specular:0x6a4a2a,emissive:0x080502}),{c:0xd8a860,i:0.3,p:2.6}));
  return mesh;
}

/* 浮冰：几块青白低多边形冰排 */
function makeIceFloes(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?41:o.seed);
  const g=new THREE.Group();
  for(let i=0;i<(o.n===undefined?6:o.n);i++){
    const w=2.4+R()*3.6, d=1.8+R()*2.4, h=0.5+R()*0.5;
    const ice=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),
      new THREE.MeshPhongMaterial({color:0xbfd4dd,shininess:52,specular:0xeaf6fc,emissive:0x0c141a}));
    ice.position.set((R()-0.5)*(o.w===undefined?60:o.w),-0.1,(R()-0.5)*(o.d===undefined?40:o.d));
    ice.rotation.y=R()*6.283; g.add(ice);
  }
  return g;
}

function bCover(){ // 封面 · 金樽夜色
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x06080e,c2:0x141a26});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:30,layers:2,peaks:4,seed:41,color:0x070b13,atmo:0x2b3f5e,fogK:0.74,glowK:0.10,y:-14});
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
function bJinzun(){ // 一 · 停杯投箸 —— 盛宴在前却停杯拔剑（盛宴与茫然的强反差）
  const g=new THREE.Group();
  const grd=makeGround({r:95,c1:0x080605,c2:0x1e150c}); g.add(grd.mesh);
  /* 背景：帷帐 + 亭柱 + 远山 */
  const ridge=makeRange({r:180,h:40,layers:2,peaks:4,seed:251,color:0x0a0807,atmo:0x3a3020,fogK:0.64,glowK:0.09,y:-14});
  ridge.g.position.set(0,0,-48); g.add(ridge.g);
  const curt=makeCurtain({w:44,h:12,color:0x2c1210,folds:12,deep:0.7});
  curt.g.position.set(0,0,-24); g.add(curt.g);
  [-15,15].forEach(function(x){
    const p=makePillar({h:11.5,r:0.4,color:0x241408,top:false});
    p.g.position.set(x,0,-9); g.add(p.g);
  });
  /* 中景：盛宴长案（金樽清酒 + 玉盘珍羞 + 停下的杯与投下的箸） */
  const tb=makeTable({w:11,d:3.4,h:1.5,wood:0x30201a}); tb.g.position.set(0,0,-0.5); g.add(tb.g);
  const zun=makeVessel({type:'樽',mat:'金',scale:1.0,liquid:true}); zun.g.position.set(-3.4,1.5,-1.0); g.add(zun.g);
  const jadePlate=makeVessel({type:'盘',mat:'玉',scale:1.15}); jadePlate.g.position.set(-0.6,1.5,-0.8); g.add(jadePlate.g);
  const d1=makeDish({r:0.72,n:5}); d1.g.position.set(2.2,1.5,-0.9); g.add(d1.g);
  const d2=makeDish({r:0.6,n:4,plate:0x5a4a3a}); d2.g.position.set(3.8,1.5,-1.4); g.add(d2.g);
  const cup=makeVessel({type:'杯',mat:'金',scale:0.9}); cup.g.position.set(0.2,1.5,0.8); cup.g.rotation.z=1.25; g.add(cup.g);
  const zhu=makeChopsticks(); zhu.position.set(1.3,1.5,0.5); zhu.rotation.y=0.5; g.add(zhu);
  /* 主体：拔剑四顾者（按剑，环顾姿态） */
  const boss=makeFigure({pose:'按剑',robe:0x30222a,belt:0xa8842f,hat:'幞头',beard:true,face:0.15,scale:1.42,rim:0.66,rimC:0xffd890});
  boss.position.set(-1.2,0,-4.2); g.add(boss);
  const crowd=makeCrowd({n:6,rect:[-15,-13,30,4],seed:261,color:0x181a20,rimC:0xc98a4a,rim:0.24});
  g.add(crowd.mesh);
  /* 灯串 + 火盆 */
  const lans=[];
  [0,1,2].forEach(function(i){
    const l=makeLantern(0.5,{flame:i===0});
    l.position.set(-6+i*6,7.6,-7); g.add(l); lans.push(l);
  });
  const br=makeBrazier({r:1.0,fh:2.3,fw:1.15,light:1.25,lightD:44,embers:22,spark:true});
  br.g.position.set(9,0,3); g.add(br.g);
  /* 茫然雾流：灰金雾缓缓绕行（心茫然） */
  const flow=makeFlow({n:420,box:[130,20,90],pos:[0,11,-16],color:0xb0a080,size:22,speed:2.8,maxA:0.28});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[120,20,80],pos:[0,8,-16],scale:52,color:0xa8886a,op:0.07});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x060504,seed:63,rim:0.15});
  rk.g.position.set(-15,-1.4,9); g.add(rk.g);
  addLights(g,{c:0x9a8568,i:0.32,p:[30,60,40]},{c:0x2e2519,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); crowd.update(t);
    lans.forEach(function(l){l.update(t,k);});
    br.update(t,k); flow.update(t); mist.update(t,k);
    boss.update(t,k); zun.update(t,k); jadePlate.update(t,k); rk.update(t,k);
  }};
}
function bBingshan(){ // 二 · 冰塞雪满 —— 冰封黄河与雪满太行的双重阻隔
  const g=new THREE.Group();
  /* 冰封的大川：静止无波的青白水面 */
  const ice=makeWater({size:620,seg:90,amp:0.12,freq:0.14,speed:0.12,flow:[0.05,0.05],spec:1.9,
    deep:0x14242e,shallow:0x3a5866,skyc:0x54707e,moonDir:[-60,100,-150]});
  g.add(ice.mesh);
  const floes=makeIceFloes({n:9,w:90,d:56,seed:271}); g.add(floes);
  /* 背景：雪满太行（冷雪山脊） */
  const ridge=makeRange({r:220,h:74,layers:3,peaks:5,seed:281,color:0x1a2830,atmo:0x8aa4b2,fogK:0.58,glowK:0.10});
  g.add(ridge.g);
  /* 风雪横流（贴地冷白雾流） */
  const snow=makeFlow({n:650,box:[190,26,120],pos:[0,13,-24],color:0xcfe0ea,size:20,speed:6.0,maxA:0.34});
  g.add(snow.points);
  const motes=makeGlow({n:130,box:[150,20,90],pos:[0,9,-16],color:0xe8f2f8,size:4.5,speed:0.14,rise:1,maxA:0.42});
  g.add(motes.points);
  /* 前景：雪岩 + 冰凌石 */
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x1a242c,seed:87,rim:0.2,rimC:0xbfd8e4});
  rk.g.position.set(-15,-1.5,12); g.add(rk.g);
  const rk2=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:7,color:0x1a242c,seed:89,rim:0.18,rimC:0xbfd8e4});
  rk2.g.position.set(15,-1.3,11); g.add(rk2.g);
  const mist=makeMist({n:8,spread:[220,24,120],pos:[0,9,-44],scale:72,color:0x8aa4b4,op:0.09});
  g.add(mist.g);
  addLights(g,{c:0xaec4d4,i:0.5,p:[-50,90,-40]},{c:0x2a3642,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ice.update(t); ridge.update(t,0); snow.update(t); motes.update(t);
    mist.update(t,k); rk.update(t,k); rk2.update(t,k);
  }};
}
function bDiaoxi(){ // 三 · 溪钓梦日 —— 碧溪垂钓 + 日边行舟（两个典故一静一远）
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a0d08,c2:0x18241a}); g.add(grd.mesh);
  const ridge=makeRange({r:210,h:44,layers:3,peaks:5,seed:291,color:0x0b130d,atmo:0x2c4434,fogK:0.60,glowK:0.09});
  g.add(ridge.g);
  /* 碧溪 */
  const water=makeWater({size:420,seg:80,amp:0.3,freq:0.11,speed:0.6,flow:[0.5,0.2],spec:1.3,
    deep:0x0a1a16,shallow:0x14443a,skyc:0x225448,moonDir:[-60,110,-150]});
  water.mesh.position.set(0,-0.3,-18); g.add(water.mesh);
  /* 溪畔垂钓者：蓑笠翁独立 + 长竿垂线 */
  const fisher=makeFigure({pose:'独立',robe:0x2c3428,belt:0x6a5a34,hat:'发髻',beard:true,face:0.5,scale:1.3,rim:0.55,rimC:0xc8d890});
  fisher.position.set(-6,0,-4); g.add(fisher);
  const rod=new THREE.Mesh(new THREE.CylinderGeometry(0.03,0.05,6.5,5),
    new THREE.MeshPhongMaterial({color:0x2e2012}));
  rod.rotation.z=-0.95; rod.position.set(-3.4,3.6,-3.4); rod.rotation.y=0.2; g.add(rod);
  const line=new THREE.Mesh(new THREE.CylinderGeometry(0.012,0.012,3.2,4),
    new THREE.MeshBasicMaterial({color:0xd8ccb0,transparent:true,opacity:0.6}));
  line.position.set(-1.6,2.4,-3.2); g.add(line);
  const bob=new THREE.Mesh(new THREE.SphereGeometry(0.09,6,5),
    new THREE.MeshBasicMaterial({color:0xd8b050}));
  bob.position.set(-1.6,0.75,-3.2); g.add(bob);
  /* 日边行舟（远处金色小舟剪影 + 低垂日轮） */
  const dreamBoat=new THREE.Mesh(new THREE.CylinderGeometry(1.6,1.0,0.5,10),
    new THREE.MeshPhongMaterial({color:0x6a4a20,emissive:0x2a1a06,shininess:20}));
  dreamBoat.scale.set(1.8,1,0.8); dreamBoat.position.set(26,0.4,-52); g.add(dreamBoat);
  const sun=new THREE.Mesh(new THREE.CircleGeometry(7,32),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xffd070,transparent:true,opacity:0.85,fog:false}));
  sun.position.set(30,26,-92); sun.renderOrder=-7; g.add(sun);
  const sunGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb860,
    transparent:true,opacity:0.5,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sunGlow.scale.set(60,60,1); sunGlow.position.set(30,26,-92); sunGlow.renderOrder=-7; g.add(sunGlow);
  /* 萤火微尘（梦境感） */
  const flies=makeGlow({n:70,box:[90,22,60],pos:[-4,7,-12],color:0xffd98a,size:6,speed:0.05,rise:0,maxA:0.45});
  g.add(flies.points);
  const mist=makeMist({n:7,spread:[200,24,110],pos:[0,9,-42],scale:70,color:0x7fa890,op:0.09});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',w:40,n:16,d:6,color:0x050a06,seed:95,sway:0.9});
  reeds.g.position.set(12,-1.3,11); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:18,d:7,color:0x060a07,seed:97,rim:0.15});
  rk.g.position.set(-14,-1.4,12); g.add(rk.g);
  addLights(g,{c:0xc9b088,i:0.42,p:[-40,80,-40]},{c:0x203024,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); flies.update(t); mist.update(t,k);
    fisher.update(t,k);
    bob.position.y=0.75+0.06*Math.sin(t*2.2);
    dreamBoat.position.y=0.4+0.15*Math.sin(t*0.7);
    sunGlow.material.opacity=k*(0.42+0.1*Math.sin(t*0.9));
    reeds.update(t,k); rk.update(t,k);
  }};
}
function bChangfeng(){ // 四（末境·可点击）· 长风破浪 —— 沧海云帆，点击满张破浪
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,wind:0};
  const sea=makeWater({size:900,seg:110,amp:2.6,freq:0.085,speed:1.4,flow:[0,2.6],spec:1.6,
    deep:0x081a2e,shallow:0x16456e,skyc:0x2c4c74,moonDir:[80,120,-180]});
  g.add(sea.mesh);
  const foam=makeGlow({n:180,box:[110,5,16],pos:[-2,1.8,-13],color:0xd8ecf0,size:5.5,speed:0.9,rise:1,maxA:0.4});
  foam.points.renderOrder=4; g.add(foam.points);
  const ridge=makeRange({r:240,h:40,layers:2,peaks:4,seed:301,color:0x0a1018,atmo:0x2c3e58,fogK:0.60,glowK:0.08,y:-16});
  ridge.g.position.set(0,0,-80); g.add(ridge.g);
  /* 主体：云帆大船（放大拉近，斜对镜头） */
  const boat=makeSailBoat({scale:2.3,rimC:0xffd890});
  boat.position.set(-1.5,1.6,-3); boat.rotation.y=0.6; g.add(boat);
  /* 长风：定向金白风流（点击后提速加亮；粒子收小避免满屏白斑） */
  const wind=makeFlow({n:380,box:[150,22,90],pos:[22,12,-62],color:0xe8dcc0,size:9,speed:7.0,maxA:0.24});
  g.add(wind.points);
  const gold=makeGlow({n:150,box:[110,30,80],pos:[0,6,-18],color:0xffd070,size:11,speed:0.05,rise:1,maxA:0});
  g.add(gold.points);
  const burst=makeBurst({n:110,color:0xffe0a0,pos:[-1.5,12,-3]}); g.add(burst.points);
  const mist=makeMist({n:8,spread:[240,26,140],pos:[0,11,-50],scale:78,color:0x8ea4c4,op:0.09});
  g.add(mist.g);
  /* 前景：浪边礁石 */
  const rk=makeForeground({kind:'坡石',n:3,r:4.2,w:24,d:8,color:0x05070c,seed:101,rim:0.16});
  rk.g.position.set(-16,-1.6,14); g.add(rk.g);
  const rk2=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:7,color:0x05070c,seed:103,rim:0.14});
  rk2.g.position.set(15,-1.4,12); g.add(rk2.g);
  addLights(g,{c:0xaec4ea,i:0.6,p:[-50,110,-50]},{c:0x28304a,i:0.56});
  const pl=new THREE.PointLight(0xffca7a,2.6,60); pl.position.set(-1.5,11,-3); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.wind=Math.min(1,ctl.wind+dt/2.2);
      sea.update(t); ridge.update(t,0); wind.update(t); mist.update(t,k);
      burst.update(t);
      gold.mat.uniforms.uMaxA.value=k*0.6*ctl.wind;
      gold.update(t);
      /* 帆满张：帆面沿风向鼓出 + 船首前倾 + 轻微摇摆 */
      const sail=boat.userData.sail;
      sail.rotation.y=Math.sin(t*1.1)*0.05+ctl.wind*0.22;
      sail.scale.y=1+ctl.wind*0.12;
      boat.rotation.x=-0.03-ctl.wind*0.05+Math.sin(t*0.8)*0.02;
      boat.position.y=1.5+Math.sin(t*0.9)*0.22;
      pl.intensity=k*2.6*(0.54+ctl.wind*0.44*(0.85+0.15*Math.sin(t*3.3)));
      rk.update(t,k); rk2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(2,0.1,0.16); pluck(4,0.5,0.12); pluck(5,0.9,0.12); bell();
        const fl=$('#flash'); fl.textContent='直挂云帆济沧海'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
