


from manim import *

class Intro(Scene):
    def construct(self):
        title = Tex(r"Group Theory with Prior Statistics", font_size=48, color = RED)
        self.play(Write(title))
        self.wait()
        rect = Rectangle(width=title.width + 0.5, height=1.0, stroke_color=RED, fill_opacity=0)
#         rect.next_to(title, DOWN, buff=0.5)
        self.play(Create(rect))

        ResPapby = Tex(r"Research Paper by: Tongxin Li, Chun Lam, Wenhao Huang, Tarik Kaced and Sidharth Jaggi", font_size=30)
        ResPapby.next_to(title, DOWN, buff=0.5)
        self.play(Write(ResPapby))
        self.wait()
        self.play(FadeOut(ResPapby))
        
        guided_by = Tex(r"Guided by: Prof. Prasad Krishnan",font_size=38, color = BLUE)
        byok = Tex(r"Explained by: Dikshant(2022102038) \& Akshat Tiwari(2022102043)", font_size=38)
        guided_by.next_to(title, DOWN, buff=0.5)
        byok.next_to(guided_by, DOWN, buff=0.3)
        self.play(Write(byok), Write(guided_by))
        self.wait()
        self.play(FadeOut(byok),FadeOut(rect) ,FadeOut(title),FadeOut(guided_by))
        self.wait(2)