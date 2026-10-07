# 循文入境 · 引擎架构与硬性约束

参考实现：`assets/reference-jiangjinjiu.html`（约 1900 行，单文件，按下面的函数名在文件内检索）。
引擎五个部分：**引导加载 → 天空/氛围系统 → 场景管理 → 通用构件 → 朗读管线**。改造新诗时，1/2/4/5 基本不动，只动第 3 部分（数据 + 各境 builder）。

## 1. 引导加载（不可改动的骨架）

Three.js 用 r128 UMD，三个 CDN 顺序回退（cdnjs → jsdelivr → unpkg），保证 file:// 双击可用、国内可达：

```html
<script>
(function(){
  var S=['https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
        'https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js',
        'https://unpkg.com/three@0.128.0/build/three.min.js'];
  var i=0;
  function next(){
    if(window.THREE){ initApp(); return; }
    if(i>=S.length){ document.getElementById('err').style.display='flex'; return; }
    var s=document.createElement('script'); s.src=S[i++]; s.onload=next; s.onerror=next;
    document.head.appendChild(s);
  }
  next();
})();
</script>
```

主脚本在 CDN 加载完成前就解析执行，因此——

> **硬性约束：主脚本顶层禁止出现任何 `THREE.xxx` 求值。**

- 共享几何点表用惰性函数：`function gobletPts(){ if(!G)G=[...].map(p=>new THREE.Vector2(...)); return G; }`
- 每境的天空参数必须是工厂：`sky:()=>SK({moon:new THREE.Vector3(...)})`（`SK` 的默认值里全是 `C(0x…)`/`new THREE.Vector3`，调用时才求值）
- 只允许函数声明 + 纯数据常量在顶层。

validate.js 会用一个 THREE 桩在 Node 里真实执行顶层代码来抓这类错误——曾经就是一行顶层 `let curLook=new THREE.Vector3()` 让整个脚本死掉、后续 `const STAGES` 全部处于 TDZ。

## 2. 天空/氛围系统（常驻，跨境渐变）

常驻元素：渐变穹顶（DOME 着色器）、双层星星、月+辉光 Sprite、远山剪影、平行光+环境光。

- 每境用 `sky:()=>SK({...})` 提供参数：`top/hor/bot/fog/fd(雾密度)/star(星亮度)/moon(位置)/ms(月大小)/dirC/dirI/dirP/ambC/ambI`。
- 切境时 `mixSky(k)` 在旧值与新值之间对颜色（`Color.lerpColors`）、向量、数值逐项插值——**情绪曲线靠它**：如豪放境用高星亮月、沉郁境压低星亮度加大雾密度。
- 穹顶/星/月材质必须 `fog:false`，否则距离 300+ 的它们会被雾完全吞掉；远山反而要吃雾（默认 true）来做剪影层次。
- 室内境（无天空）把 `fd` 提到 0.02 左右，远山自动隐没；星星压到 0.1，月光缩到 `ms:0.001` 并移到地下。

## 3. 场景管理（改造重点）

### 3.1 两条平行数组

```js
POEM  = [ {name,jing,segs:[{c:'汉字（含标点）',p:[逐字拼音]}],read,yisi,zhu}, ... ]  // N 句
STAGES= [ {封面}, {境1}, ... {境N} ]                                                // N+1 项
```

> **生命线：`STAGES[i] ↔ POEM[i-1]`，且 `STAGES[i].name === POEM[i-1].name`。**

### 3.2 数量联动清单（增删一境时逐项核对）

| 位置 | 规则 |
|---|---|
| `goto()` 的 `clamp(i,0,N)` | N = 诗句数 |
| 进度点 `#dots` 循环 | `for(i=1;i<=N;i++)` |
| `CN` 中文数字数组 | 长度 ≥ N（第 N 境显示"第拾叁境"之类） |
| 自动游览末境判断 | `if(curIdx===N) showEnding()` |
| 下一境按钮/方向键 | `if(curIdx>=N) showEnding()` |
| 交互境的序号常量 | 如碰杯境：`curIdx===7`（按你的排列改） |
| 特定境的提示 tip | `if(i===7) tip(...)` |
| `audio/NN.mp3` 编号 | NN = 境序号；00=标题，N+1=全诗 |
| 小测评语 `words` 数组 | 长度 = 题数+1，且评语按本诗定制（勿照抄参考实现的"太白"） |

validate.js 会强制前两条与对齐关系，其余靠自查。

