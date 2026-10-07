const SK=(o)=>Object.assign({
  top:C(0x081020),hor:C(0x1d3350),bot:C(0x0c1016),fog:C(0x0a1526),fd:0.0045,star:0.85,
  moon:new THREE.Vector3(120,150,-210),ms:1.0,mph:0,mhaze:0,dirC:C(0x9db8e8),dirI:0.7,
  dirP:new THREE.Vector3(60,120,40),ambC:C(0x31405c),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCover,
  cam:{f:[0,12,80],t:[0,14,72],lf:[0,22,-40],lt:[0,22,-40]},
  sky:()=>SK({top:C(0x0c0e14),hor:C(0x222832),bot:C(0x0c0e12),fog:C(0x141820),fd:0.0042,star:0.5,
    ms:1.3,mph:0.06,mhaze:0.08,moon:new THREE.Vector3(-50,90,-190),
    dirC:C(0xaab6c8),dirI:0.42,ambC:C(0x242830),ambI:0.62}) },
{ name:'沙似雪',dwell:18,river:0.012,build:bShasixue,
  cam:{f:[0,8,34],t:[-2,7.5,30],lf:[0,8,-24],lt:[-0.6,7.8,-25]},
  sky:()=>SK({top:C(0x0a0d16),hor:C(0x1e2634),bot:C(0x0c0e12),fog:C(0x12161e),fd:0.0048,star:0.4,
    ms:2.6,mph:0,mhaze:0.06,moon:new THREE.Vector3(-40,150,-200),
    dirC:C(0xb8c4d8),dirI:0.55,ambC:C(0x262c38),ambI:0.6}) },
{ name:'芦管望乡',dwell:17,river:0.012,build:bLuguan,
  cam:{f:[0,7,30],t:[-2,6.5,26],lf:[0,8,-24],lt:[-0.5,8.2,-25]},
  sky:()=>SK({top:C(0x0a0d16),hor:C(0x1c2432),bot:C(0x0b0e12),fog:C(0x12161e),fd:0.0052,star:0.45,
    ms:2.2,mph:0,mhaze:0.06,moon:new THREE.Vector3(-40,140,-200),
    dirC:C(0xb8c4d8),dirI:0.5,ambC:C(0x262c38),ambI:0.6}) },
];
