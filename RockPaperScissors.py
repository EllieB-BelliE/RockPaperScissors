import random
cpu_options = ["rock","paper","scissors"]

def main():
    print("Welcome to RockPaperScissors!\n")

    user_choice = None
    while user_choice not in cpu_options:
        user_choice = input("Please enter an option from the list, Rock, Paper ,Scissors\n> ").lower()
    cpu_choice = random.choice(cpu_options)

    print("You chose " + user_choice + ", I chose " + cpu_choice)
    if cpu_choice == user_choice:
        print ("Tie!")
    elif cpu_choice == 'Rock': 
        lose() if user_choice == 'Paper' else win()
    elif cpu_choice == 'Paper':
        lose() if user_choice == 'Rock' else win()
    else:
        win() if user_choice == 'Rock' else lose()

def win():
    print("You win!")

def lose():
    print("You lose!")


main()