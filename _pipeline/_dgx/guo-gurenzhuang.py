# -*- coding: utf-8 -*-
"""guo-gurenzhuang.py —— 《过故人庄》（唐·孟浩然，no.215，青绿春晓·田家做客）生成配置
四境（五律四联各一境）：
  壹 鸡黍邀客（首联·故人具鸡黍，邀我至田家——炊烟黍饭，主人迎客）
  贰 绿树青山（颔联·标志性瞬间：绿树村边合、青山郭外斜——绿树两弧合抱村郭、青山斜出）
  叁 开轩把酒（颈联·开轩面场圃，把酒话桑麻——场圃在望，宾主对酌话农事）
  肆 重阳菊约（尾联·末境点击：菊花次第开 + 重来访路亮起）"""

META = dict(
    N=4, slug='guo-gurenzhuang', title='过故人庄', dyn='唐 · 孟浩然', brand_author='孟 浩 然',
    gold_rgb='163,201,143',
    root=""":root{
  --gold:#a3c98f; --ink:#eef4e6; --dim:#87a38c; --paper:rgba(10,20,14,.60);
  --line:rgba(163,201,143,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0a1410', 2),
        ('rgba(5,8,15', 'rgba(6,12,9', 1),
        ('rgba(4,6,11', 'rgba(5,10,7', 2),
        ('rgba(6,9,16', 'rgba(6,11,8', 1),
        ('rgba(3,5,9', 'rgba(4,8,6', 1),
        ('#0b101c', '#0e1a14', 1),
        ('#6f664f', '#5f7264', 1),
        ('#5a5340', '#52604f', 1),
    ],
    tip='轻点画面 / 按空格 —— 菊花次第开，重来访路亮起',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看菊花次第开、重来访路亮起',
    cover_read='过故人庄。唐，孟浩然。故人具鸡黍，邀我至田家。绿树村边合，青山郭外斜。',
    cover_p1='四重意境，随诗句次第展开：老朋友备下鸡黍饭相邀，我欣然赴田家；村边绿树环抱，郭外青山斜倚；推开轩窗，场圃在望，端起酒杯闲话桑麻；临别相约——待到重阳日，还来就菊花。',
    cover_p2='边读诗，边走进孟浩然应邀做客的那个绿树合抱、把酒言欢的田家小院。',
    end_h2='菊约 · 情真', cn_word='四',
    words_js="['再访一次田家','初识孟公，尚需共读','渐入佳境，再诵几遍','诗境渐深，宾主意浓','已解田家真味','绿树青山，重阳菊约有期']",
    sky_atmo='0x2c4434',
)

POEM_JS = """const POEM = [
{ name:'鸡黍邀客', jing:'老朋友备办了鸡和黄米饭，邀请我到他的田庄做客。（具鸡黍 · 赴田家）',
  segs:[
   {c:'故人具鸡黍，', p:py('gù rén jù jī shǔ')},
   {c:'邀我至田家。', p:py('yāo wǒ zhì tián jiā')}],
  read:'故人具鸡黍，邀我至田家。',
  yisi:'老朋友备办了鸡和黄米饭，邀请我到他的田庄做客。——「具鸡黍」见出待客的诚意：不是山珍海味，而是农家最实在的一桌饭菜；一个「邀」字脱口而出，不是客套的「请」，是熟人之间随口一唤的亲切。诗就从这声最朴素的邀请里开始，田家炊烟与饭香扑面而来。',
  zhu:[['故人','老朋友'],['具','备办，准备'],['鸡黍（shǔ）','鸡和黄米饭，农家待客的饭菜。黍：黄米，去皮软糯，是北方农家待客的主食'],['邀','邀请——不是郑重的「请」，而是熟人之间随口一唤的亲切'],['至','到、来到'],['田家','田庄，农家']] },
{ name:'绿树青山', jing:'村庄四面绿树环抱，一道青山斜倚在村郭之外。（绿树合 · 青山斜）',
  segs:[
   {c:'绿树村边合，', p:py('lǜ shù cūn biān hé')},
   {c:'青山郭外斜。', p:py('qīng shān guō wài xié')}],
  read:'绿树村边合，青山郭外斜。',
  yisi:'村庄的四周，绿树环抱成一圈绿色的围墙；一道青翠的山梁，远远地斜倚在村郭之外。——「合」字写树，像两只手臂把村庄轻轻拢住；「斜」字写山，不取正面的威压，只取一抹斜出的青影。一近一远、一合一斜，田庄的清幽与开阔同时立在纸上，是田园诗里最著名的环抱构图。',
  zhu:[['合','环抱、围拢——绿树在村边连成一圈，把村庄围在中间'],['郭','本指外城，这里借指村庄的墙垣村郭'],['斜（xié）','斜立、横斜——青山远远斜倚在郭外。旧读 xiá 以协韵，今从现代音读 xié'],['环抱构图','近处绿树合围、远处青山斜出，一收一放，是本诗最著名的画面']] },
{ name:'开轩把酒', jing:'推开窗轩，正对着打谷场和菜园；端起酒杯，闲谈的全是桑麻农事。（开轩 · 话桑麻）',
  segs:[
   {c:'开轩面场圃，', p:py('kāi xuān miàn cháng pǔ')},
   {c:'把酒话桑麻。', p:py('bǎ jiǔ huà sāng má')}],
  read:'开轩面场圃，把酒话桑麻。',
  yisi:'推开窗轩，窗外正对着打谷场和菜园；端起酒杯，说的没有一句客套话，全是桑麻长势、收成好坏这些农家事。——「开轩」一开，田野的空气就进了席面；「话桑麻」三字最见交情：只有真正的知己，才不必应酬，只把日子里的庄稼事细细说来。宾主对酌，浑然忘形。',
  zhu:[['轩','窗。开轩：推开窗'],['面','面对，正对着'],['场圃','打谷场和菜园。场：打谷晒粮的平场，读 cháng；圃：种菜蔬的园地，读 pǔ'],['把酒','端着酒杯。把：拿、持'],['话桑麻','闲谈桑麻等农事。桑麻：桑树和麻，泛指庄稼农活——语意近陶渊明「相见无杂言，但道桑麻长」']] },
{ name:'重阳菊约', jing:'临别时主人相邀：等到九九重阳那天，再来赏菊饮酒。（点击画面：菊花次第开，重来访路亮起）',
  segs:[
   {c:'待到重阳日，', p:py('dài dào chóng yáng rì')},
   {c:'还来就菊花。', p:py('huán lái jiù jú huā')}],
  read:'待到重阳日，还来就菊花。',
  yisi:'酒喝到尽兴处，主人相邀：等到九九重阳那天，你再来，我们一起赏菊、饮菊花酒吧。——不写告别的不舍，只许一个再来的约期；不说「再来」的客套，只说「就菊花」的随意。一个「就」字，凑近就坐、不拘形迹，把宾主的真率写到了极处，全诗在这声爽朗的相约里收束，余味无穷。',
  zhu:[['待','等到'],['重阳日','农历九月初九，重阳节。古人有登高、赏菊、饮菊花酒的风俗'],['还（huán）来','再来。还：再、又'],['就','凑近，奔赴——「就菊花」即来赏菊、共饮菊花酒，语气随意亲昵，不假客气']] },
];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「故人具鸡黍」的下一句是？', o:['邀我至田家','绿树村边合','把酒话桑麻'], a:0},
 {q:'「绿树村边合」的下一句是？', o:['开轩面场圃','青山郭外斜','待到重阳日'], a:1},
 {q:'「故人具鸡黍」的「黍」与「开轩面场圃」的「轩」，注音或词义都正确的是？', o:['黍 shǔ，黄米；轩，窗','黍 shǔ，高粱；轩，车','黍 shù，黄米；轩，亭'], a:0},
 {q:'本诗作者孟浩然，下列说法正确的是？', o:['盛唐山水田园诗代表，与王维并称「王孟」，一生多隐居襄阳鹿门山','中唐新乐府运动倡导者，主张「文章合为时而著」','豪放词的开创者，有「一蓑烟雨任平生」之句'], a:0},
 {q:'这首诗最打动人心的是？', o:['田家淳朴的情谊——鸡黍相邀、把酒闲话、重阳再约，真情不待铺张','壮志难酬的愤懑与牢骚','秋日登高的萧瑟与孤寂'], a:0},
];
"""

SCENES_JS = """/* ================= 过故人庄 · 四境场景（青绿春晓·田家做客：鸡黍邀客、绿树青山、开轩把酒、重阳菊约）
   本诗专属系统「绿树环抱」：绿树两弧自画面左右合拢于村后（村边合），青山斜倚郭外（郭外斜）——
   田园诗最著名的环抱构图，本诗标志性瞬间；
   末境点击——篱畔菊花次第开，重来访路（田间小路）一盏盏亮起，远天透出重阳的暖金 ================= */

