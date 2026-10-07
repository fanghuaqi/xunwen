# -*- coding: utf-8 -*-
"""xingjun-jiuri.py —— 《行军九日思长安故园》（唐·岑参，queue no.220，大漠金戈）生成配置
两境（N=queue stages 数）：登高无酒（强欲登高去·无人送酒来——行军途中重阳、佳节落空）、
菊傍战场（遥怜故园菊·应傍战场开——标志性瞬间+末境点击「菊影在战场硝烟中浮现」）。
大漠金戈全套色板：底色 #120d08、雾 #140d07～#1a110a 系、文字 #f0e2cc，accent=#b0906a
（queue 分配强调色，赭金）只落在人物边缘光/菊心/旌旗杆首/菊影暖光/UI 上，禁艳金。
时间推进线：境壹=行军暮色（行军队伍蜿蜒、旌旗在风沙里、荒丘可登、雁阵南飞、道旁翻倒的空陶壶）
→ 境贰=故园悬想（断壁残垣、折戟残旗、硝烟横流，点击后故园菊影傍着战场次第浮现）。
标志性瞬间（境贰·全诗名句）：应傍战场开——想象里故园的菊花，开在战场旁边；
与已有边塞页（孤城/雪山/金甲/密林夜猎）第一眼可区分：本页是「行军途中的重阳 + 战场旁的菊花」。
末境点击（queue interact：点击故园菊——菊影在战场硝烟中浮现）：点击画面——透明菊影自硝烟中
次第渐显、暖光涨起又徐落、金色花瓣飘落，「遥怜故园菊 应傍战场开」题字同现。
考点钉子：强 qiǎng（强欲）/ 傍 bàng（第 3 题落点）；陶渊明重阳无酒、王弘白衣送酒典故 +
安史之乱长安沦陷背景（第 4 题）；「应傍战场开」悬想（对写/虚写）手法（第 5 题）。
多音字：应 yīng 从教材通行本（tts.json 钉「应傍战场开→英傍战场开」「强欲登高去→抢欲登高去」）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='xingjun-jiuri', title='行军九日思长安故园', dyn='唐 · 岑参', brand_author='岑 参',
    gold_rgb='176,144,106',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b0906a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(176,144,106,.3);
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
    tip='轻点画面 / 按空格 —— 菊影浮现，开在战场之旁',
    hint='← → 键或空格逐境游览 · 末境可点击画面：故园菊影在战场硝烟中浮现',
    cover_read='行军九日思长安故园。唐，岑参。强欲登高去，无人送酒来。遥怜故园菊，应傍战场开。',
    cover_p1='两重意境，随诗句次第展开：行军途中恰逢重阳，勉强想循旧俗登高、却连送酒的人都没有的落寞；遥想沦陷的长安故园，菊花大概正孤单地开在战场旁边——佳节如旧，人事全非。',
    cover_p2='边读诗，边走进岑参笔下的战地重阳：他不写眼前的烽烟，反而掉转笔去写千里之外想象中的菊花——读懂这个「应」字里的悬想，就读懂了乱离诗里最深的那种牵挂。',
    end_h2='故园菊 · 傍战场', cn_word='贰',
    words_js="['再登一次重阳高','初识岑参，尚需共读','渐入诗境，再诵几遍','乡思渐起，怜意渐深','已解菊傍战场意','悬想故园，一咏三叹']",
    sky_atmo='0x332218',
)

POEM_JS = """const POEM = [
{ name:'登高无酒', jing:'行军途中恰逢重阳，勉强想循旧俗去登高，却连送酒的人都没有 —— 战地行军、佳节落空。（行军 · 重阳 · 无酒）',
  segs:[
   {c:'强欲登高去，', p:py('qiǎng yù dēng gāo qù')},
   {c:'无人送酒来。', p:py('wú rén sòng jiǔ lái')}],
  read:'强欲登高去，无人送酒来。',
  yisi:'九月初九重阳节，人在行军途中，勉强想循旧俗去登高，却没有人送酒来。——「强」字见心绪：乱离之中佳节兴致全无，却仍勉强自己循一循旧俗；「无人送酒来」反用陶渊明白衣送酒的典故：陶潜重阳无酒，尚有王弘遣白衣送来；今日行军路上，连送酒的人也没有。重阳三事——登高、饮酒、赏菊——开头两件就都落了空。',
  zhu:[['行军九日','九月初九重阳节，恰在行军途中。此诗作于安史之乱中（约至德二载，757）：长安沦陷于叛军之手，岑参随军征戍，行军路上正逢重阳——佳节与战火撞在了同一日'],['强欲','强，读 qiǎng，勉强。「强欲登高」：不是兴之所至，是战地行军中勉强自己维持一点过节的心意——一个「强」字，把乱离中人提不起又放不下的心绪写尽'],['登高','重阳习俗：登高、饮酒、佩茱萸、赏菊。王维「遥知兄弟登高处，遍插茱萸少一人」即写此俗。如今行军在身、故园陷落，登高无人偕往，佳节习俗一一落空'],['无人送酒来','化用陶渊明典故：《宋书·陶潜传》载，陶渊明九月九日无酒，坐于宅边菊丛，恰逢江州刺史王弘遣白衣送酒，遂醉而归。岑参反用其意：陶潜无酒尚有白衣送酒，今日行军途中，连送酒的人都没有——比陶渊明更孤绝']] },
{ name:'菊傍战场', jing:'遥想长安故园的菊花，此刻大概正孤单地开在战场旁边 —— 悬想中的花开，一句千钧。（故园 · 菊 · 战场 · 标志性瞬间 · 末境点击画面：菊影在战场硝烟中浮现）',
  segs:[
   {c:'遥怜故园菊，', p:py('yáo lián gù yuán jú')},
   {c:'应傍战场开。', p:py('yīng bàng zhàn chǎng kāi')}],
  read:'遥怜故园菊，应傍战场开。',
  yisi:'遥想故园的菊花，此刻大概正依傍着战场开放吧。——「遥」是空间之远，「怜」是心意之切；「应」字最沉：长安沦陷、音书断绝，故园什么样，只能悬想。而悬想偏偏不肯美化——想象中的菊花，就开在战场旁边：花照旧开，城已不是那座城。没有一句直写忧愤，而忧愤与深情尽在其中，此句遂成千古名句。',
  zhu:[['遥怜','遥，远——人在行军途中，长安远在千里之外；怜，怜爱、怜惜——怜的是菊，更是沦陷的故园与乱世中人。一句从眼前荡开去，全诗的深情都压在这个「怜」字上'],['故园菊','长安家中的菊花。故园已陷战火、家人离散，庭前菊花无人照看——重阳赏菊的旧俗，如今只剩想象'],['应','读 yīng（教材通行本），大概、想必——推想之词。长安音书断绝，诗人无从望见，只能说「应」：一个悬想的字，托住全部的牵挂'],['傍战场开','傍，读 bàng，靠近、依傍。故园就在长安城中，而长安已成战场——想象里，菊花只能开在战场旁边了。花开如旧、人事全非，无主的佳节、无主的花，一句写尽家国之痛'],['悬想手法','不写眼前行军之景，而是掉转笔头去写千里之外想象中的景象（又称「对写」「虚写」）。故乡之思不直说，借一丛想象中的菊花说出——愈是花开得平淡，愈见心中波澜']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「强欲登高去」的下一句是？', o:['无人送酒来','遥怜故园菊','应傍战场开'], a:0},
 {q:'「遥怜故园菊」的下一句是？', o:['无人送酒来','应傍战场开','强欲登高去'], a:1},
 {q:'「强欲登高去」的「强」与「应傍战场开」的「傍」，读音和意思都正确的一项是？', o:['强读 qiàng，强大；傍读 páng，旁边——力量强大，战场在菊花旁边','强读 qiǎng，勉强；傍读 bàng，靠近、依傍——勉强想循俗登高，菊花依傍着战场开放','强读 qiáng，强壮；傍读 bàng，靠近——身体强壮也要登高，菊花靠近战场'], a:1},
 {q:'「无人送酒来」暗用了一个与重阳、菊花相关的著名典故。下列说法正确的是？', o:['化用陶渊明的典故：《宋书》载陶渊明重阳无酒，坐于宅边菊丛，恰逢王弘遣白衣送酒——岑参反用其意：陶潜尚有酒可送，行军途中连送酒之人都没有，更见孤绝','化用王维《九月九日忆山东兄弟》的典故：写的是「遍插茱萸少一人」的登高怀人之俗，与送酒无关','化用杜甫《登高》的典故：「无边落木萧萧下」写的也是重阳，指登高时以酒代诗'], a:0},
 {q:'「应傍战场开」是全诗名句。诗人身在行军途中，却不直写眼前之景，而去想故园的菊花此刻开在战场旁边——这种写法妙在何处？', o:['眼前实在无景可写，只好拿菊花凑数','悬想（虚写）：长安沦陷、无从望见，一个「应」字把牵挂推到千里之外——想象中菊花依旧开，而花开之地已是战场，节令如旧、人事全非，故园之思与家国之痛尽在其中','用夸张手法形容菊花很多，开满了整个战场'], a:1},
];
"""

SCENES_JS = """/* ================= 行军九日思长安故园 · 两境场景（大漠金戈·战地重阳：登高无酒、菊傍战场） =================
   美术立意：大漠金戈色板写「战地重阳」——底色 #120d08、雾 #140d07～#1a110a 系，
   accent=#b0906a（赭金）只落在人物边缘光/菊心/旌旗杆首/菊影暖光上，禁艳金。
   与已有边塞页第一眼可区分：不做孤城/雪山/金甲/密林夜猎，做「行军途中的重阳 + 战场旁的菊花」。
   境壹（暮）：行军队伍蜿蜒远去、旌旗在风沙里，荒丘可登，雁阵南飞，道旁翻倒的空陶壶——无人送酒。
   境贰（暮·标志性瞬间+末境可点击）：断壁残垣、折戟残旗、硝烟横流；
   点击：故园菊影自战场硝烟中次第浮现（透明菊影渐显+暖光涨落+花瓣飘落）。 */

/* —— 旌旗 makeJingQi(o)：旗杆+旗面（CPU 顶点波动，挂点在杆顶）；
   torn:true 为残旗（旗面更小、下垂、摆幅弱）——「行军旌旗 / 残旗」 */
function makeJingQi(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22091:o.seed);
  const h=o.h===undefined?4.6:o.h;
  const w=o.w===undefined?(o.torn?1.35:1.9):o.w;
  const hh=o.hh===undefined?(o.torn?0.85:1.15):o.hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.035,0.052,h,5);
  pole.translate(0,h*0.5,0); B.put(pole,0x2a2016);
  const knob=new THREE.SphereGeometry(0.07,6,5);
  knob.translate(0,h,0); B.put(knob,0x8a6a44);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a2c1c,emissive:0x060402}),{c:0xb0906a,i:o.rim===undefined?0.20:o.rim,p:2.4})));
  const fl=new THREE.PlaneGeometry(w,hh,8,2);
  fl.translate(w/2+0.045,h-(o.torn?0.30:0.14),0);
  const fp=fl.attributes.position.array.slice(0);
  const flag=new THREE.Mesh(fl,new THREE.MeshPhongMaterial({color:o.flagC===undefined?(o.torn?0x3a2818:0x64431f):o.flagC,
    side:THREE.DoubleSide,shininess:3,specular:0x2a2015,emissive:0x070403}));
  g.add(flag);
  const amp=(o.torn?0.09:0.22), sp=(o.torn?1.5:2.3), droop=(o.torn?0.42:0), ph=R()*6.283;
  g.update=function(t){
    const pos=fl.attributes.position.array;
    for(let i=0;i<pos.length;i+=3){
      const kk=Math.max(0,fp[i]-0.045)/w;
      pos[i+2]=Math.sin(t*sp+fp[i]*2.1+ph)*amp*kk;
      pos[i+1]=fp[i+1]-Math.sin(t*sp*0.7+fp[i]*1.3+ph)*amp*0.2*kk-droop*kk*kk;
    }
    fl.attributes.position.needsUpdate=true;
    fl.computeVertexNormals();
  };
  g.userData.update=g.update;
  return g;
}

