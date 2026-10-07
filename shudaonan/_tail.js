/* ---------------- UI ---------------- */
function fitPoemBox(segs){ // 竖排长句字号自适应：按最长一句的字数收放
  let maxLen=1;
  segs.forEach(s=>{ maxLen=Math.max(maxLen,[...s.c].length); });
  const avail=(window.innerHeight||720)*0.74;
  const fs=clamp(avail/(maxLen*1.24)||28,15,38);
  const box=$('#poemBox');
  if(box&&box.style&&box.style.setProperty)box.style.setProperty('--segFs',fs.toFixed(1)+'px');
}
function buildPoemDOM(idx){
  const line=POEM[idx-1], box=$('#poemBox');
  box.innerHTML='';
  fitPoemBox(line.segs);
  line.segs.forEach((seg,si)=>{
    const d=document.createElement('div'); d.className='seg';
    let pi=0,ci=0;
    for(const ch of seg.c){
      let el;
      if(/[，。、！？；：]/.test(ch)){
        el=document.createElement('span'); el.className='pu'; el.textContent=ch;
      }else{
        el=document.createElement('ruby'); el.className='zi';
        el.innerHTML='<span>'+ch+'</span><rt>'+(seg.p[pi++]||'')+'</rt>';
      }
      el.style.animationDelay=(0.25+(ci++)*0.13+si*0.55)+'s';
      d.appendChild(el);
    }
    box.appendChild(d);
  });
}
function fillNotes(idx){
  const line=POEM[idx-1];
  $('#yisi').textContent=line.yisi;
  const ul=$('#zhu'); ul.innerHTML='';
  line.zhu.forEach(z=>{ const li=document.createElement('li');
    li.innerHTML='<b>'+z[0]+'</b>'+z[1]; ul.appendChild(li); });
}
function buildDots(){
  const d=$('#dots');
  for(let i=1;i<=7;i++){
    const s=document.createElement('i');
    s.title='第'+CN[i-1]+'境 · '+POEM[i-1].name;
    s.addEventListener('click',()=>goto(i));
    d.appendChild(s);
  }
}
let tipTimer=null;
let autoSpeak=true;   // 进入新境后自动朗读诗句
let speakTimer=null;
function tip(msg,dur=3200){
  const t=$('#tip'); t.textContent=msg; t.classList.add('show');
  clearTimeout(tipTimer); tipTimer=setTimeout(()=>t.classList.remove('show'),dur);
}
function updateHUD(i){
  const hud=$('#hud');
  if(i===0){ hud.classList.add('hidden'); document.body.classList.add('no-poem');
    $('#jing').classList.remove('show'); return; }
  hud.classList.remove('hidden'); document.body.classList.remove('no-poem');
  $('#stageNo').textContent='第'+CN[i-1]+'境';
  $('#stageName').textContent=POEM[i-1].name;
  buildPoemDOM(i); fillNotes(i);
  document.querySelectorAll('#dots i').forEach((d,k)=>d.classList.toggle('on',k===i-1));
  const j=$('#jing'); j.classList.remove('show');
  setTimeout(()=>{ j.textContent=POEM[i-1].jing; j.classList.add('show'); },600);
  $('#zsBox').open=false;
}

