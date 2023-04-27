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

