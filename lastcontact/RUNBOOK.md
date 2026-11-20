# LAST CONTACT — production runbook (episode = 15-min long video + Shorts + TikToks)

Owner speaks Russian: all reports to him in Russian. Channel bible: Projects doc `claude/last-contact-bible.md` (read first).
Reference episode: `lastcontact/episodes/002-21air7598-miami/` (published 2026-11-14, https://www.youtube.com/watch?v=_M1-RE_wTyw).

## Schedule (owner decision 2026-11-14)
- 4 long videos per week, ~15 min each (14:30–15:30 min of narration): Mon, Wed, Fri, Sat at 14:00 America/New_York.
- 3 YouTube Shorts per day (20–40 s) + 3 TikToks per day (61–90 s), every day. Each run schedules Shorts/TikToks for its own day AND the following days until the next run day (Mon run → Mon+Tue, Wed → Wed+Thu, Fri → Fri, Sat → Sat+Sun).
- Default ET times: Shorts 09:00, 17:30, 21:00; TikTok 10:00, 15:30, 20:00. Check getScheduledPosts first and avoid occupied slots. Ignore old SERIOUSLY APPROVED draft posts (draft=true, private) but do not publish next to them in the same minute.

## Accounts
- YouTube LAST CONTACT, channel UCt8DhOqdA0YRC0WzLIyuekA (not phone-verified → never pass videoThumbnailUrl; send thumbnails A/B/C to owner via SendUserFile).
- TikTok @lastcontactfiles. Metricool brand blogId 7805767.
- YouTube: type video/short, privacy public, category EDUCATION, madeForKids false, isAiGeneratedContent false (never set AI labels). TikTok: PUBLIC_TO_EVERYONE, isAigc false, autoAddMusic false.

## Topic choice (every run)
1. Freshest U.S. accident/incident WITH official material: NTSB investigation pages (ntsb.gov/investigations), NTSB press releases/investigative updates, preliminary reports (ntsb.gov/investigations/Documents/<ID> Prelim.pdf), CAROL/docket (data.ntsb.gov), FAA statements (faa.gov/newsroom/statements/accident_incidents).
2. Demand check: `claude/yt_research.py` (YouTube Data API key in `claude/youtube-api-key.md`), last 7–30 days.
3. No repeats: `lastcontact/used_cases.json`. A big case may get a follow-up ("NTSB update") when new official info appears.
4. Fallback on quiet days: well-known U.S. accidents with NTSB FINAL reports (docket photos, CVR transcripts as text).

## Rules (mandatory)
- Facts only from official sources; media only as "according to". Every number in sources.md. "Preliminary" until final report. Never state or imply cause/blame before the NTSB final report; open questions phrased as questions.
- No victims' names/photos, no bodies, no vehicles/places of death up close, no LiveATC audio, no other channels'/TV video, no media/social/local-police photos.
- Footage not of the event → label "FILE FOOTAGE · <what> · DVIDS" (never pass it off as the event). 3D → label "RECONSTRUCTION FROM NTSB … DATA · MOTION BETWEEN DATA POINTS INTERPOLATED".
- Independent fact-check by a separate agent BEFORE final TTS/render: every spoken line, on-screen text, title, thumbnail words. Apply all FIX items.
- Thumbnails: arrow/circle only on a meaningful detail; never crop in victims' vehicles/labels; never mirror images with text.

## Environment (verified 2026-11-14)
- Reachable: ntsb.gov, data.ntsb.gov, faa.gov, whitehouse.gov, aviationweather.gov, api.weather.gov, api.dvidshub.net (key-6ae3182ef3840), USGS basemap/elevation (basemap.nationalmap.gov export endpoint, max cached zoom 16 — use `export?bbox=…&bboxSR=3857&imageSR=3857&size=4096,4096`), raw.githubusercontent.com (OurAirports runways.csv), api.adsb.lol (live only, no history), flickr.com pages (but live.staticflickr.com returns 429 to the cloud — take NTSB photos from report PDFs via `pdfimages` and from ntsb.gov PublishingImages).
- Blocked: youtube.com, FlightAware/FR24/ADS-B Exchange/OpenSky (also licence issues — do not use), NOAA NCEI.
- Kokoro: `pip install --break-system-packages kokoro-onnx soundfile scipy brotli`; models from github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/{kokoro-v1.0.onnx,voices-v1.0.bin} into /home/claude/models.
- Voice (current): `am_puck:0.7+am_echo:0.3`, speed = per-line speed ×1.0.
- Chrome + Playwright preinstalled; three.js via npm. SwiftShader WebGL: ~0.3 s/frame for 3D at pixelRatio 0.7, ~0.1 s for cards.

## Setup (fresh container)
```bash
mkdir -p /home/claude/av && cp -r lastcontact/av/* /home/claude/av/
cd /home/claude/av && mkdir -p web && cp package.json web/ && cd web && npm i && cd .. && ln -sfn ../web/node_modules mweb/node_modules
mkdir -p ~/.fonts && cd web/node_modules/@fontsource && python3 -c "
from fontTools.ttLib import TTFont; import os
for s,d in [('jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2','JBMono-Bold.ttf'),('barlow-condensed/files/barlow-condensed-latin-800-normal.woff2','BarlowC-ExtraBold.ttf')]:
  f=TTFont(s); f.flavor=None; f.save(os.path.expanduser('~/.fonts/'+d))"
```
Scripts assume episode work dir /home/claude/av/mia and web dir /home/claude/av/mweb (rename per episode only if you also edit EP/WEB paths in build.py, mkseg.py, tts.py, vert.py, music_ep.py).

## Pipeline (reference: episode 002)
1. Research → `research.md`, `sources.md` (download prelim PDF; `pdftotext -layout`; `pdfimages -j -png` for official figures; contact-sheet every figure and look at it).
2. Script `mia/script.py`: LINES = (id, spoken text, pause, speed, visual). Visual = ("3d", shot) | ("card", name) | ("photo", file, credit) | ("clip", file, start_s, label). ~2,400 words → ~15:00 at speed 1.0. Structure that worked: cold open (3D) → toll card → title → investigation parties → airplane/flight/crew (cards + FILE FOOTAGE) → airport (3D/diagram) → weather (METAR card + wind calc) → ATC → CVR timeline card → context explainer (stabilized approach etc.) → landing on runway (3D + HUD from FDR numbers) → how the system works (explainer card) → replay → beyond the runway (NTSB photos) → wreckage findings → safety equipment → open questions → status/end card.
3. Fact-check agent → apply fixes.
4. `python3 tts.py` → vo_full.wav + timing.json (cached per line hash).
5. `python3 mkseg.py` → mweb/timing.json + segs.json. Real footage target ≥ 25% of runtime; no card segment longer than ~60 s without a change.
6. 3D scene `mweb/scene.js`: per-episode geometry (runway ends from OurAirports, displaced threshold from AirNav, rest point from report lat/lon), sim keyframes SK (time→distance) and GK (time→groundspeed) from report numbers only, EVENTS list, shots. Cards in `mweb/index.html` (.card divs, data-from="<line id>" reveals). Test stills with render_test.py (stills mode) and LOOK at contact sheets before full render.
7. DVIDS clips: search API, download 1080p, make contact sheets with exact timestamps (`-ss t` single frames — fps-tile sheets are offset by half an interval), avoid burnt-in titles/slates, 24p and 50fps sources.
8. `python3 build.py ffmpeg` (clips/photos), `nohup python3 build.py browser &` (3D 30 fps, cards 15→30 fps; ~45 min), `python3 build.py concat`.
9. Music: `python3 music_ep.py` (original synth bed) → mix with VO (sidechain, loudnorm −14 LUFS) → mux.
10. QA: contact sheet every 25 s, loudness, spot-check facts on screen.
11. Long for upload: 2-pass x264 so file ≤ 95 MB (15 min → ~720 kbps video + 96 kbps audio).
12. Verticals: `python3 vert.py` (edit cut list: Shorts 20–40 s ending on a line end; TikToks 61–90 s). Layout: blurred bg, 16:9 video at y=720, title top (y 250–620), logo/footer y 1370–1530 (TikTok safe zones).
13. Thumbnails A/B/C (1280×720, Barlow Condensed 800, brand colors) → SendUserFile to owner.
14. Hosting: scratch dir `git init; git checkout -b up; cp files; git add -f; commit; git remote add origin https://github.com/ituraev97/seriouslyapproved_media; git -c push.negotiate=false push -f origin up:lc-<ddd>` (ddd = ET weekday, e.g. lc-sat). Verify every raw URL 200 + full size.
15. Metricool createScheduledPost (blogId 7805767): long (description with chapters, sources, independence line, hashtags; firstCommentText = one question), Shorts (text + "Full breakdown on the channel." + #planecrash #aviation #NTSB #shorts), TikToks (no links; #planecrash #aviation #NTSB #aviationtiktok #fyp). Then getScheduledPosts to confirm.
16. Commit episode folder (script.py, sources.md, meta.json, research.md) to main under lastcontact/episodes/NNN-slug/ and add case to used_cases.json. Never commit media to main.
17. Report to owner in Russian (SendUserMessage): case and why, titles, durations, times ET + Tashkent, Metricool links, fact-check result, QA, problems.

## 3D aircraft models (added 2026-11-17, owner request: more realistic 3D)
- Real CC BY 4.0 models from Sketchfab are on the orphan branch `lc-models` of this repo:
  `git clone --depth 1 --branch lc-models https://github.com/ituraev97/seriouslyapproved_media /home/claude/lc-models`
  Types: b767, b767_detail, learjet45, learjet55, b737, b737_800, a320, b777, crj900, citationx, c172, sr22 (`<type>/model.glb`, credits in CREDITS.json).
- Render speed (2026-11-20): SwiftShader on 2 cores ≈ 0.7 s/frame for 3D with HDRI env; never run other heavy jobs (music synth, x264) in parallel with build.py browser. Background jobs die when a turn ends — run long encodes in the foreground (timeout ≤ 600 s).
- Load with three.js GLTFLoader instead of the procedural airplane; normalise scale from the bounding box to the real length of the type.
- Lighting: HDRI from Poly Haven (CC0), e.g. `kloofendal_48d_partly_cloudy_puresky` 2k
  (`curl -A "Mozilla/5.0" https://api.polyhaven.com/files/<id>` → hdri.2k.hdr.url), RGBELoader, ACES tone mapping, shadows on.
- Liveries: NEVER show airline/company logos. Use "clean" mode (remove base-color maps, paint #eceef0) unless the model is already plain white (b767, citationx).
- If a new type is needed: search Sketchfab API (downloadable=true, license CC Attribution or CC0, no NonCommercial/NoDerivs);
  download needs the owner's Sketchfab API token — it is NOT stored anywhere; if no model fits, use the closest type and say "illustrative model" on screen.
- Description must credit every model used: "3D model: <title> by <author> (Sketchfab), CC BY 4.0, <url>".
