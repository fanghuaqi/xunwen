# -*- coding: utf-8 -*-
"""busuanzi-huangzhou.py —— 《卜算子·黄州定慧院寓居作》（宋·苏轼，no.178，宣纸留白）生成配置
两境（N=queue stages 数）：疏桐缺月（缺月挂疏桐·漏断人初静·幽人独往来·缥缈孤鸿影——孤鸿掠影为词眼标志性瞬间）、
寒枝沙洲（惊起回头·有恨无人省·拣尽寒枝不肯栖·寂寞沙洲冷——末境点击「鸿影掠枝不肯落+沙洲寒月」）。
宣纸留白：浅纸底、笔墨极简——疏桐浓墨剪影、缺月一弯浅墨、孤鸿一点浓墨，全页大量空白。"""

META = dict(
    N=2, slug='busuanzi-huangzhou', title='卜算子·黄州定慧院寓居作', dyn='宋 · 苏轼', brand_author='苏 轼',
    gold_rgb='62,74,68',
    residual=('将进酒', '万古愁', '太白', '李白'),
    root=""":root{
  --gold:#3e4a44; --ink:#23272e; --dim:#6e695a; --paper:rgba(255,252,240,.72);
  --line:rgba(62,74,68,.26);
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
        # 长调题名（12 字）竖排封面：缩字号、收字距，保证一屏立得住
        ('font-size:clamp(64px,11vh,120px);letter-spacing:.28em',
         'font-size:clamp(40px,5.6vh,66px);letter-spacing:.14em', 1),
        ('#titleCol h1{font-size:64px}', '#titleCol h1{font-size:40px}', 1),
        # 浅色赛道：暗底投影改纸面提边（art-direction 浅色必改清单）
        ('0 2px 6px rgba(0,0,0,.7)', '0 1px 0 rgba(255,255,255,.45)', 1),
        ('text-shadow:0 0 14px rgba(0,0,0,.8)', 'text-shadow:0 1px 0 rgba(255,255,255,.45)', 1),
        ('0 4px 20px rgba(0,0,0,.8)', '0 1px 0 rgba(255,255,255,.45)', 1),
    ],
    tip='轻点画面 / 按空格 —— 看孤鸿掠枝，不肯栖落',
    hint='← → 键或空格逐境游览 · 末境可点击画面，看孤鸿掠枝、沙洲寒月',
    cover_read='卜算子·黄州定慧院寓居作。宋，苏轼。缺月挂疏桐，漏断人初静。谁见幽人独往来，缥缈孤鸿影。',
    cover_p1='两重意境，随词句次第展开：缺月挂在疏桐之上的深夜庭院；幽人独往来的缥缈鸿影；惊起回头却无人省的幽恨；拣尽寒枝不肯栖的孤高身影；末了寂寞沙洲上一片清冷的寒月。',
    cover_p2='边读词，边走进东坡黄州的那纸清寒——人是孤鸿，鸿亦如人；万语千言，只作一弯浅墨缺月、一点浓墨鸿影。',
    end_h2='鸿去 · 洲冷', cn_word='两',
    words_js="['再游一次，鸿影缥缈','初识东坡，尚需共读','渐入佳境，再诵几遍','词境渐深，幽恨初省','已解孤鸿不栖之意','孤高自许，沙洲自冷']",
    sky_atmo='0xd8d2c0',
)

POEM_JS = """const POEM = [
{ name:'疏桐缺月', jing:'缺月挂疏桐 —— 漏断人初静，谁见幽人独往来，缥缈孤鸿影。（桐 · 月 · 鸿）',
  segs:[
   {c:'缺月挂疏桐，', p:py('quē yuè guà shū tóng')},
   {c:'漏断人初静。', p:py('lòu duàn rén chū jìng')},
   {c:'谁见幽人独往来，', p:py('shuí jiàn yōu rén dú wǎng lái')},
   {c:'缥缈孤鸿影。', p:py('piāo miǎo gū hóng yǐng')}],
  read:'缺月挂疏桐，漏断人初静。谁见幽人独往来，缥缈孤鸿影。',
  yisi:'弯弯的缺月，挂在疏落的梧桐枝上；漏壶水滴已断，夜深人声初静。谁能看见幽居之人独自来去徘徊？只有那缥缈孤单的一点鸿影。——缺月、疏桐、断漏，布出一夜清寂；孤鸿掠影而过，人与鸿自此互为镜像：人如鸿，鸿亦如人。',
  zhu:[['疏桐','叶落枝稀的梧桐。梧桐是秋夜清寂之树，叶脱之后愈见孤高，为全词定下清冷底色'],['漏断','漏壶的水滴声断了，指夜已极深。漏：古人滴水计时的漏壶；「漏断人初静」即夜静更深'],['幽人','幽居之人，作者自指。乌台诗案后，苏轼以罪臣之身贬黄州，寓居定慧院，深宵不寐'],['缥缈','隐隐约约、若有若无。缥缈孤鸿影：孤鸿掠空的淡影——是全词词眼，人鸿互喻自此而起']] },
{ name:'寒枝沙洲', jing:'惊起却回头 —— 有恨无人省，拣尽寒枝不肯栖，寂寞沙洲冷。（鸿 · 枝 · 洲）',
  segs:[
   {c:'惊起却回头，', p:py('jīng qǐ què huí tóu')},
   {c:'有恨无人省。', p:py('yǒu hèn wú rén xǐng')},
   {c:'拣尽寒枝不肯栖，', p:py('jiǎn jìn hán zhī bù kěn qī')},
   {c:'寂寞沙洲冷。', p:py('jì mò shā zhōu lěng')}],
  read:'惊起却回头，有恨无人省。拣尽寒枝不肯栖，寂寞沙洲冷。',
  yisi:'孤鸿蓦然惊起，却又回头张望——满怀幽恨，无人能够理会。寒林的枝枝杈杈，它拣了又拣，竟无一枝肯于栖落，宁可归宿到那片寂寞清冷的沙洲。——不肯栖，是不肯将就：孤鸿的孤高，正是词人自守的写照；沙洲虽冷，冷得干净。',
  zhu:[['省','知晓、体察，读 xǐng。「有恨无人省」——心中有恨，却无人理会、无人懂得'],['拣尽寒枝','把寒林枝条拣选了一遍。拣：挑选——枝非不多，无一可栖，暗写不肯苟且俯就'],['栖','栖落、停宿，读 qī。「不肯栖」三字最重：宁受寂寞，不凑热闹，是全词的骨'],['沙洲','水中沙渚。元丰三年（1080）苏轼贬黄州，寓居定慧院，此词以孤鸿自况，黄庭坚叹为「语意高妙」']] }];
const CN = ['壹','贰'];
"""

QUIZ_JS = """const QUIZ = [
 {q:'「缺月挂疏桐」的下一句是？', o:['漏断人初静','谁见幽人独往来','缥缈孤鸿影'], a:0},
 {q:'「惊起却回头」的下一句是？', o:['有恨无人省','拣尽寒枝不肯栖','寂寞沙洲冷'], a:0},
 {q:'「漏断人初静」的「漏断」与「有恨无人省」的「省」，理解正确的是？', o:['漏断：屋漏雨断；省 shěng，节省','漏断：漏壶水断、夜深人静；省 xǐng，知晓、体察','漏断：漏刻刚上、入夜时分；省 xǐng，反省自律'], a:1},
 {q:'这首词作于苏轼人生的哪一阶段？', o:['「乌台诗案」险遭不测后，贬居黄州、寓居定慧院的时期','汴京名动天下、与友人诗酒相得的青年得意时期','复任翰林学士、位望清贵的元祐时期'], a:0},
 {q:'「拣尽寒枝不肯栖，寂寞沙洲冷」的孤鸿，寄托了词人怎样的心怀？', o:['渴望攀上高枝、重获起用的期待','孤高自许、不肯附势趋俗——宁可寂寞也不将就','对漂泊无依、无处安身的单纯哀叹'], a:1},
];
"""

SCENES_JS = """/* ================= 卜算子·黄州定慧院寓居作 · 两境场景（宣纸留白：疏桐缺月、寒枝沙洲） =================
   浅纸为天、浓墨作画，大量留白：疏桐浓墨剪影、缺月一弯浅墨、孤鸿一点浓墨。
   境一标志性瞬间：孤鸿掠影缓缓渡过桐梢与缺月之间；末境点击：鸿影掠枝不肯落，趋向沙洲寒月。 */

/* 疏桐 makeWutong(o) —— 梧桐剪影：干直多节、枝横斜上扬、叶大而疏（合批 1 mesh）
   leafN:0 → 临水寒枝（拣尽寒枝不肯栖的枯枝） */
function makeWutong(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2701:o.seed);
  const h=o.h===undefined?7.0:o.h;
  const ink=o.ink===undefined?0x2c2f33:o.ink;
  const leafN=o.leafN===undefined?9:o.leafN;
  const B=new GeoBag(), tips=[];
  const trunk=new THREE.CylinderGeometry(0.085,0.21,h*0.60,8);
  trunk.translate(0,h*0.30,0); trunk.rotateZ((R()-0.5)*0.10);
  B.put(trunk,ink);
  const up=new THREE.CylinderGeometry(0.05,0.095,h*0.36,7);
  up.translate(0,h*0.60+h*0.18,0); up.rotateZ((R()-0.5)*0.16);
  B.put(up,ink);
  const branch=function(tilt,rotY,len,r0,y0){
    const br=new THREE.CylinderGeometry(r0*0.42,r0,len,5);
    br.translate(0,len*0.5,0); br.rotateZ(tilt); br.rotateY(rotY);
    br.translate(0,y0,0);
    B.put(br,ink);
    tips.push([Math.sin(tilt)*Math.cos(rotY)*len,y0+Math.cos(tilt)*len,-Math.sin(tilt)*Math.sin(rotY)*len]);
  };
  const nb=o.nb===undefined?6:o.nb;
  for(let i=0;i<nb;i++){
    const y0=h*(0.42+0.40*R()), len=(1.5+R()*2.1)*(h/7), tilt=0.72+R()*0.60, a=R()*6.283;
    branch(tilt,a,len,0.055,y0);
    if(R()<0.75)branch(tilt+0.22+R()*0.30,a+0.8+R()*0.9,len*0.60,0.030,y0+len*0.55);
  }
  /* 疏叶：叶大而稀，老绿近墨（accent 一族，不作浓彩） */
  const leafC=[0x39423c,0x3e4a44,0x333b36];
  for(let i=0;i<leafN;i++){
    const t=tips[Math.floor(R()*tips.length)];
    const lf=new THREE.SphereGeometry(0.30+R()*0.20,6,5);
    lf.scale(1.35,0.28,1.05); lf.rotateY(R()*6.283); lf.rotateZ((R()-0.5)*0.5);
    lf.translate(t[0]+(R()-0.5)*0.36,t[1]+(R()-0.5)*0.26,t[2]+(R()-0.5)*0.36);
    B.put(lf,leafC[Math.floor(R()*leafC.length)]);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x35322c,emissive:0x0b0c0c}),{c:0xf0ead8,i:0.14,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}

