# -*- coding: utf-8 -*-
"""tai.py —— 《苔》（清·袁枚，no.212，宣纸留白）生成配置
两境（N=queue stages 数）：幽隅春生（白日不到处·青春恰自来）、
苔花自放（苔花如米小·也学牡丹开——末境点击「日光让位给苔米微光+牡丹形虚影」）。
宣纸留白：浅纸底、淡墨远山、大量留白；青苔灰绿只作纸上一点。
微距视角是本页最大看点：镜头低到苔藓层面，苔丘如林、苔花比人大，米粒大的花在留白里开成牡丹。
标志瞬间：大片留白里一点苔米的微光盛放。"""

META = dict(
    N=2, slug='tai', title='苔', dyn='清 · 袁枚', brand_author='袁枚',
    gold_rgb='58,68,68',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#3a4444; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(58,68,68,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(233,226,208', 1),
        ('rgba(4,6,11', 'rgba(212,202,176', 2),
        ('rgba(6,9,16', 'rgba(233,226,208', 1),
        ('rgba(3,5,9', 'rgba(236,230,214', 1),
        ('#0b101c', '#f6f1e1', 1),
        ('#6f664f', '#8a8268', 1),
        ('#5a5340', '#8d8571', 1),
        ('0x0a1526', '0xe6dfcc', 4),
    ],
    tip='轻点画面 / 按空格 —— 日光让位，苔米微光盛放',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看日光让位、苔花如牡丹般盛放',
    cover_read='苔。清，袁枚。白日不到处，青春恰自来。苔花如米小，也学牡丹开。',
    cover_p1='两重意境，随诗句次第展开：白日不到处，是苔藓幽湿的角落；青春恰自来，是无人知晓的一点新绿；苔花如米小，是郑重其事的绽放；也学牡丹开——俯身进入苔藓的丛林，看米粒大的花，开出牡丹的气象。',
    cover_p2='边读诗，边俯身走进苔藓的世界——在这里，一丛苔比你高，一朵米粒大的花，也开得像牡丹一样认真。',
    end_h2='米小 · 花开', cn_word='两',
    words_js="['再读一遍，苔花自开','初识随园，尚需共读','渐入佳境，再诵几遍','诗境渐深，幽隅生青','已解米小花放意','苔花牡丹，自信盛开']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = """const POEM = [
{ name:'幽隅春生', jing:'白日不到处 —— 幽隅无光，青意自来。（隅 · 苔 · 春）',
  segs:[
   {c:'白日不到处，', p:py('bái rì bú dào chù')},
   {c:'青春恰自来。', p:py('qīng chūn qià zì lái')}],
  read:'白日不到处，青春恰自来。',
  yisi:'太阳照不到的阴湿角落，春天的生机却自己来了——没有人播种，没有人照看，青苔依旧把这一小片幽暗，染成属于自己的春天。',
  zhu:[['白日','太阳；「白日不到处」即阳光照不到的阴湿墙隅、石缝——苔藓真实的生长环境'],['青春','古义指春天的生机、青葱的春意；今义多指青年时期——古今异义，句中即言春意，不是说人'],['恰','恰恰、恰好；「恰自来」：无人邀约，春意偏偏自己来到——一个「自」字，见其不假外求'],['苔','苔藓，阴湿处自生的低矮隐花植物，不开真正意义的花，靠孢子繁殖——「苔花」即其米粒大的孢蒴']] },
{ name:'苔花自放', jing:'苔花如米小 —— 米粒之花，亦效牡丹。（花 · 米 · 放）',
  segs:[
   {c:'苔花如米小，', p:py('tái huā rú mǐ xiǎo')},
   {c:'也学牡丹开。', p:py('yě xué mǔ dān kāi')}],
  read:'苔花如米小，也学牡丹开。',
  yisi:'苔开的花，小得只有米粒那么大；可它并不因此收敛，也像牡丹一样倾尽全力地盛放——花不择地，开不问人，微小的生命自有微小的庄严。',
  zhu:[['苔花如米小','苔花的孢蒴只有米粒大小，却是它一生郑重的「花事」'],['牡丹','花中之王，雍容盛放，古人以之象征富贵荣华——与米粒大的苔花恰成两个极端'],['也学牡丹开','一个「也」字最要紧：不自卑、不观望、不因无人喝彩而懈怠，学牡丹那倾尽全力的盛开——卑微者的自尊与自我完成'],['袁枚','（1716-1798）字子才，号简斋、随园老人，钱塘（今杭州）人，清代「性灵派」诗人——主张诗写性情，小诗亦见大生命观']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「白日不到处」的下一句是？', o:['青春恰自来','苔花如米小','也学牡丹开'], a:0},
 {q:'「苔花如米小」的下一句是？', o:['青春恰自来','白日不到处','也学牡丹开'], a:2},
 {q:'「青春恰自来」中「青春」的读音与意思是？', o:['qīng chūn，指青年时期——袁枚感叹自己青春不再','qīng chūn，指春天的生机、青葱的春意——照不到阳光的角落，春意自己来了（古今异义，不是今天说的青年）','qīng jìng，指清静幽僻——写苔藓居住的环境安安静静'], a:1},
 {q:'清代袁枚的这首小诗《苔》，近年为什么广为传唱？', o:['2018 年央视《经典咏流传》的舞台上，乡村教师梁俊带着乌蒙山的孩子把它唱成歌，打动了无数人','它是电视剧《随园故事》的主题曲，随剧集热播而走红','苏州园林把它刻在牡丹花坛边，游客争相吟诵'], a:0},
 {q:'「苔花如米小，也学牡丹开」最打动人的主旨是？', o:['感叹苔藓开不出真正的花，只能结孢子，写生命的残缺','以苔自嘲，抒发怀才不遇、无人赏识的苦闷','苔花虽只有米粒大小，也像牡丹一样倾尽全力盛放——平凡生命不待阳光眷顾的自我完成'], a:2},
];
"""

SCENES_JS = """/* ================= 苔 · 两境场景（宣纸留白：幽隅春生、苔花自放） =================
   浅纸为天、淡墨作远山，大量留白；青苔灰绿只作纸上一点。
   微距视角：镜头低到苔藓层面，苔丘如林、苔花比人大——米粒大的花在留白里开成牡丹。
   末境点击：日光让位（淡日光柱敛去）——苔米微光盛放 + 牡丹形虚影。 */

/* 淡日 makeRiPan(o) —— 白日：淡色日轮 + 一圈更淡的晕；dim∈[0,1] 让位时敛去
   （fadeK 铁律：初始 opacity=最大值，逐帧只在其下浮动且必乘 fadeK） */
function makeRiPan(o){
  o=o||{};
  const r=o.r===undefined?9:o.r;
  const discOp=o.op===undefined?0.5:o.op, hazeOp=o.haze===undefined?0.16:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xf1ead6:o.color,
    transparent:true,opacity:discOp,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0xe6dfc8:o.hazeC,
    transparent:true,opacity:hazeOp,depthWrite:false,fog:false}));
  haze.scale.set(r*6.2,r*6.2,1); g.add(haze);
  g.userData.disc=disc; g.userData.haze=haze;
  g.update=function(t,k,dim){
    const dm=dim===undefined?0:dim;
    disc.material.opacity=k*discOp*(1-0.9*dm)*(0.94+0.06*Math.sin(t*0.5));
    haze.material.opacity=k*hazeOp*(1-0.85*dm)*(0.85+0.15*Math.sin(t*0.33+1.7));
  };
  return g;
}

