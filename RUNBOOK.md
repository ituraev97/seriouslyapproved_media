# SERIOUSLY APPROVED — daily production runbook

One run = one long video (10–12 min, 1920×1080) + 6 vertical YouTube Shorts (45–60 s, 1080×1920) + 3 TikTok videos (62–85 s, 1080×1920) for ONE US day, uploaded to a `drop-<weekday>` branch and scheduled in Metricool.
Read the Projects doc `claude/seriously-approved-bible.md` first (rules, brand, voice, money). Reference Short: `episodes/000-test-kissing-shield/episode.py`.

## 0. Context
- Metricool brand "SERIOUSLY APPROVED": blogId **7805767**. Publish timezone **America/New_York**.
- Schedule per US day: Shorts 08:00, 10:30, 13:00, 15:00, 19:00, 22:00 ET; long video 16:00 ET (YouTube). TikTok (connected 04.11.2026): t1 09:30, t2 14:30, t3 20:30 ET.
- YouTube: madeForKids false, category ENTERTAINMENT. Do not set isAiGeneratedContent unless the owner decides so.
- Target date = tomorrow in America/New_York at run time. First call Metricool getScheduledPosts for blogId 7805767 over that date: if a YouTube long video is already scheduled, produce nothing and report.

## 1. Setup (fresh container)
```bash
# add_repo owner=ituraev97 repo=seriouslyapproved_media access=push first
git clone --depth 1 https://github.com/ituraev97/seriouslyapproved_media /home/claude/seriouslyapproved_media
cd /home/claude/seriouslyapproved_media/pipeline && npm i
pip install --break-system-packages kokoro-onnx soundfile scipy librosa potracer
mkdir -p /home/claude/tts && cd /home/claude/tts && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx && \
  curl -sLO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
```
Playwright's Chromium, ffmpeg and tesseract are preinstalled (render.mjs finds the headless shell itself).

## 2. Topic
- Take the first `todo` row of `topics.md`. Formats rotate: THE SHELF (Mon, Tue, Thu, Sat), ONE PATENT (Wed), DID IT WORK? (Fri), THE YEAR FILE (Sun). If the row's format does not match the weekday, take the next row that does.
- Never reuse a patent listed in `used_patents.json`.

