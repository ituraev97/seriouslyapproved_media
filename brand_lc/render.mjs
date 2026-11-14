// node brand_lc/render.mjs  -> brand_lc/out/*.png
import { chromium } from "playwright"; import path from "path"; import fs from "fs"; import { fileURLToPath } from "url";
const here = path.dirname(fileURLToPath(import.meta.url)); const out = path.join(here, "out"); fs.mkdirSync(out, { recursive: true });
const exe = ["/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"].find(p => fs.existsSync(p));
const b = await chromium.launch(exe ? { executablePath: exe } : {}); const pg = await b.newPage({ viewport: { width: 2600, height: 1500 } });
await pg.goto("file://" + path.join(here, "brand.html"));
for (const [k, transparent] of [["avatar", false], ["logo", true], ["logo_dark", true], ["watermark", true], ["banner", false]]) {
  await pg.evaluate(k => window.render(k), k); await pg.waitForTimeout(150);
  const el = await pg.$("#root > .art");
  await el.screenshot({ path: path.join(out, `${k}.png`), omitBackground: transparent });
  console.log(k);
}
await b.close();
