/* ================= 鹧鸪天·彩袖殷勤捧玉钟 · 两境场景（夜宴金彩·小山词冠篇：舞低楼月、银釭疑梦） =================
   美术口径：夜宴金彩——bg #05070d 硬底，金 #e0c060 只长在「歌筵灯烛、彩袖金缕、银釭灯焰」上。
   境①高楼歌筵（当年盛欢）：楼心矮栏围出回廊口，暖白月轮随彻夜歌舞徐徐西沉——「舞低杨柳楼心月」在画面里真实发生；
   境②梦境重逢（今宵疑梦）：低饱和暖光 + 重雾化做「疑在梦中」质感，点击挑亮银釭、灯下相认、恍然如梦。 */

/* 烛台：座 + 烛签 + 蜡柱 + 焰（境①案上，合批 1 mesh + 焰体） */
function makeZhuTai(o){
  o=o||{};
  const stem=o.stem===undefined?0.5:o.stem, wax=o.wax===undefined?0.85:o.wax;
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(0.26,0.34,0.09,12); base.translate(0,0.045,0); B.put(base,0x6a4c26);
  const disk=new THREE.CylinderGeometry(0.20,0.13,0.07,10); disk.translate(0,0.125,0); B.put(disk,0x7a5c30);
  const pin=new THREE.CylinderGeometry(0.030,0.045,stem,7); pin.translate(0,0.16+stem/2,0); B.put(pin,0x8a6a38);
  const wd=new THREE.CylinderGeometry(0.105,0.13,wax,10); wd.translate(0,0.16+stem+wax/2,0); B.put(wd,0xe8dcc2);
  const ring=new THREE.TorusGeometry(0.115,0.022,6,14); ring.rotateX(Math.PI/2);
  ring.translate(0,0.16+stem+wax,0); B.put(ring,0xc9a24a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xffd890,i:0.34,p:2.6}));
  const g=new THREE.Group(); g.add(mesh);
  const fl=makeFlame({h:o.fh===undefined?0.46:o.fh,w:o.fw===undefined?0.18:o.fw,planes:2,
    embers:o.embers===undefined?8:o.embers,esize:3.2,spark:false,light:o.light||0,lightC:0xffb060,lightD:o.lightD||18,
    core:0xffe2a8,outer:0xff7a26,wide:0.30,seed:Math.random()*8});
  fl.g.position.y=0.16+stem+wax; g.add(fl.g);
  return {g,update(t,k){ fl.update(t,k); }};
}

/* 立灯檠：覆盆足 + 擎柱 + 承盘 + 金环口 + 焰（境①楼角成列，合批 1 mesh + 焰体） */
function makeDengQing(o){
  o=o||{};
  const h=o.h===undefined?2.9:o.h;
  const B=new GeoBag();
  const ft=new THREE.CylinderGeometry(0.30,0.40,0.13,12); ft.translate(0,0.065,0); B.put(ft,0x2c2014);
  const pole=new THREE.CylinderGeometry(0.05,0.085,h,8); pole.translate(0,0.13+h/2,0); B.put(pole,0x3c2c18);
  const dish=new THREE.CylinderGeometry(0.30,0.15,0.11,12); dish.translate(0,0.13+h+0.055,0); B.put(dish,0x8a6a38);
  const bowl=new THREE.SphereGeometry(0.17,10,7,0,Math.PI*2,0,1.25); bowl.scale(1.15,0.62,1.15);
  bowl.translate(0,0.13+h+0.10,0); B.put(bowl,0xa87c40);
  const ring=new THREE.TorusGeometry(0.245,0.026,6,18); ring.rotateX(Math.PI/2);
  ring.translate(0,0.13+h+0.14,0); B.put(ring,0xc9a24a);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:34,
    specular:0x9a7a48,emissive:0x0a0704}),{c:0xffd890,i:0.36,p:2.7}));
  const g=new THREE.Group(); g.add(mesh);
  const fl=makeFlame({h:o.fh===undefined?0.60:o.fh,w:o.fw===undefined?0.23:o.fw,planes:2,
    embers:o.embers===undefined?10:o.embers,esize:3.5,spark:false,light:o.light||0,lightC:0xffa858,lightD:o.lightD||26,
    core:0xffe2a8,outer:0xff7a26,wide:0.30,seed:Math.random()*8});
  fl.g.position.y=0.13+h+0.16; g.add(fl.g);
  return {g,update(t,k){ fl.update(t,k); }};
}

