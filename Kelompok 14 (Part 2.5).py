from manimlib import *
import numpy as np
import manimlib.utils.color as C

def set_background(self):
    background = Rectangle(
    width = FRAME_WIDTH,
    height = FRAME_HEIGHT,
    stroke_width = 0,
    fill_color = "#000000",
    fill_opacity = 1)
    self.add(background)
    

class a1 (Scene):
    def construct (self):
        set_background(self)
        a=Tex(
            r'u(x,0) \text{ } = X(x) \text{ }',
            r'Y(0)',
            r' \text{ } = \text{ } 0', color=GOLD_A
        )
        a1=Tex(
            r'syarat \text{ } batas \text{ }',
            r'y \text{ } = \text{ } b,',
            r'diperoleh \text{ }',
            r'Y(b) \text{ } = \text{ } 0.', color=YELLOW_C
        )
        a1[2].next_to(a1[0],DOWN)
        a1[3].next_to(a1[1],DOWN)
        a1.next_to(a, DOWN,buff=-1)
        
        
        
        high1=SurroundingRectangle(a1[1], color=TEAL_A, fill_color=TEAL_B,fill_opacity=0.25)
        high2=SurroundingRectangle(a1[3], color=TEAL_A, fill_color=TEAL_B,fill_opacity=0.25)
        play={"run_time":3}
        self.wait(3)
        self.play(ShowCreation(a), **play)
        self.wait()
        self.play(a.move_to,(2*UP))
        self.wait(2)
        bulet=Circle(color=WHITE)
        bulet.surround(a[1],buff=0.075)
        self.play(ShowCreation(bulet))
        self.wait(2)
        self.play(FadeOut(bulet))
        self.wait(3)
        self.play(ShowCreation(a1), **play)
        self.wait()
        self.play(DrawBorderThenFill(high1))
        self.play(DrawBorderThenFill(high2))
        self.wait(5)
        self.play(Uncreate(high1),Uncreate(high2))
        self.play(Uncreate(a1))
        self.play(Uncreate(a))
        
        
class a2 (Scene):
    def construct (self):
        set_background(self)
        b=Text("Solusi umum pers. (1.4b): ", t2c={"pers. (1.4b)":TEAL_A},font_size=36)
        b1=Text("""
            substitusi syarat batas, \n
             diperoleh fungsi eigen
            """, t2c={"fungsi eigen": RED}, font_size=32
        )
        b2=VGroup(
            Tex(r'Y(y)=A \text{ } cos(\sqrt{\lambda y})\text{ }+ \text{ } B \text{ } sin (\sqrt{\lambda y})',color=TEAL_A),
            Tex(r'Y_n(y) \text{ } = \text{ } sin({n\pi \over b}y),',color=RED)
        )
        bn=Text("n = 1,2,3,...", font_size=32, color=RED)
        
        
        self.play(Write(b))
        self.wait(2)
        self.play(b.move_to,(3*UP))
        self.wait(2)
        
        b2[0].next_to(b,DOWN, buff=0.5)
        b1.next_to(b2[0],DOWN,buff=0.5)
        b2[1].next_to(b1,DOWN, buff=0.5)
        bn.next_to(b2[1],DOWN)
        
        self.play(ShowCreation(b2[0]))
        self.wait(3)
        self.play(Write(b1))
        self.wait(2)
        self.play(ShowCreation(b2[1]))
        self.wait(2)
        self.play(Write(bn))
        self.wait(5)
        
        cabut=VGroup(b,b1,b2,bn)
        self.play(FadeOut(cabut, RIGHT))
        
