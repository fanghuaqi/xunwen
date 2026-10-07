# -*- coding: utf-8 -*-
"""tiwujiangting.py —— 《题乌江亭》（唐·杜牧，queue no.233，大漠金戈·乌江史迹变体）生成配置
两境（N=queue stages 数）：忍耻男儿（胜败兵家事不期·包羞忍耻是男儿——暮色江亭、断碣题诗）、
卷土重来（江东子弟多才俊·卷土重来未可知——标志性瞬间+末境点击「点击卷土重来——
江东子弟军阵虚影集结又散」）。
大漠金戈全套色板：底色 #120d08、雾 #1a120c～#141009 系、文字 #f0e2cc，accent=#b8906a
（queue 分配强调色，暮金亭柱色）只落在亭匾/碑刻受光/人物边缘光/军阵幻影幽光/UI 上，禁艳金。
全页立意「乌江岸的假设历史」：这不是战场页，也不是白骨页——是**史迹渡口的苍凉怀古**：
江亭（柱瓦小亭）+断碣（题诗残碑）+渡口石阶+大江东去（水面原型+雾同步）+对岸江东
（常驻滩头+远岸轮廓弧带），两境同一组史迹母题贯穿：境壹暮色沉江立「忍辱」之论，
境贰入夜隔江作「卷土」之想。
标志性瞬间（境贰·mk moment「卷土重来未可知（乌江岸的假设历史）」）：对岸江东在夜色与
江雾中若隐若现——假设的历史尚未发生，只等一次点击。
末境点击（queue interact：点击卷土重来——江东子弟军阵虚影集结又散）：点击画面——
①对岸烟尘渐起；②江东子弟军阵虚影三列自江雾中集结（前后排相位错落，幻影军旗同现，
accent 幽光边缘）；③持驻明灭数息；④复又散入江雾（由后排先散，烟尘上飘，终至全无）；
「江东子弟多才俊 卷土重来未可知」题字同现。点击前幻影组 visible=false 硬关。
与已有大漠金戈页（战阵/夜射/骏马/白骨/剑客/孤城金甲/书斋吴钩/大湖/铁马冰河/凌烟阁）
第一眼可区分：没有战争进行时——只有江、亭、碣、渡口与一场隔江悬想的假设军阵，
核心是史论翻案的「静」与「想」。
考点钉子：期 qī（预料）/ 卷 juǎn（卷土）（第 3 题落点）；项羽乌江自刎+王安石《叠题乌江亭》
反驳杜牧（第 4 题）；「包羞忍耻是男儿」的翻案史论主旨（第 5 题）。
tts 多音字：事不期→事不欺（qī）、卷土重来→卷土虫来（chóng）（tts.json，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='tiwujiangting', title='题乌江亭', dyn='唐 · 杜牧', brand_author='杜 牧',
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
    ],
    tip='轻点画面 / 按空格 —— 江东子弟军阵虚影集结又散',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看江东子弟军阵虚影集结又散，散入江雾',
    cover_read='题乌江亭。唐，杜牧。胜败兵家事不期，包羞忍耻是男儿。江东子弟多才俊，卷土重来未可知。',
    cover_p1='两重意境，随诗句次第展开：乌江亭畔，暮色沉江——胜败原是兵家常事，难以预料；能包忍羞耻、受挫不折，才算是真男儿。设想江东子弟人才依旧，若肯渡江再起、卷土重来，胜负谁知？',
    cover_p2='边读诗，边随杜牧立在乌江渡口：这不是一首寻常的凭吊诗，而是一场为项羽「翻案」的史论——读懂「包羞忍耻」与「未可知」，就读懂了杜牧议史的警拔与惋惜。',
    end_h2='卷土 · 遐思', cn_word='贰',
    words_js="['再看一眼乌江渡口','初识樊川，尚需共读','渐入诗境，再诵几遍','暮色渐沉，江雾渐起','已解包羞忍耻之志','卷土重来，遐思未已']",
    sky_atmo='0x2c1e12',
)

POEM_JS = """const POEM = [
{ name:'忍耻男儿', jing:'胜败原是兵家用兵的常事，难以预料；能包忍羞耻、受挫不折，才算是真正的男儿 —— 起句立论，为翻案张本。（乌江亭畔 · 断碣题诗 · 残照沉江）',
  segs:[
   {c:'胜败兵家事不期，', p:py('shèng bài bīng jiā shì bù qī')},
   {c:'包羞忍耻是男儿。', p:py('bāo xiū rěn chǐ shì nán ér')}],
  read:'胜败兵家事不期，包羞忍耻是男儿。',
  yisi:'胜败乃兵家用兵的常事，难以预料；能包忍羞耻、忍受挫辱，才算是真正的男儿。——这是全诗立论的第一层：世人多以项羽乌江自刎为悲壮的定局，杜牧路过乌江亭却另翻新案，先立一个衡量英雄的标准——不以成败论英雄，而以能否「包羞忍耻」论男儿。「胜败兵家事不期」近乎常语，「包羞忍耻是男儿」才是卓识：项羽兵败垓下便自刎江边，在杜牧看来正是输不起、忍不了。这个标准一立，末句「未可知」的惋惜才有了着落。议论起笔，斩截有力，正是杜牧咏史绝句「翻案法」的典型笔法。',
  zhu:[['题乌江亭','乌江亭：在今安徽和县东北乌江浦，相传为西楚霸王项羽兵败自刎之处。杜牧会昌年间任池州刺史时路过凭吊，借题发挥写成这首翻案史论诗'],['兵家','用兵之人，此处偏指统兵为将者——「胜败兵家事不期」即胜败乃兵家常事'],['事不期','期，读 qī，预料、逆料——胜败之事难以预先料定，不可指望常胜，也不可因一败而定终身'],['包羞','包容羞辱——能咽下一时的失败之耻，不因颜面而轻掷性命'],['忍耻','忍住耻辱——与「包羞」互文见义，都是能屈能伸、受挫而不坠其志的意思'],['是男儿','（能包羞忍耻）才算真正的男子汉——为末句「卷土重来」的假设立起前提：先有忍辱的胸襟，才谈得上东山再起']] },
{ name:'卷土重来', jing:'江东子弟多有才能出众之人，若渡江重整旗鼓、卷土重来，胜败之数尚未可知 —— 假设历史的千古一问。（江东对岸 · 军阵虚影 · 标志性瞬间：乌江岸的假设历史）（末境点击画面：江东子弟军阵虚影集结又散）',
  segs:[
   {c:'江东子弟多才俊，', p:py('jiāng dōng zǐ dì duō cái jùn')},
   {c:'卷土重来未可知。', p:py('juǎn tǔ chóng lái wèi kě zhī')}],
  read:'江东子弟多才俊，卷土重来未可知。',
  yisi:'江东子弟多有才能出众之人，若能渡江重整旗鼓、卷土重来，胜败之数尚未可知。——这是全诗的落点，也是千古传诵的假设：「卷土重来」由「江东子弟多才俊」推出——根基还在，人才还在，凭什么断言不能再战？「未可知」三字下得极有分寸：不说「必可」，不下断语，只把历史的另一种可能轻轻推开一道门缝，惋惜与激励俱在其中。而正是这一句，引出了后来王安石的反驳——人心已散，纵有子弟，谁肯再为君王卷土？一正一反，两首同题之作成为咏史翻案的千古公案。',
  zhu:[['江东','长江在芜湖至南京间呈西南—东北走向，古人称其东岸地区为「江东」（项羽起兵的吴中之地即在此）——隔江相望，正是「卷土重来」的假设去处'],['子弟','项羽当年率八千江东子弟渡江而西——此句设想江东人才依旧辈出，仍是可用之资'],['多才俊','才俊：才能出众之人——江东人杰地灵，若项羽渡江，未必没有东山再起的资本'],['卷土重来','卷土：人马奔跑时卷扬起尘土——形容失败之后集结力量、重新来过；成语「卷土重来」即出此句。卷，读 juǎn'],['未可知','尚未可知——鹿死谁手，犹未可料；一个「未」字，把惋惜、假设与激励都收进含蓄的议论里'],['叠题乌江亭','王安石后来作《叠题乌江亭》反驳此诗：「江东子弟今虽在，肯与君王卷土重来？」——认为项羽失尽人心、大势已去，可与本诗对读']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「胜败兵家事不期」的下一句是？', o:['包羞忍耻是男儿','江东子弟多才俊','卷土重来未可知'], a:0},
 {q:'「江东子弟多才俊」的下一句是？', o:['包羞忍耻是男儿','卷土重来未可知','胜败兵家事不期'], a:1},
 {q:'「胜败兵家事不期」「卷土重来未可知」中，「期」「卷」的读音和意思都正确的一项是？', o:['期读 qī，预料——「事不期」即胜败之事难以预料；卷读 juǎn，「卷土」指人马奔跑卷起尘土，「卷土重来」喻失败之后集结力量东山再起','期读 qí，星期——「事不期」即事情没有约定日期；卷读 juàn，试卷——「卷土」指铺开舆图指挥作战','期读 jī，期年——「事不期」即不满一年；卷读 quán，卷曲——「卷土重来」是蜷缩身子躲藏退走之意'], a:0},
 {q:'本诗与项羽乌江自刎的典故相关，后世还有诗人作诗反驳本诗观点。下列说法正确的是？', o:['乌江亭在今安徽和县东北，相传是项羽兵败自刎之地——杜牧路过题诗，认为胜败乃兵家常事，项羽若能包羞忍耻渡归江东，未必不能卷土重来；后来王安石作《叠题乌江亭》反驳，认为项羽失尽人心，「江东子弟今虽在，肯与君王卷土重来？」','乌江亭是刘邦设鸿门宴之处——杜牧题诗讽刺项羽宴上不杀刘邦；王安石的反驳诗则称赞项羽当机立断','乌江亭是韩信十面埋伏之战的旧址——杜牧题诗同情韩信功高被杀；王安石反驳说韩信本无反心，不该逼反'], a:0},
 {q:'对「卷土重来未可知」与全诗主旨的理解，最恰当的一项是？', o:['这是一首翻案史论诗：世人多以项羽自刎为英雄末路的定局，杜牧却提出胜败乃兵家常事、真男儿当能包羞忍耻——若渡江东山再起，胜负尚未可知；惋惜之中含着激励，议论警拔，是为项羽「翻案」的咏史绝句','这是哀叹项羽必然兵败身死、汉家天下已定的纪实诗，意在赞美刘邦善用人才、终于一统天下','这是劝说江东子弟尽快渡江北上、为项羽复仇的动员诗，号召大家追随项羽卷土重来、与刘邦再决雌雄'], a:0},
];
"""

SCENES_JS = """/* ================= 题乌江亭 · 两境场景（大漠金戈·乌江史迹变体：忍耻男儿、卷土重来） =================
   美术立意：大漠金戈色板写「史迹渡口的苍凉怀古→隔江悬想的假设军阵」——底色 #120d08、
   雾 #1a120c～#141009 系，accent=#b8906a（暮金亭柱色）只落在亭匾/碑刻受光/人物边缘光/
   军阵幻影幽光/UI 上，禁艳金。
   全页母题是「乌江渡口的史迹感」：江亭（石台+四柱+攒尖翘檐小亭）+断碣（题诗残碑）+
   渡口石阶+大江东去（水面原型，着色器入 fogShaders 雾同步）+对岸江东（常驻滩头+
   远岸轮廓弧带）。近岸地面圆盘后撤到 z≈-24，让出 z -24…-100 的大江横带——「大江东去」
   必须第一眼可读；水面配色提亮 + uMoonDir 对准月位，月光高光铺在江面上。
   情绪推进线：境壹=暮色沉江（残照、江雾、断碣无言——立「忍辱」之论）→
   境贰=入夜悬想（月升高、星渐密——对岸江东隐约，假设历史只等一次点击）。
   标志性瞬间（境贰）：乌江岸的假设历史——对岸烟尘与江雾之间，千军卷土的幻影尚未成形。
   末境点击：江东子弟军阵虚影三列集结（相位错落）→持驻明灭→散入江雾，烟尘上飘，终至全无。
   与已有大漠金戈页第一眼可区分：不做战阵厮杀/夜射/骏马/白骨/剑客/孤城金甲/书斋吴钩/
   铁马冰河/凌烟阁——只有江、亭、碣、渡口与一场隔江悬想的假设军阵（史论翻案的「静」与「想」）。 */

/* —— 乌江亭 makeJiangTing(o)：石台基+前阶+四柱柱础+檐枋+四角攒尖重檐顶+翘檐+宝顶+匾额+矮栏
   （合批 1 mesh）——「乌江亭」本体：史迹感的小亭，非歌台非楼阁 */
function makeJiangTing(o){
  o=o||{};
  const w=o.w===undefined?7.8:o.w, d=o.d===undefined?7.8:o.d;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w,1.0,d); base.translate(0,0.50,0); B.put(base,0x37302a);
  const fl=new THREE.BoxGeometry(w*0.94,0.16,d*0.94); fl.translate(0,1.06,0); B.put(fl,0x453b30);
  for(let i=0;i<2;i++){
    const st=new THREE.BoxGeometry(w*0.34,0.26,0.80);
    st.translate(0,0.86-i*0.26,d/2+0.42+i*0.56); B.put(st,shadeColor(0x37302a,0.92+i*0.12));
  }
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const zhu=new THREE.CylinderGeometry(0.14,0.17,3.3,8);
    zhu.translate(sx*w*0.38,1.14+1.65,sz*d*0.38); B.put(zhu,0x4a2e1e);
    const chu=new THREE.BoxGeometry(0.52,0.22,0.52);
    chu.translate(sx*w*0.38,1.25,sz*d*0.38); B.put(chu,0x2c2620);
  }
  const beam=new THREE.BoxGeometry(w*1.06,0.24,d*1.06); beam.translate(0,4.52,0); B.put(beam,0x3a2416);
  const roof=new THREE.ConeGeometry(w*0.86,1.9,4); roof.rotateY(Math.PI/4);
  roof.scale(1.12,1,1.12); roof.translate(0,5.72,0); B.put(roof,0x221408);
  const skirt=new THREE.ConeGeometry(w*0.80,0.62,4); skirt.rotateY(Math.PI/4);
  skirt.scale(1.12,1,1.12); skirt.translate(0,5.02,0); B.put(skirt,0x2a1a0c);
  for(let sx=-1;sx<=1;sx+=2)for(let sz=-1;sz<=1;sz+=2){
    const eave=new THREE.ConeGeometry(0.26,1.0,4);
    eave.rotateZ(-sx*0.52); eave.rotateX(sz*0.52);
    eave.translate(sx*w*0.50,4.92,sz*d*0.50); B.put(eave,0x2e1c0e);
  }
  const finial=new THREE.SphereGeometry(0.17,7,6); finial.translate(0,6.78,0); B.put(finial,0x6a5232);
  const bian=new THREE.BoxGeometry(1.30,0.50,0.10); bian.translate(0,4.24,d*0.47); B.put(bian,0xb8906a);
  const railF=new THREE.BoxGeometry(w*0.90,0.09,0.09); railF.translate(0,1.86,d/2-0.30); B.put(railF,0x3c2c1c);
  for(let sx=-1;sx<=1;sx+=2){
    const railS=new THREE.BoxGeometry(0.09,0.09,d*0.82); railS.translate(sx*(w/2-0.26),1.86,0); B.put(railS,0x3c2c1c);
  }
  for(let i=0;i<4;i++){
    const post=new THREE.BoxGeometry(0.10,0.56,0.10); post.translate(-w*0.36+i*w*0.24,1.58,d/2-0.30); B.put(post,0x322416);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x0a0705}),{c:0xb8906a,i:o.rim===undefined?0.14:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 断碣 makeDuanJie(o)：残碑（碑座+斜立碑身+碑首+断落碎石+三行刻痕，合批 1 mesh）——
   「亭柱题诗」的题眼：当年题诗已残，史论犹在 */
function makeDuanJie(o){
  o=o||{};
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(2.3,0.55,1.25); base.translate(0,0.27,0); B.put(base,0x302a24);
  const body=new THREE.BoxGeometry(1.5,2.7,0.30); body.rotateZ(0.055); body.translate(0,1.55,0); B.put(body,0x3e372e);
  const cap=new THREE.BoxGeometry(1.66,0.36,0.40); cap.rotateZ(0.055); cap.translate(0,3.06,0); B.put(cap,0x353028);
  const frag=new THREE.BoxGeometry(0.62,0.34,0.28); frag.rotateZ(1.05); frag.rotateY(0.4);
  frag.translate(0.95,0.34,0.42); B.put(frag,0x38322a);
  for(let i=0;i<3;i++){
    const hen=new THREE.BoxGeometry(1.05-i*0.16,0.07,0.05); hen.rotateZ(0.055);
    hen.translate(-0.04,2.52-i*0.30,0.165); B.put(hen,0x2a241e);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3c3630,emissive:0x0a0806}),{c:0xb8906a,i:o.rim===undefined?0.12:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 渡口 makeDukou(o)：入水石阶五级（两侧梯梁夹持，读作"阶"而非散板）+系舟石墩（合批 1 mesh）——
   渡口的史迹痕迹 */
function makeDukou(o){
  o=o||{};
  const B=new GeoBag();
  for(let sd=-1;sd<=1;sd+=2){
    const str=new THREE.BoxGeometry(0.20,0.52,5.9); str.translate(sd*1.32,0.02,-2.15); B.put(str,0x262019);
  }
  for(let i=0;i<5;i++){
    const st=new THREE.BoxGeometry(2.7-i*0.20,0.40,0.90);
    st.translate(0,0.14-i*0.30,-i*1.05); B.put(st,shadeColor(0x2e2822,0.92-0.05*i));
  }
  const moor=new THREE.BoxGeometry(0.72,0.62,0.72); moor.translate(1.85,-0.02,0.55); B.put(moor,0x28221c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2e2a24,emissive:0x080605}),{c:0xb8906a,i:0.08,p:2.2})));
  return g;
}

