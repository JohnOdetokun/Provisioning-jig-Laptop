#!/usr/bin/env python
from serverConnect import NetworkConnect
from upgrade_debugger import UpgradeSTLink

import logging
logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
while True:
    with NetworkConnect(logger.getChild('network')) as network:
        piCommand = network.receive()
        if "start" in piCommand:
            print("beginning upgrade")
            try:
                with UpgradeSTLink(logger.getChild('upgrade')) as stStatus:
                    network.send("done")
            except:
                network.send("Couldn't upgrade")
        elif "b\'\'" == piCommand:
            logging.info("Waiting for instruction")
        else:
            network.send("Couldn't upgrade")
            logging.critical('received wrong message')
