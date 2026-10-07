/* ================= 菩萨蛮·小山重叠金明灭 · 三境场景（夜宴金彩·闺阁晨妆变体：金屏晓妆、花面交映） =================
   美术口径：暖烛金彩闺阁——铜镜、金箔屏山、烛焰、香篆、金线绣鹧鸪；与宴饮金拉开距离。 */

/* 烛台：烛身 + 焰（焰体自带闪烁点光可选） */
function makeCandle(o){
  o=o||{};
  const stem=o.stem===undefined?0.8:o.stem, wax=o.wax===undefined?0.9:o.wax;
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(0.30,0.38,0.10,12); base.translate(0,0.05,0); B.put(base,0x7a5c30);
  const st=new THREE.CylinderGeometry(0.06,0.10,stem,8); st.translate(0,0.10+stem/2,0); B.put(st,0x6a4c26);
  const cup=new THREE.CylinderGeometry(0.16,0.10,0.08,10); cup.translate(0,0.10+stem+0.04,0); B.put(cup,0x8a6a38);
  const wd=new THREE.CylinderGeometry(0.11,0.13,wax,10); wd.translate(0,0.10+stem+0.08+wax/2,0); B.put(wd,0xe6d8bc);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xffd890,i:0.34,p:2.6}));
  const g=new THREE.Group(); g.add(mesh);
  const fl=makeFlame({h:o.fh===undefined?0.50:o.fh,w:o.fw===undefined?0.20:o.fw,planes:2,
    embers:o.embers===undefined?8:o.embers,esize:3.5,spark:false,light:o.light||0,lightD:o.lightD||30,
    core:0xffdca0,outer:0xff7a22,wide:0.30,seed:Math.random()*8});
  fl.g.position.y=0.10+stem+0.08+wax; g.add(fl.g);
  return {g,update(t,k){ fl.update(t,k); }};
}

/* 小山屏风：三扇曲屏，扇面三层重叠小山（金箔面），烛光摇曳下金明灭 */
function makePingShan(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?157:o.seed);
  const dark=new GeoBag(), gold=new GeoBag();
  const PW=4.3, PH=6.3;
  const panels=[[-4.6,0.5,-0.9],[0,0,0],[4.6,-0.5,-0.9]];
  panels.forEach(function(pn){
    const px=pn[0], ry=pn[1], pz=pn[2];
    const put=function(geo,col,isGold){
      geo.rotateY(ry); geo.translate(px,0,pz);
      (isGold?gold:dark).put(geo,col);
    };
    const bb=new THREE.BoxGeometry(PW,PH,0.14); bb.translate(0,PH/2+0.25,0); put(bb,0x201610);
    const top=new THREE.BoxGeometry(PW+0.24,0.22,0.30); top.translate(0,PH+0.34,0); put(top,0x2e2114);
    [-1,1].forEach(function(s){
      const post=new THREE.BoxGeometry(0.20,PH+0.5,0.28); post.translate(s*PW/2,(PH+0.5)/2,0); put(post,0x2a1d10);
    });
    const feet=new THREE.BoxGeometry(PW*0.9,0.30,0.9); feet.translate(0,0.15,0.12); put(feet,0x241810);
    const hillC=[0x7a5e22,0xa8843a,0xc9a24a];
    const X0=-PW/2+0.55, XW=PW-1.1;               // 山体收进扇面内，不出框
    [[0,6,1.5,3.0,0.85,1.25],[1,5,1.1,2.2,0.70,1.05],[2,5,0.8,1.6,0.55,0.85]].forEach(function(cfg){
      const L=cfg[0], n=cfg[1], hMin=cfg[2], hMax=cfg[3], rMin=cfg[4], rMax=cfg[5];
      for(let i=0;i<n;i++){
        const hh=hMin+R()*(hMax-hMin), rr=rMin+R()*(rMax-rMin);
        const cone=new THREE.ConeGeometry(rr,hh,7,1);
        cone.scale(1,1,0.26);
        cone.rotateY(R()*0.6);
        cone.translate(X0+(i+0.5)*XW/n+(R()-0.5)*0.35, 0.32+hh/2, 0.30-L*0.09);
        put(cone,hillC[L],true);
      }
    });
  });
  const g=new THREE.Group();
  g.add(dark.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x5a4426,emissive:0x0a0703}),{c:0xd8b060,i:0.30,p:2.5})));
  const goldMat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:48,
    specular:0xd8b878,emissive:0x4a340c,emissiveIntensity:0.75}),{c:0xffe0a0,i:0.42,p:2.8});
  g.add(gold.mesh(goldMat));
  return {g,goldMat,update(t,k){   // 金明灭：金箔随烛焰忽明忽暗
    goldMat.emissiveIntensity=k*(0.32+0.28*(0.5+0.5*Math.sin(t*1.7))+0.15*(0.5+0.5*Math.sin(t*5.3+1.7)));
  }};
}