/* 日光柱 makeGuangZhu(o) —— 白日不到处：光柱斜落，到林梢为止、够不着苔藓（vUv.y 底部归零） */
const SHAFT_VERT=`
varying vec2 vUv;
void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const SHAFT_FRAG=`
uniform float uTime; uniform float uFade; uniform vec3 uColor; uniform float uOp;
varying vec2 vUv;
void main(){
  float a=uOp*uFade*(0.78+0.22*sin(uTime*0.55));
  a*=smoothstep(0.02,0.42,vUv.y)*(0.30+0.70*vUv.y);
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeGuangZhu(o){
  o=o||{};
  const h=o.h===undefined?13:o.h, rT=o.rT===undefined?3.4:o.rT, rB=o.rB===undefined?1.5:o.rB;
  const op=o.op===undefined?0.13:o.op;
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uFade:{value:1},uColor:{value:C(o.color===undefined?0xf2ecd2:o.color)},
      uOp:{value:op}},
    vertexShader:SHAFT_VERT,fragmentShader:SHAFT_FRAG});
  const mesh=new THREE.Mesh(new THREE.CylinderGeometry(rT,rB,h,18,1,true),m);
  mesh.renderOrder=4;
  const g=new THREE.Group(); g.add(mesh);
  g.rotation.z=o.tiltZ===undefined?0.17:o.tiltZ;   // 日自左上、柱向右下斜落
  g.update=function(t,dim){
    m.uniforms.uTime.value=t;
    m.uniforms.uOp.value=op*(1-0.9*(dim||0));
  };
  g.userData.update=g.update;
  return g;
}

