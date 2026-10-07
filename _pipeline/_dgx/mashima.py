# -*- coding: utf-8 -*-
"""mashima.py —— 《马诗·其五》（唐·李贺，queue no.225，大漠金戈）生成配置
两境（N=queue stages 数）：沙雪月钩（大漠沙如雪·燕山月似钩——标志性瞬间：沙月如铁的清冷骏马图）、
踏清秋（何当金络脑·快走踏清秋——末境点击「点击踏清秋——骏马金络脑奋蹄驰过大漠」）。
大漠金戈全套色板：底色 #120d08、雾 #141014 系、文字 #f0e2cc，accent=#b8905f
（queue 分配强调色，沙金络色）只落在金络脑/金光/人物边缘光/秋草穗/UI 上，禁艳金。
全页冷色源是「沙月」：月光沙雪清辉（地面偏银灰）+ 弯月如钩（mph 0.62 蛾眉月）——
清冷沙月与暖金络脑对撞出「渴望」。
情绪推进线：境壹=蓄（沙月如铁，骏马空有骏骨、昂首望月）→ 境贰=发（何当金络脑，一朝戴金、快走踏清秋）。
标志性瞬间（境壹·mk moment）：沙月如铁的清冷骏马图——一匹骏马（非马群）昂首静立雪色大漠之上，
弯月如钩悬于燕山之巅。末境点击（queue interact）：点击踏清秋——金络脑金光乍现戴上马首，
骏马自静立换为铜奔马式飞驰之姿（前肢腾空、后肢后蹬），沿大漠加速驰过，蹄下沙雪扬起，
「何当金络脑 快走踏清秋」题字同现。
与已有边塞页（战阵/夜射/行军/听笛/白骨/大湖/牧马群）第一眼可区分：本页主角是**一匹骏马**
——没有战争也没有马群，只有沙、月、马与一副尚未戴上的金络脑，托物言志的独骑清影。
考点钉子：燕 yān（燕山）/ 络 luò（络脑）（第 3 题落点）；李贺「诗鬼」+《马诗》二十三首
托物言志（第 4 题）；「何当」的渴望与怀才不遇（第 5 题）。
tts 多音字：燕山→烟山（yān）、金络脑→金洛脑（luò）、何当→河当（dāng）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='mashima', title='马诗·其五', dyn='唐 · 李贺', brand_author='李 贺',
    gold_rgb='184,144,95',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b8905f; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(184,144,95,.3);
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
    tip='轻点画面 / 按空格 —— 金络脑光起，骏马踏清秋',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看骏马戴上金络脑，奋蹄驰过如雪大漠',
    cover_read='马诗·其五。唐，李贺。大漠沙如雪，燕山月似钩。何当金络脑，快走踏清秋。',
    cover_p1='两重意境，随诗句次第展开：大漠平沙在月光下泛起雪一样的清辉，燕山之上，一弯新月如吴钩斜挂；何时才能戴上黄金络脑，在清爽的秋天里痛快驰骋——沙月愈冷，热望愈炽。',
    cover_p2='边读诗，边走进李贺笔下的清冷大漠：句句写马，句句写人——那匹昂首月下、空有骏骨的马，正是诗人自己的影子；读懂「何当」二字里的渴望，就读懂了怀才不遇者的胸中丘壑。',
    end_h2='络脑 · 清秋', cn_word='贰',
    words_js="['再看一眼大漠骏马','初识李贺，尚需共读','渐入诗境，再诵几遍','沙月渐明，骏骨渐昂','已解金络脑之盼','快走踏清秋，志在千里']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'沙雪月钩', jing:'大漠平沙在月光下泛起雪一样的清辉，燕山之巅，一弯新月如吴钩斜挂 —— 沙月如铁的清冷骏马图。（大漠沙如雪 · 燕山月似钩 · 标志性瞬间：沙月如铁的清冷骏马图）',
  segs:[
   {c:'大漠沙如雪，', p:py('dà mò shā rú xuě')},
   {c:'燕山月似钩。', p:py('yān shān yuè sì gōu')}],
  read:'大漠沙如雪，燕山月似钩。',
  yisi:'广阔的大漠，平沙在月光下像铺了一层白雪；燕山之上，一弯新月高悬，好像一柄弯刀。——前句写「沙」：「如雪」并非真雪，是月色给连绵沙丘镀上的寒光，以雪写沙，清冷顿生；后句写「月」：「似钩」的钩是吴钩（弯刀），月弯如钩，既状月形，也暗藏兵气。沙白、月弯、山寒——十个字勾出一幅沙月如铁的清冷骏马图：这正是骏马该纵横的天地，马尚未驰，气已满纸。',
  zhu:[['马诗·其五','李贺《马诗二十三首》的第五首——组诗通篇借咏马、赞马、慨叹马，抒写诗人怀才不遇的愤懑与渴望建功立业的雄心；此首是其中最负盛名的一首'],['大漠沙如雪','月光洒在广阔的沙漠上，平沙泛白，像铺了一层雪——「如雪」是月下错觉：不是雪，是月色。一个「如」字把大漠的寒光与静穆一并写出'],['燕山','山名，在今河北北部一带，自古为边塞要地；一说指燕然山。燕，读 yān——「燕山」点出骏马所处的征战之地'],['月似钩','钩，古代的一种弯刀（吴钩）。一弯新月像弯刀一样挂在燕山之巅——既是月形之喻，又带出兵器般的寒意与征战之气，为下文「金络脑」的建功之盼埋下伏笔'],['沙月如铁','月下白沙如雪、弯月如钩，沙与月都是寒铁般的冷色——清冷到极处的天地，恰是骏马（千里马）最能施展其才的战场底色；境愈冷，愈衬出下文金络脑之志的热']] },
{ name:'踏清秋', jing:'什么时候才能戴上黄金装饰的马笼头，在清爽的秋天里纵蹄飞驰 —— 渴望被识、被用的千古一问。（何当 · 金络脑 · 快走 · 踏清秋 · 标志性瞬间 · 末境点击画面：骏马金络脑奋蹄驰过大漠）',
  segs:[
   {c:'何当金络脑，', p:py('hé dāng jīn luò nǎo')},
   {c:'快走踏清秋。', p:py('kuài zǒu tà qīng qiū')}],
  read:'何当金络脑，快走踏清秋。',
  yisi:'什么时候才能戴上黄金装饰的辔头，在清爽的秋日原野上痛快地驰骋？——「何当」（何时才能）是全诗的诗眼：一问之中满是热切的期盼；「金络脑」是贵重的马具，骏马盼的不是草料安逸，而是被识马者委以驰骋；「快走」二字写尽急于施展的急切；「踏清秋」清劲潇洒——天高气爽，正是万里扬蹄之时。前两句清冷蓄势，后两句热望奔发：马即诗人，诗人即马。',
  zhu:[['何当','何时才能——热切盼望之词，全诗的诗眼。骏马对络脑的渴望、诗人对被识用的渴望，都凝在这一问里；问得愈急，愈见其不被识用之久'],['金络脑','用黄金装饰的马笼头（络脑：马头上的辔具，络，读 luò）。贵重的马具象征马受重用——骏马配金络脑，喻贤才得居要职、被委以重任'],['快走','痛快地奔跑。「走」在古汉语中是「跑」——不是慢步，而是纵蹄飞驰；一个「快」字，把渴望一显身手的急切心情写尽'],['踏清秋','在清爽的秋日原野上纵横驰踏。清秋天高气爽，正是骏马施展之时——「踏」字雄健有力，蹄声、秋风、沙场如在耳目之间'],['托物言志','借咏马言志向——句句写马：沙雪月钩是马所处的天地，金络脑是马的渴望；实则句句写人：李贺七岁能诗而仕途偃蹇，以骏马自况，抒发怀才不遇、渴望被朝廷识用建功的强烈心愿']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「大漠沙如雪」的下一句是？', o:['燕山月似钩','何当金络脑','快走踏清秋'], a:0},
 {q:'「何当金络脑」的下一句是？', o:['燕山月似钩','快走踏清秋','大漠沙如雪'], a:1},
 {q:'「燕山月似钩」「何当金络脑」中，「燕」「络」的读音和意思都正确的一项是？', o:['燕读 yān，燕山是边塞山名；络读 luò，「络脑」是马头上的辔具——金络脑即黄金装饰的马笼头，象征马被重用','燕读 yàn，燕子的燕——燕山即燕子北归所聚之山；络读 lào——「络脑」是一种网罗飞鸟的器具','燕读 yīn，燕姓的燕——燕山因戍将姓燕而得名；络读 luō——络脑是剥除马毛的刀具'], a:0},
 {q:'关于作者李贺与《马诗》，下列说法正确的是？', o:['李贺是中唐诗人，诗风奇诡冷艳，人称「诗鬼」；《马诗》共二十三首，都是托物言志的咏马诗——借咏马写怀才不遇与建功之望，此为其五，也是最著名的一首','李贺是盛唐山水田园诗人，与王维、孟浩然并称；《马诗》是单纯的写景组诗，记录各地名马的形态毛色','李贺是晚唐边塞将领，《马诗》作于军旅之中，二十三首都是描写战马训练的纪实之作'], a:0},
 {q:'「何当金络脑，快走踏清秋。」对这两句主旨的理解，最恰当的一项是？', o:['写牧马人盼着给爱马添置一副漂亮的新笼头，好在秋游时牵出去炫耀','托物言志：「何当」（何时才能）是热切的期盼——骏马盼戴上金络脑、纵横驰骋，正是诗人才华盼被识用、渴望建功立业的自况；沙月之清冷与金络脑之热望相激，怀才不遇之慨与昂扬进取之志俱在其中','感叹秋高马肥正宜出征，劝朝廷趁着秋天草壮马肥赶快发兵作战'], a:1},
];
"""

