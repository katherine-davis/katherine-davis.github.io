###########################################################################
#******************************--day 14 pt2--******************************


#aggregation -> fancy word for collection
basket = 0
word = "abchiabchello"

for index in range(0,len(word)):  #0, 1, 2, 3...-7
    egg = word[index]
    if egg ==("a"):
        basket = basket + 1  #update (video time 6:51)

print (basket)
print ("done")

#sliding window algorithem (11:00 in video?? i think, she paused for a little bit)
#pretend she wants us to find a series of letters (12:40ish)
#pattern recogniction
##we as humans can immidiately read text and be able to see patterns
##but computers have to be coded this way, so that's what we're coding...
#        in computers you have to individually chack each three characters to find patterns
##16:20 in the video how to do this
#you will have to find the range
# tried at 17:50 ish to show the board XD it may not have worked

#so in looking for patterns of three, the brackets will have these number in them
 #[number:number+3] explains sort of at 20:10

#actually doing the code...


#counting abc's
abcBasket = 0
for index in range(0, len(word)):
    #need to calculate stopping point
    stoppingPoint = index+3
    #get out your window (amount of letters it will be looking at at one time)
    window = word[index:stoppingPoint]
    if window == "abc":
        abcBasket = abcBasket + 1
print (abcBasket)

#by 24:30 it was basically the end of class
