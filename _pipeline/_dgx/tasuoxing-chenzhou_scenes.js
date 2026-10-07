/* ================= 踏莎行 · 郴州旅舍 两境场景（烟雨江南·秦观：浓雾是本页主角） =================
   美术立意：黛蓝湿雾 #151d26 主调、accent #8f9fc0、藕荷 #d8a7b1 仅作梅萼/桃色一点；月隐为常，
   唯「月迷津渡」境悬一团被雾裹住的低垂淡月。
   标志性瞬间「楼台显而复失」：远景楼台自浓雾浮出轮廓又溶回——开篇八字是全词意境总纲。
   末境点击郴江：江流绕郴山加速增亮（流向叩问），杜鹃三啼，题字「为谁流下潇湘去？」。
   情感曲线：雾迷 → 孤寒 → 恨砌 → 江问。 */

/* —— 杜鹃啼「不如归去」：两声下行小三度（无音频上下文时静默，Node 冒烟安全） —— */
function cuckooCry(delay,vol){
  if(!groupAudio.ctx)return;
  const ctx=groupAudio.ctx, t0=ctx.currentTime+(delay||0), v=vol===undefined?0.09:vol;
  [[920,0],[716,0.26]].forEach(function(nd){
    const o=ctx.createOscillator(), g=ctx.createGain();
    o.type='sine';
    o.frequency.setValueAtTime(nd[0]*1.04, t0+nd[1]);
    o.frequency.exponentialRampToValueAtTime(nd[0]*0.90, t0+nd[1]+0.15);
    g.gain.setValueAtTime(0.0001, t0+nd[1]);
    g.gain.exponentialRampToValueAtTime(v, t0+nd[1]+0.035);
    g.gain.exponentialRampToValueAtTime(0.0001, t0+nd[1]+0.22);
    o.connect(g); g.connect(groupAudio.master);
    o.start(t0+nd[1]); o.stop(t0+nd[1]+0.26);
  });
}

/* —— 楼台（标志性瞬间「显而复失」）：三层八角楼阁合批 1 mesh + 窗灯一粒；
      update 里透明度随慢波呼吸——自雾里浮出（显）又溶回浓雾（失）。 —— */
