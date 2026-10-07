const SK=(o)=>Object.assign({
  top:C(0x14281c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0060,star:0.16,
  moon:new THREE.Vector3(62,118,-208),ms:0.7,mph:0.34,mhaze:0.09,dirC:C(0xdccb8c),dirI:0.46,
  dirP:new THREE.Vector3(42,88,28),ambC:C(0x22301f),ambI:0.63},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.05,build:bCover,
  cam:{f:[0,7.2,42],t:[0,7.6,36],lf:[-2,4.2,-22],lt:[-3,4.3,-25]},
  sky:()=>SK({top:C(0x16301f),hor:C(0x40603c),bot:C(0x0b1510),fog:C(0x0e1d16),fd:0.0056,star:0.14,
    ms:0.65,mph:0.34,mhaze:0.08,moon:new THREE.Vector3(-66,82,-222),
    dirC:C(0xe0cf8e),dirI:0.48,ambC:C(0x26351f),ambI:0.64}) },
{ name:'篱外春船',dwell:18,river:0.07,build:bBuxi,
  cam:{f:[0,6.0,24],t:[1.0,6.0,20.5],lf:[-2,3.5,-12],lt:[-3,3.5,-14]},
  sky:()=>SK({top:C(0x152c1e),hor:C(0x3c5c3c),bot:C(0x0a1410),fog:C(0x101f17),fd:0.0060,star:0.14,
    ms:0.6,mph:0.36,mhaze:0.10,moon:new THREE.Vector3(62,74,-206),
    dirC:C(0xdccf90),dirI:0.48,dirP:new THREE.Vector3(38,78,26),ambC:C(0x22301f),ambI:0.64}) },
{ name:'小童去关',dwell:19,river:0.06,build:bQuguan,
  cam:{f:[0,5.4,17],t:[0.4,5.4,14],lf:[-1.5,2.9,-8],lt:[-2.5,2.9,-10]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0f1e16),fd:0.0062,star:0.14,
    ms:0.62,mph:0.34,mhaze:0.09,moon:new THREE.Vector3(-62,76,-204),
    dirC:C(0xdbcd90),dirI:0.48,dirP:new THREE.Vector3(-36,76,24),ambC:C(0x22301f),ambI:0.64}) },
];
