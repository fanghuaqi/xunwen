# -*- coding: utf-8 -*-
"""wangdongtinghu-zhang.py —— 《望洞庭湖赠张丞相》（唐·孟浩然，queue no.216，大漠金戈）生成配置
美术立意：大漠金戈色板移用于八月秋水大湖（底色 #120d08、雾 #1a120a 系、accent=#b8905a 取自 queue），
苍茫大气的暮色洞庭：湖面反射暗赭天光，accent 只落在人形边缘光/城垣轮廓/前景 rim 上，禁艳金。
四境情感线：前二联壮景（动）——浩阔静水 → 蒸泽撼城的雄浑动势；后二联转忱（静）——无舟楫的苦闷 → 羡鱼情的含蓄。
标志性瞬间（境贰·全诗名联）：气蒸云梦泽——三柱水汽自湖面蒸腾（自写竖向蒸汽着色器）+
波撼岳阳城——巨浪高幅拍打临湖城墙、城墙微颤、墙脚浪花四溅。
末境点击（queue interact）：点击波撼岳阳城——浪涌撼城（浪高 amp 0.7→2.5 渐涨）+ 水汽蒸腾大盛，
「羡鱼情」如湖水涌动。干谒之忱全藏在壮景的分寸里。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=4, slug='wangdongtinghu-zhang', title='望洞庭湖赠张丞相', dyn='唐 · 孟浩然', brand_author='孟 浩 然',
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
    tip='轻点画面 / 按空格 —— 浪涌撼城，水汽蒸腾',
    hint='← → 键或空格逐境游览 · 末境可点击画面：浪涌撼城、水汽蒸腾，看「羡鱼情」如湖水涌动',
    cover_read='望洞庭湖赠张丞相。唐，孟浩然。八月湖水平，涵虚混太清。气蒸云梦泽，波撼岳阳城。欲济无舟楫，端居耻圣明。坐观垂钓者，空有羡鱼情。',
    cover_p1='四重意境，随诗句次第展开：八月湖水盛涨与岸齐平、水天含混一色的浩阔；水汽蒸腾、巨浪撼动岳阳城的雄浑动势；欲渡无舟楫、盛世闲居有愧的转忱；末了坐观垂钓者、空有羡鱼情的含蓄求荐。',
    cover_p2='边读诗，边走进孟浩然笔下的洞庭秋水：前两联壮景愈是波澜浩大，后两联的求仕之忱愈见分寸——读懂这条「壮景写忱」的暗线，就读懂了这首干谒名作的气度。',
    end_h2='波撼城 · 羡鱼情', cn_word='四',
    words_js="['再游一次八月湖','初识襄阳，尚需共读','渐入诗境，再诵几遍','湖光渐阔，气象渐开','已解蒸泽撼城意','欲济有望，羡鱼成真']",
    sky_atmo='0x2e2114',
)

POEM_JS = """const POEM = [
{ name:'秋水涵虚', jing:'八月湖水盛涨与岸齐平，水天含混、上下浑然一体 —— 大湖秋水，涵容天地。（秋水 · 天光）',
  segs:[
   {c:'八月湖水平，', p:py('bā yuè hú shuǐ píng')},
   {c:'涵虚混太清。', p:py('hán xū hùn tài qīng')}],
  read:'八月湖水平，涵虚混太清。',
  yisi:'八月洞庭湖水盛涨与岸齐平，水天含混相接，浑然一体。——起笔即见浩阔：「平」字写出秋汛时节湖水漫岸的浩渺水势，「混」字把湖水与天空搅成一色，一片水光涵容万物，气象全出。',
  zhu:[['八月湖水平','八月（秋汛时节）湖水上涨，与岸齐平。点明时令，也铺开全诗浩阔的底色'],['涵虚','包含天空，指水面倒映天光、水汽空濛。涵，包含；虚，天空'],['混太清','与天空混为一体。太清，天空——「涵虚」「混太清」互文见义，写尽水天一色'],['张丞相','指张九龄，时任丞相。这是一首「干谒诗」：投赠当政者，陈情求荐']] },
{ name:'蒸泽撼城', jing:'水汽蒸腾而上，巨浪撼动城郭 —— 洞庭名联，雄浑动势扑面。（水汽 · 巨浪 · 城）（标志性瞬间）',
  segs:[
   {c:'气蒸云梦泽，', p:py('qì zhēng yún mèng zé')},
   {c:'波撼岳阳城。', p:py('bō hàn yuè yáng chéng')}],
  read:'气蒸云梦泽，波撼岳阳城。',
  yisi:'云梦二泽水汽蒸腾、白白茫茫，波涛汹涌，仿佛把岳阳城都撼动了。——千古名联在此：「蒸」字写出水汽自湖面升腾的动势，虚处传神；「撼」字写出巨浪拍城的力度，实处惊天。一上一下、一虚一实，洞庭的雄浑气象扑面而来。',
  zhu:[['气蒸','湖面水汽蒸腾而上——「蒸」字把静水写活，是虚写'],['云梦泽','古代两大湖泊：云泽在江北，梦泽在江南，后大部淤为陆地，此指洞庭湖一带浩渺水域'],['波撼','波涛激荡摇撼——「撼」字有千钧之力，是实写的夸张'],['岳阳城','今湖南岳阳，在洞庭湖东岸。此联被誉为写洞庭的千古绝唱']] },
{ name:'欲济无楫', jing:'想渡湖却没有舟楫，盛世闲居心自有愧 —— 壮景之下，转出求仕之忱。（无楫 · 有愧）',
  segs:[
   {c:'欲济无舟楫，', p:py('yù jì wú zhōu jí')},
   {c:'端居耻圣明。', p:py('duān jū chǐ shèng míng')}],
  read:'欲济无舟楫，端居耻圣明。',
  yisi:'想要渡过湖去，却没有船和桨；圣明时代闲居无事，坐食俸禄，于心有愧。——笔锋陡转：壮阔湖水忽然化作仕途的隐喻，「无舟楫」是无人引荐、报国无门的苦闷，「耻圣明」是生逢盛世却不甘闲居的焦灼，前一联的波澜至此都有了着落。',
  zhu:[['欲济','想要渡水。济，渡——渡湖暗喻入仕、寻求进身之路'],['舟楫','船和桨，暗喻实现抱负的手段与引荐之人'],['端居','平居，闲居无所事事'],['耻圣明','有愧于圣明之世。圣明，指太平盛世、圣明的朝廷——盛世闲居，于心不安']] },
{ name:'坐观羡鱼', jing:'坐看他人垂钓，空自羡慕得鱼 —— 末境点击画面：浪涌撼城、水汽蒸腾，看「羡鱼情」如湖水涌动。（垂钓 · 羡鱼 · 点击画面）',
  segs:[
   {c:'坐观垂钓者，', p:py('zuò guān chuí diào zhě')},
   {c:'空有羡鱼情。', p:py('kōng yǒu xiàn yú qíng')}],
  read:'坐观垂钓者，空有羡鱼情。',
  yisi:'闲坐观看别人临河垂钓，只能白白地生羡慕之情。——以「垂钓者」暗指在朝执政的张丞相，以「羡鱼」自比求仕不得：话说得极含蓄得体，求荐之心却灼然可见——这就是干谒诗最漂亮的分寸。',
  zhu:[['坐观','坐看，旁观'],['垂钓者','钓鱼的人，暗指执政者（张丞相），「垂钓」亦含在朝执政之意'],['空有','徒然怀有'],['羡鱼情','羡鱼而不得鱼的怅望之情。《淮南子·说林训》「临河而羡鱼，不如归家织网」——言外之意：希望对方「结网」援引，使自己得以渡湖出仕']] },
];
const CN = ['壹','贰','叁','肆'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「八月湖水平」的下一句是？', o:['涵虚混太清','气蒸云梦泽','波撼岳阳城'], a:0},
 {q:'「气蒸云梦泽」的下一句是？', o:['端居耻圣明','波撼岳阳城','涵虚混太清'], a:1},
 {q:'「涵虚混太清」的「涵虚」与「欲济无舟楫」的「楫」，读音和意思正确的是？', o:['涵虚指天空倒映水中、水汽空濛，水天混为一体；楫读 jí，指船桨','涵虚指涵养虚心、静坐养性；楫读 jī，指一座小岛','涵虚指湖水幽深不见底；楫读 yì，指船帆'], a:0},
 {q:'这是一首干谒诗。关于「赠张丞相」与「羡鱼」的典故，下列说法正确的是？', o:['「张丞相」即张九龄；「羡鱼」用《淮南子》「临河而羡鱼，不如归家织网」，孟浩然以「无舟楫」「羡鱼」自比，望张丞相引荐提携','「张丞相」即张说；「羡鱼」指诗人真的想吃洞庭湖的鱼，希望张丞相设宴款待','「张丞相」即张九龄；「羡鱼」典出《论语》，表达诗人退隐江湖、不再求仕的决心'], a:0},
 {q:'前两联极写洞庭的壮阔动势，后两联却转到「无舟楫」「羡鱼情」——全诗的主旨是？', o:['纯粹赞美八月洞庭秋水的壮美风光，并无别的寄托','抒写归隐洞庭、渔钓终老的闲适志趣','壮景写忱：以「欲济无舟楫」自比无人引荐，以「羡鱼情」含蓄表达出仕从政的愿望，希望张丞相援引'], a:2},
];
"""

SCENES_JS = """/* ================= 望洞庭湖赠张丞相 · 四境场景（大漠金戈·秋水大湖：秋水涵虚、蒸泽撼城、欲济无楫、坐观羡鱼） =================
   美术立意：大漠金戈色板移用于八月暮色洞庭——底色 #120d08、雾 #1a120a 系、accent=#b8905a（取自 queue，
   用于人形边缘光/城垣轮廓/前景 rim），禁艳金。前二联壮景（动）：浩阔静水 → 蒸泽撼城的雄浑动势；
   后二联转忱（静）：无舟楫的空舟 → 坐观羡鱼的含蓄。湖面巨浪撼城是全页最重要的水面表现。
   标志性瞬间（境贰·全诗名联）：气蒸云梦泽（自写竖向蒸汽着色器，三柱水汽自湖面升腾）+ 波撼岳阳城
   （巨浪 amp 2.0 拍打临湖城墙、城墙随浪微颤、墙脚浪花四溅）。
   末境点击（queue interact）：浪涌撼城（amp 0.7→2.5 渐涨）+ 水汽蒸腾大盛——「羡鱼情」如湖水涌动。 */

