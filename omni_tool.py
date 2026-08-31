#!/usr/bin/env python3
"""
👑 OmniExtract Pro — Local Power-Tool & Testing Console
Use our own API locally to download videos, extract transcripts, summarize articles, and polish scripts!
"""

import sys
import json
import urllib.request

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
    print("⚡ OMNIEXTRACT PRO — LOCAL TEST RUNNER & POWER CONSOLE")
    print("=" * 70)
    print("1. Test Social Media HD Video/Audio Extractor")
    print("2. Test YouTube Timed Transcript Extractor")
    print("3. Test AI Video-to-Shorts & Viral Summarizer")
    print("4. Test Web-to-Clean AI Markdown Extractor")
    print("5. Test SSML Breath & Pause Enhancer")
    print("6. Test Burner Temp Email Generator")
    print("=" * 70)

    # Run quick automated verification
    print("\n[1/4] 🚀 Probing Live Cloudflare Edge Health...")
    health = call_api("/api/health", method="GET")
    print("Response:", json.dumps(health, indent=2))

    print("\n[2/4] 🎬 Testing YouTube Transcript Extractor on Live Video...")
    transcript = call_api("/api/v1/youtube-transcript", method="POST", data={"url": "https://www.youtube.com/watch?v=192Txy9P4q4"})
    print("Response:", json.dumps(transcript, indent=2))

    print("\n[3/4] 🤖 Testing AI Viral Summarizer...")
    summary = call_api("/api/v1/ai-summarize", method="POST", data={"text": "Building a 24/7 automated passive income engine."})
    print("Response:", json.dumps(summary, indent=2))

    print("\n[4/4] 📬 Testing Temporary Email Generator...")
    temp_mail = call_api("/api/v1/temp-email", method="GET")
    print("Response:", json.dumps(temp_mail, indent=2))

    print("\n" + "=" * 70)
    print("👑 ALL 4 TESTS EXECUTED ON LIVE CLOUDFLARE EDGE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
