"""Here I import socket, _thread and time, so that I can use these modules in my program."""
import socket
from _thread import start_new_thread
import time

'''
I assign socket.socket() to Server socket as this will make it easier to use later on in the program,
I also store the host and port number to the respective variables and set ThreadCount to 0.
'''
ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0


'''
I open a try/except statement. 
In the try statement I get the application to bind the host and port.
In the excpet statement, the application will print out an error, which can be used for debugging.
'''
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

'''
Here I declare the method mainGame.
The purpose of this method is to deterime the winner of the game using both of the players choices.
Depending on the result, the method will return a string.
'''
def mainGame(playerOneChoice, playerTwoChoice):
    results = (playerOneChoice - playerTwoChoice) % 3

    if results == 0:
        return "The game is a tie"
    elif results == 1:
        return "Player 1 wins!!"
    elif results == 2:
        return "Player 2 wins!!"
    else:
        return "Invalid winner"


'''
Here I delcare the method nameToNumber.
The purpose of this method is to convert the users choice to a number so that it can be used later on to determine a winner.
Depending on the choice made by the user a number is returned unless the choice made is invalid
'''
def nameToNumber(name):
    if name == "rock":
        return 1
    elif name == "paper":
        return 2
    elif name == "scissors":
        return 3
    else:
        return "Invalid choice"


'''
Here I delcare the method thread_client.
The purpose of this method is to assign threads to users choices variables.
Once both players choices have been assigned to different  variables. The game will start doing its calculations.
If both users choices are not set. The game will not go ahead.
Once the server has done it calculations for the winner of the game,
it will send the results to both users and close the connection that was opened with them.
'''
def threadedClient(connection):
    connection.send(str.encode('Welcome to Rock, Paper, Scissors\n'))
    playGame = True
    global playerOneChoice
    global playerTwoChoice

    while playGame:
        userChoice = connection.recv(2048)
        userChoice = userChoice.decode("utf-8")
        userNumber = nameToNumber(userChoice)

        if ThreadCount == 1:
            playerOneChoice = userNumber
        elif ThreadCount == 2:
            playerTwoChoice = userNumber
        else:
            playerOneChoice = None
            playerTwoChoice = None

        time.sleep(10)

        if playerOneChoice != None and playerTwoChoice != None:
            playGame = False
            results = mainGame(playerOneChoice, playerTwoChoice)

    connection.sendall(str.encode(results))
    connection.close()


'''
Below is a while loop that runs always runs.
In this loop the server listens on the sockets and for each connection that is recieved, they are assingned a thread 
and the main game takes place. 
'''
while True:
    ServerSocket.listen()
    client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threadedClient, (client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
