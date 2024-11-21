from manim import *
import math

class Bisection(MovingCameraScene):
  def construct(self):
    ax = Axes(
      x_range=(-1, 4, 0.5),
      y_range=(-3, 3, 1),
      tips=True,
      axis_config={"include_numbers": True, "color": BLUE},
      
    )
    equation = ax.plot(lambda x: (2**x)*math.cos(x), x_range=[-1, 4], use_smoothing=False)
    equation_name = Tex("$2^x \cos x$",color=WHITE)
    equation_name.next_to(equation_name,5*UP+LEFT)


    self.play(Write(ax),run_time=1)
    self.play(LaggedStart(
        Write(equation),
        Write(equation_name),
        lag_ratio=0.5,
        run_time=2
    ))
    self.wait(2)

    self.camera.frame.save_state()
    self.play(self.camera.frame.animate.set(width=equation.width/2))
    
    dot1 = Dot(ax.c2p(1.0,0),color=PINK)
    dot2 = Dot(ax.c2p(2.0,0),color=PINK)
    dot3 = Dot(ax.c2p(1.5,0),color=PURE_RED)
    self.play(LaggedStart(
        Write(dot1),
        Write(dot2),
        lag_ratio=0.5
    ))
    l_1=Line(ax.c2p(1.0,0),ax.c2p(2.0,0),color=PINK)
    self.play(Write(l_1))

    self.wait(3)
    
    name_1 = VGroup(Tex("1.0",color=WHITE).move_to(ax.c2p(1.0,0)), Tex("2.0",color=WHITE).move_to(ax.c2p(2.0,0))).scale(0.75).shift(0.4*DOWN+0.2*LEFT)
    name_2 = VGroup(MathTex("\\frac{1.0 + 2.0}{2}").shift(2*LEFT),MathTex(" = 1.5")).move_to(ax.c2p(1.5)).scale(0.7).shift(RIGHT+UP)

    self.play(Transform(name_1,name_2))
    self.wait(3)
    self.play(Write(dot3))
    self.wait(1)
    l_2=DashedLine(ax.c2p(1.5,0),ax.c2p(1.5,0.2))
    self.play(Write(l_2,color=WHITE))
    self.wait(3)
    l_3=Line(ax.c2p(1.5,0),ax.c2p(2.0,0),color=PINK)
    dot3.set_color(PINK)

    self.play(
        Transform(dot1,dot3),
        Transform(l_1,l_3),
        Unwrite(l_2)
    )


    # Second trial
    name_2[0]=MathTex("\\frac{1.5+2.0}{2}").shift(2*LEFT)
    name_2[1]=MathTex(" = 1.75")
    name_2.move_to(ax.c2p(1.5)).scale(0.7).shift(RIGHT+UP)
    self.play(Transform(name_1,name_2))
    
    self.remove(dot3)
    dot3.move_to(ax.c2p(1.75,0))
    l_3 = Line(ax.c2p(1.5,0),ax.c2p(1.75,0),color=PINK)
    dot3.set_color(PURE_RED)
    self.wait(3)
    self.play(Write(dot3))
    l_2=DashedLine(ax.c2p(1.75,0),ax.c2p(1.75,-0.6))
    self.play(Write(l_2))
    self.wait(2)
    dot3.set_color(PINK)
    self.play(Transform(dot2,dot3),Transform(l_1,l_3))


    # Third trial
    self.play(Unwrite(l_2))
    name_2[0]=MathTex("\\frac{1.5+1.75}{2}").shift(2*LEFT)
    name_2[1]=MathTex(" = 1.625")
    name_2.move_to(ax.c2p(1.5)).scale(0.7).shift(RIGHT+UP)
    self.play(Transform(name_1,name_2))
    self.remove(dot3)
    dot3.move_to(ax.c2p(1.625,0))
    l_3 = Line(ax.c2p(1.5,0),ax.c2p(1.625,0),color=PINK)
    dot3.set_color(PURE_RED)
    self.wait()
    self.play(Write(dot3))
    l_2=DashedLine(ax.c2p(1.625,0),ax.c2p(1.625,-0.167))
    self.play(Write(l_2))
    self.wait()
    self.play(self.camera.frame.animate.set(width=equation.width/4).shift(0.4*RIGHT),Unwrite(name_1))
    dot3.set_color(PINK)
    self.play(Transform(dot2,dot3),Transform(l_1,l_3))
    self.play(Unwrite(l_2))
    self.wait(2)

    # A lots of trials
    self.remove(dot3)
    dot3.move_to(ax.c2p(1.5625,0))
    l_3 = Line(ax.c2p(1.5625,0),ax.c2p(1.625,0),color=PINK)
    dot3.set_color(PURE_RED)
    self.wait()
    self.play(Write(dot3))
    self.wait()
    dot3.set_color(PINK)
    self.play(Transform(dot1,dot3),Transform(l_1,l_3))
    self.play(Unwrite(l_2))
    self.wait()

    self.remove(dot3)
    dot3.move_to(ax.c2p(1.578125,0))
    l_3 = Line(ax.c2p(1.5625,0),ax.c2p(1.578125,0),color=PINK)
    dot3.set_color(PURE_RED)
    self.wait()
    self.play(Write(dot3))
    self.wait()
    dot3.set_color(PINK)
    self.play(Transform(dot2,dot3),Transform(l_1,l_3))
    self.wait()

    self.play(Write(dot3))
    dot3.set_color(PURE_RED)
    self.wait()
    self.play(Write(dot3))
    self.wait()
    dot3.set_color(PINK)
    self.play(Transform(dot2,dot3),Transform(l_1,l_3))
    self.wait()


    dot2.move_to(ax.c2p(math.pi/2,0))
    self.play(Unwrite(dot1),Unwrite(dot3),Unwrite(l_1))
    
    self.play(Restore(self.camera.frame))

    self.wait(2)
    name_2[0] = MathTex("Our\\ Estimated\\ Value\\ for\\ 6\\ trails:\\ 1.578125",color=WHITE).shift(2*LEFT)
    name_2[1] = MathTex("The\\ Real\\ Value:\\ \\frac{\\pi}{2} \\approx 1.570796",color=WHITE).shift(DOWN+2*LEFT)
    name_2.move_to(ax.c2p(1.5)).scale(0.7).shift(RIGHT+3*UP)
    self.play(Write(name_2[0]),Write(name_2[1]))

    self.wait()
