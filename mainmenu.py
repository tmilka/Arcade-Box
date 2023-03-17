import time

from russianroulette import RussianRoulette
from rockpaperscissors import RockPaperScissors
from gtn import guess_the_number
from tictactoe import Tictactoe
from functions import Extra
from ..FastAPI import Main

while True:

    header = """
    ___                        __        ____                
   /   |  ______________ _____/ /__     / __ )____  _  __    
  / /| | / ___/ ___/ __ `/ __  / _ \   / __  / __ \| |/_/    
 / ___ |/ /  / /__/ /_/ / /_/ /  __/  / /_/ / /_/ />  <      
/_/  |_/_/   \___/\__,_/\__,_/\___/  /_____/\____/_/|_|      
    """
    print(header)

    txt = """
            Chose from the following options: 

            - Russian Roulette (1)
            - Rock Paper Scissor (2)
            - Guess the number (3)
            - Tictactoe (4)
            - FastAPI (5)
            - End Arcade Box (6)"""
    print(txt)

    option = input('            Chose your option: ')

    if option == "1":
        print("Russian Roulette it is!")
        Extra.repeat(RussianRoulette(),0)
        Extra.wait(RussianRoulette)
    elif option == "2":
        print("Rock Paper Scissor it is!")
        Extra.repeat(RockPaperScissors(), 0)
        time.sleep(2)
    elif option == "3":
        print("Guess the number it is!")
        Extra.repeat(guess_the_number,100)
        time.sleep(2)
    elif option == "4":
        print("Tictactoe it is!")
        Extra.repeat(Tictactoe(), 0)
        time.sleep(2)
    elif option == "5":
        print()
        #print(Main.getPlayers())
    elif option == "6":
        print("            See you again...")
        break

