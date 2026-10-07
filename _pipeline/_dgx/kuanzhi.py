# -*- coding: utf-8 -*-
"""kuanzhi.py —— 《客至》（唐·杜甫，no.207，青绿春晓·浣花溪人家）生成配置
四境（七律四联各一境）：
  壹 春水群鸥（首联·舍南舍北春水绕，群鸥日日自来——草堂临水清景）
  贰 花径蓬门（颔联·标志性瞬间：花径不扫、蓬门为君开——草堂蓬门+春水群鸥的花溪人家）
  叁 樽酒盘飧（颈联·市远无兼味、家贫只旧醅——家常小宴，贵在真心）
  肆 隔篱呼邻（尾联·末境点击蓬门：柴门初开+隔篱呼邻的酒盏相碰）"""

META = dict(
    N=4, slug='kuanzhi', title='客至', dyn='唐 · 杜甫', brand_author='杜 甫',
    gold_rgb='163,201,143',
    residual=('将进酒', '万古愁', '太白', '李白'),
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
    tip='轻点画面 / 按空格 —— 柴门初开，隔篱呼邻，酒盏相碰',
    hint='← → 键或空格逐境游览 · 末境可点击蓬门，看柴门初开、隔篱呼邻碰杯',
    cover_read='客至。唐，杜甫。舍南舍北皆春水，但见群鸥日日来。花径不曾缘客扫，蓬门今始为君开。',
    cover_p1='四重意境，随诗句次第展开：舍南舍北春水漫绕，只见群鸥日日飞来；花径不曾为客打扫，蓬门今天才为您打开；市远盘简、家贫酒薄，却是真心实意；兴致到处，隔着篱笆唤邻翁过来，一同尽这余下的酒杯。',
    cover_p2='边读诗，边走进杜甫成都草堂那个春水绕舍、宾主尽欢的花溪人家。',
    end_h2='杯尽 · 情长', cn_word='四',
    words_js="['再访一次草堂','初识少陵，尚需共读','渐入佳境，再诵几遍','诗境渐深，宾主意浓','已解待客之喜','春水群鸥，蓬门杯尽情长']",
    sky_atmo='0x2c4434',
)

POEM_JS = """const POEM = [
{ name:'春水群鸥', jing:'舍南舍北，春水漫漫；群鸥点点，日日自来。（春水 · 群鸥）',
  segs:[
   {c:'舍南舍北皆春水，', p:py('shè nán shè běi jiē chūn shuǐ')},
   {c:'但见群鸥日日来。', p:py('dàn jiàn qún ōu rì rì lái')}],
  read:'舍南舍北皆春水，但见群鸥日日来。',
  yisi:'草堂的南北，处处春水漫漫；只见一群群鸥鸟，日日翩翩飞来。——一个「皆」字写尽春水盛涨、绿水绕舍的清景；鸥鸟天天来做客，既见浣花溪畔的清幽闲适，也隐隐透出平日无人登门的寂静，为「客至」暗暗伏笔。',
  zhu:[['舍（shè）','居宅，指成都浣花溪畔的杜甫草堂。「舍南舍北」即草堂前后、四野皆水'],['皆春水','春天雨水潮涨，草堂南北都是环绕的春水——绿水绕舍的湿润春景'],['但见','只见。但：只，仅仅'],['群鸥','水鸟，常翔集于江湖水滨。古人以鸥鸟为忘机之伴，借以写闲适之趣'],['日日来','天天飞来——既见环境清幽，也见门庭寂寂，惟有鸥鸟为邻']] },
{ name:'花径蓬门', jing:'花径不扫，蓬门初开 —— 柴门为君而开，是全诗最暖的一瞬。（花径 · 蓬门）',
  segs:[
   {c:'花径不曾缘客扫，', p:py('huā jìng bù céng yuán kè sǎo')},
   {c:'蓬门今始为君开。', p:py('péng mén jīn shǐ wèi jūn kāi')}],
  read:'花径不曾缘客扫，蓬门今始为君开。',
  yisi:'长满花草的小路，还不曾为迎客打扫；今天这扇蓬门，才头一回为您打开。——正因平日少客，才说「不曾缘客扫」；正因嘉客今至，才说「今始为君开」。两句互相映衬，把主人不事虚礼、真心喜客的欢欣写得亲切之至，是全诗最暖的一瞬。',
  zhu:[['花径','长满花草的庭院小路'],['缘客扫','为了客人而打扫。缘：因为、为了——不说「不曾扫」，而说「不曾为客扫」，客气里全是实心'],['蓬门','蓬草编成的门，指贫寒人家的柴门。草堂清贫，门是蓬柴所编'],['今始','今天才。始：才，第一次'],['为君开','为您打开。为：为了，读 wèi；君：指崔明府']] },
{ name:'樽酒盘飧', jing:'盘飧无兼味，樽酒只旧醅 —— 家常小宴，贵在真心。（盘飧 · 旧醅）',
  segs:[
   {c:'盘飧市远无兼味，', p:py('pán sūn shì yuǎn wú jiān wèi')},
   {c:'樽酒家贫只旧醅。', p:py('zūn jiǔ jiā pín zhǐ jiù pēi')}],
  read:'盘飧市远无兼味，樽酒家贫只旧醅。',
  yisi:'离集市太远，盘中的菜肴没有第二种美味；家境贫寒，杯里只有隔年的自酿浊酒。——「无兼味」「只旧醅」是待客从简的实情，也是主人的自谦：菜虽简、酒虽薄，情意却厚。家常话语娓娓道来，宾主间不分彼此的亲切融洽，全在其中。',
  zhu:[['盘飧（sūn）','盘中的熟食，泛指菜肴'],['市远','远离集市，买菜不便——所以菜肴简单'],['兼味','两种以上的美味，指菜肴丰盛。无兼味：待客菲薄的自谦之辞'],['樽','盛酒的器具，此处代指酒'],['旧醅（pēi）','隔年未经过滤的浊酒。醅：未滤的酒。酒不清醇，见出主人家的清贫，也见出待客的实在']] },
{ name:'隔篱呼邻', jing:'肯与邻翁相对饮，隔篱呼取尽余杯。（呼邻 · 尽杯）（点击画面：柴门初开，隔篱呼邻，酒盏相碰）',
  segs:[
   {c:'肯与邻翁相对饮，', p:py('kěn yǔ lín wēng xiāng duì yǐn')},
   {c:'隔篱呼取尽余杯。', p:py('gé lí hū qǔ jìn yú bēi')}],
  read:'肯与邻翁相对饮，隔篱呼取尽余杯。',
  yisi:'客人若是愿意和邻家老翁一同对饮，我就隔着篱笆高声唤他过来，一起喝尽这剩下的几杯。——不必事先相约，随兴唤邻；宾主的欢快，又延展到邻里之间。真率自然，毫无俗套，全诗就在这一声隔篱相唤、满饮余杯的喧笑里收束，人情之美尽在不言中。',
  zhu:[['肯','若是愿意。一说为征询之辞：可肯与邻翁同饮吗'],['邻翁','邻家的老翁'],['相对饮','面对面一起喝酒'],['隔篱呼取','隔着篱笆呼唤他过来。呼取：呼唤；取：语助词，无实义'],['尽余杯','喝干杯中余酒。余杯：剩下的酒——尽兴之至，豪爽之至']] },
];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「舍南舍北皆春水」的下一句是？', o:['但见群鸥日日来','花径不曾缘客扫','蓬门今始为君开'], a:0},
 {q:'「盘飧市远无兼味」的下一句是？', o:['肯与邻翁相对饮','樽酒家贫只旧醅','隔篱呼取尽余杯'], a:1},
 {q:'「盘飧市远无兼味」的「飧」与「樽酒家贫只旧醅」的「醅」，注音全都正确的是？', o:['飧 cān、醅 pēi','飧 sūn、醅 péi','飧 sūn、醅 pēi'], a:2},
 {q:'与「黄四娘家花满蹊」同作于成都浣花溪畔，这首诗题下自注「喜崔明府相过」，其中「明府」是对什么人的尊称？', o:['县令','太守','员外郎'], a:0},
 {q:'这首诗最打动人的是？', o:['壮志难酬的愤懑不平','远离尘嚣的孤寂冷清','宾主之欢、邻里之谊的人情味'], a:2},
];
"""

