# -*- coding: utf-8 -*-
"""yi-qin-e.py —— 《忆秦娥》（唐·李白，传，no.154，水墨夜思）生成配置
两境：秦楼月咽（箫/柳/月）、汉家陵阙（西风残照·标志性瞬间，点击残照西风陵阙显形）"""

META = dict(
    N=2, slug='yi-qin-e', title='忆秦娥', dyn='唐 · 李白（传）', brand_author='李 白',
    gold_rgb='159,179,204',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#9fb3cc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(159,179,204,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(7,10,16', 1),
        ('rgba(4,6,11', 'rgba(6,8,14', 2),
        ('rgba(6,9,16', 'rgba(7,9,15', 1),
        ('rgba(3,5,9', 'rgba(5,7,12', 1),
        ('#0b101c', '#101624', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
    ],
    tip='轻点画面 / 按空格 —— 残照西风里，汉家陵阙显形',
    hint='← → 键或空格逐境游览 · 末境可点击残照西风，看汉家陵阙显形',
    cover_read='忆秦娥。唐，李白。箫声咽，秦娥梦断秦楼月。秦楼月，年年柳色，灞陵伤别。',
    cover_p1='两重意境，随词句次第展开：箫声呜咽、秦楼月冷，年年柳色见证灞陵伤别的月夜离愁；乐游原上清秋远望，咸阳古道音尘断绝，末了西风残照里，汉家陵阙默然显形。',
    cover_p2='边读词，边走进月夜离愁与千古兴亡交织的苍茫之境。',
    end_h2='残照 · 陵阙', cn_word='两',
    words_js="['再游一次，且听箫咽','初识秦娥，尚需共读','渐入佳境，再诵几遍','词境渐深，柳色如烟','已解灞陵折柳之意','残照阙影，千古苍茫']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'秦楼月咽', jing:'箫声呜咽，秦楼月冷 —— 梦断处，柳色年年，灞陵伤别。（箫 · 柳 · 月）',
  segs:[
   {c:'箫声咽，', p:py('xiāo shēng yè')},
   {c:'秦娥梦断秦楼月。', p:py('qín é mèng duàn qín lóu yuè')},
   {c:'秦楼月，', p:py('qín lóu yuè')},
   {c:'年年柳色，', p:py('nián nián liǔ sè')},
   {c:'灞陵伤别。', p:py('bà líng shāng bié')}],
  read:'箫声咽，秦娥梦断秦楼月。秦楼月，年年柳色，灞陵伤别。',
  yisi:'箫声呜咽，把秦娥从梦中惊醒，一弯秦楼月正冷冷相照。秦楼上的明月啊，年年照着一样的柳色——灞陵桥头，多少人曾在此折柳伤别。——以月之无情，照人间离恨。',
  zhu:[['咽','呜咽，形容箫声悲切低回（读 yè）'],['秦娥','秦地女子，此处指长安楼头闻箫的思妇'],['秦楼月','秦楼上的明月，叠句回环，如箫声呜咽不绝'],['灞陵','汉文帝陵，近灞桥，汉唐人东行送别至此，折柳相赠']] },
{ name:'汉家陵阙', jing:'西风残照之中，汉家陵阙默然显形 —— 千古兴亡，尽在此八字。（点击残照西风）',
  segs:[
   {c:'乐游原上清秋节，', p:py('lè yóu yuán shàng qīng qiū jié')},
   {c:'咸阳古道音尘绝。', p:py('xián yáng gǔ dào yīn chén jué')},
   {c:'音尘绝，', p:py('yīn chén jué')},
   {c:'西风残照，', p:py('xī fēng cán zhào')},
   {c:'汉家陵阙。', p:py('hàn jiā líng què')}],
  read:'乐游原上清秋节，咸阳古道音尘绝。音尘绝，西风残照，汉家陵阙。',
  yisi:'登上乐游原，正值清秋时节；咸阳古道上，车马音信早已断绝。音尘绝啊——只有西风吹过空旷的原野，残阳余晖里，汉家帝王的陵阙遗影默然矗立。伤今怀古，苍茫入骨。',
  zhu:[['乐游原','长安东南的高地，唐人登高游赏、远眺全城的胜地'],['音尘绝','车马之声与路上扬尘都已断绝，极写古道空旷寂寥'],['西风残照','秋风与落日余晖；王国维评此八字「遂关千古登临之口」'],['陵阙','帝王的陵墓与宫阙，此处指西汉帝陵的遗影']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「箫声咽」的下一句是？', o:['秦娥梦断秦楼月','秦楼月，年年柳色','西风残照，汉家陵阙'], a:0},
 {q:'「咸阳古道音尘绝」的下一句是？', o:['音尘绝，西风残照','乐游原上清秋节','年年柳色，灞陵伤别'], a:0},
 {q:'「箫声咽」中「咽」的正确读音和意思是？', o:['yān，咽喉','yè，呜咽，声音悲切低回','yàn，吞咽'], a:1},
 {q:'「灞陵伤别」里，汉唐人送别时折赠的是？', o:['杨柳枝','梅花','红豆'], a:0},
 {q:'下片「西风残照，汉家陵阙」寄托的主要情感是？', o:['登高览胜的欢愉','羁旅行役的劳苦','怀古伤今的苍茫兴亡之感'], a:2},
];
"""

SCENES_JS = """/* ================= 忆秦娥 · 两境场景（水墨夜思：秦楼月咽、汉家陵阙） ================= */

/* 灞柳：树干 + 树冠 + 一蓬下垂柳丝（TubeGeometry 沿弧线下挂），合批 1 mesh */
function makeWillow(o){
  o=o||{};
  const g=new THREE.Group(), B=new GeoBag(), R=seedRnd(o.seed===undefined?7:o.seed);
  const n=o.n===undefined?3:o.n, spread=o.spread===undefined?14:o.spread;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, h=5.5+R()*2.5, tilt=(R()-0.5)*0.3;
    const trunk=new THREE.CylinderGeometry(0.10,0.20,h,6);
    trunk.rotateZ(tilt); trunk.translate(x,h*0.5,0); B.put(trunk,0x0a0d13);
    const top=new THREE.SphereGeometry(1.1,7,5); top.scale(1.5,0.7,1.2);
    top.translate(x-Math.sin(tilt)*h,h,0); B.put(top,0x0c1017);
    const strands=6+Math.floor(R()*4);
    for(let s=0;s<strands;s++){
      const bx=x+(R()-0.5)*2.4, bz=(R()-0.5)*1.8, len=2.2+R()*2.6;
      const p0=new THREE.Vector3(bx,h+(R()-0.5)*0.8,bz);
      const p3=new THREE.Vector3(bx+(R()-0.5)*1.6,h-len,bz+(R()-0.5)*1.2);
      const p1=new THREE.Vector3(p0.x+(p3.x-p0.x)*0.2,p0.y-len*0.25,p0.z);
      const p2=new THREE.Vector3(p0.x+(p3.x-p0.x)*0.7,p0.y-len*0.7,p3.z);
      B.put(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([p0,p1,p2,p3]),7,0.035,4,false),0x0d1119);
    }
  }
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.22,p:2.4})));
  return g;
}

