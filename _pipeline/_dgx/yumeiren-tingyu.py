# -*- coding: utf-8 -*-
"""yumeiren-tingyu.py —— 《虞美人·听雨》（宋·蒋捷，no.198，水墨夜思）生成配置
两境（queue 分境为准，一生三场雨装进两重词境）：
  壹·歌楼客舟 —— 少年听雨歌楼上，红烛昏罗帐（全页唯一暖）；壮年听雨客舟中，江阔云低、断雁叫西风（转苍）。
  贰·僧庐天明 —— 而今听雨僧庐下，鬓已星星也；悲欢离合总无情，一任阶前点滴到天明（转冷、放下）。
标志性瞬间：三场听雨写尽一生 —— 同一动作（听雨）三个时空（歌楼/客舟/僧庐），末境同框对切：
  远山歌楼暖窗、远处江上客舟、近前僧庐檐下老僧，同构图三个时空；点击听雨——雨声由暖转寒、
  头顶屋檐由歌楼换僧庐、远山暖窗熄灭，唯余阶前点滴到天明（雨声不老，听雨的人老去）。
全页冷银水墨，禁金；唯一暖是歌楼红烛（少年记忆），末境点击后连这点暖也熄了。"""

META = dict(
    N=2, slug='yumeiren-tingyu', title='虞美人·听雨', dyn='宋 · 蒋捷', brand_author='蒋捷',
    gold_rgb='144,168,200',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#90a8c8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(144,168,200,.26);
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
    tip='轻点画面 / 按空格 —— 听雨：雨声由暖转寒，屋檐由歌楼换僧庐',
    hint='← → 键或空格逐境游览 · 末境可点击听雨：雨声由暖转寒，点滴到天明',
    cover_read='虞美人·听雨。宋，蒋捷。少年听雨歌楼上，红烛昏罗帐。壮年听雨客舟中，江阔云低，断雁叫西风。而今听雨僧庐下，鬓已星星也。悲欢离合总无情，一任阶前，点滴到天明。',
    cover_p1='词以「听雨」为线，三场雨写尽一生：少年在歌楼上听雨，红烛昏黄、罗帐低垂，雨声不过是欢愉的伴奏；壮年在客舟中听雨，江阔云低、断雁叫西风，雨声里全是漂泊的苍凉；而今在僧庐下听雨，两鬓已白如星星，悲欢离合总归无情——一任阶前点滴，直到天明。',
    cover_p2='边读词，边走进蒋捷笔下这三场人生之雨：雨声不老，听雨的人却老去；末境轻点画面，听雨声由暖转寒，看屋檐由歌楼换作僧庐。',
    end_h2='点滴 · 天明', cn_word='两',
    words_js="['再游一次，且听雨声','初识竹山，尚需共读','渐入佳境，再诵几遍','词境渐深，雨声渐寒','已解三场听雨之叹','一任点滴，心境澄明']",
    sky_atmo='0x1c2433',
)

