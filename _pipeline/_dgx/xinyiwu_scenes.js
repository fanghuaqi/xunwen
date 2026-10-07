/* ================= 辛夷坞 · 三境场景（宣纸留白 · 空山辛夷变体：卷首空山辛夷、木末红萼、涧户开落）
   本诗专属系统「开且落」：木末红萼（高枝先花后叶）、涧户寂无人（无人之境）。
   末境点击开且落 → 辛夷纷纷绽放（花体放大、花光点亮）、花瓣纷纷飘落（落花加密）、涧水微响，题字「纷纷开且落」。
   宣纸留白：纸底、淡墨远山、浓墨岩壁；不用金色辉光；辛夷的紫红是全页唯一浓色。 ================= */

/* —— 辛夷：先花后叶的木兰（高枝 + 大朵六瓣紫红花 + 红萼），合批 1 mesh —— */
function makeMagnoliaXY(o){
  o=o||{};
  const h=o.h===undefined?6.6:o.h, R=seedRnd(o.seed===undefined?1301:o.seed);
  const wood=o.wood===undefined?0x3a3630:o.wood, petal=o.petal===undefined?0xc0507a:o.petal;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[(R()-0.5)*0.5,h*0.52,0],h*0.07,h*0.032,8),wood);
  const tips=[];
  const nb=o.branches===undefined?7:o.branches;
  for(let i=0;i<nb;i++){
    const a=i/nb*6.283+R()*0.5, len=h*(0.34+R()*0.26);
    const p1=[Math.sin(a)*len,h*0.5+len*0.5,Math.cos(a)*len];
    B.put(limbGeo([0,h*0.5,0],p1,h*0.03,h*0.013,6),shadeColor(wood,1.25));
    tips.push(p1);
    if(R()<0.85){
      const p2=[p1[0]+Math.sin(a+0.5)*len*0.5,p1[1]+len*0.3,p1[2]+Math.cos(a+0.5)*len*0.45];
      B.put(limbGeo(p1,p2,h*0.016,h*0.006,5),shadeColor(wood,1.4));
      tips.push(p2);
    }
  }
  for(let i=0;i<tips.length;i++){
    const tp=tips[i];
    const nf=o.flowers===undefined?3:o.flowers;
    for(let k=0;k<nf;k++){
      const cx=tp[0]+(R()-0.5)*1.1, cy=tp[1]+(R()-0.4)*0.5+(o.up===undefined?0:o.up), cz=tp[2]+(R()-0.5)*1.1;
      const pr=0.30+R()*0.12;
      /* 红萼（花托） */
      const cal=new THREE.CylinderGeometry(pr*0.34,pr*0.46,0.26,7); cal.translate(cx,cy-pr*0.5,cz);
      B.put(cal,0x8a3a4a);
      /* 六瓣：向上斜张（杯状） */
      for(let q=0;q<6;q++){
        const aq=q/6*6.283+R()*0.3;
        const pf=new THREE.PlaneGeometry(pr*0.95,pr*2.1);
        pf.rotateX(-0.55+R()*0.2); pf.rotateY(aq);
        pf.translate(cx+Math.sin(aq)*pr*0.5,cy+pr*0.55,cz+Math.cos(aq)*pr*0.5);
        B.put(pf,shadeColor(petal,0.82+R()*0.4));
      }
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:9,
    specular:0x8a7a80,emissive:0x1a0c12,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xd0a0a8:o.rimC,i:0.26,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k,wind){ const kk=k===undefined?1:k, wd=wind===undefined?0:wind;
    g.rotation.z=(0.008+0.02*wd)*Math.sin(t*0.5+ph)*kk; };
  g.userData.update=g.update;
  return {g,update:g.update,mesh};
}

