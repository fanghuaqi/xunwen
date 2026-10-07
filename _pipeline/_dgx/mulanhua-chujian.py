# -*- coding: utf-8 -*-
"""mulanhua-chujian.py —— 《木兰花·拟古决绝词柬友》（清·纳兰性德，queue no.202，水墨夜思）生成配置
两境（N=queue stages 数）：
  壹「秋风画扇」——人生若只如初见 / 秋风悲画扇（班婕妤秋扇见捐典）+ 故人心易变：
      冷月宫墙之下，画扇被弃石案（诀别面朝上），宫装人影独立，秋风卷叶——见弃之悲；
  贰「比翼连枝」（末境·可点击）——骊山语罢 / 泪雨霖铃（唐明皇杨贵妃典）+ 薄幸锦衣郎 / 比翼连枝当日愿：
      骊山华清宫远影、檐角霖铃、细雨落叶，架上一柄秋风画扇——
      点击画扇翻转初见与诀别两面（queue interact），暖忆低饱和浮现，冷对如霜回归。
标志性瞬间「画扇两面」：初见的并蒂莲面 ↔ 见弃的秋风面，一扇翻尽全词情绪轴。
水墨夜思色板：bg #0d1117、雾 #131a26 系、accent=#c4cfe0（扇骨/人物/檐铃边缘光），禁金；
初见之暖（低饱和并蒂莲、暖忆微光）与见弃之冷是全页情绪轴。"""

