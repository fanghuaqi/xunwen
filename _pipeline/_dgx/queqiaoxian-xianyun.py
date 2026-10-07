# -*- coding: utf-8 -*-
"""queqiaoxian-xianyun.py —— 《鹊桥仙·纤云弄巧》（宋·秦观，no.182，水墨夜思·星海变体）生成配置
两境：银汉暗度（纤云/飞星/双星两岸相望）、鹊桥久长（标志性瞬间，点击鹊桥：鹊鸟搭桥横跨银汉+双星渐近）
全页主景是银河/星海：斜贯天际的星河带 + 云海上的星河光路；冷月作伴，禁金。"""

META = dict(
    N=2, slug='queqiaoxian-xianyun', title='鹊桥仙·纤云弄巧', dyn='宋 · 秦观', brand_author='秦 观',
    gold_rgb='173,192,216',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#adc0d8; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(173,192,216,.26);
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
    tip='轻点画面 / 按空格 —— 鹊鸟搭桥横跨银汉，双星渐近相会',
    hint='← → 键或空格逐境游览 · 末境可点击鹊桥，看鹊鸟搭桥、双星渐近',
    cover_read='鹊桥仙。宋，秦观。纤云弄巧，飞星传恨，银汉迢迢暗度。金风玉露一相逢，便胜却人间无数。柔情似水，佳期如梦，忍顾鹊桥归路。两情若是久长时，又岂在朝朝暮暮。',
    cover_p1='两重意境，随词句次第展开：纤云弄巧、飞星传恨，迢迢银汉里双星暗度，金风玉露一相逢，便胜却人间无数；柔情似水、佳期如梦，末了鹊鸟搭桥横跨银汉，两情久长，又岂在朝朝暮暮。',
    cover_p2='边读词，边走上七夕的星河之畔，看一场胜却人间无数的相逢。',
    end_h2='两情 · 久长', cn_word='两',
    words_js="['再游一次，云汉同渡','初识鹊仙，尚需共读','渐入佳境，再诵几遍','词境渐深，星河生辉','已解金风玉露之意','两情久长，不负朝暮']",
    sky_atmo='0x1c2536',
)

POEM_JS = """const POEM = [
{ name:'银汉暗度', jing:'纤云弄巧，飞星传恨 —— 银汉迢迢，双星隔岸暗度。（星河 · 飞星 · 双星）',
  segs:[
   {c:'纤云弄巧，', p:py('xiān yún nòng qiǎo')},
   {c:'飞星传恨，', p:py('fēi xīng chuán hèn')},
   {c:'银汉迢迢暗度。', p:py('yín hàn tiáo tiáo àn dù')},
   {c:'金风玉露一相逢，', p:py('jīn fēng yù lù yī xiāng féng')},
   {c:'便胜却人间无数。', p:py('biàn shèng què rén jiān wú shù')}],
  read:'纤云弄巧，飞星传恨，银汉迢迢暗度。金风玉露一相逢，便胜却人间无数。',
  yisi:'纤薄的云彩在天际变幻出精巧的花样，飞驰的流星传递着牛郎织女的离恨。迢迢银河两岸，两人悄悄渡河相会——这一夜金风玉露里的相逢，便抵过了人间无数寻常的相聚。——以天上之一夜，胜人间之无数。',
  zhu:[['纤云','纤薄的云彩；弄巧：变幻出精巧花样，暗合七夕「乞巧」之意'],['飞星','划过天际的流星，仿佛为双星传递离恨的使者'],['银汉','银河，天河；迢迢：遥远的样子'],['暗度','悄悄渡过，七夕之夜牛郎织女渡银河相会'],['金风玉露','秋风白露，点明七夕时节，亦喻相逢之清贵']] },
{ name:'鹊桥久长', jing:'柔情似水，佳期如梦 —— 点击鹊桥，看鹊鸟搭桥横跨银汉，双星渐近。（鹊桥 · 双星 · 久长）',
  segs:[
   {c:'柔情似水，', p:py('róu qíng sì shuǐ')},
   {c:'佳期如梦，', p:py('jiā qī rú mèng')},
   {c:'忍顾鹊桥归路。', p:py('rěn gù què qiáo guī lù')},
   {c:'两情若是久长时，', p:py('liǎng qíng ruò shì jiǔ cháng shí')},
   {c:'又岂在朝朝暮暮。', p:py('yòu qǐ zài zhāo zhāo mù mù')}],
  read:'柔情似水，佳期如梦，忍顾鹊桥归路。两情若是久长时，又岂在朝朝暮暮。',
  yisi:'温柔缱绻的情意如银河之水绵绵不绝，重逢的佳期恍惚如梦、短暂将尽，怎忍心回头看那鹊桥上的归路？——然而两人的情意若是长久坚贞，又何必贪求朝朝暮暮的相守。',
  zhu:[['柔情似水','情意温柔缠绵，如银河之水绵长不绝'],['佳期如梦','相会之期美好而短暂，恍惚如梦'],['忍顾','怎忍回头看；忍：岂忍'],['鹊桥','七夕之夜喜鹊搭成的桥，渡牛郎织女相会'],['朝朝暮暮','日日夜夜，指朝夕相守；朝读 zhāo']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「纤云弄巧，飞星传恨」的下一句是？', o:['银汉迢迢暗度','金风玉露一相逢','便胜却人间无数'], a:0},
 {q:'「两情若是久长时」的下一句是？', o:['又岂在朝朝暮暮','忍顾鹊桥归路','柔情似水，佳期如梦'], a:0},
 {q:'「银汉迢迢暗度」中「度」的正确读音和意思是？', o:['duó，推测、估量','dù，渡过、越过','dù，温度的度'], a:1},
 {q:'「鹊桥」的传说与下列哪个节日相关？', o:['元宵节','中秋节','七夕（农历七月初七）'], a:2},
 {q:'「两情若是久长时，又岂在朝朝暮暮」表达的爱情观是？', o:['朝夕厮守才是真爱','两情长久坚贞，何必贪求朝暮相守','离别之后不必再相见'], a:1},
];
"""

