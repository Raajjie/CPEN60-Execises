#A good program will make sure that the data its users enter is valid. Write a program that
#asks the user for a weight and converts it from kilograms to pounds. Whenever the user
#enters a weight below 0, the program should tell them that their entry is invalid and then ask
#them again to enter a weight. [Hint: Use a while loop, not an if statement].

print("This is a weight converter from kilograms to pounds")
kg = eval(input("Enter weight in kilograms: "))

while kg > 0:
    print("The weight in pounds is = ",kg*2.20462)
    break
else:
    print("Error")


