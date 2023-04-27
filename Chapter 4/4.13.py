import random

choices = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

for i in range(1, 6):
    try:
        user_choice = input("Round " + str(i) + ": Choose rock, paper, or scissors: ").lower()
    except ValueError:
        print("Invalid Input! Round skipped")
        continue

    computer_choice = random.choice(choices)
    print("You chose: ", user_choice)
    print("Computer choice: ", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
            user_choice == 'paper' and computer_choice == 'rock' or \
            user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
        user_wins +=1
    else:
        print("You lost")
        computer_wins += 1

if user_wins > computer_wins:
    print("You won!")
elif computer_wins > user_wins:
    print("You lost!")
else:
    print("It's a tie! You both won", user_wins, "rounds.")

