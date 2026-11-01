#!/usr/bin/env python3
"""Directed Kokoro narration. usage: tts.py <episode_dir>
Reads <ep>/episode.py: LINES = [(text, shot, kind)], optional VOICE, SPEED, VOICE_FX.
Channel voice (owner's choice 02.11.2026, variant B): am_michael, speed 1.06, FX chain below.
Writes <ep>/vo/NN.wav + vo/meta.json (per-sentence timings for subtitles)."""
import sys, os, re, json, subprocess, importlib.util, numpy as np, soundfile as sf, librosa
VOICE_FX_B = ("highpass=f=75,equalizer=f=140:t=q:w=1:g=2.5,equalizer=f=380:t=q:w=1.2:g=-2,"
              "equalizer=f=3200:t=q:w=1.4:g=2.5,equalizer=f=7500:t=q:w=1:g=-1.5,"
              "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2,aecho=0.85:0.5:28|51:0.12|0.07")
ep = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("e", os.path.join(ep, "episode.py")); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
from kokoro_onnx import Kokoro
M = os.environ.get("KOKORO_DIR", "/home/claude/tts")
k = Kokoro(f"{M}/kokoro-v1.0.onnx", f"{M}/voices-v1.0.bin")
VOICE = getattr(E, "VOICE", "am_michael"); BASE = float(getattr(E, "SPEED", 1.06)); FX = getattr(E, "VOICE_FX", VOICE_FX_B)
SPEED = {"calm": 1.0, "punch": 0.93, "tense": 1.04, "slow": 0.9, "drive": 1.08, "question": 0.96}
PAUSE = {"calm": .28, "punch": .42, "tense": .22, "slow": .5, "drive": .18, "question": .4}
SAY = getattr(E, "SAY", {})   # spoken respellings: {"word on screen": "how to say it"}
os.makedirs(f"{ep}/vo", exist_ok=True); meta = []
for i, (t, shot, kind) in enumerate(E.LINES, 1):
    f = f"{ep}/vo/{i:03d}.wav"; parts = []; segs = []; cur = 0
    sents = [s for s in re.split(r"(?<=[.!?])\s+", t.strip()) if s]
    for j, s in enumerate(sents):
        spoken = s
        for a_, b_ in SAY.items(): spoken = spoken.replace(a_, b_)
        sp = BASE * SPEED[kind] * (0.95 if s.endswith("?") else 1.0) * (0.94 if len(s.split()) <= 4 else 1.0)
        a, sr = k.create(spoken, voice=VOICE, speed=sp, lang="en-us")
        a, _ = librosa.effects.trim(a, top_db=38)
        segs.append((s, cur / sr, (cur + len(a)) / sr)); parts.append(a); cur += len(a)
        if j < len(sents) - 1:
            p = np.zeros(int(sr * PAUSE[kind]), dtype=np.float32); parts.append(p); cur += len(p)
    a = np.concatenate(parts); sf.write(f, a, sr)
    if FX:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-af", FX, "-ar", str(sr), f + ".fx.wav"], check=True); os.replace(f + ".fx.wav", f)
        a, _ = sf.read(f)
    meta.append(dict(f=f"vo/{i:03d}.wav", dur=len(a) / sr, segs=segs))
json.dump(meta, open(f"{ep}/vo/meta.json", "w"), indent=1)
print("speech", round(sum(m["dur"] for m in meta), 1), "s,", len(meta), "lines")
