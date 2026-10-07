# -*- coding: utf-8 -*-
"""jianke.py —— 《剑客》（唐·贾岛，queue no.224，大漠金戈）生成配置
两境（N=queue stages 数）：磨剑十年（十年磨一剑·霜刃未曾试——寒夜砺锋、藏锋未试）、
把剑示君（今日把示君·谁为不平事——标志性瞬间+末境点击「点击霜刃——剑出鞘寒光乍现+风声」）。
大漠金戈全套色板：底色 #120d08、雾 #140d07～#141018 系、文字 #f0e2cc，accent=#c9824a
（queue 分配强调色，暗赭鎏金）只落在人物边缘光/剑柄缠丝/剑匣铜箍/窗纸暖光/UI 上，禁艳金。
全页唯一冷色源是「霜刃」：钢青 0x8a9aaa～0xd8e2ea 只属于剑——暖夜与冷刃对撞出侠气。
情绪推进线：境壹=蓄（十年磨剑，锋芒深藏，霜夜静默）→ 境贰=发（把剑示君，亮刃明志）。
标志性瞬间（境贰·末境点击）：剑出鞘——剑客捧剑示君静立如碑，剑在匣中只露剑柄；点击后
剑匣沿剑身缓缓滑落，霜刃寸寸出鞘，寒光乍现、剑鸣与风声骤起，「今日把示君 谁为不平事」题字同现。
与已有边塞页（战阵/夜射/行军/听笛/白骨/大湖）第一眼可区分：本页是「剑庐磨剑 + 捧剑示君」
的侠客独像——没有战争，只有一柄剑与一个人，蓄势与亮剑。
考点钉子：磨 mó / 示 shì / 为 wèi（第 3 题落点）；贾岛苦吟诗人+「推敲」典故+托物言志（第 4 题）；
「十年磨一剑」自喻苦修与「谁为不平事」的侠义豪情（第 5 题）。tts 多音字：磨→摩、示→世、为→未。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='jianke', title='剑客', dyn='唐 · 贾岛', brand_author='贾 岛',
    gold_rgb='201,130,74',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#c9824a; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(201,130,74,.3);
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
    tip='轻点画面 / 按空格 —— 剑出鞘，霜刃乍现寒光',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看剑客把剑示君，霜刃出鞘寒光凛冽',
    cover_read='剑客。唐，贾岛。十年磨一剑，霜刃未曾试。今日把示君，谁为不平事。',
    cover_p1='两重意境，随诗句次第展开：寒夜剑庐，十年磨出一柄霜刃，锋芒却从未一试；转过境来，剑客捧剑示君——谁有不平事？此剑当为天下而出。十年蓄势，一朝亮剑。',
    cover_p2='边读诗，边看这柄剑如何从砺石上慢慢醒来：贾岛一生苦吟、屡试不第，半生磨砺都灌进了这柄剑里——读懂了「磨剑」与「示剑」，就读懂了寒士胸中那口不平之气与侠义之志。',
    end_h2='霜刃 · 示君', cn_word='贰',
    words_js="['再陪剑客磨一回剑','初识贾岛，尚需共读','渐入诗境，再诵几遍','剑气渐凝，霜刃欲试','已解示君亮剑意','十年一剑，侠气干云']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'磨剑十年', jing:'十年工夫磨出一柄剑，剑刃寒光如霜，却还从未试过锋 —— 磨砺、藏锋，静默如夜。（剑庐 · 砺石 · 霜刃 · 藏锋）',
  segs:[
   {c:'十年磨一剑，', p:py('shí nián mó yī jiàn')},
   {c:'霜刃未曾试。', p:py('shuāng rèn wèi céng shì')}],
  read:'十年磨一剑，霜刃未曾试。',
  yisi:'十年工夫磨出这一柄剑，剑刃寒光凛冽如霜，却还从来没有试过锋。——「十年」极言磨砺之久，「一剑」极言用心之专：世上的剑千千万，他只磨这一柄；「霜刃」写剑之利，寒光逼人如霜；「未曾试」三字陡然一收——利剑已成，锋芒深藏，如志士学成而未遇。剑是贾岛的自喻：十年寒窗苦吟，磨的是一身的才与志。',
  zhu:[['剑客','佩剑行侠的人。诗题一作《述剑》——诗以剑自喻、以剑客自况，是贾岛托物言志之作'],['十年磨一剑','用十年功夫磨这一柄剑——「十年」见时间之长，「一剑」见用心之专：不博、不杂、不辍，写尽苦心磨砺、精益求精'],['霜刃','形容剑刃寒光闪闪、清冷如霜——极言其锋利，也带出一层凛然不可犯的剑气'],['未曾试','还没有试过锋——锋芒藏而未露，如才士学成而未遇；「不遇」正是此诗先抑的一笔，为下文的亮剑蓄足了势'],['苦吟诗人','贾岛作诗以苦吟著称，字斟句酌、反复推敲（「推敲」的典故即出自他）；以「十年磨一剑」自况——磨剑亦磨诗、磨志']] },
{ name:'把剑示君', jing:'今日捧剑到君前：霜刃出鞘，寒光乍现 —— 亮剑、明志，天下不平事，此剑当之。（示剑 · 出鞘 · 寒光 · 侠气 · 标志性瞬间 · 末境点击画面：剑出鞘寒光乍现+风声）',
  segs:[
   {c:'今日把示君，', p:py('jīn rì bǎ shì jūn')},
   {c:'谁为不平事。', p:py('shuí wèi bù píng shì')}],
  read:'今日把示君，谁为不平事。',
  yisi:'今天拿出来给您看：谁有冤屈不平的事？——「今日」与「十年」相对：磨了十年，为的就是今日一亮；「把示君」坦荡直率，如捧剑于君前，毫无遮掩；末句自问自答、掷地有声——天下谁有不平，此剑便为谁而出。十年蓄势，一朝亮剑，把寒窗苦守者的不平之鸣与济世之志推到顶点。',
  zhu:[['今日把示君','把，持、拿；示，给……看——今天拿出来给您看。「示君」二字坦荡磊落，不容置疑。文本从通行本（一本作「把似君」）'],['谁为不平事','为，读 wèi，替、给——谁有不平之事？我愿仗此剑替你铲平。一本作「谁有不平事」，意思相同：这是剑客自问自答的宣言，末句如剑出鞘，斩截有力'],['托物言志','借咏物言志向——全诗句句写剑：磨剑是十年苦修，霜刃是胸中才具，试剑是渴望建功；实则句句写人：以剑客自况，抒发寒士不遇、思为世用的怀抱'],['侠','中国文人心中的一种精神：见不平则鸣、挺身而出。贾岛一介寒士，以「剑客」自命——诗中侠气，正是苦吟人生里难得的一次快意出场'],['此诗背景','贾岛早年曾为僧、屡试不第，以苦吟闻名。此诗约作于其困顿之时：十年磨砺无人识，故借剑客亮剑，吐一口胸中不平之气']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「十年磨一剑」的下一句是？', o:['霜刃未曾试','今日把示君','谁为不平事'], a:0},
 {q:'「今日把示君」的下一句是？', o:['霜刃未曾试','谁为不平事','十年磨一剑'], a:1},
 {q:'「十年磨一剑」「今日把示君」「谁为不平事」中，「磨」「示」「为」的读音和意思都正确的一项是？', o:['磨读 mó，打磨、磨砺；示读 shì，给……看；为读 wèi，替——十年磨出这柄剑，今天拿来给您看：谁有不平之事，我替您铲平','磨读 mò，石磨；示读 shì，示意；为读 wéi，以为——十年守着一台石磨，今天拿来示意给您看：谁以为有不平之事','磨读 mó，折磨；示读 shì，显示；为读 wèi，因为——十年磨剑磨人太甚，今天显示给您看：因为不平才磨剑'], a:0},
 {q:'关于作者贾岛与本诗，下列说法正确的是？', o:['贾岛是中唐著名「苦吟诗人」，作诗字斟句酌，「推敲」的典故（「僧敲月下门」用敲还是用推）就出自他；《剑客》托物言志——剑是自喻：十年磨剑，亦是十年磨诗、磨志','贾岛是盛唐山水田园派诗人，与王维、孟浩然并称；《剑客》写于他隐居山中时，是一首纯粹的咏物写景诗','贾岛是晚唐边塞名将，此诗作于军旅之中，「霜刃」即他杀敌的佩刀，「把示君」是向朝廷请战'], a:0},
 {q:'「十年磨一剑，霜刃未曾试。今日把示君，谁为不平事。」对全诗主旨理解最恰当的一项是？', o:['写铸剑师夸耀手艺，希望有人出高价买走这柄十年磨成的宝剑','托物言志：十年磨剑是半生苦心磨砺的自况，「未曾试」是怀才不遇，「把示君」是渴望被识用——末句一问快意豪迈：谁有不平事，此剑当为天下而出，侠气与济世之志尽在其中','感叹宝剑久置不用会生锈，提醒人们再好的兵器也要经常磨，才能保持锋利'], a:1},
];
"""

