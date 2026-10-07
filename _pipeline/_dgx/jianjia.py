# -*- coding: utf-8 -*-
"""jianjia.py —— 《蒹葭》（先秦·诗经·秦风，queue no.254，烟雨江南·秋水苇荡变体）生成配置
3 境（三章一境，重章叠句一章一境）：
境壹白露为霜（标志性瞬间：霜烟浩渺，伊人宛在水中央，雾中若近若远）、
境贰白露未晞（晨光微明，伊人移立水中坻之湄，露珠未干）、
境叁白露未已（末境可点击：点击溯洄溯游——一苇以航，伊人若近若远）。
美术立意「一水三岸，伊人宛在」：三章重章叠句 = 三境变奏——
时间递进（为霜→未晞→未已，露渐收而晨光渐明）、位置推移（水中央→水中坻→水中沚）、
苇色递变（苍苍→萋萋→采采）。烟雨江南全套色板（bg #10141a、雾 #151d26、accent=#8fb3c9
只落在 UI/伊人边缘辉光/水路光痕/露光/苇尖霜光上），霜白 0xcadbe6 系为本诗独有的冷白。
与已有烟雨江南页第一眼可区分：不做深巷小楼杏花雨（linan-chunyu）、不做十里柳堤六朝残影
（taicheng）、不做客舟酒楼樱桃芭蕉（yijianmei-zhouguo）——本页无建筑无市井，
只有水泽苇荡、霜白烟水、一个可望而不可即的伊人剪影。
自建 builder：makeReedClumpJJ（苇丛）/ makeIsletJJ（水中洲坻）/ makeYirenJJ（伊人剪影）/
makeBoatJJ（苇叶小舟）/ makeWaterPathJJ（溯洄水路光痕，点击前 visible=false 硬关）。
考点钉子：蒹葭 jiān jiā／晞 xī／湄 méi／坻 chí／涘 sì／沚 zhǐ（小测第 3 题）；
《诗经》重章叠句（第 4 题）；「所谓伊人」求而不得与朦胧多义（第 5 题）。
多音字：为霜 wéi、坻 chí、跻 jī 等（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='jianjia', title='蒹葭', dyn='先秦 · 诗经', brand_author='诗 经',
    gold_rgb='143,179,201',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#8fb3c9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(143,179,201,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#10141a', 2),
        ('rgba(5,8,15', 'rgba(9,12,17', 1),
        ('rgba(4,6,11', 'rgba(8,11,16', 2),
        ('rgba(6,9,16', 'rgba(9,12,18', 1),
        ('rgba(3,5,9', 'rgba(7,9,14', 1),
        ('#0b101c', '#131a24', 1),
        ('#6f664f', '#5f6a7a', 1),
        ('#5a5340', '#525c6c', 1),
    ],
    tip='轻点溯洄水路 / 按空格 —— 一苇以航，雾中伊人若近若远',
    hint='← → 键或空格逐境游览 · 末境可点击溯洄溯游：一苇以航，雾中伊人若近若远',
    cover_read='蒹葭。先秦，诗经。蒹葭苍苍，白露为霜。所谓伊人，在水一方。溯洄从之，道阻且长。溯游从之，宛在水中央。',
    cover_p1='三重意境，随诗句次第展开：芦苇苍苍，白露凝霜，心中思慕的那个人，就在河水的那一方；苇色萋萋，白露未干，她又仿佛立在水草相接的岸边；苇色采采，露水未已，她又在水边高地上——溯洄从之，道阻且长；溯游从之，宛在水中洲沚。',
    cover_p2='边读诗，边随一叶苇舟溯洄而上：伊人总在眼前恍惚，总隔着一水，总追不上——这份可望而不可即，两千年后仍是我们共同的怅惘。末境轻点画面，一苇以航，看雾中伊人若近若远。',
    end_h2='宛在 · 水中央', cn_word='三',
    words_js="['再溯一回，秋水蒹葭','初识诗经，尚需共读','渐入诗境，再诵几遍','白露渐晞，伊人渐近','已解重章叠唱之妙','宛在水中央，求索不歇']",
    sky_atmo='0x344052',
)

POEM_JS = """const POEM = [
{ name:'白露为霜', jing:'河边芦苇苍苍茫茫，清晨的白露凝成了秋霜；心中思慕的那个人，就在河水的那一方。逆流而上去追寻，道路险阻而且漫长；顺流而下去追寻，她仿佛又立在水中央。（蒹葭 · 白露 · 伊人）（标志性瞬间：霜烟浩渺，雾中伊人若近若远）',
  segs:[
   {c:'蒹葭苍苍，', p:py('jiān jiā cāng cāng')},
   {c:'白露为霜。', p:py('bái lù wéi shuāng')},
   {c:'所谓伊人，', p:py('suǒ wèi yī rén')},
   {c:'在水一方。', p:py('zài shuǐ yī fāng')},
   {c:'溯洄从之，', p:py('sù huí cóng zhī')},
   {c:'道阻且长。', p:py('dào zǔ qiě cháng')},
   {c:'溯游从之，', p:py('sù yóu cóng zhī')},
   {c:'宛在水中央。', p:py('wǎn zài shuǐ zhōng yāng')}],
  read:'蒹葭苍苍，白露为霜。所谓伊人，在水一方。溯洄从之，道阻且长。溯游从之，宛在水中央。',
  yisi:'河边的芦苇苍苍茫茫，清晨的白露凝结成霜。我心中思慕的那个人啊，就站在河水的那一方。逆着流水去追寻她，道路险阻而且漫长；顺着流水去追寻她，她仿佛又在水的中央。——首章以「蒹葭」起兴：深秋拂晓，苇色苍苍，白露凝霜，一片清寥的秋境先立起来，怀人的深情才有处安放。「在水一方」把伊人推到可望而不可即的距离——她并非不在，只是隔着一片秋水；「溯洄」「溯游」上下求索，写尽追寻的执着；「道阻且长」是路途之难，「宛在水中央」是伊人之恍惚——一个「宛」字，似真似幻、若近若远，求而不得的怅惘尽在其中。',
  zhu:[['蒹葭','芦苇。蒹，荻苇，芦苇一类的草；葭，初生的芦苇——蒹葭连用，泛指水边的芦荻'],['苍苍','茂盛、众多貌，一说灰白色——深秋苇色苍茫的样子'],['白露为霜','晶莹的露水凝结成霜。为，凝结成，读 wéi——点明深秋拂晓，天气由凉转寒'],['伊人','那个人，心中思慕的对象——可解为恋人、贤才，也可解为理想与向往，历代多义'],['在水一方','在河的另一边。一方，那一边，即水的对岸'],['溯洄从之','逆流而上去追寻她。溯洄，逆着水流向上游走；从，追寻、追随'],['溯游从之','顺着流水去追寻她。溯游，顺着水流向下游走'],['道阻且长','道路险阻而且漫长。阻，艰险、难走'],['宛','仿佛、好像——「宛在」似真似幻，正是可望而不可即之感']] },
{ name:'白露未晞', jing:'河边芦苇萋萋繁茂，晶莹的露水还没有晒干；心中思慕的那个人，就立在水草相接的岸边。逆流而上去追寻，道路险阻而且步步登高；顺流而下去追寻，她仿佛又立在水中的小洲上。（芦苇萋萋 · 白露未晞 · 在水之湄）',
  segs:[
   {c:'蒹葭萋萋，', p:py('jiān jiā qī qī')},
   {c:'白露未晞。', p:py('bái lù wèi xī')},
   {c:'所谓伊人，', p:py('suǒ wèi yī rén')},
   {c:'在水之湄。', p:py('zài shuǐ zhī méi')},
   {c:'溯洄从之，', p:py('sù huí cóng zhī')},
   {c:'道阻且跻。', p:py('dào zǔ qiě jī')},
   {c:'溯游从之，', p:py('sù yóu cóng zhī')},
   {c:'宛在水中坻。', p:py('wǎn zài shuǐ zhōng chí')}],
  read:'蒹葭萋萋，白露未晞。所谓伊人，在水之湄。溯洄从之，道阻且跻。溯游从之，宛在水中坻。',
  yisi:'河边的芦苇萋萋繁茂，晶莹的露水还没有晒干。我心中思慕的那个人啊，就立在水草相接的岸边。逆着流水去追寻她，道路险阻而且步步登高；顺着流水去追寻她，她仿佛又立在水中的小洲上。——次章与首章句式全同，只换数字：「苍苍」换作「萋萋」，苇色愈见繁盛；「为霜」换作「未晞」，时间从霜重的拂晓向前推移；「一方」换作「湄」，伊人似乎近了一点；「长」换作「跻」，路愈走愈高；「中央」换作「坻」。重章不是简单的重复——苇色在变、天光在变、伊人的位置在变、追寻的难度在变，不变的是那份执着与怅惘。一唱三叹，情随境迁而愈深，这正是《诗经》重章叠句的妙处。',
  zhu:[['萋萋','茂盛的样子——与「苍苍」同写苇色，而更显繁密'],['未晞','还没有晒干。晞，晒干，读 xī——露水未干，时序在「为霜」之后向前推移'],['在水之湄','在水草相接的岸边。湄，水边、水与草相接之处，读 méi——伊人仿佛比「一方」更近了'],['道阻且跻','道路险阻而且步步升高。跻，升高、路陡，读 jī'],['坻','水中的小洲或高地，读 chí——「宛在水中坻」，伊人的身影又换了一处']] },
{ name:'白露未已', jing:'河边芦苇繁密鲜明，露水还挂在苇叶上没有收尽；心中思慕的那个人，就立在水边的高地上。逆流而上去追寻，道路险阻而且迂回曲折；顺流而下去追寻，她仿佛又立在水中的小沙洲上。（芦苇采采 · 溯洄溯游 · 水中沚）（末境点击画面：溯洄溯游——一苇以航，雾中伊人若近若远）',
  segs:[
   {c:'蒹葭采采，', p:py('jiān jiā cǎi cǎi')},
   {c:'白露未已。', p:py('bái lù wèi yǐ')},
   {c:'所谓伊人，', p:py('suǒ wèi yī rén')},
   {c:'在水之涘。', p:py('zài shuǐ zhī sì')},
   {c:'溯洄从之，', p:py('sù huí cóng zhī')},
   {c:'道阻且右。', p:py('dào zǔ qiě yòu')},
   {c:'溯游从之，', p:py('sù yóu cóng zhī')},
   {c:'宛在水中沚。', p:py('wǎn zài shuǐ zhōng zhǐ')}],
  read:'蒹葭采采，白露未已。所谓伊人，在水之涘。溯洄从之，道阻且右。溯游从之，宛在水中沚。',
  yisi:'河边的芦苇繁密鲜明，露水还挂在苇叶上没有收尽。我心中思慕的那个人啊，就立在水边的高地上。逆着流水去追寻她，道路险阻而且迂回曲折；顺着流水去追寻她，她仿佛又立在水中的小沙洲上。——末章再换数字收束全篇：「采采」写苇色之盛，「未已」承「未晞」更进一层——露始终不干，这秋晨仿佛也始终不肯放亮；「涘」「右」「沚」又是一番位置与路途的推移。三章往复回环，如秋水拍岸一遍又一遍：空间的推移（方→湄→涘，央→坻→沚）是追寻的脚步，时间的推移（为霜→未晞→未已）是不舍的晨光，而「宛」字三见——她总在眼前恍惚，总隔着一水，总追不上。「伊人」是谁？恋人、贤才、理想，朦胧多义；这份可望而不可即的怅惘与不肯止息的追寻，正是这首诗两千多年来常读常新的缘故。',
  zhu:[['采采','繁盛、鲜明众多的样子——苇色到末章最盛'],['未已','还没有完、露水未止——承「未晞」更进一层，秋晨迟迟不散'],['在水之涘','在水边的崖岸上。涘，水边、岸边，读 sì'],['道阻且右','道路险阻而且迂回曲折。右，迂回曲折，一说道路向右弯曲'],['沚','水中的小块陆地，比「坻」更小，读 zhǐ——伊人愈立愈远愈小'],['重章叠句','《诗经》常见章法：各章句式全同、只换少数字，反复咏唱、一唱三叹——本诗三章正用此法'],['赋比兴之「兴」','先言他物以引起所咏之词——以蒹葭白露起兴，引出「所谓伊人」的怀人之情']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「蒹葭苍苍，白露为霜。」的下一句是？', o:['所谓伊人，在水一方','所谓伊人，在水之湄','溯洄从之，道阻且长'], a:0},
 {q:'「溯洄从之，道阻且长。」的下一句是？', o:['溯游从之，宛在水中坻','溯游从之，宛在水中央','溯游从之，宛在水中沚'], a:1},
 {q:'下列各句中加点字的读音和解释，全都正确的一项是？', o:['「蒹葭」读 jiān jiā，指芦苇；「晞」读 xī，晒干；「湄」读 méi，水边','「蒹葭」读 qiān jiā，指荻花；「晞」读 xī，黄昏；「湄」读 méi，水中小洲','「蒹葭」读 jiān xiá，指芦芽；「晞」读 xī，黎明；「湄」读 méi，河堤'], a:0},
 {q:'全诗三章字句基本相同，只更换「苍苍／萋萋／采采」「霜／晞／已」「方／湄／涘」「央／坻／沚」等少数字，反复咏唱。对这种手法及其效果，理解正确的一项是？', o:['顶真——上句的结尾作下句的开头，词句蝉联而下，气脉紧连','互文——上下两句参互成文，合而见义，行文简洁','重章叠句——回环往复、一唱三叹，苇色、天光、伊人的位置层层推移，情感愈唱愈深'], a:2},
 {q:'对「所谓伊人，在水一方」的理解，下列说法最恰当的一项是？', o:['伊人可望而不可即，求而不得——「伊人」朦胧多义，可以是思慕的人、贤才，也可以是美好的理想，执着与怅惘并存','伊人就在对岸，只是诗人不熟悉水性，诗歌意在说明出门办事要提前查好路线','伊人是实有其人的邻家访客，诗歌记录一次寻常的访友不遇，意在介绍秦地水乡风物'], a:0},
];
"""

SCENES_JS = """/* ================= 蒹葭 · 三境场景（烟雨江南·秋水苇荡变体：白露为霜、白露未晞、白露未已） =================
   美术立意：「一水三岸，伊人宛在」——秋晨水泽，霜白烟水，苇荡连绵；
   三章重章叠句 = 三境变奏：时间递进（为霜→未晞→未已，露渐收而晨光渐明）、
   位置推移（伊人在水中央→水中坻→水中沚，若远若近）、苇色递变（苍苍→萋萋→采采）。
   母题贯穿：①伊人剪影（半透淡青白，雾中若近若远）②蜿蜒溯洄水路（境叁）③苇荡洲沚。
   accent=#8fb3c9 只落在 UI/伊人边缘辉光/水路光痕/露光/苇尖霜光；霜白 0xcadbe6 为本诗独有的冷白。
   与已有烟雨江南页第一眼可区分：不做深巷小楼杏花雨（linan-chunyu）、不做十里柳堤六朝残影
   （taicheng）、不做客舟酒楼樱桃芭蕉（yijianmei-zhouguo）——本页无建筑无市井，
   只有水泽苇荡、霜白烟水、一个可望而不可即的伊人。 */

/* —— 苇丛 makeReedClumpJJ(o)：一墩芦苇（苇秆分段微弯 + 苇穗扁穗头），合批 1 mesh ——
   蒹葭三变：base（秆色）与 tip（穗色）随章递变（苍苍灰白→萋萋灰绿→采采鲜明），穗头凝霜微亮 */
function makeReedClumpJJ(o){
  o=o||{};
  const n=o.n===undefined?14:o.n, R=seedRnd(o.seed===undefined?25401:o.seed);
  const w=o.w===undefined?4.2:o.w, hh=o.h===undefined?5.4:o.h;
  const base=o.base===undefined?0x232b2f:o.base, tipC=o.tip===undefined?0x93a4ae:o.tip;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*w*0.7, H=hh*(0.55+0.65*R());
    let px=x, py=0, pz=z, pr=0.062;
    const segs=4;
    for(let k=0;k<segs;k++){
      const nx=x+(R()-0.5)*0.55*(k+1)/segs, ny=H*(k+1)/segs, nz=z+(R()-0.5)*0.35*(k+1)/segs;
      const nr=pr*0.84;
      B.put(limbGeo([px,py,pz],[nx,ny,nz],pr,nr,4),shadeColor(base,0.8+0.5*R()));
      px=nx; py=ny; pz=nz; pr=nr;
    }
    const pl=new THREE.SphereGeometry(pr*7,5,4);
    pl.scale(1,2.3,1); pl.rotateZ((R()-0.5)*0.5); pl.translate(px,py+pr*5,pz);
    B.put(pl,shadeColor(tipC,0.82+0.4*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a4a56,emissive:0x06090c}),{c:o.rimC===undefined?0x8fb3c9:o.rimC,i:o.rim===undefined?0.16:o.rim,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.020*Math.sin(t*0.55+ph)*kk;
    g.rotation.x=0.012*Math.sin(t*0.41+ph*1.7)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 水中洲坻 makeIsletJJ(o)：低平土洲（压扁穹丘 + 洲顶缓台），合批 1 mesh ——
   「水中坻」「水中沚」的落点：伊人所立之处 */
function makeIsletJJ(o){
  o=o||{};
  const r=o.r===undefined?3.4:o.r, hh=o.h===undefined?1.0:o.h;
  const B=new GeoBag();
  const dome=new THREE.SphereGeometry(r,12,7,0,Math.PI*2,0,Math.PI/2);
  dome.scale(1,hh/r,1); B.put(dome,0x18202a);
  const top=new THREE.SphereGeometry(r*0.72,10,6,0,Math.PI*2,0,Math.PI/2);
  top.scale(1,hh*0.30/r,1); top.translate(0,hh*0.62,0); B.put(top,0x1c2531);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a3844,emissive:0x05080c}),{c:o.rimC===undefined?0x8fb3c9:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.2})));
  return g;
}