/* —— 秋菊 makeJuhua(o)：茎+叶+两层披针花瓣+花心（GeoBag 合批 1 mesh/株）——「故园菊」
   ghost:true 为菊影（MeshBasicMaterial 半透明，初值=最大、visible 关闭，供点击渐显） */
function makeJuhua(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22051:o.seed);
  const s=o.s===undefined?1:o.s;
  const petalC=o.petalC===undefined?0xc9a24a:o.petalC, tipC=o.tipC===undefined?0xe2c27c:o.tipC;
  const B=new GeoBag();
  const hH=0.85*(0.8+0.4*R());
  B.put(limbGeo([0,0,0],[0.08*(R()-0.5),hH,0.05*(R()-0.5)],0.035,0.02,5),0x3a4426);
  for(let i=0;i<2;i++){
    const lf=new THREE.SphereGeometry(0.13,5,4);
    lf.scale(1.4,0.18,0.6); lf.rotateZ(0.5+R()*0.4); lf.rotateY(R()*6.283);
    lf.translate((R()-0.5)*0.2,hH*0.45+i*0.18,(R()-0.5)*0.2);
    B.put(lf,shadeColor(0x44502c,0.85+0.3*R()));
  }
  const nr=o.nr===undefined?14:o.nr, ni=o.ni===undefined?9:o.ni, pl=0.44*(0.85+0.3*R());
  for(let i=0;i<nr;i++){
    const a=i/nr*6.283+R()*0.2;
    const pt=new THREE.PlaneGeometry(pl,0.17);
    pt.translate(pl*0.5+0.06,0,0);
    pt.rotateX(2.05+R()*0.35);
    pt.rotateY(a);
    B.put(pt,i%2?petalC:tipC);
  }
  for(let i=0;i<ni;i++){
    const a=i/ni*6.283+0.4;
    const pt=new THREE.PlaneGeometry(pl*0.75,0.14);
    pt.translate(pl*0.36+0.05,0,0);
    pt.rotateX(1.55+R()*0.2);
    pt.rotateY(a);
    B.put(pt,tipC);
  }
  for(let i=0;i<ni;i++){
    const a=i/ni*6.283+0.9;
    const pt=new THREE.PlaneGeometry(pl*0.5,0.11);
    pt.translate(pl*0.24+0.04,0,0);
    pt.rotateX(1.1+R()*0.2);
    pt.rotateY(a);
    B.put(pt,tipC);
  }
  const core=new THREE.SphereGeometry(0.095,6,5); core.translate(0,0.02,0);
  B.put(core,o.heartC===undefined?0xb07a30:o.heartC);
  const g=new THREE.Group();
  let mat;
  if(o.ghost){
    mat=new THREE.MeshBasicMaterial({color:o.ghostC===undefined?0xe8cc90:o.ghostC,vertexColors:true,
      transparent:true,opacity:o.op===undefined?0.85:o.op,depthWrite:false,side:THREE.DoubleSide});
  }else{
    mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
      specular:0x6a5428,emissive:0x0a0703}),{c:0xb0906a,i:o.rim===undefined?0.30:o.rim,p:2.6});
  }
  const m=B.mesh(mat);
  if(o.ghost)m.visible=false;
  g.add(m);
  g.scale.setScalar(s);
  g.userData.mesh=m;
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.02*Math.sin(t*0.8+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 断壁残垣 makeCanyuan(o)：锯齿断墙+碎砖+碎石堆+半埋折戟（合批 1 mesh）——「战场」 */
function makeCanyuan(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22081:o.seed);
  const w=o.w===undefined?9:o.w, nb=o.rubble===undefined?5:o.rubble;
  const B=new GeoBag();
  for(let i=0;i<3;i++){
    const sw=w/3*(0.75+R()*0.4), sx=-w/2+sw/2+(i+0.5)*w/3+(R()-0.5)*0.4;
    const h0=1.1+R()*2.1;
    const body=new THREE.BoxGeometry(sw,h0,0.75);
    body.translate(sx,h0/2,0); B.put(body,shadeColor(0x352616,0.9+0.2*R()));
    const jn=1+Math.floor(R()*2);
    for(let j2=0;j2<jn;j2++){
      const bw=sw*(0.3+R()*0.3), bh=0.25+R()*0.55;
      const bk=new THREE.BoxGeometry(bw,bh,0.78);
      bk.translate(sx+(R()-0.5)*sw*0.6,h0+bh/2,(R()-0.5)*0.1);
      B.put(bk,shadeColor(0x2e2012,0.9+0.2*R()));
    }
  }
  for(let i=0;i<nb;i++){
    const r=0.22+R()*0.5;
    const rk=rockGeo(r,1,R);
    rk.scale(1.2,0.62,1);
    rk.translate((R()-0.5)*w*1.15,r*0.3,(R()-0.5)*3.2-0.6);
    B.put(rk,shadeColor(0x1f150c,0.85+0.35*R()));
  }
  const zj=new THREE.CylinderGeometry(0.05,0.07,2.4,5);
  zj.translate(0,1.1,0); zj.rotateZ(0.9+R()*0.3);
  zj.translate(w*0.28,0,1.1);
  B.put(zj,0x231a10);
  const tip=new THREE.ConeGeometry(0.075,0.5,5);
  tip.translate(0,0.25,0); tip.rotateZ(-0.5-R()*0.3);
  tip.translate(-w*0.1,0.28,-0.8);
  B.put(tip,0x554a3c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x453626,emissive:0x050302}),{c:0xb0906a,i:o.rim===undefined?0.20:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 雁阵 makeYanzhen(o)：人字雁列（合批 1 mesh，整体缓移+微起伏）——九秋时令 */
function makeYanzhen(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22101:o.seed);
  const n=o.n===undefined?7:o.n, v=o.v===undefined?1.1:o.v, span=o.span===undefined?26:o.span;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const side=i%2?1:-1, k=Math.ceil(i/2);
    const bd=new THREE.ConeGeometry(0.10,0.5,4);
    bd.rotateX(Math.PI/2);
    bd.scale(1.5,1,0.45);
    bd.translate(side*k*0.95,(R()-0.5)*0.16,-Math.abs(k)*0.55);
    B.put(bd,shadeColor(0x16100a,0.9+0.25*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshBasicMaterial({color:0xffffff,vertexColors:true})));
  const x0=o.x0===undefined?0:o.x0;
  g.rotation.y=Math.PI/2;
  g.update=function(t){
    g.position.x=x0+((t*v)%span)-span*0.5;
    g.position.y=Math.sin(t*0.21)*1.2;
  };
  g.userData.update=g.update;
  return g;
}

