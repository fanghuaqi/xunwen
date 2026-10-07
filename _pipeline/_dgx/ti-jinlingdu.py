# -*- coding: utf-8 -*-
"""ti-jinlingdu.py —— 《题金陵渡》（唐·张祜，queue no.222，水墨夜思）生成配置
两境（N=queue stages 数）：津渡小楼（金陵津渡小山楼·一宿行人自可愁——夜泊渡口、临江小楼）、
星火瓜州（潮落夜江斜月里·两三星火是瓜州——标志性瞬间+末境点击）。
水墨夜思全套色板：底色 #0d1117、雾 #0e141e～#131a26 系、文字 #dfe6f0，accent=#a8b4c0
（queue 分配强调色，银青水月）只落在斜月晕/边缘光/楼窗灯晕/水月反光/UI 上，全页近零饱和。
时间推进线：同一次夜泊的两重「望」：境壹=近泊（渡口栈桥、泊船、小山楼一点暖窗、斜月初上）
→ 境贰=远望（潮落江空、斜月西沉，凭高极目；点击后江雾散开、瓜州星火次第亮起）。
标志性瞬间（境贰·全诗名句）：两三星火是瓜州——夜雾横江，极远处两三点星火般的微光；
与已有水墨夜思页第一眼可区分：不做舟夜孤灯（zhouye 一灯碎星）、不做雨夜棋枰（yueke 灯花）、
做「渡口小楼+空阔夜江+远岸三点渔火」的水乡夜渡——本页唯一暖点是楼上孤窗与远处星火。
末境点击（queue interact：点击星火——江雾散开+瓜州星火次第亮起）：点击画面——横江夜雾向两侧
散开退去，瓜州方向两三点渔火次第亮起（火苗微颤+水面拉出微光倒影），「潮落夜江斜月里
两三星火是瓜州」题字同现。
考点钉子：宿 xiǔ（住一夜，小测第 3 题落点）；金陵渡即今镇江西津渡（唐时润州地界古称金陵，
非今南京）+ 张祜唐诗身份（第 4 题）；「两三星火是瓜州」远望的辨认与推想/羁旅孤愁（第 5 题）。
多音字：宿 xiǔ 钉同音替换「一宿→一朽」；祜 hù 钉「张祜→张护」（tts.json）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='ti-jinlingdu', title='题金陵渡', dyn='唐 · 张祜', brand_author='张 祜',
    gold_rgb='168,180,192',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#a8b4c0; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(168,180,192,.26);
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
        ('0x0a1526', '0x10161f', 4),
    ],
    tip='轻点画面 / 按空格 —— 江雾散处，两三星火是瓜州',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看江雾散开，瓜州星火次第亮起',
    cover_read='题金陵渡。唐，张祜。金陵津渡小山楼，一宿行人自可愁。潮落夜江斜月里，两三星火是瓜州。',
    cover_p1='两重意境，随诗句次第展开：金陵渡口，小楼临江，旅宿此夜的行人愁绪暗生；潮水退落，斜月西沉，夜江空阔——极目远望，江对岸隐约亮起两三点星火般的微光，那应该就是瓜州了吧。',
    cover_p2='边读诗，边走进张祜夜泊的渡口：深夜隔江，那两三点微光本难分辨是什么——读懂「是」字里的一瞥与一问，就读懂了羁旅之人望前路的孤愁。',
    end_h2='星火 · 瓜州', cn_word='两',
    words_js="['再渡一次金陵渡','初识张祜，尚需共读','渐入诗境，再诵几遍','潮落月斜，江天澄澈','已解星火瓜州意','两三星火，愁在远望']",
    sky_atmo='0x1c2634',
)

POEM_JS = """const POEM = [
{ name:'津渡小楼', jing:'金陵渡口的夜晚，小山楼临江而立；旅宿此地的行人，愁绪不招自来 —— 夜泊、羁愁。（津渡 · 小山楼 · 行人 · 楼头一点暖窗）',
  segs:[
   {c:'金陵津渡小山楼，', p:py('jīn líng jīn dù xiǎo shān lóu')},
   {c:'一宿行人自可愁。', p:py('yī xiǔ xíng rén zì kě chóu')}],
  read:'金陵津渡小山楼，一宿行人自可愁。',
  yisi:'金陵渡口的夜晚，一座小山楼静静立在江边；露宿此地的行人，自然而然生出满腔愁绪。——起句七字把「时间、地点、居处」一并落定：金陵渡、津渡口、临江的小楼，是夜泊的场景；次句一个「自」字最沉：孤身羁旅、潮声月色相逼，愁绪不请自来、无从排遣——还没写江、没写月，愁已经先住了进来。',
  zhu:[['题金陵渡','题写在金陵渡口——羁旅夜泊之诗'],['金陵渡','渡口名，在今江苏镇江（唐代润州）城西，即今西津渡。唐时润州地界古称金陵，此「金陵」并非今南京'],['津渡','渡口。津，渡水的地方'],['小山楼','渡口旁临江而立的小楼——诗人夜宿之处（一说为渡口小山上的驿楼）'],['一宿','住一夜。宿，读 xiǔ，过夜、住宿一夜'],['行人','出门在外的人、旅人——诗人自指'],['自可愁','自然而然地生出愁绪。自，自然——羁旅之愁不招自来']] },
{ name:'星火瓜州', jing:'潮水退落，斜月西沉，夜江空阔；极远处的江对岸，两三点星火般的微光——那该就是瓜州了吧。（潮落 · 夜江 · 斜月 · 星火 · 标志性瞬间 · 末境点击画面：江雾散开，瓜州星火次第亮起）',
  segs:[
   {c:'潮落夜江斜月里，', p:py('cháo luò yè jiāng xié yuè lǐ')},
   {c:'两三星火是瓜州。', p:py('liǎng sān xīng huǒ shì guā zhōu')}],
  read:'潮落夜江斜月里，两三星火是瓜州。',
  yisi:'潮水退落，一弯斜月西沉，夜里的江面空阔而沉静；极目望去，江对岸隐约亮起两三点星火般的微光——那应该就是瓜州了吧。——「两三星火」是全诗的点睛之笔：夜深雾重、大江阻隔，极远极小的两三点光，是一夜未眠、凭高极目才捕捉到的；一个「是」字带着辨认与猜想——那点光究竟是渔火、村灯还是市集，其实看不真切，诗人却宁可笃定地说「是瓜州」。远望的一瞥里，装着羁旅的孤寂，也装着对前路的一点点悬念。',
  zhu:[['潮落','潮水退落——长江下游有潮汐，夜半潮退，江面愈显空阔沉静'],['夜江','夜间的江面'],['斜月','西斜的残月——月已西斜，暗示夜深，也暗示诗人伫立（不眠）已久'],['两三星火','两三点像星星一样远而小的火光——对岸渔家或村落的灯火，夜雾中若明若暗'],['瓜州','在长江北岸，与润州（镇江）隔江相望，今属扬州（一作「瓜洲」）'],['「是」字的推想','深夜隔江，两三点微光本难分辨是渔火、村灯还是市集，「是瓜州」是诗人辨认、猜想之后的笃定——天涯羁旅的一夜孤愁，全在这极目远望的一瞥里']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「金陵津渡小山楼」的下一句是？', o:['一宿行人自可愁','潮落夜江斜月里','两三星火是瓜州'], a:0},
 {q:'「潮落夜江斜月里」的下一句是？', o:['一宿行人自可愁','两三星火是瓜州','金陵津渡小山楼'], a:1},
 {q:'「一宿行人自可愁」的「宿」，读音和意思都正确的一项是？', o:['读 xiǔ，住一夜、过夜——诗人夜宿渡口小楼，愁绪暗生','读 sù，星宿——天上星宿照着空阔的夜江','读 xiū，休息——诗人整理行装准备歇息'], a:0},
 {q:'关于诗中的「金陵渡」与作者张祜，下列说法正确的是？', o:['金陵渡在今江苏镇江，即今西津渡——唐时润州地界古称金陵，并非今南京；张祜是唐代诗人，此诗是他羁旅夜泊的名作','金陵渡在今南京市长江边，「金陵」即南京建康的古称；张祜是南宋江湖派诗人','金陵渡是诗人虚构的地名；张祜是「初唐四杰」之一'], a:0},
 {q:'「两三星火是瓜州」历来被推为名句。对它妙处的理解，最准确的一项是？', o:['用夸张手法写灯火之盛：对岸瓜州万家灯火一齐点亮，辉煌如昼','实写白昼渡江：潮落之后江面开阔，对岸村落屋舍历历在目','夜深雾重、大江阻隔，对岸只现出两三点微光，本难分辨是什么——「是」字带着辨认与推想：诗人一夜不眠、极目远望，把羁旅的孤寂与对前路的悬念都放进这一瞥里'], a:2},
];
"""

SCENES_JS = """/* ================= 题金陵渡 · 两境场景（水墨夜思·水乡夜渡：津渡小楼、星火瓜州） =================
   美术立意：水墨夜思色板写「斜月夜江的渡口」——底色 #0d1117、雾 #0e141e～#131a26 系，
   accent=#a8b4c0（银青水月）只落在斜月晕/边缘光/楼窗灯晕/水月反光/UI 上，全页近零饱和。
   与已有水墨夜思页第一眼可区分：不做舟夜孤灯碎星（zhouye）、不做雨夜棋枰灯花（yueke）、
   不做古寺竹径（ti-poshansi）——做「渡口栈桥+临江小山楼+空阔夜江+远岸三点渔火」。
   境壹（近泊）：夜泊金陵渡——栈桥入江、渡船夜泊，小山楼临江一点暖窗，斜月初上，江雾横腰。
   境贰（远望·标志性瞬间+末境可点击）：潮落江空、斜月西沉；点击：横江夜雾散开，
   瓜州方向两三点星火次第亮起（火苗微颤+水面微光倒影）。 */

/* —— 小山楼 makeXiaoshanlou(o)：临江小楼（台基+底层楼身+腰檐平座栏杆+上层楼身+四阿顶，
   合批 1 mesh）——「金陵津渡小山楼」；楼头一扇暖窗+灯晕+一点暖光（孤窗是近岸唯一暖点） */
function makeXiaoshanlou(o){
  o=o||{};
  const w=o.w===undefined?4.6:o.w;
  const B=new GeoBag();
  const sill=new THREE.BoxGeometry(w*1.32,0.55,w*0.98);
  sill.translate(0,0.27,0); B.put(sill,0x1a2330);
  const body1=new THREE.BoxGeometry(w,2.35,w*0.66);
  body1.translate(0,1.72,0); B.put(body1,0x222d3f);
  const deck=new THREE.BoxGeometry(w*1.14,0.16,w*0.84);
  deck.translate(0,3.02,0); B.put(deck,0x2a3850);
  for(let i=0;i<7;i++){
    const px=-w*0.48+i*w*0.16;
    const post=new THREE.CylinderGeometry(0.055,0.07,0.78,5);
    post.translate(px,3.48,w*0.36); B.put(post,0x1c2634);
  }
  const rail=new THREE.BoxGeometry(w*1.06,0.07,0.07);
  rail.translate(0,3.86,w*0.36); B.put(rail,0x30405a);
  const rail2=new THREE.BoxGeometry(w*1.06,0.07,0.07);
  rail2.translate(0,3.86,-w*0.36); B.put(rail2,0x30405a);
  const body2=new THREE.BoxGeometry(w*0.76,1.95,w*0.52);
  body2.translate(0,4.07,0); B.put(body2,0x1e2939);
  const roof=new THREE.ConeGeometry(w*0.88,1.75,4);
  roof.rotateY(Math.PI/4); roof.scale(1.18,1,0.84); roof.translate(0,5.92,0); B.put(roof,0x16202e);
  const finial=new THREE.SphereGeometry(0.15,6,5);
  finial.translate(0,6.9,0); B.put(finial,0x39465c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0xa8b4c0,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  /* 楼头暖窗：楼上旅人的一点灯火（近岸唯一暖点；初值=最大，每帧写必乘 k） */
  const winOp=o.winOp===undefined?0.68:o.winOp;
  const win=new THREE.Mesh(new THREE.PlaneGeometry(w*0.13,w*0.17),
    new THREE.MeshBasicMaterial({color:o.winC===undefined?0xd9c9a0:o.winC,transparent:true,opacity:winOp}));
  win.position.set(w*0.17,4.25,w*0.263); g.add(win);
  const wg=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd9c9a0,
    transparent:true,opacity:0.08,depthWrite:false}));
  wg.scale.set(3.0,3.0,1); wg.position.set(w*0.17,4.25,w*0.55); g.add(wg);
  const lamp=new THREE.PointLight(0xd9c9a0,o.lamp===undefined?0.55:o.lamp,26);
  lamp.position.set(w*0.17,4.25,w*1.1); g.add(lamp);
  const ph=seedRnd(o.seed===undefined?22201:o.seed)()*6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k, fl=0.86+0.14*Math.sin(t*2.2+ph);
    win.material.opacity=kk*winOp*fl;
    wg.material.opacity=kk*0.10*fl;
    lamp.intensity=kk*(o.lamp===undefined?0.55:o.lamp)*fl;
  };
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 渡口栈桥 makeDukou(o)：木栈桥（板面一串+两排木桩，合批 1 mesh）自岸缘探入江心 */
function makeDukou(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22211:o.seed);
  const len=o.len===undefined?24:o.len, w=o.w===undefined?3.0:o.w;
  const B=new GeoBag();
  const n=Math.max(5,Math.round(len/2.4));
  for(let i=0;i<n;i++){
    const z=-len*(i/(n-1));
    const plank=new THREE.BoxGeometry(w,0.14,2.2);
    plank.translate(0,0.55,z); B.put(plank,shadeColor(0x323f58,0.85+0.30*R()));
  }
  for(let s=-1;s<=1;s+=2){
    for(let i=0;i<=n;i++){
      const pile=new THREE.CylinderGeometry(0.10,0.13,2.1,6);
      pile.translate(s*w*0.42,-0.45,-len*(i/n)+0.6);
      B.put(pile,shadeColor(0x1a2230,0.9+0.2*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x36445c,emissive:0x04070c}),{c:0xa8b4c0,i:o.rim===undefined?0.12:o.rim,p:2.4})));
  g.position.set(o.x===undefined?0:o.x,o.y===undefined?-0.75:o.y,o.z===undefined?0:o.z);
  return g;
}

