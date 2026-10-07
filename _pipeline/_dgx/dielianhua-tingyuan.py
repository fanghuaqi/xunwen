# -*- coding: utf-8 -*-
"""dielianhua-tingyuan.py —— 《蝶恋花·庭院深深深几许》（宋·欧阳修，no.166，水墨夜思）生成配置
两境（queue 口径 N=2，上下片各一境）：
  壹 · 庭院深深 —— 三个「深」字题眼：院门→回廊→帘幕无重数→深闺小楼，层层递深；
                    杨柳堆烟，远处玉勒雕鞍奔游冶处，楼高望断章台路。
  贰 · 泪眼问花 ——（标志性瞬间·末境可点击）雨横风狂的动态天气（斜雨+摆树），
                    门掩黄昏徐徐转沉，泪眼问花花不语；点击：花枝乱颤+红瓣飞过秋千。
水墨禁金：全页冷银水墨，乱红（落花红瓣）是唯一暖彩点。"""
import io, os
def io_open(n):
    return io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), n), encoding='utf-8').read()

META = dict(
    N=2, slug='dielianhua-tingyuan', title='蝶恋花·庭院深深深几许', dyn='宋 · 欧阳修', brand_author='欧 阳 修',
    gold_rgb='168,180,201',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#a8b4c9; --ink:#dfe6f0; --dim:#7e8ea8; --paper:rgba(9,13,22,.58);
  --line:rgba(168,180,201,.26);
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
    tip='轻点画面 / 按空格 —— 泪眼问花，乱红飞过秋千',
    hint='← → 键或空格逐境游览 · 末境可点击问花，看红瓣飞过秋千',
    cover_read='蝶恋花。宋，欧阳修。庭院深深深几许，杨柳堆烟，帘幕无重数。玉勒雕鞍游冶处，楼高不见章台路。',
    cover_p1='两重意境，随词句次第展开：庭院深深，杨柳堆烟，帘幕重重数不清；玉勒雕鞍奔游冶处，楼高望断章台路；暮春风雨横狂，门掩黄昏，留春不住；泪眼问花，花自不语，乱红飞过秋千去。',
    cover_p2='边读词，边走进欧阳修笔下这座望不到底的深深庭院——三个「深」字一重重走进去，末了立在雨后花前，看乱红掠过秋千。',
    end_h2='乱红 · 秋千', cn_word='两',
    words_js="['再游一次，重问花开','初识欧阳修，尚需共读','渐入佳境，庭院渐深','帘幕数清，意境渐明','泪眼问花，花亦有情','乱红过尽，深婉之至']",
    sky_atmo='0x1f2a3d',
)

POEM_JS = """const POEM = [
{ name:'庭院深深', jing:'庭院深深，不知几许；杨柳如烟，帘幕层层——愈深愈静，愈静愈愁。看玉勒雕鞍远去，楼高望断章台路。（院门 · 帘幕 · 深闺楼）',
  segs:[
   {c:'庭院深深深几许，', p:py('tíng yuàn shēn shēn shēn jǐ xǔ')},
   {c:'杨柳堆烟，', p:py('yáng liǔ duī yān')},
   {c:'帘幕无重数。', p:py('lián mù wú chóng shù')},
   {c:'玉勒雕鞍游冶处，', p:py('yù lè diāo ān yóu yě chù')},
   {c:'楼高不见章台路。', p:py('lóu gāo bú jiàn zhāng tái lù')}],
  read:'庭院深深深几许，杨柳堆烟，帘幕无重数。玉勒雕鞍游冶处，楼高不见章台路。',
  yisi:'庭院深深，到底有多深？杨柳茂密如烟雾堆聚，重重帘幕数也数不清。那边是玉勒雕鞍的游冶之处——他纵马远去了；这边楼纵然再高，也望不见他所流的连的章台路。',
  zhu:[['几许','多少（读 jǐ）；连用三个「深」字是本词题眼——庭院之深即相思之深、寂寞之深'],['堆烟','杨柳枝叶繁密，如烟雾堆积；柳色朦胧，恰似望不见底的愁绪'],['帘幕无重数','帘幕重重叠叠难以数清；「重」读 chóng，层也——层帘深幕，深闺更幽'],['玉勒雕鞍','镶玉的马笼头、雕花的华贵马鞍，代指远游冶游的情人'],['章台路','汉长安章台下的街路，旧时游冶之地；楼高望而不见，人去路远，怨在言外']] },
{ name:'泪眼问花', jing:'雨横风狂，门掩黄昏；泪眼问花，花自不语，乱红飞过秋千去。（点击问花：花枝乱颤，红瓣掠过秋千）',
  segs:[
   {c:'雨横风狂三月暮，', p:py('yǔ hèng fēng kuáng sān yuè mù')},
   {c:'门掩黄昏，', p:py('mén yǎn huáng hūn')},
   {c:'无计留春住。', p:py('wú jì liú chūn zhù')},
   {c:'泪眼问花花不语，', p:py('lèi yǎn wèn huā huā bù yǔ')},
   {c:'乱红飞过秋千去。', p:py('luàn hóng fēi guò qiū qiān qù')}],
  read:'雨横风狂三月暮，门掩黄昏，无计留春住。泪眼问花花不语，乱红飞过秋千去。',
  yisi:'雨下得急、风刮得狂，正是三月暮春时节；掩上院门，黄昏悄然四合，千般心思也无法把春天留住。含着泪问花，花却默默不语，只见零乱的落红，忽悠悠地飞过那架秋千去了。',
  zhu:[['横','凶暴、放纵（读 hèng）；「雨横」言雨势暴烈，与「风狂」互文，见暮春风雨之骤'],['门掩黄昏','掩门之际暮色四合；一个「掩」字，把黄昏关在门外，把人关进深深的寂寞里'],['乱红','零乱的落花；春不可留，人不可留，乱红过尽，青春亦随之飘逝'],['秋千','庭院中秋千架，旧时闺中人嬉游之物——花过秋千而架久空悬，物是人非之痛尽在言外']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「庭院深深深几许」的下一句是？', o:['杨柳堆烟，帘幕无重数','玉勒雕鞍游冶处','雨横风狂三月暮'], a:0},
 {q:'「泪眼问花花不语」的下一句是？', o:['门掩黄昏，无计留春住','乱红飞过秋千去','楼高不见章台路'], a:1},
 {q:'「雨横风狂三月暮」中「横」的正确读音与意思是？', o:['héng，与「竖」相对','héng，横竖、反正','hèng，凶暴、放纵（雨势暴烈）'], a:2},
 {q:'「章台路」在词中指什么？', o:['宫廷中珍藏图籍的台阁','汉长安章台下的街路，旧时游冶之地，借指情人流连不归处','送别友人必经的驿站长亭'], a:1},
 {q:'从「庭院深深」到「乱红飞过秋千去」，全词主要抒发什么？', o:['闺中人幽居深闺、望人不归，青春如乱红般飘逝的哀怨','暮春赏花踏青的闲适之乐','登高望远、壮志难酬的悲慨'], a:0},
];
"""

