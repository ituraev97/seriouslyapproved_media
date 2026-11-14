import sys,os,subprocess
from PIL import Image,ImageDraw,ImageFont
B=os.path.expanduser('~/.fonts/BarlowC-ExtraBold.ttf'); M=os.path.expanduser('~/.fonts/JBMono-Bold.ttf')
G=(60,255,143,255); A=(255,176,32,255); W=(238,242,244,255)
SRC='LC002_21air7598_miami.mp4'
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
    d.text((60,1500),"NTSB PRELIMINARY DATA · NO CAUSE DETERMINED",font=f(22,M),fill=(126,138,150,255))
    im.save(path)
def make(name,a,b,l1,l2,kick,foot):
    ov=f'pub/{name}_ov.png'; overlay(ov,l1,l2,kick,foot)
    fc=("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=24:2,eq=brightness=-0.28[bg];"
        "[b]scale=1080:608[fg];[bg][fg]overlay=0:720[v];[v][1:v]overlay=0:0,format=yuv420p[o]")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(a),'-t',str(b-a),'-i',SRC,'-i',ov,'-filter_complex',fc,'-map','[o]','-map','0:a',
        '-af','afade=t=out:st=%f:d=0.5'%(b-a-0.5),'-c:v','libx264','-preset','veryfast','-crf','21','-c:a','aac','-b:a','128k','-r','30','-movflags','+faststart',f'pub/{name}.mp4'],check=True)
    print(name, round(b-a,1))
J=[('lc002-short1',640.0,673.4,'TOUCHDOWN','3,750 FT DOWN\nTHE RUNWAY','21 AIR 7598 · MIAMI · SEP 6, 2026','FULL BREAKDOWN ON THE CHANNEL'),
   ('lc002-short2',0.0,39.8,'A 767 LEFT','THE RUNWAY\nAT 113 KNOTS','AMAZON 767 · MIAMI · SEP 6, 2026','FULL BREAKDOWN ON THE CHANNEL'),
   ('lc002-short3',719.2,0,'WHAT NTSB','FOUND IN\nTHE COCKPIT','21 AIR 7598 · BOEING 767','FULL BREAKDOWN ON THE CHANNEL'),
   ('lc002-tt1',0.0,73.9,'AMAZON 767','OFF THE RUNWAY\nIN MIAMI','NTSB PRELIMINARY REPORT','FOLLOW FOR THE NEXT FILE'),
   ('lc002-tt2',605.7,673.4,'THE FINAL','SECONDS ON\nTHE RUNWAY','FROM NTSB FLIGHT DATA','FOLLOW FOR THE NEXT FILE'),
   ('lc002-tt3',367.9,452.4,'COCKPIT','VOICE RECORDER\nTIMELINE','NTSB SUMMARY · 21 AIR 7598','FOLLOW FOR THE NEXT FILE')]
import json; T={d['id']:d for d in json.load(open('timing.json'))}
for n,a,b,*r in J:
    if n=='lc002-short3': b=T['f3']['end']+0.5
    make(n,a,b,*r)
