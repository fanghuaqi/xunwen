# -*- coding: utf-8 -*-
"""pusaman-renren.py —— 《菩萨蛮·人人尽说江南好》（五代·韦庄，no.157，烟雨江南）生成配置
两境（queue.json 分境口径，stages.length=2）：
壹·春水画船（人人尽说江南好+游人只合江南老+春水碧于天+画船听雨眠，标志性瞬间·全页唯一碧点）；
贰·垆边月寒（垆边人似月+皓腕凝霜雪+未老莫还乡+还乡须断肠，末境可点击：雨落春水+船影轻摇）。
情感反转结构：前境越美，末境越沉——雾色/光温随境转沉。"""

META = dict(
    N=2, slug='pusaman-renren', title='菩萨蛮·人人尽说江南好', dyn='五代 · 韦庄', brand_author='韦 庄',
    gold_rgb='154,176,201',
    root=""":root{
  --gold:#9ab0c9; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(154,176,201,.28);
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
    tip='轻点画船 / 按空格 —— 雨落春水，船影轻摇',
    hint='← → 键或空格逐境游览 · 末境可点击画船，雨落春水、船影轻摇',
    cover_read='菩萨蛮。五代，韦庄。人人尽说江南好，游人只合江南老。春水碧于天，画船听雨眠。',
    cover_p1='两重意境，随词句次第展开：人人尽说江南好、春水碧于天画船听雨眠的水乡胜景；垆边人似月、皓腕凝霜雪的月夜酒垆，与未老莫还乡、还乡须断肠的深沉喟叹。',
    cover_p2='边读词，边走进韦庄笔下那场江南的挽留——景愈写愈美，情愈收愈沉。',
    end_h2='江南 · 断肠', cn_word='二',
    words_js="['再游一次，画船听雨','初识韦庄，尚需共读','渐入佳境，再诵几遍','词心渐明，春水碧透','已解江南劝留之意','景美情深，余味悠长']",
    sky_atmo='0x2b3a48',
)

POEM_JS = """const POEM = [
{ name:'春水画船', jing:'人人尽说江南好 —— 春水比天色还碧，画船里听雨而眠。（春水 · 画船 · 雨眠）',
  segs:[
   {c:'人人尽说江南好，', p:py('rén rén jìn shuō jiāng nán hǎo')},
   {c:'游人只合江南老。', p:py('yóu rén zhǐ hé jiāng nán lǎo')},
   {c:'春水碧于天，', p:py('chūn shuǐ bì yú tiān')},
   {c:'画船听雨眠。', p:py('huà chuán tīng yǔ mián')}],
  read:'人人尽说江南好，游人只合江南老。春水碧于天，画船听雨眠。',
  yisi:'人人都说江南好，漂泊的游人只应该在江南终老。这里春水澄碧，比天色还要明净；卧在画船中听着雨声入眠，是何等的安稳。——起笔是人人艳称的一个"好"字，水碧船眠，是江南给游人的第一重挽留。',
  zhu:[['只合','应当、应该（合，读 hé）：言游人只应在江南终老'],['春水碧于天','春江水色澄碧，胜过天色；"碧"字是全词着色最亮处'],['画船','装饰华美的游船，船身绘彩、上有篷舱'],['听雨眠','卧听雨声而眠；雨声入梦，极写江南生活的安闲']] },
{ name:'垆边月寒', jing:'垆边卖酒人如月，皓腕似凝霜雪 —— 而未老莫还乡，还乡须断肠。（垆边 · 霜雪 · 断肠）',
  segs:[
   {c:'垆边人似月，', p:py('lú biān rén sì yuè')},
   {c:'皓腕凝霜雪。', p:py('hào wàn níng shuāng xuě')},
   {c:'未老莫还乡，', p:py('wèi lǎo mò huán xiāng')},
   {c:'还乡须断肠。', p:py('huán xiāng xū duàn cháng')}],
  read:'垆边人似月，皓腕凝霜雪。未老莫还乡，还乡须断肠。',
  yisi:'酒垆旁卖酒的女子容貌如月般明媚，皓白的手腕像凝着一层霜雪。可是莫要在未老时还乡——还乡，只怕要触目伤怀、肝肠寸断。——前四句越写越美，末二句陡然一沉：江南愈好，乡思愈痛，"莫还乡"是沉痛已极的言语。',
  zhu:[['垆','酒肆中垒土为台、安放酒瓮卖酒之处；旧有卓文君当垆卖酒之典'],['人似月','指垆边卖酒的女子，姿容明丽如月'],['皓腕凝霜雪','洁白的手腕像凝着一层白霜瑞雪；皓，洁白'],['须','应当、必定：还乡必定断肠'],['断肠','悲伤到极点；一说时中原离乱，还乡唯见疮痍，故反言"莫还乡"']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「人人尽说江南好」的下一句是？', o:['游人只合江南老','春水碧于天','垆边人似月'], a:0},
 {q:'「垆边人似月」的下一句是？', o:['未老莫还乡','皓腕凝霜雪','画船听雨眠'], a:1},
 {q:'「游人只合江南老」中「合」的读音与词义是？', o:['gě，容量单位，十合为一升','hé，闭合、合拢','hé，应当、应该——游人只应在江南终老'], a:2},
 {q:'「垆边人似月」的「垆」指的是？', o:['火炉、炭炉','酒垆——酒肆中垒土为台、安放酒瓮卖酒之处，旧有卓文君当垆卖酒之典','河边的渡口码头'], a:1},
 {q:'这首词极写江南之美，而末了「未老莫还乡，还乡须断肠」真正想说的是？', o:['中原离乱，还乡唯见断肠之痛——以乐景写哀情，景愈美情愈沉','江南太好，游人贪玩忘了回家','劝人趁年轻及时行乐，老了再回乡也不迟'], a:0},
];
"""

SCENES_JS = """/* ================= 菩萨蛮·人人尽说江南好 · 两境场景（烟雨江南：春水画船、垆边月寒） ================= */

/* 画船：江南游船（船底+两舷外张+首尾起翘+拱形篷舱+三道篷箍+舷缘+橹），合批 1 mesh —— 本词标志性器物 */
function makeHuachuan(o){
  o=o||{};
  const B=new GeoBag();
  const cHull=o.hull===undefined?0x1b232f:o.hull, cTrim=o.trim===undefined?0x3d4c66:o.trim,
        cCanopy=o.canopy===undefined?0x2a3546:o.canopy;
  const L=o.len===undefined?7.4:o.len, W=o.w===undefined?2.4:o.w;
  const keel=new THREE.BoxGeometry(L,0.4,W*0.6); keel.translate(0,0.22,0); B.put(keel,shadeColor(cHull,0.72));
  [1,-1].forEach(function(s){
    const side=new THREE.BoxGeometry(L*0.92,0.55,0.14); side.rotateX(s*0.17);
    side.translate(0,0.62,s*(W/2-0.07)); B.put(side,cHull);
  });
  const bow=new THREE.BoxGeometry(L*0.2,0.44,W*0.5); bow.rotateZ(-0.24); bow.translate(L*0.5,0.4,0); B.put(bow,cHull);
  const stern=new THREE.BoxGeometry(L*0.2,0.44,W*0.5); stern.rotateZ(0.24); stern.translate(-L*0.5,0.4,0); B.put(stern,cHull);
  [1,-1].forEach(function(s){
    const gun=new THREE.BoxGeometry(L*0.8,0.09,0.2); gun.translate(0,0.94,s*(W/2-0.04)); B.put(gun,cTrim);
  });
  const can=new THREE.CylinderGeometry(1.02,1.02,4.2,10,1,true,0,Math.PI);
  can.rotateZ(Math.PI/2); can.translate(-0.4,1.0,0); B.put(can,cCanopy);
  [-1.3,0,1.3].forEach(function(x){
    const hoop=new THREE.TorusGeometry(1.05,0.045,5,12,Math.PI); hoop.rotateY(Math.PI/2);
    hoop.translate(x-0.4,1.0,0); B.put(hoop,cTrim);
  });
  const oar=new THREE.CylinderGeometry(0.04,0.06,4.0,5); oar.rotateZ(1.32);
  oar.translate(-L*0.30,0.92,0); B.put(oar,shadeColor(cHull,1.35));
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x39445a,emissive:0x05070c}),{c:0x9ab0c9,i:0.30,p:2.5})));
  return g;
}

