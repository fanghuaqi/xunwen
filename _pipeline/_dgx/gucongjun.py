# -*- coding: utf-8 -*-
"""gucongjun.py —— 《古从军行》（唐·李颀，queue no.265，水墨夜思）生成配置
3 境（对句成境，mk split [2,2,2]）：
壹 烽火饮马（白日登山望烽火+黄昏饮马傍交河+行人刁斗风沙暗+公主琵琶幽怨多——
  戍边日常长卷：烽燧一点火、交河一带水、饮马牵马人、营前刁斗、帐前琵琶、风沙行军），
贰 胡雁哀鸣（野云万里无城郭+雨雪纷纷连大漠+胡雁哀鸣夜夜飞+胡儿眼泪双双落——
  标志性瞬间：雨雪旷野之上雁阵掠月南飞，两个胡家少年仰望雁阵、泪光双双而落），
叁 蒲桃入汉（闻道玉门犹被遮+应将性命逐轻车+年年战骨埋荒外+空见蒲桃入汉家——
  末境点击：驼队驮蒲桃入关剪影缓缓过境，与荒野战骨的冷意相对；克制写意不画骸骨）。
美术立意「交河戍晚，胡汉两伤」：水墨夜思全套色板——底色 #0d1117、雾 #111823～#131a26 系、
文字 #e2e8f0，accent=#8fa8c0（queue 分配强调色，月灰蓝）只落在 UI/人物边缘光/刁斗琵琶声光/
雁阵微光/泪光/驼篓蒲桃微光上，全页近零饱和；唯烽火一点暖（0xd98a4a 系）与蒲桃一簇暗紫
（0x4a3c58 系，非 accent）为有意保留的例外——「葡萄入汉家」正是全诗讽刺的落点。
与已有页第一眼可区分：不做黄沙金甲孤城誓言（congjunxing-yumen）、不做咸阳桥送别长卷
（bingchexing）、不做雪原戍楼听笛（saishang-chuidi）、不做归途四时对切（caiwei-jiexuan）——
本页是**交河畔的戍边日常与胡汉同悲**：烽燧、交河、饮马、刁斗、琵琶、雨雪、胡雁、玉门关、驼队。
自建 builder：makeBeaconGCJ（烽燧）/ makeRiverGCJ（交河）/ makeDrinkHorseGCJ（饮马）/
makeDiaoDouGCJ（刁斗+更声光）/ makePipaTentGCJ（毡帐琵琶+幽怨声光）/ makeGooseFlockGCJ（胡雁阵）/
makeHuChildGCJ（胡儿泪）/ makeYumenGCJ（玉门关）/ makeFallenGCJ（荒冢断戟，无骸骨）/
makeCamelGCJ（驮蒲桃双峰驼）/ makeCaravanGCJ（驼队，点击前 visible=false 硬关）/ makeRoadGCJ（关道）/
makeSteppeGCJ（荒原基底，山环置于骨架常驻远山环之前）。
考点钉子：刁 diāo 斗／蒲桃=葡萄／遮 zhē（小测第 3 题）；李颀借汉喻唐（第 4 题）；
胡汉两伤的反战讽刺——「年年战骨埋荒外，空见蒲桃入汉家」（第 5 题）。
多音字：饮马 yìn、应将 yīng（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='gucongjun', title='古从军行', dyn='唐 · 李颀', brand_author='李 颀',
    gold_rgb='143,168,192',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#8fa8c0; --ink:#e2e8f0; --dim:#7e8a9a; --paper:rgba(9,13,20,.60);
  --line:rgba(143,168,192,.26);
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
        ('0x0a1526', '0x121a26', 4),
    ],
    tip='轻点画面 / 按空格 —— 驼队驮蒲桃缓缓入关，荒野战骨犹寒',
    hint='← → 键或空格逐境游览 · 末境可点击画面：驼队驮蒲桃入关剪影缓缓过境，与荒野战骨的冷意相对',
    cover_read='古从军行。唐，李颀。白日登山望烽火，黄昏饮马傍交河。行人刁斗风沙暗，公主琵琶幽怨多。',
    cover_p1='三重意境，随诗句次第展开：白日登山望烽火，黄昏饮马傍交河，行人刁斗风沙暗，公主琵琶幽怨多；野云万里无城郭，雨雪纷纷连大漠，胡雁哀鸣夜夜飞，胡儿眼泪双双落；闻道玉门犹被遮，应将性命逐轻车，年年战骨埋荒外，空见蒲桃入汉家。',
    cover_p2='边读诗，边做一回交河畔的戍卒：白天登高望烽火，黄昏牵马去饮水，夜里听刁斗与琵琶声此起彼伏；再看雨雪大漠之上，胡雁哀鸣着南飞，胡家的孩子仰起脸落泪；最后看一眼玉门关外——葡萄年年入汉家，而人年年埋骨荒外。胡汉两伤，此之谓也。',
    end_h2='战骨 · 蒲桃', cn_word='叁',
    words_js="['再望一回烽火','初识李颀，尚需共读','渐入诗境，再诵几遍','刁斗琵琶，声声入耳','已解胡汉两伤之悲','蒲桃入汉，战骨犹寒']",
    sky_atmo='0x232f45',
)

POEM_JS = """const POEM = [
{ name:'烽火饮马', jing:'白天登上山头，瞭望的是报警的烽火；黄昏时分牵马到交河边上饮水。风沙昏暗里，行军的队伍带着刁斗夜行，和亲公主车队中的琵琶声，传出多少幽怨。（登山望烽 · 黄昏饮马 · 刁斗琵琶）',
  segs:[
   {c:'白日登山望烽火，', p:py('bái rì dēng shān wàng fēng huǒ')},
   {c:'黄昏饮马傍交河。', p:py('huáng hūn yìn mǎ bàng jiāo hé')},
   {c:'行人刁斗风沙暗，', p:py('xíng rén diāo dǒu fēng shā àn')},
   {c:'公主琵琶幽怨多。', p:py('gōng zhǔ pí pá yōu yuàn duō')}],
  read:'白日登山望烽火，黄昏饮马傍交河。行人刁斗风沙暗，公主琵琶幽怨多。',
  yisi:'白天登上山头，瞭望的是报警的烽火；黄昏时分牵马到交河边上饮水。风沙昏暗中，行军的队伍带着刁斗在行进，和亲公主车队里的琵琶声，传出多少幽怨。——首四句一天之内、两地之间：白日与黄昏、山上与河畔、望烽火的紧张与饮马的日常交替剪影，戍边生活的苍凉底色已经铺开。「行人刁斗」以声写夜，「公主琵琶」以乐写怨——两件乐器都不是欢音：一个是警戒巡更的铜声，一个是离乡去国的哀音，声声都在说，这里的日日夜夜是熬出来的。',
  zhu:[['烽火','古代边防报警的烟火——白天放烟叫「燧」，夜里举火叫「烽」，此处泛指边地的警报'],['饮马','给马喝水。饮，读 yìn，使（人或牲口）喝水——「饮马」是戍边生活最日常的一幕'],['交河','河名，在今新疆吐鲁番一带，唐代为西陲戍守之地——点出万里之外的边地'],['行人','指出征、戍守的将士——风沙中行进的队伍'],['刁斗','军中铜制器具，读 diāo dǒu——白天用来做饭，夜间敲击以巡更报警'],['公主琵琶','汉武帝把江都王之女封为公主嫁乌孙国，途中命人在马上弹琵琶以解乡愁——后世以「公主琵琶」写和亲离乡之怨'],['幽怨','深藏心底的怨恨哀愁——琵琶声声，皆是离乡去国之悲']] },
{ name:'胡雁哀鸣', jing:'旷野上空的阴云绵延万里，望不见一座城郭；雨雪纷纷扬扬，与苍茫大漠连成一片。胡地的鸿雁哀鸣着，夜夜向南飞去；胡人的孩子仰望雁阵，眼泪一双双落下。（野云万里 · 雨雪大漠 · 胡雁胡儿）（标志性瞬间：雨雪纷纷的旷野上，胡雁哀鸣着夜夜飞过，胡儿仰望雁阵、眼泪双双而落）',
  segs:[
   {c:'野云万里无城郭，', p:py('yě yún wàn lǐ wú chéng guō')},
   {c:'雨雪纷纷连大漠。', p:py('yǔ xuě fēn fēn lián dà mò')},
   {c:'胡雁哀鸣夜夜飞，', p:py('hú yàn āi míng yè yè fēi')},
   {c:'胡儿眼泪双双落。', p:py('hú ér yǎn lèi shuāng shuāng luò')}],
  read:'野云万里无城郭，雨雪纷纷连大漠。胡雁哀鸣夜夜飞，胡儿眼泪双双落。',
  yisi:'旷野上空的阴云绵延万里，望不见一座城郭；雨雪纷纷扬扬，与苍茫的大漠连成一片。胡地的鸿雁哀鸣着，夜夜向南飞去；胡人的孩子仰望雁阵，眼泪一双双落下。——「无城郭」三字写尽戍地的荒寂：人烟断绝，天地之间只剩野云、雨雪与大漠。胡雁尚且夜夜南飞，胡儿却只能仰望哀鸣的雁阵落泪——连西域本地的少年都为这场无休止的战争悲伤，「胡汉两伤」至此和盘托出：战争没有赢家，只有两边都数不尽的眼泪与白骨。',
  zhu:[['城郭','城，内城；郭，外城——泛指城邑，「无城郭」极言戍地荒远、人烟稀绝'],['雨雪','下雪。「雨」在这里作动词用，纷纷扬扬的大雪与荒漠连成一片'],['胡雁','西域胡地的鸿雁——雁尚知南飞避寒，年年迁徙'],['哀鸣','悲哀地鸣叫——雁声凄切，如闻边地之悲'],['夜夜','每夜——战事不休，雁阵夜夜南飞，戍卒夜夜难归'],['胡儿','西域各族的少年——连胡人的孩子都为之落泪'],['双双','成双成对——泪落成对，与「夜夜」相对，写尽悲伤的绵密不绝']] },
{ name:'蒲桃入汉', jing:'听人说玉门关还被拦阻着、不许将士归来，性命只得跟着轻车将军继续拼杀。年复一年，多少战骨埋葬在荒远之外；能看见进关的，只有一队队驮着蒲桃的驼队，进入汉家。（玉门被遮 · 战骨荒外 · 蒲桃入汉）（末境点击画面：驼队驮着蒲桃入关的剪影缓缓过境，与荒野战骨的冷意相对）',
  segs:[
   {c:'闻道玉门犹被遮，', p:py('wén dào yù mén yóu bèi zhē')},
   {c:'应将性命逐轻车。', p:py('yīng jiāng xìng mìng zhú qīng chē')},
   {c:'年年战骨埋荒外，', p:py('nián nián zhàn gǔ mái huāng wài')},
   {c:'空见蒲桃入汉家。', p:py('kōng jiàn pú táo rù hàn jiā')}],
  read:'闻道玉门犹被遮，应将性命逐轻车。年年战骨埋荒外，空见蒲桃入汉家。',
  yisi:'听人说玉门关还被拦阻着、不许将士归来，性命只好交给轻车将军，跟着他继续在沙场上拼掷。年复一年，多少战骨埋葬在荒远之外；能看见进关的，只有一队队驮着蒲桃的驼队，进入汉家。——末四句是全诗的诗眼：仗打赢打输都回不了家（「玉门犹被遮」用汉武帝下诏遮断玉门、不许罢兵的典故），士卒的性命轻贱如草芥；「年年」与「空见」相对——人埋在荒外，葡萄却进了汉家：用无数生命换来的「战果」，不过是几串葡萄。讽刺冷峻之至，却不著一句议论，反战之意自见。',
  zhu:[['玉门','玉门关，故址在今甘肃敦煌西北，通往西域的要隘——「犹被遮」用汉武帝太初年间下诏遮断玉门关、不许征宛士卒罢兵归来的典故，借指朝廷不许收兵'],['被遮','被阻拦、被拦住——归路被挡在关外'],['逐轻车','追随轻车将军继续作战。逐，追随；轻车，汉代轻车将军之省，代指统兵将帅'],['战骨','战死者的骸骨——「年年战骨埋荒外」，年年都有人埋骨他乡'],['荒外','极荒远的边外之地'],['蒲桃','即葡萄，原产西域，汉代传入中原——战骨埋于荒外，换来的只是蒲桃年年入关'],['空见','只看见、徒然看见——一个「空」字，是全诗讽刺的落点'],['借汉喻唐','诗中「公主琵琶」「玉门」「汉家」皆用汉代故事，实写唐玄宗开边之事——以汉喻唐，含蓄而有力']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「白日登山望烽火，」的下一句是？', o:['黄昏饮马傍交河','行人刁斗风沙暗','野云万里无城郭'], a:0},
 {q:'「胡雁哀鸣夜夜飞，」的下一句是？', o:['公主琵琶幽怨多','胡儿眼泪双双落','年年战骨埋荒外'], a:1},
 {q:'下列各项中，加点字的读音和词义解说全都正确的一项是？', o:['「行人刁斗风沙暗」的「刁斗」读 diāo dǒu，军中铜器，白天做饭、夜间敲更；「闻道玉门犹被遮」的「遮」读 zhē，拦阻；「空见蒲桃入汉家」的「蒲桃」即葡萄','「行人刁斗风沙暗」的「刁斗」读 diāo dòu，指短兵相接的格斗；「闻道玉门犹被遮」的「遮」读 zhà，指帐幕遮拦；「蒲桃」指一种桃树','「行人刁斗风沙暗」的「刁斗」读 dāo dǒu，指舀汤的勺子；「闻道玉门犹被遮」的「遮」读 zhé，指折断；「蒲桃」指核桃'], a:0},
 {q:'李颀是唐代边塞诗人，本诗写唐代时事，却通篇用汉家故事（公主琵琶、玉门、汉家）。对这种写法，理解正确的一项是？', o:['诗人记错了朝代，把唐代的事误写成了汉代的故事','借汉喻唐——以汉武帝开边、遮断玉门、公主和亲的故事影射唐玄宗好大喜功、频繁用兵，含蓄而有力','本诗题咏汉代历史，与唐代现实无关，只是发思古之幽情'], a:1},
 {q:'对「年年战骨埋荒外，空见蒲桃入汉家」与全诗主旨，理解最恰当的一项是？', o:['赞美边将开疆拓土的功业，蒲桃入关正是四方来朝的盛世气象','感慨边地风物美好，战事只是诗歌的背景点缀','胡汉两伤的反战讽刺——汉卒战骨埋于荒外，换来的却只是蒲桃入汉家；胡儿落泪、汉卒埋骨，两边都是这场开边之战的牺牲者'], a:2},
];
"""

SCENES_JS = """/* ================= 古从军行 · 三境场景（水墨夜思·戍边苍凉变体：烽火饮马、胡雁哀鸣、蒲桃入汉） =================
   美术立意：「交河戍晚，胡汉两伤」——白日烽烟、黄昏饮马的戍边日常起笔，
   中段以万里野云、雨雪大漠托起胡雁哀鸣、胡儿眼泪（标志性瞬间），
   末境玉门被遮、战骨埋荒外，点击看驼队驮蒲桃入关剪影缓缓过境——
   关内蒲桃满篓、关外战骨埋荒：讽刺尽在不言中（克制写意，不画骸骨）。
   水墨夜思全套色板：底色 #0d1117、雾 #111823～#131a26 系，accent=#8fa8c0
   （queue 分配强调色，月灰蓝）只落在 UI/人物边缘光/刁斗琵琶声光/雁阵微光/泪光/驼篓微光上；
   唯烽火一点暖与蒲桃一簇暗紫为有意保留的例外。
   与已有页第一眼可区分：不做黄沙金甲孤城誓言（congjunxing-yumen）、不做咸阳桥送别长卷
   （bingchexing）、不做雪原戍楼听笛（saishang-chuidi）——本页是交河畔的戍边日常与胡汉同悲。 */

/* —— 烽燧 makeBeaconGCJ(o)：夯土烽火台（锥台身 + 腰线 + 顶部垛口 + 火池）+ 小火焰 + 火光
   「白日登山望烽火」：荒原上唯一的一点暖 */
function makeBeaconGCJ(o){
  o=o||{};
  const H=o.h===undefined?7.5:o.h, rB=o.rB===undefined?2.6:o.rB, rT=o.rT===undefined?1.7:o.rT;
  const bodyC=o.bodyC===undefined?0x171d27:o.bodyC;
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(rT,rB,H,9);
  body.translate(0,H/2,0); B.put(body,bodyC);
  const band=new THREE.CylinderGeometry(rT*1.06,rT*1.12,H*0.14,9);
  band.translate(0,H*0.52,0); B.put(band,shadeColor(bodyC,1.18));
  for(let i=0;i<7;i++){
    const a=i/7*Math.PI*2;
    const m=new THREE.BoxGeometry(0.44,0.55,0.36);
    m.translate(Math.sin(a)*rT*0.84,H+0.24,Math.cos(a)*rT*0.84);
    B.put(m,shadeColor(bodyC,0.94));
  }
  const pool=new THREE.CylinderGeometry(rT*0.55,rT*0.40,0.36,8);
  pool.translate(0,H+0.16,0); B.put(pool,0x0d1016);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3444,emissive:0x05070b}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.13:o.rim,p:2.2})));
  const fl=makeFlame({h:o.fh===undefined?2.0:o.fh,w:o.fw===undefined?0.9:o.fw,planes:3,
    embers:o.embers===undefined?26:o.embers,spark:o.spark!==false,light:o.light===undefined?1.15:o.light,
    lightD:o.lightD===undefined?44:o.lightD,core:o.core===undefined?0xffd9a0:o.core,
    outer:o.outer===undefined?0xb5501e:o.outer,wide:0.32});
  fl.g.position.y=H+0.35; g.add(fl.g);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd98a4a,
    transparent:true,opacity:o.glowOp===undefined?0.12:o.glowOp,depthWrite:false,fog:false,
    blending:THREE.AdditiveBlending}));
  glow.scale.set(o.glowW===undefined?7.5:o.glowW,o.glowW*0.8,1);
  glow.position.y=H+1.4; g.add(glow);
  const glowOp0=glow.material.opacity;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    fl.update(t,kk);
    glow.material.opacity=kk*glowOp0*(0.8+0.2*Math.sin(t*2.1));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 交河 makeRiverGCJ(o)：斜贯荒原的窄河（makeWater 压缩成带，shader 自带月光镜面、雾自动同步）—— */