/* —— 蒸汽：竖向水汽柱（自写着色器：向上翻卷 + 底浓顶淡；uFade 每帧显式 ×k，不进 fogShaders）—— */
const WDT_STEAM_VERT=`
uniform float uTime; uniform float uSway;
varying vec2 vUv;
void main(){
  vUv=uv;
  vec3 p=position;
  p.x+=sin(uv.y*4.0+uTime*0.55+uSway)*2.2*uv.y;
  p.x+=sin(uTime*0.35+uSway*2.0)*1.2;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const WDT_STEAM_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; uniform float uMaxA; uniform vec3 uColor;
varying vec2 vUv;
void main(){
  float vert=smoothstep(0.0,0.18,vUv.y)*smoothstep(1.0,0.55,vUv.y);
  float side=smoothstep(0.0,0.30,vUv.x)*smoothstep(1.0,0.70,vUv.x);
  float up=0.62+0.38*sin(vUv.y*26.0-uTime*1.35+vUv.x*9.0);
  float up2=0.85+0.15*sin(vUv.y*61.0-uTime*2.3+4.7);
  gl_FragColor=vec4(uColor,uFade*uK*uMaxA*vert*side*up*up2);
}`;
function makeZhengqi(o){
  o=o||{};
  const g=new THREE.Group(), parts=[];
  const cols=o.cols===undefined?[[6,0,-30,26,46],[-12,0,-42,24,42],[16,0,-50,22,38]]:o.cols;
  cols.forEach(function(c,i){
    const geo=new THREE.PlaneGeometry(c[3],c[4],1,1);
    const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
      uniforms:{uTime:{value:i*1.7},uFade:{value:1},uK:{value:o.k===undefined?0.55:o.k},
        uMaxA:{value:(o.maxA===undefined?0.34:o.maxA)*(1-0.12*i)},
        uColor:{value:C(o.color===undefined?0x9a8468:o.color)},uSway:{value:i*2.1}},
      vertexShader:WDT_STEAM_VERT,fragmentShader:WDT_STEAM_FRAG});
    const mesh=new THREE.Mesh(geo,m); mesh.frustumCulled=false; mesh.renderOrder=3;
    mesh.position.set(c[0],c[4]*0.5-3,c[2]);
    g.add(mesh); parts.push(m);
  });
  return {g,update(t,k){ for(let i=0;i<parts.length;i++){parts[i].uniforms.uTime.value=t+i*1.7; parts[i].uniforms.uFade.value=k;} },
    setK(v){ for(let i=0;i<parts.length;i++)parts[i].uniforms.uK.value=v; }};
}

