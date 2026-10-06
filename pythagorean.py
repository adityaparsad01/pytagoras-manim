from manimlib import *

class PythagoreanTheorem(Scene):
    def construct(self):
        title = Text("Why does a² + b² = c²?", font_size=52).to_edge(UP)
        subtitle = Text("A visual proof of the Pythagorean theorem", font_size=30)
        subtitle.next_to(title, DOWN, buff=0.18)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        A = LEFT * 3.2 + DOWN * 2.0
        B = RIGHT * 0.8 + DOWN * 2.0
        C = LEFT * 0.8 + UP * 1.2
        tri = Polygon(A, B, C, stroke_width=5)
        a_line = Line(A, C, stroke_width=4)
        b_line = Line(A, B, stroke_width=4)
        c_line = Line(B, C, stroke_width=4)
        a_label = Text("a = 3", font_size=30).next_to(a_line, LEFT, buff=0.12)
        b_label = Text("b = 4", font_size=30).next_to(b_line, DOWN, buff=0.12)
        c_label = Text("c = 5", font_size=30).next_to(c_line, RIGHT, buff=0.12)
        right_angle = VGroup(
            Line(A + RIGHT*0.35, A + RIGHT*0.35 + UP*0.35),
            Line(A + RIGHT*0.35 + UP*0.35, A + UP*0.35)
        )
        self.play(ShowCreation(tri), ShowCreation(right_angle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        question = Text("What do the squares on the sides tell us?", font_size=34).to_edge(DOWN)
        self.play(Write(question))

        sq_a = Square(side_length=1.35, stroke_width=4).move_to(A + LEFT*0.78 + DOWN*0.68)
        sq_b = Square(side_length=1.8, stroke_width=4).move_to((A+B)/2 + DOWN*1.05)
        sq_c = Square(side_length=2.25, stroke_width=4).move_to((B+C)/2 + RIGHT*0.92)
        lab_a = Text("a² = 9", font_size=28).move_to(sq_a.get_center())
        lab_b = Text("b² = 16", font_size=28).move_to(sq_b.get_center())
        lab_c = Text("c² = 25", font_size=28).move_to(sq_c.get_center())
        self.play(ShowCreation(sq_a), ShowCreation(sq_b), ShowCreation(sq_c),
                  FadeIn(lab_a), FadeIn(lab_b), FadeIn(lab_c))
        self.wait(1)

        equation = Text("9 + 16 = 25", font_size=44).to_edge(DOWN)
        self.play(FadeOut(question), Write(equation))
        self.wait(1.5)

        self.play(FadeOut(tri), FadeOut(right_angle),
                  FadeOut(a_line), FadeOut(b_line), FadeOut(c_line),
                  FadeOut(a_label), FadeOut(b_label), FadeOut(c_label),
                  FadeOut(sq_a), FadeOut(sq_b), FadeOut(sq_c),
                  FadeOut(lab_a), FadeOut(lab_b), FadeOut(lab_c),
                  FadeOut(equation))

        proof_title = Text("Now the general idea", font_size=44).to_edge(UP)
        self.play(Write(proof_title))

        side = 5.2
        big = Square(side_length=side, stroke_width=5).shift(DOWN*0.2)
        center = big.get_center()
        c = 2.45
        center_sq = Square(side_length=c, stroke_width=4).move_to(center)

        tri1 = Polygon(big.get_corner(UL), big.get_corner(UR),
                       center + RIGHT*c/2 + UP*c/2, stroke_width=3)
        tri2 = Polygon(big.get_corner(UR), big.get_corner(DR),
                       center + RIGHT*c/2 - DOWN*c/2, stroke_width=3)
        tri3 = Polygon(big.get_corner(DR), big.get_corner(DL),
                       center - RIGHT*c/2 - DOWN*c/2, stroke_width=3)
        tri4 = Polygon(big.get_corner(DL), big.get_corner(UL),
                       center - RIGHT*c/2 + UP*c/2, stroke_width=3)
        tris = VGroup(tri1, tri2, tri3, tri4)

        self.play(ShowCreation(big))
        self.play(ShowCreation(tris), ShowCreation(center_sq))
        center_label = Text("c²", font_size=42).move_to(center)
        self.play(Write(center_label))

        area_note = Text("Large square area = (a + b)²", font_size=34).to_edge(DOWN)
        self.play(Write(area_note))
        self.wait(1)

        expansion = Text("(a + b)² = a² + 2ab + b²", font_size=40).to_edge(DOWN)
        self.play(Transform(area_note, expansion))
        self.wait(1)

        final_eq = Text("a² + 2ab + b² = c² + 2ab", font_size=38).to_edge(DOWN)
        self.play(Transform(area_note, final_eq))
        self.wait(1)

        result = Text("a² + b² = c²", font_size=58).move_to(DOWN*2.6)
        self.play(FadeOut(tris), FadeOut(big), FadeOut(center_sq),
                  FadeOut(center_label), Transform(area_note, result))
        self.wait(2)

        end = Text("The geometry makes the algebra inevitable.", font_size=32)
        end.next_to(result, DOWN, buff=0.25)
        self.play(Write(end))
        self.wait(2)
