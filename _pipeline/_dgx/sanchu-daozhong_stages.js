const SK=(o)=>Object.assign({
  top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0060,star:0.20,
  moon:new THREE.Vector3(60,120,-210),ms:0.8,mph:0.30,mhaze:0.08,dirC:C(0xd8c88a),dirI:0.50,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,8,46],t:[0,8.5,40],lf:[-2,4.5,-26],lt:[-3,4.6,-29]},
  sky:()=>SK({top:C(0x16301f),hor:C(0x40603c),bot:C(0x0b1510),fog:C(0x0e1d16),fd:0.0056,star:0.18,
    ms:0.75,mph:0.32,mhaze:0.07,moon:new THREE.Vector3(-66,82,-222),
    dirC:C(0xe0d090),dirI:0.50,ambC:C(0x26351f),ambI:0.64}) },
{ name:'梅黄溪尽',dwell:18,river:0.05,build:bMeihuang,
  cam:{f:[0,6.0,24],t:[1.2,5.9,20.5],lf:[-1,3.0,-10],lt:[-2.4,3.0,-12]},
  sky:()=>SK({top:C(0x152c1e),hor:C(0x3c5c3c),bot:C(0x0a1410),fog:C(0x101f17),fd:0.0060,star:0.16,
    ms:0.6,mph:0.34,mhaze:0.10,moon:new THREE.Vector3(62,74,-206),
    dirC:C(0xdcd090),dirI:0.50,dirP:new THREE.Vector3(38,80,26),ambC:C(0x22301f),ambI:0.64}) },
{ name:'绿阴黄鹂',dwell:19,river:0.04,build:bLvyin,
  cam:{f:[0,6.2,20],t:[0.6,6.2,17],lf:[-1,3.6,-9],lt:[-2,3.6,-11]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0f1e16),fd:0.0062,star:0.16,
    ms:0.62,mph:0.32,mhaze:0.09,moon:new THREE.Vector3(-62,76,-204),
    dirC:C(0xdad092),dirI:0.50,dirP:new THREE.Vector3(-36,76,24),ambC:C(0x22301f),ambI:0.64}) },
];
