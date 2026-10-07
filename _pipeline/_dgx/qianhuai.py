# -*- coding: utf-8 -*-
"""qianhuai.py —— 《遣怀》（唐·杜牧，queue no.232，夜宴金彩·扬州梦华变体）生成配置
两境（N=queue stages 数）：载酒江湖（落魄江湖载酒行·楚腰纤细掌中轻——水岸歌台灯影+舞袖剪影）、
梦醒扬州（十年一觉扬州梦·赢得青楼薄幸名——标志性瞬间「大梦初醒的灯影」+末境点击）。
夜宴金彩全套色板（赛道分配 accent=#d4a84f，落拓鎏金）：底色 #05070d、雾 #181009 系暖夜褐金、
文字 #e8dcc0。本诗的夜不是《将进酒》殿内豪宴、《过华清宫》骊山晚照、《海棠》夜庭一烛——
是「江湖水岸的繁华灯影」：临水歌台、沿岸灯串、泊岸画舫、斜挑酒旗；全页题眼是
「大梦初醒的灯影」——人已醒，梦未散：末境近处空案残樽（清醒），远处歌台灯影仍亮（梦境）。
标志性瞬间（境贰·queue moment：十年一觉扬州梦——大梦初醒的灯影）：空案残樽在前、
十年灯影在后，清醒与繁华同框对望。
末境点击（queue interact：点击扬州梦——灯影繁华如潮退去+梦醒空案）：点击画面——
①沿岸灯串与水中灯影如潮退去（按相位次第熄灭，由远及近退成一线、终至全暗）；
②清辉江月淡入（冷白横带+水面清辉微光，fog:false 点名）——繁华褪尽，只余清醒江月；
③诗人缓缓转身向月（rotation 微移）；④「十年一觉扬州梦 赢得青楼薄幸名」题字同现。
「青楼」意象含蓄雅化：只做灯影歌台与背光舞袖剪影（远景、不画具体艳俗场景）——教学对象是中学生。
考点钉子：落魄 tuò／一觉 jiào（小测第 3 题落点）；楚腰（楚王好细腰）/掌中轻（赵飞燕掌上舞）+
杜牧扬州幕僚生涯（第 4 题）；「十年一觉」自嘲与追悔的主旨（第 5 题）。
多音字：落魄→落托 一觉→一叫 薄幸→博幸（tts.json，防「魄 pò／觉 jué／薄 báo」误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='qianhuai', title='遣怀', dyn='唐 · 杜牧', brand_author='杜 牧',
    gold_rgb='212,168,79',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#d4a84f; --ink:#e8dcc0; --dim:#9a8a70; --paper:rgba(14,10,7,.60);
  --line:rgba(212,168,79,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('rgba(5,8,15', 'rgba(9,7,4', 1),
        ('rgba(4,6,11', 'rgba(8,6,3', 2),
        ('rgba(6,9,16', 'rgba(10,7,4', 1),
        ('rgba(3,5,9', 'rgba(6,4,3', 1),
        ('#0b101c', '#151009', 1),
        ('#6f664f', '#6b5c46', 1),
        ('#5a5340', '#5f5442', 1),
    ],
    tip='轻点画面 / 按空格 —— 灯影繁华如潮退去，梦醒空案',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看灯影繁华如潮退去，梦醒空案、清辉满江',
    cover_read='遣怀。唐，杜牧。落魄江湖载酒行，楚腰纤细掌中轻。十年一觉扬州梦，赢得青楼薄幸名。',
    cover_p1='两重意境，随诗句次第展开：落魄江湖，载酒漫游——歌台灯影摇曳，舞女腰细身轻，何等繁华热闹；十年扬州岁月恍如一觉大梦，惊醒之后细细盘点，自己竟什么也没有赢得，只落得青楼歌女口中的一个「薄幸」名声。',
    cover_p2='边读诗，边跟着杜牧从灯影繁华中醒来：一场大梦、一声自嘲——读懂「十年一觉」的追悔，就读懂了这首失意文人的遣怀之作。',
    end_h2='梦醒 · 空案', cn_word='两',
    words_js="['再泛一次江湖','初识樊川，尚需共读','渐入诗境，再诵几遍','灯影渐暖，歌台渐近','已解十年梦醒之意','梦醒空案，月满江湖']",
    sky_atmo='0x33261a',
)

POEM_JS = """const POEM = [
{ name:'载酒江湖', jing:'落魄江湖，载酒漫游；歌台灯影里，楚女腰身纤细、体态轻盈，仿佛能在掌上起舞 —— 落魄、载酒、楚腰、掌中轻。（水岸歌台 · 灯影 · 舞袖）',
  segs:[
   {c:'落魄江湖载酒行，', p:py('luò tuò jiāng hú zài jiǔ xíng')},
   {c:'楚腰纤细掌中轻。', p:py('chǔ yāo xiān xì zhǎng zhōng qīng')}],
  read:'落魄江湖载酒行，楚腰纤细掌中轻。',
  yisi:'失意潦倒，漂泊江湖，只好带着酒四处漫游；歌台灯影里，歌女腰身纤细、体态轻盈，仿佛能在手掌上翩翩起舞。——起句自叙落拓：一个「落魄」、一个「载酒」，把失意文人的漂泊写尽——仕途不得意，只好以酒相伴、浪迹江湖。次句荡开一笔，写扬州歌台上的繁华：「楚腰」用楚王好细腰之典，「掌中轻」用赵飞燕能作掌上舞之典，腰细、身轻二典连用，极写当年宴游的声色之乐。然而越是写得热闹，越见出后面的悲凉——这正是以乐景写哀情。',
  zhu:[['遣怀','排遣感怀之作——杜牧晚年追忆扬州幕僚岁月、自嘲自省的诗。遣，抒发、排遣'],['落魄','穷困失意、漂泊不得志。魄，读 tuò——「落魄江湖」即失意潦倒、浪迹四方'],['江湖','江河湖海，指仕途之外四处漂泊的世界——与朝廷庙堂相对'],['载酒行','带着酒远行漫游。载，装载、带着——以酒相伴的漂泊生活'],['楚腰','用楚王好细腰的典故（楚灵王喜欢细腰，宫中人争相饿瘦以讨好）——代指美人纤细的腰身，此指扬州歌女'],['掌中轻','用赵飞燕「体轻，能为掌上舞」的典故——形容舞女身轻如燕']] },
{ name:'梦醒扬州', jing:'十年扬州岁月，恍如一觉大梦；梦醒之后细细盘点，竟只赢得青楼歌女口中的一个「薄幸」名声 —— 一觉、扬州梦、薄幸名。（标志性瞬间：大梦初醒的灯影）（末境点击画面：灯影繁华如潮退去，梦醒空案）',
  segs:[
   {c:'十年一觉扬州梦，', p:py('shí nián yī jiào yáng zhōu mèng')},
   {c:'赢得青楼薄幸名。', p:py('yíng dé qīng lóu bó xìng míng')}],
  read:'十年一觉扬州梦，赢得青楼薄幸名。',
  yisi:'十年扬州岁月，恍如一觉大梦；梦醒之后细细盘点，竟什么也没有「赢得」，只落得一个青楼歌女口中的「薄幸」名声。——这是全诗的落点，也是千古传诵的自嘲名句：「十年」与「一觉」对举，十年繁华被压缩成一场睡梦，极言人生如梦之痛切；「赢得」二字看似轻松，实为沉痛——十年蹉跎，功业无成，换来的竟是「薄幸」的浮名。诗人以「薄幸」自嘲，伤的是怀才不遇、壮志消磨；调侃的口吻里，藏着深深的追悔与失意。',
  zhu:[['十年一觉','十年光阴，恍如一觉大梦。觉，读 jiào——睡一觉；「一觉」与「十年」对举，繁华顿成隔世'],['扬州梦','唐代扬州为淮南重镇、商业繁华之都，时有「扬一益二」之称；杜牧二十多岁入淮南节度使幕府任掌书记，在扬州度过数年幕僚生活，此句即追忆那段岁月如梦'],['赢得','剩得、落得——自嘲之词：十年「换来」的，竟然只是……'],['青楼','这里指华美的楼房，唐人多代指歌楼（与后世专指妓院不同）——当年宴游之地'],['薄幸','薄情、负心。幸，宠爱——歌女们眼中的「薄情郎」，是诗人给自己的自嘲评语'],['自嘲','以嘲弄自己的口吻作诗——表面调侃「赢得薄幸名」，骨子里是怀才不遇的追悔与失意']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「落魄江湖载酒行」的下一句是？', o:['楚腰纤细掌中轻','十年一觉扬州梦','赢得青楼薄幸名'], a:0},
 {q:'「十年一觉扬州梦」的下一句是？', o:['楚腰纤细掌中轻','赢得青楼薄幸名','落魄江湖载酒行'], a:1},
 {q:'「落魄江湖载酒行」的「魄」与「十年一觉扬州梦」的「觉」，读音都正确的一项是？', o:['魄读 tuò（落魄：穷困失意、漂泊无依）；觉读 jiào（一觉：睡一大觉，一觉醒来）','魄读 pò（魂魄）；觉读 jué（觉悟、察觉）','魄读 bó（通「薄」，淡薄）；觉读 jiào（觉察）'], a:0},
 {q:'「楚腰纤细掌中轻」连用两个典故，「十年一觉扬州梦」又与杜牧的经历相关。下列说法正确的是？', o:['「楚腰」用楚王好细腰之典，代指歌女纤细腰身；「掌中轻」用赵飞燕能作掌上舞之典，形容体态轻盈——两句极写扬州歌筵的繁华；杜牧年轻时曾任淮南节度使幕府掌书记，在扬州度过数年幕僚生涯，晚年追忆便成了这场「扬州梦」','「楚腰」指楚地产的腰带，「掌中轻」指手掌轻巧——两句写扬州手工业品的精巧；杜牧在扬州经商十年','「楚腰」「掌中轻」都是写诗人自己腰细身轻、善于舞蹈——这首诗是杜牧自述舞艺的自夸之作'], a:0},
 {q:'对「十年一觉扬州梦，赢得青楼薄幸名」的理解，最恰当的一项是？', o:['以「一觉」写十年繁华如大梦初醒，以「赢得」自嘲：十年蹉跎、功业无成，竟只落得青楼「薄幸」的浮名——看似调侃，实含追悔与失意，是失意文人的沉痛自省','诗人得意地炫耀自己在扬州风流十年、名声远扬，表达对这段生活的自豪与留恋','「青楼」在这里指朝廷官署，「薄幸名」指清廉的名声——两句写诗人十年为官清慎、口碑载道'], a:0},
];
"""

SCENES_JS = """/* ================= 遣怀 · 两境场景（夜宴金彩·扬州梦华变体：卷首江湖夜泊、载酒江湖、梦醒扬州） =================
   美术立意：夜宴金彩色板写「扬州十年梦」——底色 #05070d、雾 #181009 系暖夜褐金，
   accent=#d4a84f（queue 分配强调色，落拓鎏金）只落在歌台灯串/水面灯影/酒旗灯晕/人物边缘光/UI 上。
   本页的夜是「江湖水岸的繁华灯影」：临水歌台、沿岸灯串、泊岸画舫、斜挑酒旗；
   全页题眼是「大梦初醒的灯影」——人已醒，梦未散：末境近处空案残樽（清醒），
   远处歌台灯影仍亮（梦境），点击后灯影如潮退去、清辉江月淡入，只余清醒江月与空案。
   「青楼」含蓄雅化：只做灯影歌台与背光舞袖剪影（远景，不画具体艳俗场景）。
   与已有夜宴金彩页第一眼可区分：不做殿内宴席酒器星河（jiangjinjiu）、不做骊山宫门红尘驿马
   （guohuaqinggong）、不做夜庭高烛海棠（haitang）——做「水岸歌台灯影+十年梦醒」的落拓追悔。 */

/* —— 临水歌台 makeGetaiJS(o)：水岸台基+前阶+四柱+歇山小顶+矮栏（合批 1 mesh）——
   「歌台」：楚腰舞影所在——远景灯影中的水岸戏台，含蓄雅化 */
function makeGetaiJS(o){
  o=o||{};
  const w=o.w===undefined?11:o.w, d=o.d===undefined?8:o.d;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w,1.1,d); base.translate(0,0.55,0); B.put(base,0x241a10);
  const fl=new THREE.BoxGeometry(w*0.94,0.18,d*0.92); fl.translate(0,1.16,0); B.put(fl,0x2e2115);
  for(let i=0;i<2;i++){
    const st=new THREE.BoxGeometry(w*0.30,0.30,0.82);
    st.translate(0,0.92-i*0.30,d/2+0.45+i*0.60); B.put(st,shadeColor(0x241a10,0.9+i*0.14));
  }
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const col=new THREE.CylinderGeometry(0.13,0.17,3.4,7);
    col.translate(sx*w*0.40,2.9,sz*d*0.34); B.put(col,0x35261a);
  }
  const beam=new THREE.BoxGeometry(w*1.04,0.24,d*0.86); beam.translate(0,4.66,0); B.put(beam,0x2a1e13);
  const roof=new THREE.ConeGeometry(w*0.76,1.7,4); roof.rotateY(Math.PI/4);
  roof.scale(1.14,1,0.90); roof.translate(0,5.85,0); B.put(roof,0x1c1209);
  const ridgeB=new THREE.BoxGeometry(w*0.86,0.13,0.52); ridgeB.translate(0,6.76,0);
  B.put(ridgeB,shadeColor(0x4a3018,1.3));
  const railF=new THREE.BoxGeometry(w*0.90,0.09,0.09); railF.translate(0,1.82,d/2-0.28); B.put(railF,0x3c2c1c);
  for(let sx=-1;sx<=1;sx+=2){
    const railS=new THREE.BoxGeometry(0.09,0.09,d*0.82); railS.translate(sx*(w/2-0.24),1.82,0); B.put(railS,0x3c2c1c);
  }
  for(let i=0;i<5;i++){
    const post=new THREE.BoxGeometry(0.10,0.52,0.10); post.translate(-w*0.36+i*w*0.18,1.56,d/2-0.28); B.put(post,0x322416);
  }
  /* 台口两盏小灯体（暖光窗，灯晕由场景 sprite 补） */
  [1,-1].forEach(function(sd){
    const lamp=new THREE.BoxGeometry(0.30,0.42,0.30); lamp.translate(sd*w*0.30,3.35,d*0.30);
    B.put(lamp,0xe8b060);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x5a4224,emissive:0x0c0804}),{c:0xd4a84f,i:o.rim===undefined?0.20:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 酒旗 makeJiuqiJS(o)：竹杆+横挑+酒旗（双面布旗绕杆轻摆；旗 1 mesh + 杆架合批 1 mesh）——
   「载酒行」的招子：水岸一点市声 */
function makeJiuqiJS(o){
  o=o||{};
  const h=o.h===undefined?5.4:o.h;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.06,0.095,h,6); pole.translate(0,h/2,0); B.put(pole,0x3a2c1a);
  const arm=new THREE.CylinderGeometry(0.042,0.042,1.9,5); arm.rotateZ(Math.PI/2);
  arm.translate(0.68,h-0.62,0); B.put(arm,0x3a2c1a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3a24,emissive:0x0a0704}),{c:0xd4a84f,i:0.18,p:2.4})));
  const flag=new THREE.Mesh(new THREE.PlaneGeometry(1.5,2.2,4,6),
    new THREE.MeshPhongMaterial({color:0xcdb98e,side:THREE.DoubleSide,shininess:4,
      emissive:0x241c10,transparent:true,opacity:0.96}));
  flag.position.set(1.42,h-1.82,0); flag.renderOrder=1; g.add(flag);
  const ph=(o.seed===undefined?23251:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    flag.rotation.y=0.30*Math.sin(t*0.85+ph)+0.10;
    flag.rotation.z=0.05*Math.sin(t*1.3+ph*1.4);
    flag.material.opacity=kk*0.96;
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 画舫 makeHuafangJS(o)：泊岸画舫（船体+两头翘+竹篷半拱+一盏灯，合批 1 mesh + 灯晕 1 sprite；
   update 随水轻摇）——「载酒行」的舟楫 */
function makeHuafangJS(o){
  o=o||{};
  const L=o.L===undefined?7.6:o.L;
  const B=new GeoBag();
  const hull=new THREE.BoxGeometry(L,0.72,2.05); hull.translate(0,0.40,0); B.put(hull,0x2c2014);
  const bot=new THREE.BoxGeometry(L*0.9,0.22,1.7); bot.translate(0,0.10,0); B.put(bot,0x22180e);
  [1,-1].forEach(function(sd){
    const st=new THREE.BoxGeometry(1.5,0.5,1.7); st.translate(sd*(L*0.5-0.45),0.85,0);
    st.rotateZ(sd*-0.42); B.put(st,shadeColor(0x2c2014,1.08));
  });
  const deck=new THREE.BoxGeometry(L*0.66,0.14,1.86); deck.translate(-L*0.05,0.80,0); B.put(deck,0x352718);
  const peng=new THREE.CylinderGeometry(0.95,0.95,4.1,10,1,false,0,Math.PI);
  peng.rotateZ(Math.PI/2); peng.rotateY(Math.PI/2);
  peng.translate(-L*0.10,1.36,0); B.put(peng,0x3c2c18);
  const lamp=new THREE.BoxGeometry(0.26,0.36,0.26); lamp.translate(L*0.28,1.12,0); B.put(lamp,0xe8b060);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x5a4224,emissive:0x0b0703}),{c:0xd4a84f,i:o.rim===undefined?0.20:o.rim,p:2.4})));
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc478,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(3.4,3.4,1); glow.position.set(L*0.28,1.3,0); glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?23261:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.position.y=Math.sin(t*0.55+ph)*0.10;
    g.rotation.z=0.035*Math.sin(t*0.45+ph*1.3);
    g.rotation.x=0.02*Math.sin(t*0.62+ph*0.7);
    glow.material.opacity=kk*0.30*(0.85+0.15*Math.sin(t*2.1+ph));
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 舞袖人影 makeWuyingJS(o)：歌台上的舞袖剪影（裙锥+细腰身+双长袖，背光灯影；
   1 mesh/人；update 摆袖回身、侧腰微倾）——「楚腰纤细掌中轻」：含蓄雅化为远景剪影 */
