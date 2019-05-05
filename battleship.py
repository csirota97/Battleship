#!/usr/bin/env python3

from networking import networking as net
import random

# Principles Of Programming Languages - CS314
# Final Project
# File: battleship.py
# Names: Craig Sirota and Dov Kassai



#NOTES
#change when user inputs something when it is not their turn 



#----------------------------------------------------------------------
#UTILITY
#----------------------------------------------------------------------

#Ship class - stores name, size, health, and position of individual ships
class Ship:
    def __init__(self, name, size, startPos, endPos):
        self.name = name
        self.size = size
        self.pos = [startPos]
        if startPos % 10 == endPos % 10:
            k = 1
            if startPos > endPos:
                k = -1
            for i in range (1,size):
                startPos+=(k*10)
                self.pos.append(startPos)
        else:
            k = 1
            if startPos > endPos:
                k = -1
            for i in range (1,size):
                startPos+=(k*1)
                self.pos.append(startPos)

#All strings presented to the user should be stored in this list,
#   with a comment correlating to the index number
messages = [
            "Welcome To Battleship",                    #0
            "Would you like to: \n(H)ost\n(J)oin",      #1
            "Your IP address is " + net.my_ip,          #2
            "Please enter the IP address of the " +     #3
            "server you wish to connect with:\n",
            "You go first",                             #4
            "You go second",                            #5
            "HIT!",                                     #6
            "MISS!",                                    #7
            "YOU SUNK THE ENEMY'S {0}",                 #8
            "Waiting for opponent to place ship",       #9
            "Enter the starting location of your {0}",  #10
            "Enter the ending location of your {0}",    #11
            "Enter location to strike: ",               #12
            "{0} at {1}",                               #13
            "Invalid ship location",                    #14
            "NO SHIP SUNK",                             #15
            "GAME OVER",                                #16
            "YOU WIN",                                  #17
            "YOU LOSE",                                 #18
            "YOUR {0} WAS SUNK",                        #19
            "ERROR:\nPLEASE SEND LOCATION AGAIN",       #20
            "Location already used, please enter new location"  #21
            ]


join_request = "JOIN_REQUESTED"

isHost = -1
start = -1
turns = 0
ships_left = 0


#Converts game position on board to index in list - SEE COMMENT BLOCK BELOW
def boardPosToIndex(pos):
    pos = pos.replace(" ", "")
    letter = (ord(pos[0].upper())-65)
    num = (int(pos[1:])-1)*10
    return letter+num

#BOARD IS 100 SPACE 1-D LIST
#EVERY 10 SPACES IS EQUIVALENT TO ONE ROW ON BOARD
#INDEX: 00 = A1 : 09 = A10
#       90 = J1 : 99 = J10
#INDEX +/- 10 MOVES VERTICALLY (+ => right : - => left)
#INDEX +/- 1 MOVES HORIZONTALLY(+ => down : - => up)


def isValidAlpha(str):
    if "abcdefghijABCDEFGHIJ".__contains__(str[0]):
        return 1
    return 0

def check_validity(string):
    if len(string)==2 or len(string)==3:
        if isValidAlpha(string[0]):
            if string[1:].isdigit():
                if hitmap[boardPosToIndex(string)] == " ":
                    print(hitmap[boardPosToIndex(string)])
                    return 1
                else:
                    print(messages[21])
    return 0





def printBoard(board):
    row = "   +-+-+-+-+-+-+-+-+-+-+"
    print ("    A B C D E F G H I J\n"+ row)
    rows = []
    cur_row = "1  |"
    for i in range(len(board)):
        cur_row+=str(board[i])+"|"
        if i % 10 == 9:
            rows.append(cur_row)
            if int(i/10)+2 < 10:
                cur_row = str(int(i/10)+2) + "  |"
            else:
                cur_row = str(int(i/10)+2) + " |"
    for i in range(len(rows)):
        print(rows[i])
        print(row)


playerBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
               ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

hitmap = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

ships = []
#----------------------------------------------------------------------
#SETUP
#----------------------------------------------------------------------

def setup():
    global isHost
    
    f = open("networking/config.svg", "w")
    f.write("" )
    f.close()
    
    print (messages[0])
    isHost = input (messages[1] + '\n').upper()
    while (isHost != 'H' and isHost != 'J'):
        isHost = input(messages[1] + '\n').upper()

    if isHost == 'H':
        host_setup()
    else:
        join_setup()

def host_setup():
    global isHost
    isHost = 1
    print(messages[2])
    msg = net.rec_set_reciever(32) #
    if msg == join_request:
        final_setup()

