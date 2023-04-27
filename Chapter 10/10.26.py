#  Write a program that asks the user for a number and prints out all the ways to write the
# number as difference of two perfect squares, x^2 − y^2, where x and y are both between 1 and 1000. Writing a number as a difference of two squares leads to clever techniques for factoring
# large numbers.

def find_difference_of_squares(n):
    result = []
    for x in range(1, 1001):
        for y in range(1, 1001):
            if x ** 2 - y ** 2 == n:
                result.append((x, y))
    return result

num = int(input("Enter a number: "))

squares = find_difference_of_squares(num)

if squares:
    print(f"{num} can be written as the difference of two squares in the following ways:")
    for x, y in squares:
        print(f"{x}^2 - {y}^2 = {num}")
else:
    print(f"{num} cannot be written as the difference of two squares.")
