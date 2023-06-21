

from manim import *

class MainRes(Scene):
    def construct(self):
        sect = Tex(r"Section-3", font_size=48, color = BLUE)
        rect = Rectangle(width=sect.width + 0.5, height=1.0, stroke_color=RED, fill_opacity=0)
        self.play(Write(sect),Create(rect))
        self.play(FadeOut(sect),FadeOut(rect))
        
        tit2 = Tex(r"Main Result", font_size=48, color = BLUE)
        tit2.to_edge(UP)
        rec3 = Rectangle(width=tit2.width + 0.5, height=1.0, stroke_color=RED, fill_color=RED, fill_opacity=0.2)
        rec3.move_to(tit2.get_center())
        self.play(Write(tit2),Create(rec3))
        # self.play(FadeOut(tit), FadeOut(rect2))

        nest = Tex(r"Nested Algorithim With Source Codes",font_size = 38,color=YELLOW)
        nest.move_to( UP * 2 + LEFT * 5)
        self.play(Write(nest))
        self.wait(2)
        
        first = Tex(r"$min|(\prod _{Xj\ \in S_{1}{}_{1}{}_{r}}) - \frac{1}{2}|$")
        rec4 = Rectangle(width=first.width + 0.5, height=1.0, stroke_color=YELLOW,  )
        rec4.move_to(first.get_center())
        self.play(Write(first),Create(rec4))
        # self.play(Write(first))
        # first.next_to(nest, DOWN, buff=0.5)
        self.wait(5)
        self.play(FadeOut(nest), FadeOut(rec3),FadeOut(tit2),FadeOut(first),FadeOut(rec4))