### 3.3 每境定义

```js
{ name:'金樽对月', dwell:16, river:0.03, build:bToast, roll:0.035(可选滚镜),
  cam:{f:[x,y,z], t:[...], lf:[...], lt:[...]},   // 到达位→缓慢漂移位 / 注视点同理
  sky:()=>SK({...}) }                              // 必须是工厂！
```

- `build()` 返回 `{group, update(t,dt), click?, onEnter?}`；group 内一切透明材质/光会被 `setFade()` 统一淡入淡出（ShaderMaterial 约定 `uFade` uniform）。
- 切境 = 相机插值运镜 + 新旧 group 交叉淡化 + 天空插值，约 2.6s。
- 镜头内缓慢漂移：30s 内从 cam.f 线性走到 cam.t；鼠标视差 ±2.4 单位。
- 交互境：给返回对象挂 `click()`，在 `renderer.domElement` 的 pointerdown 与空格键里按境界序号调用。

### 3.4 场景构建预算

单境粒子上限数千、水面 110×110 段、InstancedMesh ≤300、**draw call ≤120（硬指标，实测见下）、三角面 ≤12 万**。手机可跑的量级。透明物 `renderOrder`：穹顶 -10 < 星 -9 < 月 -8 < 山 -6 < 山脚近层 -5 < 山(默认0) < 水 1 < 粒子 3 < 雾 Sprite 5。

**draw call 是这个引擎唯一容易失控的数**：一件器物 1-2、一个人物 3-5、一盏灯笼 3-4、一片雾 = sprite 数。2026-09 实测：把 7 境（杯莫停）从 172 压到 123，靠的是「灯串 7→4、盘飧 6→4、小器 6→4、只给一盏灯笼装内焰」。新写场景请在构建后自查：

```js
// 控制台：renderer.info.render.calls / triangles
console.table([{stage:curIdx, calls:renderer.info.render.calls, tris:renderer.info.render.triangles}]);
```

**省 draw call 的三招**：① `mergeGeos()` 顶点色合批（人物=躯干+左右臂 3 个 mesh，器物=1 个）；② `InstancedMesh` 摆一片人/一片杯；③ 远景一律 `makeCrowd`/`simple` 单体，不做完整人物。

### 3.5 雾密度预算 —— 「主体必须可读」（硬性）

2026-09 起因《念奴娇·赤壁怀古》第二境整页泡在同一色相的橙褐雾里、浪花被雾吃光被退回，固化以下预算：

**判据**：主体距离 `d` 处的雾遮蔽率 `1-exp(-(fd·d)²)` 必须 ≤ **0.35**（主角/标志性物件）；远山等背景层 ≤ 0.60。等价地：`fd · d_主体 ≤ 0.65`。

| 赛道 | fd 上限 | 说明 |
|---|---|---|
| 豪放/壮阔（山、海、边塞） | 0.006 | 主体多在 60-120 单位外 |
| 宴饮/市井（室内感） | 0.008 | 主体 15-30 单位，可稍浓 |
| 田园/静夜 | 0.006 | 同上 |
| 室内/梦境（月隐、远山要没） | 0.020-0.025 | 只有此时允许「浓到吃掉远景」 |
| 自定义 ShaderMaterial 的雾 | `uFogK` 0.56-0.74 | 远山着色器按 `uFogK` 保留骨相；`fd≥0.012` 时自动交还全部雾量 → 室内境自动隐没 |

**自检方法（三条，缺一不可）**：
1. 数一遍：`1-exp(-(fd*d)²)`，`d` = 相机到主要景物的距离。超了就降 fd 或把景物拉近（拉近通常更好看）。
2. **拍一张实拍图，把图缩小到 200px 宽再看**：主体还认得出吗？整页是不是只剩一个色相？色相的「明度差」比「色相差」更容易救画面——远景压暗、主体提亮，比换颜色有效。
3. 逐境检查 `fog:false` 名单：穹顶/星/月/日/落霞必须是 `fog:false`；自定义着色器（水/山/地）必须把 `uniforms` 推进 `fogShaders` 由 `applySky()` 每帧同步；**additive 的火焰不推**（吃雾会变灰白）。

> 反例警示：`makeGlow` 的 box 宽度别开到 180+ 还在 maxA 0.7 上叠三层 —— 那是「一团糊满全屏的白光」，不是浪花。粒子盒宽 ≈ 景物宽 ×1.2，maxA 单层 ≤0.6，宁少勿糊。

