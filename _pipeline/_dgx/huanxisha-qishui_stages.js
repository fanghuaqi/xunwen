const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.2,
  moon:new THREE.Vector3(60,120,-210),ms:0.8,mph:0.3,mhaze:0.08,dirC:C(0xd8c88a),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,11,64],t:[0,12,56],lf:[-2,10,-36],lt:[-2,11,-38]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0048,star:0.16,
    ms:0.7,mph:0.35,mhaze:0.06,moon:new THREE.Vector3(-70,80,-230),
    dirC:C(0xe0cf8e),dirI:0.48,ambC:C(0x26351f),ambI:0.64}) },
{ name:'兰芽浸溪',dwell:17,river:0.05,build:bLanya,
  cam:{f:[1,6.5,26],t:[3,6,22],lf:[-4,3.5,-10],lt:[-6,3.2,-12]},
  sky:()=>SK({top:C(0x112218),hor:C(0x27422c),bot:C(0x0b1310),fog:C(0x101f17),fd:0.0060,star:0.14,
    ms:0.45,mph:0.4,mhaze:0.12,moon:new THREE.Vector3(80,60,-210),
    dirC:C(0xc2bd90),dirI:0.40,dirP:new THREE.Vector3(45,65,25),ambC:C(0x1c2a1e),ambI:0.66}) },
{ name:'流水能西',dwell:18,river:0.06,build:bLiuxi,
  cam:{f:[4,5.6,19],t:[-1,5.8,16],lf:[-8,2.6,-6],lt:[-12,2.6,-7]},
  sky:()=>SK({top:C(0x122418),hor:C(0x2c4630),bot:C(0x0a140f),fog:C(0x0e1d16),fd:0.0056,star:0.16,
    ms:0.6,mph:0.38,mhaze:0.09,moon:new THREE.Vector3(-85,62,-200),
    dirC:C(0xc9bc85),dirI:0.42,dirP:new THREE.Vector3(-50,70,20),ambC:C(0x1e2c1e),ambI:0.64}) },
];
