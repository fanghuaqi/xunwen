# -*- coding: utf-8 -*-
"""laojiang.py —— 《老将行》（王维，queue no.266，大漠金戈）生成配置
四境长卷（N=4，15 分句）：
壹 少年战功（步行夺得胡马骑+射杀白额虎+转战三千里一剑百万师+汉兵霹雳虏骑畏蒺藜：
  晨光大漠演武场，少年将军徒步降服一匹人立而起的黑胡马，地面撒着铁蒺藜，远处军阵旌旗烽燧），
贰 天幸数奇（卫青天幸李广数奇+自从弃置便衰朽世事蹉跎成白首：冷月荒原两重对照——
  远处封侯将坛灯火上明（天幸者云上），近处老将白发坐断戟旁、篝火将熄、旌旗歪斜），
叁 古木穷巷（昔时飞箭无全目+卖故侯瓜学种先生柳+古木穷巷寒山虚牖+疏勒飞泉不使酒：
  黄昏穷巷，古木参天、篱笆柴门、瓜摊柳影，白首老将守着一摊故侯瓜，巷尾古井微光不改其志），
肆 犹堪一战（末境点击，标志性瞬间：贺兰山下阵如云+羽檄交驰+试拂铁衣聊持宝剑+莫嫌旧日云中守
  犹堪一战取功名。点击「犹堪一战」：①老将披甲再起（落魄/披甲两态同位交叠明灭）；
  ②旧部云集（军阵群像自暗中亮起、向前涌近）；③旌旗重振（歪斜的旧旗猛然立直、旗面猎猎）；
  题字「莫嫌旧日云中守 犹堪一战取功名」同现+三音拨弦）。
美术立意「老将的一生三折」：全卷只跟着一位老将走——少年英姿（挺拔亮甲）→ 数奇见弃（白发
坐断戟）→ 穷巷卖瓜（布衣守摊）→ 暮年请缨（重新披甲）。同一张脸三种状态：英姿/落魄/披甲，
由 makeFigure 换袍色发色姿势构成；甲衣架与宝剑贯穿末境（试拂铁衣如雪色/聊持宝剑动星文）。
大漠金戈全套色板：底色 #120d08、雾 #180f08～#1c130a 系、文字 #f0e2cc，accent=#a8905f
（黄沙赭金，queue 分配强调色）只落在 UI/人物边缘光/旗顶缨座/甲衣雪色寒光/古井微光/烽火，
禁艳金。与已有边塞页第一眼可区分：不做雪原戍楼听笛（saishang-chuidi）、不做拂晓誓师整甲
（wuyi）、不做木兰人生六景（mulanci）、不做燕歌行对切——本页是**老将一人四境一生三折**：
少年夺马-天幸数奇-穷巷卖瓜-暮年请缨，有将坛有瓜摊有古井，无两态对切的歌舞帐。
标志性瞬间（境肆·queue moment：莫嫌旧日云中守犹堪一战取功名）：点击——老将披甲再起、
旧部云集、旌旗重振，甲光剑气把前三境的委屈一笔荡开。
末境点击（queue interact：点击犹堪一战——老将披甲再起）如上四步，可反复观看 reveal 渐进。
考点钉子：骑 jì／蒺藜 jí lí／数奇 shù jī（小测第 3 题落点）；蹉跎 cuō tuó／牖 yǒu／
羽檄 xí／燕弓 yān（逐字注音）；王维早期边塞诗·借汉喻唐（卫青/李广/云中守魏尚）（第 4 题）；
功过不公与老将壮心（第 5 题）。
多音字：肯数→肯属 一剑曾当→一剑曾裆 虏骑→虏寄 数奇→树饥 蒺藜→及黎 虚牖→虚友
疏勒→书乐 羽檄→羽习 燕弓→烟弓 天将→天匠 邺下→业下（tts.json sub 表，防误读）。"""

