# Write your code here :-)
import random
from time import sleep
import json

# dice rolls
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
            count = 1
            for line in f:
                #print(line)
                #convert the string to a dictornary
                stats = eval(line)
                #make count a string
                print(str(count) + ". " + stats['name'])
                count += 1
        #ask the user which save they want
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
        
# enemy stats 
def enemy_stats():
    health = 15
    strength = d10()
    intellegence = d10()
    charasma = d10()
    dex = d10()
    conc = d10()
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
    counter = 0
    if roll >= 10:
        print("you hit the enemy")
        damage = d6()
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

def enemyTurn(roll, stats):
    print("\n-----ENEMY TURN-----")
    counter = 0
    if roll >= 10:
        print("the enemy hit you")
        damage = d6()
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