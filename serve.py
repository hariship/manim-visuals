#!/usr/bin/env python3
"""
Simple HTTP server for viewing Manim animations with auto-refresh.
Usage: python serve.py [project] [file] [scene]
Example: python serve.py basic-shapes test_scene SquareToCircle
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching so browser always gets fresh video
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Suppress console logs except errors
        if args[1] != '200':
            super().log_message(format, *args)

def main():
    # Get project, file, and scene from command line arguments
    project = sys.argv[1] if len(sys.argv) > 1 else 'basic-shapes'
    file = sys.argv[2] if len(sys.argv) > 2 else 'test_scene'
    scene = sys.argv[3] if len(sys.argv) > 3 else 'SquareToCircle'

    os.chdir(Path(__file__).parent)

    Handler = MyHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        # Build URL with query parameters
        url = f"http://localhost:{PORT}/tools/viewer.html?project={project}&file={file}&scene={scene}"

        print(f"{'='*60}")
        print(f"🌐 Starting web server...")
        print(f"{'='*60}")
        print(f"📁 Project: {project}")
        print(f"📄 File: {file}")
        print(f"🎬 Scene: {scene}")
        print(f"📺 Viewer URL: {url}")
        print(f"🔄 Video will auto-refresh when re-rendered")
        print(f"🛑 Press Ctrl+C to stop")
        print(f"{'='*60}\n")

        # Open browser
        print(f"🌐 Opening browser...\n")
        webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Stopping server. Goodbye!\n")

if __name__ == "__main__":
    main()
