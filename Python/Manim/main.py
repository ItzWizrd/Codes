from manim import *

class WIZRD(Scene):
    def construct(self):
        text = Text("WIZRD",font_size=100,color="#00FFFB")

        self.play(Write(text))
        self.wait(1)

class myAnimation(Scene):
    def construct(self):

        circle=Circle(radius=1)
        square=Square()
        triangle=Triangle()
        

        circle.shift(LEFT*2.2)
        
        
        square.shift(RIGHT*2.2)
        
        circle.set_fill(RED,1)
        triangle.set_fill(BLUE,1)
        square.set_fill(WHITE,1)

        self.play(DrawBorderThenFill(circle), DrawBorderThenFill(square), DrawBorderThenFill(triangle))


        self.wait(1)

class Shape_Transforming(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        self.play(Create(circle))
        self.wait(.2)
        self.play(Transform(circle,square))



class MinecraftLogoAnimation(Scene):
    def construct(self):
 
        self.camera.background_color = "#000000"  
        

        cube = Cube(side_length=1, fill_opacity=1, fill_color=GREEN)
        text = Text("MINECRAFT", font="Arial", weight=BOLD).scale(0.8)
        
        
    
        
    
        self.play(GrowFromCenter(text))
        
        self.wait(1)
        self.play(Transform(text,cube))
        self.wait(1)   

class WindowsLogoLOL(Scene):
    def construct(self):
        sq1 = Square(side_length=1, fill_opacity= 1).set_color(BLUE)
        sq2 = Square(side_length=1, fill_opacity= 1).set_color(BLUE).next_to(sq1,RIGHT)
        sq3 = Square(side_length=1, fill_opacity= 1).set_color(BLUE).next_to(sq1,DOWN)
        sq4 = Square(side_length=1, fill_opacity= 1).set_color(BLUE).next_to(sq3,RIGHT)


        Logo = VGroup(sq1,sq2,sq3,sq4).scale(1)

        self.play(Write(Logo))
        self.wait(1)

class CustomObjects(Scene):
    def construct(self):
        Logo = SVGMobject("barca.svg")
        Logo2 = SVGMobject("madrid.svg")
        self.play(Write(Logo))
        self.wait(3)
        self.play(Write(Logo2))
        self.wait(3)


class IDK(Scene):
    def construct(self):
        Logo = SVGMobject("Smile.svg",color=YELLOW ).move_to([5,0,0])
        Logo.scale(0.5)

        t=  Text("xBadMas",color=YELLOW,weight=BOLD).move_to([-5,0,0])
        
        G1 = VGroup(Logo,t)

        self.play(Write(Logo),Write(t))
        self.wait(1)

        self.play(t.animate.move_to([0,-1 ,0]),Logo.animate.move_to([0,0,0]))
        self.play(Transform (G1,Logo))
        self.play(Logo.animate.scale(100),color=YELLOW)
        self.play(FadeOut(Logo))
        t=  Text("xBadMas",color=YELLOW,weight=BOLD)
        self.play(Write(t))
         
class SquaresXD(Scene):
    def construct(self):
        s1 = Square(fill_opacity=1,color=WHITE,side_length=0.5).move_to([-5,0,0]).set_color("#2AD110")
        s2 = Square(fill_opacity=1,color=WHITE,side_length=0.5).move_to([5,0,0]).set_color("#FF00CC")

        self.play(DrawBorderThenFill(s1))
        self.play(DrawBorderThenFill(s2))
        self.wait(0.5)
        self.play(s2.animate.next_to(s1,RIGHT))

        G1 = VGroup(s1,s2)

        S1 =  Square(fill_opacity=1,side_length=0.5,color=RED)
        S2 =  Square(fill_opacity=1,side_length=0.5,color=ORANGE)
        S5 =  Square(fill_opacity=1,side_length=0.5,color=PURE_GREEN)
        S3 =  Square(fill_opacity=1,side_length=0.5,color=YELLOW)
        S4 =  Square(fill_opacity=1,side_length=0.5,color=GREEN)


        G2= VGroup(S1,S2,S3,S4,S5)
        G2.arrange()

        self.play(ReplacementTransform(G1,G2))

        r1=SurroundingRectangle(G2,color=WHITE) 
        r2 = SurroundingRectangle(r1,color=WHITE)

        self.play(Write(r1),Write(r2),run_time=1.5,)

        no=Text("1 2 3 4 5").next_to(r2,UP).scale(1.5).set_color("#00EEFF")
        

        self.play(Write(no))

        self.play(Indicate(S1,color=RED,scale_factor=0.5),Indicate(no[0],color=RED,scale_factor=1.2))
        self.play(Indicate(S2,color=RED,scale_factor=0.5),Indicate(no[1],color=RED,scale_factor=1.2))
        self.play(Indicate(S3,color=RED,scale_factor=0.5),Indicate(no[2],color=RED,scale_factor=1.2))
        self.play(Indicate(S4,color=RED,scale_factor=0.5),Indicate(no[3],color=RED,scale_factor=1.2))
        self.play(Indicate(S5,color=RED,scale_factor=0.5),Indicate(no[4],color=RED,scale_factor=1.2))

        name=Text("WIZRD",color="#8800FF")
        g99= VGroup(G2,r1,r2,G1,no)

        self.play(g99.animate.move_to([0,2,0]))
        self.play(Write(name))

 