import numpy as np,soundfile as sf,json
import json as _j
sr=48000; D=_j.load(open('/home/claude/av/mia/segs.json'))[-1]['end']; n=int(D*sr); t=np.arange(n)/sr
T={d['id']:d for d in json.load(open('/home/claude/av/mia/timing.json'))}
def env(a,b,fa=2,fb=2):
    return np.clip((t-a)/fa,0,1)*np.clip((b-t)/fb,0,1)
rng=np.random.default_rng(7)
mus=np.zeros(n)
# chord progression every 8s: Dm, Bb, F, C (roots in Hz)
prog=[(146.83,174.61,220.0),(116.54,146.83,174.61),(174.61,220.0,261.63),(130.81,164.81,196.0)]
for i in range(int(D/8)+1):
    a=i*8; ch=prog[i%4]; i0=int(a*sr); i1=min(n,int((a+10)*sr))
    if i0>=n: break
    tt=t[i0:i1]; e=np.clip((tt-a)/2.5,0,1)*np.clip((a+10-tt)/2.5,0,1)
    for f in ch:
        for det in (-0.6,0.6):
            mus[i0:i1]+=e*0.05*np.sin(2*np.pi*(f+det)*tt+rng.random()*6)
mus+=0.06*np.sin(2*np.pi*73.4*t)*(0.6+0.4*np.sin(2*np.pi*t/16))
# soft pulse (ticks) during investigative parts
pulse=np.zeros(n)
for k in np.arange(0,D,0.75):
    i=int(k*sr); L=int(0.06*sr)
    if i+L<n: pulse[i:i+L]+=np.sin(2*np.pi*880*np.arange(L)/sr)*np.exp(-np.arange(L)/(0.012*sr))*0.03
pulse*=env(T['l1']['start'],T['l11']['end'],3,3)+env(T['f6']['start'],T['x3']['end'],3,3)+env(T['z2']['start'],T['z4']['end'],3,3)
mus=mus+pulse
# lowpass-ish smoothing
from scipy.signal import butter,sosfilt
mus=sosfilt(butter(4,2500,fs=sr,output='sos'),mus)
sfx=np.zeros(n)
# music ducked lower overall, fade in/out
mus*= np.clip(t/3,0,1)*np.clip((D-t)/3,0,1)
sf.write('/home/claude/av/mia/music.wav',(mus*0.55).astype(np.float32),sr); sf.write('/home/claude/av/mia/sfx.wav',sfx.astype(np.float32),sr)
print('ok')
