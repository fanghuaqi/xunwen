# -*- coding: utf-8 -*-
"""ti-poshansi.py —— 《题破山寺后禅院》（唐·常建，queue no.218，水墨夜思）生成配置
四境（N=queue stages 数）：初日高林（清晨入古寺·初日照高林）、竹径禅房（竹径通幽处·禅房花木深
——标志性瞬间）、山光潭影（山光悦鸟性·潭影空人心）、万籁钟磬（万籁此都寂·但余钟磬音——末境点击）。
水墨夜思全套色板：底色 #0d1117、雾 #131a26 系、文字 #dfe6f0，accent=#98aec8（queue 分配强调色，
淡青晨蓝）只落在初日晕/边缘光/音波环/UI 上，全页近零饱和。本诗是清晨时相：水墨夜思的冷银里
放一轮淡日（无月，ms 0.001 移出视野；淡日自建 makeChuri，fog:false），晨雾横腰、晨光斜柱。
标志性瞬间（境贰·全诗名联）：曲径通幽的纵深——石径沿弧线没入竹径深处，两侧带节竹丛渐远渐矮，
禅房半隐在花木与晨雾深处，一眼望不到底。
末境点击（queue interact）：点击钟磬音——一声磬响（bell）+ 音波环自禅房荡开（横向 Ring 逐环
扩散淡出，余韵不绝），窗纸微光轻颤、万籁愈静，「但余钟磬音」。
考点钉子：禅 chán / 磬 qìng / 籁 lài（小测第 3 题落点）；「曲径通幽」成语出处（第 4 题）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='ti-poshansi', title='题破山寺后禅院', dyn='唐 · 常建', brand_author='常 建',
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
        ('rgba(5,8,15', 'rgba(9,14,22', 1),
        ('rgba(4,6,11', 'rgba(8,12,19', 2),
        ('rgba(6,9,16', 'rgba(10,15,23', 1),
        ('rgba(3,5,9', 'rgba(6,9,15', 1),
        ('#0b101c', '#121a28', 1),
        ('#6f664f', '#5f6c80', 1),
        ('#5a5340', '#526074', 1),
        ('0x0a1526', '0x131a26', 4),
    ],
    tip='轻点画面 / 按空格 —— 磬音一声，自禅房荡开',
    hint='← → 键或空格逐境游览 · 末境可点击画面：听一声磬响，看音波自禅房荡开',
    cover_read='题破山寺后禅院。唐，常建。清晨入古寺，初日照高林。竹径通幽处，禅房花木深。山光悦鸟性，潭影空人心。万籁此都寂，但余钟磬音。',
    cover_p1='四重意境，随诗句次第展开：清晨入寺、初日正照上高林的明朗开篇；竹径蜿蜒通幽、禅房深藏花木的曲径纵深；山光使鸟性欢悦、潭影使人心涤净的物我相契；末了万籁俱寂、只余钟磬一声的空明收束。',
    cover_p2='边读诗，边跟着常建走进清晨的古寺：这条「曲径通幽」的小路后来成了汉语里最著名的一条路——读懂了路越走越深、心越走越静这条暗线，就读懂了这首题壁诗的禅意。',
    end_h2='钟磬 · 心空', cn_word='四',
    words_js="['再入一次古寺','初识常建，尚需共读','渐入诗境，再诵几遍','曲径渐深，禅意渐明','已解钟磬空人心','万籁俱寂，余音在心']",
    sky_atmo='0x1c2836',
)

POEM_JS = """const POEM = [
{ name:'初日高林', jing:'清晨走进古寺，初升的太阳正照上高耸的林梢 —— 古寺晨光，禅境初开。（古寺 · 初日 · 高林）',
  segs:[
   {c:'清晨入古寺，', p:py('qīng chén rù gǔ sì')},
   {c:'初日照高林。', p:py('chū rì zhào gāo lín')}],
  read:'清晨入古寺，初日照高林。',
  yisi:'清晨走进这座古老的寺院，初升的太阳正照在高高的树林上。——起笔是「入寺」的时与景：清晨、古寺、初日、高林，四个意象一齐落定，无一句抒情而清新庄穆之气自现。「初日」是刚刚升起的太阳，「照高林」让光线有了高度与方向——一天之中最早的、也是最干净的一段光阴，被诗人赶上了。',
  zhu:[['题','书写、题写——这是一首题壁诗：诗人清晨游寺，在后禅院题诗纪游'],['初日','初升的太阳'],['古寺','指破山寺，故址在今江苏常熟虞山，后改名兴福寺'],['高林','高耸的树林——佛家称僧众聚集修行之处为「丛林」，「高林」亦暗指禅林寺院']] },
{ name:'竹径禅房', jing:'竹林小径蜿蜒，通向幽深之处；禅房就藏在花木丛的深处 —— 曲径通幽的纵深。（竹径 · 幽处 · 禅房）（标志性瞬间）',
  segs:[
   {c:'竹径通幽处，', p:py('zhú jìng tōng yōu chù')},
   {c:'禅房花木深。', p:py('chán fáng huā mù shēn')}],
  read:'竹径通幽处，禅房花木深。',
  yisi:'穿过寺内，一条竹林小径蜿蜒着通向幽深之处，禅房就掩映在花木丛的深处。——全诗最著名的十个字：小径是「通」，一眼望不到尽头是「幽」，禅房被花木层层围住是「深」——三个字都在写纵深，路越走越深，心也随之越走越静。后世由此凝练出成语「曲径通幽」。',
  zhu:[['竹径','竹林间的小路。教材通行本作「竹径」（语料作「竹迳」，一作「曲径」）——语意相同：小路在竹丛间蜿蜒'],['通幽处','通向幽深的地方。幽，幽静、幽深'],['禅房','僧人居住、静修的房舍'],['深','茂盛、幽深——「花木深」是花木层层掩映，禅房若隐若现'],['曲径通幽','「竹径通幽处，禅房花木深」后世凝练为成语「曲径通幽」，形容环境幽静雅致、道路蜿蜒深远——汉语里最著名的一条「路」']] },
{ name:'山光潭影', jing:'山间风光让鸟儿欢悦，潭中倒影使人心中的杂念涤净 —— 山光潭影，物我两忘。（山光 · 潭影 · 飞鸟）',
  segs:[
   {c:'山光悦鸟性，', p:py('shān guāng yuè niǎo xìng')},
   {c:'潭影空人心。', p:py('tán yǐng kōng rén xīn')}],
  read:'山光悦鸟性，潭影空人心。',
  yisi:'山间的明媚风光让飞鸟欢悦，潭中空明的倒影让人心中的尘念涤荡净尽。——「悦」与「空」是全诗诗眼，都作使动用：山光使鸟性欢悦，是写物之乐；潭影使人心空明，是写我之净。一外一内、一物一我，互文见义——山水既悦了鸟，也空了人；走到此处，尘心自然放下。',
  zhu:[['山光','山间风光、山色'],['悦鸟性','使鸟性欢悦。悦，使动用法：使……欢悦'],['潭影','潭水中倒映的山光日影——天光云影在潭中空明晃动'],['空人心','使人心中的杂念涤除净尽。空，使动用法：使……空明、涤净'],['诗眼','「悦」「空」二字：一写物（鸟性悦）、一写我（人心空），景中含情，是全诗精神所在']] },
{ name:'万籁钟磬', jing:'此时此地万籁俱寂，只留下钟磬的余音在回荡 —— 一切声响都退去，只剩这一声清音。（万籁俱寂 · 钟磬 · 末境点击画面：磬音一声，音波自禅房荡开）',
  segs:[
   {c:'万籁此都寂，', p:py('wàn lài cǐ dōu jì')},
   {c:'但余钟磬音。', p:py('dàn yú zhōng qìng yīn')}],
  read:'万籁此都寂，但余钟磬音。',
  yisi:'此时此地，自然界的一切声响都沉寂了，只留下钟磬的余音在禅院里回荡。——收束全诗的「静」不是死寂：万籁退尽之后，特意让一声钟磬荡开——以极轻微的声音反衬极彻底的寂静（以声衬静），音波散处，禅院愈空，人心愈静。全诗在这最后一响里收住，余味也在这一响里不尽。',
  zhu:[['万籁','各种声响。籁，从孔穴里发出的声音，泛指一切声响，读 lài'],['此都寂','此时此地一切都沉寂。都，全、尽（教材通行本；一作「俱」）'],['但余','只留下。但，只'],['钟磬','寺院中诵经、斋供时鸣击的法器信号。钟为铜钟；磬为钵形铜法器，读 qìng'],['以声衬静','本诗写静的高招：不着一「静」字，让一声钟磬在万籁俱寂中荡开——以有声衬无声，静得更可听见']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「清晨入古寺」的下一句是？', o:['初日照高林','竹径通幽处','禅房花木深'], a:0},
 {q:'「竹径通幽处」的下一句是？', o:['山光悦鸟性','禅房花木深','初日照高林'], a:1},
 {q:'「但余钟磬音」的「磬」与「万籁此都寂」的「籁」，读音和意思都正确的一项是？', o:['磬读 qìng，寺院中钵形的铜制打击法器；籁读 lài，从孔穴里发出的声音，泛指一切声响','磬读 qíng，僧人手中的念珠；籁读 lài，竹林间呼啸的风声','磬读 pán，僧人打坐的坐具；籁读 lài，清晨的鸟鸣声'], a:0},
 {q:'这是一首题壁诗。关于诗中古寺与名句的文学常识，下列说法正确的是？', o:['诗题中的「破山寺」即今江苏常熟虞山的兴福寺；「竹径通幽处，禅房花木深」后世凝练成成语「曲径通幽」','「破山寺」在四川峨眉山中，因寺后山体崩破而得名；「曲径通幽」一词出自《诗经》','「破山寺」是诗人虚构的寺名；常建是晚唐朦胧诗派的代表诗人'], a:0},
 {q:'「山光悦鸟性，潭影空人心」中的「悦」与「空」，历来被视作全诗诗眼——妙在何处？', o:['两个词都写景物的颜色：山光是暖色、潭影是冷色，色彩对比鲜明','都是使动用法：山光使鸟性欢悦，潭影使人心中的杂念涤净——物我呼应、景中含情，写出山水涤荡尘心的宁静力量','都用夸张手法：极言山光之亮、潭影之深，突出寺院地势的高峻险远'], a:1},
];
"""

SCENES_JS = """/* ================= 题破山寺后禅院 · 四境场景（水墨夜思·清晨古寺：初日高林、竹径禅房、山光潭影、万籁钟磬） =================
   美术立意：水墨夜思色板写「清晨的古寺」——底色 #0d1117、雾 #131a26 系、accent=#98aec8（淡青晨蓝）
   只落在初日晕/边缘光/音波环/UI 上，全页近零饱和；无月（ms 0.001 移出视野），晨光淡日自建。
   境壹：古寺晨光——重檐大殿在晨雾里，两侧高林合抱，初日斜照、光柱穿林，诗人沿石径入寺。
   境贰（标志性瞬间）：曲径通幽的纵深——石径沿弧线没入竹径深处，两侧带节竹丛渐远渐矮，
   禅房半隐在花木与晨雾深处，一眼望不到底。
   境叁：山光潭影——潭水空明、山脊晨光、翔鸟掠潭，潭中小洲花木临水。
   境肆（末境可点击）：万籁俱寂的深院——一切声光退到最低；点击钟磬音：一声磬响（bell）
   + 音波环自禅房荡开（横向 Ring 逐环扩散淡出，余韵不绝），窗纸微光轻颤。 */

/* —— 初日 makeChuri(o)：水墨晨光里的淡日（limbTex 日轮 + 银青晕 + 斜光柱 Sprite；fadeK 铁律：初值=最大）—— */
function makeChuri(o){
  o=o||{};
  const r=o.r===undefined?7:o.r, op=o.op===undefined?0.42:o.op, haze=o.haze===undefined?0.15:o.haze;
  const g=new THREE.Group(), rays=[];
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xe9e4d4:o.color,
    transparent:true,opacity:op,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const hz=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0x98aec8:o.hazeC,
    transparent:true,opacity:haze,depthWrite:false,fog:false}));
  hz.scale.set(r*6.4,r*6.4,1); g.add(hz);
  for(let i=0;i<3;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:o.rayC===undefined?0xb8c4d4:o.rayC,
      transparent:true,opacity:0.085,depthWrite:false,fog:false,rotation:-0.42+i*0.17});
    const s=new THREE.Sprite(m);
    s.scale.set(r*1.5,r*10.5,1); s.position.set((i-1)*r*1.35,-r*1.6,0);
    g.add(s); rays.push(m);
  }
  g.update=function(t,k){
    disc.material.opacity=k*op*(0.95+0.05*Math.sin(t*0.4));
    hz.material.opacity=k*haze*(0.82+0.18*Math.sin(t*0.27+1.3));
    for(let i=0;i<rays.length;i++)rays[i].opacity=k*0.085*(0.68+0.32*Math.sin(t*0.5+i*2.1));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 高林 makeGulin(o)：古寺四周的高树（干+层叠冠+疏枝，合批 1 mesh）——「初日照高林」 */
function makeGulin(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21801:o.seed);
  const n=o.n===undefined?7:o.n, w=o.w===undefined?46:o.w;
  const z=o.z===undefined?-18:o.z, dz=o.dz===undefined?16:o.dz, h0=o.h===undefined?15:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, zz=z+(R()-0.5)*dz, h=h0*(0.7+0.6*R());
    const tr=new THREE.CylinderGeometry(0.13,0.30,h,6);
    tr.translate(x,h*0.5,zz); B.put(tr,shadeColor(0x131822,0.85+0.4*R()));
    const nb=2+Math.floor(R()*2);
    for(let c2=0;c2<nb;c2++){
      const cr=(2.2+R()*2.4)*(o.crown===undefined?1:o.crown);
      const cp=new THREE.SphereGeometry(cr,7,6);
      cp.scale(1,0.62+R()*0.25,1);
      cp.translate(x+(R()-0.5)*2.4,h*(0.72+c2*0.16+R()*0.08),zz+(R()-0.5)*2.0);
      B.put(cp,shadeColor(0x1a2330,0.7+0.5*R()));
    }
    for(let b=0;b<3;b++){
      const a=R()*6.283, y0=h*(0.42+R()*0.3), len=2.4+R()*2.4;
      B.put(limbGeo([x,y0,zz],[x+Math.cos(a)*len,y0+len*0.42,zz+Math.sin(a)*len*0.7],0.10,0.03,5),0x12171f);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x36445c,emissive:0x05070c}),{c:0x98aec8,i:0.14,p:2.4})));
  return g;
}