### 3.6 构图铁律：前景剪影 → 中景主体 → 背景层次

任何一境都必须同时有三层，缺一层就会「平」或「空」：

| 层 | 做法 | 原语 |
|---|---|---|
| 前景（暗、虚、贴相机） | 至少一处，压暗到几乎全黑，占画面下缘/左右缘 | `makeForeground({kind:'岩壁'|'坡石'|'芦苇'|'栏杆'|'树枝'})` |
| 中景（清晰、受光） | 主体 + 案/器/人，有明确的受光面与接触阴影 | `makeTable`/`makeVessel`/`makeFigure`/`makeDish`/`makeBrazier` |
| 背景（渐淡） | 2-3 层山脊（近深远浅）+ 帷帐/亭柱/宫阙 + 远处人影 | `makeRange`/`makeCurtain`/`makePillar`/`makeCrowd` |

**宴席类场面的最低信息量**（否则撑不住诗意）：一场宴 = 案有厚度 + 盘飧 ≥4 + 酒器 ≥6（樽/壶/爵/杯/碗混搭）+ 灯具 ≥4 盏成列 + 前景一层 + 背景一层 + 人物 3-6 位（有姿态，不是柱子）。

## 4. 通用构件（直接从参考实现取用）

### 4.1 2026-09 升级的「造型工坊」（重点，人物/器物/火/山/月已全部重写）

| 函数 | 参数 | 用途 / 关键点 |
|---|---|---|
| `makeFigure(o)` | `pose:'举杯'|'指月'|'倾酒'|'按剑'|'独立'|'坐饮'`、`robe/belt/skin/hair/collar:色`、`beard:bool`、`hat:'发髻'|'幞头'|'无'`、`scale`、`face:朝向弧度`、`rim/rimC:边缘光`、`noProp:bool` | 唐装人物：LatheGeometry 袍身（下摆张开、前后略扁）+ 肩线转折 + 领口/腰带/袖口变色收边 + 两段手臂带肘关节 + 发髻/幞头/胡须。**返回 Group（旧的 `makeFigure(1.1)`、`makeFigure(1.1,0x色)` 仍可用）**，带 `f.update(t,fadeK)` 做呼吸/衣袖微动。一个人物 3 个 mesh（躯干/左臂/右臂），暗背景下靠轮廓+边缘光读出人形 |
| `makeVessel(o)` | `type:'樽'|'壶'|'杯'|'爵'|'盘'|'碗'|'坛'`、`mat:'金'|'陶'|'玉'`、`scale`、`liquid:bool`、`shadow:bool` | 真实器型剖面（口沿/颈/腹/足比例各不同）+ 口沿细高光环 + 三足/流/鋬/盖 + 接触阴影 + 酒面反光。返回 `{g,mesh,wine,update(t,k),setLiquid(y)}`；`makeGoblet(s)`/`makeJar(s)` 是它的兼容壳 |
| `makeFlame(o)` | `h,w,core,outer,planes,embers,spark,light,lightD,wide` | 有形状的焰体（花瓣/水滴形包络 + 湍流抖动 + 焰心/外焰色差 + 偶爆火星 + 可选点光），交叉 2-3 片成体积。返回 `{g,update(t,k),mat}` |
| `makeLantern(scale,o)` | `flame:bool`、`glow`、`flick` | 有骨架的椭圆灯体（8 根竖筋沿同一剖面 + 上下箍）+ 半透纸质感 + 内部暖光 + 外辉。**不再是橙色圆片** |
| `makeRange(o)` | `r,h,layers,peaks,seed,color,atmo,glow,fogK,glowK,arc,a0,y,order` | 多峰折线剖面远山（主峰+副峰+山脊凹口，种子可复现）+ 2-3 层纵深（近深、远混天光）+ 山脊微光 + 层间视差。**任何"等边三角形山"都该换成它**；`arc/a0` 可切出近景山/两岸/浪墙 |
| `makeMoon(o)` | `r,phase(0=满月 0.5=弦月),haze,base,dark,hazeColor`；`set({color,phase,haze,glowColor,scale})` | 临边昏暗 + 极淡月面斑纹 + 圆缺（终止线一族椭圆）+ 三层由紧到松的辉光 + 近地大气染色。取代原先"平涂白圆" |
| `limbTex()` | — | 日/月盘贴图（径向临边昏暗 + 斑纹 + 圆边 alpha）：给**不能换 shader 的旧日轮**用（`map:limbTex()` 即得球感） |
| `makeGround(o)` | `r,c1,c2,y` | 斑驳质感地面（fbm 混色，自定义雾同步）。**别再放一条纯黑 CircleGeometry 当地** |
| `makeForeground(o)` | `kind:'岩壁'|'坡石'|'芦苇'|'栏杆'|'树枝'`、`n,r,w,d,color,seed,sway,rim` | 前景框景：压暗、贴近相机、给画面做"框"与纵深（芦苇/树枝带风摆） |
| `makeTable(o)` | `w,d,h,wood` | 案：有厚度的案面 + 受光细边 + 两端板足 + 横枨 —— 器物不再浮空 |
| `makeDish(o)` | `r,n,plate,foods,sheen` | 盘飧：有厚度的盘 + 几团食物（+可选油光） |
| `makePillar(o)` | `h,r,color,top` | 亭柱：础 + 柱身 +（`top:false` 只留柱身，避免梁枋悬空在画面里） |
| `makeCurtain(o)` | `w,h,color,dark,folds,deep` | 帷帐：几何褶皱 + 上亮下暗顶点色（不是一大片平涂红） |
| `makeBrazier(o)` | `r,fh,fw,light,lightD,embers,spark,color` | 火盆：三足铜盆 + 火焰 + 地面光池（"火"有形状） |
| `makeCrowd(o)` | `n,rect,seed,color,rimC,rim,sMin,sMax` | 远景人影：一个合并几何的 InstancedMesh（1 draw call 摆一片人） |

