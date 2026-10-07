# -*- coding: utf-8 -*-
"""xianyang-chenglou.py —— 《咸阳城东楼》（唐·许浑，queue no.227，水墨夜思）生成配置
四境（N=queue stages 数）：高城汀洲（一上高城万里愁·蒹葭杨柳似汀洲——登楼起愁、水国似乡）、
溪云风楼（溪云初起日沉阁·山雨欲来风满楼——标志性瞬间）、秦苑汉宫（鸟下绿芜秦苑夕·蝉鸣黄叶
汉宫秋——兴亡荒芜）、渭水东流（行人莫问当年事·故国东来渭水流——末境点击）。
水墨夜思全套色板：底色 #0d1117、雾 #121a26 系、文字 #dfe6f0，accent=#93a8c4（queue 分配强调色，
雨前青灰）只落在残日晕/云缘光/城楼边缘光/渭水天光/UI 上，全页近零饱和。
本诗是雨前黄昏时相：水墨夜思的冷银里放一轮被云啃去的残日（无月，ms 0.001 移出视野；残日自建
makeCanri，fog:false、云带掩腰），溪云自水面向城头推进，风线横穿楼身、旗幡始动——山雨未至，
风先满楼。
标志性瞬间（境贰·全诗名联）：山雨欲来风满楼——溪云初起横推、残日半沉阁后、风线穿楼、旗幡
乱卷初动，满画面都是雨前的压迫感（却一滴雨未落——「欲来」二字就是画面本身）。
末境点击（queue interact：点击风满楼——风起云涌+雨点初落+旗幡乱卷）：点击画面——云阵涌动
加速压城、雨点初落渐密（自写斜雨着色器，点击前 visible=false 硬关）、楼头旗幡乱卷、风声骤起；
「溪云初起日沉阁 山雨欲来风满楼」题字同现，而渭水依旧东流——危机预感与家国愁思在风雨与流水
的对切里合拢。
考点钉子：芜 wú / 汀 tīng / 蒹葭 jiān jiā（小测第 3 题落点）；许浑「许千首湿」+ 咸阳秦都故地
（第 4 题）；「山雨欲来风满楼」名句的危机预感与家国愁思（第 5 题）。
多音字：蒹葭/汀/芜/当年 钉同音替换（tts.json）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='xianyang-chenglou', title='咸阳城东楼', dyn='唐 · 许浑', brand_author='许 浑',
    gold_rgb='147,168,196',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#93a8c4; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(147,168,196,.26);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0d1117', 2),
        ('rgba(5,8,15', 'rgba(9,14,22', 1),
        ('rgba(4,6,11', 'rgba(8,12,19', 2),
        ('rgba(6,9,16', 'rgba(10,15,23', 1),
        ('rgba(3,5,9', 'rgba(6,9,15', 1),
        ('#0b101c', '#121a28', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
        ('0x0a1526', '0x121a26', 4),
    ],
    tip='轻点画面 / 按空格 —— 风起云涌，山雨欲来',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看风起云涌、雨点初落，旗幡乱卷',
    cover_read='咸阳城东楼。唐，许浑。一上高城万里愁，蒹葭杨柳似汀洲。溪云初起日沉阁，山雨欲来风满楼。鸟下绿芜秦苑夕，蝉鸣黄叶汉宫秋。行人莫问当年事，故国东来渭水流。',
    cover_p1='四重意境，随诗句次第展开：一登高城、万里愁生的乡关之思；溪云初起、日沉阁后、山雨欲来风满楼的危城暮色；鸟下绿芜、蝉鸣黄叶的秦苑汉宫秋色；末了行人莫问当年事，唯见故国渭水东流。',
    cover_p2='边读诗，边跟着许浑登上咸阳城东楼：一个「愁」字领起全篇——乡愁之上，更有对大唐国势的深忧；读懂「山雨欲来风满楼」里那份山雨未至、风已满楼的危机预感，就读懂了这首晚唐登临名作。',
    end_h2='山雨 · 渭水', cn_word='四',
    words_js="['再登一次咸阳城楼','初识许浑，尚需共读','渐入诗境，再诵几遍','云起风满，雨意渐紧','已解山雨欲来之意','莫问当年，渭水长流']",
    sky_atmo='0x1f2937',
)

POEM_JS = """const POEM = [
{ name:'高城汀洲', jing:'秋日傍晚，登上高高的咸阳城楼，万里乡愁陡然而生；眼前蒹葭苍苍、杨柳依依，沙洲罗列，仿佛江南水乡的汀洲 —— 高城一上，愁生万里。（高城 · 蒹葭 · 杨柳 · 汀洲）',
  segs:[
   {c:'一上高城万里愁，', p:py('yī shàng gāo chéng wàn lǐ chóu')},
   {c:'蒹葭杨柳似汀洲。', p:py('jiān jiā yáng liǔ sì tīng zhōu')}],
  read:'一上高城万里愁，蒹葭杨柳似汀洲。',
  yisi:'一登上高高的咸阳城楼，万里愁思便涌上心头；眼前水中蒹葭苍苍、岸上杨柳依依，沙洲罗列，好像江南水乡的汀洲。——起句「一上」与「万里」劈面对起：楼才登、脚未稳，愁已万里——这个「愁」字是全诗之纲，乡愁、怀古之忧、忧时之愁都从这里生发。次句以「似」字轻轻荡开：咸阳渭水边的风物像极了记忆里的江南水乡——诗人是润州丹阳（今江苏镇江）人，一眼蒹葭杨柳，看得见的是汀洲，放不下的是故乡。',
  zhu:[['咸阳','秦汉故都，今陕西咸阳，在长安西北、渭水北岸——城东楼即咸阳城东门城楼'],['一上高城','刚刚登上高城。一，甫一、才——与「万里」对举，登楼之顷愁即万里'],['蒹葭','芦苇一类的荻苇，苍苍水草。蒹葭，读 jiān jiā'],['汀洲','水边（或水中）的平地与小洲。汀，读 tīng'],['似汀洲','咸阳渭水风物像极了江南水乡——许浑是润州丹阳（今江苏镇江）人，见景思乡，故「万里愁」']] },
{ name:'溪云风楼', jing:'磻溪上空暮云刚刚升起，夕阳已沉落在慈福寺阁后；山雨即将来临，满楼已灌满了呼啸的风声 —— 山雨欲来风满楼。（溪云 · 日沉 · 风满楼）（标志性瞬间）',
  segs:[
   {c:'溪云初起日沉阁，', p:py('xī yún chū qǐ rì chén gé')},
   {c:'山雨欲来风满楼。', p:py('shān yǔ yù lái fēng mǎn lóu')}],
  read:'溪云初起日沉阁，山雨欲来风满楼。',
  yisi:'磻溪上暮云刚刚升起，夕阳已经沉落在慈福寺阁后面；山雨眼看就要来了，满楼已灌满了呼啸的风。——全诗最负盛名的一联：云「初起」、日「沉」、风「满」、雨「欲来」，一联十四字四个动词层层加码，把暴雨前一瞬的天象写得风生水起；云愈压愈低、风愈吹愈急，雨却一滴未落——压迫感全在「欲来」二字。「山雨欲来风满楼」由此成为千古传诵的名句，凡大事发生前山雨欲来的紧张气氛，人们都会想起这七个字。',
  zhu:[['溪云','磻溪上空的云。溪、阁：诗人本联下自注「南近磻溪，西对慈福寺阁」'],['日沉阁','夕阳沉落在寺阁之后'],['初起','刚刚升起——云是一点一点压上来的'],['山雨欲来风满楼','山雨将要到来，满楼已是大风——以风雨欲来的自然征兆暗喻时局：许浑身处晚唐，藩镇割据、王朝飘摇，景中含忧，「风满楼」的风声里全是危机预感']] },
{ name:'秦苑汉宫', jing:'鸟儿飞落在黄昏的绿芜深处，秋蝉在枯黄的叶间嘶鸣，诉说着秦苑汉宫的秋色 —— 帝业成空，荒烟蔓草。（绿芜 · 黄叶 · 秦苑 · 汉宫）',
  segs:[
   {c:'鸟下绿芜秦苑夕，', p:py('niǎo xià lǜ wú qín yuàn xī')},
   {c:'蝉鸣黄叶汉宫秋。', p:py('chán míng huáng yè hàn gōng qiū')}],
  read:'鸟下绿芜秦苑夕，蝉鸣黄叶汉宫秋。',
  yisi:'黄昏里，鸟儿飞落在长满绿草的荒芜废苑；秋蝉在枯黄的叶间嘶鸣——那是汉宫旧地的秋声。——「秦苑」「汉宫」实写咸阳原上秦汉遗迹：当年万国衣冠的宫苑，如今只剩绿芜任鸟栖、黄叶任蝉嘶。「夕」与「秋」把时间也推向尽头——日暮是一天之秋，秋是一年之暮，帝业消亡、繁华成空；历史之愁与首联的万里乡愁在此合流，并为结联的「莫问」蓄势。',
  zhu:[['绿芜','丛生的绿草、杂草。芜，读 wú，乱草丛生之地'],['秦苑','秦代的宫苑遗迹，在咸阳原上——当年帝都宫禁，今日鸟雀荒园'],['汉宫','汉代宫殿遗迹——与「秦苑」互文，泛指秦汉故都的宫阙废墟'],['蝉鸣黄叶','秋蝉在枯黄的叶间嘶鸣，如泣如诉——以虫鸟之微写兴亡之大'],['互文见义','「秦苑夕」「汉宫秋」互相补足：秦汉宫苑都在黄昏、都在秋里——不拆开讲，荒凉才铺满整个故都']] },
{ name:'渭水东流', jing:'行人啊，不要再问当年的旧事了；我东望故国，只见渭水不言不语、不舍昼夜地东流 —— 万事消沉，流水无恙。（行人 · 渭水 · 末境点击画面：风起云涌，雨点初落，旗幡乱卷）',
  segs:[
   {c:'行人莫问当年事，', p:py('xíng rén mò wèn dāng nián shì')},
   {c:'故国东来渭水流。', p:py('gù guó dōng lái wèi shuǐ liú')}],
  read:'行人莫问当年事，故国东来渭水流。',
  yisi:'来往的行人，不要再追问秦汉兴亡的旧事了；我自东边故乡来，登上故国城楼，只见渭水依旧不言不语地东流。——结句以「莫问」作答、以流水收束：不是无话可说，而是千头万绪无从说起——山雨欲来的时局、秦汉兴亡的怅惘、宦游万里的乡愁，都付与不舍昼夜的渭水。以景结情，语尽而意不尽。',
  zhu:[['行人','过往的旅人——也包含诗人自己'],['当年事','秦汉盛衰、前朝兴亡的旧事'],['故国','指咸阳——昔日的秦国故地、帝都旧壤'],['渭水','黄河最大支流，流经咸阳——「东来渭水流」：不言不语的流水，对人间万事做了最沉默的回答'],['以景结情','不把话说尽，用一幅流水东去的画面收束全诗——愁绪与流水俱长，余味无穷']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「一上高城万里愁」的下一句是？', o:['蒹葭杨柳似汀洲','溪云初起日沉阁','山雨欲来风满楼'], a:0},
 {q:'「溪云初起日沉阁」的下一句是？', o:['鸟下绿芜秦苑夕','山雨欲来风满楼','蒹葭杨柳似汀洲'], a:1},
 {q:'「鸟下绿芜秦苑夕」的「芜」与「蒹葭杨柳似汀洲」的「汀」，读音和意思都正确的一项是？', o:['芜读 wú，指丛生的杂草；汀读 tīng，指水边的平地、小洲','芜读 wū，指荒废的宫殿；汀读 dīng，指水边的亭子','芜读 wú，指茂密的树林；汀读 tīng，指水中的渡口'], a:0},
 {q:'关于作者许浑与咸阳，下列说法正确的是？', o:['许浑是唐代诗人，诗中多写水、雨意象，后人戏称「许浑千首湿」；咸阳是秦汉故都之地，此诗登楼所感不止乡愁，更有对国势的深忧','许浑是宋代江西诗派诗人，「许浑千首湿」说他屡试不第泪湿青衫；咸阳即今南京的古称','许浑是「初唐四杰」之一；咸阳城东楼是他的田园隐逸之作，全诗只写个人闲适之趣'], a:0},
 {q:'「溪云初起日沉阁，山雨欲来风满楼」历来传诵。对这一联妙处的理解，最准确的一项是？', o:['单纯写景：云起日落、风雨将至只是天气变化，与诗人的情感无关','用夸张手法写雨势：山上真的下起了倾盆大雨，楼中行人浑身湿透','以自然风雨喻时局危机：云起、日沉、风满、雨欲来层层压迫，既写出暴雨前的逼仄气象，也暗喻晚唐国势飘摇的危机预感——景中含忧，「欲来」二字最见分量'], a:2},
];
"""

SCENES_JS = """/* ================= 咸阳城东楼 · 四境场景（水墨夜思·雨前危城：高城汀洲、溪云风楼、秦苑汉宫、渭水东流） =================
   美术立意：水墨夜思色板写「山雨欲来的黄昏危城」——底色 #0d1117、雾 #121a26 系、
   accent=#93a8c4（雨前青灰）只落在残日晕/云缘光/城楼边缘光/渭水天光/UI 上，全页近零饱和。
   与已有水墨夜思页第一眼可区分：不做舟夜孤灯碎星（zhouye）、不做雨夜棋枰灯花（yueke）、
   不做古寺竹径（ti-poshansi）、不做渡口小楼星火（ti-jinlingdu）、不做暮雨洒江天的大雨（bashengganzhou，
   本页山雨未至，一滴雨都不落——直到末境点击）——做「城楼+垛口城墙+旗幡+溪云压城+风线穿楼」的
   登楼望乡与危机预感。
   境壹（登楼）：高城垛口为前景，凭堞望水——蒹葭、杨柳、汀洲如江南，乡愁万里。
   境贰（标志性瞬间）：溪云初起横推、残日半沉阁后、风线穿楼、旗幡始动——雨前压迫感拉满，雨未落。
   境叁（怀古）：秦苑断墙、绿芜黄叶、鸟下蝉嘶、汉宫遗阁——帝业成空。
   境肆（末境可点击）：危楼临渭水，行人凭堞；点击：云阵涌动、雨点初落渐密、旗幡乱卷、风声骤起，
   渭水依旧东流。 */

/* —— 城楼 makeChenglou(o)：城墙段+垛口+门楼（台基+双重楼身+腰檐+四阿顶，合批 1 mesh）
   ——「一上高城」「风满楼」的城与楼；水墨剪影+青灰边缘光，与 ti-jinlingdu 小山楼、bashengganzhou
   江楼的临水民居/歌楼剪影完全不同形：这是有垛口城墙的城防楼 */
function makeChenglou(o){
  o=o||{};
  const w=o.w===undefined?4.4:o.w, wl=o.wallLen===undefined?18:o.wallLen;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(wl,3.2,5);
  wall.translate(0,1.6,0); B.put(wall,0x1a212e);
  const wallTop=new THREE.BoxGeometry(wl,0.22,5.3);
  wallTop.translate(0,3.3,0); B.put(wallTop,0x232d3b);
  for(let s=-1;s<=1;s+=2){
    for(let i=0;i<Math.floor(wl/1.5);i++){
      const cx=-wl/2+0.9+i*1.5;
      const cr=new THREE.BoxGeometry(0.62,0.72,0.5);
      cr.translate(cx,3.76,s*2.4); B.put(cr,0x202a38);
    }
  }
  const base=new THREE.BoxGeometry(w*1.5,0.7,w*1.15);
  base.translate(0,3.85,0); B.put(base,0x252f3e);
  const body1=new THREE.BoxGeometry(w,2.6,w*0.72);
  body1.translate(0,5.5,0); B.put(body1,0x1c2532);
  for(let i=0;i<5;i++){
    const px=-w*0.4+i*w*0.2;
    const col=new THREE.BoxGeometry(0.16,2.3,0.16);
    col.translate(px,5.5,w*0.38); B.put(col,0x27323f);
  }
  const deck=new THREE.BoxGeometry(w*1.26,0.2,w*0.96);
  deck.translate(0,6.9,0); B.put(deck,0x2b3749);
  const body2=new THREE.BoxGeometry(w*0.72,2.1,w*0.55);
  body2.translate(0,8.05,0); B.put(body2,0x1e2836);
  const roof=new THREE.ConeGeometry(w*0.88,1.6,4);
  roof.rotateY(Math.PI/4); roof.scale(1.16,1,0.8); roof.translate(0,9.9,0); B.put(roof,0x141c28);
  const finial=new THREE.SphereGeometry(0.2,6,5);
  finial.translate(0,10.8,0); B.put(finial,0x3a4759);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x93a8c4,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 旗幡 makeQifan(o)：城头旗杆两根（杆+石座+杆顶，合批 1 mesh）+ 幡两面（自写 ShaderMaterial：
   顶点 sin 波浪，uSway 控制摆幅——初动 0.5 → 点击乱卷 3.5）；uFade 每帧写=fadeK */
const XY_FLAG_VERT=`
uniform float uTime; uniform float uSway;
varying vec2 vUv;
void main(){
  vUv=uv;
  vec3 p=position;
  float w1=sin(uv.x*7.0-uTime*6.2)*0.5+sin(uv.x*13.0-uTime*9.3)*0.5;
  p.z+=w1*uSway*uv.x*uv.x*0.5;
  p.y+=sin(uv.x*5.0-uTime*4.1)*uSway*uv.x*0.08;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const XY_FLAG_FRAG=`
uniform float uTime; uniform float uFade; uniform vec3 uColor;
varying vec2 vUv;
void main(){
  float edge=smoothstep(0.0,0.07,vUv.y)*smoothstep(1.0,0.93,vUv.y);
  float fly=0.4+0.6*smoothstep(0.0,0.5,vUv.x);
  float shade=0.82+0.18*sin(vUv.x*3.0);
  vec3 c=mix(uColor*1.25,uColor*0.72,vUv.x);
  gl_FragColor=vec4(c,uFade*0.8*edge*fly*shade);
}`;
function makeQifan(o){
  o=o||{};
  const h=o.h===undefined?3.6:o.h;
  const xs=o.xs===undefined?[[-10.5,0],[11,0]]:o.xs;
  const fl=o.flagC===undefined?0x4a5870:o.flagC;
  const B=new GeoBag();
  xs.forEach(function(p){
    const st=new THREE.CylinderGeometry(0.075,0.1,h,6);
    st.translate(p[0],h*0.5,p[1]); B.put(st,0x2a3342);
    const cap=new THREE.SphereGeometry(0.1,6,5);
    cap.translate(p[0],h+0.08,p[1]); B.put(cap,0x3a4759);
    const bk=new THREE.BoxGeometry(0.5,0.3,0.5);
    bk.translate(p[0],0.15,p[1]); B.put(bk,0x161e2a);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x93a8c4,i:0.14,p:2.4})));
  const mats=[], meshes=[];
  xs.forEach(function(p,i){
    const geo=new THREE.PlaneGeometry(1.8,0.9,10,5);
    geo.translate(0.93,0,0);
    const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
      uniforms:{uTime:{value:i*1.9},uSway:{value:0.5},uFade:{value:1},
        uColor:{value:C(fl)}}});
    m.vertexShader=XY_FLAG_VERT; m.fragmentShader=XY_FLAG_FRAG;
    const mesh=new THREE.Mesh(geo,m);
    mesh.position.set(p[0]+0.06,h*0.86,p[1]);
    mesh.rotation.y=i===0?0.26:-0.22;
    mesh.renderOrder=4; mesh.frustumCulled=false;
    g.add(mesh); mats.push(m); meshes.push(mesh);
  });
  g.update=function(t,k,sway){
    const kk=k===undefined?1:k, sw=sway===undefined?0.5:sway;
    for(let i=0;i<mats.length;i++){
      mats[i].uniforms.uTime.value=t+i*1.9;
      mats[i].uniforms.uFade.value=kk;
      mats[i].uniforms.uSway.value=sw*(0.9+0.2*Math.sin(t*0.7+i*2.6));
    }
  };
  g.userData.update=g.update;
  return g;
}

/* —— 蒹葭 makeJianjia(o)：水边荻苇丛（细竿+穗头+斜叶，合批 1 mesh，整丛微摆）——「蒹葭杨柳」 */
function makeJianjia(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22701:o.seed);
  const n=o.n===undefined?14:o.n, w=o.w===undefined?9:o.w, d=o.d===undefined?2.4:o.d;
  const h0=o.h===undefined?3.1:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, h=h0*(0.6+0.75*R()), tilt=(R()-0.5)*0.16;
    const st=new THREE.CylinderGeometry(0.028,0.05,h,5);
    st.translate(x+tilt*h*0.4,h*0.5,z); B.put(st,shadeColor(0x2a333f,0.8+0.4*R()));
    const sd=new THREE.CylinderGeometry(0.02,0.085,0.66,5);
    sd.rotateZ(tilt*2.4+0.14); sd.translate(x+tilt*h+0.1,h+0.24,z); B.put(sd,shadeColor(0x49535f,0.85+0.4*R()));
    const lf=new THREE.PlaneGeometry(0.9+R()*0.5,0.12);
    lf.rotateY(R()*3.14); lf.rotateZ(-0.5-R()*0.4);
    lf.translate(x+(R()-0.5)*0.6,h*(0.5+R()*0.3),z+(R()-0.5)*0.4);
    B.put(lf,shadeColor(0x303b41,0.7+0.4*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36445a,emissive:0x04070a,side:THREE.DoubleSide}),{c:0x93a8c4,i:0.12,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.014*Math.sin(t*0.75+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 杨柳 makeYangliu(o)：水边垂柳（斜干+横枝+垂丝+疏叶，合批 1 mesh，整树微摆）——「杨柳」 */
function makeYangliu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22711:o.seed);
  const h0=o.h===undefined?4.6:o.h;
  const B=new GeoBag();
  const tr=new THREE.CylinderGeometry(0.14,0.26,h0,6);
  tr.rotateZ(0.08); tr.translate(0,h0*0.5,0); B.put(tr,shadeColor(0x242d38,0.9+0.25*R()));
  for(let b=0;b<4;b++){
    const a=R()*6.283, ly=h0*(0.62+0.3*R()), len=1.6+R()*1.8;
    const bx=Math.cos(a)*len, bz=Math.sin(a)*len*0.5;
    B.put(limbGeo([0,ly,0],[bx,ly+0.5,bz],0.09,0.04,5),shadeColor(0x28323e,0.9+0.25*R()));
    for(let s=0;s<3;s++){
      const tx=bx*(0.55+0.35*s/2), tz=bz*(0.55+0.35*s/2), ty=ly+0.4-s*0.55;
      const dr=limbGeo([tx,ty,tz],[tx+(R()-0.5)*0.4,ty-1.5-R()*1.1,tz+(R()-0.5)*0.4],0.035,0.015,4);
      B.put(dr,shadeColor(0x2c3644,0.85+0.3*R()));
      const lf=new THREE.PlaneGeometry(0.52,0.13);
      lf.rotateY(R()*3.14); lf.rotateZ(-0.3-R()*0.3);
      lf.translate(tx+(R()-0.5)*0.5,ty-0.7-R()*0.8,tz+(R()-0.5)*0.4);
      B.put(lf,shadeColor(0x3d4a42,0.7+0.45*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36485a,emissive:0x04070a,side:THREE.DoubleSide}),{c:0x93a8c4,i:0.11,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.006*Math.sin(t*0.55+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 汀洲 makeTingzhou(o)：水中沙洲（伏水低洲+苇荻数茎，合批 1 mesh）——「似汀洲」 */
function makeTingzhou(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22721:o.seed);
  const r=o.r===undefined?6.5:o.r;
  const B=new GeoBag();
  const mound=new THREE.SphereGeometry(r,10,7);
  mound.scale(1,0.16,0.55); mound.translate(0,0.1,0); B.put(mound,0x101823);
  const mound2=new THREE.SphereGeometry(r*0.55,9,6);
  mound2.scale(1,0.2,0.6); mound2.translate(r*0.4,0.16,-r*0.12); B.put(mound2,shadeColor(0x101823,1.25));
  for(let i=0;i<9;i++){
    const x=(R()-0.5)*r*1.5, z=(R()-0.5)*r*0.7, h=1.5+R()*1.6;
    const st=new THREE.CylinderGeometry(0.02,0.04,h,4);
    st.translate(x,h*0.5+0.3,z); B.put(st,shadeColor(0x2a333f,0.85+0.35*R()));
    const sd=new THREE.CylinderGeometry(0.015,0.07,0.5,4);
    sd.rotateZ(0.12); sd.translate(x+0.07,h+0.42,z); B.put(sd,shadeColor(0x49535f,0.9+0.3*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x303c50,emissive:0x04070b}),{c:0x93a8c4,i:0.13,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 残日 makeCanri(o)：被云啃去的雨前残日（limbTex 日轮+青灰晕+掩腰云带；均 fog:false
   如星月点名；fadeK 铁律：初值=最大）——「溪云初起日沉阁」的「日」 */
function makeCanri(o){
  o=o||{};
  const r=o.r===undefined?7.5:o.r, op=o.op===undefined?0.3:o.op, haze=o.haze===undefined?0.12:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xcfc4ae:o.color,
    transparent:true,opacity:op,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const hz=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0x93a8c4:o.hazeC,
    transparent:true,opacity:haze,depthWrite:false,fog:false}));
  hz.scale.set(r*6.2,r*6.2,1); g.add(hz);
  const veil=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.veilC===undefined?0x333e52:o.veilC,
    transparent:true,opacity:0.4,depthWrite:false,fog:false}));
  veil.scale.set(r*4.6,r*1.5,1); veil.position.set(r*0.4,-r*0.42,0.5); g.add(veil);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    disc.material.opacity=kk*op*(0.94+0.06*Math.sin(t*0.35));
    hz.material.opacity=kk*haze*(0.8+0.2*Math.sin(t*0.23+1.1));
    veil.material.opacity=kk*0.4*(0.85+0.15*Math.sin(t*0.3+2.2));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 溪云 makeXiyun(o)：自水面横推向城头的云阵（Sprite 横带漂移+回绕；surge 0→1 时涌动加速
   增浓——末境点击「风起云涌」）；fadeK 铁律：初值=最大 */
function makeXiyun(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22731:o.seed);
  const n=o.n===undefined?9:o.n;
  const box=o.box===undefined?[150,9,22]:o.box;
  const pos=o.pos===undefined?[0,13,-52]:o.pos;
  const scale=o.scale===undefined?46:o.scale;
  const color=o.color===undefined?0x27303f:o.color;
  const g=new THREE.Group(), items=[];
  const L=pos[0]-box[0]*0.5-30, span=box[0]+60;
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:color,transparent:true,
      opacity:0.30*(0.5+0.6*R()),depthWrite:false});
    const s=new THREE.Sprite(m);
    const x0=L+R()*span, y0=pos[1]+(R()-0.5)*box[1], z0=pos[2]+(R()-0.5)*box[2];
    s.position.set(x0,y0,z0);
    const sc=scale*(0.55+0.8*R());
    s.scale.set(sc,sc*0.4,1); s.renderOrder=5;
    g.add(s); items.push({m:m,s:s,x0:x0,y0:y0,spd:1.0+1.4*R(),op:m.opacity,ph:R()*6.283});
  }
  g.update=function(t,k,surge){
    const kk=k===undefined?1:k, sg=surge===undefined?0:surge, sp=1+2.4*sg;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      let x=it.x0+t*it.spd*sp;
      x=L+((x-L)%span+span)%span;
      it.s.position.x=x;
      it.m.opacity=kk*it.op*(0.44+0.56*sg)*(0.72+0.28*Math.sin(t*0.24+it.ph));
    }
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 寺阁 makeGe(o)：远处慈福寺阁剪影（台基+四柱+攒尖顶，合批 1 mesh）——「日沉阁」的阁 */
function makeGe(o){
  o=o||{};
  const w=o.w===undefined?3.2:o.w;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w*1.5,0.5,w*1.1);
  base.translate(0,0.25,0); B.put(base,0x1c2532);
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const col=new THREE.CylinderGeometry(0.09,0.11,1.9,5);
    col.translate(sx*w*0.55,1.45,sz*w*0.42); B.put(col,0x232d3b);
  }
  const body=new THREE.BoxGeometry(w,1.3,w*0.72);
  body.translate(0,1.6,0); B.put(body,0x1a2330);
  const roof=new THREE.ConeGeometry(w*0.98,1.15,4);
  roof.rotateY(Math.PI/4); roof.scale(1.15,1,0.82); roof.translate(0,2.85,0); B.put(roof,0x121926);
  const finial=new THREE.SphereGeometry(0.11,6,5);
  finial.translate(0,3.5,0); B.put(finial,0x36445a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x93a8c4,i:o.rim===undefined?0.15:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 鸟下 makeNiaoxia(o)：飞鸟徐徐下落归芜（简笔鸟 InstancedMesh 1 draw call，错峰盘旋下坠）
   ——「鸟下绿芜」 */
function makeNiaoxia(o){
  o=o||{};
  const n=o.n===undefined?6:o.n;
  const geo=new THREE.BufferGeometry();
  const v=new Float32Array([
    0,0,0.78,  -0.23,0.04,-0.48,  0.23,0.04,-0.48,
    0,0.04,0.07,  -1.5,0.17,-0.58,  -0.21,0.04,-0.52,
    0,0.04,0.07,   0.21,0.04,-0.52,  1.5,0.17,-0.58
  ]);
  geo.setAttribute('position',new THREE.BufferAttribute(v,3));
  geo.computeVertexNormals();
  const mesh=new THREE.InstancedMesh(geo,
    new THREE.MeshBasicMaterial({color:o.color===undefined?0x27313e:o.color,side:THREE.DoubleSide}),n);
  mesh.frustumCulled=false;
  const dm=new THREE.Object3D(), items=[];
  const R=seedRnd(o.seed===undefined?22741:o.seed);
  const cx=o.cx===undefined?0:o.cx, cy=o.cy===undefined?9:o.cy, cz=o.cz===undefined?-30:o.cz;
  const rad=o.rad===undefined?10:o.rad, drop=o.drop===undefined?6.5:o.drop;
  for(let i=0;i<n;i++)items.push({a:R()*6.283,ph:R()*6.283,off:R()*13.0,s:0.55+0.4*R(),fl:5.5+R()*3.5});
  const g=new THREE.Group(); g.add(mesh);
  g.update=function(t){
    for(let i=0;i<n;i++){
      const it=items[i], cyc=(t/13+it.off/13)%1;
      const a=it.a+t*0.32+cyc*2.4, r=rad*(1-0.55*cyc);
      const y=cy+drop*(1-cyc)+Math.sin(t*0.5+it.ph)*0.5;
      const flap=Math.sin(t*it.fl+it.ph)*0.55;
      dm.position.set(cx+Math.cos(a)*r, y, cz+Math.sin(a)*r*0.6);
      dm.rotation.set(flap*0.35, -a+(Math.cos(a)>0?0:Math.PI), flap);
      dm.scale.setScalar(it.s*(1-0.35*cyc));
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 绿芜 makeLvwu(o)：荒苑芜草（伏地草墩+草叶斜出，合批 1 mesh）——「鸟下绿芜」 */
function makeLvwu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22751:o.seed);
  const n=o.n===undefined?5:o.n, w=o.w===undefined?16:o.w, d=o.d===undefined?8:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, r=1.1+R()*1.3;
    const mound=new THREE.SphereGeometry(r,8,6);
    mound.scale(1,0.34,0.8); mound.translate(x,r*0.16,z);
    B.put(mound,shadeColor(0x18211c,0.8+0.45*R()));
  }
  for(let i=0;i<26;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d;
    const bl=new THREE.PlaneGeometry(0.09,0.7+R()*0.5);
    bl.rotateY(R()*3.14); bl.rotateZ((R()-0.5)*0.7);
    bl.translate(x,0.45+R()*0.3,z);
    B.put(bl,shadeColor(0x222f26,0.7+0.5*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36485a,emissive:0x04070a,side:THREE.DoubleSide}),{c:0x93a8c4,i:0.12,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 黄叶树 makeHuangyeshu(o)：秋深疏叶树（斜干+枯枝+稀疏黄叶，合批 1 mesh）——「蝉鸣黄叶」 */
function makeHuangyeshu(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22761:o.seed);
  const h0=o.h===undefined?3.6:o.h;
  const B=new GeoBag();
  const tr=new THREE.CylinderGeometry(0.1,0.2,h0,5);
  tr.rotateZ(0.1); tr.translate(0,h0*0.5,0); B.put(tr,shadeColor(0x20282f,0.9+0.3*R()));
  for(let b=0;b<3;b++){
    const a=R()*6.283, ly=h0*(0.5+0.34*R()), len=1.1+R()*1.3;
    const bx=Math.cos(a)*len, bz=Math.sin(a)*len*0.5;
    B.put(limbGeo([0,ly,0],[bx,ly+0.5,bz],0.06,0.025,4),shadeColor(0x242c34,0.9+0.3*R()));
    for(let l=0;l<4;l++){
      const lf=new THREE.PlaneGeometry(0.5+R()*0.25,0.2);
      lf.rotateY(R()*3.14); lf.rotateZ(-0.35-R()*0.4);
      lf.translate(bx*(0.4+0.6*R())+(R()-0.5)*0.6,ly+0.3+R()*0.7,bz*(0.4+0.6*R())+(R()-0.5)*0.5);
      B.put(lf,shadeColor(0x6b6446,0.7+0.5*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x36485a,emissive:0x04070a,side:THREE.DoubleSide}),{c:0x93a8c4,i:0.12,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.008*Math.sin(t*0.6+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 秦苑断墙 makeGongqiang(o)：荒废宫苑（夯土台基+断墙残段+柱础残柱，合批 1 mesh）
   ——「秦苑」「汉宫」的废墟剪影：与 makeChenglou 的完整城防楼完全不同形 */
function makeGongqiang(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22771:o.seed);
  const w=o.w===undefined?16:o.w;
  const B=new GeoBag();
  const ter=new THREE.BoxGeometry(w,1.2,w*0.6);
  ter.translate(0,0.6,0); B.put(ter,0x1a2230);
  const segs=[[0.5,2.6,1.1],[-0.28,1.6,0.8],[0.24,3.2,1.5],[-0.16,2.0,0.9]];
  let cx0=-w*0.36;
  for(let i=0;i<segs.length;i++){
    const bw=w*segs[i][0]*0.5, bh=segs[i][1], bd=segs[i][2];
    const seg=new THREE.BoxGeometry(bw,bh,bd);
    seg.translate(cx0+bw*0.5,1.2+bh*0.5,0); B.put(seg,shadeColor(0x202a38,0.8+0.4*R()));
    for(let r2=0;r2<3;r2++){
      const rb=new THREE.BoxGeometry(0.3+R()*0.3,0.2+R()*0.24,0.3);
      rb.translate(cx0+bw*(0.2+0.6*R()),1.2+bh+0.12,cx0*0.01+(R()-0.5)*bd*0.7);
      B.put(rb,shadeColor(0x242e3c,0.75+0.4*R()));
    }
    cx0+=bw+0.3+R()*0.8;
  }
  for(let i=0;i<3;i++){
    const x=-w*0.3+R()*w*0.6;
    const stump=new THREE.CylinderGeometry(0.3,0.38,0.8+R()*1.0,7);
    stump.translate(x,1.6+R()*0.4,(R()-0.5)*w*0.4);
    B.put(stump,shadeColor(0x1c2532,0.8+0.35*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x303c50,emissive:0x04060a}),{c:0x93a8c4,i:o.rim===undefined?0.14:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 雨点 makeYudian(o)：山雨初落的斜雨（自写 Points 着色器：快落+微摆+距离衰减；
   uOn 0→1 控制雨势渐密——点击前 alpha=0 且 visible=false 硬关，无幻影）——末境点击「雨点初落」 */
const XY_RAIN_VERT=`
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
attribute float aSeed; attribute float aSize;
varying float vA;
void main(){
  vec3 p=position;
  float fall=mod(p.y-uTime*uSpeed*(0.75+0.5*aSeed),uBox.y);
  p.y=fall;
  p.x+=sin(uTime*2.1+aSeed*43.0)*0.5;
  vA=0.5+0.5*aSeed;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(240.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const XY_RAIN_FRAG=`
uniform float uFade; uniform float uOn; uniform float uMaxA; uniform vec3 uColor;
varying float vA;
void main(){
  vec2 d=gl_PointCoord-vec2(0.5);
  float m=smoothstep(0.5,0.1,length(d));
  gl_FragColor=vec4(uColor,uFade*uOn*uMaxA*m*vA);
}`;
function makeYudian(o){
  o=o||{};
  const n=o.n===undefined?420:o.n;
  const box=o.box===undefined?[120,26,66]:o.box;
  const pos=o.pos===undefined?[0,0,-30]:o.pos;
  const g=new THREE.Group();
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  const R=seedRnd(o.seed===undefined?22781:o.seed);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(R()-0.5)*box[0];
    P[i*3+1]=R()*box[1];
    P[i*3+2]=pos[2]+(R()-0.5)*box[2];
    S[i]=R(); Z[i]=1.0+1.3*R();
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?11:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0x9fb2c8:o.color)},uFade:{value:1},
      uOn:{value:0},uMaxA:{value:o.maxA===undefined?0.34:o.maxA}}});
  m.vertexShader=XY_RAIN_VERT; m.fragmentShader=XY_RAIN_FRAG;
  const points=new THREE.Points(geo,m);
  points.frustumCulled=false; points.renderOrder=4; points.visible=false;
  g.add(points);
  g.update=function(t,k,on){
    m.uniforms.uTime.value=t;
    m.uniforms.uFade.value=k===undefined?1:k;
    m.uniforms.uOn.value=on===undefined?0:on;
    points.visible=(k===undefined?1:k)*(on===undefined?0:on)>0.004;
  };
  g.userData.update=g.update;
  g.rotation.z=0.07;
  return {g:g,update:g.update,points:points,mat:m};
}

