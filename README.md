# Battleship
Final Project for Principles of Programming Languages (CS 314) at Rutgers University with Jeff Ames.

By Craig Sirota (cms631) and Dov Kassai (dk778)

For our final project, we recreated the classic guessing game, Battleship. Players are able to play games with their friends. A chat players to communicate with each other, enhancing the game experience.

Also check out FinalAssignmentProposal_Battleship.pdf

# Run The Game
In order to run the game, navigate to the /Battleship directory in your command line, then run the game by using the command:
>python3 battleship.py

In you would like to also take advantage of the chat functions, 2 additional terminal windows are required to be open in the same directory. Once battleship.py is running, in the first of the two new windows, run
>python3 comms.py

and in the other window, run

>python3 chat.py


# Gameplay
Once you run battleship.py, you will be prompted for whether you would like to either host or join a game. When playing with a friend, one person must host and one person must join.

To select, enter 'h' to host a game or 'j' to join a game.

If you select host, you will be prompted with your IP address, which the other player must enter. If the IP address was entered correctly, the host will be given a screen to place a ship. Players will alternate taking turns placing ships by entering the starting and ending coordinates when prompted, starting from largest to smallest. Coordinates should be formatted Column_letterRow_number (a1, b2, c3, etc.).

Ship Name - Size - Symbol

Aircraft Carrier - 5 - a

Battleship - 4 - b

Destroyer - 3 - d

Submarine - 3 - s

Patrol Boat - 2 - p

Once all ships have been placed, a player will randomly assigned to go first. On your turn, two boards will be printed out. The first board is your hitmap, which shows what locations you have already attacked. An empty spot means it has not been attacked, an 'X' means you hit a ship there, and an 'O' means you attacked that location but there was no ship there. The second board is your shipmap. Like the hit map, empty, 'X', and 'O' coorespond to an empty space, hit, and a miss; however, you will also see other characters on the board. These characters are the symbols of your ships, cooresponding to the locations of your ships. When prompted, enter a coordinate that you would like to attack on the opposing board. It is recommended to use your hitmap to guide your decision.

After your attack, you will be returned of whether you hit or missed their ship. If you sunk a ship, you will be alerted that you sunk their <ship name>, and your updated hitmap and shipmap will be printed.

When it is not your turn, you will wait for your opponent to enter a coordinate. Once they do, you will be alerted of whether or not they hit you, and if they sunk a ship. Then your hitmap and updated shipmap will be printed out, and you will be prompted to attack.

# Chat

When running the chat window and comm window, once a connection has been estabilshed between the two players in battleship.py, the communation windows will display connected. The window running chat.py will display the following:

":>"

After this symbol, you enter your message and hit enter to send. The message will then appear in the window running comms.py. Messages will be displayed as either your message or the opponent's message.


# Testing
If you would like to play the game with only patrol boats, in order to make testing faster comment out the following lines:

327-363

377-410
