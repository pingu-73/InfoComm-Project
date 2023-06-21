

from manim import *

class Huffmn(Scene):
    def construct(self):
        self.wait(1)
        
#         sect = Tex(r"Section-2", font_size=48, color = BLUE)
#         rect = Rectangle(width=sect.width + 0.5, height=1.0, stroke_color=RED, fill_opacity=0)
#         self.play(Write(sect),Create(rect))
#         self.play(FadeOut(sect),FadeOut(rect))
        
#         tit = Tex(r"preliminaries", font_size=48, color = BLUE)
#         rect2 = Rectangle(width=tit.width + 0.5, height=1.0, stroke_color=RED, fill_opacity=0)
#         self.play(Write(tit),Create(rect2))
#         self.play(FadeOut(tit), FadeOut(rect2))
        
        square_a = Square(side_length=1, color=YELLOW)
        rectangle_a = Rectangle(width=1, height=0.5, color=BLUE)
        
        square_b = Square(side_length=1, color=YELLOW)
        rectangle_b = Rectangle(width=1, height=0.5, color=BLUE)
        
        square_c = Square(side_length=1, color=YELLOW)
        rectangle_c = Rectangle(width=1, height=0.5, color=BLUE)
        
        square_d = Square(side_length=1, color=YELLOW)
        rectangle_d = Rectangle(width=1, height=0.5, color=BLUE)
        
        label_a = Tex("A").move_to(square_a)
        prob_a = Tex(r"0.5", font_size=22).move_to(rectangle_a)
        
        label_b = Tex("B").move_to(square_b)
        prob_b = Tex(r"0.25", font_size=22).move_to(rectangle_b)
        
        label_c = Tex("C").move_to(square_c)
        prob_c = Tex(r"0.125", font_size=22).move_to(rectangle_c)
        
        label_d = Tex("D").move_to(square_d)
        prob_d = Tex(r"0.125", font_size=22).move_to(rectangle_d)
        
        Square_a = VGroup(square_a, label_a)
        Rect_a = VGroup(rectangle_a, prob_a)
        
        Square_b = VGroup(square_b, label_b)
        Rect_b = VGroup(rectangle_b, prob_b)
        
        Square_c = VGroup(square_c, label_c)
        Rect_c = VGroup(rectangle_c, prob_c)
        
        Square_d = VGroup(square_d, label_d)
        Rect_d = VGroup(rectangle_d, prob_d)
        
        Square_b.next_to(Square_a, RIGHT)
        Rect_b.next_to(Rect_a, RIGHT)
        
        Square_c.next_to(Square_b, RIGHT)
        Rect_c.next_to(Rect_b, RIGHT)
        
        Square_d.next_to(Square_c, RIGHT)
        Rect_d.next_to(Rect_c, RIGHT)
        
        Squares_group = VGroup(Square_a, Square_b, Square_c, Square_d)
        Rect_group = VGroup(Rect_a, Rect_b, Rect_c, Rect_d)
        
        Squares_group.move_to(LEFT * 0.5)
        Rect_group.move_to(LEFT * 0.53 + UP * 0.79)
        
        self.play(Create(Squares_group), Create(Rect_group))
        self.wait(2)
        self.play(FadeOut(Squares_group), FadeOut(Rect_group))
        
        A = VGroup(Square_a, Rect_a)
        B = VGroup(Square_b, Rect_b)
        C = VGroup(Square_c, Rect_c)
        D = VGroup(Square_d, Rect_d)
        
#         first D
        D.move_to(LEFT * 2 + UP * 2.9)
        C.next_to(D, RIGHT)
        B.next_to(C, RIGHT)
        A.next_to(B, RIGHT)
        
#         self.play(Create(D), Create(C),Create(B), Create(A))
        
        line1 = DashedLine(B.get_center(), A.get_center(), dash_length=0.1)
        line1.rotate(np.pi / 2)
        line1.scale(1.5)
        line1.set_color(ORANGE)
        Case1 = VGroup(A,B,C,D,line1)
        self.play(Create(D), Create(C),Create(B), Create(A), Create(line1))
#         self.play(Create(line1))

        
        self.wait(2)
        
#         ------------------------------------------------------------------------------------------------
        
        A1 = VGroup(Square_a.copy(), Rect_a.copy())
        B1 = VGroup(Square_b.copy(), Rect_b.copy())
        C1 = VGroup(Square_c.copy(), Rect_c.copy())
        D1 = VGroup(Square_d.copy(), Rect_d.copy())

        D1.move_to(UP*0.9 + LEFT * 3)
        C1.next_to(D1, RIGHT)
        B1.next_to(C1, RIGHT)
        A1.next_to(B1, RIGHT, buff=1.9)

        line2 = DashedLine(C1.get_center(), B1.get_center(), dash_length=0.1)
        line2.rotate(np.pi / 2)
        line2.scale(1.5)
        line2.set_color(ORANGE)
        Case2 = VGroup(A1,B1,C1,D1,line2)
        
        self.play(Create(Case2))
#         self.play(FadeOut(Case1))
        self.wait(2)
    
    
    
#     ----------------------------------------------------------------------------------------------


#         A2 = VGroup(Square_a.copy(), Rect_a.copy())
        B2 = VGroup(Square_b.copy(), Rect_b.copy())
        C2 = VGroup(Square_c.copy(), Rect_c.copy())
        D2 = VGroup(Square_d.copy(), Rect_d.copy())

        D2.move_to(DOWN*1.0 + LEFT * 3.5)
        C2.next_to(D2, RIGHT)
#         B2.next_to(C1, RIGHT)
        B2.next_to(C2, RIGHT, buff=2.0)

        line3 = DashedLine(D2.get_center(), C2.get_center(), dash_length=0.1)
        line3.rotate(np.pi / 2)
        line3.scale(1.5)
        line3.set_color(ORANGE)
        Case3 = VGroup(B2,C2,D2,line3)
        
        self.play(Create(Case3))
#         self.play(FadeOut(Case1))
        self.wait(2)

    
#     ---------------------------------------------------------------------------------

#         B3 = VGroup(Square_b.copy(), Rect_b.copy())
        C3 = VGroup(Square_c.copy(), Rect_c.copy())
        D3 = VGroup(Square_d.copy(), Rect_d.copy())

        D3.move_to(DOWN*2.9 + LEFT * 3.9)
        C3.next_to(D3, RIGHT)
#         B2.next_to(C1, RIGHT)
        C3.next_to(D3, RIGHT, buff=1.6)

#         line4 = DashedLine(D2.get_center(), C2.get_center(), dash_length=0.1)
#         line4.rotate(np.pi / 2)
#         line4.scale(1.5)
#         line4.set_color(ORANGE)
        Case4 = VGroup(C3,D3)
        
        self.play(Create(Case4))
#         self.play(FadeOut(Case1))
        self.wait(2)