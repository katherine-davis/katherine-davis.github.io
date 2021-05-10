#########################################################################
#*************************---DAY 21---***********************************

import turtle

sandbox = turtle.Screen()

ranch = turtle.Turtle()

ranch.shape("turtle")


ranch.left(90)

for i in range (12):
    ranch.penup()
    ranch.forward(100)
    if i == 1:
        location = ranch.position()
    ranch.pendown()
    ranch.forward(15)
    ranch.penup()
    ranch.goto(0,0)
    ranch.right(30)


ranch.pendown
ranch.goto(location.x,location.y)
