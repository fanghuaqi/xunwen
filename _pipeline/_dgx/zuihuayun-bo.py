# -*- coding: utf-8 -*-
"""zuihuayun-bo.py —— 《醉花阴·薄雾浓云愁永昼》（宋·李清照，no.186，宣纸留白）生成配置
两境（N=queue stages 数）：愁雾凉宵（永昼雾云·瑞脑金兽·重阳纱厨凉透）、
西风瘦菊（东篱把酒·暗香盈袖·末境点击「帘卷西风，菊影人影对瘦」）。
宣纸留白：浅纸底、淡墨云山、大量留白；菊用浅赭黄淡彩（低饱和，非金），是全页唯一暖彩；
永昼日光淡弱、半夜月色清冷。标志瞬间：帘卷西风——帘内人影与东篱瘦菊同框对瘦。"""

META = dict(
    N=2, slug='zuihuayun-bo', title='醉花阴·薄雾浓云愁永昼', dyn='宋 · 李清照', brand_author='李清照',
    gold_rgb='80,72,74',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#50484a; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(80,72,74,.26);
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
    tip='轻点画面 / 按空格 —— 西风卷帘，菊影人影对瘦',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看西风卷帘、人比黄花瘦',
    cover_read='醉花阴·薄雾浓云愁永昼。宋，李清照。薄雾浓云愁永昼，瑞脑销金兽。佳节又重阳，玉枕纱厨，半夜凉初透。',
    cover_p1='两重意境，随词句次第展开：薄雾浓云愁永昼的黯淡长昼；瑞脑销金兽的一炉沉香；佳节又重阳、玉枕纱厨半夜凉初透的孤清寒夜；东篱把酒黄昏后的淡淡菊香；最终帘卷西风——人与黄花对瘦，销魂尽在千古一个「瘦」字。',
    cover_p2='边读词，边走进那幅淡墨闺秋——雾云永昼是一天，凉透纱厨是一夜，而瘦过黄花的，是相思人。',
    end_h2='魂销 · 花瘦', cn_word='两',
    words_js="['再读一遍，帘卷西风','初识易安，尚需共读','渐入佳境，再诵几遍','词境渐深，暗香盈袖','已解东篱把酒意','人比黄花，千古瘦字']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = """const POEM = [
{ name:'愁雾凉宵', jing:'薄雾浓云愁永昼 —— 雾云黯黯日如年，一炉香冷玉枕寒。（雾 · 香 · 凉）',
  segs:[
   {c:'薄雾浓云愁永昼，', p:py('bó wù nóng yún chóu yǒng zhòu')},
   {c:'瑞脑销金兽。', p:py('ruì nǎo xiāo jīn shòu')},
   {c:'佳节又重阳，', p:py('jiā jié yòu chóng yáng')},
   {c:'玉枕纱厨，', p:py('yù zhěn shā chú')},
   {c:'半夜凉初透。', p:py('bàn yè liáng chū tòu')}],
  read:'薄雾浓云愁永昼，瑞脑销金兽。佳节又重阳，玉枕纱厨，半夜凉初透。',
  yisi:'薄雾漫漫，浓云低垂，愁绪仿佛随着这漫漫白昼一起绵长难挨。兽形的铜香炉里，瑞脑香一点一点燃尽消融。又到了重阳佳节，独卧纱帐间，枕着玉枕，到半夜时分，凉意初次浸透了全身。——白昼愁长，夜半凉透，佳节偏偏独处，孤清从早到晚。',
  zhu:[['薄雾浓云','薄薄的雾，浓厚的云，烘出阴沉郁结的天色；一个「愁」字把天气与心境拧在了一起'],['永昼','漫长的白天；秋日本已昼短，偏说「永昼」，是愁人觉得时光格外难熬'],['瑞脑销金兽','瑞脑：香料名，即龙脑冰片；金兽：兽形铜香炉——瑞脑香在金兽炉中缓缓燃尽，「销」是消融、燃消'],['重阳','农历九月初九；古俗登高、佩茱萸、饮菊花酒，亲友团聚——佳节偏独守闺中，倍增孤清'],['玉枕纱厨','玉枕：光洁如玉的瓷枕；纱厨：防蚊的纱帐。半夜凉气刚刚浸透——不单是天凉，更是心境之凉']] },
{ name:'西风瘦菊', jing:'东篱把酒黄昏后 —— 帘卷西风处，人比黄花瘦。（酒 · 帘 · 菊）',
  segs:[
   {c:'东篱把酒黄昏后，', p:py('dōng lí bǎ jiǔ huáng hūn hòu')},
   {c:'有暗香盈袖。', p:py('yǒu àn xiāng yíng xiù')},
   {c:'莫道不销魂，', p:py('mò dào bù xiāo hún')},
   {c:'帘卷西风，', p:py('lián juǎn xī fēng')},
   {c:'人比黄花瘦。', p:py('rén bǐ huáng huā shòu')}],
  read:'东篱把酒黄昏后，有暗香盈袖。莫道不销魂，帘卷西风，人比黄花瘦。',
  yisi:'黄昏之后，到东篱下把盏饮酒，淡淡的菊香幽幽地盈满了衣袖。莫要说此情此景不叫人黯然神伤——西风卷起帘子，帘内那细细的身影，竟比篱边的黄菊还要清瘦。',
  zhu:[['东篱','化用陶渊明「采菊东篱下」——菊自此与高洁相连；易安把酒赏菊，亦有此意'],['暗香盈袖','幽幽菊香盈满衣袖；暗香既是菊香，也是挥之不去的思念'],['销魂','魂魄仿佛离体，形容愁苦到极处；「莫道不销魂」是反说，实则早已愁到极点'],['帘卷西风','即「西风卷帘」的倒文：秋风卷动帘幕——帘一动，帘内人影便与帘外黄菊撞个正着'],['人比黄花瘦','黄花：菊花。菊瓣纤长清瘦，人竟比菊还瘦——以形写神，相思之苦尽在一个「瘦」字，千古名句']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「薄雾浓云愁永昼」的下一句是？', o:['佳节又重阳','瑞脑销金兽','东篱把酒黄昏后'], a:1},
 {q:'「东篱把酒黄昏后」的下一句是？', o:['有暗香盈袖','帘卷西风，人比黄花瘦','莫道不销魂'], a:0},
 {q:'「瑞脑销金兽」中「销」的读音与意思是？', o:['xiāo，消融、燃尽——瑞脑香在兽形铜炉里缓缓燃消','xiāo，销毁——把金兽熔化掉','shāo，烧火——在金兽炉里烧炭取暖'], a:0},
 {q:'据《琅嬛记》载：赵明诚得此词，叹赏又自愧不如，闭门三日夜得五十阕，杂己作于其中请友人陆德夫品评，陆氏只称赏三句「绝佳」。是哪三句？', o:['东篱把酒黄昏后，有暗香盈袖','佳节又重阳，玉枕纱厨，半夜凉初透','莫道不销魂，帘卷西风，人比黄花瘦'], a:2},
 {q:'「人比黄花瘦」被推为千古名句，妙处在于？', o:['写重阳菊花开得不好，比人还瘦，景色凋零','菊瓣本就纤长清瘦，人比菊更瘦——说形瘦更写神伤，相思憔悴全在一个「瘦」字','人像黄花一样面黄肌瘦，是写词人生病了'], a:1},
];
"""

SCENES_JS = """/* ================= 醉花阴·薄雾浓云愁永昼 · 两境场景（宣纸留白：愁雾凉宵、西风瘦菊） =================
   浅纸为天、淡墨作云山，大量留白；菊用浅赭黄淡彩（宣纸赛道允许的低饱和淡彩，非金）。
   末境点击：西风卷帘——帘自下而上卷起，帘内人影与东篱瘦菊同框对瘦。 */

/* 淡日 makePaleSun(o) —— 永昼的日光淡弱：淡色日轮 + 一圈更淡的晕
   （fadeK 铁律：初始 opacity=最大值，逐帧只在其下浮动且必乘 fadeK） */
function makePaleSun(o){
  o=o||{};
  const r=o.r===undefined?10:o.r;
  const discOp=o.op===undefined?0.5:o.op, hazeOp=o.haze===undefined?0.15:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xf1ead8:o.color,
    transparent:true,opacity:discOp,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0xe3dbc4:o.hazeC,
    transparent:true,opacity:hazeOp,depthWrite:false,fog:false}));
  haze.scale.set(r*6.5,r*6.5,1); g.add(haze);
  g.userData.disc=disc; g.userData.haze=haze;
  g.userData.discOp=discOp; g.userData.hazeOp=hazeOp;
  g.update=function(t,k){
    disc.material.opacity=k*discOp*(0.94+0.06*Math.sin(t*0.5));
    haze.material.opacity=k*hazeOp*(0.85+0.15*Math.sin(t*0.33+1.7));
  };
  return g;
}

