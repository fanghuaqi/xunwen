const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.44,
  dirP:new THREE.Vector3(-50,110,30),ambC:C(0xd6d8c6),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,7.5,50],t:[0,7.5,44],lf:[-2,4.5,-28],lt:[-3,4.6,-31]},
  sky:()=>SK({fd:0.0046,star:0.03,dirI:0.44}) },
{ name:'寥落宫花',dwell:18,river:0.02,build:bLiaoluo,
  cam:{f:[0,6.4,26],t:[1,6.4,22.5],lf:[-2,4.0,-14],lt:[-3,4.0,-16]},
  sky:()=>SK({fd:0.0056,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.44,dirP:new THREE.Vector3(-45,105,20),ambC:C(0xd4d8c6),ambI:0.62}) },
{ name:'白头宫女',dwell:19,river:0.02,build:bBaitou,
  cam:{f:[0,4.6,16],t:[0.4,4.6,13.5],lf:[-1,2.6,-8],lt:[-2,2.6,-9.5]},
  sky:()=>SK({fd:0.0060,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.46,dirP:new THREE.Vector3(-42,100,20),ambC:C(0xd4d8c6),ambI:0.62}) },
];