/* ---------------- 场景切换 ---------------- */
function goto(i){
  if(state==='transition'||i===curIdx)return;
  i=clamp(i,0,7);
  stopSpeak();
  clearTimeout(speakTimer);
  $('#ending').classList.remove('show');
  curIdx=i;
  const def=STAGES[i];
  const st=def.build();
  scene.add(st.group); setFade(st.group,0);
  trans={t:0,dur:2.6,fromP:camera.position.clone(),fromL:curLook.clone(),
    toP:v3(def.cam.f),toL:v3(def.cam.lf),stage:st,old:curStageObj};
  skyFrom=cloneSky(SKYcur); skyTo=def.sky();
  stageT=0; autoT=0; state='transition';
  updateHUD(i);
  setAmbience(def.river);
  if(i>0){
    pluck(i%PENTA.length,0.3,0.15);
    pluck((i+3)%PENTA.length,0.75,0.11);
    if(st.onEnter)st.onEnter();
    if(autoSpeak)speakTimer=setTimeout(()=>{ if(curIdx===i)aiSpeak(stageAudio(i),POEM[i-1].read); },1600);
  }
  if(i===6)setTimeout(()=>tip('轻点画面 / 按空格 —— 绝壁显形，炸开万壑雷'),2600);
  if(i===7)setTimeout(()=>tip('轻点画面 / 按空格 —— 剑阁当关，万夫莫开'),2600);
}
function showEnding(){
  if(state!=='stage')return;
  state='ending';
  const box=$('#endPoem'); box.innerHTML='';
  POEM.forEach(line=>{
    line.segs.forEach(seg=>{
      const d=document.createElement('div'); d.className='seg';
      let pi=0;
      for(const ch of seg.c){
        let el;
        if(/[，。、！？；：]/.test(ch)){ el=document.createElement('span'); el.className='pu'; el.textContent=ch; }
        else{ el=document.createElement('ruby'); el.className='zi';
          el.innerHTML='<span>'+ch+'</span><rt>'+(seg.p[pi++]||'')+'</rt>'; }
        d.appendChild(el);
      }
      box.appendChild(d);
    });
  });
  $('#ending').classList.add('show');
  if(autoSpeak)aiSpeak('08.mp3',POEM.map(l=>l.read).join(''));
}
function hideEnding(to){
  $('#ending').classList.remove('show');
  state='stage';
  if(to==='cover'){ $('#cover').classList.remove('off'); goto(0); }
  else goto(1);
}

/* ---------------- 主循环 ---------------- */
function animate(){
  requestAnimationFrame(animate);
  const now=performance.now()/1000;
  let dt=clock.last?now-clock.last:0.016;
  clock.last=now; dt=Math.min(dt,0.05); clock.t+=dt;
  const t=clock.t;
  if(state==='transition'&&trans){
    trans.t+=dt;
    const k=ease(clamp(trans.t/trans.dur,0,1));
    camera.position.lerpVectors(trans.fromP,trans.toP,k);
    curLook.lerpVectors(trans.fromL,trans.toL,k);
    setFade(trans.stage.group,k);
    if(trans.old)setFade(trans.old.group,1-k);
    mixSky(k);
    if(trans.stage.update)trans.stage.update(trans.t,dt);
    if(k>=1){
      if(trans.old){ scene.remove(trans.old.group); disposeGroup(trans.old.group); }
      curStageObj=trans.stage; curDef=STAGES[curIdx];
      state='stage'; stageT=0; autoT=0;
    }
  }
  else if(state==='stage'&&curStageObj){
    stageT+=dt; autoT+=dt;
    if(curStageObj.update)curStageObj.update(stageT,dt);
    const p=Math.min(1,stageT/30);
    camera.position.set(lerp(curDef.cam.f[0],curDef.cam.t[0],p),
      lerp(curDef.cam.f[1],curDef.cam.t[1],p),lerp(curDef.cam.f[2],curDef.cam.t[2],p));
    curLook.set(lerp(curDef.cam.lf[0],curDef.cam.lt[0],p),
      lerp(curDef.cam.lf[1],curDef.cam.lt[1],p),lerp(curDef.cam.lf[2],curDef.cam.lt[2],p));
    if(autoMode&&curIdx>0){
      if(autoT>curDef.dwell){ if(curIdx===7)showEnding(); else goto(curIdx+1); }
    }
  }
  // 视差 + 呼吸
  if(curDef){
    const fwd=new THREE.Vector3().subVectors(curLook,camera.position).normalize();
    const right=new THREE.Vector3().crossVectors(fwd,new THREE.Vector3(0,1,0)).normalize();
    const up=new THREE.Vector3().crossVectors(right,fwd).normalize();
    camera.position.addScaledVector(right,mouse.x*2.4).addScaledVector(up,mouse.y*1.4);
    camera.position.y+=Math.sin(t*0.5)*0.16;
    camera.lookAt(curLook);
    if(curDef.roll&&state==='stage')camera.rotateZ(Math.sin(t*0.2)*curDef.roll);
  }
  if(bgRange)bgRange.update(t,mouse.x);   // 远山层间轻微视差
  applySky();
  renderer.render(scene,camera);
}

