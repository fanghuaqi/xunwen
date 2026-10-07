# -*- coding: utf-8 -*-
"""shiwucongjun.py —— 《十五从军征》（汉乐府，queue no.258，宣纸留白·荒村暮归变体）生成配置
4 境（[2,2,2,2] 分境）：
境壹从军始归（十五从军征·八十始得归·道逢问家——乡道暮色，拄杖归人与指路乡人）、
境贰松柏累累（标志性瞬间：松柏冢累累——乡人所指的「君家」是松柏成林下的累累坟冢；
兔从狗窦入、雉从梁上飞，荒宅兔雉穿行）、
境叁旅谷旅葵（中庭生旅谷、井上生旅葵——破败庭院里野谷自生野葵自长，舂谷持作饭）、
境肆羹饭贻谁（末境可点击：点击羹饭一时熟——热气升腾无人共食，案对面蒲团空席虚位，
暮色转冷青灰暮流，泪光一点——出门东向看，泪落沾我衣）。
美术立意「暮年归乡·家已成冢」：宣纸上一次极克制的荒凉——浅纸为天、浓墨作剪影、大量留白，
一条乡道贯穿（卷首远望→境壹道逢→境贰望家→境叁庭中→境肆檐下）。
教学对象中学生：荒冢意象克制写意——松柏环冢、土馒头坟形、兔雉惊走剪影，不画碑石骨骸。
与已有宣纸留白页第一眼可区分：终南望余雪=雪线山体+城头望雪（雪景城郭），
本页=荒村坟园+破败庭院（松柏冢、断墙狗窦、兔雉、旅谷旅葵、饭案空席），无雪无城郭。
自建 builder：makeSongbaiSW（松柏二态）/ makeZhongSW（坟冢）/ makeCanQiangSW（残墙断壁+狗窦+断梁）/
makeJingSW（井台井栏）/ makeJiuSW（石臼+杵）/ makeLvguSW（旅谷丛）/ makeLvkuiSW（旅葵丛）/
makeTuSW（兔·惊走）/ makeZhiSW（雉·梁上飞）/ makeLaobingSW（老兵拄杖·白发佝偻）/
makeXiangrenSW（指路乡人）/ makeKuShuSW（枯树）/ makeWusheSW（远处屋舍剪影）/
makePutuanSW（蒲团）/ makeDanriSW（纸色淡日）/ makeDaoSW（乡道）。
考点钉子：冢 zhǒng／雉 zhì／羹 gēng／贻 yí／舂 chōng／窦 dòu／累累 léi léi（小测第 3 题）；
汉乐府叙事诗与兵役之苦（第 4 题）；「羹饭一时熟不知贻阿谁」的细节与控诉（第 5 题）。
多音字：冢累累 léi léi、窦 dòu、舂 chōng、雉 zhì、羹 gēng、贻 yí、熟 shú（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='shiwucongjun', title='十五从军征', dyn='汉 · 乐府', brand_author='汉 乐 府',
    gold_rgb='74,80,96',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#4a5060; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(74,80,96,.28);
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
    tip='轻点画面 / 按空格 —— 羹饭一时熟，热气升腾无人共食',
    hint='← → 键或空格逐境游览 · 末境可点击画面：热气升腾，空席虚位，不知贻阿谁',
    cover_read='十五从军征。汉，乐府。十五从军征，八十始得归。道逢乡里人，家中有阿谁？遥看是君家，松柏冢累累。兔从狗窦入，雉从梁上飞。中庭生旅谷，井上生旅葵。舂谷持作饭，采葵持作羹。羹饭一时熟，不知贻阿谁。出门东向看，泪落沾我衣。',
    cover_p1='四重意境，随诗句次第展开：十五岁从军出征，八十岁才得以还乡，路上向乡人打听——家里还有谁在？遥遥望见的「家」，已是松柏成林、坟冢相连；野兔从狗洞钻进，野鸡从梁上惊飞；庭院里野谷自生，井台上野葵自长。舂谷做饭，采葵做羹——羹饭一时熟了，却不知道该送给谁。',
    cover_p2='边读诗，边跟着这位八十岁的老兵走一趟回家的路：家还在原处，家已经没有了。末境轻点画面，看饭菜热气升起，空席虚位，无人共食——「出门东向看，泪落沾我衣」。',
    end_h2='泪落 · 沾衣', cn_word='四',
    words_js="['再随老兵归一次乡','初识汉乐府，尚需共读','渐入诗境，再诵几遍','松柏在望，悲意渐深','已解舂谷采葵之苦','泪落沾衣，千古同悲']",
    sky_atmo='0xd8d5c9',
)

POEM_JS = """const POEM = [
{ name:'从军始归', jing:'十五岁就随军出征，八十岁才得以还乡。半路上遇到乡里人，急急地问一句：我家中还有谁在？（归途 · 拄杖白发 · 乡音相问）',
  segs:[
   {c:'十五从军征，', p:py('shí wǔ cóng jūn zhēng')},
   {c:'八十始得归。', p:py('bā shí shǐ dé guī')},
   {c:'道逢乡里人，', p:py('dào féng xiāng lǐ rén')},
   {c:'家中有阿谁？', p:py('jiā zhōng yǒu ā shuí')}],
  read:'十五从军征，八十始得归。道逢乡里人，家中有阿谁？',
  yisi:'十五岁就随军出征，到了八十岁才得以回乡。半路上遇到乡里的人，问一声：我家中还有谁在？——起笔两句像一份兵役档案：「十五」「八十」两个数字对举，中间六十五年的岁月全部压进一个「始」字里：才、方才。没有一句写军旅之苦，苦尽在不言中。归人进乡问的第一件事不是吃饭安身，而是家人的存亡——「家中有阿谁」，问得越急切，越见六十五年里刻骨的牵挂，也埋下全诗最不忍读的答案。',
  zhu:[['始得归','才得以回乡。始，才——「十五」与「八十」对举，六十五年戍涯全在这个「始」字的迟与难里'],['征','从军出征、服兵役'],['道逢','在路上遇到'],['阿谁','谁。「阿」是口语词头，无实义；一句乡音的「阿谁」，是近乡情怯的惶惑与指望']] },
{ name:'松柏累累', jing:'远远望去，乡人指处那座「君家」，已是松柏成林、坟冢累累相连。野兔从墙脚的狗洞钻进屋里，野鸡从房梁上扑翅惊飞。（望家 · 荒冢松柏 · 兔雉穿行）（标志性瞬间：松柏冢累累——遥看是君家）',
  segs:[
   {c:'遥看是君家，', p:py('yáo kàn shì jūn jiā')},
   {c:'松柏冢累累。', p:py('sōng bǎi zhǒng léi léi')},
   {c:'兔从狗窦入，', p:py('tù cóng gǒu dòu rù')},
   {c:'雉从梁上飞。', p:py('zhì cóng liáng shàng fēi')}],
  read:'遥看是君家，松柏冢累累。兔从狗窦入，雉从梁上飞。',
  yisi:'远远望去，那里就是你家——松柏树下，坟冢连绵成片。野兔从墙脚的狗洞里钻进屋去，野鸡从房梁上扑翅惊飞。——乡人的回答不是一句话，而是一指：你家的「人」都已埋在松柏之下，坟头一个连着一个。荒宅成了兔雉的天下：野物敢从狗洞进出、敢在梁上栖身，正见屋残墙颓、久无人居。以景代答、以物写人，一个「悲」字不说，荒凉与死灭已扑面而来——这是全诗最惊心的一境。',
  zhu:[['遥看','远远地望——乡人所指的，正是「家」之所在'],['松柏冢累累','松柏树下坟冢连绵成片。冢，高起的坟墓，读 zhǒng；累累，连缀成串、接连不断的样子，这里形容坟冢一个连着一个，读 léi léi——汉人墓地多植松柏，松柏成林，即见家中之人长眠已久'],['狗窦','墙脚给狗进出的洞。窦，孔穴、洞，读 dòu'],['雉','野鸡，读 zhì'],['梁上飞','从房梁上惊飞而起——屋顶残破、堂上无人，野禽才得以栖梁安家']] },
{ name:'旅谷旅葵', jing:'庭院当中长出了野生的谷子，井台边长出了野生的葵菜。舂掉谷壳拿来做饭，采下葵叶拿来煮羹。（荒园自生 · 舂谷采葵 · 亲手做一顿没人等的饭）',
  segs:[
   {c:'中庭生旅谷，', p:py('zhōng tíng shēng lǚ gǔ')},
   {c:'井上生旅葵。', p:py('jǐng shàng shēng lǚ kuí')},
   {c:'舂谷持作饭，', p:py('chōng gǔ chí zuò fàn')},
   {c:'采葵持作羹。', p:py('cǎi kuí chí zuò gēng')}],
  read:'中庭生旅谷，井上生旅葵。舂谷持作饭，采葵持作羹。',
  yisi:'庭院当中长出了野生的谷子，井台边长出了野生的葵菜。舂掉谷壳拿来做饭，采下葵叶拿来煮羹。——家园无主，谷物与葵菜便自生自长，喧宾夺主地住进了院子。老兵认认真真地舂谷、采葵、做饭、煮羹：这是一生颠沛之后最寻常不过的「过日子」的动作，然而愈是认真，愈见荒凉——这顿饭，从一开始就注定没有人来吃。动作写得越实，心里的空落写得越虚，为末境「不知贻阿谁」蓄足了力。',
  zhu:[['中庭','庭院当中'],['旅谷','野生的谷子。旅，不经播种而野生'],['旅葵','野生的葵菜。葵，冬苋菜一类，古人的常食之蔬'],['舂谷','把谷子放在石臼里捣去外壳。舂，捣米，读 chōng'],['持作饭','拿来做饭。持，拿、取'],['羹','用菜和肉（或菜和米）煮成的带汤汁的食，读 gēng']] },
{ name:'羹饭贻谁', jing:'羹和饭一会儿就熟了，却不知道送给谁吃。走出大门向东张望，眼泪落下来，沾湿了衣裳。（热气升腾 · 空席虚位 · 泪落沾衣）（末境点击画面：点击羹饭——热气升腾，空席无人共食）',
  segs:[
   {c:'羹饭一时熟，', p:py('gēng fàn yī shí shú')},
   {c:'不知贻阿谁。', p:py('bù zhī yí ā shuí')},
   {c:'出门东向看，', p:py('chū mén dōng xiàng kàn')},
   {c:'泪落沾我衣。', p:py('lèi luò zhān wǒ yī')}],
  read:'羹饭一时熟，不知贻阿谁。出门东向看，泪落沾我衣。',
  yisi:'羹和饭一会儿就煮熟了，却不知道送给谁吃。走出大门向着东方张望，眼泪落下来，沾湿了衣裳。——「不知贻阿谁」与境壹「家中有阿谁」遥遥相对：出门时问「还有谁」，归来后答「没有谁」。热气腾起的饭菜本是人间最暖的东西，在这里却成了最冷的一问。老兵无处安放这顿饭，只能出门东望——望什么呢？什么也没有。全诗不着一字议论，只把舂谷、采葵、做饭、东望、落泪一连串动作摆在这里，兵役之苦、家破人亡之痛尽在无言，这正是乐府「感于哀乐，缘事而发」的力量。',
  zhu:[['一时熟','一会儿就煮熟了。一时，顷刻、一会儿'],['贻','送给、赠给，读 yí'],['出门东向看','走出大门向着东方张望——东向而望，望而无所得，是极度悲怆后的茫然'],['泪落沾我衣','眼泪落下沾湿了衣裳——全诗唯一的收束，仍是一个动作细节；以「泪」字收尽全篇，控诉尽在不言中'],['乐府','本是汉代掌管音乐的官署，负责采集民歌配乐演唱，后遂称这类民歌及文人拟作为「乐府」——《十五从军征》即汉乐府叙事诗的代表']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「十五从军征，八十始得归。」的下一句是？', o:['道逢乡里人，家中有阿谁？','遥看是君家，松柏冢累累。','中庭生旅谷，井上生旅葵。'], a:0},
 {q:'「兔从狗窦入，雉从梁上飞。」的下一句是？', o:['出门东向看，泪落沾我衣。','羹饭一时熟，不知贻阿谁。','中庭生旅谷，井上生旅葵。'], a:2},
 {q:'下列加点字的读音和解释，全都正确的一项是？', o:['「冢」读 zhǒng，坟墓；「雉」读 zhì，野鸡；「舂」读 chōng，把谷捣去外壳','「冢」读 zhōng，家中；「雉」读 lí，篱笆；「舂」读 chūn，春季','「冢」读 chóng，重复；「雉」读 zhī，支撑；「舂」读 chǒng，宠爱'], a:0},
 {q:'关于《十五从军征》的体裁与主旨，理解正确的一项是？', o:['唐代格律诗——讲究平仄对仗，主要赞美老兵归乡后躬耕自食的田园之乐','宋人词作——长短句交错，重点写归乡路途的艰险遥远','汉乐府叙事诗——乐府本是汉代采集民歌配乐演唱的官署，后成为诗体名；此诗以老兵六十五年服役、归家而家已成冢的遭遇，控诉兵役制度给百姓带来的深重苦难'], a:2},
 {q:'对「羹饭一时熟，不知贻阿谁。出门东向看，泪落沾我衣」的理解，最恰当的一项是？', o:['饭菜做熟了却无人可送，只能出门东望、泪落沾衣——以做饭、张望、落泪这些最平常的动作细节，把家破人亡的巨大悲恸写得不动声色，不着一字控诉而控诉自见','老兵嫌饭菜做得太慢，一气之下摔门而出，泪落沾衣是委屈的表现','这是写老兵请邻人吃饭，邻人失约未至，老兵伤心落泪'], a:0},
];
"""

SCENES_JS = """/* ================= 十五从军征 · 四境场景（宣纸留白·荒村暮归：从军始归、松柏累累、旅谷旅葵、羹饭贻谁） =================
   美术立意：「暮年归乡·家已成冢」——宣纸上一次极克制的荒凉：浅纸为天、浓墨作剪影、大量留白，
   一条乡道贯穿（卷首远望→境壹道逢→境贰望家→境叁庭中→境肆檐下）。
   与已有宣纸留白页第一眼可区分：终南望余雪=雪线山体+城头望雪（雪景城郭），
   本页=荒村坟园+破败庭院（松柏冢、断墙狗窦、兔雉、旅谷旅葵、饭案空席），无雪无城郭。
   荒冢意象克制写意：松柏环冢、土馒头坟形、兔雉惊走剪影——不画碑石，不画骨骸。
   标志性瞬间（境贰）：松柏冢累累——乡人所指的「君家」是松柏成林下的累累坟冢，兔从狗窦入、雉从梁上飞。
   末境点击：点击羹饭一时熟——热气升腾、暮色由暖转冷、青灰暮流漫院、泪光一点，案对面蒲团空席虚位。
   accent=#4a5060（青灰）只落在：老兵袍色/衣领、UI、末境暮流与泪光上，全页近零饱和。
   布局纪律：主体场景群放 z −11…−75（骨架常驻远山环 z≈−260…−330 之前）；自建低平远山环在 z≈−120。 */

/* —— 乡道 makeDaoSW(o)：浅色土路（微弯长条板，颜色略亮于地面），归途的视觉引导 —— */
function makeDaoSW(o){
  o=o||{};
  const w=o.w===undefined?3.4:o.w, L=o.L===undefined?46:o.L, rot=o.rot===undefined?0.10:o.rot;
  const g=new THREE.Group();
  const m=new THREE.Mesh(new THREE.BoxGeometry(w,0.06,L),
    new THREE.MeshPhongMaterial({color:o.c===undefined?0xd8d0b6:o.c,shininess:4,specular:0x55503e}));
  m.rotation.y=rot; m.position.y=o.y===undefined?-1.86:o.y; g.add(m);
  return g;
}

/* —— 松柏 makeSongbaiSW(o)：kind:'song' 松（伞状层叠冠）/ 'bai' 柏（紧抱塔形冠），浓墨剪影，合批 1 mesh ——
   冢旁树形瘦直，风过微摆——「松柏冢累累」的环冢林 */
function makeSongbaiSW(o){
  o=o||{};
  const kind=o.kind===undefined?'song':o.kind, R=seedRnd(o.seed===undefined?25801:o.seed);
  const h=o.h===undefined?7:o.h, B=new GeoBag();
  const inkC=o.color===undefined?0x242a25:o.color;
  const tr=new THREE.CylinderGeometry(0.09,0.16,h*0.42,6);
  tr.translate(0,h*0.21,0); B.put(tr,0x1e2124);
  if(kind==='song'){
    const layers=4;
    for(let i=0;i<layers;i++){
      const t=i/(layers-1);
      const rr=h*0.30*(1-0.62*t), hh=h*0.14*(1-0.30*t);
      const c=new THREE.ConeGeometry(rr,hh,9);
      c.scale(1.25,1,1); c.translate((R()-0.5)*0.2,h*0.30+t*h*0.20,0);
      B.put(c,shadeColor(inkC,0.85+0.30*R()));
    }
  }else{
    const layers=5;
    for(let i=0;i<layers;i++){
      const t=i/(layers-1);
      const rr=h*0.16*(1-0.72*t), hh=h*0.16;
      const c=new THREE.ConeGeometry(rr,hh,8);
      c.translate((R()-0.5)*0.10,h*0.26+t*h*0.17,0);
      B.put(c,shadeColor(inkC,0.82+0.34*R()));
    }
  }
  const sh=new THREE.CircleGeometry(h*0.10,10); sh.rotateX(-Math.PI/2);
  sh.scale(1.5,1,1.2); sh.translate(0,0.045,0); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3230,emissive:0x050706}),{c:o.rimC===undefined?0xd8d6c6:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.006*Math.sin(t*0.5+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 坟冢 makeZhongSW(o)：土馒头坟形 n 座（压扁半球+顶部微隆），克制写意，合批 1 mesh ——
   只有土丘与地面阴影，无碑无骨骸——「冢累累」的含蓄画法 */
function makeZhongSW(o){
  o=o||{};
  const n=o.n===undefined?3:o.n, r=o.r===undefined?2.4:o.r;
  const R=seedRnd(o.seed===undefined?25802:o.seed);
  const w=o.w===undefined?r*3.4:o.w, B=new GeoBag();
  for(let i=0;i<n;i++){
    const rr=r*(0.62+0.42*R());
    const x=-w/2+(i+0.5)*(w/n)+(R()-0.5)*w*0.16, z=(R()-0.5)*w*0.30;
    const dome=new THREE.SphereGeometry(rr,12,8,0,Math.PI*2,0,Math.PI/2);
    dome.scale(1,0.42,0.92); dome.translate(x,0,z);
    B.put(dome,shadeColor(o.color===undefined?0x3e4440:o.color,0.85+0.30*R()));
    const top=new THREE.SphereGeometry(rr*0.42,8,6,0,Math.PI*2,0,Math.PI/2);
    top.scale(1,0.30,1); top.translate(x,rr*0.40,z);
    B.put(top,shadeColor(o.color===undefined?0x3e4440:o.color,0.72+0.18*R()));
    const sh=new THREE.CircleGeometry(rr*1.35,12); sh.rotateX(-Math.PI/2);
    sh.scale(1.25,1,1); sh.translate(x,0.04,z+rr*0.06);
    B.put(sh,0x0a0c0e);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a302c,emissive:0x040605}),{c:o.rimC===undefined?0xd0cec0:o.rimC,i:o.rim===undefined?0.08:o.rim,p:1.8})));
  return g;
}

