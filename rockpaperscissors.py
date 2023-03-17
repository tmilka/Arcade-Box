import random

def RockPaperScissors():

 loop = "yes"
 while loop == "yes":
    print('Lets play Rock Paper Scissors')

    r = 'rock'
    p = 'paper'
    s = 'scissors'

    all_choices = [r,p,s]

    user = input(f'Enter your choice ({r}, {p}, {s}): ')

    if user not in all_choices:
        print('invalid choice!')
        return

    computer = random.choice(all_choices)

    print(f'User chose {user}, computer chose {computer}')

    # r>s p>r s>p

    if user == computer:
        print('Tie!')
    elif(user == r and computer == s) or (user == p and computer == r) or (user == s and computer == p):
        print('You won!')
    else:
        print('You lost!')
    
    print("You want to give it another try?")
    loop = input("yes/no")
 else:
    print("Allright, your choice...")

