from big_ol_pile_of_manim_imports import *
#from manimlib.imports import *
from objectPosition import *
import os
import pyclbr
import numpy as np


      
from big_ol_pile_of_manim_imports import *

 
class Scene1(Scene):
    def construct (self):
       #kotak1
       gucci = TextMobject("Persamaan Diferensial Parsial (Eliptik)",font="Arial").scale(1.5)
       gucci.set_color(TEAL_B)
       gucci1 = TextMobject("Persamaan Laplace",font="Arial").scale(1.5)
       gucci1.set_color(TEAL)
       
       #kotak2
       gucci2 = TextMobject("Persamaan Laplace",font="Arial")
       gucci2.set_color(WHITE)
       gucci2.to_edge(UP)
       prada = Arrow(np.array([0,3,0]),np.array([0,0.25,0]),buff=0,tip_length=0.4,width=2,color=RED)
       fendi = TextMobject("Steady State")
       tas = VGroup(gucci,prada,fendi)
       
       #kotak3
       chatime = TextMobject("Persamaan Difusi",font="Arial")
       chatime.to_corner(UL)
       BR = BackgroundRectangle(mobject=chatime,color=BLUE,fill_opacity=0.2,buff=0.2)
       chatime1 = TextMobject("Persamaan Gelombang",font="Arial")
       chatime1.to_corner(UR)
       BR1 = BackgroundRectangle(mobject=chatime1,color=BLUE,fill_opacity=0.2,buff=0.2)
       haus = VGroup(chatime,chatime1,BR,BR1)
       SS = TexMobject(r"u_{t}\equiv 0\,  dan\,   u_{tt}\equiv 0")
       SS.move_to(0.5*DOWN)
       BR2 = BackgroundRectangle(mobject=SS,color=RED,fill_opacity=0.2,buff=0.2)
       nike = Arrow(np.array([-4,3,0]),np.array([-0.5,0.1,0]),buff=0,tip_length=0.4,width=2,color=RED)
       adidas = Arrow(np.array([4,3,0]),np.array([0.5,0.1,0]),buff=0,tip_length=0.4,width=2,color=RED)
       sepatu = VGroup(SS,BR2,nike,adidas,haus)
       
       #kotak4
       hokben = TexMobject(r"u_{xx}=0\,  ", r"(Pada\,  Kasus\,  1D)")
       hokben.to_edge(UP)
       BNI = BackgroundRectangle(mobject=hokben[0],color=BLUE,fill_opacity=0.2,buff=0.1)
       gokana = TexMobject(r"u_{xx}+u_{yy}=0\, ", r"  (Pada\,  Kasus\,  2D)")
       gokana.next_to(hokben,DOWN).buff=4
       BNI1 = BackgroundRectangle(mobject=gokana[0],color=BLUE,fill_opacity=0.2,buff=0.1)
       kfc = TexMobject(r"u_{xx}+u_{yy}+u_{zz}=0\, ", r" (Pada\,  Kasus\,  3D)")
       kfc.next_to(gokana,DOWN).buff=4
       BNI2 = BackgroundRectangle(mobject=kfc[0],color=BLUE,fill_opacity=0.2,buff=0.1)
       makanan = VGroup(hokben,gokana,kfc,BNI,BNI1,BNI2)
       wagyu = TexMobject (r"Solusi \Rightarrow Fungsi \, Harmonik",color=YELLOW,font="Arial")
       wagyu.move_to(1*DOWN)
       food = VGroup(makanan,wagyu)
       
       
       
       self.play(Write(gucci), run_time=5)
       self.wait(4)
       self.play(Transform(gucci,gucci1), run_time=1)
       self.wait(3)
       self.play(Transform(gucci,gucci2), run_time=3)
       self.wait(5)
       self.play(ShowCreation(prada))
       self.wait(3)
       self.play(FadeIn(fendi),run_time=3)
       self.wait(3)
       self.play(FadeOut(tas),run_time=3)
       self.wait(2)
       self.play(FadeIn(haus),run_time=4)
       self.wait(2)
       self.play(ShowCreation(nike),ShowCreation(adidas))
       self.wait(2)
       self.play(FadeIn(SS),FadeIn(BR2),run_time=4)
       self.wait(3)
       self.play(FadeOut(sepatu),run_time=3)
       self.wait(3)
       self.play(FadeIn(makanan),run_time=3)
       self.wait(4)
       self.play(Write(wagyu),run_time=3)
       self.wait(3)
       self.play(FadeOut(food),run_time=3)
       self.wait(2)
       

