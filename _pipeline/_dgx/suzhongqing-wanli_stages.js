const SK=(o)=>Object.assign({
  top:C(0x140f0a),hor:C(0x3a2a18),bot:C(0x0c0805),fog:C(0x1a120a),fd:0.006,star:0.2,
  moon:new THREE.Vector3(-60,26,-190),ms:0.5,mph:0,mhaze:0,dirC:C(0xc89860),dirI:0.42,
  dirP:new THREE.Vector3(-50,70,30),ambC:C(0x33281a),ambI:0.6},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverSzq,
  cam:{f:[0,10,70],t:[0,9,60],lf:[0,9,-30],lt:[0,9,-38]},
  sky:()=>SK({top:C(0x16100a),hor:C(0x3a2a18),bot:C(0x0b0805),fog:C(0x191108),fd:0.0060,star:0.22,
    ms:0.55,moon:new THREE.Vector3(-70,24,-190),dirI:0.40}) },
{ name:'梦戍梁州',dwell:17,river:0.02,build:bMengshu,
  cam:{f:[0,7,30],t:[-2,6.4,24],lf:[0,5,-14],lt:[-3,5.5,-22]},
  sky:()=>SK({top:C(0x1a1008),hor:C(0x4a3018),bot:C(0x0c0805),fog:C(0x1c130a),fd:0.0058,star:0.26,
    ms:0.5,mph:0.05,mhaze:0.05,moon:new THREE.Vector3(-90,20,-185),dirC:C(0xe0a860),dirI:0.55,ambI:0.64}) },
{ name:'尘暗貂裘',dwell:17,river:0.006,build:bChenan,
  cam:{f:[0,5.5,17],t:[1.2,5,14],lf:[0,3.8,-4],lt:[0.5,4,-7]},
  sky:()=>SK({top:C(0x0e0b08),hor:C(0x2a2418),bot:C(0x0a0705),fog:C(0x15100a),fd:0.0075,star:0.08,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),dirC:C(0x8a7a5e),dirI:0.26,ambC:C(0x2e2820),ambI:0.74}) },
{ name:'天山沧洲',dwell:20,river:0.05,build:bTianshan,
  cam:{f:[0,5.5,30],t:[0,5,25],lf:[0,7,-36],lt:[0,7.5,-44]},
  sky:()=>SK({top:C(0x120d09),hor:C(0x332617),bot:C(0x0b0805),fog:C(0x171009),fd:0.0068,star:0.18,
    ms:0.45,moon:new THREE.Vector3(-85,32,-185),dirC:C(0xb08858),dirI:0.32,ambI:0.60}) },
];
