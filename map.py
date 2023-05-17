#this is the map where the user is walking, it's a 10x10 grid that is an array that will have marks that will mark entering combat
#the user will be able to move around the map and enter combat with enemies
#the user will be able to save their progress and load it later
#the user will be able to find objects and also flee if they can recall the ext, like a blind map
import char_funcs as fun
import inventory as inv
import random
from rich import print
from rich.traceback import install
install()
#make the 10x10 array
def move(stats):
    map = [
        [0,2,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        ]

    #working on movment, user will use "l" for left and "r" for right. 
    #this willl be a loop that moves us through the list variable map and will check to see if the current number is 0 or 1 and if its 1 will print out "yes"
    i = 0
    j = 0
    moves = {'w':[1,0], 'a':[0,-1], 's':[-1,0], 'd':[0,1]}
    grid = map[i][j]
    while True:
        movment = input("Which way would you like to go? (w,a,s,d) or (e) to exit:")
        if movment == 'd':
            if j == 9:
                print("You are at the end of the row")
                grid = map[i][j]
                print(str(grid))
                return grid
            else:
                j = j + 1
                grid = map[i][j]
                print("Moving Right: " + str(grid))
                
        elif movment == 'a':
            if j == 0:
                print("You are at the start of the row")
                grid = map[i][j]
                print(str(grid))
            else:
                j = j - 1
                grid = map[i][j]
                print("Moving Left: " + str(grid))
        elif movment == 'w':
            if i == 0:
                print("You are at the start of the map")
                grid = map[i][j]
                print(str(grid))
            else:
                i = i - 1
                grid = map[i][j]
                print("Moving Up: " + str(grid))
        elif movment == 's':
            if i == 4:
                print("You are at the bottom of the map")
                grid = map[i][j]
                print(str(grid))
            else:
                i = i + 1
                grid = map[i][j]
                print("Moving Down: " + str(grid))
        elif movment == 'e':
            print("You have exited the map")
            break
        else:
            print("You did not enter a valid direction")
            grid = map[i][j]
        if j == 9:
            if i == 4:
                print("You have reached the end of the map")
                continue
            else:
                i += 1
                print("you have reached the end of coloum!, moving to next row")

        # if grid == 1 enter combat
        if grid == 1:
            map[i][j] = 0
            fun.combat(stats)
            continue
        else:
            pass
        # if grid == 2 enter loot
        if grid == 2:
            map[i][j] = 0
            inv.loot()
            continue


def flee():
    escape_map = [
        [0,0,0],
        [0,0,0],
        [0,0,1]
    ]
    i = 0
    j = 0
    grid = escape_map[i][j]
    while True:
        movment = input("Which way would you like to go? (w,a,s,d): ")
        if movment == 'd':
            if j == 2:
                print("ows that's the right wall")
                grid = escape_map[i][j]
                print(str(grid))
            else:
                j = j + 1
                print(i)
                print(j)
                grid = escape_map[i][j]
                print("Moving Right: " + str(grid))
                
        elif movment == 'a':
            if j == 0:
                print("ow that's the left wall")
                grid = escape_map[i][j]
                print(str(grid))
            else:
                j = j - 1
                grid = escape_map[i][j]
                print("Moving Left: " + str(grid))
        elif movment == 'w':
            if i == 0:
                print("careful along the upper wall")
                grid = escape_map[i][j]
                print(str(grid))
            else:
                i = i - 1
                grid = escape_map[i][j]
                print("Moving Up: " + str(grid))
        elif movment == 's':
            if i == 2:
                print("Careful along the wall there!")
                grid = escape_map[i][j]
                print(str(grid))
            else:
                i = i + 1
                grid = escape_map[i][j]
                print("Moving Down: " + str(grid))
        else:
            print("bro")
            grid = escape_map[i][j]
        if j == 2:
            if i == 2:
                grid = escape_map[i][j]
                print("that's the corner")
            else:
                grid = escape_map[i][j]
                print("OW! right wall")
        if grid == 1:
            print("You have escaped!")
            break
