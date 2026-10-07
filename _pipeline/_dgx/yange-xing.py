# -*- coding: utf-8 -*-
"""yange-xing.py —— 《燕歌行》（唐·高适，queue no.263，大漠金戈）生成配置
四境长卷（N=4，14 分句 [4,4,4,2]）：
壹 烟尘汉家（汉家烟尘在东北…单于猎火照狼山——出征：榆关关楼+旌旆行军长龙下关+摐金伐鼓立鼓+
  东北烟尘柱+狼山猎火，昼昏黄烟尘蔽日），
贰 萧条边庭（山川萧条极边土…力尽关山未解围——战场危局+标志性瞬间：战士军前半死生，美人帐下犹歌舞——
  牙帐暖光歌舞剪影（含蓄）与帐外寒沙苦战同框对切；孤城落日、大漠穷秋、塞草腓），
叁 两地悬望（铁衣远戍辛勤久…寒声一夜传刁斗——征人思妇对切：左蓟北戍楼征人回首+右城南楼头思妇灯暖+
  中间绝域苍茫一雾相隔+阵云低垂+刁斗夜声，高悬一轮共照之月），
肆 白刃沙场（相看白刃血纷纷…至今犹忆李将军——末境可点击：白刃寒光。
  交互：点击——白刃寒光自左向右次第亮起如一列刀锋点名，冷光扫过军阵，题字同现，可反复点击）。
美术立意「一帐之隔，两个世界」：全诗是盛唐边塞诗最锋利的讽刺——出征之壮（壹）→危局之酷（贰·
帐内帐外对切）→两地之思（叁·征人思妇悬望）→白刃之烈（肆·收束于死节岂顾勋）。
大漠金戈全套色板：底色 #120d08、雾 #190f08～#1d140b 系、文字 #f0e2cc，accent=#b8906a
（queue 分配强调色）只落在 UI/人物边缘光/旗面光边/帐内暖光/白刃寒光上，禁艳金。
与已有边塞页第一眼可区分：不做拂晓誓师整甲群像（wuyi）、不做木兰人生长卷（mulanci）、
不做骨梦对切（longxixing）、不做金甲黄沙孤城烽燧（congjunxing-yumen）、不做密林夜射（saixiaqu-linan）、
不做雪原听笛（saishang-chuidi）——本页是**牙帐一顶定褒贬**：帐内暖光歌舞剪影与帐外寒沙苦战
同框对切是全页的构图心脏，无大场面厮杀，战争意象克制写意（姿态写意、无血腥直写）。
自建 builder：makeDamoYG（大漠基底）/ makeGuanYG（榆关关楼）/ makeJingqiYG（军旗）/
makeXingjunYG（行军长龙低模）/ makeLiguYG（立鼓）/ makeYanchenYG（东北烟尘）/
makeLangshanYG（狼山猎火）/ makeYaZhangYG（牙帐+帐内歌舞剪影）/ makeKuzhanYG（苦战群像）/
makeCangeYG（残戈残旗）/ makeSaicaoYG（塞草枯黄）/ makeGuchengYG（孤城远影）/
makeShulouYG（蓟北戍楼+刁斗）/ makeChengnanYG（城南城郭楼头）/ makeBairenYG（白刃军阵·可点击）。
考点钉子：摐 chuāng／腓 féi／飘飖 piāo yáo／勋 xūn／单于 chán yú／玉箸 zhù／蓟北 jì／
胡骑 jì（小测第 3 题落点）；乐府旧题+开元二十六年张守珪部冒功事+高适边塞诗（第 4 题）；
将帅骄逸与士卒苦战对比讽刺、借李将军寄托（第 5 题）。
多音字：摐金→窗金 单于→蝉于 燕歌行→烟歌行 胡骑→胡寄 蓟北→寄北 草腓→草肥 飘飖→飘摇
玉箸→玉住 校尉→效尉 旌旆→旌配 那可度→哪可度（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='yange-xing', title='燕歌行', dyn='唐 · 高适', brand_author='高 适',
    gold_rgb='184,144,106',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b8906a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(184,144,106,.3);
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
    tip='轻点画面 / 按空格 —— 白刃寒光次第亮起，死节岂为顾勋',
    hint='← → 键或空格逐境游览 · 末境可点击画面：白刃寒光自左向右次第亮起，看相看白刃的决绝',
    cover_read='燕歌行。唐，高适。汉家烟尘在东北，汉将辞家破残贼。摐金伐鼓下榆关，旌旆逶迤碣石间。战士军前半死生，美人帐下犹歌舞。相看白刃血纷纷，死节从来岂顾勋。君不见沙场征战苦，至今犹忆李将军。',
    cover_p1='四重意境，随诗句次第展开：汉家烽烟又起东北，男儿辞家出塞、本自重横行，天子格外赐予颜色；摐金伐鼓直下榆关，旌旆逶迤碣石间，校尉羽书飞瀚海，单于猎火照狼山；山川萧条极边土，战士军前半死生，美人帐下犹歌舞——大漠穷秋塞草腓，孤城落日斗兵稀；铁衣远戍辛勤久，玉箸应啼别离后，少妇城南欲断肠，征人蓟北空回首；相看白刃血纷纷，死节从来岂顾勋——君不见沙场征战苦，至今犹忆李将军。',
    cover_p2='边读诗，边走进高适笔下这场被功名心驱赶的远征：同一片沙场，帐内暖光歌舞、帐外寒沙苦战——一顶牙帐隔开两个世界；同一轮明月，城南楼头断肠、蓟北戍楼回首。读懂这一对切，就读懂了盛唐边塞诗最锋利的讽刺，也读懂了「死节从来岂顾勋」的悲壮。',
    end_h2='白刃 · 李将军', cn_word='肆',
    words_js="['再入一次燕歌行','初识高适，尚需共读','渐入诗境，再诵几遍','金鼓渐远，边庭渐寒','两地悬望，白刃相照','已解帐内帐外之叹']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'烟尘汉家', jing:'汉家烽烟又在东北燃起，将军辞别家室去扫荡残寇。男儿本来就崇尚纵横驰骋、沙场建功，天子又格外赐予恩宠荣遇。大军鸣钲击鼓直下榆关，旌旆在碣石一带蜿蜒绵延；校尉的羽书飞越瀚海告急，单于的猎火已经照亮狼山。（出征 · 摐金伐鼓 · 旌旆逶迤 · 羽书猎火）',
  segs:[
   {c:'汉家烟尘在东北，', p:py('hàn jiā yān chén zài dōng běi')},
   {c:'汉将辞家破残贼。', p:py('hàn jiàng cí jiā pò cán zéi')},
   {c:'男儿本自重横行，', p:py('nán ér běn zì zhòng héng xíng')},
   {c:'天子非常赐颜色。', p:py('tiān zǐ fēi cháng cì yán sè')},
   {c:'摐金伐鼓下榆关，', p:py('chuāng jīn fá gǔ xià yú guān')},
   {c:'旌旆逶迤碣石间。', p:py('jīng pèi wēi yí jié shí jiān')},
   {c:'校尉羽书飞瀚海，', p:py('xiào wèi yǔ shū fēi hàn hǎi')},
   {c:'单于猎火照狼山。', p:py('chán yú liè huǒ zhào láng shān')}],
  read:'汉家烟尘在东北，汉将辞家破残贼。男儿本自重横行，天子非常赐颜色。摐金伐鼓下榆关，旌旆逶迤碣石间。校尉羽书飞瀚海，单于猎火照狼山。',
  yisi:'东北边境战尘又起，将军们辞家出塞，去讨伐背盟的残寇。「男儿本自重横行」一句先声夺人：好男儿本来就崇尚在万里之外纵横驰骋，何况天子又格外降恩礼遇——出师的豪气被推到顶点。于是摐金伐鼓，大军直下榆关，旌旆如云，在碣石间逶迤而行；而另一面，校尉的羽书正飞越瀚海，单于的猎火已照亮狼山——敌情如火，军情如羽。前四句写出征之壮、军容之盛，后四句已暗暗埋下大战将临的紧张：写得愈威武，后文的危局与讽意愈见分量。',
  zhu:[['汉家','汉朝，唐诗中常借汉指唐——「汉家烟尘」即唐境东北燃起的战火'],['烟尘','烽烟与征尘，代指战争'],['残贼','凶残的敌寇——指背盟挑衅的部落'],['横行','纵横驰骋、冲杀无阻——男儿建功立业的豪情。重，看重、崇尚，读 zhòng'],['非常赐颜色','超过寻常地赐予恩宠礼遇。非常，格外；赐颜色，给以恩遇——这份「恩遇」正是后文「身当恩遇常轻敌」的伏笔'],['摐金伐鼓','鸣钲击鼓。摐，敲击，读 chuāng；金，钲一类行军乐器；伐，击——金声鼓声开道，写大军开拔的声威'],['榆关','山海关，泛指东北边关重镇'],['旌旆','军中旗帜。旆，竿头如燕尾下垂的大旗，读 pèi'],['逶迤','蜿蜒曲折、连绵不绝的样子'],['碣石','山名，在今河北昌黎，临渤海——旌旆逶迤碣石间，见行军之众'],['校尉','武官名，地位次于将军。校，读 xiào'],['羽书','插有羽毛的紧急军事文书，即羽檄'],['瀚海','大沙漠'],['单于','匈奴君主的称号，此借指敌方首领。单于，读 chán yú'],['猎火','打猎之火——游牧部族出征前多围猎练兵，猎火弥山即是战火将起之兆'],['狼山','即狼居胥山一带，泛指敌境的山峦']] },
{ name:'萧条边庭', jing:'山川萧条荒凉，直到边境的尽头，胡骑的进犯像狂风暴雨一般。战士在阵前拼杀，半数生死难料；将帅的营帐里，美人还在轻歌曼舞。大漠穷秋时节塞草枯萎，孤城落日之下能战的士兵愈来愈稀；身受皇恩却常常轻敌，力战关山重围依然未解。（萧条 · 危局 · 标志性瞬间：帐内帐外对切——帐外半死生，帐下犹歌舞）',
  segs:[
   {c:'山川萧条极边土，', p:py('shān chuān xiāo tiáo jí biān tǔ')},
   {c:'胡骑凭陵杂风雨。', p:py('hú jì píng líng zá fēng yǔ')},
   {c:'战士军前半死生，', p:py('zhàn shì jūn qián bàn sǐ shēng')},
   {c:'美人帐下犹歌舞。', p:py('měi rén zhàng xià yóu gē wǔ')},
   {c:'大漠穷秋塞草腓，', p:py('dà mò qióng qiū sài cǎo féi')},
   {c:'孤城落日斗兵稀。', p:py('gū chéng luò rì dòu bīng xī')},
   {c:'身当恩遇常轻敌，', p:py('shēn dāng ēn yù cháng qīng dí')},
   {c:'力尽关山未解围。', p:py('lì jìn guān shān wèi jiě wéi')}],
  read:'山川萧条极边土，胡骑凭陵杂风雨。战士军前半死生，美人帐下犹歌舞。大漠穷秋塞草腓，孤城落日斗兵稀。身当恩遇常轻敌，力尽关山未解围。',
  yisi:'笔锋从出征的豪壮猛地跌进战场的萧条：山川萧条到极边之地，胡骑凭陵，如风雨骤至。接着是全诗最锋利的一联——「战士军前半死生，美人帐下犹歌舞」：帐外沙场，士卒正在殊死苦战、死伤过半；帐内牙帐，将帅还在听歌看舞、醉生梦死。一面是寒沙白刃，一面是暖帐歌管，只隔一层帐布，却是两个世界——诗人不作一句议论，对比本身就是判词。大漠穷秋、塞草枯萎、孤城落日、斗兵愈稀，战场危局步步逼紧，而病根正在「身当恩遇常轻敌」：将帅恃恩而骄、轻敌无谋，才有「力尽关山未解围」的死局。',
  zhu:[['极边土','到了疆土的尽头——极言边地之荒远萧条'],['凭陵','仗势侵凌、步步进逼'],['杂风雨','如风雨交加般急骤凶猛——形容敌骑攻势'],['半死生','出生入死、死伤过半——一个「半」字，见战况之酷'],['帐下','将帅营帐之中——与「军前」对举，构成全诗最著名的对比'],['犹','还、仍然——一个「犹」字，讽刺尽出'],['腓','枯萎（一说病害）。腓，读 féi——穷秋塞草腓，草木凋零亦如士卒凋敝'],['斗兵稀','能战斗的士兵愈来愈稀少'],['恩遇','皇帝的恩宠厚遇——回应首段「非常赐颜色」'],['轻敌','恃宠而骄、轻忽敌情——全诗讽意的落点'],['未解围','重围未解——力已尽而势未转，败局已定']] },
{ name:'两地悬望', jing:'身披铁衣远戍边地，岁月久得望不到头；家中的妻子想必在别离之后，双泪长垂如玉箸。少妇在城南愁肠欲断，征人在蓟北徒然回首——边庭动荡飘飖，哪里度得回去？绝域苍茫，更还有什么！杀气整日凝作低垂的阵云，寒夜里通宵只听刁斗声声。（悬望 · 玉箸 · 阵云 · 刁斗）',
  segs:[
   {c:'铁衣远戍辛勤久，', p:py('tiě yī yuǎn shù xīn qín jiǔ')},
   {c:'玉箸应啼别离后。', p:py('yù zhù yīng tí bié lí hòu')},
   {c:'少妇城南欲断肠，', p:py('shào fù chéng nán yù duàn cháng')},
   {c:'征人蓟北空回首。', p:py('zhēng rén jì běi kōng huí shǒu')},
   {c:'边庭飘飖那可度，', p:py('biān tíng piāo yáo nǎ kě dù')},
   {c:'绝域苍茫更何有。', p:py('jué yù cāng máng gèng hé yǒu')},
   {c:'杀气三时作阵云，', p:py('shā qì sān shí zuò zhèn yún')},
   {c:'寒声一夜传刁斗。', p:py('hán shēng yī yè chuán diāo dǒu')}],
  read:'铁衣远戍辛勤久，玉箸应啼别离后。少妇城南欲断肠，征人蓟北空回首。边庭飘飖那可度，绝域苍茫更何有。杀气三时作阵云，寒声一夜传刁斗。',
  yisi:'战场之外，诗人把镜头拉向更辽远的两地相思：征人铁衣远戍，苦守经年；思妇玉箸双垂，啼于别离之后——一个在蓟北回首，一个在城南断肠，中间隔着飘飖莫度的边庭与苍茫无物的绝域。两地各自悬望，谁也望不见谁，唯有杀气凝成的阵云整日不散，唯有刁斗的寒声彻夜传来。「少妇城南」「征人蓟北」一联，把同一时刻的两个空间剪在一句诗里——这也是「美人帐下犹歌舞」的又一重对照：帐下有歌舞，两地只有悬望。战争之苦，至此从沙场漫入千家万户。',
  zhu:[['远戍','远离家乡驻守边地。戍，驻防，读 shù'],['辛勤久','辛勤戍守，旷日持久'],['玉箸','玉筷，比喻思妇垂落的两行眼泪。箸，筷子，读 zhù'],['应啼','料想（此刻）正在啼哭。应，推测之词，读 yīng'],['城南','长安城南，唐代住宅多在城南——思妇居处的泛指'],['欲断肠','哀伤到极点'],['蓟北','蓟州之北，唐边塞战地，征人所戍之处。蓟，读 jì'],['空回首','徒然回首远望——望不见、也回不去，「空」字最苦'],['飘飖','飘荡、动荡不安，读 piāo yáo——边庭局势动荡，归路难测'],['那可度','哪里能够度越。那，同「哪」，读 nǎ——关山万里，归期难料'],['绝域','极其偏远、与世隔绝之地'],['苍茫','旷远无际、迷茫一片'],['三时','春、夏、秋三季农时——「杀气三时」谓整日整年，战云不散'],['阵云','浓重堆积如战阵的云——杀气所凝'],['刁斗','军中铜器，白天用来做饭，夜间敲击巡更。刁斗，读 diāo dǒu——寒声一夜，见戍守之辛劳']] },
{ name:'白刃沙场', jing:'你看阵前相望，白刃之上血迹纷纷——将士们从来只为守节赴死，哪里是为了个人功勋！你不见沙场征战之苦，自古如此——人们至今还深深记念着那位与士卒同甘苦的李将军。（收束 · 白刃 · 死节 · 李将军 · 末境点击画面：白刃寒光次第亮起）',
  segs:[
   {c:'相看白刃血纷纷，', p:py('xiāng kàn bái rèn xuè fēn fēn')},
   {c:'死节从来岂顾勋。', p:py('sǐ jié cóng lái qǐ gù xūn')},
   {c:'君不见沙场征战苦，', p:py('jūn bù jiàn shā chǎng zhēng zhàn kǔ')},
   {c:'至今犹忆李将军。', p:py('zhì jīn yóu yì lǐ jiāng jūn')}],
  read:'相看白刃血纷纷，死节从来岂顾勋。君不见沙场征战苦，至今犹忆李将军。',
  yisi:'鏖战之中，镜头落到阵前最近的地方：士兵们相看白刃，血迹纷纷——不必言说，彼此眼中只有赴死的决绝。「死节从来岂顾勋」一句如金石掷地：为国死节是本分，几曾是为了个人功勋？与「身当恩遇常轻敌」的将帅一对照，士卒的忠勇愈显悲壮。结尾以「君不见」长叹收束全篇：沙场征战之苦，古来如此——于是人们至今怀念那位爱护士卒、与士卒同甘苦的飞将军李广。以怀念作结，讽意愈深：今之将军贵宠而骄，古之李将军善待其卒而士乐为用——全篇的讽刺与同情，都落在这一个「忆」字上。',
  zhu:[['相看','相对而视——士卒彼此相望，白刃与血痕俱在眼前'],['白刃','雪亮的刀锋'],['血纷纷','血流纷纷。血，读 xuè——战争之烈只此四字，写得极克制'],['死节','为坚守气节（为国捐躯）而死——士卒以死殉国是「节」，不是交易'],['岂顾勋','哪里是顾念个人功勋。勋，功勋，读 xūn——与将帅冒功邀赏暗相对照'],['君不见','乐府诗习用语，犹言「你看啊」——引出全篇的收束长叹'],['沙场征战苦','边庭征战之苦古来不息——「君不见」三字将一役之痛推及千古'],['李将军','汉代飞将军李广：骁勇善战，与士卒同甘苦，得赏赐尽分麾下，士卒爱乐为用——「至今犹忆」，正是对眼前骄纵将帅的反衬']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「汉家烟尘在东北」的下一句是？', o:['汉将辞家破残贼','男儿本自重横行','摐金伐鼓下榆关'], a:0},
 {q:'「战士军前半死生」的下一句是？', o:['大漠穷秋塞草腓','美人帐下犹歌舞','孤城落日斗兵稀'], a:1},
 {q:'「摐金伐鼓下榆关」「大漠穷秋塞草腓」「边庭飘飖那可度」「死节从来岂顾勋」四句中加点字的读音与解释，完全正确的一项是？', o:['摐读 chuāng，敲击、鸣钲；腓读 féi，枯萎；飘飖读 piāo yáo，飘荡不定；勋读 xūn，功勋','摐读 chuàng，闯开；腓读 fēi，肥壮；飘飖读 biāo yáo，骏马奔跑；勋读 xún，询问','摐读 zǒng，聚合；腓读 fèi，废弛；飘飖读 piāo yáo，歌舞摇曳；勋读 xūn，和睦'], a:0},
 {q:'关于《燕歌行》的体裁与写作背景，下列说法正确的是？', o:['《燕歌行》是高适自创的新乐府诗题，专写燕地山水游猎的风光','《燕歌行》原是曹丕所作的乐府旧题（也是现存最早的完整七言诗）；高适借用旧题写时事——开元二十六年，张守珪所部与奚作战先胜后败，却谎报战功，高适有感而作此诗讽喻','《燕歌行》是盛唐流行的词牌名，高适依谱填词，写征人思妇的闺怨小唱'], a:1},
 {q:'「战士军前半死生，美人帐下犹歌舞」与「相看白刃血纷纷，死节从来岂顾勋」对读，对本诗主旨的理解最恰当的一项是？', o:['以帐内歌舞与帐外苦战、将帅骄逸与士卒死节的鲜明对比，揭露将帅轻敌骄纵、冒功无能，同情士卒浴血苦战；结尾怀念爱护士卒的李将军，讽今之意尽在言外','歌颂大唐军威浩荡、将士用命，最终大破敌军、天子论功行赏的煌煌战功','本诗主旨是写闺中少妇的相思离愁，战争场面只是陪衬相思的背景点缀'], a:0},
];
"""