/* 夜楼剪影：台基 + 两层楼身 + 腰檐 + 攒尖顶 + 三扇窗烛光（卷首远景，合批 1 mesh + 窗光 2 mesh + 顶辉 1 sprite） */
function makeLouGe(o){
  o=o||{};
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(7.6,1.1,6.0); base.translate(0,0.55,0); B.put(base,0x100c0a);
  const f1=new THREE.BoxGeometry(5.8,3.6,4.4); f1.translate(0,2.9,0); B.put(f1,0x18110b);
  const eave1=new THREE.ConeGeometry(5.3,1.2,4); eave1.rotateY(Math.PI/4); eave1.translate(0,5.3,0); B.put(eave1,0x221507);
  const f2=new THREE.BoxGeometry(4.4,3.0,3.4); f2.translate(0,7.4,0); B.put(f2,0x170f09);
  const eave2=new THREE.ConeGeometry(4.1,1.1,4); eave2.rotateY(Math.PI/4); eave2.translate(0,9.45,0); B.put(eave2,0x201406);
  const roof=new THREE.ConeGeometry(3.3,1.6,4); roof.rotateY(Math.PI/4); roof.translate(0,10.8,0); B.put(roof,0x1c1107);
  const fin=new THREE.SphereGeometry(0.15,8,6); fin.translate(0,11.7,0); B.put(fin,0xc9a24a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x080505}),{c:0xd8a060,i:0.22,p:2.5})));
  const winMat=new THREE.MeshBasicMaterial({color:0xffb868,transparent:true,opacity:0.85,fog:false,depthWrite:false});
  const wins=[];
  [[-1.35,3.3,2.42,1.3,1.0],[1.35,3.3,2.42,1.3,1.0],[0,7.6,1.88,1.55,0.85]].forEach(function(w){
    const p=new THREE.Mesh(new THREE.PlaneGeometry(w[3],w[3]*0.82),winMat);
    p.position.set(w[0],w[1],w[2]); p.renderOrder=-5; g.add(p); wins.push(p);
  });
  const wg=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8863a,
    transparent:true,opacity:0.26,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  wg.scale.set(9,6,1); wg.position.set(0,5.4,2.6); wg.renderOrder=-5; g.add(wg);
  return {g,wins,wg,update(t,k){
    const e=0.80+0.08*Math.sin(t*2.1)+0.04*Math.sin(t*7.7);
    wins.forEach(function(p,i){ p.material.opacity=k*0.85*e*(i===2?0.85:1); });
    wg.material.opacity=k*0.26*(0.82+0.18*Math.sin(t*1.7+1));
  }};
}

/* 楼栏：望柱 + 寻杖 + 华板的矮栏（境①楼心回廊口，月从栏外沉下去；合批 1 mesh） */
function makeLouLan(o){
  o=o||{};
  const w=o.w===undefined?15:o.w, h=o.h===undefined?1.35:o.h;
  const B=new GeoBag();
  const top=new THREE.BoxGeometry(w,0.11,0.18); top.translate(0,h,0); B.put(top,0x44311c);
  const mid=new THREE.CylinderGeometry(0.032,0.032,w,6); mid.rotateZ(Math.PI/2); mid.translate(0,h*0.70,0); B.put(mid,0x352617);
  const board=new THREE.BoxGeometry(w,h*0.46,0.075); board.translate(0,h*0.30,0); B.put(board,0x2c2013);
  const n=Math.round(w/1.4);
  for(let i=0;i<=n;i++){
    const x=-w/2+w*i/n;
    const p=new THREE.BoxGeometry(0.11,h,0.13); p.translate(x,h/2,0); B.put(p,0x302214);
    const cap=new THREE.BoxGeometry(0.17,0.07,0.20); cap.translate(x,h+0.055,0); B.put(cap,0x4c3820);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4426,emissive:0x080504}),{c:0xd8a060,i:0.20,p:2.4})));
  return g;
}

/* 楼心月：暖白月轮 + 双层暖辉（fog:false，辉光沿视线方向前移避开共面 z-fight），
   随彻夜歌舞徐徐西沉——境①的时间性元素（标志性瞬间） */
