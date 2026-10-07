# -*- coding: utf-8 -*-
"""shejiang-caifurong.py —— 《涉江采芙蓉》（汉·古诗十九首，queue no.260，宣纸留白）生成配置
4 境（[1,1,1,1] 分境）：
境壹涉江采芳（涉江采芙蓉·兰泽多芳草——江渚兰泽，采莲人小舟入芙蓉丛）、
境贰采之遗谁（采之欲遗谁·所思在远道——执芳在手，所思的人远在长路尽头）、
境叁还顾旧乡（标志性瞬间：还顾望旧乡·长路漫浩浩——回望长路的转身构图：
采莲人在舟中转身回望，长路沿江岸一路远去、尽头旧乡剪影淡若烟痕）、
境肆离居终老（末境可点击：点击还顾——故乡剪影淡现又缓缓远去，
暮色转冷、青灰雾流漫江、双雁同飞——同心而离居，忧伤以终老）。
美术立意「江渚采芳·回望长路」：宣纸上一次深挚的怅望——浅纸为天、浓墨作剪影、大量留白，
一江浅水贯穿（卷首俯瞰→境壹入丛→境贰执芳→境叁回望→境肆临暮）。
与已有宣纸留白页第一眼可区分：终南望余雪=雪线山体+城头望雪（雪景城郭）、
十五从军征=荒村坟园+破败庭院、登乐游原=夕阳驱车、幸蜀宫=行宫宫苑——
本页=江面采芳+回望长路（芙蓉浮叶、兰泽芳草、兰舟采莲人、渐窄长路、岸柳、旧乡剪影、双雁），
有水有舟无雪无城郭无坟园。核心构图是「江上采芳+回望长路的转身」。
自建 builder：makeJiangShuiSJ（纸色江水）/ makeFurongSJ（芙蓉丛：浮叶+花头+花苞）/
makeLanzeSJ（兰泽芳草丛）/ makeLianZhouSJ（兰舟）/ makeCailianrenSJ（采莲人·含蓄剪影·执芳）/
makeChangluSJ（长路：渐窄路板+岸柳）/ makeJiuxiangSJ（旧乡剪影，末境点击前 visible=false 硬关）/
makeShuangyanSJ（双雁同飞）/ makeDanriSJ（纸色淡日）/ makeYuanHuanSJ（低平远山环）。
考点钉子：遗 wèi（采之欲遗谁）／浩浩 hào／离居 lí／还 huán（还顾）（小测第 3 题）；
《古诗十九首》五言之冠冕+《文选》收录+采芳赠远的楚辞传统（第 4 题）；
「同心而离居，忧伤以终老」的深挚（第 5 题）。
多音字：遗→未（wèi）、还顾→环顾（huán gù）（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='shejiang-caifurong', title='涉江采芙蓉', dyn='汉 · 古诗十九首',
    brand_author='古 诗 十 九 首',
    gold_rgb='74,90,78',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#4a5a4e; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(74,90,78,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(233,226,208', 1),
        ('rgba(4,6,11', 'rgba(212,202,176', 2),
        ('rgba(6,9,16', 'rgba(233,226,208', 1),
        ('rgba(3,5,9', 'rgba(236,230,214', 1),
        ('#0b101c', '#f6f1e1', 1),
        ('#6f664f', '#8a8268', 1),
        ('#5a5340', '#8d8571', 1),
        ('0x0a1526', '0xe6dfcc', 4),
    ],
    tip='轻点画面 / 按空格 —— 故乡剪影淡现，又缓缓远去',
    hint='← → 键或空格逐境游览 · 末境可点击画面：点击还顾，故乡剪影淡现又远去',
    cover_read='涉江采芙蓉。汉，古诗十九首。涉江采芙蓉，兰泽多芳草。采之欲遗谁，所思在远道。还顾望旧乡，长路漫浩浩。同心而离居，忧伤以终老。',
    cover_p1='四重意境，随诗句次第展开：渡过江水去采摘芙蓉，兰泽里芳草何其繁盛；采下花来想送给谁呢？所思念的人远在迢迢长路的另一头；回望旧乡，长路漫漫浩浩没有尽头；两心相同却各在一方，只能怀着这份忧伤一直到老。',
    cover_p2='边读诗，边随采莲人渡江采芳、执花远望：花采到了，要送的人不在眼前；家在心上，却隔着漫浩浩的长路。末境轻点画面，看故乡剪影从雾中淡现、又缓缓远去——「同心而离居，忧伤以终老」。',
    end_h2='同心 · 离居', cn_word='四',
    words_js="['再涉一次江，采一枝芙蓉','初识古诗十九首，尚需共读','渐入诗境，再诵几遍','兰泽芳草，远道思深','已解还顾望乡之痛','同心离居，余哀不尽']",
    sky_atmo='0xd8d5c9',
)

POEM_JS = """const POEM = [
{ name:'涉江采芳', jing:'渡过江水去采摘芙蓉，兰花泽里芳草多么繁盛。（江渚 · 兰泽 · 采莲人入芙蓉丛）',
  segs:[
   {c:'涉江采芙蓉，', p:py('shè jiāng cǎi fú róng')},
   {c:'兰泽多芳草。', p:py('lán zé duō fāng cǎo')}],
  read:'涉江采芙蓉，兰泽多芳草。',
  yisi:'渡过江水去采摘芙蓉花，兰花泽里长满了芬芳的香草。——起笔是一幅纯净的采芳图：江水、兰泽、芙蓉、芳草，全是洁净芳洁之物。「涉江」二字见得郑重：不是顺手掐一朵，而是专程渡水而去；「多」字写足兰泽芳草的繁盛，也暗中蓄起一份兴致与欢喜——采芳是为了赠人。以乐景起笔，后面的怅惘才跌得越深：这一枝兴冲冲采下的芙蓉，注定送不出去。',
  zhu:[['涉江','渡过江水。涉，徒步渡水，此指乘舟渡江——为一枝芙蓉专程渡水，见得郑重','芙蓉','荷花的别名。莲与「怜」谐音，古人采莲多寄相思','兰泽','长满兰草的低湿水泽。泽，聚水的洼地——江边多芳草的湿地'],['芳草','香草，兰草之类——楚辞以来以香草喻美好的人与情，采芳以赠远人']] },
{ name:'采之遗谁', jing:'花采在手，要送给谁呢？所思念的那个人，远在迢迢的长道那头。（执芳 · 远望 · 长路上的行人）（所思在远道）',
  segs:[
   {c:'采之欲遗谁，', p:py('cǎi zhī yù wèi shuí')},
   {c:'所思在远道。', p:py('suǒ sī zài yuǎn dào')}],
  read:'采之欲遗谁，所思在远道。',
  yisi:'花采到手，想要送给谁呢？我所思念的那个人，远在遥远的长路上。——自问自答，一句话把欢喜问成了空：「遗」是赠，赠要两人在场，而所思之人偏偏「在远道」。花在手中，人在天边，采芳的全部兴致顷刻落空。古人采芳本为赠远（香草赠人，以寄相思），如今芳草满泽、芙蓉在手，却空无一人可赠——这一问，问出了全诗的转折：乐景到此收束，怅惘从此展开。',
  zhu:[['遗','赠送、赠给，读 wèi——「采之欲遗谁」：采下花来想送给谁呢'],['所思','所思念的人——未必实指一人，可解为妻子、故乡的亲人，历代多说并存'],['远道','遥远的路途——所思之人行役在外，正走在归不到头的长路上'],['采芳赠远','古代风俗与诗学传统：芳草香花赠人以寄情，上承楚辞香草美人之意——采花本为赠人，花在而人远，相思由此而生']] },
{ name:'还顾旧乡', jing:'回头看故乡的方向，长路漫漫浩浩，望不到尽头。（转身回望 · 长路远去 · 旧乡烟痕）（标志性瞬间：还顾望旧乡——长路漫浩浩）',
  segs:[
   {c:'还顾望旧乡，', p:py('huán gù wàng jiù xiāng')},
   {c:'长路漫浩浩。', p:py('cháng lù màn hào hào')}],
  read:'还顾望旧乡，长路漫浩浩。',
  yisi:'回过头来眺望故乡，长路漫漫浩浩，无边无际。——「还顾」是一个转身的动作：身在江渚采芳，心却早已越过江面、顺着来路回去了。望见的是什么呢？不是家，而是路——长路漫浩浩，一直铺到天边，旧乡只在水天尽头留一道淡淡的烟痕。「漫」是漫长无尽，「浩浩」是浩渺无际，四字把空间的远与时间的久叠在一起：路望不到头，归期同样望不到头。这一转身，是全诗最痛的一笔——所思的人远在长路那头，故乡也在长路那头，两头都回不去。',
  zhu:[['还顾','回头望、回望。还，回转、掉转，读 huán——身在江上而心回故里，一个动作写尽归思'],['旧乡','故乡'],['漫','漫长、无边无际的样子——写路望不到头'],['浩浩','广阔浩渺、盛大无际的样子，读 hào hào——本多用于水势，移来写长路，路与愁一同浩浩而去']] },
{ name:'离居终老', jing:'心意相同的人偏偏各在一方，只能怀着忧伤一直到老。（暮江 · 点击还顾：故乡剪影淡现又远去 · 双雁同飞）（末境点击画面：点击还顾——故乡剪影淡现，又缓缓远去）',
  segs:[
   {c:'同心而离居，', p:py('tóng xīn ér lí jū')},
   {c:'忧伤以终老。', p:py('yōu shāng yǐ zhōng lǎo')}],
  read:'同心而离居，忧伤以终老。',
  yisi:'彼此的心意息息相通，人却分居两地不得相聚，只能怀着这份忧伤一直到老。——「同心」与「离居」四个字硬生生对撞：心越近，人越远，越见离之无奈。收束不呼号、不泣诉，只淡淡说「忧伤以终老」——把一时的相思说成一生的底色，语浅而情深，正是《古诗十九首》「深衷浅貌，短语长情」的绝唱处。采芳赠远而终不可赠，回望旧乡而终不可归，一切深情都安放在「终老」二字里，余哀不尽。',
  zhu:[['同心','心意相通、两情相契——指心心相印的伴侣或知音'],['离居','分处两地、分离而居——同心而偏离居，是全诗最深的痛处'],['终老','到老、终其一生——忧伤不止一年一月，而是一生'],['五言之冠冕','《古诗十九首》历代被誉为「五言之冠冕」：东汉末年文人五言诗成熟的最高代表，刘勰称其「一字千金」']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「涉江采芙蓉，兰泽多芳草。」的下一句是？', o:['采之欲遗谁，所思在远道','还顾望旧乡，长路漫浩浩','同心而离居，忧伤以终老'], a:0},
 {q:'「还顾望旧乡，长路漫浩浩。」的下一句是？', o:['采之欲遗谁，所思在远道','同心而离居，忧伤以终老','兰泽多芳草'], a:1},
 {q:'「采之欲遗谁」「长路漫浩浩」的读音与词义，正确的一项是？', o:['遗读 wèi，赠送——采下花来想送给谁；浩浩读 hào hào，广阔浩渺、无边无际的样子','遗读 yí，遗失——采下的花弄丢了；浩浩读 gǎo gǎo，草木枯白的样子','遗读 wèi，遗留——把花遗落在兰泽里；浩浩读 hào hào，喧闹嘈杂的样子'], a:0},
 {q:'关于《涉江采芙蓉》与《古诗十九首》，下列说法正确的一项是？', o:['《古诗十九首》是西汉乐府官署采集的民歌，专写田间劳作与丰收的喜悦','此诗为唐代律诗，讲究平仄对仗，中间两联必须工整相对','《古诗十九首》是东汉文人五言诗的代表，最早收录于南朝梁萧统所编《文选》；「涉江采芳」上承楚辞采香草赠远人的传统——采花本为赠人，花在而人远，相思由此而生'], a:2},
 {q:'对「同心而离居，忧伤以终老」的理解，最恰当的一项是？', o:['两心相知相通，人却分处两地不得相聚——不写撕心裂肺的呼号，只以「忧伤以终老」作结，把绵长无尽的思念写成一生的底色，语浅而情深','两个人同心协力却分开居住，诗在议论成家立业应当同住一处','诗人最终决定放弃思念，与所思之人断绝往来，忧伤到此为止'], a:0},
];
"""

SCENES_JS = """/* ================= 涉江采芙蓉 · 四境场景（宣纸留白·江渚采芳：涉江采芳、采之遗谁、还顾旧乡、离居终老） =================
   美术立意：「江渚采芳·回望长路」——宣纸上一次深挚的怅望：浅纸为天、浓墨作剪影、大量留白，
   一江浅水贯穿（卷首俯瞰→境壹入丛→境贰执芳→境叁回望→境肆临暮）。
   与已有宣纸留白页第一眼可区分：终南望余雪=雪线山体+城头望雪（雪景城郭）、
   十五从军征=荒村坟园+破败庭院、登乐游原=夕阳驱车、幸蜀宫=行宫宫苑——
   本页=江面采芳+回望长路（芙蓉浮叶、兰泽芳草、兰舟采莲人、渐窄长路、岸柳、旧乡剪影、双雁），
   有水有舟，无雪无城郭无坟园。核心是「江上采芳+回望长路的转身构图」。
   标志性瞬间（境叁）：还顾望旧乡——采莲人在舟中转身回望，长路沿江岸一路远去、
   尽头旧乡剪影淡若烟痕，「长路漫浩浩」。
   末境点击：点击还顾——故乡剪影淡现又缓缓远去，暮色由暖转冷、青灰雾流漫江（accent）、双雁同飞。
   accent=#4a5a4e（青灰竹叶色）只落在：采莲人袍色衣领、UI、末境暮流与暮光转冷上，全页近零饱和；
   芙蓉花用极淡的藕色 0xd8c2b6 系，是全页唯一一点花意。
   布局纪律：主体场景群放 z −12…−80（骨架常驻远山环 z≈−260…−330 之前）；自建低平远山环在 z≈−118。 */

/* —— 纸色江水 makeJiangShuiSJ(o)：makeWater 换宣纸色板（deep/shallow/skyc 全纸色、spec 压低），
   波幅放缓如绢，自定义水面着色器随 fogShaders 同步雾参 —— */
function makeJiangShuiSJ(o){
  o=o||{};
  return makeWater({size:o.size===undefined?700:o.size,seg:110,
    amp:o.amp===undefined?0.30:o.amp,freq:o.freq===undefined?0.075:o.freq,
    speed:o.speed===undefined?0.55:o.speed,flow:o.flow===undefined?[0.22,1]:o.flow,
    deep:o.deep===undefined?0xbab49c:o.deep,shallow:o.shallow===undefined?0xd6cfb8:o.shallow,
    skyc:o.skyc===undefined?0xe3dccb:o.skyc,moonDir:o.moonDir===undefined?[0.3,1,0.25]:o.moonDir,
    spec:o.spec===undefined?0.30:o.spec,y:o.y===undefined?-1.6:o.y});
}

/* —— 芙蓉丛 makeFurongSJ(o)：浮叶圆盘（青灰绿）+ 花头（8 瓣极淡藕色）+ 花苞，合批 1 mesh ——
   「涉江采芙蓉」：叶贴水、花离水，全页近零饱和里唯一一点花意 */
function makeFurongSJ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26061:o.seed);
  const n=o.n===undefined?4:o.n, m=o.m===undefined?2:o.m;
  const w=o.w===undefined?3.2:o.w, h=o.h===undefined?2.1:o.h;
  const leafC=o.leafC===undefined?0x4e5948:o.leafC, floC=o.floC===undefined?0xd8c2b6:o.floC;
  const yW=o.yWater===undefined?-1.42:o.yWater;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*w*0.7, r=(0.55+0.55*R())*h*0.45;
    const leaf=new THREE.SphereGeometry(r,10,7);
    leaf.scale(1,0.10,1); leaf.translate(x,yW,z);
    B.put(leaf,shadeColor(leafC,0.80+0.38*R()));
  }
  for(let i=0;i<m;i++){
    const x=(R()-0.5)*w*0.8, z=(R()-0.5)*w*0.5;
    const top=yW+h*(0.55+0.35*R());
    B.put(limbGeo([x,yW-0.15,z],[x+(R()-0.5)*0.2,top,z+(R()-0.5)*0.2],0.035,0.026,6),shadeColor(leafC,0.9+0.2*R()));
    const blo=yW+h;
    for(let p=0;p<8;p++){
      const a=p/8*6.283+(R()-0.5)*0.3;
      const pet=new THREE.SphereGeometry(0.20,6,5);
      pet.scale(0.55,1.5,0.30); pet.rotateX(0.42+R()*0.2); pet.rotateY(a);
      pet.translate(x+Math.cos(a)*0.17,blo,z+Math.sin(a)*0.17);
      B.put(pet,shadeColor(floC,0.92+0.16*R()));
    }
    const core=new THREE.ConeGeometry(0.12,0.34,7); core.translate(x,blo+0.18,z);
    B.put(core,shadeColor(floC,0.78));
  }
  if(o.bud!==false){
    const x=(R()-0.5)*w*0.6, z=(R()-0.5)*w*0.5, top=yW+h*(0.5+0.25*R());
    B.put(limbGeo([x,yW-0.12,z],[x,top,z],0.030,0.022,6),shadeColor(leafC,0.9+0.2*R()));
    const bud=new THREE.ConeGeometry(0.15,0.50,8); bud.rotateX(0.14); bud.translate(x,top+0.22,z);
    B.put(bud,shadeColor(floC,0.72));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4238,emissive:0x040604}),{c:o.rimC===undefined?0xd8d6c2:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.022*Math.sin(t*0.7+ph)*kk;
    g.rotation.x=0.012*Math.sin(t*0.5+ph*1.6)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 兰泽芳草 makeLanzeSJ(o)：一丛兰草（叶自根部外拱、梢头略亮），合批 1 mesh ——「兰泽多芳草」 */
function makeLanzeSJ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26071:o.seed);
  const n=o.n===undefined?12:o.n, w=o.w===undefined?1.8:o.w, h=o.h===undefined?1.5:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*w*0.7;
    const H=h*(0.5+0.6*R()), a=R()*6.283, lean=0.30+R()*0.42;
    const dx=Math.cos(a)*lean*H*0.55, dz=Math.sin(a)*lean*H*0.55;
    B.put(limbGeo([x,0,z],[x+dx*0.4,H*0.62,z+dz*0.4],0.030,0.020,4),shadeColor(0x57604e,0.85+0.30*R()));
    B.put(limbGeo([x+dx*0.4,H*0.62,z+dz*0.4],[x+dx,H,z+dz],0.020,0.012,4),shadeColor(0x7a8266,0.9+0.30*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x38402e,emissive:0x040603}),{c:o.rimC===undefined?0xcccaae:o.rimC,i:o.rim===undefined?0.09:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.030*Math.sin(t*0.85+ph)*kk;
    g.rotation.x=0.016*Math.sin(t*0.6+ph*1.4)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 兰舟 makeLianZhouSJ(o)：采莲小舟（Lathe 半壳拉长 + 两道横枋 + 斜倚竹篙 + 水面接触影），
   合批 1 mesh —— 舟身浓墨，是江面唯一深色主体 */
function makeLianZhouSJ(o){
  o=o||{};
  const B=new GeoBag();
  const pts=[[0,0.02],[0.30,0.02],[0.46,0.10],[0.50,0.30],[0.46,0.50],[0.30,0.60],[0.04,0.64]];
  const hull=new THREE.LatheGeometry(pts.map(p=>new THREE.Vector2(p[0],p[1])),18);
  hull.scale(3.6,1.5,1.7);
  B.put(hull,0x363029);
  const t1=new THREE.BoxGeometry(0.18,0.07,1.35); t1.translate(-0.55,0.50,0); B.put(t1,0x2c2822);
  const t2=new THREE.BoxGeometry(0.18,0.07,1.30); t2.translate(0.55,0.50,0); B.put(t2,0x2c2822);
  const pole=new THREE.CylinderGeometry(0.028,0.038,3.4,6); pole.rotateZ(1.30);
  pole.translate(0.15,0.42,0.42); B.put(pole,0x3a332a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x33302a,emissive:0x050505,side:THREE.DoubleSide}),{c:o.rimC===undefined?0xd2d0be:o.rimC,i:o.rim===undefined?0.13:o.rim,p:2.4})));
  return g;
}

