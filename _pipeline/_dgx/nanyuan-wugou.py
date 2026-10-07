# -*- coding: utf-8 -*-
"""nanyuan-wugou.py —— 《南园·其五》（唐·李贺，queue no.226，大漠金戈）生成配置
两境（N=queue stages 数）：吴钩关山（男儿何不带吴钩·收取关山五十州——南园书斋掷笔、
吴钩横架、烽燧城郭列成五十州版图）、凌烟之问（请君暂上凌烟阁·若个书生万户侯——
标志性瞬间+末境点击「点击凌烟阁——阁上功臣画像次第显影+吴钩寒光」）。
大漠金戈全套色板：底色 #120d08、雾 #150e08～#141014 系、文字 #f0e2cc，accent=#c9a06a
（queue 分配强调色，沙金/绢帛金）只落在阁檐边缘光/功臣画像暖辉/铜格/窗纸暖光/UI 上，禁艳金。
全页唯一冷色源是「吴钩」：钢青 0x8a9aaa～0xecf3f9 只属于刀——暖阁金辉与冷刃寒光对撞出「功名之问」。
情绪推进线：境壹=起（南园书斋，掷笔横刀，指顾关山五十州）→ 境贰=问（凌烟高阁横空，
功臣画像次第显影——若个书生万户侯）。
标志性瞬间（境贰·mk moment「请君暂上凌烟阁（功名图像的召唤）」）：凌烟阁三重楼阁横空，
点击（queue interact）——阁上二十四功臣画像自下而上次第显影（幞头冠+面容+肩甲的暖辉剪影，
各自 emissive 渐亮），阁前金辉随之漫开；末了前景吴钩寒光乍现（钢青冷光对撞暖阁金辉），
「请君暂上凌烟阁 若个书生万户侯」题字同现。
与已有边塞页（战阵/夜射/行军/听笛/白骨/骏马/剑客/大湖）第一眼可区分：本页从「南园书斋田园」
起手——书案掷笔、刀架横钩、篱笆田家，烽燧城郭灯火铺出「收取关山五十州」的版图意象
（烽燧/城郭为边塞页未用过的钉子），末境以功臣画像楼阁收束——没有战争，是一声投笔从戎的慨叹。
考点钉子：钩 gōu / 侯 hóu / 若个 ruò gè（第 3 题落点）；凌烟阁二十四功臣（唐太宗命阎立本绘）+
李贺「诗鬼」与《南园十三首》（第 4 题）；投笔从戎之叹与两问的慷慨不平（第 5 题）。
tts 多音字：吴钩→吴勾（gōu）、万户侯→万户喉（hóu）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='nanyuan-wugou', title='南园·其五', dyn='唐 · 李贺', brand_author='李 贺',
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
    ],
    tip='轻点画面 / 按空格 —— 凌烟阁功臣画像次第显影，吴钩寒光乍现',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看凌烟阁上功臣画像次第显影，吴钩寒光乍现',
    cover_read='南园·其五。唐，李贺。男儿何不带吴钩，收取关山五十州。请君暂上凌烟阁，若个书生万户侯。',
    cover_p1='两重意境，随诗句次第展开：南园书斋，一管笔掷在案头，吴钩横在架上——男儿何不带吴钩，去收取关山五十州？转过境来，凌烟高阁横空：请君暂上阁一看，二十四功臣像次第显影——若个书生万户侯？一笔与一刀之间，是一声投笔从戎的慨叹。',
    cover_p2='边读诗，边看这位书生的两难：案上的笔与架上的刀，取哪一样才不负此生？李贺以两问作答——读懂了「何不」的激愤与「若个」的不平，就读懂了中唐书生报国无路的胸中块垒。',
    end_h2='吴钩 · 凌烟', cn_word='贰',
    words_js="['再回南园书斋小坐','初识长吉，尚需共读','渐入诗境，再诵几遍','吴钩渐明，关山渐近','已解凌烟功名之问','两问在耳，壮怀激烈']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'吴钩关山', jing:'男儿为什么不带上吴钩弯刀，去收复关山五十州？——书斋掷笔、横刀指顾，建功之志一起。（南园 · 书案 · 吴钩 · 烽燧城郭 · 五十州）',
  segs:[
   {c:'男儿何不带吴钩，', p:py('nán ér hé bù dài wú gōu')},
   {c:'收取关山五十州。', p:py('shōu qǔ guān shān wǔ shí zhōu')}],
  read:'男儿何不带吴钩，收取关山五十州。',
  yisi:'男子汉为什么不带上吴钩弯刀，去收复关塞山河之间的五十州？——「男儿何不带」劈头一问，反问里全是激愤：不是不能，而是不甘；「吴钩」是弯刀，也是军功的代称，「带吴钩」即佩刀出征；「收取关山五十州」直指当时朝廷政令不及的藩镇州郡——书生搁下笔、横起刀，把一腔建功立业的壮志，说成了一道掷地有声的反问。',
  zhu:[['南园·其五','李贺《南园十三首》的第五首——组诗多写昌谷家园的田园物候与书生怀抱；此首由书斋起意，一转而为投笔从戎的慷慨之问，是组诗中最负盛名的一首'],['吴钩','吴地所产的弯形宝刀，刀头弯曲如钩，泛指锋利的佩刀——「带吴钩」即佩刀从军；唐代诗文中「吴钩」常与建功立业的豪气相连'],['男儿何不带','为什么不做/不带——反问起句，激愤与渴望并见：身在书斋而心向关山，一句反问把「书生无用武之地」的处境全盘托出'],['关山五十州','关塞山河之间的众多州郡——指当时藩镇割据、不受朝命的大河南北数十州；「收取」二字极有力量：不是游赏，是收复失地、削平藩镇的建功之志'],['李贺与南园','李贺（790—816），字长吉，中唐诗人，人称「诗鬼」。家居昌谷，有南园；他曾在此读书应举——书案之上、一笔一刀之间，正是「投笔从戎」两难的写照']] },
{ name:'凌烟之问', jing:'请您姑且登上凌烟阁看一看：阁上二十四功臣，哪一个是书生封的万户侯？——功名图像的召唤，亦是书生的不平之问。（凌烟阁 · 二十四功臣 · 万户侯 · 标志性瞬间 · 末境点击画面：阁上功臣画像次第显影+吴钩寒光）',
  segs:[
   {c:'请君暂上凌烟阁，', p:py('qǐng jūn zàn shàng líng yān gé')},
   {c:'若个书生万户侯。', p:py('ruò gè shū shēng wàn hù hóu')}],
  read:'请君暂上凌烟阁，若个书生万户侯。',
  yisi:'请您姑且登上凌烟阁看一看：那上面受表彰的功臣之中，哪一个是靠做书生封了万户侯的？——「请君暂上」妙在只请人登阁一望，答案便自分明；「若个」即「哪个」，反问收束、掷地有声：凌烟阁二十四功臣，皆是马上取功名之人——两问相对：上句问「何不」带吴钩，下句问「若个」是书生，慷慨与愤懑交织，正是书生报国无路的一声长叹。',
  zhu:[['凌烟阁','唐代长安太极宫中的高楼。贞观十七年（643），唐太宗为表彰开国功臣，命阎立本绘长孙无忌、魏徵、尉迟敬德等二十四功臣真人大小画像于阁中——「上凌烟阁」即功名图像的召唤，是唐人心目中人臣功名的顶点'],['请君暂上','请您姑且登上——「暂」字妙：不必真去，只消登阁看一眼功臣画像，答案自明；是对听者的设问，更是对时代的质问'],['若个','哪个、谁——「若个书生万户侯」：凌烟阁上功臣图像里，哪一个是单凭做书生封万户侯的？反问作结，斩截有力'],['万户侯','食邑万户的侯爵，汉代侯爵的最高一等，后世泛指极高的爵位功名——功名图像的顶点，正是书生难及之处'],['投笔从戎之叹','东汉班超掷笔感叹大丈夫当立功异域，遂投笔从戎。李贺身为书生而向往军功：一问「何不带吴钩」，再问「若个书生万户侯」——慷慨之中，藏着中唐书生干谒无门、报国无路的愤懑与不甘']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「男儿何不带吴钩」的下一句是？', o:['收取关山五十州','请君暂上凌烟阁','若个书生万户侯'], a:0},
 {q:'「请君暂上凌烟阁」的下一句是？', o:['收取关山五十州','若个书生万户侯','男儿何不带吴钩'], a:1},
 {q:'「吴钩」「万户侯」「若个」的读音和意思，都正确的一项是？', o:['钩读 gōu，弯刀；侯读 hóu，侯爵功名；若个即「哪个」——带上吴钩收复关山：凌烟阁功臣里，哪个书生封过万户侯？','钩读 gòu，钩子；侯读 hòu，等待；若个即「这个」——带上钩子去收关山：这个书生等到了万户侯','钩读 jù，铁钩；侯读 hóu，猴子；若个即「几个」——拿铁钩逗猴子：几个书生都封了万户侯'], a:0},
 {q:'关于凌烟阁与本诗作者，下列说法正确的是？', o:['凌烟阁是唐玄宗为赏花所建的楼阁，绘有名花图卷；本诗作者李贺是盛唐边塞将领，久经战阵后归隐南园','凌烟阁在唐代长安太极宫——贞观十七年唐太宗命阎立本绘二十四功臣真人大小画像于阁上；本诗作者李贺是中唐诗人，诗风奇诡冷艳，人称「诗鬼」，《南园十三首》是其家园组诗','凌烟阁是汉代藏书之阁，绘有历代儒生画像；李贺官至宰相，《南园》写于致仕归隐之后'], a:1},
 {q:'对「男儿何不带吴钩，收取关山五十州。请君暂上凌烟阁，若个书生万户侯。」全诗主旨理解最恰当的一项是？', o:['写南园田园风光正好，劝人安心耕读，不必羡慕军功爵禄','两问相对：既是「何不带吴钩」投笔从戎的壮志——书生亦当提刀收复关山；又是「若个书生万户侯」的不平之问——凌烟功名原非书生可得；慷慨与愤懑交织，正是李贺怀才不遇、渴望建功的心声','讽刺凌烟阁画像画技拙劣，把功臣都画成了武将模样，替书生鸣不平'], a:1},
];
"""