/* 戍卒/诗人：全诗贯穿的同一戎装造型（每次 build 新建材质） */
function xjFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x3a2c1c,belt:0x8a6a44,skin:0xd9b189,collar:0x7a5c38,
    hair:0x1a140c,hat:'幞头',beard:true,rimC:0xb0906a,rim:0.5,noProp:true,scale:scale===undefined?1.8:scale});
}

function bCover(){ // 卷首 · 战地重阳远望：行军队伍、旌旗、雁阵、风沙
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e0a06,c2:0x1c130b,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:22031,color:0x0d0906,atmo:0x332218,
    fogK:0.62,glowK:0.06,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-20,0,-96); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 远去的行军队伍：一列人影 + 三面旌旗 */
  const army=makeCrowd({n:10,rect:[-24,-30,42,6],seed:22032,color:0x1a1209,rimC:0xb0906a,rim:0.16,sMin:0.5,sMax:0.62,y:-1.6});
  g.add(army.mesh);
  const j1=makeJingQi({seed:22033,h:4.6}); j1.position.set(-14,-1.6,-27); g.add(j1);
  const j2=makeJingQi({seed:22034,h:5.0}); j2.position.set(-2,-1.6,-31); g.add(j2);
  const j3=makeJingQi({seed:22035,h:4.4}); j3.position.set(11,-1.6,-26); g.add(j3);
  /* 雁阵南飞（九月秋深） */
  const yan=makeYanzhen({seed:22036,n:7}); yan.position.set(18,17,-64); g.add(yan);
  const wind=makeFlow({n:380,box:[110,10,44],pos:[0,2.6,-18],color:0x6a5442,size:16,speed:5.2,maxA:0.14});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[220,14,80],pos:[0,5,-56],scale:70,color:0x4a3826,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:30,box:[170,18,70],pos:[0,9,-36],color:0x8a7048,size:4.4,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.8,w:13,d:6,color:0x0c0805,seed:22037,rim:0.09,rimC:0xb0906a});
  fg1.g.position.set(-12,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',n:4,w:12,d:4,color:0x100b06,seed:22038,sway:0.8,rim:0.08,rimC:0xb0906a});
  fg2.g.position.set(11,5.8,13); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.30,p:[-40,55,-25]},{c:0x2a1e12,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); grd.update(); army.update(t); j1.update(t); j2.update(t); j3.update(t);
    yan.update(t); wind.update(t); motes.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bDenggao(){ // 壹 · 登高无酒 —— 强欲登高去，无人送酒来：行军途中重阳，荒丘在望，空酒壶翻倒道旁
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d0906,c2:0x1b120a,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:17,layers:2,peaks:4,seed:22041,color:0x0c0805,atmo:0x332218,
    fogK:0.64,glowK:0.05,glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-30,0,-100); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 行军队伍：蜿蜒远去，旌旗在风沙里 */
  const army=makeCrowd({n:9,rect:[-30,-26,46,5],seed:22042,color:0x1a1209,rimC:0xb0906a,rim:0.15,sMin:0.5,sMax:0.6,y:-1.6});
  g.add(army.mesh);
  const j1=makeJingQi({seed:22043,h:4.8}); j1.position.set(-13,-1.6,-18); g.add(j1);
  const j2=makeJingQi({seed:22044,h:5.2}); j2.position.set(2,-1.6,-24); g.add(j2);
  const j3=makeJingQi({seed:22045,h:4.5}); j3.position.set(16,-1.6,-19); g.add(j3);
  /* 可登的荒丘：灰暗起伏，无路无阶 */
  const B=new GeoBag();
  for(let i=0;i<5;i++){
    const r=1.5+i*0.75;
    const rk=rockGeo(r*0.5,1,seedRnd(22046+i));
    rk.scale(1.4,0.5,1.0);
    rk.translate(-6+(i-2)*2.4,-1.7+r*0.12,-15-(i%2)*2.4);
    B.put(rk,shadeColor(0x191007,0.85+0.25*((i*7)%3)/2));
  }
  g.add((function(){ const mg=new THREE.Group();
    mg.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
      specular:0x3a2c1c,emissive:0x050302}),{c:0xb0906a,i:0.12,p:2.6})));
    return mg; })());
  /* 道旁翻倒的空陶壶：倾覆在地——无人送酒来 */
  const pot=makeVessel({type:'壶',mat:'陶',scale:0.62,liquid:false,shadow:false});
  pot.g.position.set(1.4,-1.42,-8.6); pot.g.rotation.z=1.35; pot.g.rotation.y=0.7; g.add(pot.g);
  /* 诗人：戎装按剑，立于道旁坡石上，仰望荒丘（暖光点缀中景） */
  const rock=makeForeground({kind:'坡石',n:2,r:2.4,w:9,d:5,color:0x0c0805,seed:22047,rim:0.12,rimC:0xb0906a});
  rock.g.position.set(4.6,-1.35,-6.8); g.add(rock.g);
  const poet=xjFigure(1.9,'按剑'); poet.position.set(5.4,-0.30,-6.4); poet.rotation.y=-1.15; g.add(poet);
  const sl=new THREE.PointLight(0xc9a878,0.65,20); sl.position.set(3.2,2.4,-6); g.add(sl);
  /* 道旁野菊一丛：伏笔（贰境主角） */
  const ju1=makeJuhua({seed:22048,s:1.4,petalC:0xa8843c,tipC:0xc0a058}); ju1.position.set(-2.2,-1.72,-7.8); g.add(ju1);
  const ju2=makeJuhua({seed:22049,s:1.0,petalC:0xa8843c,tipC:0xc0a058}); ju2.position.set(-3.0,-1.72,-7.2); g.add(ju2);
  /* 雁阵、风沙、暮霭 */
  const yan=makeYanzhen({seed:22050,n:7}); yan.position.set(-16,16,-60); g.add(yan);
  const wind=makeFlow({n:400,box:[100,9,40],pos:[0,2.4,-16],color:0x6a5442,size:16,speed:5.4,maxA:0.15});
  g.add(wind.points);
  const leaves=makeGlow({n:24,box:[70,10,28],pos:[0,4,-14],color:0x4a3a1e,size:2.4,speed:0.5,rise:-0.5,add:false,maxA:0.10});
  g.add(leaves.points);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-54],scale:68,color:0x4a3826,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'树枝',n:4,w:13,d:4,color:0x0f0a05,seed:22051,sway:0.9,rim:0.08,rimC:0xb0906a});
  fg1.g.position.set(-11,6,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0c0805,seed:22052,rim:0.10,rimC:0xb0906a});
  fg2.g.position.set(12.5,-1.8,14); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.32,p:[-38,50,-22]},{c:0x2a1e12,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); grd.update(); army.update(t); j1.update(t); j2.update(t); j3.update(t);
    yan.update(t); wind.update(t); leaves.update(t); mist.update(t,k);
    poet.update(t,k); rock.update(t,k); ju1.update(t); ju2.update(t);
    pot.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bJukai(){ // 贰（末境·可点击）· 菊傍战场 —— 遥怜故园菊，应傍战场开：断壁残垣+硝烟，点击菊影浮现
  const ctl={t:0,clicked:false,on:false,reveal:0,done:0};
  const g=new THREE.Group();
  const ridge=makeRange({r:310,h:14,layers:2,peaks:4,seed:22061,color:0x0d0906,atmo:0x332218,
    fogK:0.60,glowK:0.10,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-6,0,-116); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const grd=makeGround({r:230,c1:0x140e07,c2:0x231508,y:-1.7}); g.add(grd.mesh);
  /* 标志性瞬间：断壁残垣间，故园菊影傍着战场开 */
  const yuan=makeCanyuan({seed:22062,w:9});
  yuan.position.set(-1.8,-1.7,-11); yuan.rotation.y=0.18; g.add(yuan);
  const yuan2=makeCanyuan({seed:22063,w:5,rubble:3});
  yuan2.position.set(7.5,-1.7,-14); yuan2.rotation.y=-0.3; g.add(yuan2);
  /* 残旗：半垂在断杆上 */
  const cq=makeJingQi({seed:22064,h:3.6,torn:true});
  cq.position.set(-6.2,-1.7,-12.5); cq.rotation.z=0.22; g.add(cq);
  /* 一丛现实的野菊（暗淡，躲在墙根缺口）——眼前仅存的一点生色 */
  const ju0=makeJuhua({seed:22065,s:1.5,petalC:0xa8843c,tipC:0xc0a058});
  ju0.position.set(0.2,-1.60,-8.0); g.add(ju0);
  /* 点击：故园菊影自硝烟中浮现（透明菊影，初值=最大、visible 关闭） */
  const ghostA=makeJuhua({seed:22066,s:1.9,ghost:true}); ghostA.position.set(-3.1,-1.62,-9.4); g.add(ghostA);
  const ghostB=makeJuhua({seed:22067,s:1.6,ghost:true}); ghostB.position.set(-4.2,-1.62,-8.3); g.add(ghostB);
  const ghostC=makeJuhua({seed:22068,s:1.5,ghost:true}); ghostC.position.set(-2.2,-1.62,-8.6); g.add(ghostC);
  const ghostD=makeJuhua({seed:22069,s:2.1,ghost:true}); ghostD.position.set(-5.3,-1.62,-10.2); g.add(ghostD);
  const gmA=ghostA.userData.mesh.material, gmB=ghostB.userData.mesh.material,
        gmC=ghostC.userData.mesh.material, gmD=ghostD.userData.mesh.material;
  /* 暖光托起菊影（常驻微光=现实里的一点天光；点击后涨起又徐落） */
  const wl=new THREE.PointLight(0xd8b078,0.5,26); wl.position.set(-2.0,2.0,-9.0); g.add(wl);
  /* 花瓣飘落（点击后渐起） */
  const petals=makeGlow({n:70,box:[26,7,14],pos:[-2.6,4.2,-9.4],color:0xd8b878,size:2.6,speed:0.32,rise:-0.85,add:false,maxA:0.001});
  g.add(petals.points);
  /* 硝烟横流 */
  const smoke=makeFlow({n:420,box:[90,12,36],pos:[0,3.2,-13],color:0x584838,size:20,speed:3.6,maxA:0.20});
  g.add(smoke.points);
  const mist=makeMist({n:7,spread:[220,14,80],pos:[0,4.5,-52],scale:70,color:0x504030,op:0.12});
  g.add(mist.g);
  /* 诗人：戎装独立，3/4 侧面朝镜头左前方，望向墙根菊影 */
  const poet=xjFigure(1.75,'独立'); poet.position.set(6.8,-0.95,-5.2); poet.rotation.y=-0.55; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:1.6,w:7,d:4,color:0x0d0906,seed:22070,rim:0.12,rimC:0xb0906a});
  rock.g.position.set(7.5,-1.55,-4.4); g.add(rock.g);
  const motes=makeGlow({n:30,box:[160,16,66],pos:[0,7,-30],color:0x8a7048,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0d0906,seed:22071,rim:0.10,rimC:0xb0906a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x0d0906,seed:22072,rim:0.10,rimC:0xb0906a});
  fg2.g.position.set(12.5,-1.6,12); g.add(fg2.g);
  addLights(g,{c:0xc09868,i:0.42,p:[44,44,-16]},{c:0x342514,i:0.56});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on){
        ctl.reveal=Math.min(1,ctl.reveal+dt/1.5);
        if(ctl.reveal>=1)ctl.done+=dt;
      }
      const e0=ctl.reveal, e=e0*e0*(3-2*e0);
      const eb=Math.max(0,Math.min(1,(e0-0.2)/0.8)), ebS=eb*eb*(3-2*eb);
      /* 菊影次第浮现：前两丛随 reveal 渐显，后两丛稍迟；暖光涨起又徐落 */
      gmA.opacity=k*0.85*e; gmC.opacity=k*0.78*e;
      gmB.opacity=k*0.80*ebS; gmD.opacity=k*0.85*ebS;
      ghostA.userData.mesh.visible=e>0.01; ghostC.userData.mesh.visible=e>0.01;
      ghostB.userData.mesh.visible=ebS>0.01; ghostD.userData.mesh.visible=ebS>0.01;
      const boost=1.15*e*Math.exp(-ctl.done*1.1);
      wl.intensity=k*(0.5+boost)*(0.9+0.1*Math.sin(t*1.7));
      petals.mat.uniforms.uMaxA.value=0.001+0.38*e;
      ridge.update(t,0); grd.update();
      smoke.update(t); mist.update(t,k); motes.update(t); petals.update(t);
      poet.update(t,k); rock.update(t,k); cq.update(t); ju0.update(t);
      ghostA.update(t); ghostB.update(t); ghostC.update(t); ghostD.update(t);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.20);
        pluck(5,0.0,0.12); pluck(2,0.45,0.09); pluck(0,0.95,0.08);
        const fl=$('#flash'); fl.textContent='遥怜故园菊 应傍战场开';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0c0806),hor:C(0x2a1c10),bot:C(0x090604),fog:C(0x140d07),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-62,26,-190),ms:0.42,mph:0.44,mhaze:0.20,dirC:C(0xa8824e),dirI:0.32,
  dirP:new THREE.Vector3(-42,52,-24),ambC:C(0x2a1e12),ambI:0.54},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,46],t:[0,9.5,38],lf:[1.5,8.5,-26],lt:[2.5,9,-36]},
  sky:()=>SK({fd:0.0046,star:0.14}) },
{ name:'登高无酒',dwell:16,river:0.02,build:bDenggao,
  cam:{f:[0,6.8,26],t:[1.8,7.2,18],lf:[-1.5,6.8,-14],lt:[-3.5,7.6,-26]},
  sky:()=>SK({fd:0.0054,star:0.18,ms:0.42,mph:0.46,mhaze:0.22,
    moon:new THREE.Vector3(-52,25,-180),dirC:C(0xa8824e),dirI:0.30,
    ambC:C(0x281c10),ambI:0.52}) },
{ name:'菊傍战场',dwell:19,river:0.02,build:bJukai,
  cam:{f:[0.6,4.6,14.5],t:[-1.8,4.2,7.2],lf:[-1,4.4,-6],lt:[-2.4,4.8,-14]},
  sky:()=>SK({top:C(0x160e08),hor:C(0x4a2c16),bot:C(0x0d0805),fog:C(0x1a110a),fd:0.0060,star:0.06,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.04,
    dirC:C(0xc09868),dirI:0.42,dirP:new THREE.Vector3(44,44,-16),
    ambC:C(0x342514),ambI:0.56}) },
];
"""
