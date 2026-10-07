const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0056,star:0.18,
  moon:new THREE.Vector3(60,120,-210),ms:0.6,mph:0.3,mhaze:0.08,dirC:C(0xd8b878),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,11,62],t:[0,12,54],lf:[-2,9,-30],lt:[-2,10,-33]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3c5232),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0048,star:0.14,
    ms:0.34,mph:0.42,mhaze:0.05,moon:new THREE.Vector3(-60,70,-235),
    dirC:C(0xe0c48e),dirI:0.46,ambC:C(0x26351f),ambI:0.64}) },
{ name:'藕花深处',dwell:20,river:0.05,build:bWuru,
  cam:{f:[3.5,4.8,16],t:[0.5,4.4,12],lf:[-3,2.4,-1],lt:[-7,2.2,-4]},
  sky:()=>SK({top:C(0x112218),hor:C(0x2c442c),bot:C(0x0b1310),fog:C(0x101f17),fd:0.0058,star:0.12,
    ms:0.28,mph:0.44,mhaze:0.08,moon:new THREE.Vector3(85,42,-225),
    dirC:C(0xccb482),dirI:0.40,dirP:new THREE.Vector3(-45,60,25),ambC:C(0x1c2a1e),ambI:0.66}) },
{ name:'鸥鹭惊起',dwell:22,river:0.06,build:bJingdu,
  cam:{f:[3.2,4.4,16],t:[-0.5,4.0,12],lf:[-5,1.8,0],lt:[-9,2.4,-7]},
  sky:()=>SK({top:C(0x122418),hor:C(0x2e4830),bot:C(0x0a140f),fog:C(0x0e1d16),fd:0.0060,star:0.15,
    ms:0.3,mph:0.44,mhaze:0.07,moon:new THREE.Vector3(-90,52,-215),
    dirC:C(0xd0b884),dirI:0.42,dirP:new THREE.Vector3(-50,62,20),ambC:C(0x1e2c1e),ambI:0.64}) },
];
