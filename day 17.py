###########################################################################
#********************************--day 17--********************************

word = input("What word do you want? ")

def aNoZ (word):
    flag = False
    for index in range (0,len(word)):
        letter = word[index]
        if letter == "z":
            flag = False
        elif letter == "a":
            flag = True
    if flag == True:
        return True
    else:
        return False
    
print (aNoZ (word))

#palendrome = a word thats the same forward and backwards
#taco cat, race car, etc...

phrase = input("What palendrome do you want? ")

def isPalendromeEasy (phrase):
    backwards = ""
    for index in range(len(phrase)-1, -1, -1):
        letter = phrase[index]
        backwards = backwards + letter
    if backwards == phrase:
        return True
    else:
        return False

    
        


