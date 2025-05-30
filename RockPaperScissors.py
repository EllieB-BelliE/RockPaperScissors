import random

print("Welcome to RockPaperScissors!\n")
print("This is my branch!\n")

user_choice = input("Pick one Rock, Paper, or Scissors.\n> ")

cpu_options = ["Rock","Paper","Scissors"]
cpu_choice = random.choice(cpu_options)

print("You chose " + user_choice + ", I chose " + cpu_choice)
if cpu_choice == user_choice:
    print ("Tie!")
elif cpu_choice == 'Rock':
    if user_choice == 'Paper':
        print("You win!")
    else: 
        print("You lose!")

elif cpu_choice == 'Paper':
    if user_choice == 'Rock':
        print("You lose!")
    else:
        print("You win!")

else:
    if user_choice == 'Rock':
        print("You win")
    else:
        print("You lose")
