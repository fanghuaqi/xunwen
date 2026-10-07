const SK=(o)=>Object.assign({
  top:C(0x0e1420),hor:C(0x1c2735),bot:C(0x0d1117),fog:C(0x131a26),fd:0.0062,star:0.34,
  moon:new THREE.Vector3(30,120,-200),ms:1.5,mph:0.12,mhaze:0.12,dirC:C(0xb8c6d8),dirI:0.44,
  dirP:new THREE.Vector3(-40,90,26),ambC:C(0x1c2636),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.05,build:bCover,
  cam:{f:[0,10,54],t:[0,10.5,48],lf:[-2,6,-40],lt:[-3,6.2,-43]},
  sky:()=>SK({fd:0.0056,star:0.32,ms:1.45,mph:0.12,mhaze:0.10,moon:new THREE.Vector3(-64,96,-216),
    dirC:C(0xb4c2d4),dirI:0.44}) },
{ name:'青山画舫',dwell:19,river:0.07,build:bQingshan,
  cam:{f:[-2,9,34],t:[0,9.5,30],lf:[0,5,-34],lt:[-1,5.2,-37]},
  sky:()=>SK({fd:0.0062,star:0.32,ms:1.5,mph:0.12,mhaze:0.12,moon:new THREE.Vector3(58,88,-206),
    dirC:C(0xb8c6d8),dirI:0.44,dirP:new THREE.Vector3(36,72,24),ambC:C(0x1c2636),ambI:0.64}) },
{ name:'杭州汴州',dwell:20,river:0.06,build:bHangzhou,
  cam:{f:[0,7,20],t:[0.8,7,17],lf:[-2,4.6,-10],lt:[-3,4.6,-12]},
  sky:()=>SK({fd:0.0064,star:0.30,ms:1.55,mph:0.12,mhaze:0.12,moon:new THREE.Vector3(-54,80,-200),
    dirC:C(0xbac8da),dirI:0.46,dirP:new THREE.Vector3(-34,68,22),ambC:C(0x1e2838),ambI:0.64}) },
];