/* 兽形香炉 makeJinshou(o) —— 瑞脑销金兽：蹲兽驮一座镂盖小炉（合批 1 mesh） */
function makeJinshou(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.62,14,10);
  body.scale(1.25,0.82,0.95); body.translate(0,0.72,0); B.put(body,0x4a4238);
  const head=new THREE.SphereGeometry(0.34,12,9);
  head.scale(1.05,0.92,0.95); head.translate(0.72,1.02,0); B.put(head,0x453d33);
  const snout=new THREE.SphereGeometry(0.17,9,7);
  snout.scale(1.15,0.7,0.9); snout.translate(1.0,0.94,0); B.put(snout,0x3c352c);
  [1,-1].forEach(function(sd){
    const ear=new THREE.ConeGeometry(0.09,0.22,6);
    ear.rotateZ(-0.5*sd); ear.translate(0.66,1.36,0.22*sd); B.put(ear,0x453d33);
  });
  for(let i=0;i<4;i++){
    const lx=(i<2?0.34:-0.34), lz=(i%2?0.30:-0.30);
    const lg=new THREE.CylinderGeometry(0.11,0.13,0.5,7);
    lg.translate(lx,0.25,lz); B.put(lg,0x3c352c);
  }
  const tail=new THREE.ConeGeometry(0.10,0.42,6);
  tail.rotateZ(1.9); tail.translate(-0.78,0.86,0); B.put(tail,0x3c352c);
  /* 背上小炉：圈足炉身 + 半球镂空盖 + 兽钮 */
  const ship=new THREE.CylinderGeometry(0.40,0.46,0.30,14);
  ship.translate(-0.02,1.18,0); B.put(ship,shadeColor(0x4a4238,1.18));
  const lid=new THREE.SphereGeometry(0.36,14,8,0,Math.PI*2,0,Math.PI*0.5);
  lid.scale(1.05,0.62,1.05); lid.translate(-0.02,1.33,0); B.put(lid,shadeColor(0x4a4238,1.3));
  for(let i=0;i<6;i++){
    const a=i/6*6.283;
    const hole=new THREE.CylinderGeometry(0.045,0.045,0.10,6);
    hole.translate(-0.02+Math.cos(a)*0.22,1.50,Math.sin(a)*0.22*1.05); B.put(hole,0x241f19);
  }
  const knob=new THREE.SphereGeometry(0.13,9,7);
  knob.scale(1,0.8,1); knob.translate(-0.02,1.66,0); B.put(knob,shadeColor(0x453d33,1.25));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:42,
    specular:0x8a806c,emissive:0x0c0a08}),{c:0xe8e0ca,i:0.22,p:2.6})));
  g.scale.setScalar(s);
  g.update=function(t,k){ g.rotation.y=0.02*Math.sin(t*0.4); };
  g.userData.update=g.update;
  return g;
}

