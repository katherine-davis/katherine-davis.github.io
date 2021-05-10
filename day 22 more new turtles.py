#########################################################################
#*************************---DAY 22---***********************************

import turtle

sandbox = turtle.Screen()

ranch = turtle.Turtle()

fraction = 20
total = 100

##clock:
##ranch.left(90)
##
##for i in range (12):
##    ranch.penup()
##    ranch.forward(100)
##    if i == 1:
##        location = ranch.position()
##    ranch.pendown()
##    ranch.forward(15)
##    ranch.penup()
##    ranch.goto(0,0)
##    ranch.right(30)
##
##
##ranch.pendown
##ranch.goto(location.x,location.y)

#####creating an xy plane through turtles
##
##for i in range(4):
##    ranch.forward(230)
##    ranch.goto(0,0)
##    ranch.right(90)
####
##for i in range(4):
##    position = ranch.position()
##    ranch.forward(180)
##    ranch.setposition(position)
##    ranch.right(90)

#make a pie chart (multi-colored)

def drawSector(radius, angle, ranch):
    ranch.begin_fill()
    ranch.circle(radius, angle)
    position = ranch.position()
    ranch.goto(0,0)
    ranch.end_fill()
    ranch.setposition(position)
##    
ranch.sety(-100)
##for color in ["pink", "sandy brown", "yellow", "green yellow", "pale turquoise", "blue", "medium purple", "hot pink"]:
##    ranch.color(color)
##    drawSector(100,45, ranch)

for color in ["pink", "sandy brown", "yellow", "green yellow"]:
    ranch.color(color)
    drawSector(100, 90, ranch)




