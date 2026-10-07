const SK=(o)=>Object.assign({
  top:C(0xf2ead8),hor:C(0xe9dcc0),bot:C(0xe2d2b2),fog:C(0xe8dcc4),fd:0.005,star:0.07,
  moon:new THREE.Vector3(55,80,-200),ms:1.15,mph:0,mhaze:0,dirC:C(0xd9b98a),dirI:0.55,
  dirP:new THREE.Vector3(60,120,40),ambC:C(0x8a7a5e),ambI:0.72},o);
/* cam/dwell/river 沿用旧页基准；fd 按浅色赛道预算收紧（≤0.008） */
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCover,
  cam:{f:[0,11,74],t:[0,9,64],lf:[0,13,-40],lt:[0,11,-40]},
  sky:()=>SK({top:C(0xf2ead8),hor:C(0xe9dcc0),bot:C(0xe2d2b2),fog:C(0xe8dcc4),fd:0.0048,star:0.07,
    ms:1.15,moon:new THREE.Vector3(55,80,-200),dirC:C(0xd9b98a),dirI:0.55,ambC:C(0x8a7a5e),ambI:0.72}) },
{ name:'手中线',dwell:16,river:0.008,build:bThread,
  cam:{f:[10,6,19],t:[-4,5.2,15],lf:[0.5,4,0],lt:[-0.6,3.9,-0.5]},
  sky:()=>SK({top:C(0xeadfc6),hor:C(0xe0d0ae),bot:C(0xd6c29c),fog:C(0xe2d3b4),fd:0.0080,star:0.03,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),dirC:C(0xffd9a0),dirI:0.28,ambC:C(0x6a5638),ambI:0.9}) },
{ name:'密密缝',dwell:18,river:0.005,build:bSew,
  cam:{f:[0.8,4.9,6.8],t:[-1.2,4.3,5.7],lf:[-0.4,3.7,0.2],lt:[-0.7,3.5,-0.1]},
  sky:()=>SK({top:C(0xd9cdb4),hor:C(0xcabb9c),bot:C(0xbfab8a),fog:C(0xd2c2a2),fd:0.0080,star:0.03,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),dirC:C(0xe8c890),dirI:0.2,ambC:C(0x55462f),ambI:0.85}) },
{ name:'三春晖',dwell:20,river:0.03,build:bSpring,
  cam:{f:[0,2.6,9],t:[0,8,-12],lf:[0,4.5,-24],lt:[0,7,-70]},
  sky:()=>SK({top:C(0xf6eeda),hor:C(0xf0e2c0),bot:C(0xe7d8b4),fog:C(0xefe4c8),fd:0.0038,star:0.03,
    ms:2.3,moon:new THREE.Vector3(30,150,-190),dirC:C(0xffe2a8),dirI:1.0,
    dirP:new THREE.Vector3(30,110,40),ambC:C(0x9a8a68),ambI:0.85}) },
];