function makeLouTai(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1830:o.seed);
  const sc=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  let y=0;
  const baseR=o.r===undefined?3.2:o.r;
  for(let i=0;i<3;i++){
    const r=baseR*(1-i*0.26), h=2.2-i*0.25;
    const body=new THREE.CylinderGeometry(r*0.86,r,h,8,1);
    body.translate(0,y+h/2,0); B.put(body,i%2?0x18202c:0x141b26);
    const eave=new THREE.ConeGeometry(r*1.28,0.9,8); eave.rotateY(Math.PI/8);
    eave.translate(0,y+h+0.42,0); B.put(eave,0x0d1219);
    y+=h+0.8;
  }
  const finial=new THREE.SphereGeometry(0.28,8,6); finial.translate(0,y+0.18,0); B.put(finial,0x27313f);
  const maxOp=o.op===undefined?0.62:o.op;
  const mat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3742,emissive:0x0a0f16,transparent:true,opacity:maxOp});
  const mesh=B.mesh(rimHook(mat,{c:o.rimC===undefined?0x8f9fc0:o.rimC,i:0.26,p:2.6}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  /* 背光雾晕：楼后一团微光（雾中显形的"底"），暗色楼身剪影才读得出来 */
  const backM=new THREE.SpriteMaterial({map:glowTex(),color:0xaebfd4,transparent:true,
    opacity:maxOp*0.35,depthWrite:false,depthTest:false});
  const back=new THREE.Sprite(backM); back.scale.set(baseR*7.5,baseR*5.2,1);
  back.position.set(0,4.2,0); back.renderOrder=-1; g.add(back);
  /* 窗灯：一层檐下一粒冷光，随楼台同呼吸 */
  const lampM=new THREE.SpriteMaterial({map:glowTex(),color:0xa9bccd,transparent:true,
    opacity:maxOp*0.32,depthWrite:false});
  const lamp=new THREE.Sprite(lampM); lamp.scale.set(4.2,4.2,1);
  lamp.position.set(0,2.6,baseR*0.9); lamp.renderOrder=4; g.add(lamp);
  const ph=R()*6.283, spd=o.spd===undefined?0.28:o.spd;
  const api={g,update(t,k){
    if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    const s=0.5+0.5*Math.sin(t*spd+ph);
    const shape=Math.pow(Math.max(0,s-0.30)/0.70,1.7);      // 0..1：显-失的慢波
    mat.opacity=k*maxOp*(0.16+0.84*shape);
    backM.opacity=k*(maxOp*0.35)*(0.12+0.88*shape);
    lampM.opacity=k*(maxOp*0.32)*shape;
  }};
  g.userData.update=api.update;
  g.scale.setScalar(sc);
  return api;
}

/* —— 孤馆：客舍一楹——台基厚墙、闭着的门、一扇透冷光的纸窗（合批 1 mesh + 窗灯 sprite） —— */
function makeGuan(o){
  o=o||{};
  const w=o.w===undefined?5.6:o.w, d=o.d===undefined?4.2:o.d, h=o.h===undefined?3.1:o.h;
  const wall=0x1b2330;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w+0.6,0.5,d+0.6); base.translate(0,0.25,0); B.put(base,0x0e131a);
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h/2+0.5,0); B.put(body,wall);
  const sill=new THREE.BoxGeometry(w+0.5,0.18,d+0.5); sill.translate(0,h+0.44,0); B.put(sill,shadeColor(wall,1.3));
  const roof=new THREE.ConeGeometry(Math.max(w,d)*0.78,1.5,4); roof.rotateY(Math.PI/4);
  roof.scale(1,1,d/w); roof.translate(0,h+1.28,0); B.put(roof,0x10151d);
  const door=new THREE.BoxGeometry(1.1,2.0,0.12); door.translate(0.6,1.5,d/2+0.02); B.put(door,0x0a0e14);
  const win=new THREE.BoxGeometry(0.9,0.8,0.1); win.translate(-w*0.26,1.9,d/2+0.02); B.put(win,0x0a0e14);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x28313c,emissive:0x070a10}),{c:0x8f9fc0,i:0.18,p:2.8})));
  const lampM=new THREE.SpriteMaterial({map:glowTex(),color:0x9fb4c4,transparent:true,opacity:0.38,depthWrite:false});
  const lamp=new THREE.Sprite(lampM); lamp.scale.set(3.4,3.4,1);
  lamp.position.set(-w*0.26,1.9,d/2+0.38); lamp.renderOrder=4; g.add(lamp);
  const api={g,update(t,k){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    lampM.opacity=k*(0.26+0.12*Math.sin(t*0.8+2.1)); }};
  g.userData.update=api.update;
  return api;
}

/* —— 津渡：木栈桥入水（桩 + 面板合批 1 mesh） —— */
function makePier(o){
  o=o||{};
  const L=o.L===undefined?9:o.L, w=o.w===undefined?2.0:o.w;
  const B=new GeoBag();
  for(let i=0;i<6;i++){
    const pl=new THREE.BoxGeometry(w,0.12,L/6); pl.translate(0,0.9,L/2-(i+0.5)*L/6); B.put(pl,0x1c1610);
  }
  for(let i=0;i<4;i++)for(const s of [-1,1]){
    const pile=new THREE.CylinderGeometry(0.09,0.11,2.4,6);
    pile.translate(s*w*0.42,-0.2,(i+0.5)*L/4-0.2); B.put(pile,0x14100c);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x242a30,emissive:0x06090d}),{c:0x8f9fc0,i:0.16,p:2.8})));
  return g;
}