class a3 (Scene):
    def construct (self):
        set_background(self)
        c=Text("Solusi persamaan (1.4a): ", font_size=36, t2c={"persamaan (1.4a)": PINK})
        
        c1=VGroup(
            Tex(r'\lambda_n \text{ } = \text{ } {n^2\pi^2 \over b^2},',color=GOLD_A),
            Tex(r'n \text{ } = \text{ }1,2,3,...',color=GOLD_B),
            Tex(r"X'' \text{ } - \text{ } {n^2\pi^2 \over h^2}X \text{ } = \text{ }0", color=PINK),
            Tex(r'X(x) \text{ } = \text{ } k_1 \text{ }cosh({n\pi x\over b}) \text{ } + \text{ } k_2 \text{ } sinh ({n\pi x\over b})', color=MAROON_A)
        )
        
        nulis={"run_time":3}
        grup=VGroup(c1[0], c1[1]).arrange(DOWN,buff=0.2)
        self.wait(2)
        self.play(ShowCreation(grup),**nulis)
        self.wait(5)
        
        
        self.play(ReplacementTransform(grup, c))
        self.wait(3)
        self.play(c.move_to,(3*UP))
        
        tunjuk=Arrow([0,0,0], [0,-3,0])
        c1[2].next_to(c, DOWN)
        tunjuk.next_to(c1[2], DOWN)
        c1[3].next_to(tunjuk, DOWN, buff=0.5)
        high3=SurroundingRectangle(c1[3],color= YELLOW,buff=0.2)
        
        self.play(ShowCreation(c1[2]), **nulis)
        self.wait(2)
        self.play(GrowArrow(tunjuk))
        self.wait(2)
        self.play(ShowCreation(c1[3]), **nulis)
        self.wait()
        self.play(ShowCreation(high3))
        self.wait(5)
        
        pulang=VGroup(c1[2],c1[3],tunjuk,high3)
        self.play(Uncreate(pulang))
        self.wait()
        self.play(FadeOut(c))
        
class a4 (Scene):
    def construct (self):
        set_background(self)
        d=Text("Solusi Fundamental", font_size=32, color=YELLOW_C)
        d1=VGroup(
            Tex(r'u(0,y) \text{ } = \text{ } 0 &\Leftrightarrow X(0) \text{ }=\text{ }0 \text{ } \\&dan', isolate=["dan"],color=GOLD_A),
            Tex(r'u(a,y) \text{ } = \text{ } f(y) \Leftrightarrow X(a) \text{ }=\text{ }f(y)',color=GOLD_A),
            Tex(r'hasil \text{ } k_1 \text{ } = \text{ } 0'),
            Tex(r'sehingga:'),
            Tex(r'X_n(x) \text{ } = \text{ } k_2 \text{ } sinh({n\pi x \over b}), ',color=MAROON_A),
            Tex(r'n \text{ } = \text{ }1,2,3,...',color=MAROON_A),
            Tex(r'u(x,y) \text{ } = \text{ } sinh({n\pi x \over b})  \text{ } sin({n\pi x \over b}),',color=RED),
            Tex(r'n \text{ } = \text{ }1,2,3,...',color=RED)
        )
        
        d1[0].set_color_by_tex_to_color_map({
            "dan":WHITE
        })
        nulis={"run_time":3}
        self.wait(2)
        pack=VGroup(d1[0], d1[1], d1[2]).arrange(DOWN)
        self.play(ShowCreation(d1[0]),ShowCreation(d1[1]),**nulis)
        self.wait(3)
        self.play(Write(d1[2]))
        self.wait(3)
        self.play(ReplacementTransform(pack,d1[3]))
        self.wait(2)
        self.play(d1[3].move_to,(3*UP+3*LEFT))
        self.wait(2)
        d1[4].next_to(d1[3],DOWN+RIGHT,buff=0.2)
        self.play(Write(d1[4]),**nulis)
        self.wait()
        d1[5].next_to(d1[4],DOWN,buff=0.2)
        self.play(FadeIn(d1[5],UP))
        self.wait(2)
        
        tunjuk=Arrow([0,0,0], [0,-2,0])
        fund=VGroup(d1[6], d1[7]).arrange(DOWN,buff=0.2)
        
        tunjuk.next_to(d1[5],DOWN)
        fund.next_to(tunjuk,DOWN,buff=0.5)
        kotak=SurroundingRectangle(fund,color= YELLOW,buff=0.2)
        self.play(GrowArrow(tunjuk))
        self.wait(2)
        self.play(Write(d1[6]))
        self.wait(2)
        self.play(FadeIn(d1[7],UP))
        self.wait()
        self.play(ShowCreation(kotak))
        self.wait(4)
        d.next_to(kotak, DOWN,buff=0.2)
        self.play(Write(d),**nulis)
        self.wait(4)
        bapack=VGroup(tunjuk,kotak,d1[4],d1[5],fund,d,d1[3])
        self.play(Uncreate(bapack),**nulis)
       
        
