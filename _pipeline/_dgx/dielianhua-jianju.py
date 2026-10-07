# -*- coding: utf-8 -*-
"""dielianhua-jianju.py —— 《蝶恋花·槛菊愁烟兰泣露》（宋·晏殊，no.165，水墨夜思）生成配置
两境：月穿朱户（槛菊罗幕·燕去·明月到晓）、独上高楼（西风凋碧树·望尽天涯，王国维第一境；
点击登楼：镜头升高望尽天涯）。"""
import io, os
def io_open(n):
    return io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), n), encoding='utf-8').read()

META = dict(
    N=2, slug='dielianhua-jianju', title='蝶恋花·槛菊愁烟兰泣露', dyn='宋 · 晏殊', brand_author='晏 殊',
    gold_rgb='154,184,216',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#9ab8d8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(154,184,216,.26);
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
    tip='轻点画面 / 按空格 —— 独上高楼，望尽天涯路',
    hint='← → 键或空格逐境游览 · 末境可点击登楼，望尽天涯路',
    cover_read='蝶恋花。宋，晏殊。槛菊愁烟兰泣露，罗幕轻寒，燕子双飞去。明月不谙离恨苦，斜光到晓穿朱户。',
    cover_p1='两重意境，随词句次第展开：槛菊含愁、兰草泣露，燕子双双飞去，明月不谙离恨，斜光到晓穿朱户；昨夜西风凋尽碧树，独上高楼望尽天涯路，末了山长水阔，彩笺尺素竟不知寄往何处。',
    cover_p2='边读词，边走进晏殊笔下这条被王国维借作「治学第一境」的望远之路。',
    end_h2='望尽 · 天涯', cn_word='两',
    words_js="['再游一次，重上高楼','初识晏殊，尚需共读','渐入佳境，再诵几遍','词境渐深，月到朱户','已谙离恨，细味轻寒','望尽天涯，第一境成']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'月穿朱户', jing:'槛菊含愁，兰草泣露；燕子双飞去后，明月不谙离恨，斜光到晓，穿朱户而不言人。（罗幕 · 燕去 · 月光）',
  segs:[
   {c:'槛菊愁烟兰泣露，', p:py('jiàn jú chóu yān lán qì lù')},
   {c:'罗幕轻寒，', p:py('luó mù qīng hán')},
   {c:'燕子双飞去。', p:py('yàn zi shuāng fēi qù')},
   {c:'明月不谙离恨苦，', p:py('míng yuè bù ān lí hèn kǔ')},
   {c:'斜光到晓穿朱户。', p:py('xié guāng dào xiǎo chuān zhū hù')}],
  read:'槛菊愁烟兰泣露，罗幕轻寒，燕子双飞去。明月不谙离恨苦，斜光到晓穿朱户。',
  yisi:'栏杆外的菊花笼在愁雾里，兰草叶尖露珠如泪；罗幕之间透着轻轻的寒意，燕子已成双成对飞走了。明月不懂得离别的恨苦，只顾把斜斜的光透过朱红的门户，一直照到天亮——照着那个彻夜无眠的人。',
  zhu:[['槛','栏杆（读 jiàn）；槛菊即栏杆边的菊花'],['罗幕','丝罗的帷幕，富贵人家所居；「轻寒」是秋夜幕内微寒，人在不言中'],['谙','熟悉、体味（读 ān）；「不谙」即不解、不懂得，怨月正见离恨之深'],['朱户','朱红色的门户，指富贵人家；月光彻夜穿户，人亦彻夜无眠']] },
{ name:'独上高楼', jing:'西风凋树，独上高楼；望尽天涯路尽处——山长水阔，所思竟不知何处。（点击登楼望远）',
  segs:[
   {c:'昨夜西风凋碧树，', p:py('zuó yè xī fēng diāo bì shù')},
   {c:'独上高楼，', p:py('dú shàng gāo lóu')},
   {c:'望尽天涯路。', p:py('wàng jìn tiān yá lù')},
   {c:'欲寄彩笺兼尺素，', p:py('yù jì cǎi jiān jiān chǐ sù')},
   {c:'山长水阔知何处。', p:py('shān cháng shuǐ kuò zhī hé chù')}],
  read:'昨夜西风凋碧树，独上高楼，望尽天涯路。欲寄彩笺兼尺素，山长水阔知何处。',
  yisi:'昨夜西风劲吹，把碧树的叶子凋落殆尽；今晨独自登上高楼，望着那条通向天边的长路，一眼望到路的尽头。想给远方的人寄一封彩笺、一尺素帛，可是山长水阔——他究竟在什么地方呢？',
  zhu:[['凋','凋零、使落叶（读 diāo）；西风凋碧树，一「凋」字尽写秋风肃杀'],['彩笺兼尺素','彩笺是题诗的精美笺纸，尺素是写信的素帛，皆指书信；「兼」是加之、连同'],['天涯路','通向天边的长路；望尽天涯而不见人，离恨更深一层'],['治学第一境','王国维《人间词话》引「昨夜西风」三句，喻古今成大事业、大学问者必经的第一境：登高望远，看清方向']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「槛菊愁烟兰泣露」的下一句是？', o:['罗幕轻寒，燕子双飞去','明月不谙离恨苦，斜光到晓穿朱户','昨夜西风凋碧树'], a:0},
 {q:'「昨夜西风凋碧树」的下一句是？', o:['欲寄彩笺兼尺素','独上高楼，望尽天涯路','山长水阔知何处'], a:1},
 {q:'「明月不谙离恨苦」中「谙」的正确读音与意思是？', o:['ān，熟悉、体味','kǎn，门槛','àn，昏暗'], a:0},
 {q:'王国维借本词哪一句比喻「古今成大事业、大学问者的第一境」？', o:['槛菊愁烟兰泣露','欲寄彩笺兼尺素','独上高楼，望尽天涯路'], a:2},
 {q:'上片「明月不谙离恨苦，斜光到晓穿朱户」表达的主要情感是？', o:['秋夜赏月的闲适','离人彻夜难眠、离恨难遣的孤苦','登高怀古的兴亡之叹'], a:1},
];
"""

SCENES_JS = """/* ================= 蝶恋花 · 两境场景（水墨夜思：月穿朱户、独上高楼） ================= */

/* 朱楼：临水小楼，下层朱户（全页唯一暖色字面），上层格子窗 + 檐廊栏杆，合批 1 mesh */
function makeZhulou(){
  const B=new GeoBag(), c1=0x0d1219, c2=0x111825, c3=0x161d2b, c4=0x1a2230, red=0x5e2823;
  const base=new THREE.BoxGeometry(12,1.0,8); base.translate(0,0.5,0); B.put(base,c1);
  const hall=new THREE.BoxGeometry(7.5,6.5,5.6); hall.translate(-0.5,1.0+3.25,0); B.put(hall,c2);
  const roof1=new THREE.ConeGeometry(6.4,2.0,4); roof1.rotateY(Math.PI/4);
  roof1.scale(1.3,1,1.1); roof1.translate(-0.5,7.5+1.0,0); B.put(roof1,c3);
  const upper=new THREE.BoxGeometry(5.0,4.2,4.2); upper.translate(-0.5,9.5+2.1,0); B.put(upper,c2);
  const roof2=new THREE.ConeGeometry(4.4,1.7,4); roof2.rotateY(Math.PI/4);
  roof2.scale(1.22,1,1.05); roof2.translate(-0.5,13.7+0.85,0); B.put(roof2,c3);
  /* 朱户：门扇 + 门框 + 三级台阶 */
  const door=new THREE.BoxGeometry(2.2,4.6,0.3); door.translate(-0.5,1.0+2.3,2.86); B.put(door,red);
  [-1.35,1.35].forEach(function(dx){
    const post=new THREE.BoxGeometry(0.22,4.9,0.24); post.translate(-0.5+dx,1.0+2.45,2.88); B.put(post,c4);
  });
  const lintel=new THREE.BoxGeometry(2.9,0.34,0.28); lintel.translate(-0.5,1.0+4.75,2.88); B.put(lintel,c4);
  [0,1,2].forEach(function(s){
    const step=new THREE.BoxGeometry(3.0-s*0.5,0.28,1.0); step.translate(-0.5,0.85-s*0.28,3.4+s*0.62); B.put(step,c1);
  });
  /* 上层格窗 + 檐廊小栏杆 */
  const win=new THREE.BoxGeometry(2.4,1.8,0.18); win.translate(-0.5,9.5+2.0,2.18); B.put(win,0x0e141f);
  [-0.7,0,0.7].forEach(function(dx){
    const slat=new THREE.BoxGeometry(0.1,1.7,0.22); slat.translate(-0.5+dx+0.0,11.5,2.2); B.put(slat,c4);
  });
  for(let i=0;i<5;i++){
    const post=new THREE.BoxGeometry(0.1,0.9,0.1); post.translate(-3.0+i*1.25,9.5+0.75,2.4); B.put(post,c4);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x9ab8d8,i:0.32,p:2.5})));
  return g;
}