/* —— 花光：辛夷花上的暖粉光点（Sprite；点击开且落后次第点亮） —— */
function makeBloomGlowXY(o){
  o=o||{};
  const pos=o.pos||[], g=new THREE.Group(), items=[];
  for(let i=0;i<pos.length;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0xffb0c0:o.color,
      transparent:true,opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.position.set(pos[i][0],pos[i][1],pos[i][2]);
    s.scale.set(1.0,1.0,1); s.renderOrder=3; g.add(s);
    items.push({s:s,ph:i*0.61});
  }
  return {g,items,update:function(t,k,lit){
    const li=lit===undefined?0:lit;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const sc=(0.5+1.0*li)*(0.85+0.15*Math.sin(t*2.0+it.ph));
      it.s.scale.set(sc*1.5,sc*1.5,1);
    }
  }};
}

/* —— 纷纷落花：花瓣飘落（InstancedMesh；点击后加密加快） —— */
function makeFallingPetalsXY(o){
  o=o||{};
  const n=o.n===undefined?110:o.n, R=seedRnd(o.seed===undefined?1307:o.seed);
  const w=o.w===undefined?14:o.w, hh=o.h===undefined?9:o.h, d=o.d===undefined?10:o.d;
  const geo=new THREE.SphereGeometry(0.10,5,4); geo.scale(1.9,0.26,1.0);
  const mat=new THREE.MeshBasicMaterial({color:0xd0688c,transparent:true,opacity:0.78,depthWrite:false,side:THREE.DoubleSide});
  const mesh=new THREE.InstancedMesh(geo,mat,n);
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({x:(R()-0.5)*w,z:(R()-0.5)*d,y0:R()*hh,sp:0.5+R()*0.9,ph:R()*6.283,
      sway:0.5+R()*1.0,sc:0.7+R()*0.7});
  }
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  return {g,mesh,mat,update:function(t,k,speed){
    const kk=k===undefined?1:k, sp0=speed===undefined?1:speed;
    for(let i=0;i<n;i++){
      const it=items[i];
      let y=(it.y0-t*it.sp*sp0)%hh; y=(y+hh)%hh;
      const x=it.x+Math.sin(t*(0.6+1.1*sp0)+it.ph)*it.sway;
      const z=it.z+Math.cos(t*(0.5+sp0)+it.ph)*it.sway*0.6;
      dm.position.set(x,y,z);
      dm.rotation.set(Math.sin(t*1.2+it.ph)*0.9,it.ph+t*0.8,Math.sin(t*0.9+it.ph)*1.2);
      dm.scale.setScalar(it.sc);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* —— 涧户：山涧边的岩壁门户（两侧岩壁夹出一道涧口 + 涧水），合批 1 mesh —— */
function makeRavineXY(o){
  o=o||{};
  const w=o.w===undefined?22:o.w, h=o.h===undefined?10:o.h, R=seedRnd(o.seed===undefined?1311:o.seed);
  const rock=o.rock===undefined?0x4a4a46:o.rock;
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    for(let i=0;i<5;i++){
      const bw=6+R()*3.5, bh=h*(0.55+R()*0.5), bd=5+R()*3;
      const b=new THREE.BoxGeometry(bw,bh,bd);
      b.rotateY((R()-0.5)*0.5); b.rotateZ(s*(0.05+R()*0.12));
      b.translate(s*(w*0.5-2)+s*(R()-0.5)*3, bh*0.45, -i*3+(R()-0.5)*3);
      B.put(b,shadeColor(rock,0.85+R()*0.35));
    }
  });
  /* 涧底石与涧口 */
  const bed=new THREE.BoxGeometry(w*1.1,0.6,o.dl===undefined?26:o.dl); bed.translate(0,0.3,-12); B.put(bed,shadeColor(0x6a6a64,0.9));
  for(let i=0;i<12;i++){
    const r=new THREE.ConeGeometry(0.5+R()*0.7,0.7+R()*0.9,5);
    r.rotateZ((R()-0.5)*1.0); r.translate((R()-0.5)*w*0.9,0.6,(R()-0.5)*24); B.put(r,shadeColor(0x55554f,0.9+R()*0.3));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x7a7a72,emissive:0x0e0e0c}),{c:o.rimC===undefined?0x8a8a80:o.rimC,i:0.20,p:2.4}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?0:o.y,o.z===undefined?0:o.z);
  g.rotation.y=o.ry===undefined?0:o.ry;
  return {g,mesh};
}

