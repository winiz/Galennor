def welcomeMesg():
    print "Welcome to the Survival and Surprises CMPT 120 Games!"
    print "========================================================="
    
def askTwoValues(val1,val2,question):
    while True:
        truthValue1 = raw_input(question)
        if truthValue1 == val1 or truthValue1 == val2:
            break
        else:
            print "Sorry, was it yes or no?(y/n)"
            continue
    return truthValue1

def inputNumber(a,b,question):
    while True:
        inputNumber = input(question)
        if inputNumber >= a and inputNumber <= b:
            break
        else:
            print "Sorry, The value is not within the required range, retype"
            continue
    return inputNumber

def eXit(val):
    if val == 'n':
        raw_input("OK,Bye, press any key to exit the game then")
        s.exit()

    
def read_string_list_from_file(the_file):
    fileRef = open(the_file,"r") # opening file to be read
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]  # eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)  # adds string to list
        
    fileRef.close()  
    return localList

def whichFile():
    fileName = ''
    while True:
        fileName = raw_input("Type the name of board file including '.txt' or type d for default: ")
        if fileName == "d":
            fileName = "biomesData1.txt"
            break
        elif not ".txt" in fileName:
            print "file with '.txt' please or just d for default........."
            continue
        elif ".txt" in fileName: 
            break
    return fileName


def biomeList():      #name of biome generator
    a = []
    for item in listOfList:
        a.append(item[0])
    return a

def diamon():
    a = []
    for item in listOfList:
         a.append(item[1])
    return a 

def sword():
    a = []
    for item in listOfList:
        a.append(item[2])
    return a

def enemy():
    a = []
    for item in listOfList:
        a.append(item[3])
    return a

def create_lists_board(aList):
    i = -1
    result = []     
    for item in aList:
        i = i + 1
        result += [[str(i)] + item.split('-')]
    return result 
        
                

def show_board(mssg):
    
    print "\nShowing board... " + mssg 
    print "\nThe board at this point contains..."
    print "biome ", "Diam  ", "Sword  ", "Enemy"
    for c in range(len(listOfList)):
        for r in range (len(listOfList[c])):
            print listOfList[c][r], "\t",
        print 

def numberGenerator(a,b):    #numberGenerator generator
    a = r.randint(a,b-1)
    return a

def infoupdate(gameName,Lifepoints,Position,r): #round #
    print
    print "The player", gameName
    print "currently has",Lifepoints, "life points"
    print "has", sword[Position] ,"sword"
    print "has", diamon[Position],"diamonds"
    print "player is in the position:",Position
    if Lifepoints > 0:
        a = "Very alive!!!"
    else:
        a = "Dead... oh no!!!"
    print "So... he(could be a she tho...) is... ", a
    print 
'''
def gameplayed():
    print "yey!!...  the player collected",1, "diamonds"
    
    print "Yey!!...  the player exchanged to a better sword"
    print "The player's new sword is of type: " 2
    print "Oh well... the player tied the fight and", lost 3 "life points"
    print "The player now has ", 7 ,"life points"
'''

############################import level#########################################
import turtle as t
import math as m
import sys as s
import random as r
#############################white level#########################################
welcomeMesg()   #saying hello


truthValueGame = askTwoValues ('y','n',"Do you want to play? (y/n): ")    
eXit(truthValueGame)                     # it would check the value of truthValueGame and then decide weather to quit or not
print

truthValueBoard = askTwoValues('y','n',"Do you want to draw the board? (y/n): ")  #wheater to show the board?
print

fileName = whichFile()    # fileName could be sth.txt or d for default

listStrings = read_string_list_from_file(fileName) # this reads the flie and out put it as a list

listOfList = create_lists_board(listStrings) # i combined all the little lists into this big one

if truthValueBoard == "y":   # some user just don't want to see the board :(
    show_board("just created")
    
###############################data generators##############################################

PythonShine = numberGenerator(1,7)   #PythonShine generator
Lifepoints = numberGenerator(10,50)  #Lifepoints generator
MaximumTurns = numberGenerator(1,10) #MaximumTurns genrator
Position = numberGenerator(1,6) #DiceRoll generator (which is the same as the plyers position)
biomeList = biomeList()
sword = sword()
diamon = diamon()
enemy = enemy()

#################################################################################

print "Which position shall PythonShine be (1..7), ",PythonShine
print
print "Data for player: "
 

gameName = raw_input("Name this game?: ")
print
print "This is player :" , gameName
print
print "Initial life points (10..50)?: ",Lifepoints
print
print "Maximum turns this game? (1..10): ", MaximumTurns
print
catastrophesBoolean = askTwoValues ('y','n',"Allow that catastrophes happen? (y/n): ")
print
surprisesBoolean = askTwoValues ('y','n',"Allow that surprises happen? (y/n): ")
####################showing the board again #########################
print
print "------------------------ready? go!!!!!!!!!!!---------------------"
listOfList[PythonShine][3] = listOfList[PythonShine][3]+ " <=== PythonShine"
listOfList[0][3] = listOfList[0][3] + " <--- Player"
show_board("round 1")
infoupdate(gameName,Lifepoints,0,1)
##################################################
randomBoolean = askTwoValues('d','u',"  Roll die, or user types next pos? (d/u): ") #the user might not want to roll the dice
if randomBoolean == 'd':
    print "which biome should the player go?: ", Position
else:
    Position = inputNumber(0,7, "which biome should the player go?: ")
for i in range (MaximumTurns-1):
    print
    print "showing board...round ",i+2

     



















