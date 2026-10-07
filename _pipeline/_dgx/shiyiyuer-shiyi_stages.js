const SK=(o)=>Object.assign({
  top:C(0x241809),hor:C(0x4a3418),bot:C(0x0f0a06),fog:C(0x1a120a),fd:0.0058,star:0.24,
  moon:new THREE.Vector3(-58,64,-208),ms:0.55,mph:0.40,mhaze:0.20,dirC:C(0xc8a070),dirI:0.48,
  dirP:new THREE.Vector3(-56,78,28),ambC:C(0x2c1e0e),ambI:0.60},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,8,50],t:[0,8.5,44],lf:[0,5,-34],lt:[-1,5.2,-37]},
  sky:()=>SK({fd:0.0054,star:0.22,ms:0.55,mph:0.42,mhaze:0.18,moon:new THREE.Vector3(66,70,-218),
    dirC:C(0xbe9a6c),dirI:0.46}) },
{ name:'僵卧孤村',dwell:18,river:0.02,build:bJiangwo,
  cam:{f:[0,6.2,24],t:[1,6.2,20.5],lf:[-1,3.6,-14],lt:[-2,3.6,-16]},
  sky:()=>SK({fd:0.0058,star:0.20,ms:0.52,mph:0.42,mhaze:0.20,moon:new THREE.Vector3(-60,66,-206),
    dirC:C(0xc8a070),dirI:0.46,dirP:new THREE.Vector3(-52,74,26),ambC:C(0x2c1e0e),ambI:0.62}) },
{ name:'铁马冰河',dwell:20,river:0.03,build:bTiemai,
  cam:{f:[0,7.0,26],t:[0.5,7.0,22],lf:[-2,4.6,-22],lt:[-3,4.6,-25]},
  sky:()=>SK({fd:0.0058,star:0.18,ms:0.50,mph:0.42,mhaze:0.20,moon:new THREE.Vector3(-56,62,-202),
    dirC:C(0xd0a878),dirI:0.50,dirP:new THREE.Vector3(-48,70,24),ambC:C(0x2e2010),ambI:0.62}) },
];
