const SK=(o)=>Object.assign({
  top:C(0x081020),hor:C(0x1d3350),bot:C(0x0c1016),fog:C(0x0a1526),fd:0.0045,star:0.85,
  moon:new THREE.Vector3(120,150,-210),ms:1.0,mph:0,mhaze:0,dirC:C(0x9db8e8),dirI:0.7,
  dirP:new THREE.Vector3(60,120,40),ambC:C(0x31405c),ambI:0.55},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.02,build:bCover,
  cam:{f:[0,12,80],t:[0,14,72],lf:[0,24,-40],lt:[0,24,-40]},
  sky:()=>SK({top:C(0x100b08),hor:C(0x2c1c10),bot:C(0x0c0806),fog:C(0x181008),fd:0.0042,star:0.5,
    ms:1.4,mph:0.1,mhaze:0.14,moon:new THREE.Vector3(-50,70,-190),
    dirC:C(0xd8a860),dirI:0.45,ambC:C(0x2c211a),ambI:0.6}) },
{ name:'东望泪湿',dwell:17,river:0.02,build:bDongwang,
  cam:{f:[0,7.5,28],t:[2,7,24],lf:[2,6,-40],lt:[3,5.5,-46]},
  sky:()=>SK({top:C(0x0e0a08),hor:C(0x33210f),bot:C(0x0d0906),fog:C(0x1a120a),fd:0.0068,star:0.4,
    ms:2.4,mph:0.08,mhaze:0.22,moon:new THREE.Vector3(-90,60,-170),
    dirC:C(0xd8a860),dirI:0.5,ambC:C(0x2c211a),ambI:0.6}) },
{ name:'马上传语',dwell:18,river:0.02,build:bChuanyu,
  cam:{f:[0,6.5,26],t:[-1,6,22],lf:[0,4.5,-14],lt:[0,4.2,-15]},
  sky:()=>SK({top:C(0x0d0a08),hor:C(0x2e1e10),bot:C(0x0c0907),fog:C(0x19110a),fd:0.0065,star:0.4,
    ms:1.6,mph:0.14,mhaze:0.16,moon:new THREE.Vector3(-70,80,-180),
    dirC:C(0xd8a860),dirI:0.46,ambC:C(0x2c211a),ambI:0.62}) },
];
