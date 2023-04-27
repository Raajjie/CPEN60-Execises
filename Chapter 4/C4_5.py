#Generate a random number between 1 and 10. Ask the user to guess the number and print a
#message based on whether they get it right or not.

import random
lst = []
print("This is a Guessing Game")
guess = int(input("Guess this random number from 1 to 10:"))
random_number = random.randint(1,10)
lst.append(random_number)

if guess == lst:
    print("You guessed correctly!!"
          "Good Job!!")
else:
    print("You are wrong!!"
          "Better luck Next Time!")

print("The number is:",random_number)