META = dict(
    N=2, slug='mulanhua-chujian', title='木兰花·拟古决绝词柬友', dyn='清 · 纳兰性德', brand_author='纳 兰 性 德',
    gold_rgb='196,207,224',
    root=""":root{
  --gold:#c4cfe0; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(196,207,224,.26);
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
    ],
    tip='轻点画面 / 按空格 —— 画扇翻转，初见与诀别两面',
    hint='← → 键或空格逐境游览 · 末境可点击秋风画扇：扇面翻转初见与诀别两面',
    cover_read='木兰花·拟古决绝词柬友。清，纳兰性德。人生若只如初见，何事秋风悲画扇。等闲变却故人心，却道故人心易变。',
    cover_p1='两重意境，随词句次第展开：人生若只如初见的一问，秋风画扇的见弃之悲，故人心易变的怅惘；再到骊山盟誓、霖铃泪雨的旧事，末了比翼连枝当日愿——一柄画扇，翻尽初见与诀别的两面人间。',
    cover_p2='边读词，边走进纳兰性德笔下的初见与诀别：暖忆低回而冷对如霜，一扇两面，皆是人心。',
    end_h2='初见 · 长愿', cn_word='两',
    words_js="['再游一次，画扇两面','初识容若，尚需共读','渐入词境，初见如昨','秋扇知意，词心渐明','已解故心易变之叹','初见如月，长愿比翼']",
    sky_atmo='0x232c3d',
)

POEM_JS = """const POEM = [
{ name:'秋风画扇', jing:'人生若只如初见 —— 秋风起而画扇悲：初见之好与见弃之悲，一问千古。（团扇 · 秋风 · 冷月）',
  segs:[
   {c:'人生若只如初见，', p:py('rén shēng ruò zhǐ rú chū jiàn')},
   {c:'何事秋风悲画扇。', p:py('hé shì qiū fēng bēi huà shàn')},
   {c:'等闲变却故人心，', p:py('děng xián biàn què gù rén xīn')},
   {c:'却道故人心易变。', p:py('què dào gù rén xīn yì biàn')}],
  read:'人生若只如初见，何事秋风悲画扇。等闲变却故人心，却道故人心易变。',
  yisi:'人生若能永远像初见时那样美好，又何来秋风里团扇的悲凉？恋人的心竟就这样轻易地变了，反而说——人心本来就是容易变的。上句是破空而来的千古一问：初见之好，人人心中皆有；下句用班婕妤秋扇见捐的典故作答：夏日随身、秋来见弃，情之易终，古今同慨。「等闲」二字最凉——不是天崩地裂的辜负，只是轻描淡写的更改。',
  zhu:[['木兰花','词牌名。此词一题《木兰词》，又题《木兰花令·拟古决绝词》：摹拟古乐府中女子与负心人决绝的口吻；「柬友」——写给一位朋友，以男女之情喻朋友相交'],['初见','刚刚相识、情意最笃的时候。「人生若只如初见」：人生若能总像初见那样美好——全词之眼，千古名句'],['画扇','绘着画的有柄团扇。班婕妤《怨歌行》以扇自喻：「常恐秋节至，凉飙夺炎热，弃捐箧笥中，恩情中道绝」——秋扇见捐，喻恩爱终了、见弃失宠'],['等闲','平平常常地、轻易地。等闲变却故人心：轻易地就变了心（「变却」的「却」为语助词）'],['故人心','恋人的心（一本作「故心人」，指这位故人）。却道故人心易变：反而推说人心本来就容易变——薄幸者的口吻，愈见其凉薄']] },
{ name:'比翼连枝', jing:'骊山语罢、霖铃泪雨 —— 点击秋风画扇：扇面翻转初见与诀别两面。（骊山 · 霖铃 · 点击画扇）',
  segs:[
   {c:'骊山语罢清宵半，', p:py('lí shān yǔ bà qīng xiāo bàn')},
   {c:'泪雨霖铃终不怨。', p:py('lèi yǔ lín líng zhōng bù yuàn')},
   {c:'何如薄幸锦衣郎，', p:py('hé rú bó xìng jǐn yī láng')},
   {c:'比翼连枝当日愿。', p:py('bǐ yì lián zhī dāng rì yuàn')}],
  read:'骊山语罢清宵半，泪雨霖铃终不怨。何如薄幸锦衣郎，比翼连枝当日愿。',
  yisi:'想当年骊山上七夕密语，盟誓说到清夜将半；如今霖雨铃声里和泪而听，却终究说不敢怨恨。又怎么比得上——当日比翼连枝的誓言呢？这是唐明皇与杨贵妃的旧事：骊山盟誓何等缠绵，马嵬坡下恩情断绝，蜀道闻铃唯余血泪。「薄幸锦衣郎」一问，问的又哪里只是一人？人情易变，好事难终，初见之好只合长存在当日的愿里。',
  zhu:[['骊山','在今陕西临潼，山上有华清宫。唐明皇（玄宗）与杨贵妃曾于七夕夜半在长生殿密相誓愿，愿世世为夫妇——白居易《长恨歌》「七月七日长生殿，夜半无人私语时」即咏此事'],['语罢清宵半','（当年的盟誓）密语才罢，清夜已过半——写七夕长生殿夜半私语之缠绵'],['泪雨霖铃','唐明皇西幸入蜀，霖雨涉旬，栈道中闻铃声与雨声相应，悼念杨贵妃，采其声制《雨霖铃》曲以寄恨。「终不怨」：纵然断肠也不敢怨恨——怨到深处反说「不怨」，愈见其苦'],['薄幸','薄情、负心；锦衣郎：身着锦衣的富贵男子，此处指唐明皇，亦暗讽世间薄幸之人'],['何如','哪里比得上。何如薄幸锦衣郎，比翼连枝当日愿：如今薄幸负心，哪里还比得上当日比翼连枝的盟愿'],['比翼连枝','《长恨歌》：「在天愿作比翼鸟，在地愿为连理枝。」比翼鸟一目一翼、比翼而飞；连枝异干而同根——当日之愿何等坚牢，反衬今日人心之易变']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「人生若只如初见」的下一句是？', o:['何事秋风悲画扇','等闲变却故人心','却道故人心易变'], a:0},
 {q:'「骊山语罢清宵半」的下一句是？', o:['比翼连枝当日愿','泪雨霖铃终不怨','何如薄幸锦衣郎'], a:1},
 {q:'下列读音与词义解说正确的是？', o:['「骊山」的「骊」读 lí；「薄幸」的「薄」读 bó，意为薄情负心','「画扇」的「扇」读 shān，指扇动；「等闲」指闲暇无事','「霖铃」指久下不停的雨；「锦衣郎」指身着蓑衣的渔人'], a:0},
 {q:'「秋风悲画扇」与「骊山语罢」「泪雨霖铃」分别用了什么典故？', o:['班婕妤秋扇见捐；唐明皇与杨贵妃七夕骊山盟誓、蜀道雨中闻铃','嫦娥奔月孤居广寒；牛郎织女七夕鹊桥相会','陶渊明归隐采菊东篱；伯牙子期高山流水遇知音'], a:0},
 {q:'本词题为「拟古决绝词柬友」，借闺怨拟古，其主旨是？', o:['以初见之好对见弃之悲，慨叹人情易变、好事难终（一说寓朋友决绝之意）','单纯赞美爱情的坚贞不渝','讽刺杨贵妃惑乱朝纲致安史之乱'], a:0},
];
"""

SCENES_JS = """/* ================= 木兰花·拟古决绝词 · 两境场景（水墨夜思：秋风画扇、比翼连枝） =================
   美术立意：水墨夜思赛道——底色 #0d1117、雾 #131a26 系、accent=#c4cfe0（扇骨/人物/檐铃边缘光），禁金。
   情绪轴：初见之暖（低饱和并蒂莲绢面 + 暖忆微光，唯一暖色且低饱和）↔ 见弃之冷（秋风枯枝 + 冷月细雨）。
   标志性瞬间「画扇两面」：末境点击画扇翻转初见与诀别两面（queue interact）。 */

/* —— 绢面落笔小工（Canvas 2D，仅用基础笔画）—— */
function mLotus(c,x,y,r,petal,edge){
  for(let i=0;i<8;i++){
    c.save(); c.translate(x,y); c.rotate(i*Math.PI/4);
    c.fillStyle=(i%2?petal:edge);
    c.beginPath(); c.scale(1,0.42); c.arc(0,-r*0.95,r*0.75,0,6.2832); c.fill();
    c.restore();
  }
  c.fillStyle='#d8c9a6';
  c.beginPath(); c.arc(x,y,r*0.22,0,6.2832); c.fill();
}
function mLeafDot(c,x,y,s,rot,col){
  c.save(); c.translate(x,y); c.rotate(rot); c.scale(1,0.45*s); c.fillStyle=col;
  c.beginPath(); c.arc(0,0,16*s,0,6.2832); c.fill(); c.restore();
}
function mWindArc(c,x,y,r){
  c.beginPath(); c.arc(x,y,r,Math.PI*0.9,Math.PI*1.65); c.stroke();
}

/* —— 画扇绢面贴图：初见=并蒂莲（暖忆·低饱和）、诀别=秋风枯枝（冷对）—— */
function mlhFaceTex(kind){
  const cv=document.createElement('canvas'); cv.width=512; cv.height=512;
  const c=cv.getContext('2d');
  const cx=256, cy=256, R=250;
  const g1=c.createRadialGradient(cx,cy,40,cx,cy,R);
  if(kind==='初见'){ g1.addColorStop(0,'#e9e2cf'); g1.addColorStop(0.72,'#e1d9c3'); g1.addColorStop(1,'#d3cab1'); }
  else{ g1.addColorStop(0,'#dfe2e8'); g1.addColorStop(0.72,'#d4d9e2'); g1.addColorStop(1,'#c4cbd8'); }
  c.fillStyle=g1; c.beginPath(); c.arc(cx,cy,R,0,6.2832); c.fill();
  /* 绢纹细线 */
  c.strokeStyle='rgba(96,102,118,0.06)'; c.lineWidth=1;
  for(let y=20;y<500;y+=9){ c.beginPath(); c.moveTo(14,y); c.lineTo(498,y); c.stroke(); }
  /* 缘圈双线 */
  c.strokeStyle='rgba(70,78,94,0.55)'; c.lineWidth=5;
  c.beginPath(); c.arc(cx,cy,R-7,0,6.2832); c.stroke();
  c.strokeStyle='rgba(70,78,94,0.25)'; c.lineWidth=2;
  c.beginPath(); c.arc(cx,cy,R-26,0,6.2832); c.stroke();
  if(kind==='初见'){
    /* 一茎双莲（并蒂）+ 一梗横出 */
    c.strokeStyle='#7d8b74'; c.lineWidth=7; c.lineCap='round';
    c.beginPath(); c.moveTo(cx+26,cy+208); c.quadraticCurveTo(cx-6,cy+96,cx-34,cy+2); c.stroke();
    c.beginPath(); c.moveTo(cx-34,cy+2); c.quadraticCurveTo(cx+18,cy-34,cx+56,cy-72); c.stroke();
    c.lineWidth=4;
    c.beginPath(); c.moveTo(cx-8,cy+120); c.quadraticCurveTo(cx+60,cy+96,cx+108,cy+96); c.stroke();
    /* 叶两笔（灰绿） */
    mLeafDot(c,cx-58,cy+150,1.7,-0.5,'#87947f');
    mLeafDot(c,cx+70,cy+172,1.4,0.55,'#7f8c78');
    /* 两朵低绯莲 */
    mLotus(c,cx-36,cy-16,40,'#c7a6ab','#b18d93');
    mLotus(c,cx+62,cy-86,32,'#ccadb2','#b49097');
    /* 款识 + 印 */
    c.fillStyle='rgba(92,84,68,0.9)';
    c.font='34px "Ma Shan Zheng","Kaiti SC","KaiTi",serif';
    c.fillText('初 见',cx+100,cy+196);
    c.fillStyle='rgba(156,88,72,0.75)'; c.fillRect(cx+108,cy+208,22,22);
  }else{
    /* 枯枝入画（墨，浓笔） */
    c.strokeStyle='rgba(38,44,56,0.95)'; c.lineCap='round';
    c.lineWidth=14; c.beginPath(); c.moveTo(20,52); c.bezierCurveTo(122,124,194,154,264,162); c.stroke();
    c.lineWidth=7; c.beginPath(); c.moveTo(152,134); c.quadraticCurveTo(198,202,212,256); c.stroke();
    c.lineWidth=5; c.beginPath(); c.moveTo(96,94); c.quadraticCurveTo(54,154,54,204); c.stroke();
    c.lineWidth=4; c.beginPath(); c.moveTo(236,150); c.quadraticCurveTo(286,180,318,224); c.stroke();
    /* 辞枝余叶数点 */
    mLeafDot(c,216,266,1.3,0.4,'rgba(92,100,114,0.95)');
    mLeafDot(c,318,222,1.1,-0.6,'rgba(108,116,130,0.9)');
    mLeafDot(c,372,306,1.4,0.9,'rgba(84,92,106,0.95)');
    mLeafDot(c,296,366,1.0,-0.3,'rgba(102,110,124,0.9)');
    mLeafDot(c,176,336,1.05,1.2,'rgba(90,98,112,0.85)');
    /* 风纹三道 */
    c.strokeStyle='rgba(126,136,152,0.7)'; c.lineWidth=6;
    mWindArc(c,cx-16,cy+26,150); mWindArc(c,cx+34,cy+92,108); mWindArc(c,cx-64,cy+138,76);
    /* 款识 + 印 */
    c.fillStyle='rgba(72,78,92,0.9)';
    c.font='34px "Ma Shan Zheng","Kaiti SC","KaiTi",serif';
    c.fillText('诀 别',cx+100,cy+196);
    c.fillStyle='rgba(116,124,140,0.85)'; c.fillRect(cx+108,cy+208,22,22);
  }
  return new THREE.CanvasTexture(cv);
}

/* —— 团扇：竹骨圈 + 扇柄 + 正反两面绢面（初见/诀别）——
   返回 {g 外层（摆放/摇曳）, flip 内层（翻面）}；face:'初见' 正面朝前，'诀别' 已翻面 */
function makeTuanfan(o){
  o=o||{};
  const R=o.r===undefined?2.2:o.r, face=o.face===undefined?'诀别':o.face;
  const g=new THREE.Group(), flip=new THREE.Group();
  const B=new GeoBag();
  const rim=new THREE.TorusGeometry(R,0.075,8,44); B.put(rim,0x46403a);
  const handle=new THREE.CylinderGeometry(0.06,0.085,R*1.12,8);
  handle.translate(0,-(R+R*0.50),0); B.put(handle,0x35302a);
  const knob=new THREE.SphereGeometry(0.10,8,6); knob.translate(0,-(R+R*1.06),0); B.put(knob,0x4a4136);
  flip.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x3a404c,emissive:0x05070c}),{c:0xc4cfe0,i:0.35,p:2.6})));
  const fA=new THREE.Mesh(new THREE.CircleGeometry(R-0.04,44),
    new THREE.MeshBasicMaterial({map:mlhFaceTex('初见'),color:0xaeb4c0,transparent:true,opacity:0.97}));
  fA.position.z=0.015; fA.renderOrder=2;
  const fB=new THREE.Mesh(new THREE.CircleGeometry(R-0.04,44),
    new THREE.MeshBasicMaterial({map:mlhFaceTex('诀别'),color:0xaeb4c0,transparent:true,opacity:0.97}));
  fB.position.z=-0.015; fB.renderOrder=2; fB.rotation.y=Math.PI;
  flip.add(fA); flip.add(fB);
  if(face==='诀别')flip.rotation.y=Math.PI;
  g.add(flip);
  return {g,flip};
}

