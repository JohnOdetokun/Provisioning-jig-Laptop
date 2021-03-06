import logging 
from socket import *
class NetworkConnectFailed(Exception):
    pass


class NetworkConnect:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.host = "10.0.0.1" # set to IP address of target computer
        self.port = 13000
        self.addr = (self.host, self.port)
        self.buf = 1024
        self.serv = socket( AF_INET, SOCK_STREAM)
        self.serv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serv.bind((self.addr))
        self.serv.listen(2)
        self.conn,self.addr = self.serv.accept()
        self.logger.info("connected")


    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.serv.close()
        self.logger.debug('network closed')

    def receive(self):
        return str(self.conn.recv(self.buf))

    def send(self,message):
        self.conn.send(bytes(message,"utf-8"))
        
        
    def exit(self):
        self.conn.close()
        self.serv.close()
