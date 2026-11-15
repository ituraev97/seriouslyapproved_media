#!/usr/bin/env python3
"""Build a dubbed audio track for LC002 in one language.
usage: dub_build.py <lang>   (reads dub/<lang>/script.txt, one line per original LINES entry)
Each line is synthesized with /home/claude/dub_tts.py (Edge first, offline fallback), fitted into its original
time slot (speed up to 1.2), placed at the original start time, mixed with the original music bed (no English voice),
loudness -14 LUFS, exported as dub/<lang>/LC002_<lang>.mp3 with the exact video length."""
import sys, os, json, hashlib, subprocess, io, contextlib
import numpy as np, soundfile as sf
sys.path.insert(0, '/home/claude'); sys.path.insert(0, '/home/claude/av/mia')
import dub_tts
from script import LINES

EP = '/home/claude/av/mia'; L = sys.argv[1]; D = f'{EP}/dub/{L}'; C = f'{D}/cache'; os.makedirs(C, exist_ok=True)
VIDEO_LEN = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f'{EP}/LC002_21air7598_miami.mp4']).decode())
T = {d['id']: d for d in json.load(open(f'{EP}/timing.json'))}
txt = [l.rstrip('\n') for l in open(f'{D}/script.txt', encoding='utf-8') if l.strip()]
assert len(txt) == len(LINES), (len(txt), len(LINES))
SR = 24000
log = {'engine': {}, 'speed': {}, 'overflow': {}}

def squeeze(a, keep=0.22, win=0.02):
    """shorten internal pauses (e.g. between sentences) to at most `keep` seconds"""
    w = int(win * SR); n = len(a) // w
    if n < 3: return a
    loud = np.array([np.abs(a[i*w:(i+1)*w]).max() > 0.01 for i in range(n)])
    out = []; i = 0; k = int(keep / win)
    while i < n:
        j = i
        while j < n and loud[j] == loud[i]: j += 1
        seg = a[i*w:j*w]
        if not loud[i] and (j - i) > k: seg = np.concatenate([seg[:k*w//2], seg[-(k*w - k*w//2):]])
        out.append(seg); i = j
    out.append(a[n*w:])
    return np.concatenate(out)

def trim(a):
    nz = np.where(np.abs(a) > 0.008)[0]
    return squeeze(a[max(0, nz[0] - 200): nz[-1] + 1200]) if len(nz) else a

def synth(text, speed):
    key = hashlib.md5(f'{L}|{text}|{speed:.3f}'.encode()).hexdigest()[:12]
    f = f'{C}/{key}.wav'; eng = 'edge'
    if not os.path.exists(f):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            a, sr = dub_tts.run(L, text, None, speed)
        if 'falling back' in err.getvalue(): eng = 'fallback'; open(f + '.fb', 'w').write(err.getvalue())
        if sr != SR:
            tmp = f + '.tmp.wav'; sf.write(tmp, a, sr)
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-ar', str(SR), f], check=True); os.remove(tmp)
        else: sf.write(f, a, sr)
    elif os.path.exists(f + '.fb'): eng = 'fallback'
    a, _ = sf.read(f, dtype='float32')
    return trim(a), eng

def stretch(a, sp):
    if sp <= 1.001: return a
    tmp = f'{C}/_st_in.wav'; out = f'{C}/_st_out.wav'; sf.write(tmp, a, SR)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-filter:a', f'atempo={sp:.3f}', out], check=True)
    return sf.read(out, dtype='float32')[0]

track = np.zeros(int(VIDEO_LEN * SR) + SR, np.float32); cursor = 0.0
for i, (lid, *_r) in enumerate(LINES):
    start = T[lid]['start']
    nxt = T[LINES[i + 1][0]]['start'] if i + 1 < len(LINES) else VIDEO_LEN - 0.5
    place = max(start, cursor)          # never overlap the previous line
    slot = nxt - place - 0.12           # time left before the next original line starts
    a, eng = synth(txt[i], 1.0)         # Edge at normal rate (cached); tempo fitted with atempo
    sp = 1.0
    if slot > 0 and len(a) / SR > slot: sp = min(1.2, round(len(a) / SR / slot * 1.02, 3))
    elif slot <= 0: sp = 1.2
    a = stretch(a, sp)
    log['engine'][lid] = eng; log['speed'][lid] = sp
    drift = place - start
    if drift > 0.05: log['overflow'][lid] = round(drift, 2)
    cursor = place + len(a) / SR + 0.15
    s = int(place * SR); n = max(0, min(len(a), len(track) - s)); track[s:s + n] += a[:n]
    print(lid, round(len(a) / SR, 2), 'slot', round(slot, 2), 'speed', sp, 'drift', round(drift, 2), eng, flush=True)
track = track[: int(VIDEO_LEN * SR)]
sf.write(f'{D}/voice.wav', track, SR)
json.dump(log, open(f'{D}/log.json', 'w'), indent=1)
FX = ("highpass=f=75,equalizer=f=140:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1.4:g=1.5,"
      "acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2")
out = f'{D}/LC002_{L}.mp3'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f'{D}/voice.wav', '-i', f'{EP}/music.wav', '-filter_complex',
    f"[0:a]aresample=48000,{FX},asplit[v1][v2];[1:a]volume=0.4[m];[m][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
    f"[md][v1]amix=inputs=2:normalize=0:duration=first[mx];[mx]loudnorm=I=-14:TP=-1.5:LRA=11,atrim=0:{VIDEO_LEN}[o]",
    '-map', '[o]', '-ar', '48000', '-c:a', 'libmp3lame', '-b:a', '192k', out], check=True)
print('DONE', out, 'drift (late start, s):', log['overflow'], 'fallback lines:', [k for k, v in log['engine'].items() if v != 'edge'])