SCENES_JS = """/* ================= 剑客 · 两境场景（大漠金戈·寒夜剑庐：磨剑十年、把剑示君） =================
   美术立意：大漠金戈色板写「十年磨剑→把剑示君」——底色 #120d08、雾 #140d07～#141018 系，
   accent=#c9824a（暗赭鎏金）只落在人物边缘光/剑柄缠丝/剑匣铜箍/窗纸暖光/UI 上，禁艳金。
   全页唯一冷色源是「霜刃」：钢青 0x8a9aaa～0xd8e2ea 只属于剑——暖夜与冷刃对撞出侠气。
   与已有边塞页第一眼可区分：不做战阵/夜射/行军/听笛/白骨，做「剑庐磨剑 + 捧剑示君」
   的侠客独像——没有战争，只有一柄剑与一个人，蓄势与亮剑。
   境壹（夜·蓄）：剑庐柴门暖窗一线，砺石横剑缓缓推磨，霜气浮动、石上火星微溅——十年之功。
   境贰（夜·发，标志性瞬间+末境可点击）：剑客捧剑示君，剑在匣中只露剑柄；
   点击：剑匣下滑、霜刃出鞘，寒光乍现、剑鸣风声骤起（点击霜刃——剑出鞘寒光乍现+风声）。 */

/* —— 剑庐 makeJianlu(o)：柴门茅顶小屋+暖窗（合批 1 mesh + 1 窗光面片）——十年磨剑的居处 */
function makeJianlu(o){
  o=o||{};
  const w=o.w===undefined?6.5:o.w, d=o.d===undefined?4.6:o.d, h=o.h===undefined?3.1:o.h;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,h,d); wall.translate(0,h*0.5,0); B.put(wall,0x1a130c);
  const roof=new THREE.ConeGeometry(Math.max(w,d)*0.80,2.1,4); roof.rotateY(Math.PI/4);
  roof.scale(1,1,d/w); roof.translate(0,h+1.0,0); B.put(roof,0x2c2014);
  const door=new THREE.BoxGeometry(1.15,2.0,0.10); door.translate(w*0.10,1.0,d*0.5+0.02); B.put(door,0x0c0805);
  const win=new THREE.BoxGeometry(0.95,0.85,0.06); win.translate(-w*0.24,h*0.55,d*0.5+0.02); B.put(win,0x332310);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2012,emissive:0x040302}),{c:0xc9824a,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  const winMat=new THREE.MeshBasicMaterial({color:0xd8a060,transparent:true,opacity:o.win===undefined?0.32:o.win});
  const glow=new THREE.Mesh(new THREE.PlaneGeometry(0.76,0.66),winMat);
  glow.position.set(-w*0.24,h*0.55,d*0.5+0.06); g.add(glow);
  g.update=function(t,k){ winMat.opacity=k*(o.win===undefined?0.32:o.win)*(0.88+0.12*Math.sin(t*0.9)); };
  g.userData.update=g.update;
  return g;
}

/* —— 砺石 makeMoshi(o)：上下两叠天然巨石，顶面平缓可磨（合批 1 mesh）——「十年磨一剑」 */
function makeMoshi(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?22411:o.seed);
  const B=new GeoBag();
  const base=rockGeo(1.30,1,R); base.scale(1.30,0.45,1.02); base.rotateZ(0.05);
  base.translate(0,0.40,0); B.put(base,shadeColor(0x332c22,0.9+0.2*R()));
  const slab=rockGeo(1.05,1,R); slab.scale(1.80,0.40,0.86); slab.rotateZ(-0.03); slab.rotateY(0.06);
  slab.translate(0.05,1.18,0); B.put(slab,shadeColor(0x4a4336,0.95+0.2*R()));
  const plate=new THREE.BoxGeometry(2.45,0.07,1.02); plate.rotateY(0.06);
  plate.translate(0.05,1.585,0); B.put(plate,0x5a5344);   // 平缓磨石面：剑卧其上清晰可读
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x45402f,emissive:0x050402}),{c:0xc9824a,i:o.rim===undefined?0.15:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 长剑 makeChangjian(o)：沿 +Y 剑柄在下、剑锋在上；剑身/剑柄分 mesh，剑身带钢青渐变
   返回 {g, mat（剑身材质，emissive 可控寒光）, blade（剑身 mesh，出鞘前可硬关）, hilt} */
function makeChangjian(o){
  o=o||{};
  const L=o.L===undefined?1.55:o.L;
  const g=new THREE.Group();
  const mat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:26,
    specular:0x8a929c,emissive:0x8aa8c0,emissiveIntensity:0});
  const B2=new GeoBag();
  const segs=[[0,0x565d68],[0.26,0x767f8a],[0.52,0x98a2ad],[0.78,0xbfc9d4]];
  const bh=L*0.75/4;
  for(let i=0;i<4;i++){
    const b=new THREE.BoxGeometry(0.092-i*0.008,bh+0.004,0.024);
    b.translate(0,0.05+bh*i+bh*0.5,0); B2.put(b,segs[i][1]);
  }
  const tip=new THREE.ConeGeometry(0.048,0.26,4); tip.rotateY(Math.PI/4);
  tip.translate(0,0.05+L*0.75+0.12,0); B2.put(tip,0xd6e0ea);
  const spine=new THREE.BoxGeometry(0.015,L*0.75,0.033); spine.translate(0,0.05+L*0.375,0); B2.put(spine,0xe4ecf2);
  const blade=B2.mesh(mat); g.add(blade);
  const B=new GeoBag();
  const guard=new THREE.BoxGeometry(0.32,0.055,0.11); guard.translate(0,-0.02,0); B.put(guard,0x5a4830);
  const gline=new THREE.BoxGeometry(0.33,0.016,0.115); gline.translate(0,0.014,0); B.put(gline,0x8a6238);
  const hilt=new THREE.CylinderGeometry(0.032,0.037,0.36,6); hilt.translate(0,-0.225,0); B.put(hilt,0x241b12);
  for(let i=0;i<3;i++){
    const ring=new THREE.TorusGeometry(0.038,0.008,5,12); ring.rotateX(Math.PI/2);
    ring.translate(0,-0.12-i*0.095,0); B.put(ring,0x7a5c38);
  }
  const pom=new THREE.SphereGeometry(0.056,8,6); pom.translate(0,-0.43,0); B.put(pom,0x5a4830);
  B.put(limbGeo([0,-0.47,0],[-0.07,-1.00,0.02],0.020,0.007,4),0x6a3020);
  B.put(limbGeo([0,-0.47,0],[0.06,-0.96,-0.03],0.020,0.007,4),0x7a3a26);
  const hiltMesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a4030,emissive:0x060402}),{c:0xc9824a,i:o.rim===undefined?0.20:o.rim,p:2.4}));
  g.add(hiltMesh);
  return {g:g,mat:mat,blade:blade,hilt:hiltMesh};
}

/* —— 剑匣 makeJianxia(o)：鞘口在下（y=0）、鞘尾在上（y=Ls），合批 1 mesh ——出鞘=匣沿剑身下滑 */
function makeJianxia(o){
  o=o||{};
  const Ls=o.Ls===undefined?1.52:o.Ls;
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.044,0.058,Ls,8); body.translate(0,Ls*0.5,0);
  B.put(body,0x20180f);
  const cap=new THREE.SphereGeometry(0.048,8,6); cap.scale(1,1.5,0.62); cap.translate(0,Ls-0.02,0);
  B.put(cap,0x2c2014);
  for(let i=0;i<2;i++){
    const band=new THREE.TorusGeometry(0.060,0.011,5,14); band.rotateX(Math.PI/2); band.scale(1,1,0.62);
    band.translate(0,Ls*(0.22+0.56*i),0); B.put(band,0x6a5434);
  }
  const mouth=new THREE.TorusGeometry(0.058,0.013,5,14); mouth.rotateX(Math.PI/2); mouth.scale(1,1,0.62);
  mouth.translate(0,0.01,0); B.put(mouth,0x8a6238);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x4a4030,emissive:0x060402}),{c:0xc9824a,i:o.rim===undefined?0.18:o.rim,p:2.4})));
  return g;
}

/* 剑客/磨剑人：全诗贯穿的同一造型（每次 build 新建材质） */
function jkFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2e2418,belt:0x8a6238,skin:0xd9b189,collar:0x6a5434,
    hair:0x181209,hat:'发髻',beard:true,rimC:0xc9824a,rim:0.5,noProp:true,scale:scale===undefined?1.85:scale});
}

function bCover(){ // 卷首 · 寒夜剑庐远望：茅屋暖窗、砺石横剑、霜气横流、低月昏黄
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0e0a06,c2:0x1c130b,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:18,layers:2,peaks:5,seed:22401,color:0x0d0906,atmo:0x2e2114,
    fogK:0.62,glowK:0.06,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-20,0,-98); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const hut=makeJianlu({w:6.5,d:4.6,h:3.1,win:0.34}); hut.position.set(-8.0,-1.60,-24); hut.rotation.y=0.36; g.add(hut);
  const rock=makeForeground({kind:'坡石',n:2,r:2.2,w:8,d:5,color:0x0d0906,seed:22402,rim:0.10,rimC:0xc9824a});
  rock.g.position.set(2.6,-1.55,-13.5); g.add(rock.g);
  const mo=makeMoshi({seed:22403,scale:0.85}); mo.position.set(2.4,-1.10,-14); mo.rotation.y=-0.30; g.add(mo);
  const jian=makeChangjian({L:1.4});
  jian.g.position.set(-0.6,1.64,0.05); jian.g.rotation.y=0.15; jian.g.rotation.z=Math.PI/2-0.05;
  mo.add(jian.g);
  const frost=makeGlow({n:30,box:[96,13,40],pos:[0,4.5,-18],color:0x93a8b8,size:2.0,speed:0.15,rise:-0.10,add:false,maxA:0.09});
  g.add(frost.points);
  const wind=makeFlow({n:300,box:[100,11,40],pos:[0,3.4,-22],color:0x46382a,size:16,speed:4.4,maxA:0.12});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[220,12,80],pos:[0,5,-56],scale:70,color:0x3a2c1c,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.8,w:13,d:6,color:0x0c0805,seed:22404,rim:0.09,rimC:0xc9824a});
  fg1.g.position.set(-11,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',n:4,w:13,d:4,color:0x0e0906,seed:22405,sway:0.8,rim:0.08,rimC:0xc9824a});
  fg2.g.position.set(11.5,6.0,13); g.add(fg2.g);
  const cl=new THREE.PointLight(0xd8a060,0.5,22); cl.position.set(-7.2,1.6,-21); g.add(cl);
  addLights(g,{c:0xa8824e,i:0.30,p:[-42,50,-26]},{c:0x281c10,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); grd.update(); hut.update(t,k);
    jian.g.position.x=-0.6+0.10*Math.sin(t*1.3);
    frost.update(t); wind.update(t); mist.update(t,k); fg1.update(t,k); fg2.update(t,k); rock.update(t,k);
  }};
}
function bMojian(){ // 壹 · 磨剑十年 —— 十年磨一剑，霜刃未曾试：寒夜剑庐，砺石横剑缓缓推磨
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0e0a06,c2:0x1d130a,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:15,layers:2,peaks:4,seed:22421,color:0x0c0805,atmo:0x2e2114,
    fogK:0.63,glowK:0.05,glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-26,0,-102); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 剑庐：柴门茅顶，一窗暖光 */
  const hut=makeJianlu({w:6.8,d:4.8,h:3.2,win:0.44}); hut.position.set(-9.2,-1.60,-22); hut.rotation.y=0.40; g.add(hut);
  /* 砺石横剑：霜刃深藏未试，在石上被一寸寸推出锋（前后坡石垫脚，磨石前置于画面中景） */
  const rock=makeForeground({kind:'坡石',n:3,r:2.4,w:9,d:5,color:0x0d0906,seed:22422,rim:0.11,rimC:0xc9824a});
  rock.g.position.set(-2.6,-1.62,-8.4); g.add(rock.g);
  const rock2=makeForeground({kind:'坡石',n:2,r:1.9,w:7,d:4,color:0x0d0906,seed:22426,rim:0.11,rimC:0xc9824a});
  rock2.g.position.set(-3.0,-1.45,-5.2); g.add(rock2.g);
  const mo=makeMoshi({seed:22423,scale:1.1}); mo.position.set(-2.1,-0.55,-6.8); mo.rotation.y=0.22; g.add(mo);
  const jian=makeChangjian({L:1.6});
  jian.mat.emissiveIntensity=0.20;                 // 未试之刃亦有微芒（静态，不逐帧写）
  jian.g.position.set(-0.75,1.65,0.06); jian.g.rotation.y=0.10; jian.g.rotation.z=Math.PI/2-0.03;
  mo.add(jian.g);
  const jx=jian.g.position.x;
  /* 磨剑人：立于石侧守望——十年之功，人剑相对 */
  const poet=jkFigure(1.85,'独立'); poet.position.set(1.6,-0.30,-6.1); poet.rotation.y=-2.05; g.add(poet);
  /* 水盏：砺锋蘸水 */
  const bowl=makeVessel({type:'碗',mat:'陶',scale:0.9,liquid:true,shadow:true});
  bowl.g.position.set(0.35,-0.30,-6.9); bowl.g.rotation.y=0.5; g.add(bowl.g);
  /* 磨石火星：推磨时溅起的细碎金屑 */
  const spark=makeGlow({n:12,box:[3.6,1.1,1.6],pos:[-2.5,1.15,-7.5],color:0xc9a05a,size:1.3,speed:0.7,rise:0.28,add:true,maxA:0.08});
  g.add(spark.points);
  /* 霜气：寒夜霜屑缓缓沉降 */
  const frost=makeGlow({n:34,box:[84,12,36],pos:[0,4.5,-16],color:0x93a8b8,size:2.0,speed:0.16,rise:-0.12,add:false,maxA:0.10});
  g.add(frost.points);
  const wind=makeFlow({n:300,box:[92,10,36],pos:[0,3.2,-20],color:0x46382a,size:15,speed:4.4,maxA:0.12});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,12,76],pos:[0,5,-54],scale:68,color:0x3a2c1c,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0d0805,seed:22424,rim:0.09,rimC:0xc9824a});
  fg1.g.position.set(-11.5,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',n:4,w:12,d:4,color:0x0e0906,seed:22425,sway:0.7,rim:0.08,rimC:0xc9824a});
  fg2.g.position.set(11,6.2,12); g.add(fg2.g);
  /* 冷月照石：给霜刃一点钢青色光（贴近砺石，主体可读） */
  const cl=new THREE.PointLight(0x9ab0c0,1.1,15); cl.position.set(-2.5,3.0,-4.9); g.add(cl);
  addLights(g,{c:0xa8824e,i:0.30,p:[-40,48,-24]},{c:0x281c10,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); grd.update(); hut.update(t,k);
    jian.g.position.x=jx+0.12*Math.sin(t*1.5);       // 推磨：剑在石上缓缓往复
    poet.update(t,k); bowl.update(t,k); spark.update(t); frost.update(t); wind.update(t);
    mist.update(t,k); fg1.update(t,k); fg2.update(t,k); rock.update(t,k);
  }};
}
function bShijun(){ // 贰（末境·可点击）· 把剑示君 —— 今日把示君，谁为不平事：捧剑示君，霜刃出鞘
  const ctl={t:0,clicked:false,on:false,reveal:0,done:false,trem:0};
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d0a07,c2:0x1b120a,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:13,layers:2,peaks:4,seed:22431,color:0x0b0806,atmo:0x2e2114,
    fogK:0.60,glowK:0.10,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-6,0,-112); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 剑庐退居远处——人已出庐，立于石台之前 */
  const hut=makeJianlu({w:6.2,d:4.4,h:3.0,win:0.22}); hut.position.set(-14.5,-1.62,-30); hut.rotation.y=0.55; g.add(hut);
  const rock=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x0e0906,seed:22432,rim:0.13,rimC:0xc9824a});
  rock.g.position.set(0.2,-1.50,-8.6); g.add(rock.g);
  const poet=jkFigure(1.8,'倾酒'); poet.position.set(0.3,-0.28,-7.7); poet.rotation.y=-0.14; g.add(poet);
  /* 捧剑示君：剑横于身前双手之间——匣掩霜刃，只露剑柄；匣口在 y=0、鞘尾在 +Y（剑锋方向），
     present 转 z≈π-0.94 后剑柄端恰好落在右手（举坛位）、鞘尾伸向左手 */
  const sword=makeChangjian({L:1.55});
  const xia=makeJianxia({Ls:1.52});
  const present=new THREE.Group();
  present.position.set(0.10,2.80,0.66); present.rotation.z=2.20; present.rotation.x=0.06;
  present.add(sword.g); present.add(xia);
  poet.add(present);
  sword.blade.visible=false;                        // 点击前硬关幻影（透明残影在浏览器里会露馅）
  sword.blade.renderOrder=1; xia.children[0].renderOrder=2;   // 匣后画，深度遮住匣内剑身
  const bladeMat=sword.mat;
  /* 霜刃寒光：贴剑身两道光带 + 剑锋闪光（点击前全部硬关；初值=最大，逐帧乘 fadeK） */
  const gleamMat1=new THREE.SpriteMaterial({map:glowTex(),color:0xbfd4e6,transparent:true,opacity:0.50,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const gl1=new THREE.Sprite(gleamMat1); gl1.scale.set(0.6,1.7,1); gl1.position.set(0,0.62,0.03);
  gl1.renderOrder=3; gl1.visible=false; present.add(gl1);
  const gleamMat2=new THREE.SpriteMaterial({map:glowTex(),color:0xd8e6f0,transparent:true,opacity:0.34,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const gl2=new THREE.Sprite(gleamMat2); gl2.scale.set(0.4,1.1,1); gl2.position.set(0,1.12,0.03);
  gl2.renderOrder=3; gl2.visible=false; present.add(gl2);
  const flMat=new THREE.SpriteMaterial({map:glowTex(),color:0xe8f2f8,transparent:true,opacity:0.85,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const fl=new THREE.Sprite(flMat); fl.scale.set(5.2,5.2,1); fl.position.set(0,1.28,0.06);
  fl.renderOrder=4; fl.visible=false; present.add(fl);
  const burst=makeBurst({n:42,color:0xcfdce8,pos:[0,1.30,0.05]});
  present.add(burst.points);
  /* 出鞘冷光：常驻弱冷光托人，出鞘时剑身冷光乍亮（初值=最大 1.16，逐帧乘 fadeK 且 ≤ base） */
  const cl=new THREE.PointLight(0xa8c2d8,1.16,26); cl.position.set(0.9,4.4,-5.9); g.add(cl);
  const frost=makeGlow({n:30,box:[88,12,38],pos:[0,4.5,-16],color:0x93a8b8,size:2.0,speed:0.14,rise:-0.10,add:false,maxA:0.09});
  g.add(frost.points);
  const wind=makeFlow({n:280,box:[90,10,36],pos:[0,3.4,-20],color:0x46382a,size:15,speed:4.0,maxA:0.11});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,12,76],pos:[0,5,-56],scale:68,color:0x302824,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x0d0805,seed:22433,rim:0.10,rimC:0xc9824a});
  fg1.g.position.set(-11.5,-1.8,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x0d0805,seed:22434,rim:0.10,rimC:0xc9824a});
  fg2.g.position.set(12.2,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0x9aa8b8,i:0.30,p:[-46,50,-26]},{c:0x261d14,i:0.54});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      let e=0, fk=0;
      if(ctl.on){
        ctl.reveal=Math.min(1,ctl.reveal+dt/1.6);
        e=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);     // 平滑出鞘
        xia.position.y=-1.42*e;                        // 剑匣沿剑身滑向剑柄
        if(ctl.reveal>=1&&!ctl.done){ ctl.done=true; ctl.trem=0; burst.fire(); }
      }
      if(ctl.done)ctl.trem+=dt;
      if(ctl.done)fk=Math.exp(-ctl.trem*2.1);          // 出鞘一瞬的闪光包络
      bladeMat.emissiveIntensity=k*(0.55*e+0.45*fk);
      gleamMat1.opacity=k*0.50*(e*0.9+0.3*fk);
      gleamMat2.opacity=k*0.34*(e*0.9+0.3*fk);
      flMat.opacity=k*0.85*fk;
      cl.intensity=k*1.16*(0.19+0.45*e+0.36*fk*(0.85+0.15*Math.sin(t*7.3)));
      ridge.update(t,0); grd.update(); hut.update(t,k); poet.update(t,k); rock.update(t,k);
      burst.update(t); frost.update(t); wind.update(t); mist.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        sword.blade.visible=true; gl1.visible=true; gl2.visible=true; fl.visible=true;
        setAmbience(0.20);                                          // 风声骤起
        pluck(6,0.05,0.12); pluck(4,0.26,0.09); pluck(7,0.52,0.07); // 剑鸣
        const flash=$('#flash'); flash.textContent='今日把示君 谁为不平事';
        flash.classList.remove('go'); void flash.offsetWidth; flash.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0c0806),hor:C(0x2a1c10),bot:C(0x090604),fog:C(0x140d07),fd:0.0050,star:0.14,
  moon:new THREE.Vector3(-70,28,-200),ms:0.5,mph:0.42,mhaze:0.18,dirC:C(0xb08850),dirI:0.34,
  dirP:new THREE.Vector3(-45,55,-25),ambC:C(0x2c2014),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.5,42],t:[0,8.5,34],lf:[1.5,7.5,-24],lt:[-2.5,8,-38]},
  sky:()=>SK({fd:0.0048,star:0.12}) },
{ name:'磨剑十年',dwell:16,river:0.02,build:bMojian,
  cam:{f:[0,5.6,19.5],t:[-1.2,5.0,11.5],lf:[-1.6,4.0,-12],lt:[-4,4.4,-24]},
  sky:()=>SK({top:C(0x0e0a08),hor:C(0x241812),bot:C(0x0a0705),fog:C(0x150e08),fd:0.0054,star:0.16,
    ms:0.36,mph:0.50,mhaze:0.20,moon:new THREE.Vector3(-52,22,-180),
    dirC:C(0x9aa6b4),dirI:0.26,dirP:new THREE.Vector3(-40,42,-26),
    ambC:C(0x261c12),ambI:0.52}) },
{ name:'把剑示君',dwell:19,river:0.02,build:bShijun,
  cam:{f:[0,5.4,16.5],t:[0.4,5.0,8.5],lf:[0.6,5.2,-6],lt:[2.8,5.6,-13]},
  sky:()=>SK({top:C(0x0c0e14),hor:C(0x201814),bot:C(0x08070a),fog:C(0x141018),fd:0.0058,star:0.26,
    ms:0.52,mph:0.30,mhaze:0.14,moon:new THREE.Vector3(-62,54,-190),
    dirC:C(0x9aa8b8),dirI:0.30,dirP:new THREE.Vector3(-46,48,-28),
    ambC:C(0x241c16),ambI:0.54}) },
];
"""
