#!/usr/bin/python

import os
import platform

p = platform.system()
if "Linux" == p:
   os.system("sudo rm -rf /usr/share/googleot-file")
   os.system("sudo rm -rf /usr/bin/googleot")
   os.system("sudo rm -rf /usr/share/applications/googleot.desktop")
   print("Uninstalled Googleot. Come back again! :)")
else:
   print("Just delete the file. :/")

   