/* 铜镜：镜架 + 铜色镜面（高反光）+ 镜中「花面」双层辉光（初值=包络最大值） */
function makeMirror(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const R=o.r===undefined?0.62:o.r;
  const faceMax=o.faceMax===undefined?0.30:o.faceMax;
  const flowerMax=o.flowerMax===undefined?0.16:o.flowerMax;
  const B=new GeoBag();
  const disc=new THREE.CylinderGeometry(R,R,0.05,26); disc.rotateX(Math.PI/2); disc.translate(0,R+0.25,0.10); B.put(disc,0x6a5432);
  const ring=new THREE.TorusGeometry(R+0.02,0.045,8,26); ring.translate(0,R+0.25,0.10); B.put(ring,0xc9a24a);
  const back=new THREE.CylinderGeometry(0.05,0.05,1.15,8); back.rotateX(0.5); back.translate(0,0.62,-0.18); B.put(back,0x5a4426);
  const foot=new THREE.BoxGeometry(0.9,0.12,0.55); foot.translate(0,0.06,-0.05); B.put(foot,0x5a4426);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:96,
    specular:0xffe8c0,emissive:0x14100a}),{c:0xffe2a0,i:0.40,p:3.0}));
  const g=new THREE.Group(); g.add(mesh);
  const face=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf2c8a0,
    transparent:true,opacity:faceMax,depthWrite:false,blending:THREE.AdditiveBlending}));
  face.scale.set(R*1.55,R*1.55,1); face.position.set(0,R+0.25,0.17); face.renderOrder=2; g.add(face);
  const flower=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe89aa0,
    transparent:true,opacity:flowerMax,depthWrite:false,blending:THREE.AdditiveBlending}));
  flower.scale.set(R*1.05,R*1.05,1); flower.position.set(0,R+0.36,0.20); flower.renderOrder=2; g.add(flower);
  g.scale.setScalar(sc);
  return {g,face,flower,faceMax,flowerMax};
}

/* 妆台杂件：妆奁、粉盒、胭脂盏、玉簪、香炉（合批 1 mesh） */
function makeVanityBag(){
  const B=new GeoBag();
  const box=new THREE.BoxGeometry(0.72,0.32,0.5); box.translate(-1.35,0.16,0.25); B.put(box,0x4a2c14);
  const lid=new THREE.BoxGeometry(0.74,0.10,0.52); lid.translate(-1.35,0.37,0.25); B.put(lid,0x5c3a1a);
  const clasp=new THREE.BoxGeometry(0.07,0.09,0.05); clasp.translate(-1.35,0.33,-0.02); B.put(clasp,0xc9a24a);
  const fbox=new THREE.CylinderGeometry(0.14,0.14,0.10,12); fbox.translate(-0.62,0.05,0.38); B.put(fbox,0xd8d0c0);
  const flid=new THREE.CylinderGeometry(0.145,0.145,0.03,12); flid.translate(-0.62,0.115,0.38); B.put(flid,0xc8c0b0);
  const zhi=new THREE.CylinderGeometry(0.09,0.09,0.06,10); zhi.translate(-0.34,0.03,0.45); B.put(zhi,0x8a3030);
  const hairpin=new THREE.CylinderGeometry(0.014,0.014,0.52,6); hairpin.rotateZ(1.45); hairpin.translate(0.2,0.03,0.2); B.put(hairpin,0xcfe0d8);
  const censer=new THREE.CylinderGeometry(0.16,0.13,0.20,12); censer.translate(0.62,0.10,0.10); B.put(censer,0x6a5030);
  const cslid=new THREE.TorusGeometry(0.10,0.03,6,14); cslid.rotateX(Math.PI/2); cslid.translate(0.62,0.22,0.10); B.put(cslid,0x7a6038);
  for(let i=0;i<3;i++){
    const a=i/3*6.283+0.5;
    const lg=new THREE.CylinderGeometry(0.02,0.03,0.07,5);
    lg.translate(0.62+Math.sin(a)*0.11,0.035,0.10+Math.cos(a)*0.11); B.put(lg,0x54402a);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:34,
    specular:0x8a7048,emissive:0x0a0705}),{c:0xffdca0,i:0.32,p:2.8})));
  return g;
}