/* —— 渡船：平头小渡船（Lathe 半壳拉长 + 船板 + 拱篷 + 橹，合批 1 mesh + 接触阴影） —— */
function makeFerry(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const pts=[[0,0.02],[0.55,0.05],[0.95,0.30],[1.12,0.62],[1.18,0.72]].map(p=>new THREE.Vector2(p[0],p[1]));
  const B=new GeoBag();
  const hull=new THREE.LatheGeometry(pts,16); hull.scale(1.0,0.6,2.6); B.put(hull,0x332c22);
  const deck=new THREE.BoxGeometry(1.4,0.07,4.4); deck.translate(0,0.40,0.2); B.put(deck,0x3d352a);
  const can=new THREE.CylinderGeometry(0.8,0.8,1.9,10,1,true,Math.PI/2,Math.PI);
  can.rotateX(Math.PI/2); can.scale(1,0.62,1); can.translate(0,0.48,-0.7); B.put(can,0x20282a);
  const oar=new THREE.CylinderGeometry(0.03,0.045,2.4,5); oar.rotateX(0.6); oar.translate(0,0.5,2.0);
  B.put(oar,0x26201a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x333d46,emissive:0x080b0f,side:THREE.DoubleSide}),{c:0x8f9fc0,i:0.3,p:2.5}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const sh=new THREE.Mesh(new THREE.CircleGeometry(1.7,14),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0x000000,transparent:true,opacity:0.45,depthWrite:false}));
  sh.rotation.x=-Math.PI/2; sh.position.y=0.03; sh.renderOrder=0; g.add(sh);
  g.scale.setScalar(sc);
  return g;
}

/* —— 杜鹃鸟影：一点墨羽（躯 + 首 + 喙 + 尾，合批 1 mesh；update 做啼时仰喙） —— */
function makeCuckooBird(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.34,8,6); body.scale(1.5,0.9,0.85); B.put(body,o.color===undefined?0x0e1319:o.color);
  const head=new THREE.SphereGeometry(0.17,8,6); head.translate(0.50,0.16,0); B.put(head,0x11161d);
  const beak=new THREE.ConeGeometry(0.05,0.22,5); beak.rotateZ(-Math.PI/2); beak.translate(0.74,0.18,0); B.put(beak,0x2c3138);
  const tail=new THREE.BoxGeometry(0.55,0.05,0.16); tail.rotateZ(0.22); tail.translate(-0.52,0.08,0); B.put(tail,0x0b0f14);
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1c2229,emissive:0x04070a}));
  const g=new THREE.Group(); g.add(mesh);
  const api={g,update(t,k){
    mesh.rotation.z=(o.fly?-0.10:0.03)*Math.sin(t*(o.fly?7.3:1.2));
  }};
  g.userData.update=api.update;
  return api;
}

/* —— 梅枝（驿寄梅花）：曲干 + 疏萼粉梅（合批 1 mesh，藕荷点缀） —— */
function makePlumBranch(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1841:o.seed);
  const B=new GeoBag();
  const spots=[];
  let px=0, py=0, ang=o.lean===undefined?0.55:o.lean;
  for(let i=0;i<4;i++){
    const len=1.9-i*0.28, a=ang*(0.62+0.24*i);
    const seg=new THREE.CylinderGeometry(Math.max(0.035,0.09-i*0.018),Math.max(0.05,0.12-i*0.02),len,6);
    seg.rotateZ(-a); seg.translate(px+len*Math.sin(a)/2,py+len*Math.cos(a)/2,0);
    B.put(seg,0x241c20);
    for(let j=0;j<3;j++) spots.push([px+len*Math.sin(a)*(0.25+0.3*j), py+len*Math.cos(a)*(0.25+0.3*j), 0]);
    if(i<3){
      const sl=0.7+R()*0.5, sa=a+(R()>0.5?0.7:-0.8);
      const st=new THREE.CylinderGeometry(0.028,0.045,sl,5);
      const sx=px+len*Math.sin(a), sy=py+len*Math.cos(a);
      st.rotateZ(-sa); st.translate(sx+sl*Math.sin(sa)/2,sy+sl*Math.cos(sa)/2,0);
      B.put(st,0x201919);
      for(let j=0;j<2;j++) spots.push([sx+sl*Math.sin(sa)*(0.4+0.35*j), sy+sl*Math.cos(sa)*(0.4+0.35*j), 0]);
    }
    px+=len*Math.sin(a); py+=len*Math.cos(a);
  }
  const n=o.n===undefined?18:o.n;
  for(let i=0;i<n;i++){
    const sp=spots[Math.floor(R()*spots.length)]||[px,py,0];
    const bl=new THREE.IcosahedronGeometry(0.11+R()*0.09,0);
    bl.translate(sp[0]+(R()-0.5)*0.6, sp[1]+(R()-0.5)*0.5, (R()-0.5)*0.6);
    B.put(bl,R()>0.5?0xc995a0:0xd8a7b1);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3138,emissive:0x080a0d}),{c:0x8f9fc0,i:0.2,p:2.7})));
  return g;
}

