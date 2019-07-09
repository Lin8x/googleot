#!/usr/bin/python

import os
import platform

os.system("sudo pip3 install platform")
os.system("sudo pip3 install smtplib")
os.system("sudo pip3 install stdiomask")
os.system("sudo pip3 install imaplib")
os.system("sudo pip3 install getpass")

p = platform.system()
if "Linux" == p:
   os.system("sudo apt-get install googler")
   os.system("sudo mv googleot-file /usr/share")
   print("[+] Moved googleot-file (the python programs) to '/usr/share'!")
   os.system("sudo mv googleot /usr/bin")
   print("[+] Moved googleot (the bash program) to '/usr/bin'!")
   os.system("sudo mv googleot.desktop /usr/share/applications")
   print("[+] Moved googleot.desktop (the application program) to '/usr/share/applications'!")
   print("[-] Please type 'googleot' in your terminal to run the program or open from the application!")
else:
   os.system("brew install googler")
   print("[-] Please do 'sudo python3 googleot-files/runme.py' to run the program!")

   