/* —— 扇架：A 形木架（立扇倚其上，微微后仰）—— */
function makeShanjia(){
  const B=new GeoBag();
  [0.55,-0.55].forEach(function(z){
    const l1=new THREE.CylinderGeometry(0.05,0.07,3.0,6); l1.rotateZ(-0.42); l1.translate(-0.62,1.45,z); B.put(l1,0x161b26);
    const l2=new THREE.CylinderGeometry(0.05,0.07,3.0,6); l2.rotateZ(0.42); l2.translate(0.62,1.45,z); B.put(l2,0x161b26);
    const ft=new THREE.BoxGeometry(1.7,0.12,0.3); ft.translate(0,0.06,z); B.put(ft,0x11161f);
  });
  const beam=new THREE.CylinderGeometry(0.05,0.05,1.35,6); beam.rotateX(Math.PI/2);
  beam.translate(0,2.86,0); B.put(beam,0x1b2230);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x05070c}),{c:0x9fb3cc,i:0.28,p:2.5})));
  return {g};
}

/* —— 石案：厚石面 + 板足 + 走水线（水墨冷石）—— */
function makeShizhuo(o){
  o=o||{};
  const w=o.w===undefined?5.6:o.w, d=o.d===undefined?2.7:o.d, h=o.h===undefined?1.55:o.h;
  const B=new GeoBag();
  const top=new THREE.BoxGeometry(w,0.30,d); top.translate(0,h-0.15,0); B.put(top,0x141a24);
  const edge=new THREE.BoxGeometry(w*1.01,0.07,d*1.012); edge.translate(0,h-0.32,0); B.put(edge,0x1d2534);
  [1,-1].forEach(function(s){
    const leg=new THREE.BoxGeometry(0.55,h-0.30,d*0.72); leg.translate(s*(w*0.5-0.5),(h-0.30)/2,0); B.put(leg,0x10151f);
  });
  const stretch=new THREE.BoxGeometry(w*0.86,0.14,0.30); stretch.translate(0,0.35,0); B.put(stretch,0x10151f);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.22,p:2.5})));
  return {g,h,w,d};
}

