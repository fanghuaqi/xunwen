# -*- coding: utf-8 -*-
"""tiaotiao-qianniu.py —— 《迢迢牵牛星》（汉·古诗十九首，queue no.259，水墨夜思）生成配置
四境（N=queue stages 数）：迢迢皎皎（迢迢牵牛星·皎皎河汉女·纤纤擢素手·札札弄机杼——
双星隔河+织女弄机杼）、泣涕零雨（终日不成章·泣涕零如雨——素练无章+光雨）、
河汉清浅（河汉清且浅·相去复几许——清浅星水+对岸牵牛剪影）、
盈盈脉脉（盈盈一水间·脉脉不得语——标志性瞬间，末境点击：点击河汉——鹊影横波星光相望）。
水墨夜思全套色板：底色 #0d1117、雾 #131a26 系、文字 #dfe6f0，accent=#b8c4dd
（queue 分配强调色，月银微紫）只落在双星晕/梭光/织线光/星子落波/星光连线/鹊影边缘光/UI 上，
全页近零饱和；素练的素白与泪光微青是全页唯二亮部。
全诗立意「星河为界的两岸+织女机杼」：低垂的银河化作一条清浅的星水横在画面中部，
两岸墨色岸渚，左岸织女机杼（札札弄机杼——唯一「人间」道具，贯穿四境的母题），
牵牛织女双星低垂对望（两岸光点，含蓄不具面容）。与已有水墨夜思页第一眼可区分：
不做夜台一瑟（jinse）、不做满月江楼水天一色（jianglou-ganjiu）、
不做云海星河带+云崖+鹊群搭桥（queqiaoxian-xianyun——七夕相逢的「成」）；
本页写的是「不成」——机杼札札而终日不成章，一水盈盈而脉脉不得语，星河是界不是桥。
标志性瞬间（境肆·queue moment：盈盈一水间脉脉不得语——咫尺天涯）：
两岸双星与两岸人影隔着一条又清又浅的星水相对，水面星子落波，谁也过不去。
末境点击（queue interact：点击河汉——鹊影横波星光相望）：点击画面——
①两岸星光连线：一道含蓄的星光细线自织女星弧牵到牵牛星（连线光点次第亮起，不画具体鹊桥）；
②鹊影横波：六点鹊影贴着水面自左岸掠向右岸，翅膀明灭（剪影含蓄）；
③双星光晕徐涨、星子落波转盛；④「盈盈一水间 脉脉不得语」题字同现。
考点钉子：擢 zhuó／札札 zhá／脉脉 mò／间 jiàn（tts.json 钉同音替换，小测第 3 题落点）；
《古诗十九首》「五言之冠冕」+十句六叠词（迢迢/皎皎/纤纤/札札/盈盈/脉脉）（第 4 题）；
「盈盈一水间，脉脉不得语」的咫尺天涯主旨（第 5 题）。
多音字：擢→卓（zhuó）、札札→闸闸（zhá）、脉脉→莫莫（mò）、一水间→一水见（jiàn）（tts.json）。"""

META = dict(
    N=4, slug='tiaotiao-qianniu', title='迢迢牵牛星', dyn='汉 · 古诗十九首',
    brand_author='古 诗 十 九 首',
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
    tip='轻点画面 / 按空格 —— 鹊影横波，星光相望',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看鹊影横波掠过星水，两岸星光相望',
    cover_read='迢迢牵牛星。汉，古诗十九首。迢迢牵牛星，皎皎河汉女。纤纤擢素手，札札弄机杼。终日不成章，泣涕零如雨。河汉清且浅，相去复几许。盈盈一水间，脉脉不得语。',
    cover_p1='四重意境，随诗句次第展开：遥远的牵牛星隔着银河，与皎皎的织女星遥遥相望；织女伸出纤纤素手，札札地摆弄着机杼，却终日织不成一段布章，泪落如雨——银河之水又清又浅，两人相隔并没有多远，只隔着盈盈一水，脉脉凝望而不能互诉衷肠。',
    cover_p2='边读诗，边走到银河两岸：读懂「盈盈一水间，脉脉不得语」的咫尺天涯，就读懂了这首《古诗十九首》里最温柔的离歌。',
    end_h2='星河 · 相望', cn_word='四',
    words_js="['再渡一次星河','初识古诗十九首，尚需共读','渐入诗境，再诵几遍','机杼声声，星光渐明','已解盈盈一水之意','脉脉相望，无语成诗']",
    sky_atmo='0x1f2a3c',
)

