const SK=(o)=>Object.assign({
  top:C(0x0a0910),hor:C(0x2a2014),bot:C(0x0a0708),fog:C(0x150f08),fd:0.0075,star:0.12,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xffc890),dirI:0.32,
  dirP:new THREE.Vector3(-20,50,26),ambC:C(0x322414),ambI:0.72},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCover,
  cam:{f:[0,10,46],t:[0,9.4,41],lf:[0,8,-10],lt:[0,7.6,-12]},
  sky:()=>SK({top:C(0x090a12),hor:C(0x382616),bot:C(0x0a0708),fog:C(0x130d06),fd:0.0058,star:0.30,
    ms:0.50,mph:0.30,mhaze:0.10,moon:new THREE.Vector3(-80,34,-180),
    dirC:C(0xd8a860),dirI:0.30,ambC:C(0x2c2014),ambI:0.66}) },
{ name:'金缕少年',dwell:16,river:0.015,build:bJinLv,
  cam:{f:[0,6.4,15.5],t:[1.0,6.0,13],lf:[0,5.0,-5.5],lt:[0.6,4.9,-6]},
  sky:()=>SK({top:C(0x0a0910),hor:C(0x302216),bot:C(0x0a0708),fog:C(0x150f08),fd:0.0075,star:0.08,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xffc890),dirI:0.30,ambC:C(0x322414),ambI:0.72}) },
{ name:'花开堪折',dwell:18,river:0.015,build:bZheHua,
  cam:{f:[0,6.3,14.5],t:[-0.8,5.9,12.2],lf:[0.4,5.0,-6],lt:[0,4.9,-6.4]},
  sky:()=>SK({top:C(0x0b0a11),hor:C(0x342414),bot:C(0x0a0708),fog:C(0x160f08),fd:0.0080,star:0.05,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xffd8a0),dirI:0.32,ambC:C(0x362816),ambI:0.74}) },
];