/* 纱厨玉枕 makeShachu(o) —— 纱帐 + 凉榻 + 玉枕：半夜凉初透（纱微透，帘内光景隐约） */
function makeShachu(o){
  o=o||{};
  const w=o.w===undefined?5.4:o.w, d=o.d===undefined?3.4:o.d, h=o.h===undefined?3.3:o.h;
  const B=new GeoBag();
  [1,-1].forEach(function(sx){ [1,-1].forEach(function(sz){
    const p=new THREE.CylinderGeometry(0.055,0.07,h,7);
    p.translate(sx*w*0.5,h*0.5,sz*d*0.5); B.put(p,0x4a3a2a);
  });});
  const top1=new THREE.BoxGeometry(w*1.06,0.09,d*1.06); top1.translate(0,h,0); B.put(top1,0x4a3a2a);
  const couch=new THREE.BoxGeometry(w*0.94,0.42,d*0.8); couch.translate(0,0.21,0); B.put(couch,0x33261a);
  const couchTop=new THREE.BoxGeometry(w*0.98,0.08,d*0.86); couchTop.translate(0,0.46,0); B.put(couchTop,0x3d2e1f);
  const pillow=new THREE.SphereGeometry(0.5,12,9);
  pillow.scale(1.5,0.42,0.8); pillow.translate(-w*0.22,0.72,0); B.put(pillow,0xdedac6);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x6a5a44,emissive:0x08060a}),{c:0xe8e0ca,i:0.2,p:2.5})));
  const gauzeMat=new THREE.MeshPhongMaterial({color:0xf2ecdc,shininess:4,specular:0x8a8574,
    transparent:true,opacity:0.30,side:THREE.DoubleSide,depthWrite:false});
  const gz=new THREE.Group();
  const back=new THREE.Mesh(new THREE.PlaneGeometry(w,h*0.96),gauzeMat);
  back.position.set(0,h*0.48,-d*0.5); back.renderOrder=2; gz.add(back);
  const front=new THREE.Mesh(new THREE.PlaneGeometry(w,h*0.96),gauzeMat);
  front.position.set(0,h*0.48,d*0.5); front.renderOrder=2; gz.add(front);
  [1,-1].forEach(function(sx){
    const side=new THREE.Mesh(new THREE.PlaneGeometry(d,h*0.96),gauzeMat);
    side.rotation.y=Math.PI/2; side.position.set(sx*w*0.5,h*0.48,0); side.renderOrder=2; gz.add(side);
  });
  const roof=new THREE.Mesh(new THREE.PlaneGeometry(w,d),gauzeMat);
  roof.rotation.x=-Math.PI/2; roof.position.set(0,h-0.06,0); roof.renderOrder=2; gz.add(roof);
  g.add(gz);
  const ph=Math.random()*6.283;
  g.update=function(t,k){
    for(let i=0;i<gz.children.length;i++) gz.children[i].rotation.z=0.012*Math.sin(t*0.5+i+ph);
  };
  g.userData.update=g.update;
  return g;
}

