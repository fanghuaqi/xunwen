# -*- coding: utf-8 -*-
"""zhongnanwang-yuxue.py —— 《终南望余雪》（唐·祖咏，queue no.217，宣纸留白）生成配置
两境（N=queue stages 数）：雪浮云端（终南阴岭秀·积雪浮云端——标志性瞬间）、
霁色暮寒（林表明霁色·城中增暮寒——末境点击「林表霁色渐冷+城中暮色四合」）。
宣纸留白全套色板：浅纸底 #e9e2d0、浓墨远山 #2c2f33 系、淡雾 #e6dfcc，accent=#4a5060
（queue 分配强调色，青灰雪影）只落在雪影/暮流/人物袍色与 UI 上，全页近零饱和。
标志性瞬间（境壹·全诗名句）：积雪浮云端——雪线山体着色器让雪冠停在山肩，
山腰一道横云海缓缓横流，山基没入云中，积雪如悬浮云端。
末境点击（queue interact）：点击暮寒——山脊霁色微光转冷渐隐+暮光由暖转冷，
青灰暮流横城、雾加浓、暮雪又起、城中灯火初上，「城中增暮寒」。
彩蛋典故：祖咏考场「意尽」只写四句（小测第 4 题落点）。"""
import io, os
_here = os.path.dirname(os.path.abspath(__file__))