/* 苔丘 makeTaiQiu(o) —— 一丛苔：垫状丘体 + 细密新梢 + 孢蒴小柱（合批 1 mesh）；fresh=嫩绿新梢（青春恰自来） */
function makeTaiQiu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?701:o.seed);
  const r=o.r===undefined?1.0:o.r;
  const fresh=!!o.fresh;
  const B=new GeoBag();
  const mound=new THREE.SphereGeometry(r,12,9);
  mound.scale(1.25,0.52+0.16*R(),1.12); mound.translate(0,r*0.22,0);
  B.put(mound,o.cushion===undefined?0x46523f:o.cushion);
  const n=o.n===undefined?30:o.n;
  for(let i=0;i<n;i++){
    const a=R()*6.283, rr=Math.sqrt(R())*r*1.05;
    const x=Math.cos(a)*rr, z=Math.sin(a)*rr;
    const hh=(0.18+0.36*R())*r*1.5;
    const tip=fresh&&R()<0.5;
    const sh=new THREE.ConeGeometry(0.035*r+0.02,hh,4);
    sh.translate(0,hh*0.5,0); sh.rotateZ((R()-0.5)*0.5); sh.rotateX((R()-0.5)*0.5);
    sh.translate(x,r*0.3,z);
    B.put(sh,tip?0x8aa866:shadeColor(0x54644a,0.9+0.35*R()));
  }
  const nc=o.capsule===undefined?8:o.capsule;
  const capH=o.capH===undefined?1.5:o.capH;   // 孢蒴杆高系数：末境压低，别高过主角花头
  for(let i=0;i<nc;i++){
    const a=R()*6.283, rr=Math.sqrt(R())*r*0.92;
    const x=Math.cos(a)*rr, z=Math.sin(a)*rr;
    const hh=(0.55+0.6*R())*r*capH;
    const st=new THREE.CylinderGeometry(0.016,0.024,hh,4);
    st.translate(0,hh*0.5,0); st.translate(x,r*0.3,z);
    B.put(st,0x6a7a52);
    const cap=new THREE.SphereGeometry(0.05*r+0.02,6,5);
    cap.scale(1,1.3,1); cap.translate(x,r*0.3+hh,z);
    B.put(cap,o.capC===undefined?0x8a9a68:o.capC);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x5a6048,emissive:0x0b0d09}),{c:0xe8e4cc,i:0.16,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.01*Math.sin(t*0.5+ph); };
  g.userData.update=g.update;
  return g;
}

/* 孢蒴林 makeBaoLin(o) —— 一片高举的孢蒴细杆：微距苔原上的「小树林」（合批 1 mesh） */
function makeBaoLin(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?721:o.seed);
  const n=o.n===undefined?14:o.n, w=o.w===undefined?10:o.w, d=o.d===undefined?4:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d;
    const hh=1.8+2.8*R();
    const st=new THREE.CylinderGeometry(0.03,0.05,hh,5);
    st.translate(0,hh*0.5,0); st.rotateZ((R()-0.5)*0.22); st.rotateX((R()-0.5)*0.18);
    st.translate(x,0,z);
    B.put(st,shadeColor(0x77875c,0.9+0.3*R()));
    const cap=new THREE.SphereGeometry(0.10+0.07*R(),7,5);
    cap.scale(1,1.35,1); cap.translate(x+hh*Math.sin(0.1)*0.5,hh,z);
    B.put(cap,R()<0.5?0x97a570:0xa4b078);
    const tipn=new THREE.ConeGeometry(0.045,0.14,5);
    tipn.translate(x+hh*Math.sin(0.1)*0.5,hh+0.16*R()+0.12,z);
    B.put(tipn,0xb2bd86);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x646a50,emissive:0x0b0d08}),{c:0xe8e4cc,i:0.18,p:2.6})));
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.006*Math.sin(t*0.7+ph); };
  g.userData.update=g.update;
  return g;
}

