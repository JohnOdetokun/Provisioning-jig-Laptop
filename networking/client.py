# Save as client.py 
# Message Sender
import os
from socket import *
host = "localhost" # set to IP address of target computer
port = 13000
addr = (host, port)
buf = 1024

cli = socket( AF_INET, SOCK_STREAM)
cli.connect((addr))

data = cli.recv(buf)
print(data)

cli.close()
