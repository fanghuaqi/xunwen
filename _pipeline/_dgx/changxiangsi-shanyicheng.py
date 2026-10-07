# -*- coding: utf-8 -*-
"""changxiangsi-shanyicheng.py —— 《长相思·山一程》（清·纳兰性德，queue no.201，大漠金戈）生成配置
两境（N=queue stages 数）：千帐灯（山一程水一程·榆关夜营·清词第一名画面「夜深千帐灯」）、
故园声（风一更雪一更·聒碎乡心·末境点击「帐灯连绵铺向关外+风雪声起」）。
大漠金戈夜行营色板：底色 #120d08、雾 #1a120a 系、accent=#b8905f（帐灯/灯杆/人物边缘光），
落雪与千帐灯是本页两大视觉系统，灯暖是全页唯一暖色；
「聒碎乡心」的风雪声（末境点击后 ambience 风声渐起）与「故园无此声」的静对照。
标志性瞬间「夜深千帐灯」（境①）：雪原上帐灯成阵如星海，沿廊道铺向榆关城关剪影；
本事：康熙二十一年（1682）纳兰性德以御前侍卫扈从康熙帝东巡祭祖，出山海关夜宿军营。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='changxiangsi-shanyicheng', title='长相思·山一程', dyn='清 · 纳兰性德', brand_author='纳 兰 性 德',
    gold_rgb='184,144,95',
    root=""":root{
  --gold:#b8905f; --ink:#f0e2cc; --dim:#a68d68; --paper:rgba(22,15,9,.6);
  --line:rgba(184,144,95,.3);
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
    tip='轻点画面 / 按空格 —— 帐灯连绵铺向关外，风雪声起',
    hint='← → 键或空格逐境游览 · 末境可点击千帐灯：帐灯连绵铺向关外，风雪声起',
    cover_read='长相思·山一程。清，纳兰性德。山一程，水一程，身向榆关那畔行，夜深千帐灯。风一更，雪一更，聒碎乡心梦不成，故园无此声。',
    cover_p1='两重意境，随词句次第展开：山一程、水一程的扈从长途，身向榆关那畔行的关外夜道，夜深千帐灯的行营灯火；再听风一更、雪一更的帐外风雪，聒碎乡心梦不成的辗转难眠，末了轻轻一叹——故园无此声。',
    cover_p2='边读词，边走进纳兰性德笔下的寒夜行营：千帐灯是天涯的壮阔，故园声是心底的柔软——一壮一柔，都是乡心。',
    end_h2='风雪 · 乡心', cn_word='两',
    words_js="['再游一次，帐下听雪','初识容若，尚需共读','渐入词境，略有所感','乡心渐起，夜雪正紧','已解千帐灯中意','天涯羁旅，梦忆故园']",
    sky_atmo='0x332414',
)