SCENES_JS = """/* ================= 蝶恋花 · 两境场景（水墨夜思：庭院深深、泪眼问花） ================= */

/* 垂柳：曲干 + 下垂披拂的柳丝（合批 1 mesh；风摆在 update 里整体微转） */
function makeLiushu(o){
  o=o||{};
  const B=new GeoBag(), R=seedRnd(o.seed===undefined?11:o.seed);
  const h=o.h===undefined?7.5:o.h;
  const cTrunk=0x0b0e14, cTwig=0x10151f;
  const t0=new THREE.CylinderGeometry(0.10,0.30,h*0.42,6);
  t0.rotateZ((R()-0.5)*0.2); t0.translate(0,h*0.21,0); B.put(t0,cTrunk);
  const t1=new THREE.CylinderGeometry(0.06,0.11,h*0.30,5);
  t1.rotateZ((R()-0.5)*0.34); t1.translate((R()-0.5)*0.5,h*0.42+h*0.14,0); B.put(t1,cTrunk);
  const nb=o.fronds===undefined?9:o.fronds;
  for(let i=0;i<nb;i++){
    const a=i/nb*Math.PI*2+R()*0.7, rr=h*(0.24+R()*0.22);
    const bx=Math.cos(a)*rr, bz=Math.sin(a)*rr*0.8, by=h*(0.48+R()*0.24);
    let px=bx*0.35, py=by, pz=bz*0.35;
    const segs=4, len=h*(0.42+R()*0.20);
    for(let k2=0;k2<segs;k2++){
      const t2=k2/segs;
      const nx=bx*(0.35+0.65*t2)+(R()-0.5)*0.4, ny=by-len*Math.pow(t2,1.7), nz=bz*(0.35+0.65*t2)+(R()-0.5)*0.4;
      const seg=new THREE.CylinderGeometry(0.03,0.05,Math.hypot(nx-px,ny-py,nz-pz)*1.05,4,1,true);
      seg.translate((px+nx)/2,(py+ny)/2,(pz+nz)/2); B.put(seg,cTwig);
      if(R()<0.65){
        const leaf=new THREE.PlaneGeometry(0.5,1.6+R()*1.2);
        leaf.rotateZ(0.24); leaf.translate((px+nx)/2+(R()-0.5)*0.3,(py+ny)/2-0.7,(pz+nz)/2);
        B.put(leaf,shadeColor(0x1a2636,0.8+R()*0.6));
      }
      px=nx; py=ny; pz=nz;
    }
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.18,p:2.3})));
  return g;
}

/* 深闺小楼：两层 + 檐 + 顶层阁窗（帘幕深处那人所在），合批 1 mesh */
function makeGuiLou(){
  const B=new GeoBag(), c1=0x0c1017, c2=0x111723, c3=0x161d2b, c4=0x1b2331;
  const base=new THREE.BoxGeometry(9,1.0,6.4); base.translate(0,0.5,0); B.put(base,c1);
  const hall=new THREE.BoxGeometry(6.4,5.6,4.6); hall.translate(0,1.0+2.8,0); B.put(hall,c2);
  const roof1=new THREE.ConeGeometry(5.4,1.8,4); roof1.rotateY(Math.PI/4);
  roof1.scale(1.26,1,1.08); roof1.translate(0,6.6+0.9,0); B.put(roof1,c3);
  const upper=new THREE.BoxGeometry(4.4,3.6,3.6); upper.translate(0,8.4+1.8,0); B.put(upper,c2);
  const roof2=new THREE.ConeGeometry(3.7,1.5,4); roof2.rotateY(Math.PI/4);
  roof2.scale(1.2,1,1.02); roof2.translate(0,12.0+0.75,0); B.put(roof2,c3);
  /* 阁窗（冷光所出）+ 檐廊小栏杆 + 门 */
  const win=new THREE.BoxGeometry(1.9,1.5,0.16); win.translate(0,10.6,1.82); B.put(win,0x0e141f);
  [-0.55,0,0.55].forEach(function(dx){
    const slat=new THREE.BoxGeometry(0.09,1.4,0.2); slat.translate(dx,10.6,1.84); B.put(slat,c4);
  });
  for(let i=0;i<5;i++){
    const post=new THREE.BoxGeometry(0.1,0.85,0.1); post.translate(-2.4+i*1.2,8.4+0.62,1.92); B.put(post,c4);
  }
  const door=new THREE.BoxGeometry(1.7,3.2,0.22); door.translate(0,1.0+1.6,2.32); B.put(door,0x0a0e14);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:10,
    specular:0x3a465c,emissive:0x05070c}),{c:0xa8b4c9,i:0.34,p:2.5})));
  return g;
}

/* 游骑：玉勒雕鞍（马身+鞍+骑者剪影），合批 1 mesh（远去路径在 update 里驱动） */
function makeYouQi(){
  const B=new GeoBag(), cH=0x0a0e15, cR=0x18202f, cS=0x2a3550;
  const body=new THREE.SphereGeometry(1.0,9,6); body.scale(1.55,0.62,0.5);
  body.translate(0,1.45,0); B.put(body,cH);
  const neck=new THREE.CylinderGeometry(0.16,0.30,1.1,5);
  neck.rotateZ(-0.6); neck.translate(1.35,2.15,0); B.put(neck,cH);
  const head=new THREE.BoxGeometry(0.62,0.26,0.24); head.rotateZ(-0.25);
  head.translate(1.92,2.62,0); B.put(head,cH);
  [[0.95,0.12],[0.95,-0.12],[-0.85,0.12],[-0.85,-0.12]].forEach(function(l){
    const leg=new THREE.CylinderGeometry(0.07,0.05,1.25,4);
    leg.translate(l[0],0.62,l[1]); B.put(leg,cH);
  });
  const tail=new THREE.ConeGeometry(0.09,0.85,4); tail.rotateZ(0.7);
  tail.translate(-1.62,1.5,0); B.put(tail,cH);
  const saddle=new THREE.BoxGeometry(0.72,0.2,0.5); saddle.translate(0.12,1.88,0); B.put(saddle,cS);
  const torso=new THREE.SphereGeometry(0.4,7,5); torso.scale(0.72,1.15,0.62);
  torso.translate(0.1,2.5,0); B.put(torso,cR);
  const hr=new THREE.SphereGeometry(0.2,7,5); hr.translate(0.1,3.16,0); B.put(hr,0xb5a792);
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x3a465c,emissive:0x04060a}),{c:0x9fb2cc,i:0.38,p:2.4})));
  return g;
}

function bCover(){ // 封面 · 墨夜深苑
  const g=new THREE.Group();
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-2; g.add(grd.mesh);
  const ridge=makeRange({r:150,h:22,layers:2,peaks:4,seed:16601,color:0x070a10,atmo:0x1f2a3d,fogK:0.72,glowK:0.07,y:-12});
  ridge.g.position.set(0,0,40); g.add(ridge.g);
  /* 远处院墙门楼剪影 + 门前望远人影（深深庭院之伏笔） */
  const B=new GeoBag(), c1=0x0b0f16, c2=0x10151f;
  const wall=new THREE.BoxGeometry(16,4.6,1.2); wall.translate(0,2.3,0); B.put(wall,c1);
  const gt=new THREE.BoxGeometry(3.4,7.0,2.4); gt.translate(0,3.5,0); B.put(gt,c2);
  const grf=new THREE.ConeGeometry(2.9,1.3,4); grf.rotateY(Math.PI/4);
  grf.translate(0,7.0+0.65,0); B.put(grf,c2);
  const yard=new THREE.Group();
  yard.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0x8fa4c4,i:0.2,p:2.4})));
  yard.position.set(-26,0,-58); g.add(yard);
  const farman=makeFigure({pose:'独立',robe:0x141c28,belt:0x3c4a60,skin:0xb5a792,collar:0x94a4bc,
    hat:'发髻',rimC:0x8fa4c4,rim:0.3,noProp:true,scale:0.8});
  farman.position.set(-19.5,0,-52); farman.rotation.y=0.7; g.add(farman);
  const w1=makeLiushu({h:8,seed:16602}); w1.position.set(14,0,-50); g.add(w1);
  const fg=makeForeground({kind:'坡石',n:3,r:4.2,w:26,d:9,color:0x04060a,seed:16603,rim:0.14});
  fg.g.position.set(0,-2,26); g.add(fg.g);
  const tree=makeForeground({kind:'树枝',n:2,w:15,d:5,color:0x04060a,seed:16604,sway:1.1,rim:0.16});
  tree.g.position.set(15,-1.5,24); g.add(tree.g);
  const mist=makeMist({n:9,spread:[240,34,160],pos:[0,11,-55],scale:82,color:0x8fa4c4,op:0.085});
  g.add(mist.g);
  const motes=makeGlow({n:60,box:[210,38,120],pos:[0,10,-40],color:0xa8bcd8,size:8,speed:0.05,rise:0,maxA:0.36});
  g.add(motes.points);
  addLights(g,{c:0x8fa4c8,i:0.42,p:[30,70,40]},{c:0x182031,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); fg.update(t,k); tree.update(t,k); mist.update(t,k); motes.update(t); }};
}

function bTingYuan(){ // 一 · 庭院深深 —— 三个「深」层层递深：院门→回廊→帘幕无重数→深闺楼
  const g=new THREE.Group(), st={t:0};
  const grd=makeGround({r:150,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-0.4; g.add(grd.mesh);
  const ridge=makeRange({r:240,h:18,layers:2,peaks:4,seed:16605,color:0x070a10,atmo:0x1f2a3d,fogK:0.64,glowK:0.06,y:-16});
  ridge.g.position.set(0,0,-100); g.add(ridge.g);
  /* 深之一：院门（两柱一梁，虚框景） */
  const B=new GeoBag(), c1=0x0c1017, c2=0x121826, c3=0x171f2d;
  [-2.6,2.6].forEach(function(dx){
    const post=new THREE.BoxGeometry(0.5,5.2,0.5); post.translate(dx,2.6,-8); B.put(post,c1);
  });
  const liang=new THREE.BoxGeometry(6.6,0.6,0.7); liang.translate(0,5.4,-8); B.put(liang,c2);
  const menE=new THREE.BoxGeometry(4.0,4.4,0.24); menE.translate(5.9,2.2,-8); B.put(menE,0x0e141f);
  /* 深之二：回廊短墙（左右两列廊柱+栏板） */
  [-1,1].forEach(function(s){
    for(let i=0;i<5;i++){
      const p=new THREE.BoxGeometry(0.34,3.6,0.34);
      p.translate(s*(6.2+i*2.4),1.8,-12-i*3.4); B.put(p,c2);
    }
    const rail=new THREE.BoxGeometry(0.24,0.16,18.4);
    rail.translate(s*9.2,1.05,-18.6); B.put(rail,c1);
    const wall=new THREE.BoxGeometry(0.4,2.6,17.0);
    wall.translate(s*10.6,1.3,-19.5); B.put(wall,c3);
  });
  const gate=new THREE.Group();
  gate.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:9,
    specular:0x3a465c,emissive:0x05070c}),{c:0xa8b4c9,i:0.3,p:2.4})));
  g.add(gate);
  /* 深之三：帘幕无重数——四重垂幕沿纵深递远，左右交错留缝，缝隙里一重重望进去 */
  const CW=[6.2,6.8,6.4,7.0], CX=[-2.5,2.4,-2.1,1.9], CZ=[-16.5,-20.5,-24.5,-28.5];
  for(let i=0;i<4;i++){
    const cu=makeCurtain({w:CW[i],h:5.8+i*0.35,color:0x1c2434,dark:0x0d1320,folds:6,deep:0.5});
    cu.g.position.set(CX[i],0.5,CZ[i]); cu.g.rotation.y=(CX[i]>0?-1:1)*0.1;
    cu.mesh.material.transparent=true; cu.mesh.material.opacity=0.45;
    g.add(cu.g);
  }
  /* 深之四：帘幕尽处的深闺小楼 + 楼头冷窗 + 伫立人影 */
  const lou=makeGuiLou(); lou.position.set(0,0,-38); g.add(lou);
  const win=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xcfdff2,
    transparent:true,opacity:0.30,depthWrite:false,blending:THREE.AdditiveBlending}));
  win.scale.set(3.8,3.8,1); win.position.set(0,10.6,-36.0); win.renderOrder=2; g.add(win);
  const figure=makeFigure({pose:'独立',robe:0x1f2a3e,belt:0x516282,skin:0xcbb9a2,collar:0xb6c4d8,
    hat:'发髻',rimC:0xa8b4c9,rim:0.55,noProp:true,scale:1.5});
  figure.position.set(-1.5,1.0,-34.6); figure.rotation.y=0.3; g.add(figure);
  /* 杨柳堆烟：柳各一株 + 柳冠堆烟 */
  const w1=makeLiushu({h:8.5,seed:16606}); w1.position.set(-13,0,-22); g.add(w1);
  const w2=makeLiushu({h:7.5,seed:16607}); w2.position.set(13.5,0,-27); g.add(w2);
  const smoke=makeMist({n:6,spread:[26,5,10],pos:[0.2,9.6,-24.5],scale:11,color:0x9fb0c8,op:0.16});
  g.add(smoke.g);
  /* 玉勒雕鞍游冶处：远骑循路远去 + 路口人影 + 雾里隐没的章台路（楼高不见） */
  const rider=makeYouQi(); rider.position.set(11,0,-40); rider.rotation.y=0.5; g.add(rider);
  const road=new THREE.Mesh(new THREE.PlaneGeometry(6.5,52),
    new THREE.MeshPhongMaterial({color:0x1a2333,transparent:true,opacity:0.85,shininess:4}));
  road.rotation.x=-Math.PI/2; road.rotation.z=0.42;
  road.position.set(28,0.06,-70); g.add(road);
  const crowd=makeCrowd({n:3,rect:[26,-64,5.5,2.2],seed:16608,color:0x131a26,rimC:0x9fb2cc,
    rim:0.2,sMin:0.3,sMax:0.42,y:0.5});
  g.add(crowd.mesh);
  const mist2=makeMist({n:7,spread:[210,20,105],pos:[0,7,-52],scale:76,color:0x7e8ea8,op:0.085});
  g.add(mist2.g);
  const dust=makeGlow({n:40,box:[24,10,22],pos:[0,5,-20],color:0xa8bcd8,size:5,speed:0.05,rise:0.04,maxA:0.3});
  g.add(dust.points);
  /* 庭中一点冷光（银灯意，非金），把「深」的中景托出来 */
  const pl=new THREE.PointLight(0x8fa4c8,0.55,70); pl.position.set(0,7,-22); g.add(pl);
  const rk=makeForeground({kind:'坡石',n:3,r:3.8,w:22,d:8,color:0x04060a,seed:16609,rim:0.14});
  rk.g.position.set(13,-1.2,14); g.add(rk.g);
  const tree=makeForeground({kind:'树枝',n:2,w:16,d:5,color:0x04060a,seed:16610,sway:1.2,rim:0.18});
  tree.g.position.set(-16,-0.5,13); g.add(tree.g);
  addLights(g,{c:0x8fa4c8,i:0.5,p:[30,90,-30]},{c:0x1a2232,i:0.62});
  return {group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      st.t+=dt;
      ridge.update(t,0); mist2.update(t,k); smoke.update(t,k); dust.update(t);
      rk.update(t,k); tree.update(t,k);
      win.material.opacity=k*(0.24+0.06*Math.sin(t*0.66));
      pl.intensity=k*(0.55+0.05*Math.sin(t*0.8));
      const p=sstep(5,46,st.t);
      rider.position.set(11+18*p,0,-40-29*p);
      rider.scale.setScalar(1-0.30*p);
      w1.rotation.z=0.035*Math.sin(t*0.9);
      w2.rotation.z=-0.03*Math.sin(t*0.8+1.7);
    }};
}

/* 横雨着色器：雨丝斜掠（风大则斜），独享 uTime/uWind/uFade */
const RAIN_VERT=[
'attribute vec2 aOfs; attribute float aSeed;',
'uniform float uTime; uniform float uWind;',
'varying float vA;',
'void main(){',
'  vec3 p=position;',
'  float fall=mod(uTime*(30.0+aSeed*12.0)+aSeed*117.0,30.0);',
'  p.y-=fall; p.x+=fall*uWind;',
'  p.x=mod(p.x+44.0,88.0)-44.0;',
'  p+=vec3(aOfs.x*uWind,aOfs.y,0.0);',
'  vA=0.55+0.45*sin(aSeed*39.0);',
'  vec4 mv=modelViewMatrix*vec4(p,1.0);',
'  vA*=(1.0-smoothstep(30.0,55.0,-mv.z));',
'  gl_Position=projectionMatrix*mv;',
'}'].join('\\n');
const RAIN_FRAG=[
'uniform vec3 uColor; uniform float uFade; uniform float uA; varying float vA;',
'void main(){',
'  gl_FragColor=vec4(uColor,uFade*uA*vA);',
'}'].join('\\n');

/* 红瓣飞过秋千：点击后一群红瓣自花冠沿弧线掠过秋千架（uT0<0 时隐没） */
const PETAL_VERT=[
'attribute float aSeed; attribute float aSize;',
'uniform float uTime; uniform float uT0;',
'uniform vec3 uFrom; uniform vec3 uTo;',
'varying float vA;',
'void main(){',
'  float age=max(uTime-uT0,0.0);',
'  float d=0.55+0.75*aSeed;',
'  float pr=clamp(age/d,0.0,1.0);',
'  vec3 p=mix(uFrom,uTo,pr);',
'  p.y+=sin(pr*3.14159)*(2.6+3.0*aSeed);',
'  p.x+=sin(pr*9.0+aSeed*40.0)*0.9;',
'  p.z+=cos(pr*7.0+aSeed*23.0)*0.7;',
'  vA=smoothstep(0.0,0.06,pr)*smoothstep(1.0,0.75,pr)*step(0.0,uT0);',
'  vec4 mv=modelViewMatrix*vec4(p,1.0);',
'  gl_PointSize=aSize*(150.0/max(1.0,-mv.z));',
'  gl_Position=projectionMatrix*mv;',
'}'].join('\\n');
const PETAL_FRAG=[
'uniform vec3 uColor; uniform float uFade; varying float vA;',
'void main(){',
'  vec2 q=gl_PointCoord-vec2(0.5);',
'  float d=length(vec2(q.x*0.72,q.y));',
'  float a=smoothstep(0.5,0.12,d)*vA*uFade;',
'  if(a<0.004) discard;',
'  gl_FragColor=vec4(uColor,a);',
'}'].join('\\n');

function bWenHua(){ // 二（标志性瞬间·末境可点击）· 泪眼问花 —— 雨横风狂、门掩黄昏；点击：花枝乱颤+红瓣过秋千
  const g=new THREE.Group(), st={t:0}, ctl={t:0,clicked:false,trem:0};
  const grd=makeGround({r:110,c1:0x07090e,c2:0x0f141d});
  grd.mesh.position.y=-0.4; grd.mesh.position.z=-18; g.add(grd.mesh);
  const ridge=makeRange({r:260,h:14,layers:2,peaks:3,seed:16611,color:0x070a10,atmo:0x161c29,fogK:0.60,glowK:0.015,y:-10});
  ridge.g.position.set(0,0,-110); g.add(ridge.g);
  /* 横雨：雨丝斜掠（雨横风狂） */
  const NR=620, rp=new Float32Array(NR*2*3), ro=new Float32Array(NR*2*2), rs=new Float32Array(NR*2);
  for(let i=0;i<NR;i++){
    const x=(seedRnd(i+16612)())*88-44, y=2+seedRnd(i+26612)()*26,
          z=-34+seedRnd(i+36612)()*40, len=1.3+seedRnd(i+46612)()*0.8, sd=seedRnd(i+56612)();
    rp[i*6]=x;   rp[i*6+1]=y;   rp[i*6+2]=z;
    rp[i*6+3]=x; rp[i*6+4]=y;   rp[i*6+5]=z;
    ro[i*4]=0;        ro[i*4+1]=0;
    ro[i*4+2]=len*0.6; ro[i*4+3]=len;
    rs[i*2]=sd; rs[i*2+1]=sd;
  }
  const rainGeo=new THREE.BufferGeometry();
  rainGeo.setAttribute('position',new THREE.BufferAttribute(rp,3));
  rainGeo.setAttribute('aOfs',new THREE.BufferAttribute(ro,2));
  rainGeo.setAttribute('aSeed',new THREE.BufferAttribute(rs,1));
  const rainMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uWind:{value:0.6},uFade:{value:1},uA:{value:0.62},
      uColor:{value:C(0xa9bad2)}},
    vertexShader:RAIN_VERT,fragmentShader:RAIN_FRAG});
  const rain=new THREE.LineSegments(rainGeo,rainMat); rain.frustumCulled=false; rain.renderOrder=3;
  g.add(rain);
  /* 门掩黄昏：院门两扇徐徐合拢，门缝天光渐窄、渐沉 */
  const BD=new GeoBag(), c1=0x0c1017, c2=0x121826;
  [-2.5,2.5].forEach(function(dx){
    const post=new THREE.BoxGeometry(0.5,5.4,0.5); post.translate(dx,2.7,-11.5); BD.put(post,c1);
  });
  const lin=new THREE.BoxGeometry(5.9,0.6,0.7); lin.translate(0,5.6,-11.5); BD.put(lin,c2);
  const frame=new THREE.Group();
  frame.add(BD.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:9,
    specular:0x3a465c,emissive:0x05070c}),{c:0xa8b4c9,i:0.3,p:2.4})));
  g.add(frame);
  const doorGeoL=new THREE.BoxGeometry(2.15,4.8,0.16); doorGeoL.translate(1.075,0,0);
  const doorMatL=new THREE.MeshPhongMaterial({color:0x141b28,shininess:8,specular:0x2a3446,transparent:true,opacity:1});
  const doorL=new THREE.Mesh(doorGeoL,doorMatL); doorL.position.set(-2.25,2.6,-11.5); g.add(doorL);
  const doorGeoR=new THREE.BoxGeometry(2.15,4.8,0.16); doorGeoR.translate(-1.075,0,0);
  const doorMatR=new THREE.MeshPhongMaterial({color:0x141b28,shininess:8,specular:0x2a3446,transparent:true,opacity:1});
  const doorR=new THREE.Mesh(doorGeoR,doorMatR); doorR.position.set(2.25,2.6,-11.5); g.add(doorR);
  const shaft=new THREE.Mesh(new THREE.PlaneGeometry(4.3,4.8),
    new THREE.MeshBasicMaterial({color:0x93a6c0,transparent:true,opacity:0.16,depthWrite:false,
      blending:THREE.AdditiveBlending}));
  shaft.position.set(0,2.6,-11.4); shaft.renderOrder=2; g.add(shaft);
  const pool=new THREE.Mesh(new THREE.CircleGeometry(2.2,18),
    new THREE.MeshBasicMaterial({color:0x93a2ba,transparent:true,opacity:0.16,depthWrite:false,
      blending:THREE.AdditiveBlending}));
  pool.rotation.x=-Math.PI/2; pool.position.set(0,0.35,-9.6); pool.renderOrder=2; g.add(pool);
  /* 泪眼问花：人影立花前，抬手问花 */
  const figure=makeFigure({pose:'指月',robe:0x1f2a3e,belt:0x516282,skin:0xcbb9a2,collar:0xb6c4d8,
    hat:'发髻',rimC:0xa8b4c9,rim:0.55,noProp:true,scale:1.5});
  figure.position.set(-6.2,0,-13.5); figure.rotation.y=-0.5; g.add(figure);
  const tears=makeGlow({n:10,box:[0.8,0.7,0.7],pos:[-5.7,4.2,-13.2],color:0xd6e2f4,size:2.0,
    speed:0.03,rise:-0.05,maxA:0.3});
  g.add(tears.points);
  /* 花树：曲干横枝 + 满冠乱红（全页唯一暖彩） */
  const tree=new THREE.Group();
  const BT=new GeoBag(), R=seedRnd(16613);
  const cB=0x0b0e14;
  const tr0=new THREE.CylinderGeometry(0.14,0.34,3.0,6); tr0.rotateZ(0.10);
  tr0.translate(-0.15,1.5,0); BT.put(tr0,cB);
  const tr1=new THREE.CylinderGeometry(0.09,0.15,2.6,5); tr1.rotateZ(-0.30);
  tr1.translate(0.55,4.0,0); BT.put(tr1,cB);
  const tips=[];
  for(let i=0;i<6;i++){
    const a=R()*Math.PI*2, el=0.35+R()*0.5, len=2.0+R()*1.6;
    const bx=Math.cos(a)*len*Math.cos(el), by=4.6+Math.sin(el)*len*0.8, bz=Math.sin(a)*len*0.6;
    const br=new THREE.CylinderGeometry(0.03,0.07,len,4);
    br.rotateZ(Math.atan2(-bx,by)); br.rotateY(Math.atan2(bz,bx));
    br.translate(bx*0.5,4.4+(by-4.4)*0.5,bz*0.5); BT.put(br,cB);
    tips.push([bx,by,bz]);
  }
  const REDS=[0x8f4340,0xa8544c,0xbb6b5c,0x6e3532,0xa8544c];
  tips.forEach(function(tp){
    for(let k2=0;k2<6;k2++){
      const bl=new THREE.IcosahedronGeometry(0.22+R()*0.24,0);
      bl.translate(tp[0]+(R()-0.5)*1.5,tp[1]+(R()-0.5)*1.1,tp[2]+(R()-0.5)*1.2);
      BT.put(bl,REDS[Math.floor(R()*REDS.length)]);
    }
  });
  tree.add(BT.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x33262a,emissive:0x0a0507}),{c:0xc9a2a0,i:0.22,p:2.2})));
  tree.position.set(-11,0,-20); g.add(tree);
  const pile=new THREE.Mesh(new THREE.CircleGeometry(2.2,16),
    new THREE.MeshPhongMaterial({color:0x3f2422,transparent:true,opacity:0.55,shininess:3}));
  pile.rotation.x=-Math.PI/2; pile.position.set(-10.4,0.12,-18.8); g.add(pile);
  /* 乱红（常落）：非叠加红瓣辞枝，细而克制、贴地飘坠 */
  const petals=makeGlow({n:50,box:[24,8,14],pos:[-4,4.5,-19],color:0xa8544c,size:1.6,
    speed:0.10,rise:-0.55,add:false,maxA:0.28});
  g.add(petals.points);
  /* 红瓣飞过秋千：点击触发的一阵急瓣 */
  const pfGeo=new THREE.BufferGeometry();
  const pfn=70, pfP=new Float32Array(pfn*3), pfS=new Float32Array(pfn), pfZ=new Float32Array(pfn);
  for(let i=0;i<pfn;i++){
    pfP[i*3]=-11+(R()-0.5)*1.6; pfP[i*3+1]=6.5+(R()-0.5)*1.8; pfP[i*3+2]=-20+(R()-0.5)*1.6;
    pfS[i]=R(); pfZ[i]=2.6+R()*2.2;
  }
  pfGeo.setAttribute('position',new THREE.BufferAttribute(pfP,3));
  pfGeo.setAttribute('aSeed',new THREE.BufferAttribute(pfS,1));
  pfGeo.setAttribute('aSize',new THREE.BufferAttribute(pfZ,1));
  const pfMat=new THREE.ShaderMaterial({transparent:true,depthWrite:false,
    uniforms:{uTime:{value:0},uT0:{value:-999},uFade:{value:1},
      uFrom:{value:new THREE.Vector3(-11,6.5,-20)},uTo:{value:new THREE.Vector3(16,2.0,-19.5)},
      uColor:{value:C(0xc4685f)}},
    vertexShader:PETAL_VERT,fragmentShader:PETAL_FRAG});
  const fly=new THREE.Points(pfGeo,pfMat); fly.frustumCulled=false; fly.renderOrder=4;
  g.add(fly);
  /* 秋千：双柱斜撑 + 横梁 + 双绳 + 踏板（画面右翼，红瓣掠过的去处） */
  const BS=new GeoBag(), cW=0x1c2432, cRope=0x46536b;
  [[-1.8,0],[1.8,0]].forEach(function(px){
    [-1.0,1.0].forEach(function(dz){
      const leg=new THREE.CylinderGeometry(0.12,0.17,7.0,5);
      leg.rotateX(dz>0?-0.26:0.26);
      leg.translate(px[0],3.4,-20+dz); BS.put(leg,cW);
    });
  });
  const beam=new THREE.CylinderGeometry(0.15,0.15,4.8,6); beam.rotateZ(Math.PI/2);
  beam.translate(0,6.4,-20); BS.put(beam,cW);
  [-0.55,0.55].forEach(function(rx){
    const rope=new THREE.CylinderGeometry(0.035,0.035,4.7,4);
    rope.translate(rx,4.05,-20); BS.put(rope,cRope);
  });
  const seat=new THREE.BoxGeometry(2.1,0.14,0.55); seat.translate(0,1.7,-20); BS.put(seat,cW);
  const swing=new THREE.Group();
  swing.add(BS.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:8,
    specular:0x2a3446,emissive:0x04060a}),{c:0xa8b4c9,i:0.3,p:2.4})));
  swing.position.set(8.5,0,0);
  g.add(swing);
  /* 风尘 + 低雾（湿意靠雨丝与雾气，不做反光水板） */
  const wind=makeFlow({n:150,box:[120,16,55],pos:[0,8,-25],color:0x8fa0b8,size:20,speed:7.5,maxA:0.16});
  g.add(wind.points);
  const mist=makeMist({n:9,spread:[240,30,110],pos:[0,7,-58],scale:74,color:0x74839c,op:0.06});
  g.add(mist.g);
  const reeds=makeForeground({kind:'树枝',n:2,w:15,d:5,color:0x04060a,seed:16614,sway:2.2,rim:0.16});
  reeds.g.position.set(14,-0.5,11); g.add(reeds.g);
  const rk=makeForeground({kind:'坡石',n:3,r:3.6,w:20,d:7,color:0x04060a,seed:16615,rim:0.14});
  rk.g.position.set(-14,-1.2,9.5); g.add(rk.g);
  const dirL=new THREE.DirectionalLight(0x8296b4,0.42); dirL.position.set(-25,60,-10); g.add(dirL);
  g.add(new THREE.AmbientLight(0x161d2b,0.66));
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      st.t+=dt; ctl.t+=dt;
      ctl.trem=Math.max(0,ctl.trem-dt*0.55);
      const e=sstep(2,16,Math.min(st.t,16));
      ridge.update(t,0); wind.update(t);
      petals.update(t); pfMat.uniforms.uTime.value=t; tears.update(t);
      mist.update(t,k); reeds.update(t,k); rk.update(t,k);
      const ang=1.05-0.99*e;
      doorL.rotation.y=ang; doorR.rotation.y=-ang;
      shaft.material.opacity=k*(0.26*(1-e)+0.02);
      pool.material.opacity=k*(0.16*(1-e)+0.02);
      dirL.intensity=k*(0.42*(1-0.38*e));
      tree.rotation.z=0.025*Math.sin(t*0.8)+ctl.trem*0.055*Math.sin(t*22.0);
      tree.rotation.x=ctl.trem*0.03*Math.sin(t*17.3+1.0);
    },click(){
      if(ctl.t<1.2)return;
      if(!ctl.clicked){
        ctl.clicked=true; api.clicked=true; ctl.trem=1;
        pfMat.uniforms.uT0.value=st.t;
        pluck(2,0.05,0.12); pluck(4,0.5,0.10); pluck(7,1.05,0.09);
        const fl=$('#flash'); fl.textContent='乱红飞过秋千'; fl.classList.remove('go');
        void fl.offsetWidth; fl.classList.add('go');
      }
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0x090d15),hor:C(0x161e2c),bot:C(0x0a0d13),fog:C(0x101724),fd:0.0056,star:0.45,
  moon:new THREE.Vector3(34,112,-185),ms:1.9,mph:0,mhaze:0.05,dirC:C(0x8fa4c8),dirI:0.5,
  dirP:new THREE.Vector3(30,90,-30),ambC:C(0x1a2232),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,60],t:[0,9.5,55],lf:[0,13,-40],lt:[0,13.5,-44]},
  sky:()=>SK({top:C(0x080b12),hor:C(0x121a28),bot:C(0x090c11),fog:C(0x0e141f),fd:0.0048,star:0.40,
    ms:1.5,moon:new THREE.Vector3(24,98,-175),
    dirC:C(0x8fa4c8),dirI:0.40,ambC:C(0x182031),ambI:0.60}) },
{ name:'庭院深深',dwell:18,river:0.02,build:bTingYuan,
  cam:{f:[0,6.2,22],t:[0.6,5.8,18.5],lf:[0,5.5,-32],lt:[-0.5,5,-34]},
  sky:()=>SK({top:C(0x090d15),hor:C(0x161e2c),bot:C(0x0a0d13),fog:C(0x101724),fd:0.0056,star:0.45,
    ms:1.6,mph:0,mhaze:0.05,moon:new THREE.Vector3(-55,110,-200),
    dirC:C(0x8fa4c8),dirI:0.62,dirP:new THREE.Vector3(20,60,-10),ambC:C(0x1a2232),ambI:0.66}) },
{ name:'泪眼问花',dwell:20,river:0.02,build:bWenHua,
  cam:{f:[0,6,16],t:[-1.5,5.4,13],lf:[-1,4.5,-19],lt:[-2,4,-20]},
  sky:()=>SK({top:C(0x080a10),hor:C(0x10141d),bot:C(0x090b10),fog:C(0x0e131d),fd:0.0066,star:0.22,
    ms:0.55,mph:0.1,mhaze:0.06,moon:new THREE.Vector3(-40,80,-160),
    dirC:C(0x8296b4),dirI:0.42,ambC:C(0x161d2b),ambI:0.66}) },
];
"""
