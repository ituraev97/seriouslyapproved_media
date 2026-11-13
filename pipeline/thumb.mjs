// usage: node thumb.mjs <episode_dir>   (template: thumb2.html "loud" v2 by default; variants with "tpl":"v1" use thumb.html)
//   reads <ep>/thumb.json {"variants":[{"id":"A","hook":"THIS IS REAL","words":"[Kissing]|shield","num":"US 5,727,565","fig":"thumb_fig.png","stamp":"U.S. 1998"}, …]}
// writes <ep>/thumb_<id>.png (1280x720). Bottom-right stays empty (duration badge).
import { chromium } from "playwright"; import { execFileSync } from "child_process"; import fs from "fs"; import path from "path"; import url from "url";
const here = path.dirname(url.fileURLToPath(import.meta.url)); const ep = path.resolve(process.argv[2]);
const cfgFile = process.argv[3] || (fs.existsSync(`${ep}/thumb2.json`) ? "thumb2.json" : "thumb.json");
const cfg = JSON.parse(fs.readFileSync(`${ep}/${cfgFile}`));
const exe = ["/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"].find(p => fs.existsSync(p));
const b = await chromium.launch(exe ? { executablePath: exe } : {}); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
let curTpl = null;
for (const v of cfg.variants) { const tpl = v.tpl === "v1" ? "thumb.html" : "thumb2.html";
  if (tpl !== curTpl) { await pg.goto("file://" + path.join(here, tpl)); await pg.evaluate(() => document.fonts.ready); await pg.evaluate(() => document.fonts.load("150px Anton")); curTpl = tpl; } let figp = path.join(ep, v.fig);
  if (tpl === "thumb2.html" && !v.card && v.sticker !== false) { const sp = figp.replace(/\.png$/, "_sticker.png"); execFileSync("python3", [path.join(here, "sticker.py"), figp, sp]); figp = sp; }
  v.figsrc = "data:image/png;base64," + fs.readFileSync(figp).toString("base64");
  await pg.evaluate(v => draw(v), v); await pg.waitForTimeout(150); await pg.screenshot({ path: `${ep}/thumb_${v.id}.png` }); console.log("thumb", v.id); }
await b.close();
