# -*- coding: utf-8 -*-
"""yijianmei-hongou.py —— 《一剪梅·红藕香残玉簟秋》（宋·李清照，no.188，水墨夜思）生成配置
四境（queue 分境为准）：红藕兰舟（红藕香残·玉簟秋·独上兰舟）、雁字西楼（标志性瞬间：雁阵排「人」字掠月·锦书虚影·月满西楼）、
花水两愁（花自飘零水自流·两地同月对切：左西楼凭栏的她/右随流的孤舟）、眉间心头（末境点击：雁字掠月+锦书浮来终是影）。
全页冷银水墨，禁金；accent=#b4c2d4。意象链：荷塘残红/兰舟/西楼/雁阵/满月/水中月。"""

META = dict(
    N=4, slug='yijianmei-hongou', title='一剪梅·红藕香残玉簟秋', dyn='宋 · 李清照', brand_author='李清照',
    gold_rgb='180,194,212',
    root=""":root{
  --gold:#b4c2d4; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(180,194,212,.26);
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
        ('rgba(232,220,192', 'rgba(186,200,222', 2),
    ],
    tip='轻点画面 / 按空格 —— 雁字掠月，锦书浮来',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看雁字掠月、锦书虚影',
    cover_read='一剪梅。宋，李清照。红藕香残玉簟秋。轻解罗裳，独上兰舟。云中谁寄锦书来？雁字回时，月满西楼。花自飘零水自流。一种相思，两处闲愁。此情无计可消除，才下眉头，却上心头。',
    cover_p1='四重意境，随词句次第展开：红藕香残、玉簟生凉的清秋里，她轻解罗裳、独上兰舟；西楼望尽雁字回时，一轮满月洒满楼头，锦书却仍在云外；花自飘零水自流，同一种相思牵起两处闲愁；愁绪无计可消除，才下眉头，却上心头。',
    cover_p2='边读词，边走进易安居士这一塘秋色、一叶兰舟与满楼月色，看雁字掠月处的两地相思。',
    end_h2='眉头 · 心头', cn_word='四',
    words_js="['再游一次，月满西楼','初识易安，尚需共读','渐入佳境，再诵几遍','两处闲愁，渐次懂得','深得易安词心','一种相思，两处相知']",
    sky_atmo='0x1c2433',
)

POEM_JS = """const POEM = [
{ name:'红藕兰舟', jing:'红藕香残，玉簟生凉 —— 轻解罗裳，独上兰舟。（残荷 · 玉簟 · 兰舟）',
  segs:[
   {c:'红藕香残玉簟秋。', p:py('hóng ǒu xiāng cán yù diàn qiū')},
   {c:'轻解罗裳，', p:py('qīng jiě luó cháng')},
   {c:'独上兰舟。', p:py('dú shàng lán zhōu')}],
  read:'红藕香残玉簟秋。轻解罗裳，独上兰舟。',
  yisi:'粉红的荷花已经凋残，幽香消散，竹席透出秋的凉意。她轻轻提起罗裙，独自登上兰木小舟。——荷残席凉，点出清秋时节，也点出独处空闺的索寞；荡舟原为排遣，却把这分秋思带进了满塘暮色。',
  zhu:[['红藕','红色的荷花。荷花凋残、幽香消散，暗写青春与欢爱随秋光同逝'],
       ['玉簟','光洁如玉的竹席。簟读 diàn；「玉簟秋」语带双关：既写席上生凉，也写心头秋意'],
       ['罗裳','丝罗衣裙。裳读 cháng，古指下身所着的裙'],
       ['兰舟','木兰木所造之船，诗词中作小舟的美称'],
       ['独上','无人相伴。一个「独」字领起全词离情']] },
{ name:'雁字西楼', jing:'云中谁寄锦书来？雁字回时，月满西楼。（雁阵 · 锦书 · 满月）',
  segs:[
   {c:'云中谁寄锦书来？', p:py('yún zhōng shuí jì jǐn shū lái')},
   {c:'雁字回时，', p:py('yàn zì huí shí')},
   {c:'月满西楼。', p:py('yuè mǎn xī lóu')}],
  read:'云中谁寄锦书来？雁字回时，月满西楼。',
  yisi:'仰望云天：是谁把锦字书信寄来？当雁阵排成「人」字飞回的时候，皎洁的月光已经洒满西楼。——盼书不至，唯见雁归月满；一个「谁」字问尽长空，满楼月色正是她望遍天涯的目光。',
  zhu:[['锦书','锦字书。前秦苏蕙织锦回文诗寄夫窦滔，后泛指夫妻、情人间的书信'],
       ['雁字','雁群飞行时排成「一」字或「人」字，故称。古有雁足传书之说，雁归最牵相思'],
       ['雁足传书','《汉书·苏武传》载：汉使诡言天子射上林中得雁，雁足系帛书、言苏武所在，单于只得放还苏武。后世遂以「鸿雁传书」代指书信往来'],
       ['月满西楼','月光铺满楼头。月圆而人未圆，满楼月色反衬满怀离愁']] },
{ name:'花水两愁', jing:'花自飘零水自流 —— 一种相思，两处闲愁。（落花 · 流水 · 两地同月）',
  segs:[
   {c:'花自飘零水自流。', p:py('huā zì piāo líng shuǐ zì liú')},
   {c:'一种相思，', p:py('yī zhǒng xiāng sī')},
   {c:'两处闲愁。', p:py('liǎng chù xián chóu')}],
  read:'花自飘零水自流。一种相思，两处闲愁。',
  yisi:'花，自顾飘零；水，自顾东流。同是一样的相思，却牵起分居两地的你、我各自心头的闲愁。——两个「自」字写尽万物无情、各不相管，唯独情不能自已；为同一种相思所苦的两人，恰是两心相通的印证。',
  zhu:[['花自飘零水自流','花落水流本是无心之物，与上阕「红藕香残」「独上兰舟」暗合；亦喻两人如花落水流、各自东西'],
       ['一种相思','同样的相思。楼头人与远行人共此一心'],
       ['两处闲愁','两地各自萦绕的愁。明知对方也在愁，愁里便有了相知的暖；闲愁非闲，是排遣不去']] },
{ name:'眉间心头', jing:'此情无计可消除 —— 才下眉头，却上心头。（楼头 · 凭栏 · 心月）',
  segs:[
   {c:'此情无计可消除，', p:py('cǐ qíng wú jì kě xiāo chú')},
   {c:'才下眉头，', p:py('cái xià méi tóu')},
   {c:'却上心头。', p:py('què shàng xīn tóu')}],
  read:'此情无计可消除，才下眉头，却上心头。',
  yisi:'这相思之情没有办法消除，颦着的眉头刚刚舒展，它却又悄悄涌上心头。——眉头是外，心头是内；一「下」一「上」、一「才」一「却」，愁绪去而复来、萦绕不去之态如在目前，遂成写愁绝唱。',
  zhu:[['无计可消除','没有办法排遣、消除'],
       ['才下眉头，却上心头','化用范仲淹「都来此事，眉间心上，无计相回避」而翻出新意：愁先在眉间、后落心头，内里更深更沉'],
       ['却','再、又；转折中见愁之缠绵']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「红藕香残玉簟秋」的下一句是？', o:['轻解罗裳，独上兰舟','云中谁寄锦书来','花自飘零水自流'], a:0},
 {q:'「花自飘零水自流」的下一句是？', o:['才下眉头，却上心头','一种相思，两处闲愁','雁字回时，月满西楼'], a:1},
 {q:'「玉簟秋」中「簟」的正确读音和意思是？', o:['dàn，挑担的担具','diàn，光洁如玉的竹席','tán，深潭之潭'], a:1},
 {q:'「雁字回时」暗用的典故是？', o:['庄周梦蝶，物我两忘','嫦娥奔月，碧海青天','雁足传书：苏武以帛书系雁足，后世遂以鸿雁代书信'], a:2},
 {q:'「才下眉头，却上心头」写出的是？', o:['久别重逢、眉开眼笑的欢愉','相思之愁无法排遣，眉间刚舒展又涌上心头','岁月催人老的无奈'], a:1},
];
"""

SCENES_JS = """/* ================= 一剪梅·红藕香残玉簟秋 · 四境场景（水墨夜思：冷银、残荷、兰舟、雁阵、满月） ================= */

/* 漂瓣：水面残红（菱形小瓣贴水缓流，Normal 混合不吃雾）——「红藕香残」「花自飘零」 */
const BAN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform vec3 uBox; uniform vec2 uFlow;
varying float vA;
void main(){
  vec3 p=position;
  p.x=mod(p.x+uTime*uFlow.x+uBox.x*0.5,uBox.x)-uBox.x*0.5;
  p.z=mod(p.z+uTime*uFlow.y+uBox.z*0.5,uBox.z)-uBox.z*0.5;
  p.y+=sin(uTime*0.8+aSeed*41.0)*0.05;
  vA=0.35+0.65*fract(aSeed*13.7);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const BAN_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=abs(q.x)*1.3+abs(q.y);
  float a=smoothstep(0.5,0.15,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLianban(o){
  o=o||{};
  const n=o.n===undefined?90:o.n, box=o.box||[90,1.5,64], pos=o.pos||[0,0.08,-22];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.8:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},
      uFlow:{value:new THREE.Vector2(o.fx===undefined?0.55:o.fx,o.fz===undefined?0.22:o.fz)},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x7a4a54:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.4:o.maxA}},
    vertexShader:BAN_VERT,fragmentShader:BAN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* 残荷：荷塘秋深（弯茎 + 低垂残叶/立叶 + 莲蓬 + 零星残红），一簇合批 1 mesh，水墨禁金唯残瓣哑红 */
function makeCanhe(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?81:o.seed);
  const n=o.n===undefined?9:o.n, w=o.w===undefined?9:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*w*0.7, h=1.6+R()*1.9, bend=(R()-0.5)*1.3;
    const p0=[x,0,z], p1=[x+bend*0.3,h*0.55,z+(R()-0.5)*0.5], p2=[x+bend,h,z+(R()-0.5)*0.9];
    B.put(limbGeo(p0,p1,0.045,0.03,5),0x1c2622);
    B.put(limbGeo(p1,p2,0.03,0.022,5),0x1a231f);
    const u=R();
    if(u<0.55){          /* 低垂残叶：斜倾圆盘（秋深荷残的「倒叶」） */
      const lr=0.55+R()*0.75;
      const leaf=new THREE.CircleGeometry(lr,9);
      leaf.rotateX(-Math.PI/2+(0.65+R()*0.5)*(R()<0.5?1:-1));
      leaf.rotateY(R()*6.283);
      leaf.translate(p2[0],p2[1]-lr*0.35,p2[2]);
      B.put(leaf,0x161f1a);
    }else if(u<0.8){     /* 莲蓬：小柄 + 顶盘 */
      const pod=new THREE.CylinderGeometry(0.11,0.15,0.34,7);
      pod.translate(p2[0],p2[1]+0.12,p2[2]); B.put(pod,0x20281f);
      const top=new THREE.CylinderGeometry(0.17,0.13,0.09,7);
      top.translate(p2[0],p2[1]+0.32,p2[2]); B.put(top,0x28311f);
    }else{               /* 未折的立叶 */
      const lr=0.5+R()*0.5;
      const leaf=new THREE.CircleGeometry(lr,9);
      leaf.rotateX(-Math.PI/2+0.28); leaf.rotateY(R()*6.283);
      leaf.translate(p2[0],p2[1],p2[2]);
      B.put(leaf,0x1a241d);
    }
  }
  /* 残红一二点：将谢未谢的花（全簇唯一的哑红残迹） */
  for(let i=0;i<(o.hong===undefined?2:o.hong);i++){
    const x=(R()-0.5)*w*0.8, z=(R()-0.5)*w*0.6, h=1.1+R()*1.4;
    const stem=new THREE.CylinderGeometry(0.028,0.035,h,5);
    stem.translate(x,h/2,z); B.put(stem,0x1c2622);
    const b1=new THREE.ConeGeometry(0.14,0.42,5); b1.translate(x,h+0.2,z); B.put(b1,0x4e2f36);
    const b2=new THREE.ConeGeometry(0.10,0.30,5); b2.rotateX(0.5); b2.translate(x+0.08,h+0.30,z); B.put(b2,0x5c3840);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x23303a,emissive:0x04070a,side:THREE.DoubleSide}),{c:0xb4c2d4,i:o.rim===undefined?0.20:o.rim,p:2.3})));
  return {g};
}

