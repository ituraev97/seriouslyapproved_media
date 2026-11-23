# LAST CONTACT — production runbook (episode = 15-min long video + Shorts + TikToks)

Owner speaks Russian: all reports to him in Russian. Channel bible: Projects doc `claude/last-contact-bible.md` (read first).
Reference episode: `lastcontact/episodes/002-21air7598-miami/` (published 2026-11-14, https://www.youtube.com/watch?v=_M1-RE_wTyw).

## Shorts: cadence + hook rules — owner decision 2026-11-23 (OVERRIDES every other YouTube Shorts count/slot: the old "3 per day" of this file, the root SERIOUSLY APPROVED RUNBOOK's 3/6 per day and the bible)
Evidence (Metricool, 2026-10-23 → 11-22): 81 YouTube Shorts here got a median of 15 views with a median average view duration of 4 s. The three "The U.S. Approved a …" patent Shorts passed 1000 views (1210, 1041, 1014) but were watched only 1–2 s on average — feed impressions swiped away, which teaches YouTube to stop showing the channel. The NTSB aviation Shorts since Nov 14 have a higher floor (Nov 16–22 median 54 vs 12–13 before; Learjet 60 286 views, 13 s watched), and on TikTok aviation (1019, 811) beats patents (~92–330).
- **Cadence: 1–2 YouTube Shorts per day, never more.** The run still cuts its usual candidates (3 per day in vert.py), scores each with the scorecard below, and schedules only the best 1–2 per day on YouTube at 09:00 and 17:30 ET (≥ 6 h apart, different visual templates). On a long-video day (Mon/Wed/Fri/Sat) the 17:30 Short is a trailer for that day's long video (last line "Full story on the channel."). A candidate not used on YouTube may be extended to 61–90 s and used as one of the TikToks; **TikTok stays exactly 3 per day at 10:00, 15:30, 20:00 ET.**
- **Topic priority:** aviation/NTSB Shorts first. Patent Shorts ("The U.S. Approved a …") stay allowed — nothing is paused — but only with a real payoff that holds viewers (what it does / why it was approved / what happened to it, paid in the last 2–3 s); a patent Short that is only a name + drawing does not pass the scorecard.
- **Scorecard — a Short goes on YouTube only if it scores ≥ 7/10:** Hook 0–4 (the first second has a hard number, a famous name/brand or a paradox question, on screen AND spoken); Payoff 0–3 (the hook's promise is paid in the last 2–3 s: a reveal, a number, a twist); Freshness 0–2 (new story/angle, not the same template as yesterday's Short); Clarity 0–1 (understandable with sound off). Below 7 → rewrite the hook/cut and re-render; write each Short's score in the owner report.
- **Hook rules:** second 0 = the most surprising sentence — no logo, no title card, no "In 2008…" slow start; on-screen hook ≤ 7 words, large, centred in the upper third. Titles ≤ 60 chars + #shorts, formulas that won: [number] + [stakes] ("638 Gang Arrests in 179 Cities…"), [famous name] + [unexpected fact] ("The Wolf of Wall Street Still Owes…"), "Why/How did…?" + paradox ("How Did a Japanese Destroyer Lead U.S. Bombers to Its Own Carriers?").
- **Banned openers/titles:** quizzes ("Name this X in 3 seconds"), plain recaps of old cases with no number or famous name, "Here's what happened…", "Did you know…".
- **Length 20–40 s, hard cap 50 s.** End on the payoff and cut; no outro card longer than 1 s; a loopable last line is a plus.
- **Template rotation:** at least 3 visual templates (footage-led, document/number-led, map/timeline/3D-led); never the same one two days running.
- **Watch-time check:** a Short with average view duration < 5 s after 48 h = that hook style is dead; do not repeat it.
- **Weekly review every Monday:** read the last 7 days of YouTube Shorts analytics in Metricool (views + avg view duration), list top 3 / bottom 3, and add one line "what won" to this section — repeat the winners' hook pattern, drop the losers'.

## Real footage via relay — owner decision 2026-11-23 (OVERRIDES the rules below where they differ)
The cloud sandbox cannot reach youtube.com; a relay on the owner's server downloads clips from YouTube (or any yt-dlp URL: archive.org, C-SPAN, …) and hands them over through Google Drive folder "FOOTAGE RELAY". Client: `tools/footage_client.py` (stdlib only; read its docstring).
- Creds: Projects doc `claude/google-drive-oauth.md` → `/tmp/drive_creds.json` (keys client_id, client_secret, refresh_token). Never into git.
- Find candidates with the YouTube Data API (`claude/yt_research.py`, key in `claude/youtube-api-key.md`): search the exact accident + "NTSB", NTSB/FAA channels, news reports. Pick timestamps from titles/descriptions/chapters/transcripts where available.
- `clips.json` = `[{"name","src":"<youtube id or URL>","start":"M:SS","end":"M:SS"}]`, ≤ 40 clips, ≤ 90 s each.
- Request EARLY (right after research): `python3 tools/footage_client.py request <RUN> clips.json --creds /tmp/drive_creds.json` (RUN = e.g. lc-007-<date>), keep working (script, TTS, 3D), then `python3 tools/footage_client.py wait <RUN> /home/claude/av/mia/relay --creds /tmp/drive_creds.json --timeout 1800`. No answer in 30 min → continue without (DVIDS/NTSB photos/3D as before) and note it in the owner report.
- Source priority: (1) official/public-domain — NTSB media briefings and accident animations (NTSB YouTube = US government, public domain), FAA, US military/DVIDS, official ATC audio releases; (2) news reports of the exact accident (short clips, with our commentary — fair use) and manufacturer/airline official statements.
- NEVER: movies/TV dramas (Air Crash Investigation / Mayday reconstructions are copyrighted TV — never), other YouTubers' videos, victims' faces or bodies, gore, crash-moment footage showing people dying.
- Real footage 30–50% of runtime; ≤ ~12 s of one external clip at a time; mostly muted under narration, original audio only for short key quotes (≤ 15 s, speaker named on screen); on-screen source label on every clip ("NTSB MEDIA BRIEFING", "NEWS REPORT · <outlet>", …); list all footage sources (title, channel, URL) in the description and sources.md.
- LOOK at every received clip (contact sheet with exact `-ss` timestamps) before using it; drop anything that breaks the NEVER list.

## Voice = Chatterbox via TTS relay — owner decision 2026-11-23 (overrides "Voice (current)" in Environment and pipeline step 4)
Why: long videos are the weak spot (median 32 views) and the Kokoro narrator is the clearest "AI" tell. Chatterbox with the channel's own calm male voice (`lc`) runs on the owner's server, ~3–5 h per episode, so a run publishes the episode whose voice was ordered in the PREVIOUS run, and writes + orders the next one.
Tools: `tools/lc_voice.py` (wraps `tools/tts_client.py`; read both docstrings). Creds = the same `/tmp/drive_creds.json` as the footage relay. RUN id = `lc-<NNN>` (episode number).

**Run order:**
1. **Publish the voiced episode.** If the newest `lastcontact/episodes/NNN-slug/` has `VOICING` in its folder (a file with the RUN id), check `python3 tools/lc_voice.py status lc-NNN --creds /tmp/drive_creds.json`.
   - `ready` → setup, copy that episode's script.py (and research.md/sources.md) into /home/claude/av/mia, `python3 tools/lc_voice.py fetch lc-NNN /home/claude/av/mia --creds /tmp/drive_creds.json`, get the relay footage (`footage_client.py wait lc-NNN …`, clips stay 7 days), then pipeline steps 4–17 as usual (`tts.py` must not voice any line — if it does, the text changed after ordering: mixed voices, say so in the report). Delete `VOICING` in the commit.
   - `pending` (server still working) → build this run's episode with Kokoro (old flow, steps 1–17) so the schedule never slips, and keep `VOICING` for the next run.
   - `failed` or older than 72 h → build it now with Kokoro, delete `VOICING`.
   - No `VOICING` episode (first run after this change) → old flow with Kokoro for today.
2. **Write the next episode** (topic choice, research, script.py, independent fact-check with all fixes applied). Its LINES are final after the fact-check.
3. **Order its voice:** `python3 tools/lc_voice.py request lc-NNN lastcontact/episodes/NNN-slug/script.py --creds /tmp/drive_creds.json --hint "<airline, airport, aircraft type, place names>"`; order its footage (`footage_client.py request lc-NNN clips.json`). Commit script.py + research.md + sources.md + a `VOICING` file (content: lc-NNN) to main. Do NOT build it now.
**Writing for Chatterbox:** spoken text uses real spellings (no respellings; put names in `--hint`), numbers as words, short sentences; "!" only on real reveals; per-line speed still works (it becomes tempo); keep the pause column as before. ~2,300 words → ~15 min.

## Schedule (owner decision 2026-11-14)
- 4 long videos per week, ~15 min each (14:30–15:30 min of narration): Mon, Wed, Fri, Sat at 14:00 America/New_York.
- YouTube Shorts: 1–2 per day (20–40 s), the best-scoring of the day's candidates (owner 2026-11-23, see "Shorts: cadence + hook rules" at the top) + 3 TikToks per day (61–90 s), every day. Each run schedules Shorts/TikToks for its own day AND the following days until the next run day (Mon run → Mon+Tue, Wed → Wed+Thu, Fri → Fri, Sat → Sat+Sun).
- Default ET times: Shorts 09:00, 17:30 (trailer on long days); TikTok 10:00, 15:30, 20:00. Check getScheduledPosts first and avoid occupied slots. Ignore old SERIOUSLY APPROVED draft posts (draft=true, private) but do not publish next to them in the same minute.

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
- Blocked: youtube.com (→ real footage only via the relay, see top), FlightAware/FR24/ADS-B Exchange/OpenSky (also licence issues — do not use), NOAA NCEI.
- Kokoro: `pip install --break-system-packages kokoro-onnx soundfile scipy brotli`; models from github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/{kokoro-v1.0.onnx,voices-v1.0.bin} into /home/claude/models.
- Voice: Chatterbox `lc` via TTS relay (see "Voice = Chatterbox via TTS relay"). Kokoro fallback: `am_puck:0.7+am_echo:0.3`, speed = per-line speed ×1.0 (keep it: it is part of tts.py cache file names).
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
5. `python3 mkseg.py` → mweb/timing.json + segs.json. Real footage target 30–50% of runtime (relay clips + DVIDS/NTSB); no card segment longer than ~60 s without a change.
6. 3D scene `mweb/scene.js`: per-episode geometry (runway ends from OurAirports, displaced threshold from AirNav, rest point from report lat/lon), sim keyframes SK (time→distance) and GK (time→groundspeed) from report numbers only, EVENTS list, shots. Cards in `mweb/index.html` (.card divs, data-from="<line id>" reveals). Test stills with render_test.py (stills mode) and LOOK at contact sheets before full render.
7. Real footage: relay clips (see "Real footage via relay" at the top; `wait` into mia/relay/, visual ("clip", file, start_s, label) with source label, ≤ ~12 s per cut, muted under VO except named quotes ≤ 15 s) + DVIDS clips: search API, download 1080p, make contact sheets with exact timestamps (`-ss t` single frames — fps-tile sheets are offset by half an interval), avoid burnt-in titles/slates, 24p and 50fps sources.
8. `python3 build.py ffmpeg` (clips/photos), `nohup python3 build.py browser &` (3D 30 fps, cards 15→30 fps; ~45 min), `python3 build.py concat`.
9. Music: `python3 music_ep.py` (original synth bed) → mix with VO (sidechain, loudnorm −14 LUFS) → mux.
10. QA: contact sheet every 25 s, loudness, spot-check facts on screen.
11. Long for upload (owner decision 2026-11-23): 2-pass x264 so file ≤ 450 MB (Metricool YouTube limit 500 MB; 15 min → ~3,600 kbps video + 160 kbps audio). Fallbacks only if Metricool rejects it: ≤ 300 MB (~2,400 kbps video), then the old ≤ 95 MB (~720 kbps video + 96 kbps audio) via GitHub (step 14).
12. Verticals: `python3 vert.py` (edit cut list: Short candidates 20–40 s ending on a line end — score them, ≤ 2/day go on YouTube; TikToks 61–90 s). Layout: blurred bg, 16:9 video at y=720, title top (y 250–620), logo/footer y 1370–1530 (TikTok safe zones).
13. Thumbnails A/B/C (1280×720, Barlow Condensed 800, brand colors) → SendUserFile to owner.
14. Hosting — long video (owner decision 2026-11-23): Google Drive folder "LAST CONTACT": `python3 tools/drive_upload.py <long.mp4> --folder "LAST CONTACT" --creds /tmp/drive_creds.json` → its `direct` URL is the Metricool media (check it returns 200). Shorts/TikToks/thumbnails keep the GitHub hosting below (and the long video only in the ≤ 95 MB fallback). GitHub hosting: scratch dir `git init; git checkout -b up; cp files; git add -f; commit; git remote add origin https://github.com/ituraev97/seriouslyapproved_media; git -c push.negotiate=false push -f origin up:lc-<ddd>` (ddd = ET weekday, e.g. lc-sat). Verify every raw URL 200 + full size.
15. Metricool createScheduledPost (blogId 7805767): long (description with chapters, sources, independence line, hashtags; firstCommentText = one question), Shorts (text + "Full breakdown on the channel." + #planecrash #aviation #NTSB #shorts), TikToks (no links; #planecrash #aviation #NTSB #aviationtiktok #fyp). Then getScheduledPosts to confirm. After scheduling: `python3 tools/drive_upload.py --folder "LAST CONTACT" --creds /tmp/drive_creds.json --cleanup-days 7` (deletes this app's files older than 7 days; never the ones just scheduled).
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
- b777 model (2026-11-21, ep 006): long axis is z, nose faces −z → rotate yaw 180°; registration text "HL7742" is dark-material geometry on the wing → paint every material white except glass (see episodes/006 scene.js). Airborne-approach scene template (glidepath ribbon, PAPI sprites, HUD with A/T mode + PAPI) in episodes/006 scene.js.
- a320 model (2026-11-23, ep 007): long axis x, nose faces −x with the default auto-rotation → YAW 180; landing gear meshes Cylinder006/008/009/012/013/015/017/019/021/022 (hide for airborne shots); material names are generic (white/metal_1/gen_grey) so the clean-white mapping works as is. Docket 'Aircraft Performance' factual reports often contain ASR radar tables with lat/lon + Mode C — use them for the 3D track (episodes/007 scene.js). Smooth heading/bank and freeze heading ~7 s before the end of the track, otherwise bank spikes at the last point.

## Thumbnails v5 — illustrated cut-out from REAL images (owner decision 2026-11-23)
Owner: "bright and illustrated-looking, like the top drama channels — but faces must not be distorted". This section overrides the **thumb_A** part of the earlier thumbnail rules; thumb_B and thumb_C keep the current generator, so YouTube Studio → Test & Compare measures the new style against the old one. All earlier content rules stay in force: lawful image sources, every word true and sourced, fact-check of the thumbnail text, no gore, no victims' faces under crime words, bottom-right corner empty.

- Tool: `tools/thumbkit/thumbkit.py` (header = full spec). Setup once per run: `pip install -q pillow numpy opencv-python-headless "rembg[cpu]"` (downloads a 176 MB cut-out model on first use; if that fails the tool still works with a soft oval mask — say so in the report).
- It cuts the subject out of a real photo or video frame, adds a white sticker outline, a coloured glow and a rim light, washes the background in colour and sets 2–3 huge Anton words + an optional yellow sticker. Only pixel filters — no AI redraw, faces stay exactly as photographed. NEVER feed it an AI-generated image of a real person.
- Spec (`<ep>/thumbkit.json`, a list → thumb.jpg, thumb_B.jpg… — for this channel set "out":"thumb_A.jpg"):
  `[{"out":"thumb_A.jpg","layout":"solo","people":[{"src":"photo_or_clip","t":12.4,"crop":[x,y,w,h],"tint":"warm","kind":"person"}],"line1":"$250M","line2":"VANISHED","sticker":"SMALL FACT","brand":{"accent":"<channel colour>","sticker":"#FFD400","border":false}}]`
  - `layout`: "solo" (subject right, words left) or "versus" (two REAL sides of the same dispute, words centre — never pair people who are not part of the same story).
  - `kind`: "person" or "object" (boat, drug bundle, document, product, building, aircraft…).
  - `crop`: generous box around head + shoulders (face ≈ 35–50 % of its height) in source pixels; the subject must be ≥ 360 px tall in the source (the tool warns otherwise — find a bigger image).
  - `tint`: warm | cold | toxic | gold. `brand.accent` = the channel's main colour from the current generator.
- After rendering, LOOK at thumb_A at 320 px wide: words readable, face not covered, outline clean (no chunks of background). If the cut-out is bad (busy background, hands lost), use the current generator for A and say so in the report.