function makeRiverGCJ(o){
  o=o||{};
  const water=makeWater({size:o.size===undefined?440:o.size,seg:72,amp:o.amp===undefined?0.10:o.amp,
    freq:0.14,speed:0.26,flow:[0.08,0.26],spec:o.spec===undefined?0.95:o.spec,
    deep:0x0a1119,shallow:0x16222f,skyc:0x1e2a3a,moonDir:o.moonDir===undefined?[-30,14,-130]:o.moonDir});
  water.mesh.material.uniforms.uMoonColor.value=C(0x9fb4c8);
  water.mesh.scale.set(o.narrow===undefined?0.17:o.narrow,1,1);
  water.mesh.rotation.y=o.rot===undefined?0.42:o.rot;
  water.mesh.position.set(o.x===undefined?0:o.x,o.y===undefined?-0.06:o.y,o.z===undefined?-38:o.z);
  return water;
}

/* —— 饮马 makeDrinkHorseGCJ(o)：低头就水的战马剪影（身/胸/颈/垂首/四足/尾），合批 1 mesh
   「黄昏饮马傍交河」：马首低垂近水面，静立河畔 */
function makeDrinkHorseGCJ(o){
  o=o||{};
  const c=o.color===undefined?0x11161e:o.color, B=new GeoBag();
  const body=new THREE.SphereGeometry(0.62,10,8);
  body.scale(1.45,0.82,0.62); body.translate(0,1.42,0); B.put(body,c);
  const chest=new THREE.SphereGeometry(0.42,8,7);
  chest.scale(1,1.15,0.7); chest.translate(-0.72,1.34,0); B.put(chest,shadeColor(c,1.08));
  const rump=new THREE.SphereGeometry(0.46,8,7);
  rump.scale(1,1.05,0.68); rump.translate(0.78,1.40,0); B.put(rump,shadeColor(c,0.94));
  B.put(limbGeo([-0.98,1.62,0],[-1.42,0.80,0],0.24,0.15,6),shadeColor(c,1.04));
  const head=new THREE.SphereGeometry(0.24,7,6);
  head.scale(1.5,0.8,0.55); head.rotateZ(0.5); head.translate(-1.58,0.58,0); B.put(head,shadeColor(c,1.1));
  const ear=new THREE.ConeGeometry(0.05,0.16,4); ear.translate(-1.42,0.80,0); B.put(ear,shadeColor(c,1.2));
  B.put(limbGeo([1.18,1.52,0],[1.34,0.92,-0.06],0.07,0.03,5),shadeColor(c,0.8));
  [[0.62,0.28],[0.88,-0.16],[-0.50,0.30],[-0.86,-0.14]].forEach(function(l,i){
    B.put(limbGeo([l[0],1.18,l[1]],[l[0]+0.03,0.06,l[1]],0.09,0.05,5),shadeColor(c,0.9+0.06*i));
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3644,emissive:0x04060a}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.15:o.rim,p:2.3})));
  const ph=(o.seed===undefined?26501:o.seed)%6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.012*Math.sin(t*0.7+ph)*kk;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 刁斗 makeDiaoDouGCJ(o)：军中铜刁斗（三足铜锅 + 长柄）架在营前木叉上 + 定更声光脉冲
   「行人刁斗风沙暗」：白天做饭、夜里敲更的行军铜器，声光荡开极克制 */
