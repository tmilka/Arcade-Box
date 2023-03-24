import time
import sqlite3


class Extra:

    def wait(function):
        function
        time.sleep(2)

    def repeat(function, *args):
        all_answers = ["yes", "y", "Yes"]

        while True:
            
            try:
                function(*args)
            
                print("You want to give it another try?")
                choice = input("yes/no: ")


                if choice not in all_answers:
                    print("Allright, your choice...")
                    return False
              
            except TypeError:
                print("answer contained a Typo! Going back to the Main menu...")
                break
        
    def scoreUp(name):
                conn = sqlite3.connect("players.db")
                c = conn.cursor()

                #get player
                c.execute("SELECT * FROM players WHERE name=:name", {'name': name})
                player = c.fetchall()
                user = player[0]
                x = user[2]
                newScore = x+1
                
                #Update score
                c.execute('''UPDATE players SET score = :score WHERE name= :name''',
                {'name': user[1], 'score': newScore})
                conn.commit()
                c.close()
                print("Your new score is: "+ str(newScore))
    

class Login:
        #dialog

    def intro():
            # establish DB connection
            conn = sqlite3.connect("players.db")
            c = conn.cursor()
            userExist = True
            all_answers = ["yes", "y", "Yes"]

            print("Welcome to Tim´s Arcade Box!")
            name = input("Enter your Username: ")
            
            #get player by name
            c.execute("SELECT * FROM players WHERE name=:name", {'name': name})
            player = c.fetchone()
            # player allready exist?
            try:
                if player[1] == name:
                    userExist = True      
            except TypeError:
                userExist = not userExist

            if userExist == True:
                print("Hi " + name + ", glad to see you again!")
            else:
                print("No player found!")
                options = input("Create new player? y/n")

                if options in all_answers:
                    name = input("Choose your name: ")
                    score = 0
                    
                    print(name)

                    #player_id is always Max count from players +1
                    c.execute("SELECT COUNT(name) FROM players")
                    player_id = c.fetchall()
                    player_id = player_id[0]
                    player_id = player_id[0]+1
                    
                    print(player_id)
                    #create player
                    try:
                        c.execute("INSERT INTO players VALUES (:player_id, :name, :score)", {'player_id': player_id, 'name': name, 'score':score})
                        conn.commit()
                        print("Hi " + name + "!")
                    except:
                        print("Error occured!")
                    print(name)

                    print(c.execute("SELECT * FROM players").fetchall())
                    conn.close()
                else:
                    print("See ya!")
                    quit()
            return name

    