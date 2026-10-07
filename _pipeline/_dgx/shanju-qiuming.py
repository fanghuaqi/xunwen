# -*- coding: utf-8 -*-
"""shanju-qiuming.py —— 《山居秋暝》（唐·王维，no.204，水墨夜思）生成配置
两境：松月泉声（绝唱对·标志性瞬间：月光穿松成柱+清泉过石成溪）、
竹喧莲动（浣女归/渔舟下，末境点击清泉：月光穿松+泉石流光，王孙自可留）"""

META = dict(
    N=2, slug='shanju-qiuming', title='山居秋暝', dyn='唐 · 王维', brand_author='王 维',
    gold_rgb='168,184,160',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#a8b8a0; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(168,184,160,.26);
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
    tip='轻点画面 / 按空格 —— 泉石流光，王孙自可留',
    hint='← → 键或空格逐境游览 · 末境可点击清泉，看月光穿松、泉石流光',
    cover_read='山居秋暝。唐，王维。空山新雨后，天气晚来秋。明月松间照，清泉石上流。',
    cover_p1='两重意境，随诗句次第展开：空山新雨、天气晚来的秋暝时节，明月穿松成柱、清泉过石成溪；竹喧声里浣女归，莲叶摇处渔舟下，末了春芳任歇，王孙自可留。',
    cover_p2='边读诗，边走进王维「诗中有画」的空山秋暝。',
    end_h2='泉石 · 可留', cn_word='两',
    words_js="['再游一次，且听泉响','初识空山，尚需共读','渐入佳境，再诵几遍','诗境渐深，月照松间','已解王孙自留之意','诗中有画，空山心境']",
    sky_atmo='0x26332f',
)

POEM_JS = """const POEM = [
{ name:'松月泉声', jing:'空山新雨，明月穿松成柱，清泉过石成溪 —— 一色一声，动静相生。（松 · 月 · 泉）',
  segs:[
   {c:'空山新雨后，', p:py('kōng shān xīn yǔ hòu')},
   {c:'天气晚来秋。', p:py('tiān qì wǎn lái qiū')},
   {c:'明月松间照，', p:py('míng yuè sōng jiān zhào')},
   {c:'清泉石上流。', p:py('qīng quán shí shàng liú')}],
  read:'空山新雨后，天气晚来秋。明月松间照，清泉石上流。',
  yisi:'空旷的山林刚下过一场新雨，傍晚的天气带来初秋的凉意。明月洒下清辉，从松针的缝隙间穿过，在林间投下一道道光的柱、光的斑；清泉涨满山涧，从青石上淙淙流过。一静一动，一色一声——被后人誉为山水诗的绝唱。',
  zhu:[['秋暝','秋天的日暮时分。暝（míng），日落黄昏、天色向晚——诗题点明时间：秋日傍晚雨后的山中'],['空山','幽静空寂的山林；「空」非无人，而是心境的空灵澄澈'],['新雨','刚下过的雨；雨霁之后，尘埃洗尽，清气满山'],['清泉石上流','雨后山泉漫过青石淙淙而下。上句「明月松间照」写色写静，此句写声写动，动静相生']] },
{ name:'竹喧莲动', jing:'竹喧声里浣女归，莲叶摇处渔舟下；随意春芳歇，王孙自可留。（竹 · 莲 · 点击清泉）',
  segs:[
   {c:'竹喧归浣女，', p:py('zhú xuān guī huàn nǚ')},
   {c:'莲动下渔舟。', p:py('lián dòng xià yú zhōu')},
   {c:'随意春芳歇，', p:py('suí yì chūn fāng xiē')},
   {c:'王孙自可留。', p:py('wáng sūn zì kě liú')}],
  read:'竹喧归浣女，莲动下渔舟。随意春芳歇，王孙自可留。',
  yisi:'竹林里传来一阵阵欢声笑语，那是浣衣的女子结伴归来；水面的莲叶纷纷摇动，原来是渔舟顺流而下。任凭春天的芳菲消歇吧——这秋山中自有明月清泉，诗人这「王孙」，自可留在此间。以动衬静，愈见山居之静与心境之安。',
  zhu:[['竹喧','竹林中传来喧笑语声——未见其人，先闻其声'],['浣女','水边洗衣的女子。浣（huàn），洗涤'],['莲动','水面莲叶摇动——原来是顺流而下的渔舟'],['春芳歇','春天的芳华已然消歇。歇（xiē），消逝；「随意」即任凭它消逝'],['王孙','诗人自指。《楚辞·招隐士》云「王孙兮归来，山中兮不可久留」，此处反用其意：山中自有明月清泉，王孙自可长留']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「空山新雨后」的下一句是？', o:['明月松间照','天气晚来秋','清泉石上流'], a:1},
 {q:'「竹喧归浣女」的下一句是？', o:['莲动下渔舟','随意春芳歇','王孙自可留'], a:0},
 {q:'诗题「山居秋暝」的「暝」与「浣女」的「浣」，注音全都正确的是？', o:['暝 huàn、浣 míng','暝 míng、浣 huàn','暝 míng、浣 wán'], a:1},
 {q:'「王孙自可留」反用《楚辞·招隐士》「王孙兮归来，山中兮不可久留」的典故，意在？', o:['山中寂寞，确实不可久留','怀念京城，欲归而不得','山中自有明月清泉，可游可居，故「自可留」'], a:2},
 {q:'苏轼评王维「诗中有画」。这首诗最核心的心境是？', o:['空山隐逸、宁静淡泊','秋夜凄凉、孤独思归','怀才不遇、愤世嫉俗'], a:0},
];
"""

