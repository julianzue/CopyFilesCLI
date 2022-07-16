import os
from traceback import print_tb
from colorama import Fore, init
import shutil
from pyfiglet import Figlet
from datetime import datetime
import time as ti

init()

c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
re = Fore.RESET
w =  Fore.LIGHTWHITE_EX
b = Fore.LIGHTBLUE_EX

f = Figlet()
print(y + f.renderText("Copy Files") + re)

co = 0
files = []

print(y + "[*] " + re +"SELECT FOLDERS")
print("")

for file in os.scandir(os.getcwd()):
    print(y + "{:03d}".format(co) + " " + re + file.name)
    files.append(file.name)
    co += 1

print("")

copy_from_id = int(input(y + "[+] From: " + re))
copy_to_id   = int(input(y + "[+] To:   " + re))

copy_from = files[copy_from_id]
copy_to = files[copy_to_id]

length = len(os.listdir(copy_from))

print("")
yn = input(y + "[+] " + re + "Copying " + y + str(length) + re + " files? [Y|n]: ")

if yn == "N" or yn == "n":
    print(r + "[!]" + re + " Job canceled!")
    print(r + "[!]" + re + " Exit program!")
    quit()

starttime = datetime.now()

print("")



count = 0

for file in os.scandir(copy_from):
    count += 1

    shutil.copyfile(copy_from + "\\" + file.name, copy_to + "\\" + file.name)

    percent = count / length * 100

    size = "{:5.2f}".format(float(os.stat(copy_from + "\\" + file.name).st_size) / 1000000) + " MB"

    print(c + "[*] " +re + "[" + g + ti.strftime("%H:%M:%S") + re + "] [" + c + "{:3d}".format(int(percent)) + "%" + re + "] [" + c + "{:03d}".format(count) + "/" + "{:03d}".format(length) + re + "] " + y + copy_from + re + " => " + y + copy_to + re + " | [" + c +  size + re + "] " + w + file.name + re)

endtime = datetime.now()

difference = endtime - starttime
time = difference.seconds


print("")
print(g + "[*]" + c + " " + str(length) + re  +  " files successfully copied in " + c + str(time) + re + " seconds!")
print(r + "[!]" + re + " Exit program!")