/* —— 岳阳城：临湖城墙+敌台+垛口+中央门楼双重飞檐（合批 1 mesh，大漠金戈的城垣剪影）——「波撼岳阳城」的城 —— */
function makeYueyang(o){
  o=o||{};
  const w=o.w===undefined?20:o.w, hh=o.h===undefined?3.8:o.h, d=o.d===undefined?2.6:o.d;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,hh,d); wall.translate(0,hh/2,0); B.put(wall,0x191108);
  const merN=Math.floor(w/1.8);
  for(let i=0;i<merN;i++){
    const mx=-w/2+0.9+i*1.8;
    const mer=new THREE.BoxGeometry(0.9,0.8,0.9); mer.translate(mx,hh+0.4,-d*0.2); B.put(mer,0x150e08);
  }
  [-w/2+1.6,w/2-1.6].forEach(function(x){
    const t=new THREE.BoxGeometry(3.2,hh+1.8,3.8); t.translate(x,(hh+1.8)/2,0.2); B.put(t,0x17100a);
    const tc=new THREE.BoxGeometry(3.6,0.5,4.2); tc.translate(x,hh+2.0,0.2); B.put(tc,0x130d08);
  });
  const gate=new THREE.BoxGeometry(5.4,hh+2.2,4.4); gate.translate(0,(hh+2.2)/2,0.4); B.put(gate,0x181109);
  const door=new THREE.BoxGeometry(1.7,2.4,0.5); door.translate(0,1.2,d/2+0.42); B.put(door,0x060403);
  const hall=new THREE.BoxGeometry(4.0,1.7,3.0); hall.translate(0,hh+3.05,0.4); B.put(hall,0x1c130b);
  const r1=new THREE.ConeGeometry(3.3,1.1,4); r1.rotateY(Math.PI/4); r1.translate(0,hh+4.45,0.4); B.put(r1,0x120c07);
  const r2=new THREE.ConeGeometry(2.3,0.9,4); r2.rotateY(Math.PI/4); r2.translate(0,hh+5.4,0.4); B.put(r2,0x0f0a06);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x2a1d10,emissive:0x050302}),{c:0xb8905a,i:o.rim===undefined?0.13:o.rim,p:2.8})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* —— 湖礁：湖水浸过的礁石一丛（合批 1 mesh，供人物立足）—— */