/* —— 对岸江东两件套：滩头 makeTantouJS(o)（常驻低平沙洲长条，军阵虚影的立足之地）+
   远岸轮廓 makeJiangdongAn(o)（makeRange arc 弧带低岸线，居中朝对岸）——
   「隔江」的空间前提：滩头横在水线之外 z≈-80，远岸山影在其后 z≈-100…-128 */
function makeTantouJS(o){
  o=o||{};
  const B=new GeoBag();
  const spit=new THREE.BoxGeometry(o.len===undefined?122:o.len,2.2,8.0);
  spit.translate(0,-0.20,-80); B.put(spit,0x161009);
  const top=new THREE.BoxGeometry(o.len===undefined?100:o.len,0.20,7.6);
  top.translate(0,0.82,-80); B.put(top,0x1a130a);
  const R=seedRnd(o.seed===undefined?23341:o.seed);
  for(let i=0;i<7;i++){
    const rk=new THREE.SphereGeometry(0.5+R()*0.8,6,5); rk.scale(1.3,0.55,1.0);
    rk.translate(-54+i*18+(R()-0.5)*8,0.95,-80+(R()-0.5)*4.5); B.put(rk,0x241b10);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a241c,emissive:0x070504}),{c:0xb8906a,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  return g;
}
function makeJiangdongAn(o){
  o=o||{};
  return makeRange({r:o.r===undefined?128:o.r,h:o.h===undefined?8:o.h,layers:2,peaks:4,seg:120,
    seed:o.seed===undefined?23322:o.seed,color:o.color===undefined?0x0d0906:o.color,atmo:0x2c1e12,
    fogK:o.fogK===undefined?0.58:o.fogK,glowK:0.06,glow:0xd8a860,
    y:o.y===undefined?-5.5:o.y,order:-5,arc:1.5,a0:Math.PI-0.75});
}

