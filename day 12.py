###########################################################################
#********************************--day 12--********************************

##Write a function called initials
##it to take in three perameters
##    first name
##    last name
##    and middle name
##    and then return their initials         

firstName = input ("What is your first name? ")
middleName = input("What is your middle name? ")
lastName = input("What is your last name? ")


def initials(firstName,middleName, lastName):
    numLettersFirst = len (firstName)
    numLettersMiddle = len (middleName)
    numLettersLast = len (lastName)
    firstInitial = firstName[0]
    middleInitial = middleName [0]
    lastInitial = lastName [0]
    return "Your initials are: " + firstInitial + "." + middleInitial + "." + lastInitial + "."


print (initials(firstName, middleName, lastName))


def fancyInitials(fromTheEnd, first, middle, last):
    if fromTheEnd == False:
        answer = initials(first, middle, last)
        return answer
    else:
        lastFirstInitial = first[len(first-1)]
        lastMiddleInitial = middle[len(middle-1)]
        lastLastInitial = last[len(last-1)]
        firs = str(lastFirstInitial)
        mids = str(lastMiddleInitial)
        lass = str(lastLastInitial)
        return firs + "." + mids + "." + lass + "." 


print (fancyInitials (True, firstName, middleName, lastName))

##
##THIS DOESNT WORK AND I WANT LISTENING SO IM KINDA SCREW BUTS ITS FINE