/* 槛菊 + 兰：低栏一列 + 栏下菊丛 + 阶前兰草（叶尖带露），合批 1 mesh */
function makeJianLan(){
  const B=new GeoBag(), c1=0x0b0f16, c2=0x141a26;
  for(let i=0;i<10;i++){
    const x=-24+i*2.2;
    const post=new THREE.BoxGeometry(0.14,1.5,0.14); post.translate(x,0.75,-10.5); B.put(post,c1);
  }
  [0.8,1.4].forEach(function(y){
    const rail=new THREE.BoxGeometry(21.0,0.09,0.09); rail.translate(-13.5,y,-10.5); B.put(rail,c2);
  });
  const R=seedRnd(16511);
  for(let i=0;i<8;i++){
    const x=-23.5+i*2.7+ (R()-0.5), z=-10.5+0.9+R()*1.1;
    for(let k=0;k<3;k++){
      const bloom=new THREE.IcosahedronGeometry(0.30+R()*0.16,0);
      bloom.scale(1,0.72,1); bloom.translate(x+(R()-0.5)*0.7,1.9+R()*0.55,z+(R()-0.5)*0.7);
      B.put(bloom,R()<0.5?0x8d9ab5:0x77879f);
    }
  }
  /* 兰：阶前侧一丛细叶 + 两茎淡花 */
  for(let i=0;i<7;i++){
    const leaf=new THREE.ConeGeometry(0.09,2.0+R()*0.8,4);
    leaf.rotateZ((R()-0.5)*1.1); leaf.rotateX((R()-0.5)*0.8);
    leaf.translate(-9.5+(R()-0.5)*1.2,1.1,-16.5+(R()-0.5)*1.0); B.put(leaf,0x24354a);
  }
  [0,1].forEach(function(s){
    const spike=new THREE.ConeGeometry(0.14,0.6,5);
    spike.translate(-9.2+s*0.9,2.3,-16.2+s*0.5); B.put(spike,0x9fb3d0);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.26,p:2.4})));
  return g;
}