/* —— 采莲人 makeCailianrenSJ(o)：青灰袍（accent）采莲人，含蓄剪影（背影侧影示人，无面目特写），
   sprig:true 时手执一枝芙蓉（花在手上=「采之」）—— 全诗贯穿的同一造型 */
function makeCailianrenSJ(o){
  o=o||{};
  const sc=o.scale===undefined?1.15:o.scale;
  const fig=makeFigure({pose:'独立',robe:0x4a5a4e,belt:0x66755f,skin:0xd2ae86,collar:0x8f9c88,
    hair:0x1b1d1a,hat:'发髻',rim:0.42,rimC:o.rimC===undefined?0xd8d6c2:o.rimC,noProp:true,scale:sc});
  if(o.sprig){
    const B=new GeoBag();
    const hx=0.66, hy=1.30, hz=0.10;
    B.put(limbGeo([hx,hy,hz],[hx+0.30,hy+0.85,hz+0.12],0.030,0.020,6),0x4e5948);
    const lf=new THREE.SphereGeometry(0.14,6,5); lf.scale(1.5,0.16,0.8);
    lf.translate(hx+0.16,hy+0.52,hz+0.06); B.put(lf,0x56614e);
    for(let p=0;p<5;p++){
      const a=p/5*6.283;
      const pet=new THREE.SphereGeometry(0.085,6,5); pet.scale(0.55,1.5,0.32);
      pet.rotateX(0.5); pet.rotateY(a);
      pet.translate(hx+0.30,hy+0.92,hz+0.12);
      B.put(pet,0xd8c2b6);
    }
    const core=new THREE.ConeGeometry(0.055,0.16,6); core.translate(hx+0.30,hy+1.00,hz+0.12);
    B.put(core,0xc9aa9c);
    const sprig=new THREE.Mesh(mergeGeos(B.list),
      rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
        specular:0x3a4238,emissive:0x050505}),{c:0xd8d6c2,i:0.12,p:2.4}));
    fig.add(sprig);
  }
  const g=new THREE.Group(); g.add(fig);
  const ph=(o.seed===undefined?26081:o.seed)%6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    fig.update(t,kk);
    fig.rotation.z=0.010*Math.sin(t*0.4+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 兰舟+采莲人 makeBoatSJ(o)：舟与舟中人合组（同摇摆），face=人朝向（弧度），
   sprig=是否执芳 —— 摇摆只作用于整组，fadeK 逐帧合规 */
function makeBoatSJ(o){
  o=o||{};
  const boat=makeLianZhouSJ({});
  const poet=makeCailianrenSJ({scale:1.15,sprig:o.sprig,seed:o.seed});
  poet.position.set(0,-0.02,0.1); poet.rotation.y=o.face===undefined?0:o.face;
  boat.add(poet);
  const g=new THREE.Group(); g.add(boat);
  const ph=(o.seed===undefined?26091:o.seed)%6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.014*Math.sin(t*0.55+ph)*kk;
    g.rotation.x=0.010*Math.sin(t*0.42+ph*1.7)*kk;
    g.position.y=(o.y0===undefined?0:o.y0)+0.035*Math.sin(t*0.5+ph)*kk;
    poet.update(t,kk); };
  g.userData.update=g.update;
  return g;
}