SCENES_JS = """/* ================= 山居秋暝 · 两境场景（水墨夜思·青灰山色：松月泉声、竹喧莲动） ================= */

/* 松林：树干 + 3-4 层松冠（锥台成层），全部合批 1 mesh（月光从株间穿过的留白即「松间」） */
function makePines(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?204:o.seed);
  const n=o.n===undefined?5:o.n, spread=o.spread===undefined?30:o.spread, deep=o.deep===undefined?18:o.deep;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, zz=(R()-0.5)*deep, h=(o.h===undefined?14:o.h)*(0.72+0.55*R());
    const tilt=(R()-0.5)*0.12;
    const trunk=new THREE.CylinderGeometry(0.12,0.28,h*0.62,6);
    trunk.rotateZ(tilt); trunk.translate(x,h*0.3,zz); B.put(trunk,0x0a0e0c);
    const layers=3+Math.floor(R()*2);
    for(let L=0;L<layers;L++){
      const f=L/layers;
      const cone=new THREE.ConeGeometry((2.0-f*1.2)*(0.85+0.4*R()),h*0.30,7);
      cone.rotateZ(tilt*0.5); cone.translate(x,h*0.36+f*h*0.48,zz);
      B.put(cone,L%2?0x0d1511:0x0f1813);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x27332c,emissive:0x04070a}),{c:0xa8b8a0,i:0.2,p:2.4})));
  return g;
}

/* 竹丛：细长竹竿微倾 + 叶片（PlaneGeometry），合批 1 mesh（DoubleSide） */
function makeBamboo(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?104:o.seed);
  const n=o.n===undefined?8:o.n, spread=o.spread===undefined?20:o.spread;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, zz=(R()-0.5)*(o.deep===undefined?12:o.deep), h=9+R()*5.5;
    const tilt=(R()-0.5)*0.16;
    const stalk=new THREE.CylinderGeometry(0.075,0.11,h,5);
    stalk.rotateZ(tilt); stalk.translate(x,h*0.5,zz); B.put(stalk,0x0f1810);
    const nodes=2+Math.floor(R()*2);
    for(let s=0;s<nodes;s++){
      const ny=h*(0.55+0.4*s/nodes), nx=x+Math.sin(tilt)*ny*0.5;
      const cl=4+Math.floor(R()*2);
      for(let c=0;c<cl;c++){
        const yaw=R()*6.283, droop=0.45+R()*0.5;
        const lf=new THREE.PlaneGeometry(2.8,0.24);
        lf.translate(1.4,0,0);
        lf.rotateZ(-droop); lf.rotateY(yaw);
        lf.translate(nx,ny,zz);
        B.put(lf,R()<0.5?0x101c14:0x142218);
      }
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x141c18,emissive:0x04080a,side:THREE.DoubleSide}),{c:0xa8b8a0,i:0.18,p:2.4})));
  return g;
}

/* 泉石：沿溪一线的青石（rockGeo），合批 1 mesh —— 「清泉石上流」的石 */
function makeStreamRocks(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?404:o.seed);
  const n=o.n===undefined?7:o.n, len=o.len===undefined?42:o.len;
  const x0=o.x===undefined?2:o.x, z0=o.z0===undefined?6:o.z0;
  for(let i=0;i<n;i++){
    const z=z0-i*(len/(n-1))+(R()-0.5)*3, x=x0+(R()-0.5)*5;
    const rg=rockGeo(0.7+R()*1.0,1,R);
    rg.translate(x,-0.25+R()*0.15,z); B.put(rg,0x0c1113);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a4a44,emissive:0x04070a}),{c:0xa8b8a0,i:0.3,p:2.3})));
  return g;
}

/* 月光穿松成柱：标志性瞬间。竖长面片 + 冷银青辉着色器（显式双 shader，additive，不入雾同步表） */
const BEAM_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const BEAM_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float ex=smoothstep(0.0,0.40,vUv.x)*smoothstep(1.0,0.60,vUv.x);
  float ey=smoothstep(0.05,0.55,vUv.y)*smoothstep(1.0,0.75,vUv.y);
  float shimmer=0.84+0.14*sin(uTime*0.7+vUv.y*6.0)+0.05*sin(uTime*2.1+vUv.y*23.0);
  vec3 col=vec3(0.72,0.82,0.76);
  gl_FragColor=vec4(col,uFade*uK*ex*ey*shimmer*0.5);
}`;

function makeMoonShafts(o){
  o=o||{};
  const xs=o.xs||[-6,0,7,13], len=o.len===undefined?46:o.len, z=o.z===undefined?-28:o.z;
  const k0=o.k===undefined?1:o.k;
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:k0}},
    vertexShader:BEAM_VERT,fragmentShader:BEAM_FRAG});
  const g=new THREE.Group();
  for(let i=0;i<xs.length;i++){
    const w=(o.w===undefined?4:o.w)*(0.7+0.06*((i*37)%10));
    const m=new THREE.Mesh(new THREE.PlaneGeometry(w,len),mat);
    m.rotation.set(o.tiltX===undefined?-0.53:o.tiltX,0,o.tiltZ===undefined?-0.22:o.tiltZ);
    m.position.set(xs[i],len*0.5-6,z); m.renderOrder=2; g.add(m);
  }
  return {g,mat,update(t,k){ mat.uniforms.uTime.value=t;
    if(k!==undefined)mat.uniforms.uK.value=k; }};
}

/* 莲塘：莲叶（CircleGeometry 微倾）+ 数茎荷花，合批 1 mesh */
function makeLotus(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?304:o.seed);
  const n=o.n===undefined?12:o.n, w=o.w===undefined?22:o.w, deep=o.deep===undefined?20:o.deep;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, zz=(R()-0.5)*deep;
    const lf=new THREE.CircleGeometry(0.9+R()*1.0,9);
    lf.rotateX(-Math.PI/2+(R()-0.5)*0.24); lf.translate(x,0.32+R()*0.1,zz);
    B.put(lf,R()<0.5?0x17301f:0x122a1b);
    if(R()<0.2){
      const stem=new THREE.CylinderGeometry(0.03,0.045,0.9,5); stem.translate(x,0.62,zz); B.put(stem,0x122016);
      const fl=new THREE.IcosahedronGeometry(0.26,0); fl.scale(1,1.5,1); fl.translate(x,1.15,zz); B.put(fl,0xbccfc2);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3c32,emissive:0x05080a,side:THREE.DoubleSide}),{c:0xa8b8a0,i:0.22,p:2.4})));
  return g;
}

/* 渔舟：Lathe 舱体拉长 + 坐板 + 篙，合批 1 mesh（渔翁人形单独 makeFigure 立舟上） */
function makeSkiff(o){
  o=o||{};
  const B=new GeoBag();
  const hull=new THREE.LatheGeometry(
    [[0,-0.5],[0.55,-0.4],[0.85,-0.12],[0.92,0.1],[0.6,0.14],[0,0.16]].map(function(p){return new THREE.Vector2(p[0],p[1]);}),12);
  hull.scale(2.4,0.55,1.0); B.put(hull,0x262e28);
  const bench=new THREE.BoxGeometry(1.5,0.08,0.7); bench.translate(0,0.28,0); B.put(bench,0x2c342c);
  const pole=new THREE.CylinderGeometry(0.035,0.05,4.4,5); pole.rotateZ(0.9); pole.translate(-0.8,1.6,0); B.put(pole,0x30281e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a4440,emissive:0x060a08}),{c:0xa8b8a0,i:0.35,p:2.4})));
  const base=o.base||[0,0,0], ph=o.ph===undefined?2.1:o.ph;
  const api={g,update(t){
    g.position.set(base[0]+1.4*Math.sin(t*0.045+ph),base[1]+0.05*Math.sin(t*0.6+ph),base[2]+0.8*Math.cos(t*0.03+ph));
    g.rotation.set(0,0.3*Math.sin(t*0.05+ph),0.02*Math.sin(t*0.5+ph));
  }};
  return api;
}

function bCover(){ // 封面 · 空山夜色
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090c,c2:0x0e1315});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:2040,color:0x070a0d,atmo:0x26332f,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const pines=makePines({n:4,spread:46,deep:10,h:11,seed:2041}); pines.position.set(0,-2,-8); g.add(pines);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:2042,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:8,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x8fa89c,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,40,130],pos:[0,10,-40],color:0xc4d8cc,size:8,speed:0.05,rise:0,maxA:0.36});
  g.add(motes.points);
  addLights(g,{c:0x9fb8ab,i:0.42,p:[30,70,40]},{c:0x17201c,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bSongYue(){ // 一 · 松月泉声 —— 绝唱对：月光穿松成柱 + 清泉过石成溪
  const g=new THREE.Group();
  const water=makeWater({size:420,seg:72,amp:0.24,freq:0.12,speed:0.55,flow:[0.3,1],spec:2.2,
    deep:0x0a1416,shallow:0x1a3230,skyc:0x24403c,moonDir:[42,112,-185]});
  water.mesh.position.y=-0.55; g.add(water.mesh);
  const ridge=makeRange({r:250,h:22,layers:2,peaks:5,seed:2043,color:0x070b0d,atmo:0x26332f,fogK:0.62,glowK:0.06,y:-14});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 松林两岸（株间留白给月光穿行） */
  const pines=makePines({n:6,spread:44,deep:20,h:15,seed:2044}); pines.position.set(0,0,-26); g.add(pines);
  /* 月光穿松成柱（标志性瞬间） */
  const shafts=makeMoonShafts({xs:[-6,0,7,13],w:4.4,len:46,z:-28,k:1});
  g.add(shafts.g);
  /* 清泉石上流：青石一线 + 流光粒子顺溪而下 */
  const rocks=makeStreamRocks({n:8,x:2,z0:8,len:44,seed:2045}); g.add(rocks);
  const flow=makeFlow({n:180,box:[9,2.2,80],pos:[2,0.6,-14],color:0xcfe8e0,size:8,speed:3.2,maxA:0.3});
  g.add(flow.points);
  /* 诗人独立溪畔，望月听泉（空山之「空」，以一人衬之） */
  const poet=makeFigure({pose:'独立',robe:0x1c2824,belt:0x4a5a52,skin:0xcbb9a2,collar:0xaebfae,
    hat:'发髻',rimC:0xa8b8a0,rim:0.5,noProp:true,scale:1.7});
  poet.position.set(-9.5,-0.75,-8); poet.rotation.y=0.55; g.add(poet);
  /* 月华微尘 + 谷雾 */
  const motes=makeGlow({n:50,box:[70,14,40],pos:[0,7,-16],color:0xc4d8cc,size:5,speed:0.05,rise:0.1,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[200,20,110],pos:[0,9,-48],scale:70,color:0x8fa89c,op:0.085});
  g.add(mist.g);
  /* 前景框景：坡石 + 溪畔芦苇 */
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:2046,rim:0.14});
  rk.g.position.set(-13,-1.4,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:20,n:9,d:6,color:0x04060a,seed:2047,sway:0.9});
  reeds.g.position.set(19,-1.3,10); g.add(reeds.g);
  addLights(g,{c:0x9fb8ab,i:0.52,p:[30,90,-60]},{c:0x1a2420,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); shafts.update(t,k);
    flow.update(t); motes.update(t); mist.update(t,k);
    rk.update(t,k); reeds.update(t,k); poet.update(t,k);
  }};
}

function bZhuLian(){ // 二（末境可点击）· 竹喧莲动 —— 点击清泉：月光穿松 + 泉石流光
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  const water=makeWater({size:440,seg:76,amp:0.2,freq:0.13,speed:0.5,flow:[0.2,0.6],spec:1.7,
    deep:0x0a1416,shallow:0x1a3230,skyc:0x24403c,moonDir:[30,104,-175]});
  water.mesh.position.y=-0.55; g.add(water.mesh);
  const ridge=makeRange({r:260,h:20,layers:2,peaks:4,seed:2048,color:0x070b0d,atmo:0x26332f,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-112); g.add(ridge.g);
  /* 竹喧（左）：竹丛两片 + 归来浣女二人 */
  const bamboo=makeBamboo({n:13,spread:26,deep:16,seed:2049}); bamboo.position.set(-20,0,-26); g.add(bamboo);
  const bamboo2=makeBamboo({n:6,spread:12,deep:8,seed:2050}); bamboo2.position.set(-34,0,-16); g.add(bamboo2);
  const optHuan={robe:0x1e2a30,belt:0x50646a,skin:0xcbb9a2,collar:0xbcc9c4,hat:'发髻',
    rimC:0xa8b8a0,rim:0.45,noProp:true,scale:1.25};
  const huan1=makeFigure(optHuan); huan1.position.set(-13,-0.75,-14); huan1.rotation.y=0.4; g.add(huan1);
  const huan2=makeFigure(optHuan); huan2.position.set(-16.5,-0.75,-19); huan2.rotation.y=-0.2; g.add(huan2);
  const crowd=makeCrowd({n:3,rect:[-38,-30,10,8],seed:2051,color:0x11181a,rimC:0xa8b8a0,
    rim:0.16,sMin:0.38,sMax:0.5,y:-0.7});
  g.add(crowd.mesh);
  /* 莲动（右）：莲塘 + 渔舟（渔翁独立舟上，随波缓行） */
  const lotus=makeLotus({n:14,w:24,deep:22,seed:2052}); lotus.position.set(17,-0.15,-18); g.add(lotus);
  const skiff=makeSkiff({base:[13,0.02,-16],ph:2.1}); g.add(skiff.g);
  const fisher=makeFigure({pose:'独立',robe:0x1a221e,belt:0x46564e,skin:0xcbb9a2,collar:0xa8b8a0,
    hat:'发髻',rimC:0xa8b8a0,rim:0.42,noProp:true,scale:1.0});
  fisher.position.set(0.2,0.3,0); fisher.rotation.y=-0.5; skiff.g.add(fisher);
  /* 泉石流光（点击清泉的主对象）：后景松影 + 泉石一线 */
  const pines=makePines({n:4,spread:22,deep:10,h:16,seed:2053}); pines.position.set(4,0,-56); g.add(pines);
  const shafts=makeMoonShafts({xs:[-2,4,10],w:4,len:40,z:-46,k:0.18,tiltX:-0.53,tiltZ:-0.17});
  g.add(shafts.g);
  const rocks=makeStreamRocks({n:6,x:5,z0:-26,len:30,seed:2054}); g.add(rocks);
  const flow=makeFlow({n:140,box:[8,2,40],pos:[5,0.5,-42],color:0xcfe8e0,size:7,speed:3.0,maxA:0.14});
  g.add(flow.points);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8c8b8,
    transparent:true,opacity:0.38,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(40,18,1); halo.position.set(5,12,-46); halo.renderOrder=1; g.add(halo);
  const pl=new THREE.PointLight(0xa8d8c8,1.5,60); pl.position.set(5,6,-40); g.add(pl);
  /* 秋气微尘 + 谷雾 + 前景 */
  const motes=makeGlow({n:44,box:[80,14,44],pos:[0,7,-18],color:0xc4d8cc,size:5,speed:0.05,rise:0.08,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:5,spread:[210,20,110],pos:[0,9,-52],scale:72,color:0x8fa89c,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:2055,rim:0.14});
  rk.g.position.set(-14,-1.3,15); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:20,n:9,d:6,color:0x04060a,seed:2056,sway:1.0});
  reeds.g.position.set(20,-1.2,11); g.add(reeds.g);
  addLights(g,{c:0x9fb8ab,i:0.5,p:[24,86,-56]},{c:0x1a2420,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/3.0);
      ridge.update(t,0); water.update(t);
      shafts.update(t,k*(0.18+0.82*ctl.reveal));
      flow.mat.uniforms.uMaxA.value=k*(0.2+0.45*ctl.reveal);
      flow.update(t); motes.update(t); mist.update(t,k);
      skiff.update(t); crowd.update(t);
      rk.update(t,k); reeds.update(t,k); huan1.update(t,k); huan2.update(t,k);
      halo.material.opacity=k*(0.08+0.3*ctl.reveal);
      pl.intensity=k*1.5*(0.25+0.75*ctl.reveal*(0.85+0.15*Math.sin(t*2.0)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.05,0.12); pluck(0,0.5,0.1); pluck(4,1.0,0.09);
        const fl=$('#flash'); fl.textContent='泉石流光'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070c10),hor:C(0x182320),bot:C(0x080c0f),fog:C(0x11191a),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(38,108,-180),ms:1.9,mph:0,mhaze:0.05,dirC:C(0x9fb8ab),dirI:0.52,
  dirP:new THREE.Vector3(30,90,-60),ambC:C(0x19231f),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,16,-40],lt:[0,16,-40]},
  sky:()=>SK({top:C(0x060a0e),hor:C(0x141d1b),bot:C(0x070b0e),fog:C(0x0f1718),fd:0.0050,star:0.4,
    ms:1.7,moon:new THREE.Vector3(24,96,-170),
    dirC:C(0x9fb8ab),dirI:0.4,ambC:C(0x17201c),ambI:0.6}) },
{ name:'松月泉声',dwell:16,river:0.05,build:bSongYue,
  cam:{f:[0,7.5,24],t:[1.8,7,20.5],lf:[0,8,-20],lt:[1.2,7.5,-22]},
  sky:()=>SK({top:C(0x070c10),hor:C(0x182320),bot:C(0x080c0f),fog:C(0x11191a),fd:0.0060,star:0.45,
    ms:2.0,mph:0,mhaze:0.05,moon:new THREE.Vector3(42,112,-185),
    dirC:C(0x9fb8ab),dirI:0.52,ambC:C(0x19231f),ambI:0.6}) },
{ name:'竹喧莲动',dwell:17,river:0.04,build:bZhuLian,
  cam:{f:[0,7,22],t:[-1.6,6.6,19],lf:[0,7,-22],lt:[0.6,6.6,-24]},
  sky:()=>SK({top:C(0x080d11),hor:C(0x1a2620),bot:C(0x090d10),fog:C(0x121a1b),fd:0.0060,star:0.4,
    ms:1.85,mph:0,mhaze:0.05,moon:new THREE.Vector3(30,104,-175),
    dirC:C(0x9fb8ab),dirI:0.5,ambC:C(0x1a2420),ambI:0.58}) },
];
"""
