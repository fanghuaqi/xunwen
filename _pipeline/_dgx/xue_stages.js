const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.005,star:0.05,
  moon:new THREE.Vector3(140,120,-210),ms:1.0,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.55,
  dirP:new THREE.Vector3(60,120,40),ambC:C(0xd8d2c0),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,11,88],t:[0,11,78],lf:[0,22,-50],lt:[0,22,-50]},
  sky:()=>SK({fd:0.0042,star:0.06,ms:0.75,moon:new THREE.Vector3(150,120,-205)}) },
{ name:'千山鸟绝',dwell:16,river:0.015,build:bMountains,
  cam:{f:[0,10,96],t:[0,8,66],lf:[0,26,-90],lt:[0,40,-120]},
  sky:()=>SK({fd:0.0046,star:0.05,ms:0.85,moon:new THREE.Vector3(150,130,-210)}) },
{ name:'万径踪灭',dwell:15,river:0.015,build:bPaths,
  cam:{f:[0,11,66],t:[0,6,42],lf:[0,3,-36],lt:[0,2.4,-70]},
  sky:()=>SK({fd:0.0075,star:0.04,ms:0.5,moon:new THREE.Vector3(120,100,-200),dirC:C(0xd5d1c4),dirI:0.4}) },
{ name:'孤舟蓑翁',dwell:16,river:0.05,build:bBoat,
  cam:{f:[5,4.9,14.5],t:[-2.5,3.4,11],lf:[0,2.9,-4.5],lt:[0,2.7,-6]},
  sky:()=>SK({top:C(0xdcd6c4),hor:C(0xd2c9b2),fd:0.0062,star:0.04,ms:0.001,
    moon:new THREE.Vector3(0,-400,0),dirC:C(0xc9c6ba),dirI:0.35,ambC:C(0xd2ccb8),ambI:0.65}) },
{ name:'独钓寒江',dwell:20,river:0.06,roll:0.015,build:bSnowSolo,
  cam:{f:[0,9,66],t:[0,3.2,-16],lf:[0,4,-40],lt:[0,2.2,-50]},
  sky:()=>SK({top:C(0xefe9d8),hor:C(0xe4dcc7),fd:0.0056,star:0.03,ms:0.001,
    moon:new THREE.Vector3(0,-400,0),dirC:C(0xd4d1c6),dirI:0.3,ambC:C(0xdcd6c2),ambI:0.7}) },
];