/* 苔花 makeTaiHua(o) —— 全诗的生命焦点：一株微距苔花，花头如收拢的牡丹蕊（合批 1 mesh + 微光晕 1 sprite） */
function makeTaiHua(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?777:o.seed);
  const h=o.h===undefined?5.6:o.h;
  const B=new GeoBag();
  const base=new THREE.SphereGeometry(0.55,10,7);
  base.scale(1.25,0.4,1.1); base.translate(0,0.12,0);
  B.put(base,0x4c5a42);
  const stem=new THREE.CylinderGeometry(0.05,0.085,h*0.92,6);
  stem.translate(0,h*0.46,0);
  B.put(stem,0x5d6c4c);
  for(let i=0;i<4;i++){
    const lf=new THREE.SphereGeometry(0.17,5,4);
    lf.scale(1.8,0.2,0.75);
    lf.rotateZ(0.45+R()*0.5);
    const a=R()*6.283; lf.rotateY(a);
    lf.translate(Math.cos(a)*0.12,h*(0.16+0.5*R()),Math.sin(a)*0.12);
    B.put(lf,0x57664a);
  }
  const rings=[[9,0.44,0.20,-0.16,0xbfc79a],[7,0.31,0.15,0.42,0xcdd5ac],[5,0.19,0.10,0.72,0xdde3c0]];
  for(let r=0;r<rings.length;r++){
    const rg=rings[r];
    for(let k=0;k<rg[0];k++){
      const a=k/rg[0]*6.283+r*0.45+(R()-0.5)*0.3;
      const pt=new THREE.SphereGeometry(rg[2],7,5);
      pt.scale(1.5,0.55,1.0);
      pt.translate(rg[1],0,0);
      pt.rotateZ(rg[3]);
      pt.rotateY(a);
      pt.translate(0,h,0);
      B.put(pt,rg[4]);
    }
  }
  const heart=new THREE.SphereGeometry(0.13,8,6);
  heart.scale(1,0.9,1); heart.translate(0,h+0.06,0);
  B.put(heart,0xaeb986);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x707a5c,emissive:0x0d0f0a}),{c:0xecebd6,i:0.26,p:2.4})));
  const glowOp=o.glow===undefined?0.62:o.glow;   // 初值=最大值：点击后常态 0.32、盛放 0.62
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd6e0a8,
    transparent:true,opacity:glowOp,depthWrite:false}));
  glow.scale.set(3.2,3.2,1); glow.position.set(0,h,0); glow.renderOrder=4; g.add(glow);
  g.userData.glowMat=glow.material;
  g.scale.setScalar(o.scale===undefined?1.9:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){
    g.rotation.z=0.018*Math.sin(t*0.7+ph);
    glow.material.opacity=k*0.32*(0.82+0.18*Math.sin(t*1.1+ph));   // 基态；bZifang 每帧按 bloom 覆写
  };
  g.userData.update=g.update;
  return g;
}

/* 牡丹形虚影 makeMudanXu(o) —— 末境点击后盛放：淡彩牡丹轮廓，平面朝镜头（合批 1 mesh，透明 0.30=初值最大） */
function makeMudanXu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?888:o.seed);
  const B=new GeoBag();
  const rings=[[12,2.55,0.66,0xc9cfae],[9,1.85,0.58,0xd8ddc0],[6,1.15,0.48,0xe6ead0]];
  for(let r=0;r<rings.length;r++){
    const rg=rings[r];
    for(let k=0;k<rg[0];k++){
      const a=k/rg[0]*6.283+r*0.42+(R()-0.5)*0.24;
      const pt=new THREE.SphereGeometry(rg[2],8,6);
      pt.scale(1.45,1.0,0.2);
      pt.translate(rg[1],0,0);
      pt.rotateZ(a);
      B.put(pt,rg[3]);
    }
  }
  const dome=new THREE.SphereGeometry(0.55,10,8);
  dome.scale(1,1,0.5);
  B.put(dome,0xf0eed8);
  const mat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,transparent:true,opacity:0.30,
    depthWrite:false,side:THREE.DoubleSide,shininess:8,specular:0x6a7060,emissive:0x101208});
  const mesh=B.mesh(mat); mesh.renderOrder=3;
  const g=new THREE.Group(); g.add(mesh);
  g.userData.mat=mat;
  g.scale.setScalar(0.22);
  return g;
}

