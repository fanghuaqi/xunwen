# -*- coding: utf-8 -*-
"""pusaman-pinglin.py —— 《菩萨蛮·平林漠漠烟如织》（唐·李白，传，no.155，烟雨江南）生成配置
三境（queue.json 分境口径）：平林烟织（平林烟带+寒山伤心碧+暝色高楼）、
玉阶宿鸟（玉阶伫立+宿鸟归飞急）、长亭短亭（标志性瞬间·末境可点击：宿鸟投林+长亭短亭连线）。"""

META = dict(
    N=3, slug='pusaman-pinglin', title='菩萨蛮·平林漠漠烟如织', dyn='唐 · 李白（传）', brand_author='李 白',
    gold_rgb='143,154,184',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#8f9ab8; --ink:#e6ecef; --dim:#7e93a6; --paper:rgba(13,19,27,.60);
  --line:rgba(143,154,184,.26);
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
    tip='轻点画面 / 按空格 —— 宿鸟投林，长亭短亭连向天际',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看宿鸟投林、长亭短亭一线相牵',
    cover_read='菩萨蛮。唐，李白。平林漠漠烟如织，寒山一带伤心碧。暝色入高楼，有人楼上愁。',
    cover_p1='三重意境，随词句次第展开：平林漠漠烟如织、寒山一带伤心碧的暝色远望；玉阶空伫立、宿鸟归飞急的楼头愁思；末了长亭更短亭，归程遥遥没入烟霭天际。',
    cover_p2='边读词，边走进暮烟笼罩的江南暝色，体会那份望归不得、愁绪如织的深情。',
    end_h2='暝色 · 归程', cn_word='三',
    words_js="['再游一次，烟织暮愁','初识词境，尚需共读','渐入佳境，再诵几遍','愁绪渐深，暮色四合','已解长亭送别之意','归程入雾，余韵悠长']",
    sky_atmo='0x2a3a46',
)

POEM_JS = """const POEM = [
{ name:'平林烟织', jing:'平林漠漠、烟霭如织，寒山一带碧得叫人心伤——暝色四合，高楼之上有人怀愁。（烟 · 碧 · 暝色）',
  segs:[
   {c:'平林漠漠烟如织，', p:py('píng lín mò mò yān rú zhī')},
   {c:'寒山一带伤心碧。', p:py('hán shān yí dài shāng xīn bì')},
   {c:'暝色入高楼，', p:py('míng sè rù gāo lóu')},
   {c:'有人楼上愁。', p:py('yǒu rén lóu shàng chóu')}],
  read:'平林漠漠烟如织，寒山一带伤心碧。暝色入高楼，有人楼上愁。',
  yisi:'平坦的树林上空，暮霭沉沉、烟丝如织；寒山一带，是一片叫人伤心的碧色。暮色渐渐漫进高楼，楼上有人正满怀忧愁。——以烟织愁起笔，暝色入楼，愁亦入楼。',
  zhu:[['平林','平整延展的树林，远望如一带横陈'],['漠漠','迷蒙广漠、密布遍野的样子'],['烟如织','暮烟稠密横斜，像织成的轻纱'],['伤心碧','碧得叫人心伤；碧，青绿色，此处碧色因愁眼相看而致伤'],['暝色','暮色、黄昏的天色（暝，读 míng）'],['楼上愁','楼上远望之人满怀愁绪，词眼所在']] },
{ name:'玉阶宿鸟', jing:'玉阶伫立终是枉然，归鸟急急投林——鸟犹知返，人归何处？（玉阶 · 宿鸟）',
  segs:[
   {c:'玉阶空伫立，', p:py('yù jiē kōng zhù lì')},
   {c:'宿鸟归飞急。', p:py('sù niǎo guī fēi jí')},
   {c:'何处是归程？', p:py('hé chù shì guī chéng')}],
  read:'玉阶空伫立，宿鸟归飞急。何处是归程？',
  yisi:'她在玉阶上久久伫立，终究是枉然；归巢的鸟儿急急掠过天际。鸟儿尚知急急归巢，我的归程又在哪里呢？——以鸟之急归，反衬人之难归。',
  zhu:[['玉阶','玉石台阶，一说白石阶，言其洁净清冷'],['空伫立','久久站立而一无所获，枉自等候（伫，读 zhù）'],['宿鸟','归巢栖息的鸟（宿，读 sù）'],['归飞急','急急飞回巢去；鸟归之「急」，正映人归之遥'],['归程','回家的路程']] },
{ name:'长亭短亭', jing:'望断归程，唯有长亭连着短亭，一路没入暝色天际。（点击画面——宿鸟投林、亭亭相连）',
  segs:[
   {c:'长亭更短亭。', p:py('cháng tíng gèng duǎn tíng')}],
  read:'长亭更短亭。',
  yisi:'望断了归程，哪里有答案？只有那长亭连着短亭、短亭接着长亭，一路逶迤没入暝色天际。——归程愈显遥远，愁思愈见绵长，全词收在一片苍茫里。',
  zhu:[['长亭短亭','古时设在路旁供行人歇脚的亭舍，十里一长亭、五里一短亭；亭亭相接，代指漫长旅途与送别之地'],['更','接连、又加上（读 gèng）：长亭过后又是短亭，极言归途之遥、愁绪之不尽']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「平林漠漠烟如织」的下一句是？', o:['寒山一带伤心碧','暝色入高楼','玉阶空伫立'], a:0},
 {q:'「宿鸟归飞急」的下一句是？', o:['有人楼上愁','长亭更短亭','何处是归程？'], a:2},
 {q:'「暝色入高楼」中「暝」的读音与词义是？', o:['míng，暮色、黄昏的天色','míng，明亮的月光','mèng，朦胧的梦境'], a:0},
 {q:'「长亭更短亭」中「长亭短亭」指的是？', o:['江边泊船的码头','古时路旁供行人歇脚的亭舍，十里一长亭、五里一短亭，常代指漫长旅途与送别','城头报时的更楼'], a:1},
 {q:'这首词借暝色高楼、归鸟长亭，主要抒发的是？', o:['游子思归、思妇怀远的羁旅愁思','田园隐居的闲适之乐','边塞征战的豪情壮志'], a:0},
];
"""

