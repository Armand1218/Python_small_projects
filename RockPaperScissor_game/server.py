import random

user_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose Rock, Paper or Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        continue

    # rock: 0, paper:1, scissors:2
    ran_num = random.randint(0,2)
    #the computer will choose randomly between rock, paper and scissors.
    computer_guess = choices[ran_num]
    print("Computer picked", computer_guess + ".")

    #if user choose rock and computer pick is scissors it will print you won and gain a point.
    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        user_wins += 1
        continue

    else:
        print("You Lose!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer", computer_wins, "times.")
print("Play again next time!")