function makeDiaoDouGCJ(o){
  o=o||{};
  const B=new GeoBag();
  [-0.34,0.34].forEach(function(x){
    B.put(limbGeo([x,0,0],[x*1.12,1.9,0],0.055,0.045,5),0x141922);
    B.put(limbGeo([x*1.12,1.9,0],[x*0.6,2.2,0],0.045,0.035,5),0x141922);
  });
  B.put(limbGeo([-0.62,2.2,0],[0.62,2.2,0],0.035,0.035,5),0x161b24);
  const pot=new THREE.SphereGeometry(0.34,10,7,0,Math.PI*2,Math.PI*0.45,Math.PI*0.55);
  pot.scale(1,0.85,1); pot.translate(0,1.98,0); B.put(pot,0x3a4252);
  const rim=new THREE.TorusGeometry(0.33,0.03,5,14);
  rim.rotateX(Math.PI/2); rim.translate(0,1.99,0); B.put(rim,0x4a5468);
  for(let i=0;i<3;i++){
    const a=i/3*Math.PI*2+0.4;
    B.put(limbGeo([Math.sin(a)*0.20,1.86,Math.cos(a)*0.20],[Math.sin(a)*0.13,1.60,Math.cos(a)*0.13],0.028,0.02,4),0x3a4252);
  }
  B.put(limbGeo([0.30,2.06,0],[0.92,2.32,0],0.032,0.022,5),0x4a5468);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0x5a6a82,emissive:0x05070b}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.18:o.rim,p:2.4})));
  const ring=new THREE.Mesh(new THREE.RingGeometry(0.5,0.60,26),
    new THREE.MeshBasicMaterial({color:o.waveC===undefined?0x8fa8c0:o.waveC,transparent:true,opacity:0,
      depthWrite:false,blending:THREE.AdditiveBlending,side:THREE.DoubleSide}));
  ring.rotation.x=-Math.PI/2; ring.position.y=2.05; g.add(ring);
  const period=o.period===undefined?4.2:o.period, ph=(o.seed===undefined?26502:o.seed)%period;
  const baseOp=o.waveOp===undefined?0.15:o.waveOp;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    const u=((t+ph)%period)/period;
    ring.scale.setScalar(0.5+u*3.2);
    ring.material.opacity=kk*baseOp*Math.sin(u*Math.PI)*Math.sin(u*Math.PI);
  };
  g.userData.update=g.update;
  return g;
}

