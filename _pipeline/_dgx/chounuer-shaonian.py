# -*- coding: utf-8 -*-
"""chounuer-shaonian.py —— 《丑奴儿·书博山道中壁》（宋·辛弃疾，no.191，水墨夜思）生成配置
两境（今昔两层愁，同一座层楼同景叠化）：
  壹·爱上层楼 —— 少年登楼，为赋新词强说愁（稍亮稍暖，锈色霜叶是全页唯一暖处）
  贰·却道天凉 —— 而今识尽愁滋味，欲说还休（转冷转沉；标志性瞬间：一声轻叹化雾）
末境可点击：楼影今昔叠化 + 秋声四起（落叶骤急、西风横流、雁阵横空、四声下行的轻叹）"""

META = dict(
    N=2, slug='chounuer-shaonian', title='丑奴儿', dyn='宋 · 辛弃疾', brand_author='辛弃疾',
    gold_rgb='160,180,204',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#a0b4cc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(160,180,204,.26);
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
    tip='轻点画面 / 按空格 —— 层楼今昔叠化，秋声四起',
    hint='← → 键或空格逐境游览 · 末境可点击层楼：今昔叠化，秋声四起',
    cover_read='丑奴儿·书博山道中壁。宋，辛弃疾。少年不识愁滋味，爱上层楼。爱上层楼，为赋新词强说愁。',
    cover_p1='两重意境，随词句次第展开：先随少年爱上层楼，为赋新词强说一段闲愁；再伴稼轩凭栏独立，欲说还休——万千愁绪，只化作「天凉好个秋」的一声轻叹。同一座层楼，今昔两样心境。',
    cover_p2='边读词，边走进辛弃疾笔下从「强说愁」到「欲说还休」的今昔对照之境。',
    end_h2='天凉 · 好个秋', cn_word='两',
    words_js="['再游一次，且听秋声','初识稼轩，尚需共读','渐入佳境，再诵几遍','词境渐深，秋意渐浓','已解今昔两层愁','欲说还休，一声轻叹']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'爱上层楼', jing:'少年登楼望远，意气扬扬 —— 新词未成，先强说一段愁。（秋山 · 层楼 · 霜叶）',
  segs:[
   {c:'少年不识愁滋味，', p:py('shào nián bù shí chóu zī wèi')},
   {c:'爱上层楼。', p:py('ài shàng céng lóu')},
   {c:'爱上层楼，', p:py('ài shàng céng lóu')},
   {c:'为赋新词强说愁。', p:py('wèi fù xīn cí qiǎng shuō chóu')}],
  read:'少年不识愁滋味，爱上层楼。爱上层楼，为赋新词强说愁。',
  yisi:'少年时候不懂得什么是愁，偏偏喜欢登上高楼；喜欢登上高楼，为写一首新词，便勉强说出许多「愁」来。——少年的愁是修辞，是登楼望远的意气。',
  zhu:[['丑奴儿','词牌名，双调四十四字，又名「采桑子」'],['不识','不懂，未曾真正体味'],['层楼','高楼'],['强说愁','本无愁而勉强说愁；强，读 qiǎng'],['赋','填写、写作（诗词）']] },
{ name:'却道天凉', jing:'欲说还休，欲说还休 —— 万千愁绪，只化作一声轻叹：天凉好个秋。（凭栏 · 轻叹 · 雁声）',
  segs:[
   {c:'而今识尽愁滋味，', p:py('ér jīn shí jìn chóu zī wèi')},
   {c:'欲说还休。', p:py('yù shuō hái xiū')},
   {c:'欲说还休，', p:py('yù shuō hái xiū')},
   {c:'却道天凉好个秋。', p:py('què dào tiān liáng hǎo gè qiū')}],
  read:'而今识尽愁滋味，欲说还休。欲说还休，却道天凉好个秋。',
  yisi:'如今尝尽了愁的滋味，想说，却终于没有说；想说，却终于没有说——只淡淡道一句：好一个凉爽的秋天啊。满腹愁绪，尽在不言中。',
  zhu:[['识尽','尝够，深深体味透了'],['欲说还休','想说却终于没有说；还，读 hái'],['却道','反倒说，只说'],['博山','在今江西广丰西南；辛弃疾落职闲居上饶带湖时，常往返博山道间，此词题于道中壁']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「少年不识愁滋味」的下一句是？', o:['爱上层楼','欲说还休','为赋新词强说愁'], a:0},
 {q:'「欲说还休」的下一句是？', o:['却道天凉好个秋','爱上层楼','而今识尽愁滋味'], a:0},
 {q:'「为赋新词强说愁」中「强」的正确读音与意思是？', o:['qiáng，强大','qiǎng，勉强','jiàng，倔强'], a:1},
 {q:'这首词题于博山道中壁，其时辛弃疾正处于怎样的人生境况？', o:['率军北伐，收复中原','被劾落职，闲居江西带湖','少年得意，名满天下'], a:1},
 {q:'上片「强说愁」与下片「欲说还休」对照，要表达的是？', o:['秋去冬来，天气转凉的感慨','愁随阅历而深：昔日无愁强说，今朝愁重反难言说','少年与暮年登楼的爱好不同'], a:1},
];
"""

SCENES_JS = """/* ================= 丑奴儿 · 两境场景（水墨夜思：爱上层楼、却道天凉） =================
   今昔对照是全词骨架：同一座八角层楼、同一条山道、同一个凭栏处——
   壹稍亮稍暖（青春），贰转冷转沉（暮年）；点击层楼，楼影今昔叠化，秋声四起。 */

/* 收集一个 figure 的材质（躯干+双臂共用一份）并钉上 baseOpacity 上限 */
function figMats(fig){
  const mats=[];
  fig.traverse(function(o){ if(o.material&&mats.indexOf(o.material)<0)mats.push(o.material); });
  mats.forEach(function(m){ m.transparent=true; });
  return mats;
}

/* 落叶：自定义着色器（菱形叶影，自上而下飘落带摆）——水墨母题里唯一的锈色 */
const LEAF_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform float uBoxH;
varying float vA;
void main(){
  float life=fract(uTime*uSpeed+aSeed);
  vec3 p=position;
  p.y+=uBoxH*(0.5-life);
  p.x+=sin(uTime*1.15+aSeed*57.0)*1.8;
  p.z+=cos(uTime*0.85+aSeed*23.0)*1.3;
  vA=smoothstep(0.0,0.12,life)*smoothstep(1.0,0.78,life);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const LEAF_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=abs(q.x)*1.6+abs(q.y);
  float a=smoothstep(0.5,0.1,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLuoye(o){
  const n=o.n===undefined?40:o.n, box=o.box||[50,16,26], pos=o.pos||[0,7,-16];
  const color=o.color===undefined?0x8a5a40:o.color, speed=o.speed===undefined?0.05:o.speed;
  const maxA=o.maxA===undefined?0.4:o.maxA, size=o.size===undefined?6:o.size;
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1]*0.5;
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=size*(0.6+Math.random()*0.8);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uSpeed:{value:speed},uBoxH:{value:box[1]},
      uColor:{value:C(color)},uFade:{value:1},uMaxA:{value:maxA}},
    vertexShader:LEAF_VERT,fragmentShader:LEAF_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* 秋雁南征：V 字雁阵（合批 1 mesh），update 里沿 x 缓移横空 */
function makeYanzhen(o){
  o=o||{};
  const n=o.n===undefined?7:o.n, B=new GeoBag();
  for(let i=0;i<n;i++){
    const k=Math.ceil(i/2), bx=-k*2.6, by=k*0.62;
    const w1=new THREE.PlaneGeometry(1.6,0.4); w1.rotateZ(0.45); w1.translate(bx-0.66,by+0.16,0);
    const w2=new THREE.PlaneGeometry(1.6,0.4); w2.rotateZ(-0.45); w2.translate(bx+0.66,by+0.16,0);
    B.put(w1,0x11161f); B.put(w2,0x11161f);
  }
  const mesh=new THREE.Mesh(mergeGeos(B.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,transparent:true,
      opacity:0.30,specular:0x2a3446,emissive:0x05070c}));
  mesh.renderOrder=2; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh};
}

