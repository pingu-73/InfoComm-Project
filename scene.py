from manim import *

# Opening Playcard Type-1
from manim import *

class Intro(Scene):
    def construct(self):
        title = Tex(r"Group Theory with Prior Statistics", font_size=48)
        self.play(Write(title))
        self.wait()

        ResPapby = Tex(r"Research Paper by: Tongxin Li, Chun Lam, Wenhao Huang, Tarik Kaced and Sidharth Jaggi", font_size=30)
        ResPapby.next_to(title, DOWN, buff=0.5)
        self.play(Write(ResPapby))
        self.wait(2)
        self.play(FadeOut(ResPapby))
                  
        byok = Tex(r"Explained by: Dikshant(2022102038) \& Akshat Tiwari(2022102043)", font_size=38)
        byok.next_to(title, DOWN, buff=0.5)
        self.play(Write(byok))
        self.wait()
        self.play(FadeOut(byok), FadeOut(title))
        self.wait(3)



# square and groups
class Slide2(Scene):
    def construct(self):
        big_square = Square(side_length=3, color=BLUE)
#         self.play(Create(big_square))
#         self.wait()

        grid_lines = VGroup(*[
            Line(start=big_square.get_corner(DL) + RIGHT * i, end=big_square.get_corner(UL) + RIGHT * i)
            for i in range(1, 3)
        ] + [
            Line(start=big_square.get_corner(DL) + UP * i, end=big_square.get_corner(DR) + UP * i)
            for i in range(1, 3)
        ])

#         self.play(Create(grid_lines))
        self.wait()

        labels = VGroup()
        for j in range(1, 4):
            for i in range(1, 4):
                if i == 2 and j == 3:
                    label = MathTex(f"P_{{ {i} {j} }}", color=ORANGE)
                else:
                    label = MathTex(f"P_{{ {i} {j} }}")
                label.move_to(big_square.get_corner(UL) + DOWN * (i - 0.5) + RIGHT * (j - 0.5))
                labels.add(label)

#         self.play(Create(labels))
#         self.wait(2)
        
        scene_group = VGroup(big_square, grid_lines, labels)
        self.play(Create(scene_group))
        self.wait(2)

        scene_group.generate_target()
        scene_group.target.shift(5 * LEFT+ 1.5 * UP)
        self.play(MoveToTarget(scene_group))
        self.wait()
# --------------------------------------------------------------------------------------------

        oval_1 = Ellipse(height=2, width=3.5, color=YELLOW)
        oval_1.next_to(big_square, RIGHT, buff=1)

        group_label_1 = MathTex("Group 1")
        group_label_1.next_to(oval_1, UP, buff=0.1)

        p11 = MathTex("P_{11}")
        p11.move_to(oval_1.get_center() + UP * 0.6 + LEFT * 0.6)

        p12 = MathTex("P_{12}")
        p12.move_to(oval_1.get_center() + UP * 0.6 + RIGHT * 0.6)

        p13 = MathTex("P_{13}")
        p13.move_to(oval_1.get_center() + DOWN * 0.6)

#         self.play(Create(oval_1), Write(group_label_1), Write(p11), Write(p12), Write(p13))
#         self.wait(1)
        
        
        scene_group1 = VGroup(oval_1, group_label_1, p11, p12, p13)
        self.play(Create(scene_group1))
        self.wait()
        
#         --------------------------------------------------------------

        oval_2 = Ellipse(height=2, width=3.5, color=RED)
        oval_2.next_to(oval_1, DOWN, buff=1)

        group_label_2 = MathTex("Group 2")
        group_label_2.next_to(oval_2, UP, buff=0.1)

        p21 = MathTex("P_{21}")
        p21.move_to(oval_2.get_center() + UP * 0.6 + LEFT * 0.6)

        p22 = MathTex("P_{22}")
        p22.move_to(oval_2.get_center() + UP * 0.6 + RIGHT * 0.6)

        p23 = MathTex("P_{23}", color=ORANGE)
        p23.move_to(oval_2.get_center() + DOWN * 0.6)

#         self.play(Create(oval_2), Write(group_label_2), Write(p21), Write(p22), Write(p23))
#         self.wait(2)
        
        scene_group2 = VGroup(oval_2, group_label_2, p21, p22, p23)
        self.play(Create(scene_group2))
        self.wait()
#         --------------------------------------------------------------------------------------
        
        oval_3 = Ellipse(height=2, width=3.5, color=GREEN)
        oval_3.next_to(oval_2, RIGHT, buff=1)

        group_label_3 = MathTex("Group 3")
        group_label_3.next_to(oval_3, UP, buff=0.1)

        p31 = MathTex("P_{31}")
        p31.move_to(oval_3.get_center() + UP * 0.6 + LEFT * 0.6)

        p32 = MathTex("P_{32}")
        p32.move_to(oval_3.get_center() + UP * 0.6 + RIGHT * 0.6)

        p33 = MathTex("P_{33}")
        p33.move_to(oval_3.get_center() + DOWN * 0.6)

#         self.play(Create(oval_3), Write(group_label_3), Write(p31), Write(p32), Write(p33))
#         self.wait(2)
        
        scene_group3 = VGroup(oval_3, group_label_3, p31, p32, p33)
        self.play(Create(scene_group3))
        self.wait(2)
#        --------------------------------------------------------------------------------------
        
        self.play(FadeOut(scene_group1), FadeOut(scene_group3))
        self.wait()
        
        
#         ------------------------------------------------------------------------------------
        scene_group2.generate_target()
        scene_group2.target.shift(1.9 * UP+0.5* RIGHT)
        self.play(MoveToTarget(scene_group2))
        self.wait()



class MainScene(Scene):
    def constructor(self):
        intro_scene = Intro()
        slide2_scene = Slide2()

        self.play(AnimationGroup(intro_scene, slide2_scene))

# Run the Manim script
if __name__ == "__main__":
    scene = MainScene()
    scene.render()
