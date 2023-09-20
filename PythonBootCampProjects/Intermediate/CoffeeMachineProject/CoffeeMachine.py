from CoffeeMachineData import MENU

# print("Welcome to the Coffee Machine!")

# things_on_machine = {
#     "water_on_machine": 1000,
#     "coffee_on_machine": 500,
#     "milk_on_machine": 1000,
#     "money": 50,
# }


# def checking_items(user_choice):
#     if things_on_machine["water_on_machine"] < MENU[user_choice]["ingredients"]["water"]:
#         print("Sorry there is not enough water")
#         return False
#     elif things_on_machine["coffee_on_machine"] < MENU[user_choice]["ingredients"]["coffee"]:
#         print("Sorry there is not enough coffee")
#         return False
#     elif things_on_machine["milk_on_machine"] < MENU[user_choice]["ingredients"]["milk"]:
#         print("Sorry there is not enough milk")
#         return False
#     else:
#         w_update = things_on_machine["water_on_machine"] - MENU[user_choice]["ingredients"]["water"]
#         c_update = things_on_machine["coffee_on_machine"] - MENU[user_choice]["ingredients"]["coffee"]
#         m_update = things_on_machine["milk_on_machine"] - MENU[user_choice]["ingredients"]["milk"]
#         things_on_machine.update({"water_on_machine": w_update})
#         things_on_machine.update({"coffee_on_machine": c_update})
#         things_on_machine.update({"milk_on_machine": m_update})


# def insert_coins(quarter, dime, nickel, penny):
#     q_result = quarter * 0.25
#     d_result = dime * 0.10
#     n_result = nickel * 0.05
#     p_result = penny * 0.01
#     total = round(q_result + d_result + n_result + p_result, 2)
#     if total < MENU["espresso"]["cost"]:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#     else:
#         if total == MENU["espresso"]["cost"]:
#             add_money = things_on_machine["money"] + total
#             things_on_machine.update({"money": add_money})
#         else:
#             add_money = things_on_machine["money"] + MENU["espresso"]["cost"]
#             things_on_machine.update({"money": add_money})
#             change = round(total - MENU["espresso"]["cost"], 2)
#             print(f"Here's your change ${change}")


# while True:
#     choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if choice == "espresso":
#         print("Please insert coins!")
#         quarters = int(input("How many quarters? "))
#         dimes = int(input("How many dimes? "))
#         nickels = int(input("How many nickels? "))
#         pennies = int(input("How many pennies? "))
#         insert_coins(quarters, dimes, nickels, pennies)
#         checking_items(choice)
#         print(f"Here's your {choice}")
#     elif choice == "latte":
#         print("Please insert coins!")
#         quarters = int(input("How many quarters? "))
#         dimes = int(input("How many dimes? "))
#         nickels = int(input("How many nickels? "))
#         pennies = int(input("How many pennies? "))
#         insert_coins(quarters, dimes, nickels, pennies)
#         checking_items(choice)
#         print(f"Here's your {choice}")
#     elif choice == "cappuccino":
#         print("Please insert coins!")
#         quarters = int(input("How many quarters? "))
#         dimes = int(input("How many dimes? "))
#         nickels = int(input("How many nickels? "))
#         pennies = int(input("How many pennies? "))
#         insert_coins(quarters, dimes, nickels, pennies)
#         checking_items(choice)
#         print(f"Here's your {choice}")
#     elif choice == "report":
#         print("Please insert coins!")
#         quarters = int(input("How many quarters? "))
#         dimes = int(input("How many dimes? "))
#         nickels = int(input("How many nickels? "))
#         pennies = int(input("How many pennies? "))
#         insert_coins(quarters, dimes, nickels, pennies)
#         checking_items(choice)
#         print(f"Here's your {choice}")
#     else:
#         break



#The other way to do it.
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])