/* —— 毡帐琵琶 makePipaTentGCJ(o)：公主毡帐（穹顶毡包 + 顶饰）+ 帐前曲项琵琶斜倚 + 幽怨声光涟漪
   「公主琵琶幽怨多」：和亲车队夜宿，马上之乐化作帐前幽怨 */
function makePipaTentGCJ(o){
  o=o||{};
  const R=o.r===undefined?2.6:o.r, H=o.h===undefined?3.1:o.h;
  const B=new GeoBag();
  const dome=new THREE.SphereGeometry(R,14,8,0,Math.PI*2,0,Math.PI*0.52);
  dome.scale(1,H/R,1); B.put(dome,0x181f2a);
  const skirt=new THREE.CylinderGeometry(R*0.99,R*1.06,H*0.22,14);
  skirt.translate(0,H*0.11,0); B.put(skirt,0x141a24);
  const finial=new THREE.SphereGeometry(0.12,6,5); finial.translate(0,H+0.10,0); B.put(finial,0x8fa8c0);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3444,emissive:0x05070a}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.12:o.rim,p:2.2})));
  const P=new GeoBag();
  const pear=new THREE.SphereGeometry(0.34,10,8);
  pear.scale(0.82,1.15,0.42); pear.translate(0,0.42,0); P.put(pear,0x2a2620);
  const face=new THREE.CylinderGeometry(0.27,0.30,0.03,10);
  face.rotateX(1.48); face.translate(0,0.44,0.14); P.put(face,0x38322a);
  const neck1=new THREE.CylinderGeometry(0.045,0.055,0.55,6); neck1.translate(0,1.02,0.02); P.put(neck1,0x2a2620);
  const neck2=new THREE.CylinderGeometry(0.04,0.045,0.34,6); neck2.rotateZ(0.38); neck2.translate(0.10,1.42,0.02); P.put(neck2,0x2a2620);
  const phead=new THREE.BoxGeometry(0.13,0.16,0.07); phead.rotateZ(0.38); phead.translate(0.16,1.60,0.02); P.put(phead,0x332e26);
  for(let i=0;i<4;i++){
    const st=new THREE.BoxGeometry(0.008,1.28,0.006); st.rotateZ(0.026*(i-1.5)); st.translate(0,0.95,0.155);
    P.put(st,0x6a7488);
  }
  P.put((function(){ const s=new THREE.BoxGeometry(0.5,0.06,0.30); s.translate(0,0.03,0); return s; })(),0x141922);
  const pipa=new THREE.Mesh(mergeGeos(P.list),
    new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,specular:0x3a4050,emissive:0x06080c}));
  pipa.rotation.z=-0.16; pipa.rotation.y=-0.7; pipa.position.set(R*0.72,0.06,0.4); g.add(pipa);
  const rings=[];
  for(let i=0;i<3;i++){
    const rg=new THREE.Mesh(new THREE.RingGeometry(0.9,1.0,30),
      new THREE.MeshBasicMaterial({color:o.waveC===undefined?0x8fa8c0:o.waveC,transparent:true,opacity:0,
        depthWrite:false,blending:THREE.AdditiveBlending,side:THREE.DoubleSide}));
    rg.rotation.x=-Math.PI/2; rg.position.set(R*0.72,0.14,0.4); rg.userData.ph=i/3;
    g.add(rg); rings.push(rg);
  }
  const period=o.period===undefined?6.0:o.period, baseOp=o.waveOp===undefined?0.12:o.waveOp;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    for(let i=0;i<rings.length;i++){
      const u=((t/period)+rings[i].userData.ph)%1;
      rings[i].scale.setScalar(0.5+u*4.6);
      rings[i].material.opacity=kk*baseOp*Math.sin(u*Math.PI)*Math.sin(u*Math.PI);
    }
  };
  g.userData.update=g.update;
  return g;
}

/* —— 胡雁阵 makeGooseFlockGCJ(o)：人字形雁阵（逐只振翅），缓缓横过高天 + 前导雁鸣声光
   「胡雁哀鸣夜夜飞」：雁阵掠过月光下的高天，声声哀鸣 */
function makeGooseFlockGCJ(o){
  o=o||{};
  const n=o.n===undefined?9:o.n, sc=o.scale===undefined?1.5:o.scale;
  const y0=o.y===undefined?24:o.y, y1=o.y1===undefined?30:o.y1, z=o.z===undefined?-58:o.z;
  const wingC=o.color===undefined?0x0c1017:o.color;
  const g=new THREE.Group(), geese=[];
  for(let i=0;i<n;i++){
    const gg=new THREE.Group();
    const body=new THREE.Mesh(new THREE.SphereGeometry(0.16,6,5),
      new THREE.MeshPhongMaterial({color:wingC,shininess:4,emissive:0x04060a}));
    body.scale(1.7,0.72,0.62); gg.add(body);
    const wmat=new THREE.MeshBasicMaterial({color:wingC,side:THREE.DoubleSide,transparent:true,opacity:0.94});
    const wg=new THREE.PlaneGeometry(0.30,0.80); wg.rotateX(-Math.PI/2);
    const wl=new THREE.Mesh(wg,wmat); wl.position.z=-0.52;
    const wr=new THREE.Mesh(wg.clone(),wmat); wr.position.z=0.52;
    gg.add(wl); gg.add(wr);
    gg.scale.setScalar(sc*(i===0?1.15:0.85+0.18*((i*7)%3)));
    geese.push({gg,wl,wr,ph:i*0.72,rank:Math.ceil(i/2),side:i===0?0:(i%2===1?1:-1)});
    g.add(gg);
  }
  const wave=new THREE.Mesh(new THREE.RingGeometry(0.6,0.72,22),
    new THREE.MeshBasicMaterial({color:o.waveC===undefined?0x8fa8c0:o.waveC,transparent:true,opacity:0,
      depthWrite:false,blending:THREE.AdditiveBlending,side:THREE.DoubleSide}));
  g.add(wave);
  const x0=o.x0===undefined?62:o.x0, x1=o.x1===undefined?-66:o.x1;
  const speed=o.speed===undefined?0.014:o.speed, span=o.span===undefined?1.35:o.span;
  const period=o.period===undefined?5.6:o.period, baseOp=o.waveOp===undefined?0.13:o.waveOp;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    const u=(t*speed)%1;
    const px=lerp(x0,x1,u);
    for(let i=0;i<geese.length;i++){
      const G=geese[i];
      G.gg.position.set(px+G.rank*span, y0+(y1-y0)*u-G.rank*0.18, z+G.side*G.rank*0.9);
      const flap=Math.sin(t*(o.flap===undefined?7.5:o.flap)+G.ph);
      G.wl.rotation.x=-0.55*flap; G.wr.rotation.x=0.55*flap;
      G.gg.rotation.z=0.06*Math.sin(t*0.5+G.ph);
    }
    const lead=geese[0].gg;
    const wu=(t%period)/period;
    wave.position.set(lead.position.x-1.2*sc,lead.position.y,lead.position.z);
    wave.scale.setScalar(0.4+wu*5.5);
    wave.material.opacity=kk*baseOp*Math.sin(wu*Math.PI)*Math.sin(wu*Math.PI);
  };
  g.userData.update=g.update;
  return g;
}

