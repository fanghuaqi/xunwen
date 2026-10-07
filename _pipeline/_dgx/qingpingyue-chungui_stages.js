const SK=(o)=>Object.assign({
  top:C(0x142c1e),hor:C(0x3c5c40),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0055,star:0.15,
  moon:new THREE.Vector3(-70,54,-215),ms:0.55,mph:0.45,mhaze:0.06,dirC:C(0xe6d2a0),dirI:0.46,
  dirP:new THREE.Vector3(45,70,25),ambC:C(0x22301f),ambI:0.64},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,11,64],t:[0,12,56],lf:[-2,10,-36],lt:[-2,11,-38]},
  sky:()=>SK({top:C(0x152e1f),hor:C(0x40603f),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0050,star:0.18,
    ms:0.6,mph:0.42,mhaze:0.05,moon:new THREE.Vector3(-75,50,-220),
    dirC:C(0xe8d4a2),dirI:0.44,ambC:C(0x243320),ambI:0.64}) },
{ name:'春归何处',dwell:16,river:0.05,build:bChungui,
  cam:{f:[-1,5.2,20],t:[1,5.0,17],lf:[-1,3.0,-14],lt:[-4,2.8,-16]},
  sky:()=>SK({top:C(0x132919),hor:C(0x37543a),bot:C(0x0b1310),fog:C(0x101f17),fd:0.0058,star:0.12,
    ms:0.5,mph:0.46,mhaze:0.08,moon:new THREE.Vector3(-70,48,-210),
    dirC:C(0xcac294),dirI:0.40,dirP:new THREE.Vector3(45,68,25),ambC:C(0x1e2c1e),ambI:0.66}) },
{ name:'问取黄鹂',dwell:18,river:0.05,build:bWenqu,
  cam:{f:[-1,4.6,16],t:[0.5,4.3,13],lf:[0.8,3.4,-9],lt:[-0.5,3.3,-11]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x3e5e40),bot:C(0x0a140f),fog:C(0x0e1d16),fd:0.0052,star:0.10,
    ms:0.5,mph:0.45,mhaze:0.06,moon:new THREE.Vector3(-80,44,-205),
    dirC:C(0xd8c896),dirI:0.43,dirP:new THREE.Vector3(-40,70,20),ambC:C(0x203020),ambI:0.65}) },
];
