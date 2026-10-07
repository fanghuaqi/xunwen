# 批次5：新创作 20 首（no.134-153）

管线（每首同短歌行批次）：配置(_dgx/) → build.py → validate → derive_smoke → smoke → tts.json → gen-voice-edge → README → accept → mark-done → update-gallery（批尾）→ style-audit（批尾）→ 实拍抽检关键境

约定：yanye 变体底色必须 #05070d（style-audit 硬校验）；--gold=accent；非 yanye bg=赛道 bg；
新 smoke 一律从 wanghaichao/smoke.test.js 派生（自带 vendor three 回退）。

- [x] 134 行路难·其一（xinglu-nan）ACCEPT+实拍4轮（帆改梯形+帆骨）
- [x] 135 次北固山下（cibeigushan）ACCEPT（3轮：scale方法/背景层/几何rotation误用）
- [x] 136 渡荆门送别（dujingmen）ACCEPT（蜃楼shader+月影光晕3轮）
- [x] 137 饮酒·其五（yinjiu）ACCEPT（hex大写+灯基线2轮）
- [x] 138 归园田居·其三（guiyuantianju）ACCEPT（补原语自包含1轮）
- [x] 139 望江南·梳洗罢（wangjiangnan）ACCEPT
- [x] 140 逢入京使（fengrujingshi）ACCEPT
- [x] 141 夜上受降城闻笛（yeshouxiangwen）ACCEPT（{g}约定/背景层2轮）
- [x] 142 送友人（songyouren）ACCEPT
- [x] 143 月夜忆舍弟（yueye-yishe）ACCEPT（Geometry当Mesh用+sprite基线3轮）
- [x] 144 卖炭翁（maitanweng）ACCEPT（一次过）
- [x] 145 石壕吏（shihaoli）ACCEPT（helm.scale+光晕基线2轮）
- [x] 146 茅屋为秋风所破歌（maowu）ACCEPT
- [x] 147 渔家傲·秋思（yujiaao-qiusi）ACCEPT
- [x] 148 破阵子·为陈同甫赋壮词以寄之（pozhenzi）ACCEPT（补原语自包含2轮）
- [x] 149 定风波·莫听穿林打叶声（dingfengbo）ACCEPT（修Geometry位移1轮）
- [x] 150 江城子·密州出猎（jiangchengzi）ACCEPT（修灯基座1轮）
- [x] 151 过零丁洋（guolingdingyang）ACCEPT（Geometry修位移+初值基座2轮）
- [x] 152 无题·相见时难别亦难（wuti）ACCEPT（修letter基座1轮）
- [x] 153 渔家傲·天接云涛连晓雾（yujiaao-tianjie）ACCEPT（GeoBag建楼+自包含小舟+fadeK基座2轮）