/* —— 田家茅屋：土墙+双层草顶+暖窗+石烟囱（合批 1 mesh） —— */
function makeCotGRZ(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, d=o.d===undefined?5.2:o.d, h=o.h===undefined?2.9:o.h;
  const wall=o.wall===undefined?0x33291a:o.wall, thatch=o.thatch===undefined?0x68552a:o.thatch;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h/2,0); B.put(body,wall);
  const eave=new THREE.BoxGeometry(w+1.0,0.14,d+1.0); eave.translate(0,h-0.04,0);
  B.put(eave,shadeColor(0x463820,1.02));
  const door=new THREE.BoxGeometry(1.15,1.95,0.12); door.translate(-w*0.22,0.98,d/2+0.05); B.put(door,0x120e08);
  if(o.window!==false){
    const win=new THREE.BoxGeometry(0.95,0.85,0.10); win.translate(w*0.28,h*0.58,d/2+0.05);
    B.put(win,shadeColor(0xd8a850,0.55));
  }
  const rh=o.rh===undefined?1.8:o.rh;
  const r1=new THREE.ConeGeometry(1,rh,4); r1.rotateY(Math.PI/4);
  r1.scale((w+1.7)/1.414,1,(d+1.5)/1.414); r1.translate(0,h+rh/2+0.06,0); B.put(r1,thatch);
  const r2=new THREE.ConeGeometry(1,rh*0.56,4); r2.rotateY(Math.PI/4);
  r2.scale((w+1.7)*0.64/1.414,1,(d+1.5)*0.64/1.414); r2.translate(0,h+rh*0.80,0);
  B.put(r2,shadeColor(thatch,1.24));
  if(o.chimney){
    const ch=new THREE.BoxGeometry(0.36,1.0,0.36); ch.translate(w*0.30,h+0.30,-d*0.20);
    B.put(ch,shadeColor(0x4a4438,1.0));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a4430,emissive:0x0a0d06}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.24:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 篱笆：细桩+双横杆（合批 1 mesh） —— */
function makeFenceGRZ(o){
  o=o||{};
  const w=o.w===undefined?10:o.w, h=o.h===undefined?1.3:o.h, R=seedRnd(o.seed===undefined?11:o.seed);
  const n=Math.max(3,Math.round(w/0.66)), wood=o.wood===undefined?0x3c2f1c:o.wood;
  const B=new GeoBag();
  for(let i=0;i<=n;i++){
    const x=-w/2+w*i/n;
    const p=new THREE.BoxGeometry(0.09,h*(0.84+R()*0.28),0.09);
    p.rotateZ((R()-0.5)*0.09); p.translate(x,h*0.45,(R()-0.5)*0.1);
    B.put(p,shadeColor(wood,0.85+R()*0.35));
  }
  const r1=new THREE.BoxGeometry(w,0.08,0.06); r1.translate(0,h*0.76,0); B.put(r1,shadeColor(wood,1.14));
  const r2=new THREE.BoxGeometry(w,0.07,0.06); r2.translate(0,h*0.32,0); B.put(r2,shadeColor(wood,0.94));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x33301e,emissive:0x0a0906}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.16:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 团冠树：曲干+团簇树冠（合批 1 mesh） —— */
function makeTreeGRZ(o){
  o=o||{};
  const h=o.h===undefined?5:o.h, R=seedRnd(o.seed===undefined?7:o.seed);
  const leaf=o.leaf===undefined?0x16381f:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.5-0.25,h*0.62,0],h*0.05,h*0.022,6),0x241c12);
  const nb=o.blobs===undefined?3:o.blobs;
  for(let i=0;i<nb;i++){
    const bl=new THREE.SphereGeometry(h*(0.16+R()*0.10),8,6);
    bl.scale(1.14,0.86,1.14);
    bl.translate((R()-0.5)*h*0.30,h*(0.60+0.30*R()),(R()-0.5)*h*0.24);
    B.put(bl,shadeColor(leaf,0.8+R()*0.45));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2c3c28,emissive:0x081008}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.2:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 绿树合抱之弧：沿椭圆弧种一列树（全村的「环抱围墙」，标志性瞬间的主角，合批 1 mesh/弧） —— */
