import socketserver
import socket
import threading
import pickle

class GM():
    
    sockets = []
    
    def add_socket(self):
        if(len(self.portlist)<=0):
            return
        self.sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.sockets[-1].bind((self.host,self.portlist[0]))
        self.sockets[-1].listen(1)
        conn, addr = self.sockets[-1].accept()
        del self.portlist[0]
        self.sockets[-1] = [self.sockets[-1],conn,addr]
        print('Connected to', self.sockets[-1])
    
    def broadcast(self,msg):
        for i in self.sockets:
            i[1].sendall(bytes(msg,'ascii'))
    
    def __init__(self, host, portlist):
        self.playercount = len(portlist)
        self.portlist = portlist
        self.host = host
        self.add_socket()
        self.add_socket()
        self.add_socket()
        self.broadcast("YOLO!")


portlist = [4876,5554,9922]
host = "localhost"

GM(host,portlist)