/* 篱菊 makeChrysanth(o) —— 丛生矮菊：茎叶灰绿、花瓣浅赭黄淡彩（低饱和，非金）；hero 为一株瘦菊大花 */
function makeChrysanth(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2640:o.seed);
  const n=o.n===undefined?7:o.n, spread=o.spread===undefined?2.4:o.spread;
  const hero=!!o.hero;
  const petals=hero?[0xcabb82,0xb9a96f,0xcabb82,0xd0c294]:[0xd0c088,0xc4b47c,0xb3a677,0xd8ca9a];
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, z=(R()-0.5)*spread*0.7;
    const hh=(hero?1.7:1.05)*(0.6+0.6*R());
    const tilt=(R()-0.5)*0.3;
    const st=new THREE.CylinderGeometry(hero?0.045:0.03,hero?0.07:0.055,hh,5);
    st.translate(0,hh*0.5,0); st.rotateZ(tilt); st.translate(x,0,z);
    B.put(st,0x6e7052);
    const nl=hero?2:1;
    for(let L=0;L<nl;L++){
      const lf=new THREE.SphereGeometry(0.13+R()*0.08,5,4);
      lf.scale(1.8,0.32,0.9); lf.rotateZ(tilt+(R()-0.5)*0.7);
      lf.translate(x+(R()-0.5)*0.4,hh*(0.25+0.35*R()),z+(R()-0.5)*0.3);
      B.put(lf,0x5c6148);
    }
    const hy=hh+(hero?0.2:0.1);
    /* 双环瓣：外环长瓣外垂、内环短瓣上仰，头更圆实（菊头不是平面星形） */
    const rings=hero?[[14,0.92,0.62,-0.30,0.072],[9,0.55,0.38,0.55,0.058]]
                    :[[8,0.5,0.3,-0.18,0.05],[5,0.3,0.18,0.5,0.04]];
    for(let r=0;r<rings.length;r++){
      const rg=rings[r];
      for(let k=0;k<rg[0];k++){
        const a=k/rg[0]*6.283+R()*0.5+r*0.45;
        const pl=new THREE.ConeGeometry(rg[4],rg[1],4);
        pl.translate(0,rg[1]*0.5,0);
        pl.rotateX(Math.PI/2-rg[3]-(R()-0.5)*0.3);
        pl.rotateY(a);
        pl.translate(x+Math.cos(a)*rg[2]*0.35,hy,z+Math.sin(a)*rg[2]*0.35);
        B.put(pl,r===0?petals[Math.floor(R()*petals.length)]:0xd8ca9a);
      }
    }
    const ct=new THREE.SphereGeometry(hero?0.17:0.09,7,5);
    ct.scale(1.15,0.7,1.15); ct.translate(x,hy+0.08,z);
    B.put(ct,0x8f7434);
  }
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x55503e,emissive:0x0e0c07})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 人影 makeRenYing(o) —— 帘内思妇剪影：纤细裙影，愈瘦愈见相思（标志瞬间：与菊对瘦） */
function makeRenYing(o){
  o=o||{};
  const ink=o.ink===undefined?0x39333a:o.ink;
  const sc=o.scale===undefined?1:o.scale;
  const prof=[[0.0,0.0],[0.52,0.0],[0.58,0.05],[0.50,0.35],[0.42,0.9],[0.30,1.5],[0.24,2.0],[0.26,2.45],[0.30,2.75],[0.26,2.95]];
  const B=new GeoBag();
  const robe=new THREE.LatheGeometry(prof.map(p=>new THREE.Vector2(p[0],p[1])),18);
  robe.scale(1,1,0.62); B.put(robe,ink);
  const hem=new THREE.TorusGeometry(0.54,0.045,5,20); hem.rotateX(Math.PI/2); hem.scale(1,1,0.62);
  hem.translate(0,0.05,0); B.put(hem,shadeColor(ink,0.7));
  const chest=new THREE.CylinderGeometry(0.20,0.30,0.5,10); chest.translate(0,2.9,0); B.put(chest,ink);
  const neck=new THREE.CylinderGeometry(0.10,0.12,0.26,8); neck.translate(0,3.24,0); B.put(neck,shadeColor(ink,0.9));
  const head=new THREE.SphereGeometry(0.27,12,9); head.scale(0.92,1.08,0.94); head.translate(0,3.52,0); B.put(head,ink);
  const bun=new THREE.SphereGeometry(0.14,9,7); bun.translate(0,3.86,-0.04); B.put(bun,shadeColor(ink,0.6));
  [1,-1].forEach(function(s){
    B.put(limbGeo([0.24*s,3.0,0.02],[0.34*s,1.7,0.06],0.11,0.07,6),ink);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a4442,emissive:0x0a0908}),{c:0xece5d0,i:0.24,p:2.3})));
  g.scale.setScalar(sc);
  g.update=function(t,k){ g.scale.y=sc*(1+0.005*Math.sin(t*1.1)); };
  g.userData.update=g.update;
  return g;
}

