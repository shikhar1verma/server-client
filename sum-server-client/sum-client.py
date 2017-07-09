#!/usr/bin/env python
'''
here the user from client give two numbers for
addition and the numbers will go as string to
server side and server will calculate the value
and send back the results to client side
'''

import socket                                           #socket library
(host,port) = ('192.168.43.62',12343)                   #host is the ip of the server and port is port no. of the server is running on
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)  #socket instantiation and object 's'
s.connect((host, port))                                 #connect method trying to establish connection with server
print 'enter numbers for addition on server side'
a=raw_input()                                           #user input
s.sendall(a)                                            #sending the input of user
data = s.recv(1024)                                     #data received by the client
s.close()                                               #closing the connection
print('Received Data:',  data)
