print("Welcome to the tip calculator.")
total_cost = float(input("What was the total bill? "))
split = float(input("How many people to split the bill? "))


def tip():
    tip1 = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
    if tip1 == 10:
        tip1 = total_cost * 0.10
        final_value = total_cost + tip1
        print(final_value)
    elif tip1 == 12:
        tip1 = total_cost * 0.12
        final_value = total_cost + tip1
        print(final_value)
    elif tip1 == 15:
        tip1 = total_cost * 0.15
        final_value = total_cost + tip1
        print(final_value)
    else: 
        print("Not a valid option")
        quit


def tips():
    tip2 = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
    if tip2 == 10:
        tip2 = total_cost * 0.10
        tip_value = total_cost + tip2
        total_value_split = tip_value // split
        print(total_value_split)
    elif tip2 == 12:
        tip2 = total_cost * 0.12
        tip_value = total_cost + tip2
        total_value_split = tip_value // split
        print(total_value_split)
    elif tip2 == 15:
        tip2 = total_cost * 0.15
        tip_value = total_cost + tip2
        total_value_split = tip_value // split
        print(total_value_split)
    else:
        print("Not a valid option")
        quit

if split == 0:
    tip()
else:
    tips()