/* —— 伊人 makeYirenJJ(o)：雾中伊人剪影（先秦深衣：长衣垂袖 + 顶髻），合批 1 mesh
   + 身后一枚柔光（fog:false 加色）。半透淡青白、含蓄无面目——「宛在」之物，似真似幻；
   update(t,k,env)：呼吸式明灭与缓漂（若近若远），env（点击溯洄）增幅仍在初值以内 */
function makeYirenJJ(o){
  o=o||{};
  const bodyOp=o.op===undefined?0.40:o.op;
  const glowOp=o.glowOp===undefined?0.10:o.glowOp;
  const B=new GeoBag();
  const pts=[[0.02,0],[0.30,0.02],[0.34,0.10],[0.30,0.42],[0.25,0.86],[0.21,1.22],[0.17,1.46],[0.10,1.56],[0.03,1.62]]
    .map(function(p){ return new THREE.Vector2(p[0],p[1]); });
  const robe=new THREE.LatheGeometry(pts,14);
  robe.scale(1,1.52,0.78); B.put(robe,0xffffff);
  const head=new THREE.SphereGeometry(0.115,8,7); head.translate(0,1.70,0); B.put(head,0xffffff);
  const bun=new THREE.SphereGeometry(0.055,6,5); bun.translate(0,1.82,-0.05); B.put(bun,0xffffff);
  [1,-1].forEach(function(s){
    B.put(limbGeo([s*0.24,1.46,0],[s*0.30,0.95,0.02],0.055,0.045,5),0xffffff);
    B.put(limbGeo([s*0.30,0.95,0.02],[s*0.31,0.52,0.04],0.045,0.035,5),0xffffff);
  });
  const mesh=new THREE.Mesh(mergeGeos(B.list),
    new THREE.MeshBasicMaterial({color:o.color===undefined?0xe2ecf4:o.color,transparent:true,
      opacity:bodyOp,depthWrite:false}));
  mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.glowC===undefined?0x8fb3c9:o.glowC,
    transparent:true,opacity:glowOp,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(o.glowW===undefined?3.4:o.glowW,o.glowH===undefined?4.6:o.glowH,1);
  glow.position.set(0,2.5,0.2); glow.renderOrder=3; g.add(glow);
  g.scale.setScalar(o.scale===undefined?2.4:o.scale);
  const ph=(o.seed===undefined?25402:o.seed)%6.283;
  let lx=null, lz=null;
  g.update=function(t,k,env){ const kk=k===undefined?1:k, e=env===undefined?0:env;
    if(lx===null){ lx=g.position.x; lz=g.position.z; }
    const br=0.78+0.16*Math.sin(t*0.30+ph);                 /* 呼吸明灭（≤1） */
    mesh.material.opacity=kk*bodyOp*Math.min(1,br+0.20*e);  /* 点击增幅仍在初值内 */
    const drift=0.35*Math.sin(t*0.11+ph)+0.9*e;             /* 缓漂 + 点击时向深处退（若近若远） */
    g.position.x=lx+drift*0.5;
    g.position.z=lz-drift;
    glow.material.opacity=kk*glowOp*Math.min(1,br*0.8+0.4*e);
    g.visible=kk>0.004;
  };
  g.userData.update=g.update;
  return g;
}

