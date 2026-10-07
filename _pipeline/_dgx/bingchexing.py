# -*- coding: utf-8 -*-
"""bingchexing.py —— 《兵车行》（唐·杜甫，queue no.262，水墨夜思）生成配置
四境长卷（N=4，17 分句，mk split [3,4,3,7]）：
壹 辚辚萧萧（车辚辚马萧萧行人弓箭各在腰+爷娘妻子走相送尘埃不见咸阳桥+牵衣顿足拦道哭哭声直上干云霄——
  标志性瞬间：咸阳桥头车马队列+送别群像+尘埃没桥，兵车过桥、弓箭在腰、人潮拦道），
贰 点行频（道旁过者问行人行人但云点行频+防河营田裹头还戍+边庭流血成海水——问答结构画面：
  道旁过者侧立相问、征夫垂首诉苦，远处征调长队与暗色浪影），
叁 秦兵况复（君不闻汉家山东二百州千村万落生荆杞+健妇把锄犁禾生陇亩无东西+况复秦兵耐苦战被驱不异犬与鸡——
  荒村陇亩：荆杞丛生、健妇荷锄、残垣枯树、被驱队伍远去），
肆 边庭血流（长者虽有问役夫敢申恨+县官急索租+信知生男恶生女犹得嫁比邻+君不见青海头古来白骨无人收+
  新鬼烦冤旧鬼哭天阴雨湿声啾啾——末境点击：青海头暗浪阴云纸钱写意收束；
  点击画面——咸阳桥送别人潮幻影涌动重现，牵衣顿足、哭声干云，沉痛克制勿直白血腥）。
美术立意「咸阳桥头一幅尘土送别长卷」：全卷立在一旁只看不说（道旁过者=杜甫的见证视角）——
壹桥头尘潮（声）→ 贰道旁问答（诉）→ 叁田园荒芜（荒）→ 肆青海鬼哭（冤）；
水墨夜思全套色板：底色 #0d1117、雾 #111823～#131a26 系、文字 #dfe6f0，accent=#93a8c4
（queue 分配强调色，青灰微蓝）只落在 UI/人物边缘光/哭声光柱/纸钱微光/幻影人潮上，全页近零饱和；
战争苦难意象克制写意：送别人潮、尘埃、暗色浪影、纸钱，不画尸骸不直白血腥。
与已有水墨夜思/战乱页第一眼可区分：不做雨前危楼眺望（xianyang-chenglou）、不做雪原戍楼听笛
（saishang-chuidi）、不做关外行军（congjunxing-yumen）、不做暮村差吏夜呼（shihaoli）——
本页是**咸阳桥尘土飞扬的送别长卷**：有桥有驿道有群像，无战斗场面、无残肢白骨直写。
标志性瞬间（境壹·queue moment：车辚辚马萧萧行人弓箭各在腰）：兵车双马开道、征夫弓箭在腰鱼贯过桥，
尘埃一道横抹，半掩咸阳桥。
末境点击（queue interact：点击牵衣顿足拦道哭——送别人潮涌动）：点击——
①咸阳桥送别人潮幻影（发光剪影）自雾中涌动而来，浪形起伏、牵衣顿足（幻影组点击前 visible=false 硬关）；
②尘光微涨、哭声光柱复起；③三叠下行拨弦，如哭声渐远；
④「牵衣顿足拦道哭 哭声直上干云霄」题字同现——送别一幕，正是此后一切白骨的起点。
考点钉子：辚 lín／干 gān 云霄／点行 háng／耶娘=爷娘／走=跑／妻子=妻与子／恶 è／啾 jiū
（小测第 3 题落点）；杜甫即事名篇的新题乐府（第 4 题）；反战与穷兵黩武之害（第 5 题）。
多音字：辚辚→林林 耶娘→爷娘 点行频→点航频 干云霄→甘云霄 还戍边→环戍边
生男恶→生男饿 荆杞→荆起（tts.json sub 表，防误读）。"""
import os

