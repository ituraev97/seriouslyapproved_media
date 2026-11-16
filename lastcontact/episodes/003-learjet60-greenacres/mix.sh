set -e
cd /home/claude/av/mia
D=$(python3 -c "import json;print(json.load(open('timing.json'))[-1]['end']+2.0)")
ffmpeg -v error -y -i vo_full.wav -i music.wav -filter_complex "[0:a]aresample=48000,apad,atrim=0:$D,asplit[v1][v2];[1:a]volume=1.0[m];[m][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];[v1][md]amix=inputs=2:normalize=0:weights=1 0.9[o]" -map "[o]" -ac 2 mix.wav
cp mix.wav mix.mp3.wav; ffmpeg -v error -y -i mix.wav -c:a libmp3lame -b:a 192k mix.mp3; python3 norm2.py mix.mp3
ffmpeg -v error -y -i video_raw.mp4 -i mix.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest master.mp4
echo mixed