META = dict(
    N=2, slug='zhongnanwang-yuxue', title='终南望余雪', dyn='唐 · 祖咏', brand_author='祖 咏',
    gold_rgb='74,80,96',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#4a5060; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(74,80,96,.28);
  --kai:'Ma Shan Zheng','Kaiti SC','STKaiti','KaiTi','Noto Serif SC',serif;
  --song:'Noto Serif SC','SimSun','STSong',serif;
}""",
    repl_colors=[
        ('background:#05070d', 'background:#e9e2d0', 2),
        ('rgba(5,8,15', 'rgba(233,226,208', 1),
        ('rgba(4,6,11', 'rgba(212,202,176', 2),
        ('rgba(6,9,16', 'rgba(233,226,208', 1),
        ('rgba(3,5,9', 'rgba(236,230,214', 1),
        ('#0b101c', '#f6f1e1', 1),
        ('#6f664f', '#8a8268', 1),
        ('#5a5340', '#8d8571', 1),
        ('0x0a1526', '0xe6dfcc', 4),
    ],
    tip='轻点画面 / 按空格 —— 霁色渐冷，暮色四合',
    hint='← → 键或空格逐境游览 · 末境可点击画面：看林表霁色渐冷、城中暮色四合',
    cover_read='终南望余雪。唐，祖咏。终南阴岭秀，积雪浮云端。林表明霁色，城中增暮寒。',
    cover_p1='两重意境，随诗句次第展开：从长安城头北望终南，阴岭秀色尽收眼底，一线积雪悬浮在云端之上；雪后初晴的明净光色染亮林梢，待到暮色四合，城中的寒意又添了几分。',
    cover_p2='边读诗，边站在长安城头远望终南：山顶的积雪像浮在云上——这是祖咏在科举考场上「意尽」搁笔的四句，短到近乎任性，却句句都是画。',
    end_h2='霁色 · 暮寒', cn_word='两',
    words_js="['再望一次终南雪','初识祖咏，尚需共读','渐入诗境，再诵几遍','雪意渐明，寒意渐生','已解浮云霁色意','意尽而止，余味无穷']",
    sky_atmo='0xd8d5c9',
)

POEM_JS = """const POEM = [
{ name:'雪浮云端', jing:'终南阴岭秀，积雪浮云端 —— 从长安北望：山北秀色尽收眼底，一线积雪悬浮在云端之上。（雪山 · 云海 · 标志性瞬间：雪线悬于云端的错觉）',
  segs:[
   {c:'终南阴岭秀，', p:py('zhōng nán yīn lǐng xiù')},
   {c:'积雪浮云端。', p:py('jī xuě fú yún duān')}],
  read:'终南阴岭秀，积雪浮云端。',
  yisi:'遥望终南山的北坡，山色秀美；山顶的积雪，仿佛浮在云端之上。——起笔先立「望」的立足点：人在长安城中，望的是山的阴面（北岭）；一个「秀」字总写雪后山色，一个「浮」字化静为动：山顶积雪与天际层云相接，雪像不是长在山上，而是轻轻搁在云上——高、洁、远，五个字里全有了。',
  zhu:[['终南','终南山，秦岭主峰之一，在唐长安城（今西安）以南约六十里，天气晴好时城中抬头可见——「望余雪」的立足点在长安'],['阴岭','山的北面。山北水南为阴——从长安北望终南，正见其阴岭；「阴岭」也暗含背阴多雪之意'],['秀','秀丽、挺秀——一个「秀」字总起阴岭雪后的姿色，是「望」之所聚'],['积雪浮云端','山顶积雪与白云相接，远望似积雪浮于云端——「浮」字是千古诗眼：雪本静物，着一「浮」字便有了凌虚之势，雪之高、云之白、山之峻尽出']] },
{ name:'霁色暮寒', jing:'林表明霁色，城中增暮寒 —— 雪后初晴的余光染亮林梢；暮色四合，长安城里的寒意又重了几分。（霁色 · 暮寒 · 末境点击画面：霁色渐冷，暮色四合）',
  segs:[
   {c:'林表明霁色，', p:py('lín biǎo míng jì sè')},
   {c:'城中增暮寒。', p:py('chéng zhōng zēng mù hán')}],
  read:'林表明霁色，城中增暮寒。',
  yisi:'傍晚时分，雪后初晴的明净光色染明了林梢；随着日暮天暗，长安城里的寒意反而更重了。——「明」字作动词用：霁色是雪后初晴给林梢镀上的最后一层亮光；「增」字从视觉转向体感：雪后放晴时只觉爽洁，待暮色一合、余光收尽，寒气才真正落到人身上——望雪的终点，是雪的寒意落在望雪人心里。',
  zhu:[['林表','林梢、树梢——雪后初晴时最先被余光照亮的地方'],['霁','雨雪初停、天空放晴，读 jì——「霁色」即雪后初晴时天宇间明净的光色'],['明','此处作动词：照亮、染明——余光把林梢照得发亮，与下句「增」字对仗'],['城中增暮寒','暮色降临，城中寒气愈重——「增」字把景语转成体感，由望雪落到感寒，余味全在这一个「寒」字'],['意尽的典故','据《唐诗纪事》：此诗为祖咏在长安应试时所作。唐代试帖诗规定作六韵十二句的五言排律，祖咏写完四句即交卷，人问其故，答曰：「意尽。」——意尽则止，不画蛇添足']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「终南阴岭秀」的下一句是？', o:['积雪浮云端','林表明霁色','城中增暮寒'], a:0},
 {q:'「林表明霁色」的下一句是？', o:['积雪浮云端','城中增暮寒','终南阴岭秀'], a:1},
 {q:'「林表明霁色」中「霁」的读音与意思是？', o:['jì，雨雪初停、天空放晴——「霁色」即雪后初晴时明净的光色','qīng，清凉寒冷——「霁色」指雪后清冽的寒气','tíng，聚集停留——「霁色」指山间停驻不散的云雾'], a:0},
 {q:'这首诗是祖咏在科举考场上写的。关于他「只写四句就交卷」的典故，下列说法正确的是？', o:['唐代试帖诗规定作六韵十二句的五言排律，祖咏写完四句便搁笔交卷，主考官问他为何不写完，他只答两个字：「意尽」——意尽则止，不画蛇添足','祖咏来不及答完考卷，匆忙交卷后追悔莫及，主考官怜他才思给了名次','当时考官只要求写四句，祖咏依规完成任务，并无出格之处'], a:0},
 {q:'前两句写望中所见（阴岭秀、雪浮云端），后两句写望中所感（霁色明林表、暮寒增城中）——这首咏雪名作最妙的写法是？', o:['用大量笔墨正面堆砌雪的颜色与形状，把雪写得越白越好','从侧面着笔：以「秀」「浮」「明」「增」四字写雪之势、雪之光、雪之寒，不着一字正面铺陈雪形——「意尽」即止，四句抵得十二句','借终南山的积雪讽刺朝廷官员不体恤城中贫寒百姓'], a:1},
];
"""

SCENES_JS = """/* ================= 终南望余雪 · 两境场景（宣纸留白·雪霁暮寒：雪浮云端、霁色暮寒） =================
   浅纸为天、浓墨作山、大量留白；accent=#4a5060（青灰雪影）只落在雪影/暮流/人物袍色上，全页近零饱和。
   境壹（标志性瞬间）：积雪浮云端——自写雪线山体着色器（雪冠停在山肩、参差雪线），山腰一道横云海
   缓缓横流、山基没入云中，积雪如悬浮云端；落雪疏疏，淡日雪晴。
   境贰（末境可点击）：自长安城中望终南——城廓垛口、角楼屋舍顶上残雪，林表冬枝承霁色；
   点击暮寒：山脊霁色微光转冷渐隐+暮光由暖转冷，青灰暮流横城、雾加浓、暮雪又起、灯火初上。 */

/* —— 雪线山体 makeXueling(o)：弧形山 ribbon（多峰折线剖面）+ 自写着色器——
   v 高于参差雪线处覆纸白雪冠、雪线以下青灰雪影渐入浓墨（uFogK 雾同步进 fogShaders）——
   「积雪浮云端」的山。 */

const XL_VERT=`
varying vec2 vUv; varying float vD;
void main(){
  vUv=uv;
  vec4 wp=modelMatrix*vec4(position,1.0);
  vD=length(cameraPosition-wp.xyz);
  gl_Position=projectionMatrix*viewMatrix*wp;
}`;
const XL_FRAG=`
uniform vec3 uInk; uniform vec3 uInk2; uniform vec3 uSnow; uniform vec3 uShade;
uniform float uSnowK; uniform vec3 uFogColor; uniform float uFogDensity; uniform float uFogK; uniform float uFade;
varying vec2 vUv; varying float vD;
float hash1(float n){return fract(sin(n)*43758.5453123);}
float noise1(float x){float i=floor(x);float f=fract(x);f=f*f*(3.0-2.0*f);return mix(hash1(i),hash1(i+1.0),f);}
void main(){
  float alt=clamp(vUv.y,0.0,1.4);
  float u=vUv.x*23.0;
  float n=noise1(u)*0.7+noise1(u*1.9+13.0)*0.3;
  float line=0.54+(n-0.5)*0.10;
  float sn=smoothstep(line,line+0.10,alt);
  vec3 rock=mix(uInk,uInk2,pow(clamp(alt/0.9,0.0,1.0),0.7));
  vec3 snowc=mix(uShade,uSnow,smoothstep(line,line+0.30,alt));
  vec3 col=mix(rock,snowc,sn*uSnowK);
  float fk=mix(uFogK,1.0,smoothstep(0.012,0.020,uFogDensity));
  float f=clamp((1.0-exp(-uFogDensity*uFogDensity*vD*vD))*fk,0.0,0.94);
  col=mix(col,uFogColor,f);
  gl_FragColor=vec4(col,uFade);
}`;
function makeXueling(o){
  o=o||{};
  const arc=o.arc===undefined?1.2:o.arc, r=o.r===undefined?300:o.r;
  const yBase=o.yBase===undefined?-12:o.yBase, hBase=o.hBase===undefined?42:o.hBase;
  const seg=o.seg===undefined?110:o.seg, R=seedRnd(o.seed===undefined?21701:o.seed);
  const peaks=o.peaks===undefined?4:o.peaks, a0=o.a0===undefined?(Math.PI-arc/2):o.a0;
  const pk=[];
  for(let i=0;i<peaks;i++)pk.push({u:(i+0.5)/peaks+(R()-0.5)*(0.5/peaks),h:hBase*(0.35+0.45*R()),w:0.16+0.10*R(),p:1.1+R()*0.6});
  for(let i=0;i<10;i++)pk.push({u:R(),h:hBase*(0.10+0.22*R()),w:0.05+0.09*R(),p:1.2});
  const floor=hBase*0.40, f=5+R()*6, ph=R()*6.283, jit=hBase*0.02;
  const pos=[],uv=[],idx=[];
  for(let i=0;i<=seg;i++){
    const uu=i/seg, ang=a0+arc*uu;
    let h=floor;
    for(let k=0;k<pk.length;k++){const p2=pk[k];const x=Math.abs(uu-p2.u)/p2.w;if(x<1)h+=p2.h*Math.pow(1-x,p2.p);}
    h*=1+0.06*Math.sin(uu*f*6.283+ph);
    h+=jit*(Math.sin(uu*87+ph*3)+0.6*Math.sin(uu*193+ph*7));
    h*=Math.pow(Math.sin(Math.PI*uu),0.6);
    const sx=Math.sin(ang)*r, sz=Math.cos(ang)*r;
    pos.push(sx,yBase,sz, sx,yBase+h,sz);
    uv.push(uu,0, uu,h/hBase);
  }
  for(let i=0;i<seg;i++){const a=i*2;idx.push(a,a+2,a+1, a+1,a+2,a+3);}
  const geo=new THREE.BufferGeometry();
  geo.setAttribute('position',new THREE.BufferAttribute(new Float32Array(pos),3));
  geo.setAttribute('uv',new THREE.BufferAttribute(new Float32Array(uv),2));
  geo.setIndex(idx); geo.computeVertexNormals();
  const atmo=o.atmo===undefined?0xd8d5c9:o.atmo, ink=o.ink===undefined?0x2c2f33:o.ink;
  const m=new THREE.ShaderMaterial({transparent:true,side:THREE.DoubleSide,
    uniforms:{uInk:{value:C(ink)},uInk2:{value:C(ink).lerp(C(atmo),0.25)},
      uSnow:{value:C(o.snowC===undefined?0xf6f3e8:o.snowC)},
      uShade:{value:C(o.shadeC===undefined?0x767f92:o.shadeC)},
      uSnowK:{value:o.snowK===undefined?1:o.snowK},
      uFogColor:{value:C(0xe6dfcc)},uFogDensity:{value:0.005},
      uFogK:{value:o.fogK===undefined?0.42:o.fogK},uFade:{value:1}},
    vertexShader:XL_VERT,fragmentShader:XL_FRAG});
  fogShaders.push(m.uniforms);
  const mesh=new THREE.Mesh(geo,m);
  mesh.frustumCulled=false; mesh.renderOrder=o.order===undefined?-6:o.order;
  const g=new THREE.Group(); g.add(mesh);
  return {g:g};
}

/* —— 云海 makeYunhai(o)：山腰横带云层（大扁 Sprite 缓慢横流、首尾回绕）——
   山基没入云中，雪冠如浮云端——「积雪浮云端」错觉的机关（fadeK 铁律：初值=最大，逐帧 ×k） */
function makeYunhai(o){
  o=o||{};
  const n=o.n===undefined?9:o.n, w=o.w===undefined?240:o.w;
  const y=o.y===undefined?2:o.y, spread=o.spread===undefined?14:o.spread;
  const z=o.z===undefined?-92:o.z, zSpread=o.zSpread===undefined?22:o.zSpread;
  const scale=o.scale===undefined?74:o.scale, speed=o.speed===undefined?1.1:o.speed;
  const color=o.color===undefined?0xe6e0cc:o.color, op=o.op===undefined?0.16:o.op;
  const g=new THREE.Group(), items=[];
  for(let i=0;i<n;i++){
    const m=new THREE.SpriteMaterial({map:glowTex(),color:color,transparent:true,
      opacity:op*(0.55+0.45*Math.random()),depthWrite:false});
    const s=new THREE.Sprite(m);
    s.position.set((Math.random()-0.5)*w, y+(Math.random()-0.5)*spread, z+(Math.random()-0.5)*zSpread);
    const sx=scale*(0.7+0.6*Math.random());
    s.scale.set(sx,sx*(0.09+0.06*Math.random()),1);
    s.renderOrder=2;
    g.add(s);
    items.push({s:s,x0:s.position.x,op0:m.opacity,ph:Math.random()*6.283,v:speed*(0.5+0.7*Math.random())});
  }
  g.update=function(t,k){
    const kk=k===undefined?1:k;
    for(let i=0;i<items.length;i++){
      const it=items[i];
      let x=it.x0+t*it.v;
      x=((x+w*0.5)%w+w)%w-w*0.5;
      it.s.position.x=x;
      it.s.material.opacity=kk*it.op0*(0.72+0.28*Math.sin(t*0.21+it.ph));
    }
  };
  g.userData.update=g.update;
  return {g:g,update:g.update};
}

/* —— 落雪 makeLuoXue(o)：自写着色器（自上而下缓落 + 横向风漂；uMaxA 作雪势可渐起；
   uFade 显式交给 setFade，浅纸底用 NormalBlending，additive 会把雪洗成白棉团） */
const ZN_SNOW_VERT=`
attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uSpeed; uniform vec3 uBox; uniform float uWind;
varying float vA;
void main(){
  vec3 p=position;
  float h=uBox.y;
  float fall=fract(uTime*uSpeed*(0.35+0.75*aSeed)+aSeed);
  p.y-=fall*h;
  p.x+=sin(uTime*(0.5+0.4*aSeed)+aSeed*43.0)*(0.8+1.4*aSeed)+uWind*uTime*(0.3+aSeed*0.5);
  p.x=mod(p.x+uBox.x*0.5,uBox.x)-uBox.x*0.5;
  p.z+=cos(uTime*0.4+aSeed*31.0)*1.2;
  vA=smoothstep(0.0,0.10,fall)*smoothstep(1.0,0.86,fall);
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.75+0.25*sin(uTime*1.3+aSeed*50.0))*(150.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;
function makeLuoXue(o){
  const n=o.n===undefined?160:o.n, box=o.box===undefined?[190,44,80]:o.box, pos=o.pos===undefined?[0,20,-46]:o.pos;
  const color=o.color===undefined?0xf6f4ec:o.color, size=o.size===undefined?2.1:o.size;
  const speed=o.speed===undefined?1.0:o.speed, wind=o.wind===undefined?1.1:o.wind, maxA=o.maxA===undefined?0.30:o.maxA;
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*box[0];
    P[i*3+1]=pos[1]+(Math.random()-0.5)*box[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*box[2];
    S[i]=Math.random(); Z[i]=size*(0.6+0.9*Math.random());
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aSeed',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.NormalBlending,
    uniforms:{uTime:{value:0},uSpeed:{value:speed},uBox:{value:new THREE.Vector3(box[0],box[1],box[2])},
      uWind:{value:wind},uColor:{value:C(color)},uFade:{value:0},uMaxA:{value:maxA}},
    vertexShader:ZN_SNOW_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points:points,update(t){m.uniforms.uTime.value=t;},mat:m};
}

/* —— 淡日 makeDanRi(o)：雪后初晴的纸色淡日（limbTex 日轮+一圈更淡的晕；fadeK 初值=最大） */
function makeDanRi(o){
  o=o||{};
  const r=o.r===undefined?8:o.r, discOp=o.op===undefined?0.40:o.op, hazeOp=o.haze===undefined?0.13:o.haze;
  const g=new THREE.Group();
  const disc=new THREE.Sprite(new THREE.SpriteMaterial({map:limbTex(),color:o.color===undefined?0xf3ecda:o.color,
    transparent:true,opacity:discOp,depthWrite:false,fog:false}));
  disc.scale.set(r*2,r*2,1); g.add(disc);
  const haze=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:o.hazeC===undefined?0xeee8d4:o.hazeC,
    transparent:true,opacity:hazeOp,depthWrite:false,fog:false}));
  haze.scale.set(r*5.6,r*5.6,1); g.add(haze);
  g.update=function(t,k){
    disc.material.opacity=k*discOp*(0.94+0.06*Math.sin(t*0.5));
    haze.material.opacity=k*hazeOp*(0.85+0.15*Math.sin(t*0.33+1.7));
  };
  g.userData.update=g.update;
  return g;
}

/* —— 冬林 makeShuCong(o)：几株落尽叶子的树（干+疏枝合批 1 mesh，枝头一点霁色亮梢）——「林表」 */
function makeShuCong(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?21731:o.seed);
  const n=o.n===undefined?3:o.n, w=o.w===undefined?7:o.w;
  const B=new GeoBag();
  for(let i=0;i<n;i++){
    const x=(R()-0.5)*w, z=(R()-0.5)*2.0;
    const hh=2.2+2.2*R();
    const tr=new THREE.CylinderGeometry(0.05,0.10,hh,5);
    tr.translate(0,hh*0.5,0); tr.translate(x,0,z); B.put(tr,0x262a30);
    const nb=3+Math.floor(R()*3);
    for(let b=0;b<nb;b++){
      const a=R()*6.283, len=hh*(0.30+0.35*R()), y0=hh*(0.45+0.5*R());
      const tx=x+Math.cos(a)*len*0.8, ty=y0+len*0.7, tz=z+Math.sin(a)*len*0.5;
      B.put(limbGeo([x,y0,z],[tx,ty,tz],0.045,0.014,5),shadeColor(0x262a30,0.9+0.3*R()));
      if(R()<0.55){
        const tip=new THREE.SphereGeometry(0.07,5,4);
        tip.scale(1.4,0.5,1); tip.translate(tx,ty+0.05,tz);
        B.put(tip,o.tipC===undefined?0x9aa2b0:o.tipC);
      }
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x555c6a,emissive:0x050608}),{c:0xe8e6da,i:0.16,p:2.6})));
  const ph=R()*6.283;
  g.update=function(t){ g.rotation.z=0.004*Math.sin(t*0.6+ph); };
  g.userData.update=g.update;
  return g;
}

/* —— 城廓 makeChengKuo(o)：城墙垛口+角楼+门楼+城内屋舍（顶上残雪），合批 1 mesh——「城中」 */
function makeChengKuo(o){
  o=o||{};
  const w=o.w===undefined?30:o.w, hh=o.h===undefined?3.4:o.h;
  const R=seedRnd(o.seed===undefined?21741:o.seed);
  const B=new GeoBag();
  const wall=new THREE.BoxGeometry(w,hh,2.2); wall.translate(0,hh/2,0); B.put(wall,0x26292f);
  const cap2=new THREE.BoxGeometry(w,0.12,2.4); cap2.translate(0,hh+0.06,0); B.put(cap2,0xdad8cc);
  const merN=Math.floor(w/1.9);
  for(let i=0;i<merN;i++){
    const mx=-w/2+0.95+i*1.9;
    const mer=new THREE.BoxGeometry(0.95,0.75,0.9); mer.translate(mx,hh+0.375,-0.4); B.put(mer,0x222530);
    const cap=new THREE.BoxGeometry(1.05,0.10,1.0); cap.translate(mx,hh+0.80,-0.4); B.put(cap,0xe8e6da);
  }
  const tw=new THREE.BoxGeometry(4.2,2.6,3.2); tw.translate(-w*0.5+2.4,hh+1.3,0.2); B.put(tw,0x242831);
  const r1=new THREE.ConeGeometry(3.4,1.2,4); r1.rotateY(Math.PI/4); r1.translate(-w*0.5+2.4,hh+3.2,0.2); B.put(r1,0x1e222a);
  const rc1=new THREE.ConeGeometry(2.4,0.24,4); rc1.rotateY(Math.PI/4); rc1.translate(-w*0.5+2.4,hh+3.66,0.2); B.put(rc1,0xe4e2d6);
  const gate=new THREE.BoxGeometry(4.6,hh+1.6,3.0); gate.translate(w*0.18,(hh+1.6)/2,0.3); B.put(gate,0x23262e);
  const door=new THREE.BoxGeometry(1.6,2.3,0.4); door.translate(w*0.18,1.15,1.75); B.put(door,0x0d0f13);
  const r2=new THREE.ConeGeometry(3.6,1.3,4); r2.rotateY(Math.PI/4); r2.translate(w*0.18,hh+2.25,0.3); B.put(r2,0x1d212a);
  const rc2=new THREE.ConeGeometry(2.5,0.26,4); rc2.rotateY(Math.PI/4); rc2.translate(w*0.18,hh+2.76,0.3); B.put(rc2,0xe4e2d6);
  [[-6.5,-5.5,2.6],[0.5,-7.5,3.2],[7.5,-5.2,2.4],[13,-7.6,2.9],[-12,-6.8,2.7]].forEach(function(p){
    const bw=p[2], bh=1.5+R()*0.8;
    const body=new THREE.BoxGeometry(bw,bh,bw*0.8); body.translate(p[0],bh/2,p[1]); B.put(body,0x252931);
    const roof=new THREE.ConeGeometry(bw*0.82,1.1,4); roof.rotateY(Math.PI/4); roof.translate(p[0],bh+0.55,p[1]); B.put(roof,0x1c2027);
    const snow=new THREE.ConeGeometry(bw*0.5,0.22,4); snow.rotateY(Math.PI/4); snow.translate(p[0],bh+1.16,p[1]); B.put(snow,0xe6e4d8);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:5,
    specular:0x3a4050,emissive:0x050609}),{c:0xd8dce4,i:o.rim===undefined?0.13:o.rim,p:2.8})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 望雪人/城中人：全诗贯穿的同一造型（青灰袍，幞头；每次 build 新建材质） */
function znFigure(scale){
  return makeFigure({pose:'独立',robe:0x2e3440,belt:0x454e5e,skin:0xd9b189,collar:0x4a5262,
    hair:0x1a1d24,hat:'幞头',rimC:0x9aa4b8,rim:0.45,noProp:true,scale:scale===undefined?1.8:scale});
}

function bCover(){ // 卷首 · 宣纸长卷远望终南雪：雪冠停在山肩、云海横腰、落雪疏疏
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d0,c2:0xc9cdb0,y:-2}); g.add(grd.mesh);
  const xr=makeXueling({arc:1.5,r:210,yBase:-14,hBase:46,seed:21701,peaks:4,fogK:0.42});
  xr.g.position.set(-12,0,-4); g.add(xr.g);
  const xr2=makeXueling({arc:1.1,r:130,yBase:-12,hBase:26,seed:21702,peaks:3,fogK:0.50,order:-5});
  xr2.g.position.set(30,0,2); xr2.g.rotation.y=0.12; g.add(xr2.g);
  const ridge=makeRange({r:300,h:16,layers:2,peaks:5,seed:21703,color:0x2c2f33,atmo:0xd8d5c9,
    fogK:0.62,glowK:0.03,glow:0xf4eeda,y:-10,order:-6});
  ridge.g.position.set(-70,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const sea=makeYunhai({n:9,w:240,y:8,spread:5,z:-132,zSpread:22,scale:74,color:0xf0ebda,op:0.42,speed:1.1});
  g.add(sea.g);
  const sun=makeDanRi({r:8,op:0.40});
  sun.position.set(-42,40,-92); g.add(sun);
  const snow=makeLuoXue({n:140,box:[190,44,80],pos:[0,20,-46],speed:1.0,wind:1.2,maxA:0.30,size:2.0});
  g.add(snow.points);
  const mist=makeMist({n:6,spread:[230,20,90],pos:[0,7,-62],scale:70,color:0xe2dcc8,op:0.10});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:3,r:3.2,w:16,d:7,color:0x23262b,seed:21704,rim:0.10,rimC:0xecead8});
  fg1.g.position.set(-13,-2,16); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:2.4,w:12,d:6,color:0x23262b,seed:21705,rim:0.10,rimC:0xecead8});
  br.g.position.set(14,-1.8,14); g.add(br.g);
  addLights(g,{c:0xe4dcc4,i:0.46,p:[-45,100,25]},{c:0xd6d8c6,i:0.6});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); sea.update(t,k); snow.update(t); mist.update(t,k);
    sun.update(t,k); fg1.update(t,k); br.update(t,k);
  }};
}
function bXueduan(){ // 壹（标志性瞬间）· 雪浮云端 —— 终南阴岭秀，积雪浮云端：雪线悬于云端的错觉
  const g=new THREE.Group();
  const grd=makeGround({r:250,c1:0xe8e2cf,c2:0xc6cab0,y:-2}); g.add(grd.mesh);
  /* 主峰：终南阴岭——雪冠停在山肩（自写雪线着色器） */
  const xr=makeXueling({arc:1.35,r:190,yBase:-14,hBase:44,seed:21706,peaks:4,fogK:0.42});
  xr.g.position.set(-10,0,-10); g.add(xr.g);
  const xr2=makeXueling({arc:0.9,r:120,yBase:-12,hBase:24,seed:21707,peaks:3,fogK:0.50,order:-5});
  xr2.g.position.set(26,0,6); xr2.g.rotation.y=0.10; g.add(xr2.g);
  const ridge=makeRange({r:300,h:16,layers:2,peaks:5,seed:21708,color:0x2c2f33,atmo:0xd8d5c9,
    fogK:0.62,glowK:0.03,glow:0xf4eeda,y:-10,order:-6});
  ridge.g.position.set(-76,0,-96); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  /* 云海横腰：山基没入云中——雪冠如浮云端（错觉机关，两层缓流） */
  const sea=makeYunhai({n:10,w:250,y:8,spread:5,z:-140,zSpread:26,scale:78,color:0xf0ebda,op:0.42,speed:1.15});
  g.add(sea.g);
  const sea2=makeYunhai({n:6,w:180,y:13,spread:4,z:-152,zSpread:14,scale:56,color:0xf2edda,op:0.20,speed:0.8});
  g.add(sea2.g);
  /* 淡日：雪后初晴 */
  const sun=makeDanRi({r:7.5,op:0.40});
  sun.position.set(-40,38,-90); g.add(sun);
  /* 落雪疏疏（余雪飘絮） */
  const snow=makeLuoXue({n:130,box:[180,44,80],pos:[0,20,-44],speed:0.95,wind:1.1,maxA:0.30,size:2.0});
  g.add(snow.points);
  /* 城头望雪人：坡石上临风北望 */
  const rock=makeForeground({kind:'坡石',n:3,r:2.6,w:10,d:6,color:0x23262b,seed:21709,rim:0.12,rimC:0xecead8});
  rock.g.position.set(9,-1.6,6); g.add(rock.g);
  const poet=znFigure(1.8); poet.position.set(9,-0.30,6); poet.rotation.y=2.7; g.add(poet);
  const mist=makeMist({n:6,spread:[220,20,90],pos:[0,6,-64],scale:70,color:0xe2dcc8,op:0.10});
  g.add(mist.g);
  const fg1=makeForeground({kind:'坡石',n:2,r:3.2,w:14,d:6,color:0x23262b,seed:21710,rim:0.10,rimC:0xecead8});
  fg1.g.position.set(-13,-2,15); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:2.4,w:12,d:6,color:0x23262b,seed:21711,rim:0.10,rimC:0xecead8});
  br.g.position.set(15,-1.8,13); g.add(br.g);
  addLights(g,{c:0xe6dec2,i:0.5,p:[-45,100,25]},{c:0xd8dac8,i:0.62});
  return {group:g,update(t){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); sea.update(t,k); sea2.update(t,k); snow.update(t); mist.update(t,k);
    sun.update(t,k); fg1.update(t,k); br.update(t,k); poet.update(t,k); rock.update(t,k);
  }};
}
function bJise(){ // 贰（末境·可点击）· 霁色暮寒 —— 林表明霁色，城中增暮寒：点击霁色渐冷+暮色四合
  const ctl={t:0,clicked:false,on:false,dusk:0};
  const g=new THREE.Group();
  /* 远处终南残雪：山脊一带霁色微光（点击后渐冷渐隐） */
  const ridge=makeRange({r:300,h:26,layers:2,peaks:5,seed:21712,color:0x2c2f33,atmo:0xd8d5c9,
    fogK:0.60,glowK:0.14,glow:0xe8ddc0,y:-9,order:-6});
  ridge.g.position.set(-10,0,-118); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const warmGlow=C(0xe8ddc0), coolGlow=C(0x8b93a4), lw=C(0xdcc8a2), lc=C(0x8b93a4);
  const grd=makeGround({r:220,c1:0xe6e0cd,c2:0xc2c6ac,y:-1.6}); g.add(grd.mesh);
  /* 城廓：城墙垛口+角楼+门楼+屋舍（顶上残雪） */
  const city=makeChengKuo({w:34,h:3.4,seed:21713,scale:1.05});
  city.position.set(-3,-1.6,-14); city.rotation.y=0.16; g.add(city);
  /* 林表：城内外几丛冬林，枝头一点霁色亮梢 */
  const shu1=makeShuCong({seed:21714,n:3,w:8}); shu1.position.set(7.5,-1.6,-9); g.add(shu1);
  const shu2=makeShuCong({seed:21715,n:2,w:5}); shu2.position.set(-12,-1.6,-8.5); g.add(shu2);
  const shu3=makeShuCong({seed:21716,n:3,w:9}); shu3.position.set(15,-1.6,-16); g.add(shu3);
  /* 城中行人（远景人影一片） */
  const crowd=makeCrowd({n:6,rect:[-9,-11,15,5],seed:21717,color:0x2e3440,rimC:0x9aa4b8,rim:0.22,sMin:0.5,sMax:0.62,y:-0.30});
  g.add(crowd.mesh);
  /* 城头望雪人 */
  const poet=znFigure(1.55); poet.position.set(4.6,-0.28,-7.5); poet.rotation.y=2.95; g.add(poet);
  const rock=makeForeground({kind:'坡石',n:2,r:2.2,w:8,d:5,color:0x23262b,seed:21718,rim:0.12,rimC:0xecead8});
  rock.g.position.set(5.6,-1.2,-5.6); g.add(rock.g);
  /* 落雪：雪霁零星；点击后暮雪又起 */
  const snow=makeLuoXue({n:80,box:[150,40,70],pos:[0,18,-34],speed:0.8,wind:0.9,maxA:0.30,size:1.9});
  g.add(snow.points);
  /* 暮霭：点击后加浓（初值=最大，基态取半） */
  const mist=makeMist({n:7,spread:[240,18,90],pos:[0,5.5,-56],scale:72,color:0xdad4c2,op:0.16});
  g.add(mist.g);
  /* 青灰暮流横城（accent=#4a5060 正是暮色的颜色）：点击后漫起 */
  const flow=makeFlow({n:520,box:[120,16,60],pos:[0,7,-24],color:0x4a5060,size:22,speed:3.2,maxA:0.001});
  g.add(flow.points);
  /* 暮色里的城中灯火：零星暖点+一点暖光（寒意里的对照） */
  const deng=makeGlow({n:26,box:[24,3.2,10],pos:[-3,1.6,-13],color:0xd8a860,size:5,speed:0.05,rise:0,add:false,maxA:0.001});
  g.add(deng.points);
  const pl=new THREE.PointLight(0xd8a860,0.85,46); pl.position.set(-3,3,-13); g.add(pl);
  /* 前景 */
  const fg1=makeForeground({kind:'坡石',n:2,r:3.0,w:13,d:6,color:0x23262b,seed:21719,rim:0.10,rimC:0xecead8});
  fg1.g.position.set(-12,-1.8,13); g.add(fg1.g);
  const br=makeForeground({kind:'坡石',n:2,r:2.3,w:11,d:5,color:0x23262b,seed:21720,rim:0.10,rimC:0xecead8});
  br.g.position.set(13.5,-1.6,11); g.add(br.g);
  /* 局部暮光：点击后由暖转冷（自建灯便于逐帧动画；初值 0.5=最大） */
  const dLight=new THREE.DirectionalLight(0xdcc8a2,0.5); dLight.position.set(40,50,15); g.add(dLight);
  addLights(g,null,{c:0xcccbc2,i:0.58});
  const glowItems=ridge.items;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.on)ctl.dusk=Math.min(1,ctl.dusk+dt/4.2);
      const e0=ctl.dusk, e=e0*e0*(3-2*e0);
      /* 霁色渐冷：山脊霁色微光减弱、转青灰；暮光由暖转冷 */
      for(let i=0;i<glowItems.length;i++){
        const u=glowItems[i].mesh.material.uniforms;
        u.uGlowK.value=0.14*(1-0.85*e);
        u.uGlow.value.copy(warmGlow).lerp(coolGlow,e);
      }
      dLight.color.copy(lw).lerp(lc,e);
      dLight.intensity=k*(0.5-0.26*e)*(0.92+0.08*Math.sin(t*0.7));
      grd.update();
      /* 暮色四合：雾浓、青灰暮流漫城、暮雪又起、灯火初上 */
      mist.update(t,k*(0.55+0.45*e));
      flow.mat.uniforms.uMaxA.value=0.001+0.34*e;
      snow.mat.uniforms.uMaxA.value=0.30*(0.45+0.55*e);
      deng.mat.uniforms.uMaxA.value=0.001+0.50*e;
      pl.intensity=k*0.85*e*(0.85+0.15*Math.sin(t*5.3));
      ridge.update(t,0); flow.update(t); snow.update(t); deng.update(t);
      fg1.update(t,k); br.update(t,k); crowd.update(t);
      shu1.update(t); shu2.update(t); shu3.update(t); poet.update(t,k); rock.update(t,k);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.on=true;
        setAmbience(0.35);
        pluck(0,0.0,0.11); pluck(3,0.5,0.09); pluck(1,1.05,0.08);
        const fl=$('#flash'); fl.textContent='林表明霁色 城中增暮寒';
        fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xdcd6c4),bot:C(0xcfc7b0),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.44,
  dirP:new THREE.Vector3(-50,110,30),ambC:C(0xd6d8c6),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,66],t:[0,12,56],lf:[1.5,10,-26],lt:[2.5,11.5,-34]},
  sky:()=>SK({fd:0.0046,star:0.03}) },
{ name:'雪浮云端',dwell:17,river:0.02,build:bXueduan,
  cam:{f:[0,9,40],t:[0,13,34],lf:[-2,11,-34],lt:[1.5,12.5,-46]},
  sky:()=>SK({fd:0.0050,star:0.02,dirC:C(0xe6dec2),dirI:0.5,
    dirP:new THREE.Vector3(-45,100,25),ambC:C(0xd8dac8),ambI:0.62}) },
{ name:'霁色暮寒',dwell:19,river:0.02,build:bJise,
  cam:{f:[0,7.5,28],t:[-1,8.5,21],lf:[0,8,-14],lt:[-2,8.5,-24]},
  sky:()=>SK({fd:0.0066,star:0.02,dirC:C(0xdcc8a2),dirI:0.42,
    dirP:new THREE.Vector3(40,60,15),ambC:C(0xcccbc2),ambI:0.58}) },
];
"""
