# -*- coding: utf-8 -*-
"""changxiangsi-yichongshan.py —— 《长相思·一重山》（五代·李煜，no.161，宣纸留白）生成配置
两境（N=queue stages 数）：叠山枫丹（一重山两重山·烟水寒处一点丹）、
雁字风月（菊开菊残·塞雁人未还·末境点击「万山褪墨唯枫独染」）。
宣纸留白：浅纸底、浓墨叠山推远、枫丹是全页唯一浓彩；点击后万山墨色尽数褪入留白。"""

META = dict(
    N=2, slug='changxiangsi-yichongshan', title='长相思·一重山', dyn='五代 · 李煜', brand_author='李 煜',
    gold_rgb='74,80,96',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#4a5060; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(74,80,96,.26);
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
    tip='轻点画面 / 按空格 —— 万山褪墨，唯枫独染',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看万山褪墨、唯枫独染',
    cover_read='长相思·一重山。五代，李煜。一重山，两重山。山远天高烟水寒，相思枫叶丹。',
    cover_p1='两重意境，随词句次第展开：一重山、两重山的叠嶂远天；山远天高烟水寒的秋江寒烟；相思枫叶丹的一点丹红；菊花开、菊花残的篱畔秋声；塞雁高飞人未还的长天雁字；末了一帘风月闲的帘外清风明月。',
    cover_p2='边读词，边走进那幅淡墨秋思——万重山色皆可褪作留白，唯余相思一点枫丹。',
    end_h2='山远 · 枫丹', cn_word='两',
    words_js="['再游一次，且看枫丹','初识后主，尚需共读','渐入佳境，再诵几遍','词境渐深，雁字回时','已解万山褪墨之意','一帘风月，唯枫独染']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = """const POEM = [
{ name:'叠山枫丹', jing:'一重山，两重山 —— 山远天高烟水寒，相思枫叶丹。（山 · 水 · 枫）',
  segs:[
   {c:'一重山，', p:py('yī chóng shān')},
   {c:'两重山。', p:py('liǎng chóng shān')},
   {c:'山远天高烟水寒，', p:py('shān yuǎn tiān gāo yān shuǐ hán')},
   {c:'相思枫叶丹。', p:py('xiāng sī fēng yè dān')}],
  read:'一重山，两重山。山远天高烟水寒，相思枫叶丹。',
  yisi:'一重山，又一重山，山峦层层叠叠，望不到尽头。山那么远，天那么高，烟云水气又冷又寒，可我的思念，却像枫叶一样红到了极处。——以叠山之远、烟水之寒，衬相思之炽：景愈冷，情愈热。',
  zhu:[['重','量词「层」，读 chóng——一重山即一层山，叠言其多，望之不尽'],['山远天高','山在远处绵延，天在高处辽阔——望不见的阻隔，正是思而不得的空间写照'],['烟水寒','烟雾笼着江水，透出秋意之寒；「寒」既是水汽之冷，也是心境之清冷'],['枫叶丹','枫叶红到极处；丹：红色——以枫叶之丹喻相思之炽，是全词最暖的一点颜色']] },
{ name:'雁字风月', jing:'菊花开，菊花残 —— 塞雁高飞人未还，一帘风月闲。（菊 · 雁 · 帘）',
  segs:[
   {c:'菊花开，', p:py('jú huā kāi')},
   {c:'菊花残。', p:py('jú huā cán')},
   {c:'塞雁高飞人未还，', p:py('sài yàn gāo fēi rén wèi huán')},
   {c:'一帘风月闲。', p:py('yī lián fēng yuè xián')}],
  read:'菊花开，菊花残。塞雁高飞人未还，一帘风月闲。',
  yisi:'菊花开了一次，又凋残了一次，年复一年。塞外的大雁高高飞过，人却还没有回来；唯有帘外的清风明月，悠来荡去，闲得让人心慌。——以风月之「闲」反衬人心之切，以雁之按时归来反衬人之无音无信。',
  zhu:[['菊花开，菊花残','菊开了又谢，暗写光阴流转、盼归之久——不说「年年」，而年年在其中'],['塞雁','塞外南来的雁阵；雁是候鸟，秋来有信，人却无音——「塞」读 sài'],['人未还','雁尚且按时归来，远人却一去未返；「未还」二字，是全词的叹息所在'],['一帘风月闲','帘外清风明月自在悠荡；闲：清闲、安静——以风月之闲，写人不能闲的相思']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「一重山，两重山」的下一句是？', o:['山远天高烟水寒','菊花开，菊花残','塞雁高飞人未还'], a:0},
 {q:'「塞雁高飞人未还」的下一句是？', o:['一帘风月闲','相思枫叶丹','山远天高烟水寒'], a:0},
 {q:'「一重山，两重山」中「重」的正确读音与意思是？', o:['zhòng，沉重、重要','chóng，量词「层」——一层层的山','cóng，跟随、随从'], a:1},
 {q:'「塞雁高飞人未还」以雁反衬人，妙在何处？', o:['鸿雁秋来有信，雁归而人未归——以雁之守信反衬人之无音','大雁南飞只是天气转冷的标志，与人事无关','古人以雁喻隐士，指远人去隐居了'], a:0},
 {q:'结句「一帘风月闲」的「闲」，要表达的是？', o:['词人闲适自得、无所事事','以风月之闲反衬人心之切——景越闲，思越乱','埋怨清风明月太悠闲、不解人意'], a:1},
];
"""

SCENES_JS = """/* ================= 长相思·一重山 · 两境场景（宣纸留白：叠山枫丹、雁字风月） =================
   浅纸为天、浓墨作山，大量留白；枫丹是全页唯一浓彩。末境点击：万山褪墨，唯枫独染。 */

/* 枫树 makeMaple(o) —— 干 + 枝 + 丹叶簇（合批 1 mesh）+ 冠后丹晕 sprite（全页唯一浓彩） */
function makeMaple(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2613:o.seed);
  const h=o.h===undefined?6.0:o.h;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.10,0.22,h*0.5,7);
  trunk.translate(0,h*0.25,0); trunk.rotateZ((R()-0.5)*0.12); B.put(trunk,0x33281e);
  const nb=5+Math.floor(R()*3);
  for(let i=0;i<nb;i++){
    const a=R()*6.283, len=1.6+R()*2.1;
    const br=new THREE.CylinderGeometry(0.025,0.06,len,5);
    br.translate(0,len*0.5,0); br.rotateZ(0.55+R()*0.6); br.rotateY(a);
    br.translate((R()-0.5)*0.5, h*(0.42+R()*0.36), (R()-0.5)*0.5);
    B.put(br,0x33281e);
  }
  const nf=o.leafN===undefined?26:o.leafN;
  const reds=[0x8c2a1c,0xa83526,0xa83526,0xc14b30,0xd4583a];
  const crownY0=h*0.56, crownR=o.crownR===undefined?2.1:o.crownR, crownH=h*0.44;
  for(let i=0;i<nf;i++){
    const a=R()*6.283, rr=Math.pow(R(),0.6)*crownR;
    const fl=new THREE.SphereGeometry(0.10+R()*0.16,6,5);
    fl.scale(1.4,0.72,1.4);
    fl.translate(Math.sin(a)*rr, crownY0+(1-rr/crownR)*crownH*(0.35+0.65*R()), Math.cos(a)*rr*0.85);
    B.put(fl,reds[Math.floor(R()*reds.length)]);
  }
  /* 根下落丹数点 */
  for(let i=0;i<6;i++){
    const lf=new THREE.SphereGeometry(0.07+R()*0.05,5,4);
    lf.scale(1.5,0.3,1.2);
    lf.translate((R()-0.5)*crownR*1.6, 0.06, (R()-0.5)*crownR*1.3);
    B.put(lf,reds[Math.floor(R()*3)]);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a332c,emissive:0x140604}),{c:0xf0ead8,i:0.16,p:2.2})));
  /* 冠后丹晕：初始即最大值，逐帧只在其下浮动（fadeK 铁律） */
  const haloMax=o.haloMax===undefined?0.5:o.haloMax;
  const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc14b30,
    transparent:true,opacity:haloMax,depthWrite:false}));
  sp.scale.set(crownR*4.6,crownR*3.4,1);
  sp.position.set(0,crownY0+crownH*0.4,0.25); sp.renderOrder=2;
  g.add(sp); g.userData.halo=sp; g.userData.haloMax=haloMax;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 江渚 makeIslet(o) —— 水中石渚（合批 1 mesh） */