其余旧构件仍在：| `makeWater({amp,freq,speed,flow,deep,shallow,skyc,moonDir,spec})` | 波浪+菲涅尔+月光高光水面（自定义雾同步） |
| `makeWaterfall({w,h,z})` | fbm 流动瀑布（双面交叉两片） |
| `makeGlow({n,box,pos,color,size,speed,rise,add,maxA})` | 万能粒子：浪花/流萤/金光/落雪。**box 别超过景物宽度**（否则糊成一片） |
| `makeFlow({n,box,color,speed,maxA})` | 定向流动雾流（"愁绪东流"类意象） |
| `makeBurst({n,color,pos})` | 碰杯/溅射火花（`fire()` 触发，起点=最后一次 update 的时间） |
| `makeMist({n,spread,pos,scale,color,op})` | 大团雾 Sprite（`update(t,fadeK)` 已修 fadeK） |
| `makeStars(n,size,op)` / `addLights(g,{c,i,p},{c,i})` | 星层 / 每境自带平行光+环境光（随 group 淡入淡出） |

r128 能力边界：可用 `LatheGeometry / TorusGeometry / TubeGeometry / ExtrudeGeometry / InstancedMesh / Points / ShaderMaterial`；**没有 CapsuleGeometry**（人形肢体 = `limbGeo()` 圆柱收细 + 球关节）；`PointsMaterial` 的 size 在 `sizeAttenuation:false` 时是像素。

### 4.2 合批与边缘光（写新原语时的两把刀）

```js
// 顶点色合批：把 N 个几何体并成 1 个带 color 属性的 BufferGeometry（draw call 直接除 N）
const B=new GeoBag();
B.put(new THREE.LatheGeometry(pts,20), 0xc9a24a);   // 各自带一个色
B.put(legGeo, 0x8a6a3a);
const mesh=B.mesh(vesMat('金'));                    // → 1 个 Mesh
```
```js
// rimHook：给 Phong 注入菲涅尔边缘光（夜景里把剪影"跳"出来）。同一份 onBeforeCompile 源码 → 共用一个着色程序
rimHook(new THREE.MeshPhongMaterial({color:0xffffff,vertexColors:true}), {c:0xffe2a0,i:0.5,p:2.6});
```
注意：**几何体不要全局缓存后共享**（`disposeGroup()` 在切境时会 dispose 掉），每次 build 重建即可（几百个小几何的合并是微秒级）；**材质必须每次 build 新建**，否则两个境共用材质对象会让交叉淡化的 opacity 互相打架。

## 5. 朗读管线（v2）