/* ---------------- 小测 ---------------- */
let qIdx=0,qScore=0;
function startQuiz(){
  qIdx=0; qScore=0;
  $('#quiz').classList.add('show');
  renderQuiz();
}
function renderQuiz(){
  $('#quizCnt').textContent='第 '+(qIdx+1)+' 题 / 共 '+QUIZ.length+' 题';
  const q=QUIZ[qIdx], body=$('#quizBody');
  body.innerHTML='<div id="quizQ">'+q.q+'</div>';
  q.o.forEach((op,i)=>{
    const b=document.createElement('button'); b.className='opt'; b.textContent=String.fromCharCode(65+i)+'. '+op;
    b.addEventListener('click',()=>{
      const opts=body.querySelectorAll('.opt');
      opts.forEach(x=>x.disabled=true);
      if(i===q.a){ b.classList.add('right'); qScore++; }
      else{ b.classList.add('wrong'); opts[q.a].classList.add('right'); }
      const nb=document.createElement('button');
      nb.id='quizNext'; nb.textContent=qIdx<QUIZ.length-1?'下一题':'查看结果';
      nb.addEventListener('click',()=>{ qIdx++; qIdx<QUIZ.length?renderQuiz():showResult(); });
      body.appendChild(nb);
    });
    body.appendChild(b);
  });
}
function showResult(){
  $('#quizCnt').textContent='测 验 完 成';
  const words=['初入蜀道，且随诗行','渐识崎岖，再诵几遍','已过青泥，颇得险意','胸有剑阁，险中见奇','长嗟一叹，深味其难','蜀道知己，危乎高哉'];
  $('#quizBody').innerHTML='<div id="quizResult"><div class="score">'+qScore+' / '+QUIZ.length+
    '</div><div class="word">「'+words[qScore]+'」</div></div>';
  const cb=document.createElement('button'); cb.id='quizClose'; cb.textContent='回到终章';
  cb.addEventListener('click',()=>$('#quiz').classList.remove('show'));
  $('#quizBody').appendChild(cb);
}

