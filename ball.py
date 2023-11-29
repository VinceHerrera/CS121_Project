'''
Vince Herrera

11/28/2023

This file contains the class and functions for the ball for the ping pong game
'''
#Setting up the Ball, changed it into a class
import time
import turtle
class Ball(turtle.Turtle):
    def __init__(self,window):
        super().__init__()
        self.window = window
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len = 1,stretch_wid = 1)
        self.goto(0,0)
        self.dx = 0.2
        self.dy = 0.15
#function to 
# restart the movement after stopping the ball
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
#Puts a timer for the game to reset so the players can get ready to once again fight for the point.

    def resume_after_point(self):
        self.goto(0,0)
        self.dx = 0
        self.dy = 0
        time.sleep(1)    
        self.start_movement()

#Reset the ball's movement after scoring a point

    def start_movement(self):
        self.dx = 0.2
        self.dy = 0.15
        self.window.update()
