import random 


def rollDice():
    cont = input("Would you like to roll the dice?")
    while cont != "no":
        dice = random.randint(1,6)
        print("You rolled a %s" % (dice))
        cont = input("Would you like to roll again?")

        if cont == "no":
            print("goodbye!")



rollDice()
    

