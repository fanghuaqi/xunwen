# -*- coding: utf-8 -*-
"""yueke.py —— 《约客》（宋·赵师秀，no.211，水墨夜思）生成配置
两境：梅雨蛙声（家家雨·处处蛙：雨幕 LineSegments + WebAudio 蛙声）、
闲敲灯花（标志性瞬间·末境可点击：点击棋子——指落棋枰+灯花簌落+蛙声一片；
灯花一点暖是全页唯一暖色，水墨禁金）"""

META = dict(
    N=2, slug='yueke', title='约客', dyn='宋 · 赵师秀', brand_author='赵 师 秀',
    gold_rgb='143,164,184',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#8fa4b8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(143,164,184,.26);
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
    ],
    tip='轻点画面 / 按空格 —— 棋子敲处，灯花簌落，蛙声一片',
    hint='← → 键或空格逐境游览 · 末境可点击棋盘，看指落棋枰、灯花簌落',
    cover_read='约客。宋，赵师秀。黄梅时节家家雨，青草池塘处处蛙。有约不来过夜半，闲敲棋子落灯花。',
    cover_p1='两重意境，随诗句次第展开：黄梅时节，雨落千家，青草池塘处处蛙鸣；约好的客人过了半夜还没有来，诗人闲闲地敲着棋子，震落了一朵灯花——等待的悠长夜晚，就凝成这轻轻一敲。',
    cover_p2='边读诗，边走进那个梅雨绵绵、蛙声一片的江南雨夜。',
    end_h2='灯花 · 簌落', cn_word='两',
    words_js="['再游一次，且听蛙鸣','初识梅雨，尚需共读','渐入佳境，再诵几遍','诗境渐深，雨密塘深','已解闲敲灯花之意','一子一花，静夜自适']",
    sky_atmo='0x1c2531',
)

POEM_JS = """const POEM = [
{ name:'梅雨蛙声', jing:'黄梅雨落千家，蛙鸣盈塘 —— 雨声与蛙声，把这个夜晚拉得很长。（雨 · 塘 · 蛙）',
  segs:[
   {c:'黄梅时节家家雨，', p:py('huáng méi shí jié jiā jiā yǔ')},
   {c:'青草池塘处处蛙。', p:py('qīng cǎo chí táng chù chù wā')}],
  read:'黄梅时节家家雨，青草池塘处处蛙。',
  yisi:'梅子黄熟的时节，细雨连绵不断，家家户户都笼在蒙蒙雨幕里；长满青草的池塘边上，蛙声此起彼伏，处处可闻。「家家」「处处」两组叠字，把雨的绵密、蛙的喧闹铺满天地——而这份热闹，正反衬出等待中人的安静。',
  zhu:[['黄梅时节','梅子黄熟的江南雨季（农历四五月），连日阴雨，俗称「黄梅雨」'],['家家雨','雨水洒遍千家万户，写梅雨的普遍与绵密'],['青草池塘','春夏之交池水新满、岸草繁茂的江南水乡景象'],['处处蛙','蛙声四起，以声衬静——蛙鸣愈闹，夜愈显静，独坐等人的人也愈显孤单']] },
{ name:'闲敲灯花', jing:'约客不至，夜已过半 —— 闲闲敲着棋子，震落一朵灯花。（点击棋盘）',
  segs:[
   {c:'有约不来过夜半，', p:py('yǒu yuē bù lái guò yè bàn')},
   {c:'闲敲棋子落灯花。', p:py('xián qiāo qí zǐ luò dēng huā')}],
  read:'有约不来过夜半，闲敲棋子落灯花。',
  yisi:'约好的客人，过了半夜还没有来。诗人独自对着棋枰，闲闲地拿棋子轻敲枰面，不知不觉间，震落了灯芯上烧结的灯花。一个「敲」字，把等客不至的悠长时光，凝成一个安静的小动作——闲适里，藏着一点淡淡的寂寞。',
  zhu:[['约客','邀请客人前来相会。约（yuē），预先约定'],['过夜半','过了半夜，极言等待之久'],['敲棋子','轻轻敲打棋子。本与客人约好对弈，客至而棋不至，只能独自消遣——这是全诗的诗眼'],['灯花','灯芯燃烧时结出的花状焦结，古人以见灯花为喜兆；敲棋震落灯花，正是久坐无聊的写照']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「黄梅时节家家雨」的下一句是？', o:['青草池塘处处蛙','有约不来过夜半','闲敲棋子落灯花'], a:0},
 {q:'「有约不来过夜半」的下一句是？', o:['黄梅时节家家雨','青草池塘处处蛙','闲敲棋子落灯花'], a:2},
 {q:'「闲敲棋子落灯花」中，「敲」的读音与「灯花」的意思是？', o:['qiāo；灯芯燃烧结出的花状物','qiào；灯罩上绘制的花纹','qiāo；灯火映亮的院中花朵'], a:0},
 {q:'赵师秀与徐照、徐玑、翁卷并称，是南宋诗坛的？', o:['永嘉四灵','唐宋八大家','苏门四学士'], a:0},
 {q:'客人半夜不至，诗人却只是「闲敲棋子」。全诗传达的情感最贴近？', o:['焦躁愤懑，拍案而起','等待中的闲适与淡淡的寂寞','辗转难眠的思乡之愁'], a:1},
];
"""

