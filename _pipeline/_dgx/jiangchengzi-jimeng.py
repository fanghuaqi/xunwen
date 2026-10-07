# -*- coding: utf-8 -*-
"""jiangchengzi-jimeng.py —— 《江城子·乙卯正月二十日夜记梦》（宋·苏轼，no.175，水墨夜思）生成配置
三境（queue 分境为准）：生死茫茫（十年之隔·千里孤坟·凄凉无处话）、幽梦还乡（标志性瞬间：小轩窗暖光·窗内梳妆影——
全页唯一暖点，冷暖对照即「生死之隔」）、明月松冈（末境点击：窗内梳妆影凝现+明月照短松冈）。
全页冷银水墨，禁金；唯有小轩窗一盏暖光是「家」的温度（同 jingyesi 灯火先例：月是冷的，家是暖的）。"""

META = dict(
    N=3, slug='jiangchengzi-jimeng', title='江城子·乙卯正月二十日夜记梦', dyn='宋 · 苏轼', brand_author='苏轼',
    gold_rgb='184,196,221',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b8c4dd; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(184,196,221,.26);
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
    tip='轻点画面 / 按空格 —— 轩窗梳妆影凝现，明月照短松冈',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看梳妆影凝现、明月照短松冈',
    cover_read='江城子。宋，苏轼。十年生死两茫茫，不思量，自难忘。千里孤坟，无处话凄凉。纵使相逢应不识，尘满面，鬓如霜。夜来幽梦忽还乡，小轩窗，正梳妆。相顾无言，惟有泪千行。料得年年肠断处，明月夜，短松冈。',
    cover_p1='三重意境，随词句次第展开：十年生死相隔，渺茫如烟海，不去想、也自难忘，千里孤坟之外满腹凄凉无处可诉；纵使相逢你也认不出我了吧——尘满面、鬓如霜，而夜来幽梦忽然还乡，小轩窗前，你正梳妆；梦中相顾无言、泪落千行，料想年年令人肠断的，还是那明月夜里的短松冈。',
    cover_p2='边读词，边走进这场冷月照孤坟的十年之梦，看小轩窗前那一盏暖光——茫茫生死里唯一的暖。',
    end_h2='明月 · 松冈', cn_word='三',
    words_js="['再游一次，梦里相逢','初识此词，尚需共读','渐入佳境，再诵几遍','词境渐深，泪光点点','已解十年生死之痛','明月松冈，此情不灭']",
    sky_atmo='0x1c2433',
)