function makeLakeRock(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?21600:o.seed);
  const n=o.n===undefined?4:o.n, r0=o.r===undefined?3.0:o.r;
  for(let i=0;i<n;i++){
    const rg=rockGeo(r0*(0.5+0.8*R()),1,R);
    rg.scale(1,0.55+0.35*R(),1);
    rg.translate((R()-0.5)*(o.w===undefined?6:o.w),R()*0.35-0.2,(R()-0.5)*(o.d===undefined?3.5:o.d));
    B.put(rg,shadeColor(0x0d0906,0.8+0.5*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a1d10,emissive:0x040302}),{c:o.rimC===undefined?0xb8905a:o.rimC,i:0.2,p:2.4})));
  return g;
}

/* —— 空舟：有桨座而无楫的一叶小舟（合批 1 mesh）——「欲济无舟楫」的画眼 —— */
function makeSampan(o){
  o=o||{};
  const L=o.L===undefined?4.6:o.L;
  const B=new GeoBag();
  const bot=new THREE.BoxGeometry(L*0.86,0.2,1.15); bot.translate(0,0.14,0); B.put(bot,0x181009);
  const sideL=new THREE.BoxGeometry(L*0.92,0.46,0.15); sideL.rotateX(0.10); sideL.translate(0,0.46,-0.60); B.put(sideL,0x1c130a);
  const sideR=new THREE.BoxGeometry(L*0.92,0.46,0.15); sideR.rotateX(-0.10); sideR.translate(0,0.46,0.60); B.put(sideR,shadeColor(0x1c130a,1.15));
  const bow=new THREE.BoxGeometry(0.9,0.4,0.8); bow.rotateZ(0.35); bow.translate(L*0.5,0.42,0); B.put(bow,0x1a1108);
  const stern=new THREE.BoxGeometry(0.8,0.42,0.8); stern.rotateZ(-0.38); stern.translate(-L*0.5,0.44,0); B.put(stern,0x1a1108);
  const canopy=new THREE.CylinderGeometry(0.55,0.55,1.5,10);
  canopy.rotateZ(Math.PI/2); canopy.translate(-0.4,0.62,0); B.put(canopy,0x241a10);
  [[0.7,1],[0.7,-1]].forEach(function(p){
    const lock=new THREE.TorusGeometry(0.10,0.035,6,10); lock.rotateX(Math.PI/2); lock.translate(p[0],0.56,p[1]*0.62); B.put(lock,0x3a2a18);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a1d10,emissive:0x040302}),{c:0xb8905a,i:o.rim===undefined?0.12:o.rim,p:2.6})));
  return g;
}

