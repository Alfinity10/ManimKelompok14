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
    
class m0 (Scene):
    def construct (self):
        set_background(self)
        a = Text("""
            Persamaan Laplace pada Kasus Masalah Syarat Batas\n
                     Dirichlet pada Domain Lingkaran
            """,
            t2c = {"Laplace" : PINK, "Dirichlet": TEAL_A}
        )
        
        a.set_width(FRAME_WIDTH -1)
        self.play(Write(a))
        self.wait(3)
        self.play(Uncreate(a))
        self.wait()
        
class m1 (Scene):
    def construct (self):
        set_background(self)
        a = Tex(r'{\nabla^2 u}\text{ }', 
            r'{=}\text{ }', 
            r'{u_{rr}\text{ } {+}}\text{ }', 
            r'{1 \over r} {u_r}',
            r'\text{ }+\text{ }',
            r'{1 \over r^2} \text{ } {u_{\theta \theta}}', color = BLUE)
        
        b = Tex(r'Dimana\text{ }' ,
                r'0 < r \leq {a}, 0 < \theta \leq {2 \pi},',
                r'\text{ }dengan\text{ }syarat\text{ }batas: ')
        c = Tex(r'{u({\alpha, \theta}) \text{ } {=} \text{ } {f(\theta)}}', color=TEAL_A)
        
        pack = VGroup(a, b, c).arrange(DOWN)
        
        delay={"run_time":2}
        self.play(ShowCreation(a), **delay)
        self.wait(5)
        self.play(Write(b), **delay)
        self.wait(5)
        self.play(ShowCreation(c), **delay)
        self.wait(6)
        self.play(Uncreate(pack), **delay)
        self.wait()

class m2 (Scene):
    def construct(self):
        set_background(self)
        a=Tex(r'u(r,\theta)\text{ }=\text{ }R(r)\circleddash (\theta)',color=TEAL_A)
        b=Tex(r"R''\circleddash+{1 \over r}R'\circleddash+{1 \over r^2}R\circleddash''\text{ }=\text{ }0",color=RED)
        c=Tex(r"{r^2 R''+rR' \over R}=-{\circleddash''\over\circleddash}=\lambda", color=BLUE)
        d=Tex(r"dengan\text{ }\lambda\text{ }adalah\text{ }konstan.", isolate=["\lambda", "konstan"])
        
        pack = VGroup(a,b,c,d).arrange(DOWN, buff=0.8)
        
        d.set_color_by_tex_to_color_map({
            "\lambda":BLUE,
            "konstan":GREEN
        })
        
        delay={"run_time":2}
        self.play(ShowCreation(a), **delay)
        self.wait(5)
        self.play(ShowCreation(b), **delay)
        self.wait(5)
        self.play(ShowCreation(c), **delay)
        self.wait(4)
        self.play(Write(d))
        self.wait(6)
        self.play(FadeOut(pack,DOWN), **delay)
        self.wait()
        
        
class m3(Scene):
    def construct(self):
        set_background(self)
        a=Tex(r'Didapat\text{ }2\text{ }PDB', isolate=["PDB"])
        b=Tex(r"r^2 R''+rR'- \lambda R \text{ }=\text{ }0 \text{ }\text{ } (1)", color=GOLD_A)
        c=Tex(r"\circleddash''\text{ }+\text{ }\lambda\circleddash\text{ }=\text{ }0 \text{ }\text{ } (2)", color=GOLD_B)
        
        d=Tex(r'u(r,\theta)\text{ }=\text{ }u(r,\theta+2\pi)', color= MAROON_A)
        e=Tex(r'R(r)\circleddash(\theta)\text{ }=\text{ }R(r)\circleddash(\theta + 2\pi)', color=MAROON_A)
        f=Tex(r'\circleddash(\theta)\text{ }=\text{ }\circleddash(\theta+2\pi)',color=MAROON_A)
        
        g=Tex(r"\circleddash(- \pi)\text{ }=\text{ } \circleddash(\pi)\text{ }dan\text{ }\circleddash'(- \pi)\text{ }=\text{ } \circleddash'(\pi),", color=RED_A)
        
        bapack = VGroup(a,b,c).arrange(DOWN, buff=0.4)
        pack = VGroup(d,e,f,g).arrange(DOWN, buff=0.4)
        
        pack.next_to(bapack,DOWN,buff=-1.5)
        a.set_color_by_tex_to_color_map({
            "PDB":GREEN
        })
        delay={"run_time":1.5}
        self.play(ShowCreation(a), **delay)
        self.wait(2)
        self.play(ShowCreation(b), **delay)
        self.wait()
        self.play(ShowCreation(c), **delay)
        self.wait(5)
        self.play(bapack.move_to,(2.5*UP))
        self.wait()
        self.play(FadeIn(d,RIGHT), **delay)
        self.wait(2)
        self.play(FadeIn(e,LEFT), **delay)
        self.wait(2)
        self.play(FadeIn(f,UP), **delay)
        self.wait(3)
        self.play(Write(g), **delay)
        self.wait(6)
        self.play(Uncreate(pack),Uncreate(bapack), **delay)
        self.wait()
        