POEM_JS = """const POEM = [
{ name:'生死茫茫', jing:'十年生死相隔，音容渺茫 —— 不思量，自难忘；千里孤坟，凄凉无处话。（孤坟 · 凄凉 · 茫茫）',
  segs:[
   {c:'十年生死两茫茫，', p:py('shí nián shēng sǐ liǎng máng máng')},
   {c:'不思量，', p:py('bù sī liáng')},
   {c:'自难忘。', p:py('zì nán wàng')},
   {c:'千里孤坟，', p:py('qiān lǐ gū fén')},
   {c:'无处话凄凉。', p:py('wú chù huà qī liáng')}],
  read:'十年生死两茫茫，不思量，自难忘。千里孤坟，无处话凄凉。',
  yisi:'十年来生死殊途，一在天之涯、一在地之下，两下里音容渺茫。不必刻意思量，你的影子也自然而然难以忘怀。你的孤坟远在千里之外，我竟连一处可以诉说这满腹凄凉的地方都没有。——生者与死者，被十年光阴与千里山河同时隔开。',
  zhu:[['乙卯','宋熙宁八年（1075）。时苏轼知密州，正月二十日夜梦见亡妻王弗，醒后写下此词，题曰「记梦」'],
       ['王弗','苏轼结发之妻，十六岁嫁苏轼，夫妻情笃；治平二年（1065）病逝，归葬四川眉州祖茔，与苏轼任所相隔数千里'],
       ['茫茫','渺茫无边之貌；生死阻隔，音容两不可寻'],
       ['思量','想念、记挂；「量」在此读 liáng，不读 liàng'],
       ['孤坟','王弗孤零零的坟墓。坟远千里，无从凭吊，凄凉更无处诉说']] },
{ name:'幽梦还乡', jing:'纵使相逢，你也认不出我了吧 —— 尘满面、鬓如霜；夜来幽梦忽还乡，小轩窗前，你正梳妆。（幽梦 · 轩窗 · 梳妆）',
  segs:[
   {c:'纵使相逢应不识，', p:py('zòng shǐ xiāng féng yīng bù shí')},
   {c:'尘满面，', p:py('chén mǎn miàn')},
   {c:'鬓如霜。', p:py('bìn rú shuāng')},
   {c:'夜来幽梦忽还乡，', p:py('yè lái yōu mèng hū huán xiāng')},
   {c:'小轩窗，', p:py('xiǎo xuān chuāng')},
   {c:'正梳妆。', p:py('zhèng shū zhuāng')}],
  read:'纵使相逢应不识，尘满面，鬓如霜。夜来幽梦忽还乡，小轩窗，正梳妆。',
  yisi:'即便我们真能相逢，恐怕你也认不出我了：十年来我风尘仆仆、满面尘土，两鬓已经白得像霜雪。昨夜我在幽渺迷离的梦中忽然回到了故乡，看见小轩窗前，你还像生前一样，正对着晨光梳妆。——不敢想重逢，是因为怕；偏偏梦里还乡，是因为忘不掉。',
  zhu:[['纵使相逢应不识','生死茫茫，纵然重逢也怕彼此认不出；「应」是推测语气，想必、大概，读 yīng'],
       ['尘满面，鬓如霜','苏轼因反对新法自请外放，辗转州县、奔波劳碌，未老先衰；既是实写风尘，也是仕途坎坷、心境苍凉的写照'],
       ['幽梦','幽渺迷离的梦；梦境虚幻难凭，故曰「幽」'],
       ['小轩窗','小室的窗。轩，有窗的小室或长廊，此处指王弗生前居室的窗前'],
       ['正梳妆','梦见妻子临窗对镜梳妆，如在生前——全词最动人的一幕，家常一瞬，抵过十年']] },
{ name:'明月松冈', jing:'千言万语，相对无言，唯有泪落千行 —— 料想年年肠断之处，正是明月照着的短松冈。（无言 · 泪千行 · 短松冈）',
  segs:[
   {c:'相顾无言，', p:py('xiāng gù wú yán')},
   {c:'惟有泪千行。', p:py('wéi yǒu lèi qiān háng')},
   {c:'料得年年肠断处，', p:py('liào dé nián nián cháng duàn chù')},
   {c:'明月夜，', p:py('míng yuè yè')},
   {c:'短松冈。', p:py('duǎn sōng gāng')}],
  read:'相顾无言，惟有泪千行。料得年年肠断处，明月夜，短松冈。',
  yisi:'梦中相见，千言万语却不知从何说起，只有你望着我、我望着你，默默无言，泪水落了千行。料想年年岁岁令人柔肠寸断的地方，就是那一轮冷月照着、长着矮小松树的坟冈吧。——梦总会醒，而思念年年；月照孤坟，是死者长眠处的清冷，也是生者长夜里的断肠。',
  zhu:[['相顾无言','夫妻梦中重逢，千种思念无从说起，惟有默然相望；此时无声胜有声'],
       ['泪千行','泪水纵横成行，极言哀痛之深；「行」读 háng，不读 xíng'],
       ['料得','料想、推测；梦醒之后替对方悬想，一说兼摄自己年年之断肠'],
       ['肠断处','令人极度悲伤之处'],
       ['短松冈','长着矮小松树的山冈，指王弗坟茔所在。明月夜夜照孤坟，凄清至极，与上阕「千里孤坟」遥相呼应']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「十年生死两茫茫」的下一句是？', o:['不思量，自难忘','千里孤坟，无处话凄凉','纵使相逢应不识'], a:0},
 {q:'「夜来幽梦忽还乡」的下一句是？', o:['相顾无言，惟有泪千行','小轩窗，正梳妆','尘满面，鬓如霜'], a:1},
 {q:'「不思量，自难忘」中「量」的正确读音和意思是？', o:['liáng，想念、记挂','liàng，数量、测量','liǎng，两次、再三'], a:0},
 {q:'词题「乙卯正月二十日夜记梦」——这一夜词人梦见的是？', o:['贬谪途中久别的弟弟苏辙','他病逝十年的结发妻子王弗','早已离散的同窗故友'], a:1},
 {q:'全词以「料得年年肠断处，明月夜，短松冈」作结，主要表达的是？', o:['对故乡山水风物的深切怀念','宦海沉浮、壮志难酬的愤懑','对亡妻深挚的悼念与生死相隔的无尽哀思'], a:2},
];
"""

