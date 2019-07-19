#!/usr/bin/python

import os
import platform
import subprocess

had_error = False

def get_current_dir():
    save_location = str(subprocess.check_output(["pwd"]))
    # save directory to txt file in the simple-scan folder
    # delete this folder later in uninstaller.py
    folder = save_location.split("/")
    folder.remove("b'")  # this is needed to remove the first element in the list
    folder[len(folder) - 1] = folder[len(folder) - 1].split("\\")[0]  # removes the \n in the last element
    result = ""
    for i in folder:
        result += "/" + i
return result


def save_folder_location(location):
    try:
        file = open(location + "/location.txt", "w")
        file.write(location)
    except:
        print("[-] Error writing to file")
        had_error = True
        raise
    finally:
file.close()

try:
   subprocess.call("sudo -H pip3 install --upgrade pip", shell=True)
   subprocess.call("sudo pip3 install platform", shell=True)
   subprocess.call("pip3 install smtplib", shell=True)
   subprocess.call("sudo pip3 install imaplib", shell=True)


   p = platform.system()
   if "Linux" == p:
      subprocess.call("sudo apt-get install googler", shell=True)
      subprocess.call("sudo mv googleot-file /usr/share", shell=True)
      print("[+] Moved googleot-file (the python programs) to '/usr/share'!", shell=True)
      subprocess.call("sudo mv googleot /usr/bin", shell=True)
      print("[+] Moved googleot (the bash program) to '/usr/bin'!")
      subprocess.call("sudo mv googleot.desktop /usr/share/applications", shell=True)
      print("[+] Moved googleot.desktop (the application program) to '/usr/share/applications'!")
      print("[-] Please type 'googleot' in your terminal to run the program or open from the application!")
   else:
      subprocess.call("brew install googler", shell=True)
      print("[-] Please do 'sudo python3 googleot-files/runme.py' to run the program!")
   save_folder_location(get_current_dir())
   time.sleep(3)
except:
    had_error = True
    raise
finally:
    if had_error:
        print("[-] Setup Failed, an error stopped the setup process ")
    else:
        print("[+] Setup is complete, no errors!")
