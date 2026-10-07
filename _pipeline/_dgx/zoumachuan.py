# -*- coding: utf-8 -*-
"""zoumachuan.py —— 《走马川行奉送封大夫出师西征》（唐·岑参，queue no.264，大漠金戈）生成配置
四境（N=4，6 分句 [2,2,1,1]）：
壹 雪海莽沙（君不见走马川行雪海边……随风满地石乱走——标志性瞬间：走马川干河床上
  一川碎石大如斗随风满地石乱走，平沙莽莽黄入天+雪海远带+风夜吼），
贰 出师夜行（匈奴草黄马正肥……风头如刀面如割——金山烟尘飞+夜行军火把长龙+
  将军金甲夜不脱按剑立马+旌旗横卷+风头如刀疾流），
叁 汗气成冰（马毛带雪汗气蒸，五花连钱旋作冰，幕中草檄砚水凝——奇寒之夜：
  战马汗气成冰白雾蒸腾+冰斑寒光+中军大帐草檄砚水凝冷光，全页最冷一境），
肆 车师献捷（虏骑闻之应胆慑……车师西门伫献捷——末境可点击：车师西门城楼旌旗伫候+
  曙色初临。交互：点击石乱走——碎石风暴卷地而起+风声+行军队伍迎风疾进幻影，题字同现，
  可反复点击）。
美术立意「风是主角」：全页一切物象都在风里——横扫的沙尘流、满地乱滚的大如斗碎石、
被吹折横卷的旌旗、迎风的火把长龙、马毛上蒸腾又凝冰的汗气；走马川干河床+
碎石阵是舞台本体，「石乱走」是全页的心跳。时间线：风夜吼（壹）→ 夜行军（贰）→
奇寒中夜（叁）→ 破晓献捷（肆），天色由黄尘蔽月到星寒霜白再到天际微明。
大漠金戈全套色板：底色 #120d08、雾 #190f08～#1d140b 系、文字 #f0e2cc，accent=#c9a06a
（queue 分配强调色，沙金）只落在 UI/人物边缘光/火把光/旗面光边/碎石风暴幻影/献捷曙色上，
禁艳金。与已有边塞页第一眼可区分：不做雪原牧马听笛（saishang-chuidi）、不做拂晓誓师整甲
（wuyi）、不做密林夜射（saixiaqu-linan）、不做金甲烽燧孤城（congjunxing-yumen）、
不做木兰人生长卷（mulanci）、不做牙帐对切（yange-xing）——本页是**狂风卷石的走马川夜行军**：
无人做到过「风夜吼+石乱走」的风之动势第一帧。
标志性瞬间（境壹·queue moment：一川碎石大如斗随风满地石乱走）：低机位沿干河床看风——
满川碎石大如斗，走石沿风向翻滚弹跳、静石震颤摇撼，黄尘平沙黄入天，雪海远带在侧。
末境点击（queue interact：点击石乱走——碎石风暴）：点击画面——
①碎石风暴幻影卷地而起（腾空翻卷的石阵+卷石沙尘暴+风暴风声流，加色幻影）；
②行军队伍迎风疾进幻影（火把长龙自画右向车师西门推进）；
③「一川碎石大如斗 随风满地石乱走」题字同现+五声风吼鼓点，可反复点击。
考点钉子：莽莽 mǎng／檄 xí／伫 zhù／慑 shè／虏骑 jì／旋 xuán／斗 dǒu（小测第 3 题落点）；
岑参边塞诗（与高适并称「高岑」）+走马川/雪海/轮台/车师西域地名+歌行体（第 4 题）；
奇丽壮阔的边塞风物与金甲夜不脱的军威、料敌胆慑伫献捷的必胜信心（第 5 题）。
多音字：走马川行→走马川型 大如斗→大如抖 旋作冰→悬作冰 草檄→草习 虏骑→虏寄
应胆慑→鹰胆慑 伫献捷→住献捷 岑参→岑身（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='zoumachuan', title='走马川行奉送封大夫出师西征', dyn='唐 · 岑参', brand_author='岑 参',
    gold_rgb='201,160,106',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#c9a06a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(201,160,106,.3);
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
        ('0x0a1526', '0x1a1209', 4),
    ],
    tip='轻点画面 / 按空格 —— 碎石风暴卷地而起，行军队伍迎风疾进',
    hint='← → 键或空格逐境游览 · 末境可点击画面：碎石风暴卷地而起，风声里看行军队伍迎风疾进',
    cover_read='走马川行奉送封大夫出师西征。唐，岑参。君不见走马川行雪海边，平沙莽莽黄入天。轮台九月风夜吼，一川碎石大如斗，随风满地石乱走。将军金甲夜不脱，半夜军行戈相拨，风头如刀面如割。虏骑闻之应胆慑，车师西门伫献捷。',
    cover_p1='四重意境，随诗句次第展开：君不见走马川行雪海边，平沙莽莽黄入天——轮台九月风夜吼，一川碎石大如斗，随风满地石乱走；匈奴草黄马正肥，金山西见烟尘飞，汉家大将西出师——将军金甲夜不脱，半夜军行戈相拨，风头如刀面如割；马毛带雪汗气蒸，五花连钱旋作冰，幕中草檄砚水凝；虏骑闻之应胆慑，料知短兵不敢接，车师西门伫献捷。',
    cover_p2='边读诗，边跟着大军走进轮台九月的狂风夜：风是全诗的主角——吹得满川碎石大如斗随风乱走、吹得旌旗横卷、风头如刀；风愈狂、寒愈极，愈显出「金甲夜不脱」的军威。读懂「料知短兵不敢接」的侧面烘托与「伫献捷」的必胜豪情，就读懂了岑参奇气奇境的边塞歌行。',
    end_h2='石走 · 献捷', cn_word='肆',
    words_js="['再入一次走马川','初识岑参，尚需共读','渐入诗境，再诵几遍','风吼石走，夜行如铁','汗气成冰，军心愈壮','已解碎石狂风之壮']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'雪海莽沙', jing:'你可曾见过走马川在雪海边奔行而过，茫茫平沙、浩浩黄尘直卷上天际？轮台的九月，狂风整夜怒吼——走马川中满川的碎石个个大如斗，被风卷得满地乱滚、四散乱走。（君不见 · 雪海边 · 平沙莽莽 · 风夜吼 · 石乱走）（标志性瞬间：一川碎石大如斗，随风满地石乱走）',
  segs:[
   {c:'君不见走马川行雪海边，', p:py('jūn bú jiàn zǒu mǎ chuān xíng xuě hǎi biān')},
   {c:'平沙莽莽黄入天。', p:py('píng shā mǎng mǎng huáng rù tiān')},
   {c:'轮台九月风夜吼，', p:py('lún tái jiǔ yuè fēng yè hǒu')},
   {c:'一川碎石大如斗，', p:py('yī chuān suì shí dà rú dǒu')},
   {c:'随风满地石乱走。', p:py('suí fēng mǎn dì shí luàn zǒu')}],
  read:'君不见走马川行雪海边，平沙莽莽黄入天。轮台九月风夜吼，一川碎石大如斗，随风满地石乱走。',
  yisi:'开篇便是一声惊呼：「君不见」——你可曾见过？走马川在雪海之畔奔行，茫茫平沙一望无际，黄尘莽莽直卷上天。接着写风：轮台的九月，狂风在深夜里怒吼——一个「吼」字，风便有了声威；风声之后写风势的实证：一川碎石大如斗，被狂风卷得满地乱滚、四散奔走。石头本是无情之物，此刻却像活了——诗人不写风如何吹，只让石头自己「走」给你看：风之狂、地之荒、天之寒，全在这满川乱走的碎石里。以奇景压卷、以夸张取胜，正是岑参边塞歌行「奇气奇境」的本色。',
  zhu:[['君不见','乐府歌行习用语，犹言「你可曾看见」——劈头一呼，领起全篇奇景'],['走马川','西域地名（河流名，一说即今新疆车尔臣河一带）——「行」是歌行体标志，题目即「走马川歌」'],['雪海','西域地名，泛指终年积雪、苦寒多雪之地'],['平沙莽莽','茫茫平沙无边无际。莽莽，广袤无际的样子，读 mǎng mǎng'],['黄入天','黄尘沙雾直卷上天际——天地一片昏黄，极写大漠风尘之烈'],['轮台','唐代安西、北庭辖地（在今新疆境内），当时岑参封常清幕府驻地。轮，读 lún'],['风夜吼','狂风在深夜怒吼——「吼」字赋风以声势，为「石乱走」张本'],['斗','古代量器，十升为一斗——「大如斗」极言碎石之巨，读 dǒu'],['石乱走','石头被狂风卷得满地乱滚——以石写风：风不见其形而风势自见，是全诗最惊人的一笔']] },
{ name:'出师夜行', jing:'匈奴的草已枯黄，战马正养得肥壮——金山的西面，望见敌人的烟尘滚滚飞来；汉家的大将，正奉命挥师西征。将军的铠甲夜里也不解下，半夜行军，长戈在暗中相碰作响；风头凶猛如刀，迎面割得人脸生疼。（敌情 · 烟尘飞 · 西出师 · 金甲夜不脱 · 风如刀）',
  segs:[
   {c:'匈奴草黄马正肥，', p:py('xiōng nú cǎo huáng mǎ zhèng féi')},
   {c:'金山西见烟尘飞，', p:py('jīn shān xī jiàn yān chén fēi')},
   {c:'汉家大将西出师。', p:py('hàn jiā dà jiàng xī chū shī')},
   {c:'将军金甲夜不脱，', p:py('jiāng jūn jīn jiǎ yè bù tuō')},
   {c:'半夜军行戈相拨，', p:py('bàn yè jūn xíng gē xiāng bō')},
   {c:'风头如刀面如割。', p:py('fēng tóu rú dāo miàn rú gē')}],
  read:'匈奴草黄马正肥，金山西见烟尘飞，汉家大将西出师。将军金甲夜不脱，半夜军行戈相拨，风头如刀面如割。',
  yisi:'镜头从风沙转向军情：匈奴草黄马正肥——秋草枯黄正是马肥之时，也是游牧铁骑最剽悍之时，敌情如火；金山西面烟尘飞扬，敌骑蠢蠢欲动，一声「汉家大将西出师」，大军迎敌而上。接着是夜行军的三笔特写：「金甲夜不脱」，是枕戈待旦的常备不懈；「半夜军行戈相拨」，黑夜衔枚疾走，只闻长戈轻轻相碰——静中有声，军纪森严；「风头如刀面如割」，呼应有时的「风夜吼」，狂风扑面如刀，而队伍一刻不停。敌愈强、夜愈黑、风愈狂，愈显出这支军队闻警即动、严整无畏的军威——全为末境「虏骑胆慑」的预想张本。',
  zhu:[['匈奴','汉代北方游牧民族，唐人诗中借指当时西域的敌对部落'],['草黄马正肥','秋草枯黄、战马养肥——游牧骑兵草肥马壮之时最为剽悍，点出敌情紧迫'],['金山','即阿尔泰山，蒙语「阿尔泰」意为金——「金山西见烟尘飞」：金山以西望见敌骑烟尘飞扬，敌情已至'],['汉家大将','借汉指唐，指封常清（时任安西、北庭节度使，封御史大夫）——题中「封大夫」即其人'],['西出师','向西出兵征讨'],['金甲','铠甲的美称——「夜不脱」即夜不解甲，写主帅常备不懈、与士卒同甘苦'],['戈相拨','兵器互相轻轻碰击。拨，碰击——黑夜行军衔枚疾走，唯闻戈矛相拨之声，见军纪之严'],['风头如刀','风势迎面扑来凶猛如刀锋——「面如割」与境壹「风夜吼」相呼应，风之烈贯穿行军全程']] },
{ name:'汗气成冰', jing:'战马毛上带着落雪，奔驰的汗气却从毛间蒸腾而出，转眼又在毛尖凝成了冰；五花连钱的骏马身披霜雪，汗水旋即结作冰花。中军帐里连夜起草声讨的檄文，连砚台里的墨水都冻结了。（马毛带雪 · 汗气蒸 · 旋作冰 · 草檄 · 砚水凝）',
  segs:[
   {c:'马毛带雪汗气蒸，', p:py('mǎ máo dài xuě hàn qì zhēng')},
   {c:'五花连钱旋作冰，', p:py('wǔ huā lián qián xuán zuò bīng')},
   {c:'幕中草檄砚水凝。', p:py('mù zhōng cǎo xí yàn shuǐ níng')}],
  read:'马毛带雪汗气蒸，五花连钱旋作冰，幕中草檄砚水凝。',
  yisi:'这一境把「寒」写到了极致，也写出了奇趣：马毛上挂着风送来的雪花，可马身奔驰的汗气仍旧蒸腾而上——一寒一热在马毛尖上相激，汗气旋即凝作冰霜。五花连钱的骏马，转眼披上了一身冰甲。帐外的马尚且如此，帐内呢？连夜起草讨敌檄文的砚台，墨水都冻结了——由马及人、由帐外到帐内，三句一层紧似一层。妙在热气愈蒸、寒意愈烈：汗气蒸、砚水凝两相对照，奇寒之境反写出了人马勃发的热气——这支军队连严寒都压不垮。',
  zhu:[['马毛带雪汗气蒸','马毛上带着雪花，汗气仍自毛间蒸腾——奇寒与热气相激，是全诗最富质感的一笔'],['五花','毛色呈五色花纹的名马（一说指马鬃剪饰成五瓣的花样）'],['连钱','毛色斑驳如连缀铜钱的名马——「五花连钱」泛指骏马'],['旋作冰','旋即结成冰。旋，随即、立刻，读 xuán——汗气在马毛上立刻凝为冰霜'],['幕','军帐、幕府'],['草檄','起草声讨敌人的文书。檄，古代官方征讨、晓谕的文书，读 xí'],['砚水凝','砚台里的墨水都冻结了——以帐内小物写彻骨奇寒，笔墨极省而寒意极重']] },
{ name:'车师献捷', jing:'敌人的骑兵听说大军西来，想必早已胆战心惊——料定他们不敢短兵相接；此刻只须在车师西门，伫候将军献上凯旋的捷报。（虏骑胆慑 · 短兵不敢接 · 伫献捷 · 末境点击画面：碎石风暴卷地而起，行军队伍迎风疾进）',
  segs:[
   {c:'虏骑闻之应胆慑，', p:py('lǔ jì wén zhī yīng dǎn shè')},
   {c:'料知短兵不敢接，', p:py('liào zhī duǎn bīng bù gǎn jiē')},
   {c:'车师西门伫献捷。', p:py('chē shī xī mén zhù xiàn jié')}],
  read:'虏骑闻之应胆慑，料知短兵不敢接，车师西门伫献捷。',
  yisi:'结尾三句不写一战而胜局已定：敌人的骑兵听说汉家大军冒风雪西来——那支金甲夜不脱、半夜衔枚疾进的队伍——想必早已吓破了胆；料定他们不敢短兵相接。于是车师西门，众人伫候的已不是战报，而是捷报。全诗从头到尾没有写一场厮杀：风夜吼、石乱走是「势」，金甲不脱、戈相拨是「威」，虏骑胆慑、短兵不敢接是把这势与威推到敌营里去的回声——以未战写必胜，以预想收束全篇，既见主帅声威，也见诗人对这次西征满溢的信心。送行诗写出了凯旋曲的调子，正是此诗最豪迈处。',
  zhu:[['虏骑','敌人的骑兵。虏，对敌方的蔑称；骑，读 jì'],['闻之','听说（汉家大军出师西征）的消息'],['应胆慑','料想必已吓破胆。应，料想、想必，读 yīng；慑，恐惧、害怕，读 shè'],['料知','料定、断定'],['短兵不敢接','不敢短兵相接——不战而屈人之兵，从侧面写大军声威之盛'],['车师','西域古国名（汉车师故地，唐为西州、庭州一带，在今新疆吐鲁番盆地），此指唐军驻地'],['伫','久立等待，读 zhù——「伫献捷」：在西门伫候将军献捷'],['献捷','战胜后进献战利品、报捷——以必胜的预想作结，送行诗写出了凯旋的调子']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「君不见走马川行雪海边」的下一句是？', o:['平沙莽莽黄入天','轮台九月风夜吼','一川碎石大如斗'], a:0},
 {q:'「一川碎石大如斗」的下一句是？', o:['随风满地石乱走','平沙莽莽黄入天','料知短兵不敢接'], a:0},
 {q:'「平沙莽莽黄入天」「幕中草檄砚水凝」「车师西门伫献捷」三句中加点字的读音与解释，完全正确的一项是？', o:['莽莽读 mǎng，广袤无际；檄读 xí，声讨敌人的文书；伫读 zhù，久立等待','莽莽读 māng，黄沙弥漫；檄读 yì，军事密信；伫读 chù，站立不安','莽莽读 mǎng，山峰重叠；檄读 jiǎo，缴获的文书；伫读 zhù，储备粮草'], a:0},
 {q:'关于这首诗的作者与「走马川」，下列说法正确的是？', o:['岑参是盛唐边塞诗人，两度出塞入戎幕，与高适并称「高岑」；走马川、雪海、轮台、车师都是西域地名，「走马川行」的「行」表示这是歌行体','岑参是盛唐山水田园诗人，与王维并称「王孟」；走马川是长安附近的狩猎场','此诗作于岑参进士及第之前居家时，「走马川」是虚构的乌有之乡，「封大夫」即杜甫'], a:0},
 {q:'全诗从狂风卷石的走马川写到「虏骑闻之应胆慑，料知短兵不敢接，车师西门伫献捷」，对主旨理解最恰当的一项是？', o:['写奇丽壮阔的边塞风物与连夜顶风冒寒西征的军旅生活——风愈狂、寒愈极，愈显唐军将士金甲夜不脱的英姿；料敌胆慑、伫候献捷，洋溢着必胜的信心与豪迈气概','抱怨西征路途过于艰险，暗讽封大夫穷兵黩武、驱士卒于风雪而不顾','纯粹记录轮台九月的自然风光，狂风碎石只是气象实录，与出师送行无关'], a:0},
];
"""

