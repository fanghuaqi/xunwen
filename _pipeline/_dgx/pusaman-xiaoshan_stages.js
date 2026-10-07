const SK=(o)=>Object.assign({
  top:C(0x0a0a12),hor:C(0x2e2118),bot:C(0x0a0708),fog:C(0x140f0a),fd:0.0075,star:0.12,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xffc890),dirI:0.32,
  dirP:new THREE.Vector3(-20,50,26),ambC:C(0x322618),ambI:0.72},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.015,build:bCover,
  cam:{f:[0,10,46],t:[0,9.4,41],lf:[0,8,-10],lt:[0,7.6,-12]},
  sky:()=>SK({top:C(0x090a14),hor:C(0x3a2818),bot:C(0x0a0708),fog:C(0x130d08),fd:0.0052,star:0.30,
    ms:0.55,mph:0.32,mhaze:0.12,moon:new THREE.Vector3(70,30,-170),
    dirC:C(0xd8a860),dirI:0.30,ambC:C(0x2c2018),ambI:0.68}) },
{ name:'金屏晓妆',dwell:17,river:0.015,build:bJinPing,
  cam:{f:[0,6.4,15.5],t:[1.2,6.0,13],lf:[0.2,5.0,-5.5],lt:[0.8,4.9,-6]},
  sky:()=>SK({top:C(0x0a0910),hor:C(0x32241a),bot:C(0x0a0708),fog:C(0x150f0a),fd:0.0085,star:0.08,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xffc890),dirI:0.30,ambC:C(0x322618),ambI:0.72}) },
{ name:'花面交映',dwell:19,river:0.015,build:bJiaoYing,
  cam:{f:[0,6.3,14.5],t:[-0.8,5.9,12.2],lf:[0.2,5.0,-6],lt:[0,4.9,-6.4]},
  sky:()=>SK({top:C(0x0b0a11),hor:C(0x362718),bot:C(0x0a0708),fog:C(0x160f0a),fd:0.0090,star:0.05,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xffd8a0),dirI:0.32,ambC:C(0x362a1e),ambI:0.74}) },
];
