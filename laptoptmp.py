from clientConnect import NetworkConnect
from upgrade_debugger import UpgradeSTLink

with NetworkConnect() as network:
    while true:
        piCommand = network.receive()
        if "start" in piCommand:
            print("Upgraded")
            try:
                UpgradeSTLink()
                network.send("done")
            except:
                network.send("Couldn't upgrade")
        else:
            network.send("Couldn't upgrade")
