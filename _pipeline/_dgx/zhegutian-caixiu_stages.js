const SK=(o)=>Object.assign({
  top:C(0x090a12),hor:C(0x3a2414),bot:C(0x0a0708),fog:C(0x110d0a),fd:0.0058,star:0.50,
  moon:new THREE.Vector3(0,-400,0),ms:0.001,mph:0,mhaze:0,dirC:C(0xd8a060),dirI:0.30,
  dirP:new THREE.Vector3(-40,50,26),ambC:C(0x2e2418),ambI:0.66},o);
const STAGES=[
{ key:'cover',name:'卷首',dwell:0,river:0.012,build:bCover,
  cam:{f:[0,10,46],t:[0,9.4,41],lf:[0,8,-10],lt:[0,7.6,-12]},
  sky:()=>SK({top:C(0x090a12),hor:C(0x3c2414),bot:C(0x0a0708),fog:C(0x110d0a),fd:0.0058,star:0.52,
    ms:0.85,mph:0.10,mhaze:0.10,moon:new THREE.Vector3(-70,95,-190),
    dirC:C(0xd8a060),dirI:0.30,ambC:C(0x2c241a),ambI:0.68}) },
{ name:'舞低楼月',dwell:19,river:0.012,build:bWuYue,
  cam:{f:[0,5.5,16],t:[1.0,5.1,13.6],lf:[0.4,4.0,-4.5],lt:[1.0,3.9,-5.2]},
  sky:()=>SK({top:C(0x0b0a12),hor:C(0x2e1c10),bot:C(0x0b0806),fog:C(0x140e08),fd:0.0085,star:0.14,
    ms:0.001,moon:new THREE.Vector3(0,-400,0),
    dirC:C(0xffb070),dirI:0.32,dirP:new THREE.Vector3(-56,34,-40),ambC:C(0x342416),ambI:0.72}) },
{ name:'银釭疑梦',dwell:20,river:0.010,build:bDengZhao,
  cam:{f:[0,4.2,12.8],t:[0.5,4.0,10.8],lf:[0,2.6,-2.2],lt:[0.5,2.5,-2.8]},
  sky:()=>SK({top:C(0x0a0b14),hor:C(0x241a1c),bot:C(0x090809),fog:C(0x141014),fd:0.0130,star:0.12,
    ms:0.5,mph:0.14,mhaze:0.16,moon:new THREE.Vector3(50,120,-200),
    dirC:C(0xa8886a),dirI:0.22,ambC:C(0x2e2822),ambI:0.74}) },
];