/* 帘架纱帘 makeLian2(o) —— 帘架 + 半透纱帘；setRoll(r)：r∈[0,1] 帘自下而上卷起（西风卷帘） */
function makeLian2(o){
  o=o||{};
  const w=o.w===undefined?4.8:o.w, h=o.h===undefined?5.0:o.h;
  const g=new THREE.Group();
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const post=new THREE.CylinderGeometry(0.07,0.09,h,7);
    post.translate(s*w*0.5,h*0.5,0); B.put(post,0x42362a);
    const ft=new THREE.CylinderGeometry(0.16,0.18,0.12,8);
    ft.translate(s*w*0.5,0.06,0); B.put(ft,0x332a20);
  });
  const beam=new THREE.BoxGeometry(w*1.12,0.12,0.16); beam.translate(0,h,0); B.put(beam,0x42362a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a563e,emissive:0x080503}),{c:0xe8e0ca,i:0.2,p:2.4})));
  const rod=new THREE.Mesh(new THREE.CylinderGeometry(0.035,0.035,w*0.98,8),
    new THREE.MeshPhongMaterial({color:0x4a3a2c,shininess:16,specular:0x6a563e}));
  rod.rotation.z=Math.PI/2; rod.position.set(0,h-0.22,0.05); g.add(rod);
  const cloth=new THREE.Mesh(new THREE.CylinderGeometry(2.5,2.5,(h-0.22)*0.96,22,1,true,-0.62,1.24),
    new THREE.MeshPhongMaterial({color:0xefe8d5,shininess:4,specular:0x8a8574,
      side:THREE.DoubleSide,transparent:true,opacity:0.55,depthWrite:false}));
  cloth.position.set(0,(h-0.22)*0.48,0.55); cloth.renderOrder=2; g.add(cloth);
  const roll=new THREE.Mesh(new THREE.CylinderGeometry(0.055,0.055,w*0.9,8),
    new THREE.MeshPhongMaterial({color:0x6a5a44,shininess:14,specular:0x8a7454}));
  roll.rotation.z=Math.PI/2; roll.position.set(0,h-0.22,0.55); roll.scale.set(1,0.22,0.22); g.add(roll);
  const topY=h-0.22, clothH=(h-0.22)*0.96;
  let ph=Math.random()*6.283;
  g.update=function(t,k,gust){
    const gu=gust||0;
    cloth.rotation.y=Math.sin(t*(0.62+gu*1.6))*(0.045+gu*0.22)+Math.sin(t*3.1)*gu*0.05;
    cloth.rotation.z=0.01*Math.sin(t*0.5+ph)+gu*0.03*Math.sin(t*2.7);
  };
  g.setRoll=function(r){
    const sy=Math.max(1-r*0.94,0.06);
    cloth.scale.y=sy;
    cloth.position.y=topY-clothH*sy*0.5;
    const rs=0.22+r*3.1;
    roll.scale.set(1,rs,rs);
  };
  g.userData.update=g.update;
  return {g:g,update:g.update,setRoll:g.setRoll};
}

/* 落菊瓣 makePetalBurst(o) —— 点击触发（uT0 激活）：菊瓣被西风扬起、旋舞着吹向帘边 */
const PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uT0;
varying float vA;
void main(){
  float age=uTime-uT0;
  vec3 p=position; float a=0.0;
  if(age>0.0&&age<9.0){
    float k=age/9.0;
    float sw=aSeed*6.283;
    p.y+=sin(uTime*1.2+sw)*(0.5+k*2.0)+(1.0-k)*1.6-k*k*4.5;
    p.x+=(aSeed*0.6+0.4)*k*15.0+sin(uTime*0.9+sw)*(0.4+k*2.6);
    p.z+=cos(uTime*0.8+sw*1.7)*(0.4+k*2.0);
    a=(1.0-k)*smoothstep(0.0,0.05,age);
  }
  vA=a;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const PETAL_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.14,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makePetalBurst(o){
  o=o||{};
  const n=o.n===undefined?120:o.n, src=o.src||[-8.2,2.4,-8.2];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=src[0]+(Math.random()-0.5)*1.8;
    P[i*3+1]=src[1]+(Math.random()-0.5)*1.2;
    P[i*3+2]=src[2]+(Math.random()-0.5)*1.6;
    S[i]=Math.random(); Z[i]=2.2+Math.random()*2.0;
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uT0:{value:-999},uColor:{value:C(0xcabb82)},uFade:{value:1},uMaxA:{value:o.maxA===undefined?0.8:o.maxA}},
    vertexShader:PETAL_VERT,fragmentShader:PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  const grp=new THREE.Group(); grp.add(points);
  let lastT=0;
  grp.update=function(t){ lastT=t; m.uniforms.uTime.value=t; };
  grp.fire=function(){ m.uniforms.uT0.value=lastT; };
  return {g:grp,update:grp.update,fire:grp.fire};
}

