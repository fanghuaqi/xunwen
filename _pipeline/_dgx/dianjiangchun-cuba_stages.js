const SK=(o)=>Object.assign({
  top:C(0x152c1f),hor:C(0x3a5c42),bot:C(0x0c1711),fog:C(0x0e1d16),fd:0.0054,star:0.08,
  moon:new THREE.Vector3(-85,52,-210),ms:0.42,mph:0.52,mhaze:0.05,dirC:C(0xd8c88a),dirI:0.48,
  dirP:new THREE.Vector3(-45,75,35),ambC:C(0x243320),ambI:0.64},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,11,58],t:[0,10,50],lf:[-2,7,-26],lt:[-3,6,-30]},
  sky:()=>SK({top:C(0x142a1e),hor:C(0x365640),bot:C(0x0c1610),fd:0.0050,star:0.10,
    ms:0.50,mph:0.5,dirC:C(0xe0cf8e),dirI:0.46}) },
{ name:'露浓花瘦',dwell:17,river:0.02,build:bNong,
  cam:{f:[1.5,4.8,17],t:[4,4.2,13],lf:[-2,2.8,-5],lt:[-3.5,2.5,-7]},
  sky:()=>SK({fd:0.0054,star:0.08,ms:0.42,dirC:C(0xd8c88a),dirI:0.50}) },
{ name:'却把青梅嗅',dwell:19,river:0.02,build:bXiu,
  cam:{f:[0,4.6,17],t:[-3.5,4.0,14],lf:[-3,2.6,-8],lt:[-5,2.5,-10]},
  sky:()=>SK({top:C(0x172f22),hor:C(0x3e6246),bot:C(0x0d1812),fd:0.0058,star:0.06,
    ms:0.36,mph:0.54,dirC:C(0xdcc98c),dirI:0.52,ambC:C(0x28381f),ambI:0.66}) },
];