/* 孤鸿 makeHong(o) —— 缥缈孤鸿影：浓墨一点（身首尾合批 1 mesh + 双翼各 1，绕核心缓飞） */
function makeHong(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2702:o.seed);
  const ink=0x23262b;
  const B=new GeoBag();
  const body=new THREE.SphereGeometry(0.15,9,7);
  body.scale(2.2,0.88,1.0); body.rotateZ(-0.10);
  B.put(body,ink);
  const neck=new THREE.CylinderGeometry(0.045,0.085,0.34,6);
  neck.rotateZ(1.18); neck.translate(0.36,0.09,0); B.put(neck,ink);
  const head=new THREE.SphereGeometry(0.078,8,6); head.translate(0.50,0.19,0); B.put(head,ink);
  const bill=new THREE.ConeGeometry(0.026,0.15,5); bill.rotateZ(-1.35); bill.translate(0.62,0.21,0); B.put(bill,ink);
  const tail=new THREE.ConeGeometry(0.10,0.46,5); tail.rotateZ(2.95); tail.translate(-0.40,0.03,0); B.put(tail,ink);
  const g=new THREE.Group();
  g.add(B.mesh(new THREE.MeshPhongMaterial({color:ink,shininess:5,specular:0x2a2d33,emissive:0x08090c})));
  const wing=new THREE.BoxGeometry(0.36,0.032,1.00);
  wing.translate(0,0,0.52);
  const wm=new THREE.MeshPhongMaterial({color:ink,shininess:5,specular:0x2a2d33,emissive:0x08090c,
    side:THREE.DoubleSide});
  const wr=new THREE.Mesh(wing,wm);
  const wl=new THREE.Mesh(wing,wm); wl.scale.z=-1;
  g.add(wr); g.add(wl);
  const cx=o.cx===undefined?0:o.cx, cy=o.cy===undefined?10.5:o.cy, cz=o.cz===undefined?-16:o.cz;
  const rx=o.rx===undefined?8.5:o.rx, rz=o.rz===undefined?3.6:o.rz, w=o.w===undefined?0.13:o.w;
  const ph=R()*6.283;
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  g.update=function(t){
    const a=t*w+ph;
    const x=cx+Math.sin(a)*rx, z=cz+Math.cos(a)*rz, y=cy+Math.sin(a*2.3)*0.9;
    const dx=Math.cos(a)*rx, dz=-Math.sin(a)*rz;
    g.position.set(x,y,z);
    g.rotation.set(0.10*Math.sin(a*2.3+1.2),Math.atan2(-dz,dx),0.26*Math.sin(a));
    const flap=0.42*Math.sin(t*2.7)+0.08*Math.sin(t*7.3);
    wr.rotation.x=-flap; wl.rotation.x=flap;
  };
  return {g:g,update:g.update};
}

