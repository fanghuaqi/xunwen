# -*- coding: utf-8 -*-
"""zhouye-shushuo.py —— 《舟夜书所见》（清·查慎行，no.213，水墨夜思）生成配置
两境：月黑渔灯（墨夜孤舟一点暖）、星散满河（风簇浪 · 标志性瞬间，点击河星——渔灯碎作满河星光）
全诗 20 字写尽水面反光的奇迹：由一到万（一点萤火孤光 → 满河碎星）。
「月黑」故无月轮（ms 0.001 + 月移出视野）；渔灯暖光是全页唯一暖点，与全局冷银水墨互为对比。"""

META = dict(
    N=2, slug='zhouye-shushuo', title='舟夜书所见', dyn='清 · 查慎行', brand_author='查慎行',
    gold_rgb='168,180,192',
    residual=('将进酒', '万古愁'),
    root=""":root{
  --gold:#a8b4c0; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(168,180,192,.26);
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
    tip='轻点画面 / 按空格 —— 风起浪簇，渔灯碎作满河星光',
    hint='← → 键或空格逐境游览 · 末境可点击河星，看孤光散作满河星',
    cover_read='舟夜书所见。清，查慎行。月黑见渔灯，孤光一点萤。',
    cover_p1='两重意境，随诗句次第展开：月黑无月之夜，沉沉墨色里唯见一盏渔灯，孤光如萤，一点浮沉；微风乍起，吹簇起层层细浪，那一点孤光被浪揉碎荡开——散作满河星光。由一到万，是水面反光的奇迹。',
    cover_p2='边读诗，边走进查慎行笔下这个由一点萤光到满河星子的夜之奇境。',
    end_h2='灯散 · 星河', cn_word='两',
    words_js="['再游一次，静守孤灯','初识诗境，尚需共读','渐入佳境，再诵几遍','已见风簇细浪','深得由一到万之妙','满河星光，尽收眼底']",
    sky_atmo='0x1c2634',
)

POEM_JS = """const POEM = [
{ name:'月黑渔灯', jing:'月黑无月之夜，唯见一盏渔灯 —— 孤光如萤，一点浮沉。（孤光 · 渔灯）',
  segs:[
   {c:'月黑见渔灯，', p:py('yuè hēi jiàn yú dēng')},
   {c:'孤光一点萤。', p:py('gū guāng yī diǎn yíng')}],
  read:'月黑见渔灯，孤光一点萤。',
  yisi:'夜黑无月，四下漆黑，河面上唯一看得见的，是一盏渔灯的光。那一点孤立的光亮，像一只小小的萤火虫，在茫茫墨色里微微闪烁、轻轻浮沉。',
  zhu:[['舟夜书所见','夜间在船上记下所见的景象（书：写、记录）'],['月黑','月夜无光，天色漆黑'],['孤光','孤立而微弱的光，指那盏渔灯的光'],['萤','萤火虫，此处比喻渔灯孤微的光，如一点萤火']] },
{ name:'星散满河', jing:'微风簇浪，孤光碎作满河星 —— 由一到万的夜之魔法。（点击河星）',
  segs:[
   {c:'微微风簇浪，', p:py('wēi wēi fēng cù làng')},
   {c:'散作满河星。', p:py('sàn zuò mǎn hé xīng')}],
  read:'微微风簇浪，散作满河星。',
  yisi:'微微的风吹簇起层层细浪，渔灯的倒影被浪揉碎、荡开，散落在河面上，像撒了满河的星星。一点萤光，顿成万点星光——全诗最奇的想象，正在这由一到万的一瞬。',
  zhu:[['簇','簇拥、聚拢，指风把浪吹簇起来（读 cù）'],['散作','散开，变成'],['满河星','灯光倒影随浪碎开，如满天繁星洒落河面，是全诗最奇的想象']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「月黑见渔灯」的下一句是？', o:['孤光一点萤','微微风簇浪','散作满河星'], a:0},
 {q:'「微微风簇浪」的下一句是？', o:['孤光一点萤','月黑见渔灯','散作满河星'], a:2},
 {q:'「孤光一点萤」中「萤」的正确读音和妙处是？', o:['yíng，实写河面上萤火虫飞舞','yìng，形容灯光映水摇荡','yíng，把孤灯微光比作一点萤火，孤而微'], a:2},
 {q:'「微微风簇浪」中「簇」的正确读音和意思是？', o:['cù，簇拥、聚起——风把浪吹簇成层层细浪','zú，箭头，形容浪如飞箭','còu，拼凑，浪花零碎散乱'], a:0},
 {q:'这首诗最令人称奇的想象是？', o:['渔人深夜捕鱼的辛劳','一点孤灯的倒影被风浪揉碎，散作满河星光——由一到万','月黑之夜行船的惊险'], a:1},
];
"""

SCENES_JS = """/* ================= 舟夜书所见 · 两境场景（水墨夜思：月黑渔灯、星散满河） =================
   「月黑」故无月轮——全页唯一的光是一盏渔灯的暖，与全局冷银水墨互为对比；
   末境标志性瞬间：点击河星，风起浪簇，一点萤火孤光碎作满河星光（由一到万）。 */

/* 渔舟：船体剖面（Lathe 拉长成舢板）+ 舱面 + 后舱矮篷 + 船头斜桅，合批 1 mesh */
function makeBoat(){
  const B=new GeoBag(), c1=0x0a0e15, c2=0x101620, c3=0x151c28;
  const hull=new THREE.LatheGeometry(
    [[0,0.16],[0.42,0.16],[0.62,0.20],[0.74,0.34],[0.70,0.52],[0.52,0.64],[0.18,0.70]].map(function(p){
      return new THREE.Vector2(p[0],p[1]);}),18);
  hull.scale(5.2,1,1.6); B.put(hull,c1);
  const deck=new THREE.CylinderGeometry(0.62,0.66,0.10,16);
  deck.scale(4.6,1,1.34); deck.translate(0,0.68,0); B.put(deck,c2);
  const canopy=new THREE.CylinderGeometry(0.78,0.82,2.6,12,1,true,0,Math.PI);
  canopy.rotateZ(Math.PI/2); canopy.scale(1,1,1.5); canopy.translate(-2.2,1.18,0); B.put(canopy,c3);
  const pole=new THREE.CylinderGeometry(0.045,0.06,2.5,6);
  pole.rotateZ(-0.42); pole.translate(2.85,1.62,0); B.put(pole,c2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
    specular:0x2c3850,emissive:0x04060b}),{c:0x8fa4c4,i:0.26,p:2.5})));
  return g;
}

