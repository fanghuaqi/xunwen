# -*- coding: utf-8 -*-
"""pusaman-yugu.py —— 《菩萨蛮·书江西造口壁》（宋·辛弃疾，no.192，水墨夜思）生成配置
两境（稼轩抚时感事之名作，N=queue stages=2）：
  壹·郁孤台下 —— 清江水带行人泪，西北望长安，可怜无数山遮断望眼（泪江→望断）
  贰·毕竟东流 —— 全词气骨：江水冲开青山夹峙奔流而去（大势不可挡）；江晚愁余、山深闻鹧鸪（转沉）
末境可点击：点击江水 —— 雾闸散开、两岸青山让路、一线银光水路亮起、急流迸发，鹧鸪啼「行不得也哥哥」作收束音效"""

META = dict(
    N=2, slug='pusaman-yugu', title='菩萨蛮·书江西造口壁', dyn='宋 · 辛弃疾', brand_author='辛弃疾',
    gold_rgb='143,164,192',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#8fa4c0; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(143,164,192,.26);
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
    tip='轻点画面 / 按空格 —— 江水冲开夹峙青山，毕竟东流去',
    hint='← → 键或空格逐境游览 · 末境可点击江水：冲开青山夹峙，毕竟东流去',
    cover_read='菩萨蛮·书江西造口壁。宋，辛弃疾。郁孤台下清江水，中间多少行人泪。西北望长安，可怜无数山。',
    cover_p1='两重意境，随词句次第展开：先登郁孤台，看清江水带走多少行人泪——西北望长安，可怜无数山遮断望眼；再入江晚山深，看江水冲开青山夹峙浩荡东流，鹧鸪声里，满腔忠愤化作暮色啼鸣。',
    cover_p2='边读词，边走进稼轩笔下造口暮江的郁孤台上，体会「青山遮不住，毕竟东流去」的大势与悲慨。',
    end_h2='江去 · 愁余', cn_word='两',
    words_js="['再游一次，且听江声','初识稼轩，尚需共读','渐入佳境，再诵几遍','词境渐深，江声入怀','已解青山遮不住之意','郁孤台下，忠愤满襟']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'郁孤台下', jing:'郁孤台下，清江水带走多少行人泪 —— 西北望长安，可怜无数山遮断望眼。（高台 · 泪江 · 层山）',
  segs:[
   {c:'郁孤台下清江水，', p:py('yù gū tái xià qīng jiāng shuǐ')},
   {c:'中间多少行人泪。', p:py('zhōng jiān duō shǎo xíng rén lèi')},
   {c:'西北望长安，', p:py('xī běi wàng cháng ān')},
   {c:'可怜无数山。', p:py('kě lián wú shù shān')}],
  read:'郁孤台下清江水，中间多少行人泪。西北望长安，可怜无数山。',
  yisi:'郁孤台下，滚滚赣江清流日夜奔涌，这江水中，掺和着多少流离行人的眼泪啊！举头西北遥望故都长安，可怜被无数的青山遮挡，望不见那残破的山河。——以水带泪，以山遮眼，家国之痛尽在其中。',
  zhu:[['菩萨蛮','词牌名，双调四十四字；此词作于宋孝宗淳熙二、三年间，辛弃疾任江西提点刑狱，驻节赣州，题词于造口壁'],['郁孤台','在今江西赣州西北贺兰山上，为郡城登临胜地；唐人李勉登台北望京阙，改题「望阙」'],['清江','赣江水色清深，此指造口之下奔流的赣江'],['行人泪','建炎年间金兵南下，追隆祐太后御舟至造口，士民流离死难；「行人泪」即指国难中流离者的血泪'],['西北望长安','长安借指北宋故都汴京与沦陷的中原；西北，故土所在之方'],['可怜','可惜，可叹']] },
{ name:'毕竟东流', jing:'青山遮不住，毕竟东流去 —— 江晚愁余，山深鹧鸪声声「行不得也哥哥」。（点击江水 · 冲开夹峙）',
  segs:[
   {c:'青山遮不住，', p:py('qīng shān zhē bú zhù')},
   {c:'毕竟东流去。', p:py('bì jìng dōng liú qù')},
   {c:'江晚正愁余，', p:py('jiāng wǎn zhèng chóu yú')},
   {c:'山深闻鹧鸪。', p:py('shān shēn wén zhè gū')}],
  read:'青山遮不住，毕竟东流去。江晚正愁余，山深闻鹧鸪。',
  yisi:'青山哪能遮得住？江水终究冲开重山夹峙，浩浩东流而去。暮色苍茫的江景令我愁绪满怀，忽听得深山里传来鹧鸪「行不得也哥哥」的啼声。——水喻大势所趋不可阻挡，鸟啼道尽恢复无路的悲愤。',
  zhu:[['遮不住','青山纵然层叠夹峙，也遮不住东流的江水；梁武帝「青山不可上，一上一怅惘」、李白「抽刀断水水更流」同此意脉'],['毕竟','终归，终究'],['愁余','使我发愁；余，我。江晚暮色，正令我愁绪难遣'],['鹧鸪','鸟名，其鸣悲切，古人拟其音为「行不得也哥哥」——闻之如闻恢复之事「行不得」，愁上加愁']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「青山遮不住」的下一句是？', o:['毕竟东流去','江晚正愁余','可怜无数山'], a:0},
 {q:'「江晚正愁余」的下一句是？', o:['可怜无数山','中间多少行人泪','山深闻鹧鸪'], a:2},
 {q:'「山深闻鹧鸪」的「鹧鸪」（zhè gū），古人拟其啼声为？寓意何在？', o:['「不如归去」，盼游子早归故里','「行不得也哥哥」，暗喻恢复中原之事难行','「关关」，喻夫妇和鸣之乐'], a:1},
 {q:'词人题词造口壁，上片「中间多少行人泪」暗指的史事是？', o:['建炎年间金兵南下追隆祐太后至造口，士民流离死难','安史之乱中杜甫携家流离入蜀','靖康之变后徽钦二帝被掳北去'], a:0},
 {q:'「青山遮不住，毕竟东流去」寄托的主要情怀是？', o:['赞美赣江冲开群山的自然伟力','感叹时光如流水一去不返','以江水东流喻恢复大势不可阻挡，而自己忠愤郁结、壮志难酬'], a:2},
];
"""

SCENES_JS = """/* ================= 菩萨蛮·书江西造口壁 · 两境场景（水墨夜思：郁孤台下、毕竟东流） =================
   情感曲线：泪江→望断→江去→愁余，末境转沉；全词气骨在「青山遮不住，毕竟东流去」——
   点击江水：雾闸散开、两岸青山向两侧让路、一线银光水路亮起、急流迸发，鹧鸪啼作收束。 */

/* 鹧鸪啼：四声下行「行不得也哥哥」（WebAudio 合成；无音频上下文时静默返回） */
function zheguCall(){
  if(!groupAudio.ctx)return;
  const ctx=groupAudio.ctx, t0=ctx.currentTime+0.05;
  [[980,0.00],[820,0.30],[690,0.62],[520,0.95]].forEach(function(nt){
    const o=ctx.createOscillator(), ga=ctx.createGain();
    o.type='sine';
    o.frequency.setValueAtTime(nt[0]*1.05,t0+nt[1]);
    o.frequency.exponentialRampToValueAtTime(nt[0]*0.86,t0+nt[1]+0.24);
    ga.gain.setValueAtTime(0.0001,t0+nt[1]);
    ga.gain.exponentialRampToValueAtTime(0.14,t0+nt[1]+0.04);
    ga.gain.exponentialRampToValueAtTime(0.0001,t0+nt[1]+0.28);
    o.connect(ga).connect(groupAudio.master);
    o.start(t0+nt[1]); o.stop(t0+nt[1]+0.32);
  });
}

/* 郁孤台：两层台基 + 台身阁楼 + 上层小阁（攒尖顶）+ 台沿栏杆，合批 1 mesh */
function makeYugutai(){
  const B=new GeoBag(), c1=0x0b0f16, c2=0x111824, c3=0x18202e;
  const t1=new THREE.BoxGeometry(12,1.6,9); t1.translate(0,0.8,0); B.put(t1,c1);
  const t2=new THREE.BoxGeometry(8.6,1.5,6.6); t2.translate(0,1.6+0.75,0); B.put(t2,c1);
  const body=new THREE.BoxGeometry(5.2,4.6,4.4); body.translate(0,3.1+2.3,0); B.put(body,c2);
  const eave=new THREE.ConeGeometry(4.6,1.6,4); eave.rotateY(Math.PI/4);
  eave.scale(1.22,1,1.02); eave.translate(0,7.7+0.8,0); B.put(eave,c3);
  const up=new THREE.BoxGeometry(3.4,2.2,3.0); up.translate(0,9.3+1.1,0); B.put(up,c2);
  const roof=new THREE.ConeGeometry(3.2,1.7,4); roof.rotateY(Math.PI/4);
  roof.scale(1.22,1,1.02); roof.translate(0,11.5+0.85,0); B.put(roof,c3);
  for(let i=0;i<6;i++){
    const post=new THREE.BoxGeometry(0.14,1.0,0.14);
    post.translate(-3.9+i*1.56,3.1+0.5,3.15); B.put(post,c3);
  }
  const rail=new THREE.BoxGeometry(8.2,0.10,0.12); rail.translate(0,4.12,3.15); B.put(rail,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x8fa4c0,i:0.32,p:2.5})));
  return g;
}

