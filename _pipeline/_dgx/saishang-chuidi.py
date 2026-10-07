# -*- coding: utf-8 -*-
"""saishang-chuidi.py —— 《塞上听吹笛》（唐·高适，queue no.221，大漠金戈）生成配置
两境（N=queue stages 数）：雪净牧还（雪净胡天牧马还·月明羌笛戍楼间——雪原牧归、静夜闻笛）、
笛满关山（借问梅花何处落·风吹一夜满关山——标志性瞬间+末境点击「笛声起+梅花雪片漫卷关山」）。
大漠金戈全套色板：底色 #120d08、雾 #140d07～#161009 系、文字 #f0e2cc，accent=#c49a5a
（queue 分配强调色，沙金月色）只落在月色雪光/戍楼灯火/人物边缘光/笛纹音波/梅花/UI 上，禁艳金。
时间推进线：同一月夜的两重「听」：境壹=远望（雪净月明、牧马成群归来、戍楼一点灯火）
→ 境贰=近听（戍楼吹笛人立于挑台、关山两重横陈，点击后笛声化作漫天梅花随风漫卷关山）。
标志性瞬间（境贰·全诗名句）：风吹一夜满关山——笛曲《梅花落》化作漫天梅花，随夜风一阵一阵漫卷关山；
与已有边塞页第一眼可区分：不做孤城/金甲/烽燧/密林夜射/战场残垣，做「雪净月明+牧马归+戍楼笛声」
的边塞静夜——大漠金戈赛道里唯一的一片月光雪原。
末境点击（queue interact：点击梅花落——笛声起+梅花雪片漫卷关山）：点击画面——笛声五声渐起、
笛纹音波环自戍楼荡开不歇，漫天梅花随风波前一阵一阵漫卷关山，「借问梅花何处落 风吹一夜满关山」题字同现。
考点钉子：羌 qiāng / 牧 mù（小测第 3 题落点）；〈梅花落〉汉乐府横吹笛曲+高适边塞诗人身份
（与岑参并称「高岑」，第 4 题）；「化虚为实/通感」名句手法（第 5 题）。
多音字：还 huán 从通行本（tts.json 钉「牧马还→牧马环」；塞 sài 钉「塞上→赛上」；戍 shù 钉「戍楼→树楼」）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='saishang-chuidi', title='塞上听吹笛', dyn='唐 · 高适', brand_author='高 适',
    gold_rgb='196,154,90',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#c49a5a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(196,154,90,.3);
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
    tip='轻点画面 / 按空格 —— 笛声起处，梅花落满关山',
    hint='← → 键或空格逐境游览 · 末境可点击画面：听一声笛起，看〈梅花落〉化作漫天梅花漫卷关山',
    cover_read='塞上听吹笛。唐，高适。雪净胡天牧马还，月明羌笛戍楼间。借问梅花何处落，风吹一夜满关山。',
    cover_p1='两重意境，随诗句次第展开：雪净月明的胡天之下，牧马成群归来，羌笛声从戍楼间悠悠传出；试问笛中的《梅花落》究竟落向何处——一夜风把它吹散，落满了层层关山。',
    cover_p2='边读诗，边走进高适笔下的边塞静夜：笛曲本无形，诗人偏问「梅花何处落」——读懂这个双关，就读懂了化声为花的想象，也读懂了征人月夜闻笛时那一缕哀而不伤的乡愁。',
    end_h2='梅落 · 满关山', cn_word='贰',
    words_js="['再听一次塞上笛','初识高适，尚需共读','渐入诗境，再诵几遍','月明笛声，渐入耳鼓','已解梅落满山意','风吹一夜，关山皆花']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'雪净牧还', jing:'冰雪融尽的胡天明净如洗，月光下牧马成群归来，羌笛声从戍楼间悠悠传出 —— 雪净、月明、牧还，一片边关静夜。（雪净胡天 · 牧马归还 · 月明羌笛 · 戍楼）',
  segs:[
   {c:'雪净胡天牧马还，', p:py('xuě jìng hú tiān mù mǎ huán')},
   {c:'月明羌笛戍楼间。', p:py('yuè míng qiāng dí shù lóu jiān')}],
  read:'雪净胡天牧马还，月明羌笛戍楼间。',
  yisi:'冰雪融尽，胡地的天空明净如洗；暮色里，放牧的马群成群归来；明月高照，不知哪座戍楼上，有人吹起了羌笛。——前句写「所见」：雪净、天清、马还，是边塞难得的安闲明净，全无惯常的肃杀之气；后句写「所闻」：万籁俱寂之中，一声羌笛自戍楼间传出——静夜闻笛，笛声一起，后两句的万千联想便有了来处。',
  zhu:[['塞上','边塞一带。诗题「听吹笛」三字点明：全诗是从「听」的角度写起的——先写听到笛声前的所见（雪净、马还、月明），再写笛声本身'],['雪净','冰雪消融干净，雪后天空明净。胡天，胡地的天空（塞北）。一个「净」字写尽边塞冬末的澄澈晴朗，也悄悄卸下了边塞诗惯有的剑拔弩张'],['牧马还','放牧的马群归来。战马征用、牧地荒废是战时景象，「牧马还」三字透出战事稍歇、边地安宁的气息——这是能安然听笛的夜晚'],['羌笛','出于古代西部羌地的管乐器，竹制，音色清亮哀婉，边塞诗中最常见的乐器意象——王之涣「羌笛何须怨杨柳」写的也是它。羌，读 qiāng'],['戍楼','军队驻防瞭望警戒的碉楼。「月明羌笛戍楼间」：明月照着戍楼，笛声就在楼间响起——月是静，笛是动，一动一静互相衬托，静夜愈静，笛声愈清']] },
{ name:'笛满关山', jing:'试问笛曲里的梅花，究竟落向何处？一夜风把它吹散，落满了层层关山 —— 闻笛生情、化声为花的千古名句。（借问梅花 · 风吹一夜 · 满关山 · 标志性瞬间 · 末境点击画面：笛声起，〈梅花落〉化作漫天梅花漫卷关山）',
  segs:[
   {c:'借问梅花何处落，', p:py('jiè wèn méi huā hé chù luò')},
   {c:'风吹一夜满关山。', p:py('fēng chuī yī yè mǎn guān shān')}],
  read:'借问梅花何处落，风吹一夜满关山。',
  yisi:'借问：这笛中所吹的《梅花落》，究竟飘向何处落下了？——原来是风把它吹了一夜，洒满了关山。——妙在双关：《梅花落》本是笛曲名，诗人偏把曲名拆开来问「梅花何处落」，仿佛吹的不是曲子、而是真有梅花漫天飘散；「风吹一夜满关山」再补一笔——无形的笛声随风吹遍关山，化作处处盛开的梅花。以视觉写听觉（通感），战地苦寒的静夜顿时开满了想象里的春色：征人思乡而不哀，哀而不伤，正是高适边塞诗的浑厚气度。',
  zhu:[['借问','试问、请问——诗人向吹笛人、也向读者发问。这一问把笛曲问成了真花，是全诗想象的起点'],['梅花何处落','一语双关：既指笛曲《梅花落》，又故意把曲名拆开发问「梅花落在何处」，仿佛笛声化作了漫天飘落的梅花——曲名在此刻变成了眼前（心中）之景'],['《梅花落》','汉乐府横吹曲名（横吹曲是军中马上所奏之乐，多用笛、角吹奏）。唐代诗人常借「梅花落」写闻笛思乡；高适只用其名、不摹其声，直接让它「落」满了关山'],['关山','关塞与山岭，泛指边关的层层山峦。「满关山」：笛声（梅花）随夜风吹遍每一座关隘山岭——何处关山无明月，何处关山无笛声'],['化虚为实（通感）','笛声本不可见，诗人却让它化作漫天梅花、随风飞落——以视觉写听觉，把无形的音乐写成看得见的春色。虚景写实情：雪夜闻笛的乡思，尽在这场想象的花雨里，这正是此句成为千古名句的原因']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「雪净胡天牧马还」的下一句是？', o:['月明羌笛戍楼间','借问梅花何处落','风吹一夜满关山'], a:0},
 {q:'「借问梅花何处落」的下一句是？', o:['月明羌笛戍楼间','风吹一夜满关山','雪净胡天牧马还'], a:1},
 {q:'「月明羌笛戍楼间」的「羌」与「雪净胡天牧马还」的「牧」，读音和意思都正确的一项是？', o:['羌读 qiāng，羌笛是边塞常见的管乐器；牧读 mù，放牧——明月下羌笛声从戍楼间传出，牧放的马群正成群归来','羌读 qiáng，指强壮的士兵；牧读 mó，放养——强壮的戍卒在楼间放马','羌读 kāng，一种鼓的名目；牧读 mù，牧场——鼓声和牧场写边地操练'], a:0},
 {q:'关于「借问梅花何处落」里的「梅花」与本诗作者高适，下列说法正确的是？', o:['《梅花落》是汉乐府横吹曲名（军中笛曲）——诗人拆用曲名发问，让笛曲化作漫天飘落的梅花，一语双关；高适是唐代著名边塞诗人，与岑参并称「高岑」','《梅花落》是高适自创的新曲；高适是山水田园诗人，与王维并称「王孟」','「梅花」就是比喻雪花：边塞苦寒、雪大如花，诗人借落花写天气严寒；高适一生从未到过边塞'], a:0},
 {q:'「风吹一夜满关山」是千古名句。对它妙处的理解，最准确的一项是？', o:['用夸张手法写风势：一夜大风把关山吹平了','写战事骤起：笛声是进攻的号角，一夜之间传遍关山各处军营','化虚为实（通感）：无形的笛声随夜风吹遍关山，仿佛《梅花落》化作漫天梅花纷纷飘落——雪夜闻笛的乡思化作满关山的春色，哀而不伤'], a:2},
];
"""