/* 酒垆：垒土为台的垆台 + 台上酒瓮二三 + 地上酒瓮 + 旗杆酒旗（「垆边人似月」），合批 1 mesh */
function makeLu(o){
  o=o||{};
  const B=new GeoBag(), c1=o.c1===undefined?0x1a2029:o.c1, c2=0x232c3a, c3=0x314052;
  const tai=new THREE.CylinderGeometry(1.5,1.75,1.0,12); tai.translate(0,0.5,0); B.put(tai,c1);
  const mian=new THREE.CylinderGeometry(1.58,1.58,0.14,12); mian.translate(0,1.06,0); B.put(mian,c3);
  const zao=new THREE.CylinderGeometry(0.34,0.42,0.52,8); zao.translate(0.85,1.4,0.85); B.put(zao,shadeColor(c1,0.68));
  function jar(s,x,y,z,c){
    const pts=[new THREE.Vector2(0.02,0),new THREE.Vector2(0.46*s,0.05*s),new THREE.Vector2(0.60*s,0.30*s),
      new THREE.Vector2(0.50*s,0.58*s),new THREE.Vector2(0.26*s,0.70*s),new THREE.Vector2(0.28*s,0.82*s),
      new THREE.Vector2(0.34*s,0.88*s)];
    const j=new THREE.LatheGeometry(pts,10); j.translate(x,y,z); B.put(j,c);
  }
  jar(1.0,-0.55,1.13,-0.35,c2); jar(0.85,0.35,1.13,-0.5,c3); jar(0.9,0.05,1.13,0.45,shadeColor(c2,1.12));
  jar(1.15,1.9,0,0.6,shadeColor(c1,1.1));
  const pole=new THREE.CylinderGeometry(0.055,0.085,5.8,6); pole.translate(-2.4,2.9,0.2); B.put(pole,c2);
  const arm=new THREE.BoxGeometry(0.9,0.08,0.08); arm.translate(-2.05,5.55,0.2); B.put(arm,c2);
  const flag=new THREE.BoxGeometry(0.06,1.9,0.82); flag.translate(-1.72,4.55,0.2); B.put(flag,0x9fb0c0);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x34404e,emissive:0x04060a}),{c:0x8fa4c0,i:0.28,p:2.5})));
  return g;
}

