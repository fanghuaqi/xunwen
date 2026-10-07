# -*- coding: utf-8 -*-
"""wuyi.py —— 《无衣》（先秦·诗经·秦风，queue no.257，大漠金戈）生成配置
3 境（三章一境，重章叠句一章一境）：
境壹同袍同仇（标志性瞬间：岂曰无衣与子同袍——拂晓大漠营盘，王旗初展，军士并肩整甲列阵，
  主将振臂誓师，戈矛成架，修我戈矛与子同仇）、
境贰同泽偕作（日暮修备：锻炉火光，矛戟成架，军士整甲扶兵，与子偕作）、
境叁同裳偕行（末境可点击：点击共修甲兵——鼓声三通，戈矛林立同举，兵刃寒光次第点亮）。
美术立意「同袍三誓，戈矛同举」：三章重章叠句 = 三境变奏——
时间递进（拂晓誓师→日暮修备→夜火出征，晨光→暮色→星火）、
兵器递修（戈矛→矛戟→甲兵，架上之兵与手中之兵同步递进）、
誓言递进（同仇→偕作→偕行）。大漠金戈全套色板（bg #120d08、雾 #180f08～#1c130a 系、
文字 #f0e2cc，accent=#b8905a 只落在 UI/人物边缘光/兵刃寒光/旗面光边/炉火光晕上，禁艳金）。
与已有边塞页第一眼可区分：不做密林夜射白羽（saixiaqu-linan）、不做雪原听笛戍楼（saishang-chuidi）、
不做行军出关（congjunxing-yuben）、不做战阵残垣——本页是**战前誓师的并肩整甲群像**：
军士低模列阵 + 王旗 + 战鼓 + 兵器架 + 火把，无战斗无残垣，只有整肃与慷慨。
自建 builder：makeChangbingWY（长兵：矛/戈/戟，握点枢轴可举起）/ makeShizuRowWY（军士低模一排）/
makeBingjiaWY（兵器架）/ makeJiajiaWY（甲架）/ makeWangqiWY（王旗）/ makeZhanguWY（战鼓）/
makeHuobaWY（火把）/ makeDamoWY（大漠营盘基底）。
考点钉子：泽 zé（贴身内衣）/ 戟 jǐ / 偕 xié / 裳 cháng（小测第 3 题落点）；
《诗经》重章叠句与秦风慷慨从军（第 4 题）；「与子同袍」袍泽之义与同仇敌忾（第 5 题）。
多音字：兴师 xīng、裳 cháng、偕 xié、仇 chóu、戟 jǐ、曰 yuē（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='wuyi', title='无衣', dyn='先秦 · 诗经', brand_author='诗 经',
    gold_rgb='184,144,90',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b8905a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(184,144,90,.3);
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
    tip='轻点画面 / 按空格 —— 王于兴师，修我甲兵，戈矛同举',
    hint='← → 键或空格逐境游览 · 末境可点击画面：共修甲兵——鼓声三通，戈矛林立同举',
    cover_read='无衣。先秦，诗经。岂曰无衣？与子同袍。王于兴师，修我戈矛。与子同仇！',
    cover_p1='三重意境，随诗句次第展开：谁说没有衣裳？愿与你同披一件战袍——拂晓的大漠营盘上，王旗初展，军士并肩整甲列阵，修我戈矛，同仇敌忾；日暮的锻炉旁火光四起，矛戟修成，与你一同奋起；出征前夜火把通明，甲兵齐整——鼓声三通，戈矛林立同举，与你偕行，共赴国难。',
    cover_p2='边读诗，边走进两千多年前秦地的战前誓师：三章一问一答，衣从袍到泽到裳，兵从戈矛到矛戟到甲兵，心从同仇到偕作到偕行——读懂这层层递进的重章叠句，就读懂了「袍泽」二字的分量，也读懂了秦风慷慨从军的浩然之气。',
    end_h2='同袍 · 偕行', cn_word='叁',
    words_js="['再赴一场，秦风誓师','初识诗经，尚需共读','渐入诗境，再诵几遍','同仇渐炽，偕作已起','已解重章叠唱之妙','修我甲兵，与子偕行']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'同袍同仇', jing:'谁说没有衣裳？愿与你同披一件战袍。君王要起兵出征，快快修整我们的戈与矛——与你同仇敌忾！（誓师 · 战袍 · 戈矛 · 同仇）（标志性瞬间：拂晓大漠营盘，王旗初展，军士并肩整甲列阵，主将振臂誓师）',
  segs:[
   {c:'岂曰无衣？', p:py('qǐ yuē wú yī')},
   {c:'与子同袍。', p:py('yǔ zǐ tóng páo')},
   {c:'王于兴师，', p:py('wáng yú xīng shī')},
   {c:'修我戈矛。', p:py('xiū wǒ gē máo')},
   {c:'与子同仇！', p:py('yǔ zǐ tóng chóu')}],
  read:'岂曰无衣？与子同袍。王于兴师，修我戈矛。与子同仇！',
  yisi:'谁说没有衣裳？愿与你同披一件战袍。君王要起兵出征，快快修整我们的戈与矛，与你同仇敌忾！——首章以反问劈空而起：「岂曰无衣」不是真的没有衣，而是秦地军士相邀共赴国难的慷慨之言；「与子同袍」把有限的衣装与无限的情谊合在一处，战友之义自此有了名字。「王于兴师」点明缘由：国难当头，王师即出；「修我戈矛」是行动——磨刃理弦、人人整装；「与子同仇」是心魂——劲往一处使，敌忾同一心。反问起、誓言结，慷慨淋漓，是真正的「军歌」气象。',
  zhu:[['无衣','「岂曰无衣」：谁说没有衣裳？一说秦地军士衣装不足，故有「无衣」之问，而以「同袍」相励——衣可同、难可同，慷慨自见'],['岂曰','难道说、谁说——反问起势，斩钉截铁。岂，读 qǐ；曰，说，读 yuē'],['袍','长衣，即战袍，白天当衣、夜里当被。与子同袍：愿与你同披一件战袍——成语「袍泽之谊」即源于此二句'],['王于兴师','君王要起兵出征。于，语助词；兴师，起兵、发动军队。兴，读 xīng（兴起、发动），不读 xìng'],['修我戈矛','修整好我们的戈与矛。修，修整、磨砺——一个「我」字，把国之兵器说成自家之事，同袍一体之情尽在其中'],['戈矛','戈，横刃长柄、可钩可啄的古兵器；矛，直刃长杆的刺兵——并指各类长兵器。戈，读 gē；矛，读 máo'],['同仇','同心合力争同一敌人，即「同仇敌忾」。《秦风·无衣》正是「同仇」二字的出处。仇，读 chóu']] },
{ name:'同泽偕作', jing:'谁说没有衣裳？愿与你同穿一件贴身汗衣。君王要起兵出征，快快修整我们的矛与戟——与你一同奋起！（整甲 · 矛戟 · 偕作）',
  segs:[
   {c:'岂曰无衣？', p:py('qǐ yuē wú yī')},
   {c:'与子同泽。', p:py('yǔ zǐ tóng zé')},
   {c:'王于兴师，', p:py('wáng yú xīng shī')},
   {c:'修我矛戟。', p:py('xiū wǒ máo jǐ')},
   {c:'与子偕作！', p:py('yǔ zǐ xié zuò')}],
  read:'岂曰无衣？与子同泽。王于兴师，修我矛戟。与子偕作！',
  yisi:'谁说没有衣裳？愿与你同穿一件贴身的汗衣。君王要起兵出征，快快修整我们的矛与戟，与你一同奋起！——次章只换数字而情谊更进一层：「泽」是贴身之内衣，比「袍」更贴身一层，同穿之谊也更亲一层；「矛戟」是戈矛合一的精利长兵，比「戈矛」更进一层，武备愈修愈精；「偕作」由「同仇」的同心更进一步——不止心齐，更要一齐行动起来。重章不是简单重复：衣愈贴、兵愈利、行愈急，赴战的慷慨一层紧似一层。',
  zhu:[['泽','贴身内衣（汗衫），通「襗」，读 zé——不是沼泽。从「同袍」到「同泽」，同穿之衣贴身愈近，共赴之情愈深'],['矛戟','戟，将戈与矛合为一体的长兵器，既可钩啄又可直刺，读 jǐ。兵器由「戈矛」修至「矛戟」，见武备愈修愈精'],['偕作','一同奋起行动。偕，一同、一起，读 xié；作，起、行动起来——「同仇」是心，「偕作」是行'],['重章叠句','《诗经》常见章法：各章句式全同、只换少数字，反复咏唱而层层递进——本诗三章「袍／泽／裳」「戈矛／矛戟／甲兵」「同仇／偕作／偕行」三组递进正是典范']] },
{ name:'同裳偕行', jing:'谁说没有衣裳？愿与你同穿一件下衣。君王要起兵出征，快快修整我们的铠甲兵器——与你并肩同行！（出征 · 甲兵 · 偕行 · 末境点击画面：共修甲兵——鼓声三通，戈矛林立同举）',
  segs:[
   {c:'岂曰无衣？', p:py('qǐ yuē wú yī')},
   {c:'与子同裳。', p:py('yǔ zǐ tóng cháng')},
   {c:'王于兴师，', p:py('wáng yú xīng shī')},
   {c:'修我甲兵。', p:py('xiū wǒ jiǎ bīng')},
   {c:'与子偕行！', p:py('yǔ zǐ xié xíng')}],
  read:'岂曰无衣？与子同裳。王于兴师，修我甲兵。与子偕行！',
  yisi:'谁说没有衣裳？愿与你同穿一件下衣。君王要起兵出征，快快修整我们的铠甲兵器，与你并肩同行！——末章收束全篇：「裳」是下衣，至此袍、泽、裳上下俱同，同袍之义已无处不在；「甲兵」是铠甲与兵器的总称，武备修至最全；「偕行」由「偕作」的行动再进一步——一齐开拔、并肩上阵。从同仇（同心）到偕作（同起）到偕行（同行），三章层层递进如战鼓三通：一通誓师、二通修备、三通出征。慷慨从军的秦风之气，至此推向顶点。',
  zhu:[['裳','下衣、战裙，读 cháng（不读轻声 shang）——从袍到泽到裳，衣之上下俱同，同袍之义无处不在'],['甲兵','铠甲与兵器，泛指武器装备。修我甲兵：甲胄鲜明、兵刃犀利，只待出征'],['偕行','一同前往、并肩上阵。行，读 xíng——由「同仇」而「偕作」而「偕行」，同心、同起、同行，层层递进至并肩赴战'],['秦风与慷慨从军','《诗经》十五国风之一，秦地民风尚武，诗风慷慨激昂。《无衣》是秦人的战歌：闻王师兴而修兵同袍，正合「岂曰无衣，与子同袍」的慷慨气概，被誉为最早的军歌之一'],['袍泽','「与子同袍」「与子同泽」——后世遂以「袍泽」代称战友、军中同僚之谊，其源即在本诗']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「岂曰无衣？与子同袍。」的下一句是？', o:['王于兴师，修我戈矛','岂曰无衣？与子同泽','王于兴师，修我甲兵'], a:0},
 {q:'「王于兴师，修我矛戟。」的下一句是？', o:['与子同仇！','与子偕作！','与子偕行！'], a:1},
 {q:'「与子同泽」「修我矛戟」「与子偕作」中加点字的读音和解释，全都正确的一项是？', o:['泽读 zé，贴身内衣（汗衫）；戟读 jǐ，戈矛合一的长兵器；偕读 xié，一同、一起——同穿贴身之衣，共修精利之兵，一齐奋起','泽读 yì，光泽；戟读 jí，短剑；偕读 jiē，皆、都——衣服光洁、短剑锋利、人人都到','泽读 zé，沼泽；戟读 jǐ，弓箭；偕读 xié，和谐——蹚过沼泽、挽弓搭箭、军容和谐'], a:0},
 {q:'本诗三章句式全同，只换「袍／泽／裳」「戈矛／矛戟／甲兵」「同仇／偕作／偕行」等词。对这种手法与《诗经·秦风》的理解，正确的一项是？', o:['顶真——上句的结尾作下句的开头，词句蝉联而下，气脉紧连','排比——三章平行罗列战前准备的各种事项，只为铺陈场面热闹','重章叠句——回环往复、层层递进：衣愈贴（袍→泽→裳）、兵愈利（戈矛→矛戟→甲兵）、行愈急（同仇→偕作→偕行），秦风慷慨激昂，正是一首赴战的「军歌」'], a:2},
 {q:'「岂曰无衣？与子同袍」两千多年来读来令人热血。对这一句的理解，最恰当的一项是？', o:['诗人衣衫单薄，向朋友借衣过冬，写的是冬日的贫困与互助','写战士们衣服破旧无人缝补，意在讽刺军中后勤不力','谁说没有衣裳？愿与你同披一件战袍——战友间患难与共、慷慨相助，「袍泽」从此成为战友的代称；全诗洋溢着同仇敌忾、共赴国难的豪情'], a:2},
];
"""

