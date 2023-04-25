#this is the map where the user is walking, it's a 10x10 grid that is an array that will have marks that will mark entering combat
#the user will be able to move around the map and enter combat with enemies
#the user will be able to save their progress and load it later
#the user will be able to find objects and also flee if they can recall the ext, like a blind map

#make the 10x10 array
def move():
    map = [
        [0,1,2,3,4,5,6,7,8,9],
        [10,11,12,13,14,15,16,17,18,19],
        [20,21,22,23,24,25,26,27,28,29],
        [30,31,32,33,34,35,36,37,38,39],
        [40,41,42,43,44,45,46,47,48,49]
        ]
    #this is bad array
    #snakes down so moves left to right, then down then right to left
    #run for loop so it runs like a grid
    # for i in range(0,4):
    #     grid = map[i]
    #     print(str(grid)+"\n")
    #     i+=1


    #working on movment, user will use "l" for left and "r" for right. 
    #this willl be a loop that moves us through the list variable map and will check to see if the current number is 0 or 1 and if its 1 will print out "yes"
    i = 0
    j = 0

    grid = map[i][j]
    while True:
        movment = input("Which way would you like to go? (w,a,s,d) or (e) to exit:")
        if movment == 'd':
            if j == 9:
                print("You are at the end of the row")
                grid = map[i][j]
                print(str(grid))
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
                break
            else:
                i += 1
                print("you have reached the end of coloum!, moving to next row")