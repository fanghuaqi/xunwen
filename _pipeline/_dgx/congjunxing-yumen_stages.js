const SK=(o)=>Object.assign({
  top:C(0x140f0a),hor:C(0x3a2a18),bot:C(0x0c0805),fog:C(0x1a120a),fd:0.006,star:0.2,
  moon:new THREE.Vector3(-60,26,-190),ms:0.5,mph:0,mhaze:0,dirC:C(0xc89860),dirI:0.42,
  dirP:new THREE.Vector3(-50,70,30),ambC:C(0x33281a),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverCjx,
  cam:{f:[0,10,68],t:[0,9.4,58],lf:[0,8,-34],lt:[0,9,-44]},
  sky:()=>SK({top:C(0x16100a),hor:C(0x342414),bot:C(0x0b0805),fog:C(0x191108),fd:0.0058,star:0.20,
    ms:0.5,mhaze:0.08,moon:new THREE.Vector3(-75,24,-195),dirI:0.40}) },
{ name:'长云暗雪',dwell:18,river:0.02,build:bChangyunY,
  cam:{f:[0,6.5,30],t:[-1,6.2,24],lf:[0,7,-60],lt:[1,8,-80]},
  sky:()=>SK({top:C(0x0e0b08),hor:C(0x2a2014),bot:C(0x0a0705),fog:C(0x170f08),fd:0.0070,star:0.10,
    ms:0.22,mhaze:0.20,moon:new THREE.Vector3(-90,14,-200),dirC:C(0xa88658),dirI:0.28,ambI:0.56}) },
{ name:'百战金甲',dwell:19,river:0.05,build:bJinjia,
  cam:{f:[0,6,27],t:[0,5.6,21],lf:[0,4.5,-16],lt:[2,5,-30]},
  sky:()=>SK({top:C(0x15100a),hor:C(0x3e2c16),bot:C(0x0c0805),fog:C(0x191109),fd:0.0062,star:0.26,
    ms:0.5,mph:0.05,mhaze:0.06,moon:new THREE.Vector3(-70,28,-195),dirC:C(0xd8a860),dirI:0.50,ambI:0.62}) },
];