function makeIslet(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2612:o.seed);
  const B=new GeoBag(), n=o.n===undefined?4:o.n;
  for(let i=0;i<n;i++){
    const rr=(o.r===undefined?1.5:o.r)*(0.5+0.9*R());
    const rg=rockGeo(rr,1,R);
    rg.translate((R()-0.5)*(o.w===undefined?3.2:o.w), rr*0.22, (R()-0.5)*(o.d===undefined?2.4:o.d));
    B.put(rg,i%2?0x2c2f33:0x23262b);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2a26,emissive:0x0a0a08}),{c:0xf0ead8,i:0.12,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 篱菊 makeChrys(o) —— mode:'开'|'残'（合批 1 mesh；纸黄淡彩，不与枫丹争色） */
function makeChrys(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2623:o.seed);
  const open=o.mode!=='残';
  const nStem=open?9:6;
  const B=new GeoBag();
  for(let i=0;i<nStem;i++){
    const x=(R()-0.5)*(open?1.7:1.3), z=(R()-0.5)*1.1;
    const hh=(open?1.15:0.95)*(0.55+0.6*R());
    const tilt=(R()-0.5)*(open?0.24:0.85);
    const st=new THREE.CylinderGeometry(0.022,0.045,hh,5);
    st.translate(0,hh*0.5,0); st.rotateZ(tilt); st.translate(x,0,z);
    B.put(st,open?0x6b7052:0x6e6148);
    const lf=new THREE.SphereGeometry(0.10+R()*0.07,5,4);
    lf.scale(1.7,0.35,0.9); lf.rotateZ(tilt+(R()-0.5)*0.6);
    lf.translate(x+(R()-0.5)*0.3, hh*(0.3+0.4*R()), z+(R()-0.5)*0.3);
    B.put(lf,open?0x5a6148:0x5c5342);
    const hd=new THREE.SphereGeometry(open?0.17+R()*0.09:0.10+R()*0.06,7,5);
    hd.scale(1.25,0.62,1.25); hd.rotateZ(tilt*1.4);
    hd.translate(x,hh+(open?0.05:-0.10),z);
    B.put(hd,open?(R()<0.75?0xd8cda0:0xcfc093):(R()<0.7?0x8a7a5c:0x6e6148));
    const ct=new THREE.SphereGeometry(open?0.06:0.045,5,4);
    ct.translate(x,hh+(open?0.10:-0.02),z);
    B.put(ct,open?0x9a7c3f:0x57503c);
  }
  if(!open){
    for(let i=0;i<5;i++){
      const p=new THREE.SphereGeometry(0.07,5,4);
      p.scale(1.5,0.3,1.2);
      p.translate((R()-0.5)*1.6,0.05,(R()-0.5)*1.4);
      B.put(p,0x8a7a5c);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a382e,emissive:0x0e0d08})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 塞雁 makeGeese(o) —— 一列雁字掠天（合批 1 mesh，缓慢横渡） */
function makeGeese(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2614:o.seed);
  const n=o.n===undefined?7:o.n;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const t=i/(n-1)-0.5, x=t*12.5, zOff=Math.abs(t)*4.2, yOff=Math.abs(t)*1.4, s=0.85+R()*0.3;
    const w1=new THREE.BoxGeometry(1.7*s,0.06,0.36*s);
    w1.rotateZ(0.24); w1.translate(x-0.80*s,yOff,zOff);
    const w2=new THREE.BoxGeometry(1.7*s,0.06,0.36*s);
    w2.rotateZ(-0.24); w2.translate(x+0.80*s,yOff,zOff);
    B.put(w1,0x2c2f33); B.put(w2,0x2c2f33);
  }
  const g=new THREE.Group();
  const mesh=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x22252a,emissive:0x0a0b0e}));
  mesh.frustumCulled=false; g.add(mesh);
  const sp=o.speed===undefined?1.05:o.speed, span=o.span===undefined?120:o.span;
  const z0=o.z===undefined?-70:o.z;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.update=function(t){
    g.position.x=-span*0.5+((t*sp)%span);
    g.position.y=(o.y===undefined?30:o.y)+Math.sin(t*0.4)*0.9;
    g.position.z=z0;
  };
  return {g:g,update:g.update};
}