/* —— 案头绢卷：画卷一轴（被弃的旧日玩意）—— */
function makeJtjuan(){
  const B=new GeoBag();
  const roll=new THREE.CylinderGeometry(0.15,0.15,1.5,10); roll.rotateZ(Math.PI/2);
  roll.translate(0,0.15,0); B.put(roll,0x2a303c);
  [1,-1].forEach(function(s){
    const ax=new THREE.CylinderGeometry(0.05,0.05,0.34,6); ax.rotateZ(Math.PI/2);
    ax.translate(s*0.90,0.15,0); B.put(ax,0x1a1f2a);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x2e3848,emissive:0x05070c}),{c:0x9fb3cc,i:0.22,p:2.5})));
  return g;
}

/* —— 宫墙：一段宫墙 + 门楼 + 角楼剪影（长门清冷）—— */
function makeGongqiang(){
  const B=new GeoBag(), c1=0x0c1017, c2=0x111824, c3=0x18202e;
  const wall=new THREE.BoxGeometry(64,5.6,2.4); wall.translate(0,2.8,0); B.put(wall,c1);
  const cap=new THREE.BoxGeometry(64.6,0.5,2.9); cap.translate(0,5.85,0); B.put(cap,c2);
  for(let i=0;i<21;i++){
    const du=new THREE.BoxGeometry(1.2,0.8,1.1); du.translate(-30+i*3,6.5,0); B.put(du,c1);
  }
  const gate=new THREE.BoxGeometry(4.2,3.4,3.0); gate.translate(-12,1.7,0.4); B.put(gate,0x080b11);
  const body=new THREE.BoxGeometry(8.6,5.4,4.4); body.translate(-12,5.6+2.7,0); B.put(body,c2);
  const roof=new THREE.ConeGeometry(6.4,1.9,4); roof.rotateY(Math.PI/4);
  roof.scale(1.25,1,1.05); roof.translate(-12,11.0+0.95,0); B.put(roof,c3);
  [24,-30].forEach(function(px){
    const tw=new THREE.BoxGeometry(5,3.6,3.6); tw.translate(px,5.6+1.8,0); B.put(tw,c2);
    const tr=new THREE.ConeGeometry(4.1,1.4,4); tr.rotateY(Math.PI/4);
    tr.scale(1.22,1,1.0); tr.translate(px,9.2+0.7,0); B.put(tr,c3);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb3cc,i:0.24,p:2.5})));
  return g;
}

