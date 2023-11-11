import turtle

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
Right_paddle.shapesize(stretch_len=0.5,stretch_wid=5)
Right_paddle.goto(350,0)

#Setting up the Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.shapesize(stretch_len=1,stretch_wid=1)
Ball.goto(0,0)

#Functions to move the paddles
#Left paddle
def Left_paddle_up():
    y_coordinate = Left_paddle.ycor()
    y_coordinate += 15
    Left_paddle.sety(y_coordinate)
def Left_paddle_down():
    y_coordinate = Left_paddle.ycor()
    y_coordinate -= 15
    Left_paddle.sety(y_coordinate)

#Right paddles
def Right_paddle_up():
    y_coordinate = Right_paddle.ycor()
    y_coordinate += 15
    Right_paddle.sety(y_coordinate)
def Right_paddle_down():
    y_coordinate = Right_paddle.ycor()
    y_coordinate -= 15
    Right_paddle.sety(y_coordinate)


window.listen()
window.onkeypress(Left_paddle_up, "w")
window.onkeypress(Left_paddle_down, "s")
window.onkeypress(Right_paddle_up, "Up")
window.onkeypress(Right_paddle_down, "Down")
#Without this, the window closes instantly/automatically
while True:
    window.update()