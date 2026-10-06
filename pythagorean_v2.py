from manimlib import *

class PythagoreanTheoremV2(Scene):
    def construct(self):
        self.camera.background_color = "#0b1020"

        title = Text("Why does  a^2 + b^2 = c^2 ?", font_size=58)
        title.set_color_by_gradient("#7dd3fc", "#c4b5fd")
        sub = Text("A visual proof of the Pythagorean theorem", font_size=30)
        sub.set_color("#cbd5e1")
        sub.next_to(title, DOWN, buff=0.22)
        self.play(Write(title), FadeIn(sub, shift=UP*0.15), run_time=1.5)
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(sub), run_time=0.6)

        # 3-4-5 triangle
        A = LEFT*3.0 + DOWN*1.8
        B = RIGHT*3.0 + DOWN*1.8
        C = LEFT*3.0 + UP*2.2
        tri = Polygon(A, B, C, stroke_width=6)
        tri.set_fill("#1e3a5f", opacity=0.45)
        tri.set_color("#e2e8f0")
        la = Text("a = 3", font_size=34).next_to((A+C)/2, LEFT, buff=0.25)
        lb = Text("b = 4", font_size=34).next_to((A+B)/2, DOWN, buff=0.25)
        lc = Text("c = 5", font_size=34).next_to((C+B)/2, RIGHT*0.35 + UP*0.05, buff=0.25)
        ra = Polygon(A+RIGHT*0.32, A+RIGHT*0.32+UP*0.32, A+UP*0.32, stroke_width=3)
        self.play(ShowCreation(tri), FadeIn(ra), Write(la), Write(lb), Write(lc), run_time=1.6)
        self.wait(1.2)

        # squares on sides
        sq_a = Polygon(A, C, C+LEFT*2.4, A+LEFT*2.4)
        sq_b = Polygon(A, B, B+DOWN*2.4, A+DOWN*2.4)
        # construct c-square outward using vector rotation
        v = B-C
        perp = np.array([v[1], -v[0], 0.0])
        perp = perp / np.linalg.norm(perp) * 4.0
        sq_c = Polygon(C, B, B+perp, C+perp)
        for sq in [sq_a, sq_b, sq_c]:
            sq.set_fill(opacity=0.22)
            sq.set_stroke(width=5)
        sq_a.set_color("#38bdf8")
        sq_b.set_color("#a78bfa")
        sq_c.set_color("#fbbf24")
        ta = Text("a^2 = 9", font_size=32).move_to(A*0.55 + C*0.45 + LEFT*1.15)
        tb = Text("b^2 = 16", font_size=32).move_to((A+B)/2 + DOWN*1.15)
        tc = Text("c^2 = 25", font_size=34).move_to((C+B)/2 + perp*0.55)
        self.play(ShowCreation(sq_a), ShowCreation(sq_b), ShowCreation(sq_c), run_time=1.5)
        self.play(FadeIn(ta), FadeIn(tb), FadeIn(tc), run_time=0.8)
        self.wait(1.2)

        check = Text("9 + 16 = 25", font_size=48)
        check.set_color("#f8fafc")
        check.to_edge(UP, buff=0.45)
        self.play(Write(check), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(VGroup(tri, ra, la, lb, lc, sq_a, sq_b, sq_c, ta, tb, tc, check)), run_time=0.7)

        # General proof: four triangles inside a large square
        header = Text("Now make the argument general", font_size=42)
        header.set_color("#c4b5fd")
        header.to_edge(UP, buff=0.4)
        self.play(Write(header), run_time=0.8)

        s = 5.4
        big = Square(side_length=s)
        big.set_stroke("#e2e8f0", width=5)
        big.set_fill("#111827", opacity=0.55)
        big.move_to(DOWN*0.15)

        # Four congruent right triangles arranged around a central c-square.
        p = s/2
        a = 1.65
        b = s-a
        # corners of big square
        TL = big.get_corner(UL); TR = big.get_corner(UR)
        BR = big.get_corner(DR); BL = big.get_corner(DL)
        P1 = TL + RIGHT*a
        P2 = TR + DOWN*a
        P3 = BR + LEFT*a
        P4 = BL + UP*a
        t1 = Polygon(TL, P1, TR)
        t2 = Polygon(TR, P2, BR)
        t3 = Polygon(BR, P3, BL)
        t4 = Polygon(BL, P4, TL)
        tris = VGroup(t1,t2,t3,t4)
        for t in tris:
            t.set_fill("#2563eb", opacity=0.32)
            t.set_stroke("#60a5fa", width=3)

        # center square using intersections: visually represented by a rotated square
        center = Square(side_length=2.34)
        center.rotate(PI/4)
        center.move_to(big.get_center())
        center.set_fill("#fbbf24", opacity=0.18)
        center.set_stroke("#fbbf24", width=4)

        self.play(ShowCreation(big), LaggedStart(*[ShowCreation(t) for t in tris], lag_ratio=0.12), run_time=2)
        self.play(ShowCreation(center), run_time=0.8)
        center_label = Text("center area = c^2", font_size=34)
        center_label.set_color("#fde68a").move_to(center.get_center())
        self.play(FadeIn(center_label, scale=0.8), run_time=0.7)
        self.wait(1.5)

        eq1 = Text("(a + b)^2  =  a^2 + 2ab + b^2", font_size=40)
        eq1.set_color("#e2e8f0").to_edge(DOWN, buff=0.45)
        self.play(Write(eq1), run_time=1.0)
        self.wait(1.5)

        eq2 = Text("large square  =  4 triangles  +  center square", font_size=31)
        eq2.set_color("#94a3b8").next_to(header, DOWN, buff=0.35)
        self.play(Write(eq2), run_time=0.9)
        self.wait(1.4)

        eq3 = Text("a^2 + 2ab + b^2  =  c^2 + 2ab", font_size=40)
        eq3.set_color("#f8fafc").move_to(eq1)
        self.play(Transform(eq1, eq3), run_time=0.9)
        self.wait(1.3)

        cancel = Text("2ab cancels", font_size=34)
        cancel.set_color("#fb7185").next_to(eq3, UP, buff=0.35)
        self.play(Write(cancel), run_time=0.7)
        self.wait(1.0)

        final = Text("a^2 + b^2 = c^2", font_size=64)
        final.set_color_by_gradient("#38bdf8", "#fbbf24")
        final.move_to(ORIGIN + DOWN*0.15)
        box = SurroundingRectangle(final, buff=0.25, stroke_width=4)
        box.set_color("#fbbf24")
        self.play(FadeOut(eq2), FadeOut(cancel), FadeOut(header), FadeOut(eq3),
                  Transform(center_label, Text("c^2", font_size=34).set_color("#fde68a").move_to(center.get_center())),
                  run_time=0.7)
        self.play(Write(final), ShowCreation(box), run_time=1.0)
        self.wait(2.5)
        outro = Text("The geometry makes the equation inevitable.", font_size=31)
        outro.set_color("#cbd5e1").next_to(final, DOWN, buff=0.35)
        self.play(FadeIn(outro, shift=UP*0.15), run_time=0.7)
        self.wait(2.0)