/* 八角层楼：石台基 + 楼身 + 平座栏杆 + 攒尖顶（合批 1 mesh）——「爱上层楼」的那座楼 */
function makeCenglou(){
  const B=new GeoBag(), c1=0x0c1017, c2=0x121926, c3=0x1a2332;
  const base=new THREE.CylinderGeometry(4.6,5.0,1.3,8); base.translate(0,0.65,0); B.put(base,c1);
  const body1=new THREE.CylinderGeometry(3.2,3.6,5.2,8); body1.translate(0,1.3+2.6,0); B.put(body1,c2);
  const eave1=new THREE.CylinderGeometry(4.5,3.8,0.55,8); eave1.translate(0,6.45,0); B.put(eave1,c3);
  const deck=new THREE.CylinderGeometry(4.2,4.2,0.5,8); deck.translate(0,6.75,0); B.put(deck,c1);
  for(let i=0;i<12;i++){
    const a=i/12*Math.PI*2;
    const post=new THREE.BoxGeometry(0.14,1.05,0.14);
    post.translate(Math.cos(a)*3.9,7.77,Math.sin(a)*3.9); B.put(post,c3);
  }
  const rail=new THREE.TorusGeometry(3.9,0.07,5,24); rail.rotateX(Math.PI/2);
  rail.translate(0,8.25,0); B.put(rail,c3);
  const body2=new THREE.CylinderGeometry(2.5,2.8,4.2,8); body2.translate(0,7.0+2.1,0); B.put(body2,c2);
  const roof=new THREE.ConeGeometry(3.9,2.8,8); roof.translate(0,11.2+1.4,0); B.put(roof,c3);
  const finial=new THREE.SphereGeometry(0.24,8,6); finial.translate(0,14.25,0); B.put(finial,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0xa0b4cc,i:0.32,p:2.5})));
  return g;
}

