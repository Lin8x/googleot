#!/usr/bin/python

# For anyone willing to work on this code, each section of this tool is in its own seperate program file.
# For instance, the section where you can google stuff, its using the google.py file.
# For emailing with the gmail section, it uses gmail.py

import gmails
import google
import core

w = core.white
r = core.red
y = core.yellow
lc = core.lcyan

#CLEARS THE SCREEN
def clear():
  core.clear()

def startup():
  try:
    clear()
    core.googlelogo()
    print(core.r + "\n" + core.red + core.bold + "[+] " + core.r + "By lin8x " + core.red + core.bold + "[-] " + core.r + core.lcyan + core.ul + "www.github.com/lin8x" + core.r + core.red + core.bold + " [+]" + core.r + "\n")
    print(core.ul + core.bold + "Welcome to Google-Ot!\n")
    print(core.r + "(" + lc + "1" + w + ") " + core.lblue + "G" + core.red + "o" + core.yellow + "o" + core.lblue + "g" + core.green + "l" + core.red + "e" + core.r + " Search")
    print(core.r + "(" + lc + "2" + w + ") " + r + "G" + w + "m" + y + "a" + w + "i" + y + "l")
    print(core.r + "(" + lc + "q" + w + ") " + w + "Exit\n")
    try:
        while True:
          answer = input(core.lblue + "G" + core.red + "o" + core.yellow + "o" + core.lblue + "g" + core.green + "l" + core.red + "e" + core.yellow + " > " + core.r + "")
          if answer == "1":
            print("")
            google.startup()
          elif answer == "2":
            print("")
            clear()
            gmails.startup()
          elif answer == "q":
            core.quit()
          else:
            print("\nCommand '" + answer + "' not found. Please pick a choice above.\n")
    except:
        raise
  except KeyboardInterrupt:
    clear()
    exit()