function bCover(){ // 卷首 · 宣纸秋庭：重阳明日，雾云未散
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d3,c2:0xdcd4bd,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:58,layers:3,peaks:6,seed:2631,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-88); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:180,h:26,layers:2,peaks:4,seed:2632,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-6,order:-5});
  ridge2.g.position.set(-8,0,-42); ridge2.g.rotation.y=Math.PI*1.03; g.add(ridge2.g);
  const chrys=makeChrysanth({seed:2633,n:6,spread:3.0});
  chrys.position.set(-8.5,-1.4,-13); g.add(chrys);
  const mist=makeMist({n:9,spread:[270,28,150],pos:[0,9,-60],scale:82,color:0xe2dbc6,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:42,box:[210,30,120],pos:[0,12,-36],color:0xb8bcc2,size:4,speed:0.04,
    rise:0.05,add:false,maxA:0.2});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.0,w:18,d:7,color:0x23262b,seed:2634,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(17,-1.9,14); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:36,n:14,d:6,color:0x2c2f33,seed:2635,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(-7,-1.5,34); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[60,110,40]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t);
    rk.update(t,k); reeds.update(t,k);
  }};
}

function bChouwu(){ // 一 · 愁雾凉宵 —— 薄雾浓云愁永昼，瑞脑销金兽；佳节又重阳，玉枕纱厨半夜凉初透
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0xe8e2d1,c2:0xd9d1b8,y:-1.5}); g.add(grd.mesh);
  /* 背景：淡墨远山两层 */
  const ridge=makeRange({r:270,h:64,layers:3,peaks:6,seed:2636,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:175,h:30,layers:2,peaks:5,seed:2637,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.03,glow:0xf4eeda,y:-5,order:-5});
  ridge2.g.position.set(-10,0,-38); ridge2.g.rotation.y=Math.PI*1.04; g.add(ridge2.g);
  /* 薄雾浓云愁永昼：纸面淡墨浓云缓缓横流 + 贴地薄雾 */
  const mist=makeMist({n:10,spread:[280,24,140],pos:[0,13,-58],scale:86,color:0xd8d0ba,op:0.14});
  g.add(mist.g);
  const clouds=makeFlow({n:420,box:[190,18,80],pos:[0,14,-48],color:0xa8a49a,size:22,speed:2.4,maxA:0.22});
  g.add(clouds.points);
  const lowMist=makeMist({n:6,spread:[190,10,90],pos:[0,1.2,-30],scale:60,color:0xe0dac8,op:0.10});
  g.add(lowMist.g);
  /* 永昼的日光淡弱：左上一轮淡日，晕在浓云之后 */
  const sun=makePaleSun({r:9,op:0.5});
  sun.position.set(-46,44,-84); g.add(sun);
  /* 瑞脑销金兽：矮香案 + 蹲兽铜炉 + 一缕香烟 */
  const incenseTable=makeTable({w:3.4,d:2.0,h:1.4,wood:0x33241a});
  incenseTable.g.position.set(-7.2,-1.5,-8.0); incenseTable.g.rotation.y=0.18; g.add(incenseTable.g);
  const censer=makeJinshou({scale:1.15});
  censer.position.set(-7.2,-0.1,-8.0); g.add(censer);
  const smoke=makeGlow({n:34,box:[0.6,4.4,0.6],pos:[-7.2,2.0,-8.0],color:0xc6c9be,size:3.4,speed:0.18,
    rise:0.6,add:false,maxA:0.3});
  g.add(smoke.points);
  /* 佳节又重阳：远处山坡上登高的人影三两（人独在闺中） */
  const climbers=makeCrowd({n:3,rect:[-30,-58,16,8],seed:2639,color:0x3a3d44,rimC:0xe8e2d0,rim:0.16,
    sMin:0.42,sMax:0.55,y:4});
  g.add(climbers.mesh);
  /* 玉枕纱厨，半夜凉初透：右侧纱厨一座，月色清冷、凉雾漫地 */
  const shachu=makeShachu({w:5.4,d:3.4,h:3.3});
  shachu.position.set(9.2,-1.5,-10.5); shachu.rotation.y=-0.28; g.add(shachu);
  const coolMist=makeMist({n:6,spread:[30,6,16],pos:[9,0.6,-10],scale:26,color:0xd6dad2,op:0.12});
  g.add(coolMist.g);
  const motes=makeGlow({n:44,box:[100,16,60],pos:[0,7,-22],color:0xb4bab8,size:4,speed:0.05,
    rise:0.07,add:false,maxA:0.2});
  g.add(motes.points);
  /* 前景：栏杆 + 芦苇框住画缘 */
  const rail=makeForeground({kind:'栏杆',w:30,h:3.2,color:0x2a2c30,seed:2641,rim:0.12,rimC:0xf0ead8});
  rail.g.position.set(-2,-2.0,17); g.add(rail.g);
  const reeds=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x2c2f33,seed:2642,sway:0.7,tip:0x4a4f56});
  reeds.g.position.set(-14,-1.6,10); g.add(reeds.g);
  addLights(g,{c:0xd8d4c4,i:0.46,p:[-40,110,30]},{c:0xd8d2c0,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0);
    mist.update(t,k); clouds.update(t); lowMist.update(t,k); coolMist.update(t,k);
    sun.update(t,k);
    smoke.update(t); motes.update(t); climbers.update(t);
    shachu.update(t,k); censer.update(t,k);
    rail.update(t,k); reeds.update(t,k);
  }};
}