POEM_JS = """const POEM = [
{ name:'千帐灯', jing:'山一程，水一程，身向榆关那畔行，夜深千帐灯。（扈从东巡，夜出榆关：千座营帐的灯火在雪夜里连绵铺向关外——标志性瞬间）',
  segs:[
   {c:'山一程，', p:py('shān yī chéng')},
   {c:'水一程，', p:py('shuǐ yī chéng')},
   {c:'身向榆关那畔行，', p:py('shēn xiàng yú guān nà pàn xíng')},
   {c:'夜深千帐灯。', p:py('yè shēn qiān zhàng dēng')}],
  read:'山一程，水一程，身向榆关那畔行，夜深千帐灯。',
  yisi:'翻过一座山，又蹚过一条河，将士们不辞辛苦地奔向山海关那边。夜已经深了，千万座营帐里都点起了灯。——「一程」「一程」叠用，写出扈从队伍翻山涉水的漫长旅程；「夜深千帐灯」忽然从行路的辛苦中仰起头来，把整个雪夜行营收进五个字里：帐灯如星海铺向关外，天涯的况味与胸中的气象俱在其中，被王国维推为近于「千古壮观」的境界。',
  zhu:[['长相思','词牌名，双调三十六字，上下片各四句，句句用韵'],['程','里程、路途。山一程、水一程：走过一座山，又渡过一道水，叠言路途遥远艰险'],['榆关','即山海关（在今河北秦皇岛），明清时是关内关外的门户'],['那畔','那边、那头。那，读 nà；身向榆关那畔行：队伍向着山海关外行进'],['夜深千帐灯','夜深了，千座营帐灯火齐明。康熙二十一年（1682）春，纳兰性德以御前侍卫扈从康熙帝东巡祭祖，出山海关，夜宿军营，本词即作于此时——王国维称纳兰塞上之作近于「千古壮观」']] },
{ name:'故园声', jing:'风一更，雪一更，聒碎乡心梦不成，故园无此声。（风雪彻夜聒噪，乡心碎而梦不成——故园，没有这样的声音。末境·点击千帐灯：帐灯连绵铺向关外，风雪声起）',
  segs:[
   {c:'风一更，', p:py('fēng yī gēng')},
   {c:'雪一更，', p:py('xuě yī gēng')},
   {c:'聒碎乡心梦不成，', p:py('guō suì xiāng xīn mèng bù chéng')},
   {c:'故园无此声。', p:py('gù yuán wú cǐ shēng')}],
  read:'风一更，雪一更，聒碎乡心梦不成，故园无此声。',
  yisi:'帐篷外，风刮了一更天，雪又下了一更天，嘈杂的风雪声搅碎了思乡的梦——家乡故园，可从来没有这样的声音。上片「一程」「一程」是空间的长，下片「一更」「一更」是时间的长；风雪愈聒噪，乡心愈清晰。「故园无此声」五字轻轻落下，与「夜深千帐灯」一对照：天涯行营的灯再亮再暖，也不及故园静夜里的一声犬吠。',
  zhu:[['更','旧时夜间计时单位，一夜分五更，每更约两小时；风一更、雪一更：风雪彻夜不停。更，读 gēng'],['聒','声音嘈杂吵扰，读 guō；聒碎：嘈杂之声搅碎（乡梦）'],['乡心','思念故乡之心'],['梦不成','想梦回家乡而不得——风雪声太吵，乡梦难成'],['故园','故乡、家园。故园无此声：故园里没有这样的风雪聒噪——以天涯之声反衬故园之静，是全词最柔软的一笔']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「山一程，水一程」的下一句是？', o:['身向榆关那畔行','夜深千帐灯','风一更，雪一更'], a:0},
 {q:'「风一更，雪一更」的下一句是？', o:['故园无此声','聒碎乡心梦不成','夜深千帐灯'], a:1},
 {q:'下列读音与词义解释正确的是？', o:['「聒碎乡心」的「聒」读 guō，指声音嘈杂吵扰；「榆关」即山海关','「夜深千帐灯」的「帐」指蚊帐；「榆关」在甘肃敦煌','「风一更」的「更」读 gèng，指更加；「那畔」的「那」读 nǎ'], a:0},
 {q:'关于这首词的写作本事，下列说法正确的是？', o:['康熙二十一年纳兰性德以御前侍卫扈从康熙帝东巡、出山海关夜宿军营时所作','纳兰性德获罪被贬、独守边关多年时所作','纳兰性德晚年隐居故乡、怀念亡妻时所作'], a:0},
 {q:'「夜深千帐灯」壮阔，「故园无此声」柔软——全词的主旨是？', o:['天涯羁旅的乡思：行营风雪愈壮阔，故园之思愈深切','赞美帝王出巡仪仗的盛大与军威','感叹边关苦寒，埋怨朝廷征战太勤'], a:0},
];
"""