/* 秦楼：双层楼影 + 四阿顶 + 伸向水面的平台栏杆，合批 1 mesh（剪影 + 银边光） */
function makeQinlou(){
  const B=new GeoBag(), c1=0x0d1219, c2=0x111824, c3=0x18202e;
  const base=new THREE.BoxGeometry(11,1.2,8); base.translate(0,0.6,0); B.put(base,c1);
  const lower=new THREE.BoxGeometry(6.4,5.2,5.2); lower.translate(-1,1.2+2.6,0); B.put(lower,c2);
  const lowerRoof=new THREE.ConeGeometry(5.4,1.7,4); lowerRoof.rotateY(Math.PI/4);
  lowerRoof.scale(1.25,1,1.05); lowerRoof.translate(-1,6.4+0.85,0); B.put(lowerRoof,c3);
  const upper=new THREE.BoxGeometry(4.6,3.4,3.8); upper.translate(-1,7.6+1.7,0); B.put(upper,c2);
  const topRoof=new THREE.ConeGeometry(4.1,1.6,4); topRoof.rotateY(Math.PI/4);
  topRoof.scale(1.25,1,1.05); topRoof.translate(-1,11.2+0.8,0); B.put(topRoof,c3);
  const deck=new THREE.BoxGeometry(4.6,0.35,3.2); deck.translate(2.6,1.35,0.8); B.put(deck,c1);
  [1,-1].forEach(function(s){
    for(let i=0;i<4;i++){
      const post=new THREE.BoxGeometry(0.12,0.95,0.12);
      post.translate(1.2+i*0.95,1.35+0.65,0.8+s*1.35); B.put(post,c3);
    }
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x9fb3cc,i:0.34,p:2.5})));
  return g;
}