META = dict(
    N=4, slug='laojiang', title='老将行', dyn='唐 · 王维', brand_author='王 维',
    gold_rgb='168,144,95',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#a8905f; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(168,144,95,.3);
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
    tip='轻点画面 / 按空格 —— 犹堪一战，老将披甲再起',
    hint='← → 键或空格逐境游览 · 末境可点击画面：老将披甲再起，旧部云集，旌旗重振',
    cover_read='老将行。唐，王维。少年十五二十时，步行夺得胡马骑。一身转战三千里，一剑曾当百万师。自从弃置便衰朽，世事蹉跎成白首。莫嫌旧日云中守，犹堪一战取功名。',
    cover_p1='四重意境，随诗句次第展开：少年十五二十时，步行夺得胡马骑，射杀山中白额虎，一身转战三千里，一剑曾当百万师；卫青不败由天幸，李广无功缘数奇——自从弃置便衰朽，世事蹉跎成白首；昔时飞箭无全目，路旁时卖故侯瓜，苍茫古木连穷巷，寥落寒山对虚牖；贺兰山下阵如云，羽檄交驰日夕闻——试拂铁衣如雪色，聊持宝剑动星文，莫嫌旧日云中守，犹堪一战取功名。',
    cover_p2='边读诗，边看一位老将的一生三折：少年是何等英姿，中年遭逢怎样的不公，暮年穷居又如何在贺兰山警讯里重新披起铁衣——读懂「天幸」与「数奇」的对照，就读懂了他「犹堪一战」的全部分量。',
    end_h2='暮年 · 壮心', cn_word='肆',
    words_js="['再随老将赴一阵贺兰','初识摩诘，尚需共读','渐入诗境，再诵几遍','数奇之叹渐明，壮心渐见','已解功过天命之愤','老将壮心，千古一振']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'少年战功', jing:'十五二十的年纪，徒步就从胡人手里夺得战马。射杀山中白额猛虎，论勇武岂止数得上邺下那位黄须儿。只身转战三千里，一柄剑曾抵挡过百万大军。汉兵攻势迅疾如霹雳，虏骑崩逃，畏惧的只是地上的蒺藜。（夺马 · 射虎 · 一剑百万师）',
  segs:[
   {c:'少年十五二十时，', p:py('shào nián shí wǔ èr shí shí')},
   {c:'步行夺得胡马骑。', p:py('bù xíng duó dé hú mǎ qí')},
   {c:'射杀山中白额虎，', p:py('shè shā shān zhōng bái é hǔ')},
   {c:'肯数邺下黄须儿。', p:py('kěn shǔ yè xià huáng xū ér')},
   {c:'一身转战三千里，', p:py('yī shēn zhuǎn zhàn sān qiān lǐ')},
   {c:'一剑曾当百万师。', p:py('yī jiàn céng dāng bǎi wàn shī')},
   {c:'汉兵奋迅如霹雳，', p:py('hàn bīng fèn xùn rú pī lì')},
   {c:'虏骑崩腾畏蒺藜。', p:py('lǔ jì bēng téng wèi jí lí')}],
  read:'少年十五二十时，步行夺得胡马骑。射杀山中白额虎，肯数邺下黄须儿。一身转战三千里，一剑曾当百万师。汉兵奋迅如霹雳，虏骑崩腾畏蒺藜。',
  yisi:'少年十五二十时，步行夺得胡马骑——十五二十的年纪，徒步就从胡人手里夺下战马；射杀山中白额虎，肯数邺下黄须儿——深山白额猛虎一箭射杀，比起曹操那员黄须猛子曹彰来也毫不逊色。一身转战三千里，一剑曾当百万师——只身转战三千里，一柄剑抵得住百万大军；汉兵奋迅如霹雳，虏骑崩腾畏蒺藜——汉兵攻势如疾雷骤至，虏骑望风崩逃，连地上的铁蒺藜都叫他们胆寒。——四联一气，全是快马轻裘的少年意气：夺马、射虎、转战、却敌，英姿写在每一句的音节里，也为后文的弃置蓄足了反差。',
  zhu:[['少年十五二十时','十五、二十岁上下——少年时候'],['步行夺得胡马骑','徒步夺得胡人的战马。骑，读 jì，一人一马的合称，此指战马——步马夺马，极言其矫捷'],['白额虎','相传最凶猛的老虎——「射杀山中白额虎」极言其胆勇'],['肯数邺下黄须儿','肯，岂止、哪里只让；数，读 shǔ，称数、数得上。黄须儿，曹操次子曹彰，须黄而刚猛，曹操呼为「黄须儿」——此句谓少年之勇可比曹彰'],['一身转战三千里','身经百战，南北转战三千里——极言战功之盛'],['曾当百万师','曾经抵挡过百万大军。当，读 dāng，抵挡'],['霹雳','疾雷——「汉兵奋迅如霹雳」写汉军攻势如雷霆般迅疾'],['虏骑崩腾畏蒺藜','虏骑，胡人的骑兵，骑读 jì；崩腾，溃散奔逃。蒺藜，读 jí lí，带刺的野草，古时常制铁蒺藜撒地阻敌马足——虏骑畏的不是敌兵而是蒺藜，极言汉兵之威']] },
{ name:'天幸数奇', jing:'卫青出兵不败，不过靠着天幸；李广屡建战功终身难封，只因命数不好。自从被朝廷弃置不用，身子便衰朽下来；世事蹉跎，转眼满头白发。（天幸 · 数奇 · 白首）',
  segs:[
   {c:'卫青不败由天幸，', p:py('wèi qīng bù bài yóu tiān xìng')},
   {c:'李广无功缘数奇。', p:py('lǐ guǎng wú gōng yuán shù jī')},
   {c:'自从弃置便衰朽，', p:py('zì cóng qì zhì biàn shuāi xiǔ')},
   {c:'世事蹉跎成白首。', p:py('shì shì cuō tuó chéng bái shǒu')}],
  read:'卫青不败由天幸，李广无功缘数奇。自从弃置便衰朽，世事蹉跎成白首。',
  yisi:'卫青不败由天幸，李广无功缘数奇——卫青七击匈奴未尝败绩，不过得天之幸；李广身经七十余战，却因命数不好终身难封。自从弃置便衰朽，世事蹉跎成白首——自从此被朝廷弃置不用，身子便衰朽下来，世事蹉跎，转眼白发满头。——前两句一「由天」一「缘数」，把功过是非冷冷推给天命，正是全诗怨愤的根：老将的衰朽不是岁月使然，是被弃置折损的。少年英姿至此陡然折落，诗笔不写战场写命运的账目，最见唐诗的筋骨。',
  zhu:[['卫青','汉代名将，七击匈奴未尝败绩，官至大将军'],['天幸','天所保佑的幸运——谓卫青之不败出于运气'],['李广','汉代名将，与匈奴大小七十余战，却终身不得封侯，时人惜之'],['数奇','命运不好。数，读 shù，命运的定数；奇，读 jī，古人以单数为奇、不偶——数奇即命数不佳'],['缘','因为、由于'],['弃置','抛弃搁置——朝廷不再任用'],['衰朽','衰老朽败'],['蹉跎','光阴虚度、失时。跎，读 tuó'],['白首','白发——老将军在蹉跎中老去']] },
{ name:'古木穷巷', jing:'当年飞箭伤了眼睛，两眼未能保全；如今左肘又生出瘤子。路旁时时叫卖故侯瓜，门前学五柳先生种柳自遣。苍茫古木连着僻陋穷巷，寥落寒山空对虚牖。却立誓像疏勒城中拜井得泉那样不改其志，不肯像颍川灌夫那样借酒使气。（故侯瓜 · 先生柳 · 穷巷虚牖）',
  segs:[
   {c:'昔时飞箭无全目，', p:py('xī shí fēi jiàn wú quán mù')},
   {c:'今日垂杨生左肘。', p:py('jīn rì chuí yáng shēng zuǒ zhǒu')},
   {c:'路旁时卖故侯瓜，', p:py('lù páng shí mài gù hóu guā')},
   {c:'门前学种先生柳。', p:py('mén qián xué zhòng xiān shēng liǔ')},
   {c:'苍茫古木连穷巷，', p:py('cāng máng gǔ mù lián qióng xiàng')},
   {c:'寥落寒山对虚牖。', p:py('liáo luò hán shān duì xū yǒu')},
   {c:'誓令疏勒出飞泉，', p:py('shì lìng shū lè chū fēi quán')},
   {c:'不似颍川空使酒。', p:py('bù sì yǐng chuān kōng shǐ jiǔ')}],
  read:'昔时飞箭无全目，今日垂杨生左肘。路旁时卖故侯瓜，门前学种先生柳。苍茫古木连穷巷，寥落寒山对虚牖。誓令疏勒出飞泉，不似颍川空使酒。',
  yisi:'昔时飞箭无全目，今日垂杨生左肘——当年作战飞箭伤目，两眼未能保全；如今左肘又生出瘤子（垂杨即「柳」，谐「瘤」，用《庄子》「柳生其左肘」语）。路旁时卖故侯瓜，门前学种先生柳——像亡国的东陵侯召平那样在路旁卖瓜为生，学五柳先生在门前种柳自遣。苍茫古木连穷巷，寥落寒山对虚牖——苍茫古木连着僻陋的穷巷，寥落寒山空对无人凭望的窗牖。誓令疏勒出飞泉，不似颍川空使酒——却仍立誓像耿恭困守疏勒、拜井而飞泉涌出那样绝不丧志，不肯像颍川灌夫失势后借酒使气。——境愈穷而志愈坚：四句落魄铺到极处，末一联忽然振起，穷巷寒山反衬出这一句自誓的亮色，也为末境的请缨埋下火种。',
  zhu:[['昔时飞箭无全目','当年飞箭伤目，两眼未能保全——老将带著战伤老去'],['垂杨生左肘','如今左肘生出肿瘤。垂杨，即「柳」，谐「瘤」；《庄子·至乐》有「柳（瘤）生其左肘」之语'],['故侯瓜','汉初召平本为秦东陵侯，秦亡后种瓜长安城东，瓜美，世称「故侯瓜」——以故侯卖瓜比老将的落魄'],['先生柳','晋陶渊明宅边有五柳树，自号「五柳先生」——门前学种柳树，是穷居的闲职，也是自我解嘲'],['穷巷','偏僻的深巷'],['寥落','冷落、寂寞'],['虚牖','空空的窗户。牖，读 yǒu，窗'],['誓令疏勒出飞泉','后汉耿恭被围疏勒城，穿井十五丈不得水，整衣拜井，飞泉涌出——立誓像耿恭那样绝境中志气不改'],['颍川空使酒','汉景帝时颍川人灌夫，失势后因酒使气骂座获罪——老将虽有不平，不肯借酒撒气']] },
{ name:'犹堪一战', jing:'贺兰山下大军列阵如云，插羽的军书日夜交驰。朝廷使臣持节到三河招募少年，诏书命兵分五道出师。老将把铁甲拂拭得雪亮，拿起宝剑，剑上星纹闪动。愿得燕地强弓射杀敌将，以敌甲惊动吾君为耻。莫嫌我是旧日的云中守——还堪一战，再取功名！（阵如云 · 铁衣雪色 · 犹堪一战）（末境点击画面：老将披甲再起，旧部云集，旌旗重振）',
  segs:[
   {c:'贺兰山下阵如云，', p:py('hè lán shān xià zhèn rú yún')},
   {c:'羽檄交驰日夕闻。', p:py('yǔ xí jiāo chí rì xī wén')},
   {c:'节使三河募年少，', p:py('jié shǐ sān hé mù nián shào')},
   {c:'诏书五道出将军。', p:py('zhào shū wǔ dào chū jiāng jūn')},
   {c:'试拂铁衣如雪色，', p:py('shì fú tiě yī rú xuě sè')},
   {c:'聊持宝剑动星文。', p:py('liáo chí bǎo jiàn dòng xīng wén')},
   {c:'愿得燕弓射天将，', p:py('yuàn dé yān gōng shè tiān jiàng')},
   {c:'耻令越甲鸣吾君。', p:py('chǐ lìng yuè jiǎ míng wú jūn')},
   {c:'莫嫌旧日云中守，', p:py('mò xián jiù rì yún zhōng shǒu')},
   {c:'犹堪一战取功名。', p:py('yóu kān yī zhàn qǔ gōng míng')}],
  read:'贺兰山下阵如云，羽檄交驰日夕闻。节使三河募年少，诏书五道出将军。试拂铁衣如雪色，聊持宝剑动星文。愿得燕弓射天将，耻令越甲鸣吾君。莫嫌旧日云中守，犹堪一战取功名。',
  yisi:'贺兰山下阵如云，羽檄交驰日夕闻——边地又有战事，贺兰山下大军列阵如云，插羽的紧急军书日夜交驰；节使三河募年少，诏书五道出将军——持节使者到三河招募新兵，诏书命五道并出。试拂铁衣如雪色，聊持宝剑动星文——老将闻警而起，把搁置多年的铁甲拂拭得雪亮，拿起宝剑，剑上星纹闪闪；愿得燕弓射天将，耻令越甲鸣吾君——愿得燕地强弓射杀敌将，以敌国兵甲惊动君王为耻。莫嫌旧日云中守，犹堪一战取功名——莫嫌我是昔日的云中守，如今还堪一战，再取功名！——末五句一气呵成，「试拂」「聊持」两个轻轻的动作，把十年弃置的委屈一笔荡开：暮年请缨，掷地有声，是全诗最响亮的收束。',
  zhu:[['贺兰山','在今宁夏境内，唐代西北边防要地'],['羽檄','插着羽毛的紧急军事文书，取其疾如飞鸟。檄，读 xí'],['节使三河募年少','朝廷使臣持节到三河（河东、河内、河南）招募少年兵。年少，读 nián shào'],['诏书五道出将军','诏书命兵分五道出师——大军齐发，边情紧急'],['试拂铁衣如雪色','把铁甲擦拭得雪亮——「试」「聊」二字，是闲置多年的人闻警一试的身段'],['星文','剑身的花纹如星——剑光闪动'],['燕弓','燕地所产的强弓。燕，读 yān'],['天将','敌军的将帅'],['耻令越甲鸣吾君','以敌国兵甲惊动自己的国君为耻。用齐人雍门子狄事：越兵入境，子狄以为越甲鸣君，引剑自刎'],['云中守','汉文帝时云中太守魏尚，抚士守边有功，一度因小过削爵，赖冯唐进言得复职——「莫嫌旧日云中守」，老将以魏尚自比'],['犹堪一战','还能为国一战——全诗在老将请缨的强音中收束']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「一身转战三千里」的下一句是？', o:['一剑曾当百万师','汉兵奋迅如霹雳','步行夺得胡马骑'], a:0},
 {q:'「莫嫌旧日云中守」的下一句是？', o:['犹堪一战取功名','愿得燕弓射天将','耻令越甲鸣吾君'], a:0},
 {q:'下列加点字的读音，完全正确的一项是？', o:['「虏骑崩腾畏蒺藜」的骑读 jì、蒺藜读 jí lí；「李广无功缘数奇」的数奇读 shù jī；「寥落寒山对虚牖」的牖读 yǒu','「虏骑崩腾畏蒺藜」的骑读 qí、蒺藜读 zhí lí；「李广无功缘数奇」的数奇读 shù qí；「寥落寒山对虚牖」的牖读 yōng','「虏骑崩腾畏蒺藜」的骑读 jì、蒺藜读 jí lí；「李广无功缘数奇」的数奇读 shù qí；「门前学种先生柳」的种读 zhǒng'], a:0},
 {q:'关于《老将行》，下列说法正确的是？', o:['王维早期的边塞名篇：借汉喻唐——以卫青、李广的际遇与云中守魏尚的故事，写唐时老将有功不赏、弃置衰朽，而壮心不已','王维晚年隐居辋川后的山水小诗：全诗写隐居种瓜种柳的闲适，卫青李广只是田园点缀','一首北朝乐府民歌：采自边地军中，王维只是记录者，诗中「老将」实有其人'], a:0},
 {q:'对全诗主旨理解最恰当的一项是？', o:['为功过不公而愤：天幸者封侯、数奇者弃置；而老将在贺兰山警讯中重新披甲请缨——「犹堪一战取功名」，怨愤之中更见壮心','单纯歌颂少年将军的英雄业绩：从夺马射虎到转战千里，全诗重点在渲染战功的辉煌','感叹人生易老：从少年英姿到白首穷居，主旨是劝人及时行乐，功名如浮云不足慕'], a:0},
];
"""

SCENES_JS = """/* ================= 老将行 · 四境场景（大漠金戈·老将一生三折：少年战功、天幸数奇、古木穷巷、犹堪一战） =================
   低模骏马/旌旗/古木/篱笆/瓜摊/土屋/古井/铁衣架/宝剑/断戟/将坛/蒺藜 —— 全部自建 builder 组合 */

/* —— 低模骏马 makeHanmaLJ(o)：stand 立马 / rear 人立欲走（前蹄腾空）——「步行夺得胡马骑」 */
function makeHanmaLJ(o){
  o=o||{};
  const pose=o.pose||'stand';
  const coat=o.coat===undefined?0x33261a:o.coat, dk=shadeColor(coat,0.60), lt=shadeColor(coat,1.30);
  const B=new GeoBag();
  const bd=new THREE.SphereGeometry(1.5,10,8); bd.scale(1.58,1.02,0.76); bd.translate(0,3.05,0); B.put(bd,coat);
  const rp=new THREE.SphereGeometry(1.05,8,7); rp.scale(0.82,0.92,0.80); rp.translate(-1.85,3.02,0); B.put(rp,lt);
  function leg(x0,z,x1,y1){
    B.put(limbGeo([x0,2.7,z],[x1,y1,z],0.22,0.12,5),shadeColor(coat,0.92));
    const hf=new THREE.SphereGeometry(0.19,6,5); hf.scale(1.05,0.8,0.95); hf.translate(x1,y1-0.03,z);
    B.put(hf,dk);
  }
  if(pose==='stand'){
    leg(1.58,0.40,1.66,0.18); leg(1.58,-0.40,1.62,0.18);
    leg(-1.72,0.44,-1.80,0.18); leg(-1.72,-0.44,-1.76,0.18);
    for(let s2=0;s2<2;s2++){
      const sh=new THREE.SphereGeometry(0.48,7,6); sh.translate(1.58,2.80,(s2?0.38:-0.38)); B.put(sh,coat);
      const hc=new THREE.SphereGeometry(0.55,7,6); hc.translate(-1.72,2.85,(s2?0.42:-0.42)); B.put(hc,coat);
    }
    B.put(limbGeo([1.42,3.30,0],[2.70,4.78,0],0.80,0.44,6),coat);          // 颈：粗壮昂起
    const sk=new THREE.SphereGeometry(0.62,8,7); sk.scale(1.25,0.95,0.68); sk.rotateZ(-0.12);
    sk.translate(3.00,5.05,0); B.put(sk,coat);
    B.put(limbGeo([3.25,4.95,0],[4.25,4.72,0],0.34,0.19,6),dk);            // 颌鼻
    for(let e=0;e<2;e++){ const ear=new THREE.ConeGeometry(0.13,0.50,4);
      ear.translate(2.80,5.65,(e?0.18:-0.18)); B.put(ear,dk); }
    for(let i=0;i<5;i++){ const tt=i/4; const m=new THREE.SphereGeometry(0.24-0.09*tt,7,6);
      m.translate(1.66+1.10*tt,3.55+1.45*tt,0); B.put(m,dk); }             // 鬃：颈脊圆珠一列
    B.put(limbGeo([-2.70,3.45,0],[-3.45,1.60,0],0.28,0.10,5),dk);          // 尾：垂落
  }else{                                                                  // rear 人立：前蹄腾空
    leg(1.58,0.40,2.85,3.70); leg(1.58,-0.40,2.70,3.52);
    leg(-1.72,0.44,-2.15,0.30); leg(-1.72,-0.44,-2.08,0.28);
    for(let s2=0;s2<2;s2++){
      const sh=new THREE.SphereGeometry(0.48,7,6); sh.translate(1.58,2.80,(s2?0.38:-0.38)); B.put(sh,coat);
      const hc=new THREE.SphereGeometry(0.55,7,6); hc.translate(-1.72,2.85,(s2?0.42:-0.42)); B.put(hc,coat);
    }
    B.put(limbGeo([1.42,3.25,0],[2.95,5.15,0],0.80,0.46,6),coat);          // 颈：怒昂
    const sk=new THREE.SphereGeometry(0.62,8,7); sk.scale(1.25,0.95,0.68); sk.rotateZ(-0.30);
    sk.translate(3.30,5.55,0); B.put(sk,coat);
    B.put(limbGeo([3.55,5.45,0],[4.55,5.28,0],0.34,0.19,6),dk);
    for(let e=0;e<2;e++){ const ear=new THREE.ConeGeometry(0.13,0.50,4);
      ear.translate(3.05,6.18,(e?0.18:-0.18)); B.put(ear,dk); }
    for(let i=0;i<5;i++){ const tt=i/4; const m=new THREE.SphereGeometry(0.24-0.09*tt,7,6);
      m.translate(1.70+1.20*tt,3.50+1.62*tt,0); B.put(m,dk); }
    B.put(limbGeo([-2.75,3.40,0],[-3.60,2.20,0],0.28,0.09,5),dk);
  }
  if(o.saddle){                                                            // 鞍鞯深赭
    const dbl=new THREE.BoxGeometry(1.34,0.08,1.02); dbl.translate(-0.12,4.18,0); B.put(dbl,0x5a3a20);
    const an=new THREE.BoxGeometry(1.02,0.16,0.84); an.translate(0.05,4.30,0); B.put(an,0x4a2e18);
    const qiao=new THREE.BoxGeometry(0.15,0.26,0.78); qiao.translate(0.52,4.46,0); B.put(qiao,0x3c2414);
  }
  const g=new THREE.Group();
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x6a6048,emissive:0x050403}),{c:0xa8905f,i:o.rim===undefined?0.16:o.rim,p:2.3}));
  g.add(mesh);
  const ph=(o.seed===undefined?26611:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    mesh.position.y=0.045*(1+Math.sin(t*1.15+ph))*kk;
    if(pose!=='stand')g.rotation.z=0.018*Math.sin(t*2.3+ph)*kk;
    g.visible=kk>0.004;
  };
  g.scale.setScalar(o.scale===undefined?1.18:o.scale);
  return {g:g,update:g.userData.update};
}

