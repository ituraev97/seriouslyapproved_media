import { chromium } from "playwright"; import path from "path";
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell" });
const pg = await b.newPage({ viewport: { width: 2700, height: 1600 } });
await pg.goto("file://" + path.resolve("brand.html")); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(400);
for (const [id, out, omit] of [["logo","logo_paper.png"],["logo-dark","logo_blueprint.png"],["avatar","avatar_800.png"],["banner","banner_2560x1440.png"],["wm","watermark_300.png",true],["thumbA","thumb_A_example.png"],["thumbC","thumb_C_example.png"]]) {
  await pg.locator("#"+id).screenshot({ path: out, omitBackground: !!omit }); }
await b.close(); console.log("ok");
