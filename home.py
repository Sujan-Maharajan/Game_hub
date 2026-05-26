from dataManager.dataManager import *
from wordle import *
from guess_number import *
from view_score_and_leaderboard import *

temp = True
while temp == True:

    print("\nPress 1 to Play Games")
    print("Press 2 to View Profile")
    print("Press 3 to View Leaderboard")
    print("Press 4 to Exit\n")
    num = int(input("Enter your choice:"))

    if num == 1:
        print("Press 1 to Play Wordle")
        print("Press 2 to Play Number Guessing Game")
        print("Press 3 to Play Rock Paper Scissor")
        print("Press 4 to Play Tic Tak Toe")
        game=input("\nSelect your game:")
        if game==1:
            wordle("username")
        else:
            print("Invalid input")

    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        temp = False
    else:
        print("Invalid Input")
        temp = False