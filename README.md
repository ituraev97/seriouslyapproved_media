# SERIOUSLY APPROVED — media & pipeline

Real patents. Somehow approved. The weirdest real U.S. patents, explained with a straight face. Independent channel, not affiliated with or endorsed by the USPTO.

- `pipeline/` — patent fetch (archive.org USPTO disks) + OCR, figure vectorising, Kokoro narration (voice B), timeline, frame template (Shorts 1080×1920 and long 1920×1080), render, score/SFX mix, encode, thumbnails.
- `episodes/` — scripts (`episode.py`), Shorts, figure SVGs, sources, thumbnail configs, descriptions. No video, audio or scans on `main`.
- `brand/` — logos, avatar, banner, watermark, brand-art source.
- `topics.md` — season plan; `used_patents.json` — never reuse a patent; `disks.json` — archive.org USPTO disk ranges.
- `drop-mon` … `drop-sun` — one day's video files per branch (orphan commit, force-pushed) so Metricool can fetch them by public raw URL.
- `RUNBOOK.md` — the daily run.

Patent texts and drawings: U.S. patents (public record).
