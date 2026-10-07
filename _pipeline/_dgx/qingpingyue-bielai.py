# -*- coding: utf-8 -*-
"""qingpingyue-bielai.py —— 《清平乐·别来春半》（五代·李煜，no.160，水墨夜思）生成配置
两境（N=queue stages 数）：砌下梅雪（落梅如雪乱·标志性瞬间「拂了一身还满」循环）、
恨如春草（雁杳梦难成·末境点击拂梅：梅雪扑落又纷回 + 春草更行更远还生）。
冷银水墨：月是唯一主角；落梅白与春草微青是全页仅有的两处色彩层次。"""

META = dict(
    N=2, slug='qingpingyue-bielai', title='清平乐·别来春半', dyn='五代 · 李煜', brand_author='李 煜',
    gold_rgb='168,188,212',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#a8bcd4; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(168,188,212,.26);
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
    tip='轻点画面 / 按空格 —— 拂梅：梅雪扑落又纷回，春草更远还生',
    hint='← → 键或空格逐境游览 · 末境可点击拂梅，看梅雪纷回、春草延展',
    cover_read='清平乐·别来春半。五代，李煜。别来春半，触目柔肠断。砌下落梅如雪乱，拂了一身还满。',
    cover_p1='两重意境，随词句次第展开：别来春半、触目柔肠断的凭栏春望；砌下落梅如雪乱、拂了一身还满的梅雪纷飞；雁来音信无凭、路遥归梦难成的长天雁杳；末了离恨恰如春草——更行更远还生。',
    cover_p2='边读词，边走进落梅如雪、离恨如草的那片月下春愁——拂了还满，愈远愈生。',
    end_h2='梅落 · 草生', cn_word='两',
    words_js="['再游一次，且看梅落','初识春半，尚需共读','渐入佳境，再诵几遍','词境渐深，雁字回时','已解离恨如春草之意','草色连天，离恨绵绵']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'砌下梅雪', jing:'别来春半，触目柔肠断 —— 砌下落梅如雪，拂了一身还满。（梅 · 雪 · 砌）',
  segs:[
   {c:'别来春半，', p:py('bié lái chūn bàn')},
   {c:'触目柔肠断。', p:py('chù mù róu cháng duàn')},
   {c:'砌下落梅如雪乱，', p:py('qì xià luò méi rú xuě luàn')},
   {c:'拂了一身还满。', p:py('fú liǎo yì shēn huán mǎn')}],
  read:'别来春半，触目柔肠断。砌下落梅如雪乱，拂了一身还满。',
  yisi:'自从分别以后，春天已过去一半；触目所见，处处令人柔肠寸断。石阶下落梅纷乱如雪，刚把满身花瓣拂拭干净，转眼又落满一身。——落梅拂了还满，离愁也正如此：挥之不去，去而复来。',
  zhu:[['春半','春天已过去一半——别后不觉时节飞逝'],['砌','台阶；砌下即石阶之下'],['落梅如雪乱','落梅纷飞，如雪片乱舞；梅开冬末春初，落梅恰是春半光景'],['了','完毕，读 liǎo——拂了：拂拭干净'],['还','仍旧、又（读 huán）——刚拂去，转眼又落满一身']] },
{ name:'恨如春草', jing:'雁来音信无凭，归梦难成 —— 离恨恰如春草，更行更远还生。（雁 · 路 · 草）',
  segs:[
   {c:'雁来音信无凭，', p:py('yàn lái yīn xìn wú píng')},
   {c:'路遥归梦难成。', p:py('lù yáo guī mèng nán chéng')},
   {c:'离恨恰如春草，', p:py('lí hèn qià rú chūn cǎo')},
   {c:'更行更远还生。', p:py('gèng xíng gèng yuǎn huán shēng')}],
  read:'雁来音信无凭，路遥归梦难成。离恨恰如春草，更行更远还生。',
  yisi:'大雁飞回来了，却没有捎来半点音信；长路迢迢，连归梦也难以做成。这离恨啊，恰如春草——人越走越远，它越是绵延生长，无边无际。——以春草的蔓生不尽，写离恨的无处不生、愈远愈深。',
  zhu:[['凭','凭据、音讯；音信无凭：雁来了，书信却没有到'],['雁','暗用「鸿雁传书」之典——古人以雁喻音信，雁至而书不至，怅惘更深'],['归梦难成','连梦中归去一趟也做不到；路遥阻了梦，也阻了人'],['更行更远还生','人越行越远，春草越远越见其绵延生长；还：仍、又（读 huán）——喻离恨之无穷']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「砌下落梅如雪乱」的下一句是？', o:['雁来音信无凭','拂了一身还满','触目柔肠断'], a:1},
 {q:'「离恨恰如春草」的下一句是？', o:['更行更远还生','路遥归梦难成','拂了一身还满'], a:0},
 {q:'「拂了一身还满」中「还」的正确读音与意思是？', o:['hái，还是、仍然','huán，仍旧、又——刚拂去又落满','huán，归还、交还'], a:1},
 {q:'「雁来音信无凭」的「雁」暗用了哪个典故？', o:['鸿雁传书——雁足系帛传信','庄周梦蝶——物我两忘','精卫填海——矢志不移'], a:0},
 {q:'结句以「春草」设喻，要表达的是？', o:['春光易逝，伤春惜时','归途遥远，行旅艰辛','离恨绵绵不尽，愈远愈生'], a:2},
];
"""

SCENES_JS = """/* ================= 清平乐·别来春半 · 两境场景（水墨夜思：砌下梅雪、恨如春草） =================
   冷银水墨：月是唯一主角；落梅白与春草微青是全页仅有的两处色彩层次，禁金。 */

/* 白梅：干 + 枝 + 白花簇（合批 1 mesh） */
function makePlumtree(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1601:o.seed);
  const h=o.h===undefined?6.4:o.h;
  const B=new GeoBag();
  const t1=new THREE.CylinderGeometry(0.11,0.24,h*0.55,7);
  t1.translate(0,h*0.275,0); t1.rotateZ((R()-0.5)*0.14); B.put(t1,0x0a0d13);
  const t2=new THREE.CylinderGeometry(0.07,0.13,h*0.52,7);
  t2.translate(0.25,h*0.55+h*0.25,0); t2.rotateZ(-0.10+(R()-0.5)*0.2); B.put(t2,0x0b0e15);
  const nb=4+Math.floor(R()*3);
  for(let i=0;i<nb;i++){
    const a=R()*6.283, len=1.7+R()*2.3;
    const br=new THREE.CylinderGeometry(0.028,0.065,len,5);
    br.translate(0,len*0.5,0);
    br.rotateZ(0.5+R()*0.55); br.rotateY(a);
    br.translate((R()-0.5)*0.6, h*(0.60+R()*0.32), (R()-0.5)*0.6);
    B.put(br,0x0b0e15);
  }
  const nf=22+Math.floor(R()*8);
  for(let i=0;i<nf;i++){
    const a=R()*6.283, rr=0.6+R()*3.2;
    const fl=new THREE.SphereGeometry(0.075+R()*0.095,6,5);
    fl.scale(1.45,0.7,1.45);
    fl.translate(Math.sin(a)*rr+(R()-0.5)*0.9, h*(0.64+R()*0.36), Math.cos(a)*rr*0.8+(R()-0.5)*0.8);
    const tint=R();
    B.put(fl,tint<0.5?0xcdd9ec:(tint<0.8?0xdde6f2:0xeef3fb));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x33405a,emissive:0x04060a}),{c:0xa8bcd4,i:0.30,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 石砌：三级石阶 + 台沿受光细边（合批 1 mesh） */
function makeQidi(o){
  o=o||{};
  const w=o.w===undefined?8.5:o.w, n=o.n===undefined?3:o.n;
  const rise=o.rise===undefined?0.52:o.rise, dd=2.2;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const top=(i+1)*rise;
    const st=new THREE.BoxGeometry(w,top,dd);
    st.translate(0,top*0.5,-i*dd);
    B.put(st,i%2?0x0c1016:0x0d1219);
    const edge=new THREE.BoxGeometry(w*1.004,0.055,dd*1.006);
    edge.translate(0,top-0.03,-i*dd);
    B.put(edge,0x151c28);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.2,p:2.3})));
  return g;
}