/* 「春水碧于天」：水天相接处一带碧光（全页唯一碧点，着色器轻透缓息） */
const BIH_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const BIH_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float band=smoothstep(0.0,0.30,vUv.y)*smoothstep(1.0,0.45,vUv.y);
  band*=smoothstep(0.0,0.25,vUv.x)*smoothstep(1.0,0.75,vUv.x);
  float sway=0.86+0.14*sin(uTime*0.26+vUv.x*5.0);
  vec3 col=mix(vec3(0.16,0.42,0.36),vec3(0.10,0.28,0.27),clamp(vUv.y*1.5,0.0,1.0));
  gl_FragColor=vec4(col,uFade*uK*band*sway);
}`;

function bCover(){ // 卷首 · 烟雨江天 —— 隐月远山，画船一点
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0e1319,c2:0x171f2a});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:41,color:0x0b0f15,atmo:0x2b3a48,fogK:0.74,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const boat=makeHuachuan(); boat.position.set(14,0,-64); boat.scale.setScalar(0.6);
  boat.rotation.y=0.4; g.add(boat);
  const boatman=makeFigure({pose:'独立',robe:0x1a222e,belt:0x46566c,skin:0xc4b29c,collar:0xa4b4c6,
    hat:'幞头',rimC:0x9ab0c9,rim:0.4,noProp:true,scale:0.38});
  boatman.position.set(14.6,0.5,-63.6); g.add(boatman);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x090c11,seed:5,rim:0.15});
  fg.g.position.set(-6,-2,26); g.add(fg.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x090c11,seed:7,sway:0.9});
  reeds.g.position.set(15,-1.6,30); g.add(reeds.g);
  const mist=makeMist({n:9,spread:[250,26,160],pos:[0,10,-60],scale:85,color:0x8fa4bc,op:0.10});
  g.add(mist.g);
  const rain=makeGlow({n:150,box:[170,30,90],pos:[0,15,-20],color:0xa8bcd0,size:3.4,speed:0.5,rise:1,maxA:0.28,add:false});
  g.add(rain.points);
  const motes=makeGlow({n:42,box:[200,34,110],pos:[0,9,-44],color:0xa8bcd4,size:7,speed:0.05,rise:0,maxA:0.30});
  g.add(motes.points);
  addLights(g,{c:0x9ab0c9,i:0.40,p:[30,70,40]},{c:0x222c38,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); reeds.update(t,k); mist.update(t,k); rain.update(t); motes.update(t);
    boat.rotation.z=Math.sin(t*0.8)*0.015;
    boatman.update(t,k); }};
}

function bSpring(){ // 壹 · 春水画船 —— 春水碧于天，画船听雨眠（标志性瞬间·全页唯一碧点）
  const g=new THREE.Group();
  const water=makeWater({size:470,seg:92,amp:0.16,freq:0.12,speed:0.5,flow:[0.32,0.06],spec:0.42,
    deep:0x09201c,shallow:0x1d4f45,skyc:0x2c544c,moonDir:[-150,40,-200]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:26,layers:2,peaks:5,seed:1571,color:0x0a0f15,atmo:0x273541,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 水天相接一带碧光（春水碧于天——全页唯一彩点） */
  const bihMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.62}},
    vertexShader:BIH_VERT,fragmentShader:BIH_FRAG});
  const bih=new THREE.Mesh(new THREE.PlaneGeometry(230,26),bihMat);
  bih.position.set(0,7,-150); bih.renderOrder=2; g.add(bih);
  /* 两岸柳岸（水汊土盘 + 柳丝垂岸） */
  const bankL=makeGround({r:13,c1:0x0c1117,c2:0x151c26}); bankL.mesh.position.set(-21,0.08,-5); g.add(bankL.mesh);
  const bankR=makeGround({r:11,c1:0x0c1117,c2:0x151c26}); bankR.mesh.position.set(20,0.08,-10); g.add(bankR.mesh);
  const willowL=makeForeground({kind:'树枝',n:4,w:9,d:4,color:0x0a0e14,seed:1572,sway:0.8,rim:0.20});
  willowL.g.position.set(-21,0.1,-5); g.add(willowL.g);
  const willowR=makeForeground({kind:'树枝',n:3,w:8,d:4,color:0x0a0e14,seed:1573,sway:0.7,rim:0.18});
  willowR.g.position.set(20,0.1,-10); g.add(willowR.g);
  /* 画船（中景主体）+ 船头游人听雨 */
  const boat=makeHuachuan(); boat.position.set(0.9,0.02,-11.5); boat.rotation.y=0.14; g.add(boat);
  const figure=makeFigure({pose:'独立',robe:0x2a3342,belt:0x4e5f74,skin:0xcbb9a2,collar:0xaebfd2,
    hat:'幞头',rimC:0x9ab0c9,rim:0.5,noProp:true,scale:0.72});
  figure.position.set(2.3,0.9,-11.2); figure.rotation.y=-0.6; g.add(figure);
  const mist=makeMist({n:6,spread:[230,14,110],pos:[0,6,-56],scale:64,color:0x8fa4bc,op:0.07});
  g.add(mist.g);
  const rain=makeGlow({n:300,box:[150,32,80],pos:[0,16,-10],color:0xa8bcd0,size:4.2,speed:0.6,rise:1,maxA:0.40,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  const motes=makeGlow({n:40,box:[120,20,50],pos:[0,8,-40],color:0x9fb2c6,size:5.5,speed:0.04,rise:0,maxA:0.14});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:8,color:0x080b10,seed:1574,rim:0.14});
  rk.g.position.set(-12,-1.4,10); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:16,n:8,d:6,color:0x080b10,seed:1575,sway:1.0});
  reeds.g.position.set(12,-1.2,9); g.add(reeds.g);
  addLights(g,{c:0x9ab4c4,i:0.42,p:[-30,80,-30]},{c:0x26323e,i:0.70});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); rain.update(t); motes.update(t);
    figure.update(t,k); willowL.update(t,k); willowR.update(t,k); rk.update(t,k); reeds.update(t,k);
    boat.rotation.z=Math.sin(t*1.05)*0.013;
    boat.position.y=0.02+Math.sin(t*0.85)*0.05;
    bihMat.uniforms.uTime.value=t;
    bihMat.uniforms.uFade.value=k;
    bihMat.uniforms.uK.value=k*(0.50+0.14*Math.sin(t*0.3));
  }};
}

function bLuBian(){ // 贰（末境可点击）· 垆边月寒 —— 人似月皓腕霜雪；点击：雨落春水，船影轻摇
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,rainK:0,rockK:0};
  const water=makeWater({size:470,seg:92,amp:0.14,freq:0.12,speed:0.42,flow:[0.25,0.06],spec:0.5,
    deep:0x081714,shallow:0x16382f,skyc:0x1f332f,moonDir:[-34,22,-120]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:22,layers:2,peaks:4,seed:1576,color:0x090d12,atmo:0x212c38,fogK:0.58,glowK:0.05});
  g.add(ridge.g);
  /* 岸盘（酒垆之岸）+ 归乡路（没入雾中）+ 行人二三 */
  const bank=makeGround({r:30,c1:0x0d1218,c2:0x171e29}); bank.mesh.position.set(0,0.1,-34); g.add(bank.mesh);
  const road=new THREE.Mesh(new THREE.BoxGeometry(2.4,0.06,46),
    new THREE.MeshPhongMaterial({color:0x161c26,shininess:8,specular:0x2c3844}));
  road.rotation.y=0.10; road.position.set(-9,0.14,-52); g.add(road);
  const crowd=makeCrowd({n:2,rect:[-11,-64,4,12],seed:1577,color:0x10151c,rimC:0x8fa4bc,
    rim:0.16,sMin:0.5,sMax:0.66});
  g.add(crowd.mesh);
  /* 酒垆 + 垆边人（月白罗衫、银边光——人似月） */
  const lu=makeLu(); lu.position.set(-7.5,0.12,-15); lu.rotation.y=0.5; g.add(lu);
  const figure=makeFigure({pose:'独立',robe:0xbfc9d6,belt:0x8395ab,skin:0xd9c4ae,collar:0xe8eef4,
    hat:'发髻',rimC:0xd6e2ee,rim:0.75,noProp:true,scale:1.0});
  figure.position.set(-5.4,0.12,-13.4); figure.rotation.y=-0.35; g.add(figure);
  /* 画船夜泊（前景之侧）+ 船头游子望岸 */
  const boat=makeHuachuan(); boat.position.set(5.5,0.02,-3.5); boat.rotation.y=-0.52; g.add(boat);
  const poet=makeFigure({pose:'独立',robe:0x2a3342,belt:0x4e5f74,skin:0xcbb9a2,collar:0xaebfd2,
    hat:'幞头',rimC:0x9ab0c9,rim:0.65,noProp:true,scale:0.88});
  poet.position.set(4.1,0.9,-2.6); poet.rotation.y=-1.15; g.add(poet);
  const lamp=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9ab0c9,
    transparent:true,opacity:0.55,depthWrite:false,blending:THREE.AdditiveBlending}));
  lamp.scale.set(2.6,2.6,1); lamp.position.set(6.6,1.9,-3.0); lamp.renderOrder=2; g.add(lamp);
  const pl=new THREE.PointLight(0x8fa8c4,1.1,26); pl.position.set(6.6,2.2,-3.0); g.add(pl);
  /* 雨两层：底噪细雨 + 点击后「雨落春水」 */
  const rain=makeGlow({n:150,box:[130,28,70],pos:[0,14,-8],color:0xa8bcd0,size:3.4,speed:0.45,rise:1,maxA:0.24,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  const rainH=makeGlow({n:260,box:[90,26,54],pos:[4,13,-6],color:0xb2c6da,size:4.4,speed:0.72,rise:1,maxA:0.5,add:false});
  rainH.points.renderOrder=3; g.add(rainH.points);
  const mist=makeMist({n:7,spread:[220,14,110],pos:[0,6,-46],scale:74,color:0x7e93a6,op:0.09});
  g.add(mist.g);
  const willowL=makeForeground({kind:'树枝',n:3,w:13,d:5,color:0x070a0f,seed:1578,sway:1.2,rim:0.18});
  willowL.g.position.set(-13,-0.5,12); g.add(willowL.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:8,color:0x070a0f,seed:1579,rim:0.14});
  rk.g.position.set(11,-1.3,13); g.add(rk.g);
  addLights(g,{c:0x8aa0b4,i:0.32,p:[-40,80,-40]},{c:0x1f2833,i:0.68});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.rainK=Math.min(1,ctl.rainK+dt/2.2);
        ctl.rockK=Math.min(1,ctl.rockK+dt/3.0);
      }
      ridge.update(t,0); water.update(t); mist.update(t,k); rain.update(t);
      figure.update(t,k); poet.update(t,k); crowd.update(t); willowL.update(t,k); rk.update(t,k);
      /* 船影轻摇：点击后摆幅与浮沉渐大 */
      boat.rotation.z=Math.sin(t*1.1)*0.016+ctl.rockK*Math.sin(t*1.9)*0.05;
      boat.rotation.x=ctl.rockK*Math.sin(t*1.4)*0.02;
      boat.position.y=0.02+Math.sin(t*0.9)*0.05+ctl.rockK*Math.sin(t*1.7)*0.1;
      rainH.mat.uniforms.uFade.value=k*ctl.rainK;
      lamp.material.opacity=k*(0.42+0.13*Math.sin(t*2.1));
      pl.intensity=k*(0.85+0.25*Math.sin(t*2.1));
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(1,0.1,0.12); pluck(3,0.5,0.11); pluck(4,0.95,0.10); pluck(5,1.4,0.09);
        const fl=$('#flash'); fl.textContent='画船听雨'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0f141c),hor:C(0x232e3a),bot:C(0x0b0e13),fog:C(0x151d26),fd:0.013,star:0.05,
  moon:new THREE.Vector3(-110,50,-190),ms:0.45,mph:0.2,mhaze:0.12,dirC:C(0x9ab0c9),dirI:0.4,
  dirP:new THREE.Vector3(-30,80,-30),ambC:C(0x222c38),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.04,build:bCover,
  cam:{f:[0,10,64],t:[0,9,54],lf:[0,10,-46],lt:[0,10,-46]},
  sky:()=>SK({top:C(0x10161f),hor:C(0x242f3b),bot:C(0x0c0f14),fog:C(0x151c25),fd:0.012,star:0.10,
    ms:0.5,moon:new THREE.Vector3(-90,60,-190),
    dirC:C(0x9ab0c9),dirI:0.4,ambC:C(0x222c38),ambI:0.66}) },
{ name:'春水画船',dwell:17,river:0.06,build:bSpring,
  cam:{f:[0,5.8,15.5],t:[1,5.2,13],lf:[1.5,4.5,-12],lt:[3.5,4.5,-16]},
  sky:()=>SK({top:C(0x121a24),hor:C(0x2b3a44),bot:C(0x0d1116),fog:C(0x17222b),fd:0.013,star:0.04,
    ms:0.35,mph:0.25,mhaze:0.12,moon:new THREE.Vector3(-150,40,-200),
    dirC:C(0x9ab4c4),dirI:0.42,ambC:C(0x26323e),ambI:0.70}) },
{ name:'垆边月寒',dwell:19,river:0.035,build:bLuBian,
  cam:{f:[0,6,17],t:[-1,5.5,14],lf:[-2,4.5,-14],lt:[-4,4,-22]},
  sky:()=>SK({top:C(0x0c1017),hor:C(0x1c2530),bot:C(0x090b10),fog:C(0x141b23),fd:0.015,star:0.05,
    ms:0.55,mph:0.12,mhaze:0.10,moon:new THREE.Vector3(-30,33,-120),
    dirC:C(0x8aa0b4),dirI:0.32,ambC:C(0x1f2833),ambI:0.68}) },
];
"""