function makeTreeArcGRZ(o){
  o=o||{};
  const cx=o.cx===undefined?0:o.cx, cz=o.cz===undefined?-14:o.cz;
  const R=o.R===undefined?25:o.R, rz=o.rz===undefined?0.72:o.rz;
  const a0=o.a0, a1=o.a1, n=o.n===undefined?9:o.n, R2=seedRnd(o.seed===undefined?7:o.seed);
  const leaf=o.leaf===undefined?0x14331d:o.leaf, hh0=o.h===undefined?7.5:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const u=n===1?0.5:i/(n-1);
    const ang=a0+(a1-a0)*u;
    const x=cx+Math.cos(ang)*R, z=cz+Math.sin(ang)*R*rz;
    const hh=hh0*(0.8+R2()*0.5);
    const tk=limbGeo([x,0,z],[x+(R2()-0.5)*0.7,hh*0.6,z+(R2()-0.5)*0.5],hh*0.045,hh*0.02,6);
    B.put(tk,0x241c12);
    const nb=2+(R2()*2|0);
    for(let k=0;k<nb;k++){
      const bl=new THREE.SphereGeometry(hh*(0.17+R2()*0.10),8,6);
      bl.scale(1.12,0.85,1.12);
      bl.translate(x+(R2()-0.5)*hh*0.34,hh*(0.58+0.16*k+0.10*R2()),z+(R2()-0.5)*hh*0.26);
      B.put(bl,shadeColor(leaf,0.82+R2()*0.42));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2c3c28,emissive:0x081008}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.22:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 黍田/麻田：成行庄稼（黍带下垂金穗；ear:false 则是高挑麻秆，合批 1 mesh） —— */
function makeMilletGRZ(o){
  o=o||{};
  const rows=o.rows===undefined?4:o.rows, len=o.len===undefined?11:o.len, gap=o.gap===undefined?1.0:o.gap;
  const R=seedRnd(o.seed===undefined?71:o.seed);
  const ear=o.ear!==false, h0=o.h0===undefined?(ear?0.9:1.45):o.h0;
  const stalkC=o.stalk===undefined?(ear?0x4a6a2c:0x5a7a38):o.stalk;
  const earC=o.earC===undefined?0xd0a84e:o.earC;
  const B=new GeoBag();
  for(let r=0;r<rows;r++){
    for(let x=-len/2;x<len/2;x+=0.5){
      const px=x+(R()-0.5)*0.24, pz=r*gap+(R()-0.5)*0.3;
      const hh=h0+R()*0.45;
      const st=new THREE.CylinderGeometry(0.022,0.03,hh,4);
      st.translate(px,hh/2,pz); B.put(st,shadeColor(stalkC,0.85+R()*0.35));
      if(ear){
        const e=new THREE.ConeGeometry(0.055,0.30,4);
        e.translate(0,0.15,0); e.rotateX(2.55+R()*0.25); e.rotateY(R()*6.28);
        e.translate(px,hh,pz); B.put(e,shadeColor(earC,0.9+R()*0.25));
      }
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a5230,emissive:0x0a120a}),{c:0xc4dc9a,i:0.24,p:2.3}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 菜圃：三道田垄，垄上菜苗成球（合批 1 mesh） —— */
function makePlotGRZ(o){
  o=o||{};
  const rows=o.rows===undefined?3:o.rows, len=o.len===undefined?6.5:o.len, gap=o.gap===undefined?1.05:o.gap;
  const R=seedRnd(o.seed===undefined?73:o.seed);
  const B=new GeoBag();
  for(let r=0;r<rows;r++){
    const rd=new THREE.BoxGeometry(len,0.18,0.8); rd.translate(0,0.09,r*gap); B.put(rd,shadeColor(0x2e2416,1.0));
    for(let x=-len/2+0.3;x<len/2-0.2;x+=0.56){
      const m=new THREE.SphereGeometry(0.17+R()*0.08,6,5);
      m.scale(1,0.62,1); m.translate(x+(R()-0.5)*0.1,0.24,r*gap+(R()-0.5)*0.16);
      B.put(m,shadeColor(0x3a6a2c,0.85+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a5230,emissive:0x0a120a}),{c:0xc4dc9a,i:0.22,p:2.3}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 打谷场：晒场圆坪+两垛金谷（合批 1 mesh） —— */
function makeThreshGRZ(o){
  o=o||{};
  const r=o.r===undefined?3.1:o.r, R=seedRnd(o.seed===undefined?79:o.seed);
  const B=new GeoBag();
  const fl=new THREE.CylinderGeometry(r,r*1.04,0.10,18); fl.translate(0,0.05,0); B.put(fl,shadeColor(0x6a6250,1.0));
  const g1=new THREE.ConeGeometry(r*0.38,r*0.5,9); g1.translate(r*0.30,r*0.25,r*0.10); B.put(g1,shadeColor(0xb08c40,1.0+R()*0.1));
  const g2=new THREE.ConeGeometry(r*0.26,r*0.33,8); g2.translate(-r*0.36,r*0.17,-r*0.18); B.put(g2,shadeColor(0xa8813c,1.0));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3828,emissive:0x0a0a06}),{c:0xc0b088,i:0.18,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 篱下鸡群：觅食母鸡带红冠（合批 1 mesh，鸡黍的生活气） —— */
function makeHenGRZ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?47:o.seed), n=o.n===undefined?3:o.n, w=o.w===undefined?6:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*2.4, s=0.8+R()*0.35, peck=R()<0.5?0.55:0.15;
    const body=new THREE.SphereGeometry(0.24,8,6); body.scale(1.25,0.95,0.9); body.translate(x,0.26*s,z);
    B.put(body,shadeColor(0x8a5a30,0.85+R()*0.35));
    const head=new THREE.SphereGeometry(0.10,7,5); head.translate(x+0.30*s,0.26*s+peck*0.4,z);
    B.put(head,shadeColor(0x8a5a30,1.1));
    const comb=new THREE.BoxGeometry(0.05,0.09,0.09); comb.translate(x+0.28*s,0.26*s+peck*0.4+0.11,z);
    B.put(comb,0xc84a30);
    const beak=new THREE.ConeGeometry(0.035,0.10,5); beak.rotateZ(-Math.PI/2);
    beak.translate(x+0.42*s,0.26*s+peck*0.4,z); B.put(beak,0xd8a850);
    const tail=new THREE.ConeGeometry(0.10,0.30,5); tail.rotateZ(Math.PI/2.6);
    tail.translate(x-0.30*s,0.40*s,z); B.put(tail,shadeColor(0x5a3a20,1.0));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a3020,emissive:0x0a0805}),{c:0xc0a878,i:0.22,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 燕群：斜翅剪影掠过村野（每只 2 面片拍翅，共 1 材质） —— */
function makeSwallowGRZ(o){
  o=o||{};
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0x161e18:o.color,side:THREE.DoubleSide});
  const g=new THREE.Group(), items=[];
  const n=o.n===undefined?4:o.n;
  for(let i=0;i<n;i++){
    const b=new THREE.Group();
    const bd=new THREE.Mesh(new THREE.BoxGeometry(0.36,0.07,0.12),mat); b.add(bd);
    const w1=new THREE.Mesh(new THREE.PlaneGeometry(0.95,0.28),mat); w1.position.x=-0.5; w1.rotation.y=0.35;
    const w2=new THREE.Mesh(new THREE.PlaneGeometry(0.95,0.28),mat); w2.position.x=0.5; w2.rotation.y=-0.35;
    b.add(w1,w2); g.add(b);
    items.push({b,w1,w2,cx:o.cx===undefined?0:o.cx,cz:o.cz===undefined?-14:o.cz,
      r:(o.r===undefined?9:o.r)*(0.6+Math.random()*0.8),
      y:(o.y===undefined?11:o.y)+Math.random()*3.2,
      sp:(o.sp===undefined?0.3:o.sp)*(0.75+Math.random()*0.5),
      ph:Math.random()*6.283,sc:(o.scMin===undefined?0.5:o.scMin)+Math.random()*0.6});
  }
  const api={g,update(t){
    for(const it of items){
      const a=it.ph+t*it.sp;
      it.b.position.set(it.cx+Math.sin(a)*it.r,it.y+Math.sin(t*1.1+it.ph)*1.2,it.cz+Math.cos(a)*it.r*0.6);
      it.b.rotation.y=-a+Math.PI/2;
      it.b.scale.setScalar(it.sc);
      const f=Math.sin(t*7.5+it.ph)*0.5; it.w1.rotation.z=f; it.w2.rotation.z=-f;
    }
  }};
  return api;
}

/* —— 菊花：茎叶+花头（两层舌状花瓣，花头可缩放「次第开」；茎叶合批 1 mesh，花头独立 Group） —— */
function makeChrysGRZ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?61:o.seed);
  const h=o.h===undefined?0.85:o.h;
  const c=o.color===undefined?0xf2c94c:o.color;
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group();
  const B=new GeoBag();
  const stem=limbGeo([0,0,0],[R()*0.14-0.07,h,0],0.035,0.02,5); B.put(stem,0x2c4a24);
  for(let i=0;i<2;i++){
    const lf=new THREE.PlaneGeometry(0.34,0.12);
    lf.rotateZ(0.5+R()*0.5); lf.rotateY(R()*1.6);
    lf.translate(R()*0.12-0.06,h*(0.32+0.22*i),0); B.put(lf,shadeColor(0x2c4a24,1.1));
  }
  const stemMesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a5230,emissive:0x0a120a,side:THREE.DoubleSide}),{c:0xc4dc9a,i:0.24,p:2.3}));
  g.add(stemMesh);
  const head=new THREE.Group();
  const HB=new GeoBag();
  const core=new THREE.SphereGeometry(0.075,7,5); HB.put(core,shadeColor(c,1.28));
  for(let ring=0;ring<2;ring++){
    const np=8, tilt=1.18-ring*0.34;
    for(let i=0;i<np;i++){
      const a=i/np*6.283+ring*0.42;
      const petal=new THREE.ConeGeometry(0.045,0.24-0.05*ring,4);
      petal.translate(0,0.12,0);
      petal.rotateX(tilt); petal.rotateY(a);
      HB.put(petal,shadeColor(c,1.0+0.22*ring+R()*0.12));
    }
  }
  const headMesh=HB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x5a4a20,emissive:0x1a1406,side:THREE.DoubleSide}),{c:0xf2d488,i:0.30,p:2.3}));
  head.add(headMesh);
  head.position.y=h+0.03;
  head.scale.setScalar(0.22);
  g.add(head);
  g.scale.setScalar(s);
  return {g,head,setBloom(b){ head.scale.setScalar(0.22+0.78*b); },
    update(t,k){ g.rotation.z=0.05*Math.sin(t*0.7+R()*6.28)*k; }};
}

