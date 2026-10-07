/* ================= 海棠 · 三境场景（夜宴金彩 · 夜庭海棠变体：卷首夜庭、东风香雾、烧烛红妆）
   本诗专属系统「秉烛照花」：夜庭里一树海棠，东风与香雾浮动，月转回廊（月光带在地面缓缓转过）。
   末境点击高烛 → 烛焰亮起、暖光池铺开、海棠"红妆"在夜色中显影（花光次第亮起）。
   与同赛道《过华清宫》《菩萨蛮·小山重叠》不同：本页是夜庭一树海棠与一支高烛。 ================= */

/* —— 海棠：枝干 + 满树红粉花簇（含花蕾），合批 1 mesh；末境靠烛光与花光层「显影」 —— */
function makeCrabappleHT(o){
  o=o||{};
  const h=o.h===undefined?4.4:o.h, R=seedRnd(o.seed===undefined?83:o.seed);
  const wood=o.wood===undefined?0x2a1c14:o.wood;
  const petal=o.petal===undefined?0xe8697e:o.petal, budC=o.bud===undefined?0xb8425c:o.bud;
  const B=new GeoBag(), spots=[];
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.46,0],h*0.075,h*0.03,7),wood);
  const tips=[];
  const nb=o.branches===undefined?7:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.34+R()*0.28);
    const p1=[Math.sin(a)*len, h*0.44+len*0.5, Math.cos(a)*len];
    B.put(limbGeo([0,h*0.44,0],p1,h*0.03,h*0.012,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.85){
      const p2=[p1[0]+Math.sin(a+0.6)*len*0.5, p1[1]+len*0.34, p1[2]+Math.cos(a+0.6)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.015,h*0.006,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    for(let k=0;k<4;k++){
      const cx=tp[0]+(R()-0.5)*1.1, cy=tp[1]+(R()-0.3)*0.8, cz=tp[2]+(R()-0.5)*1.1;
      const pr=0.26+R()*0.13;
      for(let q=0;q<5;q++){
        const aq=q/5*6.283+R()*0.3;
        const pf=new THREE.PlaneGeometry(pr*1.35,pr*0.9);
        pf.rotateZ(aq); pf.rotateX(-0.5+R()*0.9); pf.rotateY(R()*0.6);
        pf.translate(cx+Math.cos(aq)*pr*0.6, cy, cz+Math.sin(aq)*pr*0.6);
        B.put(pf,shadeColor(petal,0.82+R()*0.36));
      }
      const st=new THREE.SphereGeometry(pr*0.22,6,5); st.translate(cx,cy+pr*0.08,cz);
      B.put(st,0xf0d070);
      if(R()<0.5){   /* 花蕾 */
        const bd=new THREE.SphereGeometry(pr*0.42,7,6); bd.scale(1,1.15,1);
        bd.translate(cx+(R()-0.5)*0.8, cy+(R()-0.5)*0.6, cz+(R()-0.5)*0.8);
        B.put(bd,shadeColor(budC,0.85+R()*0.4));
      }
      spots.push([cx,cy,cz]);
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a4a48,emissive:0x1c0a10,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xe8a0a8:o.rimC,i:0.30,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){
    const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.02+0.05*wd)*Math.sin(t*(0.9+1.6*wd)+ph)*kk;
  };
  g.userData.update=g.update;
  return {g,update:g.update,mesh,spots};
}

/* —— 花光：海棠花上的红色花光点（Sprite；末境点亮后次第显影） —— */
function makeFlowerGlowHT(o){
  o=o||{};
  const pos=o.pos||[], g=new THREE.Group(), items=[];
  for(let i=0;i<pos.length;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0xff8a96:o.color,
      transparent:true,opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set(pos[i][0],pos[i][1],pos[i][2]);
    s.scale.set(1.0,1.0,1); s.renderOrder=3; g.add(s);
    items.push({s:s,ph:i*0.53});
  }
  return {g,items,update:function(t,k,lit){
    const li=lit===undefined?0:lit;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const s=(0.45+0.95*li)*(0.9+0.1*Math.sin(t*2.4+it.ph));
      it.s.scale.set(s*1.35,s*1.35,1);
    }
  }};
}