/* 兰舟：轻桡小舟（弯壳船体 + 两端挑尖 + 舱面横木 + 搁竹篙），合批 1 mesh，随波可荡 */
function makeLanzhou(o){
  o=o||{};
  const s=o.scale===undefined?1:o.scale;
  const g=new THREE.Group(), B=new GeoBag();
  const hull=new THREE.CylinderGeometry(0.62,0.34,4.9,8);
  hull.rotateZ(Math.PI/2); hull.scale(1,0.56,1.3); B.put(hull,0x2c3542);
  const bow=new THREE.ConeGeometry(0.38,1.15,8); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.8,1.4); bow.rotateZ(0.2); bow.translate(3.0,0.26,0); B.put(bow,0x2c3542);
  const stern=new THREE.ConeGeometry(0.34,0.95,8); stern.rotateZ(Math.PI/2);
  stern.scale(1,0.8,1.35); stern.rotateZ(-0.24); stern.translate(-2.85,0.30,0); B.put(stern,0x27303c);
  const plank=new THREE.BoxGeometry(1.5,0.09,1.1); plank.translate(0.5,0.32,0); B.put(plank,0x354050);
  const pole=new THREE.CylinderGeometry(0.045,0.045,4.4,6);
  pole.rotateZ(Math.PI/2); pole.rotateY(0.18); pole.translate(-0.4,0.5,0.3); B.put(pole,0x3a4a4a);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a465c,emissive:0x060a10,side:THREE.DoubleSide}),{c:0xb4c2d4,i:o.rim===undefined?0.42:o.rim,p:2.4})));
  g.scale.setScalar(s);
  return g;
}

