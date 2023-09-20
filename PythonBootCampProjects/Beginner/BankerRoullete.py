import random

name_string = input("Type the name of the people: ")
names = name_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
bill = names[random_choice]
print(bill)

#bill = random.choice(names)
#print(bill + "is paying the bill") também vai funcionar do mesmo jeito