/* —— 古寺大殿 makeDadian(o)：重檐大殿（台基+殿身+双重飞檐+宝顶，合批 1 mesh）——「清晨入古寺」 */
function makeDadian(o){
  o=o||{};
  const w=o.w===undefined?10:o.w;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w*1.24,0.5,w*0.86); base.translate(0,0.25,0); B.put(base,0x232c3a);
  const body=new THREE.BoxGeometry(w,2.3,w*0.62); body.translate(0,1.65,0); B.put(body,0x1b2331);
  const door=new THREE.BoxGeometry(w*0.2,1.7,0.2); door.translate(0,1.7,w*0.31); B.put(door,0x0b0e14);
  const eave1=new THREE.BoxGeometry(w*1.22,0.16,w*0.84); eave1.translate(0,2.88,0); B.put(eave1,0x2c3648);
  const r1=new THREE.ConeGeometry(w*0.78,1.5,4); r1.rotateY(Math.PI/4); r1.scale(1.15,1,0.78); r1.translate(0,3.7,0); B.put(r1,0x141b28);
  const eave2=new THREE.BoxGeometry(w*0.86,0.14,w*0.56); eave2.translate(0,4.55,0); B.put(eave2,0x2c3648);
  const r2=new THREE.ConeGeometry(w*0.52,1.2,4); r2.rotateY(Math.PI/4); r2.scale(1.12,1,0.76); r2.translate(0,5.42,0); B.put(r2,0x121826);
  const finial=new THREE.SphereGeometry(0.22,6,5); finial.translate(0,6.15,0); B.put(finial,0x39465c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x98aec8,i:o.rim===undefined?0.15:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 竹丛 makeZhuCong(o)：带竹节的竹丛（分节竿+竹节环+斜叶，合批 1 mesh，整丛微摆）——「竹径」 */
function makeZhuCong(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21811:o.seed);
  const n=o.n===undefined?6:o.n, w=o.w===undefined?8:o.w, d=o.d===undefined?3:o.d;
  const culmC=o.culm===undefined?0x2a3831:o.culm, leafC=o.leaf===undefined?0x33443b:o.leaf;
  const h0=o.h===undefined?9:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, h=h0*(0.68+0.55*R());
    const tilt=(R()-0.5)*0.10, seg=Math.max(3,Math.round(h/1.6));
    for(let sgi=0;sgi<seg;sgi++){
      const y0=h*sgi/seg, y1=h*(sgi+1)/seg;
      const cgm=new THREE.CylinderGeometry(0.13*(1-y1/h*0.35),0.155*(1-y0/h*0.35),(y1-y0)*0.94,6);
      cgm.translate(x+tilt*y0,(y0+y1)/2,z); B.put(cgm,shadeColor(culmC,0.80+0.28*R()));
      const node=new THREE.CylinderGeometry(0.165*(1-y0/h*0.3),0.165*(1-y0/h*0.3),0.10,6);
      node.translate(x+tilt*y0,y1,z); B.put(node,shadeColor(culmC,1.22));
    }
    const nb=3+Math.floor(R()*3);
    for(let b=0;b<nb;b++){
      const ly=h*(0.55+0.42*R()), a=R()*6.283, len=1.5+R()*1.5;
      const bx=x+tilt*ly+Math.cos(a)*len*0.5, bz=z+Math.sin(a)*len*0.35;
      B.put(limbGeo([x+tilt*ly,ly,z],[bx,ly+0.5,bz],0.06,0.025,4),shadeColor(culmC,0.75));
      for(let lf=0;lf<3;lf++){
        const lp=new THREE.PlaneGeometry(0.9+R()*0.8,0.17);
        lp.rotateY(a+(R()-0.5)*0.9); lp.rotateZ(-0.55-R()*0.5);
        lp.translate(bx+(R()-0.5)*0.55,ly+0.3+lf*0.28+R()*0.3,bz+(R()-0.5)*0.45);
        B.put(lp,shadeColor(leafC,0.62+0.30*R()));
      }
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36485a,emissive:0x04070a,side:THREE.DoubleSide}),{c:0x98aec8,i:o.rim===undefined?0.10:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.0035*Math.sin(t*0.5+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 石径 makeShiJing(o)：沿弧线没入深处的石板小路（扁石一串）——「通幽处」的纵深线 */
function makeShiJing(o){
  o=o||{};
  const n=o.n===undefined?16:o.n;
  const z0=o.z0===undefined?-3:o.z0, z1=o.z1===undefined?-58:o.z1;
  const amp=o.amp===undefined?5.5:o.amp, R=seedRnd(o.seed===undefined?21821:o.seed);
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const t=i/(n-1), z=z0+(z1-z0)*t;
    const x=Math.sin(t*2.3+0.4)*amp*(0.35+0.65*t);
    const s=1.5-t*0.9;
    const st=new THREE.CylinderGeometry(s*(0.75+0.4*R()),s*(0.75+0.4*R()),0.14,7);
    st.scale(1.25,1,0.9); st.translate(x,0.07,z+(R()-0.5)*1.2);
    B.put(st,shadeColor(0x5d6a80,0.78+0.36*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x303c50,emissive:0x04060a}),{c:0x98aec8,i:0.10,p:2.2})));
  return g;
}