SCENES_JS = """/* ================= 江城子·乙卯正月二十日夜记梦 · 三境场景（水墨夜思：冷银、孤坟、轩窗暖光、短松冈） ================= */

/* 泪千行：竖直泪光细痕（缓慢下坠 + 微微偏摆），Normal 混合不吃雾 */
const LEI_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uSpeed*(0.55+0.9*fract(aSeed*7.77));
  p.y=mod(position.y-uTime*sp,uBox.y);
  p.x+=sin(uTime*0.5+aSeed*47.0)*0.35;
  vA=smoothstep(0.0,0.8,p.y)*smoothstep(uBox.y,uBox.y-1.0,p.y)*(0.30+0.70*fract(aSeed*13.3));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const LEI_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-0.5;
  float d=length(q*vec2(2.6,0.9));
  float a=smoothstep(0.5,0.08,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLei(o){
  o=o||{};
  const n=o.n===undefined?90:o.n, box=o.box||[26,12,14], pos=o.pos||[-7,6,-13];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.2:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.9:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0xcdd9ec:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.20:o.maxA}},
    vertexShader:LEI_VERT,fragmentShader:LEI_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* 短松冈：土冈 + 封土坟丘 + 石碑 + 数株矮松（冷墨色，禁金），合批 1 mesh */
function makeSongGang(o){
  o=o||{};
  const n=o.pines===undefined?3:o.pines, R=seedRnd(o.seed===undefined?75180:o.seed);
  const B=new GeoBag();
  const mound=new THREE.SphereGeometry(o.r===undefined?5.2:o.r,14,10);
  mound.scale(1,0.36,0.86); mound.translate(0,-0.2,0); B.put(mound,0x0b111c);
  const tomb=new THREE.SphereGeometry(1.6,12,8); tomb.scale(1,0.55,0.9);
  tomb.translate(0,1.18,-0.6); B.put(tomb,0x0d1420);
  const stele=new THREE.BoxGeometry(0.62,1.50,0.16); stele.rotateZ(0.04);
  stele.translate(0,1.22,0.92); B.put(stele,0x1a2331);
  const cap=new THREE.BoxGeometry(0.80,0.12,0.30); cap.rotateZ(0.04);
  cap.translate(0,2.02,0.92); B.put(cap,0x232e42);
  for(let i=0;i<n;i++){
    const a=R()*6.283, rr=2.2+R()*2.6, px=Math.cos(a)*rr, pz=Math.sin(a)*rr*0.8;
    const h=0.5+R()*0.5;
    const trunk=new THREE.CylinderGeometry(0.07,0.11,h,6); trunk.translate(px,h/2,pz); B.put(trunk,0x10151f);
    let cy=h;
    for(let k=0;k<3;k++){
      const cr=(1.15-k*0.30)*(0.8+R()*0.4), ch=0.75*(0.8+R()*0.4);
      const cone=new THREE.ConeGeometry(cr,ch,7); cone.translate(px,cy+ch*0.42,pz); B.put(cone,0x0d141d);
      cy+=ch*0.62;
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.22,p:2.4})));
  return {g};
}

/* 小轩窗：屋舍一角（前墙留窗口）+ 暖纸窗 + 窗内梳妆影 + 窗棂 —— 全页唯一暖点。
   梳妆影 opacity 由各境按 fadeK 自控（幽梦朦胧 / 点击凝现），暖光呼吸由 glow/light 承担。 */
function makeXuanchuang(o){
  o=o||{};
  const B=new GeoBag(), wallC=0x111722, wall2=0x0c101a, roofC=0x090d15;
  /* 前墙（x -3.7..3.7，留出轩窗口 x -0.15..2.35 / y 1.5..3.65） */
  const wl=new THREE.BoxGeometry(3.55,4.7,0.34); wl.translate(-1.925,2.35,0); B.put(wl,wallC);
  const wr=new THREE.BoxGeometry(1.35,4.7,0.34); wr.translate(3.025,2.35,0); B.put(wr,wallC);
  const wt=new THREE.BoxGeometry(2.5,1.05,0.34); wt.translate(1.1,4.175,0); B.put(wt,wallC);
  const wb=new THREE.BoxGeometry(2.5,1.5,0.34); wb.translate(1.1,0.75,0); B.put(wb,wallC);
  /* 侧墙 + 山墙 + 两坡顶 + 正脊 */
  [1,-1].forEach(function(s){
    const side=new THREE.BoxGeometry(0.36,4.4,5.6); side.translate(s*3.68,2.2,-2.6); B.put(side,wall2);
    const gab=new THREE.BoxGeometry(0.36,1.7,0.36); gab.translate(s*3.68,5.15,-2.6); B.put(gab,wall2);
  });
  const rl=new THREE.BoxGeometry(4.35,0.22,7.2); rl.rotateZ(0.453); rl.translate(-2.0,5.3,-2.6); B.put(rl,roofC);
  const rr=new THREE.BoxGeometry(4.35,0.22,7.2); rr.rotateZ(-0.453); rr.translate(2.0,5.3,-2.6); B.put(rr,roofC);
  const ridgeB=new THREE.BoxGeometry(0.30,0.30,7.4); ridgeB.translate(0,6.26,-2.6); B.put(ridgeB,roofC);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.20,p:2.5})));
  /* 窗框 + 窗棂（格心） */
  const FB=new GeoBag(), frC=0x1d2532, latC=0x0a0e15;
  const ft=new THREE.BoxGeometry(2.78,0.14,0.42); ft.translate(1.1,3.71,0); FB.put(ft,frC);
  const fb=new THREE.BoxGeometry(2.78,0.14,0.42); fb.translate(1.1,1.44,0); FB.put(fb,frC);
  const fl=new THREE.BoxGeometry(0.14,2.43,0.42); fl.translate(-0.21,2.575,0); FB.put(fl,frC);
  const frg=new THREE.BoxGeometry(0.14,2.43,0.42); frg.translate(2.41,2.575,0); FB.put(frg,frC);
  [0.48,-0.48].forEach(function(dx){
    const bar=new THREE.BoxGeometry(0.07,2.15,0.07); bar.translate(1.1+dx,2.575,0.12); FB.put(bar,latC);
  });
  const hbar=new THREE.BoxGeometry(2.5,0.07,0.07); hbar.translate(1.1,2.575,0.12); FB.put(hbar,latC);
  const frame=new THREE.Mesh(mergeGeos(FB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
      specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.24,p:2.4}));
  g.add(frame);
  /* 暖纸窗（页内唯一暖色：灯光透过窗纸） */
  const paperMat=new THREE.MeshBasicMaterial({color:0xd99a55,fog:false,transparent:true,opacity:0.92,depthWrite:false});
  const paper=new THREE.Mesh(new THREE.PlaneGeometry(2.5,2.15),paperMat);
  paper.position.set(1.1,2.575,-0.10); g.add(paper);
  /* 梳妆影：窗内剪影（发髻 + 抬臂拢发），剪影暖黑而非冷黑；上身抬高让窗口读到「腰上人影」 */
  const SB=new GeoBag(), silC=0x120b06;
  const torso=new THREE.CylinderGeometry(0.44,0.60,1.30,10); torso.translate(1.1,1.95,0.02); SB.put(torso,silC);
  const shd=new THREE.SphereGeometry(0.34,8,6); shd.scale(1.5,0.6,0.8); shd.translate(1.1,2.62,0.02); SB.put(shd,silC);
  const neck=new THREE.CylinderGeometry(0.10,0.12,0.22,6); neck.translate(1.1,2.76,0.02); SB.put(neck,silC);
  const head=new THREE.SphereGeometry(0.27,10,8); head.scale(0.95,1.05,0.95); head.translate(1.12,3.06,0.02); SB.put(head,silC);
  const bun=new THREE.SphereGeometry(0.13,8,6); bun.translate(1.12,3.34,-0.03); SB.put(bun,silC);
  SB.put(limbGeo([1.38,2.55,0.05],[1.44,3.14,0.10],0.075,0.055,6),silC);
  const hand=new THREE.SphereGeometry(0.07,6,5); hand.translate(1.44,3.16,0.10); SB.put(hand,silC);
  const silMat=new THREE.MeshBasicMaterial({color:0x120b06,transparent:true,opacity:0.95,depthWrite:false});
  const sil=new THREE.Mesh(mergeGeos(SB.list),silMat);
  sil.scale.z=0.25; sil.renderOrder=1; g.add(sil);   // 压扁成剪影贴片（不凸出墙面），并在窗纸之后绘制
  /* 暖光呼吸：外辉（冠于窗顶，不淹没窗内人影）+ 地面光池 + 暖点光 */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xeab36a,
    transparent:true,opacity:0.40,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(6.0,6.0,1); glow.position.set(1.1,3.4,0.9); glow.renderOrder=3; g.add(glow);
  const poolGeo=new THREE.CircleGeometry(4.2,24); poolGeo.rotateX(-Math.PI/2);
  const poolMat=new THREE.MeshBasicMaterial({color:0xd99a55,transparent:true,opacity:0.13,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const pool=new THREE.Mesh(poolGeo,poolMat); pool.position.set(1.1,0.04,3.4); pool.renderOrder=2; g.add(pool);
  const light=new THREE.PointLight(0xd99a55,1.45,30); light.position.set(1.1,2.3,3.0); g.add(light);
  return {g,silMat,glowMat:glow.material,poolMat,light};
}

function bCover(){ // 封面 · 寒水孤坟 —— 十年生死，冷月照孤坟
  const g=new THREE.Group();
  const water=makeWater({size:320,seg:76,amp:0.14,freq:0.18,speed:0.36,flow:[0.1,0.38],spec:1.5,
    deep:0x0a0f18,shallow:0x16202f,skyc:0x1e2c40,moonDir:[-30,102,-184]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:18,layers:2,peaks:5,seed:75175,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  const gang=makeSongGang({pines:2,seed:75181});
  gang.g.position.set(-19,0,-52); gang.g.scale.setScalar(1.2); g.add(gang.g);
  const fig=makeFigure({pose:'独立',robe:0x1b2536,belt:0x54607a,skin:0xd0bda6,collar:0xa6b3ca,
    hair:0x4a5164,hat:'发髻',beard:true,rimC:0xb8c4dd,rim:0.42,noProp:true,scale:1.25});
  fig.position.set(3,0,-30); fig.rotation.y=0.35; g.add(fig);
  const fgRock=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:75182,rim:0.14});
  fgRock.g.position.set(-14,-1.6,34); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:10,d:6,color:0x04060a,seed:75183,sway:0.8});
  reeds.g.position.set(13,-1.1,30); g.add(reeds.g);
  const mist=makeMist({n:7,spread:[240,24,130],pos:[0,10,-54],scale:78,color:0x8fa0ba,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:55,box:[190,30,110],pos:[0,11,-42],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.30});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.40,p:[-30,80,-40]},{c:0x18202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); motes.update(t);
    fgRock.update(t,k); reeds.update(t,k);
    fig.userData.update(t,k);
  }};
}

function bShengsi(){ // 一 · 生死茫茫 —— 千里孤坟、凄凉无处话
  const g=new THREE.Group();
  const water=makeWater({size:340,seg:80,amp:0.15,freq:0.17,speed:0.38,flow:[0.1,0.4],spec:1.6,
    deep:0x0a0f18,shallow:0x17212f,skyc:0x20304a,moonDir:[-38,104,-182]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:17,layers:2,peaks:4,seed:75176,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-128); g.add(ridge.g);
  /* 千里孤坟：隔水远冈上的孤坟与矮松 */
  const gang=makeSongGang({pines:2,seed:75184});
  gang.g.position.set(-21,0,-47); gang.g.scale.setScalar(1.35); g.add(gang.g);
  /* 十年尘面的词人：立于寒水之滨，望向孤坟 */
  const fig=makeFigure({pose:'独立',robe:0x1c2637,belt:0x55627c,skin:0xd0bda6,collar:0xaab8cf,
    hair:0x4a5164,hat:'发髻',beard:true,rimC:0xb8c4dd,rim:0.50,noProp:true,scale:1.85});
  fig.position.set(2.5,0,-12.5); fig.rotation.y=0.55; g.add(fig);
  /* 茫茫：生死之隔的茫茫雾海缓缓横流 */
  const flow=makeFlow({n:170,box:[130,16,54],pos:[0,9,-38],color:0x9fb0c8,size:22,speed:1.7,maxA:0.17});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[220,20,116],pos:[0,9,-50],scale:74,color:0x8fa0ba,op:0.075});
  g.add(mist.g);
  const motes=makeGlow({n:50,box:[150,22,80],pos:[0,9,-28],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.26});
  g.add(motes.points);
  const reeds=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:75185,sway:0.8});
  reeds.g.position.set(-13,-1.2,11); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:75186,rim:0.14});
  rk.g.position.set(14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0x8fa4c4,i:0.44,p:[-36,84,-34]},{c:0x19202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); flow.update(t); mist.update(t,k); motes.update(t);
    reeds.update(t,k); rk.update(t,k);
    fig.userData.update(t,k);
  }};
}

function bHuanxiang(){ // 二（标志性瞬间）· 幽梦还乡 —— 尘面霜鬓之外，小轩窗一盏暖光，窗内梳妆影
  const g=new THREE.Group();
  const grd=makeGround({r:140,c1:0x080b11,c2:0x0f1520});
  grd.mesh.position.y=-0.15; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:14,layers:2,peaks:4,seed:75177,color:0x070a10,atmo:0x1e2636,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 故居小轩窗：全页唯一暖点（暖纸窗 + 窗内梳妆影朦胧可见） */
  const hut=makeXuanchuang();
  hut.g.position.set(5.8,0,-17); hut.g.rotation.y=-0.5; hut.g.scale.setScalar(1.35); g.add(hut.g);
  /* 梦里的词人：霜鬓尘面，立在院中望窗 */
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x586680,skin:0xd0bda6,collar:0xaab8cf,
    hair:0x535b6e,hat:'发髻',beard:true,rimC:0xb8c4dd,rim:0.55,noProp:true,scale:1.9});
  fig.position.set(-3.6,0,-11.8); fig.rotation.y=-0.85; g.add(fig);
  /* 矮院墙 */
  const wallB=new GeoBag(), wc=0x0b0f16;
  const wl=new THREE.BoxGeometry(26,2.1,0.9); wl.translate(-3,1.05,-24); wallB.put(wl,wc);
  const cap=new THREE.BoxGeometry(26.6,0.20,1.3); cap.translate(-3,2.2,-24); wallB.put(cap,shadeColor(wc,1.5));
  [1,-1].forEach(function(s){
    const post=new THREE.BoxGeometry(1.0,2.6,1.2); post.translate(-3+s*11,1.3,-23.8); wallB.put(post,shadeColor(wc,1.15));
  });
  const wall=new THREE.Mesh(mergeGeos(wallB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.16,p:2.4}));
  g.add(wall);
  /* 老树移至屋后远处（避免枝影挡窗），远村人影（梦里故乡夜色） */
  const tree=makeForeground({kind:'树枝',n:2,w:10,d:4,color:0x04060a,seed:75187,sway:1.1,rim:0.14});
  tree.g.position.set(16,0,-30); g.add(tree.g);
  const crowd=makeCrowd({n:3,rect:[12,-30,14,4],seed:75188,color:0x10151f,rimC:0x8fa4c4,
    rim:0.12,sMin:0.38,sMax:0.52,y:0});
  g.add(crowd.mesh);
  /* 霜晶微闪 */
  const frost=makeGlow({n:40,box:[70,12,50],pos:[0,5,-14],color:0xbfcde4,size:4.5,speed:0.12,rise:0.05,maxA:0.26});
  g.add(frost.points);
  const mist=makeMist({n:5,spread:[200,18,100],pos:[0,8,-46],scale:70,color:0x8fa0ba,op:0.06});
  g.add(mist.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:75189,rim:0.14});
  fgRock.g.position.set(-15,-1.6,12); g.add(fgRock.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:9,d:6,color:0x04060a,seed:75190,sway:0.7});
  reeds.g.position.set(14,-1.1,10); g.add(reeds.g);
  addLights(g,{c:0x8fa4c4,i:0.42,p:[30,80,-30]},{c:0x1a2230,i:0.56});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); frost.update(t); crowd.update(t);
    tree.update(t,k); fgRock.update(t,k); reeds.update(t,k);
    fig.userData.update(t,k);
    hut.silMat.opacity=k*(0.62+0.06*Math.sin(t*0.7));       // 梦里影朦胧可读
    hut.glowMat.opacity=k*(0.24+0.05*Math.sin(t*0.8));      // 暖光呼吸
    hut.poolMat.opacity=k*(0.10+0.03*Math.sin(t*0.8));
    hut.light.intensity=k*(1.05+0.08*Math.sin(t*0.8));
  }};
}

function bMingyue(){ // 三（标志性瞬间·末境可点击）· 明月松冈 —— 相顾无言泪千行；点击：梳妆影凝现+明月照短松冈
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0};
  const grd=makeGround({r:150,c1:0x070a10,c2:0x0e1420});
  grd.mesh.position.y=-0.15; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:75178,color:0x070a10,atmo:0x1e2636,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-122); g.add(ridge.g);
  /* 小轩窗仍在（梦将醒）：窗内影散作微茫，点击后凝现 */
  const hut=makeXuanchuang();
  hut.g.position.set(-10.8,0,-15.5); hut.g.rotation.y=0.5; hut.g.scale.setScalar(1.3); g.add(hut.g);
  /* 相顾无言：词人望窗而立 */
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x586680,skin:0xd0bda6,collar:0xaab8cf,
    hair:0x535b6e,hat:'发髻',beard:true,rimC:0xb8c4dd,rim:0.55,noProp:true,scale:1.9});
  fig.position.set(-2.5,0,-11.5); fig.rotation.y=-2.14; g.add(fig);
  /* 短松冈：明月之下的孤坟矮松 */
  const gang=makeSongGang({pines:4,seed:75191});
  gang.g.position.set(17,0,-44); gang.g.scale.setScalar(1.6); g.add(gang.g);
  const gangLight=new THREE.PointLight(0xaebfe0,0.75,46); gangLight.position.set(17,10,-40); g.add(gangLight);
  /* 明月光柱（点击后自月垂照短松冈）+ 冈上清辉 */
  const beamMat=new THREE.MeshBasicMaterial({color:0xaebfe0,transparent:true,opacity:0.13,
    depthWrite:false,side:THREE.DoubleSide,blending:THREE.AdditiveBlending,fog:false});
  const beam=new THREE.Mesh(new THREE.PlaneGeometry(7,64),beamMat);
  beam.position.set(23,32,-58); beam.rotation.set(0,-0.15,0.30); beam.renderOrder=2; g.add(beam);
  const graveGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaebfe0,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  graveGlow.scale.set(10,10,1); graveGlow.position.set(17,4,-44); graveGlow.renderOrder=3; g.add(graveGlow);
  /* 泪千行：无声的泪光细痕 */
  const lei=makeLei({n:90,box:[26,12,14],pos:[-7,6,-13],speed:0.9,size:2.2,maxA:0.20});
  g.add(lei.points);
  const flow=makeFlow({n:80,box:[90,10,30],pos:[10,6,-34],color:0x9fb0c8,size:20,speed:1.0,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:5,spread:[200,18,100],pos:[0,9,-48],scale:72,color:0x8fa0ba,op:0.06});
  g.add(mist.g);
  const motes=makeGlow({n:46,box:[140,20,80],pos:[0,9,-26],color:0xa8b8d0,size:5.5,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const fgTree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:75192,sway:1.2,rim:0.16});
  fgTree.g.position.set(-16,-0.6,13); g.add(fgTree.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:75193,rim:0.14});
  fgRock.g.position.set(15,-1.6,13); g.add(fgRock.g);
  addLights(g,{c:0x9fb0cc,i:0.48,p:[36,90,-30]},{c:0x1a2232,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const el=ctl.clicked?ctl.t-ctl.clickT:0;
      const e=ease(clamp(el/2.8,0,1));
      ridge.update(t,0); mist.update(t,k); flow.update(t); lei.update(t); motes.update(t);
      fgTree.update(t,k); fgRock.update(t,k);
      fig.userData.update(t,k);
      hut.silMat.opacity=k*(0.10+0.85*e);                     // 梳妆影凝现
      hut.glowMat.opacity=k*(0.24+0.05*Math.sin(t*0.8)+0.11*e);
      hut.poolMat.opacity=k*(0.09+0.03*Math.sin(t*0.8)+0.03*e);
      hut.light.intensity=k*(1.05+0.08*Math.sin(t*0.8)+0.30*e);
      beamMat.opacity=k*(0.13*e);                             // 明月照短松冈
      graveGlow.material.opacity=k*(0.20*e);
      gangLight.intensity=k*(0.35+0.40*e);
    },onEnter(){
      pluck(0,0.3,0.07); pluck(2,0.9,0.05);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(4,0.05,0.10); pluck(2,0.5,0.08); pluck(0,0.95,0.07);
        const fl=$('#flash'); fl.textContent='明月照短松冈'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111825),fd:0.0055,star:0.30,
  moon:new THREE.Vector3(40,112,-180),ms:1.6,mph:0.04,mhaze:0.03,dirC:C(0x8fa4c4),dirI:0.45,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x19202e),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,56],t:[0,8.5,50],lf:[0,9,-46],lt:[2,9,-52]},
  sky:()=>SK({top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x10161f),fd:0.0050,star:0.32,
    ms:1.5,mph:0.03,mhaze:0.05,moon:new THREE.Vector3(-26,100,-186),
    dirC:C(0x8fa4c4),dirI:0.42,ambC:C(0x182031),ambI:0.62}) },
{ name:'生死茫茫',dwell:16,river:0.04,build:bShengsi,
  cam:{f:[0,4.8,18],t:[0.6,4.6,15.5],lf:[-4,5,-40],lt:[-3,4.6,-44]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x161e2c),bot:C(0x090c12),fog:C(0x121926),fd:0.0060,star:0.22,
    ms:1.55,mph:0.05,mhaze:0.06,moon:new THREE.Vector3(-38,104,-182),
    dirC:C(0x8fa4c4),dirI:0.44,ambC:C(0x19202e),ambI:0.6}) },
{ name:'幽梦还乡',dwell:18,river:0.02,build:bHuanxiang,
  cam:{f:[-1,4.4,17],t:[-0.4,4.2,14.5],lf:[3.5,4.2,-17],lt:[4.2,4.0,-18.5]},
  sky:()=>SK({top:C(0x090c14),hor:C(0x171f2d),bot:C(0x090c11),fog:C(0x121826),fd:0.0058,star:0.16,
    ms:1.6,mph:0.06,mhaze:0.06,moon:new THREE.Vector3(18,96,-180),
    dirC:C(0x8fa4c4),dirI:0.42,ambC:C(0x1a2230),ambI:0.58}) },
{ name:'明月松冈',dwell:20,river:0.03,build:bMingyue,
  cam:{f:[0,5.4,20],t:[0.6,5.0,17],lf:[-3,4.8,-20],lt:[-2,4.6,-24]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x171f2e),bot:C(0x090c12),fog:C(0x111825),fd:0.0055,star:0.30,
    ms:2.2,mph:0.08,mhaze:0.04,moon:new THREE.Vector3(52,110,-188),
    dirC:C(0x9fb0cc),dirI:0.48,ambC:C(0x1a2232),ambI:0.6}) },
];
"""
