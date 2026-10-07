# -*- coding: utf-8 -*-
"""mulanci.py —— 《木兰辞》（北朝民歌，queue no.261，大漠金戈）生成配置
六境长卷（N=6，23 分句）：
壹 机杼叹息（唧唧机杼替爷征——当户织机+军帖+忧思：夜闺织机，木兰停梭长叹，案上军帖微光），
贰 市鞍赴边（东西南北市买鞍马+旦辞黄河暮宿黑山：晨市鞍马摊+木兰牵马+远处黄河水光一带+黑山燕山），
叁 关山铁衣（万里赴戎机朔气金柝寒光铁衣将军百战：大关山重岭+烽燧孤光+山径铁衣行军长龙），
肆 辞赏还乡（归来见天子不用尚书郎愿驰千里足：明堂柱列+幡旗+箱笼赐物+阶前木兰+千里马候归），
伍 家人相迎（爷娘出郭相扶将+阿姊理红妆+小弟磨刀霍霍向猪羊+开阁坐床脱袍著裳+当窗理云鬓对镜帖花黄：
  家园院落群像——敞廊妆台木兰理妆、爷娘相扶、阿姊迎门、小弟磨刀火花、羊圈炊烟），
陆 火伴惊忙（当窗理云鬓对镜帖花黄之后出门看火伴+雄兔雌兔——末境点击，标志性瞬间：
  双兔傍地走。点击「安能辨我是雄雌」：双兔幻影傍地疾走+木兰军装/红妆两态若隐若现交叠明灭）。
美术立意「当户一门，双兔一辨」：全卷只跟着木兰一人走——闺夜织机（女）→ 市鞍赴边（换装）→
关山铁衣（壮士）→ 辞赏还乡（功成不受）→ 家人相迎（归妆）→ 火伴惊忙（雌雄莫辨）。
贯穿母题一扇「当户」的木门（壹当户织/陆出门看火伴）与一匹马（贰市鞍马/肆驰千里足）。
大漠金戈全套色板：底色 #120d08、雾 #180f08～#1c130a 系、文字 #f0e2cc，accent=#c4823a
（沙金赭，queue 分配强调色）只落在 UI/人物边缘光/军帖光晕/烽火/铁衣寒光/双兔幻影/门内灯火，
禁艳金。与已有边塞页第一眼可区分：不做雪原戍楼听笛（saishang-chuidi）、不做拂晓誓师整甲
（wuyi）、不做密林夜射（saixiaqu-linan）、不做行军出关（congjunxing-yuben）——本页是
**木兰一人的六境人生长卷**：闺夜-市集-关山-明堂-家园-村道，有家院有群像有双兔，无战阵残垣。
标志性瞬间（境陆前半·queue moment：雄兔脚扑朔雌兔眼迷离双兔傍地走）：村道前景一褐一灰两只
低模兔交错奔走（傍地走动画），木兰红妆当门而立、火伴惊忙于前。
末境点击（queue interact：点击安能辨我是雄雌——双兔幻影）：点击——
①发光双兔幻影沿大弧傍地疾走、交错明灭；②木兰军装/红妆两态同位交叠呼吸互换（opacity 错相）；
③「雄兔脚扑朔 雌兔眼迷离 安能辨我是雄雌」题字同现+三音拨弦。
考点钉子：机杼 zhù／金柝 tuò／著 zhuó／帖 tiē 花黄／霍霍 huò／可汗 kè hán／燕山 yān／
胡骑 jì／溅溅 jiān／同行 háng／裳 cháng（小测第 3 题落点）；乐府双璧·北朝民歌（第 4 题）；
木兰形象与双兔之喻（第 5 题）。
多音字：可汗→克酣 机杼→机住 军帖→军铁 帖花黄→贴花黄 金柝→金拓 燕山→烟山 胡骑→胡寄
溅溅→尖尖 著我→浊我 旧时裳→旧时常 同行十二年→同航十二年 愿为市鞍马→愿慰市鞍马
（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=6, slug='mulanci', title='木兰辞', dyn='北朝 · 乐府民歌', brand_author='北 朝 民 歌',
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
        ('0x0a1526', '0x1a1209', 4),
    ],
    tip='轻点画面 / 按空格 —— 双兔傍地走，安能辨我是雄雌',
    hint='← → 键或空格逐境游览 · 末境可点击画面：双兔幻影傍地疾走，木兰军装红妆两态若隐若现',
    cover_read='木兰辞。北朝民歌。唧唧复唧唧，木兰当户织。万里赴戎机，关山度若飞。将军百战死，壮士十年归。当窗理云鬓，对镜帖花黄。双兔傍地走，安能辨我是雄雌。',
    cover_p1='六重意境，随诗句次第展开：唧唧复唧唧，木兰当户织，昨夜军帖卷卷有爷名，愿为市鞍马从此替爷征；东西南北市买齐鞍辔，旦辞爷娘暮宿黄河，燕山胡骑鸣啾啾；万里赴戎机，朔气金柝寒光照铁衣，将军百战壮士十年归来见天子——木兰不用尚书郎，愿驰千里足送儿还故乡；爷娘出郭相扶将，小弟磨刀霍霍向猪羊，当窗理云鬓对镜帖花黄；出门看火伴——雄兔脚扑朔，雌兔眼迷离，双兔傍地走，安能辨我是雄雌。',
    cover_p2='边读诗，边跟着木兰走完这一趟人生长卷：闺夜的织机、市上的鞍马、关山的铁衣、明堂的辞赏、家园的灯火、村道的双兔——读懂「双兔傍地走」的妙喻与「不用尚书郎」的干脆，就读懂了这位巾帼英雄的全部心事。',
    end_h2='双兔 · 雄雌', cn_word='陆',
    words_js="['再随木兰赴一趟戎机','初识木兰，尚需共读','渐入诗境，再诵几遍','铁衣渐寒，乡关渐近','已解双兔傍地之喻','巾帼千古，雌雄谁辨']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'机杼叹息', jing:'叹息声一声接着一声，木兰对着门织布。听不见织机的声音，只听见姑娘的叹息。问她想什么，问她忆什么——昨夜见了征兵的军帖，可汗大规模点兵，征兵名册卷卷都有父亲的名字；阿爷没有成年的儿子，木兰没有兄长，愿意为此去买鞍马，从此替父出征。（机杼 · 军帖 · 替爷征）',
  segs:[
   {c:'唧唧复唧唧，', p:py('jī jī fù jī jī')},
   {c:'木兰当户织。', p:py('mù lán dāng hù zhī')},
   {c:'不闻机杼声，', p:py('bù wén jī zhù shēng')},
   {c:'惟闻女叹息。', p:py('wéi wén nǚ tàn xī')},
   {c:'问女何所思，', p:py('wèn nǚ hé suǒ sī')},
   {c:'问女何所忆。', p:py('wèn nǚ hé suǒ yì')},
   {c:'女亦无所思，', p:py('nǚ yì wú suǒ sī')},
   {c:'女亦无所忆。', p:py('nǚ yì wú suǒ yì')},
   {c:'昨夜见军帖，', p:py('zuó yè jiàn jūn tiě')},
   {c:'可汗大点兵，', p:py('kè hán dà diǎn bīng')},
   {c:'军书十二卷，', p:py('jūn shū shí èr juàn')},
   {c:'卷卷有爷名。', p:py('juàn juàn yǒu yé míng')},
   {c:'阿爷无大儿，', p:py('ā yé wú dà ér')},
   {c:'木兰无长兄，', p:py('mù lán wú zhǎng xiōng')},
   {c:'愿为市鞍马，', p:py('yuàn wèi shì ān mǎ')},
   {c:'从此替爷征。', p:py('cóng cǐ tì yé zhēng')}],
  read:'唧唧复唧唧，木兰当户织。不闻机杼声，惟闻女叹息。问女何所思，问女何所忆。女亦无所思，女亦无所忆。昨夜见军帖，可汗大点兵，军书十二卷，卷卷有爷名。阿爷无大儿，木兰无长兄，愿为市鞍马，从此替爷征。',
  yisi:'叹息声一声连着一声，木兰对着家门织布。织机忽然停了——听不见机杼声，只听见姑娘的叹息。问她想什么，问她忆什么，她说自己也没想什么、没忆什么；可昨夜见过的那纸军帖还摊在案上：可汗大规模点兵，征兵名册卷卷都有父亲的名字。阿爷没有长大的儿子，木兰没有兄长——于是她说：愿意为此去市上买来鞍马，从此替父亲出征。——开篇由「织」入「叹」，由「叹」引出心事：两问两答，军帖才露出半角，一个敢于担当的女儿心事已定。「愿为市鞍马」五字平平道出，把后来十二年的出生入死，轻轻接在了自己肩上。',
  zhu:[['唧唧','叹息声——一说织机声；与下文「不闻机杼声，惟闻女叹息」合看，以叹息声为长'],['当户织','对着门织布。当，对着'],['机杼','织布的梭子。杼，织布梭子，读 zhù——「不闻机杼声」即听不见织机声'],['军帖','征兵的文书。帖，读 tiě'],['可汗','古代西北地区少数民族对君主的称呼，读 kè hán'],['十二卷','极言军书之多；「十二」与下文「策勋十二转」「同行十二年」皆表多数，非确数'],['愿为市鞍马','愿意为此（替父出征）去买鞍马。为，读 wèi，为了；市，买——名词作动词']] },
{ name:'市鞍赴边', jing:'到东市买骏马，西市买鞍鞯，南市买辔头，北市买长鞭。清晨辞别爷娘出发，傍晚宿在黄河边——听不见爷娘唤女儿的声音了，只听见黄河流水鸣溅溅；清晨辞别黄河上路，傍晚到达黑山头——只听见燕山胡人的战马鸣啾啾。（市鞍马 · 旦辞暮宿 · 黄河黑山）',
  segs:[
   {c:'东市买骏马，', p:py('dōng shì mǎi jùn mǎ')},
   {c:'西市买鞍鞯，', p:py('xī shì mǎi ān jiān')},
   {c:'南市买辔头，', p:py('nán shì mǎi pèi tóu')},
   {c:'北市买长鞭。', p:py('běi shì mǎi cháng biān')},
   {c:'旦辞爷娘去，', p:py('dàn cí yé niáng qù')},
   {c:'暮宿黄河边，', p:py('mù sù huáng hé biān')},
   {c:'不闻爷娘唤女声，', p:py('bù wén yé niáng huàn nǚ shēng')},
   {c:'但闻黄河流水鸣溅溅。', p:py('dàn wén huáng hé liú shuǐ míng jiān jiān')},
   {c:'旦辞黄河去，', p:py('dàn cí huáng hé qù')},
   {c:'暮至黑山头，', p:py('mù zhì hēi shān tóu')},
   {c:'不闻爷娘唤女声，', p:py('bù wén yé niáng huàn nǚ shēng')},
   {c:'但闻燕山胡骑鸣啾啾。', p:py('dàn wén yān shān hú jì míng jiū jiū')}],
  read:'东市买骏马，西市买鞍鞯，南市买辔头，北市买长鞭。旦辞爷娘去，暮宿黄河边，不闻爷娘唤女声，但闻黄河流水鸣溅溅。旦辞黄河去，暮至黑山头，不闻爷娘唤女声，但闻燕山胡骑鸣啾啾。',
  yisi:'骏马、鞍鞯、辔头、长鞭——东、西、南、北四市一件一件备齐。行装既然办妥，出发便写得如流水：早晨辞别爷娘上路，晚上已宿在黄河边，听不见爷娘呼唤女儿的声音了，只听见黄河流水溅溅；第二天早晨再辞黄河，晚上已到黑山头，耳边换成了燕山胡骑的啾啾马鸣。——四个「买」字排开，是女儿家备装的郑重；两组「旦辞」「暮宿」对奔而下，是替父从军的急切。离家愈远，爷娘唤女声便愈被水声马鸣替代——不著一个「思」字，思亲之情尽在水声马声里。',
  zhu:[['鞍鞯','马鞍下的垫子。鞯，读 jiān'],['辔头','驾驭牲口用的嚼子和缰绳。辔，读 pèi'],['旦','早晨——与「暮」对举，极言行程之速、离家之远'],['溅溅','水流声，读 jiān jiān'],['黑山','与下文「燕山」均为当时北方山名，代指边关战场'],['燕山胡骑','燕山一带胡人的战马。燕，读 yān；骑，读 jì，战马'],['啾啾','马鸣声']] },
{ name:'关山铁衣', jing:'远行万里奔赴战场，像飞一样翻越关隘山岭。北方的寒气传送着打更的声音，清冷的月光映照着将士的铁甲战衣。将军身经百战九死一生，壮士征战十年才得归来。（赴戎机 · 朔气金柝 · 铁衣寒光）',
  segs:[
   {c:'万里赴戎机，', p:py('wàn lǐ fù róng jī')},
   {c:'关山度若飞。', p:py('guān shān dù ruò fēi')},
   {c:'朔气传金柝，', p:py('shuò qì chuán jīn tuò')},
   {c:'寒光照铁衣。', p:py('hán guāng zhào tiě yī')},
   {c:'将军百战死，', p:py('jiāng jūn bǎi zhàn sǐ')},
   {c:'壮士十年归。', p:py('zhuàng shì shí nián guī')}],
  read:'万里赴戎机，关山度若飞。朔气传金柝，寒光照铁衣。将军百战死，壮士十年归。',
  yisi:'万里赴戎机，关山度若飞——行军之速，一日千里。北方的寒气里传送着打更的梆子声，清冷的月光照着将士的铁甲：夜不解甲，朔风柝声，是十年征戍的日常。将军百战死，壮士十年归——生死对举，十年一瞬，把最惨烈的岁月压缩成最简省的十个字：不写厮杀，只写幸存者的归来，战争的全部重量都压在「度若飞」与「十年归」的巨大落差里。这是全诗唯一正面写战场的六句，惜墨如金，却字字带霜。',
  zhu:[['赴戎机','奔赴战场。戎机，军机、战场'],['关山度若飞','像飞一样越过一道道关塞山岭。度，越过'],['朔气','北方来的寒气。朔，北方'],['金柝','古时军中夜间报更用的器具。柝，打更用的梆子，读 tuò'],['铁衣','铠甲战衣——「寒光照铁衣」写夜巡宿卫的清苦'],['百战死／十年归','互文见义：将军与壮士身经百战，有的战死沙场，有的十年后归来——非谓将军尽死、壮士独归']] },
{ name:'辞赏还乡', jing:'归来朝见天子，天子坐在殿堂上。（木兰）被记功很多次，赏赐很多的财物。天子问木兰想要什么，木兰不愿做尚书郎；希望骑上千里快马，送我回到故乡。（见天子 · 坐明堂 · 不用尚书郎）',
  segs:[
   {c:'归来见天子，', p:py('guī lái jiàn tiān zǐ')},
   {c:'天子坐明堂。', p:py('tiān zǐ zuò míng táng')},
   {c:'策勋十二转，', p:py('cè xūn shí èr zhuǎn')},
   {c:'赏赐百千强。', p:py('shǎng cì bǎi qiān qiáng')},
   {c:'可汗问所欲，', p:py('kè hán wèn suǒ yù')},
   {c:'木兰不用尚书郎，', p:py('mù lán bù yòng shàng shū láng')},
   {c:'愿驰千里足，', p:py('yuàn chí qiān lǐ zú')},
   {c:'送儿还故乡。', p:py('sòng ér huán gù xiāng')}],
  read:'归来见天子，天子坐明堂。策勋十二转，赏赐百千强。可汗问所欲，木兰不用尚书郎，愿驰千里足，送儿还故乡。',
  yisi:'凯旋朝见，天子坐堂，记功封赏——策勋升至十二转，赏赐百千万还有余。天子问木兰想要什么，她的回答出人意料：不愿做尚书郎，只愿骑上一匹千里快马，送我回故乡。——封赏愈重，愈见辞谢之贵；「木兰不用尚书郎」说得干脆利落，功劳簿上的十二转抵不过故乡一扇门。这个跪过明堂的奇女子，把功名还给了朝堂，把自己还给了爷娘。',
  zhu:[['明堂','古代帝王理政、举行大典的殿堂'],['策勋十二转','记功很多次。策勋，记功；转，勋级每升一级叫一转，十二转为最高——极言功大'],['赏赐百千强','赏赐很多的财物。强，有余'],['不用','不愿做'],['尚书郎','尚书省的官，泛指朝中高官'],['千里足','日行千里的好马——愿驰千里足，即希望骑上千里马（一作「愿借明驼千里足」）'],['儿','木兰自称——军中天子面前自称「儿」，见其率真本色']] },
{ name:'家人相迎', jing:'爷娘听说女儿回来，互相搀扶着出外城迎接；阿姊听说妹妹回来，对着门梳妆打扮；小弟听说姐姐回来，霍霍地磨刀要杀猪宰羊。打开我东阁的门，坐上我西阁的床，脱下我打仗时的战袍，穿上我以前的衣裳。对着窗户梳理云一样的鬓发，照着镜子在额上贴好花黄。（出郭相扶将 · 磨刀霍霍 · 理妆帖黄）',
  segs:[
   {c:'爷娘闻女来，', p:py('yé niáng wén nǚ lái')},
   {c:'出郭相扶将。', p:py('chū guō xiāng fú jiāng')},
   {c:'阿姊闻妹来，', p:py('ā zǐ wén mèi lái')},
   {c:'当户理红妆。', p:py('dāng hù lǐ hóng zhuāng')},
   {c:'小弟闻姊来，', p:py('xiǎo dì wén zǐ lái')},
   {c:'磨刀霍霍向猪羊。', p:py('mó dāo huò huò xiàng zhū yáng')},
   {c:'开我东阁门，', p:py('kāi wǒ dōng gé mén')},
   {c:'坐我西阁床，', p:py('zuò wǒ xī gé chuáng')},
   {c:'脱我战时袍，', p:py('tuō wǒ zhàn shí páo')},
   {c:'著我旧时裳。', p:py('zhuó wǒ jiù shí cháng')},
   {c:'当窗理云鬓，', p:py('dāng chuāng lǐ yún bìn')},
   {c:'对镜帖花黄。', p:py('duì jìng tiē huā huáng')}],
  read:'爷娘闻女来，出郭相扶将。阿姊闻妹来，当户理红妆。小弟闻姊来，磨刀霍霍向猪羊。开我东阁门，坐我西阁床，脱我战时袍，著我旧时裳。当窗理云鬓，对镜帖花黄。',
  yisi:'爷娘听说了，互相搀扶着出外城迎接；阿姊听说妹妹回来，赶紧对户梳妆；小弟听说姐姐回来，磨刀霍霍要杀猪宰羊——三位家人闻讯而动的三个特写，写尽一家的欢喜。回家第一件事，是开东阁门、坐西阁床、脱战时袍、著旧时裳：四个连续动作，是十二年来第一次做回自己。当窗理云鬓，对镜帖花黄——女儿家的妆扮一样不少地回来了。铁衣换红妆，故园灯火下，木兰终于是木兰。',
  zhu:[['扶将','搀扶、扶持。将，读 jiāng'],['阿姊','姐姐。姊，读 zǐ'],['红妆','指女子的艳丽装束'],['霍霍','磨刀的声音，读 huò huò——磨刀的急切里是小弟的欢喜'],['阁','木兰家的闺阁，东阁西阁泛指闺房'],['著','穿，读 zhuó'],['裳','古代女子的下裙，读 cháng'],['云鬓','像云那样柔美的鬓发'],['帖花黄','帖，同「贴」，读 tiē；花黄，古代女子的面部装饰——把金黄纸剪成花样贴在额上，或在额上涂一点黄颜色']] },
{ name:'火伴惊忙', jing:'走出家门看同伍的伙伴，伙伴们都很惊讶——同行十二年，竟不知道木兰是女郎。雄兔的脚喜欢乱扑腾，雌兔的眼睛常眯着；两只兔子贴着地面并排跑，怎能分辨哪只是雄兔、哪只是雌兔？（火伴惊忙 · 雄兔雌兔 · 双兔傍地走）（末境点击画面：双兔幻影傍地疾走，木兰军装红妆两态若隐若现）',
  segs:[
   {c:'出门看火伴，', p:py('chū mén kàn huǒ bàn')},
   {c:'火伴皆惊忙，', p:py('huǒ bàn jiē jīng máng')},
   {c:'同行十二年，', p:py('tóng háng shí èr nián')},
   {c:'不知木兰是女郎。', p:py('bù zhī mù lán shì nǚ láng')},
   {c:'雄兔脚扑朔，', p:py('xióng tù jiǎo pū shuò')},
   {c:'雌兔眼迷离。', p:py('cí tù yǎn mí lí')},
   {c:'双兔傍地走，', p:py('shuāng tù bàng dì zǒu')},
   {c:'安能辨我是雄雌？', p:py('ān néng biàn wǒ shì xióng cí')}],
  read:'出门看火伴，火伴皆惊忙，同行十二年，不知木兰是女郎。雄兔脚扑朔，雌兔眼迷离。双兔傍地走，安能辨我是雄雌？',
  yisi:'出门看火伴，伙伴们都惊呆了：同行十二年，竟不知木兰是女郎！——十二年出生入死无人识破，一身红妆便教众人惊忙，这一「惊」是对木兰最好的注脚。于是有了那个千古妙喻：雄兔脚扑朔，雌兔眼迷离；双兔傍地走，安能辨我是雄雌？兔子静时可辨雌雄，并排奔跑起来就难分彼此——正如木兰，闺中是女儿，阵前是壮士。全诗在这跳跃的双兔与一问中收束：不答之答，是全诗最响亮的一笔。',
  zhu:[['火伴','同伍的士兵。「火」同「伙」，一作「伙伴」——古代兵制十人为一火，同火者称火伴'],['惊忙','惊讶慌忙——十二年并肩而不觉，一妆之后惊认女郎'],['扑朔','动弹、扑腾——雄兔脚好动'],['迷离','眯着眼——雌兔眼好眯'],['傍地走','贴近地面并排跑。傍，靠近、临近'],['安能','怎能、哪能——双兔难辨雄雌，正是对木兰男女莫辨的绝妙比喻']] }];
const CN = ['壹','贰','叁','肆','伍','陆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「万里赴戎机」的下一句是？', o:['关山度若飞','朔气传金柝','寒光照铁衣'], a:0},
 {q:'「将军百战死」的下一句是？', o:['壮士十年归','同行十二年，不知木兰是女郎','策勋十二转'], a:0},
 {q:'下列加点字的读音，完全正确的一项是？', o:['机杼读 zhù，金柝读 tuò，「著我旧时裳」的著读 zhuó，「对镜帖花黄」的帖读 tiē','机杼读 zhū，金柝读 tuò，「著我旧时裳」的著读 zhù，「对镜帖花黄」的帖读 tiè','机杼读 zhù，金柝读 tuò，「著我旧时裳」的著读 zhuó，「对镜帖花黄」的帖读 tiè'], a:0},
 {q:'关于《木兰辞》，下列说法正确的是？', o:['它是北朝乐府民歌，与《孔雀东南飞》合称「乐府双璧」；「可汗」是古代西北民族对君主的称呼，「策勋十二转」极言其功勋之高','它是南朝宫体诗，与《孔雀东南飞》合称「乐府双璧」；「可汗」是汉族皇帝的庙号','它是唐代文人拟作，与《孔雀东南飞》并称「哀感顽艳」；「军帖」即皇帝登基的诏书'], a:0},
 {q:'结尾「雄兔脚扑朔，雌兔眼迷离。双兔傍地走，安能辨我是雄雌」这一比喻的作用，理解最恰当的一项是？', o:['以双兔傍地难辨雄雌，喻木兰女扮男装、建功沙场而性别不为人辨——赞美她勤劳勇敢、不慕功名、巾帼不让须眉','说明兔子雌雄本来难以分辨，木兰借此打岔，把话题从封赏岔开','感叹从军十二年虚度了青春年华，双兔的比喻写岁月如梭、物是人非'], a:0},
];
"""