/* —— 禅房 makeChanfang(o)：藏在花木深处的禅房（台基+房身+坡顶合批；窗纸透一点晨光）——「禅房花木深」 */
function makeChanfang(o){
  o=o||{};
  const w=o.w===undefined?4.2:o.w;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w*1.3,0.36,w*0.92); base.translate(0,0.18,0); B.put(base,0x202a38);
  const body=new THREE.BoxGeometry(w,1.7,w*0.68); body.translate(0,1.2,0); B.put(body,0x1a2230);
  const door=new THREE.BoxGeometry(w*0.18,1.4,0.16); door.translate(-w*0.16,1.06,w*0.34); B.put(door,0x0b0e14);
  const r1=new THREE.ConeGeometry(w*0.94,1.35,4); r1.rotateY(Math.PI/4); r1.scale(1.18,1,0.80); r1.translate(0,2.72,0); B.put(r1,0x121826);
  const finial=new THREE.SphereGeometry(0.14,6,5); finial.translate(0,3.5,0); B.put(finial,0x36445a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x98aec8,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  const win=new THREE.Mesh(new THREE.PlaneGeometry(w*0.16,w*0.13),
    new THREE.MeshBasicMaterial({color:o.winC===undefined?0xcfd6c8:o.winC,transparent:true,
      opacity:o.winOp===undefined?0.55:o.winOp}));
  win.position.set(w*0.20,1.35,w*0.345); g.add(win);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 花木 makeHuamu(o)：花木深处的花树（冠团+满树花点，合批 1 mesh）——「花木深」 */
function makeHuamu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21831:o.seed);
  const n=o.n===undefined?5:o.n, w=o.w===undefined?20:o.w;
  const z=o.z===undefined?-6:o.z, dz=o.dz===undefined?10:o.dz;
  const bloom=o.bloom===undefined?0xd0d5e0:o.bloom;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, zz=z+(R()-0.5)*dz, h=2.6+2.6*R();
    const tr=new THREE.CylinderGeometry(0.09,0.16,h,5); tr.translate(x,h*0.5,zz); B.put(tr,0x161d29);
    const nb=2+Math.floor(R()*2);
    for(let c2=0;c2<nb;c2++){
      const cr=1.5+R()*1.7;
      const cp=new THREE.SphereGeometry(cr,7,6); cp.scale(1,0.8,1);
      cp.translate(x+(R()-0.5)*1.8,h*0.9+c2*cr*0.7,zz+(R()-0.5)*1.6);
      B.put(cp,shadeColor(0x232f3e,0.8+0.4*R()));
    }
    const nf=6+Math.floor(R()*8);
    for(let f=0;f<nf;f++){
      const fs=new THREE.SphereGeometry(0.10+R()*0.13,5,4);
      fs.translate(x+(R()-0.5)*3.0,h*(0.75+R()*0.5),zz+(R()-0.5)*2.6);
      B.put(fs,shadeColor(bloom,0.85+0.35*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36445a,emissive:0x05070c}),{c:0x98aec8,i:0.17,p:2.4})));
  return g;
}

