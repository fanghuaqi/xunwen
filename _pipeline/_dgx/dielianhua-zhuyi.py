# -*- coding: utf-8 -*-
"""dielianhua-zhuyi.py —— 《蝶恋花·伫倚危楼风细细》（宋·柳永，no.170，烟雨江南）生成配置
两境（queue 口径 N=2）：伫倚危楼（望极春愁黯黯生天际·草色烟光残照里·谁会凭阑意）、
衣带渐宽（拟醉无味·王国维治学第二境）。
标志性瞬间「衣带渐宽终不悔」：凭阑人剪影倚栏；末境点击凭阑人——
衣带松宽垂落、身形渐瘦（具象化），春愁自天际铺满，残照被愁云吞去。
美术：全页禁金，黛蓝 #90a8c0 主调（queue accent）、藕荷 #d8a7b1 仅作残照点缀；
暮景月隐星稀；与 dielianhua-jianju（晏殊·第一境，水墨）同族异貌——本页重心在凭阑人的
身形与春愁天际，楼不必高、愁要看得见。"""
import io, os
def io_open(n):
    return io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), n), encoding='utf-8').read()

META = dict(
    N=2, slug='dielianhua-zhuyi', title='蝶恋花·伫倚危楼风细细', dyn='宋 · 柳永', brand_author='柳 永',
    gold_rgb='144,168,192',
    root=""":root{
  --gold:#90a8c0; --ink:#e6ecef; --dim:#7e8ea0; --paper:rgba(13,17,26,.60);
  --line:rgba(144,168,192,.28);
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
    tip='轻点画面 / 按空格 —— 衣带渐宽，春愁铺满天际',
    hint='← → 键或空格逐境游览 · 末境可点击凭阑人：衣带渐宽，春愁铺满天际',
    cover_read='蝶恋花。宋，柳永。伫倚危楼风细细，望极春愁，黯黯生天际。草色烟光残照里，无言谁会凭阑意。',
    cover_p1='两重意境，随词句次第展开：伫倚危楼，春风细细，望极春愁黯黯生天际，草色烟光残照里无人会得凭阑意；拟把疏狂图一醉，对酒当歌强乐还无味，最终衣带渐宽终不悔，为伊消得人憔悴。',
    cover_p2='边读词，边走近柳永笔下这位无言的凭阑人——王国维借作「治学第二境」的执着不悔之境。',
    end_h2='不悔 · 憔悴', cn_word='两',
    words_js="['再游一次，重倚危楼','初识柳永，尚需共读','渐入词境，略有所感','词境渐深，春愁在望','已会凭阑之意','衣带渐宽，不悔之境']",
    sky_atmo='0x39455c',
)

POEM_JS = """const POEM = [
{ name:'伫倚危楼', jing:'伫倚危楼，风细细；望极春愁，黯黯生天际——草色烟光残照里，无言谁会凭阑意。（危楼倚暮 · 春愁自天际暗生）',
  segs:[
   {c:'伫倚危楼风细细，', p:py('zhù yǐ wēi lóu fēng xì xì')},
   {c:'望极春愁，', p:py('wàng jí chūn chóu')},
   {c:'黯黯生天际。', p:py('àn àn shēng tiān jì')},
   {c:'草色烟光残照里，', p:py('cǎo sè yān guāng cán zhào lǐ')},
   {c:'无言谁会凭阑意。', p:py('wú yán shuí huì píng lán yì')}],
  read:'伫倚危楼风细细，望极春愁，黯黯生天际。草色烟光残照里，无言谁会凭阑意。',
  yisi:'久久地倚立在高楼之上，春风细细拂面。极目远望，春天的闲愁暗暗地从天边升起。萋萋芳草与蒙蒙暮霭，笼罩在夕阳的余晖里；默默无言，又有谁能理解我凭阑远望的心意呢？',
  zhu:[['伫','久立、久倚'],['危楼','高楼'],['黯黯','迷蒙不明的样子，也形容心情沮丧忧闷'],['草色烟光','芳草萋萋、暮霭朦胧的暮春暮色'],['残照','夕阳的余晖'],['会','领会、理解'],['凭阑','靠着栏杆。阑，同「栏」']] },
{ name:'衣带渐宽', jing:'拟把疏狂图一醉，对酒当歌，强乐还无味——衣带渐宽终不悔，为伊消得人憔悴。（点击凭阑人：衣带渐宽，春愁铺满天际）',
  segs:[
   {c:'拟把疏狂图一醉，', p:py('nǐ bǎ shū kuáng tú yī zuì')},
   {c:'对酒当歌，', p:py('duì jiǔ dāng gē')},
   {c:'强乐还无味。', p:py('qiǎng lè huán wú wèi')},
   {c:'衣带渐宽终不悔，', p:py('yī dài jiàn kuān zhōng bù huǐ')},
   {c:'为伊消得人憔悴。', p:py('wèi yī xiāo dé rén qiáo cuì')}],
  read:'拟把疏狂图一醉，对酒当歌，强乐还无味。衣带渐宽终不悔，为伊消得人憔悴。',
  yisi:'打算把这疏放不羁的心情，借酒一醉；对着美酒听着歌声，勉强寻欢终究没有滋味。衣带渐渐宽松也始终不后悔，为了她，我甘愿这样消瘦憔悴。',
  zhu:[['拟把','打算将'],['疏狂','生活狂放散漫、不受拘束的样子'],['图','谋求、博取'],['强乐','勉强作乐。强（qiǎng），勉强'],['还','仍、还是（读 huán）'],['衣带渐宽','人渐消瘦，衣带都显得宽松了'],['消得','值得'],['伊','她，指所思念的人'],['治学第二境','王国维《人间词话》引「衣带渐宽」二句，喻古今成大事业、大学问者的第二境：执着追求，虽憔悴而不悔']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「伫倚危楼风细细」的下一句是？', o:['望极春愁，黯黯生天际','草色烟光残照里','无言谁会凭阑意'], a:0},
 {q:'「拟把疏狂图一醉」的下一句是？', o:['衣带渐宽终不悔','对酒当歌，强乐还无味','为伊消得人憔悴'], a:1},
 {q:'「强乐还无味」中「强」的正确读音与意思是？', o:['qiáng，强大、强壮','jiàng，倔强','qiǎng，勉强'], a:2},
 {q:'王国维《人间词话》借本词哪两句比喻「治学第二境」（执着追求、虽憔悴而不悔）？', o:['衣带渐宽终不悔，为伊消得人憔悴','草色烟光残照里，无言谁会凭阑意','拟把疏狂图一醉，对酒当歌'], a:0},
 {q:'这首词抒发的核心情感是？', o:['暮春登楼对江天景色的赏悦','对所爱之人坚贞不渝、甘愿憔悴的深挚相思','怀才不遇、仕途失意的愤懑'], a:1},
];
"""

SCENES_JS = """/* ================= 蝶恋花·伫倚危楼 · 两境场景（烟雨江南·柳永：黛蓝湿雾、危楼凭阑、残照烟光） =================
   美术立意：全页禁金，黛蓝 #90a8c0 主调、藕荷 #d8a7b1 仅作残照点缀；暮景月隐星稀。
   标志性瞬间「衣带渐宽终不悔」：凭阑人剪影倚栏；末境点击凭阑人——衣带松宽垂落、身形渐瘦，
   春愁自天际铺满（王国维治学第二境的具象化）。楼不必高、愁要看得见。 */

/* —— 残照/暮霭天际带：glowTex 软边横带（Sprite，雾外着色，随暮色呼吸）—— */
function makeBand(o){
  o=o||{};
  const s=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),
    color:o.color===undefined?0xa8848c:o.color,
    transparent:true,opacity:o.op===undefined?0.16:o.op,depthWrite:false,fog:false,
    blending:o.add===false?THREE.NormalBlending:THREE.AdditiveBlending}));
  s.scale.set(o.w===undefined?240:o.w,o.h===undefined?30:o.h,1);
  s.position.set(o.x===undefined?0:o.x,o.y===undefined?11:o.y,o.z===undefined?-105:o.z);
  s.renderOrder=o.order===undefined?1:o.order;
  return s;
}

