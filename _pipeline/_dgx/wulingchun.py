# -*- coding: utf-8 -*-
"""wulingchun.py —— 《武陵春·风住尘香花已尽》（宋·李清照，no.189，水墨夜思）生成配置
两境（queue 分境为准，N=2）：尘香花尽（暮春庭院·妆台倦梳·落花成尘·欲语泪先流）、舴艋载愁（末境点击：
泛舟双溪——先闻「春尚好」的一丝起意（远岸一线冷青、轻舟吃水浅），点击后「只恐」跌回：轻舟吃水渐沉、
愁雾压舟、愁绪化作满江雾，春意被愁雾淹没——把愁写出重量，作全页标志性瞬间）。
全页冷银水墨，禁金；accent=#93a8c4（queue）。意象链：落花/尘香/妆台铜镜/双溪/舴艋舟/满江愁雾。"""

META = dict(
    N=2, slug='wulingchun', title='武陵春·风住尘香花已尽', dyn='宋 · 李清照', brand_author='李清照',
    gold_rgb='147,168,196',
    root=""":root{
  --gold:#93a8c4; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(147,168,196,.26);
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
        ('rgba(232,220,192', 'rgba(186,200,222', 2),
    ],
    tip='轻点画面 / 按空格 —— 泛舟双溪，看轻舟载愁渐沉',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看轻舟吃水渐沉、愁化满江雾',
    cover_read='武陵春。宋，李清照。风住尘香花已尽，日晚倦梳头。物是人非事事休，欲语泪先流。闻说双溪春尚好，也拟泛轻舟。只恐双溪舴艋舟，载不动许多愁。',
    cover_p1='两重意境，随词句次第展开：风住尘香、花已落尽的暮春，日色已高仍倦于梳头，物是人非、事事休——话未出口，泪已先流；听说双溪春光尚好，也曾拟驾一叶轻舟去寻春，却只怕那形似蚱蜢的小舟，载不动心头这许多沉重的愁。',
    cover_p2='边读词，边走进易安居士这场暮春心事：看轻舟吃水渐沉、愁绪化作满江雾——愁，在这里第一次有了重量。',
    end_h2='舟轻 · 愁重', cn_word='二',
    words_js="['再游一次，泛舟双溪','初识易安，尚需共读','渐入佳境，再诵几遍','尘香花尽，渐次懂得','深得易安词心','愁有重量，念念不忘']",
    sky_atmo='0x1c2433',
)

POEM_JS = """const POEM = [
{ name:'尘香花尽', jing:'风住尘香，花已落尽 —— 物是人非，欲语泪先流。（落花 · 妆台 · 泪）',
  segs:[
   {c:'风住尘香花已尽，', p:py('fēng zhù chén xiāng huā yǐ jìn')},
   {c:'日晚倦梳头。', p:py('rì wǎn juàn shū tóu')},
   {c:'物是人非事事休，', p:py('wù shì rén fēi shì shì xiū')},
   {c:'欲语泪先流。', p:py('yù yǔ lèi xiān liú')}],
  read:'风住尘香花已尽，日晚倦梳头。物是人非事事休，欲语泪先流。',
  yisi:'风停了，尘埃里还留着落花的余香，可是花已经全部落尽。日头已经很高，人也懒得起身梳头。眼前景物依旧，人事却已全非，一切心事都无从提起——话还没有出口，泪水先落了下来。——「事事休」三字道尽万念俱灰：不是不想说，是说了也无用；不是不梳头，是梳给谁看。',
  zhu:[['尘香','花落在尘土里，尘泥中犹带花香。风住之后，落花化作尘泥、唯余香气，写尽「花已尽」的凄凉'],
       ['日晚','日色已高、晨光迟暮。早该梳妆的时辰早已过去，仍「倦梳头」，见出意趣全无'],
       ['倦梳头','无心梳妆。女为悦己者容，良人已逝、心事无凭，梳妆还有什么意义'],
       ['物是人非','风物依然如旧，人事却已全非。此词作于李清照晚年避难金华时：丈夫赵明诚病故，金石书画散佚殆尽，国破家亡'],
       ['事事休','一切心事都完了、都提不起了。极言哀毁，万念俱灰'],
       ['欲语泪先流','想说点什么，眼泪先落了下来。泪比语快，哀伤深到无从说起']] },
{ name:'舴艋载愁', jing:'闻说双溪春尚好 —— 只恐舴艋舟，载不动许多愁。（双溪 · 轻舟 · 愁重）',
  segs:[
   {c:'闻说双溪春尚好，', p:py('wén shuō shuāng xī chūn shàng hǎo')},
   {c:'也拟泛轻舟。', p:py('yě nǐ fàn qīng zhōu')},
   {c:'只恐双溪舴艋舟，', p:py('zhǐ kǒng shuāng xī zé měng zhōu')},
   {c:'载不动许多愁。', p:py('zài bù dòng xǔ duō chóu')}],
  read:'闻说双溪春尚好，也拟泛轻舟。只恐双溪舴艋舟，载不动许多愁。',
  yisi:'听说双溪的春光还正好，也曾真的打算驾一叶轻舟去寻春散心。只怕那双溪上形似蚱蜢的小船，载不动我心头这许多沉重的愁啊。——「闻说」「也拟」「只恐」三层转折：本已心灰意懒，闻春尚好而勉强动念，动念又立刻被更深的愁压了回去。愁本无形，着一「载」字，竟有了重量。',
  zhu:[['双溪','水名，在今浙江金华，唐宋时是风景优美的游乐之地。李清照晚年避难金华时曾寓居于此'],
       ['闻说','听说。春色是「闻说」来的，自己并不曾去看——意懒心灰，见于字间'],
       ['也拟','也打算、也曾想要。拟读 nǐ。一「也」字见出迟疑勉强：本无意出游，勉强起的一丝念头'],
       ['舴艋','形似蚱蜢的小船。舴读 zé、艋读 měng。船越小越轻，越衬得愁重难载'],
       ['只恐','只怕、就怕。刚刚起的游兴，立刻被压了回去——全词最沉重的一转'],
       ['载不动许多愁','愁本无形无质，这里却让它有了分量，连轻舟都载不动。化虚为实、以轻写重，遂成千古写愁名句']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「风住尘香花已尽」的下一句是？', o:['日晚倦梳头','物是人非事事休','欲语泪先流'], a:0},
 {q:'「只恐双溪舴艋舟」的下一句是？', o:['也拟泛轻舟','闻说双溪春尚好','载不动许多愁'], a:2},
 {q:'「舴艋舟」中「舴艋」的正确读音和意思是？', o:['zhà mèng，雕饰华美的画舫','zé měng，形似蚱蜢的小船','zé míng，载货运粮的大船'], a:1},
 {q:'词中「双溪」是风景名胜之地，在今天的哪里？', o:['江苏南京','浙江杭州','浙江金华——李清照晚年避难金华时作此词'], a:2},
 {q:'「只恐双溪舴艋舟，载不动许多愁」千古传诵，妙在何处？', o:['把无形的愁写出重量：轻舟也载不动，化虚为实','夸写双溪春水暴涨、行船艰难','感叹行装沉重、出游不便'], a:0},
];
"""

SCENES_JS = """/* ================= 武陵春·风住尘香花已尽 · 两境场景（水墨夜思：冷银、落花成尘、舴艋载愁） ================= */

/* 落瓣：最后几片残花缓缓坠落（竖直下降 + 随风偏摆，Normal 混合不吃雾）——「风住尘香花已尽」 */
const LUO_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uSpeed*(0.45+0.85*fract(aSeed*7.77));
  p.y=mod(position.y-uTime*sp,uBox.y);
  p.x+=sin(uTime*0.55+aSeed*43.0)*(0.45+1.25*fract(aSeed*11.1));
  p.z+=cos(uTime*0.42+aSeed*29.0)*0.65;
  vA=smoothstep(0.0,0.7,p.y)*(0.35+0.65*fract(aSeed*13.3));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const LUO_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-0.5;
  float d=abs(q.x)*1.7+abs(q.y);
  float a=smoothstep(0.5,0.10,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLuoban(o){
  o=o||{};
  const n=o.n===undefined?46:o.n, box=o.box||[30,15,16], pos=o.pos||[0,7.5,-12];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.4:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.55:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x96686f:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.32:o.maxA}},
    vertexShader:LUO_VERT,fragmentShader:LUO_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* 愁雾压舟：无形之愁化作有形之雾——初悬江面上空，点击后整体下压、收拢、漫过船舷（uDrop 0→1） */
const CHOU_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uDrop; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float d=uDrop;
  p.y=position.y-d*uBox.y*0.80;
  p.y+=sin(uTime*0.45+aSeed*31.0)*(0.20+0.50*d);
  p.x+=sin(uTime*0.55+aSeed*43.0)*(0.40+1.70*(1.0-d));
  p.z+=cos(uTime*0.48+aSeed*17.0)*(0.40+1.30*(1.0-d));
  vA=(0.40+0.60*fract(aSeed*13.3))*(0.50+0.50*d)*smoothstep(-0.4,1.4,p.y);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const CHOU_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-0.5);
  float a=smoothstep(0.5,0.06,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeChouwu(o){
  o=o||{};
  const n=o.n===undefined?110:o.n, box=o.box||[13,9,9], pos=o.pos||[0,6.5,-24];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?7.0:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uDrop:{value:0},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x8b9cb4:o.color)},
      uFade:{value:0},uMaxA:{value:0.30}},
    vertexShader:CHOU_VERT,fragmentShader:CHOU_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* 满江愁雾：贴水一层的宽幅雾墙（boost 0→1 点击后涨起），Sprite 一片一 draw call */
function makeJiangwu(o){
  o=o||{};
  const n=o.n===undefined?7:o.n, op=o.op===undefined?0.34:o.op;
  const g=new THREE.Group(); const items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:o.color===undefined?0x8fa0ba:o.color,
      transparent:true,opacity:op,depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set((Math.random()-0.5)*(o.w===undefined?150:o.w),
      (Math.random()-0.5)*2.2,(Math.random()-0.5)*(o.d===undefined?56:o.d));
    const sc=(o.scale===undefined?34:o.scale)*(0.7+Math.random()*0.8);
    s.scale.set(sc*2.2,sc*0.62,1); s.renderOrder=5; g.add(s);
    items.push({s,op0:op,ph:Math.random()*6.28});
  }
  return {g,update(t,k,boost){ const b=boost===undefined?0:boost;
    for(let i=0;i<items.length;i++){ const it=items[i];
      it.s.material.opacity=k*b*it.op0*(0.72+0.28*Math.sin(t*0.30+it.ph));
    } }};
}