/* —— 钓组：钓竿+入水钓线（limbGeo 两段合批 1 mesh）——「坐观垂钓者」的竿 —— */
function makeDiaogan(hx,hy,hz,tx,ty,tz){
  const B=new GeoBag();
  B.put(limbGeo([hx,hy,hz],[tx,ty,tz],0.04,0.016,6),0x140e08);
  B.put(limbGeo([tx,ty,tz],[tx,0.02,tz],0.006,0.003,4),0x9a8468);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a1d10,emissive:0x030201}),{c:0xb8905a,i:0.18,p:2.6})));
  return g;
}

/* 望湖人/坐观者：全诗贯穿的同一造型（每次 build 新建材质） */
function wdtFigure(scale,pose){
  return makeFigure({pose:pose||'独立',robe:0x2a1e12,belt:0x8a6a44,skin:0xcbb9a2,collar:0x6a5030,
    hair:0x140f0a,hat:'发髻',rimC:0xb8905a,rim:0.5,noProp:true,scale:scale===undefined?1.7:scale});
}

function bCoverWdt(){ // 封面 · 八月暮色洞庭：湖天相接、岳阳城剪影、低月昏黄
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:96,amp:0.7,freq:0.075,speed:0.6,flow:[0.25,0.5],spec:1.5,
    deep:0x100a06,shallow:0x2c1f10,skyc:0x38281a,moonDir:[-0.5,0.18,-1]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xe0c090);
  g.add(water.mesh);
  const ridge=makeRange({r:320,h:14,layers:2,peaks:4,seed:21601,color:0x0b0805,atmo:0x2e2114,fogK:0.62,glowK:0.05,y:-8});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  const city=makeYueyang({scale:1.0,rim:0.12}); city.position.set(-24,-0.4,-64); city.rotation.y=0.4; g.add(city);
  const mist=makeMist({n:8,spread:[300,16,70],pos:[0,7,-84],scale:78,color:0x6a5a44,op:0.12});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[220,22,100],pos:[0,10,-40],color:0xc0a070,size:6,speed:0.05,rise:0,maxA:0.13});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.4,w:16,d:7,color:0x0a0704,seed:21602,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-14,-2.0,18); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:10,d:6,color:0x0a0704,seed:21603,sway:0.8,rim:0.12,rimC:0xb8905a});
  reeds.g.position.set(13,-1.5,16); g.add(reeds.g);
  addLights(g,{c:0xc09860,i:0.38,p:[-40,60,-30]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); motes.update(t);
    fg1.update(t,k); reeds.update(t,k);
  }};
}
function bQiushui(){ // 壹 · 秋水涵虚 —— 八月湖水平，涵虚混太清（大湖秋水，静而浩阔）
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:96,amp:0.5,freq:0.07,speed:0.45,flow:[0.15,0.5],spec:1.15,
    deep:0x0f0a06,shallow:0x32220f,skyc:0x3e2b1a,moonDir:[-0.4,0.2,-1]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xd0b080);
  g.add(water.mesh);
  const ridge=makeRange({r:330,h:9,layers:2,peaks:3,seed:21604,color:0x0a0705,atmo:0x2e2114,fogK:0.66,glowK:0.04,y:-10});
  ridge.g.position.set(0,0,-120); g.add(ridge.g);
  /* 涵虚混太清：天际一带水汽长雾，把湖与天搅成一色 */
  const mist=makeMist({n:9,spread:[320,13,60],pos:[0,5.5,-95],scale:84,color:0x7a6448,op:0.16});
  g.add(mist.g);
  const rock=makeLakeRock({n:5,r:2.8,seed:21605}); rock.position.set(6.5,-0.7,-4); g.add(rock);
  const poet=wdtFigure(2.0,'独立'); poet.position.set(6.5,-0.32,-4); poet.rotation.y=3.1; g.add(poet);
  const motes=makeGlow({n:50,box:[200,20,90],pos:[0,9,-40],color:0xc8a878,size:5.5,speed:0.045,rise:0,maxA:0.13});
  g.add(motes.points);
  const foam=makeGlow({n:90,box:[130,3,50],pos:[0,0.3,-26],color:0xa08860,size:7,speed:0.25,rise:1,maxA:0.14});
  g.add(foam.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.2,w:16,d:7,color:0x0a0704,seed:21606,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-14,-1.8,16); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:10,d:6,color:0x0a0704,seed:21607,sway:0.7,rim:0.12,rimC:0xb8905a});
  reeds.g.position.set(13,-1.3,14); g.add(reeds.g);
  addLights(g,{c:0xc09860,i:0.42,p:[-40,60,-30]},{c:0x33281a,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); mist.update(t,k); motes.update(t); foam.update(t);
    fg1.update(t,k); reeds.update(t,k); poet.update(t,k);
  }};
}
function bZhengze(){ // 贰（标志性瞬间）· 蒸泽撼城 —— 气蒸云梦泽，波撼岳阳城（名联，全诗气骨）
  const g=new THREE.Group();
  const water=makeWater({size:640,seg:96,amp:2.2,freq:0.075,speed:1.05,flow:[0.85,0.5],spec:1.15,
    deep:0x0e0905,shallow:0x2c1e10,skyc:0x2e2114,moonDir:[-0.12,0.16,-1]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x9a7c50);
  g.add(water.mesh);
  const ridge=makeRange({r:340,h:11,layers:2,peaks:4,seed:21608,color:0x090604,atmo:0x2a1d10,fogK:0.64,glowK:0.04,y:-12});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 岳阳城：城墙直抵水线，被巨浪摇撼（update 里随浪微颤） */
  const city=makeYueyang({scale:1.35,rim:0.15}); city.position.set(-24,-0.7,-52); city.rotation.y=0.35; g.add(city);
  /* 浪撼城墙：墙脚浪花四溅 */
  const spray=makeGlow({n:150,box:[34,6.5,10],pos:[-24,2.2,-46],color:0xd8c8a8,size:8,speed:0.7,rise:1,maxA:0.42});
  g.add(spray.points);
  /* 气蒸云梦泽：三柱水汽自湖面蒸腾而上 */
  const steam=makeZhengqi({cols:[[6,0,-30,26,46],[-12,0,-42,24,42],[16,0,-50,22,38]],maxA:0.44,k:0.85,color:0xb09878});
  g.add(steam.g);
  const mist=makeMist({n:8,spread:[300,20,90],pos:[0,7,-80],scale:82,color:0x6a5a44,op:0.13});
  g.add(mist.g);
  /* 临湖望潮人：右前方礁石上，衣袂当风 */
  const rock=makeLakeRock({n:4,r:2.4,seed:21609}); rock.position.set(9,-0.8,-6); g.add(rock);
  const poet=wdtFigure(1.8,'独立'); poet.position.set(9,-0.45,-6); poet.rotation.y=2.8; g.add(poet);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x090604,seed:21610,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-13,-2.2,18); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:20,n:9,d:6,color:0x090604,seed:21611,sway:1.1,rim:0.12,rimC:0xb8905a});
  reeds.g.position.set(13,-1.6,15); g.add(reeds.g);
  addLights(g,{c:0xb08850,i:0.40,p:[-30,55,-25]},{c:0x33281a,i:0.56});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0);
    city.position.y=-0.7+0.09*Math.sin(t*7.3); city.rotation.z=0.012*Math.sin(t*5.1);
    spray.update(t); steam.update(t,k); mist.update(t,k);
    fg1.update(t,k); reeds.update(t,k); poet.update(t,k);
  }};
}
function bYuji(){ // 叁 · 欲济无楫 —— 欲济无舟楫，端居耻圣明（壮景转忱，静）
  const g=new THREE.Group();
  const water=makeWater({size:560,seg:96,amp:0.6,freq:0.075,speed:0.5,flow:[0.2,0.5],spec:1.05,
    deep:0x0d0905,shallow:0x2c1e0f,skyc:0x32241a,moonDir:[-0.4,0.18,-1]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xc0a070);
  g.add(water.mesh);
  const grd=makeGround({r:110,c1:0x0d0906,c2:0x191108});
  grd.mesh.position.set(0,-0.55,12); g.add(grd.mesh);
  const ridge=makeRange({r:320,h:12,layers:2,peaks:4,seed:21612,color:0x0a0705,atmo:0x2a1d10,fogK:0.62,glowK:0.05,y:-10});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 远处岳阳城淡影（回望名联之城） */
  const city=makeYueyang({scale:0.85,rim:0.10}); city.position.set(-28,-0.5,-92); city.rotation.y=-0.3; g.add(city);
  /* 空舟一叶：有桨座而无楫（画眼），系在岸石边随水轻摇 */
  const boat=makeSampan(); boat.position.set(-4.5,0.05,-9); boat.rotation.y=0.5; g.add(boat);
  const rock=makeLakeRock({n:3,r:1.9,seed:21613}); rock.position.set(-8.2,-0.6,-7.6); g.add(rock);
  const poet=wdtFigure(1.85,'独立'); poet.position.set(4.6,-0.3,-3.4); poet.rotation.y=2.5; g.add(poet);
  const mist=makeMist({n:7,spread:[240,18,80],pos:[0,6,-64],scale:76,color:0x6a5a44,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:36,box:[160,18,70],pos:[0,8,-30],color:0xc0a070,size:5,speed:0.04,rise:0,maxA:0.12});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.0,w:14,d:6,color:0x090604,seed:21614,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-13,-2.2,14); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:18,n:9,d:5,color:0x090604,seed:21615,sway:0.6,rim:0.12,rimC:0xb8905a});
  reeds.g.position.set(15.5,-1.8,14.5); g.add(reeds.g);
  addLights(g,{c:0xb08850,i:0.36,p:[-35,55,-20]},{c:0x33281a,i:0.58});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); grd.update(); ridge.update(t,0);
    boat.position.y=0.05+0.07*Math.sin(t*0.9); boat.rotation.z=0.03*Math.sin(t*0.7+1);
    mist.update(t,k); motes.update(t); fg1.update(t,k); reeds.update(t,k); poet.update(t,k);
  }};
}
function bXianyu(){ // 肆（末境可点击）· 坐观羡鱼 —— 坐观垂钓者，空有羡鱼情：点击浪涌撼城+水汽蒸腾
  const ctl={t:0,clicked:false,reveal:0};
  const g=new THREE.Group();
  const water=makeWater({size:620,seg:96,amp:0.85,freq:0.08,speed:0.65,flow:[0.6,0.45],spec:0.95,
    deep:0x0e0905,shallow:0x2a1c0e,skyc:0x342418,moonDir:[-0.25,0.2,-1]});
  water.mesh.material.uniforms.uMoonColor.value=C(0x8f734c);
  g.add(water.mesh);
  const ridge=makeRange({r:330,h:10,layers:2,peaks:4,seed:21616,color:0x0a0705,atmo:0x2e2114,fogK:0.62,glowK:0.05,y:-10});
  ridge.g.position.set(0,0,-105); g.add(ridge.g);
  /* 岳阳城隔湖在望（坐观的方向，亦是名联的回响） */
  const city=makeYueyang({scale:1.15,rim:0.13}); city.position.set(-20,-0.6,-64); city.rotation.y=0.3; g.add(city);
  /* 浪花与水汽：点击后大盛（浪涌撼城 + 水汽蒸腾） */
  const spray=makeGlow({n:120,box:[30,6,9],pos:[-20,1.8,-58],color:0xd8c8a8,size:7,speed:0.55,rise:1,maxA:0.001});
  g.add(spray.points);
  const steam=makeZhengqi({cols:[[2,0,-38,24,42],[-16,0,-52,22,40],[14,0,-56,20,36]],maxA:0.30,k:0.18});
  g.add(steam.g);
  /* 垂钓者：临湖礁上持竿而立，钓竿一线入水 */
  const rock1=makeLakeRock({n:4,r:2.2,seed:21617}); rock1.position.set(-7.5,-0.7,-11); g.add(rock1);
  const angler=wdtFigure(1.6,'独立'); angler.position.set(-7.5,-0.38,-11); angler.rotation.y=2.35; g.add(angler);
  const rod=makeDiaogan(-6.9,0.95,-11.4,-4.9,2.55,-13.4); g.add(rod);
  /* 远渚小礁上又一小影（垂钓者之二） */
  const rock3=makeLakeRock({n:3,r:1.7,seed:21622}); rock3.position.set(14.5,-0.55,-20); g.add(rock3);
  const far=makeCrowd({n:2,rect:[13.5,-21,3.5,3],seed:21618,color:0x16100a,rimC:0xb8905a,rim:0.18,sMin:0.62,sMax:0.70,y:-0.30});
  g.add(far.mesh);
  /* 坐观者：近岸礁石上临湖而立，望着钓者与湖水 */
  const rock2=makeLakeRock({n:4,r:2.3,seed:21619}); rock2.position.set(7.0,-0.65,-5); g.add(rock2);
  const poet=wdtFigure(1.7,'独立'); poet.position.set(7.0,-0.30,-5); poet.rotation.y=2.6; g.add(poet);
  const mist=makeMist({n:7,spread:[260,18,80],pos:[0,6,-70],scale:78,color:0x6a5a44,op:0.11});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[180,20,80],pos:[0,9,-34],color:0xc8a878,size:5.5,speed:0.045,rise:0,maxA:0.12});
  g.add(motes.points);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x0a0704,seed:21620,rim:0.10,rimC:0xb8905a});
  fg1.g.position.set(-13,-1.8,15); g.add(fg1.g);
  const reeds=makeForeground({kind:'芦苇',w:20,n:10,d:6,color:0x0a0704,seed:21621,sway:0.8,rim:0.12,rimC:0xb8905a});
  reeds.g.position.set(14,-1.3,13); g.add(reeds.g);
  addLights(g,{c:0xc09860,i:0.44,p:[-40,60,-30]},{c:0x33281a,i:0.6});
  const pl=new THREE.PointLight(0xd8b070,0.9,70); pl.position.set(-20,4,-58); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/4.2);
      const rv=ctl.reveal, up=rv*rv*(3-2*rv);
      const wm=water.mesh.material.uniforms;
      wm.uAmp.value=0.85+1.75*up;                   // 浪涌撼城：浪高涨起
      wm.uSpeed.value=0.65+0.55*up;
      spray.mat.uniforms.uMaxA.value=0.001+0.44*up; // 城墙脚下浪花四溅
      steam.setK(0.18+0.62*up);                     // 水汽蒸腾大盛
      city.position.y=-0.6+0.10*up*Math.sin(t*7.3); // 撼城微颤随之而来
      pl.intensity=k*0.9*up*(0.82+0.18*Math.sin(t*6.1));
      water.update(t); ridge.update(t,0);
      spray.update(t); steam.update(t,k); mist.update(t,k); motes.update(t);
      fg1.update(t,k); reeds.update(t,k); poet.update(t,k); angler.update(t,k); far.update(t);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        setAmbience(0.45);                          // 湖声渐起
        pluck(0,0.0,0.10); pluck(2,0.45,0.09); pluck(4,0.95,0.08);
        const fl=$('#flash'); fl.textContent='空有羡鱼情'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x120d08),hor:C(0x3a2a18),bot:C(0x0c0805),fog:C(0x1a120a),fd:0.0055,star:0.16,
  moon:new THREE.Vector3(-75,24,-190),ms:0.42,mph:0,mhaze:0.12,dirC:C(0xc09860),dirI:0.4,
  dirP:new THREE.Vector3(-50,60,-20),ambC:C(0x33281a),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverWdt,
  cam:{f:[0,10,64],t:[0,9.5,56],lf:[0,9,-40],lt:[0,9.5,-52]},
  sky:()=>SK({top:C(0x130e09),hor:C(0x342414),bot:C(0x0b0805),fog:C(0x191108),fd:0.0050,star:0.14,
    ms:0.42,mhaze:0.12,moon:new THREE.Vector3(-75,22,-195),dirI:0.38}) },
{ name:'秋水涵虚',dwell:17,river:0.03,build:bQiushui,
  cam:{f:[0,7,30],t:[-1,7.3,26],lf:[0,10,-60],lt:[2,10.5,-80]},
  sky:()=>SK({top:C(0x110c08),hor:C(0x3a2a18),bot:C(0x0b0805),fog:C(0x1a120a),fd:0.0052,star:0.12,
    ms:0.40,mhaze:0.14,moon:new THREE.Vector3(-80,20,-195),dirC:C(0xc09860),dirI:0.38,ambI:0.6}) },
{ name:'蒸泽撼城',dwell:19,river:0.05,build:bZhengze,
  cam:{f:[0,6.2,30],t:[-1.5,7.4,27],lf:[-4,8,-40],lt:[-6,9,-56]},
  sky:()=>SK({top:C(0x0e0a07),hor:C(0x2c1f12),bot:C(0x090604),fog:C(0x180f08),fd:0.0058,star:0.06,
    ms:0.001,moon:new THREE.Vector3(0,-80,-190),dirC:C(0xb08850),dirI:0.32,ambI:0.56}) },
{ name:'欲济无楫',dwell:17,river:0.02,build:bYuji,
  cam:{f:[0,6,22],t:[0.5,5.8,18],lf:[-1,3,-16],lt:[1.5,3.2,-22]},
  sky:()=>SK({top:C(0x0d0906),hor:C(0x2a1d10),bot:C(0x090604),fog:C(0x190f08),fd:0.0060,star:0.18,
    ms:0.38,mhaze:0.16,moon:new THREE.Vector3(-84,18,-190),dirC:C(0xb08850),dirI:0.34,ambI:0.58}) },
{ name:'坐观羡鱼',dwell:19,river:0.04,build:bXianyu,
  cam:{f:[0,5.8,24],t:[0,6.2,21],lf:[0,6,-48],lt:[1.5,6.5,-62]},
  sky:()=>SK({top:C(0x110c08),hor:C(0x362616),bot:C(0x0b0805),fog:C(0x1a120a),fd:0.0056,star:0.20,
    ms:0.42,mhaze:0.12,moon:new THREE.Vector3(-72,24,-195),dirC:C(0xc09860),dirI:0.42,ambI:0.6}) },
];
"""