SCENES_JS = """/* ================= 长相思·山一程 · 两境场景（大漠金戈夜行营：千帐灯、故园声） =================
   美术立意：大漠金戈赛道落于雪夜行营——底色 #120d08、雾 #1a120a 系、accent=#b8905f（帐灯/灯杆/人物边缘光），禁艳金。
   落雪与千帐灯是本页两大视觉系统，灯暖是全页唯一暖色；
   境①「夜深千帐灯」壮阔（帐灯成阵铺向榆关），境②「故园无此声」安静（风雪聒噪里的乡心），
   末境点击：帐灯连绵铺向关外 + 风雪声起（ambience 渐强）——以天涯之声反衬故园之静。 */

/* —— 落雪（自写着色器：顶点回绕下落 + 横向风漂；uMaxA 作雪势，uWind 可渐起）—— */
const SNOW_VERT=`
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
  vA=smoothstep(0.0,4.0,fall)*smoothstep(h,h-4.0,fall);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.7+0.3*fract(aSeed*13.7))*(140.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeSnow(o){
  const n=o.n===undefined?300:o.n, box=o.box===undefined?[120,55,80]:o.box, pos=o.pos===undefined?[0,26,-10]:o.pos;
  const color=o.color===undefined?0xe8e4da:o.color, size=o.size===undefined?2.2:o.size;
  const speed=o.speed===undefined?5:o.speed, wind=o.wind===undefined?2.5:o.wind, maxA=o.maxA===undefined?0.7:o.maxA;
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
    vertexShader:SNOW_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 千帐灯灯海（本诗标志性系统）：帐门灯火成阵，沿雪原廊道铺向榆关 ——
   aT=灯在廊道上的位置（0 近营 →1 关前）；uExt=点亮推进度（点击后 0→1，帐灯连绵铺向关外）；
   每灯自带闪烁相位；uFade 显式交给 setFade（ShaderMaterial 双 shader 铁律） */
const CXS_LAMP_VERT=`
attribute float aSeed; attribute float aSize; attribute float aT;
uniform float uTime; uniform float uExt;
varying float vA;
void main(){
  vec3 p=position;
  p.y+=sin(uTime*0.8+aSeed*37.0)*0.05;
  float rev=smoothstep(aT-0.12,aT+0.03,uExt);
  vA=rev*(0.72+0.28*sin(uTime*(1.6+2.6*aSeed)+aSeed*43.0));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const CXS_LAMP_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA;
varying float vA;
void main(){
  float d=length(gl_PointCoord-vec2(0.5));
  float a=smoothstep(0.5,0.10,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeDengdian(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?5217:o.seed);
  const rows=o.rows===undefined?13:o.rows, per=o.per===undefined?18:o.per;
  const z0=o.z0===undefined?-12:o.z0, step=o.step===undefined?8.8:o.step;
  const w0=o.w0===undefined?9:o.w0, spread=o.spread===undefined?1.3:o.spread;
  const n=rows*per;
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n),T=new Float32Array(n);
  let k=0;
  for(let r=0;r<rows;r++){
    const z=z0-step*r+(R()-0.5)*2.2;
    const hw=w0+spread*r;
    for(let i=0;i<per;i++){
      const x=(R()*2-1)*hw+(r%2?1.6:-1.6)+(R()-0.5)*3.0;
      P[k*3]=x; P[k*3+1]=0.8+R()*1.8; P[k*3+2]=z+(R()-0.5)*3.0;
      T[k]=Math.min(1,Math.max(0,(-z+6)/(step*rows+6)));
      S[k]=Math.random(); Z[k]=(3.2+R()*3.4)*(1.0+0.6*T[k]);
      k++;
    }
  }
  const g=new THREE.BufferGeometry();
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  g.setAttribute('aT',new THREE.BufferAttribute(T,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uExt:{value:o.ext===undefined?1:o.ext},uColor:{value:C(0xffb060)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.6:o.maxA}},
    vertexShader:CXS_LAMP_VERT,fragmentShader:CXS_LAMP_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=4;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;},
    setExt(v){m.uniforms.uExt.value=Math.max(0.001,Math.min(1,v));}};
}

/* —— 帐海：行营毡帐 InstancedMesh（1 draw call 摆一片帐阵，随灯阵铺向关外）—— */
function makeZhanghai(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?5219:o.seed);
  const rows=o.rows===undefined?12:o.rows, per=o.per===undefined?16:o.per;
  const z0=o.z0===undefined?-26:o.z0, step=o.step===undefined?8.8:o.step;
  const w0=o.w0===undefined?8:o.w0, spread=o.spread===undefined?1.25:o.spread;
  const prof=[[1.90,0.02],[2.10,0.25],[2.02,0.60],[1.62,0.92],[0.90,1.12],[0.07,1.22]];
  const geo=new THREE.LatheGeometry(prof.map(p=>new THREE.Vector2(p[0],p[1])),8);
  const mesh=new THREE.InstancedMesh(geo,
    rimHook(new THREE.MeshPhongMaterial({color:0x241c11,shininess:4,specular:0x241a10,
      emissive:0x080503}),{c:0xb8905f,i:o.rim===undefined?0.06:o.rim,p:2.6}),rows*per);
  const dm=new THREE.Object3D(); let k=0;
  for(let r=0;r<rows;r++){
    for(let i=0;i<per;i++){
      const x=(R()*2-1)*(w0+spread*r)+0.6*(R()-0.5);
      const z=z0-step*r+(R()-0.5)*2.6;
      const s=(0.85+R()*0.5)*(1-0.42*r/rows);
      dm.position.set(x,0,z); dm.rotation.set(0,R()*6.283,0); dm.scale.setScalar(s);
      dm.updateMatrix(); mesh.setMatrixAt(k++,dm.matrix);
    }
  }
  mesh.frustumCulled=false; mesh.renderOrder=0;
  const g=new THREE.Group(); g.add(mesh);
  g.position.y=o.y===undefined?-1.4:o.y;
  return {g,update(){}};
}

/* —— 毡帐：穹顶毡帐 + 帐门暖光 + 内透光（近景主角帐；帐灯暖是全页唯一暖色）—— */
function makeZhanzhang(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?5211:o.seed);
  const sc=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const prof=[[1.62,0.02],[1.80,0.12],[1.88,0.38],[1.84,0.78],[1.62,1.20],[1.24,1.56],[0.80,1.82],[0.38,1.96],[0.08,2.04]];
  B.put(new THREE.LatheGeometry(prof.map(p=>new THREE.Vector2(p[0],p[1])),16),
    shadeColor(0x40321e,0.8+0.4*R()));
  const fin=new THREE.CylinderGeometry(0.03,0.055,0.55,6); fin.translate(0,2.28,0); B.put(fin,0x2a1f12);
  const lintel=new THREE.BoxGeometry(0.92,0.10,0.12); lintel.translate(0,1.52,1.70); B.put(lintel,0x241a10);
  for(let i=0;i<3;i++){
    const a=i/3*6.283+R();
    const rope=new THREE.CylinderGeometry(0.018,0.018,2.3,4);
    rope.rotateZ(1.05); rope.rotateY(a); rope.translate(Math.sin(a)*-0.2,1.0,Math.cos(a)*-0.2);
    B.put(rope,0x2a2013);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x2a2016,emissive:0x0a0704}),{c:0xb8905f,i:0.16,p:2.6})));
  const door=new THREE.Mesh(new THREE.PlaneGeometry(0.68,1.30),
    new THREE.MeshBasicMaterial({color:0xffb45c,transparent:true,opacity:0.85,depthWrite:false}));
  door.position.set(0,0.72,1.66); door.renderOrder=2; g.add(door);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
    transparent:true,opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(5.2,4.2,1); glow.position.set(0,1.2,2.0); glow.renderOrder=3; g.add(glow);
  let light=null,baseI=0;
  if(o.light){ light=new THREE.PointLight(0xffa050,o.light,o.lightD===undefined?26:o.lightD);
    light.position.set(0,1.3,1.2); g.add(light); baseI=o.light; }
  g.scale.setScalar(sc);
  const ph=R()*6.283;
  g.update=function(t,fk){ const k=fk===undefined?1:fk;
    door.material.opacity=k*0.85*(0.70+0.18*Math.sin(t*2.9+ph)+0.10*Math.sin(t*7.1+ph*2.3));
    glow.material.opacity=k*0.30*(0.80+0.20*Math.sin(t*4.3+ph));
    if(light)light.intensity=k*baseI*(0.84+0.16*Math.sin(t*5.1+ph));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 榆关（山海关）城关剪影：城垣+双塔楼+垛口+门洞，立在雪原尽头的丘冈上—— */
function makeYuguan(o){
  o=o||{};
  const sc=o.scale===undefined?1:o.scale;
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(30,7.5,7); wall.translate(0,2.9,0); B.put(wall,0x141009);
  const gate=new THREE.BoxGeometry(5.2,4.6,7.4); gate.translate(0,1.6,0); B.put(gate,0x050302);
  [-16.5,16.5].forEach(function(px){
    const tw=new THREE.BoxGeometry(7.5,11.5,7.5); tw.translate(px,5.0,0); B.put(tw,0x17120b);
    const rf=new THREE.ConeGeometry(6.0,2.6,4); rf.rotateY(Math.PI/4); rf.translate(px,12.1,0); B.put(rf,0x1b150c);
  });
  for(let i=0;i<9;i++){
    const c=new THREE.BoxGeometry(1.1,1.0,1.0); c.translate(-12+i*3,7.2,3.2); B.put(c,0x120e08);
  }
  const mound=rockGeo(16,1,seedRnd(o.seed===undefined?5213:o.seed));
  mound.scale(2.2,0.5,1.4); mound.translate(0,-3.6,-2); B.put(mound,0x0d0a06);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x201810,emissive:0x060403}),{c:0xb8905f,i:0.14,p:2.8})));
  /* 关门口一点暖光：千帐灯铺向关外的明亮终点 */
  const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffb45c,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  gl.scale.set(8,5.5,1); gl.position.set(0,3.4,4.2); gl.renderOrder=3; g.add(gl);
  g.scale.setScalar(sc);
  return g;
}

/* —— 营旗：旗杆+杆顶+暗赭黄旗面（清行营旗色，风雪中猎猎）—— */
function makeYingqi(o){
  o=o||{};
  const h=o.h===undefined?7:o.h, ph=o.ph===undefined?0:o.ph;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.07,0.10,h,6); pole.translate(0,h/2,0); B.put(pole,0x0d0a07);
  const fin=new THREE.SphereGeometry(0.14,8,6); fin.translate(0,h+0.08,0); B.put(fin,0x6a5030);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:4,
    specular:0x1d160e,emissive:0x040302}),{c:0xb8905f,i:0.18,p:2.6})));
  const fl=new THREE.Mesh(new THREE.PlaneGeometry(2.5,1.55,5,2),
    new THREE.MeshPhongMaterial({color:o.flagC===undefined?0x4a3413:o.flagC,side:THREE.DoubleSide,
      shininess:6,specular:0x3a2c14,emissive:0x0d0903}));
  fl.position.set(1.25,h-1.05,0); g.add(fl);
  const amp=o.amp===undefined?0.5:o.amp;
  return {g,fl,update(t){ fl.rotation.y=amp*Math.sin(t*1.7+ph)+0.18*Math.sin(t*3.1+ph*1.7); }};
}

/* —— 杆灯：灯杆挑一盏灯笼（帐外立灯，暖是全页唯一暖色）—— */
function makeGandeng(o){
  o=o||{};
  const h=o.h===undefined?4.4:o.h;
  const B=new GeoBag();
  const pole=new THREE.CylinderGeometry(0.05,0.08,h,6); pole.translate(0,h/2,0); B.put(pole,0x14100a);
  const arm=new THREE.CylinderGeometry(0.035,0.035,1.1,6); arm.rotateZ(Math.PI/2); arm.translate(0.42,h-0.12,0); B.put(arm,0x14100a);
  const base=new THREE.CylinderGeometry(0.22,0.30,0.18,8); base.translate(0,0.09,0); B.put(base,0x1a140c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a2016,emissive:0x060403}),{c:0xb8905f,i:0.18,p:2.6})));
  const lt=makeLantern(o.ls===undefined?0.5:o.ls,{flick:1});
  lt.position.set(0.82,h-0.75,0); g.add(lt);
  let light=null,baseI=0;
  if(o.light){ light=new THREE.PointLight(0xffa050,o.light,o.lightD===undefined?20:o.lightD);
    light.position.set(0.82,h-0.8,0); g.add(light); baseI=o.light; }
  g.update=function(t,fk){ const k=fk===undefined?1:fk;
    lt.update(t,k);
    if(light)light.intensity=k*baseI*(0.88+0.12*Math.sin(t*6.3));
  };
  g.userData.update=g.update;
  return g;
}

function bCoverCxs(){ // 卷首 · 雪夜行营远景：千帐灯如星海，铺向榆关
  const g=new THREE.Group();
  const grd=makeGround({r:300,c1:0x181410,c2:0x252017,y:-2.0}); g.add(grd.mesh);
  const ridge=makeRange({r:340,h:22,layers:3,peaks:5,seed:5201,color:0x0b0805,atmo:0x332414,fogK:0.60,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-60); g.add(ridge.g);
  const guan=makeYuguan({scale:1.1,seed:5203}); guan.position.set(0,-1.2,-150); g.add(guan);
  const zhai=makeZhanghai({rows:10,per:13,z0:-30,step:9.8,w0:8,spread:1.35,y:-2.0,seed:5205}); g.add(zhai.g);
  const deng=makeDengdian({rows:12,per:18,z0:-22,step:9.2,w0:9,spread:1.35,maxA:0.45,ext:1,seed:5207});
  deng.points.position.y=-2.0; g.add(deng.points);
  const ntent=makeZhanzhang({seed:5206,scale:1.35}); ntent.position.set(-10,-2.0,-3); ntent.rotation.y=0.5; g.add(ntent);
  const snow=makeSnow({n:260,box:[200,58,120],pos:[0,27,-30],speed:3.8,wind:2.0,maxA:0.38});
  g.add(snow.points);
  const mist=makeMist({n:10,spread:[300,28,150],pos:[0,10,-90],scale:90,color:0x6a5a44,op:0.11});
  g.add(mist.g);
  const flow=makeFlow({n:120,box:[240,14,100],pos:[0,8,-60],color:0x8a7a64,size:18,speed:5,maxA:0.10});
  g.add(flow.points);
  const guard=makeFigure({pose:'独立',robe:0x201810,belt:0x5a4226,hat:'幞头',scale:0.7,rim:0.5,rimC:0xb8905f});
  guard.position.set(6,-2.0,16); guard.rotation.y=Math.PI-0.5; g.add(guard);
  const sentry=makeCrowd({n:8,rect:[-26,-40,52,22],color:0x191309,rimC:0xb8905f,rim:0.16,sMin:0.55,sMax:0.80,y:-2.0,seed:5209});
  g.add(sentry.mesh);
  const fgT=makeForeground({kind:'树枝',w:22,n:6,d:5,color:0x0c0906,seed:5211,sway:0.8});
  fgT.g.position.set(-17,-2.2,26); g.add(fgT.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:3.2,w:12,d:6,color:0x0b0805,seed:5212,rim:0.10,rimC:0xb8905f});
  fgR.g.position.set(15,-4.2,20); g.add(fgR.g);
  addLights(g,{c:0xc09058,i:0.30,p:[-50,55,-20]},{c:0x33281a,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); zhai.update(t); deng.update(t); snow.update(t); flow.update(t);
    mist.update(t,k); fgT.update(t,k); fgR.update(t,k); guard.update(t,k); sentry.update(t);
  }};
}
function bDengying(){ // 一（标志性瞬间）· 千帐灯 —— 夜深千帐灯：帐灯如星海，铺向榆关
  const g=new THREE.Group();
  const grd=makeGround({r:300,c1:0x181410,c2:0x272117,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:320,h:20,layers:2,peaks:5,seed:5215,color:0x0b0805,atmo:0x3a2a16,fogK:0.60,glowK:0.06,glow:0xd8b088,y:-14});
  ridge.g.position.set(0,0,-40); g.add(ridge.g);
  const guan=makeYuguan({scale:1.35,seed:5213}); guan.position.set(0,-0.6,-128); g.add(guan);
  /* 帐海（中远景）+ 灯海：夜深千帐灯 */
  const zhai=makeZhanghai({rows:12,per:13,z0:-26,step:9.6,w0:8,spread:1.25,y:-1.4,seed:5219});
  g.add(zhai.g);
  const deng=makeDengdian({rows:14,per:18,z0:-12,step:8.8,w0:11,spread:1.3,maxA:0.55,ext:1,seed:5217});
  deng.points.position.y=-1.4; g.add(deng.points);
  /* 近营三帐 + 灯杆 */
  const t1=makeZhanzhang({seed:5221}); t1.position.set(-8.5,-1.4,-4); t1.rotation.y=0.55; g.add(t1);
  const t2=makeZhanzhang({seed:5222}); t2.position.set(9.5,-1.4,-7); t2.rotation.y=-0.7; g.add(t2);
  const t3=makeZhanzhang({seed:5223,light:1.1,lightD:30}); t3.position.set(1.5,-1.4,-19); t3.rotation.y=0.1; g.add(t3);
  const gand=makeGandeng({light:0.9}); gand.position.set(-5.5,-1.4,3.5); g.add(gand);
  /* 词人按剑立在中军帐前（御前侍卫扈从东巡）+ 帐前士卒 */
  const poet=makeFigure({pose:'按剑',robe:0x241c12,belt:0x6a4e2e,hat:'幞头',scale:1.4,rim:0.62,rimC:0xb8905f});
  poet.position.set(-1.5,-1.4,1.5); poet.rotation.y=Math.PI-0.15; g.add(poet);
  const army=makeCrowd({n:22,rect:[-22,-10,44,13],color:0x191309,rimC:0xb8905f,rim:0.20,sMin:0.80,sMax:1.05,y:-1.4,seed:5225});
  g.add(army.mesh);
  /* 营旗两面 */
  const q1=makeYingqi({h:7.2,ph:0.3}); q1.g.position.set(-13,-1.4,-9); g.add(q1.g);
  const q2=makeYingqi({h:6.4,ph:2.6}); q2.g.position.set(12.5,-1.4,-13); g.add(q2.g);
  /* 落雪 + 风雪横流 + 低雾 */
  const snow=makeSnow({n:300,box:[180,55,110],pos:[0,26,-30],speed:4.2,wind:2.2,maxA:0.48});
  g.add(snow.points);
  const flow=makeFlow({n:150,box:[210,12,80],pos:[0,6,-45],color:0x8a7a64,size:16,speed:5,maxA:0.10});
  g.add(flow.points);
  const mist=makeMist({n:8,spread:[270,22,120],pos:[0,8,-80],scale:80,color:0x6a5a44,op:0.10});
  g.add(mist.g);
  /* 前景：枯枝 + 坡石框景 */
  const fgT=makeForeground({kind:'树枝',w:20,n:7,d:5,color:0x0c0906,seed:5227,sway:0.9});
  fgT.g.position.set(-15,-1.8,14); g.add(fgT.g);
  const fgR=makeForeground({kind:'坡石',n:2,r:3.4,w:12,d:6,color:0x0b0805,seed:5228,rim:0.10,rimC:0xb8905f});
  fgR.g.position.set(14,-3.2,17); g.add(fgR.g);
  addLights(g,{c:0xc09058,i:0.34,p:[-50,55,-20]},{c:0x33281a,i:0.55});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); zhai.update(t); deng.update(t); snow.update(t); flow.update(t);
    t1.update(t,k); t2.update(t,k); t3.update(t,k); gand.update(t,k);
    poet.update(t,k); army.update(t); q1.update(t); q2.update(t);
    mist.update(t,k); fgT.update(t,k); fgR.update(t,k);
  }};
}
function bFengxue(){ // 二（末境·可点击）· 故园声 —— 风一更雪一更：点击千帐灯，帐灯连绵铺向关外，风雪声起
  const ctl={t:0,clicked:false,ext:0.02,wind:4.5,last:0};
  const g=new THREE.Group();
  const grd=makeGround({r:300,c1:0x161210,c2:0x231d14,y:-1.4}); g.add(grd.mesh);
  const ridge=makeRange({r:320,h:20,layers:2,peaks:5,seed:5231,color:0x0a0704,atmo:0x2c2013,fogK:0.62,glowK:0.04,y:-14});
  ridge.g.position.set(0,0,-40); g.add(ridge.g);
  const guan=makeYuguan({scale:1.35,seed:5233}); guan.position.set(0,-0.8,-128); g.add(guan);
  /* 中远景帐海剪影（风雪夜昏暗）+ 灯阵（点击后铺向关外） */
  const zhai=makeZhanghai({rows:12,per:13,z0:-26,step:9.6,w0:8,spread:1.25,y:-1.4,seed:5235,rim:0.06});
  g.add(zhai.g);
  const deng=makeDengdian({rows:14,per:18,z0:-12,step:8.8,w0:11,spread:1.3,maxA:0.50,ext:0.02,seed:5237});
  deng.points.position.y=-1.4; g.add(deng.points);
  /* 主帐（词人之帐）+ 帐前风雪独立的词人 + 火盆 */
  const tent=makeZhanzhang({seed:5239,light:1.3,lightD:34,scale:2.2});
  tent.position.set(6.5,-1.4,-6); tent.rotation.y=-0.55; g.add(tent);
  const poet=makeFigure({pose:'独立',robe:0x221a10,belt:0x5a4226,hat:'发髻',scale:1.35,rim:0.66,rimC:0xb8905f});
  poet.position.set(2.6,-1.4,-1.2); poet.rotation.y=Math.PI+0.35; g.add(poet);
  const bz=makeBrazier({r:0.85,fh:1.9,fw:0.95,light:1.0,lightD:34,embers:20});
  bz.g.position.set(-4.5,-1.4,-2.5); g.add(bz.g);
  /* 远哨 + 营旗 */
  const sentry=makeCrowd({n:4,rect:[-30,-30,12,10],color:0x18120a,rimC:0xb8905f,rim:0.14,sMin:0.80,sMax:0.95,y:-1.4,seed:5241});
  g.add(sentry.mesh);
  const q1=makeYingqi({h:7.0,ph:1.2,flagC:0x5a3f18,amp:0.7}); q1.g.position.set(-14,-1.4,-16); g.add(q1.g);
  /* 风雪更急（雪一更：雪势/风速都比境①大；点击后风声再起） */
  const snow=makeSnow({n:430,box:[190,62,120],pos:[0,28,-25],speed:5.2,wind:4.5,maxA:0.72});
  g.add(snow.points);
  const flow=makeFlow({n:220,box:[240,16,100],pos:[0,7,-40],color:0x9a8a72,size:20,speed:6.5,maxA:0.15});
  g.add(flow.points);
  const mist=makeMist({n:9,spread:[270,24,130],pos:[0,7,-70],scale:84,color:0x5f5240,op:0.12});
  g.add(mist.g);
  /* 前景：坡石 + 枯枝 */
  const fgR=makeForeground({kind:'坡石',n:2,r:3.2,w:12,d:6,color:0x0b0805,seed:5243,rim:0.10,rimC:0xb8905f});
  fgR.g.position.set(12,-2.8,12.5); g.add(fgR.g);
  const fgT=makeForeground({kind:'树枝',w:22,n:7,d:5,color:0x0c0906,seed:5244,sway:1.1});
  fgT.g.position.set(-13,-1.8,12); g.add(fgT.g);
  addLights(g,{c:0xa87848,i:0.24,p:[-40,50,-15]},{c:0x2c2216,i:0.50});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked){
        ctl.ext=Math.min(1,ctl.ext+dt/4.0);        // 帐灯连绵，铺向关外
        ctl.wind=Math.min(10,ctl.wind+dt*3.5);      // 风雪声势渐起
      }
      deng.setExt(ctl.ext);
      snow.mat.uniforms.uWind.value=ctl.wind;
      ridge.update(t,0); zhai.update(t); deng.update(t); snow.update(t); flow.update(t);
      tent.update(t,k); bz.update(t,k); poet.update(t,k); sentry.update(t); q1.update(t);
      mist.update(t,k); fgR.update(t,k); fgT.update(t,k);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.2)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      setAmbience(0.5);                             // 风雪声起（故园无此声）
      pluck(0,0.0,0.10); pluck(2,0.4,0.09); pluck(4,0.85,0.08); pluck(5,1.3,0.07);
      const fl=$('#flash'); fl.textContent='故园无此声'; fl.classList.remove('go');
      void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x0d0a07),hor:C(0x2a1d10),bot:C(0x0a0705),fog:C(0x1a120a),fd:0.0056,star:0.26,
  moon:new THREE.Vector3(-70,22,-215),ms:0.55,mph:0,mhaze:0.10,dirC:C(0xc09058),dirI:0.34,
  dirP:new THREE.Vector3(-50,55,-20),ambC:C(0x33281a),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverCxs,
  cam:{f:[0,9.5,70],t:[0,9,58],lf:[0,4.5,-60],lt:[0,6,-90]},
  sky:()=>SK({fd:0.0052,star:0.24,hor:C(0x332414),ms:0.5,mhaze:0.08,moon:new THREE.Vector3(-80,20,-210),dirI:0.30}) },
{ name:'千帐灯',dwell:17,river:0.02,build:bDengying,
  cam:{f:[0,6.5,36],t:[0,5.6,28],lf:[0,4.5,-40],lt:[0,5.5,-75]},
  sky:()=>SK({fd:0.0062,star:0.30,hor:C(0x332414),ms:0.55,mhaze:0.10,dirC:C(0xc89860),dirI:0.36,ambI:0.56}) },
{ name:'故园声',dwell:18,river:0.045,build:bFengxue,
  cam:{f:[4,5.2,18],t:[-1,4.6,13],lf:[-2,3.2,-12],lt:[0.5,3.6,-32]},
  sky:()=>SK({fd:0.0068,star:0.10,hor:C(0x241a10),ms:0.32,mhaze:0.16,dirC:C(0xa87848),dirI:0.24,ambI:0.50}) },
];
"""