SCENES_JS = """/* ================= 塞上听吹笛 · 两境场景（大漠金戈·雪夜闻笛：雪净牧还、笛满关山） =================
   美术立意：大漠金戈色板写「边塞静夜」——底色 #120d08、雾 #140d07～#161009 系，
   accent=#c49a5a（沙金月色）只落在月色雪光/戍楼灯火/人物边缘光/笛纹音波/梅花上，禁艳金。
   与已有边塞页第一眼可区分：不做孤城/金甲/烽燧/密林夜射/战场残垣，
   做「月光雪原 + 牧马归 + 戍楼笛声」——大漠金戈赛道里唯一的一片雪原静夜。
   境壹（远望）：雪净胡天、大月明照，牧马群自雪原缓步归还，远处戍楼一点灯火。
   境贰（近听·标志性瞬间+末境可点击）：戍楼吹笛人立于挑台、关山两重横陈；
   点击：笛声起（五声渐起+笛纹音波环自戍楼荡开不歇），漫天梅花随风波前漫卷关山。 */

/* —— 牧马群 makeMuMa(o)：简化低模马（躯干/四腿/颈/头/耳/尾/鬃，GeoBag 分 k 组合批），
   整群缓步位移（走一段绕回，wrap 于 span）+ 分组迈步起伏——「牧马还」 */
function makeMuMa(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22211:o.seed);
  const n=o.n===undefined?6:o.n, k=o.k===undefined?3:o.k;
  const w=o.w===undefined?30:o.w, d=o.d===undefined?7:o.d;
  const s=o.s===undefined?1.0:o.s;
  const bags=[], meshes=[], phases=[];
  for(let i=0;i<k;i++)bags.push(new GeoBag());
  for(let i=0;i<n;i++){
    const B=bags[i%k];
    const x=(R()-0.5)*w, zz=(R()-0.5)*d, hh=(0.88+0.26*R())*s;
    const coat=[0x2b2014,0x33261a,0x231a10,0x1d150c][Math.floor(R()*4)];
    const dk=shadeColor(coat,0.72);
    const bd=new THREE.SphereGeometry(1.5,9,7);
    bd.scale(1.5*hh,hh,0.72*hh);
    bd.translate(x,3.2*hh,zz); B.put(bd,coat);
    const legR=0.17*hh, legT=2.35*hh;
    [[0.95,0.35],[0.95,-0.38],[-1.0,0.36],[-1.0,-0.37]].forEach(function(p){
      const lg=new THREE.CylinderGeometry(legR*0.8,legR,legT,5);
      lg.translate(x+p[0]*hh,legT*0.5,zz+p[1]*hh);
      B.put(lg,dk);
    });
    B.put(limbGeo([x+1.6*hh,3.7*hh,zz],[x+2.75*hh,5.35*hh,zz],0.62*hh,0.34*hh,6),coat);
    B.put(limbGeo([x+2.8*hh,5.5*hh,zz],[x+3.85*hh,4.95*hh,zz],0.40*hh,0.17*hh,6),dk);
    for(let e=0;e<2;e++){
      const ear=new THREE.ConeGeometry(0.10*hh,0.36*hh,4);
      ear.translate(x+2.92*hh,5.95*hh,zz+(e?0.15:-0.15)*hh);
      B.put(ear,dk);
    }
    B.put(limbGeo([x-2.25*hh,3.9*hh,zz],[x-3.0*hh,2.1*hh,zz],0.26*hh,0.05*hh,5),dk);
    B.put(limbGeo([x+2.15*hh,4.5*hh,zz],[x+2.9*hh,5.6*hh,zz],0.16*hh,0.05*hh,4),dk);
  }
  const g=new THREE.Group();
  for(let i=0;i<k;i++){
    const m=bags[i].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      specular:0x2a2014,emissive:0x040302}),{c:0xc49a5a,i:o.rim===undefined?0.14:o.rim,p:2.2}));
    g.add(m); meshes.push(m); phases.push(R()*6.283);
  }
  const span=o.span===undefined?0:o.span, v=o.walk===undefined?0:o.walk;
  let bx=null;
  g.userData.update=function(t){
    for(let i=0;i<k;i++) meshes[i].position.y=0.14*s*Math.sin(t*1.15+phases[i]);
    if(span>0&&v>0){
      if(bx===null)bx=g.position.x;
      let xx=bx+t*v;
      xx=((xx+span*0.5)%span+span)%span-span*0.5;
      g.position.x=xx;
    }
  };
  return g;
}

/* —— 戍楼 makeShuLou(o)：夯土楼身+挑台+垛口+四柱攒尖顶（GeoBag 合批 1 mesh），
   楼身一扇暖灯窗 + 挑台灯辉 sprite + 点光（灯火微微闪烁）——「戍楼间」
   挑台面在局部 y = D（默认 4.4）：吹笛人立于其上 */
function makeShuLou(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22201:o.seed);
  const D=o.deckY===undefined?4.4:o.deckY;
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(2.6,3.2,1.2,8);
  base.translate(0,0.6,0); B.put(base,0x241c12);
  const body=new THREE.CylinderGeometry(1.7,2.3,D-1.2,8);
  body.translate(0,1.2+(D-1.2)/2,0); B.put(body,0x2b2014);
  const deck=new THREE.CylinderGeometry(2.5,1.75,0.5,8);
  deck.translate(0,D-0.25,0); B.put(deck,0x33271a);
  for(let i=0;i<10;i++){
    const a=i/10*6.283+0.31;
    const mer=new THREE.BoxGeometry(0.62,0.56,0.22);
    mer.rotateY(-a);
    mer.translate(Math.sin(a)*2.28,D+0.28,Math.cos(a)*2.28);
    B.put(mer,0x2a1f13);
  }
  for(let i=0;i<4;i++){
    const a=i/4*6.283+0.785;
    const post=new THREE.CylinderGeometry(0.075,0.09,2.4,5);
    post.translate(Math.sin(a)*1.55,D+1.2,Math.cos(a)*1.55);
    B.put(post,0x1f150c);
  }
  const roof=new THREE.ConeGeometry(2.75,1.15,4);
  roof.rotateY(Math.PI/4);
  roof.translate(0,D+2.975,0); B.put(roof,0x191009);
  const knob=new THREE.SphereGeometry(0.13,6,5);
  knob.translate(0,D+3.62,0); B.put(knob,0x6a5232);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a2c1c,emissive:0x050302}),{c:0xc49a5a,i:o.rim===undefined?0.18:o.rim,p:2.4})));
  /* 楼身暖灯窗：夜里透出的一点灯火 */
  const win=new THREE.Mesh(new THREE.BoxGeometry(0.46,0.6,0.12),
    new THREE.MeshBasicMaterial({color:0xd8a860,transparent:true,opacity:0.85}));
  win.position.set(0,3.3,1.92); g.add(win);
  /* 挑台灯辉 + 点光（闪烁包络 ≤1.0，fadeK 铁律：每帧写必乘 k） */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8a860,
    transparent:true,opacity:0.16,depthWrite:false}));
  glow.scale.set(6.5,6.5,1); glow.position.set(0,D+0.9,0); g.add(glow);
  const lamp=new THREE.PointLight(0xd8a860,0.55,30);
  lamp.position.set(0,D+0.9,1.2); g.add(lamp);
  const ph=R()*6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k, fl=0.86+0.14*Math.sin(t*2.6+ph);
    glow.material.opacity=kk*0.16*fl;
    lamp.intensity=kk*0.55*fl;
  };
  return g;
}

/* —— 羌笛 makeQiangDi()：竹笛横持（细管+微高光+accent 流苏坠），挂到吹笛人口边（局部坐标） */
function makeQiangDi(){
  const B=new GeoBag();
  const tube=new THREE.CylinderGeometry(0.038,0.042,1.0,6);
  tube.rotateZ(Math.PI/2);
  B.put(tube,0x4a3822);
  const mouth=new THREE.CylinderGeometry(0.045,0.045,0.05,6);
  mouth.rotateZ(Math.PI/2); mouth.translate(-0.32,0,0);
  B.put(mouth,0x6a5232);
  for(let i=0;i<3;i++){
    const hole=new THREE.SphereGeometry(0.018,5,4);
    hole.translate(-0.05+i*0.13,0.038,0);
    B.put(hole,0x1f150c);
  }
  const tassel=new THREE.ConeGeometry(0.045,0.22,5);
  tassel.translate(0.52,-0.13,0);
  B.put(tassel,0xc49a5a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4a30,emissive:0x070502}),{c:0xc49a5a,i:0.30,p:2.6})));
  return g;
}

/* —— 梅花雪片 makeMeihua(o)：自写着色器（自上而下缓落+夜风横漂；
   「漫卷」机关：亮度波前沿 +x 一阵一阵扫过——风一阵，花一阵；
   uMaxA 作花势可渐起；uFade 显式交给 setFade；深底用 NormalBlending，additive 会洗成白棉团） */
const SSC_HUA_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uWind;
varying float vA;
void main(){
  vec3 p=position;
  float fall=fract(uTime*uSpeed*(0.35+0.75*aSeed)+aSeed);
  p.y-=fall*uBox.y;
  p.x+=sin(uTime*(0.5+0.4*aSeed)+aSeed*43.0)*(0.9+1.7*aSeed)+uWind*uTime*(0.35+aSeed*0.5);
  p.x=mod(p.x+uBox.x*0.5,uBox.x)-uBox.x*0.5;
  p.z+=cos(uTime*0.4+aSeed*31.0)*1.7;
  vA=smoothstep(0.0,0.10,fall)*smoothstep(1.0,0.86,fall);
  float band=0.40+0.60*sin(p.x*0.055-uTime*1.05);
  vA*=band;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.75+0.25*sin(uTime*1.3+aSeed*50.0))*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeMeihua(o){
  o=o||{};
  const n=o.n===undefined?240:o.n, box=o.box===undefined?[130,44,66]:o.box, pos=o.pos===undefined?[0,23,-26]:o.pos;
  const color=o.color===undefined?0xe8ccc2:o.color, size=o.size===undefined?3.2:o.size;
  const speed=o.speed===undefined?0.42:o.speed, wind=o.wind===undefined?1.35:o.wind;
  const maxA=o.maxA===undefined?0.001:o.maxA;
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
    vertexShader:SSC_HUA_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points:points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 笛纹音波环 makeDiWen(o)：点击后自戍楼荡开的音波环（横向 Ring 逐环扩散淡出；
   amp 保持>0 则环持续不歇——「一夜」笛声；fadeK 铁律：初值=最大、每帧写必乘 k） */
function makeDiWen(o){
  o=o||{};
  const n=o.n===undefined?4:o.n;
  const reach=o.reach===undefined?42:o.reach, speed=o.speed===undefined?0.11:o.speed;
  const maxOp=o.maxOp===undefined?0.30:o.maxOp, color=o.color===undefined?0xc9a06a:o.color;
  const g=new THREE.Group(), rings=[];
  for(let i=0;i<n;i++){
    const mesh=new THREE.Mesh(new THREE.RingGeometry(0.94,1.0,56),
      new THREE.MeshBasicMaterial({color:color,transparent:true,opacity:maxOp,depthWrite:false,side:THREE.DoubleSide}));
    mesh.rotation.x=-Math.PI/2; mesh.position.y=0; mesh.renderOrder=4;
    g.add(mesh); rings.push({m:mesh.material,mesh:mesh,ph:i/n});
  }
  g.update=function(t,k,amp){
    if(amp===undefined||amp<=0.001){ for(let i=0;i<n;i++)rings[i].m.opacity=0; return; }
    for(let i=0;i<n;i++){
      const it=rings[i], cyc=(t*speed+it.ph)%1, s=1.8+cyc*reach;
      it.mesh.scale.set(s,s,1);
      it.m.opacity=amp*k*Math.pow(1-cyc,1.6)*maxOp;
    }
  };
  g.userData.update=g.update;
  return g;
}

/* 闻笛人（诗人高适）/ 戍楼吹笛人：全诗贯穿的同一造型系（每次 build 新建材质） */
function sscFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x33281a,belt:0x8a6a44,skin:0xd9b189,collar:0x6a5232,
    hair:0x1a140c,hat:'幞头',beard:true,rimC:0xc49a5a,rim:0.5,noProp:true,scale:scale===undefined?1.8:scale});
}
function sscGuard(scale){
  return makeFigure({pose:'举杯',robe:0x2e2416,belt:0x7a5c38,skin:0xd9b189,collar:0x4c3a22,
    hair:0x161009,hat:'发髻',beard:false,rimC:0xc49a5a,rim:0.55,noProp:true,scale:scale===undefined?0.55:scale});
}

function bCover(){ // 卷首 · 雪净胡天远望：月光雪原、牧马群缓归、远处戍楼一点灯火、大月明照
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x38342a,c2:0x585140,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:22131,color:0x0d0906,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-20,0,-96); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:230,h:13,layers:2,peaks:4,seed:22132,color:0x0a0704,atmo:0x2e2114,
    fogK:0.58,glowK:0.04,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(16,0,-58); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  const herd=makeMuMa({n:5,k:2,w:20,d:5,seed:22133,walk:1.3,span:60,rim:0.13});
  herd.position.set(0,-1.75,-12); g.add(herd);
  const lou=makeShuLou({seed:22134,rim:0.15});
  lou.position.set(24,-1.8,-42); lou.scale.setScalar(0.8); g.add(lou);
  const wind=makeFlow({n:340,box:[110,10,44],pos:[0,2.8,-20],color:0x6e5e46,size:15,speed:4.2,maxA:0.10});
  g.add(wind.points);
  const snow=makeGlow({n:30,box:[120,12,46],pos:[0,6,-24],color:0xbfb298,size:2.0,speed:0.10,rise:-0.10,add:false,maxA:0.08});
  g.add(snow.points);
  const mist=makeMist({n:6,spread:[230,14,80],pos:[0,5,-56],scale:70,color:0x5a4c38,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[170,18,70],pos:[0,9,-36],color:0xc9b28a,size:4.2,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x14100a,seed:22135,rim:0.10,rimC:0xc49a5a});
  fg1.g.position.set(-12,-1.9,15); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',n:4,w:12,d:4,color:0x100b06,seed:22136,sway:0.7,rim:0.08,rimC:0xc49a5a});
  fg2.g.position.set(11,6.2,13); g.add(fg2.g);
  addLights(g,{c:0xc0a878,i:0.38,p:[-50,60,-30]},{c:0x2c2418,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); grd.update(); herd.userData.update(t);
    lou.userData.update(t,k);
    wind.update(t); snow.update(t); motes.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXuehuan(){ // 壹 · 雪净牧还 —— 雪净胡天牧马还，月明羌笛戍楼间：雪原牧归，静夜闻笛
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x3a362b,c2:0x5a5340,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:17,layers:2,peaks:5,seed:22141,color:0x0c0805,atmo:0x2e2114,
    fogK:0.64,glowK:0.05,glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-30,0,-100); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:240,h:13,layers:2,peaks:4,seed:22142,color:0x0a0704,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(18,0,-56); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  /* 牧马群：自画面深处向戍楼方向缓步归还（马道在戍楼身后 z≈-40 一带，
     马影恒在地平线一带，不与近景人物剪影相叠；s 放大补远） */
  const herd=makeMuMa({n:7,k:3,w:34,d:7,s:1.15,seed:22143,walk:2.0,span:84,rim:0.20});
  herd.position.set(0,-1.75,-20); g.add(herd);
  /* 戍楼：远处一点灯火（月下吹笛处） */
  const lou=makeShuLou({seed:22144,rim:0.18});
  lou.position.set(15,-1.8,-32); lou.scale.setScalar(1.0); g.add(lou);
  /* 闻笛人（诗人）：立于雪坡巨石上（高出门槛一线），俯望马群缓缓归来 */
  const poet=sscFigure(1.75,'独立');
  poet.position.set(-6.0,1.35,-3.6); poet.rotation.y=2.95; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.6,w:9,d:5,color:0x14100a,seed:22145,rim:0.12,rimC:0xc49a5a});
  rock.g.position.set(-7.2,-0.1,-3.0); g.add(rock.g);
  /* 雪后夜风轻流 + 雪尘微飘 */
  const wind=makeFlow({n:320,box:[96,9,40],pos:[0,2.6,-18],color:0x6e5e46,size:15,speed:4.0,maxA:0.11});
  g.add(wind.points);
  const snow=makeGlow({n:36,box:[110,12,44],pos:[0,6,-22],color:0xbfb298,size:2.2,speed:0.10,rise:-0.10,add:false,maxA:0.10});
  g.add(snow.points);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-54],scale:68,color:0x5a4c38,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[160,18,66],pos:[0,9,-34],color:0xc9b28a,size:4.2,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:22146,rim:0.10,rimC:0xc49a5a});
  fg1.g.position.set(-12,-1.8,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:22147,rim:0.10,rimC:0xc49a5a});
  fg2.g.position.set(13,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0xc0a878,i:0.40,p:[-48,58,-28]},{c:0x2e2618,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); grd.update();
    herd.userData.update(t);
    lou.userData.update(t,k); poet.update(t,k); rock.update(t,k);
    wind.update(t); snow.update(t); motes.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bDiman(){ // 贰（末境·可点击）· 笛满关山 —— 借问梅花何处落，风吹一夜满关山：点击笛声起，梅花漫卷关山
  const ctl={t:0,clicked:false,on:false,reveal:0,done:0};
  const g=new THREE.Group();
  const ridge=makeRange({r:310,h:15,layers:2,peaks:4,seed:22151,color:0x0c0805,atmo:0x2e2114,
    fogK:0.62,glowK:0.08,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-6,0,-116); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:250,h:20,layers:2,peaks:4,seed:22152,color:0x0a0603,atmo:0x2e2114,
    fogK:0.58,glowK:0.06,glow:0xd8a860,y:-9,order:-5});
  ridge2.g.position.set(26,0,-64); ridge2.g.rotation.y=Math.PI*0.9; g.add(ridge2.g);
  const grd=makeGround({r:230,c1:0x36322a,c2:0x544e3c,y:-1.7}); g.add(grd.mesh);
  /* 戍楼近景：吹笛人立于挑台（举杯姿态托笛于口边），楼身灯火微闪 */
  const lou=makeShuLou({seed:22153,rim:0.20});
  lou.position.set(-7,-1.7,-14); lou.scale.setScalar(1.1); g.add(lou);
  const guard=sscGuard(0.5);
  guard.position.set(0.05,4.4,-0.10); lou.add(guard);
  const di=makeQiangDi();
  di.position.set(0.06,3.42,0.40); di.rotation.y=0.22; di.rotation.z=0.05;
  guard.add(di);
  const deckY=-1.7+4.4*1.1;                       // 挑台世界高度 ≈3.14
  /* 笛纹音波环：自戍楼吹笛人口边荡开（点击后 amp 渐起、保持不歇——「一夜」笛声） */
  const diwen=makeDiWen({n:4,y:4.95,reach:44,speed:0.11,maxOp:0.30,color:0xc9a06a});
  diwen.position.set(-7,0,-14); g.add(diwen);
  /* 标志性瞬间：漫天梅花雪片（点击后 uMaxA 渐起；波前自左向右一阵一阵漫卷关山） */
  const hua=makeMeihua({n:320,box:[130,44,66],pos:[0,23,-26],speed:0.42,wind:1.35,maxA:0.001});
  g.add(hua.points);
  /* 夜风横流（点击后风势渐紧，托着梅花走） */
  const wind=makeFlow({n:380,box:[96,10,42],pos:[0,3.4,-18],color:0x6e5e46,size:16,speed:4.4,maxA:0.10});
  g.add(wind.points);
  /* 闻笛人（诗人）：前景右，背身 3/4 面向戍楼 */
  const poet=sscFigure(1.8,'独立');
  poet.position.set(3.6,-0.28,-5.4); poet.rotation.y=2.95; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:1.6,w:8,d:4,color:0x14100a,seed:22154,rim:0.12,rimC:0xc49a5a});
  rock.g.position.set(6.2,-1.45,-2.6); g.add(rock.g);
  /* 雪尘、夜霭、微尘 */
  const snow=makeGlow({n:30,box:[100,11,40],pos:[0,6,-20],color:0xbfb298,size:2.0,speed:0.10,rise:-0.10,add:false,maxA:0.09});
  g.add(snow.points);
  const mist=makeMist({n:7,spread:[220,14,78],pos:[0,4.5,-52],scale:70,color:0x5a4c38,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[160,16,66],pos:[0,8,-30],color:0xc9b28a,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:22155,rim:0.10,rimC:0xc49a5a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:22156,rim:0.10,rimC:0xc49a5a});
  fg2.g.position.set(12.5,-1.6,12); g.add(fg2.g);
  addLights(g,{c:0xc0a878,i:0.42,p:[-46,55,-22]},{c:0x322818,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on){
        ctl.reveal=Math.min(1,ctl.reveal+dt/1.7);
        if(ctl.reveal>=1)ctl.done+=dt;
      }
      const e0=ctl.reveal, e=e0*e0*(3-2*e0);
      /* 笛声不歇：音波环渐起后保持余响；花势随 reveal 涨满 */
      const amp=ctl.on?Math.max(e,0.62):0;
      diwen.update(t,k,amp);
      hua.mat.uniforms.uMaxA.value=k*(0.001+0.55*e);
      wind.mat.uniforms.uMaxA.value=k*(0.10+0.16*e);
      ridge.update(t,0); ridge2.update(t,0); grd.update();
      lou.userData.update(t,k); guard.update(t,k);
      hua.update(t); wind.update(t); snow.update(t);
      mist.update(t,k); motes.update(t);
      poet.update(t,k); rock.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.16);
        pluck(4,0.0,0.12); pluck(2,0.30,0.10); pluck(5,0.66,0.10); pluck(3,1.05,0.09); pluck(1,1.5,0.08);   // 笛声五声渐起
        const fl=$('#flash'); fl.textContent='借问梅花何处落 风吹一夜满关山';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0c0806),hor:C(0x2a1c10),bot:C(0x090604),fog:C(0x140d07),fd:0.0050,star:0.30,
  moon:new THREE.Vector3(-62,40,-190),ms:0.95,mph:0.06,mhaze:0.20,dirC:C(0xb8a078),dirI:0.36,
  dirP:new THREE.Vector3(-48,58,-28),ambC:C(0x2c2418),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,46],t:[0,9.5,38],lf:[1.5,8.5,-26],lt:[2.5,9,-36]},
  sky:()=>SK({fd:0.0046,star:0.34}) },
{ name:'雪净牧还',dwell:16,river:0.02,build:bXuehuan,
  cam:{f:[0,6.6,25],t:[2.2,6.9,16],lf:[-2,6.6,-15],lt:[-4,7.2,-28]},
  sky:()=>SK({fd:0.0052,star:0.42,ms:1.05,mph:0.05,mhaze:0.22,
    moon:new THREE.Vector3(-58,46,-185),dirC:C(0xc0a878),dirI:0.40,
    ambC:C(0x2e2618),ambI:0.58}) },
{ name:'笛满关山',dwell:19,river:0.02,build:bDiman,
  cam:{f:[1.6,5.2,13.5],t:[-2.4,5.0,6.5],lf:[0.4,5.1,-6],lt:[-1.6,5.6,-15]},
  sky:()=>SK({top:C(0x0d0a07),hor:C(0x2e2012),bot:C(0x0a0705),fog:C(0x161009),fd:0.0056,star:0.38,
    ms:1.0,mph:0.05,mhaze:0.20,moon:new THREE.Vector3(-64,46,-180),
    dirC:C(0xc0a878),dirI:0.42,dirP:new THREE.Vector3(-46,55,-22),
    ambC:C(0x322818),ambI:0.58}) },
];
"""