/* —— 胡儿泪 makeHuChildGCJ(o)：仰望雁阵的胡家少年（深衣小帽）+ 眼泪双双而落的微光
   「胡儿眼泪双双落」：并肩仰望，泪光成对垂落（克制写意，不见面目细节） */
function makeHuChildGCJ(o){
  o=o||{};
  const fig=makeFigure({pose:o.pose===undefined?'独立':o.pose,
    robe:o.robe===undefined?0x232028:o.robe,belt:o.belt===undefined?0x3d3a44:o.belt,
    skin:0xc9a884,collar:0x4a4652,hair:0x141317,hat:'无',noProp:true,
    rim:o.rim===undefined?0.34:o.rim,rimC:o.rimC===undefined?0x8fa8c0:o.rimC,
    scale:o.scale===undefined?0.66:o.scale});
  const tears=[], tearOp=o.tearOp===undefined?0.38:o.tearOp;
  [-0.09,0.09].forEach(function(x,i){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.tearC===undefined?0xb8d0e4:o.tearC,
      transparent:true,opacity:0,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    s.scale.set(0.30,0.30,1); s.position.set(x,3.55,0.30);
    s.userData.ph=i*0.5+x*3;
    fig.add(s); tears.push(s);
  });
  return {g:fig,tears:tears,tearOp:tearOp,
    update:function(t,k){ const kk=k===undefined?1:k;
      fig.update(t,kk);
      for(let i=0;i<tears.length;i++){
        const u=(t*0.30+tears[i].userData.ph)%1;
        tears[i].position.y=3.55-0.55*u;
        tears[i].material.opacity=kk*tearOp*(1-u)*(u>0.02?1:0);
      }
    }};
}

/* —— 玉门关 makeYumenGCJ(o)：汉代夯土关城（两段长墙 + 垛口 + 门洞墩台 + 残楼 + 门内幽深）
   「闻道玉门犹被遮」：门洞深黑如不许归 */
function makeYumenGCJ(o){
  o=o||{};
  const c=o.color===undefined?0x161c26:o.color;
  const H=o.h===undefined?6.4:o.h, gW=o.gW===undefined?3.6:o.gW, wallL=o.wallL===undefined?30:o.wallL;
  const segW=(wallL-gW)/2, B=new GeoBag();
  [-1,1].forEach(function(s){
    const w=new THREE.BoxGeometry(segW,H,2.2);
    w.translate(s*(gW/2+segW/2),H/2,0); B.put(w,shadeColor(c,s>0?1.0:0.93));
    const np=Math.max(2,Math.floor(segW/2.4));
    for(let i=0;i<np;i++){
      const m=new THREE.BoxGeometry(0.9,0.7,1.6);
      m.translate(s*(gW/2+1.2+2.4*i+0.5),H+0.3,0); B.put(m,shadeColor(c,1.06));
    }
    const t=new THREE.BoxGeometry(1.7,H+2.4,3.0);
    t.translate(s*(gW/2+0.85),(H+2.4)/2,0); B.put(t,shadeColor(c,1.12));
  });
  const lint=new THREE.BoxGeometry(gW+3.4,1.3,2.6); lint.translate(0,H+0.85,0); B.put(lint,shadeColor(c,1.06));
  const tower=new THREE.BoxGeometry(3.4,1.7,2.0); tower.translate(-0.6,H+2.3,0); B.put(tower,shadeColor(c,0.9));
  const troof=new THREE.BoxGeometry(4.0,0.3,2.4); troof.translate(-0.6,H+3.2,0); B.put(troof,shadeColor(c,1.0));
  const jambL=new THREE.BoxGeometry(0.5,H*0.9,3.6); jambL.translate(-gW/2-0.25,H*0.45,-1.4); B.put(jambL,shadeColor(c,0.8));
  const jambR=new THREE.BoxGeometry(0.5,H*0.9,3.6); jambR.translate(gW/2+0.25,H*0.45,-1.4); B.put(jambR,shadeColor(c,0.8));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a3444,emissive:0x05070a}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.12:o.rim,p:2.2})));
  const dark=new THREE.Mesh(new THREE.PlaneGeometry(gW,H*0.92),
    new THREE.MeshBasicMaterial({color:0x03050a}));
  dark.position.set(0,H*0.46,-1.6); g.add(dark);
  return g;
}

/* —— 荒冢断戟 makeFallenGCJ(o)：低平荒冢数座 + 折戟斜插 + 微弱冷缘光
   「年年战骨埋荒外」的冷意：克制写意，只作土冢与断杆，不画骸骨 */
function makeFallenGCJ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26511:o.seed);
  const n=o.n===undefined?6:o.n, spread=o.spread===undefined?14:o.spread, B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, z=(R()-0.5)*spread*0.8, r=0.9+R()*1.4, hh=0.35+R()*0.5;
    const m=new THREE.SphereGeometry(r,9,6,0,Math.PI*2,0,Math.PI/2);
    m.scale(1,hh/r,1); m.translate(x,0,z); B.put(m,shadeColor(0x10151d,0.9+0.3*R()));
  }
  for(let i=0;i<(o.shafts===undefined?3:o.shafts);i++){
    const x=(R()-0.5)*spread, z=(R()-0.5)*spread*0.8;
    B.put(limbGeo([x,0,z],[x+(R()-0.5)*1.2,1.5+R()*1.1,z+(R()-0.5)*1.2],0.045,0.02,4),0x1a212c);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x28313e,emissive:0x04060a}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  return g;
}

/* —— 双峰驼 makeCamelGCJ(o)：驼身/双峰/昂颈/首/四足/尾 + 驮篓蒲桃（暗紫簇 + accent 微光），合批 1 mesh
   「空见蒲桃入汉家」：篓口蒲桃成串露出，暗紫近黑，唯一点微光 */
