import sys,os,subprocess
from PIL import Image,ImageDraw,ImageFont
B=os.path.expanduser('~/.fonts/BarlowC-ExtraBold.ttf'); M=os.path.expanduser('~/.fonts/JBMono-Bold.ttf')
G=(60,255,143,255); A=(255,176,32,255); W=(238,242,244,255)
SRC='master.mp4'
def overlay(path,l1,l2,kick,foot):
    im=Image.new('RGBA',(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    f=lambda s,fn=B:ImageFont.truetype(fn,s)
    d.text((60,250),kick,font=f(30,M),fill=G)
    y=300
    for line,col in ((l1,W),(l2,G)):
        for part in line.split('\n'):
            d.text((60,y),part,font=f(104),fill=col,stroke_width=3,stroke_fill=(0,0,0,255)); y+=108
    d.text((60,1370),"LAST",font=f(60),fill=W); d.text((185,1370),"CONTACT",font=f(60),fill=G)
    d.text((60,1450),foot,font=f(28,M),fill=(200,210,218,255))
    d.text((60,1500),"NTSB FINAL REPORT · NTSB/AAR-14/01",font=f(22,M),fill=(126,138,150,255))
    im.save(path)
def make(name,a,b,l1,l2,kick,foot):
    ov=f'pub/{name}_ov.png'; overlay(ov,l1,l2,kick,foot)
    fc=("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,eq=brightness=-0.28[bg];"
        "[b]scale=1080:608[fg];[bg][fg]overlay=0:720[v];[v][1:v]overlay=0:0,format=yuv420p[o]")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(a),'-t',str(b-a),'-i',SRC,'-i',ov,'-filter_complex',fc,'-map','[o]','-map','0:a',
        '-af','afade=t=out:st=%f:d=0.5'%(b-a-0.5),'-c:v','libx264','-preset','veryfast','-crf','21','-c:a','aac','-b:a','128k','-r','30','-movflags','+faststart',f'pub/{name}.mp4'],check=True)
    print(name, round(b-a,1))
import json; T={d['id']:d for d in json.load(open('timing.json'))}
def R(a,b): return T[a]['start']-0.15, T[b]['end']+0.45

K='ASIANA 214 · BOEING 777 · SFO · 2013'
FT='FULL BREAKDOWN ON THE CHANNEL'; GT='FOLLOW FOR THE NEXT FILE'
J=[('lc006-short1',*R('o3','o5'),'THE AUTOTHROTTLE','WAS IN HOLD',K,FT),
   ('lc006-short2',*R('m4','m6'),'THE MODE CHANGE','NO ONE NOTICED',K,FT),
   ('lc006-short3',*R('l6','l9'),'TWO WHITE, TWO RED.','THEN FOUR RED',K,FT),
   ('lc006-short4',*R('s5','s8'),'307 ON BOARD.','99% SURVIVED',K,FT),
   ('lc006-short5',*R('r3','r4'),'NO GLIDESLOPE.','FOUR LIGHTS',K,FT),
   ('lc006-short6',*R('q1','q2'),'NO MECHANICAL','FAILURE',K,FT),
   ('lc006-tt1',T['o1']['start']-0.15,T['o7']['end']+1.2,'ASIANA 214:','THE LAST\nMINUTE',K,GT),
   ('lc006-tt2',*R('m1','m7'),'HOW SPEED','CONTROL\nWAS LOST',K,GT),
   ('lc006-tt3',*R('l1','l8'),'THE LAST','1,000 FEET',K,GT),
   ('lc006-tt4',*R('x1','s2'),'GO AROUND.','2.5 SECONDS\nBEFORE IMPACT',K,GT),
   ('lc006-tt5',*R('w1','w5'),'WHY THE','SPEED WENT\nUNNOTICED',K,GT),
   ('lc006-tt6',*R('k1','k5'),'WHAT THE NTSB','ASKED FOR',K,GT)]
only=sys.argv[1:]
os.makedirs('pub',exist_ok=True)
for n,a,b,*r in J:
    if only and n not in only: continue
    make(n,a,b,*r)
