const SK=(o)=>Object.assign({
  top:C(0xe9e2d0),hor:C(0xded5bd),bot:C(0xcfc6ae),fog:C(0xe6dfcc),fd:0.0052,star:0.04,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd9d4c4),dirI:0.44,
  dirP:new THREE.Vector3(-50,110,30),ambC:C(0xd6d8c6),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,6.4,52],t:[0,6.6,46],lf:[-1,4.2,-24],lt:[-2,4.4,-28]},
  sky:()=>SK({fd:0.0046,star:0.03,dirI:0.44}) },
{ name:'独立疏篱',dwell:17,river:0.02,build:bShuli,
  cam:{f:[-4,4.6,20],t:[-2,4.6,17],lf:[2,3.4,-6],lt:[3,3.5,-8]},
  sky:()=>SK({fd:0.0056,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.42,dirP:new THREE.Vector3(-45,105,20),ambC:C(0xd4d8c6),ambI:0.62}) },
{ name:'抱香枝头',dwell:19,river:0.02,build:bBaoxiang,
  cam:{f:[2.5,3.8,12],t:[1.2,3.9,10],lf:[-2,3.4,-4],lt:[-3,3.5,-5.5]},
  sky:()=>SK({fd:0.0068,star:0.02,dirC:C(0xd8d4c0),
    dirI:0.40,dirP:new THREE.Vector3(-42,100,20),ambC:C(0xd4d8c6),ambI:0.60}) },
];