/* —— 危楼露台：台基 + 面江栏杆（望柱两道横栏）+ 两侧亭柱（合批 1 mesh）—— */
function makeTerrace(){
  const B=new GeoBag(), c1=0x131824, c2=0x1a2130, c3=0x0e131d;
  const deck=new THREE.BoxGeometry(26,0.9,30); deck.translate(0,1.75,3); B.put(deck,c1);
  const lip=new THREE.BoxGeometry(26.7,0.24,30.7); lip.translate(0,2.26,3); B.put(lip,shadeColor(c1,1.35));
  const plinth=new THREE.BoxGeometry(29,3.6,33); plinth.translate(0,-0.5,3); B.put(plinth,c3);
  for(let i=0;i<10;i++){
    const x=-11.7+i*2.6;
    const post=new THREE.BoxGeometry(0.20,2.0,0.20); post.translate(x,3.2,-11.6); B.put(post,c2);
    const cap=new THREE.BoxGeometry(0.34,0.16,0.34); cap.translate(x,4.28,-11.6); B.put(cap,shadeColor(c2,1.25));
  }
  [3.95,3.05].forEach(function(y){
    const rail=new THREE.BoxGeometry(24.2,0.13,0.16); rail.translate(0,y,-11.6); B.put(rail,shadeColor(c2,1.4));
  });
  [1,-1].forEach(function(s){
    const bs=new THREE.BoxGeometry(1.0,0.36,1.0); bs.translate(s*11.4,2.38,7.5); B.put(bs,c3);
    const col=new THREE.CylinderGeometry(0.22,0.26,4.6,8); col.translate(s*11.4,4.86,7.5); B.put(col,c2);
  });
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x36424e,emissive:0x05080c}),{c:0x90a8c0,i:0.30,p:2.5})));
  return g;
}