/* 苔米微光爆 makeTaiMi(o) —— 点击触发（uT0 激活）：苔花头上升起一片微光米粒 */
const TAIMI_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uT0;
varying float vA;
void main(){
  float age=uTime-uT0;
  vec3 p=position; float a=0.0;
  if(age>0.0&&age<10.0){
    float k=age/10.0;
    float sw=aSeed*6.283;
    p.y+=k*6.0+sin(uTime*1.1+sw)*(0.35+k*1.2);
    p.x+=(aSeed-0.5)*k*6.0+sin(uTime*0.8+sw)*(0.3+k*1.3);
    p.z+=(fract(aSeed*7.31)-0.5)*k*6.0+cos(uTime*0.7+sw*1.7)*(0.3+k*1.2);
    a=(1.0-k)*smoothstep(0.0,0.04,age);
  }
  vA=a;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const TAIMI_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.12,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeTaiMi(o){
  o=o||{};
  const n=o.n===undefined?110:o.n, src=o.src||[1.3,4.1,-6.3];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=src[0]+(Math.random()-0.5)*0.8;
    P[i*3+1]=src[1]+(Math.random()-0.5)*0.7;
    P[i*3+2]=src[2]+(Math.random()-0.5)*0.8;
    S[i]=Math.random(); Z[i]=2.0+Math.random()*2.2;
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  /* 浅纸底上用 NormalBlending：additive 会把微光洗成白棉团；灰绿苔米微光才是本诗的点 */
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uT0:{value:-999},uColor:{value:C(0xc3cf8e)},uFade:{value:1},
      uMaxA:{value:o.maxA===undefined?0.62:o.maxA}},
    vertexShader:TAIMI_VERT,fragmentShader:TAIMI_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  const grp=new THREE.Group(); grp.add(points);
  let lastT=0;
  grp.update=function(t){ lastT=t; m.uniforms.uTime.value=t; };
  grp.fire=function(){ m.uniforms.uT0.value=lastT; };
  return {g:grp,update:grp.update,fire:grp.fire};
}

function bCover(){ // 卷首 · 宣纸苔原远望：淡墨远山下，苔丘如林的天际线
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d0,c2:0xc6cbab,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:56,layers:3,peaks:6,seed:711,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-96); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:180,h:24,layers:2,peaks:4,seed:712,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-6,order:-5});
  ridge2.g.position.set(-6,0,-50); ridge2.g.rotation.y=Math.PI*1.03; g.add(ridge2.g);
  /* 苔丘如林的天际线（微距世界：一丛苔高过人） */
  [[-16,3.8,-26],[-8,4.6,-30],[1,5.4,-33],[9,4.2,-28],[17,3.4,-24],[-2,2.6,-22]].forEach(function(p,i){
    const q=makeTaiQiu({seed:715+i,scale:p[1]});
    q.position.set(p[0],-1.5,p[2]); g.add(q);
  });
  const sun=makeRiPan({r:8.5,op:0.42});
  sun.position.set(-44,46,-88); g.add(sun);
  const mist=makeMist({n:8,spread:[260,26,140],pos:[0,9,-58],scale:80,color:0xe2dbc6,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[200,26,120],pos:[0,10,-34],color:0xb4bc9e,size:4,speed:0.04,
    rise:0.06,add:false,maxA:0.2});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:7,color:0x23262b,seed:717,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(15,-1.9,15); g.add(rk.g);
  addLights(g,{c:0xd9d4c4,i:0.44,p:[-50,110,30]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t);
    sun.update(t,k,0); rk.update(t,k);
    g.children.forEach(function(c){ if(c.userData.update&&c!==sun&&c!==rk)c.userData.update(t,k); });
  }};
}

