# Manim Visuals

Create beautiful mathematical animations like 3Blue1Brown using Manim!

## Project Structure

```
manim-visuals/
├── serve.py              # Web server for live preview
├── tools/                # Development tools
│   ├── watch.py         # File watcher for auto-rendering
│   └── viewer.html      # Auto-refreshing browser viewer
├── projects/            # Your animation projects
│   └── basic-shapes/   # Example project
│       └── test_scene.py
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
python serve.py basic-shapes test_scene SquareToCircle
```
Opens a browser that auto-refreshes. Arguments: `[project] [file] [scene]`

**Terminal 2 - File Watcher:**
```bash
conda activate manim
python tools/watch.py projects/basic-shapes/test_scene.py SquareToCircle
```
Watches for file changes and automatically re-renders.

**Terminal 3 - Code Editor:**
```bash
vim projects/basic-shapes/test_scene.py  # or your preferred editor
```

**Workflow:** Save your code → Watcher auto-renders → Browser auto-refreshes!

### 3. Single Render (No Live Preview)

```bash
conda activate manim
manim -pql projects/basic-shapes/test_scene.py SquareToCircle
```

**Quality Flags:**
- `-ql` = Low quality (480p, fast)
- `-qm` = Medium quality (720p)
- `-qh` = High quality (1080p)
- `-qk` = 4K quality

**Other Flags:**
- `-p` = Preview (automatically open video)
- `-s` = Save last frame as image

## Creating a New Project

### 1. Create Project Folder

```bash
mkdir -p projects/my-project
cd projects/my-project
```

### 2. Create Your Animation File

```python
# projects/my-project/animations.py
from manim import *

class MyFirstAnimation(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(Create(circle))
        self.wait(1)
```

### 3. Run Live Development

```bash
# Terminal 1
python serve.py my-project animations MyFirstAnimation

# Terminal 2
python tools/watch.py projects/my-project/animations.py MyFirstAnimation
```

## Example Scenes

Located in `projects/basic-shapes/test_scene.py`:

1. **SquareToCircle** - Basic shape transformation
2. **TextExample** - Text animations with color changes
3. **MathEquation** - LaTeX mathematical equations

```bash
# Render different scenes
manim -pql projects/basic-shapes/test_scene.py TextExample
manim -pql projects/basic-shapes/test_scene.py MathEquation

# Or use live development
python serve.py basic-shapes test_scene TextExample
python tools/watch.py projects/basic-shapes/test_scene.py TextExample
```

## Creating Animations

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

- **projects/**: Each folder is a separate project
  - Example: `projects/basic-shapes/`, `projects/math-explained/`, etc.
  - Keeps your work organized and separate
- **tools/**: Helper scripts for development
- **media/**: Auto-generated render output (gitignored)

## Tips

1. Start with **low quality** (`-ql`) for fast iteration during development
2. Use `self.wait(duration)` to pause between animations
3. Chain animations: `self.play(anim1, anim2)` runs them simultaneously
4. Use raw strings for LaTeX: `r"\frac{1}{2}"`
5. Check rendered videos in `media/videos/projects/[project-name]/`

## Resources

- [Manim Community Documentation](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [3Blue1Brown Channel](https://www.youtube.com/c/3blue1brown)
- [Manim Tutorial](https://docs.manim.community/en/stable/tutorials.html)

## License

MIT

---

Have fun creating beautiful mathematical animations! 🎨🚀