/* 宫阙残影：西北山影之间若有若无的双阙残影（望长安而不得见） */
function makeGongque(){
  const B=new GeoBag(), c1=0x10141c, c2=0x161c28;
  [1,-1].forEach(function(s){
    const x=s*3.2;
    const body=new THREE.BoxGeometry(1.7,4.4,1.6); body.translate(x,2.2,0); B.put(body,c1);
    const roof=new THREE.ConeGeometry(1.6,0.9,4); roof.rotateY(Math.PI/4);
    roof.translate(x,4.4+0.45,0); B.put(roof,c2);
  });
  const wall=new THREE.BoxGeometry(4.4,1.9,1.3); wall.translate(0,0.95,0); B.put(wall,c1);
  const g=new THREE.Group();
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c,transparent:true,opacity:0.42}),{c:0x8fa4c0,i:0.3,p:2.5});
  g.add(new THREE.Mesh(mergeGeos(B.list),mat));
  return g;
}

/* 鹧鸪：栖鸟剪影（身+头+喙+尾，合批 1 mesh）——「山深闻鹧鸪」的收束之物 */
function makeZhegu(){
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.42,10,8); body.scale(1,0.86,1.35);
  body.translate(0,0.40,0); B.put(body,0x151b26);
  const head=new THREE.SphereGeometry(0.20,8,6); head.translate(0,0.78,0.44); B.put(head,0x121722);
  const beak=new THREE.ConeGeometry(0.05,0.16,5); beak.rotateX(Math.PI/2);
  beak.translate(0,0.76,0.62); B.put(beak,0x2c2a24);
  const tail=new THREE.ConeGeometry(0.16,0.55,6); tail.rotateX(-Math.PI*0.42);
  tail.translate(0,0.46,-0.62); B.put(tail,0x0e131c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x03050a}),{c:0x8fa4c0,i:0.26,p:2.6})));
  return g;
}

