#!/usr/bin/env python3
"""Timeline from narration. usage: compose.py <episode_dir>  -> <ep>/timeline.json
episode.py: FMT ('short'|'long'), LINES, optional HOOK/HOOK2/HOOK_SWITCH (shorts), NUM, TAIL, LEAD.
Each shot lasts its line + a gap; subtitles are 2-3 word chunks timed inside each sentence."""
import sys, os, json, re, importlib.util
ep = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("e", f"{ep}/episode.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
meta = json.load(open(f"{ep}/vo/meta.json"))
GAP = {"punch": .45, "slow": .4, "question": .5}
t = getattr(E, "LEAD", 0.35); shots = []; subs = []; vo = []
for i, ((text, shot, kind), m) in enumerate(zip(E.LINES, meta)):
    vo.append(dict(f=m["f"], t=round(t, 3)))
    for s, a, b in m["segs"]:
        words = s.split(); chunks = []; cur = []
        for w in words:
            cur.append(w)
            if len(cur) == 3 or re.search(r"[,.!?;:]$", w): chunks.append(cur); cur = []
        if cur: chunks.append(cur)
        tot = sum(len(" ".join(c)) for c in chunks); x = t + a
        for c in chunks:
            d = (b - a) * len(" ".join(c)) / tot
            subs.append(dict(t0=round(x, 3), t1=round(x + d, 3), txt=" ".join(c))); x += d
    end = t + m["dur"] + shot.get("gap", GAP.get(kind, .3))
    segs = [(round(t + a, 3), round(t + b, 3)) for _, a, b in m["segs"]]
    shots.append(dict(t0=round(t if i else 0, 3), t1=round(end, 3), i=i, segs=segs, **shot)); t = end
T = round(t + getattr(E, "TAIL", 1.6), 2); shots[-1]["t1"] = T
fmt = getattr(E, "FMT", "short")
json.dump(dict(T=T, fmt=fmt, W=1920 if fmt == "long" else 1080, H=1080 if fmt == "long" else 1920, shots=shots, subs=subs, vo=vo,
               hook=getattr(E, "HOOK", ""), hook2=getattr(E, "HOOK2", ""), hookSwitch=getattr(E, "HOOK_SWITCH", 10**6), num=getattr(E, "NUM", "")),
          open(f"{ep}/timeline.json", "w"), indent=1)
print(fmt, "total", T, "s;", len(shots), "shots;", len(subs), "subtitle chunks")
