total = 0
sign = 1

for number in range(1, 2001):
    total += sign * number
    sign *= -1


print("The sum of the series is:", total)