###############################################################################
#*******************************-- day 7 --*******************************

#Notes
##p = principle
##r = annual interest rate
##n = number of times / year
##t = number of years


##CHALLENGE - find interest


def compoundInterest (p, r, n, t):
    firstStep = r/n
    exponent = n*t
    secondStep = 1 + firstStep
    third = p * secondStep
    fourth = third ** exponent
    return fourth

amount = compoundInterest(100, .01, 1, 1)
print (amount)


##truncation = chopping off the decimal
#to do this you use // in division instead of /

#CHALLENGE TWO
##take in change
##take in the type of bill
##calculate how many needed
##return that amount

def changeMaker(change, typeOfBill):
    numberOfBills = change // typeOfBill
    return numberOfBills

money = input ("What amount of money should I turn into change? ")
amount = int(money)
num10s = changeMaker(amount, 10)
##num10 = str(num10s)
#do this for answer with writing
print (num10s)

amount = amount - num10s * 10
num5s = changeMaker(amount, 5)
print (num5s)

amount = amount - num5s *5
num1s = changeMaker(amount, 1)
print (num1s)

amount = amount - num1s * 1
numQuarters = changeMaker(amount, .25)
print (numQuarters)

amount = amount - numQuarters * .25
numDimes = changeMaker(amount, .10)
print (numDimes)

amount = amount - numDimes * .10
numNickels = changeMaker(amount, .05)
print (numNickels)

amount = amount - numNickels * .05
numPennies = changeMaker(amount, .01)
print (numPennies)


