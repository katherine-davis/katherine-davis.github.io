##############################################################################
#*********************************-- day 8 --*********************************


import turtle

sandbox = turtle.Screen()

fred = turtle.Turtle()

fred.shape("turtle")



fred.left(90)
fred.forward(100)
fred.left(90)
fred.forward(100)
fred.left(90)
fred.forward(100)
fred.left(90)
fred.forward(100)

fred.clear()

#1st number start second end 3rd number means how many each rep is i think
#start be inclusive and exclusive of end
#meaning for the example below it would be 0,1,2,3


#but (0,4,1) is also (4)

for i in range(0,4,1):
    fred.right(90)
    fred.forward(100)
    
fred.clear()

for i in range(4):
    fred.forward(100)
    fred.right(90)
    

fred.clear()

for i in range(4):
    fred.forward(100)
    fred.left(90)
    

fred.clear()
fred.color("pink")

for i in range(3):
    fred.right(120)
    fred.forward(150)

fred.clear()

for i in ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink"]:
    fred.color(i)
    fred.forward(50)
    fred.left(45)

fred.clear()
    
#CHALLENGE
colors = input("What color do you want your shape to be? ")
fred.color(colors)

side = input("How many sides do you want your polygon to be?(NO CIRCLES) ")
numSide = int(side)


for i in range(numSide):
    firstStep = numSide - 2
    multiply = firstStep * 180
    lastStep = multiply/numSide
    fred.forward(50)
    fred.left(180 - lastStep)


