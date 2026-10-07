const SK=(o)=>Object.assign({
  top:C(0x14281c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0e1d16),fd:0.0060,star:0.16,
  moon:new THREE.Vector3(62,118,-208),ms:0.7,mph:0.34,mhaze:0.09,dirC:C(0xdccb8c),dirI:0.46,
  dirP:new THREE.Vector3(42,88,28),ambC:C(0x22301f),ambI:0.63},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.03,build:bCover,
  cam:{f:[0,8,46],t:[0,8.5,40],lf:[-2,4.5,-26],lt:[-3,4.6,-29]},
  sky:()=>SK({top:C(0x16301f),hor:C(0x40603c),bot:C(0x0b1510),fog:C(0x0e1d16),fd:0.0056,star:0.14,
    ms:0.65,mph:0.34,mhaze:0.08,moon:new THREE.Vector3(-66,82,-222),
    dirC:C(0xe0cf8e),dirI:0.48,ambC:C(0x26351f),ambI:0.64}) },
{ name:'百啭千声',dwell:18,river:0.04,build:bBaizhuan,
  cam:{f:[0,6.0,24],t:[1.2,6.0,20.5],lf:[-1,3.4,-10],lt:[-2.4,3.4,-12]},
  sky:()=>SK({top:C(0x152c1e),hor:C(0x3c5c3c),bot:C(0x0a1410),fog:C(0x101f17),fd:0.0060,star:0.14,
    ms:0.6,mph:0.36,mhaze:0.10,moon:new THREE.Vector3(62,74,-206),
    dirC:C(0xdccf90),dirI:0.48,dirP:new THREE.Vector3(38,78,26),ambC:C(0x22301f),ambI:0.64}) },
{ name:'金笼林间',dwell:19,river:0.04,build:bZizai,
  cam:{f:[0,6.4,20],t:[0.6,6.4,17],lf:[-1,3.6,-8],lt:[-2,3.6,-10]},
  sky:()=>SK({top:C(0x142a1c),hor:C(0x3a5a3c),bot:C(0x0a1410),fog:C(0x0f1e16),fd:0.0062,star:0.14,
    ms:0.62,mph:0.34,mhaze:0.09,moon:new THREE.Vector3(-62,76,-204),
    dirC:C(0xdbcd90),dirI:0.48,dirP:new THREE.Vector3(-36,76,24),ambC:C(0x22301f),ambI:0.64}) },
];
