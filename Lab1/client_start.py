# from the socket module import all
from socket import *
import socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
HOST = socket.gethostname()
PORT = 6000
server_address = (HOST, PORT)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
client.connect(server_address)
try:
    
    # Send data
    message = 'This is the message from the client to the server.'
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    client.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
     # Data is read from the connection with recv()
        # decode() function returns string object
        data = client.recv(16).decode()
        amount_received += len(data)
        print('received "%s"' % data)
finally:
    print('closing socket')
    client.close()
