import random
temp = True
tries = 0
random_number = random.randint(1, 100)

while temp == True:

    user_number = int(input("Enter any number between 1 to 100:"))
    tries += 1

    if random_number > user_number:
        print("Your entered number is lower.")

    elif user_number > random_number:
        print("Your entered number is higher.")

    else:
        print("\nYou guess the correct number.")
        print("Total tries:",tries)

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
        
        print("Your score is:", score)

        break