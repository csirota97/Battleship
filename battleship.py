import networking as net
import random

# Principles Of Programming Languages - CS314
# Final Project
# File: battleship.py
# Names: Craig Sirota and Dov Kassai


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
            "YOU SUNK MY ",                             #8
            ]


join_request = "JOIN_REQUESTED"

isHost = -1
start = -1
turns = 0
ships_left = 5


#Converts game position on board to index in list - SEE COMMENT BLOCK BELOW
def boardPosToIndex(pos):
    letter = (ord(pos[0].upper())-65) * 10
    num = int(pos[1:])-1
    return letter+num

#BOARD IS 100 SPACE 1-D LIST
#EVERY 10 SPACES IS EQUIVALENT TO ONE ROW ON BOARD
#INDEX: 00 = A1 : 09 = A10
#       90 = J1 : 99 = J10
#INDEX +/- 10 MOVES VERTICALLY (+ => right : - => left)
#INDEX +/- 1 MOVES HORIZONTALLY(+ => down : - => up)

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


sampleBoard = [0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9,
               0,1,2,3,4,5,6,7,8,9]

#----------------------------------------------------------------------
#SETUP
#----------------------------------------------------------------------

def setup():
    global isHost
    print (messages[0])
    isHost = input (messages[1] + '\n')
    while (isHost != 'H' and isHost != 'J'):
        isHost = input(messages[1] + '\n')

    if isHost == 'H':
        host_setup()
    else:
        join_setup()

def host_setup():
    global isHost
    isHost = 0
    print(messages[2])
    msg = net.rec_set_reciever(14)
    if msg == join_request:
        final_setup()

def final_setup():
    global start, isHost
    start = random.randint(0,1)
    net.send(str(start))
    start = (start+isHost)%2

def join_setup():
    global isHost
    isHost = 1
    net.set_target(input(messages[3]))
    net.send(join_request)
    start = (int(net.rec(1))+isHost)%2

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
        pass


#----------------------------------------------------------------------
#MAIN
#----------------------------------------------------------------------


def main():
    setup()
    play()

#main()