/* —— 山鸟 makeShanniao(o)：潭上翔鸟（简笔飞鸟 InstancedMesh 1 draw call，逐帧扑翼盘旋）——「山光悦鸟性」 */
function makeShanniao(o){
  o=o||{};
  const n=o.n===undefined?7:o.n;
  const geo=new THREE.BufferGeometry();
  const v=new Float32Array([
    0,0,0.72,  -0.21,0.03,-0.46,  0.21,0.03,-0.46,
    0,0.03,0.06,  -1.45,0.14,-0.55,  -0.19,0.03,-0.50,
    0,0.03,0.06,   0.19,0.03,-0.50,  1.45,0.14,-0.55
  ]);
  geo.setAttribute('position',new THREE.BufferAttribute(v,3));
  geo.computeVertexNormals();
  const mesh=new THREE.InstancedMesh(geo,
    new THREE.MeshBasicMaterial({color:o.color===undefined?0x2a3542:o.color,side:THREE.DoubleSide}),n);
  mesh.frustumCulled=false;
  const dm=new THREE.Object3D(), items=[];
  const R=seedRnd(o.seed===undefined?21841:o.seed);
  const cx=o.cx===undefined?0:o.cx, cy=o.cy===undefined?13:o.cy, cz=o.cz===undefined?-34:o.cz;
  const rad=o.rad===undefined?16:o.rad;
  for(let i=0;i<n;i++)items.push({a:R()*6.283,v:(0.10+0.10*R())*(R()<0.5?1:-1),r:rad*(0.55+0.6*R()),
    ph:R()*6.283,s:0.7+0.5*R(),fl:6+R()*4});
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t){
    for(let i=0;i<n;i++){
      const it=items[i], a=it.a+t*it.v, flap=Math.sin(t*it.fl+it.ph)*0.55;
      dm.position.set(cx+Math.cos(a)*it.r, cy+Math.sin(t*0.5+it.ph)*1.2, cz+Math.sin(a)*it.r*0.6);
      dm.rotation.set(flap*0.35, -a+(it.v>0?0:Math.PI), flap);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 磬音波环 makeYinbo(o)：点击后自禅房荡开的音波环（横向 Ring 逐环扩散淡出；fadeK 铁律：初值=最大）—— */
function makeYinbo(o){
  o=o||{};
  const n=o.n===undefined?4:o.n, y=o.y===undefined?2.4:o.y;
  const reach=o.reach===undefined?30:o.reach, speed=o.speed===undefined?0.15:o.speed;
  const maxOp=o.maxOp===undefined?0.40:o.maxOp;
  const g=new THREE.Group(), rings=[];
  for(let i=0;i<n;i++){
    const mesh=new THREE.Mesh(new THREE.RingGeometry(0.94,1.0,56),
      new THREE.MeshBasicMaterial({color:o.color===undefined?0x98aec8:o.color,
        transparent:true,opacity:maxOp,depthWrite:false,side:THREE.DoubleSide}));
    mesh.rotation.x=-Math.PI/2; mesh.position.y=y; mesh.renderOrder=4;
    g.add(mesh); rings.push({m:mesh.material,mesh:mesh,ph:i/n});
  }
  g.update=function(t,k,amp){
    if(amp===undefined||amp<=0.001){ for(let i=0;i<n;i++)rings[i].m.opacity=0; return; }
    for(let i=0;i<n;i++){
      const it=rings[i], cyc=(t*speed+it.ph)%1, s=1.6+cyc*reach;
      it.mesh.scale.set(s,s,1);
      it.m.opacity=amp*k*Math.pow(1-cyc,1.6)*maxOp;
    }
  };
  g.userData.update=g.update;
  return g;
}

/* 游寺人/望潭人：全诗贯穿的同一造型（青灰袍、幞头；每次 build 新建材质） */
function csFigure(scale){
  return makeFigure({pose:'独立',robe:0x2c3648,belt:0x71829c,skin:0xd3b294,collar:0x9aa8ba,
    hair:0x12161e,hat:'幞头',rimC:0x98aec8,rim:0.45,noProp:true,scale:scale===undefined?1.8:scale});
}

function bCover(){ // 卷首 · 晨雾古寺远望：重檐大殿半隐雾中，高林合抱，初日斜照
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0c1119,c2:0x1b2534,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:26,layers:2,peaks:5,seed:21851,color:0x0e141f,atmo:0x1c2836,
    fogK:0.60,glowK:0.10,glow:0xd8d2c0,y:-10,order:-6});
  ridge.g.position.set(-30,0,-96); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const dadian=makeDadian({scale:1.7,rim:0.18}); dadian.position.set(-12,-1.8,-46); dadian.rotation.y=0.3; g.add(dadian);
  const gulin=makeGulin({n:9,w:70,h:17,z:-48,dz:20,seed:21852}); gulin.position.set(2,0,0); g.add(gulin);
  const sun=makeChuri({r:8,op:0.40,haze:0.14}); sun.position.set(34,17,-76); g.add(sun);
  const mist=makeMist({n:7,spread:[240,18,80],pos:[0,7,-62],scale:74,color:0x2a3648,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:34,box:[210,24,90],pos:[0,12,-40],color:0x9fb2c8,size:5,speed:0.045,rise:0,add:false,maxA:0.10});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.2,w:15,d:6,color:0x10141d,seed:21853,rim:0.10,rimC:0x98aec8});
  fg1.g.position.set(-13,-2,16); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x10141d,seed:21854,rim:0.10,rimC:0x98aec8});
  br.g.position.set(14,-1.8,14); g.add(br.g);
  addLights(g,{c:0x9fb4cc,i:0.42,p:[-40,80,-20]},{c:0x1a2230,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    sun.update(t,k); fg1.update(t,k); br.update(t,k);
  }};
}
function bChuri(){ // 壹 · 初日高林 —— 清晨入古寺，初日照高林：晨光穿林、诗人入寺
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0c1119,c2:0x202c3c,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:20,layers:2,peaks:4,seed:21855,color:0x0d1320,atmo:0x1c2836,
    fogK:0.62,glowK:0.08,glow:0xd8d2c0,y:-10,order:-6});
  ridge.g.position.set(-40,0,-100); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 古寺大殿：高林合抱之中 */
  const dadian=makeDadian({scale:2.0,rim:0.18}); dadian.position.set(-12,-1.8,-40); dadian.rotation.y=0.25; g.add(dadian);
  const gl1=makeGulin({n:6,w:30,h:16,z:-30,dz:10,seed:21856}); gl1.position.set(20,0,2); g.add(gl1);
  const gl2=makeGulin({n:5,w:26,h:14,z:-26,dz:9,seed:21857}); gl2.position.set(-26,0,4); g.add(gl2);
  /* 入寺石径 + 入寺人 */
  const path=makeShiJing({n:12,z0:-4,z1:-36,amp:3,seed:21858}); g.add(path);
  const poet=csFigure(1.8); poet.position.set(2.2,-0.30,-10); poet.rotation.y=3.4; g.add(poet);
  /* 初日：晨光斜柱穿林 */
  const sun=makeChuri({r:9,op:0.50,haze:0.18,color:0xf0e8d0,rayC:0xc4cedd}); sun.position.set(20,33,-62); g.add(sun);
  const mist=makeMist({n:6,spread:[220,16,80],pos:[0,7,-58],scale:72,color:0x2a3648,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[180,26,80],pos:[0,11,-36],color:0xa8bacd,size:4.6,speed:0.05,rise:0,add:false,maxA:0.11});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.0,w:13,d:6,color:0x10141d,seed:21859,rim:0.10,rimC:0x98aec8});
  fg1.g.position.set(-12,-1.9,14); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x10141d,seed:21860,rim:0.10,rimC:0x98aec8});
  br.g.position.set(13.5,-1.7,12); g.add(br.g);
  addLights(g,{c:0xa8bccf,i:0.48,p:[35,70,-25]},{c:0x1c2534,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    sun.update(t,k); fg1.update(t,k); br.update(t,k); poet.update(t,k);
  }};
}
function bZhujing(){ // 贰（标志性瞬间）· 竹径禅房 —— 竹径通幽处，禅房花木深：曲径通幽的纵深
  const g=new THREE.Group();
  const grd=makeGround({r:230,c1:0x0b101a,c2:0x1b2735,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:320,h:9,layers:2,peaks:4,seed:21861,color:0x0d1320,atmo:0x1c2836,
    fogK:0.70,glowK:0.05,glow:0xd8d2c0,y:-12,order:-6});
  ridge.g.position.set(0,0,-120); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 纵深线：石径沿弧线没入深处 */
  const path=makeShiJing({n:16,z0:-2.5,z1:-60,amp:6.5,seed:21862}); g.add(path);
  /* 两侧竹丛：渐远渐矮，把「幽」围出来 */
  const zhuLg=[], zhuRg=[];
  [[-4.6,-7,1.05],[-5.6,-15,0.96],[-6.2,-24,0.86],[-5.4,-35,0.75],[-4.6,-47,0.63]].forEach(function(p,i){
    const zc=makeZhuCong({n:7,w:6.2,d:2.6,h:10,seed:21863+i*2});
    zc.position.set(p[0],-0.02,p[1]); zc.scale.setScalar(p[2]); g.add(zc); zhuLg.push(zc);
  });
  [[5.0,-10,1.0],[6.0,-19,0.92],[6.4,-29,0.82],[5.8,-41,0.71],[4.8,-53,0.60]].forEach(function(p,i){
    const zc=makeZhuCong({n:7,w:6.2,d:2.6,h:9.5,seed:21864+i*2});
    zc.position.set(p[0],-0.02,p[1]); zc.scale.setScalar(p[2]); g.add(zc); zhuRg.push(zc);
  });
  /* 禅房半隐深处 + 花木深深 */
  const fang=makeChanfang({scale:1.25,rim:0.20,winOp:0.85,winC:0xd8dcc4}); fang.position.set(3.2,-1.5,-54); fang.rotation.y=-0.35; g.add(fang);
  const hm=makeHuamu({n:5,w:24,z:-54,dz:12,seed:21874}); hm.position.set(0,-1.5,0); g.add(hm);
  const petals=makeGlow({n:55,box:[56,15,46],pos:[1,8.5,-34],color:0xc9c6d2,size:3.0,speed:0.10,rise:-1,add:false,maxA:0.12});
  g.add(petals.points);
  const mist=makeMist({n:7,spread:[220,16,70],pos:[0,6,-56],scale:70,color:0x2a3648,op:0.13});
  g.add(mist.g);
  const motes=makeGlow({n:30,box:[150,20,60],pos:[0,9,-32],color:0x9fb2c8,size:4.4,speed:0.04,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  /* 竹径口两丛近竹+坡石作前景框 */
  const fgz=makeZhuCong({n:8,w:7,d:2.6,h:11,seed:21875});
  fgz.position.set(-6.5,-0.02,15); fgz.scale.setScalar(1.5); g.add(fgz); zhuLg.push(fgz);
  const br=makeForeground({kind:'坡石',n:2,r:2.2,w:10,d:5,color:0x0d1119,seed:21876,rim:0.08,rimC:0x98aec8});
  br.g.position.set(10,-1.6,13); g.add(br.g);
  addLights(g,{c:0x93a8c0,i:0.40,p:[-20,60,-30]},{c:0x19222f,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t); petals.update(t);
    br.update(t,k);
    zhuLg.forEach(function(zc){ zc.update(t); });
    zhuRg.forEach(function(zc){ zc.update(t); });
  }};
}
function bTanying(){ // 叁 · 山光潭影 —— 山光悦鸟性，潭影空人心：空明潭水、翔鸟掠潭
  const g=new THREE.Group();
  const water=makeWater({size:360,seg:96,amp:0.26,freq:0.06,speed:0.30,flow:[0.05,0.5],spec:0.40,
    deep:0x0a1018,shallow:0x1d2a3c,skyc:0x2a3950,moonDir:[0.15,0.55,-1]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x93a4b8);
  water.mesh.position.set(0,-0.35,-36); g.add(water.mesh);
  const grd=makeGround({r:120,c1:0x0c1119,c2:0x1b2534,y:-0.9}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:24,layers:2,peaks:5,seed:21877,color:0x0e141f,atmo:0x243446,
    fogK:0.60,glowK:0.26,glow:0xdde6ee,y:-9,order:-6});
  ridge.g.position.set(0,0,-112); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 山光悦鸟性：翔鸟掠潭 */
  const birds=makeShanniao({n:7,cx:0,cy:8,cz:-30,rad:9,seed:21878}); g.add(birds);
  /* 潭中小洲：花木临水 */
  const isle=makeForeground({kind:'坡石',n:5,r:3.6,w:14,d:8,color:0x11161f,seed:21879,rim:0.12,rimC:0x98aec8});
  isle.g.position.set(-11,-1.1,-58); g.add(isle.g);
  const hm=makeHuamu({n:4,w:12,z:-58,dz:6,seed:21880}); hm.position.set(-11,-0.6,0); g.add(hm);
  /* 望潭人：右前岩上 */
  const rock=makeForeground({kind:'坡石',n:3,r:2.6,w:9,d:5,color:0x10141d,seed:21881,rim:0.12,rimC:0x98aec8});
  rock.g.position.set(9,-0.9,-5.5); g.add(rock.g);
  const poet=csFigure(1.8); poet.position.set(9,-0.30,-5.5); poet.rotation.y=2.8; g.add(poet);
  const mist=makeMist({n:6,spread:[220,14,70],pos:[0,3,-52],scale:62,color:0x2a3648,op:0.13});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[170,18,70],pos:[0,8,-34],color:0x9fb2c8,size:4.6,speed:0.04,rise:0,add:false,maxA:0.10});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x0f131c,seed:21882,rim:0.09,rimC:0x98aec8});
  fg1.g.position.set(-12,-1.8,14); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:1.7,w:7,d:4,color:0x0f131c,seed:21883,rim:0.09,rimC:0x98aec8});
  br.g.position.set(13.5,-1.7,13); g.add(br.g);
  addLights(g,{c:0xaec2d4,i:0.50,p:[45,85,-30]},{c:0x1e2836,i:0.64});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); motes.update(t);
    fg1.update(t,k); br.update(t,k); poet.update(t,k); birds.update(t);
    isle.update(t,k); rock.update(t,k);
  }};
}
function bWlai(){ // 肆（末境·可点击）· 万籁钟磬 —— 万籁此都寂，但余钟磬音：点击磬响+音波环自禅房荡开
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0x0a0f18,c2:0x161f2b,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:18,layers:2,peaks:4,seed:21884,color:0x0d1320,atmo:0x1c2836,
    fogK:0.64,glowK:0.05,glow:0xd8d2c0,y:-10,order:-6});
  ridge.g.position.set(-20,0,-108); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 深院禅房：万籁俱寂的中心，亦是音波环的原点 */
  const fang=makeChanfang({scale:1.35,rim:0.18,winOp:0.85,winC:0xd8dcc4}); fang.position.set(0,-1.4,-30); g.add(fang);
  /* 院墙矮篱与竹径口石板 */
  const path=makeShiJing({n:8,z0:-6,z1:-25,amp:1.5,seed:21885}); g.add(path);
  const gl1=makeGulin({n:5,w:34,h:15,z:-42,dz:12,seed:21886}); gl1.position.set(-26,0,2); g.add(gl1);
  const hm=makeHuamu({n:4,w:20,z:-38,dz:10,seed:21887}); hm.position.set(14,-1.6,0); g.add(hm);
  /* 远处一僧一影，愈显院空 */
  const crowd=makeCrowd({n:2,rect:[3.4,-33,3.0,2.4],seed:21888,color:0x20262f,rimC:0x98aec8,rim:0.20,sMin:0.55,sMax:0.62,y:-1.3});
  g.add(crowd.mesh);
  /* 窗纸微光：点击后轻颤 */
  const pl=new THREE.PointLight(0xcfd8c0,0.9,42); pl.position.set(0,2.6,-29); g.add(pl);
  /* 音波环：自禅房荡开 */
  const yinbo=makeYinbo({n:4,y:2.4,reach:30,speed:0.15,maxOp:0.40,color:0x98aec8});
  yinbo.position.set(0,-1.4,-30); g.add(yinbo);
  const mist=makeMist({n:8,spread:[230,16,80],pos:[0,6,-54],scale:72,color:0x2a3648,op:0.14});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[160,18,64],pos:[0,9,-32],color:0x9fb2c8,size:4.2,speed:0.035,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  /* 伫立听磬人：左前 */
  const poet=csFigure(1.6); poet.position.set(-8.5,-0.30,-6); poet.rotation.y=3.6; g.add(poet);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x0e121b,seed:21889,rim:0.09,rimC:0x98aec8});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:1.7,w:7,d:4,color:0x0e121b,seed:21890,rim:0.09,rimC:0x98aec8});
  br.g.position.set(13,-1.7,12); g.add(br.g);
  addLights(g,{c:0x8fa2b8,i:0.34,p:[30,60,-20]},{c:0x161f2b,i:0.54});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/3.5);
      const rv=ctl.reveal, e=rv*rv*(3-2*rv);
      pl.intensity=k*0.9*(0.35+0.65*e)*(0.85+0.15*Math.sin(t*5.1));
      yinbo.update(t,k,e*0.85);
      ridge.update(t,0); mist.update(t,k); motes.update(t);
      fg1.update(t,k); br.update(t,k); poet.update(t,k); crowd.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.10);                          // 万籁愈静
        bell(); pluck(3,0.55,0.07); pluck(5,1.15,0.05);   // 一声磬响+余韵
        const fl=$('#flash'); fl.textContent='万籁此都寂 但余钟磬音';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0b111c),hor:C(0x1c2836),bot:C(0x0a0f18),fog:C(0x131a26),fd:0.0058,star:0.06,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0x9fb4cc),dirI:0.46,
  dirP:new THREE.Vector3(-40,80,-30),ambC:C(0x1a2230),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8.5,58],t:[0,9.5,50],lf:[0,10,-30],lt:[2,11,-40]},
  sky:()=>SK({fd:0.0050,star:0.05,hor:C(0x212e3e),dirI:0.40}) },
{ name:'初日高林',dwell:17,river:0.02,build:bChuri,
  cam:{f:[0,6.5,36],t:[0,7.5,30],lf:[0,9,-40],lt:[2,10,-54]},
  sky:()=>SK({fd:0.0058,star:0.03,hor:C(0x263344),dirC:C(0xa8bccf),dirI:0.48,
    dirP:new THREE.Vector3(35,70,-25),ambC:C(0x1c2534),ambI:0.62}) },
{ name:'竹径禅房',dwell:19,river:0.02,build:bZhujing,
  cam:{f:[0,4.8,30],t:[0.5,5,24],lf:[0,4,-36],lt:[2.5,4,-58]},
  sky:()=>SK({fd:0.0066,star:0.01,top:C(0x0a0f1a),hor:C(0x1c2634),bot:C(0x090d15),
    dirC:C(0x93a8c0),dirI:0.40,ambC:C(0x19222f),ambI:0.58}) },
{ name:'山光潭影',dwell:18,river:0.03,build:bTanying,
  cam:{f:[0,6.5,27],t:[1,7,21],lf:[0,8,-42],lt:[2.5,8.5,-58]},
  sky:()=>SK({fd:0.0054,star:0.02,hor:C(0x2a3848),dirC:C(0xaec2d4),dirI:0.50,
    dirP:new THREE.Vector3(45,85,-30),ambC:C(0x1e2836),ambI:0.64}) },
{ name:'万籁钟磬',dwell:19,river:0.02,build:bWlai,
  cam:{f:[0,5.5,24],t:[0,5.8,19],lf:[0,5,-22],lt:[0,5.6,-34]},
  sky:()=>SK({fd:0.0072,star:0.01,top:C(0x090e17),hor:C(0x18222f),bot:C(0x080c13),
    dirC:C(0x8fa2b8),dirI:0.34,ambC:C(0x161f2b),ambI:0.54}) },
];
"""