/* 秋树：树干 + 斜枝 + 锈色霜叶树冠（合批 1 mesh）——少年境全页唯一的稍暖处 */
function makeQiushu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21:o.seed), h=o.h===undefined?6.5:o.h;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.14,0.30,h,7);
  trunk.translate(0,h*0.5,0); B.put(trunk,0x0a0d13);
  for(let i=0;i<4;i++){
    const br=new THREE.CylinderGeometry(0.05,0.10,h*0.5,5);
    br.translate(0,h*0.25,0); br.rotateZ((R()-0.5)*1.5); br.rotateY(R()*6.28);
    br.translate(0,h*0.5,0); B.put(br,0x0b0e14);
  }
  const cr=h*0.34;
  for(let i=0;i<4;i++){
    const s=new THREE.SphereGeometry(cr*(0.55+0.5*R()),8,6);
    s.scale(1.25,0.85,1.25);
    s.translate((R()-0.5)*h*0.62,h+(R()-0.35)*cr*1.4,(R()-0.5)*h*0.5);
    B.put(s,R()<0.5?0x3e322c:0x2c313c);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0xa0b4cc,i:0.16,p:2.4})));
  return g;
}

/* 山道：一条微斜的暗径（两境同一条路——同景叠化；压暗不吃光，只留一道隐约的走向） */
function makeShandao(){
  const path=new THREE.Mesh(new THREE.PlaneGeometry(2.6,54),
    new THREE.MeshPhongMaterial({color:0x0a0e15,shininess:2,specular:0x0e131c}));
  path.rotation.x=-Math.PI/2; path.rotation.z=0.12; path.position.set(-3.2,0.04,-10);
  return path;
}

