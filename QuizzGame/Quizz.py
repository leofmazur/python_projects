#Quizz Game

from queue import PriorityQueue


print("Welcome to my game!")

answer = input("Do you want to play the game? ")
if answer.lower() != "yes":
    quit()

print("So let's play the game!")
score = 0

answer = input("What does SCCP stand for? ").lower()
if answer == ("sport clube corinthians paulista"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SPFC stand for? ").lower()
if answer == ("sao paulo futebol clube"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PAL stand for? ").lower()
if answer == ("palmeiras"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ATL stand for? ").lower()
if answer == ("atletico"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " points")
print("You got " + str((score / 4) * 100) + "%")