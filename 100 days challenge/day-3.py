print("Welcome to the Treasure Island.\n")
print("Your Mission is to find Treasure.\n You are at Crossroad. Which way you want to go?\n")
choice1=input("Left or Right.  \n")
choice1.lower()
if choice1=="right":
    print("You fell into a Hole. Game Over....")
elif choice1=="left":
    choice2=input("You have come to a lake. There is an Island in the center of the lake.\n Would you like wait for boat or swim?:")
    choice2.lower()
    if choice2=="wait":
        print("You have taken boat and reached the Island.\n There is a House with 3 doors painted Red,Blue,Green.")
        choice3=input("Which door would you like to open Red,Blue or Green?")
        choice3.lower()
        if choice3=="red":
            print("It's a room full of fire, you are burned. Game Over...")
        elif choice3=="green":
            print("It's a trap,you are in lion's room. You are Eaten. Game Over...")
        elif choice3=="blue":
            print("You found the Treasure Box filled with Gold. YOU WIN !!!")
        else:
            print("Invalid Choice.")
    elif choice2=="swim":
        print("You tried swim and Eaten by Sea Monsters. Game Over...")
    else:
        print("Invalid Choice.")
else:
    print("Invalid Choice.")