##########################################################################
#*******************--REVIEW SO WE DONT FAIL THE QUIZ--*******************

#General Format:
#def functionName(optionalParameters):
    #write code
    #return something

#def mystery(strs):
    

##def grabLetter (word, index):
##    #return letter at index
##    letter = word[index]
##    return letter

def firstHalf (string):
    middle = len(string)//2
    firstHalfs = string [0:middle]
    return firstHalfs

print (firstHalf ("nutella"))


def secondHalf (string):
    middle = len(string)//2
    secondHalfs = string[middle: len(string)]
    return secondHalfs

print (secondHalf ("nutella"))


def swapHalves(strs):
    numLetters = len(strs)
    first = firstHalf(strs)
    second = secondHalf(strs)
    return second + first

print (swapHalves ("banana bread"))

def sameFirstLast (word):
    numLetters = len(word)
    firstTwo = word[0:2]
    lastTwo = word [numLetters - 2 : numLetters]
    if firstTwo == lastTwo:
        return True
    else:
        return False

print (sameFirstLast ("nnaaann"))

print (sameFirstLast ("strawberries"))


food = "pineapple"
print (food[4])
    #a
print (food[1:4])
    #ine
print (food[len(food)-3])
    #p
print (food[len(food)])
    #error



    