def final_setup():
    global start, isHost
    start = random.randint(0,1)
    net.send(str(start))
    print(net.reciever_ip)
    start = (start+isHost)%2

def join_setup():
    global isHost, start
    isHost = 0
    net.set_target(input(messages[3]))
    net.send(join_request)
    start = (int(net.rec(1))+isHost)%2

def new_ship(name, size):
    global playerBoard
    printBoard(playerBoard)
    start = int(boardPosToIndex(input(messages[10].format("{0} - size {1}: ".format(name,size)))))
    
    legalPlacement = 1
    
    while (start > 99 or start < 0):
        start = int(boardPosToIndex(input(messages[10].format("{0} - size {1}: ".format(name,size)))))
        
    end = int(boardPosToIndex(input(messages[11].format("{0} - size {1}: ".format(name,size)))))

    oogyboogy = [start]
    start2 = start
    if start2 % 10 == end % 10:   #column
        k = 1
        if start2 > end:
            k = -1
        for i in range (1,size):
            start2+=(k*10)
            oogyboogy.append(start2)
    else:                           #row
        k = 1
        if start2 > end:
            k = -1
        for i in range (1,size):
        
            start2+=(k*1)
            oogyboogy.append(start2)

#    print (oogyboogy)

    for i in range(len(oogyboogy)):
#        print ('"'+playerBoard[oogyboogy[i]]+'"')
        if playerBoard[oogyboogy[i]] != ' ':
            legalPlacement = 0
            break

#    print(size)
#    print (legalPlacement == 0)
#    print (end > 99 or end < 0)
#    print (abs(end - start) != size-1)
#    print (end)
#    print (start)
#    print (end - start)
#    print (abs(end-start))
#    print (str(abs(end - start)) + ","+ str(size-1))
#    print (abs(end - start) != (size-1)*10 )
#    print(end > 99 or end < 0)
        #    while (((int(start/10) != int(end/10) or abs(end-start) != size-1) and (start% 10 != end%10 or abs(end-start) != (size-1)*10))
        #    or end > 99 or end < 0
        #   or legalPlacement == 0):

    while (legalPlacement == 0
           or end > 99 or end < 0
           or (abs(end - start) != size-1 and abs(end - start) != (size-1)*10 )):
        print (messages[14])
        
        if legalPlacement == 0:
            start = int(boardPosToIndex(input(messages[10].format("{0} - size {1}: ".format(name,size)))))

            legalPlacement = 1
            
            while (start > 99 or start < 0):
                start = int(boardPosToIndex(input(messages[10].format("{0} - size {1}: ".format(name,size)))))
        
        
        end = int(boardPosToIndex(input(messages[11].format("{0} - size {1}: ".format(name,size)))))
#print (end)

        start2 = start
        oogyboogy = [start]
        if start2 % 10 == end % 10:   #column
            k = 1
            if start2 > end:
                k = -1
            for i in range (1,size):
                start2+=(k*10)
                oogyboogy.append(start2)
        else:                           #row
            k = 1
            if start2 > end:
                k = -1
            for i in range (1,size):
                start2+=(k*1)
                oogyboogy.append(start2)

        for i in range(len(oogyboogy)):
            if playerBoard[oogyboogy[i]] != ' ':
                legalPlacement = 0
                break

    ships.append(Ship(name, size, start, end))

    c= ''
    if name == "Aircraft Carrier":
        c = 'a'
    elif name == "Battleship":
        c='b'
    elif name == "Destroyer":
        c='d'
    elif name == "Submarine":
        c='s'
    elif name == "Patrol Boat":
        c='p'
    
    
    
    if start % 10 == end % 10:
        k = 1
        if start > end:
            k = -1
        for i in range (0,size):
            playerBoard[start]=c
            start+=(k*10)
    else:
        k = 1
        if start > end:
            k = -1
        for i in range (0,size):
            playerBoard[start]=c
            start+=(k*1)
    


