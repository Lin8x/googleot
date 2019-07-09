#!/usr/bin/python

import os

os.system("sudo mv googleot-file /usr/share")
print("Moved googleot-file (the python programs) to '/usr/share'!")
os.system("sudo mv googleot /usr/bin")
print("Moved googleot (the bash program) to '/usr/bin'!")
os.system("sudo mv googleot.desktop /usr/share/applications")
print("Moved googleot.desktop (the application program) to '/usr/share/applications'!")
print("Please type 'googleot' in your terminal to run the program or open from the application!")