/* —— 枯树 makeKuShuSW(o)：荒村枯树（分段弯干+光秃枝桠，无叶），合批 1 mesh —— */
function makeKuShuSW(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25803:o.seed);
  const h=o.h===undefined?5.4:o.h, B=new GeoBag();
  let px=0,py=0,pz=0,pr=0.20;
  const lean=(R()-0.5)*1.1;
  for(let k=0;k<4;k++){
    const nx=lean*(k+1)/4*(0.8+0.5*R()), ny=h*(k+1)/4, nz=(R()-0.5)*0.5*(k+1)/4;
    B.put(limbGeo([px,py,pz],[nx,ny,nz],pr,pr*0.72,5),shadeColor(0x23262a,0.85+0.35*R()));
    px=nx; py=ny; pz=nz; pr*=0.72;
    if(k>=1){
      const nb=2+((R()*2)|0);
      for(let b=0;b<nb;b++){
        const a=R()*6.283, len=h*(0.16+0.24*R());
        B.put(limbGeo([px,py,pz],[px+Math.cos(a)*len,py+len*(0.5+0.5*R()),pz+Math.sin(a)*len*0.6],
          pr,pr*0.4,4),shadeColor(0x23262a,0.8+0.4*R()));
      }
    }
  }
  const sh=new THREE.CircleGeometry(h*0.14,10); sh.rotateX(-Math.PI/2);
  sh.scale(1.4,1,1.1); sh.translate(0,0.045,0); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a2c30,emissive:0x040506}),{c:o.rimC===undefined?0xd6d4c4:o.rimC,i:o.rim===undefined?0.09:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.010*Math.sin(t*0.62+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 残墙 makeCanQiangSW(o)：断墙残壁（分段塌墙+豁口，可选狗窦洞、断梁、塌顶），合批 1 mesh ——
   「兔从狗窦入」的狗窦=墙脚半圆黑洞（Basic 近墨色）；「雉从梁上飞」的梁=斜倚断梁 */
function makeCanQiangSW(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25804:o.seed);
  const w=o.w===undefined?9:o.w, h=o.h===undefined?2.4:o.h, d=o.d===undefined?0.45:o.d;
  const segs=o.segs===undefined?3:o.segs, B=new GeoBag();
  let x=-w/2;
  for(let i=0;i<segs;i++){
    const sw=w/segs*(0.62+0.5*R()), hh=h*(0.32+0.68*R());
    const b=new THREE.BoxGeometry(sw,hh,d); b.translate(x+sw/2,hh/2,0);
    B.put(b,shadeColor(0x35342f,0.82+0.36*R()));
    const cap=new THREE.BoxGeometry(sw*1.03,0.09,d*1.08); cap.translate(x+sw/2,hh+0.045,0);
    B.put(cap,shadeColor(0x49473f,0.85+0.3*R()));
    x+=sw+(R()<0.45?(0.6+R()*1.1):0.05);
  }
  const sh=new THREE.CircleGeometry(w*0.62,12); sh.rotateX(-Math.PI/2);
  sh.scale(1.15,1,0.9); sh.translate(0,0.035,0.1); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x33342e,emissive:0x050605}),{c:o.rimC===undefined?0xd2d0c0:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  if(o.dou){
    const hole=new THREE.Mesh(new THREE.CircleGeometry(0.40,12,0,Math.PI),
      new THREE.MeshBasicMaterial({color:0x0b0d10}));
    hole.position.set(o.douX===undefined?0:o.douX,0.03,d/2+0.02);
    if(o.douFlip)hole.rotation.y=Math.PI;
    g.add(hole);
  }
  if(o.beams){
    const BB=new GeoBag();
    const b1=limbGeo([w*0.1,h*0.55,d*0.2],[w*0.42,h*0.06,d*1.5],0.10,0.05,5);
    BB.put(b1,shadeColor(0x2c241c,0.9));
    const b2=limbGeo([-w*0.28,h*0.72,d*0.2],[-w*0.62,h*0.05,d*1.2],0.09,0.045,5);
    BB.put(b2,shadeColor(0x2c241c,0.8));
    g.add(BB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x3a3026,emissive:0x050403}),{c:0xd2d0c0,i:0.10,p:2.2})));
  }
  const ph=R()*6.283;
  g.update=function(t){ };
  g.userData.update=g.update;
  return g;
}