/* ================= 三境 ================= */
function bCover(){ // 卷首 · 空山辛夷 —— 纸色空山、一株辛夷临涧
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xeae4d2,c2:0xc8cdac,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:44,layers:3,peaks:6,seed:2511,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.03,glow:0x8a8a78,y:-13});
  ridge.g.position.set(0,0,-96); g.add(ridge.g);
  const ravine=makeRavineXY({w:24,h:11,x:6,y:-1.4,z:-40,seed:1313}); g.add(ravine.g);
  const trees=[];
  [[-6,0,-10,1317,1.15],[-14,0,-18,1319,0.95],[10,0,-22,1321,0.9]].forEach(function(p){
    const t=makeMagnoliaXY({h:6.4,seed:p[3],scale:p[4]}); t.g.position.set(p[0],-1.4,p[2]); g.add(t.g); trees.push(t);
  });
  const falling=makeFallingPetalsXY({n:90,w:18,h:10,d:12,x:-2,y:-1.4,z:-10,seed:1323});
  g.add(falling.g);
  const ink=makeMist({n:7,spread:[220,24,110],pos:[0,9,-48],scale:74,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:170,box:[190,24,100],pos:[0,8,-24],color:0x7a7a70,size:9,speed:0.6,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:7,color:0xb8b2a0,seed:221,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-17,-1.6,34); g.add(fg.g);
  const fg2=makeForeground({kind:'树枝',w:28,n:8,d:6,color:0x3f3f38,seed:223,sway:0.5,rim:0.08,rimC:0x5a5a4e});
  fg2.g.position.set(18,-1.4,26); fg2.g.rotation.z=-0.18; g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-50,110,30]},{c:0xd8dac8,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ink.update(t,k); dust.update(t);
    const wd=0.25+0.15*Math.sin(t*0.4);
    for(let i=0;i<trees.length;i++)trees[i].update(t,k,wd);
    falling.update(t,k,0.5);
    fg.update(t,k); fg2.update(t,k);
  }};
}
function bMumo(){ // 一 · 木末红萼 —— 木末芙蓉花，山中发红萼
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d0,c2:0xc6cbab,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:48,layers:3,peaks:6,seed:2521,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.03,glow:0x8a8a78,y:-14});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 木末：辛夷高树在近景右侧，花在枝梢（仰观） */
  const main=makeMagnoliaXY({h:7.2,seed:1327,scale:1.2,flowers:3}); main.g.position.set(5,-1.3,-8); g.add(main.g);
  const tree2=makeMagnoliaXY({h:5.6,seed:1329,scale:1.0,flowers:2}); tree2.g.position.set(-9,-1.3,-14); g.add(tree2.g);
  const tree3=makeMagnoliaXY({h:4.6,seed:1331,scale:0.9,flowers:2}); tree3.g.position.set(14,-1.3,-18); g.add(tree3.g);
  /* 山中岩壁（空山之体） */
  const ravine=makeRavineXY({w:26,h:12,x:-2,y:-1.3,z:-44,seed:1333}); g.add(ravine.g);
  const falling=makeFallingPetalsXY({n:90,w:16,h:10,d:12,x:2,y:-1.3,z:-8,seed:1337});
  g.add(falling.g);
  const ink=makeMist({n:7,spread:[210,22,100],pos:[0,9,-46],scale:72,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:160,box:[180,22,94],pos:[0,8,-22],color:0x7a7a70,size:9,speed:0.6,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'坡石',n:3,r:3.2,w:17,d:7,color:0xc0baa8,seed:227,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-15,-1.5,20); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0xb2ac9a,seed:229,sway:0.6,tip:0x5a5a4a});
  fg2.g.position.set(16,-1.4,18); g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-48,105,28]},{c:0xd8dac8,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); ink.update(t,k); dust.update(t);
      const wd=0.3+0.2*Math.sin(t*0.42);
      main.update(t,k,wd); tree2.update(t,k,wd); tree3.update(t,k,wd);
      falling.update(t,k,0.6);
      fg.update(t,k); fg2.update(t,k);
    },onEnter(){ pluck(3,0.4,0.08); }};
}
function bJianhu(){ // 二（末境·可点击）· 涧户开落 —— 涧户寂无人，纷纷开且落
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,pulse:0,bloom:0,fall:0};
  const grd=makeGround({r:260,c1:0xe9e2cf,c2:0xc5cbaa,y:-1.3}); g.add(grd.mesh);
  const ridge=makeRange({r:270,h:46,layers:3,peaks:6,seed:2531,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.62,glowK:0.03,glow:0x8a8a78,y:-14});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  /* 涧户：两侧岩壁夹出涧口（"涧户"） */
  const ravine=makeRavineXY({w:28,h:13,x:0,y:-1.3,z:-30,dl:30,seed:1341}); g.add(ravine.g);
  /* 涧水（一线） */
  const water=makeWater({size:26,seg:22,amp:0.05,freq:0.2,speed:0.5,flow:[0.2,0.5],spec:1.0,
    deep:0x6a7a86,shallow:0x9aa8b0,skyc:0xb8c4cc,moonDir:[0,-80,-100],y:-0.55});
  water.mesh.scale.set(0.7,1,0.5); water.mesh.position.set(0,-0.55,-16); g.add(water.mesh);
  /* 一株辛夷在涧户之前（花在木末） */
  const magno=makeMagnoliaXY({h:6.8,seed:1347,scale:1.15,flowers:3}); magno.g.position.set(2.5,-1.3,-9); g.add(magno.g);
  const magno2=makeMagnoliaXY({h:5.0,seed:1349,scale:1.0,flowers:2}); magno2.g.position.set(-9,-1.3,-13); g.add(magno2.g);
  /* 花光：待点亮 */
  const pos=[];
  for(let i=0;i<10;i++){
    const a=i/10*6.283;
    pos.push([2.5+Math.sin(a)*3.2,3.6+Math.cos(a*1.7)*2.2,-9+Math.cos(a)*2.6]);
  }
  const glow=makeBloomGlowXY({pos:pos}); g.add(glow.g);
  /* 纷纷落花（点击后加密加快） */
  const falling=makeFallingPetalsXY({n:130,w:20,h:11,d:14,x:1,y:-1.3,z:-8,seed:1351});
  g.add(falling.g);
  const ink=makeMist({n:7,spread:[210,22,100],pos:[0,9,-46],scale:72,color:0x8a8578,op:0.10}); g.add(ink.g);
  const dust=makeFlow({n:160,box:[180,22,94],pos:[0,8,-22],color:0x7a7a70,size:9,speed:0.6,maxA:0.10});
  g.add(dust.points);
  const fg=makeForeground({kind:'岩壁',n:3,r:3.0,w:15,d:6,color:0xb8b2a0,seed:231,rim:0.10,rimC:0x6a6a5a});
  fg.g.position.set(-14,-1.4,13); g.add(fg.g);
  const fg2=makeForeground({kind:'芦苇',w:16,n:8,d:5,color:0xb4ae9c,seed:233,sway:0.6,tip:0x5a5a4a});
  fg2.g.position.set(14,-1.3,11); g.add(fg2.g);
  addLights(g,{c:0xf0ead8,i:0.50,p:[-46,100,26]},{c:0xd8dac8,i:0.64});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){ ctl.bloom=Math.min(1,ctl.bloom+dt/2.4); ctl.fall=Math.min(1,ctl.fall+dt/2.0); }
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const bl=ctl.bloom+0.5*ctl.pulse, fa=ctl.fall+0.5*ctl.pulse;
      ridge.update(t,0); ink.update(t,k); dust.update(t); water.update(t);
      const wd=0.25+0.5*bl;
      magno.update(t,k,wd); magno2.update(t,k,wd);
      glow.update(t,k,bl);
      falling.update(t,k,0.5+1.6*fa);
      fg.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.00,0.12); pluck(4,0.22,0.10); pluck(5,0.45,0.09); pluck(3,0.70,0.08);
        const fl=$('#flash'); fl.textContent='纷纷开且落'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      ctl.pulse=1;                 /* 可反复点：花再开一分，花再落一阵 */
    },clicked:false};
  return api;
}
