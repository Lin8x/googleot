#!/usr/bin/python

r = '\033[0m'     #reset
bold = '\033[01m'
d = '\033[02m'     #disable
ul = '\033[04m' #underline
reverse = '\033[07m'
st = '\033[09m' #strikethrough
invis = '\033[08m'#invisible
white = '\033[0m'
cwhite = '\33[37m'
black ='\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'

re = red
w = white
b = lblue
g = green
y = yellow

import os

def clear():
  i = 0
  while i <= 5:
    os.system("clear")
    i = i + 1

def quit():
  clear()  
  exit()

def logo():
  print(white + "")
  print(red + "@@@" + white + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + red + "@@@")
  print(red + "@@/(" + white + "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%" + red + "(/@@")
  print(red + "@((((((" + white + "%%%%%%%%%%%%%%%%%%%%%%%%%" + red + "((((((@")
  print(red + "@(((((((((" + white + "%%%%%%%%%%%%%%%%%%%" + red + "((((((((#@")
  print(red + "@(((#((((((((" + white + "%%%%%%%%%%%%%" + red + "((((((((####@")
  print(red + "@((((" + white + "$,," + red + "((((((((" + white + "%%%%%%%" + red + "((((((((" + white + ",,$" + red + "####@")
  print(red + "@((((" + white + "$$$,,," + red + "((((((((" + white + "%" + red + "((((((((" + white + ",,$$$$" + red + "####@")
  print(red + "@((((" + white + "$$$$$,,,," + red + "(((((((((((" + white + ",,$$$$$$%" + red + "####@")
  print(red + "@((((" + white + "$$$$$$$$,,," + red + "*(((((" + white + ",,$$$$$$$%%%" + red + "####@")
  print(red + "@((((" + white + "$$$$$$$$$$$$$" + red + ",*," + white + "$$$$$$$$%%%%%" + red + "####@")
  print(red + "@((((" + white + "$$$$$$$$$$$$$$$$$$$$$$%%%%%%%" + red + "####@")
  print(red + "@((((" + white + "$$$$$$$$$%%%%$$$$$$$%%%%%%%%%" + red + "####@")
  print(red + "@((((" + white + "$$$$$$%%%%%%%%%$$$%%%%%%%%%%%" + red + "####@")
  print(red + "@((((" + white + "$$$%%%%%%%%%%%%%%%%%%%%%%%%%%" + red + "####@")
  print(red + "@@#((" + white + "$%%%%%%%%%%%%%%%%%%%%%%%%%%%%" + red + "##%@@")
  print(red + "@@@@@" + white + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + red + "@@@@@")
  print(red + "@@@@@" + white + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + red + "@@@@@")

def name():
  print("")
  print(red + """MMMMMMMMMMM""")
  print(red + "MM" + white + "######6" + red + "MM" + yellow + "                     {} dP")
  print(red + "M" + white + "'#'" + red + "   " + white + "'#6" + red + "M" + white + """                        88""")
  print(red + "M" + white + "#  " + red + "      " + red + "M" + yellow + " 88d8b.d8b. .d8888b. dP 88")
  print(red + "M" + white + "##" + red + "  " + white + "######" + red + "" + white + " 88'`88'`88 88'  `88 88 88")
  print(red + "M" + white + "##7" + red + "   " + white + "7##" + red + "M" + yellow + " 88  88  88 88.  .88 88 88")
  print(red + "MM" + white + "9#####6" + red + "MM" + white + " dP  dP  dP `88888P8 dP dP")
  print(red + "MMMMMMMMMMM" + r + "") 

def chromelogo():
  print(r + "MMMMMMMMMMMMMMMN" + red + "mdhyssoooooossyhdm" + white + "NMMMMMMMMMMMMMMM")
  print(white + "MMMMMMMMMMMN" + red + "dysooooooooooooooooooooshd" + white + "MMMMMMMMMMMM")
  print("MMMMMMMMM" + red + "dyooooooooooooooooooooooooooooym" + white + "MMMMMMMMM")
  print(white + "MMMMMMM" + red + "dsoooooooooooooooooooooooooooooooosd" + white + "MMMMMMM")
  print(r + "MMMMM" + red + "msoooooooooooooooooooooooooooooooooooosm" + white + "MMMMM")
  print(r + "MMMM" + red + "hsssoooooooooooooooooooooooooooooooooooooy" + white + "MMMM")
  print(w + "MMN" + re + "ysssssoooooooooooooo++++ooooooooooooooooooos" + w + "NMM")
  print(w + "MN" + g + "ysssss" + re + "sssooooooo+:" + w + "-````````." + y + "-:////:::::::::::/" + w + "NM")
  print(w + "M" + g + "ysssssss" + re + "ssssooo+" + w + ".``" + b + "-/++oo++/-" + w + "``." + y + "-:::::::-------" + w + "+M")
  print("m" + g + "ssssssssss" + re + "ssso" + w + "-``" + b + "/+ooooooooooo/" + w + "``." + y + "--------------" + w + "d")
  print(w + "h" + g + "sssssssssss" + re + "ss" + w + "-`." + b + "+oooooooooooooo+" + w + ".`." + y + "-------------" + w + "+")
  print(g + "sssssssssssss" + re + "o" + w + "``" + b + "+oooooooooooooooo+" + w + "``" + y + "-------------" + w + ":")
  print(g + "sssssssssssss+" + w + "``" + b + "oooooooooooooooooo" + w + "``." + y + "-------------" + w)
  print(g + "ysssssssssssso" + w + "``" + b + "+oooooooooooooooo+" + w + "``" + y + "-------------" + w + ":")
  print(w + "h" + g + "sssssssssssss:" + w + "`." + b + "+oooooooooooooo+" + w + ".`." + y + "-------------" + w + "+")
  print("m" + g + "ssssssssssssss:" + w + "``" + b + "/oooooooooooo/" + w + "``." + y + "--------------" + w + "d")
  print("M" + g + "hssssssssssssss+" + w + ".``" + b + "-/+oooo+/-" + w + "``" + y + "-:--------------" + w + "+M")
  print(w + "My" + g + "ssssssssssssssso" + w + "/-````````-/s/" + y + "---------------" + w + "/NM")
  print(w + "MMN" + g + "ysssssssssssssssssssoooosyyy" + y + "/--------------" + w + "/NMM")
  print(w + "MMMM" + g + "hssssssssssssssssssssyyyyy" + y + ":--------------" + w +"oNMMM")
  print(w + "MMMMM" + g + "mysssssssssssssssssyyyys" + y + ":-------------:" + w + "hMMMMM")
  print("MMMMMMM" + g + "mysssssssssssssyyyyys" + y + "-------------:" + w + "yMMMMMMM")
  print("MMMMMMMMM" + g + "mhysssssyyyyyyyyyo" + y + "------------" + w + "odMMMMMMMMM")
  print("MMMMMMMMMMMM" + g + "mdyyyyyyyyyyy" + y + "+---------/" + w + "shNMMMMMMMMMMM")
  print("MMMMMMMMMMMMMMMMN" + g + "mdhhyyy" + y + "/--::/+" + w + "sydNMMMMMMMMMMMMMMM")