/* —— 高烛：红烛（烛身 + 承盘 + 烛芯 + 焰 + 暖光池；点击点燃，焰与光由 scale/强度驱动） —— */
function makeCandleHT(o){
  o=o||{};
  const h=o.h===undefined?2.6:o.h, B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.16,0.19,h,10); body.translate(0,h/2,0); B.put(body,0xb8323a);
  const drip=new THREE.SphereGeometry(0.05,6,5); drip.translate(0.15,h*0.7,0); B.put(drip,0xd05058);
  const dish=new THREE.CylinderGeometry(0.46,0.52,0.12,12); dish.translate(0,0.06,0); B.put(dish,0x8a6a34);
  const stem=new THREE.CylinderGeometry(0.10,0.16,0.5,8); stem.translate(0,-0.25,0); B.put(stem,0x6a5230);
  const wick=new THREE.CylinderGeometry(0.02,0.02,0.2,4); wick.translate(0,h+0.1,0); B.put(wick,0x201a14);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:20,
    specular:0x8a5a4a,emissive:0x1a0a0c}),{c:0xffb070,i:0.36,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const flame=makeFlame({h:0.9,w:0.34,planes:3,embers:0,spark:false,light:o.light===undefined?1.35:o.light,
    lightD:o.lightD===undefined?40:o.lightD,core:0xffe0a0,outer:0xff8a3a,wide:0.28});
  flame.g.position.y=h+0.24; g.add(flame.g);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb060,transparent:true,
    opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.position.y=h+0.3; halo.scale.set(2.6,2.6,1); halo.renderOrder=3; g.add(halo);
  const pool=new THREE.Mesh(new THREE.CircleGeometry(2.4,20),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0xff9a4a,transparent:true,opacity:0.26,
      depthWrite:false,blending:THREE.AdditiveBlending}));
  pool.rotation.x=-Math.PI/2; pool.position.y=-0.42; pool.renderOrder=3; g.add(pool);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,flame,halo,pool,mesh,
    update:function(t,k,lit){
      const kk=k===undefined?1:k, li=lit===undefined?0:lit;
      flame.update(t,kk*(0.03+0.92*li));   /* li=0 时几乎不燃，点击后才烧起来 */
      const hs=(0.5+1.1*li)*(0.94+0.06*Math.sin(t*6.1));
      halo.scale.set(2.6*hs,2.6*hs,1);
      const ps=(0.4+1.0*li)*(0.96+0.04*Math.sin(t*3.3));
      pool.scale.set(ps,ps,1);
    }};
}

/* —— 回廊：柱 + 梁 + 栏 + 廊顶（合批 1 mesh） —— */
function makeCorridorHT(o){
  o=o||{};
  const len=o.len===undefined?44:o.len, h=o.h===undefined?7.2:o.h, n=o.n===undefined?5:o.n;
  const col=o.color===undefined?0x2a1a12:o.color, B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=-len/2+len*i/(n-1);
    const base=new THREE.BoxGeometry(1.1,0.6,1.1); base.translate(x,0.3,0); B.put(base,shadeColor(col,0.75));
    const p=new THREE.CylinderGeometry(0.32,0.36,h,10); p.translate(x,h/2+0.6,0); B.put(p,col);
    const dou=new THREE.BoxGeometry(1.3,0.34,1.3); dou.translate(x,h+0.77,0); B.put(dou,shadeColor(col,1.15));
  }
  const beam=new THREE.BoxGeometry(len+2,0.5,1.0); beam.translate(0,h+1.2,0); B.put(beam,shadeColor(col,1.25));
  const railT=new THREE.BoxGeometry(len,0.18,0.26); railT.translate(0,2.3,3.6); B.put(railT,shadeColor(col,1.3));
  const railB=new THREE.BoxGeometry(len,0.14,0.22); railB.translate(0,1.2,3.6); B.put(railB,shadeColor(col,1.05));
  for(let i=0;i<=n*3;i++){
    const x=-len/2+len*i/(n*3);
    const q=new THREE.BoxGeometry(0.16,2.4,0.16); q.translate(x,1.2,3.6); B.put(q,col);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x5a3a22,emissive:0x0a0604}),{c:o.rimC===undefined?0xd9a85a:o.rimC,i:0.30,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?-24:o.z);
  return {g,mesh};
}