```
aiSpeak('07.mp3', read文本)
  ├─ 1) 检测到神经语音（Edge"在线自然语音"Yunjian/Yunxi/Xiaoxiao…）
  │      → speakLive() 逐句现场朗诵：按 。！？； 切句、句间停顿 420ms、rate 0.78（真人朗诵节奏）
  ├─ 2) 无神经语音 → new Audio('audio/07.mp3')   ← 内置配音（gen-voice.js 生成；配 Azure 密钥可得诗朗诵级音色）
  └─ 3) 播放失败 → speak() 普通系统语音整段兜底
```

- 令牌防串音：`speakSeq` 在每次 `stopSpeak()` 自增，所有异步回调先比对令牌再继续——切境/重播时旧朗读立即静默。
- 首句播放失败（如 Edge 离线）自动降级到内置 MP3。
- 进入新境 1.6s 后自动朗读（等逐字动画播完）；定时器同样被 stopSpeak 清除。
- 自动朗读/自动游览默认开（教学展示），都可一键关。

## 6. 诗句 UI（竖排 + 注音）

- 容器 `writing-mode:vertical-rl`，**块级流**排句（`.seg{margin-block-end:1.3em}`）——不要用 flex row，vertical-rl 下 flex 主轴是垂直的，会叠成一列。
- 每字 `<ruby class="zi"><span>君</span><rt>jūn</rt></ruby>`，标点是普通 span 不加 rt；`.zi` 逐字入场动画用 `animation-delay` 按 `ci*0.13s` 递增。
- rt 字号 0.32em；容器 `padding-right:2.6em` 给注音留位。
- 汉字数必须等于拼音数组长度（标点不计），validate.js 强制。

## 6.5 实拍验证（唯一能证"画面对不对"的手段）

`validate.js` 与 `smoke.test.js` 都只跑 THREE 桩，**只能证明"不报错"，证不了"好不好看"**。
整页泡在雾里、主体读不出来、物件浮空、山是三角形……这类问题只有真渲染 + 真截图才看得见。

```bash
cd <项目>/_pipeline && python shots.py ../<slug> --stages 1,2,7 --out <输出目录> --hold 2.5
```
每首输出到 `<输出目录>/<slug>/stageN.png`，交付前**必须自己 Read 这些 PNG 逐张检查**。

### 血泪教训：绝不要为了跳境去强写 `state='stage'`
引擎的切境是异步过渡：`goto(i)` 置 `state='transition'`，逐帧把新境 `uFade` 从 0 推到 1、
旧境从 1 推到 0，走完才置 `state='stage'` 并把 `curStageObj/curDef` 换成新境。

若在过渡进行中硬写 `state='stage'`，过渡被**永久打断**：旧境停在 `uFade≈1`、新境停在 `uFade≈0`，
`curStageObj/curDef` 再也不更新。此时截图会看到**旧境残留**，新境内容全不可见——
而 `userData.fadeK` 与材质 `uFade` 会呈现"组说 0.995、材质说 0.005"的矛盾值。

这个假象曾导致两个真实损失：① 有人据"第一境瀑布看不见"的截图连改四轮，
把好端端的瀑布堆成 820 粒白色棉团（事后已回退为细密水丝）；② 有人据"小径被画成放射光束"
误判了一页浅色赛道页面。**根因都在工具，不在页面。**

**正确姿势**：点 `#enterBtn` 关封面 → 置 `autoMode=false`（否则等过渡的几秒会自动切到下一境）
→ 轮询等 `state==='stage'` → 才 `goto(目标境)` → 再轮询等 `state==='stage' && curIdx===目标境` → 截图。
`shots.py` 已按此实现。**注意这个坑只影响第一境**：`goto(1)` 会因 `i===curIdx` 直接返回，
于是第一境永远等不到那次被中断的过渡。所以**第一境的截图历史上一律不可信**，必须用修好的工具重拍。

## 7. 音频生成（scripts/gen-voice.js）

- 从 index.html 提取全部 `read:'…'`，按 `{00:标题, 01..N:各句, N+1:全诗}` 生成。
**首选 `scripts/gen-voice-edge.py`（Python）**：Edge 神经语音，与 Azure 付费"诗朗诵"同套音色，免费无密钥，
按赛道自动选声（云健/云希/晓晓）。多音字优先读诗目录下 `tts.json` 的 `sub`，其次自动从
`gen-voice.local.js` 的 SUB 表迁移，最后才用内置高置信兜底表。需 `edge-tts` ≥7.2.8。

`gen-voice.js`（Node，百度 TTS 兜底）仅在 edge-tts 不可用时使用，音色明显不如神经语音。
