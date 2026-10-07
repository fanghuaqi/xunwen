# -*- coding: utf-8 -*-
"""taoyao.py —— 《桃夭》（先秦·诗经·周南，queue no.256，青绿春晓·桃林送嫁变体）生成配置
3 境（三章一境：华→实→叶的时间递进 + 婚嫁推进 于归→宜室→宜家）：
境壹灼灼其华（标志性瞬间：盛放桃林深处送嫁队列，落英缤纷，婚嫁喜送）、
境贰有蕡其实（花落结实，青枝缀实，家宅炊烟在望）、
境叁其叶蓁蓁（末境可点击：点击桃花次第盛放，送嫁队伍亮起）。
美术立意「三章一境·桃之婚嫁」：春晓桃林，一场婚嫁被整个春天祝福——
花是其人（灼灼其华喻新嫁娘之美）、实是其家（有蕡其实祝多子多福）、叶是其族（其叶蓁蓁祝家族兴旺）。
母题贯穿：①桃树三态（同源 builder 参数变奏）②送嫁队伍（含蓄剪影+花轿）③落英 ④家宅炊烟 ⑤一湾溪水。
青绿春晓全套色板（bg #0a1410、雾 #0e1d16），accent=#c9a0a8（桃粉）只落在 UI/花瓣/
桃花盛放光点/灯笼暖光/队伍亮起上。
与已有青绿页第一眼可区分：不做三色花田春游（xingxiangzi-shurao）、不做山寺桃花
（dalinsi-taohua）、不做村居田园（cunju 等）——本页=桃林深处一场婚嫁，
桃花、桃实、桃荫三章递进，送嫁队伍与家宅炊烟是画面叙事的两岸。
自建 builder：makePeachTreeTY（桃树三态：华/实/叶）/ makePetalTY（落英缤纷，自写着色器缓落）/
makeBloomPointsTY（点击桃花次第盛放的光点，点击前 visible=false 硬关）/
makeSedanTY（花轿剪影）/ makeHomeTY（茅檐家宅+炊烟）/ makeGroveTY（春晓桃林基底）。
考点钉子：夭 yāo／蕡 fén／蓁 zhēn（小测第 3 题）；《诗经》重章叠句+桃夭是祝嫁诗（第 4 题）；
「于归/宜其室家」的祝福与比兴（第 5 题）。
多音字：华 huā（灼灼其华）、蕡 fén、蓁 zhēn、夭 yāo（tts.json sub 表，防误读）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=3, slug='taoyao', title='桃夭', dyn='先秦 · 诗经', brand_author='诗 经',
    gold_rgb='201,160,168',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#c9a0a8; --ink:#eef4e6; --dim:#8aa892; --paper:rgba(10,18,14,.60);
  --line:rgba(201,160,168,.30);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#0a1410', 2),
        ('rgba(5,8,15', 'rgba(6,12,9', 1),
        ('rgba(4,6,11', 'rgba(5,10,7', 2),
        ('rgba(6,9,16', 'rgba(6,11,8', 1),
        ('rgba(3,5,9', 'rgba(4,8,6', 1),
        ('#0b101c', '#0e1a14', 1),
        ('#6f664f', '#5f7264', 1),
        ('#5a5340', '#52604f', 1),
    ],
    tip='轻点画面 / 按空格 —— 桃花次第盛放，送嫁队伍亮起',
    hint='← → 键或空格逐境游览 · 壹境看灼灼其华的婚嫁喜送 · 末境可点击画面：桃花次第盛放，送嫁队伍亮起',
    cover_read='桃夭。先秦，诗经。桃之夭夭，灼灼其华。之子于归，宜其室家。桃之夭夭，有蕡其实。之子于归，宜其家室。桃之夭夭，其叶蓁蓁。之子于归，宜其家人。',
    cover_p1='三重意境，随诗句次第展开：桃树茁壮摇曳，桃花开得灼灼明艳，姑娘出嫁的队伍走在花影之间——愿她的家庭和顺美满；花落之后，桃子结得肥硕累累——愿她的家室幸福兴旺；桃叶密密层层、绿叶成荫——愿她一家和乐、人丁兴旺。',
    cover_p2='边读诗，边走进三千年前那片春天的桃林：一场婚嫁正被整个春天祝福着——花是其人，实是其家，叶是其族。末境轻点画面，看桃花次第再放、送嫁队伍亮起。',
    end_h2='宜其 · 家人', cn_word='三',
    words_js="['再入桃林，春晓正好','初识诗经，尚需共读','渐入诗境，再诵几遍','灼灼在目，于归在望','已解比兴祝福之妙','绿叶成荫，宜室宜家']",
    sky_atmo='0x2e4436',
)

POEM_JS = """const POEM = [
{ name:'灼灼其华', jing:'桃树茁壮摇曳，桃花开得灿烂明艳；这位姑娘就要出嫁，定使家庭和顺美满。（桃花盛放 · 之子于归 · 婚嫁喜送）（标志性瞬间：灼灼其华之子于归——盛放桃林深处的送嫁队列，落英缤纷）',
  segs:[
   {c:'桃之夭夭，', p:py('táo zhī yāo yāo')},
   {c:'灼灼其华。', p:py('zhuó zhuó qí huā')},
   {c:'之子于归，', p:py('zhī zǐ yú guī')},
   {c:'宜其室家。', p:py('yí qí shì jiā')}],
  read:'桃之夭夭，灼灼其华。之子于归，宜其室家。',
  yisi:'桃树多么茁壮，桃花开得灿烂明艳。这位姑娘就要出嫁了，定能使家庭和顺美满。——首章以盛放的桃花起兴：「夭夭」写桃树少壮摇曳之貌，「灼灼」写花开如火之明——两个字把春光的明媚全推到眼前，也为全诗定下喜庆明亮的调子；以花之艳起兴，引出人之美，桃花的明艳与新娘的青春互相映衬，这是《诗经》比兴手法的典范。「之子于归」点出正题：这位姑娘出嫁了；「宜」字是全诗祝福的核心——宜，和顺、美好，这里用作动词「使……和美」，一句「宜其室家」，把对新人的祝愿说得含蓄而隆重。',
  zhu:[['桃之夭夭','桃树多么茁壮茂盛。之，用在主谓之间，带咏叹语气；夭夭，草木茂盛、生机勃勃的样子，读 yāo'],['灼灼','花开繁盛、鲜艳明亮的样子，明亮如火烧——写桃花之艳，也暗喻新娘的青春光彩'],['华','同「花」，花朵——古无「花」字，先秦诗文皆作「华」，读 huā'],['之子','这位姑娘。之，这、此；子，古代对男女青年的美称，这里指出嫁的女子'],['于归','出嫁。于，往、到；归，女子出嫁——古人认为女子出嫁到夫家才是找到归宿'],['宜其室家','使家庭和顺美满。宜，和顺，用作动词「使……和美」；室家，家庭——与下两章「家室」「家人」同义而换字']] },
{ name:'有蕡其实', jing:'桃树茁壮摇曳，桃子结得肥硕累累；这位姑娘就要出嫁，定使家室幸福美满。（花落结实 · 青枝缀实 · 家宅炊烟）',
  segs:[
   {c:'桃之夭夭，', p:py('táo zhī yāo yāo')},
   {c:'有蕡其实。', p:py('yǒu fén qí shí')},
   {c:'之子于归，', p:py('zhī zǐ yú guī')},
   {c:'宜其家室。', p:py('yí qí jiā shì')}],
  read:'桃之夭夭，有蕡其实。之子于归，宜其家室。',
  yisi:'桃树多么茁壮，桃子结得又肥又大。这位姑娘就要出嫁了，定能使家室幸福美满。——第二章从花写到实：花期过后，枝头缀满肥硕的果实，由「美」进而祝愿「多子多福」——在先民的观念里，人丁兴旺是家庭幸福最实在的标志。章法与首章全同，只换「华」为「实」、「室家」为「家室」：重章不是简单的重复，而是把祝福一层层推进——先祝其人美，再祝其家兴。画面里花渐落而实渐肥，家宅炊烟在望，正是「成家立室」的春天。',
  zhu:[['有蕡其实','桃子结得又肥又大。蕡，果实肥大的样子，读 fén；实，果实；有，助词，放在动词前凑足音节'],['实','果实——由「华（花）」到「实」，祝福由容貌之美推进到生儿育女、多子多福'],['家室','家庭，与首章「室家」同义互文——换字不改义，正见重章叠唱之妙'],['宜其家室','使家室幸福美满——祝愿新人婚后家业兴旺、日子红火']] },
{ name:'其叶蓁蓁', jing:'桃树茁壮摇曳，桃叶密密层层成荫；这位姑娘就要出嫁，定使一家人和顺幸福。（绿叶成荫 · 浓荫覆路 · 家人团聚）（末境点击画面：桃花次第盛放——送嫁队伍亮起）',
  segs:[
   {c:'桃之夭夭，', p:py('táo zhī yāo yāo')},
   {c:'其叶蓁蓁。', p:py('qí yè zhēn zhēn')},
   {c:'之子于归，', p:py('zhī zǐ yú guī')},
   {c:'宜其家人。', p:py('yí qí jiā rén')}],
  read:'桃之夭夭，其叶蓁蓁。之子于归，宜其家人。',
  yisi:'桃树多么茁壮，桃叶长得密密层层、绿荫如盖。这位姑娘就要出嫁了，定能使一家人和顺幸福。——第三章由实写到叶：绿叶成荫，浓荫覆路，由「多子」再推到「旺族」——「家人」比「室家」「家室」范围更广，祝福从一对新人扩大到整个家族的兴旺。三章只换四组字（夭夭／灼灼／有蕡其实／其叶蓁蓁，室家／家室／家人），句式回环往复，正是《诗经》重章叠句的典型章法；以桃起兴、以人作结，花、实、叶三层递进，美、福、寿三层祝愿——这首两千多年前的婚礼祝歌，至今仍是「宜室宜家」一词的出处。',
  zhu:[['其叶蓁蓁','桃叶长得茂密繁盛。蓁蓁，草木茂盛的样子，读 zhēn——绿叶成荫，浓荫覆路'],['家人','全家人——比「室家」「家室」所指更广，祝福由小家推及整个家族'],['重章叠句','《诗经》常见章法：各章句式基本相同、只换少数字，回环往复、一唱三叹——本诗三章正用此法，祝福层层递进'],['比兴','先言他物以引起所咏之词——以桃之花、实、叶起兴，兼作比喻：花喻其貌美，实喻其多子，叶喻其旺族，物与人层层映衬']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「桃之夭夭，灼灼其华。」的下一句是？', o:['之子于归，宜其室家','之子于归，宜其家人','桃之夭夭，有蕡其实'], a:0},
 {q:'「之子于归，宜其室家。」的下一句是？', o:['桃之夭夭，其叶蓁蓁','桃之夭夭，灼灼其华','桃之夭夭，有蕡其实'], a:2},
 {q:'下列各句中加点字的读音，全都正确的一项是？', o:['「夭」读 yāo，草木茂盛；「蕡」读 fén，果实肥大；「蓁」读 zhēn，草木繁盛','「夭」读 wāo，草木弯曲；「蕡」读 fèi，花开满枝；「蓁」读 qín，草木稀疏','「夭」读 yǎo，年少早逝；「蕡」读 fén，焚烧草木；「蓁」读 zhēn，凋零飘落'], a:0},
 {q:'《桃夭》三章句式基本相同，只更换「华／实／叶」「室家／家室／家人」等少数字。对这种章法及其效果，理解最恰当的一项是？', o:['重章叠句——回环往复、一唱三叹：花艳祝其容貌之美，结实祝其多子多福，叶茂祝其家族兴旺，祝福层层递进','顶真——上句的结尾作下句的开头，词句蝉联而下，一气呵成','对比——三章互不相干，是三首咏物诗的合集，分别歌咏桃花、果实与树叶'], a:0},
 {q:'对「之子于归，宜其室家」的理解，最恰当的一项是？', o:['「于归」指这位姑娘就要出嫁；「宜其室家」祝愿她使新家庭和顺美满——以盛放的桃花起兴写人，是先民对婚嫁最朴素温暖的祝福，「宜室宜家」一词即出于此','「于归」指姑娘回娘家探亲；「宜其室家」祝愿她把家里收拾得井井有条','「于归」指姑娘远行求学；「宜其室家」祝愿她学成归来、光耀门楣'], a:0},
];
"""

SCENES_JS = """/* ================= 桃夭 · 三境场景（青绿春晓·桃林送嫁变体：灼灼其华、有蕡其实、其叶蓁蓁） =================
   美术立意：「三章一境·桃之婚嫁」——春晓桃林，一场婚嫁被整个春天祝福：
   华（花开灼灼，姑娘出嫁）→ 实（花落结实，家室兴旺）→ 叶（绿叶成荫，家人和乐），
   时间递进（花期→果期→叶茂期）+ 婚嫁推进（于归→宜室→宜家）。
   母题贯穿：①桃树三态（同源 builder 参数变奏：phase 华/实/叶）②送嫁队伍（含蓄剪影+花轿）
   ③落英 ④家宅炊烟 ⑤一湾溪水（溪带横陈于林后，通向家宅）。
   accent=#c9a0a8（桃粉）只落在 UI/花瓣/桃花盛放光点/灯笼暖光/队伍亮起；底色仍是青绿春晓全套色板。
   与已有青绿页第一眼可区分：不做三色花田春游（xingxiangzi-shurao）、不做山寺桃花
   （dalinsi-taohua）、不做村居田园（cunju 等）——本页=桃林深处一场婚嫁。
   布局纪律：主体桃树/队伍放 z −22…−60（骨架常驻远山环 z≈−260…−330 之前）；
   溪带 z −69…−127、低平雾山环 z≈−135，在远山环之前不被遮挡。 */

/* —— 桃树 makePeachTreeTY(o)：桃干（分段微弯+斜枝+树底接触阴影）+ 树冠三态 ——
   树干与树冠分两 mesh：树冠自带微自发光（华=桃粉微亮，实/叶=暗绿），「灼灼」才能在青绿底上发亮；
   华相树冠外加一层桃粉柔光（additive halo，静态 opacity，fadeK 由 setFade 统一驱动）。
   phase:'华'=桃花团簇灼灼 / '实'=青枝缀实花渐稀 / '叶'=浓荫成盖 */
function makePeachTreeTY(o){
  o=o||{};
  const phase=o.phase||'华', R=seedRnd(o.seed===undefined?25601:o.seed);
  const h=o.h===undefined?5.4:o.h, w=o.w===undefined?2.8:o.w;
  const BT=new GeoBag();
  let px=0, py=0, pz=0, pr=0.30*(0.8+0.4*R());
  const lean=(R()-0.5)*0.9, leanZ=(R()-0.5)*0.5;
  for(let k=0;k<4;k++){
    const nx=lean*(k+1)/4*(0.7+0.6*R()), ny=h*(k+1)/4, nz=leanZ*(k+1)/4*(0.7+0.6*R());
    BT.put(limbGeo([px,py,pz],[nx,ny,nz],pr,pr*0.74,5),shadeColor(0x241a14,0.8+0.5*R()));
    px=nx; py=ny; pz=nz; pr*=0.74;
    if(k>=1){
      const s=R()<0.5?-1:1;
      const bx=px+s*w*(0.35+0.5*R()), by=py+h*0.09, bz=pz+(R()-0.5)*w*0.5;
      BT.put(limbGeo([px,py,pz],[bx,by,bz],pr,pr*0.5,4),shadeColor(0x2a1e15,0.8+0.5*R()));
    }
  }
  const sh=new THREE.CircleGeometry(w*0.95,10); sh.rotateX(-Math.PI/2);
  sh.scale(1.3,1,1); sh.translate(0,0.05,0); BT.put(sh,0x04070a);
  const g=new THREE.Group();
  g.add(new THREE.Mesh(mergeGeos(BT.list),rimHook(new THREE.MeshPhongMaterial({color:0xffffff,
    vertexColors:true,shininess:8,specular:0x3a3226,emissive:0x050403}),
    {c:o.rimC===undefined?0xc9a0a8:o.rimC,i:o.rim===undefined?0.12:o.rim,p:2.2})));
  const BC=new GeoBag();
  const crownY=h*(0.92+0.10*R()), crownR=w*(1.10+0.28*R());
  if(phase==='华'){
    const pinks=[0xc4788c,0xd0889c,0xdb9aa8,0xe8aec0];
    const nP=12+((R()*4)|0);
    for(let i=0;i<nP;i++){
      const a=R()*6.283, rr=crownR*(0.10+0.55*Math.sqrt(R()));
      const pg=new THREE.SphereGeometry(crownR*(0.30+0.24*R()),7,6);
      pg.scale(1.25,0.62,1.05);
      pg.translate(px+Math.cos(a)*rr, crownY+(R()-0.42)*crownR*0.62, pz+Math.sin(a)*rr*0.85);
      const pal=i<3?[0xc4788c,0xd0889c]:pinks;
      BC.put(pg,shadeColor(pal[(R()*pal.length)|0],i<3?1.00+0.06*R():0.85+0.20*R()));
    }
  }else if(phase==='实'){
    const greens=[0x35603e,0x3c6a44,0x47784a];
    for(let i=0;i<10;i++){
      const a=R()*6.283, rr=crownR*(0.10+0.60*Math.sqrt(R()));
      const pg=new THREE.SphereGeometry(crownR*(0.30+0.22*R()),7,6);
      pg.scale(1.25,0.64,1.05);
      pg.translate(px+Math.cos(a)*rr, crownY+(R()-0.40)*crownR*0.62, pz+Math.sin(a)*rr*0.85);
      BC.put(pg,shadeColor(greens[(R()*3)|0],0.82+0.40*R()));
    }
    for(let i=0;i<8;i++){
      const a=R()*6.283, rr=crownR*(0.28+0.60*R());
      const fg=new THREE.SphereGeometry(0.18+0.09*R(),7,6);
      fg.translate(px+Math.cos(a)*rr, crownY-crownR*(0.22+0.50*R()), pz+Math.sin(a)*rr*0.85);
      BC.put(fg,shadeColor(R()<0.5?0xd4a870:0xc4b46e,0.90+0.35*R()));
    }
    const left=new THREE.SphereGeometry(crownR*0.26,7,6); left.scale(1.25,0.60,1.05);
    left.translate(px+crownR*0.40,crownY+crownR*0.30,pz); BC.put(left,0xdb9aa8);
  }else{
    const greens=[0x35603e,0x44724a,0x54855a];
    for(let i=0;i<16;i++){
      const a=R()*6.283, rr=crownR*(0.08+0.80*Math.sqrt(R()));
      const pg=new THREE.SphereGeometry(crownR*(0.26+0.24*R()),7,6);
      pg.scale(1.30,0.60,1.10);
      pg.translate(px+Math.cos(a)*rr, crownY+(R()-0.46)*crownR*0.8, pz+Math.sin(a)*rr*0.88);
      BC.put(pg,shadeColor(greens[(R()*3)|0],i<4?1.05+0.30*R():0.76+0.42*R()));
    }
  }
  g.add(new THREE.Mesh(mergeGeos(BC.list),new THREE.MeshPhongMaterial({color:0xffffff,
    vertexColors:true,shininess:6,specular:0x2a2020,
    emissive:phase==='华'?0x33141e:(phase==='实'?0x0c1a10:0x0c1c12)})));
  if(phase==='华'){
    const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd08298,
      transparent:true,opacity:0.09,depthWrite:false,blending:THREE.AdditiveBlending}));
    halo.scale.set(crownR*2.8,crownR*2.2,1); halo.position.set(px,crownY+crownR*0.15,pz);
    halo.renderOrder=4; g.add(halo);
  }
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=R()*6.283;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    g.rotation.z=0.014*Math.sin(t*0.5+ph)*kk;
    g.rotation.x=0.008*Math.sin(t*0.37+ph*1.6)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 落英 makePetalTY(o)：粉白花瓣自树冠缓落（Points 自写着色器，uFade 由 setFade 同步）——
   婚嫁喜送的暖意：壹境落英缤纷，贰境残英零落，叁境花事已了（点击后以盛放光点回放） */
