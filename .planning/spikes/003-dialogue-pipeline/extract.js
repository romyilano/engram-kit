#!/usr/bin/env node
/* Spike 003 — dialogue pipeline.
 * Reads the existing manga lettering blocks in documentation/manga/<book>/page-NN.md
 * and emits a structured VN script, proving the dialogue is already authored in-repo.
 *
 *   node extract.js
 *
 * Outputs:
 *   script.json  — full structured script for BOTH books (the proof artifact)
 *   script.js    — window.VN_SCRIPT = <ALMA scenes>  (loaded by play.html, no fetch/CORS)
 */
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '../../..');
const BOOKS = [
  { id: 'alma',      dir: 'documentation/manga/alma',      panel: n => `alma_page${n}.png`,     panelDir: 'docs/manga/alma/panels' },
  { id: 'ama-bench', dir: 'documentation/manga/ama-bench', panel: n => `amabench_page${n}.png`, panelDir: 'docs/manga/ama-bench/panels' },
];

// "Sensei" -> "sensei", "Meta Agent" -> "metaagent", "The Examiner"/"Examiner" -> "examiner"
function speakerKey(label) {
  const l = label.trim().toLowerCase();
  if (l.includes('caption')) return 'narrator';
  if (l.includes('examiner')) return 'examiner';
  if (l.includes('meta agent')) return 'metaagent';
  if (l.includes('engy')) return 'engy';
  if (l.includes('sensei')) return 'sensei';
  return l.replace(/[^a-z]/g, '') || 'narrator';
}

// *word* -> <em>word</em>; strip a wrapping pair of quotes; trim.
function cleanText(raw) {
  let t = raw.trim();
  if ((t.startsWith('"') && t.endsWith('"')) || (t.startsWith('“') && t.endsWith('”'))) t = t.slice(1, -1);
  else if (t.startsWith('"') || t.startsWith('“')) t = t.slice(1); // unterminated (multi-line caption) — keep what we have
  t = t.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  return t.trim();
}

// Parse one "- Panel N — Speaker: text" lettering line. Returns null if not a dialogue line.
function parseLetteringLine(line) {
  // must start with "- Panel <n>" ; dialogue lines are bulleted, panel *descriptions* are not.
  const m = line.match(/^\s*-\s*Panel\s+(\d+)\s*[—–-]\s*(.+)$/);
  if (!m) return null;
  const panel = parseInt(m[1], 10);
  let rest = m[2].trim();

  // caption form: "(caption) "text"" — no colon before the text
  const cap = rest.match(/^\(caption\)\s*(.*)$/i);
  if (cap) return { panel, speaker: 'narrator', label: '(caption)', text: cleanText(cap[1]) };

  // named-speaker form: "Speaker: "text"" — split on the FIRST ": "
  const idx = rest.indexOf(': ');
  if (idx === -1) return null;
  const label = rest.slice(0, idx).trim();
  const text = cleanText(rest.slice(idx + 2));
  return { panel, speaker: speakerKey(label), label, text };
}

function pageNum(file) {
  const m = file.match(/page-(\d+)\.md$/);
  return m ? m[1] : null;
}

const full = { generatedFrom: 'documentation/manga/**/page-NN.md', books: {} };
const summary = [];

for (const book of BOOKS) {
  const dir = path.join(REPO, book.dir);
  const files = fs.readdirSync(dir).filter(f => /^page-\d+\.md$/.test(f)).sort();
  const scenes = [];
  for (const file of files) {
    const nn = pageNum(file);
    const md = fs.readFileSync(path.join(dir, file), 'utf8');
    const lines = md.split('\n').map(parseLetteringLine).filter(Boolean);
    const panelPath = `${book.panelDir}/${book.panel(nn)}`; // clean repo-relative path
    scenes.push({ page: nn, panel: book.panel(nn), panelPath, lines });
    summary.push({ book: book.id, page: nn, lines: lines.length,
      speakers: [...new Set(lines.map(l => l.speaker))].join(',') });
  }
  full.books[book.id] = scenes;
}

// 1) full proof artifact
fs.writeFileSync(path.join(__dirname, 'script.json'), JSON.stringify(full, null, 2));

// 2) flat ALMA script for the player (window global -> no fetch, opens via file://)
const almaFlat = [];
for (const sc of full.books['alma']) {
  for (const ln of sc.lines) almaFlat.push({ bg: `../../../docs/manga/alma/panels/${sc.panel}`, page: sc.page, ...ln });
}
fs.writeFileSync(path.join(__dirname, 'script.js'), 'window.VN_SCRIPT = ' + JSON.stringify(almaFlat, null, 2) + ';\n');

// 3) report
const totalLines = summary.reduce((a, s) => a + s.lines, 0);
console.log('\nExtracted VN dialogue from existing manga lettering blocks\n');
console.log('book        page  lines  speakers');
console.log('----------  ----  -----  --------------------------');
for (const s of summary) console.log(`${s.book.padEnd(10)}  ${s.page.padEnd(4)}  ${String(s.lines).padEnd(5)}  ${s.speakers}`);
console.log('----------  ----  -----  --------------------------');
console.log(`${'TOTAL'.padEnd(10)}  ${String(summary.length).padEnd(4)}  ${String(totalLines).padEnd(5)}  across ${BOOKS.length} books`);
console.log(`\nWrote script.json (${summary.length} pages, ${totalLines} lines) and script.js (ALMA, ${almaFlat.length} lines).`);
console.log('Open play.html to play the auto-extracted ALMA script.\n');
