const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.2,
  moon:new THREE.Vector3(60,120,-210),ms:0.8,mph:0.3,mhaze:0.08,dirC:C(0xd8c88a),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,12,78],t:[0,13,68],lf:[0,14,-40],lt:[0,15,-42]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0052,star:0.16,
    ms:0.7,mph:0.35,mhaze:0.06,moon:new THREE.Vector3(-60,80,-230),
    dirC:C(0xe0cf8e),dirI:0.5,ambC:C(0x26351f),ambI:0.64}) },
{ name:'芳草天涯',dwell:16,river:0.03,build:bChuncan,
  cam:{f:[0,6.5,30],t:[2.5,6,26],lf:[-4,6,-14],lt:[-6,6,-18]},
  sky:()=>SK({top:C(0x15271b),hor:C(0x2c4830),bot:C(0x0b1410),fog:C(0x101f18),fd:0.0062,star:0.12,
    ms:0.6,mph:0.4,mhaze:0.10,moon:new THREE.Vector3(-80,60,-220),
    dirC:C(0xc9bd85),dirI:0.42,dirP:new THREE.Vector3(-50,70,20),ambC:C(0x1e2c1e),ambI:0.66}) },
{ name:'墙里墙外',dwell:18,river:0.03,build:bQiang,
  cam:{f:[4.5,5.2,15],t:[-2,5.6,11],lf:[-3,5.4,-16],lt:[-7,5.6,-20]},
  sky:()=>SK({top:C(0x112017),hor:C(0x26422c),bot:C(0x0a130e),fog:C(0x0e1c15),fd:0.0070,star:0.2,
    ms:0.55,mph:0.42,mhaze:0.12,moon:new THREE.Vector3(-90,55,-200),
    dirC:C(0xc2b47c),dirI:0.36,dirP:new THREE.Vector3(-45,65,15),ambC:C(0x1a281a),ambI:0.64}) },
];