POEM_JS = """const POEM = [
{ name:'迢迢皎皎', jing:'遥远的牵牛星，隔着银河与皎皎的织女星遥遥相望；织女伸出纤纤素手，札札地摆弄着机杼 —— 迢迢、皎皎、纤纤、札札。（双星 · 银汉 · 机杼）',
  segs:[
   {c:'迢迢牵牛星，', p:py('tiáo tiáo qiān niú xīng')},
   {c:'皎皎河汉女。', p:py('jiǎo jiǎo hé hàn nǚ')},
   {c:'纤纤擢素手，', p:py('xiān xiān zhuó sù shǒu')},
   {c:'札札弄机杼。', p:py('zhá zhá nòng jī zhù')}],
  read:'迢迢牵牛星，皎皎河汉女。纤纤擢素手，札札弄机杼。',
  yisi:'遥远的牵牛星，隔着银河，与明亮皎洁的织女星遥遥相望。织女伸出细长柔白的素手，札札地穿引着织机，摆弄着机杼。——开头四句全用叠词起笔：「迢迢」写牵牛之远，「皎皎」写织女之亮——先立起两岸的距离与光亮；「纤纤」写素手之柔，「札札」写机声之碎——镜头随即落到织女身上：星光下，只有她在劳作。四组叠词由远而近、由天及人，音韵轻软绵密，像叹息一样铺开全诗。',
  zhu:[['迢迢牵牛星','牵牛星：隔银河与织女星相对的亮星（河鼓二）；迢迢，遥远的样子'],['河汉女','指织女星——河汉，即银河；织女在银河之一侧，与牵牛隔河相对。女，读 nǚ'],['纤纤','细长柔美的样子，形容素手'],['擢','读 zhuó，伸出、抽出的样子——写素手在机杼间穿引的动作'],['素手','白皙的手。素，白色'],['札札','织机声，象声词。札，读 zhá'],['机杼','织机的部件：杼是织布的梭子，用以引纬线；机杼泛指织机。杼，读 zhù']] },
{ name:'泣涕零雨', jing:'她整日织啊织，却织不成一段布章；泪水簌簌落下，像下雨一样 —— 不成章、泣涕、零如雨。（素练 · 光雨）（光雨如泪，簌簌而落）',
  segs:[
   {c:'终日不成章，', p:py('zhōng rì bù chéng zhāng')},
   {c:'泣涕零如雨。', p:py('qì tì líng rú yǔ')}],
  read:'终日不成章，泣涕零如雨。',
  yisi:'她整天织啊织，却织不成布帛上的经纬纹理；无声的眼泪簌簌落下，像下雨一样。——「终日不成章」是全诗最含蓄的一笔：机杼札札、素手不停，布却总织不成——不是手笨，是心不在：思念的人隔着一道银河，织出来的每一梭都成了乱的。「章」字语出《诗经》「跂彼织女，终日七襄；虽则七襄，不成报章」，原就带着「劳而无成」的怅惘。后半句忽然点破：泪水零落如雨——原来札札机声里，全是泣涕的声音。',
  zhu:[['终日不成章','整天织不出布帛的纹理。章，指布帛上的经纬纹理——心不在织，故「不成章」；语本《诗经·小雅·大东》「跂彼织女，终日七襄。虽则七襄，不成报章」'],['泣涕','无声哭泣时流下的眼泪。泣，无声流泪或低声哭；涕，眼泪'],['零如雨','零，落下——泪水落下像下雨一样']] },
{ name:'河汉清浅', jing:'银河之水又清又浅，两人相隔，又能有多远呢 —— 清且浅、相去、复几许。（清浅星水 · 对岸牵牛）（对岸人影与低垂的星）',
  segs:[
   {c:'河汉清且浅，', p:py('hé hàn qīng qiě qiǎn')},
   {c:'相去复几许。', p:py('xiāng qù fù jǐ xǔ')}],
  read:'河汉清且浅，相去复几许。',
  yisi:'银河之水又清澈又浅平，两人相隔，又能有多远呢？——镜头从织女身上移开，落到那道隔开他们的水上：水是清的，浅得看得见底；对岸的牵牛就在那里，影子那么近。——这一问最是揪心：不是天堑，只是一水；不是不能相望，只是不得相聚。障碍越「轻」，悲哀越「重」——因为阻隔他们的从来不是水的深浅，而是那道不可逾越的天规。',
  zhu:[['河汉清且浅','银河之水既清澈又浅平——并非深不可渡，为下文蓄势'],['相去','相隔、相距'],['复几许','又能有多远呢。几许，多少、几何——反问语气，言其近；近在眼前而不可即，愈见其悲']] },
{ name:'盈盈脉脉', jing:'只隔着盈盈一条浅浅的水，却只能含情凝望，而不能互诉衷肠 —— 盈盈、脉脉、不得语。（一水 · 相望 · 不得语）（标志性瞬间）（末境点击画面：鹊影横波，星光相望）',
  segs:[
   {c:'盈盈一水间，', p:py('yíng yíng yī shuǐ jiàn')},
   {c:'脉脉不得语。', p:py('mò mò bù dé yǔ')}],
  read:'盈盈一水间，脉脉不得语。',
  yisi:'只隔着清浅盈盈的一条水，两人含情相望，却一句话也说不得。——「盈盈」写水之清浅，「脉脉」写相视之含情；水越清浅，越显得这一水之隔毫无道理；相望越深情，越显得「不得语」之残忍。距离咫尺，却如天涯——把全诗的悲哀凝成最静的一瞬：没有呼喊，没有动作，只有隔水的凝望。六组叠词在这里收束成一幅无声的画，成为千古写「咫尺天涯」的绝唱。',
  zhu:[['盈盈','水清浅的样子；一说形容仪态美好——此处兼写水与隔水相望之人'],['一水间','只隔一条浅浅的银河。间，间隔，读 jiàn'],['脉脉','相视而含情不语的样子。脉，读 mò'],['咫尺天涯','距离虽近，却如同远在天边——「盈盈一水间，脉脉不得语」正是咫尺天涯的千古写照']] }];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「迢迢牵牛星」的下一句是？', o:['皎皎河汉女','纤纤擢素手','盈盈一水间'], a:0},
 {q:'「河汉清且浅」的下一句是？', o:['脉脉不得语','相去复几许','泣涕零如雨'], a:1},
 {q:'「纤纤擢素手」的「擢」，读音和意思都正确的一项是？', o:['读 zhuó，伸出、抽出的样子——写织女伸出纤纤素手，在机杼间穿引拨弄','读 yào，同「耀」，闪耀——写织女的素手在星光下闪闪发亮','读 dí，拾取、捡起——写织女俯身拾起散落的织线'], a:0},
 {q:'关于《古诗十九首》与这首诗，下列说法正确的是？', o:['《古诗十九首》是东汉文人五言诗的代表作，刘勰誉为「五言之冠冕」；此诗借天上牵牛织女双星写人间离情，十句之中六用叠词——迢迢、皎皎、纤纤、札札、盈盈、脉脉','《迢迢牵牛星》选自《诗经·小雅》，是最早记录七夕乞巧习俗的篇章','此诗是南朝乐府民歌，写的是元宵灯节青年男女观灯相会的热闹'], a:0},
 {q:'「盈盈一水间，脉脉不得语」历来为人称道。对它的理解，最恰当的一项是？', o:['银河水面宽阔、波涛汹涌，两人被天险阻隔无法渡河，重在写自然之险','银河之水又清又浅、相隔并不遥远，却只能含情凝望而不能互诉衷肠——咫尺天涯，把离人的悲哀写到极处','织女终日织布无暇开口，写的是劳动的辛苦与忙碌'], a:1},
];
"""

