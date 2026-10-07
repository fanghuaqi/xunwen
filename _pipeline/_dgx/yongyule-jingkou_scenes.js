/* ================= 永遇乐·京口北固亭怀古 · 四境场景（大漠金戈：千古江山、金戈铁马、烽火扬州、凭谁问） =================
   美术立意：大漠金戈赛道——底色 #120d08、雾 #1a120a 系、accent=#c9a06a（人物边缘光/旗纹/祠庙轮廓光），禁艳金。
   全页意象链：斜阳—尘霭—战旗—烽烟—神鸦社鼓。五典连环（孙权/刘裕/刘义隆/佛狸/廉颇）是教学骨架。
   标志性瞬间：境②「金戈铁马气吞万里如虎」——斜阳巷陌外铁骑碾尘（全页最亮），
              对 境④「佛狸祠下神鸦社鼓」——沦陷区的太平假象（香火最暖、心底最寒）。
   末境点击（queue interact）：点击烽火扬州路——烽烟起落 + 「凭谁问」问句悬空。
   情感曲线：怅惘无觅 → 昂扬追慕 → 沉痛警醒 → 最沉一问（收束留白）。 */

/* —— 低垂昏黄的斜阳（本诗自有光源，替代蓝白月轮；uAlpha 由 update 乘 fadeK）—— */
function makeXieyang(o){
  o=o||{};
  const sun=makeMoon({r:o.r===undefined?9:o.r,base:o.base===undefined?0xffd9a0:o.base,
    dark:o.dark===undefined?0xb06a28:o.dark,hazeColor:o.hazeColor===undefined?0xff9a4a:o.hazeColor,
    haze:o.haze===undefined?0.42:o.haze,phase:0});
  sun.group.position.set(o.x===undefined?-78:o.x,o.y===undefined?10:o.y,o.z===undefined?-250:o.z);
  return {g:sun.group,update(t,k){ const kk=k===undefined?1:k;
    sun.update(t); sun.mat.uniforms.uAlpha.value=kk; }};
}

/* —— 北固亭：台基+四柱+额枋+攒尖顶+顶珠+栏杆（合批 1 mesh）——与姐妹篇《南乡子》同构，accent 换 #c9a06a —— */
function makeBeigu(o){
  o=o||{};
  const wood=o.color===undefined?0x1c130a:o.color, wood2=shadeColor(wood,1.7);
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(9,1.4,7); base.translate(0,0.7,0); B.put(base,shadeColor(wood,1.1));
  [[-3.3,-2.3],[3.3,-2.3],[-3.3,2.3],[3.3,2.3]].forEach(function(p){
    const c=new THREE.CylinderGeometry(0.20,0.25,4.6,8); c.translate(p[0],3.7,p[1]); B.put(c,wood2);
  });
  const beam=new THREE.BoxGeometry(8.8,0.5,6.4); beam.translate(0,6.25,0); B.put(beam,shadeColor(wood,1.3));
  const roof=new THREE.ConeGeometry(6.3,2.5,4); roof.rotateY(Math.PI/4); roof.translate(0,7.65,0); B.put(roof,shadeColor(wood,1.5));
  const orb=new THREE.SphereGeometry(0.42,10,8); orb.translate(0,9.15,0); B.put(orb,0x8a6a3a);
  const rl=new THREE.BoxGeometry(7.4,0.12,0.14); rl.translate(0,2.52,2.35); B.put(rl,wood2);
  for(let i=0;i<5;i++){
    const p=new THREE.BoxGeometry(0.13,1.0,0.13); p.translate(-3.4+i*1.7,2.0,2.35); B.put(p,wood);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a1c10,emissive:0x0a0704}),{c:0xc9a06a,i:o.rim===undefined?0.3:o.rim,p:2.6})));
  return g;
}
/* —— 战旗：旗杆+杆顶+旗面（旗面摆动，2 draw call）——「大纛」猎猎 —— */
function makeZhanqi(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.08,0.11,h,6); pole.translate(0,h/2,0); B.put(pole,0x0b0806);
  const fin=new THREE.SphereGeometry(0.16,8,6); fin.translate(0,h+0.1,0); B.put(fin,0x6a5030);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc9a06a,i:0.2,p:2.6})));
  const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.7,1.7,5,2),
    new THREE.MeshPhongMaterial({color:o.flagC===undefined?0x6a1e12:o.flagC,side:THREE.DoubleSide,
      shininess:6,specular:0x3a2418}));
  fl.position.set(1.35,h-1.15,0); g.add(fl);
  return {g,fl,ph,update(t){ fl.rotation.y=0.42*Math.sin(t*1.5+ph)+0.16*Math.sin(t*2.6+ph*1.7); }};
}

