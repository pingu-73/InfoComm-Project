from manim import *

class Intro(Scene):
    def introAnime(self):
        title = Text("Group Theory with Prior Statistics", font_size=48)
        self.play(Write(title))
        self.wait(1)

        ResPapby = Text("Tongxin Li, Chun Lam, Wenhao Huang, Tarik Kaced and Sidharth Jaggi", font_size=30)
        self.play(Write(ResPapby))
        by = Text("Dikshant(2022102038) & Akshat Tiwari(2022102043)", font_size=38)
        self.play(Write(by))
        self.wait(1)
        self.play(FadeOut(by), FadeOut(ResPapby), FadeOut(title))
        self.wait(3)


class Overview(Scene):
    def constructor(self):
        # Title
        title = Text("Group Theory with Prior Statistics", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Scene 1: Overview of Group Theory
        scene1_title = Text("Group Theory: An Overview", font_size=36)
        scene1_content = Text("Explain the fundamentals of Group Theory using visuals and animations.")
        self.play(Write(scene1_title))
        self.wait(1)
        self.play(Write(scene1_content))
        self.wait(2)
        self.play(FadeOut(scene1_title), FadeOut(scene1_content))
        self.wait(3)

    def constructor(self):
        # Create the big square
        big_square = Square(side_length=3, color=BLUE)
        self.play(Create(big_square))

        # Divide the big square into three rectangles
        rectangles = VGroup(*[Rectangle(width=1, height=3, color=YELLOW) for _ in range(3)])
        rectangles.arrange(direction=RIGHT, buff=0.1)
        self.play(Create(rectangles))

        # Divide each rectangle into three small squares with labels
        small_squares = VGroup()
        labels = VGroup()
        for rectangle in rectangles:
            square_group = VGroup()
            label_group = VGroup()
            for i in range(3):
                square = Square(side_length=1, color=GREEN)
                label = Tex(f"P{i+1}", color=WHITE).scale(0.5)
                square.next_to(rectangle, UP, buff=0)
                square.shift(i * RIGHT)
                label.next_to(square, DOWN)
                square_group.add(square)
                label_group.add(label)
            small_squares.add(square_group)
            labels.add(label_group)

        self.play(Create(small_squares), Write(labels))
        self.wait(1)


class MainScene(Scene):
    def constructor(self):
        intro_scene = Intro()
        overview_scene = Overview()

        self.play(AnimationGroup(intro_scene, overview_scene))

# Run the Manim script
if __name__ == "__main__":
    scene = MainScene()
    scene.render()