/* 灞桥：石拱 + 桥面分段沿拱起伏 + 栏柱 + 桥头，合批 1 mesh */
function makeBaBridge(){
  const B=new GeoBag();
  const arch=new THREE.TorusGeometry(9.5,0.55,6,18,Math.PI);
  arch.scale(1,0.30,1); arch.translate(0,0.15,0); B.put(arch,0x0b0f16);
  for(let i=0;i<7;i++){
    const x=-12+i*4;
    const y=3.0*Math.sqrt(Math.max(0.02,1-(x*x)/144))+0.35;
    const seg=new THREE.BoxGeometry(4.4,0.32,3.6); seg.translate(x,y,0); B.put(seg,0x0c1017);
    [1,-1].forEach(function(s){
      const post=new THREE.BoxGeometry(0.14,0.95,0.14);
      post.translate(x-1.6,y+0.6,s*1.55); B.put(post,0x141a26);
      const post2=new THREE.BoxGeometry(0.14,0.95,0.14);
      post2.translate(x+1.6,y+0.6,s*1.55); B.put(post2,0x141a26);
    });
  }
  [[-13.4],[13.4]].forEach(function(p){
    const ab=new THREE.BoxGeometry(3.4,1.1,4.4); ab.translate(p[0],0.55,0); B.put(ab,0x0a0e15);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.24,p:2.5})));
  return g;
}

function bCover(){ // 封面 · 秦月无声
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:154,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:155,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:10,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:64,box:[220,40,130],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bQinlou(){ // 一 · 秦楼月咽 —— 箫声、秦楼月、灞柳伤别
  const g=new THREE.Group();
  const water=makeWater({size:480,seg:90,amp:0.28,freq:0.12,speed:0.5,flow:[0.5,0.15],spec:1.9,
    deep:0x081221,shallow:0x14304a,skyc:0x23405e,moonDir:[34,118,-190]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:20,layers:2,peaks:4,seed:156,color:0x070a10,atmo:0x1c2739,fogK:0.62,glowK:0.06,y:-18});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 秦楼（左）+ 楼头窗月微光（冷银，月是唯一主角） */
  const tower=makeQinlou(); tower.position.set(-13,0,-24); g.add(tower);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.28,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(4.2,4.2,1); win.position.set(-13.4,8.4,-21.0); win.renderOrder=2; g.add(win);
  /* 秦娥：梦断楼头，指月吹箫 */
  const figure=makeFigure({pose:'指月',robe:0x1e2a3c,belt:0x5a6a82,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0x9fb3cc,rim:0.5,noProp:true,scale:1.5});
  figure.position.set(-10.4,1.52,-22.4); figure.rotation.y=0.7; g.add(figure);
  /* 灞桥 + 桥上送别人影（折柳伤别） */
  const bridge=makeBaBridge(); bridge.position.set(2,0,-14); g.add(bridge);
  const crowd=makeCrowd({n:4,rect:[-1.0,-15.6,6.4,1.2],seed:1542,color:0x11161f,rimC:0x8fa4c4,
    rim:0.18,sMin:0.4,sMax:0.52,y:3.55});
  g.add(crowd.mesh);
  /* 灞柳两岸（柳丝下挂） */
  const willow=makeWillow({n:4,spread:26,seed:1543}); willow.position.set(13,0,-17); g.add(willow);
  const willow2=makeWillow({n:3,spread:16,seed:1544}); willow2.position.set(-26,0,-20); g.add(willow2);
  /* 柳絮与微尘（水墨母题） */
  const catkins=makeGlow({n:70,box:[70,12,44],pos:[4,5,-10],color:0xbcc9dc,size:5,speed:0.06,rise:0.12,maxA:0.3});
  g.add(catkins.points);
  const mist=makeMist({n:7,spread:[220,22,120],pos:[0,8,-50],scale:76,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:1545,rim:0.14});
  rk.g.position.set(-14,-1.4,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:1546,sway:0.9});
  reeds.g.position.set(13,-1.3,12); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[-30,90,-40]},{c:0x1a2232,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); catkins.update(t);
    win.material.opacity=k*(0.22+0.06*Math.sin(t*0.7));
    crowd.update(t);
    rk.update(t,k); reeds.update(t,k);
  }};
}