class Scene2(Scene):
    def construct (self):
       #kotak5
       bec = TextMobject(r"Kasus aliran fluida tunak, ",r"inkompresibel,",r" dan irotasional",font="Arial",color=GOLD)
       bec[1].set_color(BLUE)
       bec.to_edge(UP)
       kurungbawah = Brace(bec[1],DOWN,color=GREEN)
       bip = TextMobject("Persamaan Konservasi Massa (Kontinuitas)",font="Arial",color=GOLD)
       panah = Arrow(kurungbawah,bip)
       btc = TexMobject(r"\triangledown", r" \cdot", r" V ", r" =", r" 0")
       btc.next_to(bip,DOWN).buff=2
       btc[0].set_color(WHITE)
       btc[1].set_color(GREEN)
       btc[2].set_color(ORANGE)
       btc[3].set_color(BLUE)
       btc[4].set_color(PURPLE)
       tembok = BackgroundRectangle(mobject=btc,color=BLUE,fill_opacity=0.1,buff=0.1)
       btt = VGroup(btc,tembok)
       
       #kotak6
       mall = VGroup(bip,panah,kurungbawah,bec)
       btc1 = TexMobject(r"\triangledown", r" \cdot", r" V ", r" =", r" 0").scale(1.4)
       btc1.to_edge(UP)
       btc1[0].set_color(WHITE)
       btc1[1].set_color(GREEN)
       btc1[2].set_color(ORANGE)
       btc1[3].set_color(BLUE)
       btc1[4].set_color(PURPLE)
       tembok1 = BackgroundRectangle(mobject=btc1,color=YELLOW,fill_opacity=0.1,buff=0.1)
       btt1 = VGroup(btc1,tembok1)
       baltos = TextMobject("V = V(x,y,z)",color=RED)
       arrow = Arrow(btt1,baltos)
       jatos = TextMobject("Medan Kecepatan Aliran",color=GOLD)
       jatos.next_to(baltos,DOWN).buff=4
       bandung = VGroup(btt,btt1,baltos,arrow,jatos)
       
        
        
        
       self.play(Write(bec),run_time=3)
       self.wait(2)
       self.play(ShowCreation(kurungbawah),run_time=3)
       self.wait(3)
       self.play(GrowArrow(panah),run_time=3)
       self.wait(3)
       self.play(FadeIn(bip),run_time=2)
       self.wait(3)
       self.play(FadeIn(btc),FadeIn(tembok),run_time=3)
       self.wait(4)
       self.play(FadeOut(mall))
       self.wait(2)
       self.play(Transform(btt,btt1),run_time=3)
       self.wait(3)
       self.play(Write(baltos),run_time=3)
       self.wait(3)
       self.play(GrowArrow(arrow),run_time=3)
       self.wait(3)
       self.play(Write(jatos),run_rime=3)
       self.wait(3)
       self.play(Uncreate(bandung))
       self.wait(4)
       
       
