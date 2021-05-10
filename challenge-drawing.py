###############################################################################
#*******************************-- CHALLENGE --*******************************



import turtle

sandbox = turtle.Screen()
derek = turtle.Turtle()
derek.shape("turtle")
derek.speed(0)


#body of airplane
derek.left(90)
derek.forward(25)
derek.left(40)
derek.forward(27)
derek.right(120)
derek.forward(100)

derek.right(130)
derek.forward(90)

derek.right(105)
derek.forward(27)

derek.right(92)
derek.forward(85)

derek.left(162)
derek.forward(88)
derek.backward(88)
derek.left(15)
derek.forward(102)

derek.right(120)
derek.forward(4)
derek.backward(4)

derek.left(275)
derek.forward(20)


#dotted tail
derek.penup()
derek.backward(20)
derek.left(20)
derek.backward(15)

derek.pendown()
derek.backward(30)

derek.penup()
derek.backward(15)
derek.pendown()

derek.left(180)

#1st number size o circle, 2nd amount of circle (180 = semi circle)
derek.circle(30,40)

derek.penup()
derek.forward(15)
derek.pendown()

derek.circle(35,40)

derek.penup()
derek.forward(15)
derek.pendown()

derek.circle(20,40)

derek.penup()
derek.forward(15)
derek.pendown()

derek.circle(20,50)

derek.penup()
derek.forward(15)
derek.pendown()

derek.circle(20,60)

derek.penup()
derek.forward(15)
derek.pendown()

derek.circle(20,60)

derek.penup()
derek.forward(15)
derek.pendown()

derek.circle(20,60)

derek.right(20)
derek.penup()
derek.forward(15)
derek.pendown()

derek.forward(7)
derek.right(12)
derek.forward(10)

derek.right(20)
derek.penup()
derek.forward(8)
derek.pendown()

derek.right(20)
derek.forward(10)
derek.right(9)
derek.forward(10)

derek.penup()
derek.forward(12)
derek.pendown()

derek.left(15)
derek.forward(15)

derek.penup()
derek.forward(12)
derek.pendown()

derek.left(15)
derek.forward(15)

derek.penup()
derek.forward(12)
derek.pendown()

derek.left(15)
derek.forward(15)

derek.penup()
derek.forward(12)
derek.pendown()

derek.left(20)
derek.forward(15)

derek.penup()
derek.forward(10)
derek.pendown()

derek.left(20)
derek.forward(15)

derek.penup()
derek.forward(10)
derek.pendown()

derek.left(20)
derek.forward(15)

#get to sun
derek.penup()
derek.right(160)
derek.forward(210)
derek.pendown

#sun
derek.color("#FEE12B")
derek.begin_fill()
derek.circle(50)
derek.end_fill()

#sun's dark rays
derek.right(90)
derek.penup()
derek.forward(10)
derek.pendown()
derek.forward(20)
derek.backward(20)
derek.penup()
derek.backward(10)
derek.left(90)
derek.circle(50,60)

derek.right(90)
derek.penup()
derek.forward(10)
derek.pendown()
derek.forward(20)
derek.backward(20)
derek.penup()
derek.backward(10)
derek.left(90)
derek.circle(50,60)

derek.right(90)
derek.penup()
derek.forward(10)
derek.pendown()
derek.forward(20)
derek.backward(20)
derek.penup()
derek.backward(10)
derek.left(90)
derek.circle(50,60)

derek.right(90)
derek.penup()
derek.forward(10)
derek.pendown()
derek.forward(20)
derek.backward(20)
derek.penup()
derek.backward(10)
derek.left(90)
derek.circle(50,60)

derek.right(90)
derek.penup()
derek.forward(10)
derek.pendown()
derek.forward(20)
derek.backward(20)
derek.penup()
derek.backward(10)
derek.left(90)
derek.circle(50,60)

derek.right(90)
derek.penup()
derek.forward(10)
derek.pendown()
derek.forward(20)
derek.backward(20)
derek.penup()
derek.backward(10)
derek.left(90)
derek.circle(50,60)


#sun's light rays

derek.circle(50,30)

derek.penup()

derek.color("#EFFD5F")

derek.right(90)

derek.forward(5)
derek.pendown()
derek.forward(45)
derek.backward(45)
derek.penup()
derek.backward(5)
derek.left(90)
derek.circle(50,60)

derek.right(90)

derek.forward(5)
derek.pendown()
derek.forward(45)
derek.backward(45)
derek.penup()
derek.backward(5)
derek.left(90)
derek.circle(50,60)

derek.right(90)

derek.forward(5)
derek.pendown()
derek.forward(45)
derek.backward(45)
derek.penup()
derek.backward(5)
derek.left(90)
derek.circle(50,60)

derek.right(90)

derek.forward(5)
derek.pendown()
derek.forward(45)
derek.backward(45)
derek.penup()
derek.backward(5)
derek.left(90)
derek.circle(50,60)

derek.right(90)

derek.forward(5)
derek.pendown()
derek.forward(45)
derek.backward(45)
derek.penup()
derek.backward(5)
derek.left(90)
derek.circle(50,60)

derek.right(90)

derek.forward(5)
derek.pendown()
derek.forward(45)
derek.backward(45)
derek.penup()
derek.backward(5)
derek.left(90)
derek.circle(50,60)

sun highlights
derek.left(90)
derek.forward(40)
derek.color("#FFEE75")
derek.pendown()
derek.begin_fill()
derek.circle(20,360)
derek.end_fill()

##
##Top view---------------------------------
##derek.reset()
##derek.left(70)
##derek.forward(100)
##derek.backward(100)
##derek.left(10)
##derek.forward(110)
##derek.backward(110)
##derek.left(10)
##derek.forward(110)
##derek.backward(110)
##Mayyybee later----------------------------
##
##def make_a_paper_airplane
##derek.forward(80)
##derek.backward(80)
##derek.right(130)
##derek.forward(10)
##derek.left(135)
##derek.forward(80)
##derek.right(170)
##derek.forward(80)
##derek.right(110)
##derek.forward(12)
##
##




##
##derek.right(105)
##derek.forward(200)
##derek.color("#39f077")
##derek.right(12)
##derek.forward(100)
