# LC008 research — 2026-11-25 run (Wed)
## Topic choice
- No fresh U.S. case with enough new official NTSB material for an "update" episode; fallback to a case with a final report, a rich public docket and strong demand.
- Chosen: Southwest Airlines flight 1380 (Boeing 737-7H4 N772SW, CFM56-7B fan blade failure and cabin window loss, 2018-04-17). NTSB final report NTSB/AAR-19/03 (adopted 2019-11-19), docket DCA18MA142 (FDR data with lat/lon/alt/speed/roll/pitch at 1 Hz), NTSB board meeting slides/video (relay clips), DVIDS file footage.
- Demand (YouTube Data API, US/en, last 30 days, order=viewCount; from the 2026-11-23 check): "Southwest 1380 engine" top-15 total 2.20M views, listed there as the next fallback after US Airways 1549.
## Legal/sensitivity handling
- One passenger fatality: no victim details, no names, no seat/photos of the person; cause only as quoted from the NTSB probable cause; "NTSB found/said" attribution on every finding; design intent vs NTSB findings kept separate; "index" (not "rating") for ARFF.
- Thumbnails use NTSB report figures (Fig. 12 replica fragments; Fig. 2 fan assembly diagram), tag "NTSB REPORT".
## QA
- Independent fact-check (separate agent) of all spoken lines → many FIXes applied before TTS; second independent check of on-screen cards, captions, title and thumbnail words → 10 FIXes applied (attribution of recommendations/certification panel, CVR time 11:15:14, FDR fuel-cutoff wording, replica-fragment caption, figure titles, end-card graphic).
- Real material (NTSB figures + NTSB board-meeting clips + DVIDS file footage) ≈ 26% of runtime.
