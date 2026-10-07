const SK=(o)=>Object.assign({
  top:C(0x16281a),hor:C(0x4a5a34),bot:C(0x0a1410),fog:C(0x101d13),fd:0.0060,star:0.18,
  moon:new THREE.Vector3(60,118,-208),ms:0.7,mph:0.34,mhaze:0.09,dirC:C(0xe8c078),dirI:0.54,
  dirP:new THREE.Vector3(-70,60,26),ambC:C(0x26341c),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,8,46],t:[0,8.5,40],lf:[-2,4.4,-24],lt:[-3,4.5,-27]},
  sky:()=>SK({top:C(0x1a2c1a),hor:C(0x5a5c34),bot:C(0x0b1510),fog:C(0x101d13),fd:0.0056,star:0.16,
    ms:0.92,mph:0.10,mhaze:0.04,moon:new THREE.Vector3(-68,30,-204),
    dirC:C(0xf0c470),dirI:0.54,dirP:new THREE.Vector3(-72,58,24),ambC:C(0x28361c),ambI:0.64}) },
{ name:'绕舍秋丛',dwell:18,river:0.04,build:bRaoshe,
  cam:{f:[0,6.2,26],t:[1.2,6.2,22.5],lf:[-2,3.8,-12],lt:[-3,3.8,-14]},
  sky:()=>SK({top:C(0x182a1a),hor:C(0x53562f),bot:C(0x0a1410),fog:C(0x111e14),fd:0.0060,star:0.14,
    ms:0.95,mph:0.08,mhaze:0.04,moon:new THREE.Vector3(-72,26,-200),
    dirC:C(0xecc470),dirI:0.54,dirP:new THREE.Vector3(-68,56,22),ambC:C(0x26341c),ambI:0.64}) },
{ name:'偏爱菊花',dwell:19,river:0.04,build:bPianai,
  cam:{f:[0,5.2,17],t:[0.5,5.2,14],lf:[-1,2.9,-6],lt:[-2,2.9,-8]},
  sky:()=>SK({top:C(0x172818),hor:C(0x4e522d),bot:C(0x0a1410),fog:C(0x101d13),fd:0.0062,star:0.14,
    ms:0.94,mph:0.08,mhaze:0.04,moon:new THREE.Vector3(-66,28,-198),
    dirC:C(0xefc06c),dirI:0.56,dirP:new THREE.Vector3(-64,54,20),ambC:C(0x26341c),ambI:0.64}) },
];