function makeLouYue(o){
  o=o||{};
  const r=o.r===undefined?2.6:o.r;
  const S=256, cv=document.createElement('canvas'); cv.width=cv.height=S;
  const cx=cv.getContext('2d');
  const gr=cx.createRadialGradient(S/2,S/2,0,S/2,S/2,S/2);
  gr.addColorStop(0.00,'rgba(255,250,234,1)');
  gr.addColorStop(0.55,'rgba(255,240,204,0.98)');
  gr.addColorStop(0.82,'rgba(252,220,158,0.80)');
  gr.addColorStop(1.00,'rgba(248,206,138,0)');
  cx.fillStyle=gr; cx.fillRect(0,0,S,S);
  const tex=new THREE.CanvasTexture(cv);
  const disc=new THREE.Mesh(new THREE.CircleGeometry(r,36),
    new THREE.MeshBasicMaterial({map:tex,color:0xffffff,transparent:true,opacity:1.0,fog:false,depthWrite:true}));
  disc.renderOrder=-7;
  const g=new THREE.Group(); g.add(disc);
  const halo=[];
  [[r*5.0,0.34,0xd8a45c,2.2],[r*2.5,0.50,0xffe2a8,1.1]].forEach(function(cfg){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:cfg[2],
      transparent:true,opacity:cfg[1],depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    s.scale.set(cfg[0],cfg[0],1); s.position.set(0,0,cfg[3]); s.renderOrder=-7; g.add(s); halo.push({s:s,op:cfg[1]});
  });
  return {g,disc,update(t,k){
    for(let i=0;i<halo.length;i++)
      halo[i].s.material.opacity=k*halo[i].op*(0.88+0.12*Math.sin(t*0.8+i*1.9));
  }};
}

/* 银釭：银质釭灯——覆盆足 + 擎柱 + 承盘 + 银灯盏 + 金环口 + 焰（境②主器，末境交互「挑亮」） */
function makeYinGang(o){
  o=o||{};
  const h=o.h===undefined?0.95:o.h;
  const B=new GeoBag();
  const ft=new THREE.CylinderGeometry(0.24,0.32,0.10,12); ft.translate(0,0.05,0); B.put(ft,0x5c616c);
  const pole=new THREE.CylinderGeometry(0.05,0.085,h,8); pole.translate(0,0.10+h/2,0); B.put(pole,0x7e848f);
  const dish=new THREE.CylinderGeometry(0.27,0.14,0.09,12); dish.translate(0,0.10+h+0.045,0); B.put(dish,0x8e949f);
  const cup=new THREE.SphereGeometry(0.185,12,8,0,Math.PI*2,0,1.32); cup.scale(1.1,0.66,1.1);
  cup.translate(0,0.10+h+0.09,0); B.put(cup,0xb4bac6);
  const ring=new THREE.TorusGeometry(0.215,0.024,6,18); ring.rotateX(Math.PI/2);
  ring.translate(0,0.10+h+0.125,0); B.put(ring,0xe0c060);
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:70,
    specular:0xd4dce8,emissive:0x0a0c10}),{c:0xe6ecf4,i:0.44,p:2.9}));
  const g=new THREE.Group(); g.add(mesh);
  const fl=makeFlame({h:o.fh===undefined?0.56:o.fh,w:o.fw===undefined?0.21:o.fw,planes:3,
    embers:o.embers===undefined?12:o.embers,esize:3.5,spark:true,
    light:o.light||0,lightC:0xffd9a0,lightD:o.lightD||24,
    core:0xffe4b4,outer:0xff8a2c,wide:0.30,seed:Math.random()*8});
  fl.g.position.y=0.10+h+0.14; g.add(fl.g);
  return {g,fl,update(t,k){ fl.update(t,k); }};
}