SCENES_JS = """/* ================= 木兰辞 · 六境场景（大漠金戈·木兰人生长卷：机杼叹息、市鞍赴边、关山铁衣、辞赏还乡、家人相迎、火伴惊忙） =================
   美术立意：当户一门，双兔一辨——全卷只跟着木兰一人走（女→军→功→归→妆→辨）。
   大漠金戈色板：底色 #120d08、雾 #180f08～#1c130a 系，accent=#c4823a 只落在人物边缘光/
   军帖光晕/烽火/铁衣寒光/双兔幻影/门内灯火/UI，禁艳金。
   与已有边塞页第一眼可区分：不做雪原戍楼听笛（saishang-chuidi）、不做拂晓誓师整甲（wuyi）、
   不做密林夜射（saixiaqu-linan）、不做行军出关（congjunxing-yuben）——
   本页=闺夜-市集-关山-明堂-家园-村道 六境人生长卷，有家院群像与双兔，无战阵残垣。 */

/* —— 院墙门楼 makeYuanJS(o)：夯土墙两段+双扇门板（预开 open 角度）+门框门槛+门内暖光
   Sprite（fog:false 加色；初值=峰值，update 包络 ≤1）——「当户」之门，卷首/壹/伍/陆复用 */
function makeYuanJS(o){
  o=o||{};
  const B=new GeoBag();
  const W=o.W===undefined?20:o.W, H=o.H===undefined?4.8:o.H, open=o.open===undefined?0.14:o.open;
  const half=(W-3.4)/2;
  const wl=new THREE.BoxGeometry(half,H,0.65);
  wl.translate(-(1.75+half/2),H/2,0); B.put(wl,0x241a10);
  const wr=new THREE.BoxGeometry(half,H,0.65);
  wr.translate(1.75+half/2,H/2,0); B.put(wr,0x241a10);
  const capL=new THREE.BoxGeometry(half+0.3,0.18,0.95);
  capL.translate(-(1.75+half/2),H+0.09,0); B.put(capL,0x2e2114);
  const capR=new THREE.BoxGeometry(half+0.3,0.18,0.95);
  capR.translate(1.75+half/2,H+0.09,0); B.put(capR,0x2e2114);
  [1,-1].forEach(function(s){
    const pl=new THREE.BoxGeometry(0.34,H+0.7,0.42);
    pl.translate(s*1.78,(H+0.7)/2,0); B.put(pl,0x33220f);
    const leaf=new THREE.BoxGeometry(1.62,H-0.2,0.10);
    leaf.translate(-0.81*s,0,0); leaf.rotateY(s*open);
    leaf.translate(s*1.75,(H-0.2)/2+0.04,0); B.put(leaf,0x2a1c10);
    const band=new THREE.BoxGeometry(1.4,0.12,0.13);
    band.translate(-0.81*s,0,0); band.rotateY(s*open);
    band.translate(s*1.75,H*0.56,0); B.put(band,0x4a3418);
  });
  const liang=new THREE.BoxGeometry(4.0,0.34,0.48);
  liang.translate(0,H+0.45,0); B.put(liang,0x33220f);
  const menKan=new THREE.BoxGeometry(3.3,0.16,0.55);
  menKan.translate(0,0.08,0.4); B.put(menKan,0x2e2010);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  const lampOp=o.lampOp===undefined?0.13:o.lampOp;
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a44,
    transparent:true,opacity:lampOp,depthWrite:false,fog:false,
    blending:THREE.AdditiveBlending}));
  lamp.scale.set(5.5,5.0,1); lamp.position.set(0,H*0.52,-0.6); lamp.renderOrder=3; g.add(lamp);
  const ph=(o.seed===undefined?26101:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    lamp.material.opacity=kk*lampOp*(0.80+0.20*Math.sin(t*1.1+ph));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 织机 makeJiJS(o)：机架斜柱+机身+经轴卷布轴+踏板+坐凳（合批 1 mesh）+经线细线阵
   （1 LineSegments）+梭子（独立小 mesh，update 左右缓移）+accent 微光——「木兰当户织」 */
function makeJiJS(o){
  o=o||{};
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(2.5,0.16,1.0);
  base.translate(0,0.08,0); B.put(base,0x33220f);
  [1,-1].forEach(function(s){
    B.put(limbGeo([s*0.95,0.10,0.42],[s*0.42,2.05,-0.30],0.10,0.08,6),0x3a2a16);
    B.put(limbGeo([s*0.95,0.10,0.42],[s*0.60,1.15,0.45],0.08,0.06,6),0x2e2010);
  });
  const beam=new THREE.BoxGeometry(1.1,0.14,0.16);
  beam.translate(0,2.10,-0.30); B.put(beam,0x4a3418);
  const body=new THREE.BoxGeometry(1.7,0.42,0.55);
  body.translate(0,1.05,-0.10); B.put(body,0x402c14);
  const top=new THREE.BoxGeometry(1.7,0.10,0.55);
  top.translate(0,1.30,-0.10); B.put(top,shadeColor(0x402c14,1.3));
  const zhou=new THREE.CylinderGeometry(0.09,0.09,1.55,8);
  zhou.rotateZ(Math.PI/2); zhou.translate(0,1.52,-0.28); B.put(zhou,0x5a4224);
  const bu=new THREE.CylinderGeometry(0.07,0.07,1.5,8);
  bu.rotateZ(Math.PI/2); bu.translate(0,0.86,0.28); B.put(bu,0x5a4224);
  [1,-1].forEach(function(s){
    const tb=new THREE.BoxGeometry(0.44,0.06,0.16);
    tb.rotateX(0.5); tb.translate(s*0.35,0.28,0.55); B.put(tb,0x4a3418);
  });
  const stool=new THREE.BoxGeometry(0.62,0.10,0.5);
  stool.translate(0,0.52,0.95); B.put(stool,0x33220f);
  const sleg=new THREE.BoxGeometry(0.5,0.48,0.4);
  sleg.translate(0,0.24,0.95); B.put(sleg,0x2a1c10);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.14:o.rim,p:2.4})));
  const n=o.warp===undefined?13:o.warp, pos=new Float32Array(n*6);
  for(let i=0;i<n;i++){
    const x=-0.72+(i/(n-1))*1.44;
    pos[i*6]=x; pos[i*6+1]=1.56; pos[i*6+2]=-0.24;
    pos[i*6+3]=x; pos[i*6+4]=1.14; pos[i*6+5]=0.14;
  }
  const sg=new THREE.BufferGeometry();
  sg.setAttribute('position',new THREE.BufferAttribute(pos,3));
  const lines=new THREE.LineSegments(sg,
    new THREE.LineBasicMaterial({color:0x9a7a54,transparent:true,opacity:0.38}));
  lines.renderOrder=1; g.add(lines);
  const sh=new THREE.Mesh(new THREE.BoxGeometry(0.20,0.06,0.09),
    new THREE.MeshPhongMaterial({color:0x8a6238,shininess:20,specular:0x8a6a3a}));
  sh.position.set(0,1.20,0.10); g.add(sh);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc4823a,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(2.6,1.5,1); glow.position.set(0,1.30,0.05); glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?26102:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1.55:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    sh.position.x=0.55*Math.sin(t*0.9+ph);
    lines.material.opacity=kk*0.38*(0.80+0.20*Math.sin(t*0.9+ph));
    glow.material.opacity=kk*0.10*(0.75+0.25*Math.sin(t*1.2+ph));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 案上军帖 makeJunTieJS(o)：小案+卷轴+展帛+帛上字行细线+accent 光晕（低频呼吸）——
   「昨夜见军帖，可汗大点兵」：夜闺唯一的光点心事 */
function makeJunTieJS(o){
  o=o||{};
  const B=new GeoBag();
  const top=new THREE.BoxGeometry(1.7,0.10,0.85);
  top.translate(0,0.80,0); B.put(top,0x3a2a16);
  [[-0.72,-0.30],[0.72,-0.30],[-0.72,0.30],[0.72,0.30]].forEach(function(q){
    const lg=new THREE.BoxGeometry(0.14,0.78,0.14);
    lg.translate(q[0],0.39,q[1]); B.put(lg,0x2e2010);
  });
  const roll=new THREE.CylinderGeometry(0.055,0.055,0.62,8);
  roll.rotateZ(Math.PI/2); roll.translate(-0.35,0.88,0); B.put(roll,0x4a331c);
  const bo=new THREE.BoxGeometry(0.52,0.012,0.36);
  bo.translate(0.10,0.885,0.06); B.put(bo,0xc9b489);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.16:o.rim,p:2.4})));
  const lp=new Float32Array(24);
  for(let i=0;i<4;i++){
    lp[i*6]=0.98; lp[i*6+1]=0.90; lp[i*6+2]=-0.08+i*0.045;
    lp[i*6+3]=0.26; lp[i*6+4]=0.90; lp[i*6+5]=-0.08+i*0.045;
  }
  const lg=new THREE.BufferGeometry();
  lg.setAttribute('position',new THREE.BufferAttribute(lp,3));
  const lines=new THREE.LineSegments(lg,
    new THREE.LineBasicMaterial({color:0x6a4a2a,transparent:true,opacity:0.6}));
  lines.renderOrder=1; g.add(lines);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc4823a,
    transparent:true,opacity:0.14,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(2.2,1.6,1); glow.position.set(0.1,1.05,0.06); glow.renderOrder=3; g.add(glow);
  const ph=(o.seed===undefined?26103:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    glow.material.opacity=kk*0.14*(0.62+0.38*Math.pow(Math.max(0,Math.sin(t*0.7+ph)),3));
    lines.material.opacity=kk*0.6;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 老树 makeOldTreeJS(o)：主干+四枝（limbGeo 合批 1 mesh）——北地村口枯树剪影 */
function makeOldTreeJS(o){
  o=o||{};
  const B=new GeoBag();
  const h=o.h===undefined?6:o.h;
  B.put(limbGeo([0,0,0],[0.10,h,0],0.26,0.10,7),0x1c130c);
  B.put(limbGeo([0.08,h*0.62,0],[h*0.34,h*0.94,h*0.10],0.09,0.04,6),0x181009);
  B.put(limbGeo([0.09,h*0.80,0],[h*0.26,h*1.12,-h*0.06],0.07,0.03,6),0x181009);
  B.put(limbGeo([0.06,h*0.48,0],[-h*0.30,h*0.85,-h*0.08],0.08,0.03,6),0x181009);
  B.put(limbGeo([0.04,h*0.34,0],[-h*0.22,h*0.60,h*0.10],0.07,0.03,5),0x181009);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a1c10,emissive:0x040302}),{c:0xc4823a,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  const ph=(o.seed===undefined?26104:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.008*Math.sin(t*0.5+ph)*kk;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 骏马 makeJuJS(o)：低模马（躯干/四腿/颈/头/耳/尾/鬃，GeoBag 合批 1 mesh），
   saddle 鞍鞯、pel 辔、whip 长鞭可选；自写骨架体态（头颈前探、尾下垂）——
   「东市买骏马」「愿驰千里足」：贰配全套鞍具、肆素马候归、远景剪影作胡骑 */
function makeJuJS(o){
  o=o||{};
  const B=new GeoBag();
  const s=o.s===undefined?1:o.s;
  const coat=o.coat===undefined?0x33261a:o.coat, dk=shadeColor(coat,0.72);
  const bd=new THREE.SphereGeometry(1.5,10,8);
  bd.scale(1.45*s,1.0*s,0.68*s);
  bd.translate(0,3.1*s,0); B.put(bd,coat);
  const legR=0.17*s, legT=2.35*s;
  [[0.95,0.35],[0.95,-0.38],[-1.0,0.36],[-1.0,-0.37]].forEach(function(p){
    const lg=new THREE.CylinderGeometry(legR*0.8,legR,legT,5);
    lg.translate(p[0]*s,legT*0.5,p[1]*s);
    B.put(lg,dk);
  });
  B.put(limbGeo([1.6*s,3.7*s,0],[2.75*s,5.35*s,0],0.62*s,0.34*s,6),coat);
  const hd=new THREE.SphereGeometry(0.44*s,8,6);
  hd.scale(1.55,0.92,0.72); hd.translate(3.35*s,5.42*s,0);
  B.put(hd,dk);
  const muz=new THREE.ConeGeometry(0.16*s,0.5*s,6);
  muz.rotateZ(-Math.PI/2); muz.translate(4.05*s,5.30*s,0); B.put(muz,shadeColor(coat,0.6));
  for(let e=0;e<2;e++){
    const ear=new THREE.ConeGeometry(0.10*s,0.34*s,4);
    ear.translate(3.05*s,5.95*s,(e?0.16:-0.16)*s);
    B.put(ear,dk);
  }
  B.put(limbGeo([1.7*s,5.6*s,0],[3.1*s,5.5*s,0],0.16*s,0.05*s,5),shadeColor(coat,0.5));
  B.put(limbGeo([-2.25*s,3.9*s,0],[-3.0*s,2.1*s,0],0.26*s,0.05*s,5),dk);
  if(o.saddle){
    const an=new THREE.BoxGeometry(0.95*s,0.22*s,0.78*s);
    an.translate(0.05*s,4.35*s,0); B.put(an,0x5a3a20);
    const qiao=new THREE.BoxGeometry(0.16*s,0.30*s,0.74*s);
    qiao.translate(0.48*s,4.5*s,0); B.put(qiao,0x4a2e18);
    const jian=new THREE.BoxGeometry(1.15*s,0.10*s,0.92*s);
    jian.translate(0.05*s,4.22*s,0); B.put(jian,0x6a4a2c);
  }
  if(o.pel){
    const pei=new THREE.TorusGeometry(0.30*s,0.045*s,5,12);
    pei.translate(3.15*s,5.30*s,0); B.put(pei,0x4a3418);
  }
  if(o.whip){
    const bp=new THREE.CylinderGeometry(0.03*s,0.02*s,1.5*s,5);
    bp.rotateZ(0.9); bp.translate(-0.5*s,4.4*s,0.5*s); B.put(bp,0x2a1c10);
  }
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a2014,emissive:0x040302}),{c:0xc4823a,i:o.rim===undefined?0.14:o.rim,p:2.2}));
  g.add(mesh);
  const ph=(o.seed===undefined?26105:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    mesh.position.y=0.05*s*(1+Math.sin(t*1.3+ph))*kk;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 市摊 makeShiTanJS(o)：木架横杆+布幌（Plane 顶点波动，accent 顶边）+鞍具座——
   「东市买骏马」的市集一角 */
function makeShiTanJS(o){
  o=o||{};
  const B=new GeoBag();
  const H=o.H===undefined?2.6:o.H, W=o.W===undefined?2.0:o.W;
  [1,-1].forEach(function(s){
    const post=new THREE.CylinderGeometry(0.07,0.09,H,6);
    post.translate(s*W/2,H/2,0); B.put(post,0x33220f);
  });
  const bar=new THREE.CylinderGeometry(0.055,0.055,W+0.5,6);
  bar.rotateZ(Math.PI/2); bar.translate(0,H-0.08,0); B.put(bar,0x3a2a16);
  const an=new THREE.BoxGeometry(1.0,0.20,0.7);
  an.translate(0.3,0.85,0.25); B.put(an,0x4a331c);
  const leg=new THREE.BoxGeometry(0.9,0.8,0.6);
  leg.translate(0.3,0.42,0.25); B.put(leg,0x2a1c10);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  const bw=o.bw===undefined?1.7:o.bw, bh=o.bh===undefined?1.15:o.bh;
  const geo=new THREE.PlaneGeometry(bw,bh,8,3);
  geo.translate(0,-bh/2,0);
  const base=geo.attributes.position.array.slice(), cnt=geo.attributes.position.count;
  const cols=new Float32Array(cnt*3);
  const cb=new THREE.Color(0x8a5a30), ca=new THREE.Color(0xc4823a);
  for(let i=0;i<cnt;i++){
    const t=Math.max(0,(base[i*3+1]+bh)/bh);
    const c=cb.clone().lerp(ca,t*0.8);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(cols,3));
  const bu=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,emissive:0x140b05}));
  bu.position.set(0,H-0.10,0); g.add(bu);
  const pos=geo.attributes.position, ph=(o.seed===undefined?26106:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<pos.count;i++){
      const bx=base[i*3], by=base[i*3+1], f=(by+bh)/bh;
      pos.array[i*3+2]=Math.sin(bx*2.2-t*2.6+ph)*0.14*f*kk;
      pos.array[i*3+1]=by-Math.abs(Math.sin(bx*1.4-t*1.9+ph))*0.05*f*kk;
    }
    pos.needsUpdate=true;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 长幡 makeFanJS(o)：旗杆+细长横幡（Plane 顶点波动，accent 顶边光）——
   明堂双幡/市集村口一幡（杆合批 1 mesh，幡布独立 1 mesh） */
function makeFanJS(o){
  o=o||{};
  const H=o.H===undefined?6.2:o.H, W=o.W===undefined?1.7:o.W, Hh=o.Hh===undefined?2.3:o.Hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.075,0.11,H,7);
  pole.translate(-W/2-0.35,H/2,0); B.put(pole,0x342413);
  const fin=new THREE.ConeGeometry(0.13,0.44,6);
  fin.translate(-W/2-0.35,H+0.20,0); B.put(fin,0x8a6a3a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:0.20,p:2.6})));
  const geo=new THREE.PlaneGeometry(W,Hh,10,4);
  geo.translate(W/2+0.02,0,0);
  const base=geo.attributes.position.array.slice(), cnt=geo.attributes.position.count;
  const cols=new Float32Array(cnt*3);
  const cb=new THREE.Color(0x241610), ca=new THREE.Color(0xc4823a);
  for(let i=0;i<cnt;i++){
    const y=base[i*3+1];
    const t=Math.max(0,((y+Hh/2)/Hh-0.70)/0.30);
    const c=cb.clone().lerp(ca,t*0.85);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(cols,3));
  const fan=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,emissive:0x140b05}));
  fan.position.y=H-Hh/2-0.55; g.add(fan);
  const pos=geo.attributes.position, ph=(o.seed===undefined?26107:o.seed)%6.283;
  g.userData.update=function(t,k,wind){
    const kk=k===undefined?1:k, wd=(wind===undefined?1:wind)*kk;
    for(let i=0;i<pos.count;i++){
      const bx=base[i*3], by=base[i*3+1], f=bx/W;
      pos.array[i*3+2]=Math.sin(bx*1.6-t*3.2+by*0.8+ph)*0.30*f*f*wd;
      pos.array[i*3+1]=by-Math.abs(Math.sin(bx*1.2-t*2.4+ph))*0.09*f*f*wd;
    }
    pos.needsUpdate=true;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 烽燧 makeFengsuiJS(o)：夯土台身+垛口+台顶火焰（makeFlame）+狼烟（makeGlow）+
   金柝声光点（Sprite 脉冲）——「朔气传金柝」的边关信号 */
function makeFengsuiJS(o){
  o=o||{};
  const B=new GeoBag();
  const H=o.H===undefined?6.5:o.H;
  const b1=new THREE.BoxGeometry(3.2,H*0.55,3.2);
  b1.translate(0,H*0.275,0); B.put(b1,0x2e2114);
  const b2=new THREE.BoxGeometry(2.6,H*0.45,2.6);
  b2.translate(0,H*0.55+H*0.225,0); B.put(b2,0x352618);
  for(let i=0;i<4;i++){
    const a=i/4*6.283+0.4;
    const dk=new THREE.BoxGeometry(0.4,0.5,0.4);
    dk.translate(Math.sin(a)*1.1,H+0.22,Math.cos(a)*1.1); B.put(dk,0x3a2a16);
  }
  const men=new THREE.BoxGeometry(0.8,1.3,0.2);
  men.translate(0,0.65,1.55); B.put(men,0x120c07);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x4a3820,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.16:o.rim,p:2.2})));
  const flame=makeFlame({h:1.15,w:0.52,core:0xffd898,outer:0xd06020,embers:18,light:0.9,
    lightC:0xff9a40,lightD:26,spark:false});
  flame.g.position.set(0,H+0.5,0); g.add(flame.g);
  const smoke=makeGlow({n:12,box:[0.7,6.5,0.7],pos:[0,H+2.6,0],color:0x8a8478,size:2.4,
    speed:0.04,rise:1,add:false,maxA:0.12});
  smoke.points.renderOrder=3; g.add(smoke.points);
  const tuo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc4823a,
    transparent:true,opacity:0.20,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  tuo.scale.set(3.2,3.2,1); tuo.position.set(0,H+1.2,0); tuo.renderOrder=4; g.add(tuo);
  const ph=(o.seed===undefined?26108:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    flame.update(t,kk);
    smoke.update(t);
    tuo.material.opacity=kk*0.20*Math.pow(Math.max(0,Math.sin(t*1.1+ph)),12);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 明堂 makeMingtangJS(o)：双层台基+六柱+檐额+殿顶+正脊+殿门暖光（合批 1 mesh）——
   「归来见天子，天子坐明堂」 */
function makeMingtangJS(o){
  o=o||{};
  const B=new GeoBag();
  const W=o.W===undefined?19:o.W, D=o.D===undefined?11:o.D;
  const b1=new THREE.BoxGeometry(W+6,1.2,D+4);
  b1.translate(0,0.6,0); B.put(b1,0x2a1e12);
  const b2=new THREE.BoxGeometry(W+2.6,0.9,D+1.6);
  b2.translate(0,1.8,0); B.put(b2,0x33230f);
  for(let i=0;i<3;i++){
    const st=new THREE.BoxGeometry(6.5-i*1.4,0.34,1.5);
    st.translate(0,0.17+i*0.34,D/2+3.4-i*0.5); B.put(st,shadeColor(0x2a1e12,0.94+i*0.10));
  }
  for(let i=0;i<6;i++){
    const col=new THREE.CylinderGeometry(0.34,0.38,3.7,8);
    col.translate(-W/2+0.8+i*(W-1.6)/5,1.8+1.85,D/2-0.5); B.put(col,0x3a2a16);
  }
  const ef=new THREE.BoxGeometry(W+1.5,0.55,1.1);
  ef.translate(0,5.9,0); B.put(ef,0x402c14);
  const roof=new THREE.BoxGeometry(W+3.2,0.42,D+2.2);
  roof.translate(0,6.85,0); B.put(roof,0x1f1610);
  const ridge=new THREE.BoxGeometry(W-2,0.55,0.7);
  ridge.translate(0,7.35,0); B.put(ridge,0x402c14);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.15:o.rim,p:2.3})));
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a44,
    transparent:true,opacity:0.12,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(8.5,6.5,1); glow.position.set(0,3.4,D/2+0.4); glow.renderOrder=3; g.add(glow);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    glow.material.opacity=kk*0.12*(0.85+0.15*Math.sin(t*0.8));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 箱笼赐物 makeXiangJS(o)：叠放的箱笼（合批 1 mesh）——「赏赐百千强」 */
function makeXiangJS(o){
  o=o||{};
  const B=new GeoBag();
  const cols=[0x4a331c,0x3a2a16,0x54381e];
  for(let i=0;i<5;i++){
    const w=0.9+(i%3)*0.25, h=0.5+(i%2)*0.14;
    const bx=new THREE.BoxGeometry(w,h,w*0.8);
    bx.translate((i-2)*0.55+(i%2)*0.14,h/2+(i>2?0.52:0),(i%2)*0.3-0.15);
    B.put(bx,cols[i%3]);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:0.12,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 磨刀 makeMoDaoJS(o)：矮凳磨石+刀（合批 1 mesh）+火花光点（Sprite 高频脉冲）——
   「磨刀霍霍向猪羊」 */
function makeMoDaoJS(o){
  o=o||{};
  const B=new GeoBag();
  const deng=new THREE.BoxGeometry(0.9,0.42,0.6);
  deng.translate(0,0.21,0); B.put(deng,0x33220f);
  const shi=new THREE.BoxGeometry(0.62,0.16,0.34);
  shi.rotateY(0.5); shi.translate(0,0.50,0); B.put(shi,0x4a4438);
  const dao=new THREE.BoxGeometry(0.85,0.15,0.035);
  dao.rotateY(0.5); dao.rotateZ(0.10); dao.translate(0.16,0.60,0.06); B.put(dao,0x8a8478);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x6a5a44,emissive:0x050302}),{c:0xc4823a,i:0.12,p:2.2})));
  const spark=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc060,
    transparent:true,opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  spark.scale.set(1.1,1.1,1); spark.position.set(0.30,0.66,0.14); spark.renderOrder=4; g.add(spark);
  const ph=(o.seed===undefined?26109:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    spark.material.opacity=kk*0.30*Math.pow(Math.max(0,Math.sin(t*7.3+ph)),18);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 羊圈 makeYangJS(o)：矮栅+两只低模羊（合批 1 mesh）——「磨刀霍霍向猪羊」的家畜一角 */
function makeYangJS(o){
  o=o||{};
  const B=new GeoBag();
  for(let i=0;i<5;i++){
    const post=new THREE.BoxGeometry(0.12,0.75,0.12);
    post.translate(i*0.85-1.7,0.375,0); B.put(post,0x33220f);
  }
  const rail=new THREE.BoxGeometry(3.6,0.10,0.10);
  rail.translate(0,0.58,0); B.put(rail,0x3a2a16);
  const rail2=new THREE.BoxGeometry(3.6,0.10,0.10);
  rail2.translate(0,0.30,0); B.put(rail2,0x3a2a16);
  [[-0.8,0.55],[0.5,0.4]].forEach(function(q,i){
    const s=0.9-i*0.12;
    const bd=new THREE.SphereGeometry(0.42*s,8,6);
    bd.scale(1.35,1.0,0.9); bd.translate(q[0],0.5*s,q[1]); B.put(bd,0xcabfa8);
    const hd=new THREE.SphereGeometry(0.20*s,7,5);
    hd.translate(q[0]+0.55*s,0.72*s,q[1]); B.put(hd,0x3a322a);
    for(let l=0;l<4;l++){
      const lg=new THREE.CylinderGeometry(0.05*s,0.045*s,0.34*s,5);
      lg.translate(q[0]+(l%2?0.18:-0.18)*s,0.17*s,q[1]+(l<2?0.12:-0.12)*s);
      B.put(lg,0x2e2822);
    }
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x4a4034,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  const ph=(o.seed===undefined?26110:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=0.004*Math.sin(t*0.7+ph)*kk;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 妆台明镜 makeJingtaiJS(o)：妆台+镜架圆镜+妆奁+花黄光点（合批 1 mesh+镜 1+Sprite）——
   「当窗理云鬓，对镜帖花黄」 */
function makeJingtaiJS(o){
  o=o||{};
  const B=new GeoBag();
  const tai=new THREE.BoxGeometry(1.0,0.78,0.55);
  tai.translate(0,0.39,0); B.put(tai,0x3a2a16);
  const lian=new THREE.BoxGeometry(0.34,0.20,0.24);
  lian.translate(-0.24,0.88,0.06); B.put(lian,0x54381e);
  const jia=new THREE.BoxGeometry(0.10,0.55,0.08);
  jia.translate(0.22,1.05,-0.14); B.put(jia,0x33220f);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x6a5a44,emissive:0x050302}),{c:0xc4823a,i:0.14,p:2.3})));
  const jin=new THREE.Mesh(new THREE.CircleGeometry(0.20,16),
    new THREE.MeshPhongMaterial({color:0xb8b0a0,shininess:60,specular:0xcabb98,
      emissive:0x2a261e}));
  jin.position.set(0.22,1.30,-0.09); g.add(jin);
  const hh=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc4823a,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  hh.scale.set(1.3,1.3,1); hh.position.set(0.22,1.30,-0.05); hh.renderOrder=4; g.add(hh);
  const ph=(o.seed===undefined?26111:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    hh.material.opacity=kk*0.10*(0.7+0.3*Math.sin(t*1.0+ph));
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 敞廊正屋 makeWuJS(o)：台基+四柱+额枋+悬山两坡顶+后矮墙（合批 1 mesh）——
   「开我东阁门，坐我西阁床」的家屋：开敞不闭，望得见窗内理妆 */
function makeWuJS(o){
  o=o||{};
  const B=new GeoBag();
  const W=o.W===undefined?11:o.W, D=o.D===undefined?6.5:o.D;
  const base=new THREE.BoxGeometry(W+1.2,0.55,D+1.2);
  base.translate(0,0.27,0); B.put(base,0x2a1e12);
  [[-1,-1],[1,-1],[-1,1],[1,1]].forEach(function(q){
    const col=new THREE.CylinderGeometry(0.20,0.24,3.3,8);
    col.translate(q[0]*(W/2-0.3),0.55+1.65,q[1]*(D/2-0.3)); B.put(col,0x33220f);
  });
  const ef=new THREE.BoxGeometry(W,0.34,0.5);
  ef.translate(0,4.25,D/2-0.3); B.put(ef,0x3a2a16);
  const eb=new THREE.BoxGeometry(W,0.34,0.5);
  eb.translate(0,4.25,-(D/2-0.3)); B.put(eb,0x3a2a16);
  const back=new THREE.BoxGeometry(W-0.6,1.6,0.28);
  back.translate(0,0.55+0.8,-(D/2-0.05)); B.put(back,0x2e2114);
  const rN=new THREE.BoxGeometry(W+2.2,0.20,D*0.62);
  rN.rotateX(-0.42); rN.translate(0,5.55,-D*0.30); B.put(rN,0x1f1610);
  const rS=new THREE.BoxGeometry(W+2.2,0.20,D*0.62);
  rS.rotateX(0.42); rS.translate(0,5.55,D*0.30); B.put(rS,0x1f1610);
  const ridge=new THREE.BoxGeometry(W+1.4,0.30,0.55);
  ridge.translate(0,6.35,0); B.put(ridge,0x3a2a16);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x6a5232,emissive:0x050302}),{c:0xc4823a,i:o.rim===undefined?0.13:o.rim,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 低模兔 makeTuJS(o)：身/头/双长耳/尾/四短腿（合批 1 mesh）；ghost:true 为
   accent 加色幻影态——「雄兔脚扑朔，雌兔眼迷离」 */
function makeTuJS(o){
  o=o||{};
  const B=new GeoBag();
  const s=o.s===undefined?1:o.s;
  const fur=o.color===undefined?0x8a7458:o.color;
  const dk=shadeColor(fur,0.8);
  const bd=new THREE.SphereGeometry(0.30*s,8,6);
  bd.scale(1.35,0.95,0.88); bd.translate(0,0.28*s,0); B.put(bd,fur);
  const hd=new THREE.SphereGeometry(0.17*s,8,6);
  hd.translate(0.30*s,0.44*s,0); B.put(hd,dk);
  for(let e=0;e<2;e++){
    const ear=new THREE.ConeGeometry(0.05*s,0.34*s,5);
    ear.rotateZ(-0.22);
    ear.translate(0.38*s,0.68*s,(e?0.06:-0.06)*s); B.put(ear,dk);
  }
  const tail=new THREE.SphereGeometry(0.09*s,6,5);
  tail.translate(-0.38*s,0.32*s,0); B.put(tail,shadeColor(fur,1.25));
  [[0.16,0.10],[0.16,-0.10],[-0.16,0.10],[-0.16,-0.10]].forEach(function(q){
    const lg=new THREE.CylinderGeometry(0.035*s,0.03*s,0.18*s,5);
    lg.translate(q[0]*s,0.09*s,q[1]*s); B.put(lg,dk);
  });
  const g=new THREE.Group();
  if(o.ghost){
    g.add(B.mesh(new THREE.MeshBasicMaterial({color:0xd09a5c,transparent:true,
      opacity:o.op===undefined?0.26:o.op,depthWrite:false,blending:THREE.AdditiveBlending})));
  }else{
    g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      specular:0x4a4034,emissive:0x040302}),{c:0xc4823a,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  }
  return g;
}

/* —— 双兔傍地走 makeShuangTuJS(o)：一褐一灰两只兔沿椭圆交错奔走（傍地走：
   贴地小起伏、相互穿越）；ghost 为幻影态（accent 加色）；update(t,k,ex) 的
   ex 即点击增幅——跑得更快、起伏更大 */
function makeShuangTuJS(o){
  o=o||{};
  const g=new THREE.Group();
  const col=o.color===undefined?null:o.color;
  const t1=makeTuJS({color:col===null?(o.c1===undefined?0x9a7a54:o.c1):col,
    s:o.s===undefined?1:o.s,ghost:o.ghost,op:o.op});
  const t2=makeTuJS({color:col===null?(o.c2===undefined?0x5c574e:o.c2):col,
    s:o.s===undefined?1:o.s,ghost:o.ghost,op:o.op});
  g.add(t1); g.add(t2);
  const R1=o.R===undefined?4.2:o.R, R2=R1*0.62, sp=o.sp===undefined?0.5:o.sp;
  g.userData.update=function(t,k,ex){
    const kk=k===undefined?1:k, e=ex===undefined?0:ex;
    const v=sp*(1+1.5*e);
    const put=function(tu,a,ph){
      const x=Math.cos(a)*R1, z=Math.sin(a)*R2;
      tu.position.set(x,Math.abs(Math.sin(a*2.6+ph))*0.15*(1+1.2*e),z);
      const dx=-Math.sin(a)*R1, dz=Math.cos(a)*R2;
      tu.rotation.y=Math.atan2(-dz,dx);
    };
    put(t1,t*v,0); put(t2,t*v+Math.PI,0.5);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 末境幻影组 makeMulGhostJS(o)：发光双兔幻影（大弧疾走）+木兰头顶光晕，
   点击前 visible=false 硬关；update(t,k,rv) 的 rv 0→1 淡现——
   「双兔傍地走，安能辨我是雄雌」的幻化（木兰两态交叠由 bHuoban 直接驱动） */
function makeMulGhostJS(o){
  o=o||{};
  const g=new THREE.Group();
  const gt=makeShuangTuJS({ghost:true,color:0xd09a5c,s:o.s===undefined?1.12:o.s,R:7.2,sp:0.95,op:0.26});
  gt.g.position.set(o.cx===undefined?4.5:o.cx,0.06,o.cz===undefined?-5:o.cz);
  g.add(gt.g);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xc4823a,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(44,18,1); halo.position.set(2,5,-13); halo.renderOrder=3; g.add(halo);
  g.visible=false;
  return {g:g,update:function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    gt.update(t,1,r);
    gt.g.visible=kk*r>0.004;
    halo.material.opacity=kk*0.10*r*(0.75+0.25*Math.sin(t*1.3));
    g.visible=kk*r>0.004;
  }};
}

/* —— 木兰两态：全诗贯穿的同一张脸——女妆（发髻布裙）/红妆（归家艳色）/军装（幞头按剑） */
function mulNv(scale){
  return makeFigure({pose:'独立',robe:0x5c3428,belt:0x8a5a38,skin:0xd9b189,collar:0xc8a878,
    hair:0x1a120c,hat:'发髻',rimC:0xc4823a,rim:0.42,noProp:true,scale:scale===undefined?1.4:scale});
}
function mulHong(scale){
  return makeFigure({pose:'独立',robe:0x6e3230,belt:0xa87848,skin:0xd9b189,collar:0xd8b088,
    hair:0x1a120c,hat:'发髻',rimC:0xc4823a,rim:0.50,noProp:true,scale:scale===undefined?1.4:scale});
}
function mulJun(scale){
  return makeFigure({pose:'按剑',robe:0x3c342c,belt:0x6a5232,skin:0xd9b189,collar:0x8a7a5c,
    hair:0x14100a,hat:'幞头',rimC:0xc4823a,rim:0.38,noProp:true,scale:scale===undefined?1.45:scale});
}
function mulSitting(scale,robe){
  return makeFigure({pose:'坐饮',robe:robe===undefined?0x5c3428:robe,belt:0x8a5a38,
    skin:0xd9b189,collar:0xc8a878,hair:0x1a120c,hat:'发髻',rimC:0xc4823a,rim:0.40,
    noProp:true,scale:scale===undefined?1.3:scale});
}
function figMats(fig){
  const set=[];
  fig.traverse(function(o){ if(o.material&&set.indexOf(o.material)<0)set.push(o.material); });
  return set;
}

function bCover(){ // 卷首 · 北地村暮：暮色大漠尽头的村落院门，门内一点灯火，老树沙丘远山环合
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0d0906,c2:0x1a120a,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeRange({r:250,h:16,layers:2,peaks:5,seed:26121,color:0x140d07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xc4823a,y:-8,order:-6});
  yuan.g.position.set(0,0,-185); g.add(yuan.g);
  const dun=makeRange({r:150,h:7,layers:1,peaks:7,seed:26122,color:0x1a1209,atmo:0x2e2114,
    fogK:0.60,glowK:0.04,glow:0xb08a52,y:-4,order:-5});
  dun.g.position.set(0,0,-95); g.add(dun.g);
  const jy=makeYuanJS({open:0.16,lampOp:0.15,seed:26101}); jy.g.position.set(0,0,-24); g.add(jy.g);
  const t1=makeOldTreeJS({h:7,seed:26103}); t1.g.position.set(-13,0,-18); g.add(t1.g);
  const t2=makeOldTreeJS({h:5.5,seed:26105}); t2.g.position.set(15,0,-14);
  t2.g.rotation.y=2.1; g.add(t2.g);
  const mist=makeMist({n:5,spread:[130,10,56],pos:[0,3.2,-16],scale:44,color:0x2e2114,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[90,14,44],pos:[0,8,0],color:0xb08a52,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x080503,seed:26123,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(-13,-1.6,21); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26124,sway:0.6,rim:0.08,rimC:0xc4823a});
  fg2.g.position.set(13.5,-1.8,20); g.add(fg2.g);
  addLights(g,{c:0xc49a68,i:0.30,p:[-40,55,-40]},{c:0x2a1e12,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0); dun.update(t,0);
    jy.update(t,k); t1.update(t,k); t2.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bJizhu(){ // 壹 · 机杼叹息 —— 唧唧复唧唧，木兰当户织：
                   // 夜闺织机，木兰停梭长叹；门边案上军帖微光，一盏油灯照着心事
  const g=new THREE.Group();
  const grd=makeGround({r:110,c1:0x0c0806,c2:0x181008,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeRange({r:240,h:14,layers:2,peaks:5,seed:26125,color:0x130c07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xc4823a,y:-8,order:-6});
  yuan.g.position.set(0,0,-160); g.add(yuan.g);
  const jy=makeYuanJS({W:20,H:5.0,open:0.34,lampOp:0.14,seed:26102});
  jy.g.position.set(2.5,0,-12); jy.g.rotation.y=0.10; g.add(jy.g);
  const ji=makeJiJS({seed:26102}); ji.g.position.set(1.6,0,-7.2);
  ji.g.rotation.y=Math.PI+0.15; g.add(ji.g);
  const ml=mulSitting(1.32); ml.position.set(1.6,0,-5.6); ml.rotation.y=Math.PI+0.35; g.add(ml);
  const jt=makeJunTieJS({seed:26103}); jt.g.position.set(4.6,0,-8.2);
  jt.g.rotation.y=0.55; g.add(jt.g);
  const dt=new THREE.Mesh(new THREE.CylinderGeometry(0.24,0.30,0.5,8),
    new THREE.MeshPhongMaterial({color:0x33220f,shininess:8,specular:0x4a3820}));
  dt.position.set(6.2,0.25,-9.5); g.add(dt);
  const flame=makeFlame({h:0.55,w:0.24,core:0xffd898,outer:0xc05a18,embers:12,light:0.9,
    lightC:0xff9a40,lightD:22,spark:false});
  flame.g.position.set(6.2,0.62,-9.5); g.add(flame.g);
  const mist=makeMist({n:5,spread:[120,9,50],pos:[0,3.0,-14],scale:42,color:0x2e2114,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[84,12,40],pos:[0,7,0],color:0xb08a52,size:3.2,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x070403,seed:26126,rim:0.09,rimC:0xc4823a});
  fg1.g.position.set(-10.5,-1.5,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:16,n:6,d:4,color:0x070403,seed:26127,sway:0.5,rim:0.08,rimC:0xc4823a});
  fg2.g.position.set(11,-1.7,16); g.add(fg2.g);
  addLights(g,{c:0xb08a5c,i:0.26,p:[-30,44,-30]},{c:0x281d10,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0);
    jy.update(t,k); ji.update(t,k);
    jt.update(t,k); flame.update(t,k);
    ml.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bShian(){ // 贰 · 市鞍赴边 —— 东市买骏马……旦辞爷娘去，暮宿黄河边：
                   // 晨光市集，木兰军装牵骏马立于鞍摊之间；远处黄河水光一带，黑山燕山在望
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0e0a06,c2:0x1c1309,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const he=makeWater({size:300,seg:64,amp:0.08,freq:0.16,speed:0.24,flow:[0.10,0.02],spec:1.0,
    deep:0x0a0805,shallow:0x241708,skyc:0x2f2210,moonDir:[0.2,0.12,-0.9]});
  he.mesh.material.uniforms.uMoonColor.value=C(0xc4a068);
  he.mesh.position.set(34,-0.35,-100); g.add(he.mesh);
  const shan=makeRange({r:250,h:30,layers:2,peaks:6,seed:26127,color:0x150d07,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xc4823a,y:-10,order:-6});
  shan.g.position.set(0,0,-165); g.add(shan.g);
  const dun=makeRange({r:130,h:6,layers:1,peaks:6,seed:26128,color:0x1a1209,atmo:0x2e2114,
    fogK:0.60,glowK:0.04,glow:0xb08a52,y:-4,order:-5});
  dun.g.position.set(-30,0,-80); g.add(dun.g);
  const tan1=makeShiTanJS({seed:26106}); tan1.g.position.set(-8.5,0,-6.5);
  tan1.g.rotation.y=0.5; g.add(tan1.g);
  const tan2=makeShiTanJS({seed:26107,W:1.7}); tan2.g.position.set(-5.8,0,-10);
  tan2.g.rotation.y=0.9; g.add(tan2.g);
  const fan=makeFanJS({H:5.6,Hh:2.0,seed:26109}); fan.g.position.set(-10.5,0,-11);
  fan.g.rotation.y=0.7; g.add(fan.g);
  const ma=makeJuJS({s:1.22,saddle:true,pel:true,whip:true,seed:26105});
  ma.g.position.set(2.6,0,-6.0); ma.g.rotation.y=0.35; g.add(ma.g);
  const ml=mulJun(1.42); ml.position.set(0.8,0,-4.8); ml.rotation.y=0.55; g.add(ml);
  const hq1=makeJuJS({s:0.8,coat:0x241a10,rim:0.08,seed:26112});
  hq1.g.position.set(-27,0,-52); hq1.g.rotation.y=-0.6; g.add(hq1.g);
  const hq2=makeJuJS({s:0.74,coat:0x201709,rim:0.08,seed:26113});
  hq2.g.position.set(-21,0,-60); hq2.g.rotation.y=-0.3; g.add(hq2.g);
  const mist=makeMist({n:5,spread:[140,10,58],pos:[0,3.2,-16],scale:46,color:0x2e2114,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[96,13,44],pos:[0,8,2],color:0xb08a52,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x080503,seed:26129,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(-12,-1.6,18); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:24,h:3.0,color:0x080503,seed:26130,rim:0.08,rimC:0xc4823a});
  fg2.g.position.set(2,-3.0,16.5); g.add(fg2.g);
  addLights(g,{c:0xc09058,i:0.32,p:[38,48,-30]},{c:0x2c2012,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); he.update(t);
    shan.update(t,0); dun.update(t,0);
    tan1.update(t,k); tan2.update(t,k); fan.update(t,k);
    ma.update(t,k); hq1.update(t,k); hq2.update(t,k);
    ml.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bGuanshan(){ // 叁 · 关山铁衣 —— 万里赴戎机，朔气传金柝，寒光照铁衣：
                      // 大关山重岭之间烽燧孤光，山径铁衣行军长龙，木兰牵马当先
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0c0906,c2:0x181008,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,20);
  const shan=makeRange({r:270,h:58,layers:3,peaks:8,seed:26131,color:0x120c07,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xb08a52,y:-12,order:-6});
  shan.g.position.set(0,0,-130); g.add(shan.g);
  const zui=makeRange({arc:1.0,a0:0.5,r:95,h:24,layers:2,peaks:5,seed:26132,color:0x160e08,
    atmo:0x2e2114,fogK:0.58,glowK:0.05,glow:0xc4823a,y:-6,order:-5});
  zui.g.position.set(-18,0,-58); g.add(zui.g);
  const lie=makeCrowd({n:26,rect:[-30,-42,42,22],color:0x1c150e,rimC:0xc4823a,rim:0.16,
    sMin:0.7,sMax:1.0,seed:26115});
  g.add(lie.mesh);
  const hang=makeGlow({n:14,box:[38,2.6,20],pos:[-8,4.4,-32],color:0xd8a060,size:2.2,
    speed:0.02,rise:0,add:true,maxA:0.13});
  hang.points.renderOrder=3; g.add(hang.points);
  const fs=makeFengsuiJS({scale:1.4,seed:26108}); fs.g.position.set(20,0,-46); g.add(fs.g);
  const ma=makeJuJS({s:0.95,saddle:true,pel:true,seed:26114});
  ma.g.position.set(2.0,0,-17); ma.g.rotation.y=-0.45; g.add(ma.g);
  const ml=mulJun(1.32); ml.position.set(3.7,0,-15.4); ml.rotation.y=-0.25; g.add(ml);
  const shuoqi=makeMist({n:6,spread:[150,11,60],pos:[0,4.0,-18],scale:46,color:0x6a6258,op:0.10});
  g.add(shuoqi.g);
  const motes=makeGlow({n:20,box:[100,14,46],pos:[0,9,-4],color:0xa88a58,size:3.2,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x070403,seed:26133,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(-13,-1.8,22); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x070403,seed:26134,rim:0.09,rimC:0xc4823a});
  fg2.g.position.set(12,-1.4,20); g.add(fg2.g);
  addLights(g,{c:0xa8804e,i:0.28,p:[-36,52,-36]},{c:0x241a0e,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); shan.update(t,0); zui.update(t,0);
    lie.update(t); hang.update(t);
    fs.update(t,k);
    ma.update(t,k); ml.update(t,k);
    shuoqi.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bCishang(){ // 肆 · 辞赏还乡 —— 归来见天子，天子坐明堂……愿驰千里足，送儿还故乡：
                     // 明堂柱列双幡，阶下箱笼赐物；木兰军装辞赏，千里马候归途
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0d0906,c2:0x1a1209,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,18);
  const shan=makeRange({r:260,h:18,layers:2,peaks:5,seed:26135,color:0x140d07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xc4823a,y:-8,order:-6});
  shan.g.position.set(0,0,-180); g.add(shan.g);
  const mt=makeMingtangJS({scale:1.3,rim:0.20,seed:26109}); mt.g.position.set(0,0,-24); g.add(mt.g);
  const tz=mulSitting(1.15,0x2c2018); tz.position.set(0,2.73,-26.5);
  tz.rotation.y=Math.PI; g.add(tz);
  const fan1=makeFanJS({H:6.4,Hh:2.4,seed:26110}); fan1.g.position.set(-9.5,2.73,-18);
  fan1.g.rotation.y=0.15; g.add(fan1.g);
  const fan2=makeFanJS({H:6.4,Hh:2.4,seed:26111}); fan2.g.position.set(9.5,2.73,-18);
  fan2.g.rotation.y=Math.PI-0.15; g.add(fan2.g);
  const xg1=makeXiangJS({}); xg1.position.set(-8.2,2.73,-15.6); g.add(xg1);
  const xg2=makeXiangJS({}); xg2.position.set(8.8,2.73,-15.4);
  xg2.rotation.y=0.5; g.add(xg2);
  const ml=mulJun(1.45); ml.position.set(2.6,2.73,-13.6); ml.rotation.y=Math.PI+0.4; g.add(ml);
  const ma=makeJuJS({s:1.18,pel:true,seed:26116});
  ma.g.position.set(9.4,0,-11.2); ma.g.rotation.y=-1.15; g.add(ma.g);
  const mist=makeMist({n:5,spread:[140,10,56],pos:[0,3.4,-16],scale:46,color:0x2e2114,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[98,13,46],pos:[0,8,0],color:0xb08a52,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'栏杆',w:24,h:3.0,color:0x080503,seed:26136,rim:0.08,rimC:0xc4823a});
  fg1.g.position.set(0,-3.0,16.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x080503,seed:26137,rim:0.09,rimC:0xc4823a});
  fg2.g.position.set(-11.5,-1.5,17); g.add(fg2.g);
  addLights(g,{c:0xc09058,i:0.30,p:[30,50,-32]},{c:0x2c2012,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); shan.update(t,0);
    mt.update(t,k);
    fan1.update(t,k); fan2.update(t,k);
    ma.update(t,k);
    ml.update(t,k); tz.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bXiangying(){ // 伍 · 家人相迎 —— 爷娘出郭相扶将……当窗理云鬓，对镜帖花黄：
                       // 黄昏家园：敞廊窗内木兰理妆，院中爷娘相扶、阿姊迎门、小弟磨刀霍霍
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0e0a06,c2:0x1c1309,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const shan=makeRange({r:250,h:14,layers:2,peaks:5,seed:26138,color:0x140d07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xc4823a,y:-8,order:-6});
  shan.g.position.set(0,0,-170); g.add(shan.g);
  const jy=makeYuanJS({W:24,H:5.4,open:0.6,lampOp:0.13,seed:26103});
  jy.g.position.set(1,0,-15); jy.g.rotation.y=0.06; g.add(jy.g);
  const wu=makeWuJS({}); wu.position.set(-4.5,0,-22.5); wu.rotation.y=0.06; g.add(wu);
  const jt=makeJingtaiJS({}); jt.g.position.set(-2.4,0.55,-19.8);
  jt.g.rotation.y=0.45; g.add(jt.g);
  const ml=mulSitting(1.28,0x6e3230); ml.position.set(-3.4,0.55,-19.3);
  ml.rotation.y=0.75; g.add(ml);
  const chw=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a44,
    transparent:true,opacity:0.10,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  chw.scale.set(9,6,1); chw.position.set(-4.2,3.2,-20.5); chw.renderOrder=3; g.add(chw);
  const ye=makeFigure({pose:'独立',robe:0x4a3a28,belt:0x6a5232,skin:0xd9b189,collar:0x9a8a6a,
    hair:0x181008,hat:'幞头',beard:true,rimC:0xc4823a,rim:0.30,noProp:true,scale:1.36});
  ye.position.set(-7.0,0,-11.6); ye.rotation.y=0.55; g.add(ye);
  const niang=makeFigure({pose:'独立',robe:0x54402e,belt:0x8a6a44,skin:0xd9b189,collar:0xb0a084,
    hair:0x1a120c,hat:'发髻',rimC:0xc4823a,rim:0.32,noProp:true,scale:1.28});
  niang.position.set(-5.8,0,-10.9); niang.rotation.y=-0.9; g.add(niang);
  const zi=makeFigure({pose:'独立',robe:0x74403a,belt:0xa87848,skin:0xd9b189,collar:0xd8b088,
    hair:0x1a120c,hat:'发髻',rimC:0xc4823a,rim:0.40,noProp:true,scale:1.34});
  zi.position.set(-9.6,0,-13.4); zi.rotation.y=-0.55; g.add(zi);
  const di=makeFigure({pose:'独立',robe:0x3c3226,belt:0x7a5a34,skin:0xd9b189,collar:0x8a7a5c,
    hair:0x181008,hat:'发髻',rimC:0xc4823a,rim:0.30,noProp:true,scale:1.24});
  di.position.set(-8.6,0,-9.8); di.rotation.y=0.85; g.add(di);
  const md=makeMoDaoJS({}); md.g.position.set(-7.8,0,-8.9); g.add(md.g);
  const yg=makeYangJS({}); yg.g.position.set(-13.0,0,-13.0);
  yg.g.rotation.y=0.2; g.add(yg.g);
  const smoke=makeGlow({n:12,box:[0.8,7,0.8],pos:[-5,8,-25],color:0x8a8478,size:2.6,
    speed:0.035,rise:1,add:false,maxA:0.10});
  smoke.points.renderOrder=3; g.add(smoke.points);
  const mist=makeMist({n:5,spread:[130,10,54],pos:[0,3.4,-13],scale:44,color:0x33241a,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[92,13,44],pos:[0,7,2],color:0xc49058,size:3.4,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x080503,seed:26139,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(11,-1.5,16); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26140,sway:0.5,rim:0.08,rimC:0xc4823a});
  fg2.g.position.set(-12,-1.7,15); g.add(fg2.g);
  addLights(g,{c:0xc89058,i:0.30,p:[-30,46,-30]},{c:0x2e2113,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); shan.update(t,0);
    jy.update(t,k);
    jt.update(t,k); md.update(t,k); yg.update(t,k);
    chw.material.opacity=k*0.10*(0.82+0.18*Math.sin(t*1.1));
    smoke.update(t);
    ml.update(t,k); ye.update(t,k); niang.update(t,k); zi.update(t,k); di.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bHuoban(){ // 陆（末境·可点击）· 火伴惊忙 —— 出门看火伴……双兔傍地走，安能辨我是雄雌：
                    // 木兰红妆当门而立，火伴惊忙于前；双兔傍地交错奔走。
                    // 点击：双兔幻影大弧疾走+木兰军装/红妆两态若隐若现交叠明灭+题字
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0d0906,c2:0x1a1209,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const shan=makeRange({r:250,h:15,layers:2,peaks:5,seed:26141,color:0x140d07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xc4823a,y:-8,order:-6});
  shan.g.position.set(0,0,-175); g.add(shan.g);
  const jy=makeYuanJS({W:22,H:5.2,open:0.5,lampOp:0.12,seed:26104});
  jy.g.position.set(0,0,-19); jy.g.rotation.y=0.04; g.add(jy.g);
  const nv=mulHong(1.42); nv.position.set(0,0,-16.2); nv.rotation.y=0.06; g.add(nv);
  const jun=mulJun(1.42); jun.position.set(0,0,-16.2); jun.rotation.y=0.06;
  jun.visible=false; g.add(jun);
  const nvM=figMats(nv), junM=figMats(jun);
  const hA=makeFigure({pose:'指月',robe:0x3a322a,belt:0x6a5232,skin:0xd9b189,collar:0x8a7a5c,
    hair:0x14100a,hat:'幞头',rimC:0xc4823a,rim:0.30,noProp:true,scale:1.36});
  hA.position.set(-2.9,0,-9.6); hA.rotation.y=0.85; g.add(hA);
  const hB=makeFigure({pose:'独立',robe:0x363028,belt:0x6a5232,skin:0xd9b189,collar:0x8a7a5c,
    hair:0x14100a,hat:'幞头',rimC:0xc4823a,rim:0.30,noProp:true,scale:1.32});
  hB.position.set(3.1,0,-9.0); hB.rotation.y=-0.7; g.add(hB);
  const huo=makeCrowd({n:7,rect:[-7.5,-14.5,15,4.2],color:0x241c12,rimC:0xc4823a,rim:0.14,
    sMin:0.82,sMax:1.05,seed:26116});
  g.add(huo.mesh);
  const fan=makeFanJS({H:5.8,Hh:2.1,seed:26112}); fan.g.position.set(-9.5,0,-12);
  fan.g.rotation.y=0.4; g.add(fan.g);
  const tu=makeShuangTuJS({s:1.35,c1:0xa8865c,c2:0x746e64,R:4.6,sp:0.55});
  tu.g.position.set(3.8,0.02,-3.6); g.add(tu.g);
  /* 标志性交互：双兔幻影+两态交叠（点击前幻影组 visible=false 硬关） */
  const gh=makeMulGhostJS({cx:3.8,cz:-3.6,s:1.6}); g.add(gh.g);
  const shuoqi=makeMist({n:6,spread:[130,10,56],pos:[0,3.4,-13],scale:46,color:0x2e2114,op:0.09});
  g.add(shuoqi.g);
  const motes=makeGlow({n:22,box:[92,13,44],pos:[0,7,0],color:0xb08a52,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x080503,seed:26142,rim:0.10,rimC:0xc4823a});
  fg1.g.position.set(-11,-1.5,15); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26143,sway:0.5,rim:0.08,rimC:0xc4823a});
  fg2.g.position.set(11.5,-1.7,15.5); g.add(fg2.g);
  addLights(g,{c:0xc09058,i:0.28,p:[-30,46,-30]},{c:0x2a1e12,i:0.52});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/7.0);
      const e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      tu.update(t,k,ctl.reveal>0?e:0);
      gh.update(t,k,ctl.reveal);
      if(ctl.reveal>0){
        jun.visible=e>0.01;
        const os=0.5+0.5*Math.sin(t*1.15);
        for(let i=0;i<nvM.length;i++)nvM[i].opacity=k*(1-0.62*os*e);
        for(let i=0;i<junM.length;i++)junM[i].opacity=k*(0.30+0.62*os)*e;
      }
      nv.update(t,k); if(jun.visible)jun.update(t,k);
      hA.update(t,k); hB.update(t,k);
      fan.update(t,k);
      jy.update(t,k);
      shuoqi.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); shan.update(t,0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.10);
        pluck(5,0.05,0.12); pluck(2,0.90,0.10); pluck(0,1.80,0.08);
        const fl=$('#flash'); fl.textContent='雄兔脚扑朔 雌兔眼迷离 安能辨我是雄雌';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x150f09),hor:C(0x2f2210),bot:C(0x0b0806),fog:C(0x190f08),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-70,28,-190),ms:0.30,mph:0.46,mhaze:0.20,dirC:C(0xb08a52),dirI:0.32,
  dirP:new THREE.Vector3(-48,50,-26),ambC:C(0x2b1f13),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.5,46],t:[0,8.5,38],lf:[2,8,-24],lt:[3,8.5,-38]},
  sky:()=>SK({fd:0.0048,star:0.10,hor:C(0x40280f),ms:0.34,mph:0.42,mhaze:0.24}) },
{ name:'机杼叹息',dwell:26,river:0.02,build:bJizhu,
  cam:{f:[7.0,3.2,6.0],t:[1.4,2.4,-4.0],lf:[3.5,2.6,-6],lt:[1.2,2.6,-12]},
  sky:()=>SK({top:C(0x120d08),hor:C(0x241708),fd:0.0054,star:0.16,
    moon:new THREE.Vector3(-58,30,-180),ms:0.30,mph:0.50,mhaze:0.22,
    dirC:C(0xb08a5c),dirI:0.26,dirP:new THREE.Vector3(-30,44,-30),
    ambC:C(0x281d10),ambI:0.52}) },
{ name:'市鞍赴边',dwell:22,river:0.03,build:bShian,
  cam:{f:[-3,3.6,14],t:[2,3.2,7],lf:[-1,3.2,-6],lt:[4,3.4,-20]},
  sky:()=>SK({top:C(0x171009),hor:C(0x4a3416),bot:C(0x0d0905),fog:C(0x1c130a),fd:0.0056,star:0.03,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.10,
    dirC:C(0xc89050),dirI:0.32,dirP:new THREE.Vector3(38,48,-30),
    ambC:C(0x2c2012),ambI:0.56}) },
{ name:'关山铁衣',dwell:18,river:0.02,build:bGuanshan,
  cam:{f:[0,7.5,28],t:[0,6.4,18],lf:[0,6.8,-8],lt:[0,7.2,-26]},
  sky:()=>SK({top:C(0x0e0c08),hor:C(0x2c2214),fog:C(0x1a130c),fd:0.0060,star:0.40,
    moon:new THREE.Vector3(46,36,-190),ms:0.24,mph:0.55,mhaze:0.24,
    dirC:C(0xa8804e),dirI:0.26,dirP:new THREE.Vector3(-36,52,-36),
    ambC:C(0x241a0e),ambI:0.50}) },
{ name:'辞赏还乡',dwell:20,river:0.02,build:bCishang,
  cam:{f:[0,5.4,24],t:[0,4.4,14],lf:[2,5.0,-6],lt:[3,5.2,-20]},
  sky:()=>SK({top:C(0x181009),hor:C(0x3a2812),fd:0.0056,star:0.05,
    moon:new THREE.Vector3(-60,32,-180),ms:0.28,mph:0.48,mhaze:0.20,
    dirC:C(0xc09058),dirI:0.34,dirP:new THREE.Vector3(30,50,-32),
    ambC:C(0x2c2012),ambI:0.56}) },
{ name:'家人相迎',dwell:26,river:0.02,build:bXiangying,
  cam:{f:[4.5,4.4,14],t:[-2.0,3.0,8],lf:[0,3.6,-7],lt:[-3.5,3.4,-15]},
  sky:()=>SK({top:C(0x1a1109),hor:C(0x4a3012),fd:0.0054,star:0.02,
    moon:new THREE.Vector3(56,22,-170),ms:0.20,mph:0.44,mhaze:0.18,
    dirC:C(0xc89058),dirI:0.30,dirP:new THREE.Vector3(-30,46,-30),
    ambC:C(0x2e2113),ambI:0.54}) },
{ name:'火伴惊忙',dwell:22,river:0.02,build:bHuoban,
  cam:{f:[2.5,3.8,12],t:[0,2.6,5],lf:[1,3.0,-8],lt:[0,2.8,-18]},
  sky:()=>SK({top:C(0x171009),hor:C(0x382410),fd:0.0058,star:0.10,
    moon:new THREE.Vector3(-64,34,-185),ms:0.26,mph:0.48,mhaze:0.20,
    dirC:C(0xb89058),dirI:0.28,dirP:new THREE.Vector3(-30,46,-30),
    ambC:C(0x2a1e12),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('mulanci.py —— 被 build.py 消费：python build.py mulanci')
