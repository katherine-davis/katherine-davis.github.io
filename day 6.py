###############################################################################
#*******************************-- day 6 --*******************************

#Fun with Functions!!

###Review
#Print
print("Hello world!")
#Input
name = input("What is your name?")
print("Hello, " + name)

#Functions have parameters and arguements
#-->things that go inside the parentheses

#There is also something called "return types"
#-->the return type for an input is a string

#We can write our own functions! (Normally at the top)

#def= definition of function
#blue is name of function
#whitespace -> any space that is whit
#funcitons require whitespace, things after defs must be tabed over

def addTwoNumbers(number1, number2):
    result = number1 + number2
    return result

answer = addTwoNumbers(13,13)
print (answer)

answer2 = addTwoNumbers(234234223,8494)
print (answer2)

def tipCalculator (subtotal, taxPerc, tipPerc):
    total= subtotal * taxPerc + subtotal
    tip = total * tipPerc
    print ("The tip is: " + str(tip))
    finalTotal = total + tip
    return finalTotal

##answer3 = finalTotal
##answer3 + tipCalculator(18.50, .075, .25)
##print (answer3)


#a^2 + b^2 = c^2
#c = sqrt(a^2 + b^2)
#Reminder-> in python, exp use ** (2^3 --> 2**3)

side1 = input("What is side 'a' on your triangle?")
side2 = input("What is side 'b' on your triangle? ")
numA = int(side1)
numB = int(side2)

def pythagorean (a, b):
    aSq = numA**2
    bSq = numB**2
    total = aSq + bSq
    finalTotal = (total)**.5
    finaleTotal = str(finalTotal)
    return finalTotal

pleaseWork = pythagorean(numA,numB)
pleaseWorks = str(pleaseWork)
print (pleaseWorks + " is your answer")

##
##OMG I DID IT YESSS FINALLLLY
##


##triangle= pythagorean
##print (triangle)
##
















#Answer
def py(e,f):
    esq = e ** 2
    fsq = f**2
    summed = esq + fsq
    c = summed ** .5
    return c

