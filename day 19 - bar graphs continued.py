###############################################################################
#*********************************-- day 19 --*********************************

import turtle

sandbox = turtle.Screen()
deborah = turtle.Turtle()

data = "2387419"

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

    
def drawGraph(heights, barWidth, colorList):
	deborah.left(180)
	deborah.penup()
	deborah.forward(barWidth*len(heights))
	deborah.pendown()
	deborah.right(180)
	for index in range (0,len(heights)):
		currentHeight = heights[index]
		currentHeight = int(currentHeight)
		drawBar(currentHeight*15, barWidth, colorList[index%len(colorList)])
		deborah.penup()
		deborah.forward(barWidth*2)
		deborah.pendown()

#remember % = remainder
#so the solution to the pattern is index%3

data = "238741934529"
#colors = "pale violet red", "medium purple", "sky blue"
colors = ["pink", "sandy brown", "yellow", "green yellow", "pale turquoise", "medium purple", "hot pink"]

drawGraph(data, 10, colors)