/* —— 舞榭歌台残迹：土冈 + 残台基 + 断柱三根（两斜一桩）+ 坠梁（合批 1 mesh）——「风流总被雨打风吹去」 */
function makeXietai(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19403:o.seed);
  const B=new GeoBag();
  const mound=rockGeo(9,1,R); mound.scale(3.0,0.20,1.9); mound.translate(0,-1.55,0); B.put(mound,shadeColor(0x241a10,0.8+0.2*R()));
  const tai=new THREE.BoxGeometry(11,1.1,8); tai.rotateY(0.12); tai.translate(0,0.55,0); B.put(tai,0x1c130a);
  const edge=new THREE.BoxGeometry(11.3,0.14,8.3); edge.rotateY(0.12); edge.translate(0,1.1,0); B.put(edge,shadeColor(0x241a10,1.5));
  [[-3.6,-2.4,0.30],[-0.5,-2.9,-0.42],[3.4,-2.2,0.18]].forEach(function(p,i){
    const h=[3.1,1.3,4.2][i];
    const c=new THREE.CylinderGeometry(0.26,0.32,h,8);
    c.rotateZ(p[2]); c.translate(p[0],1.1+h/2,p[1]); B.put(c,shadeColor(0x2a1c10,0.9+0.25*R()));
  });
  const beam=new THREE.BoxGeometry(4.6,0.34,0.34); beam.rotateZ(0.52); beam.rotateY(0.5);
  beam.translate(1.6,0.7,1.8); B.put(beam,shadeColor(0x1e140b,1.1));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a1f12,emissive:0x060402}),{c:0xc9a06a,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  return g;
}

/* —— 斜阳草树·寻常巷陌：草舍（土墙+苫草顶）合批 1 mesh ——寄奴故居 */
function makeCaoshe(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19405:o.seed);
  const B=new GeoBag();
  const w=o.w===undefined?4.6:o.w, d=o.d===undefined?3.6:o.d, h=o.h===undefined?2.1:o.h;
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h/2,0); B.put(body,shadeColor(0x2e2013,0.75+0.2*R()));
  const door=new THREE.BoxGeometry(0.9,1.4,0.1); door.translate(w*0.18,0.7,d/2+0.03); B.put(door,0x0d0906);
  const roof=new THREE.ConeGeometry(Math.max(w,d)*0.78,1.7,4); roof.rotateY(Math.PI/4);
  roof.scale(1,1,d/w); roof.translate(0,h+0.82,0); B.put(roof,shadeColor(0x3a2c16,0.85+0.2*R()));
  const ridge=new THREE.BoxGeometry(w*0.98,0.12,0.3); ridge.translate(0,h+1.62,0); B.put(ridge,0x241a0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x241a10,emissive:0x050302}),{c:0xc9a06a,i:0.14,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}
/* —— 篱笆一排（柴枝合批 1 mesh）—— */
function makeZhalan(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19407:o.seed);
  const w=o.w===undefined?9:o.w;
  const B=new GeoBag();
  for(let i=0;i<=7;i++){
    const p=new THREE.CylinderGeometry(0.05,0.07,1.15,5);
    p.rotateZ((R()-0.5)*0.16); p.translate(-w/2+w*i/7,0.55,0); B.put(p,shadeColor(0x241a10,0.7+0.3*R()));
  }
  for(let k=0;k<2;k++){
    const r=new THREE.CylinderGeometry(0.035,0.035,w,5);
    r.rotateZ(Math.PI/2); r.rotateX((R()-0.5)*0.1); r.translate(0,0.35+k*0.55,0.05); B.put(r,shadeColor(0x2a1c10,0.8));
  }
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,specular:0x1d160e,emissive:0x040302})));
  return g;
}