/* 渔灯：船头桅灯 —— 笼身 + 暖焰心 + 暖辉 + 一点暖光（全页唯一暖点；材质初值=最大值） */
function makeFishLamp(o){
  o=o||{};
  const dim=o.dim===undefined?1:o.dim;
  const g=new THREE.Group();
  const cage=new THREE.Mesh(new THREE.SphereGeometry(0.20,10,8),
    new THREE.MeshPhongMaterial({color:0x3a2e22,emissive:0xff8c3a,emissiveIntensity:0.55,shininess:8}));
  cage.renderOrder=2; g.add(cage);
  const core=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc37a,
    transparent:true,opacity:0.85,depthWrite:false,blending:THREE.AdditiveBlending}));
  core.scale.set(0.95,0.95,1); core.renderOrder=3; g.add(core);
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
    transparent:true,opacity:0.5,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.set(4.6,4.6,1); glow.renderOrder=3; g.add(glow);
  const pl=new THREE.PointLight(0xffa050,1.5,34);
  g.add(pl);
  const ph=Math.random()*6.283;
  g.update=function(t,fk){
    const k=(fk===undefined?1:fk)*dim;
    core.material.opacity=k*0.85*(0.78+0.14*Math.sin(t*6.3+ph)+0.08*Math.sin(t*17.7+ph*2.1));
    glow.material.opacity=k*0.5*(0.86+0.14*Math.sin(t*2.3+ph));
    cage.material.emissiveIntensity=k*0.55*(0.80+0.20*Math.sin(t*5.1+ph));
    pl.intensity=k*1.5*(0.85+0.15*Math.sin(t*7.7+ph));
  };
  g.userData.update=g.update;
  return {g,update:g.update,glow,core};
}

/* 孤光倒影：灯下水面的一点萤 + 立在灯下的一段微光柱（additive Sprite，不进雾同步） */
function makeGlimmer(x,z){
  const g=new THREE.Group();
  const dot=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xffc37a,
    transparent:true,opacity:0.55,depthWrite:false,blending:THREE.AdditiveBlending}));
  dot.scale.set(1.7,1.7,1); dot.position.set(x,0.32,z); dot.renderOrder=3; g.add(dot);
  const col=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xff9a4a,
    transparent:true,opacity:0.20,depthWrite:false,blending:THREE.AdditiveBlending}));
  col.scale.set(1.8,7.0,1); col.position.set(x,2.0,z); col.renderOrder=3; g.add(col);
  const ph=Math.random()*6.283;
  g.update=function(t,fk){
    const k=fk===undefined?1:fk;
    dot.material.opacity=k*0.55*(0.72+0.28*Math.sin(t*2.6+ph));
    col.material.opacity=k*0.20*(0.85+0.15*Math.sin(t*1.7+ph*1.3));
  };
  g.userData.update=g.update;
  return {g,update:g.update,dot,col};
}