/* —— 尺素（鱼传尺素）：石上一卷素帛半展（合批 1 mesh） —— */
function makeSilk(o){
  o=o||{};
  const B=new GeoBag();
  const stone=rockGeo(0.55,0,seedRnd(o.seed===undefined?1855:o.seed));
  stone.scale(1.25,0.5,1.0); stone.translate(0,0.16,0); B.put(stone,0x1a2129);
  const roll=new THREE.CylinderGeometry(0.09,0.09,0.62,10); roll.rotateZ(Math.PI/2);
  roll.translate(0.14,0.46,0.02); B.put(roll,0xd9dfe6);
  const strip=new THREE.BoxGeometry(0.66,0.02,0.30); strip.translate(-0.42,0.40,0.04); B.put(strip,0xcfd6de);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a444e,emissive:0x0a0d12}),{c:0xaebfd4,i:0.3,p:2.6})));
  return g;
}

/* —— 恨砌（砌成此恨无重数）：四进石砌层台，一进退一进、没入雾里（合批 1 mesh） —— */
function makeHateTiers(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1851:o.seed);
  const n=o.n===undefined?4:o.n;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const w=(o.w===undefined?9.0:o.w)*(1-i*0.16), dep=(o.d===undefined?3.4:o.d)*(1-i*0.10);
    const h=0.9+i*0.30;
    const t=new THREE.BoxGeometry(w,h,dep);
    t.translate((R()-0.5)*1.2,h/2,-i*2.7); B.put(t,shadeColor(0x11161f,1-i*0.07));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x242e38,emissive:0x06090e}),{c:0x8f9fc0,i:0.16,p:2.8})));
  return g;
}

function bCoverTsuo(){ // 封面 · 郴州烟雨（雾失楼台的序曲：浓雾压江，渡口无人，旅人一点）
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:88,amp:0.4,freq:0.07,speed:0.4,flow:[0,0.3],
    deep:0x0b111a,shallow:0x15202e,skyc:0x1d2836,spec:0.5,y:-1.9});
  g.add(water.mesh);
  const bank=makeGround({r:46,c1:0x0c1016,c2:0x131a24});
  bank.mesh.position.set(0,-1.15,42); g.add(bank.mesh);
  const ridge=makeRange({r:250,h:20,layers:2,peaks:4,seed:1831,color:0x0a0e15,atmo:0x35455c,fogK:0.70,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,26); g.add(ridge.g);
  /* 远处楼台只剩一点影子（序曲：常没雾中，偶一显形） */
  const t1=makeLouTai({seed:1833,op:0.30,spd:0.11,scale:0.9}); t1.g.position.set(15,0,-50); t1.g.rotation.y=0.5; g.add(t1.g);
  /* 渡口：栈桥 + 系舟（月迷津渡的伏笔） */
  const pier=makePier({seed:1835}); pier.position.set(8,-1.6,-10); pier.rotation.y=-0.5; g.add(pier);
  const ferry=makeFerry({}); ferry.position.set(12,-1.72,-13); ferry.rotation.y=0.7; g.add(ferry);
  /* 旅人一点，正走向渡口 */
  const walker=makeFigure({pose:'独立',robe:0x272f3d,belt:0x3a4553,hat:'幞头',scale:0.92,rim:0.5,rimC:0x8f9fc0});
  walker.position.set(4.5,-1.35,-6); walker.rotation.y=-0.7; g.add(walker);
  const lowFog=makeFlow({n:340,box:[340,7,110],pos:[0,-0.8,-46],color:0x7e92ac,size:22,speed:3.4,maxA:0.28});
  g.add(lowFog.points);
  const mist=makeMist({n:10,spread:[250,26,120],pos:[0,8,-40],scale:82,color:0x8fa0b8,op:0.13});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:48,n:14,d:6,color:0x0b0f15,seed:1837,sway:0.85,tip:0x26323c});
  fg.g.position.set(0,-1.5,26); g.add(fg.g);
  addLights(g,{c:0x8fa0b8,i:0.30,p:[-30,60,30]},{c:0x232e3c,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); lowFog.update(t); mist.update(t,k);
    walker.update(t,k); fg.update(t,k); t1.update(t,k);
    ferry.position.y=-1.72+0.05*Math.sin(t*0.7); ferry.rotation.z=0.02*Math.sin(t*0.5);
  }};
}