/* —— 井 makeJingSW(o)：井台（低台+石井口+井口水影）+ 双柱顶梁井栏，合批 1 mesh ——
   「井上生旅葵」的井台 */
function makeJingSW(o){
  o=o||{};
  const B=new GeoBag();
  const base=new THREE.CylinderGeometry(1.55,1.78,0.52,12); base.translate(0,0.26,0);
  B.put(base,shadeColor(0x3f4144,0.9+0.2*Math.random()));
  const mouth=new THREE.CylinderGeometry(1.02,1.14,0.52,10); mouth.translate(0,0.76,0);
  B.put(mouth,0x33363a);
  const water=new THREE.CylinderGeometry(0.86,0.86,0.05,10); water.translate(0,1.0,0);
  B.put(water,0x11151a);
  [1,-1].forEach(function(s){
    const p=new THREE.CylinderGeometry(0.075,0.09,1.05,7); p.translate(s*1.12,1.42,0.55);
    B.put(p,0x2c2e32);
  });
  const beam=new THREE.BoxGeometry(2.5,0.14,0.16); beam.translate(0,1.98,0.55);
  B.put(beam,0x24262a);
  const sh=new THREE.CircleGeometry(2.0,14); sh.rotateX(-Math.PI/2);
  sh.scale(1.15,1,1); sh.translate(0,0.045,0.05); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3e42,emissive:0x050607}),{c:o.rimC===undefined?0xd4d2c2:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  return g;
}

