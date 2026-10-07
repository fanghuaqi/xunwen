const SK=(o)=>Object.assign({
  top:C(0x14100c),hor:C(0x3a2c20),bot:C(0x05070d),fog:C(0x0a1526),fd:0.0056,star:0.50,
  moon:new THREE.Vector3(70,110,-210),ms:0.9,mph:0.30,mhaze:0.10,dirC:C(0xd9c090),dirI:0.46,
  dirP:new THREE.Vector3(-50,80,30),ambC:C(0x2a1c12),ambI:0.58},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,48],t:[0,8.5,42],lf:[-2,5,-26],lt:[-3,5.2,-29]},
  sky:()=>SK({fd:0.0052,star:0.46,ms:0.9,mph:0.30,mhaze:0.10,moon:new THREE.Vector3(-66,92,-214),
    dirC:C(0xd4bc8c),dirI:0.46}) },
{ name:'东风香雾',dwell:18,river:0.02,build:bDongfeng,
  cam:{f:[0,7,24],t:[1,7,20.5],lf:[-2,4,-10],lt:[-3,4.1,-12]},
  sky:()=>SK({fd:0.0056,star:0.48,ms:0.92,mph:0.28,mhaze:0.12,moon:new THREE.Vector3(62,88,-206),
    dirC:C(0xd9c090),dirI:0.46,dirP:new THREE.Vector3(-46,78,26),ambC:C(0x2a1c12),ambI:0.60}) },
{ name:'烧烛红妆',dwell:20,river:0.02,build:bShaozhu,
  cam:{f:[0,4.2,13],t:[0.6,4.2,10.5],lf:[-1,3,-6],lt:[-2,3.1,-7.5]},
  sky:()=>SK({fd:0.0056,star:0.44,ms:0.88,mph:0.30,mhaze:0.12,moon:new THREE.Vector3(-58,72,-198),
    dirC:C(0xc8ae84),dirI:0.42,dirP:new THREE.Vector3(-42,72,22),ambC:C(0x261a10),ambI:0.58}) },
];
