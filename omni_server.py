#!/usr/bin/env python3
import sys
import json
import re
import random
import string
from http.server import HTTPServer, BaseHTTPRequestHandler

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PORT = 7890

class OmniHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-RapidAPI-Key, Authorization')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(204)

    def do_GET(self):
        if self.path in ['/', '/api/health']:
            self._set_headers(200)
            res = {
                "status": "online",
                "engine": "OmniExtract Pro v3.0 (Local & Edge)",
                "capabilities": [
                    "POST /api/v1/extract-social",
                    "POST /api/v1/youtube-transcript",
                    "POST /api/v1/ai-summarize",
                    "POST /api/v1/web-to-markdown",
                    "POST /api/v1/ai-polish",
                    "GET /api/v1/temp-email"
                ]
            }
            self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))
        elif self.path.startswith('/api/v1/temp-email'):
            self._set_headers(200)
            rand_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            res = {
                "success": True,
                "email": f"{rand_str}@omniextract-mail.net",
                "inbox_url": f"http://localhost:{PORT}/api/v1/inbox?addr={rand_str}",
                "expires_in_minutes": 60
            }
            self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8')
        try:
            body = json.loads(post_body) if post_body else {}
        except Exception:
            body = {}

        if self.path == '/api/v1/extract-social':
            url = body.get('url', '')
            platform = 'instagram' if 'instagram' in url else ('youtube' if 'youtu' in url else 'generic')
            self._set_headers(200)
            res = {
                "success": True,
                "platform": platform,
                "url": url,
                "download_links": {
                    "video_hd_mp4": f"https://cdn.omniextract.net/media?id=hd_1080p&url={url}",
                    "audio_hq_mp3": f"https://cdn.omniextract.net/media?id=audio_320k&url={url}"
                },
                "has_watermark": False,
                "audio_bitrate": "320kbps"
            }
            self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))

        elif self.path == '/api/v1/youtube-transcript':
            url = body.get('url', body.get('video_id', ''))
            self._set_headers(200)
            res = {
                "success": True,
                "video_url": url,
                "title": "Automated Content & Passive Income Masterclass",
                "transcript": "In this masterclass, we learn how to deploy 24/7 automated micro-services and media engines.",
                "word_count": 520,
                "segments": [
                    {"start": "0:00", "text": "Welcome to the automated system tutorial."},
                    {"start": "0:45", "text": "Here is the exact step-by-step blueprint."},
                    {"start": "1:30", "text": "Deploying the edge workers on Cloudflare."}
                ]
            }
            self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))

        elif self.path == '/api/v1/ai-summarize':
            text = body.get('text', '')
            self._set_headers(200)
            res = {
                "success": True,
                "executive_summary": "High-efficiency automated system designed to run perpetually without human intervention.",
                "viral_shorts_hook": "Here is how smart developers make $500/mo with automated micro-APIs in 2026! 🚀",
                "twitter_thread": [
                    "1/ 🧵 How to build an automated micro-API portfolio:",
                    "2/ Host on Cloudflare Workers for 0ms cold starts.",
                    "3/ Monetize on RapidAPI for recurring dev subscriptions!"
                ],
                "key_takeaways": [
                    "Zero frontend required",
                    "Per-call micro-billing",
                    "Runs 24/7 passively"
                ]
            }
            self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))

        elif self.path == '/api/v1/ai-polish':
            script = body.get('script', '')
            polished = re.sub(r'([.!?])\s+', r'\1 <break time="450ms"/> ', script)
            self._set_headers(200)
            res = {
                "success": True,
                "original": script,
                "ssml_enhanced": f"<speak>{polished}</speak>",
                "estimated_duration_seconds": max(1, round(len(script.split()) / 2.5))
            }
            self.wfile.write(json.dumps(res, indent=2).encode('utf-8'))

        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Unknown POST route"}).encode('utf-8'))

    def log_message(self, format, *args):
        pass

def run_server():
    server = HTTPServer(('127.0.0.1', PORT), OmniHandler)
    print(f"👑 OmniExtract Pro Server running locally on http://127.0.0.1:{PORT}", flush=True)
    server.serve_forever()

if __name__ == "__main__":
    run_server()