/* 鬓边簪花：金芯粉瓣一小朵（合批 1 mesh） */
function makeHairFlower(){
  const B=new GeoBag();
  const c=new THREE.SphereGeometry(0.07,8,6); B.put(c,0xc09a3a);
  for(let i=0;i<5;i++){
    const a=i/5*6.283;
    const p=new THREE.SphereGeometry(0.075,7,5); p.scale(1,0.55,1);
    p.translate(Math.cos(a)*0.115,0.01,Math.sin(a)*0.115); B.put(p,0xc86878);
  }
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:40,
    specular:0xffd0d0,emissive:0x180a0c})));
  return g;
}

/* 衣架 + 绣罗襦 + 双双金鹧鸪（架 1 + 襦 1 + 鸪 1 共 3 mesh；鸪金线可点暗生辉） */
function makeLuoru(o){
  o=o||{};
  const stand=new GeoBag();
  [-0.85,0.85].forEach(function(x){
    const pole=new THREE.CylinderGeometry(0.05,0.07,2.6,8); pole.translate(x,1.3,0); stand.put(pole,0x3a2414);
    const bs=new THREE.BoxGeometry(0.5,0.10,0.5); bs.translate(x,0.05,0); stand.put(bs,0x2c1c10);
  });
  const bar=new THREE.CylinderGeometry(0.045,0.045,1.9,8); bar.rotateZ(Math.PI/2); bar.translate(0,2.56,0); stand.put(bar,0x4a3018);
  const g=new THREE.Group();
  g.add(stand.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4426,emissive:0x0a0704}),{c:0xd8b060,i:0.26,p:2.5})));
  const pts=[[0.72,0.62],[0.74,1.0],[0.68,1.45],[0.58,1.9],[0.46,2.2],[0.34,2.38],[0.10,2.46]];
  const robe=new THREE.LatheGeometry(pts.map(p=>new THREE.Vector2(p[0],p[1])),18);
  robe.scale(1,1,0.38);
  const robeMesh=new THREE.Mesh(robe,rimHook(new THREE.MeshPhongMaterial({color:0x7a2840,shininess:26,
    specular:0xc89070,emissive:0x120508,side:THREE.DoubleSide}),{c:0xffb890,i:0.40,p:2.6}));
  robeMesh.position.y=0.02; g.add(robeMesh);
  const birds=new GeoBag();
  [-0.42,0.42].forEach(function(x){
    const body=new THREE.SphereGeometry(0.13,8,6); body.scale(1.3,0.95,0.85); body.translate(x,1.66,0.38); birds.put(body,0xc9a24a);
    const head=new THREE.SphereGeometry(0.075,8,6); head.translate(x+0.11,1.77,0.45); birds.put(head,0xc9a24a);
    const beak=new THREE.ConeGeometry(0.028,0.09,5); beak.rotateX(Math.PI/2); beak.translate(x+0.21,1.76,0.49); birds.put(beak,0xb8862a);
    const tail=new THREE.ConeGeometry(0.06,0.26,5); tail.rotateX(-Math.PI/2.6); tail.translate(x-0.19,1.64,0.28); birds.put(tail,0xa8843a);
  });
  const birdMat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:80,
    specular:0xffe8b8,emissive:0x6a4a10,emissiveIntensity:1.85}),{c:0xffe0a0,i:0.55,p:3.0});
  g.add(birds.mesh(birdMat));
  return {g,birdMat};
}