function bShouju(){ // 二（末境·可点击）· 西风瘦菊 —— 东篱把酒黄昏后，有暗香盈袖；点击：帘卷西风，菊影人影对瘦
  const g=new THREE.Group();
  const ctl={t:0,last:-9,clicked:false,rolling:false,rolled:0,gust:0};
  const grd=makeGround({r:250,c1:0xe9e2cf,c2:0xd9cfb2,y:-1.5}); g.add(grd.mesh);
  /* 背景：黄昏淡墨远山（暮色稍暖） */
  const ridge=makeRange({r:270,h:66,layers:3,peaks:6,seed:2643,color:0x2c2f33,atmo:0xd8cfae,
    fogK:0.60,glowK:0.045,glow:0xf2e8cc,y:-8});
  ridge.g.position.set(0,0,-92); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:175,h:30,layers:2,peaks:4,seed:2644,color:0x23262b,atmo:0xd8cfae,
    fogK:0.68,glowK:0.03,glow:0xf2e8cc,y:-5,order:-5});
  ridge2.g.position.set(6,0,-36); ridge2.g.rotation.y=Math.PI*1.02; g.add(ridge2.g);
  /* 东篱：一段疏篱 + 篱下丛菊（浅赭黄淡彩） */
  const hedge=makeForeground({kind:'栏杆',w:13,h:2.1,color:0x3a352c,seed:2645,rim:0.14,rimC:0xe8e0ca});
  hedge.g.position.set(-7.5,-1.5,-15.5); hedge.g.rotation.y=0.12; g.add(hedge.g);
  const chrys1=makeChrysanth({seed:2646,n:8,spread:3.6});
  chrys1.position.set(-8.2,-1.5,-13.6); chrys1.scale.setScalar(1.25); g.add(chrys1);
  const chrys2=makeChrysanth({seed:2647,n:5,spread:2.2});
  chrys2.position.set(-3.2,-1.5,-14.6); g.add(chrys2);
  /* 标志主体：篱前一株瘦菊（大花纤瓣，与帘内人影对瘦） */
  const heroChrys=makeChrysanth({seed:2648,n:1,spread:0.6,hero:true});
  heroChrys.position.set(-8.2,-1.5,-8.2); heroChrys.scale.setScalar(2.05); g.add(heroChrys);
  /* 把酒：小案 + 陶壶陶杯 + 黄昏后伫立的人（衣取 accent 墨紫） */
  const table=makeTable({w:3.2,d:1.9,h:1.45,wood:0x33241a});
  table.g.position.set(-0.8,-1.5,-8.6); table.g.rotation.y=-0.14; g.add(table.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:1.15,liquid:false});
  hu.g.position.set(-1.4,-0.05,-8.6); g.add(hu.g);
  const bei=makeVessel({type:'杯',mat:'陶',scale:1.0,liquid:true});
  bei.g.position.set(-0.1,-0.05,-8.3); g.add(bei.g);
  const yian=makeFigure({pose:'独立',robe:0x4c4348,belt:0x332c30,skin:0xd9bfa4,collar:0xe9e2d0,
    hat:'发髻',rimC:0xece5d0,rim:0.30,noProp:true,scale:1.16});
  yian.position.set(1.6,-1.5,-7.4); yian.rotation.y=-0.55; g.add(yian);
  /* 有暗香盈袖：细碎菊瓣幽幽浮动在人侧 */
  const incense=makeGlow({n:26,box:[6.5,4.2,4.5],pos:[0.2,3.2,-8.4],color:0xd3c48e,size:3,speed:0.05,
    rise:0.14,add:false,maxA:0.3});
  g.add(incense.points);
  /* 帘架 + 纱帘：帘内人影隐约立于纱后（点击后卷帘现出，与瘦菊对瘦） */
  const lian=makeLian2({w:4.8,h:5.0});
  lian.g.position.set(9.0,-1.5,-10.6); lian.g.rotation.y=-0.3; g.add(lian.g);
  const renying=makeRenYing({scale:1.08});
  renying.position.set(9.3,-1.5,-12.2); renying.rotation.y=-0.22; g.add(renying);
  /* 西风：横流风绪（点击后增强） */
  const wind=makeFlow({n:380,box:[80,14,40],pos:[-8,7,-14],color:0xb8b2a0,size:16,speed:6.5,maxA:0.16});
  g.add(wind.points);
  /* 点击触发：菊瓣纷飞（瘦菊处起，向西风方向吹卷） */
  const petals=makePetalBurst({n:120,src:[-8.2,2.4,-8.2]}); g.add(petals.g);
  const motes=makeGlow({n:44,box:[100,16,60],pos:[0,7,-20],color:0xb8b2a4,size:4,speed:0.05,
    rise:0.07,add:false,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[240,24,130],pos:[0,8,-60],scale:78,color:0xe0d8c2,op:0.10});
  g.add(mist.g);
  /* 前景：坡石 + 枯苇框住画缘 */
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:20,d:7,color:0x23262b,seed:2649,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(-16,-1.8,12.5); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:30,n:13,d:6,color:0x2c2f33,seed:2650,sway:1.0,tip:0x4a4f56});
  reeds.g.position.set(10,-1.6,14); g.add(reeds.g);
  addLights(g,{c:0xd9ccb0,i:0.42,p:[-50,90,-20]},{c:0xd8d0bc,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.rolling){
        ctl.rolled=Math.min(1,ctl.rolled+dt/3.2);
        ctl.gust=Math.min(1,ctl.gust+dt/1.4);
      }
      lian.setRoll(ctl.rolled);
      lian.update(t,k,ctl.gust);
      ridge.update(t,0); ridge2.update(t,0);
      mist.update(t,k); motes.update(t); wind.update(t);
      incense.update(t); petals.update(t);
      yian.update(t,k); renying.update(t,k);
      rk.update(t,k); reeds.update(t,k);
      chrys1.rotation.z=0.012*Math.sin(t*0.9)*(1+ctl.gust*2.2);
      heroChrys.rotation.z=-0.014*Math.sin(t*0.8+1.2)*(1+ctl.gust*2.6);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.2)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      ctl.rolling=true;
      petals.fire();
      pluck(2,0.0,0.12); pluck(4,0.5,0.10); pluck(1,1.0,0.09); pluck(3,1.6,0.08);
      const fl=$('#flash'); fl.textContent='帘卷西风 人比黄花瘦';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.06,
  moon:new THREE.Vector3(128,122,-205),ms:0.9,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.52,
  dirP:new THREE.Vector3(60,120,40),ambC:C(0xd8d2c0),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,12,92],t:[0,11,82],lf:[0,18,-56],lt:[0,18,-56]},
  sky:()=>SK({fd:0.0045,star:0.05,ms:0.7,moon:new THREE.Vector3(130,118,-200)}) },
{ name:'愁雾凉宵',dwell:17,river:0.02,build:bChouwu,
  cam:{f:[-1.5,6.5,26],t:[2.0,5.8,20],lf:[-1.0,6.0,-8],lt:[3.5,6.2,-14]},
  sky:()=>SK({fd:0.0058,star:0.04,ms:0.8,mph:0.14,mhaze:0.04,
    moon:new THREE.Vector3(118,102,-190),dirC:C(0xd6d4c8),dirI:0.46}) },
{ name:'西风瘦菊',dwell:19,river:0.02,build:bShouju,
  cam:{f:[0,6.2,22],t:[1.4,5.6,17],lf:[-0.5,5.6,-9],lt:[0.8,6.0,-15]},
  sky:()=>SK({fd:0.0070,star:0.03,ms:0.9,mph:0.2,mhaze:0.05,
    moon:new THREE.Vector3(-108,96,-192),dirC:C(0xd9ccb0),dirI:0.4,ambI:0.58}) },
];
"""