/* —— 檐角霖铃：檐柱托角梁，梁下挂三铃（泪雨霖铃意象，随风轻晃）—— */
function makeYanling(){
  const B=new GeoBag();
  const zhu=new THREE.CylinderGeometry(0.09,0.13,7.6,8); zhu.translate(-0.2,-3.4,0); B.put(zhu,0x11161f);
  const dou=new THREE.BoxGeometry(0.62,0.42,0.66); dou.translate(-0.2,0.10,0); B.put(dou,0x1b2230);
  const liang=new THREE.BoxGeometry(3.4,0.22,0.5); liang.translate(1.4,0,0); B.put(liang,0x141a24);
  const wa=new THREE.BoxGeometry(3.6,0.16,0.72); wa.translate(1.4,0.26,0.06); B.put(wa,0x18202e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x05070c}),{c:0x9fb3cc,i:0.30,p:2.5})));
  const bells=[];
  [[1.35,0.5],[1.85,0.76],[2.35,1.05]].forEach(function(b){
    const s=new THREE.Group();
    const str=new THREE.Mesh(new THREE.CylinderGeometry(0.012,0.012,b[1],4),
      new THREE.MeshPhongMaterial({color:0x3a414e}));
    str.position.set(b[0],-b[1]/2,0); s.add(str);
    const bell=new THREE.Mesh(new THREE.ConeGeometry(0.14,0.26,8),
      new THREE.MeshPhongMaterial({color:0x4a5260,shininess:40,specular:0x8fa0b8,emissive:0x060a12}));
    bell.rotation.x=Math.PI; bell.position.set(b[0],-b[1]-0.13,0); s.add(bell);
    g.add(s); bells.push({s,ph:b[0]*2.1});
  });
  g.rotation.z=-0.16;
  return {g,update(t){ for(const b of bells){
    b.s.rotation.x=0.16*Math.sin(t*1.8+b.ph);
    b.s.rotation.z=0.10*Math.sin(t*1.3+b.ph*1.7);
  } }};
}