/* 沙洲 makeShazhou(o) —— 水中沙渚：沙脊起伏 + 墨石压角（合批 1 mesh） */
function makeShazhou(o){
  o=o||{};
  const R=seedRnd(o.seed===undefined?2703:o.seed);
  const B=new GeoBag(), n=o.n===undefined?5:o.n;
  for(let i=0;i<n;i++){
    const rr=(o.r===undefined?1.7:o.r)*(0.55+0.85*R());
    const m=new THREE.SphereGeometry(rr,9,7);
    m.scale(1.55,0.34,1.0);
    m.translate((R()-0.5)*(o.w===undefined?3.6:o.w),rr*0.16,(R()-0.5)*(o.d===undefined?2.6:o.d));
    B.put(m,i%3===2?0x655f52:(i%2?0x7a7466:0x6e685a));
  }
  const nr=o.rocks===undefined?3:o.rocks;
  for(let i=0;i<nr;i++){
    const rr=0.24+R()*0.34;
    const rg=rockGeo(rr,1,R);
    rg.translate((R()-0.5)*(o.w===undefined?3.6:o.w)*1.1,rr*0.42,(R()-0.5)*(o.d===undefined?2.6:o.d)*1.1);
    B.put(rg,i%2?0x2c2f33:0x23262b);
  }
  const g=new THREE.Group();
  g.add(B.mesh(rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true,shininess:6,
    specular:0x35322c,emissive:0x0d0c08}),{c:0xf0ead8,i:0.12,p:2.2})));
  g.scale.setScalar(o.scale===undefined?1:o.scale);
  return g;
}
/* 点击位移关键帧 [k,dx,dy,dz]：俯身掠枝 → 贴枝不肯落 → 趋向寒月（首尾皆 0，与绕飞无缝衔接） */
const SWK=[[0,0,0,0],[0.20,-4.6,-5.0,1.2],[0.42,-3.2,-6.0,-2.2],[0.60,0.6,-5.2,-1.4],
  [0.80,1.0,2.4,0.6],[1,0,0,0]];
