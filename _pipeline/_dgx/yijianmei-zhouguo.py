# -*- coding: utf-8 -*-
"""yijianmei-zhouguo.py —— 《一剪梅·舟过吴江》（宋·蒋捷，no.199，烟雨江南）生成配置
N=3（queue 分境为准，舟过吴江的时光之叹装进三重词境）：
  壹·舟摇帘招 —— 一片春愁待酒浇。江上舟摇，楼上帘招。（客舟摇于烟江，酒楼帘招于岸）
  贰·渡桥风雨 —— 秋娘渡与泰娘桥，风又飘飘，雨又萧萧。何日归家洗客袍？（渡口石桥柳丝风雨）
  叁·流光抛人 —— 银字笙调，心字香烧。流光容易把人抛，红了樱桃，绿了芭蕉。（词眼境）
标志性瞬间：流光的时间推移 —— 樱桃由青转红、芭蕉由卷展绿；点击流光，樱桃红透、芭蕉展绿、
  客舟被抛向远处（流光具象成两种颜色的时序推移）。樱桃红与芭蕉绿是末境唯二暖彩点，前境保持黛蓝。
叠字节奏的动态表达：舟摇（船体摇荡）、帘招（酒帘摆动）、飘飘（柳丝横摆+风痕）、萧萧（雨丝斜密）。"""

META = dict(
    N=3, slug='yijianmei-zhouguo', title='一剪梅·舟过吴江', dyn='宋 · 蒋捷', brand_author='蒋 捷',
    gold_rgb='159,176,201',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#9fb0c9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(16,20,26,.60);
  --line:rgba(159,176,201,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#131a24', 1),
        ('#6f664f', '#5f6a7a', 1),
        ('#5a5340', '#525c6c', 1),
    ],
    tip='轻点画面 / 按空格 —— 流光推移：樱桃红透，芭蕉展绿',
    hint='← → 键或空格逐境游览 · 末境可点击流光：红了樱桃，绿了芭蕉',
    cover_read='一剪梅·舟过吴江。宋，蒋捷。一片春愁待酒浇。江上舟摇，楼上帘招。秋娘渡与泰娘桥，风又飘飘，雨又萧萧。何日归家洗客袍？银字笙调，心字香烧。流光容易把人抛，红了樱桃，绿了芭蕉。',
    cover_p1='三重意境，随词句次第展开：一片春愁待酒浇，客舟摇于烟江、酒帘招于岸上；船过秋娘渡与泰娘桥，风飘飘、雨萧萧，归期无定；最后遥想家中银字笙调、心字香烧——而流光最易把人抛下，转眼红了樱桃，绿了芭蕉。',
    cover_p2='边读词，边随蒋捷的一叶客舟过吴江：时光之叹不在言语里，而在樱桃由青转红、芭蕉由卷转展的一瞬。末境轻点画面，看流光推移、樱桃红透、芭蕉展绿。',
    end_h2='樱桃 · 芭蕉', cn_word='三',
    words_js="['再游一次，舟过吴江','初识竹山，尚需共读','渐入佳境，再诵几遍','词境渐深，愁绪渐浓','已解流光抛人之叹','红了樱桃，绿了芭蕉']",
    sky_atmo='0x2e3d4e',
)

POEM_JS = """const POEM = [
{ name:'舟摇帘招', jing:'一片春愁待酒浇 —— 客舟摇于烟江，酒楼的青帘在雨雾里招展，酒在岸上，人在途中。（酒楼 · 酒帘 · 客舟）',
  segs:[
   {c:'一片春愁待酒浇。', p:py('yī piàn chūn chóu dài jiǔ jiāo')},
   {c:'江上舟摇，', p:py('jiāng shàng zhōu yáo')},
   {c:'楼上帘招。', p:py('lóu shàng lián zhāo')}],
  read:'一片春愁待酒浇。江上舟摇，楼上帘招。',
  yisi:'满腹春愁无处排遣，只想借酒来浇灭；船行江上摇摇荡荡，抬头看见岸边酒楼的酒旗正在风雨里招展——酒就在岸上，人却还在途中。一「摇」一「招」，把羁旅的漂泊感与愁绪的无处安放，都写进了这一江烟雨里。',
  zhu:[['一剪梅','词牌名，双调六十字，前后阕各三平韵；蒋捷此首与李清照「红藕香残玉簟秋」同调而异境，一写闺思、一写羁旅'],
       ['吴江','今江苏苏州吴江区，滨太湖、枕吴淞江的水乡泽国；舟过吴江，是词人漂泊江南途中所见'],
       ['蒋捷','宋末词人，号竹山，阳羡（今江苏宜兴）人；南宋亡后隐居不仕，与周密、王沂孙、张炎并称「宋末四大家」'],
       ['待酒浇','等待用酒来浇灭（愁绪）；浇，浇灌、浇灭——化无形的愁为可浇之物，见愁之重'],
       ['舟摇','船在江上摇荡不定；既是舟行之态，也是漂泊之人身心无着的样子'],
       ['帘招','酒楼悬挂的布招旗（酒帘、酒旗）在风中招展；招展的帘子最撩羁旅人——酒能浇愁，而人不得停舟']] },
{ name:'渡桥风雨', jing:'船过秋娘渡与泰娘桥，风又飘飘，雨又萧萧 —— 何日才能归家，洗去这一身客袍的风尘？（渡口 · 石桥 · 柳丝）',
  segs:[
   {c:'秋娘渡与泰娘桥，', p:py('qiū niáng dù yǔ tài niáng qiáo')},
   {c:'风又飘飘，', p:py('fēng yòu piāo piāo')},
   {c:'雨又萧萧。', p:py('yǔ yòu xiāo xiāo')},
   {c:'何日归家洗客袍？', p:py('hé rì guī jiā xǐ kè páo')}],
  read:'秋娘渡与泰娘桥，风又飘飘，雨又萧萧。何日归家洗客袍？',
  yisi:'小船驶过秋娘渡、泰娘桥，一路江风飘飘、细雨萧萧；什么时候才能回到家中，洗尽这身客袍上的风尘呢？渡口与桥都是归途上的地标，过了一处还有一处；「飘飘」「萧萧」两组叠字，风声雨声交织，声声都是乡愁。',
  zhu:[['秋娘渡与泰娘桥','吴江地名：一处渡口、一座桥；秋娘、泰娘本是唐代歌女的名字，用作地名，一路皆是柔软缠绵的江南水乡印记'],
       ['飘飘','风吹拂的样子；柳丝、雨脚、客愁都随之飘摇'],
       ['萧萧','雨细密疏落的声音；与「飘飘」叠字相对，风又是风、雨又是雨，「又……又……」写尽旅途的绵长烦乱'],
       ['客袍','旅人穿的衣服；「洗客袍」意味着结束羁旅、回家安顿——一个「洗」字，藏着风尘与倦意'],
       ['何日归家','以问句写归期无定，是「一片春愁」的根由；不问「能否归」只问「何日归」，更见归心之切']] },
{ name:'流光抛人', jing:'银字笙调，心字香烧 —— 而流光容易把人抛下：转眼红了樱桃，绿了芭蕉。（樱桃 · 芭蕉 · 流光）（点击流光：樱桃红透，芭蕉展绿）',
  segs:[
   {c:'银字笙调，', p:py('yín zì shēng tiáo')},
   {c:'心字香烧。', p:py('xīn zì xiāng shāo')},
   {c:'流光容易把人抛，', p:py('liú guāng róng yì bǎ rén pāo')},
   {c:'红了樱桃，', p:py('hóng liǎo yīng táo')},
   {c:'绿了芭蕉。', p:py('lǜ liǎo bā jiāo')}],
  read:'银字笙调，心字香烧。流光容易把人抛，红了樱桃，绿了芭蕉。',
  yisi:'遥想家中旧日清欢：银字笙悠扬调弄，心字香静静燃着——可流光最是无情，最容易把人抛下：转眼樱桃由青转红、芭蕉叶由卷舒展，春夏暗暗换季，人还被抛在旅途上。樱桃红、芭蕉绿，两种颜色的时序推移，把抽象的时光流逝写成了看得见的物候，是全词词眼。',
  zhu:[['银字笙','饰有银字的笙（簧管乐器）；「银字」「心字」皆是家中旧物的精致名目，是归家后清欢的声音与气息'],
       ['调','调弄、吹奏，读 tiáo；笙簧须调弄而后声音和润'],
       ['心字香','制成篆文「心」字形状的香；点燃之后心字渐残，旧日心事也随之袅袅销尽'],
       ['流光','如流水般逝去的光阴；「容易」二字最狠——不催不赶，时光自己就走远了'],
       ['抛','时光把人抛在身后；人追着时序走，却永远慢一步'],
       ['红了樱桃，绿了芭蕉','樱桃由青转红、芭蕉由卷展绿——以两种颜色的推移写季节暗换，不着一字感慨而感慨至深，历来被视为词眼']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「一片春愁待酒浇」的下一句是？', o:['江上舟摇，楼上帘招','秋娘渡与泰娘桥','风又飘飘，雨又萧萧'], a:0},
 {q:'「流光容易把人抛」的下一句是？', o:['银字笙调，心字香烧','红了樱桃，绿了芭蕉','何日归家洗客袍'], a:1},
 {q:'「银字笙调，心字香烧」中「调」的正确读音与意思是？', o:['diào，调动的调','tiáo，调弄、吹奏乐器','tiáo，调皮捣蛋'], a:1},
 {q:'「秋娘渡与泰娘桥」中「秋娘」「泰娘」指的是？', o:['词人的两位故人','唐代歌女的名字，此处用作吴江渡口与桥的地名','两座寺庙的名字'], a:1},
 {q:'全词以「流光容易把人抛，红了樱桃，绿了芭蕉」作结，主要抒发的是？', o:['对江南春色的赞美','时光易逝、把人抛下的感慨，与倦游思归的春愁','樱桃芭蕉的滋味'], a:1},
];
"""

