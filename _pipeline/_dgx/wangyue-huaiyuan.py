# -*- coding: utf-8 -*-
"""wangyue-huaiyuan.py —— 《望月怀远》（唐·张九龄，no.214，水墨夜思）生成配置
四境（五律四联各一境）：
  壹 海月天涯（首联·全诗冠联·标志性瞬间：大月自海面涌起，一轮月照两头）
  贰 遥夜相思（颔联·长夜流云、露光初凝，相思竟夕而起）
  叁 灭烛披衣（颈联·时序小戏：烛灭→月光满室，披衣出户→露湿衣裳）
  肆 盈手佳期（尾联·末境点击明月：月轮满升 + 两地对望光带相连）"""

META = dict(
    N=4, slug='wangyue-huaiyuan', title='望月怀远', dyn='唐 · 张九龄', brand_author='张 九 龄',
    gold_rgb='159,179,204',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#9fb3cc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(159,179,204,.26);
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
    tip='轻点画面 / 按空格 —— 明月满升，两地光带相连',
    hint='← → 键或空格逐境游览 · 末境可点击明月，看月轮满升、两地对望光带相连',
    cover_read='望月怀远。唐，张九龄。海上生明月，天涯共此时。情人怨遥夜，竟夕起相思。',
    cover_p1='四重意境，随诗句次第展开：海上明月自波间涌起，天涯两地共望此轮清辉；长夜难尽，相思竟夕而起；灭烛披衣，月光满室、夜露沾衣；末了月光满手却不能相赠，唯盼梦中赴一场佳期。',
    cover_p2='边读诗，边走进张九龄笔下海天月色、两地相思的清辉世界。',
    end_h2='月满 · 梦佳', cn_word='四',
    words_js="['再望一次海明月','初识曲江，尚需共读','渐入佳境，再诵几遍','诗境渐深，月华满襟','已解两地相思之切','天涯此时，梦亦佳期']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'海月天涯', jing:'海上明月自波间涌起，天涯两端共望此轮清辉 —— 千古冠联，一轮月照两头。（海 · 月 · 两地）',
  segs:[
   {c:'海上生明月，', p:py('hǎi shàng shēng míng yuè')},
   {c:'天涯共此时。', p:py('tiān yá gòng cǐ shí')}],
  read:'海上生明月，天涯共此时。',
  yisi:'海面上升起一轮明月，远在天涯的你我，此刻正共望这轮清辉。——起句即冠绝千古：一个「生」字写出明月自海面涌出的磅礴动感；「共此时」三字，把相隔两地的思念拉进同一片月光。',
  zhu:[['海上生明月','明月从海面上升起。不用「升」而用「生」，明月与大海如一同诞生，气象阔大'],['天涯','天的边际，指极远的地方，此处指远方的亲人所在'],['共此时','在这同一时刻共同望月。谢庄《月赋》「隔千里兮共明月」是其远源'],['怀远','怀念远方的亲人（一说友人），全诗诗眼所在']] },
{ name:'遥夜相思', jing:'长夜漫漫，怨它太长；竟夕不眠，相思暗生。（遥夜 · 相思）',
  segs:[
   {c:'情人怨遥夜，', p:py('qíng rén yuàn yáo yè')},
   {c:'竟夕起相思。', p:py('jìng xī qǐ xiāng sī')}],
  read:'情人怨遥夜，竟夕起相思。',
  yisi:'多情的人埋怨这夜太长，整夜整夜地思念，辗转难眠。——因念而怨夜长，因怨而更显念深；「竟夕」即终夜，一夜无眠，只把相思付与月光。',
  zhu:[['情人','有情之人、怀有相思之情的人，此处诗人自指'],['遥夜','长夜。遥，长——因相思难眠，才觉夜格外漫长'],['竟夕','终夜、通宵。竟，终'],['相思','彼此思念。月圆而人未圆，故一夜相思不断']] },
{ name:'灭烛披衣', jing:'灭烛见月光满室，披衣觉夜露沾衣 —— 由室内到户外，月色一步步把人引向天涯。（烛 · 光 · 露）',
  segs:[
   {c:'灭烛怜光满，', p:py('miè zhú lián guāng mǎn')},
   {c:'披衣觉露滋。', p:py('pī yī jué lù zī')}],
  read:'灭烛怜光满，披衣觉露滋。',
  yisi:'熄灭蜡烛，更爱这满屋的月光；披衣出门，才发觉露水已打湿了衣裳。——灭烛是为怜爱月光之「满」，披衣久立则见夜露之「滋」，一派痴态，皆由相思而生。',
  zhu:[['怜','爱怜。烛光反而夺月，灭烛正见爱月之痴'],['光满','月光满屋，皎洁盈室'],['披衣','披上衣服走出门户——月色太好，忍不住出户看月'],['觉露滋','发觉露水沾湿。滋，润泽沾湿——久立户外，衣裳为露所湿']] },
{ name:'盈手佳期', jing:'月光满手却不能赠人，还是回到梦里去赴那一场佳期吧。（盈手 · 梦佳期）（点击明月）',
  segs:[
   {c:'不堪盈手赠，', p:py('bù kān yíng shǒu zèng')},
   {c:'还寝梦佳期。', p:py('huán qǐn mèng jiā qī')}],
  read:'不堪盈手赠，还寝梦佳期。',
  yisi:'这月光虽可满握于手，却不能把它赠给远方的你；还是回到床上睡去吧，希望在梦里与你相会。——化用陆机「照之有余辉，揽之不盈手」而翻进一层：纵能盈手，也难以相赠，只好托之于梦。',
  zhu:[['不堪','不能。指月光虽可满握，却无法赠送远人'],['盈手','满手。化用陆机《拟明月何皎皎》「照之有余辉，揽之不盈手」'],['还寝','回到寝室就寝。还（huán），回'],['梦佳期','在梦中相会。佳期，美好的会面之期——现实难聚，唯托于梦']] },
];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「海上生明月」的下一句是？', o:['天涯共此时','海上明月共潮生','千里共婵娟'], a:0},
 {q:'「灭烛怜光满」的下一句是？', o:['不堪盈手赠','披衣觉露滋','情人怨遥夜'], a:1},
 {q:'「披衣觉露滋」与「还寝梦佳期」中「觉」「还」的读音，正确的是？', o:['jiào、hái','jué、huán','jué、hái'], a:1},
 {q:'张九龄是开元盛世的最后一位贤相，此诗多认为作于他遭谗罢相、贬为荆州长史之后。诗题「望月怀远」的「怀远」指？', o:['怀念远方的亲人','追怀远古的圣人','胸怀远大的志向'], a:0},
 {q:'结尾「不堪盈手赠，还寝梦佳期」寄托的主旨是？', o:['月色虽美却无可奈何的扫兴','月光无法盈手相赠，唯愿梦中相会的深挚思念','夜露湿衣、意兴阑珊的孤寂'], a:1},
];
"""

SCENES_JS = """/* ================= 望月怀远 · 四境场景（水墨夜思：海月天涯、遥夜相思、灭烛披衣、盈手佳期） ================= */