_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='bingchexing', title='兵车行', dyn='唐 · 杜甫', brand_author='杜 甫',
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
        ('rgba(5,8,15', 'rgba(7,10,16', 1),
        ('rgba(4,6,11', 'rgba(6,8,14', 2),
        ('rgba(6,9,16', 'rgba(7,9,15', 1),
        ('rgba(3,5,9', 'rgba(5,7,12', 1),
        ('#0b101c', '#101624', 1),
        ('#6f664f', '#5f6a7e', 1),
        ('#5a5340', '#525c6e', 1),
        ('0x0a1526', '0x121a26', 4),
    ],
    tip='轻点画面 / 按空格 —— 送别人潮涌动，牵衣顿足拦道哭',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看咸阳桥送别人潮幻影涌动重现，牵衣顿足、哭声干云',
    cover_read='兵车行。唐，杜甫。车辚辚，马萧萧，行人弓箭各在腰。耶娘妻子走相送，尘埃不见咸阳桥。牵衣顿足拦道哭，哭声直上干云霄。道旁过者问行人，行人但云点行频。君不见青海头，古来白骨无人收。新鬼烦冤旧鬼哭，天阴雨湿声啾啾！',
    cover_p1='四重意境，随诗句次第展开：车辚辚，马萧萧，行人弓箭各在腰；爷娘妻子走相送，尘埃不见咸阳桥，牵衣顿足拦道哭，哭声直上干云霄。道旁过者问行人，行人但云点行频——或从十五北防河，便至四十西营田，边庭流血成海水，武皇开边意未已。千村万落生荆杞，纵有健妇把锄犁，况复秦兵耐苦战，被驱不异犬与鸡。县官急索租，信知生男恶，反是生女好；君不见青海头，古来白骨无人收，新鬼烦冤旧鬼哭，天阴雨湿声啾啾！',
    cover_p2='边读诗，边在咸阳古道上做一回「道旁过者」：听车声、马声、哭声齐作，问一句「点行频」，看田园荒芜、白骨蔽野——读懂「开边意未已」四字之重，就读懂了杜甫「诗史」二字的分量。',
    end_h2='哭声 · 啾啾', cn_word='肆',
    words_js="['再送一程咸阳古道','初识少陵，尚需共读','渐入诗境，再诵几遍','点行频里，民生多艰','已解反战诗史之沉郁','边庭声咽，诗史千秋']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'辚辚萧萧', jing:'兵车隆隆，战马萧萧，出征的士兵把弓箭挂在腰间；爷娘妻子一路奔跑相送，扬起的尘埃遮没了咸阳桥。送行的人群牵衣顿足、拦在道上放声痛哭，哭声直冲云天。（辚辚 · 萧萧 · 走相送）（标志性瞬间：兵车双马过桥，征夫弓箭在腰，人潮拦道，尘埃没桥）',
  segs:[
   {c:'车辚辚，', p:py('chē lín lín')},
   {c:'马萧萧，', p:py('mǎ xiāo xiāo')},
   {c:'行人弓箭各在腰。', p:py('xíng rén gōng jiàn gè zài yāo')},
   {c:'耶娘妻子走相送，', p:py('yē niáng qī zǐ zǒu xiāng sòng')},
   {c:'尘埃不见咸阳桥。', p:py('chén āi bù jiàn xián yáng qiáo')},
   {c:'牵衣顿足拦道哭，', p:py('qiān yī dùn zú lán dào kū')},
   {c:'哭声直上干云霄。', p:py('kū shēng zhí shàng gān yún xiāo')}],
  read:'车辚辚，马萧萧，行人弓箭各在腰。耶娘妻子走相送，尘埃不见咸阳桥。牵衣顿足拦道哭，哭声直上干云霄。',
  yisi:'兵车辚辚，战马萧萧，出征的士兵一个个弓箭挂在腰间。爹娘、妻子儿女一路奔跑着赶来送行，扬起的尘土遮天蔽日，连咸阳桥都望不见了；他们拉住征人的衣衫、跺着脚、拦在大路上放声痛哭，哭声直冲云霄。——开篇七句不用一个「悲」字，却是一幅声泪俱下的送行长卷：车声、马声、哭声齐作，先声夺人；「走」「牵」「顿」「拦」四个动词把生离写成了死别。诗人只把镜头如实架在咸阳桥头，不着一字议论，惨别之状已刺人眼目——这就是「诗史」的笔法。',
  zhu:[['辚辚','车轮滚动的声音。辚，读 lín——象声词，车行的隆隆之声'],['萧萧','战马嘶鸣声——未见其人，先闻车马之声，以声起笔'],['行人','指出征的士兵——与下文「道旁过者问行人」的「行人」同指征夫，不是过路之人'],['耶娘妻子','耶娘，即爷娘、父母（耶，同「爷」）；妻子，妻和子女——与现代汉语「妻子」不同：这里是两个人，不是一个'],['走相送','跑着赶来相送。走，古义是跑，与今义「步行」不同'],['咸阳桥','即渭桥，横跨渭水，是唐代从长安通往西北的必经之路——送征人远行的去处'],['干云霄','冲上天空。干，读 gān，冲犯、直冲——形容哭声之高之惨']] },
{ name:'点行频', jing:'道旁的过者上前打听，行人只答三个字：点行频。有人十五岁就去北边防河，到四十岁又被调往西边屯田；去时年幼还得里正替他裹头，归来头发白了又被派去戍边——边庭将士的血流入海成海水，皇上开拓边疆的念头却还没有停下。（问答 · 点行频 · 开边未已）',
  segs:[
   {c:'道旁过者问行人，', p:py('dào páng guò zhě wèn xíng rén')},
   {c:'行人但云点行频。', p:py('xíng rén dàn yún diǎn háng pín')},
   {c:'或从十五北防河，', p:py('huò cóng shí wǔ běi fáng hé')},
   {c:'便至四十西营田。', p:py('biàn zhì sì shí xī yíng tián')},
   {c:'去时里正与裹头，', p:py('qù shí lǐ zhèng yǔ guǒ tóu')},
   {c:'归来头白还戍边。', p:py('guī lái tóu bái huán shù biān')},
   {c:'边庭流血成海水，', p:py('biān tíng liú xuè chéng hǎi shuǐ')},
   {c:'武皇开边意未已。', p:py('wǔ huáng kāi biān yì wèi yǐ')}],
  read:'道旁过者问行人，行人但云点行频。或从十五北防河，便至四十西营田。去时里正与裹头，归来头白还戍边。边庭流血成海水，武皇开边意未已。',
  yisi:'道旁过者壮着胆子上前打听，行人只答了一句：「点行频」——按名册点征，太频繁了！于是这位征夫絮絮诉说自己的一生：有人十五岁去北边防河，到四十岁又被调去西边屯田；离家时年岁尚小，连裹头巾都要里正代劳，归来已是满头白发，却又被派去戍守边关。「点行频」三字是全诗的诗眼——个人的悲欢都从这里来。结穴于「边庭流血成海水，武皇开边意未已」：以「汉武」暗指唐皇，把矛头直指穷兵黩武的决策者——在不敢明言的年代里，这是沉痛中见胆识的一笔。',
  zhu:[['点行频','按名册一次又一次强征壮丁。点行，按户籍名册征调；行，读 háng，指名册行伍；频，频繁——三字为全篇之眼'],['但云','只说、只是说——欲言又止，满腹辛酸尽在不言中'],['防河','防守黄河河防，当时朝廷常征兵抵御吐蕃、突厥'],['营田','屯垦戍边——战时作战、闲时种田的军事制度'],['里正','里长，乡里小吏——「去时里正与裹头」，征人年幼，连裹头巾都要人代劳'],['还戍边','还要去戍守边疆。还，读 huán，仍、又'],['武皇','汉武帝——唐人避讳，借汉指唐，实指唐玄宗的开边政策'],['开边','以武力开拓疆土——「意未已」，野心未止，正是万民流血的根源']] },
{ name:'秦兵况复', jing:'你不听说吗？华山以东二百个州，千村万落长满荆棘枸杞；纵然有健壮的妇女拿着锄头犁耙，田里的庄稼也东倒西歪不成行列。何况关中的士兵最能吃苦耐战，被驱赶上战场，跟鸡犬没有什么两样。（山东二百州 · 健妇锄犁 · 犬与鸡）',
  segs:[
   {c:'君不闻汉家山东二百州，', p:py('jūn bù wén hàn jiā shān dōng èr bǎi zhōu')},
   {c:'千村万落生荆杞。', p:py('qiān cūn wàn luò shēng jīng qǐ')},
   {c:'纵有健妇把锄犁，', p:py('zòng yǒu jiàn fù bǎ chú lí')},
   {c:'禾生陇亩无东西。', p:py('hé shēng lǒng mǔ wú dōng xī')},
   {c:'况复秦兵耐苦战，', p:py('kuàng fù qín bīng nài kǔ zhàn')},
   {c:'被驱不异犬与鸡。', p:py('bèi qū bù yì quǎn yǔ jī')}],
  read:'君不闻汉家山东二百州，千村万落生荆杞。纵有健妇把锄犁，禾生陇亩无东西。况复秦兵耐苦战，被驱不异犬与鸡。',
  yisi:'由一个人的血泪推及天下的荒凉：关东二百州，千村万落田园抛荒、荆棘丛生；男人都被抽走了，纵有健壮的妇女扶锄把犁，田里的庄稼也乱不成行、没有收成。末了「况复秦兵耐苦战，被驱不异犬与鸡」——关中兵越能苦战，被驱遣得就越狠，如同鸡犬。这一段不写战场写田畴，不写死亡写荒芜：战争之害，不只在戍卒的白骨，更在千门万户的生计。「君不闻」三字领起，是行人反问过者，也是诗人反问世人——你难道没有听说吗？',
  zhu:[['君不闻','你不听说吗——与下文「君不见」同为乐府常用的呼告语，把读者拉到眼前'],['汉家','汉朝，借指唐朝——与「武皇」同一避讳手法'],['山东','华山以东，泛指关东广大地区——不是今天的山东省'],['荆杞','荆棘和枸杞，泛指野生灌木——良田抛荒之象。杞，读 qǐ'],['健妇','健壮能干的妇女——男丁尽征，唯妇孺耕作'],['陇亩','田地、田垄。陇，通「垄」，读 lǒng——「无东西」指庄稼杂乱不成行列'],['秦兵','关中一带（古秦地）的士兵，素称耐苦战——正因能战，被征调驱遣愈甚'],['犬与鸡','像鸡犬一样被驱赶——「被驱不异犬与鸡」，以白写痛，沉痛至极']] },
{ name:'边庭血流', jing:'长者既有此问，役夫哪敢尽吐怨恨？只说今年冬天，关西的兵还没放还休整，县官又急着催租——租税从哪里出？这才真知道生男是祸、反不如生女好：生女还能嫁给近邻，生男只能埋没荒草。你没看见青海边上，自古以来的白骨无人收殓；新鬼含冤，旧鬼痛哭，天阴雨湿之时，哭声啾啾！（敢申恨 · 生男恶 · 青海头）（末境点击画面：咸阳桥送别人潮幻影涌动重现，牵衣顿足、哭声干云）',
  segs:[
   {c:'长者虽有问，', p:py('zhǎng zhě suī yǒu wèn')},
   {c:'役夫敢申恨？', p:py('yì fū gǎn shēn hèn')},
   {c:'且如今年冬，', p:py('qiě rú jīn nián dōng')},
   {c:'未休关西卒。', p:py('wèi xiū guān xī zú')},
   {c:'县官急索租，', p:py('xiàn guān jí suǒ zū')},
   {c:'租税从何出？', p:py('zū shuì cóng hé chū')},
   {c:'信知生男恶，', p:py('xìn zhī shēng nán è')},
   {c:'反是生女好。', p:py('fǎn shì shēng nǚ hǎo')},
   {c:'生女犹得嫁比邻，', p:py('shēng nǚ yóu dé jià bǐ lín')},
   {c:'生男埋没随百草。', p:py('shēng nán mái mò suí bǎi cǎo')},
   {c:'君不见青海头，', p:py('jūn bù jiàn qīng hǎi tóu')},
   {c:'古来白骨无人收。', p:py('gǔ lái bái gǔ wú rén shōu')},
   {c:'新鬼烦冤旧鬼哭，', p:py('xīn guǐ fán yuān jiù guǐ kū')},
   {c:'天阴雨湿声啾啾！', p:py('tiān yīn yǔ shī shēng jiū jiū')}],
  read:'长者虽有问，役夫敢申恨？且如今年冬，未休关西卒。县官急索租，租税从何出？信知生男恶，反是生女好。生女犹得嫁比邻，生男埋没随百草。君不见青海头，古来白骨无人收。新鬼烦冤旧鬼哭，天阴雨湿声啾啾！',
  yisi:'面对长者的追问，役夫先是「敢申恨」——哪里敢倾诉怨恨！可话锋一转，压不住的苦水还是涌了出来：今年冬天关西的兵尚未放还，官府反倒催租更急，人被抽走、田已抛荒，租税从何而出？于是逼出那两句颠倒人心的反常话：「信知生男恶，反是生女好」——重男轻女的千年常态，被战争生生反转。末四句境界陡然拉开：青海头边，古来白骨无人收埋，新鬼旧鬼在天阴雨湿里啾啾而哭——由眼前一场送别，推到旷古不绝的边庭之冤；全诗就在这声声鬼哭里收束，冷雨阴云，余恨无穷。',
  zhu:[['长者','对年长者的尊称——指道旁过者（即诗人自己）；役夫称问者「长者」，敬中含悲'],['役夫','服役的人，征夫自称'],['敢申恨','岂敢诉说怨恨。敢，岂敢——反问语气，不是「敢于」；怨气愈压愈重'],['关西卒','函谷关以西的士兵——「未休」，至今不得放还'],['县官','官府、朝廷——「急索租」，人被抽走田已荒，租税却催得更急'],['信知','确实知道、这才真的明白——比「始知」更沉痛'],['生男恶','生男是坏事。恶，读 è——与「反是生女好」对举，战乱中是非颠倒之语'],['青海头','青海湖边，唐与吐蕃长期交战之地——白骨蔽野，无人收埋'],['啾啾','象声词，形容鬼哭之声，凄厉细碎。啾，读 jiū']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「车辚辚，马萧萧」的下一句是？', o:['行人弓箭各在腰','耶娘妻子走相送','尘埃不见咸阳桥'], a:0},
 {q:'「牵衣顿足拦道哭」的下一句是？', o:['哭声直上干云霄','道旁过者问行人','行人但云点行频'], a:0},
 {q:'下列加点字的读音与解释，完全正确的一项是？', o:['辚读 lín，车轮声；「哭声直上干云霄」的干读 gān，冲上；「行人但云点行频」的行读 háng，指按名册点征；「耶娘」即爷娘，指父母','辚读 lìn，车轮声；「哭声直上干云霄」的干读 gàn，干练；「行人但云点行频」的行读 xíng，行走','辚读 lín，车轮声；「哭声直上干云霄」的干读 gān，干燥；「耶娘妻子」指母亲与妻子两个人'], a:0},
 {q:'关于《兵车行》的体裁与写法，下列说法正确的是？', o:['它是杜甫「即事名篇，无复依傍」的新题乐府叙事诗——不用汉乐府旧题，就眼前咸阳桥送别之事自创新题、直书时事，被视为新乐府诗体的先声','它是沿用汉乐府《兵车行》旧题的拟乐府，按古题旧例咏汉代征战故事','它是七言律诗，中间两联对仗工整，格律严谨'], a:0},
 {q:'对这首诗主旨的理解，最恰当的一项是？', o:['借咸阳桥头生离死别的送别长卷与征夫的血泪自述，揭露「开边」战争给百姓带来的深重灾难——「边庭流血成海水，武皇开边意未已」，是一首沉郁深广的反战名篇','歌颂出征将士奋勇杀敌、建功立业的豪情壮志，风格雄浑昂扬','讽刺征夫贪生怕死、不肯为国效力，告诫世人当以从军报国为荣'], a:0},
];
"""

SCENES_JS = """/* ================= 兵车行 · 四境场景（水墨夜思·咸阳桥送别长卷：辚辚萧萧、点行频、秦兵况复、边庭血流） =================
   美术立意：咸阳桥头一幅尘土飞扬的送别长卷——全卷立在道旁只看不说（道旁过者=杜甫的见证视角）：
   壹桥头尘潮（声）→ 贰道旁问答（诉）→ 叁田园荒芜（荒）→ 肆青海鬼哭（冤）。
   水墨夜思色板：底色 #0d1117、雾 #111823～#131a26 系，accent=#93a8c4 只落在 UI/人物边缘光/
   哭声光柱/纸钱微光/幻影人潮；战争苦难意象克制写意：人潮、尘埃、暗色浪影、纸钱，不画尸骸。
   与已有页第一眼可区分：不做雨前危楼（xianyang-chenglou）、不做雪原戍楼（saishang-chuidi）、
   不做关外行军（congjunxing-yumen）、不做差吏夜呼（shihaoli）——有桥有驿道有群像，无战斗场面。 */

/* —— 驿道 makeDaoJS(o)：黄土官道（合批 1 mesh：路面微起伏分条+车辙细条+路缘）——
   咸阳古道：壹横向过桥、贰纵向远去、卷首通向桥头 */
function makeDaoJS(o){
  o=o||{};
  const B=new GeoBag();
  const L=o.L===undefined?46:o.L, W=o.W===undefined?6.4:o.W;
  const n=o.segN===undefined?7:o.segN;
  for(let i=0;i<n;i++){
    const x=-L/2+L*(i+0.5)/n;
    const seg=new THREE.BoxGeometry(L/n*1.06,0.24,W*(0.92+0.10*Math.sin(i*2.7+1.3)));
    seg.translate(x,0.10,Math.sin(i*1.9)*0.28);
    B.put(seg,i%2?0x1b2029:0x181d26);
  }
  for(let s=-1;s<=1;s+=2){
    const rut=new THREE.BoxGeometry(L,0.10,0.16);
    rut.translate(0,0.20,s*W*0.26); B.put(rut,0x11151d);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a303a,emissive:0x04060a}),{c:0x93a8c4,i:o.rim===undefined?0.09:o.rim,p:2.0})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 咸阳桥 makeQiaoJS(o)：石拱桥（桥面分段拱起+拱下暗影半盘+两侧望柱栏板+两端石堤，
   合批 1 mesh+拱影 1）——「尘埃不见咸阳桥」：全页的地标，总在尘烟后半隐半现 */