/* 西楼：临水小楼（石基 + 下层楼身 + 上层望月栏 + 四阿顶 + 窗内冷光），合批 1 mesh + 一点窗光 */
function makeXilou(o){
  o=o||{};
  const B=new GeoBag(), c1=0x0d1219, c2=0x121a26, c3=0x19222f, c4=0x0a0e15;
  const base=new THREE.BoxGeometry(11,1.3,8.6); base.translate(0,0.65,0); B.put(base,c1);
  const lower=new THREE.BoxGeometry(6.8,5.4,5.2); lower.translate(0,1.3+2.7,0); B.put(lower,c2);
  const deck=new THREE.BoxGeometry(8.4,0.36,3.2); deck.translate(0,6.85,3.0); B.put(deck,c1);
  const upper=new THREE.BoxGeometry(5.2,4.0,4.4); upper.translate(0,7.0+2.0,0); B.put(upper,c2);
  const rail=new THREE.BoxGeometry(8.4,0.13,0.13); rail.translate(0,8.05,4.5); B.put(rail,c3);
  const rail2=new THREE.BoxGeometry(8.4,0.10,0.10); rail2.translate(0,7.45,4.5); B.put(rail2,c3);
  [1,-1].forEach(function(s){
    const sr=new THREE.BoxGeometry(0.12,0.12,3.0); sr.translate(s*4.2,8.05,3.1); B.put(sr,c3);
    const sr2=new THREE.BoxGeometry(0.12,0.10,3.0); sr2.translate(s*4.2,7.45,3.1); B.put(sr2,c3);
  });
  for(let i=0;i<7;i++){
    const post=new THREE.BoxGeometry(0.15,1.25,0.15);
    post.translate(-4.2+i*1.4,7.5,4.5); B.put(post,c3);
  }
  [1,-1].forEach(function(s){
    const win=new THREE.BoxGeometry(0.9,1.2,0.1); win.translate(s*1.15,9.2,2.22); B.put(win,0x2b3a52);
  });
  const roof=new THREE.ConeGeometry(4.9,2.1,4); roof.rotateY(Math.PI/4);
  roof.scale(1.34,1,1.06); roof.translate(0,11.0+1.05,0); B.put(roof,c4);
  const finial=new THREE.ConeGeometry(0.16,0.6,6); finial.translate(0,12.4,0); B.put(finial,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0xb4c2d4,i:o.rim===undefined?0.30:o.rim,p:2.5})));
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.16,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(3.2,3.2,1); lamp.position.set(0,9.2,2.4); lamp.renderOrder=2; g.add(lamp);
  return {g,lamp};
}