function swoopOff(k){
  for(let i=1;i<SWK.length;i++){
    if(k<=SWK[i][0]){
      const a=SWK[i-1],b=SWK[i],t=(k-a[0])/(b[0]-a[0]),s=t*t*(3-2*t);
      return [a[1]+(b[1]-a[1])*s,a[2]+(b[2]-a[2])*s,a[3]+(b[3]-a[3])*s];
    }
  }
  return [0,0,0];
}

function bCover(){ // 卷首 · 宣纸清夜，缺月疏桐藏一点鸿影
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d3,c2:0xdcd4bd,y:-1.5}); g.add(grd.mesh);
  const ridge=makeRange({r:280,h:58,layers:3,peaks:5,seed:2730,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.035,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-92); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:180,h:26,layers:2,peaks:4,seed:2731,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.025,glow:0xf4eeda,y:-6,order:-5});
  ridge2.g.position.set(8,0,-44); ridge2.g.rotation.y=Math.PI*1.04; g.add(ridge2.g);
  const tree=makeWutong({seed:2732,h:6.2,leafN:7});
  tree.position.set(-9,-1.1,-30); g.add(tree);
  const hong=makeHong({seed:2733,cx:-2,cy:13,cz:-46,rx:12,rz:4,w:0.09,scale:0.8}); g.add(hong.g);
  const mist=makeMist({n:8,spread:[270,26,150],pos:[0,8,-66],scale:82,color:0xe6dfcc,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:40,box:[220,30,120],pos:[0,10,-42],color:0xb8bcc2,size:4,speed:0.04,
    rise:0.05,add:false,maxA:0.20});
  g.add(motes.points);
  const reeds=makeForeground({kind:'芦苇',w:26,n:14,d:5,color:0x2c2f33,seed:2734,sway:0.9,tip:0x4a4f56});
  reeds.g.position.set(14,-1.8,42); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[40,110,30]},{c:0xd8d2c0,i:0.6});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t);
    hong.update(t); reeds.update(t,k);
  }};
}

