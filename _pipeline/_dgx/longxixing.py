# -*- coding: utf-8 -*-
"""longxixing.py —— 《陇西行》（唐·陈陶，queue no.223，大漠金戈）生成配置
两境（N=queue stages 数）：誓扫胡尘（誓扫匈奴不顾身·五千貂锦丧胡尘——暮色誓师→冲入胡尘）、
春闺梦里（可怜无定河边骨·犹是春闺梦里人——标志性瞬间+末境点击「骨与梦的对切」）。
大漠金戈全套色板：底色 #120d08、雾 #140d07～#141018 系、文字 #f0e2cc，accent=#c4823a
（queue 分配强调色，赭金）只落在军旗/戟锋/人物边缘光/梦烛暖光/UI 上，禁艳金。
情绪推进线：境壹=残阳暮色（誓师果决、胡尘漫天，暖赭）→ 境贰=冷月寒滩（无定河边，冷灰蓝）
——冷色河滩与点击后浮现的暖色梦影构成全页核心的冷暖对切。
标志性瞬间（境贰·全诗名句）：骨与梦的对切——无定河寒滩上残戈锈甲半掩（白骨意象克制写意，
不直写尸骸），点击后春闺梦影暖光浮现，冷滩与暖梦如电影交叉剪辑般缓缓明灭；
与已有边塞页（孤城/金甲/雪弓刀/梦回连营/望乡闻笛）第一眼可区分：本页是「丧师的悲剧 + 骨梦两重时空」。
末境点击（queue interact：点击梦里人——河边白骨冷景与闺中梦里人暖影对切）：点击画面——
春闺窗影暖光渐亮、闺中人与梦里人相对而立，冷暖两景交叉明灭，「可怜无定河边骨 犹是春闺梦里人」题字同现。
考点钉子：貂 diāo / 闺 guī / 丧 sàng（第 3 题落点）；陇西行乐府旧题+陈陶《陇西行四首》其二+
无定河得名（第 4 题）；「河边骨」与「梦里人」的对照反战主旨（第 5 题）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='longxixing', title='陇西行', dyn='唐 · 陈陶', brand_author='陈 陶',
    gold_rgb='196,130,58',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#c4823a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(196,130,58,.3);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#120d08', 2),
        ('rgba(5,8,15', 'rgba(24,16,9', 1),
        ('rgba(4,6,11', 'rgba(12,8,5', 2),
        ('rgba(6,9,16', 'rgba(24,16,9', 1),
        ('rgba(3,5,9', 'rgba(8,5,3', 1),
        ('#0b101c', '#181009', 1),
        ('#6f664f', '#7a6a50', 1),
        ('#5a5340', '#6a5a44', 1),
    ],
    tip='轻点画面 / 按空格 —— 骨与梦，一冷一暖两相照',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看河边寒骨与春闺梦影的冷暖对切',
    cover_read='陇西行。唐，陈陶。誓扫匈奴不顾身，五千貂锦丧胡尘。可怜无定河边骨，犹是春闺梦里人。',
    cover_p1='两重意境，随诗句次第展开：暮色沙场上，五千貂锦精锐誓师杀敌、奋不顾身，却一朝丧身胡尘；转过境来，无定河边只剩寒滩残戈，而远方春闺的梦里，他还是那个活生生的人——一冷一暖，两相对照。',
    cover_p2='边读诗，边走进陈陶笔下这场无声的悲剧：他不写厮杀、不写眼泪，只把「河边骨」与「梦里人」两个画面剪在一起——读懂了这两句的对照，就读懂了唐代边塞诗里最沉痛的反战名句。',
    end_h2='河边骨 · 梦里人', cn_word='贰',
    words_js="['再入一次无定河边','初识陈陶，尚需共读','渐入诗境，再诵几遍','沙尘渐远，悲意渐深','已解骨梦对切意','一冷一暖，千古同悲']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'誓扫胡尘', jing:'暮色沙场上唐军将士誓师杀敌、奋不顾身，五千身着貂裘锦衣的精锐之师，从此丧身胡地风沙 —— 誓师、激战、丧师，一境写尽。（誓师 · 貂锦 · 胡尘）',
  segs:[
   {c:'誓扫匈奴不顾身，', p:py('shì sǎo xiōng nú bù gù shēn')},
   {c:'五千貂锦丧胡尘。', p:py('wǔ qiān diāo jǐn sàng hú chén')}],
  read:'誓扫匈奴不顾身，五千貂锦丧胡尘。',
  yisi:'将士们发誓要扫平匈奴，奋不顾身；五千身穿貂裘锦衣的精锐之师，从此丧身在胡地风沙之中。——「誓扫」「不顾身」写尽出征的果决豪勇；「五千貂锦」愈见其众、愈见朝廷用兵之重；而「丧胡尘」三字轻轻收束——五千里外的激战、五千人的性命，只化成一个「丧」字。不写交战过程，直接交代结果：前句有多壮，后句就有多痛，落差之大，正是悲剧的开始。',
  zhu:[['陇西行','乐府《相和歌辞》旧题，多写边塞征战之事。陈陶《陇西行四首》约作于唐宣宗大中年间，此为其二，也是四首中最著名的一首'],['誓扫','发誓要扫除、歼灭。一个「誓」字起笔，写尽将士出征时的决绝：不打退敌人，绝不回头'],['不顾身','奋不顾身，把生死置之度外。前四字全是果决与豪勇，为后文的悲剧蓄足了力量'],['貂锦','汉代羽林军衣貂裘、着锦衣，这里借指唐朝精锐的边防军。貂，读 diāo。「五千」言其众——人愈众，后文的「丧」字愈重'],['丧胡尘','丧身于胡尘之中，丧，读 sàng。胡尘，胡地的风沙，兼指北方部族入侵扬起的战尘。前句写出征之壮，此句只以「丧」字收束：五千儿郎，再没有回来']] },
{ name:'春闺梦里', jing:'无定河寒滩上散落着战死者的残戈锈甲，而远方春闺的梦里，他依然是那个活生生的人 —— 骨与梦的对切，全诗最沉痛的一刻。（无定河 · 寒骨 · 春闺 · 梦里人 · 标志性瞬间 · 末境点击画面：河边冷景与闺中梦影冷暖对切）',
  segs:[
   {c:'可怜无定河边骨，', p:py('kě lián wú dìng hé biān gǔ')},
   {c:'犹是春闺梦里人。', p:py('yóu shì chūn guī mèng lǐ rén')}],
  read:'可怜无定河边骨，犹是春闺梦里人。',
  yisi:'可怜啊，无定河边散落着战死者的累累寒骨，他们却依然是春闺里妻子梦中思念的活人。——前句是现实的「骨」：冷月寒滩，残戈锈甲；后句是梦境的「人」：春闺灯暖，梦里人还。一实一虚、一冷一暖，两个画面被诗人剪在一起：家里不知他已战死，还在盼他归来。不说破、不议论，而悲从中来——这两句遂成唐诗中最沉痛的反战名句。',
  zhu:[['无定河','黄河支流，流经今陕西北部，因河道迁徙无常、深浅不定而得名——唐代边塞著名的战场，古诗中常与征戍、寒骨相连'],['骨','战死者的遗骸。诗人不写尸横遍野的惨状，只淡淡点出「河边骨」三个字：誓扫匈奴的五千貂锦，如今成了无定河边无人收殓的寒骨'],['春闺','闺中，指战死者家中的年轻妻子。闺，读 guī。「春」字愈暖，衬得消息愈寒'],['犹是','还是、依然是——在亲人的梦中，他依然活着，依然是那个鲜亮完整的人。亲人至今不知死讯'],['骨与梦的对照','现实中他已是河边之「骨」（实·冷），梦里他仍是闺中之「人」（虚·暖）——诗人把两个时空的画面剪在一起，不说一个「悲」字而沉痛至极。以美梦写惨祸，以「人」写「骨」，正是此诗成为唐代反战名篇的缘故']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「誓扫匈奴不顾身」的下一句是？', o:['五千貂锦丧胡尘','可怜无定河边骨','犹是春闺梦里人'], a:0},
 {q:'「可怜无定河边骨」的下一句是？', o:['五千貂锦丧胡尘','犹是春闺梦里人','誓扫匈奴不顾身'], a:1},
 {q:'「五千貂锦丧胡尘」中，「貂锦」与「丧」的读音和意思都正确的一项是？', o:['貂锦读 diāo jǐn，貂裘锦衣，借指精锐部队；丧读 sàng，丧生——五千精锐一战尽殁','貂锦读 tiáo jǐn，指军中锦旗；丧读 sāng，丧事——五千人举丧致哀','貂锦读 diāo jìn，貂皮做的铠甲；丧读 sàng，丢失——五千副铠甲遗落沙场'], a:0},
 {q:'关于《陇西行》与「无定河」，下列说法正确的是？', o:['本诗是陈陶《陇西行四首》中的第二首；「陇西行」是乐府旧题，多写边塞征战；「无定河」是黄河支流，因河道迁徙、深浅不定而得名，流经唐代边塞战场','「陇西行」是陈陶自创的诗题，专写陇西的风土人情；「无定河」在今浙江，因水乡河道曲折而得名','陈陶是盛唐边塞将领，此诗写于他戍守陇西期间；「无定河」因河边埋骨无数、尸骨无处寻觅而得名'], a:0},
 {q:'「可怜无定河边骨，犹是春闺梦里人」是全诗诗眼。这两句最打动人的写法是？', o:['正面铺写战场上尸横遍野的惨状，用血腥场面直接控诉战争的残酷','把「河边骨」（现实·冷）与「梦里人」（梦境·暖）两个画面并置对照：亲人不知死讯，他仍是梦中活生生的人——不说一个悲字而悲不可遏，沉痛的反战尽在其中','用夸张手法写死者化作春梦回到家人身边，赞美将士虽死犹生、忠魂不灭的豪情'], a:1},
];
"""