/* —— 远山一环 makeYuanShanJS(o)：夜色深处的低平远山环（骨架 bgRange 之前的自建层，z≈-170）—— */
function makeYuanShanJS(o){
  o=o||{};
  return makeRange({r:o.r===undefined?240:o.r,h:o.h===undefined?8:o.h,layers:2,
    peaks:o.peaks===undefined?4:o.peaks,seed:o.seed===undefined?23321:o.seed,
    color:o.color===undefined?0x0c0806:o.color,atmo:0x2c1e12,
    fogK:o.fogK===undefined?0.60:o.fogK,glowK:0.05,glow:0xd8a860,
    y:o.y===undefined?-7:o.y,order:-6});
}

/* —— 军阵虚影 makeJunZhen(o)：江东子弟三列幻影（每列 GeoBag 合批 1 mesh：锥身+头+长戟+戟锋，
   半透明 Phong+accent 边缘幽光）+ 幻影军旗三面（旗杆并入中列，旗面独立摆动）。
   update(t,k,ct)：ct=点击后秒数（未点击传 -1）——集结→持驻→散入江雾，逐列相位错落；
   包络恒 ≤1，材质 opacity 初值=峰值 op0，逐帧写 k*op0*env*flick（fadeK 合规）。
   立足于对岸滩头（z≈-78…-84，滩头面 y≈+0.42）。 */
