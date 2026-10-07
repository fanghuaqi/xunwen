const SK=(o)=>Object.assign({
  top:C(0x14281c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.16,
  moon:new THREE.Vector3(62,118,-208),ms:0.7,mph:0.34,mhaze:0.09,dirC:C(0xdccb8c),dirI:0.46,
  dirP:new THREE.Vector3(42,88,28),ambC:C(0x22301f),ambI:0.63},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,12,58],t:[0,13,50],lf:[-2,7,-26],lt:[-3,7.5,-30]},
  sky:()=>SK({top:C(0x18301f),hor:C(0x436344),bot:C(0x0c1810),fog:C(0x0e1d16),fd:0.0048,star:0.10,
    ms:0.60,mph:0.36,mhaze:0.07,moon:new THREE.Vector3(-72,84,-228),
    dirC:C(0xe6d190),dirI:0.48,ambC:C(0x26351f),ambI:0.64}) },
{ name:'吹皱春水',dwell:18,river:0.05,build:bChunshui,
  cam:{f:[0,5.8,24],t:[1.2,5.6,20],lf:[-1,2.6,-11],lt:[-2.4,2.5,-13]},
  sky:()=>SK({top:C(0x16301f),hor:C(0x40603c),bot:C(0x0b1510),fog:C(0x101f17),fd:0.0058,star:0.10,
    ms:0.40,mph:0.40,mhaze:0.12,moon:new THREE.Vector3(74,62,-206),
    dirC:C(0xd8cf94),dirI:0.46,dirP:new THREE.Vector3(40,70,24),ambC:C(0x1e2c1e),ambI:0.66}) },
{ name:'倚阑望君',dwell:20,river:0.05,build:bYilan,
  cam:{f:[0.6,6.6,21],t:[0,6.2,18],lf:[-2,2.2,-8],lt:[-4,2.0,-10]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x36543a),bot:C(0x0a140f),fog:C(0x0e1d16),fd:0.0056,star:0.15,
    ms:0.62,mph:0.38,mhaze:0.09,moon:new THREE.Vector3(-84,64,-198),
    dirC:C(0xccc084),dirI:0.42,dirP:new THREE.Vector3(-50,70,20),ambC:C(0x1e2c1e),ambI:0.62}) },
];
