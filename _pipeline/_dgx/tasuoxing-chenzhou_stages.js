const SK=(o)=>Object.assign({
  top:C(0x0a0f17),hor:C(0x1d2733),bot:C(0x080b11),fog:C(0x151d26),fd:0.016,star:0.06,
  moon:new THREE.Vector3(0,-200,-160),ms:0.001,mph:0,mhaze:0,dirC:C(0x8fa0b8),dirI:0.30,
  dirP:new THREE.Vector3(40,90,30),ambC:C(0x25303e),ambI:0.62},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCoverTsuo,
  cam:{f:[0,7,46],t:[0,7.5,42],lf:[0,4.5,-24],lt:[0,4.8,-28]},
  sky:()=>SK({top:C(0x0d1320),hor:C(0x202b39),bot:C(0x0a0e15),fog:C(0x151d26),fd:0.017,star:0.06,
    dirC:C(0x8fa0b8),dirI:0.30,ambC:C(0x232e3c),ambI:0.66}) },
{ name:'雾失楼台',dwell:19,river:0.012,build:bWushiloutai,
  cam:{f:[0,5.4,20],t:[1.4,5.0,17],lf:[0,3.6,-6],lt:[0.8,3.4,-8]},
  sky:()=>SK({top:C(0x090e17),hor:C(0x1e2733),bot:C(0x080b10),fog:C(0x151d26),fd:0.020,star:0.03,
    ms:0.55,mph:0.42,mhaze:0.60,moon:new THREE.Vector3(-105,42,-240),
    dirC:C(0x939fb0),dirI:0.26,dirP:new THREE.Vector3(-50,50,-20),ambC:C(0x26313f),ambI:0.68}) },
{ name:'郴江之问',dwell:16,river:0.03,build:bChenjiang,
  cam:{f:[-2,6.2,21],t:[0.5,5.8,18],lf:[1,3.4,-12],lt:[2,3.8,-16]},
  sky:()=>SK({top:C(0x0a0f18),hor:C(0x1d2733),bot:C(0x080b11),fog:C(0x151d26),fd:0.016,star:0.04,
    dirC:C(0x8ea0b8),dirI:0.30,ambC:C(0x242f3d),ambI:0.64}) },
];
