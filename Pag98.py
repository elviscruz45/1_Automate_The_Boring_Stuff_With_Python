import random
guest=int(input("Please, enter a number between 1 to 100: "))
won_number=random.randint(1,21)


while True:
    if guest==won_number:
        print("You Win. The number is {}".format(won_number))
        break
    else:
        print("You loose. Try again")

        guest=int(input("Please, enter a number between 1 to 100: "))

        
    