/* 妆台：案 + 立式铜镜（镜面冷光，照不见故人）+ 梳匣妆奁 —— 「日晚倦梳头」的空镜 */
function makeZhuangtai(o){
  o=o||{};
  const B=new GeoBag(), wd=0x2c2429, wd2=0x201a1e;
  const top=new THREE.BoxGeometry(3.6,0.15,1.7); top.translate(0,1.32,0); B.put(top,wd);
  const edge=new THREE.BoxGeometry(3.64,0.05,1.74); edge.translate(0,1.22,0); B.put(edge,shadeColor(wd,1.5));
  [1,-1].forEach(function(s){
    const leg=new THREE.BoxGeometry(0.22,1.22,1.3); leg.translate(s*1.55,0.61,0); B.put(leg,wd2);
  });
  const brace=new THREE.BoxGeometry(2.9,0.09,0.14); brace.translate(0,0.5,0.55); B.put(brace,wd2);
  const post=new THREE.CylinderGeometry(0.055,0.075,0.95,7); post.rotateX(-0.32);
  post.translate(0.55,1.85,-0.25); B.put(post,wd2);
  const foot=new THREE.BoxGeometry(0.5,0.09,0.5); foot.translate(0.55,1.42,-0.18); B.put(foot,wd);
  const boxx=new THREE.BoxGeometry(0.62,0.24,0.4); boxx.translate(-0.95,1.5,0.15); B.put(boxx,wd2);
  const jar=new THREE.CylinderGeometry(0.14,0.17,0.26,9); jar.translate(-0.2,1.52,0.3); B.put(jar,wd2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a465c,emissive:0x06080e}),{c:0x93a8c4,i:o.rim===undefined?0.24:o.rim,p:2.4})));
  const mir=new THREE.Mesh(new THREE.CircleGeometry(0.55,26),
    new THREE.MeshPhongMaterial({color:0x232c3a,specular:0xbcc9dd,shininess:150,emissive:0x0a1018}));
  mir.position.set(0.55,2.28,0.02); mir.rotation.x=-0.28; g.add(mir);
  const ring=new THREE.Mesh(new THREE.TorusGeometry(0.57,0.035,6,26),
    new THREE.MeshPhongMaterial({color:0x3c485c,shininess:40,specular:0x8fa4c4}));
  ring.position.copy(mir.position); ring.rotation.copy(mir.rotation); g.add(ring);
  return {g};
}

