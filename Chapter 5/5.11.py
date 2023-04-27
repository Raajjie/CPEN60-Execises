# Write a program that computes the factorial of a number. The factorial, n!, of a number n is the
# product of all the integers between 1 and n, including n. For instance, 5! = 1 · 2 · 3 · 4 · 5 = 120.
# [Hint: Try using a multiplicative equivalent of the summing technique.]

result = 1
n = int(input("Enter number: "))


if n < 0:
    print("Factorial cannot be computed for negative numbers.")
elif n == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        result *= i

print(result)

