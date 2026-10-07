const SK=(o)=>Object.assign({
  top:C(0x2a1a0c),hor:C(0x5a3c1a),bot:C(0x120d08),fog:C(0x1a120a),fd:0.0060,star:0.22,
  moon:new THREE.Vector3(-60,60,-210),ms:0.5,mph:0.40,mhaze:0.20,dirC:C(0xf0c078),dirI:0.54,
  dirP:new THREE.Vector3(-60,80,30),ambC:C(0x33220f),ambI:0.60},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,9,58],t:[0,10,50],lf:[0,12,-44],lt:[-1,12,-46]},
  sky:()=>SK({fd:0.0056,star:0.22,ms:0.5,mph:0.42,mhaze:0.18,moon:new THREE.Vector3(70,72,-220),
    dirC:C(0xe8bc74),dirI:0.52,ambC:C(0x32200f),ambI:0.60}) },
{ name:'千寻高塔',dwell:18,river:0.02,build:bQianxun,
  cam:{f:[0,8,30],t:[0,9,26],lf:[0,12,-40],lt:[0,12.5,-42]},
  sky:()=>SK({fd:0.0060,star:0.20,ms:0.45,mph:0.42,mhaze:0.18,moon:new THREE.Vector3(-66,64,-212),
    dirC:C(0xf0c078),dirI:0.54,dirP:new THREE.Vector3(-56,78,28),ambC:C(0x33220f),ambI:0.62}) },
{ name:'身在高层',dwell:20,river:0.02,build:bZuigao,
  cam:{f:[0,11,16],t:[0,11,13.5],lf:[0,5.5,-26],lt:[0,5.6,-28]},
  sky:()=>SK({fd:0.0058,star:0.18,ms:0.40,mph:0.42,mhaze:0.16,moon:new THREE.Vector3(-62,60,-206),
    dirC:C(0xffd28a),dirI:0.56,dirP:new THREE.Vector3(-52,74,26),ambC:C(0x352310),ambI:0.62}) },
];