/* —— 渡船 makeDuchuan(o)：方头平底渡船（船身+上翘艏艉+矮篷+横凳+橹+系桩，合批 1 mesh），
   夜泊于栈桥侧——与舟夜页的尖头渔舟剪影可区分 */
function makeDuchuan(o){
  o=o||{};
  const L=o.L===undefined?6.6:o.L, W=o.W===undefined?2.0:o.W;
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(L,0.78,W);
  hull.translate(0,0.39,0); B.put(hull,0x1c2534);
  const bow=new THREE.BoxGeometry(1.7,0.72,W*0.9);
  bow.rotateZ(-0.40); bow.translate(L*0.5+0.6,0.62,0); B.put(bow,0x222c3e);
  const stern=new THREE.BoxGeometry(1.5,0.68,W*0.9);
  stern.rotateZ(0.36); stern.translate(-L*0.5-0.5,0.58,0); B.put(stern,0x222c3e);
  const canopy=new THREE.CylinderGeometry(0.60,0.64,L*0.40,10,1,true,0,Math.PI);
  canopy.rotateZ(Math.PI/2); canopy.scale(1,1.3,1.06); canopy.translate(-0.3,0.86,0);
  B.put(canopy,0x253044);
  const bench=new THREE.BoxGeometry(W*0.78,0.10,0.52);
  bench.translate(1.5,0.86,0); B.put(bench,0x2a3346);
  const lu=new THREE.CylinderGeometry(0.035,0.05,3.3,5);
  lu.rotateZ(0.52); lu.translate(L*0.36,0.55,W*0.32); B.put(lu,0x1a2230);
  const moor=new THREE.CylinderGeometry(0.06,0.08,0.8,5);
  moor.translate(L*0.5+1.2,0.95,0); B.put(moor,0x161e2c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36445c,emissive:0x04070c,side:THREE.DoubleSide}),{c:0xa8b4c0,i:o.rim===undefined?0.14:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 江雾横带 makeJiangwu(o)：伏在江面的夜雾 Sprite 横带（可被「散开」：e 0→1 时透明度退尽），
   拦在江心与远岸之间——「潮落夜江」的空阔与「星火」藏身之处 */
function makeJiangwu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22241:o.seed);
  const n=o.n===undefined?8:o.n;
  const spread=o.spread===undefined?[210,9,54]:o.spread;
  const pos=o.pos===undefined?[0,2.0,-70]:o.pos;
  const scale=o.scale===undefined?62:o.scale;
  const color=o.color===undefined?0x2a3648:o.color;
  const op0=o.op===undefined?0.13:o.op;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:color,transparent:true,
      opacity:op0*(0.5+0.5*R()),depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set(pos[0]+(R()-0.5)*spread[0],
      pos[1]+(R()-0.5)*spread[1]*0.5,
      pos[2]+(R()-0.5)*spread[2]);
    const sc=scale*(0.6+0.9*R());
    s.scale.set(sc,sc*0.34,1); s.renderOrder=5;
    g.add(s); items.push({m:m,seed:R()*100,op:m.opacity});
  }
  g.update=function(t,k,e){
    const kk=k===undefined?1:k, ee=e===undefined?0:e;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.m.opacity=kk*it.op*(1-0.94*ee)*(0.72+0.28*Math.sin(t*0.21+it.seed));
    }
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 瓜州星火 makeXinghuo(o)：远岸两三点渔火（每点=火核+晕圈+水面微光倒影，均 fog:false
   如星月点名；初值=最大，点击前由 rv=0 压到 0，点击后随 reveal 次第亮起、火苗微颤） */
