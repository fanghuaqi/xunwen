const SK=(o)=>Object.assign({
  top:C(0x151d26),hor:C(0x2c3c4c),bot:C(0x10141a),fog:C(0x151d26),fd:0.0075,star:0.10,
  moon:new THREE.Vector3(56,104,-208),ms:0.45,mph:0.42,mhaze:0.16,dirC:C(0xa8bccc),dirI:0.42,
  dirP:new THREE.Vector3(38,72,26),ambC:C(0x1e2836),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.05,build:bCover,
  cam:{f:[0,10,58],t:[0,11,50],lf:[-2,5,-40],lt:[-3,5,-42]},
  sky:()=>SK({top:C(0x18202a),hor:C(0x33455a),bot:C(0x111620),fog:C(0x151d26),fd:0.0070,star:0.08,
    ms:0.42,mph:0.44,mhaze:0.18,moon:new THREE.Vector3(-70,80,-226),
    dirC:C(0xb0c0d0),dirI:0.42,ambC:C(0x202a38),ambI:0.66}) },
{ name:'江雨空啼',dwell:18,river:0.07,build:bJiangyu,
  cam:{f:[0,6.2,30],t:[1.5,6.0,26],lf:[-2,3.4,-14],lt:[-3.5,3.2,-16]},
  sky:()=>SK({top:C(0x161e28),hor:C(0x2e4052),bot:C(0x0f141c),fog:C(0x151d26),fd:0.0078,star:0.08,
    ms:0.40,mph:0.44,mhaze:0.18,moon:new THREE.Vector3(62,70,-206),
    dirC:C(0xa4b8c8),dirI:0.42,dirP:new THREE.Vector3(36,68,24),ambC:C(0x1e2836),ambI:0.68}) },
{ name:'烟笼十里',dwell:19,river:0.06,build:bYanlong,
  cam:{f:[-5,5.2,22],t:[-3,5.2,19],lf:[6,3.4,-6],lt:[8,3.2,-8]},
  sky:()=>SK({top:C(0x151d27),hor:C(0x2b3c4e),bot:C(0x0f141b),fog:C(0x151d26),fd:0.0082,star:0.09,
    ms:0.46,mph:0.42,mhaze:0.20,moon:new THREE.Vector3(-58,66,-200),
    dirC:C(0xa6bacb),dirI:0.42,dirP:new THREE.Vector3(-34,66,22),ambC:C(0x1e2734),ambI:0.68}) },
];