class m4(Scene):
    def construct(self):
        set_background(self)
        a=Tex(r'\circleddash(\theta)\text{ }=\text{ } A\text{ }cos(\sqrt{\lambda\theta})+B\text{ }sin(\sqrt{\lambda\theta})', color=LIGHT_BROWN)
        
        b=Tex(r'solusi\text{ }umumnya:')
        c=Tex(r'\lambda_{0}\text{ }=\text{ }0,\text{        }\circleddash_{0}(\theta)\text{ }=\text{ }1', isolate=["\lambda_{0}","\circleddash_{0}","\theta","(",")"])
        
        d=Tex(r'\lambda_{n}\text{ }=\text{ }n^2,', isolate=["\lambda_{n}"])
        e=Tex(r'\circleddash _{n}(\theta)\text{ }=\text{ }A _{n} \text{ } cos \text{ } n\theta \text{ } + \text{ } B _{n} \text{ } sin \text{ } n\theta',
            isolate=["\circleddash _{n}","\theta", "A _{n}", "B _{n}","(",")"])
        f=Tex(r'untuk\text{ }n\text{ }=\text{ }1,2,3,\text{ }....',isolate=["n","1","2","3"])
        
        pack = VGroup(a,b,c,d,e,f).arrange(DOWN, buff=0.8)
        
        c.set_color_by_tex_to_color_map({
            "\lambda_{0}":BLUE,
            "\circleddash_{0}":PINK,
            "\theta":PINK,
            "(":PINK,
            ")":PINK
        })
        d.set_color_by_tex_to_color_map({
            "\lambda_{n}":RED
        })
        e.set_color_by_tex_to_color_map({
            "\circleddash _{n}":PINK,
            "\theta":PINK,
            "(":PINK,
            ")":PINK,
            "A _{n}":YELLOW_A,
            "B _{n}":TEAL_B
        })
        f.set_color_by_tex_to_color_map({
            "1":GREEN,
            "2":GREEN,
            "3":GREEN
        })
        
        delay={"run_time":1.5}
        self.play(ShowCreation(a), **delay)
        self.wait(2)
        self.play(ShowCreation(b), **delay)
        self.wait(2)
        self.play(ShowCreation(c), **delay)
        self.wait(4)
        self.play(FadeIn(d,UP), **delay)
        self.wait(2)
        self.play(Write(e), **delay)
        self.wait(2)
        self.play(Write(f), **delay)
        self.wait(6)
        self.play(FadeOut(pack,RIGHT), **delay)
        self.wait()
        
class m5(Scene):
    def construct(self):
        set_background(self)
        a=Tex(r'Untuk \text{ } \lambda_{0}\text{ }=\text{ }0,',isolate=["\lambda_{0}","=","0"])
        b=Tex(r'maka \text{ } persamaan \text{ } (1) \text{ } menjadi', isolate=["persamaan","(","1",")"])
        c=Tex(r"r^2 R''_{0}\text{ }+\text{ }rR'_{0}\text{ }=\text{ }0",color=GOLD_A)
        
        d=Tex(r'R_{0}(r)\text{ }=\text{ }C_{0}\text{ }+\text{ }D_{0} \text{ }ln\text{ } r',color=GOLD_B)
        
        e=Tex(r'R_{0}(r)\text{ }=\text{ }1',color=GOLD_C)
        f=Tex(r'dan \text{ } solusinya \text{ } dari \text{ } persamaan \text{ } Laplace\text{ } nya:', isolate=["Laplace"])
        g=Tex(r'u_{0}(r,\theta)\text{ }=\text{ } R_{0}(r)\circleddash_{0}(\theta)\text{ }=\text{ }1',color=TEAL_B)
        pack = VGroup(a,b,c,d,e,f,g).arrange(DOWN, buff=0.5)
        
        a.set_color_by_tex_to_color_map({
            "\lambda_{0}":BLUE,
            "=":BLUE,
            "0":BLUE
        })
        b.set_color_by_tex_to_color_map({
            "persamaan":RED,
            "(":RED,
            ")":RED,
            "1":RED
        })
        f.set_color_by_tex_to_color_map({
            "Laplace":GREEN,
        })
        delay={"run_time":1.5}
        self.play(Write(a), **delay)
        self.wait(2)
        self.play(Write(b), **delay)
        self.wait(2)
        self.play(ShowCreation(c), **delay)
        self.wait(5)
        self.play(ShowCreation(d), **delay)
        self.wait(2)
        self.play(ShowCreation(e), **delay)
        self.wait(2)
        self.play(ShowCreation(f), **delay)
        self.wait(2)
        self.play(ShowCreation(g), **delay)
        self.wait(6)
        self.play(Uncreate(pack), **delay)
        self.wait()
        
        
        