/* —— 孟浩然（客）：蓝灰袍幞头，全诗一线贯穿（每次 build 新建材质） —— */
function grzGuest(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x35404a,belt:0x6a5638,skin:0xd9b189,collar:0xb8c0cc,
    hair:0x14161c,hat:'幞头',beard:true,rimC:0xa3c98f,rim:0.42,noProp:true,scale:scale});
}
/* —— 田家主人：土褐短褐装，发髻 —— */
function grzHost(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x52432a,belt:0x8f6a33,skin:0xd9b189,collar:0xc0a878,
    hair:0x181410,hat:'发髻',beard:true,rimC:0xa3c98f,rim:0.42,noProp:true,scale:scale});
}

function bCover(){ // 卷首 · 田家晓色 —— 绿树环抱的村郭远影，田野铺展，晨光熹微
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0b150e,c2:0x16281a,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:3,peaks:5,seed:215,color:0x0c1911,atmo:0x2c4434,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-85); g.add(ridge.g);
  /* 村郭远影：绿树弧一痕环着两三茅屋 */
  const cot1=makeCotGRZ({w:7,d:5,h:2.8,window:false}); cot1.g.position.set(-13,-1.6,-44); cot1.g.rotation.y=0.45; g.add(cot1.g);
  const cot2=makeCotGRZ({w:5.5,d:4.4,h:2.5,window:false}); cot2.g.position.set(-4,-1.6,-52); cot2.g.rotation.y=-0.2; g.add(cot2.g);
  const arcB=makeTreeArcGRZ({cx:-8,cz:-48,R:16,rz:0.7,a0:2.3,a1:4.4,n:6,h:6.5,seed:31}); g.add(arcB.g);
  const t1=makeTreeGRZ({h:7,seed:9,scale:1.4}); t1.g.position.set(-24,-1.6,-38); g.add(t1.g);
  const t2=makeTreeGRZ({h:6,seed:13,scale:1.1}); t2.g.position.set(20,-1.6,-46); g.add(t2.g);
  /* 田畴与一湾溪水 */
  const mil=makeMilletGRZ({rows:4,len:16,gap:1.0,seed:33}); mil.g.position.set(8,-1.5,-30); mil.g.rotation.y=0.3; g.add(mil.g);
  const water=makeWater({size:13,seg:20,amp:0.10,freq:0.16,speed:0.4,flow:[0.15,0.5],spec:1.0,
    deep:0x0a1a12,shallow:0x1e4a34,skyc:0x2c5840,moonDir:[-60,90,-160],y:-1.5});
  water.mesh.scale.set(1,1,12); water.mesh.rotation.y=Math.PI/2;
  water.mesh.position.set(14,-1.5,-26); g.add(water.mesh);
  /* 燕群两点 + 村人一痕 */
  const sw=makeSwallowGRZ({n:2,cx:2,cz:-34,y:10,r:10,scMin:0.4}); g.add(sw.g);
  const crowd=makeCrowd({n:4,rect:[0,-38,18,7],seed:67,color:0x131e14,rimC:0xa3c98f,rim:0.2});
  crowd.mesh.position.y=-1.5; g.add(crowd.mesh);
  /* 晨光熹微：东天一抹暖意（青绿底上唯一的暖，随呼吸微明） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.15,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,60,1); dawn.position.set(-60,26,-120); dawn.renderOrder=-7; g.add(dawn);
  const motes=makeGlow({n:40,box:[190,26,100],pos:[0,8,-26],color:0xcfe0a8,size:6,speed:0.03,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,30,130],pos:[0,10,-52],scale:78,color:0x1e3424,op:0.12});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:50,n:9,d:7,color:0x081009,seed:19,sway:0.7,rim:0.12,rimC:0xa3c98f});
  brL.g.position.set(-26,-1.6,40); brL.g.scale.setScalar(2.0); g.add(brL.g);
  const rkR=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x060c08,seed:21,rim:0.14,rimC:0xa3c98f});
  rkR.g.position.set(17,-1.4,15); g.add(rkR.g);
  addLights(g,{c:0xe8d8a8,i:0.46,p:[-50,80,30]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    brL.update(t,k); rkR.update(t,k); crowd.update(t); sw.update(t);
    dawn.material.opacity=k*(0.11+0.03*Math.sin(t*0.4));
  }};
}

function bJishu(){ // 一 · 鸡黍邀客 —— 故人具鸡黍，邀我至田家（炊烟起，主人候客，黍田夹路）
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0b150e,c2:0x16281a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:2,peaks:4,seed:219,color:0x09150e,atmo:0x2c4434,
    fogK:0.60,glowK:0.04,glow:0xaac890,y:-7});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 田埂小路：从相机脚下通向院门 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.08,42),
    new THREE.MeshPhongMaterial({color:0x4c4830,shininess:4,emissive:0x12110a}));
  path.position.set(1.8,0.04,4); g.add(path);
  /* 田家：茅屋（带石烟囱）+ 篱笆两段夹一门 */
  const cot=makeCotGRZ({w:8,d:5.5,h:3.0,chimney:true}); cot.g.position.set(-3.4,0,-16); cot.g.rotation.y=0.35; g.add(cot.g);
  const feL=makeFenceGRZ({w:9,seed:23}); feL.g.position.set(-9.6,0,-13.4); feL.g.rotation.y=0.42; g.add(feL.g);
  const feR=makeFenceGRZ({w:7,seed:25}); feR.g.position.set(2.6,0,-11.4); feR.g.rotation.y=0.68; g.add(feR.g);
  /* 具鸡黍：灶烟自烟囱袅袅而起 + 暖窗 */
  const smoke=makeGlow({n:26,box:[1.3,6.5,1.3],pos:[-3.6,4.3,-17.2],color:0xcfd0c0,size:6,speed:0.4,rise:1,maxA:0.26});
  g.add(smoke.points);
  /* 篱下鸡群（鸡黍之鸡）+ 院角草垛 */
  const hens=makeHenGRZ({n:3,seed:47,w:5}); hens.g.position.set(-5.8,0,-11.2); g.add(hens.g);
  const stack=new THREE.Mesh(new THREE.ConeGeometry(1.05,1.5,8),
    new THREE.MeshPhongMaterial({color:0x8a6a30,shininess:4,emissive:0x120e06}));
  stack.position.set(5.4,0.75,-13.6); g.add(stack);
  /* 黍田两畦夹路（既是鸡黍之黍，也是田家本色） */
  const milL=makeMilletGRZ({rows:4,len:12,gap:1.0,seed:71}); milL.g.position.set(-8.5,0,1.5); milL.g.rotation.y=0.05; g.add(milL.g);
  const milR=makeMilletGRZ({rows:4,len:12,gap:1.0,seed:75}); milR.g.position.set(11.5,0,-1.5); milR.g.rotation.y=0.05; g.add(milR.g);
  /* 主人候于篱门（指途相邀），客人沿路走来 */
  const host=grzHost(1.42,'指月'); host.position.set(0.6,0,-10.6); host.rotation.y=-0.4; g.add(host);
  const guest=grzGuest(1.4,'独立'); guest.position.set(1.7,0,3.6); guest.rotation.y=3.0; g.add(guest);
  /* 远处田里农人一痕 + 村树 */
  const crowd=makeCrowd({n:3,rect:[10,-30,16,7],seed:77,color:0x121c13,rimC:0xa3c98f,rim:0.18});
  g.add(crowd.mesh);
  const t1=makeTreeGRZ({h:6.5,seed:81,scale:1.2}); t1.g.position.set(-14,0,-20); g.add(t1.g);
  const t2=makeTreeGRZ({h:7,seed:83,scale:1.3}); t2.g.position.set(14,0,-22); g.add(t2.g);
  const motes=makeGlow({n:30,box:[120,18,60],pos:[0,7,-12],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[200,22,100],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x070d08,seed:41,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(-14,-1.1,13); g.add(rk.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:43,sway:1.1,tip:0x2c4028});
  reed.g.position.set(15,-1.0,14); g.add(reed.g);
  addLights(g,{c:0xe8d2a0,i:0.46,p:[35,70,25]},{c:0x21301f,i:0.66});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); smoke.update(t);
      rk.update(t,k); reed.update(t,k); crowd.update(t);
      host.update(t,k); guest.update(t,k);
      stack.rotation.y=0;
    },onEnter(){   // 鸡鸣两声（WebAudio 可用时）
      pluck(5,0.15,0.08); pluck(3,0.6,0.07);
    }};
}

