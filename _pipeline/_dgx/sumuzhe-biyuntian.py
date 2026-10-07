# -*- coding: utf-8 -*-
"""sumuzhe-biyuntian.py —— 《苏幕遮·碧云天》（宋·范仲淹，no.163，水墨夜思）生成配置
三境（N=queue stages 数）：碧天黄叶（秋色连波·寒烟翠）、
斜阳芳草（山映斜阳天接水·标志性瞬间「芳草更在斜阳外」）、
月夜愁肠（明月楼高·末境点击：斜光铺水+芳草蔓出画外）。
冷银水墨：月是唯一主角；黄叶枯金、寒烟空翠、斜阳锈赭是全页仅有的三处低饱和色彩层次，禁金。
情感曲线「秋阔→魂黯→泪酒」，色温自秋高气爽的清冷渐入深夜的沉冷。"""

META = dict(
    N=3, slug='sumuzhe-biyuntian', title='苏幕遮·碧云天', dyn='宋 · 范仲淹', brand_author='范 仲 淹',
    gold_rgb='176,188,205',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b0bccd; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(176,188,205,.26);
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
    tip='轻点画面 / 按空格 —— 斜光铺水，芳草蔓出画外',
    hint='← → 键或空格逐境游览 · 末境可点击斜阳芳草，看斜光铺水、芳草蔓出画外',
    cover_read='苏幕遮·碧云天。宋，范仲淹。碧云天，黄叶地。秋色连波，波上寒烟翠。',
    cover_p1='三重意境，随词句次第展开：碧云黄叶、秋色连波的澄江秋望；山映斜阳、芳草无情的天涯远眺；夜夜好梦难留，明月楼头休独倚，酒入愁肠，尽化作相思之泪。',
    cover_p2='边读词，边走进水阔天长的秋色与斜阳外的乡愁——秋阔、魂黯、泪酒。',
    end_h2='酒入愁肠 · 相思成泪', cn_word='三',
    words_js="['再游一次，且看碧云','初识秋阔，尚需共读','渐入佳境，再诵几遍','词境渐深，斜阳芳草','已解黯然销魂之意','泪洒楼头，乡思无尽']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'碧天黄叶', jing:'碧云高天，黄叶满地 —— 秋色与秋波相接，波上寒烟一片空翠。（天 · 叶 · 波 · 烟）',
  segs:[
   {c:'碧云天，', p:py('bì yún tiān')},
   {c:'黄叶地。', p:py('huáng yè dì')},
   {c:'秋色连波，', p:py('qiū sè lián bō')},
   {c:'波上寒烟翠。', p:py('bō shàng hán yān cuì')}],
  read:'碧云天，黄叶地。秋色连波，波上寒烟翠。',
  yisi:'碧云高天，黄叶铺满大地；秋色绵延不绝，与江水相连，波上笼罩着一层带着寒意的烟雾，一片空翠。——起笔天对地、云对叶，一笔便把秋写得又高又阔，秋色一直漫到水天相接之处。',
  zhu:[['碧云天','碧蓝天宇与高远云霞；与「黄叶地」对起，天地相对，写尽秋色之高远澄澈'],['黄叶地','黄叶铺地，深秋水面与岸上的光景'],['秋色连波','秋色随江水绵延起伏，天光水色连成一片'],['寒烟','江上清寒的水雾；秋水气冷，故曰寒'],['翠','苍翠、空明之绿；寒烟带秋水之色，故曰翠——冷而不衰，正是此词秋色的底子']] },
{ name:'斜阳芳草', jing:'山映斜阳，天水相接 —— 芳草无情，一直蔓到斜阳之外、望不见的家乡。（斜阳 · 芳草 · 天涯）',
  segs:[
   {c:'山映斜阳天接水，', p:py('shān yìng xié yáng tiān jiē shuǐ')},
   {c:'芳草无情，', p:py('fāng cǎo wú qíng')},
   {c:'更在斜阳外。', p:py('gèng zài xié yáng wài')},
   {c:'黯乡魂，', p:py('àn xiāng hún')},
   {c:'追旅思。', p:py('zhuī lǚ sì')}],
  read:'山映斜阳天接水，芳草无情，更在斜阳外。黯乡魂，追旅思。',
  yisi:'夕阳映着远山，天水相接；芳草全不解人的愁绪，只顾一直铺展到斜阳之外——比极目所能望见的更远，那里才是家乡。思乡之情使人黯然销魂，羁旅的愁绪缠绕不休，摆脱不开。——以芳草的绵延无尽，写乡愁的望不到头。',
  zhu:[['山映斜阳','斜阳映照山峦，山影带着余晖没入天水相接之处'],['芳草无情','芳草绵延到天涯，如离恨一样没有尽头，却全不顾人的愁情，故曰无情'],['更在斜阳外','比斜阳还要遥远；斜阳已是极目所尽，故乡更在其外——望乡而不见乡的极致写法'],['黯乡魂','因思念故乡而黯然销魂；语出江淹《别赋》「黯然销魂者，唯别而已矣」'],['追旅思','羁旅愁思萦绕心头、追随不去；思，心绪、情思（读 sì）']] },
{ name:'月夜愁肠', jing:'明月高楼不可独倚 —— 酒入愁肠，都化作相思泪。（月 · 楼 · 酒 · 泪）',
  segs:[
   {c:'夜夜除非，', p:py('yè yè chú fēi')},
   {c:'好梦留人睡。', p:py('hǎo mèng liú rén shuì')},
   {c:'明月楼高休独倚，', p:py('míng yuè lóu gāo xiū dú yǐ')},
   {c:'酒入愁肠，', p:py('jiǔ rù chóu cháng')},
   {c:'化作相思泪。', p:py('huà zuò xiāng sī lèi')}],
  read:'夜夜除非，好梦留人睡。明月楼高休独倚，酒入愁肠，化作相思泪。',
  yisi:'每天夜里，除非做上好梦，才能得片刻安睡——其实是愁思之深，连好梦也难成。不要在明月之夜独自登上高楼凭栏远望：月愈明，望愈远，愁愈深。借酒浇愁吧，酒一入愁肠，全都化作了相思的眼泪。——楼头、月下、酒中、泪里，四层递进，把乡愁写到无可排遣。',
  zhu:[['除非，好梦留人睡','除非夜夜有好梦，才能安然入睡；反言其意：正是好梦难成，愁思才夜夜相缠'],['休独倚','不要独自凭倚高楼栏杆；月明愈亮，望乡愈远，独自看月愁愈重'],['酒入愁肠','借酒浇愁，愁不曾减，反随酒入肠'],['相思泪','酒入愁肠都化作了泪水——酒与泪在肠中互化，写尽乡愁无从排遣']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「碧云天，黄叶地」的下一句是？', o:['秋色连波，波上寒烟翠','山映斜阳天接水','明月楼高休独倚'], a:0},
 {q:'「黯乡魂，追旅思」的下一句是？', o:['酒入愁肠，化作相思泪','夜夜除非，好梦留人睡','碧云天，黄叶地'], a:1},
 {q:'「追旅思」中「思」的正确读音与意思是？', o:['sī，思念','shī，诗意','sì，心绪、情思'], a:2},
 {q:'「黯乡魂」暗用了江淹《别赋》中的哪一句？', o:['黯然销魂者，唯别而已矣','采菊东篱下，悠然见南山','昔我往矣，杨柳依依'], a:0},
 {q:'全词借秋景抒发的核心情感是？', o:['秋日登高的畅快','羁旅思乡、黯然销魂的愁绪','重逢故人的欣喜'], a:1},
];
"""

SCENES_JS = """/* ================= 苏幕遮·碧云天 · 三境场景（水墨夜思：碧天黄叶、斜阳芳草、月夜愁肠） =================
   冷银水墨：月是唯一主角；黄叶枯金、寒烟空翠、斜阳锈赭是全页仅有的三处低饱和色彩层次，禁金。 */

/* 黄叶树：干 + 枝 + 低饱和枯黄树冠（合批 1 mesh；枯叶取暗橄榄，不取亮金） */
function makeHuangye(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1631:o.seed);
  const h=o.h===undefined?6.0:o.h;
  const B=new GeoBag();
  const t1=new THREE.CylinderGeometry(0.10,0.24,h*0.56,7);
  t1.translate(0,h*0.28,0); t1.rotateZ((R()-0.5)*0.12); B.put(t1,0x0a0d12);
  const t2=new THREE.CylinderGeometry(0.06,0.12,h*0.5,6);
  t2.translate(0.22,h*0.55+h*0.24,0); t2.rotateZ(-0.12+(R()-0.5)*0.18); B.put(t2,0x0b0e14);
  const nb=3+Math.floor(R()*3);
  for(let i=0;i<nb;i++){
    const a=R()*6.283,len=1.6+R()*2.2;
    const br=new THREE.CylinderGeometry(0.026,0.06,len,5);
    br.translate(0,len*0.5,0); br.rotateZ(0.5+R()*0.5); br.rotateY(a);
    br.translate((R()-0.5)*0.6,h*(0.58+R()*0.34),(R()-0.5)*0.6);
    B.put(br,0x0b0e14);
  }
  const nc=4+Math.floor(R()*4), cCol=[0x3d3a20,0x494424,0x544e2a,0x5f5730];
  for(let i=0;i<nc;i++){
    const a=R()*6.283,rr=0.5+R()*2.8;
    const cl=new THREE.SphereGeometry(0.55+R()*0.85,7,5);
    cl.scale(1.5,0.72,1.4);
    cl.translate(Math.sin(a)*rr+(R()-0.5)*0.9,h*(0.62+R()*0.36),Math.cos(a)*rr*0.8+(R()-0.5)*0.8);
    B.put(cl,cCol[Math.floor(R()*cCol.length)]);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x333a30,emissive:0x04060a}),{c:0x948f6a,i:0.24,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 斜光铺水：斜阳在水面铺出的一道锈赭光路（additive 光体，不进 fogShaders——吃雾会洗灰） */
const XG_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const XG_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float across=smoothstep(0.0,0.30,vUv.x)*smoothstep(1.0,0.60,vUv.x);
  float along=pow(clamp(vUv.y,0.0,1.0),1.25);
  float shim=0.80+0.20*sin(uTime*0.9+vUv.y*24.0);
  float spk=0.92+0.08*sin(uTime*1.8+vUv.x*46.0);
  vec3 col=mix(vec3(0.24,0.18,0.19),vec3(0.66,0.41,0.28),clamp(vUv.y*1.2,0.0,1.0));
  gl_FragColor=vec4(col,uFade*uK*across*along*shim*spk);
}`;
function makeXieguang(o){
  o=o||{};
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.k0===undefined?0.5:o.k0}},
    vertexShader:XG_VERT,fragmentShader:XG_FRAG});
  const geo=new THREE.PlaneGeometry(o.w===undefined?26:o.w,o.len===undefined?110:o.len);
  geo.rotateX(-Math.PI/2);
  const mesh=new THREE.Mesh(geo,m);
  mesh.position.set(o.x===undefined?13:o.x,o.y===undefined?0.18:o.y,o.z===undefined?-92:o.z);
  mesh.rotation.y=o.rot===undefined?-0.15:o.rot;
  mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t,k){ m.uniforms.uTime.value=t; if(k!==undefined)m.uniforms.uFade.value=k; };
  return {g,mesh,mat:m,update:g.update};
}

/* 芳草蔓生：合批草叶（aBase/aRank/aPhase/aTip），uSpread 0→1 让芳草沿 rank 依次立起、蔓出画外；
   自定义雾同步（进 fogShaders） */
const CAO_VERT=`
attribute vec3 aBase; attribute float aRank; attribute float aPhase; attribute float aTip;
uniform float uTime; uniform float uSpread;
varying float vTip; varying vec3 vW;
void main(){
  float gr=smoothstep(aRank,aRank+0.14,uSpread);
  vec3 p=aBase+(position-aBase)*gr;
  p.x+=sin(uTime*1.2+aPhase)*0.34*aTip*aTip*gr;
  p.z+=cos(uTime*0.8+aPhase*1.7)*0.20*aTip*aTip*gr;
  vec4 wp=modelMatrix*vec4(p,1.0); vW=wp.xyz; vTip=aTip;
  gl_Position=projectionMatrix*viewMatrix*wp;
}`;
const CAO_FRAG=`
uniform vec3 uCBase; uniform vec3 uCTip; uniform vec3 uFogColor; uniform float uFogDensity; uniform float uFade;
varying float vTip; varying vec3 vW;
void main(){
  vec3 col=mix(uCBase,uCTip,pow(clamp(vTip,0.0,1.0),1.5));
  float d=length(cameraPosition-vW);
  float f=1.0-exp(-uFogDensity*uFogDensity*d*d);
  col=mix(col,uFogColor,clamp(f,0.0,1.0));
  gl_FragColor=vec4(col,uFade);
}`;
function makeFangcao(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1640:o.seed);
  const n=o.n===undefined?760:o.n, z0=o.z0===undefined?9:o.z0, z1=o.z1===undefined?-80:o.z1;
  const pos=[],base=[],rank=[],phase=[],tip=[],idx=[];
  let vi=0;
  for(let i=0;i<n;i++){
    const rk=Math.pow(R(),1.2);
    const z=z0+(z1-z0)*rk;
    const x=(R()-0.5)*2*(4.5+30.0*rk);
    const hgt=0.55+R()*1.0, ph=R()*6.283, rot=R()*3.14;
    const bl=new THREE.PlaneGeometry(0.13,hgt,1,2);
    bl.translate(0,hgt*0.5,0);
    bl.rotateZ((R()-0.5)*0.5); bl.rotateY(rot);
    const pa=bl.attributes.position;
    for(let v=0;v<pa.count;v++){
      pos.push(pa.getX(v)+x,pa.getY(v),pa.getZ(v)+z);
      base.push(x,0,z);
      rank.push(rk); phase.push(ph);
      tip.push(Math.max(0,Math.min(1,pa.getY(v)/hgt)));
    }
    const ia=bl.index.array;
    for(let kk=0;kk<ia.length;kk++) idx.push(ia[kk]+vi);
    vi+=pa.count;
  }
  const G=new THREE.BufferGeometry();
  G.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  G.setAttribute('aBase',new THREE.BufferAttribute(new Float32Array(base),3));
  G.setAttribute('aRank',new THREE.BufferAttribute(new Float32Array(rank),1));
  G.setAttribute('aPhase',new THREE.BufferAttribute(new Float32Array(phase),1));
  G.setAttribute('aTip',new THREE.BufferAttribute(new Float32Array(tip),1));
  G.setIndex(idx);
  const m=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSpread:{value:o.spread0===undefined?0.30:o.spread0},
      uCBase:{value:C(0x0b100e)},uCTip:{value:C(o.tipC===undefined?0x5f7a62:o.tipC)},
      uFogColor:{value:C(0x121826)},uFogDensity:{value:0.005},uFade:{value:1}},
    vertexShader:CAO_VERT,fragmentShader:CAO_FRAG});
  fogShaders.push(m.uniforms);
  const mesh=new THREE.Mesh(G,m); mesh.frustumCulled=false; mesh.renderOrder=1;
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t,k){ m.uniforms.uTime.value=t; if(k!==undefined)m.uniforms.uFade.value=k; };
  return {g,mesh,mat:m,update:g.update};
}

/* 明月楼：台基 + 楼身 + 腰檐 + 平座栏杆 + 上层 + 攒尖顶，合批 1 mesh（剪影 + 银边光） */
function makeGaolou(){
  const B=new GeoBag(), c1=0x0c1119, c2=0x151c2a, c3=0x1d2636;
  const base=new THREE.BoxGeometry(11,1.6,7.5); base.translate(0,0.8,0); B.put(base,c1);
  const lip=new THREE.BoxGeometry(11.3,0.14,7.8); lip.translate(0,1.56,0); B.put(lip,c3);
  const body=new THREE.BoxGeometry(5.8,6.6,4.4); body.translate(0,1.6+3.3,0); B.put(body,c2);
  const eave=new THREE.ConeGeometry(5.7,1.25,4); eave.rotateY(Math.PI/4);
  eave.scale(1.3,1,1.12); eave.translate(0,8.2+0.62,0); B.put(eave,c3);
  const deck=new THREE.BoxGeometry(7.2,0.5,6.2); deck.translate(0,9.4+0.25,0); B.put(deck,c1);
  const upper=new THREE.BoxGeometry(4.6,2.8,3.6); upper.translate(0,9.9+1.4,0); B.put(upper,c2);
  const roof=new THREE.ConeGeometry(4.5,1.9,4); roof.rotateY(Math.PI/4);
  roof.scale(1.32,1,1.08); roof.translate(0,12.7+0.95,0); B.put(roof,c3);
  for(let i=0;i<6;i++){
    const post=new THREE.BoxGeometry(0.13,0.95,0.13);
    post.translate(-2.9+i*1.16,9.9+0.475,2.85); B.put(post,c3);
  }
  const rail=new THREE.BoxGeometry(6.3,0.11,0.15); rail.translate(0,9.9+0.95,2.85); B.put(rail,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0xb0bccd,i:0.46,p:2.5})));
  return g;
}

function bCover(){ // 封面 · 秋水长天
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:1630,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const tree=makeHuangye({seed:1631,h:6.2}); tree.position.set(12,0,-16); tree.scale.setScalar(1.15); g.add(tree);
  const figure=makeFigure({pose:'独立',robe:0x242e40,belt:0x5f6e86,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xb0bccd,rim:0.4,noProp:true,scale:1.8});
  figure.position.set(-4.5,0,3); figure.rotation.y=0.5; g.add(figure);
  const clouds=makeFlow({n:110,box:[190,10,80],pos:[0,28,-58],color:0x8fa4c4,size:32,speed:1.1,maxA:0.16});
  g.add(clouds.points);
  const mist=makeMist({n:8,spread:[250,34,160],pos:[0,12,-58],scale:82,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[210,40,120],pos:[0,10,-36],color:0xbcc9dc,size:7,speed:0.05,rise:0,maxA:0.34});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:9,color:0x04060a,seed:1632,rim:0.14});
  rk.g.position.set(0,-2,25); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); clouds.update(t);
    rk.update(t,k); figure.update(t,k);
  }};
}

function bQiutian(){ // 一 · 碧天黄叶 —— 秋色连波，波上寒烟翠
  const g=new THREE.Group();
  const water=makeWater({size:460,seg:86,amp:0.26,freq:0.11,speed:0.45,flow:[0.45,0.1],spec:1.5,
    deep:0x0a141d,shallow:0x143030,skyc:0x2a464a,moonDir:[20,90,-160]});
  g.add(water.mesh);
  const ridge=makeRange({r:245,h:16,layers:2,peaks:4,seed:1633,color:0x081018,atmo:0x24344a,fogK:0.62,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-115); g.add(ridge.g);
  /* 两岸：左近岸立望秋人，右远岸黄叶成林 */
  const bankL=new THREE.Mesh(new THREE.BoxGeometry(16,1.0,64),
    new THREE.MeshPhongMaterial({color:0x0b0f14,shininess:4,specular:0x1d2530}));
  bankL.position.set(-15,-0.15,-12); g.add(bankL);
  const bankR=new THREE.Mesh(new THREE.BoxGeometry(24,1.0,72),
    new THREE.MeshPhongMaterial({color:0x0b0f14,shininess:4,specular:0x1d2530}));
  bankR.position.set(22,-0.15,-14); g.add(bankR);
  const t1=makeHuangye({seed:1634,h:6.4}); t1.position.set(14,0.35,-16); g.add(t1);
  const t2=makeHuangye({seed:1635,h:5.4}); t2.position.set(20,0.35,-24); g.add(t2);
  const t3=makeHuangye({seed:1636,h:4.8}); t3.position.set(-24,0.35,-30); g.add(t3);
  /* 独立岸头的望秋人 */
  const figure=makeFigure({pose:'独立',robe:0x2a3548,belt:0x5f6e86,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xb0bccd,rim:0.5,noProp:true,scale:1.5});
  figure.position.set(-12,0.35,-9); figure.rotation.y=-0.55; g.add(figure);
  /* 波上寒烟翠：贴水冷雾一层 */
  const hanYan=makeMist({n:7,spread:[210,14,110],pos:[0,4.5,-55],scale:70,color:0x6a8a80,op:0.11});
  g.add(hanYan.g);
  /* 黄叶：岸上积叶 + 空中缓落 */
  const fallen=makeGlow({n:44,box:[20,0.5,10],pos:[17,1.4,-18],color:0x6e6438,size:4.2,speed:0.02,rise:0,maxA:0.3,add:false});
  g.add(fallen.points);
  const leaves=makeGlow({n:40,box:[34,12,22],pos:[14,6.5,-12],color:0x746a3a,size:5.5,speed:0.05,rise:0.85,maxA:0.3});
  g.add(leaves.points);
  const clouds=makeFlow({n:100,box:[180,10,80],pos:[0,26,-60],color:0x8fa4c4,size:30,speed:1.2,maxA:0.15});
  g.add(clouds.points);
  const motes=makeGlow({n:50,box:[70,12,40],pos:[0,5,-14],color:0xbcc9dc,size:5,speed:0.06,rise:0.1,maxA:0.24});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:8,color:0x04060a,seed:1637,rim:0.14});
  rk.g.position.set(16,-1.0,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:1638,sway:0.9});
  reeds.g.position.set(-13,-1.1,11); g.add(reeds.g);
  addLights(g,{c:0x9fb3cc,i:0.5,p:[-30,80,-30]},{c:0x1a2430,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); hanYan.update(t,k); fallen.update(t); leaves.update(t);
    clouds.update(t); motes.update(t);
    rk.update(t,k); reeds.update(t,k); figure.update(t,k);
  }};
}

function bXieyang(){ // 二（标志性瞬间）· 斜阳芳草 —— 山映斜阳天接水；芳草无情，更在斜阳外
  const g=new THREE.Group();
  const water=makeWater({size:480,seg:86,amp:0.24,freq:0.10,speed:0.4,flow:[0.4,0.1],spec:1.8,
    deep:0x0b1016,shallow:0x182a2c,skyc:0x3a3430,moonDir:[24,9,-150]});
  water.mesh.position.y=-0.5; g.add(water.mesh);
  const grd=makeGround({r:62,c1:0x090c10,c2:0x10151c});
  grd.mesh.position.set(0,-0.06,26); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:12,layers:2,peaks:3,seed:1639,color:0x0a0d12,atmo:0x2e2620,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-125); g.add(ridge.g);
  /* 山映斜阳：山脊线上的低日轮 + 暖晕（锈赭，禁金） */
  const sun=new THREE.Mesh(new THREE.CircleGeometry(6.5,28),
    new THREE.MeshBasicMaterial({color:0x8a5038,transparent:true,opacity:0.72,depthWrite:false,fog:false,
      blending:THREE.AdditiveBlending}));
  sun.position.set(24,7,-150); sun.renderOrder=2; g.add(sun);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8a5a42,
    transparent:true,opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(72,26,1); halo.position.set(20,9,-148); halo.renderOrder=2; g.add(halo);
  /* 斜光铺水：自日轮一路铺到眼前的锈赭光路 */
  const xg=makeXieguang({w:26,len:112,x:13,y:0.35,z:-92,rot:-0.15,k0:0.5});
  g.add(xg.g);
  /* 芳草无情：静置铺展，蔓向天际 */
  const cao=makeFangcao({n:700,z0:9,z1:-34,spread0:0.62,tipC:0x5f7a62,seed:1640});
  cao.g.position.y=-0.04; g.add(cao.g);
  /* 更在斜阳外：极远处一个独行旅影 */
  const walker=makeCrowd({n:1,rect:[-2,-44,1.2,1.6],seed:1641,color:0x0e131b,rimC:0x8fa4c4,rim:0.16,sMin:0.5,sMax:0.6});
  g.add(walker.mesh);
  /* 黯乡魂：岸上背身而立的旅人 */
  const figure=makeFigure({pose:'独立',robe:0x25303f,belt:0x5f6e86,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xb0bccd,rim:0.48,noProp:true,scale:1.45});
  figure.position.set(3.2,-0.04,-13); figure.rotation.y=2.85; g.add(figure);
  const motes=makeGlow({n:46,box:[80,14,50],pos:[4,6,-20],color:0xbcc9dc,size:5,speed:0.05,rise:0.08,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,20,110],pos:[0,8,-58],scale:76,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const reedsL=makeForeground({kind:'芦苇',w:28,n:14,d:6,color:0x04060a,seed:1642,sway:1.0});
  reedsL.g.position.set(-12,-0.9,17); g.add(reedsL.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:1643,sway:1.2,rim:0.16});
  tree.g.position.set(15,-0.5,24); g.add(tree.g);
  addLights(g,{c:0xb0a08c,i:0.45,p:[30,44,-70]},{c:0x22242a,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    xg.update(t,k); cao.update(t,k); walker.update(t);
    sun.material.opacity=k*(0.62+0.10*Math.sin(t*0.4));
    halo.material.opacity=k*(0.24+0.06*Math.sin(t*0.3+1.0));
    reedsL.update(t,k); tree.update(t,k); figure.update(t,k);
  }};
}

function bLouyue(){ // 三（末境可点击）· 月夜愁肠 —— 点击：斜光铺水、芳草蔓出画外（泪眼中重见斜阳芳草）
  const g=new THREE.Group();
  const ctl={t:0,last:-9,clicked:false,reveal:0};
  const water=makeWater({size:470,seg:86,amp:0.24,freq:0.11,speed:0.42,flow:[0.35,0.12],spec:2.1,
    deep:0x091320,shallow:0x12283e,skyc:0x22364e,moonDir:[-46,100,-175]});
  g.add(water.mesh);
  const ridge=makeRange({r:255,h:14,layers:2,peaks:3,seed:1644,color:0x070b10,atmo:0x1c2434,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 明月楼：楼头独倚人 + 樽前一杯 */
  const tower=makeGaolou(); tower.position.set(-7.5,0,-24); g.add(tower);
  const figure=makeFigure({pose:'独立',robe:0x2a3548,belt:0x5f6e86,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xb0bccd,rim:0.5,noProp:true,scale:1.35});
  figure.position.set(-5.8,9.9,-22.3); figure.rotation.y=2.35; g.add(figure);
  const cup=makeVessel({type:'杯',mat:'陶',scale:1.0,liquid:true,shadow:true});
  cup.g.position.set(-8.9,9.9,-21.9); g.add(cup.g);
  /* 芳草：夜色里伏在岸边，点击后蔓出画外 */
  const cao=makeFangcao({n:820,z0:9,z1:-70,spread0:0.30,tipC:0x4e6356,seed:1645});
  cao.g.position.y=0.05; g.add(cao.g);
  /* 斜光铺水：点击后如泪眼中重见的斜阳 */
  const xg=makeXieguang({w:30,len:118,x:10,y:0.22,z:-86,rot:-0.12,k0:0.0});
  g.add(xg.g);
  const mem=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9a664a,
    transparent:true,opacity:0.34,depthWrite:false,blending:THREE.AdditiveBlending}));
  mem.scale.set(130,34,1); mem.position.set(12,10,-118); mem.renderOrder=2; g.add(mem);
  const motes=makeGlow({n:54,box:[80,14,50],pos:[0,6,-16],color:0xc9d6e8,size:5,speed:0.05,rise:0.08,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,20,110],pos:[0,8,-58],scale:78,color:0x7e8ea8,op:0.09});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',w:28,n:14,d:6,color:0x04060a,seed:1646,sway:0.9});
  reeds.g.position.set(11,-0.9,15); g.add(reeds.g);
  const tree=makeForeground({kind:'树枝',n:2,w:15,d:5,color:0x04060a,seed:1647,sway:1.3,rim:0.16});
  tree.g.position.set(-16,-0.5,24); g.add(tree.g);
  addLights(g,{c:0x9fb3cc,i:0.5,p:[-40,90,-50]},{c:0x1a2232,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/4.0);
      cao.mat.uniforms.uSpread.value=0.30+0.70*ctl.reveal;
      xg.mat.uniforms.uK.value=0.85*ctl.reveal;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      cao.update(t,k); xg.update(t,k);
      mem.material.opacity=k*(0.34*ctl.reveal);
      reeds.update(t,k); tree.update(t,k); figure.update(t,k); cup.update(t,k);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.5)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      pluck(2,0.0,0.12); pluck(4,0.5,0.10); pluck(1,1.0,0.09);
      const fl=$('#flash'); fl.textContent='斜阳芳草';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
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
  cam:{f:[0,9,58],t:[0,9.5,52],lf:[0,13,-42],lt:[0,13,-42]},
  sky:()=>SK({top:C(0x0a0e16),hor:C(0x1a222e),bot:C(0x0b0e14),fog:C(0x101620),fd:0.0048,star:0.35,
    ms:1.3,moon:new THREE.Vector3(24,74,-170),
    dirC:C(0x8fa4c8),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'碧天黄叶',dwell:16,river:0.03,build:bQiutian,
  cam:{f:[0,7,22],t:[0.6,6.8,19],lf:[0,8,-30],lt:[1.5,8,-34]},
  sky:()=>SK({top:C(0x0d1420),hor:C(0x25323c),bot:C(0x0c1118),fog:C(0x111a24),fd:0.0050,star:0.06,
    ms:0.001,moon:new THREE.Vector3(40,-40,120),
    dirC:C(0x9fb3cc),dirI:0.5,ambC:C(0x1a2430),ambI:0.64}) },
{ name:'斜阳芳草',dwell:17,river:0.02,build:bXieyang,
  cam:{f:[0,6.5,24],t:[0,6.8,21],lf:[0,7.5,-60],lt:[0,8.5,-72]},
  sky:()=>SK({top:C(0x0c1017),hor:C(0x33302c),bot:C(0x0d0f13),fog:C(0x14161c),fd:0.0062,star:0.12,
    ms:0.001,moon:new THREE.Vector3(-60,-40,110),
    dirC:C(0xb0a08c),dirI:0.45,ambC:C(0x22242a),ambI:0.60}) },
{ name:'月夜愁肠',dwell:17,river:0.02,build:bLouyue,
  cam:{f:[0,7,28],t:[-0.8,7.5,25],lf:[-6,11.5,-28],lt:[-5,11.5,-31]},
  sky:()=>SK({top:C(0x080c13),hor:C(0x141c2a),bot:C(0x090d13),fog:C(0x121a26),fd:0.0058,star:0.5,
    ms:2.0,mph:0,mhaze:0.04,moon:new THREE.Vector3(-46,100,-175),
    dirC:C(0x9fb3cc),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
];
"""
