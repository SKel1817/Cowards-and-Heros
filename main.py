# imports here
from time import sleep
import inventory
import char_funcs as fun
from make_character import make_character
from map import move
import json
#welcome
print("Welcome to the COWARDS and HEROES")

#load or make new
load = input("Do you want to load a save? (y/n) ")
if load == "y":
    #run load_save()
    stats = fun.load_save()
elif load == "n":
    #run make_character.py
    stats = make_character()
else:
    print("invaild input, get good")
    exit()
        
#save to the save file
with open('save.txt', 'a') as f:
    f.write("\n")
    f.write("-------Start of Game-------")
    f.write("\n")

#update chara_det.json with the stats from make_character/load


fun.update(stats)

#print(stats)
#okay actual story now
# do a file import like one is all character making the next is story? you know what yes lets do that

#variables
char_weap = inventory.char_weap
char_pot = inventory.char_pot
char_kit = inventory.char_kit
char_items = inventory.char_items
weapons = inventory.weapons
potions = inventory.potions
kits = inventory.kits
enemy = fun.enemy_stats()

print("-----------------------")
print("Welcome to COWARDS and HEROES\n here the rules are simple, adventure until you drop dead and yeah you might want to move a little to the left.")
print("You are " + str(stats['name']) + " and you have " + str(stats['Health']) + " health")
input("When you are ready to begin press enter")


print("you are now in combat (congrats)")
print("you have " + str(stats['Health']) + " health")
response = input("What do you want to do? [attack or flee]").lower()
if response == "attack":
    while enemy['Health'] >= 0 or stats['Health'] >= 0:
        roll = fun.d20()
        fun.playerTurn(roll, stats)
        sleep(3)
        roll = fun.d20()
        fun.enemyTurn(roll, stats)
        sleep(3)
        #check enemy and player health
        if enemy['Health'] <= 0:
            print("You have defeated the enemy")
            with open('save.txt', 'a') as f:
                f.write("----you have defeated the enemy----\n")
            break
        elif stats['Health'] <= 0:
            print("You have died")
            with open('save.txt', 'a') as f:
                f.write("----You have died----\n")
            break
        else:
            continue
elif response == "flee":
    print("you have fled")
    with open('save.txt', 'a') as f:
        f.write("----you have fled----\n")
        move() #this works now
else:
    print("Invalid response, get good")