/* 窗棂：格窗剪影（合批 1 mesh），窗外晓色由光 Sprite 另置 */
function makeWindow(o){
  o=o||{};
  const w=o.w===undefined?4.6:o.w, h=o.h===undefined?4.8:o.h;
  const B=new GeoBag(), c=0x140d08;
  [[-w/2,h/2],[w/2,h/2]].forEach(function(p){
    const s=new THREE.BoxGeometry(0.16,h+0.2,0.14); s.translate(p[0],p[1],0); B.put(s,c);
  });
  [[0,h],[0,0.1]].forEach(function(p){
    const s=new THREE.BoxGeometry(w+0.3,0.16,0.14); s.translate(p[0],p[1],0); B.put(s,c);
  });
  [-w/6,w/6].forEach(function(x){
    const s=new THREE.BoxGeometry(0.09,h,0.10); s.translate(x,h/2,0); B.put(s,c);
  });
  [h*0.33,h*0.66].forEach(function(y){
    const s=new THREE.BoxGeometry(w,0.09,0.10); s.translate(0,y,0); B.put(s,c);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2c1c,emissive:0x060403}),{c:0xd8b060,i:0.22,p:2.5})));
  return g;
}

/* 晓色光团（窗外/檐下的暖光 Sprite，初值=包络最大值） */
function dawnGlow(o){
  o=o||{};
  const op=o.op===undefined?0.5:o.op;
  const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),
    color:o.color===undefined?0xd89a58:o.color,
    transparent:true,opacity:op,depthWrite:false,blending:THREE.AdditiveBlending}));
  const sc=o.scale===undefined?7:o.scale;
  s.scale.set(sc,sc,1); s.renderOrder=2;
  return {s:s,op:op};
}

/* 远处闺楼剪影（两层 + 攒尖顶 + 一格金窗，合批 1 mesh） */
function makeLouGe(){
  const B=new GeoBag(), c1=0x120d0a, c2=0x1a120c, c3=0x241810;
  const base=new THREE.BoxGeometry(8,0.8,6); base.translate(0,0.4,0); B.put(base,c1);
  const s1=new THREE.BoxGeometry(5.4,3.4,4.4); s1.translate(0,2.5,0); B.put(s1,c2);
  const e1=new THREE.BoxGeometry(6.8,0.4,5.4); e1.translate(0,4.4,0); B.put(e1,c3);
  const s2=new THREE.BoxGeometry(4.2,2.8,3.6); s2.translate(0,6.0,0); B.put(s2,c2);
  const e2=new THREE.BoxGeometry(5.4,0.36,4.4); e2.translate(0,7.6,0); B.put(e2,c3);
  const roof=new THREE.ConeGeometry(3.6,1.8,4); roof.rotateY(Math.PI/4); roof.translate(0,8.5,0); B.put(roof,c3);
  const win=new THREE.BoxGeometry(0.9,1.1,0.1); win.translate(0,6.2,1.85); B.put(win,0xb8923a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x0a0603}),{c:0xd8b060,i:0.26,p:2.6})));
  return g;
}

/* 回廊一列（柱 + 枋 + 栏，合批 1 mesh） */
function makeCorridor(){
  const B=new GeoBag(), c=0x161009, c2=0x1e140a;
  for(let i=0;i<5;i++){
    const x=i*2.8-5.6;
    const p=new THREE.CylinderGeometry(0.16,0.2,3.6,7); p.translate(x,1.8,0); B.put(p,c);
  }
  const beam=new THREE.BoxGeometry(11.6,0.28,0.5); beam.translate(0,3.75,0); B.put(beam,c2);
  const rail=new THREE.BoxGeometry(11.6,0.14,0.14); rail.translate(0,1.35,0.22); B.put(rail,c2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x0a0603}),{c:0xd8b060,i:0.22,p:2.6})));
  return g;
}