/* 帘 makeLian(o) —— 弧面帘幕 + 帘杆，轻摆（一帘风月闲） */
function makeLian(o){
  o=o||{};
  const h=o.h===undefined?4.8:o.h, r=o.r===undefined?2.5:o.r;
  const g=new THREE.Group();
  const rod=new THREE.Mesh(new THREE.CylinderGeometry(0.035,0.035,r*1.6,8),
    new THREE.MeshPhongMaterial({color:0x4a3a2c,shininess:12,specular:0x6a563e}));
  rod.rotation.z=Math.PI/2; rod.position.y=h; g.add(rod);
  const cloth=new THREE.Mesh(new THREE.CylinderGeometry(r,r,h,26,1,true,-1.05,2.1),
    new THREE.MeshPhongMaterial({color:0xe9e3d2,shininess:4,specular:0x8a8574,
      side:THREE.DoubleSide,transparent:true,opacity:0.92}));
  cloth.position.y=h*0.5; g.add(cloth);
  const sw=o.sway===undefined?0.05:o.sway;
  g.update=function(t){
    cloth.rotation.y=Math.sin(t*0.5)*sw*3;
    cloth.scale.x=1+0.045*Math.sin(t*0.8);
    rod.rotation.x=Math.sin(t*0.5)*0.012;
  };
  return {g:g,update:g.update};
}