/* —— 远处危楼剪影（封面伏笔，合批 1 mesh）—— */
function makeYuanlou(){
  const B=new GeoBag(), c1=0x0d1219, c2=0x111826;
  const base=new THREE.BoxGeometry(6.5,1.0,5.2); base.translate(0,0.5,0); B.put(base,c1);
  const body=new THREE.BoxGeometry(4.6,5.6,3.8); body.translate(0,1.0+2.8,0); B.put(body,c1);
  const ledge=new THREE.BoxGeometry(3.4,0.18,1.2); ledge.translate(-0.5,6.69,2.1); B.put(ledge,c2);
  const r1=new THREE.ConeGeometry(3.8,1.5,4); r1.rotateY(Math.PI/4); r1.scale(1.2,1,1.05);
  r1.translate(0,6.6+0.75,0); B.put(r1,c2);
  const upper=new THREE.BoxGeometry(3.4,2.8,2.8); upper.translate(-0.5,8.1+1.4,0); B.put(upper,c2);
  const r2=new THREE.ConeGeometry(2.9,1.2,4); r2.rotateY(Math.PI/4); r2.scale(1.15,1,1.05);
  r2.translate(-0.5,10.9+0.6,0); B.put(r2,c2);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x90a8c0,i:0.22,p:2.4})));
  return g;
}

