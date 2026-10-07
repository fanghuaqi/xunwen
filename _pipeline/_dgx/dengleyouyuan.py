# -*- coding: utf-8 -*-
"""dengleyouyuan.py —— 《登乐游原》（唐·李商隐，queue no.229，宣纸留白）生成配置
两境（N=queue stages 数）：向晚驱车（向晚意不适·驱车登古原——车影缓行于古原车辙）、
夕阳黄昏（夕阳无限好·只是近黄昏——标志性瞬间+末境点击）。
宣纸留白全套色板：浅纸底 #e9e2d0、浓墨 #2c2f33 系、淡雾 #e6dabb，accent=#3e4436
（queue 分配强调色，苍绿墨）只落在古原地面/车影/诗人袍色/UI 上，全页近零饱和；
本诗点睛：克制的暖橙余晖（#f0b464/#e6c284 系）——「暖调余晖」是全页主视觉，
与 zhongnanwang-yuxue（雪山青灰）第一眼可区分：这里是一轮古原大夕阳。
时间推进线：同一趟黄昏登原——境壹=向晚（日已偏西仍高，郁郁驱车上原）
→ 境贰=原顶（大夕阳半衔远原线，辉煌无限好；点击后夕阳大盛而后徐沉、余晖渐敛、
暮霭转灰、遥遥城郭渐隐、初星点点——「只是近黄昏」）。
标志性瞬间（境贰·全诗名句）：夕阳无限好只是近黄昏——古原大夕阳（renderOrder -7，
沉落时被远原/地面覆盖，做出「徐沉入暮」）。
末境点击（queue interact：点击夕阳——夕阳大盛而后徐沉+暮色四合）：点击画面——
日轮先涨大、暖晕大涨（大盛），继而徐徐沉入远原线，余晖敛尽、暮霭由暖纸转灰紫、
原际暖晕渐冷、城郭隐入霭中、暮鸦远去、初星点点，「夕阳无限好 只是近黄昏」题字同现。
考点钉子：驱 qū（驾车，小测第 3 题落点）；乐游原（唐长安登高胜地）+ 李商隐
「小李杜」（第 4 题）；「只是」的转折与惜时伤怀/迟暮之感（第 5 题）。
多音字：乐游原 lè（tts.json 钉「乐游原→勒游原」防误读 yuè）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='dengleyouyuan', title='登乐游原', dyn='唐 · 李商隐', brand_author='李商隐',
    gold_rgb='62,68,54',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#3e4436; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(62,68,54,.28);
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
        ('0x0a1526', '0xe6dabb', 4),
    ],
    tip='轻点画面 / 按空格 —— 夕阳大盛，而后徐沉',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看夕阳大盛后徐沉、暮色四合',
    cover_read='登乐游原。唐，李商隐。向晚意不适，驱车登古原。夕阳无限好，只是近黄昏。',
    cover_p1='两重意境，随诗句次第展开：向晚时分心里闷闷不乐，赶着车子登上古老的乐游原——不想在原顶撞见一轮无限好的夕阳，正缓缓沉向黄昏。',
    cover_p2='边读诗，边跟着李商隐驱车登原：登上原顶，看夕阳大盛又徐徐沉落——读懂「只是」那一转里的惋惜，就读懂了这首二十字的绝唱。',
    end_h2='夕阳 · 黄昏', cn_word='两',
    words_js="['再登一次古原','初识义山，尚需共读','渐入诗境，再诵几遍','夕阳渐好，暖意渐生','已解好景黄昏意','夕阳徐沉，余味无穷']",
    sky_atmo='0xdcd2b8',
)

POEM_JS = """const POEM = [
{ name:'向晚驱车', jing:'向晚时分心里闷闷不乐，赶着车子登上古老的乐游原 —— 向晚、驱车、古原：一次说走就走的登高排闷。（向晚 · 驱车 · 古原 · 车影缓行）',
  segs:[
   {c:'向晚意不适，', p:py('xiàng wǎn yì bú shì')},
   {c:'驱车登古原。', p:py('qū chē dēng gǔ yuán')}],
  read:'向晚意不适，驱车登古原。',
  yisi:'傍晚时分心情闷闷不乐，于是赶着车子登上古老的乐游原。——起句先写「因何而登」：向晚意不适——一天将尽，心头的不快却无处安放；次句写「以何排遣」：驱车登古原——不假思索、说走就走，「驱」「登」两个字里，有一股急于摆脱郁结的劲。登高本为遣怀，却不想在原上撞见了黄昏最美的风景——郁闷的起点，恰恰通向名句的诞生。',
  zhu:[['登乐游原','诗题一作《乐游原》——向晚登原遣怀之作'],['乐游原','在唐长安城东南（今西安曲江池一带），地势高敞、可俯望长安全城，汉代以来即是著名游览胜地，唐人最爱来此登高望景，尤其黄昏'],['向晚','傍晚将至、天色向晚。向，接近'],['意不适','心情不舒畅、闷闷不乐'],['驱车','驾着车子前行。驱，读 qū，赶马前进，引申为驾御'],['古原','指乐游原。「古」字有来历：此地汉代已建为乐游苑，至李商隐时已是一座「古」原——一个「古」字也添了几分苍茫']] },
{ name:'夕阳黄昏', jing:'夕阳无限美好，只是已近黄昏 —— 古原大夕阳：辉煌与转瞬，同在一瞬。（夕阳 · 无限好 · 近黄昏 · 标志性瞬间 · 末境点击画面：看夕阳大盛后徐沉、暮色四合）',
  segs:[
   {c:'夕阳无限好，', p:py('xī yáng wú xiàn hǎo')},
   {c:'只是近黄昏。', p:py('zhǐ shì jìn huáng hūn')}],
  read:'夕阳无限好，只是近黄昏。',
  yisi:'傍晚的夕阳无限美好，只可惜已近黄昏。——这两句是千古名句：不说自己心情如何，只把满眼辉煌推到人面前——「无限好」三字毫无保留，是把全部赞叹都给了这轮落日；「只是」轻轻一转，好景与时限同时到场——愈辉煌，愈接近消逝。惜黄昏，是惜美景难留，也是惜年华迟暮；一千多年来，凡见过「无限好」又留不住的人，都会在这一联前停一停。',
  zhu:[['夕阳','傍晚的太阳——与首句「向晚」呼应，时间是同一段黄昏'],['无限好','好到没有边际——极写夕阳晚景的灿烂辉煌，赞叹到近乎失语'],['只是','转折：只是、偏偏——无限好的夕阳偏偏已近黄昏（另有一说解作「正是」：这正是近黄昏时才有的美景；教材通行取转折说，惋惜之意更切）'],['近黄昏','逼近黄昏——太阳就要沉落，好景将尽'],['迟暮之感','传统解读认为此诗借夕阳抒发人生迟暮、好景无多的感伤，也有学者读出忧时伤世的时代悲感——个人身世与时代气象，在这一联里难以分清']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「向晚意不适」的下一句是？', o:['驱车登古原','夕阳无限好','只是近黄昏'], a:0},
 {q:'「夕阳无限好」的下一句是？', o:['向晚意不适','只是近黄昏','驱车登古原'], a:1},
 {q:'「驱车登古原」的「驱」，读音和意思都正确的一项是？', o:['读 qū，赶马驾车——「驱车」即驾着车子前行，与「登」字相连，见出排遣闷怀的急切','读 qù，离去——「驱车」即弃车而去，诗人独自徒步登上古原','读 jū，车马——「驱车」即换乘快马，一路奔驰上原'], a:0},
 {q:'关于「乐游原」与作者李商隐，下列说法正确的是？', o:['乐游原在唐长安城东南，地势高敞、可俯望全城，是唐人黄昏登高揽胜之地；李商隐是晚唐诗人，与杜牧并称「小李杜」','乐游原在江南苏州，是宋代才兴起的私家园林；李商隐是「唐宋八大家」之一','乐游原是汉代边塞关隘，以军旅诗闻名；李商隐与李贺并称「老李杜」'], a:0},
 {q:'「夕阳无限好，只是近黄昏」历来被推为名句。对「只是」与全诗主旨的理解，最准确的一项是？', o:['「只是」是转折：无限好的夕阳偏偏已近黄昏——美景与迟暮同时到场，愈辉煌愈近消逝，珍惜好景、感叹时光（一说兼有忧时伤世之慨）','「只是」表因果：因为夕阳无限好，所以黄昏格外温暖——全诗是一首纯粹的写景欢歌','「只是」表递进：夕阳不但好，黄昏还要更好——诗人对前途充满信心'], a:0},
];
"""

SCENES_JS = """/* ================= 登乐游原 · 两境场景（宣纸留白·暖晖古原：向晚驱车、夕阳黄昏） =================
   美术立意：宣纸留白色板写「薄暮古原的大夕阳」——浅纸为天、浓墨作烟树远原、大量留白，
   accent=#3e4436（苍绿墨）只落在古原地面/车影/诗人袍色/UI 上，全页近零饱和；
   点睛是一轮克制的暖橙余晖（#f6d69c/#f0b464/#e6c284）——与 zhongnanwang-yuxue（雪山青灰）
   第一眼可区分：这里日轮当空、余晖满纸。
   境壹（向晚）：车影缓行于古原车辙——车厢拱篷、双轮徐转、车夫随行，淡日偏西、暮鸦点点，
   郁郁驱车而上；境贰（原顶·标志性瞬间+末境可点击）：大夕阳半衔远原线，余晖染纸，
   遥遥城郭一痕；点击：日轮大盛而后徐沉，余晖渐敛、暮霭转灰、城郭渐隐、初星点点。 */

/* —— 大夕阳 makeXiyang(o)：古原落日（limbTex 日轮+紧晕+远晕三层，均 fog:false 如星月点名；
   renderOrder -7——沉落时被远原带/地面覆盖，做出「徐沉入暮」）。
   update(t,k) 微息；setDusk(e,k)：e 0→1——先大盛（日轮涨大、暖晕大涨），后徐沉
   （日轮沉入远原线、晕光渐敛），「夕阳无限好 只是近黄昏」。fadeK 铁律：初值=最大 */
function makeXiyang(o){
  o=o||{};
  const r=o.r===undefined?27:o.r;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),
    color:o.color===undefined?0xf6d69c:o.color,transparent:true,opacity:0.96,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); disc.renderOrder=-7; g.add(disc);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),
    color:o.glowC===undefined?0xf0b464:o.glowC,transparent:true,opacity:0.55,depthWrite:false,fog:false}));
  glow.scale.set(r*4.4,r*4.4,1); glow.renderOrder=-7; g.add(glow);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),
    color:o.hazeC===undefined?0xe6c284:o.hazeC,transparent:true,opacity:0.29,depthWrite:false,fog:false}));
  haze.scale.set(r*9.0,r*9.0,1); haze.renderOrder=-7; g.add(haze);
  const sm=function(a,b,x){x=Math.max(0,Math.min(1,(x-a)/(b-a)));return x*x*(3-2*x);};
  const api={g:g,disc:disc,glow:glow,haze:haze,r:r,y0:o.y0===undefined?21:o.y0,
    update(t,k){ const kk=k===undefined?1:k, p=0.985+0.015*Math.sin(t*0.5);
      disc.material.opacity=kk*0.96*p;
      glow.material.opacity=kk*0.55*p;
      haze.material.opacity=kk*0.29*p;
    },
    setDusk(e,k){ const kk=k===undefined?1:k;
      const pulse=Math.sin(sm(0,1,Math.min(e/0.30,1))*Math.PI);   /* 大盛：先涨、复敛 */
      const sink=sm(0.18,1,e);                                    /* 徐沉 */
      const breathe=0.985+0.015*Math.sin(e*20);
      api.g.position.y=api.y0-sink*(api.y0+30);
      const sc=1+0.24*pulse;
      disc.scale.set(api.r*2*sc,api.r*2*sc,1);
      glow.scale.set(api.r*4.4*(1+0.85*pulse),api.r*4.4*(1+0.85*pulse),1);
      haze.scale.set(api.r*9.0*(1+0.45*pulse),api.r*9.0*(1+0.45*pulse),1);
      const env=1-0.96*sm(0.42,1,e);                              /* 余晖渐敛 */
      disc.material.opacity=kk*0.96*env*breathe;
      glow.material.opacity=kk*0.55*env*breathe;
      haze.material.opacity=kk*0.29*(1-0.90*sm(0.35,1,e))*breathe;
    }};
  g.userData.update=api.update;
  return api;
}

