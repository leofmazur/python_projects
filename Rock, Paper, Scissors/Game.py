import random

computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Choose rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("The computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw")

    elif user_input == "rock" and computer_pick == "rock":
        print("Draw")

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw")

    else:
        print("The computer won!")
        computer_wins += 1

print("You got", user_wins, "wins.")
print("The computer got", computer_wins, "wins.")
print("Bye Bye!")


