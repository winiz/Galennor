def welcomeMesg():
    print "Welcome to the Survival and Surprises CMPT 120 Games!"
    print "========================================================="
def askTwoValues(val1,val2,question,errormesg):
    while True:
        truthValue1 = raw_input(question)
        if truthValue1 == val1 or truthValue1 == val2:
            break
        else:
            print errormesg
            continue
    return truthValue1


#top level
welcomeMesg()
truthValueBoard = askTwoValues('y','n',"Do you want to draw the board? (y/n): ","Sorry, was it yes or no?(y/n)")
truthValueGame = askTwoValues ('y','n',"Do you want to play? (y/n): ","Sorry, was it yes or no?(y/n)")
