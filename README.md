# Manim Experiments

Create beautiful mathematical animations like 3Blue1Brown!

## Quick Start

### Setup (one time)
```bash
conda activate manim
```

### Live Development Workflow

**Terminal 1 - Web Server:**
```bash
cd ~/Desktop/workspace/personal/manim-experiments
python serve.py
```
This opens a browser that auto-refreshes. Keep it open.

**Terminal 2 - File Watcher:**
```bash
cd ~/Desktop/workspace/personal/manim-experiments
conda activate manim
python watch.py test_scene.py SquareToCircle
```
This watches for file changes and auto-renders.

**Terminal 3 - Code Editor:**
```bash
cd ~/Desktop/workspace/personal/manim-experiments
vim test_scene.py  # or your preferred editor
```

**That's it!** Save your code → Terminal 2 renders → Browser auto-refreshes!

## Alternative: Single Render

If you don't need live preview, just render once:
```bash
conda activate manim
manim -pql test_scene.py SquareToCircle
```

Flags:
- `-p` = Preview (open video)
- `-ql` = Quality Low (fast, 480p)
- `-qm` = Quality Medium (720p)
- `-qh` = Quality High (1080p)

## Available Scenes

1. **SquareToCircle** - Basic shape transformation
2. **TextExample** - Text animations
3. **MathEquation** - LaTeX math rendering

```bash
# Render different scenes
manim -pql test_scene.py TextExample
manim -pql test_scene.py MathEquation
```

## Basic Manim Concepts

### Scene Structure
```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Your animation code here
        pass
```

### Common Objects
```python
Circle()
Square()
Text("Your text")
MathTex(r"\LaTeX math")
```

### Common Animations
```python
self.play(Create(object))          # Draw the object
self.play(Write(text))             # Write text/math
self.play(Transform(obj1, obj2))   # Morph obj1 into obj2
self.play(FadeIn(object))          # Fade in
self.play(object.animate.rotate(PI))  # Animate rotation
```

### Colors
```python
RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK, TEAL, GOLD
```

## File Structure

```
manim-experiments/
├── test_scene.py       # Your animation scenes
├── watch.py           # File watcher for auto-render
├── serve.py           # Web server for browser preview
├── viewer.html        # Auto-refreshing browser viewer
├── README.md          # This file
└── media/            # Rendered videos
    └── videos/
        └── test_scene/
            └── 480p15/
                └── SquareToCircle.mp4
```

## Tips

1. **Start with low quality** (`-ql`) for fast iteration
2. **Use `self.wait()`** to pause and see what's happening
3. **Chain animations**: `self.play(anim1, anim2)` runs them simultaneously
4. **Colors**: All caps like `RED`, `BLUE`, `GREEN`
5. **Math**: Use raw strings `r"\LaTeX"` for equations

## Resources

- [Manim Community Docs](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [3Blue1Brown Videos](https://www.youtube.com/c/3blue1brown)

Have fun creating! 🎨