/* 舴艋舟：形似蚱蜢的浅窄小舟（弯壳船体 + 两端挑尖 + 坐板 + 竹篙），合批 1 mesh；
   吃水由 boat.position.y 控制——「载不动许多愁」的视觉支点 */
function makeZemeng(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group(), B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.60,0.34,4.3,9);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.62,1.22); B.put(hull,0x36404e);
  const bow=new THREE.ConeGeometry(0.36,1.1,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.72,1.3); bow.rotateZ(0.14); bow.translate(2.62,0.20,0); B.put(bow,0x36404e);
  const stern=new THREE.ConeGeometry(0.33,0.95,8); stern.rotateZ(Math.PI/2);
  stern.scale(1,0.72,1.3); stern.rotateZ(-0.16); stern.translate(-2.52,0.22,0); B.put(stern,0x303a46);
  const bench=new THREE.BoxGeometry(0.92,0.08,1.05); bench.translate(0.1,0.28,0); B.put(bench,0x3c4856);
  const pole=new THREE.CylinderGeometry(0.04,0.04,4.8,6);
  pole.rotateZ(Math.PI/2+0.10); pole.translate(-0.7,0.62,0.42); B.put(pole,0x44504a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a465c,emissive:0x060a10,side:THREE.DoubleSide}),{c:0x93a8c4,i:o.rim===undefined?0.55:o.rim,p:2.4})));
  g.scale.setScalar(s);
  return g;
}

