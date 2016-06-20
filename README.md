# Provisioning-jig-Laptop
laptop talking to pi in order to update the stlink

In this repository I have the laptopmp.py program which is the main program that is run from the laptop.
This program imports from clientConnect and upgrade_debugger

seems to be a problem committing native folder(linux drivers do not get commit..)

Program is run after debugger program is run on raspberry pi

ethernet cable must be connected.

Communicates with Raspberry pi and begins firmware upgrade of debugger chip

Zip for st-linkv2_upgrade is included. Extract zip and copy contents of AllPlatforms to Provisioning-jig-Laptop directory

you can run using ./main.py


