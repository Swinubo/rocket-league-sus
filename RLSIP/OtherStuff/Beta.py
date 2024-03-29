def StartGame():
    print("Bring Jim to his house!")
    print("You'll be playing as Jim. \n")
    print("You will have to go around the black walls.")
    
def Help():
    print("Control Jim with: ")
    print("W - move up")
    print("S - move down")
    print("A - move Left")
    print("D - move Right")
    print("L - Quit playing \n")
    print("And if you ever forget any of this just click ?\n")

#Defining entities
wall = '⬛'
character = '🧍'
empty = '⬜'
net = '🏠'

#Defining coordinates
#Walls
CooWall1 = 2, 1
CooWall2 = 2, 2
CooWall3 = 2, 3
CooWall4 = 3, 3
CooWall5 = 5, 2
#WinSpot
WinSpot = 5, 1
#Character
X = 1
Y = 3
#Empty
Empty1 = 1, 1
Empty2 = 1, 2
Empty3 = 1, 3
Empty4 = 1, 4
Empty5 = 2, 4
Empty6 = 3, 4
Empty7 = 4, 4
Empty8 = 5, 4
Empty9 = 5, 3
Empty10 = 4, 3
Empty11 = 4, 2
Empty12 = 3, 2
Empty13 = 3, 1
Empty14 = 4, 1
    
def Place(X, Y):
    Coordinate = X, Y
    print(Coordinate)
    if Coordinate == CooWall1 or Coordinate == CooWall2 or Coordinate == CooWall3 or Coordinate == CooWall4 or Coordinate == CooWall5:
        print("You can't move there!")
    elif Coordinate == WinSpot:
        #Line 1    
        print (empty, wall, empty, empty, character)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (character, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty + "\n")
        print("Woohoo! You won!")
    elif Coordinate == Empty3:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (character, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty2:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (character, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty1:
        #Line 1    
        print (character, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty4:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (character, empty, empty, empty, empty)
    elif Coordinate == Empty5:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, character, empty, empty, empty)
    elif Coordinate == Empty6:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, character, empty, empty)
    elif Coordinate == Empty7:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, character, empty)
    elif Coordinate == Empty8:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, character)
    elif Coordinate == Empty9:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, character)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty10:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, character, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty11:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, character, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty12:
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, character, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty13:
        #Line 1    
        print (empty, wall, character, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    elif Coordinate == Empty14:
        #Line 1    
        print (empty, wall, empty, character, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (empty, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty)
    else:
        #Reminder
        print("You can't go out of bounds! Now, you will have to restart from the beginning. \n")
        
        #Line 1    
        print (empty, wall, empty, empty, net)
        #Line 2    
        print (empty, wall, empty, empty, wall)
        #Line 3    
        print (character, wall, wall, empty, empty)
        #Line 4   
        print (empty, empty, empty, empty, empty, "\n")

        
StartGame()
Help()

print("Good luck!\n")
#Line 1    
print (empty, wall, empty, empty, net)
#Line 2    
print (empty, wall, empty, empty, wall)
#Line 3    
print (character, wall, wall, empty, empty)
#Line 4   
print (empty, empty, empty, empty, empty + "\n")


user_input = input("\n").upper()
    
while user_input != "L":
    if user_input == "W":
        Y = Y - 1
        if ((Y == 5) or (Y == 0)):
            X = 1
            Y = 3
            print("Since you went out of bounds, you will now go back to the starting position.\n")
        Place(X, Y)
        user_input = input("\n").upper()
    elif user_input == "S":
        Y = Y + 1
        if ((Y == 5) or (Y == 0)):
            X = 1
            Y = 3
            print("Since you went out of bounds, you will now go back to the starting position.\n")
        Place(X, Y)
        user_input = input("\n").upper()
    elif user_input == "A":
        X = X - 1
        if ((X == 6) or (X == 0)):
            X = 1
            Y = 3
            print("Since you went out of bounds, you will now go back to the starting position. \n")
        Place(X, Y)
        user_input = input("\n").upper()
    elif user_input == "D":
        X = X + 1
        if ((X == 6) or (X == 0)):
            X = 1
            Y = 3
            print("Since you went out of bounds, you will now go back to the starting position.\n")
        Place(X, Y)
        user_input = input("\n").upper()
    elif user_input == "?":
        Help()
        user_input = input("\n").upper()
    else:
        print("You wrote the wrong input.")
        user_input = input("\n").upper()
        
print("Goodbye!")