function bYouyu(){ // 一 · 幽隅春生 —— 白日不到处，青春恰自来：光柱到不了、新绿自己来
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0xe8e2ce,c2:0xc3c9a8,y:-1.5}); g.add(grd.mesh);
  /* 背景：淡墨远山两层 */
  const ridge=makeRange({r:270,h:62,layers:3,peaks:6,seed:731,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:175,h:28,layers:2,peaks:5,seed:732,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-5,order:-5});
  ridge2.g.position.set(-10,0,-40); ridge2.g.rotation.y=Math.PI*1.04; g.add(ridge2.g);
  /* 白日不到处：左上淡日 + 光柱斜落、到林梢为止 */
  const sun=makeRiPan({r:8.5,op:0.42});
  sun.position.set(-40,44,-84); g.add(sun);
  const shaft=makeGuangZhu({h:13,rT:3.4,rB:1.5,op:0.13});
  shaft.position.set(-8,6.8,-12); g.add(shaft);
  /* 苔丘如林（微距世界）+ 一丛嫩绿新梢（青春恰自来——生命焦点） */
  [[-9,2.6,-10],[-5,3.4,-14],[-12,3.0,-17],[2,2.8,-16],[5,2.2,-11],[-2,1.8,-8.5]].forEach(function(p,i){
    const q=makeTaiQiu({seed:735+i,scale:p[1]});
    q.position.set(p[0],-1.5,p[2]); g.add(q);
  });
  const young=makeTaiQiu({seed:742,scale:2.6,fresh:true,capsule:4});
  young.position.set(-1.6,-1.5,-6.8); g.add(young);
  const grove=makeBaoLin({seed:743,n:12,w:9,d:4});
  grove.position.set(-7,-1.5,-13); g.add(grove);
  /* 青意微尘 + 贴地幽凉雾 */
  const motes=makeGlow({n:46,box:[26,10,26],pos:[-3,3,-11],color:0x9fb489,size:3.5,speed:0.05,
    rise:0.1,add:false,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[180,8,80],pos:[0,0.8,-28],scale:56,color:0xdad6c2,op:0.10});
  g.add(mist.g);
  /* 前景：左上岩壁压暗成荫（芦苇近景会糊成黑碎片，本页一律不用近景芦苇） */
  const cliff=makeForeground({kind:'岩壁',n:3,r:3.6,w:14,d:6,color:0x23262b,seed:744,rim:0.12,rimC:0xf0ead8});
  cliff.g.position.set(-15,3.2,5); g.add(cliff.g);
  addLights(g,{c:0xd8d4c0,i:0.34,p:[-40,100,20]},{c:0xd4d8c6,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0);
    sun.update(t,k,0); shaft.update(t,0);
    mist.update(t,k); motes.update(t);
    cliff.update(t,k); grove.update(t);
    g.children.forEach(function(c){ if(c.userData.update&&c!==sun&&c!==shaft&&c!==cliff)c.userData.update(t,k); });
  }};
}

