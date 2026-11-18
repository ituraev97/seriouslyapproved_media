import numpy as np,soundfile as sf,json
from scipy.signal import butter,sosfilt
sr=48000; tm=json.load(open('timing.json')); D=tm[-1]['end']+2.0; n=int(D*sr); t=np.arange(n)/sr
T={d['id']:d for d in tm}
rng=np.random.default_rng(11)
mus=np.zeros(n)
prog=[(146.83,174.61,220.0),(116.54,146.83,174.61),(130.81,164.81,196.0),(110.0,130.81,164.81)]
for i in range(int(D/8)+1):
    a=i*8; ch=prog[i%4]; i0=int(a*sr); i1=min(n,int((a+10)*sr))
    if i0>=n: break
    tt=t[i0:i1]; e=np.clip((tt-a)/2.5,0,1)*np.clip((a+10-tt)/2.5,0,1)
    for f in ch:
        for det in (-0.5,0.5): mus[i0:i1]+=e*0.045*np.sin(2*np.pi*(f+det)*tt+rng.random()*6)
mus+=0.05*np.sin(2*np.pi*73.4*t)*(0.6+0.4*np.sin(2*np.pi*t/16))
pulse=np.zeros(n)
for k in np.arange(0,D,0.75):
    i=int(k*sr); L=int(0.06*sr)
    if i+L<n: pulse[i:i+L]+=np.sin(2*np.pi*880*np.arange(L)/sr)*np.exp(-np.arange(L)/(0.012*sr))*0.03
def env(a,b,fa=3,fb=3): return np.clip((t-a)/fa,0,1)*np.clip((b-t)/fb,0,1)
pulse*=env(0,T['o6']['start'])+env(T['x1']['start'],T['i1']['start'])
mus=sosfilt(butter(4,2500,fs=sr,output='sos'),mus+pulse)
mus*=np.clip(t/3,0,1)*np.clip((D-t)/3,0,1)
sf.write('music.wav',(mus*0.55).astype(np.float32),sr); print('music',round(D,1))