/* 残照：天边一道冷赭余晖（水墨赛道的唯一非冷色，禁金——残照取锈赭不取金） */
const ZHAO_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const ZHAO_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float band=pow(smoothstep(0.0,0.5,vUv.y),1.7);
  band*=smoothstep(0.0,0.30,vUv.x)*smoothstep(1.0,0.70,vUv.x);
  float sway=0.86+0.14*sin(uTime*0.35+vUv.x*9.0);
  vec3 col=mix(vec3(0.50,0.29,0.21),vec3(0.24,0.18,0.21),clamp(vUv.y*1.5,0.0,1.0));
  gl_FragColor=vec4(col,uFade*uK*band*sway);
}`;

/* 汉家陵阙：双阙 + 夹墙门道，合批 1 mesh（点击前只是残照里的淡影） */
function makeLingque(){
  const B=new GeoBag(), c1=0x10141c, c2=0x161c28, c3=0x1d2534;
  [1,-1].forEach(function(s){
    const x=s*11;
    const base=new THREE.BoxGeometry(6.5,1.4,5.4); base.translate(x,0.7,0); B.put(base,c1);
    const body=new THREE.BoxGeometry(4.8,9.6,4.2); body.translate(x,1.4+4.8,0); B.put(body,c2);
    const guan=new THREE.BoxGeometry(5.9,2.5,4.9); guan.translate(x,11+1.25,0); B.put(guan,c2);
    const roof=new THREE.ConeGeometry(4.9,2.0,4); roof.rotateY(Math.PI/4);
    roof.scale(1.22,1,1.0); roof.translate(x,13.5+1.0,0); B.put(roof,c3);
  });
  [-1,1].forEach(function(s){
    const wall=new THREE.BoxGeometry(8.2,4.6,2.6); wall.translate(s*7.0,2.3,0); B.put(wall,c1);
    const pai=new THREE.BoxGeometry(8.2,0.5,2.8); pai.translate(s*7.0,4.85,0); B.put(pai,c2);
  });
  const g=new THREE.Group();
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a465c,emissive:0x05070c,transparent:true,opacity:0.95}),{c:0x9fb3cc,i:0.4,p:2.4});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat);
  mesh.renderOrder=1; g.add(mesh);
  return {g,mesh};
}

function bLingque(){ // 二（标志性瞬间·末境可点击）· 汉家陵阙 —— 点击残照西风，陵阙剪影显形
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  const grd=makeGround({r:170,c1:0x080a10,c2:0x11141c});
  grd.mesh.position.y=-0.4; g.add(grd.mesh);
  const ridge=makeRange({r:260,h:13,layers:2,peaks:3,seed:158,color:0x080a10,atmo:0x201d26,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 咸阳古道：一条空旷的长路，音尘绝 */
  const road=new THREE.Mesh(new THREE.PlaneGeometry(12,130),
    new THREE.MeshPhongMaterial({color:0x141119,shininess:4,specular:0x2a2434}));
  road.rotation.x=-Math.PI/2; road.position.set(0,0.06,-78); g.add(road);
  /* 残照：冷赭余晖 + 残日之魂 */
  const bandMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.55}},
    vertexShader:ZHAO_VERT,fragmentShader:ZHAO_FRAG});
  const band=new THREE.Mesh(new THREE.PlaneGeometry(250,32),bandMat);
  band.position.set(6,14,-152); band.renderOrder=2; g.add(band);
  const sunGhost=new THREE.Mesh(new THREE.CircleGeometry(6.5,28),
    new THREE.MeshBasicMaterial({color:0x7a4638,transparent:true,opacity:0.75,depthWrite:false,
      fog:false,blending:THREE.AdditiveBlending}));
  sunGhost.position.set(26,12,-150); sunGhost.renderOrder=2; g.add(sunGhost);
  /* 汉家陵阙（点击显形）+ 显形时的一线银月光晕 */
  const lq=makeLingque(); lq.g.position.set(0,0,-70); g.add(lq.g);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaebfd8,
    transparent:true,opacity:0.44,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(50,22,1); halo.position.set(0,10,-76); halo.renderOrder=1; g.add(halo);
  /* 神道石翁仲（陵前石人，千载无言） */
  const stoneOpt={pose:'独立',robe:0x2b3140,belt:0x495264,skin:0x848d9c,collar:0x556074,
    hat:'幞头',rimC:0x9fb3cc,rim:0.32,noProp:true,scale:2.4};
  const stone1=makeFigure(stoneOpt); stone1.position.set(-7.5,0,-38); stone1.rotation.y=0.16; g.add(stone1);
  const stone2=makeFigure(stoneOpt); stone2.position.set(7.5,0,-38); stone2.rotation.y=-0.16; g.add(stone2);
  /* 西风：横流风雾 + 秋原微尘 */
  const wind=makeFlow({n:240,box:[150,16,70],pos:[0,9,-46],color:0x8fa0b8,size:26,speed:6.5,maxA:0.26});
  g.add(wind.points);
  const motes=makeGlow({n:60,box:[160,20,90],pos:[0,8,-40],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.28});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[240,22,120],pos:[0,8,-62],scale:80,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:911,sway:1.5,rim:0.18});
  tree.g.position.set(15,-0.5,34); g.add(tree.g);
  const grass=makeForeground({kind:'芦苇',n:14,w:30,d:6,color:0x04060a,seed:913,sway:1.1});
  grass.g.position.set(-14,-0.6,31); g.add(grass.g);
  addLights(g,{c:0x9fb3cc,i:0.5,p:[-40,100,-60]},{c:0x1c202c,i:0.6});
  const pl=new THREE.PointLight(0x8a4a38,1.6,70); pl.position.set(8,12,-60); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/3.0);
      ridge.update(t,0); mist.update(t,k); wind.update(t); motes.update(t);
      tree.update(t,k); grass.update(t,k);
      bandMat.uniforms.uTime.value=t; bandMat.uniforms.uFade.value=k;
      bandMat.uniforms.uK.value=0.55+0.45*ctl.reveal;
      sunGhost.material.opacity=k*(0.40+0.10*Math.sin(t*0.5)+0.25*ctl.reveal);
      lq.mesh.material.opacity=k*(0.18+0.77*ctl.reveal);
      halo.material.opacity=k*(0.10+0.34*ctl.reveal);
      pl.intensity=k*1.6*(0.25+0.75*ctl.reveal*(0.85+0.15*Math.sin(t*2.2)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(3,0.05,0.13); pluck(1,0.5,0.11); pluck(4,1.0,0.09);
        const fl=$('#flash'); fl.textContent='汉家陵阙'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(34,118,-190),ms:1.8,mph:0,mhaze:0.05,dirC:C(0x8fa4c8),dirI:0.5,
  dirP:new THREE.Vector3(30,90,-40),ambC:C(0x1a2232),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,16,-40],lt:[0,16,-40]},
  sky:()=>SK({top:C(0x060910),hor:C(0x141c2a),bot:C(0x080b11),fog:C(0x0f1520),fd:0.0048,star:0.45,
    ms:1.6,moon:new THREE.Vector3(20,100,-180),
    dirC:C(0x8fa4c8),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'秦楼月咽',dwell:16,river:0.03,build:bQinlou,
  cam:{f:[0,6,20],t:[1.2,5.8,17],lf:[-2,7,-22],lt:[-1,6.5,-24]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0060,star:0.5,
    ms:1.9,mph:0,mhaze:0.05,moon:new THREE.Vector3(34,118,-190),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
{ name:'汉家陵阙',dwell:17,river:0.02,build:bLingque,
  cam:{f:[0,6.5,44],t:[0,7,38],lf:[0,10,-70],lt:[1.5,10.5,-76]},
  sky:()=>SK({top:C(0x0a0d14),hor:C(0x262028),bot:C(0x0a0c11),fog:C(0x121520),fd:0.0065,star:0.45,
    ms:1.7,mph:0.1,mhaze:0.04,moon:new THREE.Vector3(-50,125,-200),
    dirC:C(0x9fb3cc),dirI:0.5,ambC:C(0x1c202c),ambI:0.6}) },
];
"""
