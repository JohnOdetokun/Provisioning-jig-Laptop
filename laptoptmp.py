#!/usr/bin/env python
from clientConnect import NetworkConnect
from upgrade_debugger import UpgradeSTLink

import logging

with NetworkConnect() as network:
    while True:
        piCommand = network.receive()
        if "start" in piCommand:
            print("beginning upgrade")
            try:
                with UpgradeSTLink() as stStatus:
                    if stStatus.status == 1:
                        print("completing upgrade")
                        network.send("done")
                        
                    else:
                        network.send("Couldn't upgrade")
            except:
                network.send("Couldn't upgrade")
        elif "b\'\'" == piCommand:
            logging.info("Waiting for instruction")

        else:
            network.send("Couldn't upgrade")
