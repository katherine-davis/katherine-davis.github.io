def mystery(strs):
    numLetters = len(strs)
    firstHalf = strs[0:numLetters//2]
    secondHalf = strs[numLetters//2: numLetters]
    firstLet = strs[0:1]
    lastLet = strs[numLetters-1:numLetters]
    if firstLet == "a":
        return firstHalf
    if lastLet == "z":
        return secondHalf
    else:
        return strs *3

print(mystery("apple"))
print(mystery("grapez"))
print(mystery("banana"))

word = "hamburger"

print(word[4])
print(word[0:3])
print(word[len(word)-2])
##print(0:word[len(word):2)


# oh non... this could be bad for me