function makeJunZhen(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?23311:o.seed);
  const g=new THREE.Group();
  const rows=[{z:-78,n:13,op:0.50},{z:-80.5,n:11,op:0.44},{z:-83,n:10,op:0.38}];
  const mats=[];
  rows.forEach(function(rw){
    const B=new GeoBag();
    for(let i=0;i<rw.n;i++){
      const x=-46+(i+0.5)*(92/rw.n)+(R()-0.5)*2.0;
      const s=1.0+R()*0.45, bx=x, bz=rw.z+(R()-0.5)*1.6, by=0.94;
      const bd=new THREE.ConeGeometry(0.34,1.2,7); bd.scale(s,s,s); bd.translate(bx,by+0.62*s,bz);
      B.put(bd,shadeColor(0x6a5c4a,0.78+0.42*R()));
      const hd=new THREE.SphereGeometry(0.15,6,5); hd.scale(s,s,s); hd.translate(bx,by+1.46*s,bz); B.put(hd,0x4a4034);
      const jp=new THREE.CylinderGeometry(0.028,0.036,2.9,5); jp.rotateZ((R()-0.5)*0.16);
      jp.translate(bx+0.32*s,by+1.52*s,bz); B.put(jp,shadeColor(0x6a5a44,0.9+0.3*R()));
      const jt=new THREE.ConeGeometry(0.062,0.36,4); jt.translate(bx+0.32*s,by+3.12*s,bz); B.put(jt,0x9a8258);
    }
    const m=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,transparent:true,opacity:rw.op,
      shininess:8,specular:0x5a4c3a,emissive:0x2a1c10,depthWrite:false});
    rimHook(m,{c:0xc9a878,i:0.90,p:2.4});
    const mesh=B.mesh(m); mesh.renderOrder=2; g.add(mesh);
    mats.push(m);
  });
  const Bp=new GeoBag();
  [[-32,-79.5],[3,-77.5],[33,-81]].forEach(function(p){
    const pole=new THREE.CylinderGeometry(0.05,0.075,4.8,5); pole.translate(p[0],2.55,p[1]); Bp.put(pole,0x5a4a34);
  });
  const poleMesh=Bp.mesh(mats[1]); g.add(poleMesh);
  const flags=[];
  [[-32,-79.5],[3,-77.5],[33,-81]].forEach(function(p,i){
    const fm=new THREE.MeshPhongMaterial({color:0x6a4e2c,transparent:true,opacity:0.42,side:THREE.DoubleSide,
      emissive:0x33200c,depthWrite:false});
    const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.2,3.0,4,6),fm);
    fl.position.set(p[0]+1.15,3.55,p[1]); fl.renderOrder=3; g.add(fl);
    flags.push({m:fl,mat:fm,ph:i*2.09});
  });
  function envRow(ri,ct){
    const rA=Math.max(0,Math.min(1,ct/3.4));
    const rise=sstep(0.06+ri*0.26,0.46+ri*0.26,rA);
    const rD=Math.max(0,Math.min(1,(ct-5.8)/5.4));
    const fall=1-sstep(0.10+ri*0.22,0.56+ri*0.22,rD);
    return rise*fall;
  }
  g.userData.update=function(t,k,ct){
    for(let ri=0;ri<3;ri++){
      const env=ct<0?0:envRow(ri,ct);
      const flick=0.82+0.18*Math.sin(t*2.2+ri*1.7);
      mats[ri].opacity=k*rows[ri].op*env*flick;
      if(ri===1)flags.forEach(function(f){
        f.mat.opacity=k*0.40*env*(0.74+0.26*Math.sin(t*1.7+f.ph));
        f.m.rotation.y=0.24*Math.sin(t*1.6+f.ph);
      });
    }
  };
  return {g:g,update:g.userData.update,env:envRow,mats:mats};
}

