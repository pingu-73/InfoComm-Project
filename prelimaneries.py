


from manim import *

class OvalAroundText(Scene):
    def construct(self):
        sect = Tex(r"Section-2", font_size=48, color = BLUE)
        rect = Rectangle(width=sect.width + 0.5, height=1.0, stroke_color=RED, fill_opacity=0)
        self.play(Write(sect),Create(rect))
        self.play(FadeOut(sect),FadeOut(rect))
        
        tit = Tex(r"preliminaries", font_size=48, color = BLUE)
        tit.to_edge(UP)
        rect2 = Rectangle(width=tit.width + 0.5, height=1.0, stroke_color=RED, fill_color=RED, fill_opacity=0.2)
        rect2.move_to(tit.get_center())
        self.play(Write(tit),Create(rect2))
        # self.play(FadeOut(tit), FadeOut(rect2))

        set_N = Ellipse(height=4, width=2, color=ORANGE)
        x1 = MathTex("X_{1}")
        x2 = MathTex("X_{2}")
        x2.next_to(x1, DOWN, buff=0.5)
        x3 =MathTex(".")
        x3.next_to(x2, DOWN, buff=0.5)
        
        x4 = MathTex(".")
        
        x4.next_to(x3, DOWN, buff=0.5)
        x5 = MathTex("X_{N}")
        x5.next_to(x4, DOWN, buff=0.5)
        
        n=VGroup(x1,x2,x3,x4,x5)
        
        n.move_to(set_N.get_center())
#         oval = Circle(color=WHITE, fill_opacity=0.3).surround(N).scale(1.2)
        SetN = MathTex("Set N")
        SetN.next_to(set_N, DOWN, buff=0.1)
        
        N= VGroup(n,SetN,set_N)
        N.shift(LEFT*5)
#         self.play(Write(n),Write(SetN))
        self.play(Create(N))
        self.wait()

#         ----------------------------------------------------------------------------





        set_X = Ellipse(height=4, width=2, color=GREEN)
        X1 = MathTex("X_{1}")
        X2 = MathTex("X_{2}")
        X2.next_to(X1, DOWN, buff=0.5)
        X3 =MathTex(".")
        X3.next_to(X2, DOWN, buff=0.5)
        X4 = MathTex(".")
        X4.next_to(X3, DOWN, buff=0.5)
        X5 = MathTex("X_{N}")
        X5.next_to(X4, DOWN, buff=0.5)
        
        x=VGroup(X1,X2,X3,X4,X5)
        
        x.move_to(set_X.get_center())
#         oval = Circle(color=WHITE, fill_opacity=0.3).surround(N).scale(1.2)
        SetX = MathTex("Set X")
        SetX.next_to(set_X, DOWN, buff=0.1)
        
        X= VGroup(x,SetX,set_X)
        X.shift(LEFT*2)
#         self.play(Write(n),Write(SetN))

        self.play(Create(X))
        self.wait(2)
        
        rel = Tex(r"$X \in \lbrace0,1\rbrace ^{N}$",color=YELLOW)
#         rel1 = MathTex("\in")
#         rel2 = MathTex("{0,1}^{N}")
        
        rel.move_to( UP * 2 + RIGHT * 5)
        self.play(Write(rel))
        
        pi =Tex(r"$each\ tested\ item X_{i}\  can\ be\ defective\ \newline with\ a\ priori\ probability\ p_{i}$", font_size=26)
        pi.move_to( UP * 1 + RIGHT * 3)
        self.play(Write(pi))
        self.wait(2)
        # self.play(FadeOut(pi),FadeOut(rel),FadeOut(X),FadeOut(N),FadeOut(tit),FadeOut(rect2))
        self.wait(2)

        defin1 = Tex(r"$The\ Univeral\ set\ N\ is\ said\ to\ be\ a\ skewed\ set\ if\ the\ entropy\ \newline of\ the\ population\ vector\ H(X)\ can\ be\ bounded\ by \newline H(X)\ > max(2\mu \ , \gamma^{2} )$", font_size = 26)
        defin1.next_to(pi,DOWN,buff=1)
        defin2 = Tex(r"$p_{i} ^{2} \leq p_{j} ^{2} \forall \  X_{i},X_{j} \in U$")
        defin2.next_to(defin1, DOWN, buff=0.5)
        self.play(Write(defin1))
        self.wait(6)
        self.play(Write(defin2))
        self.wait(4)

        self.play(FadeOut(pi),FadeOut(rel),FadeOut(X),FadeOut(N),FadeOut(tit),FadeOut(rect2),FadeOut(defin1),FadeOut(defin2))