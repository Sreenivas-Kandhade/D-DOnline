import socket
import time

class Player():
    
    def read(self):
        print(str(self.sock.recv(1024),'ascii'))
    
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))
        print('Client connected')

portlist = [4876,5554,9922]
host = "localhost"

a = Player(host,portlist[0])
time.sleep(3)
b = Player(host,portlist[1])
time.sleep(3)
c = Player(host,portlist[2])
time.sleep(3)

a.read()
b.read()
c.read()