POEM_JS = """const POEM = [
{ name:'歌楼客舟', jing:'同一夜雨，先落在歌楼的红烛罗帐里，再落在客舟的篷顶上 —— 江阔云低，断雁叫西风。（红烛 · 客舟 · 断雁）',
  segs:[
   {c:'少年听雨歌楼上，', p:py('shào nián tīng yǔ gē lóu shàng')},
   {c:'红烛昏罗帐。', p:py('hóng zhú hūn luó zhàng')},
   {c:'壮年听雨客舟中，', p:py('zhuàng nián tīng yǔ kè zhōu zhōng')},
   {c:'江阔云低，', p:py('jiāng kuò yún dī')},
   {c:'断雁叫西风。', p:py('duàn yàn jiào xī fēng')}],
  read:'少年听雨歌楼上，红烛昏罗帐。壮年听雨客舟中，江阔云低，断雁叫西风。',
  yisi:'少年时候在歌楼上听雨，红烛的光昏昏沉沉，映得丝罗帐幔一片朦胧——雨声混着笙歌，不过是欢愉的伴奏；壮年时在客船里听雨，江面辽阔、云脚低垂，一只失群的孤雁在西风里声声哀叫——雨打篷顶，也打在羁旅人的心上。同是听雨，少年听出的是繁华，壮年听出的是身世。',
  zhu:[['虞美人','词牌名，双调五十六字，得名于项羽垓下之围中「霸王别姬」的虞姬故事；蒋捷此词与李煜「春花秋月何时了」同为此调千古名作'],
       ['蒋捷','宋末词人，号竹山，阳羡（今江苏宜兴）人；南宋亡后隐居不仕，气节为时人推重，世称「竹山先生」，一生饱经离乱'],
       ['红烛昏罗帐','红烛之光昏昏，映得丝罗帐幔朦胧温软；写少年听雨的欢愉缱绻，是全词唯一的暖色'],
       ['客舟','羁旅客居之船；壮年为生计奔波、漂泊江湖，夜雨孤舟，最能照见身世'],
       ['断雁','失群的孤雁；断，离群、孤绝。雁声哀切混着西风，正是游子心声；西风，秋风']] },
{ name:'僧庐天明', jing:'而今僧庐听雨，两鬓已白如星星 —— 悲欢离合总无情，一任阶前点滴到天明。（僧庐 · 鬓星星 · 一任）',
  segs:[
   {c:'而今听雨僧庐下，', p:py('ér jīn tīng yǔ sēng lú xià')},
   {c:'鬓已星星也。', p:py('bìn yǐ xīng xīng yě')},
   {c:'悲欢离合总无情，', p:py('bēi huān lí hé zǒng wú qíng')},
   {c:'一任阶前，', p:py('yī rèn jiē qián')},
   {c:'点滴到天明。', p:py('diǎn dī dào tiān míng')}],
  read:'而今听雨僧庐下，鬓已星星也。悲欢离合总无情，一任阶前，点滴到天明。',
  yisi:'如今两鬓已经斑白，听雨的地方换成了僧庐之下。悲欢离合总归是无情的东西，由不得人，也就不必再为它动心——且听阶前的雨滴吧，一任它点点滴滴，下到天明。一个「一任」，看似放下，底子里是一生沧桑说不得的苍凉。',
  zhu:[['僧庐','僧房、寺庙的屋舍；词人晚年寓居僧舍听雨，境况孤寂清冷'],
       ['鬓已星星也','两鬓已经斑白，白发点点如星；星星，形容白发斑斑的样子；也，语气词，一声长叹'],
       ['总无情','悲欢离合总是无情，由不得人；历尽沧桑后的彻悟之语'],
       ['一任','听凭、任凭；任雨滴落到天明也无动于衷——看似超脱，实是心如止水后的放下；任，读 rèn'],
       ['点滴到天明','雨滴在阶前点点滴滴，直到天亮；无眠听雨，言尽而意不尽']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「少年听雨歌楼上」的下一句是？', o:['红烛昏罗帐','壮年听雨客舟中','江阔云低，断雁叫西风'], a:0},
 {q:'「悲欢离合总无情」的下一句是？', o:['鬓已星星也','一任阶前，点滴到天明','而今听雨僧庐下'], a:1},
 {q:'「一任阶前，点滴到天明」中「任」的正确读音与意思是？', o:['rén，姓氏，如姓任','rèn，听凭、任凭','rèn，任务、责任'], a:1},
 {q:'词牌「虞美人」得名于？', o:['项羽垓下被围时「霸王别姬」的虞姬故事','江南一种美人花的别名','汉代宫廷壁画《虞美人图》'], a:0},
 {q:'全词用同一「听雨」串起少年歌楼、壮年客舟、而今僧庐三境，主要想说的是？', o:['听雨的场所越换越差，感慨生活变故','一生欢愉、漂泊与孤寂尽在三场雨声里，最终以「一任」二字放下悲欢','雨声有暖有寒，教人分辨四季'], a:1},
];
"""