class a5 (Scene):
    def construct (self):
        set_background(self)
        e=VGroup(
            Text("Syarat batas: ", font_size=36, color=RED),
            Text("(TERPENUHI)", font_size = 32, color= YELLOW)
        )
        
        e1=VGroup(
            Tex(r'u(a,y) \text{ } = \text { } f(y)',color=BLUE),
            Tex(r'u(x,y) \text{ } &= \text{ } \sum_{n=1}^{\infty} u_n(x,y) \text{ } \\&= \text{ } \sum_{n=1}^{\infty} C_n \text{ } sinh ({n\pi x\over b}) \text{ } sin ({n\pi x\over b})',color=GREEN)
        ).arrange(DOWN)
        
        nulis={"run_time":2}
        self.play(Write(e[0]), **nulis)
        self.wait(2)
        e1[0].next_to(e[0],DOWN,buff=0.2)
        self.play(ShowCreation(e1[0]))
        self.wait(2)
        e[1].next_to(e1[0],RIGHT,buff=0.75)
        self.play(Write(e[1]), **nulis)
        self.wait(2)
        
        pack=VGroup(e[0], e[1], e1[0])
        self.play(pack.move_to,(3*UP))
        self.wait(3)
        
        self.play(ShowCreation(e1[1]), **nulis)
        self.wait(5)
        bapack=VGroup(pack,e1[1])
        self.play(FadeOut(bapack, DOWN))
        
class a6 (Scene):
    def construct(self):
        set_background(self)
        f=VGroup(
            Text("dari rumus tadi, ",font_size=32),
            Tex(r'\sum_{n=1}^{\infty} u_n(x,y)', color=GOLD_A),
            Text("dihilangkan.", font_size=32),
        ).arrange(RIGHT)
        
        
        f1=Text("""
                Pada u(x,y) atau persamaan yang masih \n
                tersisa, x berubah menjadi a. Didapat:
            """, font_size=32
            )
        
        f2=VGroup(
            Tex(r'u(a,y) \text{ } ='),
            Tex(r'\text{ } \sum_{n=1}^{\infty}'),
            Tex(r'C_n \text{ } sinh ({n\pi \over b}a) \text{ }',color=BLUE),
            Tex(r'sin ({n\pi y\over b}) \text{ } = \text{ } f(y)')
        ).arrange(RIGHT)
        
        f3=VGroup(
            Tex(r'C_n \text{ } sinh ({n\pi \over b}a) \text{ }',color=BLUE),
            Text("adalah koefisien deret Fourier Sinus,", font_size=32, t2c={"deret Fourier Sinus": RED}),
            Text("dengan periode 2b", font_size=32)
        ).arrange(DOWN)
        
        f4=VGroup(
            Tex(r'C_n \text{ } sinh ({n\pi \over b}a) \text{ } = \text{ } {2 \over b}\int_{0}^{b}f(y) \text{ } sin({n\pi y\over b})dy,',color=MAROON_A),
            Tex(r'n \text{ } = \text{ }1,2,3,...',color=MAROON_A)
        ).arrange(DOWN)
        
        nulis={"run_time":3}
        self.wait(3)
        self.play(Write(f),**nulis)
        self.play(f.move_to,(3*UP))
        
        f1.next_to(f,DOWN,buff=0.2)
        self.play(Write(f1), **nulis)
        self.wait(3)
        
        f2.next_to(f1,DOWN)
        self.play(ShowCreation(f2),**nulis)
        self.wait(3)
        
        sulap=VGroup(f,f1)
        self.play(FadeOut(sulap,UP),f2.move_to,(3*UP))
        self.wait(2)
        
        high=SurroundingRectangle(f2[2], color=YELLOW, buff=0.2)
        self.play(ShowCreation(high))
        self.wait()
        
        f3.next_to(f2,DOWN,buff=0.2)
        self.play(Write(f3), **nulis)
        self.wait(2)
        
        tunjuk=Arrow([0,0,0], [0,-1,0])
        tunjuk.next_to(f3,DOWN)
        f4.next_to(tunjuk,DOWN,buff=0.5)
        self.play(GrowArrow(tunjuk))
        high1=SurroundingRectangle(f4, color=YELLOW, buff=0.2)
        self.play(ShowCreation(f4), **nulis)
        self.wait()
        self.play(ShowCreation(high1))
        self.wait(5)
        
        bubar=VGroup(f4,f3,f2,tunjuk,high1,high)
        self.play(FadeOut(bubar,LEFT))