/* —— 车 makeCheying(o)：「驱车」的车影（车板+车厢+拱篷+车轴+双辕，合批 1 mesh；
   双轮各 1 mesh 可徐转；车夫随车缓行（远景人影 1 draw call）。o.move 时沿车辙缓行，
   行至远处悄然而回；fadeK：材质由 setFade 统一管，update 只动位姿不写透明度 */
function makeLun(r){
  const B=new GeoBag();
  const rim=new THREE.TorusGeometry(r,0.075,7,22); B.put(rim,0x262218);
  for(let i=0;i<4;i++){
    const sp=new THREE.CylinderGeometry(0.034,0.05,r*1.86,5);
    sp.rotateZ(Math.PI/4*i); B.put(sp,0x2b2620);
  }
  const hub=new THREE.CylinderGeometry(0.12,0.12,0.24,8); hub.rotateX(Math.PI/2); B.put(hub,0x332d24);
  return B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x453f34,emissive:0x060504}));
}
function makeCheying(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22901:o.seed);
  const B=new GeoBag();
  const board=new THREE.BoxGeometry(2.0,0.10,1.9); board.translate(-0.1,0.82,0); B.put(board,0x332d24);
  const box=new THREE.BoxGeometry(1.55,1.0,1.9); box.translate(-0.1,1.34,0); B.put(box,0x2e2921);
  const canopy=new THREE.CylinderGeometry(0.84,0.90,2.1,10,1,true,0,Math.PI);
  canopy.rotateZ(Math.PI/2); canopy.scale(1.02,1,0.80); canopy.translate(-0.1,1.82,0);
  B.put(canopy,0x39342a);
  const axle=new THREE.CylinderGeometry(0.055,0.055,2.02,6); axle.rotateZ(Math.PI/2); axle.translate(0,0.62,0); B.put(axle,0x241f19);
  for(let s=-1;s<=1;s+=2){
    const sh=new THREE.CylinderGeometry(0.045,0.06,1.9,5);
    sh.rotateZ(-(Math.PI/2-0.22)); sh.translate(1.55,1.02,s*0.50); B.put(sh,0x2a251e);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x453f34,emissive:0x060504}),{c:0xe8cf9a,i:o.rim===undefined?0.13:o.rim,p:2.4})));
  const wheels=[];
  for(let s=-1;s<=1;s+=2){
    const w=makeLun(0.62); w.position.set(0,0.62,s*0.96); g.add(w); wheels.push(w);
  }
  const driver=makeCrowd({n:1,rect:[-2.4,0.3,0.3,0.3],seed:(o.seed===undefined?22901:o.seed)+1,
    color:0x2c2a24,rimC:0xd8b888,rim:0.16,sMin:0.58,sMax:0.64,y:0});
  g.add(driver.mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283, y0=o.y===undefined?-1.52:o.y;
  g.position.set(o.x===undefined?0:o.x,y0,o.z===undefined?0:o.z);
  const mv=o.move===undefined?true:!!o.move;
  const vx=o.vx===undefined?-0.556:o.vx, vz=o.vz===undefined?-0.831:o.vz;
  const wrapZ=o.wrapZ===undefined?-26:o.wrapZ;
  const api={g:g,wheels:wheels,driver:driver,
    update(t,dt,k){
      const d=(dt===undefined?0:dt);
      if(mv){
        g.position.x+=vx*d; g.position.z+=vz*d;
        if(g.position.z<wrapZ){ g.position.x=o.x===undefined?0:o.x; g.position.z=o.z===undefined?0:o.z; }
        for(let i=0;i<wheels.length;i++)wheels[i].rotation.z-=0.68*d;
      }
      g.rotation.z=0.010*Math.sin(t*1.7+ph);
      g.position.y=y0+0.028*Math.sin(t*2.1+ph);
      driver.update(t);
    }};
  return api;
}

