# -*- coding: utf-8 -*-
"""yangzhoman-huaizuo.py —— 《扬州慢·淮左名都》（宋·姜夔，no.197，烟雨江南·黍离之悲变体）生成配置
四境（queue.json 分境口径，长调对句成境 N=4）：
  名都荠麦（淮左名都+竹西佳处+解鞍少驻+春风十里尽荠麦青青）/
  空城清角（自胡马窥江+废池乔木犹厌言兵+渐黄昏清角吹寒都在空城）/
  杜郎须惊（杜郎俊赏+重到须惊+豆蔻青楼难赋深情）/
  冷月无声（二十四桥仍在+波心荡冷月无声+念桥边红药年年知为谁生·末境可点击）。
美术立意：全页禁金，主色黛蓝 #8f9fc9；荠麦青为唯一冷绿，红药为全页唯一暖红（只此一点）。
标志性瞬间「波心冷月」：天上无月、月沉波心——二十四桥卧波，冷月的影子在波心无声摇荡（词眼）。
末境点击：月影入波无声荡漾（涟漪骤盛）+ 荠麦青青漫城（青雾漫过空城）。"""

META = dict(
    N=4, slug='yangzhoman-huaizuo', title='扬州慢·淮左名都', dyn='宋 · 姜夔', brand_author='姜 夔',
    gold_rgb='143,159,201',
    root=""":root{
  --gold:#8f9fc9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(143,159,201,.28);
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
    tip='轻点画面 / 按空格 —— 月影入波无声荡漾，荠麦青青漫过空城',
    hint='← → 键或空格逐境游览 · 末境可点击画面：月影入波无声荡漾，荠麦青青漫城',
    cover_read='扬州慢。宋，姜夔。淮左名都，竹西佳处，解鞍少驻初程。过春风十里，尽荠麦青青。',
    cover_p1='四重意境，随词句次第展开：名都竹西、解鞍少驻，而春风十里长街尽是荠麦青青的荒芜；废池乔木犹厌言兵，黄昏清角吹寒、都在空城的死寂；杜郎俊赏，纵有豆蔻词工、青楼梦好也难赋深情的惊叹；以及二十四桥仍在、波心荡冷月无声，念桥边红药年年知为谁生的天问。',
    cover_p2='边读词，边走进姜夔笔下这座劫后的空城，体会那份「黍离之悲」——昔盛今衰的家国之痛，千古绝唱。',
    end_h2='冷月 · 红药', cn_word='四',
    words_js="['再游一次，波心月冷','初识白石，尚需共读','渐入词境，略有所感','黍离之悲，渐上心头','深得白石词心','红药年年，与君同问']",
    sky_atmo='0x36445a',
)

POEM_JS = """const POEM = [
{ name:'名都荠麦', jing:'淮左名都，竹西佳处——词人解鞍少驻，转入初程；春风十里长街，尽荠麦青青。（词人解鞍，鞍马静立，长街荒芜）',
  segs:[
   {c:'淮左名都，', p:py('huái zuǒ míng dū')},
   {c:'竹西佳处，', p:py('zhú xī jiā chù')},
   {c:'解鞍少驻初程。', p:py('jiě ān shǎo zhù chū chéng')},
   {c:'过春风十里，', p:py('guò chūn fēng shí lǐ')},
   {c:'尽荠麦青青。', p:py('jìn jì mài qīng qīng')}],
  read:'淮左名都，竹西佳处，解鞍少驻初程。过春风十里，尽荠麦青青。',
  yisi:'淮河东部的著名都城，竹西亭畔的清幽佳境——我解下马鞍，稍作停留，走上这初来的旅程。曾经春风十里的繁华长街，如今满眼都是青青的荠菜野麦。',
  zhu:[['淮左','淮河以东、淮南东路地区，宋朝设淮南东路，扬州为其首府'],['竹西佳处','扬州城东竹西亭，以竹景清幽著称；语出杜牧「谁知竹西路，歌吹是扬州」'],['解鞍少驻','解下马鞍，稍作停留。少驻，短暂停留；少，读 shǎo'],['春风十里','用杜牧「春风十里扬州路」句，写昔日扬州的繁华长街'],['荠麦青青','荠菜和野麦一片青绿——昔日繁华之地，如今遍地荒芜。荠，读 jì']]} ,
{ name:'空城清角', jing:'自胡马窥江去后，废池乔木犹厌言兵；渐黄昏，清角吹寒，都在空城。（废城死寂，一声清角，寒意四起）',
  segs:[
   {c:'自胡马窥江去后，', p:py('zì hú mǎ kuī jiāng qù hòu')},
   {c:'废池乔木，', p:py('fèi chí qiáo mù')},
   {c:'犹厌言兵。', p:py('yóu yàn yán bīng')},
   {c:'渐黄昏，', p:py('jiàn huáng hūn')},
   {c:'清角吹寒，', p:py('qīng jiǎo chuī hán')},
   {c:'都在空城。', p:py('dōu zài kōng chéng')}],
  read:'自胡马窥江去后，废池乔木，犹厌言兵。渐黄昏，清角吹寒，都在空城。',
  yisi:'自从金兵南侵长江之后，连荒废的池苑、古老的大树，都仿佛厌恶再提起那场战争。渐渐到了黄昏，凄清的号角声送来阵阵寒意——这一切，都回荡在劫后的空城之上。',
  zhu:[['胡马窥江','指金兵南侵至长江流域：1129—1130 年金兵攻陷扬州焚掠而去，1161 年完颜亮再度大举南侵'],['废池乔木','荒废的池苑与高大的老树——战争浩劫后幸存的旧物'],['犹厌言兵','（它们）仿佛还厌恶谈起战争——拟人手法：无情的池、树尚且厌战，何况人情'],['清角吹寒','凄清的号角声送来寒意。角，号角，读 jiǎo'],['都在空城','暮色与角声，弥漫在劫后的空城之上。都，读 dōu']]} ,
{ name:'杜郎须惊', jing:'杜郎俊赏，算而今重到须惊——纵豆蔻词工、青楼梦好，难赋深情。（昔日繁华化作雾中幻影，须臾明灭）',
  segs:[
   {c:'杜郎俊赏，', p:py('dù láng jùn shǎng')},
   {c:'算而今，', p:py('suàn ér jīn')},
   {c:'重到须惊。', p:py('chóng dào xū jīng')},
   {c:'纵豆蔻词工，', p:py('zòng dòu kòu cí gōng')},
   {c:'青楼梦好，', p:py('qīng lóu mèng hǎo')},
   {c:'难赋深情。', p:py('nán fù shēn qíng')}],
  read:'杜郎俊赏，算而今，重到须惊。纵豆蔻词工，青楼梦好，难赋深情。',
  yisi:'杜牧有卓越的赏游之才，料想他如今重到扬州，也必定会大吃一惊。纵然有咏「豆蔻梢头」的精工词笔、「青楼梦好」的风流才情，也难以表达我面对此城的一片深情悲怆。',
  zhu:[['杜郎俊赏','杜牧曾如此游赏。杜郎，唐代诗人杜牧，曾任扬州淮南节度使掌书记；俊赏，卓越的鉴赏游赏'],['算而今','设想算来，如今'],['重到须惊','若重新来到，定会吃惊。重，读 chóng'],['豆蔻词工','杜牧《赠别》「豆蔻梢头二月初」以豆蔻喻少女，词笔精工。豆蔻，读 dòu kòu'],['青楼梦好','杜牧「十年一觉扬州梦，赢得青楼薄幸名」——纵有当年风流词笔'],['难赋深情','也难以表达面对劫后荒城的深沉悲怆——以旧日繁华反衬今日之痛']]} ,
{ name:'冷月无声', jing:'二十四桥仍在，波心荡，冷月无声；念桥边红药，年年知为谁生？（词眼：桥在、月冷、城空——点击冷月，月影入波）',
  segs:[
   {c:'二十四桥仍在，', p:py('èr shí sì qiáo réng zài')},
   {c:'波心荡，', p:py('bō xīn dàng')},
   {c:'冷月无声。', p:py('lěng yuè wú shēng')},
   {c:'念桥边红药，', p:py('niàn qiáo biān hóng yào')},
   {c:'年年知为谁生。', p:py('nián nián zhī wèi shuí shēng')}],
  read:'二十四桥仍在，波心荡，冷月无声。念桥边红药，年年知为谁生。',
  yisi:'二十四桥依然还在，水波中心，一弯冷月无声地摇荡。想那桥边的红芍药，一年又一年，不知是为谁而生、为谁而开呢？——桥在、月冷、城空，黍离之悲，至此痛彻千古。',
  zhu:[['二十四桥','扬州名胜，一说城中有二十四座桥，一说即吴家砖桥（一名红药桥）'],['波心荡','月亮的影子在波心轻轻摇荡——词眼所在：桥仍在、月正冷、城已空'],['冷月无声','清冷的月亮毫无声息——以「无声」写死寂，物是人非，欲说无凭'],['红药','红色的芍药花；二十四桥又名红药桥'],['年年知为谁生','一年又一年，究竟为谁而生呢？——花木无知、繁华不返的天问'],['黍离之悲','《诗经·黍离》写周大夫过故宗庙，见禾黍丛生而悲——后世以「黍离之悲」代指故国昔盛今衰的悲痛']]}];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「过春风十里，」的下一句是？', o:['尽荠麦青青','废池乔木','波心荡，冷月无声'], a:0},
 {q:'「二十四桥仍在，」的下一句是？', o:['念桥边红药','年年知为谁生','波心荡，冷月无声'], a:2},
 {q:'「纵豆蔻词工」中「豆蔻」的读音与用意是？', o:['dòu kòu，用杜牧《赠别》「豆蔻梢头二月初」典——纵有杜牧咏扬州风流的名笔，也难赋眼前深情','mò kòu，指军中豆绿色的战旗，写胡马窥江的兵气','dòu kòu，实写桥边的香料作物，与红药相呼应'], a:0},
 {q:'关于《扬州慢》，下列说法正确的是？', o:['柳永写的市井繁华词，描写扬州的歌舞升平','姜夔的自度曲——词牌与曲调均出自其手，小序记冬至夜过扬州，感慨金兵两次南侵后的城池残破','苏轼途经扬州时怀念杜牧而作'], a:1},
 {q:'这首词「黍离之悲」的核心是？', o:['对二十四桥月色之美的赞叹','对桥边红药年年自开的好奇','家国昔盛今衰、繁华成空的悲慨——名城成空城，红药无知年年自开，更衬人事全非之痛'], a:2},
];
"""

SCENES_JS = """/* ================= 扬州慢·淮左名都 · 四境场景（烟雨江南·黍离之悲变体：黛蓝湿雾、荠麦青青、空城冷月） =================
   美术立意：全页禁金，主色黛蓝 #8f9fc9；荠麦青为唯一冷绿，红药为全页唯一暖红（只此一点）。
   标志性瞬间「波心冷月」：天上无月、月沉波心——二十四桥卧波，冷月的影子在波心无声摇荡（词眼）。
   末境点击：月影入波无声荡漾（涟漪骤盛）+ 荠麦青青漫城（青雾漫过空城）。 */