/* —— 骊山之巅华清宫剪影（重檐殿 + 两侧配殿）—— */
function makeHuaqing(){
  const B=new GeoBag(), c1=0x0d121b, c2=0x131a28, c3=0x1a2331;
  const base=new THREE.BoxGeometry(9,1.4,5); base.translate(0,0.7,0); B.put(base,c1);
  const body=new THREE.BoxGeometry(5.6,4.6,3.6); body.translate(0,1.4+2.3,0); B.put(body,c2);
  const rf=new THREE.ConeGeometry(4.6,1.7,4); rf.rotateY(Math.PI/4);
  rf.scale(1.22,1,1.0); rf.translate(0,6.0+0.85,0); B.put(rf,c3);
  [1,-1].forEach(function(s){
    const hall=new THREE.BoxGeometry(2.6,2.6,2.6); hall.translate(s*3.4,1.4+1.3,0); B.put(hall,c2);
    const hr=new THREE.ConeGeometry(2.4,1.1,4); hr.rotateY(Math.PI/4);
    hr.translate(s*3.4,4.0+0.55,0); B.put(hr,c3);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.26,p:2.5})));
  return g;
}

/* —— 坠落粒子（落叶 / 细雨两用）：自写着色器，顶点回绕下落 + 横向风漂 —— */
const MLH_DROP_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uWind;
varying float vA;
void main(){
  vec3 p=position;
  float h=uBox.y;
  float fall=mod(uTime*uSpeed*(0.55+0.9*aSeed)+aSeed*h*7.0,h);
  p.y+=h*0.5-fall;
  p.x+=mod(uWind*uTime*(0.5+aSeed)+sin(uTime*0.8+aSeed*41.0)*1.6+uBox.x*0.5,uBox.x)-uBox.x*0.5;
  p.z+=cos(uTime*0.6+aSeed*29.0)*1.2;
  vA=smoothstep(0.0,4.0,fall)*smoothstep(h,h-4.0,fall);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.7+0.3*fract(aSeed*13.7))*(140.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeFall(o){
  const n=o.n===undefined?120:o.n, box=o.box===undefined?[120,50,80]:o.box, pos=o.pos===undefined?[0,22,-15]:o.pos;
  const color=o.color===undefined?0x8a94a2:o.color, size=o.size===undefined?4.5:o.size;
  const speed=o.speed===undefined?2:o.speed, wind=o.wind===undefined?2.4:o.wind, maxA=o.maxA===undefined?0.45:o.maxA;
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=size*(0.6+Math.random()*0.9);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:speed},uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uWind:{value:wind},uColor:{value:C(color)},uFade:{value:0},uMaxA:{value:maxA}},
    vertexShader:MLH_DROP_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

