# -*- coding: utf-8 -*-
"""linjiangxian-menghou.py —— 《临江仙·梦后楼台高锁》（宋·晏几道，no.174，水墨夜思）生成配置
三境（queue 分境为准）：梦后楼台（梦断酒醒·帘幕低垂）、落花燕雨（千古名句精雕：落花人独立·微雨燕双飞·初见小苹）、
当时明月（标志性瞬间：旧月犹在·彩云已散；末境点击：双燕掠过独立人影+落花渐积）。
全页冷银水墨，禁金；微雨/双飞燕/落花为动态三要素，月光串起回忆境。"""

META = dict(
    N=3, slug='linjiangxian-menghou', title='临江仙·梦后楼台高锁', dyn='宋 · 晏几道', brand_author='晏几道',
    gold_rgb='164,182,204',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#a4b6cc; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(164,182,204,.26);
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
    tip='轻点画面 / 按空格 —— 双燕掠过独立人影，落花渐积满庭',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看微雨燕飞、落花渐积',
    cover_read='临江仙。宋，晏几道。梦后楼台高锁，酒醒帘幕低垂。去年春恨却来时。落花人独立，微雨燕双飞。记得小苹初见，两重心字罗衣。琵琶弦上说相思。当时明月在，曾照彩云归。',
    cover_p1='三重意境，随词句次第展开：梦断酒醒，楼台高锁、帘幕低垂，去年春恨又到心头；微雨落花里人自独立、燕自双飞，记得小苹初见、两重心字罗衣；琵琶弦上诉说相思，当时明月犹在，曾照彩云的人已如云散去。',
    cover_p2='边读词，边走进这场梦后酒醒的深夜庭院，看旧月照人、燕雨落花里的刻骨相思。',
    end_h2='当时 · 明月', cn_word='三',
    words_js="['再游一次，月下重逢','初识小苹，尚需共读','渐入佳境，再诵几遍','词境渐深，燕雨落花','已解两重心字之意','月曾照处，相思不灭']",
    sky_atmo='0x1c2433',
)

POEM_JS = """const POEM = [
{ name:'梦后楼台', jing:'梦后酒醒，楼台高锁、帘幕低垂 —— 去年春恨，又上心头。（楼台 · 帘幕 · 春恨）',
  segs:[
   {c:'梦后楼台高锁，', p:py('mèng hòu lóu tái gāo suǒ')},
   {c:'酒醒帘幕低垂。', p:py('jiǔ xǐng lián mù dī chuí')},
   {c:'去年春恨却来时。', p:py('qù nián chūn hèn què lái shí')}],
  read:'梦后楼台高锁，酒醒帘幕低垂。去年春恨却来时。',
  yisi:'梦里依稀又回到旧日之地，醒来才见楼台依旧深深锁闭；酒意退去，只余帘幕沉沉低垂。去年春天的离恨，偏偏在此时又涌上心头。——梦留不住、酒也留不住的人与事，被一重楼台、一道帘幕锁在眼前。',
  zhu:[['锁','层层闭锁，写庭院深幽、门禁森严，也锁住了记忆与相思'],['帘幕低垂','帘幕沉沉垂落，写屋宇寂寥、人去楼空'],['春恨','春日伤别的愁恨，指去年与小苹分别之恨'],['却来','再次到来，偏偏又来']] },
{ name:'落花燕雨', jing:'微雨里落花满地，人自独立、燕自双飞 —— 记得小苹初见，两重心字罗衣。（落花 · 双燕 · 罗衣）',
  segs:[
   {c:'落花人独立，', p:py('luò huā rén dú lì')},
   {c:'微雨燕双飞。', p:py('wēi yǔ yàn shuāng fēi')},
   {c:'记得小苹初见，', p:py('jì de xiǎo píng chū jiàn')},
   {c:'两重心字罗衣。', p:py('liǎng chóng xīn zì luó yī')}],
  read:'落花人独立，微雨燕双飞。记得小苹初见，两重心字罗衣。',
  yisi:'纷飞落花之中，人独自伫立；细细微雨里，燕子却成双掠过。还记得与小苹初次相见时，她穿着心字香叠作两重的罗衣。——燕犹双飞，人却独立；衣上心字犹在，同心相许的人已不在眼前。谭献评此十字「千古不能有二」。',
  zhu:[['落花人独立，微雨燕双飞','化用五代翁宏诗句而点铁成金：燕双飞反衬人独立，以乐景写哀，孤寂自见'],['小苹','歌女名。《小山词》自记友人家有莲、鸿、苹、云四位歌女，苹即其一，善琵琶'],['两重心字罗衣','衣领如两个篆体心字相叠的罗衫，喻两心相许；一说罗衣上两处绣有心字'],['重','读 chóng，重叠、层叠']] },
{ name:'当时明月', jing:'琵琶弦上声声相思 —— 当时明月犹在，曾照彩云的人已散如云归。（琵琶 · 明月 · 彩云）',
  segs:[
   {c:'琵琶弦上说相思。', p:py('pí pá xián shàng shuō xiāng sī')},
   {c:'当时明月在，', p:py('dāng shí míng yuè zài')},
   {c:'曾照彩云归。', p:py('céng zhào cǎi yún guī')}],
  read:'琵琶弦上说相思。当时明月在，曾照彩云归。',
  yisi:'而今琵琶弦上，声声都在诉说相思。当时的明月还在天上——它曾照着小苹如彩云般飘然归去。月犹是当时之月，云已散、人已远，唯有弦上相思与旧月同在。',
  zhu:[['琵琶弦上说相思','当年小苹以琵琶传情，如今弦声可闻，弹弦之人已不在'],['当时明月','旧时照过相聚的月亮；月光成为回忆的见证，康有为评此词「情深而语极纯」'],['彩云','喻小苹，如彩云般美好而飘忽，一别之后如云散难寻'],['曾照彩云归','明月曾照她归去；如今月在而云散，物是人非']] }];
const CN = ['壹','贰','叁'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「梦后楼台高锁」的下一句是？', o:['酒醒帘幕低垂','去年春恨却来时','落花人独立'], a:0},
 {q:'「琵琶弦上说相思」的下一句是？', o:['记得小苹初见','当时明月在','微雨燕双飞'], a:1},
 {q:'「两重心字罗衣」中「重」的正确读音和意思是？', o:['zhòng，沉重、贵重','chóng，重叠、层叠','zhòng，重要'], a:1},
 {q:'词中「小苹」指的是？', o:['词人的妹妹','友人家的歌女，善琵琶，与词人曾两心相许','卖酒的邻家女子'], a:1},
 {q:'以「当时明月在，曾照彩云归」作结，全词主要表达的是？', o:['对月色的赞美','月犹在而人已散的刻骨相思与怅惘','豁达超脱的胸怀'], a:1},
];
"""

