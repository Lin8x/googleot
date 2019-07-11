#!/usr/bin/python

import os
import platform
red = '\033[31m'
green = '\033[92m'
rr = '\033[0m'  # reset
bold = '\033[01m'
had_error = False

p = platform.system()
try:
   if "Linux" == p:
      os.system("sudo rm -rf /usr/share/googleot-file")
      print("[+] removed /usr/share/googleot-file")
      os.system("sudo rm /usr/bin/googleot")
      print("[+] removed /usr/bin/googleot")
      os.system("sudo rm /usr/share/applications/googleot.desktop")
      print("[+] removed /usr/share/applications/googleot.desktop")
      print("[-] Uninstalled Googleot. Come back again! :)")
   else:
      print("[-] Just delete the file. :/")
   
   # removes the folder where simple scan installation folder is located
    try:
        file = open("location.txt", "r")
        location = file.readlines()[0]
        os.system("sudo rm -rf {}".format(location))
    except:
        had_error=True
        print("[!] Error-Unable to find location.txt")

except:
    had_error = True
    raise
finally:
    if had_error:
        print(red+bold+"[!] Unable to uninstall googleot due to an error"+rr)
    else:
print(rr+"[" + green + " OK " + rr + "] Uninstall is complete, no errors !"+rr)


