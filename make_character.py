# imports here
from time import sleep
import json

# making the charactor
# so this is lists, its kinda a jumble but just cause I need it to be
def make_character():
    print("welcome! This is a fun little fighter game that i will work from on tommorrow")
    races = ["Orc", "Elf", "Wood Elf", "Dark Elf", "Dragonborn", "Dwarf", "Human", "Goblin"]
    name = input("What is your Charater's Name? ").title()
    print(races)
    #insert if statment or something to insure a actual race is being entered
    race = input("Pick a race from the list above and enter it: ").title()
    #starting health value
    health = 15
    # making the stats for charactor
    print("Welcome " + name + " so your a " + race + " well there is a few things left to do")
    print("you have 10 points to use so enter them accordingly you can use it on strength, intellgence. charasma, dexetrity, and Constitution")
    points = 10
    #while loop runs to make sure it goes through (is it needed pobeley not but makes me feel better
    while True:
        #list of stats
        # stats = ["Strength", "Intellgence", "Charasma", "Dexetrity", "Constitution"]
        #make a try expect statment with a for loop that makes sure its a valid number and adds it to the proper stat
        # for i in stats():
        #     stat = input("How many points for " + stat + ": ")
        #     if int(stat) > 0 and int(stat) <= points:
        #         points = points - int(stat)
        #         print("points left: " + str(points))
        #         #save into stat into correct variable
        #         num[i] = stat
        #         i+
        #     else:
        #         print("invaild number your " + stat + " is 0")
        #         stat = 0
        strength = input("How many points for strength: ")
        if int(strength) >= 0 and int(strength) <= 10:
            points = points - int(strength)
            print("points left: " + str(points))
        else:
            print("invaild number your strength is 0")
            strength = 0

        intel = input("How many points for intellgence: ")
        if int(intel) >=0 and int(intel) <= points:
            points = points - int(intel)
            print("points left: " + str(points))
        else:
            print("invaild number your intellegence is 0")
            intellegence = 0

        charsama = input("How many points for Charasma: ")
        if int(charsama) >= 0 and int(charsama) <= points:
            points = points - int(charsama)
            print("points left: " + str(points))
        else:
            print("invaild number your charasma is 0")
            charsama = 0

        dex = input("How many points for dexetrity: ")
        if int(dex) >= 0 and int(dex) <= points:
            points = points - int(dex)
            print("points left: " + str(points))
        else:
            print("invaild number your dexetrity is 0")
            dex = 0

        conc = input("How many points for constiution: ")
        if int(conc) >= 0 and int(conc) <= points:
            points = points - int(conc)
            print("points left: " + str(points))
        else:
            print("invaild number your constiution is 0")
            conc = 0
        break
    # dictornary full of all the dets
    chara_det = {
        'name': name,
        'race': race,
        'Strength': strength,
        "Intellegence": intel,
        "Charasma": charsama,
        "dexetrity": dex,
        "Constitution":conc,
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
