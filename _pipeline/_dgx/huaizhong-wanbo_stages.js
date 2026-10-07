const SK=(o)=>Object.assign({
  top:C(0x0e1420),hor:C(0x1c2735),bot:C(0x0d1117),fog:C(0x131a26),fd:0.0064,star:0.30,
  moon:new THREE.Vector3(30,120,-200),ms:1.2,mph:0.14,mhaze:0.12,dirC:C(0xa8bccc),dirI:0.42,
  dirP:new THREE.Vector3(-40,90,26),ambC:C(0x1a2430),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.06,build:bCover,
  cam:{f:[0,9,50],t:[0,9.5,44],lf:[-2,5,-30],lt:[-3,5.2,-33]},
  sky:()=>SK({fd:0.0060,star:0.28,ms:1.15,mph:0.14,mhaze:0.10,moon:new THREE.Vector3(-62,92,-214),
    dirC:C(0xa4b8c8),dirI:0.42}) },
{ name:'春阴幽花',dwell:18,river:0.06,build:bChunyin,
  cam:{f:[0,7.0,26],t:[1.2,7.0,22.5],lf:[-1,3.8,-12],lt:[-2.4,3.8,-14]},
  sky:()=>SK({fd:0.0064,star:0.28,ms:1.2,mph:0.14,mhaze:0.12,moon:new THREE.Vector3(58,84,-206),
    dirC:C(0xa8bccc),dirI:0.42,dirP:new THREE.Vector3(36,74,24),ambC:C(0x1a2430),ambI:0.64}) },
{ name:'孤舟潮生',dwell:20,river:0.09,build:bChaosheng,
  cam:{f:[0,6.4,20],t:[0.8,6.4,17],lf:[-2,3.4,-14],lt:[-3,3.4,-16]},
  sky:()=>SK({fd:0.0066,star:0.26,ms:1.15,mph:0.14,mhaze:0.14,moon:new THREE.Vector3(-54,72,-198),
    dirC:C(0xa0b4c4),dirI:0.42,dirP:new THREE.Vector3(-34,68,22),ambC:C(0x1a222c),ambI:0.62}) },
];