/* —— 铁骑（人马合体，合批成一份几何）：马身/颈/首/四蹄/尾 + 骑手/长戈 ——军阵用 InstancedMesh 摆一片 */
function tieqiGeo(){
  const B=new GeoBag();
  const barrel=new THREE.CylinderGeometry(0.40,0.47,2.0,7); barrel.rotateZ(Math.PI/2);
  barrel.scale(1,1.08,0.86); barrel.translate(0,1.16,0); B.put(barrel,0x1c140c);
  const chest=new THREE.SphereGeometry(0.45,8,7); chest.translate(0.92,1.14,0); B.put(chest,0x1c140c);
  const rump=new THREE.SphereGeometry(0.42,8,7); rump.translate(-0.92,1.10,0); B.put(rump,0x1a130b);
  const neck=new THREE.CylinderGeometry(0.15,0.24,0.95,7); neck.rotateZ(-0.66); neck.translate(1.16,1.56,0); B.put(neck,0x1c140c);
  const head=new THREE.BoxGeometry(0.52,0.21,0.20); head.rotateZ(-0.38); head.translate(1.60,1.86,0); B.put(head,0x17100a);
  const ear=new THREE.ConeGeometry(0.05,0.16,5); ear.translate(1.42,2.06,0); B.put(ear,0x17100a);
  const mane=new THREE.BoxGeometry(0.72,0.14,0.10); mane.rotateZ(-0.62); mane.translate(1.10,1.82,0); B.put(mane,0x110c07);
  const tail=new THREE.ConeGeometry(0.09,0.85,6); tail.rotateZ(2.55); tail.translate(-1.18,1.30,0); B.put(tail,0x110c07);
  /* 四蹄（奔姿各有角度） */
  [[0.68,0.20,0.34],[-0.62,0.20,-0.30],[0.60,-0.20,-0.24],[-0.70,-0.20,0.26]].forEach(function(L){
    const leg=new THREE.CylinderGeometry(0.055,0.07,1.10,5);
    leg.rotateZ(L[2]); leg.translate(L[0],0.55,L[1]); B.put(leg,0x140e09);
  });
  /* 骑手：上身/头/盔/一腿夹马腹/一臂前伸擎戈 */
  const torso=new THREE.CylinderGeometry(0.16,0.26,0.66,7); torso.translate(-0.12,1.98,0); B.put(torso,0x2e2016);
  const hd=new THREE.SphereGeometry(0.145,8,6); hd.translate(-0.12,2.46,0); B.put(hd,0xc89878);
  const helm=new THREE.SphereGeometry(0.165,8,6); helm.scale(1,0.8,1); helm.translate(-0.12,2.50,0); B.put(helm,0x3a3226);
  const leg=new THREE.CylinderGeometry(0.05,0.06,0.62,5); leg.rotateZ(0.42); leg.translate(0.14,1.42,0.24); B.put(leg,0x241a12);
  const arm=new THREE.CylinderGeometry(0.045,0.05,0.52,5); arm.rotateZ(-1.05); arm.translate(0.42,2.02,0.10); B.put(arm,0x2e2016);
  const ge=new THREE.CylinderGeometry(0.026,0.026,2.7,5); ge.rotateZ(Math.PI/2); ge.rotateY(0.06);
  ge.translate(0.75,2.02,0.14); B.put(ge,0x2a1c10);
  const blade=new THREE.BoxGeometry(0.34,0.10,0.02); blade.translate(2.02,2.12,0.16); B.put(blade,0x6a6458);
  return mergeGeos(B.list);
}
/* —— 金戈铁马：铁骑阵（InstancedMesh 1 draw call，奔姿起伏）——「气吞万里如虎」 */
function makeTieqi(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19409:o.seed);
  const list=o.list===undefined?[[0,0]]:o.list;
  const mesh=new THREE.InstancedMesh(tieqiGeo(),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
      specular:0x3a2f1e,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.22:o.rim,p:2.6}),list.length);
  const dm=new THREE.Object3D(), base=[];
  for(let i=0;i<list.length;i++){
    base.push({x:list[i][0],z:list[i][1],ry:(o.faceLeft===false?0:Math.PI)+(R()-0.5)*0.10,
      s:(o.sMin===undefined?0.95:o.sMin)+R()*((o.sMax===undefined?1.1:o.sMax)-(o.sMin===undefined?0.95:o.sMin)),ph:R()*6.283});
  }
  mesh.frustumCulled=false;
  const put=function(t){
    for(let i=0;i<base.length;i++){
      const b=base[i];
      dm.position.set(b.x,Math.abs(Math.sin(t*3.1+b.ph))*0.055,b.z);
      dm.rotation.set(0,b.ry+0.012*Math.sin(t*1.1+b.ph),0);
      dm.scale.setScalar(b.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  };
  put(0);
  return {mesh,update:put};
}
/* —— 前锋骑（合批 1 mesh，位在阵首）+ 大纛战旗（旗面摆动）—— */
function makeQiansfeng(o){
  o=o||{};
  const mesh=new THREE.Mesh(tieqiGeo(),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
      specular:0x3a2f1e,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.26:o.rim,p:2.6}));
  mesh.frustumCulled=false; mesh.scale.setScalar(o.scale===undefined?1.18:o.scale);
  mesh.rotation.y=Math.PI;
  const g=new THREE.Group(); g.add(mesh);
  return {g,update(t){ g.position.y=Math.abs(Math.sin(t*2.9+1.3))*0.06; }};
}

/* —— 烽燧：夯土方台（n 座合批 1 mesh），顶置火池 ——烽火扬州路 */
function makeFengta(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19411:o.seed);
  const list=o.list||[]; const B=new GeoBag();
  for(let i=0;i<list.length;i++){
    const x=list[i][0], z=list[i][1], h=list[i][2], r=1.35+h*0.30;
    const body=new THREE.BoxGeometry(r*1.5,h,r*1.5); body.rotateY(R()*0.4); body.translate(x,h/2,z);
    B.put(body,shadeColor(0x2a1c10,0.65+0.35*R()));
    const cap=new THREE.BoxGeometry(r*1.75,0.5,r*1.75); cap.translate(x,h+0.25,z); B.put(cap,shadeColor(0x33220f,0.85));
    const skirt=new THREE.BoxGeometry(r*2.2,0.9,r*2.2); skirt.translate(x,0.45,z); B.put(skirt,shadeColor(0x1e140b,0.8));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x241a10,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.14:o.rim,p:2.6})));
  return g;
}
/* —— 烽燧火（焰+火星+辉光+烟柱）：lvl 0→1 点燃，update(t,k) 统一乘 fadeK ——「烽烟起落」 */
function makeFenghuo(o){
  o=o||{};
  const fl=makeFlame({h:o.h===undefined?2.8:o.h,w:o.w===undefined?1.15:o.w,planes:3,
    embers:16,spark:false,light:o.light||0,core:0xffd090,outer:0xd84a14,wide:0.34});
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff8a3a,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(9,9,1); glow.renderOrder=3;
  const smoke=makeGlow({n:o.smokeN===undefined?24:o.smokeN,box:[2.4,15,2.4],
    pos:[0,7.5,0],color:0x7a5c3a,size:24,speed:0.34,rise:1,add:true,maxA:o.smokeMax===undefined?0.30:o.smokeMax});
  smoke.points.frustumCulled=false;
  const g=new THREE.Group(); g.add(fl.g); g.add(glow); g.add(smoke.points);
  let lvl=1, smokeBase=smoke.mat.uniforms.uMaxA.value;
  return {g,lvl,glow,smokeMat:smoke.mat,update(t,k){
    const kk=k===undefined?1:k;
    fl.update(t,kk);
    glow.material.opacity=kk*0.5*lvl;
    smoke.mat.uniforms.uMaxA.value=smokeBase*lvl;
  },setLvl(v){
    lvl=Math.max(0.0001,v);
    fl.g.visible=lvl>0.005;
    fl.g.scale.setScalar(0.001+1.12*lvl);
  }};
}

