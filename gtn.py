import random
from functions import Extra

def guess_the_number(x,name):
    
    print("Lets play guess the number")

    r_number = random.randint(0,x)

    num_guesses = 0

    while True:
        
        guess= int(input(f"Guess a number between 0 and {x}: "))
        num_guesses += 1 

        if guess == r_number:
            print(f"Congrats, the number is {r_number}")
            Extra.scoreUp(name)
            break
        elif guess < r_number:
            print("Too low!")
        else:
            print("Too high!")
        