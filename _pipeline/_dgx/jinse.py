# -*- coding: utf-8 -*-
"""jinse.py —— 《锦瑟》（唐·李商隐，queue no.231，水墨夜思）生成配置
四境（N=queue stages 数）：锦瑟华年（锦瑟无端五十弦·一弦一柱思华年——瑟与弦光）、
蝶梦鹃心（庄生晓梦迷蝴蝶·望帝春心托杜鹃——晓梦之蝶+远山鹃影）、
珠泪玉烟（沧海月明珠有泪·蓝田日暖玉生烟——标志性瞬间，冷月海珠与暖山玉烟一联对切）、
追忆惘然（此情可待成追忆·只是当时已惘然——末境点击，四象叠化流转+瑟弦余音）。
水墨夜思全套色板：底色 #0d1117、雾 #111823～#131a26 系、文字 #dfe6f0，accent=#b8c4dd
（queue 分配强调色，月银微紫）只落在弦光/蝶翼/鹃啼光晕/珠光/玉烟月晕/人物边缘光/UI 上，
全页近零饱和；唯境叁蓝田一侧有一抹极克制的暖（玉烟暖白+山体暖灰+暖光晕）——
冷（沧海月明）与暖（蓝田日暖）的对切就是颈联对仗本身，也是全页唯一的暖色正用。
全诗立意「一瑟四典梦境化」：石台露台上一张锦瑟横陈（贯穿四境的母题），四典作梦境次第展开：
境壹瑟与弦光（华年）、境贰晓梦之蝶+远山鹃影（迷与托）、境叁沧海珠泪+蓝田玉烟（可望不可即）、
境肆四象隐入惘然（点击后叠化流转、瑟弦余音）。《锦瑟》是全卷最朦胧的诗——
与已有水墨夜思页第一眼可区分：不做宣室殿内夜谈（jiasheng）、不做满月江楼水天一色
（jianglou-ganjiu）、不做孤山梅影暗香（shanyuan-xiaomei）、不做古寺竹径/雨前危城/渡口渔火——
做「夜台一瑟、四典如梦」的朦胧追忆。
标志性瞬间（境叁·queue moment：沧海月明珠有泪蓝田日暖玉生烟——迷离意象）：
月明沧海在左（水上光珠点点如泪），日暖蓝田在右（玉气如烟可望不可即），一联冷暖对切同框。
末境点击（queue interact：点击追忆——四象叠化流转+瑟弦余音）：点击画面——
①蝶梦/鹃啼/珠泪/玉烟四象幻影沿远山弧次第淡现、错位流转、渐次隐入雾中（叠化）；
②瑟弦光带沿五十弦往返、光华起伏（余音可视）；③四叠下行拨弦音渐远渐杳；
④「此情可待成追忆 只是当时已惘然」题字同现——追忆未成，惘然先至。
考点钉子：瑟 sè／惘 wǎng（小测第 3 题落点）；中间两联四典庄周梦蝶/望帝啼鹃/鲛人泣珠/
蓝田玉烟（第 4 题）；主旨多元解读「悼亡/自伤/诗集自序」（第 5 题）。
多音字：惘然→往然 钉同音替换（tts.json，防「惘」误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='jinse', title='锦瑟', dyn='唐 · 李商隐', brand_author='李 商 隐',
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
        ('rgba(5,8,15', 'rgba(9,14,22', 1),
        ('rgba(4,6,11', 'rgba(8,12,19', 2),
        ('rgba(6,9,16', 'rgba(10,15,23', 1),
        ('rgba(3,5,9', 'rgba(6,9,15', 1),
        ('#0b101c', '#121a28', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
        ('0x0a1526', '0x121a26', 4),
    ],
    tip='轻点画面 / 按空格 —— 四象叠化流转，瑟弦余音',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看蝶梦鹃心珠泪玉烟四象叠化流转，听瑟弦余音',
    cover_read='锦瑟。唐，李商隐。锦瑟无端五十弦，一弦一柱思华年。庄生晓梦迷蝴蝶，望帝春心托杜鹃。沧海月明珠有泪，蓝田日暖玉生烟。此情可待成追忆，只是当时已惘然。',
    cover_p1='四重意境，随诗句次第展开：锦瑟无端五十弦，一弦一柱都惹起对华年的追思；庄生晓梦里迷了蝴蝶，望帝的春心托付给啼血的杜鹃；沧海月明之下鲛人泣泪成珠，蓝田日暖之中良玉升起轻烟；此情哪里是等到今日追忆才觉怅惘——当时身历之际，便已惘然。',
    cover_p2='边读诗，边跟着李商隐坐在这张锦瑟前：全诗最朦胧，也最深情——读懂「一弦一柱思华年」的无端之思与「惘然」的回望，就读懂了这首千古朦胧诗的绝唱。',
    end_h2='曲终 · 惘然', cn_word='四',
    words_js="['再抚一次锦瑟','初识义山，尚需共读','渐入诗境，再诵几遍','一弦一柱，华年可思','已解四典朦胧之意','曲终惘然，追忆成诗']",
    sky_atmo='0x202a3a',
)

POEM_JS = """const POEM = [
{ name:'锦瑟华年', jing:'锦瑟呀，你为什么无端地有五十根弦？一弦一柱，都惹人追忆那似水的华年 —— 无端、一弦一柱、思华年。（锦瑟 · 五十弦 · 华年）',
  segs:[
   {c:'锦瑟无端五十弦，', p:py('jǐn sè wú duān wǔ shí xián')},
   {c:'一弦一柱思华年。', p:py('yī xián yī zhù sī huá nián')}],
  read:'锦瑟无端五十弦，一弦一柱思华年。',
  yisi:'锦瑟呀，你为什么无缘无故有五十根弦？每一根弦、每一个柱，都惹人追念那逝去的美好年华。——起联以锦瑟起兴：瑟本二十五弦，诗人偏说「五十弦」，是过数之辞，不管它合不合数——「无端」二字埋怨得没来由，正是有情人才说得出的话：物本无情，人自多恨。瑟弦繁多，恰似纷繁往事；一抚一按之间，「一弦一柱」都是年华的刻度。这两句也可理解为诗人以瑟自况：弦弦掩抑，声声清怨，正是自己诗歌一生的写照。',
  zhu:[['锦瑟','瑟面织有锦纹的宝瑟，装饰华美的瑟——弦乐器，相传古瑟本有五十弦'],['无端','无缘无故，没来由——埋怨之词：瑟弦多本是常事，诗人却怪它「无端」，无理而妙'],['五十弦','古制瑟为五十弦，后世改为二十五弦——此处极言弦多，亦有「断弦」之痛的影子'],['一弦一柱','每一根弦、每一个支弦的码子（柱）——弦柱之繁，正如往事之繁'],['思华年','追忆美好的年华。思，追念；华年，青春年华、一生中最美的岁月'],['起兴','先言他物以引起所咏之词——以锦瑟发端，引出「思华年」的主旨']] },
{ name:'蝶梦鹃心', jing:'庄周晓梦，醒来分不清是自己梦见了蝴蝶，还是蝴蝶梦见了自己；望帝的春心，托付给杜鹃的声声啼血 —— 晓梦、迷蝴蝶、托杜鹃。（庄生梦蝶 · 望帝啼鹃）',
  segs:[
   {c:'庄生晓梦迷蝴蝶，', p:py('zhuāng shēng xiǎo mèng mí hú dié')},
   {c:'望帝春心托杜鹃。', p:py('wàng dì chūn xīn tuō dù juān')}],
  read:'庄生晓梦迷蝴蝶，望帝春心托杜鹃。',
  yisi:'庄周梦见自己化为蝴蝶，翩翩然欣然自得——醒来才知身是庄周，却再也分不清：是庄周梦里成了蝴蝶，还是蝴蝶梦里成了庄周？望帝禅位之后国亡身死，魂化杜鹃，暮春啼叫，声声悲切，以至于啼血——满腔春心，尽托付在这鸟鸣里。——颔联连用两典，都写「失去」与「迷惘」：庄生梦蝶，是美好境界的痴迷与幻灭；望帝托鹃，是未了心愿的死而不已。一「迷」一「托」，把华年往事写成一片真幻交织、生死相续的迷离。',
  zhu:[['庄生晓梦迷蝴蝶','用《庄子·齐物论》典故：庄周梦为蝴蝶，「栩栩然蝴蝶也」；俄然觉，则蘧蘧然周也——不知周之梦为蝴蝶与，蝴蝶之梦为周与'],['庄生','即庄周，战国时宋国蒙人，道家学派代表人物'],['望帝春心托杜鹃','用蜀王杜宇典故：望帝号杜宇，禅位（一说国亡）之后，魂化杜鹃，暮春而啼，声声泣血'],['春心','伤春之心、惜春之情——此处兼指对美好事物的眷恋与追求'],['托','寄托、托付——身可死而心不死，一腔深情托之啼鸟']] },
{ name:'珠泪玉烟', jing:'大海月明之夜，鲛人的泪水化作明珠；蓝田日暖之时，良玉升起丝丝轻烟，远望可见、近观即无 —— 月明、珠有泪、日暖、玉生烟。（沧海珠泪 · 蓝田玉烟）（标志性瞬间）',
  segs:[
   {c:'沧海月明珠有泪，', p:py('cāng hǎi yuè míng zhū yǒu lèi')},
   {c:'蓝田日暖玉生烟。', p:py('lán tián rì nuǎn yù shēng yān')}],
  read:'沧海月明珠有泪，蓝田日暖玉生烟。',
  yisi:'南海外有鲛人，水居如鱼，其眼能泣泪成珠——月明沧海，珠光与泪光，一片晶莹而凄清；蓝田山产美玉，相传日暖之时，玉气升腾为烟，远而望之依稀可见，近前即寻不着——美好的东西，远远望得见一缕影，走近了却永远把握不住。——颈联一冷一暖、一海一山、一月一日，对仗工绝而境界迷离：珠有泪，是至美之物含着至深之痛；玉生烟，是至美之境可望而不可即。诗人一生所珍视的一切——才情、情事、理想——都像这月下珠泪、日中玉烟：确凿地存在过，又永远无法把握。',
  zhu:[['沧海月明珠有泪','用鲛人典故：《博物志》载「南海外有鲛人，水居如鱼，不废织绩，其眼能泣珠」——又有鲛人对月而泣、其泪成珠之说'],['蓝田日暖玉生烟','蓝田，山名，在今陕西，产美玉，又称玉山；相传日光和暖时宝玉之气升腾如烟，远可见而近即无——司空图引戴叔伦语：「诗家之景，如蓝田日暖，良玉生烟，可望而不可置于眉睫之前也」'],['珠有泪','珠光莹然如泪光，泪凝为珠——至美与至痛合为一体'],['可望而不可即','远远望得见，却无法靠近、无法把握——颈联迷离境界共同的感觉指向']] },
{ name:'追忆惘然', jing:'这份深情，哪里是等到今日追忆时才觉怅惘？就在当时身历之际，便已经是一片迷惘 —— 可待、追忆、惘然。（追忆 · 惘然）（末境点击画面：蝶梦鹃心珠泪玉烟四象叠化流转，瑟弦余音）',
  segs:[
   {c:'此情可待成追忆，', p:py('cǐ qíng kě dài chéng zhuī yì')},
   {c:'只是当时已惘然。', p:py('zhǐ shì dāng shí yǐ wǎng rán')}],
  read:'此情可待成追忆，只是当时已惘然。',
  yisi:'这份深情，难道是等到今天追忆起来，才感到无限怅惘吗？——不，就在当时身历其境的时候，便已经令人迷惘失意了。——尾联用反问把时间推回去一层：「可待」即「岂待」——不是事过境迁才惘然，身在其中时便已惘然：华年的美好，当事人当时就抓住了、也留不住。全诗到此收束于一片怅惘：锦瑟余音里，四象朦胧如梦，追忆未成而惘然先至。此诗历来多解：悼亡妻王氏者有之，自伤身世者有之，以为诗集自序者有之——正因四典朦胧，才容得下万种心事；而「思华年」的深情与「惘然」的怅惘，是所有解读共同的底色。',
  zhu:[['此情','统指中间两联所写的种种情事与情境'],['可待','岂待、哪等到——反诘之词'],['惘然','怅然若失、迷惘不知所从的样子。惘，读 wǎng'],['一篇《锦瑟》解人难','此诗主旨历来聚讼：悼亡说（悼念亡妻王氏）、自伤身世说（才志不遇、一生坎坷）、诗集自序说（以瑟起兴总领平生诗作）——诸说并存，正成其「朦胧诗绝唱」的地位']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「锦瑟无端五十弦」的下一句是？', o:['一弦一柱思华年','庄生晓梦迷蝴蝶','望帝春心托杜鹃'], a:0},
 {q:'「沧海月明珠有泪」的下一句是？', o:['此情可待成追忆','蓝田日暖玉生烟','只是当时已惘然'], a:1},
 {q:'「锦瑟无端五十弦」的「瑟」与「只是当时已惘然」的「惘」，读音都正确的一项是？', o:['瑟读 sè，弦乐器；惘读 wǎng，怅然若失、失神迷茫的样子','瑟读 bì，是「璱」的通假字，指玉的光彩；惘读 máng，与「盲」同源','瑟读 ruò，古入声字；惘读 wǎng，兴旺兴盛的样子'], a:0},
 {q:'中间两联「庄生晓梦迷蝴蝶，望帝春心托杜鹃。沧海月明珠有泪，蓝田日暖玉生烟」连用四个典故，下列说法正确的是？', o:['庄周梦蝶（人生如梦、真幻难分）、望帝啼鹃（春心哀托、啼血之怨）、鲛人泣珠（泪化为珠）、蓝田玉烟（美好可望而不可即）——四个朦胧典故层层叠出怅惘','分别是女娲补天、精卫填海、湘妃泣竹、吴刚伐桂——写四个神话传说里的坚持与不屈','都是写实：写诗人清晨看见蝴蝶、听见杜鹃、傍晚海边采珠、夜里山中烧玉的四段见闻'], a:0},
 {q:'对这首诗主旨的理解，下列说法最恰当的一项是？', o:['历来有多元解读：悼亡说、自伤身世说、诗集自序说……中间两联四典朦胧，正因「朦胧」而容许多解；但无论何解，「一弦一柱思华年」的追思与「惘然」的怅惘是共同底色','此诗是李商隐为一张新制五十弦瑟写的咏物说明诗，目的在介绍这种乐器的构造与形制','此诗记录诗人夜半被邻家瑟声吵醒的恼怒，中间两联是抱怨瑟声扰人清梦'], a:0},
];
"""

SCENES_JS = """/* ================= 锦瑟 · 四境场景（水墨夜思·一瑟四典梦境化：锦瑟华年、蝶梦鹃心、珠泪玉烟、追忆惘然） =================
   美术立意：水墨夜思色板写「夜台一瑟、四典如梦」——底色 #0d1117、雾 #111823～#131a26 系，
   accent=#b8c4dd（月银微紫）只落在弦光/蝶翼/鹃啼光晕/珠光/玉烟月晕/边缘光/UI 上，全页近零饱和；
   唯境叁蓝田一侧一抹极克制的暖（玉烟暖白 0xd8c8a8+山体暖灰+暖光晕 0xc9a878）——
   冷（沧海月明）与暖（蓝田日暖）的对切就是颈联对仗本身。
   母题贯穿：石台露台上一张锦瑟横陈（细线弦阵+弦光），四境同在、视角与远景随诗推进：
   境壹=瑟与弦光（华年）；境贰=晓梦之蝶绕瑟+远山鹃影啼晕（迷与托）；
   境叁（标志性瞬间）=月明沧海光珠（左·冷）与日暖蓝田玉烟（右·暖）一联对切同框；
   境肆（末境可点击）=四象隐入惘然：点击——蝶/鹃/珠/玉四象幻影沿远山弧叠化流转+瑟弦余音光带。
   与已有水墨夜思页第一眼可区分：不做宣室殿内夜谈（jiasheng）、不做满月江楼水天一色
   （jianglou-ganjiu）、不做孤山梅影暗香（shanyuan-xiaomei）、不做古寺竹径（ti-poshansi）、
   不做雨前危城（xianyang-chenglou）、不做渡口斜月渔火（ti-jinlingdu）。 */

/* —— 石台露台 makeTerraceJS(o)：台基+地坪+前阶+沿边矮栏望柱（合批 1 mesh）——
   「夜台」本体：一张瑟与一炉香所在的露台，矮栏之外即是梦境展开处 */
function makeTerraceJS(o){
  o=o||{};
  const B=new GeoBag();
  const tai=new THREE.BoxGeometry(34,1.4,22);
  tai.translate(0,0.70,3); B.put(tai,0x161d29);
  const fl=new THREE.BoxGeometry(32,0.22,20);
  fl.translate(0,1.44,3); B.put(fl,0x1c2534);
  for(let i=0;i<3;i++){
    const st=new THREE.BoxGeometry(8.5-i*1.2,0.40,1.35);
    st.translate(0,1.20-i*0.40,14.7+i*0.70); B.put(st,shadeColor(0x151d29,0.92+i*0.10));
  }
  const wF=new THREE.BoxGeometry(34,0.50,0.35);
  wF.translate(0,1.80,-8); B.put(wF,0x1a2330);
  const capF=new THREE.BoxGeometry(34.6,0.12,0.55);
  capF.translate(0,2.12,-8); B.put(capF,0x232f42);
  for(let i=0;i<9;i++){
    const p=new THREE.BoxGeometry(0.30,0.78,0.30);
    p.translate(-17+i*4.25,1.94,-8); B.put(p,0x202b3c);
  }
  for(let s=-1;s<=1;s+=2){
    const wS=new THREE.BoxGeometry(0.35,0.50,6.5);
    wS.translate(s*16.8,1.80,-4.6); B.put(wS,0x1a2330);
    const capS=new THREE.BoxGeometry(0.55,0.12,7.1);
    capS.translate(s*16.8,2.12,-4.6); B.put(capS,0x232f42);
    const pS=new THREE.BoxGeometry(0.30,0.78,0.30);
    pS.translate(s*16.8,1.94,-8); B.put(pS,0x202b3c);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x36445c,emissive:0x05070c}),{c:0xb8c4dd,i:o.rim===undefined?0.12:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 锦瑟 makeSeJS(o)：瑟首/瑟尾/琴身+五十弦细线阵（1 LineSegments）+一弦一柱斜列
   （并入本体合批）+尾端三瑟枘+弦光 Sprite（fog:false 加色；初值=峰值——fadeK 铁律，
   update 里包络 ≤1）——「锦瑟」本体：update(t,k,ex) 的 ex（0..1）即「瑟弦余音」：
   点击后弦光沿弦往返、光华起伏（增幅全在初值以内） */
function makeSeJS(o){
  o=o||{};
  const L=o.L===undefined?3.2:o.L, W=o.W===undefined?1.0:o.W;
  const n=o.strings===undefined?50:o.strings;
  const glowOp=o.glowOp===undefined?0.10:o.glowOp;
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(L,0.16,W);
  body.translate(0,0.08,0); B.put(body,0x231a15);
  const top=new THREE.BoxGeometry(L*0.96,0.045,W*0.92);
  top.translate(0,0.182,0); B.put(top,shadeColor(0x231a15,1.35));
  const head=new THREE.BoxGeometry(0.24,0.30,W*1.04);
  head.translate(-L*0.5-0.06,0.15,0); B.put(head,0x2a1e17);
  const tail=new THREE.BoxGeometry(0.20,0.24,W*1.02);
  tail.translate(L*0.5+0.03,0.12,0); B.put(tail,0x281c15);
  [[-L*0.32,W*0.30],[L*0.30,W*0.30],[-L*0.32,-W*0.30],[L*0.30,-W*0.30]].forEach(function(q){
    const ft=new THREE.BoxGeometry(0.10,0.16,0.10);
    ft.translate(q[0],-0.07,q[1]); B.put(ft,0x1c140f);
  });
  for(let i=0;i<n;i++){
    const z=(i/(n-1)-0.5)*W*0.72;
    const x=-L*0.30+(i/(n-1))*L*0.60;
    const br=new THREE.BoxGeometry(0.045,0.075,0.028);
    br.translate(x,0.205,z); B.put(br,0x6a5c40);
  }
  for(let i=0;i<3;i++){
    const r=new THREE.SphereGeometry(0.05,6,5);
    r.translate(-L*0.5-0.22,0.16,(i-1)*0.22); B.put(r,0x6a5c40);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x4a4038,emissive:0x080503}),{c:0xb8c4dd,i:o.rim===undefined?0.16:o.rim,p:2.6})));
  /* 五十弦：细线阵（1 draw call） */
  const pos=new Float32Array(n*6), y0=0.24, x0=-L*0.46, x1=L*0.44;
  for(let i=0;i<n;i++){
    const z=(i/(n-1)-0.5)*W*0.72;
    pos[i*6]=x0; pos[i*6+1]=y0; pos[i*6+2]=z;
    pos[i*6+3]=x1; pos[i*6+4]=y0; pos[i*6+5]=z;
  }
  const sg=new THREE.BufferGeometry();
  sg.setAttribute('position',new THREE.BufferAttribute(pos,3));
  const lines=new THREE.LineSegments(sg,
    new THREE.LineBasicMaterial({color:0x8b9cbb,transparent:true,opacity:0.5}));
  lines.renderOrder=1; g.add(lines);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8c4dd,
    transparent:true,opacity:glowOp,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(L*1.15,0.72,1); glow.position.set(0,y0+0.06,0); glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?23101:o.seed)%6.283;
  g.update=function(t,k,ex){
    const kk=k===undefined?1:k, e=ex===undefined?0:ex;
    const sweep=Math.sin(t*(0.5+1.6*e)+ph);
    glow.position.x=sweep*L*0.16*(1+1.4*e);
    glow.material.opacity=kk*glowOp*(0.55+0.15*Math.sin(t*0.8+ph)+0.30*e);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 香炉 makeCenserJS(o)：三足双耳铜香炉（合批 1 mesh）+一缕冷香（makeGlow 细柱缓升）
   ——「思华年」的香事：炉冷香微，思亦如缕 */
function makeCenserJS(o){
  o=o||{};
  const B=new GeoBag();
  const bd=new THREE.SphereGeometry(0.30,10,8);
  bd.scale(1,0.78,1); bd.translate(0,0.30,0); B.put(bd,0x39404c);
  const mouth=new THREE.CylinderGeometry(0.16,0.19,0.10,10);
  mouth.translate(0,0.56,0); B.put(mouth,shadeColor(0x39404c,1.18));
  const lid=new THREE.SphereGeometry(0.17,9,7);
  lid.scale(1,0.55,1); lid.translate(0,0.62,0); B.put(lid,shadeColor(0x39404c,0.92));
  for(let i=0;i<3;i++){
    const a=i/3*6.283+0.5;
    const lg=new THREE.CylinderGeometry(0.035,0.05,0.16,6);
    lg.translate(Math.sin(a)*0.20,0.07,Math.cos(a)*0.20); B.put(lg,shadeColor(0x39404c,0.8));
  }
  [1,-1].forEach(function(sd){
    const ear=new THREE.TorusGeometry(0.075,0.018,5,10,Math.PI);
    ear.translate(sd*0.30,0.42,0); B.put(ear,shadeColor(0x39404c,1.1));
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:24,
    specular:0x5a6272,emissive:0x07090d}),{c:0xb8c4dd,i:0.20,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const smoke=makeGlow({n:o.smokeN===undefined?14:o.smokeN,box:[0.36,5.5,0.36],pos:[0,0.74,0],
    color:o.smokeC===undefined?0x8fa3b8:o.smokeC,size:2.6,speed:0.035,rise:1,add:false,maxA:0.15});
  smoke.points.renderOrder=3; g.add(smoke.points);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    smoke.update(t);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 晓梦之蝶 makeButterfliesJS(o)：半透明蝶影（双翅=两片合八字的小翼，InstancedMesh
   1 draw call；scale.x 摆动即扇翅；update(t,k,env) 的 env 供末境幻影淡入淡出用） */
function makeButterfliesJS(o){
  o=o||{};
  const n=o.n===undefined?7:o.n;
  const area=o.area===undefined?{c:[0,4.4,3.5],r:[11,2.6,9]}:o.area;
  const op0=o.op===undefined?0.52:o.op;
  const g=new THREE.Group();
  const R=seedRnd(o.seed===undefined?23102:o.seed);
  const B=new GeoBag();
  /* 双翅：两只压扁的横锥（泪滴翅形，尖朝外），微八字上翘——远比矩形片更像蝶翅 */
  [1,-1].forEach(function(s){
    const w=new THREE.ConeGeometry(0.15,0.42,5);
    w.rotateZ(s*-1.5708);
    w.scale(1,1,0.16);
    w.translate(s*0.20,0,0);
    w.rotateX(s*0.25);
    B.put(w,0xffffff);
  });
  const mesh=new THREE.InstancedMesh(mergeGeos(B.list),
    new THREE.MeshBasicMaterial({color:o.color===undefined?0xaebcd4:o.color,
      transparent:true,opacity:op0,depthWrite:false,side:THREE.DoubleSide}),n);
  mesh.frustumCulled=false; mesh.renderOrder=3;
  const items=[];
  const sMin=o.sMin===undefined?0.30:o.sMin, sMax=o.sMax===undefined?0.65:o.sMax;
  for(let i=0;i<n;i++){
    items.push({x:area.c[0]+(R()-0.5)*area.r[0], y:area.c[1]+(R()-0.5)*area.r[1], z:area.c[2]+(R()-0.5)*area.r[2],
      ph:R()*6.283, sp:0.5+R()*0.8, sc:sMin+R()*(sMax-sMin), rx:2.0+R()*3.0, flap:4.5+R()*3.5});
  }
  const dm=new THREE.Object3D();
  g.add(mesh);
  g.update=function(t,k,env){
    const kk=k===undefined?1:k, e=env===undefined?1:env;
    for(let i=0;i<n;i++){
      const it=items[i], a=t*it.sp+it.ph;
      dm.position.set(it.x+Math.sin(a)*it.rx, it.y+Math.sin(a*1.7)*0.55, it.z+Math.cos(a*0.83)*it.rx*0.7);
      dm.rotation.set(Math.sin(a*1.3)*0.2, a*0.35, 0);
      dm.scale.set(it.sc*(Math.abs(Math.sin(t*it.flap+it.ph))*0.75+0.25), it.sc, it.sc);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mesh.material.opacity=kk*op0*e;
    g.visible=kk*e>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 杜鹃 makeBirdJS(o)：远山鸟影（合批 1 mesh：体/颈/首/喙/尾/足）+啼光晕 Sprite
   （初值=峰值；包络每约 4 秒一次啼鸣尖峰——「望帝春心托杜鹃」的声光点） */
function makeBirdJS(o){
  o=o||{};
  const c=o.color===undefined?0x0e141f:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.34,9,7);
  body.scale(1.65,0.95,0.85); body.translate(0,0.52,0); B.put(body,c);
  const neck=new THREE.CylinderGeometry(0.09,0.14,0.5,7);
  neck.rotateZ(-0.55); neck.translate(0.56,1.02,0); B.put(neck,shadeColor(c,1.1));
  const head=new THREE.SphereGeometry(0.16,8,6);
  head.translate(0.76,1.24,0); B.put(head,shadeColor(c,1.12));
  const beak=new THREE.ConeGeometry(0.05,0.24,6);
  beak.rotateZ(-Math.PI/2); beak.translate(1.0,1.20,0); B.put(beak,0x5a5244);
  const tail=new THREE.ConeGeometry(0.13,0.85,6);
  tail.rotateZ(1.35); tail.translate(-0.66,0.44,0); B.put(tail,shadeColor(c,0.85));
  for(let i=0;i<2;i++){
    const leg=new THREE.CylinderGeometry(0.028,0.024,0.34,5);
    leg.translate(0.05+i*0.09,0.17,0); B.put(leg,0x4a4238);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x303c50,emissive:0x05070b}),{c:0xb8c4dd,i:o.rim===undefined?0.24:o.rim,p:2.6})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const pulse=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.pulseC===undefined?0xb8c4dd:o.pulseC,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  pulse.scale.set(2.6,2.6,1); pulse.position.set(0.85,1.25,0); pulse.renderOrder=4; g.add(pulse);
  const ph=(o.seed===undefined?23103:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.03*Math.sin(t*0.5+ph)*kk;
    const cry=Math.pow(Math.max(0,Math.sin(t*0.8+ph)),10);
    pulse.material.opacity=kk*0.30*cry;
    pulse.scale.setScalar(1.6+2.2*cry);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 沧海珠泪 makePearlsJS(o)：月下海面光珠（InstancedMesh 小珠缓沉浮 1 draw call）
   +珠光点点（makeGlow 冷色微粒）——「珠有泪」：至美之物含着至深之痛 */
function makePearlsJS(o){
  o=o||{};
  const n=o.n===undefined?7:o.n;
  const area=o.area===undefined?{c:[-36,2.6,-58],r:[30,2.4,20]}:o.area;
  const op0=o.op===undefined?0.85:o.op;
  const g=new THREE.Group(), R=seedRnd(o.seed===undefined?23104:o.seed);
  const mesh=new THREE.InstancedMesh(new THREE.SphereGeometry(0.55,8,6),
    new THREE.MeshBasicMaterial({color:o.color===undefined?0xdde6f4:o.color,
      transparent:true,opacity:op0,depthWrite:false}),n);
  mesh.frustumCulled=false; mesh.renderOrder=2;
  const items=[];
  for(let i=0;i<n;i++){
    items.push({x:area.c[0]+(R()-0.5)*area.r[0], y:area.c[1]+(R()-0.5)*area.r[1], z:area.c[2]+(R()-0.5)*area.r[2],
      ph:R()*6.283, sc:0.9+R()*0.9});
  }
  const dm=new THREE.Object3D(); g.add(mesh);
  const glint=makeGlow({n:o.glintN===undefined?24:o.glintN,box:[area.r[0]*1.1,area.r[1]*1.4,area.r[2]*1.1],
    pos:[area.c[0],area.c[1],area.c[2]],color:o.glintC===undefined?0xbccadd:o.glintC,
    size:3.4,speed:0.03,rise:0.5,add:true,maxA:0.18});
  glint.points.renderOrder=3; g.add(glint.points);
  g.update=function(t,k,env){
    const kk=k===undefined?1:k, e=env===undefined?1:env;
    for(let i=0;i<n;i++){
      const it=items[i];
      dm.position.set(it.x,it.y+Math.sin(t*0.5+it.ph)*0.6,it.z);
      dm.rotation.set(0,it.ph+t*0.2,0);
      dm.scale.setScalar(it.sc*(0.9+0.1*Math.sin(t*0.9+it.ph)));
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mesh.material.opacity=kk*op0*e;
    glint.update(t);
    g.visible=kk*e>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 蓝田玉烟 makeYuYanJS(o)：日暖玉山头升起的玉气（makeGlow 暖白缓升+暖光晕 Sprite
   fog:false；初值=峰值）——「玉生烟」：可望而不可置眉睫之前 */
function makeYuYanJS(o){
  o=o||{};
  const pos=o.pos===undefined?[38,6,-92]:o.pos;
  const g=new THREE.Group();
  const smoke=makeGlow({n:o.n===undefined?26:o.n,box:o.box===undefined?[34,24,14]:o.box,pos:pos,
    color:o.color===undefined?0xd8c8a8:o.color,size:o.size===undefined?5.5:o.size,
    speed:0.05,rise:0.9,add:true,maxA:0.13});
  smoke.points.renderOrder=3; g.add(smoke.points);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc9a878,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(60,26,1); glow.position.set(pos[0],pos[1]-2,pos[2]); glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?23105:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    smoke.update(t);
    glow.material.opacity=kk*0.10*(0.80+0.20*Math.sin(t*0.3+ph));
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 四象幻影 makeSiyuanJS(o)：末境点击的四典虚象（蝶梦/鹃啼/珠泪/玉烟），沿远山弧排布；
   组 visible=false 硬关——点击前无幻影；update(t,k,rv)：
   rv 0→1 次第淡现（相位错开）→错位流转（叠化）→渐次隐入雾中——「四象叠化流转」 */
function makeSiyuanJS(o){
  o=o||{};
  const g=new THREE.Group(), phantoms=[];
  const sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  const ridge=makeRange({r:64,h:8,layers:2,peaks:3,seed:23131,color:0x0b111b,atmo:0x202a3a,
    fogK:0.60,glowK:0.05,glow:0xaebccd,y:-4,order:-4});
  ridge.g.position.set(0,0,-62); ridge.g.visible=false; g.add(ridge.g);
  function addPhantom(fn,ph){
    const sub=new THREE.Group(); const up=fn(sub);
    sub.visible=false; g.add(sub); phantoms.push({sub:sub,up:up,ph:ph});
  }
  addPhantom(function(sub){                     /* ① 蝶梦 */
    const die=makeButterfliesJS({n:6,area:{c:[-15,5.4,-30],r:[11,2.4,4]},seed:23132,
      op:0.70,sMin:0.60,sMax:1.05});
    sub.add(die);
    return function(t,k,env){ die.update(t,k,env); };
  },0.00);
  addPhantom(function(sub){                     /* ② 鹃啼（孤岩鸟影） */
    const rock=new THREE.ConeGeometry(1.7,4.4,5);
    rock.translate(0,2.2,0);
    const rm=new THREE.Mesh(rock,new THREE.MeshPhongMaterial({color:0x0d131d,
      emissive:0x05070b,shininess:6,specular:0x303c50}));
    rm.position.set(7,1.2,-33); sub.add(rm);
    const bird=makeBirdJS({scale:1.8,seed:23133});
    bird.g.position.set(7,3.4,-33); bird.g.rotation.y=-0.35; sub.add(bird.g);
    return function(t,k,env){ bird.update(t,k); };
  },0.25);
  addPhantom(function(sub){                     /* ③ 珠泪 */
    const pear=makePearlsJS({n:5,area:{c:[-8,4.2,-32],r:[10,2.2,6]},seed:23134,glintN:16,op:0.9});
    sub.add(pear);
    const yue=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:0xdfe8f4,
      transparent:true,opacity:0.65,depthWrite:false,fog:false}));
    yue.scale.set(7,7,1); yue.position.set(-8,8.4,-32); yue.renderOrder=2; sub.add(yue);
    return function(t,k,env){ pear.update(t,k,env); yue.material.opacity=0.65*env*k; };
  },0.50);
  addPhantom(function(sub){                     /* ④ 玉烟 */
    const hill=makeRange({r:26,h:5,layers:2,peaks:3,seed:23135,color:0x12161e,atmo:0x202a3a,
      fogK:0.60,glowK:0.05,glow:0xaebccd,y:1,order:-3});
    hill.g.position.set(19,0,-36); sub.add(hill.g);
    const yan=makeYuYanJS({pos:[19,4.5,-34],n:20,box:[14,14,8],size:4.5});
    sub.add(yan);
    return function(t,k,env){ yan.update(t,k); hill.update(t,0); };
  },0.75);
  g.position.y=1.2;
  g.visible=false;
  return {g:g,update:function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const any=kk*r>0.004;
    ridge.update(t,0); ridge.g.visible=any;
    for(let i=0;i<phantoms.length;i++){
      const p=phantoms[i];
      const appear=sm01((r-p.ph*0.55-0.06)/0.20);
      const fade=1-sm01((r-0.66-p.ph*0.10)/0.26);
      const env=Math.min(appear,fade);
      p.sub.position.x=Math.sin(r*6.283+p.ph*2.2)*3.2*(0.4+0.6*sm01(r/0.3));
      p.sub.visible=any&&env>0.004;
      p.up(t,kk,env);
    }
    g.visible=any;
  }};
}

/* 诗人：全诗贯穿的同一造型（青灰微紫袍、幞头；每次 build 新建材质） */
function jsPoet(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2b3346,belt:0x6f7d92,skin:0xd3b294,collar:0x9aa6b8,
    hair:0x12161e,hat:'幞头',rimC:0xb8c4dd,rim:0.42,noProp:true,scale:scale===undefined?1.55:scale});
}

/* 远山一环 makeYaoyuanJS(o)：夜色深处的低平远山（两层，带雾骨相）——梦境展开的天际；
   组放近（z≈-150 以上），不被骨架常驻远山环（z≈-300）遮挡 */
function makeYaoyuanJS(o){
  o=o||{};
  return makeRange({r:o.r===undefined?230:o.r,h:o.h===undefined?12:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?23121:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x202a3a,
    fogK:o.fogK===undefined?0.60:o.fogK,glowK:0.05,glow:0xaebccd,
    y:o.y===undefined?-10:o.y,order:-6});
}

function bCover(){ // 卷首 · 夜台一瑟：石台露台锦瑟横陈，一炉冷香，诗人独立夜色，远山环合
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0e16,c2:0x141b28,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeYaoyuanJS({r:250,h:13,seed:23122}); yuan.g.position.set(0,0,-165); g.add(yuan.g);
  const terr=makeTerraceJS({}); g.add(terr);
  const an=makeTable({w:3.7,d:1.25,h:0.82,wood:0x231a14}); an.g.position.set(0.8,1.55,3.2); g.add(an.g);
  const se=makeSeJS({seed:23101}); se.g.position.set(0.8,2.37,3.2); g.add(se.g);
  const jj=makeTable({w:1.15,d:1.15,h:0.70,wood:0x211812}); jj.g.position.set(-5.4,1.55,1.8); g.add(jj.g);
  const censer=makeCenserJS({}); censer.g.position.set(-5.4,2.25,1.8); g.add(censer.g);
  const poet=jsPoet(1.55,'独立'); poet.position.set(6.2,1.55,4.5); poet.rotation.y=-0.75; g.add(poet);
  const mist=makeMist({n:5,spread:[130,10,56],pos:[0,3.2,-16],scale:44,color:0x2a3648,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[90,14,44],pos:[0,8,0],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x05080e,seed:23123,rim:0.10,rimC:0xb8c4dd});
  fg1.g.position.set(-13,-1.6,21); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x05080e,seed:23124,sway:0.6,rim:0.08,rimC:0xb8c4dd});
  fg2.g.position.set(13.5,-1.8,20); g.add(fg2.g);
  addLights(g,{c:0xa8bad0,i:0.30,p:[-40,55,-40]},{c:0x1b2433,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    se.update(t,k); censer.update(t,k);
    poet.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bHuonian(){ // 壹 · 锦瑟华年 —— 锦瑟无端五十弦，一弦一柱思华年：
                     // 俯临瑟面，五十弦细线阵与弦光微漾，香缕如思——人不入画，空席待思
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0e16,c2:0x151c29,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeYaoyuanJS({seed:23125}); yuan.g.position.set(70,0,-120); g.add(yuan.g);
  const terr=makeTerraceJS({}); g.add(terr);
  const an=makeTable({w:3.7,d:1.25,h:0.82,wood:0x231a14}); an.g.position.set(0.8,1.55,3.2); g.add(an.g);
  const se=makeSeJS({seed:23101,glowOp:0.13}); se.g.position.set(0.8,2.37,3.2); g.add(se.g);
  const jj=makeTable({w:1.15,d:1.15,h:0.70,wood:0x211812}); jj.g.position.set(-5.4,1.55,1.8); g.add(jj.g);
  const censer=makeCenserJS({}); censer.g.position.set(-5.4,2.25,1.8); g.add(censer.g);
  const mist=makeMist({n:5,spread:[130,10,54],pos:[0,3.4,-14],scale:44,color:0x2a3648,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[86,13,42],pos:[0,8,2],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x05080e,seed:23126,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(-11.5,-1.5,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:24,h:3.0,color:0x05080e,seed:23127,rim:0.08,rimC:0xb8c4dd});
  fg2.g.position.set(2,-3.1,16.5); g.add(fg2.g);
  addLights(g,{c:0xa6b6cc,i:0.30,p:[-40,50,-40]},{c:0x1a2331,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    se.update(t,k); censer.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bDiemeng(){ // 贰 · 蝶梦鹃心 —— 庄生晓梦迷蝴蝶，望帝春心托杜鹃：
                     // 诗人正坐瑟后，晓梦之蝶半透绕瑟而舞；右侧山嘴杜鹃鸟影啼晕，春心如雾东流
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0a0e16,c2:0x141b28,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeYaoyuanJS({seed:23128,h:10}); yuan.g.position.set(0,0,-150); g.add(yuan.g);
  const terr=makeTerraceJS({}); g.add(terr);
  const an=makeTable({w:3.7,d:1.25,h:0.82,wood:0x231a14}); an.g.position.set(0.8,1.55,3.2); g.add(an.g);
  const se=makeSeJS({seed:23101}); se.g.position.set(0.8,2.37,3.2); g.add(se.g);
  const poet=jsPoet(1.4,'坐饮'); poet.position.set(1.0,1.55,0.4); poet.rotation.y=0.12; g.add(poet);
  /* 晓梦之蝶：半透明蝶影在瑟上、檐前飘舞（梦中之象，故作半透） */
  const die=makeButterfliesJS({n:8,area:{c:[1.5,4.6,4],r:[12,3,10]},seed:23102,op:0.42});
  g.add(die);
  /* 望帝之鹃：远山一嘴（右侧弧段山嘴）+杜鹃鸟影+啼光晕；春心如雾自山嘴流向天际 */
  const zui=makeRange({arc:0.80,a0:-0.62,r:40,h:9,layers:2,peaks:3,seed:23106,color:0x0b101b,atmo:0x1f2a3d,
    fogK:0.60,glowK:0.05,glow:0xaebccd,y:-4,order:-5});
  zui.g.position.set(30,0,-70); g.add(zui.g);
  const bird=makeBirdJS({scale:2.0,seed:23103}); bird.g.position.set(23.5,6.5,-41.5); bird.g.rotation.y=-0.35; g.add(bird.g);
  const flow=makeFlow({n:150,box:[56,9,20],pos:[8,7,-46],color:0x5f6e84,size:13,speed:2.4,maxA:0.07});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[150,10,60],pos:[0,3.4,-12],scale:46,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[100,14,46],pos:[0,8,2],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'树枝',w:17,n:6,d:4,color:0x05080e,seed:23129,sway:0.7,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(-12,-1.8,16.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:10,d:4,color:0x05080e,seed:23130,rim:0.09,rimC:0xb8c4dd});
  fg2.g.position.set(11.5,-1.4,15.5); g.add(fg2.g);
  addLights(g,{c:0xa6b4c8,i:0.28,p:[36,44,-36]},{c:0x19222f,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0); zui.update(t,0);
    se.update(t,k); die.update(t,k); bird.update(t,k);
    flow.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
    poet.update(t,k);
  }};
}
function bZhulei(){ // 叁（标志性瞬间）· 珠泪玉烟 —— 沧海月明珠有泪，蓝田日暖玉生烟：
                    // 月明沧海在左（光珠点点如泪），日暖蓝田在右（玉气如烟），一联冷暖对切同框
  const g=new THREE.Group();
  const water=makeWater({size:440,seg:80,amp:0.10,freq:0.14,speed:0.28,flow:[0.12,0.03],spec:1.0,
    deep:0x05080e,shallow:0x0d1522,skyc:0x111827,moonDir:[-0.30,0.16,-0.94]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xbcc9dc);
  water.mesh.position.set(-50,-0.55,-110); g.add(water.mesh);
  const grd=makeGround({r:96,c1:0x0a0e16,c2:0x141b28,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,52);
  const yuan=makeYaoyuanJS({r:250,h:8,y:-13,seed:23140}); yuan.g.position.set(-30,0,-170); g.add(yuan.g);
  /* 蓝田玉山（右）：山体入冷色（与全页一致）——「日暖」只交给玉烟暖雾与山脚一抹暖光晕；
     弧段六峰重叠成连绵山 mass，山脚沉入夜色原面 */
  const hill=makeRange({arc:0.62,a0:2.56,r:110,h:24,layers:2,peaks:6,seed:23141,
    color:0x12161e,atmo:0x202a3a,fogK:0.60,glowK:0.05,glow:0xaebccd,y:-8,order:-5});
  g.add(hill.g);
  const yan=makeYuYanJS({pos:[38,6,-92]}); g.add(yan);
  const warm=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc9a878,
    transparent:true,opacity:0.09,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  warm.scale.set(46,18,1); warm.position.set(38,7,-94); warm.renderOrder=3; g.add(warm);
  /* 沧海珠泪（左·冷）：月下海面光珠点点（月明由 STAGES 天空月担任，正落海面左上方） */
  const pearls=makePearlsJS({n:8,area:{c:[-36,2.6,-58],r:[30,2.4,20]},seed:23104});
  g.add(pearls);
  const terr=makeTerraceJS({}); g.add(terr);
  const an=makeTable({w:3.7,d:1.25,h:0.82,wood:0x231a14}); an.g.position.set(0.8,1.55,3.2); g.add(an.g);
  const se=makeSeJS({seed:23101}); se.g.position.set(0.8,2.37,3.2); g.add(se.g);
  const poet=jsPoet(1.55,'独立'); poet.position.set(-7.2,1.55,-2.8); poet.rotation.y=-2.35; g.add(poet);
  const mist=makeMist({n:6,spread:[160,10,64],pos:[0,3.2,-18],scale:48,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[110,15,48],pos:[0,9,-4],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05080e,seed:23142,rim:0.10,rimC:0xb8c4dd});
  fg1.g.position.set(-12.5,-1.6,18); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:24,h:3.0,color:0x05080e,seed:23143,rim:0.08,rimC:0xb8c4dd});
  fg2.g.position.set(2,-3.1,16.5); g.add(fg2.g);
  addLights(g,{c:0xa4b2cc,i:0.32,p:[-52,56,-44]},{c:0x1a2331,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); water.update(t);
    yuan.update(t,0); hill.update(t,0);
    yan.update(t,k);
    warm.material.opacity=k*0.09*(0.82+0.18*Math.sin(t*0.25+1.2));
    pearls.update(t,k);
    se.update(t,k);
    poet.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bWangran(){ // 肆（末境·可点击）· 追忆惘然 —— 此情可待成追忆，只是当时已惘然：
                     // 万象隐入惘然，唯瑟犹在；点击：四象幻影叠化流转+瑟弦余音光带
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x090d14,c2:0x131a26,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeYaoyuanJS({seed:23144,h:9}); yuan.g.position.set(0,0,-150); g.add(yuan.g);
  const terr=makeTerraceJS({}); g.add(terr);
  const an=makeTable({w:3.7,d:1.25,h:0.82,wood:0x231a14}); an.g.position.set(0.8,1.55,3.2); g.add(an.g);
  const se=makeSeJS({seed:23101,glowOp:0.16}); se.g.position.set(0.8,2.37,3.2); g.add(se.g);
  const jj=makeTable({w:1.15,d:1.15,h:0.70,wood:0x211812}); jj.g.position.set(-5.4,1.55,1.8); g.add(jj.g);
  const censer=makeCenserJS({}); censer.g.position.set(-5.4,2.25,1.8); g.add(censer.g);
  const poet=jsPoet(1.55,'独立'); poet.position.set(5.6,1.55,2.2); poet.rotation.y=-1.05; g.add(poet);
  /* 标志性交互：四象幻影（点击前 visible=false 硬关） */
  const sy=makeSiyuanJS({}); g.add(sy.g);
  const mist=makeMist({n:7,spread:[150,12,64],pos:[0,3.6,-14],scale:48,color:0x2a3648,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[100,15,48],pos:[0,8,0],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'栏杆',w:26,h:3.0,color:0x05080e,seed:23145,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(0,-2.9,14.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:10,d:4,color:0x05080e,seed:23146,rim:0.09,rimC:0xb8c4dd});
  fg2.g.position.set(11,-1.5,15); g.add(fg2.g);
  addLights(g,{c:0xa4b2c6,i:0.26,p:[-44,48,-40]},{c:0x18212e,i:0.50});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/6.0);
      const e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      se.update(t,k,ctl.reveal>0?e:0);          // 瑟弦余音：弦光沿弦往返、光华起伏（初值=峰值）
      sy.update(t,k,ctl.reveal);                 // 四象叠化流转
      poet.update(t,k); censer.update(t,k);
      mist.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); yuan.update(t,0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.10);
        pluck(5,0.05,0.12); pluck(3,0.85,0.10); pluck(1,1.70,0.08); pluck(0,2.60,0.06);   // 瑟弦余音四叠，渐远渐杳
        const fl=$('#flash'); fl.textContent='此情可待成追忆 只是当时已惘然';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b13),hor:C(0x161d2b),bot:C(0x04070c),fog:C(0x111823),fd:0.0052,star:0.20,
  moon:new THREE.Vector3(-40,66,-170),ms:1.1,mph:0.4,mhaze:0.20,dirC:C(0xa8bad0),dirI:0.34,
  dirP:new THREE.Vector3(-40,55,-40),ambC:C(0x1b2433),ambI:0.54},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,6.6,24],t:[0,5.0,14],lf:[0,5.8,-2],lt:[0,7.2,-28]},
  sky:()=>SK({fd:0.0052,star:0.20,ms:1.1,mph:0.4}) },
{ name:'锦瑟华年',dwell:17,river:0.02,build:bHuonian,
  cam:{f:[-3.8,4.0,8.6],t:[1.2,2.9,1.2],lf:[-1.8,3.9,3.5],lt:[2.5,3.4,-4]},
  sky:()=>SK({fd:0.0055,star:0.13,ms:0.85,mph:0.5,mhaze:0.22,
    moon:new THREE.Vector3(-46,56,-160),dirC:C(0xa6b6cc),dirI:0.30,
    dirP:new THREE.Vector3(-40,50,-40),ambC:C(0x1a2331),ambI:0.52}) },
{ name:'蝶梦鹃心',dwell:18,river:0.02,build:bDiemeng,
  cam:{f:[-1.0,5.6,14.5],t:[2.0,3.4,-2],lf:[2.5,5.8,-7],lt:[12,7.4,-30]},
  sky:()=>SK({fd:0.0060,star:0.05,ms:0.55,mph:0.55,mhaze:0.26,hor:C(0x1b2331),
    moon:new THREE.Vector3(28,34,-150),dirC:C(0xa6b4c8),dirI:0.26,
    dirP:new THREE.Vector3(36,44,-36),ambC:C(0x19222f),ambI:0.50}) },
{ name:'珠泪玉烟',dwell:20,river:0.02,build:bZhulei,
  cam:{f:[0,8.6,21],t:[0,4.8,-8],lf:[-2.5,9.2,-10],lt:[-8,10.8,-36]},
  sky:()=>SK({fd:0.0062,star:0.10,ms:1.8,mph:0.10,mhaze:0.12,
    moon:new THREE.Vector3(-82,52,-190),dirC:C(0xa4b2cc),dirI:0.32,
    dirP:new THREE.Vector3(-52,56,-44),ambC:C(0x1a2331),ambI:0.56}) },
{ name:'追忆惘然',dwell:19,river:0.02,build:bWangran,
  cam:{f:[0,5.8,15.5],t:[0.6,3.5,1.5],lf:[2.5,6.0,-4],lt:[7,7.2,-26]},
  sky:()=>SK({fd:0.0062,star:0.06,ms:0.9,mph:0.45,mhaze:0.24,
    moon:new THREE.Vector3(-58,48,-170),dirC:C(0xa4b2c6),dirI:0.26,
    dirP:new THREE.Vector3(-44,48,-40),ambC:C(0x18212e),ambI:0.50}) },
];
"""

if __name__ == '__main__':
    print('jinse.py —— 被 build.py 消费：python build.py jinse')