SCENES_JS = """/* ================= 约客 · 两境场景（水墨夜思·冷银雨夜：梅雨蛙声、闲敲灯花） ================= */

/* 雨幕：LineSegments 细长雨丝（顶点着色器下落 + 沿程淡出），显式双 shader，uFade 铁律 */
const RAIN_VERT=`
attribute float aSeed; attribute float aEnd;
uniform float uTime; uniform float uSpeed; uniform float uH;
varying float vEnd; varying float vDist;
void main(){
  vec3 p=position;
  p.y=mod(position.y - uTime*uSpeed*(0.75+0.5*aSeed), uH);
  p.x+=aEnd*0.10; p.z+=aEnd*0.035;
  vEnd=aEnd;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  vDist=-mv.z;
  gl_Position=projectionMatrix*mv;
}`;
const RAIN_FRAG=`
uniform float uFade; uniform vec3 uC; uniform vec3 uFogColor; uniform float uFogDensity;
varying float vEnd; varying float vDist;
void main(){
  float a=uFade*(1.0-vEnd*0.72)*0.30;
  float f=1.0-exp(-pow(uFogDensity*vDist,2.0));
  a*=1.0-clamp(f,0.0,1.0)*0.9;
  gl_FragColor=vec4(uC,a);
}`;
function makeRain(o){
  o=o||{};
  const n=o.n===undefined?520:o.n, box=o.box||[90,42,120], pos=o.pos||[0,0,-16];
  const speed=o.speed===undefined?27:o.speed;
  const P=new Float32Array(n*2*3), E=new Float32Array(n*2), S=new Float32Array(n*2);
  for(let i=0;i<n;i++){
    const x=pos[0]+(Math.random()-0.5)*box[0];
    const y=pos[1]+Math.random()*box[1];
    const z=pos[2]+(Math.random()-0.5)*box[2];
    const len=0.9+Math.random()*1.2, sd=Math.random();
    for(let e=0;e<2;e++){
      const k=i*2+e;
      P[k*3]=x; P[k*3+1]=y+e*len; P[k*3+2]=z;
      E[k]=e; S[k]=sd;
    }
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aEnd',new THREE.BufferAttribute(E,1));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:speed},uH:{value:box[1]},
      uC:{value:C(o.color===undefined?0x9fb4cc:o.color)},uFade:{value:1},
      uFogColor:{value:C(0x101722)},uFogDensity:{value:0.0058}},
    vertexShader:RAIN_VERT,fragmentShader:RAIN_FRAG});
  fogShaders.push(mat.uniforms);
  const lines=new THREE.LineSegments(geo,mat);
  lines.frustumCulled=false; lines.renderOrder=3;
  return {lines:lines,update:function(t){mat.uniforms.uTime.value=t;}};
}

/* 蛙声（WebAudio）：锯齿波 + 颤音包络 + 带通，「呱——呱——」一片 */
function croak(delay,base){
  if(!groupAudio.ctx)return;
  const ctx=groupAudio.ctx, t0=ctx.currentTime+delay;
  const o=ctx.createOscillator(); o.type='sawtooth';
  o.frequency.setValueAtTime(base,t0);
  o.frequency.linearRampToValueAtTime(base*0.8,t0+0.2);
  const lfo=ctx.createOscillator(); lfo.type='sine'; lfo.frequency.value=22+base*0.05;
  const lg=ctx.createGain(); lg.gain.value=0.045;
  const g=ctx.createGain();
  g.gain.setValueAtTime(0.0001,t0);
  g.gain.exponentialRampToValueAtTime(0.05,t0+0.045);
  g.gain.setValueAtTime(0.05,t0+0.15);
  g.gain.exponentialRampToValueAtTime(0.0001,t0+0.28);
  const bp=ctx.createBiquadFilter(); bp.type='bandpass'; bp.frequency.value=base*2.4; bp.Q.value=1.8;
  o.connect(bp); bp.connect(g); g.connect(groupAudio.master);
  lg.connect(g.gain);
  o.start(t0); o.stop(t0+0.32); lfo.start(t0); lfo.stop(t0+0.32);
}
function frogChorus(n){
  if(!groupAudio.ctx)return;
  for(let i=0;i<n;i++)croak(Math.random()*1.4, 92+Math.random()*66);
}

/* 雨中村落：box 身 + 四棱顶剪影，合批 1 mesh（家家雨落处） */
function makeHouses(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?211:o.seed);
  const n=o.n===undefined?6:o.n, spread=o.spread===undefined?70:o.spread;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*spread, z=(R()-0.5)*(o.deep===undefined?18:o.deep);
    const w=4.5+R()*3.5, h=3.2+R()*2.2, d=3.5+R()*2.5;
    const body=new THREE.BoxGeometry(w,h,d); body.translate(x,h*0.5,z); B.put(body,0x0a0e16);
    const roof=new THREE.ConeGeometry(Math.max(w,d)*0.78,1.6+R()*1.1,4);
    roof.rotateY(Math.PI/4); roof.scale(1.25,1,0.95); roof.translate(x,h+0.8,z); B.put(roof,0x0d1119);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x242e40,emissive:0x04060a}),{c:0x8fa4b8,i:0.16,p:2.6})));
  return g;
}

/* 棋案：案面 + 细边 + 板足 + 横枨（冷银边光，不用金木原色辉） */
function makeQiAn(o){
  o=o||{};
  const w=o.w===undefined?5.4:o.w, d=o.d===undefined?2.9:o.d, h=o.h===undefined?1.32:o.h;
  const wood=o.wood===undefined?0x241a12:o.wood, wood2=shadeColor(wood,0.68);
  const B=new GeoBag();
  const top=new THREE.BoxGeometry(w,0.15,d); top.translate(0,h-0.075,0); B.put(top,wood);
  const edge=new THREE.BoxGeometry(w*1.008,0.045,d*1.01); edge.translate(0,h-0.16,0); B.put(edge,shadeColor(wood,1.6));
  [1,-1].forEach(function(s){
    const lg=new THREE.BoxGeometry(0.26,h-0.15,d*0.74); lg.translate(s*(w*0.5-0.32),(h-0.15)/2,0); B.put(lg,wood2);
  });
  const st=new THREE.BoxGeometry(w*0.8,0.09,0.14); st.translate(0,h*0.36,d*0.36); B.put(st,wood2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:16,
    specular:0x3a4252,emissive:0x05040a}),{c:0x8fa4b8,i:0.24,p:2.6})));
  return {g:g,h:h};
}

/* 棋枰：枰面 + 纵横格线 + 散布黑白子，合批 1 mesh */
function makeQipan(o){
  o=o||{};
  const s=o.s===undefined?2.3:o.s;
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?2120:o.seed);
  const board=new THREE.BoxGeometry(s,0.08,s); board.translate(0,0.04,0); B.put(board,0x2b2117);
  const frame=new THREE.BoxGeometry(s*1.05,0.03,s*1.05); frame.translate(0,0.005,0); B.put(frame,0x191209);
  for(let i=0;i<9;i++){
    const t=(i/8-0.5)*(s*0.86);
    const gx=new THREE.BoxGeometry(s*0.86,0.006,0.016); gx.translate(0,0.084,t); B.put(gx,0x4d4234);
    const gz=new THREE.BoxGeometry(0.016,0.006,s*0.86); gz.translate(t,0.084,0); B.put(gz,0x4d4234);
  }
  for(let i=0;i<12;i++){
    const st=new THREE.SphereGeometry(0.085,8,6); st.scale(1,0.42,1);
    st.translate((R()-0.5)*s*0.66,0.115,(R()-0.5)*s*0.66);
    B.put(st,R()<0.5?0x11141b:0xaab6c4);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x333c4c,emissive:0x04040a}),{c:0x8fa4b8,i:0.2,p:2.6})));
  return g;
}

/* 油灯：灯座 Lathe + 暖焰（全页唯一暖色）+ 暖晕 */
function makeDeng(o){
  o=o||{};
  const g=new THREE.Group(), B=new GeoBag();
  const zu=new THREE.LatheGeometry(
    [[0,0.02],[0.34,0.02],[0.38,0.08],[0.16,0.16],[0.13,0.50],[0.19,0.68],[0.30,0.78],[0.32,0.84]]
    .map(function(p){return new THREE.Vector2(p[0],p[1]);}),14);
  B.put(zu,0x1c222e);
  const pan=new THREE.CylinderGeometry(0.30,0.22,0.10,12); pan.translate(0,0.86,0); B.put(pan,0x1a202b);
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:40,
    specular:0x4a5468,emissive:0x06070c}),{c:0x8fa4b8,i:0.3,p:2.8})));
  const fl=makeFlame({h:0.95,w:0.24,planes:3,embers:12,spark:true,sparkN:10,
    core:0xffd9a4,outer:0xd96f24,light:o.light===undefined?1.2:o.light,lightD:8,lightC:0xffa050,wide:0.32});
  fl.g.position.y=0.94; g.add(fl.g);
  const baseOp=0.20;
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb066,
    transparent:true,opacity:baseOp,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(2.1,2.1,1); halo.position.y=1.35; halo.renderOrder=3; g.add(halo);
  g.update=function(t,fk){
    const k=fk===undefined?1:fk;
    fl.update(t,k);
    halo.material.opacity=k*baseOp*(0.8+0.2*Math.sin(t*6.3));
  };
  g.userData.update=g.update;
  return {g:g,update:g.update,flame:fl,halo:halo};
}

/* 灯花簌落：焰下缓落的暖烬（点击后 uGo 点亮），显式双 shader + uFade 铁律 */
const LAMPFALL_VERT=`
attribute float aSeed;
uniform float uTime; uniform float uGo;
varying float vA;
void main(){
  vec3 p=position;
  float sp=0.55+0.5*aSeed;
  float y=mod(position.y - uTime*sp*1.6, 2.6);
  p.y=y;
  vA=uGo*(1.0-y/2.6)*(0.5+0.5*aSeed);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=(3.5+3.0*aSeed)*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const LAMPFALL_FRAG=`
uniform float uFade; uniform vec3 uC; varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.1,d)*vA*uFade;
  if(a<0.004)discard;
  gl_FragColor=vec4(uC,a);
}`;
function makeLampFall(o){
  o=o||{};
  const n=o.n===undefined?46:o.n, pos=o.pos||[0,1,0];
  const P=new Float32Array(n*3), S=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*0.16;
    P[i*3+1]=pos[1]+Math.random()*2.6;
    P[i*3+2]=pos[2]+(Math.random()-0.5)*0.16;
    S[i]=Math.random();
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(P,3));
  geo.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uGo:{value:0},uFade:{value:1},uC:{value:C(0xffc07a)}},
    vertexShader:LAMPFALL_VERT,fragmentShader:LAMPFALL_FRAG});
  const points=new THREE.Points(geo,mat);
  points.frustumCulled=false; points.renderOrder=4;
  return {points:points,update:function(t,go){mat.uniforms.uTime.value=t;mat.uniforms.uGo.value=go;}};
}

function bCover(){ // 封面 · 梅雨之夜
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0e1219});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:24,layers:2,peaks:4,seed:2110,color:0x070a10,atmo:0x1c2531,fogK:0.74,glowK:0.08,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const houses=makeHouses({n:6,spread:80,deep:22,seed:2111}); houses.position.set(0,-1.6,-52); g.add(houses);
  const poet=makeFigure({pose:'独立',robe:0x1c2534,belt:0x52617a,skin:0xcbb9a2,collar:0xb4c2d4,
    hat:'发髻',rimC:0x8fa4b8,rim:0.4,noProp:true,scale:0.9});
  poet.position.set(-4,-1.8,-9); poet.rotation.y=0.4; g.add(poet);
  const rain=makeRain({n:300,box:[130,44,140],pos:[0,0,-18],speed:24,color:0x8fa4b8}); g.add(rain.lines);
  const mist=makeMist({n:7,spread:[260,36,170],pos:[0,12,-60],scale:85,color:0x7e8ea8,op:0.09});
  g.add(mist.g);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:2112,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  addLights(g,{c:0x8fa4b8,i:0.42,p:[-28,74,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); rain.update(t); mist.update(t,k); fg.update(t,k); poet.update(t,k); }};
}

function bMeiyu(){ // 一 · 梅雨蛙声 —— 家家雨 · 处处蛙（雨幕 + 蛙声）
  const g=new THREE.Group();
  const ctl={frog:1.2};
  const grd=makeGround({r:160,c1:0x06080d,c2:0x0d1119});
  grd.mesh.position.y=-0.5; g.add(grd.mesh);
  const water=makeWater({size:300,seg:80,amp:0.34,freq:0.16,speed:0.9,flow:[0.15,0.35],spec:1.1,
    deep:0x081019,shallow:0x14263a,skyc:0x1c2c42,moonDir:[28,98,-175]});
  water.mesh.position.set(9,-0.32,-20); g.add(water.mesh);
  const ridge=makeRange({r:250,h:20,layers:2,peaks:4,seed:2113,color:0x070a10,atmo:0x1c2531,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-108); g.add(ridge.g);
  /* 家家雨：雨中村落剪影 + 一两点冷窗 */
  const houses=makeHouses({n:7,spread:88,deep:20,seed:2114}); houses.position.set(-6,-0.4,-52); g.add(houses);
  const win1=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8bcd8,
    transparent:true,opacity:0.12,depthWrite:false,blending:THREE.AdditiveBlending}));
  win1.scale.set(3.2,3.2,1); win1.position.set(-16,3.4,-47); win1.renderOrder=2; g.add(win1);
  const win2=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xa8bcd8,
    transparent:true,opacity:0.10,depthWrite:false,blending:THREE.AdditiveBlending}));
  win2.scale.set(2.6,2.6,1); win2.position.set(9,2.9,-50); win2.renderOrder=2; g.add(win2);
  /* 青草池塘：塘岸草丛（芦苇代青草） */
  const grass1=makeForeground({kind:'芦苇',w:34,n:16,d:7,color:0x05080d,seed:2115,sway:1.2});
  grass1.g.position.set(-16,-0.4,-6); g.add(grass1.g);
  const grass2=makeForeground({kind:'芦苇',w:26,n:12,d:6,color:0x05080d,seed:2116,sway:0.9});
  grass2.g.position.set(20,-0.4,-12); g.add(grass2.g);
  /* 等客的诗人：独立塘畔，望着雨幕深处 */
  const poet=makeFigure({pose:'独立',robe:0x1c2534,belt:0x52617a,skin:0xcbb9a2,collar:0xb4c2d4,
    hat:'发髻',rimC:0x8fa4b8,rim:0.5,noProp:true,scale:1.62});
  poet.position.set(-9.5,-0.42,-7); poet.rotation.y=0.55; g.add(poet);
  /* 雨幕（家家雨的氛围主角）+ 塘雾 */
  const rain=makeRain({n:560,box:[110,42,120],pos:[0,1,-16],speed:27,color:0x9fb4cc}); g.add(rain.lines);
  const mist=makeMist({n:6,spread:[230,24,120],pos:[0,8,-46],scale:76,color:0x7e8ea8,op:0.085});
  g.add(mist.g);
  /* 前景框景 */
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:2117,rim:0.14});
  rk.g.position.set(-14,-1.4,14); g.add(rk.g);
  addLights(g,{c:0x8fa4b8,i:0.44,p:[-30,86,-40]},{c:0x1a2230,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.frog-=dt;
      if(ctl.frog<=0){ ctl.frog=2.4+Math.random()*2.6; frogChorus(1+Math.floor(Math.random()*3)); }
      ridge.update(t,0); water.update(t); rain.update(t); mist.update(t,k);
      grass1.update(t,k); grass2.update(t,k); rk.update(t,k); poet.update(t,k);
    }};
}

function bQiao(){ // 二（标志性瞬间·末境可点击）· 闲敲灯花 —— 点击棋盘：指落棋枰+灯花簌落+蛙声一片
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0,frog:2.0};
  const grd=makeGround({r:140,c1:0x080a10,c2:0x10141d});
  grd.mesh.position.y=-0.02; g.add(grd.mesh);
  const ridge=makeRange({r:260,h:16,layers:2,peaks:3,seed:2118,color:0x070a10,atmo:0x1c2531,fogK:0.60,glowK:0.04,y:-14});
  ridge.g.position.set(0,0,-115); g.add(ridge.g);
  /* 水轩之外：雨夜池塘，蛙声从雾外的水面上来 */
  const water=makeWater({size:280,seg:72,amp:0.26,freq:0.15,speed:0.8,flow:[0.2,0.3],spec:0.9,
    deep:0x081019,shallow:0x132437,skyc:0x1b2a3e,moonDir:[-40,96,-170]});
  water.mesh.position.set(7,-0.42,-30); g.add(water.mesh);
  /* 轩柱（top:false）+ 栏杆前景 + 屏风 */
  const p1=makePillar({h:8.5,r:0.30,color:0x18110c,top:false}); p1.g.position.set(-4.8,0,2.2); g.add(p1.g);
  const p2=makePillar({h:8.5,r:0.30,color:0x18110c,top:false}); p2.g.position.set(5.6,0,1.4); g.add(p2.g);
  const rail=makeForeground({kind:'栏杆',w:26,h:2.6,color:0x04060a,seed:2119,rim:0.1});
  rail.g.position.set(0,-0.4,1.5); g.add(rail.g);
  const screen=makeCurtain({w:15,h:6.2,color:0x121926,dark:0x080b11,folds:5,deep:0.5});
  screen.g.position.set(-1.5,0,-13); g.add(screen.g);
  /* 棋案 + 棋枰 */
  const an=makeQiAn({w:5.4,d:2.9,h:1.32}); an.g.position.set(-0.15,0,-6.8); g.add(an.g);
  const pan=makeQipan({s:2.3,seed:2120}); pan.position.set(-0.15,1.32,-6.8); g.add(pan);
  /* 独坐敲棋人：手临枰上（坐饮式） */
  const poet=makeFigure({pose:'坐饮',robe:0x1e2938,belt:0x54647e,skin:0xcbb9a2,collar:0xb6c3d4,
    hat:'发髻',rimC:0x8fa4b8,rim:0.5,noProp:true,scale:0.66});
  poet.position.set(-0.15,0,-8.6); g.add(poet);
  /* 被敲的棋子：一下一下，闲敲不止 */
  const tapStone=new THREE.Mesh(new THREE.SphereGeometry(0.1,10,8),
    new THREE.MeshPhongMaterial({color:0x11141c,shininess:36,specular:0x39445a}));
  tapStone.scale.set(1,0.45,1); tapStone.position.set(0.18,1.455,-7.9); g.add(tapStone);
  /* 案头青瓷盏 */
  const cup=makeVessel({type:'碗',mat:'陶',scale:0.55,liquid:false,shadow:true});
  cup.g.position.set(-1.6,1.32,-6.4); g.add(cup.g);
  /* 一盏油灯：灯花一点暖（全页唯一暖色） */
  const deng=makeDeng({light:1.2}); deng.g.position.set(1.85,1.32,-6.45); g.add(deng.g);
  const lampFall=makeLampFall({n:46,pos:[1.85,1.95,-6.45]}); g.add(lampFall.points);
  const burst=makeBurst({n:26,color:0xffc07a,pos:[1.85,2.05,-6.45]}); g.add(burst.points);
  const flowerGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc07a,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  flowerGlow.scale.set(2.6,2.6,1); flowerGlow.position.set(1.85,1.95,-6.45); flowerGlow.renderOrder=3; g.add(flowerGlow);
  const glowPool=new THREE.Mesh(new THREE.CircleGeometry(1.5,16),
    new THREE.MeshBasicMaterial({map:glowTex(),color:0xff9a4a,transparent:true,opacity:0.15,
      depthWrite:false,blending:THREE.AdditiveBlending}));
  glowPool.rotation.x=-Math.PI/2; glowPool.position.set(1.85,1.335,-6.45); glowPool.renderOrder=2; g.add(glowPool);
  /* 轩外雨幕 + 塘雾 + 岸草 */
  const rain=makeRain({n:380,box:[100,36,95],pos:[4,1,-32],speed:24,color:0x8fa4b8}); g.add(rain.lines);
  const mist=makeMist({n:6,spread:[220,22,110],pos:[0,7,-52],scale:74,color:0x7e8ea8,op:0.075});
  g.add(mist.g);
  const grass=makeForeground({kind:'芦苇',w:22,n:9,d:5,color:0x04060a,seed:2121,sway:0.8});
  grass.g.position.set(13,-0.5,-14); g.add(grass.g);
  addLights(g,{c:0x8fa4b8,i:0.38,p:[-24,80,-50]},{c:0x19202c,i:0.58});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/2.6);
      /* 闲敲不止：棋子轻轻磕在枰上 */
      const hop=ctl.t%1.7;
      tapStone.position.y=1.455+(hop<0.36?0.15*Math.sin(hop/0.36*Math.PI):0);
      ridge.update(t,0); water.update(t); rain.update(t); mist.update(t,k);
      rail.update(t,k); grass.update(t,k); poet.update(t,k);
      deng.update(t,k);
      lampFall.update(t,ctl.reveal);
      burst.update(t);
      flowerGlow.material.opacity=k*(0.10+0.40*ctl.reveal);
      ctl.frog-=dt;
      if(ctl.frog<=0){ ctl.frog=4.5+Math.random()*3.5; frogChorus(1+Math.floor(Math.random()*2)); }
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(1,0.02,0.14); pluck(4,0.24,0.09); pluck(2,0.5,0.07);
        burst.fire();
        frogChorus(7);
        const fl=$('#flash'); fl.textContent='灯花簌落'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070b12),hor:C(0x161e2b),bot:C(0x080c11),fog:C(0x101722),fd:0.0058,star:0.5,
  moon:new THREE.Vector3(30,100,-180),ms:1.5,mph:0,mhaze:0.06,dirC:C(0x8fa4b8),dirI:0.46,
  dirP:new THREE.Vector3(-26,84,-42),ambC:C(0x19202c),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,10,64],t:[0,11,58],lf:[0,16,-40],lt:[0,16,-40]},
  sky:()=>SK({top:C(0x060910),hor:C(0x131a26),bot:C(0x070a10),fog:C(0x0e141e),fd:0.0050,star:0.14,
    ms:1.35,mhaze:0.10,moon:new THREE.Vector3(24,92,-170),
    dirC:C(0x8fa4b8),dirI:0.38,ambC:C(0x182031),ambI:0.62}) },
{ name:'梅雨蛙声',dwell:16,river:0.055,build:bMeiyu,
  cam:{f:[0,6.5,24],t:[1.4,6.1,20.5],lf:[1.5,8,-16],lt:[0,7.6,-19]},
  sky:()=>SK({top:C(0x070b12),hor:C(0x161e2b),bot:C(0x080c11),fog:C(0x101722),fd:0.0062,star:0.12,
    ms:1.45,mhaze:0.10,moon:new THREE.Vector3(28,98,-175),
    dirC:C(0x8fa4b8),dirI:0.44,ambC:C(0x1a2230),ambI:0.62}) },
{ name:'闲敲灯花',dwell:17,river:0.035,build:bQiao,
  cam:{f:[0,3.7,4.5],t:[0.8,3.5,2.5],lf:[0.3,3.2,-8],lt:[1.2,3.2,-9.2]},
  sky:()=>SK({top:C(0x080c12),hor:C(0x171f2c),bot:C(0x090d12),fog:C(0x111823),fd:0.0075,star:0.10,
    ms:1.15,mhaze:0.12,moon:new THREE.Vector3(-36,92,-170),
    dirC:C(0x8fa4b8),dirI:0.4,ambC:C(0x1a222e),ambI:0.6}) },
];
"""
