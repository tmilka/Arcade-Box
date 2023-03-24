import time
import random
from functions import Extra

def RussianRoulette(name):

    print("Welcome to Russian Roulette!")

    y= int(input("How many bullets in the magazine: "))
    x = random.randrange(1, y, 1)
    bullet = random.randrange(1, y, 1)
    
    print("You load the bullet")
    time.sleep(1)
    print("You spin the chamber as fast as you can hopping to live till tomorow")
    time.sleep(1)
    print("You think over your live choices as it stops spinning...")
    time.sleep(1)
    print("You raise the gun to your head.")

    time.sleep(random.randrange(3,5))

    if x == bullet:
        print("The gun goes off. You are dead.")
    else:
        print("The gun makes clicking noises redering you unharmed. You live to see another day!")
        Extra.scoreUp(name)
