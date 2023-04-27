# Write a program to play the following simple game. The player starts with $100. On each
# turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
# correct guess and loses $10 for each incorrect guess. The game ends either when the player
# runs out of money or gets to $200.

import random

player = 100
coin = ["heads", "tails"]

while True:
    if player <= 0 or player >= 200:
        break
    coin_random = random.choice(coin)
    player_guess = input("Guess, heads or tails?: ").lower()
    print("Your guess: ", player_guess)
    print("Computer guess:", coin_random)
    if player_guess == coin_random:
        player += 9
        print("You guessed right!")
    elif player_guess != coin_random:
        player -= 10
        print("You guessed wrong!")
    print("Current money: ", player, "$")

if player <= 0:
    print("You lost!")
elif player >= 200:
    print("You Won")

