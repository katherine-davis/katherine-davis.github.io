###########################################################################
#********************************--day 14--********************************

words = input("What word's first and last letters do you want me to swap? ")

def swap (word):
    firstLetter = word[0]
    lastLetter = word[len(word)-1]
    middle = word[1:len(word)-1]
     
    return lastLetter + middle + firstLetter

print (swap (words))

phrases = input("Another word? ")

def firstTwoAsLastTwo(phrase):
    firstTwo = phrase[0:2]
    lastTwo = phrase[len(phrase)-2:len(phrase)]
    newWord = phrase[0:len(phrase)-2]
    return newWord + firstTwo

print (firstTwoAsLastTwo (phrases))

strs = input("Another? ")

def swapLastTwo (strs):
    lastLetter = strs[len(strs)-1]
    secondLast = strs[len(strs)-2]
    wordWOit = strs[0:len(strs)-2]
    return wordWOit +lastLetter + secondLast

print (swapLastTwo (strs))
