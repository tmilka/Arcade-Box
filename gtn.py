import random

def guess_the_number(x):
    
 #loop = "yes"
 #while loop == "yes":
    
    print("Lets play guess the number")

    r_number = random.randint(0,x)

    num_guesses = 0

    while True:
        
        guess= int(input(f"Guess a number between 0 and {x}: "))
        num_guesses += 1 

        if guess == r_number:
            print(f"Congrats, the number is {r_number}")
            break
        elif guess < r_number:
            print("Too low!")
        else:
            print("Too high!")
        