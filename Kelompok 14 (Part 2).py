from big_ol_pile_of_manim_imports import *
#from manimlib.imports import *
from objectPosition import *
import os
import pyclbr
import numpy as np


      
from big_ol_pile_of_manim_imports import *

#PDF Slide 15-17
class Scene1(Scene):
    def construct (self):
       #kotak1
       senter = TextMobject("Persamaan Laplace dalam koordinat polar",font="Arial",color=TEAL_B).scale(1.2)
       senter1 = TextMobject("Persamaan Laplace dalam koordinat polar",font="Arial",color=TEAL_B).scale(1.2)
       senter1.to_edge(UP)
       #kotak2
       casan = TexMobject(r"\triangledown^{2}", r"u", r" = u_{xx}", r"+u_{yy}=0")
       casan[0].set_color(RED)
       casan[1].set_color(YELLOW)
       casan[2].set_color(GREEN)
       casan[3].set_color(BLUE)
       kurung = SurroundingRectangle(mobject=casan,color=WHITE,buff=0.2)
       grup = VGroup(casan,kurung)
       #kotak3
       casan1 = TexMobject(r"\triangledown^{2}", r"u", r" = u_{xx}", r"+u_{yy}=0")
       casan1[0].set_color(RED)
       casan1[1].set_color(YELLOW)
       casan1[2].set_color(GREEN)
       casan1[3].set_color(BLUE)
       casan1.move_to(1.5*UP)
       kurung1 = SurroundingRectangle(mobject=casan1,color=WHITE,buff=0.2)
       grup1 = VGroup(casan1,kurung1)
       aerator = TextMobject("""Untuk mentransformasi kedalam koordinat polar\n
                                definisikan:""")
       kipas = TexMobject(r"x=r\, cos\theta ,y=r\, sin\theta",color=YELLOW)
       kipas.next_to(aerator,3*DOWN).buff=3
       grup2 = VGroup(grup,senter,kipas,aerator)
       #kotak4
       kardus = TexMobject(r"Hubungan\, r\, dan\, \theta\, diberikan\, oleh:")
       kardus.set_submobject_colors_by_gradient(RED,GREY)
       kardus.to_edge(UP)
       botol = TexMobject(r"r=\sqrt{x^{2}+y^{2}}, tan\theta=\frac{y}{x}")
       botol.set_submobject_colors_by_gradient(WHITE,BLUE)
       botol.next_to(kardus,3*DOWN).buff=3
       kurung2 = SurroundingRectangle(mobject=botol,color=WHITE,buff=0.2)
       kabel = TextMobject("Dengan aturan rantai, turunan u sebagai berikut. ")
       kabel.next_to(botol,3*DOWN).buff=3
       kasur = TexMobject(r"u_{x}",r"=u_{r}r_{x}",r"+u_{\theta}\theta_{x}")
       kasur[0].set_color(GREEN)
       kasur[1].set_color(YELLOW)
       kasur[2].set_color(RED)
       kasur.next_to(kabel,3*DOWN).buff=3
       akhir = VGroup(kasur,kabel,kurung2,kardus,botol)
       
       
       self.play(Write(senter))
       self.wait(3)
       self.play(Transform(senter,senter1))
       self.wait(4)
       self.play(FadeIn(casan),ShowCreation(kurung))
       self.wait(7)
       self.play(Transform(grup,grup1))
       self.wait(2)
       self.play(Write(aerator))
       self.wait(2)
       self.play(FadeIn(kipas))
       self.wait(4)
       self.play(Uncreate(grup2))
       self.wait(3)
       self.play(Write(kardus))
       self.wait(2)
       self.play(FadeIn(botol),FadeIn(kurung2))
       self.wait(3)
       self.play(Write(kabel),Write(kasur),run_time=4)
       self.wait(3)
       self.play(FadeOut(akhir))
       self.wait(3)
       
       