/* —— 长路 makeChangluSJ(o)：沿江岸一路远去的长路（渐窄路板 + 岸柳垂枝 + 路畔芦荻），合批 1 mesh ——
   「长路漫浩浩」：路宽随远渐收，尽头没入雾中 */
function makeChangluSJ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26021:o.seed);
  const x0=o.x0===undefined?26:o.x0, x1=o.x1===undefined?-70:o.x1;
  const z0=o.z0===undefined?-56:o.z0, z1=o.z1===undefined?-78:o.z1;
  const segs=o.segs===undefined?12:o.segs, y=o.y===undefined?-1.47:o.y;
  const B=new GeoBag();
  let px=x0, pz=z0;
  const pts=[];
  for(let i=0;i<=segs;i++){
    const t=i/segs;
    pts.push([x0+(x1-x0)*t, z0+(z1-z0)*t+Math.sin(t*5.2)*(z1-z0)*0.06]);
  }
  for(let i=0;i<segs;i++){
    const a=pts[i], b=pts[i+1], t1=(i+1)/segs;
    const w=3.0*(1-0.66*t1), len=Math.hypot(b[0]-a[0],b[1]-a[1]);
    const rd=new THREE.BoxGeometry(w+0.5,0.07,len+0.4);
    rd.rotateY(Math.atan2(b[0]-a[0],b[1]-a[1]));
    rd.translate((a[0]+b[0])/2,y,(a[1]+b[1])/2);
    B.put(rd,shadeColor(0xbbb096,0.94+0.12*R()));
  }
  /* 岸柳：沿路数株，干+垂枝 */
  const nb=o.willows===undefined?7:o.willows;
  for(let i=0;i<nb;i++){
    const t=0.04+0.92*R();
    const wx=pts[0][0]+(pts[pts.length-1][0]-pts[0][0])*t+(R()-0.5)*3;
    const wz=pts[0][1]+(pts[pts.length-1][1]-pts[0][1])*t+Math.sin(t*5.2)*(z1-z0)*0.06+(R()<0.5?-1:1)*(2.2+R()*1.6);
    const hh=3.2+2.6*R();
    B.put(limbGeo([wx,y,wz],[wx+(R()-0.5)*0.5,y+hh,wz+(R()-0.5)*0.5],0.14,0.06,5),shadeColor(0x33392f,0.9+0.25*R()));
    for(let b=0;b<5;b++){
      const a2=R()*6.283, len=hh*(0.30+0.30*R());
      const tx=wx+Math.cos(a2)*len*0.55, ty=y+hh*(0.55+0.3*R())-len*0.55, tz=wz+Math.sin(a2)*len*0.4;
      B.put(limbGeo([wx,y+hh*(0.62+0.28*R()),wz],[tx,ty,tz],0.045,0.016,4),shadeColor(0x3a4034,0.85+0.30*R()));
    }
  }
  /* 路畔芦荻数丛 */
  for(let i=0;i<10;i++){
    const t=R(), wx=pts[0][0]+(pts[pts.length-1][0]-pts[0][0])*t+(R()-0.5)*4;
    const wz=pts[0][1]+(pts[pts.length-1][1]-pts[0][1])*t+(R()<0.5?-1:1)*(3.4+R()*2);
    for(let b=0;b<3;b++){
      const hh=1.0+1.1*R();
      B.put(limbGeo([wx,y,wz],[wx+(R()-0.5)*0.3,y+hh,wz+(R()-0.5)*0.3],0.024,0.014,4),shadeColor(0x6a6a52,0.85+0.35*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x38382c,emissive:0x040504}),{c:o.rimC===undefined?0xd4d2c0:o.rimC,i:o.rim===undefined?0.09:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.004*Math.sin(t*0.5+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 旧乡剪影 makeJiuxiangSJ(o)：低城垣（门楼+角楼）+ 屋舍 + 树，平面浓墨（MeshBasic 吃雾），
   材质透明（op 可调），末境作「点击还顾」的幻影（点击前 visible=false 硬关）——
   返回 {g,mat}；每帧写 opacity 时由调用方乘 fadeK */
function makeJiuxiangSJ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26041:o.seed);
  const inkC=o.color===undefined?0x3c423c:o.color;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(30,2.2,1.6); wall.translate(0,1.1,0); B.put(wall,shadeColor(inkC,0.92));
  const cap=new THREE.BoxGeometry(30.6,0.22,2.0); cap.translate(0,2.31,0); B.put(cap,shadeColor(inkC,1.12));
  [[-9.5],[9.5]].forEach(function(p){
    const tw=new THREE.BoxGeometry(3.0,3.4,2.4); tw.translate(p[0],1.7,0.1); B.put(tw,shadeColor(inkC,0.84));
    const rf=new THREE.ConeGeometry(2.5,1.1,4); rf.rotateY(Math.PI/4); rf.translate(p[0],3.95,0.1);
    B.put(rf,shadeColor(inkC,0.72));
  });
  const gate=new THREE.BoxGeometry(3.6,3.0,2.0); gate.translate(0,1.5,-0.1); B.put(gate,shadeColor(inkC,0.80));
  const gArc=new THREE.CylinderGeometry(1.0,1.0,0.6,10,1,false,0,Math.PI); gArc.rotateX(Math.PI/2);
  gArc.translate(0,3.0,0.92); B.put(gArc,0x14171a);
  for(let i=0;i<4;i++){
    const hx=-12+i*8+(R()-0.5)*2, bw=2.6+1.2*R(), bh=1.7+0.9*R();
    const body=new THREE.BoxGeometry(bw,bh,bw*0.8); body.translate(hx,bh/2,3.6+(R()-0.5)*1.6);
    B.put(body,shadeColor(inkC,0.88+0.2*R()));
    const roof=new THREE.ConeGeometry(bw*0.82,1.0,4); roof.rotateY(Math.PI/4);
    roof.translate(hx,bh+0.5,3.6+(R()-0.5)*1.6); B.put(roof,shadeColor(inkC,0.70));
  }
  for(let i=0;i<3;i++){
    const tx=-14+i*13+(R()-0.5)*3, hh=2.6+1.4*R();
    B.put(limbGeo([tx,0,-2.5],[tx+(R()-0.5)*0.4,hh,-2.5],0.10,0.05,5),shadeColor(inkC,0.78));
    const crown=new THREE.SphereGeometry(1.0+0.5*R(),7,6);
    crown.scale(1.15,0.85,1.0); crown.translate(tx,hh+0.4,-2.5);
    B.put(crown,shadeColor(inkC,0.86));
  }
  const mat=new THREE.MeshBasicMaterial({vertexColors:true,transparent:true,
    opacity:o.op===undefined?0.5:o.op,fog:true});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat);
  const g=new THREE.Group(); g.add(mesh);
  return {g:g,mat:mat};
}

/* —— 双雁 makeShuangyanSJ(o)：两只雁剪影同飞（同心之喻），墨色，update 缓慢横渡 —— */
function makeShuangyanSJ(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26051:o.seed);
  const B=new GeoBag();
  for(let i=0;i<2;i++){
    const bx=i*1.5, by=i*0.30, bz=-i*0.5;
    const body=new THREE.SphereGeometry(0.30,7,6); body.scale(1.9,0.55,0.7);
    body.translate(bx,by,bz); B.put(body,0x343a38);
    [-1,1].forEach(function(s){
      const wg=new THREE.SphereGeometry(0.55,6,5); wg.scale(0.5,0.10,1.6);
      wg.rotateZ(s*0.18); wg.rotateY(s*0.40);
      wg.translate(bx+s*0.42,by+0.06,bz-0.10);
      B.put(wg,shadeColor(0x343a38,0.9));
    });
    const nk=new THREE.SphereGeometry(0.09,6,5); nk.translate(bx+0.62,by+0.10,bz);
    B.put(nk,0x343a38);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a2e2c,emissive:0x050605}),{c:0xd2d0be,i:0.14,p:2.6})));
  const x0=g.position.x, y0=g.position.y, ph=R()*6.283;
  const rng=o.rng===undefined?100:o.rng, v=o.v===undefined?1.6:o.v;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    let x=x0+t*v*kk;
    x=((x+rng*0.5)%rng+rng)%rng-rng*0.5;
    g.position.x=x;
    g.position.y=y0+0.5*Math.sin(t*0.4+ph)*kk;
    g.rotation.z=0.05*Math.sin(t*0.8+ph)*kk;
    g.rotation.y=-0.20; };
  g.userData.update=g.update;
  return g;
}