/* 舟中夜坐观灯人 + 渔舟 + 桅灯 组合（各境共用） */
function makeNightBoat(x,z){
  const g=new THREE.Group();
  const boat=makeBoat(); g.add(boat);
  const poet=makeFigure({pose:'坐饮',robe:0x1c2534,belt:0x4c5c74,skin:0xcbb9a2,collar:0x9aabc2,
    hat:'发髻',rimC:0xa8b4c0,rim:0.5,noProp:true,scale:0.5});
  poet.position.set(0.5,0.12,0); poet.rotation.y=1.2; g.add(poet);
  const lamp=makeFishLamp({}); lamp.g.position.set(3.15,2.45,0); g.add(lamp.g);
  g.position.set(x,0.02,z);
  return {g,poet,lamp};
}

/* 满河星：星光粒子自灯下一点荡开 —— uT0 触发「由一到万」，点击前 vA 全 0
   （自定义 ShaderMaterial，显式传 vertexShader+fragmentShader；淡入淡出走 uFade） */
const STAR_VERT=`
attribute vec3 aDir; attribute float aSp; attribute float aSeed; attribute float aSize;
uniform float uTime; uniform float uT0; varying float vA;
void main(){
  float age=max(uTime-uT0,0.0);
  float r=aSp*3.2*(1.0-exp(-age*0.5));
  vec3 p=position;
  p.x+=aDir.x*r; p.z+=aDir.z*r;
  p.y+=0.10+sin(uTime*1.8+aSeed*37.0)*0.12;
  float tw=0.52+0.48*sin(uTime*(1.4+aSeed*3.4)+aSeed*47.0);
  float edge=(1.0-smoothstep(0.70,1.0,clamp(r/17.0,0.0,1.0)))*smoothstep(0.0,0.6,r);
  vA=step(0.001,uT0)*tw*edge;
  vec4 mv=modelViewMatrix*vec4(p,1.0);
  gl_PointSize=aSize*(0.72+0.28*tw)*(115.0/max(1.0,-mv.z));
  gl_Position=projectionMatrix*mv;
}`;

function makeRiverStars(pos,n){
  const g=new THREE.BufferGeometry();
  const P=new Float32Array(n*3),D=new Float32Array(n*3),S=new Float32Array(n),Z=new Float32Array(n),A=new Float32Array(n);
  for(let i=0;i<n;i++){
    P[i*3]=pos[0]+(Math.random()-0.5)*0.5;
    P[i*3+1]=pos[1];
    P[i*3+2]=pos[2]+(Math.random()-0.5)*0.5;
    const a=Math.random()*6.283;
    D[i*3]=Math.cos(a); D[i*3+1]=0; D[i*3+2]=Math.sin(a);
    S[i]=1.3+4.3*Math.random();
    A[i]=Math.random(); Z[i]=1.4+Math.random()*2.2;
  }
  g.setAttribute('position',new THREE.BufferAttribute(P,3));
  g.setAttribute('aDir',new THREE.BufferAttribute(D,3));
  g.setAttribute('aSp',new THREE.BufferAttribute(S,1));
  g.setAttribute('aSeed',new THREE.BufferAttribute(A,1));
  g.setAttribute('aSize',new THREE.BufferAttribute(Z,1));
  const m=new THREE.ShaderMaterial({transparent:true,depthWrite:false,blending:THREE.AdditiveBlending,
    uniforms:{uTime:{value:0},uT0:{value:-999},uColor:{value:C(0xd9e6f5)},uFade:{value:1},uMaxA:{value:0.55}},
    vertexShader:STAR_VERT,fragmentShader:GLOW_FRAG});
  const points=new THREE.Points(g,m); points.frustumCulled=false; points.renderOrder=3;
  return {points,mat:m,update(t){m.uniforms.uTime.value=t;}};
}

