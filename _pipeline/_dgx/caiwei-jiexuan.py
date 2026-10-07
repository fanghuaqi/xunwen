# -*- coding: utf-8 -*-
"""caiwei-jiexuan.py —— 《采薇·节选》（先秦·诗经·小雅，no.255，水墨夜思）生成配置
四境（末章八句，两句一境）：昔往杨柳（标志性瞬间的前一半：去时的春天）、
今来雨雪（后一半：归来的冬天）、行道迟迟（长路饥渴）、
莫知我哀（末境点击：今昔四时对切——杨柳与雨雪两景交叠）。
核心创意「同一条归途上的四时对切」：一条归家长道贯穿四境（母题），
境壹与境贰同一排柳树同位对照——带叶春柳（依依）↔ 叶尽冬柳（霏霏），
镜头与天空随之冷暖对切；境肆点击：春柳记忆淡现、柳絮飘起而雨雪未停，
两景交叠于归人一身——「昔往」「今来」十六个字的物是人非。
水墨夜思全套色板：底色 #0d1117、雾 #111823～#141b27 系、文字 #dfe6f0，accent=#98aec8
（queue 分配强调色，月银青灰）只落在雪光/柳梢边缘光/远村灯火雪帽/人物边缘光/UI 上，
全页近零饱和；唯春柳一侧一抹极克制的灰绿（柳叶 0x667d68 系+柳色微光 0x7d9080+柳絮
0xaab9a2）——杨柳（春·记忆）与雨雪（冬·眼前）的对切就是末章前四句本身，
也是全页唯一的彩色正用。
与已有水墨夜思页第一眼可区分：不做落木长江登高（denggao）、不做梅雨蛙声敲棋
（yueke）、不做满月江楼水天一色（jianglou-ganjiu）、不做夜台一瑟四典如梦（jinse）、
不做孤山梅影暗香（shanyuan-xiaomei）、不做玉笛光缕柳丝漫卷（chunye-luocheng）、
不做古寺竹径/雨前危城/渡口渔火——做「归途长道+一排柳树一春一冬」的戍卒归人视角。
标志性瞬间（queue moment：昔往杨柳依依今来雨雪霏霏——四时对切）：
境壹带叶春柳依依（柳色微光+柳絮）↔ 境贰同位冬柳霏霏（大雪），
末境点击把两景叠在同一画面里交叠流转。
末境点击（queue interact：点击今昔对切——杨柳与雨雪两景交叠）：点击画面——
①同一排柳回到带叶的春天（记忆组淡现，组 visible=false 硬关）；②柳絮缓起、
柳色微光漫开；③雨雪收势三成但仍落——春柳与冬雪叠于一身；④「昔我往矣 杨柳依依
今我来思 雨雪霏霏」题字同现，下行三叠拨音如长叹。
考点钉子：思 sì（语助词）/雨 yù（落下）/霏 fēi/载 zài（小测第 3 题落点）；
《诗经·小雅·采薇》全诗六章、本篇为末章+重章叠句（第 4 题）；
「昔往今来」以乐景写哀、物是人非的戍卒之悲（第 5 题）。
多音字：雨雪霏霏→玉雪霏霏、今我来思→今我来四、载渴载饥→再渴再饥（tts.json，
按教材读音钉同音替换）。"""
import os

META = dict(
    N=4, slug='caiwei-jiexuan', title='采薇·节选', dyn='先秦 · 诗经', brand_author='诗 经',
    gold_rgb='152,174,200',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#98aec8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(152,174,200,.26);
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
        ('0x0a1526', '0x111823', 4),
    ],
    tip='轻点画面 / 按空格 —— 今昔对切，杨柳雨雪两景交叠',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看昔往杨柳与今来雨雪四时对切、两景交叠',
    cover_read='采薇·节选。先秦，诗经。昔我往矣，杨柳依依。今我来思，雨雪霏霏。行道迟迟，载渴载饥。我心伤悲，莫知我哀！',
    cover_p1='四重意境，随诗句次第展开：回想当年离家出征，杨柳正随风轻摆、依依不舍；如今踏上归途，漫天雨雪纷纷扬扬；归路漫长，走一步又渴又饿；心中悲伤，却没有谁知道他的哀痛。',
    cover_p2='边读诗，边跟着一位久戍归来的士兵走完这条长路：去时杨柳依依，来时雨雪霏霏——读懂「昔往」「今来」十六个字的物是人非，就读懂了《诗经》里最动人的这四句。',
    end_h2='杨柳 · 雨雪', cn_word='四',
    words_js="['再走一次归途','初识采薇，尚需共读','渐入诗境，再诵几遍','杨柳雨雪，今昔渐明','已解戍卒归途之悲','莫知我哀，千古同叹']",
    sky_atmo='0x1e2836',
)

