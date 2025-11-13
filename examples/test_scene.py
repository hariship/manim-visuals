from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Simple square
        square = Square(color=BLUE, fill_opacity=0.5, side_length=2)

        # Show the square
        self.play(Create(square))
        self.wait(0.5)

        # Rotate it
        self.play(square.animate.rotate(PI/4).set_color(PURPLE))
        self.wait(0.5)

        # Transform to circle
        circle = Circle(color=RED, fill_opacity=0.5, radius=1)
        self.play(Transform(square, circle))
        self.wait(0.5)

        # Change color
        self.play(square.animate.set_color(YELLOW))
        self.wait(1)


class TextExample(Scene):
    def construct(self):
        # Create text
        text = Text("Hello, Manim!", font_size=60)

        # Animate the text
        self.play(Write(text))
        self.wait(1)

        # Change color
        self.play(text.animate.set_color(YELLOW))
        self.wait(1)


class MathEquation(Scene):
    def construct(self):
        # Create a mathematical equation
        equation = MathTex(r"e^{i\pi} + 1 = 0")

        # Animate the equation
        self.play(Write(equation))
        self.wait(2)

        # Transform to another equation
        equation2 = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        self.play(Transform(equation, equation2))
        self.wait(2)
