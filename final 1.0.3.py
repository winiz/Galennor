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

       
def create_lists_board(aList):
    i = -1
    result = []     
    for item in aList:
        i = i + 1
        result += [[str(i)] + item.split('-')]
    return result 
        
                

def show_board(mssg):
    
    print "\nShowing board... " + mssg 
    print "\n The board at this point contains..."
    print "Biome#    Diam    Sword     Enemy"
    for i in range (len(listOfList)):
        print listOfList[i]


#########################################################
    
#import level
import turtle as t
import math as m
import sys as s

#white level
welcomeMesg()   #saying hello

truthValueGame = askTwoValues ('y','n',"Do you want to play? (y/n): ")    
eXit(truthValueGame)                     # it would check the value of truthValueGame and then decide weather to quit or not

truthValueBoard = askTwoValues('y','n',"Do you want to draw the board? (y/n): ")  #wheater to show the board?

fileName = whichFile()    # fileName could be sth.txt or d for default
listStrings = read_string_list_from_file(fileName) # this reads the flie and out put it as a list

listOfList = create_lists_board(listStrings)


if truthValueBoard == "y":
    show_board("just created")






