/* 诗人（杜牧）：全诗贯穿的同一造型（青衫落拓、幞头；每次 build 新建材质） */
function twPoet(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x3a4048,belt:0x6a5a34,skin:0xd3b294,collar:0x8a94a2,
    hair:0x12161e,hat:'幞头',rimC:0xb8906a,rim:0.42,noProp:true,scale:scale===undefined?1.6:scale});
}

/* 江水（水面原型）：着色器入 fogShaders 雾同步；每境显式配色（avoid 默认色残留）；
   uMoonDir 对准月位（月悬 -x 上空）——月光光路另由 makeYueGuangJS 的江面光带 sprite 补足 */
function twWater(o){
  const water=makeWater(Object.assign({size:620,seg:96,amp:0.14,freq:0.12,speed:0.26,
    flow:[0.16,0.04],spec:1.30,deep:0x181108,shallow:0x362510,skyc:0x463014,
    moonDir:[-0.44,0.55,-0.72]},o||{}));
  water.mesh.position.set(0,-0.55,-120);
  return water;
}

/* —— 月光江面 makeYueGuangJS(o)：月位正下方的江面光路（一列竖长加性 sprite，fog:false，
   初值=峰值，逐帧乘 k 与微闪包络 ≤1，fadeK 合规）——「大江东去」月光可读性的保底 */