/* 燕影：身 + 双翅 + 剪尾，合批 1 mesh（返回 mesh，飞行路径在 update 里驱动） */
function makeSwallow(){
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.5,7,5); body.scale(1.0,0.34,0.30); B.put(body,0x0a0e15);
  [-1,1].forEach(function(s){
    const wing=new THREE.BoxGeometry(1.05,0.05,0.34);
    wing.rotateZ(s*0.42); wing.translate(s*0.55,0.10,0); B.put(wing,0x0c1017);
  });
  [-1,1].forEach(function(s){
    const tail=new THREE.BoxGeometry(0.42,0.04,0.07);
    tail.rotateZ(s*0.30); tail.translate(-0.62,-0.02,s*0.09); B.put(tail,0x0a0e15);
  });
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.20,p:2.4}));
  return mesh;
}

/* 斜光着色器：明月斜穿朱户的光柱（到晓缓移，冷银，唯一自定义着色器） */
const BEAM_VERT='varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }';
const BEAM_FRAG=[
'uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;',
'void main(){',
'  float across=smoothstep(0.0,0.40,vUv.x)*smoothstep(1.0,0.60,vUv.x);',
'  float along=0.30+0.70*(1.0-vUv.y);',
'  float sway=0.86+0.14*sin(uTime*0.8+vUv.x*7.0);',
'  vec3 col=vec3(0.74,0.82,0.95);',
'  gl_FragColor=vec4(col,uFade*uK*across*along*sway);',
'}'].join('\\n');

