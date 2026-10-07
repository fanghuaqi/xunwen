# -*- coding: utf-8 -*-
"""huanxisha-xifeng.py —— 《浣溪沙·谁念西风独自凉》（清·纳兰性德，no.203，水墨夜思）生成配置
两境（N=queue stages 数，queue 唯一口径）：
  壹「西风残阳」——谁念西风独自凉 / 萧萧黄叶闭疏窗 / 沉思往事立残阳：
      冷灰残阳低垂山脊，疏窗紧闭，词人独立庭院望残阳，黄叶辞枝、西风横流——无人念我独自凉；
  贰「赌书泼茶」（末境·可点击）——被酒莫惊春睡重 / 赌书消得泼茶香 / 当时只道是寻常：
      同一座庭院，镜头推向疏窗——窗内书案茶盏、夫妻对影伏而未现（寻常到被忽略）；
      点击「泼茶香」：茶香书影闪回凝现（赌书泼茶的闺房之乐，李清照赵明诚典）+ 残阳满窗，
      暖忆低饱和微光（同 mulanhua 先例）——回忆越暖，现实越冷，「当时只道是寻常」的钝痛。
标志性瞬间「一窗两界」：窗内是暖忆书影，窗外是冷灰残阳——寻常与失去，只隔一层窗纸。
水墨夜思色板：bg #0d1117、雾 #131a26 系、accent=#b0bcc9（残阳冷灰/人物/窗棂边缘光），禁金；
现实残阳冷灰（0xd9dee6 盘 + 银灰辉光），唯一暖点是闪回的茶色暖忆（0xb08e80，低饱和）。"""

META = dict(
    N=2, slug='huanxisha-xifeng', title='浣溪沙·谁念西风独自凉', dyn='清 · 纳兰性德', brand_author='纳 兰 性 德',
    gold_rgb='176,188,201',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#b0bcc9; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(176,188,201,.26);
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
        ('rgba(232,220,192', 'rgba(186,200,222', 2),
    ],
    tip='轻点画面 / 按空格 —— 茶香书影闪回，残阳满窗',
    hint='← → 键或空格逐境游览 · 末境可点击画面：茶香书影闪回，残阳满窗，忆当时寻常',
    cover_read='浣溪沙·谁念西风独自凉。清，纳兰性德。谁念西风独自凉，萧萧黄叶闭疏窗，沉思往事立残阳。被酒莫惊春睡重，赌书消得泼茶香，当时只道是寻常。',
    cover_p1='两重意境，随词句次第展开：西风乍起，黄叶闭窗，谁还惦念西风里独自凄凉的我，沉思往事，独立残阳；一转春睡沉沉、赌书泼茶满室香——当时只道是寻常，如今天人永隔，才知寻常二字最断肠。',
    cover_p2='边读词，边走进纳兰性德的西风庭院：现实是冷灰残阳，回忆是一窗暖光——钝痛，藏在最寻常的旧事里。',
    end_h2='残阳 · 寻常', cn_word='两',
    words_js="['再游一次，西风庭院','初识容若，尚需共读','渐入词境，黄叶知秋','词心渐明，茶香可辨','已解赌书泼茶之乐','寻常最忆，残阳独凉']",
    sky_atmo='0x232c3d',
)