SCENES_JS = """/* ================= 鹊桥仙 · 两境场景（水墨夜思·星海变体：银汉暗度、鹊桥久长） ================= */

/* 银河带：斜贯天际的星河（fbm 星云 + 双层星点 + 中缝暗隙），additive 不吃雾 */
const YH_VERT=`varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }`;
const YH_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
float hash(vec2 p){ return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453); }
float vnoise(vec2 p){ vec2 i=floor(p),f=fract(p); f=f*f*(3.0-2.0*f);
  return mix(mix(hash(i),hash(i+vec2(1.0,0.0)),f.x),mix(hash(i+vec2(0.0,1.0)),hash(i+vec2(1.0,1.0)),f.x),f.y); }
float fbm(vec2 p){ float v=0.0,a=0.5; for(int i=0;i<4;i++){ v+=a*vnoise(p); p=p*2.17+vec2(3.1,1.7); a*=0.5; } return v; }
float stars(vec2 uv,float n,float thr){
  vec2 g=uv*n; vec2 id=floor(g); vec2 f=fract(g)-0.5;
  vec2 off=vec2(hash(id+1.3),hash(id+2.7))-0.5;
  float r=length(f-off*0.55);
  return smoothstep(0.16,0.0,r)*step(thr,hash(id))*(0.35+0.65*hash(id+4.1));
}
void main(){
  vec2 uv=vUv;
  float lane=exp(-pow((uv.y-0.5)*3.6,2.0));
  float rift=0.35+0.65*smoothstep(0.05,0.30,abs(uv.y-0.5));
  float neb=fbm(uv*vec2(6.0,2.2)+vec2(uTime*0.006,0.0));
  float neb2=fbm(uv*vec2(11.0,4.0)-vec2(uTime*0.004,2.0));
  float glowA=lane*rift*(0.30+0.95*neb)*(0.40+0.60*neb2);
  float st=stars(uv+vec2(0.13,0.0),95.0,0.68)+0.65*stars(uv+vec2(0.51,0.0),170.0,0.78);
  float tw=0.72+0.28*sin(uTime*1.6+hash(floor(uv*95.0))*40.0);
  vec3 col=mix(vec3(0.30,0.40,0.62),vec3(0.66,0.76,0.92),clamp(glowA*1.4,0.0,1.0));
  float a=(glowA*0.72+st*tw*lane*rift)*uK;
  gl_FragColor=vec4(col*(0.36+glowA*1.05+st*tw*1.5), a*uFade);
}`;
function makeYinhan(o){
  o=o||{};
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.k===undefined?1:o.k}},
    vertexShader:YH_VERT,fragmentShader:YH_FRAG});
  const mesh=new THREE.Mesh(new THREE.PlaneGeometry(o.w===undefined?410:o.w,o.h===undefined?150:o.h,1,1),mat);
  mesh.renderOrder=o.order===undefined?-5:o.order; mesh.frustumCulled=false;
  return {mesh,mat,update(t){ mat.uniforms.uTime.value=t; }};
}

/* 星河光路：云海上一条流向天际的星河（与天上银河带相接），additive 不吃雾 */
const XH_FRAG=`
uniform float uTime; uniform float uFade; uniform float uK; varying vec2 vUv;
float hash(vec2 p){ return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453); }
float vnoise(vec2 p){ vec2 i=floor(p),f=fract(p); f=f*f*(3.0-2.0*f);
  return mix(mix(hash(i),hash(i+vec2(1.0,0.0)),f.x),mix(hash(i+vec2(0.0,1.0)),hash(i+vec2(1.0,1.0)),f.x),f.y); }
float fbm(vec2 p){ float v=0.0,a=0.5; for(int i=0;i<4;i++){ v+=a*vnoise(p); p=p*2.17+vec2(3.1,1.7); a*=0.5; } return v; }
float stars(vec2 uv,float n,float thr){
  vec2 g=uv*n; vec2 id=floor(g); vec2 f=fract(g)-0.5;
  vec2 off=vec2(hash(id+1.3),hash(id+2.7))-0.5;
  float r=length(f-off*0.55);
  return smoothstep(0.10,0.0,r)*step(thr,hash(id))*(0.35+0.65*hash(id+4.1));
}
void main(){
  vec2 uv=vUv;
  float cx=abs(uv.x-0.5)*2.0+(fbm(vec2(uv.y*1.4,uTime*0.02))-0.5)*0.5;
  float edge=smoothstep(1.0,0.12,cx);
  float flow=fbm(vec2(uv.x*2.5,uv.y*7.0-uTime*0.085));
  float sp=stars(vec2(uv.x*6.0,uv.y*46.0-uTime*0.13),70.0,0.84);
  float ends=smoothstep(0.0,0.10,uv.y)*smoothstep(1.0,0.90,uv.y);
  float a=(edge*(0.16+0.55*flow)+sp*edge*1.5)*ends*uK;
  vec3 col=mix(vec3(0.34,0.44,0.66),vec3(0.72,0.80,0.94),flow);
  gl_FragColor=vec4(col,a*uFade);
}`;
function makeXinghe(o){
  o=o||{};
  const mat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uFade:{value:1},uK:{value:o.k===undefined?0.8:o.k}},
    vertexShader:YH_VERT,fragmentShader:XH_FRAG});
  const g=new THREE.PlaneGeometry(o.w===undefined?17:o.w,o.len===undefined?230:o.len,1,1);
  g.rotateX(-Math.PI/2);
  const mesh=new THREE.Mesh(g,mat);
  mesh.position.set(o.x===undefined?0:o.x,o.y===undefined?0.55:o.y,o.z===undefined?-105:o.z);
  mesh.renderOrder=2; mesh.frustumCulled=false;
  return {mesh,mat,update(t){ mat.uniforms.uTime.value=t; }};
}

/* 云崖：云海中耸起的星河两岸（石崖堆叠，顶上是相望之地），合批 1 mesh */
function makeBank(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?5:o.seed);
  const B=new GeoBag(), n=o.n===undefined?4:o.n;
  let y=1.5,topY=1.5;
  for(let i=0;i<n;i++){
    const rr=(o.r===undefined?9:o.r)*(1.06-0.15*i)*(0.82+0.36*R());
    const rg=rockGeo(rr,1,R);
    rg.scale(1.3,0.72,1.0);
    y+=rr*0.72*0.80;
    rg.translate((R()-0.5)*2.4,y,(R()-0.5)*1.8);
    B.put(rg,shadeColor(0x070a10,0.70+0.26*R()));
    topY=y+rr*0.72*0.5;
  }

  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x1c2434,emissive:0x04060a}),{c:0xadc0d8,i:0.20,p:2.4})));
  return {g,topY};
}

/* 双星：牛郎星与织女星（寒银亮核 + 银蓝大晕，随呼吸明灭） */
function makeShuangxing(o){
  o=o||{};
  const g=new THREE.Group(), stars=[];
  (o.stars||[{x:-27,y:28,c:0xe6eefc,s:2.7},{x:27,y:26,c:0xd4e2f6,s:2.3}]).forEach(function(c,i){
    const core=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:c.c,transparent:true,
      opacity:1.0,depthWrite:false,blending:THREE.AdditiveBlending}));
    core.scale.set(c.s,c.s,1); core.renderOrder=3;
    const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xadc0d8,transparent:true,
      opacity:0.38,depthWrite:false,blending:THREE.AdditiveBlending}));
    halo.scale.set(c.s*5.2,c.s*5.2,1); halo.renderOrder=3;
    const grp=new THREE.Group(); grp.add(core); grp.add(halo);
    grp.position.set(c.x,c.y,c.z===undefined?-52:c.z);
    g.add(grp); stars.push({grp,core,halo,ph:i*2.4,from:grp.position.clone(),to:null});
  });
  return {g,stars,update(t,k){
    for(let i=0;i<stars.length;i++){
      const s=stars[i];
      s.core.material.opacity=k*(0.86+0.14*Math.sin(t*1.3+s.ph));
      s.halo.material.opacity=k*(0.34+0.04*Math.sin(t*0.9+s.ph));
    }
  }};
}

/* 飞星：周期掠过的流星（传恨），1 sprite 一颗 */
function makeFeixing(o){
  o=o||{};
  const g=new THREE.Group(), items=[];
  const n=o.n===undefined?3:o.n;
  const defs=o.defs||[{p:[46,44,-96],d:[-1,-0.42,0],len:30,rot:-0.40},
                      {p:[-52,52,-120],d:[0.9,-0.5,0],len:34,rot:0.48},
                      {p:[10,58,-140],d:[-0.8,-0.55,0],len:26,rot:-0.60}];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:0xdfe9fa,transparent:true,opacity:0.85,
      depthWrite:false,blending:THREE.AdditiveBlending,rotation:defs[i%defs.length].rot});
    const s=new THREE.Sprite(m);
    s.scale.set(7.5,0.6,1); s.renderOrder=4; g.add(s);
    items.push({s,p:defs[i%defs.length].p,d:defs[i%defs.length].d,len:defs[i%defs.length].len,
      period:o.period===undefined?7:o.period,off:i*2.3+0.6,dur:1.7});
  }
  return {g,update(t,k){
    for(let i=0;i<items.length;i++){
      const it=items[i], local=(t+it.off)%it.period;
      if(local<it.dur){
        const q=local/it.dur, e=Math.sin(q*Math.PI);
        it.s.position.set(it.p[0]+it.d[0]*q*it.len,it.p[1]+it.d[1]*q*it.len,it.p[2]);
        it.s.material.opacity=k*0.85*e;
      }else it.s.material.opacity=0;
    }
  }};
}

/* 鹊群：InstancedMesh 80 只鹊鸟（散旋 → 点击后错峰飞向桥位，合抱成弧） */
function makeMagpies(n,slots,seed){
  const B=new GeoBag();
  const body=new THREE.ConeGeometry(0.13,0.62,5); body.rotateX(Math.PI/2);
  body.translate(0,0.02,0.08); B.put(body,0x0b0e15);
  const head=new THREE.SphereGeometry(0.10,6,5); head.translate(0,0.06,0.38); B.put(head,0x0d1119);
  const tail=new THREE.ConeGeometry(0.08,0.44,4); tail.rotateX(-Math.PI/2);
  tail.translate(0,0.02,-0.36); B.put(tail,0x0a0d13);
  [1,-1].forEach(function(s){
    const w=new THREE.BufferGeometry();
    w.setAttribute('position',new THREE.BufferAttribute(new Float32Array([
      0,0.05,0.16, 0,0.05,-0.18, s*1.12,0.22,0.0]),3));
    w.computeVertexNormals(); B.put(w,0x0d1119);
  });
  const mat=rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x03050a}),{c:0xadc0d8,i:0.5,p:2.4});
  const mesh=new THREE.InstancedMesh(mergeGeos(B.list),mat,n);
  mesh.frustumCulled=false;
  const R=seedRnd(seed===undefined?182:seed), birds=[];
  for(let i=0;i<n;i++){
    birds.push({r:15+R()*10,a0:R()*6.283,sp:0.35+R()*0.5,ph:R()*6.283,fs:0.9+R()*0.35,
      s:1.3+R()*0.7,delay:(i%16)*0.15+Math.floor(i/16)*0.12,jx:(R()-0.5)*2.6,jz:(R()-0.5)*4});
  }
  const dm=new THREE.Object3D();
  const slotOf=function(i){
    const sl=slots[i%slots.length];
    return {x:sl[0]+birds[i].jx,y:sl[1],z:sl[2]+birds[i].jz};
  };
  return {mesh,update(t,elapsed,k){
    for(let i=0;i<n;i++){
      const b=birds[i];
      const oa=b.a0+t*b.sp;
      const ox=Math.cos(oa)*b.r, oz=-68+Math.sin(oa)*b.r*0.55, oy=44+Math.sin(t*0.85+b.ph)*3.4;
      const p=ease(clamp((elapsed-b.delay)/1.5,0,1));
      const sl=slotOf(i);
      const px=ox+(sl.x-ox)*p, py=oy+(sl.y-oy)*p+Math.sin(t*1.4+b.ph)*0.3*p, pz=oz+(sl.z-oz)*p;
      const flap=Math.sin(t*10.5*b.fs+b.ph)*0.5*(1-p*0.55);
      const yaw=p<0.999?Math.atan2(sl.x-ox,sl.z-oz):(sl.x<0?Math.PI/2:-Math.PI/2);
      dm.position.set(px,py,pz);
      dm.rotation.set(0,yaw,flap);
      dm.scale.setScalar(b.s);
      dm.updateMatrix(); mesh.setMatrixAt(i,dm.matrix);
    }
    mesh.instanceMatrix.needsUpdate=true;
  }};
}

/* 共用布景：云海 + 远山 + 银河带 + 星河光路（返回可 update 的句柄） */
function bXianheBase(g,opt){
  opt=opt||{};
  const water=makeWater({size:520,seg:84,amp:0.5,freq:0.06,speed:0.45,flow:[0.3,0.55],spec:1.5,
    deep:0x0a101c,shallow:0x1c2c44,skyc:0x2a3a55,moonDir:opt.moonDir||[-60,120,-180]});
  g.add(water.mesh);
  const ridge=makeRange({r:250,h:22,layers:2,peaks:4,seed:1820,color:0x070a11,atmo:0x1c2536,fogK:0.66,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-118); g.add(ridge.g);
  const yh=makeYinhan({k:opt.yhK===undefined?1:opt.yhK});
  yh.mesh.position.set(0,70,-192); yh.mesh.rotation.set(-0.72,0,0.50); g.add(yh.mesh);
  const xh=makeXinghe({k:opt.xhK===undefined?0.75:opt.xhK});
  g.add(xh.mesh);
  const dust=makeGlow({n:80,box:[190,52,120],pos:[0,28,-72],color:0xc6d4ea,size:4.5,speed:0.04,rise:0.05,maxA:0.24});
  g.add(dust.points);
  const mist=makeMist({n:5,spread:[230,24,120],pos:[0,12,-58],scale:70,color:0x8fa4c4,op:0.055});
  g.add(mist.g);
  return {water,ridge,yh,xh,dust,mist};
}

function bCover(){ // 封面 · 云汉无声 —— 星河初见
  const g=new THREE.Group();
  const base=bXianheBase(g,{yhK:1.0,xhK:0.7,moonDir:[40,120,-180]});
  const bankL=makeBank({seed:1821,r:9}); bankL.g.position.set(-31,0,-54); g.add(bankL.g);
  const bankR=makeBank({seed:1822,r:9}); bankR.g.position.set(31,0,-54); g.add(bankR.g);
  const zhnv=makeFigure({pose:'指月',robe:0x24314a,belt:0x7e92b4,skin:0xd9c3ae,collar:0xbcc9dc,
    hat:'发髻',rimC:0xadc0d8,rim:0.46,noProp:true,scale:1.5});
  zhnv.position.set(-30,bankL.topY-0.4,-53.5); zhnv.rotation.y=Math.PI/2-0.25; g.add(zhnv);
  const niul=makeFigure({pose:'独立',robe:0x1e2637,belt:0x6a7c9c,skin:0xd9b9a0,collar:0xb2c0d6,
    hat:'发髻',rimC:0xadc0d8,rim:0.46,noProp:true,scale:1.5});
  niul.position.set(30,bankR.topY-0.4,-53.5); niul.rotation.y=-Math.PI/2+0.25; g.add(niul);
  const fgL=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1823,rim:0.14});
  fgL.g.position.set(-15,-2,50); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:8,color:0x04060a,seed:1824,rim:0.14});
  fgR.g.position.set(15,-2,52); g.add(fgR.g);
  addLights(g,{c:0xa8bad4,i:0.38,p:[-30,90,-40]},{c:0x182031,i:0.56});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.water.update(t); base.ridge.update(t,0); base.yh.update(t); base.xh.update(t);
    base.dust.update(t); base.mist.update(t,k);
    fgL.update(t,k); fgR.update(t,k);
    zhnv.userData.update(t,k); niul.userData.update(t,k);
  }};
}

function bYinhan(){ // 一 · 银汉暗度 —— 纤云、飞星、双星隔岸相望，人间仰望
  const g=new THREE.Group();
  const base=bXianheBase(g,{yhK:1.4,xhK:1.0,moonDir:[-60,120,-180]});
  /* 云崖两岸 + 牛郎织女相望 */
  const bankL=makeBank({seed:1831,r:9}); bankL.g.position.set(-31,0,-52); g.add(bankL.g);
  const bankR=makeBank({seed:1832,r:9}); bankR.g.position.set(31,0,-52); g.add(bankR.g);
  const zhnv=makeFigure({pose:'指月',robe:0x24314a,belt:0x7e92b4,skin:0xd9c3ae,collar:0xbcc9dc,
    hat:'发髻',rimC:0xadc0d8,rim:0.5,noProp:true,scale:2.1});
  zhnv.position.set(-30,bankL.topY-0.5,-51.5); zhnv.rotation.y=Math.PI/2-0.22; g.add(zhnv);
  const niul=makeFigure({pose:'独立',robe:0x1e2637,belt:0x6a7c9c,skin:0xd9b9a0,collar:0xb2c0d6,
    hat:'发髻',rimC:0xadc0d8,rim:0.5,noProp:true,scale:2.1});
  niul.position.set(30,bankR.topY-0.5,-51.5); niul.rotation.y=-Math.PI/2+0.22; g.add(niul);
  /* 双星悬于两人头顶 */
  const sx=makeShuangxing({stars:[{x:-30,y:bankL.topY+8.6,z:-51.5,c:0xe6eefc,s:3.4},
                                  {x:30,y:bankR.topY+7.8,z:-51.5,c:0xd4e2f6,s:3.0}]});
  g.add(sx.g);
  /* 纤云：横渡星河的薄云缕 */
  const wisps=makeFlow({n:210,box:[140,10,46],pos:[0,32,-70],color:0xaebfd8,size:20,speed:1.7,maxA:0.22});
  g.add(wisps.points);
  /* 飞星传恨 */
  const fx=makeFeixing({n:3}); g.add(fx.g);
  /* 人间：远处低崖上仰望星河的人影（便胜却人间无数） */
  const hill=makeBank({seed:1833,r:13,n:3}); hill.g.position.set(6,0,-108); g.add(hill.g);
  const crowd=makeCrowd({n:7,rect:[-6,-111,13,3],seed:1834,color:0x0d1220,rimC:0x8fa4c4,
    rim:0.16,sMin:0.5,sMax:0.72,y:hill.topY-0.4});
  g.add(crowd.mesh);
  /* 前景云脚 */
  const fgL=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1835,rim:0.14});
  fgL.g.position.set(-15,-2,16); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:8,color:0x04060a,seed:1836,rim:0.14});
  fgR.g.position.set(15,-2,18); g.add(fgR.g);
  addLights(g,{c:0xa8bad4,i:0.40,p:[-40,95,-40]},{c:0x1a2232,i:0.56});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    base.water.update(t); base.ridge.update(t,0); base.yh.update(t); base.xh.update(t);
    base.dust.update(t); base.mist.update(t,k);
    fgL.update(t,k); fgR.update(t,k);
    zhnv.userData.update(t,k); niul.userData.update(t,k);
    sx.update(t,k); wisps.update(t); fx.update(t,k);
    crowd.update(t);
  }};
}

function bQueqiao(){ // 二（标志性瞬间·末境可点击）· 鹊桥久长 —— 点击鹊桥：鹊鸟搭桥横跨银汉，双星渐近
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,clickT:0,rv:0};
  const base=bXianheBase(g,{yhK:1.3,xhK:1.05,moonDir:[70,125,-185]});
  /* 云崖两岸（桥的两端）+ 相望的两人 */
  const bankL=makeBank({seed:1841,r:9}); bankL.g.position.set(-31,0,-52); g.add(bankL.g);
  const bankR=makeBank({seed:1842,r:9}); bankR.g.position.set(31,0,-52); g.add(bankR.g);
  const zhnv=makeFigure({pose:'指月',robe:0x24314a,belt:0x7e92b4,skin:0xd9c3ae,collar:0xbcc9dc,
    hat:'发髻',rimC:0xadc0d8,rim:0.5,noProp:true,scale:2.1});
  zhnv.position.set(-30,bankL.topY-0.5,-51.5); zhnv.rotation.y=Math.PI/2-0.22; g.add(zhnv);
  const niul=makeFigure({pose:'独立',robe:0x1e2637,belt:0x6a7c9c,skin:0xd9b9a0,collar:0xb2c0d6,
    hat:'发髻',rimC:0xadc0d8,rim:0.5,noProp:true,scale:2.1});
  niul.position.set(30,bankR.topY-0.5,-51.5); niul.rotation.y=-Math.PI/2+0.22; g.add(niul);
  /* 桥位弧线（鹊鸟的落点）+ 桥成后的微光桥脊 */
  const topY=(bankL.topY+bankR.topY)*0.5;
  const slots=[];
  for(let i=0;i<20;i++){
    const s=i/19;
    slots.push([-30+60*s, topY+2+14.5*Math.sin(Math.PI*s), -53]);
  }
  const arcPts=slots.filter(function(_,i){return i%2===0;}).map(function(p){
    return new THREE.Vector3(p[0],p[1]+0.4,p[2]); });
  const bridgeMat=new THREE.MeshBasicMaterial({color:0xc4d4ec,transparent:true,opacity:0.34,
    depthWrite:false,blending:THREE.AdditiveBlending});
  const bridge=new THREE.Mesh(new THREE.TubeGeometry(
    new THREE.CatmullRomCurve3(arcPts),32,0.17,5,false),bridgeMat);
  bridge.renderOrder=3; g.add(bridge);
  const mqp=makeMagpies(80,slots,1843); g.add(mqp.mesh);
  /* 双星（点击后沿桥渐近相会）+ 桥心相逢光晕 */
  const sx=makeShuangxing({stars:[{x:-30,y:topY+7.2,z:-53,c:0xe6eefc,s:4.0},
                                  {x:30,y:topY+6.4,z:-53,c:0xd4e2f6,s:3.6}]});
  g.add(sx.g);
  const meet=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xe9f1fc,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  meet.scale.set(16,16,1); meet.position.set(0,topY+16,-53); meet.renderOrder=4; g.add(meet);
  /* 相逢的银白点光（点成方亮） */
  const pl=new THREE.PointLight(0xcadaf2,1.5,90); pl.position.set(0,topY+15,-50); g.add(pl);
  /* 云海如水 + 前景云脚 */
  const fgL=makeForeground({kind:'坡石',n:3,r:4.0,w:24,d:8,color:0x04060a,seed:1844,rim:0.14});
  fgL.g.position.set(-15,-2,32); g.add(fgL.g);
  const fgR=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:8,color:0x04060a,seed:1845,rim:0.14});
  fgR.g.position.set(15,-2,34); g.add(fgR.g);
  addLights(g,{c:0xadc0d8,i:0.40,p:[40,95,-40]},{c:0x1b2333,i:0.56});
  const fromL=new THREE.Vector3(-27,topY+7.2,-53), toL=new THREE.Vector3(-6.5,topY+15.6,-53);
  const fromR=new THREE.Vector3(27,topY+6.4,-53), toR=new THREE.Vector3(6.5,topY+15.2,-53);
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      const elapsed=ctl.clicked?ctl.t-ctl.clickT:0;
      if(ctl.clicked)ctl.rv=Math.min(1,ctl.rv+dt/3.4);
      base.water.update(t); base.ridge.update(t,0); base.yh.update(t); base.xh.update(t);
      base.dust.update(t); base.mist.update(t,k);
      fgL.update(t,k); fgR.update(t,k);
      zhnv.userData.update(t,k); niul.userData.update(t,k);
      sx.update(t,k);
      mqp.update(t,elapsed,k);
      const rvS=ctl.clicked?ease(ctl.rv):0;
      bridgeMat.opacity=k*0.34*rvS;
      meet.material.opacity=k*0.5*sstep(0.5,1,ctl.rv)*(0.85+0.15*Math.sin(t*2.4));
      pl.intensity=k*1.5*sstep(0.5,1,ctl.rv)*(0.85+0.15*Math.sin(t*2.2));
      if(ctl.clicked){
        sx.stars[0].grp.position.copy(fromL).lerp(toL,rvS);
        sx.stars[1].grp.position.copy(fromR).lerp(toR,rvS);
        const sc=1+0.45*rvS; sx.stars[0].grp.scale.setScalar(sc); sx.stars[1].grp.scale.setScalar(sc);
      }
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.clickT=ctl.t;
        pluck(2,0.05,0.14); pluck(4,0.45,0.12); pluck(5,0.9,0.10); pluck(0,1.4,0.09);
        const fl=$('#flash'); fl.textContent='鹊桥相会'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x05080f),hor:C(0x121a28),bot:C(0x070a10),fog:C(0x111826),fd:0.0055,star:0.6,
  moon:new THREE.Vector3(-85,155,-215),ms:1.15,mph:0,mhaze:0.02,dirC:C(0xa8bad4),dirI:0.42,
  dirP:new THREE.Vector3(-40,90,-40),ambC:C(0x1a2232),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,64],t:[0,10,58],lf:[0,22,-52],lt:[0,23,-54]},
  sky:()=>SK({top:C(0x060a12),hor:C(0x131b29),bot:C(0x080b11),fog:C(0x10161f),fd:0.0050,star:0.55,
    ms:1.3,moon:new THREE.Vector3(48,138,-205),
    dirC:C(0xa8bad4),dirI:0.44,ambC:C(0x182031),ambI:0.62,mhaze:0.02}) },
{ name:'银汉暗度',dwell:17,river:0.05,build:bYinhan,
  cam:{f:[0,7.5,30],t:[1.5,7,26],lf:[0,18,-55],lt:[0,17.5,-58]},
  sky:()=>SK({top:C(0x05080f),hor:C(0x121a28),bot:C(0x070a10),fog:C(0x0d1320),fd:0.0055,star:0.62,
    ms:1.45,mph:0,mhaze:0.02,moon:new THREE.Vector3(-85,155,-215),
    dirC:C(0xa8bad4),dirI:0.5,dirP:new THREE.Vector3(-40,95,-40),ambC:C(0x1a2232),ambI:0.62}) },
{ name:'鹊桥久长',dwell:18,river:0.04,build:bQueqiao,
  cam:{f:[0,8,44],t:[0,9,38],lf:[0,20,-56],lt:[0,21,-58]},
  sky:()=>SK({top:C(0x060910),hor:C(0x141c2b),bot:C(0x080b11),fog:C(0x10161f),fd:0.0060,star:0.58,
    ms:1.3,mph:0.08,mhaze:0.02,moon:new THREE.Vector3(90,152,-218),
    dirC:C(0xadc0d8),dirI:0.5,dirP:new THREE.Vector3(40,95,-40),ambC:C(0x1b2333),ambI:0.62}) },
];
"""