/* 标志性瞬间「拂了一身还满」：自定义 petal 着色器 —— 周期 P 内先两轮纷落（肩头渐积满），
   随后一阵横风把落梅自足边扬起、散向四周；风过又落，循环往复，正是离愁的具象。 */
const PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uPeriod; uniform float uSpread0;
uniform vec3 uCrown; uniform vec3 uBase;
varying float vA;
void main(){
  float G=fract(uTime/uPeriod);
  vec3 p; float a;
  if(G<0.66){
    float life=fract(G*2.0+aSeed);
    p=vec3(mix(uCrown.x,uBase.x,life*0.8), mix(uCrown.y,uBase.y,life), mix(uCrown.z,uBase.z,life*0.7));
    p.x+=(aSeed-0.5)*uSpread0 + sin(uTime*1.4+aSeed*61.0)*(0.5+2.4*life);
    p.z+=cos(uTime*1.1+aSeed*47.0)*(0.5+2.0*life);
    a=smoothstep(0.0,0.10,life)*smoothstep(1.0,0.80,life);
  }else{
    float kp=(G-0.66)/0.34;
    vec2 dir=normalize(vec2(aSeed*2.0-1.0, fract(aSeed*13.7)-0.5)+vec2(0.001,0.001));
    p=vec3(uBase.x,uBase.y,uBase.z);
    p.xz+=dir*kp*(2.5+6.5*aSeed);
    p.y+=kp*kp*(3.5+4.5*fract(aSeed*7.31));
    a=(1.0-kp)*smoothstep(0.0,0.08,kp)*0.9;
  }
  vA=a;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const PETAL_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.16,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeFumei(o){
  o=o||{};
  const n=o.n===undefined?140:o.n, P=o.period===undefined?9.0:o.period;
  const crown=o.crown||[-8.2,6.8,-10.5], base=o.base||[0.9,2.0,-4.4];
  const g=new THREE.BufferGeometry();
  const Pp=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){ S[i]=Math.random(); Z[i]=2.6+Math.random()*2.2; }
  g.setAttribute('position',new THREE.BufferAttribute(Pp,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uPeriod:{value:P},uSpread0:{value:o.spread0===undefined?8.5:o.spread0},
      uCrown:{value:new THREE.Vector3(crown[0],crown[1],crown[2])},
      uBase:{value:new THREE.Vector3(base[0],base[1],base[2])},
      uColor:{value:C(0xe9eff9)},uFade:{value:1},uMaxA:{value:o.maxA===undefined?0.85:o.maxA}},
    vertexShader:PETAL_VERT,fragmentShader:PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  const grp=new THREE.Group(); grp.add(points);
  /* 肩头积梅：两片白瓣积在肩上，随周期积满→拂去（初值=最大值，每帧乘 fadeK） */
  const sh=[];
  [[-0.52,0.10],[0.52,-0.06]].forEach(function(s){
    const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe9eff9,
      transparent:true,opacity:0.76,depthWrite:false}));
    sp.scale.set(1.15,0.6,1);
    sp.position.set(base[0]+s[0], base[1]+4.62, base[2]+s[1]);
    sp.renderOrder=3;
    grp.add(sp); sh.push(sp);
  });
  grp.update=function(t,k){
    m.uniforms.uTime.value=t;
    const G=(t/P)%1;
    const env=G<0.66?Math.min(1,G/0.20):0;
    const kk=k===undefined?1:k;
    for(let i=0;i<sh.length;i++) sh[i].material.opacity=kk*0.76*env*(0.82+0.18*Math.sin(t*0.9+i*2.1));
  };
  return {g:grp,points:points,update:grp.update};
}

