#!/usr/bin/python

import core
import os
import main

global lines
lines = 10

#CLEARS THE SCREEN
def clear():
  i = 0
  while i <= 5:
    os.system("clear")
    i = i + 1

def startup():
  try:
      clear()
      core.testchrome()
      print("")
      print(core.red + core.bold + "[+] " + core.r + "Relies on Googler " + core.red + core.bold + "[-] " + core.r + core.lcyan + core.ul + "https://github.com/jarun/googler" + core.r + core.red + core.bold + " [+]" + core.r + "\n")
      print(core.ul + "Please type 'help' for help!" + core.r + "\n")
      while True:
         answer = input(core.lblue + "S" + core.red + "e" + core.yellow + "a" + core.lblue + "r" + core.green + "c" + core.red + "h" + core.yellow + " > " + core.r + "")
         answer = answer.split(" ")
         if answer[0] == "exit":
            main.startup()
         elif answer[0] == "lines":
            try:
               lines = answer[1]
               print("\n# of lines set to " + answer[1] + "\n")
            except:
               print("\nError: Could not set lines. Please do 'lines <#>'\n")
         elif answer[0] == "help":
            print("\n-----------\n")
            print(core.ul + "The Help/Command Menu" + core.r)
            print("\nhelp - Opens the help menu")
            print("exit - Exits back to the main menu")
            print("lines <number> - Set the amount of search results you want per search")
            print("search <word> - Search for any specific thing. \n" + "(This can be anything that is not a command already said above.)")
            print("\n----------- \n")
         elif answer[0] == "search":
            try:
                  search = answer[1]
                  os.system("googler -n " +  lines + " google.com " + search + "\n")
                  input("Please press {ENTER} to continue... " + core.invis)
                  startup()
            except:
                  print("\nError: Could not search. \nMake sure you have Googler installed and type 'search <word>'!\n")
         else:
            print("\n " + answer + " is not a command. Please type 'help' for help. \n")
  except KeyboardInterrupt:
      main.startup()