/* —— 车辙 makeCarzhe(o)：一串浅色平石自近及远微弯（合批 1 mesh）——古原上的路 */
function makeCarzhe(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22931:o.seed);
  const n=o.n===undefined?8:o.n, x0=o.x0===undefined?4:o.x0, z0=o.z0===undefined?-3:o.z0;
  const dx=o.dx===undefined?-0.55:o.dx, dz=o.dz===undefined?-0.84:o.dz, step=o.step===undefined?3.4:o.step;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const w=2.5-i*0.10, px=x0+dx*step*i+(R()-0.5)*0.5, pz=z0+dz*step*i+(R()-0.5)*0.5;
    const st=new THREE.BoxGeometry(w,0.12,w*0.66);
    st.translate(px,-1.54,pz); B.put(st,shadeColor(0xd8cdaa,0.9+0.25*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x5a5344,emissive:0x080705}),{c:0xe8d8ac,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  return g;
}

/* —— 遥遥城郭 makeChengying(o)：原顶北望的长安一痕（城垣+雉楼+屋舍+浮图，合批 1 mesh，
   暖缘微光）——「夕阳无限好」映照下的天际线；暮色四合时被城头暮霭渐渐掩住 */
function makeChengying(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22993:o.seed);
  const w=o.w===undefined?34:o.w;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,1.15,1.4); wall.translate(0,0.58,0); B.put(wall,0x3a362e);
  const cap=new THREE.BoxGeometry(w,0.12,1.7); cap.translate(0,1.21,0); B.put(cap,0x4a463c);
  const nt=Math.floor(w/6.5);
  for(let i=0;i<nt;i++){
    const tx=-w/2+3+i*6.5;
    const tw=new THREE.BoxGeometry(1.5,1.0,1.1); tw.translate(tx,1.7,0); B.put(tw,0x2f2c26);
    const tr=new THREE.ConeGeometry(1.25,0.7,4); tr.rotateY(Math.PI/4); tr.translate(tx,2.55,0); B.put(tr,0x28251f);
  }
  [[-8,-4,1.1],[2,-5.5,1.4],[9,-4.5,1.2],[-3,-6.5,1.5],[14,-6,1.1]].forEach(function(p){
    const bw=p[2], bh=1.0+R()*0.7;
    const hs=new THREE.BoxGeometry(bw*1.6,bh,bw*1.2); hs.translate(p[0],bh/2,p[1]); B.put(hs,0x302d27);
    const hr=new THREE.ConeGeometry(bw*1.15,0.75,4); hr.rotateY(Math.PI/4); hr.translate(p[0],bh+0.37,p[1]); B.put(hr,0x2a2721);
  });
  let ty=0;   /* 浮图一座 */
  for(let i=0;i<4;i++){
    const bw=1.9-i*0.34, bh=1.15-i*0.08;
    const seg=new THREE.BoxGeometry(bw,bh,bw); seg.translate(-w*0.30,ty+bh/2,2.2); B.put(seg,0x2d2a24);
    const eave=new THREE.BoxGeometry(bw*1.5,0.14,bw*1.5); eave.translate(-w*0.30,ty+bh,2.2); B.put(eave,0x242119);
    ty+=bh+0.14;
  }
  const tsp=new THREE.ConeGeometry(0.34,0.9,6); tsp.translate(-w*0.30,ty+0.45,2.2); B.put(tsp,0x242119);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x4a4436,emissive:0x070604}),{c:0xe4c690,i:o.rim===undefined?0.16:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1.15:o.scale);
  return g;
}