class m6(Scene):
    def construct(self):
        set_background(self)
        a=Tex(r'Untuk \text{ } \lambda_{n}\text{ }=\text{ }n^2,\text{ } persamaan\text{ }(1)\text{ }menjadi:',
            isolate=["\lambda_{n}","=","n^2", "persamaan","(","1",")"]
        )
        b=Tex(r"r^2 R''_{n} \text{ }+\text{ } rR'_{n} \text{ }-\text{ } n^2 R_{n}\text{ }=\text{ }0", color=PINK)
        
        c=Tex(r'R_{n}(r)\text{ }=\text{ }C_{n}r^n\text{ }+\text{ }D_{n}r^{-n}', color=MAROON_A)
        
        d=Tex(r'U_{n}(r,\theta) \text{ } &= \text{ } R_{n}(r)\circleddash_{n}(\theta) \\&= r^n (A_{n} \text{ } cos \text{ } n\theta \text{ }+\text{ } B_{n} \text{ } sin \text{ } n\theta)',
            isolate=["R_{n}","\circleddash_{n}","r^n", "A_{n}", "B_{n}","U_{n}","r","\theta"]
        )
        e=Tex(r'untuk\text{ }n\text{ }=\text{ }1,2,3,...',isolate=["n","1","2","3"])
        
        a.set_color_by_tex_to_color_map({
            "\lambda_{n}":RED,
            "=":RED,
            "n^2":RED,
            "persamaan":BLUE,
            "(":BLUE,
            ")":BLUE,
            "1":BLUE
        })
        d.set_color_by_tex_to_color_map({
            "U_{n}":DARK_BROWN,
            "r":ORANGE,
            "R_{n}":PINK,
            "\theta":GREEN,
            "\circleddash_{n}":PURPLE,
            "A_{n}":YELLOW_A,
            "B_{n}":TEAL_B
        })
        e.set_color_by_tex_to_color_map({
            "1":YELLOW_C,
            "2":YELLOW_C,
            "3":YELLOW_C
        })
        
        pack = VGroup(a,b,c,d,e).arrange(DOWN, buff=0.5)
        
        delay={"run_time":2}
        self.play(Write(a), **delay)
        self.wait(3)
        self.play(DrawBorderThenFill(b), **delay)
        self.wait(4)
        self.play(DrawBorderThenFill(c), **delay)
        self.wait(5)
        self.play(ShowCreation(d), **delay)
        self.wait(2)
        self.play(Write(e), **delay)
        self.wait(6)
        self.play(Uncreate(pack), **delay)
        self.wait()
        
        
        
class m7(Scene):
    def construct(self):
        set_background(self)
        a=Tex(r'u(r,\theta) \text{ } = \text{ } {A_{0} \over 2 } \text{ } + \text{ } \sum_{n=1}^\infty  r^n (A_{n} \text{ } cos \text{ } (n\theta) \text{ } + \text{ } B_{n} \text{ } sin (n\theta)',color=GOLD_A)
        
        b=Tex(r'u(a,\theta) \text{ } = \text{ } {A_{0} \over 2 } \text{ } + \text{ } \sum_{n=1}^\infty  a^n (A_{n} \text{ } cos \text{ } (n\theta) \text{ } + \text{ } B_{n} \text{ } sin (n\theta) ) \text{ } =f(\theta)',color=GOLD_C)
        
        c=Tex(r'A_{n}\text{ }=\text{ } {1 \over \pi a^n} \int_{0}^2\pi f(\theta) \text{ } cos \text{ } n\theta \text{ } d\theta',
            isolate=["="],color=MAROON_A
        )
        d=Tex(r'untuk\text{ }n\text{ }=\text{ }1,2,3,...',color=GOLD_A)
        
        e=Tex(r'B_{n}\text{ }=\text{ } {1 \over \pi a^n} \int_{0}^2\pi f(\theta) \text{ } sin \text{ } n\theta \text{ } d\theta',
            isolate=["="],color=TEAL_A
        )
        f=Tex(r'untuk\text{ }n\text{ }=\text{ }1,2,3,...',color=GOLD_A)
        c.set_color_by_tex_to_color_map({
            "=":WHITE
        })
        e.set_color_by_tex_to_color_map({
            "=":WHITE
        })
        pack = VGroup(a,b,c,d,e,f).arrange(DOWN, buff=0.3)
        
        delay={"run_time":2}
        self.play(ShowCreation(a), **delay)
        self.wait(3)
        self.play(ShowCreation(b), **delay)
        self.wait(3)
        self.play(ShowCreation(c), **delay)
        self.wait(2)
        self.play(FadeIn(d,UP), **delay)
        self.wait(4)
        self.play(Write(e), **delay)
        self.wait(2)
        self.play(Write(f), **delay)
        self.wait(6)
        self.play(Uncreate(pack), **delay)
        self.wait()