function bLvhe(){ // 二（标志性瞬间）· 绿树青山 —— 绿树村边合（两弧合抱），青山郭外斜（斜倚村郭）
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0b150e,c2:0x16281a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:260,h:40,layers:3,peaks:5,seed:223,color:0x09150e,atmo:0x2c4434,
    fogK:0.60,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-112); g.add(ridge.g);
  /* 青山郭外斜：一道山梁斜倚在村郭右侧之外 */
  const hill=makeRange({r:170,h:26,layers:2,peaks:3,seed:225,color:0x10281c,atmo:0x2c4434,
    fogK:0.56,glowK:0.05,glow:0x9ec488,y:-6});
  hill.g.position.set(30,0,-52); hill.g.rotation.y=-0.62; g.add(hill.g);
  /* 村郭：矮土墙一痕横在村后（郭） */
  const wallB=new GeoBag();
  const wl=new THREE.BoxGeometry(10,1.0,0.7); wl.translate(-11.5,0.5,-26); wallB.put(wl,shadeColor(0x2e2a20,1.0));
  const wr=new THREE.BoxGeometry(10,1.0,0.7); wr.translate(11.5,0.5,-26); wallB.put(wr,shadeColor(0x322d22,1.0));
  const wallM=wallB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4}),
    {c:0xa3c98f,i:0.12,p:2.4}));
  g.add(wallM);
  /* 村中：茅屋三两 + 草垛 + 篱笆 */
  const cot1=makeCotGRZ({w:7,d:5,h:2.9}); cot1.g.position.set(-2.2,0,-12); cot1.g.rotation.y=0.2; g.add(cot1.g);
  const cot2=makeCotGRZ({w:5.6,d:4.4,h:2.5}); cot2.g.position.set(5,0,-17); cot2.g.rotation.y=-0.16; g.add(cot2.g);
  const cot3=makeCotGRZ({w:5,d:4,h:2.3,window:false}); cot3.g.position.set(-7.6,0,-19); cot3.g.rotation.y=0.55; g.add(cot3.g);
  const fe=makeFenceGRZ({w:8,seed:27}); fe.g.position.set(1.5,0,-8.6); g.add(fe.g);
  const st1=new THREE.Mesh(new THREE.ConeGeometry(1.1,1.6,8),
    new THREE.MeshPhongMaterial({color:0x8a6a30,shininess:4,emissive:0x120e06}));
  st1.position.set(-5.6,0.8,-10.5); g.add(st1);
  /* ★ 绿树村边合：两弧绿树自左右合拢于村后 —— 田园诗最著名的环抱构图 */
  const arcL=makeTreeArcGRZ({cx:0,cz:-14,R:25,rz:0.72,a0:2.15,a1:4.75,n:9,h:7.5,seed:51});
  g.add(arcL.g);
  const arcR=makeTreeArcGRZ({cx:0,cz:-14,R:25,rz:0.72,a0:-1.61,a1:0.99,n:9,h:7.8,seed:57});
  g.add(arcR.g);
  const tf1=makeTreeGRZ({h:7,seed:59,scale:1.2}); tf1.g.position.set(-17.5,0,2); g.add(tf1.g);
  const tf2=makeTreeGRZ({h:7.5,seed:63,scale:1.25}); tf2.g.position.set(17.5,0,1); g.add(tf2.g);
  /* 燕群掠村 + 村人一痕 */
  const sw=makeSwallowGRZ({n:4,cx:0,cz:-14,y:11,r:10,scMin:0.4}); g.add(sw.g);
  const crowd=makeCrowd({n:3,rect:[0,-21,14,6],seed:81,color:0x121c13,rimC:0xa3c98f,rim:0.18});
  g.add(crowd.mesh);
  const motes=makeGlow({n:32,box:[130,20,70],pos:[0,8,-14],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[210,24,110],pos:[0,9,-50],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:34,n:7,d:6,color:0x081009,seed:61,sway:0.8,rim:0.14,rimC:0xa3c98f});
  brL.g.position.set(-19,-1.2,12); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x070d08,seed:63,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(14,-1.2,12); g.add(rk.g);
  addLights(g,{c:0xdccf9a,i:0.46,p:[-40,80,30]},{c:0x22301f,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); hill.update(t,0); mist.update(t,k); motes.update(t);
      brL.update(t,k); rk.update(t,k); crowd.update(t); sw.update(t);
    }};
}