function makeXinghuo(o){
  o=o||{};
  const pts=o.pts===undefined?[[-30,7.5,-102],[-12,6.5,-108],[30,8.5,-98]]:o.pts;
  const coreC=o.coreC===undefined?0xf2c888:o.coreC;
  const haloC=o.haloC===undefined?0xe0a860:o.haloC;
  const reflC=o.reflC===undefined?0xc9a05c:o.reflC;
  const g=new THREE.Group(), items=[];
  const R=seedRnd(o.seed===undefined?22251:o.seed);
  for(let i=0;i<pts.length;i++){
    const core=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:coreC,
      transparent:true,opacity:1.0,depthWrite:false,fog:false}));
    core.scale.set(5.5,5.5,1); core.position.set(pts[i][0],pts[i][1],pts[i][2]);
    core.renderOrder=2; g.add(core);
    const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:haloC,
      transparent:true,opacity:0.30,depthWrite:false,fog:false}));
    halo.scale.set(26,26,1); halo.position.set(pts[i][0],pts[i][1],pts[i][2]);
    halo.renderOrder=2; g.add(halo);
    const refl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:reflC,
      transparent:true,opacity:0.18,depthWrite:false,fog:false}));
    refl.scale.set(2.6,22,1); refl.position.set(pts[i][0],pts[i][1]-9.5,pts[i][2]+2.5);
    refl.renderOrder=3; g.add(refl);
    items.push({core:core,halo:halo,refl:refl,ph:R()*6.283});
  }
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const on=Math.max(0,Math.min(1,(r-(0.10+i*0.26))/0.28));
      const tw=0.82+0.18*Math.sin(t*(1.2+i*0.35)+it.ph*7.0);
      it.core.material.opacity=kk*1.0*on*tw;
      it.halo.material.opacity=kk*0.30*on*tw;
      it.refl.material.opacity=kk*0.18*on*(0.70+0.30*Math.sin(t*2.1+it.ph*3.0));
    }
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* 夜泊行人：全诗贯穿的同一造型（青灰袍、幞头；每次 build 新建材质） */
function tjdFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x28324a,belt:0x6a7c96,skin:0xd3b294,collar:0x9aa8ba,
    hair:0x12161e,hat:'幞头',rimC:0xa8b4c0,rim:0.45,noProp:true,scale:scale===undefined?1.8:scale});
}