function bCover(){ // 卷首 · 夜色楼远 —— 歌楼剪影窗烛点点，星河低垂，尘金浮游（当年歌筵在灯火阑珊处）
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07070b,c2:0x120c08});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:1731,color:0x0a0809,atmo:0x4a3018,fogK:0.70,glowK:0.10,y:-14});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const lou=makeLouGe(); lou.g.position.set(-17,0,-58); lou.g.scale.setScalar(1.15); g.add(lou.g);
  const lou2=makeLouGe(); lou2.g.position.set(30,0,-84); lou2.g.scale.setScalar(0.72); lou2.g.rotation.y=-0.4; g.add(lou2.g);
  const servants=makeCrowd({n:3,rect:[12,-46,26,10],seed:173,color:0x131014,rimC:0xe0c060,rim:0.20,sMin:0.8,sMax:1.0});
  g.add(servants.mesh);
  const motes=makeGlow({n:60,box:[190,32,100],pos:[0,9,-32],color:0xe0c060,size:6,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[240,30,140],pos:[0,8,-52],scale:78,color:0x6a4a38,op:0.09});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',n:2,w:16,d:6,color:0x050405,seed:17,sway:0.9,rim:0.14});
  fg.g.position.set(-16,-1,18); g.add(fg.g);
  const rail=makeForeground({kind:'栏杆',w:26,h:3.0,color:0x070505,seed:19,rim:0.12});
  rail.g.position.set(0,-2,20); g.add(rail.g);
  addLights(g,{c:0xd8a060,i:0.30,p:[-40,44,30]},{c:0x2c241a,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); servants.update(t);
    fg.update(t,k); rail.update(t,k); lou.update(t,k); lou2.update(t,k);
  }};
}

