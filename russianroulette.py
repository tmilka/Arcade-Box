import random

def RussianRoulette():

 loop = "yes"

 while loop == "yes":

  spin = random.randint(1,6)

  bullets = int(input("Lade 1 bis 6 Kugeln in den Revolver!"))

  print("You load the bullet")

  print("You spin the chamber as fast as you can hopping to live till tomorow")

  print("You think over your live choices as it stops spinning...")

  print("You raise the gun to your head.")

  spinner = random.randint(1,6)


  if spinner == spin:
    print("The gun goes off. You are dead.")

  if spinner != spin:
    print("The gun makes clicking noises redering you unharmed. You live to see another day!")
  
  print("You want to give it another try?")
  loop = input("yes/no")

 else:
  print("Allright, your choice...")
