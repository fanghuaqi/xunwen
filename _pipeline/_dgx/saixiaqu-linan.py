# -*- coding: utf-8 -*-
"""saixiaqu-linan.py —— 《塞下曲·其二》（唐·卢纶，queue no.219，大漠金戈）生成配置
两境（N=queue stages 数）：林暗引弓（林暗草惊风·将军夜引弓——夜惊→引弓）、
白羽没石（平明寻白羽·没在石棱中——晨寻→没石，标志性瞬间+末境点击）。
大漠金戈全套色板：底色 #120d08、雾 #140d07～#1c130a 系、文字 #f0e2cc，accent=#c4824a
（queue 分配强调色，暗赭鎏金）只落在人物边缘光/箭镞寒光/石棱受光/晨光/UI 上，禁艳金。
时间推进线：境壹=夜（林暗、惊风、引弓，低月昏黄）→ 境贰=平明（晨光斜照、宿雾未散）。
标志性瞬间（境贰·全诗名句）：没在石棱中——晨光斜掠的大石棱线上，一支白羽箭深深没入石中，
不见镞、只见杆羽（没镞特写）；与已有边塞页（孤城/大漠/城垣）第一眼可区分：本页是密林夜惊+晨石特写。
末境点击（queue interact：点击引弓——夜射白羽+箭没石棱特写）：点击画面——幽影飞箭沿抛物线
自夜林深处破空而来（重现昨夜一射），钉入石棱迸出石屑、白羽犹颤，「将军夜引弓 没在石棱中」题字同现。
考点钉子：没 mò（没入）/ 棱 léng（小测第 3 题落点）；李广射石典故《史记·李将军列传》（第 4 题，
兼塞下曲组诗常识）；侧面烘托写法（第 5 题）。彩蛋：成语「没石饮羽」即出此典。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='saixiaqu-linan', title='塞下曲·其二', dyn='唐 · 卢纶', brand_author='卢 纶',
    gold_rgb='196,130,74',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#c4824a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(196,130,74,.3);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(24,16,9', 1),
        ('rgba(4,6,11', 'rgba(12,8,5', 2),
        ('rgba(6,9,16', 'rgba(24,16,9', 1),
        ('rgba(3,5,9', 'rgba(8,5,3', 1),
        ('#0b101c', '#181009', 1),
        ('#6f664f', '#7a6a50', 1),
        ('#5a5340', '#6a5a44', 1),
    ],
    tip='轻点画面 / 按空格 —— 箭没石棱，白羽犹颤',
    hint='← → 键或空格逐境游览 · 末境可点击画面：重现昨夜引弓一箭，看白羽没入石棱',
    cover_read='塞下曲·其二。唐，卢纶。林暗草惊风，将军夜引弓。平明寻白羽，没在石棱中。',
    cover_p1='两重意境，随诗句次第展开：夜黑林暗、疾风惊草，将军在黑暗中闻声引弓的一瞬；天刚放亮去寻箭，白羽竟深深没入石棱——一夜惊险，只留一支没石之箭作证。',
    cover_p2='边读诗，边走进那个惊风四起的夜晚：不写射虎、不写搏斗，只写「引弓」与「寻箭」两个动作——读懂了这两处留白，就读懂了飞将军的神勇，也读懂了李广射石这个千古典故。',
    end_h2='白羽 · 没石', cn_word='贰',
    words_js="['再引一次夜林弓','初识卢纶，尚需共读','渐入诗境，再诵几遍','风惊草动，弓开满月','已解没石白羽意','箭镞入石，神勇自见']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'林暗引弓', jing:'幽暗的密林里疾风骤起、草浪伏动，将军在黑夜中从容拉弓 —— 夜惊、引弓，一瞬千钧。（夜林 · 惊风 · 引弓）',
  segs:[
   {c:'林暗草惊风，', p:py('lín àn cǎo jīng fēng')},
   {c:'将军夜引弓。', p:py('jiāng jūn yè yǐn gōng')}],
  read:'林暗草惊风，将军夜引弓。',
  yisi:'幽暗的深林里，疾风骤起，杂草伏倒；将军在这黑夜之中从容拉开弓，一箭射出。——前句写「险」：夜黑、林暗、风急、草动，层层逼出大敌当前的紧张；后句写「定」：不辨目标、不待天明，闻声即引弓——一场夜射只写引弓的一瞬，箭去何方全然留白，二十个字字字千钧。',
  zhu:[['塞下曲','唐代乐府旧题，多写边塞征战生活。卢纶《塞下曲》组诗共六首，此为第二首（其三「月黑雁飞高」最为人熟知）'],['林暗','幽暗的密林。林「暗」既写夜色浓重、林木遮天，也暗写风声骤起前那一分不祥的静'],['草惊风','疾风猝至，草浪伏起，仿佛草丛受了惊吓——是风动，也是心惊：暗写林中似有物潜行'],['引弓','拉弓、开弓。引，张——黑夜之中不辨目标，闻声即射，一个「引」字写出弓如满月、箭在弦上的果决与镇定']] },
{ name:'白羽没石', jing:'天刚放亮去寻找昨晚射出的箭，那支白羽箭竟深深没入石棱之中 —— 晨寻、没石，神力自见。（平明 · 白羽 · 没石 · 标志性瞬间 · 末境点击画面：重现昨夜引弓一箭）',
  segs:[
   {c:'平明寻白羽，', p:py('píng míng xún bái yǔ')},
   {c:'没在石棱中。', p:py('mò zài shí léng zhōng')}],
  read:'平明寻白羽，没在石棱中。',
  yisi:'天刚放亮，将军去寻找昨晚射出的那支白羽箭，发现它早已深深没入石棱之中。——「寻」字最妙：夜射时并不知道自己射中了什么，清晨才去寻，悬念全在「寻」里，惊叹全在「没」里。及至看见白羽深陷石棱，才知昨夜那一箭射的是石不是虎——不必写虎，虎威自在；不必夸神力，没石之箭自见神力。',
  zhu:[['平明','天刚亮的时候'],['白羽','箭杆尾部装的白色鸟羽，代指箭——寻「白羽」即寻昨夜射出的那支箭'],['没','读 mò，没入、陷入——箭不但射中了石，连箭头（镞）都整个陷进石棱里。成语「没石饮羽」即出此典'],['石棱','石头的棱角、边缝——箭恰恰没入石棱最坚硬处，「没镞」愈显神力'],['李广射石的典故','《史记·李将军列传》：李广出猎，见草中石，以为虎而射之，中石没镞（箭头全部没入石中），再射终不能复入石中。卢纶化用此典：将军夜半闻风惊草动，疑虎而射；平明寻箭，方知中石——「飞将军」的神力与沉着尽在不言中']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「林暗草惊风」的下一句是？', o:['将军夜引弓','平明寻白羽','没在石棱中'], a:0},
 {q:'「平明寻白羽」的下一句是？', o:['将军夜引弓','没在石棱中','林暗草惊风'], a:1},
 {q:'「没在石棱中」的「没」与「棱」，读音和意思都正确的一项是？', o:['没读 mò，没入、陷入；棱读 léng，石头的棱角——连箭头都陷进了石头的棱缝里','没读 méi，没有——石头棱角里找不到箭；棱读 líng，指山岭','没读 mò，沉入水中；棱读 léng，指江河的堤岸'], a:0},
 {q:'这首诗化用了一个著名典故。关于「夜引弓」与「没在石棱中」，下列说法正确的是？', o:['化用《史记·李将军列传》「飞将军」李广的典故：李广见草中石，以为虎而射之，中石没镞——卢纶借李广写将军夜疑虎、晨见箭没石棱的神勇','化用「后羿射日」的典故：将军一箭射落天上星辰，所以白羽能没入石棱','化用「养由基百步穿杨」的典故：将军射穿百步外的杨叶，箭余力未尽又没入石棱'], a:0},
 {q:'全诗只二十字：夜惊（林暗草惊）→ 引弓 → 晨寻 → 没石。这首诗写将军神勇最妙的手法是？', o:['正面铺写搏斗场面，用大量笔墨直接描写将军与猛虎搏杀的惊险过程','不写射的场面，也不点破射的是石不是虎：只以「引弓」「寻白羽」两个动作带出悬念，让「没在石棱中」的结果自己说话——侧面烘托，神力自见','用夸张的数字（如「一箭三百步」）直接称赞将军武艺高强天下第一'], a:1},
];
"""