function bCover(){ // 封面 · 暮春寒溪 —— 花尽尘香，一水暮色
  const g=new THREE.Group();
  const water=makeWater({size:320,seg:80,amp:0.14,freq:0.18,speed:0.36,flow:[0.1,0.36],spec:1.5,
    deep:0x0a0f18,shallow:0x16202f,skyc:0x1e2c40,moonDir:[-18,102,-184]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:17,layers:2,peaks:5,seed:1890,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-116); g.add(ridge.g);
  const luo=makeLuoban({n:34,box:[46,16,24],pos:[0,8,-22],size:2.6}); g.add(luo.points);
  const fgReedL=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:1894,sway:0.9});
  fgReedL.g.position.set(-13,-1.2,25); g.add(fgReedL.g);
  const fgRockR=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1895,rim:0.14});
  fgRockR.g.position.set(14,-1.6,28); g.add(fgRockR.g);
  const mist=makeMist({n:7,spread:[230,24,130],pos:[0,10,-54],scale:76,color:0x8fa0ba,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:56,box:[190,32,110],pos:[0,11,-42],color:0xa8b8d0,size:6.5,speed:0.05,rise:0,maxA:0.28});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.42,p:[-30,80,-40]},{c:0x18202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); luo.update(t);
    fgReedL.update(t,k); fgRockR.update(t,k);
  }};
}