/* —— 石臼 makeJiuSW(o)：石臼+斜倚木杵，合批 1 mesh ——「舂谷持作饭」的落点 */
function makeJiuSW(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.56,0.42,0.78,10); body.translate(0,0.39,0);
  B.put(body,shadeColor(0x3c3e42,0.95));
  const hole=new THREE.CylinderGeometry(0.30,0.26,0.10,10); hole.translate(0,0.76,0);
  B.put(hole,0x101215);
  const ch=new THREE.CylinderGeometry(0.055,0.08,1.55,7); ch.rotateZ(0.34);
  ch.translate(-0.14,1.22,0.05); B.put(ch,shadeColor(0x2c241c,1.0));
  const sh=new THREE.CircleGeometry(0.85,10); sh.rotateX(-Math.PI/2);
  sh.scale(1.3,1,1); sh.translate(0,0.04,0.04); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3e42,emissive:0x050606}),{c:o.rimC===undefined?0xd4d2c2:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  return g;
}

/* —— 旅谷 makeLvguSW(o)：一丛野谷（细秆微弯+垂穗），枯黄绿，合批 1 mesh ——「中庭生旅谷」 */
function makeLvguSW(o){
  o=o||{};
  const n=o.n===undefined?9:o.n, R=seedRnd(o.seed===undefined?25805:o.seed);
  const w=o.w===undefined?1.6:o.w, h=o.h===undefined?1.5:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*w*0.6, H=h*(0.6+0.55*R()), bnd=(R()-0.5)*0.4;
    B.put(limbGeo([x,0,z],[x+bnd*0.4,H*0.6,z],0.028,0.02,4),shadeColor(0x565838,0.85+0.35*R()));
    B.put(limbGeo([x+bnd*0.4,H*0.6,z],[x+bnd,H,z+bnd*0.3],0.02,0.016,4),shadeColor(0x565838,0.8+0.3*R()));
    const ear=new THREE.SphereGeometry(0.10,6,5);
    ear.scale(0.55,2.0,0.55); ear.rotateZ(bnd*0.5+0.25);
    ear.translate(x+bnd,H+0.14,z+bnd*0.3);
    B.put(ear,shadeColor(0x6e6638,0.9+0.3*R()));
  }
  const sh=new THREE.CircleGeometry(w*0.55,9); sh.rotateX(-Math.PI/2);
  sh.translate(0,0.035,0); B.put(sh,0x0b0d0f);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a3c2c,emissive:0x050604}),{c:o.rimC===undefined?0xcccaae:o.rimC,i:o.rim===undefined?0.09:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.035*Math.sin(t*0.9+ph)*kk;
    g.rotation.x=0.018*Math.sin(t*0.7+ph*1.4)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 旅葵 makeLvkuiSW(o)：一丛野葵（心形阔叶自中心外张），墨绿，合批 1 mesh ——「井上生旅葵」 */
function makeLvkuiSW(o){
  o=o||{};
  const n=o.n===undefined?8:o.n, R=seedRnd(o.seed===undefined?25806:o.seed);
  const r=o.r===undefined?0.85:o.r;
  const B=new GeoBag();
  const core=new THREE.CylinderGeometry(0.09,0.12,0.16,7); core.translate(0,0.08,0);
  B.put(core,0x3a4436);
  for(let i=0;i<n;i++){
    const a=i/n*6.283+(R()-0.5)*0.5, rr=r*(0.4+0.6*R());
    const leaf=new THREE.SphereGeometry(0.22+0.14*R(),7,5);
    leaf.scale(1.5,0.22,0.9); leaf.rotateZ(0.30); leaf.rotateY(-a);
    leaf.translate(Math.cos(a)*rr,0.16+0.10*R(),Math.sin(a)*rr);
    B.put(leaf,shadeColor(0x3e4c38,0.8+0.45*R()));
  }
  const sh=new THREE.CircleGeometry(r*0.9,9); sh.rotateX(-Math.PI/2);
  sh.translate(0,0.035,0); B.put(sh,0x0b0d0f);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c3a2c,emissive:0x040604}),{c:o.rimC===undefined?0xc8c6b2:o.rimC,i:o.rim===undefined?0.08:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.030*Math.sin(t*0.8+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 兔 makeTuSW(o)：野兔剪影（球身+长耳+短尾），近墨色，update 原地惊跳小巡——「兔从狗窦入」 */
function makeTuSW(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25807:o.seed);
  const s=o.scale===undefined?1:o.scale, B=new GeoBag();
  const body=new THREE.SphereGeometry(0.26,9,7);
  body.scale(1.05,0.85,1.55); body.translate(0,0.30,0); B.put(body,0x24262c);
  const head=new THREE.SphereGeometry(0.155,8,6); head.translate(0,0.42,0.34); B.put(head,0x24262c);
  [1,-1].forEach(function(sd){
    const ear=limbGeo([sd*0.06,0.52,0.30],[sd*0.10,0.86,0.38],0.045,0.018,5);
    B.put(ear,0x24262c);
  });
  const tail=new THREE.SphereGeometry(0.09,6,5); tail.translate(0,0.34,-0.40); B.put(tail,0x33363c);
  const sh=new THREE.CircleGeometry(0.32,9); sh.rotateX(-Math.PI/2);
  sh.scale(1.3,1,1.4); sh.translate(0,0.035,0); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3c4048,emissive:0x040506}),{c:o.rimC===undefined?0xd6d4c4:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  g.scale.setScalar(s);
  const ph=R()*6.283, x0=g.position.x, z0=g.position.z, ry0=g.rotation.y;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    const hop=Math.abs(Math.sin(t*2.6+ph));
    g.position.y=y0SW(g)+hop*0.15*kk;
    g.position.x=x0+0.42*Math.sin(t*0.21+ph)*kk;
    g.position.z=z0+0.30*Math.sin(t*0.17+ph*2.0)*kk;
    g.rotation.y=ry0+0.2*Math.sin(t*0.13+ph); };
  g.userData.update=g.update;
  return g;
}
function y0SW(g){ return g.userData.y0===undefined?(g.userData.y0=g.position.y):g.userData.y0; }

