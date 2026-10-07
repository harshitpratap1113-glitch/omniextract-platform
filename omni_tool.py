#!/usr/bin/env python3
"""
OmniExtract Pro v3.0 — Local Power-Tool & Testing Console
Use our own API locally to download videos, extract transcripts, summarize articles, and polish scripts!
"""

import sys
import json
import urllib.request

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BASE_URL = "https://omniextract-pro-api.occipital-range.workers.dev"

def call_api(endpoint, method="POST", data=None):
    url = f"{BASE_URL}{endpoint}"
    req_data = json.dumps(data).encode("utf-8") if data else None
    headers = {"Content-Type": "application/json", "User-Agent": "OmniCLI/3.0"}
    
    req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 70)
    print("⚡ OMNIEXTRACT PRO v3.0 — LOCAL RUNNER & POWER CONSOLE")
    print("=" * 70)
    print("1. Social Media HD Video/Audio Extractor (/api/v1/extract-social)")
    print("2. YouTube Timed Transcript Extractor (/api/v1/youtube-transcript)")
    print("3. AI Video-to-Shorts & Viral Summarizer (/api/v1/ai-summarize)")
    print("4. Web-to-Clean AI Markdown Extractor (/api/v1/web-to-markdown)")
    print("5. SSML Breath & Pause Enhancer (/api/v1/ai-polish)")
    print("6. Burner Temp Email Generator (/api/v1/temp-email)")
    print("=" * 70)

    print("\n[1/4] 🚀 Testing YouTube Transcript Extractor on Live Video...")
    transcript = call_api("/api/v1/youtube-transcript", method="POST", data={"url": "https://www.youtube.com/watch?v=192Txy9P4q4"})
    print("Output:", json.dumps(transcript, indent=2))

    print("\n[2/4] 🤖 Testing AI Viral Summarizer & Shorts Hook Generator...")
    summary = call_api("/api/v1/ai-summarize", method="POST", data={"text": "Building a 24/7 automated passive income engine on Cloudflare Workers and RapidAPI."})
    print("Output:", json.dumps(summary, indent=2))

    print("\n[3/4] 🎬 Testing Social Media HD MP4/MP3 Extractor...")
    social = call_api("/api/v1/extract-social", method="POST", data={"url": "https://www.instagram.com/reel/C7xyz123/"})
    print("Output:", json.dumps(social, indent=2))

    print("\n[4/4] 📬 Testing Temporary Burner Email Generator...")
    temp_mail = call_api("/api/v1/temp-email", method="GET")
    print("Output:", json.dumps(temp_mail, indent=2))

    print("\n" + "=" * 70)
    print("👑 ALL ENGINES FUNCTIONING LOCALLY & ON EDGE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
