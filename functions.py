import time

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
