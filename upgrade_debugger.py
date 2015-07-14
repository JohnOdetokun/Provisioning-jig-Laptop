import os
import sys
import pexpect
import time
import logging

class UpgradeFailed(Exception):
    pass

class UpgradeSTLink:
    def __init__(self):
        logging.basicConfig()
        self.upgrade = pexpect.spawn("java -jar ./STLinkUpgrade.jar -jtag -force_prog", timeout=8)
        time.sleep(2)
        upgrade_result = self.upgrade.expect([\
            "[\s\S]*Upgrade is successful.",\
            "Detected firmware is up to date[\s\S]*",\
            "ST-Link is not in the DFU mode.",\
            "No ST-Link detected"])
        if upgrade_result == 0:
            logging.info("Firmware upgraded")
        elif upgrade_result == 1:
            logging.info("upgraded or already the latest version")
        else:
            logging.critical("something went wrong")
            raise UpgradeFailed()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        print("End of update")
        self.upgrade.terminate(force = False)
        
