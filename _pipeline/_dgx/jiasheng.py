# -*- coding: utf-8 -*-
"""jiasheng.py —— 《贾生》（唐·李商隐，queue no.230，水墨夜思）生成配置
两境（N=queue stages 数）：宣室访贤（宣室求贤访逐臣·贾生才调更无伦——殿内召对、才调无伦）、
夜半前席（可怜夜半虚前席·不问苍生问鬼神——末境点击，标志性瞬间）。
水墨夜思全套色板：底色 #0d1117、雾 #121a26 系、文字 #dfe6f0，accent=#9ab8d8（queue 分配强调色，
月银青蓝）只落在冷月晕/殿外夜色/鬼神异光/人物边缘光/UI 上，全页近零饱和；殿内烛火是全页
唯一的暖色（水墨夜思「暖烛光点缀」的正用）——暖与冷的对切就是本诗的结构：宣室内烛光殷勤，
殿外夜色里才是苍生。
与已有水墨夜思页第一眼可区分：不做满月江楼水天一色（jianglou-ganjiu）、不做古寺竹径
（ti-poshansi）、不做雨前危城（xianyang-chenglou）、不做渡口斜月渔火（ti-jinlingdu）——
做「汉宫宣室大殿内景」：殿柱两列、帷幔帝座、铜烛台暖光、君臣对坐席案；东廊开敞，
殿外夜色宫墙阙楼做冷色对比。全诗无江湖山海，是一次室内夜谈。
标志性瞬间（境贰·全诗名句，queue moment：不问苍生问鬼神——夜半前席的错位）：夜半烛短，
点击画面——①烛影摇动（焰宽加大、暖晕升至顶）②文帝连席前移、倾身相问（「前席」的具象）
③殿内冷异光自藻井缓缓沉落（鬼神之问的阴翳）④殿门外苍生剪影淡现又散（「不问苍生」——
被冷落的人在门外）⑤题字「可怜夜半虚前席 不问苍生问鬼神」同现——前席愈切，讽意愈深。
考点钉子：贾 jiǎ（人名）/ 调 diào（才调）（小测第 3 题落点）；贾谊宣室召对 + 李商隐托古讽时
（第 4 题）；「不问苍生问鬼神」的对比讽刺手法（第 5 题）。
多音字：贾生→甲生、才调→才掉 钉同音替换（tts.json）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='jiasheng', title='贾生', dyn='唐 · 李商隐', brand_author='李 商 隐',
    gold_rgb='154,184,216',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#9ab8d8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(154,184,216,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(9,14,22', 1),
        ('rgba(4,6,11', 'rgba(8,12,19', 2),
        ('rgba(6,9,16', 'rgba(10,15,23', 1),
        ('rgba(3,5,9', 'rgba(6,9,15', 1),
        ('#0b101c', '#121a28', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
        ('0x0a1526', '0x121a26', 4),
    ],
    tip='轻点画面 / 按空格 —— 夜半前席，烛影摇动',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看文帝前席倾谈、烛影摇动，殿外苍生淡现又散',
    cover_read='贾生。唐，李商隐。宣室求贤访逐臣，贾生才调更无伦。可怜夜半虚前席，不问苍生问鬼神。',
    cover_p1='两重意境，随诗句次第展开：汉文帝求贤若渴，在宣室接见被放逐多年的贾谊，这位少年的才华气调举世无伦；夜半谈深，文帝不觉前席倾身——可惜问的不是苍生百姓，而是鬼神之事。',
    cover_p2='边读诗，边跟着李商隐走进这间烛火摇曳的宣室：前两句把文帝抬得多高，后两句就叹得多重——读懂「不问苍生问鬼神」这一声反讽，就读懂了这首咏史绝句里的时代之痛。',
    end_h2='前席 · 长叹', cn_word='两',
    words_js="['再入一次宣室','初识义山，尚需共读','渐入诗境，再诵几遍','夜半前席，烛影摇动','已解不问苍生之讽','鬼神之问，苍生谁问']",
    sky_atmo='0x1f2b3a',
)

POEM_JS = """const POEM = [
{ name:'宣室访贤', jing:'汉文帝求贤，在宣室接见被放逐之臣；贾谊的才华气调，更是举世无伦 —— 求贤访逐，才调无伦。（宣室 · 逐臣 · 才调）',
  segs:[
   {c:'宣室求贤访逐臣，', p:py('xuān shì qiú xián fǎng zhú chén')},
   {c:'贾生才调更无伦。', p:py('jiǎ shēng cái diào gèng wú lún')}],
  read:'宣室求贤访逐臣，贾生才调更无伦。',
  yisi:'汉文帝为了访求贤才，接见被放逐在外的臣子；贾谊的才华气调，更是无与伦比。——前两句从正面落笔，写得堂皇郑重：「求贤」「访逐臣」，俨然一副求贤若渴的明君气象；「才调更无伦」是极高的推许——一个「更」字，把贾谊抬到诸贤之上。抬得越高，后面摔得越响：这两句的隆重，全是为后两句的反转蓄力，欲抑先扬。',
  zhu:[['宣室','未央宫前殿的正室，汉代皇帝斋戒、召对大臣之处——这里代指朝廷召见'],['逐臣','被贬逐放逐的臣子——指贾谊：他因锋芒太露遭大臣构陷，被外放为长沙王太傅多年，后被文帝召回长安'],['贾生','即贾谊（前 200—前 168），西汉洛阳人，少年政论家，十八岁以能诵诗书属文闻名郡中，著有《过秦论》《陈政事疏》等；人称贾生、贾长沙'],['才调','才华气调。调，读 diào，指才情风调——不是调子的调'],['更无伦','更加无与伦比。伦，辈、类——无人能与他同列而比'],['欲抑先扬','先极力褒扬（求贤、才调无伦），再急转揭示了可叹的真相（问鬼神）——褒扬是蓄势，反讽因落差而生']] },
{ name:'夜半前席', jing:'谈到夜半，文帝徒然前席倾身；可问的不是苍生百姓，而是鬼神之事 —— 前席愈切，可叹愈深。（夜半 · 前席 · 苍生 · 鬼神）（末境点击画面：烛影摇动，看文帝前席、殿外苍生淡现）',
  segs:[
   {c:'可怜夜半虚前席，', p:py('kě lián yè bàn xū qián xí')},
   {c:'不问苍生问鬼神。', p:py('bù wèn cāng shēng wèn guǐ shén')}],
  read:'可怜夜半虚前席，不问苍生问鬼神。',
  yisi:'谈到夜半，文帝听得入神，在坐席上不知不觉向前挪移，凑近贾谊——可惜，他殷勤问的不是苍生百姓，而是鬼神之事。——全诗的讽刺全在最后七个字的对比里：「前席」这个动作何等恳切，「夜半」谈兴何等浓酣，可惜全是徒然（「虚」字是诗眼）——因为话题问错了：不问苍生问鬼神。贾谊满腹安民济世之策，文帝却只对祭祀鬼神、长生祈福感兴趣。诗人不置一句褒贬，只把「前席之勤」与「所问之误」并置，讽意自见。这是借汉文帝这件「明君求贤」的美谈翻案——托古讽时：晚唐皇帝佞佛崇道、不问国计民生，李商隐为贾生哭，也为天下才士哭，更为苍生哭。',
  zhu:[['可怜','可惜、可叹——一声浩叹，全诗讽意由此透出'],['夜半','半夜——召谈从入夜直谈到夜半，见谈之久、文帝谈兴之浓'],['虚前席','徒然地在坐席上向前移动、凑近对方。虚，徒然、白白地；前席，古人席地而坐，谈得投机便不觉向前移膝——古人表示倾心请教的动作'],['苍生','百姓、黎民——贾谊胸中最要紧的事'],['鬼神','鬼神祭祀、长生祈福一类虚无缥缈的话题'],['托古讽时','借汉文帝宣室召对的故事，讽刺晚唐帝王崇道佞佛、不求贤不问民的现实——咏史而后讽今，一句「不问苍生」双写古今']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「宣室求贤访逐臣」的下一句是？', o:['贾生才调更无伦','可怜夜半虚前席','不问苍生问鬼神'], a:0},
 {q:'「可怜夜半虚前席」的下一句是？', o:['宣室求贤访逐臣','贾生才调更无伦','不问苍生问鬼神'], a:2},
 {q:'「贾生才调更无伦」中「贾」与「调」的读音，正确的一项是？', o:['贾读 jiǎ（贾生即贾谊，人名）；调读 diào——「才调」即才华气调','贾读 gǔ（行商坐贾）；调读 tiáo——「才调」即调整、协调','贾读 jiǎ；调读 tiáo——「才调」即调子、曲调，指贾谊善鼓瑟'], a:0},
 {q:'关于贾谊宣室召对与这首诗，下列说法正确的是？', o:['贾谊是西汉政论家，被贬为长沙王太傅多年后文帝将他召回，在未央宫宣室接见——李商隐咏此事，是借古人酒杯浇自己块垒的咏史诗','贾谊是东汉隐士，隐居宣室著《过秦论》；此诗写他归隐田园的闲适自得','贾谊是「初唐四杰」之一；此诗写他登楼远眺、思念长安的乡愁'], a:0},
 {q:'「可怜夜半虚前席，不问苍生问鬼神」历来被推为咏史绝句的顶点。对它的讽刺手法，理解最准确的一项是？', o:['以「前席」之勤与「所问之误」对比：君王求贤貌似殷勤恳切，关心的却不是国计民生——不着一字褒贬，托古讽时自在言外','单纯记事：如实记录文帝夜半向贾谊请教祭祀礼仪的经过，并无讽刺之意','极力颂美文帝：夜半仍向贤臣倾身求教，说明他求贤若渴、勤政爱民'], a:0},
];
"""

SCENES_JS = """/* ================= 贾生 · 两境场景（水墨夜思·宣室夜话：宣室访贤、夜半前席） =================
   美术立意：水墨夜思色板写「汉宫宣室的烛光夜谈」——底色 #0d1117、雾 #121a26 系，
   accent=#9ab8d8（月银青蓝）只落在冷月/殿外夜色/鬼神异光/边缘光/UI 上，全页近零饱和；
   殿内铜烛台的暖光（core 0xffe2a8/outer 0xff8a3a）是全页唯一暖色——暖（殿内殷勤）与
   冷（殿外苍生）的对切，就是「不问苍生问鬼神」的画面结构。
   与已有水墨夜思页第一眼可区分：不做满月江楼（jianglou-ganjiu）、不做古寺竹径（ti-poshansi）、
   不做雨前危城（xianyang-chenglou）、不做渡口渔火（ti-jinlingdu）——做宣室大殿内景：
   台基高殿、殿柱两列、帷幔帝座、藻井四阿顶，君臣对坐席案于殿心，东廊开敞，
   门外夜色里宫墙阙楼横陈——全诗无江湖山海，是一次室内夜谈。
   境壹：殿内斜望——帝座帷幔在左上，君臣对坐烛光在中，东廊外冷月宫墙在右——宣室求贤的隆重。
   境贰（末境可点击）：夜半烛短，镜头更低更近；点击：烛影摇动（焰宽加大）+文帝连席前移
   （「前席」具象化）+殿内冷异光沉落（鬼神之问）+殿外苍生剪影淡现又散（不问苍生）——
   前席愈切，讽意愈深。 */

/* —— 殿幔 makeLian(o)：自建帷幔（几何褶皱+上亮下暗顶点色；墨青冷丝——specular 压到近零
   并自带冷性自发光，避免骨架 makeCurtain 的红铜 specular 把烛光反成绛红，破坏水墨零饱和） */
function makeLian(o){
  o=o||{};
  const w=o.w===undefined?14:o.w, h=o.h===undefined?9:o.h;
  const folds=o.folds===undefined?7:o.folds;
  const geo=new THREE.PlaneGeometry(w,h,36,1);
  const pos=geo.attributes.position;
  const col=new Float32Array(pos.count*3);
  const base=C(o.color===undefined?0x252c3a:o.color), dk=C(o.dark===undefined?0x0a0d13:o.dark);
  for(let i=0;i<pos.count;i++){
    const x=pos.getX(i), y=pos.getY(i);
    pos.setZ(i,(o.deep===undefined?0.70:o.deep)*Math.sin(x/w*Math.PI*folds));
    const t=clamp(y/h+0.5,0,1);
    const foldK=0.80+0.34*(0.5+0.5*Math.sin(x/w*Math.PI*folds+1.2));
    const c=dk.clone().lerp(base,0.16+t*t*0.84);
    col[i*3]=c.r*foldK; col[i*3+1]=c.g*foldK; col[i*3+2]=c.b*foldK;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(col,3));
  pos.needsUpdate=true; geo.computeVertexNormals();
  const mat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:2,specular:0x0c1016,emissive:0x0b101a,side:THREE.DoubleSide});
  const mesh=new THREE.Mesh(geo,mat); mesh.renderOrder=0;
  mesh.position.y=h/2;
  const g=new THREE.Group(); g.add(mesh);
  return {g,mesh};
}

