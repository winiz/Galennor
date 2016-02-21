
def welcomeMesg():
    print
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

def infoupdate2(gameName,LifepointsCURRENT,swordCURRENT,diamonCURRENT): #round #
    print
    print "The player", gameName
    print "currently has",LifepointsCURRENT, "life points"
    print "has sword", swordCURRENT 
    print "has", diamonCURRENT,"diamonds"
    print "player is in the position:",Position_new
    if LifepointsCURRENT > 0:
        a = "Very alive!!!"
    else:
        a = "Dead... oh no!!!"
    print "So... he(could be a she tho...) is...",a
    print 


def diamonupdate(Position,diamonCURRENT):
    print 
    print "yey!!...  the player collected",int((1.0/3)* int(diamon[Position])), "diamonds"
    diamonCURRENT += int((1.0/3)*int(diamon[Position]))
    return diamonCURRENT

def swordupdate (Position,swordCURRENT):
    if sword[Position] > swordCURRENT:
        print "Yey!!...  the player exchanged to a better sword"
        swordCURRENT,sword[Position] = sword[Position],swordCURRENT
    print "The player's new sword is of type: ", swordCURRENT
    return swordCURRENT

def Lifepointsupdate(Position,LifepointsCURRENT):
    
    if swordCURRENT < enemy[Position]:
        bloodvalue =  r.randint(1,LifepointsCURRENT+1)                 #If the player has a weaker sword than the enemy, the player will lose life points, a random value, between 1 and all the points he has. 
        print "Oh well... the player fights and lost",bloodvalue, "life points"
        LifepointsCURRENT = LifepointsCURRENT - bloodvalue
        print "The player now has ", LifepointsCURRENT ,"life points"
        
    elif swordCURRENT == enemy[Position]:                                      #If the player has a sword of the same strength as the enemy, he may lose life 44points from 1 to half as many life points as he had so far (if the player’s current points are only 1 he may lose that whole 1 point) 
         bloodvalue =  r.randint(1,LifepointsCURRENT+1)
         print "Oh well... the player fights and lost",bloodvalue/2, "life points"
         LifepointsCURRENT = LifepointsCURRENT - (bloodvalue/2)
         print "The player now has ", LifepointsCURRENT ,"life points"
    else:
         bloodvalue =  r.randint(1,LifepointsCURRENT+1)                                                                    #If the player has a stronger sword than the enemy, he gains more life points, from 1 up to as many as he had before, i.e. potentially doubling his original points. 

         print "Oh well... the player fights and gain",bloodvalue, "life points"
         LifepointsCURRENT = LifepointsCURRENT + bloodvalue
         print "The player now has ", LifepointsCURRENT ,"life points"

    return LifepointsCURRENT

def goback():
        t.penup()
        t.backward(300)
        t.pendown()
        
def draw(a,colour):
    for i in range (a):
        t.fillcolor(colour)
        t.begin_fill()
        for i in range(2):
            t.forward(60)
            t.left(90)
            t.forward (90)
            t.left (90)
        t.forward(70)
        t.end_fill()
        
def biome(PythonShine,notPythonShinecolour,PythonShinecolour):
    draw(PythonShine-1,notPythonShinecolour)   
    draw(1,PythonShinecolour)
    draw(8-PythonShine,notPythonShinecolour)
    
def turtle(val1,val2,question):
    answer = askTwoValues(val1,val2,question)
    if answer == "y":
        print "[Close the turtle window to resume]"
        t.speed(0)
        goback()
        biome (PythonShine,"yellow","purple")
        t.done()


############################ import level #########################################
import turtle as t
import math as m
import sys as s
import random as r
############################ restarter ##################################
restart = 'y'
while restart == 'y':
############################# white level #########################################
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
    