function bWuYue(){ // 壹 · 舞低楼月 —— 彩袖殷勤捧玉钟，当年拼却醉颜红；舞低杨柳楼心月，歌尽桃花扇底风
  const g=new THREE.Group();
  const ctl={t:0};
  const grd=makeGround({r:120,c1:0x0b0706,c2:0x170d08});
  grd.mesh.position.y=-0.05; g.add(grd.mesh);
  const ridge=makeRange({r:210,h:20,layers:2,peaks:4,seed:1732,color:0x0b0807,atmo:0x3a2412,fogK:0.68,glowK:0.04});
  g.add(ridge.g);
  /* 楼心格局：背帷 + 双侧垂帐 + 四柱一枋 + 楼心矮栏（月从栏外沉下去） */
  const curtain=makeCurtain({w:9.8,h:4.8,color:0x4a2a22,dark:0x1c0f0c,folds:7,deep:0.6});
  curtain.g.position.set(0,0,-9.9); g.add(curtain.g);
  const curtL=makeCurtain({w:5.2,h:4.4,color:0x3a2a18,dark:0x181008,folds:5,deep:0.6});
  curtL.g.position.set(-5.9,0,-7.2); curtL.g.rotation.y=1.25; g.add(curtL.g);
  const curtR=makeCurtain({w:5.2,h:4.4,color:0x3a2a18,dark:0x181008,folds:5,deep:0.6});
  curtR.g.position.set(5.9,0,-7.2); curtR.g.rotation.y=-1.25; g.add(curtR.g);
  const PB=new GeoBag();
  [[-5.4,-3.2],[5.4,-3.2],[-5.4,-8.8],[5.4,-8.8]].forEach(function(p){
    const col=new THREE.CylinderGeometry(0.21,0.26,5.6,9); col.translate(p[0],2.8,p[1]); PB.put(col,0x2a1a0e);
    const cap=new THREE.BoxGeometry(0.64,0.15,0.64); cap.translate(p[0],5.68,p[1]); PB.put(cap,0x1e1309);
  });
  const beam=new THREE.BoxGeometry(11.2,0.36,0.44); beam.translate(0,5.35,-8.8); PB.put(beam,0x1e1309);
  g.add(PB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x8a6a3a,emissive:0x0a0704}),{c:0xe0c060,i:0.26,p:2.5})));
  const lan=makeLouLan({w:15,h:1.35}); lan.position.set(0,0,-12.6); g.add(lan);
  /* 楼心月：随歌舞徐徐西沉（0.17/秒，楼外开阔天际——月路避开楼身，沉入山际为止） */
  const louyue=makeLouYue({r:2.6}); louyue.g.position.set(-13,12.4,-46); g.add(louyue.g);
  const louyueY0=12.4;
  /* 案 + 盘飧 + 酒器（玉钟之宴：金樽一、陶壶一、金杯四、香碗一） */
  const tb=makeTable({w:4.8,d:1.9,h:1.5,wood:0x33200f}); tb.g.position.set(-1.7,0,-5.9); g.add(tb.g);
  const dish1=makeDish({r:0.8,n:5}); dish1.g.position.set(-2.8,1.5,-6.2); dish1.g.rotation.y=0.3; g.add(dish1.g);
  const dish2=makeDish({r:0.7,n:4,foods:[0xc08a3a,0x6a7a3a,0xd8b45a,0x8a5a2a]});
  dish2.g.position.set(-0.6,1.5,-6.6); g.add(dish2.g);
  const zun=makeVessel({type:'樽',mat:'金',scale:1.05,liquid:true}); zun.g.position.set(-1.2,1.5,-5.4); g.add(zun.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.9}); hu.g.position.set(-3.7,1.5,-5.6); g.add(hu.g);
  [[0.1,-5.3],[0.7,-6.2],[-2.3,-5.3],[0.4,-6.6]].forEach(function(p,i){
    const cp=makeVessel({type:'杯',mat:'金',scale:0.8,liquid:i<2,shadow:false});
    cp.g.position.set(p[0],1.5,p[1]); g.add(cp.g);
  });
  const censer=makeVessel({type:'碗',mat:'陶',scale:0.7,shadow:false}); censer.g.position.set(-3.8,1.5,-6.5); g.add(censer.g);
  const smoke=makeGlow({n:28,box:[0.6,4.6,0.6],pos:[-3.8,1.9,-6.5],color:0xc0a890,size:3.4,speed:0.16,rise:1,maxA:0.15});
  g.add(smoke.points);
  /* 人物：彩袖舞者环舞，主人与客坐饮，侍女立后（玉钟劝酒的正是她） */
  const dancer=makeFigure({pose:'独立',robe:0x6a3050,belt:0xe0c060,skin:0xe0c0a8,hair:0x1a1210,collar:0xe8d0b0,
    hat:'发髻',face:0.3,scale:0.95,rim:0.62,rimC:0xffd890,noProp:true});
  dancer.position.set(2.7,0,-4.8); g.add(dancer);
  const host=makeFigure({pose:'坐饮',robe:0x6e7a8c,belt:0x8a6a3a,skin:0xd9b189,hat:'幞头',
    face:-0.3,scale:1.02,rim:0.5,rimC:0xffd890});
  host.position.set(-3.0,0,-4.3); host.rotation.y=0.5; g.add(host);
  const guest=makeFigure({pose:'坐饮',robe:0x8a6a4a,belt:0x6a5030,skin:0xd9b189,hat:'幞头',
    face:0.4,scale:1.0,rim:0.5,rimC:0xffd890});
  guest.position.set(-0.5,0,-7.4); guest.rotation.y=-2.7; g.add(guest);
  const maid=makeFigure({pose:'独立',robe:0x2c2420,belt:0x6a5030,skin:0xd9b189,hat:'发髻',
    face:0.5,scale:0.8,rim:0.4,rimC:0xffd890,noProp:true});
  maid.position.set(4.5,0,-8.3); maid.rotation.y=-1.2; g.add(maid);
  /* 灯具成列：立灯檠二（四柱侧）+ 案上烛台二 */
  const dq1=makeDengQing({light:0.9,lightD:22}); dq1.g.position.set(-5.0,0,-3.0); g.add(dq1.g);
  const dq2=makeDengQing({h:2.5}); dq2.g.position.set(5.0,0,-8.6); g.add(dq2.g);
  const zt1=makeZhuTai({light:0.85,lightD:18}); zt1.g.position.set(-0.3,1.5,-5.1); g.add(zt1.g);
  const zt2=makeZhuTai({stem:0.35,wax:0.65}); zt2.g.position.set(-4.0,1.5,-5.2); g.add(zt2.g);
  /* 扇底风：桃花色风屑绕舞者（NormalBlending，非流萤）+ 金尘 + 雾 */
  const breeze=makeGlow({n:64,box:[6.5,4.6,4.6],pos:[2.7,1.6,-4.8],color:0xdca8a2,size:5.0,speed:0.12,rise:0.14,add:false,maxA:0.30});
  g.add(breeze.points);
  const motes=makeGlow({n:48,box:[36,11,26],pos:[-1,3.6,-5],color:0xe0c060,size:4.4,speed:0.05,rise:0.22,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[130,16,70],pos:[0,4,-24],scale:56,color:0x6a4a38,op:0.07});
  g.add(mist.g);
  /* 前景：回廊栏 + 楼外探枝 */
  const rail=makeForeground({kind:'栏杆',w:24,h:2.8,color:0x070505,seed:23,rim:0.12});
  rail.g.position.set(2,-1.6,8.6); g.add(rail.g);
  const fg2=makeForeground({kind:'树枝',n:2,w:13,d:5,color:0x050404,seed:29,sway:1.0,rim:0.12});
  fg2.g.position.set(-12,-0.6,9); g.add(fg2.g);
  addLights(g,{c:0xffb070,i:0.32,p:[-56,34,-40]},{c:0x342416,i:0.72});
  const pl=new THREE.PointLight(0xffc890,1.55,28); pl.position.set(0.4,3.6,-5.2); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ctl.t+=dt;
    ridge.update(t,0); mist.update(t,k); motes.update(t); breeze.update(t); smoke.update(t);
    rail.update(t,k); fg2.update(t,k);
    /* 舞者环舞：回旋 + 侧腰 + 轻踮 */
    dancer.rotation.y=0.3+Math.sin(ctl.t*0.5)*1.1;
    dancer.rotation.z=0.05*Math.sin(ctl.t*1.8);
    dancer.position.y=0.05*Math.abs(Math.sin(ctl.t*1.8));
    dancer.update(t,k); host.update(t,k); guest.update(t,k); maid.update(t,k);
    dq1.update(t,k); dq2.update(t,k); zt1.update(t,k); zt2.update(t,k);
    louyue.g.position.y=Math.max(2.4,louyueY0-ctl.t*0.17);   // 舞低楼心月
    louyue.update(t,k);
    pl.intensity=k*1.55*(0.70+0.18*Math.sin(t*8.8)+0.12*Math.sin(t*15.7));
  }};
}