/* 楼头小平台：凭栏望月的立足处（面层 + 栏杆 + 身后楼身一角 + 檐角 + 窗光），合批 1 mesh */
function makeTerrace(){
  const B=new GeoBag(), c1=0x0d1219, c2=0x121a26, c3=0x19222f, c4=0x0a0e15;
  const deck=new THREE.BoxGeometry(9,0.52,5.2); deck.translate(0,0.26,-0.4); B.put(deck,c1);
  const rail=new THREE.BoxGeometry(8.6,0.14,0.14); rail.translate(0,1.62,2.1); B.put(rail,c3);
  const rail2=new THREE.BoxGeometry(8.6,0.10,0.10); rail2.translate(0,1.10,2.1); B.put(rail2,c3);
  for(let i=0;i<7;i++){
    const post=new THREE.BoxGeometry(0.16,1.5,0.16); post.translate(-4.3+i*1.43,0.9,2.1); B.put(post,c3);
  }
  [1,-1].forEach(function(s){
    const sr=new THREE.BoxGeometry(0.14,0.14,4.6); sr.translate(s*4.3,1.62,-1.0); B.put(sr,c3);
  });
  const wall=new THREE.BoxGeometry(7.4,6.4,1.0); wall.translate(0,3.2,-2.9); B.put(wall,c2);
  [1,-1].forEach(function(s){
    const col=new THREE.CylinderGeometry(0.20,0.24,5.6,8); col.translate(s*3.3,3.3,-2.2); B.put(col,c2);
  });
  const beam=new THREE.BoxGeometry(8.2,0.5,1.4); beam.translate(0,6.7,-2.4); B.put(beam,c2);
  const roof=new THREE.ConeGeometry(6.2,2.2,4); roof.rotateY(Math.PI/4);
  roof.scale(1.5,1,1.0); roof.translate(0,8.4,-1.6); B.put(roof,c4);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c,side:THREE.DoubleSide}),{c:0xb4c2d4,i:0.26,p:2.4})));
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.14,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(3.4,3.4,1); win.position.set(-1.2,4.4,-2.2); win.renderOrder=2; g.add(win);
  return {g,win};
}

/* 雁阵：排「人」字的雁群（InstancedMesh 7 只同航线：巡天掠月 / 点击掠月两用） */
function makeYanzhen(o){
  o=o||{};
  const n=o.n===undefined?7:o.n;
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.11,0.52,5); body.rotateX(Math.PI/2); B.put(body,0x121a27);
  const head=new THREE.SphereGeometry(0.08,6,5); head.translate(0,0.045,0.30); B.put(head,0x16202f);
  const beak=new THREE.ConeGeometry(0.028,0.12,4); beak.rotateX(Math.PI/2);
  beak.translate(0,0.045,0.41); B.put(beak,0x0e1520);
  [1,-1].forEach(function(s){
    const w=new THREE.BufferGeometry();
    w.setAttribute('position',new THREE.BufferAttribute(new Float32Array([
      0,0.035,0.11, 0,0.035,-0.15, s*0.74,0.15,-0.03]),3));
    w.computeVertexNormals(); B.put(w,0x18222f);
    const tail=new THREE.ConeGeometry(0.045,0.30,4); tail.rotateX(-Math.PI/2);
    tail.rotateZ(s*0.22); tail.translate(s*0.05,0.02,-0.38); B.put(tail,0x101825);
  });
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060b}),{c:0xb4c2d4,i:0.7,p:2.4});
  const mesh=new THREE.InstancedMesh(mergeGeos(B.list),mat,n);
  mesh.frustumCulled=false;
  const offs=[[0,0]];
  for(let i=1;i<=3;i++){ offs.push([0.95*i,-0.72*i],[-0.95*i,-0.72*i]); }
  const sc=o.scale===undefined?2.4:o.scale;
  const dm=new THREE.Object3D();
  return {mesh,update(t,k,fb,show){
    for(let i=0;i<n;i++){
      const o2=offs[i%offs.length];
      let px,py,pz,yaw;
      if(!show){ dm.position.set(0,-40,0); dm.scale.setScalar(0.0001); dm.rotation.set(0,0,0);
        dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix); continue; }
      if(fb===null||fb===undefined){
        const a=t*0.16+0.9;                     // 巡天：大椭圆缓飞，周期性掠过月前
        px=5+Math.cos(a)*78; pz=-190+Math.sin(a)*42;
        py=113+6*Math.sin(a*2.3);
        yaw=Math.atan2(-Math.sin(a)*78,Math.cos(a)*42);
      }else if(fb>=1){
        const a=t*0.13;                          // 掠月之后：绕月盘旋不去
        px=-8+Math.cos(a)*26; pz=-180+Math.sin(a)*20; py=64+3*Math.sin(a*2);
        yaw=Math.atan2(-Math.sin(a)*26,Math.cos(a)*20);
      }else{
        const e=ease(clamp(fb,0,1)), u=1-e;      // 点击航线：自天边掠月而过
        const p0=[-88,26,-20], p1=[-8,64,-118], p2=[70,84,-215];
        px=u*u*p0[0]+2*u*e*p1[0]+e*e*p2[0];
        py=u*u*p0[1]+2*u*e*p1[1]+e*e*p2[1];
        pz=u*u*p0[2]+2*u*e*p1[2]+e*e*p2[2];
        const dx=2*u*(p1[0]-p0[0])+2*e*(p2[0]-p1[0]), dz=2*u*(p1[2]-p0[2])+2*e*(p2[2]-p1[2]);
        yaw=Math.atan2(dx,dz);
      }
      const cy=Math.cos(yaw), sy=Math.sin(yaw);
      const lx=o2[0]+Math.sin(t*2.1+i)*0.05, lz=o2[1];
      dm.position.set(px+lx*cy+lz*sy, py+Math.sin(t*3.3+i*1.3)*0.12, pz-lx*sy+lz*cy);
      dm.rotation.set(0,yaw,Math.sin(t*9.5+i*1.7)*0.42);
      dm.scale.setScalar(sc);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* 锦书虚影：半透绢帛 + 双卷轴 + 月晕微光（「云中谁寄锦书来」的想象；初值=最大透明度） */
function makeJinshu(o){
  o=o||{};
  const g=new THREE.Group();
  const silkMat=new THREE.MeshBasicMaterial({color:0xdfe8f6,transparent:true,opacity:0.5,
    depthWrite:false,side:THREE.DoubleSide});
  const silk=new THREE.Mesh(new THREE.PlaneGeometry(1.5,1.05),silkMat); silk.renderOrder=2; g.add(silk);
  const B=new GeoBag();
  [1,-1].forEach(function(s){
    const r=new THREE.CylinderGeometry(0.055,0.055,1.16,7); r.rotateZ(Math.PI/2);
    r.translate(s*0.78,0,0); B.put(r,0x39435a);
  });
  const roller=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a465c,emissive:0x06080f}),{c:0xb4c2d4,i:0.35,p:2.4}));
  roller.renderOrder=2; g.add(roller);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc9d6ec,
    transparent:true,opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(4.2,3.4,1); glow.renderOrder=3; g.add(glow);
  return {g,silkMat,glow,roller,update(t,k){
    silkMat.opacity=k*(0.26+0.10*Math.sin(t*1.1));
    glow.material.opacity=k*(0.16+0.08*Math.sin(t*0.9+0.5));
  }};
}

