const SK=(o)=>Object.assign({
  top:C(0x0a0a14),hor:C(0x3a2414),bot:C(0x0a0708),fog:C(0x120d0a),fd:0.0050,star:0.20,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd8a060),dirI:0.30,
  dirP:new THREE.Vector3(-40,50,26),ambC:C(0x302418),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCover,
  cam:{f:[0,10,46],t:[0,9.4,41],lf:[0,8,-10],lt:[0,7.6,-12]},
  sky:()=>SK({top:C(0x090a12),hor:C(0x43291a),bot:C(0x0a0708),fog:C(0x120d0a),fd:0.0050,star:0.24,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xd8a060),dirI:0.30,ambC:C(0x2e2418),ambI:0.66}) },
{ name:'新曲旧亭',dwell:18,river:0.015,build:bXinTing,
  cam:{f:[0,6.2,16.5],t:[1.0,5.8,13.5],lf:[0.4,4.6,-4.5],lt:[1.0,4.5,-5.2]},
  sky:()=>SK({top:C(0x0c0a12),hor:C(0x4e2d16),bot:C(0x0c0806),fog:C(0x1a110a),fd:0.0068,star:0.10,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xffb070),dirI:0.34,dirP:new THREE.Vector3(-60,34,-40),ambC:C(0x362416),ambI:0.72}) },
{ name:'花落燕归',dwell:19,river:0.015,build:bYanGui,
  cam:{f:[0,4.8,14],t:[-0.6,4.4,11.6],lf:[0,3.3,-6],lt:[-0.8,3.2,-7]},
  sky:()=>SK({top:C(0x0a0b16),hor:C(0x33221e),bot:C(0x090708),fog:C(0x141019),fd:0.0075,star:0.22,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xd89a78),dirI:0.26,ambC:C(0x2e2620),ambI:0.70}) },
];