function bWushiloutai(){ // 一（标志性瞬间）· 雾失楼台 —— 楼台显而复失、月迷津渡、孤馆闭春寒、杜鹃声里斜阳暮
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:84,amp:0.35,freq:0.08,speed:0.4,flow:[0,0.25],
    deep:0x0b111b,shallow:0x16222f,skyc:0x1e2937,spec:0.5,y:-1.85});
  g.add(water.mesh);
  /* 孤馆所在的岸 */
  const bank=new THREE.Mesh(new THREE.BoxGeometry(30,1.1,22),
    new THREE.MeshPhongMaterial({color:0x10151d,shininess:6,specular:0x232d39}));
  bank.position.set(-4,-0.55,-2); g.add(bank);
  const soil=makeGround({r:17,c1:0x0c1016,c2:0x131a23});
  soil.mesh.position.set(-4,0.02,-3); g.add(soil.mesh);
  const ridge=makeRange({r:240,h:16,layers:2,peaks:4,seed:1839,color:0x090d14,atmo:0x35455c,fogK:0.68,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-2); g.add(ridge.g);
  /* 标志性瞬间：楼台显而复失（近一座呼吸明灭，远一座常没雾中） */
  const lou1=makeLouTai({seed:1833,op:0.80,spd:0.28}); lou1.g.position.set(10,0,-22); lou1.g.rotation.y=-0.4; g.add(lou1.g);
  const lou2=makeLouTai({seed:1834,op:0.40,spd:0.12,scale:0.85}); lou2.g.position.set(26,0,-38); lou2.g.rotation.y=0.6; g.add(lou2.g);
  const towerMist=makeMist({n:5,spread:[26,8,18],pos:[15,7,-30],scale:26,color:0x8fa0b8,op:0.16});
  g.add(towerMist.g);
  /* 可堪孤馆闭春寒：孤馆一楹 + 窗冷光 + 馆前孤客 */
  const guan=makeGuan({}); guan.g.position.set(-6.5,0,-7.5); guan.g.rotation.y=0.35; g.add(guan.g);
  const poet=makeFigure({pose:'独立',robe:0x272f3d,belt:0x3a4553,hat:'幞头',beard:true,scale:1.26,rim:0.62,rimC:0x8f9fc0});
  poet.position.set(-4.6,0,-4.2); poet.rotation.y=0.55; g.add(poet);
  /* 月迷津渡：栈桥 + 系住的渡船（低垂淡月由 STAGES 天空悬于雾后） */
  const pier=makePier({seed:1835}); pier.position.set(7,-1.6,-12.5); pier.rotation.y=-0.55; g.add(pier);
  const ferry=makeFerry({}); ferry.position.set(10.5,-1.72,-15); ferry.rotation.y=0.6; g.add(ferry);
  /* 桃源望断无寻处：极远处一抹桃色微光，永远不可抵达 */
  const taoyuan=makeGlow({n:52,box:[36,11,18],pos:[27,5,-52],color:0xd8a7b1,size:7,speed:0.03,rise:0,maxA:0.16,add:false});
  g.add(taoyuan.points);
  /* 杜鹃声里：馆顶一只栖禽、雾中一只远飞 */
  const bird1=makeCuckooBird({}); bird1.g.position.set(-6.3,5.15,-6.9); bird1.g.scale.setScalar(0.85); bird1.g.rotation.y=1.2; g.add(bird1.g);
  const bird2=makeCuckooBird({fly:true}); bird2.g.scale.setScalar(0.8); g.add(bird2.g);
  /* 湿雾：本页主角——贴地雾流 + 大团雾阵 */
  const lowFog=makeFlow({n:380,box:[330,7,110],pos:[0,-0.7,-36],color:0x7e92ac,size:22,speed:3.2,maxA:0.30});
  g.add(lowFog.points);
  const mist=makeMist({n:10,spread:[240,22,110],pos:[0,7.5,-42],scale:78,color:0x8fa0b8,op:0.13});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:13,d:6,color:0x0b0f15,seed:1845,sway:0.8,tip:0x26323c});
  fg.g.position.set(8,-1.2,13); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.6,w:11,d:6,color:0x080b10,seed:1846,rim:0.12});
  rk.g.position.set(-17,-1.0,10); g.add(rk.g);
  addLights(g,{c:0x93a0b2,i:0.26,p:[-50,50,-20]},{c:0x26313f,i:0.70});
  let cryT=0;
  return {group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); lowFog.update(t); taoyuan.update(t);
    mist.update(t,k); towerMist.update(t,k);
    poet.update(t,k); fg.update(t,k); rk.update(t,k); guan.update(t,k);
    lou1.update(t,k); lou2.update(t,k); bird1.update(t,k); bird2.update(t,k);
    ferry.position.y=-1.72+0.05*Math.sin(t*0.7); ferry.rotation.z=0.02*Math.sin(t*0.5);
    /* 远飞杜鹃：自雾里横穿 */
    bird2.g.position.set(34-((t*1.15)%84),9.5+0.7*Math.sin(t*0.5),-30);
    bird2.g.rotation.y=Math.PI;
    /* 杜鹃啼：约 8.5s 一声（Node 无音频上下文时静默） */
    cryT+=dt;
    if(cryT>8.5){ cryT=0; cuckooCry(0,0.06); cuckooCry(1.1,0.045); }
  }};
}

