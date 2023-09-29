import random

topRange = input("Enter a random number: ")

if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
        print("Please enter a number greater than 0.")
        quit()

else:
    print("Please enter numbers only.")
    quit()

ran_num = random.randint(0, topRange)
correct_guess = 0

while True:
    user_number = input("Make a guess: ")
    correct_guess += 1
    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("Please enter a number next time.")
        continue

    if user_number == ran_num:
        print("Your guess is correct!")
        break
    elif user_number > ran_num:
        print("Your number above the random number.")
    else:
        print("Your number is below the random number.")
