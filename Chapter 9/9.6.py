from random import randint

sn = randint(1, 100)

for ng in range(5):
    guesses_left = 4 - ng
    guess = int(input("Enter your guess (1-100): "))
    if guess < sn:
        print("Higher. ", end="")
    elif guess > sn:
        print("Lower. ", end="")
    else:
        print("You got it!")
        break

    if guesses_left == 1:
        print("1 guess left.")
    else:
        print(f"{guesses_left} guesses left.")

else:
    print(f"You lose. The correct number is {sn}.")