POEM_JS = """const POEM = [
{ name:'昔往杨柳', jing:'回想当年离家出征的时候，杨柳随风轻摆，依依不舍 —— 昔、往矣、依依。（杨柳 · 依依 · 昔往）（四时对切·前一半：去时的春天）',
  segs:[
   {c:'昔我往矣，', p:py('xī wǒ wǎng yǐ')},
   {c:'杨柳依依。', p:py('yáng liǔ yī yī')}],
  read:'昔我往矣，杨柳依依。',
  yisi:'回想当年我离家出征的时候，杨柳正随风轻拂、依依不舍。——「昔我往矣」起笔回望：一个「昔」字把镜头推回多年前的春天。「杨柳依依」既是实景——春柳柔软、随风摇曳；又是深情——柳条「依依」似也挽留行人，仿佛连杨柳都舍不得他走。这四句要与下一境对照着读：「昔」对「今」，「往」对「来」，「杨柳依依」对「雨雪霏霏」——起句有多温柔，对照就有多锋利。',
  zhu:[['昔','从前、当年——指出征离家之时；与下一句的「今」相对，一字之间隔着整整一场战争'],['往矣','去了、走了——「矣」是语气词，轻轻一声收住，有无穷感慨'],['依依','柳条轻柔、随风摇曳的样子——又含留恋不舍之意：杨柳仿佛依依惜别，不忍征人离去'],['杨柳','春日柳树。古人送别有折柳之俗，「柳」谐音「留」——柳既是眼前春色，也暗含挽留之意'],['以乐景写哀','离家时杨柳依依是乐景，心中却是生离之苦——以乐景写哀，其哀倍增，这四句历来被推为《诗经》中最动人的名句']] },
{ name:'今来雨雪', jing:'如今我走在归来的路上，雨雪漫天，纷纷扬扬 —— 今、来、雨雪霏霏。（雨雪 · 霏霏 · 今来）（四时对切·后一半：归来的冬天）',
  segs:[
   {c:'今我来思，', p:py('jīn wǒ lái sì')},
   {c:'雨雪霏霏。', p:py('yù xuě fēi fēi')}],
  read:'今我来思，雨雪霏霏。',
  yisi:'如今我终于走在归来的路上，漫天雨雪纷纷扬扬。——与上句一字一景地对看：去时是杨柳依依的春天，归来是雨雪霏霏的冬天。十六个字两番景象，把物是人非的怆痛全压在景物的错位里：走的时候正是好时节，回来时天地萧瑟——岁月、青春、家人多年的等待，都在这一去一回之间耗尽了。归来本该是喜事，可天地却以一场大雪相迎，近乡的百感交集，尽在这片无声的霏霏之中。',
  zhu:[['思','句末语助词，没有实义——读 sì，与「悠哉悠哉」的「哉」同类，《诗经》常见'],['雨雪','雨（yù）作动词：落下的意思——「雨雪」即「下雪」；教材注音「雨」读 yù'],['霏霏','雪下得又大又密的样子——与「依依」相对：一柔一烈，一春一冬'],['今来','如今归来——与「昔往」对举；同一条路、同一排柳，去时着春色，归来披冬雪'],['重章叠句的底色','《采薇》全诗以重章叠句回环推进，末章却在此陡然一转——由眼前冬雪回望昔日春柳，时空错落，是全诗最见笔力的一笔']] },
{ name:'行道迟迟', jing:'归路漫长，脚步越来越沉，走一步又渴又饿 —— 行道、迟迟、载渴载饥。（长路 · 饥渴 · 迟迟）',
  segs:[
   {c:'行道迟迟，', p:py('xíng dào chí chí')},
   {c:'载渴载饥。', p:py('zài kě zài jī')}],
  read:'行道迟迟，载渴载饥。',
  yisi:'归路漫长，我走得越来越慢，一路上又渴又饿。——「迟迟」既是脚步慢，也是心绪沉：路未必变长了，是盼了多年的人临近家门，反而百感交集、举步维艰。「载渴载饥」——「载……载……」即又……又……，饥渴交加不只是身体的煎熬，更是多年戍边苦楚一齐涌上来的滋味。前两境写天地（杨柳、雨雪），这一境落到自己身上：战争结束了，可它留给人的损耗，要在这条长路上一步一步偿还。',
  zhu:[['行道','归家的道路——即归人所走的漫漫长途'],['迟迟','缓慢、走不动的样子——脚步迟缓，也含心事重重、近乡情怯之意'],['载……载……','一边……一边……；又……又……——「载渴载饥」即又渴又饿，饥渴交加。载，读 zài'],['渴饥','渴与饿——久戍归来的士兵粮尽体乏，归途中备受煎熬，与前文的「雨雪霏霏」相呼应']] },
{ name:'莫知我哀', jing:'我心中的悲伤，却没有谁知道我的哀痛 —— 伤悲、莫知、我哀。（莫知我哀 · 物是人非）（标志性瞬间：今昔四时对切）（末境点击画面：昔往杨柳与今来雨雪两景交叠）',
  segs:[
   {c:'我心伤悲，', p:py('wǒ xīn shāng bēi')},
   {c:'莫知我哀！', p:py('mò zhī wǒ āi')}],
  read:'我心伤悲，莫知我哀！',
  yisi:'我心中的悲伤，没有人能够知道。——全诗到此由景入情，直抒胸臆：一路的雨雪、饥渴都还可以忍受，最难忍受的是「莫知我哀」——戍卒终于归来，可当年送他出征的杨柳仿佛还依依着（春天只留在记忆里了），而人事已非；他的悲哀无处诉说，也无人能懂。不说「家破」，不说「人亡」，只说没人懂我——把归来者一肚子的沧海桑田，收在一个「哀」字的沉默里。这一个叹号，是整部《诗经》里最沉重的一声。',
  zhu:[['伤悲','悲伤——「我心伤悲」直陈其痛，是全诗情感的落点'],['莫知我哀','没有人知道我的哀痛——「莫」：没有谁；悲到深处，是无处诉说的孤独'],['末章','《采薇》全诗共六章，写戍卒从出征到归来的全过程；课本节选的是末章（即第六章），也是全诗情感最沉痛的部分'],['千古名句','东晋谢玄被问《诗经》中何句最佳，即举「昔我往矣，杨柳依依；今我来思，雨雪霏霏」——十六个字写尽物是人非，历代推为三百篇压卷之笔']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「昔我往矣」的下一句是？', o:['杨柳依依','今我来思','雨雪霏霏'], a:0},
 {q:'「行道迟迟」的下一句是？', o:['我心伤悲','载渴载饥','莫知我哀'], a:1},
 {q:'「今我来思，雨雪霏霏」的读音，完全正确的一项是？', o:['思读 sì（句末语助词，无实义）；雨读 yù（落下的意思，「雨雪」即下雪）；霏读 fēi（雪下得又大又密的样子）','思读 sī（思念的意思）；雨读 yǔ（雨水的雨）；霏读 fěi（微小的样子）','思读 shì（「是」的通假字）；雨读 yǔ；霏读 fēi（形容风声）'], a:0},
 {q:'关于《采薇》与这首诗的文学常识，下列说法正确的是？', o:['《采薇》出自《诗经·小雅》，全诗共六章，课本节选的是末章；诗中多用重章叠句，叠字「依依」「霏霏」相映成趣，回环往复、一唱三叹','《采薇》出自《楚辞·九歌》，是屈原祭祀湘水之神时所唱，全诗共三章','《采薇》是汉代乐府民歌，收录于《乐府诗集》，相传为曹植所作'], a:0},
 {q:'「昔我往矣，杨柳依依。今我来思，雨雪霏霏」历来被推为千古名句。对这四句的理解，最恰当的一项是？', o:['单纯写景：记录了两次出行的时间与天气，出发时是春天，回来时下大雪','以乐景写哀、以哀景写哀：去时杨柳依依的春光愈美，愈见离家之痛；归来时雨雪霏霏的萧瑟，愈见物是人非之悲——一往一来、一春一冬，把戍卒半生的沧桑与「莫知我哀」的孤独写尽','用对比说明出行要挑好天气，回来遇上坏天气只是运气不好，与情感无关'], a:1},
];
"""