/* ---------------- 启动 ---------------- */
function boot(){
  try{
    renderer=new THREE.WebGLRenderer({antialias:true});
  }catch(e){ $('#err').style.display='flex'; return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.8));
  renderer.setSize(window.innerWidth,window.innerHeight);
  $('#app').appendChild(renderer.domElement);
  scene=new THREE.Scene();
  scene.fog=new THREE.FogExp2(0x1a120a,0.0058);
  camera=new THREE.PerspectiveCamera(55,window.innerWidth/window.innerHeight,0.1,1500);
  curLook=new THREE.Vector3();
  buildSky();
  buildDots();
  // 初始：封面境
  curIdx=0; curDef=STAGES[0];
  SKYcur=cloneSky(curDef.sky());
  curStageObj=curDef.build();
  scene.add(curStageObj.group); setFade(curStageObj.group,1);
  curStageObj.group.userData.fadeK=1;
  camera.position.set(...curDef.cam.f);
  curLook.set(...curDef.cam.lf);
  applySky();
  state='stage';
  window.addEventListener('resize',()=>{
    camera.aspect=window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth,window.innerHeight);
    if(curIdx>0)fitPoemBox(POEM[curIdx-1].segs);   // 竖排字号随窗高重算
  });
  window.addEventListener('pointermove',e=>{
    mouse.x=(e.clientX/window.innerWidth-0.5)*2;
    mouse.y=-(e.clientY/window.innerHeight-0.5)*2;
  });
  /* 交互点睛（全诗一处机制、两境可用）：第六境连峰飞湍、第七境剑阁崔嵬 —— 点击绝壁 */
  renderer.domElement.addEventListener('pointerdown',()=>{
    if(curIdx===6&&state==='stage'&&curStageObj&&curStageObj.click){curStageObj.click();return;}
    if(curIdx===7&&state==='stage'&&curStageObj&&curStageObj.click)curStageObj.click();
  });
  // 控件
  $('#enterBtn').addEventListener('click',()=>{
    initAudio();
    if(groupAudio.ctx&&groupAudio.ctx.state==='suspended')groupAudio.ctx.resume();
    $('#cover').classList.add('off');
    setAmbience(STAGES[1].river);
    goto(1);
  });
  $('#btnNext').addEventListener('click',()=>{ if(curIdx>=7)showEnding(); else goto(curIdx+1); });
  $('#btnPrev').addEventListener('click',()=>goto(curIdx-1));
  $('#btnAuto').addEventListener('click',e=>{
    autoMode=!autoMode; autoT=0;
    e.currentTarget.classList.toggle('on',autoMode);
    e.currentTarget.textContent='自动游览 · '+(autoMode?'开':'关');
  });
  $('#btnSpeak').addEventListener('click',()=>{
    if(curIdx>0)aiSpeak(stageAudio(curIdx),POEM[curIdx-1].read);
    else aiSpeak('00.mp3','蜀道难。唐，李白。噫吁嚱，危乎高哉！蜀道之难，难于上青天。');
  });
  $('#btnAutoSpeak').addEventListener('click',e=>{
    autoSpeak=!autoSpeak;
    e.currentTarget.classList.toggle('on',autoSpeak);
    e.currentTarget.textContent='自动朗读 · '+(autoSpeak?'开':'关');
    if(!autoSpeak)stopSpeak();
  });
  $('#btnPy').addEventListener('click',e=>{
    const off=document.body.classList.toggle('no-py-off');
    e.currentTarget.classList.toggle('on',!off);
    e.currentTarget.textContent='注音 · '+(off?'关':'开');
  });
  $('#btnSnd').addEventListener('click',e=>{
    groupAudio.muted=!groupAudio.muted;
    if(groupAudio.master)groupAudio.master.gain.value=groupAudio.muted?0:1;
    e.currentTarget.classList.toggle('on',!groupAudio.muted);
    e.currentTarget.textContent='声音 · '+(groupAudio.muted?'关':'开');
  });
  $('#btnFs').addEventListener('click',()=>{
    if(document.fullscreenElement)document.exitFullscreen();
    else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();
  });
  $('#btnQuiz').addEventListener('click',startQuiz);
  $('#btnPoemAudio').addEventListener('click',()=>aiSpeak('08.mp3',POEM.map(l=>l.read).join('')));
  $('#btnAgain').addEventListener('click',()=>hideEnding('start'));
  $('#btnCover').addEventListener('click',()=>hideEnding('cover'));
  window.addEventListener('keydown',e=>{
    if(document.activeElement&&document.activeElement.tagName==='BUTTON')document.activeElement.blur();
    if($('#quiz').classList.contains('show'))return;
    if(e.code==='ArrowRight'){ if(curIdx>=7)showEnding(); else goto(curIdx+1); }
    else if(e.code==='ArrowLeft')goto(curIdx-1);
    else if(e.code==='Space'){
      e.preventDefault();
      if(curIdx===6&&state==='stage'&&curStageObj.click)curStageObj.click();
      else if(curIdx===7&&state==='stage'&&curStageObj.click)curStageObj.click();
      else if(curIdx>=7)showEnding();
      else goto(curIdx+1);
    }
    else if(e.code==='Escape'){
      stopSpeak();
      $('#ending').classList.remove('show'); $('#quiz').classList.remove('show'); state='stage';
    }
  });
  animate();
}
function initApp(){
  if(window.__inited)return; window.__inited=true;
  if(window.THREE)boot();
}
</script>

<!-- Three.js 多源加载（cdnjs → jsdelivr → unpkg） -->
<script>
(function(){
  var S=['https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
        'https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js',
        'https://unpkg.com/three@0.128.0/build/three.min.js'];
  var i=0;
  function next(){
    if(window.THREE){ initApp(); return; }
    if(i>=S.length){ document.getElementById('err').style.display='flex'; return; }
    var s=document.createElement('script');
    s.src=S[i++];
    s.onload=next; s.onerror=next;
    document.head.appendChild(s);
  }
  next();
  setTimeout(function(){ if(!window.THREE)document.getElementById('err').style.display='flex'; },20000);
})();
</script>
</body>
</html>