function makeQiaoJS(o){
  o=o||{};
  const B=new GeoBag();
  const W=o.W===undefined?54:o.W, R=o.R===undefined?3.4:o.R, D=o.D===undefined?4.6:o.D;
  const n=o.n===undefined?15:o.n;
  const deckC=0x2a3038, railC=0x333a44;
  for(let i=0;i<n;i++){
    const x0=-W/2+W*i/n, x1=-W/2+W*(i+1)/n, xm=(x0+x1)/2;
    const h0=R*Math.sin(Math.PI*i/n), h1=R*Math.sin(Math.PI*(i+1)/n);
    const len=Math.hypot(x1-x0,h1-h0), ang=Math.atan2(h1-h0,x1-x0);
    const dk=new THREE.BoxGeometry(len+0.1,0.34,D);
    dk.rotateZ(-ang); dk.translate(xm,0.30+(h0+h1)/2,0); B.put(dk,deckC);
    const rb=new THREE.BoxGeometry(len+0.1,0.10,0.14);
    rb.rotateZ(-ang); rb.translate(xm,1.42+(h0+h1)/2,-D/2+0.07); B.put(rb,railC);
    const rb2=rb.clone(); rb2.translate(0,0,D-0.14); B.put(rb2,railC);
    if(i%2===0){
      const p1=new THREE.BoxGeometry(0.18,0.85,0.18);
      p1.translate(x0,0.85+h0,-D/2+0.07); B.put(p1,railC);
      const p2=p1.clone(); p2.translate(0,0,D-0.14); B.put(p2,railC);
    }
  }
  for(let s=-1;s<=1;s+=2){
    const pier=new THREE.BoxGeometry(2.2,1.5,D+0.6);
    pier.translate(s*(W/2-1.4),-0.45,0); B.put(pier,0x222831);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3c4654,emissive:0x05070b}),{c:0x93a8c4,i:o.rim===undefined?0.13:o.rim,p:2.3})));
  const arch=new THREE.Mesh(new THREE.CircleGeometry(R*0.72,18,Math.PI,Math.PI),
    new THREE.MeshBasicMaterial({color:0x05070c,side:THREE.DoubleSide,depthWrite:false}));
  arch.position.set(0,0.16,D/2+0.02); arch.renderOrder=1; g.add(arch);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=(o.seed===undefined?26201:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 低模马 makeMaJS(o)：躯干/四腿（前后微错步）/颈/头/耳/鬃/尾（合批 1 mesh），
   颈粗壮上收约五十七度、头位明显高于背线、头平伸微俯——辚辚萧萧的开道战马
   （壹双马驾辕、卷首官道车马、肆驿马剪影） */
function makeMaJS(o){
  o=o||{};
  const s=o.s===undefined?1:o.s;
  const coat=o.coat===undefined?0x3a332a:o.coat, dk=shadeColor(coat,0.72);
  const B=new GeoBag();
  const bd=new THREE.SphereGeometry(0.60,10,8);
  bd.scale(1.55*s,0.88*s,0.60*s); bd.translate(0,1.22*s,0); B.put(bd,coat);
  const legs=[[0.72,0.30,0.26],[0.66,-0.28,-0.24],[-0.74,0.32,-0.26],[-0.68,-0.30,0.28]];
  legs.forEach(function(p){
    const lg=new THREE.CylinderGeometry(0.075*s,0.05*s,0.78*s,5);
    lg.translate(0,-0.39*s,0);
    lg.rotateZ(p[2]*0.30); lg.rotateX(p[1]*0.4);
    lg.translate(p[0]*s,0.80*s,p[1]*s*0.9);
    B.put(lg,dk);
  });
  B.put(limbGeo([0.70*s,1.42*s,0],[1.48*s,2.62*s,0],0.34*s,0.19*s,7),coat);
  const hd=new THREE.ConeGeometry(0.155*s,0.72*s,6);
  hd.rotateZ(-1.68); hd.translate(1.90*s,2.52*s,0); B.put(hd,dk);
  const mz=new THREE.SphereGeometry(0.10*s,7,5);
  mz.scale(1.2,0.9,0.9); mz.translate(2.24*s,2.34*s,0); B.put(mz,shadeColor(coat,0.6));
  for(let e=0;e<2;e++){
    const ear=new THREE.ConeGeometry(0.05*s,0.20*s,4);
    ear.rotateZ(0.3);
    ear.translate(1.52*s,2.94*s,(e?0.09:-0.09)*s); B.put(ear,dk);
  }
  B.put(limbGeo([0.60*s,1.72*s,0],[1.44*s,2.82*s,0],0.10*s,0.045*s,5),shadeColor(coat,1.35));
  B.put(limbGeo([-0.94*s,1.46*s,0],[-1.28*s,0.70*s,0],0.09*s,0.03*s,5),dk);
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a241c,emissive:0x040302}),{c:0x93a8c4,i:o.rim===undefined?0.18:o.rim,p:2.2}));
  g.add(mesh);
  const ph=(o.seed===undefined?26202:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    mesh.position.y=0.03*s*(1+Math.sin(t*2.1+ph))*kk;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 兵车 makeCheJS(o)：双轮（轮辋+辐条+毂）/车舆/轼栏/单辕/衡木/身后军旗（幡布顶点波动），
   合批 1 mesh+旗 1——「车辚辚」的本体 */
function makeCheJS(o){
  o=o||{};
  const B=new GeoBag();
  const s=o.s===undefined?1:o.s;
  const wd=o.wood===undefined?0x463a2b:o.wood;
  for(let sd=-1;sd<=1;sd+=2){
    const rim=new THREE.TorusGeometry(0.82*s,0.085*s,6,16);
    rim.translate(0,0.82*s,sd*0.62*s); B.put(rim,shadeColor(wd,0.62));
    for(let i=0;i<6;i++){
      const sp=new THREE.BoxGeometry(0.05*s,1.5*s,0.05*s);
      sp.rotateZ(i*Math.PI/6);
      sp.translate(0,0.82*s,sd*0.62*s); B.put(sp,shadeColor(wd,0.8));
    }
    const hub=new THREE.CylinderGeometry(0.10*s,0.10*s,0.30*s,8);
    hub.rotateX(Math.PI/2); hub.translate(0,0.82*s,sd*0.62*s); B.put(hub,shadeColor(wd,1.2));
  }
  const ax=new THREE.CylinderGeometry(0.06*s,0.06*s,1.5*s,6);
  ax.rotateX(Math.PI/2); ax.translate(0,0.82*s,0); B.put(ax,shadeColor(wd,0.7));
  const yu=new THREE.BoxGeometry(1.44*s,0.62*s,1.10*s);
  yu.translate(0,1.42*s,0); B.put(yu,wd);
  for(let i=0;i<4;i++){
    const side=new THREE.BoxGeometry(i<2?1.44*s:0.06*s,0.30*s,i<2?0.06*s:1.10*s);
    side.translate(i===0?0:(i===1?0:(i===2?0.72*s:-0.72*s)),1.80*s,i===0?-0.55*s:(i===1?0.55*s:0));
    B.put(side,shadeColor(wd,1.18));
  }
  const shi=new THREE.BoxGeometry(0.07*s,0.07*s,1.10*s);
  shi.translate(0.70*s,1.86*s,0); B.put(shi,shadeColor(wd,1.3));
  for(let i=0;i<2;i++){
    const leg=new THREE.BoxGeometry(0.07*s,0.62*s,0.07*s);
    leg.translate(-0.52*s+i*1.04*s,1.05*s,0); B.put(leg,shadeColor(wd,0.85));
  }
  B.put(limbGeo([0.70*s,1.44*s,0],[2.75*s,1.10*s,0],0.07*s,0.05*s,6),shadeColor(wd,0.9));
  const heng=new THREE.CylinderGeometry(0.05*s,0.05*s,1.9*s,6);
  heng.rotateX(Math.PI/2); heng.translate(2.75*s,1.24*s,0); B.put(heng,shadeColor(wd,1.05));
  B.put(limbGeo([-0.66*s,1.72*s,0],[-0.66*s,3.55*s,0],0.045*s,0.03*s,5),shadeColor(wd,0.9));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a4034,emissive:0x050403}),{c:0x93a8c4,i:o.rim===undefined?0.12:o.rim,p:2.3})));
  const W=o.flagW===undefined?1.5:o.flagW, H=o.flagH===undefined?1.0:o.flagH;
  const geo=new THREE.PlaneGeometry(W,H,8,3);
  geo.translate(W/2+0.02,0,0);
  const base=geo.attributes.position.array.slice(), cnt=geo.attributes.position.count;
  const cols=new Float32Array(cnt*3);
  const cb=new THREE.Color(0x2b323d), ca=new THREE.Color(0x93a8c4);
  for(let i=0;i<cnt;i++){
    const y=base[i*3+1], t=Math.max(0,((y+H/2)/H-0.62)/0.38);
    const c=cb.clone().lerp(ca,t*0.8);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(cols,3));
  const flag=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,emissive:0x0a0d14}));
  flag.position.set(-0.66*s,3.02*s,0); g.add(flag);
  const fpos=geo.attributes.position, ph=(o.seed===undefined?26203:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<fpos.count;i++){
      const bx=base[i*3], by=base[i*3+1], f=bx/W;
      fpos.array[i*3+2]=Math.sin(bx*2.0-t*3.1+ph)*0.20*f*f*kk;
      fpos.array[i*3+1]=by-Math.abs(Math.sin(bx*1.5-t*2.3+ph))*0.06*f*f*kk;
    }
    fpos.needsUpdate=true;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 弓箭在腰：弓弧+弦线+箭囊由 bcZhengfu 的 bow 选项挂于征夫腰侧——「行人弓箭各在腰」 */

