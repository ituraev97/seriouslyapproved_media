# SERIOUSLY APPROVED — daily production runbook

One run = one long video (10–12 min, 1920×1080) + 6 vertical Shorts (45–65 s, 1080×1920) for ONE US day, uploaded to a `drop-<weekday>` branch and scheduled in Metricool.
Read the Projects doc `claude/seriously-approved-bible.md` first (rules, brand, voice, money). Reference Short: `episodes/000-test-kissing-shield/episode.py`.

## 0. Context
- Metricool brand "SERIOUSLY APPROVED": blogId **7805767**. Publish timezone **America/New_York**.
- Schedule per US day: Shorts 08:00, 10:30, 13:00, 15:00, 19:00, 22:00 ET; long video 16:00 ET.
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
Shorts: `$EP/shorts/s1 … s6/episode.py` with `FMT = "short"`, `NUM`, `HOOK` ("GUESS WHAT|THIS IS [FOR]" style), `HOOK2` (name of the invention), `HOOK_SWITCH` (index of the reveal line), optional `TAIL`. Copy the figures they use into `shorts/sN/fig/`. 45–65 s; any Short meant for TikTok must run > 60 s.
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
for S in $EP/shorts/s*; do python3 $P/tts.py $S && python3 $P/compose.py $S && node $P/render.mjs $S 30 && python3 $P/mix.py $S && bash $P/encode.sh $S $S/short.mp4 95; done
node $P/thumb.mjs $EP        # $EP/thumb.json: variants A and C -> thumb_A.png, thumb_C.png
```

## 7. QA (do not skip)
- Stills every ~8 s (`node render.mjs $EP 30 0 <T> 8`) → contact sheet: nothing clipped, callouts on the right parts, subtitles readable, no front page/addresses.
- Loudness ≈ −14 LUFS (encode.sh prints it). Long ≥ 10:00. Each Short ≤ 3 min.
- Thumbnail at 168×94: the big words still read; bottom-right corner empty.

## 8. Upload (public raw URLs for Metricool)
Branch = weekday of the ET publish date: drop-mon … drop-sun. Orphan commit with only that day's files, force-push:
```bash
cd /home/claude/seriouslyapproved_media && git checkout --orphan up && git rm -rqf . && \
cp $EP/long.mp4 $EP/thumb_A.png . && for i in 1 2 3 4 5 6; do cp $EP/shorts/s$i/short.mp4 s$i.mp4; done && \
git add long.mp4 thumb_A.png s*.mp4 && git -c user.name="SERIOUSLY APPROVED bot" -c user.email="ituraev97@users.noreply.github.com" commit -qm "drop NNN" && \
git push -f origin up:drop-XXX && git checkout -q main && git branch -D up
```
URL: `https://raw.githubusercontent.com/ituraev97/seriouslyapproved_media/drop-XXX/<file>`; check each with `curl -sI` (200).

## 9. Schedule in Metricool
- createScheduledPost, blogId 7805767, providers [{"network":"youtube"}], publicationDate {dateTime, timezone:"America/New_York"}, autoPublish true.
- Long: youtubeData {title, type:"video", privacy:"public", tags, category:"ENTERTAINMENT", madeForKids:false}; text = description; media [long.mp4 URL]; videoThumbnailUrl = thumb_A URL.
- Shorts: youtubeData {title, type:"short", privacy:"public", category:"ENTERTAINMENT", madeForKids:false}; text = Short description.
- TikTok / Instagram: only once connected to the brand (none on 02.11.2026). TikTok: only Shorts > 60 s.
- Titles: long ≤ 70 chars, curiosity + "Real Patents" (e.g. "9 Real Patents Nobody Asked For (All Approved)"); Short = the invention + a hook ("The U.S. Approved a Kissing Shield").
- Long description: 2-line summary · chapters with timestamps (chapter shot starts from timeline.json, first = 0:00) · "Patents in this video:" one line each (number, title, year, Google Patents link) · "SERIOUSLY APPROVED is an independent channel and is not affiliated with or endorsed by the USPTO. Patent texts and drawings: U.S. patents (public record)." · hashtags `#weirdpatents #inventions #weirdhistory #patents #strangeinventions #history`.
- Short description: one line + "US <number> (<year>) — <Google Patents link>" + "Full episode on the channel." + `#weirdpatents #inventions #shorts #patents #weirdhistory #funnyinventions`.

## 10. Close the run
- Commit to main: `episodes/NNN-slug/` (episode.py, shorts/*/episode.py, fig/*.svg, sources.md, thumb.json, description.txt — never video, audio or scans), `topics.md` row → `done YYYY-MM-DD`, `used_patents.json` (+ numbers used).
- Message the owner in Russian: title, publish times (ET and Tashkent), patents used, thumb_C attached for Test & Compare, anything needing attention.
