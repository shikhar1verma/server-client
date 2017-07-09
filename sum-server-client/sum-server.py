#!/usr/bin/env python
'''
this is server which get the numbers from client
as a string and convert those numbers to int and
calculate the sum and convert int to string and
send the result to the client
'''

import socket                                           #socket library
(server,port)=('192.168.43.62',12343)                   # ip and port of the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #socket instantiation and object 's'
s.bind((server, port))                                  #making a socket from ip and port from bind method
s.listen(1)                                             #listen the single tcp client
conn, addr = s.accept()                                 #server accepting the connection request by accept method
print('Connected by', addr)
while 1:                                                #goes in an infinite loop
    data = conn.recv(1024)                              #recv method is a blocking statement which will get the dat from client
    if not data: break                                  #if no data receive aftger some time time then break the loop
    s=[int(i) for i in data.split(' ')]                 #adding the number
    t=s[0]+s[1]
    t=str(t)
    conn.sendall(t)                                     #sending the added numbers as string
    print 'sent sum',t
conn.close()                                            #closing the connection made by server and client
