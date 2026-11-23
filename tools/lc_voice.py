#!/usr/bin/env python3
"""LAST CONTACT narration in Chatterbox (voice "lc", owner decision 2026-11-23) via the owner's server. Wraps tools/tts_client.py.

  python3 tools/lc_voice.py request RUN path/to/script.py --creds /tmp/drive_creds.json [--hint "names"]
      Orders every LINES text (id, spoken, pause, speed, visual) as the exact cache file av/mia/tts.py looks for:
      vo/<id>_<md5(text+str(speed)+VOICE+'x1.0')[:8]>.wav (24 kHz). ~3–5 h on the server, so the NEXT run builds it.
  python3 tools/lc_voice.py status RUN --creds ...
  python3 tools/lc_voice.py fetch RUN WORKDIR --creds ...     (WORKDIR = /home/claude/av/mia → writes mia/vo/*.wav)
      Then `python3 tts.py` in WORKDIR finds every file and does not run Kokoro. A line whose text/speed changed after
      `request` gets a new hash → Kokoro voices it (mixed voices) — never edit LINES after ordering.
Keep the VOICE env/default of tts.py unchanged ('am_puck:0.7+am_echo:0.3'): it is part of the cache file name.
"""
import argparse, hashlib, importlib.util, json, os, subprocess, sys, tempfile

VOICE_NAME = "lc"                                                   # reference voice on the server
KOKORO_VOICE = os.environ.get("VOICE", "am_puck:0.7+am_echo:0.3")   # must match av/mia/tts.py
HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["request", "status", "fetch"]); ap.add_argument("run"); ap.add_argument("path", nargs="?")
    ap.add_argument("--creds", default="/tmp/drive_creds.json"); ap.add_argument("--hint", default="")
    a = ap.parse_args()
    client = [sys.executable, os.path.join(HERE, "tts_client.py")]
    if a.cmd == "request":
        spec = importlib.util.spec_from_file_location("script", os.path.abspath(a.path))
        S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
        L = S.LINES
        names = [f"{lid}_" + hashlib.md5((txt + str(spd) + KOKORO_VOICE + "x1.0").encode()).hexdigest()[:8] + ".wav"
                 for lid, txt, pause, spd, vis in L]
        body = {"vo": {"lines": [txt for _, txt, _, _, _ in L], "names": names,
                       "tempos": [round(float(spd), 3) for _, _, _, spd, _ in L], "voice": VOICE_NAME, "sr": 24000}}
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump(body, f); f.close()
        sys.exit(subprocess.call(client + ["request-spec", a.run, f.name, "--creds", a.creds, "--hint", a.hint]))
    if a.cmd == "status":
        sys.exit(subprocess.call(client + ["status", a.run, "--creds", a.creds]))
    sys.exit(subprocess.call(client + ["fetch", a.run, os.path.abspath(a.path), "--creds", a.creds]))

if __name__ == "__main__":
    main()
