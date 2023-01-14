"""Here I import socket so that I can use this modules in my program."""
import socket

'''
I assign socket.socket() to Server socket as this will make it easier to use later on in the program,
'''
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

'''
I open a try/except statement. 
In the try statement I get the application to bind the host and port.
It also recieves a message from the server confirming that the client has connected to the server.
In the excpet statement, the application will print out an error, which can be used for debugging.
'''
try:
    ClientSocket.connect((host, port))
    Response = ClientSocket.recv(1024)
    print(Response.decode("utf-8"))
except socket.error as e:
    print(str(e))

"""
Below the user is asked to choose their option of rock, paper or scissors.
Once the user has inputted, their choice is sent to the server application.
The user is informed that the application is waiting to recieve a result from the server.
Once a response is recieved from the server, it is outputted to the client.
The client then closes the connection to the socket and the program ends.
"""
userChoice = input("Do you want to choose rock, paper or scissors?\n: ")
ClientSocket.send(str.encode(userChoice))
print("Waiting for result")
Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
ClientSocket.close()
