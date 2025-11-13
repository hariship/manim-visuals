#!/usr/bin/env python3
"""
Simple file watcher for Manim that actually works.
Usage: python watch.py test_scene.py SquareToCircle
"""

import sys
import time
import subprocess
import os
from pathlib import Path

def get_file_mtime(filepath):
    """Get the last modification time of a file."""
    try:
        return os.path.getmtime(filepath)
    except:
        return 0

def render(file_path, scene_name):
    """Render the Manim scene."""
    print(f"\n{'='*60}")
    print(f"🎬 Rendering {scene_name}...")
    print(f"{'='*60}\n")

    try:
        cmd = ["manim", "-ql", str(file_path), scene_name]  # Removed -p flag (no auto-preview)
        subprocess.run(cmd, check=True)
        print(f"\n✅ Render complete!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error rendering: {e}\n")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python tools/watch.py <scene_file.py> <SceneName>")
        print("Example: python tools/watch.py examples/test_scene.py SquareToCircle")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.is_absolute():
        file_path = Path.cwd() / file_path

    scene_name = sys.argv[2]

    if not file_path.exists():
        print(f"Error: File {file_path} does not exist!")
        sys.exit(1)

    print(f"{'='*60}")
    print(f"🔍 Watching: {file_path.relative_to(Path.cwd())}")
    print(f"🎯 Scene: {scene_name}")
    print(f"{'='*60}\n")

    # Initial render
    last_mtime = get_file_mtime(file_path)
    render(file_path, scene_name)

    print(f"{'='*60}")
    print("👀 Watching for changes...")
    print("💾 Save your file to trigger re-render")
    print("🛑 Press Ctrl+C to stop")
    print(f"{'='*60}\n")

    render_count = 0
    try:
        while True:
            time.sleep(1)  # Check every second
            current_mtime = get_file_mtime(file_path)

            if current_mtime != last_mtime:
                last_mtime = current_mtime
                render_count += 1
                print(f"\n⚡ Change detected! (#{render_count})")
                time.sleep(0.5)  # Small delay to ensure file is fully written
                render(file_path, scene_name)

    except KeyboardInterrupt:
        print("\n\n👋 Stopping watcher. Goodbye!\n")

if __name__ == "__main__":
    main()
