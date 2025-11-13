# Manim Visuals

Create beautiful mathematical animations like 3Blue1Brown using Manim!

## Project Structure

```
manim-visuals/
├── serve.py              # Web server for live preview
├── tools/                # Development tools
│   ├── watch.py         # File watcher for auto-rendering
│   └── viewer.html      # Auto-refreshing browser viewer
├── examples/            # Example animations
│   └── test_scene.py   # Sample scenes (SquareToCircle, TextExample, MathEquation)
├── projects/            # Your animation projects go here
└── media/              # Rendered videos (auto-generated, gitignored)
```

## Quick Start

### 1. Setup (one time)

```bash
# Clone the repository
git clone git@github.com:hariship/manim-visuals.git
cd manim-visuals

# Create conda environment
conda create -n manim python=3.11 -y
conda activate manim

# Install Manim
pip install manim
```

### 2. Live Development Workflow

**Terminal 1 - Web Server:**
```bash
python serve.py
```
Opens a browser that auto-refreshes when animations are re-rendered.

**Terminal 2 - File Watcher:**
```bash
conda activate manim
python tools/watch.py examples/test_scene.py SquareToCircle
```
Watches for file changes and automatically re-renders.

**Terminal 3 - Code Editor:**
```bash
vim examples/test_scene.py  # or your preferred editor
```

**Workflow:** Save your code → Watcher auto-renders → Browser auto-refreshes!

### 3. Single Render (No Live Preview)

```bash
conda activate manim
manim -pql examples/test_scene.py SquareToCircle
```

**Quality Flags:**
- `-ql` = Low quality (480p, fast)
- `-qm` = Medium quality (720p)
- `-qh` = High quality (1080p)
- `-qk` = 4K quality

**Other Flags:**
- `-p` = Preview (automatically open video)
- `-s` = Save last frame as image

## Example Scenes

Located in `examples/test_scene.py`:

1. **SquareToCircle** - Basic shape transformation
2. **TextExample** - Text animations with color changes
3. **MathEquation** - LaTeX mathematical equations

```bash
# Render different scenes
manim -pql examples/test_scene.py TextExample
manim -pql examples/test_scene.py MathEquation
```

## Creating Your Own Animations

### Basic Scene Structure

```python
from manim import *

class MyAnimation(Scene):
    def construct(self):
        # Your animation code here
        circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(Create(circle))
        self.wait(1)
```

### Common Objects

```python
Circle(color=RED, radius=1)
Square(color=BLUE, side_length=2)
Text("Your text", font_size=48)
MathTex(r"e^{i\pi} + 1 = 0")
```

### Common Animations

```python
self.play(Create(object))           # Draw the object
self.play(Write(text))              # Write text/math
self.play(Transform(obj1, obj2))    # Morph obj1 into obj2
self.play(FadeIn(object))           # Fade in
self.play(FadeOut(object))          # Fade out
self.play(object.animate.rotate(PI)) # Animate rotation
self.play(object.animate.scale(2))   # Animate scaling
```

### Available Colors

```python
RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK, TEAL, GOLD, WHITE, BLACK
```

## Project Organization

- **examples/**: Pre-built example animations for learning
- **projects/**: Create your own project folders here
- **tools/**: Helper scripts for development
- **media/**: Auto-generated render output (gitignored)

## Tips

1. Start with **low quality** (`-ql`) for fast iteration during development
2. Use `self.wait(duration)` to pause between animations
3. Chain animations: `self.play(anim1, anim2)` runs them simultaneously
4. Use raw strings for LaTeX: `r"\frac{1}{2}"`
5. Check rendered videos in `media/videos/`

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [3Blue1Brown Channel](https://www.youtube.com/c/3blue1brown)
- [Manim Tutorial](https://docs.manim.community/en/stable/tutorials.html)

## License

MIT

---

Have fun creating beautiful mathematical animations! 🎨🚀