/* 枫叶纷飞 makeLeafBurst(o)：点击触发（uT0 激活）——丹叶自冠升扬、旋舞而下 */
const LEAF_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uT0;
varying float vA;
void main(){
  float age=uTime-uT0;
  vec3 p=position; float a=0.0;
  if(age>0.0&&age<8.0){
    float k=age/8.0;
    float sw=aSeed*6.283;
    p.y+=(1.0-k)*3.0-k*k*7.2;
    p.x+=sin(uTime*1.1+sw)*(0.4+k*3.4)+(aSeed-0.5)*3.2*k;
    p.z+=cos(uTime*0.9+sw*1.7)*(0.4+k*2.6);
    a=(1.0-k)*smoothstep(0.0,0.06,age);
  }
  vA=a;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const LEAF_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.12,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLeafBurst(o){
  o=o||{};
  const n=o.n===undefined?110:o.n, crown=o.crown||[10.5,5.0,-15];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=crown[0]+(Math.random()-0.5)*2.6;
    P[i*3+1]=crown[1]+(Math.random()-0.5)*1.6;
    P[i*3+2]=crown[2]+(Math.random()-0.5)*2.2;
    S[i]=Math.random(); Z[i]=2.4+Math.random()*2.0;
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uT0:{value:-999},uColor:{value:C(0xb8402a)},uFade:{value:1},uMaxA:{value:o.maxA===undefined?0.85:o.maxA}},
    vertexShader:LEAF_VERT,fragmentShader:LEAF_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  const grp=new THREE.Group(); grp.add(points);
  let lastT=0;
  grp.update=function(t){ lastT=t; m.uniforms.uTime.value=t; };
  grp.fire=function(){ m.uniforms.uT0.value=lastT; };
  return {g:grp,update:grp.update,fire:grp.fire};
}

function bCover(){ // 卷首 · 宣纸秋远，万山深处藏一点丹
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d3,c2:0xdcd4bd,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:64,layers:3,peaks:6,seed:2600,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-88); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:180,h:30,layers:2,peaks:4,seed:2602,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-6,order:-5});
  ridge2.g.position.set(6,0,-40); ridge2.g.rotation.y=Math.PI*1.05; g.add(ridge2.g);
  const islet=makeIslet({seed:2603,r:1.3,n:3,w:2.8,d:2.2});
  islet.position.set(-7.5,-0.9,-26); g.add(islet);
  const maple=makeMaple({seed:2604,h:5.0,crownR:1.8});
  maple.position.set(-7.5,-0.35,-26); g.add(maple);
  const mist=makeMist({n:9,spread:[280,30,150],pos:[0,9,-64],scale:84,color:0xe6dfcc,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[220,34,120],pos:[0,12,-40],color:0xb8bcc2,size:4,speed:0.04,
    rise:0.06,add:false,maxA:0.22});
  g.add(motes.points);
  const reeds=makeForeground({kind:'芦苇',w:40,n:18,d:8,color:0x2c2f33,seed:2605,sway:1.0,tip:0x4a4f56});
  reeds.g.position.set(8,-1.5,34); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[60,120,40]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t); reeds.update(t,k);
    const halo=maple.userData.halo;
    if(halo)halo.material.opacity=k*maple.userData.haloMax*(0.34+0.08*Math.sin(t*0.7));
  }};
}

