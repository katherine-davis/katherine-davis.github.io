##############################################################################
#*********************************-- day 11 --********************************


favoriteFood = input("What is your favorite food? ")

##remember - concatonate mean to glue 2 things together
##so...

sentence = "My favorite food is: " + favoriteFood

##Now an index = a spot for a specific letter in a string
##indexing - retrieving letters out of a string
##valid index range -> 0, to len - 1

firstLetter = favoriteFood[0]

print ("First Letter = " + firstLetter)

numLetters = len(favoriteFood)

lastLetter = favoriteFood[numLetters-1]

print ("Last Letter = " + lastLetter)

print (numLetters)

##colon operator -> starting point : stopping point (:step)

firstThree = favoriteFood[0:3]

print (firstThree)

lastThree = favoriteFood[numLetters-3:numLetters]

print (lastThree)

#pig latin translator

firstHalf = favoriteFood[0: numLetters//2]

print (firstHalf)

secondHalf = favoriteFood [numLetters//2 : numLetters]

print (secondHalf)

test = favoriteFood * 5

print (test)