SCENES_JS = """/* ================= 马诗·其五 · 两境场景（大漠金戈·清冷独骑：沙雪月钩、踏清秋） =================
   美术立意：大漠金戈色板写「沙月如铁→金络脑之志」——底色 #120d08、雾 #141014 系，
   accent=#b8905f（沙金络色）只落在金络脑/金光/人物边缘光/秋草穗/UI 上，禁艳金。
   全页冷色源是「沙月」：月光沙雪清辉（地面银灰）+ 弯月如钩（蛾眉月）——清冷沙月对撞暖金络脑。
   与已有边塞页第一眼可区分：不做战阵/夜射/行军/听笛/白骨/大湖/牧马群，
   主角是**一匹骏马**——沙、月、马与一副尚未戴上的金络脑，托物言志的独骑清影。
   境壹（标志性瞬间）：沙月如铁的清冷骏马图——骏马昂首静立雪色大漠，弯月如钩悬于燕山之巅。
   境贰（末境可点击）：点击踏清秋——金络脑金光乍现戴上马首，骏马自静立换为铜奔马式飞驰之姿，
   沿大漠加速驰过、蹄下沙雪扬起（点击踏清秋——骏马金络脑奋蹄驰过大漠）。 */

/* —— 骏马 makeJunma(o)：全诗唯一的主角——一匹骏马（赛道里唯一以单骑为主角的页面）。
   pose:'stand'（昂首静立望月）|'gallop'（铜奔马式飞驰：前肢腾空前伸、后肢后蹬、颈尾拉成一线）；
   bridle:true 时附「金络脑」（黄金马笼头：鼻环+额环+颊带+额饰额缨，返回 bridleMat 可控发光）。
   骊色深棕近剪影，冷月下以 accent 边缘光跳出；返回 {g,bridle,bridleMat} */
function makeJunma(o){
  o=o||{};
  const pose=o.pose||'stand';
  const coat=o.coat===undefined?0x2a2016:o.coat, dk=shadeColor(coat,0.62), lt=shadeColor(coat,1.30);
  const B=new GeoBag();
  const bd=new THREE.SphereGeometry(1.5,10,8); bd.scale(1.6,1.05,0.78); bd.translate(0,3.05,0); B.put(bd,coat);
  const ch=new THREE.SphereGeometry(1.0,8,7); ch.scale(0.85,1.0,0.80); ch.translate(1.55,2.94,0); B.put(ch,coat);
  const rp=new THREE.SphereGeometry(1.1,8,7); rp.scale(0.80,0.95,0.80); rp.translate(-1.9,3.0,0); B.put(rp,lt);
  const cloth=new THREE.SphereGeometry(1,8,6); cloth.scale(0.85,0.26,0.70); cloth.translate(0.35,3.98,0);
  B.put(cloth,0x4a241a);                                   // 鞍鞯深赭一点暖色锚
  function leg(x0,z,x1,y1){
    B.put(limbGeo([x0,2.7,z],[x1,y1,z],0.22,0.12,5),shadeColor(coat,0.9));
    const hf=new THREE.SphereGeometry(0.19,6,5); hf.scale(1.05,0.8,0.95); hf.translate(x1,y1-0.03,z);
    B.put(hf,dk);
  }
  let head;
  if(pose==='stand'){
    leg(1.6,0.40,1.68,0.18); leg(1.6,-0.40,1.64,0.18);
    leg(-1.75,0.44,-1.82,0.18); leg(-1.75,-0.44,-1.78,0.18);
    for(let s2=0;s2<2;s2++){                                // 肩甲/后髋体块：腿根不再纤细
      const sh=new THREE.SphereGeometry(0.48,7,6); sh.translate(1.6,2.8,(s2?0.38:-0.38)); B.put(sh,coat);
      const hc=new THREE.SphereGeometry(0.55,7,6); hc.translate(-1.75,2.85,(s2?0.42:-0.42)); B.put(hc,coat);
    }
    B.put(limbGeo([1.45,3.3,0],[2.75,4.75,0],0.82,0.46,6),coat);            // 颈：粗壮昂起望月
    const sk=new THREE.SphereGeometry(0.62,8,7); sk.scale(1.25,0.95,0.68); sk.rotateZ(-0.10);
    sk.translate(3.05,5.02,0); B.put(sk,coat);
    B.put(limbGeo([3.3,4.92,0],[4.3,4.68,0],0.34,0.19,6),dk);               // 颌鼻
    for(let e=0;e<2;e++){ const ear=new THREE.ConeGeometry(0.13,0.5,4);
      ear.translate(2.85,5.62,(e?0.18:-0.18)); B.put(ear,dk); }
    B.put(limbGeo([1.7,3.5,0],[2.9,5.1,0],0.10,0.06,5),dk);                 // 鬃脊
    for(let i=0;i<5;i++){ const tt=i/4; const m=new THREE.SphereGeometry(0.24-0.10*tt,7,6);
      m.translate(1.70+1.15*tt,3.55+1.50*tt,0); B.put(m,dk); }              // 鬃：颈脊圆珠一列（无尖刺）
    B.put(limbGeo([-2.75,3.45,0],[-3.5,1.5,0],0.30,0.10,5),dk);             // 尾：垂落
    const tp=new THREE.ConeGeometry(0.16,0.6,5); tp.rotateX(Math.PI); tp.translate(-3.6,1.15,0);
    B.put(tp,dk);
    head={c:[3.0,5.15],m:[3.8,4.85],f:[3.35,5.45]};
  }else{
    leg(1.55,0.38,3.7,0.65); leg(1.55,-0.38,3.55,0.60);                     // 前肢腾空前伸
    leg(-1.75,0.42,-4.05,0.90); leg(-1.75,-0.42,-3.90,0.85);                // 后肢后蹬
    for(let s2=0;s2<2;s2++){                                // 肩甲/后髋体块
      const sh=new THREE.SphereGeometry(0.48,7,6); sh.translate(1.6,2.8,(s2?0.38:-0.38)); B.put(sh,coat);
      const hc=new THREE.SphereGeometry(0.55,7,6); hc.translate(-1.75,2.85,(s2?0.42:-0.42)); B.put(hc,coat);
    }
    B.put(limbGeo([1.45,3.25,0],[3.15,4.1,0],0.82,0.50,6),coat);            // 颈：前引拉成一线
    const sk=new THREE.SphereGeometry(0.62,8,7); sk.scale(1.25,0.95,0.68); sk.rotateZ(-0.38);
    sk.translate(3.6,4.25,0); B.put(sk,coat);
    B.put(limbGeo([3.85,4.12,0],[4.8,3.9,0],0.34,0.19,6),dk);
    for(let e=0;e<2;e++){ const ear=new THREE.ConeGeometry(0.13,0.5,4);
      ear.translate(3.4,4.75,(e?0.18:-0.18)); B.put(ear,dk); }
    B.put(limbGeo([1.7,3.45,0],[3.3,4.35,0],0.10,0.06,5),dk);
    for(let i=0;i<5;i++){ const tt=i/4; const m=new THREE.SphereGeometry(0.24-0.10*tt,7,6);
      m.translate(1.70+1.55*tt,3.50+0.85*tt,0); B.put(m,dk); }
    B.put(limbGeo([-2.8,3.4,0],[-4.75,3.95,0],0.30,0.08,5),dk);             // 尾：水平后掠
    const tp=new THREE.ConeGeometry(0.15,0.55,5); tp.rotateZ(-1.35); tp.translate(-4.95,4.05,0);
    B.put(tp,dk);
    head={c:[3.55,4.35],m:[4.35,4.05],f:[3.9,4.62]};
  }
  let bridle=null, bridleMat=null;
  if(o.bridle){
    const B2=new GeoBag(), gold=0xb8905f, goldL=shadeColor(gold,1.45);
    const ring=new THREE.TorusGeometry(0.36,0.05,6,16); ring.rotateY(Math.PI/2); ring.scale(1,1.06,1);
    ring.translate(head.m[0]+0.14,head.m[1]+0.06,0); B2.put(ring,gold);           // 鼻环
    const band=new THREE.TorusGeometry(0.46,0.05,6,16); band.rotateY(Math.PI/2); band.rotateZ(0.18);
    band.translate(head.c[0]-0.02,head.c[1]+0.08,0); B2.put(band,gold);           // 额环
    for(let s2=0;s2<2;s2++){ const zz=s2?0.22:-0.22;
      B2.put(limbGeo([head.c[0]+0.14,head.c[1]+0.02,zz],[head.m[0]+0.12,head.m[1]+0.08,zz*0.6],0.045,0.045,4),
        shadeColor(gold,0.85)); }                                                 // 颊带
    const orn=new THREE.SphereGeometry(0.11,7,6); orn.translate(head.f[0],head.f[1],0);
    B2.put(orn,goldL);                                                            // 额饰
    for(let s2=0;s2<2;s2++){ const tl=new THREE.ConeGeometry(0.055,0.28,4); tl.rotateX(Math.PI);
      tl.translate(head.f[0]+0.02,head.f[1]-0.22,(s2?0.15:-0.15)); B2.put(tl,gold); }   // 额缨
    bridleMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:60,
      specular:0xe0c090,emissive:0xb8905f,emissiveIntensity:0});
    bridle=B2.mesh(rimHook(bridleMat,{c:0xb8905f,i:0.5,p:2.6}));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a7484,emissive:0x050404}),{c:0xb8905f,i:o.rim===undefined?0.16:o.rim,p:2.3})));
  if(bridle)g.add(bridle);
  g.scale.setScalar(o.scale===undefined?1.3:o.scale);
  return {g:g,bridle:bridle,bridleMat:bridleMat};
}

/* —— 沙丘 makeShaQiu(o)：扁半球缓丘组合（GeoBag 1 mesh）——「大漠沙如雪」的波浪地势 */
function makeShaQiu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22502:o.seed);
  const list=o.mounds||[];
  const B=new GeoBag();
  for(let i=0;i<list.length;i++){
    const m=list[i];
    const q=new THREE.SphereGeometry(1,14,10); q.scale(m[2],m[3],m[2]*0.72);
    q.translate(m[0],-m[3]*0.45,m[1]); B.put(q,shadeColor(0x4c4a58,0.86+0.30*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x3a3848,emissive:0x050508}),{c:0xb8905f,i:o.rim===undefined?0.07:o.rim,p:2.0})));
  return g;
}

/* —— 秋草 makeQiuCao(o)：枯黄草丛（细叶+穗，GeoBag 1 mesh），微风轻摆——「踏清秋」的秋意 */
function makeQiuCao(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22541:o.seed);
  const n=o.n===undefined?3:o.n, w=o.w===undefined?2.2:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*0.9;
    const nb=4+Math.floor(R()*3);
    for(let b=0;b<nb;b++){
      const h=0.5+0.7*R(), a=R()*6.283, lean=0.18+0.30*R();
      const tx=x+Math.cos(a)*lean, tz=z+Math.sin(a)*lean*0.55;
      B.put(limbGeo([x,0,z],[tx,h,tz],0.030,0.006,4),shadeColor(0x7a6640,0.75+0.5*R()));
      if(b===0){
        const sui=new THREE.ConeGeometry(0.055,0.30,4); sui.translate(tx,h+0.13,tz);
        B.put(sui,shadeColor(0x8a744c,0.9+0.3*R()));
      }
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a4030,emissive:0x040302}),{c:0xb8905f,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  const ph=R()*6.283;
  g.userData.update=function(t){ g.rotation.z=0.045*Math.sin(t*0.75+ph); };
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 望马人（诗人李贺）：全诗贯穿的同一造型（每次 build 新建材质） */
function lmFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x232028,belt:0x6a5434,skin:0xd9b189,collar:0x45403a,
    hair:0x171208,hat:'幞头',beard:true,rimC:0xb8905f,rim:0.42,noProp:true,scale:scale===undefined?1.6:scale});
}

function bCover(){ // 卷首 · 沙雪大漠远望：弯月如钩、燕山横黛、一匹骏马静立沙丘之上
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x31313b,c2:0x595965,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:20,layers:2,peaks:5,seed:22501,color:0x0b0910,atmo:0x2e2114,
    fogK:0.63,glowK:0.05,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-20,0,-98); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:235,h:12,layers:2,peaks:4,seed:22502,color:0x0a080c,atmo:0x2e2114,
    fogK:0.58,glowK:0.04,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(18,0,-58); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  const dunes=makeShaQiu({seed:22503,
    mounds:[[3,-22,8,1.5],[-12,-30,10,1.8],[14,-34,9,1.6],[-4,-44,12,2.1],[9,-12,5,0.9]]});
  g.add(dunes);
  const horse=makeJunma({pose:'stand',scale:0.95,rim:0.20});
  horse.g.position.set(3.0,-1.78,-21); horse.g.rotation.y=-2.4; g.add(horse.g);
  const shimmer=makeGlow({n:26,box:[110,12,44],pos:[0,5.5,-20],color:0xaeb6c8,size:2.0,speed:0.10,rise:-0.08,add:false,maxA:0.08});
  g.add(shimmer.points);
  const wind=makeFlow({n:300,box:[100,10,42],pos:[0,3.2,-20],color:0x55504a,size:15,speed:4.2,maxA:0.09});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[220,14,80],pos:[0,5,-54],scale:70,color:0x3a3444,op:0.10});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:5,color:0x14121a,seed:22504,rim:0.08,rimC:0xb8905f});
  fg1.g.position.set(-12,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',n:5,w:10,d:2.5,color:0x2a2012,seed:22505,sway:0.7,rim:0.07,rimC:0xb8905f,scale:0.8});
  fg2.g.position.set(12.5,-1.75,13); g.add(fg2.g);
  addLights(g,{c:0xaab8cc,i:0.34,p:[-46,58,-30]},{c:0x2a2622,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); grd.update();
    shimmer.update(t); wind.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bShaxue(){ // 壹（标志性瞬间）· 沙雪月钩 —— 大漠沙如雪，燕山月似钩：沙月如铁的清冷骏马图
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x323039,c2:0x5b5b68,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:24,layers:2,peaks:5,seed:22511,color:0x0b0910,atmo:0x2e2114,
    fogK:0.64,glowK:0.05,glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-24,0,-102); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:240,h:13,layers:2,peaks:4,seed:22512,color:0x0a080c,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(20,0,-58); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  const dunes=makeShaQiu({seed:22513,
    mounds:[[3.2,-20,7,1.2],[-11,-28,9,1.6],[13,-32,8,1.4],[-5,-42,11,1.9],[8,-10,4,0.7],[-14,-14,5,0.9]]});
  g.add(dunes);
  /* 骏马：昂首望月，静立如铸——空有骏骨，络脑未戴 */
  const horse=makeJunma({pose:'stand',scale:1.3,rim:0.22});
  horse.g.position.set(2.3,-1.78,-14); horse.g.rotation.y=-2.35; g.add(horse.g);
  const hl=new THREE.PointLight(0x9ab0c8,0.95,20); hl.position.set(0.2,3.6,-10.5); g.add(hl);
  /* 望马人：诗人立于沙地仰望沙月骏马（人小马大，马是主角） */
  const poet=lmFigure(1.55,'独立'); poet.position.set(-8.0,-1.78,-6.0); poet.rotation.y=2.2; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.0,w:7,d:4,color:0x14121a,seed:22514,rim:0.10,rimC:0xb8905f});
  rock.g.position.set(-9.4,-1.55,-8.2); g.add(rock.g);
  /* 清秋枯草 */
  const qc1=makeQiuCao({seed:22515,n:3}); qc1.position.set(-4,-1.58,-10.5); g.add(qc1);
  const qc2=makeQiuCao({seed:22516,n:4,w:2.8,scale:1.15}); qc2.position.set(7.5,-1.62,-16); g.add(qc2);
  const qc3=makeQiuCao({seed:22517,n:2}); qc3.position.set(-11,-1.6,-19); g.add(qc3);
  /* 月下浮尘如雪、沙风横流、清雾 */
  const shimmer=makeGlow({n:30,box:[100,12,42],pos:[0,5,-18],color:0xaeb6c8,size:2.0,speed:0.12,rise:-0.08,add:false,maxA:0.10});
  g.add(shimmer.points);
  const wind=makeFlow({n:320,box:[96,10,40],pos:[0,3.2,-18],color:0x55504a,size:15,speed:4.2,maxA:0.10});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-52],scale:68,color:0x3a3444,op:0.10});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x12101a,seed:22518,rim:0.09,rimC:0xb8905f});
  fg1.g.position.set(-12.5,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',n:5,w:10,d:2.5,color:0x2a2012,seed:22519,sway:0.7,rim:0.07,rimC:0xb8905f,scale:0.85});
  fg2.g.position.set(12,-1.78,12); g.add(fg2.g);
  addLights(g,{c:0xaab8cc,i:0.36,p:[-44,58,-28]},{c:0x2a2622,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); grd.update();
    poet.update(t,k); rock.update(t,k);
    qc1.userData.update(t); qc2.userData.update(t); qc3.userData.update(t);
    shimmer.update(t); wind.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bTaQingqiu(){ // 贰（末境·可点击）· 踏清秋 —— 何当金络脑，快走踏清秋：点击金络脑光起、骏马奋蹄驰过
  const ctl={t:0,clicked:false,on:false,reveal:0,flying:false,flash:0,dist:0,x0:0.8,y0:-1.78};
  const SPAN=80;
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x30303a,c2:0x585866,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:22,layers:2,peaks:5,seed:22531,color:0x0b0910,atmo:0x2e2114,
    fogK:0.62,glowK:0.08,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-16,0,-112); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:240,h:14,layers:2,peaks:4,seed:22532,color:0x0a080c,atmo:0x2e2114,
    fogK:0.58,glowK:0.06,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(22,0,-62); ridge2.g.rotation.y=Math.PI*0.9; g.add(ridge2.g);
  const dunes=makeShaQiu({seed:22533,
    mounds:[[-12,-24,9,1.6],[16,-30,10,1.8],[-4,-40,12,2.0],[24,-18,6,1.0],[-20,-14,6,1.0]]});
  g.add(dunes);
  /* 骏马：静立（金络脑未戴——「何当」之盼）；点击后换铜奔马式飞驰之姿沿大漠驰过 */
  const anchor=new THREE.Group(); anchor.position.set(ctl.x0,ctl.y0,-11); anchor.rotation.y=-2.2;
  g.add(anchor);
  const stand=makeJunma({pose:'stand',scale:1.35,bridle:true,rim:0.22});
  stand.bridle.visible=false;                        // 点击前硬关：无络脑（金光也不可见）
  const gallop=makeJunma({pose:'gallop',scale:1.35,bridle:true,rim:0.26});
  gallop.g.visible=false; gallop.bridle.visible=false;
  anchor.add(stand.g); anchor.add(gallop.g);
  /* 戴上金络脑的一瞬：金光一闪 + 马首金色光晕 + 金色点光（初值=最大，逐帧乘 fadeK） */
  const burst=makeBurst({n:36,color:0xe8cc90,pos:[3.4,5.4,0]});
  stand.g.add(burst.points);
  const gleamMat=new THREE.SpriteMaterial({map:glowTex(),color:0xeccf96,transparent:true,opacity:0.55,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const gl1=new THREE.Sprite(gleamMat); gl1.scale.set(3.4,3.4,1); gl1.position.set(3.4,5.4,0.2);
  gl1.renderOrder=4; gl1.visible=false; stand.g.add(gl1);
  const gl2=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xeccf96,transparent:true,
    opacity:0.40,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  gl2.scale.set(2.6,2.6,1); gl2.position.set(3.95,4.6,0.2); gl2.renderOrder=4; gl2.visible=false;
  gallop.g.add(gl2);
  const kl=new THREE.PointLight(0xd8a860,1.0,24); kl.position.set(4.6,6.4,0); anchor.add(kl);
  /* 蹄下沙雪扬起：粒子云随马（anchor 局部，maxA 点击后渐起） */
  const dust=makeGlow({n:44,box:[5.5,2.8,2.6],pos:[-3.8,1.0,0],color:0xd0d4de,size:2.6,speed:1.0,rise:0.5,add:false,maxA:0.001});
  anchor.add(dust.points);
  /* 望马人：前景右独立凝望（识马者与骏马惺惺相惜） */
  const poet=lmFigure(1.5,'独立'); poet.position.set(6.6,-1.78,-4.4); poet.rotation.y=2.9; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.1,w:8,d:4,color:0x12101a,seed:22534,rim:0.11,rimC:0xb8905f});
  rock.g.position.set(7.8,-1.55,-6.6); g.add(rock.g);
  /* 远处行旅一列：大漠地平线上的剪影（远景人影，一层纵深） */
  const crowd=makeCrowd({n:5,rect:[-46,-56,84,8],seed:22535,color:0x171219,rimC:0xb8905f,rim:0.10,
    sMin:0.42,sMax:0.55,y:-0.5});
  g.add(crowd.mesh);
  /* 清秋枯草 */
  const qc1=makeQiuCao({seed:22536,n:3}); qc1.position.set(-5.5,-1.58,-8.5); g.add(qc1);
  const qc2=makeQiuCao({seed:22537,n:4,w:2.8,scale:1.1}); qc2.position.set(9.5,-1.62,-14); g.add(qc2);
  const qc3=makeQiuCao({seed:22538,n:2}); qc3.position.set(-12,-1.6,-20); g.add(qc3);
  const shimmer=makeGlow({n:28,box:[100,12,42],pos:[0,5,-18],color:0xaeb6c8,size:2.0,speed:0.12,rise:-0.08,add:false,maxA:0.09});
  g.add(shimmer.points);
  const wind=makeFlow({n:340,box:[96,10,40],pos:[0,3.4,-18],color:0x55504a,size:16,speed:4.4,maxA:0.10});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-54],scale:68,color:0x3a3444,op:0.10});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.5,w:11,d:5,color:0x12101a,seed:22539,rim:0.09,rimC:0xb8905f});
  fg1.g.position.set(-12,-1.8,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',n:5,w:10,d:2.5,color:0x2a2012,seed:22540,sway:0.7,rim:0.07,rimC:0xb8905f,scale:0.85});
  fg2.g.position.set(12.5,-1.78,12); g.add(fg2.g);
  addLights(g,{c:0xaab8cc,i:0.38,p:[-42,60,-26]},{c:0x2c2622,i:0.56});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on){
        ctl.reveal=Math.min(1,ctl.reveal+dt/2.4);
        if(ctl.reveal>0.42&&!ctl.flying){                 // 戴络脑毕：静立换飞驰，纵蹄起
          ctl.flying=true; ctl.flash=0;
          stand.g.visible=false; gallop.g.visible=true;
          gallop.bridle.visible=true; gl2.visible=true;
          burst.fire();
        }
      }
      const e0=Math.max(0,Math.min(1,ctl.reveal/0.42));   // 戴络脑：金光渐显
      const eb=e0*e0*(3-2*e0);
      const f0=Math.max(0,Math.min(1,(ctl.reveal-0.42)/0.58));   // 起驰：加速
      const ef=f0*f0*(3-2*f0);
      if(ctl.flying)ctl.flash+=dt;
      const fk=ctl.flying?Math.exp(-ctl.flash*2.2):0;     // 戴上一瞬的金光包络
      stand.bridleMat.emissiveIntensity=k*(0.95*eb+0.9*fk);
      gallop.bridleMat.emissiveIntensity=k*(0.95*eb+0.9*fk);
      gleamMat.opacity=k*0.55*(eb+0.8*fk);
      gl2.material.opacity=k*0.40*ef*(0.8+0.2*Math.sin(t*9.1));
      kl.intensity=k*1.0*(0.10+0.55*eb+0.35*fk);
      if(ctl.on&&!ctl.flying)stand.g.position.y=0.05*Math.sin(t*1.4);   // 静立呼吸起伏
      if(ctl.flying){                                     // 奔驰：转向→加速→wrap 环驰→蹄下沙雪
        ctl.dist+=dt*(2.0+7.5*ef);
        let x=ctl.x0+ctl.dist;
        x=((x+SPAN*0.5)%SPAN+SPAN)%SPAN-SPAN*0.5;
        anchor.position.x=x;
        anchor.position.y=ctl.y0+0.32*Math.abs(Math.sin(ctl.dist*0.8))*ef;
        anchor.rotation.y=-2.2+2.05*ef;
        dust.mat.uniforms.uMaxA.value=k*(0.001+0.50*ef);
      }
      ridge.update(t,0); ridge2.update(t,0); grd.update();
      crowd.update(t);
      poet.update(t,k); rock.update(t,k);
      qc1.userData.update(t); qc2.userData.update(t); qc3.userData.update(t);
      burst.update(t); shimmer.update(t); wind.update(t); mist.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        stand.bridle.visible=true; gl1.visible=true;      // 金络脑戴上（此前硬关无幻影）
        setAmbience(0.22);                                // 清秋风声
        pluck(7,0.0,0.12); pluck(4,0.28,0.10); pluck(5,0.62,0.10); pluck(2,1.0,0.09);   // 金络脑光起·奋蹄四声
        const fl=$('#flash'); fl.textContent='何当金络脑 快走踏清秋';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0a0d16),hor:C(0x2a1e12),bot:C(0x090a10),fog:C(0x141014),fd:0.0052,star:0.42,
  moon:new THREE.Vector3(-46,56,-168),ms:1.15,mph:0.74,mhaze:0.14,dirC:C(0xaab4c8),dirI:0.34,
  dirP:new THREE.Vector3(-42,58,-28),ambC:C(0x2a2420),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,42],t:[0,8.5,34],lf:[1.5,8,-24],lt:[-2,8.5,-36]},
  sky:()=>SK({fd:0.0048,star:0.36,ms:1.05}) },
{ name:'沙雪月钩',dwell:16,river:0.02,build:bShaxue,
  cam:{f:[0,6.2,24],t:[0.6,6.4,15],lf:[0.5,5.8,-10],lt:[-1.5,6.6,-24]},
  sky:()=>SK({fd:0.0052,star:0.44,ms:1.38,mhaze:0.16,
    moon:new THREE.Vector3(-50,60,-172),dirI:0.36,dirP:new THREE.Vector3(-44,60,-28),
    ambC:C(0x2a2622),ambI:0.56}) },
{ name:'踏清秋',dwell:19,river:0.02,build:bTaQingqiu,
  cam:{f:[0.6,5.2,16.5],t:[0.8,5.0,8.0],lf:[0.8,5.0,-7],lt:[2.6,5.4,-15]},
  sky:()=>SK({fd:0.0056,star:0.55,ms:1.22,hor:C(0x302014),
    moon:new THREE.Vector3(-42,64,-178),dirI:0.38,dirP:new THREE.Vector3(-40,62,-26),
    ambC:C(0x2c2622),ambI:0.56}) },
];
"""
