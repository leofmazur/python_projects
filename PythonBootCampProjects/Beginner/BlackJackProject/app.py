import random
import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random_cards_pc = []
random_cards_user = []

def random_cards_add ():
    for i in range(1):
        user_cards = random.choice(cards)
        random_cards_user.append(user_cards)
    for n in range(0, len(random_cards_user)):
        random_cards_user[n] = int(random_cards_user[n])


def random_cards_add_pc():
    for i in range(1):
        pc_cards = random.choice(cards)
        random_cards_pc.append(pc_cards)
    for n in range(0, len(random_cards_pc)):
        random_cards_pc[n] = int(random_cards_pc[n])


def adding_cards_user(user_cards_add):
    for n in range(0, len(random_cards_user)):
        random_cards_user[n] = int(random_cards_user[n])
    for user_sum in random_cards_user:
        user_cards_add += user_sum
    return user_cards_add


def adding_cards_pc(pc_cards_add):
    for n in range(0, len(random_cards_pc)):
        random_cards_pc[n] = int(random_cards_pc[n])
    for pc_sum in random_cards_pc:
        pc_cards_add += pc_sum
    return pc_cards_add


def checking_score(anything):
    if anything == True:
        if adding_cards_user(user_cards_add = 0) == 21 and adding_cards_pc(pc_cards_add = 0) == 21:
            print("Draw")
            return anything
        elif adding_cards_user(user_cards_add = 0) == 21:
            print("You won!")
            return anything
        elif adding_cards_pc(pc_cards_add = 0) == 21:
            print("You lost")
            return anything
        elif adding_cards_pc(pc_cards_add = 0) > 21:
            print("You Won!")
            return anything
        else:
            if adding_cards_user(user_cards_add = 0) > 21:
                print("You lost!")
                return anything
    else:
        return False
                

#Beggining of the game
start_game = input("Do you wanna play BlackJack? Y or N ").lower()
if start_game == 'y':
    #game_image and the lists
    print(logo.logo)

    #generating the two random cards to start the game
    for i in range(2):
        user_cards = random.choice(cards)
        random_cards_user.append(user_cards)
        computer_cards = random.choice(cards)
        random_cards_pc.append(computer_cards)
    print(f"The computer card is: {random_cards_pc[0]}")
    print(f"Your cards are: {random_cards_user}")

    while True:

        #Checking if anyone got cards greater than 21
        if checking_score(anything=True):
            break

        #Decision if the user wants to get another card
        text = input("Do you want another card? Y or N: ").lower()
        if text == "y":
            random_cards_add()
            adding_cards_user(user_cards_add = 0)
            print(random_cards_user)
        else:
            checking_cards = True
            while checking_cards != False:
                if adding_cards_pc(pc_cards_add=0) < 17:
                    random_cards_add_pc()
                    adding_cards_pc(pc_cards_add=0)
                    if checking_score(anything=True):
                        break
                else:
                    checking_cards = False

            #Checking if the PC exceeded the cards
            if adding_cards_pc(pc_cards_add = 0) > 21:
                print("You Won!")
                break
            
            #Final Check to find out who won
            if adding_cards_pc(pc_cards_add=0) > adding_cards_user(user_cards_add = 0):
                print(f"The computer cards were: {random_cards_pc}")
                print(f"Your cards were: {random_cards_user}")
                print("You Lost!")
                break
            else:
                print(f"The computer card were: {random_cards_pc}")
                print(f"Your cards were: {random_cards_user}")
                print("You won!")
                break
else:
    print("Bye Bye !")


#The way she did it.
# import random
# from replit import clear
# from art import logo

# def deal_card():
#   """Returns a random card from the deck."""
#   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#   card = random.choice(cards)
#   return card


# def calculate_score(cards):
#   """Take a list of cards and return the score calculated from the cards"""

#   #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#   if sum(cards) == 21 and len(cards) == 2:
#     return 0
#   #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
#   if 11 in cards and sum(cards) > 21:
#     cards.remove(11)
#     cards.append(1)
#   return sum(cards)

# #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"


#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"

# def play_game():

#   print(logo)

#   #Hint 5: Deal the user and computer 2 cards each using deal_card()
#   user_cards = []
#   computer_cards = []
#   is_game_over = False

#   for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

#   #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#   while not is_game_over:
#     #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"   Your cards: {user_cards}, current score: {user_score}")
#     print(f"   Computer's first card: {computer_cards[0]}")

#     if user_score == 0 or computer_score == 0 or user_score > 21:
#       is_game_over = True
#     else:
#       #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#       user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#       if user_should_deal == "y":
#         user_cards.append(deal_card())
#       else:
#         is_game_over = True

#   #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#   while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

#   print(f"   Your final hand: {user_cards}, final score: {user_score}")
#   print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#   print(compare(user_score, computer_score))

# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#   clear()
#   play_game()