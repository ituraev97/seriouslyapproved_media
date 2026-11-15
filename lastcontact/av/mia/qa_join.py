import sys, json, random, numpy as np, soundfile as sf
sys.path.insert(0,'.'); from script import LINES
T={d['id']:d for d in json.load(open('timing.json'))}
random.seed(11)
for l in sys.argv[1:]:
    v,sr=sf.read(f'dub/{l}/voice.wav',dtype='float32'); lg=json.load(open(f'dub/{l}/log.json'))
    def rms(a,b): seg=v[int(a*sr):int(b*sr)]; return float(np.sqrt((seg**2).mean())) if len(seg) else 0
    bad=[]
    for i,(lid,*_) in enumerate(LINES):
        p=T[lid]['start']+lg['overflow'].get(lid,0)
        if i>0 and rms(p-0.08,p-0.01)>0.01: bad.append(lid)   # previous line still talking at a join
    pick=sorted(random.sample(range(len(LINES)),3)); res=[]
    for i in pick:
        lid=LINES[i][0]; p=T[lid]['start']+lg['overflow'].get(lid,0)
        res.append(f"{lid}@{p:.1f}s voice={rms(p,p+1.5):.3f} pre={rms(p-0.3,p-0.02):.3f}")
    print(l,'overlapping joins:',bad or 'none','| spot:',' ; '.join(res),'| max drift',max(lg['overflow'].values() or [0]))