function bCover(){ // 封面 · 墨夜庭苑
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:22,layers:2,peaks:4,seed:1650,color:0x070a10,atmo:0x1f2a3d,fogK:0.72,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  /* 远处楼影（末境高楼之伏笔）+ 楼下一位望远人影 */
  const B=new GeoBag(), c1=0x0c1017, c2=0x10151f;
  const b1=new THREE.BoxGeometry(5.5,10.5,5.0); b1.translate(0,5.25,0); B.put(b1,c1);
  const b2=new THREE.BoxGeometry(3.8,4.4,3.6); b2.translate(0,10.5+2.2,0); B.put(b2,c2);
  const rf=new THREE.ConeGeometry(3.6,1.5,4); rf.rotateY(Math.PI/4);
  rf.translate(0,14.9+0.75,0); B.put(rf,c2);
  const farlou=new THREE.Group();
  farlou.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.2,p:2.4})));
  farlou.position.set(-30,0,-64); g.add(farlou);
  const farman=makeFigure({pose:'独立',robe:0x141c28,belt:0x3c4a60,skin:0xb5a792,collar:0x94a4bc,
    hat:'幞头',rimC:0x8fa4c4,rim:0.3,noProp:true,scale:0.85});
  farman.position.set(-25.5,0,-58); farman.rotation.y=0.5; g.add(farman);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:1651,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const tree=makeForeground({kind:'树枝',n:2,w:15,d:5,color:0x04060a,seed:1652,sway:1.1,rim:0.16});
  tree.g.position.set(15,-1.5,24); g.add(tree.g);
  const mist=makeMist({n:9,spread:[240,34,160],pos:[0,11,-55],scale:82,color:0x8fa4c4,op:0.085});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[210,38,120],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.38});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); tree.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bZhuHu(){ // 一 · 月穿朱户 —— 槛菊罗幕、燕子双飞、斜光到晓穿朱户
  const g=new THREE.Group(), st={t:0};
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-0.4; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:18,layers:2,peaks:4,seed:1653,color:0x070a10,atmo:0x1f2a3d,fogK:0.64,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 朱楼（左）+ 楼头窗月微光（冷银） */
  const lou=makeZhulou(); lou.position.set(-13,0,-24); lou.rotation.y=0.14; g.add(lou);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.27,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(4.0,4.0,1); win.position.set(-13.5,11.6,-21.4); win.renderOrder=2; g.add(win);
  /* 斜光穿朱户：光柱 + 地面光池（到晓缓移） */
  const beamMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.50}},
    vertexShader:BEAM_VERT,fragmentShader:BEAM_FRAG});
  const S=new THREE.Vector3(-12.4,5.0,-21.0), E=new THREE.Vector3(-6.0,0.5,-11.2);
  const beam=new THREE.Mesh(new THREE.PlaneGeometry(5.0,13.6),beamMat);
  beam.position.copy(S.clone().add(E).multiplyScalar(0.5));
  beam.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),E.clone().sub(S).normalize());
  beam.renderOrder=2; g.add(beam);
  const poolMat=new THREE.MeshBasicMaterial({color:0x8fa4c8,transparent:true,opacity:0.22,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const pool=new THREE.Mesh(new THREE.CircleGeometry(2.8,20),poolMat);
  pool.rotation.x=-Math.PI/2; pool.position.set(E.x,0.42,E.z); pool.renderOrder=2; g.add(pool);
  /* 光柱里的浮尘 + 兰上露珠微闪 */
  const dust=makeGlow({n:40,box:[6,9,8],pos:[-9.3,3.0,-15.8],color:0xcfdcf0,size:4.5,speed:0.05,rise:0.05,maxA:0.5});
  g.add(dust.points);
  const dew=makeGlow({n:16,box:[2.6,1.4,1.8],pos:[-9.5,1.0,-16.5],color:0xdde9fa,size:2.5,speed:0.02,rise:0,maxA:0.32});
  g.add(dew.points);
  /* 槛菊（栏杆一列 + 菊丛）与阶前兰 */
  const jian=makeJianLan(); jian.position.set(0,0,0); g.add(jian);
  /* 罗幕：门侧一帔轻纱 */
  const curtain=makeCurtain({w:5.4,h:5.2,color:0x2a3448,dark:0x131a28,folds:6,deep:0.5});
  curtain.g.position.set(-19.6,1.0,-20.2); curtain.g.rotation.y=0.14; g.add(curtain.g);
  /* 燕子双飞去：双双辞梁，径向天际 */
  const sw1=makeSwallow(); g.add(sw1);
  const sw2=makeSwallow(); g.add(sw2);
  const SW=[{m:sw1,d:0,s0:[-8.5,8.0,-16],s1:[-36,46,-118]},{m:sw2,d:1.6,s0:[-7.0,7.2,-15],s1:[-32,43,-114]}];
  /* 思妇：独立栏边，仰望明月 */
  const figure=makeFigure({pose:'独立',robe:0x202c40,belt:0x57688a,skin:0xcbb9a2,collar:0xbcc9dc,
    hat:'发髻',rimC:0x9ab8d8,rim:0.55,noProp:true,scale:1.5});
  figure.position.set(-4.6,1.5,-13.0); figure.rotation.y=-0.6; g.add(figure);
  const mist=makeMist({n:7,spread:[210,20,105],pos:[0,7,-52],scale:76,color:0x7e8ea8,op:0.075});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:1654,rim:0.14});
  rk.g.position.set(13,-1.2,14); g.add(rk.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:1655,sway:1.2,rim:0.18});
  tree.g.position.set(-17,-0.5,12); g.add(tree.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[30,90,-30]},{c:0x1a2232,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      st.t+=dt;
      ridge.update(t,0); mist.update(t,k); dust.update(t); dew.update(t);
      rk.update(t,k); tree.update(t,k);
      beamMat.uniforms.uTime.value=t; beamMat.uniforms.uFade.value=k;
      poolMat.opacity=k*(0.16+0.06*Math.sin(t*0.6));
      pool.position.x=E.x+0.7*Math.sin(t*0.045);
      win.material.opacity=k*(0.20+0.07*Math.sin(t*0.7));
      for(let i=0;i<SW.length;i++){
        const w=SW[i], q=Math.min(1,Math.max(0,(st.t-w.d)/48)), e=q*q*(3-2*q);
        w.m.position.set(
          w.s0[0]+(w.s1[0]-w.s0[0])*e,
          w.s0[1]+(w.s1[1]-w.s0[1])*e+6*Math.sin(Math.PI*Math.min(1,q*0.9)),
          w.s0[2]+(w.s1[2]-w.s0[2])*e);
        w.m.scale.setScalar(1-0.78*e);
        w.m.rotation.z=0.16*Math.sin(t*7+i*2.1);
      }
    }};
}

