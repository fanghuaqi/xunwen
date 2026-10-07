const SK=(o)=>Object.assign({
  top:C(0x0e1420),hor:C(0x1c2735),bot:C(0x0d1117),fog:C(0x131a26),fd:0.0064,star:0.30,
  moon:new THREE.Vector3(30,120,-200),ms:1.3,mph:0.14,mhaze:0.12,dirC:C(0xa8bccc),dirI:0.42,
  dirP:new THREE.Vector3(-40,90,26),ambC:C(0x1a2430),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.06,build:bCover,
  cam:{f:[0,9,54],t:[0,9.5,48],lf:[-2,5,-32],lt:[-3,5.2,-35]},
  sky:()=>SK({fd:0.0058,star:0.28,ms:1.25,mph:0.14,mhaze:0.10,moon:new THREE.Vector3(-62,92,-214),
    dirC:C(0xa4b8c8),dirI:0.42}) },
{ name:'飞桥石矶',dwell:19,river:0.08,build:bFeiqiao,
  cam:{f:[0,8.0,28],t:[0.6,8.0,24.5],lf:[-2,4.4,-14],lt:[-3,4.4,-16]},
  sky:()=>SK({fd:0.0064,star:0.28,ms:1.3,mph:0.14,mhaze:0.12,moon:new THREE.Vector3(58,86,-206),
    dirC:C(0xa8bccc),dirI:0.42,dirP:new THREE.Vector3(36,76,24),ambC:C(0x1a2430),ambI:0.64}) },
{ name:'桃花清溪',dwell:20,river:0.09,build:bTaohua,
  cam:{f:[0,6.6,22],t:[0.6,6.6,19],lf:[-1.5,3.4,-16],lt:[-2.5,3.4,-18]},
  sky:()=>SK({fd:0.0066,star:0.26,ms:1.25,mph:0.14,mhaze:0.14,moon:new THREE.Vector3(-54,74,-198),
    dirC:C(0xa6bacb),dirI:0.42,dirP:new THREE.Vector3(-34,70,22),ambC:C(0x1a222c),ambI:0.62}) },
];
