from big_ol_pile_of_manim_imports import *
#from manimlib.imports import *
from objectPosition import *
import os
import pyclbr
import numpy as np


      
from big_ol_pile_of_manim_imports import *

#PDF Slide 5-11 
class Scene1(Scene):
    def construct (self):
       #kotak1
       ayam = TextMobject("""Pembahasan kasus masalah syarat batas\n
                            Dirichlet pada domain segi empat""",font="Arial",color=GOLD_A,font_size=110)
       #kotak2
       ikan = TexMobject(r"u_{xx}+u_{yy}=0....(1)")
       ikan.set_submobject_colors_by_gradient(GREY,BLUE)
       ikan.to_edge(UP)
       cumi = TexMobject(r"0<x<a, 0<y<b ",color=YELLOW)
       cumi.next_to(ikan,3*DOWN).buff=2.5
       hiu = TextMobject("Syarat Batas",font="Arial",color=BLUE,font_size=110)
       hiu.next_to(cumi,3*DOWN).buff=3.2
       lele = TextMobject(""" u(x,0)=0; u(x,b)=0;\n
                            u(0,y)=0; u(a,y)=f(y)""",font="Arial",color=YELLOW,font_size=90)
       lele.next_to(hiu,3*DOWN).buff=2.5
       udang = TextMobject("f(y) merupakan sembarang fungsi pada",font="Arial",color=BLUE,font_size=110)
       udang.next_to(lele,3*DOWN).buff=2.5
       rebon = TexMobject("0\leq y\leq b")
       rebon.next_to(udang,3*DOWN)
       peyek = VGroup(udang,rebon)
       hewan = VGroup(peyek,lele,hiu,cumi,ikan)
       
       #kotak3
       grid = NumberPlane(color=BLACK)
       grid.add_coordinates()
       teks = TextMobject("Perhatikan Gambar Berikut:",font="Arial").scale(0.9)
       teks.to_corner(UL)
       kotak = Square()
       kotak = Polygon(np.array([0,0,0]),np.array([0,3,0]),np.array([4,3,0]),np.array([4,0,0]),color=BLUE,fill_opacity=0.16)
       teks1 = TexMobject(r"u_{xx}+u_{yy}=0").scale(0.7)
       teks1.move_to(1.5*UP+2*RIGHT)
       atas = TextMobject("u(x,b)=0").scale(0.6)
       atas.move_to(3.2*UP+2*RIGHT)
       bawah = TextMobject("u(x,0)=0").scale(0.6)
       bawah.move_to(0.5*DOWN+2*RIGHT)
       kiri= TextMobject("u(0,y)=0").scale(0.6)
       kiri.move_to(1.5*UP+1.3*LEFT)
       kanan= TextMobject("u(a,y)=f(y)").scale(0.6)
       kanan.move_to(1.5*UP+5*RIGHT)
       lokasi = VGroup(atas,bawah,kiri,kanan)
       a = TextMobject("a",color=YELLOW).scale(1.1)
       a.move_to(4*RIGHT+0.5*DOWN)
       b = TextMobject("b",color=YELLOW).scale(1.1)
       b.move_to(0.3*LEFT+3.1*UP)
       ab = VGroup(a,b)
       final = VGroup(ab,lokasi,teks1,teks,kotak,grid)
       
       
              
       self.play(Write(ayam))
       self.wait(5)
       self.play(FadeOut(ayam))
       self.wait(3)
       self.play(Write(ikan))
       self.wait(2)
       self.play(Write(cumi))
       self.wait(3)
       self.play(Write(hiu),Write(lele))
       self.wait(8)
       self.play(FadeIn(peyek))
       self.wait(6)
       self.play(Uncreate(hewan))
       self.wait(3)
       self.play(ShowCreation(grid),Write(teks),run_time=3)
       self.wait(3)
       self.play(ShowCreation(kotak))
       self.wait(3)
       self.play(FadeIn(teks1),FadeIn(ab))
       self.wait(3)
       self.play(FadeIn(lokasi))
       self.wait(4)
       self.play(Uncreate(final))
       self.wait(3)
       
     
