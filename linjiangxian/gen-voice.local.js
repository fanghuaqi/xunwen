/*
 * gen-voice.local.js —— 为「循文入境」《临江仙》（明·杨慎）生成 AI 朗读 MP3。
 * 本文件是 xunwen-rujing/scripts/gen-voice.js 的**本词专用副本**（只改 SUB 表，引擎逻辑未动）。
 * 引擎: 百度翻译 TTS 开放接口（免密钥，国内直连，16kHz MP3）。
 * 用法: node gen-voice.local.js index.html "临江仙" "明，杨慎"
 * 注: 若需更高级的"诗朗诵"级神经语音，可设 TTS_AZURE_KEY 后重跑，
 *     或在 Edge 浏览器中打开网页并删除 audio/ 目录——页面会自动优先选用 Edge 的"在线自然语音"。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const https = require('https');

const SPD = 4; // 语速 1-9，4 略慢，适合古诗

/* ============================================================
 * 按诗改编：多音字替换表（只影响音频读音，不改页面文字）
 * —— 临江仙（杨慎）专用表：逐句核过读音，只列易读错的 ——
 *   滚滚长江东逝水：长江 cháng（非 zhǎng）｜浪花淘尽英雄：尽 jìn（非 jǐn）
 *   是非成败转头空：转 zhuǎn（非 zhuàn）、空 kōng（非 kòng）
 *   青山依旧在，几度夕阳红：几 jǐ（非 jī）→ 见表
 *   白发渔樵江渚上：发 fà（非 fā）→ 见表；渚 zhǔ（单一读音）
 *   惯看秋月春风：看 kàn（非 kān）｜一壶浊酒喜相逢：浊 zhuó（单一读音）
 *   古今多少事，都付笑谈中：都 dōu（非 dū）、多少 duō shǎo
 * ============================================================ */
const SUB = [
  ['白发','白髮'],   // 白发渔樵：发 fà（头发），避免读成 fā（发现）
  ['几度','己度'],   // 几度夕阳红：几 jǐ（几多/多少），避免读成 jī（几乎）
];

/* ---------- 读取目标页面并提取全部 read 句 ---------- */
const target = path.resolve(process.argv[2] || 'index.html');
const html = fs.readFileSync(target, 'utf8');
const OUT = path.join(path.dirname(target), 'audio');
const reads = [...html.matchAll(/read:'([^']+)'/g)].map(m => m[1]);
if (!reads.length) { console.error('未从 ' + target + ' 解析到任何 read:"…" 句'); process.exit(1); }
console.log('解析到 ' + reads.length + ' 句，输出目录: ' + OUT);

/* ---------- 可选升级：Azure 神经语音（真人"诗朗诵"级） ----------
 * 设置环境变量后自动启用，未设置则用百度接口兜底：
 *   Windows CMD : set TTS_AZURE_KEY=你的密钥
 *   PowerShell  : $env:TTS_AZURE_KEY="你的密钥"
 * 可选: TTS_AZURE_REGION (默认 eastasia) 、 TTS_VOICE (默认 zh-CN-YunjianNeural)
 * 免费密钥: portal.azure.com 创建"语音服务"免费层 (F0, 每月 50 万字符)
 * ------------------------------------------------------------- */
const AZ_KEY = process.env.TTS_AZURE_KEY;
const AZ_REGION = process.env.TTS_AZURE_REGION || 'eastasia';
const AZ_VOICE = process.env.TTS_VOICE || 'zh-CN-YunjianNeural';
console.log('TTS 引擎: ' + (AZ_KEY ? 'Azure 神经语音 · ' + AZ_VOICE + '（诗朗诵风格）' : '百度翻译 TTS（免密钥兜底；配置 TTS_AZURE_KEY 可升级诗朗诵级音色）'));
const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function azureOne(text) {
  return new Promise((resolve, reject) => {
    const ssml = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis'"
      + " xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='zh-CN'>"
      + "<voice name='" + AZ_VOICE + "'><mstts:express-as style='poetry-reading'>"
      + "<prosody rate='-12%'>" + esc(text) + '</prosody></mstts:express-as></voice></speak>';
    const req = https.request({
      hostname: AZ_REGION + '.tts.speech.microsoft.com',
      path: '/cognitiveservices/v1', method: 'POST',
      headers: {
        'Ocp-Apim-Subscription-Key': AZ_KEY,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'audio-24khz-48kbitrate-mono-mp3',
        'User-Agent': 'xunwen-rujing',
      },
    }, res => {
      const chunks = [];
      res.on('data', d => chunks.push(d));
      res.on('end', () => {
        const b = Buffer.concat(chunks);
        if (res.statusCode !== 200) return reject(new Error('Azure HTTP ' + res.statusCode + ': ' + b.toString('utf8').slice(0, 120)));
        if (b.length < 800 || !(b[0] === 0xFF || b.slice(0, 3).toString('ascii') === 'ID3')) return reject(new Error('返回内容不是音频'));
        resolve(b);
      });
    });
    req.on('error', reject);
    req.setTimeout(20000, () => req.destroy(new Error('timeout')));
    req.write(ssml); req.end();
  });
}
const sub = t => { let s = t; for (const [a, b] of SUB) s = s.split(a).join(b); return s; };

