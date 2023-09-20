import random
from secrets import choice

print("Welcome to the Heads or Tails !")
options = ["heads", "tails"]

while True:    
    choice = input("Choose between Heads or Tails or Q to quit: ").lower()
    if choice == "q":
        break
    if choice not in options:
        continue

    random_number = random.randint(0, 1)
    computer_pick = options[random_number]
    print("The coin picked", computer_pick + ".")