/* 凋树：一夜西风后的碧树——疏枝横斜，残叶无几，合批 1 mesh */
function makeDiaoshu(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?7:o.seed);
  const h=o.h===undefined?8:o.h, x0=0, z0=0;
  const trunk=new THREE.CylinderGeometry(0.16,0.34,h*0.6,6);
  trunk.rotateZ((R()-0.5)*0.24); trunk.translate(x0,h*0.3,z0); B.put(trunk,0x0a0d13);
  const nb=5+Math.floor(R()*2);
  const trunkTop=new THREE.Vector3(x0,h*0.6,z0);
  for(let i=0;i<nb;i++){
    const a=i/nb*Math.PI*2+R(), up=0.5+R()*0.8, len=h*(0.32+R()*0.24);
    const tip=new THREE.Vector3(x0+Math.cos(a)*len*0.8,h*0.6+up*len*0.55,z0+Math.sin(a)*len*0.55);
    const dir=tip.clone().sub(trunkTop);
    const seg1=new THREE.CylinderGeometry(0.05,0.10,dir.length(),5);
    seg1.applyMatrix4(new THREE.Matrix4().makeRotationFromQuaternion(
      new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0,1,0),dir.clone().normalize())));
    seg1.translate(trunkTop.x+dir.x*0.5,trunkTop.y+dir.y*0.5,trunkTop.z+dir.z*0.5); B.put(seg1,0x0c1017);
    const twig=new THREE.CylinderGeometry(0.025,0.05,len*0.5,4);
    const dir2=dir.clone().normalize(); dir2.x+= (R()-0.5)*0.7; dir2.z+=(R()-0.5)*0.7; dir2.normalize();
    twig.applyMatrix4(new THREE.Matrix4().makeRotationFromQuaternion(
      new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0,1,0),dir2)));
    twig.translate(tip.x,tip.y,tip.z); B.put(twig,0x0d1119);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.2,p:2.4})));
  return g;
}

