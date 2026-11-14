import sys,os,json,numpy as np,soundfile as sf
sys.path.insert(0,'.'); from script import LINES
from kokoro_onnx import Kokoro
k=Kokoro('/home/claude/models/kokoro-v1.0.onnx','/home/claude/models/voices-v1.0.bin')
VOICE=os.environ.get('VOICE','am_puck:0.7+am_echo:0.3')
def style(s):
    if '+' not in s and ':' not in s: return s
    return sum(k.get_voice_style(n)*float(w) for n,w in (p.split(':') for p in s.split('+')))
V=style(VOICE); os.makedirs('vo',exist_ok=True)
out=[];t=0.0;tim=[];sr=24000
out.append(np.zeros(int(0.6*sr))); t=0.6
for i,(lid,txt,pause,spd,vis) in enumerate(LINES):
    import hashlib; f=f'vo/{lid}_'+hashlib.md5((txt+str(spd)+VOICE+'x1.0').encode()).hexdigest()[:8]+'.wav'
    if not os.path.exists(f):
        a,sr=k.create(txt,voice=V,speed=spd*1.0,lang='en-us'); sf.write(f,a,sr)
    a,sr=sf.read(f)
    # trim silence
    nz=np.where(np.abs(a)>0.01)[0]; a=a[max(0,nz[0]-240):nz[-1]+1200]
    tim.append({'id':lid,'start':round(t,3),'end':round(t+len(a)/sr,3),'text':txt})
    out.append(a); t+=len(a)/sr
    out.append(np.zeros(int(pause*sr))); t+=pause
y=np.concatenate(out); sf.write('vo_full.wav',y,sr)
json.dump(tim,open('timing.json','w'),indent=1); print('total',round(t,1))