function bCover(){ // 封面 · 博山秋道 —— 远景层楼先在雾里立着
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:1910,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const lou=makeCenglou(); lou.scale.setScalar(0.8); lou.position.set(-10,0,-64); g.add(lou);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:1912,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:1913,sway:0.9});
  reeds.g.position.set(-13,-1.6,24); g.add(reeds.g);
  const mist=makeMist({n:10,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:64,box:[220,40,130],pos:[0,10,-40],color:0xa8b8ce,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xaebccd,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); reeds.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bShaonian(){ // 壹 · 爱上层楼 —— 少年登楼，为赋新词强说愁（稍亮稍暖）
  const g=new THREE.Group();
  const grd=makeGround({r:170,c1:0x080b11,c2:0x121722});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:22,layers:2,peaks:4,seed:1911,color:0x080b11,atmo:0x232c3c,fogK:0.62,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  g.add(makeShandao());
  /* 八角层楼（少年在其上）+ 楼头窗月微光（贴楼身前脸，作少年的背光） */
  const lou=makeCenglou(); lou.position.set(-7,0,-30); g.add(lou);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.24,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(4.2,4.2,1); win.position.set(-7,10.0,-26.9); win.renderOrder=2; g.add(win);
  /* 少年：爱上层楼，指点远方（月白袍，无胡须） */
  const boy=makeFigure({pose:'指月',robe:0x55648a,belt:0x8292ac,skin:0xd9bb9c,collar:0xc9d4e4,
    hat:'发髻',rimC:0xa0b4cc,rim:0.72,noProp:true,scale:1.42});
  boy.position.set(-6.5,7.0,-26.6); boy.rotation.y=0.55; g.add(boy);
  /* 秋树两株（锈色霜叶） */
  const tree1=makeQiushu({seed:1914,h:7}); tree1.position.set(10,0,-24); g.add(tree1);
  const tree2=makeQiushu({seed:1915,h:5.6}); tree2.position.set(-22,0,-19); g.add(tree2);
  /* 落叶 + 微尘 + 雾（水墨母题） */
  const leaves=makeLuoye({n:44,box:[54,16,26],pos:[-2,7,-16],color:0x8a5a40,speed:0.055,maxA:0.42,size:6});
  g.add(leaves.points);
  const motes=makeGlow({n:60,box:[150,24,90],pos:[0,9,-36],color:0xa8b8ce,size:5,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,22,120],pos:[0,8,-56],scale:78,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:1916,rim:0.14});
  rk.g.position.set(-15,-1.2,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:12,n:8,d:5,color:0x04060a,seed:1917,sway:0.8,tip:0x4c586c,scale:0.7});
  reeds.g.position.set(16,-2.0,12); g.add(reeds.g);
  addLights(g,{c:0xb6c2d2,i:0.55,p:[24,78,36]},{c:0x1e2532,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); leaves.update(t);
    boy.userData.update(t,k);
    win.material.opacity=k*0.24;
    rk.update(t,k); reeds.update(t,k);
  }};
}

