import random
cpu_options = ["Rock","Paper","Scissors"]

def main():
    print("Welcome to RockPaperScissors!\n")
    print("This is my branch!\n")

    user_choice = input("Pick one Rock, Paper, or Scissors.\n> ")
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