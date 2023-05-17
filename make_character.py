# imports here
from time import sleep
import json

# making the charactor
# so this is lists, its kinda a jumble but just cause I need it to be
def make_character():
    print("MAKE YOUR CHARACTOR\n")
    races = ["Orc", "Elf", "Wood Elf", "Dark Elf", "Dragonborn", "Dwarf", "Human", "Goblin"]
    name = input("What is your Charater's Name? ").title()
    print(races)
    while True:
        #insert if statment or something to insure a actual race is being entered
        race = input("Pick a race from the list above and enter it: ").title()
        #make sure they entered the an option from the races list
        if race in races:
            break
        else: 
            print("invalid option please try again")
    #starting health value
    health = 15
    # making the stats for charactor
    print("Welcome " + name + " so your a " + race + " well there is a few things left to do")
    print("you have 10 points to use so enter them accordingly you can use it on strength, intellgence. charasma, dexetrity, and Constitution")
    points = 10
    #while loop runs to make sure it goes through (is it needed pobeley not but makes me feel better
    while True:
        #list of stats
        options = ["Strength", "Intellgence", "Charasma", "Dexetrity", "Constitution"]
        #list of the varibles
        strength, intel, charsama, dex, conc = 0,0,0,0,0
        var = [strength, intel, charsama, dex, conc]
        #make a try expect statment with a for loop that makes sure its a valid number and adds it to the proper stat
        for i in range(len(options)):
            stat = input("How many points for " + options[i]  + ": ")
            try:
                if int(stat) >= 0 and int(stat) <= points:
                    points = points - int(stat)
                    print("points left: " + str(points))
                    #update the variable number in var list
                    var[i] = int(stat)
                    
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
            }
        #no you can't have save and load yet need to have a save and load function and the game 

        # work out how to print the dets
        # run through the dictornary and print the key and value
        # for key, value in chara_det.items():
        #     print(key, value)

        #save character data to json file
        with open('chara_det.json', 'w') as fp:
            #append to json
            json.dump(chara_det, fp, indent=4, separators=(',', ': '))
        with open('past_char.txt', 'a') as f:
            f.write(str(chara_det))
            f.write("\n")
        #okay actual storry now
        # do a file import like one is all character making the next is story? you know what yes lets do that
        return chara_det