/* —— 蒺藜 makeCizhenJS(o)：地面铁蒺藜一撮撮（四角刺+核心，GeoBag 1 mesh）——「虏骑崩腾畏蒺藜」 */
function makeCizhenJS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26621:o.seed);
  const n=o.n===undefined?7:o.n, w=o.w===undefined?9:o.w, d=o.d===undefined?6:o.d;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, s=0.5+0.5*R();
    const core=new THREE.SphereGeometry(0.10*s,5,4); core.translate(x,0.09*s,z); B.put(core,0x241c12);
    for(let s2=0;s2<4;s2++){
      const sp=new THREE.ConeGeometry(0.035*s,0.34*s,4);
      const ax=s2<2?1:-1, az=s2%2?1:-1;
      sp.rotateZ(ax*0.9); sp.rotateX(-az*0.9);
      sp.translate(x+ax*0.10*s,0.16*s,z+az*0.10*s);
      B.put(sp,0x2e2418);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:30,
    specular:0x5a5040,emissive:0x060503}),{c:0xa8905f,i:o.rim===undefined?0.12:o.rim,p:2.4})));
  return g;
}

/* —— 烽燧 makeDunTaiJS(o)：夯土高台+垛口+台顶烽火+烟+光晕 —— 军书日夜、羽檄交驰的信标 */
function makeDunTaiJS(o){
  o=o||{};
  const H=o.H===undefined?6.8:o.H;
  const B=new GeoBag();
  const b1=new THREE.BoxGeometry(3.0,H*0.58,3.0); b1.translate(0,H*0.29,0); B.put(b1,0x2c2012);
  const b2=new THREE.BoxGeometry(2.4,H*0.42,2.4); b2.translate(0,H*0.58+H*0.21,0); B.put(b2,0x332413);
  for(let i=0;i<4;i++){
    const a=i/4*6.283+0.4;
    const dk=new THREE.BoxGeometry(0.38,0.46,0.38);
    dk.translate(Math.sin(a)*1.02,H+0.20,Math.cos(a)*1.02); B.put(dk,0x3a2a16);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x4a3820,emissive:0x050302}),{c:0xa8905f,i:o.rim===undefined?0.15:o.rim,p:2.2})));
  const flame=makeFlame({h:1.05,w:0.48,core:0xffd898,outer:0xc85a1c,embers:14,light:o.light===undefined?0.75:o.light,
    lightC:0xff9a40,lightD:24,spark:false});
  flame.g.position.set(0,H+0.45,0); g.add(flame.g);
  const smoke=makeGlow({n:10,box:[0.7,6,0.7],pos:[0,H+2.4,0],color:0x8a8478,size:2.2,
    speed:0.04,rise:1,add:false,maxA:0.10});
  smoke.points.renderOrder=3; g.add(smoke.points);
  const tuo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8905f,
    transparent:true,opacity:0.18,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  tuo.scale.set(3.0,3.0,1); tuo.position.set(0,H+1.1,0); tuo.renderOrder=4; g.add(tuo);
  const ph=(o.seed===undefined?26622:o.seed)%6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    flame.update(t,kk);
    smoke.update(t);
    tuo.material.opacity=kk*0.18*Math.pow(Math.max(0,Math.sin(t*1.2+ph)),10);
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 旌旗 makeJingqiJS(o)：旗杆+顶缨+披幅旗面（顶点波动），tilt>0 表失修歪斜
   返回 {g,update,tilt0,wm}——wm 旗面起伏倍率（末境点击旌旗重振时上调） */