/* 水中月影：两片叠加的加色光盘（长椭圆倒影），随波呼吸 —— 两地同望的这一轮月 */
function makeYueying(o){
  o=o||{};
  const g=new THREE.Group();
  const mat=new THREE.MeshBasicMaterial({map:glowTex(),color:o.color===undefined?0xcfe0f4:o.color,
    transparent:true,opacity:0.46,depthWrite:false,blending:THREE.AdditiveBlending});
  const m1=new THREE.Mesh(new THREE.PlaneGeometry(1,1),mat);
  m1.rotation.x=-Math.PI/2; m1.scale.set(9,26,1); m1.renderOrder=2; g.add(m1);
  const mat2=new THREE.MeshBasicMaterial({map:glowTex(),color:0xe4edfa,
    transparent:true,opacity:0.6,depthWrite:false,blending:THREE.AdditiveBlending});
  const m2=new THREE.Mesh(new THREE.PlaneGeometry(1,1),mat2);
  m2.rotation.x=-Math.PI/2; m2.scale.set(4.2,10,1); m2.renderOrder=2; g.add(m2);
  return {g,update(t,k){
    mat.opacity=k*(0.36+0.10*Math.sin(t*0.5));
    mat2.opacity=k*(0.44+0.16*Math.sin(t*0.5+1.3));
  }};
}

function bCover(){ // 封面 · 荷塘月夜 —— 残荷、空舟与远处西楼
  const g=new THREE.Group();
  const water=makeWater({size:320,seg:80,amp:0.14,freq:0.18,speed:0.36,flow:[0.1,0.35],spec:1.5,
    deep:0x0a0f18,shallow:0x16202f,skyc:0x1e2c40,moonDir:[20,105,-182]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:18,layers:2,peaks:5,seed:1881,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-112); g.add(ridge.g);
  const lou=makeXilou({rim:0.2}); lou.g.position.set(-26,0,-58); lou.g.rotation.y=0.3; lou.g.scale.setScalar(0.75); g.add(lou.g);
  const he1=makeCanhe({seed:1882,n:10,w:10,hong:2}); he1.g.position.set(-6,0,-22); g.add(he1.g);
  const he2=makeCanhe({seed:1883,n:8,w:8,hong:1}); he2.g.position.set(9,0,-27); g.add(he2.g);
  const boat=makeLanzhou(); boat.position.set(5,0.16,-17); boat.rotation.y=-0.4; g.add(boat);
  const fgReedL=makeForeground({kind:'芦苇',w:22,n:11,d:6,color:0x04060a,seed:1884,sway:0.8});
  fgReedL.g.position.set(-13,-1.2,26); g.add(fgReedL.g);
  const fgRockR=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1885,rim:0.14});
  fgRockR.g.position.set(14,-1.6,30); g.add(fgRockR.g);
  const mist=makeMist({n:7,spread:[230,24,130],pos:[0,10,-55],scale:76,color:0x8fa0ba,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:56,box:[190,34,110],pos:[0,11,-42],color:0xa8b8d0,size:6.5,speed:0.05,rise:0,maxA:0.3});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.42,p:[-30,80,-40]},{c:0x18202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    boat.position.y=0.16+0.05*Math.sin(t*0.85);
    boat.rotation.z=0.02*Math.sin(t*0.7);
    lou.lamp.material.opacity=k*(0.12+0.04*Math.sin(t*0.8));
    fgReedL.update(t,k); fgRockR.update(t,k);
  }};
}

