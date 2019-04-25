import networking as net
import random

# Principles Of Programming Languages - CS314
# Final Project
# File: battleship.py
# Names: Craig Sirota and Dov Kassai



#NOTES
    # chamge so the input of row and column would be ROW: ___ and COLUMN: ____



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
            "YOU SUNK MY {0}",                          #8
            "Waiting for opponent to place ship",       #9
            "Enter the starting location of your {0}",  #10
            "Enter the ending location of your {0}",    #11
            "Enter location to strike: ",               #12
            "{0} at {1}",                               #13
            "Invalid ship location",                    #14
            ]


join_request = "JOIN_REQUESTED"

isHost = -1
start = -1
turns = 0
ships_left = 0


#Converts game position on board to index in list - SEE COMMENT BLOCK BELOW
def boardPosToIndex(pos):
    letter = (ord(pos[0].upper())-65)
    num = (int(pos[1:])-1)*10
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
    if start % 10 == end % 10:   #column
        k = 1
        if start > end:
            k = -1
        for i in range (1,size):
            start+=(k*10)
            oogyboogy.append(start)
    else:                           #row
        k = 1
        if start > end:
            k = -1
        for i in range (1,size):
            start+=(k*1)
            oogyboogy.append(start)

    print (oogyboogy)

    for i in range(len(oogyboogy)):
        if playerBoard[oogyboogy[i]] != ' ':
            legalPlacement = 0
            break

    print (end)
    while ((int(start/10) != int(end/10) or abs(end-start) != size-1 or legalPlacement == 0)
           and (start% 10 != end%10 or abs(end-start) != (size-1)*10)
           or end > 99 or end < 0):
        print (messages[14])
        end = int(boardPosToIndex(input(messages[11].format("{0} - size {1}: ".format(name,size)))))
        print (end)

        oogyboogy = [start]
        if start % 10 == end % 10:   #column
            k = 1
            if start > end:
                k = -1
            for i in range (1,size):
                start+=(k*10)
                oogyboogy.append(start)
        else:                           #row
            k = 1
            if start > end:
                k = -1
            for i in range (1,size):
                start+=(k*1)
                oogyboogy.append(start)

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
        c='c'
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
        new_ship("Aircraft Carrier", 5)
        net.send(str(1))
        
        print(messages[9])
        net.rec(1)
        new_ship("Battleship", 4)
        net.send(str(1))
    
        print(messages[9])
        net.rec(1)
        new_ship("Destroyer", 3)
        net.send(str(1))
        
        print(messages[9])
        net.rec(1)
        new_ship("Submarine", 3)
        net.send(str(1))

        print(messages[9])
        net.rec(1)
        new_ship("Patrol Boat", 2)
        net.send(str(1))

        print(messages[9])
        net.rec(1)


    else:
        print(messages[9])
        net.rec(1)
        new_ship("Aircraft Carrier", 5)
        net.send(str(1))

        print(messages[9])
        net.rec(1)
        new_ship("Battleship", 4)
        net.send(str(1))
        
        print(messages[9])
        net.rec(1)
        new_ship("Destroyer", 3)
        net.send(str(1))

        print(messages[9])
        net.rec(1)
        new_ship("Submarine", 3)
        net.send(str(1))

        print(messages[9])
        net.rec(1)
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
            msg = net.rec(2)
            msg2 = check_player_map(msg)
            net.send(msg2)
            print(messages[13].format(msg2, msg))
            printBoard(hitmap)
            printBoard(playerBoard)
        player_move = input(messages[12])
        net.send(player_move)
        msg = net.rec(5)
        update_hitmap(msg,player_move)
        print(messages[13].format(msg, player_move))
        printBoard(hitmap)
        printBoard(playerBoard)
         

        
        msg = net.rec(2)
        msg2 = check_player_map(msg)
        net.send(msg2)
        print(messages[13].format(msg2, msg))
        printBoard(hitmap)
        printBoard(playerBoard)
        


            
def update_hitmap(variable, location):
    if variable == messages[6]:
        hitmap[boardPosToIndex(location)] = "X"
    elif variable==messages[7]:
        hitmap[boardPosToIndex(location)] = "O"

def check_player_map(location):
        if " " != playerBoard[boardPosToIndex(location)]:
            playerBoard[boardPosToIndex(location)]= "X"
            for i in range(len(ships)):
                if ships[i].pos[0]%10 == boardPosToIndex(location)% 10 or int(ships[i].pos[0]/10) == int(boardPosToIndex(location)/10):
                    for j in range(len(ships[i].pos)):
                        if ships[i].pos[j]==boardPosToIndex(location):
                            ships[i].pos.remove(j)
                            if len(ships[i].pos)==0:
                                ships.remove(ships[i])
                            return messages[6]
        else:
            playerBoard[boardPosToIndex(location)]= "O"
            return messages[7]



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

main()