function bCoverMlh(){ // 封面 · 冷月无声
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:2026,color:0x070a10,atmo:0x232c3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:2027,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const reed=makeForeground({kind:'芦苇',n:10,w:24,d:6,color:0x04060a,seed:2028,sway:0.8});
  reed.g.position.set(-13,-1.6,20); g.add(reed.g);
  const mist=makeMist({n:10,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0xaebcd4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:64,box:[220,40,130],pos:[0,10,-40],color:0xc4cfe0,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xaebcd4,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); reed.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bHuafan(){ // 一 · 秋风画扇 —— 初见之好与见弃之悲（画扇被弃石案，诀别面朝上）
  const g=new THREE.Group();
  const grd=makeGround({r:160,c1:0x07090e,c2:0x101520});
  grd.mesh.position.y=-0.5; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:18,layers:2,peaks:4,seed:2101,color:0x070a10,atmo:0x1f2a3d,fogK:0.62,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 宫墙 + 门楼角楼剪影（长门）+ 门侧 distant 宫人 */
  const wall=makeGongqiang(); wall.position.set(0,0,-32); g.add(wall);
  const crowd=makeCrowd({n:3,rect:[-15,-30.5,7,2.2],seed:2102,color:0x11161f,rimC:0x9fb3cc,
    rim:0.20,sMin:0.5,sMax:0.62});
  g.add(crowd.mesh);
  /* 石案 + 绢卷 + 画扇（诀别面朝外，斜倚案沿而立——秋扇见捐）*/
  const table=makeShizhuo({w:5.6,d:2.7,h:1.55}); table.g.position.set(-2.8,0,-8.5); g.add(table.g);
  const juan=makeJtjuan(); juan.position.set(-0.7,1.55,-8.1); juan.rotation.y=0.5; g.add(juan);
  const fan=makeTuanfan({r:1.8,face:'诀别'});
  fan.g.position.set(-3.1,3.26,-7.6); fan.g.rotation.x=-0.30; g.add(fan.g);
  /* 宫装人影：独立案旁，望扇不语（班婕妤之影）*/
  const lady=makeFigure({pose:'独立',robe:0x1e2836,belt:0x4a5a72,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0xc4cfe0,rim:0.5,scale:1.32});
  lady.position.set(3.4,0,-11.5); lady.rotation.y=-0.5; g.add(lady);
  /* 秋风横流 + 落叶辞枝 + 低雾 */
  const flow=makeFlow({n:190,box:[150,16,70],pos:[0,9,-30],color:0x8fa0b8,size:24,speed:5.5,maxA:0.14});
  g.add(flow.points);
  const leaves=makeFall({n:44,box:[80,26,44],pos:[0,13,-14],color:0x8a94a2,size:5,speed:1.7,wind:2.6,maxA:0.5});
  g.add(leaves.points);
  const mist=makeMist({n:7,spread:[220,22,120],pos:[0,8,-50],scale:76,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  /* 前景框景：枯枝入画 + 坡石 */
  const br=makeForeground({kind:'树枝',n:3,w:18,d:5,color:0x04060a,seed:2103,sway:1.2});
  br.g.position.set(-14,2,22); g.add(br.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.6,w:20,d:8,color:0x04060a,seed:2104,rim:0.14});
  rk.g.position.set(13,-1.2,24); g.add(rk.g);
  addLights(g,{c:0xaebcd4,i:0.5,p:[-30,90,-40]},{c:0x1a2232,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); flow.update(t); leaves.update(t); mist.update(t,k);
    crowd.update(t); lady.update(t,k);
    br.update(t,k); rk.update(t,k);
  }};
}

function bBiyi(){ // 二（末境·可点击）· 比翼连枝 —— 点击秋风画扇：扇面翻转初见与诀别两面
  const ctl={t:0,clicked:false,last:-9,faceA:false,k:1,from:Math.PI,to:Math.PI,warm:0};
  const g=new THREE.Group();
  const grd=makeGround({r:170,c1:0x080a10,c2:0x121722});
  grd.mesh.position.y=-0.4; g.add(grd.mesh);
  const ridge=makeRange({r:260,h:13,layers:2,peaks:3,seed:2111,color:0x080a10,atmo:0x1f2a3d,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 骊山双峰 + 山巅华清宫剪影（七月七日长生殿）*/
  const hillMat=new THREE.MeshPhongMaterial({color:0x0a0e16,shininess:4,specular:0x1c2432,emissive:0x04060a});
  const li1=new THREE.Mesh(new THREE.SphereGeometry(46,20,12),hillMat);
  li1.scale.set(1,0.17,0.62); li1.position.set(-6,-1.5,-82); g.add(li1);
  const li2=new THREE.Mesh(new THREE.SphereGeometry(30,16,10),hillMat);
  li2.scale.set(1,0.15,0.6); li2.position.set(34,-1.8,-98); g.add(li2);
  const gong=makeHuaqing(); gong.position.set(-6,6.1,-76); gong.scale.setScalar(1.35); g.add(gong);
  /* 檐角霖铃（泪雨霖铃）*/
  const bells=makeYanling(); bells.g.position.set(-9.5,6.4,-13); g.add(bells.g);
  /* 扇架 + 秋风画扇（主角·可点击翻面：初见 ↔ 诀别）*/
  const jia=makeShanjia(); jia.g.position.set(2.4,0,-4.5); g.add(jia.g);
  const fan=makeTuanfan({r:2.05,face:'诀别'});
  fan.g.position.set(2.4,6.75,-4.2); fan.g.rotation.x=-0.16; g.add(fan.g);
  /* 词人独立（容若望着画扇）*/
  const poet=makeFigure({pose:'独立',robe:0x202a3a,belt:0x51617a,skin:0xd3c0a6,collar:0xc4cfe0,
    hat:'幞头',rimC:0xc4cfe0,rim:0.55,scale:1.3});
  poet.position.set(-4.8,0,-2.5); poet.rotation.y=0.55; g.add(poet);
  /* 暖忆微光：翻到初见面时的一线低饱和暖（全页唯一暖色，低饱和）*/
  const warmLight=new THREE.PointLight(0xb08e80,1.15,26); // 初值=最大值（fadeK 铁律）
  warmLight.position.set(2.4,6.2,-2.2); g.add(warmLight);
  /* 冷雨 + 落叶 + 风流 + 低雾 */
  const rain=makeFall({n:240,box:[150,46,80],pos:[0,23,-18],color:0xaebccd,size:2.4,speed:13,wind:3.0,maxA:0.4});
  g.add(rain.points);
  const leaves=makeFall({n:30,box:[70,22,36],pos:[0,11,-10],color:0x8a94a2,size:4.6,speed:1.5,wind:2.2,maxA:0.42});
  g.add(leaves.points);
  const flow=makeFlow({n:150,box:[200,14,80],pos:[0,8,-40],color:0x8fa0b8,size:22,speed:5,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[240,22,120],pos:[0,8,-60],scale:80,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  /* 前景框景：芦苇 + 枯枝 */
  const reed=makeForeground({kind:'芦苇',n:12,w:26,d:6,color:0x04060a,seed:2112,sway:1.0});
  reed.g.position.set(-13,-1.3,13); g.add(reed.g);
  const br=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:2113,sway:1.4,rim:0.18});
  br.g.position.set(14,1.5,15); g.add(br.g);
  addLights(g,{c:0xaebcd4,i:0.4,p:[-20,70,-30]},{c:0x1c2430,i:0.55});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.k<1){ ctl.k=Math.min(1,ctl.k+dt/1.5);
        fan.flip.rotation.y=ctl.from+(ctl.to-ctl.from)*ease(ctl.k); }
      ctl.warm+=((ctl.faceA?1:0)-ctl.warm)*Math.min(1,dt*1.6);
      warmLight.intensity=k*1.15*ctl.warm*(0.88+0.12*Math.sin(t*2.0));
      fan.g.rotation.z=0.018*Math.sin(t*0.6);
      ridge.update(t,0); bells.update(t); rain.update(t); leaves.update(t); flow.update(t);
      mist.update(t,k); poet.update(t,k); reed.update(t,k); br.update(t,k);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.4)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; setAmbience(0.32); }
      ctl.faceA=!ctl.faceA;
      ctl.from=fan.flip.rotation.y; ctl.to=ctl.from+Math.PI; ctl.k=0;
      pluck(2,0,0.10); pluck(4,0.42,0.085);
      const fl=$('#flash'); fl.textContent=ctl.faceA?'人生若只如初见':'何事秋风悲画扇';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(34,118,-190),ms:1.8,mph:0,mhaze:0.05,dirC:C(0xa8b8d0),dirI:0.5,
  dirP:new THREE.Vector3(-30,90,-40),ambC:C(0x1a2232),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverMlh,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,16,-40],lt:[0,16,-40]},
  sky:()=>SK({top:C(0x060910),hor:C(0x141c2a),bot:C(0x080b11),fog:C(0x0f1520),fd:0.0048,star:0.45,
    ms:1.7,moon:new THREE.Vector3(24,104,-180),
    dirC:C(0xaebcd4),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'秋风画扇',dwell:16,river:0.02,build:bHuafan,
  cam:{f:[0,5.6,20],t:[1.0,5.2,16],lf:[-0.5,4.4,-9],lt:[0.5,4.2,-11]},
  sky:()=>SK({fd:0.0060,star:0.5,ms:2.0,mph:0,mhaze:0.05,moon:new THREE.Vector3(-42,120,-185),
    dirC:C(0xaebcd4),dirI:0.5,ambC:C(0x1a2232),ambI:0.6}) },
{ name:'比翼连枝',dwell:18,river:0.03,build:bBiyi,
  cam:{f:[0,6.2,16.5],t:[-0.8,5.9,13],lf:[1.2,5.9,-5],lt:[2.2,5.6,-8]},
  sky:()=>SK({fd:0.0066,star:0.35,ms:1.5,mph:0.15,mhaze:0.10,moon:new THREE.Vector3(-55,105,-200),
    dirI:0.4,ambC:C(0x1c2430),ambI:0.55}) },
];
"""
