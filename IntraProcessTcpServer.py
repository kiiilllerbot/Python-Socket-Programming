##########################################################
##        Python Socket Programming - TCP Server        ##
##    Intra-process Communication (Different Host)      ##
##              Shimol Khan (D20171079547)              ##
##########################################################

# server

# Importing the SOCKET module
from socket import *

# Defining port as 8080
serverPort = 8080

# Defining socket object and binding it to the port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# Up to 25 request will be listened by the server
serverSocket.listen(25)

while 1:
    # Establish a connection
    connectionSocket, addr = serverSocket.accept()
    # Receive the data and transmit it
    sentence = connectionSocket.recv(1024)
    # Capitalizing the message using upper() function
    capitalizedSentence = sentence.upper()
    # Sending data back to the client
    connectionSocket.send(capitalizedSentence)
    # Close the connection
    connectionSocket.close()
