name = input("Please type your name: ")
print("Welcome", name, "to your own adventure!")

answer = input("Please choose between left or right: ").lower()

if answer == "left":
    answer = input("You're on a random city! You want to ride the bus or hitchhike a car? ")
    
    if answer == "ride the bus":
        print("You reach your your destination within an hour!")
    elif answer == "hitchhike a car":
        print("The car you hitchhiked with is a robber and you guys got caught by the police!")
    else:
        print("You didn't choose a path! Please start at the beginning")

elif answer == "right":
    answer = input("You're on a jungle! please choose between climbing the trees or swimming the river? ")

    if answer == "climbing the trees":
        print("There's a big snake waiting for you and you lose...")
    elif answer == "swimming the river":
        print("Congrats! You just discover a town and gave you food and helped you get home!")
    else:
        print("You didn't choose a path! Please start at the beginning")

else:
    print("The answer you put isn't valid. Please start at the beginning!")