/* —— 暮鸦 makeGuiya(o)：几点远鸦剪影（自绘 V 形鸦贴图 Sprite），缓缓飞向夕阳——
   夕阳里的墨点，是「近黄昏」的注脚（fadeK 铁律：初值=最大） */
let _yaTex=null;
function yaTex(){
  if(_yaTex)return _yaTex;
  const c=document.createElement('canvas');c.width=64;c.height=32;const x=c.getContext('2d');
  x.strokeStyle='rgba(255,255,255,1)';x.lineWidth=5;x.lineCap='round';
  x.beginPath();x.moveTo(4,22);x.quadraticCurveTo(18,4,32,16);x.quadraticCurveTo(46,4,60,22);x.stroke();
  _yaTex=new THREE.CanvasTexture(c);return _yaTex;
}
function makeGuiya(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22961:o.seed);
  const n=o.n===undefined?5:o.n, w=o.w===undefined?26:o.w;
  const y=o.y===undefined?19:o.y, spread=o.spread===undefined?5:o.spread;
  const z=o.z===undefined?-150:o.z, zSpread=o.zSpread===undefined?8:o.zSpread;
  const x0=o.x0===undefined?-2:o.x0, vx=o.vx===undefined?-1.15:o.vx;
  const s=o.s===undefined?2.3:o.s, op=o.op===undefined?0.85:o.op;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:yaTex(),color:o.color===undefined?0x2a2c2a:o.color,
      transparent:true,opacity:op*(0.55+0.45*R()),depthWrite:false});
    const sp=new THREE.Sprite(m);
    sp.position.set(x0+R()*w, y+(R()-0.5)*spread, z+(R()-0.5)*zSpread);
    sp.scale.set(s*(0.8+0.5*R()),s*(0.42+0.22*R()),1);
    sp.renderOrder=4; g.add(sp);
    items.push({sp:sp,m:m,x0:sp.position.x,y0:sp.position.y,op0:m.opacity,ph:R()*6.283,
      v:vx*(0.75+0.5*R()),fl:2.4+R()*1.8});
  }
  g.update=function(t,k,dt){
    const kk=k===undefined?1:k, d=dt===undefined?0:dt;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.x0+=it.v*d;
      if(it.x0<x0-w)it.x0=x0+w*0.4;
      it.sp.position.x=it.x0;
      it.sp.position.y=it.y0+Math.sin(t*it.fl+it.ph)*0.5;
      it.sp.material.rotation=Math.sin(t*it.fl*0.5+it.ph)*0.18;
      it.m.opacity=kk*it.op0*(0.8+0.2*Math.sin(t*0.9+it.ph));
    }
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* 诗人：全诗贯穿的同一造型（苍绿袍，幞头——accent=#3e4436 正是袍色；每次 build 新建材质） */
function dlyFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x3e4436,belt:0x5a614c,skin:0xd8b28c,collar:0xd9d0b6,
    hair:0x1a1d1a,hat:'幞头',rimC:0xd8b888,rim:0.42,noProp:true,scale:scale===undefined?1.75:scale});
}