/* —— 荠麦青青：低丛野麦（全页唯一冷绿；GeoBag 合批 1 mesh + 摇摆着色器，uFade 交 setFade）—— */
const ZM_QM_VERT=`
uniform float uTime; uniform float uSway; varying vec2 vUv;
void main(){
  vUv=uv;
  vec3 p=position;
  float k=clamp(uv.y*1.4,0.0,1.0);
  float ph=p.x*1.7+p.z*2.3;
  p.x+=sin(uTime*0.8+ph)*uSway*k;
  p.z+=cos(uTime*0.6+ph*1.3)*uSway*0.5*k;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const ZM_QM_FRAG=`
uniform vec3 uC; uniform vec3 uTipC; uniform float uFade; varying vec2 vUv;
void main(){
  vec3 col=mix(uC,uTipC,smoothstep(0.15,0.95,vUv.y));
  gl_FragColor=vec4(col,uFade);
}`;
function makeQimaiZM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?71:o.seed);
  const n=o.n===undefined?60:o.n, w=o.w===undefined?40:o.w, d=o.d===undefined?10:o.d;
  const h=o.h===undefined?0.9:o.h;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*d, hh=h*(0.5+R()*0.9), ww=0.34+R()*0.3, rr=R()*0.9;
    for(let k=0;k<2;k++){
      const pl=new THREE.PlaneGeometry(ww,hh,1,2);
      if(k)pl.rotateY(Math.PI/2);
      pl.rotateY(rr);
      pl.translate(x,hh/2,z);
      B.put(pl,0xffffff);
    }
  }
  const mat=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uTime:{value:0},uSway:{value:o.sway===undefined?0.12:o.sway},
      uC:{value:C(o.color===undefined?0x2e5346:o.color)},
      uTipC:{value:C(o.tip===undefined?0x4f7f6a:o.tip)},uFade:{value:1}},
    vertexShader:ZM_QM_VERT,fragmentShader:ZM_QM_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat); mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const api={g,update(t,k){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    mat.uniforms.uTime.value=t; }};
  g.userData.update=api.update;
  return api;
}

/* —— 竹：竹西佳处（秆 3 节 + 叶片，GeoBag 合批 1 mesh）—— */
function makeZhuZM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?53:o.seed);
  const n=o.n===undefined?6:o.n, h=o.h===undefined?6.5:o.h;
  const B=new GeoBag(), culm=0x1d2a24, leaf=0x27392f;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*1.8, z=(R()-0.5)*1.6, hh=h*(0.6+R()*0.55), lean=(R()-0.5)*0.3;
    for(let k=0;k<3;k++){
      const seg=new THREE.CylinderGeometry(0.045,0.06,hh/3,5);
      seg.rotateZ(lean*(k+1)*0.3);
      seg.translate(x+lean*hh*0.06*k,hh*(k+0.5)/3,z);
      B.put(seg,k%2?shadeColor(culm,1.12):culm);
    }
    for(let L=0;L<4;L++){
      const lf=new THREE.PlaneGeometry(0.9,0.16);
      lf.rotateX((R()-0.5)*0.8); lf.rotateZ(-0.5-R()*0.5); lf.rotateY(R()*6.28);
      lf.translate(x+(R()-0.5)*0.5,hh*(0.6+R()*0.4),z+(R()-0.5)*0.5);
      B.put(lf,leaf);
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3a34,emissive:0x050a08,side:THREE.DoubleSide}),{c:0x8f9fc9,i:0.2,p:2.6})));
  return g;
}

/* —— 竹西亭：石基 + 四柱 + 攒尖顶 + 顶珠（GeoBag 合批 1 mesh）—— */
function makeTingZM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?59:o.seed);
  const w=o.w===undefined?4.4:o.w, h=o.h===undefined?3.4:o.h;
  const B=new GeoBag(), c1=0x12171f, c2=0x1a2230;
  const base=new THREE.BoxGeometry(w*1.25,0.5,w*1.25); base.translate(0,0.25,0); B.put(base,c1);
  const px=w/2;
  [[px,px],[px,-px],[-px,px],[-px,-px]].forEach(function(p){
    const post=new THREE.CylinderGeometry(0.10,0.13,h,6); post.translate(p[0],0.5+h/2,p[1]); B.put(post,c2);
  });
  const roof=new THREE.ConeGeometry(w*0.92,h*0.52,4); roof.rotateY(Math.PI/4);
  roof.translate(0,0.5+h+h*0.26,0); B.put(roof,c1);
  const knob=new THREE.SphereGeometry(0.16,6,5); knob.translate(0,0.5+h+h*0.55,0); B.put(knob,c2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x34404e,emissive:0x04060a}),{c:0x8f9fc9,i:0.30,p:2.5})));
  return g;
}

/* —— 解鞍之马：低头 grazes 荠麦（身/颈/头/鬃/四腿/尾，GeoBag 合批 1 mesh；朝 +x）—— */
function makeHorseZM(o){
  o=o||{};
  const c=o.color===undefined?0x181d25:o.color;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.62,9,7); body.scale(1.65,0.92,0.66); body.translate(0,1.12,0); B.put(body,c);
  const neck=new THREE.CylinderGeometry(0.13,0.24,1.2,7);
  neck.rotateZ(-1.05); neck.translate(1.0,0.86,0); B.put(neck,shadeColor(c,1.08));
  const head=new THREE.BoxGeometry(0.64,0.21,0.22); head.rotateZ(0.55); head.translate(1.52,0.4,0); B.put(head,shadeColor(c,1.12));
  for(const sz of [0.09,-0.09]){
    const ear=new THREE.ConeGeometry(0.05,0.16,4); ear.rotateZ(-0.3); ear.translate(1.3,0.62,sz); B.put(ear,shadeColor(c,1.1));
  }
  const mane=new THREE.BoxGeometry(0.52,0.1,0.07); mane.rotateZ(-1.0); mane.translate(1.14,1.08,0); B.put(mane,shadeColor(c,1.3));
  [[0.74,0.3],[0.74,-0.3],[-0.74,0.3],[-0.74,-0.3]].forEach(function(p){
    const leg=new THREE.CylinderGeometry(0.07,0.05,1.18,6); leg.translate(p[0],0.59,p[1]); B.put(leg,c);
  });
  const tail=new THREE.CylinderGeometry(0.05,0.02,0.92,5); tail.rotateZ(0.65); tail.translate(-1.2,0.95,0); B.put(tail,shadeColor(c,0.85));
  const mesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2c3442,emissive:0x04060a}),{c:0x8f9fc9,i:0.3,p:2.6}));
  mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 空城残垣：段墙 + 雉堞随机残缺 + 豁口碎砖（GeoBag 合批 1 mesh）—— */
function makeWallZM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?97:o.seed);
  const w=o.w===undefined?40:o.w, h=o.h===undefined?7:o.h, d=o.d===undefined?2.4:o.d;
  const breach=o.breach===undefined?-1:o.breach;      // 0..1 沿墙位置的豁口；-1 无
  const B=new GeoBag(), base=o.color===undefined?0x11161e:o.color;
  if(breach>=0){
    const bx=-w/2+breach*w, gw=4.6;
    const La=Math.max(0.1,bx-gw/2+w/2), Lb=Math.max(0.1,w/2-(bx+gw/2));
    const segA=new THREE.BoxGeometry(La,h,d); segA.translate(-w/2+La/2,h/2,0); B.put(segA,base);
    const segB=new THREE.BoxGeometry(Lb,h,d); segB.translate(w/2-Lb/2,h/2,0); B.put(segB,base);
    const jagA=new THREE.BoxGeometry(1.6,h*0.3,d*0.9); jagA.rotateZ(-0.12); jagA.translate(bx-gw/2-0.4,h*0.92,0);
    B.put(jagA,shadeColor(base,1.1));
    const jagB=new THREE.BoxGeometry(1.4,h*0.24,d*0.9); jagB.rotateZ(0.1); jagB.translate(bx+gw/2+0.3,h*0.9,0);
    B.put(jagB,shadeColor(base,1.05));
    for(let i=0;i<5;i++){
      const rb=new THREE.BoxGeometry(1.0+R()*1.2,0.5+R()*0.7,1.0+R()*0.6);
      rb.rotateZ((R()-0.5)*0.7); rb.rotateY((R()-0.5)*0.6);
      rb.translate(bx+(R()-0.5)*gw*1.2,0.28+R()*0.5,(R()-0.5)*2.0);
      B.put(rb,shadeColor(base,0.9+0.3*R()));
    }
  } else {
    const body=new THREE.BoxGeometry(w,h,d); body.translate(0,h/2,0); B.put(body,base);
  }
  const top=new THREE.BoxGeometry(w*1.005,0.3,d*1.25); top.translate(0,h+0.15,0); B.put(top,shadeColor(base,1.25));
  const n=Math.floor(w/1.7);
  for(let i=0;i<=n;i++){
    const x=-w/2+1.0+i*(w-2.0)/n;
    if(breach>=0&&Math.abs(x-(-w/2+breach*w))<3.0)continue;
    if(R()<0.16)continue;
    const mh=0.55+R()*0.55;
    const m=new THREE.BoxGeometry(1.05,mh,0.55); m.translate(x,h+0.3+mh/2,0);
    B.put(m,shadeColor(base,1.05+0.25*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3444,emissive:0x04060a}),{c:0x8f9fc9,i:0.24,p:2.5})));
  return g;
}

/* —— 谯楼（角楼）：台基 + 楼身 + 上层 + 四角攒尖顶（GeoBag 合批 1 mesh）—— */
function makeJiaoLouZM(o){
  o=o||{};
  const B=new GeoBag(), c1=0x10151d, c2=0x171e2a;
  const plat=new THREE.BoxGeometry(6.4,1.4,6.4); plat.translate(0,0.7,0); B.put(plat,c1);
  const body=new THREE.BoxGeometry(4.0,4.6,4.0); body.translate(0,3.7,0); B.put(body,c2);
  const rail=new THREE.BoxGeometry(4.7,0.25,4.7); rail.translate(0,6.1,0); B.put(rail,shadeColor(c2,1.2));
  const up=new THREE.BoxGeometry(2.9,2.5,2.9); up.translate(0,7.5,0); B.put(up,c2);
  const roof=new THREE.ConeGeometry(3.1,1.5,4); roof.rotateY(Math.PI/4); roof.translate(0,9.5,0); B.put(roof,c1);
  const knob=new THREE.SphereGeometry(0.2,6,5); knob.translate(0,10.4,0); B.put(knob,shadeColor(c2,1.3));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x303c4c,emissive:0x04060a}),{c:0x8f9fc9,i:0.26,p:2.5})));
  return g;
}

/* —— 废池乔木之乔木：枯木（干 + 斜枝 limbGeo，GeoBag 合批 1 mesh）—— */
function makeDeadTreeZM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?83:o.seed);
  const h=o.h===undefined?8:o.h;
  const B=new GeoBag(), c=0x14171d;
  const trunk=new THREE.CylinderGeometry(0.16,0.36,h*0.52,6); trunk.translate(0,h*0.26,0); B.put(trunk,c);
  for(let i=0;i<6;i++){
    const a=R()*6.283, el=0.5+R()*0.7;
    const dx=Math.cos(a)*h*(0.16+R()*0.2), dz=Math.sin(a)*h*(0.12+R()*0.16);
    const br=limbGeo([0,h*(0.42+R()*0.14),0],[dx,h*(0.62+R()*0.36),dz],0.10,0.025,5);
    B.put(br,i%2?shadeColor(c,1.15):c);
    if(R()<0.7){
      const t=limbGeo([dx*0.8,h*0.7,dz*0.8],[dx*1.5,h*(0.8+R()*0.2),dz*1.5],0.04,0.015,4);
      B.put(t,shadeColor(c,1.2));
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x28303e,emissive:0x03050a}),{c:0x7288a0,i:0.18,p:2.6})));
  return g;
}

/* —— 清角吹寒：角楼声波化作寒纹，一圈圈漫过空城（单面着色器，additive 冷环，无声而寒）—— */
const ZM_JIAO_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const ZM_JIAO_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  vec2 p=vUv*2.0-1.0; float r=length(p);
  float w=sin(r*9.0-uTime*1.5);
  float band=smoothstep(0.55,0.95,w);
  float env=exp(-r*2.6)*smoothstep(0.10,0.24,r);
  float a=band*env*0.5*uFade*uK;
  if(a<0.004) discard;
  vec3 col=mix(vec3(0.56,0.66,0.82),vec3(0.74,0.84,1.0),band);
  gl_FragColor=vec4(col,a);
}`;
function makeHanjiaoZM(o){
  o=o||{};
  const s=o.size===undefined?80:o.size;
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.8}},
    vertexShader:ZM_JIAO_VERT,fragmentShader:ZM_JIAO_FRAG});
  const mesh=new THREE.Mesh(new THREE.PlaneGeometry(s,s),mat);
  mesh.rotation.x=-Math.PI/2; mesh.renderOrder=4; mesh.frustumCulled=false;
  const g=new THREE.Group(); g.add(mesh);
  const api={g,update(t,k){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    mat.uniforms.uTime.value=t;
    mat.uniforms.uK.value=k*(0.75+0.25*Math.sin(t*0.47)); }};
  g.userData.update=api.update;
  return api;
}

