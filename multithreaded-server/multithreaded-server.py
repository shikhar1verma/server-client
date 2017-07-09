#!/usr/bin/env python

'''
multithreading is used to fullfill the request of
multiple client at the same time by the server
and not go in a queue and done faster than a
single client at a time.In this server script
server act as a echo server
'''


from socket import *        #import all the methods frm socket library
import thread               #import thread so multiple client can connect to server at the same time


HOST = '127.0.0.1'          #ip of server
PORT = 9999                 #port at wich server is running
def response(key):          #showing the data received then sent the same data by the server
    return 'Server response: ' + key

def handler(clientsock,addr):                               #it will send the same data to the client that was sent by the server
    while 1:
        data = clientsock.recv(1024)                        #receive the data from client
        if not data: break
        print repr(addr) + ' recv:' + repr(data)            #repr put anything in a string
        clientsock.send(response(data))                     #send the same data to the client
        print repr(addr) + ' sent:' + repr(response(data))
        if "close" == data.rstrip(): break                  #type 'close' on client console to close connection from the server side

    clientsock.close()
    print addr, "- closed connection"                       #log on console

if __name__=='__main__':                                            #main function
    ADDR = (HOST, PORT)                                             #server ip and port
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)              #so that it will close the already open port
    serversock.bind(ADDR)                                           #it will bind the ip and port so it will make a socket
    serversock.listen(5)                                            #start listening the client max. client is 5
    while 1:                                                        #infinite loop
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()                      #it will accept the connection from the client and make a tcp connection
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))        #it will make a thread for a new client so they can talk to serv er simultaneously