function bKaixuan(){ // 三 · 开轩把酒 —— 开轩面场圃，把酒话桑麻（宾主对酌，场圃在望）
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0c160e,c2:0x18261a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:2,peaks:4,seed:229,color:0x091409,atmo:0x2a4230,
    fogK:0.58,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 茅屋开轩（暖窗向着席面） */
  const cot=makeCotGRZ({w:9,d:5,h:3.1}); cot.g.position.set(-2.5,0,-12); cot.g.rotation.y=0.18; g.add(cot.g);
  /* 小案 + 盘飧 + 酒器（樽/壶/杯二/碗） */
  const tb=makeTable({w:5.2,d:2.4,h:1.5}); tb.g.position.set(0,0,-3.2); g.add(tb.g);
  const dz1=makeDish({r:0.7,n:4}); dz1.g.position.set(-1.5,1.5,-3.6); g.add(dz1.g);
  const dz2=makeDish({r:0.7,n:3}); dz2.g.position.set(1.4,1.5,-3.0); g.add(dz2.g);
  const jz=makeVessel({type:'樽',mat:'陶',scale:0.85,liquid:true}); jz.g.position.set(0,1.5,-3.8); g.add(jz.g);
  const hp=makeVessel({type:'壶',mat:'陶',scale:0.66}); hp.g.position.set(-2.1,1.5,-3.0); g.add(hp.g);
  const c1=makeVessel({type:'杯',mat:'陶',scale:0.85,liquid:true}); c1.g.position.set(0.8,1.5,-2.5); g.add(c1.g);
  const c2=makeVessel({type:'杯',mat:'陶',scale:0.85,liquid:true}); c2.g.position.set(-0.7,1.5,-2.4); g.add(c2.g);
  const wz=makeVessel({type:'碗',mat:'陶',scale:0.85}); wz.g.position.set(2.1,1.5,-3.6); g.add(wz.g);
  /* 樽上酒气 */
  const steam=makeGlow({n:18,box:[1.2,1.8,1.2],pos:[0,2.7,-3.8],color:0xdce8cc,size:4,speed:0.5,rise:1,maxA:0.18});
  g.add(steam.points);
  /* 宾主对酌：主人指谈农事，客举杯相听 */
  const host=grzHost(1.42,'指月'); host.position.set(-2.7,0,-1.6); host.rotation.y=1.1; g.add(host);
  const guest=grzGuest(1.4,'举杯'); guest.position.set(2.7,0,-1.4); guest.rotation.y=-1.0; g.add(guest);
  /* 场圃在望：打谷场（晒场+谷堆）与菜圃 */
  const th=makeThreshGRZ({r:3.1,seed:87}); th.g.position.set(7.5,0,-9); g.add(th.g);
  const plot=makePlotGRZ({rows:3,len:6.5,gap:1.05,seed:73}); plot.g.position.set(-8.5,0,-6); plot.g.rotation.y=0.3; g.add(plot.g);
  /* 桑麻：桑树两株 + 麻田一畦 */
  const mb1=makeTreeGRZ({h:6,seed:91,scale:1.2,leaf:0x1e4028}); mb1.g.position.set(11,0,-17); g.add(mb1.g);
  const mb2=makeTreeGRZ({h:5.5,seed:93,scale:1.0,leaf:0x1e4028}); mb2.g.position.set(-11,0,-17); g.add(mb2.g);
  const hemp=makeMilletGRZ({rows:3,len:8,gap:1.1,ear:false,h0:1.5,seed:95}); hemp.g.position.set(12.5,0,-11); hemp.g.rotation.y=0.35; g.add(hemp.g);
  /* 场上农人一痕 + 燕两行 */
  const crowd=makeCrowd({n:2,rect:[6,-13,10,5],seed:97,color:0x121c13,rimC:0xa3c98f,rim:0.16});
  g.add(crowd.mesh);
  const sw=makeSwallowGRZ({n:2,cx:-2,cz:-10,y:9,r:8,scMin:0.45}); g.add(sw.g);
  const motes=makeGlow({n:26,box:[100,16,50],pos:[0,6,-10],color:0xe0d0a0,size:5,speed:0.05,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[180,20,90],pos:[0,8,-50],scale:70,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x070d08,seed:99,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(-12,-1.2,11); g.add(rk.g);
  const brR=makeForeground({kind:'树枝',w:28,n:6,d:5,color:0x081009,seed:101,sway:0.8,rim:0.14,rimC:0xa3c98f});
  brR.g.position.set(14,-1.0,10); g.add(brR.g);
  addLights(g,{c:0xeed49c,i:0.5,p:[30,68,28]},{c:0x22301f,i:0.68});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); steam.update(t);
      rk.update(t,k); brR.update(t,k); crowd.update(t); sw.update(t);
      host.update(t,k); guest.update(t,k);
      jz.update(t,k); c1.update(t,k); c2.update(t,k); hp.update(t,k);
      dz1.glow.material.opacity=k*0.16*(0.8+0.2*Math.sin(t*1.1));
      dz2.glow.material.opacity=k*0.16*(0.8+0.2*Math.sin(t*1.2+1.4));
    }};
}

