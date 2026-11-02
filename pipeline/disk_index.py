#!/usr/bin/env python3
"""Index of every patent scan on the archive.org USPTO disks (~2.3 million utility patents of ~6 million; coverage is patchy).
usage: disk_index.py build            -> /home/claude/cache/idx/<disk>.txt (file lists, ~2 min, 8 threads) + all_utility.txt
       disk_index.py has 5443036 ...   -> YES / - per number (check candidates BEFORE researching them; most famous weird patents are missing)
patent.py uses the idx files automatically when they exist."""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
C = os.environ.get("IDX_CACHE", "/home/claude/cache"); IDX = f"{C}/idx"; ALL = f"{C}/all_utility.txt"
here = os.path.dirname(os.path.abspath(__file__))
def one(d):
    ident = d[2]; op = f"{IDX}/{ident}.txt"
    if os.path.exists(op): return
    for k in range(4):
        try:
            with urllib.request.urlopen(f"https://archive.org/metadata/{ident}", timeout=180) as r: data = json.loads(r.read()); break
        except Exception: time.sleep(5 * (k + 1))
    else: print("FAIL", ident); return
    open(op, "w").write("\n".join(f["name"] for f in data.get("files", []) if f["name"].endswith(".tif"))); print(ident, flush=True)
if sys.argv[1] == "build":
    os.makedirs(IDX, exist_ok=True); disks = json.load(open(os.path.join(here, "..", "disks.json")))
    with ThreadPoolExecutor(8) as ex: list(ex.map(one, disks))
    nums = set()
    for f in os.listdir(IDX):
        for line in open(f"{IDX}/{f}"):
            b = line.strip().rsplit("/", 1)[-1][:-4]
            if b.isdigit(): nums.add(int(b))
    open(ALL, "w").write("\n".join(map(str, sorted(nums)))); print(len(nums), "utility patents indexed")
else:
    s = set(int(x) for x in open(ALL))
    for a in sys.argv[2:]: n = int(a.replace(",", "")); print(n, "YES" if n in s else "-")