function bCover(){ // 封面 · 月黑河夜 —— 远处一点渔灯，是整幅夜色里唯一的光（悬念）
  const g=new THREE.Group();
  const water=makeWater({size:420,seg:70,amp:0.18,freq:0.13,speed:0.42,flow:[0.3,0.08],spec:1.7,
    deep:0x05080f,shallow:0x0b1420,skyc:0x121a27,moonDir:[0,-1,0]});
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:14,layers:2,peaks:5,seed:2130,color:0x060910,atmo:0x1c2634,fogK:0.56,glowK:0.04,y:-12});
  ridge.g.position.set(0,0,-98); g.add(ridge.g);
  const nb=makeNightBoat(1.5,-30); g.add(nb.g);
  const motes=makeGlow({n:52,box:[170,26,90],pos:[0,8,-20],color:0x9db0c8,size:6,speed:0.05,rise:0,maxA:0.24});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,26,130],pos:[0,9,-52],scale:78,color:0x7e8ea8,op:0.08});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:34,n:14,d:6,color:0x04060a,seed:2131,sway:0.9});
  reed.g.position.set(-11,-1.2,14); g.add(reed.g);
  const rock=makeForeground({kind:'坡石',n:3,r:4.0,w:22,d:8,color:0x04060a,seed:2132,rim:0.14});
  rock.g.position.set(12,-1.2,12); g.add(rock.g);
  addLights(g,{c:0x8fa4c8,i:0.32,p:[-30,70,-50]},{c:0x151c29,i:0.72});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); motes.update(t); mist.update(t,k);
    reed.update(t,k); rock.update(t,k); nb.lamp.update(t,k*0.5); nb.poet.update(t,k);
  }};
}

function bYudeng(){ // 一 · 月黑渔灯 —— 墨色里的一盏渔灯、一点萤（水面高光即灯的暖光柱）
  const g=new THREE.Group();
  const water=makeWater({size:520,seg:96,amp:0.15,freq:0.18,speed:0.42,flow:[0.28,0.06],spec:0.65,
    deep:0x05080e,shallow:0x0b141f,skyc:0x121b28,moonDir:[2.9,2.5,-9]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xffa860);
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:13,layers:2,peaks:5,seed:2133,color:0x060910,atmo:0x1c2634,fogK:0.55,glowK:0.04,y:-12});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 孤舟 + 舟中夜坐观灯人 + 桅灯（渔灯为全页唯一暖点） */
  const nb=makeNightBoat(0,-9); g.add(nb.g);
  /* 孤光倒影：水面一点萤 + 微光柱 */
  const glimmer=makeGlimmer(2.9,-9); g.add(glimmer.g);
  const dust=makeGlow({n:60,box:[90,18,50],pos:[0,6,-12],color:0x8fa2bc,size:5,speed:0.05,rise:0,maxA:0.20});
  g.add(dust.points);
  const mist=makeMist({n:7,spread:[220,16,80],pos:[0,5,-50],scale:60,color:0x7e8ea8,op:0.07});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:30,n:12,d:6,color:0x04060a,seed:2134,sway:0.8});
  reed.g.position.set(-10,-1.2,11); g.add(reed.g);
  const rock=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:7,color:0x04060a,seed:2135,rim:0.14});
  rock.g.position.set(13.5,-1.0,9); g.add(rock.g);
  addLights(g,{c:0x8fa4c8,i:0.34,p:[-30,70,-50]},{c:0x161d2a,i:0.70});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); dust.update(t); mist.update(t,k);
    reed.update(t,k); rock.update(t,k);
    nb.lamp.update(t,k); nb.poet.update(t,k); glimmer.update(t,k);
  }};
}