/* —— 雉 makeZhiSW(o)：野鸡剪影（球身+长尾锥+短翅），青铜暗色，update 绕残梁盘飞——「雉从梁上飞」 */
function makeZhiSW(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25808:o.seed);
  const s=o.scale===undefined?1:o.scale, B=new GeoBag();
  const body=new THREE.SphereGeometry(0.24,9,7);
  body.scale(0.95,0.8,1.5); B.put(body,0x33281e);
  const head=new THREE.SphereGeometry(0.11,7,6); head.translate(0,0.12,0.30); B.put(head,0x241c14);
  const beak=new THREE.ConeGeometry(0.035,0.14,5); beak.rotateX(Math.PI/2);
  beak.translate(0,0.11,0.44); B.put(beak,0x4a3c24);
  const tail=new THREE.ConeGeometry(0.055,1.15,6); tail.rotateX(Math.PI/2-0.45);
  tail.translate(0,0.16,-0.78); B.put(tail,shadeColor(0x33281e,1.15));
  [1,-1].forEach(function(sd){
    const wing=new THREE.SphereGeometry(0.16,7,5);
    wing.scale(0.24,0.10,0.9); wing.rotateZ(sd*0.35);
    wing.translate(sd*0.20,0.04,-0.05); B.put(wing,shadeColor(0x33281e,0.85));
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a3c2c,emissive:0x060403}),{c:o.rimC===undefined?0xd6d0c0:o.rimC,i:o.rim===undefined?0.12:o.rim,p:2.4})));
  g.scale.setScalar(s);
  const ph=R()*6.283;
  const cx=g.position.x, cy=g.position.y, cz=g.position.z;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    const a=t*0.40+ph;
    g.position.set(cx+Math.cos(a)*3.0, cy+0.9*(0.5+0.5*Math.sin(t*1.5+ph)), cz+Math.sin(a)*2.1);
    g.rotation.y=-a+Math.PI/2;
    g.rotation.z=0.12*Math.sin(t*3.0+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 老兵 makeLaobingSW(o)：八十岁归人（青灰袍/白发/发髻+拄杖），makeFigure 组合 ——
   贯穿全诗的同一造型：杖在右手侧、身形微倾，背影或侧影示人，含蓄无面目特写 */
function makeLaobingSW(o){
  o=o||{};
  const sc=o.scale===undefined?1.75:o.scale;
  const fig=makeFigure({pose:'独立',robe:0x3d4450,belt:0x5a6270,skin:0xd0ac86,collar:0x4a5060,
    hair:0xcac5ba,hat:'发髻',rim:0.40,rimC:o.rimC===undefined?0x8a94a6:o.rimC,noProp:true,scale:sc});
  if(o.cane!==false){
    const B=new GeoBag();
    B.put(limbGeo([0.80,0.02,0.16],[0.70,1.28,0.10],0.05,0.042,6),0x2a2018);
    const grip=new THREE.TorusGeometry(0.11,0.030,6,10,Math.PI);
    grip.translate(0.70,1.30,0.10); B.put(grip,0x2a2018);
    const cane=new THREE.Mesh(mergeGeos(B.list),
      new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
        specular:0x3a3026,emissive:0x050403}));
    fig.add(cane);
  }
  const g=new THREE.Group();
  g.add(fig);
  const ph=(o.seed===undefined?25809:o.seed)%6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    fig.rotation.z=0.012*Math.sin(t*0.4+ph)*kk;   /* 佝偻微晃 */
    fig.update(t,kk); };
  g.userData.update=g.update;
  return g;
}

/* —— 乡人 makeXiangrenSW(o)：指路乡人（指月姿态+褐灰袍），——「道逢乡里人」 */
function makeXiangrenSW(o){
  o=o||{};
  const sc=o.scale===undefined?1.6:o.scale;
  const fig=makeFigure({pose:'指月',robe:0x4a4438,belt:0x6a5a3a,skin:0xd2b090,collar:0x8a7a5a,
    hair:0x1c1c1c,hat:'幞头',rim:0.30,rimC:o.rimC===undefined?0xcfc8b4:o.rimC,noProp:true,scale:sc});
  const g=new THREE.Group(); g.add(fig);
  g.update=function(t,k){ const kk=k===undefined?1:k; fig.update(t,kk); };
  g.userData.update=g.update;
  return g;
}

/* —— 屋舍剪影 makeWusheSW(o)：远处村落（盒身+锥顶，浓墨剪影），合批 1 mesh —— 归途尽头的「家」之错觉 */
function makeWusheSW(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25810:o.seed);
  const n=o.n===undefined?4:o.n, w=o.w===undefined?16:o.w, B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=-w/2+(i+0.5)*(w/n)+(R()-0.5)*2.0, bw=2.2+1.6*R(), bh=1.6+1.1*R();
    const body=new THREE.BoxGeometry(bw,bh,bw*0.8); body.translate(x,bh/2,0);
    B.put(body,shadeColor(0x2a2d33,0.85+0.3*R()));
    const roof=new THREE.ConeGeometry(bw*0.85,1.0,4); roof.rotateY(Math.PI/4);
    roof.translate(x,bh+0.5,0); B.put(roof,shadeColor(0x22252a,0.85+0.3*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2e34,emissive:0x040506}),{c:o.rimC===undefined?0xd0cec0:o.rimC,i:o.rim===undefined?0.08:o.rim,p:2.0})));
  return g;
}

/* —— 蒲团 makePutuanSW(o)：草编坐席（扁圆墩），合批 1 mesh —— 案侧的「席」，空着的那只即「虚位」 */
function makePutuanSW(o){
  o=o||{};
  const B=new GeoBag();
  const c=new THREE.CylinderGeometry(0.52,0.58,0.17,12); c.translate(0,0.085,0);
  B.put(c,shadeColor(0x6a5c42,0.95));
  const top=new THREE.CylinderGeometry(0.42,0.50,0.06,12); top.translate(0,0.20,0);
  B.put(top,shadeColor(0x6a5c42,1.18));
  const sh=new THREE.CircleGeometry(0.66,10); sh.rotateX(-Math.PI/2);
  sh.translate(0,0.035,0); B.put(sh,0x0a0c0e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a4232,emissive:0x050403}),{c:o.rimC===undefined?0xd0c8b2:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  return g;
}

/* —— 纸色淡日 makeDanriSW(o)：limbTex 日轮+一环更淡的晕（fog:false；fadeK 初值=最大）——
   卷首/归途的暮日与末境东天的淡光 */
function makeDanriSW(o){
  o=o||{};
  const r=o.r===undefined?7:o.r, discOp=o.op===undefined?0.32:o.op, hazeOp=o.haze===undefined?0.10:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xf3ecd8:o.color,
    transparent:true,opacity:discOp,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0xefe8d2:o.hazeC,
    transparent:true,opacity:hazeOp,depthWrite:false,fog:false}));
  haze.scale.set(r*5.4,r*5.4,1); g.add(haze);
  g.update=function(t,k){ const kk=k===undefined?1:k;
    disc.material.opacity=kk*discOp*(0.95+0.05*Math.sin(t*0.4));
    haze.material.opacity=kk*hazeOp*(0.85+0.15*Math.sin(t*0.27+1.3)); };
  g.userData.update=g.update;
  return g;
}

/* —— 低平远山环 makeYuanHuanSW(o)：自建远山（在骨架常驻 bgRange 之前，z≈−120 不被遮挡）—— */
function makeYuanHuanSW(o){
  o=o||{};
  const ridge=makeRange({r:o.r===undefined?250:o.r,h:o.h===undefined?13:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?25811:o.seed,
    color:0x2c2f33,atmo:0xd8d5c9,fogK:0.60,glowK:0.03,glow:0xf2ecd8,y:-11,order:-6});
  return ridge;
}