function bYanshui(){ // 一 · 叠山枫丹 —— 一重山两重山，烟水寒处一点丹（标志性瞬间铺垫）
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:88,amp:0.30,freq:0.085,speed:0.48,flow:[0.12,0.18],spec:0.7,
    deep:0x8a9094,shallow:0xb8bcb4,skyc:0xd6d2c0,moonDir:[0.3,1,0.25]});
  g.add(water.mesh);
  /* 背景：三重淡墨远山（愈远愈淡）——一重山，两重山…… */
  const ridge=makeRange({r:280,h:84,layers:3,peaks:6,seed:2601,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.58,glowK:0.045,glow:0xf4eeda,y:-6});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 近山浓墨一层压角 */
  const ridge2=makeRange({r:180,h:42,layers:2,peaks:5,seed:2611,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-4,order:-5});
  ridge2.g.position.set(-14,0,-30); ridge2.g.rotation.y=Math.PI*1.04; g.add(ridge2.g);
  /* 江渚枫树：万山烟水中唯一点丹 */
  const islet=makeIslet({seed:2612,r:1.5,n:4,w:3.4,d:2.6});
  islet.position.set(8.2,-0.15,-10.5); g.add(islet);
  const maple=makeMaple({seed:2613,h:6.2,crownR:2.2});
  maple.position.set(8.2,0.45,-10.5); maple.rotation.y=-0.5; g.add(maple);
  /* 烟水寒：暖纸色雾霭 + 一缕寒烟横流 */
  const mist=makeMist({n:8,spread:[260,26,140],pos:[0,7,-56],scale:80,color:0xe0d8c2,op:0.11});
  g.add(mist.g);
  const flow=makeFlow({n:460,box:[180,16,90],pos:[0,5.5,-44],color:0xa8adb5,size:20,speed:3.2,maxA:0.26});
  g.add(flow.points);
  const motes=makeGlow({n:46,box:[90,14,50],pos:[0,6,-20],color:0xb8bcc2,size:4,speed:0.05,
    rise:0.08,add:false,maxA:0.22});
  g.add(motes.points);
  /* 水面流丹数点（水流红叶） */
  const drift=makeGlow({n:14,box:[10,0.6,7],pos:[7.5,0.55,-9.5],color:0xa83526,size:3.2,speed:0.05,
    rise:0,add:false,maxA:0.5});
  g.add(drift.points);
  /* 前景：坡石 + 枯苇框住画缘 */
  const rk=makeForeground({kind:'坡石',n:3,r:2.9,w:18,d:7,color:0x23262b,seed:2616,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(18,-2.0,14); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:12,d:6,color:0x2c2f33,seed:2617,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(-19,-1.5,16); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[50,110,40]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); ridge2.update(t,0);
    mist.update(t,k); flow.update(t); motes.update(t); drift.update(t);
    rk.update(t,k); reeds.update(t,k);
    const halo=maple.userData.halo;
    if(halo)halo.material.opacity=k*maple.userData.haloMax*(0.32+0.08*Math.sin(t*0.8));
  }};
}

