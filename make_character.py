# imports here
from time import sleep
import json

#list of the varibles
strength, intel, charsama, dex, conc = 0,0,0,0,0
var = [strength, intel, charsama, dex, conc]
# making the charactor
# so this is lists, its kinda a jumble but just cause I need it to be
def make_character():
    print("MAKE YOUR CHARACTOR\n")
    #name of charactor
    name = input("What is your Charater's Name? ").title()

    #race options and base stats
    races = ["Orc", "Elf", "Wood Elf", "Dark Elf", "Dragonborn", "Dwarf", "Human", "Goblin"]
    orc = {"Strength": 4, "Intellgence": 1, "Charasma": 2, "Dexetrity": 3, "Constitution": 4}
    elf = {"Strength": 2, "Intellgence": 3, "Charasma": 4, "Dexetrity": 4, "Constitution": 1}
    wood_elf = {"Strength": 2, "Intellgence": 3, "Charasma": 4, "Dexetrity": 4, "Constitution": 1}
    dark_elf = {"Strength": 3, "Intellgence": 4, "Charasma": 2, "Dexetrity": 4, "Constitution": 1}
    dragonborn = {"Strength": 4, "Intellgence": 2, "Charasma": 3, "Dexetrity": 4, "Constitution": 3}
    dwarf = {"Strength": 3, "Intellgence": 2, "Charasma": 1, "Dexetrity": 2, "Constitution": 4}
    human = {"Strength": 3, "Intellgence": 3, "Charasma": 3, "Dexetrity": 3, "Constitution": 3}
    goblin = {"Strength": 1, "Intellgence": 3, "Charasma": 2, "Dexetrity": 4, "Constitution": 2}
    #make a list of the dicts
    race_dic = [orc, elf, wood_elf, dark_elf, dragonborn, dwarf, human, goblin]
    
    # pick the race
    count = 1
    #for loop that loops through and lists the race with a number
    for i in races:
        print(str(count) + ". " + i)
        count += 1

    while True:
        #insert if statment or something to insure a actual race is being entered
        race = input("Pick a race from the list above by entering the number assocatcte to it: ")

        #make sure they entered the an option from the races list
        try:
            race = int(race) - 1
            start = race_dic[race]
            #assign the starting stats to the var list
            for i in range(len(var)):
                var[i] = start[list(start)[i]]
            race = races[race]
            break
        except KeyError:
            print("invaild input")
            continue

    #starting health value
    health = 15 + var[4]
    # making the stats for charactor
    print("Welcome " + name + " so your a " + race + " well there is a few things left to do")
    print("you have 10 points to use so enter them accordingly you can use it on strength, intellgence. charasma, dexetrity, and Constitution")
    points = 10
    #while loop runs to make sure it goes through (is it needed pobeley not but makes me feel better
    while True:
        #list of stats
        options = ["Strength", "Intellgence", "Charasma", "Dexetrity", "Constitution"]
        #make a try expect statment with a for loop that makes sure its a valid number and adds it to the proper stat
        for i in range(len(options)):
            stat = input("How many points for " + options[i]  + ": ")
            try:
                if int(stat) >= 0 and int(stat) <= points:
                    points = points - int(stat)
                    print("points left: " + str(points))
                    #update the variable number in var list
                    var[i] = var[i] + int(stat)
                    
                    i+=1
                else:
                    print("invaild number you get a 0" )
                    stat = 0
            except ValueError:
                print("invaild input")
                stat = 0
    
        # dictornary full of all the dets
        chara_det = {
            'name': name,
            'race': race,
            'Strength': var[0],
            "Intellegence": var[1],
            "Charasma": var[2],
            "dexetrity": var[3],
            "Constitution": var[4],
            "Health": health,
            "level":1,
            }
        
        #save character data to json file
        with open('chara_det.json', 'w') as fp:
            #append to json
            json.dump(chara_det, fp, indent=4, separators=(',', ': '))
        with open('past_char.txt', 'a') as f:
            f.write(str(chara_det))
            f.write("\n")
        return chara_det