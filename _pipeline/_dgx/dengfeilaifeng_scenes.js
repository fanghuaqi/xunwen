/* ================= 登飞来峰 · 三境场景（大漠金戈 · 孤峰塔影变体：卷首孤峰、千寻高塔、身在高层）
   本诗专属系统「浮云散·日升」：孤峰顶一座七层宝塔，晨雾浮云漫过山腰；
   末境点击最高层 → 近前塔檐沉下（身已上升）、浮云四散、旭日跃出云海、金光铺满画面。
   与同赛道《从军行》（玉门孤城、金甲烽火）不同：本页是孤峰、宝塔、云海与日出。 ================= */

/* —— 飞来峰：四层台地岩体堆成的孤峰（合批 1 mesh）+ 岩块点缀 —— */
function makePeakDFL(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17:o.seed);
  const r0=o.r===undefined?15:o.r, h=o.h===undefined?18:o.h;
  const col=o.color===undefined?0x3a2a1a:o.color;
  const B=new GeoBag();
  const layers=4;
  let y=0, rr=r0;
  for(let i=0;i<layers;i++){
    const hh=h/layers*(1.05-i*0.06);
    const g=new THREE.CylinderGeometry(rr*(0.86-i*0.07), rr, hh, 9);
    g.translate(0,y+hh*0.5,0);
    B.put(g,shadeColor(col,0.78+R()*0.5));
    y+=hh; rr*=0.70;
  }
  for(let i=0;i<16;i++){
    const s=1.2+R()*2.4, a=R()*6.283;
    const rg=rockGeo(s,1,R);
    rg.translate(Math.sin(a)*r0*(0.5+R()*0.7), R()*h*0.55, Math.cos(a)*r0*(0.5+R()*0.7));
    B.put(rg,shadeColor(col,0.6+R()*0.6));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a2a1a,emissive:0x0a0604}),{c:o.rimC===undefined?0xd9a05a:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x, o.y===undefined?0:o.y, o.z===undefined?0:o.z);
  return {g,mesh};
}

/* —— 千寻塔：七层宝塔（塔基 + 层身 + 四角檐 + 塔刹），合批 1 mesh —— */
function makePagodaDFL(o){
  o=o||{};
  const tiers=o.tiers===undefined?7:o.tiers, baseR=o.r===undefined?1.9:o.r;
  const tierH=o.tierH===undefined?1.5:o.tierH;
  const body=o.body===undefined?0x6a4a2e:o.body, roof=o.roof===undefined?0x3a2a1c:o.roof;
  const B=new GeoBag();
  const bs=new THREE.BoxGeometry(baseR*2.5,1.3,baseR*2.5); bs.translate(0,0.65,0); B.put(bs,0x50402c);
  const bp=new THREE.CylinderGeometry(baseR*1.15,baseR*1.35,0.5,8); bp.translate(0,1.55,0); B.put(bp,0x5a4630);
  let y=1.8;
  for(let i=0;i<tiers;i++){
    const k=1-0.045*i;
    const hh=tierH*(0.98-0.05*i), rr=baseR*k;
    const bd=new THREE.BoxGeometry(rr*1.7,hh,rr*1.7); bd.translate(0,y+hh*0.5,0);
    B.put(bd,shadeColor(body,0.92+i*0.03));
    const dr=new THREE.BoxGeometry(rr*0.46,hh*0.5,0.18); dr.translate(0,y+hh*0.42,rr*0.86); B.put(dr,0x140f0a);
    const rf=new THREE.ConeGeometry(rr*1.72,hh*0.58,4); rf.rotateY(Math.PI/4);
    rf.translate(0,y+hh+hh*0.28,0); B.put(rf,shadeColor(roof,1.0+i*0.05));
    const kn=new THREE.SphereGeometry(rr*0.10,5,4); kn.translate(0,y+hh+hh*0.62,0); B.put(kn,0xa88a4a);
    y+=hh+hh*0.56;
  }
  const spire=new THREE.ConeGeometry(baseR*0.30,2.6,8); spire.translate(0,y+1.3,0); B.put(spire,0x8a6a3a);
  const ball=new THREE.SphereGeometry(baseR*0.20,8,6); ball.translate(0,y+2.7,0); B.put(ball,0xd0a850);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a5030,emissive:0x0c0804}),{c:o.rimC===undefined?0xe0b070:o.rimC,i:0.34,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g,mesh};
}