def googlelogo():
  print(re + """
                     `.--::--.`                    
                .:+oooooooooooo+:.                
             `:oooooooooooooooooooo.              
            :ooooooooo+////+ooooo/`""")               
  print(y + "          `+oooo" + re + "ooo:.        .:/`")                 
  print(y + """          -/+oooo:                                
         .::::/o.""")                                 
  print(y + "         ::::::-" + b + "         ooooooooooooooo`")         
  print(y + "         ::::::." + b + "         ooooooooooooooo.")         
  print(y + "         ::::::-         " + b + "ooooooooooooooo.")         
  print(y + "         .::::/o-" + b + "        ````````:oooooo")          
  print(y + "          -/+ssss:" + b + "              -oooooo-")          
  print(y + "          `+ssss" + g + "sso:." + g + "        `-+ooo" + b + "ooo/")           
  print(g + "            :ossssssso+////+ossssooo" + b + "o-")            
  print(g + "             `:osssssssssssssssssso:`")    
  print(g + "                .:+sssssssssssso/-")     
  print(g + "                    `.-::::--.")

def testchrome():
  print(r + "                " + red + " dhyssoooooossyhd " + white + "                ")
  print(white + "            " + red + "dysooooooooooooooooooooshd" + white + "            ")
  print("         " + red + "dyooooooooooooooooooooooooooooy " + white + "         ")
  print(white + "       " + red + "dsoooooooooooooooooooooooooooooooosd" + white + "       ")
  print(r + "     " + red + " soooooooooooooooooooooooooooooooooooos " + white + "     ")
  print(r + "    " + red + "hsssoooooooooooooooooooooooooooooooooooooy" + white + "    ") 
  print(w + "   " + re + "ysssssoooooooooooooo++++ooooooooooooooooooos" + w + "   ")
  print(w + "  " + g + "ysssss" + re + "sssooooooo+:" + w + "-````````." + y + "-:////:::::::::::/" + w + "  ")
  print(w + " " + g + "ysssssss" + re + "ssssooo+" + w + ".``" + b + "-/++oo++/-" + w + "``." + y + "-:::::::-------" + w + "  ")
  print(" " + g + "ssssssssss" + re + "ssso" + w + "-``" + b + "/+ooooooooooo/" + w + "``." + y + "--------------" + w + " ")
  print(w + " " + g + "sssssssssss" + re + "ss" + w + "-`." + b + "+oooooooooooooo+" + w + ".`." + y + "-------------" + w + " ")
  print(g + "sssssssssssss" + re + "o" + w + "``" + b + "+oooooooooooooooo+" + w + "``" + y + "-------------" + w + " ")
  print(g + "sssssssssssss+" + w + "``" + b + "oooooooooooooooooo" + w + "``." + y + "-------------" + w)
  print(g + "ysssssssssssso" + w + "``" + b + "+oooooooooooooooo+" + w + "``" + y + "-------------" + w + " ")
  print(w + " " + g + "sssssssssssss:" + w + "`." + b + "+oooooooooooooo+" + w + ".`." + y + "-------------" + w + " ")
  print(" " + g + "ssssssssssssss:" + w + "``" + b + "/oooooooooooo/" + w + "``." + y + "--------------" + w + " ")
  print(" " + g + "hssssssssssssss+" + w + ".``" + b + "-/+oooo+/-" + w + "``" + y + "-:--------------" + w + "  ")
  print(w + "  " + g + "ssssssssssssssso/" + w + "-```````````-" + y + "/s/------------" + w + "   ")
  print(w + "   " + g + "ysssssssssssssssssssoooosyyy" + y + "/--------------" + w + "    ")
  print(w + "    " + g + "hssssssssssssssssssssyyyyy" + y + ":--------------" + w +"    ")
  print(w + "     " + g + " ysssssssssssssssssyyyys" + y + ":-------------:" + w + "      ")
  print("       " + g + " ysssssssssssssyyyyys" + y + "-------------:" + w + "        ")
  print("         " + g + " hysssssyyyyyyyyyo" + y + "------------" + w + "           ")
  print("            " + g + " dyyyyyyyyyyy" + y + "+---------/" + w + "              ")
  print("                 " + g + " dhhyyy" + y + "/--::/+" + w + "                   ")