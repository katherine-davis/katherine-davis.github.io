###############################################################################
#*********************************-- day 18 --*********************************

import turtle

sandbox = turtle.Screen()
deborah = turtle.Turtle()

data = "2387419"
##
##hei = input("What height do you want?" )
##wid = input("What width do you want?" )
##
##heiint = int(hei)
##widint = int(wid)
##
##def drawBar(height, width):
##    #draw a square with specified height and width (must use a loop)
##    for i in range(0, 2, 1):
##        deborah.forward(width)
##        deborah.right(90)
##        deborah.forward(height)
##        deborah.right(90)
##        
##
##print (drawBar(heiint,widint))

#her answer:
def drawBar(height, width, color):
    deborah.color(color)
    deborah.begin_fill()
    for i in range (0,4):
        if i == 0 or i == 2:
            deborah.forward(width)
        else:
            deborah.forward(height)
        deborah.left(90)
    deborah.end_fill()



print (drawBar(70,20,"green"))

deborah.penup()
deborah.forward(25)
deborah.pendown()


print (drawBar(140,40,"blue"))

deborah.penup()
deborah.forward(70)
deborah.pendown()