/* —— 纸色淡日 makeDanriSJ(o)：limbTex 日轮+一环更淡的晕（fog:false；fadeK 初值=最大）—— */
function makeDanriSJ(o){
  o=o||{};
  const r=o.r===undefined?7:o.r, discOp=o.op===undefined?0.30:o.op, hazeOp=o.haze===undefined?0.10:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xf3ecd8:o.color,
    transparent:true,opacity:discOp,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0xefe8d2:o.hazeC,
    transparent:true,opacity:hazeOp,depthWrite:false,fog:false}));
  haze.scale.set(r*5.4,r*5.4,1); g.add(haze);
  g.update=function(t,k){ const kk=k===undefined?1:k;
    disc.material.opacity=kk*discOp*(0.95+0.05*Math.sin(t*0.4));
    haze.material.opacity=kk*hazeOp*(0.85+0.15*Math.sin(t*0.27+1.3)); };
  g.userData.update=g.update;
  return g;
}

/* —— 低平远山环 makeYuanHuanSJ(o)：自建远山（在骨架常驻 bgRange 之前，z≈−118 不被遮挡）—— */
function makeYuanHuanSJ(o){
  o=o||{};
  return makeRange({r:o.r===undefined?280:o.r,h:o.h===undefined?8.5:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?26001:o.seed,
    color:0x2c2f33,atmo:0xd8d5c9,fogK:0.70,glowK:0.03,glow:0xf2ecd8,y:-12,order:-6});
}

