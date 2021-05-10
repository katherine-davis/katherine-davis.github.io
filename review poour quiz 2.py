#########################################################################
#*************************---REVIEW FOR QUIZ 2---*************************


#Example:
def printEveryThree(str):
  for i in range(0, len(str)):
      stop = i + 3
      window = str[i:stop]
      print (window)

printEveryThree("hello")


#1

print ("----------")

def testforTarget(strs, target):
    for i in range(0, len(strs)):
        numtar = len(target)
        stop = i+numtar
        window = strs[i:stop]
        if window == target:
            return True
    else:
        return False


    
##    for i in range (0, len(strs)):
##        numletters = len(target)
##        stop = i + numletters
##        window = strs[i:stop]
##        if window == target:
##            return True
##    else:
##        return False


print (testforTarget("Giraffe", "raf"))
       
print (testforTarget("Giraffe", "rafs"))


#2

print("-----------")

def countAdjDuplicates(phrase):
    basket = 0
    for i in range (0, len(phrase)-1):
        let1 = phrase[i]
        let2 = phrase [i+1]
        if let1 == let2:
            basket = basket +1
    return basket

    
##    basket = 0
##    for i in range (0, len(phrase)-1):
##        firstlet = phrase[i]
##        secondlet = phrase[i+1]
##        if firstlet == secondlet:
##            basket = basket + 1
##    return basket



print (countAdjDuplicates("Good Guy Greg"))
print (countAdjDuplicates("Giraffe"))
print (countAdjDuplicates("Material"))



#3

print ("----------")
        
def ABCtester (string):
    basketa = 0
    basketb = 0
    basketc = 0
    for i in range(0, len(string)):
        letter = string[i]
        if letter == "A":
            basketa = basketa +1
        if letter == "B":
            basketb = basketb + 1
        if letter == "C":
            basketc = basketc+1
    if basketa >= basketb and basketa >= basketc:
        return "A"
    if basketb >= basketa and basketb >= basketc:
        return "B"
    if basketc >= basketa and basketc >= basketb:
        return "C"

print (ABCtester("AAABBCC"))
print(ABCtester("ABBBCC"))
print(ABCtester("ABCCCC"))
