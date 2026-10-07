#!/usr/bin/env node
/* mark-done.js —— 验收通过后登记 manifest
 * 用法: node mark-done.js <slug> [slug...]
 * 先跑 accept.js，只有 exit 0 才写 done。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const DIR = __dirname;
const file = path.join(DIR, 'manifest.json');
const m = JSON.parse(fs.readFileSync(file, 'utf8'));
const today = new Date().toISOString().slice(0, 10);

let bad = 0;
for (const slug of process.argv.slice(2)) {
  let pass = false, out = '';
  try {
    out = execFileSync('node', [path.join(DIR, 'accept.js'), slug], { stdio: 'pipe' }).toString();
    pass = true;
  } catch (e) {
    out = String(e.stdout || '') + String(e.stderr || '');
  }
  if (!pass) {
    bad++;
    console.log(`✗ ${slug} 验收未通过：\n${out.trim().split('\n').slice(-12).join('\n')}`);
    continue;
  }
  const cur = m[slug] || { attempts: 1 };
  m[slug] = { ...cur, status: 'done', accepted: today };
  console.log(`✓ ${slug} done (${out.trim().split('\n')[0]})`);
}
fs.writeFileSync(file, JSON.stringify(m, null, 1));
const cnt = {};
for (const v of Object.values(m)) cnt[v.status] = (cnt[v.status] || 0) + 1;
console.log('manifest:', JSON.stringify(cnt));
process.exit(bad ? 1 : 0);