/* 望月人：全诗贯穿的同一造型（每次 build 新建材质） */
function wmFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x1e2736,belt:0x51607a,skin:0xcbb9a2,collar:0xb9c6d8,
    hair:0x10141c,hat:'发髻',rimC:0x9fb3cc,rim:0.5,noProp:true,scale:scale===undefined?1.7:scale});
}

/* 石台：台基 + 台面 + 台缘（合批 1 mesh，水墨剪影） */
function makeShitai(o){
  o=o||{};
  const B=new GeoBag(), c1=0x0a0e16, c2=0x101723, c3=0x161d2b;
  const w=o.w===undefined?14:o.w, d=o.d===undefined?8:o.d;
  const base=new THREE.BoxGeometry(w+4.5,0.9,d+3.4); base.translate(0,0.45,0); B.put(base,c1);
  const top=new THREE.BoxGeometry(w,0.5,d); top.translate(0,1.15,0); B.put(top,c2);
  const edge=new THREE.BoxGeometry(w+0.3,0.14,d+0.3); edge.translate(0,1.42,0); B.put(edge,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x39465c,emissive:0x05070c}),{c:0x9fb3cc,i:0.3,p:2.5})));
  return g;
}

/* 海中礁石：压扁岩石一丛（合批 1 mesh，供望月人立足） */
function makeJiaoshi(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?214:o.seed);
  const n=o.n===undefined?4:o.n, r0=o.r===undefined?3.2:o.r;
  for(let i=0;i<n;i++){
    const rg=rockGeo(r0*(0.5+0.8*R()),1,R);
    rg.scale(1,0.55+0.35*R(),1);
    rg.translate((R()-0.5)*(o.w===undefined?7:o.w),R()*0.35-0.2,(R()-0.5)*(o.d===undefined?4:o.d));
    B.put(rg,shadeColor(0x0a0e16,0.8+0.5*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:o.rimC===undefined?0x8fa4c4:o.rimC,i:0.2,p:2.4})));
  return g;
}