function bCover(){ // 卷首 · 驱车登原远望：古原苍莽、车影缓行、淡日偏西、暮鸦点点
  const g=new THREE.Group();
  const grd=makeGround({r:230,c1:0xe7dfc6,c2:0xccc09a,y:-1.6}); g.add(grd.mesh);
  const band=makeRange({r:300,h:26,layers:2,peaks:3,seed:22971,color:0x35312a,atmo:0xdcd2b8,
    fogK:0.66,glowK:0.10,glow:0xe8c890,y:-16,order:-6});
  band.g.position.set(12,0,-175); band.g.rotation.y=Math.PI; g.add(band.g);
  const band2=makeRange({r:215,h:16,layers:2,peaks:4,seed:22972,color:0x3a352c,atmo:0xdcd2b8,
    fogK:0.60,glowK:0.13,glow:0xe8c890,y:-12,order:-6});
  band2.g.position.set(-6,0,-146); band2.g.rotation.y=Math.PI; g.add(band2.g);
  const sun=makeXiyang({r:12,y0:42}); sun.g.position.set(-30,42,-150); g.add(sun.g);
  const path=makeCarzhe({seed:22973,n:8,x0:4,z0:-3}); g.add(path);
  const cart=makeCheying({seed:22974,x:3.5,z:-5}); g.add(cart.g);
  const gany=makeGuiya({n:4,x0:-16,w:20,y:38,z:-142,seed:22975,s:2.0,op:0.8}); g.add(gany.g);
  const mist=makeMist({n:6,spread:[220,16,80],pos:[0,4.5,-72],scale:62,color:0xe6d8b4,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:15,d:6,color:0x2c2a24,seed:22976,rim:0.10,rimC:0xe8d8ac});
  fg1.g.position.set(-12,-1.8,16); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:10,n:4,d:4,sway:0.5,color:0x2a2822,seed:22977,rim:0.10,rimC:0xe8d8ac});
  fg2.g.position.set(17.5,-1.2,15); g.add(fg2.g);
  addLights(g,{c:0xe8d4a4,i:0.5,p:[-40,80,10]},{c:0xd8d2c0,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    band.update(t,0); band2.update(t,0);
    sun.update(t,k); cart.update(t,dt,k); gany.update(t,k,dt); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXiangwan(){ // 壹 · 向晚驱车 —— 向晚意不适，驱车登古原：车影缓行于古原车辙，淡日偏西
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0xe7dec4,c2:0xcdbf98,y:-1.6}); g.add(grd.mesh);
  const band=makeRange({r:290,h:24,layers:2,peaks:3,seed:22981,color:0x35312a,atmo:0xdcd2b8,
    fogK:0.64,glowK:0.11,glow:0xe8c890,y:-15,order:-6});
  band.g.position.set(8,0,-170); band.g.rotation.y=Math.PI; g.add(band.g);
  const band2=makeRange({r:210,h:13,layers:2,peaks:4,seed:22982,color:0x3a352c,atmo:0xdcd2b8,
    fogK:0.58,glowK:0.14,glow:0xe8c890,y:-12,order:-6});
  band2.g.position.set(-10,0,-142); band2.g.rotation.y=Math.PI; g.add(band2.g);
  const sun=makeXiyang({r:14,y0:38}); sun.g.position.set(-27,38,-148); g.add(sun.g);
  const path=makeCarzhe({seed:22983,n:9,x0:6,z0:-1}); g.add(path);
  const cart=makeCheying({seed:22984,x:5.5,z:-3}); g.add(cart.g);
  const gany=makeGuiya({n:3,x0:-14,w:16,y:34,z:-138,seed:22985,s:1.8,op:0.75}); g.add(gany.g);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,4,-66],scale:60,color:0xe6d8b4,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:6,color:0x2c2a24,seed:22986,rim:0.10,rimC:0xe8d8ac});
  fg1.g.position.set(-10,-1.8,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.3,w:10,d:5,color:0x2c2a24,seed:22987,rim:0.10,rimC:0xe8d8ac});
  fg2.g.position.set(12.5,-1.6,11); g.add(fg2.g);
  addLights(g,{c:0xe8d2a0,i:0.5,p:[-46,70,-10]},{c:0xd8d0bc,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    band.update(t,0); band2.update(t,0);
    sun.update(t,k); cart.update(t,dt,k); gany.update(t,k,dt); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXiyangHuanghun(){ // 贰（末境·可点击）· 夕阳黄昏 —— 夕阳无限好，只是近黄昏：
                            // 点击夕阳大盛而后徐沉+暮色四合
  const ctl={t:0,clicked:false,on:false,dusk:0};
  const g=new THREE.Group();
  const grd=makeGround({r:220,c1:0xe9ddbe,c2:0xd2bd92,y:-1.6}); g.add(grd.mesh);
  const warmC1=C(0xe9ddbe),duskC1=C(0xc6bfae),warmC2=C(0xd2bd92),duskC2=C(0x9f9280);
  const band=makeRange({r:300,h:23,layers:2,peaks:3,seed:22991,color:0x35312a,atmo:0xdcd2b8,
    fogK:0.66,glowK:0.12,glow:0xe8c890,y:-16,order:-6});
  band.g.position.set(10,0,-172); band.g.rotation.y=Math.PI; g.add(band.g);
  const band2=makeRange({r:212,h:16,layers:2,peaks:4,seed:22992,color:0x3a352c,atmo:0xdcd2b8,
    fogK:0.60,glowK:0.16,glow:0xe8c890,y:-12,order:-6});
  band2.g.position.set(-8,0,-140); band2.g.rotation.y=Math.PI; g.add(band2.g);
  const glowItems=[];
  band.items.forEach(function(it){ glowItems.push({u:it.mesh.material.uniforms,base:0.12}); });
  band2.items.forEach(function(it){ glowItems.push({u:it.mesh.material.uniforms,base:0.16}); });
  /* 遥遥长安城郭（原顶北望）：城垣一痕、浮图一座 */
  const cheng=makeChengying({seed:22993}); cheng.position.set(17,-1.15,-116); cheng.rotation.y=-0.10; g.add(cheng);
  /* 城头暮霭：点击后渐浓，城郭渐隐入暮色（初值=暮时最大，基态取一成） */
  const hazeG=new THREE.Group(), hazeItems=[];
  for(let i=0;i<3;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:0xd8ccb2,transparent:true,
      opacity:0.5,depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set(13+i*5-5,1.2+(i%2)*1.4,-108-i*3);
    s.scale.set(30,10,1); s.renderOrder=5; hazeG.add(s);
    hazeItems.push({m:m,op0:0.5});
  }
  g.add(hazeG);
  const warmHaze=C(0xd8ccb2),duskHaze=C(0x8e8a92);
  /* 标志性瞬间：古原大夕阳（半衔远原线，一轮大日） */
  const sun=makeXiyang({r:36,y0:31}); sun.g.position.set(-20,31,-160); g.add(sun.g);
  /* 暮鸦点点，飞向夕阳 */
  const gany=makeGuiya({n:5,x0:-4,w:26,y:30,spread:5,z:-150,zSpread:7,seed:22994,s:2.3,op:0.9});
  g.add(gany.g);
  /* 停稳的车影（驱车至此） */
  const cart=makeCheying({seed:22995,move:0}); cart.g.position.set(11.5,-1.52,-24); cart.g.rotation.y=2.75; g.add(cart.g);
  /* 诗人立于原缘，指暮景 */
  const poet=dlyFigure(1.75,'指月'); poet.position.set(-8.2,-0.30,-8.6); poet.rotation.y=-3.06; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:1.8,w:8,d:5,color:0x2c2a24,seed:22996,rim:0.12,rimC:0xe8d8ac});
  rock.g.position.set(-9.4,-1.5,-5.6); g.add(rock.g);
  /* 暮霭横原：点击后加浓转灰（初值=暮时最大，基态取半） */
  const mist=makeMist({n:7,spread:[240,16,84],pos:[0,4.5,-78],scale:66,color:0xe6d8b4,op:0.30});
  g.add(mist.g);
  const warmMist=C(0xe6d8b4),duskMist=C(0x94909a);
  /* 初星：暮色四合后点点初现（点击前 maxA=0.001 压到不可见） */
  const stars=makeGlow({n:42,box:[280,90,30],pos:[0,70,-176],color:0xc4b89c,size:2.4,speed:0.02,rise:0,add:false,maxA:0.001});
  g.add(stars.points);
  /* 前景 */
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x2c2a24,seed:22997,rim:0.10,rimC:0xe8d8ac});
  fg1.g.position.set(-13,-1.9,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x2c2a24,seed:22998,rim:0.10,rimC:0xe8d8ac});
  fg2.g.position.set(13.5,-1.7,12); g.add(fg2.g);
  /* 局部暮光：暖起而随暮冷沉（自建灯便于逐帧动画；初值 0.5=最大） */
  const dLight=new THREE.DirectionalLight(0xf2cf92,0.5); dLight.position.set(-46,34,-110); g.add(dLight);
  const lw=C(0xf2cf92), lc=C(0x8f8fa2);
  addLights(g,null,{c:0xd6cdb6,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.dusk=Math.min(1,ctl.dusk+dt/8.0);
      const e=ctl.dusk, sm=function(a,b,x){x=Math.max(0,Math.min(1,(x-a)/(b-a)));return x*x*(3-2*x);};
      /* 夕阳大盛而后徐沉 */
      sun.setDusk(e,k);
      /* 暮色四合：暮霭加浓转灰、地面转冷、城郭渐隐、初星点点 */
      mist.update(t,k*(0.55+0.45*e));
      hazeG.children.forEach(function(s){ s.material.color.copy(warmHaze).lerp(duskHaze,e); });
      hazeItems.forEach(function(it){ it.m.opacity=k*it.op0*(0.10+0.90*e); });
      for(let i=0;i<glowItems.length;i++){
        const gi=glowItems[i];
        gi.u.uGlowK.value=gi.base*(1-0.85*e);
        gi.u.uGlow.value.copy(C(0xe8c890)).lerp(C(0x8e8c96),e);
      }
      dLight.color.copy(lw).lerp(lc,e);
      dLight.intensity=k*0.5*(0.90+0.10*Math.sin(t*0.7))*(1-0.75*e);
      grd.mat.uniforms.uC1.value.copy(warmC1).lerp(duskC1,e);
      grd.mat.uniforms.uC2.value.copy(warmC2).lerp(duskC2,e);
      stars.mat.uniforms.uMaxA.value=0.001+0.10*e*e;
      grd.update();
      band.update(t,0); band2.update(t,0);
      gany.update(t,k,dt); cart.update(t,0,k);
      stars.update(t);
      poet.update(t,k); rock.update(t,k); fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.32);
        pluck(2,0.05,0.11); pluck(4,0.6,0.09); pluck(1,1.3,0.08); pluck(0,2.1,0.07);   // 大盛一亮，徐沉三叠
        const fl=$('#flash'); fl.textContent='夕阳无限好 只是近黄昏';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xece3cc),hor:C(0xe6d5b0),bot:C(0xd6c69e),fog:C(0xe6dabb),fd:0.0050,star:0.03,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xe8d4a6),dirI:0.5,
  dirP:new THREE.Vector3(-50,80,-20),ambC:C(0xd8d2c0),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,11,60],t:[-4,11,46],lf:[-4,10.5,-24],lt:[-10,10.5,-40]},
  sky:()=>SK({fd:0.0046,star:0.03,hor:C(0xe6d8ba),bot:C(0xd8caa8)}) },
{ name:'向晚驱车',dwell:16,river:0.02,build:bXiangwan,
  cam:{f:[3,7.6,17],t:[-1,7.3,8],lf:[-2,7.8,-2],lt:[-8,8.2,-16]},
  sky:()=>SK({fd:0.0050,star:0.02,hor:C(0xe8d3a8),bot:C(0xd8c498),dirI:0.52,
    dirP:new THREE.Vector3(-46,66,-24)}) },
{ name:'夕阳黄昏',dwell:19,river:0.02,build:bXiyangHuanghun,
  cam:{f:[0,9,20],t:[-3,9.5,10],lf:[-2,9.3,-4],lt:[-7,10,-20]},
  sky:()=>SK({fd:0.0058,star:0.02,hor:C(0xeacf98),bot:C(0xd4bc8c),dirC:C(0xeccf96),dirI:0.55,
    dirP:new THREE.Vector3(-44,52,-70),ambC:C(0xd6cdb6),ambI:0.58}) },
];
"""