function bCover(){ // 封面 · 暮烟江天（残照将尽，远处危楼孤倚一人）
  const g=new THREE.Group();
  const water=makeWater({size:680,seg:88,amp:0.4,freq:0.09,speed:0.42,flow:[0,0.3],
    deep:0x0b1220,shallow:0x15243a,skyc:0x27334a,spec:0.6,moonDir:[0.42,0.10,-0.90],y:-0.6});
  g.add(water.mesh);
  const bank=makeGround({r:80,c1:0x0b1210,c2:0x17221b});
  bank.mesh.position.set(0,-0.3,70); g.add(bank.mesh);
  const ridge=makeRange({r:270,h:15,layers:2,peaks:4,seed:17001,color:0x0b0f16,atmo:0x39455c,fogK:0.66,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-58); g.add(ridge.g);
  /* 残照（藕荷余晖）+ 黯黯暮霭横带 */
  const dusk=makeBand({color:0xa8848c,op:0.22,w:280,h:34,x:18,y:9.5,z:-100}); g.add(dusk);
  const dark=makeBand({color:0x151d29,op:0.42,add:false,w:320,h:26,x:0,y:5.5,z:-84,order:2}); g.add(dark);
  /* 远处危楼剪影 + 楼头一点凭阑人影 */
  const isle=makeGround({r:16,c1:0x0b0f15,c2:0x121a22});
  isle.mesh.position.set(-15,-0.55,-44); g.add(isle.mesh);
  const lou=makeYuanlou(); lou.position.set(-15,-0.3,-44); g.add(lou);
  const farman=makeFigure({pose:'独立',robe:0x141b26,belt:0x39434f,skin:0xb5a792,collar:0x8fa2ba,
    hat:'幞头',beard:true,rimC:0x90a8c0,rim:0.3,noProp:true,scale:0.5});
  farman.position.set(-15.5,6.48,-41.9); farman.rotation.y=0.4; g.add(farman);
  /* 风细细 + 浮尘 + 烟雾 */
  const wind=makeFlow({n:160,box:[200,16,70],pos:[0,8,-34],color:0x93a8c0,size:12,speed:3.2,maxA:0.11});
  g.add(wind.points);
  const motes=makeGlow({n:36,box:[130,18,60],pos:[0,7,-22],color:0x9fb2c4,size:5,speed:0.06,rise:0,maxA:0.2});
  g.add(motes.points);
  const mist=makeMist({n:8,spread:[240,24,110],pos:[0,8,-52],scale:76,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'芦苇',w:44,n:13,d:6,color:0x0a0e13,seed:17003,sway:0.8,tip:0x26323c});
  fg.g.position.set(-9,-1.2,18); g.add(fg.g);
  const tree=makeForeground({kind:'树枝',n:2,w:14,d:4,color:0x0a0e13,seed:17004,sway:1.0,rim:0.14});
  tree.g.position.set(13,-0.6,14); g.add(tree.g);
  addLights(g,{c:0x93a4bc,i:0.34,p:[-40,60,-30]},{c:0x242e3c,i:0.64});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); wind.update(t); motes.update(t);
    mist.update(t,k); fg.update(t,k); tree.update(t,k); farman.update(t,k);
    dusk.material.opacity=k*0.22*(0.82+0.18*Math.sin(t*0.10));
    dark.material.opacity=k*0.42*(0.92+0.08*Math.sin(t*0.23+1.7));
  }};
}

