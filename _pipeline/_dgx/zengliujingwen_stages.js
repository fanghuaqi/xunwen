const SK=(o)=>Object.assign({
  top:C(0x14281c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0056,star:0.16,
  moon:new THREE.Vector3(62,118,-208),ms:0.7,mph:0.34,mhaze:0.09,dirC:C(0xdccb8c),dirI:0.46,
  dirP:new THREE.Vector3(42,88,28),ambC:C(0x22301f),ambI:0.63},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,8,50],t:[0,8.5,44],lf:[-2,4,-30],lt:[-3,4.2,-33]},
  sky:()=>SK({top:C(0x16301f),hor:C(0x3e5c3e),bot:C(0x0b1510),fog:C(0x0e1d16),fd:0.0052,star:0.12,
    ms:0.6,mph:0.4,mhaze:0.10,moon:new THREE.Vector3(-68,80,-224),
    dirC:C(0xe0cf8e),dirI:0.46,ambC:C(0x26351f),ambI:0.64}) },
{ name:'荷尽菊残',dwell:18,river:0.05,build:bHejin,
  cam:{f:[0,5.6,22],t:[1.2,5.5,18.5],lf:[-1,2.4,-8],lt:[-2.4,2.3,-10]},
  sky:()=>SK({top:C(0x142a1d),hor:C(0x365434),bot:C(0x0a130f),fog:C(0x0e1d16),fd:0.0056,star:0.14,
    ms:0.5,mph:0.4,mhaze:0.12,moon:new THREE.Vector3(70,66,-206),
    dirC:C(0xd6c88c),dirI:0.44,dirP:new THREE.Vector3(40,70,24),ambC:C(0x1e2c1e),ambI:0.64}) },
{ name:'橙黄橘绿',dwell:19,river:0.04,build:bChengju,
  cam:{f:[0,5.4,20],t:[0.8,5.4,17],lf:[3,2.6,-6],lt:[4,2.5,-8]},
  sky:()=>SK({top:C(0x17321f),hor:C(0x41603e),bot:C(0x0c1710),fog:C(0x101f17),fd:0.0054,star:0.12,
    ms:0.6,mph:0.38,mhaze:0.10,moon:new THREE.Vector3(-66,72,-204),
    dirC:C(0xe4d492),dirI:0.48,ambC:C(0x26351f),ambI:0.65}) },
];