function bChenjiang(){ // 二（末境·可点击）· 郴江之问 —— 驿寄梅花、鱼传尺素、砌成此恨；点击郴江：江流绕山而下，杜鹃三啼
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const water=makeWater({size:760,seg:92,amp:0.5,freq:0.07,speed:0.5,flow:[0,0.5],
    deep:0x0a1119,shallow:0x15202c,skyc:0x1d2836,spec:0.7,y:-1.9});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(26,1.1,20),
    new THREE.MeshPhongMaterial({color:0x0f141b,shininess:6,specular:0x222c38}));
  bank.position.set(-3,-0.55,5); g.add(bank);
  const soil=makeGround({r:15,c1:0x0c0f15,c2:0x121820});
  soil.mesh.position.set(-3,0.02,3); g.add(soil.mesh);
  const ridge=makeRange({r:270,h:18,layers:2,peaks:4,seed:1847,color:0x090d14,atmo:0x35455c,fogK:0.66,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-6); g.add(ridge.g);
  /* 郴山：雾中孤山（郴江所绕） */
  const hillGeo=rockGeo(8.5,1,seedRnd(1849)); hillGeo.scale(1.25,1.7,1.25);
  const hill=new THREE.Mesh(hillGeo,rimHook(new THREE.MeshPhongMaterial({color:0x141a24,shininess:10,
    specular:0x2b3644,emissive:0x070b11}),{c:0x8f9fc0,i:0.24,p:2.6}));
  hill.position.set(2,-1.7,-27); g.add(hill);
  /* 郴江绕山：三道水流沿山弧而行（点击后加速增亮），一道远去下潇湘 */
  function cur(n,box,pos,ry,spd,maxA){
    const f=makeFlow({n:n,box:box,pos:[0,0,0],color:0x93a8c0,size:15,speed:spd,maxA:maxA});
    f.points.position.set(pos[0],pos[1],pos[2]); f.points.rotation.y=ry; g.add(f.points);
    return f;
  }
  const c1=cur(200,[26,2.6,52],[-10.3,-1.05,-35.6],2.53,3.2,0.30);
  const c2=cur(200,[26,2.6,52],[2,-1.05,-42],Math.PI/2,3.2,0.32);
  const c3=cur(200,[26,2.6,52],[14.3,-1.05,-35.6],0.61,3.2,0.30);
  const cx=cur(240,[60,3,84],[2,-1.1,-62],Math.PI,3.8,0.32);
  /* 砌成此恨无重数：四进石砌层台，一进退一进没入雾里 */
  const tiers=makeHateTiers({seed:1851,n:4}); tiers.position.set(-9.5,0,-11); tiers.rotation.y=0.5; g.add(tiers);
  /* 孤馆客立于水边（背影四分之三，望江） */
  const poet=makeFigure({pose:'独立',robe:0x272f3d,belt:0x3a4553,hat:'幞头',beard:true,scale:1.30,rim:0.64,rimC:0x8f9fc0});
  poet.position.set(-2.6,0,0.8); poet.rotation.y=Math.PI+0.42; g.add(poet);
  /* 驿寄梅花：坡缘雾线上一株梅枝，疏萼粉白（杜鹃栖其枝头） */
  const plum=makePlumBranch({seed:1853}); plum.position.set(-8,0,9); plum.rotation.y=-0.5; g.add(plum);
  const bird=makeCuckooBird({}); bird.g.position.set(-5.3,5.35,10.5); bird.g.rotation.y=2.2; g.add(bird.g);
  /* 鱼传尺素：石上一卷素帛半展 */
  const silk=makeSilk({seed:1855}); silk.position.set(-4.4,0.0,3.6); silk.rotation.y=0.9; g.add(silk);
  /* 点击主体：江流前段的迸溅 */
  const burst=makeBurst({n:64,color:0xbcd0e4,pos:[2,-0.6,-34]}); g.add(burst.points);
  const lowFog=makeFlow({n:340,box:[320,7,110],pos:[0,-0.8,-40],color:0x7e92ac,size:22,speed:3.0,maxA:0.26});
  g.add(lowFog.points);
  const mist=makeMist({n:9,spread:[250,20,110],pos:[0,7.5,-46],scale:80,color:0x8fa0b8,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:42,n:12,d:6,color:0x0b0f15,seed:1857,sway:0.78,tip:0x26323c});
  fg.g.position.set(9,-1.5,14); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:7,color:0x080b10,seed:1859,rim:0.13});
  rk.g.position.set(-15,-1.1,10); g.add(rk.g);
  addLights(g,{c:0x8fa0b8,i:0.30,p:[-30,60,-20]},{c:0x242f3d,i:0.64});
  const api={group:g,update(t,dt){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ctl.t+=dt;
    if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/2.6);
    water.update(t); ridge.update(t,0); lowFog.update(t); mist.update(t,k);
    poet.update(t,k); fg.update(t,k); rk.update(t,k); bird.update(t,k);
    burst.update(t);
    /* 江流绕山：点击后加速增亮（流向叩问） */
    const boost=1+1.5*ctl.ext, amp=k*(0.30+0.34*ctl.ext);
    [c1,c2,c3].forEach(function(f){
      f.mat.uniforms.uMaxA.value=amp; f.mat.uniforms.uSpeed.value=3.2*boost; f.update(t);
    });
    cx.mat.uniforms.uMaxA.value=amp*1.05; cx.mat.uniforms.uSpeed.value=3.8*boost; cx.update(t);
    /* 杜鹃：点击后仰喙急啼 */
    bird.g.rotation.z=ctl.clicked?0.18*Math.sin(t*9):0.04*Math.sin(t*1.2);
  },click(){
    if(ctl.t<1.2)return;
    if(!ctl.clicked){
      ctl.clicked=true; api.clicked=true;
      burst.fire();
      cuckooCry(0,0.09); cuckooCry(0.55,0.075); cuckooCry(1.1,0.06);
      const fl=$('#flash'); fl.textContent='为谁流下潇湘去？'; fl.classList.remove('go');
      void fl.offsetWidth; fl.classList.add('go');
    }
  },clicked:false};
  return api;
}
