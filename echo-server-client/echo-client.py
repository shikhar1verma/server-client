#!/usr/bin/env python
'''
here is the client side program of a tcp connection
which send some message to server and server reply the same
message to the client
'''

import socket                                          #socket library is for basic socket programming
(host,port) = ('127.0.0.1',9999)                       #host is for the server ip and port is port on which server is active
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #it is an instance of a socket an we get an object 's' argument1 is family of protocol and argument 2 is type of communication (here connection oriented
s.connect((host, port))                                #here we connect to the server by makin connection
print 'sending server msg: Hey how are you'            #sent message
s.sendall('Hey how are you')                           #through this method message is sent
data = s.recv(1024)                                    # through .recv we receive the data sent by the server
s.close()                                              #we have to alaways close the connection
print('Received Data:',  data)                         #here we printing the data