SCENES_JS = """/* ================= 一剪梅·舟过吴江 · 三境场景（烟雨江南：舟摇帘招 → 渡桥风雨 → 流光抛人） =================
   黛蓝湿雾世界：前两境全冷（黛蓝/藕灰/烟青），末境唯二暖彩点 = 樱桃红 + 芭蕉绿。
   叠字节奏的动态表达：舟摇（船体摇荡）、帘招（酒帘迎风）、飘飘（柳丝横摆+风痕流走）、萧萧（雨丝斜密）。 */

/* 淡青酒帘贴图（布上「酒」字，冷调，不用暖金） */
function lianTex(){
  const c=document.createElement('canvas');c.width=64;c.height=128;const x=c.getContext('2d');
  x.font='38px serif';x.textAlign='center';x.textBaseline='middle';
  x.shadowColor='rgba(159,176,201,.6)';x.shadowBlur=10;
  x.fillStyle='#ccd6e2';x.fillText('酒',32,42);x.fillText('酒',32,92);
  return new THREE.CanvasTexture(c);
}
/* 酒帘：顶边固定的竖幅布帘，下摆随风摆（帘招） */
const LIAN_VERT=`
uniform float uTime; uniform float uSway;
varying vec2 vUv;
void main(){
  vUv=uv;
  vec3 p=position;
  float k=1.0-uv.y; k*=k;
  p.x+=sin(uTime*2.1+uv.x*2.4)*uSway*k;
  p.z+=cos(uTime*1.55+uv.y*3.1)*uSway*0.45*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const LIAN_FRAG=`
uniform sampler2D uMap; uniform vec3 uColor; uniform float uFade;
varying vec2 vUv;
void main(){
  vec4 t=texture2D(uMap,vUv);
  float a=t.a*uFade*0.92;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor*t.rgb,a);
}`;
function makeLian(o){
  o=o||{};
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.34:o.sway},
      uMap:{value:lianTex()},uColor:{value:C(o.color===undefined?0xaebdd0:o.color)},uFade:{value:1}},
    vertexShader:LIAN_VERT,fragmentShader:LIAN_FRAG});
  const mesh=new THREE.Mesh(new THREE.PlaneGeometry(0.82,3.1,6,10),m);
  mesh.renderOrder=3; mesh.frustumCulled=false;
  return {mesh,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* 客舟：船体（中段+两头翘）+ 竹篷（半穹+三道箍）+ 接触阴影 —— 合批 1 mesh */
function makeKezhou(o){
  o=o||{};
  const B=new GeoBag(), hullC=o.hull===undefined?0x10161f:o.hull, canopyC=0x0c1119;
  const mid=new THREE.BoxGeometry(4.6,0.78,1.8); mid.translate(0,0.55,0); B.put(mid,hullC);
  const bow=new THREE.ConeGeometry(0.82,2.0,4); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.62,1.05); bow.translate(3.05,0.62,0); B.put(bow,hullC);
  const stern=new THREE.ConeGeometry(0.82,2.0,4); stern.rotateZ(Math.PI/2);
  stern.scale(1,0.62,1.05); stern.translate(-3.05,0.58,0); B.put(stern,hullC);
  const rim=new THREE.BoxGeometry(4.7,0.10,1.9); rim.translate(0,0.98,0); B.put(rim,shadeColor(hullC,1.55));
  const dome=new THREE.SphereGeometry(1.05,10,6,0,Math.PI*2,0,Math.PI/2);
  dome.scale(1.55,0.70,0.92); dome.translate(-0.8,1.0,0); B.put(dome,canopyC);
  for(let i=0;i<3;i++){
    const rb=new THREE.TorusGeometry(1.02,0.045,5,12,Math.PI);
    rb.rotateY(Math.PI/2); rb.scale(1,0.70,0.92); rb.translate(-0.8-i*1.0+1.0,1.0,0);
    B.put(rb,shadeColor(canopyC,1.8));
  }
  const shadow=new THREE.CircleGeometry(2.6,16); shadow.rotateX(-Math.PI/2); shadow.scale(1.3,1,0.55);
  shadow.translate(0,0.06,0); B.put(shadow,0x04060a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb0c9,i:0.18,p:2.4})));
  return {g};
}

/* 江畔酒楼：两层木楼 + 檐角 + 二层临河栏杆，杆头斜挑一根帘杆（酒帘挂于其上）—— 合批 1 mesh。
   返回 {g, lian, glowMat, winMat, light}：帘招的动态在 lian.update，暖意只许极淡的青白窗光 */
function makeJiuLou(){
  const B=new GeoBag();
  const stoneC=0x0c1119, wallC=0x10161f, woodC=0x161d2a, roofC=0x0a0e15;
  const base=new THREE.BoxGeometry(7.0,1.0,5.6); base.translate(0,0.5,0); B.put(base,stoneC);
  const stair=new THREE.BoxGeometry(2.4,1.0,1.4); stair.translate(0,0.5,3.6); B.put(stair,stoneC);
  const pil1=new THREE.BoxGeometry(4.6,2.6,0.5); pil1.translate(0,1.0+1.3,-2.2); B.put(pil1,wallC);
  [[-3.1,-2.3],[3.1,-2.3],[-3.1,2.3],[3.1,2.3]].forEach(function(pt){
    const c=new THREE.CylinderGeometry(0.16,0.19,3.4,7); c.translate(pt[0],1.0+1.7,pt[1]); B.put(c,woodC);
  });
  const hall=new THREE.BoxGeometry(6.4,2.9,5.0); hall.translate(0,1.0+1.45,0); B.put(hall,wallC);
  const e1f=new THREE.BoxGeometry(8.0,0.24,1.9); e1f.translate(0,4.15,3.0); B.put(e1f,roofC);
  const e1b=new THREE.BoxGeometry(8.0,0.24,1.9); e1b.translate(0,4.15,-3.0); B.put(e1b,roofC);
  const e1l=new THREE.BoxGeometry(1.9,0.24,6.0); e1l.translate(-3.85,4.15,0); B.put(e1l,roofC);
  const e1r=new THREE.BoxGeometry(1.9,0.24,6.0); e1r.translate(3.85,4.15,0); B.put(e1r,roofC);
  const deck=new THREE.BoxGeometry(5.8,0.34,4.4); deck.translate(0,4.4,0); B.put(deck,woodC);
  [[-2.4,-1.8],[2.4,-1.8],[-2.4,1.8],[2.4,1.8]].forEach(function(pt){
    const c=new THREE.CylinderGeometry(0.12,0.14,2.6,7); c.translate(pt[0],4.57+1.3,pt[1]); B.put(c,woodC);
  });
  const rail=new THREE.BoxGeometry(5.2,0.09,0.11); rail.translate(0,5.95,2.0); B.put(rail,shadeColor(woodC,1.4));
  for(let i=0;i<5;i++){
    const pt=new THREE.BoxGeometry(0.08,0.55,0.08); pt.translate(-2.2+i*1.1,5.62,2.0); B.put(pt,woodC);
  }
  const beam=new THREE.BoxGeometry(5.6,0.32,4.0); beam.translate(0,7.35,0); B.put(beam,shadeColor(woodC,1.15));
  const roof=new THREE.ConeGeometry(4.4,2.2,4); roof.rotateY(Math.PI/4); roof.translate(0,7.65+1.1,0); B.put(roof,roofC);
  const finial=new THREE.SphereGeometry(0.22,8,6); finial.translate(0,10.1,0); B.put(finial,roofC);
  /* 二层前窗两扇 + 帘杆（自楼角斜挑向江面） */
  const pole=new THREE.CylinderGeometry(0.05,0.06,3.4,6); pole.rotateZ(1.16);
  pole.translate(3.4,6.5,2.5); B.put(pole,woodC);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb0c9,i:0.22,p:2.5})));
  /* 两扇暗青窗光（初值=最大值） */
  const winMat=new THREE.MeshBasicMaterial({color:0x2c4a5e,transparent:true,opacity:0.8,depthWrite:false});
  const w1=new THREE.Mesh(new THREE.PlaneGeometry(0.9,1.15),winMat); w1.position.set(-1.7,6.2,2.03); g.add(w1);
  const w2=new THREE.Mesh(new THREE.PlaneGeometry(0.9,1.15),winMat); w2.position.set(0.2,6.2,2.03); g.add(w2);
  /* 极淡青辉 + 冷光 */
  const glowMat=new THREE.SpriteMaterial({map:glowTex(),color:0x8fb0c9,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending});
  const glow=new THREE.Sprite(glowMat);
  glow.scale.set(5.5,5.5,1); glow.position.set(-0.8,6.4,2.8); glow.renderOrder=3; g.add(glow);
  glowMat.userData.baseOpacity=0.21;   /* 每帧写入上限，fadeK 合规基线 */
  const light=new THREE.PointLight(0x9fb0c9,0.55,26); light.position.set(-0.8,6.2,3.2);
  light.userData.baseI=0.55; g.add(light);
  /* 酒帘：挂在帘杆末梢 */
  const lian=makeLian({});
  lian.mesh.position.set(4.75,5.05,2.5); g.add(lian.mesh);
  return {g,lian,glowMat,light};
}

/* 泰娘桥：石拱桥（半环拱 + 桥面 + 栏柱 + 两端桥台）—— 合批 1 mesh */
function makeShiQiao(){
  const B=new GeoBag(), stoneC=0x141a24, stone2=shadeColor(stoneC,1.4);
  const arch=new THREE.TorusGeometry(3.1,0.62,8,16,Math.PI); arch.translate(0,0.4,0); B.put(arch,stoneC);
  const deck=new THREE.BoxGeometry(8.4,0.42,2.2); deck.translate(0,3.85,0); B.put(deck,stone2);
  const railL=new THREE.BoxGeometry(8.2,0.10,0.12); railL.translate(0,4.65,1.0); B.put(railL,stone2);
  const railR=new THREE.BoxGeometry(8.2,0.10,0.12); railR.translate(0,4.65,-1.0); B.put(railR,stone2);
  for(let i=0;i<7;i++){
    const p1=new THREE.BoxGeometry(0.16,0.6,0.14); p1.translate(-3.6+i*1.2,4.32,1.0); B.put(p1,stone2);
    const p2=new THREE.BoxGeometry(0.16,0.6,0.14); p2.translate(-3.6+i*1.2,4.32,-1.0); B.put(p2,stone2);
  }
  const abut1=new THREE.BoxGeometry(1.6,2.4,2.6); abut1.translate(-4.3,1.0,0); B.put(abut1,stoneC);
  const abut2=new THREE.BoxGeometry(1.6,2.4,2.6); abut2.translate(4.3,1.0,0); B.put(abut2,stoneC);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb0c9,i:0.16,p:2.4})));
  return {g};
}

/* 秋娘渡：渡口木栈台 + 系船桩 + 拢岸石阶 —— 合批 1 mesh */
function makeDukou(){
  const B=new GeoBag(), woodC=0x151b26, wood2=shadeColor(woodC,1.35);
  const deck1=new THREE.BoxGeometry(5.6,0.3,2.8); deck1.translate(0,1.35,0); B.put(deck1,wood2);
  const deck2=new THREE.BoxGeometry(2.6,0.28,1.8); deck2.translate(2.9,1.05,1.4); B.put(deck2,wood2);
  [[-2.4,-1.1],[2.4,-1.1],[-2.4,1.1],[2.4,1.1],[0,0]].forEach(function(pt){
    const p=new THREE.CylinderGeometry(0.11,0.13,2.6,6); p.translate(pt[0],0.15,pt[1]); B.put(p,woodC);
  });
  const post=new THREE.CylinderGeometry(0.09,0.11,1.5,6); post.translate(-2.9,2.2,0.6); B.put(post,woodC);
  for(let i=0;i<3;i++){
    const st=new THREE.BoxGeometry(2.2-i*0.3,0.22,0.8);
    st.translate(-4.6-i*0.55,0.35+i*0.02,0.4); B.put(st,shadeColor(0x10151e,1.15));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb0c9,i:0.16,p:2.4})));
  return {g};
}

/* 柳：曲干 + 垂丝（垂丝顶挂、末端随风横摆 —— 「飘飘」）。
   返回 {g,update(t)}；垂丝为 ShaderMaterial（显式双 shader，uFade 由 setFade 接管） */
const WIL_VERT=`
uniform float uTime; uniform float uSway;
varying float vY;
void main(){
  vY=uv.y;
  vec3 p=position;
  float k=(1.0-uv.y); k*=k;
  p.x+=sin(uTime*1.2+uv.y*4.2+position.x*0.7)*uSway*k;
  p.z+=cos(uTime*0.85+uv.y*3.3)*uSway*0.5*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const WIL_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade;
varying float vY;
void main(){
  vec3 c=mix(uC,uTipC,pow(1.0-vY,1.4));
  gl_FragColor=vec4(c,uFade*(0.55+0.45*vY));
}`;
function makeWillow(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?17:o.seed);
  const B=new GeoBag(), barkC=0x12161f;
  const lean=(R()-0.5)*0.5;
  const trunk=new THREE.CylinderGeometry(0.16,0.30,3.4,7);
  trunk.rotateZ(lean); trunk.translate(0,1.7,0); B.put(trunk,barkC);
  for(let i=0;i<2;i++){
    const br=new THREE.CylinderGeometry(0.06,0.12,2.2,5);
    br.rotateZ((R()<0.5?1:-1)*(0.7+R()*0.5)); br.translate((R()-0.5)*0.9,3.2+R()*0.5,(R()-0.5)*0.7);
    B.put(br,barkC);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb0c9,i:0.14,p:2.4})));
  /* 垂丝：细长面片一束，挂向水面 */
  const SB=new GeoBag();
  const n=o.n===undefined?9:o.n, len=o.len===undefined?4.6:o.len;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*2.6, z=(R()-0.5)*1.4, top=3.4+R()*1.4;
    const st=new THREE.PlaneGeometry(0.34+R()*0.2,len,1,7);
    st.translate(x,top-len/2,z); SB.put(st,0x000000);
  }
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.5:o.sway},
      uC:{value:C(0x1c2a26)},uTipC:{value:C(0x33493e)},uFade:{value:1}},
    vertexShader:WIL_VERT,fragmentShader:WIL_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(SB.list),m);
  mesh.renderOrder=3; mesh.frustumCulled=false; g.add(mesh);
  return {g,update(t){m.uniforms.uTime.value=t;}};
}

/* 夜雨：斜落的细雨丝（自定义着色器，显式双 shader；uMaxA 由各境按叙事驱动） */
const RAIN_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uSlant;
varying float vA;
void main(){
  float life=fract(uTime*uSpeed*(0.7+0.6*fract(aSeed*5.31))+aSeed);
  vec3 p=position;
  float dy=uBox.y*(0.5-life);
  p.y+=dy; p.x+=dy*uSlant;
  vA=smoothstep(0.0,0.10,life)*smoothstep(1.0,0.86,life)*(0.35+0.65*fract(aSeed*13.7));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const RAIN_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=length(q*vec2(8.0,0.36));
  float a=smoothstep(0.5,0.06,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeRain(o){
  o=o||{};
  const n=o.n===undefined?140:o.n, box=o.box||[110,28,56], pos=o.pos||[0,15,-16];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.4:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.5:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uSlant:{value:o.slant===undefined?0.14:o.slant},
      uColor:{value:C(o.color===undefined?0x9aabbf:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.22:o.maxA}},
    vertexShader:RAIN_VERT,fragmentShader:RAIN_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* 樱桃树：曲干 + 三簇叶团（合批 1 mesh）+ 果实 InstancedMesh（青→红的时序推移就发生在果实上）。
   返回 {g, berries, update(t,k,ripe)}；ripe 0=青 1=红透，逐帧 lerp 实例色 */
function makeYingTao(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?57:o.seed);
  const B=new GeoBag(), barkC=0x1a1410;
  const trunk=new THREE.CylinderGeometry(0.19,0.34,2.3,8);
  trunk.rotateZ(0.2); trunk.translate(0.22,1.15,0); B.put(trunk,barkC);
  for(let i=0;i<3;i++){
    const br=new THREE.CylinderGeometry(0.07,0.14,1.6,5);
    br.rotateZ((i-1)*0.85); br.translate((i-1)*0.7,2.2+R()*0.3,(R()-0.5)*0.5); B.put(br,barkC);
  }
  [[-0.85,2.85],[0.75,3.1],[0,2.6]].forEach(function(pt){
    const leaf=new THREE.IcosahedronGeometry(0.85+R()*0.25,1);
    leaf.scale(1.35,0.55,1.0); leaf.translate(pt[0],pt[1],(R()-0.5)*0.5); B.put(leaf,0x22331f);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x050806}),{c:0x9fb0c9,i:0.2,p:2.4})));
  /* 果实：成簇挂在叶团下缘，青果也清晰可辨 */
  const n=o.n===undefined?26:o.n;
  const berryGeo=new THREE.SphereGeometry(0.185,8,6);
  const berryMat=new THREE.MeshPhongMaterial({color:0xffffff,shininess:32,specular:0x50607a,
    transparent:true,emissive:0x0a0d08});
  const berries=new THREE.InstancedMesh(berryGeo,berryMat,n);
  const bases=[];
  const M=new THREE.Matrix4();
  for(let i=0;i<n;i++){
    const cl=Math.floor(R()*3), cx=[[-0.85,2.85],[0.75,3.1],[0,2.6]][cl];
    bases.push({x:cx[0]+(R()-0.5)*1.6, y:cx[1]-0.5-R()*0.42, z:(R()-0.5)*0.9,
      s:0.8+R()*0.5, jit:0.75+R()*0.35});
  }
  function apply(ripe){
    const grn=C(0x6b9450), red=C(0xd0453a), tmp=new THREE.Color();
    for(let i=0;i<n;i++){
      const b=bases[i];
      tmp.copy(grn).lerp(red,Math.min(1,ripe*b.jit));
      berries.setColorAt(i,tmp);
      const s=b.s*(0.85+0.35*ripe*b.jit);
      M.makeScale(s,s,s); M.setPosition(b.x,b.y,b.z);
      berries.setMatrixAt(i,M);
    }
    if(berries.instanceColor)berries.instanceColor.needsUpdate=true;
    berries.instanceMatrix.needsUpdate=true;
  }
  apply(0);
  berries.renderOrder=2; g.add(berries);
  const api={g,berries,update(t,k,ripe){ apply(ripe===undefined?0:ripe); }};
  return api;
}

/* 芭蕉：茎干（合批 1）+ 卷叶（筒状，未展）+ 展叶（叶形面片，随点击横向展开）。
   返回 {g, curlMat, openMat, openMesh, update(t,k,e)}：e 0=卷 1=展 —— 「绿了芭蕉」的时序推移 */
function leafGeo(w,h){
  const g=new THREE.PlaneGeometry(w,h,6,8);
  const p=g.attributes.position;
  for(let i=0;i<p.count;i++){
    const ty=Math.min(1,Math.max(0,p.getY(i)/h+0.5));
    const taper=0.5+0.78*Math.sin(ty*Math.PI);
    p.setX(i,p.getX(i)*taper);
    p.setZ(i,p.getZ(i)+Math.sin(ty*2.6)*0.30);
  }
  g.computeVertexNormals(); return g;
}
function makeBaJiao(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?77:o.seed);
  const g=new THREE.Group();
  /* 茎干 ×2（一高一矮，芭蕉假茎粗壮） */
  const B=new GeoBag(), stemC=0x1b2620;
  const s1=new THREE.CylinderGeometry(0.22,0.34,2.6,8); s1.translate(0,1.3,0); B.put(s1,stemC);
  const s2=new THREE.CylinderGeometry(0.15,0.24,1.8,7); s2.translate(0.75,0.9,0.3); B.put(s2,stemC);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x04060a}),{c:0x9fb0c9,i:0.16,p:2.4})));
  /* 卷叶：三支上指的青卷（粗壮醒目，未展之态；初值=最大值，点击后旋开散去） */
  const CB=new GeoBag();
  [[-0.25,2.9,0.22,0.13],[-0.62,2.3,-0.3,0.10],[0.95,1.9,0.38,0.09]].forEach(function(pt){
    const cu=new THREE.CylinderGeometry(pt[3],pt[3]*2.1,pt[1],7,1,true);
    cu.rotateZ(pt[2]); cu.translate(pt[0]*0.9,pt[1]/2+0.55,0); CB.put(cu,0x3a5642);
  });
  const curlMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    transparent:true,opacity:1.0,side:THREE.DoubleSide,specular:0x2a3446,emissive:0x040706});
  const curl=new THREE.Mesh(mergeGeos(CB.list),curlMat); curl.renderOrder=2; g.add(curl);
  /* 展叶：三片大叶（初值隐藏，点击后横向展开、颜色转深绿） */
  const OB=new GeoBag();
  [[-2.6,3.6,-1.1,0.9],[2.9,3.9,1.15,0.75],[0.3,4.4,0.05,1.0]].forEach(function(pt){
    const lf=leafGeo(1.5*pt[3],pt[1]);
    lf.rotateZ(-pt[2]); lf.rotateY((R()-0.5)*0.8);
    lf.translate(pt[0],pt[1]/2+1.6,0.1); OB.put(lf,0x3d5c40);
    const mid=new THREE.BoxGeometry(0.05,pt[1]*0.92,0.05);
    mid.rotateZ(-pt[2]); mid.translate(pt[0],pt[1]*0.46+1.6,0.14); OB.put(mid,shadeColor(0x3d5c40,0.6));
  });
  const openMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    transparent:true,opacity:0.0,side:THREE.DoubleSide,specular:0x2a3446,emissive:0x050b06});
  openMat.userData.baseOpacity=1.0;   /* 初值=最大值：点击后由 update 驱动 k*e 亮起 */
  const open=new THREE.Mesh(mergeGeos(OB.list),openMat);
  open.renderOrder=2; g.add(open);
  const api={g,curlMat,openMat,open,update(t,k,e){
    curlMat.opacity=k*Math.max(0.0,1.0-e*1.25);
    openMat.opacity=k*Math.min(1.0,e*1.35);
    open.scale.x=0.22+0.78*e;
    open.rotation.z=0.04*Math.sin(t*0.5);
  }};
  return api;
}

/* 银字笙：笙斗碗 + 一圈参差笙管 + 吹管（银灰，合批 1 mesh） */
function makeSheng(){
  const B=new GeoBag(), silver=0x9aa8b8, dark=0x39434f;
  const bowl=new THREE.SphereGeometry(0.42,10,7,0,Math.PI*2,0,Math.PI/2);
  bowl.rotateX(Math.PI); bowl.translate(0,0.42,0); B.put(bowl,dark);
  const R=seedRnd(39);
  for(let i=0;i<10;i++){
    const a=i/10*Math.PI*2, rr=0.22+R()*0.06, h=0.9+R()*1.3;
    const p=new THREE.CylinderGeometry(0.055,0.055,h,6);
    p.translate(Math.cos(a)*rr,0.5+h/2,Math.sin(a)*rr); B.put(p,silver);
  }
  const pipe=new THREE.CylinderGeometry(0.06,0.07,1.0,6);
  pipe.rotateZ(1.1); pipe.translate(0.5,0.35,0.2); B.put(pipe,silver);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:38,
    specular:0x8ea4c0,emissive:0x05070c}),{c:0x9fb0c9,i:0.3,p:2.6})));
  return {g};
}

/* 心字香：小香炉 + 篆成「心」字形的香环 + 极小红点香头（合批 1 mesh） */
function makeXinXiang(){
  const B=new GeoBag();
  const bowl=new THREE.SphereGeometry(0.34,10,7,0,Math.PI*2,0,Math.PI/2);
  bowl.rotateX(Math.PI); bowl.translate(0,0.3,0); B.put(bowl,0x2a3038);
  [[0.18,0.06],[-0.18,0.06],[0,0.18]].forEach(function(pt){
    const leg=new THREE.CylinderGeometry(0.035,0.05,0.22,5);
    leg.translate(pt[0],0.11,pt[1]); B.put(leg,0x1d232c);
  });
  const ring=new THREE.TorusGeometry(0.20,0.030,5,18);
  ring.rotateX(-Math.PI/2); ring.scale(1.25,1,0.9); ring.translate(0,0.5,0); B.put(ring,0x4a352a);
  const tip=new THREE.SphereGeometry(0.035,6,5); tip.translate(0.26,0.52,0); B.put(tip,0x8c4030);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x3d465e,emissive:0x05070c}),{c:0x9fb0c9,i:0.2,p:2.5})));
  return {g};
}

function bCover(){ // 封面 · 吴江烟雨 —— 一江黛蓝湿雾，舟自天际来
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:72,amp:0.15,freq:0.17,speed:0.38,flow:[0.08,0.4],spec:1.35,
    deep:0x0a111c,shallow:0x18232f,skyc:0x233040,moonDir:[-24,90,-180]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:19901,color:0x090e15,atmo:0x2e3d4e,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 远处酒楼一点青窗 + 酒帘 */
  const lou=makeJiuLou(); lou.g.position.set(-30,0,-34); lou.g.rotation.y=0.7;
  lou.g.scale.setScalar(0.62); g.add(lou.g);
  /* 远处客舟一叶 */
  const boat=makeKezhou(); boat.g.position.set(17,-0.3,-40); boat.g.rotation.y=0.45;
  boat.g.scale.setScalar(0.72); g.add(boat.g);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaec2d8,
    transparent:true,opacity:0.3,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.material.userData.baseOpacity=0.32;   /* 每帧写入上限 0.31，fadeK 合规基线 */
  lamp.scale.set(2.8,2.8,1); lamp.position.set(17,1.5,-39); lamp.renderOrder=3; g.add(lamp);
  const rain=makeRain({n:110,box:[150,30,70],pos:[0,16,-20],color:0x9aabbf,maxA:0.16,size:2.2,slant:0.13});
  g.add(rain.points);
  const mist=makeMist({n:6,spread:[240,22,120],pos:[0,9,-52],scale:78,color:0x8496ae,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[170,24,90],pos:[0,10,-34],color:0xa4b2c6,size:5,speed:0.05,rise:0,maxA:0.20});
  g.add(motes.points);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:19902,rim:0.14});
  fgRock.g.position.set(-14,-1.6,30); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:19903,sway:0.9});
  reeds.g.position.set(13,-1.1,28); g.add(reeds.g);
  addLights(g,{c:0x8fa4c4,i:0.40,p:[-30,78,-36]},{c:0x1c2530,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); rain.update(t); mist.update(t,k); motes.update(t);
    lou.lian.update(t); lou.glowMat.opacity=k*(0.18+0.03*Math.sin(t*1.4));
    boat.g.position.y=-0.3+0.07*Math.sin(t*0.8); boat.g.rotation.z=0.02*Math.sin(t*0.62+1);
    lamp.material.opacity=k*(0.26+0.05*Math.sin(t*1.7));
    fgRock.update(t,k); reeds.update(t,k);
  }};
}

function bZhouYao(){ // 壹 · 舟摇帘招 —— 客舟摇于烟江（一片春愁待酒浇），酒楼青帘招展于岸（楼上帘招）
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:76,amp:0.17,freq:0.18,speed:0.42,flow:[0.08,0.42],spec:1.5,
    deep:0x0a111c,shallow:0x18232f,skyc:0x233040,moonDir:[-28,88,-186]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:16,layers:2,peaks:4,seed:19905,color:0x090e15,atmo:0x2e3d4e,fogK:0.58,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 江畔酒楼：帘招所自 */
  const lou=makeJiuLou(); lou.g.position.set(-11,0.2,-24); lou.g.rotation.y=0.5;
  lou.g.scale.setScalar(1.3); g.add(lou.g);
  const rock=new THREE.Mesh(rockGeo(6.5,1,seedRnd(19906)),
    rimHook(new THREE.MeshPhongMaterial({color:0x0a0e15,shininess:6,specular:0x222c3c,emissive:0x04060a}),
      {c:0x9fb0c9,i:0.14,p:2.4}));
  rock.scale.set(1.7,0.85,1.3); rock.position.set(-11,-1.4,-25.5); g.add(rock);
  /* 客舟与舟中客：一片春愁待酒浇（酒在岸上，人在舟中） */
  const boat=makeKezhou(); boat.g.position.set(3,-0.1,-16); boat.g.rotation.y=-0.35;
  boat.g.scale.setScalar(1.3); g.add(boat.g);
  const poet=makeFigure({pose:'坐饮',robe:0x39445c,belt:0x5a6a80,skin:0xcdb193,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0x9fb0c9,rim:0.5,noProp:true,scale:0.72});
  poet.position.set(1.35,1.02,0.05); poet.rotation.y=-0.42; boat.g.add(poet);
  /* 烟雨 + 江雾 */
  const rain=makeRain({n:140,box:[120,28,58],pos:[2,15,-16],color:0x9aabbf,maxA:0.22,size:2.4,slant:0.12});
  g.add(rain.points);
  const mist=makeMist({n:5,spread:[220,20,110],pos:[0,8,-50],scale:74,color:0x8496ae,op:0.07});
  g.add(mist.g);
  const motes=makeGlow({n:36,box:[150,22,80],pos:[0,9,-28],color:0xa4b2c6,size:5,speed:0.05,rise:0,maxA:0.18});
  g.add(motes.points);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:19907,rim:0.14});
  fgRock.g.position.set(14,-1.5,12); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:9,d:6,color:0x04060a,seed:19908,sway:0.9});
  reeds.g.position.set(-14,-1.2,12); g.add(reeds.g);
  addLights(g,{c:0x93a4ba,i:0.40,p:[-24,80,-30]},{c:0x1c2530,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); rain.update(t); mist.update(t,k); motes.update(t);
    /* 舟摇：摇荡+微侧 */
    boat.g.position.y=-0.1+0.10*Math.sin(t*0.85);
    boat.g.rotation.z=0.035*Math.sin(t*0.62+1);
    boat.g.rotation.x=0.018*Math.sin(t*0.5+2);
    poet.userData.update(t,k);
    /* 帘招：风来则张，风过则垂 */
    lou.lian.update(t);
    lou.lian.mat.uniforms.uSway.value=0.30+0.14*Math.sin(t*0.35);
    lou.glowMat.opacity=k*(0.17+0.03*Math.sin(t*1.3));
    lou.light.intensity=k*0.55*(0.8+0.2*Math.sin(t*1.1));
    fgRock.update(t,k); reeds.update(t,k);
  }};
}

function bDuQiao(){ // 贰 · 渡桥风雨 —— 船过秋娘渡与泰娘桥，风又飘飘（柳丝横摆），雨又萧萧（雨密斜急）
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:76,amp:0.19,freq:0.2,speed:0.5,flow:[0.1,0.45],spec:1.4,
    deep:0x090f19,shallow:0x15202c,skyc:0x1f2b39,moonDir:[-30,86,-190]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:18,layers:2,peaks:5,seed:19909,color:0x080d14,atmo:0x2a3846,fogK:0.58,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-122); g.add(ridge.g);
  /* 泰娘桥：石拱横波 */
  const qiao=makeShiQiao(); qiao.g.position.set(10,-0.2,-30); qiao.g.rotation.y=0.35;
  qiao.g.scale.setScalar(1.5); g.add(qiao.g);
  /* 秋娘渡：渡口栈台（归途的地标，也是等船的地方） */
  const du=makeDukou(); du.g.position.set(-10,-0.15,-13); du.g.rotation.y=-0.4;
  g.add(du.g);
  const duP=makeCrowd({n:3,rect:[-11.5,-14,4.5,2.4],seed:19910,color:0x11161e,rimC:0x9fb0c9,
    rim:0.22,sMin:0.5,sMax:0.62});
  g.add(duP.mesh);
  /* 两岸柳丝：飘飘 */
  const willowL=makeWillow({seed:19911,n:10,sway:0.55}); willowL.g.position.set(-16,0,-21);
  willowL.g.scale.setScalar(1.5); g.add(willowL.g);
  const willowR=makeWillow({seed:19912,n:8,sway:0.62}); willowR.g.position.set(15.5,0,-23);
  willowR.g.scale.setScalar(1.3); g.add(willowR.g);
  /* 客舟过桥 */
  const boat=makeKezhou(); boat.g.position.set(0,-0.1,-19); boat.g.rotation.y=0.3;
  boat.g.scale.setScalar(1.35); g.add(boat.g);
  const poet=makeFigure({pose:'坐饮',robe:0x39445c,belt:0x5a6a80,skin:0xcdb193,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0x9fb0c9,rim:0.48,noProp:true,scale:0.74});
  poet.position.set(1.35,1.02,0.05); poet.rotation.y=-0.35; boat.g.add(poet);
  /* 萧萧：雨更密更斜 */
  const rain=makeRain({n:170,box:[130,30,62],pos:[0,15,-16],color:0x9aabbf,maxA:0.28,size:2.6,slant:0.17});
  g.add(rain.points);
  /* 飘飘：横掠的风痕 */
  const gust=makeFlow({n:80,box:[130,10,50],pos:[0,7,-20],color:0x8ea0b6,size:20,speed:3.4,maxA:0.11});
  g.add(gust.points);
  const mist=makeMist({n:5,spread:[220,20,110],pos:[0,8,-50],scale:74,color:0x7e90a8,op:0.08});
  g.add(mist.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x04060a,seed:19913,rim:0.14});
  fgRock.g.position.set(14,-1.5,12); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:19914,sway:1.15});
  reeds.g.position.set(-14,-1.2,12); g.add(reeds.g);
  addLights(g,{c:0x8ea0b6,i:0.38,p:[-26,80,-30]},{c:0x19222e,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); rain.update(t); gust.update(t); mist.update(t,k);
    /* 萧萧的呼吸：雨脚随风一阵紧一阵疏 */
    rain.mat.uniforms.uMaxA.value=k*(0.25+0.06*Math.sin(t*0.45));
    /* 飘飘的呼吸：柳丝一阵急一阵缓 */
    willowL.update(t*1.15); willowR.update(t);
    boat.g.position.y=-0.1+0.11*Math.sin(t*0.9);
    boat.g.rotation.z=0.038*Math.sin(t*0.66+1);
    poet.userData.update(t,k); duP.update(t);
    fgRock.update(t,k); reeds.update(t,k);
  }};
}

function bLiuGuang(){ // 叁（末境·可点击）· 流光抛人 —— 银字笙调心字香烧是家中的旧忆；点击流光：樱桃红透、芭蕉展绿、客舟被抛向远处
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0,ripe:0};
  const water=makeWater({size:340,seg:76,amp:0.15,freq:0.18,speed:0.4,flow:[0.08,0.42],spec:1.4,
    deep:0x0a111c,shallow:0x17222e,skyc:0x223040,moonDir:[-26,90,-188]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:19915,color:0x090e15,atmo:0x2e3d4e,fogK:0.58,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 江畔石台（岸上的小小庭院） */
  const bank=new THREE.Mesh(rockGeo(7,1,seedRnd(19916)),
    rimHook(new THREE.MeshPhongMaterial({color:0x0b0f16,shininess:6,specular:0x222c3c,emissive:0x04060a}),
      {c:0x9fb0c9,i:0.14,p:2.4}));
  bank.scale.set(3.2,0.16,2.2); bank.position.set(-1,-1.0,-15); g.add(bank);
  /* 樱桃树（左）+ 芭蕉（右）：词眼的两种颜色 */
  const yt=makeYingTao({seed:19917,n:26}); yt.g.position.set(-6.2,0.1,-12.6); yt.g.scale.setScalar(1.9);
  g.add(yt.g);
  const ripeLight=new THREE.PointLight(0xc05040,0.0,26);
  ripeLight.position.set(-6.2,3.6,-12); ripeLight.userData.baseI=1.1; g.add(ripeLight);
  const bj=makeBaJiao({seed:19918}); bj.g.position.set(6.2,0.1,-11); bj.g.scale.setScalar(1.9);
  g.add(bj.g);
  /* 家中旧忆：案上银字笙、心字香（银与青灰，不是暖色） */
  const table=makeTable({w:3.6,d:1.7,h:1.55,wood:0x141a26}); table.g.position.set(-0.5,0.1,-19);
  table.g.rotation.y=0.1; g.add(table.g);
  const sheng=makeSheng(); sheng.g.position.set(-1.0,1.68,-19.1); sheng.g.scale.setScalar(0.9);
  g.add(sheng.g);
  const xx=makeXinXiang(); xx.g.position.set(0.7,1.68,-18.8); g.add(xx.g);
  const smoke=makeGlow({n:16,box:[0.5,4.5,0.5],pos:[0.96,6.2,-18.8],color:0xa9b8c8,size:2.4,speed:0.10,rise:1,maxA:0.20});
  g.add(smoke.points);
  /* 客舟（远处，正被流光抛下） */
  const boat=makeKezhou(); boat.g.position.set(13,-0.15,-28); boat.g.rotation.y=0.5;
  boat.g.scale.setScalar(1.0); g.add(boat.g);
  const poet=makeFigure({pose:'坐饮',robe:0x39445c,belt:0x5a6a80,skin:0xcdb193,collar:0x9dabbf,
    hat:'幞头',beard:true,rimC:0x9fb0c9,rim:0.42,noProp:true,scale:0.6});
  poet.position.set(1.35,1.02,0.05); poet.rotation.y=-0.4; boat.g.add(poet);
  /* 流光：时间的色流（accent 青蓝），过境不停 */
  const flow=makeFlow({n:100,box:[130,8,44],pos:[0,4.5,-22],color:0x9fb0c9,size:15,speed:2.6,maxA:0.13});
  g.add(flow.points);
  const motes=makeGlow({n:36,box:[130,20,70],pos:[0,9,-26],color:0xa4b2c6,size:5,speed:0.05,rise:0,maxA:0.18});
  g.add(motes.points);
  const burst=makeBurst({n:70,color:0xd8b8a8,pos:[-0.5,4.5,-16]}); g.add(burst.points);
  const rain=makeRain({n:60,box:[110,26,54],pos:[0,15,-16],color:0x9aabbf,maxA:0.10,size:2.2,slant:0.10});
  g.add(rain.points);
  const mist=makeMist({n:4,spread:[220,20,110],pos:[0,8,-48],scale:74,color:0x8496ae,op:0.06});
  g.add(mist.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:3.8,w:20,d:8,color:0x04060a,seed:19919,rim:0.14});
  fgRock.g.position.set(13,-1.5,12); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:19920,sway:1.0});
  reeds.g.position.set(-14,-1.2,12); g.add(reeds.g);
  addLights(g,{c:0x93a4ba,i:0.40,p:[-24,80,-28]},{c:0x1c2530,i:0.60});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        const el=ctl.t-ctl.clickT;
        ctl.ripe=ease(clamp(el/3.2,0,1));
      }
      const e=ctl.ripe;
      ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
      smoke.update(t); rain.update(t); burst.update(t);
      fgRock.update(t,k); reeds.update(t,k);
      /* 樱桃：青 → 红透（末境唯二暖彩点之一） */
      yt.update(t,k,e);
      ripeLight.intensity=k*1.1*e*(0.8+0.2*Math.sin(t*2.2));
      /* 芭蕉：卷 → 展（末境唯二暖彩点之二） */
      bj.update(t,k,e);
      /* 流光大盛，客舟被抛向远处 */
      flow.mat.uniforms.uMaxA.value=k*(0.13+0.20*e);
      flow.update(t*(1.0+e*0.8));
      boat.g.position.x=13-e*6-((t*(0.35+e*0.5))%14);
      boat.g.position.y=-0.15+0.08*Math.sin(t*0.85);
      boat.g.rotation.z=0.03*Math.sin(t*0.6+1);
      poet.userData.update(t,k);
    },onEnter(){
      pluck(2,0.2,0.06); pluck(4,0.8,0.05);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        burst.fire(); pluck(1,0.05,0.12); pluck(3,0.5,0.10); pluck(5,1.05,0.10); pluck(0,1.7,0.09);
        const fl=$('#flash'); fl.textContent='红了樱桃，绿了芭蕉'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0a0f18),hor:C(0x1e2a38),bot:C(0x080b11),fog:C(0x151d26),fd:0.013,star:0.08,
  moon:new THREE.Vector3(30,108,-190),ms:0.5,mph:0.3,mhaze:0.2,dirC:C(0x9aaec4),dirI:0.34,
  dirP:new THREE.Vector3(-24,80,-30),ambC:C(0x1c2530),ambI:0.58},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,58],t:[0,10.5,52],lf:[2,11,-46],lt:[4,10.5,-50]},
  sky:()=>SK({top:C(0x090e16),hor:C(0x1c2836),bot:C(0x080b11),fog:C(0x141c26),fd:0.013,star:0.10,
    ms:0.45,mph:0.32,mhaze:0.22,moon:new THREE.Vector3(-28,92,-190),
    dirC:C(0x9aaec4),dirI:0.34,ambC:C(0x1c2530),ambI:0.58}) },
{ name:'舟摇帘招',dwell:16,river:0.05,build:bZhouYao,
  cam:{f:[1.5,5.4,19],t:[2.2,5.2,16.5],lf:[-2.5,6.4,-24],lt:[-1.8,6.1,-26]},
  sky:()=>SK({top:C(0x0a0f18),hor:C(0x1e2a38),bot:C(0x080b11),fog:C(0x151d26),fd:0.012,star:0.08,
    ms:0.4,mph:0.3,mhaze:0.2,moon:new THREE.Vector3(-30,90,-192),
    dirC:C(0x9aaec4),dirI:0.34,ambC:C(0x1c2530),ambI:0.60}) },
{ name:'渡桥风雨',dwell:17,river:0.04,build:bDuQiao,
  cam:{f:[0,5.2,18],t:[0.8,5,15.5],lf:[4,6,-30],lt:[5,5.7,-32]},
  sky:()=>SK({top:C(0x080c13),hor:C(0x18232f),bot:C(0x070a0f),fog:C(0x141b25),fd:0.014,star:0.05,
    ms:0.35,mph:0.34,mhaze:0.22,moon:new THREE.Vector3(26,86,-194),
    dirC:C(0x8ea0b6),dirI:0.32,ambC:C(0x19222e),ambI:0.58}) },
{ name:'流光抛人',dwell:19,river:0.03,build:bLiuGuang,
  cam:{f:[0,5.6,19],t:[0.6,5.2,16],lf:[-3,6.2,-20],lt:[-2,6,-22]},
  sky:()=>SK({top:C(0x0a101a),hor:C(0x20303a),bot:C(0x080b11),fog:C(0x151d27),fd:0.0125,star:0.10,
    ms:0.4,mph:0.3,mhaze:0.18,moon:new THREE.Vector3(-26,92,-192),
    dirC:C(0x9aaec4),dirI:0.36,ambC:C(0x1c2530),ambI:0.60}) },
];
"""