SCENES_JS = """/* ================= 迢迢牵牛星 · 四境场景（水墨夜思·星河为界的两岸：迢迢皎皎、泣涕零雨、河汉清浅、盈盈脉脉） =================
   美术立意：水墨夜思色板写「星河为界的两岸+织女机杼」——底色 #0d1117、雾 #131a26 系，
   accent=#b8c4dd（月银微紫）只落在双星晕/梭光/织线光/星子落波/星光连线/鹊影边缘光/UI 上，
   全页近零饱和。母题贯穿：左岸织女机杼（木架+经线阵+素练+往返的杼），四境同在、镜头随诗推进：
   壹=双星隔河+机杼札札；贰=素练不成章+泣涕光雨；叁=清浅星水+对岸牵牛剪影；
   肆（标志性瞬间·末境可点击）=两岸对望盈盈一水：点击——星光连线次第亮起+鹊影横波掠过
   （连线而不画桥，含蓄不画具体鹊桥）。
   与已有水墨夜思页第一眼可区分：不做夜台一瑟（jinse）、不做满月江楼水天一色（jianglou-ganjiu）、
   不做云海星河带+云崖+鹊群搭桥成会（queqiaoxian-xianyun）——本页写「不成」：
   机杼札札而终日不成章，一水盈盈而脉脉不得语，星河是界不是桥。 */

/* —— 织女机杼 makeJizhuJS(o)：木架织机（台座+双立柱+顶梁+经轴/布轴/筘，合批 1 mesh）
   +经线 LineSegments（1 draw call）+素练（终日不成章的素帛）+杼（独立小 mesh 往返滑行）
   +梭光 Sprite+织线光带（均 fog:false 加色；初值=峰值——fadeK 铁律）+织女（坐姿，noProp）
   ——「札札弄机杼」的母题本体：update(t,k) 里杼沿经线往返、梭光随之、织线光按札札节律明灭 */
function makeJizhuJS(o){
  o=o||{};
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(5.8,0.5,3.6);
  base.translate(0,0.25,0); B.put(base,0x141a24);
  const fl=new THREE.BoxGeometry(5.4,0.16,3.3);
  fl.translate(0,0.56,0); B.put(fl,0x1a2230);
  [1,-1].forEach(function(s){
    const post=new THREE.BoxGeometry(0.17,2.85,0.17);
    post.translate(s*1.45,2.0,0); B.put(post,0x241d13);
    const brace=new THREE.CylinderGeometry(0.055,0.07,1.55,6);
    brace.rotateZ(s*0.5); brace.translate(s*1.02,1.25,0.60); B.put(brace,0x201a11);
  });
  const beam=new THREE.BoxGeometry(3.34,0.17,0.20);
  beam.translate(0,3.35,0); B.put(beam,0x282013);
  const cap=new THREE.BoxGeometry(3.6,0.09,0.30);
  cap.translate(0,3.48,0); B.put(cap,0x2e2517);
  const jing=new THREE.CylinderGeometry(0.09,0.09,3.05,8);
  jing.rotateZ(Math.PI/2); jing.translate(0,2.55,-0.62); B.put(jing,0x332818);
  const bu=new THREE.CylinderGeometry(0.115,0.115,3.05,8);
  bu.rotateZ(Math.PI/2); bu.translate(0,1.42,0.88); B.put(bu,0x332818);
  const kou=new THREE.BoxGeometry(2.9,0.42,0.06);
  kou.translate(0,1.98,0.30); B.put(kou,0x2a2214);
  const silk=new THREE.BoxGeometry(2.3,1.05,0.05);
  silk.translate(0,0.86,0.99); B.put(silk,0x8b98ad);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a4356,emissive:0x06080c}),{c:0xb8c4dd,i:o.rim===undefined?0.18:o.rim,p:2.4})));
  /* 经线：细线阵（1 draw call），自经轴到布轴微张 */
  const n=o.warp===undefined?26:o.warp, pos=new Float32Array(n*6);
  for(let i=0;i<n;i++){
    const x=-1.32+(i/(n-1))*2.64;
    pos[i*6]=x; pos[i*6+1]=2.52; pos[i*6+2]=-0.62;
    pos[i*6+3]=x; pos[i*6+4]=1.46; pos[i*6+5]=0.86;
  }
  const wg=new THREE.BufferGeometry();
  wg.setAttribute('position',new THREE.BufferAttribute(pos,3));
  const warp=new THREE.LineSegments(wg,
    new THREE.LineBasicMaterial({color:0x8fa0bd,transparent:true,opacity:0.34}));
  warp.renderOrder=1; g.add(warp);
  /* 杼：织布的梭子（小梭随 update 往返） */
  const shut=new THREE.Mesh(new THREE.SphereGeometry(0.09,8,6),
    new THREE.MeshPhongMaterial({color:0x3a3226,shininess:24,specular:0x556078,emissive:0x090906}));
  shut.scale.set(2.3,0.55,0.55); shut.position.set(0,2.0,0.12); shut.renderOrder=1; g.add(shut);
  /* 梭光 + 织线光带（初值=峰值；update 里包络 ≤1） */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8c4dd,
    transparent:true,opacity:0.20,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(1.1,1.1,1); glow.renderOrder=3; g.add(glow);
  const band=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa9b6cf,
    transparent:true,opacity:0.085,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  band.scale.set(3.1,0.62,1); band.position.set(0,2.0,0.16); band.renderOrder=3; g.add(band);
  /* 织女：坐姿于机后，素手向机（noProp 去杯） */
  const nz=makeFigure({pose:'坐饮',robe:0x252e40,belt:0x70809a,skin:0xd8c2ac,collar:0xaeb9c9,
    hair:0x141821,hat:'发髻',rimC:0xb8c4dd,rim:0.40,noProp:true,scale:1.02});
  nz.position.set(0,0.64,-0.95); nz.rotation.y=0.06; g.add(nz);
  const ph=(o.seed===undefined?25901:o.seed)%6.283;
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    const sx=Math.sin(t*0.85+ph);
    shut.position.x=sx*1.15;
    shut.position.y=2.0+Math.sin(t*1.7+ph)*0.05;
    glow.position.set(shut.position.x,shut.position.y+0.10,shut.position.z);
    const zhazha=Math.pow(Math.max(0,Math.sin(t*3.4+ph)),6);   /* 札札节律 */
    glow.material.opacity=kk*0.20*(0.55+0.45*zhazha);
    band.material.opacity=kk*0.085*Math.min(1,0.55+0.30*Math.sin(t*0.9+ph)+0.30*zhazha);
    nz.userData.update(t,kk);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 牵牛织女双星 makeShuangJS(o)：寒银亮核+银蓝大晕（fog:false 加色；初值=峰值），
   随呼吸明灭；update(t,k,e) 的 e 供末境点击后光晕徐涨（只放缩 scale，不加 opacity，
   fadeK 合规：任何 opacity 写 ≤ base）——「迢迢牵牛星，皎皎河汉女」 */
function makeShuangJS(o){
  o=o||{};
  const g=new THREE.Group(), stars=[];
  (o.stars||[{x:-8,y:14,z:-46,c:0xe8f0fc,s:2.4},{x:15,y:10.5,z:-54,c:0xdde9f8,s:2.0}]).forEach(function(c,i){
    const core=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:c.c,transparent:true,
      opacity:0.95,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    core.scale.set(c.s,c.s,1); core.renderOrder=3;
    const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8c4dd,transparent:true,
      opacity:0.30,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
    halo.scale.set(c.s*4.6,c.s*4.6,1); halo.renderOrder=3;
    const grp=new THREE.Group(); grp.add(core); grp.add(halo);
    grp.position.set(c.x,c.y,c.z);
    g.add(grp); stars.push({grp:grp,core:core,halo:halo,s0:c.s,ph:i*2.6});
  });
  g.update=function(t,k,e){
    const kk=k===undefined?1:k, ee=e===undefined?0:e;
    for(let i=0;i<stars.length;i++){
      const s=stars[i];
      s.core.material.opacity=kk*0.95*(0.86+0.14*Math.sin(t*1.25+s.ph));
      s.halo.material.opacity=kk*0.30*(0.82+0.18*Math.sin(t*0.85+s.ph));
      const sc=(1+0.38*ee)*(1+0.05*Math.sin(t*0.6+s.ph));
      s.halo.scale.setScalar(s.s0*4.6*sc);
      s.core.scale.setScalar(s.s0*(1+0.15*ee));
    }
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 泣涕光雨 makeLeiyuJS(o)：竖直坠落的泪光雨点（自写 ShaderMaterial，必挂
   vertexShader/fragmentShader，uFade 由 setFade 统一接管；局地光效不进 fogShaders）——
   「泣涕零如雨」：泪化作冷银光点，簌簌而落 */
const TEAR_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
varying float vA;
void main(){
  float life=fract(uTime*uSpeed*(0.6+0.8*fract(aSeed*7.7))+aSeed);
  vec3 p=position;
  p.y-=uBox.y*life;
  p.x+=sin(uTime*0.8+aSeed*31.0)*0.06;
  vA=smoothstep(0.0,0.08,life)*smoothstep(1.0,0.86,life)*(0.35+0.65*fract(aSeed*13.7));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const TEAR_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.08,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLeiyuJS(o){
  o=o||{};
  const n=o.n===undefined?110:o.n, box=o.box||[14,11,8], pos=o.pos||[-2.2,10.5,-6.5];
  const geo=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.0:o.size)*(0.7+Math.random()*0.6);
  }
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.16:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0xb9c6da:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.30:o.maxA}},
    vertexShader:TEAR_VERT,fragmentShader:TEAR_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

/* —— 天河横带 makeTianheJS(o)：高天一抹极淡的星河雾带（数条 wide fog:false 辉光 Sprite
   沿对角斜排+星尘微粒；初值=峰值）——银河在天的来处，与地上清浅星水上下相映；
   只做水墨淡痕，不做 nebula（与 queqiaoxian 的 shader 星河带区分） */
function makeTianheJS(o){
  o=o||{};
  const g=new THREE.Group(), items=[];
  const bands=o.bands||[[0,46,-172,220,30,-0.30,0.055],[ -34,52,-176,150,22,-0.34,0.045],
    [30,38,-174,130,18,-0.26,0.04]];
  for(let i=0;i<bands.length;i++){
    const b=bands[i];
    const m=new THREE.SpriteMaterial({map:glowTex(),color:i===0?0x93a5c4:0xaebccd,
      transparent:true,opacity:b[6],depthWrite:false,fog:false,blending:THREE.AdditiveBlending,
      rotation:b[5]});
    const s=new THREE.Sprite(m);
    s.scale.set(b[3],b[4],1); s.position.set(b[0],b[1],b[2]); s.renderOrder=-4;
    g.add(s); items.push({m:m,op0:b[6],ph:i*2.1});
  }
  const dust=makeGlow({n:o.dustN===undefined?40:o.dustN,box:[140,26,10],pos:[0,44,-172],
    color:0xaebccd,size:3.2,speed:0.02,rise:0,add:true,maxA:0.10});
  g.add(dust.points);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.m.opacity=kk*it.op0*(0.82+0.18*Math.sin(t*0.2+it.ph));
    }
    dust.update(t);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 星子落波 makeXingziJS(o)：清浅星水上的星子微光（makeGlow rise:0 悬浮微光，
   两层疏密；add:true 加色）——「河汉清且浅」的水面写法：星光落在水上 */
function makeXingziJS(o){
  o=o||{};
  const g=new THREE.Group();
  const a=makeGlow({n:o.nA===undefined?36:o.nA,box:o.boxA||[96,2.2,44],pos:o.posA||[0,0.8,-74],
    color:0xbccadd,size:3.0,speed:0.02,rise:0,add:true,maxA:o.maxA===undefined?0.11:o.maxA});
  a.points.renderOrder=2; g.add(a.points);
  const b=makeGlow({n:o.nB===undefined?20:o.nB,box:o.boxB||[52,1.6,22],pos:o.posB||[0,0.9,-60],
    color:0xdde6f4,size:2.2,speed:0.03,rise:0,add:true,maxA:0.08});
  b.points.renderOrder=2; g.add(b.points);
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    a.update(t); b.update(t);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 星光倒影柱 makeDaoJS(o)：双星在水面上的倒影光柱（3 枚纵列窄 fog:false 辉光，
   初值=峰值）——星在 upstream，影在水中，两岸对望的落点 */
function makeDaoJS(o){
  o=o||{};
  const g=new THREE.Group(), items=[];
  const cols=o.cols||[{x:-8.5,y:11.5,z:-40},{x:10.5,y:9.5,z:-46}];
  for(let j=0;j<cols.length;j++){
    const c=cols[j];
    for(let i=0;i<3;i++){
      const op=[0.10,0.065,0.04][i];
      const m=new THREE.SpriteMaterial({map:glowTex(),color:0xb8c4dd,transparent:true,
        opacity:op,depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
      const s=new THREE.Sprite(m);
      const sc=(3.0-i*0.8);
      s.scale.set(sc*0.55,sc*1.6,1);
      s.position.set(c.x,(c.y-2.2)-i*2.4,c.z+1.5);
      s.renderOrder=2; g.add(s); items.push({m:m,op0:op,ph:i*1.7+j});
    }
  }
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.m.opacity=kk*it.op0*(0.78+0.22*Math.sin(t*0.5+it.ph));
    }
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 星光连线 makeLianxianJS(o)：末境点击后两岸双星之间一道含蓄的星光细线
   （THREE.Line+沿线光点 Sprite，CatmullRom 弧；组 visible=false 硬关——点击前无幻影）；
   update(t,k,rv)：rv 0→1 光点次第亮起、细线徐牵——「星光相望」而不画桥 */
function makeLianxianJS(o){
  o=o||{};
  const p0=o.p0||[-8.5,13.0,-34], p1=o.p1||[10.5,11.5,-42], lift=o.lift===undefined?6.5:o.lift;
  const crv=new THREE.CatmullRomCurve3([
    new THREE.Vector3(p0[0],p0[1],p0[2]),
    new THREE.Vector3((p0[0]+p1[0])/2,Math.max(p0[1],p1[1])+lift,(p0[2]+p1[2])/2),
    new THREE.Vector3(p1[0],p1[1],p1[2])]);
  const g=new THREE.Group();
  const lp=[];
  for(let i=0;i<=30;i++){ const v=crv.getPoint(i/30); lp.push(v.x,v.y,v.z); }
  const lg=new THREE.BufferGeometry();
  lg.setAttribute('position',new THREE.BufferAttribute(new Float32Array(lp),3));
  const line=new THREE.Line(lg,new THREE.LineBasicMaterial({color:0xd8e2f2,transparent:true,
    opacity:0.42,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  line.renderOrder=4; g.add(line);
  const dots=[];
  for(let i=1;i<12;i++){
    const v=crv.getPoint(i/12);
    const base=0.30+0.30*Math.sin(i/12*Math.PI);
    const m=new THREE.SpriteMaterial({map:glowTex(),color:i%3===0?0xe6eefc:0xb8c4dd,
      transparent:true,opacity:base,depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
    const s=new THREE.Sprite(m);
    const sc=0.7+1.1*Math.sin(i/12*Math.PI);
    s.scale.set(sc,sc,1); s.position.copy(v); s.renderOrder=4;
    g.add(s); dots.push({s:s,m:m,base:base,sc:sc,ph:i*1.3});
  }
  const meet=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xdde8f8,
    transparent:true,opacity:0.24,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  const mv=crv.getPoint(0.5);
  meet.scale.set(9,9,1); meet.position.copy(mv); meet.renderOrder=4; g.add(meet);
  g.visible=false;
  const sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    const env=sm01(r/0.30);
    line.material.opacity=kk*0.42*env*(0.78+0.22*Math.sin(t*1.1));
    for(let i=0;i<dots.length;i++){
      const d=dots[i];
      const ap=sm01((r-0.04-i*0.045)/0.16);
      d.m.opacity=kk*d.base*env*ap*(0.72+0.28*Math.sin(t*1.6+d.ph));
      d.s.scale.setScalar(d.sc*(1+0.25*Math.sin(t*2.1+d.ph)));
    }
    meet.material.opacity=kk*0.24*env*(0.80+0.20*Math.sin(t*1.4));
    g.visible=kk*env>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 鹊影 makeQueyingJS(o)：末境点击后贴水掠过的鹊影（InstancedMesh 6 只，剪影含蓄，
   组 visible=false 硬关）；update(t,k,rv)：rv 驱动错峰自左岸掠向右岸，翅膀明灭，
   过后即隐——「鹊影横波」，不搭桥、不成会 */
function makeQueyingJS(o){
  o=o||{};
  const n=o.n===undefined?6:o.n;
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.10,0.5,5); body.rotateX(Math.PI/2);
  body.translate(0,0.02,0.06); B.put(body,0x0b0e15);
  const head=new THREE.SphereGeometry(0.075,6,5); head.translate(0,0.05,0.30); B.put(head,0x0d1119);
  const tail=new THREE.ConeGeometry(0.055,0.36,4); tail.rotateX(-Math.PI/2);
  tail.translate(0,0.02,-0.30); B.put(tail,0x0a0d13);
  [1,-1].forEach(function(s){
    const w=new THREE.BufferGeometry();
    w.setAttribute('position',new THREE.BufferAttribute(new Float32Array([
      0,0.04,0.12, 0,0.04,-0.14, s*0.85,0.18,-0.02]),3));
    w.computeVertexNormals(); B.put(w,0x0d1119);
  });
  const mesh=new THREE.InstancedMesh(mergeGeos(B.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
      specular:0x2a3446,emissive:0x03050a}),{c:0xb8c4dd,i:0.42,p:2.4}),n);
  mesh.frustumCulled=false; mesh.renderOrder=4;
  const g=new THREE.Group(); g.add(mesh);
  const R=seedRnd(o.seed===undefined?25931:o.seed), birds=[];
  for(let i=0;i<n;i++){
    birds.push({p0:[-10+R()*4,1.8+R()*1.2,-29-R()*4],
      p1:[10+R()*4,2.2+R()*1.2,-33-R()*5],
      d:0.06+i*0.075,ph:R()*6.283,s:0.75+R()*0.35});
  }
  const dm=new THREE.Object3D();
  g.visible=false;
  const sm01=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  g.update=function(t,k,rv){
    const kk=k===undefined?1:k, r=rv===undefined?0:rv;
    for(let i=0;i<n;i++){
      const b=birds[i];
      const q=clamp((r-b.d)/0.34,0,1);
      const e=sm01(q);
      const env=Math.sin(q*Math.PI);
      const x=b.p0[0]+(b.p1[0]-b.p0[0])*e;
      const y=b.p0[1]+(b.p1[1]-b.p0[1])*e+Math.sin(e*Math.PI)*1.4;
      const z=b.p0[2]+(b.p1[2]-b.p0[2])*e;
      dm.position.set(x,y,z);
      dm.rotation.set(0,Math.atan2(b.p1[0]-b.p0[0],b.p1[2]-b.p0[2]),Math.sin(t*10+b.ph)*0.5);
      dm.scale.setScalar(Math.max(0.001,b.s*env));
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
    g.visible=kk*r>0.004&&r<0.985;
  };
  g.userData.update=g.update;
  return g;
}

/* 远岸横陈 makeYuanJS(o)：夜色深处的低平远岸（两层，带雾骨相）——星水流向的天际；
   组放近（z≈-165），不被骨架常驻远山环（z≈-300）遮挡 */
function makeYuanJS(o){
  o=o||{};
  return makeRange({r:o.r===undefined?250:o.r,h:o.h===undefined?11:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?25921:o.seed,
    color:o.color===undefined?0x0a0f18:o.color,atmo:0x1f2a3c,
    fogK:o.fogK===undefined?0.60:o.fogK,glowK:0.05,glow:0xaebccd,
    y:o.y===undefined?-11:o.y,order:-6});
}

/* 星水 makeHanJS(o)：低垂的银河本体——清浅星水（水面 amp 极小近镜面） */
function makeHanJS(o){
  o=o||{};
  const water=makeWater({size:o.size===undefined?560:o.size,seg:88,amp:o.amp===undefined?0.06:o.amp,
    freq:0.16,speed:0.24,flow:[0.10,0.02],spec:0.95,
    deep:0x05080e,shallow:0x0e1522,skyc:0x121a28,moonDir:[-0.34,0.20,-0.92]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xbcc9dc);
  water.mesh.position.set(o.x===undefined?0:o.x,-0.52,o.z===undefined?-120:o.z);
  return water;
}

function bCover(){ // 卷首 · 星河两岸初望：清浅星水横陈，两岸岸渚，左岸机杼一点，双星低垂
  const g=new THREE.Group();
  const grd=makeGround({r:104,c1:0x0a0e16,c2:0x141b28,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const water=makeHanJS({}); g.add(water.mesh);
  const yuan=makeYuanJS({seed:25922}); yuan.g.position.set(0,0,-165); g.add(yuan.g);
  const bankL=makeRange({arc:1.0,a0:-0.55,r:38,h:6,layers:2,peaks:3,seed:25923,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-5,order:-5});
  bankL.g.position.set(-26,0,-66); g.add(bankL.g);
  const bankR=makeRange({arc:1.0,a0:-0.55,r:38,h:6,layers:2,peaks:3,seed:25924,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-5,order:-5});
  bankR.g.position.set(26,0,-66); g.add(bankR.g);
  const jz=makeJizhuJS({seed:25901}); jz.position.set(-3.2,0.55,-9); jz.rotation.y=0.32; g.add(jz);
  const sx=makeShuangJS({stars:[{x:-9,y:14.5,z:-46,c:0xe8f0fc,s:2.2},{x:14,y:11,z:-52,c:0xdde9f8,s:1.9}]});
  g.add(sx);
  const th=makeTianheJS({}); g.add(th);
  const mist=makeMist({n:5,spread:[150,10,60],pos:[0,3.4,-16],scale:46,color:0x2a3648,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[100,14,46],pos:[0,8,-2],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x05080e,seed:25925,rim:0.10,rimC:0xb8c4dd});
  fg1.g.position.set(-12,-1.6,19); g.add(fg1.g);
  const fg2=makeForeground({kind:'芦苇',w:22,n:8,d:4,color:0x05080e,seed:25926,sway:0.7,rim:0.08,rimC:0xb8c4dd});
  fg2.g.position.set(12,-1.4,18); g.add(fg2.g);
  addLights(g,{c:0xa6b6cc,i:0.30,p:[-40,52,-40]},{c:0x1a2331,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); water.update(t); yuan.update(t,0);
    jz.update(t,k); sx.update(t,k); th.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bShuang(){ // 壹 · 迢迢皎皎 —— 迢迢牵牛星，皎皎河汉女。纤纤擢素手，札札弄机杼：
                    // 机杼近景，杼往经线间穿行、札札光颤；窗外双星隔河，一低一高
  const g=new THREE.Group();
  const grd=makeGround({r:104,c1:0x0a0e16,c2:0x151c29,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const water=makeHanJS({z:-100}); g.add(water.mesh);
  const yuan=makeYuanJS({seed:25927}); yuan.g.position.set(30,0,-150); g.add(yuan.g);
  const bankR=makeRange({arc:1.0,a0:-0.55,r:34,h:5.5,layers:2,peaks:3,seed:25928,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-5,order:-5});
  bankR.g.position.set(26,0,-60); g.add(bankR.g);
  const jz=makeJizhuJS({seed:25901}); jz.position.set(-2.2,0.55,-6.4); jz.rotation.y=0.30; g.add(jz);
  /* 双星：织女星高悬机杼左上，牵牛星低垂对岸右上——迢迢与皎皎 */
  const sx=makeShuangJS({stars:[{x:-7.5,y:13.5,z:-40,c:0xe8f0fc,s:2.6},{x:17,y:9.5,z:-52,c:0xdde9f8,s:2.1}]});
  g.add(sx);
  const th=makeTianheJS({dustN:28}); g.add(th);
  const mist=makeMist({n:5,spread:[140,10,56],pos:[2,3.2,-16],scale:44,color:0x2a3648,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:22,box:[92,13,42],pos:[0,8,0],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x05080e,seed:25929,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(-11,-1.5,17); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',w:15,n:5,d:4,color:0x05080e,seed:25930,sway:0.6,rim:0.08,rimC:0xb8c4dd});
  fg2.g.position.set(12.5,-1.7,16.5); g.add(fg2.g);
  addLights(g,{c:0xa6b6cc,i:0.32,p:[-38,50,-38]},{c:0x1a2331,i:0.52});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); water.update(t); yuan.update(t,0);
    jz.update(t,k); sx.update(t,k); th.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bLeiyu(){ // 贰 · 泣涕零雨 —— 终日不成章，泣涕零如雨：
                   // 同一架机杼，素练垂而未成章；冷银光雨簌簌而落，机前积泪成泽微光
  const g=new THREE.Group();
  const grd=makeGround({r:104,c1:0x090d14,c2:0x131a26,y:-0.05}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.05,14);
  const water=makeHanJS({z:-100}); g.add(water.mesh);
  const yuan=makeYuanJS({seed:25932,h:9}); yuan.g.position.set(-20,0,-155); g.add(yuan.g);
  const jz=makeJizhuJS({seed:25902}); jz.position.set(-2.2,0.55,-6.4); jz.rotation.y=0.30; g.add(jz);
  /* 泣涕零如雨：竖直坠落的冷银光雨 + 机前泪泽微光 */
  const rain=makeLeiyuJS({n:120,box:[15,11,8],pos:[-2.2,10.5,-6.5],speed:0.15,maxA:0.30});
  g.add(rain.points);
  const pool=makeGlow({n:16,box:[9,0.7,5],pos:[-2.2,0.85,-5.5],color:0x9fb0c8,size:2.6,
    speed:0.04,rise:0,add:true,maxA:0.10});
  pool.points.renderOrder=2; g.add(pool.points);
  const sx=makeShuangJS({stars:[{x:-7.5,y:13.5,z:-40,c:0xe8f0fc,s:2.0},{x:17,y:9.5,z:-52,c:0xdde9f8,s:1.6}]});
  g.add(sx);
  const mist=makeMist({n:6,spread:[150,10,58],pos:[-1,3.4,-15],scale:46,color:0x2a3648,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:20,box:[90,13,42],pos:[0,8,0],color:0xaebccd,size:3.4,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.3,w:10,d:4,color:0x05080e,seed:25933,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(-11.5,-1.5,16.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'栏杆',w:22,h:3.0,color:0x05080e,seed:25934,rim:0.08,rimC:0xb8c4dd});
  fg2.g.position.set(2,-2.9,15.5); g.add(fg2.g);
  addLights(g,{c:0xa2b0c6,i:0.26,p:[-38,48,-38]},{c:0x18212e,i:0.50});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); water.update(t); yuan.update(t,0);
    jz.update(t,k); rain.update(t); pool.update(t,k); sx.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bQingqian(){ // 叁 · 河汉清浅 —— 河汉清且浅，相去复几许：
                      // 镜头压低贴着星水望去：水面星子落波，对岸小渚立着牵牛剪影，星低垂
  const g=new THREE.Group();
  const grd=makeGround({r:88,c1:0x0a0e16,c2:0x141b28,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,40);
  const water=makeHanJS({size:640,z:-130,amp:0.045}); g.add(water.mesh);
  const yuan=makeYuanJS({r:250,h:8,y:-13,seed:25935}); yuan.g.position.set(-10,0,-170); g.add(yuan.g);
  /* 近右岸渚 + 远左岸渚：河道中开，一水纵目 */
  const bankR=makeRange({arc:0.9,a0:-0.50,r:30,h:5.5,layers:2,peaks:3,seed:25936,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-5,order:-5});
  bankR.g.position.set(24,0,-56); g.add(bankR.g);
  const bankL=makeRange({arc:0.9,a0:-0.55,r:40,h:6.5,layers:2,peaks:3,seed:25937,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-6,order:-5});
  bankL.g.position.set(-32,0,-88); g.add(bankL.g);
  /* 对岸牵牛剪影：小渚（已知高度的岩嘴）上一个远人影，牵牛星低垂其上 */
  const rock=new THREE.Mesh(new THREE.ConeGeometry(1.7,3.2,5),
    new THREE.MeshPhongMaterial({color:0x0d131d,emissive:0x05070b,shininess:6,specular:0x303c50}));
  rock.position.set(13,1.2,-72); g.add(rock);
  const fig=new THREE.Mesh(crowdGeo(),
    rimHook(new THREE.MeshPhongMaterial({color:0x1a2230,vertexColors:true,shininess:8,
      specular:0x303c50,emissive:0x05070b}),{c:0xb8c4dd,i:0.30,p:2.4}));
  fig.position.set(13,2.6,-71.6); fig.scale.setScalar(0.95); fig.rotation.y=-2.6; g.add(fig);
  const sx=makeShuangJS({stars:[{x:-30,y:16,z:-100,c:0xe8f0fc,s:2.0},{x:13,y:9.5,z:-74,c:0xdde9f8,s:2.3}]});
  g.add(sx);
  /* 星子落波：清浅星水的亮面 */
  const xz=makeXingziJS({}); g.add(xz);
  const th=makeTianheJS({dustN:30}); g.add(th);
  const mist=makeMist({n:5,spread:[170,9,64],pos:[0,2.6,-60],scale:52,color:0x2a3648,op:0.08});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[120,12,50],pos:[0,6,-20],color:0xaebccd,size:3.4,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:26,n:10,d:5,color:0x05080e,seed:25938,sway:0.8,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(-10,-1.4,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05080e,seed:25939,rim:0.10,rimC:0xb8c4dd});
  fg2.g.position.set(12,-1.5,11.5); g.add(fg2.g);
  addLights(g,{c:0xa6b4c8,i:0.30,p:[30,46,-40]},{c:0x1a2331,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grd.update(); water.update(t); yuan.update(t,0);
    sx.update(t,k); xz.update(t,k); th.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bYingying(){ // 肆（标志性瞬间·末境可点击）· 盈盈脉脉 —— 盈盈一水间，脉脉不得语：
                      // 两岸相近：左岸机杼织女、右岸牵牛剪影，双星与倒影两两相对；
                      // 点击：星光连线次第亮起+鹊影横波自左岸掠向右岸（不画桥）
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const g=new THREE.Group();
  const grd=makeGround({r:92,c1:0x0a0e16,c2:0x141b28,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,40);
  const water=makeHanJS({size:560,z:-110,amp:0.05}); g.add(water.mesh);
  const yuan=makeYuanJS({r:250,h:9,y:-12,seed:25940}); yuan.g.position.set(0,0,-168); g.add(yuan.g);
  /* 两岸相近（盈盈一水间）：左右岸渚相夹，河道收窄 */
  const bankL=makeRange({arc:1.0,a0:-0.55,r:32,h:6.5,layers:2,peaks:3,seed:25941,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-5,order:-5});
  bankL.g.position.set(-25,0,-58); g.add(bankL.g);
  const bankR=makeRange({arc:1.0,a0:-0.55,r:32,h:6.5,layers:2,peaks:3,seed:25942,color:0x0b111c,
    atmo:0x1f2a3c,fogK:0.62,glowK:0.05,glow:0xaebccd,y:-5,order:-5});
  bankR.g.position.set(25,0,-58); g.add(bankR.g);
  /* 左岸：机杼与织女（暗调，唯梭光与素练微亮） */
  const plat=new THREE.Mesh(new THREE.BoxGeometry(6,1.0,3.6),
    new THREE.MeshPhongMaterial({color:0x11161f,emissive:0x04060a,shininess:5,specular:0x2a3346}));
  plat.position.set(-7,0.35,-30); g.add(plat);
  const jz=makeJizhuJS({seed:25903,rim:0.12}); jz.position.set(-7,0.85,-30); jz.rotation.y=-0.42;
  jz.scale.setScalar(0.82); g.add(jz);
  /* 右岸：牵牛剪影立于岸嘴，星低垂其上 */
  const rock2=new THREE.Mesh(new THREE.ConeGeometry(1.5,2.6,5),
    new THREE.MeshPhongMaterial({color:0x0d131d,emissive:0x05070b,shininess:6,specular:0x303c50}));
  rock2.position.set(9.5,0.7,-40); g.add(rock2);
  const fig=new THREE.Mesh(crowdGeo(),
    rimHook(new THREE.MeshPhongMaterial({color:0x1a2230,vertexColors:true,shininess:8,
      specular:0x303c50,emissive:0x05070b}),{c:0xb8c4dd,i:0.30,p:2.4}));
  fig.position.set(9.5,1.8,-39.6); fig.scale.setScalar(0.95); fig.rotation.y=-2.9; g.add(fig);
  /* 双星与倒影：织女星高、牵牛星低，两两相对；水面倒影柱 */
  const sx=makeShuangJS({stars:[{x:-8.5,y:13.0,z:-34,c:0xe8f0fc,s:2.5},{x:10.5,y:11.5,z:-42,c:0xdde9f8,s:2.2}]});
  g.add(sx);
  const dao=makeDaoJS({cols:[{x:-8.5,y:11.0,z:-40},{x:10.5,y:9.4,z:-46}]}); g.add(dao);
  const xz=makeXingziJS({boxA:[76,2.2,36],posA:[0,0.8,-62],nA:30,maxA:0.10}); g.add(xz);
  /* 标志性交互：星光连线+鹊影横波（点击前 visible=false 硬关） */
  const lx=makeLianxianJS({p0:[-8.5,13.0,-34],p1:[10.5,11.5,-42],lift:6.5}); g.add(lx);
  const qy=makeQueyingJS({seed:25943}); g.add(qy);
  const mist=makeMist({n:6,spread:[160,10,62],pos:[0,3.0,-30],scale:50,color:0x2a3648,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:24,box:[110,13,48],pos:[0,7,-12],color:0xaebccd,size:3.6,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'芦苇',w:24,n:9,d:5,color:0x05080e,seed:25944,sway:0.75,rim:0.09,rimC:0xb8c4dd});
  fg1.g.position.set(-11,-1.4,13.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x05080e,seed:25945,rim:0.10,rimC:0xb8c4dd});
  fg2.g.position.set(11.5,-1.5,13); g.add(fg2.g);
  addLights(g,{c:0xa4b2c8,i:0.28,p:[-42,50,-42]},{c:0x19222f,i:0.52});
  const eSm=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/6.0);
      const e=eSm(ctl.reveal);
      sx.update(t,k,e);                          // 双星光晕徐涨（scale 放缩，opacity 不越峰值）
      lx.update(t,k,ctl.reveal);                 // 星光连线次第亮起
      qy.update(t,k,ctl.reveal);                 // 鹊影横波
      jz.update(t,k); dao.update(t,k); xz.update(t,k);
      mist.update(t,k); motes.update(t);
      fg1.update(t,k); fg2.update(t,k);
      grd.update(); water.update(t); yuan.update(t,0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.10);
        pluck(1,0.05,0.10); pluck(3,0.75,0.09); pluck(5,1.5,0.08);   // 星光三叠，渐远
        const fl=$('#flash'); fl.textContent='盈盈一水间 脉脉不得语';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x060a13),hor:C(0x141c2a),bot:C(0x04070c),fog:C(0x131a26),fd:0.0052,star:0.30,
  moon:new THREE.Vector3(-64,74,-180),ms:0.85,mph:0.42,mhaze:0.14,dirC:C(0xa6b6cc),dirI:0.32,
  dirP:new THREE.Vector3(-40,52,-40),ambC:C(0x1a2331),ambI:0.52},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9.5,30],t:[0,8.2,20],lf:[0,7.5,-10],lt:[0,9.5,-34]},
  sky:()=>SK({fd:0.0050,star:0.34,ms:0.85,mph:0.42}) },
{ name:'迢迢皎皎',dwell:17,river:0.02,build:bShuang,
  cam:{f:[-1.8,4.4,9.6],t:[0.8,3.1,1.5],lf:[-1.2,4.2,-6],lt:[2.5,4.6,-18]},
  sky:()=>SK({fd:0.0052,star:0.30,ms:0.80,mph:0.44,mhaze:0.16,
    moon:new THREE.Vector3(-60,70,-176),dirC:C(0xa6b6cc),dirI:0.32,
    dirP:new THREE.Vector3(-38,50,-38),ambC:C(0x1a2331),ambI:0.52}) },
{ name:'泣涕零雨',dwell:17,river:0.02,build:bLeiyu,
  cam:{f:[-1.2,4.9,8.4],t:[-0.4,2.9,-0.5],lf:[-1.5,4.6,-8],lt:[1.0,4.2,-20]},
  sky:()=>SK({fd:0.0058,star:0.14,ms:0.55,mph:0.50,mhaze:0.24,hor:C(0x121a28),
    moon:new THREE.Vector3(-52,60,-170),dirC:C(0xa2b0c6),dirI:0.26,
    dirP:new THREE.Vector3(-38,48,-38),ambC:C(0x18212e),ambI:0.50}) },
{ name:'河汉清浅',dwell:18,river:0.02,build:bQingqian,
  cam:{f:[1.2,3.1,12.5],t:[2.8,3.7,-10],lf:[2.0,3.4,-12],lt:[6.0,5.0,-34]},
  sky:()=>SK({fd:0.0056,star:0.34,ms:0.75,mph:0.46,mhaze:0.14,
    moon:new THREE.Vector3(-66,76,-182),dirC:C(0xa6b4c8),dirI:0.30,
    dirP:new THREE.Vector3(30,46,-40),ambC:C(0x1a2331),ambI:0.54}) },
{ name:'盈盈脉脉',dwell:20,river:0.02,build:bYingying,
  cam:{f:[0,5.6,14.5],t:[0,6.4,-6],lf:[0,6.6,-12],lt:[0,7.6,-30]},
  sky:()=>SK({fd:0.0060,star:0.40,ms:0.70,mph:0.46,mhaze:0.15,
    moon:new THREE.Vector3(-70,80,-184),dirC:C(0xa4b2c8),dirI:0.28,
    dirP:new THREE.Vector3(-42,50,-42),ambC:C(0x19222f),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('tiaotiao-qianniu.py —— 被 build.py 消费：python build.py tiaotiao-qianniu')
