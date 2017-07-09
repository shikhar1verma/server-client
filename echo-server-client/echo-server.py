#!/usr/bin/env python
'''this is a server side program
and we are trying to make a tcp connection with single client
and return the same message to the client that is sent by the
client.
'''

import socket                                          #importing socket library
(server,port)=('127.0.0.1',9999)                       #server is the ip of the server and port is the port it is running on
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket instance and object 's'
s.bind((server, port))                                 #here we binding the ip and the port for getting the socket
s.listen(1)                                            #server start listening to single client
conn, addr = s.accept()                                #accepting the connection requested by client and getting the address of client
print('Connected by', addr)
while 1:
    data = conn.recv(1024)                             #now it goes in infinite loop conn.recv statement is block statement so pointer of program stops there till it gets the value from client
    if not data: break
    conn.sendall(data)                                 #sending same message to the client
    print 'sent msg back',data
conn.close()                                           #always close the comnnection
