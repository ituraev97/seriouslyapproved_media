#!/usr/bin/env python3
"""Fetch a U.S. patent's full TIFF from the archive.org USPTO disks, split pages, OCR them.
usage: patent.py <number> <out_dir>      e.g. patent.py 5727565 episodes/001-x/pat
-> <out_dir>/<number>/<number>.tif, p0.png…, p0.txt…, sheet.jpg (all pages, small, for choosing figures)
Disks: ../disks.json = [[from_int, to_str, identifier], …]. archive.org sometimes answers 500: retried."""
import sys, os, json, time, subprocess, urllib.request
from PIL import Image
N = int(str(sys.argv[1]).replace(",", "").replace("US", "").strip()); out = os.path.join(sys.argv[2], str(N)); os.makedirs(out, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__)); disks = json.load(open(os.path.join(here, "..", "disks.json")))
cache = os.environ.get("META_CACHE", "/home/claude/cache/archive_meta"); os.makedirs(cache, exist_ok=True)
def get(url, tries=4):
    for k in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r: data = r.read()
            if len(data) > 300 or not data.startswith(b"<html"): return data
        except Exception as e: err = e
        time.sleep(4 * (k + 1))
    raise SystemExit(f"failed: {url}")
cands = [d for d in disks if d[0] <= N and (not d[1].isdigit() or int(d[1]) >= N)]
cands.sort(key=lambda d: (not d[1].isdigit(), (int(d[1]) - d[0]) if d[1].isdigit() else 0))
name = f"{N:08d}.tif"; hit = None
for _, _, ident in cands:
    cp = os.path.join(cache, ident + ".json")
    if not os.path.exists(cp): open(cp, "wb").write(get(f"https://archive.org/metadata/{ident}"))
    files = [f["name"] for f in json.load(open(cp)).get("files", [])]
    m = [f for f in files if f.endswith("/" + name)]
    if m: hit = (ident, m[0]); break
if not hit: raise SystemExit(f"US {N} not on any archive.org disk (checked {len(cands)})")
tif = os.path.join(out, f"{N}.tif")
if not os.path.exists(tif) or os.path.getsize(tif) < 5000:
    open(tif, "wb").write(get(f"https://archive.org/download/{hit[0]}/{hit[1]}"))
im = Image.open(tif); pages = []
try:
    while True:
        im.seek(len(pages)); p = os.path.join(out, f"p{len(pages)}.png"); im.convert("L").save(p); pages.append(p)
except EOFError: pass
for p in pages:
    if not os.path.exists(p[:-4] + ".txt"): subprocess.run(["tesseract", p, p[:-4]], capture_output=True)
th = [Image.open(p).resize((Image.open(p).width // 5, Image.open(p).height // 5)) for p in pages]
sheet = Image.new("L", (sum(t.width for t in th) + 10 * len(th), max(t.height for t in th)), 255); x = 0
for t in th: sheet.paste(t, (x, 0)); x += t.width + 10
sheet.save(os.path.join(out, "sheet.jpg"))
json.dump(dict(number=N, archive=hit[0], path=hit[1], pages=len(pages)), open(os.path.join(out, "source.json"), "w"), indent=1)
print(f"US {N}: {len(pages)} pages from {hit[0]} -> {out}")
