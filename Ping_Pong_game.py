'''
Vince Herrera

11/28/2023

The purpose of this file is to run a ping pong game
'''
import turtle
import time
from ball import Ball

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

Score_Player_A = 0
Score_Player_B = 0
#Dictionary to store the score
scores = {"Player_A": 0, "Player_B":0}

def update_score_board():
    score_board.clear()
    score_board.write("Player A: {} Player B: {}".format(scores["Player_A"],scores["Player_B"]), align="center", font=("Times New Roman",20, "normal"))

#Declaring the victor
def display_winner(winner):
    winner_turtle = turtle.Turtle()
    winner_turtle.speed(0)
    winner_turtle.color("white")
    winner_turtle.penup()
    winner_turtle.hideturtle()
    winner_turtle.goto(0, 0)
    winner_turtle.write(f"{winner} wins!",align = "center", font =("Times New Roman", 40, "normal"))
#Score board
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0,250)
update_score_board()

#Display how to restart the game
def restart():
    restart = turtle.Turtle()
    restart.speed(0)
    restart.color("white")
    restart.penup()
    restart.hideturtle()
    restart.goto(0, -100)
    restart.write(f"Close and rerun to restart",align = "center", font =("Times New Roman", 20, "normal"))


#the game listen or look for when the keys are pressed
window.listen()
window.onkeypress(Left_paddle_up, "w")
window.onkeypress(Left_paddle_down, "s")
window.onkeypress(Right_paddle_up, "Up")
window.onkeypress(Right_paddle_down, "Down")


ball = Ball(window)

#Without this, the window closes instantly/automatically
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
        scores["Player_A"] += 1
        update_score_board()
        if scores["Player_A"] == 5:
            display_winner("Player A")
            restart()
            ball.goto(0,0)
            ball.dx = 0
            ball.dy = 0
        else:
            ball.resume_after_point()


        
    
    if ball.xcor() <= -390:
        scores["Player_B"] += 1
        update_score_board()
        if scores["Player_B"] == 5:
            restart()
            display_winner("Player B")
            ball.goto(0,0)
            ball.dx = 0
            ball.dy = 0
        else:
            ball.resume_after_point()



    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Right_paddle.ycor() + 65 and ball.ycor() > Right_paddle.ycor() -65):
        ball.dx *= -1.05

    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Left_paddle.ycor() + 65 and ball.ycor() > Left_paddle.ycor() -55):
        ball.dx *= -1.05