function makeJingqiJS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26631:o.seed);
  const H=o.H===undefined?7.0:o.H, W=o.W===undefined?2.7:o.W, Hh=o.Hh===undefined?2.0:o.Hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.05,0.085,H,6);
  pole.translate(0,H/2,0); B.put(pole,0x3a2c1a);
  const knob=new THREE.SphereGeometry(0.13,7,6); knob.translate(0,H+0.10,0); B.put(knob,0x8a744c);
  for(let s2=0;s2<3;s2++){
    const ts=new THREE.ConeGeometry(0.045,0.44,4); ts.rotateX(Math.PI);
    ts.translate(0,H-0.14,0); ts.rotateX((s2-1)*0.5);
    B.put(ts,0x7a2e1e);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x4a3820,emissive:0x060402}),{c:0xa8905f,i:o.rim===undefined?0.18:o.rim,p:2.3})));
  const seg=o.seg===undefined?6:o.seg, segY=o.segY===undefined?4:o.segY;
  const geo=new THREE.PlaneGeometry(W,Hh,seg,segY);
  geo.translate(W/2,0,0);
  const fmat=new THREE.MeshPhongMaterial({color:o.color===undefined?0x5a4628:o.color,
    side:THREE.DoubleSide,shininess:6,specular:0x3a2c1a,emissive:0x0a0603});
  const flag=new THREE.Mesh(geo,fmat);
  flag.position.set(0.02,H-0.42,0); g.add(flag);
  const tilt0=o.tilt===undefined?0:o.tilt, amp=o.amp===undefined?0.26:o.amp;
  g.rotation.z=tilt0;
  const ph=R()*6.283;
  const api={g:g,tilt0:tilt0,wm:1,update:function(t,k){
    const kk=k===undefined?1:k;
    const pos=geo.attributes.position;
    for(let i=0;i<pos.count;i++){
      const x=pos.getX(i);
      pos.setZ(i,(amp*api.wm)*Math.sin(t*2.1+x*1.35+ph)*(x/W)*kk);
    }
    pos.needsUpdate=true;
  }};
  return api;
}

/* —— 将坛 makeJiangtanJS(o)：三层夯土高台+台上旌旗+暖光晕——「天幸者」封侯拜将的高处 */
function makeJiangtanJS(o){
  o=o||{};
  const B=new GeoBag();
  [[4.4,1.0,0.50],[3.3,0.9,1.50],[2.3,0.85,2.42]].forEach(function(t){
    const c=new THREE.CylinderGeometry(t[0],t[0]*1.10,t[1],12);
    c.translate(0,t[2],0); B.put(c,0x241a0e);
  });
  const post=new THREE.CylinderGeometry(0.09,0.13,4.6,6); post.translate(0,5.1,0); B.put(post,0x332413);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x4a3820,emissive:0x050302}),{c:0xa8905f,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  const qi=makeJingqiJS({H:4.8,W:2.0,Hh:1.6,color:0x6a4a2a,seed:26632,amp:0.30});
  qi.g.position.set(0,5.4,0); g.add(qi.g);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8a060,
    transparent:true,opacity:0.20,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(9,7,1); glow.position.set(0,3.6,0); glow.renderOrder=4; g.add(glow);
  const lamp=new THREE.PointLight(0xd8a060,0.85,36);
  lamp.position.set(0,3.4,0); g.add(lamp);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    qi.update(t,kk);
    glow.material.opacity=kk*0.20*(0.82+0.18*Math.sin(t*1.05));
    lamp.intensity=kk*0.85;
    g.visible=kk>0.004;
  };
  return {g:g,update:g.userData.update};
}

/* —— 断戟 makeDuanJiJS(o)：斜插沙中的断杆残刃——弃置的注脚 */
function makeDuanJiJS(o){
  o=o||{};
  const B=new GeoBag();
  const sha=new THREE.CylinderGeometry(0.045,0.06,2.6,6);
  sha.translate(0,1.15,0); B.put(sha,0x33241a);
  const zhe=new THREE.ConeGeometry(0.06,0.5,5);
  zhe.rotateZ(2.6); zhe.translate(0.22,2.45,0); B.put(zhe,0x4a3a24);
  const ren=new THREE.ConeGeometry(0.05,0.34,5);
  ren.rotateZ(-Math.PI/2); ren.scale(1,1,0.45);
  ren.translate(0.16,2.28,0); B.put(ren,0x6a5a38);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x5a5040,emissive:0x050302}),{c:0xa8905f,i:o.rim===undefined?0.14:o.rim,p:2.3})));
  g.rotation.z=o.tilt===undefined?0.38:o.tilt;
  g.rotation.y=o.ry===undefined?0:o.ry;
  return g;
}