SCENES_JS = """/* ================= 塞下曲·其二 · 两境场景（大漠金戈·夜林惊风：林暗引弓、白羽没石） =================
   美术立意：大漠金戈色板写「夜林惊风→平明没石」——底色 #120d08、雾 #140d07～#1c130a 系，
   accent=#c4824a（暗赭鎏金）只落在人物边缘光/箭镞寒光/石棱受光/晨光上，禁艳金。
   与已有边塞页第一眼可区分：不做孤城/大漠/城垣，做「密林夜惊 + 晨石白羽特写」。
   境壹（夜）：密林四面合围、草浪伏动、罡风横流，低月昏黄，将军持弓 引弓夜射。
   境贰（平明·标志性瞬间+末境可点击）：晨光斜掠大石棱线，白羽箭没镞于石（只见杆羽）；
   点击：幽影飞箭沿抛物线自夜林破空而来（重现昨夜一射），钉入石棱迸石屑、白羽犹颤。 */

/* —— 草浪 makeCaolang(o)：整片草叶自写着色器（叶身随风摆 + 阵风涌动，风从草梢算起）——「草惊风」 */
const SQL_CAO_VERT=`
uniform float uTime; uniform float uSway; uniform float uGust;
varying float vY;
void main(){
  vY=uv.y;
  vec3 p=position;
  float k=uv.y*uv.y;
  float ph=position.x*2.7+position.z*1.9;
  p.x+=sin(uTime*2.1+ph)*uSway*k+sin(uTime*0.6+ph*0.31)*uGust*k;
  p.z+=cos(uTime*1.6+ph*1.4)*uSway*0.55*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const SQL_CAO_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade;
varying float vY;
void main(){
  vec3 c=mix(uC,uTipC,pow(clamp(vY,0.0,1.0),1.5));
  gl_FragColor=vec4(c,uFade);
}`;
function makeCaolang(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21901:o.seed);
  const n=o.n===undefined?240:o.n, w=o.w===undefined?56:o.w, d=o.d===undefined?26:o.d;
  const z=o.z===undefined?-14:o.z;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, zz=z+(R()-0.5)*d, h=(o.h===undefined?1.15:o.h)*(0.5+0.9*R());
    const bl=new THREE.PlaneGeometry(0.10+R()*0.08,h,1,3);
    bl.rotateY(R()*6.283); bl.translate(x,h*0.5,zz);
    B.put(bl,0xffffff);
  }
  const mt=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.16:o.sway},uGust:{value:o.gust===undefined?0.10:o.gust},
      uC:{value:C(o.c===undefined?0x241a10:o.c)},uTipC:{value:C(o.tip===undefined?0x4a3a22:o.tip)},uFade:{value:1}},
    vertexShader:SQL_CAO_VERT,fragmentShader:SQL_CAO_FRAG});
  const mesh=B.mesh(mt);
  mesh.frustumCulled=false; mesh.renderOrder=1;
  const g=new THREE.Group(); g.add(mesh);
  g.userData.mt=mt;
  g.update=function(t){ mt.uniforms.uTime.value=t; };
  g.userData.update=g.update;
  return g;
}

/* —— 夜林 makeYelin(o)：密林墙（干+层叠暗冠+疏枝，合批 1 mesh，整片微摆）——「林暗」 */
function makeYelin(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21911:o.seed);
  const n=o.n===undefined?8:o.n, w=o.w===undefined?44:o.w;
  const z=o.z===undefined?-20:o.z, dz=o.dz===undefined?14:o.dz, h0=o.h===undefined?13:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, zz=z+(R()-0.5)*dz, h=h0*(0.65+0.6*R());
    const tr=new THREE.CylinderGeometry(0.16,0.36,h,6);
    tr.translate(x,h*0.5,zz); B.put(tr,shadeColor(0x171009,0.8+0.4*R()));
    const nb=2+Math.floor(R()*2);
    for(let c2=0;c2<nb;c2++){
      const cr=2.4+R()*2.6;
      const cp=new THREE.SphereGeometry(cr,7,6);
      cp.scale(1,0.60+R()*0.25,1);
      cp.translate(x+(R()-0.5)*3.0,h*(0.70+c2*0.17+R()*0.08),zz+(R()-0.5)*2.2);
      B.put(cp,shadeColor(0x1c1409,0.65+0.5*R()));
    }
    for(let b=0;b<2;b++){
      const a=R()*6.283, y0=h*(0.45+R()*0.3), len=2.2+R()*2.2;
      B.put(limbGeo([x,y0,zz],[x+Math.cos(a)*len,y0+len*0.4,zz+Math.sin(a)*len*0.7],0.09,0.03,5),0x140e08);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2012,emissive:0x040302}),{c:0xc4824a,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.0022*Math.sin(t*0.5+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 白羽箭 makeJian(o)：杆沿 +X、镞在 +X 端、白羽在尾端（没石箭把 +X 端调头朝下没入石中） */
function makeJian(o){
  o=o||{};
  const L=o.L===undefined?1.5:o.L;
  const B=new GeoBag();
  const sha=new THREE.CylinderGeometry(0.021,0.027,L,6);
  sha.rotateZ(-Math.PI/2); sha.translate(L/2,0,0); B.put(sha,0x6a5030);
  if(o.head!==false){
    const hd=new THREE.ConeGeometry(0.05,0.22,6);
    hd.rotateZ(-Math.PI/2); hd.translate(L+0.10,0,0); B.put(hd,0x9a9088);
  }
  const fk=o.fk===undefined?1:o.fk;
  for(let i=0;i<3;i++){
    const f=new THREE.PlaneGeometry(0.36*fk,0.115*fk);
    f.translate(0.20+i*0.13*fk,0.068*fk,0);
    f.rotateX(i*2.094);
    B.put(f,o.feather===undefined?0xece2cc:o.feather);
  }
  const mat=o.basic?new THREE.MeshBasicMaterial({color:o.basicC===undefined?0xdcc9a4:o.basicC,transparent:true,opacity:0.90})
    :new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
      specular:0x4a4038,emissive:0x080604,side:THREE.DoubleSide});
  const g=new THREE.Group(); g.add(B.mesh(mat));
  return g;
}

/* —— 弓 makeGongju(o)：弓身（弧环）+ 弓弦 + 搭弦白羽箭，箭指 +X（挂到人物手上后转朝面向） */
function makeGongju(o){
  o=o||{};
  const r=o.r===undefined?0.85:o.r, arc=2.0;
  const B=new GeoBag();
  const bowArc=new THREE.TorusGeometry(r,0.036,6,22,arc);
  bowArc.rotateZ(-arc/2);                 // 弓背朝 +X，弓梢上下张开
  B.put(bowArc,0x33240f);
  const tx=Math.cos(arc/2)*r, ty=Math.sin(arc/2)*r;
  B.put(limbGeo([tx,-ty,0],[tx,ty,0],0.014,0.010,4),0xe2d6ba);   // 弦
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a3020,emissive:0x070502}),{c:0xc4824a,i:o.rim===undefined?0.38:o.rim,p:2.2})));
  const arr=makeJian({L:1.25,head:true});
  arr.position.set(tx-0.02,0,0);          // 箭尾抵弦
  g.add(arr);
  g.scale.setScalar(o.scale===undefined?1.5:o.scale);
  return g;
}

/* —— 大石 makeLishi(o)：风蚀巨石叠出棱线（合批 1 mesh，晨光斜掠时棱线发亮）——「石棱」 */
function makeLishi(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?21921:o.seed);
  const r0=o.r===undefined?1.75:o.r;
  const a=rockGeo(r0,1,R); a.scale(1.25,0.85,0.95); a.translate(0,r0*0.55,0); B.put(a,0x39302a);
  const b=rockGeo(r0*0.72,1,R); b.scale(1.15,0.9,0.9); b.rotateZ(0.12); b.translate(-r0*0.55,r0*1.15,-r0*0.18); B.put(b,0x443a30);
  const c=rockGeo(r0*0.95,1,R); c.scale(1.5,0.52,0.8); c.rotateZ(-0.16); c.rotateY(0.2); c.translate(r0*0.22,r0*1.55,r0*0.1); B.put(c,0x4a4036);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x554a3a,emissive:0x060503}),{c:0xc4824a,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 淡日 makeChenri(o)：平明的晨日低悬（limbTex 日轮+暖晕；fadeK 铁律：初值=最大） */
function makeChenri(o){
  o=o||{};
  const r=o.r===undefined?7:o.r, op=o.op===undefined?0.30:o.op;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xe8c890:o.color,
    transparent:true,opacity:op,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0xd8a860:o.hazeC,
    transparent:true,opacity:o.haze===undefined?0.12:o.haze,depthWrite:false,fog:false}));
  haze.scale.set(r*5.6,r*5.6,1); g.add(haze);
  g.update=function(t,k){
    disc.material.opacity=k*op*(0.94+0.06*Math.sin(t*0.4));
    haze.material.opacity=k*(o.haze===undefined?0.12:o.haze)*(0.85+0.15*Math.sin(t*0.33+1.7));
  };
  g.userData.update=g.update;
  return g;
}

/* 寻箭人/夜射将军：全诗贯穿的同一造型（每次 build 新建材质） */
function sqlFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x3a2c1c,belt:0x8a6a44,skin:0xd9b189,collar:0x7a5c38,
    hair:0x1a140c,hat:'发髻',beard:true,rimC:0xc4824a,rim:0.5,noProp:true,scale:scale===undefined?1.9:scale});
}

function bCover(){ // 卷首 · 夜林惊风：密林合围、草浪伏动、罡风横流、低月昏黄
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e0a06,c2:0x1c130b,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:21931,color:0x0d0906,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-20,0,-96); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ye1=makeYelin({n:10,w:80,h:14,z:-48,dz:16,seed:21932}); g.add(ye1);
  const cao1=makeCaolang({n:240,w:64,d:26,z:-14,seed:21933}); g.add(cao1);
  const cao2=makeCaolang({n:110,w:34,d:10,z:-3,h:0.9,seed:21934}); g.add(cao2);
  const wind=makeFlow({n:380,box:[100,10,40],pos:[0,2.6,-16],color:0x6a5442,size:16,speed:5.2,maxA:0.14});
  g.add(wind.points);
  const motes=makeGlow({n:30,box:[170,20,70],pos:[0,9,-38],color:0x8a7048,size:4.6,speed:0.04,rise:0,add:false,maxA:0.10});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,14,80],pos:[0,5,-58],scale:70,color:0x4a3826,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'树枝',n:4,w:12,d:4,color:0x100b06,seed:21935,sway:0.8,rim:0.08,rimC:0xc4824a});
  fg1.g.position.set(-9.5,5.6,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.8,w:13,d:6,color:0x0c0805,seed:21936,rim:0.09,rimC:0xc4824a});
  fg2.g.position.set(13,-1.9,15); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.30,p:[-40,55,-25]},{c:0x281c10,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ye1.update(t); cao1.update(t); cao2.update(t); wind.update(t);
    motes.update(t); mist.update(t,k); fg1.update(t,k); fg2.update(t,k);
  }};
}
function bYejing(){ // 壹 · 林暗引弓 —— 林暗草惊风，将军夜引弓：密林夜惊，引弓一瞬
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d0906,c2:0x1b120a,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:16,layers:2,peaks:4,seed:21941,color:0x0c0805,atmo:0x2e2114,
    fogK:0.64,glowK:0.04,glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-30,0,-100); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 密林四面合围 */
  const ye1=makeYelin({n:6,w:30,h:15,z:-26,dz:10,seed:21942}); ye1.position.set(-17,0,0); g.add(ye1);
  const ye2=makeYelin({n:6,w:28,h:14,z:-30,dz:10,seed:21943}); ye2.position.set(18,0,0); g.add(ye2);
  const ye3=makeYelin({n:10,w:70,h:13,z:-48,dz:14,seed:21944}); g.add(ye3);
  /* 将军：持弓引弓，射向暗林深处 */
  const rock=makeForeground({kind:'坡石',n:2,r:2.4,w:9,d:5,color:0x0c0805,seed:21945,rim:0.12,rimC:0xc4824a});
  rock.g.position.set(2.6,-1.4,-6.6); g.add(rock.g);
  const poet=sqlFigure(1.9,'指月'); poet.position.set(3.2,-0.30,-6.5); poet.rotation.y=2.75; g.add(poet);
  const gong=makeGongju({scale:1.5}); gong.position.set(0.98,3.66,0.26); gong.rotation.y=-Math.PI/2;
  gong.rotation.z=-0.12; poet.add(gong);
  /* 草惊风：整片草浪随风伏动，阵风一阵紧似一阵 */
  const cao1=makeCaolang({n:240,w:60,d:24,z:-16,seed:21946,sway:0.20}); g.add(cao1);
  const cao2=makeCaolang({n:120,w:32,d:10,z:-2,h:1.0,seed:21947,sway:0.24}); g.add(cao2);
  const wind=makeFlow({n:420,box:[95,9,38],pos:[0,2.4,-15],color:0x6a5442,size:16,speed:5.6,maxA:0.15});
  g.add(wind.points);
  const leaves=makeGlow({n:26,box:[60,10,26],pos:[0,4,-14],color:0x4a3a1e,size:2.6,speed:0.5,rise:-0.6,add:false,maxA:0.12});
  g.add(leaves.points);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-56],scale:68,color:0x4a3826,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[160,18,66],pos:[0,8,-34],color:0x8a7048,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'树枝',n:4,w:13,d:4,color:0x0f0a05,seed:21948,sway:0.9,rim:0.09,rimC:0xc4824a});
  fg1.g.position.set(-11,6,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0c0805,seed:21949,rim:0.10,rimC:0xc4824a});
  fg2.g.position.set(12.5,-1.8,14); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.32,p:[-38,50,-22]},{c:0x281c10,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ye1.update(t); ye2.update(t); ye3.update(t);
    const gust=0.10+0.12*(0.5+0.5*Math.sin(t*0.43));      // 阵风一阵紧似一阵
    cao1.userData.mt.uniforms.uGust.value=gust;
    cao2.userData.mt.uniforms.uGust.value=gust*1.2;
    cao1.update(t); cao2.update(t); wind.update(t); leaves.update(t);
    mist.update(t,k); motes.update(t); poet.update(t,k);
    fg1.update(t,k); fg2.update(t,k); rock.update(t,k);
  }};
}
function bXunyu(){ // 贰（末境·可点击）· 白羽没石 —— 平明寻白羽，没在石棱中：晨光斜掠，白羽没镞于石
  const ctl={t:0,clicked:false,on:false,reveal:0,hit:false,trem:0};
  const g=new THREE.Group();
  const ridge=makeRange({r:310,h:14,layers:2,peaks:4,seed:21951,color:0x0d0906,atmo:0x2e2114,
    fogK:0.60,glowK:0.12,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-6,0,-116); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const grd=makeGround({r:230,c1:0x140e07,c2:0x241808,y:-1.7}); g.add(grd.mesh);
  /* 标志性瞬间：晨光斜掠的大石棱线，白羽箭没镞于石（不见镞，只见杆羽）
     箭：镞端（+X）经 rotation.z=π+1.05 调头朝下斜没入石顶（60°），杆羽露在石上约 1 单位 */
  const stone=makeLishi({r:1.75,scale:1.4,rim:0.22,seed:21952});
  stone.position.set(-1.6,-1.3,-9.2); stone.rotation.y=0.35; g.add(stone);
  const yu=makeJian({L:1.5,head:false,fk:1.35});            // 没镞之箭：镞全没入石，只余杆羽
  yu.position.set(0.30,4.464,0.12); yu.rotation.z=Math.PI+1.05; yu.rotation.y=0.40;
  yu.scale.setScalar(1.28);
  stone.add(yu);
  const yuBase={rz:yu.rotation.z};
  const IMP=new THREE.Vector3(-1.35,4.65,-9.1);             // 幽影飞箭的落点=石上羽端
  /* 晨光斜照石棱：常驻暖点光把大石从暗底里托出来 */
  const sl=new THREE.PointLight(0xd8a878,0.9,34); sl.position.set(0.5,4.5,-6.5); g.add(sl);
  /* 点击交互：幽影飞箭重现昨夜一射，自夜林深处破空而来 */
  const P0=[-36,17,-54], P1=[-16,16,-30], P2=[IMP.x,IMP.y,IMP.z];
  const ghost=makeJian({L:1.4,head:true,basic:true,basicC:0xdcc9a4});
  ghost.rotation.y=-Math.PI/2; ghost.visible=false; ghost.position.set(P0[0],P0[1],P0[2]);
  g.add(ghost);
  const ghostMat=ghost.children[0].material;
  const burst=makeBurst({n:64,color:0xcabf9f,pos:[IMP.x,IMP.y,IMP.z]});
  g.add(burst.points);
  const pl=new THREE.PointLight(0xd8b070,0.85,26); pl.position.set(IMP.x,IMP.y+0.4,IMP.z); g.add(pl);
  /* 平明：晨日低悬、宿雾未散、晨光斜照 */
  const ri=makeChenri({r:7,op:0.30}); ri.position.set(46,10,-70); g.add(ri);
  const crowd=makeCrowd({n:2,rect:[7.5,-15,4,3],seed:21953,color:0x1c1409,rimC:0xc4824a,rim:0.20,sMin:0.6,sMax:0.7,y:-1.3});
  g.add(crowd.mesh);
  /* 将军俯身寻箭：晨光里立在石旁右前 */
  const rock=makeForeground({kind:'坡石',n:2,r:2.2,w:8,d:5,color:0x0d0906,seed:21954,rim:0.12,rimC:0xc4824a});
  rock.g.position.set(6.2,-1.3,-4.4); g.add(rock.g);
  const poet=sqlFigure(1.7,'独立'); poet.position.set(7.2,-0.28,-4.0); poet.rotation.y=3.45; g.add(poet);
  /* 晨草：草梢挑着一点晨光 */
  const cao1=makeCaolang({n:220,w:58,d:24,z:-16,c:0x2e2214,tip:0x6a5430,seed:21955,sway:0.12,gust:0.06}); g.add(cao1);
  const cao2=makeCaolang({n:100,w:30,d:9,z:-3,h:0.95,c:0x2e2214,tip:0x6a5430,seed:21956,sway:0.14,gust:0.06}); g.add(cao2);
  const mist=makeMist({n:7,spread:[230,14,80],pos:[0,4.5,-56],scale:72,color:0x5a4630,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:34,box:[170,16,70],pos:[0,7,-32],color:0xb09060,size:4.4,speed:0.04,rise:0,add:false,maxA:0.10});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0d0906,seed:21957,rim:0.10,rimC:0xc4824a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x0d0906,seed:21958,rim:0.10,rimC:0xc4824a});
  fg2.g.position.set(12.5,-1.6,12); g.add(fg2.g);
  addLights(g,{c:0xd0a268,i:0.50,p:[52,40,-16]},{c:0x3a2b18,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      let e=0;
      if(ctl.on){
        ctl.reveal=Math.min(1,ctl.reveal+dt/1.15);
        e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
        const u=e, iu=1-u, u2=Math.min(1,u+0.03), iu2=1-u2;
        const bx0=iu*iu*P0[0]+2*u*iu*P1[0]+u*u*P2[0];
        const by0=iu*iu*P0[1]+2*u*iu*P1[1]+u*u*P2[1]-0.8*u*(1-u);
        const bz0=iu*iu*P0[2]+2*u*iu*P1[2]+u*u*P2[2];
        ghost.position.set(bx0,by0,bz0);
        ghost.lookAt(iu2*iu2*P0[0]+2*u2*iu2*P1[0]+u2*u2*P2[0],
          iu2*iu2*P0[1]+2*u2*iu2*P1[1]+u2*u2*P2[1]-0.8*u2*(1-u2),
          iu2*iu2*P0[2]+2*u2*iu2*P1[2]+u2*u2*P2[2]);
        if(ctl.reveal>=1&&!ctl.hit){ ctl.hit=true; ghost.visible=false; burst.fire(); }
      }
      if(ctl.hit)ctl.trem+=dt;
      /* 白羽犹颤：中石后石棱震颤渐息 + 一点石光 */
      yu.rotation.z=yuBase.rz+(ctl.hit?0.045*Math.sin(ctl.trem*30)*Math.exp(-ctl.trem*1.6):0);
      pl.intensity=k*(ctl.hit?(0.72+1.3*Math.exp(-ctl.trem*2.4)):e*0.30);
      ghostMat.opacity=k*0.90*((ctl.on&&!ctl.hit)?1:0);
      ridge.update(t,0); grd.update();
      ri.update(t,k); crowd.update(t); poet.update(t,k); rock.update(t,k);
      cao1.update(t); cao2.update(t); mist.update(t,k); motes.update(t);
      burst.update(t);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.18);
        pluck(5,0.0,0.13); pluck(4,0.07,0.10); pluck(2,0.42,0.08);   // 弦响
        const fl=$('#flash'); fl.textContent='将军夜引弓 没在石棱中';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0c0806),hor:C(0x2a1c10),bot:C(0x090604),fog:C(0x140d07),fd:0.0052,star:0.16,
  moon:new THREE.Vector3(-70,28,-200),ms:0.5,mph:0.42,mhaze:0.18,dirC:C(0xb08850),dirI:0.34,
  dirP:new THREE.Vector3(-45,55,-25),ambC:C(0x2c2014),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,46],t:[0,9.5,38],lf:[1.5,8.5,-26],lt:[2.5,9,-36]},
  sky:()=>SK({fd:0.0048,star:0.14}) },
{ name:'林暗引弓',dwell:16,river:0.02,build:bYejing,
  cam:{f:[0,7,24],t:[1.6,7.4,16],lf:[-2,7.5,-14],lt:[-4,8,-26]},
  sky:()=>SK({fd:0.0056,star:0.20,ms:0.36,mph:0.46,mhaze:0.22,
    moon:new THREE.Vector3(-58,26,-185),dirC:C(0xa8824e),dirI:0.30,
    ambC:C(0x281c10),ambI:0.52}) },
{ name:'白羽没石',dwell:19,river:0.02,build:bXunyu,
  cam:{f:[0,5.0,14.5],t:[-1,4.6,7],lf:[-1.2,4.6,-5],lt:[-2.2,5.0,-12]},
  sky:()=>SK({top:C(0x181109),hor:C(0x503a1e),bot:C(0x0f0a06),fog:C(0x1c130a),fd:0.0060,star:0.03,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.05,
    dirC:C(0xd0a268),dirI:0.50,dirP:new THREE.Vector3(55,42,-15),
    ambC:C(0x3a2b18),ambI:0.58}) },
];
"""
