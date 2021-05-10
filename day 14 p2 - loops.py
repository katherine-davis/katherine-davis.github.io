###########################################################################
#********************************--day 14 pt2--********************************

for i in range (0,4):
    print(i)

#from this, we can see that the range in the
    #parentheses dictate wha "i" stands for

#Colon operator:
#   start:stop:step

print ("2nd exercise: ")

for i in range (0,10, 2):
    print (i)

print ("3rd exercise: ")

#printing individual letters

word = input("What word do you want? ")

for index in range(0, len (word)):
    print (word[index])

print("----first half----")

for index in range(0,len(word)//2):
    print (word[index])

print("-------")

for index in range (len(word)//2 , len(word)):
    print (word[index])