SCENES_JS = """/* ================= 客至 · 四境场景（青绿春晓·浣花溪人家：春水群鸥、花径蓬门、樽酒盘飧、隔篱呼邻）
   本诗专属系统「蓬门柴扉」：花径两侧篱笆、交叉枝条柴门（带小草檐），末境点击——
   柴门呀然内开，邻翁举杯穿门而入，隔篱相唤的酒盏在门边相碰迸出暖光 ================= */

/* —— 群鸥：白翅水鸟绕舍盘旋（每只 2 面片拍翅，合 1 材质） —— */
function makeGullsKZ(o){
  o=o||{};
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0xdce6d8:o.color,side:THREE.DoubleSide});
  const g=new THREE.Group(), items=[];
  const n=o.n===undefined?5:o.n;
  for(let i=0;i<n;i++){
    const b=new THREE.Group();
    const w1=new THREE.Mesh(new THREE.PlaneGeometry(1.9,0.55),mat); w1.position.x=-0.9;
    const w2=new THREE.Mesh(new THREE.PlaneGeometry(1.9,0.55),mat); w2.position.x=0.9;
    b.add(w1,w2); g.add(b);
    items.push({b,w1,w2,cx:o.cx===undefined?4:o.cx,cz:o.cz===undefined?-22:o.cz,
      r:(o.r===undefined?8:o.r)*(0.6+Math.random()*0.8),
      y:(o.y===undefined?7:o.y)+Math.random()*3.5,
      sp:(o.sp===undefined?0.2:o.sp)*(0.75+Math.random()*0.5),
      ph:Math.random()*6.283,sc:(o.scMin===undefined?0.55:o.scMin)+Math.random()*0.65});
  }
  const api={g,update(t){
    for(const it of items){
      const a=it.ph+t*it.sp;
      it.b.position.set(it.cx+Math.sin(a)*it.r,it.y+Math.sin(t*0.9+it.ph)*1.1,it.cz+Math.cos(a)*it.r*0.62);
      it.b.rotation.y=-a+Math.PI/2;
      it.b.scale.setScalar(it.sc);
      const f=Math.sin(t*6.5+it.ph)*0.55; it.w1.rotation.z=f; it.w2.rotation.z=-f;
    }
  }};
  return api;
}

/* —— 花瓣：粉白小片缓落（Points 自定义着色器，显式双 shader + uFade） —— */
const KZ_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uH; uniform float uB; uniform float uFall; uniform float uSway;
varying float vA; varying float vS;
void main(){
  vec3 p=position;
  float sp=uFall*(0.7+aSeed*0.6);
  float y=mod(p.y-uB+uTime*sp,uH);
  p.y=uB+uH-y;
  p.x+=sin(uTime*0.8+aSeed*87.0)*uSway;
  p.z+=cos(uTime*0.6+aSeed*51.0)*uSway*0.6;
  vA=smoothstep(0.0,uH*0.06,y)*(1.0-smoothstep(uH*0.88,uH,y));
  vS=aSeed;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=min(aSize*(150.0/max(1.0,-mv.z)),13.0);
  gl_Position=projectionMatrix*mv;
}`;
const KZ_PETAL_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA; varying float vS;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=abs(q.x)*0.72+abs(q.y)*0.72+0.4*q.x*q.y;
  float a=smoothstep(0.5,0.16,d)*vA*uFade*uMaxA*(0.72+0.28*vS);
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makePetalsKZ(o){
  const d=Object.assign({n:70,box:[90,22,60],pos:[0,3,-14],fall:0.75,sway:1.6,
    size:7,maxA:0.34,c:0xf0d4d4},o);
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(d.n*3),S=new Float32Array(d.n),Z=new Float32Array(d.n);
  for(let i=0;i<d.n;i++){
    P[i*3]=d.pos[0]+(Math.random()-0.5)*d.box[0];
    P[i*3+1]=d.pos[1]+Math.random()*d.box[1];
    P[i*3+2]=d.pos[2]+(Math.random()-0.5)*d.box[2];
    S[i]=Math.random(); Z[i]=d.size*(0.6+Math.random()*0.8);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uFall:{value:d.fall},uH:{value:d.box[1]},uB:{value:d.pos[1]},
      uSway:{value:d.sway},uC:{value:C(d.c)},uFade:{value:0},uMaxA:{value:d.maxA}},
    vertexShader:KZ_PETAL_VERT,fragmentShader:KZ_PETAL_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 草堂：土墙茅顶（双层茅草坡+屋脊+暖窗），合批 1 mesh —— */
function makeThatchKZ(o){
  o=o||{};
  const w=o.w===undefined?7:o.w, d=o.d===undefined?5.2:o.d, h=o.h===undefined?2.9:o.h;
  const wall=o.wall===undefined?0x302a1c:o.wall, thatch=o.thatch===undefined?0x6a5626:o.thatch;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h/2,0); B.put(body,wall);
  const eave=new THREE.BoxGeometry(w+1.1,0.16,d+1.1); eave.translate(0,h-0.04,0);
  B.put(eave,shadeColor(0x4a3a20,1.05));
  const door=new THREE.BoxGeometry(1.3,2.1,0.12); door.translate(-0.6,1.05,d/2+0.06); B.put(door,0x120e08);
  if(o.window!==false){
    const win=new THREE.BoxGeometry(1.0,0.9,0.10); win.translate(w*0.28,h*0.60,d/2+0.05);
    B.put(win,shadeColor(0xd8a850,0.55));
  }
  const rh=o.rh===undefined?1.9:o.rh;
  const r1=new THREE.ConeGeometry(1,rh,4); r1.rotateY(Math.PI/4);
  r1.scale((w+1.8)/1.414,1,(d+1.6)/1.414); r1.translate(0,h+rh/2+0.06,0); B.put(r1,thatch);
  const r2=new THREE.ConeGeometry(1,rh*0.58,4); r2.rotateY(Math.PI/4);
  r2.scale((w+1.8)*0.66/1.414,1,(d+1.6)*0.66/1.414); r2.translate(0,h+rh*0.80,0);
  B.put(r2,shadeColor(thatch,1.24));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a4430,emissive:0x0a0d06}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.24:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 篱笆：一排细桩 + 双横杆（合批 1 mesh） —— */
function makeFenceKZ(o){
  o=o||{};
  const w=o.w===undefined?10:o.w, h=o.h===undefined?1.35:o.h, R=seedRnd(o.seed===undefined?11:o.seed);
  const n=Math.max(3,Math.round(w/0.62)), wood=o.wood===undefined?0x3c2f1c:o.wood;
  const B=new GeoBag();
  for(let i=0;i<=n;i++){
    const x=-w/2+w*i/n;
    const p=new THREE.BoxGeometry(0.10,h*(0.82+R()*0.30),0.10);
    p.rotateZ((R()-0.5)*0.10); p.translate(x,h*0.45,(R()-0.5)*0.1);
    B.put(p,shadeColor(wood,0.85+R()*0.35));
  }
  const r1=new THREE.BoxGeometry(w,0.09,0.07); r1.translate(0,h*0.74,0); B.put(r1,shadeColor(wood,1.15));
  const r2=new THREE.BoxGeometry(w,0.08,0.07); r2.translate(0,h*0.32,0); B.put(r2,shadeColor(wood,0.95));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x33301e,emissive:0x0a0906}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.16:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 蓬门（柴门）：双柱+顶枋+小草檐，扉为交叉枝条、铰在左柱可开（末境交互主角） —— */
function makeGateKZ(o){
  o=o||{};
  const w=o.w===undefined?2.3:o.w, h=o.h===undefined?2.15:o.h;
  const wood=o.wood===undefined?0x4a3820:o.wood, thatch=o.thatch===undefined?0x5c4a20:o.thatch;
  const rm={c:o.rimC===undefined?0xb8cc90:o.rimC,i:o.rim===undefined?0.26:o.rim,p:2.4};
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const post=new THREE.BoxGeometry(0.16,h+0.55,0.16); post.translate(s*w/2,(h+0.55)/2,0);
    B.put(post,shadeColor(wood,1.12));
  });
  const beam=new THREE.BoxGeometry(w+0.55,0.14,0.20); beam.translate(0,h+0.46,0); B.put(beam,shadeColor(wood,1.26));
  const cap=new THREE.ConeGeometry(1,0.55,4); cap.rotateY(Math.PI/4);
  cap.scale((w+1.4)/1.414,1,1.05/1.414); cap.translate(0,h+0.46+0.30,0); B.put(cap,thatch);
  const meshF=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a3424,emissive:0x0a0805}),rm));
  const L=new GeoBag(), Lw=w-0.1, Lh=h-0.2;
  const st1=new THREE.BoxGeometry(0.09,Lh,0.06); st1.translate(0.05,Lh/2+0.12,0); L.put(st1,shadeColor(wood,1.0));
  const st2=new THREE.BoxGeometry(0.09,Lh,0.06); st2.translate(Lw-0.05,Lh/2+0.12,0); L.put(st2,shadeColor(wood,1.0));
  const rl1=new THREE.BoxGeometry(Lw,0.09,0.06); rl1.translate(Lw/2,h-0.28,0); L.put(rl1,shadeColor(wood,0.95));
  const rl2=new THREE.BoxGeometry(Lw,0.08,0.06); rl2.translate(Lw/2,0.34,0); L.put(rl2,shadeColor(wood,0.9));
  const dg=Math.hypot(Lw,Lh-0.5);
  const br1=new THREE.BoxGeometry(dg,0.07,0.05); br1.rotateZ(Math.atan2(Lh-0.6,Lw));
  br1.translate(Lw/2,(Lh+0.2)/2,0); L.put(br1,shadeColor(wood,1.08));
  const br2=new THREE.BoxGeometry(dg,0.07,0.05); br2.rotateZ(-Math.atan2(Lh-0.6,Lw));
  br2.translate(Lw/2,(Lh+0.2)/2,0); L.put(br2,shadeColor(wood,1.08));
  const leaf=new THREE.Group();
  leaf.add(L.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a3424,emissive:0x0a0805}),rm)));
  leaf.position.set(-w/2+0.05,0,0);
  const g=new THREE.Group(); g.add(meshF); g.add(leaf);
  return {g,leaf,w:w};
}

/* —— 树：曲干 + 团冠（合批 1 mesh，青绿团簇） —— */
function makeTreeKZ(o){
  o=o||{};
  const h=o.h===undefined?5:o.h, R=seedRnd(o.seed===undefined?7:o.seed);
  const leaf=o.leaf===undefined?0x183a24:o.leaf;
  const B=new GeoBag();
  B.put(limbGeo([0,0,0],[R()*0.5-0.25,h*0.62,0],h*0.05,h*0.022,6),0x2a2018);
  const nb=o.blobs===undefined?3:o.blobs;
  for(let i=0;i<nb;i++){
    const bl=new THREE.SphereGeometry(h*(0.16+R()*0.10),8,6);
    bl.scale(1.15,0.85,1.15);
    bl.translate((R()-0.5)*h*0.30,h*(0.62+0.30*R()),(R()-0.5)*h*0.24);
    B.put(bl,shadeColor(leaf,0.8+R()*0.45));
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2c3c28,emissive:0x081008}),{c:o.rimC===undefined?0xa3c98f:o.rimC,i:o.rim===undefined?0.2:o.rim,p:2.4}));
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g};
}

/* —— 花径花丛：细茎小团花（杏黄/粉白相间）+ 叶（合批 1 mesh） —— */
function makeBlossomKZ(o){
  o=o||{};
  const n=o.n===undefined?12:o.n, w=o.w===undefined?14:o.w, R=seedRnd(o.seed===undefined?31:o.seed);
  const cols=[0xf2c94c,0xe8b8c4,0xf2e2c0,0xc8d89a];
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*1.6, hh=0.5+R()*0.75;
    const stem=new THREE.CylinderGeometry(0.03,0.045,hh,5); stem.translate(x,hh/2,z); B.put(stem,0x2c4024);
    const bl=new THREE.SphereGeometry(0.16+R()*0.12,7,5); bl.translate(x,hh+0.08,z);
    B.put(bl,cols[(R()*cols.length)|0]);
    if(R()<0.6){
      const lf=new THREE.PlaneGeometry(0.5,0.18); lf.rotateZ(0.4+R()*0.6); lf.rotateY(R()*1.2);
      lf.translate(x+0.14,hh*0.55,z); B.put(lf,shadeColor(0x3a5a30,0.9+R()*0.4));
    }
  }
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x44523a,emissive:0x0b120a,side:THREE.DoubleSide}),{c:0xc4dc9a,i:0.30,p:2.3}));
  const g=new THREE.Group(); g.add(mesh);
  return {g};
}

/* —— 篱下鸡群：觅食母鸡两三只（合批 1 mesh，静态点缀生活气） —— */
function makeHensKZ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?47:o.seed), n=o.n===undefined?3:o.n, w=o.w===undefined?6:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*2.4, s=0.8+R()*0.35, peck=R()<0.5?0.55:0.15;
    const body=new THREE.SphereGeometry(0.24,8,6); body.scale(1.25,0.95,0.9); body.translate(x,0.26*s,z);
    B.put(body,shadeColor(0x8a5a30,0.85+R()*0.35));
    const head=new THREE.SphereGeometry(0.10,7,5); head.translate(x+0.30*s,0.26*s+peck*0.4,z);
    B.put(head,shadeColor(0x8a5a30,1.1));
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

/* —— 杜甫（主人）：草堂褐袍，全诗一线贯穿（每次 build 新建材质） —— */
function kuanzhiHost(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x4a3a26,belt:0x8f6a33,skin:0xd9b189,collar:0xc8b488,
    hair:0x181410,hat:'发髻',beard:true,rimC:0xa3c98f,rim:0.42,noProp:true,scale:scale});
}

function bCover(){ // 卷首 · 浣花溪晓 —— 草堂远影，春水一湾，晨光熹微
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0b150e,c2:0x16281a,y:-1.6}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:3,peaks:5,seed:207,color:0x0c1911,atmo:0x2c4434,
    fogK:0.62,glowK:0.05,glow:0xbcd8a0,y:-10});
  ridge.g.position.set(0,0,-85); g.add(ridge.g);
  /* 一湾春水绕村 */
  const water=makeWater({size:14,seg:24,amp:0.10,freq:0.16,speed:0.45,flow:[0.12,0.5],spec:1.0,
    deep:0x0a1a12,shallow:0x1e4a34,skyc:0x2c5840,moonDir:[-60,90,-160],y:-1.5});
  water.mesh.scale.set(1,1,14); water.mesh.rotation.y=Math.PI/2;
  water.mesh.position.set(4,-1.5,-30); g.add(water.mesh);
  /* 草堂远影 + 村树两三株 */
  const cot=makeThatchKZ({w:8,d:6,h:3.2,window:false}); cot.g.position.set(-16,-1.6,-42); cot.g.rotation.y=0.5; g.add(cot.g);
  const t1=makeTreeKZ({h:7,seed:9,scale:1.5}); t1.g.position.set(-27,-1.6,-38); g.add(t1.g);
  const t2=makeTreeKZ({h:6,seed:13,scale:1.2}); t2.g.position.set(-6,-1.6,-50); g.add(t2.g);
  const t3=makeTreeKZ({h:8,seed:15,scale:1.6}); t3.g.position.set(22,-1.6,-46); g.add(t3.g);
  /* 群鸥四点 + 村人一痕 */
  const gulls=makeGullsKZ({n:4,cx:6,cz:-28,y:9,r:11,scMin:0.5}); gulls.g.position.set(0,-1.4,0); g.add(gulls.g);
  const crowd=makeCrowd({n:4,rect:[6,-36,18,7],seed:67,color:0x131e14,rimC:0xa3c98f,rim:0.2});
  crowd.mesh.position.y=-1.5; g.add(crowd.mesh);
  /* 晨光熹微：东天一抹暖意（青绿底上唯一的暖，随呼吸微明） */
  const dawn=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8c88a,
    transparent:true,opacity:0.15,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dawn.scale.set(150,60,1); dawn.position.set(-60,26,-120); dawn.renderOrder=-7; g.add(dawn);
  const petals=makePetalsKZ({n:44,box:[170,26,90],pos:[0,4,-30],size:6,maxA:0.2}); g.add(petals.points);
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
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
    brL.update(t,k); rkR.update(t,k); crowd.update(t); gulls.update(t);
    dawn.material.opacity=k*(0.11+0.03*Math.sin(t*0.4));
  }};
}

function bChunshui(){ // 一 · 春水群鸥 —— 舍南舍北皆春水，但见群鸥日日来
  const g=new THREE.Group();
  /* 大水漫绕：草堂坐落水中一渚（舍南舍北皆春水） */
  const water=makeWater({size:420,seg:76,amp:0.16,freq:0.14,speed:0.5,flow:[0.25,0.4],spec:1.1,
    deep:0x0a1a12,shallow:0x1e4a34,skyc:0x2c5840,moonDir:[-70,80,-150],y:-0.35});
  g.add(water.mesh);
  const grd=makeGround({r:15,c1:0x14231a,c2:0x1d3020,y:-0.1}); grd.mesh.position.set(-11,-0.1,-16); g.add(grd.mesh);
  /* 远岸一带 + 远村人影 */
  const bank=makeGround({r:90,c1:0x0c1710,c2:0x152417,y:-1.2}); bank.mesh.position.set(6,-1.2,-78); g.add(bank.mesh);
  const crowd=makeCrowd({n:4,rect:[-14,-66,26,9],seed:69,color:0x121c13,rimC:0xa3c98f,rim:0.18});
  g.add(crowd.mesh);
  const ridge=makeRange({r:260,h:36,layers:3,peaks:5,seed:213,color:0x09150e,atmo:0x2c4434,
    fogK:0.60,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 草堂 + 篱笆（渚上人家） */
  const cot=makeThatchKZ({w:7,d:5.2,h:2.9}); cot.g.position.set(-12,0,-18.5); cot.g.rotation.y=0.35; g.add(cot.g);
  const fe1=makeFenceKZ({w:8,seed:23}); fe1.g.position.set(-7,0,-11.6); fe1.g.rotation.y=0.5; g.add(fe1.g);
  const fe2=makeFenceKZ({w:6,seed:25}); fe2.g.position.set(-16.5,0,-12.4); fe2.g.rotation.y=-0.4; g.add(fe2.g);
  /* 主人临流而立，看鸥鸟自来 */
  const host=kuanzhiHost(1.35,'独立'); host.position.set(-8.4,0,-12.4); host.rotation.y=-0.6; g.add(host);
  /* 群鸥日日来：绕渚盘旋（远而小，不抢景） */
  const gulls=makeGullsKZ({n:5,cx:8,cz:-16,y:8,r:10,scMin:0.35}); g.add(gulls.g);
  /* 水线浮光 */
  const foam=makeGlow({n:60,box:[150,2,40],pos:[0,-0.15,-12],color:0x9ec8a8,size:6,speed:0.3,rise:0,maxA:0.16});
  g.add(foam.points);
  const petals=makePetalsKZ({n:36,box:[120,20,60],pos:[0,3,-14],size:6,maxA:0.22,c:0xe8cccc}); g.add(petals.points);
  const motes=makeGlow({n:30,box:[150,20,80],pos:[0,7,-20],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,24,110],pos:[0,8,-48],scale:74,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:22,n:11,d:5,color:0x071009,seed:43,sway:1.2,tip:0x2c4028});
  reed.g.position.set(15,-0.9,14); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.4,w:16,d:6,color:0x070d08,seed:41,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(-14,-1.1,13); g.add(rk.g);
  addLights(g,{c:0xd8cc9a,i:0.44,p:[-40,75,25]},{c:0x1e2c1e,i:0.64});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
      foam.update(t); rk.update(t,k); reed.update(t,k); crowd.update(t); gulls.update(t);
      host.update(t,k);
    },onEnter(){   // 鸥鸣两声（WebAudio 可用时）
      pluck(5,0.15,0.07); pluck(4,0.6,0.06);
    }};
}

function bPengmen(){ // 二（标志性瞬间）· 花径蓬门 —— 花径不曾缘客扫，蓬门今始为君开
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0b150e,c2:0x16281a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:36,layers:3,peaks:5,seed:221,color:0x09150e,atmo:0x2c4434,
    fogK:0.60,glowK:0.04,glow:0xaac890,y:-7});
  ridge.g.position.set(0,0,-95); g.add(ridge.g);
  /* 花径：一条小路通向柴门，两侧花丛相夹 */
  const path=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.10,22),
    new THREE.MeshPhongMaterial({color:0x4c4830,shininess:4,emissive:0x12110a}));
  path.position.set(0,0.05,4); g.add(path);
  const blL=makeBlossomKZ({n:14,w:17,seed:31}); blL.g.position.set(-2.1,0,3); g.add(blL.g);
  const blR=makeBlossomKZ({n:12,w:15,seed:37}); blR.g.position.set(2.1,0,4.5); g.add(blR.g);
  /* 篱笆两段夹一门（蓬门） */
  const feL=makeFenceKZ({w:11,seed:51}); feL.g.position.set(-6.9,0,-6); g.add(feL.g);
  const feR=makeFenceKZ({w:11,seed:53}); feR.g.position.set(6.9,0,-6); g.add(feR.g);
  const gate=makeGateKZ({}); gate.g.position.set(0,0,-6); g.add(gate.g);
  /* 门内草堂（春水群鸥的花溪人家） */
  const cot=makeThatchKZ({w:8,d:6,h:3.1}); cot.g.position.set(-2.5,0,-17.5); cot.g.rotation.y=0.2; g.add(cot.g);
  const t1=makeTreeKZ({h:6.5,seed:57}); t1.g.position.set(7,0,-13); g.add(t1.g);
  const t2=makeTreeKZ({h:7,seed:59}); t2.g.position.set(-13,0,-16); g.add(t2.g);
  /* 篱下鸡群（生活气）+ 篱外一湾春水微光 */
  const hens=makeHensKZ({n:3,seed:47,w:6}); hens.g.position.set(-4.6,0,-3.2); g.add(hens.g);
  const water=makeWater({size:12,seg:16,amp:0.08,freq:0.16,speed:0.4,flow:[0.15,0.5],spec:1.0,
    deep:0x0a1a12,shallow:0x1e4a34,skyc:0x2c5840,moonDir:[-60,80,-150],y:-0.2});
  water.mesh.scale.set(1,1,7); water.mesh.rotation.y=Math.PI/2;
  water.mesh.position.set(14,-0.25,-12); g.add(water.mesh);
  /* 主人倚门延客（为君开的姿态），客自花径来 */
  const host=kuanzhiHost(1.4,'指月'); host.position.set(1.9,0,-5.1); host.rotation.y=-0.35; g.add(host);
  const guest=makeFigure({pose:'独立',robe:0x2c3440,belt:0x6a5638,skin:0xd9b189,collar:0xb8c0cc,
    hair:0x14161c,hat:'幞头',beard:false,rimC:0xa3c98f,rim:0.4,noProp:true,scale:1.32});
  guest.position.set(-2.2,0,0.6); guest.rotation.y=3.02; g.add(guest);
  /* 群鸥三两，绕舍而翔 */
  const gulls=makeGullsKZ({n:3,cx:-2,cz:-15,y:10.5,r:9,scMin:0.35}); g.add(gulls.g);
  /* 花瓣两色缓落 */
  const petals=makePetalsKZ({n:64,box:[70,20,44],pos:[0,3,-8],size:7,maxA:0.34,c:0xf0d4d4});
  g.add(petals.points);
  const petals2=makePetalsKZ({n:40,box:[60,18,36],pos:[3,3,-4],size:6,maxA:0.26,c:0xf2e4c4});
  g.add(petals2.points);
  /* 东天晨光：柴门为客而开的一点暖 */
  const east=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf2cc88,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  east.scale.set(130,48,1); east.position.set(70,20,-90); east.renderOrder=-7; g.add(east);
  const motes=makeGlow({n:32,box:[110,18,60],pos:[0,7,-12],color:0xcfe0b0,size:6,speed:0.04,rise:0,maxA:0.13});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[190,22,100],pos:[0,8,-46],scale:72,color:0x1e3424,op:0.11});
  g.add(mist.g);
  const brL=makeForeground({kind:'树枝',w:34,n:7,d:6,color:0x081009,seed:61,sway:0.9,rim:0.14,rimC:0xa3c98f});
  brL.g.position.set(-19,-1.2,11); g.add(brL.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x070d08,seed:63,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(13,-1.2,12); g.add(rk.g);
  addLights(g,{c:0xeed8a0,i:0.48,p:[45,70,30]},{c:0x20301e,i:0.66});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      petals.update(t); petals2.update(t);
      brL.update(t,k); rk.update(t,k); gulls.update(t);
      host.update(t,k); guest.update(t,k);
      east.material.opacity=k*(0.17+0.12*(0.5+0.5*Math.sin(t*0.3)));
    }};
}

function bZunjiu(){ // 三 · 樽酒盘飧 —— 盘飧市远无兼味，樽酒家贫只旧醅
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0c160e,c2:0x18261a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:34,layers:2,peaks:4,seed:229,color:0x091409,atmo:0x2a4230,
    fogK:0.58,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 草堂作底（檐下小宴）+ 暖窗 */
  const cot=makeThatchKZ({w:11,d:5.5,h:3.3}); cot.g.position.set(0,0,-10); g.add(cot.g);
  /* 长案 + 盘飧四碟（市远无兼味：家常小菜） */
  const tb=makeTable({w:8,d:3,h:1.5}); tb.g.position.set(0,0,-2); g.add(tb.g);
  const dishPos=[[-2.7,0.15],[-0.9,-0.35],[0.9,0.2],[2.7,-0.2]];
  const dishes=[];
  for(let i=0;i<dishPos.length;i++){
    const d=makeDish({r:0.75,n:4}); d.g.position.set(dishPos[i][0],1.5,-2+dishPos[i][1]); g.add(d.g); dishes.push(d);
  }
  /* 酒器六件：樽/壶/坛（旧醅封泥）/杯二/碗 —— 混搭成组 */
  const vz1=makeVessel({type:'樽',mat:'陶',scale:0.9,liquid:true}); vz1.g.position.set(-0.35,1.5,-2.5); g.add(vz1.g);
  const vz2=makeVessel({type:'壶',mat:'陶',scale:0.72}); vz2.g.position.set(-1.7,1.5,-2.85); g.add(vz2.g);
  const vz3=makeVessel({type:'坛',mat:'陶',scale:0.78}); vz3.g.position.set(1.75,1.5,-2.55); g.add(vz3.g);
  const vz4=makeVessel({type:'杯',mat:'陶',scale:0.85,liquid:true}); vz4.g.position.set(0.85,1.5,-1.55); g.add(vz4.g);
  const vz5=makeVessel({type:'杯',mat:'陶',scale:0.85,liquid:true}); vz5.g.position.set(-2.15,1.5,-1.5); g.add(vz5.g);
  const vz6=makeVessel({type:'碗',mat:'陶',scale:0.9}); vz6.g.position.set(2.6,1.5,-1.55); g.add(vz6.g);
  /* 火盆温酒 + 樽上酒气 */
  const br=makeBrazier({r:0.9,fh:1.7,fw:0.95,light:0.85,lightD:28,embers:20});
  br.g.position.set(5.7,0,-4.9); g.add(br.g);
  const steam=makeGlow({n:20,box:[1.4,2.0,1.4],pos:[-0.35,2.55,-2.5],color:0xdce8cc,size:4,speed:0.5,rise:1,maxA:0.20});
  g.add(steam.points);
  /* 主人指樽让客（无兼味、只旧醅的自谦），客举杯相酬 */
  const host=kuanzhiHost(1.42,'指月'); host.position.set(-3.5,0,0.7); host.rotation.y=0.9; g.add(host);
  const guest=makeFigure({pose:'举杯',robe:0x2c3440,belt:0x6a5638,skin:0xd9b189,collar:0xb8c0cc,
    hair:0x14161c,hat:'幞头',beard:false,rimC:0xa3c98f,rim:0.4,scale:1.4});
  guest.position.set(2.7,0,1.0); guest.rotation.y=-0.55; g.add(guest);
  /* 篱外远村人影一痕 */
  const crowd=makeCrowd({n:3,rect:[8,-30,14,7],seed:71,color:0x121c13,rimC:0xa3c98f,rim:0.16});
  g.add(crowd.mesh);
  const petals=makePetalsKZ({n:30,box:[90,18,50],pos:[0,3,-10],size:6,maxA:0.2,c:0xe8cccc}); g.add(petals.points);
  const motes=makeGlow({n:28,box:[100,16,50],pos:[0,6,-10],color:0xe0d0a0,size:5,speed:0.05,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[180,20,90],pos:[0,8,-50],scale:70,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x070d08,seed:81,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(-12,-1.2,11); g.add(rk.g);
  const brR=makeForeground({kind:'树枝',w:28,n:6,d:5,color:0x081009,seed:83,sway:0.8,rim:0.14,rimC:0xa3c98f});
  brR.g.position.set(14,-1.0,10); g.add(brR.g);
  addLights(g,{c:0xeed49c,i:0.5,p:[35,68,28]},{c:0x21301f,i:0.68});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ridge.update(t,0); mist.update(t,k); motes.update(t); petals.update(t); steam.update(t);
      rk.update(t,k); brR.update(t,k); crowd.update(t);
      host.update(t,k); guest.update(t,k); br.update(t,k);
      for(let i=0;i<dishes.length;i++)dishes[i].glow.material.opacity=k*0.16*(0.8+0.2*Math.sin(t*1.1+i));
    }};
}

function bHulin(){ // 四（末境·可点击）· 隔篱呼邻 —— 点击蓬门：柴门初开，隔篱呼邻，酒盏相碰
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,open:0,pulse:0};
  const grd=makeGround({r:130,c1:0x0c160e,c2:0x18261a,y:0}); g.add(grd.mesh);
  const ridge=makeRange({r:250,h:34,layers:2,peaks:4,seed:237,color:0x091409,atmo:0x2a4230,
    fogK:0.58,glowK:0.04,glow:0xaac890,y:-8});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  /* 草堂暖窗（宴饮的背景） */
  const cot=makeThatchKZ({w:9,d:5.5,h:3.2}); cot.g.position.set(-3,0,-16); g.add(cot.g);
  /* 长篱横贯，中间柴门（点击对象） */
  const feL=makeFenceKZ({w:17,seed:91}); feL.g.position.set(-7.6,0,-5.2); g.add(feL.g);
  const feR=makeFenceKZ({w:14,seed:93}); feR.g.position.set(11.5,0,-5.2); g.add(feR.g);
  const gate=makeGateKZ({w:2.3,h:2.2,seed:95}); gate.g.position.set(2,0,-5.2); g.add(gate.g);
  /* 案酒：主人与客（肯与邻翁相对饮） */
  const tb=makeTable({w:5.4,d:2.6,h:1.5}); tb.g.position.set(-5.6,0,-2.4); tb.g.rotation.y=0.12; g.add(tb.g);
  const dz1=makeDish({r:0.7,n:4}); dz1.g.position.set(-6.6,1.5,-2.6); g.add(dz1.g);
  const dz2=makeDish({r:0.7,n:3}); dz2.g.position.set(-4.6,1.5,-2.2); g.add(dz2.g);
  const jz=makeVessel({type:'樽',mat:'陶',scale:0.85,liquid:true}); jz.g.position.set(-5.6,1.5,-2.9); g.add(jz.g);
  const hp=makeVessel({type:'壶',mat:'陶',scale:0.66}); hp.g.position.set(-6.7,1.5,-1.9); g.add(hp.g);
  const c1=makeVessel({type:'杯',mat:'陶',scale:0.85,liquid:true}); c1.g.position.set(-4.7,1.5,-1.8); g.add(c1.g);
  const c2=makeVessel({type:'杯',mat:'陶',scale:0.85,liquid:true}); c2.g.position.set(-6.3,1.5,-1.8); g.add(c2.g);
  const host=kuanzhiHost(1.42,'举杯'); host.position.set(-3.7,0,-1.0); host.rotation.y=1.05; g.add(host);
  const guest=makeFigure({pose:'举杯',robe:0x2c3440,belt:0x6a5638,skin:0xd9b189,collar:0xb8c0cc,
    hair:0x14161c,hat:'幞头',beard:false,rimC:0xa3c98f,rim:0.4,scale:1.4});
  guest.position.set(-7.3,0,-1.5); guest.rotation.y=0.45; g.add(guest);
  /* 邻翁（隔篱相唤者）：篱外举杯候呼，点击后穿门而入 */
  const neighbor=makeFigure({pose:'举杯',robe:0x3a3226,belt:0x7a6238,skin:0xd0ab84,collar:0xb0a484,
    hair:0xcfd2c4,hat:'发髻',beard:true,rimC:0xb8cc90,rim:0.44,noProp:true,scale:1.36});
  neighbor.position.set(6.2,0,-8.6); neighbor.rotation.y=-0.7; g.add(neighbor);
  /* 隔篱相唤的暖光：柴门边一盏（点击后酒盏相碰处迸亮） */
  const clink=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xf2d488,
    transparent:true,opacity:0.5,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  clink.scale.set(7,4,1); clink.position.set(4.2,2.4,-3.4); clink.renderOrder=4; g.add(clink);
  const burst=makeBurst({n:70,color:0xffe0a0,pos:[4.2,2.35,-3.4]}); g.add(burst.points);
  const pl=new THREE.PointLight(0xf2c884,1.25,42); pl.position.set(4.0,3.4,-3.6); g.add(pl);
  /* 篱外一湾春水微光 + 鸥影 + 鸡群 */
  const water=makeWater({size:13,seg:16,amp:0.08,freq:0.15,speed:0.4,flow:[0.2,0.5],spec:1.0,
    deep:0x0a1a12,shallow:0x1e4a34,skyc:0x2c5840,moonDir:[-60,80,-150],y:-0.22});
  water.mesh.scale.set(1,1,8); water.mesh.rotation.y=Math.PI/2;
  water.mesh.position.set(-21,-0.25,-14); g.add(water.mesh);
  const gulls=makeGullsKZ({n:3,cx:-4,cz:-20,y:9,r:9,scMin:0.5}); g.add(gulls.g);
  const hens=makeHensKZ({n:3,seed:97,w:5}); hens.g.position.set(12.5,0,-3.6); g.add(hens.g);
  const petals=makePetalsKZ({n:36,box:[100,18,54],pos:[0,3,-10],size:6,maxA:0.24,c:0xe8cccc}); g.add(petals.points);
  const motes=makeGlow({n:30,box:[120,18,60],pos:[0,7,-12],color:0xe0d0a0,size:5,speed:0.05,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[200,22,100],pos:[0,8,-52],scale:72,color:0x1e3424,op:0.10});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x071009,seed:99,sway:1.1,tip:0x2c4028});
  reed.g.position.set(-15,-1.0,13); g.add(reed.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:6,color:0x070d08,seed:101,rim:0.12,rimC:0xa3c98f});
  rk.g.position.set(13,-1.2,12); g.add(rk.g);
  addLights(g,{c:0xf0d49c,i:0.5,p:[30,70,30]},{c:0x21301f,i:0.68});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.open=Math.min(1,ctl.open+dt/1.8);
      ctl.pulse=Math.max(0,ctl.pulse-dt/2.2);
      const sm=ctl.open*ctl.open*(3-2*ctl.open);       // smoothstep：开门与唤邻的缓起缓收
      gate.leaf.rotation.y=1.95*sm;                    // 柴门呀然内开
      neighbor.position.set(6.2-3.0*sm,0,-8.6+5.4*sm); // 邻翁穿门而入
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t); petals.update(t);
      burst.update(t); reed.update(t,k); rk.update(t,k); gulls.update(t);
      host.update(t,k); guest.update(t,k); neighbor.update(t,k);
      jz.update(t,k); c1.update(t,k); c2.update(t,k); hp.update(t,k);
      /* 门边暖光：随点击迸亮（峰值 0.50 = 初值，每帧乘 fadeK） */
      clink.material.opacity=k*(0.06+0.44*ctl.pulse);
      pl.intensity=k*1.25*(0.30+0.70*ctl.pulse);
    },click(){
      if(ctl.t<1.2)return;                             // 冷却：入场与连点间隔
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(0,0,0.15); pluck(2,0.35,0.12); pluck(4,0.8,0.11); pluck(5,1.35,0.09);
        const fl=$('#flash'); fl.textContent='隔篱呼取尽余杯'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
      burst.fire(); ctl.pulse=1;                       // 可再点：酒盏再碰一拍
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x132a1e),hor:C(0x35543a),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0056,star:0.12,
  moon:new THREE.Vector3(-95,64,-210),ms:0.55,mph:0.42,mhaze:0.05,dirC:C(0xe6cd92),dirI:0.5,
  dirP:new THREE.Vector3(-55,75,45),ambC:C(0x25331f),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,11,62],t:[0,12,55],lf:[-4,9,-30],lt:[-5,10,-32]},
  sky:()=>SK({top:C(0x152c20),hor:C(0x3a5c40),bot:C(0x0c1710),fog:C(0x0e1d16),fd:0.0050,star:0.10,
    ms:0.45,mph:0.46,mhaze:0.04,moon:new THREE.Vector3(-80,58,-220),
    dirC:C(0xe8d094),dirI:0.46,ambC:C(0x27351f),ambI:0.68}) },
{ name:'春水群鸥',dwell:17,river:0.05,build:bChunshui,
  cam:{f:[0,6.5,26],t:[-2,6,22],lf:[-11,3.5,-16],lt:[-12,3.2,-18]},
  sky:()=>SK({top:C(0x122818),hor:C(0x31503a),bot:C(0x0a1410),fog:C(0x0f1e17),fd:0.0056,star:0.12,
    ms:0.42,mph:0.44,mhaze:0.05,moon:new THREE.Vector3(-95,64,-210),
    dirC:C(0xe6cd92),dirI:0.48,dirP:new THREE.Vector3(-50,72,40),ambC:C(0x25331f),ambI:0.66}) },
{ name:'花径蓬门',dwell:18,river:0.04,build:bPengmen,
  cam:{f:[2.8,5.6,14.5],t:[-1.2,5,11.5],lf:[0,2.6,-6],lt:[0,2.4,-7]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x36543c),bot:C(0x0a1410),fog:C(0x0f1e17),fd:0.0058,star:0.12,
    ms:0.45,mph:0.46,mhaze:0.05,moon:new THREE.Vector3(-100,62,-205),
    dirC:C(0xf0d69a),dirI:0.5,dirP:new THREE.Vector3(50,70,35),ambC:C(0x26341f),ambI:0.68}) },
{ name:'樽酒盘飧',dwell:17,river:0.02,build:bZunjiu,
  cam:{f:[3.2,5.4,12],t:[-1.8,5,9.5],lf:[0,2.2,-2],lt:[0,2.1,-2.5]},
  sky:()=>SK({top:C(0x152a1c),hor:C(0x3a563c),bot:C(0x0b150f),fog:C(0x101f17),fd:0.0060,star:0.12,
    ms:0.45,mph:0.46,mhaze:0.05,moon:new THREE.Vector3(-105,60,-200),
    dirC:C(0xf0d69a),dirI:0.52,dirP:new THREE.Vector3(40,68,32),ambC:C(0x27351f),ambI:0.68}) },
{ name:'隔篱呼邻',dwell:18,river:0.03,build:bHulin,
  cam:{f:[2,5.5,16],t:[-1,5,14],lf:[0,2.4,-5],lt:[0,2.3,-6]},
  sky:()=>SK({top:C(0x162c1c),hor:C(0x3c583c),bot:C(0x0b150f),fog:C(0x101f17),fd:0.0062,star:0.12,
    ms:0.45,mph:0.44,mhaze:0.06,moon:new THREE.Vector3(-110,58,-200),
    dirC:C(0xf2d89c),dirI:0.52,dirP:new THREE.Vector3(30,66,30),ambC:C(0x27351f),ambI:0.68}) },
];
"""
