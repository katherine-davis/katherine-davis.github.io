##############################################################################
#*********************************-- day 9 --*********************************

import turtle
sandbox = turtle.Screen()
ben = turtle.Turtle()

##conditional statements
##for us to make decisions
##we use conditionals all the time
##Ex: if im hungry, then i'll eat
##
##boolean -> new data type (like int or float or string)
##boolean can only be true(True) of false (False)
##
##
##holder = True
##print (holder)
##
####operators creat booleans
##  >  <  >=  <=  ==  !+
##
##Greater than
##less than
##less than or equal to
##greater than or qual to
##equal
##
##greater7 = 9 > 7
##equalto7 = 9 == 7
##
##print (equalto7)
# = the assignment operator
#single equals assigns a variable a value
#double equals is the comparison operator, it will tell you true or false 

print ("Positive or negative number identifier ")

numbe = input ("What is your number? ")
number = int(numbe)

if number > 0:
    print("Your number is positive :D ")
elif number == 0:
    print("Your number is just zero :) ")
else:
    print ("Your number is negative :0 ")
   

print ("Thank you for your business! ")



for i in range(10):
    benColor = input ("What color do you want Ben (the turtle <3) to be? ")
    direction = input ("What direction do you want to turn? ")
    degrees = input ("How many degrees do you want to turn? ")
    degrees = int(degrees)

    distance = input ("How far do you want to travel? ")
    distance = int(distance)

    penUp = input ("Should your pen be up? (yes or no) ")

    ben.color (benColor)
    
    if direction == "right" and degrees <= 180:
        ben.right(degrees)
    elif direction == "right" and degrees > 180:
        ben.left (360 - degrees)
    elif direction== "left" and degrees <=180:
        ben.left(degrees)
    else:
        ben.right(360-degrees)
    

    if penUp == "yes":
        ben.penup()
    else:
        ben.pendown()
    
    ben.forward(distance)