function bCover(){ // 卷首 · 归乡暮色 —— 乡道蜿蜒，拄杖归人小影独行，远处松柏环冢、村舍剪影、淡日低垂
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe7e1cd,c2:0xc7cbaf,y:-2}); g.add(grd.mesh);
  const ridge=makeYuanHuanSW({seed:25811,r:250,h:13}); ridge.g.position.set(0,0,-120); g.add(ridge.g);
  const dao=makeDaoSW({w:3.0,L:62,rot:-0.10,y:-2.02,c:0xd9d1b7}); dao.position.set(1,0,-34); g.add(dao);
  /* 远处松柏环冢（荒凉预告） */
  const zhong=makeZhongSW({n:2,r:2.2,seed:25812,w:6.5}); zhong.position.set(-22,-1.72,-72); g.add(zhong);
  const bai1=makeSongbaiSW({kind:'bai',h:7.5,seed:25813}); bai1.position.set(-25,-1.7,-75); g.add(bai1);
  const bai2=makeSongbaiSW({kind:'bai',h:6.4,seed:25814}); bai2.position.set(-18.5,-1.7,-76.5); g.add(bai2);
  const song1=makeSongbaiSW({kind:'song',h:5.8,seed:25815}); song1.position.set(-27.5,-1.7,-68.5); g.add(song1);
  /* 村舍剪影与远处乡人 */
  const wushe=makeWusheSW({n:4,w:18,seed:25816}); wushe.position.set(24,-1.7,-62); g.add(wushe);
  const crowd=makeCrowd({n:3,rect:[19,-58,10,6],seed:25817,color:0x2a2f3a,rimC:0xbab8a8,rim:0.16,sMin:0.5,sMax:0.6,y:-1.7});
  g.add(crowd.mesh);
  /* 拄杖归人：小影独行于道上 */
  const laobing=makeLaobingSW({scale:1.25,seed:25818}); laobing.position.set(2.6,-1.02,-30); laobing.rotation.y=2.85; g.add(laobing);
  /* 淡日低垂、薄雾、枯树 */
  const sun=makeDanriSW({r:6.5,op:0.30,haze:0.09}); sun.position.set(-46,17,-98); g.add(sun);
  const ku1=makeKuShuSW({h:5.2,seed:25819}); ku1.position.set(-12,-1.7,-40); g.add(ku1);
  const mist=makeMist({n:6,spread:[220,16,90],pos:[0,4.5,-56],scale:68,color:0xe0d9c4,op:0.11});
  g.add(mist.g);
  const dust=makeGlow({n:22,box:[150,12,60],pos:[0,6,-42],color:0xd8d0b4,size:4.0,speed:0.03,rise:0,add:true,maxA:0.07});
  g.add(dust.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:3.0,w:13,d:6,color:0x23262b,seed:25820,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-12,-1.9,17); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:12,n:8,d:3,color:0x1d1f22,seed:25821,sway:0.8,tip:0x5a5648,scale:0.8});
  fgR.g.position.set(11,-1.8,16); g.add(fgR.g);
  addLights(g,{c:0xe2d8bc,i:0.5,p:[-40,84,26]},{c:0xd4d6c4,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); sun.update(t,k); ku1.update(t,k); laobing.update(t,k);
    bai1.update(t,k); bai2.update(t,k); song1.update(t,k);
    mist.update(t,k); dust.update(t); fgL.update(t,k); fgR.update(t,k); crowd.update(t);
  }};
}
function bShigui(){ // 壹 · 从军始归 —— 十五从军征，八十始得归；道逢乡里人，家中有阿谁：
                    // 暮色乡道，拄杖白发的老兵与抬手遥指的乡人
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0xe7e1cd,c2:0xc6caae,y:-1.8}); g.add(grd.mesh);
  const ridge=makeYuanHuanSW({seed:25822,r:240,h:12}); ridge.g.position.set(-20,0,-118); g.add(ridge.g);
  const dao=makeDaoSW({w:3.2,L:44,rot:0.10,y:-1.83,c:0xd9d1b7}); dao.position.set(0.5,0,-22); g.add(dao);
  /* 道逢二人：老兵拄杖侧影，乡人抬手遥指（指向境贰的方向） */
  const laobing=makeLaobingSW({scale:1.8,seed:25823}); laobing.position.set(-2.2,-0.32,-13.5); laobing.rotation.y=1.2; g.add(laobing);
  const xiangren=makeXiangrenSW({scale:1.62,seed:25824}); xiangren.position.set(1.8,-0.28,-11.8); xiangren.rotation.y=1.0; g.add(xiangren);
  /* 归途尽头：村舍剪影+枯树（家的错觉所在） */
  const wushe=makeWusheSW({n:3,w:13,seed:25825}); wushe.position.set(14,-1.6,-52); g.add(wushe);
  const ku1=makeKuShuSW({h:4.6,seed:25826}); ku1.position.set(-8.5,-1.7,-30); g.add(ku1);
  const ku2=makeKuShuSW({h:5.4,seed:25827}); ku2.position.set(9.5,-1.7,-34); g.add(ku2);
  /* 暮日西斜、薄雾、草虫微光 */
  const sun=makeDanriSW({r:6,op:0.30,haze:0.09}); sun.position.set(-42,15,-92); g.add(sun);
  const mist=makeMist({n:6,spread:[210,15,90],pos:[0,4.2,-50],scale:66,color:0xe0d9c4,op:0.10});
  g.add(mist.g);
  const dust=makeGlow({n:20,box:[140,11,56],pos:[0,5.5,-38],color:0xd8d0b4,size:4.0,speed:0.03,rise:0,add:true,maxA:0.07});
  g.add(dust.points);
  const fgL=makeForeground({kind:'芦苇',w:13,n:9,d:3,color:0x1d1f22,seed:25828,sway:0.9,tip:0x5a5648,scale:0.78});
  fgL.g.position.set(-11,-1.7,14); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:2.6,w:11,d:5,color:0x23262b,seed:25829,rim:0.10,rimC:0xecead8});
  fgR.g.position.set(11.5,-1.6,13); g.add(fgR.g);
  addLights(g,{c:0xe4d8b8,i:0.52,p:[-40,80,26]},{c:0xd6d8c6,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); sun.update(t,k); laobing.update(t,k); xiangren.update(t,k);
    ku1.update(t,k); ku2.update(t,k);
    mist.update(t,k); dust.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bSongbai(){ // 贰（标志性瞬间）· 松柏累累 —— 遥看是君家，松柏冢累累；兔从狗窦入，雉从梁上飞：
                     // 乡人所指的「君家」，是松柏成林下的累累坟冢与一座兔雉横行的荒宅
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0xe5dfcc,c2:0xc3c7ad,y:-1.8}); g.add(grd.mesh);
  const ridge=makeYuanHuanSW({seed:25830,r:240,h:12}); ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 松柏冢累累：三座土冢，松柏环立（克制写意：土馒头坟形，无碑无骸） */
  const zhong=makeZhongSW({n:3,r:2.4,seed:25831,w:11}); zhong.position.set(-2.5,-1.62,-56); g.add(zhong);
  const bai1=makeSongbaiSW({kind:'bai',h:8.6,seed:25832}); bai1.position.set(-8.5,-1.7,-64); g.add(bai1);
  const bai2=makeSongbaiSW({kind:'bai',h:7.8,seed:25833}); bai2.position.set(2.5,-1.7,-66); g.add(bai2);
  const bai3=makeSongbaiSW({kind:'bai',h:6.8,seed:25834}); bai3.position.set(-3.5,-1.7,-61); g.add(bai3);
  const song1=makeSongbaiSW({kind:'song',h:6.6,seed:25835}); song1.position.set(-13,-1.7,-58); g.add(song1);
  const song2=makeSongbaiSW({kind:'song',h:6.0,seed:25836}); song2.position.set(8.5,-1.7,-60); g.add(song2);
  const song3=makeSongbaiSW({kind:'song',h:5.4,seed:25837}); song3.position.set(-16.5,-1.7,-50); g.add(song3);
  /* 荒宅断墙：狗窦洞开（兔入之门）、断梁斜倚（雉起之梁） */
  const qiang=makeCanQiangSW({w:10,h:2.3,segs:3,seed:25838,dou:true,douX:1.2,beams:true});
  qiang.position.set(11,-1.8,-30); qiang.rotation.y=-0.35; g.add(qiang);
  /* 兔从狗窦入（洞口旁惊跳）、雉从梁上飞（绕梁盘旋） */
  const tu=makeTuSW({scale:1.15,seed:25839}); tu.position.set(7.6,-1.72,-27.2); tu.rotation.y=-0.6; g.add(tu);
  const zhi=makeZhiSW({scale:1.25,seed:25840}); zhi.position.set(11,2.6,-30); g.add(zhi);
  /* 老兵背影：立于道口，望着松柏下的坟园 */
  const laobing=makeLaobingSW({scale:1.8,seed:25841}); laobing.position.set(-11,-0.32,-16); laobing.rotation.y=2.86; g.add(laobing);
  /* 纸上淡日、薄雾、枯树 */
  const sun=makeDanriSW({r:5.5,op:0.24,haze:0.08}); sun.position.set(34,20,-95); g.add(sun);
  const ku1=makeKuShuSW({h:4.8,seed:25842}); ku1.position.set(-18,-1.7,-34); g.add(ku1);
  const mist=makeMist({n:6,spread:[220,15,90],pos:[0,4.2,-52],scale:66,color:0xded7c2,op:0.11});
  g.add(mist.g);
  const dust=makeGlow({n:20,box:[140,11,56],pos:[0,5.5,-40],color:0xd6ceB4,size:4.0,speed:0.03,rise:0,add:true,maxA:0.07});
  g.add(dust.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:3.0,w:12,d:5,color:0x23262b,seed:25843,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-12,-1.8,13); g.add(fgL.g);
  const fgR=makeForeground({kind:'树枝',w:11,n:7,d:3,color:0x1a1c20,seed:25844,sway:0.7,tip:0x3a3e3a,scale:0.85});
  fgR.g.position.set(12,-1.2,14); g.add(fgR.g);
  addLights(g,{c:0xdcd8c4,i:0.46,p:[30,76,26]},{c:0xd2d4c4,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); sun.update(t,k);
    bai1.update(t,k); bai2.update(t,k); bai3.update(t,k);
    song1.update(t,k); song2.update(t,k); song3.update(t,k);
    tu.update(t,k); zhi.update(t,k); laobing.update(t,k); ku1.update(t,k);
    mist.update(t,k); dust.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bLvgu(){ // 叁 · 旅谷旅葵 —— 中庭生旅谷，井上生旅葵；舂谷持作饭，采葵持作羹：
                  // 破败庭院里野谷自生野葵自长，老兵在石臼旁舂谷做饭——一顿没人等的饭
  const g=new THREE.Group();
  const grd=makeGround({r:230,c1:0xe6e0cc,c2:0xc5c9ad,y:-1.8}); g.add(grd.mesh);
  const ridge=makeYuanHuanSW({seed:25845,r:230,h:11}); ridge.g.position.set(-14,0,-118); g.add(ridge.g);
  /* 庭院：后墙（带门洞豁口）+ 左侧断墙 + 右侧塌矮墙 */
  const qb=makeCanQiangSW({w:17,h:2.5,segs:4,seed:25846,dou:true,douX:4.0});
  qb.position.set(0,-1.8,-34); g.add(qb);
  const ql=makeCanQiangSW({w:8,h:2.0,segs:2,seed:25847,dou:false});
  ql.position.set(-11.5,-1.8,-27); ql.rotation.y=Math.PI/2; g.add(ql);
  const qr=makeCanQiangSW({w:5.5,h:1.5,segs:2,seed:25848,dou:false,beams:true});
  qr.position.set(10.5,-1.8,-30); qr.rotation.y=Math.PI/2; g.add(qr);
  /* 中庭旅谷丛生、井上旅葵自长 */
  const gu1=makeLvguSW({seed:25849,h:1.6}); gu1.position.set(1.0,-1.76,-28.5); g.add(gu1);
  const gu2=makeLvguSW({seed:25850,h:1.3,n:7}); gu2.position.set(4.0,-1.76,-31.5); g.add(gu2);
  const gu3=makeLvguSW({seed:25851,h:1.1,n:6,w:1.2}); gu3.position.set(-2.5,-1.76,-31); g.add(gu3);
  const jing=makeJingSW({seed:25852}); jing.position.set(-6.5,-1.78,-27); g.add(jing);
  const kui1=makeLvkuiSW({seed:25853,r:0.8}); kui1.position.set(-6.5,-1.28,-26.2); g.add(kui1);
  const kui2=makeLvkuiSW({seed:25854,r:0.7}); kui2.position.set(2.8,-1.76,-24.5); g.add(kui2);
  const kui3=makeLvkuiSW({seed:25855,r:0.6,n:6}); kui3.position.set(-3.8,-1.76,-22.5); g.add(kui3);
  /* 舂谷：石臼+杵，老兵侧影对臼而立 */
  const jiu=makeJiuSW({seed:25856}); jiu.position.set(6.8,-1.76,-25); g.add(jiu);
  const laobing=makeLaobingSW({scale:1.75,seed:25857,cane:false}); laobing.position.set(8.6,-0.34,-21.8); laobing.rotation.y=-2.65; g.add(laobing);
  /* 淡日在天、薄雾横庭 */
  const sun=makeDanriSW({r:5.5,op:0.26,haze:0.08}); sun.position.set(-38,18,-92); g.add(sun);
  const mist=makeMist({n:6,spread:[210,14,86],pos:[0,4.0,-50],scale:64,color:0xded7c2,op:0.10});
  g.add(mist.g);
  const dust=makeGlow({n:20,box:[130,10,52],pos:[0,5,-36],color:0xd6ceB4,size:3.8,speed:0.03,rise:0,add:true,maxA:0.07});
  g.add(dust.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x23262b,seed:25858,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-10,-1.8,12.5); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:11,n:8,d:3,color:0x1d1f22,seed:25859,sway:0.8,tip:0x5a5648,scale:0.75});
  fgR.g.position.set(10.5,-1.7,12); g.add(fgR.g);
  addLights(g,{c:0xe0d8c0,i:0.5,p:[-36,78,24]},{c:0xd4d6c6,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); sun.update(t,k);
    gu1.update(t,k); gu2.update(t,k); gu3.update(t,k);
    kui1.update(t,k); kui2.update(t,k); kui3.update(t,k);
    laobing.update(t,k);
    mist.update(t,k); dust.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bGengfan(){ // 肆（末境·可点击）· 羹饭贻谁 —— 羹饭一时熟，不知贻阿谁；出门东向看，泪落沾我衣：
                     // 檐下一案两席：案上羹饭初熟、对面蒲团空席虚位；点击后热气升腾、暮色转冷、青灰暮流、泪光一点
  const ctl={t:0,clicked:false,on:false,dusk:0};
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0xe4decb,c2:0xc2c6ac,y:-1.8}); g.add(grd.mesh);
  const ridge=makeYuanHuanSW({seed:25860,r:220,h:11}); ridge.g.position.set(6,0,-116); g.add(ridge.g);
  /* 身后的屋：残墙带门洞（出门东向的门） */
  const qiang=makeCanQiangSW({w:14,h:2.4,segs:3,seed:25861,dou:true,douX:-3.5,beams:true});
  qiang.position.set(-3,-1.8,-30); qiang.rotation.y=-0.15; g.add(qiang);
  /* 案上羹饭：一案、饭碗羹碗、一碟、热气（点击前 uMaxA=0.001 近隐） */
  const table=makeTable({w:5.6,d:2.3,h:1.45,wood:0x2a221a});
  table.g.position.set(-2,-1.62,-19.5); g.add(table.g);
  const fan=makeVessel({type:'碗',mat:'陶',scale:1.0,shadow:true});
  fan.g.position.set(-1.3,1.44,-19.9); fan.g.rotation.y=0.4; g.add(fan.g);
  const geng=makeVessel({type:'碗',mat:'陶',scale:0.92,shadow:true});
  geng.g.position.set(-2.7,1.44,-19.3); geng.g.rotation.y=-0.5; g.add(geng.g);
  const die=makeDish({r:0.55,n:3,plate:0x6a6252,sheen:false});
  die.g.position.set(-0.6,1.44,-18.9); g.add(die.g);
  /* 对面空席：案两端各一只蒲团——席在，人不在（含蓄的「虚位」）+ 案头空碗 */
  const pt1=makePutuanSW({}); pt1.position.set(-4.6,-1.6,-17.2); g.add(pt1);
  const pt2=makePutuanSW({}); pt2.position.set(0.6,-1.6,-17.2); g.add(pt2);
  const kong=makeVessel({type:'碗',mat:'陶',scale:0.9,shadow:true});
  kong.g.position.set(-3.9,1.44,-19.0); g.add(kong.g);
  /* 热气（点击后升腾；组 visible=false 硬关，uMaxA 初值=峰值 0.42） */
  const steamG=new THREE.Group(); steamG.visible=false; g.add(steamG);
  const steam=makeGlow({n:26,box:[2.6,4.2,2.0],pos:[-2.2,1.9,-19.5],color:0xf2ecd8,size:1.7,speed:0.13,rise:1,add:false,maxA:0.42});
  steamG.add(steam.points);
  /* 老兵侧背影：立于案侧向东（画面右）望——出门东向看 */
  const laobing=makeLaobingSW({scale:1.8,seed:25862}); laobing.position.set(1.4,-0.32,-20.6); laobing.rotation.y=1.62; g.add(laobing);
  /* 泪光一点（点击后显；accent 青灰，初值=峰值） */
  const leig=new THREE.Group(); leig.visible=false; g.add(leig);
  const lei=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x6a7284,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  lei.scale.set(0.9,1.3,1); lei.position.set(1.4,5.2,-20.4); lei.renderOrder=4; leig.add(lei);
  /* 东天淡日（暮）+ 青灰暮流（accent=#4a5060，点击后漫起；初值=峰值）+ 薄雾 */
  const sun=makeDanriSW({r:6.5,op:0.26,haze:0.09,color:0xefe6cc,hazeC:0xe6dcc0});
  sun.position.set(46,9,-84); g.add(sun);
  const flow=makeFlow({n:360,box:[110,14,50],pos:[8,6,-34],color:0x4a5060,size:20,speed:2.6,maxA:0.001});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[200,14,84],pos:[0,4.0,-48],scale:64,color:0xdcd5c1,op:0.10});
  g.add(mist.g);
  const dust=makeGlow({n:18,box:[120,10,50],pos:[0,5,-34],color:0xd4ccB2,size:3.8,speed:0.03,rise:0,add:true,maxA:0.06});
  g.add(dust.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x23262b,seed:25863,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-10.5,-1.8,12.5); g.add(fgL.g);
  const fgR=makeForeground({kind:'树枝',w:10,n:7,d:3,color:0x1a1c20,seed:25864,sway:0.7,tip:0x3a3e3a,scale:0.8});
  fgR.g.position.set(11,-1.2,12); g.add(fgR.g);
  /* 局部暮光：点击后由暖转冷（自建灯逐帧动画；初值 0.5=最大） */
  const dLight=new THREE.DirectionalLight(0xdccaa2,0.5); dLight.position.set(44,50,16); g.add(dLight);
  addLights(g,null,{c:0xccccc0,i:0.58});
  const lw=C(0xdccaa2), lc=C(0x8b93a4);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.dusk=Math.min(1,ctl.dusk+dt/4.0);
      const e0=ctl.dusk, e=e0*e0*(3-2*e0);
      /* 暮色转冷：局部光由暖转冷、渐暗；热气升腾、青灰暮流漫院、泪光一点 */
      dLight.color.copy(lw).lerp(lc,e);
      dLight.intensity=k*(0.5-0.24*e)*(0.92+0.08*Math.sin(t*0.7));
      steamG.visible=k*e>0.004;
      steam.mat.uniforms.uMaxA.value=0.001+0.42*e;
      flow.mat.uniforms.uMaxA.value=0.001+0.22*e;
      leig.visible=k*e>0.004;
      lei.material.opacity=k*0.20*e;
      mist.update(t,k*(0.6+0.4*e));
      grd.update();
      ridge.update(t,0); flow.update(t); steam.update(t); sun.update(t,k);
      laobing.update(t,k); fan.update(t,k); geng.update(t,k); kong.update(t,k);
      fgL.update(t,k); fgR.update(t,k); dust.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.20);
        pluck(0,0.0,0.10); pluck(2,0.7,0.08); pluck(1,1.5,0.06);
        const fl=$('#flash'); fl.textContent='羹饭一时熟 不知贻阿谁';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xdcd4bc),bot:C(0xccc4ad),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d2be),dirI:0.44,
  dirP:new THREE.Vector3(-46,105,30),ambC:C(0xd4d6c4),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,52],t:[0,11,46],lf:[0,7,-30],lt:[2,7.5,-42]},
  sky:()=>SK({fd:0.0046,star:0.03}) },
{ name:'从军始归',dwell:20,river:0.02,build:bShigui,
  cam:{f:[-0.5,6.2,24],t:[1.0,6.8,20],lf:[-1,5.2,-13],lt:[1.5,5.8,-17]},
  sky:()=>SK({fd:0.0050,dirC:C(0xe4d8b8),dirI:0.50,
    dirP:new THREE.Vector3(-40,90,26),ambC:C(0xd8d8c6),ambI:0.62}) },
{ name:'松柏累累',dwell:22,river:0.02,build:bSongbai,
  cam:{f:[0,7.5,32],t:[-1.5,8,26],lf:[0,5.5,-42],lt:[-2,6,-56]},
  sky:()=>SK({fd:0.0058,hor:C(0xd6cfb8),dirC:C(0xd4d0c0),dirI:0.44,
    dirP:new THREE.Vector3(34,88,24),ambC:C(0xd0d2c2),ambI:0.60}) },
{ name:'旅谷旅葵',dwell:20,river:0.02,build:bLvgu,
  cam:{f:[2,5.8,21],t:[0,6.2,17],lf:[0,4.4,-26],lt:[-1.5,4.8,-32]},
  sky:()=>SK({fd:0.0052,dirC:C(0xe0d8c0),dirI:0.48,
    dirP:new THREE.Vector3(-36,84,24),ambC:C(0xd4d6c6),ambI:0.62}) },
{ name:'羹饭贻谁',dwell:24,river:0.02,build:bGengfan,
  cam:{f:[0,5.8,20],t:[-1,6.2,16],lf:[0,4.8,-18],lt:[2.5,5.2,-22]},
  sky:()=>SK({fd:0.0060,hor:C(0xd2cab2),dirC:C(0xd4cbb0),dirI:0.42,
    dirP:new THREE.Vector3(40,70,18),ambC:C(0xccccc0),ambI:0.58}) },
];
"""

if __name__ == '__main__':
    print('shiwucongjun.py —— 被 build.py 消费：python build.py shiwucongjun')