function makeCamelGCJ(o){
  o=o||{};
  const c=o.color===undefined?0x161b23:o.color, B=new GeoBag();
  const body=new THREE.SphereGeometry(0.55,9,7);
  body.scale(1.5,0.9,0.62); body.translate(0,1.52,0); B.put(body,c);
  const h1=new THREE.SphereGeometry(0.30,7,6);
  h1.scale(1,1.05,0.8); h1.translate(-0.30,1.98,0); B.put(h1,shadeColor(c,1.06));
  const h2=new THREE.SphereGeometry(0.28,7,6);
  h2.scale(1,1.02,0.8); h2.translate(0.34,1.94,0); B.put(h2,shadeColor(c,1.02));
  B.put(limbGeo([-0.72,1.66,0],[-1.06,2.30,0],0.16,0.10,5),shadeColor(c,1.04));
  const head=new THREE.SphereGeometry(0.16,6,5);
  head.scale(1.45,0.85,0.6); head.translate(-1.22,2.42,0); B.put(head,shadeColor(c,1.1));
  const ear=new THREE.ConeGeometry(0.04,0.10,4); ear.translate(-1.12,2.58,0); B.put(ear,shadeColor(c,1.2));
  B.put(limbGeo([0.86,1.60,0],[1.10,1.02,0.04],0.05,0.025,4),shadeColor(c,0.8));
  [[-0.60,0.26],[-0.30,-0.22],[0.52,0.24],[0.82,-0.20]].forEach(function(l,i){
    B.put(limbGeo([l[0],1.30,l[1]],[l[0]+0.04,0.05,l[1]],0.075,0.04,4),shadeColor(c,0.88+0.05*i));
  });
  if(o.load!==false){
    [1,-1].forEach(function(s){
      const bk=new THREE.CylinderGeometry(0.30,0.24,0.44,7);
      bk.rotateZ(0.06*s); bk.translate(-0.10,1.86,s*0.56); B.put(bk,shadeColor(0x1c1710,1.0));
      for(let i=0;i<5;i++){
        const gr=new THREE.SphereGeometry(0.10,6,5);
        gr.translate(-0.10+(i-2)*0.075,2.10+((i%2)?0.04:0),s*0.56);
        B.put(gr,shadeColor(0x4a3c58,0.9+0.1*(i%2)));
      }
    });
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3644,emissive:0x04060a}),{c:o.rimC===undefined?0x8fa8c0:o.rimC,i:o.rim===undefined?0.14:o.rim,p:2.3})));
  const glint=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x8fa8c0,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glint.scale.set(1.5,1.1,1); glint.position.set(-0.10,2.3,0); g.add(glint);
  const glintOp0=glint.material.opacity, ph=(o.seed===undefined?26560:o.seed)%6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    glint.material.opacity=kk*glintOp0*(0.75+0.25*Math.sin(t*1.7+ph));
    g.rotation.z=0.02*Math.sin(t*1.9+ph)*kk;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 关道 makeRoadGCJ(o)：沿曲线的窄驿道（ribbon，微亮于地面）——驼队入关的路 */
