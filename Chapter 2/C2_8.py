#Write a program that asks the user for their name and how many times to print it.
# The program should print out the user’s name the specified number of times.

name = input("What is your name? ")
times = int(input("How many times do you want to print it? "))

for i in range(times):
    print(name)