function bHongou(){ // 一 · 红藕兰舟 —— 红藕香残玉簟秋，轻解罗裳、独上兰舟
  const g=new THREE.Group();
  const water=makeWater({size:320,seg:84,amp:0.15,freq:0.20,speed:0.4,flow:[0.12,0.4],spec:1.6,
    deep:0x0a0f18,shallow:0x17212f,skyc:0x20304a,moonDir:[28,110,-172]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:17,layers:2,peaks:5,seed:1886,color:0x070a10,atmo:0x1c2433,fogK:0.61,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-124); g.add(ridge.g);
  /* 兰舟 + 独上兰舟的思妇（同组随波轻荡） */
  const boat=makeLanzhou({scale:1.15}); boat.position.set(2.5,0.18,-24); boat.rotation.y=0.14; g.add(boat);
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x55627c,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xb4c2d4,rim:0.52,noProp:true,scale:1.4});
  fig.position.set(0.45,0.34,-0.15); fig.rotation.y=-0.3; boat.add(fig);
  /* 残荷三丛：秋深荷塘（红藕香残） */
  const he1=makeCanhe({seed:1887,n:11,w:11,hong:3}); he1.g.position.set(-8.5,0,-16); g.add(he1.g);
  const he2=makeCanhe({seed:1888,n:9,w:9,hong:2}); he2.g.position.set(9,0,-20); g.add(he2.g);
  const he3=makeCanhe({seed:1889,n:8,w:12,hong:2,rim:0.14}); he3.g.position.set(-2,0,-31); g.add(he3.g);
  /* 水面残红漂瓣 */
  const ban=makeLianban({n:90,box:[80,1.4,52],pos:[0,0.08,-19]}); g.add(ban.points);
  const fgReed=makeForeground({kind:'芦苇',w:24,n:12,d:6,color:0x04060a,seed:1890,sway:0.9});
  fgReed.g.position.set(-13,-1.2,12); g.add(fgReed.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:1891,rim:0.14});
  fgRock.g.position.set(13.5,-1.5,10); g.add(fgRock.g);
  const mist=makeMist({n:6,spread:[210,22,120],pos:[0,9,-52],scale:74,color:0x8fa0ba,op:0.075});
  g.add(mist.g);
  const motes=makeGlow({n:52,box:[150,22,80],pos:[0,9,-30],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.46,p:[30,85,-30]},{c:0x18202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    ban.update(t);
    boat.position.y=0.18+0.055*Math.sin(t*0.85);
    boat.rotation.z=0.022*Math.sin(t*0.66);
    boat.rotation.x=0.014*Math.sin(t*0.5+1.0);
    fig.userData.update(t,k);
    fgReed.update(t,k); fgRock.update(t,k);
  },onEnter(){ pluck(1,0.2,0.13); pluck(3,0.8,0.09); }};
}

function bYanzi(){ // 二 · 雁字西楼（标志性瞬间）—— 云中谁寄锦书来？雁字回时，月满西楼
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:84,amp:0.15,freq:0.17,speed:0.38,flow:[0.1,0.4],spec:1.7,
    deep:0x0a0f18,shallow:0x182435,skyc:0x22334a,moonDir:[40,120,-170]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:1892,color:0x070a10,atmo:0x1e2636,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-128); g.add(ridge.g);
  /* 西楼临水而立，楼上人凭栏望月 */
  const lou=makeXilou(); lou.g.position.set(-11,0,-32); lou.g.rotation.y=0.35; g.add(lou.g);
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x55627c,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xb4c2d4,rim:0.5,noProp:true,scale:1.12});
  fig.position.set(2.1,7.05,3.1); fig.rotation.y=0.9; lou.g.add(fig);
  /* 云中锦书虚影（盼书之念，悬于月旁）+ 雁阵巡天（周期掠月） */
  const shu=makeJinshu(); shu.g.position.set(13,30,-84); shu.g.rotation.y=-0.5;
  shu.g.scale.setScalar(2.3); g.add(shu.g);
  const yan=makeYanzhen({scale:2.6}); g.add(yan.mesh);
  /* 月前流云两缕 */
  const clouds=makeMist({n:4,spread:[70,10,36],pos:[34,116,-156],scale:40,color:0xb4bfda,op:0.06});
  g.add(clouds.g);
  const fgTree=makeForeground({kind:'树枝',n:2,w:18,d:5,color:0x04060a,seed:1893,sway:1.3,rim:0.16});
  fgTree.g.position.set(15,-0.5,26); g.add(fgTree.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1894,rim:0.14});
  fgRock.g.position.set(-14,-1.6,22); g.add(fgRock.g);
  const mist=makeMist({n:6,spread:[220,22,120],pos:[0,10,-55],scale:76,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  const motes=makeGlow({n:46,box:[160,26,90],pos:[0,11,-36],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.50,p:[40,90,-30]},{c:0x1a2230,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); clouds.update(t,k); motes.update(t);
    yan.update(t,k,null,true);
    shu.g.position.y=30+0.8*Math.sin(t*0.5);
    shu.g.rotation.z=0.04*Math.sin(t*0.33);
    shu.update(t,k);
    lou.lamp.material.opacity=k*(0.13+0.05*Math.sin(t*0.8));
    fig.userData.update(t,k);
    fgTree.update(t,k); fgRock.update(t,k);
  },onEnter(){ pluck(0,0.2,0.14); pluck(3,0.7,0.10); pluck(1,1.3,0.09); }};
}

