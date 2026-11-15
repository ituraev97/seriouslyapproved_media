import sys, json, subprocess, re
f=sys.argv[1]
r=subprocess.run(['ffmpeg','-hide_banner','-i',f,'-af','loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
m=json.loads(r[r.rindex('{'):r.rindex('}')+1])
af=f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000"
subprocess.run(['ffmpeg','-v','error','-y','-i',f,'-af',af,'-c:a','libmp3lame','-b:a','192k',f+'.tmp.mp3'],check=True)
import os; os.replace(f+'.tmp.mp3',f)