/* —— 幻影繁华：旧日楼阁画桥的雾中虚像（additive 顶点色着色器，须臾明灭）—— */
const ZM_PH_VERT=`
attribute vec3 color; varying vec3 vC;
void main(){ vC=color; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const ZM_PH_FRAG=`
uniform float uFade; uniform float uK; varying vec3 vC;
void main(){ gl_FragColor=vec4(vC*1.6,uFade*uK); }`;
function makePhantomZM(){
  const B=new GeoBag();
  const c1=0x2a3550, c2=0x4a3a4c, c3=0x222e48, ck=0x5a4256;
  function lou(x,z,s){
    const b1=new THREE.BoxGeometry(2.6*s,1.7*s,2.0*s); b1.translate(x,0.85*s,z); B.put(b1,c1);
    const b2=new THREE.BoxGeometry(1.9*s,1.4*s,1.5*s); b2.translate(x,2.4*s,z); B.put(b2,c1);
    const r1=new THREE.ConeGeometry(2.2*s,0.8*s,4); r1.rotateY(Math.PI/4); r1.translate(x,3.7*s,z); B.put(r1,c2);
    const r2=new THREE.ConeGeometry(1.6*s,0.6*s,4); r2.rotateY(Math.PI/4); r2.translate(x,4.4*s,z); B.put(r2,c2);
  }
  lou(-6,2,1.15); lou(3.5,-2,0.9); lou(9,-6,0.7);
  const arch=new THREE.TorusGeometry(3.6,0.28,6,16,Math.PI); arch.scale(1,0.5,1); arch.translate(-11,0.02,4);
  B.put(arch,c3);
  const deck=new THREE.TorusGeometry(4.1,0.10,5,16,Math.PI); deck.scale(1,0.5,1); deck.translate(-11,0.06,4);
  B.put(deck,shadeColor(c3,1.4));
  for(let i=0;i<2;i++){
    const st=new THREE.CylinderGeometry(0.03,0.04,1.0,4); st.translate(-8.5+i*1.4,0.5,6.5-i*0.8); B.put(st,0x244034);
    const fl=new THREE.IcosahedronGeometry(0.2,0); fl.translate(-8.5+i*1.4,1.1,6.5-i*0.8); B.put(fl,ck);
  }
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    blending:THREE.AdditiveBlending,
    uniforms:{uFade:{value:1},uK:{value:0.16}},
    vertexShader:ZM_PH_VERT,fragmentShader:ZM_PH_FRAG});
  const mesh=new THREE.Mesh(mergeGeos(B.list),mat);
  mesh.frustumCulled=false; mesh.renderOrder=2;
  const g=new THREE.Group(); g.add(mesh);
  const api={g,update(t,k){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    mat.uniforms.uK.value=k*(0.15+0.05*Math.sin(t*0.7)+0.03*Math.sin(t*2.3));
    g.position.y=0.15*Math.sin(t*0.4); }};
  g.userData.update=api.update;
  return api;
}

/* —— 二十四桥：低拱长桥（拱+桥面带+双石栏+24 望柱+桥墩，GeoBag 合批 1 mesh；拱跨沿 x）—— */
function makeQiaoZM(o){
  o=o||{};
  const span=o.span===undefined?18:o.span;
  const Rr=span*0.5, sy=o.sy===undefined?0.30:o.sy;
  const B=new GeoBag(), stone=0x161b22, stone2=0x12171f;
  const arch=new THREE.TorusGeometry(Rr,0.62,8,30,Math.PI); arch.scale(1,sy,1); B.put(arch,stone);
  const deck=new THREE.TorusGeometry(Rr+0.35,0.14,5,30,Math.PI); deck.scale(1,sy,1);
  deck.translate(0,0.10,0); B.put(deck,shadeColor(stone,1.35));
  [1.05,-1.05].forEach(function(off){
    const rail=new THREE.TorusGeometry(Rr+0.35,0.05,4,30,Math.PI); rail.scale(1,sy,1);
    rail.translate(0,0.75,off); B.put(rail,shadeColor(stone,1.5));
    for(let i=1;i<=12;i++){
      const a=Math.PI*i/12;
      const px=Math.cos(a)*(Rr+0.35), py=Math.sin(a)*(Rr+0.35)*sy+0.72;
      const post=new THREE.BoxGeometry(0.09,0.55,0.09); post.translate(px,py,off);
      B.put(post,shadeColor(stone,1.4));
    }
  });
  [1,-1].forEach(function(s){
    const pier=new THREE.BoxGeometry(1.3,1.6,3.2); pier.translate(s*(Rr-0.4),-0.55,0); B.put(pier,stone2);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x36424e,emissive:0x05080c}),{c:0x8f9fc9,i:0.28,p:2.5})));
  return g;
}

/* —— 波心冷月（标志性瞬间）：天上无月，月影沉在波心——平躺月盘 + 水汽月晕 + 无声涟漪 —— */
const ZM_RIP_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const ZM_RIP_FRAG=`
uniform float uTime; uniform float uFade; uniform float uAmp; varying vec2 vUv;
void main(){
  vec2 p=vUv*2.0-1.0; float r=length(p);
  float w=sin(r*20.0-uTime*1.1);
  float band=pow(max(w,0.0),3.0);
  float env=smoothstep(0.10,0.22,r)*exp(-r*2.4);
  float a=band*env*uAmp*uFade;
  if(a<0.004) discard;
  gl_FragColor=vec4(vec3(0.72,0.82,0.96),a*0.55);
}`;
function makeShuiYueZM(o){
  o=o||{};
  const r=o.r===undefined?5.2:o.r;
  const g=new THREE.Group();
  const disc=new THREE.Mesh(new THREE.CircleGeometry(r,40),
    new THREE.MeshBasicMaterial({map:limbTex(),color:0xdce8f8,transparent:true,opacity:1.0,
      fog:false,depthWrite:false}));
  disc.rotation.x=-Math.PI/2; disc.position.y=0.08; disc.renderOrder=2; g.add(disc);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaec4e2,
    transparent:true,opacity:0.22,depthWrite:false,fog:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(r*3.4,r*1.5,1); glow.position.y=1.1; glow.renderOrder=3; g.add(glow);
  const rmat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uAmp:{value:0.5}},
    vertexShader:ZM_RIP_VERT,fragmentShader:ZM_RIP_FRAG});
  const rmesh=new THREE.Mesh(new THREE.PlaneGeometry(r*7.2,r*7.2),rmat);
  rmesh.rotation.x=-Math.PI/2; rmesh.position.y=0.12; rmesh.renderOrder=4; rmesh.frustumCulled=false;
  g.add(rmesh);
  const api={g,update(t,k,ext){ if(k===undefined)k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ext=ext||0;
    rmat.uniforms.uTime.value=t;
    rmat.uniforms.uAmp.value=k*(0.5+1.3*ext);
    disc.material.opacity=k*(0.78+0.06*Math.sin(t*0.8)+0.10*ext);
    glow.material.opacity=k*(0.13+0.05*Math.sin(t*0.6)+0.04*ext);
  }};
  g.userData.update=api.update;
  return api;
}

/* —— 桥边红药：红芍药一丛（茎/叶冷绿，花头全页唯一暖红；GeoBag 合批 1 mesh）—— */
function makeHongyaoZM(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?89:o.seed);
  const n=o.n===undefined?3:o.n;
  const B=new GeoBag(), stem=0x2a3a2e, leaf=0x2c4434, petal=0x8e4650, core=0x6e3038;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*1.1, z=(R()-0.5)*0.9, hh=0.75+R()*0.45;
    const st=new THREE.CylinderGeometry(0.028,0.04,hh,5); st.translate(x,hh/2,z); B.put(st,stem);
    for(let L=0;L<3;L++){
      const lf=new THREE.PlaneGeometry(0.42,0.13);
      lf.rotateZ(-0.5-R()*0.4); lf.rotateY(R()*6.28);
      lf.translate(x+(R()-0.5)*0.24,hh*(0.3+L*0.22),z+(R()-0.5)*0.2);
      B.put(lf,leaf);
    }
    const fl=new THREE.IcosahedronGeometry(0.20+R()*0.08,0); fl.scale(1,0.82,1);
    fl.translate(x,hh+0.14,z); B.put(fl,petal);
    const co=new THREE.IcosahedronGeometry(0.10,0); co.translate(x,hh+0.18,z); B.put(co,core);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x443036,emissive:0x120407,side:THREE.DoubleSide}),{c:0xb87a80,i:0.22,p:2.4})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

function bCoverZM(){ // 卷首 · 江城烟雨 —— 名都城郭远影，荠麦漫野，烟雨迷蒙
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0d1117,c2:0x151c26});
  grd.mesh.position.y=-1.4; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:20,layers:2,peaks:4,seed:1971,color:0x0a0e14,atmo:0x36445a,fogK:0.70,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,20); g.add(ridge.g);
  const wall=makeWallZM({w:110,h:7,seed:1973}); wall.position.set(0,0,-64); g.add(wall);
  const tower=makeJiaoLouZM(); tower.position.set(-24,0,-62); tower.scale.setScalar(0.9); g.add(tower);
  const qm=makeQimaiZM({n:80,w:96,d:30,h:0.8,seed:1975}); qm.g.position.set(0,-1.3,-26); g.add(qm.g);
  const zhu1=makeZhuZM({n:7,h:7,seed:1977}); zhu1.position.set(-19,-1.3,-16); g.add(zhu1);
  const zhu2=makeZhuZM({n:5,h:5.6,seed:1979}); zhu2.position.set(17,-1.3,-20); g.add(zhu2);
  const rain=makeGlow({n:180,box:[180,28,90],pos:[0,15,-16],color:0x9fb2c8,size:3.2,speed:0.5,rise:1,maxA:0.24,add:false});
  g.add(rain.points);
  const motes=makeGlow({n:40,box:[200,26,110],pos:[0,8,-40],color:0x9fb2c6,size:6,speed:0.05,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:9,spread:[250,22,150],pos:[0,8,-56],scale:80,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:13,d:7,color:0x0b0f15,seed:1981,sway:0.85,tip:0x2c3a44});
  fg.g.position.set(-8,-1.4,24); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:3,r:4.0,w:18,d:7,color:0x080b10,seed:1983,rim:0.14});
  rk.g.position.set(16,-1.5,18); g.add(rk.g);
  addLights(g,{c:0x93a8c2,i:0.32,p:[-40,70,30]},{c:0x232e3c,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rain.update(t); motes.update(t); mist.update(t,k);
    fg.update(t,k); rk.update(t,k); qm.update(t,k);
  }};
}
function bMingduZM(){ // 壹 · 名都荠麦 —— 解鞍少驻：竹西亭畔鞍马静立，春风十里长街尽荠麦青青
  const g=new THREE.Group();
  const grd=makeGround({r:52,c1:0x0c1016,c2:0x131a22}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:16,layers:2,peaks:4,seed:1985,color:0x0a0e14,atmo:0x36445a,fogK:0.62,glowK:0.05,y:-10});
  ridge.g.position.set(0,0,10); g.add(ridge.g);
  /* 名都城郭远影（80 单位外，雾遮蔽约 0.60 = 背景层上限内） */
  const wall=makeWallZM({w:80,h:6,seed:1987}); wall.position.set(0,0,-58); g.add(wall);
  /* 春风十里长街：旧石板道没入荒田 */
  const lane=new THREE.Mesh(new THREE.BoxGeometry(3.4,0.10,64),
    new THREE.MeshPhongMaterial({color:0x10151c,shininess:8,specular:0x242e3a}));
  lane.position.set(0.8,0.02,-30); g.add(lane);
  /* 尽荠麦青青：长街两侧与街心漫生野荠 */
  const qm=makeQimaiZM({n:110,w:34,d:44,h:1.0,seed:1989}); qm.g.position.set(0,0,-14); g.add(qm.g);
  const qm2=makeQimaiZM({n:26,w:20,d:8,h:0.7,seed:1991}); qm2.g.position.set(0,0,2); g.add(qm2.g);
  /* 竹西佳处：竹西亭 + 修竹 */
  const ting=makeTingZM(); ting.position.set(-8.5,0,-14); ting.rotation.y=0.5; g.add(ting);
  const zhu1=makeZhuZM({n:8,h:7.5,seed:1993}); zhu1.position.set(-13,0,-10); g.add(zhu1);
  const zhu2=makeZhuZM({n:6,h:6.2,seed:1995}); zhu2.position.set(-16,0,-14); g.add(zhu2);
  const zhu3=makeZhuZM({n:5,h:5.8,seed:1997}); zhu3.position.set(8,0,-18); g.add(zhu3);
  /* 解鞍少驻：词人立，鞍鞯置于地，马低头食荠 */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.24,rim:0.62,rimC:0x8f9fc9});
  poet.position.set(-2.2,0,-4.6); poet.rotation.y=2.75; g.add(poet);
  const saddle=new THREE.Mesh(new THREE.BoxGeometry(0.9,0.2,0.62),
    new THREE.MeshPhongMaterial({color:0x3a2f28,shininess:6,specular:0x2a221c}));
  saddle.position.set(-3.4,0.12,-5.7); saddle.rotation.set(0,0.5,0.12); g.add(saddle);
  const horse=makeHorseZM({scale:1.5}); horse.position.set(-4.8,0,-7.0); horse.rotation.y=1.3; g.add(horse);
  /* 烟雨迷蒙 + 青野雾光 */
  const rain=makeGlow({n:170,box:[170,26,90],pos:[0,14,-14],color:0x9fb2c8,size:3.2,speed:0.5,rise:1,maxA:0.26,add:false});
  g.add(rain.points);
  const motes=makeGlow({n:40,box:[140,18,60],pos:[0,7,-30],color:0x9fb2c6,size:6,speed:0.05,rise:0,maxA:0.16});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[220,16,100],pos:[0,7,-46],scale:70,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:36,n:12,d:6,color:0x0b0f15,seed:1999,sway:0.9,tip:0x2c3a44});
  fg.g.position.set(-12,-0.2,11); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x080b10,seed:2001,rim:0.13});
  rk.g.position.set(14,-0.6,8); g.add(rk.g);
  addLights(g,{c:0x93a8c2,i:0.34,p:[-40,70,20]},{c:0x202b38,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rain.update(t); motes.update(t); mist.update(t,k);
    fg.update(t,k); rk.update(t,k); poet.update(t,k);
    qm.update(t,k); qm2.update(t,k);
  }};
}
function bKongchengZM(){ // 贰 · 空城清角 —— 废池乔木犹厌言兵；渐黄昏，清角吹寒，都在空城
  const g=new THREE.Group();
  const grd=makeGround({r:50,c1:0x0b0e13,c2:0x121721}); g.add(grd.mesh);
  const ridge=makeRange({r:230,h:18,layers:2,peaks:4,seed:2003,color:0x090d13,atmo:0x33404e,fogK:0.60,glowK:0.05,y:-11});
  ridge.g.position.set(0,0,4); g.add(ridge.g);
  /* 空城残垣：主墙带豁口碎砖 + 侧墙 */
  const wall=makeWallZM({w:50,h:7.6,seed:2005,breach:0.42}); wall.position.set(2,0,-24); wall.rotation.y=0.06; g.add(wall);
  const wall2=makeWallZM({w:26,h:6.4,seed:2007}); wall2.position.set(18,0,-30); wall2.rotation.y=-0.5; g.add(wall2);
  /* 谯楼（角声来处） */
  const tower=makeJiaoLouZM(); tower.position.set(-17,0,-26); tower.rotation.y=0.5; g.add(tower);
  /* 废池乔木：枯木三株 + 一汪死水废池 */
  const tr1=makeDeadTreeZM({h:8.5,seed:2009}); tr1.position.set(-6,0,-13); g.add(tr1);
  const tr2=makeDeadTreeZM({h:7,seed:2011}); tr2.position.set(7.5,0,-16); g.add(tr2);
  const tr3=makeDeadTreeZM({h:9.5,seed:2013}); tr3.position.set(13,0,-23); g.add(tr3);
  const pond=makeWater({size:22,seg:18,amp:0.04,freq:0.13,speed:0.2,flow:[0,0],
    deep:0x0a1119,shallow:0x0f1a26,skyc:0x18222e,spec:0.7,y:-0.12});
  pond.mesh.position.set(3,-0.12,-9); g.add(pond.mesh);
  const RB=new GeoBag();
  for(let i=0;i<6;i++){
    const a=i/6*6.283+0.4, rr=11.4+(i%2)*0.5;
    const rk=new THREE.SphereGeometry(0.5+(i%3)*0.18,6,5); rk.scale(1.2,0.55,1);
    rk.translate(3+Math.cos(a)*rr,-0.15,-9+Math.sin(a)*rr*0.8);
    RB.put(rk,0x10141b);
  }
  g.add(RB.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x28303e,emissive:0x03050a}),{c:0x7288a0,i:0.15,p:2.6})));
  /* 城中信步的词人（背影，走向空城深处） */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.2,rim:0.58,rimC:0x8f9fc9});
  poet.position.set(3.8,0,-3.2); poet.rotation.y=Math.PI+0.45; g.add(poet);
  /* 清角吹寒：寒纹自角楼一圈圈漫过空城（死城唯一的"声音"） */
  const jiao=makeHanjiaoZM({size:82}); jiao.g.position.set(-17,6.5,-26); g.add(jiao.g);
  /* 黄昏冷尘 + 贴地湿雾 */
  const motes=makeGlow({n:50,box:[150,16,70],pos:[0,6,-24],color:0x8fa4bc,size:5,speed:0.04,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,18,110],pos:[0,6.5,-44],scale:76,color:0x8298b0,op:0.11});
  g.add(mist.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:18,d:7,color:0x080b10,seed:2015,rim:0.13});
  rk.g.position.set(-13,-0.8,10); g.add(rk.g);
  const fg=makeForeground({kind:'芦苇',w:26,n:10,d:5,color:0x080b10,seed:2017,sway:0.8,tip:0x26323c});
  fg.g.position.set(14,-0.6,9); g.add(fg.g);
  addLights(g,{c:0x8497ae,i:0.26,p:[-30,60,-10]},{c:0x1c2430,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); pond.update(t); motes.update(t); mist.update(t,k);
    poet.update(t,k); rk.update(t,k); fg.update(t,k); jiao.update(t,k);
  }};
}
function bDulangZM(){ // 叁 · 杜郎须惊 —— 俊赏重到亦须惊：昔日繁华化作雾中幻影，须臾明灭
  const g=new THREE.Group();
  const grd=makeGround({r:52,c1:0x0c0f15,c2:0x121820}); g.add(grd.mesh);
  const ridge=makeRange({r:240,h:16,layers:2,peaks:4,seed:2019,color:0x090d14,atmo:0x36445a,fogK:0.62,glowK:0.05,y:-11});
  ridge.g.position.set(0,0,8); g.add(ridge.g);
  /* 幻影繁华：旧日楼阁画桥的虚像（豆蔻梢头二点藕荷） */
  const ph=makePhantomZM(); ph.g.position.set(0,0,-22); g.add(ph.g);
  const dots=makeGlow({n:44,box:[30,8,16],pos:[0,3.5,-22],color:0xd8a7b1,size:5,speed:0.05,rise:0,maxA:0.2});
  g.add(dots.points);
  /* 空城地面残荠 */
  const qm=makeQimaiZM({n:26,w:26,d:12,h:0.7,seed:2021}); qm.g.position.set(0,0,-9); g.add(qm.g);
  /* 伫立的词人（面向幻影） */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.26,rim:0.6,rimC:0x8f9fc9});
  poet.position.set(-1.8,0,-2.4); poet.rotation.y=Math.PI-0.3; g.add(poet);
  const motes=makeGlow({n:44,box:[150,18,70],pos:[0,7,-28],color:0x9fb2c6,size:5.5,speed:0.04,rise:0,maxA:0.15});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[230,16,110],pos:[0,6.5,-44],scale:74,color:0x8298b0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:40,n:12,d:6,color:0x0b0f15,seed:2023,sway:0.85,tip:0x2c3a44});
  fg.g.position.set(-11,-0.4,12); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.4,w:15,d:6,color:0x080b10,seed:2025,rim:0.13});
  rk.g.position.set(13,-0.7,9); g.add(rk.g);
  addLights(g,{c:0x8ba1ba,i:0.28,p:[-30,70,-20]},{c:0x1e2834,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); motes.update(t); mist.update(t,k);
    poet.update(t,k); fg.update(t,k); rk.update(t,k); ph.update(t,k); dots.update(t); qm.update(t,k);
  }};
}
function bLengyueZM(){ // 肆（末境·可点击）· 冷月无声（词眼）—— 二十四桥仍在，波心荡，冷月无声；红药一丛桥边自开
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const water=makeWater({size:700,seg:96,amp:0.30,freq:0.09,speed:0.42,flow:[0,0.3],
    deep:0x0a1220,shallow:0x14263a,skyc:0x1c2938,spec:1.25,moonDir:[0.16,0.14,-0.97],y:-1.7});
  g.add(water.mesh);
  const bank=new THREE.Mesh(new THREE.BoxGeometry(30,1.1,26),
    new THREE.MeshPhongMaterial({color:0x0f141b,shininess:6,specular:0x222c38}));
  bank.position.set(0,-0.55,0); g.add(bank);
  const soil=makeGround({r:17,c1:0x0c0f15,c2:0x121823});
  soil.mesh.position.set(0,0.02,0); g.add(soil.mesh);
  const far=makeGround({r:36,c1:0x0b0e14,c2:0x11171f});
  far.mesh.position.set(2,-0.35,-40); g.add(far.mesh);
  const ridge=makeRange({r:280,h:14,layers:2,peaks:3,seed:2027,color:0x090d14,atmo:0x36445a,fogK:0.62,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,-6); g.add(ridge.g);
  /* 空城远影（对岸城郭一角） */
  const wall=makeWallZM({w:44,h:6.2,seed:2029,breach:0.35}); wall.position.set(13,0,-42); wall.rotation.y=-0.2; g.add(wall);
  const tower=makeJiaoLouZM(); tower.position.set(26,0,-45); tower.scale.setScalar(0.8); g.add(tower);
  /* 二十四桥仍在：低拱长桥卧波（拱跨沿 x，自岸边没入烟波；24 望柱） */
  const bridge=makeQiaoZM({span:18}); bridge.position.set(-3.5,-1.85,-18); g.add(bridge);
  /* 波心冷月：天上无月，月影沉在波心（桥拱框月） */
  const moon=makeShuiYueZM({r:5.2}); moon.g.position.set(-3.5,-1.62,-16.6); g.add(moon.g);
  /* 桥边红药：全页唯一暖红，一丛自开 */
  const hy1=makeHongyaoZM({n:3,scale:1.15}); hy1.position.set(6.2,0,-8.6); g.add(hy1);
  const hy2=makeHongyaoZM({n:2,scale:0.9}); hy2.position.set(7.8,0,-10); g.add(hy2);
  /* 岸畔残荠 */
  const qm=makeQimaiZM({n:36,w:16,d:7,h:0.8,seed:2031}); qm.g.position.set(-2,0,-9.5); g.add(qm.g);
  const qm2=makeQimaiZM({n:20,w:9,d:5,h:0.7,seed:2033}); qm2.g.position.set(6,0,-11.5); g.add(qm2.g);
  /* 立于岸边的词人（背影望桥月） */
  const poet=makeFigure({pose:'独立',robe:0x232b38,belt:0x37414f,hat:'幞头',beard:true,scale:1.26,rim:0.6,rimC:0x8f9fc9});
  poet.position.set(-2.8,0,-3.4); poet.rotation.y=Math.PI+0.15; g.add(poet);
  /* 点击后：荠麦青青漫城（青雾漫过桥面城郭） */
  const green=makeFlow({n:300,box:[150,9,54],pos:[0,1.6,-18],color:0x47705c,size:16,speed:3.5,maxA:0});
  g.add(green.points);
  const burst=makeBurst({n:50,color:0xbcd4ee,pos:[-3.5,-1.2,-16.6]}); g.add(burst.points);
  const motes=makeGlow({n:40,box:[160,16,80],pos:[0,6,-30],color:0x9fb2c6,size:5,speed:0.04,rise:0,maxA:0.14});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,16,110],pos:[0,7,-46],scale:76,color:0x8298b0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:12,d:6,color:0x0b0f15,seed:2035,sway:0.75,tip:0x26323c});
  fg.g.position.set(0,-1.6,14); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:3.8,w:16,d:7,color:0x080b10,seed:2037,rim:0.13});
  rk.g.position.set(-14,-1.6,11); g.add(rk.g);
  addLights(g,{c:0x9db0cc,i:0.3,p:[20,40,-60]},{c:0x1a2530,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/3.0);
      water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k);
      poet.update(t,k); fg.update(t,k); rk.update(t,k);
      qm.update(t,k); qm2.update(t,k); burst.update(t);
      moon.update(t,k,ctl.ext);
      green.mat.uniforms.uMaxA.value=k*(0.02+0.26*ctl.ext);
      green.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(0,0.05,0.12); pluck(2,0.5,0.11); pluck(4,1.0,0.12); pluck(5,1.5,0.09);
        const fl=$('#flash'); fl.textContent='波心荡，冷月无声'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0a1220),hor:C(0x1d2937),bot:C(0x090d13),fog:C(0x151d26),fd:0.013,star:0.10,
  moon:new THREE.Vector3(0,-200,-160),ms:0.001,mph:0,mhaze:0,dirC:C(0x9db4cc),dirI:0.34,
  dirP:new THREE.Vector3(50,110,40),ambC:C(0x26313f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCoverZM,
  cam:{f:[0,11,48],t:[0,11.5,44],lf:[0,10,-26],lt:[0,10.5,-30]},
  sky:()=>SK({top:C(0x0e141e),hor:C(0x242e3a),bot:C(0x0b0f15),fog:C(0x141c26),fd:0.013,star:0.08,
    dirC:C(0x93a8c2),dirI:0.32,ambC:C(0x232e3c),ambI:0.64}) },
{ name:'名都荠麦',dwell:19,river:0.02,build:bMingduZM,
  cam:{f:[0,5.8,20],t:[1.2,5.5,17],lf:[1,4.2,-8],lt:[2,4,-10]},
  sky:()=>SK({top:C(0x10161f),hor:C(0x2a3140),bot:C(0x0c0f14),fog:C(0x161c26),fd:0.012,star:0.03,
    dirC:C(0x8fa4c4),dirI:0.34,ambC:C(0x202b38),ambI:0.66}) },
{ name:'空城清角',dwell:18,river:0.018,build:bKongchengZM,
  cam:{f:[0,6.4,22],t:[0,6,19],lf:[-2,4.6,-14],lt:[-3,4.4,-16]},
  sky:()=>SK({top:C(0x0a0e16),hor:C(0x2b2833),bot:C(0x090c11),fog:C(0x141924),fd:0.016,star:0.04,
    dirC:C(0x8497ae),dirI:0.22,ambC:C(0x1c2430),ambI:0.6}) },
{ name:'杜郎须惊',dwell:17,river:0.02,build:bDulangZM,
  cam:{f:[1.2,6,20],t:[0.6,5.6,17],lf:[0,5,-18],lt:[0,5,-20]},
  sky:()=>SK({top:C(0x0a0f18),hor:C(0x1c2431),bot:C(0x090c11),fog:C(0x131a24),fd:0.014,star:0.06,
    dirC:C(0x8ba1ba),dirI:0.26,ambC:C(0x1e2834),ambI:0.6}) },
{ name:'冷月无声',dwell:20,river:0.026,build:bLengyueZM,
  cam:{f:[0,6.2,21],t:[0,5.8,18],lf:[-1,3.4,-13],lt:[-1.5,3.2,-15]},
  sky:()=>SK({top:C(0x080d15),hor:C(0x1a222e),bot:C(0x080b10),fog:C(0x121922),fd:0.012,star:0.08,
    dirC:C(0x9db0cc),dirI:0.3,dirP:new THREE.Vector3(20,36,-60),ambC:C(0x1a2530),ambI:0.6}) },
];
"""
