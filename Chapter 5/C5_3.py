#Write a program that asks the user to enter a value n, and then computes(1+1/2+1/3+...+1/n)-ln(n)

import math

n = float(input("Enter a number: "))
calc = (1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/n)
print("The answer is", calc - math.log(n))