function bChenxiang(){ // 一 · 尘香花尽 —— 风住尘香花已尽，日晚倦梳头；物是人非，欲语泪先流
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x080b11,c2:0x10151f});
  grd.mesh.position.y=-0.15; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:1891,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-126); g.add(ridge.g);
  /* 暮春庭院：矮院墙 + 妆台铜镜 + 倦立拢发的词人（物是人非：景在人不归） */
  const wallB=new GeoBag(), wc=0x0b0f16;
  const wl=new THREE.BoxGeometry(28,2.1,0.9); wl.translate(-2,1.05,-25); wallB.put(wl,wc);
  const cap=new THREE.BoxGeometry(28.6,0.20,1.3); cap.translate(-2,2.2,-25); wallB.put(cap,shadeColor(wc,1.5));
  [1,-1].forEach(function(s){
    const post=new THREE.BoxGeometry(1.0,2.6,1.2); post.translate(-2+s*12,1.3,-24.8); wallB.put(post,shadeColor(wc,1.15));
  });
  const wall=new THREE.Mesh(mergeGeos(wallB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x2a3446,emissive:0x04060a}),{c:0x93a8c4,i:0.16,p:2.4}));
  g.add(wall);
  const zt=makeZhuangtai(); zt.g.position.set(1.7,0,-14.8); zt.g.rotation.y=-0.38; g.add(zt.g);
  const fig=makeFigure({pose:'指月',robe:0x27334a,belt:0x50607a,skin:0xd0bda6,collar:0x9fb0c8,
    hair:0x3f4456,hat:'发髻',rimC:0x93a8c4,rim:0.60,noProp:true,scale:1.55});
  fig.position.set(-1.4,0,-11.6); fig.rotation.y=2.0; g.add(fig);
  /* 落花成尘：地上零星残瓣 + 空中最后几片落瓣 + 尘香微尘 */
  const petalB=new GeoBag();
  for(let i=0;i<26;i++){
    const pg=new THREE.CircleGeometry(0.14+Math.random()*0.16,7);
    pg.rotateX(-Math.PI/2); pg.rotateY(Math.random()*6.283);
    pg.translate((Math.random()-0.5)*24,0.03+Math.random()*0.05,-8+Math.random()*14);
    petalB.put(pg,shadeColor(0x64444e,0.75+Math.random()*0.55));
  }
  g.add(petalB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x241a1e,emissive:0x050308,side:THREE.DoubleSide})));
  const luo=makeLuoban({n:40,box:[26,15,16],pos:[0,7.5,-12]}); g.add(luo.points);
  const motes=makeGlow({n:52,box:[120,20,70],pos:[0,8,-24],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[210,20,110],pos:[0,9,-50],scale:74,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  const fgTree=makeForeground({kind:'树枝',n:2,w:10,d:5,color:0x04060a,seed:1892,sway:1.2,rim:0.15});
  fgTree.g.position.set(-19,-0.8,4); g.add(fgTree.g);
  const fgRock=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:6,color:0x04060a,seed:1893,rim:0.14});
  fgRock.g.position.set(19,-2.0,14); g.add(fgRock.g);
  addLights(g,{c:0x8fa4c4,i:0.42,p:[-26,80,-30]},{c:0x18202e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); luo.update(t);
    fgTree.update(t,k); fgRock.update(t,k);
    fig.userData.update(t,k);
  },onEnter(){ pluck(1,0.25,0.12); pluck(3,0.85,0.08); }};
}