function bCover(){ // 卷首 · 晓色闺楼 —— 天将明，闺楼一点金窗烛光未熄
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0a0709,c2:0x191210});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0b0809,atmo:0x3a2c20,fogK:0.74,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const tower=makeLouGe(); tower.position.set(-26,0,-70); tower.scale.setScalar(1.15); g.add(tower);
  const corridor=makeCorridor(); corridor.position.set(14,0,-30); g.add(corridor);
  const lantern=makeLantern(0.5,{flick:0.9}); lantern.position.set(11.2,3.5,-29); g.add(lantern);
  /* makeLantern 内辉包络最高 1.08×base（双频闪烁同相）——初值提到包络最大值，fadeK 合规 */
  lantern.traverse(function(o){ if(o.isSprite)o.material.opacity=0.78; });
  /* 庭院侍女（远景人影）+ 廊下小鬟 */
  const maids=makeCrowd({n:3,rect:[8,-40,26,10],seed:161,color:0x14100c,rimC:0xd4b050,rim:0.22,sMin:0.8,sMax:1.0});
  g.add(maids.mesh);
  const maid=makeFigure({pose:'独立',robe:0x2c1c1c,belt:0x6a5030,skin:0xd9b189,hat:'发髻',
    face:0.4,scale:0.85,rim:0.4,rimC:0xffd890,noProp:true});
  maid.position.set(10,0,-27.5); g.add(maid);
  const winGlow=dawnGlow({color:0xd89a58,op:0.36,scale:5});
  winGlow.s.position.set(-26,7.4,-67.5); g.add(winGlow.s);
  const mist=makeMist({n:9,spread:[240,30,140],pos:[0,8,-50],scale:78,color:0x8a6a50,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:56,box:[180,30,100],pos:[0,8,-30],color:0xd4b050,size:6,speed:0.05,rise:0,maxA:0.30});
  g.add(motes.points);
  const fg=makeForeground({kind:'树枝',n:2,w:16,d:6,color:0x060404,seed:9,sway:0.9,rim:0.14});
  fg.g.position.set(-18,-1,18); g.add(fg.g);
  const rail=makeForeground({kind:'栏杆',w:26,h:3.0,color:0x080505,seed:11,rim:0.12});
  rail.g.position.set(0,-2,20); g.add(rail.g);
  addLights(g,{c:0xd8a860,i:0.34,p:[-40,60,30]},{c:0x2c2018,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); maids.update(t); maid.update(t,k);
    fg.update(t,k); rail.update(t,k); lantern.userData.update(t,k);
    winGlow.s.material.opacity=k*(0.30+0.06*Math.sin(t*0.8));
  }};
}