/* —— 月光带：地面上一道随月移缓缓转过的月华（只改 rotation/scale，不动 opacity） —— */
function makeMoonBandHT(o){
  o=o||{};
  const w=o.w===undefined?30:o.w;
  const m=new THREE.Mesh(new THREE.PlaneGeometry(w,w*0.28),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0xbfd0e8,transparent:true,opacity:0.16,
      depthWrite:false,blending:THREE.AdditiveBlending}));
  m.rotation.x=-Math.PI/2; m.renderOrder=3;
  m.position.set(o.x===undefined?0:o.x,o.y===undefined?0.06:o.y,o.z===undefined?0:o.z);
  return {mesh:m,update:function(t,run){
    const r=run===undefined?0:run;
    m.rotation.z=o.a0===undefined?-0.5:o.a0+r*0.55;
    const s=1+0.04*Math.sin(t*0.3);
    m.scale.set(s,s,1);
  }};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 夜庭海棠 —— 回廊一侧，海棠一树，月色与香雾
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0a0806,c2:0x181008,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:36,layers:3,peaks:5,seed:1211,color:0x0d0906,atmo:0x3a2c20,
    fogK:0.62,glowK:0.08,glow:0xd9a85a,y:-11});
  ridge.g.position.set(0,0,-94); g.add(ridge.g);
  const cor=makeCorridorHT({len:46,h:7.0,x:-14,y:-1.4,z:-22}); g.add(cor.g);
  const tree=makeCrabappleHT({h:5.0,seed:87,scale:1.1}); tree.g.position.set(6,-1.4,-12); g.add(tree.g);
  const tree2=makeCrabappleHT({h:4.0,seed:89,scale:0.92}); tree2.g.position.set(18,-1.4,-20); g.add(tree2.g);
  const band=makeMoonBandHT({w:34,x:2,y:-1.32,z:-14,a0:-0.5}); g.add(band.mesh);
  const mist=makeMist({n:8,spread:[220,26,110],pos:[0,9,-46],scale:76,color:0x3a2418,op:0.12}); g.add(mist.g);
  const motes=makeGlow({n:46,box:[180,28,90],pos:[0,10,-26],color:0xe8c080,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motes.points);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:18,d:7,color:0x0a0705,seed:37,rim:0.18,rimC:0xd9a85a});
  fg.g.position.set(-17,-1.6,36); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x080604,seed:39,rim:0.14,rimC:0xc08a4a});
  fg2.g.position.set(16,-1.4,22); g.add(fg2.g);
  addLights(g,{c:0xd9c090,i:0.46,p:[-50,80,26]},{c:0x2a1c12,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    tree.update(t,k,0.25); tree2.update(t,k,0.2); band.update(t,0.15);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bDongfeng(){ // 一 · 东风香雾 —— 东风袅袅泛崇光，香雾空蒙月转廊
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0a0806,c2:0x181008,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:3,peaks:5,seed:1221,color:0x0d0906,atmo:0x3a2c20,
    fogK:0.62,glowK:0.08,glow:0xd9a85a,y:-11});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  /* 回廊在左，月转廊（地面月光带缓缓转过） */
  const cor=makeCorridorHT({len:50,h:7.4,x:-16,y:-1.3,z:-18}); g.add(cor.g);
  const band=makeMoonBandHT({w:40,x:0,y:-1.22,z:-10,a0:-0.62}); g.add(band.mesh);
  /* 海棠当庭（近景主体） */
  const tree=makeCrabappleHT({h:5.4,seed:91,scale:1.18}); tree.g.position.set(5.5,-1.3,-9); g.add(tree.g);
  const tree2=makeCrabappleHT({h:4.2,seed:97,scale:0.95}); tree2.g.position.set(16,-1.3,-16); g.add(tree2.g);
  /* 香雾空蒙：低回香雾 + 浮尘 */
  const mist=makeMist({n:10,spread:[200,20,90],pos:[0,4.2,-14],scale:52,color:0x6a4a34,op:0.13});
  g.add(mist.g);
  const scent=makeFlow({n:220,box:[170,18,90],pos:[0,4.5,-18],color:0xe0b088,size:12,speed:1.1,maxA:0.14});
  g.add(scent.points);
  const motes=makeGlow({n:44,box:[170,26,86],pos:[0,9,-24],color:0xe8c080,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motes.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.4,w:17,d:7,color:0x060504,seed:41,rim:0.16,rimC:0xd9a85a});
  fg.g.position.set(-13,-1.5,19); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:30,n:8,d:6,color:0x060504,seed:43,sway:0.7,rim:0.14,rimC:0xc08a4a});
  fg2.g.position.set(17,-1.3,17); fg2.g.rotation.z=-0.2; g.add(fg2.g);
  addLights(g,{c:0xd9c090,i:0.46,p:[-46,78,24]},{c:0x2a1c12,i:0.60});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); scent.update(t); motes.update(t);
      const wind=0.35+0.25*Math.sin(t*0.5);
      tree.update(t,k,wind); tree2.update(t,k,wind*0.85);
      band.update(t,0.8);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(4,0.3,0.09); pluck(5,0.9,0.08); }};
}
function bShaozhu(){ // 二（末境·可点击）· 烧烛红妆 —— 只恐夜深花睡去，故烧高烛照红妆
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,lit:0};
  const grd=makeGround({r:240,c1:0x090705,c2:0x150e07,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:30,layers:2,peaks:5,seed:1231,color:0x0c0805,atmo:0x352718,
    fogK:0.60,glowK:0.06,glow:0xcc9a52,y:-11});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const cor=makeCorridorHT({len:46,h:7.2,x:-18,y:-1.3,z:-20}); g.add(cor.g);
  /* 夜深：海棠低垂（花睡去） */
  const tree=makeCrabappleHT({h:5.2,seed:101,scale:1.14}); tree.g.position.set(3.6,-1.3,-7.6); g.add(tree.g);
  tree.g.rotation.z=-0.06;
  const spots=[];
  for(let i=0;i<tree.spots.length;i+=5){
    const p=tree.spots[i];
    spots.push([p[0]+3.6,p[1]-1.3,p[2]-7.6]);
  }
  const glow=makeFlowerGlowHT({pos:spots}); g.add(glow.g);
  /* 高烛一支（在诗人手边；点击点燃） */
  const candle=makeCandleHT({h:2.8,scale:0.95,x:0,y:-1.3,z:1.2}); g.add(candle.g);
  /* 诗人：持烛看花（独立于花前） */
  const poet=makeFigure({pose:'独立',robe:0x3a2a20,belt:0xd9a85a,collar:0xf0e2cc,hat:'幞头',
    hair:0x14100c,scale:1.16,rim:0.50,rimC:0xe8c088,noProp:true});
  poet.position.set(-1.9,-1.0,0.8); poet.rotation.y=-1.9; g.add(poet);
  const band=makeMoonBandHT({w:32,x:2,y:-1.22,z:-6,a0:-0.7}); g.add(band.mesh);
  const mist=makeMist({n:8,spread:[200,20,90],pos:[0,4.0,-14],scale:50,color:0x5a4030,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[160,24,84],pos:[0,8,-20],color:0xe8c080,size:7,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x060504,seed:45,rim:0.16,rimC:0xd9a85a});
  fg.g.position.set(-13,-1.4,10.5); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0x070604,seed:47,sway:0.8,tip:0x3a2a18});
  fg2.g.position.set(13,-1.3,9); g.add(fg2.g);
  addLights(g,{c:0xc8b088,i:0.40,p:[-44,76,22]},{c:0x261a10,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.lit=Math.min(1,ctl.lit+dt/1.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const lit=ctl.lit+0.5*ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      candle.update(t,k,lit);
      glow.update(t,k,lit);
      tree.update(t,k,0.12); band.update(t,0.2);
      poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.13); pluck(2,0.28,0.11); pluck(4,0.60,0.09);
        const fl=$('#flash'); fl.textContent='照红妆'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：烛光再亮一分，花容再显一层 */
    },clicked:false};
  return api;
}