class Scene2(Scene):
    def construct (self):
       #kotak5
       kasur = TexMobject(r"u_{x}",r"=u_{r}r_{x}",r"+u_{\theta}\theta_{x}")
       kasur[0].set_color(GREEN)
       kasur[1].set_color(YELLOW)
       kasur[2].set_color(RED)
       kasur.to_edge(UP)
       kursi = TexMobject(r"u_{xx}=(u_{r}r_{x})_{x}+(u_{\theta}\theta_{x})_{x}")
       kursi.move_to(1.5*UP)
       panah = Arrow(kasur,kursi)
       kursi1 = TexMobject(r"=(u_{r})_{x}r_{x}+u_{r}r_{xx}+(u_{\theta})_{x}\theta_{x}+u_{\theta}\theta_{xx}")
       kursi1.next_to(kursi,DOWN)
       kursi2 = TexMobject(r"=(u_{rr}r_{x}+u_{r\theta}\theta_{x})r_{x}+u_{r}r_{xx}+(u_{\theta r}r_{x}+u_{\theta \theta}\theta_{x})\theta_{x}+u_{\theta}\theta_{xx}....(**)")
       kursi2.next_to(kursi1,DOWN)
       meja = TextMobject("TURUNAN KEDUA",font="Arial",color=YELLOW)
       meja.to_edge(DOWN)
       panah2 = Arrow(kursi2,meja,color=RED)
       mebel = VGroup(kasur,kursi,panah,kursi1,kursi2,meja,panah2)
       #kotak6
       kipas = TexMobject("Turunan\,  dari\,  ", r"r\, ", r"dan\, ", r"\theta :")
       kipas.to_edge(UP)
       kipas[1].set_color(BLUE)
       kipas[3].set_color(BLUE)
       bufet = TexMobject(r"r_{x}=\frac{x}{\sqrt{x^2+y^2}}=\frac{x}{r},")
       bufet.set_submobject_colors_by_gradient(WHITE,BLUE)
       bufet.move_to(3.5*LEFT+1.3*UP)
       tas = TexMobject(r"\theta_{x}=\frac{1}{1+(\frac{y}{x})^2}(-\frac{y}{x^2})=-\frac{y}{r^2}")
       tas.set_submobject_colors_by_gradient(WHITE,PINK)
       tas.next_to(bufet,2*RIGHT).buff=3
       #kotak7
       bufet1 = TexMobject(r"r_{xx}=\frac{r-xr_{x}}{r^2}=\frac{1}{r}-\frac{x^2}{r^3}=\frac{y^2}{r^3},")
       bufet1.set_submobject_colors_by_gradient(PINK,WHITE)
       bufet1.move_to(3.2*LEFT+2*DOWN)
       tas1 = TexMobject(r"\theta_{xx}=-y(-\frac{2}{r^3})r_{x}=\frac{2xy}{r^4}")
       tas1.set_submobject_colors_by_gradient(BLUE,WHITE)
       tas1.next_to(bufet1,2*RIGHT).buff=3
       gabung1 = VGroup(tas,bufet)
       gabung2 = VGroup(tas1,bufet1)
       panah3 = Arrow(gabung1,gabung2)
       campur = VGroup(gabung1,gabung2,kipas,panah3)
       #kotak8
       keyboard = TextMobject("Substitusikan ke persamaan (**)",font="Arial",color=TEAL_B)
       keyboard.to_corner(UP)
       mouse = TexMobject(r"u_{xx}=(u_{rr}r_{x}+u_{r\theta}\theta_{x})r_{x}+u_{r}r_{xx}+(u_{\theta r}r_{x}+u_{\theta \theta}\theta_{x})\theta_{x}+u_{\theta}\theta_{xx}....(**)")
       mouse.next_to(keyboard,3*DOWN).buff=2.5
       pad = TextMobject("Diperoleh:",font="Arial",color=TEAL_B)
       pad.next_to(mouse,2.5*DOWN).buff=2.5
       monitor = TexMobject(r"u_{xx}=\frac{x^2}{r^2}u_{rr}-", r"2\frac{xy}{r^3}u_{r\theta}", r"+\frac{y^2}{r^4}u_{\theta \theta} +\frac{y^2}{r^3}u_{r}+", r"2\frac{xy}{r^4}u_{\theta}")
       monitor.next_to(pad,3*DOWN).buff=2.5
       layar = TexMobject(r"u_{yy}=\frac{y^2}{r^2}u_{rr}+", r"2\frac{xy}{r^3}u_{r\theta}" ,r"+\frac{x^2}{r^4}u_{\theta \theta} +\frac{x^2}{r^3}u_{r}-", r"2\frac{xy}{r^4}u_{\theta}")
       layar.next_to(monitor,DOWN)
       silang = Cross(mobject=monitor[1],stroke_color=RED,storoke_width=6)
       silang1 = Cross(mobject=layar[1],stroke_color=RED,storoke_width=6)
       silang2 = Cross(mobject=monitor[3],stroke_color=BLUE,color=BLUE,storoke_width=6)
       silang3 = Cross(mobject=layar[3],stroke_color=BLUE,color=BLUE,storoke_width=6)
       silang12 = VGroup(silang,silang1)
       silang34 = VGroup(silang2,silang3)
       kotak8 = VGroup(silang12,silang34,layar,monitor,pad,mouse,keyboard)
       #kotak9dan10
       lemari = TextMobject("Substitusikan kedua rumus ke Persamaan Laplace",font="Arial",color=GOLD_A)
       lemari.to_edge(UP)
       hasil = TexMobject(r"\triangledown u = u_{rr}+\frac{1}{r}u_{r}+\frac{1}{r^2}u_{\theta \theta}")
       hasil.set_submobject_colors_by_gradient(BLUE,WHITE,RED)
       kotak = SurroundingRectangle(mobject=hasil,color=WHITE,buff=0.2)
       arrow = Arrow(lemari,hasil)
       katahasil = TextMobject("HASIL",font="Arial")
       katahasil.next_to(hasil,5*DOWN).buff=4
       laplace = TextMobject("Persamaan Laplace dalam Koordinat Polar",font="Arial",color=GOLD_A)
       laplace.next_to(katahasil,2*DOWN).buff=2.5
       all = VGroup(katahasil,arrow,kotak,hasil,lemari,laplace)
       
       
       self.play(Write(kasur))
       self.wait(2)
       self.play(GrowArrow(panah),Write(kursi))
       self.wait(3)
       self.play(FadeIn(kursi1))
       self.wait(3)
       self.play(FadeIn(kursi2))
       self.wait(3)
       self.play(GrowArrow(panah2))
       self.wait()
       self.play(FadeIn(meja))
       self.wait(4)
       self.play(FadeOut(mebel))
       self.wait(3)
       self.play(Write(kipas))
       self.wait(3)
       self.play(FadeIn(bufet),FadeIn(tas))
       self.wait(5)
       self.play(GrowArrow(panah3))
       self.wait()
       self.play(FadeIn(bufet1),FadeIn(tas1))
       self.wait(5)
       self.play(Uncreate(campur))
       self.wait(3)
       self.play(Write(keyboard))
       self.wait()
       self.play(Write(mouse),run_time=3)
       self.wait(4)
       self.play(Write(pad))
       self.wait()
       self.play(FadeIn(monitor),FadeIn(layar))
       self.wait(5)
       self.play(ShowCreation(silang12),run_time=4)
       self.wait(2)
       self.play(ShowCreation(silang34),run_time=4)
       self.wait(4)
       self.play(FadeOut(kotak8))
       self.wait(3)
       self.play(Write(lemari),GrowArrow(arrow))
       self.wait(4)
       self.play(FadeIn(hasil),ShowCreation(kotak))
       self.wait(3)
       self.play(FadeIn(katahasil))
       self.wait(3)
       self.play(Write(laplace))
       self.wait(4)
       self.play(FadeOut(all))
       self.wait(4)
       
       
       
       