def place_ships():
    global playerBoard, ships, isHost
    if isHost:
        try:
            new_ship("Aircraft Carrier", 5)
            net.send(str(1))
        except ValueError:
            new_ship("Aircraft Carrier", 5)
            net.send(str(1))

        print(messages[9])
        net.rec(1)

        try:
            new_ship("Battleship", 4)
            net.send(str(1))
        except ValueError:
            new_ship("Battleship", 4)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Destroyer", 3)
            net.send(str(1))
        except ValueError:
            new_ship("Destroyer", 3)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Submarine", 3)
            net.send(str(1))
        except ValueError:
            new_ship("Submarine", 3)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Patrol Boat", 2)
            net.send(str(1))
        except ValueError:
            new_ship("Patrol Boat", 2)
            net.send(str(1))

        print(messages[9])
        net.rec(1)


    else:
        print(messages[9])
        net.rec(1)
        try:
            new_ship("Aircraft Carrier", 5)
            net.send(str(1))
        except ValueError:
            new_ship("Aircraft Carrier", 5)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Battleship", 4)
            net.send(str(1))
        except ValueError:
            new_ship("Battleship", 4)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Destroyer", 3)
            net.send(str(1))
        except ValueError:
            new_ship("Destroyer", 3)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Submarine", 3)
            net.send(str(1))
        except ValueError:
            new_ship("Submarine", 3)
            net.send(str(1))

        print(messages[9])
        net.rec(1)
        try:
            new_ship("Patrol Boat", 2)
            net.send(str(1))
        except ValueError:
            new_ship("Patrol Boat", 2)
            net.send(str(1))
#----------------------------------------------------------------------
#PLAY
#----------------------------------------------------------------------

def play():
    global turns, start, messages
    
    if start:
        print(messages[4])
    else:
        print(messages[5])

    while 1:
        if start==0 and turns==0:
            turns +=1
            try:
                msg = net.rec(3)
                msg2,lcheck,sunk = check_player_map(msg)
                net.send(msg2)
            except ValueError:
                msg = net.rec(3)
                msg2,lcheck,sunk = check_player_map(msg)
                net.send(msg2)
            
            print(messages[13].format(msg2, msg))
            printBoard(hitmap)
            printBoard(playerBoard)
        
        #---------------------------------------------------------
        
        player_move = input(messages[12])
        while not check_validity(player_move):
            print(messages[20])
            player_move = input(messages[12])
        net.send(player_move)
        msg2 = net.rec(len(messages[8])+16).upper()
        msg = net.rec(5)
#        print(msg,player_move)
        update_hitmap(msg,player_move)

        if msg == messages[16][0:5]:
            print(messages[13].format(messages[6], player_move))
        else:
            print(messages[13].format(msg, player_move))
        if msg2 != messages[15]:
            print(msg2)
        printBoard(hitmap)
        printBoard(playerBoard)
        if msg == messages[16][0:5]:
            print(messages[17])
            return


        #---------------------------------------------------------
        
        try:
            msg = net.rec(3)
            msg2,lcheck, sunk = check_player_map(msg)
            net.send(msg2)
        except ValueError:
            msg = net.rec(3)
            msg2,lcheck, sunk = check_player_map(msg)
            net.send(msg2)
        print(messages[13].format(msg2, msg))
        if sunk:
            print(messages[19].format(sunk.upper()))
        printBoard(hitmap)
        printBoard(playerBoard)

        if lcheck == 1:
            print(messages[18])
            return


            
def update_hitmap(variable, location):
    if variable == messages[6] or variable == messages[16][0:5]:
        hitmap[boardPosToIndex(location)] = "X"
    elif variable==messages[7]:
        hitmap[boardPosToIndex(location)] = "O"

def check_player_map(location):
    lose = 0
    sunk = ''
    if " " != playerBoard[boardPosToIndex(location)]:
        playerBoard[boardPosToIndex(location)]= "X"
        for i in range(len(ships)):
            if ships[i].pos[0]%10 == boardPosToIndex(location)% 10 or int(ships[i].pos[0]/10) == int(boardPosToIndex(location)/10):
                for j in range(len(ships[i].pos)):
                    if ships[i].pos[j]==boardPosToIndex(location):
                        ships[i].pos.remove(ships[i].pos[j])
                        if len(ships[i].pos)==0:
                            sunk = ships[i].name
                            net.send(messages[8].format(ships[i].name))
                            ships.remove(ships[i])
                            if len(ships) == 0:
                                net.send(messages[16])
                                lose = 1
                        else:
                            net.send(messages[15])
                        return messages[6], lose, sunk

        net.send(messages[15])
        return messages[6], lose, sunk
    else:
        playerBoard[boardPosToIndex(location)]= "O"
        net.send(messages[15])
        return messages[7], lose, sunk



#----------------------------------------------------------------------
# this is where the gameplay happens
# ---------------------------------------------------------------------

# send the location you want to hit 
# either it is a hit or a miss 
    # if it is a hit then you update their playermap, update their ships list 
# then update your hitmap and their playermap a
#wait for response from other player 




#----------------------------------------------------------------------
#MAIN
#----------------------------------------------------------------------

def main():
    setup()
    place_ships()
    play()

    
    f = open("networking/config.svg", "w")
    f.write("" )
    f.close()

main()