SCENES_JS = """/* ================= 无衣 · 三境场景（大漠金戈·战前誓师：同袍同仇、同泽偕作、同裳偕行） =================
   美术立意：「同袍三誓，戈矛同举」——大漠营盘上的战前誓师群像：
   三章重章叠句 = 三境变奏——时间递进（拂晓誓师→日暮修备→夜火出征）、
   兵器递修（戈矛→矛戟→甲兵）、誓言递进（同仇→偕作→偕行）。
   accent=#b8905a 只落在 UI/人物边缘光/兵刃寒光/旗面光边/炉火光晕上，禁艳金。
   与已有边塞页第一眼可区分：不做密林夜射（saixiaqu）、不做雪原听笛（saishang）、
   不做行军出关、不做战阵残垣——本页是**战前誓师的并肩整甲群像**：
   军士低模列阵、王旗、战鼓、兵器架、火把，无战斗无残垣，只有整肃与慷慨。
   末境点击（共修甲兵·戈矛林立同举）：鼓声三通，长兵自握点逐支举起成林，
   兵刃寒光次第点亮，火星腾起，题字「修我甲兵 与子偕行」同现，可反复点击（收而复举）。 */

/* —— 长兵 makeChangbingWY(o)：单支长兵（type:'mao'矛|'ge'戈|'ji'戟），枢轴在握点 y=0，
   兵刃朝上，rest 斜倚、举起渐归竖直（「戈矛林立同举」）；头部 accent 寒光 sprite（举起后段点亮）
   update(t,k,raise)：raise 0..1 = 举起度；寒光/微颤每帧写必乘 fadeK（初值=峰值） */
function makeChangbingWY(o){
  o=o||{};
  const type=o.type===undefined?'mao':o.type, L=o.L===undefined?3.3:o.L;
  const g=o.g===undefined?0.28:o.g;                       /* 握点距底比例 */
  const rest=o.rest===undefined?0.20:o.rest, up=o.up===undefined?-0.07:o.up;
  const B=new GeoBag();
  const yTop=(1-g)*L, yBot=-g*L;
  const sha=new THREE.CylinderGeometry(0.026,0.038,L,6);
  sha.translate(0,(yTop+yBot)/2,0); B.put(sha,0x4a3820);
  const rope=new THREE.CylinderGeometry(0.042,0.042,g*L*0.55,5);
  rope.translate(0,yBot+g*L*0.27,0); B.put(rope,0x33240f);
  const headY=yTop;
  if(type==='mao'||type==='ji'){
    const mh=new THREE.ConeGeometry(0.075,0.46,6);
    mh.translate(0,headY+0.22,0); B.put(mh,0x7a6a44);
    const ys=new THREE.ConeGeometry(0.055,0.16,5);        /* 红缨座 */
    ys.translate(0,headY-0.06,0); B.put(ys,0x7a2e1e);
  }
  if(type==='ge'||type==='ji'){
    const hy=headY-(type==='ji'?0.34:0.10);
    const yuan=new THREE.ConeGeometry(0.052,0.40,5);      /* 戈援（横刃） */
    yuan.rotateZ(-Math.PI/2); yuan.scale(1,1,0.45);
    yuan.translate(0.20,hy,0); B.put(yuan,0x7a6a44);
    const nei=new THREE.BoxGeometry(0.16,0.07,0.05);      /* 内 */
    nei.translate(-0.14,hy,0); B.put(nei,0x6a5a38);
  }
  const g2=new THREE.Group();
  g2.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x8a7448,emissive:0x080502}),{c:0xb8905a,i:o.rim===undefined?0.22:o.rim,p:2.8})));
  const glint=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8b070,
    transparent:true,opacity:0.85,depthWrite:false,blending:THREE.AdditiveBlending,fog:false}));
  glint.scale.set(1.15,1.15,1); glint.position.set(0,headY+0.30,0); glint.renderOrder=4; g2.add(glint);
  const ph=(o.seed===undefined?25701:o.seed)%6.283;
  g2.update=function(t,k,raise){
    const kk=k===undefined?1:k, r=raise===undefined?0:raise;
    g2.rotation.z=rest*(1-r)+up*r+0.012*Math.sin(t*0.9+ph)*kk;
    glint.material.opacity=kk*0.85*Math.max(0,(r-0.72)/0.28)*(0.72+0.28*Math.sin(t*3.1+ph));
  };
  g2.userData.update=g2.update;
  return g2;
}

/* —— 军士一排 makeShizuRowWY(o)：先秦军士低模一排（长衣+皮甲护肩+圆盔，GeoBag 分 k 组合批），
   pose:'执兵'（双手斜前扶兵位，长兵由 makeChangbingWY 另行对位挂载）|'整甲'（左手抚甲、右手扶兵）
   o.xs 给定列位（局部 x 数组，与外部长兵对位）、o.jz 纵深抖动（默认 0.7；执兵排传 0 保证对位）
   返回 {g}：阵列肃立（不动，长兵对位不漂移） */
function makeShizuRowWY(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25711:o.seed);
  const n=o.n===undefined?5:o.n, k=o.k===undefined?2:o.k;
  const w=o.w===undefined?14.5:o.w, s=o.s===undefined?1.35:o.s;
  const pose=o.pose===undefined?'执兵':o.pose, jz=o.jz===undefined?0.7:o.jz;
  const xs=o.xs===undefined?(function(a){for(let i=0;i<n;i++)a.push(-w/2+w*(i+0.5)/n);return a;}([])):o.xs;
  const bags=[],meshes=[];
  for(let i=0;i<k;i++)bags.push(new GeoBag());
  for(let i=0;i<n;i++){
    const B=bags[i%k];
    const x=xs[i]||0, zz=(R()-0.5)*jz;
    const robe=[0x2b2114,0x31261a,0x271e12,0x2e2314][Math.floor(R()*4)];
    const dk=shadeColor(robe,0.72);
    const bd=new THREE.CylinderGeometry(0.30,0.54,1.58,7);
    bd.translate(x,0.79,zz); B.put(bd,robe);                        /* 长衣 */
    const jia=new THREE.CylinderGeometry(0.40,0.455,0.46,7);
    jia.translate(x,1.12,zz); B.put(jia,0x3a2c1a);                  /* 皮甲 */
    for(let sd=0;sd<2;sd++){                                        /* 护肩 */
      const sh=new THREE.SphereGeometry(0.13,6,5);
      sh.scale(1.15,0.7,1); sh.translate(x+(sd?0.42:-0.42),1.38,zz);
      B.put(sh,0x443420);
    }
    const hd=new THREE.SphereGeometry(0.165,7,6);
    hd.translate(x,1.72,zz); B.put(hd,0x8a6a48);                    /* 面部 */
    const kh=new THREE.SphereGeometry(0.19,7,5,0,Math.PI*2,0,Math.PI/2);
    kh.scale(1,0.92,1); kh.translate(x,1.70,zz); B.put(kh,0x26201a); /* 圆盔 */
    const kn=new THREE.ConeGeometry(0.035,0.10,5);
    kn.translate(x,1.92,zz); B.put(kn,0x6a5232);                    /* 盔缨座 */
    if(pose==='整甲'){
      B.put(limbGeo([x-0.40,1.34,zz],[x-0.10,1.16,zz+0.28],0.075,0.055,5),dk); /* 左手抚甲 */
      B.put(limbGeo([x+0.40,1.34,zz],[x+0.12,0.93,zz+0.50],0.075,0.055,5),dk); /* 右手扶兵 */
    }else{
      B.put(limbGeo([x-0.40,1.34,zz],[x-0.12,1.06,zz+0.50],0.075,0.055,5),dk); /* 扶兵上 */
      B.put(limbGeo([x+0.40,1.34,zz],[x+0.12,0.80,zz+0.50],0.075,0.055,5),dk); /* 扶兵下 */
    }
  }
  const g=new THREE.Group();
  for(let i=0;i<k;i++){
    const m=bags[i].mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,
      shininess:6,specular:0x2a2014,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.16:o.rim,p:2.2}));
    g.add(m); meshes.push(m);
  }
  g.scale.setScalar(s);
  return g;
}

/* —— 兵器架 makeBingjiaWY(o)：木架（双柱+横梁+斜撑）+ 数支长兵倚立（type:'ge'|'mao'|'ji'|'mix'）
   ——「修我戈矛／矛戟」 */
function makeBingjiaWY(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25721:o.seed);
  const w=o.w===undefined?4.6:o.w, hh=o.h===undefined?2.5:o.h;
  const B=new GeoBag();
  for(let sd=0;sd<2;sd++){
    const px=sd?w/2:-w/2;
    const post=new THREE.CylinderGeometry(0.09,0.12,hh,6);
    post.translate(px,hh/2,0); B.put(post,0x2e2114);
    const brace=new THREE.CylinderGeometry(0.055,0.07,hh*0.62,5);
    brace.rotateZ(sd?-0.5:0.5); brace.translate(px+(sd?-0.5:0.5),hh*0.28,0); B.put(brace,0x241a0e);
  }
  const beam=new THREE.BoxGeometry(w+0.5,0.14,0.16);
  beam.translate(0,hh-0.1,0); B.put(beam,0x33251a);
  const n=o.n===undefined?5:o.n, type=o.type===undefined?'mao':o.type, L=o.L===undefined?3.9:o.L;
  for(let i=0;i<n;i++){
    const x=-w/2+w*(i+0.5)/n+(R()-0.5)*0.22;
    const tp=(type==='mix')?(i%2?'mao':'ge'):type;
    const ll=L*(0.92+R()*0.16), topY=0.12+ll;
    const shaft=new THREE.CylinderGeometry(0.026,0.036,ll,5);
    shaft.translate(x,0.12+ll/2,0.10); B.put(shaft,0x44341e);
    if(tp==='ge'){
      const yuan=new THREE.ConeGeometry(0.05,0.36,5);
      yuan.rotateZ(-Math.PI/2); yuan.scale(1,1,0.45);
      yuan.translate(x+0.18,topY-0.12,0.10); B.put(yuan,0x7a6a44);
    }else{
      const mh=new THREE.ConeGeometry(0.07,0.42,6);
      mh.translate(x,topY+0.20,0.10); B.put(mh,0x7a6a44);
      if(tp==='ji'){
        const yuan=new THREE.ConeGeometry(0.05,0.34,5);
        yuan.rotateZ(-Math.PI/2); yuan.scale(1,1,0.45);
        yuan.translate(x+0.17,topY-0.10,0.10); B.put(yuan,0x7a6a44);
      }else{
        const ys=new THREE.ConeGeometry(0.055,0.15,5);
        ys.translate(x,topY-0.05,0.10); B.put(ys,0x7a2e1e);
      }
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2c1a,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.16:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1.1:o.scale);
  return g;
}

/* —— 甲架 makeJiajiaWY(o)：木架上一领甲衣（钟形甲壳+护肩+圆盔），合批 1 mesh ——「修我甲兵」 */
function makeJiajiaWY(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?25731:o.seed);
  const n=o.n===undefined?2:o.n, w=o.w===undefined?3.2:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=-w/2+w*(i+0.5)/n;
    const post=new THREE.CylinderGeometry(0.08,0.11,1.7,6);
    post.translate(x,0.85,0); B.put(post,0x2e2114);
    const cross=new THREE.CylinderGeometry(0.06,0.08,1.1,5);
    cross.rotateZ(Math.PI/2); cross.translate(x,1.7,0); B.put(cross,0x241a0e);
    const pts=[[0.02,0],[0.34,0.06],[0.40,0.34],[0.37,0.62],[0.30,0.84],[0.20,0.98],[0.10,1.04]]
      .map(function(p){ return new THREE.Vector2(p[0],p[1]); });
    const shell=new THREE.LatheGeometry(pts,10);
    shell.scale(1.22,1.15,0.92); shell.translate(x,1.76,0); B.put(shell,0x3a2c1a);  /* 甲衣 */
    for(let sd=0;sd<2;sd++){
      const sh=new THREE.SphereGeometry(0.15,6,5);
      sh.scale(1.2,0.65,1); sh.translate(x+(sd?0.40:-0.40),2.60,0); B.put(sh,0x443420);
    }
    const kh=new THREE.SphereGeometry(0.185,7,5,0,Math.PI*2,0,Math.PI/2);
    kh.scale(1,0.92,1); kh.translate(x,2.84,0); B.put(kh,0x26201a);              /* 盔 */
    const kn=new THREE.ConeGeometry(0.04,0.12,5);
    kn.translate(x,3.08,0); B.put(kn,0x6a5232);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2c1a,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.16:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1.15:o.scale);
  return g;
}

/* —— 王旗 makeWangqiWY(o)：高杆王旗（旗杆+铜顶+玄色旗面顶点波动+accent 光边顶点色）
   update(t,k,wind)：wind 风力（点击同举时增强）——「王于兴师」 */
function makeWangqiWY(o){
  o=o||{};
  const H=o.H===undefined?11:o.H, W=o.W===undefined?4.4:o.W, Hh=o.Hh===undefined?2.4:o.Hh;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.075,0.11,H,7);
  pole.translate(0,H/2,0); B.put(pole,0x342413);
  const fin=new THREE.ConeGeometry(0.13,0.42,6);
  fin.translate(0,H+0.20,0); B.put(fin,0x8a6a3a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x6a5232,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.22:o.rim,p:2.6})));
  const geo=new THREE.PlaneGeometry(W,Hh,10,4);
  geo.translate(W/2+0.06,0,0);
  const base=geo.attributes.position.array.slice();
  const cnt=geo.attributes.position.count, cols=new Float32Array(cnt*3);
  const cb=new THREE.Color(0x241610), ca=new THREE.Color(0xb8905a);
  for(let i=0;i<cnt;i++){
    const y=base[i*3+1];
    const t=Math.max(0,((y+Hh/2)/Hh-0.72)/0.28);            /* 顶边 28% 渐入 accent 光边 */
    const c=cb.clone().lerp(ca,t*0.85);
    cols[i*3]=c.r; cols[i*3+1]=c.g; cols[i*3+2]=c.b;
  }
  geo.setAttribute('color',new THREE.BufferAttribute(cols,3));
  const flag=new THREE.Mesh(geo,new THREE.MeshLambertMaterial({color:0xffffff,vertexColors:true,
    side:THREE.DoubleSide,emissive:0x140b05}));
  flag.position.y=H-Hh/2-0.55; g.add(flag);
  const pos=geo.attributes.position;
  const ph=(o.seed===undefined?25751:o.seed)%6.283;
  g.userData.update=function(t,k,wind){
    const wd=wind===undefined?1:wind;
    for(let i=0;i<pos.count;i++){
      const bx=base[i*3], by=base[i*3+1], f=bx/W;
      pos.array[i*3+2]=Math.sin(bx*1.5-t*3.4+by*0.9+ph)*0.34*f*f*wd;
      pos.array[i*3+1]=by-Math.abs(Math.sin(bx*1.2-t*2.6+ph))*0.10*f*f*wd;
    }
    pos.needsUpdate=true;
  };
  return g;
}

/* —— 战鼓 makeZhanguWY(o)：大鼓横置木架（鼓身+双鼓面+鼓钉+鼓绳+四足 X 架，合批 1 mesh；
   sticks:true 加一对搁置的鼓槌）——誓师之鼓 */
function makeZhanguWY(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.88,0.88,1.5,12);
  body.rotateZ(Math.PI/2); body.translate(0,1.42,0); B.put(body,0x4a2c16);
  for(let sd=0;sd<2;sd++){
    const face=new THREE.CylinderGeometry(0.92,0.92,0.06,12);
    face.rotateZ(Math.PI/2); face.translate(sd?0.78:-0.78,1.42,0); B.put(face,0x2a1810);
    for(let i=0;i<8;i++){
      const a=i/8*Math.PI*2;
      const stud=new THREE.SphereGeometry(0.045,5,4);
      stud.translate(sd?0.80:-0.80,1.42+Math.sin(a)*0.90,Math.cos(a)*0.90);
      B.put(stud,0x8a6238);
    }
  }
  for(let i=0;i<6;i++){
    const a=i/6*Math.PI*2;
    B.put(limbGeo([0.70,1.42+Math.sin(a)*0.86,Math.cos(a)*0.86],
                  [-0.70,1.42+Math.sin(a)*0.86,Math.cos(a)*0.86],0.022,0.022,4),0x1e120a);
  }
  for(let sd=0;sd<2;sd++){
    for(let p2=0;p2<2;p2++){
      const px=sd?0.95:-0.95, pz=p2?0.55:-0.55;
      B.put(limbGeo([px-0.30,0,pz],[px+0.30,2.1,pz],0.07,0.055,5),0x241a0e);
      B.put(limbGeo([px+0.30,0,pz],[px-0.30,2.1,pz],0.07,0.055,5),0x241a0e);
    }
  }
  if(o.sticks){
    const st1=new THREE.CylinderGeometry(0.035,0.045,1.3,5);
    st1.rotateZ(Math.PI/2-0.12); st1.translate(-0.1,2.42,0.15); B.put(st1,0x5a4024);
    const st2=new THREE.CylinderGeometry(0.035,0.045,1.3,5);
    st2.rotateZ(Math.PI/2+0.16); st2.translate(0.15,2.44,-0.18); B.put(st2,0x5a4024);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x5a4024,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.18:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 火把 makeHuobaWY(o)：木杆+油碗+焰体（makeFlame）+光晕，夜境列火 ——「王于兴师」夜火 */
function makeHuobaWY(o){
  o=o||{};
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.055,0.085,2.7,6);
  pole.translate(0,1.35,0); B.put(pole,0x241a0e);
  const bowl=new THREE.CylinderGeometry(0.20,0.12,0.22,7);
  bowl.translate(0,2.78,0); B.put(bowl,0x3a2c1a);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a2014,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  const fl=makeFlame({h:o.fh===undefined?0.85:o.fh,w:0.24,planes:2,embers:8,spark:false,wide:0.28,
    light:o.light===undefined?0.9:o.light,lightD:o.lightD===undefined?24:o.lightD});
  fl.g.position.set(0,3.02,0); g.add(fl.g);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd88a48,
    transparent:true,opacity:0.14,depthWrite:false}));
  glow.scale.set(5,5,1); glow.position.set(0,3.1,0); g.add(glow);
  const ph=(o.seed===undefined?25741:o.seed)%6.283;
  g.userData.update=function(t,k){
    const kk=k===undefined?1:k;
    fl.update(t,kk);
    glow.material.opacity=kk*0.14*(0.82+0.18*Math.sin(t*2.6+ph));
  };
  return g;
}

/* —— 大漠营盘基底 makeDamoWY(o)：斑驳营地地面 + 两层台地远山 + 沙尘横流
   远山放 z≈-108/-62，在骨架常驻远山环（z≈-260…-330）之前，不被遮挡 */
function makeDamoWY(o){
  o=o||{};
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:o.c1===undefined?0x140e07:o.c1,c2:o.c2===undefined?0x241808:o.c2,y:-1.8});
  g.add(grd.mesh);
  const ridge=makeRange({r:300,h:o.h1===undefined?17:o.h1,layers:2,peaks:o.p1===undefined?4:o.p1,
    seed:o.seed1===undefined?25751:o.seed1,color:0x0d0906,atmo:0x2e2114,fogK:0.62,glowK:0.06,
    glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-16,0,-108); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:240,h:o.h2===undefined?11:o.h2,layers:2,peaks:3,
    seed:o.seed2===undefined?25752:o.seed2,color:0x0a0704,atmo:0x2e2114,fogK:0.58,glowK:0.04,
    glow:0xd8a860,y:-9,order:-5});
  ridge2.g.position.set(20,0,-62); ridge2.g.rotation.y=Math.PI*0.92; g.add(ridge2.g);
  const dust=makeFlow({n:o.dustN===undefined?330:o.dustN,box:[110,10,44],pos:[0,2.8,-18],
    color:o.dustC===undefined?0x6a5442:o.dustC,size:15,speed:o.dustV===undefined?4.4:o.dustV,
    maxA:o.dustA===undefined?0.11:o.dustA});
  g.add(dust.points);
  return {g:g,grd:grd,ridge:ridge,ridge2:ridge2,dust:dust};
}

/* 誓师主将（贯穿造型系，每次 build 新建材质；pose 可换） */
function wyCommander(scale,pose){
  return makeFigure({pose:pose||'指月',robe:0x33241a,belt:0x8a6238,skin:0xd9b189,collar:0x6a4a28,
    hair:0x1a140c,hat:'发髻',beard:true,rimC:0xb8905a,rim:0.5,noProp:true,scale:scale===undefined?0.85:scale});
}

function bCover(){ // 卷首 · 拂晓大漠营盘全景：王旗初展、军士列阵、戈矛成架、晨尘横流
  const g=new THREE.Group();
  const base=makeDamoWY({}); g.add(base.g);
  const crowd=makeCrowd({n:12,rect:[-34,-96,44,12],seed:25761,color:0x181008,rimC:0xb8905a,rim:0.15,y:-1.8});
  g.add(crowd.mesh);
  const XF=[-4.8,-2.9,-1.0,1.0,2.9,4.8];
  const row=makeShizuRowWY({n:6,w:9.6,xs:XF,jz:0,seed:25762,s:1.05,pose:'执兵',rim:0.12});
  row.position.set(4,-1.78,-44); g.add(row);
  const TF=['ge','mao','ge','mao','ge','mao'];
  const cSpears=[];
  XF.forEach(function(x,i){
    const sp=makeChangbingWY({type:TF[i],rest:(i%2?-0.16:0.18),seed:25790+i,g:0.28,L:3.3,rim:0.14});
    sp.position.set(4+(x+0.08)*1.05,-1.78+0.93*1.05,-44+0.50*1.05);
    sp.scale.setScalar(1.05); g.add(sp); cSpears.push(sp);
  });
  const qi=makeWangqiWY({H:12,seed:25753}); qi.position.set(-7,-1.8,-52); qi.rotation.y=0.08; g.add(qi);
  const jia1=makeBingjiaWY({type:'mix',seed:25763}); jia1.position.set(-20,-1.8,-38); jia1.rotation.y=0.5; g.add(jia1);
  const gu=makeZhanguWY({seed:25764}); gu.position.set(15,-1.8,-36); gu.rotation.y=-0.5; g.add(gu);
  const motes=makeGlow({n:26,box:[170,18,70],pos:[0,9,-38],color:0x8a7048,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const mist=makeMist({n:6,spread:[220,14,80],pos:[0,5,-58],scale:70,color:0x4a3826,op:0.10});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.0,w:14,d:6,color:0x14100a,seed:25765,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-12,-1.9,15); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x14100a,seed:25766,rim:0.09,rimC:0xb8905a});
  fg2.g.position.set(13,-1.8,13); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.34,p:[-44,52,-24]},{c:0x2a1e12,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    qi.userData.update(t,k,1); crowd.update(t);
    for(let i=0;i<cSpears.length;i++)cSpears[i].userData.update(t,k,0);
    motes.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bTongpao(){ // 壹（标志性瞬间）· 同袍同仇 —— 岂曰无衣？与子同袍。王于兴师，修我戈矛。与子同仇！：
                     // 拂晓大漠营盘，王旗初展，军士并肩整甲列阵，主将振臂誓师，戈矛成架
  const g=new THREE.Group();
  const base=makeDamoWY({seed1:25771,seed2:25772}); g.add(base.g);
  /* 王旗：阵后初展 */
  const qi=makeWangqiWY({H:11.5,seed:25754}); qi.position.set(-5,-1.8,-33); qi.rotation.y=0.10; g.add(qi);
  /* 军士两排：并肩整甲列阵（执兵姿，戈矛混编） */
  const XF=[-5.8,-2.9,0,2.9,5.8];
  const rowF=makeShizuRowWY({n:5,w:14.5,xs:XF,jz:0,seed:25773,s:1.38,pose:'执兵',rim:0.24});
  rowF.position.set(-1,-1.78,-17); g.add(rowF);
  const XB=[-7.3,-4.4,-1.5,1.5,4.4,7.3];
  const rowB=makeShizuRowWY({n:6,w:14.6,xs:XB,jz:0,seed:25774,s:1.30,pose:'执兵',rim:0.18});
  rowB.position.set(-0.5,-1.78,-23.5); g.add(rowB);
  const spears=[];
  const TF=['ge','mao','ge','mao','ge'], RF=[0.20,-0.16,0.22,-0.18,0.20];
  XF.forEach(function(x,i){
    const sp=makeChangbingWY({type:TF[i],rest:RF[i],seed:25790+i,g:0.28,L:3.3});
    sp.position.set(-1+(x+0.08)*1.38,-1.78+0.93*1.38,-17+0.50*1.38);
    sp.scale.setScalar(1.38); g.add(sp); spears.push(sp);
  });
  const TB=['mao','ge','mao','ge','mao','ge'], RB=[-0.18,0.20,-0.22,0.16,-0.20,0.18];
  XB.forEach(function(x,i){
    const sp=makeChangbingWY({type:TB[i],rest:RB[i],seed:25800+i,g:0.28,L:3.3,rim:0.18});
    sp.position.set(-0.5+(x+0.08)*1.30,-1.78+0.93*1.30,-23.5+0.50*1.30);
    sp.scale.setScalar(1.30); g.add(sp); spears.push(sp);
  });
  /* 戈矛架两座：阵侧修整 */
  const rack1=makeBingjiaWY({type:'ge',seed:25775}); rack1.position.set(-14.5,-1.8,-21); rack1.rotation.y=0.55; g.add(rack1);
  const rack2=makeBingjiaWY({type:'mao',seed:25776}); rack2.position.set(15.5,-1.8,-23); rack2.rotation.y=-0.7; g.add(rack2);
  /* 战鼓：誓师之位 */
  const gu=makeZhanguWY({seed:25777}); gu.position.set(9.5,-1.8,-8.5); gu.rotation.y=-0.42; g.add(gu);
  /* 主将：振臂誓师（指月姿态，指向阵前） */
  const rock=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:5,color:0x14100a,seed:25778,rim:0.12,rimC:0xb8905a});
  rock.g.position.set(-6.2,-1.5,-6.8); g.add(rock.g);
  const cmd=wyCommander(0.88,'指月'); cmd.position.set(-4.9,-1.10,-6.4); cmd.rotation.y=0.55; g.add(cmd);
  /* 拂晓残火：两支火把将熄未熄 */
  const th1=makeHuobaWY({seed:25781,light:0.7,fh:0.7}); th1.position.set(-15.5,-1.8,-13); g.add(th1);
  const th2=makeHuobaWY({seed:25782,light:0.7,fh:0.7}); th2.position.set(14.5,-1.8,-13.5); g.add(th2);
  /* 晨光低照：一盏暖光托出阵列（王旗初展、群像整甲） */
  const sl=new THREE.PointLight(0xc89058,0.85,52);
  sl.position.set(-2,3.4,-18); g.add(sl);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-54],scale:68,color:0x4a3826,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[160,18,66],pos:[0,9,-34],color:0x8a7048,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:25783,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-12,-1.8,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:25784,rim:0.09,rimC:0xb8905a});
  fg2.g.position.set(12.5,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0xc09055,i:0.46,p:[-52,40,-24]},{c:0x2c2012,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    qi.userData.update(t,k,1);
    for(let i=0;i<spears.length;i++)spears[i].userData.update(t,k,0);
    th1.userData.update(t,k); th2.userData.update(t,k);
    cmd.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k); rock.update(t,k);
  }};
}
function bTongze(){ // 贰 · 同泽偕作 —— 岂曰无衣？与子同泽。王于兴师，修我矛戟。与子偕作！：
                    // 日暮修备：锻炉火光、矛戟成架、军士整甲扶兵、鼓声催行
  const g=new THREE.Group();
  const base=makeDamoWY({seed1:25785,seed2:25786,dustA:0.13,dustV:5.0,c1:0x160e07,c2:0x2a1a0c}); g.add(base.g);
  const qi=makeWangqiWY({H:11.5,seed:25755}); qi.position.set(-6.5,-1.8,-33); qi.rotation.y=0.12; g.add(qi);
  /* 军士两排：整甲（左手抚甲），矛戟在手 */
  const XF=[-5.8,-2.9,0,2.9,5.8];
  const rowF=makeShizuRowWY({n:5,w:14.5,xs:XF,jz:0,seed:25787,s:1.38,pose:'整甲',rim:0.20});
  rowF.position.set(0,-1.78,-17); g.add(rowF);
  const XB=[-7.3,-4.4,-1.5,1.5,4.4,7.3];
  const rowB=makeShizuRowWY({n:6,w:14.6,xs:XB,jz:0,seed:25788,s:1.30,pose:'整甲',rim:0.15});
  rowB.position.set(0,-1.78,-23.5); g.add(rowB);
  const spears=[];
  const RF=[0.15,-0.13,0.17,-0.15,0.15], RB=[-0.14,0.16,-0.17,0.13,-0.15,0.14];
  XF.forEach(function(x,i){
    const sp=makeChangbingWY({type:'ji',rest:RF[i],seed:25810+i,g:0.28,L:3.3});
    sp.position.set(0+(x+0.08)*1.38,-1.78+0.93*1.38,-17+0.50*1.38);
    sp.scale.setScalar(1.38); g.add(sp); spears.push(sp);
  });
  XB.forEach(function(x,i){
    const sp=makeChangbingWY({type:'ji',rest:RB[i],seed:25820+i,g:0.28,L:3.3,rim:0.18});
    sp.position.set(0+(x+0.08)*1.30,-1.78+0.93*1.30,-23.5+0.50*1.30);
    sp.scale.setScalar(1.30); g.add(sp); spears.push(sp);
  });
  /* 矛戟架两座 */
  const rack1=makeBingjiaWY({type:'ji',seed:25789}); rack1.position.set(15,-1.8,-22); rack1.rotation.y=-0.6; g.add(rack1);
  const rack2=makeBingjiaWY({type:'ji',seed:25791}); rack2.position.set(-15.5,-1.8,-25); rack2.rotation.y=0.6; g.add(rack2);
  /* 锻炉火盆：修兵之火 */
  const bz=makeBrazier({r:1.0,fh:2.1,fw:1.05,light:1.15,lightD:38,embers:24,spark:true});
  bz.g.position.set(-6.8,-1.8,-7.5); g.add(bz.g);
  const emb=makeGlow({n:26,box:[6,7,6],pos:[-6.8,3.4,-7.5],color:0xd88040,size:2.6,speed:0.5,rise:0.9,add:true,maxA:0.30});
  g.add(emb.points);
  /* 战鼓（带鼓槌）：鼓声催行 */
  const gu=makeZhanguWY({sticks:true,seed:25792}); gu.position.set(9.8,-1.8,-8.2); gu.rotation.y=-0.42; g.add(gu);
  /* 主将：立于阵前督修（独立姿态） */
  const cmd=wyCommander(0.88,'独立'); cmd.position.set(-4.9,-1.78,-6.4); cmd.rotation.y=0.55; g.add(cmd);
  const mist=makeMist({n:7,spread:[220,14,78],pos:[0,5,-54],scale:70,color:0x5a4228,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[160,16,66],pos:[0,8,-32],color:0xb09060,size:4.2,speed:0.035,rise:0,add:false,maxA:0.09});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x14100a,seed:25793,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x14100a,seed:25794,rim:0.09,rimC:0xb8905a});
  fg2.g.position.set(12.5,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0xc8884a,i:0.30,p:[48,30,-20]},{c:0x30200f,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
    qi.userData.update(t,k,1.15);
    for(let i=0;i<spears.length;i++)spears[i].userData.update(t,k,0);
    bz.update(t,k); emb.update(t);
    cmd.update(t,k);
    mist.update(t,k); motes.update(t);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bTongchang(){ // 叁（末境·可点击）· 同裳偕行 —— 岂曰无衣？与子同裳。王于兴师，修我甲兵。与子偕行！：
                       // 夜火通明，甲兵齐整；点击共修甲兵：鼓声三通，戈矛林立同举
  const ctl={t:0,clicked:false,on:false,reveal:0,down:false,burstDone:false};
  const g=new THREE.Group();
  const base=makeDamoWY({seed1:25795,seed2:25796,dustA:0.09,dustV:3.4,c1:0x120c06,c2:0x201408}); g.add(base.g);
  /* 王旗：阵后正中，夜风猎猎 */
  const qi=makeWangqiWY({H:11.5,seed:25756}); qi.position.set(0,-1.8,-36); g.add(qi);
  /* 甲架两座 + 矛戟架一座：甲兵齐整 */
  const jj1=makeJiajiaWY({seed:25797}); jj1.position.set(-15,-1.8,-25); jj1.rotation.y=0.5; g.add(jj1);
  const jj2=makeJiajiaWY({seed:25798}); jj2.position.set(-18,-1.8,-31); jj2.rotation.y=0.8; g.add(jj2);
  const rack=makeBingjiaWY({type:'ji',seed:25799}); rack.position.set(15,-1.8,-25); rack.rotation.y=-0.6; g.add(rack);
  /* 夜火四支：出征前夜列火 */
  const torches=[];
  [[-13.5,-12],[13.5,-13],[-9,-31],[10,-32]].forEach(function(p,i){
    const th=makeHuobaWY({seed:25830+i,light:0.85,fh:0.8+i*0.05});
    th.position.set(p[0],-1.8,p[1]); g.add(th); torches.push(th);
  });
  /* 军士两排：执兵肃立（戈矛在手） */
  const XF=[-5.8,-2.9,0,2.9,5.8];
  const rowF=makeShizuRowWY({n:5,w:14.5,xs:XF,jz:0,seed:25801,s:1.38,pose:'执兵',rim:0.20});
  rowF.position.set(0,-1.78,-17); g.add(rowF);
  const XB=[-7.3,-4.4,-1.5,1.5,4.4,7.3];
  const rowB=makeShizuRowWY({n:6,w:14.6,xs:XB,jz:0,seed:25802,s:1.30,pose:'执兵',rim:0.15});
  rowB.position.set(0,-1.78,-23.5); g.add(rowB);
  const spears=[];
  const RF=[0.20,-0.16,0.22,-0.18,0.20], TB=['ji','mao','ji','mao','ji'];
  XF.forEach(function(x,i){
    const sp=makeChangbingWY({type:TB[i],rest:RF[i],seed:25840+i,g:0.28,L:3.3});
    sp.position.set(0+(x+0.08)*1.38,-1.78+0.93*1.38,-17+0.50*1.38);
    sp.scale.setScalar(1.38); g.add(sp); spears.push(sp);
  });
  const RB=[-0.18,0.20,-0.22,0.16,-0.20,0.18], TB2=['mao','ji','mao','ji','mao','ji'];
  XB.forEach(function(x,i){
    const sp=makeChangbingWY({type:TB2[i],rest:RB[i],seed:25850+i,g:0.28,L:3.3,rim:0.18});
    sp.position.set(0+(x+0.08)*1.30,-1.78+0.93*1.30,-23.5+0.50*1.30);
    sp.scale.setScalar(1.30); g.add(sp); spears.push(sp);
  });
  /* 战鼓：三通催征 */
  const gu=makeZhanguWY({sticks:true,seed:25803}); gu.position.set(7.5,-1.8,-8.5); gu.rotation.y=-0.42; g.add(gu);
  /* 主将：振臂同举（指月姿态） */
  const cmd=wyCommander(0.88,'指月'); cmd.position.set(-4.9,-1.78,-6.4); cmd.rotation.y=0.55; g.add(cmd);
  /* 点击交互：戈矛林立同举——齐振之光 + 火星腾起 */
  const burst=makeBurst({n:70,color:0xd8b070,pos:[0,1.8,-16]});
  g.add(burst.points);
  const qlight=new THREE.PointLight(0xd8a870,1.6,44);
  qlight.position.set(0,2.2,-16); g.add(qlight);
  const embB=makeGlow({n:30,box:[40,10,30],pos:[0,3,-20],color:0xd88a48,size:2.8,speed:0.4,rise:0.8,add:true,maxA:0.28});
  g.add(embB.points);
  const mist=makeMist({n:6,spread:[210,14,76],pos:[0,5,-54],scale:68,color:0x4a3626,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[160,16,66],pos:[0,8,-32],color:0xa8804e,size:4.0,speed:0.03,rise:0,add:false,maxA:0.08});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x100b06,seed:25804,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.0,w:9,d:4,color:0x100b06,seed:25805,rim:0.09,rimC:0xb8905a});
  fg2.g.position.set(12.5,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0xa8804e,i:0.26,p:[-40,50,-24]},{c:0x241a0e,i:0.52});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on){
        if(ctl.down){ ctl.reveal=Math.max(0,ctl.reveal-dt/0.5); if(ctl.reveal===0)ctl.down=false; }
        else ctl.reveal=Math.min(1,ctl.reveal+dt/1.5);
        if(ctl.reveal>=1&&!ctl.burstDone){ ctl.burstDone=true; burst.fire(); }
      }
      const rv=ctl.reveal;
      for(let i=0;i<spears.length;i++){
        const raw=Math.max(0,Math.min(1,rv*1.9-i*0.09));
        const e=raw*raw*(3-2*raw);
        spears[i].userData.update(t,k,e);
      }
      qlight.intensity=k*1.6*rv;
      embB.points.material.opacity=k*0.28*rv*(0.8+0.2*Math.sin(t*3.3));
      qi.userData.update(t,k,1+1.1*rv);
      for(let i=0;i<torches.length;i++)torches[i].userData.update(t,k);
      cmd.update(t,k);
      burst.update(t);
      mist.update(t,k); motes.update(t);
      base.ridge.update(t,0); base.ridge2.update(t,0); base.grd.update(); base.dust.update(t);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.15);
      }
      if(ctl.reveal>0.5)ctl.down=true;               /* 收而复举：可反复点击 */
      else ctl.down=false;
      ctl.burstDone=false;
      pluck(1,0.0,0.16); pluck(1,0.42,0.13); pluck(2,0.9,0.11); pluck(4,1.5,0.09);   /* 鼓声三通 */
      const fl=$('#flash'); fl.textContent='修我甲兵 与子偕行';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x14100a),hor:C(0x32220f),bot:C(0x0c0805),fog:C(0x180f08),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-70,26,-190),ms:0.30,mph:0.46,mhaze:0.20,dirC:C(0xb08850),dirI:0.32,
  dirP:new THREE.Vector3(-48,50,-26),ambC:C(0x2a1e12),ambI:0.56},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,46],t:[0,9.5,38],lf:[1.5,8.5,-26],lt:[2.5,9,-36]},
  sky:()=>SK({fd:0.0046,star:0.14}) },
{ name:'同袍同仇',dwell:20,river:0.02,build:bTongpao,
  cam:{f:[0,4.6,26],t:[-1.5,4.0,18],lf:[-3,4.4,-14],lt:[-5,4.6,-26]},
  sky:()=>SK({top:C(0x181009),hor:C(0x3a2812),bot:C(0x0d0905),fog:C(0x1a1108),fd:0.0056,star:0.10,
    ms:0.26,mph:0.46,mhaze:0.24,moon:new THREE.Vector3(-64,22,-180),
    dirC:C(0xc09055),dirI:0.36,dirP:new THREE.Vector3(-52,34,-24),
    ambC:C(0x2c2012),ambI:0.56}) },
{ name:'同泽偕作',dwell:20,river:0.02,build:bTongze,
  cam:{f:[1.5,4.2,24],t:[-0.5,3.8,17],lf:[2,4.0,-10],lt:[0,4.2,-24]},
  sky:()=>SK({top:C(0x181008),hor:C(0x463016),bot:C(0x0e0905),fog:C(0x1c130a),fd:0.0058,star:0.04,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),mhaze:0.06,
    dirC:C(0xc8884a),dirI:0.30,dirP:new THREE.Vector3(48,28,-20),
    ambC:C(0x30200f),ambI:0.55}) },
{ name:'同裳偕行',dwell:22,river:0.02,build:bTongchang,
  cam:{f:[0,4.4,25],t:[0,3.8,17],lf:[0,4.2,-12],lt:[0,4.6,-28]},
  sky:()=>SK({top:C(0x0d0a06),hor:C(0x241708),bot:C(0x0a0705),fog:C(0x16100a),fd:0.0056,star:0.55,
    ms:0.30,mph:0.50,mhaze:0.16,moon:new THREE.Vector3(-58,40,-185),
    dirC:C(0xa8804e),dirI:0.26,dirP:new THREE.Vector3(-40,50,-24),
    ambC:C(0x241a0e),ambI:0.52}) },
];
"""

if __name__ == '__main__':
    print('wuyi.py —— 被 build.py 消费：python build.py wuyi')