SCENES_JS = """/* ================= 燕歌行 · 四境场景（大漠金戈·一帐之隔两个世界：烟尘汉家、萧条边庭、两地悬望、白刃沙场） =================
   美术立意：一帐之隔，两个世界——出征之壮（壹）→ 危局之酷（贰·帐内帐外对切）→
   两地之思（叁·征人思妇悬望）→ 白刃之烈（肆·死节岂顾勋）。
   大漠金戈色板：底色 #120d08、雾 #190f08～#1d140b 系，accent=#b8906a 只落在
   UI/人物边缘光/旗面光边/帐内暖光/白刃寒光上，禁艳金。
   与已有边塞页第一眼可区分：不做誓师整甲（wuyi）、不做人生长卷（mulanci）、不做骨梦对切（longxixing）、
   不做金甲烽燧（congjunxing）、不做密林夜射/雪原听笛——本页是**牙帐一顶定褒贬**：
   帐内暖光歌舞剪影（含蓄：剪影只在帐门口光影里摇曳）与帐外寒沙苦战同框对切是构图心脏，
   无大场面厮杀，战争意象克制写意。 */

/* —— 大漠基底 makeDamoYG(o)：斑驳大漠地面 + 两层台地远山 + 沙尘横流
   远山放 z≈-118/-64，在骨架常驻远山环（z≈-260…-330）之前，不被遮挡 */
function makeDamoYG(o){
  o=o||{};
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:o.c1===undefined?0x150e07:o.c1,c2:o.c2===undefined?0x241708:o.c2,y:-1.8});
  g.add(grd.mesh);
  const ridge=makeRange({r:310,h:o.h1===undefined?16:o.h1,layers:2,peaks:o.p1===undefined?5:o.p1,
    seed:o.seed1===undefined?26351:o.seed1,color:0x0d0906,atmo:0x2e2114,fogK:0.62,glowK:0.06,
    glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(o.r1x===undefined?-14:o.r1x,0,o.r1z===undefined?-118:o.r1z);
  ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:250,h:o.h2===undefined?10:o.h2,layers:2,peaks:3,
    seed:o.seed2===undefined?26352:o.seed2,color:0x0a0704,atmo:0x2e2114,fogK:0.58,glowK:0.04,
    glow:0xd8a860,y:-9,order:-5});
  ridge2.g.position.set(o.r2x===undefined?22:o.r2x,0,o.r2z===undefined?-64:o.r2z);
  ridge2.g.rotation.y=Math.PI*0.92; g.add(ridge2.g);
  const dust=makeFlow({n:o.dustN===undefined?300:o.dustN,box:[110,10,44],pos:[0,2.6,-16],
    color:o.dustC===undefined?0x6a5442:o.dustC,size:15,speed:o.dustV===undefined?4.2:o.dustV,
    maxA:o.dustA===undefined?0.10:o.dustA});
  g.add(dust.points);
  return {g:g,grd:grd,ridge:ridge,ridge2:ridge2,dust:dust};
}

/* —— 榆关关楼 makeGuanYG(o)：城台+门洞+女墙+台上两层楼阁（柱/腰檐/悬山顶/正脊，合批 1 mesh）——
   「摐金伐鼓下榆关」：大军自门洞鱼贯而出 */
function makeGuanYG(o){
  o=o||{};
  const B=new GeoBag();
  const W=o.W===undefined?17:o.W;
  const t1=new THREE.BoxGeometry(W,3.4,7.4);
  t1.translate(0,1.7,0); B.put(t1,0x2a1d11);
  const t2=new THREE.BoxGeometry(W-1.4,2.1,6.2);
  t2.translate(0,4.45,0); B.put(t2,0x332415);
  const men=new THREE.BoxGeometry(3.6,3.0,0.7);
  men.translate(0,1.5,3.5); B.put(men,0x0f0a06);
  for(let i=0;i<9;i++){
    const ml=new THREE.BoxGeometry(0.85,0.55,0.5);
    ml.translate(-W/2+0.7+i*(W-1.4)/8,5.75,3.0); B.put(ml,0x2a1d11);
  }
  for(let i=0;i<4;i++){
    const col=new THREE.CylinderGeometry(0.20,0.24,2.7,7);
    col.translate(-3.9+i*2.6,6.7,1.4); B.put(col,0x3a2a16);
  }
  const yy=new THREE.BoxGeometry(W-0.6,0.4,4.6);
  yy.translate(0,8.15,1.2); B.put(yy,0x402c14);
  const sh=new THREE.BoxGeometry(9.5,1.9,3.4);
  sh.translate(0,9.25,1.2); B.put(sh,0x33241a);
  const rg1=new THREE.BoxGeometry(10.5,0.34,2.2);
  rg1.rotateX(0.42); rg1.translate(0,10.55,0.4); B.put(rg1,0x241a10);
  const rg2=new THREE.BoxGeometry(10.5,0.34,2.2);
  rg2.rotateX(-0.42); rg2.translate(0,10.55,2.0); B.put(rg2,0x241a10);
  const ji=new THREE.BoxGeometry(11,0.28,0.5);
  ji.translate(0,11.15,1.2); B.put(ji,0x402c14);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:7,
    specular:0x5a4224,emissive:0x060402}),{c:0xb8906a,i:o.rim===undefined?0.16:o.rim,p:2.3})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 军旗 makeJingqiYG(o)：高杆+竿头旄缨+横长旗面（Plane 顶点波动，accent 顶边光）
   ——「旌旆逶迤」的军中之旗（横旗，非幡非王旗） */
function makeJingqiYG(o){
  o=o||{};
  const H=o.H===undefined?7.6:o.H, W=o.W===undefined?2.7:o.W, Hh=o.Hh===undefined?1.7:o.Hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.07,0.10,H,7);
  pole.translate(-W/2-0.3,H/2,0); B.put(pole,0x342413);
  const mao=new THREE.ConeGeometry(0.14,0.55,6);
  mao.translate(-W/2-0.3,H+0.24,0); B.put(mao,0xcabb9a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a5232,emissive:0x060402}),{c:0xb8906a,i:o.rim===undefined?0.20:o.rim,p:2.5})));
  const geo=new THREE.PlaneGeometry(W,Hh,10,4);
  geo.translate(W/2+0.02,0,0);
  const base=geo.attributes.position.array.slice(), cnt=geo.attributes.position.count;
  const cols=new Float32Array(cnt*3);
  const cb=new THREE.Color(0x45150c), ca=new THREE.Color(0xb8906a);
  for(let i=0;i<cnt;i++){
    const y=base[i*3+1];
    const t=Math.max(0,((y+Hh/2)/Hh-0.70)/0.30);
    const c=cb.clone().lerp(ca,t*0.6);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(cols,3));
  const flag=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,emissive:0x160b06}));
  flag.position.y=H-Hh/2-0.5; g.add(flag);
  const pos=geo.attributes.position, ph=(o.seed===undefined?26301:o.seed)%6.283;
  g.userData.update=function(t,k,wind){
    const kk=k===undefined?1:k, wd=(wind===undefined?1:wind)*kk;
    for(let i=0;i<pos.count;i++){
      const bx=base[i*3], by=base[i*3+1], f=bx/W;
      pos.array[i*3+2]=Math.sin(bx*1.7-t*3.3+by*0.8+ph)*0.30*f*f*wd;
      pos.array[i*3+1]=by-Math.abs(Math.sin(bx*1.3-t*2.5+ph))*0.08*f*f*wd;
    }
    pos.needsUpdate=true;
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 行军长龙 makeXingjunYG(o)：低模行军士一列（长衣+皮甲+圆盔，两臂前伸扛长兵，
   GeoBag 分 2 组合批）；o.pts 为 [x,z,ry] 队列点位（鱼贯下关的行军线）——「旌旆逶迤」 */
function makeXingjunYG(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26311:o.seed);
  const pts=o.pts||[[0,0,0]];
  const bags=[new GeoBag(),new GeoBag()];
  for(let i=0;i<pts.length;i++){
    const B=bags[i%2];
    const p=pts[i], x=p[0]+(R()-0.5)*0.7, z=p[1]+(R()-0.5)*0.7, ry=p[2]+(R()-0.5)*0.24;
    const robe=[0x241a10,0x2a1e12,0x201709,0x2c2113][Math.floor(R()*4)];
    const dk=shadeColor(robe,0.74);
    const bd=new THREE.CylinderGeometry(0.27,0.46,1.52,6);
    bd.rotateY(ry); bd.translate(x,0.76,z); B.put(bd,robe);
    const jia=new THREE.CylinderGeometry(0.36,0.42,0.44,6);
    jia.rotateY(ry); jia.translate(x,1.12,z); B.put(jia,0x362816);
    const hd=new THREE.SphereGeometry(0.155,6,5);
    hd.translate(x,1.70,z); B.put(hd,0x8a6a48);
    const kh=new THREE.SphereGeometry(0.18,6,5,0,Math.PI*2,0,Math.PI/2);
    kh.scale(1,0.9,1); kh.translate(x,1.68,z); B.put(kh,0x241d14);
    const ca=Math.cos(ry), sa=Math.sin(ry);
    const ox=dx=>dx*ca, oz=dx=>-dx*sa;
    B.put(limbGeo([x+ox(-0.32),1.30,z+oz(-0.32)+0.16],[x+ox(-0.06),1.04,z+oz(-0.06)+0.44],0.068,0.05,5),dk);
    B.put(limbGeo([x+ox(0.32),1.30,z+oz(0.32)+0.16],[x+ox(0.08),1.00,z+oz(0.08)+0.44],0.068,0.05,5),dk);
    const sp=new THREE.CylinderGeometry(0.024,0.034,3.1,5);
    sp.rotateZ(0.30); sp.rotateY(ry);
    sp.translate(x+ox(-0.30),1.66,z+oz(-0.30)+0.24); B.put(sp,0x44341e);
    const tp=new THREE.ConeGeometry(0.05,0.28,5);
    tp.rotateZ(0.30); tp.rotateY(ry);
    tp.translate(x+ox(-0.30)-Math.sin(0.30)*1.55*0+(-Math.sin(0.30)*1.55)*ca,1.66+Math.cos(0.30)*1.55,z+oz(-0.30)+0.24+(-Math.sin(0.30)*1.55)*(-sa));
    B.put(tp,0x7a6a44);
  }
  const g=new THREE.Group();
  for(let i=0;i<2;i++){
    g.add(bags[i].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
      shininess:5,specular:0x2a2014,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  }
  return g;
}

/* —— 立鼓 makeLiguYG(o)：竖立扁鼓+双向 X 鼓架+鼓钉（合批 1 mesh）——「摐金伐鼓」的军中战鼓 */
function makeLiguYG(o){
  o=o||{};
  const B=new GeoBag();
  const gu=new THREE.CylinderGeometry(0.92,0.92,0.52,14);
  gu.rotateX(Math.PI/2); gu.translate(0,1.75,0); B.put(gu,0x4a2c16);
  for(let sd=0;sd<2;sd++){
    const mz=new THREE.CylinderGeometry(0.95,0.95,0.07,14);
    mz.rotateX(Math.PI/2); mz.translate(0,1.75,sd?0.28:-0.28); B.put(mz,0x2a1810);
    for(let i=0;i<8;i++){
      const a=i/8*Math.PI*2;
      const stud=new THREE.SphereGeometry(0.045,5,4);
      stud.translate(Math.cos(a)*0.88,1.75+Math.sin(a)*0.88,sd?0.30:-0.30);
      B.put(stud,0x8a6238);
    }
  }
  for(let sd=0;sd<2;sd++){
    for(let p2=0;p2<2;p2++){
      const pz=sd?0.62:-0.62, px=p2?0.55:-0.55;
      B.put(limbGeo([px,0,pz-0.30],[px,1.95,pz+0.30],0.065,0.05,5),0x241a0e);
      B.put(limbGeo([px,0,pz+0.30],[px,1.95,pz-0.30],0.065,0.05,5),0x241a0e);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:9,
    specular:0x5a4024,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.16:o.rim,p:2.3})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 东北烟尘 makeYanchenYG(o)：暗色烟柱缓升+底部烽燧余光——「汉家烟尘在东北」
   （烟柱在画面右后方，即「东北」方向） */
function makeYanchenYG(o){
  o=o||{};
  const g=new THREE.Group();
  const x=o.x===undefined?26:o.x, z=o.z===undefined?-64:o.z;
  const smoke=makeGlow({n:o.n===undefined?18:o.n,box:[7,28,7],pos:[x,15,z],color:0x453422,
    size:9,speed:0.045,rise:1,add:false,maxA:0.16});
  smoke.points.renderOrder=3; g.add(smoke.points);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8502c,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(9,7,1); glow.position.set(x,2.4,z); glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?26302:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    smoke.update(t);
    glow.material.opacity=kk*0.16*(0.78+0.22*Math.sin(t*0.9+ph));
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 狼山猎火 makeLangshanYG(o)：弧段远山+山脊猎火三点（红光脉冲，fog:false 加色）
   ——「单于猎火照狼山」：敌境山峦上战火将起之兆 */
function makeLangshanYG(o){
  o=o||{};
  const g=new THREE.Group();
  const shan=makeRange({arc:o.arc===undefined?0.85:o.arc,a0:o.a0===undefined?2.35:o.a0,
    r:o.r===undefined?105:o.r,h:o.h===undefined?14:o.h,layers:2,peaks:4,
    seed:o.seed===undefined?26353:o.seed,color:0x0e0a06,atmo:0x2e2114,fogK:0.62,glowK:0.06,
    glow:0xd88050,y:-8,order:-4});
  g.add(shan.g);
  const fires=[];
  const fx=o.fx||[[30,2.2,-70],[38,4.4,-78],[46,2.8,-87]];
  for(let i=0;i<fx.length;i++){
    const f=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd86030,
      transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    f.scale.set(5+i*1.5,5+i*1.5,1);
    f.position.set(fx[i][0],fx[i][1],fx[i][2]); f.renderOrder=3; g.add(f); fires.push(f);
  }
  const ph=(o.seed===undefined?26303:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    shan.update(t,0);
    for(let i=0;i<fires.length;i++){
      fires[i].material.opacity=kk*0.30*(0.55+0.45*Math.pow(Math.max(0,Math.sin(t*1.25+i*1.8+ph)),3));
    }
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 牙帐 makeYaZhangYG(o)：穹顶毡帐（帐顶缨+帐裙）+帐门口暖光+帐内暖光点光+
   两名歌舞剪影（含蓄：逆光剪影在帐门口光影里缓摇，不见面目衣色）——
   标志性瞬间「美人帐下犹歌舞」的帐内一侧 */
function makeYaZhangYG(o){
  o=o||{};
  const g=new THREE.Group();
  const R=seedRnd(o.seed===undefined?26321:o.seed);
  const dome=new THREE.Mesh(new THREE.SphereGeometry(3.1,16,10,0,Math.PI*2,0,Math.PI/2),
    rimHook(new THREE.MeshPhongMaterial({color:0x241709,shininess:5,specular:0x4a341c,
      emissive:0x100904,side:THREE.DoubleSide}),{c:0xb8906a,i:o.rim===undefined?0.14:o.rim,p:2.2}));
  dome.scale.set(1,0.82,1); g.add(dome);
  const skirt=new THREE.Mesh(new THREE.CylinderGeometry(3.18,3.34,0.6,16,1,true),
    new THREE.MeshPhongMaterial({color:0x1e1208,shininess:4,emissive:0x0d0703,side:THREE.DoubleSide}));
  skirt.position.y=0.3; g.add(skirt);
  const tip=new THREE.CylinderGeometry(0.045,0.07,1.0,6);
  tip.translate(0,3.4,0);
  const ying=new THREE.ConeGeometry(0.14,0.5,6);
  ying.translate(0,4.05,0);
  const topB=new GeoBag(); topB.put(tip,0x342413); topB.put(ying,0xb8906a);
  const topM=new THREE.Mesh(mergeGeos(topB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
      specular:0x6a5232,emissive:0x080502}),{c:0xb8906a,i:0.24,p:2.5}));
  g.add(topM);
  /* 帐内暖光（点光）+帐门口暖光（sprite，初值=峰值） */
  const inLight=new THREE.PointLight(0xd88a48,1.15,24);
  inLight.position.set(0,2.1,0); g.add(inLight);
  const doorOp=o.doorOp===undefined?0.85:o.doorOp;
  const door=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffa050,
    transparent:true,opacity:doorOp,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  door.scale.set(4.6,4.1,1); door.position.set(-4.25,1.60,0.30); door.renderOrder=3; g.add(door);
  const core=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc078,
    transparent:true,opacity:0.65,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  core.scale.set(2.1,2.1,1); core.position.set(-4.05,1.45,0.30); core.renderOrder=3; g.add(core);
  const fabric=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd89048,
    transparent:true,opacity:0.11,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  fabric.scale.set(8.5,6.0,1); fabric.position.set(0,2.0,0); fabric.renderOrder=3; g.add(fabric);
  /* 帐门双 flap：门口实体感（门朝 -x，rotation 由摆位决定） */
  const flapB=new GeoBag();
  const f1=new THREE.BoxGeometry(1.35,2.3,0.07);
  f1.rotateY(0.5); f1.translate(-3.85,1.15,0.95); flapB.put(f1,0x1a0f06);
  const f2=new THREE.BoxGeometry(1.35,2.3,0.07);
  f2.rotateY(-0.4); f2.translate(-3.85,1.15,-0.50); flapB.put(f2,0x170d05);
  const flapM=new THREE.Mesh(mergeGeos(flapB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
      specular:0x3a2c1a,emissive:0x060302}),{c:0xb8906a,i:0.16,p:2.2}));
  g.add(flapM);
  /* 歌舞剪影×2（含蓄）：逆光剪影在帐门口，袖臂上举，缓摇如舞 */
  const dancers=[];
  const dB1=new GeoBag();
  const rb1=new THREE.ConeGeometry(0.40,1.6,7);
  rb1.translate(0,0.80,0); dB1.put(rb1,0x140c06);
  const hd1=new THREE.SphereGeometry(0.20,6,5);
  hd1.translate(0,1.76,0); dB1.put(hd1,0x140c06);
  dB1.put(limbGeo([-0.26,1.42,0],[-0.64,2.06,0.06],0.062,0.045,5),0x140c06);
  dB1.put(limbGeo([0.26,1.42,0],[0.62,1.98,-0.08],0.062,0.045,5),0x140c06);
  const d1=new THREE.Mesh(mergeGeos(dB1.list),
    new THREE.MeshBasicMaterial({color:0x140c06,transparent:true,opacity:0.94,depthWrite:false}));
  d1.position.set(-3.75,0.30,1.15); d1.renderOrder=2; g.add(d1); dancers.push(d1);
  const dB2=new GeoBag();
  const rb2=new THREE.ConeGeometry(0.34,1.42,7);
  rb2.translate(0,0.71,0); dB2.put(rb2,0x120b05);
  const hd2=new THREE.SphereGeometry(0.175,6,5);
  hd2.translate(0,1.56,0); dB2.put(hd2,0x120b05);
  dB2.put(limbGeo([-0.22,1.24,0],[-0.56,1.84,0.05],0.056,0.04,5),0x120b05);
  dB2.put(limbGeo([0.22,1.24,0],[0.54,1.78,-0.06],0.056,0.04,5),0x120b05);
  const d2=new THREE.Mesh(mergeGeos(dB2.list),
    new THREE.MeshBasicMaterial({color:0x120b05,transparent:true,opacity:0.9,depthWrite:false}));
  d2.position.set(-4.30,0.28,-0.10); d2.renderOrder=2; g.add(d2); dancers.push(d2);
  const ph=(o.seed===undefined?26321:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    door.material.opacity=kk*doorOp*(0.76+0.24*Math.sin(t*1.9+ph));
    core.material.opacity=kk*0.65*(0.80+0.20*Math.sin(t*1.9+ph));
    fabric.material.opacity=kk*0.10*(0.85+0.15*Math.sin(t*1.35+ph*2));
    inLight.intensity=kk*1.15*(0.92+0.08*Math.sin(t*1.9+ph));
    d1.rotation.z=0.085*Math.sin(t*1.65+ph)*kk;
    d2.rotation.z=-0.075*Math.sin(t*1.42+ph*1.3)*kk;
    d1.rotation.y=0.16*Math.sin(t*0.62+ph);
    d2.rotation.y=0.14*Math.sin(t*0.55+ph*1.7);
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 苦战群像 makeKuzhanYG(o)：帐外寒沙苦战低模（半跪撑刀/弓身前突/单膝半仆/拄兵喘息/
   执盾低伏，GeoBag 分 2 组合批；姿态写意，无血腥直写）——「战士军前半死生」的帐外一侧 */
function makeKuzhanYG(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26331:o.seed);
  const n=o.n===undefined?5:o.n;
  const bags=[new GeoBag(),new GeoBag()];
  const robeC=[0x1c130a,0x201709,0x181008,0x231a0e];
  for(let i=0;i<n;i++){
    const B=bags[i%2];
    const x=(R()-0.5)*(o.w===undefined?10:o.w);
    const z=(R()-0.5)*(o.d===undefined?7:o.d);
    const robe=robeC[Math.floor(R()*4)], dk=shadeColor(robe,0.72);
    const pose=i%5;
    if(pose===0){ /* 半跪撑刀 */
      const bd=new THREE.CylinderGeometry(0.24,0.42,1.05,6);
      bd.rotateX(0.16); bd.translate(x,0.72,z); B.put(bd,robe);
      const lg=new THREE.CylinderGeometry(0.09,0.11,0.62,5);
      lg.rotateX(1.1); lg.translate(x+0.30,0.22,z+0.22); B.put(lg,dk);
      const hd=new THREE.SphereGeometry(0.145,6,5);
      hd.translate(x+0.02,1.32,z+0.10); B.put(hd,0x8a6c50);
      const kh=new THREE.SphereGeometry(0.17,6,5,0,Math.PI*2,0,Math.PI/2);
      kh.scale(1,0.9,1); kh.translate(x+0.02,1.30,z+0.10); B.put(kh,0x201a12);
      B.put(limbGeo([x-0.28,1.05,z+0.06],[x+0.10,0.72,z+0.44],0.062,0.045,5),dk);
      const dao=new THREE.BoxGeometry(0.05,0.78,0.12);
      dao.rotateZ(-0.5); dao.translate(x+0.20,1.02,z+0.52); B.put(dao,0x6a7078);
    }else if(pose===1){ /* 弓身前突 */
      const bd=new THREE.CylinderGeometry(0.25,0.44,1.45,6);
      bd.rotateX(0.42); bd.translate(x,0.86,z+0.16); B.put(bd,robe);
      const hd=new THREE.SphereGeometry(0.15,6,5);
      hd.translate(x,1.42,z+0.52); B.put(hd,0x8a6c50);
      const kh=new THREE.SphereGeometry(0.175,6,5,0,Math.PI*2,0,Math.PI/2);
      kh.scale(1,0.9,1); kh.rotateX(0.42); kh.translate(x,1.40,z+0.52); B.put(kh,0x201a12);
      B.put(limbGeo([x-0.30,1.22,z+0.28],[x-0.34,0.86,z+0.72],0.062,0.045,5),dk);
      B.put(limbGeo([x+0.30,1.22,z+0.28],[x+0.36,0.84,z+0.74],0.062,0.045,5),dk);
      const dao=new THREE.BoxGeometry(0.05,0.72,0.12);
      dao.rotateZ(0.9); dao.translate(x+0.48,1.06,z+0.86); B.put(dao,0x6a7078);
    }else if(pose===2){ /* 单膝半仆 */
      const bd=new THREE.CylinderGeometry(0.24,0.40,1.1,6);
      bd.rotateX(0.95); bd.translate(x,0.62,z+0.18); B.put(bd,robe);
      const hd=new THREE.SphereGeometry(0.145,6,5);
      hd.translate(x,1.10,z+0.60); B.put(hd,0x8a6c50);
      B.put(limbGeo([x-0.26,0.72,z+0.30],[x-0.44,0.06,z+0.52],0.058,0.042,5),dk);
      B.put(limbGeo([x+0.26,0.72,z+0.30],[x+0.50,0.10,z+0.42],0.058,0.042,5),dk);
      const sp=new THREE.CylinderGeometry(0.026,0.034,2.6,5);
      sp.rotateZ(0.5); sp.translate(x-0.32,1.10,z+0.10); B.put(sp,0x44341e);
    }else if(pose===3){ /* 拄兵喘息 */
      const bd=new THREE.CylinderGeometry(0.26,0.44,1.5,6);
      bd.rotateX(-0.12); bd.translate(x,0.90,z); B.put(bd,robe);
      const hd=new THREE.SphereGeometry(0.15,6,5);
      hd.translate(x,1.78,z-0.06); B.put(hd,0x8a6c50);
      const kh=new THREE.SphereGeometry(0.175,6,5,0,Math.PI*2,0,Math.PI/2);
      kh.scale(1,0.9,1); kh.translate(x,1.76,z-0.06); B.put(kh,0x201a12);
      const sp=new THREE.CylinderGeometry(0.026,0.034,2.9,5);
      sp.rotateZ(0.24); sp.translate(x+0.34,1.30,z+0.18); B.put(sp,0x44341e);
      B.put(limbGeo([x-0.30,1.24,z+0.10],[x+0.22,1.28,z+0.24],0.06,0.044,5),dk);
    }else{ /* 执盾低伏 */
      const bd=new THREE.CylinderGeometry(0.26,0.44,1.2,6);
      bd.rotateX(0.55); bd.translate(x,0.68,z+0.10); B.put(bd,robe);
      const hd=new THREE.SphereGeometry(0.145,6,5);
      hd.translate(x,1.20,z+0.38); B.put(hd,0x8a6c50);
      const kh=new THREE.SphereGeometry(0.17,6,5,0,Math.PI*2,0,Math.PI/2);
      kh.scale(1,0.9,1); kh.rotateX(0.55); kh.translate(x,1.18,z+0.38); B.put(kh,0x201a12);
      const dun=new THREE.CylinderGeometry(0.46,0.46,0.09,9,1,false,0,Math.PI);
      dun.rotateZ(Math.PI/2); dun.rotateX(-0.4);
      dun.translate(x-0.42,0.70,z+0.44); B.put(dun,0x33261a);
      B.put(limbGeo([x+0.28,1.00,z+0.26],[x+0.42,0.66,z+0.60],0.06,0.044,5),dk);
    }
  }
  const g=new THREE.Group();
  for(let i=0;i<2;i++){
    g.add(bags[i].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
      shininess:5,specular:0x3a424c,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.26:o.rim,p:2.2})));
  }
  return g;
}

/* —— 残戈残旗 makeCangeYG(o)：折断斜插的长戈两支+一面残破斜旗（合批 1 mesh）——
   战后/危局的沙场遗物，写意不血腥 */
function makeCangeYG(o){
  o=o||{};
  const B=new GeoBag();
  const items=o.items||[[-0.6,0,0.45],[-1.6,0.6,-0.35]];
  for(let i=0;i<items.length;i++){
    const p=items[i];
    const sh=new THREE.CylinderGeometry(0.03,0.045,2.6,5);
    sh.rotateZ(p[2]); sh.translate(p[0],1.05,p[1]); B.put(sh,0x3a2c1a);
    const yuan=new THREE.ConeGeometry(0.05,0.34,5);
    yuan.rotateZ(-Math.PI/2+p[2]);
    yuan.translate(p[0]+Math.cos(p[2])*1.28,1.05+Math.sin(p[2])*1.28,p[1]); B.put(yuan,0x70624a);
  }
  const flag=new THREE.PlaneGeometry(1.5,0.95,4,2);
  flag.rotateZ(-0.35);
  flag.translate(-2.5,2.55,0.2);
  B.put(flag,0x4a1c10);
  const fp=new THREE.CylinderGeometry(0.035,0.05,3.3,5);
  fp.rotateZ(-0.35); fp.translate(-2.5,1.5,0.2); B.put(fp,0x2e2114);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x4a4034,emissive:0x050302,side:THREE.DoubleSide}),{c:0xb8906a,i:o.rim===undefined?0.12:o.rim,p:2.1})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 塞草枯黄 makeSaicaoYG(o)：一丛丛枯草（每丛 3-5 茎细锥，GeoBag 合批 1 mesh）
   ——「大漠穷秋塞草腓」：穷秋草木凋零 */
function makeSaicaoYG(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26341:o.seed);
  const n=o.n===undefined?12:o.n;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const cx=(R()-0.5)*(o.w===undefined?46:o.w), cz=(R()-0.5)*(o.d===undefined?30:o.d)+(o.z===undefined?0:o.z);
    const m=3+Math.floor(R()*3);
    for(let j=0;j<m;j++){
      const h=0.45+R()*0.55, a=R()*6.283, rr=R()*0.28;
      const st=new THREE.ConeGeometry(0.045,h,4);
      st.rotateZ((R()-0.5)*0.55); st.rotateX((R()-0.5)*0.55);
      st.translate(cx+Math.sin(a)*rr,h*0.42,cz+Math.cos(a)*rr);
      B.put(st,R()>0.5?0x4a3a1c:0x3a2c14);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x2a2014,emissive:0x040302}),{c:0xb8906a,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  return g;
}

/* —— 孤城远影 makeGuchengYG(o)：城墙一段+女墙+角楼（合批 1 mesh）——「孤城落日斗兵稀」 */
function makeGuchengYG(o){
  o=o||{};
  const B=new GeoBag();
  const W=o.W===undefined?24:o.W;
  const wall=new THREE.BoxGeometry(W,4.2,3.0);
  wall.translate(0,2.1,0); B.put(wall,0x241810);
  const wall2=new THREE.BoxGeometry(W-2,1.4,2.2);
  wall2.translate(0,4.9,0); B.put(wall2,0x2a1c11);
  for(let i=0;i<10;i++){
    const ml=new THREE.BoxGeometry(0.8,0.6,0.5);
    ml.translate(-W/2+0.9+i*(W-1.8)/9,5.9,0.8); B.put(ml,0x241810);
  }
  const tw=new THREE.BoxGeometry(4.2,6.4,4.2);
  tw.translate(W/2-1.6,3.2,-1.4); B.put(tw,0x281a0f);
  const tr1=new THREE.BoxGeometry(5.0,0.3,2.6);
  tr1.rotateX(0.5); tr1.translate(W/2-1.6,7.2,-2.2); B.put(tr1,0x1f140c);
  const tr2=new THREE.BoxGeometry(5.0,0.3,2.6);
  tr2.rotateX(-0.5); tr2.translate(W/2-1.6,7.2,-0.6); B.put(tr2,0x1f140c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x4a3420,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.20:o.rim,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 蓟北戍楼 makeShulouYG(o)：夯土高台两层+顶层女墙平台+台角木架悬刁斗+刁斗声光脉冲
   ——「征人蓟北空回首」「寒声一夜传刁斗」的边庭一侧（征人立于顶层平台，build 侧对位） */
function makeShulouYG(o){
  o=o||{};
  const B=new GeoBag();
  const b1=new THREE.BoxGeometry(5.2,3.6,5.2);
  b1.translate(0,1.8,0); B.put(b1,0x281b10);
  const b2=new THREE.BoxGeometry(4.2,2.6,4.2);
  b2.translate(0,4.9,0); B.put(b2,0x2e2012);
  for(let i=0;i<4;i++){
    const fx=-1.6+i*1.06;
    const m1=new THREE.BoxGeometry(0.72,0.55,0.35);
    m1.translate(fx,6.47,2.0); B.put(m1,0x281b10);
    const m2=new THREE.BoxGeometry(0.72,0.55,0.35);
    m2.translate(fx,6.47,-2.0); B.put(m2,0x281b10);
  }
  const pole=new THREE.CylinderGeometry(0.05,0.07,1.7,5);
  pole.translate(1.45,7.0,1.45); B.put(pole,0x362616);
  const arm=new THREE.CylinderGeometry(0.035,0.035,0.9,5);
  arm.rotateZ(Math.PI/2); arm.translate(1.1,7.75,1.45); B.put(arm,0x362616);
  const dd=new THREE.CylinderGeometry(0.17,0.23,0.14,8);
  dd.rotateX(Math.PI/2); dd.translate(0.85,7.35,1.45); B.put(dd,0x6a5a3a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x4a3820,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.18:o.rim,p:2.2})));
  const tuo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcabfa8,
    transparent:true,opacity:0.22,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  tuo.scale.set(2.4,2.4,1); tuo.position.set(0.85,7.35,1.55); tuo.renderOrder=4; g.add(tuo);
  const ph=(o.seed===undefined?26361:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    tuo.material.opacity=kk*0.22*Math.pow(Math.max(0,Math.sin(t*1.05+ph)),14);
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 城南城郭 makeChengnanYG(o)：城墙一段+敞楼（台+楼头平顶+女墙，不封顶——思妇立于楼头）
   ——「少妇城南欲断肠」的家园一侧（灯火一点是全境唯一暖色） */
function makeChengnanYG(o){
  o=o||{};
  const W=o.W===undefined?15:o.W;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(W,3.2,1.8);
  wall.translate(0,1.6,0); B.put(wall,0x261a10);
  const nv=new THREE.BoxGeometry(W,0.55,0.7);
  nv.translate(0,3.45,0.45); B.put(nv,0x261a10);
  const tai=new THREE.BoxGeometry(5.6,3.4,5.6);
  tai.translate(0,1.7,0); B.put(tai,0x2a1c11);
  const lou=new THREE.BoxGeometry(4.4,2.8,4.4);
  lou.translate(0,4.8,0); B.put(lou,0x2e2012);
  for(let i=0;i<4;i++){
    const fx=-1.65+i*1.1;
    const m1=new THREE.BoxGeometry(0.7,0.5,0.32);
    m1.translate(fx,6.45,2.05); B.put(m1,0x2e2012);
    const m2=new THREE.BoxGeometry(0.7,0.5,0.32);
    m2.translate(fx,6.45,-2.05); B.put(m2,0x2e2012);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a3820,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.16:o.rim,p:2.2})));
  const lampOp=o.lampOp===undefined?0.22:o.lampOp;
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd89048,
    transparent:true,opacity:lampOp,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(3.0,3.0,1); lamp.position.set(1.5,6.6,1.4); lamp.renderOrder=3; g.add(lamp);
  const ph=(o.seed===undefined?26371:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    lamp.material.opacity=kk*lampOp*(0.80+0.20*Math.sin(t*1.1+ph));
    g.visible=kk>0.004;
  };
  return g;
}

/* —— 白刃军阵 makeBairenYG(o)：两列持刀军士（结阵相望）+ 每人一刀（独立 mesh）
   + 刀锋寒光 sprite（初值=峰值；update(t,k,sweep) 里寒光沿队列次第点亮）+
   冷光点光——末境「相看白刃血纷纷」的白刃一侧 */
function makeBairenYG(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26381:o.seed);
  const rowsA=o.rowsA||[[-5.6,-8.2,0.16],[-1.9,-8.5,-0.12],[1.9,-8.5,0.12],[5.6,-8.2,-0.16]];
  const rowsB=o.rowsB||[[-6.5,-12.6,0.20],[-2.2,-12.9,-0.16],[2.2,-12.9,0.16],[6.5,-12.6,-0.20]];
  const bags=[new GeoBag(),new GeoBag()];
  const blades=[],glints=[];
  const robeC=[0x231a0e,0x271d10,0x1f1609,0x2b2012];
  const g=new THREE.Group();
  function man(B,x,z,ry){
    const robe=robeC[Math.floor(R()*4)], dk=shadeColor(robe,0.74);
    const bd=new THREE.CylinderGeometry(0.28,0.48,1.56,6);
    bd.rotateY(ry); bd.translate(x,0.78,z); B.put(bd,robe);
    const jia=new THREE.CylinderGeometry(0.38,0.44,0.46,6);
    jia.rotateY(ry); jia.translate(x,1.14,z); B.put(jia,0x3a2c1a);
    for(let sd=0;sd<2;sd++){
      const sh=new THREE.SphereGeometry(0.13,6,5);
      sh.scale(1.15,0.7,1); sh.translate(x+(sd?0.42:-0.42),1.40,z);
      B.put(sh,0x443420);
    }
    const hd=new THREE.SphereGeometry(0.155,6,5);
    hd.translate(x,1.74,z); B.put(hd,0x8a6a48);
    const kh=new THREE.SphereGeometry(0.18,6,5,0,Math.PI*2,0,Math.PI/2);
    kh.scale(1,0.9,1); kh.translate(x,1.72,z); B.put(kh,0x241d14);
    const kn=new THREE.ConeGeometry(0.035,0.10,5);
    kn.translate(x,1.94,z); B.put(kn,0x6a5232);
    const ca=Math.cos(ry), sa=Math.sin(ry);
    B.put(limbGeo([x+(-0.32)*ca,1.34,z-(-0.32)*sa+0.14],[x+(-0.10)*ca,1.02,z+(-0.10)*sa+0.40],0.068,0.05,5),dk);
    B.put(limbGeo([x+(0.32)*ca,1.34,z-(0.32)*sa+0.14],[x+(0.12)*ca,1.00,z+(0.12)*sa+0.40],0.068,0.05,5),dk);
  }
  rowsA.concat(rowsB).forEach(function(p,i){
    man(bags[i%2],p[0],p[1],p[2]);
    const B=new GeoBag();
    const bing=new THREE.CylinderGeometry(0.032,0.04,0.44,5);
    bing.rotateZ(-0.62); bing.translate(p[0]+0.10,1.08,p[1]+0.42); B.put(bing,0x3a2c1a);
    const ren=new THREE.BoxGeometry(0.055,0.86,0.13);
    ren.rotateZ(-0.62); ren.translate(p[0]+0.26,1.52,p[1]+0.52); B.put(ren,0x8a9098);
    const bG=new THREE.Group();
    bG.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:34,
      specular:0xbac4cc,emissive:0x0a0c10}),{c:0xb8906a,i:0.10,p:2.6})));
    g.add(bG); blades.push(bG);
    const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8e4ec,
      transparent:true,opacity:0.55,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    gl.scale.set(1.15,1.15,1);
    gl.position.set(p[0]+0.26+Math.sin(0.62)*0.34,1.52+Math.cos(0.62)*0.34,p[1]+0.55);
    gl.renderOrder=4; g.add(gl); glints.push(gl);
  });
  const meshA=bags[0].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x2a2014,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.26:o.rim,p:2.2}));
  const meshB=bags[1].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
    shininess:6,specular:0x2a2014,emissive:0x050302}),{c:0xb8906a,i:o.rim===undefined?0.20:o.rim,p:2.2}));
  g.add(meshA); g.add(meshB);
  const cold=new THREE.PointLight(0xcfe0e8,1.5,34);
  cold.position.set(0,2.6,-13); g.add(cold);
  g.userData.update=function(t,k,sweep){
    const kk=k===undefined?1:k, sw=sweep===undefined?-1:sweep;
    let wsum=0;
    for(let i=0;i<glints.length;i++){
      const w=sw<0?0:Math.max(0,Math.min(1,1-Math.abs(sw*1.5-i*0.10)/0.22));
      wsum+=w;
      const env=Math.min(1,0.34+0.10*Math.sin(t*2.3+i*1.7)+0.56*w);
      glints[i].material.opacity=kk*0.55*env;
    }
    cold.intensity=kk*1.5*Math.min(1,wsum/3.2);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 一骑远影 makeYijiYG(o)：地平线上一人一马的极简剪影（合批 1 mesh）——
   「至今犹忆李将军」的写意远象：大漠尽头一骑巡边 */
function makeYijiYG(o){
  o=o||{};
  const B=new GeoBag();
  const s=o.s===undefined?1:o.s;
  const bd=new THREE.SphereGeometry(0.52*s,7,5);
  bd.scale(1.7,1.0,0.62); bd.translate(0,1.05*s,0); B.put(bd,0x14100a);
  const nk=new THREE.SphereGeometry(0.20*s,6,5);
  nk.scale(1.0,1.7,0.6); nk.translate(0.78*s,1.62*s,0); B.put(nk,0x14100a);
  const hd=new THREE.SphereGeometry(0.14*s,6,5);
  hd.scale(1.5,0.9,0.7); hd.translate(1.02*s,1.85*s,0); B.put(hd,0x14100a);
  [[0.42,-0.14],[0.42,0.14],[-0.44,-0.15],[-0.44,0.15]].forEach(function(p){
    const lg=new THREE.CylinderGeometry(0.045*s,0.055*s,0.85*s,4);
    lg.translate(p[0]*s,0.42*s,p[1]*s); B.put(lg,0x14100a);
  });
  const rd=new THREE.CylinderGeometry(0.11*s,0.16*s,0.62*s,5);
  rd.translate(0.05*s,1.72*s,0); B.put(rd,0x14100a);
  const rh=new THREE.SphereGeometry(0.11*s,6,5);
  rh.translate(0.05*s,2.12*s,0); B.put(rh,0x14100a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x3a3428,emissive:0x030202}),{c:0xb8906a,i:o.rim===undefined?0.14:o.rim,p:2.0})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 边塞人物（贯穿造型系，每次 build 新建材质） */
function ygFigure(scale,pose,robe){
  return makeFigure({pose:pose||'独立',robe:robe||0x2e2314,belt:0x8a6238,skin:0xd9b189,
    collar:0x6a4a28,hair:0x1a140c,hat:'发髻',rimC:0xb8906a,rim:0.42,noProp:true,
    scale:scale===undefined?1:scale});
}

function bCover(){ // 卷首 · 暮色大漠全览：孤城远影、榆关在望、牙帐一点暖光、行军线逶迤、狼山猎火
  const g=new THREE.Group();
  const base=makeDamoYG({}); g.add(base.g);
  const guan=makeGuanYG({scale:0.9}); guan.position.set(-22,-1.8,-74); guan.rotation.y=0.25; g.add(guan);
  const cheng=makeGuchengYG({scale:0.85}); cheng.position.set(20,-1.8,-92); cheng.rotation.y=-0.2; g.add(cheng);
  const lang=makeLangshanYG({}); lang.position.set(-6,0,-6); g.add(lang);
  const march=makeXingjunYG({seed:26312,pts:[[0,-58,0.4],[3,-52,0.5],[7,-46,0.6],[11,-40,0.7],[15,-34,0.8],[19,-29,0.9]]});
  march.position.set(-6,0,4); g.add(march);
  const crowd=makeCrowd({n:10,rect:[-16,-84,26,14],seed:26313,color:0x181008,rimC:0xb8906a,rim:0.13,y:-1.8});
  g.add(crowd.mesh);
  const tent=makeYaZhangYG({scale:0.85}); tent.position.set(8,-1.78,-52); tent.rotation.y=1.1; g.add(tent);
  const flag=makeJingqiYG({seed:26301}); flag.position.set(3,-1.8,-62); g.add(flag);
  const qi=makeJingqiYG({H:6.8,seed:26302}); qi.position.set(-16,-1.8,-56); qi.rotation.y=-0.3; g.add(qi);
  const dust2=makeYanchenYG({x:44,z:-96}); g.add(dust2);
  const mist=makeMist({n:6,spread:[210,14,80],pos:[0,5,-56],scale:68,color:0x4a3826,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[160,18,66],pos:[0,9,-34],color:0x8a7048,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x14100a,seed:26314,rim:0.10,rimC:0xb8906a});
  fg1.g.position.set(-12,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x14100a,seed:26315,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(13,-1.8,12); g.add(fg2.g);
  addLights(g,{c:0xb08850,i:0.34,p:[-44,52,-24]},{c:0x2a1e12,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    lang.userData.update(t,k); dust2.userData.update(t,k);
    tent.userData.update(t,k);
    flag.userData.update(t,k,1); qi.userData.update(t,k,1);
    crowd.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bChuchen(){ // 壹 · 烟尘汉家 —— 汉家烟尘在东北……单于猎火照狼山：
                    // 昼昏黄烟尘蔽日，榆关关楼下大军鱼贯而出，旌旆逶迤，立鼓催行；东北烟尘、狼山猎火
  const g=new THREE.Group();
  const base=makeDamoYG({seed1:26353,seed2:26354,dustA:0.13,dustV:5.0,c1:0x180f08,c2:0x2a1a0c}); g.add(base.g);
  const guan=makeGuanYG({}); guan.position.set(-2.5,-1.8,-30); guan.rotation.y=0.06; g.add(guan);
  /* 行军长龙：出关鱼贯而下，折向右前 */
  const march=makeXingjunYG({seed:26312,pts:[
    [-1.5,-26.5,0.1],[0,-24.5,0.35],[1.8,-22.5,0.5],[3.6,-20.5,0.62],
    [5.6,-18.4,0.72],[7.8,-16.2,0.82],[10.2,-13.8,0.9],[12.6,-11.4,0.95],
    [15.0,-9.2,1.0],[17.4,-7.2,1.05],[-4.6,-24.8,0.2],[-3.4,-23.4,0.42]]});
  g.add(march);
  const crowd=makeCrowd({n:14,rect:[-12,-44,30,10],seed:26316,color:0x181008,rimC:0xb8906a,rim:0.12,y:-1.8});
  g.add(crowd.mesh);
  /* 旌旆三杆：沿行军线逶迤 */
  const f1=makeJingqiYG({seed:26301}); f1.position.set(-7.5,-1.8,-27.5); f1.rotation.y=0.3; g.add(f1);
  const f2=makeJingqiYG({H:7.0,seed:26302}); f2.position.set(2.5,-1.8,-20.5); f2.rotation.y=-0.25; g.add(f2);
  const f3=makeJingqiYG({H:6.6,seed:26303}); f3.position.set(9.5,-1.8,-13.5); f3.rotation.y=-0.5; g.add(f3);
  /* 立鼓+鼓手：摐金伐鼓催行 */
  const gu=makeLiguYG({}); gu.position.set(-10.5,-1.8,-16.5); gu.rotation.y=0.5; g.add(gu);
  const drummer=ygFigure(0.98,'指月',0x30241a); drummer.position.set(-12.3,-1.78,-15.0);
  drummer.rotation.y=1.15; g.add(drummer);
  /* 主将按剑立于门侧：男儿本自重横行 */
  const cmd=ygFigure(1.02,'按剑',0x33261a); cmd.position.set(-6.6,-1.78,-24.5);
  cmd.rotation.y=0.75; g.add(cmd);
  /* 东北烟尘（右后）+狼山猎火（右后远山） */
  const yc=makeYanchenYG({x:27,z:-60}); g.add(yc);
  const lang=makeLangshanYG({fx:[[31,2.6,-66],[39,4.8,-74],[47,3.0,-84]]}); lang.position.set(4,0,4); g.add(lang);
  const mist=makeMist({n:6,spread:[200,14,74],pos:[0,5,-50],scale:64,color:0x54402a,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[150,17,62],pos:[0,9,-30],color:0xa8824e,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:26317,rim:0.10,rimC:0xb8906a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:26318,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0xc89050,i:0.44,p:[44,52,-26]},{c:0x2e2012,i:0.60});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    f1.userData.update(t,k,1); f2.userData.update(t,k,1.1); f3.userData.update(t,k,1.2);
    yc.userData.update(t,k); lang.userData.update(t,k);
    drummer.update(t,k); cmd.update(t,k);
    crowd.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bWeiju(){ // 贰（标志性瞬间）· 萧条边庭 —— 山川萧条极边土……力尽关山未解围：
                   // 落日孤城。右侧牙帐暖光透帐、门口歌舞剪影缓摇（含蓄）；左侧寒沙苦战群像低伏；
                   // 一帐之隔，两个世界。塞草腓、残戈斜插
  const g=new THREE.Group();
  const base=makeDamoYG({seed1:26355,seed2:26356,dustA:0.12,dustV:4.4,c1:0x140d07,c2:0x221508}); g.add(base.g);
  /* 标志性瞬间核心：牙帐（右）暖光歌舞剪影 */
  const tent=makeYaZhangYG({seed:26321,scale:1.18}); tent.position.set(10.5,-1.78,-15);
  tent.rotation.y=1.25; g.add(tent);
  const shuaiqi=makeJingqiYG({H:8.0,W:2.4,seed:26304}); shuaiqi.position.set(14.5,-1.8,-21);
  shuaiqi.rotation.y=-0.4; g.add(shuaiqi);
  /* 帐外苦战（左）：低伏群像+残戈残旗 */
  const kuzhan=makeKuzhanYG({seed:26331,n:6,w:11,d:8}); kuzhan.position.set(-9.5,-1.78,-16); g.add(kuzhan);
  const coldL=new THREE.PointLight(0x8a94a8,0.85,32);
  coldL.position.set(-9,4.2,-16); g.add(coldL);
  const kuzhan2=makeKuzhanYG({seed:26332,n:3,w:7,d:5}); kuzhan2.position.set(-7,-1.78,-23); g.add(kuzhan2);
  const cange=makeCangeYG({}); cange.position.set(-14,-1.78,-13.5); cange.rotation.y=0.4; g.add(cange);
  /* 塞草腓：枯草一地 */
  const cao=makeSaicaoYG({seed:26341,n:16,w:44,d:26,z:-8}); g.add(cao);
  const cao2=makeSaicaoYG({seed:26342,n:7,w:16,d:8,z:8}); g.add(cao2);
  /* 孤城落日：孤城（中远）+落日光晕（帐侧低垂） */
  const cheng=makeGuchengYG({scale:0.9}); cheng.position.set(-2,-1.8,-56); cheng.rotation.y=0.1; g.add(cheng);
  const sun1=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd87040,
    transparent:true,opacity:0.15,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sun1.scale.set(52,30,1); sun1.position.set(36,3.5,-96); sun1.renderOrder=2; g.add(sun1);
  const sun2=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe89858,
    transparent:true,opacity:0.22,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  sun2.scale.set(17,11,1); sun2.position.set(36,2.2,-95); sun2.renderOrder=2; g.add(sun2);
  const mist=makeMist({n:6,spread:[210,14,46],pos:[0,5,-62],scale:62,color:0x4a3020,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[150,16,60],pos:[0,8,-28],color:0x9a7848,size:4.0,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x100b06,seed:26319,rim:0.10,rimC:0xb8906a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x100b06,seed:26320,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0xc07c48,i:0.34,p:[52,26,-22]},{c:0x2a1c10,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    tent.userData.update(t,k); shuaiqi.userData.update(t,k,1.15);
    coldL.intensity=k*0.85*(0.92+0.08*Math.sin(t*0.9));
    sun1.material.opacity=k*0.15*(0.90+0.10*Math.sin(t*0.5));
    sun2.material.opacity=k*0.22*(0.92+0.08*Math.sin(t*0.8));
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXuanwang(){ // 叁 · 两地悬望 —— 铁衣远戍辛勤久……寒声一夜传刁斗：
                     // 左蓟北：戍楼高台、征人回首望乡、刁斗夜声；右城南：城郭楼头、思妇凭栏、灯暖一点；
                     // 中间绝域苍茫一雾相隔，阵云低垂，共月高悬
  const g=new THREE.Group();
  const base=makeDamoYG({seed1:26357,seed2:26358,dustA:0.07,dustV:2.6,dustC:0x4a3e30,
    c1:0x0e0a06,c2:0x181009,h1:14}); g.add(base.g);
  /* 左·蓟北：戍楼+征人回首+刁斗夜声（征人立于顶层平台：顶层 local 6.2 → 世界 y≈4.4） */
  const shulou=makeShulouYG({seed:26361,scale:1.15,rim:0.26}); shulou.position.set(-13.5,-1.8,-17); g.add(shulou);
  const zheng=ygFigure(0.95,'指月',0x241b10); zheng.position.set(-13.9,5.37,-16.4);
  zheng.rotation.y=-0.9; g.add(zheng);
  const moonL=new THREE.PointLight(0x9aa4b8,0.5,26);
  moonL.position.set(-12.5,5.6,-14.5); g.add(moonL);
  /* 右·城南：城郭楼头+思妇凭栏+灯暖（楼头 local 6.2 → 世界 y≈4.4） */
  const chengnan=makeChengnanYG({seed:26371,scale:1.12,rim:0.24,lampOp:0.30}); chengnan.position.set(14.5,-1.8,-19); g.add(chengnan);
  const sifu=ygFigure(0.88,'独立',0x3a2a2a); sifu.position.set(13.9,5.19,-17.8);
  sifu.rotation.y=-1.15; g.add(sifu);
  /* 中间·绝域苍茫：低雾横隔 */
  const gap=makeMist({n:5,spread:[74,4,16],pos:[0,1.0,-22],scale:32,color:0x241a10,op:0.11});
  g.add(gap.g);
  /* 阵云低垂+杀气横流 */
  const zhenyun=makeMist({n:5,spread:[110,7,26],pos:[0,14,-44],scale:30,color:0x141009,op:0.16});
  g.add(zhenyun.g);
  const shaqi=makeFlow({n:110,box:[120,8,20],pos:[0,13,-40],color:0x2a2014,size:16,speed:1.6,maxA:0.10});
  g.add(shaqi.points);
  /* 远处边城剪影（左后）与烽墩（右后）：两地各自的天地 */
  const yuan1=makeRange({arc:0.7,a0:-2.6,r:120,h:10,layers:2,peaks:3,seed:26359,color:0x0d0906,
    atmo:0x2e2114,fogK:0.60,glowK:0.05,glow:0xd8a860,y:-7,order:-5});
  g.add(yuan1.g);
  const mist=makeMist({n:5,spread:[180,12,66],pos:[0,4.5,-46],scale:58,color:0x332818,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[140,15,56],pos:[0,9,-26],color:0x8a7850,size:4.0,speed:0.028,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0e0a06,seed:26360,rim:0.10,rimC:0xb8906a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:14,n:5,d:4,color:0x0e0a06,seed:26362,sway:0.5,rim:0.08,rimC:0xb8906a});
  fg2.g.position.set(12,-1.7,12.5); g.add(fg2.g);
  addLights(g,{c:0x9a8a68,i:0.24,p:[-30,54,-30]},{c:0x20180f,i:0.48});
  const lampL=new THREE.PointLight(0xd89048,1.0,24);
  lampL.position.set(13.9,6.4,-17.0); g.add(lampL);
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    yuan1.update(t,0);
    shulou.userData.update(t,k); chengnan.userData.update(t,k);
    zheng.update(t,k); sifu.update(t,k);
    lampL.intensity=k*1.0*(0.88+0.12*Math.sin(t*1.2));
    moonL.intensity=k*0.5*(0.92+0.08*Math.sin(t*0.7));
    gap.update(t,k); zhenyun.update(t,k); shaqi.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bBairen(){ // 肆（末境·可点击）· 白刃沙场 —— 相看白刃血纷纷……至今犹忆李将军：
                    // 破晓前最暗的沙场，两列持刀军士结阵相望，白刃低垂；阵云低垂、残旗斜插，
                    // 大漠尽头一骑巡边（至今犹忆李将军的写意远象）。
                    // 点击：白刃寒光自左向右次第亮起，冷光扫过军阵，题字同现，可反复点击
  const ctl={t:0,clicked:false,on:false,reveal:0,sweep:-1,burstDone:false};
  const g=new THREE.Group();
  const base=makeDamoYG({seed1:26363,seed2:26364,dustA:0.06,dustV:2.2,dustC:0x40382c,
    c1:0x0d0905,c2:0x171009}); g.add(base.g);
  /* 白刃军阵（两列相望） */
  const array=makeBairenYG({seed:26381}); array.g.position.set(0,-1.78,1.0);
  array.g.scale.setScalar(1.35); g.add(array.g);
  /* 阵中军旗+残旗：死守之阵 */
  const flag=makeJingqiYG({H:7.8,seed:26305}); flag.position.set(0,-1.8,-22.5); g.add(flag);
  const cange=makeCangeYG({}); cange.position.set(-13.5,-1.78,-19); cange.rotation.y=-0.3; g.add(cange);
  /* 阵云低垂 */
  const zhenyun=makeMist({n:4,spread:[100,6,22],pos:[0,12,-36],scale:26,color:0x120d08,op:0.15});
  g.add(zhenyun.g);
  /* 大漠尽头一骑远影：至今犹忆李将军 */
  const yiji=makeYijiYG({s:1.25}); yiji.position.set(19,-1.78,-40); yiji.rotation.y=-0.5; g.add(yiji);
  /* 点击交互：冷光爆发（爆发前不可见——burst 由 fire() 触发）+军阵上方冷辉（初值=峰值） */
  const burst=makeBurst({n:60,color:0xd8e4ec,pos:[0,2.2,-12]});
  g.add(burst.points);
  const hui=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0e8,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  hui.scale.set(30,12,1); hui.position.set(0,3.0,-12); hui.renderOrder=3; g.add(hui);
  const mist=makeMist({n:5,spread:[180,12,64],pos:[0,4.5,-44],scale:56,color:0x302616,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[140,15,54],pos:[0,8,-24],color:0x8a8878,size:4.0,speed:0.028,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const cao=makeSaicaoYG({seed:26343,n:10,w:40,d:20,z:-4}); g.add(cao);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0c0805,seed:26365,rim:0.10,rimC:0xb8906a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x0c0805,seed:26366,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(12.5,-1.7,11.5); g.add(fg2.g);
  addLights(g,{c:0x8a8494,i:0.22,p:[-40,46,-28]},{c:0x1c1712,i:0.46});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on){
        ctl.reveal=Math.min(1,ctl.reveal+dt/2.4);
        if(ctl.sweep>=0)ctl.sweep+=dt;
        if(ctl.reveal>0.35&&!ctl.burstDone){ ctl.burstDone=true; burst.fire(); }
      }
      array.update(t,k,ctl.sweep);
      hui.material.opacity=k*0.10*ctl.reveal*(0.85+0.15*Math.sin(t*1.6));
      flag.userData.update(t,k,1.1);
      burst.update(t);
      zhenyun.update(t,k); mist.update(t,k); motes.update(t);
      cao.visible=k>0.004;
      base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.12);
        pluck(1,0.0,0.14); pluck(4,0.38,0.10); pluck(2,0.90,0.08); pluck(0,1.55,0.06);
      }
      ctl.sweep=0; ctl.burstDone=false;                       /* 冷光重扫：可反复点击 */
      const fl=$('#flash'); fl.textContent='相看白刃血纷纷 死节从来岂顾勋';
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
  cam:{f:[0,10.5,50],t:[0,7.5,30],lf:[2,10,-22],lt:[3,10.5,-36]},
  sky:()=>SK({fd:0.0046,star:0.10,hor:C(0x40280f),ms:0.34,mph:0.42,mhaze:0.24}) },
{ name:'烟尘汉家',dwell:19,river:0.02,build:bChuchen,
  cam:{f:[-4,5.4,25],t:[2.8,3.6,3],lf:[-2,4.6,-8],lt:[4,4.4,-24]},
  sky:()=>SK({top:C(0x1c140b),hor:C(0x4a3416),bot:C(0x0e0906),fog:C(0x1d140b),fd:0.0058,star:0.02,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.10,
    dirC:C(0xc89050),dirI:0.40,dirP:new THREE.Vector3(44,52,-26),
    ambC:C(0x2e2012),ambI:0.60}) },
{ name:'萧条边庭',dwell:24,river:0.02,build:bWeiju,
  cam:{f:[-3.5,4.8,24],t:[1.0,3.4,-6],lf:[-5,4.4,-12],lt:[2,4.2,-28]},
  sky:()=>SK({top:C(0x180f09),hor:C(0x52321a),bot:C(0x0d0805),fog:C(0x1b110a),fd:0.0056,star:0.04,
    ms:0.75,mph:0.50,mhaze:0.34,moon:new THREE.Vector3(58,16,-168),
    dirC:C(0xc07c48),dirI:0.34,dirP:new THREE.Vector3(52,26,-22),
    ambC:C(0x2a1c10),ambI:0.52}) },
{ name:'两地悬望',dwell:22,river:0.02,build:bXuanwang,
  cam:{f:[0,5.4,22],t:[0,4.0,-3],lf:[0,5.2,-8],lt:[0,5.0,-26]},
  sky:()=>SK({top:C(0x0d0b08),hor:C(0x241a0e),bot:C(0x090706),fog:C(0x171009),fd:0.0058,star:0.42,
    ms:0.85,mph:0.42,mhaze:0.18,moon:new THREE.Vector3(0,64,-195),
    dirC:C(0x9a8a68),dirI:0.22,dirP:new THREE.Vector3(-30,54,-30),
    ambC:C(0x20180f),ambI:0.48}) },
{ name:'白刃沙场',dwell:22,river:0.02,build:bBairen,
  cam:{f:[0,4.6,19.5],t:[0,3.1,-4],lf:[0,4.2,-8],lt:[0,3.4,-24]},
  sky:()=>SK({top:C(0x0b0a08),hor:C(0x1e160e),bot:C(0x080706),fog:C(0x161009),fd:0.0056,star:0.55,
    ms:0.28,mph:0.48,mhaze:0.16,moon:new THREE.Vector3(-72,14,-180),
    dirC:C(0x8a8494),dirI:0.26,dirP:new THREE.Vector3(-40,46,-28),
    ambC:C(0x221c15),ambI:0.54}) },
];
"""

if __name__ == '__main__':
    print('yange-xing.py —— 被 build.py 消费：python build.py yange-xing')
