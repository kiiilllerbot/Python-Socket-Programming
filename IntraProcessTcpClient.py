##########################################################
##        Python Socket Programming - TCP Client        ##
##     Intra-process Communication (Different Host)     ##
##              Shimol Khan (D20171079547)              ##
##########################################################

# client

# Importing the SOCKET module
import socket

# Importing the AF_INET, SOCK_STREAM from socket module
# from socket import AF_INET, SOCK_STREAM

# Getting the hostname since different computers
serverName = socket.gethostname()

# Setting the port as 8080
serverPort = 8080

# Defining socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connection to hostname on the defined port
clientSocket.connect((serverName, serverPort))

# Getting input
sentence = raw_input('Input lowercase sentence :')
clientSocket.send(sentence)

# Receive no more than 1024 bytes
modifiedSentence = clientSocket.recv(1024)

# Printing the message
print('From '+ serverName + ':', modifiedSentence)

# Close connection
clientSocket.close()
