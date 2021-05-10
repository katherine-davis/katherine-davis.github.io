##############################################################################
#*********************************-- day 10 --*********************************

grade = input ("What is your number average? ")
numberGrade = int(grade)

##a-> 90-100
##b-> 80-89
##c->70-79
##d->60-69
##f-> 0-59

##sequential if statements
##vs. elif statements

def letterGrade(numberGrade):

    lettergrade = "Z"
    if numberGrade >= 90:
        letterGrade = "A"
    elif numberGrade >= 80:
        letterGrade = "B"
    elif numberGrade >= 70:
        letterGrade = "C"
    elif numberGrade >= 60:
        letterGrade = "D"
    elif numberGrade < 50:
        letterGrade = "F"
    return letterGrade

print (letterGrade(numberGrade))
