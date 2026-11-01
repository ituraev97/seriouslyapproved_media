// usage: node render.mjs <episode_dir> [fps=30] [t0 t1 step  -> stills only]
// Renders frame.html for every frame of <ep>/timeline.json. Figures: <ep>/fig/*.svg (keys = file names).
import { chromium } from "playwright"; import fs from "fs"; import path from "path"; import url from "url";
const here = path.dirname(url.fileURLToPath(import.meta.url));
const ep = path.resolve(process.argv[2]); const FPS = +(process.argv[3] || 30);
const tl = JSON.parse(fs.readFileSync(`${ep}/timeline.json`)); const figs = {};
if (fs.existsSync(`${ep}/fig`)) for (const f of fs.readdirSync(`${ep}/fig`)) if (f.endsWith(".svg")) figs[f.replace(".svg", "")] = fs.readFileSync(`${ep}/fig/${f}`, "utf8");
const exe = ["/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"].find(p => fs.existsSync(p));
const b = await chromium.launch(exe ? { executablePath: exe } : {});
const pg = await b.newPage({ viewport: { width: tl.W, height: tl.H } });
const errs = []; pg.on("pageerror", e => errs.push(String(e)));
await pg.goto("file://" + path.join(here, "frame.html")); await pg.evaluate(([t, f]) => init(t, f), [tl, figs]);
const still = process.argv[4] !== undefined; const out = still ? `${ep}/stills` : `${ep}/frames`; fs.mkdirSync(out, { recursive: true });
const times = []; if (still) for (let t = +process.argv[4]; t < Math.min(+process.argv[5], tl.T); t += +process.argv[6]) times.push(t); else for (let i = 0; i < Math.round(tl.T * FPS); i++) times.push(i / FPS);
let i = 0; for (const t of times) { await pg.evaluate((t) => render(t), t);
  if (errs.length) { console.error("page error at t=" + t + ": " + errs[0]); process.exit(1); }
  await pg.screenshot({ path: `${out}/${still ? "s" + t.toFixed(1) : "f" + String(i).padStart(5, "0")}.jpg`, type: "jpeg", quality: 92 }); i++; }
await b.close(); console.log("frames", i);