/* —— 佛狸祠：台基+殿身+庑殿顶+正脊+台阶（合批 1 mesh）——异族君主的行宫祠庙 */
function makeFoli(o){
  o=o||{};
  const B=new GeoBag();
  const tai=new THREE.BoxGeometry(7.4,1.1,5.4); tai.translate(0,0.55,0); B.put(tai,0x211609);
  const step=new THREE.BoxGeometry(1.9,0.28,0.9); step.translate(0,0.42,3.1); B.put(step,0x1a1208);
  const body=new THREE.BoxGeometry(4.6,2.7,3.3); body.translate(0,2.45,0); B.put(body,0x1c1208);
  const door=new THREE.BoxGeometry(1.0,1.5,0.1); door.translate(0,1.85,1.68); B.put(door,0x0a0705);
  const roof=new THREE.ConeGeometry(4.1,1.75,4); roof.rotateY(Math.PI/4); roof.scale(1,1,0.78);
  roof.translate(0,4.65,0); B.put(roof,0x2a1c10);
  const ridge=new THREE.BoxGeometry(4.3,0.16,0.34); ridge.translate(0,5.35,0); B.put(ridge,0x181008);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x2a1c10,emissive:0x060402}),{c:0xc9a06a,i:o.rim===undefined?0.24:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}
/* —— 老树+栖鸦（枯枝合批 1 mesh，枝上三两点鸦影）——「神鸦」栖处 */
function makeLaoshu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?19413:o.seed);
  const h=o.h===undefined?8.5:o.h;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.30,0.62,h,7); trunk.rotateZ((R()-0.5)*0.14);
  trunk.translate(0,h/2,0); B.put(trunk,0x14100a);
  for(let i=0;i<5;i++){
    const a=i/5*Math.PI*2+R()*0.8, L=2.2+R()*2.6, y=h*(0.52+0.3*R());
    const br=new THREE.CylinderGeometry(0.045,0.11,L,5);
    br.rotateZ(0.9+R()*0.5); br.rotateY(a);
    br.translate(Math.cos(a)*L*0.34,y,Math.sin(a)*L*0.34); B.put(br,0x110d08);
    if(R()<0.75){
      const crow=new THREE.ConeGeometry(0.13,0.42,5); crow.rotateX(Math.PI/2);
      crow.rotateY(a+Math.PI/2); crow.translate(Math.cos(a)*L*0.6,y+0.30,Math.sin(a)*L*0.6);
      B.put(crow,0x080604);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc9a06a,i:o.rim===undefined?0.12:o.rim,p:2.8})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}
/* —— 绕祠神鸦（InstancedMesh 1 draw call，绕祠盘旋）—— */
function makeWuya(o){
  o=o||{};
  const n=o.n===undefined?7:o.n, R=seedRnd(o.seed===undefined?19415:o.seed);
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.11,0.5,5); body.rotateX(Math.PI/2); B.put(body,0x080604);
  const w1=new THREE.PlaneGeometry(0.55,0.16); w1.rotateX(-Math.PI/2); w1.rotateZ(0.22); w1.translate(0.22,0.04,0.16); B.put(w1,0x0a0705);
  const w2=new THREE.PlaneGeometry(0.55,0.16); w2.rotateX(-Math.PI/2); w2.rotateZ(-0.22); w2.translate(0.22,0.04,-0.16); B.put(w2,0x0a0705);
  const mesh=new THREE.InstancedMesh(mergeGeos(B.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      specular:0x241a10,emissive:0x040302}),{c:0xc9a06a,i:o.rim===undefined?0.18:o.rim,p:2.8}),n);
  mesh.frustumCulled=false;
  const base=[];
  for(let i=0;i<n;i++)base.push({r:4.5+R()*9,h:9+R()*6,w:(R()<0.5?1:-1)*(0.22+R()*0.3),a:R()*6.283,s:0.8+R()*0.5});
  const dm=new THREE.Object3D();
  const put=function(t){
    for(let i=0;i<n;i++){
      const b=base[i], a=b.a+t*b.w;
      dm.position.set(Math.cos(a)*b.r, b.h+0.5*Math.sin(t*0.9+b.a), Math.sin(a)*b.r);
      dm.rotation.set(0,-(a+Math.PI/2)*(b.w>0?1:1),0);
      dm.scale.setScalar(b.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  };
  put(0);
  return {mesh,update:put};
}
/* —— 社鼓：鼓身+鼓面+交叉鼓架（合批 1 mesh）——「社鼓」声声 */
function makeShegu(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.62,0.62,0.46,14); body.rotateX(Math.PI/2); body.translate(0,1.28,0);
  B.put(body,0x4a1812);
  const face=new THREE.CircleGeometry(0.62,14); face.translate(0,1.28,0.24); B.put(face,0x8a6a4a);
  [[-0.5,0.28],[0.5,-0.28]].forEach(function(p){
    const leg=new THREE.BoxGeometry(0.09,1.35,0.09); leg.rotateZ(p[1]); leg.translate(p[0],0.62,0); B.put(leg,0x1c130a);
  });
  const bar=new THREE.BoxGeometry(1.34,0.08,0.1); bar.translate(0,1.06,0); B.put(bar,0x241a10);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a2418,emissive:0x060402}),{c:0xc9a06a,i:0.2,p:2.6})));
  g.scale.setScalar(o.scale===undefined?0.9:o.scale);
  return g;
}
/* —— 「凭谁问」问句悬空（canvas 题字，fog:false；opacity=k*op0*lvl 交给末境点击）—— */
const YYK_QUESTION='凭谁问 —— 廉颇老矣，尚能饭否？';
function makeWenju(o){
  o=o||{};
  const c=document.createElement('canvas'); c.width=1280; c.height=128;
  const x=c.getContext('2d');
  x.font='64px "Ma Shan Zheng","Kaiti SC","STKaiti","KaiTi","Noto Serif SC",serif';
  x.textAlign='center'; x.textBaseline='middle';
  x.shadowColor='rgba(201,160,106,.85)'; x.shadowBlur=16;
  x.fillStyle='#ecd6ac';
  x.fillText(YYK_QUESTION,640,68);
  const mat=new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(c),transparent:true,
    opacity:0.92,depthWrite:false,fog:false});
  const mesh=new THREE.Mesh(new THREE.PlaneGeometry(46,4.6),mat);
  mesh.renderOrder=6; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const y0=o.y===undefined?26:o.y;
  g.position.set(o.x===undefined?0:o.x,y0,o.z===undefined?-84:o.z);
  return {g,update(t,k,lvl){ const kk=k===undefined?1:k;
    mat.opacity=kk*0.92*lvl;
    mesh.position.y=y0+0.5*Math.sin(t*0.4);
  }};
}

