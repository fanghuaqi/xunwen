const SK=(o)=>Object.assign({
  top:C(0x1c1208),hor:C(0x50361a),bot:C(0x0a0704),fog:C(0x1a120a),fd:0.0055,star:0.5,
  moon:new THREE.Vector3(70,110,-210),ms:0.85,mph:0.28,mhaze:0.10,dirC:C(0xe8b070),dirI:0.52,
  dirP:new THREE.Vector3(-50,80,30),ambC:C(0x30200f),ambI:0.60},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,13,60],t:[0,14,52],lf:[-2,10,-44],lt:[-3,10.5,-46]},
  sky:()=>SK({top:C(0x241708),hor:C(0x5c3f1e),bot:C(0x0c0906),fog:C(0x1a120a),fd:0.0050,star:0.42,
    ms:0.9,mph:0.30,mhaze:0.08,moon:new THREE.Vector3(-80,86,-230),
    dirC:C(0xf0bc74),dirI:0.54,ambC:C(0x33220f),ambI:0.60}) },
{ name:'长安回望',dwell:18,river:0.04,build:bChangan,
  cam:{f:[0,13.5,32],t:[-2,14,28],lf:[-2,15,-56],lt:[-3,15,-58]},
  sky:()=>SK({top:C(0x1e1308),hor:C(0x553a1c),bot:C(0x0a0704),fog:C(0x1a120a),fd:0.0055,star:0.48,
    ms:0.8,mph:0.30,mhaze:0.10,moon:new THREE.Vector3(76,96,-212),
    dirC:C(0xe8b470),dirI:0.52,dirP:new THREE.Vector3(-46,80,28),ambC:C(0x30200f),ambI:0.62}) },
{ name:'一骑红尘',dwell:20,river:0.05,build:bHongchen,
  cam:{f:[6,5.2,16],t:[4,5.2,13],lf:[-4,4.2,-16],lt:[-6,4.2,-18]},
  sky:()=>SK({top:C(0x1c1108),hor:C(0x4c3218),bot:C(0x090604),fog:C(0x1a120a),fd:0.0053,star:0.52,
    ms:0.86,mph:0.26,mhaze:0.09,moon:new THREE.Vector3(-66,84,-204),
    dirC:C(0xeab878),dirI:0.50,dirP:new THREE.Vector3(-44,74,24),ambC:C(0x2e1f0e),ambI:0.60}) },
];
