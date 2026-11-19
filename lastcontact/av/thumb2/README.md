# LAST CONTACT thumbnails — SWORN style (owner decision 2026-11-19: "такие же яркие как в SWORN, 2 обложки")
Template copied from ituraev97/sworn_media pipeline/thumb2.js (Anton font, yellow #FFE81A, red #FF2A2A).
Run: `npm i playwright@1` once, then `node thumb2.js spec.json <assetsdir> <outdir>` (launches /usr/bin/google-chrome) → thumb_A.jpg, thumb_B.jpg.
Make exactly 2 per long video:
- A: one strong image (official NTSB photo, else our 3D render with chip "3D RECONSTRUCTION"), split 1 or 0.52 + red number panel
  (a key NTSB number: speed, altitude, minutes, distance), tag "NTSB" / "NTSB UPDATE", line1 = aircraft/case, line2 = "WHAT THE NTSB SAYS"-type line.
- B: question panel {"q":[...]} on the left (an open question, never an answer) + the image on the right; or image + number panel.
- seal:false always. Red circle (circle:{x,y,r}) only on a real detail (contact point, part). Bottom-right 260x90 stays clear.
- Every word must be true per the official sources; no blame words ("pilot error", "did not stop" quotes singled out, "fault"), no victims, no logos.
Examples: example_002.json (Miami 767), example_003.json (Learjet 60), example_004.json (UPS/Copa).
