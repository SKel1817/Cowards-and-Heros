#lists that contain all possible (maybe make dictionary for damage)
# or make each weapon a dictornary and have dictionary in list
import char_funcs as fun
import random
from rich import print
from rich.traceback import install
install()
weapons = {'sword': fun.d10(), 'axe': fun.d10(), 'bow': fun.d8(), 'dagger': fun.d6(), 'staff': fun.d6, 'fists': fun.d4()}
potions = {'health': fun.d8(), 'mana': fun.d8(), 'stamina': fun.d8()}
items = []
#random = random.randint(0,5)
#ran = random.randint(0,2)
chest = ['sword', 'health']

#what the character has, can be added to by using class inventory
char_weap = ["fists"]
char_pot = []
char_kit = []
char_items = []
inventory = [char_weap, char_pot, char_kit, char_items]
def add_item():
    print("you have added an item")
def lose_item():
    print("You lost an item")
def list_inv():
    print("You have....")
    #print inventory
    for item in inventory:
        print(item)
def list_weap():
    print("You have....")
    #print inventory
    for item in char_weap:
        print(item)
def list_potion():
    print("You have....")
    for item in char_pot:
        print(item)
def loot():
    print("You have found a chest")
    print("You have found a  " + chest[0] + " and a " + chest[1] + " potion")
    print("Do you want to add the items to your inventory?")
    response = input("Yes or No?").lower()
    if response == "yes":
        print("You have added the items to your inventory and left the chest")
        char_weap.append(chest[0])
        char_pot.append(chest[1])
        print(char_weap)
        print(char_pot)
    else:
        print("You have left the items")