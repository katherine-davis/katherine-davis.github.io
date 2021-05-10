
##############################################################################
#*********************************---DAY 5---*********************************

#how long they want the egde of a square to be

import turtle

side = input("How long do you want Dennis to paint the sides of your square today? (Just a number, please) ")
color = input("What color would you like Dennis and the square to be? ")

numSide = int(side)


sandbox = turtle.Screen()
dennis = turtle.Turtle()
dennis.shape("turtle")

dennis.pencolor(color)
dennis.color(color)
dennis.begin_fill()
dennis.forward(numSide)
dennis.left(90)
dennis.forward(numSide)
dennis.left(90)
dennis.forward(numSide)
dennis.left(90)
dennis.forward(numSide)
dennis.right(90)
dennis.end_fill()

##dennis.clear()


dennis.right(90)
dennis.penup()
dennis.forward(100)
dennis.pendown()
dennis.pencolor(color)
dennis.left(90)
dennis.circle(100)

dennis.beginfill()
