result = 0
n = int(input("Enter number: "))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

result = factorial(n)
print(result)

