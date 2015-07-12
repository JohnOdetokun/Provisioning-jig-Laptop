
from serverConnect import NetworkConnect

with NetworkConnect() as network:
    network.connection()
    network.send("this is cool")
        
