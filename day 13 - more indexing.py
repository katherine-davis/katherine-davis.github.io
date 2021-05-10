###########################################################################
#********************************--day 13--********************************

def lastTwo(word):
    #lastLetter = word[len(word)]
    #That triggers index out of bounds
    lastLetter = word[len(word)-1]
    secondToLastLetter = word[len(word)-2]

    return secondToLastLetter + lastLetter

    #return word[len(word) - 2:len(word) - 1]
##
##def endsWithLY(word):
##    #return True if the word ends with LY, and False if it doesn't
##    lastTwoLetters = lastTwo(word)
##    if lastTwoLetters == ly:
##        return True
##    else:
##        return False
##
##print (endsWithLY("beautifully"))

##def firstALastB(a,b):
##    first = a[0]
##    last = b[len(b) - 1]
##    return first + last
##
##print (firstALastB ("hello", "goodbye"))

def middleTwo(word):
    mid = len(word)//2
    first = word[mid]
    last = word[mid-1]
    return first + last

print (middleTwo ("summer"))

##
##reminder:
##concatonation -> where you combine two strings

def fancyConcatonation (str1, str2):
    lastLetter = str1[len(str1)-1]
    firstLetter = str2[0]
    first = str1[0:len(str1)-1]
    last = str2[1:len(str2)]
    if lastLetter == firstLetter:
        return first +last
    else:
        return str1 + str2


print (fancyConcatonation ("fancy","yellow"))
print (fancyConcatonation ("pan", "cake"))