/* —— 征夫 bcZhengfu(scale,pose,bow,rim)：泥灰布袍+幞头，可选腰挂弓箭——「行人」全诗同一造型 */
function bcZhengfu(scale,pose,bow,rim){
  const fig=makeFigure({pose:pose||'独立',robe:0x39404a,belt:0x5a5340,skin:0xd3b294,collar:0x76808e,
    hair:0x14161c,hat:'幞头',rimC:0x93a8c4,rim:rim===undefined?0.30:rim,noProp:true,scale:scale===undefined?1.35:scale});
  if(bow){
    const B=new GeoBag();
    const bowG=new THREE.TorusGeometry(0.34,0.024,5,12,Math.PI*0.9);
    bowG.rotateZ(-0.35); bowG.translate(-0.44,1.92,0.16); B.put(bowG,0x241c12);
    const str=new THREE.CylinderGeometry(0.011,0.011,0.60,4);
    str.rotateZ(0.5); str.translate(-0.44,1.92,0.16); B.put(str,0x8a8272);
    const qt=new THREE.CylinderGeometry(0.030,0.024,0.80,5);
    qt.rotateZ(0.42); qt.translate(0.42,1.70,0.18); B.put(qt,0x2c2418);
    const bw=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      specular:0x2a241a,emissive:0x030202}));
    fig.add(bw);
  }
  return fig;
}

/* —— 道旁过者（见证者·杜甫视角）bcPoet(scale,pose)：青灰袍、幞头，全卷同一张脸——只看只问，不评一句 */
function bcPoet(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2e3742,belt:0x71809a,skin:0xd3b294,collar:0x9aa6b8,
    hair:0x12161e,hat:'幞头',rimC:0x93a8c4,rim:0.36,noProp:true,scale:scale===undefined?1.5:scale});
}

/* —— 尘埃 makeChenJS(o)：贴地尘带（add:false 灰褐双层 makeGlow）+大团尘雾（makeMist）+
   尘头缓移——「尘埃不见咸阳桥」：全页标志性的「土雾」 */
