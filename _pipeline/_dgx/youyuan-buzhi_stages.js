const SK=(o)=>Object.assign({
  top:C(0x12261c),hor:C(0x2e4a30),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.006,star:0.2,
  moon:new THREE.Vector3(60,120,-210),ms:0.8,mph:0.3,mhaze:0.08,dirC:C(0xd8c88a),dirI:0.5,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x22301f),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9.2,58],t:[0,9.8,50],lf:[0,6.2,-24],lt:[0,6.8,-30]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x3a5a40),bot:C(0x0c1610),fog:C(0x0e1d16),fd:0.0048,star:0.15,
    ms:0.6,mph:0.32,mhaze:0.07,moon:new THREE.Vector3(-70,64,-220),
    dirC:C(0xd8d8a0),dirI:0.44,ambC:C(0x24331f),ambI:0.64}) },
{ name:'屐齿苍苔',dwell:17,river:0.012,build:bCangtai,
  cam:{f:[4.6,4.5,14.5],t:[2.8,4.2,11.5],lf:[-0.6,3.0,-13.5],lt:[-1.0,3.1,-14]},
  sky:()=>SK({top:C(0x112218),hor:C(0x243c2a),bot:C(0x0a130f),fog:C(0x101f17),fd:0.0062,star:0.12,
    ms:0.42,mph:0.42,mhaze:0.12,moon:new THREE.Vector3(85,48,-210),
    dirC:C(0xb8bd92),dirI:0.34,dirP:new THREE.Vector3(-40,58,22),ambC:C(0x1a261c),ambI:0.68}) },
{ name:'红杏出墙',dwell:18,river:0.015,build:bXing,
  cam:{f:[5.4,4.8,15.5],t:[3.4,5.0,12.5],lf:[1.0,5.7,-12],lt:[0.2,5.9,-11]},
  sky:()=>SK({top:C(0x15291b),hor:C(0x3c5a3c),bot:C(0x0b150e),fog:C(0x0e1d15),fd:0.0056,star:0.14,
    ms:0.5,mph:0.36,mhaze:0.08,moon:new THREE.Vector3(90,56,-205),
    dirC:C(0xd8cc96),dirI:0.46,dirP:new THREE.Vector3(46,66,26),ambC:C(0x1e2c1e),ambI:0.66}) },
];