/* 山深林：暗色树影一簇（树干+锥冠，合批 1 mesh）——鹧鸪栖处 */
function makeSenlin(o){
  o=o||{}; const R=seedRnd(o.seed===undefined?31:o.seed), B=new GeoBag(), n=o.n===undefined?6:o.n;
  for(let i=0;i<n;i++){
    const h=4+R()*4, x=(R()-0.5)*(o.w===undefined?18:o.w), z=(R()-0.5)*(o.d===undefined?10:o.d);
    const tr=new THREE.CylinderGeometry(0.10,0.20,h,5); tr.translate(x,h*0.5,z); B.put(tr,0x080b11);
    const cn=new THREE.ConeGeometry(1.6+R()*0.9,h*0.9,7); cn.translate(x,h*0.95,z); B.put(cn,0x0a0f17);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x222c3e,emissive:0x03050a}),{c:0x8fa4c0,i:0.14,p:2.4})));
  return g;
}

/* 两岸崖壁：rockGeo 大石堆叠成山崖（点击后整组向两侧让路） */
function makeYabi(side,seed){
  const R=seedRnd(seed), B=new GeoBag();
  for(let i=0;i<4;i++){
    const r=7+R()*6;
    const rg=rockGeo(r,1,R);
    rg.scale(1,1.5+R()*0.6,1.25);
    rg.translate(side*(11+R()*7),r*0.55,-58+i*13+(R()-0.5)*6);
    B.put(rg,shadeColor(0x0b0f16,0.8+0.5*R()));
  }
  const grp=new THREE.Group();
  grp.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c0,i:0.20,p:2.4})));
  return grp;
}