function bJinPing(){ // 壹 · 金屏晓妆 —— 小山重叠金明灭，鬓云欲度香腮雪；懒起画蛾眉，弄妆梳洗迟
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0b0808,c2:0x1c1410});
  g.add(grd.mesh);
  const ridge=makeRange({r:210,h:24,layers:2,peaks:4,seed:1571,color:0x0c0808,atmo:0x38281c,fogK:0.62,glowK:0.05});
  g.add(ridge.g);
  /* 窗棂 + 窗外晓色 */
  const win=makeWindow({w:4.6,h:4.8}); win.position.set(-9.5,0,-13); g.add(win);
  const dawn=dawnGlow({color:0xd89a58,op:0.52,scale:7});
  dawn.s.position.set(-9.5,3.4,-14.6); g.add(dawn.s);
  /* 小山屏风（金明灭主体） */
  const shan=makePingShan({seed:157}); shan.g.position.set(1.2,0,-8.6); shan.g.rotation.y=0.06; g.add(shan.g);
  /* 闺中人（懒起） */
  const lady=makeFigure({pose:'独立',robe:0x7a3040,belt:0xc9a24a,skin:0xe0c0a8,hair:0x1a1210,collar:0xe8d0b0,
    hat:'发髻',face:-0.4,scale:1.04,rim:0.55,rimC:0xffd890,noProp:true});
  lady.position.set(3.1,0,-5.6); lady.rotation.y=0.9; g.add(lady);
  /* 妆台 + 杂件 + 案上铜镜 + 双烛 */
  const tb=makeTable({w:4.8,d:1.9,h:1.52,wood:0x33200f}); tb.g.position.set(-2.2,0,-5.2); g.add(tb.g);
  const vanity=makeVanityBag(); vanity.position.set(-2.2,1.52,-5.2); g.add(vanity);
  const mir=makeMirror({scale:0.8,faceMax:0.30,flowerMax:0.16});
  mir.g.position.set(-3.4,1.52,-5.6); mir.g.rotation.y=0.7; g.add(mir.g);
  const cd1=makeCandle({light:1.1,lightD:26}); cd1.g.position.set(-0.6,1.52,-5.0); g.add(cd1.g);
  const cd2=makeCandle({stem:1.2,wax:1.0}); cd2.g.position.set(-9.2,0,-5.5); g.add(cd2.g);
  /* 香篆一缕（妆奁香炉起烟）+ 金尘 */
  const smoke=makeGlow({n:36,box:[0.7,6.5,0.7],pos:[-1.58,2.2,-5.1],color:0xc0a890,size:3.6,speed:0.16,rise:1,maxA:0.18});
  g.add(smoke.points);
  const motes=makeGlow({n:60,box:[34,12,26],pos:[-1,4.5,-5],color:0xd4b050,size:4.6,speed:0.05,rise:0.25,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[120,16,70],pos:[0,4,-24],scale:58,color:0x8a6a50,op:0.07});
  g.add(mist.g);
  const rail=makeForeground({kind:'栏杆',w:24,h:2.8,color:0x080505,seed:13,rim:0.12});
  rail.g.position.set(2,-1.4,8.6); g.add(rail.g);
  addLights(g,{c:0xffc890,i:0.30,p:[-20,50,26]},{c:0x322618,i:0.72});
  const pl=new THREE.PointLight(0xffb060,1.76,30); pl.position.set(-2.2,3.4,-4.6); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); shan.update(t,k); lady.update(t,k); mist.update(t,k); motes.update(t);
    smoke.update(t); cd1.update(t,k); cd2.update(t,k); rail.update(t,k);
    mir.face.material.opacity=k*mir.faceMax*(0.85+0.15*Math.sin(t*2.0));
    mir.flower.material.opacity=k*mir.flowerMax*(0.80+0.20*Math.sin(t*1.6+0.5));
    dawn.s.material.opacity=k*(0.42+0.10*(0.5+0.5*Math.sin(t*0.5)));
    pl.intensity=k*1.76*(0.72+0.18*Math.sin(t*9.1)+0.10*Math.sin(t*17.3));
  }};
}