/* —— 宣室大殿 makeXuanshi(o)：台基+台阶+地坪+北墙西墙（东廊开敞）+藻井+四阿顶+南檐列柱+
   东廊柱列+帝座高台（合批 1 mesh）——「宣室」本体：汉家大殿，殿心留白供君臣对坐 */
function makeXuanshi(o){
  o=o||{};
  const B=new GeoBag();
  const tai=new THREE.BoxGeometry(36,1.6,34);
  tai.translate(0,0.8,-6); B.put(tai,0x161e2a);
  for(let i=0;i<3;i++){
    const st=new THREE.BoxGeometry(11-i*1.6,0.52,1.5);
    st.translate(0,0.30+i*0.52,11.9+i*0.75); B.put(st,shadeColor(0x1a2330,0.85+i*0.14));
  }
  const fl=new THREE.BoxGeometry(30,0.34,27);
  fl.translate(0,1.60,-7); B.put(fl,0x1e2836);
  const back=new THREE.BoxGeometry(33,10,1.2);
  back.translate(0,6.6,-20.4); B.put(back,0x121926);
  const ww=new THREE.BoxGeometry(1.2,9.4,28);
  ww.translate(-15.2,6.4,-7); B.put(ww,0x111824);
  const ceil=new THREE.BoxGeometry(33,0.9,31);
  ceil.translate(0,11.6,-6.5); B.put(ceil,0x0d131d);
  const beam=new THREE.BoxGeometry(33,1.3,1.6);
  beam.translate(0,10.6,10.3); B.put(beam,0x1a2330);
  const roof=new THREE.ConeGeometry(24,5.2,4);
  roof.rotateY(Math.PI/4); roof.scale(1.28,1,1.10); roof.translate(0,14.6,-6); B.put(roof,0x101724);
  const ridge=new THREE.BoxGeometry(22,0.9,1.6);
  ridge.translate(0,17.4,-6); B.put(ridge,0x1a2330);
  /* 南檐列柱 + 东廊柱列（础+柱身；殿内不做西列，免与人物抢画面） */
  const southX=[-13,-6.5,0,6.5,13];
  for(let i=0;i<southX.length;i++){
    const b0=new THREE.BoxGeometry(1.25,0.45,1.25);
    b0.translate(southX[i],1.83,9.0); B.put(b0,0x1f2836);
    const c0=new THREE.CylinderGeometry(0.40,0.46,8.7,8);
    c0.translate(southX[i],6.30,9.0); B.put(c0,0x2e2730);
  }
  const eastZ=[-15,-10,-5,0,5];
  for(let i=0;i<eastZ.length;i++){
    const b1=new THREE.BoxGeometry(1.25,0.45,1.25);
    b1.translate(13.8,1.83,eastZ[i]); B.put(b1,0x1f2836);
    const c1=new THREE.CylinderGeometry(0.40,0.46,8.7,8);
    c1.translate(13.8,6.30,eastZ[i]); B.put(c1,0x2c262e);
  }
  /* 帝座高台 + 座后屏板（北端） */
  const dais=new THREE.BoxGeometry(9,1.0,4.5);
  dais.translate(0,2.27,-17); B.put(dais,0x242e3e);
  const scr=new THREE.BoxGeometry(10,5.6,0.5);
  scr.translate(0,5.0,-18.9); B.put(scr,0x1b2432);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x9ab8d8,i:o.rim===undefined?0.12:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 铜烛台 makeZhutai(o)：座+柱+承盘+素烛（合批 1 mesh）+焰（makeFlame）+暖晕 Sprite
  [+可选 1 PointLight]——「烛影」「夜半」的光源本体；暖晕初值=最大（fadeK 铁律），
  flare 只在初值以内起伏，点击烛影摇动时焰宽 uWide 加大、暖晕升到顶 */
function makeZhutai(o){
  o=o||{};
  const B=new GeoBag();
  const ft=new THREE.CylinderGeometry(0.34,0.42,0.14,10);
  ft.translate(0,0.07,0); B.put(ft,0x3a3328);
  const st=new THREE.CylinderGeometry(0.05,0.08,1.9,7);
  st.translate(0,1.02,0); B.put(st,shadeColor(0x3a3328,1.12));
  const dish=new THREE.CylinderGeometry(0.26,0.18,0.10,9);
  dish.translate(0,2.02,0); B.put(dish,0x443c2e);
  const wax=new THREE.CylinderGeometry(0.085,0.095,o.wax===undefined?0.46:o.wax,8);
  wax.translate(0,2.02+(o.wax===undefined?0.46:o.wax)*0.5,0); B.put(wax,0xd8d2c4);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0x6a5a3a,emissive:0x080604}),{c:0xffb066,i:0.22,p:2.6})));
  const fl=makeFlame({h:0.72,w:0.26,planes:2,embers:9,spark:false,wide:o.wide===undefined?0.30:o.wide,
    core:0xffe2a8,outer:0xff8a3a,seed:o.seed===undefined?3.3:o.seed,light:o.light||0,lightD:36,lightC:0xffc290});
  fl.g.position.y=2.24+(o.wax===undefined?0.46:o.wax); g.add(fl.g);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb066,
    transparent:true,opacity:0.5,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(9,9,1); glow.position.y=2.9+(o.wax===undefined?0.46:o.wax)*0.4;
  glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?3.3:o.seed)%6.283;
  g.update=function(t,k,flare){
    const kk=k===undefined?1:k, fr=flare===undefined?0:flare;
    fl.update(t,kk);
    fl.mat.uniforms.uWide.value=(o.wide===undefined?0.30:o.wide)+0.42*fr;
    glow.material.opacity=kk*0.5*(0.62+0.18*Math.sin(t*4.7+ph)+0.20*fr);
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 席 makeXitan(w,d)：席地而坐的席（席面+缘边，合批 1 mesh）——「前席」的席 */
function makeXitan(w,d){
  const B=new GeoBag();
  const m1=new THREE.BoxGeometry(w,0.14,d);
  m1.translate(0,0.07,0); B.put(m1,0x2b3040);
  const m2=new THREE.BoxGeometry(w+0.16,0.05,d+0.16);
  m2.translate(0,0.025,0); B.put(m2,0x3c4456);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36445c,emissive:0x05070c}),{c:0x9ab8d8,i:0.10,p:2.4})));
  return g;
}