function bZemeng(){ // 二（末境·可点击）· 舴艋载愁 —— 闻说双溪春尚好；点击：轻舟吃水渐沉，愁绪化作满江雾
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0};
  const water=makeWater({size:360,seg:88,amp:0.16,freq:0.16,speed:0.42,flow:[0.14,0.5],spec:1.7,
    deep:0x0a0f18,shallow:0x182435,skyc:0x22334a,moonDir:[42,116,-176]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:14,layers:2,peaks:4,seed:1896,color:0x070a10,atmo:0x20302c,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-124); g.add(ridge.g);
  /* 「春尚好」的一丝起意：远岸一线冷青（点击后随愁雾漫起而退去——全页唯一一处冷绿色温） */
  const springMat=new THREE.SpriteMaterial({map:glowTex(),color:0x567a67,transparent:true,opacity:0.18,
    depthWrite:false});
  const spring=new THREE.Sprite(springMat); spring.scale.set(170,30,1);
  spring.position.set(0,5,-102); spring.renderOrder=1; g.add(spring);
  /* 舴艋轻舟（吃水浅，浮得高）+ 舟上人 */
  const boat=makeZemeng({scale:1.7}); boat.position.set(0,0.18,-24); boat.rotation.y=0.32; g.add(boat);
  const fig=makeFigure({pose:'独立',robe:0x27334a,belt:0x54627e,skin:0xd0bda6,collar:0x9fb0c8,
    hair:0x3f4456,hat:'发髻',rimC:0x93a8c4,rim:0.6,noProp:true,scale:0.66});
  fig.position.set(0.1,0.34,-0.1); fig.rotation.y=0.4; boat.add(fig);
  /* 点击涟漪：吃水加深时自船身漾开 */
  const ripMat=new THREE.MeshBasicMaterial({color:0x9fb8d0,transparent:true,opacity:0.4,depthWrite:false});
  const rip=new THREE.Mesh(new THREE.RingGeometry(0.86,1.0,44),ripMat);
  rip.rotation.x=-Math.PI/2; rip.position.set(0,0.07,-24); rip.renderOrder=2; g.add(rip);
  /* 愁绪压舟：悬于江面上空的无形之雾，点击后下压收拢、漫过船舷 */
  const chou=makeChouwu({n:110,box:[13,9,9],pos:[0,6.5,-24]}); g.add(chou.points);
  /* 满江愁雾：贴水一层的宽幅雾墙（点击后涨起）+ 愁绪东流 */
  const jiang=makeJiangwu({n:9,w:150,d:56,scale:34,op:0.40,color:0x8fa0ba});
  jiang.g.position.set(0,0.6,-34); g.add(jiang.g);
  const flow=makeFlow({n:90,box:[130,10,46],pos:[0,5,-40],color:0x9fb0c8,size:20,speed:1.5,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[220,20,120],pos:[0,9,-52],scale:76,color:0x8fa0ba,op:0.065});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[150,24,80],pos:[0,9,-32],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.2});
  g.add(motes.points);
  const fgReed=makeForeground({kind:'芦苇',w:22,n:11,d:6,color:0x04060a,seed:1897,sway:0.9});
  fgReed.g.position.set(-14,-1.3,10); g.add(fgReed.g);
  const fgRock=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:5,color:0x04060a,seed:1898,rim:0.14});
  fgRock.g.position.set(18,-1.9,13); g.add(fgRock.g);
  addLights(g,{c:0x93a8c4,i:0.48,p:[34,88,-30]},{c:0x1a2232,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const el=ctl.clicked?ctl.t-ctl.clickT:0;
      const e=ease(clamp(el/4.5,0,1));            // 吃水渐沉：0.18 → -0.18，舷缘渐近水面
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      flow.update(t);
      boat.position.y=0.18-0.36*e+(ctl.clicked?0.01*Math.sin(t*0.8):0.05*Math.sin(t*0.85));
      boat.rotation.z=ctl.clicked?(0.05*e+0.008*Math.sin(t*0.66)):0.022*Math.sin(t*0.66);
      boat.rotation.x=ctl.clicked?0.030*e:0.014*Math.sin(t*0.5+1.0);
      fig.userData.update(t,k);
      rip.scale.setScalar(1+9.5*clamp(el/2.8,0,1));
      ripMat.opacity=k*0.4*Math.sin(Math.PI*clamp(el/2.8,0,1));
      const e2=ease(clamp((el-0.5)/3.2,0,1));      // 愁雾下压 + 满江雾涨起
      chou.mat.uniforms.uDrop.value=e2;
      chou.mat.uniforms.uMaxA.value=k*0.30*e2;
      chou.update(t);
      jiang.update(t,k,e2);
      flow.mat.uniforms.uMaxA.value=k*(0.10+0.15*e2);
      springMat.opacity=k*0.18*(1-e)*(0.85+0.15*Math.sin(t*0.7));
      fgReed.update(t,k); fgRock.update(t,k);
    },onEnter(){ pluck(0,0.3,0.09); pluck(3,0.9,0.06); },
    click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(0,0.05,0.12); pluck(1,0.45,0.10); pluck(2,1.0,0.08);
        const fl=$('#flash'); fl.textContent='载不动许多愁'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111825),fd:0.0055,star:0.30,
  moon:new THREE.Vector3(40,112,-180),ms:1.7,mph:0.04,mhaze:0.04,dirC:C(0x93a8c4),dirI:0.48,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x19202e),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,6.5,40],t:[0,7.0,37],lf:[0,7,-24],lt:[0,8,-28]},
  sky:()=>SK({top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x10161f),fd:0.0050,star:0.34,
    ms:1.55,mph:0.03,moon:new THREE.Vector3(-18,102,-184),
    dirC:C(0x8fa4c4),dirI:0.44,ambC:C(0x182031),ambI:0.62}) },
{ name:'尘香花尽',dwell:17,river:0.01,build:bChenxiang,
  cam:{f:[0,3.5,9],t:[0.8,3.3,6],lf:[1.2,3.0,-14],lt:[1.6,2.9,-16]},
  sky:()=>SK({top:C(0x090c14),hor:C(0x18202e),bot:C(0x090c12),fog:C(0x121926),fd:0.0058,star:0.20,
    ms:1.35,mph:0.32,mhaze:0.10,moon:new THREE.Vector3(30,96,-178),
    dirC:C(0x8fa4c4),dirI:0.40,ambC:C(0x19202e),ambI:0.62}) },
{ name:'舴艋载愁',dwell:20,river:0.05,build:bZemeng,
  cam:{f:[0,3.1,13],t:[0.6,2.9,10.5],lf:[0,2.4,-24],lt:[0.4,2.2,-27]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x171f2e),bot:C(0x090c12),fog:C(0x121926),fd:0.0060,star:0.28,
    ms:1.95,mph:0.10,mhaze:0.05,moon:new THREE.Vector3(44,116,-176),
    dirC:C(0x93a8c4),dirI:0.50,ambC:C(0x1a2232),ambI:0.60}) },
];
"""