/* 春草原：合批叶片（每叶带 aBase/aRank/aPhase/aTip），uSpread 让春草「更行更远还生」——
   点击后 spread 0.18→1.0，草叶沿 rank 依次立起、蔓向天际；自定义雾同步（进 fogShaders）。 */
const GRASS_VERT=`
attribute vec3 aBase; attribute float aRank; attribute float aPhase; attribute float aTip;
uniform float uTime; uniform float uSpread;
varying float vTip; varying vec3 vW;
void main(){
  float gr=smoothstep(aRank,aRank+0.14,uSpread);
  vec3 p=aBase+(position-aBase)*gr;
  p.x+=sin(uTime*1.25+aPhase)*0.38*aTip*aTip*gr;
  p.z+=cos(uTime*0.85+aPhase*1.7)*0.22*aTip*aTip*gr;
  vec4 wp=modelMatrix*vec4(p,1.0); vW=wp.xyz; vTip=aTip;
  gl_Position=projectionMatrix*viewMatrix*wp;
}`;
const GRASS_FRAG=`
uniform vec3 uCBase; uniform vec3 uCTip; uniform vec3 uFogColor; uniform float uFogDensity; uniform float uFade;
varying float vTip; varying vec3 vW;
void main(){
  vec3 col=mix(uCBase,uCTip,pow(clamp(vTip,0.0,1.0),1.5));
  float d=length(cameraPosition-vW);
  float f=1.0-exp(-uFogDensity*uFogDensity*d*d);
  col=mix(col,uFogColor,clamp(f,0.0,1.0));
  gl_FragColor=vec4(col,uFade);
}`;
function makeGrassfield(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1605:o.seed);
  const n=o.n===undefined?900:o.n, z0=o.z0===undefined?8:o.z0, z1=o.z1===undefined?-84:o.z1;
  const roadX=o.roadX===undefined?2.2:o.roadX, gap=o.gap===undefined?4.2:o.gap;
  const pos=[],base=[],rank=[],phase=[],tip=[],idx=[];
  let vi=0;
  for(let i=0;i<n;i++){
    const rk=Math.pow(R(),1.25);
    const z=z0+(z1-z0)*rk;
    let x=(R()-0.5)*2*(4.5+30*rk)+roadX*rk;
    if(z<6&&Math.abs(x-roadX)<gap){ x=roadX+gap*(x<roadX?-1:1)*(0.2+R()*2.2); }
    const hgt=0.6+R()*1.0, ph=R()*6.283, rot=R()*3.14;
    const bl=new THREE.PlaneGeometry(0.13,hgt,1,2);
    bl.translate(0,hgt*0.5,0);
    bl.rotateZ((R()-0.5)*0.5); bl.rotateY(rot);
    const pa=bl.attributes.position;
    for(let v=0;v<pa.count;v++){
      pos.push(pa.getX(v)+x,pa.getY(v),pa.getZ(v));
      base.push(x,0,0);
      rank.push(rk); phase.push(ph);
      tip.push(pa.getY(v)/hgt);
    }
    const ia=bl.index.array;
    for(let k=0;k<ia.length;k++) idx.push(ia[k]+vi);
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
    uniforms:{uTime:{value:0},uSpread:{value:o.spread0===undefined?0.18:o.spread0},
      uCBase:{value:C(0x0b1013)},uCTip:{value:C(0x74927e)},
      uFogColor:{value:C(0x121826)},uFogDensity:{value:0.005},uFade:{value:1}},
    vertexShader:GRASS_VERT,fragmentShader:GRASS_FRAG});
  fogShaders.push(m.uniforms);
  const mesh=new THREE.Mesh(G,m); mesh.frustumCulled=false; mesh.renderOrder=1;
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t){ m.uniforms.uTime.value=t; };
  return {g:g,mesh:mesh,mat:m,update:g.update};
}