function bShutong(){ // 一 · 疏桐缺月 —— 缺月挂疏桐，缥缈孤鸿影（标志性瞬间：孤鸿掠影渡桐月之间）
  const g=new THREE.Group();
  const grd=makeGround({r:260,c1:0xe9e3d3,c2:0xdcd4bd,y:-1.5}); g.add(grd.mesh);
  /* 背景：两叠淡墨远山（愈远愈淡） */
  const ridge=makeRange({r:280,h:66,layers:3,peaks:5,seed:2740,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.58,glowK:0.04,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:180,h:30,layers:2,peaks:4,seed:2741,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.025,glow:0xf4eeda,y:-5,order:-5});
  ridge2.g.position.set(-12,0,-36); ridge2.g.rotation.y=Math.PI*1.05; g.add(ridge2.g);
  /* 中景：疏桐一株，缺月悬于桐梢上方（月为天穹常驻，随 sky 落位） */
  const tree=makeWutong({seed:2742,h:8.2,leafN:9,nb:7});
  tree.position.set(6.5,-1.2,-11); tree.rotation.y=-0.4; g.add(tree);
  /* 漏断人初静：庭石浅浅一笔 */
  const rk=makeForeground({kind:'坡石',n:3,r:2.4,w:16,d:6,color:0x23262b,seed:2743,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(-17,-1.8,12); g.add(rk.g);
  /* 幽人独立（衣取 accent 墨青——人如鸿，鸿如人） */
  const figure=makeFigure({pose:'独立',robe:0x3e4a44,belt:0x2c2f33,skin:0xcbb9a2,collar:0xe8e2d0,
    hat:'发髻',rimC:0xe8e2d0,rim:0.30,noProp:true,scale:1.25});
  figure.position.set(-4.6,-1.5,-8.5); figure.rotation.y=0.55; g.add(figure);
  /* 缥缈孤鸿影：一点浓墨绕庭缓飞 */
  const hong=makeHong({seed:2744,cx:-0.5,cy:10.5,cz:-15,rx:8.6,rz:3.8,w:0.125}); g.add(hong.g);
  const mist=makeMist({n:7,spread:[240,22,130],pos:[0,7,-60],scale:78,color:0xe6dfcc,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:42,box:[90,13,52],pos:[0,6,-20],color:0xb8bcc2,size:4,speed:0.05,
    rise:0.07,add:false,maxA:0.20});
  g.add(motes.points);
  /* 前景：枯苇框住画缘（避开幽人，收在右侧） */
  const reeds=makeForeground({kind:'芦苇',w:22,n:10,d:5,color:0x2c2f33,seed:2745,sway:0.8,tip:0x4a4f56});
  reeds.g.position.set(13,-1.6,17); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[-40,110,30]},{c:0xd8d2c0,i:0.62});
  return {group:g,update(t,dt){ const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
    ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t);
    hong.update(t); rk.update(t,k); reeds.update(t,k); figure.update(t,k);
  }};
}