function bWeilou(){ // 一 · 伫倚危楼 —— 望极春愁黯黯生天际；草色烟光残照里，无言谁会凭阑意
  const g=new THREE.Group();
  const water=makeWater({size:720,seg:92,amp:0.42,freq:0.085,speed:0.45,flow:[0,0.35],
    deep:0x0b1220,shallow:0x15243a,skyc:0x27334a,spec:0.55,moonDir:[0.42,0.10,-0.90],y:-0.7});
  g.add(water.mesh);
  const grass=makeGround({r:95,c1:0x0b1210,c2:0x152019});
  grass.mesh.position.set(0,-0.2,62); g.add(grass.mesh);
  const ridge=makeRange({r:280,h:17,layers:2,peaks:5,seed:17005,color:0x0b0f16,atmo:0x39455c,fogK:0.64,glowK:0.05,y:-12});
  ridge.g.position.set(0,0,-54); g.add(ridge.g);
  /* 黯黯春愁自天际暗生：暮霭横带 + 贴地愁雾；残照（藕荷余晖，将尽） */
  const dark=makeBand({color:0x141c28,op:0.40,add:false,w:330,h:26,x:0,y:5.5,z:-84,order:2}); g.add(dark);
  const sorrow=makeFlow({n:300,box:[360,10,90],pos:[0,2.5,-58],color:0x2a3648,size:26,speed:3.2,maxA:0.22});
  g.add(sorrow.points);
  const dusk=makeBand({color:0xa8848c,op:0.20,w:270,h:34,x:18,y:9.5,z:-100}); g.add(dusk);
  /* 危楼露台 + 凭阑人（背影居左，无言倚栏，避开右侧词句竖排区） */
  const terrace=makeTerrace(); g.add(terrace);
  const poet=makeFigure({pose:'独立',robe:0x2a3444,belt:0x3c4756,skin:0xc4b39c,collar:0x93a4bc,
    hat:'幞头',beard:true,rimC:0x90a8c0,rim:0.55,scale:1.32});
  poet.position.set(-3.5,2.2,-11.2); poet.rotation.y=Math.PI-0.2; poet.rotation.x=0.045; g.add(poet);
  /* 岸边渡头远景人影（谁会凭阑意——无人会得） */
  const crowd=makeCrowd({n:3,rect:[-32,-28,14,6],seed:17007,color:0x11161e,rimC:0x5a6a7a,rim:0.16,sMin:0.5,sMax:0.72});
  g.add(crowd.mesh);
  /* 风细细 + 草色烟光浮尘 + 烟雾 */
  const wind=makeFlow({n:180,box:[190,15,72],pos:[0,8,-30],color:0x93a8c0,size:12,speed:3.4,maxA:0.12});
  g.add(wind.points);
  const motes=makeGlow({n:40,box:[130,18,64],pos:[0,7,-20],color:0x9fb2c4,size:5,speed:0.06,rise:0,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,22,105],pos:[0,8,-50],scale:78,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const fg=makeForeground({kind:'树枝',n:2,w:9,d:4,color:0x0a0e13,seed:17009,sway:1.1,rim:0.14});
  fg.g.position.set(-7.5,2.8,3.5); g.add(fg.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x080b10,seed:17010,rim:0.12});
  rk.g.position.set(-18,-0.8,7); g.add(rk.g);
  addLights(g,{c:0x93a4bc,i:0.32,p:[-40,60,-30]},{c:0x232d3b,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    water.update(t); ridge.update(t,0); sorrow.update(t); wind.update(t); motes.update(t);
    mist.update(t,k); fg.update(t,k); rk.update(t,k); crowd.update(t); poet.update(t,k);
    dark.material.opacity=k*0.40*(0.92+0.08*Math.sin(t*0.21+1.7));
    dusk.material.opacity=k*0.20*(0.80+0.20*Math.sin(t*0.10));
  }};
}