SCENES_JS = """/* ================= 菩萨蛮·平林漠漠烟如织 · 三境场景（烟雨江南：平林烟织、玉阶宿鸟、长亭短亭） ================= */

/* 平林带：地平线上一排远树剪影（「漠漠」成带，合批 1 mesh） */
function makePinglin(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?31:o.seed);
  const n=o.n===undefined?16:o.n, w=o.w===undefined?150:o.w, h=o.h===undefined?4.5:o.h;
  const B=new GeoBag(), base=o.color===undefined?0x0a0e15:o.color;
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*(o.d===undefined?10:o.d);
    const hh=h*(0.45+R()), cw=1.8+R()*2.6;
    const trunk=new THREE.CylinderGeometry(0.10,0.17,hh*0.55,5);
    trunk.translate(x,hh*0.28,z); B.put(trunk,shadeColor(base,0.9));
    const top=new THREE.SphereGeometry(cw*0.5,7,5); top.scale(0.95,0.78,0.95);
    top.translate(x,hh,z); B.put(top,shadeColor(base,1.0+0.3*R()));
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3444,emissive:0x04060a}),{c:0x8fa4c0,i:0.16,p:2.6})));
  return g;
}

/* 高楼：临水楼台（台基 + 两层楼身 + 双层出挑层檐 + 顶层开敞亭室 + 东侧玉阶），合批 1 mesh */
function makeGaolou(){
  const B=new GeoBag(), c1=0x0e1219, c2=0x131a25, c3=0x1a2331, cj=0x5c6874, cj2=0x74818e;
  const terrace=new THREE.BoxGeometry(9,1.4,6.4); terrace.translate(0,0.7,0); B.put(terrace,c1);
  const s1=new THREE.BoxGeometry(5.2,3.6,4.2); s1.translate(0,3.2,0); B.put(s1,c2);
  const lip1=new THREE.BoxGeometry(7.4,0.16,5.8); lip1.translate(0,5.06,0); B.put(lip1,c3);
  const e1=new THREE.BoxGeometry(6.8,0.5,5.4); e1.translate(0,5.35,0); B.put(e1,c3);
  const s2=new THREE.BoxGeometry(4.4,3.0,3.6); s2.translate(0,7.1,0); B.put(s2,c2);
  const lip2=new THREE.BoxGeometry(6.2,0.16,4.8); lip2.translate(0,8.66,0); B.put(lip2,c3);
  const e2=new THREE.BoxGeometry(5.6,0.45,4.4); e2.translate(0,8.95,0); B.put(e2,c3);
  const deck=new THREE.BoxGeometry(3.4,0.2,3.0); deck.translate(0,9.28,0); B.put(deck,c3);
  [[1.7,1.5],[1.7,-1.5],[-1.7,1.5],[-1.7,-1.5]].forEach(function(p){
    const post=new THREE.CylinderGeometry(0.06,0.075,3.3,5); post.translate(p[0],11.03,p[1]); B.put(post,c3);
  });
  const rail=new THREE.TorusGeometry(1.62,0.035,4,18); rail.rotateX(Math.PI/2); rail.scale(1.16,1,1.0);
  rail.translate(0,11.5,0); B.put(rail,c3);
  const roof=new THREE.ConeGeometry(4.6,2.1,4); roof.rotateY(Math.PI/4);
  roof.scale(1.08,1,1.02); roof.translate(0,13.73,0); B.put(roof,c3);
  const knob=new THREE.SphereGeometry(0.14,6,5); knob.translate(0,14.92,0); B.put(knob,c3);
  for(let i=0;i<6;i++){
    const topY=Math.max(0.1,1.42-i*(1.4/6)), x=4.95+i*0.85;
    const step=new THREE.BoxGeometry(0.85,topY,2.2); step.translate(x,topY/2,0); B.put(step,i%2?cj:cj2);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x39445a,emissive:0x05070c}),{c:0x9fb3cc,i:0.30,p:2.5})));
  return g;
}

/* 宿鸟群：斜掠的鸟影（两片三角翼为一只，整群合批 1 mesh；group 沿航迹飞行） */
function makeBirds(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?47:o.seed);
  const n=o.n===undefined?9:o.n;
  const pos=[];
  const tri=[[-1.05,0.16,0.30],[0,0,-0.36],[0,0,0.30],[1.05,0.16,0.30],[0,0,0.30],[0,0,-0.36]];
  for(let i=0;i<n;i++){
    const cx=(R()-0.5)*(o.spread===undefined?15:o.spread);
    const cy=(R()-0.5)*4.5, cz=(R()-0.5)*9;
    const s=(o.sMin===undefined?0.62:o.sMin)+R()*0.7;
    const ry=(o.head===undefined?0:o.head)+(R()-0.5)*0.4;
    const c=Math.cos(ry), sn=Math.sin(ry);
    for(let v=0;v<6;v++){
      const x=tri[v][0]*s, y=tri[v][1]*s, z=tri[v][2]*s;
      pos.push(cx+x*c+z*sn, cy+y, cz-x*sn+z*c);
    }
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  const mesh=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({color:o.color===undefined?0x0a0e15:o.color,
    transparent:true,opacity:1,side:THREE.DoubleSide}));
  mesh.frustumCulled=false;
  const grp=new THREE.Group(); grp.add(mesh);
  return {g:grp,mesh:mesh};
}

/* 长亭/短亭：石基 + 四柱 + 攒尖顶 + 顶珠，合批 1 mesh（scale 出长亭短亭之别） */
function makeTing(o){
  o=o||{};
  const B=new GeoBag(), c1=o.c1===undefined?0x12171f:o.c1, c2=o.c2===undefined?0x1a2230:o.c2;
  const w=o.w===undefined?4.2:o.w, h=o.h===undefined?3.2:o.h;
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
    specular:0x34404e,emissive:0x04060a}),{c:0x8fa4c0,i:0.30,p:2.5})));
  return g;
}

/* 「伤心碧」：寒山之上一带青碧雾光——全页唯一的彩色点（着色器横带，缓息轻透） */
const BI_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const BI_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
void main(){
  float band=pow(smoothstep(0.0,0.45,vUv.y),1.5)*smoothstep(1.0,0.55,vUv.y);
  band*=smoothstep(0.0,0.35,vUv.x)*smoothstep(1.0,0.65,vUv.x);
  float sway=0.82+0.18*sin(uTime*0.22+vUv.x*7.0);
  vec3 col=mix(vec3(0.13,0.34,0.29),vec3(0.10,0.22,0.24),clamp(vUv.y*1.4,0.0,1.0));
  gl_FragColor=vec4(col,uFade*uK*band*sway);
}`;

/* 长亭短亭连线：亭顶之间的光带（aProg 逐段点亮 + 游走亮头，单 mesh） */
const LINE_VERT=`
attribute float aProg;
uniform float uTime;
varying float vP; varying vec2 vUv;
void main(){
  vP=aProg; vUv=uv;
  vec3 p=position;
  p.y+=sin(uTime*1.3+aProg*9.0)*0.10;
  gl_Position=projectionMatrix*modelViewMatrix*vec4(p,1.0);
}`;
const LINE_FRAG=`
uniform float uTime; uniform float uFade; uniform float uReveal;
varying float vP; varying vec2 vUv;
void main(){
  float lit=smoothstep(vP-0.10,vP+0.02,uReveal);
  float head=exp(-pow((uReveal-vP)*13.0,2.0))*step(0.001,uReveal)*step(uReveal,0.999);
  float ex=smoothstep(0.0,0.22,vUv.x)*smoothstep(1.0,0.78,vUv.x);
  float ey=smoothstep(0.0,0.35,vUv.y)*smoothstep(1.0,0.65,vUv.y);
  vec3 col=mix(vec3(0.58,0.68,0.84),vec3(0.88,0.93,1.0),head);
  gl_FragColor=vec4(col,uFade*(lit*0.42+head*0.85)*ex*ey);
}`;
function makeChainLine(pts){
  const SEG=8, pos=[], uv=[], prog=[], idx=[];
  const total=pts.length-1;
  for(let i=0;i<total;i++){
    const A=pts[i], Bp=pts[i+1];
    for(let s=0;s<=SEG;s++){
      const t=s/SEG;
      const x=A.x+(Bp.x-A.x)*t, z=A.z+(Bp.z-A.z)*t;
      const y=A.y+(Bp.y-A.y)*t+Math.sin(t*Math.PI)*1.1;
      pos.push(x,y,z); uv.push(t,0); prog.push((i+t)/total);
      pos.push(x,y+0.5,z); uv.push(t,1); prog.push((i+t)/total);
    }
    for(let s=0;s<SEG;s++){
      const r0=(i*(SEG+1)+s)*2;
      idx.push(r0,r0+2,r0+1, r0+1,r0+2,r0+3);
    }
  }
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  geo.setAttribute('uv',new THREE.BufferAttribute(new Float32Array(uv),2));
  geo.setAttribute('aProg',new THREE.BufferAttribute(new Float32Array(prog),1));
  geo.setIndex(idx);
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.DoubleSide,
    blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uReveal:{value:0}},
    vertexShader:LINE_VERT,fragmentShader:LINE_FRAG});
  const mesh=new THREE.Mesh(geo,mat); mesh.renderOrder=4;
  return {mesh:mesh,mat:mat};
}

function bCover(){ // 卷首 · 烟江暮色
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x0f1319,c2:0x181f28});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:26,layers:2,peaks:4,seed:41,color:0x0b0f15,atmo:0x2a3a46,fogK:0.74,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  const pinglin=makePinglin({n:10,w:200,h:4,seed:33}); pinglin.position.set(0,0,-96); g.add(pinglin);
  const tower=makeGaolou(); tower.position.set(30,0,-95); tower.scale.setScalar(0.75); g.add(tower);
  const fg=makeForeground({kind:'坡石',n:3,r:4.4,w:26,d:9,color:0x090c11,seed:5,rim:0.15});
  fg.g.position.set(-6,-2,26); g.add(fg.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:10,d:6,color:0x090c11,seed:7,sway:0.9});
  reeds.g.position.set(16,-1.6,30); g.add(reeds.g);
  const mist=makeMist({n:9,spread:[250,26,160],pos:[0,10,-60],scale:85,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const rain=makeGlow({n:160,box:[170,30,90],pos:[0,15,-20],color:0xa8bcd0,size:3.6,speed:0.5,rise:1,maxA:0.30,add:false});
  g.add(rain.points);
  const motes=makeGlow({n:46,box:[200,34,110],pos:[0,9,-44],color:0xa8bcd4,size:7,speed:0.05,rise:0,maxA:0.32});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.40,p:[30,70,40]},{c:0x212b36,i:0.66});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); reeds.update(t,k); mist.update(t,k); rain.update(t); motes.update(t); }};
}

function bPinglin(){ // 壹 · 平林烟织 —— 烟霭如织、寒山伤心碧、暝色入高楼
  const g=new THREE.Group();
  const water=makeWater({size:480,seg:90,amp:0.22,freq:0.10,speed:0.45,flow:[0.35,0.1],spec:0.9,
    deep:0x0a141d,shallow:0x16303f,skyc:0x22303c,moonDir:[-150,30,-200]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:30,layers:2,peaks:5,seed:1551,color:0x0a0f14,atmo:0x24413c,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  /* 平林两带（漠漠层叠）+ 烟织两层（横流雾带交叉如织） */
  const pl1=makePinglin({n:18,w:170,h:5,seed:1552,d:12}); pl1.position.set(0,0,-62); g.add(pl1);
  const pl2=makePinglin({n:14,w:190,h:3.6,seed:1554,d:10}); pl2.position.set(-6,0,-84); g.add(pl2);
  const flowA=makeFlow({n:300,box:[180,12,40],pos:[0,5,-66],color:0x93aac0,size:9,speed:5.2,maxA:0.22});
  g.add(flowA.points);
  const flowB=makeFlow({n:200,box:[170,9,36],pos:[0,9,-88],color:0x8aa2b8,size:12,speed:3.6,maxA:0.16});
  g.add(flowB.points);
  /* 伤心碧：寒山上空一带青碧雾光（全页唯一彩点） */
  const biMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:0.7}},
    vertexShader:BI_VERT,fragmentShader:BI_FRAG});
  const bi=new THREE.Mesh(new THREE.PlaneGeometry(210,24),biMat);
  bi.position.set(0,18,-94); bi.renderOrder=2; g.add(bi);
  /* 高楼 + 楼头愁人（开敞亭室中，倚栏望远）+ 窗间孤灯微光（黛蓝清冷） */
  const tower=makeGaolou(); tower.position.set(14,0,-20); g.add(tower);
  const figure=makeFigure({pose:'独立',robe:0x1e2836,belt:0x51617a,skin:0xcbb9a2,collar:0xb4c2d4,
    hat:'发髻',rimC:0x9fb3cc,rim:0.65,noProp:true,scale:0.8});
  figure.position.set(14.4,9.38,-20.3); figure.rotation.y=-0.45; g.add(figure);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaec2d8,
    transparent:true,opacity:0.26,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(1.8,1.8,1); win.position.set(14,10.6,-17.8); win.renderOrder=2; g.add(win);
  const mist=makeMist({n:6,spread:[240,14,110],pos:[0,6.5,-58],scale:64,color:0x7e93a6,op:0.07});
  g.add(mist.g);
  const rain=makeGlow({n:300,box:[150,34,80],pos:[0,17,-14],color:0xa8bcd0,size:4.2,speed:0.62,rise:1,maxA:0.42,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  const motes=makeGlow({n:46,box:[120,20,50],pos:[0,9,-44],color:0x9fb2c6,size:5.5,speed:0.04,rise:0,maxA:0.15});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x080b10,seed:1555,rim:0.15});
  rk.g.position.set(-13,-1.4,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:12,d:6,color:0x080b10,seed:1556,sway:1.0});
  reeds.g.position.set(12,-1.2,11); g.add(reeds.g);
  addLights(g,{c:0x8fa4c4,i:0.40,p:[-30,80,-30]},{c:0x232e3a,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); flowA.update(t); flowB.update(t);
    rain.update(t); motes.update(t); figure.update(t,k); rk.update(t,k); reeds.update(t,k);
    win.material.opacity=k*(0.20+0.06*Math.sin(t*0.7));
    biMat.uniforms.uTime.value=t;
    biMat.uniforms.uFade.value=k;
    biMat.uniforms.uK.value=k*(0.55+0.15*Math.sin(t*0.3));
  }};
}

function bYuJie(){ // 贰 · 玉阶宿鸟 —— 玉阶空伫立，宿鸟归飞急
  const g=new THREE.Group();
  const water=makeWater({size:460,seg:88,amp:0.20,freq:0.11,speed:0.5,flow:[0.4,0.12],spec:0.55,
    deep:0x0a131b,shallow:0x152c3a,skyc:0x1f2c38,moonDir:[-150,30,-200]});
  g.add(water.mesh);
  const ridge=makeRange({r:230,h:24,layers:2,peaks:4,seed:1553,color:0x090d12,atmo:0x22303c,fogK:0.60,glowK:0.05});
  g.add(ridge.g);
  const tower=makeGaolou(); tower.position.set(-10,0,-20); g.add(tower);
  /* 愁人下楼，伫立玉阶（空）——望鸟归去 */
  const figure=makeFigure({pose:'独立',robe:0x1e2836,belt:0x51617a,skin:0xcbb9a2,collar:0xb4c2d4,
    hat:'发髻',rimC:0x9fb3cc,rim:0.55,noProp:true,scale:1.05});
  figure.position.set(-3.4,0.7,-19.8); figure.rotation.y=-0.4; g.add(figure);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xaec2d8,
    transparent:true,opacity:0.16,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(1.8,1.8,1); win.position.set(-10,10.9,-17.8); win.renderOrder=2; g.add(win);
  /* 宿鸟归飞急：一列鸟影自天际急掠（向林而去） */
  const birds=makeBirds({n:10,seed:1558,spread:13,sMin:0.95});
  birds.g.rotation.y=1.57; birds.g.position.set(-70,15.5,-30); g.add(birds.g);
  /* 望眼：一条归路隐约伸向天际 */
  const road=new THREE.Mesh(new THREE.BoxGeometry(2.6,0.06,90),
    new THREE.MeshPhongMaterial({color:0x141920,shininess:8,specular:0x2c3844}));
  road.rotation.y=-0.12; road.position.set(14,0.02,-38); g.add(road);
  const mist=makeMist({n:6,spread:[220,14,100],pos:[0,6,-48],scale:74,color:0x7e93a6,op:0.09});
  g.add(mist.g);
  const rain=makeGlow({n:260,box:[140,32,76],pos:[0,16,-12],color:0xa8bcd0,size:4.0,speed:0.58,rise:1,maxA:0.42,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  const motes=makeGlow({n:40,box:[110,16,50],pos:[0,6,-20],color:0x9fb2c6,size:5,speed:0.04,rise:0,maxA:0.18});
  g.add(motes.points);
  const tree=makeForeground({kind:'树枝',n:2,w:14,d:5,color:0x070a0f,seed:911,sway:1.3,rim:0.18});
  tree.g.position.set(14,-0.5,10); g.add(tree.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:8,color:0x070a0f,seed:1559,rim:0.14});
  rk.g.position.set(-12,-1.3,11); g.add(rk.g);
  addLights(g,{c:0x8fa4c4,i:0.38,p:[-30,80,-30]},{c:0x212a35,i:0.68});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); mist.update(t,k); rain.update(t); motes.update(t);
    figure.update(t,k); tree.update(t,k); rk.update(t,k);
    birds.g.position.set(-70+((t*10)%140),15.5+Math.sin(t*2.2)*1.1,-30);
    win.material.opacity=k*(0.11+0.05*Math.sin(t*0.6));
  }};
}

function bTing(){ // 叁（标志性瞬间·末境可点击）· 长亭短亭 —— 点击：宿鸟投林，长亭短亭连向天际
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0,home:0};
  const grd=makeGround({r:140,c1:0x0e1217,c2:0x181f28});
  grd.mesh.position.y=-0.3; g.add(grd.mesh);
  const ridge=makeRange({r:250,h:20,layers:2,peaks:4,seed:1557,color:0x090c11,atmo:0x1f2b36,fogK:0.58,glowK:0.05});
  g.add(ridge.g);
  /* 归路：长亭更短亭，连向天际 */
  const road=new THREE.Mesh(new THREE.BoxGeometry(2.8,0.06,150),
    new THREE.MeshPhongMaterial({color:0x1c2330,shininess:8,specular:0x2c3844}));
  road.rotation.y=0.10; road.position.set(6.5,0.02,-56); g.add(road);
  const tingPts=[[4.5,-11,1.05],[7.5,-24,0.85],[10.5,-40,0.68],[13,-62,0.52],[15,-90,0.4]];
  const tips=[];
  tingPts.forEach(function(p){
    const t=makeTing(); t.position.set(p[0],0,p[1]); t.scale.setScalar(p[2]); g.add(t);
    tips.push({x:p[0],y:5.6*p[2]+0.15,z:p[1]});
  });
  const chain=makeChainLine(tips); g.add(chain.mesh);
  /* 投林之林 + 林梢微光（点击后亮起） */
  const shulin=makePinglin({n:14,w:44,d:16,h:7,seed:1560,color:0x080b10});
  shulin.position.set(24,0,-64); g.add(shulin);
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0x9fb8d0,
    transparent:true,opacity:0.35,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(26,14,1); halo.position.set(24,8,-62); halo.renderOrder=2; g.add(halo);
  /* 宿鸟：巡天待投 */
  const birds=makeBirds({n:10,seed:1561,spread:13,sMin:1.0});
  birds.g.rotation.y=1.57; birds.g.position.set(-60,16,-30); g.add(birds.g);
  /* 楼头人远望（画面左缘，望断归程）+ 路上行人二三 */
  const figure=makeFigure({pose:'独立',robe:0x1e2836,belt:0x51617a,skin:0xcbb9a2,collar:0xb4c2d4,
    hat:'发髻',rimC:0x9fb3cc,rim:0.6,noProp:true,scale:1.15});
  figure.position.set(-8.5,0,-6); figure.rotation.y=3.05; g.add(figure);
  const crowd=makeCrowd({n:3,rect:[5,-46,5,44],seed:1562,color:0x10151c,rimC:0x8fa4c0,
    rim:0.16,sMin:0.42,sMax:0.6});
  g.add(crowd.mesh);
  const mist=makeMist({n:6,spread:[220,14,110],pos:[0,6,-52],scale:74,color:0x7e93a6,op:0.09});
  g.add(mist.g);
  const rain=makeGlow({n:150,box:[140,28,80],pos:[0,14,-10],color:0xa8bcd0,size:3.4,speed:0.45,rise:1,maxA:0.26,add:false});
  rain.points.renderOrder=3; g.add(rain.points);
  const reedsL=makeForeground({kind:'芦苇',w:30,n:14,d:6,color:0x070a0f,seed:1563,sway:1.1});
  reedsL.g.position.set(-13,-1.2,14); g.add(reedsL.g);
  const reedsR=makeForeground({kind:'芦苇',w:24,n:12,d:6,color:0x070a0f,seed:1564,sway:0.9});
  reedsR.g.position.set(14,-1.1,16); g.add(reedsR.g);
  addLights(g,{c:0x8aa2bc,i:0.34,p:[-40,80,-40]},{c:0x1f2833,i:0.7});
  /* 连线点亮时的游走光点 */
  const pl=new THREE.PointLight(0x9fb8d0,1.5,60); pl.position.set(tips[0].x,tips[0].y,tips[0].z); g.add(pl);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.reveal=Math.min(1,ctl.reveal+dt/2.8);
        ctl.home=Math.min(1,ctl.home+dt/2.4);
      }
      ridge.update(t,0); mist.update(t,k); rain.update(t);
      figure.update(t,k); crowd.update(t); reedsL.update(t,k); reedsR.update(t,k);
      /* 宿鸟：未点击沿航迹巡天，点击后一头投林渐隐 */
      const px=-60+((t*9)%130), py=16+Math.sin(t*1.9)*1.2;
      birds.g.position.set(px+(24-px)*ctl.home,py+(7.5-py)*ctl.home,-30+(-34)*ctl.home);
      birds.mesh.material.opacity=k*(1-ctl.home);
      chain.mat.uniforms.uTime.value=t;
      chain.mat.uniforms.uFade.value=k;
      chain.mat.uniforms.uReveal.value=ctl.reveal;
      const fr=Math.min(tips.length-1.001,ctl.reveal*(tips.length-1));
      const i0=Math.floor(fr), ft=fr-i0;
      pl.position.set(tips[i0].x+(tips[i0+1].x-tips[i0].x)*ft,
        tips[i0].y+(tips[i0+1].y-tips[i0].y)*ft,
        tips[i0].z+(tips[i0+1].z-tips[i0].z)*ft);
      pl.intensity=k*1.5*(0.25+0.75*ctl.reveal*(0.85+0.15*Math.sin(t*2.4)));
      halo.material.opacity=k*(0.30*ctl.home+0.05*Math.sin(t*0.8)*ctl.home);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        pluck(1,0.1,0.12); pluck(3,0.5,0.11); pluck(4,0.95,0.10); pluck(5,1.4,0.09);
        const fl=$('#flash'); fl.textContent='长亭更短亭'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0f141c),hor:C(0x232e3a),bot:C(0x0b0e13),fog:C(0x151d26),fd:0.013,star:0.05,
  moon:new THREE.Vector3(-110,50,-190),ms:0.45,mph:0.2,mhaze:0.12,dirC:C(0x8fa4c4),dirI:0.4,
  dirP:new THREE.Vector3(-30,80,-30),ambC:C(0x232e3a),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.04,build:bCover,
  cam:{f:[0,11,72],t:[0,10,60],lf:[0,12,-60],lt:[0,12,-60]},
  sky:()=>SK({top:C(0x10161f),hor:C(0x242f3b),bot:C(0x0c0f14),fog:C(0x151c25),fd:0.012,star:0.10,
    ms:0.5,moon:new THREE.Vector3(-90,60,-190),
    dirC:C(0x8fa4c0),dirI:0.4,ambC:C(0x212b36),ambI:0.66}) },
{ name:'平林烟织',dwell:17,river:0.05,build:bPinglin,
  cam:{f:[0,6.5,22],t:[0.8,6,18],lf:[7,8.5,-18],lt:[9,8.5,-20]},
  sky:()=>SK({top:C(0x10141d),hor:C(0x2a3140),bot:C(0x0c0f14),fog:C(0x161c26),fd:0.014,star:0.05,
    ms:0.4,mph:0.25,mhaze:0.12,moon:new THREE.Vector3(-150,30,-200),
    dirC:C(0x8fa4c4),dirI:0.38,ambC:C(0x242e3a),ambI:0.68}) },
{ name:'玉阶宿鸟',dwell:15,river:0.03,build:bYuJie,
  cam:{f:[0,5.5,14],t:[-0.5,5,10],lf:[-5.5,4.5,-18],lt:[-6,4.5,-19]},
  sky:()=>SK({top:C(0x0d1118),hor:C(0x1e2733),bot:C(0x0a0d12),fog:C(0x141b23),fd:0.012,star:0.04,
    ms:0.35,mph:0.28,mhaze:0.12,moon:new THREE.Vector3(-150,40,-190),
    dirI:0.36,ambC:C(0x212a35),ambI:0.68}) },
{ name:'长亭短亭',dwell:18,river:0.015,build:bTing,
  cam:{f:[0,7,30],t:[0,6.5,25],lf:[9,5.5,-40],lt:[13,6,-70]},
  sky:()=>SK({top:C(0x0c0f16),hor:C(0x1a222d),bot:C(0x090b10),fog:C(0x131a22),fd:0.012,star:0.03,
    ms:0.3,mph:0.3,mhaze:0.1,moon:new THREE.Vector3(-140,26,-190),
    dirC:C(0x8aa2bc),dirI:0.34,ambC:C(0x1f2833),ambI:0.7}) },
];
"""