/* —— 塔檐近景：末境身处塔顶时近前的两层檐角与栏杆（点击后随"上升"沉下画面） —— */
function makeTowerTopDFL(o){
  o=o||{};
  const w=o.w===undefined?28:o.w, B=new GeoBag();
  const body=o.body===undefined?0x6a4a2e:o.body, roof=o.roof===undefined?0x3a2a1c:o.roof;
  const bd=new THREE.BoxGeometry(w,3.2,14); bd.translate(0,-1.6,0); B.put(bd,body);
  const eave=new THREE.ConeGeometry(w*0.60,2.2,4); eave.rotateY(Math.PI/4);
  eave.translate(0,0.5,0); B.put(eave,roof);
  /* 栏杆在相机前方（local z 取负），且低于视轴：读得出来"身在塔顶" */
  const railT=new THREE.BoxGeometry(w*1.02,0.24,0.34); railT.translate(0,1.35,-5.0); B.put(railT,0x7a5630);
  const railB=new THREE.BoxGeometry(w*1.02,0.18,0.26); railB.translate(0,0.45,-5.0); B.put(railB,0x5a3e26);
  for(let i=0;i<=12;i++){
    const p=new THREE.BoxGeometry(0.22,1.6,0.22); p.translate(-w*0.51+w*1.02*i/12,0.82,-5.0); B.put(p,0x4a3420);
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a5030,emissive:0x0c0804}),{c:0xe0b070,i:0.30,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x, o.y===undefined?6:o.y, o.z===undefined?10:o.z);
  return {g,mesh};
}

/* —— 云海：一层翻涌的云（Sprite 群；点击后向两侧散开、下沉 = 浮云散） —— */
function makeCloudSeaDFL(o){
  o=o||{};
  const n=o.n===undefined?26:o.n, sp=o.spread===undefined?[220,10,90]:o.spread;
  const pos=o.pos===undefined?[0,6,-26]:o.pos, sc=o.scale===undefined?34:o.scale;
  const col=o.color===undefined?0xc9b090:o.color, op=o.op===undefined?0.22:o.op;
  const R=seedRnd(o.seed===undefined?41:o.seed);
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:col,transparent:true,
      opacity:op*(0.55+R()*0.7),depthWrite:false});
    const s=new THREE.Sprite(m);
    const x0=pos[0]+(R()-0.5)*sp[0], y0=pos[1]+(R()-0.5)*sp[1], z0=pos[2]+(R()-0.5)*sp[2];
    s.position.set(x0,y0,z0);
    const k=sc*(0.7+R()*0.85);
    s.scale.set(k,k*0.42,1); s.renderOrder=5;
    g.add(s); items.push({s:s,base:[k,k*0.42],x0:x0,y0:y0,ph:R()*6.283,dir:(R()<0.5?-1:1)});
  }
  return {g,items,update:function(t,k,part){
    const pt=part===undefined?0:part;   /* 云片 opacity 由 setFade 统一淡入淡出，此处只动 scale/位置 */
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const w=1+0.05*Math.sin(t*0.22+it.ph);
      it.s.scale.set(it.base[0]*w, it.base[1]*w, 1);
      it.s.position.x=it.x0+it.dir*pt*26;
      it.s.position.y=it.y0-pt*7+0.5*Math.sin(t*0.3+it.ph);
    }
  }};
}

/* —— 旭日：一枚跃出云海的日轮（日盘 + 三层暖金辉光；随"日升"上移放大） —— */
function makeSunDFL(o){
  o=o||{};
  const r=o.r===undefined?9:o.r;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd88a,transparent:true,
    opacity:0.95,depthWrite:false,blending:THREE.AdditiveBlending}));
  disc.scale.set(r*2.1,r*2.1,1); disc.renderOrder=-8; g.add(disc);
  const halo=[];
  [2.6,4.4,7.2].forEach(function(k,i){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:[0xffc46a,0xf0a04a,0xc8803a][i],
      transparent:true,opacity:[0.36,0.20,0.12][i],depthWrite:false,blending:THREE.AdditiveBlending}));
    s.scale.set(r*k,r*k*0.9,1); s.renderOrder=-8; g.add(s); halo.push({s:s,op:[0.36,0.20,0.12][i],k:k});
  });
  g.position.set(o.x===undefined?-40:o.x, o.y===undefined?10:o.y, o.z===undefined?-150:o.z);
  const y0=g.position.y;
  return {g,halo,update:function(t,k,rise){
    const kk=k===undefined?1:k, ri=rise===undefined?0:rise;
    g.position.y=y0+ri*9;
    const w=1+0.03*Math.sin(t*0.5)+0.25*ri;
    g.scale.set(w,w,1);
    for(let i=0;i<halo.length;i++){                    /* 只调 scale，不写 opacity（fadeK 铁律） */
      const hh=halo[i].k*(1+0.22*ri)*(0.97+0.03*Math.sin(t*0.7+i));
      halo[i].s.scale.set(r*hh,r*hh*0.9,1);
    }
  }};
}

