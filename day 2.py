#########################################################################
#*************************---DAY 2---************************************

#Review:
#str -> strings (aka text)
#int -> integer (aka whole numbers)
#float -> float (aka decimal numbers)

name = input ("What is your name?")

# input is a fuction (code that is already written we can use)
# has a parameter (something that goes inside parenthesis)

print ("Hello! " + name)

brothers = input("How many brothers do you have?")

print ("You have " + brothers + " brothers")

sisters = input("How many sisters do you have?")

print ("You have " + sisters + " sisters")


numBrothers = int(brothers)
numSisters = int(sisters)
numSiblings = numBrothers + numSisters
siblings = str(numSiblings)

print ("You have " + siblings + " brothers and sisters")

#Rule: + -> str + str = concatenation (gluing)
# + -> int + int = addition
# + -> int + str = ERROR

#------Challenge 1
horse = input("How many horses do you have?")

print ("You have " + horse + " horses")

goat = input("How many goats do you have?")

print ("You have " + goat + " goats")

cow = input("How many cows do you have?")

print ("You have " + cow + " cows")

numHorse = int(horse)
numGoat = int(goat)
numCow = int(cow)
numPets = numHorse + numGoat + numCow
pets = str(numPets)

print ("You have " + pets + " lovable problems")

#-------Challenge 2

birthYear = input("What year were you born?")

birthMathYear = int(birthYear)
howOld = (2021 - birthMathYear)
hoWold = str(howOld)

print ("You are " + hoWold + " years old this year! Happy Birthday!")



