function bCover(){ // 卷首 · 江渚采芳全景 —— 一江浅水，芙蓉洲渚，长路沿江岸远去，采莲小舟入丛
  const g=new THREE.Group();
  const water=makeJiangShuiSJ({}); g.add(water.mesh);
  const ridge=makeYuanHuanSJ({seed:26002}); ridge.g.position.set(0,0,-118); g.add(ridge.g);
  /* 江岸与长路 */
  const bank=makeGround({r:70,c1:0xd9d2ba,c2:0xbdb89e,y:-1.50});
  bank.mesh.scale.set(3.4,1,0.62); bank.mesh.position.set(0,-1.50,-92); g.add(bank.mesh);
  const lu=makeChangluSJ({seed:26022,x0:26,x1:-70,z0:-56,z1:-78}); g.add(lu);
  const travelers=makeCrowd({n:2,rect:[-34,-72,22,3],seed:26023,color:0x2c302c,rimC:0xcac6b2,rim:0.14,sMin:0.34,sMax:0.42,y:-1.46});
  g.add(travelers.mesh);
  /* 芙蓉洲渚与兰泽芳草 */
  const islet1=makeGround({r:6,c1:0xd5cdb2,c2:0xb8b499,y:-1.42}); islet1.mesh.position.set(-10,-1.42,-26); g.add(islet1.mesh);
  const islet2=makeGround({r:5,c1:0xd5cdb2,c2:0xb8b499,y:-1.42}); islet2.mesh.position.set(10,-1.42,-29); g.add(islet2.mesh);
  const lz1=makeLanzeSJ({seed:26072,n:14,w:3.4,h:1.7}); lz1.position.set(-10,-1.40,-26); g.add(lz1);
  const lz2=makeLanzeSJ({seed:26073,n:12,w:3.0,h:1.5}); lz2.position.set(10,-1.40,-29); g.add(lz2);
  const fr1=makeFurongSJ({seed:26062,n:5,m:3,w:4.6}); fr1.position.set(-3.5,-1.42,-17); g.add(fr1);
  const fr2=makeFurongSJ({seed:26063,n:4,m:2,w:4.0}); fr2.position.set(5.5,-1.42,-21); g.add(fr2);
  const fr3=makeFurongSJ({seed:26064,n:5,m:3,w:5.0}); fr3.position.set(-9,-1.42,-23); g.add(fr3);
  /* 采莲小舟入丛 */
  const boat=makeBoatSJ({seed:26092,sprig:false,face:0.4}); boat.position.set(-1.0,-1.56,-15.5); boat.rotation.y=0.35; g.add(boat);
  /* 淡日、薄雾、飞鸟微尘 */
  const sun=makeDanriSJ({r:6.5,op:0.16,haze:0.11}); sun.position.set(-48,30,-95); g.add(sun);
  const mist=makeMist({n:6,spread:[230,16,90],pos:[0,3.5,-56],scale:68,color:0xe0d9c4,op:0.11});
  g.add(mist.g);
  const dust=makeGlow({n:20,box:[150,10,60],pos:[0,4,-40],color:0xd8d0b4,size:4.0,speed:0.03,rise:0,add:true,maxA:0.06});
  g.add(dust.points);
  /* 前景：岸边坡石与芦苇、近处一丛芙蓉压角 */
  const fgL=makeForeground({kind:'坡石',n:2,r:3.0,w:13,d:6,color:0x23262b,seed:26024,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-12,-1.9,18); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:12,n:8,d:3,color:0x1d1f22,seed:26025,sway:0.8,tip:0x5a5648,scale:0.8});
  fgR.g.position.set(11,-1.8,17); g.add(fgR.g);
  const frNear=makeFurongSJ({seed:26065,n:5,m:2,w:5.0,h:2.6}); frNear.position.set(4.5,-1.44,4); g.add(frNear);
  addLights(g,{c:0xe2dab8,i:0.5,p:[-40,84,26]},{c:0xd4d6c4,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sun.update(t,k); lu.update(t,k); travelers.update(t);
    lz1.update(t,k); lz2.update(t,k); fr1.update(t,k); fr2.update(t,k); fr3.update(t,k); frNear.update(t,k);
    boat.update(t,k); mist.update(t,k); dust.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bCaifang(){ // 壹 · 涉江采芳 —— 涉江采芙蓉，兰泽多芳草：小舟入芙蓉丛，兰泽芳草夹岸
  const g=new THREE.Group();
  const water=makeJiangShuiSJ({}); g.add(water.mesh);
  const ridge=makeYuanHuanSJ({seed:26026}); ridge.g.position.set(-14,0,-116); g.add(ridge.g);
  const bank=makeGround({r:70,c1:0xd8d1b9,c2:0xbcb79d,y:-1.50});
  bank.mesh.scale.set(3.4,1,0.62); bank.mesh.position.set(0,-1.50,-92); g.add(bank.mesh);
  /* 芙蓉丛：近大远小，包住小舟 */
  const fr1=makeFurongSJ({seed:26066,n:5,m:3,w:4.6,h:2.4}); fr1.position.set(-5.5,-1.42,-13.5); g.add(fr1);
  const fr2=makeFurongSJ({seed:26067,n:4,m:2,w:4.2}); fr2.position.set(4.5,-1.42,-19); g.add(fr2);
  const fr3=makeFurongSJ({seed:26068,n:5,m:3,w:5.0,h:2.3}); fr3.position.set(-2.5,-1.42,-23.5); g.add(fr3);
  const fr4=makeFurongSJ({seed:26069,n:3,m:2,w:3.6}); fr4.position.set(9.5,-1.42,-15.5); g.add(fr4);
  /* 兰泽：两处芳洲 */
  const islet1=makeGround({r:5.5,c1:0xd5cdb2,c2:0xb8b499,y:-1.42}); islet1.mesh.position.set(-11,-1.42,-25); g.add(islet1.mesh);
  const islet2=makeGround({r:4.6,c1:0xd5cdb2,c2:0xb8b499,y:-1.42}); islet2.mesh.position.set(11.5,-1.42,-27); g.add(islet2.mesh);
  const lz1=makeLanzeSJ({seed:26074,n:14,w:3.2,h:1.7}); lz1.position.set(-11,-1.40,-25); g.add(lz1);
  const lz2=makeLanzeSJ({seed:26075,n:12,w:2.8,h:1.5}); lz2.position.set(11.5,-1.40,-27); g.add(lz2);
  /* 采莲小舟入丛（尚未采得，两手空空） */
  const boat=makeBoatSJ({seed:26093,sprig:false,face:0.5}); boat.position.set(-1.2,-1.56,-17); boat.rotation.y=0.30; g.add(boat);
  const sun=makeDanriSJ({r:6,op:0.15,haze:0.10}); sun.position.set(-46,30,-94); g.add(sun);
  const mist=makeMist({n:6,spread:[220,14,88],pos:[0,3.2,-54],scale:66,color:0xe0d9c4,op:0.10});
  g.add(mist.g);
  const dust=makeGlow({n:20,box:[140,9,56],pos:[0,3.6,-38],color:0xd8d0b4,size:3.8,speed:0.03,rise:0,add:true,maxA:0.06});
  g.add(dust.points);
  /* 前景：一丛芙蓉压右下角，坡石压左 */
  const frNear=makeFurongSJ({seed:26070,n:5,m:2,w:5.4,h:2.8}); frNear.position.set(5.5,-1.44,4.5); g.add(frNear);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:5,color:0x23262b,seed:26027,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-11,-1.8,15); g.add(fgL.g);
  addLights(g,{c:0xe4dcba,i:0.52,p:[-38,82,26]},{c:0xd6d8c6,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sun.update(t,k);
    fr1.update(t,k); fr2.update(t,k); fr3.update(t,k); fr4.update(t,k);
    lz1.update(t,k); lz2.update(t,k); boat.update(t,k);
    mist.update(t,k); dust.update(t); frNear.update(t,k); fgL.update(t,k);
  }};
}
function bYishui(){ // 贰 · 采之遗谁 —— 采之欲遗谁，所思在远道：执芳在手，望向长路尽头的空茫
  const g=new THREE.Group();
  const water=makeJiangShuiSJ({}); g.add(water.mesh);
  const ridge=makeYuanHuanSJ({seed:26028}); ridge.g.position.set(8,0,-116); g.add(ridge.g);
  const bank=makeGround({r:70,c1:0xd7d0b8,c2:0xbbb69c,y:-1.50});
  bank.mesh.scale.set(3.4,1,0.62); bank.mesh.position.set(0,-1.50,-92); g.add(bank.mesh);
  /* 长路远去，路上极小的行人剪影（所思在远道） */
  const lu=makeChangluSJ({seed:26029,x0:22,x1:-66,z0:-58,z1:-78}); g.add(lu);
  const travelers=makeCrowd({n:2,rect:[-38,-70,20,3],seed:26030,color:0x2c302c,rimC:0xcac6b2,rim:0.14,sMin:0.34,sMax:0.42,y:-1.46});
  g.add(travelers.mesh);
  /* 舟中执芳：花已采得在手（右手上），人面朝长路远去的方向（侧影） */
  const boat=makeBoatSJ({seed:26094,sprig:true,face:-2.3}); boat.position.set(1.0,-1.56,-14); boat.rotation.y=0.10; g.add(boat);
  /* 舟畔疏芙蓉两丛（已过花深处） */
  const fr1=makeFurongSJ({seed:26071,n:4,m:2,w:4.0}); fr1.position.set(-6.5,-1.42,-12); g.add(fr1);
  const fr2=makeFurongSJ({seed:26076,n:3,m:1,w:3.4}); fr2.position.set(6.5,-1.42,-4.5); g.add(fr2);
  const lz1=makeLanzeSJ({seed:26077,n:10,w:2.8,h:1.5}); lz1.position.set(-11,-1.40,-20); g.add(lz1);
  const sun=makeDanriSJ({r:6,op:0.14,haze:0.10}); sun.position.set(44,28,-92); g.add(sun);
  const mist=makeMist({n:7,spread:[230,14,88],pos:[0,3.0,-56],scale:66,color:0xded7c2,op:0.11});
  g.add(mist.g);
  const dust=makeGlow({n:18,box:[140,9,54],pos:[0,3.4,-38],color:0xd6ceB4,size:3.6,speed:0.03,rise:0,add:true,maxA:0.06});
  g.add(dust.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.6,w:11,d:5,color:0x23262b,seed:26031,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-12,-1.8,0.5); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:10,n:7,d:3,color:0x1d1f22,seed:26032,sway:0.8,tip:0x5a5648,scale:0.78});
  fgR.g.position.set(12,-1.7,1.5); g.add(fgR.g);
  addLights(g,{c:0xe0d8bc,i:0.48,p:[42,80,24]},{c:0xd4d6c6,i:0.60});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sun.update(t,k); lu.update(t,k); travelers.update(t);
    boat.update(t,k); fr1.update(t,k); fr2.update(t,k); lz1.update(t,k);
    mist.update(t,k); dust.update(t); fgL.update(t,k); fgR.update(t,k);
  }};
}
function bHuangu(){ // 叁（标志性瞬间）· 还顾旧乡 —— 还顾望旧乡，长路漫浩浩：
                    // 舟中转身回望，长路沿江岸一路远去，尽头旧乡剪影淡若烟痕
  const g=new THREE.Group();
  const water=makeJiangShuiSJ({amp:0.24}); g.add(water.mesh);
  const ridge=makeYuanHuanSJ({seed:26033}); ridge.g.position.set(-30,0,-116); g.add(ridge.g);
  const bank=makeGround({r:70,c1:0xd6cfb7,c2:0xbab59b,y:-1.50});
  bank.mesh.scale.set(3.4,1,0.62); bank.mesh.position.set(-6,-1.50,-92); g.add(bank.mesh);
  /* 长路：从近处一路远去（渐窄），岸柳夹路 */
  const lu=makeChangluSJ({seed:26034,x0:26,x1:-70,z0:-56,z1:-78,willows:9}); g.add(lu);
  /* 路上极小的行人剪影（所思在远道） */
  const travelers=makeCrowd({n:3,rect:[-46,-70,26,4],seed:26035,color:0x2c302c,rimC:0xcac6b2,rim:0.14,sMin:0.32,sMax:0.42,y:-1.46});
  g.add(travelers.mesh);
  /* 旧乡剪影：长路尽头，淡若烟痕 */
  const jiuxiang=makeJiuxiangSJ({seed:26042,op:0.26});
  jiuxiang.g.position.set(-84,-1.52,-88); jiuxiang.g.scale.setScalar(1.0); g.add(jiuxiang.g);
  /* 舟中人转身回望（face 朝长路尽头的方向） */
  const boat=makeBoatSJ({seed:26095,sprig:true,face:-2.0}); boat.position.set(4.0,-1.56,-24); boat.rotation.y=0.10; g.add(boat);
  /* 舟畔疏芙蓉（花仍执在手中） */
  const fr1=makeFurongSJ({seed:26078,n:4,m:2,w:4.0}); fr1.position.set(-4.5,-1.42,-16); g.add(fr1);
  const lz1=makeLanzeSJ({seed:26079,n:10,w:2.8,h:1.5}); lz1.position.set(10,-1.40,-19); g.add(lz1);
  const sun=makeDanriSJ({r:5.6,op:0.14,haze:0.10,color:0xefe4c8,hazeC:0xe8dcbc}); sun.position.set(-42,30,-92); g.add(sun);
  const mist=makeMist({n:6,spread:[230,13,88],pos:[-8,3.0,-58],scale:66,color:0xded7c2,op:0.11});
  g.add(mist.g);
  const dust=makeGlow({n:16,box:[140,9,52],pos:[0,3.2,-40],color:0xd6ceB4,size:3.6,speed:0.03,rise:0,add:true,maxA:0.05});
  g.add(dust.points);
  addLights(g,{c:0xdcd4b8,i:0.46,p:[-36,76,24]},{c:0xd2d4c4,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sun.update(t,k); lu.update(t,k); travelers.update(t);
    boat.update(t,k); fr1.update(t,k); lz1.update(t,k);
    mist.update(t,k); dust.update(t);
  }};
}
function bLiju(){ // 肆（末境·可点击）· 离居终老 —— 同心而离居，忧伤以终老：
                  // 点击还顾——故乡剪影淡现又缓缓远去；暮色转冷、青灰雾流漫江、双雁同飞
  const ctl={t:0,clicked:false,on:false,dusk:0};
  const g=new THREE.Group();
  const water=makeJiangShuiSJ({amp:0.22}); g.add(water.mesh);
  const ridge=makeYuanHuanSJ({seed:26038}); ridge.g.position.set(6,0,-114); g.add(ridge.g);
  const bank=makeGround({r:66,c1:0xd4cdb6,c2:0xb8b399,y:-1.50});
  bank.mesh.scale.set(3.4,1,0.62); bank.mesh.position.set(-6,-1.50,-90); g.add(bank.mesh);
  /* 长路（暮色里的来路）与路上行人剪影 */
  const lu=makeChangluSJ({seed:26039,x0:24,x1:-68,z0:-56,z1:-78,willows:7}); g.add(lu);
  const travelers=makeCrowd({n:2,rect:[-40,-70,22,3],seed:26040,color:0x2c302c,rimC:0xc4c0ae,rim:0.12,sMin:0.32,sMax:0.42,y:-1.46});
  g.add(travelers.mesh);
  /* 旧乡剪影：点击还顾的幻影——淡现又远去（点击前 visible=false 硬关，初值=峰值 0.5） */
  const xiang=makeJiuxiangSJ({seed:26043,op:0.5});
  xiang.g.position.set(-84,-1.52,-88); xiang.g.scale.setScalar(1.05);
  xiang.g.visible=false; g.add(xiang.g);
  /* 舟中执芳临暮（face 朝旧乡方向，右手上花枝向镜头示出） */
  const boat=makeBoatSJ({seed:26096,sprig:true,face:-2.2}); boat.position.set(4.0,-1.56,-14); boat.rotation.y=0.10; g.add(boat);
  const fr1=makeFurongSJ({seed:26080,n:4,m:2,w:4.0}); fr1.position.set(-5.5,-1.42,-14); g.add(fr1);
  const lz1=makeLanzeSJ({seed:26082,n:9,w:2.6,h:1.4}); lz1.position.set(10,-1.40,-21); g.add(lz1);
  /* 双雁同飞（同心之喻）：暮空缓慢横渡 */
  const yan=makeShuangyanSJ({seed:26052,v:2.2}); yan.position.set(-20,11,-64); g.add(yan);
  /* 暮日低垂、薄雾横江 */
  const sun=makeDanriSJ({r:6.2,op:0.13,haze:0.10,color:0xeee0c2,hazeC:0xe4d6ba}); sun.position.set(-50,26,-88); g.add(sun);
  const mist=makeMist({n:7,spread:[220,13,86],pos:[0,2.8,-52],scale:64,color:0xdcd5c1,op:0.11});
  g.add(mist.g);
  const dust=makeGlow({n:16,box:[130,8,50],pos:[0,3.0,-36],color:0xd2caB2,size:3.4,speed:0.03,rise:0,add:true,maxA:0.05});
  g.add(dust.points);
  /* 青灰雾流漫江（accent=#4a5a4e，点击后漫起；初值=峰值） */
  const flow=makeFlow({n:340,box:[130,10,46],pos:[0,1.6,-26],color:0x4a5a4e,size:19,speed:2.2,maxA:0.001});
  g.add(flow.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.6,w:11,d:5,color:0x23262b,seed:26041,rim:0.10,rimC:0xecead8});
  fgL.g.position.set(-12,-1.8,1.5); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:10,n:7,d:3,color:0x1d1f22,seed:26053,sway:0.7,tip:0x5a5648,scale:0.78});
  fgR.g.position.set(12,-1.7,2.5); g.add(fgR.g);
  /* 局部暮光：点击后由暖转冷（自建灯逐帧动画；初值 0.5=最大） */
  const dLight=new THREE.DirectionalLight(0xdccaa2,0.5); dLight.position.set(-44,44,16); g.add(dLight);
  addLights(g,null,{c:0xccccc0,i:0.58});
  const lw=C(0xdccaa2), lc=C(0x8b93a4);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.dusk=Math.min(1,ctl.dusk+dt/4.6);
      const e0=ctl.dusk, e=e0*e0*(3-2*e0);
      /* 点击还顾：故乡剪影淡现（0→0.45）又远去（0.45→1 渐隐并缓缓退远） */
      xiang.g.visible=k*e>0.004;
      if(xiang.g.visible){
        const inK=Math.min(1,e/0.45), outK=e<=0.45?0:(e-0.45)/0.55;
        const op=0.5*(inK*(1-0.92*outK*outK));
        xiang.mat.opacity=k*op;
        xiang.g.position.set(-84-14*outK,-1.52-1.0*outK,-88-9*outK);
      }
      /* 暮色转冷：局部光由暖转冷、渐暗；青灰雾流漫江 */
      dLight.color.copy(lw).lerp(lc,e);
      dLight.intensity=k*(0.5-0.24*e)*(0.92+0.08*Math.sin(t*0.7));
      flow.mat.uniforms.uMaxA.value=0.001+0.28*e;
      mist.update(t,k*(0.6+0.4*e));
      water.update(t); ridge.update(t,0); flow.update(t); sun.update(t,k); yan.update(t,k);
      lu.update(t,k); travelers.update(t); boat.update(t,k); fr1.update(t,k); lz1.update(t,k);
      dust.update(t); fgL.update(t,k); fgR.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.22);
        pluck(0,0.0,0.10); pluck(2,0.7,0.08); pluck(4,1.4,0.07);
        const fl=$('#flash'); fl.textContent='同心而离居 忧伤以终老';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xdcd6c4),bot:C(0xcfc7b0),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.44,
  dirP:new THREE.Vector3(-46,105,30),ambC:C(0xd4d6c4),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,16,46],t:[0,4,-28],lf:[2.5,13,-16],lt:[-3.5,8,-40]},
  sky:()=>SK({fd:0.0046,star:0.03}) },
{ name:'涉江采芳',dwell:17,river:0.02,build:bCaifang,
  cam:{f:[3.4,4.6,7.5],t:[-2.0,3.4,-17],lf:[1,4.2,-8],lt:[-3,3.6,-24]},
  sky:()=>SK({fd:0.0050,star:0.02,dirC:C(0xe4dcba),dirI:0.50,
    dirP:new THREE.Vector3(-38,88,26),ambC:C(0xd6d8c6),ambI:0.62}) },
{ name:'采之遗谁',dwell:15,river:0.02,build:bYishui,
  cam:{f:[1.5,4.5,2],t:[-2.5,4.0,-18],lf:[0.5,4.3,-6],lt:[-3.5,3.9,-26]},
  sky:()=>SK({fd:0.0052,dirC:C(0xe0d8bc),dirI:0.46,
    dirP:new THREE.Vector3(42,84,24),ambC:C(0xd4d6c6),ambI:0.60}) },
{ name:'还顾旧乡',dwell:19,river:0.02,build:bHuangu,
  cam:{f:[9.5,5.2,-9],t:[-10,3.4,-36],lf:[2,4.8,-18],lt:[-7,3.4,-42]},
  sky:()=>SK({fd:0.0054,hor:C(0xd6cfb8),dirC:C(0xdcd4b8),dirI:0.44,
    dirP:new THREE.Vector3(-36,76,24),ambC:C(0xd2d4c4),ambI:0.58}) },
{ name:'离居终老',dwell:21,river:0.02,build:bLiju,
  cam:{f:[9,4.9,-2],t:[-6,2.9,-30],lf:[5,4.5,-8],lt:[-8,3.0,-38]},
  sky:()=>SK({fd:0.0064,hor:C(0xd2cab2),dirC:C(0xd4cbb0),dirI:0.42,
    dirP:new THREE.Vector3(-44,70,18),ambC:C(0xccccc0),ambI:0.58}) },
];
"""

if __name__ == '__main__':
    print('shejiang-caifurong.py —— 被 build.py 消费：python build.py shejiang-caifurong')