function makeWuyingJS(o){
  o=o||{};
  const B=new GeoBag();
  const skirt=new THREE.ConeGeometry(0.42,1.15,8); skirt.translate(0,0.58,0); B.put(skirt,0x191009);
  const body=new THREE.CylinderGeometry(0.125,0.20,0.75,7); body.translate(0,1.50,0); B.put(body,0x1a1209);
  const head=new THREE.SphereGeometry(0.115,7,6); head.translate(0,2.02,0); B.put(head,0x1c1309);
  const bun=new THREE.SphereGeometry(0.075,6,5); bun.translate(0,2.16,-0.03); B.put(bun,0x140d07);
  [1,-1].forEach(function(sd){
    const sleeve=new THREE.ConeGeometry(0.10,1.10,5);
    sleeve.rotateZ(sd*1.92); sleeve.translate(sd*0.36,1.40,0.04); B.put(sleeve,0x1d1409);
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a2c1a,emissive:0x090503}),{c:0xd4a84f,i:o.rim===undefined?0.34:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=(o.seed===undefined?23201:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    mesh.rotation.y=0.5*Math.sin(t*0.55+ph);
    mesh.rotation.z=0.05*Math.sin(t*1.1+ph*1.6);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 岸灯一线 makeAndengJS(o)：沿岸弧线的一串灯火 + 水中灯影（岸灯 1 sprite/盏 + 倒影 1 sprite/盏，
   fog:false 如灯点名）；update(t,k,rv)：rv 0→1 时灯影如潮退去——按相位由远及近次第熄灭。
   潮退是衰减：每盏 opacity = k·op0·闪烁·(≤1 的退潮包络)，fadeK 合规；live=false 时忽略 rv（静态繁华） */
function makeAndengJS(o){
  o=o||{};
  const live=o.live!==false;
  const xs=o.xs===undefined?[-52,-44,-36,-28,14,22,31,41,52]:o.xs;
  const zs=o.zs===undefined?[-64,-61,-58,-56,-56,-58,-61,-65,-70]:o.zs;
  const n=Math.min(xs.length,zs.length);
  const g=new THREE.Group(), items=[];
  const R=seedRnd(o.seed===undefined?23211:o.seed);
  for(let i=0;i<n;i++){
    const op0=0.30+0.24*R();
    const m=new THREE.SpriteMaterial({map:glowTex(),color:0xffc478,transparent:true,
      opacity:op0,depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
    const s=new THREE.Sprite(m);
    s.scale.set(4.6+R()*2.6,4.6+R()*2.6,1);
    s.position.set(xs[i],1.7+R()*1.5,zs[i]);
    s.renderOrder=3; g.add(s);
    const op2=op0*0.42;
    const m2=new THREE.SpriteMaterial({map:glowTex(),color:0xe8a858,transparent:true,
      opacity:op2,depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
    const s2=new THREE.Sprite(m2);
    s2.scale.set(2.8+R()*1.4,7.5+R()*3.0,1);
    s2.position.set(xs[i]+(R()-0.5)*2.2,0.55,zs[i]+7.5+R()*3);
    s2.renderOrder=2; g.add(s2);
    items.push({m:m,op0:op0,m2:m2,op2:op2,ph:(i/n)*0.72+R()*0.05});
  }
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=(live&&rv!==undefined)?rv:0;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      const off=1-sstep(it.ph,it.ph+0.30,r*1.10);          /* 潮退：由远及近次第熄灭 */
      it.m.opacity=kk*it.op0*(0.66+0.34*Math.sin(t*1.9+it.ph*9.1))*off;
      it.m2.opacity=kk*it.op2*(0.60+0.40*Math.sin(t*1.5+it.ph*7.7))*off;
    }
    g.visible=kk>0.004&&r<0.995;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 梦醒清辉 makeQinghuiJS(o)：点击后淡入的清醒月色（冷白横带薄雾 1 sprite+水面清辉微光
   makeGlow，fog:false 点名；初值=峰值，update(t,k,rv) 随 rv 淡入；组 rv=0 时 visible=false 硬关）——
   繁华褪尽，只余清醒江月 */
function makeQinghuiJS(o){
  o=o||{};
  const g=new THREE.Group();
  const band=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfd8e2,
    transparent:true,opacity:0.13,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  band.scale.set(250,24,1); band.position.set(-34,7.5,-122); band.renderOrder=2; g.add(band);
  const glint=makeGlow({n:20,box:[76,7,26],pos:[-18,1.8,-52],color:0xaab8c8,size:4.0,
    speed:0.02,rise:0,add:true,maxA:0.12});
  glint.points.renderOrder=3; g.add(glint.points);
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    band.material.opacity=kk*0.13*r*(0.84+0.16*Math.sin(t*0.3+0.7));
    glint.mat.uniforms.uMaxA.value=0.12*r;
    glint.update(t);
    g.visible=kk*r>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* 诗人：全诗贯穿的同一造型（青衫落拓、幞头；每次 build 新建材质） */
function qhPoet(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2e3844,belt:0x6a5a34,skin:0xd3b294,collar:0x8a94a2,
    hair:0x12161e,hat:'幞头',rimC:0xd4a84f,rim:0.40,noProp:true,scale:scale===undefined?1.6:scale});
}

/* 远山一环 makeYuanJS(o)：夜色深处的低平远山（两层，带雾骨相）——灯影展开的天际；
   组放近（z≈-160 以上），不被骨架常驻远山环（z≈-300）遮挡 */
function makeYuanJS(o){
  o=o||{};
  return makeRange({r:o.r===undefined?240:o.r,h:o.h===undefined?9:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?23221:o.seed,
    color:o.color===undefined?0x0d0906:o.color,atmo:0x33261a,
    fogK:o.fogK===undefined?0.60:o.fogK,glowK:0.06,glow:0xd4a05a,
    y:o.y===undefined?-12:o.y,order:-6});
}

/* 歌台灯晕：台口两盏小灯的光晕（各 1 sprite，fog:false，初值=峰值） */
function addGetaiGlows(g,x,y,z){
  const out=[];
  [1,-1].forEach(function(sd){
    const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc478,
      transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    gl.scale.set(5.2,5.2,1); gl.position.set(x+sd*3.2,y,z+1.4); gl.renderOrder=3;
    g.add(gl); out.push(gl);
  });
  return out;
}

function bCover(){ // 卷首 · 江湖夜泊全景：水岸歌台灯影连绵、画舫泊岸、酒旗斜挑、诗人独立岸边
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:90,amp:0.11,freq:0.14,speed:0.30,flow:[0.16,0.03],spec:0.9,
    deep:0x080504,shallow:0x140e08,skyc:0x1a1209,moonDir:[-0.28,0.30,-0.92]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xd8b878);
  water.mesh.position.set(0,-0.55,-115); g.add(water.mesh);
  const grd=makeGround({r:84,c1:0x0a0705,c2:0x171009,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,50);
  const yuan=makeYuanJS({seed:23222}); yuan.g.position.set(0,0,-160); g.add(yuan.g);
  const tai=makeGetaiJS({scale:1.2,rim:0.16}); tai.position.set(-16,0,-58); tai.rotation.y=0.12; g.add(tai);
  const gls=addGetaiGlows(g,-16,4.6,-58);
  const andeng=makeAndengJS({xs:[-50,-41,-31,20,31,43,54],zs:[-63,-60,-57,-56,-60,-64,-69],
    seed:23212}); g.add(andeng);
  const hf=makeHuafangJS({seed:23262}); hf.position.set(8,0,-24); hf.rotation.y=0.35; g.add(hf);
  const jq=makeJiuqiJS({seed:23252}); jq.position.set(13,0,-10); g.add(jq);
  const poet=qhPoet(1.15,'独立'); poet.position.set(4.2,-0.28,7); poet.rotation.y=2.7; g.add(poet);
  const mist=makeMist({n:5,spread:[200,10,70],pos:[0,3.0,-58],scale:56,color:0x2c1e0e,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[170,16,60],pos:[0,8,-10],color:0xd8b070,size:4.0,speed:0.028,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:10,d:5,color:0x060402,seed:23231,sway:0.8,rim:0.10,rimC:0xd4a84f});
  fg1.g.position.set(-11,-1.2,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x050302,seed:23232,rim:0.10,rimC:0xd4a84f});
  fg2.g.position.set(12,-1.4,13); g.add(fg2.g);
  addLights(g,{c:0xe4b078,i:0.40,p:[-46,56,-44]},{c:0x2a1c10,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    andeng.update(t,k,0); hf.update(t,k); jq.update(t,k);
    for(let i=0;i<gls.length;i++)gls[i].material.opacity=k*0.30*(0.85+0.15*Math.sin(t*2.2+i*2.1));
    poet.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bZaijiu(){ // 壹 · 载酒江湖 —— 落魄江湖载酒行，楚腰纤细掌中轻：
                    // 临水歌台灯影正盛，台上舞袖回身（腰细身轻，含蓄剪影），岸畔诗人独立、酒旗斜挑
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:90,amp:0.10,freq:0.14,speed:0.28,flow:[0.14,0.03],spec:0.92,
    deep:0x080504,shallow:0x150f08,skyc:0x1a1209,moonDir:[-0.28,0.26,-0.92]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xd8b878);
  water.mesh.position.set(0,-0.55,-112); g.add(water.mesh);
  const grd=makeGround({r:86,c1:0x0a0705,c2:0x181109,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,50);
  const yuan=makeYuanJS({seed:23223,h:8}); yuan.g.position.set(-6,0,-158); g.add(yuan.g);
  /* 水岸歌台（中景主体）+ 台上舞袖双影 + 台口灯晕 */
  const tai=makeGetaiJS({scale:1.55,rim:0.22}); tai.position.set(-5,0,-44); tai.rotation.y=0.10; g.add(tai);
  const w1=makeWuyingJS({scale:0.95,seed:23202}); w1.position.set(-6.6,1.90,-42.4); w1.rotation.y=0.4; g.add(w1);
  const w2=makeWuyingJS({scale:0.92,seed:23203}); w2.position.set(-3.0,1.90,-43.6); w2.rotation.y=-0.3; g.add(w2);
  const gls=addGetaiGlows(g,-5,6.0,-44);
  /* 沿岸灯串+水中灯影（静态繁华） */
  const andeng=makeAndengJS({live:false,seed:23213}); g.add(andeng);
  /* 诗人独立岸畔（载酒行）+ 小案酒坛 + 酒旗 + 画舫 */
  const poet=qhPoet(1.6,'独立'); poet.position.set(5.0,-0.28,2.5); poet.rotation.y=-2.75; g.add(poet);
  const an=makeTable({w:2.2,d:1.0,h:0.80,wood:0x241a10}); an.g.position.set(2.6,-0.28,0.4);
  an.g.rotation.y=-0.25; g.add(an.g);
  const jar=makeVessel({type:'坛',mat:'陶',scale:1.5,shadow:false}); jar.g.position.set(2.5,0.52,0.35);
  g.add(jar.g);
  const jq=makeJiuqiJS({seed:23253}); jq.position.set(-11,0,-4); jq.rotation.y=0.5; g.add(jq);
  const hf=makeHuafangJS({seed:23263}); hf.position.set(11,0,-20); hf.rotation.y=0.4; g.add(hf);
  const mist=makeMist({n:6,spread:[200,10,70],pos:[0,3.2,-56],scale:58,color:0x2c1e0e,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[180,16,62],pos:[0,8,-8],color:0xd8b070,size:4.2,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:24,n:10,d:5,color:0x060402,seed:23233,sway:0.75,rim:0.10,rimC:0xd4a84f});
  fg1.g.position.set(-12,-1.2,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x050302,seed:23234,rim:0.10,rimC:0xd4a84f});
  fg2.g.position.set(11.5,-1.4,12); g.add(fg2.g);
  addLights(g,{c:0xe8b478,i:0.42,p:[-40,54,-40]},{c:0x2a1c10,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    andeng.update(t,k,0); w1.update(t,k); w2.update(t,k);
    for(let i=0;i<gls.length;i++)gls[i].material.opacity=k*0.30*(0.85+0.15*Math.sin(t*2.2+i*2.3));
    poet.update(t,k); jq.update(t,k); hf.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bMengxing(){ // 贰（末境·可点击/标志性瞬间）· 梦醒扬州 —— 十年一觉扬州梦，赢得青楼薄幸名：
                      // 人已醒，梦未散——近处空案残樽（清醒），远处歌台灯影仍亮（梦境）；
                      // 点击：灯影繁华如潮退去+梦醒空案，清辉江月淡入
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:90,amp:0.10,freq:0.13,speed:0.26,flow:[0.12,0.03],spec:0.94,
    deep:0x070504,shallow:0x130d07,skyc:0x181009,moonDir:[-0.30,0.34,-0.90]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xcfc0a8);
  water.mesh.position.set(0,-0.55,-112); g.add(water.mesh);
  const grd=makeGround({r:86,c1:0x090604,c2:0x15100a,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,50);
  const yuan=makeYuanJS({seed:23224,h:8,peaks:4}); yuan.g.position.set(-8,0,-162); g.add(yuan.g);
  /* 远处歌台（梦未散的灯影）+ 台上舞袖剪影 + 台口灯晕 */
  const tai=makeGetaiJS({scale:1.35,rim:0.18}); tai.position.set(-13,0,-58); tai.rotation.y=0.10; g.add(tai);
  const w1=makeWuyingJS({scale:0.85,seed:23204}); w1.position.set(-14.4,1.66,-56.6); w1.rotation.y=0.3; g.add(w1);
  const w2=makeWuyingJS({scale:0.82,seed:23205}); w2.position.set(-11.2,1.66,-57.6); w2.rotation.y=-0.4; g.add(w2);
  const gls=addGetaiGlows(g,-13,5.2,-58);
  /* 沿岸灯串+水中灯影（可点击：如潮退去） */
  const andeng=makeAndengJS({xs:[-56,-48,-40,-32,10,19,29,40,51],
    zs:[-66,-62,-59,-57,-56,-58,-61,-65,-71],seed:23214}); g.add(andeng);
  /* 梦醒清辉（点击前 visible=false 硬关） */
  const qh=makeQinghuiJS({}); g.add(qh);
  /* 近处空案残樽（梦醒空案）+ 坐而独醒的诗人（人偏右靠后、案在其前，远处歌台灯影留出左半幅） */
  const an=makeTable({w:2.4,d:1.05,h:0.80,wood:0x241a10}); an.g.position.set(7.6,-0.28,4.6);
  an.g.rotation.y=-0.22; g.add(an.g);
  const bei=makeVessel({type:'杯',mat:'陶',scale:1.35,liquid:false,shadow:false});
  bei.g.position.set(7.1,0.62,4.7); bei.g.rotation.z=1.30; g.add(bei.g);
  const wan=makeVessel({type:'碗',mat:'陶',scale:1.1,liquid:false,shadow:false});
  wan.g.position.set(8.3,1.00,4.3); wan.g.rotation.x=Math.PI; g.add(wan.g);
  const poet=qhPoet(1.5,'坐饮'); poet.position.set(6.2,-0.28,3.2); poet.rotation.y=2.7; g.add(poet);
  const jq=makeJiuqiJS({seed:23254}); jq.position.set(-14,0,-10); jq.rotation.y=0.45; g.add(jq);
  const hf=makeHuafangJS({seed:23264,rim:0.30}); hf.position.set(14,0,-30); hf.rotation.y=0.62; g.add(hf);
  const mist=makeMist({n:7,spread:[210,11,72],pos:[0,3.4,-56],scale:58,color:0x2c1e0e,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[180,15,62],pos:[0,8,-8],color:0xd0b080,size:4.0,speed:0.028,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const wind=makeFlow({n:180,box:[130,10,46],pos:[0,7,-26],color:0x6a707c,size:14,speed:2.6,maxA:0.07});
  g.add(wind.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:11,d:5,color:0x060402,seed:23235,sway:0.8,rim:0.10,rimC:0xd4a84f});
  fg1.g.position.set(-12,-1.2,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x050302,seed:23236,rim:0.10,rimC:0xd4a84f});
  fg2.g.position.set(11,-1.4,11); g.add(fg2.g);
  addLights(g,{c:0xdcc4a0,i:0.38,p:[-50,60,-46]},{c:0x241c12,i:0.52});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/5.5);
      const r=ctl.reveal, e=r*r*(3-2*r);
      andeng.update(t,k,r);                      // 灯影繁华如潮退去
      qh.update(t,k,e);                          // 清辉江月淡入（冷白）
      poet.rotation.y=2.7+0.14*e;                // 诗人缓缓转身向月
      poet.update(t,k); w1.update(t,k); w2.update(t,k);
      for(let i=0;i<gls.length;i++)gls[i].material.opacity=k*0.30*(1-r*0.9)*(0.85+0.15*Math.sin(t*2.2+i*2.4));
      jq.update(t,k); hf.update(t,k);
      mist.update(t,k); motes.update(t); wind.update(t);
      water.update(t); yuan.update(t,0);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.06);
        pluck(4,0.05,0.12); pluck(2,0.55,0.10); pluck(0,1.15,0.08);   // 三叠下行，繁华散尽
        const fl=$('#flash'); fl.textContent='十年一觉扬州梦 赢得青楼薄幸名';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x140d07),hor:C(0x402c16),bot:C(0x080503),fog:C(0x181009),fd:0.0050,star:0.34,
  moon:new THREE.Vector3(-70,78,-190),ms:0.95,mph:0.42,mhaze:0.16,dirC:C(0xe8b878),dirI:0.44,
  dirP:new THREE.Vector3(-46,56,-44),ambC:C(0x2a1c10),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,9.0,40],t:[0,7.2,30],lf:[-7,10.5,-16],lt:[-14,12,-44]},
  sky:()=>SK({fd:0.0050,star:0.34,ms:0.95,mph:0.42}) },
{ name:'载酒江湖',dwell:17,river:0.03,build:bZaijiu,
  cam:{f:[1.6,6.4,18],t:[-1.0,5.0,6],lf:[-4,6.6,-18],lt:[-10,8.0,-42]},
  sky:()=>SK({fd:0.0056,star:0.28,ms:0.85,mph:0.48,mhaze:0.18,
    moon:new THREE.Vector3(-58,64,-180),dirC:C(0xe8b478),dirI:0.42,
    dirP:new THREE.Vector3(-40,54,-40),ambC:C(0x2a1c10),ambI:0.58}) },
{ name:'梦醒扬州',dwell:19,river:0.04,build:bMengxing,
  cam:{f:[1.4,5.8,17.5],t:[-0.6,3.3,-0.5],lf:[3,5.8,-12],lt:[8.5,7.2,-34]},
  sky:()=>SK({fd:0.0062,star:0.20,ms:1.35,mph:0.12,mhaze:0.12,
    moon:new THREE.Vector3(-64,84,-190),dirC:C(0xdcc4a0),dirI:0.38,
    dirP:new THREE.Vector3(-50,60,-46),ambC:C(0x241c12),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('qianhuai.py —— 被 build.py 消费：python build.py qianhuai')