function makeYueGuangJS(o){
  o=o||{};
  const g=new THREE.Group(), items=[];
  const xs=o.xs===undefined?[-9.5,-8.6,-7.8,-6.9,-6.0,-5.2]:o.xs;
  const zs=o.zs===undefined?[-68,-60,-52,-44,-36,-29]:o.zs;
  for(let i=0;i<Math.min(xs.length,zs.length);i++){
    const op0=0.10-0.011*i;
    const m=new THREE.SpriteMaterial({map:glowTex(),color:0xdcc08c,transparent:true,opacity:op0,
      depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
    const s=new THREE.Sprite(m);
    s.scale.set(2.6+0.5*i,7.5+2.2*i,1);
    s.position.set(xs[i],0.5,zs[i]);
    s.renderOrder=2; g.add(s);
    items.push({m:m,op0:op0,ph:i*1.7});
  }
  g.userData.update=function(t,k){
    for(let i=0;i<items.length;i++){
      const it=items[i];
      it.m.opacity=k*it.op0*(0.78+0.22*Math.sin(t*0.9+it.ph));
    }
  };
  return {g:g,update:g.userData.update};
}

/* 江雾两层：水线横雾（贴水面）+ 远景大雾 */
function twMist(seed,op){
  const m1=makeMist({n:4,spread:[190,6,40],pos:[0,1.2,-48],scale:44,color:0x362716,op:op===undefined?0.07:op});
  const m2=makeMist({n:5,spread:[215,12,74],pos:[0,3.4,-62],scale:60,color:0x2c2012,op:0.10});
  return {g:(function(){const gg=new THREE.Group(); gg.add(m1.g); gg.add(m2.g); return gg;})(),
    update:function(t,k){ m1.update(t,k); m2.update(t,k); }};
}

function bCover(){ // 卷首 · 乌江暮色全景：大江东去、江亭断碣、渡口石阶、诗人独立岸畔、对岸江东滩头远岸
  const g=new THREE.Group();
  const water=twWater(); g.add(water.mesh);
  water.mesh.material.uniforms.uMoonColor.value=C(0xe8c890);
  const yue=makeYueGuangJS({}); g.add(yue.g);
  const grd=makeGround({r:76,c1:0x0b0806,c2:0x191108,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,52);
  const yuan=makeYuanShanJS({seed:23321}); yuan.g.position.set(0,0,-170); g.add(yuan.g);
  const an=makeJiangdongAn({seed:23322}); g.add(an.g);
  const tt=makeTantouJS({seed:23341}); g.add(tt);
  const ting=makeJiangTing({}); ting.position.set(-6.5,0,-20); ting.rotation.y=0.14; g.add(ting);
  const jie=makeDuanJie({}); jie.position.set(3.0,0,-12); jie.rotation.y=-0.2; g.add(jie);
  const dk=makeDukou({}); dk.position.set(8.0,-0.28,-18); g.add(dk);
  const poet=twPoet(1.05,'独立'); poet.position.set(6.0,-0.28,3.0); poet.rotation.y=2.55; g.add(poet);
  const mist=twMist(); g.add(mist.g);
  const motes=makeGlow({n:24,box:[170,15,58],pos:[0,8,-8],color:0xd8ac74,size:4.0,speed:0.028,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const flow=makeFlow({n:200,box:[150,10,58],pos:[0,6,-58],color:0x4a3a28,size:16,speed:2.2,maxA:0.07});
  g.add(flow.points);
  const fg1=makeForeground({kind:'芦苇',w:20,n:8,d:5,color:0x070503,seed:23331,sway:0.8,rim:0.09,rimC:0xb8906a});
  fg1.g.position.set(-14,-1.2,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x060402,seed:23332,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(11.5,-1.4,12); g.add(fg2.g);
  addLights(g,{c:0xd8a870,i:0.40,p:[-46,52,-40]},{c:0x2c2118,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0); an.update(t,0); grd.update();
    yue.update(t,k); poet.update(t,k); mist.update(t,k); motes.update(t); flow.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bRenchin(){ // 壹 · 忍耻男儿 —— 胜败兵家事不期，包羞忍耻是男儿：
                     // 暮色沉江，江亭无言、断碣题诗，渡口石阶没入江水——立「忍辱」之论
  const g=new THREE.Group();
  const water=twWater(); g.add(water.mesh);
  water.mesh.material.uniforms.uMoonColor.value=C(0xe8c890);
  const yue=makeYueGuangJS({}); g.add(yue.g);
  const grd=makeGround({r:76,c1:0x0b0806,c2:0x1a1109,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,52);
  const yuan=makeYuanShanJS({seed:23323}); yuan.g.position.set(-4,0,-172); g.add(yuan.g);
  const an=makeJiangdongAn({seed:23324}); g.add(an.g);
  const tt=makeTantouJS({seed:23342}); g.add(tt);
  const ting=makeJiangTing({scale:1.15,rim:0.18}); ting.position.set(-5.5,0,-19); ting.rotation.y=0.10; g.add(ting);
  const jie=makeDuanJie({scale:1.1,rim:0.18}); jie.position.set(3.4,0,-11); jie.rotation.y=-0.24; g.add(jie);
  const dk=makeDukou({}); dk.position.set(8.5,-0.28,-16); g.add(dk);
  const poet=twPoet(1.5,'独立'); poet.position.set(6.6,-0.28,-0.5); poet.rotation.y=2.72; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.0,w:7,d:4,color:0x0a0705,seed:23333,rim:0.10,rimC:0xb8906a});
  rock.g.position.set(8.2,-1.55,-2.2); g.add(rock.g);
  const mist=twMist(23343,0.10); g.add(mist.g);
  const motes=makeGlow({n:26,box:[180,15,60],pos:[0,8,-8],color:0xd8ac74,size:4.0,speed:0.03,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const flow=makeFlow({n:220,box:[150,10,58],pos:[0,6,-56],color:0x4a3a28,size:16,speed:2.4,maxA:0.08});
  g.add(flow.points);
  const fg1=makeForeground({kind:'芦苇',w:20,n:8,d:5,color:0x070503,seed:23334,sway:0.78,rim:0.09,rimC:0xb8906a});
  fg1.g.position.set(-14,-1.2,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x060402,seed:23335,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(11,-1.4,11.5); g.add(fg2.g);
  addLights(g,{c:0xd8a870,i:0.42,p:[-42,54,-38]},{c:0x2c2118,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); yuan.update(t,0); an.update(t,0); grd.update();
    yue.update(t,k); poet.update(t,k); rock.update(t,k);
    mist.update(t,k); motes.update(t); flow.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bJuantu(){ // 贰（末境·可点击/标志性瞬间）· 卷土重来 —— 江东子弟多才俊，卷土重来未可知：
                    // 入夜隔江悬想：对岸江东隐约，烟尘与江雾之间，假设的历史只等一次点击；
                    // 点击：军阵虚影三列集结（相位错落）→持驻明灭→散入江雾，烟尘上飘终至全无
  const ctl={t:0,clicked:false,on:false,t0:0};
  const g=new THREE.Group();
  const water=twWater({deep:0x130d08,shallow:0x2c1e0d,skyc:0x3a2912,moonDir:[-0.40,0.57,-0.72]});
  g.add(water.mesh);
  water.mesh.material.uniforms.uMoonColor.value=C(0xdccba8);
  const yue=makeYueGuangJS({}); g.add(yue.g);
  const grd=makeGround({r:76,c1:0x0a0705,c2:0x181009,y:-0.30}); g.add(grd.mesh);
  grd.mesh.position.set(0,-0.30,52);
  const yuan=makeYuanShanJS({seed:23325,peaks:5}); yuan.g.position.set(-8,0,-174); g.add(yuan.g);
  const an=makeJiangdongAn({seed:23326}); g.add(an.g);
  const tt=makeTantouJS({seed:23343}); g.add(tt);
  const ting=makeJiangTing({}); ting.position.set(-9.5,0,-26); ting.rotation.y=0.16; g.add(ting);
  const jie=makeDuanJie({}); jie.position.set(-1.5,0,-13); jie.rotation.y=-0.18; g.add(jie);
  const dk=makeDukou({}); dk.position.set(6.0,-0.28,-12); g.add(dk);
  /* 军阵虚影（点击前 visible=false 硬关）+ 烟尘/幽光粒子 + 幽光点灯（初值=峰值，逐帧乘 k 与包络） */
  const jz=makeJunZhen({seed:23311}); jz.g.visible=false; g.add(jz.g);
  const dust=makeGlow({n:56,box:[104,7,14],pos:[0,2.2,-80.5],color:0x6a5a46,size:3.4,speed:0.4,rise:0.5,
    add:false,maxA:0.22});
  g.add(dust.points);
  const motesG=makeGlow({n:44,box:[96,10,12],pos:[0,4.5,-80.5],color:0xc9a26a,size:3.0,speed:0.3,rise:0.2,
    add:true,maxA:0.16});
  g.add(motesG.points);
  const kl=new THREE.PointLight(0xc9a878,1.10,110); kl.position.set(0,7,-80); g.add(kl);
  const poet=twPoet(1.38,'独立'); poet.position.set(10.5,-0.28,-1.0); poet.rotation.y=2.45; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.1,w:8,d:4,color:0x0a0705,seed:23336,rim:0.11,rimC:0xb8906a});
  rock.g.position.set(11.8,-1.55,-3.0); g.add(rock.g);
  const mist=twMist(23344,0.10); g.add(mist.g);
  const motes=makeGlow({n:24,box:[180,15,60],pos:[0,8,-8],color:0xd0ac7c,size:4.0,speed:0.028,rise:0,add:false,maxA:0.07});
  g.add(motes.points);
  const flow=makeFlow({n:240,box:[155,11,60],pos:[0,6.5,-56],color:0x443626,size:16,speed:2.6,maxA:0.08});
  g.add(flow.points);
  const fg1=makeForeground({kind:'芦苇',w:20,n:8,d:5,color:0x070503,seed:23337,sway:0.8,rim:0.09,rimC:0xb8906a});
  fg1.g.position.set(-14,-1.2,12); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:5,color:0x060402,seed:23338,rim:0.09,rimC:0xb8906a});
  fg2.g.position.set(11,-1.4,11); g.add(fg2.g);
  addLights(g,{c:0xc8a880,i:0.36,p:[-46,58,-42]},{c:0x281e14,i:0.52});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const ct=ctl.on?(ctl.t-ctl.t0):-1;
      jz.update(t,k,ct);
      const envMid=ct<0?0:jz.env(1,ct)*(0.82+0.18*Math.sin(t*2.2+1.7));
      dust.mat.uniforms.uMaxA.value=k*0.22*envMid;
      motesG.mat.uniforms.uMaxA.value=k*0.16*envMid;
      kl.intensity=k*1.10*envMid;
      water.update(t); yuan.update(t,0); an.update(t,0); grd.update();
      yue.update(t,k); poet.update(t,k); rock.update(t,k);
      mist.update(t,k); motes.update(t); flow.update(t);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true; ctl.t0=ctl.t;
        jz.g.visible=true;                               // 点击后幻影组才可见（此前硬关）
        setAmbience(0.10);
        pluck(2,0.0,0.10); pluck(4,0.45,0.09); pluck(7,0.95,0.10); pluck(5,1.5,0.08);   // 集结四声
        const fl=$('#flash'); fl.textContent='江东子弟多才俊 卷土重来未可知';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x150e09),hor:C(0x4a2f16),bot:C(0x0b0806),fog:C(0x1a120c),fd:0.0052,star:0.26,
  moon:new THREE.Vector3(-66,74,-184),ms:1.00,mph:0.42,mhaze:0.15,dirC:C(0xd8a870),dirI:0.40,
  dirP:new THREE.Vector3(-50,58,-40),ambC:C(0x2c2118),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,9,44],t:[0,7.2,32],lf:[-6,10.5,-14],lt:[-13,11.5,-42]},
  sky:()=>SK({fd:0.0050,star:0.24,ms:1.00,mph:0.42}) },
{ name:'忍耻男儿',dwell:16,river:0.03,build:bRenchin,
  cam:{f:[0.6,5.4,19],t:[-1.0,4.6,6],lf:[-4,6.0,-14],lt:[-10,6.8,-38]},
  sky:()=>SK({fd:0.0054,star:0.30,ms:1.00,mph:0.66,mhaze:0.16,
    moon:new THREE.Vector3(-66,76,-184),dirC:C(0xd8a870),dirI:0.40,
    dirP:new THREE.Vector3(-50,58,-40),ambC:C(0x2c2118),ambI:0.56}) },
{ name:'卷土重来',dwell:19,river:0.03,build:bJuantu,
  cam:{f:[1.0,6.2,17],t:[-1.2,4.2,-6],lf:[-4,6.0,-14],lt:[-12,7.0,-46]},
  sky:()=>SK({fd:0.0052,star:0.55,ms:1.15,mph:0.58,mhaze:0.12,
    moon:new THREE.Vector3(-60,84,-188),dirC:C(0xc8a880),dirI:0.36,
    dirP:new THREE.Vector3(-46,62,-42),ambC:C(0x281e14),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('tiwujiangting.py —— 被 build.py 消费：python build.py tiwujiangting')
