import os
from socket import *
class NetworkConnect:
    def __init__(self):
        self.host = "10.0.0.2" # set to IP address of target computer
        self.port = 13000
        self.addr = (self.host, self.port)
        self.buf = 1024

        self.cli = socket( AF_INET, SOCK_STREAM)
##	self.cli.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.cli.connect((self.addr))


    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.cli.close()

    def receive(self):
        return self.cli.recv(self.buf)

    def send(self,message):
        self.cli.send(bytes(message,"utf-8"))
        
        
        