SCENES_JS = """/* ================= 采薇·节选 · 四境场景（水墨夜思·归途四时对切：昔往杨柳、今来雨雪、行道迟迟、莫知我哀） =================
   美术立意：水墨夜思色板写「同一条归途上的一春一冬」——底色 #0d1117、雾 #111823～#141b27 系，
   accent=#98aec8（月银青灰）只落在雪光/柳梢边缘光/远村灯火雪帽/边缘光/UI 上，全页近零饱和；
   唯春柳（记忆）一侧一抹极克制的灰绿（柳叶 0x667d68 系+柳色微光 0x7d9080+柳絮 0xaab9a2）。
   母题贯穿：一条归家长道（路中深、路缘积雪微亮、车轮辙痕）+一排柳树（位置四境不变），
   境壹带叶春柳（依依）↔ 境贰同位冬柳叶尽（霏霏）——同位对照即「四时对切」；
   境叁镜头压低随长路无尽（行道迟迟·远村依稀）；境肆（末境可点击）点击：
   春柳记忆淡现+柳絮飘起而雨雪未停——杨柳与雨雪两景交叠于归人一身。
   自建大场景组全部放在骨架常驻远山环（z≈-260…-330）之前：远村 z≈-128、长路 z≈-165 止，
   远山环带 makeYuanling 亦只置 z≈-165，不被 bgRange 遮挡。 */

/* —— 归家长道 makeDaolu(o)：一条自近及远的土路（顶点色：路中踩实的暗、路缘积雪微亮，
   车辙更深；MeshPhongMaterial 自动吃场景雾）——全诗母题：戍卒的归途。四境同一条路 */
function makeDaolu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25501:o.seed);
  const z0=o.z0===undefined?18:o.z0, z1=o.z1===undefined?-150:o.z1;
  const rows=o.rows===undefined?24:o.rows;
  const w0=o.w0===undefined?7.2:o.w0, w1=o.w1===undefined?1.0:o.w1;
  const bend=o.bend===undefined?6:o.bend, kf=o.kf===undefined?0.016:o.kf;
  const prof=[[-1.0,0x46536b],[-0.58,0x2b3850],[-0.22,0x212d40],[0,0x1b2536],
              [0.22,0x212d40],[0.58,0x2b3850],[1.0,0x46536b]];
  const pos=[],col=[],idx=[];
  for(let i=0;i<=rows;i++){
    const v=i/rows, z=z0+(z1-z0)*v;
    const w=w0+(w1-w0)*v;
    const cx=Math.sin((z+40)*kf)*bend*(1-v*0.5);
    for(let j=0;j<prof.length;j++){
      const p=prof[j], k=0.84+0.30*R();
      pos.push(cx+p[0]*w, 0.02, z);
      col.push(((p[1]>>16)&255)*k/255, ((p[1]>>8)&255)*k/255, (p[1]&255)*k/255);
    }
  }
  const W=prof.length;
  for(let i=0;i<rows;i++)for(let j=0;j<W-1;j++){
    const a=i*W+j;
    idx.push(a,a+1,a+W, a+1,a+W+1,a+W);
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  geo.setAttribute('color',new THREE.BufferAttribute(new Float32Array(col),3));
  geo.setIndex(idx);
  const mesh=new THREE.Mesh(geo,new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,shininess:4,specular:0x2a3850,emissive:0x04060a}));
  mesh.frustumCulled=false;
  return mesh;
}

/* —— 柳树 makeLiushu(o)：水墨柳（主干+斜出枝+垂落丝条合批 1 mesh；bare:false 带叶灰绿
   柳团=春柳，bare:true 叶尽丝枯+枝头一点雪帽=冬柳）；update 整树轻摇（依依）——
   境壹/境肆记忆组用带叶，境贰/境叁用冬柳；同 seed 同位置即「同一棵树」 */
function makeLiushu(o){
  o=o||{};
  const bare=!!o.bare;
  const R=seedRnd(o.seed===undefined?25511:o.seed);
  const h=o.h===undefined?5.2:o.h;
  const B=new GeoBag();
  const trunk=new THREE.CylinderGeometry(0.10,0.26,h,7);
  trunk.rotateZ(0.06+0.10*R()); trunk.translate(0,h*0.5,0);
  B.put(trunk,0x161d26);
  const nb=2+Math.floor(R()*2), tips=[];
  for(let b=0;b<nb;b++){
    const a=R()*6.283, len=h*(0.34+0.22*R()), y0=h*(0.62+0.22*R());
    const tx=Math.cos(a)*len, tz=Math.sin(a)*len*0.7, ty=y0+len*0.18;
    B.put(limbGeo([0,y0,0],[tx,ty,tz],0.085,0.045,5),shadeColor(0x161d26,1.15));
    tips.push([tx,ty,tz]);
  }
  tips.push([0,h*0.98,0]);
  const nS=bare?(7+Math.floor(R()*3)):(9+Math.floor(R()*4));
  for(let s=0;s<nS;s++){
    const tp=tips[Math.floor(R()*tips.length)];
    const dx=(R()-0.5)*2.6, dz=(R()-0.5)*2.0;
    const L=(1.4+R()*2.2)*(bare?1.15:1.0);
    const mx=tp[0]+dx*0.55, my=tp[1]-L*0.28, mz=tp[2]+dz*0.55;
    const ex=tp[0]+dx, ey=tp[1]-L, ez=tp[2]+dz;
    const c=shadeColor(0x1a222d,0.9+0.3*R());
    B.put(limbGeo(tp,[mx,my,mz],0.040,0.026,4),c);
    B.put(limbGeo([mx,my,mz],[ex,ey,ez],0.026,0.012,4),c);
    if(!bare){
      for(let l=0;l<6;l++){                       /* 垂丝上的灰绿柳团（春） */
        const t=0.30+0.62*(l/5);
        const lx=tp[0]+dx*t*(0.9+0.2*R()), ly=tp[1]-L*t, lz=tp[2]+dz*t*(0.9+0.2*R());
        const lf=new THREE.SphereGeometry(0.38+0.20*R(),5,4);
        lf.scale(1.5,0.42,0.7);
        lf.translate(lx,ly,lz);
        B.put(lf,shadeColor(0x748a74,0.72+0.55*R()));
      }
    }else if(R()<0.8){                            /* 冬柳枝头一点雪帽 */
      const sp=new THREE.SphereGeometry(0.13+0.07*R(),5,4);
      sp.scale(1.4,0.6,1.0);
      sp.translate(ex,ey,ez);
      B.put(sp,0xc9d5e4);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3a4c,emissive:0x04070c}),{c:0x98aec8,i:o.rim===undefined?0.15:o.rim,p:2.4})));
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.011*Math.sin(t*0.5+ph); };
  g.userData.update=g.update;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 霏霏落雪 makeLuoxue(o)：自写着色器（自上而下缓落+横向风漂；uMaxA 作雪势可收放，
   显式 vertexShader/fragmentShader 双挂；uFade 交给 setFade；NormalBlending——水墨暗底
   上 additive 会把雪洗成白棉团）——「雨雪霏霏」 */
const CW_SNOW_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uWind;
varying float vA;
void main(){
  vec3 p=position;
  float h=uBox.y;
  float fall=fract(uTime*uSpeed*(0.35+0.75*aSeed)+aSeed);
  p.y-=fall*h;
  p.x+=sin(uTime*(0.5+0.4*aSeed)+aSeed*43.0)*(0.8+1.4*aSeed)+uWind*uTime*(0.3+aSeed*0.5);
  p.x=mod(p.x+uBox.x*0.5,uBox.x)-uBox.x*0.5;
  p.z+=cos(uTime*0.4+aSeed*31.0)*1.2;
  vA=smoothstep(0.0,0.10,fall)*smoothstep(1.0,0.86,fall);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.75+0.25*sin(uTime*1.3+aSeed*50.0))*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeLuoxue(o){
  o=o||{};
  const n=o.n===undefined?200:o.n, box=o.box===undefined?[200,56,90]:o.box,
    pos=o.pos===undefined?[0,24,-44]:o.pos;
  const color=o.color===undefined?0xdfe8f4:o.color, size=o.size===undefined?2.2:o.size;
  const speed=o.speed===undefined?0.95:o.speed, wind=o.wind===undefined?1.1:o.wind,
    maxA=o.maxA===undefined?0.32:o.maxA;
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=size*(0.6+0.9*Math.random());
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:speed},uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uWind:{value:wind},uColor:{value:C(color)},uFade:{value:0},uMaxA:{value:maxA}},
    vertexShader:CW_SNOW_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points:points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 远村 makeYuanCun(o)：归途尽头的几户村舍剪影（雪帽微亮，合批 1 mesh）——
   「行道迟迟」：家就在那条路的尽头，却还没走到 */
function makeYuanCun(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25531:o.seed);
  const n=o.n===undefined?5:o.n, w=o.w===undefined?26:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=-R()*4;
    const bw=1.6+R()*1.4, bh=1.0+R()*0.7;
    const body=new THREE.BoxGeometry(bw,bh,bw*0.8); body.translate(x,bh*0.5,z); B.put(body,0x101724);
    const roof=new THREE.ConeGeometry(bw*0.85,0.5+R()*0.3,4); roof.rotateY(Math.PI/4);
    roof.translate(x,bh+0.30,z); B.put(roof,0x161d2b);
    if(R()<0.85){
      const cap=new THREE.ConeGeometry(bw*0.5,0.14,4); cap.rotateY(Math.PI/4);
      cap.translate(x,bh+0.62+R()*0.2,z); B.put(cap,0xb6c4d6);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x222c3c,emissive:0x04060a})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 远山一环 makeYuanling(o)：夜色深处的低平远山（两层，带雾骨相）——
   归途展开的天际；组放近（z≈-165 止），不被骨架常驻远山环（z≈-300）遮挡 */
function makeYuanling(o){
  o=o||{};
  return makeRange({r:o.r===undefined?240:o.r,h:o.h===undefined?11:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?25541:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x1e2836,
    fogK:o.fogK===undefined?0.60:o.fogK,glowK:0.04,glow:0xaebccd,
    y:o.y===undefined?-11:o.y,order:-6});
}

/* —— 春柳记忆组 makeJinxi(o)：末境点击的「昔往」幻境（同一排柳回到带叶的春天+
   柳色微光+柳絮；材质 opacity 初值=峰值、组 visible=false 硬关——fadeK 铁律
   初值=最大，点击前靠组隐藏无幻影）；update(t,k,env)：env 0→1 淡现——
   雨雪未停，杨柳与雨雪两景交叠 */
function makeJinxi(o){
  o=o||{};
  const g=new THREE.Group(), mats=[], anims=[], embs=[];
  const t1=makeLiushu({seed:25515,h:7.0,bare:false,rim:0.26,scale:1.15}); t1.position.set(-11,0,-20); t1.rotation.y=0.6;
  const t2=makeLiushu({seed:25516,h:6.2,bare:false,rim:0.26,scale:1.15}); t2.position.set(12.5,0,-30); t2.rotation.y=-1.1;
  g.add(t1); g.add(t2);
  const EMB_T=C(0x202c22);                       /* 记忆淡现时叶面的一层极淡绿光 */
  [t1,t2].forEach(function(tr){
    tr.traverse(function(ob){
      if(ob.isMesh&&ob.material){ ob.material.transparent=true; mats.push(ob.material); embs.push(ob.material.emissive.clone()); }
    });
    anims.push(function(t){ tr.update(t); });
  });
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x7d9080,
    transparent:true,opacity:0.14,depthWrite:false,fog:false}));
  haze.scale.set(86,32,1); haze.position.set(-5,7.5,-30); haze.renderOrder=2; g.add(haze);
  const cat=makeGlow({n:26,box:[44,9,24],pos:[-4,3.8,-22],color:0xb8c4ae,size:2.8,
    speed:0.05,rise:0.4,add:false,maxA:0.16});
  g.add(cat.points);
  g.visible=false;
  g.update=function(t,k,env){
    const kk=k===undefined?1:k, e=env===undefined?0:env;
    for(let i=0;i<mats.length;i++){
      mats[i].opacity=kk*e;
      mats[i].emissive.copy(embs[i]).lerp(EMB_T,e);   /* 叶面微光随记忆浮现 */
    }
    haze.material.opacity=kk*0.14*e;
    cat.mat.uniforms.uMaxA.value=0.16*e;
    for(let i=0;i<anims.length;i++)anims[i](t);
    g.visible=kk*e>0.004;
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* 归人：全诗贯穿的同一造型（灰袍、发髻——久戍的士兵；每次 build 新建材质） */
function cwFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2e3440,belt:0x56627a,skin:0xd6b18c,collar:0x8b99ac,
    hair:0x151820,hat:'发髻',rimC:0x98aec8,rim:0.42,noProp:true,scale:scale===undefined?1.6:scale});
}

function bCover(){ // 卷首 · 归途夜雪：一条长道没入霏雪，道旁一株带叶春柳隐在记忆里、两株冬柳立于眼前
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0e1320,c2:0x1c2637,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,-8);
  const yuan=makeYuanling({r:250,h:13,seed:25541}); yuan.g.position.set(0,0,-168); g.add(yuan.g);
  const road=makeDaolu({seed:25501}); g.add(road);
  /* 柳：封面即见一春（带叶·远）一冬（叶尽·近）两个时间 */
  const lw=makeLiushu({seed:25512,h:6.0,bare:false}); lw.position.set(-13,0,-34); lw.rotation.y=0.5; g.add(lw);
  const bw1=makeLiushu({seed:25513,h:5.6,bare:true}); bw1.position.set(11,0,-22); bw1.rotation.y=-0.9; g.add(bw1);
  const bw2=makeLiushu({seed:25514,h:6.8,bare:true}); bw2.position.set(-8.5,0,-14); bw2.rotation.y=2.6; g.add(bw2);
  const poet=cwFigure(1.5); poet.position.set(2.4,0,-14); poet.rotation.y=3.14; g.add(poet);
  const snow=makeLuoxue({n:170,box:[150,42,64],pos:[0,18,-34],speed:0.85,wind:0.9,maxA:0.34,size:3.0}); g.add(snow.points);
  const mist=makeMist({n:6,spread:[170,12,60],pos:[0,3.4,-40],scale:52,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[110,14,50],pos:[0,8,-10],color:0xaebccd,size:3.4,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x05080e,seed:25542,rim:0.10,rimC:0x98aec8});
  fg1.g.position.set(-12.5,-1.6,16); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:14,n:5,d:4,color:0x05080e,seed:25543,sway:0.6,rim:0.08,rimC:0x98aec8});
  fg2.g.position.set(12,-1.8,15); g.add(fg2.g);
  addLights(g,{c:0xa6b6cc,i:0.30,p:[-40,54,-40]},{c:0x1b2433,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    lw.update(t); bw1.update(t); bw2.update(t);
    poet.update(t,k);
    snow.update(t); mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXiwang(){ // 壹 · 昔往杨柳 —— 昔我往矣，杨柳依依：
                    // 一排带叶春柳随风轻摆（柳色微光+柳絮），归人背影出征——记忆里的春天
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0d1220,c2:0x1b2434,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,-8);
  const yuan=makeYuanling({r:250,h:11,seed:25544}); yuan.g.position.set(0,0,-165); g.add(yuan.g);
  const road=makeDaolu({seed:25501}); g.add(road);
  /* 昔日的柳：一排带叶春柳（境贰同位冬柳与之对照） */
  const w1=makeLiushu({seed:25515,h:7.0,bare:false}); w1.position.set(-11,0,-20); w1.rotation.y=0.6; g.add(w1);
  const w2=makeLiushu({seed:25516,h:6.2,bare:false}); w2.position.set(12.5,0,-30); w2.rotation.y=-1.1; g.add(w2);
  const w3=makeLiushu({seed:25517,h:7.8,bare:false}); w3.position.set(-14,0,-42); w3.rotation.y=0.2; g.add(w3);
  /* 柳色微光（记忆的柔焦）+ 柳絮 */
  const liuhui=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x7d9080,
    transparent:true,opacity:0.10,depthWrite:false,fog:false}));
  liuhui.scale.set(60,22,1); liuhui.position.set(-9,6.5,-26); liuhui.renderOrder=2; g.add(liuhui);
  const cat=makeGlow({n:22,box:[40,8,22],pos:[-6,4,-26],color:0xaab9a2,size:2.6,
    speed:0.05,rise:0.4,add:false,maxA:0.13});
  g.add(cat.points);
  const poet=cwFigure(1.6); poet.position.set(2.0,0,-16); poet.rotation.y=2.9; g.add(poet);   // 背影出征
  const mist=makeMist({n:5,spread:[160,10,56],pos:[0,3.2,-38],scale:50,color:0x2c3a44,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[100,13,46],pos:[0,8,-6],color:0xaebccd,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'树枝',w:16,n:6,d:4,color:0x05080e,seed:25545,sway:0.75,rim:0.09,rimC:0x8ba192});
  fg1.g.position.set(-11,-1.7,14.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:10,d:4,color:0x05080e,seed:25546,rim:0.09,rimC:0x98aec8});
  fg2.g.position.set(11.5,-1.5,14); g.add(fg2.g);
  addLights(g,{c:0xa4b2ac,i:0.30,p:[-38,52,-38]},{c:0x1a2431,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    w1.update(t); w2.update(t); w3.update(t);
    poet.update(t,k);
    liuhui.material.opacity=k*0.10*(0.82+0.18*Math.sin(t*0.24+1.1));
    cat.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bJinlai(){ // 贰 · 今来雨雪 —— 今我来思，雨雪霏霏：
                    // 同一排柳叶尽枝枯（与境壹同位对照），大雪霏霏、归人迎面而行——眼前的冬天
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x101623,c2:0x202c40,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,-8);
  const yuan=makeYuanling({r:250,h:10,seed:25547}); yuan.g.position.set(0,0,-165); g.add(yuan.g);
  const road=makeDaolu({seed:25501}); g.add(road);
  /* 同一排柳（同 seed 同位），今已叶尽枝枯、枝头一点雪帽 */
  const w1=makeLiushu({seed:25515,h:7.0,bare:true}); w1.position.set(-11,0,-20); w1.rotation.y=0.6; g.add(w1);
  const w2=makeLiushu({seed:25516,h:6.2,bare:true}); w2.position.set(12.5,0,-30); w2.rotation.y=-1.1; g.add(w2);
  const w3=makeLiushu({seed:25517,h:7.8,bare:true}); w3.position.set(-14,0,-42); w3.rotation.y=0.2; g.add(w3);
  const poet=cwFigure(1.75); poet.position.set(-1.6,0,-11); poet.rotation.y=0.25; g.add(poet); // 归人迎面
  const snow=makeLuoxue({n:330,box:[170,44,70],pos:[0,18,-36],speed:1.0,wind:1.2,maxA:0.50,size:3.2}); g.add(snow.points);
  const wind=makeFlow({n:200,box:[110,10,46],pos:[0,6.5,-24],color:0x5f6e84,size:14,speed:3.0,maxA:0.07});
  g.add(wind.points);
  const mist=makeMist({n:7,spread:[180,12,64],pos:[0,3.6,-42],scale:54,color:0x2a3648,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[96,12,44],pos:[0,8,-8],color:0xaebccd,size:3.2,speed:0.03,rise:0,add:false,maxA:0.06});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x05080e,seed:25548,rim:0.10,rimC:0x98aec8});
  fg1.g.position.set(-12,-1.7,14.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:13,n:4,d:4,color:0x05080e,seed:25549,sway:1.0,rim:0.08,rimC:0x98aec8});
  fg2.g.position.set(11.5,-1.9,13.5); g.add(fg2.g);
  addLights(g,{c:0xa4b4c8,i:0.28,p:[-42,54,-40]},{c:0x192230,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    w1.update(t); w2.update(t); w3.update(t);
    poet.update(t,k);
    snow.update(t); wind.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXingdao(){ // 叁 · 行道迟迟 —— 行道迟迟，载渴载饥：
                     // 镜头压低随长路无尽，远村依稀而未至，风雪渐紧——长路与饥渴
  const g=new THREE.Group();
  const grd=makeGround({r:160,c1:0x0f1522,c2:0x1d2939,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,-14);
  const yuan=makeYuanling({r:250,h:9,seed:25550}); yuan.g.position.set(0,0,-170); g.add(yuan.g);
  const road=makeDaolu({seed:25501,z1:-165,bend:7}); g.add(road);
  /* 路的尽头：远村一点（家尚远，霏雪中依稀） */
  const cun=makeYuanCun({seed:25531,n:5}); cun.position.set(1,0,-112); g.add(cun);
  /* 道旁冬柳渐稀 */
  const w1=makeLiushu({seed:25518,h:6.4,bare:true}); w1.position.set(9.5,0,-26); w1.rotation.y=-1.0; g.add(w1);
  const w2=makeLiushu({seed:25519,h:7.4,bare:true}); w2.position.set(-12,0,-48); w2.rotation.y=0.4; g.add(w2);
  const poet=cwFigure(1.8); poet.position.set(-1.2,0,-13); poet.rotation.y=0.1; g.add(poet);
  const snow=makeLuoxue({n:250,box:[160,42,66],pos:[0,17,-34],speed:0.95,wind:1.1,maxA:0.44,size:3.0}); g.add(snow.points);
  const wind=makeFlow({n:230,box:[120,9,50],pos:[0,5.2,-26],color:0x5a6a80,size:13,speed:3.4,maxA:0.08});
  g.add(wind.points);
  const mist=makeMist({n:7,spread:[190,11,66],pos:[0,3.0,-46],scale:56,color:0x2a3648,op:0.12});
  g.add(mist.g);
  const fg1=makeForeground({kind:'芦苇',w:20,n:9,d:4,color:0x05080e,seed:25551,sway:0.9,rim:0.08,rimC:0x98aec8});
  fg1.g.position.set(-10,-1.6,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x05080e,seed:25552,rim:0.09,rimC:0x98aec8});
  fg2.g.position.set(10.5,-1.6,12); g.add(fg2.g);
  addLights(g,{c:0xa2b2c4,i:0.26,p:[-40,50,-40]},{c:0x18212d,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    w1.update(t); w2.update(t);
    poet.update(t,k);
    snow.update(t); wind.update(t);
    mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bMozhi(){ // 肆（末境·可点击）· 莫知我哀 —— 我心伤悲，莫知我哀：
                   // 点击：今昔对切——春柳记忆淡现+柳絮飘起而雨雪未停，杨柳与雨雪两景交叠
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x101623,c2:0x202c40,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,-8);
  const yuan=makeYuanling({r:250,h:10,seed:25553}); yuan.g.position.set(0,0,-165); g.add(yuan.g);
  const road=makeDaolu({seed:25501}); g.add(road);
  const w1=makeLiushu({seed:25515,h:7.0,bare:true}); w1.position.set(-11,0,-20); w1.rotation.y=0.6; g.add(w1);
  const w2=makeLiushu({seed:25516,h:6.2,bare:true}); w2.position.set(12.5,0,-30); w2.rotation.y=-1.1; g.add(w2);
  const poet=cwFigure(1.7); poet.position.set(-1.4,0,-12); poet.rotation.y=0.2; g.add(poet);
  const snow=makeLuoxue({n:280,box:[170,44,70],pos:[0,18,-36],speed:1.0,wind:1.1,maxA:0.46,size:3.1}); g.add(snow.points);
  /* 标志性交互：昔往的记忆（点击前 visible=false 硬关）——
     同一排柳回到带叶的春天，柳絮飘起；雨雪未停，两景交叠 */
  const jx=makeJinxi({}); g.add(jx.g);
  const mist=makeMist({n:7,spread:[180,12,64],pos:[0,3.4,-42],scale:54,color:0x2a3648,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[100,13,46],pos:[0,8,-8],color:0xaebccd,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x05080e,seed:25554,rim:0.09,rimC:0x98aec8});
  fg1.g.position.set(-11.5,-1.6,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:13,n:5,d:4,color:0x05080e,seed:25555,sway:0.9,rim:0.08,rimC:0x98aec8});
  fg2.g.position.set(11,-1.8,13.5); g.add(fg2.g);
  addLights(g,{c:0xa4b2c6,i:0.28,p:[-42,52,-40]},{c:0x19222f,i:0.52});
  const baseSnow=snow.mat.uniforms.uMaxA.value;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/5.5);
      const e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      jx.update(t,k,e);                                   // 杨柳记忆淡现（雨雪未停——两景交叠）
      snow.mat.uniforms.uMaxA.value=baseSnow*(1-0.30*e);  // 雪势稍收，交叠而不相掩
      w1.update(t); w2.update(t);
      poet.update(t,k);
      snow.update(t);
      mist.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); yuan.update(t,0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.10);
        pluck(3,0.05,0.11); pluck(1,0.85,0.09); pluck(0,1.75,0.08);   // 下行三叠，如长叹
        const fl=$('#flash'); fl.textContent='昔我往矣 杨柳依依 今我来思 雨雪霏霏';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x151c2a),bot:C(0x04070c),fog:C(0x111823),fd:0.0050,star:0.18,
  moon:new THREE.Vector3(-44,62,-170),ms:1.05,mph:0.42,mhaze:0.20,dirC:C(0xa8bad0),dirI:0.32,
  dirP:new THREE.Vector3(-40,55,-40),ambC:C(0x1b2433),ambI:0.54},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.2,30],t:[0,4.8,2],lf:[2,7.8,-2],lt:[-4,8.8,-30]},
  sky:()=>SK({fd:0.0050,star:0.16,ms:0.9,mph:0.20,mhaze:0.30}) },
{ name:'昔往杨柳',dwell:18,river:0.02,build:bXiwang,
  cam:{f:[-1.5,5.6,13],t:[1.0,3.6,-8],lf:[2.5,6.2,-10],lt:[9,7.6,-34]},
  sky:()=>SK({fd:0.0052,star:0.10,ms:0.85,mph:0.15,mhaze:0.38,hor:C(0x171f2c),
    fog:C(0x121a25),dirC:C(0xa4b2a8),dirI:0.30,
    dirP:new THREE.Vector3(-38,52,-38),ambC:C(0x1a2431),ambI:0.56}) },
{ name:'今来雨雪',dwell:19,river:0.02,build:bJinlai,
  cam:{f:[0,6.4,18],t:[0,3.9,-11],lf:[-2,7.2,-12],lt:[-8,8.4,-34]},
  sky:()=>SK({fd:0.0058,star:0.05,ms:0.8,mph:0.15,mhaze:0.45,hor:C(0x141b28),
    fog:C(0x131a26),dirC:C(0xa4b4c8),dirI:0.26,
    dirP:new THREE.Vector3(-42,54,-40),ambC:C(0x192230),ambI:0.52}) },
{ name:'行道迟迟',dwell:19,river:0.02,build:bXingdao,
  cam:{f:[0,3.4,20],t:[0,2.6,-26],lf:[0,3.9,-4],lt:[-2,4.6,-40]},
  sky:()=>SK({fd:0.0062,star:0.04,ms:0.7,mph:0.15,mhaze:0.45,hor:C(0x141a26),
    fog:C(0x141b27),dirC:C(0xa2b2c4),dirI:0.24,
    dirP:new THREE.Vector3(-40,50,-40),ambC:C(0x18212d),ambI:0.50}) },
{ name:'莫知我哀',dwell:20,river:0.02,build:bMozhi,
  cam:{f:[0,6.2,16],t:[0,4.1,-10],lf:[2,7.4,-8],lt:[6,8.6,-30]},
  sky:()=>SK({fd:0.0060,star:0.07,ms:0.85,mph:0.15,mhaze:0.40,
    fog:C(0x131a26),dirC:C(0xa4b2c6),dirI:0.28,
    dirP:new THREE.Vector3(-42,52,-40),ambC:C(0x19222f),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('caiwei-jiexuan.py —— 被 build.py 消费：python build.py caiwei-jiexuan')