/* —— 苇叶小舟 makeBoatJJ(o)：细长苇叶舟（无篷，与客舟/渔船造型区分）：舟体细长两头翘，
   浅舱沿 + 舟底接触阴影，合批 1 mesh ——「一苇以航」的溯洄之具 */
function makeBoatJJ(o){
  o=o||{};
  const L=o.L===undefined?4.6:o.L, B=new GeoBag();
  const mid=new THREE.BoxGeometry(L*0.62,0.42,L*0.24); mid.translate(0,0.34,0); B.put(mid,0x1a222c);
  const bow=new THREE.ConeGeometry(L*0.115,L*0.38,4); bow.rotateZ(-Math.PI/2);
  bow.scale(1,0.85,0.78); bow.translate(L*0.50,0.46,0); B.put(bow,0x1a222c);
  const stern=new THREE.ConeGeometry(L*0.115,L*0.34,4); stern.rotateZ(Math.PI/2);
  stern.scale(1,0.85,0.78); stern.translate(-L*0.50,0.44,0); B.put(stern,0x1a222c);
  const gun=new THREE.BoxGeometry(L*0.94,0.07,L*0.27); gun.translate(0,0.56,0); B.put(gun,0x2c3a4a);
  const shadow=new THREE.CircleGeometry(L*0.52,12); shadow.rotateX(-Math.PI/2);
  shadow.scale(1.25,1,0.55); shadow.translate(0,0.05,0); B.put(shadow,0x04070b);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x33414e,emissive:0x05070a}),{c:0x8fb3c9,i:0.20,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=(o.seed===undefined?25403:o.seed)%6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.025*Math.sin(t*0.75+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 溯洄水路 makeWaterPathJJ(o)：沿蜿蜒水路的光痕（Points 自定义着色器，uReveal 点亮）
   点击前 visible=false 硬关；update(t,k,rev)：rev 0..1 溯洄亮起→溯游渐隐 */
const JJ_PATH_VERT=`
attribute float aT;
uniform float uReveal; uniform float uDim;
varying float vA;
void main(){
  float lead=uReveal*1.08;
  float lit=1.0-smoothstep(0.0,0.22,lead-aT);
  vA=lit*uDim;
  vec4 mv=modelViewMatrix*vec4(position,1.0);
  gl_PointSize=(4.0+10.0*lit)*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const JJ_PATH_FRAG=`
uniform vec3 uC; uniform float uFade;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.5,0.10,length(q))*vA*uFade;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeWaterPathJJ(o){
  o=o||{};
  const pts=o.pts===undefined?[[0,0,0]]:o.pts, n=o.n===undefined?90:o.n;
  const curve=new THREE.CatmullRomCurve3(pts.map(function(p){ return new THREE.Vector3(p[0],p[1],p[2]); }));
  const pos=new Float32Array(n*3), tt=new Float32Array(n);
  for(let i=0;i<n;i++){
    const p=curve.getPoint(i/(n-1));
    pos[i*3]=p.x; pos[i*3+1]=p.y; pos[i*3+2]=p.z; tt[i]=i/(n-1);
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(pos,3));
  geo.setAttribute('aT',new THREE.BufferAttribute(tt,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uC:{value:C(0x9fc4dc)},uReveal:{value:0},uDim:{value:1},uFade:{value:0}},
    vertexShader:JJ_PATH_VERT,fragmentShader:JJ_PATH_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  const grp=new THREE.Group(); grp.add(points); grp.visible=false;
  grp.update=function(t,k,rev){ const kk=k===undefined?1:k, r=rev===undefined?0:rev;
    m.uniforms.uReveal.value=Math.min(1,r*1.15);
    m.uniforms.uDim.value=1-0.72*(r<0.5?0:(r-0.5)*2);
    grp.visible=kk*r>0.004;
  };
  grp.userData.update=grp.update;
  grp.curve=curve;
  return grp;
}

/* —— 秋水苇荡基底 makeMarshJJ(o)：浩渺水面 + 水下河滩 + 低平雾山环 ——
   山环放 z≈-135，在骨架常驻远山环（z≈-260…-330）之前，不被遮挡 */
function makeMarshJJ(o){
  o=o||{};
  const g=new THREE.Group();
  const water=makeWater({size:420,seg:84,amp:o.amp===undefined?0.13:o.amp,freq:0.16,speed:0.32,
    flow:[0.10,0.30],spec:0.90,deep:0x0a121b,shallow:0x18242f,skyc:0x2a3844,moonDir:[-30,14,-130]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x9fb8cc);
  water.mesh.position.set(0,-0.04,-30); g.add(water.mesh);
  const bed=makeGround({r:260,c1:0x0c1116,c2:0x182028,y:-0.5});
  bed.mesh.position.set(0,-0.5,-218); g.add(bed.mesh);
  const ridge=makeRange({r:250,h:13,layers:2,peaks:4,seed:o.seed===undefined?25411:o.seed,
    color:0x0c1218,atmo:0x2c3c4a,fogK:0.60,glowK:0.05,glow:0x9fb3c9,y:-12,order:-6});
  ridge.g.position.set(0,0,-135); g.add(ridge.g);
  return {g:g,water:water,ridge:ridge};
}

function bCover(){ // 卷首 · 秋水蒹葭 —— 苇荡苍苍，霜烟浩渺，伊人一点白影在水中央
  const g=new THREE.Group();
  const marsh=makeMarshJJ({seed:25411}); g.add(marsh.g);
  const s1=makeIsletJJ({r:4.0,h:1.1}); s1.position.set(-26,0,-62); g.add(s1);
  const c1=makeReedClumpJJ({seed:25421,tip:0x9fb0a8}); c1.position.set(-26,0.9,-62); g.add(c1);
  const c2=makeReedClumpJJ({seed:25422,tip:0x9fb0a8}); c2.position.set(21,0.8,-78); g.add(c2);
  const c3=makeReedClumpJJ({seed:25423,tip:0x9fb0a8,w:5,h:6}); c3.position.set(-40,0.9,-92); g.add(c3);
  const yr=makeYirenJJ({scale:2.6,op:0.36,glowOp:0.09,seed:25402}); yr.position.set(-16,0.1,-66); g.add(yr);
  const boat=makeBoatJJ({scale:1.0,seed:25403}); boat.position.set(-11,-0.02,-40); boat.rotation.y=1.1; g.add(boat);
  const crowd=makeCrowd({n:3,rect:[-34,-118,26,10],seed:25431,color:0x11171f,rimC:0x8fb3c9,rim:0.16});
  g.add(crowd.mesh);
  const frost=makeGlow({n:26,box:[170,3.5,90],pos:[0,1.0,-46],color:0xcadbe6,size:5.5,speed:0.02,rise:0,add:false,maxA:0.10});
  g.add(frost.points);
  const mist=makeMist({n:7,spread:[230,16,110],pos:[0,4.5,-42],scale:70,color:0x2c3c4e,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:30,box:[150,16,60],pos:[0,8,-40],color:0xa8c0d0,size:4.5,speed:0.03,rise:0,add:true,maxA:0.10});
  g.add(motes.points);
  const fgL=makeForeground({kind:'芦苇',w:16,n:11,d:4,color:0x060a0e,seed:25441,sway:1.0,tip:0x424f4a,scale:0.85});
  fgL.g.position.set(-13,-1.2,30); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:2.6,w:12,d:5,color:0x05080c,seed:25442,rim:0.12,rimC:0x8fb3c9});
  fgR.g.position.set(14,-1.4,32); g.add(fgR.g);
  addLights(g,{c:0xb0c2d2,i:0.42,p:[-38,70,26]},{c:0x1e2836,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    marsh.water.update(t); marsh.ridge.update(t,0);
    c1.update(t,k); c2.update(t,k); c3.update(t,k);
    yr.update(t,k); boat.update(t,k); crowd.update(t);
    frost.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bWeishuang(){ // 壹（标志性瞬间）· 白露为霜 —— 蒹葭苍苍，白露为霜，所谓伊人，宛在水中央：
                       // 霜烟浩渺的秋水上，伊人剪影静立水中央，若近若远
  const g=new THREE.Group();
  const marsh=makeMarshJJ({seed:25412,amp:0.12}); g.add(marsh.g);
  const c1=makeReedClumpJJ({seed:25424,base:0x232b2f,tip:0xc0cfd4}); c1.position.set(-17,0,-34); g.add(c1);
  const c2=makeReedClumpJJ({seed:25425,base:0x232b2f,tip:0xc0cfd4,w:5,h:6}); c2.position.set(15,0,-40); g.add(c2);
  const c3=makeReedClumpJJ({seed:25426,base:0x232b2f,tip:0xb0c2cc}); c3.position.set(-30,0,-58); g.add(c3);
  const s1=makeIsletJJ({r:3.2,h:0.9}); s1.position.set(28,0,-64); g.add(s1);
  const c4=makeReedClumpJJ({seed:25427,base:0x232b2f,tip:0xb0c2cc}); c4.position.set(28,0.7,-64); g.add(c4);
  const yr=makeYirenJJ({scale:3.0,op:0.46,glowOp:0.12,seed:25402,glowW:3.6,glowH:4.8});
  yr.position.set(-9,0.12,-44); g.add(yr);
  const crowd=makeCrowd({n:2,rect:[-30,-108,20,8],seed:25432,color:0x11171f,rimC:0x8fb3c9,rim:0.14});
  g.add(crowd.mesh);
  /* 白露为霜：水面霜光更重一层 */
  const frost=makeGlow({n:34,box:[170,3.5,90],pos:[0,1.0,-46],color:0xcadbe6,size:5.5,speed:0.02,rise:0,add:false,maxA:0.11});
  g.add(frost.points);
  const mist=makeMist({n:8,spread:[230,16,110],pos:[0,4.5,-46],scale:72,color:0x2e3e50,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:30,box:[150,16,60],pos:[0,8,-40],color:0xaec4d4,size:4.5,speed:0.03,rise:0,add:true,maxA:0.10});
  g.add(motes.points);
  const fgL=makeForeground({kind:'芦苇',w:14,n:9,d:3,color:0x060a0e,seed:25443,sway:1.0,tip:0x4a5a54,scale:0.8});
  fgL.g.position.set(-12,-1.2,17); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:2.4,w:10,d:4,color:0x05080c,seed:25444,rim:0.12,rimC:0x8fb3c9});
  fgR.g.position.set(12,-1.3,15); g.add(fgR.g);
  addLights(g,{c:0xb2c4d4,i:0.40,p:[-38,68,26]},{c:0x1e2836,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    marsh.water.update(t); marsh.ridge.update(t,0);
    c1.update(t,k); c2.update(t,k); c3.update(t,k); c4.update(t,k);
    yr.update(t,k); crowd.update(t);
    frost.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bWeixi(){ // 贰 · 白露未晞 —— 蒹葭萋萋，白露未晞；伊人在水之湄，宛在水中坻：
                   // 晨光微明，露珠未干点点微光，伊人移立左前小洲之湄
  const g=new THREE.Group();
  const marsh=makeMarshJJ({seed:25413,amp:0.13}); g.add(marsh.g);
  const islet=makeIsletJJ({r:4.4,h:1.2}); islet.position.set(-15.5,0,-42); g.add(islet);
  const cz1=makeReedClumpJJ({seed:25433,base:0x24312b,tip:0xa8b8ac}); cz1.position.set(-18.4,0.9,-45.5); g.add(cz1);
  const cz2=makeReedClumpJJ({seed:25434,base:0x24312b,tip:0xa8b8ac,w:3.4,h:4.6}); cz2.position.set(-13.0,0.8,-45.2); g.add(cz2);
  const yr=makeYirenJJ({scale:2.8,op:0.46,glowOp:0.11,seed:25402,glowW:3.4,glowH:4.6}); yr.position.set(-14.8,1.05,-38.8); g.add(yr);
  const c3=makeReedClumpJJ({seed:25435,base:0x24312b,tip:0xa8b8ac}); c3.position.set(20,0.8,-56); g.add(c3);
  const boat=makeBoatJJ({scale:1.0,seed:25403}); boat.position.set(6,-0.02,-10); boat.rotation.y=2.4; g.add(boat);
  /* 白露未晞：苇洲露珠点点微光 */
  const dew=makeGlow({n:30,box:[40,4,28],pos:[-15.5,2.4,-42],color:0xd8e8e4,size:3.0,speed:0.04,rise:0.35,add:true,maxA:0.12});
  g.add(dew.points);
  const mist=makeMist({n:7,spread:[230,16,110],pos:[0,4.5,-46],scale:72,color:0x2c3c4e,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[150,16,60],pos:[0,8,-40],color:0xb2c6d4,size:4.5,speed:0.03,rise:0,add:true,maxA:0.10});
  g.add(motes.points);
  const fgL=makeForeground({kind:'芦苇',w:10,n:9,d:3,color:0x060a0e,seed:25445,sway:1.0,tip:0x44524c,scale:0.75});
  fgL.g.position.set(-8,-1.3,13); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:10,n:8,d:3,color:0x060a0e,seed:25446,sway:0.9,tip:0x44524c,scale:0.75});
  fgR.g.position.set(9,-1.3,12); g.add(fgR.g);
  addLights(g,{c:0xb6c8d4,i:0.46,p:[-32,66,24]},{c:0x222c38,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    marsh.water.update(t); marsh.ridge.update(t,0);
    cz1.update(t,k); cz2.update(t,k); c3.update(t,k);
    yr.update(t,k); boat.update(t,k);
    dew.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bWeiyi(){ // 叁（末境·可点击）· 白露未已 —— 蒹葭采采，白露未已；伊人在水之涘，宛在水中沚：
                   // 近岸一叶苇舟；点击溯洄溯游：一苇以航，雾中伊人若近若远
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const ss=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  const g=new THREE.Group();
  const marsh=makeMarshJJ({seed:25414,amp:0.14}); g.add(marsh.g);
  /* 水中沚（伊人所立）：蒹葭采采最盛 */
  const islet=makeIsletJJ({r:3.6,h:1.0}); islet.position.set(-1.5,0,-30); g.add(islet);
  const cz=makeReedClumpJJ({seed:25436,base:0x263429,tip:0xacc4b4}); cz.position.set(1.4,0.7,-33.2); g.add(cz);
  const cz2=makeReedClumpJJ({seed:25437,base:0x263429,tip:0xacc4b4,w:3.2,h:4.4}); cz2.position.set(-4.4,0.6,-27.4); g.add(cz2);
  const yr=makeYirenJJ({scale:2.9,op:0.48,glowOp:0.13,seed:25402,glowW:3.4,glowH:4.6}); yr.position.set(-1.8,0.8,-29.4); g.add(yr);
  /* 溯洄水路：自小舟绕过苇洲直至沚前（点击前 visible=false 硬关） */
  const path=makeWaterPathJJ({n:96,
    pts:[[-6.5,0.14,0.5],[-5.6,0.14,-7.0],[-4.0,0.14,-13.0],[-1.8,0.14,-19.0],[-0.8,0.14,-24.0]]});
  g.add(path);
  /* 小舟与溯洄之人 */
  const boat=makeBoatJJ({scale:1.25,seed:25403}); boat.position.set(-6.5,0.0,0.5); g.add(boat);
  const seeker=makeFigure({pose:'独立',robe:0x2e3646,belt:0x7288a0,skin:0xd2b394,collar:0xa8b4c4,
    hair:0x14161c,hat:'无',rim:0.40,rimC:0x9fc0d8,noProp:true,scale:0.58});
  seeker.position.set(0.15,0.44,0); seeker.rotation.y=-0.5; boat.add(seeker);
  /* 白露未已：露光稀疏，晨光更明 */
  const dew=makeGlow({n:22,box:[80,4,44],pos:[0,1.6,-30],color:0xdcebe6,size:3.0,speed:0.04,rise:0.3,add:true,maxA:0.10});
  g.add(dew.points);
  const mist=makeMist({n:7,spread:[230,16,110],pos:[0,4.5,-46],scale:72,color:0x2c3c4e,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[150,16,60],pos:[0,8,-40],color:0xb6cad6,size:4.5,speed:0.03,rise:0,add:true,maxA:0.09});
  g.add(motes.points);
  const fgL=makeForeground({kind:'芦苇',w:12,n:10,d:3,color:0x060a0e,seed:25447,sway:1.1,tip:0x44524c,scale:0.75});
  fgL.g.position.set(-13,-1.4,8); g.add(fgL.g);
  const fgR=makeForeground({kind:'芦苇',w:10,n:8,d:3,color:0x060a0e,seed:25448,sway:1.0,tip:0x44524c,scale:0.75});
  fgR.g.position.set(10,-1.3,9); g.add(fgR.g);
  addLights(g,{c:0xbac9d4,i:0.48,p:[30,62,24]},{c:0x242e3a,i:0.68});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/8.0);
      const r=ctl.reveal;
      /* 溯洄（0→0.5 前行）→ 溯游（0.5→1 顺流而返） */
      const bp=r<0.5?0.94*ss(r/0.5):0.94*(1-ss((r-0.5)/0.5));
      const p=path.curve.getPoint(bp);
      boat.position.set(p.x,0.0,p.z);
      const tan=path.curve.getTangent(Math.min(0.999,Math.max(0.001,bp)));
      boat.rotation.y=Math.atan2(-tan.z,tan.x);
      boat.rotation.z=0.025*Math.sin(t*0.75)*k+0.02*Math.sin(r*6.283*2);
      const env=Math.sin(r*Math.PI);
      yr.update(t,k,env);
      path.update(t,k,r);
      cz.update(t,k); cz2.update(t,k);
      dew.update(t); mist.update(t,k); motes.update(t);
      seeker.update(t,k);
      marsh.water.update(t); marsh.ridge.update(t,0);
      fgL.update(t,k); fgR.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        setAmbience(0.12);
      }
      ctl.on=true; ctl.reveal=0;                 /* 可反复点：再溯洄一回 */
      pluck(2,0.00,0.11); pluck(3,0.55,0.10); pluck(4,1.10,0.09); pluck(5,1.70,0.09);   /* 溯洄 */
      pluck(4,3.60,0.08); pluck(3,4.15,0.07); pluck(2,4.70,0.06);                       /* 溯游 */
      const fl=$('#flash'); fl.textContent='所谓伊人 宛在水中央';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x161e26),hor:C(0x2e3e4c),bot:C(0x10141a),fog:C(0x151d26),fd:0.0074,star:0.08,
  moon:new THREE.Vector3(56,104,-208),ms:0.32,mph:0.42,mhaze:0.12,dirC:C(0xaec2d0),dirI:0.42,
  dirP:new THREE.Vector3(-38,70,26),ambC:C(0x1e2836),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.06,build:bCover,
  cam:{f:[0,7.5,46],t:[0,8.2,40],lf:[-2,4,-26],lt:[-3,4.4,-32]},
  sky:()=>SK({fd:0.0072,star:0.08,ms:0.34,mph:0.42}) },
{ name:'白露为霜',dwell:22,river:0.07,build:bWeishuang,
  cam:{f:[0,3.0,24],t:[0,3.2,21],lf:[0,2.8,-12],lt:[0,3.0,-34]},
  sky:()=>SK({top:C(0x141b23),hor:C(0x2b3a48),fd:0.0078,star:0.06,ms:0.30,mph:0.44,mhaze:0.14,
    dirC:C(0xb0c4d2),dirI:0.40,ambC:C(0x1e2836),ambI:0.66}) },
{ name:'白露未晞',dwell:22,river:0.07,build:bWeixi,
  cam:{f:[0.5,3.6,21],t:[-0.5,3.4,18],lf:[-7.4,3.2,-34],lt:[-8.6,3.2,-42]},
  sky:()=>SK({top:C(0x18222b),hor:C(0x33434f),fd:0.0072,star:0.05,ms:0.26,mph:0.44,mhaze:0.12,
    dirC:C(0xb6c8d4),dirI:0.46,dirP:new THREE.Vector3(-32,66,24),ambC:C(0x222c38),ambI:0.68}) },
{ name:'白露未已',dwell:24,river:0.08,build:bWeiyi,
  cam:{f:[-2.5,3.5,17],t:[-2.9,3.3,14],lf:[1.6,2.7,-16],lt:[2.4,2.7,-26]},
  sky:()=>SK({top:C(0x1a232c),hor:C(0x36464f),fd:0.0070,star:0.05,ms:0.26,mph:0.42,mhaze:0.12,
    dirC:C(0xbac9d4),dirI:0.48,dirP:new THREE.Vector3(30,62,24),ambC:C(0x242e3a),ambI:0.68}) },
];
"""

if __name__ == '__main__':
    print('jianjia.py —— 被 build.py 消费：python build.py jianjia')
