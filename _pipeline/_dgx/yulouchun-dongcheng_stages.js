const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.2,
  moon:new THREE.Vector3(0,-80,-200),ms:0.001,mph:0.3,mhaze:0.08,dirC:C(0xd8cfae),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,12,78],t:[0,13,68],lf:[0,14,-40],lt:[0,15,-42]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0055,star:0.15,
    dirC:C(0xd8cfae),dirI:0.5,ambC:C(0x26351f),ambI:0.64}) },
{ name:'东城春晓',dwell:16,river:0.03,build:bDongcheng,
  cam:{f:[0,6.5,28],t:[2.5,6,24],lf:[0,7,-14],lt:[-2,6.5,-16]},
  sky:()=>SK({top:C(0x18301f),hor:C(0x46624a),bot:C(0x0b1610),fog:C(0x122016),fd:0.0062,star:0.08,
    dirC:C(0xe4dcb8),dirI:0.62,dirP:new THREE.Vector3(50,100,20),ambC:C(0x2a3a24),ambI:0.68}) },
{ name:'花间晚照',dwell:18,river:0.04,build:bWanzhao,
  cam:{f:[0,6.5,30],t:[-2.5,6,26],lf:[0,6.5,-15],lt:[2,6,-17]},
  sky:()=>SK({top:C(0x0e1c15),hor:C(0x42362c),bot:C(0x0a130e),fog:C(0x101d15),fd:0.0070,star:0.22,
    dirC:C(0xc99a80),dirI:0.42,dirP:new THREE.Vector3(-60,50,10),ambC:C(0x203020),ambI:0.60}) },
];
