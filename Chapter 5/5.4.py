# Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.

total = 0
sign = 1

for number in range(1, 2001):
    total += sign * number
    sign *= -1


print("The sum of the series is:", total)