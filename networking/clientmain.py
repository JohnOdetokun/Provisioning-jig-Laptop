from clientConnect import NetworkConnect

with NetworkConnect() as network:
    print(network.receivemessage())