function bShazhou(){ // 二（末境·可点击）· 寒枝沙洲 —— 惊起回头、拣尽寒枝；点击：鸿影掠枝不肯落，趋向沙洲寒月
  const g=new THREE.Group();
  const ctl={t:0,last:-9,clicked:false,swoop:0,sw:0};
  /* 寂寞沙洲：寒江一水，沙渚居中 */
  const water=makeWater({size:640,seg:88,amp:0.26,freq:0.09,speed:0.42,flow:[0.10,0.16],spec:0.6,
    deep:0x8a9094,shallow:0xb8bcb4,skyc:0xd6d2c0,moonDir:[-0.35,1,0.2]});
  g.add(water.mesh);
  const ridge=makeRange({r:280,h:60,layers:3,peaks:5,seed:2750,color:0x2c2f33,atmo:0xd8d2c0,
    fogK:0.60,glowK:0.035,glow:0xf4eeda,y:-8});
  ridge.g.position.set(0,0,-95); ridge.g.rotation.y=Math.PI; g.add(ridge.g);
  const ridge2=makeRange({r:180,h:26,layers:2,peaks:4,seed:2751,color:0x23262b,atmo:0xd8d2c0,
    fogK:0.68,glowK:0.02,glow:0xf4eeda,y:-5,order:-5});
  ridge2.g.position.set(10,0,-38); ridge2.g.rotation.y=Math.PI*1.03; g.add(ridge2.g);
  /* 沙洲：沙脊 + 墨石 */
  const islet=makeShazhou({seed:2752,r:1.9,n:5,w:4.2,d:2.8,rocks:4});
  islet.position.set(0.5,-0.25,-9.5); islet.scale.setScalar(1.15); g.add(islet);
  /* 寒枝：临水枯桐（无叶）——鸿所不肯栖者 */
  const zhi=makeWutong({seed:2753,h:6.4,leafN:0,nb:7,ink:0x23262b});
  zhi.position.set(-6.2,-0.7,-13); zhi.rotation.y=0.5; g.add(zhi);
  /* 幽人独立洲上（衣取 accent 墨青） */
  const figure=makeFigure({pose:'独立',robe:0x3e4a44,belt:0x2c2f33,skin:0xcbb9a2,collar:0xe8e2d0,
    hat:'发髻',rimC:0xe8e2d0,rim:0.30,noProp:true,scale:1.2});
  figure.position.set(2.3,-0.55,-8.0); figure.rotation.y=-0.55; g.add(figure);
  /* 孤鸿低回（惊起回头之态，绕枝洲缓飞） */
  const hong=makeHong({seed:2754,cx:0,cy:7.2,cz:-11,rx:6.4,rz:3.2,w:0.14}); g.add(hong.g);
  /* 沙洲寒月：天穹缺月方向的一晕冷光（点击趋月时增亮；初始即最大值，逐帧只在其下浮动） */
  const haloMax=0.26;
  const halo=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex(),color:0xb4b8ba,
    transparent:true,opacity:haloMax,depthWrite:false}));
  halo.scale.set(30,30,1); halo.position.set(-30,30,-72); halo.renderOrder=2;
  g.add(halo);
  const mist=makeMist({n:7,spread:[240,20,130],pos:[0,6,-58],scale:76,color:0xe6dfcc,op:0.10});
  g.add(mist.g);
  const motes=makeGlow({n:38,box:[80,11,46],pos:[0,5,-18],color:0xb8bcc2,size:4,speed:0.045,
    rise:0.06,add:false,maxA:0.18});
  g.add(motes.points);
  /* 前景：坡石 + 枯苇框住画缘 */
  const rk=makeForeground({kind:'坡石',n:3,r:3.0,w:18,d:6,color:0x23262b,seed:2755,rim:0.12,rimC:0xf0ead8});
  rk.g.position.set(-15,-1.6,13); g.add(rk.g);
  const reeds=makeForeground({kind:'芦苇',w:22,n:11,d:5,color:0x2c2f33,seed:2756,sway:0.8,tip:0x4a4f56});
  reeds.g.position.set(13,-1.5,16); g.add(reeds.g);
  addLights(g,{c:0xd9d4c4,i:0.5,p:[-30,100,-30]},{c:0xd8d2c0,i:0.62});
  const api={group:g,update(t,dt){
      const k=g.userData.fadeK===undefined?1:g.userData.fadeK;
      ctl.t+=dt;
      if(ctl.swoop>0){
        ctl.sw=Math.min(1,ctl.sw+dt/7.5);
        if(ctl.sw>=1)ctl.swoop=0;
      }
      hong.update(t);
      if(ctl.sw>0&&ctl.sw<1){
        const off=swoopOff(ctl.sw);
        hong.g.position.x+=off[0]; hong.g.position.y+=off[1]; hong.g.position.z+=off[2];
        hong.g.rotation.z+=0.20*Math.sin(ctl.sw*9.4);
      }
      water.update(t); ridge.update(t,0); ridge2.update(t,0); mist.update(t,k); motes.update(t);
      rk.update(t,k); reeds.update(t,k); figure.update(t,k);
      const boost=ctl.sw>0?0.14*ctl.sw*(0.6+0.4*Math.sin(t*2.2)):0;
      halo.material.opacity=k*haloMax*(0.70+0.12*Math.sin(t*0.6)+boost);
    },click(){
      if(ctl.t<1.2||ctl.t-ctl.last<1.2)return;
      ctl.last=ctl.t;
      if(!ctl.clicked){ ctl.clicked=true; api.clicked=true; }
      ctl.swoop=1; ctl.sw=0;
      pluck(2,0.0,0.12); pluck(4,0.42,0.10); pluck(1,0.95,0.09);
      const fl=$('#flash'); fl.textContent='拣尽寒枝 不肯栖';
      fl.classList.remove('go'); void fl.offsetWidth; fl.classList.add('go');
    },clicked:false};
  return api;
}
"""

STAGES_JS = """const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(30,42,-160),ms:0.8,mph:0.22,mhaze:0.05,dirC:C(0xb0aa9a),dirI:0.46,
  dirP:new THREE.Vector3(50,110,30),ambC:C(0xd8d2c0),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,11,92],t:[0,10,82],lf:[0,13,-52],lt:[0,13,-52]},
  sky:()=>SK({fd:0.0045,star:0.05,ms:0.72,moon:new THREE.Vector3(40,50,-165)}) },
{ name:'疏桐缺月',dwell:17,river:0.02,build:bShutong,
  cam:{f:[0,6.2,24],t:[1.2,5.6,19],lf:[-0.5,5.6,-7],lt:[1.6,6.2,-12]},
  sky:()=>SK({fd:0.0056,star:0.04,ms:0.8,moon:new THREE.Vector3(30,42,-160)}) },
{ name:'寒枝沙洲',dwell:18,river:0.03,build:bShazhou,
  cam:{f:[0,6,21],t:[0.6,5.4,16],lf:[0,5.2,-9],lt:[1,5.6,-14]},
  sky:()=>SK({fd:0.0068,star:0.03,ms:0.88,mhaze:0.08,
    moon:new THREE.Vector3(-60,86,-185),dirC:C(0xa8a294),dirI:0.42,dirP:new THREE.Vector3(-40,100,-20)}) },
];
"""