function bYidai(){ // 二（标志性瞬间·末境可点击）· 衣带渐宽 —— 拟醉无味；点击凭阑人：衣带渐宽、身形渐瘦，春愁铺满天际
  const ctl={t:0,clicked:false,ext:0};
  const g=new THREE.Group();
  const water=makeWater({size:760,seg:92,amp:0.45,freq:0.085,speed:0.45,flow:[0,0.4],
    deep:0x0b1220,shallow:0x15243a,skyc:0x27334a,spec:0.55,moonDir:[0.42,0.10,-0.90],y:-0.7});
  g.add(water.mesh);
  const grass=makeGround({r:100,c1:0x0b1210,c2:0x152019});
  grass.mesh.position.set(0,-0.2,66); g.add(grass.mesh);
  const ridge=makeRange({r:300,h:15,layers:2,peaks:5,seed:17011,color:0x0a0e15,atmo:0x39455c,fogK:0.62,glowK:0.05,y:-13});
  ridge.g.position.set(0,0,-60); g.add(ridge.g);
  /* 黯黯春愁（点击后铺满天际）；残照将尽（点击后被愁云吞去大半）——初值=最大值 0.62 */
  const dark=makeBand({color:0x141c28,op:0.62,add:false,w:340,h:26,x:0,y:5.5,z:-86,order:2}); g.add(dark);
  const sorrow=makeFlow({n:340,box:[380,11,95],pos:[0,2.5,-60],color:0x2a3648,size:27,speed:3.2,maxA:0.20});
  g.add(sorrow.points);
  const dusk=makeBand({color:0xa8848c,op:0.20,w:270,h:34,x:-24,y:9.5,z:-102}); g.add(dusk);
  /* 露台 + 凭阑人（标志瞬间主体） */
  const terrace=makeTerrace(); g.add(terrace);
  const poet=makeFigure({pose:'独立',robe:0x2a3444,belt:0x3c4756,skin:0xc4b39c,collar:0x93a4bc,
    hat:'幞头',beard:true,rimC:0x90a8c0,rim:0.62,scale:1.30});
  const SC=1.30;
  poet.position.set(-2.1,2.2,-11.2); poet.rotation.y=Math.PI+0.42; poet.rotation.x=0.05; g.add(poet);
  /* 衣带：腰带环 + 带结（合批 1 mesh）+ 两条垂带（独立组，点击后松宽垂落摆动） */
  const beltG=new THREE.Group();
  const BT=new GeoBag();
  const ring=new THREE.TorusGeometry(0.70,0.055,7,26); ring.rotateX(Math.PI/2); ring.scale(1,1,0.86);
  ring.translate(0,1.74,0); BT.put(ring,0x7d8ea2);
  const knot=new THREE.BoxGeometry(0.16,0.30,0.10); knot.translate(0,1.66,0.56);
  BT.put(knot,shadeColor(0x7d8ea2,1.25));
  beltG.add(new THREE.Mesh(mergeGeos(BT.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:14,
      specular:0x4a5568,emissive:0x080a10}),{c:0xc0cedd,i:0.4,p:2.4})));
  const ribG=new THREE.Group(); ribG.position.set(0,1.70,0.58);
  const RB=new GeoBag();
  [-1,1].forEach(function(s){
    const rb=new THREE.BoxGeometry(0.085,1.15,0.028); rb.translate(0.10*s,-0.575,0);
    RB.put(rb,s<0?0x9a828e:shadeColor(0x9a828e,1.2));
  });
  const rib=new THREE.Mesh(mergeGeos(RB.list),
    rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:12,
      specular:0x4a4248,emissive:0x0a0708}),{c:0xd8b8c0,i:0.34,p:2.3}));
  ribG.add(rib); beltG.add(ribG);
  poet.add(beltG);
  /* 拟把疏狂图一醉：案上一壶一杯（杯已横倒——强乐无味），陶玉禁金 */
  const table=makeTable({w:2.2,d:1.0,h:1.3,wood:0x1e1712}); table.g.position.set(6.2,2.2,-7.2); g.add(table.g);
  const hu=makeVessel({type:'壶',mat:'陶',scale:0.46}); hu.g.position.set(6.0,3.52,-7.1); g.add(hu.g);
  const cup=makeVessel({type:'杯',mat:'玉',scale:0.4,liquid:true}); cup.g.position.set(6.7,3.52,-7.5); cup.g.rotation.z=1.25; g.add(cup.g);
  /* 点击光效 */
  const burst=makeBurst({n:70,color:0xbcd0e2,pos:[-2.1,4.4,-10.0]}); g.add(burst.points);
  /* 风细细 + 浮尘 + 烟雾 */
  const wind=makeFlow({n:180,box:[190,15,72],pos:[0,8,-30],color:0x93a8c0,size:12,speed:3.4,maxA:0.12});
  g.add(wind.points);
  const motes=makeGlow({n:40,box:[130,18,64],pos:[0,7,-18],color:0x9fb2c4,size:5,speed:0.06,rise:0,maxA:0.22});
  g.add(motes.points);
  const mist=makeMist({n:7,spread:[230,22,105],pos:[0,8,-52],scale:78,color:0x8fa4c0,op:0.10});
  g.add(mist.g);
  const tree=makeForeground({kind:'树枝',n:2,w:9,d:4,color:0x0a0e13,seed:17013,sway:1.0,rim:0.14});
  tree.g.position.set(-5.5,1.6,1.5); g.add(tree.g);
  const rk=makeForeground({kind:'坡石',n:2,r:2.6,w:10,d:5,color:0x080b10,seed:17014,rim:0.12});
  rk.g.position.set(11,-0.8,3); g.add(rk.g);
  addLights(g,{c:0x8fa2ba,i:0.32,p:[-40,60,-30]},{c:0x212b39,i:0.60});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.clicked)ctl.ext=Math.min(1,ctl.ext+dt/2.8);
      const e=ctl.ext;
      water.update(t); ridge.update(t,0); sorrow.update(t); wind.update(t); motes.update(t);
      mist.update(t,k); tree.update(t,k); rk.update(t,k); poet.update(t,k);
      hu.update(t,k); cup.update(t,k); burst.update(t);
      dark.material.opacity=k*(0.36+0.26*e)*(0.92+0.08*Math.sin(t*0.21+1.7));
      dusk.material.opacity=k*(0.20*(1-0.55*e))*(0.80+0.20*Math.sin(t*0.10));
      sorrow.mat.uniforms.uMaxA.value=k*(0.20+0.34*e);
      wind.mat.uniforms.uMaxA.value=k*(0.12+0.06*e);
      /* 衣带渐宽·身形渐瘦（王国维第二境的具象化） */
      poet.scale.set(SC*(1-0.10*e),SC,SC*(1-0.05*e));
      beltG.scale.set((1+0.30*e)/(1-0.10*e),1+0.06*e,(1+0.30*e)/(1-0.05*e));
      beltG.position.y=-0.12*e;
      ribG.rotation.z=0.05*Math.sin(t*1.2)+0.16*e*Math.sin(t*1.35);
      ribG.rotation.x=0.12*e*(0.6+0.4*Math.sin(t*0.9));
      rib.scale.y=1+0.55*e;
      poet.children[0].scale.x=1-0.10*e;
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true;
        burst.fire(); pluck(1,0.1,0.14); pluck(3,0.55,0.12); pluck(5,1.0,0.13);
        const fl=$('#flash'); fl.textContent='衣带渐宽终不悔'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x111722),hor:C(0x232e3d),bot:C(0x0b0e14),fog:C(0x161d27),fd:0.014,star:0.05,
  moon:new THREE.Vector3(0,-220,-160),ms:0.001,mph:0,mhaze:0,dirC:C(0x93a4bc),dirI:0.32,
  dirP:new THREE.Vector3(-40,60,-30),ambC:C(0x232d3b),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.014,build:bCover,
  cam:{f:[0,7.6,46],t:[0.7,7.3,41],lf:[0,7,-42],lt:[0.7,7.4,-48]},
  sky:()=>SK({top:C(0x121823),hor:C(0x252f3e),bot:C(0x0b0e14),fog:C(0x151c26),fd:0.013,star:0.06,
    dirC:C(0x93a4bc),dirI:0.34,ambC:C(0x242e3c),ambI:0.64}) },
{ name:'伫倚危楼',dwell:19,river:0.014,build:bWeilou,
  cam:{f:[0,5.9,13.5],t:[0.4,5.6,10.5],lf:[-2.5,4.6,-30],lt:[-1.8,4.9,-40]},
  sky:()=>SK({top:C(0x111722),hor:C(0x242e3d),bot:C(0x0b0e14),fog:C(0x161d27),fd:0.014,star:0.05,
    dirC:C(0x93a4bc),dirI:0.32,ambC:C(0x232d3b),ambI:0.62}) },
{ name:'衣带渐宽',dwell:19,river:0.014,build:bYidai,
  cam:{f:[3.4,4.7,1.2],t:[1.6,4.5,-2.0],lf:[-2.2,4.0,-12],lt:[-1.4,4.1,-16]},
  sky:()=>SK({top:C(0x0f1520),hor:C(0x212b3a),bot:C(0x0a0d13),fog:C(0x151c26),fd:0.014,star:0.04,
    dirC:C(0x8fa2ba),dirI:0.30,ambC:C(0x212b39),ambI:0.60}) },
];
"""
