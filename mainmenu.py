import time
from russianroulette import RussianRoulette
from rockpaperscissors import RockPaperScissors
from gtn import guess_the_number
from tictactoe import tictactoe
from functions import Extra, Login
from scoreboard import Scoreboard

name = Login.intro()

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
            - Scoreboard (5)
            - End Arcade Box (6)"""
    print(txt)

    option = input('            Chose your option: ')

    if option == "1": #finished
        print("Russian Roulette it is!")
        Extra.repeat(RussianRoulette,name)
        Extra.wait(RussianRoulette)
    elif option == "2":
        print("Rock Paper Scissor it is!")
        Extra.repeat(RockPaperScissors,name)
        time.sleep(2)
    elif option == "3":
        print("Guess the number it is!")
        Extra.repeat(guess_the_number,100,name)
        time.sleep(2)
    elif option == "4":
        print("Tictactoe it is!")
        Extra.repeat(tictactoe)
        time.sleep(2)
    elif option == "5":
        print("Scoreboard it is!")
        Scoreboard.main()
    elif option == "6":
        print("            See you again...")
        break