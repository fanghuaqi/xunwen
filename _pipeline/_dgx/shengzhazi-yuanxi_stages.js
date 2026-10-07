const SK=(o)=>Object.assign({
  top:C(0x070810),hor:C(0x2c1c10),bot:C(0x060508),fog:C(0x110d0a),fd:0.0052,star:0.30,
  moon:new THREE.Vector3(-38,38,-140),ms:1.05,mph:0,mhaze:0.05,dirC:C(0xffbe78),dirI:0.22,
  dirP:new THREE.Vector3(-28,34,-18),ambC:C(0x30281e),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCover,
  cam:{f:[0,7.0,30],t:[0,6.7,27],lf:[0,4.6,-16],lt:[0,4.4,-18]},
  sky:()=>SK({fd:0.0052,star:0.34,hor:C(0x2c1c10),dirC:C(0xffb070),ambC:C(0x2c261e),ambI:0.60}) },
{ name:'灯如昼',dwell:16,river:0.015,build:bDengRuZhou,
  cam:{f:[0,5.4,14.5],t:[0.4,5.15,12.2],lf:[0,4.1,-9],lt:[0.6,3.9,-10]},
  sky:()=>SK({top:C(0x070810),hor:C(0x38220f),bot:C(0x060508),fog:C(0x140e08),fd:0.0058,star:0.28,
    dirC:C(0xffbe78),dirI:0.22,dirP:new THREE.Vector3(-28,34,-18),
    ambC:C(0x2a221a),ambI:0.60}) },
{ name:'月依旧',dwell:19,river:0.015,build:bYueYiJiu,
  cam:{f:[0,5.4,14.5],t:[0.4,5.15,12.2],lf:[0,4.1,-9],lt:[0.6,3.9,-10]},
  sky:()=>SK({top:C(0x070810),hor:C(0x241a16),bot:C(0x060508),fog:C(0x110e11),fd:0.0066,star:0.32,
    dirC:C(0xd8a888),dirI:0.18,dirP:new THREE.Vector3(-28,34,-18),
    ambC:C(0x2a2826),ambI:0.58}) },
];
