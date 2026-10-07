# -*- coding: utf-8 -*-
"""chunye-luocheng.py —— 《春夜洛城闻笛》（唐·李白，no.208，水墨夜思）生成配置
两境：玉笛飞声（标志性瞬间·笛声光缕自一点漫散满洛城）、折柳故园（末境可点击·笛声化作柳丝漫卷洛城）"""

META = dict(
    N=2, slug='chunye-luocheng', title='春夜洛城闻笛', dyn='唐 · 李白', brand_author='李 白',
    gold_rgb='159,176,201',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#9fb0c9; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(159,176,201,.26);
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
    tip='轻点画面 / 按空格 —— 笛声化作柳丝，漫卷洛城满城春夜',
    hint='← → 键或空格逐境游览 · 末境可点击折柳，看笛声化作柳丝漫卷洛城',
    cover_read='春夜洛城闻笛。唐，李白。谁家玉笛暗飞声，散入春风满洛城。',
    cover_p1='两重意境，随诗句次第展开：谁家玉笛在暗夜里飞出声声，散入春风、漫满洛城；此夜曲中又闻《折杨柳》，笛声化作柳丝漫卷全城，唤起何人不起的故园之情。',
    cover_p2='边读诗，边走进那个春风与笛声交织的洛城春夜，体会由一声笛牵动的满城思乡。',
    end_h2='柳色 · 故园', cn_word='两',
    words_js="['再游一次，且听笛声','初闻玉笛，尚需共读','渐入佳境，再诵几遍','诗境渐深，春夜如水','已解折柳惜别之意','满城皆是故园情']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'玉笛飞声', jing:'谁家玉笛，暗夜飞声 —— 散入春风，漫满洛城。（笛光 · 春风 · 万户）',
  segs:[
   {c:'谁家玉笛暗飞声，', p:py('shuí jiā yù dí àn fēi shēng')},
   {c:'散入春风满洛城。', p:py('sàn rù chūn fēng mǎn luò chéng')}],
  read:'谁家玉笛暗飞声，散入春风满洛城。',
  yisi:'是谁家庭院，在静夜里飞出了悠扬的玉笛声？笛声随着春风吹散，飘满了整座洛阳城。——夜深人静，一声笛偏能入人心。',
  zhu:[['洛城','即洛阳，唐代东都；李白开元年间客居洛城，夜闻笛声而作此诗'],['玉笛','精美之笛，此处指悠扬的笛声'],['暗飞声','悄悄地、不知从何处飞传来；「暗」字写出夜深笛声暗度、依稀难辨的妙处'],['满洛城','笛声随风散开，仿佛无处不至；一个「满」字，把无形之声写成了有形之景']] },
{ name:'折柳故园', jing:'折柳曲里，故园情动 —— 春夜洛城，无人不思乡。（轻点画面 · 折柳）',
  segs:[
   {c:'此夜曲中闻折柳，', p:py('cǐ yè qǔ zhōng wén zhé liǔ')},
   {c:'何人不起故园情。', p:py('hé rén bù qǐ gù yuán qíng')}],
  read:'此夜曲中闻折柳，何人不起故园情。',
  yisi:'就在这样的夜里，笛中吹起了《折杨柳》，谁能不由此生出思念故乡的深情呢？——由一己之思，写到满城同心，情味悠长。',
  zhu:[['折柳','指乐府《折杨柳》曲；「柳」谐音「留」，古人送别折柳相赠，其曲多写离愁'],['故园','故乡，家乡'],['何人不起','哪一个人能不……；以反问收束，见思乡之情的普遍与深切'],['故园情','怀念故乡之情；闻笛生情，是全诗主旨所在']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「谁家玉笛暗飞声」的下一句是？', o:['散入春风满洛城','此夜曲中闻折柳','何人不起故园情'], a:0},
 {q:'「此夜曲中闻折柳」的下一句是？', o:['散入春风满洛城','谁家玉笛暗飞声','何人不起故园情'], a:2},
 {q:'「散入春风满洛城」中「洛城」指的是？', o:['长安城，唐代的首都','洛阳城，唐代的东都','金陵城，六朝的古都'], a:1},
 {q:'「折柳」指《折杨柳》曲。古人送别折柳相赠，取意是？', o:['「柳」谐音「留」，寓惜别挽留','柳枝常青，祝愿平安长寿','柳絮入药，可解行旅之乏'], a:0},
 {q:'全诗以「何人不起故园情」收束，抒发的主要情感是？', o:['春夜游赏的闲适愉悦','对笛声音色的赞叹','由笛声触发的思乡之情'], a:2},
];
"""

SCENES_JS = """/* ================= 春夜洛城闻笛 · 两境场景（水墨夜思：玉笛飞声、折柳故园） ================= */

/* 笛声光缕（标志性瞬间）：自一点漫散、随风飘向全城的光带 —— 显式双 shader，uFade 每帧同步 */
const FLY_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const FLY_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float t=uTime*0.9;
  float x=vUv.x, y=vUv.y;
  float acc=0.0;
  for(int i=0;i<7;i++){
    float fi=float(i);
    float y0=fract(fi*0.618034)*0.72+0.06;
    float amp=0.030+0.055*fract(fi*0.381);
    float yy=y0+x*0.16+amp*sin(x*8.5-t*1.5+fi*2.399)+0.02*sin(t*0.7+fi*4.1);
    float w=0.012+0.026*x;
    acc+=smoothstep(w,0.0,abs(y-yy));
  }
  float env=smoothstep(-0.02,0.10,x)*smoothstep(1.05,0.50,x);
  float flick=0.70+0.30*sin(t*2.2+x*21.0);
  gl_FragColor=vec4(vec3(0.63,0.71,0.87), uFade*uK*acc*env*flick*0.30);
}`;
function makeFlute(o){
  o=o||{};
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.k===undefined?0.55:o.k}},
    vertexShader:FLY_VERT,fragmentShader:FLY_FRAG});
  const mesh=new THREE.Mesh(new THREE.PlaneGeometry(o.w===undefined?300:o.w,o.h===undefined?64:o.h),m);
  mesh.renderOrder=3; mesh.frustumCulled=false;
  return {mesh,mat:m,update(t,fk){ m.uniforms.uTime.value=t; m.uniforms.uFade.value=(fk===undefined?1:fk); }};
}

/* 洛城城垣：城墙 + 垛口 + 门楼（城台/二层楼/四阿顶），合批 1 mesh（剪影 + 银边光） */
function makeChengyuan(){
  const B=new GeoBag(), c1=0x0b0f16, c2=0x111826, c3=0x18202e;
  const wall=new THREE.BoxGeometry(150,7.2,4.6); wall.translate(0,3.6,0); B.put(wall,c1);
  for(let x=-72;x<=72;x+=6){
    const m=new THREE.BoxGeometry(2.6,1.15,4.8); m.translate(x,7.75,0); B.put(m,c2);
  }
  const plat=new THREE.BoxGeometry(13,2.4,7); plat.translate(0,8.4,0); B.put(plat,c2);
  const body=new THREE.BoxGeometry(9.2,4.6,5.2); body.translate(0,13.1,0); B.put(body,c3);
  const upper=new THREE.BoxGeometry(6.6,3.2,4.4); upper.translate(0,17.0,0); B.put(upper,c2);
  const roof=new THREE.ConeGeometry(6.2,2.1,4); roof.rotateY(Math.PI/4);
  roof.scale(1.28,1,1.05); roof.translate(0,19.65,0); B.put(roof,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x9fb0c9,i:0.30,p:2.5})));
  return g;
}

/* 万户屋舍：成片民居剪影（坡顶参差），合批 1 mesh */
function makeHouses(o){
  o=o||{};
  const g=new THREE.Group(), B=new GeoBag(), R=seedRnd(o.seed===undefined?5:o.seed);
  const n=o.n===undefined?12:o.n, w=o.w===undefined?100:o.w;
  const z0=o.z===undefined?-56:o.z, depth=o.depth===undefined?24:o.depth;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=z0-R()*depth;
    const bw=2.6+R()*2.6, bh=2.0+R()*1.6, bd=2.4+R()*2.0;
    const body=new THREE.BoxGeometry(bw,bh,bd); body.translate(x,bh*0.5,z); B.put(body,(i%2)?0x0a0e15:0x0c1119);
    const roof=new THREE.ConeGeometry(Math.max(bw,bd)*0.78,0.9+R()*0.7,4); roof.rotateY(Math.PI/4);
    roof.scale(1.18,1,0.92); roof.translate(x,bh+0.45+R()*0.3,z); B.put(roof,0x111725);
  }
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.20,p:2.4})));
  return {g};
}

/* 谁家玉笛：万户籍里一座小楼（暗夜吹笛处），合批 1 mesh */
function makeDilou(){
  const B=new GeoBag(), c1=0x0d1219, c2=0x131a28, c3=0x1a2332;
  const base=new THREE.BoxGeometry(5.0,1.1,4.2); base.translate(0,0.55,0); B.put(base,c1);
  const lower=new THREE.BoxGeometry(3.9,4.4,3.3); lower.translate(0,3.3,0); B.put(lower,c2);
  const upper=new THREE.BoxGeometry(3.0,3.0,2.7); upper.translate(0,7.0,0); B.put(upper,c2);
  const roof=new THREE.ConeGeometry(3.3,1.5,4); roof.rotateY(Math.PI/4);
  roof.scale(1.25,1,1.05); roof.translate(0,9.25,0); B.put(roof,c3);
  const rail=new THREE.BoxGeometry(3.4,0.14,0.14); rail.translate(0,5.45,1.55); B.put(rail,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a465c,emissive:0x06080f}),{c:0x9fb0c9,i:0.32,p:2.5})));
  return g;
}

/* 折柳：树干 + 宽扁树冠 + 一蓬下垂柳丝（TubeGeometry 沿弧线下挂），合批 1 mesh */
function makeChunliu(o){
  o=o||{};
  const g=new THREE.Group(), B=new GeoBag(), R=seedRnd(o.seed===undefined?21:o.seed);
  const n=o.n===undefined?3:o.n, spread=o.spread===undefined?12:o.spread;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, h=6.6+R()*2.2, tilt=(R()-0.5)*0.30;
    const trunk=new THREE.CylinderGeometry(0.13,0.26,h,6);
    trunk.rotateZ(tilt); trunk.translate(x,h*0.5,0); B.put(trunk,0x0a0d13);
    const tx=x-Math.sin(tilt)*h*0.9;
    for(let c=0;c<3;c++){
      const top=new THREE.SphereGeometry(1.05+R()*0.5,7,5); top.scale(2.1,0.60,1.5);
      top.translate(tx+(R()-0.5)*2.2,h+0.5+(R()-0.5)*0.8,(R()-0.5)*1.6); B.put(top,0x0c1118);
    }
    const strands=14+Math.floor(R()*7);
    for(let s=0;s<strands;s++){
      const bx=tx+(R()-0.5)*4.2, bz=(R()-0.5)*2.6, len=3.0+R()*3.2;
      const p0=new THREE.Vector3(bx,h+0.6+(R()-0.5)*0.8,bz);
      const p3=new THREE.Vector3(bx+(R()-0.5)*2.4,h+0.4-len,bz+(R()-0.5)*1.8);
      const p1=new THREE.Vector3(p0.x+(p3.x-p0.x)*0.22,p0.y-len*0.22,p0.z);
      const p2=new THREE.Vector3(p0.x+(p3.x-p0.x)*0.72,p0.y-len*0.68,p3.z);
      B.put(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([p0,p1,p2,p3]),7,0.045,4,false),0x10161f);
    }
  }
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x02040a}),{c:0x9fb0c9,i:0.30,p:2.4});
  const mesh=B.mesh(mat); g.add(mesh);
  return {g,mat};
}

/* 故园剪影：茅屋 + 树 + 篱笆（点击后显影），合批 1 mesh（透明材质随 reveal 渐显） */
function makeGuyuan(){
  const B=new GeoBag(), c1=0x0b0f16, c2=0x111722;
  const body=new THREE.BoxGeometry(5.2,2.8,4.0); body.translate(0,1.4,0); B.put(body,c1);
  const roof=new THREE.ConeGeometry(4.6,1.9,4); roof.rotateY(Math.PI/4);
  roof.scale(1.22,1,0.95); roof.translate(0,3.75,0); B.put(roof,c2);
  const tree=new THREE.CylinderGeometry(0.10,0.18,2.6,5); tree.translate(3.4,1.3,1.2); B.put(tree,0x0a0d13);
  const crown=new THREE.SphereGeometry(1.05,7,5); crown.translate(3.4,3.0,1.2); B.put(crown,0x0c1118);
  for(let i=0;i<5;i++){
    const f=new THREE.BoxGeometry(0.10,0.9,0.10); f.translate(-3.4+i*0.85,0.45,2.6); B.put(f,0x0a0e15);
  }
  const g=new THREE.Group();
  /* 初值=写入区间最大值（fadeK 铁律）：点击后渐显，由 update 每帧压回低位 */
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a,transparent:true,opacity:0.85}),{c:0x9fb0c9,i:0.30,p:2.4});
  g.add(B.mesh(mat));
  return {g,mat};
}

function bCover(){ // 封面 · 洛城春夜
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:208,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  /* 远处城垣一线剪影（洛城在望） */
  const farWall=new THREE.Mesh(new THREE.BoxGeometry(190,4.2,2.5),
    rimHook(new THREE.MeshPhongMaterial({color:0x0a0e15,shininess:6,specular:0x1d2434,emissive:0x04060a}),{c:0x8fa4c4,i:0.16,p:2.4}));
  farWall.position.set(0,0.6,-88); g.add(farWall);
  const fg=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:9,color:0x04060a,seed:209,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:9,spread:[260,34,170],pos:[0,12,-60],scale:84,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,40,130],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.34});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bFeisheng(){ // 一（标志性瞬间）· 玉笛飞声 —— 暗夜笛声化作光缕，散入春风漫满洛城
  const g=new THREE.Group();
  const grd=makeGround({r:170,c1:0x07090e,c2:0x101622});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:16,layers:2,peaks:4,seed:210,color:0x070a10,atmo:0x1f2a3d,fogK:0.62,glowK:0.06,y:-14});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 洛城：城垣门楼 + 万户屋舍（剪影两簇） */
  const wall=makeChengyuan(); wall.position.set(0,0,-46); g.add(wall);
  const housesA=makeHouses({n:16,w:118,z:-56,depth:26,seed:211}); g.add(housesA.g);
  const housesB=makeHouses({n:9,w:88,z:-53,depth:6,seed:212}); g.add(housesB.g);
  /* 谁家玉笛：城下小楼，窗内一点微光（暗） */
  const dilou=makeDilou(); dilou.position.set(-24,0,-38); g.add(dilou);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.24,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(3.4,3.4,1); win.position.set(-24,6.8,-36.4); win.renderOrder=2; g.add(win);
  /* 标志性瞬间：笛声光缕自一点漫散，随风飘过高城万户（满） */
  const flyA=makeFlute({w:150,h:58,k:0.55}); flyA.mesh.position.set(42,20,-52); g.add(flyA.mesh);
  const flyB=makeFlute({w:170,h:60,k:0.30}); flyB.mesh.position.set(40,21,-38); g.add(flyB.mesh);
  /* 闻笛人：客居洛城的诗人 */
  const fig=makeFigure({pose:'独立',robe:0x1e2a3c,belt:0x5a6a82,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0x9fb0c9,rim:0.5,noProp:true,scale:1.3});
  fig.position.set(2.5,0,10); fig.rotation.y=-2.69; g.add(fig);
  /* 城中闻笛人影 + 万户窗火（冷银） */
  const crowd=makeCrowd({n:6,rect:[8,-37,22,4],seed:213,color:0x10151f,rimC:0x8fa4c4,rim:0.20,sMin:0.38,sMax:0.52,y:0.2});
  g.add(crowd.mesh);
  const wins=makeGlow({n:90,box:[120,6,26],pos:[0,4.5,-64],color:0xbcc9dc,size:4.5,speed:0.04,rise:0,maxA:0.20});
  g.add(wins.points);
  /* 春风：横流风雾 + 微尘 */
  const wind=makeFlow({n:200,box:[140,14,50],pos:[10,10,-44],color:0x8fa0b8,size:22,speed:5,maxA:0.20});
  g.add(wind.points);
  const motes=makeGlow({n:54,box:[160,24,80],pos:[0,10,-50],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,20,110],pos:[0,8,-55],scale:75,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:214,rim:0.14});
  rk.g.position.set(-16,-1.3,16); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:215,sway:0.9});
  reeds.g.position.set(15,-1.2,14); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[-30,90,-40]},{c:0x1a2232,i:0.62});
  const pl=new THREE.PointLight(0xa9bedd,0.9,55); pl.position.set(-24,7,-37); g.add(pl);
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); wind.update(t); motes.update(t); wins.update(t);
    crowd.update(t); fig.update(t,k);
    rk.update(t,k); reeds.update(t,k);
    flyA.update(t,k); flyB.update(t,k);
    flyA.mat.uniforms.uK.value=0.55*(0.85+0.15*Math.sin(t*0.5));
    flyB.mat.uniforms.uK.value=0.30*(0.80+0.20*Math.sin(t*0.4+1.7));
    win.material.opacity=k*(0.18+0.06*Math.sin(t*0.9));
    pl.intensity=k*0.9*(0.85+0.15*Math.sin(t*1.3));
  }};
}

function bZhelu(){ // 二（末境可点击）· 折柳故园 —— 点击折柳：笛声化作柳丝，漫卷洛城，故园显影
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  const grd=makeGround({r:170,c1:0x07090e,c2:0x101622});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:14,layers:2,peaks:3,seed:216,color:0x070a10,atmo:0x1f2a3d,fogK:0.60,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 洛城夜色仍在身后 */
  const wall=makeChengyuan(); wall.position.set(0,0,-54); g.add(wall);
  const housesA=makeHouses({n:14,w:110,z:-64,depth:22,seed:217}); g.add(housesA.g);
  const wins=makeGlow({n:80,box:[110,6,20],pos:[0,4.5,-70],color:0xbcc9dc,size:4.5,speed:0.04,rise:0,maxA:0.18});
  g.add(wins.points);
  /* 折柳：城下春柳两株（柳丝下挂） */
  const willow=makeChunliu({n:1,spread:2,seed:218}); willow.g.position.set(6,0,-9); g.add(willow.g);
  const willow2=makeChunliu({n:2,spread:10,seed:219}); willow2.g.position.set(-21,0,-16); g.add(willow2.g);
  /* 闻笛人：折柳曲里，客心未眠 */
  const fig=makeFigure({pose:'独立',robe:0x1e2a3c,belt:0x5a6a82,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0x9fb0c9,rim:0.5,noProp:true,scale:1.32});
  fig.position.set(-3,0,2); fig.rotation.y=2.99; g.add(fig);
  /* 城中闻笛人影 */
  const crowd=makeCrowd({n:5,rect:[-2,-45,22,4],seed:220,color:0x10151f,rimC:0x8fa4c4,rim:0.20,sMin:0.38,sMax:0.5,y:0.2});
  g.add(crowd.mesh);
  /* 故园剪影（点击后显影）+ 窗光 */
  const gy=makeGuyuan(); gy.g.position.set(-26,0,-64); gy.g.rotation.y=0.5; g.add(gy.g);
  const gyWin=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.35,depthWrite:false,blending:THREE.AdditiveBlending}));
  gyWin.scale.set(2.6,2.6,1); gyWin.position.set(-25.2,2.1,-62.2); gyWin.renderOrder=2; g.add(gyWin);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaebfd8,
    transparent:true,opacity:0.40,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(26,16,1); halo.position.set(6,9,-10); halo.renderOrder=1; g.add(halo);
  /* 笛声柳丝光带（点击后漫卷洛城） */
  const fly=makeFlute({w:130,h:56,k:0.26}); fly.mesh.position.set(52,21,-42); g.add(fly.mesh);
  /* 春风 / 柳絮 / 微尘 / 夜雾 */
  const wind=makeFlow({n:180,box:[130,14,46],pos:[4,9,-30],color:0x8fa0b8,size:22,speed:4.6,maxA:0.18});
  g.add(wind.points);
  const catkins=makeGlow({n:60,box:[56,10,30],pos:[2,5,-8],color:0xbcc9dc,size:5,speed:0.05,rise:0.12,maxA:0.24});
  g.add(catkins.points);
  const motes=makeGlow({n:46,box:[150,22,70],pos:[0,10,-46],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.20});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[230,20,110],pos:[0,8,-58],scale:76,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:221,sway:1.4,rim:0.16});
  tree.g.position.set(16,-0.4,13); g.add(tree.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:18,d:6,color:0x04060a,seed:222,rim:0.14});
  rk.g.position.set(-15,-1.2,12); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[-40,100,-60]},{c:0x1a2232,i:0.62});
  const pl=new THREE.PointLight(0xa9bedd,0.9,60); pl.position.set(-26,6,-62); g.add(pl);
  const em0=C(0x02040a), em1=C(0x0d1a20);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/3.0);
      ridge.update(t,0); mist.update(t,k); wind.update(t); motes.update(t); catkins.update(t); wins.update(t);
      crowd.update(t); fig.update(t,k);
      tree.update(t,k); rk.update(t,k);
      fly.update(t,k);
      fly.mat.uniforms.uK.value=(0.26+0.74*ctl.reveal)*(0.85+0.15*Math.sin(t*0.5));
      willow.mat.emissive.copy(em0).lerp(em1,ctl.reveal);
      halo.material.opacity=k*(0.10+0.30*ctl.reveal);
      gy.mat.opacity=k*(0.14+0.71*ctl.reveal);
      gyWin.material.opacity=k*(0.02+0.33*ctl.reveal);
      pl.intensity=k*(0.9*ctl.reveal);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.05,0.13); pluck(4,0.5,0.11); pluck(0,1.0,0.09);
        const fl=$('#flash'); fl.textContent='故园情'; fl.classList.remove('go');
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
{ name:'玉笛飞声',dwell:16,river:0.015,build:bFeisheng,
  cam:{f:[0,7,30],t:[1.5,6.5,24],lf:[-2,9,-50],lt:[0,8,-56]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0060,star:0.5,
    ms:1.9,mph:0,mhaze:0.05,moon:new THREE.Vector3(34,118,-190),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
{ name:'折柳故园',dwell:17,river:0.015,build:bZhelu,
  cam:{f:[0,6,20],t:[1.5,5.6,15],lf:[2,7,-14],lt:[3,7,-20]},
  sky:()=>SK({top:C(0x080b12),hor:C(0x182430),bot:C(0x090d13),fog:C(0x121a27),fd:0.0065,star:0.45,
    ms:1.7,mph:0.08,mhaze:0.05,moon:new THREE.Vector3(-40,110,-200),
    dirC:C(0x9fb0c9),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
];
"""