function bJiaoYing(){ // 贰（末境·可点击）· 花面交映 —— 前后镜相照，花面交相映；罗襦双鸪（点击：镜中花面重影交映）
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,glow:0};
  const grd=makeGround({r:110,c1:0x0b0808,c2:0x1c1410});
  g.add(grd.mesh);
  const ridge=makeRange({r:220,h:26,layers:2,peaks:5,seed:1581,color:0x0c0808,atmo:0x3e2c1c,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 前镜（妆台案上）与后镜（镜架）前后相照，屏山退居其后 */
  const tb=makeTable({w:4.8,d:1.9,h:1.52,wood:0x33200f}); tb.g.position.set(-1.4,0,-4.6); g.add(tb.g);
  const shan=makePingShan({seed:157}); shan.g.position.set(0.4,0,-11.6); shan.g.scale.setScalar(0.92); g.add(shan.g);
  const mirF=makeMirror({scale:1.0,r:0.64,faceMax:0.92,flowerMax:0.74});
  mirF.g.position.set(-1.4,1.52,-4.2); mirF.g.rotation.y=2.5; g.add(mirF.g);
  const mirB=makeMirror({scale:1.25,r:0.62,faceMax:0.92,flowerMax:0.74});
  mirB.g.position.set(2.6,0,-9.8); mirB.g.rotation.y=-0.62; g.add(mirB.g);
  /* 闺中人（簪花）立于两镜之间 */
  const lady=makeFigure({pose:'独立',robe:0x7a3040,belt:0xc9a24a,skin:0xe0c0a8,hair:0x1a1210,collar:0xe8d0b0,
    hat:'发髻',face:-0.66,scale:1.06,rim:0.60,rimC:0xffd890,noProp:true});
  lady.position.set(0.6,0,-6.8); lady.rotation.y=-0.66; g.add(lady);
  const flower=makeHairFlower(); flower.position.set(0.75,4.06,-6.72); flower.rotation.y=-0.4; g.add(flower);
  /* 绣罗襦 + 双双金鹧鸪 */
  const luo=makeLuoru(); luo.g.position.set(6.4,0,-6.2); luo.g.rotation.y=-0.35; g.add(luo.g);
  /* 交映光桥（两镜之间一道柔光）+ 交互光 + 金屑迸光 */
  const bridge=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd8a8,
    transparent:true,opacity:0.42,depthWrite:false,blending:THREE.AdditiveBlending}));
  bridge.scale.set(7.6,2.1,1); bridge.position.set(0.6,2.35,-7.0); bridge.renderOrder=3; g.add(bridge);
  const burst=makeBurst({n:80,color:0xffd890,pos:[0.6,3.8,-6.6]}); g.add(burst.points);
  /* 窗棂晓色 + 双烛 + 香篆 + 金尘 + 雾 + 前景画栏 */
  const win=makeWindow({w:4.2,h:4.4}); win.position.set(12.8,0,-14.5); g.add(win);
  const dawn=dawnGlow({color:0xd89a58,op:0.46,scale:6.4});
  dawn.s.position.set(12.8,3.2,-16.1); g.add(dawn.s);
  const cd1=makeCandle({light:1.0,lightD:24}); cd1.g.position.set(-2.9,1.52,-4.2); g.add(cd1.g);
  const smoke=makeGlow({n:30,box:[0.7,6.0,0.7],pos:[2.6,2.4,-4.0],color:0xc0a890,size:3.4,speed:0.16,rise:1,maxA:0.16});
  g.add(smoke.points);
  const motes=makeGlow({n:56,box:[36,12,26],pos:[0,4.5,-6],color:0xd4b050,size:4.6,speed:0.05,rise:0.25,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[120,16,70],pos:[0,4,-24],scale:58,color:0x8a6a50,op:0.07});
  g.add(mist.g);
  const rail=makeForeground({kind:'栏杆',w:24,h:2.8,color:0x080505,seed:15,rim:0.12});
  rail.g.position.set(-3,-1.4,8.2); g.add(rail.g);
  addLights(g,{c:0xffd8a0,i:0.32,p:[-20,50,26]},{c:0x362a1e,i:0.74});
  const pl=new THREE.PointLight(0xffd0a0,1.9,34); pl.position.set(0.6,3.6,-6.2); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.glow=Math.min(1,ctl.glow+dt/1.8);
      const gl=ctl.glow;
      ridge.update(t,0); shan.update(t,k); lady.update(t,k); mist.update(t,k); motes.update(t);
      smoke.update(t); burst.update(t); rail.update(t,k); cd1.update(t,k);
      mirF.face.material.opacity=k*(mirF.faceMax*(0.30+0.62*gl))*(0.86+0.14*Math.sin(t*2.2));
      mirB.face.material.opacity=k*(mirB.faceMax*(0.30+0.60*gl))*(0.86+0.14*Math.sin(t*2.2+0.9));
      mirF.flower.material.opacity=k*(mirF.flowerMax*(0.22+0.68*gl))*(0.80+0.20*Math.sin(t*1.7+0.4));
      mirB.flower.material.opacity=k*(mirB.flowerMax*(0.22+0.66*gl))*(0.80+0.20*Math.sin(t*1.7+1.1));
      bridge.material.opacity=k*0.42*gl*(0.80+0.20*Math.sin(t*1.3));
      pl.intensity=k*1.9*(0.55+0.45*gl*(0.85+0.15*Math.sin(t*2.6)));
      luo.birdMat.emissiveIntensity=k*(0.35+1.5*gl*(0.70+0.30*Math.sin(t*3.1)));
      dawn.s.material.opacity=k*(0.38+0.08*(0.5+0.5*Math.sin(t*0.5)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire();
        pluck(0,0.05,0.14); pluck(2,0.35,0.13); pluck(4,0.7,0.12); pluck(5,1.05,0.10); bell();
        const fl=$('#flash'); fl.textContent='花面交相映'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