function bErjin(){ // 贰（标志性瞬间·末境可点击）· 却道天凉 —— 欲说还休；点击层楼：今昔叠化，秋声四起
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  const grd=makeGround({r:170,c1:0x07090e,c2:0x0f131c});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:20,layers:2,peaks:4,seed:1911,color:0x070a10,atmo:0x1b2330,fogK:0.58,glowK:0.05,y:-16});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  g.add(makeShandao());
  /* 同一座层楼、同一个凭栏处（同景叠化的「景」） */
  const lou=makeCenglou(); lou.position.set(-7,0,-30); g.add(lou);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.14,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(4.2,4.2,1); win.position.set(-7,10.0,-26.9); win.renderOrder=2; g.add(win);
  win.material.userData.baseOpacity=0.21;   /* 初值=最大值：叠化时窗光可增亮 */
  /* 而今的老者：凭栏独立（幞头、蓄须，袍色转沉） */
  const old=makeFigure({pose:'独立',robe:0x2b3444,belt:0x4c5870,skin:0xc7ac8e,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0xa0b4cc,rim:0.58,noProp:true,scale:1.42});
  old.position.set(-6.5,7.0,-26.6); old.rotation.y=0.55; g.add(old);
  const oldMats=figMats(old); oldMats.forEach(function(m){ m.userData.baseOpacity=1.0; });
  /* 昔日少年的魂影（与老者同位同向）：点击后今昔叠化浮显 */
  const ghost=makeFigure({pose:'指月',robe:0x46536e,belt:0x74829c,skin:0xd9bb9c,collar:0xc9d4e4,
    hat:'发髻',rimC:0xa0b4cc,rim:0.5,noProp:true,scale:1.42});
  ghost.position.set(-6.5,7.0,-26.6); ghost.rotation.y=0.55; g.add(ghost);
  const ghostMats=figMats(ghost); ghostMats.forEach(function(m){ m.opacity=0.12; m.userData.baseOpacity=0.85; });
  /* 记忆之光：一点锈赭暖光（非金）+ 楼影晕（叠化时浮起） */
  const pl=new THREE.PointLight(0x8a5a42,0,64); pl.position.set(-6,10,-26); pl.userData.baseI=1.5; g.add(pl);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9a8a80,
    transparent:true,opacity:0.05,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(26,20,1); halo.position.set(-7,8.5,-33); halo.renderOrder=1; g.add(halo);
  halo.material.userData.baseOpacity=0.36;
  /* 一声轻叹：欲言又止，化为一缕寒雾缓缓散去（标志性瞬间——却道天凉好个秋） */
  const sighs=[];
  for(let i=0;i<2;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc9d6e8,
      transparent:true,opacity:0,depthWrite:false}));
    s.renderOrder=4; g.add(s); sighs.push(s);
    s.material.userData.baseOpacity=0.30;
  }
  /* 秋声四起（点击后）：落叶骤急 + 西风横流 + 霜晶 + 雁阵 + 落叶迸散 */
  const leaves=makeLuoye({n:34,box:[54,16,26],pos:[-2,7,-16],color:0x8a5a40,speed:0.05,maxA:0.34,size:6});
  g.add(leaves.points);
  const burst=makeBurst({n:52,color:0x8a5a40,pos:[-6,9,-27]}); g.add(burst.points);
  const wind=makeFlow({n:240,box:[150,16,70],pos:[0,9,-46],color:0x8398b4,size:26,speed:6.5,maxA:0.20});
  g.add(wind.points);
  const frost=makeGlow({n:50,box:[120,18,70],pos:[0,8,-30],color:0xc9d6e8,size:4,speed:0.06,rise:0,maxA:0.26});
  g.add(frost.points);
  const geese=makeYanzhen({n:7}); geese.g.position.set(0,44,-110); g.add(geese.g);
  geese.mesh.material.userData.baseOpacity=0.90;
  const mist=makeMist({n:6,spread:[230,22,120],pos:[0,8,-58],scale:80,color:0x7e8ea8,op:0.07});
  g.add(mist.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:1918,sway:1.6,rim:0.16});
  tree.g.position.set(14,-0.5,32); g.add(tree.g);
  const grass=makeForeground({kind:'芦苇',n:14,w:30,d:6,color:0x04060a,seed:1919,sway:1.3});
  grass.g.position.set(-15,-0.6,30); g.add(grass.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:7,color:0x04060a,seed:1920,rim:0.12});
  rk.g.position.set(9,-1.3,14); g.add(rk.g);
  addLights(g,{c:0x9db0c6,i:0.44,p:[20,70,30]},{c:0x171e2a,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/3.2);
      const rv=ctl.reveal;
      ridge.update(t,0); mist.update(t,k); wind.update(t); frost.update(t);
      leaves.update(t); burst.update(t);
      tree.update(t,k); grass.update(t,k); rk.update(t,k);
      old.userData.update(t,k); ghost.userData.update(t,k);
      /* 楼影今昔叠化：老者淡去、少年浮显，锈赭记忆之光升起 */
      oldMats.forEach(function(m){ m.opacity=k*(1.0-0.62*rv); });
      ghostMats.forEach(function(m){ m.opacity=k*(0.12+0.73*rv); });
      pl.intensity=k*1.5*rv*(0.88+0.12*Math.sin(t*1.6));
      halo.material.opacity=k*(0.05+0.31*rv);
      win.material.opacity=k*(0.10+0.11*rv);
      /* 一声轻叹化雾（欲说还休，从唇边升起） */
      for(let i=0;i<sighs.length;i++){
        const s=sighs[i], p=(t*0.21+i*0.5)%1;
        s.position.set(-6.5+p*3.2,11.8+p*2.2,-26.4+p*1.2);
        const sc=1.1+p*4.6; s.scale.set(sc,sc*0.8,1);
        s.material.opacity=k*0.30*Math.pow(Math.sin(Math.PI*p),1.4);
      }
      /* 雁阵横空 + 秋声四起 */
      geese.g.position.x=-170+((t*6.5)%340);
      geese.mesh.material.opacity=k*(0.30+0.60*rv);
      leaves.mat.uniforms.uMaxA.value=k*(0.34+0.38*rv);
      wind.mat.uniforms.uMaxA.value=k*(0.20+0.22*rv);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire();
        pluck(5,0.05,0.11); pluck(3,0.5,0.10); pluck(1,1.0,0.09); pluck(0,1.6,0.08);
        const fl=$('#flash'); fl.textContent='天凉好个秋'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x131a26),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(34,118,-190),ms:1.7,mph:0,mhaze:0.05,dirC:C(0xaebccd),dirI:0.5,
  dirP:new THREE.Vector3(-26,84,-30),ambC:C(0x1b2230),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,16,-40],lt:[0,16,-40]},
  sky:()=>SK({top:C(0x060910),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111826),fd:0.0048,star:0.45,
    ms:1.6,moon:new THREE.Vector3(26,104,-185),
    dirC:C(0xaebccd),dirI:0.44,ambC:C(0x192231),ambI:0.62}) },
{ name:'爱上层楼',dwell:17,river:0.03,build:bShaonian,
  cam:{f:[0,5.8,21],t:[0.8,5.6,18.5],lf:[-5,8.0,-27],lt:[-4.6,7.7,-28.5]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x1a2231),bot:C(0x090d13),fog:C(0x131a26),fd:0.0056,star:0.5,
    ms:1.75,mph:0,mhaze:0.04,moon:new THREE.Vector3(34,118,-190),
    dirC:C(0xb8c2ce),dirI:0.55,dirP:new THREE.Vector3(24,78,36),ambC:C(0x1e2532),ambI:0.66}) },
{ name:'却道天凉',dwell:18,river:0.02,build:bErjin,
  cam:{f:[0,5.6,21.5],t:[0.8,5.5,19],lf:[-5.2,8.0,-27.5],lt:[-4.8,7.7,-29]},
  sky:()=>SK({top:C(0x05080e),hor:C(0x131a26),bot:C(0x070a10),fog:C(0x141c29),fd:0.0068,star:0.38,
    ms:1.5,mph:0.12,mhaze:0.12,moon:new THREE.Vector3(-30,96,-200),
    dirC:C(0x93a4ba),dirI:0.44,dirP:new THREE.Vector3(20,70,30),ambC:C(0x171e2a),ambI:0.56}) },
];
"""