function bZifang(){ // 二（末境·可点击）· 苔花自放 —— 苔花如米小，也学牡丹开；点击：日光让位，苔米微光盛放+牡丹形虚影
  const g=new THREE.Group();
  const ctl={t:0,last:-9,clicked:false,blooming:false,bloom:0,dim:0};
  const grd=makeGround({r:250,c1:0xe9e2cf,c2:0xc5cbaa,y:-1.5}); g.add(grd.mesh);
  /* 背景：淡墨远山两层 */
  const ridge=makeRange({r:270,h:64,layers:3,peaks:6,seed:751,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.045,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:175,h:28,layers:2,peaks:4,seed:752,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-5,order:-5});
  ridge2.g.position.set(6,0,-40); ridge2.g.rotation.y=Math.PI*1.02; g.add(ridge2.g);
  /* 白日仍在左上（点击后让位） */
  const sun=makeRiPan({r:8,op:0.38});
  sun.position.set(-36,42,-80); g.add(sun);
  const shaft=makeGuangZhu({h:12,rT:3.0,rB:1.3,op:0.10});
  shaft.position.set(-9,6.4,-13); g.add(shaft);
  /* 标志主体：一株微距苔花（花头即牡丹蕊，株高过丘），身后牡丹形虚影收拢待放
     （scale 1.4 + y -3.74：花头锚定在 y=4.1，与苔米微光爆源、牡丹虚影同一轴心） */
  const hero=makeTaiHua({seed:755,h:5.6,scale:1.4});
  hero.position.set(1.3,-3.74,-6.3); g.add(hero);
  const mudan=makeMudanXu({seed:756});
  mudan.position.set(1.3,4.1,-7.1); g.add(mudan);
  const mdMat=mudan.userData.mat;
  /* 苔丘疏林 + 孢蒴小树林（微距苔原，留白处只疏疏几点——杆丛压低收窄，让位给花） */
  [[-2.5,3.0,-8],[4.2,3.6,-10],[-5,4.2,-13],[7,4.6,-16],[-8,2.4,-9],[2.8,2.8,-12.5]].forEach(function(p,i){
    const q=makeTaiQiu({seed:760+i,scale:p[1],capsule:3,capH:0.7,n:20});
    q.position.set(p[0],-1.5,p[2]); g.add(q);
  });
  const grove1=makeBaoLin({seed:767,n:6,w:4.5,d:3});
  grove1.position.set(4.5,-1.5,-9.5); g.add(grove1);
  const grove2=makeBaoLin({seed:768,n:7,w:5.5,d:3.4});
  grove2.position.set(-5.5,-1.5,-12); g.add(grove2);
  /* 点击触发：苔米微光自花头升起 */
  const burst=makeTaiMi({n:150,src:[1.3,4.1,-6.3]}); g.add(burst.g);
  /* 青意微尘 + 雾 */
  const motes=makeGlow({n:44,box:[30,10,28],pos:[0.5,3,-10],color:0xc0c8a4,size:3.2,speed:0.05,
    rise:0.09,add:false,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[220,22,120],pos:[0,8,-58],scale:74,color:0xe0d8c2,op:0.10});
  g.add(mist.g);
  /* 前景：近处苔丘两丛压住画缘（纯丘体不加杆，杆会在镜头前糊成巨球）+ 左缘坡石 */
  [[-2.8,3.2,4.2],[3.0,3.0,3.2]].forEach(function(p,i){
    const q=makeTaiQiu({seed:771+i,scale:p[1],capsule:0,n:12});
    q.position.set(p[0],-1.5,p[2]); g.add(q);
  });
  const rk=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:5,color:0x23262b,seed:769,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(-8,-1.5,3.0); g.add(rk.g);
  addLights(g,{c:0xd8d4c0,i:0.38,p:[-40,95,20]},{c:0xd4d8c6,i:0.6});
  const glowMat=hero.userData.glowMat;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.blooming){
        ctl.bloom=Math.min(1,ctl.bloom+dt/4.2);
        ctl.dim=Math.min(1,ctl.dim+dt/2.2);
      }
      const bloom=ctl.bloom, dim=ctl.dim;
      ridge.update(t,0); ridge2.update(t,0);
      sun.update(t,k,dim); shaft.update(t,dim);
      mist.update(t,k); motes.update(t); burst.update(t);
      rk.update(t,k);
      grove1.update(t); grove2.update(t);
      g.children.forEach(function(c){ if(c.userData.update&&c!==sun&&c!==shaft&&c!==rk)c.userData.update(t,k); });
      /* 牡丹虚影：随 bloom 盛放（opacity 每帧写必乘 fadeK，峰值 0.30=初值） */
      const e=1-Math.pow(1-bloom,3);
      mdMat.opacity=k*0.30*bloom*(0.85+0.15*Math.sin(t*1.3));
      mudan.scale.setScalar(0.22+0.85*e);
      mudan.rotation.z=bloom*t*0.12;
      /* 微光晕：点击后更盛（峰值 0.62=初值） */
      glowMat.opacity=k*(0.32+0.30*bloom)*(0.82+0.18*Math.sin(t*1.1));
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.5)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      ctl.blooming=true;
      burst.fire();
      pluck(2,0.0,0.12); pluck(4,0.5,0.10); pluck(1,1.0,0.09); pluck(3,1.5,0.08);
      const fl=$('#flash'); fl.textContent='苔花如米小 也学牡丹开';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.44,
  dirP:new THREE.Vector3(-50,110,30),ambC:C(0xd6d8c6),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.5,62],t:[0,7,54],lf:[0,7,-28],lt:[1.5,7.5,-34]},
  sky:()=>SK({fd:0.0046,star:0.03,dirI:0.44}) },
{ name:'幽隅春生',dwell:16,river:0.02,build:bYouyu,
  cam:{f:[2.0,4.0,20],t:[-0.5,4.3,15],lf:[-0.5,4.6,-6],lt:[1.5,4.3,-11]},
  sky:()=>SK({fd:0.0056,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.34,dirP:new THREE.Vector3(-45,105,20),ambC:C(0xd4d8c6),ambI:0.62}) },
{ name:'苔花自放',dwell:19,river:0.02,build:bZifang,
  cam:{f:[0.6,3.2,8.5],t:[-0.2,3.6,6.8],lf:[0.8,4.0,-5.2],lt:[1.2,4.2,-6.2]},
  sky:()=>SK({fd:0.0070,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.38,dirP:new THREE.Vector3(-40,100,20),ambC:C(0xd4d8c6),ambI:0.6}) },
];
"""