SCENES_JS = """/* ================= 南园·其五 · 两境场景（大漠金戈·书生投笔：吴钩关山、凌烟之问） =================
   美术立意：大漠金戈色板写「书斋掷笔→吴钩关山→凌烟之问」——底色 #120d08、雾 #150e08～#141014 系，
   accent=#c9a06a（沙金/绢帛金）只落在阁檐边缘光/功臣画像暖辉/铜格/窗纸暖光/UI 上，禁艳金。
   全页唯一冷色源是「吴钩」：钢青 0x8a9aaa～0xecf3f9 只属于刀——暖阁金辉与冷刃寒光对撞出「功名之问」。
   与已有边塞页第一眼可区分：不做战阵/夜射/行军/听笛/白骨/骏马/剑庐，从「南园书斋田园」起手——
   书案掷笔、刀架横钩、篱笆田家；烽燧/城郭灯火铺出「收取关山五十州」的版图意象（边塞页未用过的钉子）。
   境壹（暮·起）：书案掷笔、吴钩横架，诗人指顾关山，烽燧城郭灯火列成五十州。
   境贰（夜·问，标志性瞬间+末境可点击）：凌烟阁三重楼阁横空；点击——阁上二十四功臣画像
   自下而上次第显影（各自 emissive 渐亮），阁前金辉漫开，末了前景吴钩寒光乍现
   （点击凌烟阁——阁上功臣画像次第显影+吴钩寒光）。 */

/* —— 吴钩 makeWugou(o)：弯刃宝刀——柄在下（-Y），刃沿圆弧上弯前伸（单侧刃、渐收、末有锋尖）。
   刀身材质 emissive 可控寒光（钢青，全页唯一冷色源）；柄首缠丝、铜镡一线 accent。
   返回 {g, bladeMat} */
function makeWugou(o){
  o=o||{};
  const R0=o.R===undefined?2.1:o.R, SPAN=o.span===undefined?0.66:o.span;
  const g=new THREE.Group();
  const bladeMat=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:46,
    specular:0x9fb0be,emissive:0x9ab4c8,emissiveIntensity:0});
  const B=new GeoBag();
  const pts=[];
  for(let i=0;i<=7;i++){
    const a=SPAN*i/7;
    pts.push([R0*(1-Math.cos(a)),R0*Math.sin(a),0]);
  }
  const cols=[0x565f6a,0x6d7783,0x85909c,0x9faab6,0xb9c3ce,0xcfd9e2,0xe0e9f0];
  for(let i=0;i<7;i++){
    const r0=0.055-0.024*(i/7), r1=0.055-0.024*((i+1)/7);
    B.put(limbGeo(pts[i],pts[i+1],r0,r1,5),cols[i]);
  }
  const dx=Math.cos(SPAN),dy=Math.sin(SPAN);
  const tip=new THREE.ConeGeometry(0.026,0.34,5);
  tip.rotateZ(Math.atan2(dy,dx)-Math.PI/2);
  tip.translate(pts[7][0]+dx*0.16,pts[7][1]+dy*0.16,0);
  B.put(tip,0xecf3f9);
  const blade=B.mesh(bladeMat); g.add(blade);
  const B2=new GeoBag();
  const hilt=new THREE.CylinderGeometry(0.032,0.038,0.46,7); hilt.translate(0,-0.24,0); B2.put(hilt,0x241b12);
  for(let i=0;i<3;i++){
    const ring=new THREE.TorusGeometry(0.040,0.009,5,12); ring.rotateX(Math.PI/2);
    ring.translate(0,-0.10-i*0.12,0); B2.put(ring,0x7a5c38);
  }
  const guard=new THREE.BoxGeometry(0.20,0.05,0.09); guard.translate(0,0.015,0); B2.put(guard,0x5a4830);
  const gline=new THREE.BoxGeometry(0.21,0.014,0.095); gline.translate(0,0.046,0); B2.put(gline,0xc9a06a);
  const pom=new THREE.SphereGeometry(0.058,8,6); pom.translate(0,-0.50,0); B2.put(pom,0x5a4830);
  B2.put(limbGeo([0,-0.53,0],[-0.075,-0.95,0.02],0.020,0.007,4),0x6a3020);
  B2.put(limbGeo([0,-0.53,0],[0.06,-0.92,-0.03],0.020,0.007,4),0x7a3a26);
  g.add(B2.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x4a4030,emissive:0x060402}),{c:0xc9a06a,i:o.rim===undefined?0.22:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g:g,bladeMat:bladeMat};
}

/* —— 刀架 makeDaojia(o)：双柱斜撑横担的兵器架（合批 1 mesh）——吴钩悬架其上 */
function makeDaojia(o){
  o=o||{};
  const w=o.w===undefined?3.2:o.w, h=o.h===undefined?1.15:o.h;
  const B=new GeoBag();
  const base=new THREE.BoxGeometry(w+0.8,0.14,1.1); base.translate(0,0.07,0.05); B.put(base,0x1c130b);
  for(let s=0;s<2;s++){
    const x=(s?1:-1)*w*0.5;
    B.put(limbGeo([x,0.12,-0.22],[x,h,0],0.075,0.06,5),0x2a1c10);
    B.put(limbGeo([x,0.12,0.40],[x,h,0],0.075,0.06,5),0x2a1c10);
  }
  const bar=new THREE.CylinderGeometry(0.055,0.055,w,7); bar.rotateZ(Math.PI/2);
  bar.translate(0,h,0); B.put(bar,0x33220f);
  for(let s=0;s<2;s++){
    const notch=new THREE.TorusGeometry(0.075,0.022,5,10); notch.rotateY(Math.PI/2);
    notch.translate((s?1:-1)*w*0.28,h,0); B.put(notch,0x6a5434);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a2c1a,emissive:0x050302}),{c:0xc9a06a,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 南园书斋 makeShuzhai(o)：茅檐草堂+前廊两柱+一段篱笆（合批 1 mesh + 1 窗光面片）
   ——田园村居的南园气：堂屋更宽、茅檐双层、篱笆围院（非荒野独庐） */
function makeShuzhai(o){
  o=o||{};
  const w=o.w===undefined?7.4:o.w, d=o.d===undefined?5.0:o.d, h=o.h===undefined?3.3:o.h;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,h,d); wall.translate(0,h*0.5,0); B.put(wall,0x1b130a);
  const roof=new THREE.ConeGeometry(Math.max(w,d)*0.86,2.2,4); roof.rotateY(Math.PI/4);
  roof.scale(1,1,d/w); roof.translate(0,h+1.05,0); B.put(roof,0x2e2212);
  const eave=new THREE.ConeGeometry(Math.max(w,d)*1.06,0.85,4); eave.rotateY(Math.PI/4);
  eave.scale(1,1,d/w); eave.translate(0,h+0.42,0); B.put(eave,0x241a0d);
  const door=new THREE.BoxGeometry(1.2,2.1,0.10); door.translate(w*0.16,1.05,d*0.5+0.02); B.put(door,0x0b0704);
  const win=new THREE.BoxGeometry(1.55,1.05,0.06); win.translate(-w*0.22,h*0.52,d*0.5+0.02); B.put(win,0x30200f);
  for(let s=0;s<2;s++){
    const px=(s?1:-1)*w*0.30;
    B.put(limbGeo([px,0,d*0.5+0.62],[px,h+0.42,d*0.5+0.55],0.09,0.075,5),0x2a1c10);
  }
  const fz=w*0.5+3.4, z0=d*0.5+1.6;
  for(let i=0;i<9;i++){
    const px=-fz+i*(2*fz/8);
    const st=new THREE.CylinderGeometry(0.045,0.055,1.05,5); st.translate(px,0.52,z0); B.put(st,0x2a1e10);
  }
  for(let r=0;r<2;r++){
    const rail=new THREE.BoxGeometry(2*fz,0.07,0.05); rail.translate(0,0.38+r*0.44,z0); B.put(rail,0x241a0d);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2012,emissive:0x040302}),{c:0xc9a06a,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  const winMat=new THREE.MeshBasicMaterial({color:0xd8a060,transparent:true,opacity:o.win===undefined?0.36:o.win});
  const glow=new THREE.Mesh(new THREE.PlaneGeometry(1.3,0.86),winMat);
  glow.position.set(-w*0.22,h*0.52,d*0.5+0.06); g.add(glow);
  g.userData.update=function(t,k){ winMat.opacity=k*(o.win===undefined?0.36:o.win)*(0.88+0.12*Math.sin(t*0.85)); };
  return g;
}

/* —— 案头文房 makeWenfang(o)：摊开的书卷+砚墨+一管掷下的毛笔（书卷砚墨合批 1 mesh，笔独立）
   ——毛笔斜出案沿，是「投笔」一瞬的定格 */
function makeWenfang(o){
  o=o||{};
  const B=new GeoBag();
  const juan=new THREE.CylinderGeometry(0.085,0.085,0.95,8); juan.rotateZ(Math.PI/2);
  juan.translate(0.05,0.09,-0.10); B.put(juan,0x6a5636);
  for(let s=0;s<2;s++){
    const ax=new THREE.CylinderGeometry(0.048,0.048,0.10,6); ax.rotateZ(Math.PI/2);
    ax.translate(0.05+(s?0.505:-0.505),0.09,-0.10); B.put(ax,0x2a1c10);
  }
  const sheet=new THREE.BoxGeometry(0.86,0.014,0.52); sheet.rotateY(0.10);
  sheet.translate(-0.15,0.008,0.34); B.put(sheet,0xd8ccb0);
  const line=new THREE.BoxGeometry(0.70,0.002,0.016); line.rotateY(0.10);
  line.translate(-0.15,0.017,0.30); B.put(line,0x6a5a40);
  const yan=new THREE.BoxGeometry(0.30,0.07,0.22); yan.translate(0.62,0.035,0.42); B.put(yan,0x14100c);
  const ink=new THREE.CylinderGeometry(0.028,0.032,0.16,6); ink.translate(0.52,0.08,0.30); B.put(ink,0x0d0b08);
  const bi=new THREE.Group();
  const BB=new GeoBag();
  const gan=new THREE.CylinderGeometry(0.021,0.026,0.56,6); gan.translate(0,0.28,0); BB.put(gan,0x8a6a3a);
  const feng=new THREE.ConeGeometry(0.045,0.20,6); feng.translate(0,-0.10,0); BB.put(feng,0x2a2018);
  bi.add(BB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x4a3a26,emissive:0x040302}),{c:0xc9a06a,i:0.18,p:2.4})));
  bi.rotation.z=-1.95; bi.position.set(0.02,0.03,0.16);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x4a3a26,emissive:0x050402}),{c:0xc9a06a,i:0.16,p:2.4})));
  g.add(bi);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 烽燧 makeFengsui(o)：收分方塔+雉堞+顶上一粒烽火余光（合批 1 mesh + 1 火光 sprite）
   ——「收取关山五十州」的版图钉子（边塞页未用过烽燧） */
function makeFengsui(o){
  o=o||{};
  const h=o.h===undefined?6.5:o.h, fire=o.fire===undefined?0.30:o.fire;
  const B=new GeoBag();
  const body=new THREE.CylinderGeometry(0.95,1.45,h,4); body.rotateY(Math.PI/4);
  body.translate(0,h*0.5,0); B.put(body,0x191009);
  for(let i=0;i<4;i++){
    const a=Math.PI/4+i*Math.PI/2;
    const cr=new THREE.BoxGeometry(0.34,0.42,0.34);
    cr.translate(Math.cos(a)*1.0,h+0.2,Math.sin(a)*1.0); B.put(cr,0x140d07);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2012,emissive:0x030201}),{c:0xc9a06a,i:o.rim===undefined?0.12:o.rim,p:2.2})));
  const fm=new THREE.SpriteMaterial({map:glowTex(),color:0xd88a3a,transparent:true,opacity:fire,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const fs=new THREE.Sprite(fm); fs.scale.set(1.7,1.7,1); fs.position.set(0,h+0.55,0); fs.renderOrder=4;
  g.add(fs);
  g.userData.update=function(t,k){ fm.opacity=k*fire*(0.72+0.28*Math.sin(t*1.7+(o.ph||0))); };
  g.scale.setScalar(o.s===undefined?1:o.s);
  return g;
}

/* —— 城郭 makeChengguo(o)：夯土城墙+门楼+女墙垛口剪影（合批 1 mesh）——五十州的一座州城 */
function makeChengguo(o){
  o=o||{};
  const w=o.w===undefined?16:o.w, h=o.h===undefined?2.6:o.h;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,h,1.6); wall.translate(0,h*0.5,0); B.put(wall,0x150e08);
  const gate=new THREE.BoxGeometry(2.6,h*0.72,0.5); gate.translate(0,h*0.36,0.65); B.put(gate,0x0a0603);
  const tower=new THREE.BoxGeometry(3.4,1.5,2.2); tower.translate(0,h+0.75,0); B.put(tower,0x120c07);
  const troof=new THREE.ConeGeometry(2.6,1.0,4); troof.rotateY(Math.PI/4);
  troof.translate(0,h+2.0,0); B.put(troof,0x1c130a);
  for(let i=0;i<7;i++){
    const cr=new THREE.BoxGeometry(0.5,0.4,1.6);
    cr.translate(-w*0.5+0.6+i*(w-1.2)/6,h+0.2,0); B.put(cr,0x120c07);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a2012,emissive:0x030201}),{c:0xc9a06a,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 凌烟阁 makeLingyange(o)：唐风三重楼阁——台基两级+前阶、三层阁身逐层收分、腰檐出挑、
   顶檐正脊鸱吻；前脸 24 龛功臣画像（每层 8 龛自下而上）：龛暗底并入阁身合批，
   画像（幞头冠+面容+肩甲）为独立小 mesh、各自 emissive 材质——显影前 visible=false 硬关。
   返回 {g, ps[24], mats[24], th[24]} */
function makeLingyange(o){
  o=o||{};
  const W=o.W===undefined?12:o.W, tiers=3, bh=o.bh===undefined?3.0:o.bh, rh=o.rh===undefined?1.15:o.rh;
  const B=new GeoBag();
  const b1=new THREE.BoxGeometry(W+4.4,0.9,W*0.44+2.2); b1.translate(0,0.45,0); B.put(b1,0x17100a);
  const b2=new THREE.BoxGeometry(W+2.2,0.8,W*0.40+1.2); b2.translate(0,1.25,0); B.put(b2,0x1a120b);
  const step=new THREE.BoxGeometry(3.2,0.72,2.6); step.translate(0,0.36,(W*0.44+2.2)/2+1.1); B.put(step,0x140d08);
  let y=1.65;
  const ps=[],mats=[],th=[];
  for(let t=0;t<tiers;t++){
    const w=W*(1-0.14*t), dep=W*0.40*(1-0.10*t);
    const body=new THREE.BoxGeometry(w,bh,dep); body.translate(0,y+bh*0.5,0); B.put(body,0x221610);
    for(let c=0;c<5;c++){
      const col=new THREE.CylinderGeometry(0.16,0.17,bh*0.94,7);
      col.translate(-w*0.42+c*w*0.21,y+bh*0.47,dep*0.5+0.10); B.put(col,0x2c1c12);
    }
    const lan=new THREE.BoxGeometry(w*0.96,0.10,0.08); lan.translate(0,y+1.0,dep*0.5+0.30); B.put(lan,0x3a2818);
    for(let i=0;i<8;i++){
      const px=-w*0.40+i*(w*0.8/7);
      const recess=new THREE.BoxGeometry(1.28,1.62,0.10); recess.translate(px,y+bh*0.55,dep*0.5+0.02);
      B.put(recess,0x120b06);
      const PB=new GeoBag();
      const sh=new THREE.BoxGeometry(1.06,0.56,0.07); sh.translate(0,-0.30,0); PB.put(sh,0xf0dcbc);
      const hd=new THREE.SphereGeometry(0.30,8,7); hd.scale(0.94,1.06,0.5); hd.translate(0,0.18,0); PB.put(hd,0xe8d0b0);
      const guan=new THREE.BoxGeometry(0.40,0.20,0.36); guan.translate(0,0.44,0); PB.put(guan,0x1c1410);
      const m=new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
        specular:0x3a3026,emissive:0xd8a860,emissiveIntensity:0});
      const pm=PB.mesh(m);
      pm.position.set(px,y+bh*0.55-0.20,dep*0.5+0.12); pm.visible=false;
      ps.push(pm); mats.push(m); th.push((t*8+i+0.6)/25.2);
    }
    const roof=new THREE.ConeGeometry(w*0.78,rh,4); roof.rotateY(Math.PI/4);
    roof.scale(1.12,1,0.92); roof.translate(0,y+bh+rh*0.42,0); B.put(roof,0x241709);
    const eave=new THREE.BoxGeometry(w*1.5,0.14,dep*1.42); eave.translate(0,y+bh-0.10,0); B.put(eave,0x1e1207);
    y+=bh+rh*0.85;
  }
  const top=new THREE.ConeGeometry(W*0.52,1.7,4); top.rotateY(Math.PI/4); top.scale(1.15,1,0.9);
  top.translate(0,y+0.8,0); B.put(top,0x261908);
  const ridge=new THREE.BoxGeometry(W*0.78,0.22,0.4); ridge.translate(0,y+1.62,0); B.put(ridge,0x1c1206);
  for(let s=0;s<2;s++){
    const qw=new THREE.BoxGeometry(0.30,0.62,0.30);
    qw.translate((s?1:-1)*W*0.38,y+1.55,0); B.put(qw,0x201407);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a2a18,emissive:0x060402}),{c:0xc9a06a,i:o.rim===undefined?0.16:o.rim,p:2.3})));
  for(let i=0;i<ps.length;i++)g.add(ps[i]);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return {g:g,ps:ps,mats:mats,th:th};
}

/* 诗人李贺：全诗贯穿的同一造型（幞头青袍，与《马诗》页同一诗人的照面；每次 build 新建材质） */
function nyFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x262220,belt:0x6a5434,skin:0xd9b189,collar:0x45403a,
    hair:0x171208,hat:'幞头',beard:true,rimC:0xc9a06a,rim:0.44,noProp:true,scale:scale===undefined?1.7:scale});
}

function bCover(){ // 卷首 · 南园暮色远望：书斋暖窗一线、烽燧一点、州城灯火、低月昏黄
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0x0f0a06,c2:0x1d140b,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:300,h:18,layers:2,peaks:5,seed:22601,color:0x0d0906,atmo:0x2e2114,
    fogK:0.62,glowK:0.05,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-20,0,-98); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:235,h:11,layers:2,peaks:4,seed:22602,color:0x0c0805,atmo:0x2e2114,
    fogK:0.58,glowK:0.04,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(18,0,-58); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  const hut=makeShuzhai({win:0.30}); hut.position.set(8.5,-1.60,-27); hut.rotation.y=-0.42; g.add(hut);
  const fs1=makeFengsui({h:5.8,fire:0.22,ph:1.2}); fs1.position.set(-14,-1.72,-46); g.add(fs1);
  const lights=makeGlow({n:18,box:[150,6,22],pos:[0,1.0,-44],color:0xd8a060,size:1.5,speed:0.05,rise:0.02,add:true,maxA:0.06});
  g.add(lights.points);
  const fly=makeGlow({n:10,box:[34,4,16],pos:[0,0.8,-9],color:0xd8b070,size:1.1,speed:0.3,rise:0.22,add:true,maxA:0.07});
  g.add(fly.points);
  const wind=makeFlow({n:280,box:[96,10,40],pos:[0,3.2,-22],color:0x46382a,size:15,speed:4.0,maxA:0.11});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[215,13,78],pos:[0,5,-54],scale:70,color:0x3a2c1c,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.8,w:12,d:5,color:0x14121a,seed:22603,rim:0.08,rimC:0xc9a06a});
  fg1.g.position.set(-11.5,-1.9,14); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',n:4,w:12,d:4,color:0x0e0906,seed:22604,sway:0.8,rim:0.08,rimC:0xc9a06a});
  fg2.g.position.set(11.5,6.0,13); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.30,p:[-42,48,-26]},{c:0x281c10,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); grd.update();
    hut.userData.update(t,k); fs1.userData.update(t,k);
    lights.update(t); fly.update(t); wind.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bGuanshan(){ // 壹 · 吴钩关山 —— 男儿何不带吴钩，收取关山五十州：书斋掷笔、横刀指顾关山
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0f0a06,c2:0x1e140b,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:22,layers:2,peaks:5,seed:22611,color:0x0b0910,atmo:0x2e2114,
    fogK:0.64,glowK:0.05,glow:0xd8a860,y:-11,order:-6});
  ridge.g.position.set(-22,0,-104); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:240,h:13,layers:2,peaks:4,seed:22612,color:0x0a080c,atmo:0x2e2114,
    fogK:0.60,glowK:0.05,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(18,0,-60); ridge2.g.rotation.y=Math.PI; g.add(ridge2.g);
  /* 五十州版图：城郭横陈 + 烽燧两点 + 州城灯火 + 远行男儿一列 */
  const cg=makeChengguo({w:17}); cg.position.set(-6.5,-1.72,-46); cg.rotation.y=-0.15; g.add(cg);
  const fs1=makeFengsui({h:6.5,ph:0.4}); fs1.position.set(11.5,-1.72,-36); g.add(fs1);
  const fs2=makeFengsui({h:5.2,fire:0.24,ph:2.1}); fs2.position.set(-16,-1.72,-53); g.add(fs2);
  const lights=makeGlow({n:22,box:[168,7,24],pos:[0,1.1,-47],color:0xd8a060,size:1.6,speed:0.05,rise:0.02,add:true,maxA:0.07});
  g.add(lights.points);
  const crowd=makeCrowd({n:6,rect:[-46,-54,86,8],seed:22613,color:0x171219,rimC:0xc9a06a,rim:0.10,
    sMin:0.42,sMax:0.55,y:0});
  crowd.mesh.position.y=-1.85; g.add(crowd.mesh);
  /* 南园书斋退居左侧：一窗暖光 */
  const hut=makeShuzhai({win:0.42}); hut.position.set(-11.0,-1.60,-24); hut.rotation.y=0.40; g.add(hut);
  /* 书案文房：摊开的书卷与掷下的笔（投笔定格） */
  const an=makeTable({w:3.6,d:1.6,h:1.15,wood:0x241810}); an.g.position.set(-3.4,-1.8,-7.6);
  an.g.rotation.y=0.16; g.add(an.g);
  const wf=makeWenfang(); wf.position.set(0,1.16,0.02); an.g.add(wf);
  const dl=new THREE.PointLight(0xd8a060,0.55,9); dl.position.set(-3.0,0.6,-5.6); g.add(dl);
  /* 刀架横钩：吴钩在架、微芒内敛（全页冷色源；点击前不上寒光） */
  const dj=makeDaojia(); dj.position.set(3.1,-1.8,-8.6); dj.rotation.y=-0.5; g.add(dj);
  const wg=makeWugou({scale:1.1}); wg.g.position.set(3.1,-0.55,-8.5); wg.g.rotation.y=-0.5;
  wg.g.rotation.z=-1.42; wg.bladeMat.emissiveIntensity=0.16; g.add(wg.g);
  const cl=new THREE.PointLight(0x9ab0c0,1.05,13); cl.position.set(3.6,1.1,-6.6); g.add(cl);
  /* 诗人：立于案旁，抬手指顾关山 */
  const poet=nyFigure(1.72,'指月'); poet.position.set(-0.6,-1.78,-6.4); poet.rotation.y=2.75; g.add(poet);
  /* 园中流萤与沙风夜雾 */
  const fly=makeGlow({n:12,box:[32,4,18],pos:[0,0.8,-10],color:0xd8b070,size:1.1,speed:0.32,rise:0.24,add:true,maxA:0.07});
  g.add(fly.points);
  const wind=makeFlow({n:300,box:[92,10,38],pos:[0,3.2,-20],color:0x46382a,size:15,speed:4.2,maxA:0.11});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,13,76],pos:[0,5,-52],scale:68,color:0x3a2c1c,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x0d0805,seed:22614,rim:0.09,rimC:0xc9a06a});
  fg1.g.position.set(-11.5,-1.8,13); g.add(fg1.g);
  const fg2=makeForeground({kind:'树枝',n:4,w:12,d:4,color:0x0e0906,seed:22615,sway:0.7,rim:0.08,rimC:0xc9a06a});
  fg2.g.position.set(11,6.2,12); g.add(fg2.g);
  addLights(g,{c:0xa8824e,i:0.30,p:[-40,46,-24]},{c:0x281c10,i:0.54});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); grd.update();
    hut.userData.update(t,k); fs1.userData.update(t,k); fs2.userData.update(t,k);
    crowd.update(t);
    poet.update(t,k);
    fly.update(t); wind.update(t); mist.update(t,k);
    fg1.update(t,k); fg2.update(t,k);
  }};
}
function bLingyan(){ // 贰（末境·可点击）· 凌烟之问 —— 请君暂上凌烟阁，若个书生万户侯：画像次第显影+吴钩寒光
  const ctl={t:0,clicked:false,on:false,reveal:0,lit:[],pt:[],flashed:false,gt:0};
  const g=new THREE.Group();
  const grd=makeGround({r:240,c1:0x0d0a07,c2:0x1a120a,y:-1.8}); g.add(grd.mesh);
  const ridge=makeRange({r:310,h:16,layers:2,peaks:4,seed:22631,color:0x0b0806,atmo:0x2e2114,
    fogK:0.62,glowK:0.10,glow:0xd8a860,y:-10,order:-6});
  ridge.g.position.set(-8,0,-116); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:240,h:10,layers:2,peaks:4,seed:22632,color:0x0a070c,atmo:0x2e2114,
    fogK:0.58,glowK:0.06,glow:0xd8a860,y:-8,order:-5});
  ridge2.g.position.set(26,0,-70); ridge2.g.rotation.y=Math.PI*0.9; g.add(ridge2.g);
  /* 凌烟阁：三重楼阁横空，二十四功臣画像显影前全部硬关（无幻影） */
  const ly=makeLingyange({scale:1.55}); ly.g.position.set(4.5,-1.70,-34); ly.g.rotation.y=-0.12; g.add(ly.g);
  /* 阁前金辉：显影进度渐起（初值=最大，逐帧乘 fadeK） */
  const pl=new THREE.PointLight(0xd8a860,1.05,70); pl.position.set(4.5,9.0,-22); g.add(pl);
  /* 前景：吴钩在架（冷色源），点击末了寒光乍现 */
  const dj=makeDaojia(); dj.position.set(3.6,-1.8,-6.4); dj.rotation.y=-0.35; g.add(dj);
  const wg=makeWugou({scale:1.1}); wg.g.position.set(3.6,-0.55,-6.3); wg.g.rotation.y=-0.35;
  wg.g.rotation.z=-1.42; wg.bladeMat.emissiveIntensity=0.16; g.add(wg.g);
  const gleamMat1=new THREE.SpriteMaterial({map:glowTex(),color:0xcfdce8,transparent:true,opacity:0.50,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const gl1=new THREE.Sprite(gleamMat1); gl1.scale.set(0.5,1.5,1); gl1.position.set(0.12,0.78,0.10);
  gl1.renderOrder=4; gl1.visible=false; wg.g.add(gl1);
  const gleamMat2=new THREE.SpriteMaterial({map:glowTex(),color:0xe4ecf2,transparent:true,opacity:0.36,
    depthWrite:false,fog:false,blending:THREE.AdditiveBlending});
  const gl2=new THREE.Sprite(gleamMat2); gl2.scale.set(0.34,0.9,1); gl2.position.set(0.30,1.10,0.10);
  gl2.renderOrder=4; gl2.visible=false; wg.g.add(gl2);
  const burst=makeBurst({n:40,color:0xcfdce8,pos:[0.25,0.9,0.12]});
  wg.g.add(burst.points);
  const cl2=new THREE.PointLight(0xa8c2d8,0.9,16); cl2.position.set(4.2,0.9,-4.8); g.add(cl2);
  /* 诗人：阁下仰望（「暂上」之前的凝望），镜头缓升如登阁 */
  const poet=nyFigure(1.78,'独立'); poet.position.set(-4.6,-1.78,-9.5); poet.rotation.y=0.9; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.1,w:8,d:4,color:0x0d0906,seed:22633,rim:0.11,rimC:0xc9a06a});
  rock.g.position.set(-5.6,-1.55,-11.2); g.add(rock.g);
  /* 阁下远处的谒者人影（一层纵深） */
  const crowd=makeCrowd({n:4,rect:[-3,-30,13,4],seed:22634,color:0x161018,rimC:0xc9a06a,rim:0.08,
    sMin:0.5,sMax:0.6,y:0});
  crowd.mesh.position.y=-1.8; g.add(crowd.mesh);
  const shimmer=makeGlow({n:26,box:[90,12,40],pos:[0,5,-16],color:0x8a8074,size:2.0,speed:0.10,rise:-0.06,add:false,maxA:0.08});
  g.add(shimmer.points);
  const wind=makeFlow({n:280,box:[90,10,36],pos:[0,3.4,-18],color:0x46382a,size:15,speed:4.0,maxA:0.10});
  g.add(wind.points);
  const mist=makeMist({n:6,spread:[210,13,76],pos:[0,5,-54],scale:68,color:0x302824,op:0.11});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:2.4,w:11,d:5,color:0x0d0805,seed:22635,rim:0.10,rimC:0xc9a06a});
  fg1.g.position.set(-11.5,-1.8,12.5); g.add(fg1.g);
  const fg2=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x0d0805,seed:22636,rim:0.10,rimC:0xc9a06a});
  fg2.g.position.set(12.2,-1.7,12); g.add(fg2.g);
  addLights(g,{c:0x9aa8b8,i:0.30,p:[-46,50,-26]},{c:0x261d14,i:0.54});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/3.4);
      if(ctl.on){
        for(let i=0;i<24;i++){
          if(ctl.reveal>=ly.th[i]){
            if(!ctl.lit[i]){ ctl.lit[i]=true; ly.ps[i].visible=true; ctl.pt[i]=0; }
            ctl.pt[i]+=dt;
            const e=Math.min(1,ctl.pt[i]/0.55), es=e*e*(3-2*e);
            ly.mats[i].emissiveIntensity=k*(0.30+0.62*es);
          }
        }
      }
      const prog=ctl.reveal*ctl.reveal*(3-2*ctl.reveal);
      if(ctl.on&&ctl.reveal>=0.965&&!ctl.flashed){ ctl.flashed=true; ctl.gt=0; burst.fire();
        gl1.visible=true; gl2.visible=true; }
      if(ctl.flashed)ctl.gt+=dt;
      const fk=ctl.flashed?Math.exp(-ctl.gt*1.5):0;      // 吴钩寒光包络（快衰减）
      wg.bladeMat.emissiveIntensity=k*(0.16+0.78*fk);
      gleamMat1.opacity=k*0.50*fk;
      gleamMat2.opacity=k*0.36*fk*(0.8+0.2*Math.sin(t*8.3));
      cl2.intensity=k*0.9*(0.10+0.72*fk);
      pl.intensity=k*1.05*(0.05+0.52*prog+0.16*fk);
      ridge.update(t,0); ridge2.update(t,0); grd.update();
      crowd.update(t);
      poet.update(t,k); rock.update(t,k);
      shimmer.update(t); wind.update(t); mist.update(t,k);
      fg1.update(t,k); fg2.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.20);                                          // 夜风
        pluck(7,0.0,0.12); pluck(4,0.30,0.10); pluck(5,0.66,0.10); pluck(2,1.05,0.09);   // 阁铃四声
        const fl=$('#flash'); fl.textContent='请君暂上凌烟阁 若个书生万户侯';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
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
  cam:{f:[0,7.8,42],t:[0,8.2,34],lf:[1.2,7.6,-26],lt:[-2.2,7.9,-40]},
  sky:()=>SK({fd:0.0048,star:0.12}) },
{ name:'吴钩关山',dwell:16,river:0.02,build:bGuanshan,
  cam:{f:[0.2,5.7,19.5],t:[0.5,5.4,15.5],lf:[0.2,5.3,-14],lt:[2.0,5.7,-26]},
  sky:()=>SK({top:C(0x0d0a08),hor:C(0x261a10),bot:C(0x0a0705),fog:C(0x150e08),fd:0.0054,star:0.20,
    ms:0.42,mph:0.50,mhaze:0.14,moon:new THREE.Vector3(-66,46,-190),
    dirC:C(0x9aa6b4),dirI:0.26,dirP:new THREE.Vector3(-40,40,-26),
    ambC:C(0x261c12),ambI:0.52}) },
{ name:'凌烟之问',dwell:19,river:0.02,build:bLingyan,
  cam:{f:[0,5.4,16.5],t:[0.3,5.8,13.5],lf:[1.0,6.8,-26],lt:[0.6,9.0,-38]},
  sky:()=>SK({top:C(0x0c0e14),hor:C(0x201814),bot:C(0x08070a),fog:C(0x141014),fd:0.0056,star:0.30,
    ms:0.55,mph:0.30,mhaze:0.12,moon:new THREE.Vector3(-84,56,-196),
    dirC:C(0x9aa8b8),dirI:0.30,dirP:new THREE.Vector3(-46,48,-28),
    ambC:C(0x241c16),ambI:0.54}) },
];
"""