function makeChenJS(o){
  o=o||{};
  const g=new THREE.Group();
  const box=o.box===undefined?[46,7.5,11]:o.box, pos=o.pos===undefined?[0,3.4,-11]:o.pos;
  const d1=makeGlow({n:o.n1===undefined?26:o.n1,box:box,pos:pos,color:o.c1===undefined?0x54503f:o.c1,
    size:o.s1===undefined?7.5:o.s1,speed:0.05,rise:0.10,add:false,maxA:0.15});
  d1.points.renderOrder=3; g.add(d1.points);
  const d2=makeGlow({n:o.n2===undefined?16:o.n2,box:[box[0]*0.7,box[1]*1.4,box[2]*0.8],
    pos:[pos[0],pos[1]+1.6,pos[2]],color:o.c2===undefined?0x63604f:o.c2,
    size:(o.s1===undefined?7.5:o.s1)*0.85,speed:0.04,rise:0.05,add:false,maxA:0.10});
  d2.points.renderOrder=3; g.add(d2.points);
  const mist=makeMist({n:o.mistN===undefined?4:o.mistN,spread:[box[0]*1.1,8,box[2]*1.6],pos:pos,
    scale:o.ms===undefined?26:o.ms,color:0x4a4638,op:0.10});
  g.add(mist.g);
  const ph=(o.seed===undefined?26204:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    d1.update(t); d2.update(t);
    g.position.x=Math.sin(t*0.09+ph)*2.2;
    mist.update(t,kk);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 哭声直上 makeKuShengJS(o)：细窄光柱缓升（makeGlow rise:1）+顶口光点脉冲——
   「哭声直上干云霄」：声音的写意，唯一一根向上的光 */
function makeKuShengJS(o){
  o=o||{};
  const g=new THREE.Group();
  const pos=o.pos===undefined?[12.5,4.5,-5.5]:o.pos;
  const col=makeGlow({n:o.n===undefined?12:o.n,box:[2.4,13,2.4],pos:pos,color:0x9fb2c8,
    size:2.6,speed:0.02,rise:1,add:true,maxA:0.11});
  col.points.renderOrder=3; g.add(col.points);
  const tip=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x93a8c4,
    transparent:true,opacity:0.16,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  tip.scale.set(3.4,3.4,1); tip.position.set(pos[0],pos[1]+7.5,pos[2]); tip.renderOrder=4; g.add(tip);
  const ph=(o.seed===undefined?26205:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    col.update(t);
    tip.material.opacity=kk*0.16*Math.pow(Math.max(0,Math.sin(t*0.55+ph)),6);
    tip.scale.setScalar(2.2+2.6*Math.pow(Math.max(0,Math.sin(t*0.55+ph)),6));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 枯柳 makeKuLiuJS(o)：曲干+下垂枝条（limbGeo 多段下坠）——古道旁的送别树 */
function makeKuLiuJS(o){
  o=o||{};
  const B=new GeoBag();
  const h=o.h===undefined?5.4:o.h;
  const B0=o.B0===undefined?0x1a1d24:o.B0;
  B.put(limbGeo([0,0,0],[0.12,h*0.55,0],0.30,0.16,7),B0);
  B.put(limbGeo([0.12,h*0.55,0],[0.02,h,0.04],0.15,0.06,6),B0);
  const R=seedRnd(o.seed===undefined?26206:o.seed);
  for(let i=0;i<6;i++){
    const a=R()*6.283, rr=0.5+R()*0.9, x0=0.08+Math.sin(a)*0.1;
    const y0=h*(0.72+R()*0.24);
    B.put(limbGeo([x0,y0,Math.cos(a)*0.1],[x0+Math.sin(a)*rr,y0-0.5-R()*0.8,Math.cos(a)*rr],
      0.05,0.02,5),shadeColor(B0,1.18));
    B.put(limbGeo([x0+Math.sin(a)*rr,y0-1.1,Math.cos(a)*rr],[x0+Math.sin(a)*(rr+0.5),y0-2.0-R()*0.9,Math.cos(a)*(rr+0.4)],
      0.02,0.012,4),shadeColor(B0,1.3));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a303a,emissive:0x04050a}),{c:0x93a8c4,i:o.rim===undefined?0.08:o.rim,p:2.0})));
  const ph=(o.seed===undefined?26206:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.008*Math.sin(t*0.5+ph)*kk;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 荆杞 makeJingQiJS(o)：荒田灌木（多枝乱叉 limbGeo 合批 1 mesh）——「千村万落生荆杞」 */
function makeJingQiJS(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?26207:o.seed);
  const s=o.s===undefined?1:o.s;
  for(let i=0;i<7;i++){
    const a=R()*6.283, rr=(0.3+R()*0.75)*s, hh=(0.7+R()*1.3)*s;
    B.put(limbGeo([0,0,0],[Math.sin(a)*rr,hh,Math.cos(a)*rr],0.055*s,0.02*s,5),0x232830);
    if(R()<0.7){
      B.put(limbGeo([Math.sin(a)*rr*0.6,hh*0.5,Math.cos(a)*rr*0.6],
        [Math.sin(a)*rr+ (R()-0.5)*0.5,hh+R()*0.5,Math.cos(a)*rr+(R()-0.5)*0.5],0.03*s,0.012*s,4),0x1d2129);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a303a,emissive:0x04050a}),{c:0x93a8c4,i:o.rim===undefined?0.08:o.rim,p:2.0})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 陇亩 makeLongJS(o)：平行田垄（长条微起伏）+稀疏蔫禾短锥（合批 1 mesh）——
   「禾生陇亩无东西」：垄还在，庄稼不成行 */
function makeLongJS(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?26208:o.seed);
  const L=o.L===undefined?30:o.L, rows=o.rows===undefined?12:o.rows, dz=o.dz===undefined?1.55:o.dz;
  for(let i=0;i<rows;i++){
    const z=-rows*dz/2+dz*i;
    const rg=new THREE.BoxGeometry(L,0.24,0.72);
    rg.translate((R()-0.5)*1.2,0.10,z+(R()-0.5)*0.3);
    rg.rotateY((R()-0.5)*0.05);
    B.put(rg,i%2?0x171c22:0x141920);
    const tufts=2+Math.floor(R()*3);
    for(let j=0;j<tufts;j++){
      const tf=new THREE.ConeGeometry(0.09,0.5+R()*0.5,4);
      tf.translate(-L/2+R()*L,0.42,z+(R()-0.5)*0.5);
      tf.rotateZ((R()-0.5)*0.9);
      B.put(tf,0x272e2c);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a303a,emissive:0x04050a}),{c:0x93a8c4,i:o.rim===undefined?0.07:o.rim,p:2.0})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 锄 addHoeJS(fig)：柄+锄板，挂于健妇手侧——「纵有健妇把锄犁」 */
function addHoeJS(fig){
  const B=new GeoBag();
  B.put(limbGeo([0.10,1.05,0.34],[1.42,2.36,0.50],0.065,0.048,5),0x463a28);
  const bl=new THREE.BoxGeometry(0.52,0.30,0.055);
  bl.rotateZ(0.9); bl.translate(1.42,2.50,0.50); B.put(bl,0x868e9a);
  const hoe=B.mesh(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x5a626e,emissive:0x05070c}));
  fig.add(hoe);
  return fig;
}

/* —— 纸钱 makeZhiQianJS(o)：白纸片 InstancedMesh（1 draw call），阴风里旋落复扬——
   「古来白骨无人收」的写意祭奠：无火无坟，只有湿风中的纸钱 */
