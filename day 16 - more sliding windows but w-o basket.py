##########################################################################
#*******************************--day 15--*******************************

def containsE (word):
    for index in range (0,len(word)):
        letter = word[index]
        if letter == ("e"):
            return True
    return False
            
print (containsE ("where"))


def containsHello (phrase):
    for index in range (0,len(phrase)):
        stoppingPoint = index+5
        window = phrase[index:stoppingPoint]
        if window == "hello":
            return True
    return False

print (containsHello ("hellothere"))