## 3. Patents (8–10 for THE SHELF / YEAR FILE; 1 deep + 3–4 related for ONE PATENT)
- Find candidates with WebSearch (lists of weird/bizarre patents for the theme) and read each on Google Patents with WebFetch (`https://patents.google.com/patent/US<number>A/en`): title, inventor, filed, issued, abstract, figures, striking sentences. The shell cannot reach patents.google.com or USPTO.
- FIRST build the disk index once per container: `python3 pipeline/disk_index.py build` (~2 min), then check every candidate with `python3 pipeline/disk_index.py has <n> …` before researching it — only ~2.3 M of ~6 M patents have scans (e.g. the famous laser-pointer cat patent 5,443,036 does not). Good source of candidates: the Patent Citations / Cited By / Similar Documents lists on a Google Patents page of an available patent on the theme.
- Get the scan: `python3 pipeline/patent.py <number> $EP/pat` → TIFF from the archive.org USPTO disks, pages p0.png…, OCR p0.txt…, sheet.jpg. If it says "not on any disk", drop the patent (only 1868–1999 ranges exist).
- Exclude: injuries, death/tragedy, self-harm, weapons against people, sex, medical procedures on people, children at risk, any patent whose text carries a copyright notice. Laugh at the invention, never at the inventor; never show the front page (it carries the inventor's address); Shorts never name the inventor.
- Quotes: copy them from the OCR text and check them against the Google Patents text word for word. Note where each sits (claim N / col. N).
- Figures: view sheet.jpg and the page PNGs, choose 1–3 figures per patent, find their pixel boxes on the page (draw a grid with PIL to read coordinates), then:
  `python3 pipeline/vec.py $EP/pat/<N>/p<k>.png x0 y0 x1 y1 $EP/fig/<key>.svg [blank boxes]` (key e.g. `p3f1`), and for the thumbnail `python3 pipeline/figpng.py … $EP/thumb_fig.png`.
- Save `$EP/sources.md`: one block per patent — number, title, filed, issued, Google Patents URL, archive.org identifier/path, each quote with its location.

## 4. Scripts
Long: `$EP/episode.py` with `FMT = "long"`, `LINES = [(spoken, shot, kind)]`, optional `SAY` (on-screen word → spoken respelling).
- 1,500–1,800 spoken words → 10–12 min. Must be ≥ 10:00 (mid-roll ads). Structure: cold open ≤ 40 s (the wildest drawing + "This is real.") → title shot → for each patent: chapter shot (numeral, title, number, years) → 6–9 lines over its figures/quotes/how-it-worked → stamp → weekly "Most Approved" → tease + subscribe line.
- Every shot carries `hook` (left title, `[word]` = highlighter, `|` = line break) and `side` (e.g. `No. 3 · US 3,216,423 · 1965`).
Shorts: `$EP/shorts/s1 … s6/episode.py` with `FMT = "short"`, `NUM`, `HOOK` ("GUESS WHAT|THIS IS [FOR]" style), `HOOK2` (name of the invention), `HOOK_SWITCH` (index of the reveal line), optional `TAIL`. Copy the figures they use into `shorts/sN/fig/`. 45–60 s for YouTube.
TikTok: `$EP/tiktok/t1 … t3/episode.py` — extended versions of the three strongest Shorts. TikTok Creator Rewards pays only for videos > 60 s, so each must be 62–85 s (check `T` in timeline.json after compose; target ≥ 62). Get the extra length from MORE content — extra verified lines taken from the long episode.py (same patent), never padding, silence or slower speech. Keep the hook and the HOOK_SWITCH pointing at the stamp line. Every TikTok episode.py MUST set `TIKTOK = True` (frame.html then uses the TikTok safe-zone layout: nothing under the top search bar, the right-hand buttons or the bottom caption); check a still with the zones drawn on it. Hooks must fit 2 lines at 80 px in 820 px. Reference: `episodes/001-nobody-asked-for/tiktok/t1`, `t2`, `episodes/002-patents-for-your-cat/tiktok/t1`. `MIN_T` exists in compose.py but use it only for a second or two.
Shot types (pipeline/frame.html):
- `fig`: fig (svg key), figno, draw (False = already on screen), vb ("x y w h" crop in svg units = a cut to a detail), ring [x, y, size], calls [[text, x, y, dx, dy], …] (one per sentence of the line).
- `quote`: q (verbatim), hit (phrase to highlight), hide (True = black bar, revealed on the next line with typed=False), src ("US x · claim 1"), typed.
- `stamp`: title ("A|B" two lines), filed, date, big, nostamp, at (seconds into the line when it lands).
- `title`: kicker, title, lines [...], numeral, stamp, at.
Voice: Kokoro am_michael, speed 1.06 + FX chain B (defaults in tts.py; do not change without the owner). Write numbers and years as words. Deadpan: short sentences, no "crazy/insane". At most one dry aside per patent.

## 5. Independent fact-check (mandatory)
Launch a separate agent with sources.md + all episode.py files: every number, date, name and quote must match the patent text; "issued" vs "application" correct; nothing invented. Fix everything it finds before building.

## 6. Build
```bash
P=/home/claude/seriouslyapproved_media/pipeline
python3 $P/tts.py $EP && python3 $P/compose.py $EP
nohup node $P/render.mjs $EP 30 > $EP/render.log 2>&1 &     # long: ~15–25 min; poll the log
python3 $P/mix.py $EP && bash $P/encode.sh $EP $EP/long.mp4 95
for S in $EP/shorts/s* $EP/tiktok/t*; do python3 $P/tts.py $S && python3 $P/compose.py $S && node $P/render.mjs $S 30 && python3 $P/mix.py $S && bash $P/encode.sh $S $S/short.mp4 95; done
node $P/thumb.mjs $EP        # $EP/thumb.json: variants A and C -> thumb_A.png, thumb_C.png
```

## 7. QA (do not skip)
- Stills every ~8 s (`node render.mjs $EP 30 0 <T> 8`) → contact sheet: nothing clipped, callouts on the right parts, subtitles readable, no front page/addresses.
- Loudness ≈ −14 LUFS (encode.sh prints it). Long ≥ 10:00. Each Short ≤ 3 min. Each TikTok video ≥ 62 s (ffprobe the mp4).
- Thumbnail at 168×94: the big words still read; bottom-right corner empty.

## 8. Upload (public raw URLs for Metricool)
Branch = weekday of the ET publish date: drop-mon … drop-sun. Orphan commit with only that day's files, force-push:
```bash
cd /home/claude/seriouslyapproved_media && git checkout --orphan up && git rm -rqf . && \
cp $EP/long.mp4 $EP/thumb_A.png . && for i in 1 2 3 4 5 6; do cp $EP/shorts/s$i/short.mp4 s$i.mp4; done && \
for i in 1 2 3; do cp $EP/tiktok/t$i/short.mp4 t$i.mp4; done && \
git add long.mp4 thumb_A.png s*.mp4 t*.mp4 && git -c user.name="SERIOUSLY APPROVED bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -f origin up:drop-XXX && git checkout -q main && git branch -D up
```
URL: `https://raw.githubusercontent.com/ituraev97/seriouslyapproved_media/drop-XXX/<file>`; check each with `curl -sI` (200).

## 9. Schedule in Metricool
- createScheduledPost, blogId 7805767, providers [{"network":"youtube"}], publicationDate {dateTime, timezone:"America/New_York"}, autoPublish true.
- Long: youtubeData {title, type:"video", privacy:"public", tags, category:"ENTERTAINMENT", madeForKids:false}; text = description; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL ONLY if the channel is phone-verified — otherwise Metricool rejects the whole post (VIDEO_THUMBNAIL_NOT_APPLICABLE): resend without videoThumbnailUrl and tell the owner.
- Shorts: youtubeData {title, type:"short", privacy:"public", category:"ENTERTAINMENT", madeForKids:false}; text = Short description.
- TikTok (connected 04.11.2026): three separate posts t1.mp4/t2.mp4/t3.mp4 at 09:30, 14:30, 20:30 ET; providers [{"network":"tiktok"}]; tiktokData {"privacyOption":"PUBLIC_TO_EVERYONE","title":"<same as the Short title>","disableComment":false,"disableDuet":false,"disableStitch":false,"autoAddMusic":false,"isAigc":false}; text = one hook line + "Real U.S. patent <number> (<year>)." + `#weirdpatents #inventions #patents #history #funnyinventions #fyp` (no links, no "full episode" line — the long video is not on TikTok). Only videos ≥ 62 s go to TikTok. Instagram: only once connected.
- Titles: long ≤ 70 chars, curiosity + "Real Patents" (e.g. "9 Real Patents Nobody Asked For (All Approved)"); Short = the invention + a hook ("The U.S. Approved a Kissing Shield").
- Long description: 2-line summary · chapters with timestamps (chapter shot starts from timeline.json, first = 0:00) · "Patents in this video:" one line each (number, title, year, Google Patents link) · "SERIOUSLY APPROVED is an independent channel and is not affiliated with or endorsed by the USPTO. Patent texts and drawings: U.S. patents (public record)." · hashtags `#weirdpatents #inventions #weirdhistory #patents #strangeinventions #history`.
- Short description: one line + "US <number> (<year>) — <Google Patents link>" + "Full episode on the channel." + `#weirdpatents #inventions #shorts #patents #weirdhistory #funnyinventions`.

## 10. Close the run
- Commit to main: `episodes/NNN-slug/` (episode.py, shorts/*/episode.py, fig/*.svg, sources.md, thumb.json, description.txt — never video, audio or scans), `topics.md` row → `done YYYY-MM-DD`, `used_patents.json` (+ numbers used).
- Message the owner in Russian: title, publish times (ET and Tashkent), patents used, thumb_C attached for Test & Compare, anything needing attention.

## Performance rules
Weekly review (Mondays, Metricool, last 28 days). Each rule is backed by ≥ 3 videos; small samples — re-check every Monday and drop rules the data stops supporting. Schedules, AI labels and the owner's content/title rules are NOT changed here (see "Recommendations to the owner").
1. Shorts lose viewers in the first seconds: average view duration 1–9 s (median 4 s) across 9 Shorts with data → the drawing AND the object's name must be on screen at 0.0 s, the first spoken line names the object in ≤ 12 words, no warm-up sentence. QA frame at 0.5 s stays mandatory.
2. Cat-accessory Shorts underperformed: 5 cat Shorts (03–04.11) median 3 views vs 4 non-cat Shorts (02–03.11) median 89 → no cat-only drop before 30.11; mix animals into broader themes instead (day effect confounded — re-check).
3. Dog/everyday-object hooks lead: the channel's best Short is the dog watch (1,141) and the next three are everyday objects (mask 121, fork 57, collar 29) → pick Shorts patents that are a familiar household object or pet item doing something absurd, readable from one drawing.
4. TikTok: food/kitchen patents (ice pop 174, corn dog 123, pasta fork 110, cotton candy 93; median 117) beat hats (4 posts, median 101) and the overall median (110, 13 posts) → when choosing t1–t3, prefer food, kitchen and household objects.
5. TikTok length 70–82 s made no difference to views (13 posts, r = 0.14) → target 62–72 s (higher completion), never under 62 s.
6. Metricool returns no YouTube views for posts younger than ~5 days (all 04.11+ rows empty on 09.11) → judge YouTube videos only after 5 days; TikTok rows are usable next day.
7. Long videos: only 1 long with data (2 views, 265 s average view duration) → no rule yet; keep the owner's growth packaging (number/ranking titles) and review when ≥ 3 longs have data.

Recommendations to the owner (not applied): (a) descriptive Short titles "A [object] That [does X]" (4 Shorts, median 43 views) beat "The U.S. Approved a …" (5 Shorts, median 3; dog watch excepted) — consider allowing one descriptive title per day as a test; (b) TikTok TKPO15 (avg watch time) is empty — check that the TikTok account is connected as Business in Metricool so watch time is reported.

Changelog
- 2026-11-09: section created (first weekly review; data 02–08.11: 10 YouTube videos with analytics, 13 TikToks).