/* 高楼：三层危楼 + 顶层平台栏杆（独上高楼处），合批 1 mesh */
function makeGaolou(){
  const B=new GeoBag(), c1=0x0c1119, c2=0x101724, c3=0x151c2a, c4=0x1d2634;
  const base=new THREE.BoxGeometry(9,1.4,9); base.translate(0,0.7,0); B.put(base,c1);
  const t1=new THREE.BoxGeometry(6.2,7.0,6.2); t1.translate(0,1.4+3.5,0); B.put(t1,c2);
  const r1=new THREE.ConeGeometry(5.6,1.9,4); r1.rotateY(Math.PI/4);
  r1.scale(1.18,1,1.05); r1.translate(0,8.4+0.95,0); B.put(r1,c3);
  const t2=new THREE.BoxGeometry(4.6,4.2,4.6); t2.translate(0,10.3+2.1,0); B.put(t2,c2);
  const r2=new THREE.ConeGeometry(4.0,1.6,4); r2.rotateY(Math.PI/4);
  r2.scale(1.15,1,1.05); r2.translate(0,14.5+0.8,0); B.put(r2,c3);
  const deck=new THREE.BoxGeometry(5.8,0.5,5.8); deck.translate(0,16.1+0.25,0); B.put(deck,c1);
  for(let i=0;i<8;i++){
    const a=i/8*Math.PI*2;
    const post=new THREE.BoxGeometry(0.11,1.1,0.11);
    post.translate(Math.cos(a)*2.55,16.6+0.55,Math.sin(a)*2.55); B.put(post,c4);
  }
  const door=new THREE.BoxGeometry(1.8,3.4,0.24); door.translate(0,1.4+1.7,3.12); B.put(door,0x0a0e14);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0x9ab8d8,i:0.36,p:2.5})));
  return g;
}

/* 天涯长路：沿缓弯铺 12 段路面（自楼前直铺到水阔处），合批 1 mesh */
function makeTianyaRoad(){
  const B=new GeoBag();
  for(let i=0;i<12;i++){
    const z0=-38-i*7.4, z1=z0-7.4;
    const x0=4.6+1.8*Math.sin((z0+38)*0.05), x1=4.6+1.8*Math.sin((z1+38)*0.05);
    const seg=new THREE.PlaneGeometry(7.4,Math.hypot(x1-x0,z1-z0)+0.5);
    seg.rotateX(-Math.PI/2);
    seg.rotateY(Math.atan2(x1-x0,z1-z0));
    seg.translate((x0+x1)/2,0.12,(z0+z1)/2);
    B.put(seg,0x1a2333);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3650,emissive:0x04060a}),{c:0x9ab8d8,i:0.34,p:2.2})));
  return g;
}

