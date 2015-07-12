# Save as server.py 
# Message Receiver
import os
from socket import *
host = ""
port = 13000
buf = 1024
addr = (host, port)
serv = socket(AF_INET, SOCK_STREAM)
serv.bind(addr)
serv.listen(5)
print("Waiting to receive messages...")

conn,addr= serv.accept()
print("...Connected!")
conn.send(bytes('Testing', 'utf-8'))

conn.close