SCENES_JS = """/* ================= 陇西行 · 两境场景（大漠金戈·骨梦对切：誓扫胡尘、春闺梦里） =================
   美术立意：大漠金戈色板写「誓师丧尘→骨梦对切」——底色 #120d08、雾 #140d07～#141018 系，
   accent=#c4823a（赭金）只落在军旗/戟锋/人物边缘光/梦烛暖光/UI 上，禁艳金。
   与已有边塞页第一眼可区分：不做孤城/金甲/雪弓刀/梦回连营/望乡闻笛，
   做「五千貂锦冲入胡尘 + 无定河滩残戈锈甲 ↔ 春闺梦影」的沉痛反战叙事；
   白骨意象克制写意：残戈、锈甲、箭镞散落寒滩，不直写尸骸。
   境壹（暮）：残阳沉西、矛林军阵誓师，胡尘漫天卷来，军阵没入尘中（丧胡尘）。
   境贰（夜·标志性瞬间+末境可点击）：无定河寒滩冷月，残戈锈甲半掩寒沙；
   点击：春闺窗影暖光浮现，闺中人与梦里人相对而立，冷滩与暖梦如交叉剪辑般明灭（骨与梦的对切）。 */

/* —— 残阳 makeCanri(o)：暮色里沉西的血色残日（limbTex 日轮+暖晕；fadeK 铁律：初值=最大） —— */
function makeCanri(o){
  o=o||{};
  const r=o.r===undefined?8:o.r, op=o.op===undefined?0.34:o.op;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xc8683a:o.color,
    transparent:true,opacity:op,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0x8a4426:o.hazeC,
    transparent:true,opacity:o.haze===undefined?0.14:o.haze,depthWrite:false,fog:false}));
  haze.scale.set(r*6.0,r*6.0,1); g.add(haze);
  g.update=function(t,k){
    disc.material.opacity=k*op*(0.95+0.05*Math.sin(t*0.3));
    haze.material.opacity=k*(o.haze===undefined?0.14:o.haze)*(0.9+0.1*Math.sin(t*0.27+1.3));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 军旗 makeJunqi(o)：旗杆+杆首鎏金+自写着色器旗面（自杆侧向外波动）——「誓师」 */
const LXQ_FLAG_VERT=`
uniform float uTime; uniform float uSway;
varying vec2 vUv;
void main(){
  vUv=uv;
  vec3 p=position;
  float k=uv.x;
  p.z+=sin(uTime*2.3+k*1.9)*uSway*k;
  p.y+=sin(uTime*1.7+k*2.6)*uSway*0.24*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const LXQ_FLAG_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade;
varying vec2 vUv;
void main(){
  vec3 c=mix(uC,uTipC,vUv.x*0.7+0.3*vUv.y);
  gl_FragColor=vec4(c,uFade);
}`;
function makeJunqi(o){
  o=o||{};
  const h=o.h===undefined?7.2:o.h, w=o.w===undefined?3.2:o.w, hh=o.hh===undefined?2.0:o.hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.045,0.075,h,6);
  pole.translate(0,h*0.5,0); B.put(pole,0x2a1d10);
  const tip=new THREE.SphereGeometry(0.09,8,6); tip.translate(0,h+0.05,0); B.put(tip,0xc4823a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x4a3a22,emissive:0x060402}),{c:0xc4823a,i:o.rim===undefined?0.22:o.rim,p:2.4})));
  const fm=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    vertexShader:LXQ_FLAG_VERT,fragmentShader:LXQ_FLAG_FRAG,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.16:o.sway},
      uC:{value:C(o.c===undefined?0x34120b:o.c)},uTipC:{value:C(o.tip===undefined?0x5e2a12:o.tip)},uFade:{value:1}}});
  const fg=new THREE.PlaneGeometry(w,hh,10,3); fg.translate(w*0.5,0,0);
  const flag=new THREE.Mesh(fg,fm);
  flag.position.set(0.05,h-0.78,0); flag.renderOrder=1;
  g.add(flag); g.userData.fm=fm;
  g.update=function(t){ fm.uniforms.uTime.value=t; };
  g.userData.update=g.update;
  return g;
}

/* —— 矛林 makeQianglin(o)：誓师军阵的矛锋如林（合批 1 mesh，整片微颤）——「五千貂锦」 */
function makeQianglin(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22311:o.seed);
  const n=o.n===undefined?30:o.n, w=o.w===undefined?16:o.w, d=o.d===undefined?7:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, h=3.6+R()*1.6;
    const sp=new THREE.CylinderGeometry(0.030,0.042,h,5);
    sp.translate(x,h*0.5+0.6,z); B.put(sp,0x241a10);
    const hd=new THREE.ConeGeometry(0.055,0.30,5);
    hd.translate(x,h+0.75,z); B.put(hd,shadeColor(0x9a9084,0.75+0.55*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x5a5044,emissive:0x050403}),{c:0xc4823a,i:o.rim===undefined?0.16:o.rim,p:2.8})));
  g.update=function(t){ g.rotation.z=0.004*Math.sin(t*0.7); };
  g.userData.update=g.update;
  return g;
}

/* —— 无定河 makeWudinghe(o)：寒水带+月冷辉（自写着色器，登记 fogShaders 手动雾同步）——「无定河边」 */
const LXQ_RIVER_VERT=`
varying vec3 vW;
void main(){
  vW=(modelMatrix*vec4(position,1.0)).xyz;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);
}`;
const LXQ_RIVER_FRAG=`
uniform float uTime; uniform float uGx; uniform vec3 uC; uniform vec3 uGlint;
uniform vec3 uFogColor; uniform float uFogDensity; uniform float uFade;
varying vec3 vW;
void main(){
  float w1=sin(vW.z*0.55+uTime*0.7+sin(vW.x*0.22)*1.8);
  float w2=sin(vW.x*0.9-uTime*0.42+vW.z*0.15);
  vec3 c=uC*(0.86+0.10*w1+0.06*w2);
  float band=exp(-pow((vW.x-uGx+sin(uTime*0.35)*0.8)*0.16,2.0));
  c+=uGlint*band*(0.42+0.20*sin(uTime*0.9+vW.z*1.7));
  float d=length(cameraPosition-vW);
  float f=1.0-exp(-uFogDensity*uFogDensity*d*d);
  c=mix(c,uFogColor,clamp(f,0.0,1.0));
  gl_FragColor=vec4(c,uFade);
}`;
function makeWudinghe(o){
  o=o||{};
  const w=o.w===undefined?40:o.w, d=o.d===undefined?130:o.d;
  const geo=new THREE.PlaneGeometry(w,d,1,10); geo.rotateX(-Math.PI/2);
  const mt=new THREE.ShaderMaterial({transparent:true,
    vertexShader:LXQ_RIVER_VERT,fragmentShader:LXQ_RIVER_FRAG,
    uniforms:{uTime:{value:0},uC:{value:C(o.c===undefined?0x11141c:o.c)},
      uGlint:{value:C(o.glint===undefined?0x93a2c2:o.glint)},uGx:{value:o.gx===undefined?-14:o.gx},
      uFogColor:{value:C(0x100f14)},uFogDensity:{value:0.0052},uFade:{value:1}}});
  fogShaders.push(mt.uniforms);
  const mesh=new THREE.Mesh(geo,mt); mesh.renderOrder=1;
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t){ mt.uniforms.uTime.value=t; };
  g.userData.update=g.update;
  return g;
}

/* —— 残戈 makeGange(o)：折断的戟——半插寒沙、锈锋犹在（合批 1 mesh）——克制的「河边骨」 */
function makeGange(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22321:o.seed);
  const n=o.n===undefined?5:o.n, w=o.w===undefined?10:o.w, d=o.d===undefined?6:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d;
    if(R()<0.26){   // 倒卧在沙上的一杆
      const a=R()*6.283, L=2.2+R()*1.2;
      B.put(limbGeo([x-Math.cos(a)*L*0.5,0.08,z-Math.sin(a)*L*0.5],[x+Math.cos(a)*L*0.5,0.05,z+Math.sin(a)*L*0.5],
        0.042,0.030,5),shadeColor(0x2c2014,0.75+0.4*R()));
      continue;
    }
    const h=2.4+R()*1.5, dx=(R()-0.5)*0.9, dz=(R()-0.5)*0.5;
    const top=[x+dx,h,z+dz];
    B.put(limbGeo([x,0,z],top,0.05,0.032,5),shadeColor(0x2c2014,0.75+0.5*R()));
    B.put(limbGeo(top,[top[0]+dx*0.5,h+0.55,top[2]+dz*0.5],0.032,0.008,5),shadeColor(0x6a4426,0.8+0.6*R()));
    const sx=(R()<0.5?-1:1)*(0.5+R()*0.3);
    B.put(limbGeo(top,[top[0]+sx,top[1]-0.06,top[2]+(R()-0.5)*0.2],0.028,0.012,5),shadeColor(0x54371f,0.85+0.5*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x443626,emissive:0x050403}),{c:0xc4823a,i:o.rim===undefined?0.14:o.rim,p:2.6})));
  return g;
}

/* —— 锈甲 makeXiujia(o)：半掩寒沙的甲片与锈盔（合批 1 mesh）——克制的「河边骨」之二 */
function makeXiujia(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22331:o.seed);
  const n=o.n===undefined?9:o.n, w=o.w===undefined?9:o.w, d=o.d===undefined?6:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, s=0.16+R()*0.22;
    if(R()<0.62){
      const pl=new THREE.BoxGeometry(s*1.5,s*0.16,s);
      pl.rotateY(R()*6.283); pl.rotateZ((R()-0.5)*0.5); pl.rotateX((R()-0.5)*0.4);
      pl.translate(x,0.05+R()*0.06,z);
      B.put(pl,shadeColor(0x4e3a22,0.7+0.7*R()));
    }else{
      const hm=new THREE.SphereGeometry(s*0.9,8,6,0,6.283,0,1.25);
      hm.rotateY(R()*6.283); hm.translate(x,s*0.30,z);
      B.put(hm,shadeColor(0x3e2e1a,0.8+0.5*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3e3222,emissive:0x040302}),{c:0xc4823a,i:o.rim===undefined?0.13:o.rim,p:2.6})));
  return g;
}

/* 闺中人/梦里人：同一对身影，只在梦光里显形（每次 build 新建材质） */
function lxFigure(scale,pose,who){
  return who==='her'
    ? makeFigure({pose:pose||'独立',robe:0x4a3040,belt:0x6a4a44,skin:0xdcb890,collar:0x8a6a5c,
      hair:0x1a1210,hat:'发髻',beard:false,rimC:0xb87a4a,rim:0.34,noProp:true,scale:scale===undefined?0.92:scale})
    : makeFigure({pose:pose||'独立',robe:0x50412a,belt:0x8a6a3a,skin:0xd9b189,collar:0x9a7a44,
      hair:0x14100a,hat:'幞头',beard:false,rimC:0xc4823a,rim:0.5,noProp:true,scale:scale===undefined?0.96:scale});
}

function bCover(){ // 卷首 · 暮色大漠远望：残阳沉西、尘浪横卷、远处军阵旗影一点
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x100a06,c2:0x201408,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:18,layers:2,peaks:5,seed:22301,color:0x0e0804,atmo:0x2e2114,
    fogK:0.62,glowK:0.08,glow:0xd8864a,y:-10,order:-6});
  ridge.g.position.set(-18,0,-98); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ri=makeCanri({r:9,op:0.36}); ri.position.set(-46,6.5,-95); g.add(ri);
  const dust=makeFlow({n:380,box:[110,14,50],pos:[0,8,-46],color:0x54391f,size:18,speed:5.0,maxA:0.30});
  g.add(dust.points);
  const crowd=makeCrowd({n:12,rect:[-16,-20,30,8],seed:22302,color:0x1c1208,rimC:0xc4823a,rim:0.10,sMin:0.5,sMax:0.62,y:-1.4});
  g.add(crowd.mesh);
  const q1=makeJunqi({seed:22303,h:6.8}); q1.position.set(7,-1.3,-24); g.add(q1);
  const mist=makeMist({n:6,spread:[220,14,84],pos:[0,6,-60],scale:72,color:0x4e341c,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[170,18,70],pos:[0,9,-34],color:0x8a6038,size:4.4,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x0c0805,seed:22304,rim:0.09,rimC:0xc4823a});
  fg1.g.position.set(-11,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x0c0805,seed:22305,rim:0.09,rimC:0xc4823a});
  fg2.g.position.set(13,-1.8,13); g.add(fg2.g);
  addLights(g,{c:0xb06a38,i:0.36,p:[-48,38,-30]},{c:0x2c1c0e,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); grd.update(); ri.update(t,k); dust.update(t);
    crowd.update(t); q1.update(t); mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bShisao(){ // 壹 · 誓扫胡尘 —— 誓扫匈奴不顾身，五千貂锦丧胡尘：暮色誓师，军阵没入胡尘
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x120b06,c2:0x241608,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:15,layers:2,peaks:5,seed:22341,color:0x120a05,atmo:0x2e2114,
    fogK:0.62,glowK:0.10,glow:0xd8864a,y:-11,order:-6});
  ridge.g.position.set(-24,0,-104); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ri=makeCanri({r:8}); ri.position.set(-42,6.5,-92); g.add(ri);
  /* 将领：立于丘上举臂誓师，面朝身后军阵 */
  const rock=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x0e0906,seed:22342,rim:0.12,rimC:0xc4823a});
  rock.g.position.set(-5.6,-1.5,-7.5); g.add(rock.g);
  const poet=makeFigure({pose:'指月',robe:0x3a2c1a,belt:0x8a6a3a,skin:0xd9b189,collar:0x7a5c34,
    hair:0x1a140c,hat:'幞头',beard:true,rimC:0xc4823a,rim:0.5,noProp:true,scale:1.85});
  poet.position.set(-4.8,-0.30,-7.2); poet.rotation.y=2.6; g.add(poet);
  /* 矛林军阵：誓师之后冲入胡尘 */
  const crowd=makeCrowd({n:24,rect:[-14,-15,26,9],seed:22343,color:0x241608,rimC:0xc4823a,rim:0.16,sMin:0.62,sMax:0.78,y:-1.35});
  g.add(crowd.mesh);
  const ql=makeQianglin({n:26,w:20,d:8,seed:22344}); ql.position.set(-1,-1.1,-11); g.add(ql);
  const q1=makeJunqi({seed:22345,h:7.6}); q1.position.set(6.5,-1.2,-9.5); g.add(q1);
  const q2=makeJunqi({seed:22346,h:6.4,w:2.6,hh:1.7}); q2.position.set(-10.5,-1.3,-14); g.add(q2);
  /* 胡尘：漫天尘浪自远处卷来，吞没军阵尽头——「丧胡尘」 */
  const dust=makeFlow({n:420,box:[92,16,44],pos:[0,7,-44],color:0x5a4026,size:20,speed:4.4,maxA:0.34});
  g.add(dust.points);
  const dust2=makeFlow({n:200,box:[54,10,22],pos:[0,4.5,-28],color:0x6a4c2c,size:13,speed:6.2,maxA:0.22});
  g.add(dust2.points);
  const mist=makeMist({n:6,spread:[210,14,80],pos:[0,6,-58],scale:70,color:0x54381e,op:0.13});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[160,16,64],pos:[0,8,-30],color:0x9a7040,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0d0805,seed:22347,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x0d0805,seed:22348,rim:0.10,rimC:0xc4823a});
  fg2.g.position.set(12.5,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0xb06a38,i:0.44,p:[-52,34,-40]},{c:0x31200f,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); grd.update(); ri.update(t,k); poet.update(t,k); rock.update(t,k);
    crowd.update(t); ql.update(t); q1.update(t); q2.update(t);
    dust.update(t); dust2.update(t); mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bMengli(){ // 贰（末境·可点击）· 春闺梦里 —— 可怜无定河边骨，犹是春闺梦里人：骨与梦的对切
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d0c10,c2:0x1a1614,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:13,layers:2,peaks:4,seed:22351,color:0x0b0a0e,atmo:0x33261a,
    fogK:0.60,glowK:0.06,glow:0xc49558,y:-10,order:-6});
  ridge.g.position.set(-8,0,-112); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 无定河：寒水自远弯来，月光在水面拉出一条冷辉 */
  const he=makeWudinghe({w:40,d:130,gx:-16}); he.position.set(-16,-1.55,-58); he.rotation.y=-0.10; g.add(he);
  /* 残戈锈甲：写意的「河边骨」——散落寒滩，不直写尸骸 */
  const ge1=makeGange({n:4,w:8,d:5,seed:22352}); ge1.position.set(-3.2,-1.35,-8.6); ge1.rotation.y=0.5; g.add(ge1);
  const ge2=makeGange({n:3,w:9,d:5,seed:22353}); ge2.position.set(2.8,-1.4,-13.5); ge2.rotation.y=-0.4; g.add(ge2);
  const jia=makeXiujia({n:9,w:10,d:7,seed:22354}); jia.position.set(-0.8,-1.42,-9.8); g.add(jia);
  const jia2=makeXiujia({n:6,w:12,d:8,seed:22355}); jia2.position.set(-4.5,-1.45,-18); g.add(jia2);
  const mist=makeMist({n:7,spread:[220,12,80],pos:[0,4.5,-56],scale:70,color:0x2a2a34,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[150,14,64],pos:[0,6.5,-28],color:0x8a8a9a,size:3.8,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x0a090c,seed:22356,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(-11.5,-1.8,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:8,d:4,color:0x0a090c,seed:22357,rim:0.10,rimC:0xc4823a});
  fg2.g.position.set(12,-1.7,12); g.add(fg2.g);
  /* —— 标志性瞬间：春闺梦影（点击后浮现，与冷滩交叉明灭） —— */
  const dream=new THREE.Group(); dream.position.set(6.4,-1.72,-14.5); g.add(dream);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb87a3a,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(26,22,1); halo.position.set(0,1.8,-0.2); halo.renderOrder=4; dream.add(halo);
  const core=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8b070,
    transparent:true,opacity:0.55,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  core.scale.set(13,11,1); core.position.set(0,2.2,-0.4); core.renderOrder=4; dream.add(core);
  /* 闺窗：窗框+双棂（暗木格剪影，暖光自窗内透出，格后是梦） */
  const B=new GeoBag();
  const f1=new THREE.BoxGeometry(0.24,4.6,0.16); f1.translate(-2.68,0,0); B.put(f1,0x241a12);
  const f2=new THREE.BoxGeometry(0.24,4.6,0.16); f2.translate(2.68,0,0); B.put(f2,0x241a12);
  const f3=new THREE.BoxGeometry(5.6,0.24,0.16); f3.translate(0,2.3,0); B.put(f3,0x241a12);
  const f4=new THREE.BoxGeometry(5.6,0.24,0.16); f4.translate(0,-2.3,0); B.put(f4,0x241a12);
  const m1=new THREE.BoxGeometry(0.10,4.4,0.10); m1.translate(-1.2,0,0); B.put(m1,0x2c2016);
  const m2=new THREE.BoxGeometry(0.10,4.4,0.10); m2.translate(1.2,0,0); B.put(m2,0x2c2016);
  const m3=new THREE.BoxGeometry(5.2,0.10,0.10); m3.translate(0,0.6,0); B.put(m3,0x2c2016);
  const m4=new THREE.BoxGeometry(5.2,0.10,0.10); m4.translate(0,-0.6,0); B.put(m4,0x2c2016);
  const lat=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x3a2c1c,emissive:0x060402,transparent:true,opacity:0.96}));
  lat.position.z=-0.15;
  dream.add(lat);
  /* 闺中人与梦里人：窗前相对而立 */
  const her=lxFigure(0.92,'独立','her'); her.position.set(1.15,0,0.9); her.rotation.y=-0.55; dream.add(her);
  const him=lxFigure(0.96,'独立','him'); him.position.set(-1.05,0,0.9); him.rotation.y=Math.PI+0.5; dream.add(him);
  her.traverse(o=>{ const m=o.material; if(m&&!m.isShaderMaterial){ m.transparent=true; } });
  him.traverse(o=>{ const m=o.material; if(m&&!m.isShaderMaterial){ m.transparent=true; } });
  const herMat=her.children[0].material, himMat=him.children[0].material;
  const latMat=lat.material;
  /* 点击前整组可见性硬关（visible=false 杜绝任何渲染时序下的幽灵残影），点击后再显形 */
  const dreamKids=[halo,core,lat,her,him];
  dreamKids.forEach(function(c){ c.visible=false; });
  /* 梦烛点光（点击后随交叉明灭涨落）+ 冷滩常驻冷光 */
  const pl=new THREE.PointLight(0xd89650,0.9,30); pl.position.set(0,3.4,2.4); dream.add(pl);
  const cl=new THREE.PointLight(0x7a86a8,0.5,34); cl.position.set(-4,5,-8); g.add(cl);
  addLights(g,{c:0x8a96b8,i:0.34,p:[-42,46,-30]},{c:0x1c1e28,i:0.52});
  /* 交叉剪辑明灭：u∈[0,reveal] 内再随时间缓慢涨落（每帧写 opacity/intensity 全乘 fadeK） */
  const setDream=function(t){
    const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    const pl2=0.5+0.5*Math.sin(t*0.5);
    const u=ctl.reveal*(0.74+0.26*pl2);
    halo.material.opacity=k*0.30*u;
    core.material.opacity=k*0.55*u;
    herMat.opacity=k*u;
    himMat.opacity=k*0.94*u;
    latMat.opacity=k*0.96*u;
    pl.intensity=k*0.9*u;
    cl.intensity=k*(0.5-0.20*ctl.reveal*pl2);
    dream.position.y=-1.72+0.05*Math.sin(t*0.45);
  };
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/2.4);
      setDream(t);
      ridge.update(t,0); grd.update(); he.update(t);
      mist.update(t,k); motes.update(t);
      her.update(t,k); him.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        dreamKids.forEach(function(c){ c.visible=true; });
        setAmbience(0.14);
        pluck(2,0.0,0.10); pluck(4,0.22,0.08); pluck(1,0.5,0.08);
        const fl=$('#flash'); fl.textContent='可怜无定河边骨 犹是春闺梦里人';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0c0806),hor:C(0x2a1a0e),bot:C(0x090604),fog:C(0x140d07),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-70,26,-200),ms:0.5,mph:0.42,mhaze:0.18,dirC:C(0xb08850),dirI:0.34,
  dirP:new THREE.Vector3(-45,55,-25),ambC:C(0x2c2014),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,46],t:[0,9,38],lf:[1.5,8,-26],lt:[-2.5,8.5,-38]},
  sky:()=>SK({fd:0.0048,star:0.12,hor:C(0x3a2010)}) },
{ name:'誓扫胡尘',dwell:16,river:0.02,build:bShisao,
  cam:{f:[0,6.8,26],t:[1.5,6.2,15],lf:[-2,6,-14],lt:[-6,6.5,-30]},
  sky:()=>SK({top:C(0x140b06),hor:C(0x54290f),bot:C(0x0d0704),fog:C(0x170e08),fd:0.0060,star:0.05,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.03,
    dirC:C(0xb06a38),dirI:0.42,dirP:new THREE.Vector3(-52,34,-40),
    ambC:C(0x31200f),ambI:0.55}) },
{ name:'春闺梦里',dwell:20,river:0.02,build:bMengli,
  cam:{f:[0,4.6,15],t:[0.6,4.4,7.5],lf:[0.8,4.4,-6],lt:[3.4,4.8,-14]},
  sky:()=>SK({top:C(0x0a0c12),hor:C(0x232028),bot:C(0x08070a),fog:C(0x100f14),fd:0.0052,star:0.30,
    ms:0.55,mph:0.28,mhaze:0.14,moon:new THREE.Vector3(-58,44,-190),
    dirC:C(0x8a96b8),dirI:0.34,dirP:new THREE.Vector3(-42,46,-30),
    ambC:C(0x1c1e28),ambI:0.52}) },
];
"""
