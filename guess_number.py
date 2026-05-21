temp= True
while temp==True:
    user_number=int(input("Enter any number:"))
    b=23
    if b>user_number:
        print("Your entered number is lower.")
    elif user_number>b:
        print("Your entered number is higher.")
    else:
        print("You guess the correct number.")
        break