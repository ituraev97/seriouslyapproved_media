#!/usr/bin/env python3
"""Voice + plucked score (ducked) + SFX (pen, stamp, typewriter, pops). usage: mix.py <episode_dir> -> mix.wav"""
import sys, json, numpy as np, soundfile as sf, scipy.signal as ss
ep = sys.argv[1]; tl = json.load(open(f"{ep}/timeline.json")); SR = 48000; N = int(tl["T"] * SR) + SR
rng = np.random.default_rng(7)
def place(buf, a, t, g=1.0):
    i = int(t * SR); a = a[: max(0, len(buf) - i)]; buf[i:i + len(a)] += a * g
# --- voice
vo = np.zeros(N)
for v in tl["vo"]:
    a, sr = sf.read(f"{ep}/{v['f']}"); a = a if a.ndim == 1 else a.mean(1)
    a = ss.resample_poly(a, SR, sr); place(vo, a, v["t"])
# --- music: plucked arpeggios (Karplus-Strong) + soft bass, F major I-vi-ii-V, 100 bpm
def pluck(f, dur=1.2, dec=0.996):
    n = int(SR * dur); p = int(SR / f); buf = rng.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n): out[i] = buf[i % p]; buf[i % p] = dec * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return out * np.linspace(1, 0, n) ** 1.5
def bass(f, dur):
    t = np.arange(int(SR * dur)) / SR; return (np.sin(2 * np.pi * f * t) + .3 * np.sin(4 * np.pi * f * t)) * np.exp(-t * 3)
mu = np.zeros(N); beat = 60 / 100
chords = [[65.41*1.335, [349.2, 440, 523.3]], [73.42, [293.7, 349.2, 440]], [98.0*0.8, [392, 466.2, 587.3]], [65.41, [261.6, 329.6, 392, 466.2]]]
cache = {}
t = 0.0; k = 0
while t < tl["T"]:
    root, ns = chords[k % 4]
    place(mu, bass(root, beat * 4), t, .5)
    for j in range(8):
        f = ns[[0, 1, 2, 1, 0, 2, 1, 2][j] % len(ns)]
        if f not in cache: cache[f] = pluck(f)
        place(mu, cache[f], t + j * beat / 2, .28 if j % 2 else .38)
    t += beat * 4; k += 1
fade = np.ones(N); e = int(tl["T"] * SR); fade[e - SR:e] = np.linspace(1, 0, SR); fade[e:] = 0; mu *= fade
# duck under voice
env = np.abs(vo); env = ss.filtfilt(*ss.butter(2, 4 / (SR / 2)), env); duck = 1 - 0.55 * np.clip(env / (env.max() * .25), 0, 1)
mu *= duck
# --- SFX
sfx = np.zeros(N)
def noise(d): return rng.normal(0, 1, int(SR * d))
def bp(a, lo, hi): return ss.sosfilt(ss.butter(2, [lo / (SR / 2), hi / (SR / 2)], "band", output="sos"), a)
for s in tl["shots"]:
    t0 = s["t0"]
    if s["g"] == "fig" and s.get("draw", True):              # pen scratching the drawing on
        a = bp(noise(1.9), 2500, 7000) * (0.5 + 0.5 * np.abs(np.sin(np.arange(int(SR * 1.9)) / SR * 2 * np.pi * 5)))
        a *= np.r_[np.linspace(0, 1, 2400), np.ones(len(a) - 4800), np.linspace(1, 0, 2400)]; place(sfx, a, t0, .06)
    if (s["g"] == "stamp" or (s["g"] == "title" and s.get("stamp"))) and not s.get("nostamp"):   # stamp hit
        tt = np.arange(int(SR * .35)) / SR; th = np.sin(2 * np.pi * 70 * tt * (1 - tt)) * np.exp(-tt * 18) + bp(noise(.35), 300, 3000) * np.exp(-tt * 40) * .6
        place(sfx, th, t0 + s.get("at", .45) + .2, .9)
    if s["g"] == "quote" and s.get("typed", True):             # typewriter keys
        n = len(s["q"]); dur = min(2.4, n * .028)
        for c in range(0, n, 2):
            tt = np.arange(int(SR * .03)) / SR; place(sfx, bp(noise(.03), 1500, 6000) * np.exp(-tt * 160), t0 + c / n * dur, .18 * rng.uniform(.7, 1))
    if s.get("calls"):
        for (a_, b_) in s["segs"][:len(s["calls"])]:
            tt = np.arange(int(SR * .08)) / SR; place(sfx, np.sin(2 * np.pi * 1200 * tt) * np.exp(-tt * 50), a_, .12)
    if s.get("ring"):
        tt = np.arange(int(SR * .08)) / SR; place(sfx, np.sin(2 * np.pi * 900 * tt) * np.exp(-tt * 50), t0, .12)
mix = vo * 1.0 + mu * 0.22 + sfx
mix = mix[: int(tl["T"] * SR)]; mix /= max(1e-9, np.abs(mix).max()) / 0.9
sf.write(f"{ep}/mix.wav", np.c_[mix, mix].astype(np.float32), SR); print("ok", len(mix) / SR)