SCENES_JS = """/* ================= 走马川行 · 四境场景（大漠金戈·狂风卷石的走马川夜行军：雪海莽沙、出师夜行、汗气成冰、车师献捷） =================
   美术立意：风是主角——轮台九月风夜吼：横扫的沙尘流、满地乱滚的大如斗碎石、
   被吹得横卷的旌旗、迎风的火把长龙、马毛上蒸腾又凝冰的汗气，全页一切物象都在风里。
   大漠金戈色板：底色 #120d08、雾 #190f08～#1d140b 系，accent=#c9a06a 只落在
   UI/人物边缘光/火把光/旗面光边/碎石风暴幻影/献捷曙色上，禁艳金。
   与已有边塞页第一眼可区分：不做雪原牧马听笛（saishang-chuidi）、不做拂晓誓师整甲（wuyi）、
   不做密林夜射（saixiaqu-linan）、不做金甲烽燧孤城（congjunxing-yumen）、不做人生长卷（mulanci）、
   不做牙帐对切（yange-xing）——本页是**狂风卷石的走马川夜行军**：
   走马川干河床+大如斗碎石阵是舞台本体，「石乱走」是全页的心跳。 */

/* —— 走马川基底 makeZmcBase(o)：斑驳大漠地面 + 两层台地远山
   远山放 z≈-120/-66，在骨架常驻远山环（z≈-260…-330）之前，不被遮挡 */
function makeZmcBase(o){
  o=o||{};
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:o.c1===undefined?0x150e07:o.c1,c2:o.c2===undefined?0x261809:o.c2,
    y:o.gy===undefined?-1.8:o.gy});
  g.add(grd.mesh);
  const ridge=makeRange({r:310,h:o.h1===undefined?15:o.h1,layers:2,peaks:o.p1===undefined?4:o.p1,
    seed:o.seed1===undefined?26451:o.seed1,color:0x0d0906,atmo:0x2e2114,fogK:0.62,glowK:0.06,
    glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(o.r1x===undefined?-16:o.r1x,0,o.r1z===undefined?-120:o.r1z);
  ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:250,h:o.h2===undefined?9:o.h2,layers:2,peaks:3,
    seed:o.seed2===undefined?26452:o.seed2,color:0x0a0704,atmo:0x2e2114,fogK:0.58,glowK:0.04,
    glow:0xd8a860,y:-9,order:-5});
  ridge2.g.position.set(o.r2x===undefined?24:o.r2x,0,o.r2z===undefined?-66:o.r2z);
  ridge2.g.rotation.y=Math.PI*0.9; g.add(ridge2.g);
  return {g:g,grd:grd,ridge:ridge,ridge2:ridge2};
}

/* —— 走马川河床 makeZmcHebedJS(o)：蜿蜒干河床（Plane 顶点沿 x 正弦抬出蜿蜒浅槽，
   浅色戈壁底与地面区分）——「君不见走马川行雪海边」：全页舞台本体，合批 1 mesh */
function makeZmcHebedJS(o){
  o=o||{};
  const L=o.L===undefined?130:o.L, W=o.W===undefined?28:o.W;
  const geo=new THREE.PlaneGeometry(L,W,30,8);
  geo.rotateX(-Math.PI/2);
  const pos=geo.attributes.position, amp=o.amp===undefined?3.8:o.amp;
  const ph=(o.seed===undefined?26401:o.seed)%6.283;
  for(let i=0;i<pos.count;i++){
    const x=pos.array[i*3];
    pos.array[i*3+2]=Math.sin(x*0.05+ph)*amp;
  }
  geo.computeVertexNormals();
  const mesh=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:o.color===undefined?0x3a2a16:o.color,
    emissive:0x120b04}));
  mesh.position.set(o.x===undefined?0:o.x,o.y===undefined?-1.76:o.y,o.z===undefined?-8:o.z);
  mesh.renderOrder=0;
  const g=new THREE.Group(); g.add(mesh);
  g.userData.update=function(t,k){ g.visible=(k===undefined?1:k)>0.004; };
  return g;
}

/* —— 碎石阵 makeZmcShikeJS(o)：一川碎石大如斗（InstancedMesh 1 draw call，双石合体
   原型+顶点色）。walk 比例的走石沿风向翻滚弹跳、出界回绕（「随风满地石乱走」），
   其余静石震颤摇撼；update(t,k,storm)：storm 供末境点击——全部石子腾空卷起（碎石风暴） */
function makeZmcShikeJS(o){
  o=o||{};
  const n=o.n===undefined?84:o.n;
  const R=seedRnd(o.seed===undefined?26411:o.seed);
  const box=o.box===undefined?{cx:0,cz:-8,x:100,z:28}:o.box;
  const sMin=o.sMin===undefined?0.42:o.sMin, sMax=o.sMax===undefined?1.8:o.sMax;
  const walk=o.walk===undefined?0.34:o.walk;
  const g=new THREE.Group();
  const B=new GeoBag();
  const rk=new THREE.IcosahedronGeometry(1,0); rk.translate(0,0.16,0); B.put(rk,0x33261a);
  const rk2=new THREE.IcosahedronGeometry(0.55,0); rk2.translate(0.5,0.5,0.28); B.put(rk2,0x241a10);
  const rock=mergeGeos(B.list);
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a4030,emissive:0x070503}),{c:0xc9a06a,i:o.rim===undefined?0.18:o.rim,p:2.4});
  const mesh=new THREE.InstancedMesh(rock,mat,n);
  mesh.frustumCulled=false; mesh.renderOrder=1;
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    const mv=R()<walk;
    items.push({x0:box.cx+(R()-0.5)*box.x, z:box.cz+(R()-0.5)*box.z,
      s:sMin+R()*(sMax-sMin), v:mv?(1.5+R()*2.4):0, r0:R()*6.283, ph:R()*6.283,
      hop:1.1+R()*2.2, rx:(R()-0.5)*2.4, ry:(R()-0.5)*2.4});
  }
  g.add(mesh);
  g.userData.update=function(t,k,storm){
    const kk=k===undefined?1:k, st=storm===undefined?0:storm;
    const half=box.x*0.5;
    for(let i=0;i<n;i++){
      const it=items[i];
      let x,y,spin;
      if(st>0.004){
        const prog=((t*(0.10+it.hop*0.035)*st)+it.ph)%1;
        x=box.cx-half+prog*box.x;
        y=Math.sin(prog*Math.PI)*it.s*(1.4+it.hop)*st;
        spin=t*(1.4+it.hop*0.5);
      }else if(it.v>0){
        let w=(it.x0-half+box.cx+t*it.v)%box.x;
        if(w<0)w+=box.x;
        x=box.cx-half+w;
        y=Math.abs(Math.sin(t*it.hop+it.ph))*0.34;
        spin=t*it.v*0.9;
      }else{
        x=it.x0+Math.sin(t*1.3+it.ph)*0.06;
        y=0;
        spin=it.r0+Math.sin(t*0.7+it.ph)*0.05;
      }
      dm.position.set(x,y,it.z);
      dm.rotation.set(it.rx+spin*0.6,it.r0+spin*0.4,it.ry);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 雪海远带 makeZmcXuehaiJS(o)：左侧天际泛白寒带（长条淡色低丘+雪霰微粒）——
   「君不见走马川行雪海边」的雪海一侧 */
function makeZmcXuehaiJS(o){
  o=o||{};
  const g=new THREE.Group();
  const x=o.x===undefined?-64:o.x, z=o.z===undefined?-102:o.z;
  const band=new THREE.Mesh(new THREE.BoxGeometry(o.w===undefined?120:o.w,2.4,7),
    new THREE.MeshLambertMaterial({color:0x62625c,emissive:0x1e201c}));
  band.position.set(x,o.y===undefined?-0.4:o.y,z); band.renderOrder=-4; g.add(band);
  const sp=makeGlow({n:o.n===undefined?22:o.n,box:[110,9,26],pos:[x,5.5,z+24],
    color:0x9aa09e,size:2.2,speed:0.08,rise:-0.08,add:false,maxA:0.10});
  sp.points.renderOrder=3; g.add(sp.points);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    sp.update(t);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 军旗 makeZmcQiJS(o)：高杆+旄缨+横长旗面（Plane 顶点波动，accent 顶边光），
   wind>1 为狂风横卷——「旌旆」「辕门」之旗（杆合批 1 mesh，旗布 1 mesh） */
function makeZmcQiJS(o){
  o=o||{};
  const H=o.H===undefined?7.0:o.H, W=o.W===undefined?2.4:o.W, Hh=o.Hh===undefined?1.5:o.Hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.06,0.095,H,6);
  pole.translate(-W/2-0.3,H/2,0); B.put(pole,0x2e2010);
  const mao=new THREE.ConeGeometry(0.12,0.5,6);
  mao.translate(-W/2-0.3,H+0.22,0); B.put(mao,0xcabb9a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x5a4224,emissive:0x060402}),{c:0xc9a06a,i:o.rim===undefined?0.20:o.rim,p:2.5})));
  const geo=new THREE.PlaneGeometry(W,Hh,10,4);
  geo.translate(W/2+0.02,0,0);
  const base=geo.attributes.position.array.slice(), cnt=geo.attributes.position.count;
  const cols=new Float32Array(cnt*3);
  const cb=new THREE.Color(0x3a2410), ca=new THREE.Color(0xc9a06a);
  for(let i=0;i<cnt;i++){
    const y=base[i*3+1];
    const tt=Math.max(0,((y+Hh/2)/Hh-0.66)/0.34);
    const c=cb.clone().lerp(ca,tt*0.62);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(cols,3));
  const flag=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,emissive:0x140b05}));
  flag.position.y=H-Hh/2-0.55; g.add(flag);
  const pos=geo.attributes.position, ph=(o.seed===undefined?26402:o.seed)%6.283;
  g.userData.update=function(t,k,wind){
    const kk=k===undefined?1:k, wd=(wind===undefined?1:wind)*kk;
    for(let i=0;i<pos.count;i++){
      const bx=base[i*3], by=base[i*3+1], f=bx/W;
      pos.array[i*3+2]=Math.sin(bx*1.9-t*4.6+by*0.9+ph)*0.34*f*f*wd;
      pos.array[i*3+1]=by-Math.abs(Math.sin(bx*1.5-t*3.6+ph))*0.10*f*f*wd;
    }
    pos.needsUpdate=true;
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 低模战马 makeZmcMaJS(o)：躯干/四腿/短颈/头/耳/尾/鬃（GeoBag 合批 1 mesh，
   头颈前探收敛避「长颈鹿化」）；steam:true 汗气白雾（makeGlow 缓升）——
   「五花连钱」骏马、「马毛带雪汗气蒸」 */
function makeZmcMaJS(o){
  o=o||{};
  const s=o.s===undefined?1:o.s;
  const coat=o.coat===undefined?0x2c2114:o.coat, dk=shadeColor(coat,0.72);
  const B=new GeoBag();
  const bd=new THREE.SphereGeometry(1.5,10,8);
  bd.scale(1.5*s,1.0*s,0.7*s); bd.translate(0,3.0*s,0); B.put(bd,coat);
  const legR=0.16*s, legT=2.3*s;
  [[1.0,0.34],[1.0,-0.36],[-1.05,0.35],[-1.05,-0.37]].forEach(function(p){
    const lg=new THREE.CylinderGeometry(legR*0.8,legR,legT,5);
    lg.translate(p[0]*s,legT*0.5,p[1]*s); B.put(lg,dk);
  });
  B.put(limbGeo([1.5*s,3.6*s,0],[2.35*s,4.9*s,0],0.56*s,0.30*s,6),coat);
  const hd=new THREE.SphereGeometry(0.42*s,8,6);
  hd.scale(1.5,0.9,0.7); hd.translate(2.85*s,4.95*s,0); B.put(hd,dk);
  const muz=new THREE.ConeGeometry(0.15*s,0.46*s,6);
  muz.rotateZ(-Math.PI/2-0.15); muz.translate(3.5*s,4.8*s,0); B.put(muz,shadeColor(coat,0.6));
  for(let e=0;e<2;e++){
    const ear=new THREE.ConeGeometry(0.09*s,0.30*s,4);
    ear.translate(2.5*s,5.4*s,(e?0.14:-0.14)*s); B.put(ear,dk);
  }
  B.put(limbGeo([-2.2*s,3.7*s,0],[-2.9*s,2.0*s,0],0.24*s,0.05*s,5),dk);
  B.put(limbGeo([1.35*s,4.6*s,0],[2.4*s,4.5*s,0],0.14*s,0.05*s,5),shadeColor(coat,0.5));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a2014,emissive:0x040302}),{c:0xc9a06a,i:o.rim===undefined?0.18:o.rim,p:2.2})));
  let steam=null;
  if(o.steam){
    steam=makeGlow({n:10,box:[1.5,2.0,1.1],pos:[0,4.4*s,0],color:o.steamC===undefined?0xc3d0d8:o.steamC,
      size:1.8,speed:0.05,rise:1,add:false,maxA:0.26});
    steam.points.renderOrder=3; g.add(steam.points);
  }
  const ph=(o.seed===undefined?26412:o.seed)%6.283;
  g.scale.setScalar(1);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.006*Math.sin(t*0.9+ph)*kk;
    if(steam)steam.update(t);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 夜行军长龙 makeZmcXingjunJS(o)：低模行军士一列（长衣+皮甲+圆盔，两臂前伸执戈，
   GeoBag 分 2 组合批）；o.pts 为 [x,z,ry] 队列点位（蜿蜒行军线），torch:true 加把杆+火头；
   ghost:true 为末境幻影态（加色半透，无边缘光）——「半夜军行戈相拨」「汉家大将西出师」 */
function makeZmcXingjunJS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26421:o.seed);
  const pts=o.pts||[[0,0,0]];
  const torch=o.torch===undefined?false:o.torch;
  const ghost=o.ghost===undefined?false:o.ghost;
  const bags=[new GeoBag(),new GeoBag()];
  for(let i=0;i<pts.length;i++){
    const B=bags[i%2];
    const p=pts[i], x=p[0]+(R()-0.5)*0.6, z=p[1]+(R()-0.5)*0.6, ry=p[2]+(R()-0.5)*0.22;
    const robe=[0x221810,0x281c10,0x1d150b,0x2b1f12][Math.floor(R()*4)];
    const dk=shadeColor(robe,0.74);
    const bd=new THREE.CylinderGeometry(0.25,0.44,1.5,6);
    bd.rotateY(ry); bd.translate(x,0.75,z); B.put(bd,robe);
    const jia=new THREE.CylinderGeometry(0.34,0.42,0.44,6);
    jia.rotateY(ry); jia.translate(x,1.12,z); B.put(jia,0x33261a);
    const hd=new THREE.SphereGeometry(0.15,6,5);
    hd.translate(x,1.68,z); B.put(hd,0x8a6a48);
    const kh=new THREE.SphereGeometry(0.175,6,5,0,Math.PI*2,0,Math.PI/2);
    kh.scale(1,0.9,1); kh.translate(x,1.66,z); B.put(kh,0x221b12);
    const ca=Math.cos(ry), sa=Math.sin(ry);
    const ox=function(dx){return dx*ca;}, oz=function(dx){return -dx*sa;};
    B.put(limbGeo([x+ox(-0.30),1.28,z+oz(-0.30)+0.14],[x+ox(-0.08),1.02,z+oz(-0.08)+0.40],0.065,0.048,5),dk);
    B.put(limbGeo([x+ox(0.30),1.28,z+oz(0.30)+0.14],[x+ox(0.10),1.00,z+oz(0.10)+0.40],0.065,0.048,5),dk);
    const sp=new THREE.CylinderGeometry(0.024,0.032,3.0,5);
    sp.rotateZ(0.28); sp.rotateY(ry);
    sp.translate(x+ox(-0.28),1.60,z+oz(-0.28)+0.22); B.put(sp,0x40301c);
    const tp=new THREE.ConeGeometry(0.05,0.26,5);
    tp.rotateZ(0.28); tp.rotateY(ry);
    tp.translate(x+ox(-0.28)-Math.sin(0.28)*1.45*ca,1.60+Math.cos(0.28)*1.45,z+oz(-0.28)+0.22-Math.sin(0.28)*1.45*(-sa));
    B.put(tp,0x7a6a44);
    if(torch){
      const tg=new THREE.CylinderGeometry(0.03,0.04,0.9,5);
      tg.rotateZ(0.12); tg.rotateY(ry);
      tg.translate(x+ox(0.30),1.35,z+oz(0.30)+0.20); B.put(tg,0x3a2a16);
      const th=new THREE.ConeGeometry(0.06,0.17,5);
      th.translate(x+ox(0.30)+Math.sin(0.12)*0.45*ca,1.35+0.45+Math.cos(0.12)*0.20,z+oz(0.30)+0.20);
      B.put(th,0x8a5a26);
    }
  }
  const g=new THREE.Group(), meshes=[];
  for(let i=0;i<2;i++){
    let m;
    if(ghost){
      m=bags[i].mesh(new THREE.MeshBasicMaterial({color:0xd8a874,transparent:true,
        opacity:0.22,depthWrite:false,blending:THREE.AdditiveBlending}));
    }else{
      m=bags[i].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
        shininess:5,specular:0x2a2014,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.15:o.rim,p:2.2}));
    }
    g.add(m); meshes.push(m);
  }
  const ph=R()*6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<2;i++) meshes[i].position.y=0.07*Math.sin(t*2.2+i*1.7+ph)*kk;
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 中军大帐 makeZmcDazhangJS(o)：帐架（双坡帐顶+脊杆+四柱+围裙帐裙）+帐门暖光+
   案上「砚水凝」冷光点（accent 青金之外的冷青 Sprite+帐内冷点光）——
   「幕中草檄砚水凝」：全页唯一一处暖门光与冷砚光同框（合批 1 mesh+2 Sprite+1 PointLight） */
function makeZmcDazhangJS(o){
  o=o||{};
  const W=o.W===undefined?7.5:o.W, D=o.D===undefined?5.2:o.D, H=o.H===undefined?3.1:o.H;
  const B=new GeoBag();
  const roofL=new THREE.BoxGeometry(W*0.60,0.22,D+1.0);
  roofL.rotateZ(0.50); roofL.translate(-W*0.235,H-0.30,0); B.put(roofL,0x3c2b18);
  const roofR=new THREE.BoxGeometry(W*0.60,0.22,D+1.0);
  roofR.rotateZ(-0.50); roofR.translate(W*0.235,H-0.30,0); B.put(roofR,0x342514);
  const ridge=new THREE.CylinderGeometry(0.09,0.09,W+0.8,6);
  ridge.rotateZ(Math.PI/2); ridge.translate(0,H+0.28,0); B.put(ridge,0x2a1c10);
  for(let i=0;i<4;i++){
    const col=new THREE.CylinderGeometry(0.09,0.11,H,6);
    col.translate((i%2?1:-1)*(W/2-0.3),H/2,(i<2?1:-1)*(D/2-0.3)); B.put(col,0x2a1c10);
  }
  const sL=new THREE.BoxGeometry(D*0.92,1.45,0.10);
  sL.rotateY(Math.PI/2); sL.translate(-W/2+0.06,0.72,0); B.put(sL,0x2a1c10);
  const sR=new THREE.BoxGeometry(D*0.92,1.45,0.10);
  sR.rotateY(Math.PI/2); sR.translate(W/2-0.06,0.72,0); B.put(sR,0x2a1c10);
  const bk=new THREE.BoxGeometry(W*0.92,1.45,0.10);
  bk.translate(0,0.72,-D/2+0.10); B.put(bk,0x2e2012);
  const fl1=new THREE.BoxGeometry(0.95,2.0,0.07);
  fl1.rotateY(0.45); fl1.translate(-0.75,1.05,D/2-0.06); B.put(fl1,0x332415);
  const fl2=new THREE.BoxGeometry(0.95,2.0,0.07);
  fl2.rotateY(-0.38); fl2.translate(0.78,1.05,D/2-0.06); B.put(fl2,0x2f2011);
  const an=new THREE.BoxGeometry(1.5,0.09,0.7);
  an.translate(0,0.80,D/2-1.25); B.put(an,0x402c14);
  const leg=new THREE.BoxGeometry(1.3,0.76,0.5);
  leg.translate(0,0.38,D/2-1.25); B.put(leg,0x2e2010);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a3820,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  const door=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffa050,
    transparent:true,opacity:0.22,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  door.scale.set(4.2,3.6,1); door.position.set(0,1.5,D/2+0.25); door.renderOrder=3; g.add(door);
  const yan=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9fbccb,
    transparent:true,opacity:0.24,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  yan.scale.set(1.1,1.1,1); yan.position.set(0.25,1.05,D/2-1.25); yan.renderOrder=4; g.add(yan);
  const inL=new THREE.PointLight(0x9fbccb,0.55,12);
  inL.position.set(0,1.6,D/2-1.0); g.add(inL);
  const ph=(o.seed===undefined?26406:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    door.material.opacity=kk*0.22*(0.84+0.16*Math.sin(t*1.3+ph));
    yan.material.opacity=kk*0.24*(0.72+0.28*Math.pow(Math.max(0,Math.sin(t*0.8+ph)),3));
    inL.intensity=kk*0.55*(0.88+0.12*Math.sin(t*1.1+ph));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 车师西门 makeZmcChengmenJS(o)：城墙一段+门洞+门楼（柱/檐/坡顶）+女墙垛口+
   门侧双火把光——「车师西门伫献捷」（合批 1 mesh+2 Sprite） */
function makeZmcChengmenJS(o){
  o=o||{};
  const W=o.W===undefined?26:o.W;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(W,5.0,3.2);
  wall.translate(0,2.5,0); B.put(wall,0x261a10);
  const wall2=new THREE.BoxGeometry(W-2,1.5,2.4);
  wall2.translate(0,5.75,0); B.put(wall2,0x2b1d11);
  for(let i=0;i<11;i++){
    const ml=new THREE.BoxGeometry(0.85,0.62,0.55);
    ml.translate(-W/2+1.0+i*(W-2)/10,6.85,0.7); B.put(ml,0x261a10);
  }
  const menD=new THREE.BoxGeometry(3.6,3.4,0.8);
  menD.translate(0,1.7,1.5); B.put(menD,0x0d0805);
  const pL=new THREE.BoxGeometry(1.1,3.8,3.7);
  pL.translate(-2.35,1.9,1.5); B.put(pL,0x2b1d11);
  const pR=new THREE.BoxGeometry(1.1,3.8,3.7);
  pR.translate(2.35,1.9,1.5); B.put(pR,0x2b1d11);
  const liang=new THREE.BoxGeometry(5.8,0.8,3.0);
  liang.translate(0,3.9,0.4); B.put(liang,0x2b1d11);
  const lou=new THREE.BoxGeometry(6.4,2.6,4.0);
  lou.translate(0,6.6,0); B.put(lou,0x2c1e12);
  for(let i=0;i<4;i++){
    const col=new THREE.CylinderGeometry(0.16,0.20,2.4,6);
    col.translate(-2.1+i*1.4,9.0,1.6); B.put(col,0x332415);
  }
  const eave=new THREE.BoxGeometry(7.2,0.34,4.6);
  eave.translate(0,10.3,0.4); B.put(eave,0x3a2a16);
  const roof=new THREE.BoxGeometry(7.8,0.9,4.4);
  roof.translate(0,10.9,0); B.put(roof,0x1e140c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x4a3420,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.18:o.rim,p:2.2})));
  const torches=[];
  [-1.0,1.0].forEach(function(sd){
    const f=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffa050,
      transparent:true,opacity:0.24,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    f.scale.set(2.2,2.6,1); f.position.set(sd*2.6,3.6,2.2); f.renderOrder=3; g.add(f); torches.push(f);
  });
  const ph=(o.seed===undefined?26408:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<torches.length;i++){
      torches[i].material.opacity=kk*0.24*(0.72+0.28*Math.pow(Math.max(0,Math.sin(t*1.4+i*2.1+ph)),2));
    }
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 碎石风暴幻影组 makeZmcBaofengJS(o)：末境点击的幻象（点击前 visible=false 硬关）——
   ① 腾空翻卷的风暴石阵（加色 InstancedMesh 1 draw call）；② 卷石沙尘暴（makeGlow 底层横扫）；
   ③ 风暴风声流（makeFlow 高速）；④ 迎风疾进的行军纵队幻影+火把光带（自画右向西门推进）
   update(t,k,rv)：rv 0→1 淡现并推进军阵——「点击石乱走（碎石风暴）」 */
function makeZmcBaofengJS(o){
  o=o||{};
  const g=new THREE.Group();
  const n=o.n===undefined?64:o.n;
  const R=seedRnd(o.seed===undefined?26431:o.seed);
  const box=o.box===undefined?{cx:-2,cz:-9,w:112,d:26}:o.box;
  const B=new GeoBag();
  const rk=new THREE.IcosahedronGeometry(1,0); rk.translate(0,0.2,0); B.put(rk,0xffffff);
  const rk2=new THREE.IcosahedronGeometry(0.6,0); rk2.translate(0.55,0.55,0.3); B.put(rk2,0xffffff);
  const rock=mergeGeos(B.list);
  const mat=new THREE.MeshBasicMaterial({color:0xd8b488,transparent:true,opacity:0.30,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const mesh=new THREE.InstancedMesh(rock,mat,n);
  mesh.frustumCulled=false; mesh.renderOrder=3;
  const dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    items.push({ph:R(),sp:0.10+R()*0.10,z:box.cz+(R()-0.5)*box.d,
      s:0.5+R()*1.5,rx:(R()-0.5)*3,ry:(R()-0.5)*3,hop:2.5+R()*4.5});
  }
  g.add(mesh);
  const dust=makeGlow({n:26,box:[100,7,22],pos:[box.cx,2.2,box.cz],color:0x8a6a44,size:8,
    speed:0.30,rise:0,add:false,maxA:0.30});
  dust.points.renderOrder=3; g.add(dust.points);
  const streak=makeFlow({n:240,box:[110,9,24],pos:[box.cx,3.4,box.cz],color:0x6a5440,size:13,
    speed:9.0,maxA:0.20});
  g.add(streak.points);
  const army=new THREE.Group();
  const col=makeZmcXingjunJS({seed:26432,ghost:true,pts:[
    [12,-14,0.1],[9.4,-14.8,-0.05],[6.8,-15.4,0.06],[4.2,-15.9,-0.04],
    [1.6,-16.3,0.08],[-1.0,-16.6,-0.06],[-3.6,-16.9,0.07],[-6.2,-17.1,-0.05],
    [-8.8,-17.2,0.05],[-11.4,-17.3,-0.04]]});
  army.add(col);
  const huo=makeGlow({n:14,box:[26,2.4,4],pos:[0,2.0,-16.5],color:0xe0a45c,size:2.0,
    speed:0.06,rise:0,add:true,maxA:0.30});
  huo.points.renderOrder=3; army.add(huo.points);
  army.position.x=30; g.add(army);
  g.userData.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const on=kk*r>0.004, half=box.w*0.5;
    for(let i=0;i<n;i++){
      const it=items[i];
      const prog=(t*it.sp+it.ph)%1;
      dm.position.set(box.cx-half+prog*box.w,Math.sin(prog*Math.PI)*it.hop,it.z);
      dm.rotation.set(it.rx+t*2.2,it.ry*0.5,it.ry+t*2.8);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mesh.material.opacity=kk*0.30*r;
    dust.mat.uniforms.uMaxA.value=kk*0.30*r;
    streak.mat.uniforms.uMaxA.value=kk*0.20*r;
    dust.update(t); streak.update(t);
    army.position.x=30-34*r;
    col.userData.update(t,kk);
    g.visible=on;
  };
  g.visible=false;
  return {g:g,update:g.userData.update};
}

/* 边塞人物（贯穿造型系，每次 build 新建材质） */
function zmcFigure(scale,pose,robe){
  return makeFigure({pose:pose||'独立',robe:robe||0x2e2314,belt:0x8a6238,skin:0xd9b189,
    collar:0x6a4a28,hair:0x1a140c,hat:'幞头',rimC:0xc9a06a,rim:0.44,noProp:true,
    scale:scale===undefined?1:scale});
}

function bCover(){ // 卷首 · 走马川夜色总览：蜿蜒干河床大如斗碎石隐现，黄尘横扫，雪海远带
  const g=new THREE.Group();
  const base=makeZmcBase({seed1:26453,seed2:26454}); g.add(base.g);
  const bed=makeZmcHebedJS({seed:26401,L:140,W:30,z:-12}); g.add(bed);
  const sk=makeZmcShikeJS({seed:26411,n:80,box:{cx:0,cz:-12,x:104,z:30},walk:0.30}); g.add(sk.g);
  const xue=makeZmcXuehaiJS({x:-72,z:-84,w:130,y:-0.2}); g.add(xue.g);
  const wind=makeFlow({n:300,box:[112,9,44],pos:[0,3.2,-16],color:0x5a4a36,size:15,speed:5.4,maxA:0.10});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,13,78],pos:[0,4.6,-54],scale:64,color:0x4a3a24,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[150,15,60],pos:[0,8,-32],color:0x8a7048,size:4.0,speed:0.035,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x120d08,seed:26471,rim:0.10,rimC:0xc9a06a});
  fg1.g.position.set(-12,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x120d08,seed:26472,rim:0.09,rimC:0xc9a06a});
  fg2.g.position.set(13,-1.8,12); g.add(fg2.g);
  addLights(g,{c:0xb08850,i:0.30,p:[-44,52,-24]},{c:0x2a1e12,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update();
    bed.userData.update(t,k); sk.update(t,k); xue.update(t,k);
    wind.update(t); motes.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXuehai(){ // 壹（标志性瞬间）· 雪海莽沙 —— 君不见走马川行雪海边……随风满地石乱走：
                    // 低机位沿干河床看风：一川碎石大如斗随风乱走，平沙莽莽黄入天，雪海远带在侧
  const g=new THREE.Group();
  const base=makeZmcBase({seed1:26455,seed2:26456,h1:13}); g.add(base.g);
  const bed=makeZmcHebedJS({seed:26402,L:150,W:32,z:-6,amp:4.4}); g.add(bed);
  /* 标志性瞬间：一川碎石大如斗，随风满地石乱走（走石翻滚弹跳+静石震颤） */
  const sk=makeZmcShikeJS({seed:26412,n:96,box:{cx:2,cz:-6,x:114,z:32},sMin:0.5,sMax:2.1,walk:0.38});
  g.add(sk.g);
  /* 平沙莽莽黄入天：双层黄尘横流+天际黄雾（fog:false 加色） */
  const wind=makeFlow({n:320,box:[124,10,42],pos:[0,3.0,-10],color:0x6a5232,size:15,speed:6.2,maxA:0.15});
  g.add(wind.points);
  const wind2=makeFlow({n:220,box:[134,7,36],pos:[0,1.6,-12],color:0x7a5e38,size:12,speed:7.4,maxA:0.12});
  g.add(wind2.points);
  const huang=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8863c,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  huang.scale.set(92,36,1); huang.position.set(32,11,-112); huang.renderOrder=2; g.add(huang);
  /* 雪海边：左侧远处雪海带+雪霰 */
  const xue=makeZmcXuehaiJS({x:-30,z:-86,w:132,y:-0.2}); g.add(xue.g);
  /* 诗人立于河床远侧高崖望风（君不见——岑参在轮台望此奇景） */
  const poet=zmcFigure(1.4,'独立',0x2e2314); poet.position.set(7.4,-1.78,-15.5);
  poet.rotation.y=-2.55; g.add(poet);
  const rockP=makeForeground({kind:'坡石',n:2,r:2.2,w:8,d:4,color:0x14100a,seed:26473,rim:0.12,rimC:0xc9a06a});
  rockP.g.position.set(7.0,-0.4,-16.4); g.add(rockP.g);
  const mist=makeMist({n:6,spread:[210,12,70],pos:[0,4.4,-50],scale:62,color:0x4a3a24,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[150,15,58],pos:[0,8,-28],color:0x9a7848,size:4.0,speed:0.035,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:26474,rim:0.10,rimC:0xc9a06a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:26475,rim:0.09,rimC:0xc9a06a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0xc89050,i:0.38,p:[38,48,-26]},{c:0x2e2012,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update();
    bed.userData.update(t,k); sk.update(t,k);
    wind.update(t); wind2.update(t);
    huang.material.opacity=k*0.13*(0.88+0.12*Math.sin(t*0.5));
    xue.update(t,k);
    poet.update(t,k); rockP.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bChushi(){ // 贰 · 出师夜行 —— 匈奴草黄马正肥……风头如刀面如割：
                    // 金山烟尘飞（右后暖山+敌尘），夜行军火把长龙蜿蜒而来，将军金甲按剑立马当先
  const g=new THREE.Group();
  const base=makeZmcBase({seed1:26457,seed2:26458,h2:8,c1:0x110c07,c2:0x1c130a}); g.add(base.g);
  /* 金山（右后·暖光山骨）+ 山下烟尘飞 */
  const jinshan=makeRange({arc:0.72,a0:2.30,r:118,h:20,layers:2,peaks:5,seed:26459,
    color:0x1a1208,atmo:0x3a2412,fogK:0.60,glowK:0.10,glow:0xd8a05a,y:-9,order:-5});
  g.add(jinshan.g);
  const yanchen=makeGlow({n:16,box:[7,22,7],pos:[27,11,-60],color:0x4a3822,size:8,speed:0.05,rise:1,add:false,maxA:0.16});
  yanchen.points.renderOrder=3; g.add(yanchen.points);
  const yanGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc05a2c,
    transparent:true,opacity:0.12,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  yanGlow.scale.set(8,6,1); yanGlow.position.set(27,2.6,-58); yanGlow.renderOrder=3; g.add(yanGlow);
  /* 夜行军长龙：自画面深处蜿蜒而来（把杆火头+火把光带随队） */
  const march=makeZmcXingjunJS({seed:26422,torch:true,pts:[
    [-16,-30,0.30],[-13.2,-27.2,0.42],[-10.4,-24.4,0.52],[-7.4,-21.6,0.62],
    [-4.2,-18.9,0.72],[-0.8,-16.4,0.80],[2.8,-14.2,0.88],[6.6,-12.4,0.94],
    [10.6,-11.0,1.0],[14.6,-10.0,1.05]]});
  g.add(march);
  const huo=makeGlow({n:16,box:[34,2.4,6],pos:[-1,2.2,-20],color:0xe09a4c,size:2.0,speed:0.05,rise:0,add:true,maxA:0.27});
  huo.points.renderOrder=3; g.add(huo.points);
  /* 将军金甲夜不脱：金甲主将按剑立马队之前 */
  const gen=zmcFigure(1.42,'按剑',0x3c2c12); gen.position.set(-6.8,-1.78,-9.0);
  gen.rotation.y=0.55; g.add(gen);
  const ma=makeZmcMaJS({s:0.85,coat:0x33261a,seed:26413});
  ma.g.position.set(-4.6,-1.78,-10.8); ma.g.rotation.y=0.7; g.add(ma.g);
  /* 旌旗两杆，狂风横卷 */
  const q1=makeZmcQiJS({seed:26403,H:7.4}); q1.position.set(-12.5,-1.8,-22); q1.rotation.y=0.4; g.add(q1);
  const q2=makeZmcQiJS({seed:26404,H:6.6,W:2.0,Hh:1.3}); q2.position.set(3.5,-1.8,-15.5); q2.rotation.y=-0.3; g.add(q2);
  /* 风头如刀：疾风流细而快 */
  const blade=makeFlow({n:260,box:[120,8,36],pos:[0,3.4,-12],color:0x544434,size:11,speed:8.5,maxA:0.10});
  g.add(blade.points);
  const mist=makeMist({n:6,spread:[210,13,72],pos:[0,4.6,-52],scale:64,color:0x3e2f1e,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[150,15,58],pos:[0,8,-28],color:0x8a6c44,size:4.0,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:26476,rim:0.10,rimC:0xc9a06a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:26477,rim:0.09,rimC:0xc9a06a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0xb08a58,i:0.26,p:[-36,50,-28]},{c:0x241a0e,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update();
    jinshan.update(t,0); yanchen.update(t);
    yanGlow.material.opacity=k*0.12*(0.80+0.20*Math.sin(t*0.9));
    march.userData.update(t,k); ma.update(t,k); gen.update(t,k);
    q1.userData.update(t,k,1.3); q2.userData.update(t,k,1.3);
    huo.update(t); blade.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bHanqi(){ // 叁 · 汗气成冰 —— 马毛带雪汗气蒸，五花连钱旋作冰，幕中草檄砚水凝：
                   // 奇寒之夜：战马汗气成冰白雾蒸腾+冰斑寒光，中军大帐草檄砚水凝冷光（全页最冷一境）
  const g=new THREE.Group();
  const base=makeZmcBase({seed1:26460,seed2:26461,c1:0x0e0c09,c2:0x191611,h1:11}); g.add(base.g);
  /* 中军大帐（右）：帐内暖光一角+案上砚水凝冷光（暖门光与冷砚光同框） */
  const zhang=makeZmcDazhangJS({seed:26406}); zhang.g.position.set(8.0,-1.78,-13.5);
  zhang.g.rotation.y=-0.55; g.add(zhang.g);
  const qi=makeZmcQiJS({seed:26407,H:6.2,W:1.8,Hh:1.2}); qi.position.set(11.5,-1.8,-10.5);
  qi.rotation.y=-0.6; g.add(qi);
  /* 草檄军士立于帐门 */
  const junshi=zmcFigure(1.05,'指月',0x2a2012); junshi.position.set(6.4,-1.78,-10.0);
  junshi.rotation.y=-0.95; g.add(junshi);
  /* 战马三匹（左）：马毛带雪汗气蒸——汗气白雾自马背蒸腾 */
  const h1=makeZmcMaJS({s:1.05,coat:0x2c2114,steam:true,seed:26414});
  h1.g.position.set(-5.2,-1.78,-6.0); h1.g.rotation.y=0.5; g.add(h1.g);
  const h2=makeZmcMaJS({s:0.92,coat:0x3a2c1c,steam:true,seed:26415});
  h2.g.position.set(-9.0,-1.78,-10.5); h2.g.rotation.y=-0.4; g.add(h2.g);
  const h3=makeZmcMaJS({s:0.8,coat:0x241a10,steam:true,seed:26416});
  h3.g.position.set(-2.0,-1.78,-12.5); h3.g.rotation.y=0.15; g.add(h3.g);
  /* 五花连钱旋作冰：马身汗气凝冰的寒光（淡青冰斑） */
  const bing=[];
  [[-4.9,1.7,-6.2],[-8.7,1.6,-10.7]].forEach(function(p){
    const b=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8c4d0,
      transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    b.scale.set(4.6,2.3,1); b.position.set(p[0],p[1],p[2]); b.renderOrder=3; g.add(b); bing.push(b);
  });
  const mist=makeMist({n:5,spread:[180,11,62],pos:[0,4.2,-44],scale:56,color:0x2a2822,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[140,14,54],pos:[0,8,-24],color:0x9aa0a4,size:3.8,speed:0.028,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0d0b08,seed:26478,rim:0.10,rimC:0xc9a06a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x0d0b08,seed:26479,rim:0.09,rimC:0xc9a06a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0x9aa4b8,i:0.24,p:[-30,54,-30]},{c:0x1c1812,i:0.46});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update();
    zhang.update(t,k); qi.userData.update(t,k,0.8); junshi.update(t,k);
    h1.update(t,k); h2.update(t,k); h3.update(t,k);
    for(let i=0;i<bing.length;i++)bing[i].material.opacity=k*0.10*(0.72+0.28*Math.sin(t*0.9+i*1.7));
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXianjie(){ // 肆（末境·可点击）· 车师献捷 —— 虏骑闻之应胆慑……车师西门伫献捷：
                     // 车师西门城楼旌旗伫候，军阵静立，天际献捷曙色初临；
                     // 点击：碎石风暴幻影卷地而起+风声+行军队伍迎风疾进幻影，题字同现，可反复点击
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const base=makeZmcBase({seed1:26462,seed2:26463,c1:0x110d08,c2:0x1d140b}); g.add(base.g);
  /* 车师西门（左近）+楼上旌旗+门侧火把 */
  const men=makeZmcChengmenJS({seed:26408}); men.g.position.set(-9.5,-1.8,-17); men.g.rotation.y=0.30; g.add(men.g);
  const q1=makeZmcQiJS({seed:26409,H:7.0}); q1.position.set(-13.5,-1.8,-13.5); q1.rotation.y=0.5; g.add(q1);
  const q2=makeZmcQiJS({seed:26410,H:6.4,W:2.0,Hh:1.3}); q2.position.set(-6.0,-1.8,-14.0); q2.rotation.y=-0.35; g.add(q2);
  /* 伫候献捷的军阵（中景静立）+ 地面碎石（静石微颤） */
  const lie=makeCrowd({n:16,rect:[-4,-24,26,10],seed:26433,color:0x1c150e,rimC:0xc9a06a,rim:0.14,
    sMin:0.75,sMax:1.0});
  g.add(lie.mesh);
  const sk=makeZmcShikeJS({seed:26413,n:46,box:{cx:5,cz:-9,x:72,z:24},sMin:0.4,sMax:1.3,walk:0.0});
  g.add(sk.g);
  /* 献捷曙色：天际一线微明（右，fog:false） */
  const shu=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8a860,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  shu.scale.set(72,22,1); shu.position.set(44,4,-98); shu.renderOrder=2; g.add(shu);
  /* 标志性交互：碎石风暴+迎风疾进军阵（点击前幻影组 visible=false 硬关） */
  const bf=makeZmcBaofengJS({}); g.add(bf.g);
  const mist=makeMist({n:5,spread:[180,12,64],pos:[0,4.4,-46],scale:58,color:0x382a18,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[140,15,56],pos:[0,8,-26],color:0x9a7a4e,size:4.0,speed:0.028,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0e0a06,seed:26480,rim:0.10,rimC:0xc9a06a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x0e0a06,seed:26481,rim:0.09,rimC:0xc9a06a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0xb89058,i:0.28,p:[-34,50,-26]},{c:0x261c10,i:0.52});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/6.0);
      const e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      bf.update(t,k,e);
      men.update(t,k);
      q1.userData.update(t,k,1.15); q2.userData.update(t,k,1.15);
      lie.update(t);
      sk.update(t,k);
      shu.material.opacity=k*0.10*(0.85+0.15*Math.sin(t*0.4));
      mist.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update();
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.14);
        pluck(0,0.0,0.14); pluck(3,0.30,0.10); pluck(1,0.66,0.09); pluck(4,1.10,0.08); pluck(2,1.60,0.07);
      }
      const fl=$('#flash'); fl.textContent='一川碎石大如斗 随风满地石乱走';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x140f09),hor:C(0x30200e),bot:C(0x0b0805),fog:C(0x190f08),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-70,26,-190),ms:0.30,mph:0.46,mhaze:0.20,dirC:C(0xb08a52),dirI:0.32,
  dirP:new THREE.Vector3(-48,50,-26),ambC:C(0x2a1e12),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10.5,48],t:[0,7.0,26],lf:[2,9.5,-14],lt:[3,8.0,-30]},
  sky:()=>SK({fd:0.0048,star:0.12,hor:C(0x3e2a12),ms:0.30,mph:0.46,mhaze:0.26}) },
{ name:'雪海莽沙',dwell:24,river:0.02,build:bXuehai,
  cam:{f:[-9,3.6,14],t:[5,2.6,-4],lf:[-3,3.2,-2],lt:[6,3.0,-14]},
  sky:()=>SK({top:C(0x1c140b),hor:C(0x52381a),bot:C(0x0e0906),fog:C(0x1d140b),fd:0.0060,star:0.03,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.10,
    dirC:C(0xc89050),dirI:0.38,dirP:new THREE.Vector3(38,48,-26),
    ambC:C(0x2e2012),ambI:0.58}) },
{ name:'出师夜行',dwell:22,river:0.02,build:bChushi,
  cam:{f:[-6,5.0,22],t:[3,3.6,-6],lf:[-2,4.4,-8],lt:[5,4.2,-24]},
  sky:()=>SK({top:C(0x120d08),hor:C(0x2c1e10),fog:C(0x181009),fd:0.0056,star:0.30,
    moon:new THREE.Vector3(52,30,-180),ms:0.44,mph:0.50,mhaze:0.22,
    dirC:C(0xb08a58),dirI:0.26,dirP:new THREE.Vector3(-36,50,-28),
    ambC:C(0x241a0e),ambI:0.50}) },
{ name:'汗气成冰',dwell:20,river:0.02,build:bHanqi,
  cam:{f:[-2.5,4.4,15],t:[2.5,2.8,-4],lf:[-1,4.0,-4],lt:[3,3.6,-16]},
  sky:()=>SK({top:C(0x0b0a08),hor:C(0x1a140c),bot:C(0x080706),fog:C(0x151009),fd:0.0052,star:0.55,
    moon:new THREE.Vector3(-62,44,-185),ms:0.42,mph:0.40,mhaze:0.14,
    dirC:C(0x9aa4b8),dirI:0.24,dirP:new THREE.Vector3(-30,54,-30),
    ambC:C(0x1c1812),ambI:0.46}) },
{ name:'车师献捷',dwell:22,river:0.02,build:bXianjie,
  cam:{f:[2.5,4.8,18],t:[-5,3.4,0],lf:[1,4.2,-6],lt:[-4,3.6,-20]},
  sky:()=>SK({top:C(0x12100b),hor:C(0x3a2a16),fog:C(0x181009),fd:0.0054,star:0.18,
    moon:new THREE.Vector3(-64,36,-180),ms:0.24,mph:0.48,mhaze:0.20,
    dirC:C(0xb89058),dirI:0.28,dirP:new THREE.Vector3(-34,50,-26),
    ambC:C(0x261c10),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('zoumachuan.py —— 被 build.py 消费：python build.py zoumachuan')
