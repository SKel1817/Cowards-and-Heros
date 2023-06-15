# imports here
from time import sleep
import inventory
import random
import char_funcs as fun
from make_character import make_character
import map as m
from rich import print
from rich.traceback import install
install()
#welcome
print("Welcome to the COWARDS and HEROES")

#make a function or something idk 
while True:
    #load or make newn
    load = input("Do you want to load a save? (y/n) ")
    if load == "y":
        #run load_save()
        stats = fun.load_save()
        if stats == False:
            stats = make_character()
        else:
            break
    elif load == "n":
        #run make_character.py
        stats = make_character()
        break
    else:
        print("invaild input, get good")
        continue
    #save to the save file
with open('save.txt', 'a') as f:
    f.write("\n")
    f.write("-------Start of Game-------")
    f.write("\n")

#update chara_det.json with the stats from make_character/load
fun.update(stats)

print("-----------------------")
print("Welcome to COWARDS and HEROES\n here the rules are simple, adventure until you drop dead and yeah you might want to move a little to the left.")
print("You are " + str(stats['name']) + " and you have " + str(stats['Health']) + " health")
start = input("When you are ready to begin press enter")
running = True
while running == True:
    m.move(stats)
    running = False