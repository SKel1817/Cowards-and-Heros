# imports here
import random
from time import sleep
import inventory
import char_funcs
from make_character import make_character
import json
import requests
print("Welcome to the game")
with open('save.txt', 'a') as f:
    f.write("\n")
    f.write("-------Start of Game-------")
    f.write("\n")
#run make_character.py
stats = make_character()

#get the chara_dets dictornary from the make_character function
#print(stats)
#okay actual story now
# do a file import like one is all character making the next is story? you know what yes lets do that


chara_det = stats
char_weap = inventory.char_weap
char_pot = inventory.char_pot
char_kit = inventory.char_kit
char_items = inventory.char_items
weapons = inventory.weapons
potions = inventory.potions
kits = inventory.kits
enemy = char_funcs.enemy_stats()


def playerTurn(roll):
    print("\n-----YOUR TURN-----")
    counter = 0
    if roll >= 10:
        print("you hit the enemy")
        damage = char_funcs.d6()
        enemy['Health'] = enemy['Health'] - damage
        print("The enemy has " + str(enemy['Health']) + " health remaining")
        #write this to a txt so it can be accessed as a save point for user
        with open('save.txt', 'a') as f:
            f.write(str(chara_det['name']) + " turn:")
            f.write("Successful hit, you hit the enemy " + str(enemy['Health']))
            f.write("\n")
    else:
        print("you missed")
        print("you, " + str(chara_det['name']) + " have " + str(chara_det['Health']) + " health")
        #write this to a txt so it can be accessed as a save point for user
        with open('save.txt', 'a') as f:
            f.write(str(chara_det['name']) + " turn:")
            f.write("failed hit, you failed to hit the enemy, it's health is " + str(enemy['Health']))
            f.write("\n")
def enemyTurn(roll):
    print("\n-----ENEMY TURN-----")
    counter = 0
    if roll >= 10:
        print("the enemy hit you")
        damage = char_funcs.d6()
        chara_det['Health'] = chara_det['Health'] - damage
        print("you, " + str(chara_det['name']) + " have " + str(chara_det['Health']) + " health remaining")
        #write this to a txt so it can be accessed as a save point for user
        with open('save.txt', 'a') as f:
            f.write("Enemy turn:")
            f.write("Successful hit, the enemy hit you, your remaing health is" + str(chara_det['Health']))
            f.write("\n")
    else:
        print("the enemy missed")
        print("you, " + str(chara_det['name']) + " have " + str(chara_det['Health']) + " health")
        counter += 1
        #write this to a txt so it can be accessed as a save point for user
        with open('save.txt', 'a') as f:
            f.write("Enemy turn:")
            f.write("failed hit, the enemy failed to hit you, it's health is" + str(enemy['Health']))
            f.write("\n")

print("you are now in combat (congrats)")
print("you have " + str(stats['Health']) + " health")
response = input("What do you want to do? [attack or flee]").lower()
if response == "attack":
    while enemy['Health'] >= 0 or chara_det['Health'] >= 0:
        roll = char_funcs.d20()
        playerTurn(roll)
        sleep(3)
        roll = char_funcs.d20()
        enemyTurn(roll)
        sleep(3)
        #check enemy and player health
        if enemy['Health'] <= 0:
            print("You have defeated the enemy")
            with open('save.txt', 'a') as f:
                f.write("----you have defeated the enemy----\n")
            break
        elif chara_det['Health'] <= 0:
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
else:
    print("Invalid response, get good")
    #update health in json file
with open('chara_det.json', 'w') as fp:
    json.dump(chara_det["Health"], fp, indent=4, separators=(',', ': '))



