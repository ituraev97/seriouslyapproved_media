// usage: node thumb.mjs <episode_dir>   reads <ep>/thumb.json {"variants":[{"id":"A","hook":"THIS IS REAL","words":"[Kissing]|shield","num":"US 5,727,565","fig":"thumb_fig.png","stamp":"U.S. 1998"}, …]}
// writes <ep>/thumb_<id>.png (1280x720). Bottom-right stays empty (duration badge).
import { chromium } from "playwright"; import fs from "fs"; import path from "path"; import url from "url";
const here = path.dirname(url.fileURLToPath(import.meta.url)); const ep = path.resolve(process.argv[2]);
const cfg = JSON.parse(fs.readFileSync(`${ep}/thumb.json`));
const exe = ["/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"].find(p => fs.existsSync(p));
const b = await chromium.launch(exe ? { executablePath: exe } : {}); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
await pg.goto("file://" + path.join(here, "thumb.html")); await pg.evaluate(() => document.fonts.ready);
for (const v of cfg.variants) { v.figsrc = "data:image/png;base64," + fs.readFileSync(path.join(ep, v.fig)).toString("base64");
  await pg.evaluate(v => draw(v), v); await pg.waitForTimeout(150); await pg.screenshot({ path: `${ep}/thumb_${v.id}.png` }); console.log("thumb", v.id); }
await b.close();