POEM_JS = """const POEM = [
{ name:'西风残阳', jing:'西风乍起，无人念我独自凉 —— 黄叶萧萧闭了疏窗，独立残阳，沉思往事。（西风 · 黄叶 · 残阳）',
  segs:[
   {c:'谁念西风独自凉，', p:py('shuí niàn xī fēng dú zì liáng')},
   {c:'萧萧黄叶闭疏窗，', p:py('xiāo xiāo huáng yè bì shū chuāng')},
   {c:'沉思往事立残阳。', p:py('chén sī wǎng shì lì cán yáng')}],
  read:'谁念西风独自凉，萧萧黄叶闭疏窗，沉思往事立残阳。',
  yisi:'秋风乍起，天凉了——可谁还会惦念那个独立风中的人，惦念他独自承受的这份凉？只有萧萧黄叶纷纷飘坠，密密地遮闭了镂花的疏窗。我在残阳的余晖里久久伫立，任往事一寸寸漫上来。——上片三句一景一情：西风、黄叶、残阳，触目皆凉；「谁念」一问最重，问的是天底下再没有第二个知冷知热的人。',
  zhu:[['浣溪沙','词牌名。此词是纳兰性德悼念亡妻卢氏的名作：卢氏十八岁嫁纳兰，伉俪情笃，康熙十六年（1677）五月难产而逝，年仅二十一。此后纳兰词风愈见凄婉，悼亡之作甚多，此为其代表'],
       ['谁念','谁还惦念、谁还怜惜。西风：秋风。「独自凉」：凉的不只是天气，更是丧妻之后无人嘘寒问暖的心——劈头一问，先声夺人'],
       ['萧萧','风吹黄叶的萧瑟之声。萧萧是秋声，也是悲声；黄叶辞枝，正如斯人一去不返'],
       ['疏窗','窗棂镂刻花纹、格子疏朗的窗。「闭疏窗」：黄叶密密飘坠，遮闭了窗子；亦可解作西风紧时人闭窗独坐，凄凉无人共语'],
       ['残阳','将落未落的太阳。「沉思往事立残阳」：在夕阳余晖里久久伫立，影子被拉得又长又凉——由景入情的枢纽，逗出下片满纸回忆']] },
{ name:'赌书泼茶', jing:'春睡沉沉、赌书泼茶，昔日闺房之乐历历在目 —— 当时只道是寻常，如今追忆，钝痛入骨。（赌书 · 泼茶 · 寻常）',
  segs:[
   {c:'被酒莫惊春睡重，', p:py('bèi jiǔ mò jīng chūn shuì zhòng')},
   {c:'赌书消得泼茶香，', p:py('dǔ shū xiāo dé pō chá xiāng')},
   {c:'当时只道是寻常。', p:py('dāng shí zhǐ dào shì xún cháng')}],
  read:'被酒莫惊春睡重，赌书消得泼茶香，当时只道是寻常。',
  yisi:'带着微醺沉沉睡去，春日迟迟，谁也不要惊扰这酣酣的睡意吧；想当年你我以茶赌书，猜中的人先笑出声来，茶水泼翻，满怀都是香——那样的日子，当时只觉得再寻常不过。如今才明白：人间最贵的，恰恰就是那份「寻常」。——下片全是回忆：越暖，越见今日之冷；结句不着一个「悲」字，而痛到极处，是悼亡词里最著名的钝痛。',
  zhu:[['被酒','中酒、带着醉意。被酒莫惊春睡重：带几分酒意沉沉入睡，春睡正浓，谁也不要惊动——「重」读 zhòng，沉重之重，非重复之重'],
       ['赌书','李清照《金石录后序》记她与丈夫赵明诚的闺中雅事：饭后烹茶，指着满屋书史，说某事在某书、某卷、第几页、第几行，以猜中与否定胜负，猜中者先饮——胜者每每举杯大笑，茶倾满怀，反而饮之不得。纳兰借李赵夫妇的志趣相投，写自家与卢氏的闺房之乐'],
       ['泼茶香','赌书得胜，大笑之间茶盏倾翻，满衣满怀皆是茶香——琴瑟在御，莫不静好，是全词唯一的暖色'],
       ['当时只道是寻常','全词之眼：当年身在其中，只道是寻常光景；如今天人永隔，才知道那份寻常是一去不返的幸福。不用「悲」「痛」「断肠」，只在回望里轻轻一叹，哀而弥深'],
       ['卢氏','纳兰性德结发妻，两广总督卢兴祖之女，康熙十三年（1674）成婚，情好甚笃；三年后病逝。纳兰自言「悼亡之吟不少，知己之恨尤深」，此词即「知己之恨」的注脚']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「谁念西风独自凉」的下一句是？', o:['萧萧黄叶闭疏窗','沉思往事立残阳','被酒莫惊春睡重'], a:0},
 {q:'「赌书消得泼茶香」的下一句是？', o:['被酒莫惊春睡重','当时只道是寻常','萧萧黄叶闭疏窗'], a:1},
 {q:'「被酒莫惊春睡重」中「重」的读音、「被酒」的意思是？', o:['「重」读 zhòng，春睡正沉；「被酒」是中酒、带着醉意','「重」读 chóng，春睡反复；「被酒」是盖着酒坛','「重」读 zhǒng，睡得肿痛；「被酒」是被人劝酒'], a:0},
 {q:'「赌书消得泼茶香」用的是哪对夫妇的典故？', o:['李清照与赵明诚：饭后烹茶赌书，猜中者先饮，大笑间茶倾满怀（见《金石录后序》）','唐明皇与杨贵妃：七夕长生殿夜半私语盟誓','陶渊明与邻曲：重阳对菊闲饮，酣醉而归'], a:0},
 {q:'结句「当时只道是寻常」主要表达的是？', o:['怀念仕途得意、裘马轻狂的年少时光','悼念亡妻卢氏：昔日闺房之乐本是寻常，如今天人永隔，才知寻常最珍贵','感叹世事无常、功名如浮云'], a:1},
];
"""