const TY_PETAL_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform float uTopY; uniform float uBotY;
varying float vA;
void main(){
  float life=fract(uTime*uSpeed+aSeed);
  vec3 p=position;
  p.y=mix(uTopY,uBotY,life);
  p.x+=sin(uTime*0.8+aSeed*41.0)*(0.9+1.1*life);
  p.z+=cos(uTime*0.6+aSeed*29.0)*0.7;
  vA=smoothstep(0.0,0.10,life)*(1.0-smoothstep(0.82,1.0,life));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const TY_PETAL_FRAG=`
uniform vec3 uC; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=length(q);
  float a=smoothstep(0.5,0.12,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makePetalTY(o){
  o=o||{};
  const n=o.n===undefined?90:o.n, R=seedRnd(o.seed===undefined?25621:o.seed);
  const box=o.box===undefined?[64,8,36]:o.box, c0=o.pos===undefined?[0,8.5,-34]:o.pos;
  const topY=c0[1]+box[1]*0.5, botY=0.18;
  const P=new Float32Array(n*3), S=new Float32Array(n), Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=c0[0]+(R()-0.5)*box[0];
    P[i*3+1]=c0[1];
    P[i*3+2]=c0[2]+(R()-0.5)*box[2];
    S[i]=R(); Z[i]=1.8+2.6*R();
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?0.045:o.speed},
      uTopY:{value:topY},uBotY:{value:botY},uC:{value:C(0xe8b4c2)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.72:o.maxA}},
    vertexShader:TY_PETAL_VERT,fragmentShader:TY_PETAL_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=3;
  const grp=new THREE.Group(); grp.add(points);
  grp.update=function(t){ m.uniforms.uTime.value=t; };
  grp.userData.update=grp.update;
  return grp;
}

/* —— 盛放光点 makeBloomPointsTY(o)：点击后桃花次第盛放（Points 自写着色器，aT 定簇序、uReveal 点亮）
   点击前 visible=false 硬关；spots=[x,y,z,半径,簇序t] —— 簇序即「次第」 */
const TY_BLOOM_VERT=`
attribute float aT; attribute float aSize;
uniform float uReveal; uniform float uTime;
varying float vA;
void main(){
  float lead=uReveal*1.18;
  float lit=1.0-smoothstep(0.0,0.14,lead-aT);
  float pulse=0.86+0.14*sin(uTime*2.1+aT*43.0);
  vA=lit*pulse;
  vec4 mv=modelViewMatrix*vec4(position,1.0);
  gl_PointSize=aSize*(0.35+1.65*lit)*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const TY_BLOOM_FRAG=`
uniform vec3 uC; uniform float uFade;
varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float a=smoothstep(0.5,0.10,length(q))*vA*uFade;
  if(a<0.004) discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeBloomPointsTY(o){
  o=o||{};
  const spots=o.spots===undefined?[[0,4,0,3,0]]:o.spots;
  const per=o.per===undefined?30:o.per, R=seedRnd(o.seed===undefined?25611:o.seed);
  const n=spots.length*per;
  const P=new Float32Array(n*3), T=new Float32Array(n), Z=new Float32Array(n);
  let i=0;
  for(let s=0;s<spots.length;s++){
    const sp=spots[s];
    for(let j=0;j<per;j++){
      const a=R()*6.283, rr=sp[3]*(0.10+0.85*Math.sqrt(R()));
      P[i*3]=sp[0]+Math.cos(a)*rr;
      P[i*3+1]=sp[1]+(R()-0.35)*sp[3]*0.9;
      P[i*3+2]=sp[2]+Math.sin(a)*rr*0.8;
      T[i]=sp[4]; Z[i]=2.6+3.2*R();
      i++;
    }
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aT',new THREE.BufferAttribute(T,1));
  geo.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uReveal:{value:0},uTime:{value:0},uC:{value:C(0xe8b4c0)},uFade:{value:0}},
    vertexShader:TY_BLOOM_VERT,fragmentShader:TY_BLOOM_FRAG});
  const points=new THREE.Points(geo,m); points.frustumCulled=false; points.renderOrder=4;
  const grp=new THREE.Group(); grp.add(points); grp.visible=false;
  grp.update=function(t,k,rev){ const kk=k===undefined?1:k, r=rev===undefined?0:rev;
    m.uniforms.uReveal.value=Math.min(1,r*1.18);
    m.uniforms.uTime.value=t;
    grp.visible=kk*r>0.004;
  };
  grp.userData.update=grp.update;
  return grp;
}

/* —— 花轿 makeSedanTY(o)：含蓄剪影小轿（轿顶+轿身+轿帘+抬杆+接触阴影），合批 1 mesh ——
   「之子于归」的视觉落点：不画人面，只留一顶轿在花影之间 */
function makeSedanTY(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.BoxGeometry(1.1,1.3,0.9); body.translate(0,1.15,0); B.put(body,0x4a3238);
  const roof=new THREE.ConeGeometry(1.02,0.52,4); roof.rotateY(Math.PI/4);
  roof.scale(1.12,1,1); roof.translate(0,2.06,0); B.put(roof,0x33262a);
  const curtain=new THREE.BoxGeometry(0.72,0.56,0.07); curtain.translate(0,1.16,0.47); B.put(curtain,0x6a4248);
  [1,-1].forEach(function(s){
    const pole=new THREE.CylinderGeometry(0.05,0.05,2.7,5); pole.rotateZ(Math.PI/2);
    pole.translate(0,1.06,s*0.56); B.put(pole,0x2a201a);
  });
  const shadow=new THREE.CircleGeometry(0.95,10); shadow.rotateX(-Math.PI/2);
  shadow.scale(1.2,1,1); shadow.translate(0,0.04,0); B.put(shadow,0x050807);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x403030,emissive:0x050404}),{c:o.rimC===undefined?0xc9a0a8:o.rimC,i:o.rim===undefined?0.14:o.rim,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  const ph=(o.seed===undefined?25612:o.seed)%6.283;
  let by=null;
  g.update=function(t,k){ const kk=k===undefined?1:k;
    if(by===null)by=g.position.y;
    g.position.y=by+0.03*Math.sin(t*1.1+ph)*kk;
    g.rotation.z=0.02*Math.sin(t*0.9+ph)*kk; };
  g.userData.update=g.update;
  return g;
}

/* —— 家宅 makeHomeTY(o)：茅檐家宅（院墙+屋身+草顶+门洞），合批 1 mesh + 门前暖光点 + 炊烟 ——
   「宜其室家／宜其家人」的视觉落点：宅在林后，炊烟升起 */
function makeHomeTY(o){
  o=o||{};
  const g=new THREE.Group();
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(4.4,1.5,3.0); wall.translate(0,0.75,0); B.put(wall,0x1b211c);
  const house=new THREE.BoxGeometry(3.2,1.7,2.2); house.translate(0,0.85,-0.2); B.put(house,0x201a14);
  const roof=new THREE.ConeGeometry(2.9,1.35,4); roof.rotateY(Math.PI/4);
  roof.scale(1.18,1,1); roof.translate(0,2.37,-0.2); B.put(roof,0x2c2618);
  const door=new THREE.BoxGeometry(0.72,1.1,0.09); door.translate(0,0.55,0.96); B.put(door,0x0c0e0c);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2c2c22,emissive:0x040504}),{c:o.rimC===undefined?0xc9a0a8:o.rimC,i:o.rim===undefined?0.10:o.rim,p:2.0})));
  const warm=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xd8b088,
    transparent:true,opacity:0.10,depthWrite:false}));
  warm.scale.set(3.2,2.4,1); warm.position.set(0,1.0,0.9); warm.renderOrder=4; g.add(warm);
  const smoke=makeGlow({n:10,box:[1.2,7,1.2],pos:[1.2,3.1,-0.8],color:0x8a9488,size:4.5,speed:0.10,rise:1,add:false,maxA:0.10});
  g.add(smoke.points);
  g.update=function(t,k){ smoke.update(t); };
  g.userData.update=g.update;
  return g;
}

/* —— 春晓桃林基底 makeGroveTY(o)：一湾溪水（溪带）+ 坡地 + 低平雾山环 ——
   溪带放 z≈−98（骨架常驻远山环 z≈−260…−330 之前），山环 z≈−135，均不被遮挡 */
function makeGroveTY(o){
  o=o||{};
  const g=new THREE.Group();
  const water=makeWater({size:420,seg:84,amp:o.amp===undefined?0.10:o.amp,freq:0.15,speed:0.26,
    flow:[0.06,0.20],spec:0.90,deep:0x0a1410,shallow:0x1c3a24,skyc:0x2e4a34,moonDir:[-30,42,-110]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xe8d8a8);
  water.mesh.scale.z=0.18;
  water.mesh.position.set(0,0.10,-98); g.add(water.mesh);
  const bed=makeGround({r:260,c1:0x16241a,c2:0x2a4028,y:0});
  bed.mesh.position.set(0,0,-70); g.add(bed.mesh);
  const ridge=makeRange({r:250,h:12,layers:2,peaks:4,seed:o.seed===undefined?25631:o.seed,
    color:0x0c1510,atmo:0x2e4436,fogK:0.60,glowK:0.05,glow:0xc9d8b0,y:-12,order:-6});
  ridge.g.position.set(0,0,-135); g.add(ridge.g);
  return {g:g,water:water,ridge:ridge};
}

function bCover(){ // 卷首 · 春晓桃林 —— 桃林沿坡，晨光熹微，一湾溪水横陈林后，家宅炊烟在望
  const g=new THREE.Group();
  const grove=makeGroveTY({seed:25631}); g.add(grove.g);
  const t1=makePeachTreeTY({seed:25641,phase:'华',h:5.8,w:3.2}); t1.position.set(-14,0,-34); g.add(t1);
  const t2=makePeachTreeTY({seed:25642,phase:'华',h:4.8,w:2.8}); t2.position.set(-5,0,-50); g.add(t2);
  const t3=makePeachTreeTY({seed:25643,phase:'华',h:6.6,w:3.6}); t3.position.set(12,0,-44); g.add(t3);
  const t4=makePeachTreeTY({seed:25644,phase:'华',h:5.2,w:3.0}); t4.position.set(24,0,-60); g.add(t4);
  const t5=makePeachTreeTY({seed:25645,phase:'实',h:4.6,w:2.6}); t5.position.set(-26,0,-58); g.add(t5);
  const carpet=makeGlow({n:22,box:[9,0.4,7],pos:[-14,0.4,-34],color:0xd8a8b4,size:2.2,speed:0.02,rise:0,add:false,maxA:0.45});
  g.add(carpet.points);
  const home=makeHomeTY({seed:25651}); home.position.set(30,0,-62); home.rotation.y=-0.5; g.add(home);
  const crowd=makeCrowd({n:5,rect:[-10,-66,16,7],seed:25661,color:0x141a16,rimC:0xc9a0a8,rim:0.11});
  g.add(crowd.mesh);
  const petals=makePetalTY({n:80,box:[60,8,38],pos:[0,8,-38],speed:0.04,seed:25621}); g.add(petals);
  const mist=makeMist({n:6,spread:[230,14,100],pos:[0,5,-46],scale:66,color:0x2c4034,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[150,14,60],pos:[0,8,-40],color:0xc8d8b0,size:4.0,speed:0.03,rise:0,add:true,maxA:0.09});
  g.add(motes.points);
  const fgL=makeForeground({kind:'树枝',w:14,n:8,d:3,color:0x0a0d0a,seed:25671,sway:0.8,tip:0x4a6a48,scale:1.0});
  fgL.g.position.set(-14,-1.2,30); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:4,color:0x080b08,seed:25672,rim:0.10,rimC:0xc9a0a8});
  fgR.g.position.set(13,-1.4,32); g.add(fgR.g);
  addLights(g,{c:0xf0e2ce,i:0.48,p:[-34,66,26]},{c:0x24331f,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grove.water.update(t); grove.ridge.update(t,0);
    t1.update(t,k); t2.update(t,k); t3.update(t,k); t4.update(t,k); t5.update(t,k);
    carpet.update(t);
    home.update(t,k); crowd.update(t);
    petals.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bZhuozhuo(){ // 壹（标志性瞬间）· 灼灼其华 —— 桃之夭夭，灼灼其华；之子于归，宜其室家：
                      // 盛放桃林合围出一条花路，送嫁队伍剪影（花轿居中）行于花影之间，落英缤纷满地
  const g=new THREE.Group();
  const grove=makeGroveTY({seed:25632,amp:0.09}); g.add(grove.g);
  const t1=makePeachTreeTY({seed:25686,phase:'华',h:7.4,w:4.2}); t1.position.set(-11,0,-20); g.add(t1);
  const t2=makePeachTreeTY({seed:25647,phase:'华',h:6.6,w:3.8}); t2.position.set(10,0,-24); g.add(t2);
  const t3=makePeachTreeTY({seed:25648,phase:'华',h:6.0,w:3.4}); t3.position.set(-18,0,-38); g.add(t3);
  const t4=makePeachTreeTY({seed:25649,phase:'华',h:6.8,w:3.6}); t4.position.set(16,0,-42); g.add(t4);
  const t5=makePeachTreeTY({seed:25650,phase:'华',h:5.2,w:3.0}); t5.position.set(-3,0,-56); g.add(t5);
  /* 落英满地：树下花瓣毯 */
  const carpet1=makeGlow({n:20,box:[9,0.4,7],pos:[-11,0.4,-20],color:0xd8a8b4,size:2.2,speed:0.02,rise:0,add:false,maxA:0.50});
  g.add(carpet1.points);
  const carpet2=makeGlow({n:18,box:[8,0.4,6],pos:[10,0.4,-24],color:0xd8a8b4,size:2.2,speed:0.02,rise:0,add:false,maxA:0.45});
  g.add(carpet2.points);
  /* 送嫁队伍（中景剪影，含蓄无面目）：花轿居中，轿夫与送行人前后相随 */
  const sedan=makeSedanTY({seed:25612,scale:1.15}); sedan.position.set(-6,0.02,-28); sedan.rotation.y=0.25; g.add(sedan);
  const bearers=makeCrowd({n:7,rect:[-13,-33,13,6],seed:25662,color:0x151a16,rimC:0xc9a0a8,rim:0.14,
    sMin:0.54,sMax:0.64});
  g.add(bearers.mesh);
  const kin=makeFigure({pose:'独立',robe:0x2a2620,belt:0x6a4a44,skin:0xc8a488,collar:0x8a7460,
    hair:0x141210,hat:'发髻',rim:0.30,rimC:0xd8b0a8,noProp:true,scale:0.52});
  kin.position.set(-2.5,0,-25.5); kin.rotation.y=2.6; g.add(kin);
  /* 落英缤纷：花随人走，婚嫁喜送 */
  const petals=makePetalTY({n:130,box:[52,7.5,30],pos:[0,7,-28],speed:0.055,seed:25622}); g.add(petals);
  const mist=makeMist({n:6,spread:[230,14,100],pos:[0,5,-48],scale:68,color:0x2c4034,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:28,box:[150,14,60],pos:[0,8,-40],color:0xccd8b4,size:4.0,speed:0.03,rise:0,add:true,maxA:0.09});
  g.add(motes.points);
  const fgL=makeForeground({kind:'树枝',w:12,n:9,d:3,color:0x0a0d0a,seed:25673,sway:0.9,tip:0x6a5a52,scale:1.0});
  fgL.g.position.set(-13,-1.4,14); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:2.4,w:9,d:4,color:0x080b08,seed:25674,rim:0.10,rimC:0xc9a0a8});
  fgR.g.position.set(12,-1.4,13); g.add(fgR.g);
  addLights(g,{c:0xf2e4d4,i:0.55,p:[-30,64,24]},{c:0x243420,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grove.water.update(t); grove.ridge.update(t,0);
    t1.update(t,k); t2.update(t,k); t3.update(t,k); t4.update(t,k); t5.update(t,k);
    carpet1.update(t); carpet2.update(t);
    sedan.update(t,k); bearers.update(t); kin.update(t,k);
    petals.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bYoufen(){ // 贰 · 有蕡其实 —— 桃之夭夭，有蕡其实；之子于归，宜其家室：
                    // 花渐落而实渐肥，青枝缀实；家宅在望，炊烟升起，残英零落
  const g=new THREE.Group();
  const grove=makeGroveTY({seed:25633,amp:0.08}); g.add(grove.g);
  const t1=makePeachTreeTY({seed:25652,phase:'实',h:6.6,w:3.6}); t1.position.set(-9,0,-22); g.add(t1);
  const t2=makePeachTreeTY({seed:25653,phase:'实',h:5.8,w:3.2}); t2.position.set(7,0,-27); g.add(t2);
  const t3=makePeachTreeTY({seed:25654,phase:'实',h:5.2,w:2.8}); t3.position.set(-17,0,-38); g.add(t3);
  const t4=makePeachTreeTY({seed:25655,phase:'叶',h:6.0,w:3.4}); t4.position.set(18,0,-40); g.add(t4);
  const home=makeHomeTY({seed:25656}); home.position.set(13,0,-48); home.rotation.y=-0.6; g.add(home);
  const crowd=makeCrowd({n:4,rect:[7,-44,12,6],seed:25663,color:0x141a16,rimC:0xc9a0a8,rim:0.11,
    sMin:0.52,sMax:0.62});
  g.add(crowd.mesh);
  /* 残英零落：花期已过，花瓣稀疏 */
  const petals=makePetalTY({n:34,box:[52,8,30],pos:[0,8,-30],speed:0.035,seed:25623,maxA:0.55}); g.add(petals);
  const mist=makeMist({n:6,spread:[230,14,100],pos:[0,5,-48],scale:68,color:0x2c4034,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[150,14,60],pos:[0,8,-40],color:0xc8d8b0,size:4.0,speed:0.03,rise:0,add:true,maxA:0.08});
  g.add(motes.points);
  const fgL=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:4,color:0x080b08,seed:25675,rim:0.10,rimC:0xc9a0a8});
  fgL.g.position.set(-12,-1.3,14); g.add(fgL.g);
  const fgR=makeForeground({kind:'树枝',w:10,n:7,d:3,color:0x0a0d0a,seed:25676,sway:0.8,tip:0x4a6a48,scale:0.95});
  fgR.g.position.set(11,-1.4,15); g.add(fgR.g);
  addLights(g,{c:0xf2e4d6,i:0.58,p:[34,70,22]},{c:0x22301e,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    grove.water.update(t); grove.ridge.update(t,0);
    t1.update(t,k); t2.update(t,k); t3.update(t,k); t4.update(t,k);
    home.update(t,k); crowd.update(t);
    petals.update(t); mist.update(t,k); motes.update(t);
    fgL.update(t,k); fgR.update(t,k);
  }};
}
function bZhenzhen(){ // 叁（末境·可点击）· 其叶蓁蓁 —— 桃之夭夭，其叶蓁蓁；之子于归，宜其家人：
                      // 绿叶成荫，浓荫覆路，队伍抵达家宅门前；点击桃花次第盛放，送嫁队伍亮起
  const ctl={t:0,clicked:false,on:false,reveal:0};
  const ss=function(x){ x=Math.max(0,Math.min(1,x)); return x*x*(3-2*x); };
  const g=new THREE.Group();
  const grove=makeGroveTY({seed:25634,amp:0.09}); g.add(grove.g);
  const t1=makePeachTreeTY({seed:25657,phase:'叶',h:6.8,w:3.8}); t1.position.set(-10,0,-22); g.add(t1);
  const t2=makePeachTreeTY({seed:25658,phase:'叶',h:6.0,w:3.4}); t2.position.set(9,0,-28); g.add(t2);
  const t3=makePeachTreeTY({seed:25659,phase:'叶',h:5.2,w:3.0}); t3.position.set(-18,0,-40); g.add(t3);
  const t4=makePeachTreeTY({seed:25660,phase:'叶',h:6.2,w:3.4}); t4.position.set(16,0,-48); g.add(t4);
  const t5=makePeachTreeTY({seed:25666,phase:'叶',h:5.0,w:2.8}); t5.position.set(-2,0,-62); g.add(t5);
  const home=makeHomeTY({seed:25667}); home.position.set(13,0,-58); home.rotation.y=-0.7; g.add(home);
  /* 送嫁队伍抵达门前（剪影常在）：花轿+轿夫+送行人 */
  const sedan=makeSedanTY({seed:25613}); sedan.position.set(-5,0.02,-30); sedan.rotation.y=0.35; g.add(sedan);
  const bearers=makeCrowd({n:8,rect:[-12,-34,16,7],seed:25664,color:0x141915,rimC:0xc9a0a8,rim:0.13,
    sMin:0.50,sMax:0.60});
  g.add(bearers.mesh);
  const kin=makeFigure({pose:'独立',robe:0x2a2620,belt:0x6a4a44,skin:0xc8a488,collar:0x8a7460,
    hair:0x141210,hat:'发髻',rim:0.30,rimC:0xd8b0a8,noProp:true,scale:0.52});
  kin.position.set(-8.5,0,-27); kin.rotation.y=-2.4; g.add(kin);
  /* 灯笼光点（点击前组 visible=false 硬关；初值=峰值，逐帧 k×峰值×包络，fadeK 合规）——队伍亮起 */
  const lampG=new THREE.Group(); lampG.visible=false; g.add(lampG);
  const lampPts=[[-8.5,2.3,-27.5],[-6.5,2.4,-31],[-4.5,2.3,-33.5],[-2.5,2.4,-30.5],[12.2,1.6,-56.5]];
  const lamps=lampPts.map(function(p,i){
    const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe8b48a,
      transparent:true,opacity:0.9,depthWrite:false}));
    s.scale.set(1.7,2.2,1); s.position.set(p[0],p[1],p[2]); s.renderOrder=4;
    s.userData.ph=i*1.7; lampG.add(s); return s;
  });
  const warm=new THREE.PointLight(0xe8b48a,1.1,44,1.6); warm.position.set(-2,3.6,-32); g.add(warm);
  /* 盛放光点（点击前 visible=false 硬关）：沿林间簇序排布——点击桃花次第盛放 */
  const bloom=makeBloomPointsTY({seed:25611,per:30,spots:[
    [-10,6.4,-22,3.8,0.02],[9,5.7,-28,3.5,0.20],[-18,4.9,-40,3.0,0.38],
    [16,5.8,-48,3.5,0.56],[-2,4.7,-62,2.9,0.76],[13,2.1,-58,1.6,0.94]]});
  g.add(bloom);
  const mist=makeMist({n:6,spread:[230,14,100],pos:[0,5,-48],scale:68,color:0x2c4034,op:0.09});
  g.add(mist.g);
  const motes=makeGlow({n:26,box:[150,14,60],pos:[0,8,-40],color:0xc8d8b0,size:4.0,speed:0.03,rise:0,add:true,maxA:0.08});
  g.add(motes.points);
  const fgL=makeForeground({kind:'树枝',w:12,n:8,d:3,color:0x0a0d0a,seed:25677,sway:0.9,tip:0x4a6a48,scale:0.85});
  fgL.g.position.set(-11,-1.3,14); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:2.2,w:9,d:4,color:0x080b08,seed:25678,rim:0.10,rimC:0xc9a0a8});
  fgR.g.position.set(11,-1.4,15); g.add(fgR.g);
  addLights(g,{c:0xe8dcc0,i:0.50,p:[-28,62,24]},{c:0x1e2c1c,i:0.66});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.reveal=Math.min(1,ctl.reveal+dt/9.0);
      const r=ctl.reveal, env=ss(r*1.6);
      /* 队伍亮起：灯笼逐盏点亮（初值=峰值，逐帧 k×峰值×包络） */
      lamps.forEach(function(s){
        s.material.opacity=k*0.9*env*(0.86+0.14*Math.sin(t*6.3+s.userData.ph));
      });
      warm.intensity=k*1.1*env;
      bloom.update(t,k,r);
      grove.water.update(t); grove.ridge.update(t,0);
      t1.update(t,k); t2.update(t,k); t3.update(t,k); t4.update(t,k); t5.update(t,k);
      sedan.update(t,k); bearers.update(t); kin.update(t,k);
      mist.update(t,k); motes.update(t);
      fgL.update(t,k); fgR.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        setAmbience(0.12);
      }
      ctl.on=true; ctl.reveal=0;                 /* 可反复点：再送一程 */
      pluck(2,0.00,0.11); pluck(4,0.45,0.10); pluck(5,0.90,0.10); pluck(7,1.45,0.11); pluck(9,2.10,0.09);
      const fl=$('#flash'); fl.textContent='之子于归 宜其室家';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.2,
  moon:new THREE.Vector3(60,120,-210),ms:0.8,mph:0.3,mhaze:0.08,dirC:C(0xd8c88a),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.05,build:bCover,
  cam:{f:[0,8.5,50],t:[0,9.4,42],lf:[-2,6.5,-30],lt:[-3,7,-38]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0050,star:0.10,
    ms:0.42,mph:0.42,mhaze:0.10,moon:new THREE.Vector3(-64,66,-220),
    dirC:C(0xe4d092),dirI:0.46,ambC:C(0x24331f),ambI:0.62}) },
{ name:'灼灼其华',dwell:22,river:0.06,build:bZhuozhuo,
  cam:{f:[1.2,3.8,16],t:[-1.4,3.8,11],lf:[-6,3.2,-26],lt:[-9,3.4,-36]},
  sky:()=>SK({top:C(0x15261c),hor:C(0x3e5438),fd:0.0072,star:0.10,ms:0.30,mph:0.44,mhaze:0.12,
    dirC:C(0xf2e4d4),dirI:0.55,dirP:new THREE.Vector3(-30,64,24),ambC:C(0x243420),ambI:0.66}) },
{ name:'有蕡其实',dwell:20,river:0.055,build:bYoufen,
  cam:{f:[-2,4.6,17],t:[0.5,4.4,12],lf:[11,2.8,-26],lt:[14,2.6,-40]},
  sky:()=>SK({top:C(0x122417),hor:C(0x345030),fd:0.0062,star:0.06,ms:0.22,mph:0.44,mhaze:0.10,
    dirC:C(0xf2e4d6),dirI:0.58,dirP:new THREE.Vector3(34,70,22),ambC:C(0x22301e),ambI:0.68}) },
{ name:'其叶蓁蓁',dwell:24,river:0.065,build:bZhenzhen,
  cam:{f:[1,4.2,18],t:[-1.5,4,12.5],lf:[-5,3.2,-26],lt:[-8,3.4,-38]},
  sky:()=>SK({top:C(0x112318),hor:C(0x2e4830),fd:0.0068,star:0.07,ms:0.24,mph:0.44,mhaze:0.10,
    dirC:C(0xdcc98c),dirI:0.46,dirP:new THREE.Vector3(-28,62,24),ambC:C(0x1e2c1c),ambI:0.66}) },
];
"""

if __name__ == '__main__':
    print('taoyao.py —— 被 build.py 消费：python build.py taoyao')
