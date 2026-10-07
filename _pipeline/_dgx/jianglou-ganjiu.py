# -*- coding: utf-8 -*-
"""jianglou-ganjiu.py —— 《江楼感旧》（唐·赵嘏，queue no.228，水墨夜思）生成配置
两境（N=queue stages 数）：独上江楼（独上江楼思渺然·月光如水水如天——标志性瞬间）、
望月感旧（同来望月人何处·风景依稀似去年——末境点击）。
水墨夜思全套色板：底色 #0d1117、雾 #10161f～#131a26 系、文字 #dfe6f0，accent=#a0b4cc
（queue 分配强调色，月银水青）只落在满月晕/水中月影/银辉光路/水天光带/人物边缘光/UI 上，
全页近零饱和。本诗是满月夜时相：月是全页唯一主角（mph 0 满月，ms 1.6→1.9 渐盈），星稀。
标志性瞬间（境壹·全诗名句）：月光如水水如天——满月高悬、水中月影与之上下相望，
一条银辉光路自天际月下直铺楼前，地平一线水光接天、天水无界；银尘微光浸染全页，
澄澈通透（与 ti-jinlingdu 斜月星火的「暗夜远望」反向：这里是月光盛满的「亮夜」）。
末境点击（queue interact：点击去年风景——去年同游虚影淡现又散）：点击画面——
去年同来望月的人影在楼头月色中淡现（半透明银影、并肩而立），凝望片刻又缓缓散去
（上浮、消散如雾）；「同来望月人何处 风景依稀似去年」题字同现——景仍是去年景，
人已非去年人，物是人非一笔点破。
考点钉子：渺 miǎo（悠远迷茫，小测第 3 题落点）；赵嘏「赵渭南」+ 又题《江楼旧感》的
感旧怀人体（第 4 题）；「月光如水水如天」顶针手法与物是人非主旨（第 5 题）。
多音字：嘏 gǔ 钉同音替换「赵嘏→赵古」（tts.json）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='jianglou-ganjiu', title='江楼感旧', dyn='唐 · 赵嘏', brand_author='赵 嘏',
    gold_rgb='160,180,204',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#a0b4cc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(160,180,204,.26);
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
    tip='轻点画面 / 按空格 —— 去年同游，虚影淡现又散',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看去年同游虚影在月色中淡现又散',
    cover_read='江楼感旧。唐，赵嘏。独上江楼思渺然，月光如水水如天。同来望月人何处，风景依稀似去年。',
    cover_p1='两重意境，随诗句次第展开：夜深无寐，独自登上江边高楼，思绪悠远渺茫——满月当空，月光如水倾泻江面，水色与天光连成一片；曾经同来望月的人不知去了哪里，眼前风景却依稀还是去年模样。',
    cover_p2='边读诗，边跟着赵嘏月夜独上江楼：月还是那轮月，江天还是那样澄澈——读懂「独上」与「依稀似去年」里那一问一叹，就读懂了这首怀人感旧的绝唱。',
    end_h2='月满 · 人远', cn_word='两',
    words_js="['再上一次江楼','初识赵嘏，尚需共读','渐入诗境，再诵几遍','月色如水，水天渐明','已解望月感旧之意','风景依稀，人在何处']",
    sky_atmo='0x1c2634',
)

POEM_JS = """const POEM = [
{ name:'独上江楼', jing:'夜深无寐，独自登上江边高楼，思绪悠远渺茫；满月当空，月光如水倾泻江面，水色与天光连成一片 —— 独上、思渺、月满江楼。（江楼 · 满月 · 水天一色）（标志性瞬间）',
  segs:[
   {c:'独上江楼思渺然，', p:py('dú shàng jiāng lóu sī miǎo rán')},
   {c:'月光如水水如天。', p:py('yuè guāng rú shuǐ shuǐ rú tiān')}],
  read:'独上江楼思渺然，月光如水水如天。',
  yisi:'夜晚独自登上江边的高楼，思绪悠远渺茫；月光如水一般倾泻在江面上，江水又与天光浑然一体，水天难分。——「独上」二字是全诗的根：楼是旧时楼，月是旧时月，同来的人却不在——不说「人不在」，只说「独上」，怅惘已在不言之中。次句「月光如水水如天」以顶针相连：「水」字上递下接，月华泻地如水、水色接天如天，七个字造出一个澄澈空明、上下无界的世界——景愈静澈，思愈渺远。',
  zhu:[['江楼感旧','诗题一作《江楼旧感》——月夜登楼、追念旧游之作'],['江楼','江边的高楼——诗人月夜独登之处'],['思渺然','思绪悠远渺茫。渺然，悠远、迷茫的样子。渺，读 miǎo'],['月光如水','月光倾泻江面，清亮流动如水——月色与水色难以分辨'],['水如天','江水澄澈，水色与天光连成一片，上下无界'],['顶针','用前句结尾的字做后句开头（「水」字上递下接），句意蝉联而下——「月光如水水如天」一气贯通，正是写水天一色的名句']] },
{ name:'望月感旧', jing:'曾经同来望月的人，如今都在何处？眼前的风景，却依稀还是去年光景 —— 风景不殊，人事已非。（同来 · 望月人 · 依稀）（末境点击画面：去年同游虚影淡现又散）',
  segs:[
   {c:'同来望月人何处，', p:py('tóng lái wàng yuè rén hé chù')},
   {c:'风景依稀似去年。', p:py('fēng jǐng yī xī sì qù nián')}],
  read:'同来望月人何处，风景依稀似去年。',
  yisi:'曾经与我一同来这江楼望月的人，如今不知身在何处；眼前的风景，却依稀还是去年的模样。——后两句是「感旧」的落点：不直说怀念，先问「人何处」——一问而无答，再低头看眼前：水还是那片水，月还是那轮月，「依稀似去年」。一个「似」字最伤：像，却终究不是——景是「同」的，人是「空」的。以景之不变反衬人之不在，物是人非之感尽在言外。',
  zhu:[['同来望月人','曾经一同来这江楼赏月的人——旧日同游的友人'],['人何处','人在哪里——一问而无答，怅惘全在这一问里'],['依稀','模模糊糊、隐约相仿的样子——风景大略还是旧时光景'],['似去年','「似」字最可玩味：像去年，却终究不是去年——景同而人非'],['物是人非','风景依旧而人已不在——以景之「不变」反衬人之「不在」，感旧之情尽在言外']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「独上江楼思渺然」的下一句是？', o:['月光如水水如天','同来望月人何处','风景依稀似去年'], a:0},
 {q:'「同来望月人何处」的下一句是？', o:['月光如水水如天','风景依稀似去年','独上江楼思渺然'], a:1},
 {q:'「独上江楼思渺然」的「渺」，读音和意思都正确的一项是？', o:['读 miǎo，悠远、迷茫的样子——「思渺然」即思绪悠远绵长、怅惘无际','读 miào，藐视、轻视——诗人登上江楼俯视江水','读 miáo，描画、描摹——诗人想把月色描摹下来'], a:0},
 {q:'关于作者赵嘏与这首诗，下列说法正确的是？', o:['赵嘏是唐代诗人，因曾任渭南尉被称作「赵渭南」；此诗又题《江楼旧感》，是月夜登楼怀念旧游之作','赵嘏是南宋爱国词人，号渭南伯；此诗是他晚年隐居山阴镜湖时所作','赵嘏是「初唐四杰」之一；《江楼感旧》写的是登楼观阵、投笔从戎的豪情'], a:0},
 {q:'「月光如水水如天」历来被推为名句。对它妙处的理解，最准确的一项是？', o:['用夸张手法写江水声势：月光之下江水奔腾翻涌，涛声如雷','「水」字顶针上递下接：月华泻地如水、水色接天如天——七个字写出澄澈空明、上下无界的水天月色，以景之静澈衬思之渺远、人之孤单','单纯写景：月亮倒映在水中，说明江面平静无波，与诗人的情感无关'], a:1},
];
"""

SCENES_JS = """/* ================= 江楼感旧 · 两境场景（水墨夜思·满月江楼：独上江楼、望月感旧） =================
   美术立意：水墨夜思色板写「月光盛满的亮夜」——底色 #0d1117、雾 #10161f～#131a26 系，
   accent=#a0b4cc（月银水青）只落在满月晕/水中月影/银辉光路/水天光带/边缘光/UI 上，全页近零饱和。
   与已有水墨夜思页第一眼可区分：不做舟夜孤灯碎星（zhouye，无月）、不做渡口小楼三点渔火
   （ti-jinlingdu，斜月暗夜远望）、不做古寺竹径（ti-poshansi）、不做雨前危城（xianyang-chenglou）
   ——做「满月当空+水中月影+银辉光路+水天一色」的澄澈亮夜与登楼望月：月是唯一主角，
   江天被月光灌满，天水在一线银光里相接。
   境壹（标志性瞬间）：月光如水水如天——满月高悬（ms 1.9 满月），水中月影与之上下相望，
   银辉光路自天际月下直铺楼前，地平一线水光接天；银尘微光浸染全页，登楼人独立楼头。
   境贰（末境可点击）：风景依稀似去年——同一江楼同一月（刻意复用构图=「依稀」），
   点击：去年同来望月的人影在月色中淡现（半透明银影并肩而立），凝望片刻又缓缓散去。 */

/* —— 江楼 makeJianglou(o)：开敞楼亭（台基+台阶+底层柱廊+腰檐平座栏杆+上层开敞柱廊+四阿顶，
   合批 1 mesh）——「独上江楼」；无墙无窗全开敞（与 ti-jinlingdu 暖窗小山楼、xianyang 垛口
   城楼异形）：这是供人登临望月的临江楼亭，人立在平座栏杆之内 */
function makeJianglou(o){
  o=o||{};
  const w=o.w===undefined?4.4:o.w;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w*1.72,0.72,w*1.38);
  base.translate(0,0.36,0); B.put(base,0x1a2330);
  const st1=new THREE.BoxGeometry(w*0.80,0.22,w*0.34);
  st1.translate(0,0.11,w*0.82); B.put(st1,0x161e2a);
  const st2=new THREE.BoxGeometry(w*0.64,0.20,w*0.26);
  st2.translate(0,0.30,w*0.70); B.put(st2,0x18202e);
  const fl=new THREE.BoxGeometry(w,0.26,w*0.80);
  fl.translate(0,0.85,0); B.put(fl,0x222d3f);
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const col=new THREE.CylinderGeometry(0.10,0.13,2.10,6);
    col.translate(sx*w*0.42,2.03,sz*w*0.30); B.put(col,0x273244);
  }
  for(let sx=-1;sx<=1;sx+=2){
    const col=new THREE.CylinderGeometry(0.10,0.13,2.10,6);
    col.translate(sx*w*0.42,2.03,0); B.put(col,0x273244);
  }
  const deck=new THREE.BoxGeometry(w*1.16,0.20,w*0.90);
  deck.translate(0,3.20,0); B.put(deck,0x2a3850);
  const eave=new THREE.BoxGeometry(w*1.34,0.10,w*1.04);
  eave.translate(0,3.06,0); B.put(eave,0x1c2634);
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const post=new THREE.CylinderGeometry(0.055,0.07,0.72,5);
    post.translate(sx*w*0.52,3.66,sz*w*0.38); B.put(post,0x1e2939);
  }
  const railF=new THREE.BoxGeometry(w*1.04,0.07,0.07);
  railF.translate(0,4.04,w*0.38); B.put(railF,0x324058);
  const railB=new THREE.BoxGeometry(w*1.04,0.07,0.07);
  railB.translate(0,4.04,-w*0.38); B.put(railB,0x324058);
  const railL=new THREE.BoxGeometry(0.07,0.07,w*0.76);
  railL.translate(w*0.52,4.04,0); B.put(railL,0x324058);
  const railR=new THREE.BoxGeometry(0.07,0.07,w*0.76);
  railR.translate(-w*0.52,4.04,0); B.put(railR,0x324058);
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const col2=new THREE.CylinderGeometry(0.095,0.12,2.55,6);
    col2.translate(sx*w*0.44,4.58,sz*w*0.30); B.put(col2,0x2a3548);
  }
  const beam=new THREE.BoxGeometry(w*0.98,0.12,w*0.68);
  beam.translate(0,5.92,0); B.put(beam,0x1f2a3a);
  const roof=new THREE.ConeGeometry(w*0.94,1.80,4);
  roof.rotateY(Math.PI/4); roof.scale(1.20,1,0.86); roof.translate(0,6.88,0); B.put(roof,0x151f2d);
  const finial=new THREE.SphereGeometry(0.14,6,5);
  finial.translate(0,7.86,0); B.put(finial,0x3a4759);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x36445c,emissive:0x05070c}),{c:0xa0b4cc,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 水中月影 makeYueying(o)：江面月影（倒悬 limbTex 月盘+月银晕圈；均 fog:false 如星月
   点名；fadeK 铁律：初值=最大）——与天心满月上下相望，「月光如水」的落点 */
function makeYueying(o){
  o=o||{};
  const r=o.r===undefined?13:o.r;
  const op=o.op===undefined?0.34:o.op, hz=o.haze===undefined?0.12:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xdfe8f4:o.color,
    transparent:true,opacity:op,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*1.05,1); g.add(disc);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.haloC===undefined?0xa0b4cc:o.haloC,
    transparent:true,opacity:hz,depthWrite:false,fog:false}));
  halo.scale.set(r*4.6,r*1.5,1); g.add(halo);
  const ph=(o.seed===undefined?22801:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k, sw=0.9+0.1*Math.sin(t*0.5+ph);
    disc.material.opacity=kk*op*sw;
    halo.material.opacity=kk*hz*(0.82+0.18*Math.sin(t*0.31+ph*2.0));
    disc.position.x=Math.sin(t*0.42+ph)*1.4;          /* 涟漪轻晃 */
    halo.position.x=disc.position.x;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 银辉光路 makeYinguang(o)：月光自天际铺落江面的光路（一串纵扁 glow Sprite 沿月方位
   排布+一道水天相接的银辉横带；均 fog:false；fadeK 铁律：初值=最大）——
   「月光如水水如天」：光路连起天心月与水中月，横带抹平水天界线 */
function makeYinguang(o){
  o=o||{};
  const pts=o.pts===undefined?[[-42,-140],[-35,-118],[-29,-98],[-24,-80],[-19,-64],[-15,-50],[-11,-38]]:o.pts;
  const bandPos=o.bandPos===undefined?[-20,5.2,-152]:o.bandPos;
  const g=new THREE.Group(), items=[];
  const R=seedRnd(o.seed===undefined?22811:o.seed);
  for(let i=0;i<pts.length;i++){
    const op0=0.06+0.09*R();
    const m=new THREE.SpriteMaterial({map:glowTex(),
      color:i<3?0xbcc9dc:0xc9d5e4,transparent:true,
      opacity:op0,depthWrite:false,fog:false});
    const s=new THREE.Sprite(m);
    const sc=5.0+i*1.6;
    s.scale.set(sc*(0.8+0.5*R()),sc*0.40,1);
    s.position.set(pts[i][0],0.35,pts[i][1]);
    s.renderOrder=2; g.add(s); items.push({m:m,op0:op0,ph:R()*6.283});
  }
  const band=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa0b4cc,
    transparent:true,opacity:0.12,depthWrite:false,fog:false}));
  band.scale.set(270,11,1); band.position.set(bandPos[0],bandPos[1],bandPos[2]);
  band.renderOrder=2; g.add(band);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.m.opacity=kk*it.op0*(0.62+0.38*Math.sin(t*(0.7+i*0.09)+it.ph));
    }
    band.material.opacity=kk*0.12*(0.80+0.20*Math.sin(t*0.22+1.3));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 同游虚影 makeGuiying(o)：去年同来望月的人影（crowdGeo 剪影×2，MeshBasicMaterial
   半透明银影；初值=最大 opacity、组 visible=false 硬关——点击前无幻影）；
   rv 0→1：淡现（0~0.30）→凝望（0.30~0.52）→散去（0.52~1，上浮如雾）——末境点击 */