/* —— 古木/垂柳 makeGumuJS(o)：type:'木' 参天古木（粗干+苍冠）；type:'柳' 五柳（细干+垂条） */
function makeGumuJS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26641:o.seed);
  const type=o.type===undefined?'木':o.type;
  const h=o.h===undefined?(type==='木'?8.5:6.0):o.h;
  const B=new GeoBag();
  if(type==='木'){
    const t1=new THREE.CylinderGeometry(0.34,0.62,h*0.55,7);
    t1.translate(0,h*0.27,0); B.put(t1,0x241a10);
    const t2=new THREE.CylinderGeometry(0.20,0.34,h*0.5,6);
    t2.rotateZ(0.16); t2.translate(0.42,h*0.62,0.1); B.put(t2,0x241a10);
    for(let i=0;i<6;i++){
      const r=(0.9+R()*0.7)*(h/8.5);
      const cn=new THREE.SphereGeometry(r,8,6);
      cn.scale(1.25,0.62,1.1);
      cn.translate((R()-0.5)*2.6,h*0.72+R()*h*0.30,(R()-0.5)*2.0);
      B.put(cn,shadeColor(0x181008,0.8+0.5*R()));
    }
  }else{
    const t1=new THREE.CylinderGeometry(0.10,0.17,h*0.6,6);
    t1.translate(0,h*0.30,0); B.put(t1,0x2a2014);
    for(let b=0;b<7;b++){
      const a=b/7*6.283+R()*0.5;
      const bx=Math.cos(a)*(0.5+R()*0.7), bz=Math.sin(a)*(0.35+R()*0.5);
      B.put(limbGeo([0.05,h*(0.52+R()*0.16),0.02],[bx,h*(0.34+R()*0.30),bz],0.055,0.012,4),
        shadeColor(0x2a2014,0.9));
      const tf=new THREE.ConeGeometry(0.34,1.3,5);
      tf.rotateX(Math.PI); tf.translate(bx,h*(0.30+R()*0.26),bz);
      B.put(tf,shadeColor(0x1e1a0e,0.85+0.4*R()));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2e2418,emissive:0x040302}),{c:0xa8905f,i:o.rim===undefined?0.08:o.rim,p:2.0})));
  const ph=R()*6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    g.rotation.z=(type==='柳'?0.02:0.006)*Math.sin(t*0.6+ph)*kk;
  };
  return {g:g,update:g.userData.update};
}

/* —— 篱笆 makeLibaJS(o)：木桩一排+两道横杆（GeoBag 1 mesh）——穷巷柴扉 */
function makeLibaJS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26651:o.seed);
  const w=o.w===undefined?14:o.w;
  const B=new GeoBag();
  const n=Math.round(w/1.1);
  for(let i=0;i<=n;i++){
    const x=-w/2+w*i/n, hh=1.05+R()*0.25;
    const p=new THREE.CylinderGeometry(0.045,0.06,hh,5);
    p.rotateZ((R()-0.5)*0.14); p.translate(x,hh/2,0); B.put(p,0x2a1e12);
  }
  for(let r2=0;r2<2;r2++){
    const bar=new THREE.CylinderGeometry(0.035,0.035,w,5);
    bar.rotateZ(Math.PI/2); bar.translate(0,0.42+r2*0.44,0.02); B.put(bar,0x241a0e);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2e2418,emissive:0x040302}),{c:0xa8905f,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  return g;
}

/* —— 瓜摊 makeGuaTanJS(o)：矮木案+故侯瓜四五只（GeoBag 1 mesh）——「路旁时卖故侯瓜」 */
function makeGuaTanJS(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?26661:o.seed);
  const B=new GeoBag();
  const top=new THREE.BoxGeometry(2.6,0.12,1.2); top.translate(0,0.78,0); B.put(top,0x332413);
  [[-1.1,0.4],[1.1,0.4],[-1.1,-0.4],[1.1,-0.4]].forEach(function(p){
    const lg=new THREE.CylinderGeometry(0.055,0.07,0.78,5);
    lg.translate(p[0],0.39,p[1]); B.put(lg,0x2a1e12);
  });
  const n=o.n===undefined?5:o.n;
  for(let i=0;i<n;i++){
    const x=(i-(n-1)/2)*0.46+(R()-0.5)*0.12, s=0.30+R()*0.10;
    const mel=new THREE.SphereGeometry(s,9,7);
    mel.scale(1.25,0.95,1.05);
    mel.translate(x,0.90+s*0.55,(R()-0.5)*0.5);
    B.put(mel,shadeColor(0x5f6f3a,0.85+0.35*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2c1a,emissive:0x050302}),{c:0xa8905f,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  return g;
}

/* —— 土屋虚牖 makeTuWuJS(o)：夯土矮屋+破门+空窗框（虚牖）——「寥落寒山对虚牖」 */
function makeTuWuJS(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(4.4,2.3,3.2); body.translate(0,1.15,0); B.put(body,0x241a10);
  const roof=new THREE.BoxGeometry(5.2,0.42,3.9); roof.translate(0,2.5,0); B.put(roof,0x1c130a);
  const men=new THREE.BoxGeometry(0.95,1.7,0.12); men.translate(-1.0,0.85,1.62); B.put(men,0x0a0704);
  const wx=1.0, wy=1.45;
  const win=new THREE.BoxGeometry(0.9,0.75,0.10); win.translate(wx,wy,1.61); B.put(win,0x0a0704);
  const f1=new THREE.BoxGeometry(1.06,0.10,0.16); f1.translate(wx,wy+0.42,1.63); B.put(f1,0x3a2c1a);
  const f2=new THREE.BoxGeometry(1.06,0.10,0.16); f2.translate(wx,wy-0.42,1.63); B.put(f2,0x3a2c1a);
  const f3=new THREE.BoxGeometry(0.10,0.94,0.16); f3.translate(wx-0.48,wy,1.63); B.put(f3,0x3a2c1a);
  const f4=new THREE.BoxGeometry(0.10,0.94,0.16); f4.translate(wx+0.48,wy,1.63); B.put(f4,0x3a2c1a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:3,
    specular:0x2e2418,emissive:0x040302}),{c:0xa8905f,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  return g;
}

/* —— 古井 makeGujingJS(o)：石栏+井架+吊桶+井心微光（不减其志的「飞泉」余响） */
function makeGujingJS(o){
  o=o||{};
  const B=new GeoBag();
  const ring=new THREE.TorusGeometry(0.72,0.20,6,14); ring.rotateX(Math.PI/2);
  ring.translate(0,0.30,0); B.put(ring,0x3a352c);
  const inWell=new THREE.CylinderGeometry(0.72,0.72,0.5,14,1,true);
  inWell.translate(0,0.28,0); B.put(inWell,0x0c0a08);
  [[-0.66],[0.66]].forEach(function(p){
    const post=new THREE.CylinderGeometry(0.05,0.07,1.9,6);
    post.translate(p[0],0.95,0); B.put(post,0x2a1e12);
  });
  const bar=new THREE.CylinderGeometry(0.045,0.045,1.6,6);
  bar.rotateZ(Math.PI/2); bar.translate(0,1.86,0); B.put(bar,0x332413);
  const rope=new THREE.CylinderGeometry(0.02,0.02,0.7,4);
  rope.translate(0,1.5,0); B.put(rope,0x4a3820);
  const bucket=new THREE.CylinderGeometry(0.13,0.11,0.22,7);
  bucket.translate(0,1.1,0); B.put(bucket,0x241a10);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x4a4438,emissive:0x050403}),{c:0xa8905f,i:o.rim===undefined?0.12:o.rim,p:2.2})));
  const shimmer=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8c0d0,
    transparent:true,opacity:0.12,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  shimmer.scale.set(1.1,1.1,1); shimmer.position.set(0,0.45,0); shimmer.renderOrder=4; g.add(shimmer);
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    shimmer.material.opacity=kk*0.12*(0.55+0.45*Math.abs(Math.sin(t*0.7)));
  };
  return {g:g,update:g.userData.update};
}

/* —— 铁衣架 makeTiejiaJS(o)：木架一领铁甲（甲身+护肩+盔缨）+「雪色」寒光
   glint 初值=峰值（点击增幅合规），update 第四参 raise 提亮 */
function makeTiejiaJS(o){
  o=o||{};
  const B=new GeoBag();
  const post=new THREE.CylinderGeometry(0.07,0.10,1.95,6); post.translate(0,0.97,0); B.put(post,0x2e2114);
  for(let s2=0;s2<3;s2++){
    const a=s2/3*6.283+0.5;
    const lg=new THREE.CylinderGeometry(0.045,0.06,0.62,5);
    lg.rotateX(Math.cos(a)*0.5); lg.rotateZ(Math.sin(a)*0.5);
    lg.translate(Math.sin(a)*0.28,0.26,Math.cos(a)*0.28); B.put(lg,0x241a0e);
  }
  const jia=new THREE.CylinderGeometry(0.52,0.34,1.05,10); jia.translate(0,1.62,0); B.put(jia,0x3c4048);
  const yao=new THREE.CylinderGeometry(0.30,0.38,0.55,9); yao.translate(0,1.02,0); B.put(yao,0x33373e);
  for(let sd=0;sd<2;sd++){
    const sh=new THREE.SphereGeometry(0.20,7,6); sh.scale(1.1,0.62,1);
    sh.translate(sd?0.56:-0.56,2.08,0); B.put(sh,0x41454d);
  }
  const kz=new THREE.SphereGeometry(0.24,8,6,0,Math.PI*2,0,Math.PI/2);
  kz.scale(1.05,0.85,1.05); kz.translate(0,2.30,0); B.put(kz,0x4a4e56);
  const ying=new THREE.ConeGeometry(0.05,0.30,5); ying.translate(0,2.68,0); B.put(ying,0x7a2e1e);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:42,
    specular:0x9aa4b0,emissive:0x0a0c10}),{c:0xa8905f,i:o.rim===undefined?0.20:o.rim,p:2.6})));
  const glintOp=o.glintOp===undefined?0.34:o.glintOp;      // 峰值
  const glint=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xdde6f0,
    transparent:true,opacity:glintOp,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glint.scale.set(2.4,3.0,1); glint.position.set(0,1.85,0.30); glint.renderOrder=4; g.add(glint);
  g.userData.update=function(t,k,raise){
    const kk=k===undefined?1:k, r=raise===undefined?0:raise;
    glint.material.opacity=kk*glintOp*(0.44+0.14*Math.sin(t*1.7)+0.42*r);
  };
  return {g:g,update:g.userData.update};
}

