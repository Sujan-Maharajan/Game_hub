def quiz():

    a=int(input("Press 1 to play game or Press 0 to exit: "))
    while a==1:
        count=0
        score=0

        print("Rules:\nPress 1 to select first option")
        print("Press 2 to select second option")
        print("Press 3 to select third option\n")

        print("Question 1: What is the height of Mt.Everest?")
        print("1. 8048")
        print("2. 8484")
        print("3. 8848")

        try:
            a1 = int(input("Your answer: "))
            if a1 == 3:
                count += 1
        except:
            print("Invalid input")

        print("\nQuestion 2: Where is Mt.Everest located?")
        print("1. India")
        print("2. Nepal")
        print("3. China")

        try:
            a1 = int(input("Your answer: "))
            if a1 == 2:
                count += 1
        except:
            print("Invalid input")

        print("\nQuestion 3: What is the capital of Nepal?")
        print("1. Pokhara")
        print("2. Hetauda")
        print("3. Kathmandu")

        try:
            a1 = int(input("Your answer: "))
            if a1 == 3:
                count += 1
        except:
            print("Invalid input")

        print("\nQuestion 4: Which planet is known as the Red Planet?")
        print("1. Mercury")
        print("2. Venus")
        print("3. Mars")

        try:
            a1 = int(input("Your answer: "))
            if a1 == 3:
                count += 1
        except:
            print("Invalid input")

        print("\nQuestion 5: Which symbol is used for comments in Python?")
        print("1. #")
        print("2. \\")
        print("3. //")

        try:
            a1 = int(input("Your answer: "))
            if a1 == 1:
                count += 1
        except:
            print("Invalid input")

        if count==5:
            score=100
        elif count==4:
            score=80
        elif count==3:
            score=60
        elif count==2:
            score=40
        elif count==1:
            score=20
        else:
            score=0
        
        print("\nYou got",count,"answers correct.")
        print("Your score is:",score)
    
        a=int(input("Press 1 to play game: "))

quiz()