function makeGuiying(o){
  o=o||{};
  const peak=o.peak===undefined?0.30:o.peak;
  const spots=o.spots===undefined?[[2.8,0,-30.2],[0.6,0,-29.6]]:o.spots;
  const g=new THREE.Group(), figs=[];
  for(let i=0;i<spots.length;i++){
    const geo=crowdGeo();
    const m=new THREE.MeshBasicMaterial({color:0xc9d6e6,transparent:true,opacity:peak,
      depthWrite:false});
    const mesh=new THREE.Mesh(geo,m);
    mesh.position.set(spots[i][0],spots[i][1],spots[i][2]);
    mesh.scale.setScalar(i===0?1.42:1.32);
    mesh.rotation.y=i===0?3.02:2.86;
    mesh.renderOrder=4; mesh.frustumCulled=false;
    g.add(mesh); figs.push({mesh:mesh,m:m,ph:i*2.1});
  }
  const aura=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa0b4cc,
    transparent:true,opacity:0.10,depthWrite:false,fog:false}));
  aura.scale.set(16,12,1); aura.position.set(1.8,3.4,1.2);
  aura.renderOrder=3; g.add(aura);
  g.visible=false;
  const sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const appear=sm01(r/0.30);
    const dis=1-sm01((r-0.52)/0.48);
    const env=Math.min(appear,dis);
    const drift=Math.max(0,(r-0.52)/0.48);
    for(let i=0;i<figs.length;i++){
      const f=figs[i];
      f.m.opacity=kk*peak*env*(0.80+0.20*Math.sin(t*0.9+f.ph));
      f.mesh.position.y=spots[i][1]+drift*(2.0+i*0.7);
    }
    aura.material.opacity=kk*0.10*env;
    g.visible=kk*r>0.004&&env>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* 登楼人：全诗贯穿的同一造型（青灰袍、幞头；每次 build 新建材质） */
function jlFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2a3448,belt:0x74879c,skin:0xd3b294,collar:0x9aa8ba,
    hair:0x12161e,hat:'幞头',rimC:0xa0b4cc,rim:0.45,noProp:true,scale:scale===undefined?1.6:scale});
}

/* 远岸横陈 makeYuan(o)：江对岸的低平远岸（低多峰脊，两层，带雾骨相）——水天相接处的极淡一笔 */
function makeYuan(o){
  o=o||{};
  return makeRange({r:o.r===undefined?240:o.r,h:o.h===undefined?7:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?22821:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x1c2634,
    fogK:o.fogK===undefined?0.58:o.fogK,glowK:0.05,glow:0xaebccd,
    y:o.y===undefined?-11:o.y,order:-6});
}

function bCover(){ // 卷首 · 月满江楼远望：江楼踞岸、满月初升、银辉铺江、水天一色
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:90,amp:0.12,freq:0.15,speed:0.32,flow:[0.22,0.04],spec:0.92,
    deep:0x05080e,shallow:0x0c1420,skyc:0x121a28,moonDir:[-0.30,0.14,-0.94]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xbcc9dc);
  water.mesh.position.set(0,-0.52,-130); g.add(water.mesh);
  const grd=makeGround({r:76,c1:0x0a0f18,c2:0x151d2b,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,62);
  const yuan=makeYuan({r:230,h:8,seed:22822}); yuan.g.position.set(0,0,-160); g.add(yuan.g);
  /* 江楼踞岸（开敞楼亭），登楼人已在楼头 */
  const lou=makeJianglou({scale:1.45,rim:0.18}); lou.position.set(14,-0.28,-8);
  lou.rotation.y=-0.35; g.add(lou);
  const poet=jlFigure(1.15); poet.position.set(15.2,4.50,-7.0); poet.rotation.y=3.0; g.add(poet);
  /* 水中月影 + 银辉光路 + 水天横带 */
  const yy=makeYueying({r:10,op:0.38,seed:22801}); yy.position.set(-26,-0.6,-84); g.add(yy);
  const yg=makeYinguang({seed:22812}); g.add(yg);
  /* 江雾横腰 + 银尘微光 */
  const mist=makeMist({n:6,spread:[210,10,72],pos:[0,2.6,-70],scale:58,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:30,box:[170,18,66],pos:[0,9,-36],color:0xaebfd2,size:4.4,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:11,d:5,color:0x05080e,seed:22823,sway:0.8,rim:0.10,rimC:0xa0b4cc});
  fg1.g.position.set(-10,-1.2,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05080e,seed:22824,rim:0.10,rimC:0xa0b4cc});
  fg2.g.position.set(12.5,-1.5,12); g.add(fg2.g);
  addLights(g,{c:0xaabccd,i:0.38,p:[-44,56,-52]},{c:0x182230,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    poet.update(t,k); yy.update(t,k); yg.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bDenglou(){ // 壹（标志性瞬间）· 独上江楼 —— 独上江楼思渺然，月光如水水如天：
                    // 楼头独立望月，满月与水中月影上下相望，银辉光路直铺楼前，水天一色
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:96,amp:0.11,freq:0.14,speed:0.30,flow:[0.20,0.04],spec:0.95,
    deep:0x05080e,shallow:0x0c1420,skyc:0x131b29,moonDir:[-0.30,0.14,-0.94]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xc4d2e4);
  water.mesh.position.set(0,-0.52,-140); g.add(water.mesh);
  const grd=makeGround({r:78,c1:0x0a0f18,c2:0x161e2c,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,62);
  const yuan=makeYuan({r:250,h:7,seed:22825}); yuan.g.position.set(-8,0,-165); g.add(yuan.g);
  /* 江楼：登临之处（楼头独立——「独上」） */
  const lou=makeJianglou({scale:2.05,rim:0.18}); lou.position.set(3.5,-0.3,-31);
  lou.rotation.y=0.06; g.add(lou);
  const poet=jlFigure(1.7); poet.position.set(6.4,6.47,-29.6); poet.rotation.y=3.05; g.add(poet);
  /* 标志性瞬间：水中月影 + 银辉光路 + 水天横带（满月为 STAGES 天空的 ms 1.9 满月） */
  const yy=makeYueying({r:14,op:0.44,haze:0.14,seed:22802}); yy.position.set(-24,-0.6,-78); g.add(yy);
  const yg=makeYinguang({seed:22813}); g.add(yg);
  /* 江雾横腰 + 银尘微光浸染 + 夜气横流 */
  const mist=makeMist({n:6,spread:[220,10,76],pos:[0,3.0,-74],scale:60,color:0x2a3648,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:32,box:[180,20,70],pos:[0,10,-38],color:0xaebfd2,size:4.4,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const wind=makeFlow({n:220,box:[120,10,50],pos:[0,7,-24],color:0x5f6e84,size:15,speed:3.2,maxA:0.08});
  g.add(wind.points);
  /* 前景：楼头栏杆一角（与楼中人同望）+ 岸边芦苇低伏 */
  const fg1=makeForeground({kind:'栏杆',w:30,h:3.2,color:0x05080e,seed:22826,rim:0.10,rimC:0xa0b4cc});
  fg1.g.position.set(1,-3.5,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',w:22,n:9,d:4,color:0x05080e,seed:22827,sway:0.75,rim:0.09,rimC:0xa0b4cc});
  fg2.g.position.set(-12,-2.7,11); g.add(fg2.g);
  addLights(g,{c:0xaabccd,i:0.42,p:[-44,58,-50]},{c:0x182230,i:0.64});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    poet.update(t,k); yy.update(t,k); yg.update(t,k);
    mist.update(t,k); motes.update(t); wind.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bGanjiu(){ // 贰（末境·可点击）· 望月感旧 —— 同来望月人何处，风景依稀似去年：
                    // 风景依稀=刻意复用江楼满月构图；点击：去年同游虚影淡现又散
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  /* 风景依稀：同一江月，月稍西沉、夜稍深 */
  const water=makeWater({size:620,seg:96,amp:0.11,freq:0.14,speed:0.30,flow:[0.20,0.04],spec:0.90,
    deep:0x05080e,shallow:0x0c1420,skyc:0x121a27,moonDir:[-0.32,0.13,-0.94]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xc4d2e4);
  water.mesh.position.set(0,-0.52,-140); g.add(water.mesh);
  const grd=makeGround({r:78,c1:0x0a0f18,c2:0x161e2c,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,62);
  const yuan=makeYuan({r:250,h:7,peaks:4,seed:22828}); yuan.g.position.set(-8,0,-165); g.add(yuan.g);
  const lou=makeJianglou({scale:1.95,rim:0.18}); lou.position.set(4,-0.3,-32);
  lou.rotation.y=0.02; g.add(lou);
  const poet=jlFigure(1.65,'指月'); poet.position.set(6.6,6.14,-30.6); poet.rotation.y=3.02; g.add(poet);
  /* 水中月影 + 银辉光路 + 水天横带（依稀似去年：与境壹同一构图） */
  const yy=makeYueying({r:13.5,op:0.42,haze:0.14,seed:22803}); yy.position.set(-26,-0.6,-78); g.add(yy);
  const yg=makeYinguang({seed:22814}); g.add(yg);
  /* 标志性交互：去年同游虚影（点击前 visible=false 硬关） */
  const gy=makeGuiying({spots:[[2.8,6.14,-30.2],[0.6,6.14,-29.6]],seed:22815});
  g.add(gy);
  const mist=makeMist({n:7,spread:[220,12,76],pos:[0,3.0,-74],scale:60,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:30,box:[180,20,70],pos:[0,10,-38],color:0xaebfd2,size:4.4,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const wind=makeFlow({n:220,box:[120,10,50],pos:[0,7,-24],color:0x5f6e84,size:15,speed:3.2,maxA:0.08});
  g.add(wind.points);
  const fg1=makeForeground({kind:'栏杆',w:30,h:3.2,color:0x05080e,seed:22829,rim:0.10,rimC:0xa0b4cc});
  fg1.g.position.set(0,-3.5,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',w:22,n:9,d:4,color:0x05080e,seed:22830,sway:0.8,rim:0.09,rimC:0xa0b4cc});
  fg2.g.position.set(-12,-2.7,11); g.add(fg2.g);
  addLights(g,{c:0xaabccd,i:0.40,p:[-46,56,-50]},{c:0x182230,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/6.0);
      gy.update(t,k,ctl.reveal);
      water.update(t); yuan.update(t,0);
      poet.update(t,k); yy.update(t,k); yg.update(t,k);
      mist.update(t,k); motes.update(t); wind.update(t);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.12);
        pluck(4,0.05,0.10); pluck(2,0.60,0.08); pluck(0,1.20,0.07);   // 如旧游笑语三叠，渐远
        const fl=$('#flash'); fl.textContent='同来望月人何处 风景依稀似去年';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x060a12),hor:C(0x141c2a),bot:C(0x04070c),fog:C(0x10161f),fd:0.0050,star:0.30,
  moon:new THREE.Vector3(-58,88,-190),ms:1.6,mph:0,mhaze:0.14,dirC:C(0xaabccd),dirI:0.40,
  dirP:new THREE.Vector3(-44,56,-52),ambC:C(0x182230),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8.8,40],t:[0,9.0,34],lf:[-8,11,-24],lt:[-14,13,-44]},
  sky:()=>SK({fd:0.0046,star:0.30,ms:1.6,moon:new THREE.Vector3(-58,84,-190)}) },
{ name:'独上江楼',dwell:17,river:0.02,build:bDenglou,
  cam:{f:[2.0,7.6,16],t:[-0.6,7.4,10],lf:[-4,8.8,-14],lt:[-9,10.5,-30]},
  sky:()=>SK({fd:0.0050,star:0.26,ms:1.9,mhaze:0.12,
    moon:new THREE.Vector3(-58,96,-190),dirC:C(0xaabccd),dirI:0.42,
    ambC:C(0x182230),ambI:0.64}) },
{ name:'望月感旧',dwell:19,river:0.02,build:bGanjiu,
  cam:{f:[0,7.8,15],t:[-1,7.6,9.5],lf:[-3,9,-18],lt:[-8,10.5,-36]},
  sky:()=>SK({fd:0.0054,star:0.22,ms:1.8,mhaze:0.16,
    moon:new THREE.Vector3(-66,86,-190),dirC:C(0xa4b6ca),dirI:0.38,
    ambC:C(0x161e2c),ambI:0.60}) },
];
"""