/* —— 宝剑架 makeBaojianJS(o)：横架宝剑（刃+格+柄+首）+「星文」光点两簇 */
function makeBaojianJS(o){
  o=o||{};
  const B=new GeoBag();
  const post1=new THREE.CylinderGeometry(0.05,0.07,0.92,6); post1.translate(-0.62,0.46,0); B.put(post1,0x2a1e12);
  const post2=new THREE.CylinderGeometry(0.05,0.07,0.92,6); post2.translate(0.62,0.46,0); B.put(post2,0x2a1e12);
  const bar=new THREE.CylinderGeometry(0.04,0.04,1.42,6);
  bar.rotateZ(Math.PI/2); bar.translate(0,0.88,0); B.put(bar,0x332413);
  const bl=new THREE.BoxGeometry(1.15,0.045,0.13); bl.translate(-0.28,1.02,0); B.put(bl,0x7a828e);
  const tip=new THREE.ConeGeometry(0.075,0.22,4);
  tip.rotateZ(Math.PI/2); tip.scale(1,1,0.5); tip.translate(-0.95,1.02,0); B.put(tip,0x7a828e);
  const gd=new THREE.BoxGeometry(0.10,0.05,0.22); gd.translate(0.32,1.02,0); B.put(gd,0x8a6a3a);
  const hl=new THREE.CylinderGeometry(0.032,0.032,0.30,6);
  hl.rotateZ(Math.PI/2); hl.translate(0.50,1.02,0); B.put(hl,0x4a3418);
  const pm=new THREE.SphereGeometry(0.055,7,6); pm.translate(0.68,1.02,0); B.put(pm,0x8a6a3a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:46,
    specular:0xaab2be,emissive:0x0a0c10}),{c:0xa8905f,i:o.rim===undefined?0.18:o.rim,p:2.6})));
  const starOp=o.starOp===undefined?0.30:o.starOp;         // 峰值
  const stars=[];
  [[-0.6,1.10,0.10],[-0.05,0.98,0.10]].forEach(function(p,i){
    const st=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfdce8,
      transparent:true,opacity:starOp,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    st.scale.set(0.5,0.5,1); st.position.set(p[0],p[1],p[2]); st.renderOrder=4;
    g.add(st); stars.push(st);
  });
  g.userData.update=function(t,k,raise){
    const kk=k===undefined?1:k, r=raise===undefined?0:raise;
    for(let i=0;i<stars.length;i++){
      stars[i].material.opacity=kk*starOp*(0.46+0.24*Math.sin(t*2.2+i*2.1)+0.30*r);
    }
  };
  return {g:g,update:g.userData.update};
}

/* —— 老将三态（贯穿造型系，每次 build 新建材质）——英姿/落魄（立·坐）/披甲 */
function ljYing(scale){
  return makeFigure({pose:'指月',robe:0x4a3423,belt:0x8a6238,skin:0xd9b189,collar:0xc8a878,
    hair:0x14100a,hat:'幞头',rimC:0xa8905f,rim:0.50,noProp:true,scale:scale===undefined?1.40:scale});
}
function ljLuo(scale){
  return makeFigure({pose:'独立',robe:0x3a3630,belt:0x5a5248,skin:0xd9b189,collar:0x7a7264,
    hair:0x8a8478,hat:'发髻',beard:true,rimC:0xa8905f,rim:0.28,noProp:true,scale:scale===undefined?1.40:scale});
}
function ljZuo(scale){
  return makeFigure({pose:'坐饮',robe:0x3a3630,belt:0x5a5248,skin:0xd9b189,collar:0x7a7264,
    hair:0x8a8478,hat:'发髻',beard:true,rimC:0xa8905f,rim:0.28,noProp:true,scale:scale===undefined?1.32:scale});
}
function ljPi(scale){
  return makeFigure({pose:'按剑',robe:0x2e3038,belt:0x4a4e58,skin:0xd9b189,collar:0x6a7484,
    hair:0x14100a,hat:'幞头',rimC:0xa8905f,rim:0.55,noProp:true,scale:scale===undefined?1.42:scale});
}
function figMats(fig){
  const set=[];
  fig.traverse(function(o){ if(o.material&&set.indexOf(o.material)<0)set.push(o.material); });
  return set;
}

