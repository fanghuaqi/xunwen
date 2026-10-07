const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.44,
  dirP:new THREE.Vector3(-50,110,30),ambC:C(0xd6d8c6),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,48],t:[0,8.4,42],lf:[-2,4.6,-26],lt:[-3,4.7,-29]},
  sky:()=>SK({fd:0.0046,star:0.03,dirI:0.44}) },
{ name:'木末红萼',dwell:18,river:0.02,build:bMumo,
  cam:{f:[0,6.0,22],t:[0.8,6.0,18.5],lf:[0,3.6,-12],lt:[-1,3.6,-14]},
  sky:()=>SK({fd:0.0056,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.44,dirP:new THREE.Vector3(-45,105,20),ambC:C(0xd4d8c6),ambI:0.62}) },
{ name:'涧户开落',dwell:19,river:0.03,build:bJianhu,
  cam:{f:[0,5.4,20],t:[0.4,5.4,17],lf:[-1,3.2,-12],lt:[-2,3.2,-14]},
  sky:()=>SK({fd:0.0060,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.46,dirP:new THREE.Vector3(-42,100,20),ambC:C(0xd4d8c6),ambI:0.62}) },
];