/* —— 登山石阶：一条折上的石阶（合批 1 mesh） —— */
function makeStepsDFL(o){
  o=o||{};
  const n=o.n===undefined?22:o.n, R=seedRnd(o.seed===undefined?53:o.seed);
  const w=o.w===undefined?4.4:o.w, B=new GeoBag();
  for(let i=0;i<n;i++){
    const t=i/n;
    const st=new THREE.BoxGeometry(w*(1-t*0.25),0.42,w*0.9);
    st.translate((R()-0.5)*0.3, 0.21+i*0.62, -i*1.35);
    B.put(st,shadeColor(0x5a4a34,0.8+R()*0.5));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a3020,emissive:0x080604}),{c:0xc08a4a,i:0.24,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 孤峰塔影 —— 晨雾里的飞来峰与峰顶宝塔
  const g=new THREE.Group();
  const grd=makeGround({r:270,c1:0x140e08,c2:0x241a10,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:52,layers:3,peaks:5,seed:1011,color:0x1a1008,atmo:0x4a3418,
    fogK:0.62,glowK:0.08,glow:0xd9a05a,y:-14});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  const peak=makePeakDFL({r:16,h:19,x:0,y:-1.6,z:-46,seed:19}); g.add(peak.g);
  const pag=makePagodaDFL({tiers:7,r:1.9,scale:1.05}); pag.g.position.set(0,17.4,-46); g.add(pag.g);
  const sun=makeSunDFL({r:10,x:-70,y:14,z:-190}); g.add(sun.g);
  const clouds=makeCloudSeaDFL({n:20,spread:[240,10,80],pos:[0,4,-40],scale:32,op:0.20,seed:43});
  g.add(clouds.g);
  const crowd=makeCrowd({n:4,rect:[-10,-24,20,8],seed:61,color:0x1a1108,rimC:0xe0b070,rim:0.22});
  g.add(crowd.mesh);
  const motes=makeGlow({n:46,box:[190,26,80],pos:[0,10,-40],color:0xe8c080,size:7,speed:0.03,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,26,110],pos:[0,9,-60],scale:80,color:0x3a2814,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:4.0,w:20,d:8,color:0x0a0704,seed:23,rim:0.16,rimC:0xd9a05a});
  fg.g.position.set(-18,-1.8,42); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:6,color:0x080604,seed:25,rim:0.14,rimC:0xc08a4a});
  fg2.g.position.set(17,-1.6,24); g.add(fg2.g);
  addLights(g,{c:0xe8bc74,i:0.50,p:[-55,85,30]},{c:0x2a1c0e,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); crowd.update(t);
    clouds.update(t,k,0); sun.update(t,k,0.35);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bQianxun(){ // 一 · 千寻高塔 —— 飞来山上千寻塔，闻说鸡鸣见日升
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0x130d08,c2:0x221810,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:50,layers:3,peaks:5,seed:1021,color:0x190f07,atmo:0x46301a,
    fogK:0.62,glowK:0.08,glow:0xd9a05a,y:-13});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  /* 飞来峰与峰顶千寻塔 */
  const peak=makePeakDFL({r:17,h:20,x:0,y:-1.4,z:-42,seed:21}); g.add(peak.g);
  const pag=makePagodaDFL({tiers:7,r:2.0,scale:1.15}); pag.g.position.set(0,18.6,-42); g.add(pag.g);
  /* 登山石阶 */
  const steps=makeStepsDFL({n:24,w:4.6,x:-6.5,y:-1.4,z:6}); steps.g.rotation.y=-0.42; g.add(steps.g);
  /* 晨雾与云（山腰浮云） */
  const clouds=makeCloudSeaDFL({n:22,spread:[220,8,70],pos:[0,7,-30],scale:30,op:0.20,seed:47});
  g.add(clouds.g);
  const sun=makeSunDFL({r:11,x:-78,y:12,z:-180}); g.add(sun.g);
  /* 登山者：峰下拾级而上的一人（王安石自况） */
  const poet=makeFigure({pose:'独立',robe:0x3a2a1a,belt:0xc08a4a,collar:0xf0e2cc,hat:'幞头',
    hair:0x141008,scale:1.12,rim:0.48,rimC:0xe0b070,noProp:true});
  poet.position.set(-3.0,-0.5,3.6); poet.rotation.y=-0.5; g.add(poet);
  const motif=makeGlow({n:42,box:[180,26,80],pos:[0,10,-36],color:0xe8c080,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motif.points);
  const mist=makeMist({n:7,spread:[230,24,110],pos:[0,9,-58],scale:78,color:0x3a2814,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.6,w:18,d:7,color:0x0a0704,seed:27,rim:0.16,rimC:0xd9a05a});
  fg.g.position.set(-15,-1.6,20); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x080604,seed:29,rim:0.14,rimC:0xc08a4a});
  fg2.g.position.set(15,-1.4,16); g.add(fg2.g);
  addLights(g,{c:0xe8bc74,i:0.50,p:[-50,82,26]},{c:0x2a1c0e,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motif.update(t); clouds.update(t,k,0);
      sun.update(t,k,0.4);
      poet.update(t,k);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(3,0.3,0.09); pluck(5,0.9,0.08); }};
}
function bZuigao(){ // 二（末境·可点击）· 身在高层 —— 不畏浮云遮望眼，自缘身在最高层
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,part:0};
  const grd=makeGround({r:200,c1:0x140e08,c2:0x241a10,y:-40}); g.add(grd.mesh);   /* 谷底远在地平之下 */
  const ridge=makeRange({r:280,h:40,layers:3,peaks:6,seed:1031,color:0x1a1008,atmo:0x4a3418,
    fogK:0.62,glowK:0.08,glow:0xd9a05a,y:-22});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 云海在脚下（同一层云，点击后向两侧散开） */
  const clouds=makeCloudSeaDFL({n:30,spread:[260,8,60],pos:[0,5.2,-70],scale:44,op:0.30,seed:51});
  g.add(clouds.g);
  /* 近前塔檐与栏杆（身在此处；点击"上升"后它沉下画面） */
  const top=makeTowerTopDFL({w:28,y:6.6,z:9.5}); g.add(top.g);
  /* 旭日：云海尽头一跃而出 */
  const sun=makeSunDFL({r:13,x:-40,y:8,z:-160}); g.add(sun.g);
  const motif=makeGlow({n:40,box:[190,24,80],pos:[0,9,-40],color:0xf0cc8c,size:7,speed:0.03,rise:0,maxA:0.15});
  g.add(motif.points);
  const mist=makeMist({n:6,spread:[220,22,100],pos:[0,8,-70],scale:78,color:0x3a2814,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.4,w:18,d:7,color:0x0a0704,seed:31,rim:0.16,rimC:0xd9a05a});
  fg.g.position.set(-16,-1.0,14); g.add(fg.g);
  const fg2=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x080604,seed:33,rim:0.14,rimC:0xc08a4a});
  fg2.g.position.set(15,-1.0,12); g.add(fg2.g);
  addLights(g,{c:0xf0c47c,i:0.52,p:[-48,80,24]},{c:0x2c1e10,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.part=Math.min(1,ctl.part+dt/2.4);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.4);
      const pt=ctl.part+0.25*ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motif.update(t);
      clouds.update(t,k,pt);
      sun.update(t,k,0.20+0.55*ctl.part);
      top.g.position.y=6.6-4.6*ctl.part;        /* 近前塔檐沉下：身已升至最高层 */
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(5,0.00,0.14); pluck(2,0.30,0.12); pluck(0,0.70,0.10);
        const fl=$('#flash'); fl.textContent='不畏浮云遮望眼'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：浮云再散一分，日轮再升一程 */
    },clicked:false};
  return api;
}
