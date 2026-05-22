import random

from dataManager.dataManager import *

words = [
    "WORDS",
    "RELIC",
    "HOUSE",
    "PLANT",
    "SHAVE",
    "STONE",
    "TRAIN",
    "LIGHT",
    "MONEY",
    "WATER"
]

secret_word = random.choice(words)

tries = 0

while True:

    guess = input("Enter the five letter word: ").upper()

    while len(guess) != 5:
        print("Word must contain exactly five letters")
        guess = input("Enter the five letter word: ").upper()

    tries += 1

    for i in range(5):
        count = 0

        for j in range(5):
            if guess[i] == secret_word[j]:
                count += 1

        if count != 0:
            print(guess[i], "is correct. There are", count, guess[i])
        else:
            print(guess[i], "is incorrect")

    if guess == secret_word:

        if tries == 1:
            score = 100
        elif tries == 2:
            score = 80
        elif tries == 3:
            score = 60
        elif tries == 4:
            score = 40
        else:
            score = 20

        print("\nYou guessed it correctly")
        print("Total tries:", tries)
        print("Your score is:", score)

        save_score("wordle", score, "Sujan")
        print("\nScore Saved Successfully")

        break