/* —— 宫墙阙楼 makeGongyuan(o)：殿外宫墙（墙身+墙帽+阙楼+角墩，合批 1 mesh）——
   殿外夜色的冷剪影；水墨剪影吃雾，与殿内烛光成冷暖对切 */
function makeGongyuan(o){
  o=o||{};
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(1.6,7.5,40);
  wall.translate(0,3.75,0); B.put(wall,0x0e1522);
  const cap=new THREE.BoxGeometry(2.0,0.42,40.6);
  cap.translate(0,7.7,0); B.put(cap,0x111a28);
  const qb=new THREE.BoxGeometry(4.5,1.2,4.5);
  qb.translate(-1.2,0.6,16); B.put(qb,0x0d1420);
  const qbd=new THREE.BoxGeometry(3.2,3.4,3.2);
  qbd.translate(-1.2,2.9,16); B.put(qbd,0x101827);
  const qrf=new THREE.ConeGeometry(2.9,1.5,4);
  qrf.rotateY(Math.PI/4); qrf.translate(-1.2,5.35,16); B.put(qrf,0x0c121d);
  const jiao=new THREE.BoxGeometry(2.6,3.0,2.6);
  jiao.translate(-0.6,1.5,-17); B.put(jiao,0x0d1420);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x303c50,emissive:0x04060a}),{c:0x9ab8d8,i:o.rim===undefined?0.15:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 苍生剪影 makeCangsheng(o)：殿外宫墙下的黎民百姓（crowdGeo InstancedMesh，1 draw call；
   组 visible=false 硬关——点击前无幻影）；rv 0→1：淡现（0.10~0.38）→伫立（0.38~0.55）→
   散去（0.55~1，如夜雾消散）——「不问苍生」：被冷落的人在门外 */
function makeCangsheng(o){
  o=o||{};
  const n=o.n===undefined?9:o.n;
  const rect=o.rect===undefined?[17,-9,9,12]:o.rect;
  const g=new THREE.Group(), items=[];
  const R=seedRnd(o.seed===undefined?23011:o.seed);
  const mesh=new THREE.InstancedMesh(crowdGeo(),
    new THREE.MeshBasicMaterial({color:o.color===undefined?0x2a3648:o.color,
      transparent:true,opacity:0.85,depthWrite:false}),n);
  mesh.frustumCulled=false;
  const dm=new THREE.Object3D();
  for(let i=0;i<n;i++){
    const x=rect[0]+R()*rect[2], z=rect[1]+R()*rect[3];
    items.push({x:x,z:z,s:0.50+0.16*R(),ry:(R()-0.5)*1.2,ph:R()*6.283});
  }
  g.add(mesh); g.visible=false;
  const sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const appear=sm01((r-0.10)/0.28), dis=1-sm01((r-0.55)/0.45);
    const env=Math.min(appear,dis), drift=Math.max(0,(r-0.55)/0.45);
    for(let i=0;i<n;i++){
      const it=items[i];
      dm.position.set(it.x+drift*(0.8+it.ph*0.2),drift*1.6,it.z);
      dm.rotation.set(0,it.ry+0.02*Math.sin(t*0.3+it.ph),0);
      dm.scale.setScalar(it.s); dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mesh.material.opacity=kk*0.85*env*(0.86+0.14*Math.sin(t*0.7));
    g.visible=kk*r>0.004&&env>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 鬼神异光 makeGuangyan(o)：殿心沉落的冷异光（垂直光柱 Sprite+冷晕+微尘 points，
   均 fog:false/着色器；组 visible=false 硬关，初值=最大）——「问鬼神」：话题转向时
   殿内那层阴翳的冷光 */
function makeGuangyan(o){
  o=o||{};
  const g=new THREE.Group();
  const shaft=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),
    color:o.color===undefined?0x9ab8d8:o.color,transparent:true,opacity:0.30,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  shaft.scale.set(9,30,1); shaft.position.set(0,7,-1); shaft.renderOrder=4; g.add(shaft);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8fb2d8,
    transparent:true,opacity:0.20,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(30,24,1); halo.position.set(0,7.6,-1); halo.renderOrder=4; g.add(halo);
  const motes=makeGlow({n:22,box:[9,8,9],pos:[0,8,-1],color:0xa8c4e0,size:3.0,speed:0.10,
    rise:-0.5,add:false,maxA:0.16});
  motes.points.renderOrder=4; g.add(motes.points);
  g.visible=false;
  const sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const rise=sm01((r-0.30)/0.30);
    const dim=1-0.35*sm01((r-0.85)/0.15);
    shaft.material.opacity=kk*0.30*rise*(0.86+0.14*Math.sin(t*0.9))*dim;
    halo.material.opacity=kk*0.20*rise*(0.80+0.20*Math.sin(t*0.6+1.4))*dim;
    motes.mat.uniforms.uMaxA.value=0.16*rise*dim;
    motes.mat.uniforms.uFade.value=kk;
    motes.update(t);
    g.visible=kk*r>0.004&&rise>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* 君臣二人：全诗贯穿的同一造型（每次 build 新建材质）——文帝玄衣束带、年而有须；
   贾生青衿少年、危坐欲言 */
function jsFigure(scale,pose,opt){
  opt=opt||{};
  return makeFigure({pose:pose||'坐饮',robe:opt.robe||0x272e3e,belt:opt.belt||0x6f7d92,
    skin:0xd3b294,collar:opt.collar||0x8c98ac,hair:0x12161e,hat:opt.hat||'发髻',beard:!!opt.beard,
    rimC:0x9ab8d8,rim:0.42,noProp:true,scale:scale===undefined?1.5:scale});
}

/* 远山一环 makeYaoshan(o)：殿外天际的低平山脊（两层，带雾骨相）——透过东廊看到的
   夜色深处；组放近（z≈-80），不被骨架常驻远山环（z≈-300）遮挡 */
function makeYaoshan(o){
  o=o||{};
  return makeRange({r:o.r===undefined?210:o.r,h:o.h===undefined?15:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?23021:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x1f2b3a,
    fogK:o.fogK===undefined?0.60:o.fogK,glowK:0.05,glow:0xaebccd,
    y:o.y===undefined?-4:o.y,order:-6});
}

function bCover(){ // 卷首 · 宣室夜召：高台大殿烛光透门，阙楼宫墙横陈，冷月斜挂，逐臣只身赴召
  const g=new THREE.Group();
  const grd=makeGround({r:95,c1:0x0a0f17,c2:0x141b28,y:-0.03}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.03,10);
  const ridge=makeYaoshan({r:250,h:14,y:-8,seed:23022}); ridge.g.position.set(0,0,-175); g.add(ridge.g);
  /* 宣室大殿 + 殿内帷幔帝座（透过南檐列柱可见一层纵深） */
  const hall=makeXuanshi({rim:0.14}); hall.position.set(0,0,0); g.add(hall);
  const cm1=makeLian({w:15,h:8,folds:8,color:0x252c3a,dark:0x0a0d13});
  cm1.g.position.set(0,1.77,-18.2); g.add(cm1.g);
  const cm2=makeLian({w:7,h:8,folds:5,color:0x232a38,dark:0x0a0c11});
  cm2.g.position.set(12.4,1.77,-5.5); cm2.g.rotation.y=Math.PI/2; g.add(cm2.g);
  /* 席案与烛台：殿心一点暖 */
  const xt1=makeXitan(3.1,2.3); xt1.position.set(-2.9,1.77,-7.5); g.add(xt1);
  const xt2=makeXitan(3.0,2.2); xt2.position.set(3.1,1.77,-7.5); g.add(xt2);
  const poet=jsFigure(1.05,'独立',{robe:0x2a3344}); poet.position.set(2.2,0.02,16.5);
  poet.rotation.y=Math.PI; g.add(poet);
  const zt1=makeZhutai({seed:1.7,light:1.2}); zt1.g.position.set(-6.2,1.77,-4.6); g.add(zt1.g);
  const zt2=makeZhutai({seed:4.2}); zt2.g.position.set(5.8,1.77,-4.6); g.add(zt2.g);
  /* 殿门暖晕（宣室夜里唯一的光） */
  const dglow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb066,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dglow.scale.set(30,14,1); dglow.position.set(0,5.2,9.4); dglow.renderOrder=3; g.add(dglow);
  /* 殿外：宫墙阙楼（殿后横陈一列，双阙对峙） */
  const gy1=makeGongyuan({scale:1.35}); gy1.position.set(0,0,-37); gy1.rotation.y=Math.PI/2; g.add(gy1);
  const gy2=makeGongyuan({scale:1.2}); gy2.position.set(0,0,-40); gy2.rotation.y=-Math.PI/2; g.add(gy2);
  const mist=makeMist({n:5,spread:[120,12,60],pos:[0,3.4,-20],scale:44,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[80,16,50],pos:[0,10,8],color:0xaebccd,size:4.0,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:12,d:5,color:0x05080e,seed:23023,rim:0.10,rimC:0x9ab8d8});
  fg1.g.position.set(-13,-1.4,20); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:16,n:5,d:4,color:0x05080e,seed:23024,sway:0.7,rim:0.09,rimC:0x9ab8d8});
  fg2.g.position.set(13,-1.6,20); g.add(fg2.g);
  addLights(g,{c:0xa8bad0,i:0.30,p:[-40,55,-40]},{c:0x1b2433,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); ridge.update(t,0);
    poet.update(t,k); zt1.update(t,k,0); zt2.update(t,k,0);
    dglow.material.opacity=k*0.16*(0.85+0.15*Math.sin(t*1.1));
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bFangxian(){ // 壹 · 宣室访贤 —— 宣室求贤访逐臣，贾生才调更无伦：殿内斜望，君臣对坐烛光殷勤
  const g=new THREE.Group();
  const grd=makeGround({r:95,c1:0x0a0f17,c2:0x141b28,y:-0.03}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.03,10);
  const ridge=makeYaoshan({seed:23025}); ridge.g.position.set(80,0,-80); g.add(ridge.g);
  /* 宣室大殿 */
  const hall=makeXuanshi({rim:0.13}); hall.position.set(0,0,0); g.add(hall);
  /* 帝座帷幔（左上背景）+ 东廊半掩帘 */
  const cm1=makeLian({w:15,h:8,folds:8,color:0x252c3a,dark:0x0a0d13});
  cm1.g.position.set(0,1.77,-18.2); g.add(cm1.g);
  const cm2=makeLian({w:7,h:8,folds:5,color:0x232a38,dark:0x0a0c11});
  cm2.g.position.set(12.4,1.77,-5.5); cm2.g.rotation.y=Math.PI/2; g.add(cm2.g);
  /* 君臣对坐：文帝玄衣按杯（西席），贾生青衿危坐（东席），中间一案樽爵 */
  const wd=new THREE.Group();
  wd.add(makeXitan(3.1,2.3));
  const wdi=jsFigure(1.62,'坐饮',{robe:0x232938,belt:0x8a7448,collar:0x9aa2b4,hat:'无',beard:true});
  wdi.position.set(0,0.76,0); wdi.rotation.y=Math.PI/2; wd.add(wdi);
  wd.position.set(-2.9,0,-7.5); g.add(wd);
  const js=new THREE.Group();
  js.add(makeXitan(3.0,2.2));
  const jsf=jsFigure(1.5,'坐饮',{robe:0x2a3344,belt:0x5f6e84,collar:0xa8b2c2});
  jsf.position.set(0,0.76,0); jsf.rotation.y=-Math.PI/2; js.add(jsf);
  js.position.set(3.1,0,-7.5); g.add(js);
  const an=makeTable({w:2.6,d:1.2,h:0.85,wood:0x241a14}); an.g.position.set(0.1,1.77,-8.3); g.add(an.g);
  const vz1=makeVessel({type:'樽',mat:'陶',color:0x4a4038,scale:0.8});
  vz1.g.position.set(-0.5,2.62,-8.3); g.add(vz1.g);
  const vz2=makeVessel({type:'爵',mat:'陶',color:0x4a4038,scale:0.8});
  vz2.g.position.set(0.5,2.62,-8.1); g.add(vz2.g);
  const vz3=makeVessel({type:'盘',mat:'陶',color:0x3c3630,scale:0.75});
  vz3.g.position.set(0.3,2.62,-8.6); g.add(vz3.g);
  /* 铜烛台一双：全页唯一的暖（一盏带 PointLight） */
  const zt1=makeZhutai({seed:2.3,light:1.4}); zt1.g.position.set(-6.2,1.77,-4.6); g.add(zt1.g);
  const zt2=makeZhutai({seed:5.1}); zt2.g.position.set(5.8,1.77,-4.6); g.add(zt2.g);
  /* 殿外夜色：宫墙阙楼冷剪影 + 东廊开口一泓冷光（殿内暖烛的冷对切；
     夜半低月由 STAGES 天空月担任，位置贴着宫墙脊可见） */
  const gy=makeGongyuan({scale:1.35}); gy.position.set(30,0,-3); g.add(gy);
  const menjing=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9ab8d8,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  menjing.scale.set(34,17,1); menjing.position.set(24,5.5,-2); menjing.renderOrder=2; g.add(menjing);
  const mist=makeMist({n:4,spread:[40,8,36],pos:[0,4.5,-8],scale:26,color:0x2a3648,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[30,9,30],pos:[0,6,-8],color:0xc9b28a,size:3.4,speed:0.05,rise:0.05,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x05080e,seed:23026,rim:0.09,rimC:0x9ab8d8});
  fg1.g.position.set(-13.5,-1.2,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:22,h:3.0,color:0x05080e,seed:23027,rim:0.08,rimC:0x9ab8d8});
  fg2.g.position.set(3,-2.6,16.5); g.add(fg2.g);
  addLights(g,{c:0xa8bad0,i:0.26,p:[52,46,-24]},{c:0x1b2433,i:0.46});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); ridge.update(t,0);
    wd.children[1].update(t,k); js.children[1].update(t,k);
    zt1.update(t,k,0); zt2.update(t,k,0);
    menjing.material.opacity=k*0.10*(0.85+0.15*Math.sin(t*0.5));
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bQianxi(){ // 贰（末境·可点击）· 夜半前席 —— 可怜夜半虚前席，不问苍生问鬼神：
                    // 点击：烛影摇动+文帝连席前移+殿内冷异光沉落+殿外苍生淡现又散（前席的错位）
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:95,c1:0x0a0f17,c2:0x141b28,y:-0.03}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.03,10);
  const ridge=makeYaoshan({seed:23028}); ridge.g.position.set(80,0,-80); g.add(ridge.g);
  const hall=makeXuanshi({rim:0.12}); hall.position.set(0,0,0); g.add(hall);
  const cm1=makeLian({w:15,h:8,folds:8,color:0x252c3a,dark:0x0a0d13});
  cm1.g.position.set(0,1.77,-18.2); g.add(cm1.g);
  const cm2=makeLian({w:7,h:8,folds:5,color:0x232a38,dark:0x0a0c11});
  cm2.g.position.set(12.4,1.77,-5.5); cm2.g.rotation.y=Math.PI/2; g.add(cm2.g);
  /* 君臣对坐（夜半烛短：素烛更短小）；文帝组=前席的可动组（席与人一起前移） */
  const wd=new THREE.Group();
  wd.add(makeXitan(3.1,2.3));
  const wdi=jsFigure(1.62,'坐饮',{robe:0x232938,belt:0x8a7448,collar:0x9aa2b4,hat:'无',beard:true});
  wdi.position.set(0,0.76,0); wdi.rotation.y=Math.PI/2; wd.add(wdi);
  wd.position.set(-2.9,0,-7.5); g.add(wd);
  const js=new THREE.Group();
  js.add(makeXitan(3.0,2.2));
  const jsf=jsFigure(1.5,'坐饮',{robe:0x2a3344,belt:0x5f6e84,collar:0xa8b2c2});
  jsf.position.set(0,0.76,0); jsf.rotation.y=-Math.PI/2; js.add(jsf);
  js.position.set(3.1,0,-7.5); g.add(js);
  const an=makeTable({w:2.6,d:1.2,h:0.85,wood:0x241a14}); an.g.position.set(0.1,1.77,-8.3); g.add(an.g);
  const vz1=makeVessel({type:'樽',mat:'陶',color:0x4a4038,scale:0.8});
  vz1.g.position.set(-0.5,2.62,-8.3); g.add(vz1.g);
  const vz2=makeVessel({type:'爵',mat:'陶',color:0x4a4038,scale:0.8});
  vz2.g.position.set(0.5,2.62,-8.1); g.add(vz2.g);
  /* 烛影摇动的主角烛台（flare 由点击驱动） */
  const zt1=makeZhutai({seed:3.3,light:1.3,wax:0.30}); zt1.g.position.set(-6.2,1.77,-4.6); g.add(zt1.g);
  const zt2=makeZhutai({seed:6.2,wax:0.30}); zt2.g.position.set(5.8,1.77,-4.6); g.add(zt2.g);
  /* 殿外夜色 + 宫墙 + 东廊开口冷光（夜半低月由 STAGES 天空月担任；
     冷光初值=最大，点击后升至顶——fadeK 铁律） */
  const gy=makeGongyuan({scale:1.35}); gy.position.set(30,0,-3); g.add(gy);
  const menjing=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9ab8d8,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  menjing.scale.set(34,17,1); menjing.position.set(24,5.5,-2); menjing.renderOrder=2; g.add(menjing);
  /* 标志性交互：鬼神异光（点击前 visible=false 硬关）+ 殿外苍生（同） */
  const gyy=makeGuangyan({}); gyy.position.set(0.5,0,-9); g.add(gyy);
  const cs=makeCangsheng({n:9,rect:[17,-9,9,12],seed:23029}); g.add(cs);
  const mist=makeMist({n:4,spread:[40,8,36],pos:[0,4.5,-8],scale:26,color:0x2a3648,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[30,9,30],pos:[0,6,-8],color:0xc9b28a,size:3.4,speed:0.05,rise:0.05,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'栏杆',w:24,h:3.0,color:0x05080e,seed:23030,rim:0.09,rimC:0x9ab8d8});
  fg1.g.position.set(-2,-2.8,13.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:10,d:4,color:0x05080e,seed:23031,rim:0.09,rimC:0x9ab8d8});
  fg2.g.position.set(10,-1.4,14.5); g.add(fg2.g);
  addLights(g,{c:0xa8bad0,i:0.22,p:[52,42,-24]},{c:0x1b2433,i:0.40});
  const WD_X0=-2.9, sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/6.0);
      const rv=ctl.reveal;
      const fw=sm01(rv/0.40);                    // 前席：文帝连席前移（0~0.40 段滑完）
      wd.position.x=WD_X0+fw*1.8;
      const e=rv*rv*(3-2*rv);
      zt1.update(t,k,e); zt2.update(t,k,e);      // 烛影摇动（焰宽+暖晕）
      gyy.update(t,k,rv);                        // 殿内冷异光沉落（鬼神之问）
      cs.update(t,k,rv);                         // 殿外苍生淡现又散（不问苍生）
      wd.children[1].update(t,k); js.children[1].update(t,k);
      menjing.material.opacity=k*0.16*(0.55+0.10*Math.sin(t*0.5)+0.35*e);
      mist.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); ridge.update(t,0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.14);
        pluck(0,0.05,0.12); pluck(3,0.70,0.09); pluck(1,1.40,0.08);   // 冷弦三叠，如夜半问对
        const fl=$('#flash'); fl.textContent='可怜夜半虚前席 不问苍生问鬼神';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x060a12),hor:C(0x1a2434),bot:C(0x04070c),fog:C(0x121a26),fd:0.0048,star:0.24,
  moon:new THREE.Vector3(-52,58,-160),ms:1.15,mph:0.55,mhaze:0.16,dirC:C(0xa8bad0),dirI:0.30,
  dirP:new THREE.Vector3(-40,55,-40),ambC:C(0x1b2433),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9.6,48],t:[0,9.2,42],lf:[0,7.6,-4],lt:[0,8.2,-24]},
  sky:()=>SK({fd:0.0048,star:0.24,ms:1.15,moon:new THREE.Vector3(-52,58,-160),mph:0.55}) },
{ name:'宣室访贤',dwell:16,river:0.02,build:bFangxian,
  cam:{f:[-11.5,7.4,13.5],t:[-9.8,7.0,12.0],lf:[6,4.2,-12],lt:[9,4.4,-20]},
  sky:()=>SK({fd:0.0060,star:0.06,ms:0.50,mhaze:0.12,
    moon:new THREE.Vector3(62,15,-40),dirC:C(0xa8bad0),dirI:0.26,
    dirP:new THREE.Vector3(52,46,-24),ambC:C(0x1b2433),ambI:0.46}) },
{ name:'夜半前席',dwell:19,river:0.02,build:bQianxi,
  cam:{f:[-9.5,6.4,5.0],t:[-8.6,6.1,3.4],lf:[10,3.6,-10],lt:[13,3.8,-16]},
  sky:()=>SK({fd:0.0072,star:0.03,ms:0.42,mhaze:0.12,
    moon:new THREE.Vector3(58,16,-36),dirC:C(0xa8bad0),dirI:0.22,
    dirP:new THREE.Vector3(52,42,-24),ambC:C(0x1b2433),ambI:0.40}) },
];
"""