SCENES_JS = """/* ================= 虞美人·听雨 · 两境场景（水墨夜思：三场听雨写尽一生） =================
   同一动作（听雨）三个时空（歌楼/客舟/僧庐）：
   壹境同框两场雨——近岸歌楼红烛（全页唯一暖）+ 江心客舟断雁（苍）；
   贰境僧庐檐下老僧 + 远山歌楼、远江客舟两处记忆剪影（三境同构对切）；
   点击听雨：雨声由暖转寒、屋檐由歌楼换僧庐、远山暖窗熄灭 —— 雨声不老，听雨的人老去。 */

/* 夜雨：斜落的细雨丝（自定义着色器，水墨夜雨母题）。uColor/uMaxA 由各境按色温叙事驱动 */
const RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uSlant;
varying float vA;
void main(){
  float life=fract(uTime*uSpeed*(0.7+0.6*fract(aSeed*5.31))+aSeed);
  vec3 p=position;
  float dy=uBox.y*(0.5-life);
  p.y+=dy; p.x+=dy*uSlant;
  vA=smoothstep(0.0,0.10,life)*smoothstep(1.0,0.86,life)*(0.35+0.65*fract(aSeed*13.7));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const RAIN_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=length(q*vec2(8.0,0.36));
  float a=smoothstep(0.5,0.06,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeRain(o){
  o=o||{};
  const n=o.n===undefined?140:o.n, box=o.box||[100,28,54], pos=o.pos||[0,15,-16];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.0:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.5:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uSlant:{value:o.slant===undefined?0.14:o.slant},
      uColor:{value:C(o.color===undefined?0x9dadbe:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.20:o.maxA}},
    vertexShader:RAIN_VERT,fragmentShader:RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* 点滴：檐口坠落的雨滴（滴水穿阶，点滴到天明） */
const DI_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform float uDropH;
varying float vA;
void main(){
  float life=fract(uTime*uSpeed*(0.8+0.4*fract(aSeed*3.7))+aSeed);
  vec3 p=position; p.y-=uDropH*life;
  vA=smoothstep(0.0,0.06,life)*smoothstep(1.0,0.9,life);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const DI_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.12,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeDidi(o){
  o=o||{};
  const n=o.n===undefined?6:o.n, box=o.box||[4.6,0.4,0.6], pos=o.pos||[-4.6,4.4,-18.4];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.6:o.size)*(0.8+Math.random()*0.4);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.5:o.speed},
      uDropH:{value:o.dropH===undefined?3.6:o.dropH},
      uColor:{value:C(o.color===undefined?0xbcd0e8:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.16:o.maxA}},
    vertexShader:DI_VERT,fragmentShader:DI_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* 歌楼：两层木楼（台基+双层楼板+腰檐+四棱锥顶），二层前窗内置红烛与罗帐 —— 全页唯一暖。
   返回 {g, glowMat(暖辉), gauzeMat(罗帐), winMat(窗光), light(烛光)}，暖系统 opacity 由各境按 fadeK 自控 */
function makeGelou(o){
  o=o||{};
  const B=new GeoBag();
  const stoneC=0x0d1219, wallC=0x111722, woodC=0x151c29, wood2=0x1b2434, roofC=0x0a0e16;
  const base=new THREE.BoxGeometry(8.0,1.0,6.6); base.translate(0,0.5,0); B.put(base,stoneC);
  const stair=new THREE.BoxGeometry(2.6,1.0,1.5); stair.translate(0,0.5,4.0); B.put(stair,stoneC);
  [[-3.4,-2.6],[3.4,-2.6],[-3.4,2.6],[3.4,2.6]].forEach(function(pt){
    const c=new THREE.CylinderGeometry(0.17,0.20,3.6,7); c.translate(pt[0],1.0+1.8,pt[1]); B.put(c,woodC);
  });
  const hall=new THREE.BoxGeometry(6.8,3.2,5.2); hall.translate(0,1.0+1.6,0); B.put(hall,wallC);
  const e1f=new THREE.BoxGeometry(8.6,0.24,2.0); e1f.translate(0,4.6,3.2); B.put(e1f,roofC);
  const e1b=new THREE.BoxGeometry(8.6,0.24,2.0); e1b.translate(0,4.6,-3.2); B.put(e1b,roofC);
  const e1l=new THREE.BoxGeometry(2.0,0.24,6.2); e1l.translate(-4.15,4.6,0); B.put(e1l,roofC);
  const e1r=new THREE.BoxGeometry(2.0,0.24,6.2); e1r.translate(4.15,4.6,0); B.put(e1r,roofC);
  const deck=new THREE.BoxGeometry(6.2,0.35,4.8); deck.translate(0,4.85,0); B.put(deck,wood2);
  [[-2.6,-1.9],[2.6,-1.9],[-2.6,1.9],[2.6,1.9]].forEach(function(pt){
    const c=new THREE.CylinderGeometry(0.13,0.15,2.7,7); c.translate(pt[0],5.02+1.35,pt[1]); B.put(c,woodC);
  });
  const rail=new THREE.BoxGeometry(5.6,0.10,0.12); rail.translate(0,6.55,2.05); B.put(rail,wood2);
  for(let i=0;i<5;i++){
    const pt=new THREE.BoxGeometry(0.09,0.6,0.09); pt.translate(-2.4+i*1.2,6.2,2.05); B.put(pt,woodC);
  }
  const beam=new THREE.BoxGeometry(6.0,0.35,4.4); beam.translate(0,7.95,0); B.put(beam,wood2);
  const roof=new THREE.ConeGeometry(4.7,2.4,4); roof.rotateY(Math.PI/4); roof.translate(0,8.3+1.2,0); B.put(roof,roofC);
  const finial=new THREE.SphereGeometry(0.24,8,6); finial.translate(0,11.05,0); B.put(finial,roofC);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.22,p:2.5})));
  /* 二层前窗：暗窗膛 + 两支红烛 + 罗帐 + 窗光 + 暖辉 + 烛光（暖系统，初值=最大值） */
  const winMat=new THREE.MeshBasicMaterial({color:0x571f10,transparent:true,opacity:0.85,depthWrite:false});
  const win=new THREE.Mesh(new THREE.PlaneGeometry(2.3,1.6),winMat);
  win.position.set(-0.9,6.6,2.16); g.add(win);
  const CB=new GeoBag(), candleC=0x8a2c16;
  const c1=new THREE.CylinderGeometry(0.09,0.10,0.62,6); c1.translate(-1.25,6.05,2.32); CB.put(c1,candleC);
  const c2=new THREE.CylinderGeometry(0.09,0.10,0.62,6); c2.translate(-0.5,6.05,2.32); CB.put(c2,candleC);
  const stand=new THREE.BoxGeometry(1.3,0.10,0.34); stand.translate(-0.87,5.7,2.32); CB.put(stand,0x2a2018);
  g.add(CB.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    emissive:0x30100a,specular:0x3a2a20})));
  const mkFlame=function(x){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8a35c,
      transparent:true,opacity:0.95,depthWrite:false,blending:THREE.AdditiveBlending}));
    s.scale.set(0.9,0.9,1); s.position.set(x,6.48,2.36); s.renderOrder=3; g.add(s); return s;
  };
  const flame1=mkFlame(-1.25), flame2=mkFlame(-0.5);
  const gauzeMat=new THREE.MeshBasicMaterial({color:0xc09a74,transparent:true,opacity:0.32,
    depthWrite:false,side:THREE.DoubleSide});
  const gauze=new THREE.Mesh(new THREE.PlaneGeometry(3.2,2.0),gauzeMat);
  gauze.position.set(-0.9,6.55,2.62); gauze.renderOrder=3; g.add(gauze);
  const glowMat=new THREE.SpriteMaterial({map:glowTex(),color:0xd9a05e,
    transparent:true,opacity:0.46,depthWrite:false,blending:THREE.AdditiveBlending});
  const glow=new THREE.Sprite(glowMat);
  glow.scale.set(7.5,7.5,1); glow.position.set(-0.9,6.8,3.4); glow.renderOrder=3; g.add(glow);
  const light=new THREE.PointLight(0xd99a55,1.35,36); light.position.set(-0.9,6.4,3.6); g.add(light);
  return {g,flames:[flame1,flame2],gauzeMat,glowMat,winMat,light};
}

/* 客舟：船体（中段+两头尖）+ 篷顶（半穹）+ 接触阴影 —— 壮年听雨处 */
function makeKezhou(o){
  o=o||{};
  const B=new GeoBag(), hullC=0x10161f, canopyC=0x0c1119;
  const mid=new THREE.BoxGeometry(4.6,0.78,1.8); mid.translate(0,0.55,0); B.put(mid,hullC);
  const bow=new THREE.ConeGeometry(0.82,2.0,4); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.62,1.05); bow.translate(3.1,0.5,0); B.put(bow,hullC);
  const stern=new THREE.ConeGeometry(0.82,2.0,4); stern.rotateZ(Math.PI/2);
  stern.scale(1,0.62,1.05); stern.translate(-3.1,0.5,0); B.put(stern,hullC);
  const rim=new THREE.BoxGeometry(4.7,0.10,1.9); rim.translate(0,0.98,0); B.put(rim,shadeColor(hullC,1.5));
  const dome=new THREE.SphereGeometry(1.05,10,6,0,Math.PI*2,0,Math.PI/2);
  dome.scale(1.55,0.72,0.92); dome.translate(-0.95,1.0,0); B.put(dome,canopyC);
  for(let i=0;i<3;i++){
    const rb=new THREE.TorusGeometry(1.02,0.045,5,12,Math.PI);
    rb.rotateY(Math.PI/2); rb.scale(1,0.72,0.92); rb.translate(-0.95-i*1.0+1.0,1.0,0);
    B.put(rb,shadeColor(canopyC,1.8));
  }
  const shadow=new THREE.CircleGeometry(2.6,16); shadow.rotateX(-Math.PI/2); shadow.scale(1.3,1,0.55);
  shadow.translate(0,0.06,0); B.put(shadow,0x04060a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.18,p:2.4})));
  return {g};
}

/* 断雁：失群的孤雁（剪影，缓飞横江，哀鸣一声） */
function makeDuanYan(o){
  o=o||{};
  const B=new GeoBag(), c=o.color===undefined?0x10151d:o.color;
  const w1=new THREE.PlaneGeometry(1.6,0.38); w1.rotateZ(0.52); w1.translate(-0.68,0.16,0); B.put(w1,c);
  const w2=new THREE.PlaneGeometry(1.6,0.38); w2.rotateZ(-0.52); w2.translate(0.68,0.16,0); B.put(w2,c);
  const bd=new THREE.ConeGeometry(0.17,1.0,5); bd.rotateZ(-Math.PI/2); bd.scale(1,1,0.55);
  bd.translate(0,0.10,0); B.put(bd,c);
  const mesh=new THREE.Mesh(mergeGeos(B.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,transparent:true,
      opacity:0.62,specular:0x2a3446,emissive:0x05070c,side:THREE.DoubleSide}));
  mesh.renderOrder=2; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh};
}

/* 僧庐：矮小的僧房（台基+墙体+圆窗+门+出檐+两坡顶+阶前三级石阶） */
function makeSenglu(o){
  const B=new GeoBag();
  const stoneC=0x0c1119, wallC=0x10141d, woodC=0x171e2b, roofC=0x0a0d14;
  const base=new THREE.BoxGeometry(6.6,0.8,5.2); base.translate(0,0.4,0); B.put(base,stoneC);
  const body=new THREE.BoxGeometry(5.6,2.8,4.2); body.translate(0,0.8+1.4,0); B.put(body,wallC);
  const ring=new THREE.TorusGeometry(0.55,0.08,6,20); ring.translate(0.9,2.7,2.12); B.put(ring,woodC);
  const rd=new THREE.CircleGeometry(0.55,16); rd.translate(0.9,2.7,2.06); B.put(rd,0x05070c);
  const door=new THREE.BoxGeometry(0.95,1.75,0.10); door.translate(-1.3,0.8+0.875,2.08); B.put(door,0x05070c);
  const ef=new THREE.BoxGeometry(7.0,0.26,1.7); ef.rotateX(0.13); ef.translate(0,4.05,1.35); B.put(ef,roofC);
  const eb=new THREE.BoxGeometry(7.0,0.26,1.3); eb.translate(0,4.0,-1.5); B.put(eb,roofC);
  const rl=new THREE.BoxGeometry(4.4,0.24,5.4); rl.rotateZ(0.42); rl.translate(-2.0,5.15,0); B.put(rl,roofC);
  const rr=new THREE.BoxGeometry(4.4,0.24,5.4); rr.rotateZ(-0.42); rr.translate(2.0,5.15,0); B.put(rr,roofC);
  const ridge=new THREE.BoxGeometry(0.26,0.26,5.6); ridge.translate(0,6.1,0); B.put(ridge,roofC);
  for(let i=0;i<3;i++){
    const st=new THREE.BoxGeometry(3.4-i*0.3,0.24,0.9);
    st.translate(0,0.62-i*0.24,2.6+i*0.85+0.45); B.put(st,shadeColor(stoneC,1.25));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.20,p:2.4})));
  return {g};
}

/* 记忆之檐（末境可对切的双檐）：歌楼檐角（暖，记忆）与僧庐檐（冷，当下）同位叠置。
   返回 {g, songMats, songGrp, sengMat, gauzeMat, glowMat, light} —— 点击后由各境按 fadeK 对切 */
function makeYanDuiqie(){
  const slot=new THREE.Group();
  /* 歌楼檐（记忆）：檐板 + 两根小柱 + 栏杆一道 + 罗帐 + 暖辉 + 烛光 */
  const songGrp=new THREE.Group();
  const SB=new GeoBag();
  const se=new THREE.BoxGeometry(5.6,0.26,1.7); se.rotateX(0.14); se.translate(0,0,0); SB.put(se,0x141a26);
  const p1=new THREE.CylinderGeometry(0.10,0.12,1.5,6); p1.translate(-2.35,-0.9,0.35); SB.put(p1,0x121824);
  const p2=new THREE.CylinderGeometry(0.10,0.12,1.5,6); p2.translate(2.35,-0.9,0.35); SB.put(p2,0x121824);
  const rail=new THREE.BoxGeometry(5.2,0.09,0.10); rail.translate(0,-1.55,0.6); SB.put(rail,0x1b2434);
  for(let i=0;i<5;i++){
    const pt=new THREE.BoxGeometry(0.08,0.5,0.08); pt.translate(-2.2+i*1.1,-1.35,0.6); SB.put(pt,0x121824);
  }
  const songMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    transparent:true,opacity:1.0,specular:0x2a3446,emissive:0x04060a});
  songGrp.add(SB.mesh(rimHook(songMat,{c:0x8fa4c4,i:0.20,p:2.4})));
  const gauzeMat=new THREE.MeshBasicMaterial({color:0xc09a74,transparent:true,opacity:0.30,
    depthWrite:false,side:THREE.DoubleSide});
  const gauze=new THREE.Mesh(new THREE.PlaneGeometry(3.4,1.8),gauzeMat);
  gauze.position.set(0,-0.75,0.42); gauze.renderOrder=3; songGrp.add(gauze);
  const glowMat=new THREE.SpriteMaterial({map:glowTex(),color:0xd9a05e,
    transparent:true,opacity:0.45,depthWrite:false,blending:THREE.AdditiveBlending});
  const glow=new THREE.Sprite(glowMat);
  glow.scale.set(6.5,6.5,1); glow.position.set(0,-0.9,1.0); glow.renderOrder=3; songGrp.add(glow);
  const light=new THREE.PointLight(0xd99a55,1.2,30); light.position.set(0,-1.0,1.4);
  light.userData.baseI=1.2; songGrp.add(light);
  slot.add(songGrp);
  /* 僧庐檐（当下）：素檐板 + 檐角风铃，冷银 */
  const EB=new GeoBag();
  const eb=new THREE.BoxGeometry(5.8,0.28,1.9); eb.rotateX(0.13); eb.translate(0,0,0); EB.put(eb,0x0c1119);
  const bell=new THREE.ConeGeometry(0.09,0.22,5); bell.translate(2.72,-0.5,0.4); EB.put(bell,0x1d2532);
  const sengMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    transparent:true,opacity:0.0,specular:0x2a3446,emissive:0x04060a});
  sengMat.userData.baseOpacity=1.0;   /* 初值=最大值：点击后凝实到 1 */
  const sengGrp=new THREE.Group();
  sengGrp.add(EB.mesh(rimHook(sengMat,{c:0x8fa4c4,i:0.22,p:2.4})));
  slot.add(sengGrp);
  return {g:slot,songGrp,songMat,sengMat,gauzeMat,glowMat,light};
}

function bCover(){ // 封面 · 夜雨大江 —— 一场无始无终的夜雨
  const g=new THREE.Group();
  const water=makeWater({size:320,seg:72,amp:0.16,freq:0.19,speed:0.4,flow:[0.1,0.42],spec:1.4,
    deep:0x0a0f18,shallow:0x16202f,skyc:0x1e2a3c,moonDir:[-26,96,-182]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:16,layers:2,peaks:4,seed:19800,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-124); g.add(ridge.g);
  const boat=makeKezhou(); boat.g.position.set(13,-0.3,-40); boat.g.rotation.y=0.4;
  boat.g.scale.setScalar(0.7); g.add(boat.g);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8c2d4,
    transparent:true,opacity:0.35,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(3.2,3.2,1); lamp.position.set(13,1.6,-39); lamp.renderOrder=3; g.add(lamp);
  const rain=makeRain({n:130,box:[140,30,70],pos:[0,16,-18],color:0x93a2b6,maxA:0.20,size:2.3,slant:0.15});
  g.add(rain.points);
  const mist=makeMist({n:6,spread:[230,22,120],pos:[0,9,-52],scale:76,color:0x8496ae,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[160,24,90],pos:[0,10,-34],color:0xa4b2c6,size:5,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:19801,rim:0.14});
  fgRock.g.position.set(-14,-1.6,32); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:19802,sway:1.0});
  reeds.g.position.set(12,-1.1,30); g.add(reeds.g);
  addLights(g,{c:0x8fa4c4,i:0.40,p:[-30,78,-36]},{c:0x18202d,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); rain.update(t); mist.update(t,k); motes.update(t);
    boat.g.position.y=-0.3+0.07*Math.sin(t*0.8); boat.g.rotation.z=0.02*Math.sin(t*0.6+1);
    lamp.material.opacity=k*(0.30+0.05*Math.sin(t*1.7));
    fgRock.update(t,k); reeds.update(t,k);
  }};
}

function bGelouKezhou(){ // 壹 · 歌楼客舟 —— 近岸歌楼红烛（全页唯一暖），江心客舟断雁（苍）
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:80,amp:0.16,freq:0.18,speed:0.4,flow:[0.1,0.4],spec:1.5,
    deep:0x0a0f18,shallow:0x17212f,skyc:0x1e2a3c,moonDir:[-30,92,-190]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:19803,color:0x070a10,atmo:0x1c2433,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-126); g.add(ridge.g);
  /* 歌楼（近岸石矶上）：红烛昏罗帐 —— 全页唯一暖 */
  const gelou=makeGelou();
  gelou.g.position.set(-12,0.6,-25); gelou.g.rotation.y=0.42; gelou.g.scale.setScalar(1.3);
  g.add(gelou.g);
  const rock=new THREE.Mesh(rockGeo(6.5,1,seedRnd(19804)),
    rimHook(new THREE.MeshPhongMaterial({color:0x0a0e15,shininess:6,specular:0x222c3c,emissive:0x04060a}),
      {c:0x8fa4c4,i:0.14,p:2.4}));
  rock.scale.set(1.7,0.85,1.3); rock.position.set(-12,-1.4,-26.5); g.add(rock);
  /* 少年：凭栏听雨，意气扬扬（月白袍，无胡须） */
  const boy=makeFigure({pose:'指月',robe:0x55648a,belt:0x8292ac,skin:0xd9bb9c,collar:0xc9d4e4,
    hat:'发髻',rimC:0x90a8c8,rim:0.62,noProp:true,scale:0.64});
  boy.position.set(1.75,5.02,1.45); boy.rotation.y=-0.55; gelou.g.add(boy);
  /* 客舟（江心）：壮年听雨客舟中 */
  const boat=makeKezhou(); boat.g.position.set(9.5,-0.1,-19.5); boat.g.rotation.y=-0.4;
  boat.g.scale.setScalar(1.35); g.add(boat.g);
  const man=makeFigure({pose:'坐饮',robe:0x2e3949,belt:0x4e5b72,skin:0xcdb193,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0x90a8c8,rim:0.46,noProp:true,scale:0.72});
  man.position.set(1.35,1.02,0.05); man.rotation.y=-0.3; boat.g.add(man);
  /* 断雁：失群的孤雁横江哀鸣（压入画面内的天空） */
  const yan=makeDuanYan(); yan.g.position.set(20,14,-56); g.add(yan.g);
  /* 江阔云低：低云横江 */
  const cloud=makeFlow({n:150,box:[180,12,70],pos:[0,10,-52],color:0x8494ac,size:30,speed:2.2,maxA:0.16});
  g.add(cloud.points);
  /* 夜雨：满江冷雨 + 歌楼檐前一角被烛光映暖的雨 */
  const rain=makeRain({n:150,box:[110,28,56],pos:[2,15,-16],color:0x9dadbe,maxA:0.26,size:2.6,slant:0.15});
  g.add(rain.points);
  const warmRain=makeRain({n:90,box:[30,18,16],pos:[-11,11,-18],color:0xb9a791,maxA:0.15,slant:0.09,size:1.9});
  g.add(warmRain.points);
  const mist=makeMist({n:5,spread:[220,20,110],pos:[0,8,-50],scale:74,color:0x8496ae,op:0.07});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[150,22,80],pos:[0,9,-28],color:0xa4b2c6,size:5,speed:0.05,rise:0,maxA:0.20});
  g.add(motes.points);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:19805,rim:0.14});
  fgRock.g.position.set(14,-1.5,12); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:9,d:6,color:0x04060a,seed:19806,sway:0.9});
  reeds.g.position.set(-14,-1.2,12); g.add(reeds.g);
  addLights(g,{c:0x93a4ba,i:0.40,p:[-24,80,-30]},{c:0x1a2130,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); cloud.update(t); rain.update(t); warmRain.update(t);
    mist.update(t,k); motes.update(t);
    boat.g.position.y=-0.1+0.08*Math.sin(t*0.85); boat.g.rotation.z=0.025*Math.sin(t*0.62+1);
    yan.g.position.x=20-((t*1.6)%40); yan.g.position.y=14+0.5*Math.sin(t*0.9);
    yan.mesh.material.opacity=k*0.62;
    boy.userData.update(t,k); man.userData.update(t,k);
    gelou.light.intensity=k*(1.35+0.09*Math.sin(t*7.3)+0.05*Math.sin(t*13.7));
    gelou.glowMat.opacity=k*(0.42+0.04*Math.sin(t*2.1));
    gelou.gauzeMat.opacity=k*(0.30+0.02*Math.sin(t*1.3));
    gelou.flames[0].material.opacity=k*(0.85+0.1*Math.sin(t*9.1));
    gelou.flames[1].material.opacity=k*(0.85+0.1*Math.sin(t*8.3+1.7));
    fgRock.update(t,k); reeds.update(t,k);
  }};
}

function bSenglu(){ // 贰（标志性瞬间·末境可点击）· 僧庐天明 —— 三境同构对切；点击听雨：雨声由暖转寒，屋檐由歌楼换僧庐
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0};
  const grd=makeGround({r:150,c1:0x06090e,c2:0x0d1219});
  grd.mesh.position.y=-0.15; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:14,layers:2,peaks:4,seed:19807,color:0x070a10,atmo:0x1b2330,fogK:0.58,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-122); g.add(ridge.g);
  /* 僧庐（近山脚）：矮僧房 + 阶前石阶 */
  const hut=makeSenglu(); hut.g.position.set(-7.2,0,-24); hut.g.rotation.y=0.28;
  hut.g.scale.setScalar(1.25); g.add(hut.g);
  /* 老僧般的听雨人：鬓已星星（灰白发），立于阶前檐下 */
  const old=makeFigure({pose:'独立',robe:0x35404f,belt:0x535f73,skin:0xc9ad8f,collar:0x94a0b2,
    hair:0x828a9a,hat:'发髻',beard:true,rimC:0x90a8c8,rim:0.42,noProp:true,scale:1.5});
  old.position.set(-4.6,0.55,-16.6); old.rotation.y=0.18; g.add(old);
  /* 记忆之檐（头顶对切）：歌楼檐（暖，记忆）↔ 僧庐檐（冷，当下）——悬于听雨人头顶前方，与僧庐屋顶分离 */
  const yan=makeYanDuiqie(); yan.g.position.set(-4.9,4.3,-18.6); yan.g.rotation.y=0.18;
  g.add(yan.g);
  /* 三境同构对切的两处记忆剪影：远山歌楼（暖窗）、远江客舟 */
  const farLou=makeGelou(); farLou.g.position.set(-46,1.8,-88); farLou.g.rotation.y=0.5;
  farLou.g.scale.setScalar(0.32); g.add(farLou.g);
  const farZhou=makeKezhou(); farZhou.g.position.set(25,-0.15,-62); farZhou.g.rotation.y=0.5;
  farZhou.g.scale.setScalar(0.62); g.add(farZhou.g);
  const zhouMist=makeMist({n:3,spread:[14,3,8],pos:[25,0.1,-61],scale:7,color:0x7e90a8,op:0.14});
  g.add(zhouMist.g);
  /* 阶前点滴：檐口坠雨（点滴到天明） */
  const didi=makeDidi({n:7,box:[4.6,0.4,0.6],pos:[-4.9,3.95,-18.0],dropH:3.3,maxA:0.15});
  g.add(didi.points);
  /* 夜雨（由暖转寒的记忆色）+ 悲欢横流 + 霜尘 */
  const rain=makeRain({n:150,box:[110,30,60],pos:[0,15,-18],color:0xb0a795,maxA:0.32,size:2.6,slant:0.13});
  g.add(rain.points);
  const flow=makeFlow({n:90,box:[120,14,50],pos:[0,8,-42],color:0x8494aa,size:24,speed:1.4,maxA:0.10});
  g.add(flow.points);
  const motes=makeGlow({n:40,box:[110,18,60],pos:[0,8,-26],color:0xaebdd2,size:4.5,speed:0.05,rise:0,maxA:0.20});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,20,110],pos:[0,8,-48],scale:72,color:0x7e90a8,op:0.07});
  g.add(mist.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:19808,rim:0.14});
  fgRock.g.position.set(14,-1.5,12); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:19809,sway:1.1});
  reeds.g.position.set(-14,-1.2,12); g.add(reeds.g);
  addLights(g,{c:0x8ea2ba,i:0.36,p:[26,70,30]},{c:0x161d29,i:0.54});
  /* 点击叙事用色 */
  const warmC=C(0xb0a795), coldC=C(0xa5b9d4);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const el=ctl.clicked?ctl.t-ctl.clickT:0;
      const e=ease(clamp(el/2.6,0,1));
      ridge.update(t,0); mist.update(t,k); zhouMist.update(t,k); flow.update(t);
      rain.update(t); didi.update(t); motes.update(t);
      fgRock.update(t,k); reeds.update(t,k);
      old.userData.update(t,k);
      /* 屋檐由歌楼换僧庐：歌楼檐浮散、僧庐檐凝实 */
      yan.songMat.opacity=k*(1.0-0.92*e);
      yan.gauzeMat.opacity=k*(0.30*(1-e));
      yan.glowMat.opacity=k*(0.45*(1-e));
      yan.light.intensity=k*(1.2*(1-e));
      yan.songGrp.position.y=0.9*e; yan.songGrp.position.z=-1.1*e;
      yan.sengMat.opacity=k*(0.04+0.96*e);
      /* 远山歌楼暖窗随之熄灭（雨声由暖转寒） */
      farLou.light.intensity=k*(1.1*(1-e));
      farLou.glowMat.opacity=k*(0.40*(1-e));
      farLou.gauzeMat.opacity=k*(0.30*(1-e));
      farLou.flames.forEach(function(f){ f.material.opacity=k*(0.85*(1-e)); });
      /* 雨色转寒、雨声渐密渐清，点滴到天明 */
      rain.mat.uniforms.uColor.value.copy(warmC).lerp(coldC,e);
      rain.mat.uniforms.uMaxA.value=k*(0.26+0.06*e);
      didi.mat.uniforms.uMaxA.value=k*(0.15+0.10*e);
    },onEnter(){
      pluck(2,0.2,0.06); pluck(4,0.8,0.05);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(4,0.02,0.09); pluck(2,0.55,0.09); pluck(1,1.15,0.08); pluck(0,1.85,0.08);
        const fl=$('#flash'); fl.textContent='点滴到天明'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x161e2c),bot:C(0x080b11),fog:C(0x121926),fd:0.0055,star:0.28,
  moon:new THREE.Vector3(30,108,-190),ms:1.1,mph:0.04,mhaze:0.10,dirC:C(0x93a4ba),dirI:0.42,
  dirP:new THREE.Vector3(-24,80,-30),ambC:C(0x18202d),ambI:0.58},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9.5,56],t:[0,10,50],lf:[0,11,-46],lt:[3,10.5,-50]},
  sky:()=>SK({top:C(0x060910),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111826),fd:0.0050,star:0.24,
    ms:1.05,mph:0.04,mhaze:0.12,moon:new THREE.Vector3(-24,100,-188),
    dirC:C(0x8fa4c4),dirI:0.40,ambC:C(0x182031),ambI:0.58}) },
{ name:'歌楼客舟',dwell:17,river:0.05,build:bGelouKezhou,
  cam:{f:[0.5,5.6,17.5],t:[1.2,5.3,15],lf:[-3,6.5,-24],lt:[-2.4,6.2,-26]},
  sky:()=>SK({top:C(0x060a12),hor:C(0x1a2130),bot:C(0x080b11),fog:C(0x131a26),fd:0.0060,star:0.16,
    ms:0.85,mph:0.06,mhaze:0.16,moon:new THREE.Vector3(-30,92,-195),
    dirC:C(0x9aa8ba),dirI:0.40,ambC:C(0x1a2130),ambI:0.60}) },
{ name:'僧庐天明',dwell:20,river:0.03,build:bSenglu,
  cam:{f:[0.5,5,18],t:[1,4.8,15.5],lf:[-4.5,5.4,-20],lt:[-4,5.2,-22]},
  sky:()=>SK({top:C(0x05080e),hor:C(0x131925),bot:C(0x070a0f),fog:C(0x141b28),fd:0.0072,star:0.10,
    ms:0.8,mph:0.08,mhaze:0.18,moon:new THREE.Vector3(26,96,-200),
    dirC:C(0x8ea2ba),dirI:0.36,ambC:C(0x161d29),ambI:0.54}) },
];
"""