SCENES_JS = """/* ================= 临江仙·梦后楼台高锁 · 三境场景（水墨夜思：冷银、微雨、双燕、落花） ================= */

/* 微雨：细雨丝程序化粒子（竖直细痕下落 + 微风横移），Normal 混合不吃雾 */
const YU_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uSpeed*(0.72+0.56*fract(aSeed*7.31));
  p.y=mod(position.y-uTime*sp,uBox.y);
  p.x+=sin(uTime*0.8+aSeed*40.0)*0.5;
  vA=smoothstep(0.0,1.2,p.y)*smoothstep(uBox.y,uBox.y-1.6,p.y)*(0.30+0.70*fract(aSeed*13.7));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const YU_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  float d=abs(gl_PointCoord.x-0.5);
  float y=gl_PointCoord.y;
  float a=(1.0-smoothstep(0.06,0.30,d))*smoothstep(0.0,0.22,y)*smoothstep(1.0,0.55,y)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeYu(o){
  o=o||{};
  const n=o.n===undefined?800:o.n, box=o.box||[100,28,64], pos=o.pos||[0,14,-16];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?2.6:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?26:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uColor:{value:C(o.color===undefined?0xaebdd4:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.32:o.maxA}},
    vertexShader:YU_VERT,fragmentShader:YU_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* 落花：飘坠的花瓣粒子（下落 + 随风横摆，越近地面摆幅越大），菱形瓣形 */
const HUA_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uSway;
varying float vA;
void main(){
  vec3 p=position;
  float sp=uSpeed*(0.6+0.8*fract(aSeed*5.17));
  p.y=mod(position.y-uTime*sp,uBox.y);
  float fl=1.0-p.y/uBox.y;
  p.x+=sin(uTime*(0.8+0.6*fract(aSeed*3.3))+aSeed*50.0)*uSway*(0.35+0.65*fl);
  p.z+=cos(uTime*0.6+aSeed*33.0)*0.8*(0.35+0.65*fl);
  vA=smoothstep(0.0,0.5,p.y)*smoothstep(uBox.y,uBox.y-1.2,p.y)*(0.35+0.65*fract(aSeed*13.7));
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(160.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
const HUA_FRAG=`
uniform vec3 uColor; uniform float uFade; uniform float uMaxA; varying float vA;
void main(){
  vec2 q=gl_PointCoord-vec2(0.5);
  float d=abs(q.x)*1.35+abs(q.y);
  float a=smoothstep(0.5,0.16,d)*vA*uFade*uMaxA;
  if(a<0.004) discard;
  gl_FragColor=vec4(uColor,a);
}`;
function makeLuohua(o){
  o=o||{};
  const n=o.n===undefined?110:o.n, box=o.box||[50,15,34], pos=o.pos||[0,8,-11];
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=Math.random()*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=(o.size===undefined?3.4:o.size)*(0.7+Math.random()*0.6);
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:o.speed===undefined?1.15:o.speed},
      uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},uSway:{value:o.sway===undefined?2.4:o.sway},
      uColor:{value:C(o.color===undefined?0xd6c9d2:o.color)},
      uFade:{value:0},uMaxA:{value:o.maxA===undefined?0.5:o.maxA}},
    vertexShader:HUA_VERT,fragmentShader:HUA_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,update(t){m.uniforms.uTime.value=t;}};
}

/* 落花渐积：地面花瓣 InstancedMesh（点击后逐片浮现，prog 0→1 渐积） */
function makeJiluo(o){
  o=o||{};
  const n=o.n===undefined?72:o.n;
  const geo=new THREE.PlaneGeometry(0.60,0.34); geo.rotateX(-Math.PI/2);
  const mat=new THREE.MeshBasicMaterial({color:o.color===undefined?0xc4b6c4:o.color,
    transparent:true,opacity:0.88,depthWrite:false});
  const mesh=new THREE.InstancedMesh(geo,mat,n); mesh.renderOrder=0;
  const R=seedRnd(o.seed===undefined?74:o.seed), dm=new THREE.Object3D(), items=[];
  for(let i=0;i<n;i++){
    const a=R()*6.283, r=Math.sqrt(R())*(o.r===undefined?8.5:o.r);
    items.push({x:(o.x===undefined?-2:o.x)+Math.cos(a)*r, z:(o.z===undefined?-9.5:o.z)+Math.sin(a)*r*0.8,
      ry:R()*6.283, s:0.75+R()*0.8, d:(i/n)*0.5+R()*0.08});
  }
  return {mesh,update(t,k,prog){
    for(let i=0;i<n;i++){
      const it=items[i];
      const e=ease(clamp(prog*1.3-it.d,0,1));
      dm.position.set(it.x,0.03+0.01*e,it.z);
      dm.rotation.set(0,it.ry,0);
      dm.scale.setScalar(Math.max(it.s*e,0.0001));
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* 双飞燕：InstancedMesh 两只（巡飞 / 点击后掠过独立人影的 flyby 航线） */
function makeShuangyan(o){
  o=o||{};
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.13,0.58,5); body.rotateX(Math.PI/2);
  body.translate(0,0,0.06); B.put(body,0x1a2331);
  const head=new THREE.SphereGeometry(0.09,6,5); head.translate(0,0.05,0.34); B.put(head,0x1e2938);
  [1,-1].forEach(function(s){
    const tail=new THREE.ConeGeometry(0.05,0.42,4); tail.rotateX(-Math.PI/2);
    tail.rotateZ(s*0.28); tail.translate(s*0.07,0,-0.44); B.put(tail,0x161f2e);
    const w=new THREE.BufferGeometry();
    w.setAttribute('position',new THREE.BufferAttribute(new Float32Array([
      0,0.04,0.14, 0,0.04,-0.16, s*0.95,0.20,0.02]),3));
    w.computeVertexNormals(); B.put(w,0x202c40);
  });
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060b}),{c:0xbdd0ea,i:0.75,p:2.4});
  const mesh=new THREE.InstancedMesh(mergeGeos(B.list),mat,2);
  mesh.frustumCulled=false;
  const dm=new THREE.Object3D(), off=[-1.7,1.7], sc=o.scale===undefined?1.8:o.scale;
  return {mesh,update(t,k,fb,show){
    for(let i=0;i<2;i++){
      let px,py,pz,yaw;
      if(!show){ dm.position.set(0,-30,0); dm.scale.setScalar(0.0001); }
      else if(fb===null||fb===undefined){
        const a=t*0.32+i*2.9;
        px=Math.cos(a)*15.0; pz=-14+Math.sin(a)*8.5; py=9.0+Math.sin(a*2.1+i)*2.0;
        yaw=Math.atan2(-Math.sin(a)*15.0,Math.cos(a)*8.5);
        dm.position.set(px+off[i],py,pz); dm.scale.setScalar(sc);
      }else if(fb>=1){
        const a=t*0.4+i*2.9;   // 掠过之后：远处天际绕飞（双飞不息）
        px=-24+Math.cos(a)*14.0; pz=-50+Math.sin(a)*12.0; py=18+Math.sin(a*1.7+i)*2.2;
        yaw=Math.atan2(-Math.sin(a)*14.0,Math.cos(a)*12.0);
        dm.position.set(px+off[i],py,pz); dm.scale.setScalar(sc);
      }else{
        const e=ease(clamp(fb,0,1)), u=1-e;
        const p0=[-44,2.0,-2], p1=[-6,8.2,-9], p2=[-34,24,-78];
        px=u*u*p0[0]+2*u*e*p1[0]+e*e*p2[0];
        py=u*u*p0[1]+2*u*e*p1[1]+e*e*p2[1]+Math.sin(t*3+i)*0.25;
        pz=u*u*p0[2]+2*u*e*p1[2]+e*e*p2[2];
        const dx=2*u*(p1[0]-p0[0])+2*e*(p2[0]-p1[0]), dz=2*u*(p1[2]-p0[2])+2*e*(p2[2]-p1[2]);
        yaw=Math.atan2(dx,dz);
        dm.position.set(px+off[i],py,pz); dm.scale.setScalar(sc);
      }
      dm.rotation.set(0,yaw||0,Math.sin(t*11.5+i*1.7)*0.55);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* 楼台：双层楼影 + 四阿顶 + 前廊（高门深锁）+ 上层帘幕低垂，合批 1 mesh + 双帘 */
function makeLou(){
  const B=new GeoBag(), c1=0x0d1219, c2=0x121a26, c3=0x19222f, c4=0x0a0e15;
  const base=new THREE.BoxGeometry(13,1.1,9); base.translate(0,0.55,0); B.put(base,c1);
  const step=new THREE.BoxGeometry(3.6,0.5,1.8); step.translate(0,0.25,5.2); B.put(step,c4);
  const gate=new THREE.BoxGeometry(2.7,3.7,0.5); gate.translate(0,1.1+1.85,2.95); B.put(gate,c4);
  const lock=new THREE.BoxGeometry(0.32,0.44,0.16); lock.translate(0,2.4,3.26); B.put(lock,0x66748c);
  [1,-1].forEach(function(s){
    const ring=new THREE.TorusGeometry(0.15,0.035,6,12); ring.translate(s*0.75,3.1,3.24); B.put(ring,0x59667e);
  });
  const lower=new THREE.BoxGeometry(7.2,5.6,5.6); lower.translate(0,1.1+2.8,0); B.put(lower,c2);
  const lowerRoof=new THREE.ConeGeometry(5.6,1.9,4); lowerRoof.rotateY(Math.PI/4);
  lowerRoof.scale(1.32,1,1.08); lowerRoof.translate(0,6.7+0.95,0); B.put(lowerRoof,c3);
  const deck=new THREE.BoxGeometry(8.6,0.34,3.0); deck.translate(0,7.75,3.4); B.put(deck,c1);
  const rail=new THREE.BoxGeometry(8.6,0.12,0.12); rail.translate(0,8.9,4.8); B.put(rail,c3);
  [1,-1].forEach(function(s){
    const srail=new THREE.BoxGeometry(0.12,0.12,2.8); srail.translate(s*4.25,8.9,3.5); B.put(srail,c3);
  });
  for(let i=0;i<7;i++){
    const post=new THREE.BoxGeometry(0.14,0.95,0.14);
    post.translate(-4.2+i*1.4,8.35,4.8); B.put(post,c3);
  }
  const upper=new THREE.BoxGeometry(5.0,3.8,4.4); upper.translate(0,7.9+1.9,0); B.put(upper,c2);
  const topRoof=new THREE.ConeGeometry(4.6,1.8,4); topRoof.rotateY(Math.PI/4);
  topRoof.scale(1.3,1,1.06); topRoof.translate(0,11.7+0.9,0); B.put(topRoof,c3);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0xa4b6cc,i:0.32,p:2.5})));
  [1,-1].forEach(function(s){
    const cur=makeCurtain({w:1.9,h:2.6,folds:5,color:0x26314a,dark:0x0b0f18,deep:0.5});
    cur.g.position.set(s*1.35,7.9,2.28); g.add(cur.g);
  });
  return {g};
}

/* 小案（水墨冷调，禁金）：案面 + 板足 + 横枨 + 残壶倾杯，合批 1 mesh */
function makeAn(){
  const B=new GeoBag(), wood=0x242a36, wood2=0x1a1f2a;
  const top=new THREE.BoxGeometry(3.4,0.16,1.6); top.translate(0,1.32,0); B.put(top,wood);
  const edge=new THREE.BoxGeometry(3.46,0.05,1.64); edge.translate(0,1.23,0); B.put(edge,shadeColor(wood,1.6));
  [1,-1].forEach(function(s){
    const foot=new THREE.BoxGeometry(0.26,1.24,1.2); foot.translate(s*1.35,0.62,0); B.put(foot,wood2);
  });
  const heng=new THREE.BoxGeometry(2.6,0.10,0.14); heng.translate(0,0.5,0.55); B.put(heng,wood2);
  /* 残酒：案上一壶 + 壶旁倾覆的杯 */
  const pot=new THREE.LatheGeometry([[0,0],[0.22,0.02],[0.30,0.16],[0.26,0.42],[0.14,0.52],[0.13,0.66],[0,0.68]]
    .map(function(p){return new THREE.Vector2(p[0],p[1]);}),12);
  pot.translate(0.9,1.40,-0.2); B.put(pot,0x39404e);
  const cup=new THREE.LatheGeometry([[0,0],[0.13,0.02],[0.16,0.12],[0.12,0.16],[0,0.17]]
    .map(function(p){return new THREE.Vector2(p[0],p[1]);}),10);
  cup.rotateZ(1.35); cup.translate(-0.7,0.28,1.9); B.put(cup,0x434b5c);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
    specular:0x3a465c,emissive:0x05070c}),{c:0xa4b6cc,i:0.24,p:2.4})));
  return {g};
}

/* 琵琶：梨半身槽 + 曲项弦头 + 四弦（弦面微光，「弦上说相思」），2 mesh + 弦光 */
function makePipa(){
  const B=new GeoBag();
  const pts=[[0,0],[0.50,0.06],[0.72,0.34],[0.78,0.72],[0.68,1.10],[0.50,1.42],[0.28,1.62],[0.15,1.74],[0.15,1.80]];
  const body=new THREE.LatheGeometry(pts.map(function(p){return new THREE.Vector2(p[0],p[1]);}),14);
  body.rotateX(Math.PI/2); body.scale(1,0.30,1); body.translate(0,0.16,0); B.put(body,0x3a3038);
  const feng=new THREE.BoxGeometry(0.34,0.10,0.42); feng.translate(0,0.30,1.92); B.put(feng,0x2e262e);
  for(let i=0;i<4;i++){
    const peg=new THREE.CylinderGeometry(0.035,0.035,0.16,5);
    peg.rotateZ(Math.PI/2); peg.translate((i<2?-1:1)*0.22,0.30+(i%2)*0.09,1.92); B.put(peg,0x4a3e46);
  }
  const g=new THREE.Group();
  const bodyMesh=B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:20,
    specular:0x4a5568,emissive:0x06070c}),{c:0xa4b6cc,i:0.30,p:2.5}));
  g.add(bodyMesh);
  const strGeo=new THREE.PlaneGeometry(0.34,1.86); strGeo.rotateX(-Math.PI/2); strGeo.translate(0,0.42,0.75);
  const strMat=new THREE.MeshBasicMaterial({color:0xcfd9ea,transparent:true,opacity:0.5,
    depthWrite:false,side:THREE.DoubleSide});
  const strings=new THREE.Mesh(strGeo,strMat); strings.renderOrder=2; g.add(strings);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xbdd0ea,
    transparent:true,opacity:0.22,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(2.6,2.6,1); glow.position.set(0,0.55,0.4); glow.renderOrder=3; g.add(glow);
  return {g,strMat,glow};
}

function bCover(){ // 封面 · 庭院夜深 —— 高锁楼台初见
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x080b11,c2:0x0f1520});
  grd.mesh.position.y=-0.2; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:20,layers:2,peaks:5,seed:1738,color:0x070a10,atmo:0x1c2433,fogK:0.62,glowK:0.05,y:-14});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  const lou=makeLou(); lou.g.position.set(7,0,-46); lou.g.rotation.y=-0.22; g.add(lou.g);
  const fig=makeFigure({pose:'独立',robe:0x1a2331,belt:0x515d74,skin:0xd0bda6,collar:0xa4b2c8,
    hat:'发髻',rimC:0xa4b6cc,rim:0.44,noProp:true,scale:1.3});
  fig.position.set(2,0,-32); fig.rotation.y=0.25; g.add(fig);
  const fgTree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:1739,sway:1.2,rim:0.16});
  fgTree.g.position.set(15,-0.5,32); g.add(fgTree.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:1740,rim:0.14});
  fgRock.g.position.set(-14,-1.6,36); g.add(fgRock.g);
  const mist=makeMist({n:8,spread:[240,26,140],pos:[0,11,-56],scale:80,color:0x8fa0ba,op:0.085});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[200,36,120],pos:[0,12,-44],color:0xa8b8d0,size:7,speed:0.05,rise:0,maxA:0.34});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c4,i:0.42,p:[-30,80,-40]},{c:0x18202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); mist.update(t,k); motes.update(t);
    fgTree.update(t,k); fgRock.update(t,k);
    fig.userData.update(t,k);
  }};
}

function bMenghou(){ // 一 · 梦后楼台 —— 楼台高锁、帘幕低垂、春恨却来
  const g=new THREE.Group();
  const water=makeWater({size:320,seg:80,amp:0.16,freq:0.20,speed:0.4,flow:[0.12,0.4],spec:1.7,
    deep:0x0a0f18,shallow:0x16202f,skyc:0x1e2c40,moonDir:[40,112,-180]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:18,layers:2,peaks:5,seed:1741,color:0x070a10,atmo:0x1c2433,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-130); g.add(ridge.g);
  /* 楼台高锁（上层双帘低垂）+ 门锁一点冷光 */
  const lou=makeLou(); lou.g.position.set(0,0,-30); g.add(lou.g);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfe0f4,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(4.6,4.6,1); win.position.set(0,9.6,-27.4); win.renderOrder=2; g.add(win);
  /* 酒醒人独立庭中 + 残酒小案 */
  const fig=makeFigure({pose:'独立',robe:0x1c2637,belt:0x55627c,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xa4b6cc,rim:0.50,noProp:true,scale:1.9});
  fig.position.set(-6.5,0,-16); fig.rotation.y=0.5; g.add(fig);
  const an=makeAn(); an.g.position.set(-9.8,0,-13.2); an.g.rotation.y=0.8; g.add(an.g);
  /* 厢廊墙影（庭院深闭） */
  const wallB=new GeoBag(), wc=0x0b0f16;
  [1,-1].forEach(function(s){
    const wl=new THREE.BoxGeometry(11,3.0,1.2); wl.translate(s*13.5,1.5,-27); wallB.put(wl,wc);
    const cap=new THREE.BoxGeometry(11.6,0.22,1.6); cap.translate(s*13.5,3.1,-27); wallB.put(cap,shadeColor(wc,1.5));
    for(let i=0;i<3;i++){
      const col=new THREE.CylinderGeometry(0.20,0.24,3.0,7);
      col.translate(s*(8.5+i*3.4),1.5,-23.5); wallB.put(col,0x0d1119);
    }
  });
  const wall=new THREE.Mesh(mergeGeos(wallB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.18,p:2.4}));
  g.add(wall);
  /* 去年春恨却来：一缕淡雾自远处流向观者 */
  const flow=makeFlow({n:180,box:[120,14,50],pos:[0,10,-40],color:0x9fb0c8,size:20,speed:2.2,maxA:0.20});
  g.add(flow.points);
  const mist=makeMist({n:6,spread:[220,22,120],pos:[0,9,-52],scale:76,color:0x8fa0ba,op:0.075});
  g.add(mist.g);
  const motes=makeGlow({n:56,box:[150,22,80],pos:[0,9,-30],color:0xa8b8d0,size:6,speed:0.05,rise:0,maxA:0.28});
  g.add(motes.points);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:1742,rim:0.14});
  rk.g.position.set(14,-1.5,12); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:24,n:11,d:6,color:0x04060a,seed:1743,sway:0.8});
  reeds.g.position.set(-14,-1.2,11); g.add(reeds.g);
  addLights(g,{c:0x8fa4c4,i:0.46,p:[-30,85,-30]},{c:0x18202e,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); water.update(t); flow.update(t); mist.update(t,k); motes.update(t);
    win.material.opacity=k*(0.15+0.05*Math.sin(t*0.6));
    rk.update(t,k); reeds.update(t,k);
    fig.userData.update(t,k);
  }};
}

function bYanyu(){ // 二 · 落花燕雨（千古名句精雕）—— 人独立、燕双飞、初见小苹
  const g=new THREE.Group();
  const ctl={t:0};
  const water=makeWater({size:340,seg:84,amp:0.15,freq:0.18,speed:0.42,flow:[0.1,0.45],spec:1.45,
    deep:0x0a0f18,shallow:0x182435,skyc:0x22334a,moonDir:[55,118,-175]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:16,layers:2,peaks:4,seed:1744,color:0x070a10,atmo:0x1c2433,fogK:0.60,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-122); g.add(ridge.g);
  /* 庭院矮墙（墙内是当年初见的宴席人影，忆中之景） */
  const wallB=new GeoBag(), wc=0x0b0f16;
  const wl=new THREE.BoxGeometry(32,2.7,1.1); wl.translate(0,1.35,-25); wallB.put(wl,wc);
  const cap=new THREE.BoxGeometry(32.6,0.22,1.5); cap.translate(0,2.8,-25); wallB.put(cap,shadeColor(wc,1.5));
  [1,-1].forEach(function(s){
    const post=new THREE.BoxGeometry(1.1,3.3,1.4); post.translate(s*5,1.65,-24.8); wallB.put(post,shadeColor(wc,1.15));
  });
  const wall=new THREE.Mesh(mergeGeos(wallB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
      specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.16,p:2.4}));
  g.add(wall);
  const crowd=makeCrowd({n:6,rect:[-15,-23,10,2.4],seed:1745,color:0x10151f,rimC:0x8fa4c4,
    rim:0.14,sMin:0.42,sMax:0.60,y:0});
  g.add(crowd.mesh);
  /* 落花人独立 + 微雨燕双飞（动态三要素之三见其二） */
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x586680,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xa4b6cc,rim:0.55,noProp:true,scale:1.95});
  fig.position.set(0,0,-11); fig.rotation.y=-0.35; g.add(fig);
  const yan=makeShuangyan({scale:1.8}); g.add(yan.mesh);
  /* 记得小苹初见：月下忆影（半透明的罗衣身影 + 一环月晕） */
  const ghost=makeFigure({pose:'独立',robe:0x8fa3c2,belt:0xd8e2f0,skin:0xd9c3ae,collar:0xe2eaf6,
    hat:'发髻',rimC:0xa4b6cc,rim:0.55,noProp:true,scale:1.85});
  ghost.position.set(7.5,0,-17); ghost.rotation.y=-0.86; g.add(ghost);
  const ghostMat=ghost.children[0].material; ghostMat.transparent=true;
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xbdd0ea,
    transparent:true,opacity:0.16,depthWrite:false,blending:THREE.AdditiveBlending}));
  halo.scale.set(10,10,1); halo.position.set(7.5,4.6,-18); halo.renderOrder=2; g.add(halo);
  /* 微雨 + 落花（满庭渐积其一） */
  const yu=makeYu({n:850,box:[100,28,64],pos:[0,14,-16],speed:27,size:2.6,maxA:0.34});
  g.add(yu.points);
  const hua=makeLuohua({n:120,box:[50,15,34],pos:[0,8,-11],speed:1.15,sway:2.4,size:3.4,maxA:0.5});
  g.add(hua.points);
  const jiluo=makeJiluo({n:64,x:0,z:-11,r:7.5,seed:1746});
  g.add(jiluo.mesh);
  const fgTree=makeForeground({kind:'树枝',n:2,w:20,d:5,color:0x04060a,seed:1747,sway:1.4,rim:0.16});
  fgTree.g.position.set(14,-0.4,9); g.add(fgTree.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1748,rim:0.14});
  fgRock.g.position.set(-15,-1.8,12); g.add(fgRock.g);
  const mist=makeMist({n:5,spread:[220,22,120],pos:[0,10,-50],scale:74,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  addLights(g,{c:0x8fa4c4,i:0.50,p:[40,90,-30]},{c:0x1a2230,i:0.58});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ctl.t+=dt;
    ridge.update(t,0); water.update(t); mist.update(t,k);
    yu.update(t); hua.update(t); crowd.update(t);
    yan.update(t,k,null,true);
    jiluo.update(t,k,0.30);
    fgTree.update(t,k); fgRock.update(t,k);
    fig.userData.update(t,k);
    ghost.userData.update(t,k);
    ghostMat.opacity=k*(0.34+0.05*Math.sin(t*0.9));
    halo.material.opacity=k*(0.13+0.05*Math.sin(t*0.7));
  }};
}

function bMingyue(){ // 三（标志性瞬间·末境可点击）· 当时明月 —— 旧月犹在、彩云已散；点击：双燕掠过独立人影+落花渐积
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0};
  const water=makeWater({size:340,seg:84,amp:0.14,freq:0.16,speed:0.38,flow:[0.1,0.4],spec:1.55,
    deep:0x0a0f18,shallow:0x1a2638,skyc:0x243652,moonDir:[-45,112,-172]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:15,layers:2,peaks:4,seed:1749,color:0x070a10,atmo:0x1e2636,fogK:0.58,glowK:0.05,y:-15});
  ridge.g.position.set(0,0,-126); g.add(ridge.g);
  /* 当时明月：旧月低悬为唯一主角（ms 2.1），弦上一线相思冷光 */
  const pl=new THREE.PointLight(0xaebfe0,0.9,60); pl.position.set(1,6,-11); g.add(pl);
  /* 独立人影依旧 + 案上琵琶（忆影小苹在案后） */
  const fig=makeFigure({pose:'独立',robe:0x1e2839,belt:0x586680,skin:0xd0bda6,collar:0xaab8cf,
    hat:'发髻',rimC:0xa4b6cc,rim:0.55,noProp:true,scale:1.9});
  fig.position.set(-5,0,-10); fig.rotation.y=0.55; g.add(fig);
  const an=makeAn(); an.g.position.set(3.5,0,-12.2); an.g.rotation.y=-0.35; g.add(an.g);
  const pipa=makePipa(); pipa.g.position.set(3.6,1.47,-12.1); pipa.g.rotation.y=-0.9;
  pipa.g.scale.setScalar(1.15); g.add(pipa.g);
  const ghost=makeFigure({pose:'独立',robe:0x8fa3c2,belt:0xd8e2f0,skin:0xd9c3ae,collar:0xe2eaf6,
    hat:'发髻',rimC:0xa4b6cc,rim:0.5,noProp:true,scale:1.8});
  ghost.position.set(7.2,0,-15.5); ghost.rotation.y=-0.9; g.add(ghost);
  const ghostMat=ghost.children[0].material; ghostMat.transparent=true;
  /* 彩云已散：几缕残云自月旁缓缓流散 */
  const clouds=makeMist({n:5,spread:[70,12,40],pos:[26,30,-92],scale:46,color:0xb4bfda,op:0.075});
  g.add(clouds.g);
  const drift=makeFlow({n:90,box:[80,12,34],pos:[30,30,-94],color:0xa9b6d2,size:22,speed:1.2,maxA:0.13});
  g.add(drift.points);
  /* 微雨仍在 + 落花（点击后渐积）+ 双燕（点击掠过人影） */
  const yu=makeYu({n:520,box:[110,30,70],pos:[0,15,-18],speed:26,size:2.4,maxA:0.22});
  g.add(yu.points);
  const hua=makeLuohua({n:80,box:[54,16,36],pos:[-1,8,-11],speed:1.0,sway:2.2,size:3.2,maxA:0.38});
  g.add(hua.points);
  const jiluo=makeJiluo({n:88,x:-2,z:-9.5,r:8.5,seed:1750});
  g.add(jiluo.mesh);
  const yan=makeShuangyan({scale:1.8}); g.add(yan.mesh);
  const fgTree=makeForeground({kind:'树枝',n:2,w:18,d:5,color:0x04060a,seed:1751,sway:1.3,rim:0.16});
  fgTree.g.position.set(16,-0.5,12); g.add(fgTree.g);
  const fgRock=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1752,rim:0.14});
  fgRock.g.position.set(-15,-1.6,14); g.add(fgRock.g);
  const mist=makeMist({n:5,spread:[220,22,120],pos:[0,10,-52],scale:76,color:0x8fa0ba,op:0.07});
  g.add(mist.g);
  addLights(g,{c:0x9fb0cc,i:0.50,p:[-40,95,-30]},{c:0x1a2232,i:0.6});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const elapsed=ctl.clicked?ctl.t-ctl.clickT:0;
      ridge.update(t,0); water.update(t); mist.update(t,k); clouds.update(t,k); drift.update(t);
      yu.update(t); hua.update(t);
      yan.update(t,k,elapsed/5.2,ctl.clicked);
      jiluo.update(t,k,ctl.clicked?Math.min(1,0.15+elapsed/7.0):0.15);
      fgTree.update(t,k); fgRock.update(t,k);
      fig.userData.update(t,k);
      ghost.userData.update(t,k);
      ghostMat.opacity=k*(0.26+0.05*Math.sin(t*0.8));
      pipa.strMat.opacity=k*(0.34+0.22*Math.abs(Math.sin(t*2.1)));
      pipa.glow.material.opacity=k*(0.16+0.10*Math.abs(Math.sin(t*2.1+0.6)));
      pl.intensity=k*(0.72+0.16*Math.sin(t*1.8));
    },onEnter(){
      pluck(0,0.15,0.12); pluck(2,0.42,0.10); pluck(4,0.70,0.09); pluck(1,1.0,0.08);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(4,0.05,0.13); pluck(2,0.4,0.11); pluck(0,0.8,0.10); pluck(5,1.2,0.09);
        const fl=$('#flash'); fl.textContent='微雨燕飞'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x111825),fd:0.0055,star:0.35,
  moon:new THREE.Vector3(40,112,-180),ms:1.8,mph:0.04,mhaze:0.04,dirC:C(0x8fa4c4),dirI:0.48,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x19202e),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,58],t:[0,9.5,52],lf:[0,11,-38],lt:[0,11,-42]},
  sky:()=>SK({top:C(0x070a12),hor:C(0x151d2b),bot:C(0x080b11),fog:C(0x10161f),fd:0.0050,star:0.38,
    ms:1.7,mph:0.02,moon:new THREE.Vector3(30,105,-185),
    dirC:C(0x8fa4c4),dirI:0.44,ambC:C(0x182031),ambI:0.62}) },
{ name:'梦后楼台',dwell:16,river:0.02,build:bMenghou,
  cam:{f:[0,5.2,17],t:[0.8,5.0,14],lf:[-1,8,-28],lt:[-0.5,7.5,-30]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x161e2c),bot:C(0x090c12),fog:C(0x121926),fd:0.0062,star:0.30,
    ms:1.75,mph:0.04,moon:new THREE.Vector3(40,112,-180),
    dirC:C(0x8fa4c4),dirI:0.46,ambC:C(0x19202e),ambI:0.6}) },
{ name:'落花燕雨',dwell:18,river:0.05,build:bYanyu,
  cam:{f:[0,4.6,18],t:[0,4.4,15],lf:[0,5.2,-11],lt:[0.8,5.0,-13]},
  sky:()=>SK({top:C(0x090c14),hor:C(0x181f2d),bot:C(0x090c11),fog:C(0x131a26),fd:0.0065,star:0.22,
    ms:1.95,mph:0.05,mhaze:0.05,moon:new THREE.Vector3(55,118,-175),
    dirC:C(0x8fa4c4),dirI:0.50,ambC:C(0x1a2230),ambI:0.58}) },
{ name:'当时明月',dwell:20,river:0.03,build:bMingyue,
  cam:{f:[0,5.6,21],t:[0.6,5.2,18],lf:[1.0,4.6,-11],lt:[0.6,5.0,-13]},
  sky:()=>SK({top:C(0x080b13),hor:C(0x171f2e),bot:C(0x090c12),fog:C(0x111825),fd:0.0055,star:0.34,
    ms:2.1,mph:0.08,mhaze:0.04,moon:new THREE.Vector3(-45,112,-172),
    dirC:C(0x9fb0cc),dirI:0.52,ambC:C(0x1a2232),ambI:0.6}) },
];
"""
