#7. An integer is called squarefree if it is not divisible by any perfect squares other than 1. For instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is divisible by 9, which is a perfect square. Write a program that asks the user for an integer and tells them if it is squarefree or not.

def is_squarefree(n):
    # Check if n is divisible by any perfect squares greater than 1
    for i in range(2, int(n**0.5)+1):
        if n % (i*i) == 0:
            return False
    return True

# Get user input
n = int(input("Enter an integer: "))

# Check if n is squarefree
if is_squarefree(n):
    print(n, "is squarefree.")
else:
    print(n, "is not squarefree.")
