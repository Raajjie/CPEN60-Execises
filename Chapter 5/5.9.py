#9. Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect cubes, or perfect fifth powers.

def is_perfect_power(n, k):
    # Check if n is a perfect kth power
    root = round(n**(1/k))
    return root**k == n

# Initialize count to 0
count = 0

# Iterate over all integers from 1 to 1000
for i in range(1, 1001):
    # Check if i is a perfect square, cube, or fifth power
    if is_perfect_power(i, 2) or is_perfect_power(i, 3) or is_perfect_power(i, 5):
        continue
    else:
        count += 1

# Print the count of non-perfect squares, cubes, and fifth powers
print("There are", count, "integers from 1 to 1000 that are not perfect squares, perfect cubes, or perfect fifth powers.")