/* 远岸横陈 makeYuan(o)：瓜州方向的低平远岸（低多峰脊，两层，带雾骨相） */
function makeYuan(o){
  o=o||{};
  return makeRange({r:o.r===undefined?210:o.r,h:o.h===undefined?8:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?22261:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x1c2634,
    fogK:o.fogK===undefined?0.58:o.fogK,glowK:0.04,glow:0xa8b4c0,
    y:o.y===undefined?-11:o.y,order:-6});
}

function bCover(){ // 卷首 · 夜渡远望：栈桥入江、渡船夜泊、小山楼一点暖窗、斜月初上、江雾横腰
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:90,amp:0.14,freq:0.15,speed:0.36,flow:[0.30,0.05],spec:0.85,
    deep:0x05080e,shallow:0x0b1420,skyc:0x121a27,moonDir:[-0.26,0.12,-0.95]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xaebfd4);
  water.mesh.position.set(0,-0.52,-130); g.add(water.mesh);
  const grd=makeGround({r:78,c1:0x0a0f18,c2:0x151d2b,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,62);
  const yuan=makeYuan({r:230,h:8,seed:22262}); yuan.g.position.set(0,0,-160); g.add(yuan.g);
  const lou=makeXiaoshanlou({scale:1.7,rim:0.18,seed:22263}); lou.position.set(13,-0.28,-4);
  lou.rotation.y=-0.30; g.add(lou);
  const dock=makeDukou({x:3.2,z:-9,len:26,seed:22264}); g.add(dock);
  const chuan=makeDuchuan({}); chuan.position.set(7.8,-0.62,-37); chuan.rotation.y=0.14; g.add(chuan);
  const crowd=makeCrowd({n:2,rect:[11.6,-8,2.4,1.8],seed:22265,color:0x1c2534,rimC:0xa8b4c0,
    rim:0.18,sMin:0.55,sMax:0.62,y:-0.28});
  g.add(crowd.mesh);
  const poet=tjdFigure(1.55); poet.position.set(3.2,-0.20,-16); poet.rotation.y=3.1; g.add(poet);
  const jw=makeJiangwu({n:8,pos:[0,2.0,-74],seed:22266}); g.add(jw.g);
  const motes=makeGlow({n:30,box:[170,18,66],pos:[0,9,-36],color:0x9fb2c8,size:4.4,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:28,n:12,d:5,color:0x05080e,seed:22267,sway:0.8,rim:0.10,rimC:0xa8b4c0});
  fg1.g.position.set(-10,-1.2,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.6,w:11,d:5,color:0x05080e,seed:22268,rim:0.10,rimC:0xa8b4c0});
  fg2.g.position.set(12.5,-1.5,12); g.add(fg2.g);
  addLights(g,{c:0xa8bccf,i:0.36,p:[-42,52,-55]},{c:0x18202e,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    lou.userData.update(t,k); crowd.update(t); poet.update(t,k);
    jw.update(t,k,0); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bJindu(){ // 壹 · 津渡小楼 —— 金陵津渡小山楼，一宿行人自可愁：栈桥、泊船、楼头暖窗、斜月初上
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:96,amp:0.13,freq:0.16,speed:0.34,flow:[0.30,0.05],spec:0.80,
    deep:0x05080e,shallow:0x0c1520,skyc:0x121a27,moonDir:[-0.26,0.12,-0.95]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xaebfd4);
  water.mesh.position.set(0,-0.52,-120); g.add(water.mesh);
  const grd=makeGround({r:80,c1:0x0a0f18,c2:0x161e2c,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,64);
  const yuan=makeYuan({r:250,h:9,seed:22272}); yuan.g.position.set(-10,0,-165); g.add(yuan.g);
  /* 小山楼：临江而立，楼头一点暖窗（「一宿行人」的居处） */
  const lou=makeXiaoshanlou({scale:1.5,rim:0.20,seed:22273}); lou.position.set(14.5,-0.28,-10);
  lou.rotation.y=-0.35; g.add(lou);
  /* 栈桥入江 + 泊船夜系 */
  const dock=makeDukou({x:2.8,z:-9,len:26,seed:22274}); g.add(dock);
  const chuan=makeDuchuan({}); chuan.position.set(7.2,-0.62,-37); chuan.rotation.y=0.12; g.add(chuan);
  /* 舟子收缆 / 泊客二人剪影，愈显渡口夜静 */
  const crowd=makeCrowd({n:2,rect:[10.2,-9.5,2.4,1.8],seed:22275,color:0x1c2534,rimC:0xa8b4c0,
    rim:0.18,sMin:0.55,sMax:0.62,y:-0.28});
  g.add(crowd.mesh);
  /* 行人立于栈桥，望江生愁 */
  const poet=tjdFigure(1.75); poet.position.set(2.8,-0.20,-15); poet.rotation.y=3.05; g.add(poet);
  /* 江雾横腰 + 微尘 */
  const jw=makeJiangwu({n:6,spread:[180,8,44],pos:[0,1.8,-58],scale:54,op:0.11,seed:22276}); g.add(jw.g);
  const motes=makeGlow({n:30,box:[160,18,62],pos:[0,9,-34],color:0x9fb2c8,size:4.4,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:11,d:5,color:0x05080e,seed:22277,sway:0.85,rim:0.10,rimC:0xa8b4c0});
  fg1.g.position.set(-9.5,-1.2,11); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05080e,seed:22278,rim:0.10,rimC:0xa8b4c0});
  fg2.g.position.set(12,-1.5,11.5); g.add(fg2.g);
  addLights(g,{c:0xa8bccf,i:0.40,p:[-40,52,-50]},{c:0x18202e,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    lou.userData.update(t,k); crowd.update(t); poet.update(t,k);
    jw.update(t,k,0); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bWanghuo(){ // 贰（末境·可点击）· 星火瓜州 —— 潮落夜江斜月里，两三星火是瓜州：点击江雾散开、星火次第亮起
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:96,amp:0.12,freq:0.15,speed:0.30,flow:[0.28,0.04],spec:0.78,
    deep:0x05080e,shallow:0x0c1520,skyc:0x131c2a,moonDir:[-0.28,0.10,-0.95]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xb4c4d8);
  water.mesh.position.set(0,-0.52,-140); g.add(water.mesh);
  const grd=makeGround({r:76,c1:0x090e16,c2:0x141c2a,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,62);
  /* 瓜州远岸：低平横陈（星火的来处） */
  const yuan=makeYuan({r:230,h:7,peaks:4,seed:22282}); yuan.g.position.set(6,0,-140); g.add(yuan.g);
  const yuan2=makeYuan({r:300,h:12,peaks:3,seed:22283,y:-14}); yuan2.g.position.set(-30,0,-190); g.add(yuan2.g);
  /* 小山楼退居右缘（凭窗人所在），栈桥泊船仍在 */
  const lou=makeXiaoshanlou({scale:1.35,rim:0.16,seed:22284,lamp:0.4}); lou.position.set(13.5,-0.28,-9);
  lou.rotation.y=-0.45; g.add(lou);
  const dock=makeDukou({x:4.6,z:-10,len:20,seed:22285}); g.add(dock);
  const chuan=makeDuchuan({scale:0.9}); chuan.position.set(8.6,-0.62,-31); chuan.rotation.y=0.18; g.add(chuan);
  /* 标志性瞬间：瓜州星火三点（点击后次第亮起），江雾横带散开 */
  const huos=makeXinghuo({pts:[[-30,7.5,-102],[-12,6.5,-108],[30,8.5,-98]],seed:22286});
  g.add(huos.g);
  const jw=makeJiangwu({n:10,spread:[230,10,44],pos:[0,2.4,-84],scale:74,op:0.20,seed:22287});
  g.add(jw.g);
  /* 行人立于左前岸石，极目远望 */
  const poet=tjdFigure(1.6,'指月'); poet.position.set(-7.6,-0.26,-4.5); poet.rotation.y=2.95; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:5,color:0x06090f,seed:22288,rim:0.12,rimC:0xa8b4c0});
  rock.g.position.set(-8.8,-1.5,-3.2); g.add(rock.g);
  /* 夜气横流 + 微尘 */
  const wind=makeFlow({n:300,box:[110,9,44],pos:[0,3.0,-24],color:0x5f6e84,size:15,speed:3.6,maxA:0.09});
  g.add(wind.points);
  const motes=makeGlow({n:30,box:[170,18,68],pos:[0,9,-40],color:0x9fb2c8,size:4.4,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:11,d:5,color:0x05080e,seed:22289,sway:0.9,rim:0.10,rimC:0xa8b4c0});
  fg1.g.position.set(-11,-1.3,10); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x05080e,seed:22290,rim:0.10,rimC:0xa8b4c0});
  fg2.g.position.set(12.5,-1.5,11); g.add(fg2.g);
  addLights(g,{c:0xa8bccf,i:0.38,p:[-44,50,-48]},{c:0x18202e,i:0.60});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/2.4);
      const rv=ctl.reveal, e=rv*rv*(3-2*rv);
      huos.update(t,k,rv);
      jw.update(t,k,e);
      water.update(t); yuan.update(t,0); yuan2.update(t,0);
      lou.userData.update(t,k);
      wind.mat.uniforms.uMaxA.value=k*(0.09+0.05*e);
      wind.update(t); motes.update(t);
      poet.update(t,k); rock.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.12);
        pluck(5,0.05,0.10); pluck(3,0.55,0.08); pluck(1,1.10,0.07);   // 星火次第、如更点三响
        const fl=$('#flash'); fl.textContent='潮落夜江斜月里 两三星火是瓜州';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x060a12),hor:C(0x121a28),bot:C(0x04070c),fog:C(0x0f151f),fd:0.0054,star:0.32,
  moon:new THREE.Vector3(-52,40,-190),ms:1.35,mph:0.34,mhaze:0.16,dirC:C(0xa8bccf),dirI:0.38,
  dirP:new THREE.Vector3(-40,55,-55),ambC:C(0x18202e),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8.6,32],t:[0,8.2,24],lf:[2,7.6,-12],lt:[-2,8.2,-26]},
  sky:()=>SK({fd:0.0048,star:0.28}) },
{ name:'津渡小楼',dwell:16,river:0.02,build:bJindu,
  cam:{f:[1.8,6.4,17],t:[0.5,6.0,9],lf:[-0.5,5.6,-12],lt:[-2.5,6.0,-26]},
  sky:()=>SK({fd:0.0056,star:0.30,ms:1.3,mph:0.34,mhaze:0.18,
    moon:new THREE.Vector3(-50,44,-185),dirC:C(0xa8bccf),dirI:0.40,
    ambC:C(0x18202e),ambI:0.62}) },
{ name:'星火瓜州',dwell:19,river:0.02,build:bWanghuo,
  cam:{f:[0,7.2,14],t:[0,6.9,-4],lf:[0,6.6,-28],lt:[0,7.0,-44]},
  sky:()=>SK({fd:0.0052,star:0.36,ms:1.25,mph:0.34,mhaze:0.16,
    moon:new THREE.Vector3(-70,56,-185),dirC:C(0xa8bccf),dirI:0.38,
    ambC:C(0x161e2c),ambI:0.60}) },
];
"""