function bDengZhao(){ // 贰（末境·可点击）· 银釭疑梦 —— 从别后忆相逢，几回魂梦与君同；今宵剩把银釭照，犹恐相逢是梦中
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,glow:0,pulse:0};
  const grd=makeGround({r:110,c1:0x0a090c,c2:0x141010});
  grd.mesh.position.y=-0.02; g.add(grd.mesh);
  const ridge=makeRange({r:220,h:22,layers:2,peaks:5,seed:1733,color:0x0b0a0c,atmo:0x3a2a24,fogK:0.72,glowK:0.05});
  g.add(ridge.g);
  /* 梦境帐幕：低饱和暖紫灰帷 + 隐约屏柱 */
  const curtain=makeCurtain({w:10,h:4.6,color:0x3c2c30,dark:0x181114,folds:6,deep:0.6});
  curtain.g.position.set(0.4,0,-9.2); g.add(curtain.g);
  const PB=new GeoBag();
  [[-5.2,-4.2],[5.2,-4.2]].forEach(function(p){
    const col=new THREE.CylinderGeometry(0.20,0.25,5.2,9); col.translate(p[0],2.6,p[1]); PB.put(col,0x241a14);
    const cap=new THREE.BoxGeometry(0.6,0.14,0.6); cap.translate(p[0],5.25,p[1]); PB.put(cap,0x1a120c);
  });
  g.add(PB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a5a48,emissive:0x0a0808}),{c:0xc0a88a,i:0.22,p:2.5})));
  /* 魂梦流光：别后梦里那些相逢，在雾里横流（低饱和暖，弱化为梦境 bokeh） */
  const dream=makeFlow({n:44,box:[24,7,16],pos:[0,4.4,-6],color:0x9a8878,size:16,speed:0.5,maxA:0.10});
  g.add(dream.points);
  /* 小案横在两人之间：樽 + 双杯 + 银釭（交互主器） */
  const tb=makeTable({w:2.6,d:1.3,h:1.4,wood:0x2c1c0e}); tb.g.position.set(0,0,-3.9); g.add(tb.g);
  const zun=makeVessel({type:'樽',mat:'金',scale:0.9,liquid:true}); zun.g.position.set(-0.75,1.4,-3.9); g.add(zun.g);
  [[0.5,-3.6],[0.55,-4.15]].forEach(function(p){
    const cp=makeVessel({type:'杯',mat:'金',scale:0.75,liquid:false,shadow:false});
    cp.g.position.set(p[0],1.4,p[1]); g.add(cp.g);
  });
  const yg=makeYinGang({light:0,lightD:22}); yg.g.position.set(0.15,1.4,-3.95); g.add(yg.g);
  /* 灯辉：灯下相认的暖晕（初值即最大值，闲置半明，挑亮后 ramp 至满） */
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffd9a0,
    transparent:true,opacity:0.75,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(6.5,6.5,1); halo.position.set(0.15,2.8,-3.95); halo.renderOrder=3; g.add(halo);
  const HALO_BASE=0.75;
  const pl=new THREE.PointLight(0xffd9a0,1.5,24); pl.position.set(0.15,2.6,-3.9); g.add(pl);
  /* 重逢二人：灯下相对（他与她，当年彩袖今何在） */
  const him=makeFigure({pose:'独立',robe:0x5c6678,belt:0x8a6a3a,skin:0xd9b189,hat:'幞头',
    face:-2.5,scale:1.04,rim:0.55,rimC:0xffd890,noProp:true});
  him.position.set(2.0,0,-2.9); g.add(him);
  const her=makeFigure({pose:'独立',robe:0x63485e,belt:0xe0c060,skin:0xe0c0a8,hair:0x1a1210,collar:0xe8d0b0,
    hat:'发髻',face:0.6,scale:0.95,rim:0.6,rimC:0xffd890,noProp:true});
  her.position.set(-1.8,0,-4.9); g.add(her);
  /* 梦雾：重雾化（点击后脉动更浓——恍然如梦） */
  const dreamGlow=makeGlow({n:40,box:[11,7,8],pos:[0.2,2.6,-4.2],color:0xc0a890,size:7,speed:0.07,rise:0.10,add:false,maxA:0.28});
  g.add(dreamGlow.points);
  const mist=makeMist({n:6,spread:[120,14,60],pos:[0,4,-16],scale:55,color:0x6a5a50,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:36,box:[30,9,22],pos:[0,4,-6],color:0xe0c060,size:4,speed:0.04,rise:0.15,maxA:0.15});
  g.add(motes.points);
  const burst=makeBurst({n:70,color:0xffe0b0,pos:[0.15,2.5,-3.9]}); g.add(burst.points);
  /* 前景：纱栏 + 窗外探枝 */
  const rail=makeForeground({kind:'栏杆',w:22,h:2.8,color:0x060506,seed:31,rim:0.10});
  rail.g.position.set(-1,-1.4,7.8); g.add(rail.g);
  const fg2=makeForeground({kind:'树枝',n:2,w:13,d:5,color:0x040304,seed:37,sway:0.8,rim:0.10});
  fg2.g.position.set(-11,-0.5,8.5); g.add(fg2.g);
  addLights(g,{c:0xa8886a,i:0.22,p:[-40,30,20]},{c:0x2e2822,i:0.74});
  const DREAM_PULSE_T=2.6;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.glow=Math.min(1,ctl.glow+dt/1.8);
        ctl.pulse=Math.max(0,ctl.pulse-dt/DREAM_PULSE_T);
      }
      const gl=ctl.glow, pu=ctl.pulse;
      ridge.update(t,0); mist.update(t,k); motes.update(t); dream.update(t);
      rail.update(t,k); fg2.update(t,k); dreamGlow.update(t);
      dreamGlow.mat.uniforms.uMaxA.value=0.28*(1.0+1.3*gl*pu);      // 疑在梦中：雾涌
      yg.update(t,k);
      yg.fl.g.scale.setScalar(1+0.55*gl);                            // 挑亮：焰起
      halo.material.opacity=k*HALO_BASE*(0.55+0.45*gl*(0.85+0.15*Math.sin(t*2.6)));
      him.update(t,k); her.update(t,k);
      him.rotation.y=-2.5+0.05*Math.sin(t*0.9);
      her.rotation.y=0.6+0.06*Math.sin(t*0.8+1.2);
      burst.update(t);
      pl.intensity=k*1.5*(0.55+0.45*gl*(0.85+0.15*Math.sin(t*2.6))+0.10*Math.sin(t*7.3));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.pulse=1;
        burst.fire();
        pluck(2,0.05,0.14); pluck(4,0.4,0.13); pluck(5,0.8,0.12); pluck(1,1.15,0.10); bell();
        const fl=$('#flash'); fl.textContent='犹恐相逢是梦中'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