function bGaolou(){ // 二（标志性瞬间·末境可点击）· 独上高楼 —— 西风凋碧树，点击登楼望尽天涯
  const g=new THREE.Group(), ctl={t:0,clicked:false,reveal:0};
  const grd=makeGround({r:105,c1:0x07090e,c2:0x10141d});
  grd.mesh.position.y=-0.4; grd.mesh.position.z=-25; g.add(grd.mesh);
  const ridge=makeRange({r:270,h:11,layers:2,peaks:3,seed:1656,color:0x080a10,atmo:0x202a3d,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 山长水阔：天际一带阔水（路尽于水） */
  const water=makeWater({size:320,seg:70,amp:0.3,freq:0.11,speed:0.5,flow:[0.4,0.1],spec:1.7,
    deep:0x081221,shallow:0x14304a,skyc:0x23405e,moonDir:[-44,112,-190]});
  water.mesh.position.set(0,-0.5,-118); g.add(water.mesh);
  /* 高楼 + 楼顶独立人影（背影向天涯） */
  const lou=makeGaolou(); lou.position.set(7,0,-40); g.add(lou);
  const figure=makeFigure({pose:'独立',robe:0x18222f,belt:0x4a5a74,skin:0xc4b39c,collar:0xa9b8ce,
    hat:'幞头',rimC:0x9ab8d8,rim:0.5,noProp:true,scale:1.15});
  figure.position.set(7,16.6,-40); figure.rotation.y=Math.PI; g.add(figure);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xbcd0ea,
    transparent:true,opacity:0.35,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(14,10,1); halo.position.set(7,18.5,-40); halo.renderOrder=2; g.add(halo);
  /* 天涯长路 + 路上远处三个行人小影 + 望尽处天际一线微光（点击后亮） */
  const road=makeTianyaRoad(); g.add(road);
  const roadGlow=new THREE.Mesh(new THREE.PlaneGeometry(8.5,80),
    new THREE.MeshBasicMaterial({color:0x9ab8d8,transparent:true,opacity:0.18,depthWrite:false,
      blending:THREE.AdditiveBlending}));
  roadGlow.rotation.x=-Math.PI/2; roadGlow.position.set(4.0,0.32,-80); roadGlow.renderOrder=1; g.add(roadGlow);
  const horizon=new THREE.Mesh(new THREE.PlaneGeometry(230,7),
    new THREE.MeshBasicMaterial({color:0x9ab8d8,transparent:true,opacity:0.14,depthWrite:false,
      fog:false,blending:THREE.AdditiveBlending}));
  horizon.position.set(2,3.5,-152); horizon.renderOrder=2; g.add(horizon);
  const crowd=makeCrowd({n:3,rect:[0.8,-92,6.5,2.0],seed:1657,color:0x141a26,rimC:0x9ab8d8,
    rim:0.24,sMin:0.38,sMax:0.50,y:0.65});
  g.add(crowd.mesh);
  /* 昨夜西风凋碧树：疏树两行 + 离枝残叶（纷纷辞树）+ 横流西风 */
  const t1=makeDiaoshu({h:8,seed:1658}); t1.position.set(-13,0,-32); g.add(t1);
  const t2=makeDiaoshu({h:9.5,seed:1659}); t2.position.set(-23,0,-44); g.add(t2);
  const t3=makeDiaoshu({h:5.5,seed:1660}); t3.position.set(18,0,-52); g.add(t3);
  const leaves=makeGlow({n:110,box:[52,13,34],pos:[-16,7,-38],color:0x5c7a62,size:4.2,speed:0.32,rise:-1.5,add:false,maxA:0.5});
  g.add(leaves.points);
  const wind=makeFlow({n:220,box:[150,18,60],pos:[0,9,-52],color:0x8fa0b8,size:24,speed:6.2,maxA:0.24});
  g.add(wind.points);
  const motes=makeGlow({n:50,box:[150,22,80],pos:[0,9,-45],color:0xa8bcd8,size:6,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[240,22,120],pos:[0,8,-70],scale:80,color:0x7e8ea8,op:0.085});
  g.add(mist.g);
  const reeds=makeForeground({kind:'芦苇',n:13,w:26,d:6,color:0x04060a,seed:1661,sway:1.3});
  reeds.g.position.set(-14,-0.6,8); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:7,color:0x04060a,seed:1662,rim:0.14});
  rk.g.position.set(14,-1.2,6.5); g.add(rk.g);
  addLights(g,{c:0x94a9c6,i:0.5,p:[-30,90,-50]},{c:0x1b2130,i:0.58});
  const ease=function(r){ return r*r*(3-2*r); };
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/3.2);
      const e=ease(ctl.reveal);
      ridge.update(t,0); water.update(t);
      mist.update(t,k*(1-0.55*ctl.reveal));
      wind.update(t); leaves.update(t); motes.update(t);
      reeds.update(t,k); rk.update(t,k); crowd.update(t);
      g.position.y=-2.4*e;
      ridge.g.position.y=-2.0*e;
      roadGlow.material.opacity=k*((0.06+0.12*ctl.reveal)*(0.85+0.15*Math.sin(t*0.9)));
      horizon.material.opacity=k*(0.14*ctl.reveal*(0.8+0.2*Math.sin(t*0.5+2)));
      halo.material.opacity=k*(0.10+0.20*ctl.reveal+0.05*Math.sin(t*0.8));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(2,0.05,0.12); pluck(4,0.5,0.10); pluck(7,1.05,0.09);
        const fl=$('#flash'); fl.textContent='望尽天涯路'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(34,112,-185),ms:2.0,mph:0,mhaze:0.05,dirC:C(0x8fa4c8),dirI:0.5,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x1a2232),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,60],t:[0,9.5,55],lf:[0,14,-40],lt:[0,14.5,-42]},
  sky:()=>SK({top:C(0x060910),hor:C(0x131b29),bot:C(0x080b11),fog:C(0x0e141f),fd:0.0048,star:0.42,
    ms:1.55,moon:new THREE.Vector3(24,98,-175),
    dirC:C(0x8fa4c8),dirI:0.40,ambC:C(0x182031),ambI:0.60}) },
{ name:'月穿朱户',dwell:17,river:0.02,build:bZhuHu,
  cam:{f:[0,5.8,19],t:[0.8,5.6,16.5],lf:[-8,6.5,-24],lt:[-7.5,6,-25]},
  sky:()=>SK({top:C(0x070b13),hor:C(0x18202f),bot:C(0x090d13),fog:C(0x111826),fd:0.0056,star:0.5,
    ms:2.0,mph:0,mhaze:0.05,moon:new THREE.Vector3(34,112,-185),
    dirC:C(0x8fa4c8),dirI:0.5,ambC:C(0x1a2232),ambI:0.62}) },
{ name:'独上高楼',dwell:18,river:0.02,build:bGaolou,
  cam:{f:[0,6.8,14],t:[0,7.3,11.5],lf:[5.5,8,-46],lt:[5,8.5,-52]},
  sky:()=>SK({top:C(0x0a0d15),hor:C(0x1a2230),bot:C(0x0a0c12),fog:C(0x101622),fd:0.0060,star:0.42,
    ms:1.85,mph:0.08,mhaze:0.04,moon:new THREE.Vector3(-44,116,-195),
    dirC:C(0x94a9c6),dirI:0.5,ambC:C(0x1b2130),ambI:0.58}) },
];
"""