function makeZhiQianJS(o){
  o=o||{};
  const n=o.n===undefined?16:o.n;
  const area=o.area===undefined?{c:[0,4.2,-30],r:[26,4.5,10]}:o.area;
  const op0=o.op===undefined?0.34:o.op;
  const g=new THREE.Group(), R=seedRnd(o.seed===undefined?26209:o.seed);
  const geo=new THREE.PlaneGeometry(0.30,0.42);
  const mesh=new THREE.InstancedMesh(geo,
    new THREE.MeshBasicMaterial({color:0xd9dfe8,transparent:true,opacity:op0,
      depthWrite:false,side:THREE.DoubleSide}),n);
  mesh.frustumCulled=false; mesh.renderOrder=4;
  const items=[];
  for(let i=0;i<n;i++){
    items.push({x:area.c[0]+(R()-0.5)*area.r[0], y:area.c[1]+(R()-0.5)*area.r[1],
      z:area.c[2]+(R()-0.5)*area.r[2], ph:R()*6.283, sp:0.5+R()*0.8, sc:0.8+R()*0.7});
  }
  const dm=new THREE.Object3D(); g.add(mesh);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<n;i++){
      const it=items[i];
      const yy=it.y+Math.sin(t*it.sp+it.ph)*1.1+Math.sin(t*0.21+it.ph*2)*1.4;
      dm.position.set(it.x+Math.sin(t*0.13+it.ph)*2.2, yy, it.z+Math.cos(t*0.11+it.ph)*1.4);
      dm.rotation.set(t*it.sp+it.ph, it.ph+t*0.7, Math.sin(t*it.sp*1.3+it.ph)*0.8);
      dm.scale.setScalar(it.sc);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mesh.material.opacity=kk*op0*(0.72+0.28*Math.sin(t*0.4));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 声啾啾 makeJiuJiuJS(o)：水面三处冷光脉冲（错相呼吸）——「新鬼烦冤旧鬼哭，天阴雨湿声啾啾」：
   哭声只给光点，不给形骸 */
function makeJiuJiuJS(o){
  o=o||{};
  const g=new THREE.Group(), phs=[0,2.1,4.2];
  const ps=o.pos===undefined?[[ -9,2.6,-30],[3,3.1,-33],[12,2.4,-28]]:o.pos;
  const tips=[];
  ps.forEach(function(p,i){
    const sp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9fb0c6,
      transparent:true,opacity:0.13,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    sp.scale.set(2.6,2.6,1); sp.position.set(p[0],p[1],p[2]); sp.renderOrder=4; g.add(sp);
    tips.push({sp:sp,ph:phs[i]});
  });
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    tips.forEach(function(it){
      const pulse=Math.pow(Math.max(0,Math.sin(t*0.85+it.ph)),12);
      it.sp.material.opacity=kk*0.13*pulse;
      it.sp.scale.setScalar(1.4+2.8*pulse);
    });
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 标志性交互：送别人潮幻影 makeRenChaoJS(o)——点击后自雾中涌动的咸阳桥送别剪影：
   发光人影 InstancedMesh（浪形涌动）+四名牵衣顿足的幻影（臂前伸、顿足弹跳）+尘光晕。
   组 visible=false 硬关——点击前无幻影；update(t,k,rv) 的 rv 0→1 淡现 */
function makeRenChaoJS(o){
  o=o||{};
  const g=new THREE.Group();
  const n=o.n===undefined?18:o.n;
  const mesh=new THREE.InstancedMesh(crowdGeo(),
    new THREE.MeshBasicMaterial({color:0xa8b8cc,transparent:true,opacity:0.13,
      depthWrite:false,blending:THREE.AdditiveBlending,fog:false}),n);
  mesh.frustumCulled=false; mesh.renderOrder=4;
  const R=seedRnd(o.seed===undefined?26231:o.seed), items=[];
  for(let i=0;i<n;i++){
    items.push({x:-15+32*R(), z:-6-15*R(), s:0.72+R()*0.5, ph:R()*6.283, sp:0.5+R()*0.7});
  }
  const dm=new THREE.Object3D(); g.add(mesh);
  /* 四名牵衣顿足幻影：臂前伸（指月势）+高频顿足弹跳——「牵衣顿足」四个动词里取两个入画 */
  const hands=[];
  for(let i=0;i<4;i++){
    const B=new GeoBag();
    const robe=new THREE.LatheGeometry([new THREE.Vector2(0.02,0),new THREE.Vector2(0.42,0.9),
      new THREE.Vector2(0.34,2.1),new THREE.Vector2(0.24,2.9)],10);
    robe.scale(1,1,0.82); B.put(robe,0xa8b8cc);
    const head=new THREE.SphereGeometry(0.30,10,8);
    head.translate(0,3.35,0); B.put(head,0xa8b8cc);
    B.put(limbGeo([0.32,2.62,0],[1.10,2.30,0.55],0.14,0.09,5),0xa8b8cc);
    B.put(limbGeo([-0.30,2.60,0],[-0.44,1.75,0.10],0.13,0.09,5),0xa8b8cc);
    const fg=B.mesh(new THREE.MeshBasicMaterial({color:0xb8c6d8,transparent:true,opacity:0.10,
      depthWrite:false,blending:THREE.AdditiveBlending,fog:false}));
    fg.renderOrder=4;
    fg.position.set(-9+i*6.4,0,-8-(i%2)*5);
    g.add(fg); hands.push({m:fg,ph:i*1.57});
  }
  const dust=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x93a8c4,
    transparent:true,opacity:0.07,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  dust.scale.set(46,15,1); dust.position.set(0,5,-14); dust.renderOrder=3; g.add(dust);
  g.visible=false;
  g.userData.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const e=r*r*(3-2*r);
    for(let i=0;i<n;i++){
      const it=items[i];
      const surge=Math.sin(t*it.sp+it.ph);
      dm.position.set(it.x+Math.sin(t*0.2+it.ph)*1.2, Math.abs(Math.sin(t*2.2+it.ph))*0.14,
        it.z+surge*1.6*e);
      dm.rotation.set(0,Math.PI+0.15*Math.sin(t*0.4+it.ph),0);
      dm.scale.setScalar(it.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    mesh.material.opacity=kk*e*0.13*(0.85+0.15*Math.sin(t*1.1));
    hands.forEach(function(hd){
      hd.m.position.y=Math.abs(Math.sin(t*3.4+hd.ph))*0.24*e;
      hd.m.material.opacity=kk*e*0.10*(0.8+0.2*Math.sin(t*1.7+hd.ph));
      hd.m.visible=kk*e>0.004;
    });
    dust.material.opacity=kk*e*0.07*(0.8+0.2*Math.sin(t*0.9));
    g.visible=kk*e>0.004;
  };
  return {g:g,update:g.userData.update};
}

function bCover(){ // 卷首 · 咸阳古道暮色：官道尽头石桥半隐尘中，人车如蚁，过者立于道旁
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a0d13,c2:0x141a24,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const yuan=makeRange({r:250,h:14,layers:2,peaks:5,seed:26221,color:0x0b0f16,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x93a8c4,y:-8,order:-6});
  yuan.g.position.set(0,0,-170); g.add(yuan.g);
  const shui=makeWater({size:240,seg:56,amp:0.07,freq:0.15,speed:0.22,flow:[0.14,0.02],spec:0.8,
    deep:0x070a10,shallow:0x0d1219,skyc:0x111722,moonDir:[-0.2,0.2,-0.95]});
  shui.mesh.material.uniforms.uMoonColor.value=C(0x8fa2b8);
  shui.mesh.position.set(-4,-0.45,-62); g.add(shui.mesh);
  const qiao=makeQiaoJS({seed:26201}); qiao.g.position.set(-2,0,-46); g.add(qiao.g);
  const dao=makeDaoJS({L:58,W:6.4,seed:26211}); dao.position.set(0,0,-8);
  dao.rotation.y=Math.PI/2; g.add(dao);
  /* 车马人潮沿官道向桥而行（面 -z），尘横桥半掩 */
  const ma1=makeMaJS({s:0.92,seed:26202}); ma1.g.position.set(0.25,0,-29.3);
  ma1.g.rotation.y=Math.PI/2; g.add(ma1.g);
  const ma2=makeMaJS({s:0.88,coat:0x332c24,seed:26225}); ma2.g.position.set(1.55,0,-28.0);
  ma2.g.rotation.y=Math.PI/2; g.add(ma2.g);
  const che=makeCheJS({s:0.95,seed:26203}); che.g.position.set(0.9,0,-23.4);
  che.g.rotation.y=Math.PI/2+0.05; g.add(che.g);
  const ren=makeCrowd({n:12,rect:[-8,-37,16,16],color:0x1a202a,rimC:0x93a8c4,rim:0.12,
    sMin:0.7,sMax:1.0,seed:26212});
  g.add(ren.mesh);
  const chen=makeChenJS({box:[42,9,13],pos:[-2,4.2,-40],mistN:4,ms:32,seed:26204}); g.add(chen.g);
  const chen2=makeChenJS({box:[26,6,9],pos:[2,3,-20],mistN:3,ms:24,seed:26226}); g.add(chen2.g);
  const liu1=makeKuLiuJS({h:6,seed:26206}); liu1.g.position.set(-13,0,-1); g.add(liu1.g);
  const liu2=makeKuLiuJS({h:5,seed:26207}); liu2.g.position.set(12.5,0,-6);
  liu2.g.rotation.y=2.0; g.add(liu2.g);
  const poet=bcPoet(1.42,'独立'); poet.position.set(11,0,3.5);
  poet.rotation.y=Math.PI+0.5; g.add(poet);
  const mist=makeMist({n:5,spread:[140,10,58],pos:[0,3.4,-16],scale:46,color:0x2a3140,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[96,14,46],pos:[0,8,0],color:0x8fa0b8,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x05070c,seed:26222,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(-13,-1.6,20); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x05070c,seed:26223,sway:0.6,rim:0.08,rimC:0x93a8c4});
  fg2.g.position.set(13.5,-1.8,19); g.add(fg2.g);
  addLights(g,{c:0x8fa0b8,i:0.28,p:[-40,52,-40]},{c:0x1e2632,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0); shui.update(t);
    qiao.update(t,k); chen.update(t,k); chen2.update(t,k);
    che.update(t,k); ma1.update(t,k); ma2.update(t,k);
    ren.update(t); liu1.update(t,k); liu2.update(t,k);
    poet.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bLinli(){ // 壹（标志性瞬间）· 辚辚萧萧 —— 车辚辚，马萧萧，行人弓箭各在腰：
                   // 兵车双马开道、征夫弓箭在腰鱼贯西去；爷娘妻子走相送，牵衣顿足拦道哭，
                   // 尘埃一道横抹，咸阳桥半隐土雾之中；哭声一柱直上
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a0d13,c2:0x151b26,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeRange({r:250,h:12,layers:2,peaks:4,seed:26224,color:0x0b0f16,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x93a8c4,y:-8,order:-6});
  yuan.g.position.set(40,0,-160); g.add(yuan.g);
  const shui=makeWater({size:260,seg:60,amp:0.07,freq:0.15,speed:0.22,flow:[0.16,0.02],spec:0.8,
    deep:0x070a10,shallow:0x0d1219,skyc:0x121826,moonDir:[-0.2,0.22,-0.95]});
  shui.mesh.material.uniforms.uMoonColor.value=C(0x8fa2b8);
  shui.mesh.position.set(-6,-0.45,-58); g.add(shui.mesh);
  const qiao=makeQiaoJS({seed:26201}); qiao.g.position.set(-4,0,-46); g.add(qiao.g);
  const dao=makeDaoJS({L:52,W:6.4,seed:26211}); dao.position.set(0,0,-9.5); g.add(dao);
  /* 兵车双马：向西而行（面 -x），双马前后错半步，长卷式侧面剪影最易读 */
  const ma1=makeMaJS({s:1.05,seed:26202}); ma1.g.position.set(-8.2,0,-10.4);
  ma1.g.rotation.y=Math.PI; g.add(ma1.g);
  const ma2=makeMaJS({s:1.0,coat:0x423a2e,seed:26225}); ma2.g.position.set(-7.0,0,-8.9);
  ma2.g.rotation.y=Math.PI; g.add(ma2.g);
  const che=makeCheJS({s:1.05,seed:26203}); che.g.position.set(-2.5,0,-9.6);
  che.g.rotation.y=Math.PI; g.add(che.g);
  /* 征夫一行：弓箭各在腰，鱼贯相随（道中景） */
  const zf1=bcZhengfu(1.35,'独立',true,0.34); zf1.position.set(0.8,0,-9.0);
  zf1.rotation.y=Math.PI+0.10; g.add(zf1);
  const zf2=bcZhengfu(1.30,'独立',true,0.34); zf2.position.set(3.2,0,-10.2);
  zf2.rotation.y=Math.PI-0.06; g.add(zf2);
  const zf3=bcZhengfu(1.38,'独立',true,0.34); zf3.position.set(5.6,0,-9.2);
  zf3.rotation.y=Math.PI+0.14; g.add(zf3);
  const dui=makeCrowd({n:8,rect:[9,-16,13,4],color:0x1c222c,rimC:0x93a8c4,rim:0.12,
    sMin:0.75,sMax:1.0,seed:26213});
  g.add(dui.mesh);
  /* 爷娘妻子走相送：牵衣（妻伸手拉衣）、拦道（爷张臂）、顿足（子随行小跑），人潮于后 */
  const ye=makeFigure({pose:'指月',robe:0x33302a,belt:0x5a5340,skin:0xd3b294,collar:0x8a8272,
    hair:0x14161c,hat:'幞头',beard:true,rimC:0x93a8c4,rim:0.28,noProp:true,scale:1.36});
  ye.position.set(10.5,0,-6.5); ye.rotation.y=-2.15; g.add(ye);
  const niang=makeFigure({pose:'独立',robe:0x3a3540,belt:0x6a6252,skin:0xd3b294,collar:0x9a92a0,
    hair:0x14161c,hat:'发髻',rimC:0x93a8c4,rim:0.28,noProp:true,scale:1.26});
  niang.position.set(12.8,0,-5.2); niang.rotation.y=-2.4; g.add(niang);
  const qi=makeFigure({pose:'指月',robe:0x39414e,belt:0x6a6252,skin:0xd3b294,collar:0x8a92a0,
    hair:0x14161c,hat:'发髻',rimC:0x93a8c4,rim:0.32,noProp:true,scale:1.18});
  qi.position.set(8.8,0,-7.8); qi.rotation.y=-2.0; g.add(qi);
  const zi=makeFigure({pose:'独立',robe:0x3c3830,belt:0x5a5340,skin:0xd3b294,collar:0x8a8272,
    hair:0x14161c,hat:'无',rimC:0x93a8c4,rim:0.24,noProp:true,scale:0.92});
  zi.position.set(11.5,0,-7.6); zi.rotation.y=-2.6; g.add(zi);
  const chao=makeCrowd({n:10,rect:[9,-17,11,9],color:0x1d232e,rimC:0x93a8c4,rim:0.13,
    sMin:0.7,sMax:1.05,seed:26214});
  g.add(chao.mesh);
  const chen=makeChenJS({box:[40,7.5,10],pos:[-16,3.6,-12],mistN:4,ms:28,seed:26204}); g.add(chen.g);
  const chen2=makeChenJS({box:[30,9,10],pos:[-6,4.5,-42],mistN:3,ms:30,seed:26226}); g.add(chen2.g);
  const ku=makeKuShengJS({pos:[11.5,4.5,-6.5],seed:26205}); g.add(ku.g);
  const mist=makeMist({n:5,spread:[140,10,56],pos:[0,3.6,-14],scale:46,color:0x2b3240,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[96,13,44],pos:[0,8,2],color:0x8fa0b8,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05070c,seed:26227,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(-12,-1.6,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x05070c,seed:26228,sway:0.55,rim:0.08,rimC:0x93a8c4});
  fg2.g.position.set(12.5,-1.8,16); g.add(fg2.g);
  addLights(g,{c:0x98a4b6,i:0.28,p:[28,46,-30]},{c:0x232a36,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0); shui.update(t);
    qiao.update(t,k);
    che.update(t,k); ma1.update(t,k); ma2.update(t,k);
    chen.update(t,k); chen2.update(t,k); ku.update(t,k);
    zf1.update(t,k); zf2.update(t,k); zf3.update(t,k); dui.update(t);
    ye.update(t,k); niang.update(t,k); qi.update(t,k); zi.update(t,k); chao.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bDianxing(){ // 贰 · 点行频 —— 道旁过者问行人，行人但云点行频：
                      // 问答结构画面：过者侧立拱问，征夫垂首按弓而诉；身后驿道远去、
                      // 征调长队北行，远处暗浪一带（边庭流血成海水，武皇开边意未已）
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0a0d13,c2:0x141a23,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeRange({r:250,h:13,layers:2,peaks:5,seed:26229,color:0x0b0f16,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x93a8c4,y:-8,order:-6});
  yuan.g.position.set(-20,0,-165); g.add(yuan.g);
  /* 边庭暗浪：远处一带暗色浪影（流血成海水的克制写意——只给暗红微光，不给形） */
  const bian=makeWater({size:280,seg:60,amp:0.11,freq:0.13,speed:0.24,flow:[0.2,0.03],spec:0.7,
    deep:0x080a0e,shallow:0x151013,skyc:0x161a24,moonDir:[0.15,0.18,-0.95]});
  bian.mesh.material.uniforms.uMoonColor.value=C(0x6a4a3c);
  bian.mesh.position.set(-30,-0.5,-80); g.add(bian.mesh);
  const lang=makeRange({arc:0.85,a0:2.42,r:150,h:6,layers:2,peaks:5,seed:26230,color:0x0d0a0e,
    atmo:0x1f2a3d,fogK:0.60,glowK:0.05,glow:0x5a4038,y:-7,order:-5});
  lang.g.position.set(-24,0,-66); g.add(lang.g);
  const dao=makeDaoJS({L:44,W:6.0,seed:26211}); dao.position.set(3.4,0,-16);
  dao.rotation.y=Math.PI/2; g.add(dao);
  /* 问答二人组：过者拱手相问（指月势转为问），征夫垂首按弓而立 */
  const gz=bcPoet(1.42,'指月'); gz.position.set(-1.6,0,-5.2);
  gz.rotation.y=1.35; g.add(gz);
  const xr=bcZhengfu(1.36,'独立',true); xr.position.set(2.6,0,-5.9);
  xr.rotation.y=-1.75; xr.rotation.x=0.07; g.add(xr);
  /* 身后继续北行的征调队伍 */
  const zf4=bcZhengfu(1.28,'独立',true); zf4.position.set(6.8,0,-13.5);
  zf4.rotation.y=Math.PI*0.92; g.add(zf4);
  const zf5=bcZhengfu(1.24,'独立',true); zf5.position.set(9.6,0,-17.5);
  zf5.rotation.y=Math.PI*0.86; g.add(zf5);
  const dui=makeCrowd({n:14,rect:[-14,-34,26,12],color:0x1a202a,rimC:0x93a8c4,rim:0.11,
    sMin:0.62,sMax:0.95,seed:26215});
  g.add(dui.mesh);
  /* 西营田：远处田垄一带 */
  const tian=makeLongJS({L:22,rows:7,seed:26208}); tian.position.set(22,0,-24);
  tian.rotation.y=-0.35; g.add(tian);
  const liu=makeKuLiuJS({h:5.6,seed:26232}); liu.g.position.set(-11.5,0,-1.5);
  liu.g.rotation.y=0.9; g.add(liu.g);
  const chen=makeChenJS({box:[26,6,9],pos:[10,3,-24],mistN:3,ms:24,seed:26233}); g.add(chen.g);
  const mist=makeMist({n:5,spread:[136,10,56],pos:[0,3.4,-16],scale:44,color:0x2a3140,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[92,13,44],pos:[0,8,2],color:0x8fa0b8,size:3.2,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.3,w:10,d:5,color:0x05070c,seed:26234,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(11.5,-1.5,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.1,w:9,d:4,color:0x05070c,seed:26235,rim:0.08,rimC:0x93a8c4});
  fg2.g.position.set(-11.5,-1.4,16); g.add(fg2.g);
  addLights(g,{c:0x94908a,i:0.26,p:[-34,44,-32]},{c:0x242833,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0); bian.update(t); lang.update(t,0);
    gz.update(t,k); xr.update(t,k); zf4.update(t,k); zf5.update(t,k); dui.update(t);
    liu.update(t,k); chen.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bQinbing(){ // 叁 · 秦兵况复 —— 千村万落生荆杞，纵有健妇把锄犁，禾生陇亩无东西：
                     // 荒村陇亩：残垣枯树、荆杞丛生，健妇荷锄而立，远处秦兵被驱西去如鸡犬
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0a0d12,c2:0x131820,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,18);
  const yuan=makeRange({r:260,h:16,layers:2,peaks:6,seed:26236,color:0x0b0f15,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x93a8c4,y:-9,order:-6});
  yuan.g.position.set(0,0,-160); g.add(yuan.g);
  const tian=makeLongJS({L:34,rows:13,dz:1.6,seed:26208}); tian.position.set(0,0,-14); g.add(tian);
  /* 健妇荷锄（锄口朝向镜头一侧，读得出器形） */
  const jf=makeFigure({pose:'独立',robe:0x3c3a34,belt:0x5f5a4a,skin:0xd3b294,collar:0x8a8578,
    hair:0x14161c,hat:'发髻',rimC:0x93a8c4,rim:0.34,noProp:true,scale:1.34});
  addHoeJS(jf);
  jf.position.set(-4.6,0,-9.6); jf.rotation.y=0.9; g.add(jf);
  /* 荆杞丛生 */
  const jq1=makeJingQiJS({s:1.4,seed:26207}); jq1.position.set(-15,0,-17); g.add(jq1);
  const jq2=makeJingQiJS({s:1.1,seed:26237}); jq2.position.set(12,0,-9.5); g.add(jq2);
  const jq3=makeJingQiJS({s:1.6,seed:26238}); jq3.position.set(17.5,0,-19); g.add(jq3);
  const jq4=makeJingQiJS({s:0.9,seed:26239}); jq4.position.set(-8.5,0,-22.5); g.add(jq4);
  const jq5=makeJingQiJS({s:1.2,seed:26240}); jq5.position.set(7,0,-26); g.add(jq5);
  /* 空村残垣：断墙两段+枯树 */
  const wall1=new THREE.Mesh(new THREE.BoxGeometry(5.2,1.7,0.5),
    new THREE.MeshPhongMaterial({color:0x20242c,shininess:4,specular:0x2a303a,emissive:0x04050a}));
  wall1.position.set(-19.5,0.85,-20); wall1.rotation.y=0.2; g.add(wall1);
  const wall2=new THREE.Mesh(new THREE.BoxGeometry(3.4,1.1,0.5),
    new THREE.MeshPhongMaterial({color:0x1c2028,shininess:4,specular:0x2a303a,emissive:0x04050a}));
  wall2.position.set(-15.8,0.55,-22.6); wall2.rotation.y=-0.5; g.add(wall2);
  const tree=makeKuLiuJS({h:6.4,seed:26241}); tree.g.position.set(-21,0,-16.5); g.add(tree.g);
  /* 被驱西去的秦兵：低首疾行，如驱鸡犬 */
  const qb1=bcZhengfu(1.26,'独立',false,0.38); qb1.position.set(12.6,0,-19.6);
  qb1.rotation.y=Math.PI*0.55; qb1.rotation.x=0.13; g.add(qb1);
  const qb2=bcZhengfu(1.22,'独立',false,0.38); qb2.position.set(15.4,0,-22.4);
  qb2.rotation.y=Math.PI*0.5; qb2.rotation.x=0.15; g.add(qb2);
  const qu=makeCrowd({n:11,rect:[8,-34,20,9],color:0x1a1f28,rimC:0x93a8c4,rim:0.12,
    sMin:0.6,sMax:0.9,seed:26216});
  g.add(qu.mesh);
  const chen=makeChenJS({box:[24,5.5,8],pos:[19,2.8,-29],mistN:3,ms:22,seed:26242}); g.add(chen.g);
  const mist=makeMist({n:5,spread:[140,10,58],pos:[0,3.4,-16],scale:46,color:0x272e38,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[98,13,46],pos:[0,8,0],color:0x8fa0b8,size:3.2,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'树枝',n:5,w:9,d:4,color:0x05070c,seed:26243,sway:0.4,rim:0.08,rimC:0x93a8c4});
  fg1.g.position.set(-11,-1.3,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x05070c,seed:26244,rim:0.08,rimC:0x93a8c4});
  fg2.g.position.set(11,-1.4,18.5); g.add(fg2.g);
  addLights(g,{c:0x9aa4b2,i:0.26,p:[24,46,-30]},{c:0x252a33,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    jf.update(t,k); qb1.update(t,k); qb2.update(t,k); qu.update(t);
    tree.update(t,k); chen.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bBianting(){ // 肆（末境·可点击）· 边庭血流 —— 君不见青海头，古来白骨无人收：
                      // 青海头暗浪阴云，湿风纸钱旋落复扬，水面声啾啾冷光错现；
                      // 点击：咸阳桥送别人潮幻影涌动重现——牵衣顿足、哭声干云（沉痛克制）
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x090c11,c2:0x121722,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,12);
  const yuan=makeRange({r:250,h:11,layers:2,peaks:4,seed:26245,color:0x0a0e14,atmo:0x1f2a3d,
    fogK:0.62,glowK:0.05,glow:0x93a8c4,y:-8,order:-6});
  yuan.g.position.set(0,0,-165); g.add(yuan.g);
  /* 青海头：大面暗浪 */
  const hai=makeWater({size:400,seg:72,amp:0.13,freq:0.12,speed:0.20,flow:[0.16,0.04],spec:0.8,
    deep:0x05070c,shallow:0x0c1119,skyc:0x10161f,moonDir:[-0.3,0.22,-0.9]});
  hai.mesh.material.uniforms.uMoonColor.value=C(0x8fa2b8);
  hai.mesh.position.set(0,-0.5,-52); g.add(hai.mesh);
  const an=makeRange({arc:1.3,a0:-0.66,r:130,h:8,layers:2,peaks:5,seed:26246,color:0x0a0d12,
    atmo:0x1f2a3d,fogK:0.60,glowK:0.05,glow:0x8fa0b8,y:-6,order:-5});
  an.g.position.set(0,0,-72); g.add(an.g);
  /* 阴云两层 */
  const yun=makeMist({n:5,spread:[170,12,80],pos:[0,15,-46],scale:56,color:0x0d1219,op:0.15});
  g.add(yun.g);
  const yun2=makeMist({n:4,spread:[150,10,70],pos:[0,8,-40],scale:48,color:0x111722,op:0.12});
  g.add(yun2.g);
  /* 湿风纸钱 */
  const zq=makeZhiQianJS({area:{c:[0,4.0,-27],r:[28,4.0,9]},op:0.42,seed:26209}); g.add(zq.g);
  /* 声啾啾 */
  const jj=makeJiuJiuJS({pos:[[-10,3.0,-27],[2,3.4,-30],[11,2.8,-25]],seed:26210}); g.add(jj.g);
  /* 催租驿道一角：远堤驿马（县官急索租） */
  const di=new THREE.Mesh(new THREE.BoxGeometry(30,0.9,2.4),
    new THREE.MeshPhongMaterial({color:0x1a2029,shininess:4,specular:0x2a303a,emissive:0x04050a}));
  di.position.set(20,0.4,-40); di.rotation.y=0.22; g.add(di);
  const yi=makeMaJS({s:0.72,coat:0x1a1e26,seed:26249}); yi.g.position.set(22,1.0,-39.4);
  yi.g.rotation.y=0.9; g.add(yi.g);
  /* 标志性交互：送别人潮幻影（点击前 visible=false 硬关） */
  const rc=makeRenChaoJS({seed:26231}); g.add(rc.g);
  const mist=makeMist({n:5,spread:[140,11,58],pos:[0,3.6,-16],scale:46,color:0x222933,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[96,14,46],pos:[0,8,-2],color:0x8fa0b8,size:3.2,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.5,w:11,d:5,color:0x04060a,seed:26250,rim:0.09,rimC:0x93a8c4});
  fg1.g.position.set(-12.5,-1.6,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:14,n:5,d:4,color:0x04060a,seed:26251,sway:0.7,rim:0.08,rimC:0x93a8c4});
  fg2.g.position.set(12,-1.8,16.5); g.add(fg2.g);
  addLights(g,{c:0x8fa0b8,i:0.24,p:[-40,50,-40]},{c:0x1e2530,i:0.50});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/6.5);
      const e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      hai.update(t);
      yuan.update(t,0); an.update(t,0);
      zq.update(t,k); jj.update(t,k);
      yi.update(t,k);
      rc.update(t,k,ctl.reveal>0?e:0);
      mist.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); yun.update(t,k); yun2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.10);
        pluck(5,0.05,0.10); pluck(3,0.90,0.09); pluck(0,1.85,0.07);
        const fl=$('#flash'); fl.textContent='牵衣顿足拦道哭 哭声直上干云霄';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0a0e16),hor:C(0x1a212d),bot:C(0x05080d),fog:C(0x111823),fd:0.0054,star:0.14,
  moon:new THREE.Vector3(-46,52,-180),ms:0.8,mph:0.45,mhaze:0.22,dirC:C(0x8fa0b8),dirI:0.28,
  dirP:new THREE.Vector3(-40,50,-36),ambC:C(0x1e2632),ambI:0.52},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,5.4,27],t:[-1.5,3.8,-22],lf:[2,5.0,-8],lt:[-3,4.4,-32]},
  sky:()=>SK({fd:0.0050,star:0.16,ms:0.7,mph:0.42,mhaze:0.24}) },
{ name:'辚辚萧萧',dwell:26,river:0.02,build:bLinli,
  cam:{f:[3.5,4.4,19],t:[-3,2.6,-9],lf:[1.5,4.2,4],lt:[-8,3.4,-22]},
  sky:()=>SK({top:C(0x12161f),hor:C(0x272e3a),fd:0.0056,star:0.07,
    moon:new THREE.Vector3(42,44,-170),ms:0.55,mph:0.5,mhaze:0.26,
    dirC:C(0x98a4b6),dirI:0.28,dirP:new THREE.Vector3(28,46,-30),
    ambC:C(0x232a36),ambI:0.52}) },
{ name:'点行频',dwell:24,river:0.02,build:bDianxing,
  cam:{f:[4.8,3.5,8.8],t:[-2.4,2.5,-7.5],lf:[1.5,3.2,-3],lt:[-6,3.2,-20]},
  sky:()=>SK({top:C(0x12161e),hor:C(0x232933),fd:0.0058,star:0.04,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.20,
    dirC:C(0x94908a),dirI:0.26,dirP:new THREE.Vector3(-34,44,-32),
    ambC:C(0x242833),ambI:0.50}) },
{ name:'秦兵况复',dwell:22,river:0.02,build:bQinbing,
  cam:{f:[0,6.0,17],t:[0,2.6,-9],lf:[-2.5,5.4,-6],lt:[3,3.6,-24]},
  sky:()=>SK({top:C(0x11151c),hor:C(0x20252e),fd:0.0060,star:0.02,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.18,
    dirC:C(0x9aa4b2),dirI:0.26,dirP:new THREE.Vector3(24,46,-30),
    ambC:C(0x252a33),ambI:0.50}) },
{ name:'边庭血流',dwell:28,river:0.02,build:bBianting,
  cam:{f:[0,6.6,20],t:[0,3.4,-8],lf:[2,6.0,-8],lt:[-4,5.6,-28]},
  sky:()=>SK({top:C(0x090c12),hor:C(0x161c26),fd:0.0062,star:0.03,
    moon:new THREE.Vector3(-52,40,-175),ms:0.4,mph:0.55,mhaze:0.28,
    dirC:C(0x8fa0b8),dirI:0.24,dirP:new THREE.Vector3(-40,50,-40),
    ambC:C(0x1e2530),ambI:0.50}) },
];
"""

if __name__ == '__main__':
    print('bingchexing.py —— 被 build.py 消费：python build.py bingchexing')