/* 登楼人/凭堞人：全诗贯穿的同一造型（青灰袍、幞头；每次 build 新建材质） */
function xyFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2b3546,belt:0x74879c,skin:0xd3b294,collar:0x9aa8ba,
    hair:0x12161e,hat:'幞头',rimC:0x93a8c4,rim:0.45,noProp:true,scale:scale===undefined?1.8:scale});
}

/* 远岸横陈 makeYuan(o)：渭水对岸的低平远岸（低多峰脊，两层，带雾骨相） */
function makeYuan(o){
  o=o||{};
  return makeRange({r:o.r===undefined?210:o.r,h:o.h===undefined?8:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?22791:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x1f2937,
    fogK:o.fogK===undefined?0.58:o.fogK,glowK:0.05,glow:0xc8d2dc,
    y:o.y===undefined?-11:o.y,order:-6});
}

function bCover(){ // 卷首 · 雨前危城远望：城楼垛口剪影、溪云压城、残日半沉、蒹葭拂水
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:90,amp:0.16,freq:0.13,speed:0.4,flow:[0.3,0.06],spec:0.6,
    deep:0x05080e,shallow:0x0b1420,skyc:0x111a27,moonDir:[-0.24,0.1,-0.95]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x9fb0c4);
  water.mesh.position.set(0,-0.52,-130); g.add(water.mesh);
  const grd=makeGround({r:80,c1:0x0a0f18,c2:0x151d2b,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,62);
  const yuan=makeYuan({r:240,h:9,seed:22792}); yuan.g.position.set(-6,0,-158); g.add(yuan.g);
  const ridge=makeRange({r:300,h:18,layers:2,peaks:5,seed:22793,color:0x0d1320,atmo:0x1f2937,
    fogK:0.62,glowK:0.06,glow:0xc8d2dc,y:-10,order:-6});
  ridge.g.position.set(-34,0,-108); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 咸阳城东楼：城墙+垛口+门楼剪影 */
  const lou=makeChenglou({scale:1.35,rim:0.2,seed:22794}); lou.position.set(11,-0.28,-56);
  lou.rotation.y=-0.32; g.add(lou);
  /* 残日半沉 + 寺阁剪影 */
  const ri=makeCanri({r:8,op:0.3,haze:0.12}); ri.position.set(-34,13,-92); g.add(ri);
  const ge=makeGe({scale:1.1}); ge.position.set(-25,-0.3,-80); ge.rotation.y=0.3; g.add(ge);
  /* 溪云压城 */
  const xy=makeXiyun({n:8,pos:[0,12,-72],scale:44,seed:22795}); g.add(xy.g);
  const mist=makeMist({n:6,spread:[220,14,70],pos:[0,4,-56],scale:64,color:0x2a3648,op:0.12});
  g.add(mist.g);
  /* 水边蒹葭 */
  const jj=makeJianjia({n:12,w:10,seed:22796}); jj.position.set(-13,-0.9,-14); g.add(jj);
  const jj2=makeJianjia({n:9,w:8,seed:22797}); jj2.position.set(14,-0.9,-22); g.add(jj2);
  const motes=makeGlow({n:28,box:[170,18,66],pos:[0,9,-36],color:0x9fb2c8,size:4.4,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:28,n:12,d:5,color:0x05080e,seed:22798,sway:0.85,rim:0.10,rimC:0x93a8c4});
  fg1.g.position.set(-11,-1.2,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05080e,seed:22799,rim:0.10,rimC:0x93a8c4});
  fg2.g.position.set(12.5,-1.5,12); g.add(fg2.g);
  addLights(g,{c:0x9db0c6,i:0.34,p:[-40,50,-40]},{c:0x19222e,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0); ridge.update(t,0);
    ri.update(t,k); xy.update(t,k,0);
    jj.update(t); jj2.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bGaocheng(){ // 壹 · 高城汀洲 —— 一上高城万里愁，蒹葭杨柳似汀洲：凭堞望水，水国似乡
  const g=new THREE.Group();
  const water=makeWater({size:600,seg:96,amp:0.12,freq:0.14,speed:0.32,flow:[0.26,0.05],spec:0.62,
    deep:0x05080e,shallow:0x0c1520,skyc:0x121a27,moonDir:[-0.22,0.1,-0.95]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x9fb0c4);
  water.mesh.position.set(0,-0.52,-120); g.add(water.mesh);
  const grd=makeGround({r:78,c1:0x0a0f18,c2:0x161e2c,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,58);
  const yuan=makeYuan({r:250,h:8,seed:22802}); yuan.g.position.set(-14,0,-160); g.add(yuan.g);
  /* 高城垛口：前景城墙顶（凭堞处）——「一上高城」的城 */
  const wall=new GeoBag();
  const wb=new THREE.BoxGeometry(30,3.4,4.6);
  wb.translate(0,-0.2,0); wall.put(wb,0x1a212e);
  const wt=new THREE.BoxGeometry(30,0.22,5);
  wt.translate(0,1.65,0); wall.put(wt,0x232d3b);
  for(let s=-1;s<=1;s+=2){
    for(let i=0;i<10;i++){
      const cr=new THREE.BoxGeometry(0.62,0.7,0.5);
      cr.translate(-13.5+i*3,2.1,s*2.2); wall.put(cr,0x202a38);
    }
  }
  const nv=new THREE.Group();
  nv.add(wall.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0x93a8c4,i:0.15,p:2.4})));
  nv.position.set(2,-1.9,10.5); g.add(nv);
  /* 登楼人：立于堞后右侧，万里愁生（让开水面视线） */
  const poet=xyFigure(1.55); poet.position.set(6.2,1.15,8.8); poet.rotation.y=2.95; g.add(poet);
  /* 汀洲+蒹葭+杨柳：像极了江南 */
  const tz=makeTingzhou({r:7,scale:1.1,seed:22803}); tz.position.set(13,-0.5,-42); g.add(tz);
  const tz2=makeTingzhou({r:4.5,scale:0.9,seed:22804}); tz2.position.set(-11,-0.5,-56); g.add(tz2);
  const jj=makeJianjia({n:13,w:10,seed:22805}); jj.position.set(-12,-0.9,-16); g.add(jj);
  const jj2=makeJianjia({n:10,w:8,seed:22806}); jj2.position.set(15,-0.9,-26); g.add(jj2);
  const yl=makeYangliu({seed:22807,scale:1.25}); yl.position.set(-14,-0.3,-22); yl.rotation.y=0.4; g.add(yl);
  const yl2=makeYangliu({seed:22808,scale:0.95}); yl2.position.set(21,-0.3,-44); yl2.rotation.y=-0.3; g.add(yl2);
  const mist=makeMist({n:6,spread:[220,12,70],pos:[0,2.4,-60],scale:60,color:0x2a3648,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[170,16,64],pos:[0,8,-32],color:0x9fb2c8,size:4.2,speed:0.035,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:5,color:0x05080e,seed:22809,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(-12,-1.6,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',w:20,n:9,d:4,color:0x05080e,seed:22810,sway:0.8,rim:0.09,rimC:0x93a8c4});
  fg2.g.position.set(13,-1.4,12.5); g.add(fg2.g);
  addLights(g,{c:0x9db0c6,i:0.38,p:[-38,52,-38]},{c:0x1a2330,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0);
    poet.update(t,k);
    jj.update(t); jj2.update(t); yl.update(t); yl2.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bFenglou(){ // 贰（标志性瞬间）· 溪云风楼 —— 溪云初起日沉阁，山雨欲来风满楼：雨前压迫感拉满
  const g=new THREE.Group();
  const grd=makeGround({r:100,c1:0x0a0f18,c2:0x171f2d,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:16,layers:2,peaks:4,seed:22811,color:0x0c1220,atmo:0x1f2937,
    fogK:0.64,glowK:0.05,glow:0xc8d2dc,y:-10,order:-6});
  ridge.g.position.set(0,0,-112); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 城楼主体：垛口城墙上 doble-eave 门楼，风雨将至 */
  const lou=makeChenglou({scale:2.0,rim:0.18,seed:22812}); lou.position.set(2,-0.3,-34);
  lou.rotation.y=0.05; g.add(lou);
  /* 楼头旗幡：初动（风满楼之始） */
  const qf=makeQifan({seed:22813}); qf.position.set(2,6.1,-31); g.add(qf);
  /* 溪云自水面横推压城 */
  const xy=makeXiyun({n:10,box:[160,10,24],pos:[-6,13,-54],scale:52,seed:22814}); g.add(xy.g);
  const xy2=makeXiyun({n:6,box:[130,7,18],pos:[-20,18,-70],scale:44,seed:22815}); g.add(xy2.g);
  /* 残日半沉阁后 */
  const ri=makeCanri({r:7.5,op:0.26,haze:0.12}); ri.position.set(-30,10,-84); g.add(ri);
  const ge=makeGe({scale:1.5}); ge.position.set(-24,-1.2,-76); ge.rotation.y=0.25; g.add(ge);
  /* 风线穿楼：定向雾流横扫 */
  const wind=makeFlow({n:240,box:[130,11,46],pos:[0,8,-18],color:0x55627a,size:15,speed:4.5,maxA:0.10});
  g.add(wind.points);
  const mist=makeMist({n:7,spread:[230,14,76],pos:[0,6,-52],scale:68,color:0x2a3648,op:0.13});
  g.add(mist.g);
  /* 城头远影 + 城下旅人 */
  const poet=xyFigure(1.5); poet.position.set(-10,6.2,-27); poet.rotation.y=3.0; g.add(poet);
  const crowd=makeCrowd({n:3,rect:[-16,-18,9,4],seed:22816,color:0x1c2534,rimC:0x93a8c4,
    rim:0.16,sMin:0.55,sMax:0.62,y:-1.1});
  g.add(crowd.mesh);
  const motes=makeGlow({n:26,box:[160,18,62],pos:[0,9,-30],color:0x9fb2c8,size:4.2,speed:0.04,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x0d1119,seed:22817,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(-12,-1.5,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:18,n:5,d:4,color:0x0a0e15,seed:22818,sway:1.1,rim:0.09,rimC:0x93a8c4});
  fg2.g.position.set(12.5,-1.4,13); g.add(fg2.g);
  addLights(g,{c:0x8fa2b8,i:0.3,p:[-36,48,-36]},{c:0x18212d,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0);
    qf.update(t,k,0.5);
    xy.update(t,k,0); xy2.update(t,k,0);
    ri.update(t,k); wind.update(t);
    mist.update(t,k); motes.update(t);
    poet.update(t,k); crowd.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bQinyuan(){ // 叁 · 秦苑汉宫 —— 鸟下绿芜秦苑夕，蝉鸣黄叶汉宫秋：帝业成空，荒烟蔓草
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0f17,c2:0x161f2b,y:-1.2}); g.add(grd.mesh);
  const ridge=makeRange({r:320,h:20,layers:2,peaks:5,seed:22821,color:0x0c1220,atmo:0x1f2937,
    fogK:0.62,glowK:0.06,glow:0xc8d2dc,y:-10,order:-6});
  ridge.g.position.set(-20,0,-116); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 秦苑断墙（左）+ 汉宫遗阁（右远） */
  const gq=makeGongqiang({scale:1.3,seed:22822}); gq.position.set(-9,-1.2,-40);
  gq.rotation.y=0.22; g.add(gq);
  const ge=makeGe({scale:2.3,rim:0.16}); ge.position.set(14,-1.2,-56); ge.rotation.y=-0.3; g.add(ge);
  /* 绿芜+黄叶树 */
  const lv1=makeLvwu({n:6,w:18,d:9,seed:22823}); lv1.position.set(-4,-1.2,-28); g.add(lv1);
  const lv2=makeLvwu({n:4,w:12,d:7,seed:22824}); lv2.position.set(8,-1.2,-38); g.add(lv2);
  const hs1=makeHuangyeshu({seed:22825,scale:1.3}); hs1.position.set(-2,-1.2,-22); g.add(hs1);
  const hs2=makeHuangyeshu({seed:22826,scale:1.05}); hs2.position.set(6,-1.2,-31); g.add(hs2);
  const hs3=makeHuangyeshu({seed:22827,scale:0.85}); hs3.position.set(-15,-1.2,-42); g.add(hs3);
  /* 鸟下：盘旋下坠归芜 */
  const nx=makeNiaoxia({n:6,cx:0,cy:9,cz:-32,seed:22828}); g.add(nx);
  /* 黄叶缓落 */
  const hy=makeGlow({n:44,box:[52,13,30],pos:[0,7,-27],color:0x6b6446,size:2.6,speed:0.1,rise:-1,add:false,maxA:0.14});
  g.add(hy.points);
  const mist=makeMist({n:7,spread:[220,14,70],pos:[0,5,-50],scale:64,color:0x2a3648,op:0.13});
  g.add(mist.g);
  /* 凭吊人（右前高处望苑）+ 远客二三人（行人） */
  const rock=makeForeground({kind:'坡石',n:2,r:2.0,w:8,d:4,color:0x0d1119,seed:22829,rim:0.1,rimC:0x93a8c4});
  rock.g.position.set(9.5,-1.4,-6.5); g.add(rock.g);
  const poet=xyFigure(1.7); poet.position.set(9.5,-0.3,-6.5); poet.rotation.y=2.75; g.add(poet);
  const crowd=makeCrowd({n:3,rect:[2,-34,10,6],seed:22830,color:0x1c2534,rimC:0x93a8c4,
    rim:0.16,sMin:0.55,sMax:0.62,y:-1.1});
  g.add(crowd.mesh);
  const motes=makeGlow({n:24,box:[150,16,60],pos:[0,8,-30],color:0x9fb2c8,size:4.0,speed:0.035,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:5,color:0x0c1018,seed:22831,rim:0.08,rimC:0x93a8c4});
  fg1.g.position.set(-12,-1.7,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:16,n:5,d:4,color:0x0a0e15,seed:22832,sway:0.8,rim:0.08,rimC:0x93a8c4});
  fg2.g.position.set(13,-1.5,12.5); g.add(fg2.g);
  addLights(g,{c:0x8fa2b8,i:0.32,p:[-34,50,-34]},{c:0x18212d,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0);
    nx.update(t); hy.update(t);
    mist.update(t,k); motes.update(t);
    poet.update(t,k); rock.update(t,k); crowd.update(t);
    hs1.update(t); hs2.update(t); hs3.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bWeishui(){ // 肆（末境·可点击）· 渭水东流 —— 行人莫问当年事，故国东来渭水流：点击风满楼（风起云涌+雨点初落+旗幡乱卷）
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  /* 渭水：东流不止 */
  const water=makeWater({size:620,seg:96,amp:0.17,freq:0.12,speed:0.5,flow:[0.85,0.14],spec:0.66,
    deep:0x05080e,shallow:0x0c1520,skyc:0x101926,moonDir:[-0.2,0.1,-0.95]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x93a8c4);
  water.mesh.position.set(0,-0.52,-130); g.add(water.mesh);
  const grd=makeGround({r:76,c1:0x090e16,c2:0x141c28,y:-0.28}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.28,58);
  const yuan=makeYuan({r:260,h:7,peaks:4,seed:22841}); yuan.g.position.set(8,0,-156); g.add(yuan.g);
  /* 危楼临水：旗幡在风里（初动）——点击后乱卷 */
  const lou=makeChenglou({scale:1.5,rim:0.17,seed:22842}); lou.position.set(14,-0.28,-30);
  lou.rotation.y=-0.38; g.add(lou);
  const qf=makeQifan({seed:22843}); qf.position.set(14,4.5,-27.5); qf.rotation.y=-0.1; g.add(qf);
  /* 溪云压城：点击涌动 */
  const xy=makeXiyun({n:10,box:[170,10,24],pos:[0,13,-56],scale:54,seed:22844}); g.add(xy.g);
  /* 雨点初落：点击前 visible=false 硬关 */
  const rain=makeYudian({n:420,pos:[2,-2,-30],seed:22845}); g.add(rain.g);
  /* 风线穿楼：点击后风声骤起 */
  const wind=makeFlow({n:260,box:[130,12,50],pos:[0,8,-16],color:0x55627a,size:15,speed:5,maxA:0.10});
  g.add(wind.points);
  /* 残照余烬：天际一线青灰（accent；初值=最大，点击后反衬风雨欲来而略增） */
  const hzg=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x93a8c4,
    transparent:true,opacity:0.11,depthWrite:false,fog:false}));
  hzg.scale.set(150,17,1); hzg.position.set(-20,5.5,-96); g.add(hzg);
  /* 凭堞行人（左前） */
  const poet=xyFigure(1.75); poet.position.set(-7,-0.26,-5.5); poet.rotation.y=2.9; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:5,color:0x06090f,seed:22846,rim:0.11,rimC:0x93a8c4});
  rock.g.position.set(-8.2,-1.4,-4.2); g.add(rock.g);
  const mist=makeMist({n:7,spread:[220,14,72],pos:[0,5,-52],scale:66,color:0x2a3648,op:0.13});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[160,16,62],pos:[0,8,-30],color:0x9fb2c8,size:4.0,speed:0.035,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:11,d:5,color:0x05080e,seed:22847,sway:0.9,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(-11,-1.3,11); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x05080e,seed:22848,rim:0.09,rimC:0x93a8c4});
  fg2.g.position.set(12.5,-1.5,11.5); g.add(fg2.g);
  addLights(g,{c:0x8fa2b8,i:0.28,p:[-32,46,-38]},{c:0x161e2a,i:0.52});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/2.6);
      const rv=ctl.reveal, e=rv*rv*(3-2*rv);
      rain.update(t,k,e);                       // 雨点初落渐密
      rain.g.rotation.z=0.07+0.11*e;            // 风紧雨斜
      xy.update(t,k,e);                         // 云阵涌动
      qf.update(t,k,0.85+2.7*e);                // 旗幡乱卷
      wind.mat.uniforms.uMaxA.value=k*(0.10+0.08*e); wind.update(t);  // 风声骤起
      hzg.material.opacity=k*0.11*(0.62+0.38*e)*(0.85+0.15*Math.sin(t*0.3));
      water.update(t); yuan.update(t,0);
      mist.update(t,k); motes.update(t);
      poet.update(t,k); rock.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.16);                          // 风雨声骤起
        pluck(5,0.05,0.12); pluck(3,0.5,0.10); pluck(1,1.05,0.09);   // 风声三叠
        const fl=$('#flash'); fl.textContent='溪云初起日沉阁 山雨欲来风满楼';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0a101a),hor:C(0x253040),bot:C(0x070b12),fog:C(0x121a26),fd:0.0056,star:0.10,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0x9db0c6),dirI:0.36,
  dirP:new THREE.Vector3(-40,55,-45),ambC:C(0x1a2230),ambI:0.58},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8.6,42],t:[0,8.9,36],lf:[0,9.4,-30],lt:[2,9.8,-44]},
  sky:()=>SK({fd:0.0050,star:0.08,hor:C(0x28303e)}) },
{ name:'高城汀洲',dwell:16,river:0.02,build:bGaocheng,
  cam:{f:[-0.5,6.8,21.5],t:[-1.2,6.3,15.5],lf:[0,6.8,-18],lt:[-2,7,-34]},
  sky:()=>SK({fd:0.0052,star:0.06,hor:C(0x2a3240),dirC:C(0x9db0c6),dirI:0.38,
    ambC:C(0x1a2330),ambI:0.58}) },
{ name:'溪云风楼',dwell:19,river:0.02,build:bFenglou,
  cam:{f:[0,5.4,27],t:[0,5.8,20],lf:[0,9,-28],lt:[0,9.6,-46]},
  sky:()=>SK({fd:0.0068,star:0.02,top:C(0x080c14),hor:C(0x1e2836),bot:C(0x060a10),
    dirC:C(0x8fa2b8),dirI:0.30,ambC:C(0x18212d),ambI:0.54}) },
{ name:'秦苑汉宫',dwell:17,river:0.02,build:bQinyuan,
  cam:{f:[-1,6.0,27],t:[0.5,6.2,21],lf:[0,7,-32],lt:[2,7.5,-50]},
  sky:()=>SK({fd:0.0060,star:0.03,hor:C(0x232d3b),dirC:C(0x8fa2b8),dirI:0.32,
    ambC:C(0x18212d),ambI:0.54}) },
{ name:'渭水东流',dwell:19,river:0.02,build:bWeishui,
  cam:{f:[0,7.2,20],t:[0,7.0,15],lf:[0,7.2,-24],lt:[0,7.8,-42]},
  sky:()=>SK({fd:0.0076,star:0.01,top:C(0x070b12),hor:C(0x1a232f),bot:C(0x05080d),
    dirC:C(0x8fa2b8),dirI:0.26,ambC:C(0x161e2a),ambI:0.52}) },
];
"""