class Scene2(Scene):
    def construct (self):    
       #kotak4
       fanta = TextMobject("Metode Pemisahan Variabel",font="Arial",color=GOLD_A).scale(1.3)
       fanta1 = TextMobject("Metode Pemisahan Variabel",font="Arial",color=GOLD_A)
       fanta1.to_edge(UP)
       coca = TextMobject("Misalkan,",font="Arial",color=GREEN)
       coca.next_to(fanta1,3*DOWN).buff=3
       cola = TextMobject("u(x,y) = X(x)Y(y)....(1.2)",font="Arial")
       cola.set_submobject_colors_by_gradient(GREEN,BLUE,RED)
       cola.next_to(coca,3*DOWN).buff=2.5
       sprite = TextMobject("Substitusi pers(1.2) ke pers(1), maka diperoleh",font="Arial")
       pulpy = TexMobject(""" {X}''Y+X{Y}''=0 """,font="Arial") 
       pulpy.set_submobject_colors_by_gradient(GREEN,BLUE,RED)
       pulpy.next_to(sprite,3*DOWN).buff=3
       sr = SurroundingRectangle(mobject=pulpy,color=WHITE,buff=0.2)
       minuman = VGroup(sr,pulpy,sprite,coca,cola,fanta)
       
       #kotak5
       freshtea = TexMobject(r"\frac{{X}''}{X}", r"=-\frac{{Y}''}{Y}=", r"\lambda", r" ....(1.3)")
       freshtea.set_submobject_colors_by_gradient(WHITE,BLUE,RED)
       freshtea.move_to(2*UP)
       Sr = SurroundingRectangle(mobject=freshtea[2],color=WHITE,buff=0.2)
       fruitea = TextMobject("KONSTAN", font="Arial")
       fruitea.move_to(1.5*DOWN)
       panah = Arrow(freshtea[2],fruitea,color=RED)
       kotak5 = VGroup(freshtea,fruitea,Sr,panah)
       
       #kotak6
       kukubima = TexMobject(r"{X}''-\lambda X=0....(1.4a)")
       kukubima.set_submobject_colors_by_gradient(PINK,BLUE,WHITE)
       kukubima.move_to(1*UP)
       rossa = TexMobject(r"{Y}''+\lambda Y=0....(1.4b)")
       rossa.set_submobject_colors_by_gradient(PINK,BLUE,WHITE)
       rossa.next_to(kukubima,3*DOWN).buff=3
       marijan = VGroup(kukubima,rossa)
       sR = SurroundingRectangle(mobject=marijan,color=YELLOW,buff=0.2)
       joss = TextMobject("Solusi Persamaan (1)",font="Arial")
       joss.to_edge(DOWN)
       arrow = Arrow(marijan,joss)
       kotak6 = VGroup(marijan,sR,joss,arrow)
       
       
       
       self.play(FadeIn(fanta))
       self.wait(3)
       self.play(Transform(fanta,fanta1))
       self.wait(3)
       self.play(Write(coca),Write(cola),run_time=4)
       self.wait(3)
       self.play(Write(sprite))
       self.wait(3)
       self.play(FadeIn(pulpy),ShowCreation(sr),run_time=4)
       self.wait(7)
       self.play(FadeOut(minuman))
       self.wait(3)
       self.play(Write(freshtea),run_time=3)
       self.wait(4)
       self.play(GrowArrow(panah),Write(Sr),run_time=4)
       self.wait(2)
       self.play(FadeIn(fruitea))
       self.wait(4)
       self.play(FadeOut(kotak5),run_time=3)
       self.wait(3)
       self.play(Write(marijan))
       self.wait(2)
       self.play(ShowCreation(sR))
       self.wait(2)
       self.play(GrowArrow(arrow),FadeIn(joss),run_time=3)
       self.wait(5)
       self.play(FadeOut(kotak6))
       self.wait(3)
       