/* 白烛：烛座 + 白烛身 + 烛芯（合批 1 mesh；火苗外挂） */
function makeCandle(){
  const B=new GeoBag();
  const foot=new THREE.CylinderGeometry(0.42,0.50,0.10,12); foot.translate(0,0.05,0); B.put(foot,0x2a303e);
  const stem=new THREE.CylinderGeometry(0.05,0.07,0.62,8); stem.translate(0,0.38,0); B.put(stem,0x323a4a);
  const pan=new THREE.CylinderGeometry(0.30,0.24,0.06,12); pan.translate(0,0.72,0); B.put(pan,0x2a303e);
  const body=new THREE.CylinderGeometry(0.085,0.085,0.50,10); body.translate(0,1.00,0); B.put(body,0xd8dee8);
  const cap=new THREE.CylinderGeometry(0.082,0.085,0.05,10); cap.translate(0,1.26,0); B.put(cap,0x9aa6ba);
  const wick=new THREE.CylinderGeometry(0.012,0.016,0.09,5); wick.translate(0,1.32,0); B.put(wick,0x1a1410);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x3a465c,emissive:0x05070c}),{c:0x9fb3cc,i:0.3,p:2.5})));
  return g;
}

/* 两地对望光带：贴水长带（自写着色器；additive 不进 fogShaders，uFade 每帧显式写） */
const LP_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const LP_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float cr=smoothstep(0.0,0.32,vUv.y)*smoothstep(1.0,0.68,vUv.y);
  float ln=smoothstep(0.0,0.14,vUv.x)*smoothstep(1.0,0.86,vUv.x);
  float rip=0.72+0.28*sin(uTime*1.6+vUv.x*24.0);
  float rip2=0.86+0.14*sin(uTime*3.3+vUv.x*57.0);
  vec3 col=mix(vec3(0.58,0.68,0.86),vec3(0.88,0.93,1.0),cr);
  gl_FragColor=vec4(col,uFade*uK*cr*ln*rip*rip2);
}`;

function bCover(){ // 封面 · 海天未月
  const g=new THREE.Group();
  /* 本诗全篇海天：常驻远山整体下沉为低缓远丘，让出海平线给月出（引擎全局，boot 后一次性调整） */
  if(typeof bgRange!=='undefined'&&bgRange&&bgRange.g)bgRange.g.position.y=-55;
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:2140,color:0x070a10,atmo:0x1f2a3d,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:2141,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const mist=makeMist({n:9,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x8fa4c4,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[220,40,130],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.36});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bHaiyue(){ // 一（标志性瞬间）· 海月天涯 —— 海上生明月，天涯共此时：一轮月照两头
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:96,amp:0.55,freq:0.085,speed:0.72,flow:[0.05,0.65],spec:1.5,
    deep:0x081426,shallow:0x16324e,skyc:0x1f3a58,moonDir:[0,26,-200]});
  g.add(water.mesh);
  const ridge=makeRange({r:280,h:12,layers:2,peaks:5,seed:2142,color:0x070a10,atmo:0x1f2a3d,fogK:0.60,glowK:0.05,y:-4});
  ridge.g.position.set(0,0,30); g.add(ridge.g);
  /* 两岸墨山（天涯之远，退居两侧），中留海门让月涌出 */
  const bankL=makeRange({r:200,h:20,layers:2,peaks:3,seed:2143,arc:Math.PI*0.36,a0:-Math.PI*0.93,
    color:0x070a10,atmo:0x27334a,fogK:0.62,glowK:0.07,y:-16});
  bankL.g.position.set(-46,0,-20); g.add(bankL.g);
  const bankR=makeRange({r:210,h:18,layers:2,peaks:3,seed:2144,arc:Math.PI*0.36,a0:Math.PI*0.57,
    color:0x070a10,atmo:0x27334a,fogK:0.62,glowK:0.07,y:-16});
  bankR.g.position.set(48,0,-22); g.add(bankR.g);
  /* 明月：自建月，入场后自海面缓缓升起（引擎月在本境藏于地下） */
  const moon=makeMoon({r:15,phase:0,haze:0.05,base:0xeef3ff,dark:0x2b3552,hazeColor:0xaebfd8});
  moon.group.position.set(0,16,-150); g.add(moon.group);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaebfd8,
    transparent:true,opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(34,34,1); halo.position.set(0,16,-149); halo.renderOrder=2; g.add(halo);
  /* 望月人：近岸礁石上，背身望海（此端） */
  const rock=makeJiaoshi({n:5,r:2.6,seed:2145}); rock.position.set(6.5,-0.7,-2); g.add(rock);
  const poet=wmFigure(2.0,'独立'); poet.position.set(6.5,-0.35,-2); poet.rotation.y=2.94; g.add(poet);
  /* 天涯彼端：远渚上一个遥望的小影（共此时） */
  const shoal=makeJiaoshi({n:3,r:2.0,seed:2146}); shoal.position.set(-32,-0.9,-62); g.add(shoal);
  const far=makeCrowd({n:1,rect:[-33,-63,2.5,2.5],seed:2147,color:0x11161f,rimC:0x8fa4c4,
    rim:0.2,sMin:0.6,sMax:0.66,y:0.1});
  g.add(far.mesh);
  /* 月华微尘 + 银浪沫 + 海雾 */
  const motes=makeGlow({n:70,box:[120,26,80],pos:[0,12,-30],color:0xcdd8e6,size:4.5,speed:0.04,rise:0,maxA:0.26});
  g.add(motes.points);
  const foam=makeGlow({n:160,box:[110,4,50],pos:[2,0.2,-24],color:0xbfd2e4,size:8,speed:0.4,rise:1,maxA:0.22});
  g.add(foam.points);
  const mist=makeMist({n:6,spread:[230,20,110],pos:[0,8,-60],scale:80,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.4,w:20,d:7,color:0x04060a,seed:2148,rim:0.14});
  fg1.g.position.set(-14,-1.6,14); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:2149,sway:0.8});
  reeds.g.position.set(14,-1.4,12); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[0,80,-60]},{c:0x1a2232,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    const rise=Math.min(1,t/26);
    moon.group.position.y=16+10*rise;
    moon.update(t);
    halo.position.y=moon.group.position.y;
    halo.material.opacity=k*(0.30-0.06*rise);
    const md=water.mesh.material.uniforms.uMoonDir.value;
    md.set(0,moon.group.position.y,-150).normalize();
    ridge.update(t,0); bankL.update(t,0); bankR.update(t,0); water.update(t);
    motes.update(t); foam.update(t); mist.update(t,k);
    fg1.update(t,k); reeds.update(t,k); poet.update(t,k); far.update(t);
  }};
}

function bYaoye(){ // 二 · 遥夜相思 —— 长夜流云、露光初凝（静，怨夜之长）
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x07090e,c2:0x0e131c});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:300,h:24,layers:3,peaks:4,seed:2150,color:0x070a10,atmo:0x1f2a3d,fogK:0.58,glowK:0.04,y:-20});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 石台 + 望月人（指月，面朝天心孤月） */
  const terrace=makeShitai({w:13,d:8}); terrace.position.set(0,-0.3,-4); g.add(terrace);
  const poet=wmFigure(1.7,'指月'); poet.position.set(1.0,1.1,-5.2); poet.rotation.y=2.87; g.add(poet);
  /* 长夜流云（高天横流，极慢） */
  const cloud=makeFlow({n:150,box:[170,18,60],pos:[0,46,-80],color:0x8fa0b8,size:30,speed:1.4,maxA:0.16});
  g.add(cloud.points);
  /* 露光初凝：贴地霜晶微闪 */
  const dew=makeGlow({n:60,box:[70,4,40],pos:[0,1.2,-10],color:0xcdd8e6,size:3.6,speed:0.03,rise:0,maxA:0.24});
  g.add(dew.points);
  const mist=makeMist({n:6,spread:[220,24,110],pos:[0,6,-56],scale:76,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:2151,sway:1.1,rim:0.18});
  tree.g.position.set(13,-0.6,9); g.add(tree.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.2,w:18,d:6,color:0x04060a,seed:2152,rim:0.14});
  fg1.g.position.set(-13,-1.2,10); g.add(fg1.g);
  addLights(g,{c:0x8fa4c8,i:0.46,p:[-24,86,-40]},{c:0x19202e,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); cloud.update(t); dew.update(t); mist.update(t,k);
    tree.update(t,k); fg1.update(t,k); poet.update(t,k);
  }};
}

function bMiezhu(){ // 三 · 灭烛披衣 —— 时序小戏：烛灭 → 月光满室 → 披衣出户、露湿衣裳
  const g=new THREE.Group();
  const ctl={t:0};
  const grd=makeGround({r:120,c1:0x08090e,c2:0x10131b});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:280,h:20,layers:2,peaks:3,seed:2153,color:0x070a10,atmo:0x1f2a3d,fogK:0.56,glowK:0.04,y:-18});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  const terrace=makeShitai({w:15,d:9}); g.add(terrace);
  /* 开敞的水阁：两根冷银柱 + 一方矮案（柱自建，避免暖色 rim） */
  const zhuB=new GeoBag();
  [[-6.4,-3.6],[6.4,-3.6]].forEach(function(p){
    const zb=new THREE.BoxGeometry(0.9,0.35,0.9); zb.translate(p[0],1.4+0.17,p[1]); zhuB.put(zb,0x0c1018);
    const zc=new THREE.CylinderGeometry(0.18,0.20,5.6,10); zc.translate(p[0],1.4+0.35+2.8,p[1]); zhuB.put(zc,0x131a26);
  });
  g.add(zhuB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x9fb3cc,i:0.3,p:2.5})));
  const table=makeTable({w:3.4,d:1.7,h:0.95,wood:0x1a1410}); table.g.position.set(2.6,1.2,-2.2); g.add(table.g);
  /* 白烛一支（入场的唯一暖色）——随时间熄灭，月光满室 */
  const candle=makeCandle(); candle.position.set(2.4,2.15,-2.2); g.add(candle);
  const flame=makeFlame({h:0.44,w:0.14,planes:2,embers:5,esize:3.5,spark:false,wide:0.24,
    core:0xffe0a8,outer:0xff8a30});
  flame.g.position.set(2.4,3.48,-2.2); g.add(flame.g);
  const candL=new THREE.PointLight(0xffb070,1.5,26); candL.position.set(2.4,3.9,-2.2); g.add(candL);
  /* 月光满室：地面光池（烛灭后渐亮）+ 满室月尘 */
  const pool=new THREE.Mesh(new THREE.PlaneGeometry(15,9),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0xbcd2e8,transparent:true,opacity:0.40,
      depthWrite:false,blending:THREE.AdditiveBlending}));
  pool.rotation.x=-Math.PI/2; pool.position.set(-1,1.24,-4); pool.renderOrder=2; g.add(pool);
  const motes=makeGlow({n:56,box:[26,9,18],pos:[0,4.5,-6],color:0xcdd8e6,size:4,speed:0.035,rise:0,maxA:0.26});
  g.add(motes.points);
  /* 披衣人：立于台沿，面向户外月色 */
  const poet=wmFigure(1.7,'独立'); poet.position.set(-2.2,1.42,-6.0); poet.rotation.y=3.46; g.add(poet);
  const dew=makeGlow({n:40,box:[34,3,20],pos:[0,1.8,-8],color:0xcdd8e6,size:3.2,speed:0.03,rise:0,maxA:0.22});
  g.add(dew.points);
  const mist=makeMist({n:5,spread:[200,22,100],pos:[0,6,-52],scale:72,color:0x7e8ea8,op:0.07});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.0,w:16,d:6,color:0x04060a,seed:2162,rim:0.14});
  fg1.g.position.set(-12,-1.0,10); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:20,n:9,d:5,color:0x04060a,seed:2163,sway:0.7});
  reeds.g.position.set(13,-0.9,9); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[-30,80,-40]},{c:0x1a2232,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const die=clamp((ctl.t-2.8)/2.4,0,1);
      flame.g.scale.set(1,Math.max(0.04,1-0.96*die),1);
      flame.g.visible=die<0.995;
      candL.intensity=k*1.5*(1-die)*(0.85+0.15*Math.sin(t*9.3));
      pool.material.opacity=k*(0.12+0.28*die);
      ridge.update(t,0); flame.update(t,k); motes.update(t); dew.update(t); mist.update(t,k);
      fg1.update(t,k); reeds.update(t,k); poet.update(t,k);
    }};
}

function bMengjia(){ // 四（末境可点击）· 盈手佳期 —— 点击明月：月轮满升 + 两地对望光带相连
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0};
  const water=makeWater({size:640,seg:96,amp:0.8,freq:0.08,speed:0.9,flow:[0.05,0.8],spec:1.5,
    deep:0x081426,shallow:0x153049,skyc:0x1d3854,moonDir:[0,10,-150]});
  g.add(water.mesh);
  const ridge=makeRange({r:290,h:12,layers:2,peaks:4,seed:2154,color:0x070a10,atmo:0x1f2a3d,fogK:0.60,glowK:0.05,y:-4});
  ridge.g.position.set(0,0,30); g.add(ridge.g);
  const bankL=makeRange({r:200,h:18,layers:2,peaks:3,seed:2155,arc:Math.PI*0.36,a0:-Math.PI*0.93,
    color:0x070a10,atmo:0x27334a,fogK:0.62,glowK:0.06,y:-16});
  bankL.g.position.set(-46,0,-24); g.add(bankL.g);
  const bankR=makeRange({r:210,h:16,layers:2,peaks:3,seed:2156,arc:Math.PI*0.36,a0:Math.PI*0.57,
    color:0x070a10,atmo:0x27334a,fogK:0.62,glowK:0.06,y:-16});
  bankR.g.position.set(48,0,-26); g.add(bankR.g);
  /* 明月：自建月（初始半出海面，点击后满升；引擎月在本境藏于地下） */
  const moon=makeMoon({r:15,phase:0,haze:0.05,base:0xeef3ff,dark:0x2b3552,hazeColor:0xaebfd8});
  moon.group.position.set(0,10,-150); g.add(moon.group);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaebfd8,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(30,30,1); halo.position.set(0,10,-149); halo.renderOrder=2; g.add(halo);
  /* 两地对望光带（点击后相连）：自望月人伸向天涯彼端 */
  const pathMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.05}},
    vertexShader:LP_VERT,fragmentShader:LP_FRAG});
  const pathGeo=new THREE.PlaneGeometry(72,7); pathGeo.rotateX(-Math.PI/2);
  const path=new THREE.Mesh(pathGeo,pathMat);
  path.position.set(-12.2,0.45,-33);
  path.rotation.y=Math.atan2(58,-39.5);
  path.renderOrder=2; g.add(path);
  /* 望月人（此端）+ 天涯彼端的小影 */
  const rock=makeJiaoshi({n:5,r:2.6,seed:2157}); rock.position.set(7.5,-0.7,-4); g.add(rock);
  const poet=wmFigure(2.0,'独立'); poet.position.set(7.5,-0.35,-4); poet.rotation.y=3.2; g.add(poet);
  const shoal=makeJiaoshi({n:3,r:2.0,seed:2158}); shoal.position.set(-32,-0.9,-62); g.add(shoal);
  const far=makeCrowd({n:1,rect:[-33,-63,2.5,2.5],seed:2159,color:0x11161f,rimC:0x8fa4c4,
    rim:0.2,sMin:0.6,sMax:0.66,y:0.1});
  g.add(far.mesh);
  /* 月华微尘 + 海雾 */
  const motes=makeGlow({n:64,box:[130,28,84],pos:[0,12,-34],color:0xcdd8e6,size:4.5,speed:0.04,rise:0,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[240,20,110],pos:[0,8,-62],scale:82,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.4,w:20,d:7,color:0x04060a,seed:2160,rim:0.14});
  fg1.g.position.set(-15,-1.6,13); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:2161,sway:0.9});
  reeds.g.position.set(14,-1.4,12); g.add(reeds.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[0,80,-60]},{c:0x1a2232,i:0.62});
  const pl=new THREE.PointLight(0x9fb8d4,1.4,90); pl.position.set(0,10,-60); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/4.2);
      const rv=ctl.reveal, up=rv*rv*(3-2*rv);
      moon.group.position.y=10+49*up;
      moon.group.scale.setScalar(1+0.30*up);
      moon.update(t);
      halo.position.y=moon.group.position.y;
      halo.material.opacity=k*(0.18+0.32*up);
      halo.scale.set(30*(1+0.30*up),30*(1+0.30*up),1);
      const md=water.mesh.material.uniforms.uMoonDir.value;
      md.set(0,moon.group.position.y,-150).normalize();
      pathMat.uniforms.uTime.value=t;
      pathMat.uniforms.uFade.value=k;
      pathMat.uniforms.uK.value=0.05+0.95*up;
      ridge.update(t,0); bankL.update(t,0); bankR.update(t,0); water.update(t);
      motes.update(t); mist.update(t,k);
      fg1.update(t,k); reeds.update(t,k); poet.update(t,k); far.update(t);
      pl.intensity=k*1.4*(0.30+0.70*up*(0.85+0.15*Math.sin(t*1.9)));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(3,0.05,0.13); pluck(1,0.5,0.11); pluck(4,1.0,0.10);
        const fl=$('#flash'); fl.textContent='梦佳期'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0055,star:0.42,
  moon:new THREE.Vector3(0,44,-190),ms:1.7,mph:0,mhaze:0.05,dirC:C(0x8fa4c8),dirI:0.42,
  dirP:new THREE.Vector3(0,80,-60),ambC:C(0x1a2232),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,62],t:[0,9.5,58],lf:[0,13,-40],lt:[0,13.5,-44]},
  sky:()=>SK({top:C(0x060910),hor:C(0x141c2a),bot:C(0x080b11),fog:C(0x0f1520),fd:0.0050,star:0.40,
    ms:1.7,moon:new THREE.Vector3(0,44,-190),
    dirC:C(0x8fa4c8),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'海月天涯',dwell:16,river:0.05,build:bHaiyue,
  cam:{f:[0,7,32],t:[-0.5,7.4,29],lf:[0,16,-150],lt:[0,17,-160]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0055,star:0.45,
    ms:0.001,moon:new THREE.Vector3(0,-80,-190),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
{ name:'遥夜相思',dwell:16,river:0.015,build:bYaoye,
  cam:{f:[0,6.5,24],t:[-1,6.2,21],lf:[-2,9,-14],lt:[-1.4,8.6,-18]},
  sky:()=>SK({top:C(0x060a10),hor:C(0x161e2c),bot:C(0x080b11),fog:C(0x101722),fd:0.0062,star:0.34,
    ms:1.85,mph:0,mhaze:0.05,moon:new THREE.Vector3(-26,92,-190),
    dirC:C(0x879ab4),dirI:0.46,ambC:C(0x19202e),ambI:0.64}) },
{ name:'灭烛披衣',dwell:17,river:0.012,build:bMiezhu,
  cam:{f:[0,5.5,17],t:[0.6,5.2,14.5],lf:[0,4.5,-12],lt:[1,4.2,-14]},
  sky:()=>SK({top:C(0x06090f),hor:C(0x141b28),bot:C(0x080a10),fog:C(0x0f151f),fd:0.0066,star:0.26,
    ms:1.55,mph:0.06,mhaze:0.05,moon:new THREE.Vector3(-56,74,-170),
    dirC:C(0x8296b0),dirI:0.40,ambC:C(0x1a2230),ambI:0.66}) },
{ name:'盈手佳期',dwell:18,river:0.04,build:bMengjia,
  cam:{f:[0,7.5,30],t:[0,7.8,27],lf:[0,12,-120],lt:[1.5,13,-130]},
  sky:()=>SK({top:C(0x070b12),hor:C(0x171f2e),bot:C(0x090d13),fog:C(0x111826),fd:0.0058,star:0.40,
    ms:0.001,moon:new THREE.Vector3(0,-80,-190),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
];
"""