/* 梅雪扑落又纷回：点击触发的花瓣 burst（uT0 激活）——先自上而下斜扑，再盘旋纷回、散而复上 */
const BURST_VERT=`
attribute float aSeed; attribute float aSize; attribute vec3 aDir;
uniform float uTime; uniform float uT0;
varying float vA;
void main(){
  float age=uTime-uT0;
  vec3 p=position; float a=0.0;
  if(age>0.0&&age<7.5){
    if(age<3.2){
      float k=age/3.2;
      p.y-=k*k*10.5;
      p.x+=aDir.x*k*4.5+sin(uTime*2.0+aSeed*40.0)*0.55;
      p.z+=aDir.z*k*3.0+cos(uTime*1.7+aSeed*29.0)*0.45;
      a=smoothstep(0.0,0.05,age)*(1.0-k*0.30);
    }else{
      float kp=(age-3.2)/4.3;
      p.y+=-10.5+kp*kp*(9.5+6.0*aSeed)+kp*1.5;
      p.x+=aDir.x*4.5*(1.0+kp*0.8)+sin(uTime*1.6+aSeed*57.0)*(0.8+kp*2.4);
      p.z+=aDir.z*3.0*(1.0+kp*0.8)+cos(uTime*1.3+aSeed*33.0)*(0.7+kp*1.8);
      a=(1.0-kp)*smoothstep(0.0,0.10,kp)*0.9;
    }
  }
  vA=a;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeMeixueBurst(o){
  o=o||{};
  const n=o.n===undefined?150:o.n, box=o.box||[16,5,10], pos0=o.pos||[-2,15,-12];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),D=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos0[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos0[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos0[2]+(Math.random()-0.5)*box[2];
    const a=Math.random()*6.283;
    D[i*3]=Math.cos(a); D[i*3+1]=0; D[i*3+2]=Math.sin(a);
    S[i]=Math.random(); Z[i]=2.8+Math.random()*2.4;
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aDir',new THREE.BufferAttribute(D,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uT0:{value:-999},uColor:{value:C(0xeef3fb)},uFade:{value:1},uMaxA:{value:0.9}},
    vertexShader:BURST_VERT,fragmentShader:PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  const grp=new THREE.Group(); grp.add(points);
  let lastT=0;
  grp.update=function(t){ lastT=t; m.uniforms.uTime.value=t; };
  grp.fire=function(){ m.uniforms.uT0.value=lastT; };
  return {g:grp,points:points,update:grp.update,fire:grp.fire};
}

/* 雁阵：一列雁影掠月而行（合批 1 mesh，缓慢横渡） */
function makeGeese(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?1607:o.seed);
  const n=o.n===undefined?7:o.n;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const t=i/(n-1)-0.5, x=t*11.0, zOff=Math.abs(t)*3.4, s=0.8+R()*0.25;
    const w1=new THREE.BoxGeometry(1.5*s,0.05,0.34*s);
    w1.rotateZ(0.30); w1.translate(x-0.72*s,R()*0.5,zOff);
    const w2=new THREE.BoxGeometry(1.5*s,0.05,0.34*s);
    w2.rotateZ(-0.30); w2.translate(x+0.72*s,R()*0.5,zOff);
    B.put(w1,0x05070b); B.put(w2,0x05070b);
  }
  const g=new THREE.Group();
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x11151d,emissive:0x020304}));
  mesh.frustumCulled=false; g.add(mesh);
  const sp=o.speed===undefined?1.35:o.speed, span=o.span===undefined?90:o.span;
  g.update=function(t){
    g.position.x=-span*0.5+((t*sp)%span);
    g.position.y=(o.y===undefined?26:o.y)+Math.sin(t*0.5)*0.8;
  };
  return {g:g,mesh:mesh,update:g.update};
}

function bCover(){ // 封面 · 春半夜静
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:1600,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const tree=makePlumtree({seed:1601,h:6.0}); tree.position.set(11,0,-16); tree.scale.setScalar(1.25); g.add(tree);
  const figure=makeFigure({pose:'独立',robe:0x242e40,belt:0x5f6e86,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xa8bcd4,rim:0.4,noProp:true,scale:1.9});
  figure.position.set(-3.5,0,2); figure.rotation.y=0.5; g.add(figure);
  const mist=makeMist({n:9,spread:[250,34,160],pos:[0,12,-58],scale:82,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[210,40,120],pos:[0,10,-36],color:0xbcc9dc,size:7,speed:0.05,rise:0,maxA:0.34});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:9,color:0x04060a,seed:1602,rim:0.14});
  rk.g.position.set(0,-2,25); g.add(rk.g);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    rk.update(t,k); figure.update(t,k);
  }};
}

function bLuomei(){ // 一 · 砌下梅雪 —— 落梅如雪乱，拂了一身还满（标志性瞬间：拂了还满的循环）
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-0.02; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:18,layers:2,peaks:4,seed:1600,color:0x070a10,atmo:0x1c2637,fogK:0.62,glowK:0.06,y:-14});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 石砌 + 白梅两株 + 立于砌上的人 */
  const qidi=makeQidi({w:8.5,n:3}); qidi.position.set(0,0,-2.2); g.add(qidi);
  const tree=makePlumtree({seed:1601}); tree.position.set(-8.2,0,-10.5); g.add(tree);
  const tree2=makePlumtree({seed:1611,h:5.2}); tree2.position.set(11.5,0,-14); tree2.scale.setScalar(0.9); g.add(tree2);
  const figure=makeFigure({pose:'独立',robe:0x2a3548,belt:0x64748e,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xa8bcd4,rim:0.5,noProp:true,scale:1.5});
  figure.position.set(0.9,1.56,-4.4); figure.rotation.y=0.12; g.add(figure);
  /* 标志性瞬间：落梅纷落积肩 → 一阵风拂起扬散 → 转眼又落满（循环往复的离愁具象） */
  const fumei=makeFumei({crown:[-8.2,6.8,-10.5],base:[0.9,2.2,-4.4]});
  g.add(fumei.g);
  /* 砌下落花：地面残梅缓缓明灭 */
  const fallen=makeGlow({n:46,box:[15,0.5,9],pos:[-2.5,0.8,-6.5],color:0xe9eff9,size:4.2,speed:0.03,rise:0,maxA:0.32});
  g.add(fallen.points);
  const motes=makeGlow({n:56,box:[64,12,36],pos:[2,5,-9],color:0xbcc9dc,size:5,speed:0.06,rise:0.1,maxA:0.28});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[200,20,110],pos:[0,8,-48],scale:72,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:8,color:0x04060a,seed:1603,rim:0.14});
  rk.g.position.set(13.5,-1.2,11.5); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x04060a,seed:1604,sway:0.8});
  reeds.g.position.set(-13,-1.3,10.5); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.52,p:[-30,90,-40]},{c:0x1a2232,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); fallen.update(t); motes.update(t);
    rk.update(t,k); reeds.update(t,k); fumei.update(t,k); figure.update(t,k);
  }};
}

function bChuncao(){ // 二（末境可点击）· 恨如春草 —— 雁杳梦难成；点击拂梅：梅雪扑落又纷回、春草更远还生
  const g=new THREE.Group();
  const ctl={t:0,last:-9,clicked:false,spread:0.30,spreadOn:false};
  const grd=makeGround({r:170,c1:0x070a0d,c2:0x0e1319});
  grd.mesh.position.y=-0.05; g.add(grd.mesh);
  const ridge=makeRange({r:260,h:14,layers:2,peaks:3,seed:1606,color:0x070a0f,atmo:0x1e2a38,fogK:0.58,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 长路：路遥归梦难成 */
  const road=new THREE.Mesh(new THREE.PlaneGeometry(7.5,150),
    new THREE.MeshPhongMaterial({color:0x0e131a,shininess:14,specular:0x2c3850}));
  road.rotation.x=-Math.PI/2; road.rotation.z=0.02; road.position.set(2.2,0.04,-56); g.add(road);
  /* 春草原：uSpread 点击后 0.30→1.0，春草「更行更远还生」 */
  const grass=makeGrassfield({n:900,z0:8,z1:-84,roadX:2.2,gap:4.2,spread0:0.30});
  g.add(grass.g);
  /* 雁来音信无凭：一列雁影掠月横渡 */
  const geese=makeGeese({n:7,y:26,speed:1.35,span:90}); geese.g.position.set(0,26,-85); g.add(geese.g);
  /* 长路尽头极远处的归人影（可望不可即） */
  const walker=makeCrowd({n:1,rect:[1.8,-50,0.8,2.0],seed:1608,color:0x0e131b,rimC:0x8fa4c4,rim:0.16,sMin:0.5,sMax:0.6});
  g.add(walker.mesh);
  /* 立于草原之前望归路的词人 */
  const figure=makeFigure({pose:'独立',robe:0x25303f,belt:0x5f6e86,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xa8bcd4,rim:0.48,noProp:true,scale:1.4});
  figure.position.set(-4.5,0,-9); figure.rotation.y=0.42; g.add(figure);
  /* 梅雪扑落又纷回（点击触发） */
  const burst=makeMeixueBurst({n:150,pos:[-2,15,-12],box:[16,5,10]});
  g.add(burst.g);
  const motes=makeGlow({n:50,box:[80,14,50],pos:[0,6,-16],color:0xbcc9dc,size:5,speed:0.05,rise:0.08,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,22,120],pos:[0,8,-58],scale:80,color:0x7e8ea8,op:0.09});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',w:30,n:16,d:6,color:0x04060a,seed:1609,sway:1.0});
  reeds.g.position.set(-12,-0.7,20); g.add(reeds.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:1610,sway:1.2,rim:0.16});
  tree.g.position.set(15,-0.5,23); g.add(tree.g);
  addLights(g,{c:0x8fa4c8,i:0.48,p:[-20,80,-60]},{c:0x1a2232,i:0.66});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.spreadOn)ctl.spread=Math.min(1,ctl.spread+dt/5.5);
      grass.mat.uniforms.uSpread.value=ctl.spread;
      ridge.update(t,0); mist.update(t,k); motes.update(t); burst.update(t);
      geese.update(t); walker.update(t); grass.update(t);
      reeds.update(t,k); tree.update(t,k); figure.update(t,k);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.2)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      ctl.spreadOn=true;
      burst.fire();
      pluck(2,0.0,0.12); pluck(4,0.45,0.10); pluck(1,0.95,0.09);
      const fl=$('#flash'); fl.textContent='更行更远还生';
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
  cam:{f:[0,9,60],t:[0,9.5,54],lf:[0,13,-42],lt:[0,13,-42]},
  sky:()=>SK({top:C(0x060910),hor:C(0x141c2a),bot:C(0x080b11),fog:C(0x0f1520),fd:0.0048,star:0.45,
    ms:1.6,moon:new THREE.Vector3(20,100,-180),
    dirC:C(0x8fa4c8),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'砌下梅雪',dwell:16,river:0.02,build:bLuomei,
  cam:{f:[0,4.6,16],t:[0.8,4.4,13.5],lf:[-2.5,5.5,-10],lt:[-0.5,5.2,-13]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0058,star:0.5,
    ms:1.9,mph:0,mhaze:0.05,moon:new THREE.Vector3(34,110,-185),
    dirC:C(0x8fa4c8),dirI:0.52,ambC:C(0x1a2232),ambI:0.64}) },
{ name:'恨如春草',dwell:17,river:0.02,build:bChuncao,
  cam:{f:[0,7,26],t:[0,7.5,22],lf:[0,8.5,-34],lt:[1.5,9,-42]},
  sky:()=>SK({top:C(0x090c12),hor:C(0x1a2331),bot:C(0x0a0d13),fog:C(0x121a26),fd:0.0074,star:0.32,
    ms:1.75,mph:0.12,mhaze:0.04,moon:new THREE.Vector3(-44,104,-195),
    dirC:C(0x93a7c2),dirI:0.48,ambC:C(0x1b2431),ambI:0.66}) },
];
"""