function bChongyang(){ // 四（末境·可点击）· 重阳菊约 —— 点击：菊花次第开，重来访路亮起
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,open:0,pulse:0};
  const grd=makeGround({r:130,c1:0x0c160e,c2:0x18261a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:2,peaks:4,seed:237,color:0x091409,atmo:0x2a4230,
    fogK:0.58,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  /* 茅屋暖窗作底，长篱横贯，中间篱门 */
  const cot=makeCotGRZ({w:8,d:5,h:2.9}); cot.g.position.set(-2,0,-15); g.add(cot.g);
  const feL=makeFenceGRZ({w:14,seed:107}); feL.g.position.set(-7.6,0,-5.4); g.add(feL.g);
  const feR=makeFenceGRZ({w:12,seed:109}); feR.g.position.set(10,0,-5.4); g.add(feR.g);
  /* 重来访路：自篱门向左后田间的土路（点击后一盏盏亮起） */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.2,0.06,30),
    new THREE.MeshPhongMaterial({color:0x4c4830,shininess:4,emissive:0x12110a}));
  path.rotation.y=3.81; path.position.set(-3.5,0.03,-13.4); g.add(path);
  /* 重阳菊约：篱畔三丛菊花（点击后次第开） */
  const flowers=[];
  const clumps=[[[-3.6,-3.2],[-2.7,-3.9],[-4.4,-3.8],[-3.1,-2.6],[-4.9,-3.0]],
                [[0.9,-4.6],[1.8,-5.0],[0.4,-5.3],[1.3,-4.0]],
                [[5.5,-4.2],[6.4,-4.6],[4.8,-4.8]]];
  let ci=0;
  const cols=[0xf2c94c,0xe8d88a,0xf2c94c,0xe8e4d0,0xf2c94c];
  for(let c=0;c<clumps.length;c++){
    for(let i=0;i<clumps[c].length;i++){
      const fl=makeChrysGRZ({h:0.8+Math.random()*0.3,color:cols[ci%cols.length],
        scale:0.95+Math.random()*0.4,seed:120+ci});
      fl.g.position.set(clumps[c][i][0],0,clumps[c][i][1]);
      fl.delay=ci*0.055;                       // 次第开：逐朵延迟
      g.add(fl.g); flowers.push(fl); ci++;
    }
  }
  /* 重来访路的灯：沿路七点（点击后逐盏亮起） */
  const lamps=[];
  for(let i=0;i<7;i++){
    const d=3.0+i*3.0;
    const lp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf2c94c,
      transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    lp.scale.set(3.4,2.2,1);
    lp.position.set(2.6-0.62*d,1.15,-5.4-0.78*d);
    lp.renderOrder=4; g.add(lp); lamps.push(lp);
  }
  /* 主人篱门指途相约，客人回首应约 */
  const host=grzHost(1.42,'指月'); host.position.set(1.3,0,-4.4); host.rotation.y=0.5; g.add(host);
  const guest=grzGuest(1.4,'独立'); guest.position.set(4.2,0,-2.6); guest.rotation.y=3.6; g.add(guest);
  /* 远天一抹暖金：重阳之约的期许色（点击后渐亮） */
  const hope=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf2c06a,
    transparent:true,opacity:0.38,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  hope.scale.set(130,46,1); hope.position.set(-70,20,-75); hope.renderOrder=-7; g.add(hope);
  const burst=makeBurst({n:64,color:0xffe0a0,pos:[-3.6,1.5,-3.2]}); g.add(burst.points);
  const pl=new THREE.PointLight(0xf2c884,1.25,40); pl.position.set(-3.4,2.4,-3.4); g.add(pl);
  /* 秋意一树（金叶）+ 村树 + 燕一点 */
  const at=makeTreeGRZ({h:6.5,seed:111,scale:1.25,leaf:0x6a5a26}); at.g.position.set(-14,0,-11); g.add(at.g);
  const t2=makeTreeGRZ({h:7,seed:113,scale:1.3}); t2.g.position.set(13,0,-14); g.add(t2.g);
  const sw=makeSwallowGRZ({n:1,cx:2,cz:-12,y:10,r:8,scMin:0.5}); g.add(sw.g);
  const motes=makeGlow({n:28,box:[110,18,60],pos:[0,7,-12],color:0xe0d0a0,size:5,speed:0.05,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[200,22,100],pos:[0,8,-52],scale:72,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:115,sway:1.1,tip:0x4a4428});
  reed.g.position.set(-15,-1.0,13); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:6,color:0x070d08,seed:117,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(14,-1.2,12); g.add(rk.g);
  addLights(g,{c:0xf0d49c,i:0.5,p:[25,68,28]},{c:0x22301f,i:0.68});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.open=Math.min(1,ctl.open+dt/2.6);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      reed.update(t,k); rk.update(t,k); sw.update(t);
      host.update(t,k); guest.update(t,k);
      /* 菊花次第开：按 delay 逐朵舒展（缩放，无透明度写入） */
      for(let i=0;i<flowers.length;i++){
        const fl=flowers[i];
        let b=(ctl.open-fl.delay)/0.42; b=b<0?0:(b>1?1:b);
        b=b*b*(3-2*b);
        fl.setBloom(b);
        fl.update(t,k);
      }
      /* 重来访路：逐盏亮起 + 轻微呼吸（峰值 0.30 = 初值，每帧乘 fadeK） */
      for(let i=0;i<lamps.length;i++){
        let li=(ctl.open-(0.10+i*0.09))/0.22; li=li<0?0:(li>1?1:li);
        li=li*li*(3-2*li);
        lamps[i].material.opacity=k*0.30*li*(0.86+0.14*Math.sin(t*2.1+i));
      }
      /* 期许的暖金：随约期渐亮 + 点击脉冲（公式峰值 0.37 ≤ 初值 0.38） */
      hope.material.opacity=k*(0.05+0.20*ctl.open+0.12*ctl.pulse);
      pl.intensity=k*1.25*(0.30+0.70*ctl.pulse);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.15); pluck(2,0.35,0.12); pluck(4,0.8,0.11); pluck(6,1.3,0.09);
        const fl=$('#flash'); fl.textContent='还来就菊花'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      burst.fire(); ctl.pulse=1;               // 可再点：菊开之势再涨一拍
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x132a1e),hor:C(0x35543a),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0058,star:0.12,
  moon:new THREE.Vector3(-95,64,-210),ms:0.55,mph:0.42,mhaze:0.05,dirC:C(0xe6cd92),dirI:0.5,
  dirP:new THREE.Vector3(-55,75,45),ambC:C(0x25331f),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,11,62],t:[0,12,55],lf:[-4,9,-30],lt:[-5,10,-32]},
  sky:()=>SK({top:C(0x152c20),hor:C(0x3a5c40),bot:C(0x0c1710),fog:C(0x0e1d16),fd:0.0050,star:0.10,
    ms:0.45,mph:0.46,mhaze:0.04,moon:new THREE.Vector3(-80,58,-220),
    dirC:C(0xe8d094),dirI:0.46,ambC:C(0x27351f),ambI:0.68}) },
{ name:'鸡黍邀客',dwell:17,river:0.04,build:bJishu,
  cam:{f:[2.5,6.2,24],t:[-0.5,5.8,21],lf:[-1,2.4,-2],lt:[-2,2.3,-3]},
  sky:()=>SK({top:C(0x122818),hor:C(0x31503a),bot:C(0x0a1410),fog:C(0x0f1e17),fd:0.0056,star:0.12,
    ms:0.42,mph:0.44,mhaze:0.05,moon:new THREE.Vector3(-95,64,-210),
    dirC:C(0xe6cd92),dirI:0.48,dirP:new THREE.Vector3(-50,72,40),ambC:C(0x25331f),ambI:0.66}) },
{ name:'绿树青山',dwell:18,river:0.04,build:bLvhe,
  cam:{f:[0,10,30],t:[0,10.4,26.5],lf:[0,3.4,-14],lt:[0,3.3,-15]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x36543c),bot:C(0x0a1410),fog:C(0x0f1e17),fd:0.0058,star:0.12,
    ms:0.45,mph:0.46,mhaze:0.05,moon:new THREE.Vector3(-100,62,-205),
    dirC:C(0xf0d69a),dirI:0.5,dirP:new THREE.Vector3(50,70,35),ambC:C(0x26341f),ambI:0.68}) },
{ name:'开轩把酒',dwell:17,river:0.02,build:bKaixuan,
  cam:{f:[3.4,5.2,12.5],t:[-1.6,4.9,10],lf:[0,2.2,-2.5],lt:[0,2.1,-3]},
  sky:()=>SK({top:C(0x152a1c),hor:C(0x3a563c),bot:C(0x0b150f),fog:C(0x101f17),fd:0.0060,star:0.12,
    ms:0.45,mph:0.46,mhaze:0.05,moon:new THREE.Vector3(-105,60,-200),
    dirC:C(0xf0d69a),dirI:0.52,dirP:new THREE.Vector3(40,68,32),ambC:C(0x27351f),ambI:0.68}) },
{ name:'重阳菊约',dwell:18,river:0.03,build:bChongyang,
  cam:{f:[2.2,5.4,16.5],t:[-0.6,5.1,14],lf:[1,2.0,-4],lt:[0,2.0,-5]},
  sky:()=>SK({top:C(0x162c1c),hor:C(0x3c583c),bot:C(0x0b150f),fog:C(0x101f17),fd:0.0062,star:0.12,
    ms:0.45,mph:0.44,mhaze:0.06,moon:new THREE.Vector3(-110,58,-200),
    dirC:C(0xf2d89c),dirI:0.52,dirP:new THREE.Vector3(30,66,30),ambC:C(0x27351f),ambI:0.68}) },
];
"""
