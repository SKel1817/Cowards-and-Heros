# Write your code here :-)
import random
from time import sleep

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

# enemy stats 
def enemy_stats():
    health = 25
    strength = d10()
    intellegence = d10()
    charasma = d10()
    dex = d10()
    conc = d10()
    enemy = {'Health': health, 'strength': strength, 'intellegence': intellegence, 'charasma': charasma, 'dex': dex, 'conc': conc}
    return enemy