function bYanlian(){ // 二（末境·可点击）· 雁字风月 —— 菊开菊残、塞雁人未还；点击：万山褪墨唯枫独染
  const g=new THREE.Group();
  const ctl={t:0,last:-9,clicked:false,ink:0,fading:false};
  const grd=makeGround({r:250,c1:0xe9e3d3,c2:0xdcd4bd,y:-1.5}); g.add(grd.mesh);
  /* 背景：淡墨叠山两层 —— 点击后尽数褪入宣纸 */
  const ridge=makeRange({r:270,h:70,layers:3,peaks:6,seed:2621,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-92); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:170,h:34,layers:2,peaks:4,seed:2622,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-5,order:-5});
  ridge2.g.position.set(0,0,-34); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  /* 褪墨：存下各层原色，点击后向宣纸色渐染 */
  const inkLayers=[];
  [ridge,ridge2].forEach(function(rg){ rg.items.forEach(function(it){
    inkLayers.push({u:it.mesh.material.uniforms,
      low0:it.mesh.material.uniforms.uLow.value.clone(),
      high0:it.mesh.material.uniforms.uHigh.value.clone()});
  });});
  const paperLow=C(0xded6c2), paperHigh=C(0xefe9d8);
  /* 篱畔双菊：一丛开、一丛残 */
  const chrys1=makeChrys({mode:'开',seed:2623}); chrys1.position.set(-7.5,-1.5,-7.5); chrys1.scale.setScalar(1.6); g.add(chrys1);
  const chrys2=makeChrys({mode:'残',seed:2624}); chrys2.position.set(2.8,-1.5,-5.5); chrys2.scale.setScalar(1.35); g.add(chrys2);
  /* 相思枫叶丹（自上境延续）：右侧一株枫 —— 褪墨后唯它独染 */
  const maple=makeMaple({seed:2613,h:6.6,crownR:2.3});
  maple.position.set(10.5,-1.3,-15); maple.rotation.y=0.4; g.add(maple);
  /* 塞雁高飞：一列雁字横渡长天（飞在近山之前，高而可见） */
  const geese=makeGeese({n:7,y:15.5,z:-30,speed:0.7,span:60,scale:1.15}); g.add(geese.g);
  /* 人未还：独立望远的伊人（衣取 accent 墨青）+ 极远处未归的行影 */
  const figure=makeFigure({pose:'独立',robe:0x4a5060,belt:0x2c2f33,skin:0xcbb9a2,collar:0xe8e2d0,
    hat:'发髻',rimC:0xe8e2d0,rim:0.3,noProp:true,scale:1.2});
  figure.position.set(-5.5,-1.5,-7.5); figure.rotation.y=0.5; g.add(figure);
  const walker=makeCrowd({n:2,rect:[26,-64,10,8],seed:2625,color:0x3a3d44,rimC:0xe8e2d0,rim:0.14,
    sMin:0.5,sMax:0.62});
  g.add(walker.mesh);
  /* 一帘风月闲：帘幕轻摆于画右 */
  const lian=makeLian({h:4.4,r:2.1,sway:0.05}); lian.g.position.set(10.8,-1.5,6.5); lian.g.rotation.y=-0.85; g.add(lian.g);
  /* 点击触发：丹叶纷飞 */
  const leafBurst=makeLeafBurst({n:110,crown:[10.5,5.0,-15]}); g.add(leafBurst.g);
  const motes=makeGlow({n:46,box:[90,14,52],pos:[0,6,-18],color:0xb8bcc2,size:4,speed:0.05,
    rise:0.08,add:false,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,24,130],pos:[0,8,-64],scale:78,color:0xe0d8c2,op:0.10});
  g.add(mist.g);
  /* 前景：坡石 + 枯苇框住画缘 */
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:20,d:7,color:0x23262b,seed:2626,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(-16,-1.8,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:34,n:14,d:6,color:0x2c2f33,seed:2627,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(-8,-1.6,17); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[-30,100,-30]},{c:0xd8d2c0,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.fading)ctl.ink=Math.min(1,ctl.ink+dt/5.0);
      if(ctl.ink>0){
        const kk=1-Math.pow(1-ctl.ink,2.2);
        for(let i=0;i<inkLayers.length;i++){ const L=inkLayers[i];
          L.u.uLow.value.copy(L.low0).lerp(paperLow,kk);
          L.u.uHigh.value.copy(L.high0).lerp(paperHigh,kk); }
      }
      ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t);
      geese.update(t); walker.update(t); lian.update(t);
      rk.update(t,k); reeds.update(t,k); figure.update(t,k); leafBurst.update(t);
      const halo=maple.userData.halo;
      if(halo)halo.material.opacity=k*maple.userData.haloMax*
        (ctl.fading?(0.62+0.16*ctl.ink):(0.32+0.08*Math.sin(t*0.8)));
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.2)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      ctl.fading=true;
      leafBurst.fire();
      pluck(2,0.0,0.12); pluck(4,0.45,0.10); pluck(1,0.95,0.09);
      const fl=$('#flash'); fl.textContent='万山褪墨 唯枫独染';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.06,
  moon:new THREE.Vector3(128,122,-205),ms:0.9,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.52,
  dirP:new THREE.Vector3(60,120,40),ambC:C(0xd8d2c0),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,12,92],t:[0,11,82],lf:[0,18,-56],lt:[0,18,-56]},
  sky:()=>SK({fd:0.0045,star:0.06,ms:0.8,moon:new THREE.Vector3(135,120,-205)}) },
{ name:'叠山枫丹',dwell:16,river:0.03,build:bYanshui,
  cam:{f:[0,6.5,26],t:[1.4,5.6,20],lf:[0.5,5.5,-8],lt:[2.2,6.2,-16]},
  sky:()=>SK({fd:0.0056,star:0.05,ms:0.85,moon:new THREE.Vector3(120,118,-200)}) },
{ name:'雁字风月',dwell:18,river:0.02,build:bYanlian,
  cam:{f:[0,6,22],t:[0.6,5.6,16],lf:[0,5.5,-10],lt:[1.2,6.4,-18]},
  sky:()=>SK({fd:0.0072,star:0.04,ms:1.05,mph:0.06,mhaze:0.03,
    moon:new THREE.Vector3(-95,108,-195),dirC:C(0xd5d1c4),dirI:0.44}) },
];
"""
