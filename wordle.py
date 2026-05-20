import random

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

while True:

    guess = input("Enter the five letter word: ").upper()

    while len(guess) != 5:
        print("Word must contain exactly five letters")
        guess = input("Enter the five letter word: ").upper()

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
        print("\nYou guessed it correctly")

        break