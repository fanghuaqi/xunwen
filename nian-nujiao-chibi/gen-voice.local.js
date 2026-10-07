/*
 * gen-voice.js —— 为「循文入境」《念奴娇·赤壁怀古》生成 AI 朗读 MP3（本诗专用副本）。
 * 引擎: 百度翻译 TTS 开放接口（免密钥，国内直连，16kHz MP3）。
 * 用法: node gen-voice.js [index.html 路径]   （默认 ./index.html，音频输出到同目录 audio/）
 * 注: 若需更高级的"诗朗诵"级神经语音，可在 Edge 浏览器中打开网页并删除 audio/
 *     目录——页面会自动回退并优先选用 Edge 的"在线自然语音"。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const https = require('https');

const SPD = 4; // 语速 1-9，4 略慢，适合古诗

/* ============================================================
 * 按诗改编：多音字替换表（只影响音频读音，不改页面文字）
 * 例：将进酒读 qiāng → ['将进酒','枪进酒']
 * 换一首诗时务必逐句核对读音后重写此表！
 * —— 念奴娇·赤壁怀古（苏轼）专用表 ——
 * ============================================================ */
const SUB = [
  // —— 念奴娇·赤壁怀古 多音字表（左=页面原文，右=同音字，只改读音不改页面文字）——
  ['纶巾','官巾'],   // 羽扇纶巾：纶 guān（青丝头巾），不读 lún
  ['樯橹','墙鲁'],   // 樯橹：樯 qiáng（桅杆）、橹 lǔ（船桨）
  ['华发','华髮'],   // 早生华发：发 fà（白发），不读 fā
  ['还酹','环酹'],   // 一尊还酹江月：还 huán（回转），不读 hái
  ['嫁了','嫁瞭'],   // 小乔初嫁了：了 liǎo（完成语气），不读 le
  ['卷起','捲起'],   // 卷起千堆雪：卷 juǎn（翻卷），不读 juàn
  ['应笑','英笑'],   // 多情应笑我：应 yīng（该当），不读 yìng
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