function bManhe(){ // 二（标志性瞬间·末境可点击）· 星散满河 —— 点击河星：风起浪簇，孤光碎作满河星光
  const g=new THREE.Group();
  const ctl={t:0,clicked:false,reveal:0,uT0:-1};
  const water=makeWater({size:560,seg:96,amp:0.18,freq:0.18,speed:0.5,flow:[0.4,0.1],spec:0.8,
    deep:0x05080e,shallow:0x0c1520,skyc:0x131c2a,moonDir:[2.9,2.5,-10]});
  water.mesh.material.uniforms.uMoonColor.value=C(0xffa860);
  g.add(water.mesh);
  const ridge=makeRange({r:240,h:13,layers:2,peaks:4,seed:2136,color:0x060910,atmo:0x1d2735,fogK:0.55,glowK:0.04,y:-12});
  ridge.g.position.set(0,0,-104); g.add(ridge.g);
  const nb=makeNightBoat(0,-10); g.add(nb.g);
  const glimmer=makeGlimmer(2.9,-10); g.add(glimmer.g);
  /* 满河星：星光粒子自灯下一点荡开（点击前 vA 全 0） */
  const stars=makeRiverStars([2.9,0.5,-10],380);
  g.add(stars.points);
  /* 灯碎一瞬的暖火星（点击时 fire()） */
  const burst=makeBurst({n:90,color:0xffd9a0,pos:[2.9,0.9,-10]});
  g.add(burst.points);
  /* 微微之风（点击后增强为风簇浪） */
  const wind=makeFlow({n:170,box:[95,10,60],pos:[0,3.5,-12],color:0x8fa0b8,size:12,speed:3.0,maxA:0.10});
  g.add(wind.points);
  const dust=makeGlow({n:56,box:[100,20,56],pos:[0,6,-14],color:0x8fa2bc,size:5,speed:0.05,rise:0,maxA:0.16});
  g.add(dust.points);
  const mist=makeMist({n:7,spread:[230,18,80],pos:[0,5,-52],scale:58,color:0x7e8ea8,op:0.055});
  g.add(mist.g);
  const reed=makeForeground({kind:'芦苇',w:32,n:13,d:6,color:0x04060a,seed:2137,sway:1.0});
  reed.g.position.set(-10.5,-1.2,12); g.add(reed.g);
  const rock=makeForeground({kind:'坡石',n:2,r:3.4,w:14,d:7,color:0x04060a,seed:2138,rim:0.14});
  rock.g.position.set(13.5,-1.0,10); g.add(rock.g);
  addLights(g,{c:0x8fa4c8,i:0.34,p:[-30,70,-50]},{c:0x161d2a,i:0.70});
  const wu=water.mesh.material.uniforms;
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.reveal=Math.min(1,ctl.reveal+dt/2.8);
      const rv=ctl.reveal;
      water.update(t);
      wu.uAmp.value=0.18+0.38*rv;            // 微微风簇浪：浪随点击涌起
      wu.uSpeed.value=0.5+0.36*rv;
      wu.uSpec.value=0.8+1.0*rv;             // 浪起后光瓣被打碎，暖光柱更碎更亮
      wind.update(t);
      wind.mat.uniforms.uMaxA.value=k*(0.10+0.20*rv);
      stars.update(t);
      if(ctl.uT0>=0)stars.mat.uniforms.uT0.value=ctl.uT0;
      burst.update(t);
      dust.update(t); mist.update(t,k);
      ridge.update(t,0); reed.update(t,k); rock.update(t,k);
      nb.lamp.update(t,k); nb.poet.update(t,k); glimmer.update(t,k);
      /* 爆发感：辉光长大（scale 不受 fadeK 约束；opacity 恪守初值=最大值） */
      nb.lamp.glow.scale.setScalar(4.6*(1.0+0.55*rv));
      glimmer.dot.scale.setScalar(1.7*(1.0+0.5*rv));
      glimmer.col.scale.set(1.8*(1.0+0.8*rv),7.0*(1.0+0.25*rv),1);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.uT0=ctl.t;
        burst.fire();
        pluck(3,0.05,0.13); pluck(1,0.5,0.11); pluck(4,1.0,0.09);
        const fl=$('#flash'); fl.textContent='散作满河星'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """/* 本诗「月黑」故无月轮：ms 0.001 + 月移出视野（天空/雾/氛围走水墨夜思冷银基调） */
const SK=(o)=>Object.assign({
  top:C(0x05080e),hor:C(0x111823),bot:C(0x04060a),fog:C(0x0e141e),fd:0.0050,star:0.30,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0x8fa4c4),dirI:0.32,
  dirP:new THREE.Vector3(-30,70,-40),ambC:C(0x161d2a),ambI:0.70},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.5,34],t:[0,8,29],lf:[0,4.5,-26],lt:[0,4.5,-26]},
  sky:()=>SK({top:C(0x05070c),hor:C(0x0f151f),bot:C(0x04060a),fog:C(0x0c111a),fd:0.0046,star:0.26,dirI:0.30}) },
{ name:'月黑渔灯',dwell:15,river:0.045,build:bYudeng,
  cam:{f:[0,4.6,15],t:[0,4.3,12.5],lf:[0,2.0,-9],lt:[0.6,2.2,-9.6]},
  sky:()=>SK({hor:C(0x121a26),fog:C(0x0f151f),fd:0.0058,star:0.30}) },
{ name:'星散满河',dwell:18,river:0.05,build:bManhe,
  cam:{f:[0,6.5,18],t:[0,8.5,14],lf:[0,2.2,-10],lt:[0,3.0,-14]},
  sky:()=>SK({hor:C(0x141c29),fog:C(0x101622),fd:0.0062,star:0.34,ambI:0.66}) },
];
"""
