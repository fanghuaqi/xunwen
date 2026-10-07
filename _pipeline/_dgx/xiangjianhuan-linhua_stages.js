const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.2,
  moon:new THREE.Vector3(60,120,-210),ms:0.8,mph:0.3,mhaze:0.08,dirC:C(0xd8c88a),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,12,78],t:[0,13,68],lf:[0,14,-40],lt:[0,15,-42]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0052,star:0.18,
    ms:0.7,mph:0.35,mhaze:0.06,moon:new THREE.Vector3(-60,80,-230),
    dirC:C(0xe0cf8e),dirI:0.5,ambC:C(0x26351f),ambI:0.64}) },
{ name:'花谢匆匆',dwell:16,river:0.03,build:bHuaxie,
  cam:{f:[0,6.5,28],t:[2.5,6,24],lf:[-5,7,-14],lt:[-3,6.5,-16]},
  sky:()=>SK({top:C(0x15271b),hor:C(0x2c4830),bot:C(0x0b1410),fog:C(0x101f18),fd:0.0062,star:0.12,
    ms:0.6,mph:0.4,mhaze:0.10,moon:new THREE.Vector3(-80,60,-220),
    dirC:C(0xc9bd85),dirI:0.4,dirP:new THREE.Vector3(-50,70,20),ambC:C(0x1e2c1e),ambI:0.66}) },
{ name:'长恨东流',dwell:18,river:0.09,build:bDongliu,
  cam:{f:[0,7,32],t:[-2.5,6.5,28],lf:[6,5,-16],lt:[9,5,-20]},
  sky:()=>SK({top:C(0x0a1510),hor:C(0x1a2c1e),bot:C(0x080f0b),fog:C(0x0c1a13),fd:0.0075,star:0.3,
    ms:0.55,mph:0.46,mhaze:0.12,moon:new THREE.Vector3(-100,50,-190),
    dirC:C(0x8fa890),dirI:0.3,dirP:new THREE.Vector3(-60,60,10),ambC:C(0x18241c),ambI:0.6}) },
];
