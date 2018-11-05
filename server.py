import socket
import threading
import socketserver
import time

class PlayerThread(socketserver.BaseRequestHandler):
    
    def sendfile(self, fn):
        f = open(fn,'rb')
        self.request.sendall(fn)
        self.request.sendall('|');
        data = str(self.request.recv(10),'ascii')
        if(data != '1'):
            return
        while True:
            data = f.read()
            if not data:
                break
            self.request.sendall(data)
    
    def sendtext(self, txt):
        self.request.sendall(bytes(txt,'ascii'));
    
    def handle(self):
        #Here's where your communication implement needs to come in. It only runs once, so add a while true loop to continually receive data. Check the socketserver python API if you want any more info on it.
    
    def setup(self):
        #Here's the stuff you do when the connection to the client is established
        #I suggest starting with centralised control. Since you'll have multiple clients, start off 

if __name__ == "__main__":
    HOST, PORT = "localhost", 0
    server = socketserver.ThreadedTCPServer((HOST, PORT), PlayerThread)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
#    server.shutdown()
#    server.server_close()
