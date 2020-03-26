##########################################################
##        Python Socket Programming - TCP Client        ##
##        Interprocess Communication (Same Host)        ##
##              Shimol Khan (D20171079547)              ##
##########################################################

# client

# Importing the SOCKET module
from socket import*

# Importing the AF_INET, SOCK_STREAM from socket module
from socket import AF_INET, SOCK_STREAM

# Setting the server name as LOCALHOST
serverName = "localhost"

# Setting the port as 8080
serverPort = 8080

# Defining socket object
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connection to hostname on the defined port
clientSocket.connect((serverName, serverPort))

# Getting input
sentence = raw_input('Input lowercase sentence :')
clientSocket.send(sentence)

# Receive no more than 1024 bytes
modifiedSentence = clientSocket.recv(1024)

# Printing the message
print('From Server : ', modifiedSentence)

# Close connection
clientSocket.close()