SCENES_JS = """/* ================= 浣溪沙·谁念西风独自凉 · 两境场景（水墨夜思：冷灰残阳、黄叶疏窗、赌书泼茶） =================
   美术立意：水墨夜思赛道——底色 #0d1117、雾 #131a26 系、accent=#b0bcc9（残阳冷灰/边缘光），禁金。
   情绪轴：现实之冷（冷灰残阳 + 黄叶 + 疏窗紧闭）↔ 回忆之暖（窗内茶色暖忆微光，全页唯一暖点，低饱和 0xb08e80，同 mulanhua 先例）。
   标志性瞬间「一窗两界」：末境点击「泼茶香」——茶香书影闪回凝现 + 残阳满窗。 */

/* —— 残阳：冷灰日轮（limbTex 临边昏暗）+ 银灰双层辉光，低垂山脊之上（fog:false）—— */
function makeCanyang(o){
  o=o||{};
  const r=o.r===undefined?7.5:o.r, glowMax=o.glowMax===undefined?0.30:o.glowMax;
  const g=new THREE.Group();
  const disc=new THREE.Mesh(new THREE.CircleGeometry(r,40),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xd9dee6,fog:false,transparent:true,opacity:0.96,depthWrite:false}));
  g.add(disc);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb8b6ab,
    transparent:true,opacity:glowMax,depthWrite:false,blending:THREE.AdditiveBlending,fog:false}));
  glow.scale.set(r*4.6,r*4.2,1); g.add(glow);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8adb8,
    transparent:true,opacity:0.12,depthWrite:false,blending:THREE.AdditiveBlending,fog:false}));
  halo.scale.set(r*10,r*7,1); g.add(halo);
  g.children.forEach(function(m){ m.renderOrder=2; });
  return {g,glowMat:glow.material,haloMat:halo.material};
}

/* —— 落叶粒子（灰黄低饱和）：自写着色器，顶点回绕下落 + 西风横漂 —— */
const HXD_DROP_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uWind;
varying float vA;
void main(){
  vec3 p=position;
  float h=uBox.y;
  float fall=mod(uTime*uSpeed*(0.55+0.9*aSeed)+aSeed*h*7.0,h);
  p.y+=h*0.5-fall;
  p.x+=mod(uWind*uTime*(0.5+aSeed)+sin(uTime*0.8+aSeed*41.0)*1.6+uBox.x*0.5,uBox.x)-uBox.x*0.5;
  p.z+=cos(uTime*0.6+aSeed*29.0)*1.2;
  vA=smoothstep(0.0,3.0,fall)*smoothstep(h,h-3.0,fall);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.7+0.3*fract(aSeed*13.7))*(140.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeLuoye(o){
  const n=o.n===undefined?46:o.n, box=o.box===undefined?[80,26,44]:o.box, pos=o.pos===undefined?[0,13,-14]:o.pos;
  const color=o.color===undefined?0x8a8168:o.color, size=o.size===undefined?4.6:o.size;
  const speed=o.speed===undefined?1.7:o.speed, wind=o.wind===undefined?2.6:o.wind, maxA=o.maxA===undefined?0.46:o.maxA;
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=size*(0.6+Math.random()*0.9);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:speed},uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uWind:{value:wind},uColor:{value:C(color)},uFade:{value:0},uMaxA:{value:maxA}},
    vertexShader:HXD_DROP_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* —— 书斋疏窗：屋舍一角（前墙留疏窗）+ 疏窗棂 + 冷灰窗纸 + 窗内书案茶盏 + 夫妻对影 ——
   同一座屋子三境共用：封面远景 / 壹境紧闭（影全隐、灯近熄）/ 贰境近观（点击闪回）。
   窗内剪影 opacity、暖忆光由各境按 fadeK 自控。 */
function makeShuzhai(o){
  o=o||{};
  const B=new GeoBag(), wallC=0x111722, wall2=0x0c101a, roofC=0x090d15;
  /* 前墙（x -3.7..3.7，留出疏窗口 x -1.6..1.6 / y 1.5..3.65） */
  const wl=new THREE.BoxGeometry(2.10,4.7,0.34); wl.translate(-2.65,2.35,0); B.put(wl,wallC);
  const wr=new THREE.BoxGeometry(2.10,4.7,0.34); wr.translate(2.65,2.35,0); B.put(wr,wallC);
  const wt=new THREE.BoxGeometry(3.20,1.05,0.34); wt.translate(0,4.175,0); B.put(wt,wallC);
  const wb=new THREE.BoxGeometry(3.20,1.50,0.34); wb.translate(0,0.75,0); B.put(wb,wallC);
  /* 侧墙 + 山墙 + 两坡顶 + 正脊 */
  [1,-1].forEach(function(s){
    const side=new THREE.BoxGeometry(0.36,4.4,5.6); side.translate(s*3.68,2.2,-2.6); B.put(side,wall2);
    const gab=new THREE.BoxGeometry(0.36,1.7,0.36); gab.translate(s*3.68,5.15,-2.6); B.put(gab,wall2);
  });
  const rl=new THREE.BoxGeometry(4.35,0.22,7.2); rl.rotateZ(0.453); rl.translate(-2.0,5.3,-2.6); B.put(rl,roofC);
  const rr=new THREE.BoxGeometry(4.35,0.22,7.2); rr.rotateZ(-0.453); rr.translate(2.0,5.3,-2.6); B.put(rr,roofC);
  const ridgeB=new THREE.BoxGeometry(0.30,0.30,7.4); ridgeB.translate(0,6.26,-2.6); B.put(ridgeB,roofC);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x2a3446,emissive:0x04060a}),{c:0xa8b6c8,i:0.20,p:2.5})));
  /* 疏窗框 + 疏朗窗棂（只两根竖棂——「疏」窗） */
  const FB=new GeoBag(), frC=0x1d2532, latC=0x0a0e15;
  const ft=new THREE.BoxGeometry(3.48,0.14,0.42); ft.translate(0,3.71,0); FB.put(ft,frC);
  const fb=new THREE.BoxGeometry(3.48,0.14,0.42); fb.translate(0,1.44,0); FB.put(fb,frC);
  const fl=new THREE.BoxGeometry(0.14,2.43,0.42); fl.translate(-1.67,2.575,0); FB.put(fl,frC);
  const frg=new THREE.BoxGeometry(0.14,2.43,0.42); frg.translate(1.67,2.575,0); FB.put(frg,frC);
  [0.53,-0.53].forEach(function(dx){
    const bar=new THREE.BoxGeometry(0.07,2.15,0.07); bar.translate(dx,2.575,0.12); FB.put(bar,latC);
  });
  const frame=new THREE.Mesh(mergeGeos(FB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
      specular:0x2a3446,emissive:0x04060a}),{c:0xa8b6c8,i:0.24,p:2.4}));
  g.add(frame);
  /* 冷灰窗纸（现实层：残阳冷灰透纸） */
  const paperMat=new THREE.MeshBasicMaterial({color:0x8fa0b4,fog:false,transparent:true,opacity:0.50,depthWrite:false});
  const paper=new THREE.Mesh(new THREE.PlaneGeometry(3.2,2.15),paperMat);
  paper.position.set(0,2.575,-0.10); g.add(paper);
  /* 暖忆窗光（点击后漫上的茶色暖：残阳满窗） */
  const warmMat=new THREE.MeshBasicMaterial({color:0xb08e80,fog:false,transparent:true,opacity:0.52,depthWrite:false});
  const warm=new THREE.Mesh(new THREE.PlaneGeometry(3.2,2.15),warmMat);
  warm.position.set(0,2.575,-0.06); warm.renderOrder=1; g.add(warm);
  /* 窗内剪影：书案 + 书册 + 茶壶茶盏 + 夫妻对影（妻举书、夫抚掌），暖黑剪影贴片 */
  const SB=new GeoBag(), silC=0x140d08;
  const top=new THREE.BoxGeometry(2.2,0.12,0.72); top.translate(0,1.66,0.55); SB.put(top,silC);
  [1,-1].forEach(function(s){
    const leg=new THREE.BoxGeometry(0.14,1.60,0.5); leg.translate(s*0.92,0.80,0.55); SB.put(leg,silC);
  });
  const bk1=new THREE.BoxGeometry(0.58,0.07,0.42); bk1.rotateY(0.14); bk1.translate(-0.62,1.76,0.55); SB.put(bk1,silC);
  const bk2=new THREE.BoxGeometry(0.52,0.06,0.38); bk2.rotateY(-0.10); bk2.translate(-0.58,1.82,0.55); SB.put(bk2,silC);
  const openL=new THREE.BoxGeometry(0.34,0.025,0.46); openL.rotateZ(0.16); openL.translate(0.24,1.74,0.55); SB.put(openL,silC);
  const openR=new THREE.BoxGeometry(0.34,0.025,0.46); openR.rotateZ(-0.16); openR.translate(0.56,1.74,0.55); SB.put(openR,silC);
  const pot=new THREE.CylinderGeometry(0.17,0.20,0.20,8); pot.translate(1.28,1.87,0.62); SB.put(pot,silC);
  const lid=new THREE.SphereGeometry(0.09,8,6); lid.translate(1.28,1.99,0.62); SB.put(lid,silC);
  const cup1=new THREE.CylinderGeometry(0.065,0.055,0.09,6); cup1.translate(0.92,1.77,0.60); SB.put(cup1,silC);
  const cup2=new THREE.CylinderGeometry(0.065,0.055,0.09,6); cup2.translate(1.58,1.77,0.58); SB.put(cup2,silC);
  /* 卢氏（左）：举书之影 */
  const torsoW=new THREE.CylinderGeometry(0.30,0.44,1.30,10); torsoW.translate(-0.72,2.10,0.30); SB.put(torsoW,silC);
  const shdW=new THREE.SphereGeometry(0.26,8,6); shdW.scale(1.5,0.6,0.8); shdW.translate(-0.72,2.72,0.30); SB.put(shdW,silC);
  const headW=new THREE.SphereGeometry(0.21,10,8); headW.scale(0.95,1.05,0.95); headW.translate(-0.70,3.06,0.30); SB.put(headW,silC);
  const bunW=new THREE.SphereGeometry(0.105,8,6); bunW.translate(-0.70,3.30,0.24); SB.put(bunW,silC);
  SB.put(limbGeo([-0.50,2.56,0.34],[-0.86,2.98,0.44],0.065,0.05,6),silC);           // 举书臂
  const book=new THREE.BoxGeometry(0.30,0.22,0.05); book.rotateZ(-0.5);
  book.translate(-0.94,3.06,0.48); SB.put(book,silC);                                // 手中书卷
  /* 容若（右）：俯身抚掌之影 */
  const torsoM=new THREE.CylinderGeometry(0.32,0.47,1.40,10); torsoM.translate(0.86,2.06,0.30); SB.put(torsoM,silC);
  const shdM=new THREE.SphereGeometry(0.27,8,6); shdM.scale(1.5,0.6,0.8); shdM.translate(0.86,2.70,0.30); SB.put(shdM,silC);
  const headM=new THREE.SphereGeometry(0.22,10,8); headM.scale(0.95,1.05,0.95); headM.translate(0.60,3.02,0.34); SB.put(headM,silC);
  SB.put(limbGeo([0.62,2.52,0.36],[0.16,2.62,0.52],0.068,0.052,6),silC);             // 伸臂向茶/书
  SB.put(limbGeo([1.10,2.52,0.34],[1.30,2.02,0.50],0.068,0.052,6),silC);             // 拊案之臂
  const silMat=new THREE.MeshBasicMaterial({color:0x140d08,transparent:true,opacity:0.94,depthWrite:false});
  const sil=new THREE.Mesh(mergeGeos(SB.list),silMat);
  sil.scale.z=0.25; sil.renderOrder=1; g.add(sil);
  /* 暖忆光：窗顶外辉 + 地面光池 + 暖点光（构造初值=逐帧写入的最大值，fadeK 铁律） */
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb08e80,
    transparent:true,opacity:0.32,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(6.5,6.5,1); glow.position.set(0,3.3,0.9); glow.renderOrder=3; g.add(glow);
  const poolGeo=new THREE.CircleGeometry(4.0,24); poolGeo.rotateX(-Math.PI/2);
  const poolMat=new THREE.MeshBasicMaterial({color:0xb08e80,transparent:true,opacity:0.19,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const pool=new THREE.Mesh(poolGeo,poolMat); pool.position.set(0,0.045,3.2); pool.renderOrder=2; g.add(pool);
  const light=new THREE.PointLight(0xb08e80,1.38,26); light.position.set(0,2.3,2.2); g.add(light);
  return {g,silMat,paperMat,warmMat,glowMat:glow.material,poolMat,light};
}

function bCover(){ // 封面 · 西风庭院 —— 冷灰残阳、黄叶辞枝
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-1.2; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:16,layers:2,peaks:5,seed:75203,color:0x070a10,atmo:0x232c3d,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  const sun=makeCanyang({r:7.5}); sun.g.position.set(-30,13,-185); g.add(sun.g);
  const house=makeShuzhai();
  house.g.position.set(11,0,-42); house.g.rotation.y=0.5; house.g.scale.setScalar(1.1); g.add(house.g);
  house.silMat.opacity=0; house.light.intensity=0; house.warmMat.opacity=0;
  const fig=makeFigure({pose:'独立',robe:0x1e2838,belt:0x4e5c76,skin:0xd0bda6,collar:0xa8b6c8,
    hat:'幞头',rimC:0xb0bcc9,rim:0.46,noProp:true,scale:1.15});
  fig.position.set(2,0,-26); fig.rotation.y=0.6; g.add(fig);
  const luoye=makeLuoye({n:40,box:[90,24,40],pos:[-4,12,-16],color:0x8a8168,size:4.4,speed:1.6,wind:2.4,maxA:0.42});
  g.add(luoye.points);
  const flow=makeFlow({n:130,box:[160,16,70],pos:[0,9,-40],color:0x8fa0b8,size:22,speed:4.8,maxA:0.12});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[230,22,120],pos:[0,9,-56],scale:76,color:0x8fa0ba,op:0.075});
  g.add(mist.g);
  const motes=makeGlow({n:46,box:[170,24,90],pos:[0,10,-34],color:0xa8b8d0,size:5.5,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x04060a,seed:75204,sway:1.0});
  reeds.g.position.set(-13,-1.2,34); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:75205,rim:0.14});
  rk.g.position.set(14,-1.8,32); g.add(rk.g);
  addLights(g,{c:0xa8b4c4,i:0.42,p:[-30,80,-40]},{c:0x19202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); flow.update(t); luoye.update(t); mist.update(t,k); motes.update(t);
    reeds.update(t,k); rk.update(t,k);
    fig.userData.update(t,k);
  }};
}

function bXifeng(){ // 一 · 西风残阳 —— 谁念西风独自凉；疏窗紧闭，独立残阳
  const g=new THREE.Group();
  const grd=makeGround({r:160,c1:0x07090e,c2:0x101520});
  grd.mesh.position.y=-0.4; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:17,layers:2,peaks:4,seed:75206,color:0x070a10,atmo:0x232c3d,fogK:0.62,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  const sun=makeCanyang({r:8}); sun.g.position.set(58,12,-180); g.add(sun.g);
  /* 疏窗小屋（窗闭：剪影全隐、灯近熄，只余冷灰窗纸） */
  const house=makeShuzhai();
  house.g.position.set(-9,0,-15); house.g.rotation.y=0.5; house.g.scale.setScalar(1.3); g.add(house.g);
  house.silMat.opacity=0; house.light.intensity=0; house.warmMat.opacity=0;
  /* 独立词人：望残阳而立 */
  const fig=makeFigure({pose:'独立',robe:0x1e2838,belt:0x51617c,skin:0xd0bda6,collar:0xa8b6c8,
    hat:'幞头',rimC:0xb0bcc9,rim:0.55,noProp:true,scale:1.8});
  fig.position.set(3.2,0,-10.5); fig.rotation.y=0.75; g.add(fig);
  /* 黄叶闭疏窗：落叶纷纷，密处扑窗 */
  const luoye=makeLuoye({n:56,box:[84,26,42],pos:[-4,13,-12],color:0x8a8168,size:4.8,speed:1.9,wind:3.0,maxA:0.5});
  g.add(luoye.points);
  /* 西风横流 */
  const flow=makeFlow({n:160,box:[150,16,70],pos:[0,9,-30],color:0x8fa0b8,size:24,speed:5.5,maxA:0.13});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[220,20,116],pos:[0,9,-48],scale:74,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  const motes=makeGlow({n:44,box:[150,22,80],pos:[0,9,-26],color:0xa8b8d0,size:5.5,speed:0.05,rise:0,maxA:0.22});
  g.add(motes.points);
  /* 远处归人（暮色里各自有家，独我无人念） */
  const crowd=makeCrowd({n:3,rect:[18,-40,10,4],seed:75207,color:0x10151f,rimC:0x8fa4c4,
    rim:0.12,sMin:0.4,sMax:0.55,y:0});
  g.add(crowd.mesh);
  const reeds=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:75208,sway:1.1});
  reeds.g.position.set(-14,-1.2,11); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:75209,rim:0.14});
  rk.g.position.set(14,-1.5,12); g.add(rk.g);
  addLights(g,{c:0xa8b4c4,i:0.44,p:[40,84,-30]},{c:0x1a212e,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); flow.update(t); luoye.update(t); mist.update(t,k); motes.update(t);
    crowd.update(t); reeds.update(t,k); rk.update(t,k);
    fig.userData.update(t,k);
  }};
}

function bDushu(){ // 二（末境·可点击）· 赌书泼茶 —— 点击「泼茶香」：茶香书影闪回 + 残阳满窗
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0};
  const grd=makeGround({r:160,c1:0x070a10,c2:0x0f1420});
  grd.mesh.position.y=-0.4; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:14,layers:2,peaks:4,seed:75210,color:0x070a10,atmo:0x232c3d,fogK:0.60,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-122); g.add(ridge.g);
  const sun=makeCanyang({r:8.5,glowMax:0.44}); sun.g.position.set(14,13,-168); g.add(sun.g);
  /* 疏窗小屋近观：窗内影伏而未现（寻常到被忽略），点击后闪回凝现 */
  const house=makeShuzhai();
  house.g.position.set(-8.5,0,-13); house.g.rotation.y=0.42; house.g.scale.setScalar(1.45); g.add(house.g);
  /* 词人独立窗前（现实之冷） */
  const fig=makeFigure({pose:'独立',robe:0x1e2838,belt:0x51617c,skin:0xd0bda6,collar:0xa8b6c8,
    hat:'幞头',rimC:0xb0bcc9,rim:0.55,noProp:true,scale:1.75});
  fig.position.set(-0.5,0,-9.5); fig.rotation.y=-2.0; g.add(fig);
  /* 茶香出窗：暖灰烟缕自窗前袅袅升起（点击后随暖忆变亮） */
  const chayan=makeGlow({n:16,box:[1.8,3.4,1.0],pos:[-8.5,3.6,-10.4],color:0xc9bba8,size:4.2,
    speed:0.22,rise:0.5,maxA:0.34});
  g.add(chayan.points);
  const luoye=makeLuoye({n:36,box:[70,22,34],pos:[4,11,-8],color:0x8a8168,size:4.2,speed:1.5,wind:2.2,maxA:0.4});
  g.add(luoye.points);
  const flow=makeFlow({n:110,box:[130,14,60],pos:[6,8,-32],color:0x8fa0b8,size:22,speed:4.2,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:5,spread:[200,18,100],pos:[0,8,-46],scale:70,color:0x8fa0ba,op:0.06});
  g.add(mist.g);
  const frost=makeGlow({n:36,box:[70,12,50],pos:[-2,5,-12],color:0xbfcde4,size:4.2,speed:0.12,rise:0.05,maxA:0.24});
  g.add(frost.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.2,w:18,d:8,color:0x04060a,seed:75211,rim:0.14});
  rk.g.position.set(21,-2.0,10); g.add(rk.g);
  const br=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:75212,sway:1.2,rim:0.16});
  br.g.position.set(-16,1.2,13); g.add(br.g);
  addLights(g,{c:0xa8b4c4,i:0.44,p:[-30,86,-26]},{c:0x1a212e,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const el=ctl.clicked?ctl.t-ctl.clickT:0;
      const e=ease(clamp(el/3.0,0,1));
      ridge.update(t,0); mist.update(t,k); flow.update(t); luoye.update(t); chayan.update(t); frost.update(t);
      rk.update(t,k); br.update(t,k);
      fig.userData.update(t,k);
      house.silMat.opacity=k*(0.06+0.88*e);                    // 茶香书影闪回凝现
      house.warmMat.opacity=k*(0.52*e);                        // 残阳满窗：暖忆漫上窗纸
      house.glowMat.opacity=k*(0.08+0.20*e+0.04*Math.sin(t*0.8));
      house.poolMat.opacity=k*(0.04+0.15*e);
      house.light.intensity=k*(0.12+1.18*e+0.08*Math.sin(t*0.8));
      sun.glowMat.opacity=k*(0.30+0.14*e);                     // 残阳微亮，如回望
    },onEnter(){
      pluck(0,0.3,0.07); pluck(2,0.9,0.05);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(4,0.05,0.10); pluck(2,0.6,0.08); pluck(0,1.2,0.07);
        const fl=$('#flash'); fl.textContent='当时只道是寻常'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x121926),fd:0.0055,star:0.28,
  moon:new THREE.Vector3(0,-220,0),ms:0.001,mph:0.04,mhaze:0.03,dirC:C(0xa8b4c4),dirI:0.44,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x1a212e),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,58],t:[0,9.4,52],lf:[0,9,-40],lt:[2,9,-46]},
  sky:()=>SK({top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x10161f),fd:0.0050,star:0.30,
    dirC:C(0xa8b4c4),dirI:0.40,ambC:C(0x182031),ambI:0.62}) },
{ name:'西风残阳',dwell:16,river:0.03,build:bXifeng,
  cam:{f:[0,5.4,20],t:[1.0,5.1,17],lf:[4,4.6,-22],lt:[5,4.3,-26]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x161e2c),bot:C(0x090c12),fog:C(0x121926),fd:0.0060,star:0.20,
    dirC:C(0xa8aeb8),dirI:0.44,ambC:C(0x1a212e),ambI:0.58}) },
{ name:'赌书泼茶',dwell:20,river:0.03,build:bDushu,
  cam:{f:[0,5.8,18],t:[-0.7,5.4,15],lf:[-6,4.6,-13],lt:[-6.8,4.3,-16]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x171f2e),bot:C(0x090c12),fog:C(0x111825),fd:0.0055,star:0.26,
    dirC:C(0xa8aeb8),dirI:0.46,ambC:C(0x1a212e),ambI:0.6}) },
];
"""
