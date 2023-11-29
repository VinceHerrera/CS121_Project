import turtle
import time
__annotations__

#Setting up the screen
window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Setting up the left paddle
Left_paddle = turtle.Turtle()
Left_paddle.speed(0)
Left_paddle.shape("square")
Left_paddle.color("white")
Left_paddle.penup()
Left_paddle.shapesize(stretch_len=0.5,stretch_wid=5)
Left_paddle.goto(-350,0)

#Setting up the right paddle
Right_paddle = turtle.Turtle()
Right_paddle.speed(0)
Right_paddle.shape("square")
Right_paddle.color("white")
Right_paddle.penup()
Right_paddle.shapesize(stretch_len = 0.5,stretch_wid = 5)
Right_paddle.goto(350,0)

#Setting up the Ball
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len = 1,stretch_wid = 1)
        self.goto(0,0)
        self.dx = 0.2
        self.dy = 0.15
    
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def resume_after_point(self):
        self.goto(0,0)
        self.dx *= -1

    def pause_each_point(self,time_to_wait):
        window.ontimer(self.resume_after_point, time_to_wait)

#Functions to move the paddles
#Left paddle
def Left_paddle_up():
    y_coordinate = Left_paddle.ycor()
    if y_coordinate < 225:
        y_coordinate += 45
    Left_paddle.sety(y_coordinate)
def Left_paddle_down():
    y_coordinate = Left_paddle.ycor()
    if y_coordinate > -215:
        y_coordinate -= 45
    Left_paddle.sety(y_coordinate)

#Right paddles
def Right_paddle_up():
    y_coordinate = Right_paddle.ycor()
    if y_coordinate < 225:
        y_coordinate += 45
    Right_paddle.sety(y_coordinate)
def Right_paddle_down():
    y_coordinate = Right_paddle.ycor()
    if y_coordinate > -215:
        y_coordinate -= 45
    Right_paddle.sety(y_coordinate)




window.listen()
window.onkeypress(Left_paddle_up, "w")
window.onkeypress(Left_paddle_down, "s")
window.onkeypress(Right_paddle_up, "Up")
window.onkeypress(Right_paddle_down, "Down")
#Without this, the window closes instantly/automatically

ball = Ball()
while True:
    window.update()
    ball.move()
    #Bounces when hit the border
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1 
    
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    
    if ball.xcor() >= 390:
        ball.pause_each_point(1000)
        
    
    if ball.xcor() <= -390:
        ball.pause_each_point(1000)
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Right_paddle.ycor() + 65 and ball.ycor() > Right_paddle.ycor() -65):
        ball.dx *= -1.05

    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Left_paddle.ycor() + 65 and ball.ycor() > Left_paddle.ycor() -55):
        ball.dx *= -1.05