import os
import sys
import pexpect
import time
import logging

class UpgradeFailed(Exception):
    pass

class UpgradeSTLink:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.upgrade = pexpect.spawn("java -jar ./STLinkUpgrade.jar -jtag -force_prog", timeout=8)
        upgrade_result = self.upgrade.expect([\
            "[\s\S]*Upgrade is successful.",\
            "Detected firmware is up to date[\s\S]*",\
            "ST-Link is not in the DFU mode.",\
            "No ST-Link detected"])
        if upgrade_result == 0:
            self.logger.info("Firmware upgraded")
        else:
            self.logger.critical("something went wrong")
            raise UpgradeFailed()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.logger.info("Firmware update class end")
        self.upgrade.terminate()
        