/* 一线银光水路：贴水面的加色长带（自定义双 shader；点击后从峡谷深处亮起） */
const SHUI_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const SHUI_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float band=smoothstep(0.0,0.42,vUv.x)*smoothstep(1.0,0.58,vUv.x);
  band*=smoothstep(0.0,0.25,vUv.y)*smoothstep(1.0,0.55,vUv.y);
  float sway=0.90+0.10*sin(uTime*0.6+vUv.y*7.0);
  vec3 col=mix(vec3(0.66,0.74,0.86),vec3(0.30,0.38,0.50),vUv.y);
  gl_FragColor=vec4(col,uFade*uK*band*sway);
}`;

function bCover(){ // 封面 · 江月无声 —— 月下清江先在雾里流着
  const g=new THREE.Group();
  const water=makeWater({size:480,seg:80,amp:0.24,freq:0.11,speed:0.45,flow:[0.4,0.2],spec:1.8,
    deep:0x081221,shallow:0x142e46,skyc:0x22405c,moonDir:[26,104,-185]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:22,layers:2,peaks:4,seed:19200,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-16});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:19201,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:19202,sway:0.9});
  reeds.g.position.set(-13,-1.6,24); g.add(reeds.g);
  const mist=makeMist({n:10,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:64,box:[220,40,130],pos:[0,10,-40],color:0xa8b8ce,size:8,speed:0.05,rise:0,maxA:0.4});
  g.add(motes.points);
  addLights(g,{c:0xaebccd,i:0.42,p:[26,74,36]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); fg.update(t,k); reeds.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bYugu(){ // 壹 · 郁孤台下 —— 望西北人立台上，清江带泪，无数山遮断望眼
  const g=new THREE.Group();
  const water=makeWater({size:480,seg:90,amp:0.26,freq:0.12,speed:0.5,flow:[0.5,0.2],spec:1.9,
    deep:0x081221,shallow:0x14304a,skyc:0x23405e,moonDir:[34,118,-190]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:20,layers:2,peaks:4,seed:19203,color:0x070a10,atmo:0x1c2739,fogK:0.62,glowK:0.06,y:-18});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  /* 西北层山：一列更高的山影斜卧西北，遮断望眼（可怜无数山） */
  const west=makeRange({r:150,h:34,layers:1,peaks:6,seed:19204,arc:1.5,a0:3.25,
    color:0x0a0e16,atmo:0x2c3c52,fogK:0.60,glowK:0.05,y:-6});
  west.g.position.set(-30,0,-40); g.add(west.g);
  /* 郁孤台 + 台上望西北人（稼轩凭高，指顾中原） */
  const tai=makeYugutai(); tai.position.set(-13,0,-24); g.add(tai);
  const man=makeFigure({pose:'指月',robe:0x2b3444,belt:0x5a6a82,skin:0xc7ac8e,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0x8fa4c0,rim:0.55,noProp:true,scale:1.42});
  man.position.set(-13,3.1,-22.4); man.rotation.y=-1.05; g.add(man);
  /* 台头窗月微光（冷银，月是唯一主角） */
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(4.0,4.0,1); win.position.set(-13,5.4,-21.4); win.renderOrder=2; g.add(win);
  win.material.userData.baseOpacity=0.28;
  /* 西北山影间的宫阙残影（长安不见——只剩一线残影） */
  const gq=makeGongque(); gq.position.set(-52,0,-92); gq.rotation.y=0.5; gq.scale.setScalar(1.3); g.add(gq);
  /* 泪光：江面浮动的冷银光点（行人泪） */
  const tears=makeGlow({n:80,box:[100,4,60],pos:[0,0.9,-14],color:0xbcc9dc,size:4.5,speed:0.05,rise:0.06,maxA:0.30});
  g.add(tears.points);
  /* 流云 + 微尘 + 雾（水墨母题） */
  const clouds=makeFlow({n:110,box:[180,18,90],pos:[0,34,-60],color:0x8fa0b8,size:30,speed:2.2,maxA:0.15});
  g.add(clouds.points);
  const motes=makeGlow({n:56,box:[150,22,90],pos:[0,10,-30],color:0xa8b8ce,size:5,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,22,120],pos:[0,8,-52],scale:78,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:19205,rim:0.14});
  rk.g.position.set(-17,-1.2,14); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:12,n:8,d:5,color:0x04060a,seed:19206,sway:0.8,tip:0x4c586c,scale:0.7});
  reeds.g.position.set(16,-1.5,12); g.add(reeds.g);
  addLights(g,{c:0xb6c2d2,i:0.52,p:[28,84,-20]},{c:0x1e2532,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); west.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    tears.update(t); clouds.update(t);
    man.userData.update(t,k);
    win.material.opacity=k*0.28*(0.72+0.28*Math.sin(t*0.7));
    rk.update(t,k); reeds.update(t,k);
  }};
}

function bDongliu(){ // 贰（标志性瞬间·末境可点击）· 毕竟东流 —— 点击江水：冲开青山夹峙，奔流而去
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  const grd=makeGround({r:170,c1:0x07090e,c2:0x10141c});
  grd.mesh.position.y=-0.8; g.add(grd.mesh);
  const water=makeWater({size:360,seg:90,amp:0.34,freq:0.15,speed:0.55,flow:[0,1.5],spec:1.6,
    deep:0x081221,shallow:0x14304a,skyc:0x22344c,moonDir:[-70,110,-160]});
  g.add(water.mesh);
  const ridge=makeRange({r:260,h:16,layers:2,peaks:3,seed:19207,color:0x080b11,atmo:0x1b2330,fogK:0.58,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 青山夹峙（点击后整组向两侧让路——遮不住） */
  const wl=makeYabi(-1,19208); wl.position.set(-14,0,0); g.add(wl);
  const wr=makeYabi(1,19209);  wr.position.set(14,0,0);  g.add(wr);
  /* 下游雾闸：遮住去路（点击后散开） */
  const gate=[];
  for(let i=0;i<3;i++){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x5a6a80,
      transparent:true,opacity:0.42,depthWrite:false}));
    s.scale.set(46,20,1); s.position.set(0,7+i*3.5,-64-i*4); s.renderOrder=4; g.add(s);
    s.material.userData.baseOpacity=0.42; gate.push(s);
  }
  /* 江晚愁人：独立岸石，背影向水（愁余） */
  const rkMan=makeForeground({kind:'坡石',n:2,r:3.4,w:7,d:5,color:0x04060a,seed:19210,rim:0.14});
  rkMan.g.position.set(10,-0.5,-27); g.add(rkMan.g);
  const man=makeFigure({pose:'独立',robe:0x232c3c,belt:0x5a6a82,skin:0xc7ac8e,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0x8fa4c0,rim:0.5,noProp:true,scale:1.38});
  man.position.set(10,1.0,-27); man.rotation.y=Math.PI+0.25; g.add(man);
  /* 鹧鸪：栖在前景岩上（山深闻鹧鸪） */
  const rkL=makeForeground({kind:'坡石',n:3,r:3.2,w:9,d:5,color:0x04060a,seed:19211,rim:0.14});
  rkL.g.position.set(-12,-1.2,13); g.add(rkL.g);
  const zg=makeZhegu(); zg.scale.setScalar(1.6);
  zg.position.set(8.6,0.4,20.5); zg.rotation.y=2.6; g.add(zg);
  /* 山深林：两簇暗色树影（鹧鸪栖处） */
  const sen1=makeSenlin({n:7,seed:19212,w:26,d:12}); sen1.position.set(-30,0,-58); g.add(sen1);
  const sen2=makeSenlin({n:5,seed:19213,w:20,d:10}); sen2.position.set(32,0,-66); g.add(sen2);
  /* 一线银光水路（点击后从峡谷深处亮起）+ 峡口光晕 */
  const bandMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.30}},
    vertexShader:SHUI_VERT,fragmentShader:SHUI_FRAG});
  const band=new THREE.Mesh(new THREE.PlaneGeometry(22,120),bandMat);
  band.rotation.x=-Math.PI/2; band.position.set(0,0.16,-35); band.renderOrder=2; g.add(band);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.10,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(30,16,1); halo.position.set(0,9,-70); halo.renderOrder=3; g.add(halo);
  halo.material.userData.baseOpacity=0.35;
  /* 急流水雾（点击后加急）+ 水花迸发 + 愁绪微尘 + 雾 */
  const rapids=makeFlow({n:200,box:[30,8,60],pos:[0,3,-40],color:0x8398b4,size:18,speed:9,maxA:0.20});
  g.add(rapids.points);
  const burst=makeBurst({n:60,color:0xaebfd8,pos:[0,2.5,-34]}); g.add(burst.points);
  const wisps=makeGlow({n:36,box:[14,10,10],pos:[10,4,-26],color:0x7e8ea8,size:5,speed:0.05,rise:0.16,maxA:0.22});
  g.add(wisps.points);
  const motes=makeGlow({n:50,box:[140,16,70],pos:[0,8,-50],color:0xa8b8ce,size:5,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[230,22,120],pos:[0,8,-58],scale:80,color:0x7e8ea8,op:0.07});
  g.add(mist.g);
  const treeR=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:19214,sway:1.4,rim:0.16});
  treeR.g.position.set(14,-0.5,34); g.add(treeR.g);
  const reedsL=makeForeground({kind:'芦苇',n:14,w:28,d:6,color:0x04060a,seed:19215,sway:1.2});
  reedsL.g.position.set(-15,-0.8,31); g.add(reedsL.g);
  const rkR=makeForeground({kind:'坡石',n:2,r:3.0,w:10,d:6,color:0x04060a,seed:19216,rim:0.12});
  rkR.g.position.set(8,-1.3,20); g.add(rkR.g);
  addLights(g,{c:0x9db0c6,i:0.46,p:[-24,76,-16]},{c:0x171e2a,i:0.56});
  const pl=new THREE.PointLight(0x9fb3cc,0,80); pl.position.set(0,14,-68);
  pl.userData.baseI=1.5; g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/3.0);
      const rv=ctl.reveal;
      ridge.update(t,0); mist.update(t,k); motes.update(t); rapids.update(t);
      burst.update(t); wisps.update(t);
      wl.position.x=-14-6.5*rv; wr.position.x=14+6.5*rv;
      water.mesh.material.uniforms.uSpeed.value=0.55*(1+1.9*rv);
      water.mesh.material.uniforms.uAmp.value=0.34*(1+0.8*rv);
      water.update(t);
      for(let i=0;i<gate.length;i++)gate[i].material.opacity=k*(0.42-0.34*rv);
      bandMat.uniforms.uTime.value=t; bandMat.uniforms.uFade.value=k;
      bandMat.uniforms.uK.value=0.30+0.55*rv;
      halo.material.opacity=k*(0.10+0.25*rv);
      pl.intensity=k*(0.10+1.40*rv)*(0.90+0.10*Math.sin(t*2.0));
      man.userData.update(t,k);
      zg.position.y=0.4+0.05*Math.sin(t*1.25);
      treeR.update(t,k); reedsL.update(t,k); rkR.update(t,k); rkL.update(t,k); rkMan.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire();
        zheguCall();
        pluck(2,0.05,0.12); pluck(4,0.5,0.10); pluck(0,1.0,0.09);
        const fl=$('#flash'); fl.textContent='毕竟东流去'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x131a26),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(34,118,-190),ms:1.8,mph:0,mhaze:0.05,dirC:C(0xaebccd),dirI:0.5,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x1b2230),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,14,-40],lt:[0,14,-40]},
  sky:()=>SK({top:C(0x060910),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111826),fd:0.0048,star:0.45,
    ms:1.65,moon:new THREE.Vector3(26,104,-185),
    dirC:C(0xaebccd),dirI:0.44,ambC:C(0x192231),ambI:0.62}) },
{ name:'郁孤台下',dwell:16,river:0.05,build:bYugu,
  cam:{f:[0,6.5,26],t:[1.2,6.3,23],lf:[-11,7,-24],lt:[-10.2,6.8,-25.5]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x1a2231),bot:C(0x090d13),fog:C(0x131a26),fd:0.0060,star:0.5,
    ms:1.85,mph:0,mhaze:0.04,moon:new THREE.Vector3(34,118,-190),
    dirC:C(0xb8c2ce),dirI:0.52,dirP:new THREE.Vector3(28,84,-20),ambC:C(0x1e2532),ambI:0.64}) },
{ name:'毕竟东流',dwell:18,river:0.07,build:bDongliu,
  cam:{f:[0,6,40],t:[0,6.4,34],lf:[0,7,-55],lt:[0,7.5,-60]},
  sky:()=>SK({top:C(0x05080e),hor:C(0x121a26),bot:C(0x070a10),fog:C(0x141c29),fd:0.0062,star:0.36,
    ms:1.55,mph:0.12,mhaze:0.10,moon:new THREE.Vector3(-40,96,-200),
    dirC:C(0x93a4ba),dirI:0.44,dirP:new THREE.Vector3(-26,74,-16),ambC:C(0x171e2a),ambI:0.56}) },
];
"""
