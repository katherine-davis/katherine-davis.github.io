# 13 Questions

word = "hello"

##1. printString should print each letter of a string on its own line
##Example:
##
##print(printString(“hello”))
##
##h
##e
##l
##l
##o
def printString(word):
    for i in range (0,len(word)):
        print (word[i])

printString(word)

print ("--------------")
##2. printEveryOther should print every other letter of a string on its own line
##Example:
##
##print(printEveryOther(“hello”))
##
##h
##l
##o
def printEveryOther(word):
    for i in range (0, len(word),2):
        print (word[i])
printEveryOther(word)
print ("-----------")
##3. printBackwards should print every letter of the string on its own line, but backwards
##Example:
##
##print(printString(“hello”))
##
##o
##l
##l
##e
##h
def printBackwards(word):
    backwards = ""
    for index in range(len(word)-1,-1,-1):
        letter = word[index]
        backwards = backwards + letter
    for index in range (0,len(word)):
        print (backwards[index])
        
printBackwards(word)

print ("----------")
##4. printDoubled should print each letter twice, on its own line
##Example:
##
##print(printDoubled(“hello”))
##
##h
##h
##e
##e
##l
##l
##l
##l
##o
##o
##
def printDoubled (word):
    basket = ""
    for index in range(0,len(word)):
        letter = word[index]
        basket = basket + letter*2
    for index in range (0,len(basket)):
        print (basket[index])
printDoubled(word)
print ("---------")


##5. containsA should return true if the parameter has an ‘a’ anywhere in it, false otherwise
##
##print(containsA(“grape”))  -> True
##print(containsA(“kiwi”)) -> False

def containsA(strs):
    for index in range (0,len(strs)):
        letter = strs[index]
        if letter == ("a"):
            return True
    return False

print (containsA("grape"))
print (containsA("kiwi"))

print ("--------")


##6. containsVowel should return true if the parameter has a vowel anywhere in it, false otherwise
##
##print(containsVowel(“grape”))  -> True
##print(containsVowel(“jklmn”)) -> False
##

def containsVowel (strs):
    for index in range (0, len(strs)):
        letter = strs[index]
        if letter == ("a"):
            return True
        if letter == ("e"):
            return True
        if letter == ("i"):
            return True
        if letter == ("o"):
            return True
        if letter == ("u"):
            return True
    return False

print(containsVowel("grape"))
print(containsVowel("jklmn"))

print ("---------")

##7. countVowel should return the number of vowels in the parameter
##
##print(countVowel(“grape”))  -> 2
##print(countVowel(“banana”)) -> 3
##print(containsA(“jklmn”)) -> 0
##

def countVowel (strs):
    basket = 0
    for index in range (0, len(strs)):
        letter = strs[index]
        if letter == ("a"):
            basket = basket + 1
        if letter == ("e"):
            basket = basket + 1
        if letter == ("i"):
            basket = basket + 1
        if letter == ("o"):
            basket = basket + 1
        if letter == ("u"):
            basket = basket + 1
    return basket

print(countVowel("grape"))
print(countVowel("banana"))
print(countVowel("jklmn"))

print ("---------")
    
##8. containsKiwi should return true if ‘kiwi’ is contained anywhere in the string
##
##print(containsKiwi(“Ilovekiwi”)) -> True
##print(containsKiwi(“applesarethegoat”)) -> False
##

def containsKiwi (strs):
    for index in range(0, len(strs)):
        stoppingPoint = index+4
        window = strs[index:stoppingPoint]
        if window == "kiwi":
            return True
    else:
        return False

print (containsKiwi("Ilovekiwis"))
print (containsKiwi("applesarethegoat"))

print ("-----------")

##9. countKiwi should return the number of times ‘kiwi’ is contained anywhere in the string
##
##print(countKiwi(“kiwikiwikiwi”)) -> 3
##print(countKiwi(“applesarethegoat”)) -> 0

def countKiwi(strs):
    basket = 0
    for index in range(0, len(strs)):
        stoppingPoint = index+4
        word = strs[index:stoppingPoint]
        if word == "kiwi":
            basket = basket + 1
    return basket

print(countKiwi("kiwikiwikiwi"))
print(countKiwi("applesarethegoat"))

print ("-----------")


##10. countTarget should take in two parameters, one the string where we’re looking in, and the other a string that we’re looking for. Count how many times the target appears in the big string
##
##print(countTarget(“hellohello”, “ll”)) -> 2
##print(countTarget(“hellohello”, “e”)) -> 2
##print(countTarget(“apple”, “app”)) -> 1
##print(countTarget(“hello”, “app”)) -> 0

def countTarget (wrd, inwrd):
    basket = 0
    for index in range (0, len(wrd)):
        stoppingPoint = index+len(inwrd)
        window = wrd[index:stoppingPoint]
        if window == inwrd:
            basket = basket + 1
    return basket

print(countTarget("hellohello", "ll")) 
print(countTarget("hellohello", "e")) 
print(countTarget("apple", "app"))
print(countTarget("hello", "app"))

print("-------")

##11. containsAdjPair should return true if there are two of the same letter next to each other
##
##print(containsAdjPair(“hello”)) -> True
##print(containsAdjPair(“grape”)) -> False

def containsAdjPair(strs):
    for index in range (0,len(strs)):
        letter = strs[index]
        stoppingPoint = index+2
        word = strs[index:stoppingPoint]
        if word == letter*2:
            return True
    else:
        return False

print(containsAdjPair("hello"))
print(containsAdjPair("grape"))    

print("-------")

##12. interweave should take in two parameters and mix them together. Take the first letter of the first string, then the first letter of the second string, followed by the second letter of the first string, second letter of the second string, etc. You can assume they are the same length
##
##print(interweave(“abc”, “xyz”)) -> axbycz
##print(interweave(“hello”, “there”)) ->htehlelroe
##

def interweave (first, second):
    basket = ""
    for index in range (0, len(first), 1):
        lettera = first[index]
        letterb = second[index]
        stoppingPoint = index+1
        basket = basket + lettera + letterb

    return basket
        
print (interweave ("abc","xyz"))
print (interweave ("hello", "there"))

##13. sandwichType should tell you what appears between two “bread”s.
##
##print(sandwichType(“breadhambread”)) -> ham
##print(sandwichType(“xxbreadpb&jbreadxx”)) -> pb&j
##

def findBread(strs):
    basket = ""
    for i in range (strs):
        letter = strs[index]
        stoppingPoint = index + 5
        word = strs[index:stoppingPoint]
        if word == "bread":
            basket = basket + letter[word:len(strs)]
        return basket

print (findBread ("breadhambread"))
            
            