/* ---------- 长文本按句切分（接口对单次文本长度有限制） ---------- */
function splitText(t, max = 160) {
  if (t.length <= max) return [t];
  const parts = [];
  let cur = '';
  for (const ch of t) {
    cur += ch;
    if (cur.length >= max && /[，。！？；、]/.test(ch)) { parts.push(cur); cur = ''; }
  }
  if (cur) parts.push(cur);
  return parts;
}

/* ---------- 调用百度 TTS 接口合成一段（免密钥兜底） ---------- */
function baiduOne(text) {
  return new Promise((resolve, reject) => {
    const url = 'https://fanyi.baidu.com/gettts?lan=zh&spd=' + SPD + '&source=web&text=' + encodeURIComponent(text);
    const req = https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Referer': 'https://fanyi.baidu.com/' } }, res => {
      if (res.statusCode !== 200) { res.resume(); return reject(new Error('HTTP ' + res.statusCode)); }
      const chunks = [];
      res.on('data', d => chunks.push(d));
      res.on('end', () => {
        const b = Buffer.concat(chunks);
        // 校验是 MP3（0xFFF 帧头或 ID3）
        if (b.length < 800 || !(b[0] === 0xFF || b.slice(0, 3).toString('ascii') === 'ID3')) {
          return reject(new Error('返回内容不是音频'));
        }
        resolve(b);
      });
    });
    req.on('error', reject);
    req.setTimeout(15000, () => req.destroy(new Error('timeout')));
  });
}

const ttsOne = t => (AZ_KEY ? azureOne(t) : baiduOne(t));

async function synth(text, outFile) {
  const parts = splitText(sub(text));
  const bufs = [];
  for (const p of parts) {
    let got = null, lastErr = null;
    for (let a = 1; a <= 4 && !got; a++) {
      try { got = await ttsOne(p); }
      catch (e) { lastErr = e; await new Promise(r => setTimeout(r, 1000 * a)); }
    }
    if (!got) throw lastErr || new Error('synth failed');
    bufs.push(got);
  }
  fs.writeFileSync(outFile, Buffer.concat(bufs));
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  // 诗题/作者引言：可用第 2、3 个参数指定；否则从 <title> 智能提取（剔除"循文入境"、技术后缀等）
  let poemTitle = process.argv[3];
  const introArg = process.argv[4];
  if (!poemTitle) {
    const t = (html.match(/<title>([^<]*)<\/title>/) || ['', ''])[1];
    const segs = t.split(/[·|｜|]/).map(s => s.trim())
      .filter(s => s && !/three\.js|沉浸|诗词课|网页|interactive/i.test(s));
    poemTitle = segs.length ? segs[segs.length - 1] : '古诗';
  }
  // 00: 标题   01..N: 各境   N+1: 全诗（编号按诗句数动态生成，勿写死）
  const jobs = [
    { f: '00.mp3', t: introArg ? `${poemTitle}。${introArg}。` : `${poemTitle}。` },
    ...reads.map((t, i) => ({ f: String(i + 1).padStart(2, '0') + '.mp3', t })),
    { f: String(reads.length + 1).padStart(2, '0') + '.mp3', t: reads.join('') },
  ];
  let fail = 0;
  for (const j of jobs) {
    const out = path.join(OUT, j.f);
    try {
      await synth(j.t, out);
      const kb = (fs.statSync(out).size / 1024).toFixed(1);
      console.log(j.f + '  ' + kb + ' KB  ← ' + j.t.slice(0, 18) + (j.t.length > 18 ? '…' : ''));
      await sleep(700);
    } catch (e) {
      fail++;
      console.error('✗ ' + j.f + ' 失败: ' + e.message);
    }
  }
  console.log(fail === 0 ? '全部生成完成 ✓' : '完成，但有 ' + fail + ' 个文件失败');
  process.exit(fail === 0 ? 0 : 2);
})();