function bCoverYyk(){ // 封面 · 斜阳暮色里的京口北固亭（尘霭低回，江声如诉）
  const g=new THREE.Group();
  const water=makeWater({size:680,seg:88,amp:0.5,freq:0.08,speed:0.5,flow:[0,0.5],
    deep:0x120d08,shallow:0x241a10,skyc:0x3a2a18,spec:0.25,moonDir:[-0.55,0.14,-0.8],moonColor:0xb08858,y:-2.0});
  g.add(water.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:19401,color:0x0b0806,atmo:0x332414,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-16); g.add(ridge.g);
  const sun=makeXieyang({x:-72,y:9,z:-240}); g.add(sun.g);
  /* 崖上北固亭剪影（斜照里的「满眼风光」） */
  const cliff=new THREE.Group();
  const cb=new GeoBag();
  const r1=rockGeo(9,1,seedRnd(19403)); r1.scale(2.1,1.15,1.3); r1.translate(0,2.6,-26); cb.put(r1,0x0d0906);
  const r2=rockGeo(6,1,seedRnd(19405)); r2.scale(1.7,0.9,1.1); r2.translate(-9,1.9,-29); cb.put(r2,0x0b0805);
  const r3=rockGeo(6,1,seedRnd(19407)); r3.scale(1.8,1.0,1.2); r3.translate(9,2.1,-28); cb.put(r3,0x0c0906);
  cliff.add(cb.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xc9a06a,i:0.12,p:2.8})));
  const pav=makeBeigu({}); pav.position.set(0,4.6,-26); pav.scale.setScalar(1.0); cliff.add(pav);
  g.add(cliff);
  const motes=makeGlow({n:50,box:[220,34,130],pos:[0,10,-40],color:0xc09a68,size:7,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  const flow=makeFlow({n:130,box:[220,12,80],pos:[0,7,-30],color:0x9a7c50,size:15,speed:4.5,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:8,spread:[250,26,140],pos:[0,10,-54],scale:80,color:0x8a6f4e,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:48,n:13,d:6,color:0x0a0704,seed:19409,sway:0.9,tip:0x3a2c16});
  fg.g.position.set(0,-1.8,26); g.add(fg.g);
  addLights(g,{c:0xc09058,i:0.36,p:[-40,60,30]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sun.update(t,k); motes.update(t); flow.update(t); mist.update(t,k);
    fg.update(t,k);
  }};
}
function bQianGu(){ // 一 · 千古江山 —— 登亭北望：江山依旧，英雄无觅；舞榭歌台空对雨打风吹
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.5,freq:0.08,speed:0.55,flow:[0,0.8],
    deep:0x100c08,shallow:0x201810,skyc:0x2e2013,spec:0.22,moonDir:[-0.5,0.16,-0.85],moonColor:0xb08858,y:-6.0});
  g.add(water.mesh);
  const ridge=makeRange({r:340,h:16,layers:2,peaks:5,seed:19411,color:0x0a0705,atmo:0x302212,fogK:0.60,glowK:0.05,y:-18});
  ridge.g.position.set(0,0,-30); g.add(ridge.g);
  const sun=makeXieyang({x:-64,y:8,z:-235}); g.add(sun.g);
  /* 北固亭头：台面 + 亭柱一对 + 凭栏按剑北望的词人背影 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(30,2.6,14),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  tai.position.set(0,-0.3,-4); g.add(tai);
  const top=makeGround({r:12,c1:0x0e0a07,c2:0x16100a});
  top.mesh.position.set(0,1.05,-4); g.add(top.mesh);
  const pilL=makePillar({h:9,top:false,color:0x1c1208}); pilL.g.position.set(-7,1.05,-1.5); g.add(pilL.g);
  const pilR=makePillar({h:9,top:false,color:0x1c1208}); pilR.g.position.set(7.5,1.05,-2.2); g.add(pilR.g);
  const poet=makeFigure({pose:'按剑',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.35,rim:0.62,rimC:0xc9a06a});
  poet.position.set(2.0,1.05,-3.0); poet.rotation.y=Math.PI-0.22; g.add(poet);
  /* 舞榭歌台残迹：土冈上的断柱残基，被岁月打吹而去 */
  const xie=makeXietai({seed:19413}); xie.position.set(-17,-2.4,-50); xie.scale.setScalar(1.15); g.add(xie);
  const wind=makeFlow({n:190,box:[200,13,60],pos:[0,7.5,-56],color:0x6a5c48,size:19,speed:5.5,maxA:0.20});
  g.add(wind.points);
  const motes=makeGlow({n:36,box:[200,26,100],pos:[0,10,-40],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[260,22,120],pos:[0,7,-70],scale:84,color:0x7a674c,op:0.11});
  g.add(mist.g);
  const fg=makeForeground({kind:'栏杆',w:26,h:2.8,color:0x0d0906,seed:19415,rim:0.16,rimC:0xc9a06a});
  fg.g.position.set(0,1.0,3.6); g.add(fg.g);
  const rock=makeForeground({kind:'岩壁',n:3,r:4.2,w:16,d:7,color:0x0a0704,seed:19417,rim:0.12,rimC:0xc9a06a});
  rock.g.position.set(16,-10,20); g.add(rock.g);
  addLights(g,{c:0xa88658,i:0.34,p:[-50,60,-20]},{c:0x30251a,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sun.update(t,k); wind.update(t); motes.update(t); mist.update(t,k);
    fg.update(t,k); rock.update(t,k); poet.update(t,k);
  }};
}
function bJinge(){ // 二（标志性瞬间）· 金戈铁马 —— 斜阳巷陌之外，铁骑碾尘：气吞万里如虎
  const g=new THREE.Group();
  const ground=makeGround({r:120,c1:0x0d0a06,c2:0x1a1009});
  ground.mesh.position.set(0,-0.2,0); g.add(ground.mesh);
  const water=makeWater({size:460,seg:64,amp:0.45,freq:0.08,speed:0.6,flow:[0,0.7],
    deep:0x100c08,shallow:0x221810,skyc:0x302212,spec:0.26,moonDir:[-0.5,0.16,-0.85],moonColor:0xb08858,y:-2.4});
  water.mesh.position.set(0,-2.4,-186); g.add(water.mesh);
  const ridge=makeRange({r:340,h:18,layers:2,peaks:5,seed:19419,color:0x0a0705,atmo:0x3a2a18,fogK:0.58,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-90); g.add(ridge.g);
  const sun=makeXieyang({r:11,x:-70,y:15,z:-230}); g.add(sun.g);
  /* 斜阳草树·寻常巷陌：草舍两间 + 篱笆 + 草树（寄奴曾住处） */
  const hut1=makeCaoshe({seed:19421,scale:1.15}); hut1.position.set(13,0,-14); hut1.rotation.y=-0.5; g.add(hut1);
  const hut2=makeCaoshe({seed:19423,scale:0.9}); hut2.position.set(19,0,-23); hut2.rotation.y=-0.9; g.add(hut2);
  const zha=makeZhalan({seed:19425,w:10}); zha.position.set(9.5,0,-9); zha.rotation.y=0.9; g.add(zha);
  const treeMid=makeForeground({kind:'树枝',w:12,n:4,d:5,color:0x100b06,seed:19427,sway:0.7,tip:0x2e2412});
  treeMid.g.position.set(7,0,-30); g.add(treeMid.g);
  /* 金戈铁马：阵首前锋 + 铁骑两列（碾尘而过，全页最亮） */
  const lead=makeQiansfeng({scale:1.55}); lead.g.position.set(-28,-0.2,-40); g.add(lead.g);
  const flag=makeZhanqi({h:8.2,ph:0.7,flagC:0x6a1e12}); flag.g.position.set(-30.5,-0.2,-38); g.add(flag.g);
  const cav=makeTieqi({seed:19429,faceLeft:true,sMin:1.45,sMax:1.75,rim:0.30,
    list:[[20,-36],[10,-42],[2,-48],[-6,-54],[-14,-60],[6,-56],[-2,-64],[-12,-68],[-22,-62]]});
  g.add(cav.mesh);
  const dust=makeFlow({n:260,box:[150,10,42],pos:[-5,4.5,-48],color:0x8a6a44,size:21,speed:7,maxA:0.24});
  g.add(dust.points);
  const mist=makeMist({n:5,spread:[240,18,110],pos:[0,6,-80],scale:80,color:0x8a7454,op:0.10});
  g.add(mist.g);
  /* 前景框景 */
  const rock=makeForeground({kind:'坡石',n:2,r:3.0,w:11,d:6,color:0x0b0805,seed:19431,rim:0.12,rimC:0xc9a06a});
  rock.g.position.set(16,-1.6,16); g.add(rock.g);
  const fgTree=makeForeground({kind:'树枝',w:20,n:6,d:5,color:0x0b0805,seed:19433,sway:0.9,tip:0x2e2412});
  fgTree.g.position.set(-17,-1.2,19); g.add(fgTree.g);
  addLights(g,{c:0xd8a060,i:0.55,p:[-70,42,-40]},{c:0x3a2c1c,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ground.update(); water.update(t); ridge.update(t,0); sun.update(t,k);
    lead.update(t); flag.update(t); cav.update(t);
    dust.update(t); mist.update(t,k);
    rock.update(t,k); fgTree.update(t,k); treeMid.update(t,k);
  }};
}
function bFengHuo(){ // 三 · 烽火扬州 —— 北顾：元嘉草草的教训在案，四十三年前扬州路的烽烟犹在望中
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:88,amp:0.5,freq:0.08,speed:0.55,flow:[0,0.7],
    deep:0x0f0c08,shallow:0x201810,skyc:0x2a1d10,spec:0.22,moonDir:[-0.5,0.16,-0.85],moonColor:0xb08858,y:-6.0});
  g.add(water.mesh);
  const ridge=makeRange({r:340,h:20,layers:2,peaks:6,seed:19435,color:0x090705,atmo:0x2c1f10,fogK:0.60,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-46); g.add(ridge.g);
  /* 北固亭头：高台 + 按剑北顾的词人 */
  const tai=new THREE.Mesh(new THREE.BoxGeometry(32,2.8,15),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  tai.position.set(0,-0.3,-5); g.add(tai);
  const top=makeGround({r:13,c1:0x0e0a07,c2:0x16100a});
  top.mesh.position.set(0,1.05,-5); g.add(top.mesh);
  const pilL=makePillar({h:9,top:false,color:0x1c1208}); pilL.g.position.set(-7.5,1.05,-1.8); g.add(pilL.g);
  const pilR=makePillar({h:9,top:false,color:0x1c1208}); pilR.g.position.set(8,1.05,-2.6); g.add(pilR.g);
  const poet=makeFigure({pose:'按剑',robe:0x241c14,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.4,rim:0.60,rimC:0xc9a06a});
  poet.position.set(1.8,1.05,-3.2); poet.rotation.y=Math.PI-0.35; g.add(poet);
  /* 扬州路：北去的官道 + 沿路四座烽燧，火明烟涌（沉痛的记忆） */
  const road=new THREE.Mesh(new THREE.PlaneGeometry(8,170),
    new THREE.MeshPhongMaterial({color:0x1c130c,shininess:2,specular:0x1d160e}));
  road.rotateX(-Math.PI/2); road.rotateZ(0.30); road.position.set(-20,0.06,-92); g.add(road);
  const ft=[[ -11,-48,5.2],[-20,-74,6.2],[-31,-102,7.2],[-44,-134,8.4]];
  g.add(makeFengta({seed:19437,list:ft,rim:0.16}));
  const fires=[];
  for(let i=0;i<ft.length;i++){
    const f=makeFenghuo({h:2.5+ft[i][2]*0.14,w:1.0+ft[i][2]*0.045,
      light:i<2?0.9:0,lightD:34,smokeMax:i<2?0.30:0.22,seed:19439+i});
    f.g.position.set(ft[i][0],ft[i][2]+0.6,ft[i][1]);
    f.setLvl(1); g.add(f.g); fires.push(f);
  }
  const dust=makeFlow({n:170,box:[220,12,90],pos:[-8,7,-64],color:0x6a563c,size:17,speed:4.5,maxA:0.14});
  g.add(dust.points);
  const mist=makeMist({n:6,spread:[260,22,130],pos:[-8,8,-84],scale:84,color:0x6a5a44,op:0.12});
  g.add(mist.g);
  const fg=makeForeground({kind:'栏杆',w:28,h:2.9,color:0x0d0906,seed:19443,rim:0.16,rimC:0xc9a06a});
  fg.g.position.set(0,1.0,3.8); g.add(fg.g);
  const rock=makeForeground({kind:'坡石',n:2,r:3.0,w:11,d:6,color:0x0a0704,seed:19445,rim:0.10,rimC:0xc9a06a});
  rock.g.position.set(-17,-10,18); g.add(rock.g);
  addLights(g,{c:0xa88658,i:0.30,p:[-50,60,-20]},{c:0x2c2216,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0);
    for(let i=0;i<fires.length;i++)fires[i].update(t,k);
    dust.update(t); mist.update(t,k);
    fg.update(t,k); rock.update(t,k); poet.update(t,k);
  }};
}
function bPingWen(){ // 四（末境·可点击）· 凭谁问 —— 佛狸祠下神鸦社鼓；点击烽火扬州路：烽烟起落，「凭谁问」悬空
  const ctl={t:0,clicked:false,clickT:0,lastSong:0};
  const g=new THREE.Group();
  const water=makeWater({size:800,seg:96,amp:0.5,freq:0.08,speed:0.7,flow:[0,0.9],
    deep:0x0f0c08,shallow:0x211810,skyc:0x2c1e10,spec:0.22,moonDir:[-0.55,0.16,-0.83],moonColor:0xb08858,y:-2.0});
  g.add(water.mesh);
  const ridge=makeRange({r:320,h:18,layers:2,peaks:5,seed:19447,color:0x090705,atmo:0x2c1f10,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-66); g.add(ridge.g);
  /* 北岸土冈上的佛狸祠 + 老树栖鸦 + 社鼓 + 赛会人群 + 香火（太平假象） */
  const mound=new THREE.Mesh(rockGeo(12,1,seedRnd(19449)),
    rimHook(new THREE.MeshPhongMaterial({color:0x1a120a,shininess:4,specular:0x1d160e,emissive:0x040302}),
      {c:0xc9a06a,i:0.08,p:2.8}));
  mound.scale.set(2.2,0.34,1.5); mound.position.set(0,-3.0,-74); g.add(mound);
  const foli=makeFoli({scale:1.3}); foli.position.set(0,0.9,-72); g.add(foli);
  const tree=makeLaoshu({seed:19451,h:9,scale:1.15}); tree.position.set(10,0.2,-67); g.add(tree);
  const wuya=makeWuya({n:7,seed:19453,rim:0.26}); wuya.mesh.position.set(2,3.5,-67); g.add(wuya.mesh);
  const gu=makeShegu({scale:1.1}); gu.position.set(-5,0.5,-63.5); gu.rotation.y=0.5; g.add(gu);
  const ren=makeCrowd({n:12,rect:[-7,-3,14,7],color:0x14100a,rimC:0xc9a06a,rim:0.18,sMin:0.62,sMax:0.82,y:1.0,seed:19455});
  ren.mesh.position.set(0,-0.1,-62.5); g.add(ren.mesh);
  const incense=makeGlow({n:30,box:[12,8,6],pos:[0,3.6,-67],color:0xd8a060,size:7,speed:0.22,rise:1,add:true,maxA:0.32});
  g.add(incense.points);
  const motes=makeGlow({n:30,box:[170,22,90],pos:[0,9,-46],color:0xc09a68,size:6,speed:0.05,rise:0,maxA:0.14});
  g.add(motes.points);
  /* 远处烽燧剪影（未燃）——点击后烽烟起落：四十三年前的烽火扬州路 */
  const ft=[[-34,-104,7],[6,-120,8],[38,-96,6.5]];
  g.add(makeFengta({seed:19457,list:ft,rim:0.10}));
  const fires=[];
  for(let i=0;i<ft.length;i++){
    const f=makeFenghuo({h:3.0+ft[i][2]*0.14,w:1.15,light:0,smokeMax:0.30,seed:19459+i});
    f.g.position.set(ft[i][0],ft[i][2]+0.7,ft[i][1]);
    f.setLvl(0.0001); g.add(f.g); fires.push(f);
  }
  /* 「凭谁问」问句悬空 */
  const wenju=makeWenju({y:26,z:-84}); g.add(wenju.g);
  /* 南岸江岸高台：老臣凭江北望（前景右侧） */
  const bank=new THREE.Mesh(new THREE.BoxGeometry(38,2.4,14),
    new THREE.MeshPhongMaterial({color:0x120d08,shininess:4,specular:0x1d160e}));
  bank.position.set(0,-0.35,17); g.add(bank);
  const bankTop=makeGround({r:14,c1:0x0e0a07,c2:0x16100a});
  bankTop.mesh.position.set(0,0.85,17); g.add(bankTop.mesh);
  const poet=makeFigure({pose:'按剑',robe:0x262018,belt:0x6a4e2e,hat:'幞头',beard:true,scale:1.12,rim:0.55,rimC:0xc9a06a});
  poet.position.set(8,0.85,11); poet.rotation.y=Math.PI+0.35; g.add(poet);
  const mist=makeMist({n:6,spread:[240,20,110],pos:[0,7,-48],scale:78,color:0x7a674c,op:0.11});
  g.add(mist.g);
  const fgL=makeForeground({kind:'芦苇',w:30,n:10,d:6,color:0x120c05,seed:19461,sway:1.1,tip:0x3a2e18});
  fgL.g.position.set(-21,-1.4,13); g.add(fgL.g);
  const rock=makeForeground({kind:'坡石',n:2,r:3.0,w:11,d:6,color:0x0b0805,seed:19463,rim:0.10,rimC:0xc9a06a});
  rock.g.position.set(21,-2.0,9); g.add(rock.g);
  addLights(g,{c:0xb08858,i:0.32,p:[-40,55,-15]},{c:0x32271a,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt||0;
      /* 点击后：烽烟起落（三座烽燧错次点燃→回落为余烬）+ 问句悬空渐显 */
      const since=ctl.clicked?ctl.t-ctl.clickT:-1;
      for(let i=0;i<fires.length;i++){
        let lvl=0.0001;
        if(since>=0){
          const tt=since-i*0.45;
          if(tt>0){
            const rise=Math.min(1,tt/1.1);
            const fall=1-0.85*Math.min(1,Math.max(0,(tt-3.4)/4.0));
            lvl=Math.max(0.0001,rise*fall);
          }
        }
        const f=fires[i];
        f.setLvl(lvl);
        f.update(t,k);
      }
      wenju.update(t,k,ctl.clicked?Math.min(1,Math.max(0,(since-0.6)/2.4)):0);
      if(ctl.clicked&&t-ctl.lastSong>7.0){ ctl.lastSong=t; pluck(0,0,0.05); pluck(2,0.5,0.04); } // 烽烟余韵
      water.update(t); ridge.update(t,0); wuya.update(t); ren.update(t);
      incense.update(t); motes.update(t); mist.update(t,k);
      fgL.update(t,k); rock.update(t,k); poet.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t; ctl.lastSong=-99;
        bell(); pluck(0,0.2,0.09); pluck(0,0.6,0.07); pluck(1,1.1,0.06); // 社鼓一记，余音沉沉
        const fl=$('#flash'); fl.textContent=YYK_QUESTION; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