function makeRoadGCJ(o){
  o=o||{};
  const pts=o.path||[[0,0]], w=o.w===undefined?2.4:o.w, n=o.n===undefined?40:o.n;
  const curve=new THREE.CatmullRomCurve3(pts.map(function(p){ return new THREE.Vector3(p[0],0,p[1]); }));
  const pos=[],idx=[];
  for(let i=0;i<=n;i++){
    const p=curve.getPoint(i/n), tn=curve.getTangent(Math.min(0.999,Math.max(0.001,i/n)));
    const nx=-tn.z, nz=tn.x;
    pos.push(p.x+nx*w/2,0.02,p.z+nz*w/2, p.x-nx*w/2,0.02,p.z-nz*w/2);
    if(i<n){ const a=i*2; idx.push(a,a+1,a+2, a+1,a+3,a+2); }
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  geo.setIndex(idx); geo.computeVertexNormals();
  const mesh=new THREE.Mesh(geo,new THREE.MeshPhongMaterial({color:0x0d1219,shininess:6,
    emissive:0x05070a,side:THREE.DoubleSide}));
  mesh.renderOrder=0;
  return mesh;
}

/* —— 驼队 makeCaravanGCJ(o)：双峰驼 ×3 + 胡人驼夫 ×2 沿曲线成列缓行
   「空见蒲桃入汉家」：点击前 visible=false 硬关；update(t,k,rev) rev 0..1 缓缓过境 */
function makeCaravanGCJ(o){
  o=o||{};
  const pts=o.path||[[-20,-86],[-18.5,-70],[-16.5,-55],[-15,-40],[-12,-26],[-8,-12],[-5,-2]];
  const curve=new THREE.CatmullRomCurve3(pts.map(function(p){ return new THREE.Vector3(p[0],0,p[1]); }));
  const g=new THREE.Group(), ents=[];
  for(let i=0;i<(o.camels===undefined?3:o.camels);i++){
    const cm=makeCamelGCJ({seed:26561+i,load:i!==0}); g.add(cm); ents.push(cm);
  }
  [0,1].forEach(function(i){
    const m=makeFigure({pose:'独立',robe:i?0x2a2520:0x1f2229,belt:0x3a3630,skin:0xc9a884,
      collar:0x3c3a42,hair:0x131216,hat:'无',noProp:true,rim:0.30,rimC:0x8fa8c0,scale:0.85});
    m.rotation.y=Math.PI; g.add(m); ents.push(m);
  });
  const gap=o.gap===undefined?0.05:o.gap;
  g.update=function(t,k,rev){ const kk=k===undefined?1:k, r=rev===undefined?0:rev;
    g.visible=kk*r>0.004;
    if(!g.visible)return;
    const head=0.94*r;
    for(let i=0;i<ents.length;i++){
      const bp=Math.max(0.002,head-i*gap);
      const p=curve.getPoint(bp), tn=curve.getTangent(Math.min(0.999,Math.max(0.002,bp)));
      ents[i].position.set(p.x,0,p.z);
      if(i<3)ents[i].rotation.y=Math.atan2(tn.z,-tn.x);
      ents[i].update(t,kk);
    }
  };
  g.userData.update=g.update;
  g.curve=curve;
  return g;
}

/* —— 荒原基底 makeSteppeGCJ(o)：荒漠地 + 低平雾山环（置于骨架常驻远山环 z≈-260…-330 之前）—— */
function makeSteppeGCJ(o){
  o=o||{};
  const g=new THREE.Group();
  const bed=makeGround({r:260,c1:o.c1===undefined?0x0a0e14:o.c1,c2:o.c2===undefined?0x121a24:o.c2,y:-0.5});
  bed.mesh.position.set(0,-0.5,-200); g.add(bed.mesh);
  const ridge=makeRange({r:250,h:o.rh===undefined?13:o.rh,layers:2,peaks:o.peaks===undefined?4:o.peaks,
    seed:o.seed===undefined?26521:o.seed,color:0x0b1017,atmo:0x232f45,fogK:0.62,glowK:0.05,
    glow:0x9fb3c9,y:-12,order:-6});
  ridge.g.position.set(0,0,o.rz===undefined?-135:o.rz); g.add(ridge.g);
  return {g:g,bed:bed,ridge:ridge};
}

function bCover(){ // 卷首 · 交河戍暮全景 —— 烽燧一点火、交河一带水、雁阵一痕远、驼道一线斜
  const g=new THREE.Group();
  const steppe=makeSteppeGCJ({seed:26521}); g.add(steppe.g);
  const river=makeRiverGCJ({rot:0.40,x:-4,z:-40,narrow:0.15}); g.add(river.mesh);
  const rise=new THREE.Mesh(new THREE.SphereGeometry(6.5,12,7,0,Math.PI*2,0,Math.PI/2),
    new THREE.MeshPhongMaterial({color:0x12181f,shininess:4,emissive:0x04060a}));
  rise.scale(1,0.22,1); rise.position.set(-40,0,-72); g.add(rise);
  const beacon=makeBeaconGCJ({h:8,rim:0.13}); beacon.position.set(-40,0.4,-72); g.add(beacon);
  const march=makeCrowd({n:8,rect:[-6,-96,34,6],seed:26531,color:0x12161e,rimC:0x8fa8c0,rim:0.13});
  g.add(march.mesh);
  const flock=makeGooseFlockGCJ({y:20,y1:26,z:-72,speed:0.012,scale:1.1,waveOp:0.10});
  g.add(flock);
  const tent=makePipaTentGCJ({r:2.4,h:2.9}); tent.position.set(27,0,-84); tent.rotation.y=-0.5; g.add(tent);
  const mist=makeMist({n:8,spread:[240,18,110],pos:[0,5,-52],scale:74,color:0x1d2634,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[160,16,70],pos:[0,9,-44],color:0x9fb2c8,size:4,speed:0.03,rise:0,add:true,maxA:0.09});
  g.add(motes.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:5,color:0x05080c,seed:26541,rim:0.12,rimC:0x8fa8c0});
  fgL.g.position.set(-13,-1.3,30); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:10,n:8,d:3,color:0x060a0e,seed:26542,sway:0.8,tip:0x3a443e,scale:0.7});
  fgR.g.position.set(12,-1.2,26); g.add(fgR.g);
  addLights(g,{c:0xa8b8cc,i:0.40,p:[-34,64,24]},{c:0x19212e,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    steppe.ridge.update(t,0); river.update(t);
    beacon.update(t,k); march.update(t); flock.update(t,k); tent.update(t,k);
    mist.update(t,k); motes.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bDengWang(){ // 壹 · 烽火饮马 —— 白日登山望烽火，黄昏饮马傍交河；行人刁斗风沙暗，公主琵琶幽怨多：
                     // 烽燧一点火、交河一带水、饮马牵马人、营前刁斗、帐前琵琶、风沙行军
  const g=new THREE.Group();
  const steppe=makeSteppeGCJ({seed:26522,rh:12}); g.add(steppe.g);
  const rise=new THREE.Mesh(new THREE.SphereGeometry(7,12,7,0,Math.PI*2,0,Math.PI/2),
    new THREE.MeshPhongMaterial({color:0x12181f,shininess:4,emissive:0x04060a}));
  rise.scale(1,0.20,1); rise.position.set(-34,0,-50); g.add(rise);
  const beacon=makeBeaconGCJ({h:8.5,rim:0.14}); beacon.position.set(-34,0.4,-50); g.add(beacon);
  const watcher=makeFigure({pose:'独立',robe:0x1d232e,belt:0x3a4456,skin:0xc9a884,collar:0x39414f,
    hair:0x14161c,hat:'幞头',rim:0.30,rimC:0x8fa8c0,noProp:true,scale:0.55});
  watcher.position.set(-30.5,1.2,-46.5); g.add(watcher);
  const river=makeRiverGCJ({rot:0.34,x:2,z:-32,narrow:0.16}); g.add(river.mesh);
  const horse=makeDrinkHorseGCJ({seed:26501}); horse.scale.setScalar(1.15);
  horse.position.set(-12,-0.02,-25.5); horse.rotation.y=2.3; g.add(horse);
  const soldier=makeFigure({pose:'独立',robe:0x1d232e,belt:0x3a4456,skin:0xc9a884,collar:0x39414f,
    hair:0x14161c,hat:'幞头',rim:0.34,rimC:0x8fa8c0,noProp:true,scale:0.78});
  soldier.position.set(-9.6,0,-23.4); soldier.rotation.y=2.7; g.add(soldier);
  const tent=makePipaTentGCJ({r:2.6,h:3.2}); tent.position.set(17,0,-46); tent.rotation.y=-0.4; g.add(tent);
  const musician=makeFigure({pose:'独立',robe:0x241f28,belt:0x403a46,skin:0xc9a884,collar:0x4a4652,
    hair:0x141317,hat:'发髻',rim:0.30,rimC:0x8fa8c0,noProp:true,scale:0.62});
  musician.position.set(14.9,0,-43.2); musician.rotation.y=-0.9; g.add(musician);
  const diao=makeDiaoDouGCJ({seed:26502}); diao.position.set(6,0,-38); diao.rotation.y=-0.5; g.add(diao);
  const march=makeCrowd({n:9,rect:[10,-64,28,5],seed:26532,color:0x11151d,rimC:0x8fa8c0,rim:0.12});
  g.add(march.mesh);
  const sand=makeFlow({n:420,box:[150,16,110],pos:[0,9,-38],color:0x3a4252,size:20,speed:4.2,maxA:0.15});
  g.add(sand.points);
  const mist=makeMist({n:8,spread:[240,18,110],pos:[0,5,-50],scale:74,color:0x1d2634,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[150,14,60],pos:[0,8,-42],color:0x9fb2c8,size:4,speed:0.03,rise:0,add:true,maxA:0.08});
  g.add(motes.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.6,w:11,d:5,color:0x05080c,seed:26543,rim:0.12,rimC:0x8fa8c0});
  fgL.g.position.set(-12,-1.3,20); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:9,n:8,d:3,color:0x060a0e,seed:26544,sway:0.9,tip:0x3a443e,scale:0.7});
  fgR.g.position.set(11,-1.2,17); g.add(fgR.g);
  addLights(g,{c:0xa2b4c8,i:0.42,p:[-32,64,24]},{c:0x1a2230,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    steppe.ridge.update(t,0); river.update(t);
    beacon.update(t,k); watcher.update(t,k); horse.update(t,k); soldier.update(t,k);
    tent.update(t,k); musician.update(t,k); diao.update(t,k); march.update(t);
    sand.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bYanLei(){ // 贰（标志性瞬间）· 胡雁哀鸣 —— 野云万里无城郭，雨雪纷纷连大漠；
                   // 胡雁哀鸣夜夜飞，胡儿眼泪双双落：雨雪旷野上雁阵掠天，胡儿仰望、泪光双双
  const g=new THREE.Group();
  const steppe=makeSteppeGCJ({seed:26523,rh:9,peaks:3,rz:-150}); g.add(steppe.g);
  const dune1=new THREE.Mesh(new THREE.SphereGeometry(10,12,7,0,Math.PI*2,0,Math.PI/2),
    new THREE.MeshPhongMaterial({color:0x10151d,shininess:4,emissive:0x04060a}));
  dune1.scale(1.7,0.14,1); dune1.position.set(-5,0,-29); g.add(dune1);
  const dune2=new THREE.Mesh(new THREE.SphereGeometry(12,12,7,0,Math.PI*2,0,Math.PI/2),
    new THREE.MeshPhongMaterial({color:0x0f141c,shininess:4,emissive:0x04060a}));
  dune2.scale(1.5,0.12,1); dune2.position.set(16,0,-40); g.add(dune2);
  const child1=makeHuChildGCJ({pose:'指月',robe:0x2b2724,scale:0.68,ph:0.0});
  child1.g.position.set(-6.8,0.72,-27.6); child1.g.rotation.y=0.25; g.add(child1.g);
  const child2=makeHuChildGCJ({pose:'独立',robe:0x242028,scale:0.64,ph:0.5});
  child2.g.position.set(-4.4,0.64,-28.6); child2.g.rotation.y=-0.15; g.add(child2.g);
  const flock=makeGooseFlockGCJ({y:22,y1:29,z:-56,speed:0.013,scale:1.7,waveOp:0.15});
  g.add(flock);
  const snow=makeGlow({n:130,box:[150,26,90],pos:[0,16,-44],color:0xbcc8d6,size:2.6,speed:0.15,rise:-0.45,add:false,maxA:0.28});
  g.add(snow.points);
  const snowA=makeGlow({n:44,box:[130,24,80],pos:[0,16,-44],color:0x9fb0c4,size:2.0,speed:0.2,rise:-0.6,add:true,maxA:0.09});
  g.add(snowA.points);
  const mist=makeMist({n:9,spread:[240,20,110],pos:[0,6,-52],scale:76,color:0x1b2432,op:0.13});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[150,14,60],pos:[0,8,-42],color:0x9fb2c8,size:4,speed:0.03,rise:0,add:true,maxA:0.07});
  g.add(motes.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.7,w:11,d:5,color:0x05080c,seed:26545,rim:0.12,rimC:0x8fa8c0});
  fgL.g.position.set(-12,-1.4,18); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:9,n:9,d:3,color:0x060a0e,seed:26546,sway:1.0,tip:0x3c4640,scale:0.72});
  fgR.g.position.set(10,-1.3,15); g.add(fgR.g);
  addLights(g,{c:0x9aaec4,i:0.38,p:[28,62,22]},{c:0x161e2c,i:0.60});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    steppe.ridge.update(t,0);
    child1.update(t,k); child2.update(t,k); flock.update(t,k);
    snow.update(t); snowA.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bPutao(){ // 叁（末境·可点击）· 蒲桃入汉 —— 闻道玉门犹被遮，应将性命逐轻车；
                  // 年年战骨埋荒外，空见蒲桃入汉家：点击——驼队驮蒲桃入关剪影缓缓过境，
                  // 与荒野战骨的冷意相对（克制写意，不画骸骨）
  const ctl={t:0,clicked:false,on:false,rev:0};
  const g=new THREE.Group();
  const steppe=makeSteppeGCJ({seed:26524,rh:12}); g.add(steppe.g);
  const path=[[-20,-86],[-18.5,-70],[-16.5,-55],[-15,-40],[-12,-26],[-8,-12],[-5,-2]];
  const gate=makeYumenGCJ({h:6.4,wallL:30}); gate.position.set(-16,0,-52); gate.rotation.y=0.30; g.add(gate);
  const road=makeRoadGCJ({path:path,w:2.6}); g.add(road);
  const watcher=makeFigure({pose:'独立',robe:0x1d232e,belt:0x3a4456,skin:0xc9a884,collar:0x39414f,
    hair:0x14161c,hat:'幞头',rim:0.34,rimC:0x8fa8c0,noProp:true,scale:0.78});
  watcher.position.set(-7.5,0,-33); watcher.rotation.y=0.35; g.add(watcher);
  const fallen1=makeFallenGCJ({seed:26511,n:7,spread:16,shafts:3}); fallen1.position.set(14,0,-40); g.add(fallen1);
  const fallen2=makeFallenGCJ({seed:26512,n:4,spread:10,shafts:2}); fallen2.position.set(24,0,-60); g.add(fallen2);
  const caravan=makeCaravanGCJ({path:path,camels:3,gap:0.05});
  caravan.visible=false; g.add(caravan);
  const cold=makeGlow({n:30,box:[120,2.5,70],pos:[6,0.9,-38],color:0x8fa8c0,size:5,speed:0.02,rise:0,add:false,maxA:0.10});
  g.add(cold.points);
  const mist=makeMist({n:8,spread:[240,18,110],pos:[0,5,-50],scale:74,color:0x1b2432,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[150,14,60],pos:[0,8,-42],color:0x9fb2c8,size:4,speed:0.03,rise:0,add:true,maxA:0.08});
  g.add(motes.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:5,color:0x05080c,seed:26547,rim:0.12,rimC:0x8fa8c0});
  fgL.g.position.set(-13,-1.4,18); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:9,n:8,d:3,color:0x060a0e,seed:26548,sway:0.9,tip:0x3c4640,scale:0.72});
  fgR.g.position.set(11,-1.3,15); g.add(fgR.g);
  addLights(g,{c:0x9fb2c8,i:0.40,p:[-28,62,24]},{c:0x18202c,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.rev=Math.min(1,ctl.rev+dt/16);
      caravan.update(t,k,ctl.rev);
      watcher.update(t,k);
      cold.update(t); mist.update(t,k); motes.update(t);
      fgL.update(t,k); fgR.update(t,k);
      steppe.ridge.update(t,0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        setAmbience(0.10);
      }
      ctl.on=true; ctl.rev=0;                    /* 可反复点：再看一回驼队入关 */
      pluck(2,0.00,0.10); pluck(3,0.62,0.09); pluck(4,1.24,0.08); pluck(5,1.90,0.08);
      pluck(4,2.60,0.07); pluck(3,3.30,0.07);
      const fl=$('#flash'); fl.textContent='年年战骨埋荒外 空见蒲桃入汉家';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x10151f),hor:C(0x1d2838),bot:C(0x0d1117),fog:C(0x111823),fd:0.0076,star:0.10,
  moon:new THREE.Vector3(48,96,-210),ms:0.30,mph:0.40,mhaze:0.14,dirC:C(0x9fb2c8),dirI:0.40,
  dirP:new THREE.Vector3(-36,66,24),ambC:C(0x19212e),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.05,build:bCover,
  cam:{f:[0,8.5,52],t:[0,8.0,46],lf:[0,4.5,-34],lt:[-2,4.6,-44]},
  sky:()=>SK({fd:0.0072,star:0.09,ms:0.30,hor:C(0x222d3e)}) },
{ name:'烽火饮马',dwell:22,river:0.06,build:bDengWang,
  cam:{f:[0,4.4,30],t:[0,3.9,25],lf:[-7,3.2,-28],lt:[-10,3.0,-42]},
  sky:()=>SK({top:C(0x111622),hor:C(0x252f40),fd:0.0074,star:0.07,ms:0.28,mhaze:0.16,
    dirC:C(0xa2b4c8),dirI:0.42,ambC:C(0x1a2230),ambI:0.64}) },
{ name:'胡雁哀鸣',dwell:24,river:0.06,build:bYanLei,
  cam:{f:[0,4.6,26],t:[0,4.2,21],lf:[0,9.5,-30],lt:[-1,11.5,-46]},
  sky:()=>SK({top:C(0x0e1320),hor:C(0x1c2636),fd:0.0080,star:0.05,ms:0.34,mph:0.44,mhaze:0.20,
    dirC:C(0x9aaec4),dirI:0.36,dirP:new THREE.Vector3(30,64,22),ambC:C(0x161e2c),ambI:0.60}) },
{ name:'蒲桃入汉',dwell:26,river:0.07,build:bPutao,
  cam:{f:[3,4.2,26],t:[1,3.8,21],lf:[-6,3.4,-28],lt:[-8,3.2,-44]},
  sky:()=>SK({top:C(0x0f1420),hor:C(0x1e2938),fd:0.0072,star:0.08,ms:0.30,mhaze:0.14,
    dirC:C(0x9fb2c8),dirI:0.40,dirP:new THREE.Vector3(-28,62,24),ambC:C(0x18202c),ambI:0.62}) },
];
"""

if __name__ == '__main__':
    print('gucongjun.py —— 被 build.py 消费：python build.py gucongjun')
