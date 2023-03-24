import sqlite3
import time

conn = sqlite3.connect("players.db")
c = conn.cursor()

class Scoreboard:

    def main():
       
        while True:

            header='''
  _________                         ___.                          .___
 /   _____/ ____  ___________   ____\_ |__   _________ _______  __| _/
 \_____  \_/ ___\/  _ \_  __ \_/ __ \| __ \ /  _ \__  \\_  __ \/ __ | 
 /        \  \__(  <_> )  | \/\  ___/| \_\ (  <_> ) __ \|  | \/ /_/ | 
/_______  /\___  >____/|__|    \___  >___  /\____(____  /__|  \____ | 
        \/     \/                  \/    \/           \/           \/ 
            '''
            print(header)
            txt= '''
            Chose from the following options: 

                - Show Scoreboard (1)
                - Show Scoreboard sorted (2)
                - Search player (3)
                - Delete player (4)
                - Back to Mainmenu (5)
            '''
            print(txt)

            option = input('            Chose your option: ')

            if option == "1":
                print("Show Scoreboard it is!")
                print(*Scoreboard.getAllPlayers(), sep="\n")
                input("press any key to return to the menu")
            elif option == "2":
                print("Show Scoreboard sorted it is!")
                print(*Scoreboard.sortScores(), sep="\n")
                input("press any key to return to the menu")
            elif option == "3":
                print("Search player it is!")
                print(Scoreboard.getPlayerByName())
                input("press any key to return to the menu")
            elif option == "4":
                print("Delete player it is!")
                Scoreboard.deletePlayer()
            elif option == "5":
                print("            See you again...")
                break

    def getAllPlayers():
        with conn:
            c.execute("SELECT * FROM players")
            return c.fetchall()
    def getPlayerByName():
        with conn:
            name = input("Please enter the name: ")
            player = c.execute("SELECT * FROM players WHERE name=:name", {'name': name}).fetchall()
            return player
    def deletePlayer():
        with conn:
            name = input("Please enter the name: ")
            c.execute("DELETE from players WHERE name = :name", {"name": name})
            print("Player "+ name + "has been deleted!")
            time.sleep(2)

    def sortScores():
        list = Scoreboard.getAllPlayers()
        scorelist = sorted(list, key=lambda x: x[2], reverse=True)
        return scorelist