function bHuashui(){ // 三 · 花水两愁 —— 花自飘零水自流，一种相思、两处闲愁（两地同月对切）
  const g=new THREE.Group();
  const water=makeWater({size:360,seg:88,amp:0.18,freq:0.15,speed:0.5,flow:[0.28,0.62],spec:1.5,
    deep:0x0a0f18,shallow:0x1a2638,skyc:0x243652,moonDir:[0,118,-178]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:14,layers:2,peaks:4,seed:1895,color:0x070a10,atmo:0x1e2636,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-130); g.add(ridge.g);
  /* 同望的一轮月：水中月影居中呼吸 */
  const yy=makeYueying(); yy.g.position.set(0,0.06,-46); g.add(yy.g);
  /* 两地对切：左·西楼凭栏的她；右·随流漂荡的他乡孤舟 */
  const lou=makeXilou({rim:0.2}); lou.g.position.set(-25,0,-48); lou.g.rotation.y=0.5; lou.g.scale.setScalar(0.85); g.add(lou.g);
  const she=makeFigure({pose:'独立',robe:0x232f44,belt:0x5d6a84,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xb4c2d4,rim:0.4,noProp:true,scale:0.95});
  she.position.set(1.9,7.05,3.0); she.rotation.y=0.8; lou.g.add(she);
  const boat=makeLanzhou({scale:1.2}); boat.position.set(23,0.18,-38); boat.rotation.y=-0.6; g.add(boat);
  const he=makeFigure({pose:'独立',robe:0x252c3c,belt:0x55627c,skin:0xd0bda6,collar:0xaab8cf,
    hat:'幞头',rimC:0xb4c2d4,rim:0.4,noProp:true,scale:1.2});
  he.position.set(0.3,0.36,-0.2); he.rotation.y=0.4; boat.add(he);
  /* 远岸人影（同在一方月下的村居） */
  const crowd=makeCrowd({n:5,rect:[-68,-64,44,10],seed:1896,color:0x10151f,rimC:0x8fa4c4,rim:0.10,sMin:0.4,sMax:0.55,y:0});
  g.add(crowd.mesh);
  /* 落花随水（花自飘零水自流）+ 愁绪东流的薄雾流 */
  const ban=makeLianban({n:110,box:[110,1.4,80],pos:[0,0.08,-30],size:3.0}); g.add(ban.points);
  const flow=makeFlow({n:90,box:[120,12,44],pos:[0,8,-44],color:0x9fb0c8,size:20,speed:1.6,maxA:0.12});
  g.add(flow.points);
  const fgReedL=makeForeground({kind:'芦苇',w:24,n:12,d:6,color:0x04060a,seed:1897,sway:0.9});
  fgReedL.g.position.set(-14,-1.2,16); g.add(fgReedL.g);
  const fgReedR=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x04060a,seed:1898,sway:1.1});
  fgReedR.g.position.set(15,-1.4,14); g.add(fgReedR.g);
  const mist=makeMist({n:6,spread:[230,22,130],pos:[0,10,-58],scale:78,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[170,24,90],pos:[0,10,-34],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.2});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.48,p:[0,95,-40]},{c:0x1a2230,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    ban.update(t); flow.update(t); crowd.update(t);
    yy.update(t,k);
    boat.position.x=23+2.6*Math.sin(t*0.045);
    boat.position.z=-38+1.6*Math.sin(t*0.032+1.2);
    boat.position.y=0.18+0.05*Math.sin(t*0.8);
    boat.rotation.y=-0.6+0.05*Math.sin(t*0.07);
    boat.rotation.z=0.02*Math.sin(t*0.6);
    she.userData.update(t,k); he.userData.update(t,k);
    fgReedL.update(t,k); fgReedR.update(t,k);
  },onEnter(){ pluck(2,0.2,0.12); pluck(4,0.9,0.09); }};
}

