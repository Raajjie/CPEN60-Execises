# Write a program that asks the user for a weight in kilograms. The program should convert
# the weight to kilograms, formatting the result to one decimal place.

weight = int(input("Enter weight in kilograms: "))
print('The weight is {:.1f}kg'.format(weight))