############################### data generators ##############################################

    PythonShine = numberGenerator(0,7)   #PythonShine generator
    Lifepoints = numberGenerator(10,50)  #Lifepoints generator
    MaximumTurns = numberGenerator(1,10) #MaximumTurns genrator
    #DiceRoll generator (which is the same as the plyers position)
    biomeList = biomeList()
    sword = sword()
    diamon = diamon()
    enemy = enemy()
    swordCURRENT = 0
    diamonCURRENT = 0
    LifepointsCURRENT = Lifepoints
    Position2 = numberGenerator(1,6)
    Position_new = 0
    Position_previous = 0
    reason = ''
################################### yellow level ##############################################

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
    if PythonShine != 0:
        listOfList[PythonShine][3] = listOfList[PythonShine][3]+ " <=== PythonShine"
    listOfList[0][3] = listOfList[0][3] + " <--- Player"
########################### start to loop ################################################

    for i in range (MaximumTurns):
        print
        listOfList[0][3] = listOfList[0][3][0]
        # at this point position is most likely not 0 anymore
        listOfList[Position_new][3] = listOfList[Position_new][3] + " <--- Player"
     
    
        show_board("Round " + str(i))
        listOfList[Position_previous][3] = listOfList[Position_previous][3][0]

        infoupdate2(gameName,LifepointsCURRENT,swordCURRENT,diamonCURRENT)   # infomation
        turtle('y','n','Do you want to see the turtle board? (y/n)')
        if LifepointsCURRENT > 0 and Position_new != PythonShine and i == MaximumTurns:   #board 
            print "you won"
            reason = "max number of turns were played" #ending one
            listOfList[Position_new][3] = listOfList[Position_new][3] + " <--- Player"
            break
        elif LifepointsCURRENT < 0:
            print "you lost"
            reason = "you lost all your lifepoints"   #ending two
            listOfList[Position_new][3] = listOfList[Position_new][3] + " <--- Player"
            break
    
        if Position_new != PythonShine or PythonShine == 0:
        
            print "------------------------Ready? go!!!!!!!!!!! Round",i+1, "---------------------"
            randomBoolean = askTwoValues('d','u',"  Roll die, or user types next pos? (d/u): ") #the user might not want to roll the dice
            if randomBoolean == 'd':
                print "the die was...", Position2
                print "the previous position was ... ", Position_previous
                Position_new = (Position_previous + Position2)%8
                print "and the next position is... ", Position_new
            else:
                Position_new = inputNumber(0,7, "which biome should the player go?: ")
            Position_previous = Position_new    
            print "Position_new ",Position_new,"Position_previous ",Position_previous
            diamonCURRENT = diamonupdate(Position_new,diamonCURRENT)
            swordCURRENT = swordupdate (Position_new,swordCURRENT)
            LifepointsCURRENT = Lifepointsupdate(Position_new,LifepointsCURRENT)
        elif Position_new == PythonShine and PythonShine != 0:
            print "you won"
            reason = "you reached PhthonShine!" #ending three
            listOfList[Position_new][3] = listOfList[Position_new][3] + " <--- Player"
            break
############################# End of the game ###########################################        
    print "                RESULTS END OF GAME"
    print "The game ended because",reason
    show_board("end of game")
    if reason == "you reached PhthonShine!":
        diamonCURRENT,LifepointsCURRENT = 9999,9999
    infoupdate2(gameName,LifepointsCURRENT,swordCURRENT,diamonCURRENT)  
    restart = askTwoValues('y','n','Do you want to play again? (y/n)')
########################################################
print 
print "           RESULTS END OF ALL GAMES..........."
print "The user played",1,"games in total"
print "of those, the payer won 0"
print "To conclude, the program will do a conversion from binary to decimal!"
print "taking as source the diamonds list in the last game board"

print "List with diamonds: [0, 10, 10, 3, 7, 10, 7, 5]"
print "Corresponding Binary: [0, 0, 0, 1, 1, 0, 1, 1]"
print "which converted to decimal is: 27"
print
print
print "Bye...."

    