function bCover(){ // 卷首 · 暮色古道：大漠尽头的古道车辙，老将牵瘦马独立，一杆旧旗歪斜，远山环合
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0d0906,c2:0x1a120a,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const yuan=makeRange({r:250,h:15,layers:2,peaks:5,seed:26601,color:0x140d07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xa8905f,y:-8,order:-6});
  yuan.g.position.set(0,0,-180); g.add(yuan.g);
  const dun=makeRange({r:150,h:7,layers:1,peaks:7,seed:26602,color:0x1a1209,atmo:0x2e2114,
    fogK:0.60,glowK:0.04,glow:0x8a744c,y:-4,order:-5});
  dun.g.position.set(-20,0,-92); g.add(dun.g);
  const qi=makeJingqiJS({H:6.4,W:2.4,Hh:1.8,tilt:0.50,seed:26603,rim:0.12});
  qi.g.position.set(-6.5,0,-20); qi.g.rotation.y=0.3; g.add(qi.g);
  const ma=makeHanmaLJ({pose:'stand',coat:0x241c12,rim:0.10,seed:26604,scale:1.10});
  ma.g.position.set(4.6,0,-16.5); ma.g.rotation.y=-0.9; g.add(ma.g);
  const lj=ljLuo(1.42); lj.position.set(2.4,0,-15.0); lj.rotation.y=-0.55; g.add(lj);
  const mist=makeMist({n:5,spread:[130,10,56],pos:[0,3.2,-16],scale:44,color:0x2e2114,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[90,14,44],pos:[0,8,0],color:0x8a744c,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x080503,seed:26605,rim:0.10,rimC:0xa8905f});
  fg1.g.position.set(-13,-1.6,21); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26606,sway:0.6,rim:0.08,rimC:0xa8905f});
  fg2.g.position.set(13.5,-1.8,20); g.add(fg2.g);
  addLights(g,{c:0xa8905f,i:0.28,p:[-40,55,-40]},{c:0x2a1e12,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); yuan.update(t,0); dun.update(t,0);
    qi.update(t,k); ma.update(t,k); lj.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bShaonian(){ // 壹 · 少年战功 —— 步行夺得胡马骑……虏骑崩腾畏蒺藜：
                      // 晨光大漠演武场：少年将军徒步降服一匹人立而起的黑胡马，蒺藜撒地，军阵旌旗烽燧
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x120d07,c2:0x221608,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const shan=makeRange({r:250,h:17,layers:2,peaks:5,seed:26607,color:0x150e07,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xa8905f,y:-9,order:-6});
  shan.g.position.set(0,0,-155); g.add(shan.g);
  const dun=makeRange({r:130,h:6,layers:1,peaks:6,seed:26608,color:0x1a1209,atmo:0x2e2114,
    fogK:0.58,glowK:0.04,glow:0x8a744c,y:-4,order:-5});
  dun.g.position.set(-26,0,-72); g.add(dun.g);
  const lie=makeCrowd({n:12,rect:[-26,-46,34,16],color:0x1c150e,rimC:0xa8905f,rim:0.14,
    sMin:0.7,sMax:1.0,seed:26609});
  g.add(lie.mesh);
  const q1=makeJingqiJS({H:7.2,W:2.7,Hh:2.0,seed:26610});
  q1.g.position.set(-10.5,0,-24); q1.g.rotation.y=0.5; g.add(q1.g);
  const q2=makeJingqiJS({H:6.6,W:2.5,Hh:1.9,seed:26611,rim:0.14});
  q2.g.position.set(9.5,0,-28); q2.g.rotation.y=-0.6; g.add(q2.g);
  const dt=makeDunTaiJS({scale:1.35,seed:26612});
  dt.g.position.set(18,0,-44); g.add(dt.g);
  const ma=makeHanmaLJ({pose:'rear',coat:0x241a10,seed:26613,scale:1.05});
  ma.g.position.set(2.0,0,-5.6); ma.g.rotation.y=-0.9; g.add(ma.g);
  const ying=ljYing(1.40); ying.position.set(0.6,0,-3.0); ying.rotation.y=-1.05; g.add(ying);
  const rein=new THREE.Mesh(limbGeo([1.75,4.9,-1.6],[3.4,6.2,-2.6],0.035,0.018,4),
    new THREE.MeshPhongMaterial({color:0x2a1c10,shininess:4}));
  g.add(rein);
  const ci=makeCizhenJS({n:8,w:10,d:5,seed:26614});
  ci.position.set(-1.5,0,-1.0); g.add(ci);
  const mist=makeMist({n:5,spread:[140,10,58],pos:[0,3.2,-16],scale:46,color:0x2e2114,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[96,13,44],pos:[0,8,2],color:0xa8905f,size:3.4,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x080503,seed:26615,rim:0.10,rimC:0xa8905f});
  fg1.g.position.set(-12,-1.6,18); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26616,sway:0.5,rim:0.08,rimC:0xa8905f});
  fg2.g.position.set(11,-1.7,17); g.add(fg2.g);
  addLights(g,{c:0xc89050,i:0.34,p:[38,48,-30]},{c:0x2c2012,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); shan.update(t,0); dun.update(t,0);
    lie.update(t);
    q1.update(t,k); q2.update(t,k); dt.update(t,k);
    ma.update(t,k); ying.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bTianxing(){ // 贰 · 天幸数奇 —— 卫青不败由天幸……世事蹉跎成白首：
                      // 冷月荒原两重对照：远处封侯将坛灯火上明（天幸），近处老将白发坐断戟旁篝火将熄
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0d0a07,c2:0x171208,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,18);
  const shan=makeRange({r:270,h:26,layers:3,peaks:7,seed:26617,color:0x110c07,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0x8a744c,y:-11,order:-6});
  shan.g.position.set(0,0,-140); g.add(shan.g);
  const zui=makeRange({arc:1.0,a0:0.5,r:95,h:10,layers:2,peaks:5,seed:26618,color:0x150f08,
    atmo:0x2e2114,fogK:0.58,glowK:0.04,glow:0x8a744c,y:-5,order:-5});
  zui.g.position.set(14,0,-64); g.add(zui.g);
  const tan=makeJiangtanJS({seed:26619});
  tan.g.position.set(15,0,-40); g.add(tan.g);
  const luo=ljZuo(1.30); luo.position.set(-3.4,0,-8.6); luo.rotation.y=0.65; g.add(luo);
  const dj=makeDuanJiJS({tilt:0.42,ry:0.8,seed:26620});
  dj.position.set(-5.4,0,-9.8); g.add(dj);
  const huo=makeFlame({h:0.5,w:0.22,core:0xffd898,outer:0xb05018,embers:8,light:0.5,
    lightC:0xff9a40,lightD:16,spark:false});
  huo.g.position.set(-1.6,0.1,-6.8); g.add(huo.g);
  const chai=new THREE.Mesh(limbGeo([-2.1,0.06,-6.4],[-1.3,0.10,-7.1],0.05,0.03,4),
    new THREE.MeshPhongMaterial({color:0x1c130a,shininess:4}));
  g.add(chai);
  const qi=makeJingqiJS({H:6.8,W:2.5,Hh:1.9,tilt:0.55,seed:26621,rim:0.12});
  qi.g.position.set(-9.0,0,-14.5); qi.g.rotation.y=0.4; g.add(qi.g);
  const mist=makeMist({n:6,spread:[150,11,60],pos:[0,4.0,-18],scale:46,color:0x3a342c,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[100,14,46],pos:[0,9,-4],color:0x8a7a58,size:3.2,speed:0.03,rise:0,add:false,maxA:0.06});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x070403,seed:26622,rim:0.10,rimC:0xa8905f});
  fg1.g.position.set(-13,-1.8,21); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x070403,seed:26623,rim:0.09,rimC:0xa8905f});
  fg2.g.position.set(12,-1.4,19); g.add(fg2.g);
  addLights(g,{c:0xa8905f,i:0.24,p:[-36,52,-36]},{c:0x241a0e,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); shan.update(t,0); zui.update(t,0);
    tan.update(t,k);
    luo.update(t,k);
    huo.update(t,k);
    qi.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bQiongxiang(){ // 叁 · 古木穷巷 —— 昔时飞箭无全目……不似颍川空使酒：
                        // 黄昏穷巷：古木参天篱笆柴门，瓜摊柳影，白首老将守着一摊故侯瓜，巷尾古井微光
  const g=new THREE.Group();
  const grd=makeGround({r:120,c1:0x0e0a06,c2:0x1a1209,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const shan=makeRange({r:250,h:14,layers:2,peaks:5,seed:26624,color:0x140d07,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xa8905f,y:-8,order:-6});
  shan.g.position.set(0,0,-170); g.add(shan.g);
  const hans=makeRange({arc:1.0,a0:0.6,r:110,h:13,layers:2,peaks:6,seed:26625,color:0x150f0a,
    atmo:0x2e2114,fogK:0.60,glowK:0.04,glow:0x8a744c,y:-5,order:-5});
  hans.g.position.set(6,0,-58); g.add(hans.g);
  const gm1=makeGumuJS({type:'木',h:9.5,seed:26626});
  gm1.g.position.set(-11.5,0,-19); g.add(gm1.g);
  const gm2=makeGumuJS({type:'木',h:7.0,seed:26627});
  gm2.g.position.set(13.5,0,-24); gm2.g.rotation.y=1.2; g.add(gm2.g);
  const liu1=makeGumuJS({type:'柳',h:6.2,seed:26628});
  liu1.g.position.set(7.2,0,-9.5); g.add(liu1.g);
  const liu2=makeGumuJS({type:'柳',h:5.2,seed:26629});
  liu2.g.position.set(10.4,0,-13.5); liu2.g.rotation.y=-1.0; g.add(liu2.g);
  const lb1=makeLibaJS({w:16,seed:26630});
  lb1.position.set(6.5,0,-6.0); lb1.rotation.y=-0.12; g.add(lb1);
  const lb2=makeLibaJS({w:10,seed:26631});
  lb2.position.set(12.8,0,-13.0); lb2.rotation.y=Math.PI/2-0.1; g.add(lb2);
  const wu=makeTuWuJS({seed:26632});
  wu.position.set(9.0,0,-19.5); wu.rotation.y=0.10; g.add(wu);
  const tan=makeGuaTanJS({n:5,seed:26633});
  tan.position.set(-4.6,0,-7.2); tan.rotation.y=0.35; g.add(tan);
  const luo=ljLuo(1.40); luo.position.set(-2.9,0,-9.6); luo.rotation.y=0.30; g.add(luo);
  const jar=makeJar(1.15);
  jar.position.set(-0.6,0,-6.0); jar.rotation.z=0.30; g.add(jar);
  const jing=makeGujingJS({seed:26634});
  jing.g.position.set(-9.5,0,-13.5); jing.g.rotation.y=0.5; g.add(jing.g);
  const smoke=makeGlow({n:9,box:[0.7,6,0.7],pos:[9.6,6.5,-20.5],color:0x8a8478,size:2.2,
    speed:0.035,rise:1,add:false,maxA:0.09});
  smoke.points.renderOrder=3; g.add(smoke.points);
  const mist=makeMist({n:5,spread:[130,10,54],pos:[0,3.4,-13],scale:44,color:0x33241a,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[92,13,44],pos:[0,7,2],color:0xa8905f,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x080503,seed:26635,rim:0.10,rimC:0xa8905f});
  fg1.g.position.set(11,-1.5,16); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26636,sway:0.5,rim:0.08,rimC:0xa8905f});
  fg2.g.position.set(-12,-1.7,15); g.add(fg2.g);
  addLights(g,{c:0xb0905c,i:0.28,p:[-30,46,-30]},{c:0x2a1e12,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); shan.update(t,0); hans.update(t,0);
    gm1.update(t,k); gm2.update(t,k); liu1.update(t,k); liu2.update(t,k);
    jing.update(t,k);
    luo.update(t,k);
    smoke.update(t);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bYoukan(){ // 肆（末境·可点击）· 犹堪一战 —— 贺兰山下阵如云……犹堪一战取功名：
                    // 贺兰山夜：军阵如云旌旗列、募火两盆，老将立于铁衣架宝剑架之间，旧旗歪斜。
                    // 点击：老将披甲再起（两态交叠）+旧部云集（暗群亮起前涌）+旌旗重振（旧旗立直猎猎）+题字
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:130,c1:0x0d0906,c2:0x1a1209,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,16);
  const helan=makeRange({r:280,h:34,layers:3,peaks:8,seed:26637,color:0x110c07,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xa8905f,y:-12,order:-6});
  helan.g.position.set(0,0,-125); g.add(helan.g);
  const qian=makeRange({arc:1.0,a0:0.5,r:120,h:13,layers:2,peaks:6,seed:26638,color:0x150f08,
    atmo:0x2e2114,fogK:0.58,glowK:0.04,glow:0x8a744c,y:-6,order:-5});
  qian.g.position.set(-14,0,-62); g.add(qian.g);
  const zhen=makeCrowd({n:24,rect:[-40,-54,64,20],color:0x1c150e,rimC:0xa8905f,rim:0.14,
    sMin:0.75,sMax:1.05,seed:26639});
  g.add(zhen.mesh);
  const qizhi=[];
  [[-16,-34,0.4],[-6,-40,-0.3],[5,-36,0.5],[14,-42,-0.5]].forEach(function(p,i){
    const q=makeJingqiJS({H:7.4,W:2.7,Hh:2.0,seed:26640+i,amp:0.34});
    q.g.position.set(p[0],0,p[1]); q.g.rotation.y=p[2]; g.add(q.g); qizhi.push(q);
  });
  const dt=makeDunTaiJS({scale:1.3,seed:26644,light:0.7});
  dt.g.position.set(-22,0,-52); g.add(dt.g);
  const br1=makeBrazier({r:0.75,fh:1.4,fw:0.7,light:0.85,lightD:22,embers:10,spark:false});
  br1.g.position.set(-7.5,0,-8.0); g.add(br1.g);
  const br2=makeBrazier({r:0.70,fh:1.3,fw:0.65,light:0.80,lightD:22,embers:10,spark:false});
  br2.g.position.set(8.0,0,-9.5); g.add(br2.g);
  const tj=makeTiejiaJS({seed:26645});
  tj.g.position.set(3.4,0,-8.6); tj.g.rotation.y=-0.35; g.add(tj.g);
  const bj=makeBaojianJS({seed:26646});
  bj.g.position.set(-2.2,0,-6.8); bj.g.rotation.y=0.40; g.add(bj.g);
  const luo=ljLuo(1.42); luo.position.set(0.6,0,-6.2); luo.rotation.y=-0.25; g.add(luo);
  const pi=ljPi(1.44); pi.position.set(0.6,0,-6.2); pi.rotation.y=-0.25;
  pi.visible=false; g.add(pi);
  const luoM=figMats(luo), piM=figMats(pi);
  const qi0=makeJingqiJS({H:7.8,W:3.0,Hh:2.2,tilt:0.42,seed:26647,color:0x6a4a2a,amp:0.22});
  qi0.g.position.set(-4.6,0,-11.5); qi0.g.rotation.y=0.55; g.add(qi0.g);
  /* 标志性交互：旧部云集（点击前幻影组 visible=false 硬关） */
  const jiubu=makeCrowd({n:12,rect:[-13,-20,17,7],color:0x2a2014,rimC:0xa8905f,rim:0.20,
    sMin:0.85,sMax:1.08,seed:26648});
  jiubu.mesh.visible=false; jiubu.mesh.position.set(0,0,-17); g.add(jiubu.mesh);
  const jiubuM=jiubu.mesh.material;
  const shuoqi=makeMist({n:6,spread:[150,11,60],pos:[0,4.0,-16],scale:46,color:0x3a2c1a,op:0.10});
  g.add(shuoqi.g);
  const motes=makeGlow({n:24,box:[100,14,46],pos:[0,8,-2],color:0xa8905f,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x080503,seed:26649,rim:0.10,rimC:0xa8905f});
  fg1.g.position.set(-12,-1.6,18); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x080503,seed:26650,sway:0.5,rim:0.08,rimC:0xa8905f});
  fg2.g.position.set(11.5,-1.8,17.5); g.add(fg2.g);
  addLights(g,{c:0xb08a50,i:0.28,p:[-32,48,-30]},{c:0x2a1e12,i:0.52});
  const api={group:g,update(t,dt2){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt2;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt2/6.0);
      const e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      const os=0.5+0.5*Math.sin(t*1.15);
      if(ctl.reveal>0){
        pi.visible=e>0.01;
        for(let i=0;i<luoM.length;i++)luoM[i].opacity=k*(1-0.62*os*e);
        for(let i=0;i<piM.length;i++)piM[i].opacity=k*(0.30+0.62*os)*e;
      }
      luo.update(t,k); if(pi.visible)pi.update(t,k);
      tj.update(t,k,e); bj.update(t,k,e);
      jiubu.mesh.visible=e>0.01;
      if(ctl.reveal>0){
        jiubu.mesh.position.set(0,0,-17+5.5*e);
        jiubuM.opacity=k*(0.30+0.40*os)*e;
      }
      const tiltNow=qi0.tilt0*(1-e)+0.02*Math.sin(t*1.4)*k;
      qi0.g.rotation.z=tiltNow;
      qi0.wm=1+1.6*e;
      for(let i=0;i<qizhi.length;i++)qizhi[i].update(t,k);
      qi0.update(t,k);
      dt.update(t,k);
      br1.update(t,k); br2.update(t,k);
      shuoqi.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); helan.update(t,0); qian.update(t,0);
      zhen.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.12);
        pluck(5,0.05,0.12); pluck(2,0.90,0.10); pluck(0,1.80,0.09);
        const fl=$('#flash'); fl.textContent='莫嫌旧日云中守 犹堪一战取功名';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x140f09),hor:C(0x30220f),bot:C(0x0b0806),fog:C(0x190f08),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-70,28,-190),ms:0.30,mph:0.46,mhaze:0.20,dirC:C(0xa8905f),dirI:0.32,
  dirP:new THREE.Vector3(-48,50,-26),ambC:C(0x2b1f13),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.2,42],t:[0,7.8,34],lf:[2,7,-20],lt:[3,7.5,-32]},
  sky:()=>SK({fd:0.0048,star:0.12,hor:C(0x3c2a12),ms:0.32,mph:0.42,mhaze:0.24}) },
{ name:'少年战功',dwell:26,river:0.02,build:bShaonian,
  cam:{f:[3.6,3.4,9.5],t:[1.6,3.0,-1.5],lf:[1.5,3.2,-6],lt:[3.2,3.4,-14]},
  sky:()=>SK({top:C(0x1a1209),hor:C(0x4a3416),bot:C(0x0d0905),fog:C(0x1c130a),fd:0.0052,star:0.04,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.10,
    dirC:C(0xc89050),dirI:0.34,dirP:new THREE.Vector3(38,48,-30),
    ambC:C(0x2c2012),ambI:0.56}) },
{ name:'天幸数奇',dwell:20,river:0.02,build:bTianxing,
  cam:{f:[-1.2,3.8,9.0],t:[-2.8,2.9,-2.5],lf:[-1,3.4,-8],lt:[-3.5,3.2,-16]},
  sky:()=>SK({top:C(0x0d0b08),hor:C(0x2a2214),bot:C(0x0a0806),fog:C(0x16100a),fd:0.0058,star:0.50,
    moon:new THREE.Vector3(46,38,-190),ms:0.26,mph:0.55,mhaze:0.22,
    dirC:C(0xa8905f),dirI:0.24,dirP:new THREE.Vector3(-36,52,-36),
    ambC:C(0x241a0e),ambI:0.50}) },
{ name:'古木穷巷',dwell:30,river:0.02,build:bQiongxiang,
  cam:{f:[1.2,4.0,10.5],t:[-1.2,2.7,-3.0],lf:[0.5,3.6,-7],lt:[-2.5,3.3,-15]},
  sky:()=>SK({top:C(0x171009),hor:C(0x40301a),bot:C(0x0d0905),fog:C(0x1a1209),fd:0.0054,star:0.06,
    moon:new THREE.Vector3(-60,24,-180),ms:0.20,mph:0.44,mhaze:0.20,
    dirC:C(0xb0905c),dirI:0.28,dirP:new THREE.Vector3(-30,46,-30),
    ambC:C(0x2a1e12),ambI:0.54}) },
{ name:'犹堪一战',dwell:30,river:0.02,build:bYoukan,
  cam:{f:[2.6,4.0,11.5],t:[0.6,3.0,-3.0],lf:[1,3.6,-8],lt:[-0.5,3.4,-18]},
  sky:()=>SK({top:C(0x0d0a06),hor:C(0x2c1e10),bot:C(0x0a0705),fog:C(0x16100a),fd:0.0056,star:0.45,
    moon:new THREE.Vector3(52,40,-188),ms:0.26,mph:0.50,mhaze:0.18,
    dirC:C(0xa8804e),dirI:0.26,dirP:new THREE.Vector3(-40,50,-24),
    ambC:C(0x241a0e),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('laojiang.py —— 被 build.py 消费：python build.py laojiang')
