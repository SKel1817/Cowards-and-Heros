# Write your code here :-)
import random
from time import sleep
import json
import map 
import inventory
from rich import print
from rich.traceback import install
from make_character import make_character
install()
# dice rolls
def end():
    print("\n\nyou have completed the level congrats\n\n")
    #level += 1
    #return level

def d20():
    #random number from 1-20
    roll_d20 = random.randint(1, 20)
    #sleep(3)
    #print(roll_d20)
    return roll_d20
def d12():
    #random number from 1-12
    roll_d12 = random.randint(1, 12)
    #sleep(3)
    #print(roll_d12)
    return roll_d12
def d10():
    #random number from 1-10
    roll_d10 = random.randint(1, 10)
    #sleep(3)
    #print(roll_d10)
    return roll_d10
def d8():
    #random number from 1-8
    roll_d8 = random.randint(1, 8)
    #sleep(3)
    #print(roll_d8)
    return roll_d8
def d6():
    #random number from 1-6
    roll_d6 = random.randint(1, 6)
    #sleep(3)
    #print(roll_d6)
    return roll_d6
def d4():
    #random number from 1-4
    roll_d4 = random.randint(1, 4)
    #sleep(3)
    #print(roll_d4)
    return roll_d4

def load_save():
        with open('past_char.txt', 'r') as f:
            #list only the name part of each line'
            count = 0
            for line in f:
                count += 1
                #print(line)
                #convert the string to a dictornary
                stats = eval(line)
                #make count a string
                print(str(count) + ". " + stats['name'])
        if count == 0:
            print("There are no saves")
            successful = False
            return successful
        else:
            #ask the user which save they want
            while True:
                try:
                    save = input("Which save do you want to load? ")
                    print(save)
                    #open past_char.txt and get the last line
                    with open('past_char.txt', 'r') as f:
                        last_line = f.readlines()[int(save)-1]
                        #print(last_line)
                        #convert the string to a dictornary
                        stats = eval(last_line)
                        print(stats)
                        return stats
                except ValueError:
                    print("Invalid input, try again")
                    

def combat(stats):
    print("you are now in combat (congrats)")
    print("you have " + str(stats['Health']) + " health")
    response = input("What do you want to do? [attack or flee]").lower()
    while enemy['Health'] > 0 and stats['Health'] > 0:
        if response == "attack":
            roll = d20() 
            playerTurn(roll, stats)
            sleep(3)
            roll = d20()
            enemyTurn(roll, stats)
            sleep(3)
        elif response == "flee":
            with open('save.txt', 'a') as f:
                f.write("----you have fled----\n")
                map.flee() #this works now
            break
        else:
            print("Invalid response, off to combat you go")
            response = "attack" 
            continue
    if enemy['Health'] <= 0:
        print("You have defeated the enemy")
        with open('save.txt', 'a') as f:
            f.write("----you have defeated the enemy----\n")
    elif stats['Health'] <= 0:
        print("You have died")
        with open('save.txt', 'a') as f:
            f.write("----You have died----\n")


# enemy stats 
def enemy_stats(count = 0):
    strength = d4()
    intellegence = d4()
    charasma = d4()
    dex = d4()
    conc = d4()
    health = 15 + conc + (count * 2)
    enemy = {'Health': health, 'strength': strength, 'intellegence': intellegence, 'charasma': charasma, 'dex': dex, 'conc': conc}
    return enemy

enemy = enemy_stats()

# update player stats
def update(stats):
    #update chara_det.json with the stats from make_character/load
    with open('chara_det.json', 'w') as fp:
        #append to json
        json.dump(stats, fp, indent=4, separators=(',', ': '))

def playerTurn(roll, stats):
    print("\n-----YOUR TURN-----")
    choice = input("Would you like to attack or use a potion? [attack or potion]").lower()
    if choice == "attack":
        if roll >= 10:
            print("you can hit the enemy")
            print(" what weapon do you want to use?")
            #list character inventory
            inventory.list_weap()
            weapon = input("enter name of weapon here: ").lower()
            #get the weapon stats
            dict = inventory.weapons
            try:
            #get the weapon stats
                damage = dict[weapon] + stats['Strength']
            except KeyError:
                print("invalid weapon, you use your fists")
                damage = dict["fists"] + stats['Strength']
            print("you hit the enemy for " + str(damage) + " damage")
            enemy['Health'] = enemy['Health'] - damage
            print("The enemy has " + str(enemy['Health']) + " health remaining")
            #write this to a txt so it can be accessed as a save point for user
            with open('save.txt', 'a') as f:
                f.write(str(stats['name']) + " turn:")
                f.write("Successful hit, you hit the enemy " + str(enemy['Health']))
                f.write("\n")
            update(stats)
        else:
            print("you missed")
            print("you, " + str(stats['name']) + " have " + str(stats['Health']) + " health")
            #write this to a txt so it can be accessed as a save point for user
            with open('save.txt', 'a') as f:
                f.write(str(stats['name']) + " turn:")
                f.write("failed hit, you failed to hit the enemy, it's health is " + str(enemy['Health']))
                f.write("\n")
            update(stats)
    elif choice == "potion":
        inventory.list_potion()
        potion = input("which potion do you want to use?").lower()
        potion_dict = inventory.potions
        try :
            print("you have chosen to use a " + potion)
            stats['Health'] = stats['Health'] + potion_dict[potion]
            print("you, " + str(stats['name']) + " have " + str(stats['Health']) + " health")
        except KeyError:
            print("you don't have that potion")
    else:
        print("invalid response, you lose your turn. do better")


def enemyTurn(roll, stats):
    print("\n-----ENEMY TURN-----")
    counter = 0
    if roll >= 10:
        print("the enemy hit you")
        damage = d6() + enemy['strength']
        stats['Health'] = stats['Health'] - damage
        print("you, " + str(stats['name']) + " have " + str(stats['Health']) + " health remaining")
        #write this to a txt so it can be accessed as a save point for user
        with open('save.txt', 'a') as f:
            f.write("Enemy turn:")
            f.write("Successful hit, the enemy hit you, your remaing health is " + str(stats['Health']))
            f.write("\n")
        update(stats)
    else:
        print("the enemy missed")
        print("you, " + str(stats['name']) + " have " + str(stats['Health']) + " health")
        counter += 1
        #write this to a txt so it can be accessed as a save point for user
        with open('save.txt', 'a') as f:
            f.write("Enemy turn:")
            f.write("failed hit, the enemy failed to hit you, it's health is " + str(enemy['Health']))
            f.write("\n")
        update(stats)