class Scene3(Scene):
    def construct (self):
       #kotak7
       dago = TextMobject("Aliran Fluida Irrotasional",font="Arial")
       dago.to_edge(UP)
       punclut = TexMobject(r"\triangledown \times  V = 0")
       punclut.next_to(dago,4*DOWN).buff=3
       cimbel = BackgroundRectangle(mobject=punclut,color=BLUE,fill_opacity=0.2,buff=0.1)
       sekeloa = TexMobject(r"Fungsi\,  medan\,  skalar\, \phi   (fungsi\,  potensial\,  kecepatan)",font="Arial",color=YELLOW)
       sekeloa1 = TextMobject("Sehingga: ",font="Arial",)
       sekeloa1.next_to(sekeloa, 2*DOWN)
       tubis = TexMobject(r"V", r" = ", r"\triangledown", r" \phi")
       tubis[0].set_color(YELLOW)
       tubis[1].set_color(ORANGE)
       tubis[2].set_color(PINK)
       tubis[3].set_color(RED)
       tubis.next_to(sekeloa,5*DOWN)
       cisbar = TexMobject(r"\triangledown", r" \cdot", r" V ", r" =", r" 0 ")
       cisbar[0].set_color(WHITE)
       cisbar[1].set_color(GREEN)
       cisbar[2].set_color(ORANGE)
       cisbar[3].set_color(BLUE)
       cisbar[4].set_color(PURPLE)
       cisbar.to_edge(DOWN)
       cislam = TextMobject("Substitusikan ke:")
       cislam.next_to(cisbar,UP)
       daerah = VGroup(tubis,cisbar,sekeloa1,sekeloa,cimbel,punclut,dago,cislam)
       
       #kotak8
       teks = TexMobject(r"\triangledown\cdot  \triangledown \phi = 0")
       teks.to_edge(UP)
       teks.set_submobject_colors_by_gradient(PINK,WHITE,RED)
       teks1 = TexMobject(r" \triangledown^{2} \phi = 0")
       teks1.set_submobject_colors_by_gradient(RED,PINK,WHITE)
       arrow = Arrow(teks,teks1,color=BLUE)
       teks2 = TexMobject(r"\bigtriangleup \phi = 0")
       teks2.to_edge(DOWN)
       teks2.set_submobject_colors_by_gradient(WHITE,RED,PINK)
       arrow1 = Arrow(teks1,teks2,color=BLUE)
       formal = VGroup(teks,teks1,arrow,arrow1)
       
       #kotak9
       teks3 = TexMobject(r"\bigtriangleup \phi = 0").scale(1.3)
       teks3.to_edge(UP)
       teks3.set_submobject_colors_by_gradient(ORANGE,RED,PINK)
       stabilo = BackgroundRectangle(mobject=teks3,color=WHITE,fill_opacity=0.2,buff=0.1)
       teks4 = TextMobject("Persamaan Laplace")
       teks4.set_submobject_colors_by_gradient(ORANGE,YELLOW)
       teks4.next_to(teks3,5*DOWN)
       teks5 = TexMobject(r"  \triangle = \frac{\partial^2 }{\partial x^2},\frac{\partial^2 }{\partial y^2},\frac{\partial^2 }{\partial z^2}\, adalah\,  operator\,  Laplace")
       teks5.set_color(YELLOW)
       teks5.next_to(teks4,5*DOWN)
       final = VGroup(teks4,teks5)
       gabung = VGroup(final,teks3,stabilo,teks2)
       
       
       
       self.play(FadeIn(dago),run_time=3)
       self.wait(2)
       self.play(FadeIn(punclut),FadeIn(cimbel),run_time=3)
       self.wait(3)
       self.play(Write(sekeloa),run_time=3)
       self.wait()
       self.play(Write(sekeloa1),run_time=3)
       self.wait(2)
       self.play(Write(tubis))
       self.wait(8)
       self.play(Write(cisbar),Write(cislam))
       self.wait(5)
       self.play(FadeOut(daerah))
       self.wait(2)
       self.play(FadeIn(teks))
       self.wait(3)
       self.play(GrowArrow(arrow))
       self.wait(3)
       self.play(FadeIn(teks1))
       self.wait(3)
       self.play(GrowArrow(arrow1))
       self.wait(3)
       self.play(FadeIn(teks2))
       self.wait(5)
       self.play(FadeOut(formal))
       self.wait(3)
       self.play(Transform(teks2,teks3),FadeIn(stabilo),run_time=3)
       self.wait(3)
       self.play(Write(final),run_time=4)
       self.wait(4)
       self.play(FadeOut(gabung))
       self.wait(3)
       
       