function bMeitou(){ // 四（末境·可点击）· 眉间心头 —— 此情无计可消除；点击：雁字掠月、锦书浮来终是影
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0};
  const water=makeWater({size:340,seg:84,amp:0.15,freq:0.17,speed:0.4,flow:[0.14,0.42],spec:1.6,
    deep:0x0a0f18,shallow:0x182435,skyc:0x22334a,moonDir:[-30,62,-150]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:1899,color:0x070a10,atmo:0x1e2636,fogK:0.59,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-126); g.add(ridge.g);
  /* 楼头平台：凭栏的她（才下眉头）+ 心口一点微光（却上心头） */
  const terrace=makeTerrace(); terrace.g.position.set(0,0,-14); terrace.g.rotation.y=0.06; g.add(terrace.g);
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x55627c,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xb4c2d4,rim:0.55,noProp:true,scale:1.6});
  fig.position.set(1.15,0.52,-0.7); fig.rotation.y=0.45; terrace.g.add(fig);
  const pl=new THREE.PointLight(0xbdd0ea,0.30,10); pl.position.set(1.15,3.8,-13.4); g.add(pl);
  /* 楼下荷塘一角（回望红藕）+ 漂瓣 */
  const he1=makeCanhe({seed:1900,n:9,w:10,hong:2,rim:0.16}); he1.g.position.set(-7,0,-26); g.add(he1.g);
  const he2=makeCanhe({seed:1901,n:7,w:9,hong:1,rim:0.14}); he2.g.position.set(8,0,-30); g.add(he2.g);
  const ban=makeLianban({n:60,box:[70,1.2,44],pos:[0,0.08,-26],size:2.6}); g.add(ban.points);
  /* 点击之后：雁阵掠月 + 锦书虚影浮来（终是影） */
  const yan=makeYanzhen({scale:2.6}); g.add(yan.mesh);
  const shu=makeJinshu(); shu.g.position.set(-26,50,-138); shu.g.scale.setScalar(2.4); shu.g.rotation.y=0.5; g.add(shu.g);
  const fgTree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:1902,sway:1.3,rim:0.16});
  fgTree.g.position.set(14,-0.5,10); g.add(fgTree.g);
  const fgReed=makeForeground({kind:'芦苇',w:20,n:10,d:5,color:0x04060a,seed:1903,sway:0.8});
  fgReed.g.position.set(-13,-1.4,12); g.add(fgReed.g);
  const mist=makeMist({n:5,spread:[220,22,120],pos:[0,10,-54],scale:76,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  const motes=makeGlow({n:42,box:[150,24,80],pos:[0,10,-32],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.2});
  g.add(motes.points);
  addLights(g,{c:0x9fb0cc,i:0.42,p:[26,60,36]},{c:0x1a2232,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const el=ctl.clicked?ctl.t-ctl.clickT:0;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      ban.update(t);
      yan.update(t,k,ctl.clicked?el/5.2:0,ctl.clicked);
      /* 锦书虚影：自月旁雾中浮来，近人渐淡——锦书终是影 */
      if(ctl.clicked){
        const e=ease(clamp(el/9,0,1));
        shu.g.position.set(-26+26.5*e, 50-42*e, -138+122*e);
        const fade=el<1.5?el/1.5:(el<6?1:Math.max(0,1-(el-6)/3));
        shu.silkMat.opacity=k*fade*0.5;
        shu.glow.material.opacity=k*fade*0.30;
        shu.roller.visible=true;
      }else{
        shu.silkMat.opacity=0; shu.glow.material.opacity=0; shu.roller.visible=false;
      }
      terrace.win.material.opacity=k*(0.11+0.04*Math.sin(t*0.8));
      pl.intensity=k*(0.20+0.06*Math.sin(t*1.4)+(ctl.clicked?0.04*Math.abs(Math.sin(el*2.2)):0));
      fig.userData.update(t,k);
      fgTree.update(t,k); fgReed.update(t,k);
    },onEnter(){ pluck(1,0.2,0.12); pluck(3,0.8,0.09); },
    click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(3,0.05,0.13); pluck(1,0.35,0.11); pluck(5,0.7,0.10); pluck(2,1.1,0.09);
        const fl=$('#flash'); fl.textContent='雁字回时'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111825),fd:0.0055,star:0.35,
  moon:new THREE.Vector3(40,112,-180),ms:1.8,mph:0.04,mhaze:0.04,dirC:C(0x8fa4c4),dirI:0.48,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x19202e),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,6.5,40],t:[0,7.0,37],lf:[0,8,-30],lt:[0,9,-34]},
  sky:()=>SK({top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x10161f),fd:0.0050,star:0.38,
    ms:1.7,mph:0.02,moon:new THREE.Vector3(20,105,-182),
    dirC:C(0x8fa4c4),dirI:0.44,ambC:C(0x182031),ambI:0.62}) },
{ name:'红藕兰舟',dwell:16,river:0.03,build:bHongou,
  cam:{f:[0,3.4,6],t:[0.7,3.2,3],lf:[2,4.6,-24],lt:[2.2,4.4,-26]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x161e2c),bot:C(0x090c12),fog:C(0x121926),fd:0.0062,star:0.30,
    ms:1.8,mph:0.04,moon:new THREE.Vector3(28,110,-172),
    dirC:C(0x8fa4c4),dirI:0.46,ambC:C(0x19202e),ambI:0.6}) },
{ name:'雁字西楼',dwell:18,river:0.03,build:bYanzi,
  cam:{f:[4,5.5,16],t:[5,6.5,13],lf:[-6,13,-31],lt:[-5,14,-33]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x171f2e),bot:C(0x090c12),fog:C(0x121926),fd:0.0058,star:0.26,
    ms:2.05,mph:0.06,mhaze:0.05,moon:new THREE.Vector3(40,120,-170),
    dirC:C(0x8fa4c4),dirI:0.52,ambC:C(0x1a2230),ambI:0.58}) },
{ name:'花水两愁',dwell:18,river:0.05,build:bHuashui,
  cam:{f:[0,4.6,20],t:[0,4.4,17],lf:[0,7,-44],lt:[0,6.6,-48]},
  sky:()=>SK({top:C(0x090c14),hor:C(0x181f2d),bot:C(0x090c11),fog:C(0x131a26),fd:0.0066,star:0.22,
    ms:1.9,mph:0.05,moon:new THREE.Vector3(0,118,-178),
    dirC:C(0x8fa4c4),dirI:0.48,ambC:C(0x1a2230),ambI:0.58}) },
{ name:'眉间心头',dwell:20,river:0.03,build:bMeitou,
  cam:{f:[0,5.2,3],t:[0.4,5.0,0.5],lf:[0,4.8,-14],lt:[0.4,5.0,-16]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x171f2e),bot:C(0x090c12),fog:C(0x121926),fd:0.0056,star:0.30,
    ms:1.95,mph:0.06,moon:new THREE.Vector3(-30,62,-150),
    dirC:C(0x9fb0cc),dirI:0.44,dirP:new THREE.Vector3(-20,50,-120),ambC:C(0x1a2232),ambI:0.62}) },
];
"""
